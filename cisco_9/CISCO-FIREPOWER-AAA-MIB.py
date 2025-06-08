# SNMP MIB module (CISCO-FIREPOWER-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AAA-MIB.mib
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprAaaAccess,
 CfprAaaAccountStatus,
 CfprAaaAuthRealmFsmCurrentFsm,
 CfprAaaAuthRealmFsmStageName,
 CfprAaaCimcSessionType,
 CfprAaaCipherMode,
 CfprAaaClear,
 CfprAaaConfigState,
 CfprAaaDomainAuthRealm,
 CfprAaaEpAccess,
 CfprAaaEpFsmCurrentFsm,
 CfprAaaEpFsmStageName,
 CfprAaaEpFsmTaskItem,
 CfprAaaExtMgmtAccess,
 CfprAaaFqdnEnforceType,
 CfprAaaIpmiOverLan,
 CfprAaaLdapEpFsmCurrentFsm,
 CfprAaaLdapEpFsmStageName,
 CfprAaaLdapGroupRuleAuthorization,
 CfprAaaLdapGroupRuleTraversal,
 CfprAaaLdapVendor,
 CfprAaaNoRolePolicy,
 CfprAaaPwdPolicy,
 CfprAaaRadiusEpFsmCurrentFsm,
 CfprAaaRadiusEpFsmStageName,
 CfprAaaRadiusService,
 CfprAaaRealm,
 CfprAaaRealmFsmCurrentFsm,
 CfprAaaRealmFsmStageName,
 CfprAaaRealmFsmTaskItem,
 CfprAaaRevokePolicy,
 CfprAaaSession,
 CfprAaaSessionState,
 CfprAaaSshStr,
 CfprAaaSsoEpFsmCurrentFsm,
 CfprAaaSsoEpFsmStageName,
 CfprAaaTacacsPlusEpFsmCurrentFsm,
 CfprAaaTacacsPlusEpFsmStageName,
 CfprAaaUserEpFsmCurrentFsm,
 CfprAaaUserEpFsmStageName,
 CfprAaaUserEpFsmTaskItem,
 CfprAaaUserInterface,
 CfprCommTlsVerType,
 CfprConditionActionIndicator,
 CfprConditionCause,
 CfprConditionCode,
 CfprConditionRemoteInvRslt,
 CfprConditionSeverity,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprNetworkSwitchId,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAaaAccess",
    "CfprAaaAccountStatus",
    "CfprAaaAuthRealmFsmCurrentFsm",
    "CfprAaaAuthRealmFsmStageName",
    "CfprAaaCimcSessionType",
    "CfprAaaCipherMode",
    "CfprAaaClear",
    "CfprAaaConfigState",
    "CfprAaaDomainAuthRealm",
    "CfprAaaEpAccess",
    "CfprAaaEpFsmCurrentFsm",
    "CfprAaaEpFsmStageName",
    "CfprAaaEpFsmTaskItem",
    "CfprAaaExtMgmtAccess",
    "CfprAaaFqdnEnforceType",
    "CfprAaaIpmiOverLan",
    "CfprAaaLdapEpFsmCurrentFsm",
    "CfprAaaLdapEpFsmStageName",
    "CfprAaaLdapGroupRuleAuthorization",
    "CfprAaaLdapGroupRuleTraversal",
    "CfprAaaLdapVendor",
    "CfprAaaNoRolePolicy",
    "CfprAaaPwdPolicy",
    "CfprAaaRadiusEpFsmCurrentFsm",
    "CfprAaaRadiusEpFsmStageName",
    "CfprAaaRadiusService",
    "CfprAaaRealm",
    "CfprAaaRealmFsmCurrentFsm",
    "CfprAaaRealmFsmStageName",
    "CfprAaaRealmFsmTaskItem",
    "CfprAaaRevokePolicy",
    "CfprAaaSession",
    "CfprAaaSessionState",
    "CfprAaaSshStr",
    "CfprAaaSsoEpFsmCurrentFsm",
    "CfprAaaSsoEpFsmStageName",
    "CfprAaaTacacsPlusEpFsmCurrentFsm",
    "CfprAaaTacacsPlusEpFsmStageName",
    "CfprAaaUserEpFsmCurrentFsm",
    "CfprAaaUserEpFsmStageName",
    "CfprAaaUserEpFsmTaskItem",
    "CfprAaaUserInterface",
    "CfprCommTlsVerType",
    "CfprConditionActionIndicator",
    "CfprConditionCause",
    "CfprConditionCode",
    "CfprConditionRemoteInvRslt",
    "CfprConditionSeverity",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprNetworkSwitchId",
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

cfprAaaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprAaaAuthRealmTable_Object = MibTable
cfprAaaAuthRealmTable = _CfprAaaAuthRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfprAaaAuthRealmTable.setStatus("current")
_CfprAaaAuthRealmEntry_Object = MibTableRow
cfprAaaAuthRealmEntry = _CfprAaaAuthRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1)
)
cfprAaaAuthRealmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaAuthRealmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaAuthRealmEntry.setStatus("current")
_CfprAaaAuthRealmInstanceId_Type = CfprManagedObjectId
_CfprAaaAuthRealmInstanceId_Object = MibTableColumn
cfprAaaAuthRealmInstanceId = _CfprAaaAuthRealmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 1),
    _CfprAaaAuthRealmInstanceId_Type()
)
cfprAaaAuthRealmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmInstanceId.setStatus("current")
_CfprAaaAuthRealmDn_Type = CfprManagedObjectDn
_CfprAaaAuthRealmDn_Object = MibTableColumn
cfprAaaAuthRealmDn = _CfprAaaAuthRealmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 2),
    _CfprAaaAuthRealmDn_Type()
)
cfprAaaAuthRealmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmDn.setStatus("current")
_CfprAaaAuthRealmRn_Type = SnmpAdminString
_CfprAaaAuthRealmRn_Object = MibTableColumn
cfprAaaAuthRealmRn = _CfprAaaAuthRealmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 3),
    _CfprAaaAuthRealmRn_Type()
)
cfprAaaAuthRealmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmRn.setStatus("current")
_CfprAaaAuthRealmConLogin_Type = CfprAaaRealm
_CfprAaaAuthRealmConLogin_Object = MibTableColumn
cfprAaaAuthRealmConLogin = _CfprAaaAuthRealmConLogin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 4),
    _CfprAaaAuthRealmConLogin_Type()
)
cfprAaaAuthRealmConLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmConLogin.setStatus("current")
_CfprAaaAuthRealmDefLogin_Type = CfprAaaRealm
_CfprAaaAuthRealmDefLogin_Object = MibTableColumn
cfprAaaAuthRealmDefLogin = _CfprAaaAuthRealmDefLogin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 5),
    _CfprAaaAuthRealmDefLogin_Type()
)
cfprAaaAuthRealmDefLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmDefLogin.setStatus("current")
_CfprAaaAuthRealmDefRolePolicy_Type = CfprAaaNoRolePolicy
_CfprAaaAuthRealmDefRolePolicy_Object = MibTableColumn
cfprAaaAuthRealmDefRolePolicy = _CfprAaaAuthRealmDefRolePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 6),
    _CfprAaaAuthRealmDefRolePolicy_Type()
)
cfprAaaAuthRealmDefRolePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmDefRolePolicy.setStatus("current")
_CfprAaaAuthRealmDescr_Type = SnmpAdminString
_CfprAaaAuthRealmDescr_Object = MibTableColumn
cfprAaaAuthRealmDescr = _CfprAaaAuthRealmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 7),
    _CfprAaaAuthRealmDescr_Type()
)
cfprAaaAuthRealmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmDescr.setStatus("current")
_CfprAaaAuthRealmFsmDescr_Type = SnmpAdminString
_CfprAaaAuthRealmFsmDescr_Object = MibTableColumn
cfprAaaAuthRealmFsmDescr = _CfprAaaAuthRealmFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 8),
    _CfprAaaAuthRealmFsmDescr_Type()
)
cfprAaaAuthRealmFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmDescr.setStatus("current")
_CfprAaaAuthRealmFsmPrev_Type = SnmpAdminString
_CfprAaaAuthRealmFsmPrev_Object = MibTableColumn
cfprAaaAuthRealmFsmPrev = _CfprAaaAuthRealmFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 9),
    _CfprAaaAuthRealmFsmPrev_Type()
)
cfprAaaAuthRealmFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmPrev.setStatus("current")
_CfprAaaAuthRealmFsmProgr_Type = Gauge32
_CfprAaaAuthRealmFsmProgr_Object = MibTableColumn
cfprAaaAuthRealmFsmProgr = _CfprAaaAuthRealmFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 10),
    _CfprAaaAuthRealmFsmProgr_Type()
)
cfprAaaAuthRealmFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmProgr.setStatus("current")
_CfprAaaAuthRealmFsmRmtInvErrCode_Type = Gauge32
_CfprAaaAuthRealmFsmRmtInvErrCode_Object = MibTableColumn
cfprAaaAuthRealmFsmRmtInvErrCode = _CfprAaaAuthRealmFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 11),
    _CfprAaaAuthRealmFsmRmtInvErrCode_Type()
)
cfprAaaAuthRealmFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRmtInvErrCode.setStatus("current")
_CfprAaaAuthRealmFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprAaaAuthRealmFsmRmtInvErrDescr_Object = MibTableColumn
cfprAaaAuthRealmFsmRmtInvErrDescr = _CfprAaaAuthRealmFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 12),
    _CfprAaaAuthRealmFsmRmtInvErrDescr_Type()
)
cfprAaaAuthRealmFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRmtInvErrDescr.setStatus("current")
_CfprAaaAuthRealmFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaAuthRealmFsmRmtInvRslt_Object = MibTableColumn
cfprAaaAuthRealmFsmRmtInvRslt = _CfprAaaAuthRealmFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 13),
    _CfprAaaAuthRealmFsmRmtInvRslt_Type()
)
cfprAaaAuthRealmFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRmtInvRslt.setStatus("current")
_CfprAaaAuthRealmFsmStageDescr_Type = SnmpAdminString
_CfprAaaAuthRealmFsmStageDescr_Object = MibTableColumn
cfprAaaAuthRealmFsmStageDescr = _CfprAaaAuthRealmFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 14),
    _CfprAaaAuthRealmFsmStageDescr_Type()
)
cfprAaaAuthRealmFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageDescr.setStatus("current")
_CfprAaaAuthRealmFsmStamp_Type = DateAndTime
_CfprAaaAuthRealmFsmStamp_Object = MibTableColumn
cfprAaaAuthRealmFsmStamp = _CfprAaaAuthRealmFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 15),
    _CfprAaaAuthRealmFsmStamp_Type()
)
cfprAaaAuthRealmFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStamp.setStatus("current")
_CfprAaaAuthRealmFsmStatus_Type = SnmpAdminString
_CfprAaaAuthRealmFsmStatus_Object = MibTableColumn
cfprAaaAuthRealmFsmStatus = _CfprAaaAuthRealmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 16),
    _CfprAaaAuthRealmFsmStatus_Type()
)
cfprAaaAuthRealmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStatus.setStatus("current")
_CfprAaaAuthRealmFsmTry_Type = Gauge32
_CfprAaaAuthRealmFsmTry_Object = MibTableColumn
cfprAaaAuthRealmFsmTry = _CfprAaaAuthRealmFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 17),
    _CfprAaaAuthRealmFsmTry_Type()
)
cfprAaaAuthRealmFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmTry.setStatus("current")
_CfprAaaAuthRealmIntId_Type = SnmpAdminString
_CfprAaaAuthRealmIntId_Object = MibTableColumn
cfprAaaAuthRealmIntId = _CfprAaaAuthRealmIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 18),
    _CfprAaaAuthRealmIntId_Type()
)
cfprAaaAuthRealmIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmIntId.setStatus("current")
_CfprAaaAuthRealmName_Type = SnmpAdminString
_CfprAaaAuthRealmName_Object = MibTableColumn
cfprAaaAuthRealmName = _CfprAaaAuthRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 19),
    _CfprAaaAuthRealmName_Type()
)
cfprAaaAuthRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmName.setStatus("current")
_CfprAaaAuthRealmPolicyLevel_Type = Gauge32
_CfprAaaAuthRealmPolicyLevel_Object = MibTableColumn
cfprAaaAuthRealmPolicyLevel = _CfprAaaAuthRealmPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 20),
    _CfprAaaAuthRealmPolicyLevel_Type()
)
cfprAaaAuthRealmPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmPolicyLevel.setStatus("current")
_CfprAaaAuthRealmPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaAuthRealmPolicyOwner_Object = MibTableColumn
cfprAaaAuthRealmPolicyOwner = _CfprAaaAuthRealmPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 1, 1, 21),
    _CfprAaaAuthRealmPolicyOwner_Type()
)
cfprAaaAuthRealmPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmPolicyOwner.setStatus("current")
_CfprAaaAuthRealmFsmTable_Object = MibTable
cfprAaaAuthRealmFsmTable = _CfprAaaAuthRealmFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmTable.setStatus("current")
_CfprAaaAuthRealmFsmEntry_Object = MibTableRow
cfprAaaAuthRealmFsmEntry = _CfprAaaAuthRealmFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1)
)
cfprAaaAuthRealmFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaAuthRealmFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmEntry.setStatus("current")
_CfprAaaAuthRealmFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaAuthRealmFsmInstanceId_Object = MibTableColumn
cfprAaaAuthRealmFsmInstanceId = _CfprAaaAuthRealmFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 1),
    _CfprAaaAuthRealmFsmInstanceId_Type()
)
cfprAaaAuthRealmFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmInstanceId.setStatus("current")
_CfprAaaAuthRealmFsmDn_Type = CfprManagedObjectDn
_CfprAaaAuthRealmFsmDn_Object = MibTableColumn
cfprAaaAuthRealmFsmDn = _CfprAaaAuthRealmFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 2),
    _CfprAaaAuthRealmFsmDn_Type()
)
cfprAaaAuthRealmFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmDn.setStatus("current")
_CfprAaaAuthRealmFsmRn_Type = SnmpAdminString
_CfprAaaAuthRealmFsmRn_Object = MibTableColumn
cfprAaaAuthRealmFsmRn = _CfprAaaAuthRealmFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 3),
    _CfprAaaAuthRealmFsmRn_Type()
)
cfprAaaAuthRealmFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRn.setStatus("current")
_CfprAaaAuthRealmFsmCompletionTime_Type = DateAndTime
_CfprAaaAuthRealmFsmCompletionTime_Object = MibTableColumn
cfprAaaAuthRealmFsmCompletionTime = _CfprAaaAuthRealmFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 4),
    _CfprAaaAuthRealmFsmCompletionTime_Type()
)
cfprAaaAuthRealmFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmCompletionTime.setStatus("current")
_CfprAaaAuthRealmFsmCurrentFsm_Type = CfprAaaAuthRealmFsmCurrentFsm
_CfprAaaAuthRealmFsmCurrentFsm_Object = MibTableColumn
cfprAaaAuthRealmFsmCurrentFsm = _CfprAaaAuthRealmFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 5),
    _CfprAaaAuthRealmFsmCurrentFsm_Type()
)
cfprAaaAuthRealmFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmCurrentFsm.setStatus("current")
_CfprAaaAuthRealmFsmDescrData_Type = SnmpAdminString
_CfprAaaAuthRealmFsmDescrData_Object = MibTableColumn
cfprAaaAuthRealmFsmDescrData = _CfprAaaAuthRealmFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 6),
    _CfprAaaAuthRealmFsmDescrData_Type()
)
cfprAaaAuthRealmFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmDescrData.setStatus("current")
_CfprAaaAuthRealmFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaAuthRealmFsmFsmStatus_Object = MibTableColumn
cfprAaaAuthRealmFsmFsmStatus = _CfprAaaAuthRealmFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 7),
    _CfprAaaAuthRealmFsmFsmStatus_Type()
)
cfprAaaAuthRealmFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmFsmStatus.setStatus("current")
_CfprAaaAuthRealmFsmProgress_Type = Gauge32
_CfprAaaAuthRealmFsmProgress_Object = MibTableColumn
cfprAaaAuthRealmFsmProgress = _CfprAaaAuthRealmFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 8),
    _CfprAaaAuthRealmFsmProgress_Type()
)
cfprAaaAuthRealmFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmProgress.setStatus("current")
_CfprAaaAuthRealmFsmRmtErrCode_Type = Gauge32
_CfprAaaAuthRealmFsmRmtErrCode_Object = MibTableColumn
cfprAaaAuthRealmFsmRmtErrCode = _CfprAaaAuthRealmFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 9),
    _CfprAaaAuthRealmFsmRmtErrCode_Type()
)
cfprAaaAuthRealmFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRmtErrCode.setStatus("current")
_CfprAaaAuthRealmFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaAuthRealmFsmRmtErrDescr_Object = MibTableColumn
cfprAaaAuthRealmFsmRmtErrDescr = _CfprAaaAuthRealmFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 10),
    _CfprAaaAuthRealmFsmRmtErrDescr_Type()
)
cfprAaaAuthRealmFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRmtErrDescr.setStatus("current")
_CfprAaaAuthRealmFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaAuthRealmFsmRmtRslt_Object = MibTableColumn
cfprAaaAuthRealmFsmRmtRslt = _CfprAaaAuthRealmFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 2, 1, 11),
    _CfprAaaAuthRealmFsmRmtRslt_Type()
)
cfprAaaAuthRealmFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmRmtRslt.setStatus("current")
_CfprAaaAuthRealmFsmStageTable_Object = MibTable
cfprAaaAuthRealmFsmStageTable = _CfprAaaAuthRealmFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageTable.setStatus("current")
_CfprAaaAuthRealmFsmStageEntry_Object = MibTableRow
cfprAaaAuthRealmFsmStageEntry = _CfprAaaAuthRealmFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1)
)
cfprAaaAuthRealmFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaAuthRealmFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageEntry.setStatus("current")
_CfprAaaAuthRealmFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaAuthRealmFsmStageInstanceId_Object = MibTableColumn
cfprAaaAuthRealmFsmStageInstanceId = _CfprAaaAuthRealmFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 1),
    _CfprAaaAuthRealmFsmStageInstanceId_Type()
)
cfprAaaAuthRealmFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageInstanceId.setStatus("current")
_CfprAaaAuthRealmFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaAuthRealmFsmStageDn_Object = MibTableColumn
cfprAaaAuthRealmFsmStageDn = _CfprAaaAuthRealmFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 2),
    _CfprAaaAuthRealmFsmStageDn_Type()
)
cfprAaaAuthRealmFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageDn.setStatus("current")
_CfprAaaAuthRealmFsmStageRn_Type = SnmpAdminString
_CfprAaaAuthRealmFsmStageRn_Object = MibTableColumn
cfprAaaAuthRealmFsmStageRn = _CfprAaaAuthRealmFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 3),
    _CfprAaaAuthRealmFsmStageRn_Type()
)
cfprAaaAuthRealmFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageRn.setStatus("current")
_CfprAaaAuthRealmFsmStageDescrData_Type = SnmpAdminString
_CfprAaaAuthRealmFsmStageDescrData_Object = MibTableColumn
cfprAaaAuthRealmFsmStageDescrData = _CfprAaaAuthRealmFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 4),
    _CfprAaaAuthRealmFsmStageDescrData_Type()
)
cfprAaaAuthRealmFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageDescrData.setStatus("current")
_CfprAaaAuthRealmFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaAuthRealmFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaAuthRealmFsmStageLastUpdateTime = _CfprAaaAuthRealmFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 5),
    _CfprAaaAuthRealmFsmStageLastUpdateTime_Type()
)
cfprAaaAuthRealmFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageLastUpdateTime.setStatus("current")
_CfprAaaAuthRealmFsmStageName_Type = CfprAaaAuthRealmFsmStageName
_CfprAaaAuthRealmFsmStageName_Object = MibTableColumn
cfprAaaAuthRealmFsmStageName = _CfprAaaAuthRealmFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 6),
    _CfprAaaAuthRealmFsmStageName_Type()
)
cfprAaaAuthRealmFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageName.setStatus("current")
_CfprAaaAuthRealmFsmStageOrder_Type = Gauge32
_CfprAaaAuthRealmFsmStageOrder_Object = MibTableColumn
cfprAaaAuthRealmFsmStageOrder = _CfprAaaAuthRealmFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 7),
    _CfprAaaAuthRealmFsmStageOrder_Type()
)
cfprAaaAuthRealmFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageOrder.setStatus("current")
_CfprAaaAuthRealmFsmStageRetry_Type = Gauge32
_CfprAaaAuthRealmFsmStageRetry_Object = MibTableColumn
cfprAaaAuthRealmFsmStageRetry = _CfprAaaAuthRealmFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 8),
    _CfprAaaAuthRealmFsmStageRetry_Type()
)
cfprAaaAuthRealmFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageRetry.setStatus("current")
_CfprAaaAuthRealmFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaAuthRealmFsmStageStageStatus_Object = MibTableColumn
cfprAaaAuthRealmFsmStageStageStatus = _CfprAaaAuthRealmFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 3, 1, 9),
    _CfprAaaAuthRealmFsmStageStageStatus_Type()
)
cfprAaaAuthRealmFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaAuthRealmFsmStageStageStatus.setStatus("current")
_CfprAaaCimcSessionTable_Object = MibTable
cfprAaaCimcSessionTable = _CfprAaaCimcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cfprAaaCimcSessionTable.setStatus("current")
_CfprAaaCimcSessionEntry_Object = MibTableRow
cfprAaaCimcSessionEntry = _CfprAaaCimcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1)
)
cfprAaaCimcSessionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaCimcSessionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaCimcSessionEntry.setStatus("current")
_CfprAaaCimcSessionInstanceId_Type = CfprManagedObjectId
_CfprAaaCimcSessionInstanceId_Object = MibTableColumn
cfprAaaCimcSessionInstanceId = _CfprAaaCimcSessionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 1),
    _CfprAaaCimcSessionInstanceId_Type()
)
cfprAaaCimcSessionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionInstanceId.setStatus("current")
_CfprAaaCimcSessionDn_Type = CfprManagedObjectDn
_CfprAaaCimcSessionDn_Object = MibTableColumn
cfprAaaCimcSessionDn = _CfprAaaCimcSessionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 2),
    _CfprAaaCimcSessionDn_Type()
)
cfprAaaCimcSessionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionDn.setStatus("current")
_CfprAaaCimcSessionRn_Type = SnmpAdminString
_CfprAaaCimcSessionRn_Object = MibTableColumn
cfprAaaCimcSessionRn = _CfprAaaCimcSessionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 3),
    _CfprAaaCimcSessionRn_Type()
)
cfprAaaCimcSessionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionRn.setStatus("current")
_CfprAaaCimcSessionAdminState_Type = CfprAaaSessionState
_CfprAaaCimcSessionAdminState_Object = MibTableColumn
cfprAaaCimcSessionAdminState = _CfprAaaCimcSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 4),
    _CfprAaaCimcSessionAdminState_Type()
)
cfprAaaCimcSessionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionAdminState.setStatus("current")
_CfprAaaCimcSessionCimcAddr_Type = SnmpAdminString
_CfprAaaCimcSessionCimcAddr_Object = MibTableColumn
cfprAaaCimcSessionCimcAddr = _CfprAaaCimcSessionCimcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 5),
    _CfprAaaCimcSessionCimcAddr_Type()
)
cfprAaaCimcSessionCimcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionCimcAddr.setStatus("current")
_CfprAaaCimcSessionId_Type = SnmpAdminString
_CfprAaaCimcSessionId_Object = MibTableColumn
cfprAaaCimcSessionId = _CfprAaaCimcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 6),
    _CfprAaaCimcSessionId_Type()
)
cfprAaaCimcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionId.setStatus("current")
_CfprAaaCimcSessionIntDel_Type = TruthValue
_CfprAaaCimcSessionIntDel_Object = MibTableColumn
cfprAaaCimcSessionIntDel = _CfprAaaCimcSessionIntDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 7),
    _CfprAaaCimcSessionIntDel_Type()
)
cfprAaaCimcSessionIntDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionIntDel.setStatus("current")
_CfprAaaCimcSessionIsDelete_Type = CfprAaaClear
_CfprAaaCimcSessionIsDelete_Object = MibTableColumn
cfprAaaCimcSessionIsDelete = _CfprAaaCimcSessionIsDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 8),
    _CfprAaaCimcSessionIsDelete_Type()
)
cfprAaaCimcSessionIsDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionIsDelete.setStatus("current")
_CfprAaaCimcSessionLastUpdatedTime_Type = DateAndTime
_CfprAaaCimcSessionLastUpdatedTime_Object = MibTableColumn
cfprAaaCimcSessionLastUpdatedTime = _CfprAaaCimcSessionLastUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 9),
    _CfprAaaCimcSessionLastUpdatedTime_Type()
)
cfprAaaCimcSessionLastUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionLastUpdatedTime.setStatus("current")
_CfprAaaCimcSessionLoginTime_Type = DateAndTime
_CfprAaaCimcSessionLoginTime_Object = MibTableColumn
cfprAaaCimcSessionLoginTime = _CfprAaaCimcSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 10),
    _CfprAaaCimcSessionLoginTime_Type()
)
cfprAaaCimcSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionLoginTime.setStatus("current")
_CfprAaaCimcSessionLsDn_Type = SnmpAdminString
_CfprAaaCimcSessionLsDn_Object = MibTableColumn
cfprAaaCimcSessionLsDn = _CfprAaaCimcSessionLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 11),
    _CfprAaaCimcSessionLsDn_Type()
)
cfprAaaCimcSessionLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionLsDn.setStatus("current")
_CfprAaaCimcSessionPid_Type = Gauge32
_CfprAaaCimcSessionPid_Object = MibTableColumn
cfprAaaCimcSessionPid = _CfprAaaCimcSessionPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 12),
    _CfprAaaCimcSessionPid_Type()
)
cfprAaaCimcSessionPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionPid.setStatus("current")
_CfprAaaCimcSessionPnDn_Type = SnmpAdminString
_CfprAaaCimcSessionPnDn_Object = MibTableColumn
cfprAaaCimcSessionPnDn = _CfprAaaCimcSessionPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 13),
    _CfprAaaCimcSessionPnDn_Type()
)
cfprAaaCimcSessionPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionPnDn.setStatus("current")
_CfprAaaCimcSessionPriv_Type = SnmpAdminString
_CfprAaaCimcSessionPriv_Object = MibTableColumn
cfprAaaCimcSessionPriv = _CfprAaaCimcSessionPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 14),
    _CfprAaaCimcSessionPriv_Type()
)
cfprAaaCimcSessionPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionPriv.setStatus("current")
_CfprAaaCimcSessionSourceAddr_Type = SnmpAdminString
_CfprAaaCimcSessionSourceAddr_Object = MibTableColumn
cfprAaaCimcSessionSourceAddr = _CfprAaaCimcSessionSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 15),
    _CfprAaaCimcSessionSourceAddr_Type()
)
cfprAaaCimcSessionSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionSourceAddr.setStatus("current")
_CfprAaaCimcSessionType_Type = CfprAaaCimcSessionType
_CfprAaaCimcSessionType_Object = MibTableColumn
cfprAaaCimcSessionType = _CfprAaaCimcSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 16),
    _CfprAaaCimcSessionType_Type()
)
cfprAaaCimcSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionType.setStatus("current")
_CfprAaaCimcSessionUser_Type = SnmpAdminString
_CfprAaaCimcSessionUser_Object = MibTableColumn
cfprAaaCimcSessionUser = _CfprAaaCimcSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 4, 1, 17),
    _CfprAaaCimcSessionUser_Type()
)
cfprAaaCimcSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaCimcSessionUser.setStatus("current")
_CfprAaaConsoleAuthTable_Object = MibTable
cfprAaaConsoleAuthTable = _CfprAaaConsoleAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthTable.setStatus("current")
_CfprAaaConsoleAuthEntry_Object = MibTableRow
cfprAaaConsoleAuthEntry = _CfprAaaConsoleAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1)
)
cfprAaaConsoleAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaConsoleAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthEntry.setStatus("current")
_CfprAaaConsoleAuthInstanceId_Type = CfprManagedObjectId
_CfprAaaConsoleAuthInstanceId_Object = MibTableColumn
cfprAaaConsoleAuthInstanceId = _CfprAaaConsoleAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 1),
    _CfprAaaConsoleAuthInstanceId_Type()
)
cfprAaaConsoleAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthInstanceId.setStatus("current")
_CfprAaaConsoleAuthDn_Type = CfprManagedObjectDn
_CfprAaaConsoleAuthDn_Object = MibTableColumn
cfprAaaConsoleAuthDn = _CfprAaaConsoleAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 2),
    _CfprAaaConsoleAuthDn_Type()
)
cfprAaaConsoleAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthDn.setStatus("current")
_CfprAaaConsoleAuthRn_Type = SnmpAdminString
_CfprAaaConsoleAuthRn_Object = MibTableColumn
cfprAaaConsoleAuthRn = _CfprAaaConsoleAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 3),
    _CfprAaaConsoleAuthRn_Type()
)
cfprAaaConsoleAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthRn.setStatus("current")
_CfprAaaConsoleAuthDescr_Type = SnmpAdminString
_CfprAaaConsoleAuthDescr_Object = MibTableColumn
cfprAaaConsoleAuthDescr = _CfprAaaConsoleAuthDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 4),
    _CfprAaaConsoleAuthDescr_Type()
)
cfprAaaConsoleAuthDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthDescr.setStatus("current")
_CfprAaaConsoleAuthName_Type = SnmpAdminString
_CfprAaaConsoleAuthName_Object = MibTableColumn
cfprAaaConsoleAuthName = _CfprAaaConsoleAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 5),
    _CfprAaaConsoleAuthName_Type()
)
cfprAaaConsoleAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthName.setStatus("current")
_CfprAaaConsoleAuthOperProviderGroup_Type = SnmpAdminString
_CfprAaaConsoleAuthOperProviderGroup_Object = MibTableColumn
cfprAaaConsoleAuthOperProviderGroup = _CfprAaaConsoleAuthOperProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 6),
    _CfprAaaConsoleAuthOperProviderGroup_Type()
)
cfprAaaConsoleAuthOperProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthOperProviderGroup.setStatus("current")
_CfprAaaConsoleAuthOperRealm_Type = CfprAaaRealm
_CfprAaaConsoleAuthOperRealm_Object = MibTableColumn
cfprAaaConsoleAuthOperRealm = _CfprAaaConsoleAuthOperRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 7),
    _CfprAaaConsoleAuthOperRealm_Type()
)
cfprAaaConsoleAuthOperRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthOperRealm.setStatus("current")
_CfprAaaConsoleAuthProviderGroup_Type = SnmpAdminString
_CfprAaaConsoleAuthProviderGroup_Object = MibTableColumn
cfprAaaConsoleAuthProviderGroup = _CfprAaaConsoleAuthProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 8),
    _CfprAaaConsoleAuthProviderGroup_Type()
)
cfprAaaConsoleAuthProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthProviderGroup.setStatus("current")
_CfprAaaConsoleAuthRealm_Type = CfprAaaRealm
_CfprAaaConsoleAuthRealm_Object = MibTableColumn
cfprAaaConsoleAuthRealm = _CfprAaaConsoleAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 9),
    _CfprAaaConsoleAuthRealm_Type()
)
cfprAaaConsoleAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthRealm.setStatus("current")
_CfprAaaConsoleAuthUse2Factor_Type = TruthValue
_CfprAaaConsoleAuthUse2Factor_Object = MibTableColumn
cfprAaaConsoleAuthUse2Factor = _CfprAaaConsoleAuthUse2Factor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 5, 1, 10),
    _CfprAaaConsoleAuthUse2Factor_Type()
)
cfprAaaConsoleAuthUse2Factor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaConsoleAuthUse2Factor.setStatus("current")
_CfprAaaDefaultAuthTable_Object = MibTable
cfprAaaDefaultAuthTable = _CfprAaaDefaultAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthTable.setStatus("current")
_CfprAaaDefaultAuthEntry_Object = MibTableRow
cfprAaaDefaultAuthEntry = _CfprAaaDefaultAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1)
)
cfprAaaDefaultAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaDefaultAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthEntry.setStatus("current")
_CfprAaaDefaultAuthInstanceId_Type = CfprManagedObjectId
_CfprAaaDefaultAuthInstanceId_Object = MibTableColumn
cfprAaaDefaultAuthInstanceId = _CfprAaaDefaultAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 1),
    _CfprAaaDefaultAuthInstanceId_Type()
)
cfprAaaDefaultAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthInstanceId.setStatus("current")
_CfprAaaDefaultAuthDn_Type = CfprManagedObjectDn
_CfprAaaDefaultAuthDn_Object = MibTableColumn
cfprAaaDefaultAuthDn = _CfprAaaDefaultAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 2),
    _CfprAaaDefaultAuthDn_Type()
)
cfprAaaDefaultAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthDn.setStatus("current")
_CfprAaaDefaultAuthRn_Type = SnmpAdminString
_CfprAaaDefaultAuthRn_Object = MibTableColumn
cfprAaaDefaultAuthRn = _CfprAaaDefaultAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 3),
    _CfprAaaDefaultAuthRn_Type()
)
cfprAaaDefaultAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthRn.setStatus("current")
_CfprAaaDefaultAuthDescr_Type = SnmpAdminString
_CfprAaaDefaultAuthDescr_Object = MibTableColumn
cfprAaaDefaultAuthDescr = _CfprAaaDefaultAuthDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 4),
    _CfprAaaDefaultAuthDescr_Type()
)
cfprAaaDefaultAuthDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthDescr.setStatus("current")
_CfprAaaDefaultAuthName_Type = SnmpAdminString
_CfprAaaDefaultAuthName_Object = MibTableColumn
cfprAaaDefaultAuthName = _CfprAaaDefaultAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 5),
    _CfprAaaDefaultAuthName_Type()
)
cfprAaaDefaultAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthName.setStatus("current")
_CfprAaaDefaultAuthOperProviderGroup_Type = SnmpAdminString
_CfprAaaDefaultAuthOperProviderGroup_Object = MibTableColumn
cfprAaaDefaultAuthOperProviderGroup = _CfprAaaDefaultAuthOperProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 6),
    _CfprAaaDefaultAuthOperProviderGroup_Type()
)
cfprAaaDefaultAuthOperProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthOperProviderGroup.setStatus("current")
_CfprAaaDefaultAuthOperRealm_Type = CfprAaaRealm
_CfprAaaDefaultAuthOperRealm_Object = MibTableColumn
cfprAaaDefaultAuthOperRealm = _CfprAaaDefaultAuthOperRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 7),
    _CfprAaaDefaultAuthOperRealm_Type()
)
cfprAaaDefaultAuthOperRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthOperRealm.setStatus("current")
_CfprAaaDefaultAuthProviderGroup_Type = SnmpAdminString
_CfprAaaDefaultAuthProviderGroup_Object = MibTableColumn
cfprAaaDefaultAuthProviderGroup = _CfprAaaDefaultAuthProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 8),
    _CfprAaaDefaultAuthProviderGroup_Type()
)
cfprAaaDefaultAuthProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthProviderGroup.setStatus("current")
_CfprAaaDefaultAuthRealm_Type = CfprAaaRealm
_CfprAaaDefaultAuthRealm_Object = MibTableColumn
cfprAaaDefaultAuthRealm = _CfprAaaDefaultAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 9),
    _CfprAaaDefaultAuthRealm_Type()
)
cfprAaaDefaultAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthRealm.setStatus("current")
_CfprAaaDefaultAuthRefreshPeriod_Type = Gauge32
_CfprAaaDefaultAuthRefreshPeriod_Object = MibTableColumn
cfprAaaDefaultAuthRefreshPeriod = _CfprAaaDefaultAuthRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 10),
    _CfprAaaDefaultAuthRefreshPeriod_Type()
)
cfprAaaDefaultAuthRefreshPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthRefreshPeriod.setStatus("current")
_CfprAaaDefaultAuthSessionTimeout_Type = Gauge32
_CfprAaaDefaultAuthSessionTimeout_Object = MibTableColumn
cfprAaaDefaultAuthSessionTimeout = _CfprAaaDefaultAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 11),
    _CfprAaaDefaultAuthSessionTimeout_Type()
)
cfprAaaDefaultAuthSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthSessionTimeout.setStatus("current")
_CfprAaaDefaultAuthUse2Factor_Type = TruthValue
_CfprAaaDefaultAuthUse2Factor_Object = MibTableColumn
cfprAaaDefaultAuthUse2Factor = _CfprAaaDefaultAuthUse2Factor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 12),
    _CfprAaaDefaultAuthUse2Factor_Type()
)
cfprAaaDefaultAuthUse2Factor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthUse2Factor.setStatus("current")
_CfprAaaDefaultAuthAbsoluteSessionTimeout_Type = Gauge32
_CfprAaaDefaultAuthAbsoluteSessionTimeout_Object = MibTableColumn
cfprAaaDefaultAuthAbsoluteSessionTimeout = _CfprAaaDefaultAuthAbsoluteSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 13),
    _CfprAaaDefaultAuthAbsoluteSessionTimeout_Type()
)
cfprAaaDefaultAuthAbsoluteSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthAbsoluteSessionTimeout.setStatus("current")
_CfprAaaDefaultAuthConAbsoluteSessionTimeout_Type = Gauge32
_CfprAaaDefaultAuthConAbsoluteSessionTimeout_Object = MibTableColumn
cfprAaaDefaultAuthConAbsoluteSessionTimeout = _CfprAaaDefaultAuthConAbsoluteSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 14),
    _CfprAaaDefaultAuthConAbsoluteSessionTimeout_Type()
)
cfprAaaDefaultAuthConAbsoluteSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthConAbsoluteSessionTimeout.setStatus("current")
_CfprAaaDefaultAuthConSessionTimeout_Type = Gauge32
_CfprAaaDefaultAuthConSessionTimeout_Object = MibTableColumn
cfprAaaDefaultAuthConSessionTimeout = _CfprAaaDefaultAuthConSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 6, 1, 15),
    _CfprAaaDefaultAuthConSessionTimeout_Type()
)
cfprAaaDefaultAuthConSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDefaultAuthConSessionTimeout.setStatus("current")
_CfprAaaDomainTable_Object = MibTable
cfprAaaDomainTable = _CfprAaaDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cfprAaaDomainTable.setStatus("current")
_CfprAaaDomainEntry_Object = MibTableRow
cfprAaaDomainEntry = _CfprAaaDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1)
)
cfprAaaDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaDomainEntry.setStatus("current")
_CfprAaaDomainInstanceId_Type = CfprManagedObjectId
_CfprAaaDomainInstanceId_Object = MibTableColumn
cfprAaaDomainInstanceId = _CfprAaaDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 1),
    _CfprAaaDomainInstanceId_Type()
)
cfprAaaDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaDomainInstanceId.setStatus("current")
_CfprAaaDomainDn_Type = CfprManagedObjectDn
_CfprAaaDomainDn_Object = MibTableColumn
cfprAaaDomainDn = _CfprAaaDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 2),
    _CfprAaaDomainDn_Type()
)
cfprAaaDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainDn.setStatus("current")
_CfprAaaDomainRn_Type = SnmpAdminString
_CfprAaaDomainRn_Object = MibTableColumn
cfprAaaDomainRn = _CfprAaaDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 3),
    _CfprAaaDomainRn_Type()
)
cfprAaaDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainRn.setStatus("current")
_CfprAaaDomainDescr_Type = SnmpAdminString
_CfprAaaDomainDescr_Object = MibTableColumn
cfprAaaDomainDescr = _CfprAaaDomainDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 4),
    _CfprAaaDomainDescr_Type()
)
cfprAaaDomainDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainDescr.setStatus("current")
_CfprAaaDomainName_Type = SnmpAdminString
_CfprAaaDomainName_Object = MibTableColumn
cfprAaaDomainName = _CfprAaaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 5),
    _CfprAaaDomainName_Type()
)
cfprAaaDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainName.setStatus("current")
_CfprAaaDomainRefreshPeriod_Type = Gauge32
_CfprAaaDomainRefreshPeriod_Object = MibTableColumn
cfprAaaDomainRefreshPeriod = _CfprAaaDomainRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 6),
    _CfprAaaDomainRefreshPeriod_Type()
)
cfprAaaDomainRefreshPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainRefreshPeriod.setStatus("current")
_CfprAaaDomainSessionTimeout_Type = Gauge32
_CfprAaaDomainSessionTimeout_Object = MibTableColumn
cfprAaaDomainSessionTimeout = _CfprAaaDomainSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 7),
    _CfprAaaDomainSessionTimeout_Type()
)
cfprAaaDomainSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainSessionTimeout.setStatus("current")
_CfprAaaDomainAbsoluteSessionTimeout_Type = Gauge32
_CfprAaaDomainAbsoluteSessionTimeout_Object = MibTableColumn
cfprAaaDomainAbsoluteSessionTimeout = _CfprAaaDomainAbsoluteSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 8),
    _CfprAaaDomainAbsoluteSessionTimeout_Type()
)
cfprAaaDomainAbsoluteSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAbsoluteSessionTimeout.setStatus("current")
_CfprAaaDomainConAbsoluteSessionTimeout_Type = Gauge32
_CfprAaaDomainConAbsoluteSessionTimeout_Object = MibTableColumn
cfprAaaDomainConAbsoluteSessionTimeout = _CfprAaaDomainConAbsoluteSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 9),
    _CfprAaaDomainConAbsoluteSessionTimeout_Type()
)
cfprAaaDomainConAbsoluteSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainConAbsoluteSessionTimeout.setStatus("current")
_CfprAaaDomainConSessionTimeout_Type = Gauge32
_CfprAaaDomainConSessionTimeout_Object = MibTableColumn
cfprAaaDomainConSessionTimeout = _CfprAaaDomainConSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 7, 1, 10),
    _CfprAaaDomainConSessionTimeout_Type()
)
cfprAaaDomainConSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainConSessionTimeout.setStatus("current")
_CfprAaaDomainAuthTable_Object = MibTable
cfprAaaDomainAuthTable = _CfprAaaDomainAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cfprAaaDomainAuthTable.setStatus("current")
_CfprAaaDomainAuthEntry_Object = MibTableRow
cfprAaaDomainAuthEntry = _CfprAaaDomainAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1)
)
cfprAaaDomainAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaDomainAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaDomainAuthEntry.setStatus("current")
_CfprAaaDomainAuthInstanceId_Type = CfprManagedObjectId
_CfprAaaDomainAuthInstanceId_Object = MibTableColumn
cfprAaaDomainAuthInstanceId = _CfprAaaDomainAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 1),
    _CfprAaaDomainAuthInstanceId_Type()
)
cfprAaaDomainAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthInstanceId.setStatus("current")
_CfprAaaDomainAuthDn_Type = CfprManagedObjectDn
_CfprAaaDomainAuthDn_Object = MibTableColumn
cfprAaaDomainAuthDn = _CfprAaaDomainAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 2),
    _CfprAaaDomainAuthDn_Type()
)
cfprAaaDomainAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthDn.setStatus("current")
_CfprAaaDomainAuthRn_Type = SnmpAdminString
_CfprAaaDomainAuthRn_Object = MibTableColumn
cfprAaaDomainAuthRn = _CfprAaaDomainAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 3),
    _CfprAaaDomainAuthRn_Type()
)
cfprAaaDomainAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthRn.setStatus("current")
_CfprAaaDomainAuthDescr_Type = SnmpAdminString
_CfprAaaDomainAuthDescr_Object = MibTableColumn
cfprAaaDomainAuthDescr = _CfprAaaDomainAuthDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 4),
    _CfprAaaDomainAuthDescr_Type()
)
cfprAaaDomainAuthDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthDescr.setStatus("current")
_CfprAaaDomainAuthName_Type = SnmpAdminString
_CfprAaaDomainAuthName_Object = MibTableColumn
cfprAaaDomainAuthName = _CfprAaaDomainAuthName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 5),
    _CfprAaaDomainAuthName_Type()
)
cfprAaaDomainAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthName.setStatus("current")
_CfprAaaDomainAuthOperProviderGroup_Type = SnmpAdminString
_CfprAaaDomainAuthOperProviderGroup_Object = MibTableColumn
cfprAaaDomainAuthOperProviderGroup = _CfprAaaDomainAuthOperProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 6),
    _CfprAaaDomainAuthOperProviderGroup_Type()
)
cfprAaaDomainAuthOperProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthOperProviderGroup.setStatus("current")
_CfprAaaDomainAuthOperRealm_Type = CfprAaaRealm
_CfprAaaDomainAuthOperRealm_Object = MibTableColumn
cfprAaaDomainAuthOperRealm = _CfprAaaDomainAuthOperRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 7),
    _CfprAaaDomainAuthOperRealm_Type()
)
cfprAaaDomainAuthOperRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthOperRealm.setStatus("current")
_CfprAaaDomainAuthProviderGroup_Type = SnmpAdminString
_CfprAaaDomainAuthProviderGroup_Object = MibTableColumn
cfprAaaDomainAuthProviderGroup = _CfprAaaDomainAuthProviderGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 8),
    _CfprAaaDomainAuthProviderGroup_Type()
)
cfprAaaDomainAuthProviderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthProviderGroup.setStatus("current")
_CfprAaaDomainAuthRealm_Type = CfprAaaDomainAuthRealm
_CfprAaaDomainAuthRealm_Object = MibTableColumn
cfprAaaDomainAuthRealm = _CfprAaaDomainAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 9),
    _CfprAaaDomainAuthRealm_Type()
)
cfprAaaDomainAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthRealm.setStatus("current")
_CfprAaaDomainAuthUse2Factor_Type = TruthValue
_CfprAaaDomainAuthUse2Factor_Object = MibTableColumn
cfprAaaDomainAuthUse2Factor = _CfprAaaDomainAuthUse2Factor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 8, 1, 10),
    _CfprAaaDomainAuthUse2Factor_Type()
)
cfprAaaDomainAuthUse2Factor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaDomainAuthUse2Factor.setStatus("current")
_CfprAaaEpAuthProfileTable_Object = MibTable
cfprAaaEpAuthProfileTable = _CfprAaaEpAuthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileTable.setStatus("current")
_CfprAaaEpAuthProfileEntry_Object = MibTableRow
cfprAaaEpAuthProfileEntry = _CfprAaaEpAuthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1)
)
cfprAaaEpAuthProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaEpAuthProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileEntry.setStatus("current")
_CfprAaaEpAuthProfileInstanceId_Type = CfprManagedObjectId
_CfprAaaEpAuthProfileInstanceId_Object = MibTableColumn
cfprAaaEpAuthProfileInstanceId = _CfprAaaEpAuthProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 1),
    _CfprAaaEpAuthProfileInstanceId_Type()
)
cfprAaaEpAuthProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileInstanceId.setStatus("current")
_CfprAaaEpAuthProfileDn_Type = CfprManagedObjectDn
_CfprAaaEpAuthProfileDn_Object = MibTableColumn
cfprAaaEpAuthProfileDn = _CfprAaaEpAuthProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 2),
    _CfprAaaEpAuthProfileDn_Type()
)
cfprAaaEpAuthProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileDn.setStatus("current")
_CfprAaaEpAuthProfileRn_Type = SnmpAdminString
_CfprAaaEpAuthProfileRn_Object = MibTableColumn
cfprAaaEpAuthProfileRn = _CfprAaaEpAuthProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 3),
    _CfprAaaEpAuthProfileRn_Type()
)
cfprAaaEpAuthProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileRn.setStatus("current")
_CfprAaaEpAuthProfileDescr_Type = SnmpAdminString
_CfprAaaEpAuthProfileDescr_Object = MibTableColumn
cfprAaaEpAuthProfileDescr = _CfprAaaEpAuthProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 4),
    _CfprAaaEpAuthProfileDescr_Type()
)
cfprAaaEpAuthProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileDescr.setStatus("current")
_CfprAaaEpAuthProfileIntId_Type = SnmpAdminString
_CfprAaaEpAuthProfileIntId_Object = MibTableColumn
cfprAaaEpAuthProfileIntId = _CfprAaaEpAuthProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 5),
    _CfprAaaEpAuthProfileIntId_Type()
)
cfprAaaEpAuthProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileIntId.setStatus("current")
_CfprAaaEpAuthProfileIpmiOverLan_Type = CfprAaaIpmiOverLan
_CfprAaaEpAuthProfileIpmiOverLan_Object = MibTableColumn
cfprAaaEpAuthProfileIpmiOverLan = _CfprAaaEpAuthProfileIpmiOverLan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 6),
    _CfprAaaEpAuthProfileIpmiOverLan_Type()
)
cfprAaaEpAuthProfileIpmiOverLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileIpmiOverLan.setStatus("current")
_CfprAaaEpAuthProfileName_Type = SnmpAdminString
_CfprAaaEpAuthProfileName_Object = MibTableColumn
cfprAaaEpAuthProfileName = _CfprAaaEpAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 7),
    _CfprAaaEpAuthProfileName_Type()
)
cfprAaaEpAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfileName.setStatus("current")
_CfprAaaEpAuthProfilePolicyLevel_Type = Gauge32
_CfprAaaEpAuthProfilePolicyLevel_Object = MibTableColumn
cfprAaaEpAuthProfilePolicyLevel = _CfprAaaEpAuthProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 8),
    _CfprAaaEpAuthProfilePolicyLevel_Type()
)
cfprAaaEpAuthProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfilePolicyLevel.setStatus("current")
_CfprAaaEpAuthProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaEpAuthProfilePolicyOwner_Object = MibTableColumn
cfprAaaEpAuthProfilePolicyOwner = _CfprAaaEpAuthProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 9, 1, 9),
    _CfprAaaEpAuthProfilePolicyOwner_Type()
)
cfprAaaEpAuthProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpAuthProfilePolicyOwner.setStatus("current")
_CfprAaaEpFsmTable_Object = MibTable
cfprAaaEpFsmTable = _CfprAaaEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cfprAaaEpFsmTable.setStatus("current")
_CfprAaaEpFsmEntry_Object = MibTableRow
cfprAaaEpFsmEntry = _CfprAaaEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1)
)
cfprAaaEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaEpFsmEntry.setStatus("current")
_CfprAaaEpFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaEpFsmInstanceId_Object = MibTableColumn
cfprAaaEpFsmInstanceId = _CfprAaaEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 1),
    _CfprAaaEpFsmInstanceId_Type()
)
cfprAaaEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaEpFsmInstanceId.setStatus("current")
_CfprAaaEpFsmDn_Type = CfprManagedObjectDn
_CfprAaaEpFsmDn_Object = MibTableColumn
cfprAaaEpFsmDn = _CfprAaaEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 2),
    _CfprAaaEpFsmDn_Type()
)
cfprAaaEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmDn.setStatus("current")
_CfprAaaEpFsmRn_Type = SnmpAdminString
_CfprAaaEpFsmRn_Object = MibTableColumn
cfprAaaEpFsmRn = _CfprAaaEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 3),
    _CfprAaaEpFsmRn_Type()
)
cfprAaaEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmRn.setStatus("current")
_CfprAaaEpFsmCompletionTime_Type = DateAndTime
_CfprAaaEpFsmCompletionTime_Object = MibTableColumn
cfprAaaEpFsmCompletionTime = _CfprAaaEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 4),
    _CfprAaaEpFsmCompletionTime_Type()
)
cfprAaaEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmCompletionTime.setStatus("current")
_CfprAaaEpFsmCurrentFsm_Type = CfprAaaEpFsmCurrentFsm
_CfprAaaEpFsmCurrentFsm_Object = MibTableColumn
cfprAaaEpFsmCurrentFsm = _CfprAaaEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 5),
    _CfprAaaEpFsmCurrentFsm_Type()
)
cfprAaaEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmCurrentFsm.setStatus("current")
_CfprAaaEpFsmDescr_Type = SnmpAdminString
_CfprAaaEpFsmDescr_Object = MibTableColumn
cfprAaaEpFsmDescr = _CfprAaaEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 6),
    _CfprAaaEpFsmDescr_Type()
)
cfprAaaEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmDescr.setStatus("current")
_CfprAaaEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaEpFsmFsmStatus_Object = MibTableColumn
cfprAaaEpFsmFsmStatus = _CfprAaaEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 7),
    _CfprAaaEpFsmFsmStatus_Type()
)
cfprAaaEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmFsmStatus.setStatus("current")
_CfprAaaEpFsmProgress_Type = Gauge32
_CfprAaaEpFsmProgress_Object = MibTableColumn
cfprAaaEpFsmProgress = _CfprAaaEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 8),
    _CfprAaaEpFsmProgress_Type()
)
cfprAaaEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmProgress.setStatus("current")
_CfprAaaEpFsmRmtErrCode_Type = Gauge32
_CfprAaaEpFsmRmtErrCode_Object = MibTableColumn
cfprAaaEpFsmRmtErrCode = _CfprAaaEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 9),
    _CfprAaaEpFsmRmtErrCode_Type()
)
cfprAaaEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmRmtErrCode.setStatus("current")
_CfprAaaEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaEpFsmRmtErrDescr_Object = MibTableColumn
cfprAaaEpFsmRmtErrDescr = _CfprAaaEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 10),
    _CfprAaaEpFsmRmtErrDescr_Type()
)
cfprAaaEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmRmtErrDescr.setStatus("current")
_CfprAaaEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaEpFsmRmtRslt_Object = MibTableColumn
cfprAaaEpFsmRmtRslt = _CfprAaaEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 10, 1, 11),
    _CfprAaaEpFsmRmtRslt_Type()
)
cfprAaaEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmRmtRslt.setStatus("current")
_CfprAaaEpFsmStageTable_Object = MibTable
cfprAaaEpFsmStageTable = _CfprAaaEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageTable.setStatus("current")
_CfprAaaEpFsmStageEntry_Object = MibTableRow
cfprAaaEpFsmStageEntry = _CfprAaaEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1)
)
cfprAaaEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageEntry.setStatus("current")
_CfprAaaEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaEpFsmStageInstanceId_Object = MibTableColumn
cfprAaaEpFsmStageInstanceId = _CfprAaaEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 1),
    _CfprAaaEpFsmStageInstanceId_Type()
)
cfprAaaEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageInstanceId.setStatus("current")
_CfprAaaEpFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaEpFsmStageDn_Object = MibTableColumn
cfprAaaEpFsmStageDn = _CfprAaaEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 2),
    _CfprAaaEpFsmStageDn_Type()
)
cfprAaaEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageDn.setStatus("current")
_CfprAaaEpFsmStageRn_Type = SnmpAdminString
_CfprAaaEpFsmStageRn_Object = MibTableColumn
cfprAaaEpFsmStageRn = _CfprAaaEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 3),
    _CfprAaaEpFsmStageRn_Type()
)
cfprAaaEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageRn.setStatus("current")
_CfprAaaEpFsmStageDescr_Type = SnmpAdminString
_CfprAaaEpFsmStageDescr_Object = MibTableColumn
cfprAaaEpFsmStageDescr = _CfprAaaEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 4),
    _CfprAaaEpFsmStageDescr_Type()
)
cfprAaaEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageDescr.setStatus("current")
_CfprAaaEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaEpFsmStageLastUpdateTime = _CfprAaaEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 5),
    _CfprAaaEpFsmStageLastUpdateTime_Type()
)
cfprAaaEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageLastUpdateTime.setStatus("current")
_CfprAaaEpFsmStageName_Type = CfprAaaEpFsmStageName
_CfprAaaEpFsmStageName_Object = MibTableColumn
cfprAaaEpFsmStageName = _CfprAaaEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 6),
    _CfprAaaEpFsmStageName_Type()
)
cfprAaaEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageName.setStatus("current")
_CfprAaaEpFsmStageOrder_Type = Gauge32
_CfprAaaEpFsmStageOrder_Object = MibTableColumn
cfprAaaEpFsmStageOrder = _CfprAaaEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 7),
    _CfprAaaEpFsmStageOrder_Type()
)
cfprAaaEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageOrder.setStatus("current")
_CfprAaaEpFsmStageRetry_Type = Gauge32
_CfprAaaEpFsmStageRetry_Object = MibTableColumn
cfprAaaEpFsmStageRetry = _CfprAaaEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 8),
    _CfprAaaEpFsmStageRetry_Type()
)
cfprAaaEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageRetry.setStatus("current")
_CfprAaaEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaEpFsmStageStageStatus_Object = MibTableColumn
cfprAaaEpFsmStageStageStatus = _CfprAaaEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 11, 1, 9),
    _CfprAaaEpFsmStageStageStatus_Type()
)
cfprAaaEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmStageStageStatus.setStatus("current")
_CfprAaaEpFsmTaskTable_Object = MibTable
cfprAaaEpFsmTaskTable = _CfprAaaEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskTable.setStatus("current")
_CfprAaaEpFsmTaskEntry_Object = MibTableRow
cfprAaaEpFsmTaskEntry = _CfprAaaEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1)
)
cfprAaaEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskEntry.setStatus("current")
_CfprAaaEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprAaaEpFsmTaskInstanceId_Object = MibTableColumn
cfprAaaEpFsmTaskInstanceId = _CfprAaaEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 1),
    _CfprAaaEpFsmTaskInstanceId_Type()
)
cfprAaaEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskInstanceId.setStatus("current")
_CfprAaaEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprAaaEpFsmTaskDn_Object = MibTableColumn
cfprAaaEpFsmTaskDn = _CfprAaaEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 2),
    _CfprAaaEpFsmTaskDn_Type()
)
cfprAaaEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskDn.setStatus("current")
_CfprAaaEpFsmTaskRn_Type = SnmpAdminString
_CfprAaaEpFsmTaskRn_Object = MibTableColumn
cfprAaaEpFsmTaskRn = _CfprAaaEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 3),
    _CfprAaaEpFsmTaskRn_Type()
)
cfprAaaEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskRn.setStatus("current")
_CfprAaaEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprAaaEpFsmTaskCompletion_Object = MibTableColumn
cfprAaaEpFsmTaskCompletion = _CfprAaaEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 4),
    _CfprAaaEpFsmTaskCompletion_Type()
)
cfprAaaEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskCompletion.setStatus("current")
_CfprAaaEpFsmTaskFlags_Type = CfprFsmFlags
_CfprAaaEpFsmTaskFlags_Object = MibTableColumn
cfprAaaEpFsmTaskFlags = _CfprAaaEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 5),
    _CfprAaaEpFsmTaskFlags_Type()
)
cfprAaaEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskFlags.setStatus("current")
_CfprAaaEpFsmTaskItem_Type = CfprAaaEpFsmTaskItem
_CfprAaaEpFsmTaskItem_Object = MibTableColumn
cfprAaaEpFsmTaskItem = _CfprAaaEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 6),
    _CfprAaaEpFsmTaskItem_Type()
)
cfprAaaEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskItem.setStatus("current")
_CfprAaaEpFsmTaskSeqId_Type = Gauge32
_CfprAaaEpFsmTaskSeqId_Object = MibTableColumn
cfprAaaEpFsmTaskSeqId = _CfprAaaEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 12, 1, 7),
    _CfprAaaEpFsmTaskSeqId_Type()
)
cfprAaaEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpFsmTaskSeqId.setStatus("current")
_CfprAaaEpLoginTable_Object = MibTable
cfprAaaEpLoginTable = _CfprAaaEpLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cfprAaaEpLoginTable.setStatus("current")
_CfprAaaEpLoginEntry_Object = MibTableRow
cfprAaaEpLoginEntry = _CfprAaaEpLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1)
)
cfprAaaEpLoginEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaEpLoginInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaEpLoginEntry.setStatus("current")
_CfprAaaEpLoginInstanceId_Type = CfprManagedObjectId
_CfprAaaEpLoginInstanceId_Object = MibTableColumn
cfprAaaEpLoginInstanceId = _CfprAaaEpLoginInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 1),
    _CfprAaaEpLoginInstanceId_Type()
)
cfprAaaEpLoginInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaEpLoginInstanceId.setStatus("current")
_CfprAaaEpLoginDn_Type = CfprManagedObjectDn
_CfprAaaEpLoginDn_Object = MibTableColumn
cfprAaaEpLoginDn = _CfprAaaEpLoginDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 2),
    _CfprAaaEpLoginDn_Type()
)
cfprAaaEpLoginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginDn.setStatus("current")
_CfprAaaEpLoginRn_Type = SnmpAdminString
_CfprAaaEpLoginRn_Object = MibTableColumn
cfprAaaEpLoginRn = _CfprAaaEpLoginRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 3),
    _CfprAaaEpLoginRn_Type()
)
cfprAaaEpLoginRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginRn.setStatus("current")
_CfprAaaEpLoginDescr_Type = SnmpAdminString
_CfprAaaEpLoginDescr_Object = MibTableColumn
cfprAaaEpLoginDescr = _CfprAaaEpLoginDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 4),
    _CfprAaaEpLoginDescr_Type()
)
cfprAaaEpLoginDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginDescr.setStatus("current")
_CfprAaaEpLoginId_Type = SnmpAdminString
_CfprAaaEpLoginId_Object = MibTableColumn
cfprAaaEpLoginId = _CfprAaaEpLoginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 5),
    _CfprAaaEpLoginId_Type()
)
cfprAaaEpLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginId.setStatus("current")
_CfprAaaEpLoginIntId_Type = SnmpAdminString
_CfprAaaEpLoginIntId_Object = MibTableColumn
cfprAaaEpLoginIntId = _CfprAaaEpLoginIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 6),
    _CfprAaaEpLoginIntId_Type()
)
cfprAaaEpLoginIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginIntId.setStatus("current")
_CfprAaaEpLoginLocalHost_Type = SnmpAdminString
_CfprAaaEpLoginLocalHost_Object = MibTableColumn
cfprAaaEpLoginLocalHost = _CfprAaaEpLoginLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 7),
    _CfprAaaEpLoginLocalHost_Type()
)
cfprAaaEpLoginLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginLocalHost.setStatus("current")
_CfprAaaEpLoginName_Type = SnmpAdminString
_CfprAaaEpLoginName_Object = MibTableColumn
cfprAaaEpLoginName = _CfprAaaEpLoginName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 8),
    _CfprAaaEpLoginName_Type()
)
cfprAaaEpLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginName.setStatus("current")
_CfprAaaEpLoginPolicyLevel_Type = Gauge32
_CfprAaaEpLoginPolicyLevel_Object = MibTableColumn
cfprAaaEpLoginPolicyLevel = _CfprAaaEpLoginPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 9),
    _CfprAaaEpLoginPolicyLevel_Type()
)
cfprAaaEpLoginPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginPolicyLevel.setStatus("current")
_CfprAaaEpLoginPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaEpLoginPolicyOwner_Object = MibTableColumn
cfprAaaEpLoginPolicyOwner = _CfprAaaEpLoginPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 10),
    _CfprAaaEpLoginPolicyOwner_Type()
)
cfprAaaEpLoginPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginPolicyOwner.setStatus("current")
_CfprAaaEpLoginRemoteHost_Type = SnmpAdminString
_CfprAaaEpLoginRemoteHost_Object = MibTableColumn
cfprAaaEpLoginRemoteHost = _CfprAaaEpLoginRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 11),
    _CfprAaaEpLoginRemoteHost_Type()
)
cfprAaaEpLoginRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginRemoteHost.setStatus("current")
_CfprAaaEpLoginSession_Type = CfprAaaSession
_CfprAaaEpLoginSession_Object = MibTableColumn
cfprAaaEpLoginSession = _CfprAaaEpLoginSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 12),
    _CfprAaaEpLoginSession_Type()
)
cfprAaaEpLoginSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginSession.setStatus("current")
_CfprAaaEpLoginSwitchId_Type = CfprNetworkSwitchId
_CfprAaaEpLoginSwitchId_Object = MibTableColumn
cfprAaaEpLoginSwitchId = _CfprAaaEpLoginSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 13, 1, 13),
    _CfprAaaEpLoginSwitchId_Type()
)
cfprAaaEpLoginSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpLoginSwitchId.setStatus("current")
_CfprAaaEpUserTable_Object = MibTable
cfprAaaEpUserTable = _CfprAaaEpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cfprAaaEpUserTable.setStatus("current")
_CfprAaaEpUserEntry_Object = MibTableRow
cfprAaaEpUserEntry = _CfprAaaEpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1)
)
cfprAaaEpUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaEpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaEpUserEntry.setStatus("current")
_CfprAaaEpUserInstanceId_Type = CfprManagedObjectId
_CfprAaaEpUserInstanceId_Object = MibTableColumn
cfprAaaEpUserInstanceId = _CfprAaaEpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 1),
    _CfprAaaEpUserInstanceId_Type()
)
cfprAaaEpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaEpUserInstanceId.setStatus("current")
_CfprAaaEpUserDn_Type = CfprManagedObjectDn
_CfprAaaEpUserDn_Object = MibTableColumn
cfprAaaEpUserDn = _CfprAaaEpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 2),
    _CfprAaaEpUserDn_Type()
)
cfprAaaEpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserDn.setStatus("current")
_CfprAaaEpUserRn_Type = SnmpAdminString
_CfprAaaEpUserRn_Object = MibTableColumn
cfprAaaEpUserRn = _CfprAaaEpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 3),
    _CfprAaaEpUserRn_Type()
)
cfprAaaEpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserRn.setStatus("current")
_CfprAaaEpUserConfigState_Type = CfprAaaConfigState
_CfprAaaEpUserConfigState_Object = MibTableColumn
cfprAaaEpUserConfigState = _CfprAaaEpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 4),
    _CfprAaaEpUserConfigState_Type()
)
cfprAaaEpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserConfigState.setStatus("current")
_CfprAaaEpUserConfigStatusMessage_Type = SnmpAdminString
_CfprAaaEpUserConfigStatusMessage_Object = MibTableColumn
cfprAaaEpUserConfigStatusMessage = _CfprAaaEpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 5),
    _CfprAaaEpUserConfigStatusMessage_Type()
)
cfprAaaEpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserConfigStatusMessage.setStatus("current")
_CfprAaaEpUserDescr_Type = SnmpAdminString
_CfprAaaEpUserDescr_Object = MibTableColumn
cfprAaaEpUserDescr = _CfprAaaEpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 6),
    _CfprAaaEpUserDescr_Type()
)
cfprAaaEpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserDescr.setStatus("current")
_CfprAaaEpUserName_Type = SnmpAdminString
_CfprAaaEpUserName_Object = MibTableColumn
cfprAaaEpUserName = _CfprAaaEpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 7),
    _CfprAaaEpUserName_Type()
)
cfprAaaEpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserName.setStatus("current")
_CfprAaaEpUserPriv_Type = CfprAaaEpAccess
_CfprAaaEpUserPriv_Object = MibTableColumn
cfprAaaEpUserPriv = _CfprAaaEpUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 8),
    _CfprAaaEpUserPriv_Type()
)
cfprAaaEpUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserPriv.setStatus("current")
_CfprAaaEpUserPwd_Type = SnmpAdminString
_CfprAaaEpUserPwd_Object = MibTableColumn
cfprAaaEpUserPwd = _CfprAaaEpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 9),
    _CfprAaaEpUserPwd_Type()
)
cfprAaaEpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserPwd.setStatus("current")
_CfprAaaEpUserPwdSet_Type = TruthValue
_CfprAaaEpUserPwdSet_Object = MibTableColumn
cfprAaaEpUserPwdSet = _CfprAaaEpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 14, 1, 10),
    _CfprAaaEpUserPwdSet_Type()
)
cfprAaaEpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaEpUserPwdSet.setStatus("current")
_CfprAaaExtMgmtCutThruTknTable_Object = MibTable
cfprAaaExtMgmtCutThruTknTable = _CfprAaaExtMgmtCutThruTknTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknTable.setStatus("current")
_CfprAaaExtMgmtCutThruTknEntry_Object = MibTableRow
cfprAaaExtMgmtCutThruTknEntry = _CfprAaaExtMgmtCutThruTknEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1)
)
cfprAaaExtMgmtCutThruTknEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaExtMgmtCutThruTknInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknEntry.setStatus("current")
_CfprAaaExtMgmtCutThruTknInstanceId_Type = CfprManagedObjectId
_CfprAaaExtMgmtCutThruTknInstanceId_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknInstanceId = _CfprAaaExtMgmtCutThruTknInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 1),
    _CfprAaaExtMgmtCutThruTknInstanceId_Type()
)
cfprAaaExtMgmtCutThruTknInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknInstanceId.setStatus("current")
_CfprAaaExtMgmtCutThruTknDn_Type = CfprManagedObjectDn
_CfprAaaExtMgmtCutThruTknDn_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknDn = _CfprAaaExtMgmtCutThruTknDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 2),
    _CfprAaaExtMgmtCutThruTknDn_Type()
)
cfprAaaExtMgmtCutThruTknDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknDn.setStatus("current")
_CfprAaaExtMgmtCutThruTknRn_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknRn_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknRn = _CfprAaaExtMgmtCutThruTknRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 3),
    _CfprAaaExtMgmtCutThruTknRn_Type()
)
cfprAaaExtMgmtCutThruTknRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknRn.setStatus("current")
_CfprAaaExtMgmtCutThruTknAuthDomain_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknAuthDomain_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknAuthDomain = _CfprAaaExtMgmtCutThruTknAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 4),
    _CfprAaaExtMgmtCutThruTknAuthDomain_Type()
)
cfprAaaExtMgmtCutThruTknAuthDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknAuthDomain.setStatus("current")
_CfprAaaExtMgmtCutThruTknAuthUser_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknAuthUser_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknAuthUser = _CfprAaaExtMgmtCutThruTknAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 5),
    _CfprAaaExtMgmtCutThruTknAuthUser_Type()
)
cfprAaaExtMgmtCutThruTknAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknAuthUser.setStatus("current")
_CfprAaaExtMgmtCutThruTknCreationTime_Type = DateAndTime
_CfprAaaExtMgmtCutThruTknCreationTime_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknCreationTime = _CfprAaaExtMgmtCutThruTknCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 6),
    _CfprAaaExtMgmtCutThruTknCreationTime_Type()
)
cfprAaaExtMgmtCutThruTknCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknCreationTime.setStatus("current")
_CfprAaaExtMgmtCutThruTknDescr_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknDescr_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknDescr = _CfprAaaExtMgmtCutThruTknDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 7),
    _CfprAaaExtMgmtCutThruTknDescr_Type()
)
cfprAaaExtMgmtCutThruTknDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknDescr.setStatus("current")
_CfprAaaExtMgmtCutThruTknIntId_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknIntId_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknIntId = _CfprAaaExtMgmtCutThruTknIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 8),
    _CfprAaaExtMgmtCutThruTknIntId_Type()
)
cfprAaaExtMgmtCutThruTknIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknIntId.setStatus("current")
_CfprAaaExtMgmtCutThruTknLocales_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknLocales_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknLocales = _CfprAaaExtMgmtCutThruTknLocales_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 9),
    _CfprAaaExtMgmtCutThruTknLocales_Type()
)
cfprAaaExtMgmtCutThruTknLocales.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknLocales.setStatus("current")
_CfprAaaExtMgmtCutThruTknName_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknName_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknName = _CfprAaaExtMgmtCutThruTknName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 10),
    _CfprAaaExtMgmtCutThruTknName_Type()
)
cfprAaaExtMgmtCutThruTknName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknName.setStatus("current")
_CfprAaaExtMgmtCutThruTknPnDn_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknPnDn_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknPnDn = _CfprAaaExtMgmtCutThruTknPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 11),
    _CfprAaaExtMgmtCutThruTknPnDn_Type()
)
cfprAaaExtMgmtCutThruTknPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknPnDn.setStatus("current")
_CfprAaaExtMgmtCutThruTknPolicyLevel_Type = Gauge32
_CfprAaaExtMgmtCutThruTknPolicyLevel_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknPolicyLevel = _CfprAaaExtMgmtCutThruTknPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 12),
    _CfprAaaExtMgmtCutThruTknPolicyLevel_Type()
)
cfprAaaExtMgmtCutThruTknPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknPolicyLevel.setStatus("current")
_CfprAaaExtMgmtCutThruTknPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaExtMgmtCutThruTknPolicyOwner_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknPolicyOwner = _CfprAaaExtMgmtCutThruTknPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 13),
    _CfprAaaExtMgmtCutThruTknPolicyOwner_Type()
)
cfprAaaExtMgmtCutThruTknPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknPolicyOwner.setStatus("current")
_CfprAaaExtMgmtCutThruTknPriv_Type = CfprAaaAccess
_CfprAaaExtMgmtCutThruTknPriv_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknPriv = _CfprAaaExtMgmtCutThruTknPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 14),
    _CfprAaaExtMgmtCutThruTknPriv_Type()
)
cfprAaaExtMgmtCutThruTknPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknPriv.setStatus("current")
_CfprAaaExtMgmtCutThruTknRemote_Type = TruthValue
_CfprAaaExtMgmtCutThruTknRemote_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknRemote = _CfprAaaExtMgmtCutThruTknRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 15),
    _CfprAaaExtMgmtCutThruTknRemote_Type()
)
cfprAaaExtMgmtCutThruTknRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknRemote.setStatus("current")
_CfprAaaExtMgmtCutThruTknToken_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknToken_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknToken = _CfprAaaExtMgmtCutThruTknToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 16),
    _CfprAaaExtMgmtCutThruTknToken_Type()
)
cfprAaaExtMgmtCutThruTknToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknToken.setStatus("current")
_CfprAaaExtMgmtCutThruTknType_Type = CfprAaaExtMgmtAccess
_CfprAaaExtMgmtCutThruTknType_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknType = _CfprAaaExtMgmtCutThruTknType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 17),
    _CfprAaaExtMgmtCutThruTknType_Type()
)
cfprAaaExtMgmtCutThruTknType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknType.setStatus("current")
_CfprAaaExtMgmtCutThruTknUser_Type = SnmpAdminString
_CfprAaaExtMgmtCutThruTknUser_Object = MibTableColumn
cfprAaaExtMgmtCutThruTknUser = _CfprAaaExtMgmtCutThruTknUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 15, 1, 18),
    _CfprAaaExtMgmtCutThruTknUser_Type()
)
cfprAaaExtMgmtCutThruTknUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaExtMgmtCutThruTknUser.setStatus("current")
_CfprAaaLdapEpTable_Object = MibTable
cfprAaaLdapEpTable = _CfprAaaLdapEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cfprAaaLdapEpTable.setStatus("current")
_CfprAaaLdapEpEntry_Object = MibTableRow
cfprAaaLdapEpEntry = _CfprAaaLdapEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1)
)
cfprAaaLdapEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLdapEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLdapEpEntry.setStatus("current")
_CfprAaaLdapEpInstanceId_Type = CfprManagedObjectId
_CfprAaaLdapEpInstanceId_Object = MibTableColumn
cfprAaaLdapEpInstanceId = _CfprAaaLdapEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 1),
    _CfprAaaLdapEpInstanceId_Type()
)
cfprAaaLdapEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLdapEpInstanceId.setStatus("current")
_CfprAaaLdapEpDn_Type = CfprManagedObjectDn
_CfprAaaLdapEpDn_Object = MibTableColumn
cfprAaaLdapEpDn = _CfprAaaLdapEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 2),
    _CfprAaaLdapEpDn_Type()
)
cfprAaaLdapEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpDn.setStatus("current")
_CfprAaaLdapEpRn_Type = SnmpAdminString
_CfprAaaLdapEpRn_Object = MibTableColumn
cfprAaaLdapEpRn = _CfprAaaLdapEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 3),
    _CfprAaaLdapEpRn_Type()
)
cfprAaaLdapEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpRn.setStatus("current")
_CfprAaaLdapEpAttribute_Type = SnmpAdminString
_CfprAaaLdapEpAttribute_Object = MibTableColumn
cfprAaaLdapEpAttribute = _CfprAaaLdapEpAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 4),
    _CfprAaaLdapEpAttribute_Type()
)
cfprAaaLdapEpAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpAttribute.setStatus("current")
_CfprAaaLdapEpBasedn_Type = SnmpAdminString
_CfprAaaLdapEpBasedn_Object = MibTableColumn
cfprAaaLdapEpBasedn = _CfprAaaLdapEpBasedn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 5),
    _CfprAaaLdapEpBasedn_Type()
)
cfprAaaLdapEpBasedn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpBasedn.setStatus("current")
_CfprAaaLdapEpDescr_Type = SnmpAdminString
_CfprAaaLdapEpDescr_Object = MibTableColumn
cfprAaaLdapEpDescr = _CfprAaaLdapEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 6),
    _CfprAaaLdapEpDescr_Type()
)
cfprAaaLdapEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpDescr.setStatus("current")
_CfprAaaLdapEpFilter_Type = SnmpAdminString
_CfprAaaLdapEpFilter_Object = MibTableColumn
cfprAaaLdapEpFilter = _CfprAaaLdapEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 7),
    _CfprAaaLdapEpFilter_Type()
)
cfprAaaLdapEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFilter.setStatus("current")
_CfprAaaLdapEpFsmDescr_Type = SnmpAdminString
_CfprAaaLdapEpFsmDescr_Object = MibTableColumn
cfprAaaLdapEpFsmDescr = _CfprAaaLdapEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 8),
    _CfprAaaLdapEpFsmDescr_Type()
)
cfprAaaLdapEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmDescr.setStatus("current")
_CfprAaaLdapEpFsmPrev_Type = SnmpAdminString
_CfprAaaLdapEpFsmPrev_Object = MibTableColumn
cfprAaaLdapEpFsmPrev = _CfprAaaLdapEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 9),
    _CfprAaaLdapEpFsmPrev_Type()
)
cfprAaaLdapEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmPrev.setStatus("current")
_CfprAaaLdapEpFsmProgr_Type = Gauge32
_CfprAaaLdapEpFsmProgr_Object = MibTableColumn
cfprAaaLdapEpFsmProgr = _CfprAaaLdapEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 10),
    _CfprAaaLdapEpFsmProgr_Type()
)
cfprAaaLdapEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmProgr.setStatus("current")
_CfprAaaLdapEpFsmRmtInvErrCode_Type = Gauge32
_CfprAaaLdapEpFsmRmtInvErrCode_Object = MibTableColumn
cfprAaaLdapEpFsmRmtInvErrCode = _CfprAaaLdapEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 11),
    _CfprAaaLdapEpFsmRmtInvErrCode_Type()
)
cfprAaaLdapEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRmtInvErrCode.setStatus("current")
_CfprAaaLdapEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprAaaLdapEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprAaaLdapEpFsmRmtInvErrDescr = _CfprAaaLdapEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 12),
    _CfprAaaLdapEpFsmRmtInvErrDescr_Type()
)
cfprAaaLdapEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRmtInvErrDescr.setStatus("current")
_CfprAaaLdapEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaLdapEpFsmRmtInvRslt_Object = MibTableColumn
cfprAaaLdapEpFsmRmtInvRslt = _CfprAaaLdapEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 13),
    _CfprAaaLdapEpFsmRmtInvRslt_Type()
)
cfprAaaLdapEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRmtInvRslt.setStatus("current")
_CfprAaaLdapEpFsmStageDescr_Type = SnmpAdminString
_CfprAaaLdapEpFsmStageDescr_Object = MibTableColumn
cfprAaaLdapEpFsmStageDescr = _CfprAaaLdapEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 14),
    _CfprAaaLdapEpFsmStageDescr_Type()
)
cfprAaaLdapEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageDescr.setStatus("current")
_CfprAaaLdapEpFsmStamp_Type = DateAndTime
_CfprAaaLdapEpFsmStamp_Object = MibTableColumn
cfprAaaLdapEpFsmStamp = _CfprAaaLdapEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 15),
    _CfprAaaLdapEpFsmStamp_Type()
)
cfprAaaLdapEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStamp.setStatus("current")
_CfprAaaLdapEpFsmStatus_Type = SnmpAdminString
_CfprAaaLdapEpFsmStatus_Object = MibTableColumn
cfprAaaLdapEpFsmStatus = _CfprAaaLdapEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 16),
    _CfprAaaLdapEpFsmStatus_Type()
)
cfprAaaLdapEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStatus.setStatus("current")
_CfprAaaLdapEpFsmTry_Type = Gauge32
_CfprAaaLdapEpFsmTry_Object = MibTableColumn
cfprAaaLdapEpFsmTry = _CfprAaaLdapEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 17),
    _CfprAaaLdapEpFsmTry_Type()
)
cfprAaaLdapEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmTry.setStatus("current")
_CfprAaaLdapEpIntId_Type = SnmpAdminString
_CfprAaaLdapEpIntId_Object = MibTableColumn
cfprAaaLdapEpIntId = _CfprAaaLdapEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 18),
    _CfprAaaLdapEpIntId_Type()
)
cfprAaaLdapEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpIntId.setStatus("current")
_CfprAaaLdapEpName_Type = SnmpAdminString
_CfprAaaLdapEpName_Object = MibTableColumn
cfprAaaLdapEpName = _CfprAaaLdapEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 19),
    _CfprAaaLdapEpName_Type()
)
cfprAaaLdapEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpName.setStatus("current")
_CfprAaaLdapEpPolicyLevel_Type = Gauge32
_CfprAaaLdapEpPolicyLevel_Object = MibTableColumn
cfprAaaLdapEpPolicyLevel = _CfprAaaLdapEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 20),
    _CfprAaaLdapEpPolicyLevel_Type()
)
cfprAaaLdapEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpPolicyLevel.setStatus("current")
_CfprAaaLdapEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaLdapEpPolicyOwner_Object = MibTableColumn
cfprAaaLdapEpPolicyOwner = _CfprAaaLdapEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 21),
    _CfprAaaLdapEpPolicyOwner_Type()
)
cfprAaaLdapEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpPolicyOwner.setStatus("current")
_CfprAaaLdapEpRetries_Type = Gauge32
_CfprAaaLdapEpRetries_Object = MibTableColumn
cfprAaaLdapEpRetries = _CfprAaaLdapEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 22),
    _CfprAaaLdapEpRetries_Type()
)
cfprAaaLdapEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpRetries.setStatus("current")
_CfprAaaLdapEpTimeout_Type = Gauge32
_CfprAaaLdapEpTimeout_Object = MibTableColumn
cfprAaaLdapEpTimeout = _CfprAaaLdapEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 23),
    _CfprAaaLdapEpTimeout_Type()
)
cfprAaaLdapEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpTimeout.setStatus("current")
_CfprAaaLdapEpTlsVer_Type = CfprCommTlsVerType
_CfprAaaLdapEpTlsVer_Object = MibTableColumn
cfprAaaLdapEpTlsVer = _CfprAaaLdapEpTlsVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 16, 1, 24),
    _CfprAaaLdapEpTlsVer_Type()
)
cfprAaaLdapEpTlsVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpTlsVer.setStatus("current")
_CfprAaaLdapEpFsmTable_Object = MibTable
cfprAaaLdapEpFsmTable = _CfprAaaLdapEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmTable.setStatus("current")
_CfprAaaLdapEpFsmEntry_Object = MibTableRow
cfprAaaLdapEpFsmEntry = _CfprAaaLdapEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1)
)
cfprAaaLdapEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLdapEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmEntry.setStatus("current")
_CfprAaaLdapEpFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaLdapEpFsmInstanceId_Object = MibTableColumn
cfprAaaLdapEpFsmInstanceId = _CfprAaaLdapEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 1),
    _CfprAaaLdapEpFsmInstanceId_Type()
)
cfprAaaLdapEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmInstanceId.setStatus("current")
_CfprAaaLdapEpFsmDn_Type = CfprManagedObjectDn
_CfprAaaLdapEpFsmDn_Object = MibTableColumn
cfprAaaLdapEpFsmDn = _CfprAaaLdapEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 2),
    _CfprAaaLdapEpFsmDn_Type()
)
cfprAaaLdapEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmDn.setStatus("current")
_CfprAaaLdapEpFsmRn_Type = SnmpAdminString
_CfprAaaLdapEpFsmRn_Object = MibTableColumn
cfprAaaLdapEpFsmRn = _CfprAaaLdapEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 3),
    _CfprAaaLdapEpFsmRn_Type()
)
cfprAaaLdapEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRn.setStatus("current")
_CfprAaaLdapEpFsmCompletionTime_Type = DateAndTime
_CfprAaaLdapEpFsmCompletionTime_Object = MibTableColumn
cfprAaaLdapEpFsmCompletionTime = _CfprAaaLdapEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 4),
    _CfprAaaLdapEpFsmCompletionTime_Type()
)
cfprAaaLdapEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmCompletionTime.setStatus("current")
_CfprAaaLdapEpFsmCurrentFsm_Type = CfprAaaLdapEpFsmCurrentFsm
_CfprAaaLdapEpFsmCurrentFsm_Object = MibTableColumn
cfprAaaLdapEpFsmCurrentFsm = _CfprAaaLdapEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 5),
    _CfprAaaLdapEpFsmCurrentFsm_Type()
)
cfprAaaLdapEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmCurrentFsm.setStatus("current")
_CfprAaaLdapEpFsmDescrData_Type = SnmpAdminString
_CfprAaaLdapEpFsmDescrData_Object = MibTableColumn
cfprAaaLdapEpFsmDescrData = _CfprAaaLdapEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 6),
    _CfprAaaLdapEpFsmDescrData_Type()
)
cfprAaaLdapEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmDescrData.setStatus("current")
_CfprAaaLdapEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaLdapEpFsmFsmStatus_Object = MibTableColumn
cfprAaaLdapEpFsmFsmStatus = _CfprAaaLdapEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 7),
    _CfprAaaLdapEpFsmFsmStatus_Type()
)
cfprAaaLdapEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmFsmStatus.setStatus("current")
_CfprAaaLdapEpFsmProgress_Type = Gauge32
_CfprAaaLdapEpFsmProgress_Object = MibTableColumn
cfprAaaLdapEpFsmProgress = _CfprAaaLdapEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 8),
    _CfprAaaLdapEpFsmProgress_Type()
)
cfprAaaLdapEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmProgress.setStatus("current")
_CfprAaaLdapEpFsmRmtErrCode_Type = Gauge32
_CfprAaaLdapEpFsmRmtErrCode_Object = MibTableColumn
cfprAaaLdapEpFsmRmtErrCode = _CfprAaaLdapEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 9),
    _CfprAaaLdapEpFsmRmtErrCode_Type()
)
cfprAaaLdapEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRmtErrCode.setStatus("current")
_CfprAaaLdapEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaLdapEpFsmRmtErrDescr_Object = MibTableColumn
cfprAaaLdapEpFsmRmtErrDescr = _CfprAaaLdapEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 10),
    _CfprAaaLdapEpFsmRmtErrDescr_Type()
)
cfprAaaLdapEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRmtErrDescr.setStatus("current")
_CfprAaaLdapEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaLdapEpFsmRmtRslt_Object = MibTableColumn
cfprAaaLdapEpFsmRmtRslt = _CfprAaaLdapEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 17, 1, 11),
    _CfprAaaLdapEpFsmRmtRslt_Type()
)
cfprAaaLdapEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmRmtRslt.setStatus("current")
_CfprAaaLdapEpFsmStageTable_Object = MibTable
cfprAaaLdapEpFsmStageTable = _CfprAaaLdapEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18)
)
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageTable.setStatus("current")
_CfprAaaLdapEpFsmStageEntry_Object = MibTableRow
cfprAaaLdapEpFsmStageEntry = _CfprAaaLdapEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1)
)
cfprAaaLdapEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLdapEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageEntry.setStatus("current")
_CfprAaaLdapEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaLdapEpFsmStageInstanceId_Object = MibTableColumn
cfprAaaLdapEpFsmStageInstanceId = _CfprAaaLdapEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 1),
    _CfprAaaLdapEpFsmStageInstanceId_Type()
)
cfprAaaLdapEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageInstanceId.setStatus("current")
_CfprAaaLdapEpFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaLdapEpFsmStageDn_Object = MibTableColumn
cfprAaaLdapEpFsmStageDn = _CfprAaaLdapEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 2),
    _CfprAaaLdapEpFsmStageDn_Type()
)
cfprAaaLdapEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageDn.setStatus("current")
_CfprAaaLdapEpFsmStageRn_Type = SnmpAdminString
_CfprAaaLdapEpFsmStageRn_Object = MibTableColumn
cfprAaaLdapEpFsmStageRn = _CfprAaaLdapEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 3),
    _CfprAaaLdapEpFsmStageRn_Type()
)
cfprAaaLdapEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageRn.setStatus("current")
_CfprAaaLdapEpFsmStageDescrData_Type = SnmpAdminString
_CfprAaaLdapEpFsmStageDescrData_Object = MibTableColumn
cfprAaaLdapEpFsmStageDescrData = _CfprAaaLdapEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 4),
    _CfprAaaLdapEpFsmStageDescrData_Type()
)
cfprAaaLdapEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageDescrData.setStatus("current")
_CfprAaaLdapEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaLdapEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaLdapEpFsmStageLastUpdateTime = _CfprAaaLdapEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 5),
    _CfprAaaLdapEpFsmStageLastUpdateTime_Type()
)
cfprAaaLdapEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageLastUpdateTime.setStatus("current")
_CfprAaaLdapEpFsmStageName_Type = CfprAaaLdapEpFsmStageName
_CfprAaaLdapEpFsmStageName_Object = MibTableColumn
cfprAaaLdapEpFsmStageName = _CfprAaaLdapEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 6),
    _CfprAaaLdapEpFsmStageName_Type()
)
cfprAaaLdapEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageName.setStatus("current")
_CfprAaaLdapEpFsmStageOrder_Type = Gauge32
_CfprAaaLdapEpFsmStageOrder_Object = MibTableColumn
cfprAaaLdapEpFsmStageOrder = _CfprAaaLdapEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 7),
    _CfprAaaLdapEpFsmStageOrder_Type()
)
cfprAaaLdapEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageOrder.setStatus("current")
_CfprAaaLdapEpFsmStageRetry_Type = Gauge32
_CfprAaaLdapEpFsmStageRetry_Object = MibTableColumn
cfprAaaLdapEpFsmStageRetry = _CfprAaaLdapEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 8),
    _CfprAaaLdapEpFsmStageRetry_Type()
)
cfprAaaLdapEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageRetry.setStatus("current")
_CfprAaaLdapEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaLdapEpFsmStageStageStatus_Object = MibTableColumn
cfprAaaLdapEpFsmStageStageStatus = _CfprAaaLdapEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 18, 1, 9),
    _CfprAaaLdapEpFsmStageStageStatus_Type()
)
cfprAaaLdapEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapEpFsmStageStageStatus.setStatus("current")
_CfprAaaLdapGroupTable_Object = MibTable
cfprAaaLdapGroupTable = _CfprAaaLdapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19)
)
if mibBuilder.loadTexts:
    cfprAaaLdapGroupTable.setStatus("current")
_CfprAaaLdapGroupEntry_Object = MibTableRow
cfprAaaLdapGroupEntry = _CfprAaaLdapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19, 1)
)
cfprAaaLdapGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLdapGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLdapGroupEntry.setStatus("current")
_CfprAaaLdapGroupInstanceId_Type = CfprManagedObjectId
_CfprAaaLdapGroupInstanceId_Object = MibTableColumn
cfprAaaLdapGroupInstanceId = _CfprAaaLdapGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19, 1, 1),
    _CfprAaaLdapGroupInstanceId_Type()
)
cfprAaaLdapGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupInstanceId.setStatus("current")
_CfprAaaLdapGroupDn_Type = CfprManagedObjectDn
_CfprAaaLdapGroupDn_Object = MibTableColumn
cfprAaaLdapGroupDn = _CfprAaaLdapGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19, 1, 2),
    _CfprAaaLdapGroupDn_Type()
)
cfprAaaLdapGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupDn.setStatus("current")
_CfprAaaLdapGroupRn_Type = SnmpAdminString
_CfprAaaLdapGroupRn_Object = MibTableColumn
cfprAaaLdapGroupRn = _CfprAaaLdapGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19, 1, 3),
    _CfprAaaLdapGroupRn_Type()
)
cfprAaaLdapGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRn.setStatus("current")
_CfprAaaLdapGroupDescr_Type = SnmpAdminString
_CfprAaaLdapGroupDescr_Object = MibTableColumn
cfprAaaLdapGroupDescr = _CfprAaaLdapGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19, 1, 4),
    _CfprAaaLdapGroupDescr_Type()
)
cfprAaaLdapGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupDescr.setStatus("current")
_CfprAaaLdapGroupName_Type = SnmpAdminString
_CfprAaaLdapGroupName_Object = MibTableColumn
cfprAaaLdapGroupName = _CfprAaaLdapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 19, 1, 5),
    _CfprAaaLdapGroupName_Type()
)
cfprAaaLdapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupName.setStatus("current")
_CfprAaaLdapGroupRuleTable_Object = MibTable
cfprAaaLdapGroupRuleTable = _CfprAaaLdapGroupRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleTable.setStatus("current")
_CfprAaaLdapGroupRuleEntry_Object = MibTableRow
cfprAaaLdapGroupRuleEntry = _CfprAaaLdapGroupRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1)
)
cfprAaaLdapGroupRuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLdapGroupRuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleEntry.setStatus("current")
_CfprAaaLdapGroupRuleInstanceId_Type = CfprManagedObjectId
_CfprAaaLdapGroupRuleInstanceId_Object = MibTableColumn
cfprAaaLdapGroupRuleInstanceId = _CfprAaaLdapGroupRuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 1),
    _CfprAaaLdapGroupRuleInstanceId_Type()
)
cfprAaaLdapGroupRuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleInstanceId.setStatus("current")
_CfprAaaLdapGroupRuleDn_Type = CfprManagedObjectDn
_CfprAaaLdapGroupRuleDn_Object = MibTableColumn
cfprAaaLdapGroupRuleDn = _CfprAaaLdapGroupRuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 2),
    _CfprAaaLdapGroupRuleDn_Type()
)
cfprAaaLdapGroupRuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleDn.setStatus("current")
_CfprAaaLdapGroupRuleRn_Type = SnmpAdminString
_CfprAaaLdapGroupRuleRn_Object = MibTableColumn
cfprAaaLdapGroupRuleRn = _CfprAaaLdapGroupRuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 3),
    _CfprAaaLdapGroupRuleRn_Type()
)
cfprAaaLdapGroupRuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleRn.setStatus("current")
_CfprAaaLdapGroupRuleAuthorization_Type = CfprAaaLdapGroupRuleAuthorization
_CfprAaaLdapGroupRuleAuthorization_Object = MibTableColumn
cfprAaaLdapGroupRuleAuthorization = _CfprAaaLdapGroupRuleAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 4),
    _CfprAaaLdapGroupRuleAuthorization_Type()
)
cfprAaaLdapGroupRuleAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleAuthorization.setStatus("current")
_CfprAaaLdapGroupRuleDescr_Type = SnmpAdminString
_CfprAaaLdapGroupRuleDescr_Object = MibTableColumn
cfprAaaLdapGroupRuleDescr = _CfprAaaLdapGroupRuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 5),
    _CfprAaaLdapGroupRuleDescr_Type()
)
cfprAaaLdapGroupRuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleDescr.setStatus("current")
_CfprAaaLdapGroupRuleName_Type = SnmpAdminString
_CfprAaaLdapGroupRuleName_Object = MibTableColumn
cfprAaaLdapGroupRuleName = _CfprAaaLdapGroupRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 6),
    _CfprAaaLdapGroupRuleName_Type()
)
cfprAaaLdapGroupRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleName.setStatus("current")
_CfprAaaLdapGroupRuleTargetAttr_Type = SnmpAdminString
_CfprAaaLdapGroupRuleTargetAttr_Object = MibTableColumn
cfprAaaLdapGroupRuleTargetAttr = _CfprAaaLdapGroupRuleTargetAttr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 7),
    _CfprAaaLdapGroupRuleTargetAttr_Type()
)
cfprAaaLdapGroupRuleTargetAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleTargetAttr.setStatus("current")
_CfprAaaLdapGroupRuleTraversal_Type = CfprAaaLdapGroupRuleTraversal
_CfprAaaLdapGroupRuleTraversal_Object = MibTableColumn
cfprAaaLdapGroupRuleTraversal = _CfprAaaLdapGroupRuleTraversal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 8),
    _CfprAaaLdapGroupRuleTraversal_Type()
)
cfprAaaLdapGroupRuleTraversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleTraversal.setStatus("current")
_CfprAaaLdapGroupRuleUsePrimaryGroup_Type = TruthValue
_CfprAaaLdapGroupRuleUsePrimaryGroup_Object = MibTableColumn
cfprAaaLdapGroupRuleUsePrimaryGroup = _CfprAaaLdapGroupRuleUsePrimaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 20, 1, 9),
    _CfprAaaLdapGroupRuleUsePrimaryGroup_Type()
)
cfprAaaLdapGroupRuleUsePrimaryGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapGroupRuleUsePrimaryGroup.setStatus("current")
_CfprAaaLdapProviderTable_Object = MibTable
cfprAaaLdapProviderTable = _CfprAaaLdapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21)
)
if mibBuilder.loadTexts:
    cfprAaaLdapProviderTable.setStatus("current")
_CfprAaaLdapProviderEntry_Object = MibTableRow
cfprAaaLdapProviderEntry = _CfprAaaLdapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1)
)
cfprAaaLdapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLdapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLdapProviderEntry.setStatus("current")
_CfprAaaLdapProviderInstanceId_Type = CfprManagedObjectId
_CfprAaaLdapProviderInstanceId_Object = MibTableColumn
cfprAaaLdapProviderInstanceId = _CfprAaaLdapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 1),
    _CfprAaaLdapProviderInstanceId_Type()
)
cfprAaaLdapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderInstanceId.setStatus("current")
_CfprAaaLdapProviderDn_Type = CfprManagedObjectDn
_CfprAaaLdapProviderDn_Object = MibTableColumn
cfprAaaLdapProviderDn = _CfprAaaLdapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 2),
    _CfprAaaLdapProviderDn_Type()
)
cfprAaaLdapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderDn.setStatus("current")
_CfprAaaLdapProviderRn_Type = SnmpAdminString
_CfprAaaLdapProviderRn_Object = MibTableColumn
cfprAaaLdapProviderRn = _CfprAaaLdapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 3),
    _CfprAaaLdapProviderRn_Type()
)
cfprAaaLdapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderRn.setStatus("current")
_CfprAaaLdapProviderAttribute_Type = SnmpAdminString
_CfprAaaLdapProviderAttribute_Object = MibTableColumn
cfprAaaLdapProviderAttribute = _CfprAaaLdapProviderAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 4),
    _CfprAaaLdapProviderAttribute_Type()
)
cfprAaaLdapProviderAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderAttribute.setStatus("current")
_CfprAaaLdapProviderBasedn_Type = SnmpAdminString
_CfprAaaLdapProviderBasedn_Object = MibTableColumn
cfprAaaLdapProviderBasedn = _CfprAaaLdapProviderBasedn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 5),
    _CfprAaaLdapProviderBasedn_Type()
)
cfprAaaLdapProviderBasedn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderBasedn.setStatus("current")
_CfprAaaLdapProviderDescr_Type = SnmpAdminString
_CfprAaaLdapProviderDescr_Object = MibTableColumn
cfprAaaLdapProviderDescr = _CfprAaaLdapProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 6),
    _CfprAaaLdapProviderDescr_Type()
)
cfprAaaLdapProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderDescr.setStatus("current")
_CfprAaaLdapProviderEnableSSL_Type = TruthValue
_CfprAaaLdapProviderEnableSSL_Object = MibTableColumn
cfprAaaLdapProviderEnableSSL = _CfprAaaLdapProviderEnableSSL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 7),
    _CfprAaaLdapProviderEnableSSL_Type()
)
cfprAaaLdapProviderEnableSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderEnableSSL.setStatus("current")
_CfprAaaLdapProviderEncKey_Type = SnmpAdminString
_CfprAaaLdapProviderEncKey_Object = MibTableColumn
cfprAaaLdapProviderEncKey = _CfprAaaLdapProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 8),
    _CfprAaaLdapProviderEncKey_Type()
)
cfprAaaLdapProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderEncKey.setStatus("current")
_CfprAaaLdapProviderFilter_Type = SnmpAdminString
_CfprAaaLdapProviderFilter_Object = MibTableColumn
cfprAaaLdapProviderFilter = _CfprAaaLdapProviderFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 9),
    _CfprAaaLdapProviderFilter_Type()
)
cfprAaaLdapProviderFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderFilter.setStatus("current")
_CfprAaaLdapProviderKey_Type = SnmpAdminString
_CfprAaaLdapProviderKey_Object = MibTableColumn
cfprAaaLdapProviderKey = _CfprAaaLdapProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 10),
    _CfprAaaLdapProviderKey_Type()
)
cfprAaaLdapProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderKey.setStatus("current")
_CfprAaaLdapProviderKeySet_Type = TruthValue
_CfprAaaLdapProviderKeySet_Object = MibTableColumn
cfprAaaLdapProviderKeySet = _CfprAaaLdapProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 11),
    _CfprAaaLdapProviderKeySet_Type()
)
cfprAaaLdapProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderKeySet.setStatus("current")
_CfprAaaLdapProviderName_Type = SnmpAdminString
_CfprAaaLdapProviderName_Object = MibTableColumn
cfprAaaLdapProviderName = _CfprAaaLdapProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 12),
    _CfprAaaLdapProviderName_Type()
)
cfprAaaLdapProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderName.setStatus("current")
_CfprAaaLdapProviderOrder_Type = Gauge32
_CfprAaaLdapProviderOrder_Object = MibTableColumn
cfprAaaLdapProviderOrder = _CfprAaaLdapProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 13),
    _CfprAaaLdapProviderOrder_Type()
)
cfprAaaLdapProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderOrder.setStatus("current")
_CfprAaaLdapProviderPort_Type = Gauge32
_CfprAaaLdapProviderPort_Object = MibTableColumn
cfprAaaLdapProviderPort = _CfprAaaLdapProviderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 14),
    _CfprAaaLdapProviderPort_Type()
)
cfprAaaLdapProviderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderPort.setStatus("current")
_CfprAaaLdapProviderRetries_Type = Gauge32
_CfprAaaLdapProviderRetries_Object = MibTableColumn
cfprAaaLdapProviderRetries = _CfprAaaLdapProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 15),
    _CfprAaaLdapProviderRetries_Type()
)
cfprAaaLdapProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderRetries.setStatus("current")
_CfprAaaLdapProviderRootdn_Type = SnmpAdminString
_CfprAaaLdapProviderRootdn_Object = MibTableColumn
cfprAaaLdapProviderRootdn = _CfprAaaLdapProviderRootdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 16),
    _CfprAaaLdapProviderRootdn_Type()
)
cfprAaaLdapProviderRootdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderRootdn.setStatus("current")
_CfprAaaLdapProviderTimeout_Type = Gauge32
_CfprAaaLdapProviderTimeout_Object = MibTableColumn
cfprAaaLdapProviderTimeout = _CfprAaaLdapProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 17),
    _CfprAaaLdapProviderTimeout_Type()
)
cfprAaaLdapProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderTimeout.setStatus("current")
_CfprAaaLdapProviderVendor_Type = CfprAaaLdapVendor
_CfprAaaLdapProviderVendor_Object = MibTableColumn
cfprAaaLdapProviderVendor = _CfprAaaLdapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 18),
    _CfprAaaLdapProviderVendor_Type()
)
cfprAaaLdapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderVendor.setStatus("current")
_CfprAaaLdapProviderKeyring_Type = SnmpAdminString
_CfprAaaLdapProviderKeyring_Object = MibTableColumn
cfprAaaLdapProviderKeyring = _CfprAaaLdapProviderKeyring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 19),
    _CfprAaaLdapProviderKeyring_Type()
)
cfprAaaLdapProviderKeyring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderKeyring.setStatus("current")
_CfprAaaLdapProviderRevokePolicy_Type = CfprAaaRevokePolicy
_CfprAaaLdapProviderRevokePolicy_Object = MibTableColumn
cfprAaaLdapProviderRevokePolicy = _CfprAaaLdapProviderRevokePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 20),
    _CfprAaaLdapProviderRevokePolicy_Type()
)
cfprAaaLdapProviderRevokePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderRevokePolicy.setStatus("current")
_CfprAaaLdapProviderCipher_Type = SnmpAdminString
_CfprAaaLdapProviderCipher_Object = MibTableColumn
cfprAaaLdapProviderCipher = _CfprAaaLdapProviderCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 21),
    _CfprAaaLdapProviderCipher_Type()
)
cfprAaaLdapProviderCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderCipher.setStatus("current")
_CfprAaaLdapProviderCiphermode_Type = CfprAaaCipherMode
_CfprAaaLdapProviderCiphermode_Object = MibTableColumn
cfprAaaLdapProviderCiphermode = _CfprAaaLdapProviderCiphermode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 22),
    _CfprAaaLdapProviderCiphermode_Type()
)
cfprAaaLdapProviderCiphermode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderCiphermode.setStatus("current")
_CfprAaaLdapProviderFqdnEnforce_Type = CfprAaaFqdnEnforceType
_CfprAaaLdapProviderFqdnEnforce_Object = MibTableColumn
cfprAaaLdapProviderFqdnEnforce = _CfprAaaLdapProviderFqdnEnforce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 21, 1, 23),
    _CfprAaaLdapProviderFqdnEnforce_Type()
)
cfprAaaLdapProviderFqdnEnforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLdapProviderFqdnEnforce.setStatus("current")
_CfprAaaLocaleTable_Object = MibTable
cfprAaaLocaleTable = _CfprAaaLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22)
)
if mibBuilder.loadTexts:
    cfprAaaLocaleTable.setStatus("current")
_CfprAaaLocaleEntry_Object = MibTableRow
cfprAaaLocaleEntry = _CfprAaaLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1)
)
cfprAaaLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLocaleEntry.setStatus("current")
_CfprAaaLocaleInstanceId_Type = CfprManagedObjectId
_CfprAaaLocaleInstanceId_Object = MibTableColumn
cfprAaaLocaleInstanceId = _CfprAaaLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 1),
    _CfprAaaLocaleInstanceId_Type()
)
cfprAaaLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLocaleInstanceId.setStatus("current")
_CfprAaaLocaleDn_Type = CfprManagedObjectDn
_CfprAaaLocaleDn_Object = MibTableColumn
cfprAaaLocaleDn = _CfprAaaLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 2),
    _CfprAaaLocaleDn_Type()
)
cfprAaaLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleDn.setStatus("current")
_CfprAaaLocaleRn_Type = SnmpAdminString
_CfprAaaLocaleRn_Object = MibTableColumn
cfprAaaLocaleRn = _CfprAaaLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 3),
    _CfprAaaLocaleRn_Type()
)
cfprAaaLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleRn.setStatus("current")
_CfprAaaLocaleConfigState_Type = CfprAaaConfigState
_CfprAaaLocaleConfigState_Object = MibTableColumn
cfprAaaLocaleConfigState = _CfprAaaLocaleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 4),
    _CfprAaaLocaleConfigState_Type()
)
cfprAaaLocaleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleConfigState.setStatus("current")
_CfprAaaLocaleConfigStatusMessage_Type = SnmpAdminString
_CfprAaaLocaleConfigStatusMessage_Object = MibTableColumn
cfprAaaLocaleConfigStatusMessage = _CfprAaaLocaleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 5),
    _CfprAaaLocaleConfigStatusMessage_Type()
)
cfprAaaLocaleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleConfigStatusMessage.setStatus("current")
_CfprAaaLocaleDescr_Type = SnmpAdminString
_CfprAaaLocaleDescr_Object = MibTableColumn
cfprAaaLocaleDescr = _CfprAaaLocaleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 6),
    _CfprAaaLocaleDescr_Type()
)
cfprAaaLocaleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleDescr.setStatus("current")
_CfprAaaLocaleIntId_Type = SnmpAdminString
_CfprAaaLocaleIntId_Object = MibTableColumn
cfprAaaLocaleIntId = _CfprAaaLocaleIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 7),
    _CfprAaaLocaleIntId_Type()
)
cfprAaaLocaleIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleIntId.setStatus("current")
_CfprAaaLocaleName_Type = SnmpAdminString
_CfprAaaLocaleName_Object = MibTableColumn
cfprAaaLocaleName = _CfprAaaLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 8),
    _CfprAaaLocaleName_Type()
)
cfprAaaLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocaleName.setStatus("current")
_CfprAaaLocalePolicyLevel_Type = Gauge32
_CfprAaaLocalePolicyLevel_Object = MibTableColumn
cfprAaaLocalePolicyLevel = _CfprAaaLocalePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 9),
    _CfprAaaLocalePolicyLevel_Type()
)
cfprAaaLocalePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocalePolicyLevel.setStatus("current")
_CfprAaaLocalePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaLocalePolicyOwner_Object = MibTableColumn
cfprAaaLocalePolicyOwner = _CfprAaaLocalePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 22, 1, 10),
    _CfprAaaLocalePolicyOwner_Type()
)
cfprAaaLocalePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLocalePolicyOwner.setStatus("current")
_CfprAaaLogTable_Object = MibTable
cfprAaaLogTable = _CfprAaaLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23)
)
if mibBuilder.loadTexts:
    cfprAaaLogTable.setStatus("current")
_CfprAaaLogEntry_Object = MibTableRow
cfprAaaLogEntry = _CfprAaaLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1)
)
cfprAaaLogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLogEntry.setStatus("current")
_CfprAaaLogInstanceId_Type = CfprManagedObjectId
_CfprAaaLogInstanceId_Object = MibTableColumn
cfprAaaLogInstanceId = _CfprAaaLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1, 1),
    _CfprAaaLogInstanceId_Type()
)
cfprAaaLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLogInstanceId.setStatus("current")
_CfprAaaLogDn_Type = CfprManagedObjectDn
_CfprAaaLogDn_Object = MibTableColumn
cfprAaaLogDn = _CfprAaaLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1, 2),
    _CfprAaaLogDn_Type()
)
cfprAaaLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLogDn.setStatus("current")
_CfprAaaLogRn_Type = SnmpAdminString
_CfprAaaLogRn_Object = MibTableColumn
cfprAaaLogRn = _CfprAaaLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1, 3),
    _CfprAaaLogRn_Type()
)
cfprAaaLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLogRn.setStatus("current")
_CfprAaaLogMaxSize_Type = Gauge32
_CfprAaaLogMaxSize_Object = MibTableColumn
cfprAaaLogMaxSize = _CfprAaaLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1, 4),
    _CfprAaaLogMaxSize_Type()
)
cfprAaaLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLogMaxSize.setStatus("current")
_CfprAaaLogPurgeWindow_Type = Gauge32
_CfprAaaLogPurgeWindow_Object = MibTableColumn
cfprAaaLogPurgeWindow = _CfprAaaLogPurgeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1, 5),
    _CfprAaaLogPurgeWindow_Type()
)
cfprAaaLogPurgeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLogPurgeWindow.setStatus("current")
_CfprAaaLogSize_Type = Gauge32
_CfprAaaLogSize_Object = MibTableColumn
cfprAaaLogSize = _CfprAaaLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 23, 1, 6),
    _CfprAaaLogSize_Type()
)
cfprAaaLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLogSize.setStatus("current")
_CfprAaaModLRTable_Object = MibTable
cfprAaaModLRTable = _CfprAaaModLRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24)
)
if mibBuilder.loadTexts:
    cfprAaaModLRTable.setStatus("current")
_CfprAaaModLREntry_Object = MibTableRow
cfprAaaModLREntry = _CfprAaaModLREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1)
)
cfprAaaModLREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaModLRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaModLREntry.setStatus("current")
_CfprAaaModLRInstanceId_Type = CfprManagedObjectId
_CfprAaaModLRInstanceId_Object = MibTableColumn
cfprAaaModLRInstanceId = _CfprAaaModLRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 1),
    _CfprAaaModLRInstanceId_Type()
)
cfprAaaModLRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaModLRInstanceId.setStatus("current")
_CfprAaaModLRDn_Type = CfprManagedObjectDn
_CfprAaaModLRDn_Object = MibTableColumn
cfprAaaModLRDn = _CfprAaaModLRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 2),
    _CfprAaaModLRDn_Type()
)
cfprAaaModLRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRDn.setStatus("current")
_CfprAaaModLRRn_Type = SnmpAdminString
_CfprAaaModLRRn_Object = MibTableColumn
cfprAaaModLRRn = _CfprAaaModLRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 3),
    _CfprAaaModLRRn_Type()
)
cfprAaaModLRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRRn.setStatus("current")
_CfprAaaModLRAffected_Type = SnmpAdminString
_CfprAaaModLRAffected_Object = MibTableColumn
cfprAaaModLRAffected = _CfprAaaModLRAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 4),
    _CfprAaaModLRAffected_Type()
)
cfprAaaModLRAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRAffected.setStatus("current")
_CfprAaaModLRCause_Type = CfprConditionCause
_CfprAaaModLRCause_Object = MibTableColumn
cfprAaaModLRCause = _CfprAaaModLRCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 5),
    _CfprAaaModLRCause_Type()
)
cfprAaaModLRCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRCause.setStatus("current")
_CfprAaaModLRChangeSet_Type = SnmpAdminString
_CfprAaaModLRChangeSet_Object = MibTableColumn
cfprAaaModLRChangeSet = _CfprAaaModLRChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 6),
    _CfprAaaModLRChangeSet_Type()
)
cfprAaaModLRChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRChangeSet.setStatus("current")
_CfprAaaModLRCode_Type = CfprConditionCode
_CfprAaaModLRCode_Object = MibTableColumn
cfprAaaModLRCode = _CfprAaaModLRCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 7),
    _CfprAaaModLRCode_Type()
)
cfprAaaModLRCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRCode.setStatus("current")
_CfprAaaModLRCreated_Type = DateAndTime
_CfprAaaModLRCreated_Object = MibTableColumn
cfprAaaModLRCreated = _CfprAaaModLRCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 8),
    _CfprAaaModLRCreated_Type()
)
cfprAaaModLRCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRCreated.setStatus("current")
_CfprAaaModLRDescr_Type = SnmpAdminString
_CfprAaaModLRDescr_Object = MibTableColumn
cfprAaaModLRDescr = _CfprAaaModLRDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 9),
    _CfprAaaModLRDescr_Type()
)
cfprAaaModLRDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRDescr.setStatus("current")
_CfprAaaModLRId_Type = Gauge32
_CfprAaaModLRId_Object = MibTableColumn
cfprAaaModLRId = _CfprAaaModLRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 10),
    _CfprAaaModLRId_Type()
)
cfprAaaModLRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRId.setStatus("current")
_CfprAaaModLRInd_Type = CfprConditionActionIndicator
_CfprAaaModLRInd_Object = MibTableColumn
cfprAaaModLRInd = _CfprAaaModLRInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 11),
    _CfprAaaModLRInd_Type()
)
cfprAaaModLRInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRInd.setStatus("current")
_CfprAaaModLRSessionId_Type = SnmpAdminString
_CfprAaaModLRSessionId_Object = MibTableColumn
cfprAaaModLRSessionId = _CfprAaaModLRSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 12),
    _CfprAaaModLRSessionId_Type()
)
cfprAaaModLRSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRSessionId.setStatus("current")
_CfprAaaModLRSeverity_Type = CfprConditionSeverity
_CfprAaaModLRSeverity_Object = MibTableColumn
cfprAaaModLRSeverity = _CfprAaaModLRSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 13),
    _CfprAaaModLRSeverity_Type()
)
cfprAaaModLRSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRSeverity.setStatus("current")
_CfprAaaModLRTrig_Type = Gauge32
_CfprAaaModLRTrig_Object = MibTableColumn
cfprAaaModLRTrig = _CfprAaaModLRTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 14),
    _CfprAaaModLRTrig_Type()
)
cfprAaaModLRTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRTrig.setStatus("current")
_CfprAaaModLRTxId_Type = Unsigned64
_CfprAaaModLRTxId_Object = MibTableColumn
cfprAaaModLRTxId = _CfprAaaModLRTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 15),
    _CfprAaaModLRTxId_Type()
)
cfprAaaModLRTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRTxId.setStatus("current")
_CfprAaaModLRUser_Type = SnmpAdminString
_CfprAaaModLRUser_Object = MibTableColumn
cfprAaaModLRUser = _CfprAaaModLRUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 24, 1, 16),
    _CfprAaaModLRUser_Type()
)
cfprAaaModLRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaModLRUser.setStatus("current")
_CfprAaaOrgTable_Object = MibTable
cfprAaaOrgTable = _CfprAaaOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25)
)
if mibBuilder.loadTexts:
    cfprAaaOrgTable.setStatus("current")
_CfprAaaOrgEntry_Object = MibTableRow
cfprAaaOrgEntry = _CfprAaaOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1)
)
cfprAaaOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaOrgEntry.setStatus("current")
_CfprAaaOrgInstanceId_Type = CfprManagedObjectId
_CfprAaaOrgInstanceId_Object = MibTableColumn
cfprAaaOrgInstanceId = _CfprAaaOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 1),
    _CfprAaaOrgInstanceId_Type()
)
cfprAaaOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaOrgInstanceId.setStatus("current")
_CfprAaaOrgDn_Type = CfprManagedObjectDn
_CfprAaaOrgDn_Object = MibTableColumn
cfprAaaOrgDn = _CfprAaaOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 2),
    _CfprAaaOrgDn_Type()
)
cfprAaaOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgDn.setStatus("current")
_CfprAaaOrgRn_Type = SnmpAdminString
_CfprAaaOrgRn_Object = MibTableColumn
cfprAaaOrgRn = _CfprAaaOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 3),
    _CfprAaaOrgRn_Type()
)
cfprAaaOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgRn.setStatus("current")
_CfprAaaOrgConfigState_Type = CfprAaaConfigState
_CfprAaaOrgConfigState_Object = MibTableColumn
cfprAaaOrgConfigState = _CfprAaaOrgConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 4),
    _CfprAaaOrgConfigState_Type()
)
cfprAaaOrgConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgConfigState.setStatus("current")
_CfprAaaOrgConfigStatusMessage_Type = SnmpAdminString
_CfprAaaOrgConfigStatusMessage_Object = MibTableColumn
cfprAaaOrgConfigStatusMessage = _CfprAaaOrgConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 5),
    _CfprAaaOrgConfigStatusMessage_Type()
)
cfprAaaOrgConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgConfigStatusMessage.setStatus("current")
_CfprAaaOrgDescr_Type = SnmpAdminString
_CfprAaaOrgDescr_Object = MibTableColumn
cfprAaaOrgDescr = _CfprAaaOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 6),
    _CfprAaaOrgDescr_Type()
)
cfprAaaOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgDescr.setStatus("current")
_CfprAaaOrgName_Type = SnmpAdminString
_CfprAaaOrgName_Object = MibTableColumn
cfprAaaOrgName = _CfprAaaOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 7),
    _CfprAaaOrgName_Type()
)
cfprAaaOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgName.setStatus("current")
_CfprAaaOrgOrgDn_Type = SnmpAdminString
_CfprAaaOrgOrgDn_Object = MibTableColumn
cfprAaaOrgOrgDn = _CfprAaaOrgOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 25, 1, 8),
    _CfprAaaOrgOrgDn_Type()
)
cfprAaaOrgOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaOrgOrgDn.setStatus("current")
_CfprAaaPreLoginBannerTable_Object = MibTable
cfprAaaPreLoginBannerTable = _CfprAaaPreLoginBannerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26)
)
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerTable.setStatus("current")
_CfprAaaPreLoginBannerEntry_Object = MibTableRow
cfprAaaPreLoginBannerEntry = _CfprAaaPreLoginBannerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1)
)
cfprAaaPreLoginBannerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaPreLoginBannerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerEntry.setStatus("current")
_CfprAaaPreLoginBannerInstanceId_Type = CfprManagedObjectId
_CfprAaaPreLoginBannerInstanceId_Object = MibTableColumn
cfprAaaPreLoginBannerInstanceId = _CfprAaaPreLoginBannerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 1),
    _CfprAaaPreLoginBannerInstanceId_Type()
)
cfprAaaPreLoginBannerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerInstanceId.setStatus("current")
_CfprAaaPreLoginBannerDn_Type = CfprManagedObjectDn
_CfprAaaPreLoginBannerDn_Object = MibTableColumn
cfprAaaPreLoginBannerDn = _CfprAaaPreLoginBannerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 2),
    _CfprAaaPreLoginBannerDn_Type()
)
cfprAaaPreLoginBannerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerDn.setStatus("current")
_CfprAaaPreLoginBannerRn_Type = SnmpAdminString
_CfprAaaPreLoginBannerRn_Object = MibTableColumn
cfprAaaPreLoginBannerRn = _CfprAaaPreLoginBannerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 3),
    _CfprAaaPreLoginBannerRn_Type()
)
cfprAaaPreLoginBannerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerRn.setStatus("current")
_CfprAaaPreLoginBannerDescr_Type = SnmpAdminString
_CfprAaaPreLoginBannerDescr_Object = MibTableColumn
cfprAaaPreLoginBannerDescr = _CfprAaaPreLoginBannerDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 4),
    _CfprAaaPreLoginBannerDescr_Type()
)
cfprAaaPreLoginBannerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerDescr.setStatus("current")
_CfprAaaPreLoginBannerIntId_Type = SnmpAdminString
_CfprAaaPreLoginBannerIntId_Object = MibTableColumn
cfprAaaPreLoginBannerIntId = _CfprAaaPreLoginBannerIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 5),
    _CfprAaaPreLoginBannerIntId_Type()
)
cfprAaaPreLoginBannerIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerIntId.setStatus("current")
_CfprAaaPreLoginBannerMessage_Type = SnmpAdminString
_CfprAaaPreLoginBannerMessage_Object = MibTableColumn
cfprAaaPreLoginBannerMessage = _CfprAaaPreLoginBannerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 6),
    _CfprAaaPreLoginBannerMessage_Type()
)
cfprAaaPreLoginBannerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerMessage.setStatus("current")
_CfprAaaPreLoginBannerName_Type = SnmpAdminString
_CfprAaaPreLoginBannerName_Object = MibTableColumn
cfprAaaPreLoginBannerName = _CfprAaaPreLoginBannerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 7),
    _CfprAaaPreLoginBannerName_Type()
)
cfprAaaPreLoginBannerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerName.setStatus("current")
_CfprAaaPreLoginBannerPolicyLevel_Type = Gauge32
_CfprAaaPreLoginBannerPolicyLevel_Object = MibTableColumn
cfprAaaPreLoginBannerPolicyLevel = _CfprAaaPreLoginBannerPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 8),
    _CfprAaaPreLoginBannerPolicyLevel_Type()
)
cfprAaaPreLoginBannerPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerPolicyLevel.setStatus("current")
_CfprAaaPreLoginBannerPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaPreLoginBannerPolicyOwner_Object = MibTableColumn
cfprAaaPreLoginBannerPolicyOwner = _CfprAaaPreLoginBannerPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 26, 1, 9),
    _CfprAaaPreLoginBannerPolicyOwner_Type()
)
cfprAaaPreLoginBannerPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPreLoginBannerPolicyOwner.setStatus("current")
_CfprAaaProviderGroupTable_Object = MibTable
cfprAaaProviderGroupTable = _CfprAaaProviderGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27)
)
if mibBuilder.loadTexts:
    cfprAaaProviderGroupTable.setStatus("current")
_CfprAaaProviderGroupEntry_Object = MibTableRow
cfprAaaProviderGroupEntry = _CfprAaaProviderGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1)
)
cfprAaaProviderGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaProviderGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaProviderGroupEntry.setStatus("current")
_CfprAaaProviderGroupInstanceId_Type = CfprManagedObjectId
_CfprAaaProviderGroupInstanceId_Object = MibTableColumn
cfprAaaProviderGroupInstanceId = _CfprAaaProviderGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 1),
    _CfprAaaProviderGroupInstanceId_Type()
)
cfprAaaProviderGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupInstanceId.setStatus("current")
_CfprAaaProviderGroupDn_Type = CfprManagedObjectDn
_CfprAaaProviderGroupDn_Object = MibTableColumn
cfprAaaProviderGroupDn = _CfprAaaProviderGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 2),
    _CfprAaaProviderGroupDn_Type()
)
cfprAaaProviderGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupDn.setStatus("current")
_CfprAaaProviderGroupRn_Type = SnmpAdminString
_CfprAaaProviderGroupRn_Object = MibTableColumn
cfprAaaProviderGroupRn = _CfprAaaProviderGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 3),
    _CfprAaaProviderGroupRn_Type()
)
cfprAaaProviderGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupRn.setStatus("current")
_CfprAaaProviderGroupConfigState_Type = CfprAaaConfigState
_CfprAaaProviderGroupConfigState_Object = MibTableColumn
cfprAaaProviderGroupConfigState = _CfprAaaProviderGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 4),
    _CfprAaaProviderGroupConfigState_Type()
)
cfprAaaProviderGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupConfigState.setStatus("current")
_CfprAaaProviderGroupDescr_Type = SnmpAdminString
_CfprAaaProviderGroupDescr_Object = MibTableColumn
cfprAaaProviderGroupDescr = _CfprAaaProviderGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 5),
    _CfprAaaProviderGroupDescr_Type()
)
cfprAaaProviderGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupDescr.setStatus("current")
_CfprAaaProviderGroupName_Type = SnmpAdminString
_CfprAaaProviderGroupName_Object = MibTableColumn
cfprAaaProviderGroupName = _CfprAaaProviderGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 6),
    _CfprAaaProviderGroupName_Type()
)
cfprAaaProviderGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupName.setStatus("current")
_CfprAaaProviderGroupSize_Type = Gauge32
_CfprAaaProviderGroupSize_Object = MibTableColumn
cfprAaaProviderGroupSize = _CfprAaaProviderGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 27, 1, 7),
    _CfprAaaProviderGroupSize_Type()
)
cfprAaaProviderGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderGroupSize.setStatus("current")
_CfprAaaProviderRefTable_Object = MibTable
cfprAaaProviderRefTable = _CfprAaaProviderRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28)
)
if mibBuilder.loadTexts:
    cfprAaaProviderRefTable.setStatus("current")
_CfprAaaProviderRefEntry_Object = MibTableRow
cfprAaaProviderRefEntry = _CfprAaaProviderRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1)
)
cfprAaaProviderRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaProviderRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaProviderRefEntry.setStatus("current")
_CfprAaaProviderRefInstanceId_Type = CfprManagedObjectId
_CfprAaaProviderRefInstanceId_Object = MibTableColumn
cfprAaaProviderRefInstanceId = _CfprAaaProviderRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1, 1),
    _CfprAaaProviderRefInstanceId_Type()
)
cfprAaaProviderRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaProviderRefInstanceId.setStatus("current")
_CfprAaaProviderRefDn_Type = CfprManagedObjectDn
_CfprAaaProviderRefDn_Object = MibTableColumn
cfprAaaProviderRefDn = _CfprAaaProviderRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1, 2),
    _CfprAaaProviderRefDn_Type()
)
cfprAaaProviderRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderRefDn.setStatus("current")
_CfprAaaProviderRefRn_Type = SnmpAdminString
_CfprAaaProviderRefRn_Object = MibTableColumn
cfprAaaProviderRefRn = _CfprAaaProviderRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1, 3),
    _CfprAaaProviderRefRn_Type()
)
cfprAaaProviderRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderRefRn.setStatus("current")
_CfprAaaProviderRefDescr_Type = SnmpAdminString
_CfprAaaProviderRefDescr_Object = MibTableColumn
cfprAaaProviderRefDescr = _CfprAaaProviderRefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1, 4),
    _CfprAaaProviderRefDescr_Type()
)
cfprAaaProviderRefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderRefDescr.setStatus("current")
_CfprAaaProviderRefName_Type = SnmpAdminString
_CfprAaaProviderRefName_Object = MibTableColumn
cfprAaaProviderRefName = _CfprAaaProviderRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1, 5),
    _CfprAaaProviderRefName_Type()
)
cfprAaaProviderRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderRefName.setStatus("current")
_CfprAaaProviderRefOrder_Type = Gauge32
_CfprAaaProviderRefOrder_Object = MibTableColumn
cfprAaaProviderRefOrder = _CfprAaaProviderRefOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 28, 1, 6),
    _CfprAaaProviderRefOrder_Type()
)
cfprAaaProviderRefOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaProviderRefOrder.setStatus("current")
_CfprAaaPwdProfileTable_Object = MibTable
cfprAaaPwdProfileTable = _CfprAaaPwdProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29)
)
if mibBuilder.loadTexts:
    cfprAaaPwdProfileTable.setStatus("current")
_CfprAaaPwdProfileEntry_Object = MibTableRow
cfprAaaPwdProfileEntry = _CfprAaaPwdProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1)
)
cfprAaaPwdProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaPwdProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaPwdProfileEntry.setStatus("current")
_CfprAaaPwdProfileInstanceId_Type = CfprManagedObjectId
_CfprAaaPwdProfileInstanceId_Object = MibTableColumn
cfprAaaPwdProfileInstanceId = _CfprAaaPwdProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 1),
    _CfprAaaPwdProfileInstanceId_Type()
)
cfprAaaPwdProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileInstanceId.setStatus("current")
_CfprAaaPwdProfileDn_Type = CfprManagedObjectDn
_CfprAaaPwdProfileDn_Object = MibTableColumn
cfprAaaPwdProfileDn = _CfprAaaPwdProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 2),
    _CfprAaaPwdProfileDn_Type()
)
cfprAaaPwdProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileDn.setStatus("current")
_CfprAaaPwdProfileRn_Type = SnmpAdminString
_CfprAaaPwdProfileRn_Object = MibTableColumn
cfprAaaPwdProfileRn = _CfprAaaPwdProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 3),
    _CfprAaaPwdProfileRn_Type()
)
cfprAaaPwdProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileRn.setStatus("current")
_CfprAaaPwdProfileChangeCount_Type = Gauge32
_CfprAaaPwdProfileChangeCount_Object = MibTableColumn
cfprAaaPwdProfileChangeCount = _CfprAaaPwdProfileChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 4),
    _CfprAaaPwdProfileChangeCount_Type()
)
cfprAaaPwdProfileChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileChangeCount.setStatus("current")
_CfprAaaPwdProfileChangeDuringInterval_Type = CfprAaaPwdPolicy
_CfprAaaPwdProfileChangeDuringInterval_Object = MibTableColumn
cfprAaaPwdProfileChangeDuringInterval = _CfprAaaPwdProfileChangeDuringInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 5),
    _CfprAaaPwdProfileChangeDuringInterval_Type()
)
cfprAaaPwdProfileChangeDuringInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileChangeDuringInterval.setStatus("current")
_CfprAaaPwdProfileChangeInterval_Type = Gauge32
_CfprAaaPwdProfileChangeInterval_Object = MibTableColumn
cfprAaaPwdProfileChangeInterval = _CfprAaaPwdProfileChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 6),
    _CfprAaaPwdProfileChangeInterval_Type()
)
cfprAaaPwdProfileChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileChangeInterval.setStatus("current")
_CfprAaaPwdProfileExpirationWarnTime_Type = Gauge32
_CfprAaaPwdProfileExpirationWarnTime_Object = MibTableColumn
cfprAaaPwdProfileExpirationWarnTime = _CfprAaaPwdProfileExpirationWarnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 8),
    _CfprAaaPwdProfileExpirationWarnTime_Type()
)
cfprAaaPwdProfileExpirationWarnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileExpirationWarnTime.setStatus("current")
_CfprAaaPwdProfileHistoryCount_Type = Gauge32
_CfprAaaPwdProfileHistoryCount_Object = MibTableColumn
cfprAaaPwdProfileHistoryCount = _CfprAaaPwdProfileHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 9),
    _CfprAaaPwdProfileHistoryCount_Type()
)
cfprAaaPwdProfileHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileHistoryCount.setStatus("current")
_CfprAaaPwdProfileNoChangeInterval_Type = Gauge32
_CfprAaaPwdProfileNoChangeInterval_Object = MibTableColumn
cfprAaaPwdProfileNoChangeInterval = _CfprAaaPwdProfileNoChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 12),
    _CfprAaaPwdProfileNoChangeInterval_Type()
)
cfprAaaPwdProfileNoChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileNoChangeInterval.setStatus("current")
_CfprAaaPwdProfileExpirationDays_Type = Gauge32
_CfprAaaPwdProfileExpirationDays_Object = MibTableColumn
cfprAaaPwdProfileExpirationDays = _CfprAaaPwdProfileExpirationDays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 15),
    _CfprAaaPwdProfileExpirationDays_Type()
)
cfprAaaPwdProfileExpirationDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileExpirationDays.setStatus("current")
_CfprAaaPwdProfileExpirationGracePeriod_Type = Gauge32
_CfprAaaPwdProfileExpirationGracePeriod_Object = MibTableColumn
cfprAaaPwdProfileExpirationGracePeriod = _CfprAaaPwdProfileExpirationGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 16),
    _CfprAaaPwdProfileExpirationGracePeriod_Type()
)
cfprAaaPwdProfileExpirationGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileExpirationGracePeriod.setStatus("current")
_CfprAaaPwdProfileReuseTime_Type = Gauge32
_CfprAaaPwdProfileReuseTime_Object = MibTableColumn
cfprAaaPwdProfileReuseTime = _CfprAaaPwdProfileReuseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 29, 1, 17),
    _CfprAaaPwdProfileReuseTime_Type()
)
cfprAaaPwdProfileReuseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdProfileReuseTime.setStatus("current")
_CfprAaaRadiusEpTable_Object = MibTable
cfprAaaRadiusEpTable = _CfprAaaRadiusEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30)
)
if mibBuilder.loadTexts:
    cfprAaaRadiusEpTable.setStatus("current")
_CfprAaaRadiusEpEntry_Object = MibTableRow
cfprAaaRadiusEpEntry = _CfprAaaRadiusEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1)
)
cfprAaaRadiusEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRadiusEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRadiusEpEntry.setStatus("current")
_CfprAaaRadiusEpInstanceId_Type = CfprManagedObjectId
_CfprAaaRadiusEpInstanceId_Object = MibTableColumn
cfprAaaRadiusEpInstanceId = _CfprAaaRadiusEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 1),
    _CfprAaaRadiusEpInstanceId_Type()
)
cfprAaaRadiusEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpInstanceId.setStatus("current")
_CfprAaaRadiusEpDn_Type = CfprManagedObjectDn
_CfprAaaRadiusEpDn_Object = MibTableColumn
cfprAaaRadiusEpDn = _CfprAaaRadiusEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 2),
    _CfprAaaRadiusEpDn_Type()
)
cfprAaaRadiusEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpDn.setStatus("current")
_CfprAaaRadiusEpRn_Type = SnmpAdminString
_CfprAaaRadiusEpRn_Object = MibTableColumn
cfprAaaRadiusEpRn = _CfprAaaRadiusEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 3),
    _CfprAaaRadiusEpRn_Type()
)
cfprAaaRadiusEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpRn.setStatus("current")
_CfprAaaRadiusEpDescr_Type = SnmpAdminString
_CfprAaaRadiusEpDescr_Object = MibTableColumn
cfprAaaRadiusEpDescr = _CfprAaaRadiusEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 4),
    _CfprAaaRadiusEpDescr_Type()
)
cfprAaaRadiusEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpDescr.setStatus("current")
_CfprAaaRadiusEpFsmDescr_Type = SnmpAdminString
_CfprAaaRadiusEpFsmDescr_Object = MibTableColumn
cfprAaaRadiusEpFsmDescr = _CfprAaaRadiusEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 5),
    _CfprAaaRadiusEpFsmDescr_Type()
)
cfprAaaRadiusEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmDescr.setStatus("current")
_CfprAaaRadiusEpFsmPrev_Type = SnmpAdminString
_CfprAaaRadiusEpFsmPrev_Object = MibTableColumn
cfprAaaRadiusEpFsmPrev = _CfprAaaRadiusEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 6),
    _CfprAaaRadiusEpFsmPrev_Type()
)
cfprAaaRadiusEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmPrev.setStatus("current")
_CfprAaaRadiusEpFsmProgr_Type = Gauge32
_CfprAaaRadiusEpFsmProgr_Object = MibTableColumn
cfprAaaRadiusEpFsmProgr = _CfprAaaRadiusEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 7),
    _CfprAaaRadiusEpFsmProgr_Type()
)
cfprAaaRadiusEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmProgr.setStatus("current")
_CfprAaaRadiusEpFsmRmtInvErrCode_Type = Gauge32
_CfprAaaRadiusEpFsmRmtInvErrCode_Object = MibTableColumn
cfprAaaRadiusEpFsmRmtInvErrCode = _CfprAaaRadiusEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 8),
    _CfprAaaRadiusEpFsmRmtInvErrCode_Type()
)
cfprAaaRadiusEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRmtInvErrCode.setStatus("current")
_CfprAaaRadiusEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprAaaRadiusEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprAaaRadiusEpFsmRmtInvErrDescr = _CfprAaaRadiusEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 9),
    _CfprAaaRadiusEpFsmRmtInvErrDescr_Type()
)
cfprAaaRadiusEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRmtInvErrDescr.setStatus("current")
_CfprAaaRadiusEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaRadiusEpFsmRmtInvRslt_Object = MibTableColumn
cfprAaaRadiusEpFsmRmtInvRslt = _CfprAaaRadiusEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 10),
    _CfprAaaRadiusEpFsmRmtInvRslt_Type()
)
cfprAaaRadiusEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRmtInvRslt.setStatus("current")
_CfprAaaRadiusEpFsmStageDescr_Type = SnmpAdminString
_CfprAaaRadiusEpFsmStageDescr_Object = MibTableColumn
cfprAaaRadiusEpFsmStageDescr = _CfprAaaRadiusEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 11),
    _CfprAaaRadiusEpFsmStageDescr_Type()
)
cfprAaaRadiusEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageDescr.setStatus("current")
_CfprAaaRadiusEpFsmStamp_Type = DateAndTime
_CfprAaaRadiusEpFsmStamp_Object = MibTableColumn
cfprAaaRadiusEpFsmStamp = _CfprAaaRadiusEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 12),
    _CfprAaaRadiusEpFsmStamp_Type()
)
cfprAaaRadiusEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStamp.setStatus("current")
_CfprAaaRadiusEpFsmStatus_Type = SnmpAdminString
_CfprAaaRadiusEpFsmStatus_Object = MibTableColumn
cfprAaaRadiusEpFsmStatus = _CfprAaaRadiusEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 13),
    _CfprAaaRadiusEpFsmStatus_Type()
)
cfprAaaRadiusEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStatus.setStatus("current")
_CfprAaaRadiusEpFsmTry_Type = Gauge32
_CfprAaaRadiusEpFsmTry_Object = MibTableColumn
cfprAaaRadiusEpFsmTry = _CfprAaaRadiusEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 14),
    _CfprAaaRadiusEpFsmTry_Type()
)
cfprAaaRadiusEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmTry.setStatus("current")
_CfprAaaRadiusEpIntId_Type = SnmpAdminString
_CfprAaaRadiusEpIntId_Object = MibTableColumn
cfprAaaRadiusEpIntId = _CfprAaaRadiusEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 15),
    _CfprAaaRadiusEpIntId_Type()
)
cfprAaaRadiusEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpIntId.setStatus("current")
_CfprAaaRadiusEpName_Type = SnmpAdminString
_CfprAaaRadiusEpName_Object = MibTableColumn
cfprAaaRadiusEpName = _CfprAaaRadiusEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 16),
    _CfprAaaRadiusEpName_Type()
)
cfprAaaRadiusEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpName.setStatus("current")
_CfprAaaRadiusEpPolicyLevel_Type = Gauge32
_CfprAaaRadiusEpPolicyLevel_Object = MibTableColumn
cfprAaaRadiusEpPolicyLevel = _CfprAaaRadiusEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 17),
    _CfprAaaRadiusEpPolicyLevel_Type()
)
cfprAaaRadiusEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpPolicyLevel.setStatus("current")
_CfprAaaRadiusEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaRadiusEpPolicyOwner_Object = MibTableColumn
cfprAaaRadiusEpPolicyOwner = _CfprAaaRadiusEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 18),
    _CfprAaaRadiusEpPolicyOwner_Type()
)
cfprAaaRadiusEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpPolicyOwner.setStatus("current")
_CfprAaaRadiusEpRetries_Type = Gauge32
_CfprAaaRadiusEpRetries_Object = MibTableColumn
cfprAaaRadiusEpRetries = _CfprAaaRadiusEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 19),
    _CfprAaaRadiusEpRetries_Type()
)
cfprAaaRadiusEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpRetries.setStatus("current")
_CfprAaaRadiusEpTimeout_Type = Gauge32
_CfprAaaRadiusEpTimeout_Object = MibTableColumn
cfprAaaRadiusEpTimeout = _CfprAaaRadiusEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 30, 1, 20),
    _CfprAaaRadiusEpTimeout_Type()
)
cfprAaaRadiusEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpTimeout.setStatus("current")
_CfprAaaRadiusEpFsmTable_Object = MibTable
cfprAaaRadiusEpFsmTable = _CfprAaaRadiusEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31)
)
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmTable.setStatus("current")
_CfprAaaRadiusEpFsmEntry_Object = MibTableRow
cfprAaaRadiusEpFsmEntry = _CfprAaaRadiusEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1)
)
cfprAaaRadiusEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRadiusEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmEntry.setStatus("current")
_CfprAaaRadiusEpFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaRadiusEpFsmInstanceId_Object = MibTableColumn
cfprAaaRadiusEpFsmInstanceId = _CfprAaaRadiusEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 1),
    _CfprAaaRadiusEpFsmInstanceId_Type()
)
cfprAaaRadiusEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmInstanceId.setStatus("current")
_CfprAaaRadiusEpFsmDn_Type = CfprManagedObjectDn
_CfprAaaRadiusEpFsmDn_Object = MibTableColumn
cfprAaaRadiusEpFsmDn = _CfprAaaRadiusEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 2),
    _CfprAaaRadiusEpFsmDn_Type()
)
cfprAaaRadiusEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmDn.setStatus("current")
_CfprAaaRadiusEpFsmRn_Type = SnmpAdminString
_CfprAaaRadiusEpFsmRn_Object = MibTableColumn
cfprAaaRadiusEpFsmRn = _CfprAaaRadiusEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 3),
    _CfprAaaRadiusEpFsmRn_Type()
)
cfprAaaRadiusEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRn.setStatus("current")
_CfprAaaRadiusEpFsmCompletionTime_Type = DateAndTime
_CfprAaaRadiusEpFsmCompletionTime_Object = MibTableColumn
cfprAaaRadiusEpFsmCompletionTime = _CfprAaaRadiusEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 4),
    _CfprAaaRadiusEpFsmCompletionTime_Type()
)
cfprAaaRadiusEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmCompletionTime.setStatus("current")
_CfprAaaRadiusEpFsmCurrentFsm_Type = CfprAaaRadiusEpFsmCurrentFsm
_CfprAaaRadiusEpFsmCurrentFsm_Object = MibTableColumn
cfprAaaRadiusEpFsmCurrentFsm = _CfprAaaRadiusEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 5),
    _CfprAaaRadiusEpFsmCurrentFsm_Type()
)
cfprAaaRadiusEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmCurrentFsm.setStatus("current")
_CfprAaaRadiusEpFsmDescrData_Type = SnmpAdminString
_CfprAaaRadiusEpFsmDescrData_Object = MibTableColumn
cfprAaaRadiusEpFsmDescrData = _CfprAaaRadiusEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 6),
    _CfprAaaRadiusEpFsmDescrData_Type()
)
cfprAaaRadiusEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmDescrData.setStatus("current")
_CfprAaaRadiusEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaRadiusEpFsmFsmStatus_Object = MibTableColumn
cfprAaaRadiusEpFsmFsmStatus = _CfprAaaRadiusEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 7),
    _CfprAaaRadiusEpFsmFsmStatus_Type()
)
cfprAaaRadiusEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmFsmStatus.setStatus("current")
_CfprAaaRadiusEpFsmProgress_Type = Gauge32
_CfprAaaRadiusEpFsmProgress_Object = MibTableColumn
cfprAaaRadiusEpFsmProgress = _CfprAaaRadiusEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 8),
    _CfprAaaRadiusEpFsmProgress_Type()
)
cfprAaaRadiusEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmProgress.setStatus("current")
_CfprAaaRadiusEpFsmRmtErrCode_Type = Gauge32
_CfprAaaRadiusEpFsmRmtErrCode_Object = MibTableColumn
cfprAaaRadiusEpFsmRmtErrCode = _CfprAaaRadiusEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 9),
    _CfprAaaRadiusEpFsmRmtErrCode_Type()
)
cfprAaaRadiusEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRmtErrCode.setStatus("current")
_CfprAaaRadiusEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaRadiusEpFsmRmtErrDescr_Object = MibTableColumn
cfprAaaRadiusEpFsmRmtErrDescr = _CfprAaaRadiusEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 10),
    _CfprAaaRadiusEpFsmRmtErrDescr_Type()
)
cfprAaaRadiusEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRmtErrDescr.setStatus("current")
_CfprAaaRadiusEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaRadiusEpFsmRmtRslt_Object = MibTableColumn
cfprAaaRadiusEpFsmRmtRslt = _CfprAaaRadiusEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 31, 1, 11),
    _CfprAaaRadiusEpFsmRmtRslt_Type()
)
cfprAaaRadiusEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmRmtRslt.setStatus("current")
_CfprAaaRadiusEpFsmStageTable_Object = MibTable
cfprAaaRadiusEpFsmStageTable = _CfprAaaRadiusEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32)
)
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageTable.setStatus("current")
_CfprAaaRadiusEpFsmStageEntry_Object = MibTableRow
cfprAaaRadiusEpFsmStageEntry = _CfprAaaRadiusEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1)
)
cfprAaaRadiusEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRadiusEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageEntry.setStatus("current")
_CfprAaaRadiusEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaRadiusEpFsmStageInstanceId_Object = MibTableColumn
cfprAaaRadiusEpFsmStageInstanceId = _CfprAaaRadiusEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 1),
    _CfprAaaRadiusEpFsmStageInstanceId_Type()
)
cfprAaaRadiusEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageInstanceId.setStatus("current")
_CfprAaaRadiusEpFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaRadiusEpFsmStageDn_Object = MibTableColumn
cfprAaaRadiusEpFsmStageDn = _CfprAaaRadiusEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 2),
    _CfprAaaRadiusEpFsmStageDn_Type()
)
cfprAaaRadiusEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageDn.setStatus("current")
_CfprAaaRadiusEpFsmStageRn_Type = SnmpAdminString
_CfprAaaRadiusEpFsmStageRn_Object = MibTableColumn
cfprAaaRadiusEpFsmStageRn = _CfprAaaRadiusEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 3),
    _CfprAaaRadiusEpFsmStageRn_Type()
)
cfprAaaRadiusEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageRn.setStatus("current")
_CfprAaaRadiusEpFsmStageDescrData_Type = SnmpAdminString
_CfprAaaRadiusEpFsmStageDescrData_Object = MibTableColumn
cfprAaaRadiusEpFsmStageDescrData = _CfprAaaRadiusEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 4),
    _CfprAaaRadiusEpFsmStageDescrData_Type()
)
cfprAaaRadiusEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageDescrData.setStatus("current")
_CfprAaaRadiusEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaRadiusEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaRadiusEpFsmStageLastUpdateTime = _CfprAaaRadiusEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 5),
    _CfprAaaRadiusEpFsmStageLastUpdateTime_Type()
)
cfprAaaRadiusEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageLastUpdateTime.setStatus("current")
_CfprAaaRadiusEpFsmStageName_Type = CfprAaaRadiusEpFsmStageName
_CfprAaaRadiusEpFsmStageName_Object = MibTableColumn
cfprAaaRadiusEpFsmStageName = _CfprAaaRadiusEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 6),
    _CfprAaaRadiusEpFsmStageName_Type()
)
cfprAaaRadiusEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageName.setStatus("current")
_CfprAaaRadiusEpFsmStageOrder_Type = Gauge32
_CfprAaaRadiusEpFsmStageOrder_Object = MibTableColumn
cfprAaaRadiusEpFsmStageOrder = _CfprAaaRadiusEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 7),
    _CfprAaaRadiusEpFsmStageOrder_Type()
)
cfprAaaRadiusEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageOrder.setStatus("current")
_CfprAaaRadiusEpFsmStageRetry_Type = Gauge32
_CfprAaaRadiusEpFsmStageRetry_Object = MibTableColumn
cfprAaaRadiusEpFsmStageRetry = _CfprAaaRadiusEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 8),
    _CfprAaaRadiusEpFsmStageRetry_Type()
)
cfprAaaRadiusEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageRetry.setStatus("current")
_CfprAaaRadiusEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaRadiusEpFsmStageStageStatus_Object = MibTableColumn
cfprAaaRadiusEpFsmStageStageStatus = _CfprAaaRadiusEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 32, 1, 9),
    _CfprAaaRadiusEpFsmStageStageStatus_Type()
)
cfprAaaRadiusEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusEpFsmStageStageStatus.setStatus("current")
_CfprAaaRadiusProviderTable_Object = MibTable
cfprAaaRadiusProviderTable = _CfprAaaRadiusProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33)
)
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderTable.setStatus("current")
_CfprAaaRadiusProviderEntry_Object = MibTableRow
cfprAaaRadiusProviderEntry = _CfprAaaRadiusProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1)
)
cfprAaaRadiusProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRadiusProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderEntry.setStatus("current")
_CfprAaaRadiusProviderInstanceId_Type = CfprManagedObjectId
_CfprAaaRadiusProviderInstanceId_Object = MibTableColumn
cfprAaaRadiusProviderInstanceId = _CfprAaaRadiusProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 1),
    _CfprAaaRadiusProviderInstanceId_Type()
)
cfprAaaRadiusProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderInstanceId.setStatus("current")
_CfprAaaRadiusProviderDn_Type = CfprManagedObjectDn
_CfprAaaRadiusProviderDn_Object = MibTableColumn
cfprAaaRadiusProviderDn = _CfprAaaRadiusProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 2),
    _CfprAaaRadiusProviderDn_Type()
)
cfprAaaRadiusProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderDn.setStatus("current")
_CfprAaaRadiusProviderRn_Type = SnmpAdminString
_CfprAaaRadiusProviderRn_Object = MibTableColumn
cfprAaaRadiusProviderRn = _CfprAaaRadiusProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 3),
    _CfprAaaRadiusProviderRn_Type()
)
cfprAaaRadiusProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderRn.setStatus("current")
_CfprAaaRadiusProviderAuthPort_Type = Gauge32
_CfprAaaRadiusProviderAuthPort_Object = MibTableColumn
cfprAaaRadiusProviderAuthPort = _CfprAaaRadiusProviderAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 4),
    _CfprAaaRadiusProviderAuthPort_Type()
)
cfprAaaRadiusProviderAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderAuthPort.setStatus("current")
_CfprAaaRadiusProviderDescr_Type = SnmpAdminString
_CfprAaaRadiusProviderDescr_Object = MibTableColumn
cfprAaaRadiusProviderDescr = _CfprAaaRadiusProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 5),
    _CfprAaaRadiusProviderDescr_Type()
)
cfprAaaRadiusProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderDescr.setStatus("current")
_CfprAaaRadiusProviderEncKey_Type = SnmpAdminString
_CfprAaaRadiusProviderEncKey_Object = MibTableColumn
cfprAaaRadiusProviderEncKey = _CfprAaaRadiusProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 6),
    _CfprAaaRadiusProviderEncKey_Type()
)
cfprAaaRadiusProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderEncKey.setStatus("current")
_CfprAaaRadiusProviderKey_Type = SnmpAdminString
_CfprAaaRadiusProviderKey_Object = MibTableColumn
cfprAaaRadiusProviderKey = _CfprAaaRadiusProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 7),
    _CfprAaaRadiusProviderKey_Type()
)
cfprAaaRadiusProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderKey.setStatus("current")
_CfprAaaRadiusProviderKeySet_Type = TruthValue
_CfprAaaRadiusProviderKeySet_Object = MibTableColumn
cfprAaaRadiusProviderKeySet = _CfprAaaRadiusProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 8),
    _CfprAaaRadiusProviderKeySet_Type()
)
cfprAaaRadiusProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderKeySet.setStatus("current")
_CfprAaaRadiusProviderName_Type = SnmpAdminString
_CfprAaaRadiusProviderName_Object = MibTableColumn
cfprAaaRadiusProviderName = _CfprAaaRadiusProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 9),
    _CfprAaaRadiusProviderName_Type()
)
cfprAaaRadiusProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderName.setStatus("current")
_CfprAaaRadiusProviderOrder_Type = Gauge32
_CfprAaaRadiusProviderOrder_Object = MibTableColumn
cfprAaaRadiusProviderOrder = _CfprAaaRadiusProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 10),
    _CfprAaaRadiusProviderOrder_Type()
)
cfprAaaRadiusProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderOrder.setStatus("current")
_CfprAaaRadiusProviderRetries_Type = Gauge32
_CfprAaaRadiusProviderRetries_Object = MibTableColumn
cfprAaaRadiusProviderRetries = _CfprAaaRadiusProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 11),
    _CfprAaaRadiusProviderRetries_Type()
)
cfprAaaRadiusProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderRetries.setStatus("current")
_CfprAaaRadiusProviderService_Type = CfprAaaRadiusService
_CfprAaaRadiusProviderService_Object = MibTableColumn
cfprAaaRadiusProviderService = _CfprAaaRadiusProviderService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 12),
    _CfprAaaRadiusProviderService_Type()
)
cfprAaaRadiusProviderService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderService.setStatus("current")
_CfprAaaRadiusProviderTimeout_Type = Gauge32
_CfprAaaRadiusProviderTimeout_Object = MibTableColumn
cfprAaaRadiusProviderTimeout = _CfprAaaRadiusProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 33, 1, 13),
    _CfprAaaRadiusProviderTimeout_Type()
)
cfprAaaRadiusProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRadiusProviderTimeout.setStatus("current")
_CfprAaaRealmFsmTable_Object = MibTable
cfprAaaRealmFsmTable = _CfprAaaRealmFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34)
)
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTable.setStatus("current")
_CfprAaaRealmFsmEntry_Object = MibTableRow
cfprAaaRealmFsmEntry = _CfprAaaRealmFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1)
)
cfprAaaRealmFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRealmFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRealmFsmEntry.setStatus("current")
_CfprAaaRealmFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaRealmFsmInstanceId_Object = MibTableColumn
cfprAaaRealmFsmInstanceId = _CfprAaaRealmFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 1),
    _CfprAaaRealmFsmInstanceId_Type()
)
cfprAaaRealmFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmInstanceId.setStatus("current")
_CfprAaaRealmFsmDn_Type = CfprManagedObjectDn
_CfprAaaRealmFsmDn_Object = MibTableColumn
cfprAaaRealmFsmDn = _CfprAaaRealmFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 2),
    _CfprAaaRealmFsmDn_Type()
)
cfprAaaRealmFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmDn.setStatus("current")
_CfprAaaRealmFsmRn_Type = SnmpAdminString
_CfprAaaRealmFsmRn_Object = MibTableColumn
cfprAaaRealmFsmRn = _CfprAaaRealmFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 3),
    _CfprAaaRealmFsmRn_Type()
)
cfprAaaRealmFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmRn.setStatus("current")
_CfprAaaRealmFsmCompletionTime_Type = DateAndTime
_CfprAaaRealmFsmCompletionTime_Object = MibTableColumn
cfprAaaRealmFsmCompletionTime = _CfprAaaRealmFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 4),
    _CfprAaaRealmFsmCompletionTime_Type()
)
cfprAaaRealmFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmCompletionTime.setStatus("current")
_CfprAaaRealmFsmCurrentFsm_Type = CfprAaaRealmFsmCurrentFsm
_CfprAaaRealmFsmCurrentFsm_Object = MibTableColumn
cfprAaaRealmFsmCurrentFsm = _CfprAaaRealmFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 5),
    _CfprAaaRealmFsmCurrentFsm_Type()
)
cfprAaaRealmFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmCurrentFsm.setStatus("current")
_CfprAaaRealmFsmDescr_Type = SnmpAdminString
_CfprAaaRealmFsmDescr_Object = MibTableColumn
cfprAaaRealmFsmDescr = _CfprAaaRealmFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 6),
    _CfprAaaRealmFsmDescr_Type()
)
cfprAaaRealmFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmDescr.setStatus("current")
_CfprAaaRealmFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaRealmFsmFsmStatus_Object = MibTableColumn
cfprAaaRealmFsmFsmStatus = _CfprAaaRealmFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 7),
    _CfprAaaRealmFsmFsmStatus_Type()
)
cfprAaaRealmFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmFsmStatus.setStatus("current")
_CfprAaaRealmFsmProgress_Type = Gauge32
_CfprAaaRealmFsmProgress_Object = MibTableColumn
cfprAaaRealmFsmProgress = _CfprAaaRealmFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 8),
    _CfprAaaRealmFsmProgress_Type()
)
cfprAaaRealmFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmProgress.setStatus("current")
_CfprAaaRealmFsmRmtErrCode_Type = Gauge32
_CfprAaaRealmFsmRmtErrCode_Object = MibTableColumn
cfprAaaRealmFsmRmtErrCode = _CfprAaaRealmFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 9),
    _CfprAaaRealmFsmRmtErrCode_Type()
)
cfprAaaRealmFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmRmtErrCode.setStatus("current")
_CfprAaaRealmFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaRealmFsmRmtErrDescr_Object = MibTableColumn
cfprAaaRealmFsmRmtErrDescr = _CfprAaaRealmFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 10),
    _CfprAaaRealmFsmRmtErrDescr_Type()
)
cfprAaaRealmFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmRmtErrDescr.setStatus("current")
_CfprAaaRealmFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaRealmFsmRmtRslt_Object = MibTableColumn
cfprAaaRealmFsmRmtRslt = _CfprAaaRealmFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 34, 1, 11),
    _CfprAaaRealmFsmRmtRslt_Type()
)
cfprAaaRealmFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmRmtRslt.setStatus("current")
_CfprAaaRealmFsmStageTable_Object = MibTable
cfprAaaRealmFsmStageTable = _CfprAaaRealmFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35)
)
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageTable.setStatus("current")
_CfprAaaRealmFsmStageEntry_Object = MibTableRow
cfprAaaRealmFsmStageEntry = _CfprAaaRealmFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1)
)
cfprAaaRealmFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRealmFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageEntry.setStatus("current")
_CfprAaaRealmFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaRealmFsmStageInstanceId_Object = MibTableColumn
cfprAaaRealmFsmStageInstanceId = _CfprAaaRealmFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 1),
    _CfprAaaRealmFsmStageInstanceId_Type()
)
cfprAaaRealmFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageInstanceId.setStatus("current")
_CfprAaaRealmFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaRealmFsmStageDn_Object = MibTableColumn
cfprAaaRealmFsmStageDn = _CfprAaaRealmFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 2),
    _CfprAaaRealmFsmStageDn_Type()
)
cfprAaaRealmFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageDn.setStatus("current")
_CfprAaaRealmFsmStageRn_Type = SnmpAdminString
_CfprAaaRealmFsmStageRn_Object = MibTableColumn
cfprAaaRealmFsmStageRn = _CfprAaaRealmFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 3),
    _CfprAaaRealmFsmStageRn_Type()
)
cfprAaaRealmFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageRn.setStatus("current")
_CfprAaaRealmFsmStageDescr_Type = SnmpAdminString
_CfprAaaRealmFsmStageDescr_Object = MibTableColumn
cfprAaaRealmFsmStageDescr = _CfprAaaRealmFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 4),
    _CfprAaaRealmFsmStageDescr_Type()
)
cfprAaaRealmFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageDescr.setStatus("current")
_CfprAaaRealmFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaRealmFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaRealmFsmStageLastUpdateTime = _CfprAaaRealmFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 5),
    _CfprAaaRealmFsmStageLastUpdateTime_Type()
)
cfprAaaRealmFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageLastUpdateTime.setStatus("current")
_CfprAaaRealmFsmStageName_Type = CfprAaaRealmFsmStageName
_CfprAaaRealmFsmStageName_Object = MibTableColumn
cfprAaaRealmFsmStageName = _CfprAaaRealmFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 6),
    _CfprAaaRealmFsmStageName_Type()
)
cfprAaaRealmFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageName.setStatus("current")
_CfprAaaRealmFsmStageOrder_Type = Gauge32
_CfprAaaRealmFsmStageOrder_Object = MibTableColumn
cfprAaaRealmFsmStageOrder = _CfprAaaRealmFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 7),
    _CfprAaaRealmFsmStageOrder_Type()
)
cfprAaaRealmFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageOrder.setStatus("current")
_CfprAaaRealmFsmStageRetry_Type = Gauge32
_CfprAaaRealmFsmStageRetry_Object = MibTableColumn
cfprAaaRealmFsmStageRetry = _CfprAaaRealmFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 8),
    _CfprAaaRealmFsmStageRetry_Type()
)
cfprAaaRealmFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageRetry.setStatus("current")
_CfprAaaRealmFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaRealmFsmStageStageStatus_Object = MibTableColumn
cfprAaaRealmFsmStageStageStatus = _CfprAaaRealmFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 35, 1, 9),
    _CfprAaaRealmFsmStageStageStatus_Type()
)
cfprAaaRealmFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmStageStageStatus.setStatus("current")
_CfprAaaRealmFsmTaskTable_Object = MibTable
cfprAaaRealmFsmTaskTable = _CfprAaaRealmFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36)
)
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskTable.setStatus("current")
_CfprAaaRealmFsmTaskEntry_Object = MibTableRow
cfprAaaRealmFsmTaskEntry = _CfprAaaRealmFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1)
)
cfprAaaRealmFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRealmFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskEntry.setStatus("current")
_CfprAaaRealmFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprAaaRealmFsmTaskInstanceId_Object = MibTableColumn
cfprAaaRealmFsmTaskInstanceId = _CfprAaaRealmFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 1),
    _CfprAaaRealmFsmTaskInstanceId_Type()
)
cfprAaaRealmFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskInstanceId.setStatus("current")
_CfprAaaRealmFsmTaskDn_Type = CfprManagedObjectDn
_CfprAaaRealmFsmTaskDn_Object = MibTableColumn
cfprAaaRealmFsmTaskDn = _CfprAaaRealmFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 2),
    _CfprAaaRealmFsmTaskDn_Type()
)
cfprAaaRealmFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskDn.setStatus("current")
_CfprAaaRealmFsmTaskRn_Type = SnmpAdminString
_CfprAaaRealmFsmTaskRn_Object = MibTableColumn
cfprAaaRealmFsmTaskRn = _CfprAaaRealmFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 3),
    _CfprAaaRealmFsmTaskRn_Type()
)
cfprAaaRealmFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskRn.setStatus("current")
_CfprAaaRealmFsmTaskCompletion_Type = CfprFsmCompletion
_CfprAaaRealmFsmTaskCompletion_Object = MibTableColumn
cfprAaaRealmFsmTaskCompletion = _CfprAaaRealmFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 4),
    _CfprAaaRealmFsmTaskCompletion_Type()
)
cfprAaaRealmFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskCompletion.setStatus("current")
_CfprAaaRealmFsmTaskFlags_Type = CfprFsmFlags
_CfprAaaRealmFsmTaskFlags_Object = MibTableColumn
cfprAaaRealmFsmTaskFlags = _CfprAaaRealmFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 5),
    _CfprAaaRealmFsmTaskFlags_Type()
)
cfprAaaRealmFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskFlags.setStatus("current")
_CfprAaaRealmFsmTaskItem_Type = CfprAaaRealmFsmTaskItem
_CfprAaaRealmFsmTaskItem_Object = MibTableColumn
cfprAaaRealmFsmTaskItem = _CfprAaaRealmFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 6),
    _CfprAaaRealmFsmTaskItem_Type()
)
cfprAaaRealmFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskItem.setStatus("current")
_CfprAaaRealmFsmTaskSeqId_Type = Gauge32
_CfprAaaRealmFsmTaskSeqId_Object = MibTableColumn
cfprAaaRealmFsmTaskSeqId = _CfprAaaRealmFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 36, 1, 7),
    _CfprAaaRealmFsmTaskSeqId_Type()
)
cfprAaaRealmFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRealmFsmTaskSeqId.setStatus("current")
_CfprAaaRemoteUserTable_Object = MibTable
cfprAaaRemoteUserTable = _CfprAaaRemoteUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37)
)
if mibBuilder.loadTexts:
    cfprAaaRemoteUserTable.setStatus("current")
_CfprAaaRemoteUserEntry_Object = MibTableRow
cfprAaaRemoteUserEntry = _CfprAaaRemoteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1)
)
cfprAaaRemoteUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRemoteUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRemoteUserEntry.setStatus("current")
_CfprAaaRemoteUserInstanceId_Type = CfprManagedObjectId
_CfprAaaRemoteUserInstanceId_Object = MibTableColumn
cfprAaaRemoteUserInstanceId = _CfprAaaRemoteUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 1),
    _CfprAaaRemoteUserInstanceId_Type()
)
cfprAaaRemoteUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserInstanceId.setStatus("current")
_CfprAaaRemoteUserDn_Type = CfprManagedObjectDn
_CfprAaaRemoteUserDn_Object = MibTableColumn
cfprAaaRemoteUserDn = _CfprAaaRemoteUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 2),
    _CfprAaaRemoteUserDn_Type()
)
cfprAaaRemoteUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserDn.setStatus("current")
_CfprAaaRemoteUserRn_Type = SnmpAdminString
_CfprAaaRemoteUserRn_Object = MibTableColumn
cfprAaaRemoteUserRn = _CfprAaaRemoteUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 3),
    _CfprAaaRemoteUserRn_Type()
)
cfprAaaRemoteUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserRn.setStatus("current")
_CfprAaaRemoteUserConfigState_Type = CfprAaaConfigState
_CfprAaaRemoteUserConfigState_Object = MibTableColumn
cfprAaaRemoteUserConfigState = _CfprAaaRemoteUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 4),
    _CfprAaaRemoteUserConfigState_Type()
)
cfprAaaRemoteUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserConfigState.setStatus("current")
_CfprAaaRemoteUserConfigStatusMessage_Type = SnmpAdminString
_CfprAaaRemoteUserConfigStatusMessage_Object = MibTableColumn
cfprAaaRemoteUserConfigStatusMessage = _CfprAaaRemoteUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 5),
    _CfprAaaRemoteUserConfigStatusMessage_Type()
)
cfprAaaRemoteUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserConfigStatusMessage.setStatus("current")
_CfprAaaRemoteUserDescr_Type = SnmpAdminString
_CfprAaaRemoteUserDescr_Object = MibTableColumn
cfprAaaRemoteUserDescr = _CfprAaaRemoteUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 6),
    _CfprAaaRemoteUserDescr_Type()
)
cfprAaaRemoteUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserDescr.setStatus("current")
_CfprAaaRemoteUserName_Type = SnmpAdminString
_CfprAaaRemoteUserName_Object = MibTableColumn
cfprAaaRemoteUserName = _CfprAaaRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 7),
    _CfprAaaRemoteUserName_Type()
)
cfprAaaRemoteUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserName.setStatus("current")
_CfprAaaRemoteUserPwd_Type = SnmpAdminString
_CfprAaaRemoteUserPwd_Object = MibTableColumn
cfprAaaRemoteUserPwd = _CfprAaaRemoteUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 8),
    _CfprAaaRemoteUserPwd_Type()
)
cfprAaaRemoteUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserPwd.setStatus("current")
_CfprAaaRemoteUserPwdSet_Type = TruthValue
_CfprAaaRemoteUserPwdSet_Object = MibTableColumn
cfprAaaRemoteUserPwdSet = _CfprAaaRemoteUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 37, 1, 9),
    _CfprAaaRemoteUserPwdSet_Type()
)
cfprAaaRemoteUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRemoteUserPwdSet.setStatus("current")
_CfprAaaRoleTable_Object = MibTable
cfprAaaRoleTable = _CfprAaaRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38)
)
if mibBuilder.loadTexts:
    cfprAaaRoleTable.setStatus("current")
_CfprAaaRoleEntry_Object = MibTableRow
cfprAaaRoleEntry = _CfprAaaRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1)
)
cfprAaaRoleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRoleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRoleEntry.setStatus("current")
_CfprAaaRoleInstanceId_Type = CfprManagedObjectId
_CfprAaaRoleInstanceId_Object = MibTableColumn
cfprAaaRoleInstanceId = _CfprAaaRoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 1),
    _CfprAaaRoleInstanceId_Type()
)
cfprAaaRoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRoleInstanceId.setStatus("current")
_CfprAaaRoleDn_Type = CfprManagedObjectDn
_CfprAaaRoleDn_Object = MibTableColumn
cfprAaaRoleDn = _CfprAaaRoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 2),
    _CfprAaaRoleDn_Type()
)
cfprAaaRoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleDn.setStatus("current")
_CfprAaaRoleRn_Type = SnmpAdminString
_CfprAaaRoleRn_Object = MibTableColumn
cfprAaaRoleRn = _CfprAaaRoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 3),
    _CfprAaaRoleRn_Type()
)
cfprAaaRoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRn.setStatus("current")
_CfprAaaRoleConfigState_Type = CfprAaaConfigState
_CfprAaaRoleConfigState_Object = MibTableColumn
cfprAaaRoleConfigState = _CfprAaaRoleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 4),
    _CfprAaaRoleConfigState_Type()
)
cfprAaaRoleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleConfigState.setStatus("current")
_CfprAaaRoleConfigStatusMessage_Type = SnmpAdminString
_CfprAaaRoleConfigStatusMessage_Object = MibTableColumn
cfprAaaRoleConfigStatusMessage = _CfprAaaRoleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 5),
    _CfprAaaRoleConfigStatusMessage_Type()
)
cfprAaaRoleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleConfigStatusMessage.setStatus("current")
_CfprAaaRoleDescr_Type = SnmpAdminString
_CfprAaaRoleDescr_Object = MibTableColumn
cfprAaaRoleDescr = _CfprAaaRoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 6),
    _CfprAaaRoleDescr_Type()
)
cfprAaaRoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleDescr.setStatus("current")
_CfprAaaRoleIntId_Type = SnmpAdminString
_CfprAaaRoleIntId_Object = MibTableColumn
cfprAaaRoleIntId = _CfprAaaRoleIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 7),
    _CfprAaaRoleIntId_Type()
)
cfprAaaRoleIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleIntId.setStatus("current")
_CfprAaaRoleName_Type = SnmpAdminString
_CfprAaaRoleName_Object = MibTableColumn
cfprAaaRoleName = _CfprAaaRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 8),
    _CfprAaaRoleName_Type()
)
cfprAaaRoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleName.setStatus("current")
_CfprAaaRolePolicyLevel_Type = Gauge32
_CfprAaaRolePolicyLevel_Object = MibTableColumn
cfprAaaRolePolicyLevel = _CfprAaaRolePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 9),
    _CfprAaaRolePolicyLevel_Type()
)
cfprAaaRolePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRolePolicyLevel.setStatus("current")
_CfprAaaRolePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaRolePolicyOwner_Object = MibTableColumn
cfprAaaRolePolicyOwner = _CfprAaaRolePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 10),
    _CfprAaaRolePolicyOwner_Type()
)
cfprAaaRolePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRolePolicyOwner.setStatus("current")
_CfprAaaRolePriv_Type = CfprAaaAccess
_CfprAaaRolePriv_Object = MibTableColumn
cfprAaaRolePriv = _CfprAaaRolePriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 38, 1, 11),
    _CfprAaaRolePriv_Type()
)
cfprAaaRolePriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRolePriv.setStatus("current")
_CfprAaaSessionTable_Object = MibTable
cfprAaaSessionTable = _CfprAaaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39)
)
if mibBuilder.loadTexts:
    cfprAaaSessionTable.setStatus("current")
_CfprAaaSessionEntry_Object = MibTableRow
cfprAaaSessionEntry = _CfprAaaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1)
)
cfprAaaSessionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSessionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSessionEntry.setStatus("current")
_CfprAaaSessionInstanceId_Type = CfprManagedObjectId
_CfprAaaSessionInstanceId_Object = MibTableColumn
cfprAaaSessionInstanceId = _CfprAaaSessionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 1),
    _CfprAaaSessionInstanceId_Type()
)
cfprAaaSessionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSessionInstanceId.setStatus("current")
_CfprAaaSessionDn_Type = CfprManagedObjectDn
_CfprAaaSessionDn_Object = MibTableColumn
cfprAaaSessionDn = _CfprAaaSessionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 2),
    _CfprAaaSessionDn_Type()
)
cfprAaaSessionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionDn.setStatus("current")
_CfprAaaSessionRn_Type = SnmpAdminString
_CfprAaaSessionRn_Object = MibTableColumn
cfprAaaSessionRn = _CfprAaaSessionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 3),
    _CfprAaaSessionRn_Type()
)
cfprAaaSessionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionRn.setStatus("current")
_CfprAaaSessionHost_Type = SnmpAdminString
_CfprAaaSessionHost_Object = MibTableColumn
cfprAaaSessionHost = _CfprAaaSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 4),
    _CfprAaaSessionHost_Type()
)
cfprAaaSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionHost.setStatus("current")
_CfprAaaSessionId_Type = SnmpAdminString
_CfprAaaSessionId_Object = MibTableColumn
cfprAaaSessionId = _CfprAaaSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 5),
    _CfprAaaSessionId_Type()
)
cfprAaaSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionId.setStatus("current")
_CfprAaaSessionIntDel_Type = TruthValue
_CfprAaaSessionIntDel_Object = MibTableColumn
cfprAaaSessionIntDel = _CfprAaaSessionIntDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 6),
    _CfprAaaSessionIntDel_Type()
)
cfprAaaSessionIntDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionIntDel.setStatus("current")
_CfprAaaSessionLoginTime_Type = DateAndTime
_CfprAaaSessionLoginTime_Object = MibTableColumn
cfprAaaSessionLoginTime = _CfprAaaSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 7),
    _CfprAaaSessionLoginTime_Type()
)
cfprAaaSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLoginTime.setStatus("current")
_CfprAaaSessionPid_Type = Gauge32
_CfprAaaSessionPid_Object = MibTableColumn
cfprAaaSessionPid = _CfprAaaSessionPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 8),
    _CfprAaaSessionPid_Type()
)
cfprAaaSessionPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionPid.setStatus("current")
_CfprAaaSessionRefreshPeriod_Type = Gauge32
_CfprAaaSessionRefreshPeriod_Object = MibTableColumn
cfprAaaSessionRefreshPeriod = _CfprAaaSessionRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 9),
    _CfprAaaSessionRefreshPeriod_Type()
)
cfprAaaSessionRefreshPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionRefreshPeriod.setStatus("current")
_CfprAaaSessionSessionTimeout_Type = Gauge32
_CfprAaaSessionSessionTimeout_Object = MibTableColumn
cfprAaaSessionSessionTimeout = _CfprAaaSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 10),
    _CfprAaaSessionSessionTimeout_Type()
)
cfprAaaSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionSessionTimeout.setStatus("current")
_CfprAaaSessionSwitchId_Type = CfprNetworkSwitchId
_CfprAaaSessionSwitchId_Object = MibTableColumn
cfprAaaSessionSwitchId = _CfprAaaSessionSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 11),
    _CfprAaaSessionSwitchId_Type()
)
cfprAaaSessionSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionSwitchId.setStatus("current")
_CfprAaaSessionTerm_Type = SnmpAdminString
_CfprAaaSessionTerm_Object = MibTableColumn
cfprAaaSessionTerm = _CfprAaaSessionTerm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 12),
    _CfprAaaSessionTerm_Type()
)
cfprAaaSessionTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionTerm.setStatus("current")
_CfprAaaSessionUi_Type = CfprAaaUserInterface
_CfprAaaSessionUi_Object = MibTableColumn
cfprAaaSessionUi = _CfprAaaSessionUi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 13),
    _CfprAaaSessionUi_Type()
)
cfprAaaSessionUi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionUi.setStatus("current")
_CfprAaaSessionUser_Type = SnmpAdminString
_CfprAaaSessionUser_Object = MibTableColumn
cfprAaaSessionUser = _CfprAaaSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 14),
    _CfprAaaSessionUser_Type()
)
cfprAaaSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionUser.setStatus("current")
_CfprAaaSessionAbsoluteSessionTimeout_Type = Gauge32
_CfprAaaSessionAbsoluteSessionTimeout_Object = MibTableColumn
cfprAaaSessionAbsoluteSessionTimeout = _CfprAaaSessionAbsoluteSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 39, 1, 15),
    _CfprAaaSessionAbsoluteSessionTimeout_Type()
)
cfprAaaSessionAbsoluteSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionAbsoluteSessionTimeout.setStatus("current")
_CfprAaaSessionInfoTable_Object = MibTable
cfprAaaSessionInfoTable = _CfprAaaSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40)
)
if mibBuilder.loadTexts:
    cfprAaaSessionInfoTable.setStatus("current")
_CfprAaaSessionInfoEntry_Object = MibTableRow
cfprAaaSessionInfoEntry = _CfprAaaSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1)
)
cfprAaaSessionInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSessionInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSessionInfoEntry.setStatus("current")
_CfprAaaSessionInfoInstanceId_Type = CfprManagedObjectId
_CfprAaaSessionInfoInstanceId_Object = MibTableColumn
cfprAaaSessionInfoInstanceId = _CfprAaaSessionInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 1),
    _CfprAaaSessionInfoInstanceId_Type()
)
cfprAaaSessionInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoInstanceId.setStatus("current")
_CfprAaaSessionInfoDn_Type = CfprManagedObjectDn
_CfprAaaSessionInfoDn_Object = MibTableColumn
cfprAaaSessionInfoDn = _CfprAaaSessionInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 2),
    _CfprAaaSessionInfoDn_Type()
)
cfprAaaSessionInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoDn.setStatus("current")
_CfprAaaSessionInfoRn_Type = SnmpAdminString
_CfprAaaSessionInfoRn_Object = MibTableColumn
cfprAaaSessionInfoRn = _CfprAaaSessionInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 3),
    _CfprAaaSessionInfoRn_Type()
)
cfprAaaSessionInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoRn.setStatus("current")
_CfprAaaSessionInfoAddress_Type = SnmpAdminString
_CfprAaaSessionInfoAddress_Object = MibTableColumn
cfprAaaSessionInfoAddress = _CfprAaaSessionInfoAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 4),
    _CfprAaaSessionInfoAddress_Type()
)
cfprAaaSessionInfoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoAddress.setStatus("current")
_CfprAaaSessionInfoDestIp_Type = SnmpAdminString
_CfprAaaSessionInfoDestIp_Object = MibTableColumn
cfprAaaSessionInfoDestIp = _CfprAaaSessionInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 5),
    _CfprAaaSessionInfoDestIp_Type()
)
cfprAaaSessionInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoDestIp.setStatus("current")
_CfprAaaSessionInfoEtime_Type = DateAndTime
_CfprAaaSessionInfoEtime_Object = MibTableColumn
cfprAaaSessionInfoEtime = _CfprAaaSessionInfoEtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 6),
    _CfprAaaSessionInfoEtime_Type()
)
cfprAaaSessionInfoEtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoEtime.setStatus("current")
_CfprAaaSessionInfoId_Type = SnmpAdminString
_CfprAaaSessionInfoId_Object = MibTableColumn
cfprAaaSessionInfoId = _CfprAaaSessionInfoId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 7),
    _CfprAaaSessionInfoId_Type()
)
cfprAaaSessionInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoId.setStatus("current")
_CfprAaaSessionInfoPriv_Type = SnmpAdminString
_CfprAaaSessionInfoPriv_Object = MibTableColumn
cfprAaaSessionInfoPriv = _CfprAaaSessionInfoPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 8),
    _CfprAaaSessionInfoPriv_Type()
)
cfprAaaSessionInfoPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoPriv.setStatus("current")
_CfprAaaSessionInfoType_Type = CfprAaaCimcSessionType
_CfprAaaSessionInfoType_Object = MibTableColumn
cfprAaaSessionInfoType = _CfprAaaSessionInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 9),
    _CfprAaaSessionInfoType_Type()
)
cfprAaaSessionInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoType.setStatus("current")
_CfprAaaSessionInfoUser_Type = SnmpAdminString
_CfprAaaSessionInfoUser_Object = MibTableColumn
cfprAaaSessionInfoUser = _CfprAaaSessionInfoUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 10),
    _CfprAaaSessionInfoUser_Type()
)
cfprAaaSessionInfoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoUser.setStatus("current")
_CfprAaaSessionInfoUserType_Type = CfprAaaSession
_CfprAaaSessionInfoUserType_Object = MibTableColumn
cfprAaaSessionInfoUserType = _CfprAaaSessionInfoUserType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 40, 1, 11),
    _CfprAaaSessionInfoUserType_Type()
)
cfprAaaSessionInfoUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoUserType.setStatus("current")
_CfprAaaSessionInfoTableTable_Object = MibTable
cfprAaaSessionInfoTableTable = _CfprAaaSessionInfoTableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 41)
)
if mibBuilder.loadTexts:
    cfprAaaSessionInfoTableTable.setStatus("current")
_CfprAaaSessionInfoTableEntry_Object = MibTableRow
cfprAaaSessionInfoTableEntry = _CfprAaaSessionInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 41, 1)
)
cfprAaaSessionInfoTableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSessionInfoTableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSessionInfoTableEntry.setStatus("current")
_CfprAaaSessionInfoTableInstanceId_Type = CfprManagedObjectId
_CfprAaaSessionInfoTableInstanceId_Object = MibTableColumn
cfprAaaSessionInfoTableInstanceId = _CfprAaaSessionInfoTableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 41, 1, 1),
    _CfprAaaSessionInfoTableInstanceId_Type()
)
cfprAaaSessionInfoTableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoTableInstanceId.setStatus("current")
_CfprAaaSessionInfoTableDn_Type = CfprManagedObjectDn
_CfprAaaSessionInfoTableDn_Object = MibTableColumn
cfprAaaSessionInfoTableDn = _CfprAaaSessionInfoTableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 41, 1, 2),
    _CfprAaaSessionInfoTableDn_Type()
)
cfprAaaSessionInfoTableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoTableDn.setStatus("current")
_CfprAaaSessionInfoTableRn_Type = SnmpAdminString
_CfprAaaSessionInfoTableRn_Object = MibTableColumn
cfprAaaSessionInfoTableRn = _CfprAaaSessionInfoTableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 41, 1, 3),
    _CfprAaaSessionInfoTableRn_Type()
)
cfprAaaSessionInfoTableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionInfoTableRn.setStatus("current")
_CfprAaaSessionLRTable_Object = MibTable
cfprAaaSessionLRTable = _CfprAaaSessionLRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42)
)
if mibBuilder.loadTexts:
    cfprAaaSessionLRTable.setStatus("current")
_CfprAaaSessionLREntry_Object = MibTableRow
cfprAaaSessionLREntry = _CfprAaaSessionLREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1)
)
cfprAaaSessionLREntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSessionLRInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSessionLREntry.setStatus("current")
_CfprAaaSessionLRInstanceId_Type = CfprManagedObjectId
_CfprAaaSessionLRInstanceId_Object = MibTableColumn
cfprAaaSessionLRInstanceId = _CfprAaaSessionLRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 1),
    _CfprAaaSessionLRInstanceId_Type()
)
cfprAaaSessionLRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSessionLRInstanceId.setStatus("current")
_CfprAaaSessionLRDn_Type = CfprManagedObjectDn
_CfprAaaSessionLRDn_Object = MibTableColumn
cfprAaaSessionLRDn = _CfprAaaSessionLRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 2),
    _CfprAaaSessionLRDn_Type()
)
cfprAaaSessionLRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRDn.setStatus("current")
_CfprAaaSessionLRRn_Type = SnmpAdminString
_CfprAaaSessionLRRn_Object = MibTableColumn
cfprAaaSessionLRRn = _CfprAaaSessionLRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 3),
    _CfprAaaSessionLRRn_Type()
)
cfprAaaSessionLRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRRn.setStatus("current")
_CfprAaaSessionLRAffected_Type = SnmpAdminString
_CfprAaaSessionLRAffected_Object = MibTableColumn
cfprAaaSessionLRAffected = _CfprAaaSessionLRAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 4),
    _CfprAaaSessionLRAffected_Type()
)
cfprAaaSessionLRAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRAffected.setStatus("current")
_CfprAaaSessionLRCause_Type = CfprConditionCause
_CfprAaaSessionLRCause_Object = MibTableColumn
cfprAaaSessionLRCause = _CfprAaaSessionLRCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 5),
    _CfprAaaSessionLRCause_Type()
)
cfprAaaSessionLRCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRCause.setStatus("current")
_CfprAaaSessionLRChangeSet_Type = SnmpAdminString
_CfprAaaSessionLRChangeSet_Object = MibTableColumn
cfprAaaSessionLRChangeSet = _CfprAaaSessionLRChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 6),
    _CfprAaaSessionLRChangeSet_Type()
)
cfprAaaSessionLRChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRChangeSet.setStatus("current")
_CfprAaaSessionLRCode_Type = CfprConditionCode
_CfprAaaSessionLRCode_Object = MibTableColumn
cfprAaaSessionLRCode = _CfprAaaSessionLRCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 7),
    _CfprAaaSessionLRCode_Type()
)
cfprAaaSessionLRCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRCode.setStatus("current")
_CfprAaaSessionLRCreated_Type = DateAndTime
_CfprAaaSessionLRCreated_Object = MibTableColumn
cfprAaaSessionLRCreated = _CfprAaaSessionLRCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 8),
    _CfprAaaSessionLRCreated_Type()
)
cfprAaaSessionLRCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRCreated.setStatus("current")
_CfprAaaSessionLRDescr_Type = SnmpAdminString
_CfprAaaSessionLRDescr_Object = MibTableColumn
cfprAaaSessionLRDescr = _CfprAaaSessionLRDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 9),
    _CfprAaaSessionLRDescr_Type()
)
cfprAaaSessionLRDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRDescr.setStatus("current")
_CfprAaaSessionLRId_Type = Gauge32
_CfprAaaSessionLRId_Object = MibTableColumn
cfprAaaSessionLRId = _CfprAaaSessionLRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 10),
    _CfprAaaSessionLRId_Type()
)
cfprAaaSessionLRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRId.setStatus("current")
_CfprAaaSessionLRInd_Type = CfprConditionActionIndicator
_CfprAaaSessionLRInd_Object = MibTableColumn
cfprAaaSessionLRInd = _CfprAaaSessionLRInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 11),
    _CfprAaaSessionLRInd_Type()
)
cfprAaaSessionLRInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRInd.setStatus("current")
_CfprAaaSessionLRSessionId_Type = SnmpAdminString
_CfprAaaSessionLRSessionId_Object = MibTableColumn
cfprAaaSessionLRSessionId = _CfprAaaSessionLRSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 12),
    _CfprAaaSessionLRSessionId_Type()
)
cfprAaaSessionLRSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRSessionId.setStatus("current")
_CfprAaaSessionLRSeverity_Type = CfprConditionSeverity
_CfprAaaSessionLRSeverity_Object = MibTableColumn
cfprAaaSessionLRSeverity = _CfprAaaSessionLRSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 13),
    _CfprAaaSessionLRSeverity_Type()
)
cfprAaaSessionLRSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRSeverity.setStatus("current")
_CfprAaaSessionLRTrig_Type = Gauge32
_CfprAaaSessionLRTrig_Object = MibTableColumn
cfprAaaSessionLRTrig = _CfprAaaSessionLRTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 14),
    _CfprAaaSessionLRTrig_Type()
)
cfprAaaSessionLRTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRTrig.setStatus("current")
_CfprAaaSessionLRTxId_Type = Unsigned64
_CfprAaaSessionLRTxId_Object = MibTableColumn
cfprAaaSessionLRTxId = _CfprAaaSessionLRTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 15),
    _CfprAaaSessionLRTxId_Type()
)
cfprAaaSessionLRTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRTxId.setStatus("current")
_CfprAaaSessionLRUser_Type = SnmpAdminString
_CfprAaaSessionLRUser_Object = MibTableColumn
cfprAaaSessionLRUser = _CfprAaaSessionLRUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 42, 1, 16),
    _CfprAaaSessionLRUser_Type()
)
cfprAaaSessionLRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSessionLRUser.setStatus("current")
_CfprAaaShellLoginTable_Object = MibTable
cfprAaaShellLoginTable = _CfprAaaShellLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43)
)
if mibBuilder.loadTexts:
    cfprAaaShellLoginTable.setStatus("current")
_CfprAaaShellLoginEntry_Object = MibTableRow
cfprAaaShellLoginEntry = _CfprAaaShellLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1)
)
cfprAaaShellLoginEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaShellLoginInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaShellLoginEntry.setStatus("current")
_CfprAaaShellLoginInstanceId_Type = CfprManagedObjectId
_CfprAaaShellLoginInstanceId_Object = MibTableColumn
cfprAaaShellLoginInstanceId = _CfprAaaShellLoginInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 1),
    _CfprAaaShellLoginInstanceId_Type()
)
cfprAaaShellLoginInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaShellLoginInstanceId.setStatus("current")
_CfprAaaShellLoginDn_Type = CfprManagedObjectDn
_CfprAaaShellLoginDn_Object = MibTableColumn
cfprAaaShellLoginDn = _CfprAaaShellLoginDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 2),
    _CfprAaaShellLoginDn_Type()
)
cfprAaaShellLoginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginDn.setStatus("current")
_CfprAaaShellLoginRn_Type = SnmpAdminString
_CfprAaaShellLoginRn_Object = MibTableColumn
cfprAaaShellLoginRn = _CfprAaaShellLoginRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 3),
    _CfprAaaShellLoginRn_Type()
)
cfprAaaShellLoginRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginRn.setStatus("current")
_CfprAaaShellLoginDescr_Type = SnmpAdminString
_CfprAaaShellLoginDescr_Object = MibTableColumn
cfprAaaShellLoginDescr = _CfprAaaShellLoginDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 4),
    _CfprAaaShellLoginDescr_Type()
)
cfprAaaShellLoginDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginDescr.setStatus("current")
_CfprAaaShellLoginId_Type = SnmpAdminString
_CfprAaaShellLoginId_Object = MibTableColumn
cfprAaaShellLoginId = _CfprAaaShellLoginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 5),
    _CfprAaaShellLoginId_Type()
)
cfprAaaShellLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginId.setStatus("current")
_CfprAaaShellLoginIntId_Type = SnmpAdminString
_CfprAaaShellLoginIntId_Object = MibTableColumn
cfprAaaShellLoginIntId = _CfprAaaShellLoginIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 6),
    _CfprAaaShellLoginIntId_Type()
)
cfprAaaShellLoginIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginIntId.setStatus("current")
_CfprAaaShellLoginLocalHost_Type = SnmpAdminString
_CfprAaaShellLoginLocalHost_Object = MibTableColumn
cfprAaaShellLoginLocalHost = _CfprAaaShellLoginLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 7),
    _CfprAaaShellLoginLocalHost_Type()
)
cfprAaaShellLoginLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginLocalHost.setStatus("current")
_CfprAaaShellLoginName_Type = SnmpAdminString
_CfprAaaShellLoginName_Object = MibTableColumn
cfprAaaShellLoginName = _CfprAaaShellLoginName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 8),
    _CfprAaaShellLoginName_Type()
)
cfprAaaShellLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginName.setStatus("current")
_CfprAaaShellLoginPolicyLevel_Type = Gauge32
_CfprAaaShellLoginPolicyLevel_Object = MibTableColumn
cfprAaaShellLoginPolicyLevel = _CfprAaaShellLoginPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 9),
    _CfprAaaShellLoginPolicyLevel_Type()
)
cfprAaaShellLoginPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginPolicyLevel.setStatus("current")
_CfprAaaShellLoginPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaShellLoginPolicyOwner_Object = MibTableColumn
cfprAaaShellLoginPolicyOwner = _CfprAaaShellLoginPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 10),
    _CfprAaaShellLoginPolicyOwner_Type()
)
cfprAaaShellLoginPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginPolicyOwner.setStatus("current")
_CfprAaaShellLoginRemoteHost_Type = SnmpAdminString
_CfprAaaShellLoginRemoteHost_Object = MibTableColumn
cfprAaaShellLoginRemoteHost = _CfprAaaShellLoginRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 11),
    _CfprAaaShellLoginRemoteHost_Type()
)
cfprAaaShellLoginRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginRemoteHost.setStatus("current")
_CfprAaaShellLoginSession_Type = CfprAaaSession
_CfprAaaShellLoginSession_Object = MibTableColumn
cfprAaaShellLoginSession = _CfprAaaShellLoginSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 12),
    _CfprAaaShellLoginSession_Type()
)
cfprAaaShellLoginSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginSession.setStatus("current")
_CfprAaaShellLoginSwitchId_Type = CfprNetworkSwitchId
_CfprAaaShellLoginSwitchId_Object = MibTableColumn
cfprAaaShellLoginSwitchId = _CfprAaaShellLoginSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 43, 1, 13),
    _CfprAaaShellLoginSwitchId_Type()
)
cfprAaaShellLoginSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaShellLoginSwitchId.setStatus("current")
_CfprAaaSshAuthTable_Object = MibTable
cfprAaaSshAuthTable = _CfprAaaSshAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44)
)
if mibBuilder.loadTexts:
    cfprAaaSshAuthTable.setStatus("current")
_CfprAaaSshAuthEntry_Object = MibTableRow
cfprAaaSshAuthEntry = _CfprAaaSshAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1)
)
cfprAaaSshAuthEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSshAuthInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSshAuthEntry.setStatus("current")
_CfprAaaSshAuthInstanceId_Type = CfprManagedObjectId
_CfprAaaSshAuthInstanceId_Object = MibTableColumn
cfprAaaSshAuthInstanceId = _CfprAaaSshAuthInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1, 1),
    _CfprAaaSshAuthInstanceId_Type()
)
cfprAaaSshAuthInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSshAuthInstanceId.setStatus("current")
_CfprAaaSshAuthDn_Type = CfprManagedObjectDn
_CfprAaaSshAuthDn_Object = MibTableColumn
cfprAaaSshAuthDn = _CfprAaaSshAuthDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1, 2),
    _CfprAaaSshAuthDn_Type()
)
cfprAaaSshAuthDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSshAuthDn.setStatus("current")
_CfprAaaSshAuthRn_Type = SnmpAdminString
_CfprAaaSshAuthRn_Object = MibTableColumn
cfprAaaSshAuthRn = _CfprAaaSshAuthRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1, 3),
    _CfprAaaSshAuthRn_Type()
)
cfprAaaSshAuthRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSshAuthRn.setStatus("current")
_CfprAaaSshAuthData_Type = SnmpAdminString
_CfprAaaSshAuthData_Object = MibTableColumn
cfprAaaSshAuthData = _CfprAaaSshAuthData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1, 4),
    _CfprAaaSshAuthData_Type()
)
cfprAaaSshAuthData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSshAuthData.setStatus("current")
_CfprAaaSshAuthOldStrType_Type = CfprAaaSshStr
_CfprAaaSshAuthOldStrType_Object = MibTableColumn
cfprAaaSshAuthOldStrType = _CfprAaaSshAuthOldStrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1, 5),
    _CfprAaaSshAuthOldStrType_Type()
)
cfprAaaSshAuthOldStrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSshAuthOldStrType.setStatus("current")
_CfprAaaSshAuthStrType_Type = CfprAaaSshStr
_CfprAaaSshAuthStrType_Object = MibTableColumn
cfprAaaSshAuthStrType = _CfprAaaSshAuthStrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 44, 1, 6),
    _CfprAaaSshAuthStrType_Type()
)
cfprAaaSshAuthStrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSshAuthStrType.setStatus("current")
_CfprAaaTacacsPlusEpTable_Object = MibTable
cfprAaaTacacsPlusEpTable = _CfprAaaTacacsPlusEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45)
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpTable.setStatus("current")
_CfprAaaTacacsPlusEpEntry_Object = MibTableRow
cfprAaaTacacsPlusEpEntry = _CfprAaaTacacsPlusEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1)
)
cfprAaaTacacsPlusEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaTacacsPlusEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpEntry.setStatus("current")
_CfprAaaTacacsPlusEpInstanceId_Type = CfprManagedObjectId
_CfprAaaTacacsPlusEpInstanceId_Object = MibTableColumn
cfprAaaTacacsPlusEpInstanceId = _CfprAaaTacacsPlusEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 1),
    _CfprAaaTacacsPlusEpInstanceId_Type()
)
cfprAaaTacacsPlusEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpInstanceId.setStatus("current")
_CfprAaaTacacsPlusEpDn_Type = CfprManagedObjectDn
_CfprAaaTacacsPlusEpDn_Object = MibTableColumn
cfprAaaTacacsPlusEpDn = _CfprAaaTacacsPlusEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 2),
    _CfprAaaTacacsPlusEpDn_Type()
)
cfprAaaTacacsPlusEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpDn.setStatus("current")
_CfprAaaTacacsPlusEpRn_Type = SnmpAdminString
_CfprAaaTacacsPlusEpRn_Object = MibTableColumn
cfprAaaTacacsPlusEpRn = _CfprAaaTacacsPlusEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 3),
    _CfprAaaTacacsPlusEpRn_Type()
)
cfprAaaTacacsPlusEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpRn.setStatus("current")
_CfprAaaTacacsPlusEpDescr_Type = SnmpAdminString
_CfprAaaTacacsPlusEpDescr_Object = MibTableColumn
cfprAaaTacacsPlusEpDescr = _CfprAaaTacacsPlusEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 4),
    _CfprAaaTacacsPlusEpDescr_Type()
)
cfprAaaTacacsPlusEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpDescr.setStatus("current")
_CfprAaaTacacsPlusEpFsmDescr_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmDescr_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmDescr = _CfprAaaTacacsPlusEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 5),
    _CfprAaaTacacsPlusEpFsmDescr_Type()
)
cfprAaaTacacsPlusEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmDescr.setStatus("current")
_CfprAaaTacacsPlusEpFsmPrev_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmPrev_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmPrev = _CfprAaaTacacsPlusEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 6),
    _CfprAaaTacacsPlusEpFsmPrev_Type()
)
cfprAaaTacacsPlusEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmPrev.setStatus("current")
_CfprAaaTacacsPlusEpFsmProgr_Type = Gauge32
_CfprAaaTacacsPlusEpFsmProgr_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmProgr = _CfprAaaTacacsPlusEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 7),
    _CfprAaaTacacsPlusEpFsmProgr_Type()
)
cfprAaaTacacsPlusEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmProgr.setStatus("current")
_CfprAaaTacacsPlusEpFsmRmtInvErrCode_Type = Gauge32
_CfprAaaTacacsPlusEpFsmRmtInvErrCode_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRmtInvErrCode = _CfprAaaTacacsPlusEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 8),
    _CfprAaaTacacsPlusEpFsmRmtInvErrCode_Type()
)
cfprAaaTacacsPlusEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRmtInvErrCode.setStatus("current")
_CfprAaaTacacsPlusEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRmtInvErrDescr = _CfprAaaTacacsPlusEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 9),
    _CfprAaaTacacsPlusEpFsmRmtInvErrDescr_Type()
)
cfprAaaTacacsPlusEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRmtInvErrDescr.setStatus("current")
_CfprAaaTacacsPlusEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaTacacsPlusEpFsmRmtInvRslt_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRmtInvRslt = _CfprAaaTacacsPlusEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 10),
    _CfprAaaTacacsPlusEpFsmRmtInvRslt_Type()
)
cfprAaaTacacsPlusEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRmtInvRslt.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageDescr_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmStageDescr_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageDescr = _CfprAaaTacacsPlusEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 11),
    _CfprAaaTacacsPlusEpFsmStageDescr_Type()
)
cfprAaaTacacsPlusEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageDescr.setStatus("current")
_CfprAaaTacacsPlusEpFsmStamp_Type = DateAndTime
_CfprAaaTacacsPlusEpFsmStamp_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStamp = _CfprAaaTacacsPlusEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 12),
    _CfprAaaTacacsPlusEpFsmStamp_Type()
)
cfprAaaTacacsPlusEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStamp.setStatus("current")
_CfprAaaTacacsPlusEpFsmStatus_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmStatus_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStatus = _CfprAaaTacacsPlusEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 13),
    _CfprAaaTacacsPlusEpFsmStatus_Type()
)
cfprAaaTacacsPlusEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStatus.setStatus("current")
_CfprAaaTacacsPlusEpFsmTry_Type = Gauge32
_CfprAaaTacacsPlusEpFsmTry_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmTry = _CfprAaaTacacsPlusEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 14),
    _CfprAaaTacacsPlusEpFsmTry_Type()
)
cfprAaaTacacsPlusEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmTry.setStatus("current")
_CfprAaaTacacsPlusEpIntId_Type = SnmpAdminString
_CfprAaaTacacsPlusEpIntId_Object = MibTableColumn
cfprAaaTacacsPlusEpIntId = _CfprAaaTacacsPlusEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 15),
    _CfprAaaTacacsPlusEpIntId_Type()
)
cfprAaaTacacsPlusEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpIntId.setStatus("current")
_CfprAaaTacacsPlusEpName_Type = SnmpAdminString
_CfprAaaTacacsPlusEpName_Object = MibTableColumn
cfprAaaTacacsPlusEpName = _CfprAaaTacacsPlusEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 16),
    _CfprAaaTacacsPlusEpName_Type()
)
cfprAaaTacacsPlusEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpName.setStatus("current")
_CfprAaaTacacsPlusEpPolicyLevel_Type = Gauge32
_CfprAaaTacacsPlusEpPolicyLevel_Object = MibTableColumn
cfprAaaTacacsPlusEpPolicyLevel = _CfprAaaTacacsPlusEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 17),
    _CfprAaaTacacsPlusEpPolicyLevel_Type()
)
cfprAaaTacacsPlusEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpPolicyLevel.setStatus("current")
_CfprAaaTacacsPlusEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaTacacsPlusEpPolicyOwner_Object = MibTableColumn
cfprAaaTacacsPlusEpPolicyOwner = _CfprAaaTacacsPlusEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 18),
    _CfprAaaTacacsPlusEpPolicyOwner_Type()
)
cfprAaaTacacsPlusEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpPolicyOwner.setStatus("current")
_CfprAaaTacacsPlusEpRetries_Type = Gauge32
_CfprAaaTacacsPlusEpRetries_Object = MibTableColumn
cfprAaaTacacsPlusEpRetries = _CfprAaaTacacsPlusEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 19),
    _CfprAaaTacacsPlusEpRetries_Type()
)
cfprAaaTacacsPlusEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpRetries.setStatus("current")
_CfprAaaTacacsPlusEpTimeout_Type = Gauge32
_CfprAaaTacacsPlusEpTimeout_Object = MibTableColumn
cfprAaaTacacsPlusEpTimeout = _CfprAaaTacacsPlusEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 45, 1, 20),
    _CfprAaaTacacsPlusEpTimeout_Type()
)
cfprAaaTacacsPlusEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpTimeout.setStatus("current")
_CfprAaaTacacsPlusEpFsmTable_Object = MibTable
cfprAaaTacacsPlusEpFsmTable = _CfprAaaTacacsPlusEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46)
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmTable.setStatus("current")
_CfprAaaTacacsPlusEpFsmEntry_Object = MibTableRow
cfprAaaTacacsPlusEpFsmEntry = _CfprAaaTacacsPlusEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1)
)
cfprAaaTacacsPlusEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaTacacsPlusEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmEntry.setStatus("current")
_CfprAaaTacacsPlusEpFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaTacacsPlusEpFsmInstanceId_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmInstanceId = _CfprAaaTacacsPlusEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 1),
    _CfprAaaTacacsPlusEpFsmInstanceId_Type()
)
cfprAaaTacacsPlusEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmInstanceId.setStatus("current")
_CfprAaaTacacsPlusEpFsmDn_Type = CfprManagedObjectDn
_CfprAaaTacacsPlusEpFsmDn_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmDn = _CfprAaaTacacsPlusEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 2),
    _CfprAaaTacacsPlusEpFsmDn_Type()
)
cfprAaaTacacsPlusEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmDn.setStatus("current")
_CfprAaaTacacsPlusEpFsmRn_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmRn_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRn = _CfprAaaTacacsPlusEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 3),
    _CfprAaaTacacsPlusEpFsmRn_Type()
)
cfprAaaTacacsPlusEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRn.setStatus("current")
_CfprAaaTacacsPlusEpFsmCompletionTime_Type = DateAndTime
_CfprAaaTacacsPlusEpFsmCompletionTime_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmCompletionTime = _CfprAaaTacacsPlusEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 4),
    _CfprAaaTacacsPlusEpFsmCompletionTime_Type()
)
cfprAaaTacacsPlusEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmCompletionTime.setStatus("current")
_CfprAaaTacacsPlusEpFsmCurrentFsm_Type = CfprAaaTacacsPlusEpFsmCurrentFsm
_CfprAaaTacacsPlusEpFsmCurrentFsm_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmCurrentFsm = _CfprAaaTacacsPlusEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 5),
    _CfprAaaTacacsPlusEpFsmCurrentFsm_Type()
)
cfprAaaTacacsPlusEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmCurrentFsm.setStatus("current")
_CfprAaaTacacsPlusEpFsmDescrData_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmDescrData_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmDescrData = _CfprAaaTacacsPlusEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 6),
    _CfprAaaTacacsPlusEpFsmDescrData_Type()
)
cfprAaaTacacsPlusEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmDescrData.setStatus("current")
_CfprAaaTacacsPlusEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaTacacsPlusEpFsmFsmStatus_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmFsmStatus = _CfprAaaTacacsPlusEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 7),
    _CfprAaaTacacsPlusEpFsmFsmStatus_Type()
)
cfprAaaTacacsPlusEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmFsmStatus.setStatus("current")
_CfprAaaTacacsPlusEpFsmProgress_Type = Gauge32
_CfprAaaTacacsPlusEpFsmProgress_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmProgress = _CfprAaaTacacsPlusEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 8),
    _CfprAaaTacacsPlusEpFsmProgress_Type()
)
cfprAaaTacacsPlusEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmProgress.setStatus("current")
_CfprAaaTacacsPlusEpFsmRmtErrCode_Type = Gauge32
_CfprAaaTacacsPlusEpFsmRmtErrCode_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRmtErrCode = _CfprAaaTacacsPlusEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 9),
    _CfprAaaTacacsPlusEpFsmRmtErrCode_Type()
)
cfprAaaTacacsPlusEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRmtErrCode.setStatus("current")
_CfprAaaTacacsPlusEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmRmtErrDescr_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRmtErrDescr = _CfprAaaTacacsPlusEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 10),
    _CfprAaaTacacsPlusEpFsmRmtErrDescr_Type()
)
cfprAaaTacacsPlusEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRmtErrDescr.setStatus("current")
_CfprAaaTacacsPlusEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaTacacsPlusEpFsmRmtRslt_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmRmtRslt = _CfprAaaTacacsPlusEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 46, 1, 11),
    _CfprAaaTacacsPlusEpFsmRmtRslt_Type()
)
cfprAaaTacacsPlusEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmRmtRslt.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageTable_Object = MibTable
cfprAaaTacacsPlusEpFsmStageTable = _CfprAaaTacacsPlusEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47)
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageTable.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageEntry_Object = MibTableRow
cfprAaaTacacsPlusEpFsmStageEntry = _CfprAaaTacacsPlusEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1)
)
cfprAaaTacacsPlusEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaTacacsPlusEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageEntry.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaTacacsPlusEpFsmStageInstanceId_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageInstanceId = _CfprAaaTacacsPlusEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 1),
    _CfprAaaTacacsPlusEpFsmStageInstanceId_Type()
)
cfprAaaTacacsPlusEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageInstanceId.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaTacacsPlusEpFsmStageDn_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageDn = _CfprAaaTacacsPlusEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 2),
    _CfprAaaTacacsPlusEpFsmStageDn_Type()
)
cfprAaaTacacsPlusEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageDn.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageRn_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmStageRn_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageRn = _CfprAaaTacacsPlusEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 3),
    _CfprAaaTacacsPlusEpFsmStageRn_Type()
)
cfprAaaTacacsPlusEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageRn.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageDescrData_Type = SnmpAdminString
_CfprAaaTacacsPlusEpFsmStageDescrData_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageDescrData = _CfprAaaTacacsPlusEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 4),
    _CfprAaaTacacsPlusEpFsmStageDescrData_Type()
)
cfprAaaTacacsPlusEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageDescrData.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaTacacsPlusEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageLastUpdateTime = _CfprAaaTacacsPlusEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 5),
    _CfprAaaTacacsPlusEpFsmStageLastUpdateTime_Type()
)
cfprAaaTacacsPlusEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageLastUpdateTime.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageName_Type = CfprAaaTacacsPlusEpFsmStageName
_CfprAaaTacacsPlusEpFsmStageName_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageName = _CfprAaaTacacsPlusEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 6),
    _CfprAaaTacacsPlusEpFsmStageName_Type()
)
cfprAaaTacacsPlusEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageName.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageOrder_Type = Gauge32
_CfprAaaTacacsPlusEpFsmStageOrder_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageOrder = _CfprAaaTacacsPlusEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 7),
    _CfprAaaTacacsPlusEpFsmStageOrder_Type()
)
cfprAaaTacacsPlusEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageOrder.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageRetry_Type = Gauge32
_CfprAaaTacacsPlusEpFsmStageRetry_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageRetry = _CfprAaaTacacsPlusEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 8),
    _CfprAaaTacacsPlusEpFsmStageRetry_Type()
)
cfprAaaTacacsPlusEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageRetry.setStatus("current")
_CfprAaaTacacsPlusEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaTacacsPlusEpFsmStageStageStatus_Object = MibTableColumn
cfprAaaTacacsPlusEpFsmStageStageStatus = _CfprAaaTacacsPlusEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 47, 1, 9),
    _CfprAaaTacacsPlusEpFsmStageStageStatus_Type()
)
cfprAaaTacacsPlusEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusEpFsmStageStageStatus.setStatus("current")
_CfprAaaTacacsPlusProviderTable_Object = MibTable
cfprAaaTacacsPlusProviderTable = _CfprAaaTacacsPlusProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48)
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderTable.setStatus("current")
_CfprAaaTacacsPlusProviderEntry_Object = MibTableRow
cfprAaaTacacsPlusProviderEntry = _CfprAaaTacacsPlusProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1)
)
cfprAaaTacacsPlusProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaTacacsPlusProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderEntry.setStatus("current")
_CfprAaaTacacsPlusProviderInstanceId_Type = CfprManagedObjectId
_CfprAaaTacacsPlusProviderInstanceId_Object = MibTableColumn
cfprAaaTacacsPlusProviderInstanceId = _CfprAaaTacacsPlusProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 1),
    _CfprAaaTacacsPlusProviderInstanceId_Type()
)
cfprAaaTacacsPlusProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderInstanceId.setStatus("current")
_CfprAaaTacacsPlusProviderDn_Type = CfprManagedObjectDn
_CfprAaaTacacsPlusProviderDn_Object = MibTableColumn
cfprAaaTacacsPlusProviderDn = _CfprAaaTacacsPlusProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 2),
    _CfprAaaTacacsPlusProviderDn_Type()
)
cfprAaaTacacsPlusProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderDn.setStatus("current")
_CfprAaaTacacsPlusProviderRn_Type = SnmpAdminString
_CfprAaaTacacsPlusProviderRn_Object = MibTableColumn
cfprAaaTacacsPlusProviderRn = _CfprAaaTacacsPlusProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 3),
    _CfprAaaTacacsPlusProviderRn_Type()
)
cfprAaaTacacsPlusProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderRn.setStatus("current")
_CfprAaaTacacsPlusProviderDescr_Type = SnmpAdminString
_CfprAaaTacacsPlusProviderDescr_Object = MibTableColumn
cfprAaaTacacsPlusProviderDescr = _CfprAaaTacacsPlusProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 4),
    _CfprAaaTacacsPlusProviderDescr_Type()
)
cfprAaaTacacsPlusProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderDescr.setStatus("current")
_CfprAaaTacacsPlusProviderEncKey_Type = SnmpAdminString
_CfprAaaTacacsPlusProviderEncKey_Object = MibTableColumn
cfprAaaTacacsPlusProviderEncKey = _CfprAaaTacacsPlusProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 5),
    _CfprAaaTacacsPlusProviderEncKey_Type()
)
cfprAaaTacacsPlusProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderEncKey.setStatus("current")
_CfprAaaTacacsPlusProviderKey_Type = SnmpAdminString
_CfprAaaTacacsPlusProviderKey_Object = MibTableColumn
cfprAaaTacacsPlusProviderKey = _CfprAaaTacacsPlusProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 6),
    _CfprAaaTacacsPlusProviderKey_Type()
)
cfprAaaTacacsPlusProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderKey.setStatus("current")
_CfprAaaTacacsPlusProviderKeySet_Type = TruthValue
_CfprAaaTacacsPlusProviderKeySet_Object = MibTableColumn
cfprAaaTacacsPlusProviderKeySet = _CfprAaaTacacsPlusProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 7),
    _CfprAaaTacacsPlusProviderKeySet_Type()
)
cfprAaaTacacsPlusProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderKeySet.setStatus("current")
_CfprAaaTacacsPlusProviderName_Type = SnmpAdminString
_CfprAaaTacacsPlusProviderName_Object = MibTableColumn
cfprAaaTacacsPlusProviderName = _CfprAaaTacacsPlusProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 8),
    _CfprAaaTacacsPlusProviderName_Type()
)
cfprAaaTacacsPlusProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderName.setStatus("current")
_CfprAaaTacacsPlusProviderOrder_Type = Gauge32
_CfprAaaTacacsPlusProviderOrder_Object = MibTableColumn
cfprAaaTacacsPlusProviderOrder = _CfprAaaTacacsPlusProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 9),
    _CfprAaaTacacsPlusProviderOrder_Type()
)
cfprAaaTacacsPlusProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderOrder.setStatus("current")
_CfprAaaTacacsPlusProviderPort_Type = Gauge32
_CfprAaaTacacsPlusProviderPort_Object = MibTableColumn
cfprAaaTacacsPlusProviderPort = _CfprAaaTacacsPlusProviderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 10),
    _CfprAaaTacacsPlusProviderPort_Type()
)
cfprAaaTacacsPlusProviderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderPort.setStatus("current")
_CfprAaaTacacsPlusProviderRetries_Type = Gauge32
_CfprAaaTacacsPlusProviderRetries_Object = MibTableColumn
cfprAaaTacacsPlusProviderRetries = _CfprAaaTacacsPlusProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 11),
    _CfprAaaTacacsPlusProviderRetries_Type()
)
cfprAaaTacacsPlusProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderRetries.setStatus("current")
_CfprAaaTacacsPlusProviderTimeout_Type = Gauge32
_CfprAaaTacacsPlusProviderTimeout_Object = MibTableColumn
cfprAaaTacacsPlusProviderTimeout = _CfprAaaTacacsPlusProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 48, 1, 12),
    _CfprAaaTacacsPlusProviderTimeout_Type()
)
cfprAaaTacacsPlusProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaTacacsPlusProviderTimeout.setStatus("current")
_CfprAaaUserTable_Object = MibTable
cfprAaaUserTable = _CfprAaaUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49)
)
if mibBuilder.loadTexts:
    cfprAaaUserTable.setStatus("current")
_CfprAaaUserEntry_Object = MibTableRow
cfprAaaUserEntry = _CfprAaaUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1)
)
cfprAaaUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserEntry.setStatus("current")
_CfprAaaUserInstanceId_Type = CfprManagedObjectId
_CfprAaaUserInstanceId_Object = MibTableColumn
cfprAaaUserInstanceId = _CfprAaaUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 1),
    _CfprAaaUserInstanceId_Type()
)
cfprAaaUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserInstanceId.setStatus("current")
_CfprAaaUserDn_Type = CfprManagedObjectDn
_CfprAaaUserDn_Object = MibTableColumn
cfprAaaUserDn = _CfprAaaUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 2),
    _CfprAaaUserDn_Type()
)
cfprAaaUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDn.setStatus("current")
_CfprAaaUserRn_Type = SnmpAdminString
_CfprAaaUserRn_Object = MibTableColumn
cfprAaaUserRn = _CfprAaaUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 3),
    _CfprAaaUserRn_Type()
)
cfprAaaUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRn.setStatus("current")
_CfprAaaUserAccountStatus_Type = CfprAaaAccountStatus
_CfprAaaUserAccountStatus_Object = MibTableColumn
cfprAaaUserAccountStatus = _CfprAaaUserAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 4),
    _CfprAaaUserAccountStatus_Type()
)
cfprAaaUserAccountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserAccountStatus.setStatus("current")
_CfprAaaUserClearPwdHistory_Type = CfprAaaClear
_CfprAaaUserClearPwdHistory_Object = MibTableColumn
cfprAaaUserClearPwdHistory = _CfprAaaUserClearPwdHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 5),
    _CfprAaaUserClearPwdHistory_Type()
)
cfprAaaUserClearPwdHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserClearPwdHistory.setStatus("current")
_CfprAaaUserConfigState_Type = CfprAaaConfigState
_CfprAaaUserConfigState_Object = MibTableColumn
cfprAaaUserConfigState = _CfprAaaUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 6),
    _CfprAaaUserConfigState_Type()
)
cfprAaaUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserConfigState.setStatus("current")
_CfprAaaUserConfigStatusMessage_Type = SnmpAdminString
_CfprAaaUserConfigStatusMessage_Object = MibTableColumn
cfprAaaUserConfigStatusMessage = _CfprAaaUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 7),
    _CfprAaaUserConfigStatusMessage_Type()
)
cfprAaaUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserConfigStatusMessage.setStatus("current")
_CfprAaaUserDescr_Type = SnmpAdminString
_CfprAaaUserDescr_Object = MibTableColumn
cfprAaaUserDescr = _CfprAaaUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 8),
    _CfprAaaUserDescr_Type()
)
cfprAaaUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDescr.setStatus("current")
_CfprAaaUserEmail_Type = SnmpAdminString
_CfprAaaUserEmail_Object = MibTableColumn
cfprAaaUserEmail = _CfprAaaUserEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 9),
    _CfprAaaUserEmail_Type()
)
cfprAaaUserEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEmail.setStatus("current")
_CfprAaaUserEncPwd_Type = SnmpAdminString
_CfprAaaUserEncPwd_Object = MibTableColumn
cfprAaaUserEncPwd = _CfprAaaUserEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 10),
    _CfprAaaUserEncPwd_Type()
)
cfprAaaUserEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEncPwd.setStatus("current")
_CfprAaaUserEncPwdSet_Type = TruthValue
_CfprAaaUserEncPwdSet_Object = MibTableColumn
cfprAaaUserEncPwdSet = _CfprAaaUserEncPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 11),
    _CfprAaaUserEncPwdSet_Type()
)
cfprAaaUserEncPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEncPwdSet.setStatus("current")
_CfprAaaUserExpiration_Type = DateAndTime
_CfprAaaUserExpiration_Object = MibTableColumn
cfprAaaUserExpiration = _CfprAaaUserExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 12),
    _CfprAaaUserExpiration_Type()
)
cfprAaaUserExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserExpiration.setStatus("current")
_CfprAaaUserExpires_Type = TruthValue
_CfprAaaUserExpires_Object = MibTableColumn
cfprAaaUserExpires = _CfprAaaUserExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 13),
    _CfprAaaUserExpires_Type()
)
cfprAaaUserExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserExpires.setStatus("current")
_CfprAaaUserFirstName_Type = SnmpAdminString
_CfprAaaUserFirstName_Object = MibTableColumn
cfprAaaUserFirstName = _CfprAaaUserFirstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 14),
    _CfprAaaUserFirstName_Type()
)
cfprAaaUserFirstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserFirstName.setStatus("current")
_CfprAaaUserLastName_Type = SnmpAdminString
_CfprAaaUserLastName_Object = MibTableColumn
cfprAaaUserLastName = _CfprAaaUserLastName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 15),
    _CfprAaaUserLastName_Type()
)
cfprAaaUserLastName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLastName.setStatus("current")
_CfprAaaUserName_Type = SnmpAdminString
_CfprAaaUserName_Object = MibTableColumn
cfprAaaUserName = _CfprAaaUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 16),
    _CfprAaaUserName_Type()
)
cfprAaaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserName.setStatus("current")
_CfprAaaUserPhone_Type = SnmpAdminString
_CfprAaaUserPhone_Object = MibTableColumn
cfprAaaUserPhone = _CfprAaaUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 17),
    _CfprAaaUserPhone_Type()
)
cfprAaaUserPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserPhone.setStatus("current")
_CfprAaaUserPriv_Type = CfprAaaAccess
_CfprAaaUserPriv_Object = MibTableColumn
cfprAaaUserPriv = _CfprAaaUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 18),
    _CfprAaaUserPriv_Type()
)
cfprAaaUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserPriv.setStatus("current")
_CfprAaaUserPwd_Type = SnmpAdminString
_CfprAaaUserPwd_Object = MibTableColumn
cfprAaaUserPwd = _CfprAaaUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 19),
    _CfprAaaUserPwd_Type()
)
cfprAaaUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserPwd.setStatus("current")
_CfprAaaUserPwdSet_Type = TruthValue
_CfprAaaUserPwdSet_Object = MibTableColumn
cfprAaaUserPwdSet = _CfprAaaUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 21),
    _CfprAaaUserPwdSet_Type()
)
cfprAaaUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserPwdSet.setStatus("current")
_CfprAaaUserClearLockStatus_Type = CfprAaaClear
_CfprAaaUserClearLockStatus_Object = MibTableColumn
cfprAaaUserClearLockStatus = _CfprAaaUserClearLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 22),
    _CfprAaaUserClearLockStatus_Type()
)
cfprAaaUserClearLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserClearLockStatus.setStatus("current")
_CfprAaaUserPwdExpDate_Type = DateAndTime
_CfprAaaUserPwdExpDate_Object = MibTableColumn
cfprAaaUserPwdExpDate = _CfprAaaUserPwdExpDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 23),
    _CfprAaaUserPwdExpDate_Type()
)
cfprAaaUserPwdExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserPwdExpDate.setStatus("current")
_CfprAaaUserPwdReset_Type = TruthValue
_CfprAaaUserPwdReset_Object = MibTableColumn
cfprAaaUserPwdReset = _CfprAaaUserPwdReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 49, 1, 24),
    _CfprAaaUserPwdReset_Type()
)
cfprAaaUserPwdReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserPwdReset.setStatus("current")
_CfprAaaUserDataTable_Object = MibTable
cfprAaaUserDataTable = _CfprAaaUserDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50)
)
if mibBuilder.loadTexts:
    cfprAaaUserDataTable.setStatus("current")
_CfprAaaUserDataEntry_Object = MibTableRow
cfprAaaUserDataEntry = _CfprAaaUserDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1)
)
cfprAaaUserDataEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserDataInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserDataEntry.setStatus("current")
_CfprAaaUserDataInstanceId_Type = CfprManagedObjectId
_CfprAaaUserDataInstanceId_Object = MibTableColumn
cfprAaaUserDataInstanceId = _CfprAaaUserDataInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 1),
    _CfprAaaUserDataInstanceId_Type()
)
cfprAaaUserDataInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserDataInstanceId.setStatus("current")
_CfprAaaUserDataDn_Type = CfprManagedObjectDn
_CfprAaaUserDataDn_Object = MibTableColumn
cfprAaaUserDataDn = _CfprAaaUserDataDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 2),
    _CfprAaaUserDataDn_Type()
)
cfprAaaUserDataDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataDn.setStatus("current")
_CfprAaaUserDataRn_Type = SnmpAdminString
_CfprAaaUserDataRn_Object = MibTableColumn
cfprAaaUserDataRn = _CfprAaaUserDataRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 3),
    _CfprAaaUserDataRn_Type()
)
cfprAaaUserDataRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataRn.setStatus("current")
_CfprAaaUserDataDescr_Type = SnmpAdminString
_CfprAaaUserDataDescr_Object = MibTableColumn
cfprAaaUserDataDescr = _CfprAaaUserDataDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 4),
    _CfprAaaUserDataDescr_Type()
)
cfprAaaUserDataDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataDescr.setStatus("current")
_CfprAaaUserDataIntId_Type = SnmpAdminString
_CfprAaaUserDataIntId_Object = MibTableColumn
cfprAaaUserDataIntId = _CfprAaaUserDataIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 5),
    _CfprAaaUserDataIntId_Type()
)
cfprAaaUserDataIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataIntId.setStatus("current")
_CfprAaaUserDataName_Type = SnmpAdminString
_CfprAaaUserDataName_Object = MibTableColumn
cfprAaaUserDataName = _CfprAaaUserDataName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 6),
    _CfprAaaUserDataName_Type()
)
cfprAaaUserDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataName.setStatus("current")
_CfprAaaUserDataPolicyLevel_Type = Gauge32
_CfprAaaUserDataPolicyLevel_Object = MibTableColumn
cfprAaaUserDataPolicyLevel = _CfprAaaUserDataPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 7),
    _CfprAaaUserDataPolicyLevel_Type()
)
cfprAaaUserDataPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataPolicyLevel.setStatus("current")
_CfprAaaUserDataPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaUserDataPolicyOwner_Object = MibTableColumn
cfprAaaUserDataPolicyOwner = _CfprAaaUserDataPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 8),
    _CfprAaaUserDataPolicyOwner_Type()
)
cfprAaaUserDataPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataPolicyOwner.setStatus("current")
_CfprAaaUserDataPwdChangeCount_Type = Gauge32
_CfprAaaUserDataPwdChangeCount_Object = MibTableColumn
cfprAaaUserDataPwdChangeCount = _CfprAaaUserDataPwdChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 9),
    _CfprAaaUserDataPwdChangeCount_Type()
)
cfprAaaUserDataPwdChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataPwdChangeCount.setStatus("current")
_CfprAaaUserDataPwdChangeIntervalBegin_Type = DateAndTime
_CfprAaaUserDataPwdChangeIntervalBegin_Object = MibTableColumn
cfprAaaUserDataPwdChangeIntervalBegin = _CfprAaaUserDataPwdChangeIntervalBegin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 10),
    _CfprAaaUserDataPwdChangeIntervalBegin_Type()
)
cfprAaaUserDataPwdChangeIntervalBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataPwdChangeIntervalBegin.setStatus("current")
_CfprAaaUserDataPwdChangedDate_Type = DateAndTime
_CfprAaaUserDataPwdChangedDate_Object = MibTableColumn
cfprAaaUserDataPwdChangedDate = _CfprAaaUserDataPwdChangedDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 11),
    _CfprAaaUserDataPwdChangedDate_Type()
)
cfprAaaUserDataPwdChangedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataPwdChangedDate.setStatus("current")
_CfprAaaUserDataPwdHistory_Type = SnmpAdminString
_CfprAaaUserDataPwdHistory_Object = MibTableColumn
cfprAaaUserDataPwdHistory = _CfprAaaUserDataPwdHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 50, 1, 12),
    _CfprAaaUserDataPwdHistory_Type()
)
cfprAaaUserDataPwdHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserDataPwdHistory.setStatus("current")
_CfprAaaUserEpTable_Object = MibTable
cfprAaaUserEpTable = _CfprAaaUserEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51)
)
if mibBuilder.loadTexts:
    cfprAaaUserEpTable.setStatus("current")
_CfprAaaUserEpEntry_Object = MibTableRow
cfprAaaUserEpEntry = _CfprAaaUserEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1)
)
cfprAaaUserEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserEpEntry.setStatus("current")
_CfprAaaUserEpInstanceId_Type = CfprManagedObjectId
_CfprAaaUserEpInstanceId_Object = MibTableColumn
cfprAaaUserEpInstanceId = _CfprAaaUserEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 1),
    _CfprAaaUserEpInstanceId_Type()
)
cfprAaaUserEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserEpInstanceId.setStatus("current")
_CfprAaaUserEpDn_Type = CfprManagedObjectDn
_CfprAaaUserEpDn_Object = MibTableColumn
cfprAaaUserEpDn = _CfprAaaUserEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 2),
    _CfprAaaUserEpDn_Type()
)
cfprAaaUserEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpDn.setStatus("current")
_CfprAaaUserEpRn_Type = SnmpAdminString
_CfprAaaUserEpRn_Object = MibTableColumn
cfprAaaUserEpRn = _CfprAaaUserEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 3),
    _CfprAaaUserEpRn_Type()
)
cfprAaaUserEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpRn.setStatus("current")
_CfprAaaUserEpDescr_Type = SnmpAdminString
_CfprAaaUserEpDescr_Object = MibTableColumn
cfprAaaUserEpDescr = _CfprAaaUserEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 4),
    _CfprAaaUserEpDescr_Type()
)
cfprAaaUserEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpDescr.setStatus("current")
_CfprAaaUserEpFsmDescr_Type = SnmpAdminString
_CfprAaaUserEpFsmDescr_Object = MibTableColumn
cfprAaaUserEpFsmDescr = _CfprAaaUserEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 5),
    _CfprAaaUserEpFsmDescr_Type()
)
cfprAaaUserEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmDescr.setStatus("current")
_CfprAaaUserEpFsmPrev_Type = SnmpAdminString
_CfprAaaUserEpFsmPrev_Object = MibTableColumn
cfprAaaUserEpFsmPrev = _CfprAaaUserEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 6),
    _CfprAaaUserEpFsmPrev_Type()
)
cfprAaaUserEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmPrev.setStatus("current")
_CfprAaaUserEpFsmProgr_Type = Gauge32
_CfprAaaUserEpFsmProgr_Object = MibTableColumn
cfprAaaUserEpFsmProgr = _CfprAaaUserEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 7),
    _CfprAaaUserEpFsmProgr_Type()
)
cfprAaaUserEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmProgr.setStatus("current")
_CfprAaaUserEpFsmRmtInvErrCode_Type = Gauge32
_CfprAaaUserEpFsmRmtInvErrCode_Object = MibTableColumn
cfprAaaUserEpFsmRmtInvErrCode = _CfprAaaUserEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 8),
    _CfprAaaUserEpFsmRmtInvErrCode_Type()
)
cfprAaaUserEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRmtInvErrCode.setStatus("current")
_CfprAaaUserEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprAaaUserEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprAaaUserEpFsmRmtInvErrDescr = _CfprAaaUserEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 9),
    _CfprAaaUserEpFsmRmtInvErrDescr_Type()
)
cfprAaaUserEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRmtInvErrDescr.setStatus("current")
_CfprAaaUserEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaUserEpFsmRmtInvRslt_Object = MibTableColumn
cfprAaaUserEpFsmRmtInvRslt = _CfprAaaUserEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 10),
    _CfprAaaUserEpFsmRmtInvRslt_Type()
)
cfprAaaUserEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRmtInvRslt.setStatus("current")
_CfprAaaUserEpFsmStageDescr_Type = SnmpAdminString
_CfprAaaUserEpFsmStageDescr_Object = MibTableColumn
cfprAaaUserEpFsmStageDescr = _CfprAaaUserEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 11),
    _CfprAaaUserEpFsmStageDescr_Type()
)
cfprAaaUserEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageDescr.setStatus("current")
_CfprAaaUserEpFsmStamp_Type = DateAndTime
_CfprAaaUserEpFsmStamp_Object = MibTableColumn
cfprAaaUserEpFsmStamp = _CfprAaaUserEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 12),
    _CfprAaaUserEpFsmStamp_Type()
)
cfprAaaUserEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStamp.setStatus("current")
_CfprAaaUserEpFsmStatus_Type = SnmpAdminString
_CfprAaaUserEpFsmStatus_Object = MibTableColumn
cfprAaaUserEpFsmStatus = _CfprAaaUserEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 13),
    _CfprAaaUserEpFsmStatus_Type()
)
cfprAaaUserEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStatus.setStatus("current")
_CfprAaaUserEpFsmTry_Type = Gauge32
_CfprAaaUserEpFsmTry_Object = MibTableColumn
cfprAaaUserEpFsmTry = _CfprAaaUserEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 14),
    _CfprAaaUserEpFsmTry_Type()
)
cfprAaaUserEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTry.setStatus("current")
_CfprAaaUserEpIntId_Type = SnmpAdminString
_CfprAaaUserEpIntId_Object = MibTableColumn
cfprAaaUserEpIntId = _CfprAaaUserEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 15),
    _CfprAaaUserEpIntId_Type()
)
cfprAaaUserEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpIntId.setStatus("current")
_CfprAaaUserEpName_Type = SnmpAdminString
_CfprAaaUserEpName_Object = MibTableColumn
cfprAaaUserEpName = _CfprAaaUserEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 16),
    _CfprAaaUserEpName_Type()
)
cfprAaaUserEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpName.setStatus("current")
_CfprAaaUserEpPolicyLevel_Type = Gauge32
_CfprAaaUserEpPolicyLevel_Object = MibTableColumn
cfprAaaUserEpPolicyLevel = _CfprAaaUserEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 17),
    _CfprAaaUserEpPolicyLevel_Type()
)
cfprAaaUserEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpPolicyLevel.setStatus("current")
_CfprAaaUserEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaUserEpPolicyOwner_Object = MibTableColumn
cfprAaaUserEpPolicyOwner = _CfprAaaUserEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 18),
    _CfprAaaUserEpPolicyOwner_Type()
)
cfprAaaUserEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpPolicyOwner.setStatus("current")
_CfprAaaUserEpPwdStrengthCheck_Type = TruthValue
_CfprAaaUserEpPwdStrengthCheck_Object = MibTableColumn
cfprAaaUserEpPwdStrengthCheck = _CfprAaaUserEpPwdStrengthCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 19),
    _CfprAaaUserEpPwdStrengthCheck_Type()
)
cfprAaaUserEpPwdStrengthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpPwdStrengthCheck.setStatus("current")
_CfprAaaUserEpMaxLoginAttempts_Type = Gauge32
_CfprAaaUserEpMaxLoginAttempts_Object = MibTableColumn
cfprAaaUserEpMaxLoginAttempts = _CfprAaaUserEpMaxLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 20),
    _CfprAaaUserEpMaxLoginAttempts_Type()
)
cfprAaaUserEpMaxLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpMaxLoginAttempts.setStatus("current")
_CfprAaaUserEpMinPwdLength_Type = Gauge32
_CfprAaaUserEpMinPwdLength_Object = MibTableColumn
cfprAaaUserEpMinPwdLength = _CfprAaaUserEpMinPwdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 21),
    _CfprAaaUserEpMinPwdLength_Type()
)
cfprAaaUserEpMinPwdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpMinPwdLength.setStatus("current")
_CfprAaaUserEpUserAccountUnlockTime_Type = Gauge32
_CfprAaaUserEpUserAccountUnlockTime_Object = MibTableColumn
cfprAaaUserEpUserAccountUnlockTime = _CfprAaaUserEpUserAccountUnlockTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 22),
    _CfprAaaUserEpUserAccountUnlockTime_Type()
)
cfprAaaUserEpUserAccountUnlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpUserAccountUnlockTime.setStatus("current")
_CfprAaaUserEpIsPasswordEncryptionKeySet_Type = TruthValue
_CfprAaaUserEpIsPasswordEncryptionKeySet_Object = MibTableColumn
cfprAaaUserEpIsPasswordEncryptionKeySet = _CfprAaaUserEpIsPasswordEncryptionKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 23),
    _CfprAaaUserEpIsPasswordEncryptionKeySet_Type()
)
cfprAaaUserEpIsPasswordEncryptionKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpIsPasswordEncryptionKeySet.setStatus("current")
_CfprAaaUserEpPasswordEncryptionKey_Type = SnmpAdminString
_CfprAaaUserEpPasswordEncryptionKey_Object = MibTableColumn
cfprAaaUserEpPasswordEncryptionKey = _CfprAaaUserEpPasswordEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 51, 1, 24),
    _CfprAaaUserEpPasswordEncryptionKey_Type()
)
cfprAaaUserEpPasswordEncryptionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpPasswordEncryptionKey.setStatus("current")
_CfprAaaUserEpFsmTable_Object = MibTable
cfprAaaUserEpFsmTable = _CfprAaaUserEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52)
)
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTable.setStatus("current")
_CfprAaaUserEpFsmEntry_Object = MibTableRow
cfprAaaUserEpFsmEntry = _CfprAaaUserEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1)
)
cfprAaaUserEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmEntry.setStatus("current")
_CfprAaaUserEpFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaUserEpFsmInstanceId_Object = MibTableColumn
cfprAaaUserEpFsmInstanceId = _CfprAaaUserEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 1),
    _CfprAaaUserEpFsmInstanceId_Type()
)
cfprAaaUserEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmInstanceId.setStatus("current")
_CfprAaaUserEpFsmDn_Type = CfprManagedObjectDn
_CfprAaaUserEpFsmDn_Object = MibTableColumn
cfprAaaUserEpFsmDn = _CfprAaaUserEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 2),
    _CfprAaaUserEpFsmDn_Type()
)
cfprAaaUserEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmDn.setStatus("current")
_CfprAaaUserEpFsmRn_Type = SnmpAdminString
_CfprAaaUserEpFsmRn_Object = MibTableColumn
cfprAaaUserEpFsmRn = _CfprAaaUserEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 3),
    _CfprAaaUserEpFsmRn_Type()
)
cfprAaaUserEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRn.setStatus("current")
_CfprAaaUserEpFsmCompletionTime_Type = DateAndTime
_CfprAaaUserEpFsmCompletionTime_Object = MibTableColumn
cfprAaaUserEpFsmCompletionTime = _CfprAaaUserEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 4),
    _CfprAaaUserEpFsmCompletionTime_Type()
)
cfprAaaUserEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmCompletionTime.setStatus("current")
_CfprAaaUserEpFsmCurrentFsm_Type = CfprAaaUserEpFsmCurrentFsm
_CfprAaaUserEpFsmCurrentFsm_Object = MibTableColumn
cfprAaaUserEpFsmCurrentFsm = _CfprAaaUserEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 5),
    _CfprAaaUserEpFsmCurrentFsm_Type()
)
cfprAaaUserEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmCurrentFsm.setStatus("current")
_CfprAaaUserEpFsmDescrData_Type = SnmpAdminString
_CfprAaaUserEpFsmDescrData_Object = MibTableColumn
cfprAaaUserEpFsmDescrData = _CfprAaaUserEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 6),
    _CfprAaaUserEpFsmDescrData_Type()
)
cfprAaaUserEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmDescrData.setStatus("current")
_CfprAaaUserEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaUserEpFsmFsmStatus_Object = MibTableColumn
cfprAaaUserEpFsmFsmStatus = _CfprAaaUserEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 7),
    _CfprAaaUserEpFsmFsmStatus_Type()
)
cfprAaaUserEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmFsmStatus.setStatus("current")
_CfprAaaUserEpFsmProgress_Type = Gauge32
_CfprAaaUserEpFsmProgress_Object = MibTableColumn
cfprAaaUserEpFsmProgress = _CfprAaaUserEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 8),
    _CfprAaaUserEpFsmProgress_Type()
)
cfprAaaUserEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmProgress.setStatus("current")
_CfprAaaUserEpFsmRmtErrCode_Type = Gauge32
_CfprAaaUserEpFsmRmtErrCode_Object = MibTableColumn
cfprAaaUserEpFsmRmtErrCode = _CfprAaaUserEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 9),
    _CfprAaaUserEpFsmRmtErrCode_Type()
)
cfprAaaUserEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRmtErrCode.setStatus("current")
_CfprAaaUserEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaUserEpFsmRmtErrDescr_Object = MibTableColumn
cfprAaaUserEpFsmRmtErrDescr = _CfprAaaUserEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 10),
    _CfprAaaUserEpFsmRmtErrDescr_Type()
)
cfprAaaUserEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRmtErrDescr.setStatus("current")
_CfprAaaUserEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaUserEpFsmRmtRslt_Object = MibTableColumn
cfprAaaUserEpFsmRmtRslt = _CfprAaaUserEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 52, 1, 11),
    _CfprAaaUserEpFsmRmtRslt_Type()
)
cfprAaaUserEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmRmtRslt.setStatus("current")
_CfprAaaUserEpFsmStageTable_Object = MibTable
cfprAaaUserEpFsmStageTable = _CfprAaaUserEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53)
)
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageTable.setStatus("current")
_CfprAaaUserEpFsmStageEntry_Object = MibTableRow
cfprAaaUserEpFsmStageEntry = _CfprAaaUserEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1)
)
cfprAaaUserEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageEntry.setStatus("current")
_CfprAaaUserEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaUserEpFsmStageInstanceId_Object = MibTableColumn
cfprAaaUserEpFsmStageInstanceId = _CfprAaaUserEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 1),
    _CfprAaaUserEpFsmStageInstanceId_Type()
)
cfprAaaUserEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageInstanceId.setStatus("current")
_CfprAaaUserEpFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaUserEpFsmStageDn_Object = MibTableColumn
cfprAaaUserEpFsmStageDn = _CfprAaaUserEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 2),
    _CfprAaaUserEpFsmStageDn_Type()
)
cfprAaaUserEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageDn.setStatus("current")
_CfprAaaUserEpFsmStageRn_Type = SnmpAdminString
_CfprAaaUserEpFsmStageRn_Object = MibTableColumn
cfprAaaUserEpFsmStageRn = _CfprAaaUserEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 3),
    _CfprAaaUserEpFsmStageRn_Type()
)
cfprAaaUserEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageRn.setStatus("current")
_CfprAaaUserEpFsmStageDescrData_Type = SnmpAdminString
_CfprAaaUserEpFsmStageDescrData_Object = MibTableColumn
cfprAaaUserEpFsmStageDescrData = _CfprAaaUserEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 4),
    _CfprAaaUserEpFsmStageDescrData_Type()
)
cfprAaaUserEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageDescrData.setStatus("current")
_CfprAaaUserEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaUserEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaUserEpFsmStageLastUpdateTime = _CfprAaaUserEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 5),
    _CfprAaaUserEpFsmStageLastUpdateTime_Type()
)
cfprAaaUserEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageLastUpdateTime.setStatus("current")
_CfprAaaUserEpFsmStageName_Type = CfprAaaUserEpFsmStageName
_CfprAaaUserEpFsmStageName_Object = MibTableColumn
cfprAaaUserEpFsmStageName = _CfprAaaUserEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 6),
    _CfprAaaUserEpFsmStageName_Type()
)
cfprAaaUserEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageName.setStatus("current")
_CfprAaaUserEpFsmStageOrder_Type = Gauge32
_CfprAaaUserEpFsmStageOrder_Object = MibTableColumn
cfprAaaUserEpFsmStageOrder = _CfprAaaUserEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 7),
    _CfprAaaUserEpFsmStageOrder_Type()
)
cfprAaaUserEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageOrder.setStatus("current")
_CfprAaaUserEpFsmStageRetry_Type = Gauge32
_CfprAaaUserEpFsmStageRetry_Object = MibTableColumn
cfprAaaUserEpFsmStageRetry = _CfprAaaUserEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 8),
    _CfprAaaUserEpFsmStageRetry_Type()
)
cfprAaaUserEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageRetry.setStatus("current")
_CfprAaaUserEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaUserEpFsmStageStageStatus_Object = MibTableColumn
cfprAaaUserEpFsmStageStageStatus = _CfprAaaUserEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 53, 1, 9),
    _CfprAaaUserEpFsmStageStageStatus_Type()
)
cfprAaaUserEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmStageStageStatus.setStatus("current")
_CfprAaaUserEpFsmTaskTable_Object = MibTable
cfprAaaUserEpFsmTaskTable = _CfprAaaUserEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54)
)
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskTable.setStatus("current")
_CfprAaaUserEpFsmTaskEntry_Object = MibTableRow
cfprAaaUserEpFsmTaskEntry = _CfprAaaUserEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1)
)
cfprAaaUserEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskEntry.setStatus("current")
_CfprAaaUserEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprAaaUserEpFsmTaskInstanceId_Object = MibTableColumn
cfprAaaUserEpFsmTaskInstanceId = _CfprAaaUserEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 1),
    _CfprAaaUserEpFsmTaskInstanceId_Type()
)
cfprAaaUserEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskInstanceId.setStatus("current")
_CfprAaaUserEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprAaaUserEpFsmTaskDn_Object = MibTableColumn
cfprAaaUserEpFsmTaskDn = _CfprAaaUserEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 2),
    _CfprAaaUserEpFsmTaskDn_Type()
)
cfprAaaUserEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskDn.setStatus("current")
_CfprAaaUserEpFsmTaskRn_Type = SnmpAdminString
_CfprAaaUserEpFsmTaskRn_Object = MibTableColumn
cfprAaaUserEpFsmTaskRn = _CfprAaaUserEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 3),
    _CfprAaaUserEpFsmTaskRn_Type()
)
cfprAaaUserEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskRn.setStatus("current")
_CfprAaaUserEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprAaaUserEpFsmTaskCompletion_Object = MibTableColumn
cfprAaaUserEpFsmTaskCompletion = _CfprAaaUserEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 4),
    _CfprAaaUserEpFsmTaskCompletion_Type()
)
cfprAaaUserEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskCompletion.setStatus("current")
_CfprAaaUserEpFsmTaskFlags_Type = CfprFsmFlags
_CfprAaaUserEpFsmTaskFlags_Object = MibTableColumn
cfprAaaUserEpFsmTaskFlags = _CfprAaaUserEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 5),
    _CfprAaaUserEpFsmTaskFlags_Type()
)
cfprAaaUserEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskFlags.setStatus("current")
_CfprAaaUserEpFsmTaskItem_Type = CfprAaaUserEpFsmTaskItem
_CfprAaaUserEpFsmTaskItem_Object = MibTableColumn
cfprAaaUserEpFsmTaskItem = _CfprAaaUserEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 6),
    _CfprAaaUserEpFsmTaskItem_Type()
)
cfprAaaUserEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskItem.setStatus("current")
_CfprAaaUserEpFsmTaskSeqId_Type = Gauge32
_CfprAaaUserEpFsmTaskSeqId_Object = MibTableColumn
cfprAaaUserEpFsmTaskSeqId = _CfprAaaUserEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 54, 1, 7),
    _CfprAaaUserEpFsmTaskSeqId_Type()
)
cfprAaaUserEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserEpFsmTaskSeqId.setStatus("current")
_CfprAaaUserLocaleTable_Object = MibTable
cfprAaaUserLocaleTable = _CfprAaaUserLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55)
)
if mibBuilder.loadTexts:
    cfprAaaUserLocaleTable.setStatus("current")
_CfprAaaUserLocaleEntry_Object = MibTableRow
cfprAaaUserLocaleEntry = _CfprAaaUserLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1)
)
cfprAaaUserLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserLocaleEntry.setStatus("current")
_CfprAaaUserLocaleInstanceId_Type = CfprManagedObjectId
_CfprAaaUserLocaleInstanceId_Object = MibTableColumn
cfprAaaUserLocaleInstanceId = _CfprAaaUserLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 1),
    _CfprAaaUserLocaleInstanceId_Type()
)
cfprAaaUserLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleInstanceId.setStatus("current")
_CfprAaaUserLocaleDn_Type = CfprManagedObjectDn
_CfprAaaUserLocaleDn_Object = MibTableColumn
cfprAaaUserLocaleDn = _CfprAaaUserLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 2),
    _CfprAaaUserLocaleDn_Type()
)
cfprAaaUserLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleDn.setStatus("current")
_CfprAaaUserLocaleRn_Type = SnmpAdminString
_CfprAaaUserLocaleRn_Object = MibTableColumn
cfprAaaUserLocaleRn = _CfprAaaUserLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 3),
    _CfprAaaUserLocaleRn_Type()
)
cfprAaaUserLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleRn.setStatus("current")
_CfprAaaUserLocaleConfigState_Type = CfprAaaConfigState
_CfprAaaUserLocaleConfigState_Object = MibTableColumn
cfprAaaUserLocaleConfigState = _CfprAaaUserLocaleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 4),
    _CfprAaaUserLocaleConfigState_Type()
)
cfprAaaUserLocaleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleConfigState.setStatus("current")
_CfprAaaUserLocaleConfigStatusMessage_Type = SnmpAdminString
_CfprAaaUserLocaleConfigStatusMessage_Object = MibTableColumn
cfprAaaUserLocaleConfigStatusMessage = _CfprAaaUserLocaleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 5),
    _CfprAaaUserLocaleConfigStatusMessage_Type()
)
cfprAaaUserLocaleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleConfigStatusMessage.setStatus("current")
_CfprAaaUserLocaleDescr_Type = SnmpAdminString
_CfprAaaUserLocaleDescr_Object = MibTableColumn
cfprAaaUserLocaleDescr = _CfprAaaUserLocaleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 6),
    _CfprAaaUserLocaleDescr_Type()
)
cfprAaaUserLocaleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleDescr.setStatus("current")
_CfprAaaUserLocaleName_Type = SnmpAdminString
_CfprAaaUserLocaleName_Object = MibTableColumn
cfprAaaUserLocaleName = _CfprAaaUserLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 55, 1, 7),
    _CfprAaaUserLocaleName_Type()
)
cfprAaaUserLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLocaleName.setStatus("current")
_CfprAaaUserRoleTable_Object = MibTable
cfprAaaUserRoleTable = _CfprAaaUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56)
)
if mibBuilder.loadTexts:
    cfprAaaUserRoleTable.setStatus("current")
_CfprAaaUserRoleEntry_Object = MibTableRow
cfprAaaUserRoleEntry = _CfprAaaUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1)
)
cfprAaaUserRoleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserRoleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserRoleEntry.setStatus("current")
_CfprAaaUserRoleInstanceId_Type = CfprManagedObjectId
_CfprAaaUserRoleInstanceId_Object = MibTableColumn
cfprAaaUserRoleInstanceId = _CfprAaaUserRoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 1),
    _CfprAaaUserRoleInstanceId_Type()
)
cfprAaaUserRoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserRoleInstanceId.setStatus("current")
_CfprAaaUserRoleDn_Type = CfprManagedObjectDn
_CfprAaaUserRoleDn_Object = MibTableColumn
cfprAaaUserRoleDn = _CfprAaaUserRoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 2),
    _CfprAaaUserRoleDn_Type()
)
cfprAaaUserRoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRoleDn.setStatus("current")
_CfprAaaUserRoleRn_Type = SnmpAdminString
_CfprAaaUserRoleRn_Object = MibTableColumn
cfprAaaUserRoleRn = _CfprAaaUserRoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 3),
    _CfprAaaUserRoleRn_Type()
)
cfprAaaUserRoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRoleRn.setStatus("current")
_CfprAaaUserRoleConfigState_Type = CfprAaaConfigState
_CfprAaaUserRoleConfigState_Object = MibTableColumn
cfprAaaUserRoleConfigState = _CfprAaaUserRoleConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 4),
    _CfprAaaUserRoleConfigState_Type()
)
cfprAaaUserRoleConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRoleConfigState.setStatus("current")
_CfprAaaUserRoleConfigStatusMessage_Type = SnmpAdminString
_CfprAaaUserRoleConfigStatusMessage_Object = MibTableColumn
cfprAaaUserRoleConfigStatusMessage = _CfprAaaUserRoleConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 5),
    _CfprAaaUserRoleConfigStatusMessage_Type()
)
cfprAaaUserRoleConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRoleConfigStatusMessage.setStatus("current")
_CfprAaaUserRoleDescr_Type = SnmpAdminString
_CfprAaaUserRoleDescr_Object = MibTableColumn
cfprAaaUserRoleDescr = _CfprAaaUserRoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 6),
    _CfprAaaUserRoleDescr_Type()
)
cfprAaaUserRoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRoleDescr.setStatus("current")
_CfprAaaUserRoleName_Type = SnmpAdminString
_CfprAaaUserRoleName_Object = MibTableColumn
cfprAaaUserRoleName = _CfprAaaUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 56, 1, 7),
    _CfprAaaUserRoleName_Type()
)
cfprAaaUserRoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserRoleName.setStatus("current")
_CfprAaaWebLoginTable_Object = MibTable
cfprAaaWebLoginTable = _CfprAaaWebLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57)
)
if mibBuilder.loadTexts:
    cfprAaaWebLoginTable.setStatus("current")
_CfprAaaWebLoginEntry_Object = MibTableRow
cfprAaaWebLoginEntry = _CfprAaaWebLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1)
)
cfprAaaWebLoginEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaWebLoginInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaWebLoginEntry.setStatus("current")
_CfprAaaWebLoginInstanceId_Type = CfprManagedObjectId
_CfprAaaWebLoginInstanceId_Object = MibTableColumn
cfprAaaWebLoginInstanceId = _CfprAaaWebLoginInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 1),
    _CfprAaaWebLoginInstanceId_Type()
)
cfprAaaWebLoginInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaWebLoginInstanceId.setStatus("current")
_CfprAaaWebLoginDn_Type = CfprManagedObjectDn
_CfprAaaWebLoginDn_Object = MibTableColumn
cfprAaaWebLoginDn = _CfprAaaWebLoginDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 2),
    _CfprAaaWebLoginDn_Type()
)
cfprAaaWebLoginDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginDn.setStatus("current")
_CfprAaaWebLoginRn_Type = SnmpAdminString
_CfprAaaWebLoginRn_Object = MibTableColumn
cfprAaaWebLoginRn = _CfprAaaWebLoginRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 3),
    _CfprAaaWebLoginRn_Type()
)
cfprAaaWebLoginRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginRn.setStatus("current")
_CfprAaaWebLoginDescr_Type = SnmpAdminString
_CfprAaaWebLoginDescr_Object = MibTableColumn
cfprAaaWebLoginDescr = _CfprAaaWebLoginDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 4),
    _CfprAaaWebLoginDescr_Type()
)
cfprAaaWebLoginDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginDescr.setStatus("current")
_CfprAaaWebLoginId_Type = SnmpAdminString
_CfprAaaWebLoginId_Object = MibTableColumn
cfprAaaWebLoginId = _CfprAaaWebLoginId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 5),
    _CfprAaaWebLoginId_Type()
)
cfprAaaWebLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginId.setStatus("current")
_CfprAaaWebLoginIntId_Type = SnmpAdminString
_CfprAaaWebLoginIntId_Object = MibTableColumn
cfprAaaWebLoginIntId = _CfprAaaWebLoginIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 6),
    _CfprAaaWebLoginIntId_Type()
)
cfprAaaWebLoginIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginIntId.setStatus("current")
_CfprAaaWebLoginLocalHost_Type = SnmpAdminString
_CfprAaaWebLoginLocalHost_Object = MibTableColumn
cfprAaaWebLoginLocalHost = _CfprAaaWebLoginLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 7),
    _CfprAaaWebLoginLocalHost_Type()
)
cfprAaaWebLoginLocalHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginLocalHost.setStatus("current")
_CfprAaaWebLoginName_Type = SnmpAdminString
_CfprAaaWebLoginName_Object = MibTableColumn
cfprAaaWebLoginName = _CfprAaaWebLoginName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 8),
    _CfprAaaWebLoginName_Type()
)
cfprAaaWebLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginName.setStatus("current")
_CfprAaaWebLoginPolicyLevel_Type = Gauge32
_CfprAaaWebLoginPolicyLevel_Object = MibTableColumn
cfprAaaWebLoginPolicyLevel = _CfprAaaWebLoginPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 9),
    _CfprAaaWebLoginPolicyLevel_Type()
)
cfprAaaWebLoginPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginPolicyLevel.setStatus("current")
_CfprAaaWebLoginPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaWebLoginPolicyOwner_Object = MibTableColumn
cfprAaaWebLoginPolicyOwner = _CfprAaaWebLoginPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 10),
    _CfprAaaWebLoginPolicyOwner_Type()
)
cfprAaaWebLoginPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginPolicyOwner.setStatus("current")
_CfprAaaWebLoginRemoteHost_Type = SnmpAdminString
_CfprAaaWebLoginRemoteHost_Object = MibTableColumn
cfprAaaWebLoginRemoteHost = _CfprAaaWebLoginRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 11),
    _CfprAaaWebLoginRemoteHost_Type()
)
cfprAaaWebLoginRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginRemoteHost.setStatus("current")
_CfprAaaWebLoginSession_Type = CfprAaaSession
_CfprAaaWebLoginSession_Object = MibTableColumn
cfprAaaWebLoginSession = _CfprAaaWebLoginSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 12),
    _CfprAaaWebLoginSession_Type()
)
cfprAaaWebLoginSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginSession.setStatus("current")
_CfprAaaWebLoginSwitchId_Type = CfprNetworkSwitchId
_CfprAaaWebLoginSwitchId_Object = MibTableColumn
cfprAaaWebLoginSwitchId = _CfprAaaWebLoginSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 57, 1, 13),
    _CfprAaaWebLoginSwitchId_Type()
)
cfprAaaWebLoginSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaWebLoginSwitchId.setStatus("current")
_CfprAaaLoginRecTable_Object = MibTable
cfprAaaLoginRecTable = _CfprAaaLoginRecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58)
)
if mibBuilder.loadTexts:
    cfprAaaLoginRecTable.setStatus("current")
_CfprAaaLoginRecEntry_Object = MibTableRow
cfprAaaLoginRecEntry = _CfprAaaLoginRecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1)
)
cfprAaaLoginRecEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaLoginRecInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaLoginRecEntry.setStatus("current")
_CfprAaaLoginRecInstanceId_Type = CfprManagedObjectId
_CfprAaaLoginRecInstanceId_Object = MibTableColumn
cfprAaaLoginRecInstanceId = _CfprAaaLoginRecInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 1),
    _CfprAaaLoginRecInstanceId_Type()
)
cfprAaaLoginRecInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaLoginRecInstanceId.setStatus("current")
_CfprAaaLoginRecDn_Type = CfprManagedObjectDn
_CfprAaaLoginRecDn_Object = MibTableColumn
cfprAaaLoginRecDn = _CfprAaaLoginRecDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 2),
    _CfprAaaLoginRecDn_Type()
)
cfprAaaLoginRecDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLoginRecDn.setStatus("current")
_CfprAaaLoginRecRn_Type = SnmpAdminString
_CfprAaaLoginRecRn_Object = MibTableColumn
cfprAaaLoginRecRn = _CfprAaaLoginRecRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 3),
    _CfprAaaLoginRecRn_Type()
)
cfprAaaLoginRecRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLoginRecRn.setStatus("current")
_CfprAaaLoginRecHost_Type = SnmpAdminString
_CfprAaaLoginRecHost_Object = MibTableColumn
cfprAaaLoginRecHost = _CfprAaaLoginRecHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 4),
    _CfprAaaLoginRecHost_Type()
)
cfprAaaLoginRecHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLoginRecHost.setStatus("current")
_CfprAaaLoginRecName_Type = SnmpAdminString
_CfprAaaLoginRecName_Object = MibTableColumn
cfprAaaLoginRecName = _CfprAaaLoginRecName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 5),
    _CfprAaaLoginRecName_Type()
)
cfprAaaLoginRecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLoginRecName.setStatus("current")
_CfprAaaLoginRecTime_Type = SnmpAdminString
_CfprAaaLoginRecTime_Object = MibTableColumn
cfprAaaLoginRecTime = _CfprAaaLoginRecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 6),
    _CfprAaaLoginRecTime_Type()
)
cfprAaaLoginRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLoginRecTime.setStatus("current")
_CfprAaaLoginRecUser_Type = SnmpAdminString
_CfprAaaLoginRecUser_Object = MibTableColumn
cfprAaaLoginRecUser = _CfprAaaLoginRecUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 58, 1, 7),
    _CfprAaaLoginRecUser_Type()
)
cfprAaaLoginRecUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaLoginRecUser.setStatus("current")
_CfprAaaRoleRecTable_Object = MibTable
cfprAaaRoleRecTable = _CfprAaaRoleRecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59)
)
if mibBuilder.loadTexts:
    cfprAaaRoleRecTable.setStatus("current")
_CfprAaaRoleRecEntry_Object = MibTableRow
cfprAaaRoleRecEntry = _CfprAaaRoleRecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1)
)
cfprAaaRoleRecEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaRoleRecInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaRoleRecEntry.setStatus("current")
_CfprAaaRoleRecInstanceId_Type = CfprManagedObjectId
_CfprAaaRoleRecInstanceId_Object = MibTableColumn
cfprAaaRoleRecInstanceId = _CfprAaaRoleRecInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 1),
    _CfprAaaRoleRecInstanceId_Type()
)
cfprAaaRoleRecInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaRoleRecInstanceId.setStatus("current")
_CfprAaaRoleRecDn_Type = CfprManagedObjectDn
_CfprAaaRoleRecDn_Object = MibTableColumn
cfprAaaRoleRecDn = _CfprAaaRoleRecDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 2),
    _CfprAaaRoleRecDn_Type()
)
cfprAaaRoleRecDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecDn.setStatus("current")
_CfprAaaRoleRecRn_Type = SnmpAdminString
_CfprAaaRoleRecRn_Object = MibTableColumn
cfprAaaRoleRecRn = _CfprAaaRoleRecRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 3),
    _CfprAaaRoleRecRn_Type()
)
cfprAaaRoleRecRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecRn.setStatus("current")
_CfprAaaRoleRecCrntRole_Type = SnmpAdminString
_CfprAaaRoleRecCrntRole_Object = MibTableColumn
cfprAaaRoleRecCrntRole = _CfprAaaRoleRecCrntRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 4),
    _CfprAaaRoleRecCrntRole_Type()
)
cfprAaaRoleRecCrntRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecCrntRole.setStatus("current")
_CfprAaaRoleRecName_Type = SnmpAdminString
_CfprAaaRoleRecName_Object = MibTableColumn
cfprAaaRoleRecName = _CfprAaaRoleRecName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 5),
    _CfprAaaRoleRecName_Type()
)
cfprAaaRoleRecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecName.setStatus("current")
_CfprAaaRoleRecPrevRole_Type = SnmpAdminString
_CfprAaaRoleRecPrevRole_Object = MibTableColumn
cfprAaaRoleRecPrevRole = _CfprAaaRoleRecPrevRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 6),
    _CfprAaaRoleRecPrevRole_Type()
)
cfprAaaRoleRecPrevRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecPrevRole.setStatus("current")
_CfprAaaRoleRecTime_Type = SnmpAdminString
_CfprAaaRoleRecTime_Object = MibTableColumn
cfprAaaRoleRecTime = _CfprAaaRoleRecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 7),
    _CfprAaaRoleRecTime_Type()
)
cfprAaaRoleRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecTime.setStatus("current")
_CfprAaaRoleRecUser_Type = SnmpAdminString
_CfprAaaRoleRecUser_Object = MibTableColumn
cfprAaaRoleRecUser = _CfprAaaRoleRecUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 59, 1, 8),
    _CfprAaaRoleRecUser_Type()
)
cfprAaaRoleRecUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaRoleRecUser.setStatus("current")
_CfprAaaUserLoginInfoTable_Object = MibTable
cfprAaaUserLoginInfoTable = _CfprAaaUserLoginInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60)
)
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoTable.setStatus("current")
_CfprAaaUserLoginInfoEntry_Object = MibTableRow
cfprAaaUserLoginInfoEntry = _CfprAaaUserLoginInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60, 1)
)
cfprAaaUserLoginInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserLoginInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoEntry.setStatus("current")
_CfprAaaUserLoginInfoInstanceId_Type = CfprManagedObjectId
_CfprAaaUserLoginInfoInstanceId_Object = MibTableColumn
cfprAaaUserLoginInfoInstanceId = _CfprAaaUserLoginInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60, 1, 1),
    _CfprAaaUserLoginInfoInstanceId_Type()
)
cfprAaaUserLoginInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoInstanceId.setStatus("current")
_CfprAaaUserLoginInfoDn_Type = CfprManagedObjectDn
_CfprAaaUserLoginInfoDn_Object = MibTableColumn
cfprAaaUserLoginInfoDn = _CfprAaaUserLoginInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60, 1, 2),
    _CfprAaaUserLoginInfoDn_Type()
)
cfprAaaUserLoginInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoDn.setStatus("current")
_CfprAaaUserLoginInfoRn_Type = SnmpAdminString
_CfprAaaUserLoginInfoRn_Object = MibTableColumn
cfprAaaUserLoginInfoRn = _CfprAaaUserLoginInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60, 1, 3),
    _CfprAaaUserLoginInfoRn_Type()
)
cfprAaaUserLoginInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoRn.setStatus("current")
_CfprAaaUserLoginInfoNumFailedLogin_Type = Gauge32
_CfprAaaUserLoginInfoNumFailedLogin_Object = MibTableColumn
cfprAaaUserLoginInfoNumFailedLogin = _CfprAaaUserLoginInfoNumFailedLogin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60, 1, 4),
    _CfprAaaUserLoginInfoNumFailedLogin_Type()
)
cfprAaaUserLoginInfoNumFailedLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoNumFailedLogin.setStatus("current")
_CfprAaaUserLoginInfoNumSuccessLogin_Type = Gauge32
_CfprAaaUserLoginInfoNumSuccessLogin_Object = MibTableColumn
cfprAaaUserLoginInfoNumSuccessLogin = _CfprAaaUserLoginInfoNumSuccessLogin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 60, 1, 5),
    _CfprAaaUserLoginInfoNumSuccessLogin_Type()
)
cfprAaaUserLoginInfoNumSuccessLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserLoginInfoNumSuccessLogin.setStatus("current")
_CfprAaaPwdUserProfileTable_Object = MibTable
cfprAaaPwdUserProfileTable = _CfprAaaPwdUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61)
)
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileTable.setStatus("current")
_CfprAaaPwdUserProfileEntry_Object = MibTableRow
cfprAaaPwdUserProfileEntry = _CfprAaaPwdUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1)
)
cfprAaaPwdUserProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaPwdUserProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileEntry.setStatus("current")
_CfprAaaPwdUserProfileInstanceId_Type = CfprManagedObjectId
_CfprAaaPwdUserProfileInstanceId_Object = MibTableColumn
cfprAaaPwdUserProfileInstanceId = _CfprAaaPwdUserProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1, 1),
    _CfprAaaPwdUserProfileInstanceId_Type()
)
cfprAaaPwdUserProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileInstanceId.setStatus("current")
_CfprAaaPwdUserProfileDn_Type = CfprManagedObjectDn
_CfprAaaPwdUserProfileDn_Object = MibTableColumn
cfprAaaPwdUserProfileDn = _CfprAaaPwdUserProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1, 2),
    _CfprAaaPwdUserProfileDn_Type()
)
cfprAaaPwdUserProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileDn.setStatus("current")
_CfprAaaPwdUserProfileRn_Type = SnmpAdminString
_CfprAaaPwdUserProfileRn_Object = MibTableColumn
cfprAaaPwdUserProfileRn = _CfprAaaPwdUserProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1, 3),
    _CfprAaaPwdUserProfileRn_Type()
)
cfprAaaPwdUserProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileRn.setStatus("current")
_CfprAaaPwdUserProfileExpirationDays_Type = Gauge32
_CfprAaaPwdUserProfileExpirationDays_Object = MibTableColumn
cfprAaaPwdUserProfileExpirationDays = _CfprAaaPwdUserProfileExpirationDays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1, 4),
    _CfprAaaPwdUserProfileExpirationDays_Type()
)
cfprAaaPwdUserProfileExpirationDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileExpirationDays.setStatus("current")
_CfprAaaPwdUserProfileExpirationGracePeriod_Type = Gauge32
_CfprAaaPwdUserProfileExpirationGracePeriod_Object = MibTableColumn
cfprAaaPwdUserProfileExpirationGracePeriod = _CfprAaaPwdUserProfileExpirationGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1, 5),
    _CfprAaaPwdUserProfileExpirationGracePeriod_Type()
)
cfprAaaPwdUserProfileExpirationGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileExpirationGracePeriod.setStatus("current")
_CfprAaaPwdUserProfileExpirationWarnTime_Type = Gauge32
_CfprAaaPwdUserProfileExpirationWarnTime_Object = MibTableColumn
cfprAaaPwdUserProfileExpirationWarnTime = _CfprAaaPwdUserProfileExpirationWarnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 61, 1, 6),
    _CfprAaaPwdUserProfileExpirationWarnTime_Type()
)
cfprAaaPwdUserProfileExpirationWarnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaPwdUserProfileExpirationWarnTime.setStatus("current")
_CfprAaaSsoEpTable_Object = MibTable
cfprAaaSsoEpTable = _CfprAaaSsoEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62)
)
if mibBuilder.loadTexts:
    cfprAaaSsoEpTable.setStatus("current")
_CfprAaaSsoEpEntry_Object = MibTableRow
cfprAaaSsoEpEntry = _CfprAaaSsoEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1)
)
cfprAaaSsoEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSsoEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSsoEpEntry.setStatus("current")
_CfprAaaSsoEpInstanceId_Type = CfprManagedObjectId
_CfprAaaSsoEpInstanceId_Object = MibTableColumn
cfprAaaSsoEpInstanceId = _CfprAaaSsoEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 1),
    _CfprAaaSsoEpInstanceId_Type()
)
cfprAaaSsoEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSsoEpInstanceId.setStatus("current")
_CfprAaaSsoEpDn_Type = CfprManagedObjectDn
_CfprAaaSsoEpDn_Object = MibTableColumn
cfprAaaSsoEpDn = _CfprAaaSsoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 2),
    _CfprAaaSsoEpDn_Type()
)
cfprAaaSsoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpDn.setStatus("current")
_CfprAaaSsoEpRn_Type = SnmpAdminString
_CfprAaaSsoEpRn_Object = MibTableColumn
cfprAaaSsoEpRn = _CfprAaaSsoEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 3),
    _CfprAaaSsoEpRn_Type()
)
cfprAaaSsoEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpRn.setStatus("current")
_CfprAaaSsoEpDescr_Type = SnmpAdminString
_CfprAaaSsoEpDescr_Object = MibTableColumn
cfprAaaSsoEpDescr = _CfprAaaSsoEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 4),
    _CfprAaaSsoEpDescr_Type()
)
cfprAaaSsoEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpDescr.setStatus("current")
_CfprAaaSsoEpFsmDescr_Type = SnmpAdminString
_CfprAaaSsoEpFsmDescr_Object = MibTableColumn
cfprAaaSsoEpFsmDescr = _CfprAaaSsoEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 5),
    _CfprAaaSsoEpFsmDescr_Type()
)
cfprAaaSsoEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmDescr.setStatus("current")
_CfprAaaSsoEpFsmPrev_Type = SnmpAdminString
_CfprAaaSsoEpFsmPrev_Object = MibTableColumn
cfprAaaSsoEpFsmPrev = _CfprAaaSsoEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 6),
    _CfprAaaSsoEpFsmPrev_Type()
)
cfprAaaSsoEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmPrev.setStatus("current")
_CfprAaaSsoEpFsmProgr_Type = Gauge32
_CfprAaaSsoEpFsmProgr_Object = MibTableColumn
cfprAaaSsoEpFsmProgr = _CfprAaaSsoEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 7),
    _CfprAaaSsoEpFsmProgr_Type()
)
cfprAaaSsoEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmProgr.setStatus("current")
_CfprAaaSsoEpFsmRmtInvErrCode_Type = Gauge32
_CfprAaaSsoEpFsmRmtInvErrCode_Object = MibTableColumn
cfprAaaSsoEpFsmRmtInvErrCode = _CfprAaaSsoEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 8),
    _CfprAaaSsoEpFsmRmtInvErrCode_Type()
)
cfprAaaSsoEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRmtInvErrCode.setStatus("current")
_CfprAaaSsoEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprAaaSsoEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprAaaSsoEpFsmRmtInvErrDescr = _CfprAaaSsoEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 9),
    _CfprAaaSsoEpFsmRmtInvErrDescr_Type()
)
cfprAaaSsoEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRmtInvErrDescr.setStatus("current")
_CfprAaaSsoEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaSsoEpFsmRmtInvRslt_Object = MibTableColumn
cfprAaaSsoEpFsmRmtInvRslt = _CfprAaaSsoEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 10),
    _CfprAaaSsoEpFsmRmtInvRslt_Type()
)
cfprAaaSsoEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRmtInvRslt.setStatus("current")
_CfprAaaSsoEpFsmStageDescr_Type = SnmpAdminString
_CfprAaaSsoEpFsmStageDescr_Object = MibTableColumn
cfprAaaSsoEpFsmStageDescr = _CfprAaaSsoEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 11),
    _CfprAaaSsoEpFsmStageDescr_Type()
)
cfprAaaSsoEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageDescr.setStatus("current")
_CfprAaaSsoEpFsmStamp_Type = DateAndTime
_CfprAaaSsoEpFsmStamp_Object = MibTableColumn
cfprAaaSsoEpFsmStamp = _CfprAaaSsoEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 12),
    _CfprAaaSsoEpFsmStamp_Type()
)
cfprAaaSsoEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStamp.setStatus("current")
_CfprAaaSsoEpFsmStatus_Type = SnmpAdminString
_CfprAaaSsoEpFsmStatus_Object = MibTableColumn
cfprAaaSsoEpFsmStatus = _CfprAaaSsoEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 13),
    _CfprAaaSsoEpFsmStatus_Type()
)
cfprAaaSsoEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStatus.setStatus("current")
_CfprAaaSsoEpFsmTry_Type = Gauge32
_CfprAaaSsoEpFsmTry_Object = MibTableColumn
cfprAaaSsoEpFsmTry = _CfprAaaSsoEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 14),
    _CfprAaaSsoEpFsmTry_Type()
)
cfprAaaSsoEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmTry.setStatus("current")
_CfprAaaSsoEpIntId_Type = SnmpAdminString
_CfprAaaSsoEpIntId_Object = MibTableColumn
cfprAaaSsoEpIntId = _CfprAaaSsoEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 15),
    _CfprAaaSsoEpIntId_Type()
)
cfprAaaSsoEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpIntId.setStatus("current")
_CfprAaaSsoEpName_Type = SnmpAdminString
_CfprAaaSsoEpName_Object = MibTableColumn
cfprAaaSsoEpName = _CfprAaaSsoEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 16),
    _CfprAaaSsoEpName_Type()
)
cfprAaaSsoEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpName.setStatus("current")
_CfprAaaSsoEpPolicyLevel_Type = Gauge32
_CfprAaaSsoEpPolicyLevel_Object = MibTableColumn
cfprAaaSsoEpPolicyLevel = _CfprAaaSsoEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 17),
    _CfprAaaSsoEpPolicyLevel_Type()
)
cfprAaaSsoEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpPolicyLevel.setStatus("current")
_CfprAaaSsoEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaSsoEpPolicyOwner_Object = MibTableColumn
cfprAaaSsoEpPolicyOwner = _CfprAaaSsoEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 18),
    _CfprAaaSsoEpPolicyOwner_Type()
)
cfprAaaSsoEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpPolicyOwner.setStatus("current")
_CfprAaaSsoEpRetries_Type = Gauge32
_CfprAaaSsoEpRetries_Object = MibTableColumn
cfprAaaSsoEpRetries = _CfprAaaSsoEpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 19),
    _CfprAaaSsoEpRetries_Type()
)
cfprAaaSsoEpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpRetries.setStatus("current")
_CfprAaaSsoEpSsoEnabled_Type = TruthValue
_CfprAaaSsoEpSsoEnabled_Object = MibTableColumn
cfprAaaSsoEpSsoEnabled = _CfprAaaSsoEpSsoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 20),
    _CfprAaaSsoEpSsoEnabled_Type()
)
cfprAaaSsoEpSsoEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpSsoEnabled.setStatus("current")
_CfprAaaSsoEpTimeout_Type = Gauge32
_CfprAaaSsoEpTimeout_Object = MibTableColumn
cfprAaaSsoEpTimeout = _CfprAaaSsoEpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 62, 1, 21),
    _CfprAaaSsoEpTimeout_Type()
)
cfprAaaSsoEpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpTimeout.setStatus("current")
_CfprAaaSsoEpFsmTable_Object = MibTable
cfprAaaSsoEpFsmTable = _CfprAaaSsoEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63)
)
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmTable.setStatus("current")
_CfprAaaSsoEpFsmEntry_Object = MibTableRow
cfprAaaSsoEpFsmEntry = _CfprAaaSsoEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1)
)
cfprAaaSsoEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSsoEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmEntry.setStatus("current")
_CfprAaaSsoEpFsmInstanceId_Type = CfprManagedObjectId
_CfprAaaSsoEpFsmInstanceId_Object = MibTableColumn
cfprAaaSsoEpFsmInstanceId = _CfprAaaSsoEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 1),
    _CfprAaaSsoEpFsmInstanceId_Type()
)
cfprAaaSsoEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmInstanceId.setStatus("current")
_CfprAaaSsoEpFsmDn_Type = CfprManagedObjectDn
_CfprAaaSsoEpFsmDn_Object = MibTableColumn
cfprAaaSsoEpFsmDn = _CfprAaaSsoEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 2),
    _CfprAaaSsoEpFsmDn_Type()
)
cfprAaaSsoEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmDn.setStatus("current")
_CfprAaaSsoEpFsmRn_Type = SnmpAdminString
_CfprAaaSsoEpFsmRn_Object = MibTableColumn
cfprAaaSsoEpFsmRn = _CfprAaaSsoEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 3),
    _CfprAaaSsoEpFsmRn_Type()
)
cfprAaaSsoEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRn.setStatus("current")
_CfprAaaSsoEpFsmCompletionTime_Type = DateAndTime
_CfprAaaSsoEpFsmCompletionTime_Object = MibTableColumn
cfprAaaSsoEpFsmCompletionTime = _CfprAaaSsoEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 4),
    _CfprAaaSsoEpFsmCompletionTime_Type()
)
cfprAaaSsoEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmCompletionTime.setStatus("current")
_CfprAaaSsoEpFsmCurrentFsm_Type = CfprAaaSsoEpFsmCurrentFsm
_CfprAaaSsoEpFsmCurrentFsm_Object = MibTableColumn
cfprAaaSsoEpFsmCurrentFsm = _CfprAaaSsoEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 5),
    _CfprAaaSsoEpFsmCurrentFsm_Type()
)
cfprAaaSsoEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmCurrentFsm.setStatus("current")
_CfprAaaSsoEpFsmDescrData_Type = SnmpAdminString
_CfprAaaSsoEpFsmDescrData_Object = MibTableColumn
cfprAaaSsoEpFsmDescrData = _CfprAaaSsoEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 6),
    _CfprAaaSsoEpFsmDescrData_Type()
)
cfprAaaSsoEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmDescrData.setStatus("current")
_CfprAaaSsoEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprAaaSsoEpFsmFsmStatus_Object = MibTableColumn
cfprAaaSsoEpFsmFsmStatus = _CfprAaaSsoEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 7),
    _CfprAaaSsoEpFsmFsmStatus_Type()
)
cfprAaaSsoEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmFsmStatus.setStatus("current")
_CfprAaaSsoEpFsmProgress_Type = Gauge32
_CfprAaaSsoEpFsmProgress_Object = MibTableColumn
cfprAaaSsoEpFsmProgress = _CfprAaaSsoEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 8),
    _CfprAaaSsoEpFsmProgress_Type()
)
cfprAaaSsoEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmProgress.setStatus("current")
_CfprAaaSsoEpFsmRmtErrCode_Type = Gauge32
_CfprAaaSsoEpFsmRmtErrCode_Object = MibTableColumn
cfprAaaSsoEpFsmRmtErrCode = _CfprAaaSsoEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 9),
    _CfprAaaSsoEpFsmRmtErrCode_Type()
)
cfprAaaSsoEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRmtErrCode.setStatus("current")
_CfprAaaSsoEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprAaaSsoEpFsmRmtErrDescr_Object = MibTableColumn
cfprAaaSsoEpFsmRmtErrDescr = _CfprAaaSsoEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 10),
    _CfprAaaSsoEpFsmRmtErrDescr_Type()
)
cfprAaaSsoEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRmtErrDescr.setStatus("current")
_CfprAaaSsoEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprAaaSsoEpFsmRmtRslt_Object = MibTableColumn
cfprAaaSsoEpFsmRmtRslt = _CfprAaaSsoEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 63, 1, 11),
    _CfprAaaSsoEpFsmRmtRslt_Type()
)
cfprAaaSsoEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmRmtRslt.setStatus("current")
_CfprAaaSsoEpFsmStageTable_Object = MibTable
cfprAaaSsoEpFsmStageTable = _CfprAaaSsoEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64)
)
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageTable.setStatus("current")
_CfprAaaSsoEpFsmStageEntry_Object = MibTableRow
cfprAaaSsoEpFsmStageEntry = _CfprAaaSsoEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1)
)
cfprAaaSsoEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSsoEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageEntry.setStatus("current")
_CfprAaaSsoEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprAaaSsoEpFsmStageInstanceId_Object = MibTableColumn
cfprAaaSsoEpFsmStageInstanceId = _CfprAaaSsoEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 1),
    _CfprAaaSsoEpFsmStageInstanceId_Type()
)
cfprAaaSsoEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageInstanceId.setStatus("current")
_CfprAaaSsoEpFsmStageDn_Type = CfprManagedObjectDn
_CfprAaaSsoEpFsmStageDn_Object = MibTableColumn
cfprAaaSsoEpFsmStageDn = _CfprAaaSsoEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 2),
    _CfprAaaSsoEpFsmStageDn_Type()
)
cfprAaaSsoEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageDn.setStatus("current")
_CfprAaaSsoEpFsmStageRn_Type = SnmpAdminString
_CfprAaaSsoEpFsmStageRn_Object = MibTableColumn
cfprAaaSsoEpFsmStageRn = _CfprAaaSsoEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 3),
    _CfprAaaSsoEpFsmStageRn_Type()
)
cfprAaaSsoEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageRn.setStatus("current")
_CfprAaaSsoEpFsmStageDescrData_Type = SnmpAdminString
_CfprAaaSsoEpFsmStageDescrData_Object = MibTableColumn
cfprAaaSsoEpFsmStageDescrData = _CfprAaaSsoEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 4),
    _CfprAaaSsoEpFsmStageDescrData_Type()
)
cfprAaaSsoEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageDescrData.setStatus("current")
_CfprAaaSsoEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprAaaSsoEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprAaaSsoEpFsmStageLastUpdateTime = _CfprAaaSsoEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 5),
    _CfprAaaSsoEpFsmStageLastUpdateTime_Type()
)
cfprAaaSsoEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageLastUpdateTime.setStatus("current")
_CfprAaaSsoEpFsmStageName_Type = CfprAaaSsoEpFsmStageName
_CfprAaaSsoEpFsmStageName_Object = MibTableColumn
cfprAaaSsoEpFsmStageName = _CfprAaaSsoEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 6),
    _CfprAaaSsoEpFsmStageName_Type()
)
cfprAaaSsoEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageName.setStatus("current")
_CfprAaaSsoEpFsmStageOrder_Type = Gauge32
_CfprAaaSsoEpFsmStageOrder_Object = MibTableColumn
cfprAaaSsoEpFsmStageOrder = _CfprAaaSsoEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 7),
    _CfprAaaSsoEpFsmStageOrder_Type()
)
cfprAaaSsoEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageOrder.setStatus("current")
_CfprAaaSsoEpFsmStageRetry_Type = Gauge32
_CfprAaaSsoEpFsmStageRetry_Object = MibTableColumn
cfprAaaSsoEpFsmStageRetry = _CfprAaaSsoEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 8),
    _CfprAaaSsoEpFsmStageRetry_Type()
)
cfprAaaSsoEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageRetry.setStatus("current")
_CfprAaaSsoEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprAaaSsoEpFsmStageStageStatus_Object = MibTableColumn
cfprAaaSsoEpFsmStageStageStatus = _CfprAaaSsoEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 64, 1, 9),
    _CfprAaaSsoEpFsmStageStageStatus_Type()
)
cfprAaaSsoEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoEpFsmStageStageStatus.setStatus("current")
_CfprAaaSsoProviderTable_Object = MibTable
cfprAaaSsoProviderTable = _CfprAaaSsoProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65)
)
if mibBuilder.loadTexts:
    cfprAaaSsoProviderTable.setStatus("current")
_CfprAaaSsoProviderEntry_Object = MibTableRow
cfprAaaSsoProviderEntry = _CfprAaaSsoProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1)
)
cfprAaaSsoProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaSsoProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaSsoProviderEntry.setStatus("current")
_CfprAaaSsoProviderInstanceId_Type = CfprManagedObjectId
_CfprAaaSsoProviderInstanceId_Object = MibTableColumn
cfprAaaSsoProviderInstanceId = _CfprAaaSsoProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 1),
    _CfprAaaSsoProviderInstanceId_Type()
)
cfprAaaSsoProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderInstanceId.setStatus("current")
_CfprAaaSsoProviderDn_Type = CfprManagedObjectDn
_CfprAaaSsoProviderDn_Object = MibTableColumn
cfprAaaSsoProviderDn = _CfprAaaSsoProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 2),
    _CfprAaaSsoProviderDn_Type()
)
cfprAaaSsoProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderDn.setStatus("current")
_CfprAaaSsoProviderRn_Type = SnmpAdminString
_CfprAaaSsoProviderRn_Object = MibTableColumn
cfprAaaSsoProviderRn = _CfprAaaSsoProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 3),
    _CfprAaaSsoProviderRn_Type()
)
cfprAaaSsoProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderRn.setStatus("current")
_CfprAaaSsoProviderDescr_Type = SnmpAdminString
_CfprAaaSsoProviderDescr_Object = MibTableColumn
cfprAaaSsoProviderDescr = _CfprAaaSsoProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 4),
    _CfprAaaSsoProviderDescr_Type()
)
cfprAaaSsoProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderDescr.setStatus("current")
_CfprAaaSsoProviderEncKey_Type = SnmpAdminString
_CfprAaaSsoProviderEncKey_Object = MibTableColumn
cfprAaaSsoProviderEncKey = _CfprAaaSsoProviderEncKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 5),
    _CfprAaaSsoProviderEncKey_Type()
)
cfprAaaSsoProviderEncKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderEncKey.setStatus("current")
_CfprAaaSsoProviderIdpCert_Type = SnmpAdminString
_CfprAaaSsoProviderIdpCert_Object = MibTableColumn
cfprAaaSsoProviderIdpCert = _CfprAaaSsoProviderIdpCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 6),
    _CfprAaaSsoProviderIdpCert_Type()
)
cfprAaaSsoProviderIdpCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderIdpCert.setStatus("current")
_CfprAaaSsoProviderIdpIssuerUrl_Type = SnmpAdminString
_CfprAaaSsoProviderIdpIssuerUrl_Object = MibTableColumn
cfprAaaSsoProviderIdpIssuerUrl = _CfprAaaSsoProviderIdpIssuerUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 7),
    _CfprAaaSsoProviderIdpIssuerUrl_Type()
)
cfprAaaSsoProviderIdpIssuerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderIdpIssuerUrl.setStatus("current")
_CfprAaaSsoProviderIdpSsoUrl_Type = SnmpAdminString
_CfprAaaSsoProviderIdpSsoUrl_Object = MibTableColumn
cfprAaaSsoProviderIdpSsoUrl = _CfprAaaSsoProviderIdpSsoUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 8),
    _CfprAaaSsoProviderIdpSsoUrl_Type()
)
cfprAaaSsoProviderIdpSsoUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderIdpSsoUrl.setStatus("current")
_CfprAaaSsoProviderIdpXmlData_Type = SnmpAdminString
_CfprAaaSsoProviderIdpXmlData_Object = MibTableColumn
cfprAaaSsoProviderIdpXmlData = _CfprAaaSsoProviderIdpXmlData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 9),
    _CfprAaaSsoProviderIdpXmlData_Type()
)
cfprAaaSsoProviderIdpXmlData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderIdpXmlData.setStatus("current")
_CfprAaaSsoProviderKey_Type = SnmpAdminString
_CfprAaaSsoProviderKey_Object = MibTableColumn
cfprAaaSsoProviderKey = _CfprAaaSsoProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 10),
    _CfprAaaSsoProviderKey_Type()
)
cfprAaaSsoProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderKey.setStatus("current")
_CfprAaaSsoProviderKeySet_Type = TruthValue
_CfprAaaSsoProviderKeySet_Object = MibTableColumn
cfprAaaSsoProviderKeySet = _CfprAaaSsoProviderKeySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 11),
    _CfprAaaSsoProviderKeySet_Type()
)
cfprAaaSsoProviderKeySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderKeySet.setStatus("current")
_CfprAaaSsoProviderName_Type = SnmpAdminString
_CfprAaaSsoProviderName_Object = MibTableColumn
cfprAaaSsoProviderName = _CfprAaaSsoProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 12),
    _CfprAaaSsoProviderName_Type()
)
cfprAaaSsoProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderName.setStatus("current")
_CfprAaaSsoProviderOrder_Type = Gauge32
_CfprAaaSsoProviderOrder_Object = MibTableColumn
cfprAaaSsoProviderOrder = _CfprAaaSsoProviderOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 13),
    _CfprAaaSsoProviderOrder_Type()
)
cfprAaaSsoProviderOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderOrder.setStatus("current")
_CfprAaaSsoProviderRetries_Type = Gauge32
_CfprAaaSsoProviderRetries_Object = MibTableColumn
cfprAaaSsoProviderRetries = _CfprAaaSsoProviderRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 14),
    _CfprAaaSsoProviderRetries_Type()
)
cfprAaaSsoProviderRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderRetries.setStatus("current")
_CfprAaaSsoProviderTimeout_Type = Gauge32
_CfprAaaSsoProviderTimeout_Object = MibTableColumn
cfprAaaSsoProviderTimeout = _CfprAaaSsoProviderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 65, 1, 15),
    _CfprAaaSsoProviderTimeout_Type()
)
cfprAaaSsoProviderTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaSsoProviderTimeout.setStatus("current")
_CfprAaaUserOldPwdTable_Object = MibTable
cfprAaaUserOldPwdTable = _CfprAaaUserOldPwdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66)
)
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdTable.setStatus("current")
_CfprAaaUserOldPwdEntry_Object = MibTableRow
cfprAaaUserOldPwdEntry = _CfprAaaUserOldPwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1)
)
cfprAaaUserOldPwdEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AAA-MIB", "cfprAaaUserOldPwdInstanceId"),
)
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdEntry.setStatus("current")
_CfprAaaUserOldPwdInstanceId_Type = CfprManagedObjectId
_CfprAaaUserOldPwdInstanceId_Object = MibTableColumn
cfprAaaUserOldPwdInstanceId = _CfprAaaUserOldPwdInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 1),
    _CfprAaaUserOldPwdInstanceId_Type()
)
cfprAaaUserOldPwdInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdInstanceId.setStatus("current")
_CfprAaaUserOldPwdDn_Type = CfprManagedObjectDn
_CfprAaaUserOldPwdDn_Object = MibTableColumn
cfprAaaUserOldPwdDn = _CfprAaaUserOldPwdDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 2),
    _CfprAaaUserOldPwdDn_Type()
)
cfprAaaUserOldPwdDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdDn.setStatus("current")
_CfprAaaUserOldPwdRn_Type = SnmpAdminString
_CfprAaaUserOldPwdRn_Object = MibTableColumn
cfprAaaUserOldPwdRn = _CfprAaaUserOldPwdRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 3),
    _CfprAaaUserOldPwdRn_Type()
)
cfprAaaUserOldPwdRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdRn.setStatus("current")
_CfprAaaUserOldPwdDescr_Type = SnmpAdminString
_CfprAaaUserOldPwdDescr_Object = MibTableColumn
cfprAaaUserOldPwdDescr = _CfprAaaUserOldPwdDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 4),
    _CfprAaaUserOldPwdDescr_Type()
)
cfprAaaUserOldPwdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdDescr.setStatus("current")
_CfprAaaUserOldPwdEncPwd_Type = SnmpAdminString
_CfprAaaUserOldPwdEncPwd_Object = MibTableColumn
cfprAaaUserOldPwdEncPwd = _CfprAaaUserOldPwdEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 5),
    _CfprAaaUserOldPwdEncPwd_Type()
)
cfprAaaUserOldPwdEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdEncPwd.setStatus("current")
_CfprAaaUserOldPwdIntId_Type = SnmpAdminString
_CfprAaaUserOldPwdIntId_Object = MibTableColumn
cfprAaaUserOldPwdIntId = _CfprAaaUserOldPwdIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 6),
    _CfprAaaUserOldPwdIntId_Type()
)
cfprAaaUserOldPwdIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdIntId.setStatus("current")
_CfprAaaUserOldPwdName_Type = SnmpAdminString
_CfprAaaUserOldPwdName_Object = MibTableColumn
cfprAaaUserOldPwdName = _CfprAaaUserOldPwdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 7),
    _CfprAaaUserOldPwdName_Type()
)
cfprAaaUserOldPwdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdName.setStatus("current")
_CfprAaaUserOldPwdPolicyLevel_Type = Gauge32
_CfprAaaUserOldPwdPolicyLevel_Object = MibTableColumn
cfprAaaUserOldPwdPolicyLevel = _CfprAaaUserOldPwdPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 8),
    _CfprAaaUserOldPwdPolicyLevel_Type()
)
cfprAaaUserOldPwdPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdPolicyLevel.setStatus("current")
_CfprAaaUserOldPwdPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprAaaUserOldPwdPolicyOwner_Object = MibTableColumn
cfprAaaUserOldPwdPolicyOwner = _CfprAaaUserOldPwdPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 9),
    _CfprAaaUserOldPwdPolicyOwner_Type()
)
cfprAaaUserOldPwdPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdPolicyOwner.setStatus("current")
_CfprAaaUserOldPwdPwdEndDate_Type = DateAndTime
_CfprAaaUserOldPwdPwdEndDate_Object = MibTableColumn
cfprAaaUserOldPwdPwdEndDate = _CfprAaaUserOldPwdPwdEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 2, 66, 1, 10),
    _CfprAaaUserOldPwdPwdEndDate_Type()
)
cfprAaaUserOldPwdPwdEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprAaaUserOldPwdPwdEndDate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AAA-MIB",
    **{"cfprAaaObjects": cfprAaaObjects,
       "cfprAaaAuthRealmTable": cfprAaaAuthRealmTable,
       "cfprAaaAuthRealmEntry": cfprAaaAuthRealmEntry,
       "cfprAaaAuthRealmInstanceId": cfprAaaAuthRealmInstanceId,
       "cfprAaaAuthRealmDn": cfprAaaAuthRealmDn,
       "cfprAaaAuthRealmRn": cfprAaaAuthRealmRn,
       "cfprAaaAuthRealmConLogin": cfprAaaAuthRealmConLogin,
       "cfprAaaAuthRealmDefLogin": cfprAaaAuthRealmDefLogin,
       "cfprAaaAuthRealmDefRolePolicy": cfprAaaAuthRealmDefRolePolicy,
       "cfprAaaAuthRealmDescr": cfprAaaAuthRealmDescr,
       "cfprAaaAuthRealmFsmDescr": cfprAaaAuthRealmFsmDescr,
       "cfprAaaAuthRealmFsmPrev": cfprAaaAuthRealmFsmPrev,
       "cfprAaaAuthRealmFsmProgr": cfprAaaAuthRealmFsmProgr,
       "cfprAaaAuthRealmFsmRmtInvErrCode": cfprAaaAuthRealmFsmRmtInvErrCode,
       "cfprAaaAuthRealmFsmRmtInvErrDescr": cfprAaaAuthRealmFsmRmtInvErrDescr,
       "cfprAaaAuthRealmFsmRmtInvRslt": cfprAaaAuthRealmFsmRmtInvRslt,
       "cfprAaaAuthRealmFsmStageDescr": cfprAaaAuthRealmFsmStageDescr,
       "cfprAaaAuthRealmFsmStamp": cfprAaaAuthRealmFsmStamp,
       "cfprAaaAuthRealmFsmStatus": cfprAaaAuthRealmFsmStatus,
       "cfprAaaAuthRealmFsmTry": cfprAaaAuthRealmFsmTry,
       "cfprAaaAuthRealmIntId": cfprAaaAuthRealmIntId,
       "cfprAaaAuthRealmName": cfprAaaAuthRealmName,
       "cfprAaaAuthRealmPolicyLevel": cfprAaaAuthRealmPolicyLevel,
       "cfprAaaAuthRealmPolicyOwner": cfprAaaAuthRealmPolicyOwner,
       "cfprAaaAuthRealmFsmTable": cfprAaaAuthRealmFsmTable,
       "cfprAaaAuthRealmFsmEntry": cfprAaaAuthRealmFsmEntry,
       "cfprAaaAuthRealmFsmInstanceId": cfprAaaAuthRealmFsmInstanceId,
       "cfprAaaAuthRealmFsmDn": cfprAaaAuthRealmFsmDn,
       "cfprAaaAuthRealmFsmRn": cfprAaaAuthRealmFsmRn,
       "cfprAaaAuthRealmFsmCompletionTime": cfprAaaAuthRealmFsmCompletionTime,
       "cfprAaaAuthRealmFsmCurrentFsm": cfprAaaAuthRealmFsmCurrentFsm,
       "cfprAaaAuthRealmFsmDescrData": cfprAaaAuthRealmFsmDescrData,
       "cfprAaaAuthRealmFsmFsmStatus": cfprAaaAuthRealmFsmFsmStatus,
       "cfprAaaAuthRealmFsmProgress": cfprAaaAuthRealmFsmProgress,
       "cfprAaaAuthRealmFsmRmtErrCode": cfprAaaAuthRealmFsmRmtErrCode,
       "cfprAaaAuthRealmFsmRmtErrDescr": cfprAaaAuthRealmFsmRmtErrDescr,
       "cfprAaaAuthRealmFsmRmtRslt": cfprAaaAuthRealmFsmRmtRslt,
       "cfprAaaAuthRealmFsmStageTable": cfprAaaAuthRealmFsmStageTable,
       "cfprAaaAuthRealmFsmStageEntry": cfprAaaAuthRealmFsmStageEntry,
       "cfprAaaAuthRealmFsmStageInstanceId": cfprAaaAuthRealmFsmStageInstanceId,
       "cfprAaaAuthRealmFsmStageDn": cfprAaaAuthRealmFsmStageDn,
       "cfprAaaAuthRealmFsmStageRn": cfprAaaAuthRealmFsmStageRn,
       "cfprAaaAuthRealmFsmStageDescrData": cfprAaaAuthRealmFsmStageDescrData,
       "cfprAaaAuthRealmFsmStageLastUpdateTime": cfprAaaAuthRealmFsmStageLastUpdateTime,
       "cfprAaaAuthRealmFsmStageName": cfprAaaAuthRealmFsmStageName,
       "cfprAaaAuthRealmFsmStageOrder": cfprAaaAuthRealmFsmStageOrder,
       "cfprAaaAuthRealmFsmStageRetry": cfprAaaAuthRealmFsmStageRetry,
       "cfprAaaAuthRealmFsmStageStageStatus": cfprAaaAuthRealmFsmStageStageStatus,
       "cfprAaaCimcSessionTable": cfprAaaCimcSessionTable,
       "cfprAaaCimcSessionEntry": cfprAaaCimcSessionEntry,
       "cfprAaaCimcSessionInstanceId": cfprAaaCimcSessionInstanceId,
       "cfprAaaCimcSessionDn": cfprAaaCimcSessionDn,
       "cfprAaaCimcSessionRn": cfprAaaCimcSessionRn,
       "cfprAaaCimcSessionAdminState": cfprAaaCimcSessionAdminState,
       "cfprAaaCimcSessionCimcAddr": cfprAaaCimcSessionCimcAddr,
       "cfprAaaCimcSessionId": cfprAaaCimcSessionId,
       "cfprAaaCimcSessionIntDel": cfprAaaCimcSessionIntDel,
       "cfprAaaCimcSessionIsDelete": cfprAaaCimcSessionIsDelete,
       "cfprAaaCimcSessionLastUpdatedTime": cfprAaaCimcSessionLastUpdatedTime,
       "cfprAaaCimcSessionLoginTime": cfprAaaCimcSessionLoginTime,
       "cfprAaaCimcSessionLsDn": cfprAaaCimcSessionLsDn,
       "cfprAaaCimcSessionPid": cfprAaaCimcSessionPid,
       "cfprAaaCimcSessionPnDn": cfprAaaCimcSessionPnDn,
       "cfprAaaCimcSessionPriv": cfprAaaCimcSessionPriv,
       "cfprAaaCimcSessionSourceAddr": cfprAaaCimcSessionSourceAddr,
       "cfprAaaCimcSessionType": cfprAaaCimcSessionType,
       "cfprAaaCimcSessionUser": cfprAaaCimcSessionUser,
       "cfprAaaConsoleAuthTable": cfprAaaConsoleAuthTable,
       "cfprAaaConsoleAuthEntry": cfprAaaConsoleAuthEntry,
       "cfprAaaConsoleAuthInstanceId": cfprAaaConsoleAuthInstanceId,
       "cfprAaaConsoleAuthDn": cfprAaaConsoleAuthDn,
       "cfprAaaConsoleAuthRn": cfprAaaConsoleAuthRn,
       "cfprAaaConsoleAuthDescr": cfprAaaConsoleAuthDescr,
       "cfprAaaConsoleAuthName": cfprAaaConsoleAuthName,
       "cfprAaaConsoleAuthOperProviderGroup": cfprAaaConsoleAuthOperProviderGroup,
       "cfprAaaConsoleAuthOperRealm": cfprAaaConsoleAuthOperRealm,
       "cfprAaaConsoleAuthProviderGroup": cfprAaaConsoleAuthProviderGroup,
       "cfprAaaConsoleAuthRealm": cfprAaaConsoleAuthRealm,
       "cfprAaaConsoleAuthUse2Factor": cfprAaaConsoleAuthUse2Factor,
       "cfprAaaDefaultAuthTable": cfprAaaDefaultAuthTable,
       "cfprAaaDefaultAuthEntry": cfprAaaDefaultAuthEntry,
       "cfprAaaDefaultAuthInstanceId": cfprAaaDefaultAuthInstanceId,
       "cfprAaaDefaultAuthDn": cfprAaaDefaultAuthDn,
       "cfprAaaDefaultAuthRn": cfprAaaDefaultAuthRn,
       "cfprAaaDefaultAuthDescr": cfprAaaDefaultAuthDescr,
       "cfprAaaDefaultAuthName": cfprAaaDefaultAuthName,
       "cfprAaaDefaultAuthOperProviderGroup": cfprAaaDefaultAuthOperProviderGroup,
       "cfprAaaDefaultAuthOperRealm": cfprAaaDefaultAuthOperRealm,
       "cfprAaaDefaultAuthProviderGroup": cfprAaaDefaultAuthProviderGroup,
       "cfprAaaDefaultAuthRealm": cfprAaaDefaultAuthRealm,
       "cfprAaaDefaultAuthRefreshPeriod": cfprAaaDefaultAuthRefreshPeriod,
       "cfprAaaDefaultAuthSessionTimeout": cfprAaaDefaultAuthSessionTimeout,
       "cfprAaaDefaultAuthUse2Factor": cfprAaaDefaultAuthUse2Factor,
       "cfprAaaDefaultAuthAbsoluteSessionTimeout": cfprAaaDefaultAuthAbsoluteSessionTimeout,
       "cfprAaaDefaultAuthConAbsoluteSessionTimeout": cfprAaaDefaultAuthConAbsoluteSessionTimeout,
       "cfprAaaDefaultAuthConSessionTimeout": cfprAaaDefaultAuthConSessionTimeout,
       "cfprAaaDomainTable": cfprAaaDomainTable,
       "cfprAaaDomainEntry": cfprAaaDomainEntry,
       "cfprAaaDomainInstanceId": cfprAaaDomainInstanceId,
       "cfprAaaDomainDn": cfprAaaDomainDn,
       "cfprAaaDomainRn": cfprAaaDomainRn,
       "cfprAaaDomainDescr": cfprAaaDomainDescr,
       "cfprAaaDomainName": cfprAaaDomainName,
       "cfprAaaDomainRefreshPeriod": cfprAaaDomainRefreshPeriod,
       "cfprAaaDomainSessionTimeout": cfprAaaDomainSessionTimeout,
       "cfprAaaDomainAbsoluteSessionTimeout": cfprAaaDomainAbsoluteSessionTimeout,
       "cfprAaaDomainConAbsoluteSessionTimeout": cfprAaaDomainConAbsoluteSessionTimeout,
       "cfprAaaDomainConSessionTimeout": cfprAaaDomainConSessionTimeout,
       "cfprAaaDomainAuthTable": cfprAaaDomainAuthTable,
       "cfprAaaDomainAuthEntry": cfprAaaDomainAuthEntry,
       "cfprAaaDomainAuthInstanceId": cfprAaaDomainAuthInstanceId,
       "cfprAaaDomainAuthDn": cfprAaaDomainAuthDn,
       "cfprAaaDomainAuthRn": cfprAaaDomainAuthRn,
       "cfprAaaDomainAuthDescr": cfprAaaDomainAuthDescr,
       "cfprAaaDomainAuthName": cfprAaaDomainAuthName,
       "cfprAaaDomainAuthOperProviderGroup": cfprAaaDomainAuthOperProviderGroup,
       "cfprAaaDomainAuthOperRealm": cfprAaaDomainAuthOperRealm,
       "cfprAaaDomainAuthProviderGroup": cfprAaaDomainAuthProviderGroup,
       "cfprAaaDomainAuthRealm": cfprAaaDomainAuthRealm,
       "cfprAaaDomainAuthUse2Factor": cfprAaaDomainAuthUse2Factor,
       "cfprAaaEpAuthProfileTable": cfprAaaEpAuthProfileTable,
       "cfprAaaEpAuthProfileEntry": cfprAaaEpAuthProfileEntry,
       "cfprAaaEpAuthProfileInstanceId": cfprAaaEpAuthProfileInstanceId,
       "cfprAaaEpAuthProfileDn": cfprAaaEpAuthProfileDn,
       "cfprAaaEpAuthProfileRn": cfprAaaEpAuthProfileRn,
       "cfprAaaEpAuthProfileDescr": cfprAaaEpAuthProfileDescr,
       "cfprAaaEpAuthProfileIntId": cfprAaaEpAuthProfileIntId,
       "cfprAaaEpAuthProfileIpmiOverLan": cfprAaaEpAuthProfileIpmiOverLan,
       "cfprAaaEpAuthProfileName": cfprAaaEpAuthProfileName,
       "cfprAaaEpAuthProfilePolicyLevel": cfprAaaEpAuthProfilePolicyLevel,
       "cfprAaaEpAuthProfilePolicyOwner": cfprAaaEpAuthProfilePolicyOwner,
       "cfprAaaEpFsmTable": cfprAaaEpFsmTable,
       "cfprAaaEpFsmEntry": cfprAaaEpFsmEntry,
       "cfprAaaEpFsmInstanceId": cfprAaaEpFsmInstanceId,
       "cfprAaaEpFsmDn": cfprAaaEpFsmDn,
       "cfprAaaEpFsmRn": cfprAaaEpFsmRn,
       "cfprAaaEpFsmCompletionTime": cfprAaaEpFsmCompletionTime,
       "cfprAaaEpFsmCurrentFsm": cfprAaaEpFsmCurrentFsm,
       "cfprAaaEpFsmDescr": cfprAaaEpFsmDescr,
       "cfprAaaEpFsmFsmStatus": cfprAaaEpFsmFsmStatus,
       "cfprAaaEpFsmProgress": cfprAaaEpFsmProgress,
       "cfprAaaEpFsmRmtErrCode": cfprAaaEpFsmRmtErrCode,
       "cfprAaaEpFsmRmtErrDescr": cfprAaaEpFsmRmtErrDescr,
       "cfprAaaEpFsmRmtRslt": cfprAaaEpFsmRmtRslt,
       "cfprAaaEpFsmStageTable": cfprAaaEpFsmStageTable,
       "cfprAaaEpFsmStageEntry": cfprAaaEpFsmStageEntry,
       "cfprAaaEpFsmStageInstanceId": cfprAaaEpFsmStageInstanceId,
       "cfprAaaEpFsmStageDn": cfprAaaEpFsmStageDn,
       "cfprAaaEpFsmStageRn": cfprAaaEpFsmStageRn,
       "cfprAaaEpFsmStageDescr": cfprAaaEpFsmStageDescr,
       "cfprAaaEpFsmStageLastUpdateTime": cfprAaaEpFsmStageLastUpdateTime,
       "cfprAaaEpFsmStageName": cfprAaaEpFsmStageName,
       "cfprAaaEpFsmStageOrder": cfprAaaEpFsmStageOrder,
       "cfprAaaEpFsmStageRetry": cfprAaaEpFsmStageRetry,
       "cfprAaaEpFsmStageStageStatus": cfprAaaEpFsmStageStageStatus,
       "cfprAaaEpFsmTaskTable": cfprAaaEpFsmTaskTable,
       "cfprAaaEpFsmTaskEntry": cfprAaaEpFsmTaskEntry,
       "cfprAaaEpFsmTaskInstanceId": cfprAaaEpFsmTaskInstanceId,
       "cfprAaaEpFsmTaskDn": cfprAaaEpFsmTaskDn,
       "cfprAaaEpFsmTaskRn": cfprAaaEpFsmTaskRn,
       "cfprAaaEpFsmTaskCompletion": cfprAaaEpFsmTaskCompletion,
       "cfprAaaEpFsmTaskFlags": cfprAaaEpFsmTaskFlags,
       "cfprAaaEpFsmTaskItem": cfprAaaEpFsmTaskItem,
       "cfprAaaEpFsmTaskSeqId": cfprAaaEpFsmTaskSeqId,
       "cfprAaaEpLoginTable": cfprAaaEpLoginTable,
       "cfprAaaEpLoginEntry": cfprAaaEpLoginEntry,
       "cfprAaaEpLoginInstanceId": cfprAaaEpLoginInstanceId,
       "cfprAaaEpLoginDn": cfprAaaEpLoginDn,
       "cfprAaaEpLoginRn": cfprAaaEpLoginRn,
       "cfprAaaEpLoginDescr": cfprAaaEpLoginDescr,
       "cfprAaaEpLoginId": cfprAaaEpLoginId,
       "cfprAaaEpLoginIntId": cfprAaaEpLoginIntId,
       "cfprAaaEpLoginLocalHost": cfprAaaEpLoginLocalHost,
       "cfprAaaEpLoginName": cfprAaaEpLoginName,
       "cfprAaaEpLoginPolicyLevel": cfprAaaEpLoginPolicyLevel,
       "cfprAaaEpLoginPolicyOwner": cfprAaaEpLoginPolicyOwner,
       "cfprAaaEpLoginRemoteHost": cfprAaaEpLoginRemoteHost,
       "cfprAaaEpLoginSession": cfprAaaEpLoginSession,
       "cfprAaaEpLoginSwitchId": cfprAaaEpLoginSwitchId,
       "cfprAaaEpUserTable": cfprAaaEpUserTable,
       "cfprAaaEpUserEntry": cfprAaaEpUserEntry,
       "cfprAaaEpUserInstanceId": cfprAaaEpUserInstanceId,
       "cfprAaaEpUserDn": cfprAaaEpUserDn,
       "cfprAaaEpUserRn": cfprAaaEpUserRn,
       "cfprAaaEpUserConfigState": cfprAaaEpUserConfigState,
       "cfprAaaEpUserConfigStatusMessage": cfprAaaEpUserConfigStatusMessage,
       "cfprAaaEpUserDescr": cfprAaaEpUserDescr,
       "cfprAaaEpUserName": cfprAaaEpUserName,
       "cfprAaaEpUserPriv": cfprAaaEpUserPriv,
       "cfprAaaEpUserPwd": cfprAaaEpUserPwd,
       "cfprAaaEpUserPwdSet": cfprAaaEpUserPwdSet,
       "cfprAaaExtMgmtCutThruTknTable": cfprAaaExtMgmtCutThruTknTable,
       "cfprAaaExtMgmtCutThruTknEntry": cfprAaaExtMgmtCutThruTknEntry,
       "cfprAaaExtMgmtCutThruTknInstanceId": cfprAaaExtMgmtCutThruTknInstanceId,
       "cfprAaaExtMgmtCutThruTknDn": cfprAaaExtMgmtCutThruTknDn,
       "cfprAaaExtMgmtCutThruTknRn": cfprAaaExtMgmtCutThruTknRn,
       "cfprAaaExtMgmtCutThruTknAuthDomain": cfprAaaExtMgmtCutThruTknAuthDomain,
       "cfprAaaExtMgmtCutThruTknAuthUser": cfprAaaExtMgmtCutThruTknAuthUser,
       "cfprAaaExtMgmtCutThruTknCreationTime": cfprAaaExtMgmtCutThruTknCreationTime,
       "cfprAaaExtMgmtCutThruTknDescr": cfprAaaExtMgmtCutThruTknDescr,
       "cfprAaaExtMgmtCutThruTknIntId": cfprAaaExtMgmtCutThruTknIntId,
       "cfprAaaExtMgmtCutThruTknLocales": cfprAaaExtMgmtCutThruTknLocales,
       "cfprAaaExtMgmtCutThruTknName": cfprAaaExtMgmtCutThruTknName,
       "cfprAaaExtMgmtCutThruTknPnDn": cfprAaaExtMgmtCutThruTknPnDn,
       "cfprAaaExtMgmtCutThruTknPolicyLevel": cfprAaaExtMgmtCutThruTknPolicyLevel,
       "cfprAaaExtMgmtCutThruTknPolicyOwner": cfprAaaExtMgmtCutThruTknPolicyOwner,
       "cfprAaaExtMgmtCutThruTknPriv": cfprAaaExtMgmtCutThruTknPriv,
       "cfprAaaExtMgmtCutThruTknRemote": cfprAaaExtMgmtCutThruTknRemote,
       "cfprAaaExtMgmtCutThruTknToken": cfprAaaExtMgmtCutThruTknToken,
       "cfprAaaExtMgmtCutThruTknType": cfprAaaExtMgmtCutThruTknType,
       "cfprAaaExtMgmtCutThruTknUser": cfprAaaExtMgmtCutThruTknUser,
       "cfprAaaLdapEpTable": cfprAaaLdapEpTable,
       "cfprAaaLdapEpEntry": cfprAaaLdapEpEntry,
       "cfprAaaLdapEpInstanceId": cfprAaaLdapEpInstanceId,
       "cfprAaaLdapEpDn": cfprAaaLdapEpDn,
       "cfprAaaLdapEpRn": cfprAaaLdapEpRn,
       "cfprAaaLdapEpAttribute": cfprAaaLdapEpAttribute,
       "cfprAaaLdapEpBasedn": cfprAaaLdapEpBasedn,
       "cfprAaaLdapEpDescr": cfprAaaLdapEpDescr,
       "cfprAaaLdapEpFilter": cfprAaaLdapEpFilter,
       "cfprAaaLdapEpFsmDescr": cfprAaaLdapEpFsmDescr,
       "cfprAaaLdapEpFsmPrev": cfprAaaLdapEpFsmPrev,
       "cfprAaaLdapEpFsmProgr": cfprAaaLdapEpFsmProgr,
       "cfprAaaLdapEpFsmRmtInvErrCode": cfprAaaLdapEpFsmRmtInvErrCode,
       "cfprAaaLdapEpFsmRmtInvErrDescr": cfprAaaLdapEpFsmRmtInvErrDescr,
       "cfprAaaLdapEpFsmRmtInvRslt": cfprAaaLdapEpFsmRmtInvRslt,
       "cfprAaaLdapEpFsmStageDescr": cfprAaaLdapEpFsmStageDescr,
       "cfprAaaLdapEpFsmStamp": cfprAaaLdapEpFsmStamp,
       "cfprAaaLdapEpFsmStatus": cfprAaaLdapEpFsmStatus,
       "cfprAaaLdapEpFsmTry": cfprAaaLdapEpFsmTry,
       "cfprAaaLdapEpIntId": cfprAaaLdapEpIntId,
       "cfprAaaLdapEpName": cfprAaaLdapEpName,
       "cfprAaaLdapEpPolicyLevel": cfprAaaLdapEpPolicyLevel,
       "cfprAaaLdapEpPolicyOwner": cfprAaaLdapEpPolicyOwner,
       "cfprAaaLdapEpRetries": cfprAaaLdapEpRetries,
       "cfprAaaLdapEpTimeout": cfprAaaLdapEpTimeout,
       "cfprAaaLdapEpTlsVer": cfprAaaLdapEpTlsVer,
       "cfprAaaLdapEpFsmTable": cfprAaaLdapEpFsmTable,
       "cfprAaaLdapEpFsmEntry": cfprAaaLdapEpFsmEntry,
       "cfprAaaLdapEpFsmInstanceId": cfprAaaLdapEpFsmInstanceId,
       "cfprAaaLdapEpFsmDn": cfprAaaLdapEpFsmDn,
       "cfprAaaLdapEpFsmRn": cfprAaaLdapEpFsmRn,
       "cfprAaaLdapEpFsmCompletionTime": cfprAaaLdapEpFsmCompletionTime,
       "cfprAaaLdapEpFsmCurrentFsm": cfprAaaLdapEpFsmCurrentFsm,
       "cfprAaaLdapEpFsmDescrData": cfprAaaLdapEpFsmDescrData,
       "cfprAaaLdapEpFsmFsmStatus": cfprAaaLdapEpFsmFsmStatus,
       "cfprAaaLdapEpFsmProgress": cfprAaaLdapEpFsmProgress,
       "cfprAaaLdapEpFsmRmtErrCode": cfprAaaLdapEpFsmRmtErrCode,
       "cfprAaaLdapEpFsmRmtErrDescr": cfprAaaLdapEpFsmRmtErrDescr,
       "cfprAaaLdapEpFsmRmtRslt": cfprAaaLdapEpFsmRmtRslt,
       "cfprAaaLdapEpFsmStageTable": cfprAaaLdapEpFsmStageTable,
       "cfprAaaLdapEpFsmStageEntry": cfprAaaLdapEpFsmStageEntry,
       "cfprAaaLdapEpFsmStageInstanceId": cfprAaaLdapEpFsmStageInstanceId,
       "cfprAaaLdapEpFsmStageDn": cfprAaaLdapEpFsmStageDn,
       "cfprAaaLdapEpFsmStageRn": cfprAaaLdapEpFsmStageRn,
       "cfprAaaLdapEpFsmStageDescrData": cfprAaaLdapEpFsmStageDescrData,
       "cfprAaaLdapEpFsmStageLastUpdateTime": cfprAaaLdapEpFsmStageLastUpdateTime,
       "cfprAaaLdapEpFsmStageName": cfprAaaLdapEpFsmStageName,
       "cfprAaaLdapEpFsmStageOrder": cfprAaaLdapEpFsmStageOrder,
       "cfprAaaLdapEpFsmStageRetry": cfprAaaLdapEpFsmStageRetry,
       "cfprAaaLdapEpFsmStageStageStatus": cfprAaaLdapEpFsmStageStageStatus,
       "cfprAaaLdapGroupTable": cfprAaaLdapGroupTable,
       "cfprAaaLdapGroupEntry": cfprAaaLdapGroupEntry,
       "cfprAaaLdapGroupInstanceId": cfprAaaLdapGroupInstanceId,
       "cfprAaaLdapGroupDn": cfprAaaLdapGroupDn,
       "cfprAaaLdapGroupRn": cfprAaaLdapGroupRn,
       "cfprAaaLdapGroupDescr": cfprAaaLdapGroupDescr,
       "cfprAaaLdapGroupName": cfprAaaLdapGroupName,
       "cfprAaaLdapGroupRuleTable": cfprAaaLdapGroupRuleTable,
       "cfprAaaLdapGroupRuleEntry": cfprAaaLdapGroupRuleEntry,
       "cfprAaaLdapGroupRuleInstanceId": cfprAaaLdapGroupRuleInstanceId,
       "cfprAaaLdapGroupRuleDn": cfprAaaLdapGroupRuleDn,
       "cfprAaaLdapGroupRuleRn": cfprAaaLdapGroupRuleRn,
       "cfprAaaLdapGroupRuleAuthorization": cfprAaaLdapGroupRuleAuthorization,
       "cfprAaaLdapGroupRuleDescr": cfprAaaLdapGroupRuleDescr,
       "cfprAaaLdapGroupRuleName": cfprAaaLdapGroupRuleName,
       "cfprAaaLdapGroupRuleTargetAttr": cfprAaaLdapGroupRuleTargetAttr,
       "cfprAaaLdapGroupRuleTraversal": cfprAaaLdapGroupRuleTraversal,
       "cfprAaaLdapGroupRuleUsePrimaryGroup": cfprAaaLdapGroupRuleUsePrimaryGroup,
       "cfprAaaLdapProviderTable": cfprAaaLdapProviderTable,
       "cfprAaaLdapProviderEntry": cfprAaaLdapProviderEntry,
       "cfprAaaLdapProviderInstanceId": cfprAaaLdapProviderInstanceId,
       "cfprAaaLdapProviderDn": cfprAaaLdapProviderDn,
       "cfprAaaLdapProviderRn": cfprAaaLdapProviderRn,
       "cfprAaaLdapProviderAttribute": cfprAaaLdapProviderAttribute,
       "cfprAaaLdapProviderBasedn": cfprAaaLdapProviderBasedn,
       "cfprAaaLdapProviderDescr": cfprAaaLdapProviderDescr,
       "cfprAaaLdapProviderEnableSSL": cfprAaaLdapProviderEnableSSL,
       "cfprAaaLdapProviderEncKey": cfprAaaLdapProviderEncKey,
       "cfprAaaLdapProviderFilter": cfprAaaLdapProviderFilter,
       "cfprAaaLdapProviderKey": cfprAaaLdapProviderKey,
       "cfprAaaLdapProviderKeySet": cfprAaaLdapProviderKeySet,
       "cfprAaaLdapProviderName": cfprAaaLdapProviderName,
       "cfprAaaLdapProviderOrder": cfprAaaLdapProviderOrder,
       "cfprAaaLdapProviderPort": cfprAaaLdapProviderPort,
       "cfprAaaLdapProviderRetries": cfprAaaLdapProviderRetries,
       "cfprAaaLdapProviderRootdn": cfprAaaLdapProviderRootdn,
       "cfprAaaLdapProviderTimeout": cfprAaaLdapProviderTimeout,
       "cfprAaaLdapProviderVendor": cfprAaaLdapProviderVendor,
       "cfprAaaLdapProviderKeyring": cfprAaaLdapProviderKeyring,
       "cfprAaaLdapProviderRevokePolicy": cfprAaaLdapProviderRevokePolicy,
       "cfprAaaLdapProviderCipher": cfprAaaLdapProviderCipher,
       "cfprAaaLdapProviderCiphermode": cfprAaaLdapProviderCiphermode,
       "cfprAaaLdapProviderFqdnEnforce": cfprAaaLdapProviderFqdnEnforce,
       "cfprAaaLocaleTable": cfprAaaLocaleTable,
       "cfprAaaLocaleEntry": cfprAaaLocaleEntry,
       "cfprAaaLocaleInstanceId": cfprAaaLocaleInstanceId,
       "cfprAaaLocaleDn": cfprAaaLocaleDn,
       "cfprAaaLocaleRn": cfprAaaLocaleRn,
       "cfprAaaLocaleConfigState": cfprAaaLocaleConfigState,
       "cfprAaaLocaleConfigStatusMessage": cfprAaaLocaleConfigStatusMessage,
       "cfprAaaLocaleDescr": cfprAaaLocaleDescr,
       "cfprAaaLocaleIntId": cfprAaaLocaleIntId,
       "cfprAaaLocaleName": cfprAaaLocaleName,
       "cfprAaaLocalePolicyLevel": cfprAaaLocalePolicyLevel,
       "cfprAaaLocalePolicyOwner": cfprAaaLocalePolicyOwner,
       "cfprAaaLogTable": cfprAaaLogTable,
       "cfprAaaLogEntry": cfprAaaLogEntry,
       "cfprAaaLogInstanceId": cfprAaaLogInstanceId,
       "cfprAaaLogDn": cfprAaaLogDn,
       "cfprAaaLogRn": cfprAaaLogRn,
       "cfprAaaLogMaxSize": cfprAaaLogMaxSize,
       "cfprAaaLogPurgeWindow": cfprAaaLogPurgeWindow,
       "cfprAaaLogSize": cfprAaaLogSize,
       "cfprAaaModLRTable": cfprAaaModLRTable,
       "cfprAaaModLREntry": cfprAaaModLREntry,
       "cfprAaaModLRInstanceId": cfprAaaModLRInstanceId,
       "cfprAaaModLRDn": cfprAaaModLRDn,
       "cfprAaaModLRRn": cfprAaaModLRRn,
       "cfprAaaModLRAffected": cfprAaaModLRAffected,
       "cfprAaaModLRCause": cfprAaaModLRCause,
       "cfprAaaModLRChangeSet": cfprAaaModLRChangeSet,
       "cfprAaaModLRCode": cfprAaaModLRCode,
       "cfprAaaModLRCreated": cfprAaaModLRCreated,
       "cfprAaaModLRDescr": cfprAaaModLRDescr,
       "cfprAaaModLRId": cfprAaaModLRId,
       "cfprAaaModLRInd": cfprAaaModLRInd,
       "cfprAaaModLRSessionId": cfprAaaModLRSessionId,
       "cfprAaaModLRSeverity": cfprAaaModLRSeverity,
       "cfprAaaModLRTrig": cfprAaaModLRTrig,
       "cfprAaaModLRTxId": cfprAaaModLRTxId,
       "cfprAaaModLRUser": cfprAaaModLRUser,
       "cfprAaaOrgTable": cfprAaaOrgTable,
       "cfprAaaOrgEntry": cfprAaaOrgEntry,
       "cfprAaaOrgInstanceId": cfprAaaOrgInstanceId,
       "cfprAaaOrgDn": cfprAaaOrgDn,
       "cfprAaaOrgRn": cfprAaaOrgRn,
       "cfprAaaOrgConfigState": cfprAaaOrgConfigState,
       "cfprAaaOrgConfigStatusMessage": cfprAaaOrgConfigStatusMessage,
       "cfprAaaOrgDescr": cfprAaaOrgDescr,
       "cfprAaaOrgName": cfprAaaOrgName,
       "cfprAaaOrgOrgDn": cfprAaaOrgOrgDn,
       "cfprAaaPreLoginBannerTable": cfprAaaPreLoginBannerTable,
       "cfprAaaPreLoginBannerEntry": cfprAaaPreLoginBannerEntry,
       "cfprAaaPreLoginBannerInstanceId": cfprAaaPreLoginBannerInstanceId,
       "cfprAaaPreLoginBannerDn": cfprAaaPreLoginBannerDn,
       "cfprAaaPreLoginBannerRn": cfprAaaPreLoginBannerRn,
       "cfprAaaPreLoginBannerDescr": cfprAaaPreLoginBannerDescr,
       "cfprAaaPreLoginBannerIntId": cfprAaaPreLoginBannerIntId,
       "cfprAaaPreLoginBannerMessage": cfprAaaPreLoginBannerMessage,
       "cfprAaaPreLoginBannerName": cfprAaaPreLoginBannerName,
       "cfprAaaPreLoginBannerPolicyLevel": cfprAaaPreLoginBannerPolicyLevel,
       "cfprAaaPreLoginBannerPolicyOwner": cfprAaaPreLoginBannerPolicyOwner,
       "cfprAaaProviderGroupTable": cfprAaaProviderGroupTable,
       "cfprAaaProviderGroupEntry": cfprAaaProviderGroupEntry,
       "cfprAaaProviderGroupInstanceId": cfprAaaProviderGroupInstanceId,
       "cfprAaaProviderGroupDn": cfprAaaProviderGroupDn,
       "cfprAaaProviderGroupRn": cfprAaaProviderGroupRn,
       "cfprAaaProviderGroupConfigState": cfprAaaProviderGroupConfigState,
       "cfprAaaProviderGroupDescr": cfprAaaProviderGroupDescr,
       "cfprAaaProviderGroupName": cfprAaaProviderGroupName,
       "cfprAaaProviderGroupSize": cfprAaaProviderGroupSize,
       "cfprAaaProviderRefTable": cfprAaaProviderRefTable,
       "cfprAaaProviderRefEntry": cfprAaaProviderRefEntry,
       "cfprAaaProviderRefInstanceId": cfprAaaProviderRefInstanceId,
       "cfprAaaProviderRefDn": cfprAaaProviderRefDn,
       "cfprAaaProviderRefRn": cfprAaaProviderRefRn,
       "cfprAaaProviderRefDescr": cfprAaaProviderRefDescr,
       "cfprAaaProviderRefName": cfprAaaProviderRefName,
       "cfprAaaProviderRefOrder": cfprAaaProviderRefOrder,
       "cfprAaaPwdProfileTable": cfprAaaPwdProfileTable,
       "cfprAaaPwdProfileEntry": cfprAaaPwdProfileEntry,
       "cfprAaaPwdProfileInstanceId": cfprAaaPwdProfileInstanceId,
       "cfprAaaPwdProfileDn": cfprAaaPwdProfileDn,
       "cfprAaaPwdProfileRn": cfprAaaPwdProfileRn,
       "cfprAaaPwdProfileChangeCount": cfprAaaPwdProfileChangeCount,
       "cfprAaaPwdProfileChangeDuringInterval": cfprAaaPwdProfileChangeDuringInterval,
       "cfprAaaPwdProfileChangeInterval": cfprAaaPwdProfileChangeInterval,
       "cfprAaaPwdProfileExpirationWarnTime": cfprAaaPwdProfileExpirationWarnTime,
       "cfprAaaPwdProfileHistoryCount": cfprAaaPwdProfileHistoryCount,
       "cfprAaaPwdProfileNoChangeInterval": cfprAaaPwdProfileNoChangeInterval,
       "cfprAaaPwdProfileExpirationDays": cfprAaaPwdProfileExpirationDays,
       "cfprAaaPwdProfileExpirationGracePeriod": cfprAaaPwdProfileExpirationGracePeriod,
       "cfprAaaPwdProfileReuseTime": cfprAaaPwdProfileReuseTime,
       "cfprAaaRadiusEpTable": cfprAaaRadiusEpTable,
       "cfprAaaRadiusEpEntry": cfprAaaRadiusEpEntry,
       "cfprAaaRadiusEpInstanceId": cfprAaaRadiusEpInstanceId,
       "cfprAaaRadiusEpDn": cfprAaaRadiusEpDn,
       "cfprAaaRadiusEpRn": cfprAaaRadiusEpRn,
       "cfprAaaRadiusEpDescr": cfprAaaRadiusEpDescr,
       "cfprAaaRadiusEpFsmDescr": cfprAaaRadiusEpFsmDescr,
       "cfprAaaRadiusEpFsmPrev": cfprAaaRadiusEpFsmPrev,
       "cfprAaaRadiusEpFsmProgr": cfprAaaRadiusEpFsmProgr,
       "cfprAaaRadiusEpFsmRmtInvErrCode": cfprAaaRadiusEpFsmRmtInvErrCode,
       "cfprAaaRadiusEpFsmRmtInvErrDescr": cfprAaaRadiusEpFsmRmtInvErrDescr,
       "cfprAaaRadiusEpFsmRmtInvRslt": cfprAaaRadiusEpFsmRmtInvRslt,
       "cfprAaaRadiusEpFsmStageDescr": cfprAaaRadiusEpFsmStageDescr,
       "cfprAaaRadiusEpFsmStamp": cfprAaaRadiusEpFsmStamp,
       "cfprAaaRadiusEpFsmStatus": cfprAaaRadiusEpFsmStatus,
       "cfprAaaRadiusEpFsmTry": cfprAaaRadiusEpFsmTry,
       "cfprAaaRadiusEpIntId": cfprAaaRadiusEpIntId,
       "cfprAaaRadiusEpName": cfprAaaRadiusEpName,
       "cfprAaaRadiusEpPolicyLevel": cfprAaaRadiusEpPolicyLevel,
       "cfprAaaRadiusEpPolicyOwner": cfprAaaRadiusEpPolicyOwner,
       "cfprAaaRadiusEpRetries": cfprAaaRadiusEpRetries,
       "cfprAaaRadiusEpTimeout": cfprAaaRadiusEpTimeout,
       "cfprAaaRadiusEpFsmTable": cfprAaaRadiusEpFsmTable,
       "cfprAaaRadiusEpFsmEntry": cfprAaaRadiusEpFsmEntry,
       "cfprAaaRadiusEpFsmInstanceId": cfprAaaRadiusEpFsmInstanceId,
       "cfprAaaRadiusEpFsmDn": cfprAaaRadiusEpFsmDn,
       "cfprAaaRadiusEpFsmRn": cfprAaaRadiusEpFsmRn,
       "cfprAaaRadiusEpFsmCompletionTime": cfprAaaRadiusEpFsmCompletionTime,
       "cfprAaaRadiusEpFsmCurrentFsm": cfprAaaRadiusEpFsmCurrentFsm,
       "cfprAaaRadiusEpFsmDescrData": cfprAaaRadiusEpFsmDescrData,
       "cfprAaaRadiusEpFsmFsmStatus": cfprAaaRadiusEpFsmFsmStatus,
       "cfprAaaRadiusEpFsmProgress": cfprAaaRadiusEpFsmProgress,
       "cfprAaaRadiusEpFsmRmtErrCode": cfprAaaRadiusEpFsmRmtErrCode,
       "cfprAaaRadiusEpFsmRmtErrDescr": cfprAaaRadiusEpFsmRmtErrDescr,
       "cfprAaaRadiusEpFsmRmtRslt": cfprAaaRadiusEpFsmRmtRslt,
       "cfprAaaRadiusEpFsmStageTable": cfprAaaRadiusEpFsmStageTable,
       "cfprAaaRadiusEpFsmStageEntry": cfprAaaRadiusEpFsmStageEntry,
       "cfprAaaRadiusEpFsmStageInstanceId": cfprAaaRadiusEpFsmStageInstanceId,
       "cfprAaaRadiusEpFsmStageDn": cfprAaaRadiusEpFsmStageDn,
       "cfprAaaRadiusEpFsmStageRn": cfprAaaRadiusEpFsmStageRn,
       "cfprAaaRadiusEpFsmStageDescrData": cfprAaaRadiusEpFsmStageDescrData,
       "cfprAaaRadiusEpFsmStageLastUpdateTime": cfprAaaRadiusEpFsmStageLastUpdateTime,
       "cfprAaaRadiusEpFsmStageName": cfprAaaRadiusEpFsmStageName,
       "cfprAaaRadiusEpFsmStageOrder": cfprAaaRadiusEpFsmStageOrder,
       "cfprAaaRadiusEpFsmStageRetry": cfprAaaRadiusEpFsmStageRetry,
       "cfprAaaRadiusEpFsmStageStageStatus": cfprAaaRadiusEpFsmStageStageStatus,
       "cfprAaaRadiusProviderTable": cfprAaaRadiusProviderTable,
       "cfprAaaRadiusProviderEntry": cfprAaaRadiusProviderEntry,
       "cfprAaaRadiusProviderInstanceId": cfprAaaRadiusProviderInstanceId,
       "cfprAaaRadiusProviderDn": cfprAaaRadiusProviderDn,
       "cfprAaaRadiusProviderRn": cfprAaaRadiusProviderRn,
       "cfprAaaRadiusProviderAuthPort": cfprAaaRadiusProviderAuthPort,
       "cfprAaaRadiusProviderDescr": cfprAaaRadiusProviderDescr,
       "cfprAaaRadiusProviderEncKey": cfprAaaRadiusProviderEncKey,
       "cfprAaaRadiusProviderKey": cfprAaaRadiusProviderKey,
       "cfprAaaRadiusProviderKeySet": cfprAaaRadiusProviderKeySet,
       "cfprAaaRadiusProviderName": cfprAaaRadiusProviderName,
       "cfprAaaRadiusProviderOrder": cfprAaaRadiusProviderOrder,
       "cfprAaaRadiusProviderRetries": cfprAaaRadiusProviderRetries,
       "cfprAaaRadiusProviderService": cfprAaaRadiusProviderService,
       "cfprAaaRadiusProviderTimeout": cfprAaaRadiusProviderTimeout,
       "cfprAaaRealmFsmTable": cfprAaaRealmFsmTable,
       "cfprAaaRealmFsmEntry": cfprAaaRealmFsmEntry,
       "cfprAaaRealmFsmInstanceId": cfprAaaRealmFsmInstanceId,
       "cfprAaaRealmFsmDn": cfprAaaRealmFsmDn,
       "cfprAaaRealmFsmRn": cfprAaaRealmFsmRn,
       "cfprAaaRealmFsmCompletionTime": cfprAaaRealmFsmCompletionTime,
       "cfprAaaRealmFsmCurrentFsm": cfprAaaRealmFsmCurrentFsm,
       "cfprAaaRealmFsmDescr": cfprAaaRealmFsmDescr,
       "cfprAaaRealmFsmFsmStatus": cfprAaaRealmFsmFsmStatus,
       "cfprAaaRealmFsmProgress": cfprAaaRealmFsmProgress,
       "cfprAaaRealmFsmRmtErrCode": cfprAaaRealmFsmRmtErrCode,
       "cfprAaaRealmFsmRmtErrDescr": cfprAaaRealmFsmRmtErrDescr,
       "cfprAaaRealmFsmRmtRslt": cfprAaaRealmFsmRmtRslt,
       "cfprAaaRealmFsmStageTable": cfprAaaRealmFsmStageTable,
       "cfprAaaRealmFsmStageEntry": cfprAaaRealmFsmStageEntry,
       "cfprAaaRealmFsmStageInstanceId": cfprAaaRealmFsmStageInstanceId,
       "cfprAaaRealmFsmStageDn": cfprAaaRealmFsmStageDn,
       "cfprAaaRealmFsmStageRn": cfprAaaRealmFsmStageRn,
       "cfprAaaRealmFsmStageDescr": cfprAaaRealmFsmStageDescr,
       "cfprAaaRealmFsmStageLastUpdateTime": cfprAaaRealmFsmStageLastUpdateTime,
       "cfprAaaRealmFsmStageName": cfprAaaRealmFsmStageName,
       "cfprAaaRealmFsmStageOrder": cfprAaaRealmFsmStageOrder,
       "cfprAaaRealmFsmStageRetry": cfprAaaRealmFsmStageRetry,
       "cfprAaaRealmFsmStageStageStatus": cfprAaaRealmFsmStageStageStatus,
       "cfprAaaRealmFsmTaskTable": cfprAaaRealmFsmTaskTable,
       "cfprAaaRealmFsmTaskEntry": cfprAaaRealmFsmTaskEntry,
       "cfprAaaRealmFsmTaskInstanceId": cfprAaaRealmFsmTaskInstanceId,
       "cfprAaaRealmFsmTaskDn": cfprAaaRealmFsmTaskDn,
       "cfprAaaRealmFsmTaskRn": cfprAaaRealmFsmTaskRn,
       "cfprAaaRealmFsmTaskCompletion": cfprAaaRealmFsmTaskCompletion,
       "cfprAaaRealmFsmTaskFlags": cfprAaaRealmFsmTaskFlags,
       "cfprAaaRealmFsmTaskItem": cfprAaaRealmFsmTaskItem,
       "cfprAaaRealmFsmTaskSeqId": cfprAaaRealmFsmTaskSeqId,
       "cfprAaaRemoteUserTable": cfprAaaRemoteUserTable,
       "cfprAaaRemoteUserEntry": cfprAaaRemoteUserEntry,
       "cfprAaaRemoteUserInstanceId": cfprAaaRemoteUserInstanceId,
       "cfprAaaRemoteUserDn": cfprAaaRemoteUserDn,
       "cfprAaaRemoteUserRn": cfprAaaRemoteUserRn,
       "cfprAaaRemoteUserConfigState": cfprAaaRemoteUserConfigState,
       "cfprAaaRemoteUserConfigStatusMessage": cfprAaaRemoteUserConfigStatusMessage,
       "cfprAaaRemoteUserDescr": cfprAaaRemoteUserDescr,
       "cfprAaaRemoteUserName": cfprAaaRemoteUserName,
       "cfprAaaRemoteUserPwd": cfprAaaRemoteUserPwd,
       "cfprAaaRemoteUserPwdSet": cfprAaaRemoteUserPwdSet,
       "cfprAaaRoleTable": cfprAaaRoleTable,
       "cfprAaaRoleEntry": cfprAaaRoleEntry,
       "cfprAaaRoleInstanceId": cfprAaaRoleInstanceId,
       "cfprAaaRoleDn": cfprAaaRoleDn,
       "cfprAaaRoleRn": cfprAaaRoleRn,
       "cfprAaaRoleConfigState": cfprAaaRoleConfigState,
       "cfprAaaRoleConfigStatusMessage": cfprAaaRoleConfigStatusMessage,
       "cfprAaaRoleDescr": cfprAaaRoleDescr,
       "cfprAaaRoleIntId": cfprAaaRoleIntId,
       "cfprAaaRoleName": cfprAaaRoleName,
       "cfprAaaRolePolicyLevel": cfprAaaRolePolicyLevel,
       "cfprAaaRolePolicyOwner": cfprAaaRolePolicyOwner,
       "cfprAaaRolePriv": cfprAaaRolePriv,
       "cfprAaaSessionTable": cfprAaaSessionTable,
       "cfprAaaSessionEntry": cfprAaaSessionEntry,
       "cfprAaaSessionInstanceId": cfprAaaSessionInstanceId,
       "cfprAaaSessionDn": cfprAaaSessionDn,
       "cfprAaaSessionRn": cfprAaaSessionRn,
       "cfprAaaSessionHost": cfprAaaSessionHost,
       "cfprAaaSessionId": cfprAaaSessionId,
       "cfprAaaSessionIntDel": cfprAaaSessionIntDel,
       "cfprAaaSessionLoginTime": cfprAaaSessionLoginTime,
       "cfprAaaSessionPid": cfprAaaSessionPid,
       "cfprAaaSessionRefreshPeriod": cfprAaaSessionRefreshPeriod,
       "cfprAaaSessionSessionTimeout": cfprAaaSessionSessionTimeout,
       "cfprAaaSessionSwitchId": cfprAaaSessionSwitchId,
       "cfprAaaSessionTerm": cfprAaaSessionTerm,
       "cfprAaaSessionUi": cfprAaaSessionUi,
       "cfprAaaSessionUser": cfprAaaSessionUser,
       "cfprAaaSessionAbsoluteSessionTimeout": cfprAaaSessionAbsoluteSessionTimeout,
       "cfprAaaSessionInfoTable": cfprAaaSessionInfoTable,
       "cfprAaaSessionInfoEntry": cfprAaaSessionInfoEntry,
       "cfprAaaSessionInfoInstanceId": cfprAaaSessionInfoInstanceId,
       "cfprAaaSessionInfoDn": cfprAaaSessionInfoDn,
       "cfprAaaSessionInfoRn": cfprAaaSessionInfoRn,
       "cfprAaaSessionInfoAddress": cfprAaaSessionInfoAddress,
       "cfprAaaSessionInfoDestIp": cfprAaaSessionInfoDestIp,
       "cfprAaaSessionInfoEtime": cfprAaaSessionInfoEtime,
       "cfprAaaSessionInfoId": cfprAaaSessionInfoId,
       "cfprAaaSessionInfoPriv": cfprAaaSessionInfoPriv,
       "cfprAaaSessionInfoType": cfprAaaSessionInfoType,
       "cfprAaaSessionInfoUser": cfprAaaSessionInfoUser,
       "cfprAaaSessionInfoUserType": cfprAaaSessionInfoUserType,
       "cfprAaaSessionInfoTableTable": cfprAaaSessionInfoTableTable,
       "cfprAaaSessionInfoTableEntry": cfprAaaSessionInfoTableEntry,
       "cfprAaaSessionInfoTableInstanceId": cfprAaaSessionInfoTableInstanceId,
       "cfprAaaSessionInfoTableDn": cfprAaaSessionInfoTableDn,
       "cfprAaaSessionInfoTableRn": cfprAaaSessionInfoTableRn,
       "cfprAaaSessionLRTable": cfprAaaSessionLRTable,
       "cfprAaaSessionLREntry": cfprAaaSessionLREntry,
       "cfprAaaSessionLRInstanceId": cfprAaaSessionLRInstanceId,
       "cfprAaaSessionLRDn": cfprAaaSessionLRDn,
       "cfprAaaSessionLRRn": cfprAaaSessionLRRn,
       "cfprAaaSessionLRAffected": cfprAaaSessionLRAffected,
       "cfprAaaSessionLRCause": cfprAaaSessionLRCause,
       "cfprAaaSessionLRChangeSet": cfprAaaSessionLRChangeSet,
       "cfprAaaSessionLRCode": cfprAaaSessionLRCode,
       "cfprAaaSessionLRCreated": cfprAaaSessionLRCreated,
       "cfprAaaSessionLRDescr": cfprAaaSessionLRDescr,
       "cfprAaaSessionLRId": cfprAaaSessionLRId,
       "cfprAaaSessionLRInd": cfprAaaSessionLRInd,
       "cfprAaaSessionLRSessionId": cfprAaaSessionLRSessionId,
       "cfprAaaSessionLRSeverity": cfprAaaSessionLRSeverity,
       "cfprAaaSessionLRTrig": cfprAaaSessionLRTrig,
       "cfprAaaSessionLRTxId": cfprAaaSessionLRTxId,
       "cfprAaaSessionLRUser": cfprAaaSessionLRUser,
       "cfprAaaShellLoginTable": cfprAaaShellLoginTable,
       "cfprAaaShellLoginEntry": cfprAaaShellLoginEntry,
       "cfprAaaShellLoginInstanceId": cfprAaaShellLoginInstanceId,
       "cfprAaaShellLoginDn": cfprAaaShellLoginDn,
       "cfprAaaShellLoginRn": cfprAaaShellLoginRn,
       "cfprAaaShellLoginDescr": cfprAaaShellLoginDescr,
       "cfprAaaShellLoginId": cfprAaaShellLoginId,
       "cfprAaaShellLoginIntId": cfprAaaShellLoginIntId,
       "cfprAaaShellLoginLocalHost": cfprAaaShellLoginLocalHost,
       "cfprAaaShellLoginName": cfprAaaShellLoginName,
       "cfprAaaShellLoginPolicyLevel": cfprAaaShellLoginPolicyLevel,
       "cfprAaaShellLoginPolicyOwner": cfprAaaShellLoginPolicyOwner,
       "cfprAaaShellLoginRemoteHost": cfprAaaShellLoginRemoteHost,
       "cfprAaaShellLoginSession": cfprAaaShellLoginSession,
       "cfprAaaShellLoginSwitchId": cfprAaaShellLoginSwitchId,
       "cfprAaaSshAuthTable": cfprAaaSshAuthTable,
       "cfprAaaSshAuthEntry": cfprAaaSshAuthEntry,
       "cfprAaaSshAuthInstanceId": cfprAaaSshAuthInstanceId,
       "cfprAaaSshAuthDn": cfprAaaSshAuthDn,
       "cfprAaaSshAuthRn": cfprAaaSshAuthRn,
       "cfprAaaSshAuthData": cfprAaaSshAuthData,
       "cfprAaaSshAuthOldStrType": cfprAaaSshAuthOldStrType,
       "cfprAaaSshAuthStrType": cfprAaaSshAuthStrType,
       "cfprAaaTacacsPlusEpTable": cfprAaaTacacsPlusEpTable,
       "cfprAaaTacacsPlusEpEntry": cfprAaaTacacsPlusEpEntry,
       "cfprAaaTacacsPlusEpInstanceId": cfprAaaTacacsPlusEpInstanceId,
       "cfprAaaTacacsPlusEpDn": cfprAaaTacacsPlusEpDn,
       "cfprAaaTacacsPlusEpRn": cfprAaaTacacsPlusEpRn,
       "cfprAaaTacacsPlusEpDescr": cfprAaaTacacsPlusEpDescr,
       "cfprAaaTacacsPlusEpFsmDescr": cfprAaaTacacsPlusEpFsmDescr,
       "cfprAaaTacacsPlusEpFsmPrev": cfprAaaTacacsPlusEpFsmPrev,
       "cfprAaaTacacsPlusEpFsmProgr": cfprAaaTacacsPlusEpFsmProgr,
       "cfprAaaTacacsPlusEpFsmRmtInvErrCode": cfprAaaTacacsPlusEpFsmRmtInvErrCode,
       "cfprAaaTacacsPlusEpFsmRmtInvErrDescr": cfprAaaTacacsPlusEpFsmRmtInvErrDescr,
       "cfprAaaTacacsPlusEpFsmRmtInvRslt": cfprAaaTacacsPlusEpFsmRmtInvRslt,
       "cfprAaaTacacsPlusEpFsmStageDescr": cfprAaaTacacsPlusEpFsmStageDescr,
       "cfprAaaTacacsPlusEpFsmStamp": cfprAaaTacacsPlusEpFsmStamp,
       "cfprAaaTacacsPlusEpFsmStatus": cfprAaaTacacsPlusEpFsmStatus,
       "cfprAaaTacacsPlusEpFsmTry": cfprAaaTacacsPlusEpFsmTry,
       "cfprAaaTacacsPlusEpIntId": cfprAaaTacacsPlusEpIntId,
       "cfprAaaTacacsPlusEpName": cfprAaaTacacsPlusEpName,
       "cfprAaaTacacsPlusEpPolicyLevel": cfprAaaTacacsPlusEpPolicyLevel,
       "cfprAaaTacacsPlusEpPolicyOwner": cfprAaaTacacsPlusEpPolicyOwner,
       "cfprAaaTacacsPlusEpRetries": cfprAaaTacacsPlusEpRetries,
       "cfprAaaTacacsPlusEpTimeout": cfprAaaTacacsPlusEpTimeout,
       "cfprAaaTacacsPlusEpFsmTable": cfprAaaTacacsPlusEpFsmTable,
       "cfprAaaTacacsPlusEpFsmEntry": cfprAaaTacacsPlusEpFsmEntry,
       "cfprAaaTacacsPlusEpFsmInstanceId": cfprAaaTacacsPlusEpFsmInstanceId,
       "cfprAaaTacacsPlusEpFsmDn": cfprAaaTacacsPlusEpFsmDn,
       "cfprAaaTacacsPlusEpFsmRn": cfprAaaTacacsPlusEpFsmRn,
       "cfprAaaTacacsPlusEpFsmCompletionTime": cfprAaaTacacsPlusEpFsmCompletionTime,
       "cfprAaaTacacsPlusEpFsmCurrentFsm": cfprAaaTacacsPlusEpFsmCurrentFsm,
       "cfprAaaTacacsPlusEpFsmDescrData": cfprAaaTacacsPlusEpFsmDescrData,
       "cfprAaaTacacsPlusEpFsmFsmStatus": cfprAaaTacacsPlusEpFsmFsmStatus,
       "cfprAaaTacacsPlusEpFsmProgress": cfprAaaTacacsPlusEpFsmProgress,
       "cfprAaaTacacsPlusEpFsmRmtErrCode": cfprAaaTacacsPlusEpFsmRmtErrCode,
       "cfprAaaTacacsPlusEpFsmRmtErrDescr": cfprAaaTacacsPlusEpFsmRmtErrDescr,
       "cfprAaaTacacsPlusEpFsmRmtRslt": cfprAaaTacacsPlusEpFsmRmtRslt,
       "cfprAaaTacacsPlusEpFsmStageTable": cfprAaaTacacsPlusEpFsmStageTable,
       "cfprAaaTacacsPlusEpFsmStageEntry": cfprAaaTacacsPlusEpFsmStageEntry,
       "cfprAaaTacacsPlusEpFsmStageInstanceId": cfprAaaTacacsPlusEpFsmStageInstanceId,
       "cfprAaaTacacsPlusEpFsmStageDn": cfprAaaTacacsPlusEpFsmStageDn,
       "cfprAaaTacacsPlusEpFsmStageRn": cfprAaaTacacsPlusEpFsmStageRn,
       "cfprAaaTacacsPlusEpFsmStageDescrData": cfprAaaTacacsPlusEpFsmStageDescrData,
       "cfprAaaTacacsPlusEpFsmStageLastUpdateTime": cfprAaaTacacsPlusEpFsmStageLastUpdateTime,
       "cfprAaaTacacsPlusEpFsmStageName": cfprAaaTacacsPlusEpFsmStageName,
       "cfprAaaTacacsPlusEpFsmStageOrder": cfprAaaTacacsPlusEpFsmStageOrder,
       "cfprAaaTacacsPlusEpFsmStageRetry": cfprAaaTacacsPlusEpFsmStageRetry,
       "cfprAaaTacacsPlusEpFsmStageStageStatus": cfprAaaTacacsPlusEpFsmStageStageStatus,
       "cfprAaaTacacsPlusProviderTable": cfprAaaTacacsPlusProviderTable,
       "cfprAaaTacacsPlusProviderEntry": cfprAaaTacacsPlusProviderEntry,
       "cfprAaaTacacsPlusProviderInstanceId": cfprAaaTacacsPlusProviderInstanceId,
       "cfprAaaTacacsPlusProviderDn": cfprAaaTacacsPlusProviderDn,
       "cfprAaaTacacsPlusProviderRn": cfprAaaTacacsPlusProviderRn,
       "cfprAaaTacacsPlusProviderDescr": cfprAaaTacacsPlusProviderDescr,
       "cfprAaaTacacsPlusProviderEncKey": cfprAaaTacacsPlusProviderEncKey,
       "cfprAaaTacacsPlusProviderKey": cfprAaaTacacsPlusProviderKey,
       "cfprAaaTacacsPlusProviderKeySet": cfprAaaTacacsPlusProviderKeySet,
       "cfprAaaTacacsPlusProviderName": cfprAaaTacacsPlusProviderName,
       "cfprAaaTacacsPlusProviderOrder": cfprAaaTacacsPlusProviderOrder,
       "cfprAaaTacacsPlusProviderPort": cfprAaaTacacsPlusProviderPort,
       "cfprAaaTacacsPlusProviderRetries": cfprAaaTacacsPlusProviderRetries,
       "cfprAaaTacacsPlusProviderTimeout": cfprAaaTacacsPlusProviderTimeout,
       "cfprAaaUserTable": cfprAaaUserTable,
       "cfprAaaUserEntry": cfprAaaUserEntry,
       "cfprAaaUserInstanceId": cfprAaaUserInstanceId,
       "cfprAaaUserDn": cfprAaaUserDn,
       "cfprAaaUserRn": cfprAaaUserRn,
       "cfprAaaUserAccountStatus": cfprAaaUserAccountStatus,
       "cfprAaaUserClearPwdHistory": cfprAaaUserClearPwdHistory,
       "cfprAaaUserConfigState": cfprAaaUserConfigState,
       "cfprAaaUserConfigStatusMessage": cfprAaaUserConfigStatusMessage,
       "cfprAaaUserDescr": cfprAaaUserDescr,
       "cfprAaaUserEmail": cfprAaaUserEmail,
       "cfprAaaUserEncPwd": cfprAaaUserEncPwd,
       "cfprAaaUserEncPwdSet": cfprAaaUserEncPwdSet,
       "cfprAaaUserExpiration": cfprAaaUserExpiration,
       "cfprAaaUserExpires": cfprAaaUserExpires,
       "cfprAaaUserFirstName": cfprAaaUserFirstName,
       "cfprAaaUserLastName": cfprAaaUserLastName,
       "cfprAaaUserName": cfprAaaUserName,
       "cfprAaaUserPhone": cfprAaaUserPhone,
       "cfprAaaUserPriv": cfprAaaUserPriv,
       "cfprAaaUserPwd": cfprAaaUserPwd,
       "cfprAaaUserPwdSet": cfprAaaUserPwdSet,
       "cfprAaaUserClearLockStatus": cfprAaaUserClearLockStatus,
       "cfprAaaUserPwdExpDate": cfprAaaUserPwdExpDate,
       "cfprAaaUserPwdReset": cfprAaaUserPwdReset,
       "cfprAaaUserDataTable": cfprAaaUserDataTable,
       "cfprAaaUserDataEntry": cfprAaaUserDataEntry,
       "cfprAaaUserDataInstanceId": cfprAaaUserDataInstanceId,
       "cfprAaaUserDataDn": cfprAaaUserDataDn,
       "cfprAaaUserDataRn": cfprAaaUserDataRn,
       "cfprAaaUserDataDescr": cfprAaaUserDataDescr,
       "cfprAaaUserDataIntId": cfprAaaUserDataIntId,
       "cfprAaaUserDataName": cfprAaaUserDataName,
       "cfprAaaUserDataPolicyLevel": cfprAaaUserDataPolicyLevel,
       "cfprAaaUserDataPolicyOwner": cfprAaaUserDataPolicyOwner,
       "cfprAaaUserDataPwdChangeCount": cfprAaaUserDataPwdChangeCount,
       "cfprAaaUserDataPwdChangeIntervalBegin": cfprAaaUserDataPwdChangeIntervalBegin,
       "cfprAaaUserDataPwdChangedDate": cfprAaaUserDataPwdChangedDate,
       "cfprAaaUserDataPwdHistory": cfprAaaUserDataPwdHistory,
       "cfprAaaUserEpTable": cfprAaaUserEpTable,
       "cfprAaaUserEpEntry": cfprAaaUserEpEntry,
       "cfprAaaUserEpInstanceId": cfprAaaUserEpInstanceId,
       "cfprAaaUserEpDn": cfprAaaUserEpDn,
       "cfprAaaUserEpRn": cfprAaaUserEpRn,
       "cfprAaaUserEpDescr": cfprAaaUserEpDescr,
       "cfprAaaUserEpFsmDescr": cfprAaaUserEpFsmDescr,
       "cfprAaaUserEpFsmPrev": cfprAaaUserEpFsmPrev,
       "cfprAaaUserEpFsmProgr": cfprAaaUserEpFsmProgr,
       "cfprAaaUserEpFsmRmtInvErrCode": cfprAaaUserEpFsmRmtInvErrCode,
       "cfprAaaUserEpFsmRmtInvErrDescr": cfprAaaUserEpFsmRmtInvErrDescr,
       "cfprAaaUserEpFsmRmtInvRslt": cfprAaaUserEpFsmRmtInvRslt,
       "cfprAaaUserEpFsmStageDescr": cfprAaaUserEpFsmStageDescr,
       "cfprAaaUserEpFsmStamp": cfprAaaUserEpFsmStamp,
       "cfprAaaUserEpFsmStatus": cfprAaaUserEpFsmStatus,
       "cfprAaaUserEpFsmTry": cfprAaaUserEpFsmTry,
       "cfprAaaUserEpIntId": cfprAaaUserEpIntId,
       "cfprAaaUserEpName": cfprAaaUserEpName,
       "cfprAaaUserEpPolicyLevel": cfprAaaUserEpPolicyLevel,
       "cfprAaaUserEpPolicyOwner": cfprAaaUserEpPolicyOwner,
       "cfprAaaUserEpPwdStrengthCheck": cfprAaaUserEpPwdStrengthCheck,
       "cfprAaaUserEpMaxLoginAttempts": cfprAaaUserEpMaxLoginAttempts,
       "cfprAaaUserEpMinPwdLength": cfprAaaUserEpMinPwdLength,
       "cfprAaaUserEpUserAccountUnlockTime": cfprAaaUserEpUserAccountUnlockTime,
       "cfprAaaUserEpIsPasswordEncryptionKeySet": cfprAaaUserEpIsPasswordEncryptionKeySet,
       "cfprAaaUserEpPasswordEncryptionKey": cfprAaaUserEpPasswordEncryptionKey,
       "cfprAaaUserEpFsmTable": cfprAaaUserEpFsmTable,
       "cfprAaaUserEpFsmEntry": cfprAaaUserEpFsmEntry,
       "cfprAaaUserEpFsmInstanceId": cfprAaaUserEpFsmInstanceId,
       "cfprAaaUserEpFsmDn": cfprAaaUserEpFsmDn,
       "cfprAaaUserEpFsmRn": cfprAaaUserEpFsmRn,
       "cfprAaaUserEpFsmCompletionTime": cfprAaaUserEpFsmCompletionTime,
       "cfprAaaUserEpFsmCurrentFsm": cfprAaaUserEpFsmCurrentFsm,
       "cfprAaaUserEpFsmDescrData": cfprAaaUserEpFsmDescrData,
       "cfprAaaUserEpFsmFsmStatus": cfprAaaUserEpFsmFsmStatus,
       "cfprAaaUserEpFsmProgress": cfprAaaUserEpFsmProgress,
       "cfprAaaUserEpFsmRmtErrCode": cfprAaaUserEpFsmRmtErrCode,
       "cfprAaaUserEpFsmRmtErrDescr": cfprAaaUserEpFsmRmtErrDescr,
       "cfprAaaUserEpFsmRmtRslt": cfprAaaUserEpFsmRmtRslt,
       "cfprAaaUserEpFsmStageTable": cfprAaaUserEpFsmStageTable,
       "cfprAaaUserEpFsmStageEntry": cfprAaaUserEpFsmStageEntry,
       "cfprAaaUserEpFsmStageInstanceId": cfprAaaUserEpFsmStageInstanceId,
       "cfprAaaUserEpFsmStageDn": cfprAaaUserEpFsmStageDn,
       "cfprAaaUserEpFsmStageRn": cfprAaaUserEpFsmStageRn,
       "cfprAaaUserEpFsmStageDescrData": cfprAaaUserEpFsmStageDescrData,
       "cfprAaaUserEpFsmStageLastUpdateTime": cfprAaaUserEpFsmStageLastUpdateTime,
       "cfprAaaUserEpFsmStageName": cfprAaaUserEpFsmStageName,
       "cfprAaaUserEpFsmStageOrder": cfprAaaUserEpFsmStageOrder,
       "cfprAaaUserEpFsmStageRetry": cfprAaaUserEpFsmStageRetry,
       "cfprAaaUserEpFsmStageStageStatus": cfprAaaUserEpFsmStageStageStatus,
       "cfprAaaUserEpFsmTaskTable": cfprAaaUserEpFsmTaskTable,
       "cfprAaaUserEpFsmTaskEntry": cfprAaaUserEpFsmTaskEntry,
       "cfprAaaUserEpFsmTaskInstanceId": cfprAaaUserEpFsmTaskInstanceId,
       "cfprAaaUserEpFsmTaskDn": cfprAaaUserEpFsmTaskDn,
       "cfprAaaUserEpFsmTaskRn": cfprAaaUserEpFsmTaskRn,
       "cfprAaaUserEpFsmTaskCompletion": cfprAaaUserEpFsmTaskCompletion,
       "cfprAaaUserEpFsmTaskFlags": cfprAaaUserEpFsmTaskFlags,
       "cfprAaaUserEpFsmTaskItem": cfprAaaUserEpFsmTaskItem,
       "cfprAaaUserEpFsmTaskSeqId": cfprAaaUserEpFsmTaskSeqId,
       "cfprAaaUserLocaleTable": cfprAaaUserLocaleTable,
       "cfprAaaUserLocaleEntry": cfprAaaUserLocaleEntry,
       "cfprAaaUserLocaleInstanceId": cfprAaaUserLocaleInstanceId,
       "cfprAaaUserLocaleDn": cfprAaaUserLocaleDn,
       "cfprAaaUserLocaleRn": cfprAaaUserLocaleRn,
       "cfprAaaUserLocaleConfigState": cfprAaaUserLocaleConfigState,
       "cfprAaaUserLocaleConfigStatusMessage": cfprAaaUserLocaleConfigStatusMessage,
       "cfprAaaUserLocaleDescr": cfprAaaUserLocaleDescr,
       "cfprAaaUserLocaleName": cfprAaaUserLocaleName,
       "cfprAaaUserRoleTable": cfprAaaUserRoleTable,
       "cfprAaaUserRoleEntry": cfprAaaUserRoleEntry,
       "cfprAaaUserRoleInstanceId": cfprAaaUserRoleInstanceId,
       "cfprAaaUserRoleDn": cfprAaaUserRoleDn,
       "cfprAaaUserRoleRn": cfprAaaUserRoleRn,
       "cfprAaaUserRoleConfigState": cfprAaaUserRoleConfigState,
       "cfprAaaUserRoleConfigStatusMessage": cfprAaaUserRoleConfigStatusMessage,
       "cfprAaaUserRoleDescr": cfprAaaUserRoleDescr,
       "cfprAaaUserRoleName": cfprAaaUserRoleName,
       "cfprAaaWebLoginTable": cfprAaaWebLoginTable,
       "cfprAaaWebLoginEntry": cfprAaaWebLoginEntry,
       "cfprAaaWebLoginInstanceId": cfprAaaWebLoginInstanceId,
       "cfprAaaWebLoginDn": cfprAaaWebLoginDn,
       "cfprAaaWebLoginRn": cfprAaaWebLoginRn,
       "cfprAaaWebLoginDescr": cfprAaaWebLoginDescr,
       "cfprAaaWebLoginId": cfprAaaWebLoginId,
       "cfprAaaWebLoginIntId": cfprAaaWebLoginIntId,
       "cfprAaaWebLoginLocalHost": cfprAaaWebLoginLocalHost,
       "cfprAaaWebLoginName": cfprAaaWebLoginName,
       "cfprAaaWebLoginPolicyLevel": cfprAaaWebLoginPolicyLevel,
       "cfprAaaWebLoginPolicyOwner": cfprAaaWebLoginPolicyOwner,
       "cfprAaaWebLoginRemoteHost": cfprAaaWebLoginRemoteHost,
       "cfprAaaWebLoginSession": cfprAaaWebLoginSession,
       "cfprAaaWebLoginSwitchId": cfprAaaWebLoginSwitchId,
       "cfprAaaLoginRecTable": cfprAaaLoginRecTable,
       "cfprAaaLoginRecEntry": cfprAaaLoginRecEntry,
       "cfprAaaLoginRecInstanceId": cfprAaaLoginRecInstanceId,
       "cfprAaaLoginRecDn": cfprAaaLoginRecDn,
       "cfprAaaLoginRecRn": cfprAaaLoginRecRn,
       "cfprAaaLoginRecHost": cfprAaaLoginRecHost,
       "cfprAaaLoginRecName": cfprAaaLoginRecName,
       "cfprAaaLoginRecTime": cfprAaaLoginRecTime,
       "cfprAaaLoginRecUser": cfprAaaLoginRecUser,
       "cfprAaaRoleRecTable": cfprAaaRoleRecTable,
       "cfprAaaRoleRecEntry": cfprAaaRoleRecEntry,
       "cfprAaaRoleRecInstanceId": cfprAaaRoleRecInstanceId,
       "cfprAaaRoleRecDn": cfprAaaRoleRecDn,
       "cfprAaaRoleRecRn": cfprAaaRoleRecRn,
       "cfprAaaRoleRecCrntRole": cfprAaaRoleRecCrntRole,
       "cfprAaaRoleRecName": cfprAaaRoleRecName,
       "cfprAaaRoleRecPrevRole": cfprAaaRoleRecPrevRole,
       "cfprAaaRoleRecTime": cfprAaaRoleRecTime,
       "cfprAaaRoleRecUser": cfprAaaRoleRecUser,
       "cfprAaaUserLoginInfoTable": cfprAaaUserLoginInfoTable,
       "cfprAaaUserLoginInfoEntry": cfprAaaUserLoginInfoEntry,
       "cfprAaaUserLoginInfoInstanceId": cfprAaaUserLoginInfoInstanceId,
       "cfprAaaUserLoginInfoDn": cfprAaaUserLoginInfoDn,
       "cfprAaaUserLoginInfoRn": cfprAaaUserLoginInfoRn,
       "cfprAaaUserLoginInfoNumFailedLogin": cfprAaaUserLoginInfoNumFailedLogin,
       "cfprAaaUserLoginInfoNumSuccessLogin": cfprAaaUserLoginInfoNumSuccessLogin,
       "cfprAaaPwdUserProfileTable": cfprAaaPwdUserProfileTable,
       "cfprAaaPwdUserProfileEntry": cfprAaaPwdUserProfileEntry,
       "cfprAaaPwdUserProfileInstanceId": cfprAaaPwdUserProfileInstanceId,
       "cfprAaaPwdUserProfileDn": cfprAaaPwdUserProfileDn,
       "cfprAaaPwdUserProfileRn": cfprAaaPwdUserProfileRn,
       "cfprAaaPwdUserProfileExpirationDays": cfprAaaPwdUserProfileExpirationDays,
       "cfprAaaPwdUserProfileExpirationGracePeriod": cfprAaaPwdUserProfileExpirationGracePeriod,
       "cfprAaaPwdUserProfileExpirationWarnTime": cfprAaaPwdUserProfileExpirationWarnTime,
       "cfprAaaSsoEpTable": cfprAaaSsoEpTable,
       "cfprAaaSsoEpEntry": cfprAaaSsoEpEntry,
       "cfprAaaSsoEpInstanceId": cfprAaaSsoEpInstanceId,
       "cfprAaaSsoEpDn": cfprAaaSsoEpDn,
       "cfprAaaSsoEpRn": cfprAaaSsoEpRn,
       "cfprAaaSsoEpDescr": cfprAaaSsoEpDescr,
       "cfprAaaSsoEpFsmDescr": cfprAaaSsoEpFsmDescr,
       "cfprAaaSsoEpFsmPrev": cfprAaaSsoEpFsmPrev,
       "cfprAaaSsoEpFsmProgr": cfprAaaSsoEpFsmProgr,
       "cfprAaaSsoEpFsmRmtInvErrCode": cfprAaaSsoEpFsmRmtInvErrCode,
       "cfprAaaSsoEpFsmRmtInvErrDescr": cfprAaaSsoEpFsmRmtInvErrDescr,
       "cfprAaaSsoEpFsmRmtInvRslt": cfprAaaSsoEpFsmRmtInvRslt,
       "cfprAaaSsoEpFsmStageDescr": cfprAaaSsoEpFsmStageDescr,
       "cfprAaaSsoEpFsmStamp": cfprAaaSsoEpFsmStamp,
       "cfprAaaSsoEpFsmStatus": cfprAaaSsoEpFsmStatus,
       "cfprAaaSsoEpFsmTry": cfprAaaSsoEpFsmTry,
       "cfprAaaSsoEpIntId": cfprAaaSsoEpIntId,
       "cfprAaaSsoEpName": cfprAaaSsoEpName,
       "cfprAaaSsoEpPolicyLevel": cfprAaaSsoEpPolicyLevel,
       "cfprAaaSsoEpPolicyOwner": cfprAaaSsoEpPolicyOwner,
       "cfprAaaSsoEpRetries": cfprAaaSsoEpRetries,
       "cfprAaaSsoEpSsoEnabled": cfprAaaSsoEpSsoEnabled,
       "cfprAaaSsoEpTimeout": cfprAaaSsoEpTimeout,
       "cfprAaaSsoEpFsmTable": cfprAaaSsoEpFsmTable,
       "cfprAaaSsoEpFsmEntry": cfprAaaSsoEpFsmEntry,
       "cfprAaaSsoEpFsmInstanceId": cfprAaaSsoEpFsmInstanceId,
       "cfprAaaSsoEpFsmDn": cfprAaaSsoEpFsmDn,
       "cfprAaaSsoEpFsmRn": cfprAaaSsoEpFsmRn,
       "cfprAaaSsoEpFsmCompletionTime": cfprAaaSsoEpFsmCompletionTime,
       "cfprAaaSsoEpFsmCurrentFsm": cfprAaaSsoEpFsmCurrentFsm,
       "cfprAaaSsoEpFsmDescrData": cfprAaaSsoEpFsmDescrData,
       "cfprAaaSsoEpFsmFsmStatus": cfprAaaSsoEpFsmFsmStatus,
       "cfprAaaSsoEpFsmProgress": cfprAaaSsoEpFsmProgress,
       "cfprAaaSsoEpFsmRmtErrCode": cfprAaaSsoEpFsmRmtErrCode,
       "cfprAaaSsoEpFsmRmtErrDescr": cfprAaaSsoEpFsmRmtErrDescr,
       "cfprAaaSsoEpFsmRmtRslt": cfprAaaSsoEpFsmRmtRslt,
       "cfprAaaSsoEpFsmStageTable": cfprAaaSsoEpFsmStageTable,
       "cfprAaaSsoEpFsmStageEntry": cfprAaaSsoEpFsmStageEntry,
       "cfprAaaSsoEpFsmStageInstanceId": cfprAaaSsoEpFsmStageInstanceId,
       "cfprAaaSsoEpFsmStageDn": cfprAaaSsoEpFsmStageDn,
       "cfprAaaSsoEpFsmStageRn": cfprAaaSsoEpFsmStageRn,
       "cfprAaaSsoEpFsmStageDescrData": cfprAaaSsoEpFsmStageDescrData,
       "cfprAaaSsoEpFsmStageLastUpdateTime": cfprAaaSsoEpFsmStageLastUpdateTime,
       "cfprAaaSsoEpFsmStageName": cfprAaaSsoEpFsmStageName,
       "cfprAaaSsoEpFsmStageOrder": cfprAaaSsoEpFsmStageOrder,
       "cfprAaaSsoEpFsmStageRetry": cfprAaaSsoEpFsmStageRetry,
       "cfprAaaSsoEpFsmStageStageStatus": cfprAaaSsoEpFsmStageStageStatus,
       "cfprAaaSsoProviderTable": cfprAaaSsoProviderTable,
       "cfprAaaSsoProviderEntry": cfprAaaSsoProviderEntry,
       "cfprAaaSsoProviderInstanceId": cfprAaaSsoProviderInstanceId,
       "cfprAaaSsoProviderDn": cfprAaaSsoProviderDn,
       "cfprAaaSsoProviderRn": cfprAaaSsoProviderRn,
       "cfprAaaSsoProviderDescr": cfprAaaSsoProviderDescr,
       "cfprAaaSsoProviderEncKey": cfprAaaSsoProviderEncKey,
       "cfprAaaSsoProviderIdpCert": cfprAaaSsoProviderIdpCert,
       "cfprAaaSsoProviderIdpIssuerUrl": cfprAaaSsoProviderIdpIssuerUrl,
       "cfprAaaSsoProviderIdpSsoUrl": cfprAaaSsoProviderIdpSsoUrl,
       "cfprAaaSsoProviderIdpXmlData": cfprAaaSsoProviderIdpXmlData,
       "cfprAaaSsoProviderKey": cfprAaaSsoProviderKey,
       "cfprAaaSsoProviderKeySet": cfprAaaSsoProviderKeySet,
       "cfprAaaSsoProviderName": cfprAaaSsoProviderName,
       "cfprAaaSsoProviderOrder": cfprAaaSsoProviderOrder,
       "cfprAaaSsoProviderRetries": cfprAaaSsoProviderRetries,
       "cfprAaaSsoProviderTimeout": cfprAaaSsoProviderTimeout,
       "cfprAaaUserOldPwdTable": cfprAaaUserOldPwdTable,
       "cfprAaaUserOldPwdEntry": cfprAaaUserOldPwdEntry,
       "cfprAaaUserOldPwdInstanceId": cfprAaaUserOldPwdInstanceId,
       "cfprAaaUserOldPwdDn": cfprAaaUserOldPwdDn,
       "cfprAaaUserOldPwdRn": cfprAaaUserOldPwdRn,
       "cfprAaaUserOldPwdDescr": cfprAaaUserOldPwdDescr,
       "cfprAaaUserOldPwdEncPwd": cfprAaaUserOldPwdEncPwd,
       "cfprAaaUserOldPwdIntId": cfprAaaUserOldPwdIntId,
       "cfprAaaUserOldPwdName": cfprAaaUserOldPwdName,
       "cfprAaaUserOldPwdPolicyLevel": cfprAaaUserOldPwdPolicyLevel,
       "cfprAaaUserOldPwdPolicyOwner": cfprAaaUserOldPwdPolicyOwner,
       "cfprAaaUserOldPwdPwdEndDate": cfprAaaUserOldPwdPwdEndDate}
)
