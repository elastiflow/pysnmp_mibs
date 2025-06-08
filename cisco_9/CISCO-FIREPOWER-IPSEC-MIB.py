# SNMP MIB module (CISCO-FIREPOWER-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IPSEC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprIpsecAuthType,
 CfprIpsecCommand,
 CfprIpsecConfigState,
 CfprIpsecConnState,
 CfprIpsecEpFsmCurrentFsm,
 CfprIpsecEpFsmStageName,
 CfprIpsecEpFsmTaskItem,
 CfprIpsecEspMode,
 CfprIpsecFqdnEnforceType,
 CfprIpsecRevokePolicy,
 CfprIpsecStatsType,
 CfprPkiType,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprIpsecAuthType",
    "CfprIpsecCommand",
    "CfprIpsecConfigState",
    "CfprIpsecConnState",
    "CfprIpsecEpFsmCurrentFsm",
    "CfprIpsecEpFsmStageName",
    "CfprIpsecEpFsmTaskItem",
    "CfprIpsecEspMode",
    "CfprIpsecFqdnEnforceType",
    "CfprIpsecRevokePolicy",
    "CfprIpsecStatsType",
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

cfprIpsecObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprIpsecAuthorityTable_Object = MibTable
cfprIpsecAuthorityTable = _CfprIpsecAuthorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1)
)
if mibBuilder.loadTexts:
    cfprIpsecAuthorityTable.setStatus("current")
_CfprIpsecAuthorityEntry_Object = MibTableRow
cfprIpsecAuthorityEntry = _CfprIpsecAuthorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1)
)
cfprIpsecAuthorityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecAuthorityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecAuthorityEntry.setStatus("current")
_CfprIpsecAuthorityInstanceId_Type = CfprManagedObjectId
_CfprIpsecAuthorityInstanceId_Object = MibTableColumn
cfprIpsecAuthorityInstanceId = _CfprIpsecAuthorityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 1),
    _CfprIpsecAuthorityInstanceId_Type()
)
cfprIpsecAuthorityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityInstanceId.setStatus("current")
_CfprIpsecAuthorityDn_Type = CfprManagedObjectDn
_CfprIpsecAuthorityDn_Object = MibTableColumn
cfprIpsecAuthorityDn = _CfprIpsecAuthorityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 2),
    _CfprIpsecAuthorityDn_Type()
)
cfprIpsecAuthorityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityDn.setStatus("current")
_CfprIpsecAuthorityRn_Type = SnmpAdminString
_CfprIpsecAuthorityRn_Object = MibTableColumn
cfprIpsecAuthorityRn = _CfprIpsecAuthorityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 3),
    _CfprIpsecAuthorityRn_Type()
)
cfprIpsecAuthorityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityRn.setStatus("current")
_CfprIpsecAuthorityConfigState_Type = CfprIpsecConfigState
_CfprIpsecAuthorityConfigState_Object = MibTableColumn
cfprIpsecAuthorityConfigState = _CfprIpsecAuthorityConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 4),
    _CfprIpsecAuthorityConfigState_Type()
)
cfprIpsecAuthorityConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityConfigState.setStatus("current")
_CfprIpsecAuthorityCrlUris_Type = SnmpAdminString
_CfprIpsecAuthorityCrlUris_Object = MibTableColumn
cfprIpsecAuthorityCrlUris = _CfprIpsecAuthorityCrlUris_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 5),
    _CfprIpsecAuthorityCrlUris_Type()
)
cfprIpsecAuthorityCrlUris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityCrlUris.setStatus("current")
_CfprIpsecAuthorityDescr_Type = SnmpAdminString
_CfprIpsecAuthorityDescr_Object = MibTableColumn
cfprIpsecAuthorityDescr = _CfprIpsecAuthorityDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 6),
    _CfprIpsecAuthorityDescr_Type()
)
cfprIpsecAuthorityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityDescr.setStatus("current")
_CfprIpsecAuthorityIntId_Type = SnmpAdminString
_CfprIpsecAuthorityIntId_Object = MibTableColumn
cfprIpsecAuthorityIntId = _CfprIpsecAuthorityIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 7),
    _CfprIpsecAuthorityIntId_Type()
)
cfprIpsecAuthorityIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityIntId.setStatus("current")
_CfprIpsecAuthorityName_Type = SnmpAdminString
_CfprIpsecAuthorityName_Object = MibTableColumn
cfprIpsecAuthorityName = _CfprIpsecAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 8),
    _CfprIpsecAuthorityName_Type()
)
cfprIpsecAuthorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityName.setStatus("current")
_CfprIpsecAuthorityNumCerts_Type = Gauge32
_CfprIpsecAuthorityNumCerts_Object = MibTableColumn
cfprIpsecAuthorityNumCerts = _CfprIpsecAuthorityNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 9),
    _CfprIpsecAuthorityNumCerts_Type()
)
cfprIpsecAuthorityNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityNumCerts.setStatus("current")
_CfprIpsecAuthorityOcspUris_Type = SnmpAdminString
_CfprIpsecAuthorityOcspUris_Object = MibTableColumn
cfprIpsecAuthorityOcspUris = _CfprIpsecAuthorityOcspUris_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 10),
    _CfprIpsecAuthorityOcspUris_Type()
)
cfprIpsecAuthorityOcspUris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityOcspUris.setStatus("current")
_CfprIpsecAuthorityPolicyLevel_Type = Gauge32
_CfprIpsecAuthorityPolicyLevel_Object = MibTableColumn
cfprIpsecAuthorityPolicyLevel = _CfprIpsecAuthorityPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 11),
    _CfprIpsecAuthorityPolicyLevel_Type()
)
cfprIpsecAuthorityPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityPolicyLevel.setStatus("current")
_CfprIpsecAuthorityPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprIpsecAuthorityPolicyOwner_Object = MibTableColumn
cfprIpsecAuthorityPolicyOwner = _CfprIpsecAuthorityPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 12),
    _CfprIpsecAuthorityPolicyOwner_Type()
)
cfprIpsecAuthorityPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityPolicyOwner.setStatus("current")
_CfprIpsecAuthorityTpName_Type = SnmpAdminString
_CfprIpsecAuthorityTpName_Object = MibTableColumn
cfprIpsecAuthorityTpName = _CfprIpsecAuthorityTpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 1, 1, 13),
    _CfprIpsecAuthorityTpName_Type()
)
cfprIpsecAuthorityTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecAuthorityTpName.setStatus("current")
_CfprIpsecConnectionTable_Object = MibTable
cfprIpsecConnectionTable = _CfprIpsecConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2)
)
if mibBuilder.loadTexts:
    cfprIpsecConnectionTable.setStatus("current")
_CfprIpsecConnectionEntry_Object = MibTableRow
cfprIpsecConnectionEntry = _CfprIpsecConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1)
)
cfprIpsecConnectionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecConnectionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecConnectionEntry.setStatus("current")
_CfprIpsecConnectionInstanceId_Type = CfprManagedObjectId
_CfprIpsecConnectionInstanceId_Object = MibTableColumn
cfprIpsecConnectionInstanceId = _CfprIpsecConnectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 1),
    _CfprIpsecConnectionInstanceId_Type()
)
cfprIpsecConnectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecConnectionInstanceId.setStatus("current")
_CfprIpsecConnectionDn_Type = CfprManagedObjectDn
_CfprIpsecConnectionDn_Object = MibTableColumn
cfprIpsecConnectionDn = _CfprIpsecConnectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 2),
    _CfprIpsecConnectionDn_Type()
)
cfprIpsecConnectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionDn.setStatus("current")
_CfprIpsecConnectionRn_Type = SnmpAdminString
_CfprIpsecConnectionRn_Object = MibTableColumn
cfprIpsecConnectionRn = _CfprIpsecConnectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 3),
    _CfprIpsecConnectionRn_Type()
)
cfprIpsecConnectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionRn.setStatus("current")
_CfprIpsecConnectionAdminState_Type = CfprIpsecConnState
_CfprIpsecConnectionAdminState_Object = MibTableColumn
cfprIpsecConnectionAdminState = _CfprIpsecConnectionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 4),
    _CfprIpsecConnectionAdminState_Type()
)
cfprIpsecConnectionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionAdminState.setStatus("current")
_CfprIpsecConnectionAuth_Type = CfprIpsecAuthType
_CfprIpsecConnectionAuth_Object = MibTableColumn
cfprIpsecConnectionAuth = _CfprIpsecConnectionAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 5),
    _CfprIpsecConnectionAuth_Type()
)
cfprIpsecConnectionAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionAuth.setStatus("current")
_CfprIpsecConnectionConfigState_Type = CfprIpsecConfigState
_CfprIpsecConnectionConfigState_Object = MibTableColumn
cfprIpsecConnectionConfigState = _CfprIpsecConnectionConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 6),
    _CfprIpsecConnectionConfigState_Type()
)
cfprIpsecConnectionConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionConfigState.setStatus("current")
_CfprIpsecConnectionDescr_Type = SnmpAdminString
_CfprIpsecConnectionDescr_Object = MibTableColumn
cfprIpsecConnectionDescr = _CfprIpsecConnectionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 7),
    _CfprIpsecConnectionDescr_Type()
)
cfprIpsecConnectionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionDescr.setStatus("current")
_CfprIpsecConnectionEspMode_Type = CfprIpsecEspMode
_CfprIpsecConnectionEspMode_Object = MibTableColumn
cfprIpsecConnectionEspMode = _CfprIpsecConnectionEspMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 8),
    _CfprIpsecConnectionEspMode_Type()
)
cfprIpsecConnectionEspMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionEspMode.setStatus("current")
_CfprIpsecConnectionEspProposals_Type = SnmpAdminString
_CfprIpsecConnectionEspProposals_Object = MibTableColumn
cfprIpsecConnectionEspProposals = _CfprIpsecConnectionEspProposals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 9),
    _CfprIpsecConnectionEspProposals_Type()
)
cfprIpsecConnectionEspProposals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionEspProposals.setStatus("current")
_CfprIpsecConnectionEspRekeyTime_Type = Gauge32
_CfprIpsecConnectionEspRekeyTime_Object = MibTableColumn
cfprIpsecConnectionEspRekeyTime = _CfprIpsecConnectionEspRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 10),
    _CfprIpsecConnectionEspRekeyTime_Type()
)
cfprIpsecConnectionEspRekeyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionEspRekeyTime.setStatus("current")
_CfprIpsecConnectionIkeRekeyTime_Type = Gauge32
_CfprIpsecConnectionIkeRekeyTime_Object = MibTableColumn
cfprIpsecConnectionIkeRekeyTime = _CfprIpsecConnectionIkeRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 11),
    _CfprIpsecConnectionIkeRekeyTime_Type()
)
cfprIpsecConnectionIkeRekeyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionIkeRekeyTime.setStatus("current")
_CfprIpsecConnectionIkeVer_Type = Gauge32
_CfprIpsecConnectionIkeVer_Object = MibTableColumn
cfprIpsecConnectionIkeVer = _CfprIpsecConnectionIkeVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 12),
    _CfprIpsecConnectionIkeVer_Type()
)
cfprIpsecConnectionIkeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionIkeVer.setStatus("current")
_CfprIpsecConnectionInactivity_Type = Gauge32
_CfprIpsecConnectionInactivity_Object = MibTableColumn
cfprIpsecConnectionInactivity = _CfprIpsecConnectionInactivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 13),
    _CfprIpsecConnectionInactivity_Type()
)
cfprIpsecConnectionInactivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionInactivity.setStatus("current")
_CfprIpsecConnectionIntId_Type = SnmpAdminString
_CfprIpsecConnectionIntId_Object = MibTableColumn
cfprIpsecConnectionIntId = _CfprIpsecConnectionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 14),
    _CfprIpsecConnectionIntId_Type()
)
cfprIpsecConnectionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionIntId.setStatus("current")
_CfprIpsecConnectionKeyingtries_Type = Gauge32
_CfprIpsecConnectionKeyingtries_Object = MibTableColumn
cfprIpsecConnectionKeyingtries = _CfprIpsecConnectionKeyingtries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 15),
    _CfprIpsecConnectionKeyingtries_Type()
)
cfprIpsecConnectionKeyingtries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionKeyingtries.setStatus("current")
_CfprIpsecConnectionKeyring_Type = SnmpAdminString
_CfprIpsecConnectionKeyring_Object = MibTableColumn
cfprIpsecConnectionKeyring = _CfprIpsecConnectionKeyring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 16),
    _CfprIpsecConnectionKeyring_Type()
)
cfprIpsecConnectionKeyring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionKeyring.setStatus("current")
_CfprIpsecConnectionLocalAddrs_Type = SnmpAdminString
_CfprIpsecConnectionLocalAddrs_Object = MibTableColumn
cfprIpsecConnectionLocalAddrs = _CfprIpsecConnectionLocalAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 17),
    _CfprIpsecConnectionLocalAddrs_Type()
)
cfprIpsecConnectionLocalAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionLocalAddrs.setStatus("current")
_CfprIpsecConnectionLocalIkeIdent_Type = SnmpAdminString
_CfprIpsecConnectionLocalIkeIdent_Object = MibTableColumn
cfprIpsecConnectionLocalIkeIdent = _CfprIpsecConnectionLocalIkeIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 18),
    _CfprIpsecConnectionLocalIkeIdent_Type()
)
cfprIpsecConnectionLocalIkeIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionLocalIkeIdent.setStatus("current")
_CfprIpsecConnectionLocalTs_Type = SnmpAdminString
_CfprIpsecConnectionLocalTs_Object = MibTableColumn
cfprIpsecConnectionLocalTs = _CfprIpsecConnectionLocalTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 19),
    _CfprIpsecConnectionLocalTs_Type()
)
cfprIpsecConnectionLocalTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionLocalTs.setStatus("current")
_CfprIpsecConnectionName_Type = SnmpAdminString
_CfprIpsecConnectionName_Object = MibTableColumn
cfprIpsecConnectionName = _CfprIpsecConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 20),
    _CfprIpsecConnectionName_Type()
)
cfprIpsecConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionName.setStatus("current")
_CfprIpsecConnectionNumCerts_Type = Gauge32
_CfprIpsecConnectionNumCerts_Object = MibTableColumn
cfprIpsecConnectionNumCerts = _CfprIpsecConnectionNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 21),
    _CfprIpsecConnectionNumCerts_Type()
)
cfprIpsecConnectionNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionNumCerts.setStatus("current")
_CfprIpsecConnectionPolicyLevel_Type = Gauge32
_CfprIpsecConnectionPolicyLevel_Object = MibTableColumn
cfprIpsecConnectionPolicyLevel = _CfprIpsecConnectionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 22),
    _CfprIpsecConnectionPolicyLevel_Type()
)
cfprIpsecConnectionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionPolicyLevel.setStatus("current")
_CfprIpsecConnectionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprIpsecConnectionPolicyOwner_Object = MibTableColumn
cfprIpsecConnectionPolicyOwner = _CfprIpsecConnectionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 23),
    _CfprIpsecConnectionPolicyOwner_Type()
)
cfprIpsecConnectionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionPolicyOwner.setStatus("current")
_CfprIpsecConnectionProposals_Type = SnmpAdminString
_CfprIpsecConnectionProposals_Object = MibTableColumn
cfprIpsecConnectionProposals = _CfprIpsecConnectionProposals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 24),
    _CfprIpsecConnectionProposals_Type()
)
cfprIpsecConnectionProposals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionProposals.setStatus("current")
_CfprIpsecConnectionPwd_Type = SnmpAdminString
_CfprIpsecConnectionPwd_Object = MibTableColumn
cfprIpsecConnectionPwd = _CfprIpsecConnectionPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 25),
    _CfprIpsecConnectionPwd_Type()
)
cfprIpsecConnectionPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionPwd.setStatus("current")
_CfprIpsecConnectionRemoteAddrs_Type = SnmpAdminString
_CfprIpsecConnectionRemoteAddrs_Object = MibTableColumn
cfprIpsecConnectionRemoteAddrs = _CfprIpsecConnectionRemoteAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 26),
    _CfprIpsecConnectionRemoteAddrs_Type()
)
cfprIpsecConnectionRemoteAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionRemoteAddrs.setStatus("current")
_CfprIpsecConnectionRemoteIkeIdent_Type = SnmpAdminString
_CfprIpsecConnectionRemoteIkeIdent_Object = MibTableColumn
cfprIpsecConnectionRemoteIkeIdent = _CfprIpsecConnectionRemoteIkeIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 27),
    _CfprIpsecConnectionRemoteIkeIdent_Type()
)
cfprIpsecConnectionRemoteIkeIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionRemoteIkeIdent.setStatus("current")
_CfprIpsecConnectionRemoteTs_Type = SnmpAdminString
_CfprIpsecConnectionRemoteTs_Object = MibTableColumn
cfprIpsecConnectionRemoteTs = _CfprIpsecConnectionRemoteTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 28),
    _CfprIpsecConnectionRemoteTs_Type()
)
cfprIpsecConnectionRemoteTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionRemoteTs.setStatus("current")
_CfprIpsecConnectionRevokePolicy_Type = CfprIpsecRevokePolicy
_CfprIpsecConnectionRevokePolicy_Object = MibTableColumn
cfprIpsecConnectionRevokePolicy = _CfprIpsecConnectionRevokePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 29),
    _CfprIpsecConnectionRevokePolicy_Type()
)
cfprIpsecConnectionRevokePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionRevokePolicy.setStatus("current")
_CfprIpsecConnectionTpName_Type = SnmpAdminString
_CfprIpsecConnectionTpName_Object = MibTableColumn
cfprIpsecConnectionTpName = _CfprIpsecConnectionTpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 30),
    _CfprIpsecConnectionTpName_Type()
)
cfprIpsecConnectionTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionTpName.setStatus("current")
_CfprIpsecConnectionFqdnEnforce_Type = CfprIpsecFqdnEnforceType
_CfprIpsecConnectionFqdnEnforce_Object = MibTableColumn
cfprIpsecConnectionFqdnEnforce = _CfprIpsecConnectionFqdnEnforce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 31),
    _CfprIpsecConnectionFqdnEnforce_Type()
)
cfprIpsecConnectionFqdnEnforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionFqdnEnforce.setStatus("current")
_CfprIpsecConnectionKeyringtype_Type = CfprPkiType
_CfprIpsecConnectionKeyringtype_Object = MibTableColumn
cfprIpsecConnectionKeyringtype = _CfprIpsecConnectionKeyringtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 2, 1, 32),
    _CfprIpsecConnectionKeyringtype_Type()
)
cfprIpsecConnectionKeyringtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecConnectionKeyringtype.setStatus("current")
_CfprIpsecEpTable_Object = MibTable
cfprIpsecEpTable = _CfprIpsecEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3)
)
if mibBuilder.loadTexts:
    cfprIpsecEpTable.setStatus("current")
_CfprIpsecEpEntry_Object = MibTableRow
cfprIpsecEpEntry = _CfprIpsecEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1)
)
cfprIpsecEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecEpEntry.setStatus("current")
_CfprIpsecEpInstanceId_Type = CfprManagedObjectId
_CfprIpsecEpInstanceId_Object = MibTableColumn
cfprIpsecEpInstanceId = _CfprIpsecEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 1),
    _CfprIpsecEpInstanceId_Type()
)
cfprIpsecEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecEpInstanceId.setStatus("current")
_CfprIpsecEpDn_Type = CfprManagedObjectDn
_CfprIpsecEpDn_Object = MibTableColumn
cfprIpsecEpDn = _CfprIpsecEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 2),
    _CfprIpsecEpDn_Type()
)
cfprIpsecEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpDn.setStatus("current")
_CfprIpsecEpRn_Type = SnmpAdminString
_CfprIpsecEpRn_Object = MibTableColumn
cfprIpsecEpRn = _CfprIpsecEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 3),
    _CfprIpsecEpRn_Type()
)
cfprIpsecEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpRn.setStatus("current")
_CfprIpsecEpDescr_Type = SnmpAdminString
_CfprIpsecEpDescr_Object = MibTableColumn
cfprIpsecEpDescr = _CfprIpsecEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 4),
    _CfprIpsecEpDescr_Type()
)
cfprIpsecEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpDescr.setStatus("current")
_CfprIpsecEpExecuteCmd_Type = CfprIpsecCommand
_CfprIpsecEpExecuteCmd_Object = MibTableColumn
cfprIpsecEpExecuteCmd = _CfprIpsecEpExecuteCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 5),
    _CfprIpsecEpExecuteCmd_Type()
)
cfprIpsecEpExecuteCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpExecuteCmd.setStatus("current")
_CfprIpsecEpFsmDescr_Type = SnmpAdminString
_CfprIpsecEpFsmDescr_Object = MibTableColumn
cfprIpsecEpFsmDescr = _CfprIpsecEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 6),
    _CfprIpsecEpFsmDescr_Type()
)
cfprIpsecEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmDescr.setStatus("current")
_CfprIpsecEpFsmPrev_Type = SnmpAdminString
_CfprIpsecEpFsmPrev_Object = MibTableColumn
cfprIpsecEpFsmPrev = _CfprIpsecEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 7),
    _CfprIpsecEpFsmPrev_Type()
)
cfprIpsecEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmPrev.setStatus("current")
_CfprIpsecEpFsmProgr_Type = Gauge32
_CfprIpsecEpFsmProgr_Object = MibTableColumn
cfprIpsecEpFsmProgr = _CfprIpsecEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 8),
    _CfprIpsecEpFsmProgr_Type()
)
cfprIpsecEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmProgr.setStatus("current")
_CfprIpsecEpFsmRmtInvErrCode_Type = Gauge32
_CfprIpsecEpFsmRmtInvErrCode_Object = MibTableColumn
cfprIpsecEpFsmRmtInvErrCode = _CfprIpsecEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 9),
    _CfprIpsecEpFsmRmtInvErrCode_Type()
)
cfprIpsecEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRmtInvErrCode.setStatus("current")
_CfprIpsecEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprIpsecEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprIpsecEpFsmRmtInvErrDescr = _CfprIpsecEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 10),
    _CfprIpsecEpFsmRmtInvErrDescr_Type()
)
cfprIpsecEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRmtInvErrDescr.setStatus("current")
_CfprIpsecEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprIpsecEpFsmRmtInvRslt_Object = MibTableColumn
cfprIpsecEpFsmRmtInvRslt = _CfprIpsecEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 11),
    _CfprIpsecEpFsmRmtInvRslt_Type()
)
cfprIpsecEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRmtInvRslt.setStatus("current")
_CfprIpsecEpFsmStageDescr_Type = SnmpAdminString
_CfprIpsecEpFsmStageDescr_Object = MibTableColumn
cfprIpsecEpFsmStageDescr = _CfprIpsecEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 12),
    _CfprIpsecEpFsmStageDescr_Type()
)
cfprIpsecEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageDescr.setStatus("current")
_CfprIpsecEpFsmStamp_Type = DateAndTime
_CfprIpsecEpFsmStamp_Object = MibTableColumn
cfprIpsecEpFsmStamp = _CfprIpsecEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 13),
    _CfprIpsecEpFsmStamp_Type()
)
cfprIpsecEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStamp.setStatus("current")
_CfprIpsecEpFsmStatus_Type = SnmpAdminString
_CfprIpsecEpFsmStatus_Object = MibTableColumn
cfprIpsecEpFsmStatus = _CfprIpsecEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 14),
    _CfprIpsecEpFsmStatus_Type()
)
cfprIpsecEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStatus.setStatus("current")
_CfprIpsecEpFsmTry_Type = Gauge32
_CfprIpsecEpFsmTry_Object = MibTableColumn
cfprIpsecEpFsmTry = _CfprIpsecEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 15),
    _CfprIpsecEpFsmTry_Type()
)
cfprIpsecEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTry.setStatus("current")
_CfprIpsecEpIntId_Type = SnmpAdminString
_CfprIpsecEpIntId_Object = MibTableColumn
cfprIpsecEpIntId = _CfprIpsecEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 16),
    _CfprIpsecEpIntId_Type()
)
cfprIpsecEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpIntId.setStatus("current")
_CfprIpsecEpLogLevel_Type = Gauge32
_CfprIpsecEpLogLevel_Object = MibTableColumn
cfprIpsecEpLogLevel = _CfprIpsecEpLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 17),
    _CfprIpsecEpLogLevel_Type()
)
cfprIpsecEpLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpLogLevel.setStatus("current")
_CfprIpsecEpName_Type = SnmpAdminString
_CfprIpsecEpName_Object = MibTableColumn
cfprIpsecEpName = _CfprIpsecEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 18),
    _CfprIpsecEpName_Type()
)
cfprIpsecEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpName.setStatus("current")
_CfprIpsecEpPolicyLevel_Type = Gauge32
_CfprIpsecEpPolicyLevel_Object = MibTableColumn
cfprIpsecEpPolicyLevel = _CfprIpsecEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 19),
    _CfprIpsecEpPolicyLevel_Type()
)
cfprIpsecEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpPolicyLevel.setStatus("current")
_CfprIpsecEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprIpsecEpPolicyOwner_Object = MibTableColumn
cfprIpsecEpPolicyOwner = _CfprIpsecEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 20),
    _CfprIpsecEpPolicyOwner_Type()
)
cfprIpsecEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpPolicyOwner.setStatus("current")
_CfprIpsecEpSaEnforce_Type = TruthValue
_CfprIpsecEpSaEnforce_Object = MibTableColumn
cfprIpsecEpSaEnforce = _CfprIpsecEpSaEnforce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 3, 1, 21),
    _CfprIpsecEpSaEnforce_Type()
)
cfprIpsecEpSaEnforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpSaEnforce.setStatus("current")
_CfprIpsecEpFsmTable_Object = MibTable
cfprIpsecEpFsmTable = _CfprIpsecEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4)
)
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTable.setStatus("current")
_CfprIpsecEpFsmEntry_Object = MibTableRow
cfprIpsecEpFsmEntry = _CfprIpsecEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1)
)
cfprIpsecEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecEpFsmEntry.setStatus("current")
_CfprIpsecEpFsmInstanceId_Type = CfprManagedObjectId
_CfprIpsecEpFsmInstanceId_Object = MibTableColumn
cfprIpsecEpFsmInstanceId = _CfprIpsecEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 1),
    _CfprIpsecEpFsmInstanceId_Type()
)
cfprIpsecEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmInstanceId.setStatus("current")
_CfprIpsecEpFsmDn_Type = CfprManagedObjectDn
_CfprIpsecEpFsmDn_Object = MibTableColumn
cfprIpsecEpFsmDn = _CfprIpsecEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 2),
    _CfprIpsecEpFsmDn_Type()
)
cfprIpsecEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmDn.setStatus("current")
_CfprIpsecEpFsmRn_Type = SnmpAdminString
_CfprIpsecEpFsmRn_Object = MibTableColumn
cfprIpsecEpFsmRn = _CfprIpsecEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 3),
    _CfprIpsecEpFsmRn_Type()
)
cfprIpsecEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRn.setStatus("current")
_CfprIpsecEpFsmCompletionTime_Type = DateAndTime
_CfprIpsecEpFsmCompletionTime_Object = MibTableColumn
cfprIpsecEpFsmCompletionTime = _CfprIpsecEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 4),
    _CfprIpsecEpFsmCompletionTime_Type()
)
cfprIpsecEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmCompletionTime.setStatus("current")
_CfprIpsecEpFsmCurrentFsm_Type = CfprIpsecEpFsmCurrentFsm
_CfprIpsecEpFsmCurrentFsm_Object = MibTableColumn
cfprIpsecEpFsmCurrentFsm = _CfprIpsecEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 5),
    _CfprIpsecEpFsmCurrentFsm_Type()
)
cfprIpsecEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmCurrentFsm.setStatus("current")
_CfprIpsecEpFsmDescrData_Type = SnmpAdminString
_CfprIpsecEpFsmDescrData_Object = MibTableColumn
cfprIpsecEpFsmDescrData = _CfprIpsecEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 6),
    _CfprIpsecEpFsmDescrData_Type()
)
cfprIpsecEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmDescrData.setStatus("current")
_CfprIpsecEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprIpsecEpFsmFsmStatus_Object = MibTableColumn
cfprIpsecEpFsmFsmStatus = _CfprIpsecEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 7),
    _CfprIpsecEpFsmFsmStatus_Type()
)
cfprIpsecEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmFsmStatus.setStatus("current")
_CfprIpsecEpFsmProgress_Type = Gauge32
_CfprIpsecEpFsmProgress_Object = MibTableColumn
cfprIpsecEpFsmProgress = _CfprIpsecEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 8),
    _CfprIpsecEpFsmProgress_Type()
)
cfprIpsecEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmProgress.setStatus("current")
_CfprIpsecEpFsmRmtErrCode_Type = Gauge32
_CfprIpsecEpFsmRmtErrCode_Object = MibTableColumn
cfprIpsecEpFsmRmtErrCode = _CfprIpsecEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 9),
    _CfprIpsecEpFsmRmtErrCode_Type()
)
cfprIpsecEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRmtErrCode.setStatus("current")
_CfprIpsecEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprIpsecEpFsmRmtErrDescr_Object = MibTableColumn
cfprIpsecEpFsmRmtErrDescr = _CfprIpsecEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 10),
    _CfprIpsecEpFsmRmtErrDescr_Type()
)
cfprIpsecEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRmtErrDescr.setStatus("current")
_CfprIpsecEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprIpsecEpFsmRmtRslt_Object = MibTableColumn
cfprIpsecEpFsmRmtRslt = _CfprIpsecEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 4, 1, 11),
    _CfprIpsecEpFsmRmtRslt_Type()
)
cfprIpsecEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmRmtRslt.setStatus("current")
_CfprIpsecEpFsmStageTable_Object = MibTable
cfprIpsecEpFsmStageTable = _CfprIpsecEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5)
)
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageTable.setStatus("current")
_CfprIpsecEpFsmStageEntry_Object = MibTableRow
cfprIpsecEpFsmStageEntry = _CfprIpsecEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1)
)
cfprIpsecEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageEntry.setStatus("current")
_CfprIpsecEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprIpsecEpFsmStageInstanceId_Object = MibTableColumn
cfprIpsecEpFsmStageInstanceId = _CfprIpsecEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 1),
    _CfprIpsecEpFsmStageInstanceId_Type()
)
cfprIpsecEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageInstanceId.setStatus("current")
_CfprIpsecEpFsmStageDn_Type = CfprManagedObjectDn
_CfprIpsecEpFsmStageDn_Object = MibTableColumn
cfprIpsecEpFsmStageDn = _CfprIpsecEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 2),
    _CfprIpsecEpFsmStageDn_Type()
)
cfprIpsecEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageDn.setStatus("current")
_CfprIpsecEpFsmStageRn_Type = SnmpAdminString
_CfprIpsecEpFsmStageRn_Object = MibTableColumn
cfprIpsecEpFsmStageRn = _CfprIpsecEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 3),
    _CfprIpsecEpFsmStageRn_Type()
)
cfprIpsecEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageRn.setStatus("current")
_CfprIpsecEpFsmStageDescrData_Type = SnmpAdminString
_CfprIpsecEpFsmStageDescrData_Object = MibTableColumn
cfprIpsecEpFsmStageDescrData = _CfprIpsecEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 4),
    _CfprIpsecEpFsmStageDescrData_Type()
)
cfprIpsecEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageDescrData.setStatus("current")
_CfprIpsecEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprIpsecEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprIpsecEpFsmStageLastUpdateTime = _CfprIpsecEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 5),
    _CfprIpsecEpFsmStageLastUpdateTime_Type()
)
cfprIpsecEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageLastUpdateTime.setStatus("current")
_CfprIpsecEpFsmStageName_Type = CfprIpsecEpFsmStageName
_CfprIpsecEpFsmStageName_Object = MibTableColumn
cfprIpsecEpFsmStageName = _CfprIpsecEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 6),
    _CfprIpsecEpFsmStageName_Type()
)
cfprIpsecEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageName.setStatus("current")
_CfprIpsecEpFsmStageOrder_Type = Gauge32
_CfprIpsecEpFsmStageOrder_Object = MibTableColumn
cfprIpsecEpFsmStageOrder = _CfprIpsecEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 7),
    _CfprIpsecEpFsmStageOrder_Type()
)
cfprIpsecEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageOrder.setStatus("current")
_CfprIpsecEpFsmStageRetry_Type = Gauge32
_CfprIpsecEpFsmStageRetry_Object = MibTableColumn
cfprIpsecEpFsmStageRetry = _CfprIpsecEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 8),
    _CfprIpsecEpFsmStageRetry_Type()
)
cfprIpsecEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageRetry.setStatus("current")
_CfprIpsecEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprIpsecEpFsmStageStageStatus_Object = MibTableColumn
cfprIpsecEpFsmStageStageStatus = _CfprIpsecEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 5, 1, 9),
    _CfprIpsecEpFsmStageStageStatus_Type()
)
cfprIpsecEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmStageStageStatus.setStatus("current")
_CfprIpsecEpFsmTaskTable_Object = MibTable
cfprIpsecEpFsmTaskTable = _CfprIpsecEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6)
)
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskTable.setStatus("current")
_CfprIpsecEpFsmTaskEntry_Object = MibTableRow
cfprIpsecEpFsmTaskEntry = _CfprIpsecEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1)
)
cfprIpsecEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskEntry.setStatus("current")
_CfprIpsecEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprIpsecEpFsmTaskInstanceId_Object = MibTableColumn
cfprIpsecEpFsmTaskInstanceId = _CfprIpsecEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 1),
    _CfprIpsecEpFsmTaskInstanceId_Type()
)
cfprIpsecEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskInstanceId.setStatus("current")
_CfprIpsecEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprIpsecEpFsmTaskDn_Object = MibTableColumn
cfprIpsecEpFsmTaskDn = _CfprIpsecEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 2),
    _CfprIpsecEpFsmTaskDn_Type()
)
cfprIpsecEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskDn.setStatus("current")
_CfprIpsecEpFsmTaskRn_Type = SnmpAdminString
_CfprIpsecEpFsmTaskRn_Object = MibTableColumn
cfprIpsecEpFsmTaskRn = _CfprIpsecEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 3),
    _CfprIpsecEpFsmTaskRn_Type()
)
cfprIpsecEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskRn.setStatus("current")
_CfprIpsecEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprIpsecEpFsmTaskCompletion_Object = MibTableColumn
cfprIpsecEpFsmTaskCompletion = _CfprIpsecEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 4),
    _CfprIpsecEpFsmTaskCompletion_Type()
)
cfprIpsecEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskCompletion.setStatus("current")
_CfprIpsecEpFsmTaskFlags_Type = CfprFsmFlags
_CfprIpsecEpFsmTaskFlags_Object = MibTableColumn
cfprIpsecEpFsmTaskFlags = _CfprIpsecEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 5),
    _CfprIpsecEpFsmTaskFlags_Type()
)
cfprIpsecEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskFlags.setStatus("current")
_CfprIpsecEpFsmTaskItem_Type = CfprIpsecEpFsmTaskItem
_CfprIpsecEpFsmTaskItem_Object = MibTableColumn
cfprIpsecEpFsmTaskItem = _CfprIpsecEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 6),
    _CfprIpsecEpFsmTaskItem_Type()
)
cfprIpsecEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskItem.setStatus("current")
_CfprIpsecEpFsmTaskSeqId_Type = Gauge32
_CfprIpsecEpFsmTaskSeqId_Object = MibTableColumn
cfprIpsecEpFsmTaskSeqId = _CfprIpsecEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 6, 1, 7),
    _CfprIpsecEpFsmTaskSeqId_Type()
)
cfprIpsecEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecEpFsmTaskSeqId.setStatus("current")
_CfprIpsecStatsTable_Object = MibTable
cfprIpsecStatsTable = _CfprIpsecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7)
)
if mibBuilder.loadTexts:
    cfprIpsecStatsTable.setStatus("current")
_CfprIpsecStatsEntry_Object = MibTableRow
cfprIpsecStatsEntry = _CfprIpsecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1)
)
cfprIpsecStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPSEC-MIB", "cfprIpsecStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpsecStatsEntry.setStatus("current")
_CfprIpsecStatsInstanceId_Type = CfprManagedObjectId
_CfprIpsecStatsInstanceId_Object = MibTableColumn
cfprIpsecStatsInstanceId = _CfprIpsecStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 1),
    _CfprIpsecStatsInstanceId_Type()
)
cfprIpsecStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpsecStatsInstanceId.setStatus("current")
_CfprIpsecStatsDn_Type = CfprManagedObjectDn
_CfprIpsecStatsDn_Object = MibTableColumn
cfprIpsecStatsDn = _CfprIpsecStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 2),
    _CfprIpsecStatsDn_Type()
)
cfprIpsecStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecStatsDn.setStatus("current")
_CfprIpsecStatsRn_Type = SnmpAdminString
_CfprIpsecStatsRn_Object = MibTableColumn
cfprIpsecStatsRn = _CfprIpsecStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 3),
    _CfprIpsecStatsRn_Type()
)
cfprIpsecStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecStatsRn.setStatus("current")
_CfprIpsecStatsData_Type = SnmpAdminString
_CfprIpsecStatsData_Object = MibTableColumn
cfprIpsecStatsData = _CfprIpsecStatsData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 4),
    _CfprIpsecStatsData_Type()
)
cfprIpsecStatsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecStatsData.setStatus("current")
_CfprIpsecStatsStatsType_Type = CfprIpsecStatsType
_CfprIpsecStatsStatsType_Object = MibTableColumn
cfprIpsecStatsStatsType = _CfprIpsecStatsStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 5),
    _CfprIpsecStatsStatsType_Type()
)
cfprIpsecStatsStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecStatsStatsType.setStatus("current")
_CfprIpsecStatsTs_Type = DateAndTime
_CfprIpsecStatsTs_Object = MibTableColumn
cfprIpsecStatsTs = _CfprIpsecStatsTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 6),
    _CfprIpsecStatsTs_Type()
)
cfprIpsecStatsTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecStatsTs.setStatus("current")
_CfprIpsecStatsUpdate_Type = TruthValue
_CfprIpsecStatsUpdate_Object = MibTableColumn
cfprIpsecStatsUpdate = _CfprIpsecStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 84, 7, 1, 7),
    _CfprIpsecStatsUpdate_Type()
)
cfprIpsecStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpsecStatsUpdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IPSEC-MIB",
    **{"cfprIpsecObjects": cfprIpsecObjects,
       "cfprIpsecAuthorityTable": cfprIpsecAuthorityTable,
       "cfprIpsecAuthorityEntry": cfprIpsecAuthorityEntry,
       "cfprIpsecAuthorityInstanceId": cfprIpsecAuthorityInstanceId,
       "cfprIpsecAuthorityDn": cfprIpsecAuthorityDn,
       "cfprIpsecAuthorityRn": cfprIpsecAuthorityRn,
       "cfprIpsecAuthorityConfigState": cfprIpsecAuthorityConfigState,
       "cfprIpsecAuthorityCrlUris": cfprIpsecAuthorityCrlUris,
       "cfprIpsecAuthorityDescr": cfprIpsecAuthorityDescr,
       "cfprIpsecAuthorityIntId": cfprIpsecAuthorityIntId,
       "cfprIpsecAuthorityName": cfprIpsecAuthorityName,
       "cfprIpsecAuthorityNumCerts": cfprIpsecAuthorityNumCerts,
       "cfprIpsecAuthorityOcspUris": cfprIpsecAuthorityOcspUris,
       "cfprIpsecAuthorityPolicyLevel": cfprIpsecAuthorityPolicyLevel,
       "cfprIpsecAuthorityPolicyOwner": cfprIpsecAuthorityPolicyOwner,
       "cfprIpsecAuthorityTpName": cfprIpsecAuthorityTpName,
       "cfprIpsecConnectionTable": cfprIpsecConnectionTable,
       "cfprIpsecConnectionEntry": cfprIpsecConnectionEntry,
       "cfprIpsecConnectionInstanceId": cfprIpsecConnectionInstanceId,
       "cfprIpsecConnectionDn": cfprIpsecConnectionDn,
       "cfprIpsecConnectionRn": cfprIpsecConnectionRn,
       "cfprIpsecConnectionAdminState": cfprIpsecConnectionAdminState,
       "cfprIpsecConnectionAuth": cfprIpsecConnectionAuth,
       "cfprIpsecConnectionConfigState": cfprIpsecConnectionConfigState,
       "cfprIpsecConnectionDescr": cfprIpsecConnectionDescr,
       "cfprIpsecConnectionEspMode": cfprIpsecConnectionEspMode,
       "cfprIpsecConnectionEspProposals": cfprIpsecConnectionEspProposals,
       "cfprIpsecConnectionEspRekeyTime": cfprIpsecConnectionEspRekeyTime,
       "cfprIpsecConnectionIkeRekeyTime": cfprIpsecConnectionIkeRekeyTime,
       "cfprIpsecConnectionIkeVer": cfprIpsecConnectionIkeVer,
       "cfprIpsecConnectionInactivity": cfprIpsecConnectionInactivity,
       "cfprIpsecConnectionIntId": cfprIpsecConnectionIntId,
       "cfprIpsecConnectionKeyingtries": cfprIpsecConnectionKeyingtries,
       "cfprIpsecConnectionKeyring": cfprIpsecConnectionKeyring,
       "cfprIpsecConnectionLocalAddrs": cfprIpsecConnectionLocalAddrs,
       "cfprIpsecConnectionLocalIkeIdent": cfprIpsecConnectionLocalIkeIdent,
       "cfprIpsecConnectionLocalTs": cfprIpsecConnectionLocalTs,
       "cfprIpsecConnectionName": cfprIpsecConnectionName,
       "cfprIpsecConnectionNumCerts": cfprIpsecConnectionNumCerts,
       "cfprIpsecConnectionPolicyLevel": cfprIpsecConnectionPolicyLevel,
       "cfprIpsecConnectionPolicyOwner": cfprIpsecConnectionPolicyOwner,
       "cfprIpsecConnectionProposals": cfprIpsecConnectionProposals,
       "cfprIpsecConnectionPwd": cfprIpsecConnectionPwd,
       "cfprIpsecConnectionRemoteAddrs": cfprIpsecConnectionRemoteAddrs,
       "cfprIpsecConnectionRemoteIkeIdent": cfprIpsecConnectionRemoteIkeIdent,
       "cfprIpsecConnectionRemoteTs": cfprIpsecConnectionRemoteTs,
       "cfprIpsecConnectionRevokePolicy": cfprIpsecConnectionRevokePolicy,
       "cfprIpsecConnectionTpName": cfprIpsecConnectionTpName,
       "cfprIpsecConnectionFqdnEnforce": cfprIpsecConnectionFqdnEnforce,
       "cfprIpsecConnectionKeyringtype": cfprIpsecConnectionKeyringtype,
       "cfprIpsecEpTable": cfprIpsecEpTable,
       "cfprIpsecEpEntry": cfprIpsecEpEntry,
       "cfprIpsecEpInstanceId": cfprIpsecEpInstanceId,
       "cfprIpsecEpDn": cfprIpsecEpDn,
       "cfprIpsecEpRn": cfprIpsecEpRn,
       "cfprIpsecEpDescr": cfprIpsecEpDescr,
       "cfprIpsecEpExecuteCmd": cfprIpsecEpExecuteCmd,
       "cfprIpsecEpFsmDescr": cfprIpsecEpFsmDescr,
       "cfprIpsecEpFsmPrev": cfprIpsecEpFsmPrev,
       "cfprIpsecEpFsmProgr": cfprIpsecEpFsmProgr,
       "cfprIpsecEpFsmRmtInvErrCode": cfprIpsecEpFsmRmtInvErrCode,
       "cfprIpsecEpFsmRmtInvErrDescr": cfprIpsecEpFsmRmtInvErrDescr,
       "cfprIpsecEpFsmRmtInvRslt": cfprIpsecEpFsmRmtInvRslt,
       "cfprIpsecEpFsmStageDescr": cfprIpsecEpFsmStageDescr,
       "cfprIpsecEpFsmStamp": cfprIpsecEpFsmStamp,
       "cfprIpsecEpFsmStatus": cfprIpsecEpFsmStatus,
       "cfprIpsecEpFsmTry": cfprIpsecEpFsmTry,
       "cfprIpsecEpIntId": cfprIpsecEpIntId,
       "cfprIpsecEpLogLevel": cfprIpsecEpLogLevel,
       "cfprIpsecEpName": cfprIpsecEpName,
       "cfprIpsecEpPolicyLevel": cfprIpsecEpPolicyLevel,
       "cfprIpsecEpPolicyOwner": cfprIpsecEpPolicyOwner,
       "cfprIpsecEpSaEnforce": cfprIpsecEpSaEnforce,
       "cfprIpsecEpFsmTable": cfprIpsecEpFsmTable,
       "cfprIpsecEpFsmEntry": cfprIpsecEpFsmEntry,
       "cfprIpsecEpFsmInstanceId": cfprIpsecEpFsmInstanceId,
       "cfprIpsecEpFsmDn": cfprIpsecEpFsmDn,
       "cfprIpsecEpFsmRn": cfprIpsecEpFsmRn,
       "cfprIpsecEpFsmCompletionTime": cfprIpsecEpFsmCompletionTime,
       "cfprIpsecEpFsmCurrentFsm": cfprIpsecEpFsmCurrentFsm,
       "cfprIpsecEpFsmDescrData": cfprIpsecEpFsmDescrData,
       "cfprIpsecEpFsmFsmStatus": cfprIpsecEpFsmFsmStatus,
       "cfprIpsecEpFsmProgress": cfprIpsecEpFsmProgress,
       "cfprIpsecEpFsmRmtErrCode": cfprIpsecEpFsmRmtErrCode,
       "cfprIpsecEpFsmRmtErrDescr": cfprIpsecEpFsmRmtErrDescr,
       "cfprIpsecEpFsmRmtRslt": cfprIpsecEpFsmRmtRslt,
       "cfprIpsecEpFsmStageTable": cfprIpsecEpFsmStageTable,
       "cfprIpsecEpFsmStageEntry": cfprIpsecEpFsmStageEntry,
       "cfprIpsecEpFsmStageInstanceId": cfprIpsecEpFsmStageInstanceId,
       "cfprIpsecEpFsmStageDn": cfprIpsecEpFsmStageDn,
       "cfprIpsecEpFsmStageRn": cfprIpsecEpFsmStageRn,
       "cfprIpsecEpFsmStageDescrData": cfprIpsecEpFsmStageDescrData,
       "cfprIpsecEpFsmStageLastUpdateTime": cfprIpsecEpFsmStageLastUpdateTime,
       "cfprIpsecEpFsmStageName": cfprIpsecEpFsmStageName,
       "cfprIpsecEpFsmStageOrder": cfprIpsecEpFsmStageOrder,
       "cfprIpsecEpFsmStageRetry": cfprIpsecEpFsmStageRetry,
       "cfprIpsecEpFsmStageStageStatus": cfprIpsecEpFsmStageStageStatus,
       "cfprIpsecEpFsmTaskTable": cfprIpsecEpFsmTaskTable,
       "cfprIpsecEpFsmTaskEntry": cfprIpsecEpFsmTaskEntry,
       "cfprIpsecEpFsmTaskInstanceId": cfprIpsecEpFsmTaskInstanceId,
       "cfprIpsecEpFsmTaskDn": cfprIpsecEpFsmTaskDn,
       "cfprIpsecEpFsmTaskRn": cfprIpsecEpFsmTaskRn,
       "cfprIpsecEpFsmTaskCompletion": cfprIpsecEpFsmTaskCompletion,
       "cfprIpsecEpFsmTaskFlags": cfprIpsecEpFsmTaskFlags,
       "cfprIpsecEpFsmTaskItem": cfprIpsecEpFsmTaskItem,
       "cfprIpsecEpFsmTaskSeqId": cfprIpsecEpFsmTaskSeqId,
       "cfprIpsecStatsTable": cfprIpsecStatsTable,
       "cfprIpsecStatsEntry": cfprIpsecStatsEntry,
       "cfprIpsecStatsInstanceId": cfprIpsecStatsInstanceId,
       "cfprIpsecStatsDn": cfprIpsecStatsDn,
       "cfprIpsecStatsRn": cfprIpsecStatsRn,
       "cfprIpsecStatsData": cfprIpsecStatsData,
       "cfprIpsecStatsStatsType": cfprIpsecStatsStatsType,
       "cfprIpsecStatsTs": cfprIpsecStatsTs,
       "cfprIpsecStatsUpdate": cfprIpsecStatsUpdate}
)
