# SNMP MIB module (CISCO-FIREPOWER-AP-EXTPOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-EXTPOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApConditionRemoteInvRslt,
 CfprApExtpolAppCapability,
 CfprApExtpolConnProtocol,
 CfprApExtpolConnType,
 CfprApExtpolConnectorOperState,
 CfprApExtpolEpFsmCurrentFsm,
 CfprApExtpolEpFsmStageName,
 CfprApExtpolEpFsmTaskItem,
 CfprApExtpolProviderFsmCurrentFsm,
 CfprApExtpolProviderFsmStageName,
 CfprApExtpolProviderFsmTaskItem,
 CfprApExtpolRegistryFsmCurrentFsm,
 CfprApExtpolRegistryFsmStageName,
 CfprApExtpolRegistryFsmTaskItem,
 CfprApExtpolState,
 CfprApExtpolSuspendState,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApExtpolAppCapability",
    "CfprApExtpolConnProtocol",
    "CfprApExtpolConnType",
    "CfprApExtpolConnectorOperState",
    "CfprApExtpolEpFsmCurrentFsm",
    "CfprApExtpolEpFsmStageName",
    "CfprApExtpolEpFsmTaskItem",
    "CfprApExtpolProviderFsmCurrentFsm",
    "CfprApExtpolProviderFsmStageName",
    "CfprApExtpolProviderFsmTaskItem",
    "CfprApExtpolRegistryFsmCurrentFsm",
    "CfprApExtpolRegistryFsmStageName",
    "CfprApExtpolRegistryFsmTaskItem",
    "CfprApExtpolState",
    "CfprApExtpolSuspendState",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus")

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

cfprApExtpolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApExtpolClientTable_Object = MibTable
cfprApExtpolClientTable = _CfprApExtpolClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1)
)
if mibBuilder.loadTexts:
    cfprApExtpolClientTable.setStatus("current")
_CfprApExtpolClientEntry_Object = MibTableRow
cfprApExtpolClientEntry = _CfprApExtpolClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1)
)
cfprApExtpolClientEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolClientInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolClientEntry.setStatus("current")
_CfprApExtpolClientInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolClientInstanceId_Object = MibTableColumn
cfprApExtpolClientInstanceId = _CfprApExtpolClientInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 1),
    _CfprApExtpolClientInstanceId_Type()
)
cfprApExtpolClientInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolClientInstanceId.setStatus("current")
_CfprApExtpolClientDn_Type = CfprApManagedObjectDn
_CfprApExtpolClientDn_Object = MibTableColumn
cfprApExtpolClientDn = _CfprApExtpolClientDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 2),
    _CfprApExtpolClientDn_Type()
)
cfprApExtpolClientDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientDn.setStatus("current")
_CfprApExtpolClientRn_Type = SnmpAdminString
_CfprApExtpolClientRn_Object = MibTableColumn
cfprApExtpolClientRn = _CfprApExtpolClientRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 3),
    _CfprApExtpolClientRn_Type()
)
cfprApExtpolClientRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientRn.setStatus("current")
_CfprApExtpolClientCapability_Type = CfprApExtpolAppCapability
_CfprApExtpolClientCapability_Object = MibTableColumn
cfprApExtpolClientCapability = _CfprApExtpolClientCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 4),
    _CfprApExtpolClientCapability_Type()
)
cfprApExtpolClientCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientCapability.setStatus("current")
_CfprApExtpolClientConnProtocol_Type = CfprApExtpolConnProtocol
_CfprApExtpolClientConnProtocol_Object = MibTableColumn
cfprApExtpolClientConnProtocol = _CfprApExtpolClientConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 5),
    _CfprApExtpolClientConnProtocol_Type()
)
cfprApExtpolClientConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientConnProtocol.setStatus("current")
_CfprApExtpolClientDescr_Type = SnmpAdminString
_CfprApExtpolClientDescr_Object = MibTableColumn
cfprApExtpolClientDescr = _CfprApExtpolClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 6),
    _CfprApExtpolClientDescr_Type()
)
cfprApExtpolClientDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientDescr.setStatus("current")
_CfprApExtpolClientGracePeriodUsed_Type = Unsigned64
_CfprApExtpolClientGracePeriodUsed_Object = MibTableColumn
cfprApExtpolClientGracePeriodUsed = _CfprApExtpolClientGracePeriodUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 7),
    _CfprApExtpolClientGracePeriodUsed_Type()
)
cfprApExtpolClientGracePeriodUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientGracePeriodUsed.setStatus("current")
_CfprApExtpolClientGuid_Type = SnmpAdminString
_CfprApExtpolClientGuid_Object = MibTableColumn
cfprApExtpolClientGuid = _CfprApExtpolClientGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 8),
    _CfprApExtpolClientGuid_Type()
)
cfprApExtpolClientGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientGuid.setStatus("current")
_CfprApExtpolClientHost_Type = SnmpAdminString
_CfprApExtpolClientHost_Object = MibTableColumn
cfprApExtpolClientHost = _CfprApExtpolClientHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 9),
    _CfprApExtpolClientHost_Type()
)
cfprApExtpolClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientHost.setStatus("current")
_CfprApExtpolClientId_Type = Gauge32
_CfprApExtpolClientId_Object = MibTableColumn
cfprApExtpolClientId = _CfprApExtpolClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 10),
    _CfprApExtpolClientId_Type()
)
cfprApExtpolClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientId.setStatus("current")
_CfprApExtpolClientInterest_Type = CfprApExtpolAppCapability
_CfprApExtpolClientInterest_Object = MibTableColumn
cfprApExtpolClientInterest = _CfprApExtpolClientInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 11),
    _CfprApExtpolClientInterest_Type()
)
cfprApExtpolClientInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientInterest.setStatus("current")
_CfprApExtpolClientIp_Type = InetAddressIPv4
_CfprApExtpolClientIp_Object = MibTableColumn
cfprApExtpolClientIp = _CfprApExtpolClientIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 12),
    _CfprApExtpolClientIp_Type()
)
cfprApExtpolClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientIp.setStatus("current")
_CfprApExtpolClientIpv6_Type = InetAddressIPv6
_CfprApExtpolClientIpv6_Object = MibTableColumn
cfprApExtpolClientIpv6 = _CfprApExtpolClientIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 13),
    _CfprApExtpolClientIpv6_Type()
)
cfprApExtpolClientIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientIpv6.setStatus("current")
_CfprApExtpolClientLastPollTs_Type = DateAndTime
_CfprApExtpolClientLastPollTs_Object = MibTableColumn
cfprApExtpolClientLastPollTs = _CfprApExtpolClientLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 14),
    _CfprApExtpolClientLastPollTs_Type()
)
cfprApExtpolClientLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientLastPollTs.setStatus("current")
_CfprApExtpolClientLicState_Type = CfprApExtpolState
_CfprApExtpolClientLicState_Object = MibTableColumn
cfprApExtpolClientLicState = _CfprApExtpolClientLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 15),
    _CfprApExtpolClientLicState_Type()
)
cfprApExtpolClientLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientLicState.setStatus("current")
_CfprApExtpolClientName_Type = SnmpAdminString
_CfprApExtpolClientName_Object = MibTableColumn
cfprApExtpolClientName = _CfprApExtpolClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 16),
    _CfprApExtpolClientName_Type()
)
cfprApExtpolClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientName.setStatus("current")
_CfprApExtpolClientOperState_Type = CfprApExtpolConnectorOperState
_CfprApExtpolClientOperState_Object = MibTableColumn
cfprApExtpolClientOperState = _CfprApExtpolClientOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 17),
    _CfprApExtpolClientOperState_Type()
)
cfprApExtpolClientOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientOperState.setStatus("current")
_CfprApExtpolClientOwner_Type = SnmpAdminString
_CfprApExtpolClientOwner_Object = MibTableColumn
cfprApExtpolClientOwner = _CfprApExtpolClientOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 18),
    _CfprApExtpolClientOwner_Type()
)
cfprApExtpolClientOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientOwner.setStatus("current")
_CfprApExtpolClientSite_Type = SnmpAdminString
_CfprApExtpolClientSite_Object = MibTableColumn
cfprApExtpolClientSite = _CfprApExtpolClientSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 19),
    _CfprApExtpolClientSite_Type()
)
cfprApExtpolClientSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientSite.setStatus("current")
_CfprApExtpolClientSuspendState_Type = CfprApExtpolSuspendState
_CfprApExtpolClientSuspendState_Object = MibTableColumn
cfprApExtpolClientSuspendState = _CfprApExtpolClientSuspendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 20),
    _CfprApExtpolClientSuspendState_Type()
)
cfprApExtpolClientSuspendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientSuspendState.setStatus("current")
_CfprApExtpolClientType_Type = CfprApExtpolConnType
_CfprApExtpolClientType_Object = MibTableColumn
cfprApExtpolClientType = _CfprApExtpolClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 21),
    _CfprApExtpolClientType_Type()
)
cfprApExtpolClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientType.setStatus("current")
_CfprApExtpolClientVersion_Type = SnmpAdminString
_CfprApExtpolClientVersion_Object = MibTableColumn
cfprApExtpolClientVersion = _CfprApExtpolClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 1, 1, 22),
    _CfprApExtpolClientVersion_Type()
)
cfprApExtpolClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientVersion.setStatus("current")
_CfprApExtpolClientContTable_Object = MibTable
cfprApExtpolClientContTable = _CfprApExtpolClientContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 2)
)
if mibBuilder.loadTexts:
    cfprApExtpolClientContTable.setStatus("current")
_CfprApExtpolClientContEntry_Object = MibTableRow
cfprApExtpolClientContEntry = _CfprApExtpolClientContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 2, 1)
)
cfprApExtpolClientContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolClientContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolClientContEntry.setStatus("current")
_CfprApExtpolClientContInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolClientContInstanceId_Object = MibTableColumn
cfprApExtpolClientContInstanceId = _CfprApExtpolClientContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 2, 1, 1),
    _CfprApExtpolClientContInstanceId_Type()
)
cfprApExtpolClientContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolClientContInstanceId.setStatus("current")
_CfprApExtpolClientContDn_Type = CfprApManagedObjectDn
_CfprApExtpolClientContDn_Object = MibTableColumn
cfprApExtpolClientContDn = _CfprApExtpolClientContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 2, 1, 2),
    _CfprApExtpolClientContDn_Type()
)
cfprApExtpolClientContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientContDn.setStatus("current")
_CfprApExtpolClientContRn_Type = SnmpAdminString
_CfprApExtpolClientContRn_Object = MibTableColumn
cfprApExtpolClientContRn = _CfprApExtpolClientContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 2, 1, 3),
    _CfprApExtpolClientContRn_Type()
)
cfprApExtpolClientContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientContRn.setStatus("current")
_CfprApExtpolClientContGenNum_Type = Gauge32
_CfprApExtpolClientContGenNum_Object = MibTableColumn
cfprApExtpolClientContGenNum = _CfprApExtpolClientContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 2, 1, 4),
    _CfprApExtpolClientContGenNum_Type()
)
cfprApExtpolClientContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolClientContGenNum.setStatus("current")
_CfprApExtpolControllerTable_Object = MibTable
cfprApExtpolControllerTable = _CfprApExtpolControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3)
)
if mibBuilder.loadTexts:
    cfprApExtpolControllerTable.setStatus("current")
_CfprApExtpolControllerEntry_Object = MibTableRow
cfprApExtpolControllerEntry = _CfprApExtpolControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1)
)
cfprApExtpolControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolControllerEntry.setStatus("current")
_CfprApExtpolControllerInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolControllerInstanceId_Object = MibTableColumn
cfprApExtpolControllerInstanceId = _CfprApExtpolControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 1),
    _CfprApExtpolControllerInstanceId_Type()
)
cfprApExtpolControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolControllerInstanceId.setStatus("current")
_CfprApExtpolControllerDn_Type = CfprApManagedObjectDn
_CfprApExtpolControllerDn_Object = MibTableColumn
cfprApExtpolControllerDn = _CfprApExtpolControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 2),
    _CfprApExtpolControllerDn_Type()
)
cfprApExtpolControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerDn.setStatus("current")
_CfprApExtpolControllerRn_Type = SnmpAdminString
_CfprApExtpolControllerRn_Object = MibTableColumn
cfprApExtpolControllerRn = _CfprApExtpolControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 3),
    _CfprApExtpolControllerRn_Type()
)
cfprApExtpolControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerRn.setStatus("current")
_CfprApExtpolControllerCapability_Type = CfprApExtpolAppCapability
_CfprApExtpolControllerCapability_Object = MibTableColumn
cfprApExtpolControllerCapability = _CfprApExtpolControllerCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 4),
    _CfprApExtpolControllerCapability_Type()
)
cfprApExtpolControllerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerCapability.setStatus("current")
_CfprApExtpolControllerConnProtocol_Type = CfprApExtpolConnProtocol
_CfprApExtpolControllerConnProtocol_Object = MibTableColumn
cfprApExtpolControllerConnProtocol = _CfprApExtpolControllerConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 5),
    _CfprApExtpolControllerConnProtocol_Type()
)
cfprApExtpolControllerConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerConnProtocol.setStatus("current")
_CfprApExtpolControllerHost_Type = SnmpAdminString
_CfprApExtpolControllerHost_Object = MibTableColumn
cfprApExtpolControllerHost = _CfprApExtpolControllerHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 6),
    _CfprApExtpolControllerHost_Type()
)
cfprApExtpolControllerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerHost.setStatus("current")
_CfprApExtpolControllerId_Type = Gauge32
_CfprApExtpolControllerId_Object = MibTableColumn
cfprApExtpolControllerId = _CfprApExtpolControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 7),
    _CfprApExtpolControllerId_Type()
)
cfprApExtpolControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerId.setStatus("current")
_CfprApExtpolControllerInterest_Type = CfprApExtpolAppCapability
_CfprApExtpolControllerInterest_Object = MibTableColumn
cfprApExtpolControllerInterest = _CfprApExtpolControllerInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 8),
    _CfprApExtpolControllerInterest_Type()
)
cfprApExtpolControllerInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerInterest.setStatus("current")
_CfprApExtpolControllerIp_Type = InetAddressIPv4
_CfprApExtpolControllerIp_Object = MibTableColumn
cfprApExtpolControllerIp = _CfprApExtpolControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 9),
    _CfprApExtpolControllerIp_Type()
)
cfprApExtpolControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerIp.setStatus("current")
_CfprApExtpolControllerIpv6_Type = InetAddressIPv6
_CfprApExtpolControllerIpv6_Object = MibTableColumn
cfprApExtpolControllerIpv6 = _CfprApExtpolControllerIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 10),
    _CfprApExtpolControllerIpv6_Type()
)
cfprApExtpolControllerIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerIpv6.setStatus("current")
_CfprApExtpolControllerLastPollTs_Type = DateAndTime
_CfprApExtpolControllerLastPollTs_Object = MibTableColumn
cfprApExtpolControllerLastPollTs = _CfprApExtpolControllerLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 11),
    _CfprApExtpolControllerLastPollTs_Type()
)
cfprApExtpolControllerLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerLastPollTs.setStatus("current")
_CfprApExtpolControllerName_Type = SnmpAdminString
_CfprApExtpolControllerName_Object = MibTableColumn
cfprApExtpolControllerName = _CfprApExtpolControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 12),
    _CfprApExtpolControllerName_Type()
)
cfprApExtpolControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerName.setStatus("current")
_CfprApExtpolControllerOperState_Type = CfprApExtpolConnectorOperState
_CfprApExtpolControllerOperState_Object = MibTableColumn
cfprApExtpolControllerOperState = _CfprApExtpolControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 13),
    _CfprApExtpolControllerOperState_Type()
)
cfprApExtpolControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerOperState.setStatus("current")
_CfprApExtpolControllerType_Type = CfprApExtpolConnType
_CfprApExtpolControllerType_Object = MibTableColumn
cfprApExtpolControllerType = _CfprApExtpolControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 14),
    _CfprApExtpolControllerType_Type()
)
cfprApExtpolControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerType.setStatus("current")
_CfprApExtpolControllerVersion_Type = SnmpAdminString
_CfprApExtpolControllerVersion_Object = MibTableColumn
cfprApExtpolControllerVersion = _CfprApExtpolControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 3, 1, 15),
    _CfprApExtpolControllerVersion_Type()
)
cfprApExtpolControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerVersion.setStatus("current")
_CfprApExtpolControllerContTable_Object = MibTable
cfprApExtpolControllerContTable = _CfprApExtpolControllerContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 4)
)
if mibBuilder.loadTexts:
    cfprApExtpolControllerContTable.setStatus("current")
_CfprApExtpolControllerContEntry_Object = MibTableRow
cfprApExtpolControllerContEntry = _CfprApExtpolControllerContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 4, 1)
)
cfprApExtpolControllerContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolControllerContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolControllerContEntry.setStatus("current")
_CfprApExtpolControllerContInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolControllerContInstanceId_Object = MibTableColumn
cfprApExtpolControllerContInstanceId = _CfprApExtpolControllerContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 4, 1, 1),
    _CfprApExtpolControllerContInstanceId_Type()
)
cfprApExtpolControllerContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolControllerContInstanceId.setStatus("current")
_CfprApExtpolControllerContDn_Type = CfprApManagedObjectDn
_CfprApExtpolControllerContDn_Object = MibTableColumn
cfprApExtpolControllerContDn = _CfprApExtpolControllerContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 4, 1, 2),
    _CfprApExtpolControllerContDn_Type()
)
cfprApExtpolControllerContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerContDn.setStatus("current")
_CfprApExtpolControllerContRn_Type = SnmpAdminString
_CfprApExtpolControllerContRn_Object = MibTableColumn
cfprApExtpolControllerContRn = _CfprApExtpolControllerContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 4, 1, 3),
    _CfprApExtpolControllerContRn_Type()
)
cfprApExtpolControllerContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerContRn.setStatus("current")
_CfprApExtpolControllerContGenNum_Type = Gauge32
_CfprApExtpolControllerContGenNum_Object = MibTableColumn
cfprApExtpolControllerContGenNum = _CfprApExtpolControllerContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 4, 1, 4),
    _CfprApExtpolControllerContGenNum_Type()
)
cfprApExtpolControllerContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolControllerContGenNum.setStatus("current")
_CfprApExtpolEpTable_Object = MibTable
cfprApExtpolEpTable = _CfprApExtpolEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5)
)
if mibBuilder.loadTexts:
    cfprApExtpolEpTable.setStatus("current")
_CfprApExtpolEpEntry_Object = MibTableRow
cfprApExtpolEpEntry = _CfprApExtpolEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1)
)
cfprApExtpolEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolEpEntry.setStatus("current")
_CfprApExtpolEpInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolEpInstanceId_Object = MibTableColumn
cfprApExtpolEpInstanceId = _CfprApExtpolEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 1),
    _CfprApExtpolEpInstanceId_Type()
)
cfprApExtpolEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolEpInstanceId.setStatus("current")
_CfprApExtpolEpDn_Type = CfprApManagedObjectDn
_CfprApExtpolEpDn_Object = MibTableColumn
cfprApExtpolEpDn = _CfprApExtpolEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 2),
    _CfprApExtpolEpDn_Type()
)
cfprApExtpolEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpDn.setStatus("current")
_CfprApExtpolEpRn_Type = SnmpAdminString
_CfprApExtpolEpRn_Object = MibTableColumn
cfprApExtpolEpRn = _CfprApExtpolEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 3),
    _CfprApExtpolEpRn_Type()
)
cfprApExtpolEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpRn.setStatus("current")
_CfprApExtpolEpFsmDescr_Type = SnmpAdminString
_CfprApExtpolEpFsmDescr_Object = MibTableColumn
cfprApExtpolEpFsmDescr = _CfprApExtpolEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 4),
    _CfprApExtpolEpFsmDescr_Type()
)
cfprApExtpolEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmDescr.setStatus("current")
_CfprApExtpolEpFsmPrev_Type = SnmpAdminString
_CfprApExtpolEpFsmPrev_Object = MibTableColumn
cfprApExtpolEpFsmPrev = _CfprApExtpolEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 5),
    _CfprApExtpolEpFsmPrev_Type()
)
cfprApExtpolEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmPrev.setStatus("current")
_CfprApExtpolEpFsmProgr_Type = Gauge32
_CfprApExtpolEpFsmProgr_Object = MibTableColumn
cfprApExtpolEpFsmProgr = _CfprApExtpolEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 6),
    _CfprApExtpolEpFsmProgr_Type()
)
cfprApExtpolEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmProgr.setStatus("current")
_CfprApExtpolEpFsmRmtInvErrCode_Type = Gauge32
_CfprApExtpolEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApExtpolEpFsmRmtInvErrCode = _CfprApExtpolEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 7),
    _CfprApExtpolEpFsmRmtInvErrCode_Type()
)
cfprApExtpolEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRmtInvErrCode.setStatus("current")
_CfprApExtpolEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApExtpolEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApExtpolEpFsmRmtInvErrDescr = _CfprApExtpolEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 8),
    _CfprApExtpolEpFsmRmtInvErrDescr_Type()
)
cfprApExtpolEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRmtInvErrDescr.setStatus("current")
_CfprApExtpolEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApExtpolEpFsmRmtInvRslt_Object = MibTableColumn
cfprApExtpolEpFsmRmtInvRslt = _CfprApExtpolEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 9),
    _CfprApExtpolEpFsmRmtInvRslt_Type()
)
cfprApExtpolEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRmtInvRslt.setStatus("current")
_CfprApExtpolEpFsmStageDescr_Type = SnmpAdminString
_CfprApExtpolEpFsmStageDescr_Object = MibTableColumn
cfprApExtpolEpFsmStageDescr = _CfprApExtpolEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 10),
    _CfprApExtpolEpFsmStageDescr_Type()
)
cfprApExtpolEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageDescr.setStatus("current")
_CfprApExtpolEpFsmStamp_Type = DateAndTime
_CfprApExtpolEpFsmStamp_Object = MibTableColumn
cfprApExtpolEpFsmStamp = _CfprApExtpolEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 11),
    _CfprApExtpolEpFsmStamp_Type()
)
cfprApExtpolEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStamp.setStatus("current")
_CfprApExtpolEpFsmStatus_Type = SnmpAdminString
_CfprApExtpolEpFsmStatus_Object = MibTableColumn
cfprApExtpolEpFsmStatus = _CfprApExtpolEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 12),
    _CfprApExtpolEpFsmStatus_Type()
)
cfprApExtpolEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStatus.setStatus("current")
_CfprApExtpolEpFsmTry_Type = Gauge32
_CfprApExtpolEpFsmTry_Object = MibTableColumn
cfprApExtpolEpFsmTry = _CfprApExtpolEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 5, 1, 13),
    _CfprApExtpolEpFsmTry_Type()
)
cfprApExtpolEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTry.setStatus("current")
_CfprApExtpolEpFsmTable_Object = MibTable
cfprApExtpolEpFsmTable = _CfprApExtpolEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6)
)
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTable.setStatus("current")
_CfprApExtpolEpFsmEntry_Object = MibTableRow
cfprApExtpolEpFsmEntry = _CfprApExtpolEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1)
)
cfprApExtpolEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmEntry.setStatus("current")
_CfprApExtpolEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolEpFsmInstanceId_Object = MibTableColumn
cfprApExtpolEpFsmInstanceId = _CfprApExtpolEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 1),
    _CfprApExtpolEpFsmInstanceId_Type()
)
cfprApExtpolEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmInstanceId.setStatus("current")
_CfprApExtpolEpFsmDn_Type = CfprApManagedObjectDn
_CfprApExtpolEpFsmDn_Object = MibTableColumn
cfprApExtpolEpFsmDn = _CfprApExtpolEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 2),
    _CfprApExtpolEpFsmDn_Type()
)
cfprApExtpolEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmDn.setStatus("current")
_CfprApExtpolEpFsmRn_Type = SnmpAdminString
_CfprApExtpolEpFsmRn_Object = MibTableColumn
cfprApExtpolEpFsmRn = _CfprApExtpolEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 3),
    _CfprApExtpolEpFsmRn_Type()
)
cfprApExtpolEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRn.setStatus("current")
_CfprApExtpolEpFsmCompletionTime_Type = DateAndTime
_CfprApExtpolEpFsmCompletionTime_Object = MibTableColumn
cfprApExtpolEpFsmCompletionTime = _CfprApExtpolEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 4),
    _CfprApExtpolEpFsmCompletionTime_Type()
)
cfprApExtpolEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmCompletionTime.setStatus("current")
_CfprApExtpolEpFsmCurrentFsm_Type = CfprApExtpolEpFsmCurrentFsm
_CfprApExtpolEpFsmCurrentFsm_Object = MibTableColumn
cfprApExtpolEpFsmCurrentFsm = _CfprApExtpolEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 5),
    _CfprApExtpolEpFsmCurrentFsm_Type()
)
cfprApExtpolEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmCurrentFsm.setStatus("current")
_CfprApExtpolEpFsmDescrData_Type = SnmpAdminString
_CfprApExtpolEpFsmDescrData_Object = MibTableColumn
cfprApExtpolEpFsmDescrData = _CfprApExtpolEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 6),
    _CfprApExtpolEpFsmDescrData_Type()
)
cfprApExtpolEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmDescrData.setStatus("current")
_CfprApExtpolEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApExtpolEpFsmFsmStatus_Object = MibTableColumn
cfprApExtpolEpFsmFsmStatus = _CfprApExtpolEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 7),
    _CfprApExtpolEpFsmFsmStatus_Type()
)
cfprApExtpolEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmFsmStatus.setStatus("current")
_CfprApExtpolEpFsmProgress_Type = Gauge32
_CfprApExtpolEpFsmProgress_Object = MibTableColumn
cfprApExtpolEpFsmProgress = _CfprApExtpolEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 8),
    _CfprApExtpolEpFsmProgress_Type()
)
cfprApExtpolEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmProgress.setStatus("current")
_CfprApExtpolEpFsmRmtErrCode_Type = Gauge32
_CfprApExtpolEpFsmRmtErrCode_Object = MibTableColumn
cfprApExtpolEpFsmRmtErrCode = _CfprApExtpolEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 9),
    _CfprApExtpolEpFsmRmtErrCode_Type()
)
cfprApExtpolEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRmtErrCode.setStatus("current")
_CfprApExtpolEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApExtpolEpFsmRmtErrDescr_Object = MibTableColumn
cfprApExtpolEpFsmRmtErrDescr = _CfprApExtpolEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 10),
    _CfprApExtpolEpFsmRmtErrDescr_Type()
)
cfprApExtpolEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRmtErrDescr.setStatus("current")
_CfprApExtpolEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApExtpolEpFsmRmtRslt_Object = MibTableColumn
cfprApExtpolEpFsmRmtRslt = _CfprApExtpolEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 6, 1, 11),
    _CfprApExtpolEpFsmRmtRslt_Type()
)
cfprApExtpolEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmRmtRslt.setStatus("current")
_CfprApExtpolEpFsmStageTable_Object = MibTable
cfprApExtpolEpFsmStageTable = _CfprApExtpolEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7)
)
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageTable.setStatus("current")
_CfprApExtpolEpFsmStageEntry_Object = MibTableRow
cfprApExtpolEpFsmStageEntry = _CfprApExtpolEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1)
)
cfprApExtpolEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageEntry.setStatus("current")
_CfprApExtpolEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolEpFsmStageInstanceId_Object = MibTableColumn
cfprApExtpolEpFsmStageInstanceId = _CfprApExtpolEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 1),
    _CfprApExtpolEpFsmStageInstanceId_Type()
)
cfprApExtpolEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageInstanceId.setStatus("current")
_CfprApExtpolEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApExtpolEpFsmStageDn_Object = MibTableColumn
cfprApExtpolEpFsmStageDn = _CfprApExtpolEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 2),
    _CfprApExtpolEpFsmStageDn_Type()
)
cfprApExtpolEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageDn.setStatus("current")
_CfprApExtpolEpFsmStageRn_Type = SnmpAdminString
_CfprApExtpolEpFsmStageRn_Object = MibTableColumn
cfprApExtpolEpFsmStageRn = _CfprApExtpolEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 3),
    _CfprApExtpolEpFsmStageRn_Type()
)
cfprApExtpolEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageRn.setStatus("current")
_CfprApExtpolEpFsmStageDescrData_Type = SnmpAdminString
_CfprApExtpolEpFsmStageDescrData_Object = MibTableColumn
cfprApExtpolEpFsmStageDescrData = _CfprApExtpolEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 4),
    _CfprApExtpolEpFsmStageDescrData_Type()
)
cfprApExtpolEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageDescrData.setStatus("current")
_CfprApExtpolEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApExtpolEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApExtpolEpFsmStageLastUpdateTime = _CfprApExtpolEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 5),
    _CfprApExtpolEpFsmStageLastUpdateTime_Type()
)
cfprApExtpolEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageLastUpdateTime.setStatus("current")
_CfprApExtpolEpFsmStageName_Type = CfprApExtpolEpFsmStageName
_CfprApExtpolEpFsmStageName_Object = MibTableColumn
cfprApExtpolEpFsmStageName = _CfprApExtpolEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 6),
    _CfprApExtpolEpFsmStageName_Type()
)
cfprApExtpolEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageName.setStatus("current")
_CfprApExtpolEpFsmStageOrder_Type = Gauge32
_CfprApExtpolEpFsmStageOrder_Object = MibTableColumn
cfprApExtpolEpFsmStageOrder = _CfprApExtpolEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 7),
    _CfprApExtpolEpFsmStageOrder_Type()
)
cfprApExtpolEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageOrder.setStatus("current")
_CfprApExtpolEpFsmStageRetry_Type = Gauge32
_CfprApExtpolEpFsmStageRetry_Object = MibTableColumn
cfprApExtpolEpFsmStageRetry = _CfprApExtpolEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 8),
    _CfprApExtpolEpFsmStageRetry_Type()
)
cfprApExtpolEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageRetry.setStatus("current")
_CfprApExtpolEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApExtpolEpFsmStageStageStatus_Object = MibTableColumn
cfprApExtpolEpFsmStageStageStatus = _CfprApExtpolEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 7, 1, 9),
    _CfprApExtpolEpFsmStageStageStatus_Type()
)
cfprApExtpolEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmStageStageStatus.setStatus("current")
_CfprApExtpolEpFsmTaskTable_Object = MibTable
cfprApExtpolEpFsmTaskTable = _CfprApExtpolEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8)
)
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskTable.setStatus("current")
_CfprApExtpolEpFsmTaskEntry_Object = MibTableRow
cfprApExtpolEpFsmTaskEntry = _CfprApExtpolEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1)
)
cfprApExtpolEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskEntry.setStatus("current")
_CfprApExtpolEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolEpFsmTaskInstanceId_Object = MibTableColumn
cfprApExtpolEpFsmTaskInstanceId = _CfprApExtpolEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 1),
    _CfprApExtpolEpFsmTaskInstanceId_Type()
)
cfprApExtpolEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskInstanceId.setStatus("current")
_CfprApExtpolEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApExtpolEpFsmTaskDn_Object = MibTableColumn
cfprApExtpolEpFsmTaskDn = _CfprApExtpolEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 2),
    _CfprApExtpolEpFsmTaskDn_Type()
)
cfprApExtpolEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskDn.setStatus("current")
_CfprApExtpolEpFsmTaskRn_Type = SnmpAdminString
_CfprApExtpolEpFsmTaskRn_Object = MibTableColumn
cfprApExtpolEpFsmTaskRn = _CfprApExtpolEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 3),
    _CfprApExtpolEpFsmTaskRn_Type()
)
cfprApExtpolEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskRn.setStatus("current")
_CfprApExtpolEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApExtpolEpFsmTaskCompletion_Object = MibTableColumn
cfprApExtpolEpFsmTaskCompletion = _CfprApExtpolEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 4),
    _CfprApExtpolEpFsmTaskCompletion_Type()
)
cfprApExtpolEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskCompletion.setStatus("current")
_CfprApExtpolEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApExtpolEpFsmTaskFlags_Object = MibTableColumn
cfprApExtpolEpFsmTaskFlags = _CfprApExtpolEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 5),
    _CfprApExtpolEpFsmTaskFlags_Type()
)
cfprApExtpolEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskFlags.setStatus("current")
_CfprApExtpolEpFsmTaskItem_Type = CfprApExtpolEpFsmTaskItem
_CfprApExtpolEpFsmTaskItem_Object = MibTableColumn
cfprApExtpolEpFsmTaskItem = _CfprApExtpolEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 6),
    _CfprApExtpolEpFsmTaskItem_Type()
)
cfprApExtpolEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskItem.setStatus("current")
_CfprApExtpolEpFsmTaskSeqId_Type = Gauge32
_CfprApExtpolEpFsmTaskSeqId_Object = MibTableColumn
cfprApExtpolEpFsmTaskSeqId = _CfprApExtpolEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 8, 1, 7),
    _CfprApExtpolEpFsmTaskSeqId_Type()
)
cfprApExtpolEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolEpFsmTaskSeqId.setStatus("current")
_CfprApExtpolProviderTable_Object = MibTable
cfprApExtpolProviderTable = _CfprApExtpolProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9)
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderTable.setStatus("current")
_CfprApExtpolProviderEntry_Object = MibTableRow
cfprApExtpolProviderEntry = _CfprApExtpolProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1)
)
cfprApExtpolProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderEntry.setStatus("current")
_CfprApExtpolProviderInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolProviderInstanceId_Object = MibTableColumn
cfprApExtpolProviderInstanceId = _CfprApExtpolProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 1),
    _CfprApExtpolProviderInstanceId_Type()
)
cfprApExtpolProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolProviderInstanceId.setStatus("current")
_CfprApExtpolProviderDn_Type = CfprApManagedObjectDn
_CfprApExtpolProviderDn_Object = MibTableColumn
cfprApExtpolProviderDn = _CfprApExtpolProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 2),
    _CfprApExtpolProviderDn_Type()
)
cfprApExtpolProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderDn.setStatus("current")
_CfprApExtpolProviderRn_Type = SnmpAdminString
_CfprApExtpolProviderRn_Object = MibTableColumn
cfprApExtpolProviderRn = _CfprApExtpolProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 3),
    _CfprApExtpolProviderRn_Type()
)
cfprApExtpolProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderRn.setStatus("current")
_CfprApExtpolProviderCapability_Type = CfprApExtpolAppCapability
_CfprApExtpolProviderCapability_Object = MibTableColumn
cfprApExtpolProviderCapability = _CfprApExtpolProviderCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 4),
    _CfprApExtpolProviderCapability_Type()
)
cfprApExtpolProviderCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderCapability.setStatus("current")
_CfprApExtpolProviderConnProtocol_Type = CfprApExtpolConnProtocol
_CfprApExtpolProviderConnProtocol_Object = MibTableColumn
cfprApExtpolProviderConnProtocol = _CfprApExtpolProviderConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 5),
    _CfprApExtpolProviderConnProtocol_Type()
)
cfprApExtpolProviderConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderConnProtocol.setStatus("current")
_CfprApExtpolProviderFsmDescr_Type = SnmpAdminString
_CfprApExtpolProviderFsmDescr_Object = MibTableColumn
cfprApExtpolProviderFsmDescr = _CfprApExtpolProviderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 6),
    _CfprApExtpolProviderFsmDescr_Type()
)
cfprApExtpolProviderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmDescr.setStatus("current")
_CfprApExtpolProviderFsmPrev_Type = SnmpAdminString
_CfprApExtpolProviderFsmPrev_Object = MibTableColumn
cfprApExtpolProviderFsmPrev = _CfprApExtpolProviderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 7),
    _CfprApExtpolProviderFsmPrev_Type()
)
cfprApExtpolProviderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmPrev.setStatus("current")
_CfprApExtpolProviderFsmProgr_Type = Gauge32
_CfprApExtpolProviderFsmProgr_Object = MibTableColumn
cfprApExtpolProviderFsmProgr = _CfprApExtpolProviderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 8),
    _CfprApExtpolProviderFsmProgr_Type()
)
cfprApExtpolProviderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmProgr.setStatus("current")
_CfprApExtpolProviderFsmRmtInvErrCode_Type = Gauge32
_CfprApExtpolProviderFsmRmtInvErrCode_Object = MibTableColumn
cfprApExtpolProviderFsmRmtInvErrCode = _CfprApExtpolProviderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 9),
    _CfprApExtpolProviderFsmRmtInvErrCode_Type()
)
cfprApExtpolProviderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRmtInvErrCode.setStatus("current")
_CfprApExtpolProviderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApExtpolProviderFsmRmtInvErrDescr_Object = MibTableColumn
cfprApExtpolProviderFsmRmtInvErrDescr = _CfprApExtpolProviderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 10),
    _CfprApExtpolProviderFsmRmtInvErrDescr_Type()
)
cfprApExtpolProviderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRmtInvErrDescr.setStatus("current")
_CfprApExtpolProviderFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApExtpolProviderFsmRmtInvRslt_Object = MibTableColumn
cfprApExtpolProviderFsmRmtInvRslt = _CfprApExtpolProviderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 11),
    _CfprApExtpolProviderFsmRmtInvRslt_Type()
)
cfprApExtpolProviderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRmtInvRslt.setStatus("current")
_CfprApExtpolProviderFsmStageDescr_Type = SnmpAdminString
_CfprApExtpolProviderFsmStageDescr_Object = MibTableColumn
cfprApExtpolProviderFsmStageDescr = _CfprApExtpolProviderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 12),
    _CfprApExtpolProviderFsmStageDescr_Type()
)
cfprApExtpolProviderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageDescr.setStatus("current")
_CfprApExtpolProviderFsmStamp_Type = DateAndTime
_CfprApExtpolProviderFsmStamp_Object = MibTableColumn
cfprApExtpolProviderFsmStamp = _CfprApExtpolProviderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 13),
    _CfprApExtpolProviderFsmStamp_Type()
)
cfprApExtpolProviderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStamp.setStatus("current")
_CfprApExtpolProviderFsmStatus_Type = SnmpAdminString
_CfprApExtpolProviderFsmStatus_Object = MibTableColumn
cfprApExtpolProviderFsmStatus = _CfprApExtpolProviderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 14),
    _CfprApExtpolProviderFsmStatus_Type()
)
cfprApExtpolProviderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStatus.setStatus("current")
_CfprApExtpolProviderFsmTry_Type = Gauge32
_CfprApExtpolProviderFsmTry_Object = MibTableColumn
cfprApExtpolProviderFsmTry = _CfprApExtpolProviderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 15),
    _CfprApExtpolProviderFsmTry_Type()
)
cfprApExtpolProviderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTry.setStatus("current")
_CfprApExtpolProviderHost_Type = SnmpAdminString
_CfprApExtpolProviderHost_Object = MibTableColumn
cfprApExtpolProviderHost = _CfprApExtpolProviderHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 16),
    _CfprApExtpolProviderHost_Type()
)
cfprApExtpolProviderHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderHost.setStatus("current")
_CfprApExtpolProviderId_Type = Gauge32
_CfprApExtpolProviderId_Object = MibTableColumn
cfprApExtpolProviderId = _CfprApExtpolProviderId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 17),
    _CfprApExtpolProviderId_Type()
)
cfprApExtpolProviderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderId.setStatus("current")
_CfprApExtpolProviderInterest_Type = CfprApExtpolAppCapability
_CfprApExtpolProviderInterest_Object = MibTableColumn
cfprApExtpolProviderInterest = _CfprApExtpolProviderInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 18),
    _CfprApExtpolProviderInterest_Type()
)
cfprApExtpolProviderInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderInterest.setStatus("current")
_CfprApExtpolProviderIp_Type = InetAddressIPv4
_CfprApExtpolProviderIp_Object = MibTableColumn
cfprApExtpolProviderIp = _CfprApExtpolProviderIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 19),
    _CfprApExtpolProviderIp_Type()
)
cfprApExtpolProviderIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderIp.setStatus("current")
_CfprApExtpolProviderIpv6_Type = InetAddressIPv6
_CfprApExtpolProviderIpv6_Object = MibTableColumn
cfprApExtpolProviderIpv6 = _CfprApExtpolProviderIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 20),
    _CfprApExtpolProviderIpv6_Type()
)
cfprApExtpolProviderIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderIpv6.setStatus("current")
_CfprApExtpolProviderLastPollTs_Type = DateAndTime
_CfprApExtpolProviderLastPollTs_Object = MibTableColumn
cfprApExtpolProviderLastPollTs = _CfprApExtpolProviderLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 21),
    _CfprApExtpolProviderLastPollTs_Type()
)
cfprApExtpolProviderLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderLastPollTs.setStatus("current")
_CfprApExtpolProviderName_Type = SnmpAdminString
_CfprApExtpolProviderName_Object = MibTableColumn
cfprApExtpolProviderName = _CfprApExtpolProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 22),
    _CfprApExtpolProviderName_Type()
)
cfprApExtpolProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderName.setStatus("current")
_CfprApExtpolProviderOperState_Type = CfprApExtpolConnectorOperState
_CfprApExtpolProviderOperState_Object = MibTableColumn
cfprApExtpolProviderOperState = _CfprApExtpolProviderOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 23),
    _CfprApExtpolProviderOperState_Type()
)
cfprApExtpolProviderOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderOperState.setStatus("current")
_CfprApExtpolProviderType_Type = CfprApExtpolConnType
_CfprApExtpolProviderType_Object = MibTableColumn
cfprApExtpolProviderType = _CfprApExtpolProviderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 24),
    _CfprApExtpolProviderType_Type()
)
cfprApExtpolProviderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderType.setStatus("current")
_CfprApExtpolProviderVersion_Type = SnmpAdminString
_CfprApExtpolProviderVersion_Object = MibTableColumn
cfprApExtpolProviderVersion = _CfprApExtpolProviderVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 9, 1, 25),
    _CfprApExtpolProviderVersion_Type()
)
cfprApExtpolProviderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderVersion.setStatus("current")
_CfprApExtpolProviderContTable_Object = MibTable
cfprApExtpolProviderContTable = _CfprApExtpolProviderContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 10)
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderContTable.setStatus("current")
_CfprApExtpolProviderContEntry_Object = MibTableRow
cfprApExtpolProviderContEntry = _CfprApExtpolProviderContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 10, 1)
)
cfprApExtpolProviderContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolProviderContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderContEntry.setStatus("current")
_CfprApExtpolProviderContInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolProviderContInstanceId_Object = MibTableColumn
cfprApExtpolProviderContInstanceId = _CfprApExtpolProviderContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 10, 1, 1),
    _CfprApExtpolProviderContInstanceId_Type()
)
cfprApExtpolProviderContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolProviderContInstanceId.setStatus("current")
_CfprApExtpolProviderContDn_Type = CfprApManagedObjectDn
_CfprApExtpolProviderContDn_Object = MibTableColumn
cfprApExtpolProviderContDn = _CfprApExtpolProviderContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 10, 1, 2),
    _CfprApExtpolProviderContDn_Type()
)
cfprApExtpolProviderContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderContDn.setStatus("current")
_CfprApExtpolProviderContRn_Type = SnmpAdminString
_CfprApExtpolProviderContRn_Object = MibTableColumn
cfprApExtpolProviderContRn = _CfprApExtpolProviderContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 10, 1, 3),
    _CfprApExtpolProviderContRn_Type()
)
cfprApExtpolProviderContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderContRn.setStatus("current")
_CfprApExtpolProviderContGenNum_Type = Gauge32
_CfprApExtpolProviderContGenNum_Object = MibTableColumn
cfprApExtpolProviderContGenNum = _CfprApExtpolProviderContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 10, 1, 4),
    _CfprApExtpolProviderContGenNum_Type()
)
cfprApExtpolProviderContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderContGenNum.setStatus("current")
_CfprApExtpolProviderFsmTable_Object = MibTable
cfprApExtpolProviderFsmTable = _CfprApExtpolProviderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11)
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTable.setStatus("current")
_CfprApExtpolProviderFsmEntry_Object = MibTableRow
cfprApExtpolProviderFsmEntry = _CfprApExtpolProviderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1)
)
cfprApExtpolProviderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolProviderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmEntry.setStatus("current")
_CfprApExtpolProviderFsmInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolProviderFsmInstanceId_Object = MibTableColumn
cfprApExtpolProviderFsmInstanceId = _CfprApExtpolProviderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 1),
    _CfprApExtpolProviderFsmInstanceId_Type()
)
cfprApExtpolProviderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmInstanceId.setStatus("current")
_CfprApExtpolProviderFsmDn_Type = CfprApManagedObjectDn
_CfprApExtpolProviderFsmDn_Object = MibTableColumn
cfprApExtpolProviderFsmDn = _CfprApExtpolProviderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 2),
    _CfprApExtpolProviderFsmDn_Type()
)
cfprApExtpolProviderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmDn.setStatus("current")
_CfprApExtpolProviderFsmRn_Type = SnmpAdminString
_CfprApExtpolProviderFsmRn_Object = MibTableColumn
cfprApExtpolProviderFsmRn = _CfprApExtpolProviderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 3),
    _CfprApExtpolProviderFsmRn_Type()
)
cfprApExtpolProviderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRn.setStatus("current")
_CfprApExtpolProviderFsmCompletionTime_Type = DateAndTime
_CfprApExtpolProviderFsmCompletionTime_Object = MibTableColumn
cfprApExtpolProviderFsmCompletionTime = _CfprApExtpolProviderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 4),
    _CfprApExtpolProviderFsmCompletionTime_Type()
)
cfprApExtpolProviderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmCompletionTime.setStatus("current")
_CfprApExtpolProviderFsmCurrentFsm_Type = CfprApExtpolProviderFsmCurrentFsm
_CfprApExtpolProviderFsmCurrentFsm_Object = MibTableColumn
cfprApExtpolProviderFsmCurrentFsm = _CfprApExtpolProviderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 5),
    _CfprApExtpolProviderFsmCurrentFsm_Type()
)
cfprApExtpolProviderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmCurrentFsm.setStatus("current")
_CfprApExtpolProviderFsmDescrData_Type = SnmpAdminString
_CfprApExtpolProviderFsmDescrData_Object = MibTableColumn
cfprApExtpolProviderFsmDescrData = _CfprApExtpolProviderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 6),
    _CfprApExtpolProviderFsmDescrData_Type()
)
cfprApExtpolProviderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmDescrData.setStatus("current")
_CfprApExtpolProviderFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApExtpolProviderFsmFsmStatus_Object = MibTableColumn
cfprApExtpolProviderFsmFsmStatus = _CfprApExtpolProviderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 7),
    _CfprApExtpolProviderFsmFsmStatus_Type()
)
cfprApExtpolProviderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmFsmStatus.setStatus("current")
_CfprApExtpolProviderFsmProgress_Type = Gauge32
_CfprApExtpolProviderFsmProgress_Object = MibTableColumn
cfprApExtpolProviderFsmProgress = _CfprApExtpolProviderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 8),
    _CfprApExtpolProviderFsmProgress_Type()
)
cfprApExtpolProviderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmProgress.setStatus("current")
_CfprApExtpolProviderFsmRmtErrCode_Type = Gauge32
_CfprApExtpolProviderFsmRmtErrCode_Object = MibTableColumn
cfprApExtpolProviderFsmRmtErrCode = _CfprApExtpolProviderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 9),
    _CfprApExtpolProviderFsmRmtErrCode_Type()
)
cfprApExtpolProviderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRmtErrCode.setStatus("current")
_CfprApExtpolProviderFsmRmtErrDescr_Type = SnmpAdminString
_CfprApExtpolProviderFsmRmtErrDescr_Object = MibTableColumn
cfprApExtpolProviderFsmRmtErrDescr = _CfprApExtpolProviderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 10),
    _CfprApExtpolProviderFsmRmtErrDescr_Type()
)
cfprApExtpolProviderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRmtErrDescr.setStatus("current")
_CfprApExtpolProviderFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApExtpolProviderFsmRmtRslt_Object = MibTableColumn
cfprApExtpolProviderFsmRmtRslt = _CfprApExtpolProviderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 11, 1, 11),
    _CfprApExtpolProviderFsmRmtRslt_Type()
)
cfprApExtpolProviderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmRmtRslt.setStatus("current")
_CfprApExtpolProviderFsmStageTable_Object = MibTable
cfprApExtpolProviderFsmStageTable = _CfprApExtpolProviderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12)
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageTable.setStatus("current")
_CfprApExtpolProviderFsmStageEntry_Object = MibTableRow
cfprApExtpolProviderFsmStageEntry = _CfprApExtpolProviderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1)
)
cfprApExtpolProviderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolProviderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageEntry.setStatus("current")
_CfprApExtpolProviderFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolProviderFsmStageInstanceId_Object = MibTableColumn
cfprApExtpolProviderFsmStageInstanceId = _CfprApExtpolProviderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 1),
    _CfprApExtpolProviderFsmStageInstanceId_Type()
)
cfprApExtpolProviderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageInstanceId.setStatus("current")
_CfprApExtpolProviderFsmStageDn_Type = CfprApManagedObjectDn
_CfprApExtpolProviderFsmStageDn_Object = MibTableColumn
cfprApExtpolProviderFsmStageDn = _CfprApExtpolProviderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 2),
    _CfprApExtpolProviderFsmStageDn_Type()
)
cfprApExtpolProviderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageDn.setStatus("current")
_CfprApExtpolProviderFsmStageRn_Type = SnmpAdminString
_CfprApExtpolProviderFsmStageRn_Object = MibTableColumn
cfprApExtpolProviderFsmStageRn = _CfprApExtpolProviderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 3),
    _CfprApExtpolProviderFsmStageRn_Type()
)
cfprApExtpolProviderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageRn.setStatus("current")
_CfprApExtpolProviderFsmStageDescrData_Type = SnmpAdminString
_CfprApExtpolProviderFsmStageDescrData_Object = MibTableColumn
cfprApExtpolProviderFsmStageDescrData = _CfprApExtpolProviderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 4),
    _CfprApExtpolProviderFsmStageDescrData_Type()
)
cfprApExtpolProviderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageDescrData.setStatus("current")
_CfprApExtpolProviderFsmStageLastUpdateTime_Type = DateAndTime
_CfprApExtpolProviderFsmStageLastUpdateTime_Object = MibTableColumn
cfprApExtpolProviderFsmStageLastUpdateTime = _CfprApExtpolProviderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 5),
    _CfprApExtpolProviderFsmStageLastUpdateTime_Type()
)
cfprApExtpolProviderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageLastUpdateTime.setStatus("current")
_CfprApExtpolProviderFsmStageName_Type = CfprApExtpolProviderFsmStageName
_CfprApExtpolProviderFsmStageName_Object = MibTableColumn
cfprApExtpolProviderFsmStageName = _CfprApExtpolProviderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 6),
    _CfprApExtpolProviderFsmStageName_Type()
)
cfprApExtpolProviderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageName.setStatus("current")
_CfprApExtpolProviderFsmStageOrder_Type = Gauge32
_CfprApExtpolProviderFsmStageOrder_Object = MibTableColumn
cfprApExtpolProviderFsmStageOrder = _CfprApExtpolProviderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 7),
    _CfprApExtpolProviderFsmStageOrder_Type()
)
cfprApExtpolProviderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageOrder.setStatus("current")
_CfprApExtpolProviderFsmStageRetry_Type = Gauge32
_CfprApExtpolProviderFsmStageRetry_Object = MibTableColumn
cfprApExtpolProviderFsmStageRetry = _CfprApExtpolProviderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 8),
    _CfprApExtpolProviderFsmStageRetry_Type()
)
cfprApExtpolProviderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageRetry.setStatus("current")
_CfprApExtpolProviderFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApExtpolProviderFsmStageStageStatus_Object = MibTableColumn
cfprApExtpolProviderFsmStageStageStatus = _CfprApExtpolProviderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 12, 1, 9),
    _CfprApExtpolProviderFsmStageStageStatus_Type()
)
cfprApExtpolProviderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmStageStageStatus.setStatus("current")
_CfprApExtpolProviderFsmTaskTable_Object = MibTable
cfprApExtpolProviderFsmTaskTable = _CfprApExtpolProviderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13)
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskTable.setStatus("current")
_CfprApExtpolProviderFsmTaskEntry_Object = MibTableRow
cfprApExtpolProviderFsmTaskEntry = _CfprApExtpolProviderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1)
)
cfprApExtpolProviderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolProviderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskEntry.setStatus("current")
_CfprApExtpolProviderFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolProviderFsmTaskInstanceId_Object = MibTableColumn
cfprApExtpolProviderFsmTaskInstanceId = _CfprApExtpolProviderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 1),
    _CfprApExtpolProviderFsmTaskInstanceId_Type()
)
cfprApExtpolProviderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskInstanceId.setStatus("current")
_CfprApExtpolProviderFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApExtpolProviderFsmTaskDn_Object = MibTableColumn
cfprApExtpolProviderFsmTaskDn = _CfprApExtpolProviderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 2),
    _CfprApExtpolProviderFsmTaskDn_Type()
)
cfprApExtpolProviderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskDn.setStatus("current")
_CfprApExtpolProviderFsmTaskRn_Type = SnmpAdminString
_CfprApExtpolProviderFsmTaskRn_Object = MibTableColumn
cfprApExtpolProviderFsmTaskRn = _CfprApExtpolProviderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 3),
    _CfprApExtpolProviderFsmTaskRn_Type()
)
cfprApExtpolProviderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskRn.setStatus("current")
_CfprApExtpolProviderFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApExtpolProviderFsmTaskCompletion_Object = MibTableColumn
cfprApExtpolProviderFsmTaskCompletion = _CfprApExtpolProviderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 4),
    _CfprApExtpolProviderFsmTaskCompletion_Type()
)
cfprApExtpolProviderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskCompletion.setStatus("current")
_CfprApExtpolProviderFsmTaskFlags_Type = CfprApFsmFlags
_CfprApExtpolProviderFsmTaskFlags_Object = MibTableColumn
cfprApExtpolProviderFsmTaskFlags = _CfprApExtpolProviderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 5),
    _CfprApExtpolProviderFsmTaskFlags_Type()
)
cfprApExtpolProviderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskFlags.setStatus("current")
_CfprApExtpolProviderFsmTaskItem_Type = CfprApExtpolProviderFsmTaskItem
_CfprApExtpolProviderFsmTaskItem_Object = MibTableColumn
cfprApExtpolProviderFsmTaskItem = _CfprApExtpolProviderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 6),
    _CfprApExtpolProviderFsmTaskItem_Type()
)
cfprApExtpolProviderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskItem.setStatus("current")
_CfprApExtpolProviderFsmTaskSeqId_Type = Gauge32
_CfprApExtpolProviderFsmTaskSeqId_Object = MibTableColumn
cfprApExtpolProviderFsmTaskSeqId = _CfprApExtpolProviderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 13, 1, 7),
    _CfprApExtpolProviderFsmTaskSeqId_Type()
)
cfprApExtpolProviderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolProviderFsmTaskSeqId.setStatus("current")
_CfprApExtpolRegistryTable_Object = MibTable
cfprApExtpolRegistryTable = _CfprApExtpolRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14)
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryTable.setStatus("current")
_CfprApExtpolRegistryEntry_Object = MibTableRow
cfprApExtpolRegistryEntry = _CfprApExtpolRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1)
)
cfprApExtpolRegistryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolRegistryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryEntry.setStatus("current")
_CfprApExtpolRegistryInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolRegistryInstanceId_Object = MibTableColumn
cfprApExtpolRegistryInstanceId = _CfprApExtpolRegistryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 1),
    _CfprApExtpolRegistryInstanceId_Type()
)
cfprApExtpolRegistryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryInstanceId.setStatus("current")
_CfprApExtpolRegistryDn_Type = CfprApManagedObjectDn
_CfprApExtpolRegistryDn_Object = MibTableColumn
cfprApExtpolRegistryDn = _CfprApExtpolRegistryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 2),
    _CfprApExtpolRegistryDn_Type()
)
cfprApExtpolRegistryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryDn.setStatus("current")
_CfprApExtpolRegistryRn_Type = SnmpAdminString
_CfprApExtpolRegistryRn_Object = MibTableColumn
cfprApExtpolRegistryRn = _CfprApExtpolRegistryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 3),
    _CfprApExtpolRegistryRn_Type()
)
cfprApExtpolRegistryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryRn.setStatus("current")
_CfprApExtpolRegistryCapability_Type = CfprApExtpolAppCapability
_CfprApExtpolRegistryCapability_Object = MibTableColumn
cfprApExtpolRegistryCapability = _CfprApExtpolRegistryCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 4),
    _CfprApExtpolRegistryCapability_Type()
)
cfprApExtpolRegistryCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryCapability.setStatus("current")
_CfprApExtpolRegistryConnProtocol_Type = CfprApExtpolConnProtocol
_CfprApExtpolRegistryConnProtocol_Object = MibTableColumn
cfprApExtpolRegistryConnProtocol = _CfprApExtpolRegistryConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 5),
    _CfprApExtpolRegistryConnProtocol_Type()
)
cfprApExtpolRegistryConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryConnProtocol.setStatus("current")
_CfprApExtpolRegistryFsmDescr_Type = SnmpAdminString
_CfprApExtpolRegistryFsmDescr_Object = MibTableColumn
cfprApExtpolRegistryFsmDescr = _CfprApExtpolRegistryFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 6),
    _CfprApExtpolRegistryFsmDescr_Type()
)
cfprApExtpolRegistryFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmDescr.setStatus("current")
_CfprApExtpolRegistryFsmPrev_Type = SnmpAdminString
_CfprApExtpolRegistryFsmPrev_Object = MibTableColumn
cfprApExtpolRegistryFsmPrev = _CfprApExtpolRegistryFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 7),
    _CfprApExtpolRegistryFsmPrev_Type()
)
cfprApExtpolRegistryFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmPrev.setStatus("current")
_CfprApExtpolRegistryFsmProgr_Type = Gauge32
_CfprApExtpolRegistryFsmProgr_Object = MibTableColumn
cfprApExtpolRegistryFsmProgr = _CfprApExtpolRegistryFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 8),
    _CfprApExtpolRegistryFsmProgr_Type()
)
cfprApExtpolRegistryFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmProgr.setStatus("current")
_CfprApExtpolRegistryFsmRmtInvErrCode_Type = Gauge32
_CfprApExtpolRegistryFsmRmtInvErrCode_Object = MibTableColumn
cfprApExtpolRegistryFsmRmtInvErrCode = _CfprApExtpolRegistryFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 9),
    _CfprApExtpolRegistryFsmRmtInvErrCode_Type()
)
cfprApExtpolRegistryFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRmtInvErrCode.setStatus("current")
_CfprApExtpolRegistryFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApExtpolRegistryFsmRmtInvErrDescr_Object = MibTableColumn
cfprApExtpolRegistryFsmRmtInvErrDescr = _CfprApExtpolRegistryFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 10),
    _CfprApExtpolRegistryFsmRmtInvErrDescr_Type()
)
cfprApExtpolRegistryFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRmtInvErrDescr.setStatus("current")
_CfprApExtpolRegistryFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApExtpolRegistryFsmRmtInvRslt_Object = MibTableColumn
cfprApExtpolRegistryFsmRmtInvRslt = _CfprApExtpolRegistryFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 11),
    _CfprApExtpolRegistryFsmRmtInvRslt_Type()
)
cfprApExtpolRegistryFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRmtInvRslt.setStatus("current")
_CfprApExtpolRegistryFsmStageDescr_Type = SnmpAdminString
_CfprApExtpolRegistryFsmStageDescr_Object = MibTableColumn
cfprApExtpolRegistryFsmStageDescr = _CfprApExtpolRegistryFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 12),
    _CfprApExtpolRegistryFsmStageDescr_Type()
)
cfprApExtpolRegistryFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageDescr.setStatus("current")
_CfprApExtpolRegistryFsmStamp_Type = DateAndTime
_CfprApExtpolRegistryFsmStamp_Object = MibTableColumn
cfprApExtpolRegistryFsmStamp = _CfprApExtpolRegistryFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 13),
    _CfprApExtpolRegistryFsmStamp_Type()
)
cfprApExtpolRegistryFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStamp.setStatus("current")
_CfprApExtpolRegistryFsmStatus_Type = SnmpAdminString
_CfprApExtpolRegistryFsmStatus_Object = MibTableColumn
cfprApExtpolRegistryFsmStatus = _CfprApExtpolRegistryFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 14),
    _CfprApExtpolRegistryFsmStatus_Type()
)
cfprApExtpolRegistryFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStatus.setStatus("current")
_CfprApExtpolRegistryFsmTry_Type = Gauge32
_CfprApExtpolRegistryFsmTry_Object = MibTableColumn
cfprApExtpolRegistryFsmTry = _CfprApExtpolRegistryFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 15),
    _CfprApExtpolRegistryFsmTry_Type()
)
cfprApExtpolRegistryFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTry.setStatus("current")
_CfprApExtpolRegistryGenNum_Type = Gauge32
_CfprApExtpolRegistryGenNum_Object = MibTableColumn
cfprApExtpolRegistryGenNum = _CfprApExtpolRegistryGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 16),
    _CfprApExtpolRegistryGenNum_Type()
)
cfprApExtpolRegistryGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryGenNum.setStatus("current")
_CfprApExtpolRegistryGuid_Type = SnmpAdminString
_CfprApExtpolRegistryGuid_Object = MibTableColumn
cfprApExtpolRegistryGuid = _CfprApExtpolRegistryGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 17),
    _CfprApExtpolRegistryGuid_Type()
)
cfprApExtpolRegistryGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryGuid.setStatus("current")
_CfprApExtpolRegistryHost_Type = SnmpAdminString
_CfprApExtpolRegistryHost_Object = MibTableColumn
cfprApExtpolRegistryHost = _CfprApExtpolRegistryHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 18),
    _CfprApExtpolRegistryHost_Type()
)
cfprApExtpolRegistryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryHost.setStatus("current")
_CfprApExtpolRegistryId_Type = Gauge32
_CfprApExtpolRegistryId_Object = MibTableColumn
cfprApExtpolRegistryId = _CfprApExtpolRegistryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 19),
    _CfprApExtpolRegistryId_Type()
)
cfprApExtpolRegistryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryId.setStatus("current")
_CfprApExtpolRegistryIdCount_Type = Gauge32
_CfprApExtpolRegistryIdCount_Object = MibTableColumn
cfprApExtpolRegistryIdCount = _CfprApExtpolRegistryIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 20),
    _CfprApExtpolRegistryIdCount_Type()
)
cfprApExtpolRegistryIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryIdCount.setStatus("current")
_CfprApExtpolRegistryInterest_Type = CfprApExtpolAppCapability
_CfprApExtpolRegistryInterest_Object = MibTableColumn
cfprApExtpolRegistryInterest = _CfprApExtpolRegistryInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 21),
    _CfprApExtpolRegistryInterest_Type()
)
cfprApExtpolRegistryInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryInterest.setStatus("current")
_CfprApExtpolRegistryIp_Type = InetAddressIPv4
_CfprApExtpolRegistryIp_Object = MibTableColumn
cfprApExtpolRegistryIp = _CfprApExtpolRegistryIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 22),
    _CfprApExtpolRegistryIp_Type()
)
cfprApExtpolRegistryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryIp.setStatus("current")
_CfprApExtpolRegistryIpv6_Type = InetAddressIPv6
_CfprApExtpolRegistryIpv6_Object = MibTableColumn
cfprApExtpolRegistryIpv6 = _CfprApExtpolRegistryIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 23),
    _CfprApExtpolRegistryIpv6_Type()
)
cfprApExtpolRegistryIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryIpv6.setStatus("current")
_CfprApExtpolRegistryLastPollTs_Type = DateAndTime
_CfprApExtpolRegistryLastPollTs_Object = MibTableColumn
cfprApExtpolRegistryLastPollTs = _CfprApExtpolRegistryLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 24),
    _CfprApExtpolRegistryLastPollTs_Type()
)
cfprApExtpolRegistryLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryLastPollTs.setStatus("current")
_CfprApExtpolRegistryName_Type = SnmpAdminString
_CfprApExtpolRegistryName_Object = MibTableColumn
cfprApExtpolRegistryName = _CfprApExtpolRegistryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 25),
    _CfprApExtpolRegistryName_Type()
)
cfprApExtpolRegistryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryName.setStatus("current")
_CfprApExtpolRegistryOperState_Type = CfprApExtpolConnectorOperState
_CfprApExtpolRegistryOperState_Object = MibTableColumn
cfprApExtpolRegistryOperState = _CfprApExtpolRegistryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 26),
    _CfprApExtpolRegistryOperState_Type()
)
cfprApExtpolRegistryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryOperState.setStatus("current")
_CfprApExtpolRegistryType_Type = CfprApExtpolConnType
_CfprApExtpolRegistryType_Object = MibTableColumn
cfprApExtpolRegistryType = _CfprApExtpolRegistryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 27),
    _CfprApExtpolRegistryType_Type()
)
cfprApExtpolRegistryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryType.setStatus("current")
_CfprApExtpolRegistryVersion_Type = SnmpAdminString
_CfprApExtpolRegistryVersion_Object = MibTableColumn
cfprApExtpolRegistryVersion = _CfprApExtpolRegistryVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 14, 1, 28),
    _CfprApExtpolRegistryVersion_Type()
)
cfprApExtpolRegistryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryVersion.setStatus("current")
_CfprApExtpolRegistryFsmTable_Object = MibTable
cfprApExtpolRegistryFsmTable = _CfprApExtpolRegistryFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15)
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTable.setStatus("current")
_CfprApExtpolRegistryFsmEntry_Object = MibTableRow
cfprApExtpolRegistryFsmEntry = _CfprApExtpolRegistryFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1)
)
cfprApExtpolRegistryFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolRegistryFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmEntry.setStatus("current")
_CfprApExtpolRegistryFsmInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolRegistryFsmInstanceId_Object = MibTableColumn
cfprApExtpolRegistryFsmInstanceId = _CfprApExtpolRegistryFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 1),
    _CfprApExtpolRegistryFsmInstanceId_Type()
)
cfprApExtpolRegistryFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmInstanceId.setStatus("current")
_CfprApExtpolRegistryFsmDn_Type = CfprApManagedObjectDn
_CfprApExtpolRegistryFsmDn_Object = MibTableColumn
cfprApExtpolRegistryFsmDn = _CfprApExtpolRegistryFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 2),
    _CfprApExtpolRegistryFsmDn_Type()
)
cfprApExtpolRegistryFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmDn.setStatus("current")
_CfprApExtpolRegistryFsmRn_Type = SnmpAdminString
_CfprApExtpolRegistryFsmRn_Object = MibTableColumn
cfprApExtpolRegistryFsmRn = _CfprApExtpolRegistryFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 3),
    _CfprApExtpolRegistryFsmRn_Type()
)
cfprApExtpolRegistryFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRn.setStatus("current")
_CfprApExtpolRegistryFsmCompletionTime_Type = DateAndTime
_CfprApExtpolRegistryFsmCompletionTime_Object = MibTableColumn
cfprApExtpolRegistryFsmCompletionTime = _CfprApExtpolRegistryFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 4),
    _CfprApExtpolRegistryFsmCompletionTime_Type()
)
cfprApExtpolRegistryFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmCompletionTime.setStatus("current")
_CfprApExtpolRegistryFsmCurrentFsm_Type = CfprApExtpolRegistryFsmCurrentFsm
_CfprApExtpolRegistryFsmCurrentFsm_Object = MibTableColumn
cfprApExtpolRegistryFsmCurrentFsm = _CfprApExtpolRegistryFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 5),
    _CfprApExtpolRegistryFsmCurrentFsm_Type()
)
cfprApExtpolRegistryFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmCurrentFsm.setStatus("current")
_CfprApExtpolRegistryFsmDescrData_Type = SnmpAdminString
_CfprApExtpolRegistryFsmDescrData_Object = MibTableColumn
cfprApExtpolRegistryFsmDescrData = _CfprApExtpolRegistryFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 6),
    _CfprApExtpolRegistryFsmDescrData_Type()
)
cfprApExtpolRegistryFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmDescrData.setStatus("current")
_CfprApExtpolRegistryFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApExtpolRegistryFsmFsmStatus_Object = MibTableColumn
cfprApExtpolRegistryFsmFsmStatus = _CfprApExtpolRegistryFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 7),
    _CfprApExtpolRegistryFsmFsmStatus_Type()
)
cfprApExtpolRegistryFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmFsmStatus.setStatus("current")
_CfprApExtpolRegistryFsmProgress_Type = Gauge32
_CfprApExtpolRegistryFsmProgress_Object = MibTableColumn
cfprApExtpolRegistryFsmProgress = _CfprApExtpolRegistryFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 8),
    _CfprApExtpolRegistryFsmProgress_Type()
)
cfprApExtpolRegistryFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmProgress.setStatus("current")
_CfprApExtpolRegistryFsmRmtErrCode_Type = Gauge32
_CfprApExtpolRegistryFsmRmtErrCode_Object = MibTableColumn
cfprApExtpolRegistryFsmRmtErrCode = _CfprApExtpolRegistryFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 9),
    _CfprApExtpolRegistryFsmRmtErrCode_Type()
)
cfprApExtpolRegistryFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRmtErrCode.setStatus("current")
_CfprApExtpolRegistryFsmRmtErrDescr_Type = SnmpAdminString
_CfprApExtpolRegistryFsmRmtErrDescr_Object = MibTableColumn
cfprApExtpolRegistryFsmRmtErrDescr = _CfprApExtpolRegistryFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 10),
    _CfprApExtpolRegistryFsmRmtErrDescr_Type()
)
cfprApExtpolRegistryFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRmtErrDescr.setStatus("current")
_CfprApExtpolRegistryFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApExtpolRegistryFsmRmtRslt_Object = MibTableColumn
cfprApExtpolRegistryFsmRmtRslt = _CfprApExtpolRegistryFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 15, 1, 11),
    _CfprApExtpolRegistryFsmRmtRslt_Type()
)
cfprApExtpolRegistryFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmRmtRslt.setStatus("current")
_CfprApExtpolRegistryFsmStageTable_Object = MibTable
cfprApExtpolRegistryFsmStageTable = _CfprApExtpolRegistryFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16)
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageTable.setStatus("current")
_CfprApExtpolRegistryFsmStageEntry_Object = MibTableRow
cfprApExtpolRegistryFsmStageEntry = _CfprApExtpolRegistryFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1)
)
cfprApExtpolRegistryFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolRegistryFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageEntry.setStatus("current")
_CfprApExtpolRegistryFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolRegistryFsmStageInstanceId_Object = MibTableColumn
cfprApExtpolRegistryFsmStageInstanceId = _CfprApExtpolRegistryFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 1),
    _CfprApExtpolRegistryFsmStageInstanceId_Type()
)
cfprApExtpolRegistryFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageInstanceId.setStatus("current")
_CfprApExtpolRegistryFsmStageDn_Type = CfprApManagedObjectDn
_CfprApExtpolRegistryFsmStageDn_Object = MibTableColumn
cfprApExtpolRegistryFsmStageDn = _CfprApExtpolRegistryFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 2),
    _CfprApExtpolRegistryFsmStageDn_Type()
)
cfprApExtpolRegistryFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageDn.setStatus("current")
_CfprApExtpolRegistryFsmStageRn_Type = SnmpAdminString
_CfprApExtpolRegistryFsmStageRn_Object = MibTableColumn
cfprApExtpolRegistryFsmStageRn = _CfprApExtpolRegistryFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 3),
    _CfprApExtpolRegistryFsmStageRn_Type()
)
cfprApExtpolRegistryFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageRn.setStatus("current")
_CfprApExtpolRegistryFsmStageDescrData_Type = SnmpAdminString
_CfprApExtpolRegistryFsmStageDescrData_Object = MibTableColumn
cfprApExtpolRegistryFsmStageDescrData = _CfprApExtpolRegistryFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 4),
    _CfprApExtpolRegistryFsmStageDescrData_Type()
)
cfprApExtpolRegistryFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageDescrData.setStatus("current")
_CfprApExtpolRegistryFsmStageLastUpdateTime_Type = DateAndTime
_CfprApExtpolRegistryFsmStageLastUpdateTime_Object = MibTableColumn
cfprApExtpolRegistryFsmStageLastUpdateTime = _CfprApExtpolRegistryFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 5),
    _CfprApExtpolRegistryFsmStageLastUpdateTime_Type()
)
cfprApExtpolRegistryFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageLastUpdateTime.setStatus("current")
_CfprApExtpolRegistryFsmStageName_Type = CfprApExtpolRegistryFsmStageName
_CfprApExtpolRegistryFsmStageName_Object = MibTableColumn
cfprApExtpolRegistryFsmStageName = _CfprApExtpolRegistryFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 6),
    _CfprApExtpolRegistryFsmStageName_Type()
)
cfprApExtpolRegistryFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageName.setStatus("current")
_CfprApExtpolRegistryFsmStageOrder_Type = Gauge32
_CfprApExtpolRegistryFsmStageOrder_Object = MibTableColumn
cfprApExtpolRegistryFsmStageOrder = _CfprApExtpolRegistryFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 7),
    _CfprApExtpolRegistryFsmStageOrder_Type()
)
cfprApExtpolRegistryFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageOrder.setStatus("current")
_CfprApExtpolRegistryFsmStageRetry_Type = Gauge32
_CfprApExtpolRegistryFsmStageRetry_Object = MibTableColumn
cfprApExtpolRegistryFsmStageRetry = _CfprApExtpolRegistryFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 8),
    _CfprApExtpolRegistryFsmStageRetry_Type()
)
cfprApExtpolRegistryFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageRetry.setStatus("current")
_CfprApExtpolRegistryFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApExtpolRegistryFsmStageStageStatus_Object = MibTableColumn
cfprApExtpolRegistryFsmStageStageStatus = _CfprApExtpolRegistryFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 16, 1, 9),
    _CfprApExtpolRegistryFsmStageStageStatus_Type()
)
cfprApExtpolRegistryFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmStageStageStatus.setStatus("current")
_CfprApExtpolRegistryFsmTaskTable_Object = MibTable
cfprApExtpolRegistryFsmTaskTable = _CfprApExtpolRegistryFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17)
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskTable.setStatus("current")
_CfprApExtpolRegistryFsmTaskEntry_Object = MibTableRow
cfprApExtpolRegistryFsmTaskEntry = _CfprApExtpolRegistryFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1)
)
cfprApExtpolRegistryFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolRegistryFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskEntry.setStatus("current")
_CfprApExtpolRegistryFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolRegistryFsmTaskInstanceId_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskInstanceId = _CfprApExtpolRegistryFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 1),
    _CfprApExtpolRegistryFsmTaskInstanceId_Type()
)
cfprApExtpolRegistryFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskInstanceId.setStatus("current")
_CfprApExtpolRegistryFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApExtpolRegistryFsmTaskDn_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskDn = _CfprApExtpolRegistryFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 2),
    _CfprApExtpolRegistryFsmTaskDn_Type()
)
cfprApExtpolRegistryFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskDn.setStatus("current")
_CfprApExtpolRegistryFsmTaskRn_Type = SnmpAdminString
_CfprApExtpolRegistryFsmTaskRn_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskRn = _CfprApExtpolRegistryFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 3),
    _CfprApExtpolRegistryFsmTaskRn_Type()
)
cfprApExtpolRegistryFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskRn.setStatus("current")
_CfprApExtpolRegistryFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApExtpolRegistryFsmTaskCompletion_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskCompletion = _CfprApExtpolRegistryFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 4),
    _CfprApExtpolRegistryFsmTaskCompletion_Type()
)
cfprApExtpolRegistryFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskCompletion.setStatus("current")
_CfprApExtpolRegistryFsmTaskFlags_Type = CfprApFsmFlags
_CfprApExtpolRegistryFsmTaskFlags_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskFlags = _CfprApExtpolRegistryFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 5),
    _CfprApExtpolRegistryFsmTaskFlags_Type()
)
cfprApExtpolRegistryFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskFlags.setStatus("current")
_CfprApExtpolRegistryFsmTaskItem_Type = CfprApExtpolRegistryFsmTaskItem
_CfprApExtpolRegistryFsmTaskItem_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskItem = _CfprApExtpolRegistryFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 6),
    _CfprApExtpolRegistryFsmTaskItem_Type()
)
cfprApExtpolRegistryFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskItem.setStatus("current")
_CfprApExtpolRegistryFsmTaskSeqId_Type = Gauge32
_CfprApExtpolRegistryFsmTaskSeqId_Object = MibTableColumn
cfprApExtpolRegistryFsmTaskSeqId = _CfprApExtpolRegistryFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 17, 1, 7),
    _CfprApExtpolRegistryFsmTaskSeqId_Type()
)
cfprApExtpolRegistryFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolRegistryFsmTaskSeqId.setStatus("current")
_CfprApExtpolSystemContextTable_Object = MibTable
cfprApExtpolSystemContextTable = _CfprApExtpolSystemContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18)
)
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextTable.setStatus("current")
_CfprApExtpolSystemContextEntry_Object = MibTableRow
cfprApExtpolSystemContextEntry = _CfprApExtpolSystemContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1)
)
cfprApExtpolSystemContextEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTPOL-MIB", "cfprApExtpolSystemContextInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextEntry.setStatus("current")
_CfprApExtpolSystemContextInstanceId_Type = CfprApManagedObjectId
_CfprApExtpolSystemContextInstanceId_Object = MibTableColumn
cfprApExtpolSystemContextInstanceId = _CfprApExtpolSystemContextInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 1),
    _CfprApExtpolSystemContextInstanceId_Type()
)
cfprApExtpolSystemContextInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextInstanceId.setStatus("current")
_CfprApExtpolSystemContextDn_Type = CfprApManagedObjectDn
_CfprApExtpolSystemContextDn_Object = MibTableColumn
cfprApExtpolSystemContextDn = _CfprApExtpolSystemContextDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 2),
    _CfprApExtpolSystemContextDn_Type()
)
cfprApExtpolSystemContextDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextDn.setStatus("current")
_CfprApExtpolSystemContextRn_Type = SnmpAdminString
_CfprApExtpolSystemContextRn_Object = MibTableColumn
cfprApExtpolSystemContextRn = _CfprApExtpolSystemContextRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 3),
    _CfprApExtpolSystemContextRn_Type()
)
cfprApExtpolSystemContextRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextRn.setStatus("current")
_CfprApExtpolSystemContextCapability_Type = CfprApExtpolAppCapability
_CfprApExtpolSystemContextCapability_Object = MibTableColumn
cfprApExtpolSystemContextCapability = _CfprApExtpolSystemContextCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 4),
    _CfprApExtpolSystemContextCapability_Type()
)
cfprApExtpolSystemContextCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextCapability.setStatus("current")
_CfprApExtpolSystemContextDescr_Type = SnmpAdminString
_CfprApExtpolSystemContextDescr_Object = MibTableColumn
cfprApExtpolSystemContextDescr = _CfprApExtpolSystemContextDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 5),
    _CfprApExtpolSystemContextDescr_Type()
)
cfprApExtpolSystemContextDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextDescr.setStatus("current")
_CfprApExtpolSystemContextGuid_Type = SnmpAdminString
_CfprApExtpolSystemContextGuid_Object = MibTableColumn
cfprApExtpolSystemContextGuid = _CfprApExtpolSystemContextGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 6),
    _CfprApExtpolSystemContextGuid_Type()
)
cfprApExtpolSystemContextGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextGuid.setStatus("current")
_CfprApExtpolSystemContextId_Type = Gauge32
_CfprApExtpolSystemContextId_Object = MibTableColumn
cfprApExtpolSystemContextId = _CfprApExtpolSystemContextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 7),
    _CfprApExtpolSystemContextId_Type()
)
cfprApExtpolSystemContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextId.setStatus("current")
_CfprApExtpolSystemContextInterest_Type = CfprApExtpolAppCapability
_CfprApExtpolSystemContextInterest_Object = MibTableColumn
cfprApExtpolSystemContextInterest = _CfprApExtpolSystemContextInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 8),
    _CfprApExtpolSystemContextInterest_Type()
)
cfprApExtpolSystemContextInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextInterest.setStatus("current")
_CfprApExtpolSystemContextIp_Type = InetAddressIPv4
_CfprApExtpolSystemContextIp_Object = MibTableColumn
cfprApExtpolSystemContextIp = _CfprApExtpolSystemContextIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 9),
    _CfprApExtpolSystemContextIp_Type()
)
cfprApExtpolSystemContextIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextIp.setStatus("current")
_CfprApExtpolSystemContextIpv6addr_Type = InetAddressIPv6
_CfprApExtpolSystemContextIpv6addr_Object = MibTableColumn
cfprApExtpolSystemContextIpv6addr = _CfprApExtpolSystemContextIpv6addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 10),
    _CfprApExtpolSystemContextIpv6addr_Type()
)
cfprApExtpolSystemContextIpv6addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextIpv6addr.setStatus("current")
_CfprApExtpolSystemContextModel_Type = SnmpAdminString
_CfprApExtpolSystemContextModel_Object = MibTableColumn
cfprApExtpolSystemContextModel = _CfprApExtpolSystemContextModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 11),
    _CfprApExtpolSystemContextModel_Type()
)
cfprApExtpolSystemContextModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextModel.setStatus("current")
_CfprApExtpolSystemContextName_Type = SnmpAdminString
_CfprApExtpolSystemContextName_Object = MibTableColumn
cfprApExtpolSystemContextName = _CfprApExtpolSystemContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 12),
    _CfprApExtpolSystemContextName_Type()
)
cfprApExtpolSystemContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextName.setStatus("current")
_CfprApExtpolSystemContextOwner_Type = SnmpAdminString
_CfprApExtpolSystemContextOwner_Object = MibTableColumn
cfprApExtpolSystemContextOwner = _CfprApExtpolSystemContextOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 13),
    _CfprApExtpolSystemContextOwner_Type()
)
cfprApExtpolSystemContextOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextOwner.setStatus("current")
_CfprApExtpolSystemContextSite_Type = SnmpAdminString
_CfprApExtpolSystemContextSite_Object = MibTableColumn
cfprApExtpolSystemContextSite = _CfprApExtpolSystemContextSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 14),
    _CfprApExtpolSystemContextSite_Type()
)
cfprApExtpolSystemContextSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextSite.setStatus("current")
_CfprApExtpolSystemContextType_Type = CfprApExtpolConnType
_CfprApExtpolSystemContextType_Object = MibTableColumn
cfprApExtpolSystemContextType = _CfprApExtpolSystemContextType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 15),
    _CfprApExtpolSystemContextType_Type()
)
cfprApExtpolSystemContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextType.setStatus("current")
_CfprApExtpolSystemContextVersion_Type = SnmpAdminString
_CfprApExtpolSystemContextVersion_Object = MibTableColumn
cfprApExtpolSystemContextVersion = _CfprApExtpolSystemContextVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 24, 18, 1, 16),
    _CfprApExtpolSystemContextVersion_Type()
)
cfprApExtpolSystemContextVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtpolSystemContextVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-EXTPOL-MIB",
    **{"cfprApExtpolObjects": cfprApExtpolObjects,
       "cfprApExtpolClientTable": cfprApExtpolClientTable,
       "cfprApExtpolClientEntry": cfprApExtpolClientEntry,
       "cfprApExtpolClientInstanceId": cfprApExtpolClientInstanceId,
       "cfprApExtpolClientDn": cfprApExtpolClientDn,
       "cfprApExtpolClientRn": cfprApExtpolClientRn,
       "cfprApExtpolClientCapability": cfprApExtpolClientCapability,
       "cfprApExtpolClientConnProtocol": cfprApExtpolClientConnProtocol,
       "cfprApExtpolClientDescr": cfprApExtpolClientDescr,
       "cfprApExtpolClientGracePeriodUsed": cfprApExtpolClientGracePeriodUsed,
       "cfprApExtpolClientGuid": cfprApExtpolClientGuid,
       "cfprApExtpolClientHost": cfprApExtpolClientHost,
       "cfprApExtpolClientId": cfprApExtpolClientId,
       "cfprApExtpolClientInterest": cfprApExtpolClientInterest,
       "cfprApExtpolClientIp": cfprApExtpolClientIp,
       "cfprApExtpolClientIpv6": cfprApExtpolClientIpv6,
       "cfprApExtpolClientLastPollTs": cfprApExtpolClientLastPollTs,
       "cfprApExtpolClientLicState": cfprApExtpolClientLicState,
       "cfprApExtpolClientName": cfprApExtpolClientName,
       "cfprApExtpolClientOperState": cfprApExtpolClientOperState,
       "cfprApExtpolClientOwner": cfprApExtpolClientOwner,
       "cfprApExtpolClientSite": cfprApExtpolClientSite,
       "cfprApExtpolClientSuspendState": cfprApExtpolClientSuspendState,
       "cfprApExtpolClientType": cfprApExtpolClientType,
       "cfprApExtpolClientVersion": cfprApExtpolClientVersion,
       "cfprApExtpolClientContTable": cfprApExtpolClientContTable,
       "cfprApExtpolClientContEntry": cfprApExtpolClientContEntry,
       "cfprApExtpolClientContInstanceId": cfprApExtpolClientContInstanceId,
       "cfprApExtpolClientContDn": cfprApExtpolClientContDn,
       "cfprApExtpolClientContRn": cfprApExtpolClientContRn,
       "cfprApExtpolClientContGenNum": cfprApExtpolClientContGenNum,
       "cfprApExtpolControllerTable": cfprApExtpolControllerTable,
       "cfprApExtpolControllerEntry": cfprApExtpolControllerEntry,
       "cfprApExtpolControllerInstanceId": cfprApExtpolControllerInstanceId,
       "cfprApExtpolControllerDn": cfprApExtpolControllerDn,
       "cfprApExtpolControllerRn": cfprApExtpolControllerRn,
       "cfprApExtpolControllerCapability": cfprApExtpolControllerCapability,
       "cfprApExtpolControllerConnProtocol": cfprApExtpolControllerConnProtocol,
       "cfprApExtpolControllerHost": cfprApExtpolControllerHost,
       "cfprApExtpolControllerId": cfprApExtpolControllerId,
       "cfprApExtpolControllerInterest": cfprApExtpolControllerInterest,
       "cfprApExtpolControllerIp": cfprApExtpolControllerIp,
       "cfprApExtpolControllerIpv6": cfprApExtpolControllerIpv6,
       "cfprApExtpolControllerLastPollTs": cfprApExtpolControllerLastPollTs,
       "cfprApExtpolControllerName": cfprApExtpolControllerName,
       "cfprApExtpolControllerOperState": cfprApExtpolControllerOperState,
       "cfprApExtpolControllerType": cfprApExtpolControllerType,
       "cfprApExtpolControllerVersion": cfprApExtpolControllerVersion,
       "cfprApExtpolControllerContTable": cfprApExtpolControllerContTable,
       "cfprApExtpolControllerContEntry": cfprApExtpolControllerContEntry,
       "cfprApExtpolControllerContInstanceId": cfprApExtpolControllerContInstanceId,
       "cfprApExtpolControllerContDn": cfprApExtpolControllerContDn,
       "cfprApExtpolControllerContRn": cfprApExtpolControllerContRn,
       "cfprApExtpolControllerContGenNum": cfprApExtpolControllerContGenNum,
       "cfprApExtpolEpTable": cfprApExtpolEpTable,
       "cfprApExtpolEpEntry": cfprApExtpolEpEntry,
       "cfprApExtpolEpInstanceId": cfprApExtpolEpInstanceId,
       "cfprApExtpolEpDn": cfprApExtpolEpDn,
       "cfprApExtpolEpRn": cfprApExtpolEpRn,
       "cfprApExtpolEpFsmDescr": cfprApExtpolEpFsmDescr,
       "cfprApExtpolEpFsmPrev": cfprApExtpolEpFsmPrev,
       "cfprApExtpolEpFsmProgr": cfprApExtpolEpFsmProgr,
       "cfprApExtpolEpFsmRmtInvErrCode": cfprApExtpolEpFsmRmtInvErrCode,
       "cfprApExtpolEpFsmRmtInvErrDescr": cfprApExtpolEpFsmRmtInvErrDescr,
       "cfprApExtpolEpFsmRmtInvRslt": cfprApExtpolEpFsmRmtInvRslt,
       "cfprApExtpolEpFsmStageDescr": cfprApExtpolEpFsmStageDescr,
       "cfprApExtpolEpFsmStamp": cfprApExtpolEpFsmStamp,
       "cfprApExtpolEpFsmStatus": cfprApExtpolEpFsmStatus,
       "cfprApExtpolEpFsmTry": cfprApExtpolEpFsmTry,
       "cfprApExtpolEpFsmTable": cfprApExtpolEpFsmTable,
       "cfprApExtpolEpFsmEntry": cfprApExtpolEpFsmEntry,
       "cfprApExtpolEpFsmInstanceId": cfprApExtpolEpFsmInstanceId,
       "cfprApExtpolEpFsmDn": cfprApExtpolEpFsmDn,
       "cfprApExtpolEpFsmRn": cfprApExtpolEpFsmRn,
       "cfprApExtpolEpFsmCompletionTime": cfprApExtpolEpFsmCompletionTime,
       "cfprApExtpolEpFsmCurrentFsm": cfprApExtpolEpFsmCurrentFsm,
       "cfprApExtpolEpFsmDescrData": cfprApExtpolEpFsmDescrData,
       "cfprApExtpolEpFsmFsmStatus": cfprApExtpolEpFsmFsmStatus,
       "cfprApExtpolEpFsmProgress": cfprApExtpolEpFsmProgress,
       "cfprApExtpolEpFsmRmtErrCode": cfprApExtpolEpFsmRmtErrCode,
       "cfprApExtpolEpFsmRmtErrDescr": cfprApExtpolEpFsmRmtErrDescr,
       "cfprApExtpolEpFsmRmtRslt": cfprApExtpolEpFsmRmtRslt,
       "cfprApExtpolEpFsmStageTable": cfprApExtpolEpFsmStageTable,
       "cfprApExtpolEpFsmStageEntry": cfprApExtpolEpFsmStageEntry,
       "cfprApExtpolEpFsmStageInstanceId": cfprApExtpolEpFsmStageInstanceId,
       "cfprApExtpolEpFsmStageDn": cfprApExtpolEpFsmStageDn,
       "cfprApExtpolEpFsmStageRn": cfprApExtpolEpFsmStageRn,
       "cfprApExtpolEpFsmStageDescrData": cfprApExtpolEpFsmStageDescrData,
       "cfprApExtpolEpFsmStageLastUpdateTime": cfprApExtpolEpFsmStageLastUpdateTime,
       "cfprApExtpolEpFsmStageName": cfprApExtpolEpFsmStageName,
       "cfprApExtpolEpFsmStageOrder": cfprApExtpolEpFsmStageOrder,
       "cfprApExtpolEpFsmStageRetry": cfprApExtpolEpFsmStageRetry,
       "cfprApExtpolEpFsmStageStageStatus": cfprApExtpolEpFsmStageStageStatus,
       "cfprApExtpolEpFsmTaskTable": cfprApExtpolEpFsmTaskTable,
       "cfprApExtpolEpFsmTaskEntry": cfprApExtpolEpFsmTaskEntry,
       "cfprApExtpolEpFsmTaskInstanceId": cfprApExtpolEpFsmTaskInstanceId,
       "cfprApExtpolEpFsmTaskDn": cfprApExtpolEpFsmTaskDn,
       "cfprApExtpolEpFsmTaskRn": cfprApExtpolEpFsmTaskRn,
       "cfprApExtpolEpFsmTaskCompletion": cfprApExtpolEpFsmTaskCompletion,
       "cfprApExtpolEpFsmTaskFlags": cfprApExtpolEpFsmTaskFlags,
       "cfprApExtpolEpFsmTaskItem": cfprApExtpolEpFsmTaskItem,
       "cfprApExtpolEpFsmTaskSeqId": cfprApExtpolEpFsmTaskSeqId,
       "cfprApExtpolProviderTable": cfprApExtpolProviderTable,
       "cfprApExtpolProviderEntry": cfprApExtpolProviderEntry,
       "cfprApExtpolProviderInstanceId": cfprApExtpolProviderInstanceId,
       "cfprApExtpolProviderDn": cfprApExtpolProviderDn,
       "cfprApExtpolProviderRn": cfprApExtpolProviderRn,
       "cfprApExtpolProviderCapability": cfprApExtpolProviderCapability,
       "cfprApExtpolProviderConnProtocol": cfprApExtpolProviderConnProtocol,
       "cfprApExtpolProviderFsmDescr": cfprApExtpolProviderFsmDescr,
       "cfprApExtpolProviderFsmPrev": cfprApExtpolProviderFsmPrev,
       "cfprApExtpolProviderFsmProgr": cfprApExtpolProviderFsmProgr,
       "cfprApExtpolProviderFsmRmtInvErrCode": cfprApExtpolProviderFsmRmtInvErrCode,
       "cfprApExtpolProviderFsmRmtInvErrDescr": cfprApExtpolProviderFsmRmtInvErrDescr,
       "cfprApExtpolProviderFsmRmtInvRslt": cfprApExtpolProviderFsmRmtInvRslt,
       "cfprApExtpolProviderFsmStageDescr": cfprApExtpolProviderFsmStageDescr,
       "cfprApExtpolProviderFsmStamp": cfprApExtpolProviderFsmStamp,
       "cfprApExtpolProviderFsmStatus": cfprApExtpolProviderFsmStatus,
       "cfprApExtpolProviderFsmTry": cfprApExtpolProviderFsmTry,
       "cfprApExtpolProviderHost": cfprApExtpolProviderHost,
       "cfprApExtpolProviderId": cfprApExtpolProviderId,
       "cfprApExtpolProviderInterest": cfprApExtpolProviderInterest,
       "cfprApExtpolProviderIp": cfprApExtpolProviderIp,
       "cfprApExtpolProviderIpv6": cfprApExtpolProviderIpv6,
       "cfprApExtpolProviderLastPollTs": cfprApExtpolProviderLastPollTs,
       "cfprApExtpolProviderName": cfprApExtpolProviderName,
       "cfprApExtpolProviderOperState": cfprApExtpolProviderOperState,
       "cfprApExtpolProviderType": cfprApExtpolProviderType,
       "cfprApExtpolProviderVersion": cfprApExtpolProviderVersion,
       "cfprApExtpolProviderContTable": cfprApExtpolProviderContTable,
       "cfprApExtpolProviderContEntry": cfprApExtpolProviderContEntry,
       "cfprApExtpolProviderContInstanceId": cfprApExtpolProviderContInstanceId,
       "cfprApExtpolProviderContDn": cfprApExtpolProviderContDn,
       "cfprApExtpolProviderContRn": cfprApExtpolProviderContRn,
       "cfprApExtpolProviderContGenNum": cfprApExtpolProviderContGenNum,
       "cfprApExtpolProviderFsmTable": cfprApExtpolProviderFsmTable,
       "cfprApExtpolProviderFsmEntry": cfprApExtpolProviderFsmEntry,
       "cfprApExtpolProviderFsmInstanceId": cfprApExtpolProviderFsmInstanceId,
       "cfprApExtpolProviderFsmDn": cfprApExtpolProviderFsmDn,
       "cfprApExtpolProviderFsmRn": cfprApExtpolProviderFsmRn,
       "cfprApExtpolProviderFsmCompletionTime": cfprApExtpolProviderFsmCompletionTime,
       "cfprApExtpolProviderFsmCurrentFsm": cfprApExtpolProviderFsmCurrentFsm,
       "cfprApExtpolProviderFsmDescrData": cfprApExtpolProviderFsmDescrData,
       "cfprApExtpolProviderFsmFsmStatus": cfprApExtpolProviderFsmFsmStatus,
       "cfprApExtpolProviderFsmProgress": cfprApExtpolProviderFsmProgress,
       "cfprApExtpolProviderFsmRmtErrCode": cfprApExtpolProviderFsmRmtErrCode,
       "cfprApExtpolProviderFsmRmtErrDescr": cfprApExtpolProviderFsmRmtErrDescr,
       "cfprApExtpolProviderFsmRmtRslt": cfprApExtpolProviderFsmRmtRslt,
       "cfprApExtpolProviderFsmStageTable": cfprApExtpolProviderFsmStageTable,
       "cfprApExtpolProviderFsmStageEntry": cfprApExtpolProviderFsmStageEntry,
       "cfprApExtpolProviderFsmStageInstanceId": cfprApExtpolProviderFsmStageInstanceId,
       "cfprApExtpolProviderFsmStageDn": cfprApExtpolProviderFsmStageDn,
       "cfprApExtpolProviderFsmStageRn": cfprApExtpolProviderFsmStageRn,
       "cfprApExtpolProviderFsmStageDescrData": cfprApExtpolProviderFsmStageDescrData,
       "cfprApExtpolProviderFsmStageLastUpdateTime": cfprApExtpolProviderFsmStageLastUpdateTime,
       "cfprApExtpolProviderFsmStageName": cfprApExtpolProviderFsmStageName,
       "cfprApExtpolProviderFsmStageOrder": cfprApExtpolProviderFsmStageOrder,
       "cfprApExtpolProviderFsmStageRetry": cfprApExtpolProviderFsmStageRetry,
       "cfprApExtpolProviderFsmStageStageStatus": cfprApExtpolProviderFsmStageStageStatus,
       "cfprApExtpolProviderFsmTaskTable": cfprApExtpolProviderFsmTaskTable,
       "cfprApExtpolProviderFsmTaskEntry": cfprApExtpolProviderFsmTaskEntry,
       "cfprApExtpolProviderFsmTaskInstanceId": cfprApExtpolProviderFsmTaskInstanceId,
       "cfprApExtpolProviderFsmTaskDn": cfprApExtpolProviderFsmTaskDn,
       "cfprApExtpolProviderFsmTaskRn": cfprApExtpolProviderFsmTaskRn,
       "cfprApExtpolProviderFsmTaskCompletion": cfprApExtpolProviderFsmTaskCompletion,
       "cfprApExtpolProviderFsmTaskFlags": cfprApExtpolProviderFsmTaskFlags,
       "cfprApExtpolProviderFsmTaskItem": cfprApExtpolProviderFsmTaskItem,
       "cfprApExtpolProviderFsmTaskSeqId": cfprApExtpolProviderFsmTaskSeqId,
       "cfprApExtpolRegistryTable": cfprApExtpolRegistryTable,
       "cfprApExtpolRegistryEntry": cfprApExtpolRegistryEntry,
       "cfprApExtpolRegistryInstanceId": cfprApExtpolRegistryInstanceId,
       "cfprApExtpolRegistryDn": cfprApExtpolRegistryDn,
       "cfprApExtpolRegistryRn": cfprApExtpolRegistryRn,
       "cfprApExtpolRegistryCapability": cfprApExtpolRegistryCapability,
       "cfprApExtpolRegistryConnProtocol": cfprApExtpolRegistryConnProtocol,
       "cfprApExtpolRegistryFsmDescr": cfprApExtpolRegistryFsmDescr,
       "cfprApExtpolRegistryFsmPrev": cfprApExtpolRegistryFsmPrev,
       "cfprApExtpolRegistryFsmProgr": cfprApExtpolRegistryFsmProgr,
       "cfprApExtpolRegistryFsmRmtInvErrCode": cfprApExtpolRegistryFsmRmtInvErrCode,
       "cfprApExtpolRegistryFsmRmtInvErrDescr": cfprApExtpolRegistryFsmRmtInvErrDescr,
       "cfprApExtpolRegistryFsmRmtInvRslt": cfprApExtpolRegistryFsmRmtInvRslt,
       "cfprApExtpolRegistryFsmStageDescr": cfprApExtpolRegistryFsmStageDescr,
       "cfprApExtpolRegistryFsmStamp": cfprApExtpolRegistryFsmStamp,
       "cfprApExtpolRegistryFsmStatus": cfprApExtpolRegistryFsmStatus,
       "cfprApExtpolRegistryFsmTry": cfprApExtpolRegistryFsmTry,
       "cfprApExtpolRegistryGenNum": cfprApExtpolRegistryGenNum,
       "cfprApExtpolRegistryGuid": cfprApExtpolRegistryGuid,
       "cfprApExtpolRegistryHost": cfprApExtpolRegistryHost,
       "cfprApExtpolRegistryId": cfprApExtpolRegistryId,
       "cfprApExtpolRegistryIdCount": cfprApExtpolRegistryIdCount,
       "cfprApExtpolRegistryInterest": cfprApExtpolRegistryInterest,
       "cfprApExtpolRegistryIp": cfprApExtpolRegistryIp,
       "cfprApExtpolRegistryIpv6": cfprApExtpolRegistryIpv6,
       "cfprApExtpolRegistryLastPollTs": cfprApExtpolRegistryLastPollTs,
       "cfprApExtpolRegistryName": cfprApExtpolRegistryName,
       "cfprApExtpolRegistryOperState": cfprApExtpolRegistryOperState,
       "cfprApExtpolRegistryType": cfprApExtpolRegistryType,
       "cfprApExtpolRegistryVersion": cfprApExtpolRegistryVersion,
       "cfprApExtpolRegistryFsmTable": cfprApExtpolRegistryFsmTable,
       "cfprApExtpolRegistryFsmEntry": cfprApExtpolRegistryFsmEntry,
       "cfprApExtpolRegistryFsmInstanceId": cfprApExtpolRegistryFsmInstanceId,
       "cfprApExtpolRegistryFsmDn": cfprApExtpolRegistryFsmDn,
       "cfprApExtpolRegistryFsmRn": cfprApExtpolRegistryFsmRn,
       "cfprApExtpolRegistryFsmCompletionTime": cfprApExtpolRegistryFsmCompletionTime,
       "cfprApExtpolRegistryFsmCurrentFsm": cfprApExtpolRegistryFsmCurrentFsm,
       "cfprApExtpolRegistryFsmDescrData": cfprApExtpolRegistryFsmDescrData,
       "cfprApExtpolRegistryFsmFsmStatus": cfprApExtpolRegistryFsmFsmStatus,
       "cfprApExtpolRegistryFsmProgress": cfprApExtpolRegistryFsmProgress,
       "cfprApExtpolRegistryFsmRmtErrCode": cfprApExtpolRegistryFsmRmtErrCode,
       "cfprApExtpolRegistryFsmRmtErrDescr": cfprApExtpolRegistryFsmRmtErrDescr,
       "cfprApExtpolRegistryFsmRmtRslt": cfprApExtpolRegistryFsmRmtRslt,
       "cfprApExtpolRegistryFsmStageTable": cfprApExtpolRegistryFsmStageTable,
       "cfprApExtpolRegistryFsmStageEntry": cfprApExtpolRegistryFsmStageEntry,
       "cfprApExtpolRegistryFsmStageInstanceId": cfprApExtpolRegistryFsmStageInstanceId,
       "cfprApExtpolRegistryFsmStageDn": cfprApExtpolRegistryFsmStageDn,
       "cfprApExtpolRegistryFsmStageRn": cfprApExtpolRegistryFsmStageRn,
       "cfprApExtpolRegistryFsmStageDescrData": cfprApExtpolRegistryFsmStageDescrData,
       "cfprApExtpolRegistryFsmStageLastUpdateTime": cfprApExtpolRegistryFsmStageLastUpdateTime,
       "cfprApExtpolRegistryFsmStageName": cfprApExtpolRegistryFsmStageName,
       "cfprApExtpolRegistryFsmStageOrder": cfprApExtpolRegistryFsmStageOrder,
       "cfprApExtpolRegistryFsmStageRetry": cfprApExtpolRegistryFsmStageRetry,
       "cfprApExtpolRegistryFsmStageStageStatus": cfprApExtpolRegistryFsmStageStageStatus,
       "cfprApExtpolRegistryFsmTaskTable": cfprApExtpolRegistryFsmTaskTable,
       "cfprApExtpolRegistryFsmTaskEntry": cfprApExtpolRegistryFsmTaskEntry,
       "cfprApExtpolRegistryFsmTaskInstanceId": cfprApExtpolRegistryFsmTaskInstanceId,
       "cfprApExtpolRegistryFsmTaskDn": cfprApExtpolRegistryFsmTaskDn,
       "cfprApExtpolRegistryFsmTaskRn": cfprApExtpolRegistryFsmTaskRn,
       "cfprApExtpolRegistryFsmTaskCompletion": cfprApExtpolRegistryFsmTaskCompletion,
       "cfprApExtpolRegistryFsmTaskFlags": cfprApExtpolRegistryFsmTaskFlags,
       "cfprApExtpolRegistryFsmTaskItem": cfprApExtpolRegistryFsmTaskItem,
       "cfprApExtpolRegistryFsmTaskSeqId": cfprApExtpolRegistryFsmTaskSeqId,
       "cfprApExtpolSystemContextTable": cfprApExtpolSystemContextTable,
       "cfprApExtpolSystemContextEntry": cfprApExtpolSystemContextEntry,
       "cfprApExtpolSystemContextInstanceId": cfprApExtpolSystemContextInstanceId,
       "cfprApExtpolSystemContextDn": cfprApExtpolSystemContextDn,
       "cfprApExtpolSystemContextRn": cfprApExtpolSystemContextRn,
       "cfprApExtpolSystemContextCapability": cfprApExtpolSystemContextCapability,
       "cfprApExtpolSystemContextDescr": cfprApExtpolSystemContextDescr,
       "cfprApExtpolSystemContextGuid": cfprApExtpolSystemContextGuid,
       "cfprApExtpolSystemContextId": cfprApExtpolSystemContextId,
       "cfprApExtpolSystemContextInterest": cfprApExtpolSystemContextInterest,
       "cfprApExtpolSystemContextIp": cfprApExtpolSystemContextIp,
       "cfprApExtpolSystemContextIpv6addr": cfprApExtpolSystemContextIpv6addr,
       "cfprApExtpolSystemContextModel": cfprApExtpolSystemContextModel,
       "cfprApExtpolSystemContextName": cfprApExtpolSystemContextName,
       "cfprApExtpolSystemContextOwner": cfprApExtpolSystemContextOwner,
       "cfprApExtpolSystemContextSite": cfprApExtpolSystemContextSite,
       "cfprApExtpolSystemContextType": cfprApExtpolSystemContextType,
       "cfprApExtpolSystemContextVersion": cfprApExtpolSystemContextVersion}
)
