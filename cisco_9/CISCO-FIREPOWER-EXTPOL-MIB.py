# SNMP MIB module (CISCO-FIREPOWER-EXTPOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-EXTPOL-MIB.mib
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
 CfprExtpolAppCapability,
 CfprExtpolConnProtocol,
 CfprExtpolConnType,
 CfprExtpolConnectorOperState,
 CfprExtpolEpFsmCurrentFsm,
 CfprExtpolEpFsmStageName,
 CfprExtpolEpFsmTaskItem,
 CfprExtpolProviderFsmCurrentFsm,
 CfprExtpolProviderFsmStageName,
 CfprExtpolProviderFsmTaskItem,
 CfprExtpolRegistryFsmCurrentFsm,
 CfprExtpolRegistryFsmStageName,
 CfprExtpolRegistryFsmTaskItem,
 CfprExtpolState,
 CfprExtpolSuspendState,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprExtpolAppCapability",
    "CfprExtpolConnProtocol",
    "CfprExtpolConnType",
    "CfprExtpolConnectorOperState",
    "CfprExtpolEpFsmCurrentFsm",
    "CfprExtpolEpFsmStageName",
    "CfprExtpolEpFsmTaskItem",
    "CfprExtpolProviderFsmCurrentFsm",
    "CfprExtpolProviderFsmStageName",
    "CfprExtpolProviderFsmTaskItem",
    "CfprExtpolRegistryFsmCurrentFsm",
    "CfprExtpolRegistryFsmStageName",
    "CfprExtpolRegistryFsmTaskItem",
    "CfprExtpolState",
    "CfprExtpolSuspendState",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus")

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

cfprExtpolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprExtpolClientTable_Object = MibTable
cfprExtpolClientTable = _CfprExtpolClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1)
)
if mibBuilder.loadTexts:
    cfprExtpolClientTable.setStatus("current")
_CfprExtpolClientEntry_Object = MibTableRow
cfprExtpolClientEntry = _CfprExtpolClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1)
)
cfprExtpolClientEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolClientInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolClientEntry.setStatus("current")
_CfprExtpolClientInstanceId_Type = CfprManagedObjectId
_CfprExtpolClientInstanceId_Object = MibTableColumn
cfprExtpolClientInstanceId = _CfprExtpolClientInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 1),
    _CfprExtpolClientInstanceId_Type()
)
cfprExtpolClientInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolClientInstanceId.setStatus("current")
_CfprExtpolClientDn_Type = CfprManagedObjectDn
_CfprExtpolClientDn_Object = MibTableColumn
cfprExtpolClientDn = _CfprExtpolClientDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 2),
    _CfprExtpolClientDn_Type()
)
cfprExtpolClientDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientDn.setStatus("current")
_CfprExtpolClientRn_Type = SnmpAdminString
_CfprExtpolClientRn_Object = MibTableColumn
cfprExtpolClientRn = _CfprExtpolClientRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 3),
    _CfprExtpolClientRn_Type()
)
cfprExtpolClientRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientRn.setStatus("current")
_CfprExtpolClientCapability_Type = CfprExtpolAppCapability
_CfprExtpolClientCapability_Object = MibTableColumn
cfprExtpolClientCapability = _CfprExtpolClientCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 4),
    _CfprExtpolClientCapability_Type()
)
cfprExtpolClientCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientCapability.setStatus("current")
_CfprExtpolClientConnProtocol_Type = CfprExtpolConnProtocol
_CfprExtpolClientConnProtocol_Object = MibTableColumn
cfprExtpolClientConnProtocol = _CfprExtpolClientConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 5),
    _CfprExtpolClientConnProtocol_Type()
)
cfprExtpolClientConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientConnProtocol.setStatus("current")
_CfprExtpolClientDescr_Type = SnmpAdminString
_CfprExtpolClientDescr_Object = MibTableColumn
cfprExtpolClientDescr = _CfprExtpolClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 6),
    _CfprExtpolClientDescr_Type()
)
cfprExtpolClientDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientDescr.setStatus("current")
_CfprExtpolClientGracePeriodUsed_Type = Unsigned64
_CfprExtpolClientGracePeriodUsed_Object = MibTableColumn
cfprExtpolClientGracePeriodUsed = _CfprExtpolClientGracePeriodUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 7),
    _CfprExtpolClientGracePeriodUsed_Type()
)
cfprExtpolClientGracePeriodUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientGracePeriodUsed.setStatus("current")
_CfprExtpolClientGuid_Type = SnmpAdminString
_CfprExtpolClientGuid_Object = MibTableColumn
cfprExtpolClientGuid = _CfprExtpolClientGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 8),
    _CfprExtpolClientGuid_Type()
)
cfprExtpolClientGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientGuid.setStatus("current")
_CfprExtpolClientHost_Type = SnmpAdminString
_CfprExtpolClientHost_Object = MibTableColumn
cfprExtpolClientHost = _CfprExtpolClientHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 9),
    _CfprExtpolClientHost_Type()
)
cfprExtpolClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientHost.setStatus("current")
_CfprExtpolClientId_Type = Gauge32
_CfprExtpolClientId_Object = MibTableColumn
cfprExtpolClientId = _CfprExtpolClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 10),
    _CfprExtpolClientId_Type()
)
cfprExtpolClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientId.setStatus("current")
_CfprExtpolClientInterest_Type = CfprExtpolAppCapability
_CfprExtpolClientInterest_Object = MibTableColumn
cfprExtpolClientInterest = _CfprExtpolClientInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 11),
    _CfprExtpolClientInterest_Type()
)
cfprExtpolClientInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientInterest.setStatus("current")
_CfprExtpolClientIp_Type = InetAddressIPv4
_CfprExtpolClientIp_Object = MibTableColumn
cfprExtpolClientIp = _CfprExtpolClientIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 12),
    _CfprExtpolClientIp_Type()
)
cfprExtpolClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientIp.setStatus("current")
_CfprExtpolClientIpv6_Type = InetAddressIPv6
_CfprExtpolClientIpv6_Object = MibTableColumn
cfprExtpolClientIpv6 = _CfprExtpolClientIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 13),
    _CfprExtpolClientIpv6_Type()
)
cfprExtpolClientIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientIpv6.setStatus("current")
_CfprExtpolClientLastPollTs_Type = DateAndTime
_CfprExtpolClientLastPollTs_Object = MibTableColumn
cfprExtpolClientLastPollTs = _CfprExtpolClientLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 14),
    _CfprExtpolClientLastPollTs_Type()
)
cfprExtpolClientLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientLastPollTs.setStatus("current")
_CfprExtpolClientLicState_Type = CfprExtpolState
_CfprExtpolClientLicState_Object = MibTableColumn
cfprExtpolClientLicState = _CfprExtpolClientLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 15),
    _CfprExtpolClientLicState_Type()
)
cfprExtpolClientLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientLicState.setStatus("current")
_CfprExtpolClientName_Type = SnmpAdminString
_CfprExtpolClientName_Object = MibTableColumn
cfprExtpolClientName = _CfprExtpolClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 16),
    _CfprExtpolClientName_Type()
)
cfprExtpolClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientName.setStatus("current")
_CfprExtpolClientOperState_Type = CfprExtpolConnectorOperState
_CfprExtpolClientOperState_Object = MibTableColumn
cfprExtpolClientOperState = _CfprExtpolClientOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 17),
    _CfprExtpolClientOperState_Type()
)
cfprExtpolClientOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientOperState.setStatus("current")
_CfprExtpolClientOwner_Type = SnmpAdminString
_CfprExtpolClientOwner_Object = MibTableColumn
cfprExtpolClientOwner = _CfprExtpolClientOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 18),
    _CfprExtpolClientOwner_Type()
)
cfprExtpolClientOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientOwner.setStatus("current")
_CfprExtpolClientSite_Type = SnmpAdminString
_CfprExtpolClientSite_Object = MibTableColumn
cfprExtpolClientSite = _CfprExtpolClientSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 19),
    _CfprExtpolClientSite_Type()
)
cfprExtpolClientSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientSite.setStatus("current")
_CfprExtpolClientSuspendState_Type = CfprExtpolSuspendState
_CfprExtpolClientSuspendState_Object = MibTableColumn
cfprExtpolClientSuspendState = _CfprExtpolClientSuspendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 20),
    _CfprExtpolClientSuspendState_Type()
)
cfprExtpolClientSuspendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientSuspendState.setStatus("current")
_CfprExtpolClientType_Type = CfprExtpolConnType
_CfprExtpolClientType_Object = MibTableColumn
cfprExtpolClientType = _CfprExtpolClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 21),
    _CfprExtpolClientType_Type()
)
cfprExtpolClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientType.setStatus("current")
_CfprExtpolClientVersion_Type = SnmpAdminString
_CfprExtpolClientVersion_Object = MibTableColumn
cfprExtpolClientVersion = _CfprExtpolClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 1, 1, 22),
    _CfprExtpolClientVersion_Type()
)
cfprExtpolClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientVersion.setStatus("current")
_CfprExtpolClientContTable_Object = MibTable
cfprExtpolClientContTable = _CfprExtpolClientContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 2)
)
if mibBuilder.loadTexts:
    cfprExtpolClientContTable.setStatus("current")
_CfprExtpolClientContEntry_Object = MibTableRow
cfprExtpolClientContEntry = _CfprExtpolClientContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 2, 1)
)
cfprExtpolClientContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolClientContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolClientContEntry.setStatus("current")
_CfprExtpolClientContInstanceId_Type = CfprManagedObjectId
_CfprExtpolClientContInstanceId_Object = MibTableColumn
cfprExtpolClientContInstanceId = _CfprExtpolClientContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 2, 1, 1),
    _CfprExtpolClientContInstanceId_Type()
)
cfprExtpolClientContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolClientContInstanceId.setStatus("current")
_CfprExtpolClientContDn_Type = CfprManagedObjectDn
_CfprExtpolClientContDn_Object = MibTableColumn
cfprExtpolClientContDn = _CfprExtpolClientContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 2, 1, 2),
    _CfprExtpolClientContDn_Type()
)
cfprExtpolClientContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientContDn.setStatus("current")
_CfprExtpolClientContRn_Type = SnmpAdminString
_CfprExtpolClientContRn_Object = MibTableColumn
cfprExtpolClientContRn = _CfprExtpolClientContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 2, 1, 3),
    _CfprExtpolClientContRn_Type()
)
cfprExtpolClientContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientContRn.setStatus("current")
_CfprExtpolClientContGenNum_Type = Gauge32
_CfprExtpolClientContGenNum_Object = MibTableColumn
cfprExtpolClientContGenNum = _CfprExtpolClientContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 2, 1, 4),
    _CfprExtpolClientContGenNum_Type()
)
cfprExtpolClientContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolClientContGenNum.setStatus("current")
_CfprExtpolControllerTable_Object = MibTable
cfprExtpolControllerTable = _CfprExtpolControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3)
)
if mibBuilder.loadTexts:
    cfprExtpolControllerTable.setStatus("current")
_CfprExtpolControllerEntry_Object = MibTableRow
cfprExtpolControllerEntry = _CfprExtpolControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1)
)
cfprExtpolControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolControllerEntry.setStatus("current")
_CfprExtpolControllerInstanceId_Type = CfprManagedObjectId
_CfprExtpolControllerInstanceId_Object = MibTableColumn
cfprExtpolControllerInstanceId = _CfprExtpolControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 1),
    _CfprExtpolControllerInstanceId_Type()
)
cfprExtpolControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolControllerInstanceId.setStatus("current")
_CfprExtpolControllerDn_Type = CfprManagedObjectDn
_CfprExtpolControllerDn_Object = MibTableColumn
cfprExtpolControllerDn = _CfprExtpolControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 2),
    _CfprExtpolControllerDn_Type()
)
cfprExtpolControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerDn.setStatus("current")
_CfprExtpolControllerRn_Type = SnmpAdminString
_CfprExtpolControllerRn_Object = MibTableColumn
cfprExtpolControllerRn = _CfprExtpolControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 3),
    _CfprExtpolControllerRn_Type()
)
cfprExtpolControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerRn.setStatus("current")
_CfprExtpolControllerCapability_Type = CfprExtpolAppCapability
_CfprExtpolControllerCapability_Object = MibTableColumn
cfprExtpolControllerCapability = _CfprExtpolControllerCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 4),
    _CfprExtpolControllerCapability_Type()
)
cfprExtpolControllerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerCapability.setStatus("current")
_CfprExtpolControllerConnProtocol_Type = CfprExtpolConnProtocol
_CfprExtpolControllerConnProtocol_Object = MibTableColumn
cfprExtpolControllerConnProtocol = _CfprExtpolControllerConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 5),
    _CfprExtpolControllerConnProtocol_Type()
)
cfprExtpolControllerConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerConnProtocol.setStatus("current")
_CfprExtpolControllerHost_Type = SnmpAdminString
_CfprExtpolControllerHost_Object = MibTableColumn
cfprExtpolControllerHost = _CfprExtpolControllerHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 6),
    _CfprExtpolControllerHost_Type()
)
cfprExtpolControllerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerHost.setStatus("current")
_CfprExtpolControllerId_Type = Gauge32
_CfprExtpolControllerId_Object = MibTableColumn
cfprExtpolControllerId = _CfprExtpolControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 7),
    _CfprExtpolControllerId_Type()
)
cfprExtpolControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerId.setStatus("current")
_CfprExtpolControllerInterest_Type = CfprExtpolAppCapability
_CfprExtpolControllerInterest_Object = MibTableColumn
cfprExtpolControllerInterest = _CfprExtpolControllerInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 8),
    _CfprExtpolControllerInterest_Type()
)
cfprExtpolControllerInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerInterest.setStatus("current")
_CfprExtpolControllerIp_Type = InetAddressIPv4
_CfprExtpolControllerIp_Object = MibTableColumn
cfprExtpolControllerIp = _CfprExtpolControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 9),
    _CfprExtpolControllerIp_Type()
)
cfprExtpolControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerIp.setStatus("current")
_CfprExtpolControllerIpv6_Type = InetAddressIPv6
_CfprExtpolControllerIpv6_Object = MibTableColumn
cfprExtpolControllerIpv6 = _CfprExtpolControllerIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 10),
    _CfprExtpolControllerIpv6_Type()
)
cfprExtpolControllerIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerIpv6.setStatus("current")
_CfprExtpolControllerLastPollTs_Type = DateAndTime
_CfprExtpolControllerLastPollTs_Object = MibTableColumn
cfprExtpolControllerLastPollTs = _CfprExtpolControllerLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 11),
    _CfprExtpolControllerLastPollTs_Type()
)
cfprExtpolControllerLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerLastPollTs.setStatus("current")
_CfprExtpolControllerName_Type = SnmpAdminString
_CfprExtpolControllerName_Object = MibTableColumn
cfprExtpolControllerName = _CfprExtpolControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 12),
    _CfprExtpolControllerName_Type()
)
cfprExtpolControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerName.setStatus("current")
_CfprExtpolControllerOperState_Type = CfprExtpolConnectorOperState
_CfprExtpolControllerOperState_Object = MibTableColumn
cfprExtpolControllerOperState = _CfprExtpolControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 13),
    _CfprExtpolControllerOperState_Type()
)
cfprExtpolControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerOperState.setStatus("current")
_CfprExtpolControllerType_Type = CfprExtpolConnType
_CfprExtpolControllerType_Object = MibTableColumn
cfprExtpolControllerType = _CfprExtpolControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 14),
    _CfprExtpolControllerType_Type()
)
cfprExtpolControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerType.setStatus("current")
_CfprExtpolControllerVersion_Type = SnmpAdminString
_CfprExtpolControllerVersion_Object = MibTableColumn
cfprExtpolControllerVersion = _CfprExtpolControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 3, 1, 15),
    _CfprExtpolControllerVersion_Type()
)
cfprExtpolControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerVersion.setStatus("current")
_CfprExtpolControllerContTable_Object = MibTable
cfprExtpolControllerContTable = _CfprExtpolControllerContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 4)
)
if mibBuilder.loadTexts:
    cfprExtpolControllerContTable.setStatus("current")
_CfprExtpolControllerContEntry_Object = MibTableRow
cfprExtpolControllerContEntry = _CfprExtpolControllerContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 4, 1)
)
cfprExtpolControllerContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolControllerContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolControllerContEntry.setStatus("current")
_CfprExtpolControllerContInstanceId_Type = CfprManagedObjectId
_CfprExtpolControllerContInstanceId_Object = MibTableColumn
cfprExtpolControllerContInstanceId = _CfprExtpolControllerContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 4, 1, 1),
    _CfprExtpolControllerContInstanceId_Type()
)
cfprExtpolControllerContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolControllerContInstanceId.setStatus("current")
_CfprExtpolControllerContDn_Type = CfprManagedObjectDn
_CfprExtpolControllerContDn_Object = MibTableColumn
cfprExtpolControllerContDn = _CfprExtpolControllerContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 4, 1, 2),
    _CfprExtpolControllerContDn_Type()
)
cfprExtpolControllerContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerContDn.setStatus("current")
_CfprExtpolControllerContRn_Type = SnmpAdminString
_CfprExtpolControllerContRn_Object = MibTableColumn
cfprExtpolControllerContRn = _CfprExtpolControllerContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 4, 1, 3),
    _CfprExtpolControllerContRn_Type()
)
cfprExtpolControllerContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerContRn.setStatus("current")
_CfprExtpolControllerContGenNum_Type = Gauge32
_CfprExtpolControllerContGenNum_Object = MibTableColumn
cfprExtpolControllerContGenNum = _CfprExtpolControllerContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 4, 1, 4),
    _CfprExtpolControllerContGenNum_Type()
)
cfprExtpolControllerContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolControllerContGenNum.setStatus("current")
_CfprExtpolEpTable_Object = MibTable
cfprExtpolEpTable = _CfprExtpolEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5)
)
if mibBuilder.loadTexts:
    cfprExtpolEpTable.setStatus("current")
_CfprExtpolEpEntry_Object = MibTableRow
cfprExtpolEpEntry = _CfprExtpolEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1)
)
cfprExtpolEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolEpEntry.setStatus("current")
_CfprExtpolEpInstanceId_Type = CfprManagedObjectId
_CfprExtpolEpInstanceId_Object = MibTableColumn
cfprExtpolEpInstanceId = _CfprExtpolEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 1),
    _CfprExtpolEpInstanceId_Type()
)
cfprExtpolEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolEpInstanceId.setStatus("current")
_CfprExtpolEpDn_Type = CfprManagedObjectDn
_CfprExtpolEpDn_Object = MibTableColumn
cfprExtpolEpDn = _CfprExtpolEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 2),
    _CfprExtpolEpDn_Type()
)
cfprExtpolEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpDn.setStatus("current")
_CfprExtpolEpRn_Type = SnmpAdminString
_CfprExtpolEpRn_Object = MibTableColumn
cfprExtpolEpRn = _CfprExtpolEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 3),
    _CfprExtpolEpRn_Type()
)
cfprExtpolEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpRn.setStatus("current")
_CfprExtpolEpFsmDescr_Type = SnmpAdminString
_CfprExtpolEpFsmDescr_Object = MibTableColumn
cfprExtpolEpFsmDescr = _CfprExtpolEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 4),
    _CfprExtpolEpFsmDescr_Type()
)
cfprExtpolEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmDescr.setStatus("current")
_CfprExtpolEpFsmPrev_Type = SnmpAdminString
_CfprExtpolEpFsmPrev_Object = MibTableColumn
cfprExtpolEpFsmPrev = _CfprExtpolEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 5),
    _CfprExtpolEpFsmPrev_Type()
)
cfprExtpolEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmPrev.setStatus("current")
_CfprExtpolEpFsmProgr_Type = Gauge32
_CfprExtpolEpFsmProgr_Object = MibTableColumn
cfprExtpolEpFsmProgr = _CfprExtpolEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 6),
    _CfprExtpolEpFsmProgr_Type()
)
cfprExtpolEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmProgr.setStatus("current")
_CfprExtpolEpFsmRmtInvErrCode_Type = Gauge32
_CfprExtpolEpFsmRmtInvErrCode_Object = MibTableColumn
cfprExtpolEpFsmRmtInvErrCode = _CfprExtpolEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 7),
    _CfprExtpolEpFsmRmtInvErrCode_Type()
)
cfprExtpolEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRmtInvErrCode.setStatus("current")
_CfprExtpolEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtpolEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtpolEpFsmRmtInvErrDescr = _CfprExtpolEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 8),
    _CfprExtpolEpFsmRmtInvErrDescr_Type()
)
cfprExtpolEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRmtInvErrDescr.setStatus("current")
_CfprExtpolEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtpolEpFsmRmtInvRslt_Object = MibTableColumn
cfprExtpolEpFsmRmtInvRslt = _CfprExtpolEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 9),
    _CfprExtpolEpFsmRmtInvRslt_Type()
)
cfprExtpolEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRmtInvRslt.setStatus("current")
_CfprExtpolEpFsmStageDescr_Type = SnmpAdminString
_CfprExtpolEpFsmStageDescr_Object = MibTableColumn
cfprExtpolEpFsmStageDescr = _CfprExtpolEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 10),
    _CfprExtpolEpFsmStageDescr_Type()
)
cfprExtpolEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageDescr.setStatus("current")
_CfprExtpolEpFsmStamp_Type = DateAndTime
_CfprExtpolEpFsmStamp_Object = MibTableColumn
cfprExtpolEpFsmStamp = _CfprExtpolEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 11),
    _CfprExtpolEpFsmStamp_Type()
)
cfprExtpolEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStamp.setStatus("current")
_CfprExtpolEpFsmStatus_Type = SnmpAdminString
_CfprExtpolEpFsmStatus_Object = MibTableColumn
cfprExtpolEpFsmStatus = _CfprExtpolEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 12),
    _CfprExtpolEpFsmStatus_Type()
)
cfprExtpolEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStatus.setStatus("current")
_CfprExtpolEpFsmTry_Type = Gauge32
_CfprExtpolEpFsmTry_Object = MibTableColumn
cfprExtpolEpFsmTry = _CfprExtpolEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 5, 1, 13),
    _CfprExtpolEpFsmTry_Type()
)
cfprExtpolEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTry.setStatus("current")
_CfprExtpolEpFsmTable_Object = MibTable
cfprExtpolEpFsmTable = _CfprExtpolEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6)
)
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTable.setStatus("current")
_CfprExtpolEpFsmEntry_Object = MibTableRow
cfprExtpolEpFsmEntry = _CfprExtpolEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1)
)
cfprExtpolEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolEpFsmEntry.setStatus("current")
_CfprExtpolEpFsmInstanceId_Type = CfprManagedObjectId
_CfprExtpolEpFsmInstanceId_Object = MibTableColumn
cfprExtpolEpFsmInstanceId = _CfprExtpolEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 1),
    _CfprExtpolEpFsmInstanceId_Type()
)
cfprExtpolEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmInstanceId.setStatus("current")
_CfprExtpolEpFsmDn_Type = CfprManagedObjectDn
_CfprExtpolEpFsmDn_Object = MibTableColumn
cfprExtpolEpFsmDn = _CfprExtpolEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 2),
    _CfprExtpolEpFsmDn_Type()
)
cfprExtpolEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmDn.setStatus("current")
_CfprExtpolEpFsmRn_Type = SnmpAdminString
_CfprExtpolEpFsmRn_Object = MibTableColumn
cfprExtpolEpFsmRn = _CfprExtpolEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 3),
    _CfprExtpolEpFsmRn_Type()
)
cfprExtpolEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRn.setStatus("current")
_CfprExtpolEpFsmCompletionTime_Type = DateAndTime
_CfprExtpolEpFsmCompletionTime_Object = MibTableColumn
cfprExtpolEpFsmCompletionTime = _CfprExtpolEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 4),
    _CfprExtpolEpFsmCompletionTime_Type()
)
cfprExtpolEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmCompletionTime.setStatus("current")
_CfprExtpolEpFsmCurrentFsm_Type = CfprExtpolEpFsmCurrentFsm
_CfprExtpolEpFsmCurrentFsm_Object = MibTableColumn
cfprExtpolEpFsmCurrentFsm = _CfprExtpolEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 5),
    _CfprExtpolEpFsmCurrentFsm_Type()
)
cfprExtpolEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmCurrentFsm.setStatus("current")
_CfprExtpolEpFsmDescrData_Type = SnmpAdminString
_CfprExtpolEpFsmDescrData_Object = MibTableColumn
cfprExtpolEpFsmDescrData = _CfprExtpolEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 6),
    _CfprExtpolEpFsmDescrData_Type()
)
cfprExtpolEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmDescrData.setStatus("current")
_CfprExtpolEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtpolEpFsmFsmStatus_Object = MibTableColumn
cfprExtpolEpFsmFsmStatus = _CfprExtpolEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 7),
    _CfprExtpolEpFsmFsmStatus_Type()
)
cfprExtpolEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmFsmStatus.setStatus("current")
_CfprExtpolEpFsmProgress_Type = Gauge32
_CfprExtpolEpFsmProgress_Object = MibTableColumn
cfprExtpolEpFsmProgress = _CfprExtpolEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 8),
    _CfprExtpolEpFsmProgress_Type()
)
cfprExtpolEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmProgress.setStatus("current")
_CfprExtpolEpFsmRmtErrCode_Type = Gauge32
_CfprExtpolEpFsmRmtErrCode_Object = MibTableColumn
cfprExtpolEpFsmRmtErrCode = _CfprExtpolEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 9),
    _CfprExtpolEpFsmRmtErrCode_Type()
)
cfprExtpolEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRmtErrCode.setStatus("current")
_CfprExtpolEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtpolEpFsmRmtErrDescr_Object = MibTableColumn
cfprExtpolEpFsmRmtErrDescr = _CfprExtpolEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 10),
    _CfprExtpolEpFsmRmtErrDescr_Type()
)
cfprExtpolEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRmtErrDescr.setStatus("current")
_CfprExtpolEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtpolEpFsmRmtRslt_Object = MibTableColumn
cfprExtpolEpFsmRmtRslt = _CfprExtpolEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 6, 1, 11),
    _CfprExtpolEpFsmRmtRslt_Type()
)
cfprExtpolEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmRmtRslt.setStatus("current")
_CfprExtpolEpFsmStageTable_Object = MibTable
cfprExtpolEpFsmStageTable = _CfprExtpolEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7)
)
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageTable.setStatus("current")
_CfprExtpolEpFsmStageEntry_Object = MibTableRow
cfprExtpolEpFsmStageEntry = _CfprExtpolEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1)
)
cfprExtpolEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageEntry.setStatus("current")
_CfprExtpolEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtpolEpFsmStageInstanceId_Object = MibTableColumn
cfprExtpolEpFsmStageInstanceId = _CfprExtpolEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 1),
    _CfprExtpolEpFsmStageInstanceId_Type()
)
cfprExtpolEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageInstanceId.setStatus("current")
_CfprExtpolEpFsmStageDn_Type = CfprManagedObjectDn
_CfprExtpolEpFsmStageDn_Object = MibTableColumn
cfprExtpolEpFsmStageDn = _CfprExtpolEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 2),
    _CfprExtpolEpFsmStageDn_Type()
)
cfprExtpolEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageDn.setStatus("current")
_CfprExtpolEpFsmStageRn_Type = SnmpAdminString
_CfprExtpolEpFsmStageRn_Object = MibTableColumn
cfprExtpolEpFsmStageRn = _CfprExtpolEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 3),
    _CfprExtpolEpFsmStageRn_Type()
)
cfprExtpolEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageRn.setStatus("current")
_CfprExtpolEpFsmStageDescrData_Type = SnmpAdminString
_CfprExtpolEpFsmStageDescrData_Object = MibTableColumn
cfprExtpolEpFsmStageDescrData = _CfprExtpolEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 4),
    _CfprExtpolEpFsmStageDescrData_Type()
)
cfprExtpolEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageDescrData.setStatus("current")
_CfprExtpolEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtpolEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtpolEpFsmStageLastUpdateTime = _CfprExtpolEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 5),
    _CfprExtpolEpFsmStageLastUpdateTime_Type()
)
cfprExtpolEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageLastUpdateTime.setStatus("current")
_CfprExtpolEpFsmStageName_Type = CfprExtpolEpFsmStageName
_CfprExtpolEpFsmStageName_Object = MibTableColumn
cfprExtpolEpFsmStageName = _CfprExtpolEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 6),
    _CfprExtpolEpFsmStageName_Type()
)
cfprExtpolEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageName.setStatus("current")
_CfprExtpolEpFsmStageOrder_Type = Gauge32
_CfprExtpolEpFsmStageOrder_Object = MibTableColumn
cfprExtpolEpFsmStageOrder = _CfprExtpolEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 7),
    _CfprExtpolEpFsmStageOrder_Type()
)
cfprExtpolEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageOrder.setStatus("current")
_CfprExtpolEpFsmStageRetry_Type = Gauge32
_CfprExtpolEpFsmStageRetry_Object = MibTableColumn
cfprExtpolEpFsmStageRetry = _CfprExtpolEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 8),
    _CfprExtpolEpFsmStageRetry_Type()
)
cfprExtpolEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageRetry.setStatus("current")
_CfprExtpolEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtpolEpFsmStageStageStatus_Object = MibTableColumn
cfprExtpolEpFsmStageStageStatus = _CfprExtpolEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 7, 1, 9),
    _CfprExtpolEpFsmStageStageStatus_Type()
)
cfprExtpolEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmStageStageStatus.setStatus("current")
_CfprExtpolEpFsmTaskTable_Object = MibTable
cfprExtpolEpFsmTaskTable = _CfprExtpolEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8)
)
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskTable.setStatus("current")
_CfprExtpolEpFsmTaskEntry_Object = MibTableRow
cfprExtpolEpFsmTaskEntry = _CfprExtpolEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1)
)
cfprExtpolEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskEntry.setStatus("current")
_CfprExtpolEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtpolEpFsmTaskInstanceId_Object = MibTableColumn
cfprExtpolEpFsmTaskInstanceId = _CfprExtpolEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 1),
    _CfprExtpolEpFsmTaskInstanceId_Type()
)
cfprExtpolEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskInstanceId.setStatus("current")
_CfprExtpolEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtpolEpFsmTaskDn_Object = MibTableColumn
cfprExtpolEpFsmTaskDn = _CfprExtpolEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 2),
    _CfprExtpolEpFsmTaskDn_Type()
)
cfprExtpolEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskDn.setStatus("current")
_CfprExtpolEpFsmTaskRn_Type = SnmpAdminString
_CfprExtpolEpFsmTaskRn_Object = MibTableColumn
cfprExtpolEpFsmTaskRn = _CfprExtpolEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 3),
    _CfprExtpolEpFsmTaskRn_Type()
)
cfprExtpolEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskRn.setStatus("current")
_CfprExtpolEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtpolEpFsmTaskCompletion_Object = MibTableColumn
cfprExtpolEpFsmTaskCompletion = _CfprExtpolEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 4),
    _CfprExtpolEpFsmTaskCompletion_Type()
)
cfprExtpolEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskCompletion.setStatus("current")
_CfprExtpolEpFsmTaskFlags_Type = CfprFsmFlags
_CfprExtpolEpFsmTaskFlags_Object = MibTableColumn
cfprExtpolEpFsmTaskFlags = _CfprExtpolEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 5),
    _CfprExtpolEpFsmTaskFlags_Type()
)
cfprExtpolEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskFlags.setStatus("current")
_CfprExtpolEpFsmTaskItem_Type = CfprExtpolEpFsmTaskItem
_CfprExtpolEpFsmTaskItem_Object = MibTableColumn
cfprExtpolEpFsmTaskItem = _CfprExtpolEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 6),
    _CfprExtpolEpFsmTaskItem_Type()
)
cfprExtpolEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskItem.setStatus("current")
_CfprExtpolEpFsmTaskSeqId_Type = Gauge32
_CfprExtpolEpFsmTaskSeqId_Object = MibTableColumn
cfprExtpolEpFsmTaskSeqId = _CfprExtpolEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 8, 1, 7),
    _CfprExtpolEpFsmTaskSeqId_Type()
)
cfprExtpolEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolEpFsmTaskSeqId.setStatus("current")
_CfprExtpolProviderTable_Object = MibTable
cfprExtpolProviderTable = _CfprExtpolProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9)
)
if mibBuilder.loadTexts:
    cfprExtpolProviderTable.setStatus("current")
_CfprExtpolProviderEntry_Object = MibTableRow
cfprExtpolProviderEntry = _CfprExtpolProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1)
)
cfprExtpolProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolProviderEntry.setStatus("current")
_CfprExtpolProviderInstanceId_Type = CfprManagedObjectId
_CfprExtpolProviderInstanceId_Object = MibTableColumn
cfprExtpolProviderInstanceId = _CfprExtpolProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 1),
    _CfprExtpolProviderInstanceId_Type()
)
cfprExtpolProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolProviderInstanceId.setStatus("current")
_CfprExtpolProviderDn_Type = CfprManagedObjectDn
_CfprExtpolProviderDn_Object = MibTableColumn
cfprExtpolProviderDn = _CfprExtpolProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 2),
    _CfprExtpolProviderDn_Type()
)
cfprExtpolProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderDn.setStatus("current")
_CfprExtpolProviderRn_Type = SnmpAdminString
_CfprExtpolProviderRn_Object = MibTableColumn
cfprExtpolProviderRn = _CfprExtpolProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 3),
    _CfprExtpolProviderRn_Type()
)
cfprExtpolProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderRn.setStatus("current")
_CfprExtpolProviderCapability_Type = CfprExtpolAppCapability
_CfprExtpolProviderCapability_Object = MibTableColumn
cfprExtpolProviderCapability = _CfprExtpolProviderCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 4),
    _CfprExtpolProviderCapability_Type()
)
cfprExtpolProviderCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderCapability.setStatus("current")
_CfprExtpolProviderConnProtocol_Type = CfprExtpolConnProtocol
_CfprExtpolProviderConnProtocol_Object = MibTableColumn
cfprExtpolProviderConnProtocol = _CfprExtpolProviderConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 5),
    _CfprExtpolProviderConnProtocol_Type()
)
cfprExtpolProviderConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderConnProtocol.setStatus("current")
_CfprExtpolProviderFsmDescr_Type = SnmpAdminString
_CfprExtpolProviderFsmDescr_Object = MibTableColumn
cfprExtpolProviderFsmDescr = _CfprExtpolProviderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 6),
    _CfprExtpolProviderFsmDescr_Type()
)
cfprExtpolProviderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmDescr.setStatus("current")
_CfprExtpolProviderFsmPrev_Type = SnmpAdminString
_CfprExtpolProviderFsmPrev_Object = MibTableColumn
cfprExtpolProviderFsmPrev = _CfprExtpolProviderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 7),
    _CfprExtpolProviderFsmPrev_Type()
)
cfprExtpolProviderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmPrev.setStatus("current")
_CfprExtpolProviderFsmProgr_Type = Gauge32
_CfprExtpolProviderFsmProgr_Object = MibTableColumn
cfprExtpolProviderFsmProgr = _CfprExtpolProviderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 8),
    _CfprExtpolProviderFsmProgr_Type()
)
cfprExtpolProviderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmProgr.setStatus("current")
_CfprExtpolProviderFsmRmtInvErrCode_Type = Gauge32
_CfprExtpolProviderFsmRmtInvErrCode_Object = MibTableColumn
cfprExtpolProviderFsmRmtInvErrCode = _CfprExtpolProviderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 9),
    _CfprExtpolProviderFsmRmtInvErrCode_Type()
)
cfprExtpolProviderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRmtInvErrCode.setStatus("current")
_CfprExtpolProviderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtpolProviderFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtpolProviderFsmRmtInvErrDescr = _CfprExtpolProviderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 10),
    _CfprExtpolProviderFsmRmtInvErrDescr_Type()
)
cfprExtpolProviderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRmtInvErrDescr.setStatus("current")
_CfprExtpolProviderFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtpolProviderFsmRmtInvRslt_Object = MibTableColumn
cfprExtpolProviderFsmRmtInvRslt = _CfprExtpolProviderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 11),
    _CfprExtpolProviderFsmRmtInvRslt_Type()
)
cfprExtpolProviderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRmtInvRslt.setStatus("current")
_CfprExtpolProviderFsmStageDescr_Type = SnmpAdminString
_CfprExtpolProviderFsmStageDescr_Object = MibTableColumn
cfprExtpolProviderFsmStageDescr = _CfprExtpolProviderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 12),
    _CfprExtpolProviderFsmStageDescr_Type()
)
cfprExtpolProviderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageDescr.setStatus("current")
_CfprExtpolProviderFsmStamp_Type = DateAndTime
_CfprExtpolProviderFsmStamp_Object = MibTableColumn
cfprExtpolProviderFsmStamp = _CfprExtpolProviderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 13),
    _CfprExtpolProviderFsmStamp_Type()
)
cfprExtpolProviderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStamp.setStatus("current")
_CfprExtpolProviderFsmStatus_Type = SnmpAdminString
_CfprExtpolProviderFsmStatus_Object = MibTableColumn
cfprExtpolProviderFsmStatus = _CfprExtpolProviderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 14),
    _CfprExtpolProviderFsmStatus_Type()
)
cfprExtpolProviderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStatus.setStatus("current")
_CfprExtpolProviderFsmTry_Type = Gauge32
_CfprExtpolProviderFsmTry_Object = MibTableColumn
cfprExtpolProviderFsmTry = _CfprExtpolProviderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 15),
    _CfprExtpolProviderFsmTry_Type()
)
cfprExtpolProviderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTry.setStatus("current")
_CfprExtpolProviderHost_Type = SnmpAdminString
_CfprExtpolProviderHost_Object = MibTableColumn
cfprExtpolProviderHost = _CfprExtpolProviderHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 16),
    _CfprExtpolProviderHost_Type()
)
cfprExtpolProviderHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderHost.setStatus("current")
_CfprExtpolProviderId_Type = Gauge32
_CfprExtpolProviderId_Object = MibTableColumn
cfprExtpolProviderId = _CfprExtpolProviderId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 17),
    _CfprExtpolProviderId_Type()
)
cfprExtpolProviderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderId.setStatus("current")
_CfprExtpolProviderInterest_Type = CfprExtpolAppCapability
_CfprExtpolProviderInterest_Object = MibTableColumn
cfprExtpolProviderInterest = _CfprExtpolProviderInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 18),
    _CfprExtpolProviderInterest_Type()
)
cfprExtpolProviderInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderInterest.setStatus("current")
_CfprExtpolProviderIp_Type = InetAddressIPv4
_CfprExtpolProviderIp_Object = MibTableColumn
cfprExtpolProviderIp = _CfprExtpolProviderIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 19),
    _CfprExtpolProviderIp_Type()
)
cfprExtpolProviderIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderIp.setStatus("current")
_CfprExtpolProviderIpv6_Type = InetAddressIPv6
_CfprExtpolProviderIpv6_Object = MibTableColumn
cfprExtpolProviderIpv6 = _CfprExtpolProviderIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 20),
    _CfprExtpolProviderIpv6_Type()
)
cfprExtpolProviderIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderIpv6.setStatus("current")
_CfprExtpolProviderLastPollTs_Type = DateAndTime
_CfprExtpolProviderLastPollTs_Object = MibTableColumn
cfprExtpolProviderLastPollTs = _CfprExtpolProviderLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 21),
    _CfprExtpolProviderLastPollTs_Type()
)
cfprExtpolProviderLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderLastPollTs.setStatus("current")
_CfprExtpolProviderName_Type = SnmpAdminString
_CfprExtpolProviderName_Object = MibTableColumn
cfprExtpolProviderName = _CfprExtpolProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 22),
    _CfprExtpolProviderName_Type()
)
cfprExtpolProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderName.setStatus("current")
_CfprExtpolProviderOperState_Type = CfprExtpolConnectorOperState
_CfprExtpolProviderOperState_Object = MibTableColumn
cfprExtpolProviderOperState = _CfprExtpolProviderOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 23),
    _CfprExtpolProviderOperState_Type()
)
cfprExtpolProviderOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderOperState.setStatus("current")
_CfprExtpolProviderType_Type = CfprExtpolConnType
_CfprExtpolProviderType_Object = MibTableColumn
cfprExtpolProviderType = _CfprExtpolProviderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 24),
    _CfprExtpolProviderType_Type()
)
cfprExtpolProviderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderType.setStatus("current")
_CfprExtpolProviderVersion_Type = SnmpAdminString
_CfprExtpolProviderVersion_Object = MibTableColumn
cfprExtpolProviderVersion = _CfprExtpolProviderVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 9, 1, 25),
    _CfprExtpolProviderVersion_Type()
)
cfprExtpolProviderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderVersion.setStatus("current")
_CfprExtpolProviderContTable_Object = MibTable
cfprExtpolProviderContTable = _CfprExtpolProviderContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 10)
)
if mibBuilder.loadTexts:
    cfprExtpolProviderContTable.setStatus("current")
_CfprExtpolProviderContEntry_Object = MibTableRow
cfprExtpolProviderContEntry = _CfprExtpolProviderContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 10, 1)
)
cfprExtpolProviderContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolProviderContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolProviderContEntry.setStatus("current")
_CfprExtpolProviderContInstanceId_Type = CfprManagedObjectId
_CfprExtpolProviderContInstanceId_Object = MibTableColumn
cfprExtpolProviderContInstanceId = _CfprExtpolProviderContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 10, 1, 1),
    _CfprExtpolProviderContInstanceId_Type()
)
cfprExtpolProviderContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolProviderContInstanceId.setStatus("current")
_CfprExtpolProviderContDn_Type = CfprManagedObjectDn
_CfprExtpolProviderContDn_Object = MibTableColumn
cfprExtpolProviderContDn = _CfprExtpolProviderContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 10, 1, 2),
    _CfprExtpolProviderContDn_Type()
)
cfprExtpolProviderContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderContDn.setStatus("current")
_CfprExtpolProviderContRn_Type = SnmpAdminString
_CfprExtpolProviderContRn_Object = MibTableColumn
cfprExtpolProviderContRn = _CfprExtpolProviderContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 10, 1, 3),
    _CfprExtpolProviderContRn_Type()
)
cfprExtpolProviderContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderContRn.setStatus("current")
_CfprExtpolProviderContGenNum_Type = Gauge32
_CfprExtpolProviderContGenNum_Object = MibTableColumn
cfprExtpolProviderContGenNum = _CfprExtpolProviderContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 10, 1, 4),
    _CfprExtpolProviderContGenNum_Type()
)
cfprExtpolProviderContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderContGenNum.setStatus("current")
_CfprExtpolProviderFsmTable_Object = MibTable
cfprExtpolProviderFsmTable = _CfprExtpolProviderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11)
)
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTable.setStatus("current")
_CfprExtpolProviderFsmEntry_Object = MibTableRow
cfprExtpolProviderFsmEntry = _CfprExtpolProviderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1)
)
cfprExtpolProviderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolProviderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmEntry.setStatus("current")
_CfprExtpolProviderFsmInstanceId_Type = CfprManagedObjectId
_CfprExtpolProviderFsmInstanceId_Object = MibTableColumn
cfprExtpolProviderFsmInstanceId = _CfprExtpolProviderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 1),
    _CfprExtpolProviderFsmInstanceId_Type()
)
cfprExtpolProviderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmInstanceId.setStatus("current")
_CfprExtpolProviderFsmDn_Type = CfprManagedObjectDn
_CfprExtpolProviderFsmDn_Object = MibTableColumn
cfprExtpolProviderFsmDn = _CfprExtpolProviderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 2),
    _CfprExtpolProviderFsmDn_Type()
)
cfprExtpolProviderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmDn.setStatus("current")
_CfprExtpolProviderFsmRn_Type = SnmpAdminString
_CfprExtpolProviderFsmRn_Object = MibTableColumn
cfprExtpolProviderFsmRn = _CfprExtpolProviderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 3),
    _CfprExtpolProviderFsmRn_Type()
)
cfprExtpolProviderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRn.setStatus("current")
_CfprExtpolProviderFsmCompletionTime_Type = DateAndTime
_CfprExtpolProviderFsmCompletionTime_Object = MibTableColumn
cfprExtpolProviderFsmCompletionTime = _CfprExtpolProviderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 4),
    _CfprExtpolProviderFsmCompletionTime_Type()
)
cfprExtpolProviderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmCompletionTime.setStatus("current")
_CfprExtpolProviderFsmCurrentFsm_Type = CfprExtpolProviderFsmCurrentFsm
_CfprExtpolProviderFsmCurrentFsm_Object = MibTableColumn
cfprExtpolProviderFsmCurrentFsm = _CfprExtpolProviderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 5),
    _CfprExtpolProviderFsmCurrentFsm_Type()
)
cfprExtpolProviderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmCurrentFsm.setStatus("current")
_CfprExtpolProviderFsmDescrData_Type = SnmpAdminString
_CfprExtpolProviderFsmDescrData_Object = MibTableColumn
cfprExtpolProviderFsmDescrData = _CfprExtpolProviderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 6),
    _CfprExtpolProviderFsmDescrData_Type()
)
cfprExtpolProviderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmDescrData.setStatus("current")
_CfprExtpolProviderFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtpolProviderFsmFsmStatus_Object = MibTableColumn
cfprExtpolProviderFsmFsmStatus = _CfprExtpolProviderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 7),
    _CfprExtpolProviderFsmFsmStatus_Type()
)
cfprExtpolProviderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmFsmStatus.setStatus("current")
_CfprExtpolProviderFsmProgress_Type = Gauge32
_CfprExtpolProviderFsmProgress_Object = MibTableColumn
cfprExtpolProviderFsmProgress = _CfprExtpolProviderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 8),
    _CfprExtpolProviderFsmProgress_Type()
)
cfprExtpolProviderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmProgress.setStatus("current")
_CfprExtpolProviderFsmRmtErrCode_Type = Gauge32
_CfprExtpolProviderFsmRmtErrCode_Object = MibTableColumn
cfprExtpolProviderFsmRmtErrCode = _CfprExtpolProviderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 9),
    _CfprExtpolProviderFsmRmtErrCode_Type()
)
cfprExtpolProviderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRmtErrCode.setStatus("current")
_CfprExtpolProviderFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtpolProviderFsmRmtErrDescr_Object = MibTableColumn
cfprExtpolProviderFsmRmtErrDescr = _CfprExtpolProviderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 10),
    _CfprExtpolProviderFsmRmtErrDescr_Type()
)
cfprExtpolProviderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRmtErrDescr.setStatus("current")
_CfprExtpolProviderFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtpolProviderFsmRmtRslt_Object = MibTableColumn
cfprExtpolProviderFsmRmtRslt = _CfprExtpolProviderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 11, 1, 11),
    _CfprExtpolProviderFsmRmtRslt_Type()
)
cfprExtpolProviderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmRmtRslt.setStatus("current")
_CfprExtpolProviderFsmStageTable_Object = MibTable
cfprExtpolProviderFsmStageTable = _CfprExtpolProviderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12)
)
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageTable.setStatus("current")
_CfprExtpolProviderFsmStageEntry_Object = MibTableRow
cfprExtpolProviderFsmStageEntry = _CfprExtpolProviderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1)
)
cfprExtpolProviderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolProviderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageEntry.setStatus("current")
_CfprExtpolProviderFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtpolProviderFsmStageInstanceId_Object = MibTableColumn
cfprExtpolProviderFsmStageInstanceId = _CfprExtpolProviderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 1),
    _CfprExtpolProviderFsmStageInstanceId_Type()
)
cfprExtpolProviderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageInstanceId.setStatus("current")
_CfprExtpolProviderFsmStageDn_Type = CfprManagedObjectDn
_CfprExtpolProviderFsmStageDn_Object = MibTableColumn
cfprExtpolProviderFsmStageDn = _CfprExtpolProviderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 2),
    _CfprExtpolProviderFsmStageDn_Type()
)
cfprExtpolProviderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageDn.setStatus("current")
_CfprExtpolProviderFsmStageRn_Type = SnmpAdminString
_CfprExtpolProviderFsmStageRn_Object = MibTableColumn
cfprExtpolProviderFsmStageRn = _CfprExtpolProviderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 3),
    _CfprExtpolProviderFsmStageRn_Type()
)
cfprExtpolProviderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageRn.setStatus("current")
_CfprExtpolProviderFsmStageDescrData_Type = SnmpAdminString
_CfprExtpolProviderFsmStageDescrData_Object = MibTableColumn
cfprExtpolProviderFsmStageDescrData = _CfprExtpolProviderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 4),
    _CfprExtpolProviderFsmStageDescrData_Type()
)
cfprExtpolProviderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageDescrData.setStatus("current")
_CfprExtpolProviderFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtpolProviderFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtpolProviderFsmStageLastUpdateTime = _CfprExtpolProviderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 5),
    _CfprExtpolProviderFsmStageLastUpdateTime_Type()
)
cfprExtpolProviderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageLastUpdateTime.setStatus("current")
_CfprExtpolProviderFsmStageName_Type = CfprExtpolProviderFsmStageName
_CfprExtpolProviderFsmStageName_Object = MibTableColumn
cfprExtpolProviderFsmStageName = _CfprExtpolProviderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 6),
    _CfprExtpolProviderFsmStageName_Type()
)
cfprExtpolProviderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageName.setStatus("current")
_CfprExtpolProviderFsmStageOrder_Type = Gauge32
_CfprExtpolProviderFsmStageOrder_Object = MibTableColumn
cfprExtpolProviderFsmStageOrder = _CfprExtpolProviderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 7),
    _CfprExtpolProviderFsmStageOrder_Type()
)
cfprExtpolProviderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageOrder.setStatus("current")
_CfprExtpolProviderFsmStageRetry_Type = Gauge32
_CfprExtpolProviderFsmStageRetry_Object = MibTableColumn
cfprExtpolProviderFsmStageRetry = _CfprExtpolProviderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 8),
    _CfprExtpolProviderFsmStageRetry_Type()
)
cfprExtpolProviderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageRetry.setStatus("current")
_CfprExtpolProviderFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtpolProviderFsmStageStageStatus_Object = MibTableColumn
cfprExtpolProviderFsmStageStageStatus = _CfprExtpolProviderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 12, 1, 9),
    _CfprExtpolProviderFsmStageStageStatus_Type()
)
cfprExtpolProviderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmStageStageStatus.setStatus("current")
_CfprExtpolProviderFsmTaskTable_Object = MibTable
cfprExtpolProviderFsmTaskTable = _CfprExtpolProviderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13)
)
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskTable.setStatus("current")
_CfprExtpolProviderFsmTaskEntry_Object = MibTableRow
cfprExtpolProviderFsmTaskEntry = _CfprExtpolProviderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1)
)
cfprExtpolProviderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolProviderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskEntry.setStatus("current")
_CfprExtpolProviderFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtpolProviderFsmTaskInstanceId_Object = MibTableColumn
cfprExtpolProviderFsmTaskInstanceId = _CfprExtpolProviderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 1),
    _CfprExtpolProviderFsmTaskInstanceId_Type()
)
cfprExtpolProviderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskInstanceId.setStatus("current")
_CfprExtpolProviderFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtpolProviderFsmTaskDn_Object = MibTableColumn
cfprExtpolProviderFsmTaskDn = _CfprExtpolProviderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 2),
    _CfprExtpolProviderFsmTaskDn_Type()
)
cfprExtpolProviderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskDn.setStatus("current")
_CfprExtpolProviderFsmTaskRn_Type = SnmpAdminString
_CfprExtpolProviderFsmTaskRn_Object = MibTableColumn
cfprExtpolProviderFsmTaskRn = _CfprExtpolProviderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 3),
    _CfprExtpolProviderFsmTaskRn_Type()
)
cfprExtpolProviderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskRn.setStatus("current")
_CfprExtpolProviderFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtpolProviderFsmTaskCompletion_Object = MibTableColumn
cfprExtpolProviderFsmTaskCompletion = _CfprExtpolProviderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 4),
    _CfprExtpolProviderFsmTaskCompletion_Type()
)
cfprExtpolProviderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskCompletion.setStatus("current")
_CfprExtpolProviderFsmTaskFlags_Type = CfprFsmFlags
_CfprExtpolProviderFsmTaskFlags_Object = MibTableColumn
cfprExtpolProviderFsmTaskFlags = _CfprExtpolProviderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 5),
    _CfprExtpolProviderFsmTaskFlags_Type()
)
cfprExtpolProviderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskFlags.setStatus("current")
_CfprExtpolProviderFsmTaskItem_Type = CfprExtpolProviderFsmTaskItem
_CfprExtpolProviderFsmTaskItem_Object = MibTableColumn
cfprExtpolProviderFsmTaskItem = _CfprExtpolProviderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 6),
    _CfprExtpolProviderFsmTaskItem_Type()
)
cfprExtpolProviderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskItem.setStatus("current")
_CfprExtpolProviderFsmTaskSeqId_Type = Gauge32
_CfprExtpolProviderFsmTaskSeqId_Object = MibTableColumn
cfprExtpolProviderFsmTaskSeqId = _CfprExtpolProviderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 13, 1, 7),
    _CfprExtpolProviderFsmTaskSeqId_Type()
)
cfprExtpolProviderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolProviderFsmTaskSeqId.setStatus("current")
_CfprExtpolRegistryTable_Object = MibTable
cfprExtpolRegistryTable = _CfprExtpolRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14)
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryTable.setStatus("current")
_CfprExtpolRegistryEntry_Object = MibTableRow
cfprExtpolRegistryEntry = _CfprExtpolRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1)
)
cfprExtpolRegistryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolRegistryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryEntry.setStatus("current")
_CfprExtpolRegistryInstanceId_Type = CfprManagedObjectId
_CfprExtpolRegistryInstanceId_Object = MibTableColumn
cfprExtpolRegistryInstanceId = _CfprExtpolRegistryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 1),
    _CfprExtpolRegistryInstanceId_Type()
)
cfprExtpolRegistryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolRegistryInstanceId.setStatus("current")
_CfprExtpolRegistryDn_Type = CfprManagedObjectDn
_CfprExtpolRegistryDn_Object = MibTableColumn
cfprExtpolRegistryDn = _CfprExtpolRegistryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 2),
    _CfprExtpolRegistryDn_Type()
)
cfprExtpolRegistryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryDn.setStatus("current")
_CfprExtpolRegistryRn_Type = SnmpAdminString
_CfprExtpolRegistryRn_Object = MibTableColumn
cfprExtpolRegistryRn = _CfprExtpolRegistryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 3),
    _CfprExtpolRegistryRn_Type()
)
cfprExtpolRegistryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryRn.setStatus("current")
_CfprExtpolRegistryCapability_Type = CfprExtpolAppCapability
_CfprExtpolRegistryCapability_Object = MibTableColumn
cfprExtpolRegistryCapability = _CfprExtpolRegistryCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 4),
    _CfprExtpolRegistryCapability_Type()
)
cfprExtpolRegistryCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryCapability.setStatus("current")
_CfprExtpolRegistryConnProtocol_Type = CfprExtpolConnProtocol
_CfprExtpolRegistryConnProtocol_Object = MibTableColumn
cfprExtpolRegistryConnProtocol = _CfprExtpolRegistryConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 5),
    _CfprExtpolRegistryConnProtocol_Type()
)
cfprExtpolRegistryConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryConnProtocol.setStatus("current")
_CfprExtpolRegistryFsmDescr_Type = SnmpAdminString
_CfprExtpolRegistryFsmDescr_Object = MibTableColumn
cfprExtpolRegistryFsmDescr = _CfprExtpolRegistryFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 6),
    _CfprExtpolRegistryFsmDescr_Type()
)
cfprExtpolRegistryFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmDescr.setStatus("current")
_CfprExtpolRegistryFsmPrev_Type = SnmpAdminString
_CfprExtpolRegistryFsmPrev_Object = MibTableColumn
cfprExtpolRegistryFsmPrev = _CfprExtpolRegistryFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 7),
    _CfprExtpolRegistryFsmPrev_Type()
)
cfprExtpolRegistryFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmPrev.setStatus("current")
_CfprExtpolRegistryFsmProgr_Type = Gauge32
_CfprExtpolRegistryFsmProgr_Object = MibTableColumn
cfprExtpolRegistryFsmProgr = _CfprExtpolRegistryFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 8),
    _CfprExtpolRegistryFsmProgr_Type()
)
cfprExtpolRegistryFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmProgr.setStatus("current")
_CfprExtpolRegistryFsmRmtInvErrCode_Type = Gauge32
_CfprExtpolRegistryFsmRmtInvErrCode_Object = MibTableColumn
cfprExtpolRegistryFsmRmtInvErrCode = _CfprExtpolRegistryFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 9),
    _CfprExtpolRegistryFsmRmtInvErrCode_Type()
)
cfprExtpolRegistryFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRmtInvErrCode.setStatus("current")
_CfprExtpolRegistryFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprExtpolRegistryFsmRmtInvErrDescr_Object = MibTableColumn
cfprExtpolRegistryFsmRmtInvErrDescr = _CfprExtpolRegistryFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 10),
    _CfprExtpolRegistryFsmRmtInvErrDescr_Type()
)
cfprExtpolRegistryFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRmtInvErrDescr.setStatus("current")
_CfprExtpolRegistryFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprExtpolRegistryFsmRmtInvRslt_Object = MibTableColumn
cfprExtpolRegistryFsmRmtInvRslt = _CfprExtpolRegistryFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 11),
    _CfprExtpolRegistryFsmRmtInvRslt_Type()
)
cfprExtpolRegistryFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRmtInvRslt.setStatus("current")
_CfprExtpolRegistryFsmStageDescr_Type = SnmpAdminString
_CfprExtpolRegistryFsmStageDescr_Object = MibTableColumn
cfprExtpolRegistryFsmStageDescr = _CfprExtpolRegistryFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 12),
    _CfprExtpolRegistryFsmStageDescr_Type()
)
cfprExtpolRegistryFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageDescr.setStatus("current")
_CfprExtpolRegistryFsmStamp_Type = DateAndTime
_CfprExtpolRegistryFsmStamp_Object = MibTableColumn
cfprExtpolRegistryFsmStamp = _CfprExtpolRegistryFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 13),
    _CfprExtpolRegistryFsmStamp_Type()
)
cfprExtpolRegistryFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStamp.setStatus("current")
_CfprExtpolRegistryFsmStatus_Type = SnmpAdminString
_CfprExtpolRegistryFsmStatus_Object = MibTableColumn
cfprExtpolRegistryFsmStatus = _CfprExtpolRegistryFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 14),
    _CfprExtpolRegistryFsmStatus_Type()
)
cfprExtpolRegistryFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStatus.setStatus("current")
_CfprExtpolRegistryFsmTry_Type = Gauge32
_CfprExtpolRegistryFsmTry_Object = MibTableColumn
cfprExtpolRegistryFsmTry = _CfprExtpolRegistryFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 15),
    _CfprExtpolRegistryFsmTry_Type()
)
cfprExtpolRegistryFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTry.setStatus("current")
_CfprExtpolRegistryGenNum_Type = Gauge32
_CfprExtpolRegistryGenNum_Object = MibTableColumn
cfprExtpolRegistryGenNum = _CfprExtpolRegistryGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 16),
    _CfprExtpolRegistryGenNum_Type()
)
cfprExtpolRegistryGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryGenNum.setStatus("current")
_CfprExtpolRegistryGuid_Type = SnmpAdminString
_CfprExtpolRegistryGuid_Object = MibTableColumn
cfprExtpolRegistryGuid = _CfprExtpolRegistryGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 17),
    _CfprExtpolRegistryGuid_Type()
)
cfprExtpolRegistryGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryGuid.setStatus("current")
_CfprExtpolRegistryHost_Type = SnmpAdminString
_CfprExtpolRegistryHost_Object = MibTableColumn
cfprExtpolRegistryHost = _CfprExtpolRegistryHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 18),
    _CfprExtpolRegistryHost_Type()
)
cfprExtpolRegistryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryHost.setStatus("current")
_CfprExtpolRegistryId_Type = Gauge32
_CfprExtpolRegistryId_Object = MibTableColumn
cfprExtpolRegistryId = _CfprExtpolRegistryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 19),
    _CfprExtpolRegistryId_Type()
)
cfprExtpolRegistryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryId.setStatus("current")
_CfprExtpolRegistryIdCount_Type = Gauge32
_CfprExtpolRegistryIdCount_Object = MibTableColumn
cfprExtpolRegistryIdCount = _CfprExtpolRegistryIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 20),
    _CfprExtpolRegistryIdCount_Type()
)
cfprExtpolRegistryIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryIdCount.setStatus("current")
_CfprExtpolRegistryInterest_Type = CfprExtpolAppCapability
_CfprExtpolRegistryInterest_Object = MibTableColumn
cfprExtpolRegistryInterest = _CfprExtpolRegistryInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 21),
    _CfprExtpolRegistryInterest_Type()
)
cfprExtpolRegistryInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryInterest.setStatus("current")
_CfprExtpolRegistryIp_Type = InetAddressIPv4
_CfprExtpolRegistryIp_Object = MibTableColumn
cfprExtpolRegistryIp = _CfprExtpolRegistryIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 22),
    _CfprExtpolRegistryIp_Type()
)
cfprExtpolRegistryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryIp.setStatus("current")
_CfprExtpolRegistryIpv6_Type = InetAddressIPv6
_CfprExtpolRegistryIpv6_Object = MibTableColumn
cfprExtpolRegistryIpv6 = _CfprExtpolRegistryIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 23),
    _CfprExtpolRegistryIpv6_Type()
)
cfprExtpolRegistryIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryIpv6.setStatus("current")
_CfprExtpolRegistryLastPollTs_Type = DateAndTime
_CfprExtpolRegistryLastPollTs_Object = MibTableColumn
cfprExtpolRegistryLastPollTs = _CfprExtpolRegistryLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 24),
    _CfprExtpolRegistryLastPollTs_Type()
)
cfprExtpolRegistryLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryLastPollTs.setStatus("current")
_CfprExtpolRegistryName_Type = SnmpAdminString
_CfprExtpolRegistryName_Object = MibTableColumn
cfprExtpolRegistryName = _CfprExtpolRegistryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 25),
    _CfprExtpolRegistryName_Type()
)
cfprExtpolRegistryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryName.setStatus("current")
_CfprExtpolRegistryOperState_Type = CfprExtpolConnectorOperState
_CfprExtpolRegistryOperState_Object = MibTableColumn
cfprExtpolRegistryOperState = _CfprExtpolRegistryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 26),
    _CfprExtpolRegistryOperState_Type()
)
cfprExtpolRegistryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryOperState.setStatus("current")
_CfprExtpolRegistryType_Type = CfprExtpolConnType
_CfprExtpolRegistryType_Object = MibTableColumn
cfprExtpolRegistryType = _CfprExtpolRegistryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 27),
    _CfprExtpolRegistryType_Type()
)
cfprExtpolRegistryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryType.setStatus("current")
_CfprExtpolRegistryVersion_Type = SnmpAdminString
_CfprExtpolRegistryVersion_Object = MibTableColumn
cfprExtpolRegistryVersion = _CfprExtpolRegistryVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 14, 1, 28),
    _CfprExtpolRegistryVersion_Type()
)
cfprExtpolRegistryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryVersion.setStatus("current")
_CfprExtpolRegistryFsmTable_Object = MibTable
cfprExtpolRegistryFsmTable = _CfprExtpolRegistryFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15)
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTable.setStatus("current")
_CfprExtpolRegistryFsmEntry_Object = MibTableRow
cfprExtpolRegistryFsmEntry = _CfprExtpolRegistryFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1)
)
cfprExtpolRegistryFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolRegistryFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmEntry.setStatus("current")
_CfprExtpolRegistryFsmInstanceId_Type = CfprManagedObjectId
_CfprExtpolRegistryFsmInstanceId_Object = MibTableColumn
cfprExtpolRegistryFsmInstanceId = _CfprExtpolRegistryFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 1),
    _CfprExtpolRegistryFsmInstanceId_Type()
)
cfprExtpolRegistryFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmInstanceId.setStatus("current")
_CfprExtpolRegistryFsmDn_Type = CfprManagedObjectDn
_CfprExtpolRegistryFsmDn_Object = MibTableColumn
cfprExtpolRegistryFsmDn = _CfprExtpolRegistryFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 2),
    _CfprExtpolRegistryFsmDn_Type()
)
cfprExtpolRegistryFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmDn.setStatus("current")
_CfprExtpolRegistryFsmRn_Type = SnmpAdminString
_CfprExtpolRegistryFsmRn_Object = MibTableColumn
cfprExtpolRegistryFsmRn = _CfprExtpolRegistryFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 3),
    _CfprExtpolRegistryFsmRn_Type()
)
cfprExtpolRegistryFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRn.setStatus("current")
_CfprExtpolRegistryFsmCompletionTime_Type = DateAndTime
_CfprExtpolRegistryFsmCompletionTime_Object = MibTableColumn
cfprExtpolRegistryFsmCompletionTime = _CfprExtpolRegistryFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 4),
    _CfprExtpolRegistryFsmCompletionTime_Type()
)
cfprExtpolRegistryFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmCompletionTime.setStatus("current")
_CfprExtpolRegistryFsmCurrentFsm_Type = CfprExtpolRegistryFsmCurrentFsm
_CfprExtpolRegistryFsmCurrentFsm_Object = MibTableColumn
cfprExtpolRegistryFsmCurrentFsm = _CfprExtpolRegistryFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 5),
    _CfprExtpolRegistryFsmCurrentFsm_Type()
)
cfprExtpolRegistryFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmCurrentFsm.setStatus("current")
_CfprExtpolRegistryFsmDescrData_Type = SnmpAdminString
_CfprExtpolRegistryFsmDescrData_Object = MibTableColumn
cfprExtpolRegistryFsmDescrData = _CfprExtpolRegistryFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 6),
    _CfprExtpolRegistryFsmDescrData_Type()
)
cfprExtpolRegistryFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmDescrData.setStatus("current")
_CfprExtpolRegistryFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprExtpolRegistryFsmFsmStatus_Object = MibTableColumn
cfprExtpolRegistryFsmFsmStatus = _CfprExtpolRegistryFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 7),
    _CfprExtpolRegistryFsmFsmStatus_Type()
)
cfprExtpolRegistryFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmFsmStatus.setStatus("current")
_CfprExtpolRegistryFsmProgress_Type = Gauge32
_CfprExtpolRegistryFsmProgress_Object = MibTableColumn
cfprExtpolRegistryFsmProgress = _CfprExtpolRegistryFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 8),
    _CfprExtpolRegistryFsmProgress_Type()
)
cfprExtpolRegistryFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmProgress.setStatus("current")
_CfprExtpolRegistryFsmRmtErrCode_Type = Gauge32
_CfprExtpolRegistryFsmRmtErrCode_Object = MibTableColumn
cfprExtpolRegistryFsmRmtErrCode = _CfprExtpolRegistryFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 9),
    _CfprExtpolRegistryFsmRmtErrCode_Type()
)
cfprExtpolRegistryFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRmtErrCode.setStatus("current")
_CfprExtpolRegistryFsmRmtErrDescr_Type = SnmpAdminString
_CfprExtpolRegistryFsmRmtErrDescr_Object = MibTableColumn
cfprExtpolRegistryFsmRmtErrDescr = _CfprExtpolRegistryFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 10),
    _CfprExtpolRegistryFsmRmtErrDescr_Type()
)
cfprExtpolRegistryFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRmtErrDescr.setStatus("current")
_CfprExtpolRegistryFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprExtpolRegistryFsmRmtRslt_Object = MibTableColumn
cfprExtpolRegistryFsmRmtRslt = _CfprExtpolRegistryFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 15, 1, 11),
    _CfprExtpolRegistryFsmRmtRslt_Type()
)
cfprExtpolRegistryFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmRmtRslt.setStatus("current")
_CfprExtpolRegistryFsmStageTable_Object = MibTable
cfprExtpolRegistryFsmStageTable = _CfprExtpolRegistryFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16)
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageTable.setStatus("current")
_CfprExtpolRegistryFsmStageEntry_Object = MibTableRow
cfprExtpolRegistryFsmStageEntry = _CfprExtpolRegistryFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1)
)
cfprExtpolRegistryFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolRegistryFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageEntry.setStatus("current")
_CfprExtpolRegistryFsmStageInstanceId_Type = CfprManagedObjectId
_CfprExtpolRegistryFsmStageInstanceId_Object = MibTableColumn
cfprExtpolRegistryFsmStageInstanceId = _CfprExtpolRegistryFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 1),
    _CfprExtpolRegistryFsmStageInstanceId_Type()
)
cfprExtpolRegistryFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageInstanceId.setStatus("current")
_CfprExtpolRegistryFsmStageDn_Type = CfprManagedObjectDn
_CfprExtpolRegistryFsmStageDn_Object = MibTableColumn
cfprExtpolRegistryFsmStageDn = _CfprExtpolRegistryFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 2),
    _CfprExtpolRegistryFsmStageDn_Type()
)
cfprExtpolRegistryFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageDn.setStatus("current")
_CfprExtpolRegistryFsmStageRn_Type = SnmpAdminString
_CfprExtpolRegistryFsmStageRn_Object = MibTableColumn
cfprExtpolRegistryFsmStageRn = _CfprExtpolRegistryFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 3),
    _CfprExtpolRegistryFsmStageRn_Type()
)
cfprExtpolRegistryFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageRn.setStatus("current")
_CfprExtpolRegistryFsmStageDescrData_Type = SnmpAdminString
_CfprExtpolRegistryFsmStageDescrData_Object = MibTableColumn
cfprExtpolRegistryFsmStageDescrData = _CfprExtpolRegistryFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 4),
    _CfprExtpolRegistryFsmStageDescrData_Type()
)
cfprExtpolRegistryFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageDescrData.setStatus("current")
_CfprExtpolRegistryFsmStageLastUpdateTime_Type = DateAndTime
_CfprExtpolRegistryFsmStageLastUpdateTime_Object = MibTableColumn
cfprExtpolRegistryFsmStageLastUpdateTime = _CfprExtpolRegistryFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 5),
    _CfprExtpolRegistryFsmStageLastUpdateTime_Type()
)
cfprExtpolRegistryFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageLastUpdateTime.setStatus("current")
_CfprExtpolRegistryFsmStageName_Type = CfprExtpolRegistryFsmStageName
_CfprExtpolRegistryFsmStageName_Object = MibTableColumn
cfprExtpolRegistryFsmStageName = _CfprExtpolRegistryFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 6),
    _CfprExtpolRegistryFsmStageName_Type()
)
cfprExtpolRegistryFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageName.setStatus("current")
_CfprExtpolRegistryFsmStageOrder_Type = Gauge32
_CfprExtpolRegistryFsmStageOrder_Object = MibTableColumn
cfprExtpolRegistryFsmStageOrder = _CfprExtpolRegistryFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 7),
    _CfprExtpolRegistryFsmStageOrder_Type()
)
cfprExtpolRegistryFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageOrder.setStatus("current")
_CfprExtpolRegistryFsmStageRetry_Type = Gauge32
_CfprExtpolRegistryFsmStageRetry_Object = MibTableColumn
cfprExtpolRegistryFsmStageRetry = _CfprExtpolRegistryFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 8),
    _CfprExtpolRegistryFsmStageRetry_Type()
)
cfprExtpolRegistryFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageRetry.setStatus("current")
_CfprExtpolRegistryFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprExtpolRegistryFsmStageStageStatus_Object = MibTableColumn
cfprExtpolRegistryFsmStageStageStatus = _CfprExtpolRegistryFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 16, 1, 9),
    _CfprExtpolRegistryFsmStageStageStatus_Type()
)
cfprExtpolRegistryFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmStageStageStatus.setStatus("current")
_CfprExtpolRegistryFsmTaskTable_Object = MibTable
cfprExtpolRegistryFsmTaskTable = _CfprExtpolRegistryFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17)
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskTable.setStatus("current")
_CfprExtpolRegistryFsmTaskEntry_Object = MibTableRow
cfprExtpolRegistryFsmTaskEntry = _CfprExtpolRegistryFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1)
)
cfprExtpolRegistryFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolRegistryFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskEntry.setStatus("current")
_CfprExtpolRegistryFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprExtpolRegistryFsmTaskInstanceId_Object = MibTableColumn
cfprExtpolRegistryFsmTaskInstanceId = _CfprExtpolRegistryFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 1),
    _CfprExtpolRegistryFsmTaskInstanceId_Type()
)
cfprExtpolRegistryFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskInstanceId.setStatus("current")
_CfprExtpolRegistryFsmTaskDn_Type = CfprManagedObjectDn
_CfprExtpolRegistryFsmTaskDn_Object = MibTableColumn
cfprExtpolRegistryFsmTaskDn = _CfprExtpolRegistryFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 2),
    _CfprExtpolRegistryFsmTaskDn_Type()
)
cfprExtpolRegistryFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskDn.setStatus("current")
_CfprExtpolRegistryFsmTaskRn_Type = SnmpAdminString
_CfprExtpolRegistryFsmTaskRn_Object = MibTableColumn
cfprExtpolRegistryFsmTaskRn = _CfprExtpolRegistryFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 3),
    _CfprExtpolRegistryFsmTaskRn_Type()
)
cfprExtpolRegistryFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskRn.setStatus("current")
_CfprExtpolRegistryFsmTaskCompletion_Type = CfprFsmCompletion
_CfprExtpolRegistryFsmTaskCompletion_Object = MibTableColumn
cfprExtpolRegistryFsmTaskCompletion = _CfprExtpolRegistryFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 4),
    _CfprExtpolRegistryFsmTaskCompletion_Type()
)
cfprExtpolRegistryFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskCompletion.setStatus("current")
_CfprExtpolRegistryFsmTaskFlags_Type = CfprFsmFlags
_CfprExtpolRegistryFsmTaskFlags_Object = MibTableColumn
cfprExtpolRegistryFsmTaskFlags = _CfprExtpolRegistryFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 5),
    _CfprExtpolRegistryFsmTaskFlags_Type()
)
cfprExtpolRegistryFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskFlags.setStatus("current")
_CfprExtpolRegistryFsmTaskItem_Type = CfprExtpolRegistryFsmTaskItem
_CfprExtpolRegistryFsmTaskItem_Object = MibTableColumn
cfprExtpolRegistryFsmTaskItem = _CfprExtpolRegistryFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 6),
    _CfprExtpolRegistryFsmTaskItem_Type()
)
cfprExtpolRegistryFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskItem.setStatus("current")
_CfprExtpolRegistryFsmTaskSeqId_Type = Gauge32
_CfprExtpolRegistryFsmTaskSeqId_Object = MibTableColumn
cfprExtpolRegistryFsmTaskSeqId = _CfprExtpolRegistryFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 17, 1, 7),
    _CfprExtpolRegistryFsmTaskSeqId_Type()
)
cfprExtpolRegistryFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolRegistryFsmTaskSeqId.setStatus("current")
_CfprExtpolSystemContextTable_Object = MibTable
cfprExtpolSystemContextTable = _CfprExtpolSystemContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18)
)
if mibBuilder.loadTexts:
    cfprExtpolSystemContextTable.setStatus("current")
_CfprExtpolSystemContextEntry_Object = MibTableRow
cfprExtpolSystemContextEntry = _CfprExtpolSystemContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1)
)
cfprExtpolSystemContextEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EXTPOL-MIB", "cfprExtpolSystemContextInstanceId"),
)
if mibBuilder.loadTexts:
    cfprExtpolSystemContextEntry.setStatus("current")
_CfprExtpolSystemContextInstanceId_Type = CfprManagedObjectId
_CfprExtpolSystemContextInstanceId_Object = MibTableColumn
cfprExtpolSystemContextInstanceId = _CfprExtpolSystemContextInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 1),
    _CfprExtpolSystemContextInstanceId_Type()
)
cfprExtpolSystemContextInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextInstanceId.setStatus("current")
_CfprExtpolSystemContextDn_Type = CfprManagedObjectDn
_CfprExtpolSystemContextDn_Object = MibTableColumn
cfprExtpolSystemContextDn = _CfprExtpolSystemContextDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 2),
    _CfprExtpolSystemContextDn_Type()
)
cfprExtpolSystemContextDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextDn.setStatus("current")
_CfprExtpolSystemContextRn_Type = SnmpAdminString
_CfprExtpolSystemContextRn_Object = MibTableColumn
cfprExtpolSystemContextRn = _CfprExtpolSystemContextRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 3),
    _CfprExtpolSystemContextRn_Type()
)
cfprExtpolSystemContextRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextRn.setStatus("current")
_CfprExtpolSystemContextCapability_Type = CfprExtpolAppCapability
_CfprExtpolSystemContextCapability_Object = MibTableColumn
cfprExtpolSystemContextCapability = _CfprExtpolSystemContextCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 4),
    _CfprExtpolSystemContextCapability_Type()
)
cfprExtpolSystemContextCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextCapability.setStatus("current")
_CfprExtpolSystemContextDescr_Type = SnmpAdminString
_CfprExtpolSystemContextDescr_Object = MibTableColumn
cfprExtpolSystemContextDescr = _CfprExtpolSystemContextDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 5),
    _CfprExtpolSystemContextDescr_Type()
)
cfprExtpolSystemContextDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextDescr.setStatus("current")
_CfprExtpolSystemContextGuid_Type = SnmpAdminString
_CfprExtpolSystemContextGuid_Object = MibTableColumn
cfprExtpolSystemContextGuid = _CfprExtpolSystemContextGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 6),
    _CfprExtpolSystemContextGuid_Type()
)
cfprExtpolSystemContextGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextGuid.setStatus("current")
_CfprExtpolSystemContextId_Type = Gauge32
_CfprExtpolSystemContextId_Object = MibTableColumn
cfprExtpolSystemContextId = _CfprExtpolSystemContextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 7),
    _CfprExtpolSystemContextId_Type()
)
cfprExtpolSystemContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextId.setStatus("current")
_CfprExtpolSystemContextInterest_Type = CfprExtpolAppCapability
_CfprExtpolSystemContextInterest_Object = MibTableColumn
cfprExtpolSystemContextInterest = _CfprExtpolSystemContextInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 8),
    _CfprExtpolSystemContextInterest_Type()
)
cfprExtpolSystemContextInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextInterest.setStatus("current")
_CfprExtpolSystemContextIp_Type = InetAddressIPv4
_CfprExtpolSystemContextIp_Object = MibTableColumn
cfprExtpolSystemContextIp = _CfprExtpolSystemContextIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 9),
    _CfprExtpolSystemContextIp_Type()
)
cfprExtpolSystemContextIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextIp.setStatus("current")
_CfprExtpolSystemContextIpv6addr_Type = InetAddressIPv6
_CfprExtpolSystemContextIpv6addr_Object = MibTableColumn
cfprExtpolSystemContextIpv6addr = _CfprExtpolSystemContextIpv6addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 10),
    _CfprExtpolSystemContextIpv6addr_Type()
)
cfprExtpolSystemContextIpv6addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextIpv6addr.setStatus("current")
_CfprExtpolSystemContextModel_Type = SnmpAdminString
_CfprExtpolSystemContextModel_Object = MibTableColumn
cfprExtpolSystemContextModel = _CfprExtpolSystemContextModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 11),
    _CfprExtpolSystemContextModel_Type()
)
cfprExtpolSystemContextModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextModel.setStatus("current")
_CfprExtpolSystemContextName_Type = SnmpAdminString
_CfprExtpolSystemContextName_Object = MibTableColumn
cfprExtpolSystemContextName = _CfprExtpolSystemContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 12),
    _CfprExtpolSystemContextName_Type()
)
cfprExtpolSystemContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextName.setStatus("current")
_CfprExtpolSystemContextOwner_Type = SnmpAdminString
_CfprExtpolSystemContextOwner_Object = MibTableColumn
cfprExtpolSystemContextOwner = _CfprExtpolSystemContextOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 13),
    _CfprExtpolSystemContextOwner_Type()
)
cfprExtpolSystemContextOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextOwner.setStatus("current")
_CfprExtpolSystemContextSite_Type = SnmpAdminString
_CfprExtpolSystemContextSite_Object = MibTableColumn
cfprExtpolSystemContextSite = _CfprExtpolSystemContextSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 14),
    _CfprExtpolSystemContextSite_Type()
)
cfprExtpolSystemContextSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextSite.setStatus("current")
_CfprExtpolSystemContextType_Type = CfprExtpolConnType
_CfprExtpolSystemContextType_Object = MibTableColumn
cfprExtpolSystemContextType = _CfprExtpolSystemContextType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 15),
    _CfprExtpolSystemContextType_Type()
)
cfprExtpolSystemContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextType.setStatus("current")
_CfprExtpolSystemContextVersion_Type = SnmpAdminString
_CfprExtpolSystemContextVersion_Object = MibTableColumn
cfprExtpolSystemContextVersion = _CfprExtpolSystemContextVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 24, 18, 1, 16),
    _CfprExtpolSystemContextVersion_Type()
)
cfprExtpolSystemContextVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprExtpolSystemContextVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-EXTPOL-MIB",
    **{"cfprExtpolObjects": cfprExtpolObjects,
       "cfprExtpolClientTable": cfprExtpolClientTable,
       "cfprExtpolClientEntry": cfprExtpolClientEntry,
       "cfprExtpolClientInstanceId": cfprExtpolClientInstanceId,
       "cfprExtpolClientDn": cfprExtpolClientDn,
       "cfprExtpolClientRn": cfprExtpolClientRn,
       "cfprExtpolClientCapability": cfprExtpolClientCapability,
       "cfprExtpolClientConnProtocol": cfprExtpolClientConnProtocol,
       "cfprExtpolClientDescr": cfprExtpolClientDescr,
       "cfprExtpolClientGracePeriodUsed": cfprExtpolClientGracePeriodUsed,
       "cfprExtpolClientGuid": cfprExtpolClientGuid,
       "cfprExtpolClientHost": cfprExtpolClientHost,
       "cfprExtpolClientId": cfprExtpolClientId,
       "cfprExtpolClientInterest": cfprExtpolClientInterest,
       "cfprExtpolClientIp": cfprExtpolClientIp,
       "cfprExtpolClientIpv6": cfprExtpolClientIpv6,
       "cfprExtpolClientLastPollTs": cfprExtpolClientLastPollTs,
       "cfprExtpolClientLicState": cfprExtpolClientLicState,
       "cfprExtpolClientName": cfprExtpolClientName,
       "cfprExtpolClientOperState": cfprExtpolClientOperState,
       "cfprExtpolClientOwner": cfprExtpolClientOwner,
       "cfprExtpolClientSite": cfprExtpolClientSite,
       "cfprExtpolClientSuspendState": cfprExtpolClientSuspendState,
       "cfprExtpolClientType": cfprExtpolClientType,
       "cfprExtpolClientVersion": cfprExtpolClientVersion,
       "cfprExtpolClientContTable": cfprExtpolClientContTable,
       "cfprExtpolClientContEntry": cfprExtpolClientContEntry,
       "cfprExtpolClientContInstanceId": cfprExtpolClientContInstanceId,
       "cfprExtpolClientContDn": cfprExtpolClientContDn,
       "cfprExtpolClientContRn": cfprExtpolClientContRn,
       "cfprExtpolClientContGenNum": cfprExtpolClientContGenNum,
       "cfprExtpolControllerTable": cfprExtpolControllerTable,
       "cfprExtpolControllerEntry": cfprExtpolControllerEntry,
       "cfprExtpolControllerInstanceId": cfprExtpolControllerInstanceId,
       "cfprExtpolControllerDn": cfprExtpolControllerDn,
       "cfprExtpolControllerRn": cfprExtpolControllerRn,
       "cfprExtpolControllerCapability": cfprExtpolControllerCapability,
       "cfprExtpolControllerConnProtocol": cfprExtpolControllerConnProtocol,
       "cfprExtpolControllerHost": cfprExtpolControllerHost,
       "cfprExtpolControllerId": cfprExtpolControllerId,
       "cfprExtpolControllerInterest": cfprExtpolControllerInterest,
       "cfprExtpolControllerIp": cfprExtpolControllerIp,
       "cfprExtpolControllerIpv6": cfprExtpolControllerIpv6,
       "cfprExtpolControllerLastPollTs": cfprExtpolControllerLastPollTs,
       "cfprExtpolControllerName": cfprExtpolControllerName,
       "cfprExtpolControllerOperState": cfprExtpolControllerOperState,
       "cfprExtpolControllerType": cfprExtpolControllerType,
       "cfprExtpolControllerVersion": cfprExtpolControllerVersion,
       "cfprExtpolControllerContTable": cfprExtpolControllerContTable,
       "cfprExtpolControllerContEntry": cfprExtpolControllerContEntry,
       "cfprExtpolControllerContInstanceId": cfprExtpolControllerContInstanceId,
       "cfprExtpolControllerContDn": cfprExtpolControllerContDn,
       "cfprExtpolControllerContRn": cfprExtpolControllerContRn,
       "cfprExtpolControllerContGenNum": cfprExtpolControllerContGenNum,
       "cfprExtpolEpTable": cfprExtpolEpTable,
       "cfprExtpolEpEntry": cfprExtpolEpEntry,
       "cfprExtpolEpInstanceId": cfprExtpolEpInstanceId,
       "cfprExtpolEpDn": cfprExtpolEpDn,
       "cfprExtpolEpRn": cfprExtpolEpRn,
       "cfprExtpolEpFsmDescr": cfprExtpolEpFsmDescr,
       "cfprExtpolEpFsmPrev": cfprExtpolEpFsmPrev,
       "cfprExtpolEpFsmProgr": cfprExtpolEpFsmProgr,
       "cfprExtpolEpFsmRmtInvErrCode": cfprExtpolEpFsmRmtInvErrCode,
       "cfprExtpolEpFsmRmtInvErrDescr": cfprExtpolEpFsmRmtInvErrDescr,
       "cfprExtpolEpFsmRmtInvRslt": cfprExtpolEpFsmRmtInvRslt,
       "cfprExtpolEpFsmStageDescr": cfprExtpolEpFsmStageDescr,
       "cfprExtpolEpFsmStamp": cfprExtpolEpFsmStamp,
       "cfprExtpolEpFsmStatus": cfprExtpolEpFsmStatus,
       "cfprExtpolEpFsmTry": cfprExtpolEpFsmTry,
       "cfprExtpolEpFsmTable": cfprExtpolEpFsmTable,
       "cfprExtpolEpFsmEntry": cfprExtpolEpFsmEntry,
       "cfprExtpolEpFsmInstanceId": cfprExtpolEpFsmInstanceId,
       "cfprExtpolEpFsmDn": cfprExtpolEpFsmDn,
       "cfprExtpolEpFsmRn": cfprExtpolEpFsmRn,
       "cfprExtpolEpFsmCompletionTime": cfprExtpolEpFsmCompletionTime,
       "cfprExtpolEpFsmCurrentFsm": cfprExtpolEpFsmCurrentFsm,
       "cfprExtpolEpFsmDescrData": cfprExtpolEpFsmDescrData,
       "cfprExtpolEpFsmFsmStatus": cfprExtpolEpFsmFsmStatus,
       "cfprExtpolEpFsmProgress": cfprExtpolEpFsmProgress,
       "cfprExtpolEpFsmRmtErrCode": cfprExtpolEpFsmRmtErrCode,
       "cfprExtpolEpFsmRmtErrDescr": cfprExtpolEpFsmRmtErrDescr,
       "cfprExtpolEpFsmRmtRslt": cfprExtpolEpFsmRmtRslt,
       "cfprExtpolEpFsmStageTable": cfprExtpolEpFsmStageTable,
       "cfprExtpolEpFsmStageEntry": cfprExtpolEpFsmStageEntry,
       "cfprExtpolEpFsmStageInstanceId": cfprExtpolEpFsmStageInstanceId,
       "cfprExtpolEpFsmStageDn": cfprExtpolEpFsmStageDn,
       "cfprExtpolEpFsmStageRn": cfprExtpolEpFsmStageRn,
       "cfprExtpolEpFsmStageDescrData": cfprExtpolEpFsmStageDescrData,
       "cfprExtpolEpFsmStageLastUpdateTime": cfprExtpolEpFsmStageLastUpdateTime,
       "cfprExtpolEpFsmStageName": cfprExtpolEpFsmStageName,
       "cfprExtpolEpFsmStageOrder": cfprExtpolEpFsmStageOrder,
       "cfprExtpolEpFsmStageRetry": cfprExtpolEpFsmStageRetry,
       "cfprExtpolEpFsmStageStageStatus": cfprExtpolEpFsmStageStageStatus,
       "cfprExtpolEpFsmTaskTable": cfprExtpolEpFsmTaskTable,
       "cfprExtpolEpFsmTaskEntry": cfprExtpolEpFsmTaskEntry,
       "cfprExtpolEpFsmTaskInstanceId": cfprExtpolEpFsmTaskInstanceId,
       "cfprExtpolEpFsmTaskDn": cfprExtpolEpFsmTaskDn,
       "cfprExtpolEpFsmTaskRn": cfprExtpolEpFsmTaskRn,
       "cfprExtpolEpFsmTaskCompletion": cfprExtpolEpFsmTaskCompletion,
       "cfprExtpolEpFsmTaskFlags": cfprExtpolEpFsmTaskFlags,
       "cfprExtpolEpFsmTaskItem": cfprExtpolEpFsmTaskItem,
       "cfprExtpolEpFsmTaskSeqId": cfprExtpolEpFsmTaskSeqId,
       "cfprExtpolProviderTable": cfprExtpolProviderTable,
       "cfprExtpolProviderEntry": cfprExtpolProviderEntry,
       "cfprExtpolProviderInstanceId": cfprExtpolProviderInstanceId,
       "cfprExtpolProviderDn": cfprExtpolProviderDn,
       "cfprExtpolProviderRn": cfprExtpolProviderRn,
       "cfprExtpolProviderCapability": cfprExtpolProviderCapability,
       "cfprExtpolProviderConnProtocol": cfprExtpolProviderConnProtocol,
       "cfprExtpolProviderFsmDescr": cfprExtpolProviderFsmDescr,
       "cfprExtpolProviderFsmPrev": cfprExtpolProviderFsmPrev,
       "cfprExtpolProviderFsmProgr": cfprExtpolProviderFsmProgr,
       "cfprExtpolProviderFsmRmtInvErrCode": cfprExtpolProviderFsmRmtInvErrCode,
       "cfprExtpolProviderFsmRmtInvErrDescr": cfprExtpolProviderFsmRmtInvErrDescr,
       "cfprExtpolProviderFsmRmtInvRslt": cfprExtpolProviderFsmRmtInvRslt,
       "cfprExtpolProviderFsmStageDescr": cfprExtpolProviderFsmStageDescr,
       "cfprExtpolProviderFsmStamp": cfprExtpolProviderFsmStamp,
       "cfprExtpolProviderFsmStatus": cfprExtpolProviderFsmStatus,
       "cfprExtpolProviderFsmTry": cfprExtpolProviderFsmTry,
       "cfprExtpolProviderHost": cfprExtpolProviderHost,
       "cfprExtpolProviderId": cfprExtpolProviderId,
       "cfprExtpolProviderInterest": cfprExtpolProviderInterest,
       "cfprExtpolProviderIp": cfprExtpolProviderIp,
       "cfprExtpolProviderIpv6": cfprExtpolProviderIpv6,
       "cfprExtpolProviderLastPollTs": cfprExtpolProviderLastPollTs,
       "cfprExtpolProviderName": cfprExtpolProviderName,
       "cfprExtpolProviderOperState": cfprExtpolProviderOperState,
       "cfprExtpolProviderType": cfprExtpolProviderType,
       "cfprExtpolProviderVersion": cfprExtpolProviderVersion,
       "cfprExtpolProviderContTable": cfprExtpolProviderContTable,
       "cfprExtpolProviderContEntry": cfprExtpolProviderContEntry,
       "cfprExtpolProviderContInstanceId": cfprExtpolProviderContInstanceId,
       "cfprExtpolProviderContDn": cfprExtpolProviderContDn,
       "cfprExtpolProviderContRn": cfprExtpolProviderContRn,
       "cfprExtpolProviderContGenNum": cfprExtpolProviderContGenNum,
       "cfprExtpolProviderFsmTable": cfprExtpolProviderFsmTable,
       "cfprExtpolProviderFsmEntry": cfprExtpolProviderFsmEntry,
       "cfprExtpolProviderFsmInstanceId": cfprExtpolProviderFsmInstanceId,
       "cfprExtpolProviderFsmDn": cfprExtpolProviderFsmDn,
       "cfprExtpolProviderFsmRn": cfprExtpolProviderFsmRn,
       "cfprExtpolProviderFsmCompletionTime": cfprExtpolProviderFsmCompletionTime,
       "cfprExtpolProviderFsmCurrentFsm": cfprExtpolProviderFsmCurrentFsm,
       "cfprExtpolProviderFsmDescrData": cfprExtpolProviderFsmDescrData,
       "cfprExtpolProviderFsmFsmStatus": cfprExtpolProviderFsmFsmStatus,
       "cfprExtpolProviderFsmProgress": cfprExtpolProviderFsmProgress,
       "cfprExtpolProviderFsmRmtErrCode": cfprExtpolProviderFsmRmtErrCode,
       "cfprExtpolProviderFsmRmtErrDescr": cfprExtpolProviderFsmRmtErrDescr,
       "cfprExtpolProviderFsmRmtRslt": cfprExtpolProviderFsmRmtRslt,
       "cfprExtpolProviderFsmStageTable": cfprExtpolProviderFsmStageTable,
       "cfprExtpolProviderFsmStageEntry": cfprExtpolProviderFsmStageEntry,
       "cfprExtpolProviderFsmStageInstanceId": cfprExtpolProviderFsmStageInstanceId,
       "cfprExtpolProviderFsmStageDn": cfprExtpolProviderFsmStageDn,
       "cfprExtpolProviderFsmStageRn": cfprExtpolProviderFsmStageRn,
       "cfprExtpolProviderFsmStageDescrData": cfprExtpolProviderFsmStageDescrData,
       "cfprExtpolProviderFsmStageLastUpdateTime": cfprExtpolProviderFsmStageLastUpdateTime,
       "cfprExtpolProviderFsmStageName": cfprExtpolProviderFsmStageName,
       "cfprExtpolProviderFsmStageOrder": cfprExtpolProviderFsmStageOrder,
       "cfprExtpolProviderFsmStageRetry": cfprExtpolProviderFsmStageRetry,
       "cfprExtpolProviderFsmStageStageStatus": cfprExtpolProviderFsmStageStageStatus,
       "cfprExtpolProviderFsmTaskTable": cfprExtpolProviderFsmTaskTable,
       "cfprExtpolProviderFsmTaskEntry": cfprExtpolProviderFsmTaskEntry,
       "cfprExtpolProviderFsmTaskInstanceId": cfprExtpolProviderFsmTaskInstanceId,
       "cfprExtpolProviderFsmTaskDn": cfprExtpolProviderFsmTaskDn,
       "cfprExtpolProviderFsmTaskRn": cfprExtpolProviderFsmTaskRn,
       "cfprExtpolProviderFsmTaskCompletion": cfprExtpolProviderFsmTaskCompletion,
       "cfprExtpolProviderFsmTaskFlags": cfprExtpolProviderFsmTaskFlags,
       "cfprExtpolProviderFsmTaskItem": cfprExtpolProviderFsmTaskItem,
       "cfprExtpolProviderFsmTaskSeqId": cfprExtpolProviderFsmTaskSeqId,
       "cfprExtpolRegistryTable": cfprExtpolRegistryTable,
       "cfprExtpolRegistryEntry": cfprExtpolRegistryEntry,
       "cfprExtpolRegistryInstanceId": cfprExtpolRegistryInstanceId,
       "cfprExtpolRegistryDn": cfprExtpolRegistryDn,
       "cfprExtpolRegistryRn": cfprExtpolRegistryRn,
       "cfprExtpolRegistryCapability": cfprExtpolRegistryCapability,
       "cfprExtpolRegistryConnProtocol": cfprExtpolRegistryConnProtocol,
       "cfprExtpolRegistryFsmDescr": cfprExtpolRegistryFsmDescr,
       "cfprExtpolRegistryFsmPrev": cfprExtpolRegistryFsmPrev,
       "cfprExtpolRegistryFsmProgr": cfprExtpolRegistryFsmProgr,
       "cfprExtpolRegistryFsmRmtInvErrCode": cfprExtpolRegistryFsmRmtInvErrCode,
       "cfprExtpolRegistryFsmRmtInvErrDescr": cfprExtpolRegistryFsmRmtInvErrDescr,
       "cfprExtpolRegistryFsmRmtInvRslt": cfprExtpolRegistryFsmRmtInvRslt,
       "cfprExtpolRegistryFsmStageDescr": cfprExtpolRegistryFsmStageDescr,
       "cfprExtpolRegistryFsmStamp": cfprExtpolRegistryFsmStamp,
       "cfprExtpolRegistryFsmStatus": cfprExtpolRegistryFsmStatus,
       "cfprExtpolRegistryFsmTry": cfprExtpolRegistryFsmTry,
       "cfprExtpolRegistryGenNum": cfprExtpolRegistryGenNum,
       "cfprExtpolRegistryGuid": cfprExtpolRegistryGuid,
       "cfprExtpolRegistryHost": cfprExtpolRegistryHost,
       "cfprExtpolRegistryId": cfprExtpolRegistryId,
       "cfprExtpolRegistryIdCount": cfprExtpolRegistryIdCount,
       "cfprExtpolRegistryInterest": cfprExtpolRegistryInterest,
       "cfprExtpolRegistryIp": cfprExtpolRegistryIp,
       "cfprExtpolRegistryIpv6": cfprExtpolRegistryIpv6,
       "cfprExtpolRegistryLastPollTs": cfprExtpolRegistryLastPollTs,
       "cfprExtpolRegistryName": cfprExtpolRegistryName,
       "cfprExtpolRegistryOperState": cfprExtpolRegistryOperState,
       "cfprExtpolRegistryType": cfprExtpolRegistryType,
       "cfprExtpolRegistryVersion": cfprExtpolRegistryVersion,
       "cfprExtpolRegistryFsmTable": cfprExtpolRegistryFsmTable,
       "cfprExtpolRegistryFsmEntry": cfprExtpolRegistryFsmEntry,
       "cfprExtpolRegistryFsmInstanceId": cfprExtpolRegistryFsmInstanceId,
       "cfprExtpolRegistryFsmDn": cfprExtpolRegistryFsmDn,
       "cfprExtpolRegistryFsmRn": cfprExtpolRegistryFsmRn,
       "cfprExtpolRegistryFsmCompletionTime": cfprExtpolRegistryFsmCompletionTime,
       "cfprExtpolRegistryFsmCurrentFsm": cfprExtpolRegistryFsmCurrentFsm,
       "cfprExtpolRegistryFsmDescrData": cfprExtpolRegistryFsmDescrData,
       "cfprExtpolRegistryFsmFsmStatus": cfprExtpolRegistryFsmFsmStatus,
       "cfprExtpolRegistryFsmProgress": cfprExtpolRegistryFsmProgress,
       "cfprExtpolRegistryFsmRmtErrCode": cfprExtpolRegistryFsmRmtErrCode,
       "cfprExtpolRegistryFsmRmtErrDescr": cfprExtpolRegistryFsmRmtErrDescr,
       "cfprExtpolRegistryFsmRmtRslt": cfprExtpolRegistryFsmRmtRslt,
       "cfprExtpolRegistryFsmStageTable": cfprExtpolRegistryFsmStageTable,
       "cfprExtpolRegistryFsmStageEntry": cfprExtpolRegistryFsmStageEntry,
       "cfprExtpolRegistryFsmStageInstanceId": cfprExtpolRegistryFsmStageInstanceId,
       "cfprExtpolRegistryFsmStageDn": cfprExtpolRegistryFsmStageDn,
       "cfprExtpolRegistryFsmStageRn": cfprExtpolRegistryFsmStageRn,
       "cfprExtpolRegistryFsmStageDescrData": cfprExtpolRegistryFsmStageDescrData,
       "cfprExtpolRegistryFsmStageLastUpdateTime": cfprExtpolRegistryFsmStageLastUpdateTime,
       "cfprExtpolRegistryFsmStageName": cfprExtpolRegistryFsmStageName,
       "cfprExtpolRegistryFsmStageOrder": cfprExtpolRegistryFsmStageOrder,
       "cfprExtpolRegistryFsmStageRetry": cfprExtpolRegistryFsmStageRetry,
       "cfprExtpolRegistryFsmStageStageStatus": cfprExtpolRegistryFsmStageStageStatus,
       "cfprExtpolRegistryFsmTaskTable": cfprExtpolRegistryFsmTaskTable,
       "cfprExtpolRegistryFsmTaskEntry": cfprExtpolRegistryFsmTaskEntry,
       "cfprExtpolRegistryFsmTaskInstanceId": cfprExtpolRegistryFsmTaskInstanceId,
       "cfprExtpolRegistryFsmTaskDn": cfprExtpolRegistryFsmTaskDn,
       "cfprExtpolRegistryFsmTaskRn": cfprExtpolRegistryFsmTaskRn,
       "cfprExtpolRegistryFsmTaskCompletion": cfprExtpolRegistryFsmTaskCompletion,
       "cfprExtpolRegistryFsmTaskFlags": cfprExtpolRegistryFsmTaskFlags,
       "cfprExtpolRegistryFsmTaskItem": cfprExtpolRegistryFsmTaskItem,
       "cfprExtpolRegistryFsmTaskSeqId": cfprExtpolRegistryFsmTaskSeqId,
       "cfprExtpolSystemContextTable": cfprExtpolSystemContextTable,
       "cfprExtpolSystemContextEntry": cfprExtpolSystemContextEntry,
       "cfprExtpolSystemContextInstanceId": cfprExtpolSystemContextInstanceId,
       "cfprExtpolSystemContextDn": cfprExtpolSystemContextDn,
       "cfprExtpolSystemContextRn": cfprExtpolSystemContextRn,
       "cfprExtpolSystemContextCapability": cfprExtpolSystemContextCapability,
       "cfprExtpolSystemContextDescr": cfprExtpolSystemContextDescr,
       "cfprExtpolSystemContextGuid": cfprExtpolSystemContextGuid,
       "cfprExtpolSystemContextId": cfprExtpolSystemContextId,
       "cfprExtpolSystemContextInterest": cfprExtpolSystemContextInterest,
       "cfprExtpolSystemContextIp": cfprExtpolSystemContextIp,
       "cfprExtpolSystemContextIpv6addr": cfprExtpolSystemContextIpv6addr,
       "cfprExtpolSystemContextModel": cfprExtpolSystemContextModel,
       "cfprExtpolSystemContextName": cfprExtpolSystemContextName,
       "cfprExtpolSystemContextOwner": cfprExtpolSystemContextOwner,
       "cfprExtpolSystemContextSite": cfprExtpolSystemContextSite,
       "cfprExtpolSystemContextType": cfprExtpolSystemContextType,
       "cfprExtpolSystemContextVersion": cfprExtpolSystemContextVersion}
)
