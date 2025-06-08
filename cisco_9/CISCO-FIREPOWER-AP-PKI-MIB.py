# SNMP MIB module (CISCO-FIREPOWER-AP-PKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-PKI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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
 CfprApConditionRemoteInvRslt,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApPkiCertStatus,
 CfprApPkiEpFsmCurrentFsm,
 CfprApPkiEpFsmStageName,
 CfprApPkiEpFsmTaskItem,
 CfprApPkiKeyringState,
 CfprApPkiModulus,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAaaConfigState",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApPkiCertStatus",
    "CfprApPkiEpFsmCurrentFsm",
    "CfprApPkiEpFsmStageName",
    "CfprApPkiEpFsmTaskItem",
    "CfprApPkiKeyringState",
    "CfprApPkiModulus",
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

cfprApPkiObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApPkiCertReqTable_Object = MibTable
cfprApPkiCertReqTable = _CfprApPkiCertReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1)
)
if mibBuilder.loadTexts:
    cfprApPkiCertReqTable.setStatus("current")
_CfprApPkiCertReqEntry_Object = MibTableRow
cfprApPkiCertReqEntry = _CfprApPkiCertReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1)
)
cfprApPkiCertReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiCertReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiCertReqEntry.setStatus("current")
_CfprApPkiCertReqInstanceId_Type = CfprApManagedObjectId
_CfprApPkiCertReqInstanceId_Object = MibTableColumn
cfprApPkiCertReqInstanceId = _CfprApPkiCertReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 1),
    _CfprApPkiCertReqInstanceId_Type()
)
cfprApPkiCertReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiCertReqInstanceId.setStatus("current")
_CfprApPkiCertReqDn_Type = CfprApManagedObjectDn
_CfprApPkiCertReqDn_Object = MibTableColumn
cfprApPkiCertReqDn = _CfprApPkiCertReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 2),
    _CfprApPkiCertReqDn_Type()
)
cfprApPkiCertReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqDn.setStatus("current")
_CfprApPkiCertReqRn_Type = SnmpAdminString
_CfprApPkiCertReqRn_Object = MibTableColumn
cfprApPkiCertReqRn = _CfprApPkiCertReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 3),
    _CfprApPkiCertReqRn_Type()
)
cfprApPkiCertReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqRn.setStatus("current")
_CfprApPkiCertReqCountry_Type = SnmpAdminString
_CfprApPkiCertReqCountry_Object = MibTableColumn
cfprApPkiCertReqCountry = _CfprApPkiCertReqCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 4),
    _CfprApPkiCertReqCountry_Type()
)
cfprApPkiCertReqCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqCountry.setStatus("current")
_CfprApPkiCertReqDns_Type = SnmpAdminString
_CfprApPkiCertReqDns_Object = MibTableColumn
cfprApPkiCertReqDns = _CfprApPkiCertReqDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 5),
    _CfprApPkiCertReqDns_Type()
)
cfprApPkiCertReqDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqDns.setStatus("current")
_CfprApPkiCertReqEmail_Type = SnmpAdminString
_CfprApPkiCertReqEmail_Object = MibTableColumn
cfprApPkiCertReqEmail = _CfprApPkiCertReqEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 6),
    _CfprApPkiCertReqEmail_Type()
)
cfprApPkiCertReqEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqEmail.setStatus("current")
_CfprApPkiCertReqIp_Type = InetAddressIPv4
_CfprApPkiCertReqIp_Object = MibTableColumn
cfprApPkiCertReqIp = _CfprApPkiCertReqIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 7),
    _CfprApPkiCertReqIp_Type()
)
cfprApPkiCertReqIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqIp.setStatus("current")
_CfprApPkiCertReqIpA_Type = InetAddressIPv4
_CfprApPkiCertReqIpA_Object = MibTableColumn
cfprApPkiCertReqIpA = _CfprApPkiCertReqIpA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 8),
    _CfprApPkiCertReqIpA_Type()
)
cfprApPkiCertReqIpA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqIpA.setStatus("current")
_CfprApPkiCertReqIpB_Type = InetAddressIPv4
_CfprApPkiCertReqIpB_Object = MibTableColumn
cfprApPkiCertReqIpB = _CfprApPkiCertReqIpB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 9),
    _CfprApPkiCertReqIpB_Type()
)
cfprApPkiCertReqIpB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqIpB.setStatus("current")
_CfprApPkiCertReqIpv6_Type = InetAddressIPv6
_CfprApPkiCertReqIpv6_Object = MibTableColumn
cfprApPkiCertReqIpv6 = _CfprApPkiCertReqIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 10),
    _CfprApPkiCertReqIpv6_Type()
)
cfprApPkiCertReqIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqIpv6.setStatus("current")
_CfprApPkiCertReqIpv6A_Type = InetAddressIPv6
_CfprApPkiCertReqIpv6A_Object = MibTableColumn
cfprApPkiCertReqIpv6A = _CfprApPkiCertReqIpv6A_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 11),
    _CfprApPkiCertReqIpv6A_Type()
)
cfprApPkiCertReqIpv6A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqIpv6A.setStatus("current")
_CfprApPkiCertReqIpv6B_Type = InetAddressIPv6
_CfprApPkiCertReqIpv6B_Object = MibTableColumn
cfprApPkiCertReqIpv6B = _CfprApPkiCertReqIpv6B_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 12),
    _CfprApPkiCertReqIpv6B_Type()
)
cfprApPkiCertReqIpv6B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqIpv6B.setStatus("current")
_CfprApPkiCertReqLocality_Type = SnmpAdminString
_CfprApPkiCertReqLocality_Object = MibTableColumn
cfprApPkiCertReqLocality = _CfprApPkiCertReqLocality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 13),
    _CfprApPkiCertReqLocality_Type()
)
cfprApPkiCertReqLocality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqLocality.setStatus("current")
_CfprApPkiCertReqOrgName_Type = SnmpAdminString
_CfprApPkiCertReqOrgName_Object = MibTableColumn
cfprApPkiCertReqOrgName = _CfprApPkiCertReqOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 14),
    _CfprApPkiCertReqOrgName_Type()
)
cfprApPkiCertReqOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqOrgName.setStatus("current")
_CfprApPkiCertReqOrgUnitName_Type = SnmpAdminString
_CfprApPkiCertReqOrgUnitName_Object = MibTableColumn
cfprApPkiCertReqOrgUnitName = _CfprApPkiCertReqOrgUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 15),
    _CfprApPkiCertReqOrgUnitName_Type()
)
cfprApPkiCertReqOrgUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqOrgUnitName.setStatus("current")
_CfprApPkiCertReqPwd_Type = SnmpAdminString
_CfprApPkiCertReqPwd_Object = MibTableColumn
cfprApPkiCertReqPwd = _CfprApPkiCertReqPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 16),
    _CfprApPkiCertReqPwd_Type()
)
cfprApPkiCertReqPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqPwd.setStatus("current")
_CfprApPkiCertReqReq_Type = SnmpAdminString
_CfprApPkiCertReqReq_Object = MibTableColumn
cfprApPkiCertReqReq = _CfprApPkiCertReqReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 17),
    _CfprApPkiCertReqReq_Type()
)
cfprApPkiCertReqReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqReq.setStatus("current")
_CfprApPkiCertReqState_Type = SnmpAdminString
_CfprApPkiCertReqState_Object = MibTableColumn
cfprApPkiCertReqState = _CfprApPkiCertReqState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 18),
    _CfprApPkiCertReqState_Type()
)
cfprApPkiCertReqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqState.setStatus("current")
_CfprApPkiCertReqSubjName_Type = SnmpAdminString
_CfprApPkiCertReqSubjName_Object = MibTableColumn
cfprApPkiCertReqSubjName = _CfprApPkiCertReqSubjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 1, 1, 19),
    _CfprApPkiCertReqSubjName_Type()
)
cfprApPkiCertReqSubjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiCertReqSubjName.setStatus("current")
_CfprApPkiEpTable_Object = MibTable
cfprApPkiEpTable = _CfprApPkiEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2)
)
if mibBuilder.loadTexts:
    cfprApPkiEpTable.setStatus("current")
_CfprApPkiEpEntry_Object = MibTableRow
cfprApPkiEpEntry = _CfprApPkiEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1)
)
cfprApPkiEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiEpEntry.setStatus("current")
_CfprApPkiEpInstanceId_Type = CfprApManagedObjectId
_CfprApPkiEpInstanceId_Object = MibTableColumn
cfprApPkiEpInstanceId = _CfprApPkiEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 1),
    _CfprApPkiEpInstanceId_Type()
)
cfprApPkiEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiEpInstanceId.setStatus("current")
_CfprApPkiEpDn_Type = CfprApManagedObjectDn
_CfprApPkiEpDn_Object = MibTableColumn
cfprApPkiEpDn = _CfprApPkiEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 2),
    _CfprApPkiEpDn_Type()
)
cfprApPkiEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpDn.setStatus("current")
_CfprApPkiEpRn_Type = SnmpAdminString
_CfprApPkiEpRn_Object = MibTableColumn
cfprApPkiEpRn = _CfprApPkiEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 3),
    _CfprApPkiEpRn_Type()
)
cfprApPkiEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpRn.setStatus("current")
_CfprApPkiEpDescr_Type = SnmpAdminString
_CfprApPkiEpDescr_Object = MibTableColumn
cfprApPkiEpDescr = _CfprApPkiEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 4),
    _CfprApPkiEpDescr_Type()
)
cfprApPkiEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpDescr.setStatus("current")
_CfprApPkiEpFsmDescr_Type = SnmpAdminString
_CfprApPkiEpFsmDescr_Object = MibTableColumn
cfprApPkiEpFsmDescr = _CfprApPkiEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 5),
    _CfprApPkiEpFsmDescr_Type()
)
cfprApPkiEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmDescr.setStatus("current")
_CfprApPkiEpFsmPrev_Type = SnmpAdminString
_CfprApPkiEpFsmPrev_Object = MibTableColumn
cfprApPkiEpFsmPrev = _CfprApPkiEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 6),
    _CfprApPkiEpFsmPrev_Type()
)
cfprApPkiEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmPrev.setStatus("current")
_CfprApPkiEpFsmProgr_Type = Gauge32
_CfprApPkiEpFsmProgr_Object = MibTableColumn
cfprApPkiEpFsmProgr = _CfprApPkiEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 7),
    _CfprApPkiEpFsmProgr_Type()
)
cfprApPkiEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmProgr.setStatus("current")
_CfprApPkiEpFsmRmtInvErrCode_Type = Gauge32
_CfprApPkiEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApPkiEpFsmRmtInvErrCode = _CfprApPkiEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 8),
    _CfprApPkiEpFsmRmtInvErrCode_Type()
)
cfprApPkiEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRmtInvErrCode.setStatus("current")
_CfprApPkiEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApPkiEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApPkiEpFsmRmtInvErrDescr = _CfprApPkiEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 9),
    _CfprApPkiEpFsmRmtInvErrDescr_Type()
)
cfprApPkiEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRmtInvErrDescr.setStatus("current")
_CfprApPkiEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPkiEpFsmRmtInvRslt_Object = MibTableColumn
cfprApPkiEpFsmRmtInvRslt = _CfprApPkiEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 10),
    _CfprApPkiEpFsmRmtInvRslt_Type()
)
cfprApPkiEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRmtInvRslt.setStatus("current")
_CfprApPkiEpFsmStageDescr_Type = SnmpAdminString
_CfprApPkiEpFsmStageDescr_Object = MibTableColumn
cfprApPkiEpFsmStageDescr = _CfprApPkiEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 11),
    _CfprApPkiEpFsmStageDescr_Type()
)
cfprApPkiEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageDescr.setStatus("current")
_CfprApPkiEpFsmStamp_Type = DateAndTime
_CfprApPkiEpFsmStamp_Object = MibTableColumn
cfprApPkiEpFsmStamp = _CfprApPkiEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 12),
    _CfprApPkiEpFsmStamp_Type()
)
cfprApPkiEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStamp.setStatus("current")
_CfprApPkiEpFsmStatus_Type = SnmpAdminString
_CfprApPkiEpFsmStatus_Object = MibTableColumn
cfprApPkiEpFsmStatus = _CfprApPkiEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 13),
    _CfprApPkiEpFsmStatus_Type()
)
cfprApPkiEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStatus.setStatus("current")
_CfprApPkiEpFsmTry_Type = Gauge32
_CfprApPkiEpFsmTry_Object = MibTableColumn
cfprApPkiEpFsmTry = _CfprApPkiEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 14),
    _CfprApPkiEpFsmTry_Type()
)
cfprApPkiEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTry.setStatus("current")
_CfprApPkiEpIntId_Type = SnmpAdminString
_CfprApPkiEpIntId_Object = MibTableColumn
cfprApPkiEpIntId = _CfprApPkiEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 15),
    _CfprApPkiEpIntId_Type()
)
cfprApPkiEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpIntId.setStatus("current")
_CfprApPkiEpName_Type = SnmpAdminString
_CfprApPkiEpName_Object = MibTableColumn
cfprApPkiEpName = _CfprApPkiEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 16),
    _CfprApPkiEpName_Type()
)
cfprApPkiEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpName.setStatus("current")
_CfprApPkiEpPolicyLevel_Type = Gauge32
_CfprApPkiEpPolicyLevel_Object = MibTableColumn
cfprApPkiEpPolicyLevel = _CfprApPkiEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 17),
    _CfprApPkiEpPolicyLevel_Type()
)
cfprApPkiEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpPolicyLevel.setStatus("current")
_CfprApPkiEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPkiEpPolicyOwner_Object = MibTableColumn
cfprApPkiEpPolicyOwner = _CfprApPkiEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 2, 1, 18),
    _CfprApPkiEpPolicyOwner_Type()
)
cfprApPkiEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpPolicyOwner.setStatus("current")
_CfprApPkiEpFsmTable_Object = MibTable
cfprApPkiEpFsmTable = _CfprApPkiEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3)
)
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTable.setStatus("current")
_CfprApPkiEpFsmEntry_Object = MibTableRow
cfprApPkiEpFsmEntry = _CfprApPkiEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1)
)
cfprApPkiEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiEpFsmEntry.setStatus("current")
_CfprApPkiEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApPkiEpFsmInstanceId_Object = MibTableColumn
cfprApPkiEpFsmInstanceId = _CfprApPkiEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 1),
    _CfprApPkiEpFsmInstanceId_Type()
)
cfprApPkiEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmInstanceId.setStatus("current")
_CfprApPkiEpFsmDn_Type = CfprApManagedObjectDn
_CfprApPkiEpFsmDn_Object = MibTableColumn
cfprApPkiEpFsmDn = _CfprApPkiEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 2),
    _CfprApPkiEpFsmDn_Type()
)
cfprApPkiEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmDn.setStatus("current")
_CfprApPkiEpFsmRn_Type = SnmpAdminString
_CfprApPkiEpFsmRn_Object = MibTableColumn
cfprApPkiEpFsmRn = _CfprApPkiEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 3),
    _CfprApPkiEpFsmRn_Type()
)
cfprApPkiEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRn.setStatus("current")
_CfprApPkiEpFsmCompletionTime_Type = DateAndTime
_CfprApPkiEpFsmCompletionTime_Object = MibTableColumn
cfprApPkiEpFsmCompletionTime = _CfprApPkiEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 4),
    _CfprApPkiEpFsmCompletionTime_Type()
)
cfprApPkiEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmCompletionTime.setStatus("current")
_CfprApPkiEpFsmCurrentFsm_Type = CfprApPkiEpFsmCurrentFsm
_CfprApPkiEpFsmCurrentFsm_Object = MibTableColumn
cfprApPkiEpFsmCurrentFsm = _CfprApPkiEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 5),
    _CfprApPkiEpFsmCurrentFsm_Type()
)
cfprApPkiEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmCurrentFsm.setStatus("current")
_CfprApPkiEpFsmDescrData_Type = SnmpAdminString
_CfprApPkiEpFsmDescrData_Object = MibTableColumn
cfprApPkiEpFsmDescrData = _CfprApPkiEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 6),
    _CfprApPkiEpFsmDescrData_Type()
)
cfprApPkiEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmDescrData.setStatus("current")
_CfprApPkiEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApPkiEpFsmFsmStatus_Object = MibTableColumn
cfprApPkiEpFsmFsmStatus = _CfprApPkiEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 7),
    _CfprApPkiEpFsmFsmStatus_Type()
)
cfprApPkiEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmFsmStatus.setStatus("current")
_CfprApPkiEpFsmProgress_Type = Gauge32
_CfprApPkiEpFsmProgress_Object = MibTableColumn
cfprApPkiEpFsmProgress = _CfprApPkiEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 8),
    _CfprApPkiEpFsmProgress_Type()
)
cfprApPkiEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmProgress.setStatus("current")
_CfprApPkiEpFsmRmtErrCode_Type = Gauge32
_CfprApPkiEpFsmRmtErrCode_Object = MibTableColumn
cfprApPkiEpFsmRmtErrCode = _CfprApPkiEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 9),
    _CfprApPkiEpFsmRmtErrCode_Type()
)
cfprApPkiEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRmtErrCode.setStatus("current")
_CfprApPkiEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApPkiEpFsmRmtErrDescr_Object = MibTableColumn
cfprApPkiEpFsmRmtErrDescr = _CfprApPkiEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 10),
    _CfprApPkiEpFsmRmtErrDescr_Type()
)
cfprApPkiEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRmtErrDescr.setStatus("current")
_CfprApPkiEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPkiEpFsmRmtRslt_Object = MibTableColumn
cfprApPkiEpFsmRmtRslt = _CfprApPkiEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 3, 1, 11),
    _CfprApPkiEpFsmRmtRslt_Type()
)
cfprApPkiEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmRmtRslt.setStatus("current")
_CfprApPkiEpFsmStageTable_Object = MibTable
cfprApPkiEpFsmStageTable = _CfprApPkiEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4)
)
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageTable.setStatus("current")
_CfprApPkiEpFsmStageEntry_Object = MibTableRow
cfprApPkiEpFsmStageEntry = _CfprApPkiEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1)
)
cfprApPkiEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageEntry.setStatus("current")
_CfprApPkiEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApPkiEpFsmStageInstanceId_Object = MibTableColumn
cfprApPkiEpFsmStageInstanceId = _CfprApPkiEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 1),
    _CfprApPkiEpFsmStageInstanceId_Type()
)
cfprApPkiEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageInstanceId.setStatus("current")
_CfprApPkiEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApPkiEpFsmStageDn_Object = MibTableColumn
cfprApPkiEpFsmStageDn = _CfprApPkiEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 2),
    _CfprApPkiEpFsmStageDn_Type()
)
cfprApPkiEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageDn.setStatus("current")
_CfprApPkiEpFsmStageRn_Type = SnmpAdminString
_CfprApPkiEpFsmStageRn_Object = MibTableColumn
cfprApPkiEpFsmStageRn = _CfprApPkiEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 3),
    _CfprApPkiEpFsmStageRn_Type()
)
cfprApPkiEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageRn.setStatus("current")
_CfprApPkiEpFsmStageDescrData_Type = SnmpAdminString
_CfprApPkiEpFsmStageDescrData_Object = MibTableColumn
cfprApPkiEpFsmStageDescrData = _CfprApPkiEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 4),
    _CfprApPkiEpFsmStageDescrData_Type()
)
cfprApPkiEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageDescrData.setStatus("current")
_CfprApPkiEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApPkiEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApPkiEpFsmStageLastUpdateTime = _CfprApPkiEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 5),
    _CfprApPkiEpFsmStageLastUpdateTime_Type()
)
cfprApPkiEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageLastUpdateTime.setStatus("current")
_CfprApPkiEpFsmStageName_Type = CfprApPkiEpFsmStageName
_CfprApPkiEpFsmStageName_Object = MibTableColumn
cfprApPkiEpFsmStageName = _CfprApPkiEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 6),
    _CfprApPkiEpFsmStageName_Type()
)
cfprApPkiEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageName.setStatus("current")
_CfprApPkiEpFsmStageOrder_Type = Gauge32
_CfprApPkiEpFsmStageOrder_Object = MibTableColumn
cfprApPkiEpFsmStageOrder = _CfprApPkiEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 7),
    _CfprApPkiEpFsmStageOrder_Type()
)
cfprApPkiEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageOrder.setStatus("current")
_CfprApPkiEpFsmStageRetry_Type = Gauge32
_CfprApPkiEpFsmStageRetry_Object = MibTableColumn
cfprApPkiEpFsmStageRetry = _CfprApPkiEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 8),
    _CfprApPkiEpFsmStageRetry_Type()
)
cfprApPkiEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageRetry.setStatus("current")
_CfprApPkiEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApPkiEpFsmStageStageStatus_Object = MibTableColumn
cfprApPkiEpFsmStageStageStatus = _CfprApPkiEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 4, 1, 9),
    _CfprApPkiEpFsmStageStageStatus_Type()
)
cfprApPkiEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmStageStageStatus.setStatus("current")
_CfprApPkiEpFsmTaskTable_Object = MibTable
cfprApPkiEpFsmTaskTable = _CfprApPkiEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5)
)
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskTable.setStatus("current")
_CfprApPkiEpFsmTaskEntry_Object = MibTableRow
cfprApPkiEpFsmTaskEntry = _CfprApPkiEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1)
)
cfprApPkiEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskEntry.setStatus("current")
_CfprApPkiEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApPkiEpFsmTaskInstanceId_Object = MibTableColumn
cfprApPkiEpFsmTaskInstanceId = _CfprApPkiEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 1),
    _CfprApPkiEpFsmTaskInstanceId_Type()
)
cfprApPkiEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskInstanceId.setStatus("current")
_CfprApPkiEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApPkiEpFsmTaskDn_Object = MibTableColumn
cfprApPkiEpFsmTaskDn = _CfprApPkiEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 2),
    _CfprApPkiEpFsmTaskDn_Type()
)
cfprApPkiEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskDn.setStatus("current")
_CfprApPkiEpFsmTaskRn_Type = SnmpAdminString
_CfprApPkiEpFsmTaskRn_Object = MibTableColumn
cfprApPkiEpFsmTaskRn = _CfprApPkiEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 3),
    _CfprApPkiEpFsmTaskRn_Type()
)
cfprApPkiEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskRn.setStatus("current")
_CfprApPkiEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApPkiEpFsmTaskCompletion_Object = MibTableColumn
cfprApPkiEpFsmTaskCompletion = _CfprApPkiEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 4),
    _CfprApPkiEpFsmTaskCompletion_Type()
)
cfprApPkiEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskCompletion.setStatus("current")
_CfprApPkiEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApPkiEpFsmTaskFlags_Object = MibTableColumn
cfprApPkiEpFsmTaskFlags = _CfprApPkiEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 5),
    _CfprApPkiEpFsmTaskFlags_Type()
)
cfprApPkiEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskFlags.setStatus("current")
_CfprApPkiEpFsmTaskItem_Type = CfprApPkiEpFsmTaskItem
_CfprApPkiEpFsmTaskItem_Object = MibTableColumn
cfprApPkiEpFsmTaskItem = _CfprApPkiEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 6),
    _CfprApPkiEpFsmTaskItem_Type()
)
cfprApPkiEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskItem.setStatus("current")
_CfprApPkiEpFsmTaskSeqId_Type = Gauge32
_CfprApPkiEpFsmTaskSeqId_Object = MibTableColumn
cfprApPkiEpFsmTaskSeqId = _CfprApPkiEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 5, 1, 7),
    _CfprApPkiEpFsmTaskSeqId_Type()
)
cfprApPkiEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiEpFsmTaskSeqId.setStatus("current")
_CfprApPkiKeyRingTable_Object = MibTable
cfprApPkiKeyRingTable = _CfprApPkiKeyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6)
)
if mibBuilder.loadTexts:
    cfprApPkiKeyRingTable.setStatus("current")
_CfprApPkiKeyRingEntry_Object = MibTableRow
cfprApPkiKeyRingEntry = _CfprApPkiKeyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1)
)
cfprApPkiKeyRingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiKeyRingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiKeyRingEntry.setStatus("current")
_CfprApPkiKeyRingInstanceId_Type = CfprApManagedObjectId
_CfprApPkiKeyRingInstanceId_Object = MibTableColumn
cfprApPkiKeyRingInstanceId = _CfprApPkiKeyRingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 1),
    _CfprApPkiKeyRingInstanceId_Type()
)
cfprApPkiKeyRingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingInstanceId.setStatus("current")
_CfprApPkiKeyRingDn_Type = CfprApManagedObjectDn
_CfprApPkiKeyRingDn_Object = MibTableColumn
cfprApPkiKeyRingDn = _CfprApPkiKeyRingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 2),
    _CfprApPkiKeyRingDn_Type()
)
cfprApPkiKeyRingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingDn.setStatus("current")
_CfprApPkiKeyRingRn_Type = SnmpAdminString
_CfprApPkiKeyRingRn_Object = MibTableColumn
cfprApPkiKeyRingRn = _CfprApPkiKeyRingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 3),
    _CfprApPkiKeyRingRn_Type()
)
cfprApPkiKeyRingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingRn.setStatus("current")
_CfprApPkiKeyRingAdminState_Type = CfprApPkiKeyringState
_CfprApPkiKeyRingAdminState_Object = MibTableColumn
cfprApPkiKeyRingAdminState = _CfprApPkiKeyRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 4),
    _CfprApPkiKeyRingAdminState_Type()
)
cfprApPkiKeyRingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingAdminState.setStatus("current")
_CfprApPkiKeyRingCert_Type = SnmpAdminString
_CfprApPkiKeyRingCert_Object = MibTableColumn
cfprApPkiKeyRingCert = _CfprApPkiKeyRingCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 5),
    _CfprApPkiKeyRingCert_Type()
)
cfprApPkiKeyRingCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingCert.setStatus("current")
_CfprApPkiKeyRingCertStatus_Type = CfprApPkiCertStatus
_CfprApPkiKeyRingCertStatus_Object = MibTableColumn
cfprApPkiKeyRingCertStatus = _CfprApPkiKeyRingCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 6),
    _CfprApPkiKeyRingCertStatus_Type()
)
cfprApPkiKeyRingCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingCertStatus.setStatus("current")
_CfprApPkiKeyRingConfigState_Type = CfprApAaaConfigState
_CfprApPkiKeyRingConfigState_Object = MibTableColumn
cfprApPkiKeyRingConfigState = _CfprApPkiKeyRingConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 7),
    _CfprApPkiKeyRingConfigState_Type()
)
cfprApPkiKeyRingConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingConfigState.setStatus("current")
_CfprApPkiKeyRingConfigStatusMessage_Type = SnmpAdminString
_CfprApPkiKeyRingConfigStatusMessage_Object = MibTableColumn
cfprApPkiKeyRingConfigStatusMessage = _CfprApPkiKeyRingConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 8),
    _CfprApPkiKeyRingConfigStatusMessage_Type()
)
cfprApPkiKeyRingConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingConfigStatusMessage.setStatus("current")
_CfprApPkiKeyRingDescr_Type = SnmpAdminString
_CfprApPkiKeyRingDescr_Object = MibTableColumn
cfprApPkiKeyRingDescr = _CfprApPkiKeyRingDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 9),
    _CfprApPkiKeyRingDescr_Type()
)
cfprApPkiKeyRingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingDescr.setStatus("current")
_CfprApPkiKeyRingIntId_Type = SnmpAdminString
_CfprApPkiKeyRingIntId_Object = MibTableColumn
cfprApPkiKeyRingIntId = _CfprApPkiKeyRingIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 10),
    _CfprApPkiKeyRingIntId_Type()
)
cfprApPkiKeyRingIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingIntId.setStatus("current")
_CfprApPkiKeyRingKey_Type = SnmpAdminString
_CfprApPkiKeyRingKey_Object = MibTableColumn
cfprApPkiKeyRingKey = _CfprApPkiKeyRingKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 11),
    _CfprApPkiKeyRingKey_Type()
)
cfprApPkiKeyRingKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingKey.setStatus("current")
_CfprApPkiKeyRingModulus_Type = CfprApPkiModulus
_CfprApPkiKeyRingModulus_Object = MibTableColumn
cfprApPkiKeyRingModulus = _CfprApPkiKeyRingModulus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 12),
    _CfprApPkiKeyRingModulus_Type()
)
cfprApPkiKeyRingModulus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingModulus.setStatus("current")
_CfprApPkiKeyRingName_Type = SnmpAdminString
_CfprApPkiKeyRingName_Object = MibTableColumn
cfprApPkiKeyRingName = _CfprApPkiKeyRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 13),
    _CfprApPkiKeyRingName_Type()
)
cfprApPkiKeyRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingName.setStatus("current")
_CfprApPkiKeyRingPolicyLevel_Type = Gauge32
_CfprApPkiKeyRingPolicyLevel_Object = MibTableColumn
cfprApPkiKeyRingPolicyLevel = _CfprApPkiKeyRingPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 14),
    _CfprApPkiKeyRingPolicyLevel_Type()
)
cfprApPkiKeyRingPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingPolicyLevel.setStatus("current")
_CfprApPkiKeyRingPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPkiKeyRingPolicyOwner_Object = MibTableColumn
cfprApPkiKeyRingPolicyOwner = _CfprApPkiKeyRingPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 15),
    _CfprApPkiKeyRingPolicyOwner_Type()
)
cfprApPkiKeyRingPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingPolicyOwner.setStatus("current")
_CfprApPkiKeyRingRegen_Type = TruthValue
_CfprApPkiKeyRingRegen_Object = MibTableColumn
cfprApPkiKeyRingRegen = _CfprApPkiKeyRingRegen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 16),
    _CfprApPkiKeyRingRegen_Type()
)
cfprApPkiKeyRingRegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingRegen.setStatus("current")
_CfprApPkiKeyRingTp_Type = SnmpAdminString
_CfprApPkiKeyRingTp_Object = MibTableColumn
cfprApPkiKeyRingTp = _CfprApPkiKeyRingTp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 6, 1, 17),
    _CfprApPkiKeyRingTp_Type()
)
cfprApPkiKeyRingTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiKeyRingTp.setStatus("current")
_CfprApPkiTPTable_Object = MibTable
cfprApPkiTPTable = _CfprApPkiTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7)
)
if mibBuilder.loadTexts:
    cfprApPkiTPTable.setStatus("current")
_CfprApPkiTPEntry_Object = MibTableRow
cfprApPkiTPEntry = _CfprApPkiTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1)
)
cfprApPkiTPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-PKI-MIB", "cfprApPkiTPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPkiTPEntry.setStatus("current")
_CfprApPkiTPInstanceId_Type = CfprApManagedObjectId
_CfprApPkiTPInstanceId_Object = MibTableColumn
cfprApPkiTPInstanceId = _CfprApPkiTPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 1),
    _CfprApPkiTPInstanceId_Type()
)
cfprApPkiTPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPkiTPInstanceId.setStatus("current")
_CfprApPkiTPDn_Type = CfprApManagedObjectDn
_CfprApPkiTPDn_Object = MibTableColumn
cfprApPkiTPDn = _CfprApPkiTPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 2),
    _CfprApPkiTPDn_Type()
)
cfprApPkiTPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPDn.setStatus("current")
_CfprApPkiTPRn_Type = SnmpAdminString
_CfprApPkiTPRn_Object = MibTableColumn
cfprApPkiTPRn = _CfprApPkiTPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 3),
    _CfprApPkiTPRn_Type()
)
cfprApPkiTPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPRn.setStatus("current")
_CfprApPkiTPCertChain_Type = SnmpAdminString
_CfprApPkiTPCertChain_Object = MibTableColumn
cfprApPkiTPCertChain = _CfprApPkiTPCertChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 4),
    _CfprApPkiTPCertChain_Type()
)
cfprApPkiTPCertChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPCertChain.setStatus("current")
_CfprApPkiTPCertStatus_Type = CfprApPkiCertStatus
_CfprApPkiTPCertStatus_Object = MibTableColumn
cfprApPkiTPCertStatus = _CfprApPkiTPCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 5),
    _CfprApPkiTPCertStatus_Type()
)
cfprApPkiTPCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPCertStatus.setStatus("current")
_CfprApPkiTPDescr_Type = SnmpAdminString
_CfprApPkiTPDescr_Object = MibTableColumn
cfprApPkiTPDescr = _CfprApPkiTPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 6),
    _CfprApPkiTPDescr_Type()
)
cfprApPkiTPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPDescr.setStatus("current")
_CfprApPkiTPFp_Type = SnmpAdminString
_CfprApPkiTPFp_Object = MibTableColumn
cfprApPkiTPFp = _CfprApPkiTPFp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 7),
    _CfprApPkiTPFp_Type()
)
cfprApPkiTPFp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPFp.setStatus("current")
_CfprApPkiTPIntId_Type = SnmpAdminString
_CfprApPkiTPIntId_Object = MibTableColumn
cfprApPkiTPIntId = _CfprApPkiTPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 8),
    _CfprApPkiTPIntId_Type()
)
cfprApPkiTPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPIntId.setStatus("current")
_CfprApPkiTPName_Type = SnmpAdminString
_CfprApPkiTPName_Object = MibTableColumn
cfprApPkiTPName = _CfprApPkiTPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 9),
    _CfprApPkiTPName_Type()
)
cfprApPkiTPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPName.setStatus("current")
_CfprApPkiTPNumCerts_Type = Gauge32
_CfprApPkiTPNumCerts_Object = MibTableColumn
cfprApPkiTPNumCerts = _CfprApPkiTPNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 10),
    _CfprApPkiTPNumCerts_Type()
)
cfprApPkiTPNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPNumCerts.setStatus("current")
_CfprApPkiTPPolicyLevel_Type = Gauge32
_CfprApPkiTPPolicyLevel_Object = MibTableColumn
cfprApPkiTPPolicyLevel = _CfprApPkiTPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 11),
    _CfprApPkiTPPolicyLevel_Type()
)
cfprApPkiTPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPPolicyLevel.setStatus("current")
_CfprApPkiTPPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPkiTPPolicyOwner_Object = MibTableColumn
cfprApPkiTPPolicyOwner = _CfprApPkiTPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 61, 7, 1, 12),
    _CfprApPkiTPPolicyOwner_Type()
)
cfprApPkiTPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPkiTPPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-PKI-MIB",
    **{"cfprApPkiObjects": cfprApPkiObjects,
       "cfprApPkiCertReqTable": cfprApPkiCertReqTable,
       "cfprApPkiCertReqEntry": cfprApPkiCertReqEntry,
       "cfprApPkiCertReqInstanceId": cfprApPkiCertReqInstanceId,
       "cfprApPkiCertReqDn": cfprApPkiCertReqDn,
       "cfprApPkiCertReqRn": cfprApPkiCertReqRn,
       "cfprApPkiCertReqCountry": cfprApPkiCertReqCountry,
       "cfprApPkiCertReqDns": cfprApPkiCertReqDns,
       "cfprApPkiCertReqEmail": cfprApPkiCertReqEmail,
       "cfprApPkiCertReqIp": cfprApPkiCertReqIp,
       "cfprApPkiCertReqIpA": cfprApPkiCertReqIpA,
       "cfprApPkiCertReqIpB": cfprApPkiCertReqIpB,
       "cfprApPkiCertReqIpv6": cfprApPkiCertReqIpv6,
       "cfprApPkiCertReqIpv6A": cfprApPkiCertReqIpv6A,
       "cfprApPkiCertReqIpv6B": cfprApPkiCertReqIpv6B,
       "cfprApPkiCertReqLocality": cfprApPkiCertReqLocality,
       "cfprApPkiCertReqOrgName": cfprApPkiCertReqOrgName,
       "cfprApPkiCertReqOrgUnitName": cfprApPkiCertReqOrgUnitName,
       "cfprApPkiCertReqPwd": cfprApPkiCertReqPwd,
       "cfprApPkiCertReqReq": cfprApPkiCertReqReq,
       "cfprApPkiCertReqState": cfprApPkiCertReqState,
       "cfprApPkiCertReqSubjName": cfprApPkiCertReqSubjName,
       "cfprApPkiEpTable": cfprApPkiEpTable,
       "cfprApPkiEpEntry": cfprApPkiEpEntry,
       "cfprApPkiEpInstanceId": cfprApPkiEpInstanceId,
       "cfprApPkiEpDn": cfprApPkiEpDn,
       "cfprApPkiEpRn": cfprApPkiEpRn,
       "cfprApPkiEpDescr": cfprApPkiEpDescr,
       "cfprApPkiEpFsmDescr": cfprApPkiEpFsmDescr,
       "cfprApPkiEpFsmPrev": cfprApPkiEpFsmPrev,
       "cfprApPkiEpFsmProgr": cfprApPkiEpFsmProgr,
       "cfprApPkiEpFsmRmtInvErrCode": cfprApPkiEpFsmRmtInvErrCode,
       "cfprApPkiEpFsmRmtInvErrDescr": cfprApPkiEpFsmRmtInvErrDescr,
       "cfprApPkiEpFsmRmtInvRslt": cfprApPkiEpFsmRmtInvRslt,
       "cfprApPkiEpFsmStageDescr": cfprApPkiEpFsmStageDescr,
       "cfprApPkiEpFsmStamp": cfprApPkiEpFsmStamp,
       "cfprApPkiEpFsmStatus": cfprApPkiEpFsmStatus,
       "cfprApPkiEpFsmTry": cfprApPkiEpFsmTry,
       "cfprApPkiEpIntId": cfprApPkiEpIntId,
       "cfprApPkiEpName": cfprApPkiEpName,
       "cfprApPkiEpPolicyLevel": cfprApPkiEpPolicyLevel,
       "cfprApPkiEpPolicyOwner": cfprApPkiEpPolicyOwner,
       "cfprApPkiEpFsmTable": cfprApPkiEpFsmTable,
       "cfprApPkiEpFsmEntry": cfprApPkiEpFsmEntry,
       "cfprApPkiEpFsmInstanceId": cfprApPkiEpFsmInstanceId,
       "cfprApPkiEpFsmDn": cfprApPkiEpFsmDn,
       "cfprApPkiEpFsmRn": cfprApPkiEpFsmRn,
       "cfprApPkiEpFsmCompletionTime": cfprApPkiEpFsmCompletionTime,
       "cfprApPkiEpFsmCurrentFsm": cfprApPkiEpFsmCurrentFsm,
       "cfprApPkiEpFsmDescrData": cfprApPkiEpFsmDescrData,
       "cfprApPkiEpFsmFsmStatus": cfprApPkiEpFsmFsmStatus,
       "cfprApPkiEpFsmProgress": cfprApPkiEpFsmProgress,
       "cfprApPkiEpFsmRmtErrCode": cfprApPkiEpFsmRmtErrCode,
       "cfprApPkiEpFsmRmtErrDescr": cfprApPkiEpFsmRmtErrDescr,
       "cfprApPkiEpFsmRmtRslt": cfprApPkiEpFsmRmtRslt,
       "cfprApPkiEpFsmStageTable": cfprApPkiEpFsmStageTable,
       "cfprApPkiEpFsmStageEntry": cfprApPkiEpFsmStageEntry,
       "cfprApPkiEpFsmStageInstanceId": cfprApPkiEpFsmStageInstanceId,
       "cfprApPkiEpFsmStageDn": cfprApPkiEpFsmStageDn,
       "cfprApPkiEpFsmStageRn": cfprApPkiEpFsmStageRn,
       "cfprApPkiEpFsmStageDescrData": cfprApPkiEpFsmStageDescrData,
       "cfprApPkiEpFsmStageLastUpdateTime": cfprApPkiEpFsmStageLastUpdateTime,
       "cfprApPkiEpFsmStageName": cfprApPkiEpFsmStageName,
       "cfprApPkiEpFsmStageOrder": cfprApPkiEpFsmStageOrder,
       "cfprApPkiEpFsmStageRetry": cfprApPkiEpFsmStageRetry,
       "cfprApPkiEpFsmStageStageStatus": cfprApPkiEpFsmStageStageStatus,
       "cfprApPkiEpFsmTaskTable": cfprApPkiEpFsmTaskTable,
       "cfprApPkiEpFsmTaskEntry": cfprApPkiEpFsmTaskEntry,
       "cfprApPkiEpFsmTaskInstanceId": cfprApPkiEpFsmTaskInstanceId,
       "cfprApPkiEpFsmTaskDn": cfprApPkiEpFsmTaskDn,
       "cfprApPkiEpFsmTaskRn": cfprApPkiEpFsmTaskRn,
       "cfprApPkiEpFsmTaskCompletion": cfprApPkiEpFsmTaskCompletion,
       "cfprApPkiEpFsmTaskFlags": cfprApPkiEpFsmTaskFlags,
       "cfprApPkiEpFsmTaskItem": cfprApPkiEpFsmTaskItem,
       "cfprApPkiEpFsmTaskSeqId": cfprApPkiEpFsmTaskSeqId,
       "cfprApPkiKeyRingTable": cfprApPkiKeyRingTable,
       "cfprApPkiKeyRingEntry": cfprApPkiKeyRingEntry,
       "cfprApPkiKeyRingInstanceId": cfprApPkiKeyRingInstanceId,
       "cfprApPkiKeyRingDn": cfprApPkiKeyRingDn,
       "cfprApPkiKeyRingRn": cfprApPkiKeyRingRn,
       "cfprApPkiKeyRingAdminState": cfprApPkiKeyRingAdminState,
       "cfprApPkiKeyRingCert": cfprApPkiKeyRingCert,
       "cfprApPkiKeyRingCertStatus": cfprApPkiKeyRingCertStatus,
       "cfprApPkiKeyRingConfigState": cfprApPkiKeyRingConfigState,
       "cfprApPkiKeyRingConfigStatusMessage": cfprApPkiKeyRingConfigStatusMessage,
       "cfprApPkiKeyRingDescr": cfprApPkiKeyRingDescr,
       "cfprApPkiKeyRingIntId": cfprApPkiKeyRingIntId,
       "cfprApPkiKeyRingKey": cfprApPkiKeyRingKey,
       "cfprApPkiKeyRingModulus": cfprApPkiKeyRingModulus,
       "cfprApPkiKeyRingName": cfprApPkiKeyRingName,
       "cfprApPkiKeyRingPolicyLevel": cfprApPkiKeyRingPolicyLevel,
       "cfprApPkiKeyRingPolicyOwner": cfprApPkiKeyRingPolicyOwner,
       "cfprApPkiKeyRingRegen": cfprApPkiKeyRingRegen,
       "cfprApPkiKeyRingTp": cfprApPkiKeyRingTp,
       "cfprApPkiTPTable": cfprApPkiTPTable,
       "cfprApPkiTPEntry": cfprApPkiTPEntry,
       "cfprApPkiTPInstanceId": cfprApPkiTPInstanceId,
       "cfprApPkiTPDn": cfprApPkiTPDn,
       "cfprApPkiTPRn": cfprApPkiTPRn,
       "cfprApPkiTPCertChain": cfprApPkiTPCertChain,
       "cfprApPkiTPCertStatus": cfprApPkiTPCertStatus,
       "cfprApPkiTPDescr": cfprApPkiTPDescr,
       "cfprApPkiTPFp": cfprApPkiTPFp,
       "cfprApPkiTPIntId": cfprApPkiTPIntId,
       "cfprApPkiTPName": cfprApPkiTPName,
       "cfprApPkiTPNumCerts": cfprApPkiTPNumCerts,
       "cfprApPkiTPPolicyLevel": cfprApPkiTPPolicyLevel,
       "cfprApPkiTPPolicyOwner": cfprApPkiTPPolicyOwner}
)
