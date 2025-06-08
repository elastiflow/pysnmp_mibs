# SNMP MIB module (CISCO-FIREPOWER-PKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-PKI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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
 CfprAaaFqdnEnforceType,
 CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPkiCertRevokeMethod,
 CfprPkiCertStatus,
 CfprPkiEc,
 CfprPkiEpFsmCurrentFsm,
 CfprPkiEpFsmStageName,
 CfprPkiEpFsmTaskItem,
 CfprPkiImportActivity,
 CfprPkiKeyringState,
 CfprPkiModulus,
 CfprPkiTpAutoImportImportControlStatus,
 CfprPkiTransferState,
 CfprPkiTransport,
 CfprPkiTransportNoLocal,
 CfprPkiType,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAaaConfigState",
    "CfprAaaFqdnEnforceType",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPkiCertRevokeMethod",
    "CfprPkiCertStatus",
    "CfprPkiEc",
    "CfprPkiEpFsmCurrentFsm",
    "CfprPkiEpFsmStageName",
    "CfprPkiEpFsmTaskItem",
    "CfprPkiImportActivity",
    "CfprPkiKeyringState",
    "CfprPkiModulus",
    "CfprPkiTpAutoImportImportControlStatus",
    "CfprPkiTransferState",
    "CfprPkiTransport",
    "CfprPkiTransportNoLocal",
    "CfprPkiType",
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

cfprPkiObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprPkiCertReqTable_Object = MibTable
cfprPkiCertReqTable = _CfprPkiCertReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1)
)
if mibBuilder.loadTexts:
    cfprPkiCertReqTable.setStatus("current")
_CfprPkiCertReqEntry_Object = MibTableRow
cfprPkiCertReqEntry = _CfprPkiCertReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1)
)
cfprPkiCertReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiCertReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiCertReqEntry.setStatus("current")
_CfprPkiCertReqInstanceId_Type = CfprManagedObjectId
_CfprPkiCertReqInstanceId_Object = MibTableColumn
cfprPkiCertReqInstanceId = _CfprPkiCertReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 1),
    _CfprPkiCertReqInstanceId_Type()
)
cfprPkiCertReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiCertReqInstanceId.setStatus("current")
_CfprPkiCertReqDn_Type = CfprManagedObjectDn
_CfprPkiCertReqDn_Object = MibTableColumn
cfprPkiCertReqDn = _CfprPkiCertReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 2),
    _CfprPkiCertReqDn_Type()
)
cfprPkiCertReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqDn.setStatus("current")
_CfprPkiCertReqRn_Type = SnmpAdminString
_CfprPkiCertReqRn_Object = MibTableColumn
cfprPkiCertReqRn = _CfprPkiCertReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 3),
    _CfprPkiCertReqRn_Type()
)
cfprPkiCertReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqRn.setStatus("current")
_CfprPkiCertReqCountry_Type = SnmpAdminString
_CfprPkiCertReqCountry_Object = MibTableColumn
cfprPkiCertReqCountry = _CfprPkiCertReqCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 4),
    _CfprPkiCertReqCountry_Type()
)
cfprPkiCertReqCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqCountry.setStatus("current")
_CfprPkiCertReqDns_Type = SnmpAdminString
_CfprPkiCertReqDns_Object = MibTableColumn
cfprPkiCertReqDns = _CfprPkiCertReqDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 5),
    _CfprPkiCertReqDns_Type()
)
cfprPkiCertReqDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqDns.setStatus("current")
_CfprPkiCertReqEmail_Type = SnmpAdminString
_CfprPkiCertReqEmail_Object = MibTableColumn
cfprPkiCertReqEmail = _CfprPkiCertReqEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 6),
    _CfprPkiCertReqEmail_Type()
)
cfprPkiCertReqEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqEmail.setStatus("current")
_CfprPkiCertReqIp_Type = SnmpAdminString
_CfprPkiCertReqIp_Object = MibTableColumn
cfprPkiCertReqIp = _CfprPkiCertReqIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 7),
    _CfprPkiCertReqIp_Type()
)
cfprPkiCertReqIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqIp.setStatus("current")
_CfprPkiCertReqIpA_Type = InetAddressIPv4
_CfprPkiCertReqIpA_Object = MibTableColumn
cfprPkiCertReqIpA = _CfprPkiCertReqIpA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 8),
    _CfprPkiCertReqIpA_Type()
)
cfprPkiCertReqIpA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqIpA.setStatus("current")
_CfprPkiCertReqIpB_Type = InetAddressIPv4
_CfprPkiCertReqIpB_Object = MibTableColumn
cfprPkiCertReqIpB = _CfprPkiCertReqIpB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 9),
    _CfprPkiCertReqIpB_Type()
)
cfprPkiCertReqIpB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqIpB.setStatus("current")
_CfprPkiCertReqIpv6_Type = SnmpAdminString
_CfprPkiCertReqIpv6_Object = MibTableColumn
cfprPkiCertReqIpv6 = _CfprPkiCertReqIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 10),
    _CfprPkiCertReqIpv6_Type()
)
cfprPkiCertReqIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqIpv6.setStatus("current")
_CfprPkiCertReqIpv6A_Type = InetAddressIPv6
_CfprPkiCertReqIpv6A_Object = MibTableColumn
cfprPkiCertReqIpv6A = _CfprPkiCertReqIpv6A_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 11),
    _CfprPkiCertReqIpv6A_Type()
)
cfprPkiCertReqIpv6A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqIpv6A.setStatus("current")
_CfprPkiCertReqIpv6B_Type = InetAddressIPv6
_CfprPkiCertReqIpv6B_Object = MibTableColumn
cfprPkiCertReqIpv6B = _CfprPkiCertReqIpv6B_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 12),
    _CfprPkiCertReqIpv6B_Type()
)
cfprPkiCertReqIpv6B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqIpv6B.setStatus("current")
_CfprPkiCertReqLocality_Type = SnmpAdminString
_CfprPkiCertReqLocality_Object = MibTableColumn
cfprPkiCertReqLocality = _CfprPkiCertReqLocality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 13),
    _CfprPkiCertReqLocality_Type()
)
cfprPkiCertReqLocality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqLocality.setStatus("current")
_CfprPkiCertReqOrgName_Type = SnmpAdminString
_CfprPkiCertReqOrgName_Object = MibTableColumn
cfprPkiCertReqOrgName = _CfprPkiCertReqOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 14),
    _CfprPkiCertReqOrgName_Type()
)
cfprPkiCertReqOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqOrgName.setStatus("current")
_CfprPkiCertReqOrgUnitName_Type = SnmpAdminString
_CfprPkiCertReqOrgUnitName_Object = MibTableColumn
cfprPkiCertReqOrgUnitName = _CfprPkiCertReqOrgUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 15),
    _CfprPkiCertReqOrgUnitName_Type()
)
cfprPkiCertReqOrgUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqOrgUnitName.setStatus("current")
_CfprPkiCertReqPwd_Type = SnmpAdminString
_CfprPkiCertReqPwd_Object = MibTableColumn
cfprPkiCertReqPwd = _CfprPkiCertReqPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 16),
    _CfprPkiCertReqPwd_Type()
)
cfprPkiCertReqPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqPwd.setStatus("current")
_CfprPkiCertReqReq_Type = SnmpAdminString
_CfprPkiCertReqReq_Object = MibTableColumn
cfprPkiCertReqReq = _CfprPkiCertReqReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 17),
    _CfprPkiCertReqReq_Type()
)
cfprPkiCertReqReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqReq.setStatus("current")
_CfprPkiCertReqState_Type = SnmpAdminString
_CfprPkiCertReqState_Object = MibTableColumn
cfprPkiCertReqState = _CfprPkiCertReqState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 18),
    _CfprPkiCertReqState_Type()
)
cfprPkiCertReqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqState.setStatus("current")
_CfprPkiCertReqSubjName_Type = SnmpAdminString
_CfprPkiCertReqSubjName_Object = MibTableColumn
cfprPkiCertReqSubjName = _CfprPkiCertReqSubjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 1, 1, 19),
    _CfprPkiCertReqSubjName_Type()
)
cfprPkiCertReqSubjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertReqSubjName.setStatus("current")
_CfprPkiEpTable_Object = MibTable
cfprPkiEpTable = _CfprPkiEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2)
)
if mibBuilder.loadTexts:
    cfprPkiEpTable.setStatus("current")
_CfprPkiEpEntry_Object = MibTableRow
cfprPkiEpEntry = _CfprPkiEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1)
)
cfprPkiEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiEpEntry.setStatus("current")
_CfprPkiEpInstanceId_Type = CfprManagedObjectId
_CfprPkiEpInstanceId_Object = MibTableColumn
cfprPkiEpInstanceId = _CfprPkiEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 1),
    _CfprPkiEpInstanceId_Type()
)
cfprPkiEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiEpInstanceId.setStatus("current")
_CfprPkiEpDn_Type = CfprManagedObjectDn
_CfprPkiEpDn_Object = MibTableColumn
cfprPkiEpDn = _CfprPkiEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 2),
    _CfprPkiEpDn_Type()
)
cfprPkiEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpDn.setStatus("current")
_CfprPkiEpRn_Type = SnmpAdminString
_CfprPkiEpRn_Object = MibTableColumn
cfprPkiEpRn = _CfprPkiEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 3),
    _CfprPkiEpRn_Type()
)
cfprPkiEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpRn.setStatus("current")
_CfprPkiEpDescr_Type = SnmpAdminString
_CfprPkiEpDescr_Object = MibTableColumn
cfprPkiEpDescr = _CfprPkiEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 4),
    _CfprPkiEpDescr_Type()
)
cfprPkiEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpDescr.setStatus("current")
_CfprPkiEpFsmDescr_Type = SnmpAdminString
_CfprPkiEpFsmDescr_Object = MibTableColumn
cfprPkiEpFsmDescr = _CfprPkiEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 5),
    _CfprPkiEpFsmDescr_Type()
)
cfprPkiEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmDescr.setStatus("current")
_CfprPkiEpFsmPrev_Type = SnmpAdminString
_CfprPkiEpFsmPrev_Object = MibTableColumn
cfprPkiEpFsmPrev = _CfprPkiEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 6),
    _CfprPkiEpFsmPrev_Type()
)
cfprPkiEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmPrev.setStatus("current")
_CfprPkiEpFsmProgr_Type = Gauge32
_CfprPkiEpFsmProgr_Object = MibTableColumn
cfprPkiEpFsmProgr = _CfprPkiEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 7),
    _CfprPkiEpFsmProgr_Type()
)
cfprPkiEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmProgr.setStatus("current")
_CfprPkiEpFsmRmtInvErrCode_Type = Gauge32
_CfprPkiEpFsmRmtInvErrCode_Object = MibTableColumn
cfprPkiEpFsmRmtInvErrCode = _CfprPkiEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 8),
    _CfprPkiEpFsmRmtInvErrCode_Type()
)
cfprPkiEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRmtInvErrCode.setStatus("current")
_CfprPkiEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprPkiEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprPkiEpFsmRmtInvErrDescr = _CfprPkiEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 9),
    _CfprPkiEpFsmRmtInvErrDescr_Type()
)
cfprPkiEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRmtInvErrDescr.setStatus("current")
_CfprPkiEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprPkiEpFsmRmtInvRslt_Object = MibTableColumn
cfprPkiEpFsmRmtInvRslt = _CfprPkiEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 10),
    _CfprPkiEpFsmRmtInvRslt_Type()
)
cfprPkiEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRmtInvRslt.setStatus("current")
_CfprPkiEpFsmStageDescr_Type = SnmpAdminString
_CfprPkiEpFsmStageDescr_Object = MibTableColumn
cfprPkiEpFsmStageDescr = _CfprPkiEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 11),
    _CfprPkiEpFsmStageDescr_Type()
)
cfprPkiEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageDescr.setStatus("current")
_CfprPkiEpFsmStamp_Type = DateAndTime
_CfprPkiEpFsmStamp_Object = MibTableColumn
cfprPkiEpFsmStamp = _CfprPkiEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 12),
    _CfprPkiEpFsmStamp_Type()
)
cfprPkiEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStamp.setStatus("current")
_CfprPkiEpFsmStatus_Type = SnmpAdminString
_CfprPkiEpFsmStatus_Object = MibTableColumn
cfprPkiEpFsmStatus = _CfprPkiEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 13),
    _CfprPkiEpFsmStatus_Type()
)
cfprPkiEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStatus.setStatus("current")
_CfprPkiEpFsmTry_Type = Gauge32
_CfprPkiEpFsmTry_Object = MibTableColumn
cfprPkiEpFsmTry = _CfprPkiEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 14),
    _CfprPkiEpFsmTry_Type()
)
cfprPkiEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTry.setStatus("current")
_CfprPkiEpIntId_Type = SnmpAdminString
_CfprPkiEpIntId_Object = MibTableColumn
cfprPkiEpIntId = _CfprPkiEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 15),
    _CfprPkiEpIntId_Type()
)
cfprPkiEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpIntId.setStatus("current")
_CfprPkiEpName_Type = SnmpAdminString
_CfprPkiEpName_Object = MibTableColumn
cfprPkiEpName = _CfprPkiEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 16),
    _CfprPkiEpName_Type()
)
cfprPkiEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpName.setStatus("current")
_CfprPkiEpPolicyLevel_Type = Gauge32
_CfprPkiEpPolicyLevel_Object = MibTableColumn
cfprPkiEpPolicyLevel = _CfprPkiEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 17),
    _CfprPkiEpPolicyLevel_Type()
)
cfprPkiEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpPolicyLevel.setStatus("current")
_CfprPkiEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPkiEpPolicyOwner_Object = MibTableColumn
cfprPkiEpPolicyOwner = _CfprPkiEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 2, 1, 18),
    _CfprPkiEpPolicyOwner_Type()
)
cfprPkiEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpPolicyOwner.setStatus("current")
_CfprPkiEpFsmTable_Object = MibTable
cfprPkiEpFsmTable = _CfprPkiEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3)
)
if mibBuilder.loadTexts:
    cfprPkiEpFsmTable.setStatus("current")
_CfprPkiEpFsmEntry_Object = MibTableRow
cfprPkiEpFsmEntry = _CfprPkiEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1)
)
cfprPkiEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiEpFsmEntry.setStatus("current")
_CfprPkiEpFsmInstanceId_Type = CfprManagedObjectId
_CfprPkiEpFsmInstanceId_Object = MibTableColumn
cfprPkiEpFsmInstanceId = _CfprPkiEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 1),
    _CfprPkiEpFsmInstanceId_Type()
)
cfprPkiEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiEpFsmInstanceId.setStatus("current")
_CfprPkiEpFsmDn_Type = CfprManagedObjectDn
_CfprPkiEpFsmDn_Object = MibTableColumn
cfprPkiEpFsmDn = _CfprPkiEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 2),
    _CfprPkiEpFsmDn_Type()
)
cfprPkiEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmDn.setStatus("current")
_CfprPkiEpFsmRn_Type = SnmpAdminString
_CfprPkiEpFsmRn_Object = MibTableColumn
cfprPkiEpFsmRn = _CfprPkiEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 3),
    _CfprPkiEpFsmRn_Type()
)
cfprPkiEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRn.setStatus("current")
_CfprPkiEpFsmCompletionTime_Type = DateAndTime
_CfprPkiEpFsmCompletionTime_Object = MibTableColumn
cfprPkiEpFsmCompletionTime = _CfprPkiEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 4),
    _CfprPkiEpFsmCompletionTime_Type()
)
cfprPkiEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmCompletionTime.setStatus("current")
_CfprPkiEpFsmCurrentFsm_Type = CfprPkiEpFsmCurrentFsm
_CfprPkiEpFsmCurrentFsm_Object = MibTableColumn
cfprPkiEpFsmCurrentFsm = _CfprPkiEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 5),
    _CfprPkiEpFsmCurrentFsm_Type()
)
cfprPkiEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmCurrentFsm.setStatus("current")
_CfprPkiEpFsmDescrData_Type = SnmpAdminString
_CfprPkiEpFsmDescrData_Object = MibTableColumn
cfprPkiEpFsmDescrData = _CfprPkiEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 6),
    _CfprPkiEpFsmDescrData_Type()
)
cfprPkiEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmDescrData.setStatus("current")
_CfprPkiEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprPkiEpFsmFsmStatus_Object = MibTableColumn
cfprPkiEpFsmFsmStatus = _CfprPkiEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 7),
    _CfprPkiEpFsmFsmStatus_Type()
)
cfprPkiEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmFsmStatus.setStatus("current")
_CfprPkiEpFsmProgress_Type = Gauge32
_CfprPkiEpFsmProgress_Object = MibTableColumn
cfprPkiEpFsmProgress = _CfprPkiEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 8),
    _CfprPkiEpFsmProgress_Type()
)
cfprPkiEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmProgress.setStatus("current")
_CfprPkiEpFsmRmtErrCode_Type = Gauge32
_CfprPkiEpFsmRmtErrCode_Object = MibTableColumn
cfprPkiEpFsmRmtErrCode = _CfprPkiEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 9),
    _CfprPkiEpFsmRmtErrCode_Type()
)
cfprPkiEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRmtErrCode.setStatus("current")
_CfprPkiEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprPkiEpFsmRmtErrDescr_Object = MibTableColumn
cfprPkiEpFsmRmtErrDescr = _CfprPkiEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 10),
    _CfprPkiEpFsmRmtErrDescr_Type()
)
cfprPkiEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRmtErrDescr.setStatus("current")
_CfprPkiEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprPkiEpFsmRmtRslt_Object = MibTableColumn
cfprPkiEpFsmRmtRslt = _CfprPkiEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 3, 1, 11),
    _CfprPkiEpFsmRmtRslt_Type()
)
cfprPkiEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmRmtRslt.setStatus("current")
_CfprPkiEpFsmStageTable_Object = MibTable
cfprPkiEpFsmStageTable = _CfprPkiEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4)
)
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageTable.setStatus("current")
_CfprPkiEpFsmStageEntry_Object = MibTableRow
cfprPkiEpFsmStageEntry = _CfprPkiEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1)
)
cfprPkiEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageEntry.setStatus("current")
_CfprPkiEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprPkiEpFsmStageInstanceId_Object = MibTableColumn
cfprPkiEpFsmStageInstanceId = _CfprPkiEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 1),
    _CfprPkiEpFsmStageInstanceId_Type()
)
cfprPkiEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageInstanceId.setStatus("current")
_CfprPkiEpFsmStageDn_Type = CfprManagedObjectDn
_CfprPkiEpFsmStageDn_Object = MibTableColumn
cfprPkiEpFsmStageDn = _CfprPkiEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 2),
    _CfprPkiEpFsmStageDn_Type()
)
cfprPkiEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageDn.setStatus("current")
_CfprPkiEpFsmStageRn_Type = SnmpAdminString
_CfprPkiEpFsmStageRn_Object = MibTableColumn
cfprPkiEpFsmStageRn = _CfprPkiEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 3),
    _CfprPkiEpFsmStageRn_Type()
)
cfprPkiEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageRn.setStatus("current")
_CfprPkiEpFsmStageDescrData_Type = SnmpAdminString
_CfprPkiEpFsmStageDescrData_Object = MibTableColumn
cfprPkiEpFsmStageDescrData = _CfprPkiEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 4),
    _CfprPkiEpFsmStageDescrData_Type()
)
cfprPkiEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageDescrData.setStatus("current")
_CfprPkiEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprPkiEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprPkiEpFsmStageLastUpdateTime = _CfprPkiEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 5),
    _CfprPkiEpFsmStageLastUpdateTime_Type()
)
cfprPkiEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageLastUpdateTime.setStatus("current")
_CfprPkiEpFsmStageName_Type = CfprPkiEpFsmStageName
_CfprPkiEpFsmStageName_Object = MibTableColumn
cfprPkiEpFsmStageName = _CfprPkiEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 6),
    _CfprPkiEpFsmStageName_Type()
)
cfprPkiEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageName.setStatus("current")
_CfprPkiEpFsmStageOrder_Type = Gauge32
_CfprPkiEpFsmStageOrder_Object = MibTableColumn
cfprPkiEpFsmStageOrder = _CfprPkiEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 7),
    _CfprPkiEpFsmStageOrder_Type()
)
cfprPkiEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageOrder.setStatus("current")
_CfprPkiEpFsmStageRetry_Type = Gauge32
_CfprPkiEpFsmStageRetry_Object = MibTableColumn
cfprPkiEpFsmStageRetry = _CfprPkiEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 8),
    _CfprPkiEpFsmStageRetry_Type()
)
cfprPkiEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageRetry.setStatus("current")
_CfprPkiEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprPkiEpFsmStageStageStatus_Object = MibTableColumn
cfprPkiEpFsmStageStageStatus = _CfprPkiEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 4, 1, 9),
    _CfprPkiEpFsmStageStageStatus_Type()
)
cfprPkiEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmStageStageStatus.setStatus("current")
_CfprPkiEpFsmTaskTable_Object = MibTable
cfprPkiEpFsmTaskTable = _CfprPkiEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5)
)
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskTable.setStatus("current")
_CfprPkiEpFsmTaskEntry_Object = MibTableRow
cfprPkiEpFsmTaskEntry = _CfprPkiEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1)
)
cfprPkiEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskEntry.setStatus("current")
_CfprPkiEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprPkiEpFsmTaskInstanceId_Object = MibTableColumn
cfprPkiEpFsmTaskInstanceId = _CfprPkiEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 1),
    _CfprPkiEpFsmTaskInstanceId_Type()
)
cfprPkiEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskInstanceId.setStatus("current")
_CfprPkiEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprPkiEpFsmTaskDn_Object = MibTableColumn
cfprPkiEpFsmTaskDn = _CfprPkiEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 2),
    _CfprPkiEpFsmTaskDn_Type()
)
cfprPkiEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskDn.setStatus("current")
_CfprPkiEpFsmTaskRn_Type = SnmpAdminString
_CfprPkiEpFsmTaskRn_Object = MibTableColumn
cfprPkiEpFsmTaskRn = _CfprPkiEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 3),
    _CfprPkiEpFsmTaskRn_Type()
)
cfprPkiEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskRn.setStatus("current")
_CfprPkiEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprPkiEpFsmTaskCompletion_Object = MibTableColumn
cfprPkiEpFsmTaskCompletion = _CfprPkiEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 4),
    _CfprPkiEpFsmTaskCompletion_Type()
)
cfprPkiEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskCompletion.setStatus("current")
_CfprPkiEpFsmTaskFlags_Type = CfprFsmFlags
_CfprPkiEpFsmTaskFlags_Object = MibTableColumn
cfprPkiEpFsmTaskFlags = _CfprPkiEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 5),
    _CfprPkiEpFsmTaskFlags_Type()
)
cfprPkiEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskFlags.setStatus("current")
_CfprPkiEpFsmTaskItem_Type = CfprPkiEpFsmTaskItem
_CfprPkiEpFsmTaskItem_Object = MibTableColumn
cfprPkiEpFsmTaskItem = _CfprPkiEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 6),
    _CfprPkiEpFsmTaskItem_Type()
)
cfprPkiEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskItem.setStatus("current")
_CfprPkiEpFsmTaskSeqId_Type = Gauge32
_CfprPkiEpFsmTaskSeqId_Object = MibTableColumn
cfprPkiEpFsmTaskSeqId = _CfprPkiEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 5, 1, 7),
    _CfprPkiEpFsmTaskSeqId_Type()
)
cfprPkiEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiEpFsmTaskSeqId.setStatus("current")
_CfprPkiKeyRingTable_Object = MibTable
cfprPkiKeyRingTable = _CfprPkiKeyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6)
)
if mibBuilder.loadTexts:
    cfprPkiKeyRingTable.setStatus("current")
_CfprPkiKeyRingEntry_Object = MibTableRow
cfprPkiKeyRingEntry = _CfprPkiKeyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1)
)
cfprPkiKeyRingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiKeyRingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiKeyRingEntry.setStatus("current")
_CfprPkiKeyRingInstanceId_Type = CfprManagedObjectId
_CfprPkiKeyRingInstanceId_Object = MibTableColumn
cfprPkiKeyRingInstanceId = _CfprPkiKeyRingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 1),
    _CfprPkiKeyRingInstanceId_Type()
)
cfprPkiKeyRingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiKeyRingInstanceId.setStatus("current")
_CfprPkiKeyRingDn_Type = CfprManagedObjectDn
_CfprPkiKeyRingDn_Object = MibTableColumn
cfprPkiKeyRingDn = _CfprPkiKeyRingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 2),
    _CfprPkiKeyRingDn_Type()
)
cfprPkiKeyRingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingDn.setStatus("current")
_CfprPkiKeyRingRn_Type = SnmpAdminString
_CfprPkiKeyRingRn_Object = MibTableColumn
cfprPkiKeyRingRn = _CfprPkiKeyRingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 3),
    _CfprPkiKeyRingRn_Type()
)
cfprPkiKeyRingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingRn.setStatus("current")
_CfprPkiKeyRingAdminState_Type = CfprPkiKeyringState
_CfprPkiKeyRingAdminState_Object = MibTableColumn
cfprPkiKeyRingAdminState = _CfprPkiKeyRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 4),
    _CfprPkiKeyRingAdminState_Type()
)
cfprPkiKeyRingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingAdminState.setStatus("current")
_CfprPkiKeyRingCert_Type = SnmpAdminString
_CfprPkiKeyRingCert_Object = MibTableColumn
cfprPkiKeyRingCert = _CfprPkiKeyRingCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 5),
    _CfprPkiKeyRingCert_Type()
)
cfprPkiKeyRingCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingCert.setStatus("current")
_CfprPkiKeyRingCertStatus_Type = CfprPkiCertStatus
_CfprPkiKeyRingCertStatus_Object = MibTableColumn
cfprPkiKeyRingCertStatus = _CfprPkiKeyRingCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 6),
    _CfprPkiKeyRingCertStatus_Type()
)
cfprPkiKeyRingCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingCertStatus.setStatus("current")
_CfprPkiKeyRingConfigState_Type = CfprAaaConfigState
_CfprPkiKeyRingConfigState_Object = MibTableColumn
cfprPkiKeyRingConfigState = _CfprPkiKeyRingConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 7),
    _CfprPkiKeyRingConfigState_Type()
)
cfprPkiKeyRingConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingConfigState.setStatus("current")
_CfprPkiKeyRingConfigStatusMessage_Type = SnmpAdminString
_CfprPkiKeyRingConfigStatusMessage_Object = MibTableColumn
cfprPkiKeyRingConfigStatusMessage = _CfprPkiKeyRingConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 8),
    _CfprPkiKeyRingConfigStatusMessage_Type()
)
cfprPkiKeyRingConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingConfigStatusMessage.setStatus("current")
_CfprPkiKeyRingDescr_Type = SnmpAdminString
_CfprPkiKeyRingDescr_Object = MibTableColumn
cfprPkiKeyRingDescr = _CfprPkiKeyRingDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 9),
    _CfprPkiKeyRingDescr_Type()
)
cfprPkiKeyRingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingDescr.setStatus("current")
_CfprPkiKeyRingIntId_Type = SnmpAdminString
_CfprPkiKeyRingIntId_Object = MibTableColumn
cfprPkiKeyRingIntId = _CfprPkiKeyRingIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 10),
    _CfprPkiKeyRingIntId_Type()
)
cfprPkiKeyRingIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingIntId.setStatus("current")
_CfprPkiKeyRingKey_Type = SnmpAdminString
_CfprPkiKeyRingKey_Object = MibTableColumn
cfprPkiKeyRingKey = _CfprPkiKeyRingKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 11),
    _CfprPkiKeyRingKey_Type()
)
cfprPkiKeyRingKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingKey.setStatus("current")
_CfprPkiKeyRingModulus_Type = CfprPkiModulus
_CfprPkiKeyRingModulus_Object = MibTableColumn
cfprPkiKeyRingModulus = _CfprPkiKeyRingModulus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 12),
    _CfprPkiKeyRingModulus_Type()
)
cfprPkiKeyRingModulus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingModulus.setStatus("current")
_CfprPkiKeyRingName_Type = SnmpAdminString
_CfprPkiKeyRingName_Object = MibTableColumn
cfprPkiKeyRingName = _CfprPkiKeyRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 13),
    _CfprPkiKeyRingName_Type()
)
cfprPkiKeyRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingName.setStatus("current")
_CfprPkiKeyRingPolicyLevel_Type = Gauge32
_CfprPkiKeyRingPolicyLevel_Object = MibTableColumn
cfprPkiKeyRingPolicyLevel = _CfprPkiKeyRingPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 14),
    _CfprPkiKeyRingPolicyLevel_Type()
)
cfprPkiKeyRingPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingPolicyLevel.setStatus("current")
_CfprPkiKeyRingPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPkiKeyRingPolicyOwner_Object = MibTableColumn
cfprPkiKeyRingPolicyOwner = _CfprPkiKeyRingPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 15),
    _CfprPkiKeyRingPolicyOwner_Type()
)
cfprPkiKeyRingPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingPolicyOwner.setStatus("current")
_CfprPkiKeyRingRegen_Type = TruthValue
_CfprPkiKeyRingRegen_Object = MibTableColumn
cfprPkiKeyRingRegen = _CfprPkiKeyRingRegen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 16),
    _CfprPkiKeyRingRegen_Type()
)
cfprPkiKeyRingRegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingRegen.setStatus("current")
_CfprPkiKeyRingTp_Type = SnmpAdminString
_CfprPkiKeyRingTp_Object = MibTableColumn
cfprPkiKeyRingTp = _CfprPkiKeyRingTp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 17),
    _CfprPkiKeyRingTp_Type()
)
cfprPkiKeyRingTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingTp.setStatus("current")
_CfprPkiKeyRingZeroized_Type = TruthValue
_CfprPkiKeyRingZeroized_Object = MibTableColumn
cfprPkiKeyRingZeroized = _CfprPkiKeyRingZeroized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 18),
    _CfprPkiKeyRingZeroized_Type()
)
cfprPkiKeyRingZeroized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingZeroized.setStatus("current")
_CfprPkiKeyRingEc_Type = CfprPkiEc
_CfprPkiKeyRingEc_Object = MibTableColumn
cfprPkiKeyRingEc = _CfprPkiKeyRingEc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 19),
    _CfprPkiKeyRingEc_Type()
)
cfprPkiKeyRingEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingEc.setStatus("current")
_CfprPkiKeyRingFqdnEnforce_Type = CfprAaaFqdnEnforceType
_CfprPkiKeyRingFqdnEnforce_Object = MibTableColumn
cfprPkiKeyRingFqdnEnforce = _CfprPkiKeyRingFqdnEnforce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 20),
    _CfprPkiKeyRingFqdnEnforce_Type()
)
cfprPkiKeyRingFqdnEnforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingFqdnEnforce.setStatus("current")
_CfprPkiKeyRingType_Type = CfprPkiType
_CfprPkiKeyRingType_Object = MibTableColumn
cfprPkiKeyRingType = _CfprPkiKeyRingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 6, 1, 21),
    _CfprPkiKeyRingType_Type()
)
cfprPkiKeyRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiKeyRingType.setStatus("current")
_CfprPkiTPTable_Object = MibTable
cfprPkiTPTable = _CfprPkiTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7)
)
if mibBuilder.loadTexts:
    cfprPkiTPTable.setStatus("current")
_CfprPkiTPEntry_Object = MibTableRow
cfprPkiTPEntry = _CfprPkiTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1)
)
cfprPkiTPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiTPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiTPEntry.setStatus("current")
_CfprPkiTPInstanceId_Type = CfprManagedObjectId
_CfprPkiTPInstanceId_Object = MibTableColumn
cfprPkiTPInstanceId = _CfprPkiTPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 1),
    _CfprPkiTPInstanceId_Type()
)
cfprPkiTPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiTPInstanceId.setStatus("current")
_CfprPkiTPDn_Type = CfprManagedObjectDn
_CfprPkiTPDn_Object = MibTableColumn
cfprPkiTPDn = _CfprPkiTPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 2),
    _CfprPkiTPDn_Type()
)
cfprPkiTPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPDn.setStatus("current")
_CfprPkiTPRn_Type = SnmpAdminString
_CfprPkiTPRn_Object = MibTableColumn
cfprPkiTPRn = _CfprPkiTPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 3),
    _CfprPkiTPRn_Type()
)
cfprPkiTPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPRn.setStatus("current")
_CfprPkiTPCertChain_Type = SnmpAdminString
_CfprPkiTPCertChain_Object = MibTableColumn
cfprPkiTPCertChain = _CfprPkiTPCertChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 4),
    _CfprPkiTPCertChain_Type()
)
cfprPkiTPCertChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPCertChain.setStatus("current")
_CfprPkiTPCertStatus_Type = CfprPkiCertStatus
_CfprPkiTPCertStatus_Object = MibTableColumn
cfprPkiTPCertStatus = _CfprPkiTPCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 5),
    _CfprPkiTPCertStatus_Type()
)
cfprPkiTPCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPCertStatus.setStatus("current")
_CfprPkiTPDescr_Type = SnmpAdminString
_CfprPkiTPDescr_Object = MibTableColumn
cfprPkiTPDescr = _CfprPkiTPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 6),
    _CfprPkiTPDescr_Type()
)
cfprPkiTPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPDescr.setStatus("current")
_CfprPkiTPFp_Type = SnmpAdminString
_CfprPkiTPFp_Object = MibTableColumn
cfprPkiTPFp = _CfprPkiTPFp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 7),
    _CfprPkiTPFp_Type()
)
cfprPkiTPFp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPFp.setStatus("current")
_CfprPkiTPIntId_Type = SnmpAdminString
_CfprPkiTPIntId_Object = MibTableColumn
cfprPkiTPIntId = _CfprPkiTPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 8),
    _CfprPkiTPIntId_Type()
)
cfprPkiTPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPIntId.setStatus("current")
_CfprPkiTPName_Type = SnmpAdminString
_CfprPkiTPName_Object = MibTableColumn
cfprPkiTPName = _CfprPkiTPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 9),
    _CfprPkiTPName_Type()
)
cfprPkiTPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPName.setStatus("current")
_CfprPkiTPNumCerts_Type = Gauge32
_CfprPkiTPNumCerts_Object = MibTableColumn
cfprPkiTPNumCerts = _CfprPkiTPNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 10),
    _CfprPkiTPNumCerts_Type()
)
cfprPkiTPNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPNumCerts.setStatus("current")
_CfprPkiTPPolicyLevel_Type = Gauge32
_CfprPkiTPPolicyLevel_Object = MibTableColumn
cfprPkiTPPolicyLevel = _CfprPkiTPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 11),
    _CfprPkiTPPolicyLevel_Type()
)
cfprPkiTPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPPolicyLevel.setStatus("current")
_CfprPkiTPPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPkiTPPolicyOwner_Object = MibTableColumn
cfprPkiTPPolicyOwner = _CfprPkiTPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 12),
    _CfprPkiTPPolicyOwner_Type()
)
cfprPkiTPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPPolicyOwner.setStatus("current")
_CfprPkiTPCertChainDecode_Type = SnmpAdminString
_CfprPkiTPCertChainDecode_Object = MibTableColumn
cfprPkiTPCertChainDecode = _CfprPkiTPCertChainDecode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 7, 1, 13),
    _CfprPkiTPCertChainDecode_Type()
)
cfprPkiTPCertChainDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTPCertChainDecode.setStatus("current")
_CfprPkiCertRevokeTable_Object = MibTable
cfprPkiCertRevokeTable = _CfprPkiCertRevokeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8)
)
if mibBuilder.loadTexts:
    cfprPkiCertRevokeTable.setStatus("current")
_CfprPkiCertRevokeEntry_Object = MibTableRow
cfprPkiCertRevokeEntry = _CfprPkiCertRevokeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1)
)
cfprPkiCertRevokeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiCertRevokeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiCertRevokeEntry.setStatus("current")
_CfprPkiCertRevokeInstanceId_Type = CfprManagedObjectId
_CfprPkiCertRevokeInstanceId_Object = MibTableColumn
cfprPkiCertRevokeInstanceId = _CfprPkiCertRevokeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 1),
    _CfprPkiCertRevokeInstanceId_Type()
)
cfprPkiCertRevokeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeInstanceId.setStatus("current")
_CfprPkiCertRevokeDn_Type = CfprManagedObjectDn
_CfprPkiCertRevokeDn_Object = MibTableColumn
cfprPkiCertRevokeDn = _CfprPkiCertRevokeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 2),
    _CfprPkiCertRevokeDn_Type()
)
cfprPkiCertRevokeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeDn.setStatus("current")
_CfprPkiCertRevokeRn_Type = SnmpAdminString
_CfprPkiCertRevokeRn_Object = MibTableColumn
cfprPkiCertRevokeRn = _CfprPkiCertRevokeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 3),
    _CfprPkiCertRevokeRn_Type()
)
cfprPkiCertRevokeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeRn.setStatus("current")
_CfprPkiCertRevokeCertRevokeMethod_Type = CfprPkiCertRevokeMethod
_CfprPkiCertRevokeCertRevokeMethod_Object = MibTableColumn
cfprPkiCertRevokeCertRevokeMethod = _CfprPkiCertRevokeCertRevokeMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 4),
    _CfprPkiCertRevokeCertRevokeMethod_Type()
)
cfprPkiCertRevokeCertRevokeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCertRevokeMethod.setStatus("current")
_CfprPkiCertRevokeCertStatus_Type = CfprPkiCertStatus
_CfprPkiCertRevokeCertStatus_Object = MibTableColumn
cfprPkiCertRevokeCertStatus = _CfprPkiCertRevokeCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 5),
    _CfprPkiCertRevokeCertStatus_Type()
)
cfprPkiCertRevokeCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCertStatus.setStatus("current")
_CfprPkiCertRevokeCrl_Type = SnmpAdminString
_CfprPkiCertRevokeCrl_Object = MibTableColumn
cfprPkiCertRevokeCrl = _CfprPkiCertRevokeCrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 6),
    _CfprPkiCertRevokeCrl_Type()
)
cfprPkiCertRevokeCrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrl.setStatus("current")
_CfprPkiCertRevokeCrlPollCount_Type = Gauge32
_CfprPkiCertRevokeCrlPollCount_Object = MibTableColumn
cfprPkiCertRevokeCrlPollCount = _CfprPkiCertRevokeCrlPollCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 7),
    _CfprPkiCertRevokeCrlPollCount_Type()
)
cfprPkiCertRevokeCrlPollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollCount.setStatus("current")
_CfprPkiCertRevokeCrlPollFilename_Type = SnmpAdminString
_CfprPkiCertRevokeCrlPollFilename_Object = MibTableColumn
cfprPkiCertRevokeCrlPollFilename = _CfprPkiCertRevokeCrlPollFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 8),
    _CfprPkiCertRevokeCrlPollFilename_Type()
)
cfprPkiCertRevokeCrlPollFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollFilename.setStatus("current")
_CfprPkiCertRevokeCrlPollPeriod_Type = Gauge32
_CfprPkiCertRevokeCrlPollPeriod_Object = MibTableColumn
cfprPkiCertRevokeCrlPollPeriod = _CfprPkiCertRevokeCrlPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 9),
    _CfprPkiCertRevokeCrlPollPeriod_Type()
)
cfprPkiCertRevokeCrlPollPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollPeriod.setStatus("current")
_CfprPkiCertRevokeCrlPollPort_Type = Gauge32
_CfprPkiCertRevokeCrlPollPort_Object = MibTableColumn
cfprPkiCertRevokeCrlPollPort = _CfprPkiCertRevokeCrlPollPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 10),
    _CfprPkiCertRevokeCrlPollPort_Type()
)
cfprPkiCertRevokeCrlPollPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollPort.setStatus("current")
_CfprPkiCertRevokeCrlPollProtocol_Type = CfprPkiTransportNoLocal
_CfprPkiCertRevokeCrlPollProtocol_Object = MibTableColumn
cfprPkiCertRevokeCrlPollProtocol = _CfprPkiCertRevokeCrlPollProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 11),
    _CfprPkiCertRevokeCrlPollProtocol_Type()
)
cfprPkiCertRevokeCrlPollProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollProtocol.setStatus("current")
_CfprPkiCertRevokeCrlPollPwd_Type = SnmpAdminString
_CfprPkiCertRevokeCrlPollPwd_Object = MibTableColumn
cfprPkiCertRevokeCrlPollPwd = _CfprPkiCertRevokeCrlPollPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 12),
    _CfprPkiCertRevokeCrlPollPwd_Type()
)
cfprPkiCertRevokeCrlPollPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollPwd.setStatus("current")
_CfprPkiCertRevokeCrlPollRemotePath_Type = SnmpAdminString
_CfprPkiCertRevokeCrlPollRemotePath_Object = MibTableColumn
cfprPkiCertRevokeCrlPollRemotePath = _CfprPkiCertRevokeCrlPollRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 13),
    _CfprPkiCertRevokeCrlPollRemotePath_Type()
)
cfprPkiCertRevokeCrlPollRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollRemotePath.setStatus("current")
_CfprPkiCertRevokeCrlPollServer_Type = SnmpAdminString
_CfprPkiCertRevokeCrlPollServer_Object = MibTableColumn
cfprPkiCertRevokeCrlPollServer = _CfprPkiCertRevokeCrlPollServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 14),
    _CfprPkiCertRevokeCrlPollServer_Type()
)
cfprPkiCertRevokeCrlPollServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollServer.setStatus("current")
_CfprPkiCertRevokeCrlPollUser_Type = SnmpAdminString
_CfprPkiCertRevokeCrlPollUser_Object = MibTableColumn
cfprPkiCertRevokeCrlPollUser = _CfprPkiCertRevokeCrlPollUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 15),
    _CfprPkiCertRevokeCrlPollUser_Type()
)
cfprPkiCertRevokeCrlPollUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeCrlPollUser.setStatus("current")
_CfprPkiCertRevokeDescr_Type = SnmpAdminString
_CfprPkiCertRevokeDescr_Object = MibTableColumn
cfprPkiCertRevokeDescr = _CfprPkiCertRevokeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 16),
    _CfprPkiCertRevokeDescr_Type()
)
cfprPkiCertRevokeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeDescr.setStatus("current")
_CfprPkiCertRevokeIntId_Type = SnmpAdminString
_CfprPkiCertRevokeIntId_Object = MibTableColumn
cfprPkiCertRevokeIntId = _CfprPkiCertRevokeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 17),
    _CfprPkiCertRevokeIntId_Type()
)
cfprPkiCertRevokeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeIntId.setStatus("current")
_CfprPkiCertRevokeName_Type = SnmpAdminString
_CfprPkiCertRevokeName_Object = MibTableColumn
cfprPkiCertRevokeName = _CfprPkiCertRevokeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 18),
    _CfprPkiCertRevokeName_Type()
)
cfprPkiCertRevokeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokeName.setStatus("current")
_CfprPkiCertRevokePolicyLevel_Type = Gauge32
_CfprPkiCertRevokePolicyLevel_Object = MibTableColumn
cfprPkiCertRevokePolicyLevel = _CfprPkiCertRevokePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 19),
    _CfprPkiCertRevokePolicyLevel_Type()
)
cfprPkiCertRevokePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokePolicyLevel.setStatus("current")
_CfprPkiCertRevokePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPkiCertRevokePolicyOwner_Object = MibTableColumn
cfprPkiCertRevokePolicyOwner = _CfprPkiCertRevokePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 8, 1, 20),
    _CfprPkiCertRevokePolicyOwner_Type()
)
cfprPkiCertRevokePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiCertRevokePolicyOwner.setStatus("current")
_CfprPkiImporterTable_Object = MibTable
cfprPkiImporterTable = _CfprPkiImporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9)
)
if mibBuilder.loadTexts:
    cfprPkiImporterTable.setStatus("current")
_CfprPkiImporterEntry_Object = MibTableRow
cfprPkiImporterEntry = _CfprPkiImporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1)
)
cfprPkiImporterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiImporterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiImporterEntry.setStatus("current")
_CfprPkiImporterInstanceId_Type = CfprManagedObjectId
_CfprPkiImporterInstanceId_Object = MibTableColumn
cfprPkiImporterInstanceId = _CfprPkiImporterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 1),
    _CfprPkiImporterInstanceId_Type()
)
cfprPkiImporterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiImporterInstanceId.setStatus("current")
_CfprPkiImporterDn_Type = CfprManagedObjectDn
_CfprPkiImporterDn_Object = MibTableColumn
cfprPkiImporterDn = _CfprPkiImporterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 2),
    _CfprPkiImporterDn_Type()
)
cfprPkiImporterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterDn.setStatus("current")
_CfprPkiImporterRn_Type = SnmpAdminString
_CfprPkiImporterRn_Object = MibTableColumn
cfprPkiImporterRn = _CfprPkiImporterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 3),
    _CfprPkiImporterRn_Type()
)
cfprPkiImporterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterRn.setStatus("current")
_CfprPkiImporterAdminState_Type = CfprPkiImportActivity
_CfprPkiImporterAdminState_Object = MibTableColumn
cfprPkiImporterAdminState = _CfprPkiImporterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 4),
    _CfprPkiImporterAdminState_Type()
)
cfprPkiImporterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterAdminState.setStatus("current")
_CfprPkiImporterCertStatus_Type = CfprPkiCertStatus
_CfprPkiImporterCertStatus_Object = MibTableColumn
cfprPkiImporterCertStatus = _CfprPkiImporterCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 5),
    _CfprPkiImporterCertStatus_Type()
)
cfprPkiImporterCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterCertStatus.setStatus("current")
_CfprPkiImporterCrlSize_Type = Gauge32
_CfprPkiImporterCrlSize_Object = MibTableColumn
cfprPkiImporterCrlSize = _CfprPkiImporterCrlSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 6),
    _CfprPkiImporterCrlSize_Type()
)
cfprPkiImporterCrlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterCrlSize.setStatus("current")
_CfprPkiImporterDescr_Type = SnmpAdminString
_CfprPkiImporterDescr_Object = MibTableColumn
cfprPkiImporterDescr = _CfprPkiImporterDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 7),
    _CfprPkiImporterDescr_Type()
)
cfprPkiImporterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterDescr.setStatus("current")
_CfprPkiImporterFileName_Type = SnmpAdminString
_CfprPkiImporterFileName_Object = MibTableColumn
cfprPkiImporterFileName = _CfprPkiImporterFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 8),
    _CfprPkiImporterFileName_Type()
)
cfprPkiImporterFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterFileName.setStatus("current")
_CfprPkiImporterIntId_Type = SnmpAdminString
_CfprPkiImporterIntId_Object = MibTableColumn
cfprPkiImporterIntId = _CfprPkiImporterIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 9),
    _CfprPkiImporterIntId_Type()
)
cfprPkiImporterIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterIntId.setStatus("current")
_CfprPkiImporterName_Type = SnmpAdminString
_CfprPkiImporterName_Object = MibTableColumn
cfprPkiImporterName = _CfprPkiImporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 10),
    _CfprPkiImporterName_Type()
)
cfprPkiImporterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterName.setStatus("current")
_CfprPkiImporterPolicyLevel_Type = Gauge32
_CfprPkiImporterPolicyLevel_Object = MibTableColumn
cfprPkiImporterPolicyLevel = _CfprPkiImporterPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 11),
    _CfprPkiImporterPolicyLevel_Type()
)
cfprPkiImporterPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterPolicyLevel.setStatus("current")
_CfprPkiImporterPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPkiImporterPolicyOwner_Object = MibTableColumn
cfprPkiImporterPolicyOwner = _CfprPkiImporterPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 12),
    _CfprPkiImporterPolicyOwner_Type()
)
cfprPkiImporterPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterPolicyOwner.setStatus("current")
_CfprPkiImporterPort_Type = Gauge32
_CfprPkiImporterPort_Object = MibTableColumn
cfprPkiImporterPort = _CfprPkiImporterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 13),
    _CfprPkiImporterPort_Type()
)
cfprPkiImporterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterPort.setStatus("current")
_CfprPkiImporterProtocol_Type = CfprPkiTransport
_CfprPkiImporterProtocol_Object = MibTableColumn
cfprPkiImporterProtocol = _CfprPkiImporterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 14),
    _CfprPkiImporterProtocol_Type()
)
cfprPkiImporterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterProtocol.setStatus("current")
_CfprPkiImporterPwd_Type = SnmpAdminString
_CfprPkiImporterPwd_Object = MibTableColumn
cfprPkiImporterPwd = _CfprPkiImporterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 15),
    _CfprPkiImporterPwd_Type()
)
cfprPkiImporterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterPwd.setStatus("current")
_CfprPkiImporterRemotePath_Type = SnmpAdminString
_CfprPkiImporterRemotePath_Object = MibTableColumn
cfprPkiImporterRemotePath = _CfprPkiImporterRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 16),
    _CfprPkiImporterRemotePath_Type()
)
cfprPkiImporterRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterRemotePath.setStatus("current")
_CfprPkiImporterServer_Type = SnmpAdminString
_CfprPkiImporterServer_Object = MibTableColumn
cfprPkiImporterServer = _CfprPkiImporterServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 17),
    _CfprPkiImporterServer_Type()
)
cfprPkiImporterServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterServer.setStatus("current")
_CfprPkiImporterTimeStamp_Type = DateAndTime
_CfprPkiImporterTimeStamp_Object = MibTableColumn
cfprPkiImporterTimeStamp = _CfprPkiImporterTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 18),
    _CfprPkiImporterTimeStamp_Type()
)
cfprPkiImporterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterTimeStamp.setStatus("current")
_CfprPkiImporterTransferRate_Type = Integer32
_CfprPkiImporterTransferRate_Object = MibTableColumn
cfprPkiImporterTransferRate = _CfprPkiImporterTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 19),
    _CfprPkiImporterTransferRate_Type()
)
cfprPkiImporterTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterTransferRate.setStatus("current")
_CfprPkiImporterTransferState_Type = CfprPkiTransferState
_CfprPkiImporterTransferState_Object = MibTableColumn
cfprPkiImporterTransferState = _CfprPkiImporterTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 20),
    _CfprPkiImporterTransferState_Type()
)
cfprPkiImporterTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterTransferState.setStatus("current")
_CfprPkiImporterUser_Type = SnmpAdminString
_CfprPkiImporterUser_Object = MibTableColumn
cfprPkiImporterUser = _CfprPkiImporterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 9, 1, 21),
    _CfprPkiImporterUser_Type()
)
cfprPkiImporterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiImporterUser.setStatus("current")
_CfprPkiTpAutoImportTable_Object = MibTable
cfprPkiTpAutoImportTable = _CfprPkiTpAutoImportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10)
)
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportTable.setStatus("current")
_CfprPkiTpAutoImportEntry_Object = MibTableRow
cfprPkiTpAutoImportEntry = _CfprPkiTpAutoImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1)
)
cfprPkiTpAutoImportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PKI-MIB", "cfprPkiTpAutoImportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportEntry.setStatus("current")
_CfprPkiTpAutoImportInstanceId_Type = CfprManagedObjectId
_CfprPkiTpAutoImportInstanceId_Object = MibTableColumn
cfprPkiTpAutoImportInstanceId = _CfprPkiTpAutoImportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 1),
    _CfprPkiTpAutoImportInstanceId_Type()
)
cfprPkiTpAutoImportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportInstanceId.setStatus("current")
_CfprPkiTpAutoImportDn_Type = CfprManagedObjectDn
_CfprPkiTpAutoImportDn_Object = MibTableColumn
cfprPkiTpAutoImportDn = _CfprPkiTpAutoImportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 2),
    _CfprPkiTpAutoImportDn_Type()
)
cfprPkiTpAutoImportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportDn.setStatus("current")
_CfprPkiTpAutoImportRn_Type = SnmpAdminString
_CfprPkiTpAutoImportRn_Object = MibTableColumn
cfprPkiTpAutoImportRn = _CfprPkiTpAutoImportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 3),
    _CfprPkiTpAutoImportRn_Type()
)
cfprPkiTpAutoImportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportRn.setStatus("current")
_CfprPkiTpAutoImportCertStatus_Type = CfprPkiCertStatus
_CfprPkiTpAutoImportCertStatus_Object = MibTableColumn
cfprPkiTpAutoImportCertStatus = _CfprPkiTpAutoImportCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 4),
    _CfprPkiTpAutoImportCertStatus_Type()
)
cfprPkiTpAutoImportCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportCertStatus.setStatus("current")
_CfprPkiTpAutoImportDayRun_Type = TruthValue
_CfprPkiTpAutoImportDayRun_Object = MibTableColumn
cfprPkiTpAutoImportDayRun = _CfprPkiTpAutoImportDayRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 5),
    _CfprPkiTpAutoImportDayRun_Type()
)
cfprPkiTpAutoImportDayRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportDayRun.setStatus("current")
_CfprPkiTpAutoImportDescr_Type = SnmpAdminString
_CfprPkiTpAutoImportDescr_Object = MibTableColumn
cfprPkiTpAutoImportDescr = _CfprPkiTpAutoImportDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 6),
    _CfprPkiTpAutoImportDescr_Type()
)
cfprPkiTpAutoImportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportDescr.setStatus("current")
_CfprPkiTpAutoImportImportControlStatus_Type = CfprPkiTpAutoImportImportControlStatus
_CfprPkiTpAutoImportImportControlStatus_Object = MibTableColumn
cfprPkiTpAutoImportImportControlStatus = _CfprPkiTpAutoImportImportControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 7),
    _CfprPkiTpAutoImportImportControlStatus_Type()
)
cfprPkiTpAutoImportImportControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportImportControlStatus.setStatus("current")
_CfprPkiTpAutoImportImportStatus_Type = TruthValue
_CfprPkiTpAutoImportImportStatus_Object = MibTableColumn
cfprPkiTpAutoImportImportStatus = _CfprPkiTpAutoImportImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 8),
    _CfprPkiTpAutoImportImportStatus_Type()
)
cfprPkiTpAutoImportImportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportImportStatus.setStatus("current")
_CfprPkiTpAutoImportImportTimeHour_Type = Gauge32
_CfprPkiTpAutoImportImportTimeHour_Object = MibTableColumn
cfprPkiTpAutoImportImportTimeHour = _CfprPkiTpAutoImportImportTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 9),
    _CfprPkiTpAutoImportImportTimeHour_Type()
)
cfprPkiTpAutoImportImportTimeHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportImportTimeHour.setStatus("current")
_CfprPkiTpAutoImportImportTimeMin_Type = Gauge32
_CfprPkiTpAutoImportImportTimeMin_Object = MibTableColumn
cfprPkiTpAutoImportImportTimeMin = _CfprPkiTpAutoImportImportTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 10),
    _CfprPkiTpAutoImportImportTimeMin_Type()
)
cfprPkiTpAutoImportImportTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportImportTimeMin.setStatus("current")
_CfprPkiTpAutoImportImportUrl_Type = SnmpAdminString
_CfprPkiTpAutoImportImportUrl_Object = MibTableColumn
cfprPkiTpAutoImportImportUrl = _CfprPkiTpAutoImportImportUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 11),
    _CfprPkiTpAutoImportImportUrl_Type()
)
cfprPkiTpAutoImportImportUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportImportUrl.setStatus("current")
_CfprPkiTpAutoImportIntId_Type = SnmpAdminString
_CfprPkiTpAutoImportIntId_Object = MibTableColumn
cfprPkiTpAutoImportIntId = _CfprPkiTpAutoImportIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 12),
    _CfprPkiTpAutoImportIntId_Type()
)
cfprPkiTpAutoImportIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportIntId.setStatus("current")
_CfprPkiTpAutoImportName_Type = SnmpAdminString
_CfprPkiTpAutoImportName_Object = MibTableColumn
cfprPkiTpAutoImportName = _CfprPkiTpAutoImportName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 13),
    _CfprPkiTpAutoImportName_Type()
)
cfprPkiTpAutoImportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportName.setStatus("current")
_CfprPkiTpAutoImportNumExtractedTpAutoImport_Type = Gauge32
_CfprPkiTpAutoImportNumExtractedTpAutoImport_Object = MibTableColumn
cfprPkiTpAutoImportNumExtractedTpAutoImport = _CfprPkiTpAutoImportNumExtractedTpAutoImport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 14),
    _CfprPkiTpAutoImportNumExtractedTpAutoImport_Type()
)
cfprPkiTpAutoImportNumExtractedTpAutoImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportNumExtractedTpAutoImport.setStatus("current")
_CfprPkiTpAutoImportNumTpAutoImport_Type = Gauge32
_CfprPkiTpAutoImportNumTpAutoImport_Object = MibTableColumn
cfprPkiTpAutoImportNumTpAutoImport = _CfprPkiTpAutoImportNumTpAutoImport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 15),
    _CfprPkiTpAutoImportNumTpAutoImport_Type()
)
cfprPkiTpAutoImportNumTpAutoImport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportNumTpAutoImport.setStatus("current")
_CfprPkiTpAutoImportPolicyLevel_Type = Gauge32
_CfprPkiTpAutoImportPolicyLevel_Object = MibTableColumn
cfprPkiTpAutoImportPolicyLevel = _CfprPkiTpAutoImportPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 16),
    _CfprPkiTpAutoImportPolicyLevel_Type()
)
cfprPkiTpAutoImportPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportPolicyLevel.setStatus("current")
_CfprPkiTpAutoImportPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPkiTpAutoImportPolicyOwner_Object = MibTableColumn
cfprPkiTpAutoImportPolicyOwner = _CfprPkiTpAutoImportPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 17),
    _CfprPkiTpAutoImportPolicyOwner_Type()
)
cfprPkiTpAutoImportPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportPolicyOwner.setStatus("current")
_CfprPkiTpAutoImportRetryCount_Type = Gauge32
_CfprPkiTpAutoImportRetryCount_Object = MibTableColumn
cfprPkiTpAutoImportRetryCount = _CfprPkiTpAutoImportRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 18),
    _CfprPkiTpAutoImportRetryCount_Type()
)
cfprPkiTpAutoImportRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportRetryCount.setStatus("current")
_CfprPkiTpAutoImportRetryDelay_Type = Gauge32
_CfprPkiTpAutoImportRetryDelay_Object = MibTableColumn
cfprPkiTpAutoImportRetryDelay = _CfprPkiTpAutoImportRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 19),
    _CfprPkiTpAutoImportRetryDelay_Type()
)
cfprPkiTpAutoImportRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportRetryDelay.setStatus("current")
_CfprPkiTpAutoImportTriggerRun_Type = TruthValue
_CfprPkiTpAutoImportTriggerRun_Object = MibTableColumn
cfprPkiTpAutoImportTriggerRun = _CfprPkiTpAutoImportTriggerRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 61, 10, 1, 20),
    _CfprPkiTpAutoImportTriggerRun_Type()
)
cfprPkiTpAutoImportTriggerRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPkiTpAutoImportTriggerRun.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-PKI-MIB",
    **{"cfprPkiObjects": cfprPkiObjects,
       "cfprPkiCertReqTable": cfprPkiCertReqTable,
       "cfprPkiCertReqEntry": cfprPkiCertReqEntry,
       "cfprPkiCertReqInstanceId": cfprPkiCertReqInstanceId,
       "cfprPkiCertReqDn": cfprPkiCertReqDn,
       "cfprPkiCertReqRn": cfprPkiCertReqRn,
       "cfprPkiCertReqCountry": cfprPkiCertReqCountry,
       "cfprPkiCertReqDns": cfprPkiCertReqDns,
       "cfprPkiCertReqEmail": cfprPkiCertReqEmail,
       "cfprPkiCertReqIp": cfprPkiCertReqIp,
       "cfprPkiCertReqIpA": cfprPkiCertReqIpA,
       "cfprPkiCertReqIpB": cfprPkiCertReqIpB,
       "cfprPkiCertReqIpv6": cfprPkiCertReqIpv6,
       "cfprPkiCertReqIpv6A": cfprPkiCertReqIpv6A,
       "cfprPkiCertReqIpv6B": cfprPkiCertReqIpv6B,
       "cfprPkiCertReqLocality": cfprPkiCertReqLocality,
       "cfprPkiCertReqOrgName": cfprPkiCertReqOrgName,
       "cfprPkiCertReqOrgUnitName": cfprPkiCertReqOrgUnitName,
       "cfprPkiCertReqPwd": cfprPkiCertReqPwd,
       "cfprPkiCertReqReq": cfprPkiCertReqReq,
       "cfprPkiCertReqState": cfprPkiCertReqState,
       "cfprPkiCertReqSubjName": cfprPkiCertReqSubjName,
       "cfprPkiEpTable": cfprPkiEpTable,
       "cfprPkiEpEntry": cfprPkiEpEntry,
       "cfprPkiEpInstanceId": cfprPkiEpInstanceId,
       "cfprPkiEpDn": cfprPkiEpDn,
       "cfprPkiEpRn": cfprPkiEpRn,
       "cfprPkiEpDescr": cfprPkiEpDescr,
       "cfprPkiEpFsmDescr": cfprPkiEpFsmDescr,
       "cfprPkiEpFsmPrev": cfprPkiEpFsmPrev,
       "cfprPkiEpFsmProgr": cfprPkiEpFsmProgr,
       "cfprPkiEpFsmRmtInvErrCode": cfprPkiEpFsmRmtInvErrCode,
       "cfprPkiEpFsmRmtInvErrDescr": cfprPkiEpFsmRmtInvErrDescr,
       "cfprPkiEpFsmRmtInvRslt": cfprPkiEpFsmRmtInvRslt,
       "cfprPkiEpFsmStageDescr": cfprPkiEpFsmStageDescr,
       "cfprPkiEpFsmStamp": cfprPkiEpFsmStamp,
       "cfprPkiEpFsmStatus": cfprPkiEpFsmStatus,
       "cfprPkiEpFsmTry": cfprPkiEpFsmTry,
       "cfprPkiEpIntId": cfprPkiEpIntId,
       "cfprPkiEpName": cfprPkiEpName,
       "cfprPkiEpPolicyLevel": cfprPkiEpPolicyLevel,
       "cfprPkiEpPolicyOwner": cfprPkiEpPolicyOwner,
       "cfprPkiEpFsmTable": cfprPkiEpFsmTable,
       "cfprPkiEpFsmEntry": cfprPkiEpFsmEntry,
       "cfprPkiEpFsmInstanceId": cfprPkiEpFsmInstanceId,
       "cfprPkiEpFsmDn": cfprPkiEpFsmDn,
       "cfprPkiEpFsmRn": cfprPkiEpFsmRn,
       "cfprPkiEpFsmCompletionTime": cfprPkiEpFsmCompletionTime,
       "cfprPkiEpFsmCurrentFsm": cfprPkiEpFsmCurrentFsm,
       "cfprPkiEpFsmDescrData": cfprPkiEpFsmDescrData,
       "cfprPkiEpFsmFsmStatus": cfprPkiEpFsmFsmStatus,
       "cfprPkiEpFsmProgress": cfprPkiEpFsmProgress,
       "cfprPkiEpFsmRmtErrCode": cfprPkiEpFsmRmtErrCode,
       "cfprPkiEpFsmRmtErrDescr": cfprPkiEpFsmRmtErrDescr,
       "cfprPkiEpFsmRmtRslt": cfprPkiEpFsmRmtRslt,
       "cfprPkiEpFsmStageTable": cfprPkiEpFsmStageTable,
       "cfprPkiEpFsmStageEntry": cfprPkiEpFsmStageEntry,
       "cfprPkiEpFsmStageInstanceId": cfprPkiEpFsmStageInstanceId,
       "cfprPkiEpFsmStageDn": cfprPkiEpFsmStageDn,
       "cfprPkiEpFsmStageRn": cfprPkiEpFsmStageRn,
       "cfprPkiEpFsmStageDescrData": cfprPkiEpFsmStageDescrData,
       "cfprPkiEpFsmStageLastUpdateTime": cfprPkiEpFsmStageLastUpdateTime,
       "cfprPkiEpFsmStageName": cfprPkiEpFsmStageName,
       "cfprPkiEpFsmStageOrder": cfprPkiEpFsmStageOrder,
       "cfprPkiEpFsmStageRetry": cfprPkiEpFsmStageRetry,
       "cfprPkiEpFsmStageStageStatus": cfprPkiEpFsmStageStageStatus,
       "cfprPkiEpFsmTaskTable": cfprPkiEpFsmTaskTable,
       "cfprPkiEpFsmTaskEntry": cfprPkiEpFsmTaskEntry,
       "cfprPkiEpFsmTaskInstanceId": cfprPkiEpFsmTaskInstanceId,
       "cfprPkiEpFsmTaskDn": cfprPkiEpFsmTaskDn,
       "cfprPkiEpFsmTaskRn": cfprPkiEpFsmTaskRn,
       "cfprPkiEpFsmTaskCompletion": cfprPkiEpFsmTaskCompletion,
       "cfprPkiEpFsmTaskFlags": cfprPkiEpFsmTaskFlags,
       "cfprPkiEpFsmTaskItem": cfprPkiEpFsmTaskItem,
       "cfprPkiEpFsmTaskSeqId": cfprPkiEpFsmTaskSeqId,
       "cfprPkiKeyRingTable": cfprPkiKeyRingTable,
       "cfprPkiKeyRingEntry": cfprPkiKeyRingEntry,
       "cfprPkiKeyRingInstanceId": cfprPkiKeyRingInstanceId,
       "cfprPkiKeyRingDn": cfprPkiKeyRingDn,
       "cfprPkiKeyRingRn": cfprPkiKeyRingRn,
       "cfprPkiKeyRingAdminState": cfprPkiKeyRingAdminState,
       "cfprPkiKeyRingCert": cfprPkiKeyRingCert,
       "cfprPkiKeyRingCertStatus": cfprPkiKeyRingCertStatus,
       "cfprPkiKeyRingConfigState": cfprPkiKeyRingConfigState,
       "cfprPkiKeyRingConfigStatusMessage": cfprPkiKeyRingConfigStatusMessage,
       "cfprPkiKeyRingDescr": cfprPkiKeyRingDescr,
       "cfprPkiKeyRingIntId": cfprPkiKeyRingIntId,
       "cfprPkiKeyRingKey": cfprPkiKeyRingKey,
       "cfprPkiKeyRingModulus": cfprPkiKeyRingModulus,
       "cfprPkiKeyRingName": cfprPkiKeyRingName,
       "cfprPkiKeyRingPolicyLevel": cfprPkiKeyRingPolicyLevel,
       "cfprPkiKeyRingPolicyOwner": cfprPkiKeyRingPolicyOwner,
       "cfprPkiKeyRingRegen": cfprPkiKeyRingRegen,
       "cfprPkiKeyRingTp": cfprPkiKeyRingTp,
       "cfprPkiKeyRingZeroized": cfprPkiKeyRingZeroized,
       "cfprPkiKeyRingEc": cfprPkiKeyRingEc,
       "cfprPkiKeyRingFqdnEnforce": cfprPkiKeyRingFqdnEnforce,
       "cfprPkiKeyRingType": cfprPkiKeyRingType,
       "cfprPkiTPTable": cfprPkiTPTable,
       "cfprPkiTPEntry": cfprPkiTPEntry,
       "cfprPkiTPInstanceId": cfprPkiTPInstanceId,
       "cfprPkiTPDn": cfprPkiTPDn,
       "cfprPkiTPRn": cfprPkiTPRn,
       "cfprPkiTPCertChain": cfprPkiTPCertChain,
       "cfprPkiTPCertStatus": cfprPkiTPCertStatus,
       "cfprPkiTPDescr": cfprPkiTPDescr,
       "cfprPkiTPFp": cfprPkiTPFp,
       "cfprPkiTPIntId": cfprPkiTPIntId,
       "cfprPkiTPName": cfprPkiTPName,
       "cfprPkiTPNumCerts": cfprPkiTPNumCerts,
       "cfprPkiTPPolicyLevel": cfprPkiTPPolicyLevel,
       "cfprPkiTPPolicyOwner": cfprPkiTPPolicyOwner,
       "cfprPkiTPCertChainDecode": cfprPkiTPCertChainDecode,
       "cfprPkiCertRevokeTable": cfprPkiCertRevokeTable,
       "cfprPkiCertRevokeEntry": cfprPkiCertRevokeEntry,
       "cfprPkiCertRevokeInstanceId": cfprPkiCertRevokeInstanceId,
       "cfprPkiCertRevokeDn": cfprPkiCertRevokeDn,
       "cfprPkiCertRevokeRn": cfprPkiCertRevokeRn,
       "cfprPkiCertRevokeCertRevokeMethod": cfprPkiCertRevokeCertRevokeMethod,
       "cfprPkiCertRevokeCertStatus": cfprPkiCertRevokeCertStatus,
       "cfprPkiCertRevokeCrl": cfprPkiCertRevokeCrl,
       "cfprPkiCertRevokeCrlPollCount": cfprPkiCertRevokeCrlPollCount,
       "cfprPkiCertRevokeCrlPollFilename": cfprPkiCertRevokeCrlPollFilename,
       "cfprPkiCertRevokeCrlPollPeriod": cfprPkiCertRevokeCrlPollPeriod,
       "cfprPkiCertRevokeCrlPollPort": cfprPkiCertRevokeCrlPollPort,
       "cfprPkiCertRevokeCrlPollProtocol": cfprPkiCertRevokeCrlPollProtocol,
       "cfprPkiCertRevokeCrlPollPwd": cfprPkiCertRevokeCrlPollPwd,
       "cfprPkiCertRevokeCrlPollRemotePath": cfprPkiCertRevokeCrlPollRemotePath,
       "cfprPkiCertRevokeCrlPollServer": cfprPkiCertRevokeCrlPollServer,
       "cfprPkiCertRevokeCrlPollUser": cfprPkiCertRevokeCrlPollUser,
       "cfprPkiCertRevokeDescr": cfprPkiCertRevokeDescr,
       "cfprPkiCertRevokeIntId": cfprPkiCertRevokeIntId,
       "cfprPkiCertRevokeName": cfprPkiCertRevokeName,
       "cfprPkiCertRevokePolicyLevel": cfprPkiCertRevokePolicyLevel,
       "cfprPkiCertRevokePolicyOwner": cfprPkiCertRevokePolicyOwner,
       "cfprPkiImporterTable": cfprPkiImporterTable,
       "cfprPkiImporterEntry": cfprPkiImporterEntry,
       "cfprPkiImporterInstanceId": cfprPkiImporterInstanceId,
       "cfprPkiImporterDn": cfprPkiImporterDn,
       "cfprPkiImporterRn": cfprPkiImporterRn,
       "cfprPkiImporterAdminState": cfprPkiImporterAdminState,
       "cfprPkiImporterCertStatus": cfprPkiImporterCertStatus,
       "cfprPkiImporterCrlSize": cfprPkiImporterCrlSize,
       "cfprPkiImporterDescr": cfprPkiImporterDescr,
       "cfprPkiImporterFileName": cfprPkiImporterFileName,
       "cfprPkiImporterIntId": cfprPkiImporterIntId,
       "cfprPkiImporterName": cfprPkiImporterName,
       "cfprPkiImporterPolicyLevel": cfprPkiImporterPolicyLevel,
       "cfprPkiImporterPolicyOwner": cfprPkiImporterPolicyOwner,
       "cfprPkiImporterPort": cfprPkiImporterPort,
       "cfprPkiImporterProtocol": cfprPkiImporterProtocol,
       "cfprPkiImporterPwd": cfprPkiImporterPwd,
       "cfprPkiImporterRemotePath": cfprPkiImporterRemotePath,
       "cfprPkiImporterServer": cfprPkiImporterServer,
       "cfprPkiImporterTimeStamp": cfprPkiImporterTimeStamp,
       "cfprPkiImporterTransferRate": cfprPkiImporterTransferRate,
       "cfprPkiImporterTransferState": cfprPkiImporterTransferState,
       "cfprPkiImporterUser": cfprPkiImporterUser,
       "cfprPkiTpAutoImportTable": cfprPkiTpAutoImportTable,
       "cfprPkiTpAutoImportEntry": cfprPkiTpAutoImportEntry,
       "cfprPkiTpAutoImportInstanceId": cfprPkiTpAutoImportInstanceId,
       "cfprPkiTpAutoImportDn": cfprPkiTpAutoImportDn,
       "cfprPkiTpAutoImportRn": cfprPkiTpAutoImportRn,
       "cfprPkiTpAutoImportCertStatus": cfprPkiTpAutoImportCertStatus,
       "cfprPkiTpAutoImportDayRun": cfprPkiTpAutoImportDayRun,
       "cfprPkiTpAutoImportDescr": cfprPkiTpAutoImportDescr,
       "cfprPkiTpAutoImportImportControlStatus": cfprPkiTpAutoImportImportControlStatus,
       "cfprPkiTpAutoImportImportStatus": cfprPkiTpAutoImportImportStatus,
       "cfprPkiTpAutoImportImportTimeHour": cfprPkiTpAutoImportImportTimeHour,
       "cfprPkiTpAutoImportImportTimeMin": cfprPkiTpAutoImportImportTimeMin,
       "cfprPkiTpAutoImportImportUrl": cfprPkiTpAutoImportImportUrl,
       "cfprPkiTpAutoImportIntId": cfprPkiTpAutoImportIntId,
       "cfprPkiTpAutoImportName": cfprPkiTpAutoImportName,
       "cfprPkiTpAutoImportNumExtractedTpAutoImport": cfprPkiTpAutoImportNumExtractedTpAutoImport,
       "cfprPkiTpAutoImportNumTpAutoImport": cfprPkiTpAutoImportNumTpAutoImport,
       "cfprPkiTpAutoImportPolicyLevel": cfprPkiTpAutoImportPolicyLevel,
       "cfprPkiTpAutoImportPolicyOwner": cfprPkiTpAutoImportPolicyOwner,
       "cfprPkiTpAutoImportRetryCount": cfprPkiTpAutoImportRetryCount,
       "cfprPkiTpAutoImportRetryDelay": cfprPkiTpAutoImportRetryDelay,
       "cfprPkiTpAutoImportTriggerRun": cfprPkiTpAutoImportTriggerRun}
)
