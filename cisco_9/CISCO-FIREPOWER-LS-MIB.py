# SNMP MIB module (CISCO-FIREPOWER-LS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-LS-MIB.mib
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
 CfprFabricVConMappingScheme,
 CfprFabricVConTransportPref,
 CfprFsmCompletion,
 CfprFsmFsmStageStatus,
 CfprLsAgentCapability,
 CfprLsAgentMode,
 CfprLsApply,
 CfprLsAssignment,
 CfprLsAssocState,
 CfprLsComputeBindingOperState,
 CfprLsConfigIssues,
 CfprLsConfigState,
 CfprLsConfigWarnings,
 CfprLsFcZoneGroupSwitchId,
 CfprLsFcZoneState,
 CfprLsOperState,
 CfprLsOwner,
 CfprLsPowerState,
 CfprLsResolveFromRemoteServer,
 CfprLsServerFsmCurrentFsm,
 CfprLsServerFsmStageName,
 CfprLsServerFsmTaskFlags,
 CfprLsServerFsmTaskItem,
 CfprLsType,
 CfprNetworkConfigIssues,
 CfprNetworkSwitchId,
 CfprPolicyPolicyOwner,
 CfprServerConfigIssues,
 CfprSmDeployType,
 CfprStorageConfigIssues,
 CfprStorageFcZoningType,
 CfprVnicConfigIssues,
 CfprVnicExternalMgmtIPMode,
 CfprVnicIScsiConfigIssues,
 CfprVnicMezzMappingScheme,
 CfprVnicOrderScheme,
 CfprVnicPlacement) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFabricVConMappingScheme",
    "CfprFabricVConTransportPref",
    "CfprFsmCompletion",
    "CfprFsmFsmStageStatus",
    "CfprLsAgentCapability",
    "CfprLsAgentMode",
    "CfprLsApply",
    "CfprLsAssignment",
    "CfprLsAssocState",
    "CfprLsComputeBindingOperState",
    "CfprLsConfigIssues",
    "CfprLsConfigState",
    "CfprLsConfigWarnings",
    "CfprLsFcZoneGroupSwitchId",
    "CfprLsFcZoneState",
    "CfprLsOperState",
    "CfprLsOwner",
    "CfprLsPowerState",
    "CfprLsResolveFromRemoteServer",
    "CfprLsServerFsmCurrentFsm",
    "CfprLsServerFsmStageName",
    "CfprLsServerFsmTaskFlags",
    "CfprLsServerFsmTaskItem",
    "CfprLsType",
    "CfprNetworkConfigIssues",
    "CfprNetworkSwitchId",
    "CfprPolicyPolicyOwner",
    "CfprServerConfigIssues",
    "CfprSmDeployType",
    "CfprStorageConfigIssues",
    "CfprStorageFcZoningType",
    "CfprVnicConfigIssues",
    "CfprVnicExternalMgmtIPMode",
    "CfprVnicIScsiConfigIssues",
    "CfprVnicMezzMappingScheme",
    "CfprVnicOrderScheme",
    "CfprVnicPlacement")

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

cfprLsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprLsAgentPolicyTable_Object = MibTable
cfprLsAgentPolicyTable = _CfprLsAgentPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1)
)
if mibBuilder.loadTexts:
    cfprLsAgentPolicyTable.setStatus("current")
_CfprLsAgentPolicyEntry_Object = MibTableRow
cfprLsAgentPolicyEntry = _CfprLsAgentPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1)
)
cfprLsAgentPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsAgentPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsAgentPolicyEntry.setStatus("current")
_CfprLsAgentPolicyInstanceId_Type = CfprManagedObjectId
_CfprLsAgentPolicyInstanceId_Object = MibTableColumn
cfprLsAgentPolicyInstanceId = _CfprLsAgentPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 1),
    _CfprLsAgentPolicyInstanceId_Type()
)
cfprLsAgentPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyInstanceId.setStatus("current")
_CfprLsAgentPolicyDn_Type = CfprManagedObjectDn
_CfprLsAgentPolicyDn_Object = MibTableColumn
cfprLsAgentPolicyDn = _CfprLsAgentPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 2),
    _CfprLsAgentPolicyDn_Type()
)
cfprLsAgentPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyDn.setStatus("current")
_CfprLsAgentPolicyRn_Type = SnmpAdminString
_CfprLsAgentPolicyRn_Object = MibTableColumn
cfprLsAgentPolicyRn = _CfprLsAgentPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 3),
    _CfprLsAgentPolicyRn_Type()
)
cfprLsAgentPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyRn.setStatus("current")
_CfprLsAgentPolicyCapability_Type = CfprLsAgentCapability
_CfprLsAgentPolicyCapability_Object = MibTableColumn
cfprLsAgentPolicyCapability = _CfprLsAgentPolicyCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 4),
    _CfprLsAgentPolicyCapability_Type()
)
cfprLsAgentPolicyCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyCapability.setStatus("current")
_CfprLsAgentPolicyDescr_Type = SnmpAdminString
_CfprLsAgentPolicyDescr_Object = MibTableColumn
cfprLsAgentPolicyDescr = _CfprLsAgentPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 5),
    _CfprLsAgentPolicyDescr_Type()
)
cfprLsAgentPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyDescr.setStatus("current")
_CfprLsAgentPolicyIntId_Type = SnmpAdminString
_CfprLsAgentPolicyIntId_Object = MibTableColumn
cfprLsAgentPolicyIntId = _CfprLsAgentPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 6),
    _CfprLsAgentPolicyIntId_Type()
)
cfprLsAgentPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyIntId.setStatus("current")
_CfprLsAgentPolicyMode_Type = CfprLsAgentMode
_CfprLsAgentPolicyMode_Object = MibTableColumn
cfprLsAgentPolicyMode = _CfprLsAgentPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 7),
    _CfprLsAgentPolicyMode_Type()
)
cfprLsAgentPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyMode.setStatus("current")
_CfprLsAgentPolicyName_Type = SnmpAdminString
_CfprLsAgentPolicyName_Object = MibTableColumn
cfprLsAgentPolicyName = _CfprLsAgentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 8),
    _CfprLsAgentPolicyName_Type()
)
cfprLsAgentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyName.setStatus("current")
_CfprLsAgentPolicyPolicyLevel_Type = Gauge32
_CfprLsAgentPolicyPolicyLevel_Object = MibTableColumn
cfprLsAgentPolicyPolicyLevel = _CfprLsAgentPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 9),
    _CfprLsAgentPolicyPolicyLevel_Type()
)
cfprLsAgentPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyPolicyLevel.setStatus("current")
_CfprLsAgentPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsAgentPolicyPolicyOwner_Object = MibTableColumn
cfprLsAgentPolicyPolicyOwner = _CfprLsAgentPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 1, 1, 10),
    _CfprLsAgentPolicyPolicyOwner_Type()
)
cfprLsAgentPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsAgentPolicyPolicyOwner.setStatus("current")
_CfprLsBindingTable_Object = MibTable
cfprLsBindingTable = _CfprLsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2)
)
if mibBuilder.loadTexts:
    cfprLsBindingTable.setStatus("current")
_CfprLsBindingEntry_Object = MibTableRow
cfprLsBindingEntry = _CfprLsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1)
)
cfprLsBindingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsBindingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsBindingEntry.setStatus("current")
_CfprLsBindingInstanceId_Type = CfprManagedObjectId
_CfprLsBindingInstanceId_Object = MibTableColumn
cfprLsBindingInstanceId = _CfprLsBindingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 1),
    _CfprLsBindingInstanceId_Type()
)
cfprLsBindingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsBindingInstanceId.setStatus("current")
_CfprLsBindingDn_Type = CfprManagedObjectDn
_CfprLsBindingDn_Object = MibTableColumn
cfprLsBindingDn = _CfprLsBindingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 2),
    _CfprLsBindingDn_Type()
)
cfprLsBindingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingDn.setStatus("current")
_CfprLsBindingRn_Type = SnmpAdminString
_CfprLsBindingRn_Object = MibTableColumn
cfprLsBindingRn = _CfprLsBindingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 3),
    _CfprLsBindingRn_Type()
)
cfprLsBindingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingRn.setStatus("current")
_CfprLsBindingAssignedToDn_Type = SnmpAdminString
_CfprLsBindingAssignedToDn_Object = MibTableColumn
cfprLsBindingAssignedToDn = _CfprLsBindingAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 4),
    _CfprLsBindingAssignedToDn_Type()
)
cfprLsBindingAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingAssignedToDn.setStatus("current")
_CfprLsBindingComputeEpDn_Type = SnmpAdminString
_CfprLsBindingComputeEpDn_Object = MibTableColumn
cfprLsBindingComputeEpDn = _CfprLsBindingComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 5),
    _CfprLsBindingComputeEpDn_Type()
)
cfprLsBindingComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingComputeEpDn.setStatus("current")
_CfprLsBindingIssues_Type = CfprLsConfigIssues
_CfprLsBindingIssues_Object = MibTableColumn
cfprLsBindingIssues = _CfprLsBindingIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 6),
    _CfprLsBindingIssues_Type()
)
cfprLsBindingIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingIssues.setStatus("current")
_CfprLsBindingName_Type = SnmpAdminString
_CfprLsBindingName_Object = MibTableColumn
cfprLsBindingName = _CfprLsBindingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 7),
    _CfprLsBindingName_Type()
)
cfprLsBindingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingName.setStatus("current")
_CfprLsBindingOperState_Type = CfprLsComputeBindingOperState
_CfprLsBindingOperState_Object = MibTableColumn
cfprLsBindingOperState = _CfprLsBindingOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 8),
    _CfprLsBindingOperState_Type()
)
cfprLsBindingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingOperState.setStatus("current")
_CfprLsBindingPnDn_Type = SnmpAdminString
_CfprLsBindingPnDn_Object = MibTableColumn
cfprLsBindingPnDn = _CfprLsBindingPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 9),
    _CfprLsBindingPnDn_Type()
)
cfprLsBindingPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingPnDn.setStatus("current")
_CfprLsBindingRestrictMigration_Type = TruthValue
_CfprLsBindingRestrictMigration_Object = MibTableColumn
cfprLsBindingRestrictMigration = _CfprLsBindingRestrictMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 2, 1, 10),
    _CfprLsBindingRestrictMigration_Type()
)
cfprLsBindingRestrictMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsBindingRestrictMigration.setStatus("current")
_CfprLsFcLocaleTable_Object = MibTable
cfprLsFcLocaleTable = _CfprLsFcLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 3)
)
if mibBuilder.loadTexts:
    cfprLsFcLocaleTable.setStatus("current")
_CfprLsFcLocaleEntry_Object = MibTableRow
cfprLsFcLocaleEntry = _CfprLsFcLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 3, 1)
)
cfprLsFcLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsFcLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsFcLocaleEntry.setStatus("current")
_CfprLsFcLocaleInstanceId_Type = CfprManagedObjectId
_CfprLsFcLocaleInstanceId_Object = MibTableColumn
cfprLsFcLocaleInstanceId = _CfprLsFcLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 3, 1, 1),
    _CfprLsFcLocaleInstanceId_Type()
)
cfprLsFcLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsFcLocaleInstanceId.setStatus("current")
_CfprLsFcLocaleDn_Type = CfprManagedObjectDn
_CfprLsFcLocaleDn_Object = MibTableColumn
cfprLsFcLocaleDn = _CfprLsFcLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 3, 1, 2),
    _CfprLsFcLocaleDn_Type()
)
cfprLsFcLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcLocaleDn.setStatus("current")
_CfprLsFcLocaleRn_Type = SnmpAdminString
_CfprLsFcLocaleRn_Object = MibTableColumn
cfprLsFcLocaleRn = _CfprLsFcLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 3, 1, 3),
    _CfprLsFcLocaleRn_Type()
)
cfprLsFcLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcLocaleRn.setStatus("current")
_CfprLsFcLocaleSwitchId_Type = CfprNetworkSwitchId
_CfprLsFcLocaleSwitchId_Object = MibTableColumn
cfprLsFcLocaleSwitchId = _CfprLsFcLocaleSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 3, 1, 4),
    _CfprLsFcLocaleSwitchId_Type()
)
cfprLsFcLocaleSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcLocaleSwitchId.setStatus("current")
_CfprLsFcZoneTable_Object = MibTable
cfprLsFcZoneTable = _CfprLsFcZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4)
)
if mibBuilder.loadTexts:
    cfprLsFcZoneTable.setStatus("current")
_CfprLsFcZoneEntry_Object = MibTableRow
cfprLsFcZoneEntry = _CfprLsFcZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1)
)
cfprLsFcZoneEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsFcZoneInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsFcZoneEntry.setStatus("current")
_CfprLsFcZoneInstanceId_Type = CfprManagedObjectId
_CfprLsFcZoneInstanceId_Object = MibTableColumn
cfprLsFcZoneInstanceId = _CfprLsFcZoneInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 1),
    _CfprLsFcZoneInstanceId_Type()
)
cfprLsFcZoneInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsFcZoneInstanceId.setStatus("current")
_CfprLsFcZoneDn_Type = CfprManagedObjectDn
_CfprLsFcZoneDn_Object = MibTableColumn
cfprLsFcZoneDn = _CfprLsFcZoneDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 2),
    _CfprLsFcZoneDn_Type()
)
cfprLsFcZoneDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneDn.setStatus("current")
_CfprLsFcZoneRn_Type = SnmpAdminString
_CfprLsFcZoneRn_Object = MibTableColumn
cfprLsFcZoneRn = _CfprLsFcZoneRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 3),
    _CfprLsFcZoneRn_Type()
)
cfprLsFcZoneRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneRn.setStatus("current")
_CfprLsFcZoneAdminState_Type = CfprLsFcZoneState
_CfprLsFcZoneAdminState_Object = MibTableColumn
cfprLsFcZoneAdminState = _CfprLsFcZoneAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 4),
    _CfprLsFcZoneAdminState_Type()
)
cfprLsFcZoneAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneAdminState.setStatus("current")
_CfprLsFcZoneId_Type = Gauge32
_CfprLsFcZoneId_Object = MibTableColumn
cfprLsFcZoneId = _CfprLsFcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 5),
    _CfprLsFcZoneId_Type()
)
cfprLsFcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneId.setStatus("current")
_CfprLsFcZoneIdentity_Type = SnmpAdminString
_CfprLsFcZoneIdentity_Object = MibTableColumn
cfprLsFcZoneIdentity = _CfprLsFcZoneIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 6),
    _CfprLsFcZoneIdentity_Type()
)
cfprLsFcZoneIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneIdentity.setStatus("current")
_CfprLsFcZoneIniName_Type = SnmpAdminString
_CfprLsFcZoneIniName_Object = MibTableColumn
cfprLsFcZoneIniName = _CfprLsFcZoneIniName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 7),
    _CfprLsFcZoneIniName_Type()
)
cfprLsFcZoneIniName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneIniName.setStatus("current")
_CfprLsFcZoneName_Type = SnmpAdminString
_CfprLsFcZoneName_Object = MibTableColumn
cfprLsFcZoneName = _CfprLsFcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 8),
    _CfprLsFcZoneName_Type()
)
cfprLsFcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneName.setStatus("current")
_CfprLsFcZoneOperState_Type = CfprLsFcZoneState
_CfprLsFcZoneOperState_Object = MibTableColumn
cfprLsFcZoneOperState = _CfprLsFcZoneOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 9),
    _CfprLsFcZoneOperState_Type()
)
cfprLsFcZoneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneOperState.setStatus("current")
_CfprLsFcZonePeerDn_Type = SnmpAdminString
_CfprLsFcZonePeerDn_Object = MibTableColumn
cfprLsFcZonePeerDn = _CfprLsFcZonePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 10),
    _CfprLsFcZonePeerDn_Type()
)
cfprLsFcZonePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZonePeerDn.setStatus("current")
_CfprLsFcZoneSwitchId_Type = CfprNetworkSwitchId
_CfprLsFcZoneSwitchId_Object = MibTableColumn
cfprLsFcZoneSwitchId = _CfprLsFcZoneSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 11),
    _CfprLsFcZoneSwitchId_Type()
)
cfprLsFcZoneSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneSwitchId.setStatus("current")
_CfprLsFcZoneUsrLbl_Type = SnmpAdminString
_CfprLsFcZoneUsrLbl_Object = MibTableColumn
cfprLsFcZoneUsrLbl = _CfprLsFcZoneUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 12),
    _CfprLsFcZoneUsrLbl_Type()
)
cfprLsFcZoneUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneUsrLbl.setStatus("current")
_CfprLsFcZoneVnetId_Type = Gauge32
_CfprLsFcZoneVnetId_Object = MibTableColumn
cfprLsFcZoneVnetId = _CfprLsFcZoneVnetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 13),
    _CfprLsFcZoneVnetId_Type()
)
cfprLsFcZoneVnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneVnetId.setStatus("current")
_CfprLsFcZoneZoningType_Type = CfprStorageFcZoningType
_CfprLsFcZoneZoningType_Object = MibTableColumn
cfprLsFcZoneZoningType = _CfprLsFcZoneZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 4, 1, 14),
    _CfprLsFcZoneZoningType_Type()
)
cfprLsFcZoneZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneZoningType.setStatus("current")
_CfprLsFcZoneGroupTable_Object = MibTable
cfprLsFcZoneGroupTable = _CfprLsFcZoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5)
)
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupTable.setStatus("current")
_CfprLsFcZoneGroupEntry_Object = MibTableRow
cfprLsFcZoneGroupEntry = _CfprLsFcZoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1)
)
cfprLsFcZoneGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsFcZoneGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupEntry.setStatus("current")
_CfprLsFcZoneGroupInstanceId_Type = CfprManagedObjectId
_CfprLsFcZoneGroupInstanceId_Object = MibTableColumn
cfprLsFcZoneGroupInstanceId = _CfprLsFcZoneGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1, 1),
    _CfprLsFcZoneGroupInstanceId_Type()
)
cfprLsFcZoneGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupInstanceId.setStatus("current")
_CfprLsFcZoneGroupDn_Type = CfprManagedObjectDn
_CfprLsFcZoneGroupDn_Object = MibTableColumn
cfprLsFcZoneGroupDn = _CfprLsFcZoneGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1, 2),
    _CfprLsFcZoneGroupDn_Type()
)
cfprLsFcZoneGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupDn.setStatus("current")
_CfprLsFcZoneGroupRn_Type = SnmpAdminString
_CfprLsFcZoneGroupRn_Object = MibTableColumn
cfprLsFcZoneGroupRn = _CfprLsFcZoneGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1, 3),
    _CfprLsFcZoneGroupRn_Type()
)
cfprLsFcZoneGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupRn.setStatus("current")
_CfprLsFcZoneGroupId_Type = Gauge32
_CfprLsFcZoneGroupId_Object = MibTableColumn
cfprLsFcZoneGroupId = _CfprLsFcZoneGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1, 4),
    _CfprLsFcZoneGroupId_Type()
)
cfprLsFcZoneGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupId.setStatus("current")
_CfprLsFcZoneGroupName_Type = SnmpAdminString
_CfprLsFcZoneGroupName_Object = MibTableColumn
cfprLsFcZoneGroupName = _CfprLsFcZoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1, 5),
    _CfprLsFcZoneGroupName_Type()
)
cfprLsFcZoneGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupName.setStatus("current")
_CfprLsFcZoneGroupSwitchId_Type = CfprLsFcZoneGroupSwitchId
_CfprLsFcZoneGroupSwitchId_Object = MibTableColumn
cfprLsFcZoneGroupSwitchId = _CfprLsFcZoneGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 5, 1, 6),
    _CfprLsFcZoneGroupSwitchId_Type()
)
cfprLsFcZoneGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsFcZoneGroupSwitchId.setStatus("current")
_CfprLsIssuesTable_Object = MibTable
cfprLsIssuesTable = _CfprLsIssuesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6)
)
if mibBuilder.loadTexts:
    cfprLsIssuesTable.setStatus("current")
_CfprLsIssuesEntry_Object = MibTableRow
cfprLsIssuesEntry = _CfprLsIssuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1)
)
cfprLsIssuesEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsIssuesInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsIssuesEntry.setStatus("current")
_CfprLsIssuesInstanceId_Type = CfprManagedObjectId
_CfprLsIssuesInstanceId_Object = MibTableColumn
cfprLsIssuesInstanceId = _CfprLsIssuesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 1),
    _CfprLsIssuesInstanceId_Type()
)
cfprLsIssuesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsIssuesInstanceId.setStatus("current")
_CfprLsIssuesDn_Type = CfprManagedObjectDn
_CfprLsIssuesDn_Object = MibTableColumn
cfprLsIssuesDn = _CfprLsIssuesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 2),
    _CfprLsIssuesDn_Type()
)
cfprLsIssuesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesDn.setStatus("current")
_CfprLsIssuesRn_Type = SnmpAdminString
_CfprLsIssuesRn_Object = MibTableColumn
cfprLsIssuesRn = _CfprLsIssuesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 3),
    _CfprLsIssuesRn_Type()
)
cfprLsIssuesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesRn.setStatus("current")
_CfprLsIssuesConfigWarnings_Type = CfprLsConfigWarnings
_CfprLsIssuesConfigWarnings_Object = MibTableColumn
cfprLsIssuesConfigWarnings = _CfprLsIssuesConfigWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 4),
    _CfprLsIssuesConfigWarnings_Type()
)
cfprLsIssuesConfigWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesConfigWarnings.setStatus("current")
_CfprLsIssuesIscsiConfigIssues_Type = CfprVnicIScsiConfigIssues
_CfprLsIssuesIscsiConfigIssues_Object = MibTableColumn
cfprLsIssuesIscsiConfigIssues = _CfprLsIssuesIscsiConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 5),
    _CfprLsIssuesIscsiConfigIssues_Type()
)
cfprLsIssuesIscsiConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesIscsiConfigIssues.setStatus("current")
_CfprLsIssuesNetworkConfigIssues_Type = CfprNetworkConfigIssues
_CfprLsIssuesNetworkConfigIssues_Object = MibTableColumn
cfprLsIssuesNetworkConfigIssues = _CfprLsIssuesNetworkConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 6),
    _CfprLsIssuesNetworkConfigIssues_Type()
)
cfprLsIssuesNetworkConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesNetworkConfigIssues.setStatus("current")
_CfprLsIssuesServerConfigIssues_Type = CfprServerConfigIssues
_CfprLsIssuesServerConfigIssues_Object = MibTableColumn
cfprLsIssuesServerConfigIssues = _CfprLsIssuesServerConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 7),
    _CfprLsIssuesServerConfigIssues_Type()
)
cfprLsIssuesServerConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesServerConfigIssues.setStatus("current")
_CfprLsIssuesStorageConfigIssues_Type = CfprStorageConfigIssues
_CfprLsIssuesStorageConfigIssues_Object = MibTableColumn
cfprLsIssuesStorageConfigIssues = _CfprLsIssuesStorageConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 8),
    _CfprLsIssuesStorageConfigIssues_Type()
)
cfprLsIssuesStorageConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesStorageConfigIssues.setStatus("current")
_CfprLsIssuesVnicConfigIssues_Type = CfprVnicConfigIssues
_CfprLsIssuesVnicConfigIssues_Object = MibTableColumn
cfprLsIssuesVnicConfigIssues = _CfprLsIssuesVnicConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 6, 1, 9),
    _CfprLsIssuesVnicConfigIssues_Type()
)
cfprLsIssuesVnicConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsIssuesVnicConfigIssues.setStatus("current")
_CfprLsPowerTable_Object = MibTable
cfprLsPowerTable = _CfprLsPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7)
)
if mibBuilder.loadTexts:
    cfprLsPowerTable.setStatus("current")
_CfprLsPowerEntry_Object = MibTableRow
cfprLsPowerEntry = _CfprLsPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7, 1)
)
cfprLsPowerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsPowerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsPowerEntry.setStatus("current")
_CfprLsPowerInstanceId_Type = CfprManagedObjectId
_CfprLsPowerInstanceId_Object = MibTableColumn
cfprLsPowerInstanceId = _CfprLsPowerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7, 1, 1),
    _CfprLsPowerInstanceId_Type()
)
cfprLsPowerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsPowerInstanceId.setStatus("current")
_CfprLsPowerDn_Type = CfprManagedObjectDn
_CfprLsPowerDn_Object = MibTableColumn
cfprLsPowerDn = _CfprLsPowerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7, 1, 2),
    _CfprLsPowerDn_Type()
)
cfprLsPowerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsPowerDn.setStatus("current")
_CfprLsPowerRn_Type = SnmpAdminString
_CfprLsPowerRn_Object = MibTableColumn
cfprLsPowerRn = _CfprLsPowerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7, 1, 3),
    _CfprLsPowerRn_Type()
)
cfprLsPowerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsPowerRn.setStatus("current")
_CfprLsPowerState_Type = CfprLsPowerState
_CfprLsPowerState_Object = MibTableColumn
cfprLsPowerState = _CfprLsPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7, 1, 4),
    _CfprLsPowerState_Type()
)
cfprLsPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsPowerState.setStatus("current")
_CfprLsPowerAllocPolicyName_Type = SnmpAdminString
_CfprLsPowerAllocPolicyName_Object = MibTableColumn
cfprLsPowerAllocPolicyName = _CfprLsPowerAllocPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 7, 1, 5),
    _CfprLsPowerAllocPolicyName_Type()
)
cfprLsPowerAllocPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsPowerAllocPolicyName.setStatus("current")
_CfprLsRequirementTable_Object = MibTable
cfprLsRequirementTable = _CfprLsRequirementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8)
)
if mibBuilder.loadTexts:
    cfprLsRequirementTable.setStatus("current")
_CfprLsRequirementEntry_Object = MibTableRow
cfprLsRequirementEntry = _CfprLsRequirementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1)
)
cfprLsRequirementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsRequirementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsRequirementEntry.setStatus("current")
_CfprLsRequirementInstanceId_Type = CfprManagedObjectId
_CfprLsRequirementInstanceId_Object = MibTableColumn
cfprLsRequirementInstanceId = _CfprLsRequirementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 1),
    _CfprLsRequirementInstanceId_Type()
)
cfprLsRequirementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsRequirementInstanceId.setStatus("current")
_CfprLsRequirementDn_Type = CfprManagedObjectDn
_CfprLsRequirementDn_Object = MibTableColumn
cfprLsRequirementDn = _CfprLsRequirementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 2),
    _CfprLsRequirementDn_Type()
)
cfprLsRequirementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementDn.setStatus("current")
_CfprLsRequirementRn_Type = SnmpAdminString
_CfprLsRequirementRn_Object = MibTableColumn
cfprLsRequirementRn = _CfprLsRequirementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 3),
    _CfprLsRequirementRn_Type()
)
cfprLsRequirementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementRn.setStatus("current")
_CfprLsRequirementAssignedToDn_Type = SnmpAdminString
_CfprLsRequirementAssignedToDn_Object = MibTableColumn
cfprLsRequirementAssignedToDn = _CfprLsRequirementAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 4),
    _CfprLsRequirementAssignedToDn_Type()
)
cfprLsRequirementAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementAssignedToDn.setStatus("current")
_CfprLsRequirementComputeEpDn_Type = SnmpAdminString
_CfprLsRequirementComputeEpDn_Object = MibTableColumn
cfprLsRequirementComputeEpDn = _CfprLsRequirementComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 5),
    _CfprLsRequirementComputeEpDn_Type()
)
cfprLsRequirementComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementComputeEpDn.setStatus("current")
_CfprLsRequirementIssues_Type = CfprLsConfigIssues
_CfprLsRequirementIssues_Object = MibTableColumn
cfprLsRequirementIssues = _CfprLsRequirementIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 6),
    _CfprLsRequirementIssues_Type()
)
cfprLsRequirementIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementIssues.setStatus("current")
_CfprLsRequirementName_Type = SnmpAdminString
_CfprLsRequirementName_Object = MibTableColumn
cfprLsRequirementName = _CfprLsRequirementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 7),
    _CfprLsRequirementName_Type()
)
cfprLsRequirementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementName.setStatus("current")
_CfprLsRequirementOperName_Type = SnmpAdminString
_CfprLsRequirementOperName_Object = MibTableColumn
cfprLsRequirementOperName = _CfprLsRequirementOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 8),
    _CfprLsRequirementOperName_Type()
)
cfprLsRequirementOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementOperName.setStatus("current")
_CfprLsRequirementOperState_Type = CfprLsComputeBindingOperState
_CfprLsRequirementOperState_Object = MibTableColumn
cfprLsRequirementOperState = _CfprLsRequirementOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 9),
    _CfprLsRequirementOperState_Type()
)
cfprLsRequirementOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementOperState.setStatus("current")
_CfprLsRequirementPnDn_Type = SnmpAdminString
_CfprLsRequirementPnDn_Object = MibTableColumn
cfprLsRequirementPnDn = _CfprLsRequirementPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 10),
    _CfprLsRequirementPnDn_Type()
)
cfprLsRequirementPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementPnDn.setStatus("current")
_CfprLsRequirementPnPoolDn_Type = SnmpAdminString
_CfprLsRequirementPnPoolDn_Object = MibTableColumn
cfprLsRequirementPnPoolDn = _CfprLsRequirementPnPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 11),
    _CfprLsRequirementPnPoolDn_Type()
)
cfprLsRequirementPnPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementPnPoolDn.setStatus("current")
_CfprLsRequirementQualifier_Type = SnmpAdminString
_CfprLsRequirementQualifier_Object = MibTableColumn
cfprLsRequirementQualifier = _CfprLsRequirementQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 12),
    _CfprLsRequirementQualifier_Type()
)
cfprLsRequirementQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementQualifier.setStatus("current")
_CfprLsRequirementRestrictMigration_Type = TruthValue
_CfprLsRequirementRestrictMigration_Object = MibTableColumn
cfprLsRequirementRestrictMigration = _CfprLsRequirementRestrictMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 8, 1, 13),
    _CfprLsRequirementRestrictMigration_Type()
)
cfprLsRequirementRestrictMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsRequirementRestrictMigration.setStatus("current")
_CfprLsServerTable_Object = MibTable
cfprLsServerTable = _CfprLsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9)
)
if mibBuilder.loadTexts:
    cfprLsServerTable.setStatus("current")
_CfprLsServerEntry_Object = MibTableRow
cfprLsServerEntry = _CfprLsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1)
)
cfprLsServerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsServerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsServerEntry.setStatus("current")
_CfprLsServerInstanceId_Type = CfprManagedObjectId
_CfprLsServerInstanceId_Object = MibTableColumn
cfprLsServerInstanceId = _CfprLsServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 1),
    _CfprLsServerInstanceId_Type()
)
cfprLsServerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsServerInstanceId.setStatus("current")
_CfprLsServerDn_Type = CfprManagedObjectDn
_CfprLsServerDn_Object = MibTableColumn
cfprLsServerDn = _CfprLsServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 2),
    _CfprLsServerDn_Type()
)
cfprLsServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerDn.setStatus("current")
_CfprLsServerRn_Type = SnmpAdminString
_CfprLsServerRn_Object = MibTableColumn
cfprLsServerRn = _CfprLsServerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 3),
    _CfprLsServerRn_Type()
)
cfprLsServerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerRn.setStatus("current")
_CfprLsServerAgentPolicyName_Type = SnmpAdminString
_CfprLsServerAgentPolicyName_Object = MibTableColumn
cfprLsServerAgentPolicyName = _CfprLsServerAgentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 4),
    _CfprLsServerAgentPolicyName_Type()
)
cfprLsServerAgentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerAgentPolicyName.setStatus("current")
_CfprLsServerAssignState_Type = CfprLsAssignment
_CfprLsServerAssignState_Object = MibTableColumn
cfprLsServerAssignState = _CfprLsServerAssignState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 5),
    _CfprLsServerAssignState_Type()
)
cfprLsServerAssignState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerAssignState.setStatus("current")
_CfprLsServerAssocState_Type = CfprLsAssocState
_CfprLsServerAssocState_Object = MibTableColumn
cfprLsServerAssocState = _CfprLsServerAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 6),
    _CfprLsServerAssocState_Type()
)
cfprLsServerAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerAssocState.setStatus("current")
_CfprLsServerBiosProfileName_Type = SnmpAdminString
_CfprLsServerBiosProfileName_Object = MibTableColumn
cfprLsServerBiosProfileName = _CfprLsServerBiosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 7),
    _CfprLsServerBiosProfileName_Type()
)
cfprLsServerBiosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerBiosProfileName.setStatus("current")
_CfprLsServerBootPolicyName_Type = SnmpAdminString
_CfprLsServerBootPolicyName_Object = MibTableColumn
cfprLsServerBootPolicyName = _CfprLsServerBootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 8),
    _CfprLsServerBootPolicyName_Type()
)
cfprLsServerBootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerBootPolicyName.setStatus("current")
_CfprLsServerConfigQualifier_Type = CfprLsConfigIssues
_CfprLsServerConfigQualifier_Object = MibTableColumn
cfprLsServerConfigQualifier = _CfprLsServerConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 9),
    _CfprLsServerConfigQualifier_Type()
)
cfprLsServerConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerConfigQualifier.setStatus("current")
_CfprLsServerConfigState_Type = CfprLsConfigState
_CfprLsServerConfigState_Object = MibTableColumn
cfprLsServerConfigState = _CfprLsServerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 10),
    _CfprLsServerConfigState_Type()
)
cfprLsServerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerConfigState.setStatus("current")
_CfprLsServerDescr_Type = SnmpAdminString
_CfprLsServerDescr_Object = MibTableColumn
cfprLsServerDescr = _CfprLsServerDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 11),
    _CfprLsServerDescr_Type()
)
cfprLsServerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerDescr.setStatus("current")
_CfprLsServerDynamicConPolicyName_Type = SnmpAdminString
_CfprLsServerDynamicConPolicyName_Object = MibTableColumn
cfprLsServerDynamicConPolicyName = _CfprLsServerDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 12),
    _CfprLsServerDynamicConPolicyName_Type()
)
cfprLsServerDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerDynamicConPolicyName.setStatus("current")
_CfprLsServerExtIPPoolName_Type = SnmpAdminString
_CfprLsServerExtIPPoolName_Object = MibTableColumn
cfprLsServerExtIPPoolName = _CfprLsServerExtIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 13),
    _CfprLsServerExtIPPoolName_Type()
)
cfprLsServerExtIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerExtIPPoolName.setStatus("current")
_CfprLsServerExtIPState_Type = CfprVnicExternalMgmtIPMode
_CfprLsServerExtIPState_Object = MibTableColumn
cfprLsServerExtIPState = _CfprLsServerExtIPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 14),
    _CfprLsServerExtIPState_Type()
)
cfprLsServerExtIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerExtIPState.setStatus("current")
_CfprLsServerFltAggr_Type = Unsigned64
_CfprLsServerFltAggr_Object = MibTableColumn
cfprLsServerFltAggr = _CfprLsServerFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 15),
    _CfprLsServerFltAggr_Type()
)
cfprLsServerFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFltAggr.setStatus("current")
_CfprLsServerFsmDescr_Type = SnmpAdminString
_CfprLsServerFsmDescr_Object = MibTableColumn
cfprLsServerFsmDescr = _CfprLsServerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 16),
    _CfprLsServerFsmDescr_Type()
)
cfprLsServerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmDescr.setStatus("current")
_CfprLsServerFsmFlags_Type = SnmpAdminString
_CfprLsServerFsmFlags_Object = MibTableColumn
cfprLsServerFsmFlags = _CfprLsServerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 17),
    _CfprLsServerFsmFlags_Type()
)
cfprLsServerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmFlags.setStatus("current")
_CfprLsServerFsmPrev_Type = SnmpAdminString
_CfprLsServerFsmPrev_Object = MibTableColumn
cfprLsServerFsmPrev = _CfprLsServerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 18),
    _CfprLsServerFsmPrev_Type()
)
cfprLsServerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmPrev.setStatus("current")
_CfprLsServerFsmProgr_Type = Gauge32
_CfprLsServerFsmProgr_Object = MibTableColumn
cfprLsServerFsmProgr = _CfprLsServerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 19),
    _CfprLsServerFsmProgr_Type()
)
cfprLsServerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmProgr.setStatus("current")
_CfprLsServerFsmRmtInvErrCode_Type = Gauge32
_CfprLsServerFsmRmtInvErrCode_Object = MibTableColumn
cfprLsServerFsmRmtInvErrCode = _CfprLsServerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 20),
    _CfprLsServerFsmRmtInvErrCode_Type()
)
cfprLsServerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRmtInvErrCode.setStatus("current")
_CfprLsServerFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprLsServerFsmRmtInvErrDescr_Object = MibTableColumn
cfprLsServerFsmRmtInvErrDescr = _CfprLsServerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 21),
    _CfprLsServerFsmRmtInvErrDescr_Type()
)
cfprLsServerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRmtInvErrDescr.setStatus("current")
_CfprLsServerFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprLsServerFsmRmtInvRslt_Object = MibTableColumn
cfprLsServerFsmRmtInvRslt = _CfprLsServerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 22),
    _CfprLsServerFsmRmtInvRslt_Type()
)
cfprLsServerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRmtInvRslt.setStatus("current")
_CfprLsServerFsmStageDescr_Type = SnmpAdminString
_CfprLsServerFsmStageDescr_Object = MibTableColumn
cfprLsServerFsmStageDescr = _CfprLsServerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 23),
    _CfprLsServerFsmStageDescr_Type()
)
cfprLsServerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageDescr.setStatus("current")
_CfprLsServerFsmStamp_Type = DateAndTime
_CfprLsServerFsmStamp_Object = MibTableColumn
cfprLsServerFsmStamp = _CfprLsServerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 24),
    _CfprLsServerFsmStamp_Type()
)
cfprLsServerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStamp.setStatus("current")
_CfprLsServerFsmStatus_Type = SnmpAdminString
_CfprLsServerFsmStatus_Object = MibTableColumn
cfprLsServerFsmStatus = _CfprLsServerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 25),
    _CfprLsServerFsmStatus_Type()
)
cfprLsServerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStatus.setStatus("current")
_CfprLsServerFsmTry_Type = Gauge32
_CfprLsServerFsmTry_Object = MibTableColumn
cfprLsServerFsmTry = _CfprLsServerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 26),
    _CfprLsServerFsmTry_Type()
)
cfprLsServerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTry.setStatus("current")
_CfprLsServerHostFwPolicyName_Type = SnmpAdminString
_CfprLsServerHostFwPolicyName_Object = MibTableColumn
cfprLsServerHostFwPolicyName = _CfprLsServerHostFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 27),
    _CfprLsServerHostFwPolicyName_Type()
)
cfprLsServerHostFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerHostFwPolicyName.setStatus("current")
_CfprLsServerIdentPoolName_Type = SnmpAdminString
_CfprLsServerIdentPoolName_Object = MibTableColumn
cfprLsServerIdentPoolName = _CfprLsServerIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 28),
    _CfprLsServerIdentPoolName_Type()
)
cfprLsServerIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerIdentPoolName.setStatus("current")
_CfprLsServerIntId_Type = SnmpAdminString
_CfprLsServerIntId_Object = MibTableColumn
cfprLsServerIntId = _CfprLsServerIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 29),
    _CfprLsServerIntId_Type()
)
cfprLsServerIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerIntId.setStatus("current")
_CfprLsServerKvmMgmtPolicyName_Type = SnmpAdminString
_CfprLsServerKvmMgmtPolicyName_Object = MibTableColumn
cfprLsServerKvmMgmtPolicyName = _CfprLsServerKvmMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 30),
    _CfprLsServerKvmMgmtPolicyName_Type()
)
cfprLsServerKvmMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerKvmMgmtPolicyName.setStatus("current")
_CfprLsServerLocalDiskPolicyName_Type = SnmpAdminString
_CfprLsServerLocalDiskPolicyName_Object = MibTableColumn
cfprLsServerLocalDiskPolicyName = _CfprLsServerLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 31),
    _CfprLsServerLocalDiskPolicyName_Type()
)
cfprLsServerLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerLocalDiskPolicyName.setStatus("current")
_CfprLsServerMaintPolicyName_Type = SnmpAdminString
_CfprLsServerMaintPolicyName_Object = MibTableColumn
cfprLsServerMaintPolicyName = _CfprLsServerMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 32),
    _CfprLsServerMaintPolicyName_Type()
)
cfprLsServerMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerMaintPolicyName.setStatus("current")
_CfprLsServerMgmtAccessPolicyName_Type = SnmpAdminString
_CfprLsServerMgmtAccessPolicyName_Object = MibTableColumn
cfprLsServerMgmtAccessPolicyName = _CfprLsServerMgmtAccessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 33),
    _CfprLsServerMgmtAccessPolicyName_Type()
)
cfprLsServerMgmtAccessPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerMgmtAccessPolicyName.setStatus("current")
_CfprLsServerMgmtFwPolicyName_Type = SnmpAdminString
_CfprLsServerMgmtFwPolicyName_Object = MibTableColumn
cfprLsServerMgmtFwPolicyName = _CfprLsServerMgmtFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 34),
    _CfprLsServerMgmtFwPolicyName_Type()
)
cfprLsServerMgmtFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerMgmtFwPolicyName.setStatus("current")
_CfprLsServerName_Type = SnmpAdminString
_CfprLsServerName_Object = MibTableColumn
cfprLsServerName = _CfprLsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 35),
    _CfprLsServerName_Type()
)
cfprLsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerName.setStatus("current")
_CfprLsServerOperBiosProfileName_Type = SnmpAdminString
_CfprLsServerOperBiosProfileName_Object = MibTableColumn
cfprLsServerOperBiosProfileName = _CfprLsServerOperBiosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 36),
    _CfprLsServerOperBiosProfileName_Type()
)
cfprLsServerOperBiosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperBiosProfileName.setStatus("current")
_CfprLsServerOperBootPolicyName_Type = SnmpAdminString
_CfprLsServerOperBootPolicyName_Object = MibTableColumn
cfprLsServerOperBootPolicyName = _CfprLsServerOperBootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 37),
    _CfprLsServerOperBootPolicyName_Type()
)
cfprLsServerOperBootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperBootPolicyName.setStatus("current")
_CfprLsServerOperDynamicConPolicyName_Type = SnmpAdminString
_CfprLsServerOperDynamicConPolicyName_Object = MibTableColumn
cfprLsServerOperDynamicConPolicyName = _CfprLsServerOperDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 38),
    _CfprLsServerOperDynamicConPolicyName_Type()
)
cfprLsServerOperDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperDynamicConPolicyName.setStatus("current")
_CfprLsServerOperExtIPPoolName_Type = SnmpAdminString
_CfprLsServerOperExtIPPoolName_Object = MibTableColumn
cfprLsServerOperExtIPPoolName = _CfprLsServerOperExtIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 39),
    _CfprLsServerOperExtIPPoolName_Type()
)
cfprLsServerOperExtIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperExtIPPoolName.setStatus("current")
_CfprLsServerOperHostFwPolicyName_Type = SnmpAdminString
_CfprLsServerOperHostFwPolicyName_Object = MibTableColumn
cfprLsServerOperHostFwPolicyName = _CfprLsServerOperHostFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 40),
    _CfprLsServerOperHostFwPolicyName_Type()
)
cfprLsServerOperHostFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperHostFwPolicyName.setStatus("current")
_CfprLsServerOperIdentPoolName_Type = SnmpAdminString
_CfprLsServerOperIdentPoolName_Object = MibTableColumn
cfprLsServerOperIdentPoolName = _CfprLsServerOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 41),
    _CfprLsServerOperIdentPoolName_Type()
)
cfprLsServerOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperIdentPoolName.setStatus("current")
_CfprLsServerOperKvmMgmtPolicyName_Type = SnmpAdminString
_CfprLsServerOperKvmMgmtPolicyName_Object = MibTableColumn
cfprLsServerOperKvmMgmtPolicyName = _CfprLsServerOperKvmMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 42),
    _CfprLsServerOperKvmMgmtPolicyName_Type()
)
cfprLsServerOperKvmMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperKvmMgmtPolicyName.setStatus("current")
_CfprLsServerOperLocalDiskPolicyName_Type = SnmpAdminString
_CfprLsServerOperLocalDiskPolicyName_Object = MibTableColumn
cfprLsServerOperLocalDiskPolicyName = _CfprLsServerOperLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 43),
    _CfprLsServerOperLocalDiskPolicyName_Type()
)
cfprLsServerOperLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperLocalDiskPolicyName.setStatus("current")
_CfprLsServerOperMaintPolicyName_Type = SnmpAdminString
_CfprLsServerOperMaintPolicyName_Object = MibTableColumn
cfprLsServerOperMaintPolicyName = _CfprLsServerOperMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 44),
    _CfprLsServerOperMaintPolicyName_Type()
)
cfprLsServerOperMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperMaintPolicyName.setStatus("current")
_CfprLsServerOperMgmtAccessPolicyName_Type = SnmpAdminString
_CfprLsServerOperMgmtAccessPolicyName_Object = MibTableColumn
cfprLsServerOperMgmtAccessPolicyName = _CfprLsServerOperMgmtAccessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 45),
    _CfprLsServerOperMgmtAccessPolicyName_Type()
)
cfprLsServerOperMgmtAccessPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperMgmtAccessPolicyName.setStatus("current")
_CfprLsServerOperMgmtFwPolicyName_Type = SnmpAdminString
_CfprLsServerOperMgmtFwPolicyName_Object = MibTableColumn
cfprLsServerOperMgmtFwPolicyName = _CfprLsServerOperMgmtFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 46),
    _CfprLsServerOperMgmtFwPolicyName_Type()
)
cfprLsServerOperMgmtFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperMgmtFwPolicyName.setStatus("current")
_CfprLsServerOperPowerPolicyName_Type = SnmpAdminString
_CfprLsServerOperPowerPolicyName_Object = MibTableColumn
cfprLsServerOperPowerPolicyName = _CfprLsServerOperPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 47),
    _CfprLsServerOperPowerPolicyName_Type()
)
cfprLsServerOperPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperPowerPolicyName.setStatus("current")
_CfprLsServerOperScrubPolicyName_Type = SnmpAdminString
_CfprLsServerOperScrubPolicyName_Object = MibTableColumn
cfprLsServerOperScrubPolicyName = _CfprLsServerOperScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 48),
    _CfprLsServerOperScrubPolicyName_Type()
)
cfprLsServerOperScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperScrubPolicyName.setStatus("current")
_CfprLsServerOperSolPolicyName_Type = SnmpAdminString
_CfprLsServerOperSolPolicyName_Object = MibTableColumn
cfprLsServerOperSolPolicyName = _CfprLsServerOperSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 49),
    _CfprLsServerOperSolPolicyName_Type()
)
cfprLsServerOperSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperSolPolicyName.setStatus("current")
_CfprLsServerOperSrcTemplName_Type = SnmpAdminString
_CfprLsServerOperSrcTemplName_Object = MibTableColumn
cfprLsServerOperSrcTemplName = _CfprLsServerOperSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 50),
    _CfprLsServerOperSrcTemplName_Type()
)
cfprLsServerOperSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperSrcTemplName.setStatus("current")
_CfprLsServerOperState_Type = CfprLsOperState
_CfprLsServerOperState_Object = MibTableColumn
cfprLsServerOperState = _CfprLsServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 51),
    _CfprLsServerOperState_Type()
)
cfprLsServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperState.setStatus("current")
_CfprLsServerOperStatsPolicyName_Type = SnmpAdminString
_CfprLsServerOperStatsPolicyName_Object = MibTableColumn
cfprLsServerOperStatsPolicyName = _CfprLsServerOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 52),
    _CfprLsServerOperStatsPolicyName_Type()
)
cfprLsServerOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperStatsPolicyName.setStatus("current")
_CfprLsServerOperVconProfileName_Type = SnmpAdminString
_CfprLsServerOperVconProfileName_Object = MibTableColumn
cfprLsServerOperVconProfileName = _CfprLsServerOperVconProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 53),
    _CfprLsServerOperVconProfileName_Type()
)
cfprLsServerOperVconProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperVconProfileName.setStatus("current")
_CfprLsServerOperVmediaPolicyName_Type = SnmpAdminString
_CfprLsServerOperVmediaPolicyName_Object = MibTableColumn
cfprLsServerOperVmediaPolicyName = _CfprLsServerOperVmediaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 54),
    _CfprLsServerOperVmediaPolicyName_Type()
)
cfprLsServerOperVmediaPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOperVmediaPolicyName.setStatus("current")
_CfprLsServerOwner_Type = CfprLsOwner
_CfprLsServerOwner_Object = MibTableColumn
cfprLsServerOwner = _CfprLsServerOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 55),
    _CfprLsServerOwner_Type()
)
cfprLsServerOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerOwner.setStatus("current")
_CfprLsServerPnDn_Type = SnmpAdminString
_CfprLsServerPnDn_Object = MibTableColumn
cfprLsServerPnDn = _CfprLsServerPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 56),
    _CfprLsServerPnDn_Type()
)
cfprLsServerPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerPnDn.setStatus("current")
_CfprLsServerPolicyLevel_Type = Gauge32
_CfprLsServerPolicyLevel_Object = MibTableColumn
cfprLsServerPolicyLevel = _CfprLsServerPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 57),
    _CfprLsServerPolicyLevel_Type()
)
cfprLsServerPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerPolicyLevel.setStatus("current")
_CfprLsServerPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsServerPolicyOwner_Object = MibTableColumn
cfprLsServerPolicyOwner = _CfprLsServerPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 58),
    _CfprLsServerPolicyOwner_Type()
)
cfprLsServerPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerPolicyOwner.setStatus("current")
_CfprLsServerPowerPolicyName_Type = SnmpAdminString
_CfprLsServerPowerPolicyName_Object = MibTableColumn
cfprLsServerPowerPolicyName = _CfprLsServerPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 59),
    _CfprLsServerPowerPolicyName_Type()
)
cfprLsServerPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerPowerPolicyName.setStatus("current")
_CfprLsServerResolveRemote_Type = CfprLsResolveFromRemoteServer
_CfprLsServerResolveRemote_Object = MibTableColumn
cfprLsServerResolveRemote = _CfprLsServerResolveRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 60),
    _CfprLsServerResolveRemote_Type()
)
cfprLsServerResolveRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerResolveRemote.setStatus("current")
_CfprLsServerScrubPolicyName_Type = SnmpAdminString
_CfprLsServerScrubPolicyName_Object = MibTableColumn
cfprLsServerScrubPolicyName = _CfprLsServerScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 61),
    _CfprLsServerScrubPolicyName_Type()
)
cfprLsServerScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerScrubPolicyName.setStatus("current")
_CfprLsServerSolPolicyName_Type = SnmpAdminString
_CfprLsServerSolPolicyName_Object = MibTableColumn
cfprLsServerSolPolicyName = _CfprLsServerSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 62),
    _CfprLsServerSolPolicyName_Type()
)
cfprLsServerSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerSolPolicyName.setStatus("current")
_CfprLsServerSrcTemplName_Type = SnmpAdminString
_CfprLsServerSrcTemplName_Object = MibTableColumn
cfprLsServerSrcTemplName = _CfprLsServerSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 63),
    _CfprLsServerSrcTemplName_Type()
)
cfprLsServerSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerSrcTemplName.setStatus("current")
_CfprLsServerStatsPolicyName_Type = SnmpAdminString
_CfprLsServerStatsPolicyName_Object = MibTableColumn
cfprLsServerStatsPolicyName = _CfprLsServerStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 64),
    _CfprLsServerStatsPolicyName_Type()
)
cfprLsServerStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerStatsPolicyName.setStatus("current")
_CfprLsServerSvnicConfig_Type = TruthValue
_CfprLsServerSvnicConfig_Object = MibTableColumn
cfprLsServerSvnicConfig = _CfprLsServerSvnicConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 65),
    _CfprLsServerSvnicConfig_Type()
)
cfprLsServerSvnicConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerSvnicConfig.setStatus("current")
_CfprLsServerType_Type = CfprLsType
_CfprLsServerType_Object = MibTableColumn
cfprLsServerType = _CfprLsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 66),
    _CfprLsServerType_Type()
)
cfprLsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerType.setStatus("current")
_CfprLsServerUsrLbl_Type = SnmpAdminString
_CfprLsServerUsrLbl_Object = MibTableColumn
cfprLsServerUsrLbl = _CfprLsServerUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 67),
    _CfprLsServerUsrLbl_Type()
)
cfprLsServerUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerUsrLbl.setStatus("current")
_CfprLsServerUuid_Type = SnmpAdminString
_CfprLsServerUuid_Object = MibTableColumn
cfprLsServerUuid = _CfprLsServerUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 68),
    _CfprLsServerUuid_Type()
)
cfprLsServerUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerUuid.setStatus("current")
_CfprLsServerUuidSuffix_Type = Unsigned64
_CfprLsServerUuidSuffix_Object = MibTableColumn
cfprLsServerUuidSuffix = _CfprLsServerUuidSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 69),
    _CfprLsServerUuidSuffix_Type()
)
cfprLsServerUuidSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerUuidSuffix.setStatus("current")
_CfprLsServerVconProfileName_Type = SnmpAdminString
_CfprLsServerVconProfileName_Object = MibTableColumn
cfprLsServerVconProfileName = _CfprLsServerVconProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 70),
    _CfprLsServerVconProfileName_Type()
)
cfprLsServerVconProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerVconProfileName.setStatus("current")
_CfprLsServerVmediaPolicyName_Type = SnmpAdminString
_CfprLsServerVmediaPolicyName_Object = MibTableColumn
cfprLsServerVmediaPolicyName = _CfprLsServerVmediaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 71),
    _CfprLsServerVmediaPolicyName_Type()
)
cfprLsServerVmediaPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerVmediaPolicyName.setStatus("current")
_CfprLsServerDeployType_Type = CfprSmDeployType
_CfprLsServerDeployType_Object = MibTableColumn
cfprLsServerDeployType = _CfprLsServerDeployType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 9, 1, 72),
    _CfprLsServerDeployType_Type()
)
cfprLsServerDeployType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerDeployType.setStatus("current")
_CfprLsServerAssocCtxTable_Object = MibTable
cfprLsServerAssocCtxTable = _CfprLsServerAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 10)
)
if mibBuilder.loadTexts:
    cfprLsServerAssocCtxTable.setStatus("current")
_CfprLsServerAssocCtxEntry_Object = MibTableRow
cfprLsServerAssocCtxEntry = _CfprLsServerAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 10, 1)
)
cfprLsServerAssocCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsServerAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsServerAssocCtxEntry.setStatus("current")
_CfprLsServerAssocCtxInstanceId_Type = CfprManagedObjectId
_CfprLsServerAssocCtxInstanceId_Object = MibTableColumn
cfprLsServerAssocCtxInstanceId = _CfprLsServerAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 10, 1, 1),
    _CfprLsServerAssocCtxInstanceId_Type()
)
cfprLsServerAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsServerAssocCtxInstanceId.setStatus("current")
_CfprLsServerAssocCtxDn_Type = CfprManagedObjectDn
_CfprLsServerAssocCtxDn_Object = MibTableColumn
cfprLsServerAssocCtxDn = _CfprLsServerAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 10, 1, 2),
    _CfprLsServerAssocCtxDn_Type()
)
cfprLsServerAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerAssocCtxDn.setStatus("current")
_CfprLsServerAssocCtxRn_Type = SnmpAdminString
_CfprLsServerAssocCtxRn_Object = MibTableColumn
cfprLsServerAssocCtxRn = _CfprLsServerAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 10, 1, 3),
    _CfprLsServerAssocCtxRn_Type()
)
cfprLsServerAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerAssocCtxRn.setStatus("current")
_CfprLsServerExtensionTable_Object = MibTable
cfprLsServerExtensionTable = _CfprLsServerExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11)
)
if mibBuilder.loadTexts:
    cfprLsServerExtensionTable.setStatus("current")
_CfprLsServerExtensionEntry_Object = MibTableRow
cfprLsServerExtensionEntry = _CfprLsServerExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11, 1)
)
cfprLsServerExtensionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsServerExtensionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsServerExtensionEntry.setStatus("current")
_CfprLsServerExtensionInstanceId_Type = CfprManagedObjectId
_CfprLsServerExtensionInstanceId_Object = MibTableColumn
cfprLsServerExtensionInstanceId = _CfprLsServerExtensionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11, 1, 1),
    _CfprLsServerExtensionInstanceId_Type()
)
cfprLsServerExtensionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsServerExtensionInstanceId.setStatus("current")
_CfprLsServerExtensionDn_Type = CfprManagedObjectDn
_CfprLsServerExtensionDn_Object = MibTableColumn
cfprLsServerExtensionDn = _CfprLsServerExtensionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11, 1, 2),
    _CfprLsServerExtensionDn_Type()
)
cfprLsServerExtensionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerExtensionDn.setStatus("current")
_CfprLsServerExtensionRn_Type = SnmpAdminString
_CfprLsServerExtensionRn_Object = MibTableColumn
cfprLsServerExtensionRn = _CfprLsServerExtensionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11, 1, 3),
    _CfprLsServerExtensionRn_Type()
)
cfprLsServerExtensionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerExtensionRn.setStatus("current")
_CfprLsServerExtensionGuid_Type = SnmpAdminString
_CfprLsServerExtensionGuid_Object = MibTableColumn
cfprLsServerExtensionGuid = _CfprLsServerExtensionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11, 1, 4),
    _CfprLsServerExtensionGuid_Type()
)
cfprLsServerExtensionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerExtensionGuid.setStatus("current")
_CfprLsServerExtensionVersion_Type = Gauge32
_CfprLsServerExtensionVersion_Object = MibTableColumn
cfprLsServerExtensionVersion = _CfprLsServerExtensionVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 11, 1, 5),
    _CfprLsServerExtensionVersion_Type()
)
cfprLsServerExtensionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerExtensionVersion.setStatus("current")
_CfprLsServerFsmTable_Object = MibTable
cfprLsServerFsmTable = _CfprLsServerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12)
)
if mibBuilder.loadTexts:
    cfprLsServerFsmTable.setStatus("current")
_CfprLsServerFsmEntry_Object = MibTableRow
cfprLsServerFsmEntry = _CfprLsServerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1)
)
cfprLsServerFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsServerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsServerFsmEntry.setStatus("current")
_CfprLsServerFsmInstanceId_Type = CfprManagedObjectId
_CfprLsServerFsmInstanceId_Object = MibTableColumn
cfprLsServerFsmInstanceId = _CfprLsServerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 1),
    _CfprLsServerFsmInstanceId_Type()
)
cfprLsServerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsServerFsmInstanceId.setStatus("current")
_CfprLsServerFsmDn_Type = CfprManagedObjectDn
_CfprLsServerFsmDn_Object = MibTableColumn
cfprLsServerFsmDn = _CfprLsServerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 2),
    _CfprLsServerFsmDn_Type()
)
cfprLsServerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmDn.setStatus("current")
_CfprLsServerFsmRn_Type = SnmpAdminString
_CfprLsServerFsmRn_Object = MibTableColumn
cfprLsServerFsmRn = _CfprLsServerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 3),
    _CfprLsServerFsmRn_Type()
)
cfprLsServerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRn.setStatus("current")
_CfprLsServerFsmCompletionTime_Type = DateAndTime
_CfprLsServerFsmCompletionTime_Object = MibTableColumn
cfprLsServerFsmCompletionTime = _CfprLsServerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 4),
    _CfprLsServerFsmCompletionTime_Type()
)
cfprLsServerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmCompletionTime.setStatus("current")
_CfprLsServerFsmCurrentFsm_Type = CfprLsServerFsmCurrentFsm
_CfprLsServerFsmCurrentFsm_Object = MibTableColumn
cfprLsServerFsmCurrentFsm = _CfprLsServerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 5),
    _CfprLsServerFsmCurrentFsm_Type()
)
cfprLsServerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmCurrentFsm.setStatus("current")
_CfprLsServerFsmDescrData_Type = SnmpAdminString
_CfprLsServerFsmDescrData_Object = MibTableColumn
cfprLsServerFsmDescrData = _CfprLsServerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 6),
    _CfprLsServerFsmDescrData_Type()
)
cfprLsServerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmDescrData.setStatus("current")
_CfprLsServerFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprLsServerFsmFsmStatus_Object = MibTableColumn
cfprLsServerFsmFsmStatus = _CfprLsServerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 7),
    _CfprLsServerFsmFsmStatus_Type()
)
cfprLsServerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmFsmStatus.setStatus("current")
_CfprLsServerFsmProgress_Type = Gauge32
_CfprLsServerFsmProgress_Object = MibTableColumn
cfprLsServerFsmProgress = _CfprLsServerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 8),
    _CfprLsServerFsmProgress_Type()
)
cfprLsServerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmProgress.setStatus("current")
_CfprLsServerFsmRmtErrCode_Type = Gauge32
_CfprLsServerFsmRmtErrCode_Object = MibTableColumn
cfprLsServerFsmRmtErrCode = _CfprLsServerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 9),
    _CfprLsServerFsmRmtErrCode_Type()
)
cfprLsServerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRmtErrCode.setStatus("current")
_CfprLsServerFsmRmtErrDescr_Type = SnmpAdminString
_CfprLsServerFsmRmtErrDescr_Object = MibTableColumn
cfprLsServerFsmRmtErrDescr = _CfprLsServerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 10),
    _CfprLsServerFsmRmtErrDescr_Type()
)
cfprLsServerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRmtErrDescr.setStatus("current")
_CfprLsServerFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprLsServerFsmRmtRslt_Object = MibTableColumn
cfprLsServerFsmRmtRslt = _CfprLsServerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 12, 1, 11),
    _CfprLsServerFsmRmtRslt_Type()
)
cfprLsServerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmRmtRslt.setStatus("current")
_CfprLsServerFsmStageTable_Object = MibTable
cfprLsServerFsmStageTable = _CfprLsServerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13)
)
if mibBuilder.loadTexts:
    cfprLsServerFsmStageTable.setStatus("current")
_CfprLsServerFsmStageEntry_Object = MibTableRow
cfprLsServerFsmStageEntry = _CfprLsServerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1)
)
cfprLsServerFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsServerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsServerFsmStageEntry.setStatus("current")
_CfprLsServerFsmStageInstanceId_Type = CfprManagedObjectId
_CfprLsServerFsmStageInstanceId_Object = MibTableColumn
cfprLsServerFsmStageInstanceId = _CfprLsServerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 1),
    _CfprLsServerFsmStageInstanceId_Type()
)
cfprLsServerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageInstanceId.setStatus("current")
_CfprLsServerFsmStageDn_Type = CfprManagedObjectDn
_CfprLsServerFsmStageDn_Object = MibTableColumn
cfprLsServerFsmStageDn = _CfprLsServerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 2),
    _CfprLsServerFsmStageDn_Type()
)
cfprLsServerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageDn.setStatus("current")
_CfprLsServerFsmStageRn_Type = SnmpAdminString
_CfprLsServerFsmStageRn_Object = MibTableColumn
cfprLsServerFsmStageRn = _CfprLsServerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 3),
    _CfprLsServerFsmStageRn_Type()
)
cfprLsServerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageRn.setStatus("current")
_CfprLsServerFsmStageDescrData_Type = SnmpAdminString
_CfprLsServerFsmStageDescrData_Object = MibTableColumn
cfprLsServerFsmStageDescrData = _CfprLsServerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 4),
    _CfprLsServerFsmStageDescrData_Type()
)
cfprLsServerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageDescrData.setStatus("current")
_CfprLsServerFsmStageLastUpdateTime_Type = DateAndTime
_CfprLsServerFsmStageLastUpdateTime_Object = MibTableColumn
cfprLsServerFsmStageLastUpdateTime = _CfprLsServerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 5),
    _CfprLsServerFsmStageLastUpdateTime_Type()
)
cfprLsServerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageLastUpdateTime.setStatus("current")
_CfprLsServerFsmStageName_Type = CfprLsServerFsmStageName
_CfprLsServerFsmStageName_Object = MibTableColumn
cfprLsServerFsmStageName = _CfprLsServerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 6),
    _CfprLsServerFsmStageName_Type()
)
cfprLsServerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageName.setStatus("current")
_CfprLsServerFsmStageOrder_Type = Gauge32
_CfprLsServerFsmStageOrder_Object = MibTableColumn
cfprLsServerFsmStageOrder = _CfprLsServerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 7),
    _CfprLsServerFsmStageOrder_Type()
)
cfprLsServerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageOrder.setStatus("current")
_CfprLsServerFsmStageRetry_Type = Gauge32
_CfprLsServerFsmStageRetry_Object = MibTableColumn
cfprLsServerFsmStageRetry = _CfprLsServerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 8),
    _CfprLsServerFsmStageRetry_Type()
)
cfprLsServerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageRetry.setStatus("current")
_CfprLsServerFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprLsServerFsmStageStageStatus_Object = MibTableColumn
cfprLsServerFsmStageStageStatus = _CfprLsServerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 13, 1, 9),
    _CfprLsServerFsmStageStageStatus_Type()
)
cfprLsServerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmStageStageStatus.setStatus("current")
_CfprLsServerFsmTaskTable_Object = MibTable
cfprLsServerFsmTaskTable = _CfprLsServerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14)
)
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskTable.setStatus("current")
_CfprLsServerFsmTaskEntry_Object = MibTableRow
cfprLsServerFsmTaskEntry = _CfprLsServerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1)
)
cfprLsServerFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsServerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskEntry.setStatus("current")
_CfprLsServerFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprLsServerFsmTaskInstanceId_Object = MibTableColumn
cfprLsServerFsmTaskInstanceId = _CfprLsServerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 1),
    _CfprLsServerFsmTaskInstanceId_Type()
)
cfprLsServerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskInstanceId.setStatus("current")
_CfprLsServerFsmTaskDn_Type = CfprManagedObjectDn
_CfprLsServerFsmTaskDn_Object = MibTableColumn
cfprLsServerFsmTaskDn = _CfprLsServerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 2),
    _CfprLsServerFsmTaskDn_Type()
)
cfprLsServerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskDn.setStatus("current")
_CfprLsServerFsmTaskRn_Type = SnmpAdminString
_CfprLsServerFsmTaskRn_Object = MibTableColumn
cfprLsServerFsmTaskRn = _CfprLsServerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 3),
    _CfprLsServerFsmTaskRn_Type()
)
cfprLsServerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskRn.setStatus("current")
_CfprLsServerFsmTaskCompletion_Type = CfprFsmCompletion
_CfprLsServerFsmTaskCompletion_Object = MibTableColumn
cfprLsServerFsmTaskCompletion = _CfprLsServerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 4),
    _CfprLsServerFsmTaskCompletion_Type()
)
cfprLsServerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskCompletion.setStatus("current")
_CfprLsServerFsmTaskFlags_Type = CfprLsServerFsmTaskFlags
_CfprLsServerFsmTaskFlags_Object = MibTableColumn
cfprLsServerFsmTaskFlags = _CfprLsServerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 5),
    _CfprLsServerFsmTaskFlags_Type()
)
cfprLsServerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskFlags.setStatus("current")
_CfprLsServerFsmTaskItem_Type = CfprLsServerFsmTaskItem
_CfprLsServerFsmTaskItem_Object = MibTableColumn
cfprLsServerFsmTaskItem = _CfprLsServerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 6),
    _CfprLsServerFsmTaskItem_Type()
)
cfprLsServerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskItem.setStatus("current")
_CfprLsServerFsmTaskSeqId_Type = Gauge32
_CfprLsServerFsmTaskSeqId_Object = MibTableColumn
cfprLsServerFsmTaskSeqId = _CfprLsServerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 14, 1, 7),
    _CfprLsServerFsmTaskSeqId_Type()
)
cfprLsServerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsServerFsmTaskSeqId.setStatus("current")
_CfprLsTierTable_Object = MibTable
cfprLsTierTable = _CfprLsTierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15)
)
if mibBuilder.loadTexts:
    cfprLsTierTable.setStatus("current")
_CfprLsTierEntry_Object = MibTableRow
cfprLsTierEntry = _CfprLsTierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1)
)
cfprLsTierEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsTierInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsTierEntry.setStatus("current")
_CfprLsTierInstanceId_Type = CfprManagedObjectId
_CfprLsTierInstanceId_Object = MibTableColumn
cfprLsTierInstanceId = _CfprLsTierInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 1),
    _CfprLsTierInstanceId_Type()
)
cfprLsTierInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsTierInstanceId.setStatus("current")
_CfprLsTierDn_Type = CfprManagedObjectDn
_CfprLsTierDn_Object = MibTableColumn
cfprLsTierDn = _CfprLsTierDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 2),
    _CfprLsTierDn_Type()
)
cfprLsTierDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierDn.setStatus("current")
_CfprLsTierRn_Type = SnmpAdminString
_CfprLsTierRn_Object = MibTableColumn
cfprLsTierRn = _CfprLsTierRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 3),
    _CfprLsTierRn_Type()
)
cfprLsTierRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierRn.setStatus("current")
_CfprLsTierApply_Type = CfprLsApply
_CfprLsTierApply_Object = MibTableColumn
cfprLsTierApply = _CfprLsTierApply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 4),
    _CfprLsTierApply_Type()
)
cfprLsTierApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierApply.setStatus("current")
_CfprLsTierDescr_Type = SnmpAdminString
_CfprLsTierDescr_Object = MibTableColumn
cfprLsTierDescr = _CfprLsTierDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 5),
    _CfprLsTierDescr_Type()
)
cfprLsTierDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierDescr.setStatus("current")
_CfprLsTierIntId_Type = SnmpAdminString
_CfprLsTierIntId_Object = MibTableColumn
cfprLsTierIntId = _CfprLsTierIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 6),
    _CfprLsTierIntId_Type()
)
cfprLsTierIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierIntId.setStatus("current")
_CfprLsTierName_Type = SnmpAdminString
_CfprLsTierName_Object = MibTableColumn
cfprLsTierName = _CfprLsTierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 7),
    _CfprLsTierName_Type()
)
cfprLsTierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierName.setStatus("current")
_CfprLsTierPolicyLevel_Type = Gauge32
_CfprLsTierPolicyLevel_Object = MibTableColumn
cfprLsTierPolicyLevel = _CfprLsTierPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 8),
    _CfprLsTierPolicyLevel_Type()
)
cfprLsTierPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierPolicyLevel.setStatus("current")
_CfprLsTierPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsTierPolicyOwner_Object = MibTableColumn
cfprLsTierPolicyOwner = _CfprLsTierPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 9),
    _CfprLsTierPolicyOwner_Type()
)
cfprLsTierPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierPolicyOwner.setStatus("current")
_CfprLsTierSrcTemplName_Type = SnmpAdminString
_CfprLsTierSrcTemplName_Object = MibTableColumn
cfprLsTierSrcTemplName = _CfprLsTierSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 15, 1, 10),
    _CfprLsTierSrcTemplName_Type()
)
cfprLsTierSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsTierSrcTemplName.setStatus("current")
_CfprLsUuidHistoryTable_Object = MibTable
cfprLsUuidHistoryTable = _CfprLsUuidHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 16)
)
if mibBuilder.loadTexts:
    cfprLsUuidHistoryTable.setStatus("current")
_CfprLsUuidHistoryEntry_Object = MibTableRow
cfprLsUuidHistoryEntry = _CfprLsUuidHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 16, 1)
)
cfprLsUuidHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsUuidHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsUuidHistoryEntry.setStatus("current")
_CfprLsUuidHistoryInstanceId_Type = CfprManagedObjectId
_CfprLsUuidHistoryInstanceId_Object = MibTableColumn
cfprLsUuidHistoryInstanceId = _CfprLsUuidHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 16, 1, 1),
    _CfprLsUuidHistoryInstanceId_Type()
)
cfprLsUuidHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsUuidHistoryInstanceId.setStatus("current")
_CfprLsUuidHistoryDn_Type = CfprManagedObjectDn
_CfprLsUuidHistoryDn_Object = MibTableColumn
cfprLsUuidHistoryDn = _CfprLsUuidHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 16, 1, 2),
    _CfprLsUuidHistoryDn_Type()
)
cfprLsUuidHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsUuidHistoryDn.setStatus("current")
_CfprLsUuidHistoryRn_Type = SnmpAdminString
_CfprLsUuidHistoryRn_Object = MibTableColumn
cfprLsUuidHistoryRn = _CfprLsUuidHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 16, 1, 3),
    _CfprLsUuidHistoryRn_Type()
)
cfprLsUuidHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsUuidHistoryRn.setStatus("current")
_CfprLsUuidHistoryOlduuid_Type = SnmpAdminString
_CfprLsUuidHistoryOlduuid_Object = MibTableColumn
cfprLsUuidHistoryOlduuid = _CfprLsUuidHistoryOlduuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 16, 1, 4),
    _CfprLsUuidHistoryOlduuid_Type()
)
cfprLsUuidHistoryOlduuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsUuidHistoryOlduuid.setStatus("current")
_CfprLsVConAssignTable_Object = MibTable
cfprLsVConAssignTable = _CfprLsVConAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17)
)
if mibBuilder.loadTexts:
    cfprLsVConAssignTable.setStatus("current")
_CfprLsVConAssignEntry_Object = MibTableRow
cfprLsVConAssignEntry = _CfprLsVConAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1)
)
cfprLsVConAssignEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsVConAssignInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsVConAssignEntry.setStatus("current")
_CfprLsVConAssignInstanceId_Type = CfprManagedObjectId
_CfprLsVConAssignInstanceId_Object = MibTableColumn
cfprLsVConAssignInstanceId = _CfprLsVConAssignInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 1),
    _CfprLsVConAssignInstanceId_Type()
)
cfprLsVConAssignInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsVConAssignInstanceId.setStatus("current")
_CfprLsVConAssignDn_Type = CfprManagedObjectDn
_CfprLsVConAssignDn_Object = MibTableColumn
cfprLsVConAssignDn = _CfprLsVConAssignDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 2),
    _CfprLsVConAssignDn_Type()
)
cfprLsVConAssignDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVConAssignDn.setStatus("current")
_CfprLsVConAssignRn_Type = SnmpAdminString
_CfprLsVConAssignRn_Object = MibTableColumn
cfprLsVConAssignRn = _CfprLsVConAssignRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 3),
    _CfprLsVConAssignRn_Type()
)
cfprLsVConAssignRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVConAssignRn.setStatus("current")
_CfprLsVConAssignAdminVcon_Type = SnmpAdminString
_CfprLsVConAssignAdminVcon_Object = MibTableColumn
cfprLsVConAssignAdminVcon = _CfprLsVConAssignAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 4),
    _CfprLsVConAssignAdminVcon_Type()
)
cfprLsVConAssignAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVConAssignAdminVcon.setStatus("current")
_CfprLsVConAssignOrder_Type = Gauge32
_CfprLsVConAssignOrder_Object = MibTableColumn
cfprLsVConAssignOrder = _CfprLsVConAssignOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 5),
    _CfprLsVConAssignOrder_Type()
)
cfprLsVConAssignOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVConAssignOrder.setStatus("current")
_CfprLsVConAssignTransport_Type = CfprFabricVConTransportPref
_CfprLsVConAssignTransport_Object = MibTableColumn
cfprLsVConAssignTransport = _CfprLsVConAssignTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 6),
    _CfprLsVConAssignTransport_Type()
)
cfprLsVConAssignTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVConAssignTransport.setStatus("current")
_CfprLsVConAssignVnicName_Type = SnmpAdminString
_CfprLsVConAssignVnicName_Object = MibTableColumn
cfprLsVConAssignVnicName = _CfprLsVConAssignVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 17, 1, 7),
    _CfprLsVConAssignVnicName_Type()
)
cfprLsVConAssignVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVConAssignVnicName.setStatus("current")
_CfprLsVersionBehTable_Object = MibTable
cfprLsVersionBehTable = _CfprLsVersionBehTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18)
)
if mibBuilder.loadTexts:
    cfprLsVersionBehTable.setStatus("current")
_CfprLsVersionBehEntry_Object = MibTableRow
cfprLsVersionBehEntry = _CfprLsVersionBehEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1)
)
cfprLsVersionBehEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsVersionBehInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsVersionBehEntry.setStatus("current")
_CfprLsVersionBehInstanceId_Type = CfprManagedObjectId
_CfprLsVersionBehInstanceId_Object = MibTableColumn
cfprLsVersionBehInstanceId = _CfprLsVersionBehInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 1),
    _CfprLsVersionBehInstanceId_Type()
)
cfprLsVersionBehInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsVersionBehInstanceId.setStatus("current")
_CfprLsVersionBehDn_Type = CfprManagedObjectDn
_CfprLsVersionBehDn_Object = MibTableColumn
cfprLsVersionBehDn = _CfprLsVersionBehDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 2),
    _CfprLsVersionBehDn_Type()
)
cfprLsVersionBehDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVersionBehDn.setStatus("current")
_CfprLsVersionBehRn_Type = SnmpAdminString
_CfprLsVersionBehRn_Object = MibTableColumn
cfprLsVersionBehRn = _CfprLsVersionBehRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 3),
    _CfprLsVersionBehRn_Type()
)
cfprLsVersionBehRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVersionBehRn.setStatus("current")
_CfprLsVersionBehPciEnum_Type = CfprVnicOrderScheme
_CfprLsVersionBehPciEnum_Object = MibTableColumn
cfprLsVersionBehPciEnum = _CfprLsVersionBehPciEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 4),
    _CfprLsVersionBehPciEnum_Type()
)
cfprLsVersionBehPciEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVersionBehPciEnum.setStatus("current")
_CfprLsVersionBehVconMap_Type = CfprFabricVConMappingScheme
_CfprLsVersionBehVconMap_Object = MibTableColumn
cfprLsVersionBehVconMap = _CfprLsVersionBehVconMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 5),
    _CfprLsVersionBehVconMap_Type()
)
cfprLsVersionBehVconMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVersionBehVconMap.setStatus("current")
_CfprLsVersionBehVnicMap_Type = CfprVnicMezzMappingScheme
_CfprLsVersionBehVnicMap_Object = MibTableColumn
cfprLsVersionBehVnicMap = _CfprLsVersionBehVnicMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 6),
    _CfprLsVersionBehVnicMap_Type()
)
cfprLsVersionBehVnicMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVersionBehVnicMap.setStatus("current")
_CfprLsVersionBehVnicOrder_Type = CfprVnicPlacement
_CfprLsVersionBehVnicOrder_Object = MibTableColumn
cfprLsVersionBehVnicOrder = _CfprLsVersionBehVnicOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 18, 1, 7),
    _CfprLsVersionBehVnicOrder_Type()
)
cfprLsVersionBehVnicOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsVersionBehVnicOrder.setStatus("current")
_CfprLsZoneInitiatorMemberTable_Object = MibTable
cfprLsZoneInitiatorMemberTable = _CfprLsZoneInitiatorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19)
)
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberTable.setStatus("current")
_CfprLsZoneInitiatorMemberEntry_Object = MibTableRow
cfprLsZoneInitiatorMemberEntry = _CfprLsZoneInitiatorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1)
)
cfprLsZoneInitiatorMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsZoneInitiatorMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberEntry.setStatus("current")
_CfprLsZoneInitiatorMemberInstanceId_Type = CfprManagedObjectId
_CfprLsZoneInitiatorMemberInstanceId_Object = MibTableColumn
cfprLsZoneInitiatorMemberInstanceId = _CfprLsZoneInitiatorMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 1),
    _CfprLsZoneInitiatorMemberInstanceId_Type()
)
cfprLsZoneInitiatorMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberInstanceId.setStatus("current")
_CfprLsZoneInitiatorMemberDn_Type = CfprManagedObjectDn
_CfprLsZoneInitiatorMemberDn_Object = MibTableColumn
cfprLsZoneInitiatorMemberDn = _CfprLsZoneInitiatorMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 2),
    _CfprLsZoneInitiatorMemberDn_Type()
)
cfprLsZoneInitiatorMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberDn.setStatus("current")
_CfprLsZoneInitiatorMemberRn_Type = SnmpAdminString
_CfprLsZoneInitiatorMemberRn_Object = MibTableColumn
cfprLsZoneInitiatorMemberRn = _CfprLsZoneInitiatorMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 3),
    _CfprLsZoneInitiatorMemberRn_Type()
)
cfprLsZoneInitiatorMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberRn.setStatus("current")
_CfprLsZoneInitiatorMemberEpDn_Type = SnmpAdminString
_CfprLsZoneInitiatorMemberEpDn_Object = MibTableColumn
cfprLsZoneInitiatorMemberEpDn = _CfprLsZoneInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 4),
    _CfprLsZoneInitiatorMemberEpDn_Type()
)
cfprLsZoneInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberEpDn.setStatus("current")
_CfprLsZoneInitiatorMemberName_Type = SnmpAdminString
_CfprLsZoneInitiatorMemberName_Object = MibTableColumn
cfprLsZoneInitiatorMemberName = _CfprLsZoneInitiatorMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 5),
    _CfprLsZoneInitiatorMemberName_Type()
)
cfprLsZoneInitiatorMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberName.setStatus("current")
_CfprLsZoneInitiatorMemberUsrLbl_Type = SnmpAdminString
_CfprLsZoneInitiatorMemberUsrLbl_Object = MibTableColumn
cfprLsZoneInitiatorMemberUsrLbl = _CfprLsZoneInitiatorMemberUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 6),
    _CfprLsZoneInitiatorMemberUsrLbl_Type()
)
cfprLsZoneInitiatorMemberUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberUsrLbl.setStatus("current")
_CfprLsZoneInitiatorMemberWwpn_Type = Unsigned64
_CfprLsZoneInitiatorMemberWwpn_Object = MibTableColumn
cfprLsZoneInitiatorMemberWwpn = _CfprLsZoneInitiatorMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 19, 1, 7),
    _CfprLsZoneInitiatorMemberWwpn_Type()
)
cfprLsZoneInitiatorMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneInitiatorMemberWwpn.setStatus("current")
_CfprLsZoneTargetMemberTable_Object = MibTable
cfprLsZoneTargetMemberTable = _CfprLsZoneTargetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20)
)
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberTable.setStatus("current")
_CfprLsZoneTargetMemberEntry_Object = MibTableRow
cfprLsZoneTargetMemberEntry = _CfprLsZoneTargetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1)
)
cfprLsZoneTargetMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LS-MIB", "cfprLsZoneTargetMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberEntry.setStatus("current")
_CfprLsZoneTargetMemberInstanceId_Type = CfprManagedObjectId
_CfprLsZoneTargetMemberInstanceId_Object = MibTableColumn
cfprLsZoneTargetMemberInstanceId = _CfprLsZoneTargetMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 1),
    _CfprLsZoneTargetMemberInstanceId_Type()
)
cfprLsZoneTargetMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberInstanceId.setStatus("current")
_CfprLsZoneTargetMemberDn_Type = CfprManagedObjectDn
_CfprLsZoneTargetMemberDn_Object = MibTableColumn
cfprLsZoneTargetMemberDn = _CfprLsZoneTargetMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 2),
    _CfprLsZoneTargetMemberDn_Type()
)
cfprLsZoneTargetMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberDn.setStatus("current")
_CfprLsZoneTargetMemberRn_Type = SnmpAdminString
_CfprLsZoneTargetMemberRn_Object = MibTableColumn
cfprLsZoneTargetMemberRn = _CfprLsZoneTargetMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 3),
    _CfprLsZoneTargetMemberRn_Type()
)
cfprLsZoneTargetMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberRn.setStatus("current")
_CfprLsZoneTargetMemberEpDn_Type = SnmpAdminString
_CfprLsZoneTargetMemberEpDn_Object = MibTableColumn
cfprLsZoneTargetMemberEpDn = _CfprLsZoneTargetMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 4),
    _CfprLsZoneTargetMemberEpDn_Type()
)
cfprLsZoneTargetMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberEpDn.setStatus("current")
_CfprLsZoneTargetMemberName_Type = SnmpAdminString
_CfprLsZoneTargetMemberName_Object = MibTableColumn
cfprLsZoneTargetMemberName = _CfprLsZoneTargetMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 5),
    _CfprLsZoneTargetMemberName_Type()
)
cfprLsZoneTargetMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberName.setStatus("current")
_CfprLsZoneTargetMemberUsrLbl_Type = SnmpAdminString
_CfprLsZoneTargetMemberUsrLbl_Object = MibTableColumn
cfprLsZoneTargetMemberUsrLbl = _CfprLsZoneTargetMemberUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 6),
    _CfprLsZoneTargetMemberUsrLbl_Type()
)
cfprLsZoneTargetMemberUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberUsrLbl.setStatus("current")
_CfprLsZoneTargetMemberWwpn_Type = Unsigned64
_CfprLsZoneTargetMemberWwpn_Object = MibTableColumn
cfprLsZoneTargetMemberWwpn = _CfprLsZoneTargetMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 46, 20, 1, 7),
    _CfprLsZoneTargetMemberWwpn_Type()
)
cfprLsZoneTargetMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsZoneTargetMemberWwpn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-LS-MIB",
    **{"cfprLsObjects": cfprLsObjects,
       "cfprLsAgentPolicyTable": cfprLsAgentPolicyTable,
       "cfprLsAgentPolicyEntry": cfprLsAgentPolicyEntry,
       "cfprLsAgentPolicyInstanceId": cfprLsAgentPolicyInstanceId,
       "cfprLsAgentPolicyDn": cfprLsAgentPolicyDn,
       "cfprLsAgentPolicyRn": cfprLsAgentPolicyRn,
       "cfprLsAgentPolicyCapability": cfprLsAgentPolicyCapability,
       "cfprLsAgentPolicyDescr": cfprLsAgentPolicyDescr,
       "cfprLsAgentPolicyIntId": cfprLsAgentPolicyIntId,
       "cfprLsAgentPolicyMode": cfprLsAgentPolicyMode,
       "cfprLsAgentPolicyName": cfprLsAgentPolicyName,
       "cfprLsAgentPolicyPolicyLevel": cfprLsAgentPolicyPolicyLevel,
       "cfprLsAgentPolicyPolicyOwner": cfprLsAgentPolicyPolicyOwner,
       "cfprLsBindingTable": cfprLsBindingTable,
       "cfprLsBindingEntry": cfprLsBindingEntry,
       "cfprLsBindingInstanceId": cfprLsBindingInstanceId,
       "cfprLsBindingDn": cfprLsBindingDn,
       "cfprLsBindingRn": cfprLsBindingRn,
       "cfprLsBindingAssignedToDn": cfprLsBindingAssignedToDn,
       "cfprLsBindingComputeEpDn": cfprLsBindingComputeEpDn,
       "cfprLsBindingIssues": cfprLsBindingIssues,
       "cfprLsBindingName": cfprLsBindingName,
       "cfprLsBindingOperState": cfprLsBindingOperState,
       "cfprLsBindingPnDn": cfprLsBindingPnDn,
       "cfprLsBindingRestrictMigration": cfprLsBindingRestrictMigration,
       "cfprLsFcLocaleTable": cfprLsFcLocaleTable,
       "cfprLsFcLocaleEntry": cfprLsFcLocaleEntry,
       "cfprLsFcLocaleInstanceId": cfprLsFcLocaleInstanceId,
       "cfprLsFcLocaleDn": cfprLsFcLocaleDn,
       "cfprLsFcLocaleRn": cfprLsFcLocaleRn,
       "cfprLsFcLocaleSwitchId": cfprLsFcLocaleSwitchId,
       "cfprLsFcZoneTable": cfprLsFcZoneTable,
       "cfprLsFcZoneEntry": cfprLsFcZoneEntry,
       "cfprLsFcZoneInstanceId": cfprLsFcZoneInstanceId,
       "cfprLsFcZoneDn": cfprLsFcZoneDn,
       "cfprLsFcZoneRn": cfprLsFcZoneRn,
       "cfprLsFcZoneAdminState": cfprLsFcZoneAdminState,
       "cfprLsFcZoneId": cfprLsFcZoneId,
       "cfprLsFcZoneIdentity": cfprLsFcZoneIdentity,
       "cfprLsFcZoneIniName": cfprLsFcZoneIniName,
       "cfprLsFcZoneName": cfprLsFcZoneName,
       "cfprLsFcZoneOperState": cfprLsFcZoneOperState,
       "cfprLsFcZonePeerDn": cfprLsFcZonePeerDn,
       "cfprLsFcZoneSwitchId": cfprLsFcZoneSwitchId,
       "cfprLsFcZoneUsrLbl": cfprLsFcZoneUsrLbl,
       "cfprLsFcZoneVnetId": cfprLsFcZoneVnetId,
       "cfprLsFcZoneZoningType": cfprLsFcZoneZoningType,
       "cfprLsFcZoneGroupTable": cfprLsFcZoneGroupTable,
       "cfprLsFcZoneGroupEntry": cfprLsFcZoneGroupEntry,
       "cfprLsFcZoneGroupInstanceId": cfprLsFcZoneGroupInstanceId,
       "cfprLsFcZoneGroupDn": cfprLsFcZoneGroupDn,
       "cfprLsFcZoneGroupRn": cfprLsFcZoneGroupRn,
       "cfprLsFcZoneGroupId": cfprLsFcZoneGroupId,
       "cfprLsFcZoneGroupName": cfprLsFcZoneGroupName,
       "cfprLsFcZoneGroupSwitchId": cfprLsFcZoneGroupSwitchId,
       "cfprLsIssuesTable": cfprLsIssuesTable,
       "cfprLsIssuesEntry": cfprLsIssuesEntry,
       "cfprLsIssuesInstanceId": cfprLsIssuesInstanceId,
       "cfprLsIssuesDn": cfprLsIssuesDn,
       "cfprLsIssuesRn": cfprLsIssuesRn,
       "cfprLsIssuesConfigWarnings": cfprLsIssuesConfigWarnings,
       "cfprLsIssuesIscsiConfigIssues": cfprLsIssuesIscsiConfigIssues,
       "cfprLsIssuesNetworkConfigIssues": cfprLsIssuesNetworkConfigIssues,
       "cfprLsIssuesServerConfigIssues": cfprLsIssuesServerConfigIssues,
       "cfprLsIssuesStorageConfigIssues": cfprLsIssuesStorageConfigIssues,
       "cfprLsIssuesVnicConfigIssues": cfprLsIssuesVnicConfigIssues,
       "cfprLsPowerTable": cfprLsPowerTable,
       "cfprLsPowerEntry": cfprLsPowerEntry,
       "cfprLsPowerInstanceId": cfprLsPowerInstanceId,
       "cfprLsPowerDn": cfprLsPowerDn,
       "cfprLsPowerRn": cfprLsPowerRn,
       "cfprLsPowerState": cfprLsPowerState,
       "cfprLsPowerAllocPolicyName": cfprLsPowerAllocPolicyName,
       "cfprLsRequirementTable": cfprLsRequirementTable,
       "cfprLsRequirementEntry": cfprLsRequirementEntry,
       "cfprLsRequirementInstanceId": cfprLsRequirementInstanceId,
       "cfprLsRequirementDn": cfprLsRequirementDn,
       "cfprLsRequirementRn": cfprLsRequirementRn,
       "cfprLsRequirementAssignedToDn": cfprLsRequirementAssignedToDn,
       "cfprLsRequirementComputeEpDn": cfprLsRequirementComputeEpDn,
       "cfprLsRequirementIssues": cfprLsRequirementIssues,
       "cfprLsRequirementName": cfprLsRequirementName,
       "cfprLsRequirementOperName": cfprLsRequirementOperName,
       "cfprLsRequirementOperState": cfprLsRequirementOperState,
       "cfprLsRequirementPnDn": cfprLsRequirementPnDn,
       "cfprLsRequirementPnPoolDn": cfprLsRequirementPnPoolDn,
       "cfprLsRequirementQualifier": cfprLsRequirementQualifier,
       "cfprLsRequirementRestrictMigration": cfprLsRequirementRestrictMigration,
       "cfprLsServerTable": cfprLsServerTable,
       "cfprLsServerEntry": cfprLsServerEntry,
       "cfprLsServerInstanceId": cfprLsServerInstanceId,
       "cfprLsServerDn": cfprLsServerDn,
       "cfprLsServerRn": cfprLsServerRn,
       "cfprLsServerAgentPolicyName": cfprLsServerAgentPolicyName,
       "cfprLsServerAssignState": cfprLsServerAssignState,
       "cfprLsServerAssocState": cfprLsServerAssocState,
       "cfprLsServerBiosProfileName": cfprLsServerBiosProfileName,
       "cfprLsServerBootPolicyName": cfprLsServerBootPolicyName,
       "cfprLsServerConfigQualifier": cfprLsServerConfigQualifier,
       "cfprLsServerConfigState": cfprLsServerConfigState,
       "cfprLsServerDescr": cfprLsServerDescr,
       "cfprLsServerDynamicConPolicyName": cfprLsServerDynamicConPolicyName,
       "cfprLsServerExtIPPoolName": cfprLsServerExtIPPoolName,
       "cfprLsServerExtIPState": cfprLsServerExtIPState,
       "cfprLsServerFltAggr": cfprLsServerFltAggr,
       "cfprLsServerFsmDescr": cfprLsServerFsmDescr,
       "cfprLsServerFsmFlags": cfprLsServerFsmFlags,
       "cfprLsServerFsmPrev": cfprLsServerFsmPrev,
       "cfprLsServerFsmProgr": cfprLsServerFsmProgr,
       "cfprLsServerFsmRmtInvErrCode": cfprLsServerFsmRmtInvErrCode,
       "cfprLsServerFsmRmtInvErrDescr": cfprLsServerFsmRmtInvErrDescr,
       "cfprLsServerFsmRmtInvRslt": cfprLsServerFsmRmtInvRslt,
       "cfprLsServerFsmStageDescr": cfprLsServerFsmStageDescr,
       "cfprLsServerFsmStamp": cfprLsServerFsmStamp,
       "cfprLsServerFsmStatus": cfprLsServerFsmStatus,
       "cfprLsServerFsmTry": cfprLsServerFsmTry,
       "cfprLsServerHostFwPolicyName": cfprLsServerHostFwPolicyName,
       "cfprLsServerIdentPoolName": cfprLsServerIdentPoolName,
       "cfprLsServerIntId": cfprLsServerIntId,
       "cfprLsServerKvmMgmtPolicyName": cfprLsServerKvmMgmtPolicyName,
       "cfprLsServerLocalDiskPolicyName": cfprLsServerLocalDiskPolicyName,
       "cfprLsServerMaintPolicyName": cfprLsServerMaintPolicyName,
       "cfprLsServerMgmtAccessPolicyName": cfprLsServerMgmtAccessPolicyName,
       "cfprLsServerMgmtFwPolicyName": cfprLsServerMgmtFwPolicyName,
       "cfprLsServerName": cfprLsServerName,
       "cfprLsServerOperBiosProfileName": cfprLsServerOperBiosProfileName,
       "cfprLsServerOperBootPolicyName": cfprLsServerOperBootPolicyName,
       "cfprLsServerOperDynamicConPolicyName": cfprLsServerOperDynamicConPolicyName,
       "cfprLsServerOperExtIPPoolName": cfprLsServerOperExtIPPoolName,
       "cfprLsServerOperHostFwPolicyName": cfprLsServerOperHostFwPolicyName,
       "cfprLsServerOperIdentPoolName": cfprLsServerOperIdentPoolName,
       "cfprLsServerOperKvmMgmtPolicyName": cfprLsServerOperKvmMgmtPolicyName,
       "cfprLsServerOperLocalDiskPolicyName": cfprLsServerOperLocalDiskPolicyName,
       "cfprLsServerOperMaintPolicyName": cfprLsServerOperMaintPolicyName,
       "cfprLsServerOperMgmtAccessPolicyName": cfprLsServerOperMgmtAccessPolicyName,
       "cfprLsServerOperMgmtFwPolicyName": cfprLsServerOperMgmtFwPolicyName,
       "cfprLsServerOperPowerPolicyName": cfprLsServerOperPowerPolicyName,
       "cfprLsServerOperScrubPolicyName": cfprLsServerOperScrubPolicyName,
       "cfprLsServerOperSolPolicyName": cfprLsServerOperSolPolicyName,
       "cfprLsServerOperSrcTemplName": cfprLsServerOperSrcTemplName,
       "cfprLsServerOperState": cfprLsServerOperState,
       "cfprLsServerOperStatsPolicyName": cfprLsServerOperStatsPolicyName,
       "cfprLsServerOperVconProfileName": cfprLsServerOperVconProfileName,
       "cfprLsServerOperVmediaPolicyName": cfprLsServerOperVmediaPolicyName,
       "cfprLsServerOwner": cfprLsServerOwner,
       "cfprLsServerPnDn": cfprLsServerPnDn,
       "cfprLsServerPolicyLevel": cfprLsServerPolicyLevel,
       "cfprLsServerPolicyOwner": cfprLsServerPolicyOwner,
       "cfprLsServerPowerPolicyName": cfprLsServerPowerPolicyName,
       "cfprLsServerResolveRemote": cfprLsServerResolveRemote,
       "cfprLsServerScrubPolicyName": cfprLsServerScrubPolicyName,
       "cfprLsServerSolPolicyName": cfprLsServerSolPolicyName,
       "cfprLsServerSrcTemplName": cfprLsServerSrcTemplName,
       "cfprLsServerStatsPolicyName": cfprLsServerStatsPolicyName,
       "cfprLsServerSvnicConfig": cfprLsServerSvnicConfig,
       "cfprLsServerType": cfprLsServerType,
       "cfprLsServerUsrLbl": cfprLsServerUsrLbl,
       "cfprLsServerUuid": cfprLsServerUuid,
       "cfprLsServerUuidSuffix": cfprLsServerUuidSuffix,
       "cfprLsServerVconProfileName": cfprLsServerVconProfileName,
       "cfprLsServerVmediaPolicyName": cfprLsServerVmediaPolicyName,
       "cfprLsServerDeployType": cfprLsServerDeployType,
       "cfprLsServerAssocCtxTable": cfprLsServerAssocCtxTable,
       "cfprLsServerAssocCtxEntry": cfprLsServerAssocCtxEntry,
       "cfprLsServerAssocCtxInstanceId": cfprLsServerAssocCtxInstanceId,
       "cfprLsServerAssocCtxDn": cfprLsServerAssocCtxDn,
       "cfprLsServerAssocCtxRn": cfprLsServerAssocCtxRn,
       "cfprLsServerExtensionTable": cfprLsServerExtensionTable,
       "cfprLsServerExtensionEntry": cfprLsServerExtensionEntry,
       "cfprLsServerExtensionInstanceId": cfprLsServerExtensionInstanceId,
       "cfprLsServerExtensionDn": cfprLsServerExtensionDn,
       "cfprLsServerExtensionRn": cfprLsServerExtensionRn,
       "cfprLsServerExtensionGuid": cfprLsServerExtensionGuid,
       "cfprLsServerExtensionVersion": cfprLsServerExtensionVersion,
       "cfprLsServerFsmTable": cfprLsServerFsmTable,
       "cfprLsServerFsmEntry": cfprLsServerFsmEntry,
       "cfprLsServerFsmInstanceId": cfprLsServerFsmInstanceId,
       "cfprLsServerFsmDn": cfprLsServerFsmDn,
       "cfprLsServerFsmRn": cfprLsServerFsmRn,
       "cfprLsServerFsmCompletionTime": cfprLsServerFsmCompletionTime,
       "cfprLsServerFsmCurrentFsm": cfprLsServerFsmCurrentFsm,
       "cfprLsServerFsmDescrData": cfprLsServerFsmDescrData,
       "cfprLsServerFsmFsmStatus": cfprLsServerFsmFsmStatus,
       "cfprLsServerFsmProgress": cfprLsServerFsmProgress,
       "cfprLsServerFsmRmtErrCode": cfprLsServerFsmRmtErrCode,
       "cfprLsServerFsmRmtErrDescr": cfprLsServerFsmRmtErrDescr,
       "cfprLsServerFsmRmtRslt": cfprLsServerFsmRmtRslt,
       "cfprLsServerFsmStageTable": cfprLsServerFsmStageTable,
       "cfprLsServerFsmStageEntry": cfprLsServerFsmStageEntry,
       "cfprLsServerFsmStageInstanceId": cfprLsServerFsmStageInstanceId,
       "cfprLsServerFsmStageDn": cfprLsServerFsmStageDn,
       "cfprLsServerFsmStageRn": cfprLsServerFsmStageRn,
       "cfprLsServerFsmStageDescrData": cfprLsServerFsmStageDescrData,
       "cfprLsServerFsmStageLastUpdateTime": cfprLsServerFsmStageLastUpdateTime,
       "cfprLsServerFsmStageName": cfprLsServerFsmStageName,
       "cfprLsServerFsmStageOrder": cfprLsServerFsmStageOrder,
       "cfprLsServerFsmStageRetry": cfprLsServerFsmStageRetry,
       "cfprLsServerFsmStageStageStatus": cfprLsServerFsmStageStageStatus,
       "cfprLsServerFsmTaskTable": cfprLsServerFsmTaskTable,
       "cfprLsServerFsmTaskEntry": cfprLsServerFsmTaskEntry,
       "cfprLsServerFsmTaskInstanceId": cfprLsServerFsmTaskInstanceId,
       "cfprLsServerFsmTaskDn": cfprLsServerFsmTaskDn,
       "cfprLsServerFsmTaskRn": cfprLsServerFsmTaskRn,
       "cfprLsServerFsmTaskCompletion": cfprLsServerFsmTaskCompletion,
       "cfprLsServerFsmTaskFlags": cfprLsServerFsmTaskFlags,
       "cfprLsServerFsmTaskItem": cfprLsServerFsmTaskItem,
       "cfprLsServerFsmTaskSeqId": cfprLsServerFsmTaskSeqId,
       "cfprLsTierTable": cfprLsTierTable,
       "cfprLsTierEntry": cfprLsTierEntry,
       "cfprLsTierInstanceId": cfprLsTierInstanceId,
       "cfprLsTierDn": cfprLsTierDn,
       "cfprLsTierRn": cfprLsTierRn,
       "cfprLsTierApply": cfprLsTierApply,
       "cfprLsTierDescr": cfprLsTierDescr,
       "cfprLsTierIntId": cfprLsTierIntId,
       "cfprLsTierName": cfprLsTierName,
       "cfprLsTierPolicyLevel": cfprLsTierPolicyLevel,
       "cfprLsTierPolicyOwner": cfprLsTierPolicyOwner,
       "cfprLsTierSrcTemplName": cfprLsTierSrcTemplName,
       "cfprLsUuidHistoryTable": cfprLsUuidHistoryTable,
       "cfprLsUuidHistoryEntry": cfprLsUuidHistoryEntry,
       "cfprLsUuidHistoryInstanceId": cfprLsUuidHistoryInstanceId,
       "cfprLsUuidHistoryDn": cfprLsUuidHistoryDn,
       "cfprLsUuidHistoryRn": cfprLsUuidHistoryRn,
       "cfprLsUuidHistoryOlduuid": cfprLsUuidHistoryOlduuid,
       "cfprLsVConAssignTable": cfprLsVConAssignTable,
       "cfprLsVConAssignEntry": cfprLsVConAssignEntry,
       "cfprLsVConAssignInstanceId": cfprLsVConAssignInstanceId,
       "cfprLsVConAssignDn": cfprLsVConAssignDn,
       "cfprLsVConAssignRn": cfprLsVConAssignRn,
       "cfprLsVConAssignAdminVcon": cfprLsVConAssignAdminVcon,
       "cfprLsVConAssignOrder": cfprLsVConAssignOrder,
       "cfprLsVConAssignTransport": cfprLsVConAssignTransport,
       "cfprLsVConAssignVnicName": cfprLsVConAssignVnicName,
       "cfprLsVersionBehTable": cfprLsVersionBehTable,
       "cfprLsVersionBehEntry": cfprLsVersionBehEntry,
       "cfprLsVersionBehInstanceId": cfprLsVersionBehInstanceId,
       "cfprLsVersionBehDn": cfprLsVersionBehDn,
       "cfprLsVersionBehRn": cfprLsVersionBehRn,
       "cfprLsVersionBehPciEnum": cfprLsVersionBehPciEnum,
       "cfprLsVersionBehVconMap": cfprLsVersionBehVconMap,
       "cfprLsVersionBehVnicMap": cfprLsVersionBehVnicMap,
       "cfprLsVersionBehVnicOrder": cfprLsVersionBehVnicOrder,
       "cfprLsZoneInitiatorMemberTable": cfprLsZoneInitiatorMemberTable,
       "cfprLsZoneInitiatorMemberEntry": cfprLsZoneInitiatorMemberEntry,
       "cfprLsZoneInitiatorMemberInstanceId": cfprLsZoneInitiatorMemberInstanceId,
       "cfprLsZoneInitiatorMemberDn": cfprLsZoneInitiatorMemberDn,
       "cfprLsZoneInitiatorMemberRn": cfprLsZoneInitiatorMemberRn,
       "cfprLsZoneInitiatorMemberEpDn": cfprLsZoneInitiatorMemberEpDn,
       "cfprLsZoneInitiatorMemberName": cfprLsZoneInitiatorMemberName,
       "cfprLsZoneInitiatorMemberUsrLbl": cfprLsZoneInitiatorMemberUsrLbl,
       "cfprLsZoneInitiatorMemberWwpn": cfprLsZoneInitiatorMemberWwpn,
       "cfprLsZoneTargetMemberTable": cfprLsZoneTargetMemberTable,
       "cfprLsZoneTargetMemberEntry": cfprLsZoneTargetMemberEntry,
       "cfprLsZoneTargetMemberInstanceId": cfprLsZoneTargetMemberInstanceId,
       "cfprLsZoneTargetMemberDn": cfprLsZoneTargetMemberDn,
       "cfprLsZoneTargetMemberRn": cfprLsZoneTargetMemberRn,
       "cfprLsZoneTargetMemberEpDn": cfprLsZoneTargetMemberEpDn,
       "cfprLsZoneTargetMemberName": cfprLsZoneTargetMemberName,
       "cfprLsZoneTargetMemberUsrLbl": cfprLsZoneTargetMemberUsrLbl,
       "cfprLsZoneTargetMemberWwpn": cfprLsZoneTargetMemberWwpn}
)
