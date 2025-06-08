# SNMP MIB module (CISCO-FIREPOWER-AP-LS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-LS-MIB.mib
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
 CfprApFabricVConMappingScheme,
 CfprApFabricVConTransportPref,
 CfprApFsmCompletion,
 CfprApFsmFsmStageStatus,
 CfprApLsAgentCapability,
 CfprApLsAgentMode,
 CfprApLsApply,
 CfprApLsAssignment,
 CfprApLsAssocState,
 CfprApLsComputeBindingOperState,
 CfprApLsConfigIssues,
 CfprApLsConfigState,
 CfprApLsConfigWarnings,
 CfprApLsFcZoneGroupSwitchId,
 CfprApLsFcZoneState,
 CfprApLsOperState,
 CfprApLsOwner,
 CfprApLsPowerState,
 CfprApLsResolveFromRemoteServer,
 CfprApLsServerFsmCurrentFsm,
 CfprApLsServerFsmStageName,
 CfprApLsServerFsmTaskFlags,
 CfprApLsServerFsmTaskItem,
 CfprApLsType,
 CfprApNetworkConfigIssues,
 CfprApNetworkSwitchId,
 CfprApPolicyPolicyOwner,
 CfprApServerConfigIssues,
 CfprApStorageConfigIssues,
 CfprApStorageFcZoningType,
 CfprApVnicConfigIssues,
 CfprApVnicExternalMgmtIPMode,
 CfprApVnicIScsiConfigIssues,
 CfprApVnicMezzMappingScheme,
 CfprApVnicOrderScheme,
 CfprApVnicPlacement) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFabricVConMappingScheme",
    "CfprApFabricVConTransportPref",
    "CfprApFsmCompletion",
    "CfprApFsmFsmStageStatus",
    "CfprApLsAgentCapability",
    "CfprApLsAgentMode",
    "CfprApLsApply",
    "CfprApLsAssignment",
    "CfprApLsAssocState",
    "CfprApLsComputeBindingOperState",
    "CfprApLsConfigIssues",
    "CfprApLsConfigState",
    "CfprApLsConfigWarnings",
    "CfprApLsFcZoneGroupSwitchId",
    "CfprApLsFcZoneState",
    "CfprApLsOperState",
    "CfprApLsOwner",
    "CfprApLsPowerState",
    "CfprApLsResolveFromRemoteServer",
    "CfprApLsServerFsmCurrentFsm",
    "CfprApLsServerFsmStageName",
    "CfprApLsServerFsmTaskFlags",
    "CfprApLsServerFsmTaskItem",
    "CfprApLsType",
    "CfprApNetworkConfigIssues",
    "CfprApNetworkSwitchId",
    "CfprApPolicyPolicyOwner",
    "CfprApServerConfigIssues",
    "CfprApStorageConfigIssues",
    "CfprApStorageFcZoningType",
    "CfprApVnicConfigIssues",
    "CfprApVnicExternalMgmtIPMode",
    "CfprApVnicIScsiConfigIssues",
    "CfprApVnicMezzMappingScheme",
    "CfprApVnicOrderScheme",
    "CfprApVnicPlacement")

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

cfprApLsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApLsAgentPolicyTable_Object = MibTable
cfprApLsAgentPolicyTable = _CfprApLsAgentPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1)
)
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyTable.setStatus("current")
_CfprApLsAgentPolicyEntry_Object = MibTableRow
cfprApLsAgentPolicyEntry = _CfprApLsAgentPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1)
)
cfprApLsAgentPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsAgentPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyEntry.setStatus("current")
_CfprApLsAgentPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApLsAgentPolicyInstanceId_Object = MibTableColumn
cfprApLsAgentPolicyInstanceId = _CfprApLsAgentPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 1),
    _CfprApLsAgentPolicyInstanceId_Type()
)
cfprApLsAgentPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyInstanceId.setStatus("current")
_CfprApLsAgentPolicyDn_Type = CfprApManagedObjectDn
_CfprApLsAgentPolicyDn_Object = MibTableColumn
cfprApLsAgentPolicyDn = _CfprApLsAgentPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 2),
    _CfprApLsAgentPolicyDn_Type()
)
cfprApLsAgentPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyDn.setStatus("current")
_CfprApLsAgentPolicyRn_Type = SnmpAdminString
_CfprApLsAgentPolicyRn_Object = MibTableColumn
cfprApLsAgentPolicyRn = _CfprApLsAgentPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 3),
    _CfprApLsAgentPolicyRn_Type()
)
cfprApLsAgentPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyRn.setStatus("current")
_CfprApLsAgentPolicyCapability_Type = CfprApLsAgentCapability
_CfprApLsAgentPolicyCapability_Object = MibTableColumn
cfprApLsAgentPolicyCapability = _CfprApLsAgentPolicyCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 4),
    _CfprApLsAgentPolicyCapability_Type()
)
cfprApLsAgentPolicyCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyCapability.setStatus("current")
_CfprApLsAgentPolicyDescr_Type = SnmpAdminString
_CfprApLsAgentPolicyDescr_Object = MibTableColumn
cfprApLsAgentPolicyDescr = _CfprApLsAgentPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 5),
    _CfprApLsAgentPolicyDescr_Type()
)
cfprApLsAgentPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyDescr.setStatus("current")
_CfprApLsAgentPolicyIntId_Type = SnmpAdminString
_CfprApLsAgentPolicyIntId_Object = MibTableColumn
cfprApLsAgentPolicyIntId = _CfprApLsAgentPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 6),
    _CfprApLsAgentPolicyIntId_Type()
)
cfprApLsAgentPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyIntId.setStatus("current")
_CfprApLsAgentPolicyMode_Type = CfprApLsAgentMode
_CfprApLsAgentPolicyMode_Object = MibTableColumn
cfprApLsAgentPolicyMode = _CfprApLsAgentPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 7),
    _CfprApLsAgentPolicyMode_Type()
)
cfprApLsAgentPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyMode.setStatus("current")
_CfprApLsAgentPolicyName_Type = SnmpAdminString
_CfprApLsAgentPolicyName_Object = MibTableColumn
cfprApLsAgentPolicyName = _CfprApLsAgentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 8),
    _CfprApLsAgentPolicyName_Type()
)
cfprApLsAgentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyName.setStatus("current")
_CfprApLsAgentPolicyPolicyLevel_Type = Gauge32
_CfprApLsAgentPolicyPolicyLevel_Object = MibTableColumn
cfprApLsAgentPolicyPolicyLevel = _CfprApLsAgentPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 9),
    _CfprApLsAgentPolicyPolicyLevel_Type()
)
cfprApLsAgentPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyPolicyLevel.setStatus("current")
_CfprApLsAgentPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsAgentPolicyPolicyOwner_Object = MibTableColumn
cfprApLsAgentPolicyPolicyOwner = _CfprApLsAgentPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 1, 1, 10),
    _CfprApLsAgentPolicyPolicyOwner_Type()
)
cfprApLsAgentPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsAgentPolicyPolicyOwner.setStatus("current")
_CfprApLsBindingTable_Object = MibTable
cfprApLsBindingTable = _CfprApLsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2)
)
if mibBuilder.loadTexts:
    cfprApLsBindingTable.setStatus("current")
_CfprApLsBindingEntry_Object = MibTableRow
cfprApLsBindingEntry = _CfprApLsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1)
)
cfprApLsBindingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsBindingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsBindingEntry.setStatus("current")
_CfprApLsBindingInstanceId_Type = CfprApManagedObjectId
_CfprApLsBindingInstanceId_Object = MibTableColumn
cfprApLsBindingInstanceId = _CfprApLsBindingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 1),
    _CfprApLsBindingInstanceId_Type()
)
cfprApLsBindingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsBindingInstanceId.setStatus("current")
_CfprApLsBindingDn_Type = CfprApManagedObjectDn
_CfprApLsBindingDn_Object = MibTableColumn
cfprApLsBindingDn = _CfprApLsBindingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 2),
    _CfprApLsBindingDn_Type()
)
cfprApLsBindingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingDn.setStatus("current")
_CfprApLsBindingRn_Type = SnmpAdminString
_CfprApLsBindingRn_Object = MibTableColumn
cfprApLsBindingRn = _CfprApLsBindingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 3),
    _CfprApLsBindingRn_Type()
)
cfprApLsBindingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingRn.setStatus("current")
_CfprApLsBindingAssignedToDn_Type = SnmpAdminString
_CfprApLsBindingAssignedToDn_Object = MibTableColumn
cfprApLsBindingAssignedToDn = _CfprApLsBindingAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 4),
    _CfprApLsBindingAssignedToDn_Type()
)
cfprApLsBindingAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingAssignedToDn.setStatus("current")
_CfprApLsBindingComputeEpDn_Type = SnmpAdminString
_CfprApLsBindingComputeEpDn_Object = MibTableColumn
cfprApLsBindingComputeEpDn = _CfprApLsBindingComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 5),
    _CfprApLsBindingComputeEpDn_Type()
)
cfprApLsBindingComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingComputeEpDn.setStatus("current")
_CfprApLsBindingIssues_Type = CfprApLsConfigIssues
_CfprApLsBindingIssues_Object = MibTableColumn
cfprApLsBindingIssues = _CfprApLsBindingIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 6),
    _CfprApLsBindingIssues_Type()
)
cfprApLsBindingIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingIssues.setStatus("current")
_CfprApLsBindingName_Type = SnmpAdminString
_CfprApLsBindingName_Object = MibTableColumn
cfprApLsBindingName = _CfprApLsBindingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 7),
    _CfprApLsBindingName_Type()
)
cfprApLsBindingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingName.setStatus("current")
_CfprApLsBindingOperState_Type = CfprApLsComputeBindingOperState
_CfprApLsBindingOperState_Object = MibTableColumn
cfprApLsBindingOperState = _CfprApLsBindingOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 8),
    _CfprApLsBindingOperState_Type()
)
cfprApLsBindingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingOperState.setStatus("current")
_CfprApLsBindingPnDn_Type = SnmpAdminString
_CfprApLsBindingPnDn_Object = MibTableColumn
cfprApLsBindingPnDn = _CfprApLsBindingPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 9),
    _CfprApLsBindingPnDn_Type()
)
cfprApLsBindingPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingPnDn.setStatus("current")
_CfprApLsBindingRestrictMigration_Type = TruthValue
_CfprApLsBindingRestrictMigration_Object = MibTableColumn
cfprApLsBindingRestrictMigration = _CfprApLsBindingRestrictMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 2, 1, 10),
    _CfprApLsBindingRestrictMigration_Type()
)
cfprApLsBindingRestrictMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsBindingRestrictMigration.setStatus("current")
_CfprApLsFcLocaleTable_Object = MibTable
cfprApLsFcLocaleTable = _CfprApLsFcLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 3)
)
if mibBuilder.loadTexts:
    cfprApLsFcLocaleTable.setStatus("current")
_CfprApLsFcLocaleEntry_Object = MibTableRow
cfprApLsFcLocaleEntry = _CfprApLsFcLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 3, 1)
)
cfprApLsFcLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsFcLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsFcLocaleEntry.setStatus("current")
_CfprApLsFcLocaleInstanceId_Type = CfprApManagedObjectId
_CfprApLsFcLocaleInstanceId_Object = MibTableColumn
cfprApLsFcLocaleInstanceId = _CfprApLsFcLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 3, 1, 1),
    _CfprApLsFcLocaleInstanceId_Type()
)
cfprApLsFcLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsFcLocaleInstanceId.setStatus("current")
_CfprApLsFcLocaleDn_Type = CfprApManagedObjectDn
_CfprApLsFcLocaleDn_Object = MibTableColumn
cfprApLsFcLocaleDn = _CfprApLsFcLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 3, 1, 2),
    _CfprApLsFcLocaleDn_Type()
)
cfprApLsFcLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcLocaleDn.setStatus("current")
_CfprApLsFcLocaleRn_Type = SnmpAdminString
_CfprApLsFcLocaleRn_Object = MibTableColumn
cfprApLsFcLocaleRn = _CfprApLsFcLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 3, 1, 3),
    _CfprApLsFcLocaleRn_Type()
)
cfprApLsFcLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcLocaleRn.setStatus("current")
_CfprApLsFcLocaleSwitchId_Type = CfprApNetworkSwitchId
_CfprApLsFcLocaleSwitchId_Object = MibTableColumn
cfprApLsFcLocaleSwitchId = _CfprApLsFcLocaleSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 3, 1, 4),
    _CfprApLsFcLocaleSwitchId_Type()
)
cfprApLsFcLocaleSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcLocaleSwitchId.setStatus("current")
_CfprApLsFcZoneTable_Object = MibTable
cfprApLsFcZoneTable = _CfprApLsFcZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4)
)
if mibBuilder.loadTexts:
    cfprApLsFcZoneTable.setStatus("current")
_CfprApLsFcZoneEntry_Object = MibTableRow
cfprApLsFcZoneEntry = _CfprApLsFcZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1)
)
cfprApLsFcZoneEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsFcZoneInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsFcZoneEntry.setStatus("current")
_CfprApLsFcZoneInstanceId_Type = CfprApManagedObjectId
_CfprApLsFcZoneInstanceId_Object = MibTableColumn
cfprApLsFcZoneInstanceId = _CfprApLsFcZoneInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 1),
    _CfprApLsFcZoneInstanceId_Type()
)
cfprApLsFcZoneInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsFcZoneInstanceId.setStatus("current")
_CfprApLsFcZoneDn_Type = CfprApManagedObjectDn
_CfprApLsFcZoneDn_Object = MibTableColumn
cfprApLsFcZoneDn = _CfprApLsFcZoneDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 2),
    _CfprApLsFcZoneDn_Type()
)
cfprApLsFcZoneDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneDn.setStatus("current")
_CfprApLsFcZoneRn_Type = SnmpAdminString
_CfprApLsFcZoneRn_Object = MibTableColumn
cfprApLsFcZoneRn = _CfprApLsFcZoneRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 3),
    _CfprApLsFcZoneRn_Type()
)
cfprApLsFcZoneRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneRn.setStatus("current")
_CfprApLsFcZoneAdminState_Type = CfprApLsFcZoneState
_CfprApLsFcZoneAdminState_Object = MibTableColumn
cfprApLsFcZoneAdminState = _CfprApLsFcZoneAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 4),
    _CfprApLsFcZoneAdminState_Type()
)
cfprApLsFcZoneAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneAdminState.setStatus("current")
_CfprApLsFcZoneId_Type = Gauge32
_CfprApLsFcZoneId_Object = MibTableColumn
cfprApLsFcZoneId = _CfprApLsFcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 5),
    _CfprApLsFcZoneId_Type()
)
cfprApLsFcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneId.setStatus("current")
_CfprApLsFcZoneIdentity_Type = SnmpAdminString
_CfprApLsFcZoneIdentity_Object = MibTableColumn
cfprApLsFcZoneIdentity = _CfprApLsFcZoneIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 6),
    _CfprApLsFcZoneIdentity_Type()
)
cfprApLsFcZoneIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneIdentity.setStatus("current")
_CfprApLsFcZoneIniName_Type = SnmpAdminString
_CfprApLsFcZoneIniName_Object = MibTableColumn
cfprApLsFcZoneIniName = _CfprApLsFcZoneIniName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 7),
    _CfprApLsFcZoneIniName_Type()
)
cfprApLsFcZoneIniName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneIniName.setStatus("current")
_CfprApLsFcZoneName_Type = SnmpAdminString
_CfprApLsFcZoneName_Object = MibTableColumn
cfprApLsFcZoneName = _CfprApLsFcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 8),
    _CfprApLsFcZoneName_Type()
)
cfprApLsFcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneName.setStatus("current")
_CfprApLsFcZoneOperState_Type = CfprApLsFcZoneState
_CfprApLsFcZoneOperState_Object = MibTableColumn
cfprApLsFcZoneOperState = _CfprApLsFcZoneOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 9),
    _CfprApLsFcZoneOperState_Type()
)
cfprApLsFcZoneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneOperState.setStatus("current")
_CfprApLsFcZonePeerDn_Type = SnmpAdminString
_CfprApLsFcZonePeerDn_Object = MibTableColumn
cfprApLsFcZonePeerDn = _CfprApLsFcZonePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 10),
    _CfprApLsFcZonePeerDn_Type()
)
cfprApLsFcZonePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZonePeerDn.setStatus("current")
_CfprApLsFcZoneSwitchId_Type = CfprApNetworkSwitchId
_CfprApLsFcZoneSwitchId_Object = MibTableColumn
cfprApLsFcZoneSwitchId = _CfprApLsFcZoneSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 11),
    _CfprApLsFcZoneSwitchId_Type()
)
cfprApLsFcZoneSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneSwitchId.setStatus("current")
_CfprApLsFcZoneUsrLbl_Type = SnmpAdminString
_CfprApLsFcZoneUsrLbl_Object = MibTableColumn
cfprApLsFcZoneUsrLbl = _CfprApLsFcZoneUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 12),
    _CfprApLsFcZoneUsrLbl_Type()
)
cfprApLsFcZoneUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneUsrLbl.setStatus("current")
_CfprApLsFcZoneVnetId_Type = Gauge32
_CfprApLsFcZoneVnetId_Object = MibTableColumn
cfprApLsFcZoneVnetId = _CfprApLsFcZoneVnetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 13),
    _CfprApLsFcZoneVnetId_Type()
)
cfprApLsFcZoneVnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneVnetId.setStatus("current")
_CfprApLsFcZoneZoningType_Type = CfprApStorageFcZoningType
_CfprApLsFcZoneZoningType_Object = MibTableColumn
cfprApLsFcZoneZoningType = _CfprApLsFcZoneZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 4, 1, 14),
    _CfprApLsFcZoneZoningType_Type()
)
cfprApLsFcZoneZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneZoningType.setStatus("current")
_CfprApLsFcZoneGroupTable_Object = MibTable
cfprApLsFcZoneGroupTable = _CfprApLsFcZoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5)
)
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupTable.setStatus("current")
_CfprApLsFcZoneGroupEntry_Object = MibTableRow
cfprApLsFcZoneGroupEntry = _CfprApLsFcZoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1)
)
cfprApLsFcZoneGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsFcZoneGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupEntry.setStatus("current")
_CfprApLsFcZoneGroupInstanceId_Type = CfprApManagedObjectId
_CfprApLsFcZoneGroupInstanceId_Object = MibTableColumn
cfprApLsFcZoneGroupInstanceId = _CfprApLsFcZoneGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1, 1),
    _CfprApLsFcZoneGroupInstanceId_Type()
)
cfprApLsFcZoneGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupInstanceId.setStatus("current")
_CfprApLsFcZoneGroupDn_Type = CfprApManagedObjectDn
_CfprApLsFcZoneGroupDn_Object = MibTableColumn
cfprApLsFcZoneGroupDn = _CfprApLsFcZoneGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1, 2),
    _CfprApLsFcZoneGroupDn_Type()
)
cfprApLsFcZoneGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupDn.setStatus("current")
_CfprApLsFcZoneGroupRn_Type = SnmpAdminString
_CfprApLsFcZoneGroupRn_Object = MibTableColumn
cfprApLsFcZoneGroupRn = _CfprApLsFcZoneGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1, 3),
    _CfprApLsFcZoneGroupRn_Type()
)
cfprApLsFcZoneGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupRn.setStatus("current")
_CfprApLsFcZoneGroupId_Type = Gauge32
_CfprApLsFcZoneGroupId_Object = MibTableColumn
cfprApLsFcZoneGroupId = _CfprApLsFcZoneGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1, 4),
    _CfprApLsFcZoneGroupId_Type()
)
cfprApLsFcZoneGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupId.setStatus("current")
_CfprApLsFcZoneGroupName_Type = SnmpAdminString
_CfprApLsFcZoneGroupName_Object = MibTableColumn
cfprApLsFcZoneGroupName = _CfprApLsFcZoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1, 5),
    _CfprApLsFcZoneGroupName_Type()
)
cfprApLsFcZoneGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupName.setStatus("current")
_CfprApLsFcZoneGroupSwitchId_Type = CfprApLsFcZoneGroupSwitchId
_CfprApLsFcZoneGroupSwitchId_Object = MibTableColumn
cfprApLsFcZoneGroupSwitchId = _CfprApLsFcZoneGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 5, 1, 6),
    _CfprApLsFcZoneGroupSwitchId_Type()
)
cfprApLsFcZoneGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsFcZoneGroupSwitchId.setStatus("current")
_CfprApLsIssuesTable_Object = MibTable
cfprApLsIssuesTable = _CfprApLsIssuesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6)
)
if mibBuilder.loadTexts:
    cfprApLsIssuesTable.setStatus("current")
_CfprApLsIssuesEntry_Object = MibTableRow
cfprApLsIssuesEntry = _CfprApLsIssuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1)
)
cfprApLsIssuesEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsIssuesInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsIssuesEntry.setStatus("current")
_CfprApLsIssuesInstanceId_Type = CfprApManagedObjectId
_CfprApLsIssuesInstanceId_Object = MibTableColumn
cfprApLsIssuesInstanceId = _CfprApLsIssuesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 1),
    _CfprApLsIssuesInstanceId_Type()
)
cfprApLsIssuesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsIssuesInstanceId.setStatus("current")
_CfprApLsIssuesDn_Type = CfprApManagedObjectDn
_CfprApLsIssuesDn_Object = MibTableColumn
cfprApLsIssuesDn = _CfprApLsIssuesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 2),
    _CfprApLsIssuesDn_Type()
)
cfprApLsIssuesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesDn.setStatus("current")
_CfprApLsIssuesRn_Type = SnmpAdminString
_CfprApLsIssuesRn_Object = MibTableColumn
cfprApLsIssuesRn = _CfprApLsIssuesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 3),
    _CfprApLsIssuesRn_Type()
)
cfprApLsIssuesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesRn.setStatus("current")
_CfprApLsIssuesConfigWarnings_Type = CfprApLsConfigWarnings
_CfprApLsIssuesConfigWarnings_Object = MibTableColumn
cfprApLsIssuesConfigWarnings = _CfprApLsIssuesConfigWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 4),
    _CfprApLsIssuesConfigWarnings_Type()
)
cfprApLsIssuesConfigWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesConfigWarnings.setStatus("current")
_CfprApLsIssuesIscsiConfigIssues_Type = CfprApVnicIScsiConfigIssues
_CfprApLsIssuesIscsiConfigIssues_Object = MibTableColumn
cfprApLsIssuesIscsiConfigIssues = _CfprApLsIssuesIscsiConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 5),
    _CfprApLsIssuesIscsiConfigIssues_Type()
)
cfprApLsIssuesIscsiConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesIscsiConfigIssues.setStatus("current")
_CfprApLsIssuesNetworkConfigIssues_Type = CfprApNetworkConfigIssues
_CfprApLsIssuesNetworkConfigIssues_Object = MibTableColumn
cfprApLsIssuesNetworkConfigIssues = _CfprApLsIssuesNetworkConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 6),
    _CfprApLsIssuesNetworkConfigIssues_Type()
)
cfprApLsIssuesNetworkConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesNetworkConfigIssues.setStatus("current")
_CfprApLsIssuesServerConfigIssues_Type = CfprApServerConfigIssues
_CfprApLsIssuesServerConfigIssues_Object = MibTableColumn
cfprApLsIssuesServerConfigIssues = _CfprApLsIssuesServerConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 7),
    _CfprApLsIssuesServerConfigIssues_Type()
)
cfprApLsIssuesServerConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesServerConfigIssues.setStatus("current")
_CfprApLsIssuesStorageConfigIssues_Type = CfprApStorageConfigIssues
_CfprApLsIssuesStorageConfigIssues_Object = MibTableColumn
cfprApLsIssuesStorageConfigIssues = _CfprApLsIssuesStorageConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 8),
    _CfprApLsIssuesStorageConfigIssues_Type()
)
cfprApLsIssuesStorageConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesStorageConfigIssues.setStatus("current")
_CfprApLsIssuesVnicConfigIssues_Type = CfprApVnicConfigIssues
_CfprApLsIssuesVnicConfigIssues_Object = MibTableColumn
cfprApLsIssuesVnicConfigIssues = _CfprApLsIssuesVnicConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 6, 1, 9),
    _CfprApLsIssuesVnicConfigIssues_Type()
)
cfprApLsIssuesVnicConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsIssuesVnicConfigIssues.setStatus("current")
_CfprApLsPowerTable_Object = MibTable
cfprApLsPowerTable = _CfprApLsPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 7)
)
if mibBuilder.loadTexts:
    cfprApLsPowerTable.setStatus("current")
_CfprApLsPowerEntry_Object = MibTableRow
cfprApLsPowerEntry = _CfprApLsPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 7, 1)
)
cfprApLsPowerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsPowerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsPowerEntry.setStatus("current")
_CfprApLsPowerInstanceId_Type = CfprApManagedObjectId
_CfprApLsPowerInstanceId_Object = MibTableColumn
cfprApLsPowerInstanceId = _CfprApLsPowerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 7, 1, 1),
    _CfprApLsPowerInstanceId_Type()
)
cfprApLsPowerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsPowerInstanceId.setStatus("current")
_CfprApLsPowerDn_Type = CfprApManagedObjectDn
_CfprApLsPowerDn_Object = MibTableColumn
cfprApLsPowerDn = _CfprApLsPowerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 7, 1, 2),
    _CfprApLsPowerDn_Type()
)
cfprApLsPowerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsPowerDn.setStatus("current")
_CfprApLsPowerRn_Type = SnmpAdminString
_CfprApLsPowerRn_Object = MibTableColumn
cfprApLsPowerRn = _CfprApLsPowerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 7, 1, 3),
    _CfprApLsPowerRn_Type()
)
cfprApLsPowerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsPowerRn.setStatus("current")
_CfprApLsPowerState_Type = CfprApLsPowerState
_CfprApLsPowerState_Object = MibTableColumn
cfprApLsPowerState = _CfprApLsPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 7, 1, 4),
    _CfprApLsPowerState_Type()
)
cfprApLsPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsPowerState.setStatus("current")
_CfprApLsRequirementTable_Object = MibTable
cfprApLsRequirementTable = _CfprApLsRequirementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8)
)
if mibBuilder.loadTexts:
    cfprApLsRequirementTable.setStatus("current")
_CfprApLsRequirementEntry_Object = MibTableRow
cfprApLsRequirementEntry = _CfprApLsRequirementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1)
)
cfprApLsRequirementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsRequirementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsRequirementEntry.setStatus("current")
_CfprApLsRequirementInstanceId_Type = CfprApManagedObjectId
_CfprApLsRequirementInstanceId_Object = MibTableColumn
cfprApLsRequirementInstanceId = _CfprApLsRequirementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 1),
    _CfprApLsRequirementInstanceId_Type()
)
cfprApLsRequirementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsRequirementInstanceId.setStatus("current")
_CfprApLsRequirementDn_Type = CfprApManagedObjectDn
_CfprApLsRequirementDn_Object = MibTableColumn
cfprApLsRequirementDn = _CfprApLsRequirementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 2),
    _CfprApLsRequirementDn_Type()
)
cfprApLsRequirementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementDn.setStatus("current")
_CfprApLsRequirementRn_Type = SnmpAdminString
_CfprApLsRequirementRn_Object = MibTableColumn
cfprApLsRequirementRn = _CfprApLsRequirementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 3),
    _CfprApLsRequirementRn_Type()
)
cfprApLsRequirementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementRn.setStatus("current")
_CfprApLsRequirementAssignedToDn_Type = SnmpAdminString
_CfprApLsRequirementAssignedToDn_Object = MibTableColumn
cfprApLsRequirementAssignedToDn = _CfprApLsRequirementAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 4),
    _CfprApLsRequirementAssignedToDn_Type()
)
cfprApLsRequirementAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementAssignedToDn.setStatus("current")
_CfprApLsRequirementComputeEpDn_Type = SnmpAdminString
_CfprApLsRequirementComputeEpDn_Object = MibTableColumn
cfprApLsRequirementComputeEpDn = _CfprApLsRequirementComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 5),
    _CfprApLsRequirementComputeEpDn_Type()
)
cfprApLsRequirementComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementComputeEpDn.setStatus("current")
_CfprApLsRequirementIssues_Type = CfprApLsConfigIssues
_CfprApLsRequirementIssues_Object = MibTableColumn
cfprApLsRequirementIssues = _CfprApLsRequirementIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 6),
    _CfprApLsRequirementIssues_Type()
)
cfprApLsRequirementIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementIssues.setStatus("current")
_CfprApLsRequirementName_Type = SnmpAdminString
_CfprApLsRequirementName_Object = MibTableColumn
cfprApLsRequirementName = _CfprApLsRequirementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 7),
    _CfprApLsRequirementName_Type()
)
cfprApLsRequirementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementName.setStatus("current")
_CfprApLsRequirementOperName_Type = SnmpAdminString
_CfprApLsRequirementOperName_Object = MibTableColumn
cfprApLsRequirementOperName = _CfprApLsRequirementOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 8),
    _CfprApLsRequirementOperName_Type()
)
cfprApLsRequirementOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementOperName.setStatus("current")
_CfprApLsRequirementOperState_Type = CfprApLsComputeBindingOperState
_CfprApLsRequirementOperState_Object = MibTableColumn
cfprApLsRequirementOperState = _CfprApLsRequirementOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 9),
    _CfprApLsRequirementOperState_Type()
)
cfprApLsRequirementOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementOperState.setStatus("current")
_CfprApLsRequirementPnDn_Type = SnmpAdminString
_CfprApLsRequirementPnDn_Object = MibTableColumn
cfprApLsRequirementPnDn = _CfprApLsRequirementPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 10),
    _CfprApLsRequirementPnDn_Type()
)
cfprApLsRequirementPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementPnDn.setStatus("current")
_CfprApLsRequirementPnPoolDn_Type = SnmpAdminString
_CfprApLsRequirementPnPoolDn_Object = MibTableColumn
cfprApLsRequirementPnPoolDn = _CfprApLsRequirementPnPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 11),
    _CfprApLsRequirementPnPoolDn_Type()
)
cfprApLsRequirementPnPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementPnPoolDn.setStatus("current")
_CfprApLsRequirementQualifier_Type = SnmpAdminString
_CfprApLsRequirementQualifier_Object = MibTableColumn
cfprApLsRequirementQualifier = _CfprApLsRequirementQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 12),
    _CfprApLsRequirementQualifier_Type()
)
cfprApLsRequirementQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementQualifier.setStatus("current")
_CfprApLsRequirementRestrictMigration_Type = TruthValue
_CfprApLsRequirementRestrictMigration_Object = MibTableColumn
cfprApLsRequirementRestrictMigration = _CfprApLsRequirementRestrictMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 8, 1, 13),
    _CfprApLsRequirementRestrictMigration_Type()
)
cfprApLsRequirementRestrictMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsRequirementRestrictMigration.setStatus("current")
_CfprApLsServerTable_Object = MibTable
cfprApLsServerTable = _CfprApLsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9)
)
if mibBuilder.loadTexts:
    cfprApLsServerTable.setStatus("current")
_CfprApLsServerEntry_Object = MibTableRow
cfprApLsServerEntry = _CfprApLsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1)
)
cfprApLsServerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsServerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsServerEntry.setStatus("current")
_CfprApLsServerInstanceId_Type = CfprApManagedObjectId
_CfprApLsServerInstanceId_Object = MibTableColumn
cfprApLsServerInstanceId = _CfprApLsServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 1),
    _CfprApLsServerInstanceId_Type()
)
cfprApLsServerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsServerInstanceId.setStatus("current")
_CfprApLsServerDn_Type = CfprApManagedObjectDn
_CfprApLsServerDn_Object = MibTableColumn
cfprApLsServerDn = _CfprApLsServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 2),
    _CfprApLsServerDn_Type()
)
cfprApLsServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerDn.setStatus("current")
_CfprApLsServerRn_Type = SnmpAdminString
_CfprApLsServerRn_Object = MibTableColumn
cfprApLsServerRn = _CfprApLsServerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 3),
    _CfprApLsServerRn_Type()
)
cfprApLsServerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerRn.setStatus("current")
_CfprApLsServerAgentPolicyName_Type = SnmpAdminString
_CfprApLsServerAgentPolicyName_Object = MibTableColumn
cfprApLsServerAgentPolicyName = _CfprApLsServerAgentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 4),
    _CfprApLsServerAgentPolicyName_Type()
)
cfprApLsServerAgentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerAgentPolicyName.setStatus("current")
_CfprApLsServerAssignState_Type = CfprApLsAssignment
_CfprApLsServerAssignState_Object = MibTableColumn
cfprApLsServerAssignState = _CfprApLsServerAssignState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 5),
    _CfprApLsServerAssignState_Type()
)
cfprApLsServerAssignState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerAssignState.setStatus("current")
_CfprApLsServerAssocState_Type = CfprApLsAssocState
_CfprApLsServerAssocState_Object = MibTableColumn
cfprApLsServerAssocState = _CfprApLsServerAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 6),
    _CfprApLsServerAssocState_Type()
)
cfprApLsServerAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerAssocState.setStatus("current")
_CfprApLsServerBiosProfileName_Type = SnmpAdminString
_CfprApLsServerBiosProfileName_Object = MibTableColumn
cfprApLsServerBiosProfileName = _CfprApLsServerBiosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 7),
    _CfprApLsServerBiosProfileName_Type()
)
cfprApLsServerBiosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerBiosProfileName.setStatus("current")
_CfprApLsServerBootPolicyName_Type = SnmpAdminString
_CfprApLsServerBootPolicyName_Object = MibTableColumn
cfprApLsServerBootPolicyName = _CfprApLsServerBootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 8),
    _CfprApLsServerBootPolicyName_Type()
)
cfprApLsServerBootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerBootPolicyName.setStatus("current")
_CfprApLsServerConfigQualifier_Type = CfprApLsConfigIssues
_CfprApLsServerConfigQualifier_Object = MibTableColumn
cfprApLsServerConfigQualifier = _CfprApLsServerConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 9),
    _CfprApLsServerConfigQualifier_Type()
)
cfprApLsServerConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerConfigQualifier.setStatus("current")
_CfprApLsServerConfigState_Type = CfprApLsConfigState
_CfprApLsServerConfigState_Object = MibTableColumn
cfprApLsServerConfigState = _CfprApLsServerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 10),
    _CfprApLsServerConfigState_Type()
)
cfprApLsServerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerConfigState.setStatus("current")
_CfprApLsServerDescr_Type = SnmpAdminString
_CfprApLsServerDescr_Object = MibTableColumn
cfprApLsServerDescr = _CfprApLsServerDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 11),
    _CfprApLsServerDescr_Type()
)
cfprApLsServerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerDescr.setStatus("current")
_CfprApLsServerDynamicConPolicyName_Type = SnmpAdminString
_CfprApLsServerDynamicConPolicyName_Object = MibTableColumn
cfprApLsServerDynamicConPolicyName = _CfprApLsServerDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 12),
    _CfprApLsServerDynamicConPolicyName_Type()
)
cfprApLsServerDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerDynamicConPolicyName.setStatus("current")
_CfprApLsServerExtIPPoolName_Type = SnmpAdminString
_CfprApLsServerExtIPPoolName_Object = MibTableColumn
cfprApLsServerExtIPPoolName = _CfprApLsServerExtIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 13),
    _CfprApLsServerExtIPPoolName_Type()
)
cfprApLsServerExtIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerExtIPPoolName.setStatus("current")
_CfprApLsServerExtIPState_Type = CfprApVnicExternalMgmtIPMode
_CfprApLsServerExtIPState_Object = MibTableColumn
cfprApLsServerExtIPState = _CfprApLsServerExtIPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 14),
    _CfprApLsServerExtIPState_Type()
)
cfprApLsServerExtIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerExtIPState.setStatus("current")
_CfprApLsServerFltAggr_Type = Unsigned64
_CfprApLsServerFltAggr_Object = MibTableColumn
cfprApLsServerFltAggr = _CfprApLsServerFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 15),
    _CfprApLsServerFltAggr_Type()
)
cfprApLsServerFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFltAggr.setStatus("current")
_CfprApLsServerFsmDescr_Type = SnmpAdminString
_CfprApLsServerFsmDescr_Object = MibTableColumn
cfprApLsServerFsmDescr = _CfprApLsServerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 16),
    _CfprApLsServerFsmDescr_Type()
)
cfprApLsServerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmDescr.setStatus("current")
_CfprApLsServerFsmFlags_Type = SnmpAdminString
_CfprApLsServerFsmFlags_Object = MibTableColumn
cfprApLsServerFsmFlags = _CfprApLsServerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 17),
    _CfprApLsServerFsmFlags_Type()
)
cfprApLsServerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmFlags.setStatus("current")
_CfprApLsServerFsmPrev_Type = SnmpAdminString
_CfprApLsServerFsmPrev_Object = MibTableColumn
cfprApLsServerFsmPrev = _CfprApLsServerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 18),
    _CfprApLsServerFsmPrev_Type()
)
cfprApLsServerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmPrev.setStatus("current")
_CfprApLsServerFsmProgr_Type = Gauge32
_CfprApLsServerFsmProgr_Object = MibTableColumn
cfprApLsServerFsmProgr = _CfprApLsServerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 19),
    _CfprApLsServerFsmProgr_Type()
)
cfprApLsServerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmProgr.setStatus("current")
_CfprApLsServerFsmRmtInvErrCode_Type = Gauge32
_CfprApLsServerFsmRmtInvErrCode_Object = MibTableColumn
cfprApLsServerFsmRmtInvErrCode = _CfprApLsServerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 20),
    _CfprApLsServerFsmRmtInvErrCode_Type()
)
cfprApLsServerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRmtInvErrCode.setStatus("current")
_CfprApLsServerFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApLsServerFsmRmtInvErrDescr_Object = MibTableColumn
cfprApLsServerFsmRmtInvErrDescr = _CfprApLsServerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 21),
    _CfprApLsServerFsmRmtInvErrDescr_Type()
)
cfprApLsServerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRmtInvErrDescr.setStatus("current")
_CfprApLsServerFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApLsServerFsmRmtInvRslt_Object = MibTableColumn
cfprApLsServerFsmRmtInvRslt = _CfprApLsServerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 22),
    _CfprApLsServerFsmRmtInvRslt_Type()
)
cfprApLsServerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRmtInvRslt.setStatus("current")
_CfprApLsServerFsmStageDescr_Type = SnmpAdminString
_CfprApLsServerFsmStageDescr_Object = MibTableColumn
cfprApLsServerFsmStageDescr = _CfprApLsServerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 23),
    _CfprApLsServerFsmStageDescr_Type()
)
cfprApLsServerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageDescr.setStatus("current")
_CfprApLsServerFsmStamp_Type = DateAndTime
_CfprApLsServerFsmStamp_Object = MibTableColumn
cfprApLsServerFsmStamp = _CfprApLsServerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 24),
    _CfprApLsServerFsmStamp_Type()
)
cfprApLsServerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStamp.setStatus("current")
_CfprApLsServerFsmStatus_Type = SnmpAdminString
_CfprApLsServerFsmStatus_Object = MibTableColumn
cfprApLsServerFsmStatus = _CfprApLsServerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 25),
    _CfprApLsServerFsmStatus_Type()
)
cfprApLsServerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStatus.setStatus("current")
_CfprApLsServerFsmTry_Type = Gauge32
_CfprApLsServerFsmTry_Object = MibTableColumn
cfprApLsServerFsmTry = _CfprApLsServerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 26),
    _CfprApLsServerFsmTry_Type()
)
cfprApLsServerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTry.setStatus("current")
_CfprApLsServerHostFwPolicyName_Type = SnmpAdminString
_CfprApLsServerHostFwPolicyName_Object = MibTableColumn
cfprApLsServerHostFwPolicyName = _CfprApLsServerHostFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 27),
    _CfprApLsServerHostFwPolicyName_Type()
)
cfprApLsServerHostFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerHostFwPolicyName.setStatus("current")
_CfprApLsServerIdentPoolName_Type = SnmpAdminString
_CfprApLsServerIdentPoolName_Object = MibTableColumn
cfprApLsServerIdentPoolName = _CfprApLsServerIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 28),
    _CfprApLsServerIdentPoolName_Type()
)
cfprApLsServerIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerIdentPoolName.setStatus("current")
_CfprApLsServerIntId_Type = SnmpAdminString
_CfprApLsServerIntId_Object = MibTableColumn
cfprApLsServerIntId = _CfprApLsServerIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 29),
    _CfprApLsServerIntId_Type()
)
cfprApLsServerIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerIntId.setStatus("current")
_CfprApLsServerLocalDiskPolicyName_Type = SnmpAdminString
_CfprApLsServerLocalDiskPolicyName_Object = MibTableColumn
cfprApLsServerLocalDiskPolicyName = _CfprApLsServerLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 31),
    _CfprApLsServerLocalDiskPolicyName_Type()
)
cfprApLsServerLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerLocalDiskPolicyName.setStatus("current")
_CfprApLsServerMaintPolicyName_Type = SnmpAdminString
_CfprApLsServerMaintPolicyName_Object = MibTableColumn
cfprApLsServerMaintPolicyName = _CfprApLsServerMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 32),
    _CfprApLsServerMaintPolicyName_Type()
)
cfprApLsServerMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerMaintPolicyName.setStatus("current")
_CfprApLsServerMgmtAccessPolicyName_Type = SnmpAdminString
_CfprApLsServerMgmtAccessPolicyName_Object = MibTableColumn
cfprApLsServerMgmtAccessPolicyName = _CfprApLsServerMgmtAccessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 33),
    _CfprApLsServerMgmtAccessPolicyName_Type()
)
cfprApLsServerMgmtAccessPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerMgmtAccessPolicyName.setStatus("current")
_CfprApLsServerMgmtFwPolicyName_Type = SnmpAdminString
_CfprApLsServerMgmtFwPolicyName_Object = MibTableColumn
cfprApLsServerMgmtFwPolicyName = _CfprApLsServerMgmtFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 34),
    _CfprApLsServerMgmtFwPolicyName_Type()
)
cfprApLsServerMgmtFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerMgmtFwPolicyName.setStatus("current")
_CfprApLsServerName_Type = SnmpAdminString
_CfprApLsServerName_Object = MibTableColumn
cfprApLsServerName = _CfprApLsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 35),
    _CfprApLsServerName_Type()
)
cfprApLsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerName.setStatus("current")
_CfprApLsServerOperBiosProfileName_Type = SnmpAdminString
_CfprApLsServerOperBiosProfileName_Object = MibTableColumn
cfprApLsServerOperBiosProfileName = _CfprApLsServerOperBiosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 36),
    _CfprApLsServerOperBiosProfileName_Type()
)
cfprApLsServerOperBiosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperBiosProfileName.setStatus("current")
_CfprApLsServerOperBootPolicyName_Type = SnmpAdminString
_CfprApLsServerOperBootPolicyName_Object = MibTableColumn
cfprApLsServerOperBootPolicyName = _CfprApLsServerOperBootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 37),
    _CfprApLsServerOperBootPolicyName_Type()
)
cfprApLsServerOperBootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperBootPolicyName.setStatus("current")
_CfprApLsServerOperDynamicConPolicyName_Type = SnmpAdminString
_CfprApLsServerOperDynamicConPolicyName_Object = MibTableColumn
cfprApLsServerOperDynamicConPolicyName = _CfprApLsServerOperDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 38),
    _CfprApLsServerOperDynamicConPolicyName_Type()
)
cfprApLsServerOperDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperDynamicConPolicyName.setStatus("current")
_CfprApLsServerOperExtIPPoolName_Type = SnmpAdminString
_CfprApLsServerOperExtIPPoolName_Object = MibTableColumn
cfprApLsServerOperExtIPPoolName = _CfprApLsServerOperExtIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 39),
    _CfprApLsServerOperExtIPPoolName_Type()
)
cfprApLsServerOperExtIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperExtIPPoolName.setStatus("current")
_CfprApLsServerOperHostFwPolicyName_Type = SnmpAdminString
_CfprApLsServerOperHostFwPolicyName_Object = MibTableColumn
cfprApLsServerOperHostFwPolicyName = _CfprApLsServerOperHostFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 40),
    _CfprApLsServerOperHostFwPolicyName_Type()
)
cfprApLsServerOperHostFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperHostFwPolicyName.setStatus("current")
_CfprApLsServerOperIdentPoolName_Type = SnmpAdminString
_CfprApLsServerOperIdentPoolName_Object = MibTableColumn
cfprApLsServerOperIdentPoolName = _CfprApLsServerOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 41),
    _CfprApLsServerOperIdentPoolName_Type()
)
cfprApLsServerOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperIdentPoolName.setStatus("current")
_CfprApLsServerOperLocalDiskPolicyName_Type = SnmpAdminString
_CfprApLsServerOperLocalDiskPolicyName_Object = MibTableColumn
cfprApLsServerOperLocalDiskPolicyName = _CfprApLsServerOperLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 43),
    _CfprApLsServerOperLocalDiskPolicyName_Type()
)
cfprApLsServerOperLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperLocalDiskPolicyName.setStatus("current")
_CfprApLsServerOperMaintPolicyName_Type = SnmpAdminString
_CfprApLsServerOperMaintPolicyName_Object = MibTableColumn
cfprApLsServerOperMaintPolicyName = _CfprApLsServerOperMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 44),
    _CfprApLsServerOperMaintPolicyName_Type()
)
cfprApLsServerOperMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperMaintPolicyName.setStatus("current")
_CfprApLsServerOperMgmtAccessPolicyName_Type = SnmpAdminString
_CfprApLsServerOperMgmtAccessPolicyName_Object = MibTableColumn
cfprApLsServerOperMgmtAccessPolicyName = _CfprApLsServerOperMgmtAccessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 45),
    _CfprApLsServerOperMgmtAccessPolicyName_Type()
)
cfprApLsServerOperMgmtAccessPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperMgmtAccessPolicyName.setStatus("current")
_CfprApLsServerOperMgmtFwPolicyName_Type = SnmpAdminString
_CfprApLsServerOperMgmtFwPolicyName_Object = MibTableColumn
cfprApLsServerOperMgmtFwPolicyName = _CfprApLsServerOperMgmtFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 46),
    _CfprApLsServerOperMgmtFwPolicyName_Type()
)
cfprApLsServerOperMgmtFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperMgmtFwPolicyName.setStatus("current")
_CfprApLsServerOperPowerPolicyName_Type = SnmpAdminString
_CfprApLsServerOperPowerPolicyName_Object = MibTableColumn
cfprApLsServerOperPowerPolicyName = _CfprApLsServerOperPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 47),
    _CfprApLsServerOperPowerPolicyName_Type()
)
cfprApLsServerOperPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperPowerPolicyName.setStatus("current")
_CfprApLsServerOperScrubPolicyName_Type = SnmpAdminString
_CfprApLsServerOperScrubPolicyName_Object = MibTableColumn
cfprApLsServerOperScrubPolicyName = _CfprApLsServerOperScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 48),
    _CfprApLsServerOperScrubPolicyName_Type()
)
cfprApLsServerOperScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperScrubPolicyName.setStatus("current")
_CfprApLsServerOperSolPolicyName_Type = SnmpAdminString
_CfprApLsServerOperSolPolicyName_Object = MibTableColumn
cfprApLsServerOperSolPolicyName = _CfprApLsServerOperSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 49),
    _CfprApLsServerOperSolPolicyName_Type()
)
cfprApLsServerOperSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperSolPolicyName.setStatus("current")
_CfprApLsServerOperSrcTemplName_Type = SnmpAdminString
_CfprApLsServerOperSrcTemplName_Object = MibTableColumn
cfprApLsServerOperSrcTemplName = _CfprApLsServerOperSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 50),
    _CfprApLsServerOperSrcTemplName_Type()
)
cfprApLsServerOperSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperSrcTemplName.setStatus("current")
_CfprApLsServerOperState_Type = CfprApLsOperState
_CfprApLsServerOperState_Object = MibTableColumn
cfprApLsServerOperState = _CfprApLsServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 51),
    _CfprApLsServerOperState_Type()
)
cfprApLsServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperState.setStatus("current")
_CfprApLsServerOperStatsPolicyName_Type = SnmpAdminString
_CfprApLsServerOperStatsPolicyName_Object = MibTableColumn
cfprApLsServerOperStatsPolicyName = _CfprApLsServerOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 52),
    _CfprApLsServerOperStatsPolicyName_Type()
)
cfprApLsServerOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperStatsPolicyName.setStatus("current")
_CfprApLsServerOperVconProfileName_Type = SnmpAdminString
_CfprApLsServerOperVconProfileName_Object = MibTableColumn
cfprApLsServerOperVconProfileName = _CfprApLsServerOperVconProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 53),
    _CfprApLsServerOperVconProfileName_Type()
)
cfprApLsServerOperVconProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOperVconProfileName.setStatus("current")
_CfprApLsServerOwner_Type = CfprApLsOwner
_CfprApLsServerOwner_Object = MibTableColumn
cfprApLsServerOwner = _CfprApLsServerOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 55),
    _CfprApLsServerOwner_Type()
)
cfprApLsServerOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerOwner.setStatus("current")
_CfprApLsServerPnDn_Type = SnmpAdminString
_CfprApLsServerPnDn_Object = MibTableColumn
cfprApLsServerPnDn = _CfprApLsServerPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 56),
    _CfprApLsServerPnDn_Type()
)
cfprApLsServerPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerPnDn.setStatus("current")
_CfprApLsServerPolicyLevel_Type = Gauge32
_CfprApLsServerPolicyLevel_Object = MibTableColumn
cfprApLsServerPolicyLevel = _CfprApLsServerPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 57),
    _CfprApLsServerPolicyLevel_Type()
)
cfprApLsServerPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerPolicyLevel.setStatus("current")
_CfprApLsServerPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsServerPolicyOwner_Object = MibTableColumn
cfprApLsServerPolicyOwner = _CfprApLsServerPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 58),
    _CfprApLsServerPolicyOwner_Type()
)
cfprApLsServerPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerPolicyOwner.setStatus("current")
_CfprApLsServerPowerPolicyName_Type = SnmpAdminString
_CfprApLsServerPowerPolicyName_Object = MibTableColumn
cfprApLsServerPowerPolicyName = _CfprApLsServerPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 59),
    _CfprApLsServerPowerPolicyName_Type()
)
cfprApLsServerPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerPowerPolicyName.setStatus("current")
_CfprApLsServerResolveRemote_Type = CfprApLsResolveFromRemoteServer
_CfprApLsServerResolveRemote_Object = MibTableColumn
cfprApLsServerResolveRemote = _CfprApLsServerResolveRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 60),
    _CfprApLsServerResolveRemote_Type()
)
cfprApLsServerResolveRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerResolveRemote.setStatus("current")
_CfprApLsServerScrubPolicyName_Type = SnmpAdminString
_CfprApLsServerScrubPolicyName_Object = MibTableColumn
cfprApLsServerScrubPolicyName = _CfprApLsServerScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 61),
    _CfprApLsServerScrubPolicyName_Type()
)
cfprApLsServerScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerScrubPolicyName.setStatus("current")
_CfprApLsServerSolPolicyName_Type = SnmpAdminString
_CfprApLsServerSolPolicyName_Object = MibTableColumn
cfprApLsServerSolPolicyName = _CfprApLsServerSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 62),
    _CfprApLsServerSolPolicyName_Type()
)
cfprApLsServerSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerSolPolicyName.setStatus("current")
_CfprApLsServerSrcTemplName_Type = SnmpAdminString
_CfprApLsServerSrcTemplName_Object = MibTableColumn
cfprApLsServerSrcTemplName = _CfprApLsServerSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 63),
    _CfprApLsServerSrcTemplName_Type()
)
cfprApLsServerSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerSrcTemplName.setStatus("current")
_CfprApLsServerStatsPolicyName_Type = SnmpAdminString
_CfprApLsServerStatsPolicyName_Object = MibTableColumn
cfprApLsServerStatsPolicyName = _CfprApLsServerStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 64),
    _CfprApLsServerStatsPolicyName_Type()
)
cfprApLsServerStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerStatsPolicyName.setStatus("current")
_CfprApLsServerSvnicConfig_Type = TruthValue
_CfprApLsServerSvnicConfig_Object = MibTableColumn
cfprApLsServerSvnicConfig = _CfprApLsServerSvnicConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 65),
    _CfprApLsServerSvnicConfig_Type()
)
cfprApLsServerSvnicConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerSvnicConfig.setStatus("current")
_CfprApLsServerType_Type = CfprApLsType
_CfprApLsServerType_Object = MibTableColumn
cfprApLsServerType = _CfprApLsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 66),
    _CfprApLsServerType_Type()
)
cfprApLsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerType.setStatus("current")
_CfprApLsServerUsrLbl_Type = SnmpAdminString
_CfprApLsServerUsrLbl_Object = MibTableColumn
cfprApLsServerUsrLbl = _CfprApLsServerUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 67),
    _CfprApLsServerUsrLbl_Type()
)
cfprApLsServerUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerUsrLbl.setStatus("current")
_CfprApLsServerUuid_Type = SnmpAdminString
_CfprApLsServerUuid_Object = MibTableColumn
cfprApLsServerUuid = _CfprApLsServerUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 68),
    _CfprApLsServerUuid_Type()
)
cfprApLsServerUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerUuid.setStatus("current")
_CfprApLsServerUuidSuffix_Type = Unsigned64
_CfprApLsServerUuidSuffix_Object = MibTableColumn
cfprApLsServerUuidSuffix = _CfprApLsServerUuidSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 69),
    _CfprApLsServerUuidSuffix_Type()
)
cfprApLsServerUuidSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerUuidSuffix.setStatus("current")
_CfprApLsServerVconProfileName_Type = SnmpAdminString
_CfprApLsServerVconProfileName_Object = MibTableColumn
cfprApLsServerVconProfileName = _CfprApLsServerVconProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 9, 1, 70),
    _CfprApLsServerVconProfileName_Type()
)
cfprApLsServerVconProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerVconProfileName.setStatus("current")
_CfprApLsServerAssocCtxTable_Object = MibTable
cfprApLsServerAssocCtxTable = _CfprApLsServerAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 10)
)
if mibBuilder.loadTexts:
    cfprApLsServerAssocCtxTable.setStatus("current")
_CfprApLsServerAssocCtxEntry_Object = MibTableRow
cfprApLsServerAssocCtxEntry = _CfprApLsServerAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 10, 1)
)
cfprApLsServerAssocCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsServerAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsServerAssocCtxEntry.setStatus("current")
_CfprApLsServerAssocCtxInstanceId_Type = CfprApManagedObjectId
_CfprApLsServerAssocCtxInstanceId_Object = MibTableColumn
cfprApLsServerAssocCtxInstanceId = _CfprApLsServerAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 10, 1, 1),
    _CfprApLsServerAssocCtxInstanceId_Type()
)
cfprApLsServerAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsServerAssocCtxInstanceId.setStatus("current")
_CfprApLsServerAssocCtxDn_Type = CfprApManagedObjectDn
_CfprApLsServerAssocCtxDn_Object = MibTableColumn
cfprApLsServerAssocCtxDn = _CfprApLsServerAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 10, 1, 2),
    _CfprApLsServerAssocCtxDn_Type()
)
cfprApLsServerAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerAssocCtxDn.setStatus("current")
_CfprApLsServerAssocCtxRn_Type = SnmpAdminString
_CfprApLsServerAssocCtxRn_Object = MibTableColumn
cfprApLsServerAssocCtxRn = _CfprApLsServerAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 10, 1, 3),
    _CfprApLsServerAssocCtxRn_Type()
)
cfprApLsServerAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerAssocCtxRn.setStatus("current")
_CfprApLsServerExtensionTable_Object = MibTable
cfprApLsServerExtensionTable = _CfprApLsServerExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11)
)
if mibBuilder.loadTexts:
    cfprApLsServerExtensionTable.setStatus("current")
_CfprApLsServerExtensionEntry_Object = MibTableRow
cfprApLsServerExtensionEntry = _CfprApLsServerExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11, 1)
)
cfprApLsServerExtensionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsServerExtensionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsServerExtensionEntry.setStatus("current")
_CfprApLsServerExtensionInstanceId_Type = CfprApManagedObjectId
_CfprApLsServerExtensionInstanceId_Object = MibTableColumn
cfprApLsServerExtensionInstanceId = _CfprApLsServerExtensionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11, 1, 1),
    _CfprApLsServerExtensionInstanceId_Type()
)
cfprApLsServerExtensionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsServerExtensionInstanceId.setStatus("current")
_CfprApLsServerExtensionDn_Type = CfprApManagedObjectDn
_CfprApLsServerExtensionDn_Object = MibTableColumn
cfprApLsServerExtensionDn = _CfprApLsServerExtensionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11, 1, 2),
    _CfprApLsServerExtensionDn_Type()
)
cfprApLsServerExtensionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerExtensionDn.setStatus("current")
_CfprApLsServerExtensionRn_Type = SnmpAdminString
_CfprApLsServerExtensionRn_Object = MibTableColumn
cfprApLsServerExtensionRn = _CfprApLsServerExtensionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11, 1, 3),
    _CfprApLsServerExtensionRn_Type()
)
cfprApLsServerExtensionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerExtensionRn.setStatus("current")
_CfprApLsServerExtensionGuid_Type = SnmpAdminString
_CfprApLsServerExtensionGuid_Object = MibTableColumn
cfprApLsServerExtensionGuid = _CfprApLsServerExtensionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11, 1, 4),
    _CfprApLsServerExtensionGuid_Type()
)
cfprApLsServerExtensionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerExtensionGuid.setStatus("current")
_CfprApLsServerExtensionVersion_Type = Gauge32
_CfprApLsServerExtensionVersion_Object = MibTableColumn
cfprApLsServerExtensionVersion = _CfprApLsServerExtensionVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 11, 1, 5),
    _CfprApLsServerExtensionVersion_Type()
)
cfprApLsServerExtensionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerExtensionVersion.setStatus("current")
_CfprApLsServerFsmTable_Object = MibTable
cfprApLsServerFsmTable = _CfprApLsServerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12)
)
if mibBuilder.loadTexts:
    cfprApLsServerFsmTable.setStatus("current")
_CfprApLsServerFsmEntry_Object = MibTableRow
cfprApLsServerFsmEntry = _CfprApLsServerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1)
)
cfprApLsServerFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsServerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsServerFsmEntry.setStatus("current")
_CfprApLsServerFsmInstanceId_Type = CfprApManagedObjectId
_CfprApLsServerFsmInstanceId_Object = MibTableColumn
cfprApLsServerFsmInstanceId = _CfprApLsServerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 1),
    _CfprApLsServerFsmInstanceId_Type()
)
cfprApLsServerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsServerFsmInstanceId.setStatus("current")
_CfprApLsServerFsmDn_Type = CfprApManagedObjectDn
_CfprApLsServerFsmDn_Object = MibTableColumn
cfprApLsServerFsmDn = _CfprApLsServerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 2),
    _CfprApLsServerFsmDn_Type()
)
cfprApLsServerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmDn.setStatus("current")
_CfprApLsServerFsmRn_Type = SnmpAdminString
_CfprApLsServerFsmRn_Object = MibTableColumn
cfprApLsServerFsmRn = _CfprApLsServerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 3),
    _CfprApLsServerFsmRn_Type()
)
cfprApLsServerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRn.setStatus("current")
_CfprApLsServerFsmCompletionTime_Type = DateAndTime
_CfprApLsServerFsmCompletionTime_Object = MibTableColumn
cfprApLsServerFsmCompletionTime = _CfprApLsServerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 4),
    _CfprApLsServerFsmCompletionTime_Type()
)
cfprApLsServerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmCompletionTime.setStatus("current")
_CfprApLsServerFsmCurrentFsm_Type = CfprApLsServerFsmCurrentFsm
_CfprApLsServerFsmCurrentFsm_Object = MibTableColumn
cfprApLsServerFsmCurrentFsm = _CfprApLsServerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 5),
    _CfprApLsServerFsmCurrentFsm_Type()
)
cfprApLsServerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmCurrentFsm.setStatus("current")
_CfprApLsServerFsmDescrData_Type = SnmpAdminString
_CfprApLsServerFsmDescrData_Object = MibTableColumn
cfprApLsServerFsmDescrData = _CfprApLsServerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 6),
    _CfprApLsServerFsmDescrData_Type()
)
cfprApLsServerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmDescrData.setStatus("current")
_CfprApLsServerFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApLsServerFsmFsmStatus_Object = MibTableColumn
cfprApLsServerFsmFsmStatus = _CfprApLsServerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 7),
    _CfprApLsServerFsmFsmStatus_Type()
)
cfprApLsServerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmFsmStatus.setStatus("current")
_CfprApLsServerFsmProgress_Type = Gauge32
_CfprApLsServerFsmProgress_Object = MibTableColumn
cfprApLsServerFsmProgress = _CfprApLsServerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 8),
    _CfprApLsServerFsmProgress_Type()
)
cfprApLsServerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmProgress.setStatus("current")
_CfprApLsServerFsmRmtErrCode_Type = Gauge32
_CfprApLsServerFsmRmtErrCode_Object = MibTableColumn
cfprApLsServerFsmRmtErrCode = _CfprApLsServerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 9),
    _CfprApLsServerFsmRmtErrCode_Type()
)
cfprApLsServerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRmtErrCode.setStatus("current")
_CfprApLsServerFsmRmtErrDescr_Type = SnmpAdminString
_CfprApLsServerFsmRmtErrDescr_Object = MibTableColumn
cfprApLsServerFsmRmtErrDescr = _CfprApLsServerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 10),
    _CfprApLsServerFsmRmtErrDescr_Type()
)
cfprApLsServerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRmtErrDescr.setStatus("current")
_CfprApLsServerFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApLsServerFsmRmtRslt_Object = MibTableColumn
cfprApLsServerFsmRmtRslt = _CfprApLsServerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 12, 1, 11),
    _CfprApLsServerFsmRmtRslt_Type()
)
cfprApLsServerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmRmtRslt.setStatus("current")
_CfprApLsServerFsmStageTable_Object = MibTable
cfprApLsServerFsmStageTable = _CfprApLsServerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13)
)
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageTable.setStatus("current")
_CfprApLsServerFsmStageEntry_Object = MibTableRow
cfprApLsServerFsmStageEntry = _CfprApLsServerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1)
)
cfprApLsServerFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsServerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageEntry.setStatus("current")
_CfprApLsServerFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApLsServerFsmStageInstanceId_Object = MibTableColumn
cfprApLsServerFsmStageInstanceId = _CfprApLsServerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 1),
    _CfprApLsServerFsmStageInstanceId_Type()
)
cfprApLsServerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageInstanceId.setStatus("current")
_CfprApLsServerFsmStageDn_Type = CfprApManagedObjectDn
_CfprApLsServerFsmStageDn_Object = MibTableColumn
cfprApLsServerFsmStageDn = _CfprApLsServerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 2),
    _CfprApLsServerFsmStageDn_Type()
)
cfprApLsServerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageDn.setStatus("current")
_CfprApLsServerFsmStageRn_Type = SnmpAdminString
_CfprApLsServerFsmStageRn_Object = MibTableColumn
cfprApLsServerFsmStageRn = _CfprApLsServerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 3),
    _CfprApLsServerFsmStageRn_Type()
)
cfprApLsServerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageRn.setStatus("current")
_CfprApLsServerFsmStageDescrData_Type = SnmpAdminString
_CfprApLsServerFsmStageDescrData_Object = MibTableColumn
cfprApLsServerFsmStageDescrData = _CfprApLsServerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 4),
    _CfprApLsServerFsmStageDescrData_Type()
)
cfprApLsServerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageDescrData.setStatus("current")
_CfprApLsServerFsmStageLastUpdateTime_Type = DateAndTime
_CfprApLsServerFsmStageLastUpdateTime_Object = MibTableColumn
cfprApLsServerFsmStageLastUpdateTime = _CfprApLsServerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 5),
    _CfprApLsServerFsmStageLastUpdateTime_Type()
)
cfprApLsServerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageLastUpdateTime.setStatus("current")
_CfprApLsServerFsmStageName_Type = CfprApLsServerFsmStageName
_CfprApLsServerFsmStageName_Object = MibTableColumn
cfprApLsServerFsmStageName = _CfprApLsServerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 6),
    _CfprApLsServerFsmStageName_Type()
)
cfprApLsServerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageName.setStatus("current")
_CfprApLsServerFsmStageOrder_Type = Gauge32
_CfprApLsServerFsmStageOrder_Object = MibTableColumn
cfprApLsServerFsmStageOrder = _CfprApLsServerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 7),
    _CfprApLsServerFsmStageOrder_Type()
)
cfprApLsServerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageOrder.setStatus("current")
_CfprApLsServerFsmStageRetry_Type = Gauge32
_CfprApLsServerFsmStageRetry_Object = MibTableColumn
cfprApLsServerFsmStageRetry = _CfprApLsServerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 8),
    _CfprApLsServerFsmStageRetry_Type()
)
cfprApLsServerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageRetry.setStatus("current")
_CfprApLsServerFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApLsServerFsmStageStageStatus_Object = MibTableColumn
cfprApLsServerFsmStageStageStatus = _CfprApLsServerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 13, 1, 9),
    _CfprApLsServerFsmStageStageStatus_Type()
)
cfprApLsServerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmStageStageStatus.setStatus("current")
_CfprApLsServerFsmTaskTable_Object = MibTable
cfprApLsServerFsmTaskTable = _CfprApLsServerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14)
)
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskTable.setStatus("current")
_CfprApLsServerFsmTaskEntry_Object = MibTableRow
cfprApLsServerFsmTaskEntry = _CfprApLsServerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1)
)
cfprApLsServerFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsServerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskEntry.setStatus("current")
_CfprApLsServerFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApLsServerFsmTaskInstanceId_Object = MibTableColumn
cfprApLsServerFsmTaskInstanceId = _CfprApLsServerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 1),
    _CfprApLsServerFsmTaskInstanceId_Type()
)
cfprApLsServerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskInstanceId.setStatus("current")
_CfprApLsServerFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApLsServerFsmTaskDn_Object = MibTableColumn
cfprApLsServerFsmTaskDn = _CfprApLsServerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 2),
    _CfprApLsServerFsmTaskDn_Type()
)
cfprApLsServerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskDn.setStatus("current")
_CfprApLsServerFsmTaskRn_Type = SnmpAdminString
_CfprApLsServerFsmTaskRn_Object = MibTableColumn
cfprApLsServerFsmTaskRn = _CfprApLsServerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 3),
    _CfprApLsServerFsmTaskRn_Type()
)
cfprApLsServerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskRn.setStatus("current")
_CfprApLsServerFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApLsServerFsmTaskCompletion_Object = MibTableColumn
cfprApLsServerFsmTaskCompletion = _CfprApLsServerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 4),
    _CfprApLsServerFsmTaskCompletion_Type()
)
cfprApLsServerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskCompletion.setStatus("current")
_CfprApLsServerFsmTaskFlags_Type = CfprApLsServerFsmTaskFlags
_CfprApLsServerFsmTaskFlags_Object = MibTableColumn
cfprApLsServerFsmTaskFlags = _CfprApLsServerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 5),
    _CfprApLsServerFsmTaskFlags_Type()
)
cfprApLsServerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskFlags.setStatus("current")
_CfprApLsServerFsmTaskItem_Type = CfprApLsServerFsmTaskItem
_CfprApLsServerFsmTaskItem_Object = MibTableColumn
cfprApLsServerFsmTaskItem = _CfprApLsServerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 6),
    _CfprApLsServerFsmTaskItem_Type()
)
cfprApLsServerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskItem.setStatus("current")
_CfprApLsServerFsmTaskSeqId_Type = Gauge32
_CfprApLsServerFsmTaskSeqId_Object = MibTableColumn
cfprApLsServerFsmTaskSeqId = _CfprApLsServerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 14, 1, 7),
    _CfprApLsServerFsmTaskSeqId_Type()
)
cfprApLsServerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsServerFsmTaskSeqId.setStatus("current")
_CfprApLsTierTable_Object = MibTable
cfprApLsTierTable = _CfprApLsTierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15)
)
if mibBuilder.loadTexts:
    cfprApLsTierTable.setStatus("current")
_CfprApLsTierEntry_Object = MibTableRow
cfprApLsTierEntry = _CfprApLsTierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1)
)
cfprApLsTierEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsTierInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsTierEntry.setStatus("current")
_CfprApLsTierInstanceId_Type = CfprApManagedObjectId
_CfprApLsTierInstanceId_Object = MibTableColumn
cfprApLsTierInstanceId = _CfprApLsTierInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 1),
    _CfprApLsTierInstanceId_Type()
)
cfprApLsTierInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsTierInstanceId.setStatus("current")
_CfprApLsTierDn_Type = CfprApManagedObjectDn
_CfprApLsTierDn_Object = MibTableColumn
cfprApLsTierDn = _CfprApLsTierDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 2),
    _CfprApLsTierDn_Type()
)
cfprApLsTierDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierDn.setStatus("current")
_CfprApLsTierRn_Type = SnmpAdminString
_CfprApLsTierRn_Object = MibTableColumn
cfprApLsTierRn = _CfprApLsTierRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 3),
    _CfprApLsTierRn_Type()
)
cfprApLsTierRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierRn.setStatus("current")
_CfprApLsTierApply_Type = CfprApLsApply
_CfprApLsTierApply_Object = MibTableColumn
cfprApLsTierApply = _CfprApLsTierApply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 4),
    _CfprApLsTierApply_Type()
)
cfprApLsTierApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierApply.setStatus("current")
_CfprApLsTierDescr_Type = SnmpAdminString
_CfprApLsTierDescr_Object = MibTableColumn
cfprApLsTierDescr = _CfprApLsTierDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 5),
    _CfprApLsTierDescr_Type()
)
cfprApLsTierDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierDescr.setStatus("current")
_CfprApLsTierIntId_Type = SnmpAdminString
_CfprApLsTierIntId_Object = MibTableColumn
cfprApLsTierIntId = _CfprApLsTierIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 6),
    _CfprApLsTierIntId_Type()
)
cfprApLsTierIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierIntId.setStatus("current")
_CfprApLsTierName_Type = SnmpAdminString
_CfprApLsTierName_Object = MibTableColumn
cfprApLsTierName = _CfprApLsTierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 7),
    _CfprApLsTierName_Type()
)
cfprApLsTierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierName.setStatus("current")
_CfprApLsTierPolicyLevel_Type = Gauge32
_CfprApLsTierPolicyLevel_Object = MibTableColumn
cfprApLsTierPolicyLevel = _CfprApLsTierPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 8),
    _CfprApLsTierPolicyLevel_Type()
)
cfprApLsTierPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierPolicyLevel.setStatus("current")
_CfprApLsTierPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsTierPolicyOwner_Object = MibTableColumn
cfprApLsTierPolicyOwner = _CfprApLsTierPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 9),
    _CfprApLsTierPolicyOwner_Type()
)
cfprApLsTierPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierPolicyOwner.setStatus("current")
_CfprApLsTierSrcTemplName_Type = SnmpAdminString
_CfprApLsTierSrcTemplName_Object = MibTableColumn
cfprApLsTierSrcTemplName = _CfprApLsTierSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 15, 1, 10),
    _CfprApLsTierSrcTemplName_Type()
)
cfprApLsTierSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsTierSrcTemplName.setStatus("current")
_CfprApLsUuidHistoryTable_Object = MibTable
cfprApLsUuidHistoryTable = _CfprApLsUuidHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 16)
)
if mibBuilder.loadTexts:
    cfprApLsUuidHistoryTable.setStatus("current")
_CfprApLsUuidHistoryEntry_Object = MibTableRow
cfprApLsUuidHistoryEntry = _CfprApLsUuidHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 16, 1)
)
cfprApLsUuidHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsUuidHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsUuidHistoryEntry.setStatus("current")
_CfprApLsUuidHistoryInstanceId_Type = CfprApManagedObjectId
_CfprApLsUuidHistoryInstanceId_Object = MibTableColumn
cfprApLsUuidHistoryInstanceId = _CfprApLsUuidHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 16, 1, 1),
    _CfprApLsUuidHistoryInstanceId_Type()
)
cfprApLsUuidHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsUuidHistoryInstanceId.setStatus("current")
_CfprApLsUuidHistoryDn_Type = CfprApManagedObjectDn
_CfprApLsUuidHistoryDn_Object = MibTableColumn
cfprApLsUuidHistoryDn = _CfprApLsUuidHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 16, 1, 2),
    _CfprApLsUuidHistoryDn_Type()
)
cfprApLsUuidHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsUuidHistoryDn.setStatus("current")
_CfprApLsUuidHistoryRn_Type = SnmpAdminString
_CfprApLsUuidHistoryRn_Object = MibTableColumn
cfprApLsUuidHistoryRn = _CfprApLsUuidHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 16, 1, 3),
    _CfprApLsUuidHistoryRn_Type()
)
cfprApLsUuidHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsUuidHistoryRn.setStatus("current")
_CfprApLsUuidHistoryOlduuid_Type = SnmpAdminString
_CfprApLsUuidHistoryOlduuid_Object = MibTableColumn
cfprApLsUuidHistoryOlduuid = _CfprApLsUuidHistoryOlduuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 16, 1, 4),
    _CfprApLsUuidHistoryOlduuid_Type()
)
cfprApLsUuidHistoryOlduuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsUuidHistoryOlduuid.setStatus("current")
_CfprApLsVConAssignTable_Object = MibTable
cfprApLsVConAssignTable = _CfprApLsVConAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17)
)
if mibBuilder.loadTexts:
    cfprApLsVConAssignTable.setStatus("current")
_CfprApLsVConAssignEntry_Object = MibTableRow
cfprApLsVConAssignEntry = _CfprApLsVConAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1)
)
cfprApLsVConAssignEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsVConAssignInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsVConAssignEntry.setStatus("current")
_CfprApLsVConAssignInstanceId_Type = CfprApManagedObjectId
_CfprApLsVConAssignInstanceId_Object = MibTableColumn
cfprApLsVConAssignInstanceId = _CfprApLsVConAssignInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 1),
    _CfprApLsVConAssignInstanceId_Type()
)
cfprApLsVConAssignInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsVConAssignInstanceId.setStatus("current")
_CfprApLsVConAssignDn_Type = CfprApManagedObjectDn
_CfprApLsVConAssignDn_Object = MibTableColumn
cfprApLsVConAssignDn = _CfprApLsVConAssignDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 2),
    _CfprApLsVConAssignDn_Type()
)
cfprApLsVConAssignDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVConAssignDn.setStatus("current")
_CfprApLsVConAssignRn_Type = SnmpAdminString
_CfprApLsVConAssignRn_Object = MibTableColumn
cfprApLsVConAssignRn = _CfprApLsVConAssignRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 3),
    _CfprApLsVConAssignRn_Type()
)
cfprApLsVConAssignRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVConAssignRn.setStatus("current")
_CfprApLsVConAssignAdminVcon_Type = SnmpAdminString
_CfprApLsVConAssignAdminVcon_Object = MibTableColumn
cfprApLsVConAssignAdminVcon = _CfprApLsVConAssignAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 4),
    _CfprApLsVConAssignAdminVcon_Type()
)
cfprApLsVConAssignAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVConAssignAdminVcon.setStatus("current")
_CfprApLsVConAssignOrder_Type = Gauge32
_CfprApLsVConAssignOrder_Object = MibTableColumn
cfprApLsVConAssignOrder = _CfprApLsVConAssignOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 5),
    _CfprApLsVConAssignOrder_Type()
)
cfprApLsVConAssignOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVConAssignOrder.setStatus("current")
_CfprApLsVConAssignTransport_Type = CfprApFabricVConTransportPref
_CfprApLsVConAssignTransport_Object = MibTableColumn
cfprApLsVConAssignTransport = _CfprApLsVConAssignTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 6),
    _CfprApLsVConAssignTransport_Type()
)
cfprApLsVConAssignTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVConAssignTransport.setStatus("current")
_CfprApLsVConAssignVnicName_Type = SnmpAdminString
_CfprApLsVConAssignVnicName_Object = MibTableColumn
cfprApLsVConAssignVnicName = _CfprApLsVConAssignVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 17, 1, 7),
    _CfprApLsVConAssignVnicName_Type()
)
cfprApLsVConAssignVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVConAssignVnicName.setStatus("current")
_CfprApLsVersionBehTable_Object = MibTable
cfprApLsVersionBehTable = _CfprApLsVersionBehTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18)
)
if mibBuilder.loadTexts:
    cfprApLsVersionBehTable.setStatus("current")
_CfprApLsVersionBehEntry_Object = MibTableRow
cfprApLsVersionBehEntry = _CfprApLsVersionBehEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1)
)
cfprApLsVersionBehEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsVersionBehInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsVersionBehEntry.setStatus("current")
_CfprApLsVersionBehInstanceId_Type = CfprApManagedObjectId
_CfprApLsVersionBehInstanceId_Object = MibTableColumn
cfprApLsVersionBehInstanceId = _CfprApLsVersionBehInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 1),
    _CfprApLsVersionBehInstanceId_Type()
)
cfprApLsVersionBehInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsVersionBehInstanceId.setStatus("current")
_CfprApLsVersionBehDn_Type = CfprApManagedObjectDn
_CfprApLsVersionBehDn_Object = MibTableColumn
cfprApLsVersionBehDn = _CfprApLsVersionBehDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 2),
    _CfprApLsVersionBehDn_Type()
)
cfprApLsVersionBehDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVersionBehDn.setStatus("current")
_CfprApLsVersionBehRn_Type = SnmpAdminString
_CfprApLsVersionBehRn_Object = MibTableColumn
cfprApLsVersionBehRn = _CfprApLsVersionBehRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 3),
    _CfprApLsVersionBehRn_Type()
)
cfprApLsVersionBehRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVersionBehRn.setStatus("current")
_CfprApLsVersionBehPciEnum_Type = CfprApVnicOrderScheme
_CfprApLsVersionBehPciEnum_Object = MibTableColumn
cfprApLsVersionBehPciEnum = _CfprApLsVersionBehPciEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 4),
    _CfprApLsVersionBehPciEnum_Type()
)
cfprApLsVersionBehPciEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVersionBehPciEnum.setStatus("current")
_CfprApLsVersionBehVconMap_Type = CfprApFabricVConMappingScheme
_CfprApLsVersionBehVconMap_Object = MibTableColumn
cfprApLsVersionBehVconMap = _CfprApLsVersionBehVconMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 5),
    _CfprApLsVersionBehVconMap_Type()
)
cfprApLsVersionBehVconMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVersionBehVconMap.setStatus("current")
_CfprApLsVersionBehVnicMap_Type = CfprApVnicMezzMappingScheme
_CfprApLsVersionBehVnicMap_Object = MibTableColumn
cfprApLsVersionBehVnicMap = _CfprApLsVersionBehVnicMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 6),
    _CfprApLsVersionBehVnicMap_Type()
)
cfprApLsVersionBehVnicMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVersionBehVnicMap.setStatus("current")
_CfprApLsVersionBehVnicOrder_Type = CfprApVnicPlacement
_CfprApLsVersionBehVnicOrder_Object = MibTableColumn
cfprApLsVersionBehVnicOrder = _CfprApLsVersionBehVnicOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 18, 1, 7),
    _CfprApLsVersionBehVnicOrder_Type()
)
cfprApLsVersionBehVnicOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsVersionBehVnicOrder.setStatus("current")
_CfprApLsZoneInitiatorMemberTable_Object = MibTable
cfprApLsZoneInitiatorMemberTable = _CfprApLsZoneInitiatorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19)
)
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberTable.setStatus("current")
_CfprApLsZoneInitiatorMemberEntry_Object = MibTableRow
cfprApLsZoneInitiatorMemberEntry = _CfprApLsZoneInitiatorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1)
)
cfprApLsZoneInitiatorMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsZoneInitiatorMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberEntry.setStatus("current")
_CfprApLsZoneInitiatorMemberInstanceId_Type = CfprApManagedObjectId
_CfprApLsZoneInitiatorMemberInstanceId_Object = MibTableColumn
cfprApLsZoneInitiatorMemberInstanceId = _CfprApLsZoneInitiatorMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 1),
    _CfprApLsZoneInitiatorMemberInstanceId_Type()
)
cfprApLsZoneInitiatorMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberInstanceId.setStatus("current")
_CfprApLsZoneInitiatorMemberDn_Type = CfprApManagedObjectDn
_CfprApLsZoneInitiatorMemberDn_Object = MibTableColumn
cfprApLsZoneInitiatorMemberDn = _CfprApLsZoneInitiatorMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 2),
    _CfprApLsZoneInitiatorMemberDn_Type()
)
cfprApLsZoneInitiatorMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberDn.setStatus("current")
_CfprApLsZoneInitiatorMemberRn_Type = SnmpAdminString
_CfprApLsZoneInitiatorMemberRn_Object = MibTableColumn
cfprApLsZoneInitiatorMemberRn = _CfprApLsZoneInitiatorMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 3),
    _CfprApLsZoneInitiatorMemberRn_Type()
)
cfprApLsZoneInitiatorMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberRn.setStatus("current")
_CfprApLsZoneInitiatorMemberEpDn_Type = SnmpAdminString
_CfprApLsZoneInitiatorMemberEpDn_Object = MibTableColumn
cfprApLsZoneInitiatorMemberEpDn = _CfprApLsZoneInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 4),
    _CfprApLsZoneInitiatorMemberEpDn_Type()
)
cfprApLsZoneInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberEpDn.setStatus("current")
_CfprApLsZoneInitiatorMemberName_Type = SnmpAdminString
_CfprApLsZoneInitiatorMemberName_Object = MibTableColumn
cfprApLsZoneInitiatorMemberName = _CfprApLsZoneInitiatorMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 5),
    _CfprApLsZoneInitiatorMemberName_Type()
)
cfprApLsZoneInitiatorMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberName.setStatus("current")
_CfprApLsZoneInitiatorMemberUsrLbl_Type = SnmpAdminString
_CfprApLsZoneInitiatorMemberUsrLbl_Object = MibTableColumn
cfprApLsZoneInitiatorMemberUsrLbl = _CfprApLsZoneInitiatorMemberUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 6),
    _CfprApLsZoneInitiatorMemberUsrLbl_Type()
)
cfprApLsZoneInitiatorMemberUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberUsrLbl.setStatus("current")
_CfprApLsZoneInitiatorMemberWwpn_Type = Unsigned64
_CfprApLsZoneInitiatorMemberWwpn_Object = MibTableColumn
cfprApLsZoneInitiatorMemberWwpn = _CfprApLsZoneInitiatorMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 19, 1, 7),
    _CfprApLsZoneInitiatorMemberWwpn_Type()
)
cfprApLsZoneInitiatorMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneInitiatorMemberWwpn.setStatus("current")
_CfprApLsZoneTargetMemberTable_Object = MibTable
cfprApLsZoneTargetMemberTable = _CfprApLsZoneTargetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20)
)
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberTable.setStatus("current")
_CfprApLsZoneTargetMemberEntry_Object = MibTableRow
cfprApLsZoneTargetMemberEntry = _CfprApLsZoneTargetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1)
)
cfprApLsZoneTargetMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LS-MIB", "cfprApLsZoneTargetMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberEntry.setStatus("current")
_CfprApLsZoneTargetMemberInstanceId_Type = CfprApManagedObjectId
_CfprApLsZoneTargetMemberInstanceId_Object = MibTableColumn
cfprApLsZoneTargetMemberInstanceId = _CfprApLsZoneTargetMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 1),
    _CfprApLsZoneTargetMemberInstanceId_Type()
)
cfprApLsZoneTargetMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberInstanceId.setStatus("current")
_CfprApLsZoneTargetMemberDn_Type = CfprApManagedObjectDn
_CfprApLsZoneTargetMemberDn_Object = MibTableColumn
cfprApLsZoneTargetMemberDn = _CfprApLsZoneTargetMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 2),
    _CfprApLsZoneTargetMemberDn_Type()
)
cfprApLsZoneTargetMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberDn.setStatus("current")
_CfprApLsZoneTargetMemberRn_Type = SnmpAdminString
_CfprApLsZoneTargetMemberRn_Object = MibTableColumn
cfprApLsZoneTargetMemberRn = _CfprApLsZoneTargetMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 3),
    _CfprApLsZoneTargetMemberRn_Type()
)
cfprApLsZoneTargetMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberRn.setStatus("current")
_CfprApLsZoneTargetMemberEpDn_Type = SnmpAdminString
_CfprApLsZoneTargetMemberEpDn_Object = MibTableColumn
cfprApLsZoneTargetMemberEpDn = _CfprApLsZoneTargetMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 4),
    _CfprApLsZoneTargetMemberEpDn_Type()
)
cfprApLsZoneTargetMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberEpDn.setStatus("current")
_CfprApLsZoneTargetMemberName_Type = SnmpAdminString
_CfprApLsZoneTargetMemberName_Object = MibTableColumn
cfprApLsZoneTargetMemberName = _CfprApLsZoneTargetMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 5),
    _CfprApLsZoneTargetMemberName_Type()
)
cfprApLsZoneTargetMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberName.setStatus("current")
_CfprApLsZoneTargetMemberUsrLbl_Type = SnmpAdminString
_CfprApLsZoneTargetMemberUsrLbl_Object = MibTableColumn
cfprApLsZoneTargetMemberUsrLbl = _CfprApLsZoneTargetMemberUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 6),
    _CfprApLsZoneTargetMemberUsrLbl_Type()
)
cfprApLsZoneTargetMemberUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberUsrLbl.setStatus("current")
_CfprApLsZoneTargetMemberWwpn_Type = Unsigned64
_CfprApLsZoneTargetMemberWwpn_Object = MibTableColumn
cfprApLsZoneTargetMemberWwpn = _CfprApLsZoneTargetMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 46, 20, 1, 7),
    _CfprApLsZoneTargetMemberWwpn_Type()
)
cfprApLsZoneTargetMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsZoneTargetMemberWwpn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-LS-MIB",
    **{"cfprApLsObjects": cfprApLsObjects,
       "cfprApLsAgentPolicyTable": cfprApLsAgentPolicyTable,
       "cfprApLsAgentPolicyEntry": cfprApLsAgentPolicyEntry,
       "cfprApLsAgentPolicyInstanceId": cfprApLsAgentPolicyInstanceId,
       "cfprApLsAgentPolicyDn": cfprApLsAgentPolicyDn,
       "cfprApLsAgentPolicyRn": cfprApLsAgentPolicyRn,
       "cfprApLsAgentPolicyCapability": cfprApLsAgentPolicyCapability,
       "cfprApLsAgentPolicyDescr": cfprApLsAgentPolicyDescr,
       "cfprApLsAgentPolicyIntId": cfprApLsAgentPolicyIntId,
       "cfprApLsAgentPolicyMode": cfprApLsAgentPolicyMode,
       "cfprApLsAgentPolicyName": cfprApLsAgentPolicyName,
       "cfprApLsAgentPolicyPolicyLevel": cfprApLsAgentPolicyPolicyLevel,
       "cfprApLsAgentPolicyPolicyOwner": cfprApLsAgentPolicyPolicyOwner,
       "cfprApLsBindingTable": cfprApLsBindingTable,
       "cfprApLsBindingEntry": cfprApLsBindingEntry,
       "cfprApLsBindingInstanceId": cfprApLsBindingInstanceId,
       "cfprApLsBindingDn": cfprApLsBindingDn,
       "cfprApLsBindingRn": cfprApLsBindingRn,
       "cfprApLsBindingAssignedToDn": cfprApLsBindingAssignedToDn,
       "cfprApLsBindingComputeEpDn": cfprApLsBindingComputeEpDn,
       "cfprApLsBindingIssues": cfprApLsBindingIssues,
       "cfprApLsBindingName": cfprApLsBindingName,
       "cfprApLsBindingOperState": cfprApLsBindingOperState,
       "cfprApLsBindingPnDn": cfprApLsBindingPnDn,
       "cfprApLsBindingRestrictMigration": cfprApLsBindingRestrictMigration,
       "cfprApLsFcLocaleTable": cfprApLsFcLocaleTable,
       "cfprApLsFcLocaleEntry": cfprApLsFcLocaleEntry,
       "cfprApLsFcLocaleInstanceId": cfprApLsFcLocaleInstanceId,
       "cfprApLsFcLocaleDn": cfprApLsFcLocaleDn,
       "cfprApLsFcLocaleRn": cfprApLsFcLocaleRn,
       "cfprApLsFcLocaleSwitchId": cfprApLsFcLocaleSwitchId,
       "cfprApLsFcZoneTable": cfprApLsFcZoneTable,
       "cfprApLsFcZoneEntry": cfprApLsFcZoneEntry,
       "cfprApLsFcZoneInstanceId": cfprApLsFcZoneInstanceId,
       "cfprApLsFcZoneDn": cfprApLsFcZoneDn,
       "cfprApLsFcZoneRn": cfprApLsFcZoneRn,
       "cfprApLsFcZoneAdminState": cfprApLsFcZoneAdminState,
       "cfprApLsFcZoneId": cfprApLsFcZoneId,
       "cfprApLsFcZoneIdentity": cfprApLsFcZoneIdentity,
       "cfprApLsFcZoneIniName": cfprApLsFcZoneIniName,
       "cfprApLsFcZoneName": cfprApLsFcZoneName,
       "cfprApLsFcZoneOperState": cfprApLsFcZoneOperState,
       "cfprApLsFcZonePeerDn": cfprApLsFcZonePeerDn,
       "cfprApLsFcZoneSwitchId": cfprApLsFcZoneSwitchId,
       "cfprApLsFcZoneUsrLbl": cfprApLsFcZoneUsrLbl,
       "cfprApLsFcZoneVnetId": cfprApLsFcZoneVnetId,
       "cfprApLsFcZoneZoningType": cfprApLsFcZoneZoningType,
       "cfprApLsFcZoneGroupTable": cfprApLsFcZoneGroupTable,
       "cfprApLsFcZoneGroupEntry": cfprApLsFcZoneGroupEntry,
       "cfprApLsFcZoneGroupInstanceId": cfprApLsFcZoneGroupInstanceId,
       "cfprApLsFcZoneGroupDn": cfprApLsFcZoneGroupDn,
       "cfprApLsFcZoneGroupRn": cfprApLsFcZoneGroupRn,
       "cfprApLsFcZoneGroupId": cfprApLsFcZoneGroupId,
       "cfprApLsFcZoneGroupName": cfprApLsFcZoneGroupName,
       "cfprApLsFcZoneGroupSwitchId": cfprApLsFcZoneGroupSwitchId,
       "cfprApLsIssuesTable": cfprApLsIssuesTable,
       "cfprApLsIssuesEntry": cfprApLsIssuesEntry,
       "cfprApLsIssuesInstanceId": cfprApLsIssuesInstanceId,
       "cfprApLsIssuesDn": cfprApLsIssuesDn,
       "cfprApLsIssuesRn": cfprApLsIssuesRn,
       "cfprApLsIssuesConfigWarnings": cfprApLsIssuesConfigWarnings,
       "cfprApLsIssuesIscsiConfigIssues": cfprApLsIssuesIscsiConfigIssues,
       "cfprApLsIssuesNetworkConfigIssues": cfprApLsIssuesNetworkConfigIssues,
       "cfprApLsIssuesServerConfigIssues": cfprApLsIssuesServerConfigIssues,
       "cfprApLsIssuesStorageConfigIssues": cfprApLsIssuesStorageConfigIssues,
       "cfprApLsIssuesVnicConfigIssues": cfprApLsIssuesVnicConfigIssues,
       "cfprApLsPowerTable": cfprApLsPowerTable,
       "cfprApLsPowerEntry": cfprApLsPowerEntry,
       "cfprApLsPowerInstanceId": cfprApLsPowerInstanceId,
       "cfprApLsPowerDn": cfprApLsPowerDn,
       "cfprApLsPowerRn": cfprApLsPowerRn,
       "cfprApLsPowerState": cfprApLsPowerState,
       "cfprApLsRequirementTable": cfprApLsRequirementTable,
       "cfprApLsRequirementEntry": cfprApLsRequirementEntry,
       "cfprApLsRequirementInstanceId": cfprApLsRequirementInstanceId,
       "cfprApLsRequirementDn": cfprApLsRequirementDn,
       "cfprApLsRequirementRn": cfprApLsRequirementRn,
       "cfprApLsRequirementAssignedToDn": cfprApLsRequirementAssignedToDn,
       "cfprApLsRequirementComputeEpDn": cfprApLsRequirementComputeEpDn,
       "cfprApLsRequirementIssues": cfprApLsRequirementIssues,
       "cfprApLsRequirementName": cfprApLsRequirementName,
       "cfprApLsRequirementOperName": cfprApLsRequirementOperName,
       "cfprApLsRequirementOperState": cfprApLsRequirementOperState,
       "cfprApLsRequirementPnDn": cfprApLsRequirementPnDn,
       "cfprApLsRequirementPnPoolDn": cfprApLsRequirementPnPoolDn,
       "cfprApLsRequirementQualifier": cfprApLsRequirementQualifier,
       "cfprApLsRequirementRestrictMigration": cfprApLsRequirementRestrictMigration,
       "cfprApLsServerTable": cfprApLsServerTable,
       "cfprApLsServerEntry": cfprApLsServerEntry,
       "cfprApLsServerInstanceId": cfprApLsServerInstanceId,
       "cfprApLsServerDn": cfprApLsServerDn,
       "cfprApLsServerRn": cfprApLsServerRn,
       "cfprApLsServerAgentPolicyName": cfprApLsServerAgentPolicyName,
       "cfprApLsServerAssignState": cfprApLsServerAssignState,
       "cfprApLsServerAssocState": cfprApLsServerAssocState,
       "cfprApLsServerBiosProfileName": cfprApLsServerBiosProfileName,
       "cfprApLsServerBootPolicyName": cfprApLsServerBootPolicyName,
       "cfprApLsServerConfigQualifier": cfprApLsServerConfigQualifier,
       "cfprApLsServerConfigState": cfprApLsServerConfigState,
       "cfprApLsServerDescr": cfprApLsServerDescr,
       "cfprApLsServerDynamicConPolicyName": cfprApLsServerDynamicConPolicyName,
       "cfprApLsServerExtIPPoolName": cfprApLsServerExtIPPoolName,
       "cfprApLsServerExtIPState": cfprApLsServerExtIPState,
       "cfprApLsServerFltAggr": cfprApLsServerFltAggr,
       "cfprApLsServerFsmDescr": cfprApLsServerFsmDescr,
       "cfprApLsServerFsmFlags": cfprApLsServerFsmFlags,
       "cfprApLsServerFsmPrev": cfprApLsServerFsmPrev,
       "cfprApLsServerFsmProgr": cfprApLsServerFsmProgr,
       "cfprApLsServerFsmRmtInvErrCode": cfprApLsServerFsmRmtInvErrCode,
       "cfprApLsServerFsmRmtInvErrDescr": cfprApLsServerFsmRmtInvErrDescr,
       "cfprApLsServerFsmRmtInvRslt": cfprApLsServerFsmRmtInvRslt,
       "cfprApLsServerFsmStageDescr": cfprApLsServerFsmStageDescr,
       "cfprApLsServerFsmStamp": cfprApLsServerFsmStamp,
       "cfprApLsServerFsmStatus": cfprApLsServerFsmStatus,
       "cfprApLsServerFsmTry": cfprApLsServerFsmTry,
       "cfprApLsServerHostFwPolicyName": cfprApLsServerHostFwPolicyName,
       "cfprApLsServerIdentPoolName": cfprApLsServerIdentPoolName,
       "cfprApLsServerIntId": cfprApLsServerIntId,
       "cfprApLsServerLocalDiskPolicyName": cfprApLsServerLocalDiskPolicyName,
       "cfprApLsServerMaintPolicyName": cfprApLsServerMaintPolicyName,
       "cfprApLsServerMgmtAccessPolicyName": cfprApLsServerMgmtAccessPolicyName,
       "cfprApLsServerMgmtFwPolicyName": cfprApLsServerMgmtFwPolicyName,
       "cfprApLsServerName": cfprApLsServerName,
       "cfprApLsServerOperBiosProfileName": cfprApLsServerOperBiosProfileName,
       "cfprApLsServerOperBootPolicyName": cfprApLsServerOperBootPolicyName,
       "cfprApLsServerOperDynamicConPolicyName": cfprApLsServerOperDynamicConPolicyName,
       "cfprApLsServerOperExtIPPoolName": cfprApLsServerOperExtIPPoolName,
       "cfprApLsServerOperHostFwPolicyName": cfprApLsServerOperHostFwPolicyName,
       "cfprApLsServerOperIdentPoolName": cfprApLsServerOperIdentPoolName,
       "cfprApLsServerOperLocalDiskPolicyName": cfprApLsServerOperLocalDiskPolicyName,
       "cfprApLsServerOperMaintPolicyName": cfprApLsServerOperMaintPolicyName,
       "cfprApLsServerOperMgmtAccessPolicyName": cfprApLsServerOperMgmtAccessPolicyName,
       "cfprApLsServerOperMgmtFwPolicyName": cfprApLsServerOperMgmtFwPolicyName,
       "cfprApLsServerOperPowerPolicyName": cfprApLsServerOperPowerPolicyName,
       "cfprApLsServerOperScrubPolicyName": cfprApLsServerOperScrubPolicyName,
       "cfprApLsServerOperSolPolicyName": cfprApLsServerOperSolPolicyName,
       "cfprApLsServerOperSrcTemplName": cfprApLsServerOperSrcTemplName,
       "cfprApLsServerOperState": cfprApLsServerOperState,
       "cfprApLsServerOperStatsPolicyName": cfprApLsServerOperStatsPolicyName,
       "cfprApLsServerOperVconProfileName": cfprApLsServerOperVconProfileName,
       "cfprApLsServerOwner": cfprApLsServerOwner,
       "cfprApLsServerPnDn": cfprApLsServerPnDn,
       "cfprApLsServerPolicyLevel": cfprApLsServerPolicyLevel,
       "cfprApLsServerPolicyOwner": cfprApLsServerPolicyOwner,
       "cfprApLsServerPowerPolicyName": cfprApLsServerPowerPolicyName,
       "cfprApLsServerResolveRemote": cfprApLsServerResolveRemote,
       "cfprApLsServerScrubPolicyName": cfprApLsServerScrubPolicyName,
       "cfprApLsServerSolPolicyName": cfprApLsServerSolPolicyName,
       "cfprApLsServerSrcTemplName": cfprApLsServerSrcTemplName,
       "cfprApLsServerStatsPolicyName": cfprApLsServerStatsPolicyName,
       "cfprApLsServerSvnicConfig": cfprApLsServerSvnicConfig,
       "cfprApLsServerType": cfprApLsServerType,
       "cfprApLsServerUsrLbl": cfprApLsServerUsrLbl,
       "cfprApLsServerUuid": cfprApLsServerUuid,
       "cfprApLsServerUuidSuffix": cfprApLsServerUuidSuffix,
       "cfprApLsServerVconProfileName": cfprApLsServerVconProfileName,
       "cfprApLsServerAssocCtxTable": cfprApLsServerAssocCtxTable,
       "cfprApLsServerAssocCtxEntry": cfprApLsServerAssocCtxEntry,
       "cfprApLsServerAssocCtxInstanceId": cfprApLsServerAssocCtxInstanceId,
       "cfprApLsServerAssocCtxDn": cfprApLsServerAssocCtxDn,
       "cfprApLsServerAssocCtxRn": cfprApLsServerAssocCtxRn,
       "cfprApLsServerExtensionTable": cfprApLsServerExtensionTable,
       "cfprApLsServerExtensionEntry": cfprApLsServerExtensionEntry,
       "cfprApLsServerExtensionInstanceId": cfprApLsServerExtensionInstanceId,
       "cfprApLsServerExtensionDn": cfprApLsServerExtensionDn,
       "cfprApLsServerExtensionRn": cfprApLsServerExtensionRn,
       "cfprApLsServerExtensionGuid": cfprApLsServerExtensionGuid,
       "cfprApLsServerExtensionVersion": cfprApLsServerExtensionVersion,
       "cfprApLsServerFsmTable": cfprApLsServerFsmTable,
       "cfprApLsServerFsmEntry": cfprApLsServerFsmEntry,
       "cfprApLsServerFsmInstanceId": cfprApLsServerFsmInstanceId,
       "cfprApLsServerFsmDn": cfprApLsServerFsmDn,
       "cfprApLsServerFsmRn": cfprApLsServerFsmRn,
       "cfprApLsServerFsmCompletionTime": cfprApLsServerFsmCompletionTime,
       "cfprApLsServerFsmCurrentFsm": cfprApLsServerFsmCurrentFsm,
       "cfprApLsServerFsmDescrData": cfprApLsServerFsmDescrData,
       "cfprApLsServerFsmFsmStatus": cfprApLsServerFsmFsmStatus,
       "cfprApLsServerFsmProgress": cfprApLsServerFsmProgress,
       "cfprApLsServerFsmRmtErrCode": cfprApLsServerFsmRmtErrCode,
       "cfprApLsServerFsmRmtErrDescr": cfprApLsServerFsmRmtErrDescr,
       "cfprApLsServerFsmRmtRslt": cfprApLsServerFsmRmtRslt,
       "cfprApLsServerFsmStageTable": cfprApLsServerFsmStageTable,
       "cfprApLsServerFsmStageEntry": cfprApLsServerFsmStageEntry,
       "cfprApLsServerFsmStageInstanceId": cfprApLsServerFsmStageInstanceId,
       "cfprApLsServerFsmStageDn": cfprApLsServerFsmStageDn,
       "cfprApLsServerFsmStageRn": cfprApLsServerFsmStageRn,
       "cfprApLsServerFsmStageDescrData": cfprApLsServerFsmStageDescrData,
       "cfprApLsServerFsmStageLastUpdateTime": cfprApLsServerFsmStageLastUpdateTime,
       "cfprApLsServerFsmStageName": cfprApLsServerFsmStageName,
       "cfprApLsServerFsmStageOrder": cfprApLsServerFsmStageOrder,
       "cfprApLsServerFsmStageRetry": cfprApLsServerFsmStageRetry,
       "cfprApLsServerFsmStageStageStatus": cfprApLsServerFsmStageStageStatus,
       "cfprApLsServerFsmTaskTable": cfprApLsServerFsmTaskTable,
       "cfprApLsServerFsmTaskEntry": cfprApLsServerFsmTaskEntry,
       "cfprApLsServerFsmTaskInstanceId": cfprApLsServerFsmTaskInstanceId,
       "cfprApLsServerFsmTaskDn": cfprApLsServerFsmTaskDn,
       "cfprApLsServerFsmTaskRn": cfprApLsServerFsmTaskRn,
       "cfprApLsServerFsmTaskCompletion": cfprApLsServerFsmTaskCompletion,
       "cfprApLsServerFsmTaskFlags": cfprApLsServerFsmTaskFlags,
       "cfprApLsServerFsmTaskItem": cfprApLsServerFsmTaskItem,
       "cfprApLsServerFsmTaskSeqId": cfprApLsServerFsmTaskSeqId,
       "cfprApLsTierTable": cfprApLsTierTable,
       "cfprApLsTierEntry": cfprApLsTierEntry,
       "cfprApLsTierInstanceId": cfprApLsTierInstanceId,
       "cfprApLsTierDn": cfprApLsTierDn,
       "cfprApLsTierRn": cfprApLsTierRn,
       "cfprApLsTierApply": cfprApLsTierApply,
       "cfprApLsTierDescr": cfprApLsTierDescr,
       "cfprApLsTierIntId": cfprApLsTierIntId,
       "cfprApLsTierName": cfprApLsTierName,
       "cfprApLsTierPolicyLevel": cfprApLsTierPolicyLevel,
       "cfprApLsTierPolicyOwner": cfprApLsTierPolicyOwner,
       "cfprApLsTierSrcTemplName": cfprApLsTierSrcTemplName,
       "cfprApLsUuidHistoryTable": cfprApLsUuidHistoryTable,
       "cfprApLsUuidHistoryEntry": cfprApLsUuidHistoryEntry,
       "cfprApLsUuidHistoryInstanceId": cfprApLsUuidHistoryInstanceId,
       "cfprApLsUuidHistoryDn": cfprApLsUuidHistoryDn,
       "cfprApLsUuidHistoryRn": cfprApLsUuidHistoryRn,
       "cfprApLsUuidHistoryOlduuid": cfprApLsUuidHistoryOlduuid,
       "cfprApLsVConAssignTable": cfprApLsVConAssignTable,
       "cfprApLsVConAssignEntry": cfprApLsVConAssignEntry,
       "cfprApLsVConAssignInstanceId": cfprApLsVConAssignInstanceId,
       "cfprApLsVConAssignDn": cfprApLsVConAssignDn,
       "cfprApLsVConAssignRn": cfprApLsVConAssignRn,
       "cfprApLsVConAssignAdminVcon": cfprApLsVConAssignAdminVcon,
       "cfprApLsVConAssignOrder": cfprApLsVConAssignOrder,
       "cfprApLsVConAssignTransport": cfprApLsVConAssignTransport,
       "cfprApLsVConAssignVnicName": cfprApLsVConAssignVnicName,
       "cfprApLsVersionBehTable": cfprApLsVersionBehTable,
       "cfprApLsVersionBehEntry": cfprApLsVersionBehEntry,
       "cfprApLsVersionBehInstanceId": cfprApLsVersionBehInstanceId,
       "cfprApLsVersionBehDn": cfprApLsVersionBehDn,
       "cfprApLsVersionBehRn": cfprApLsVersionBehRn,
       "cfprApLsVersionBehPciEnum": cfprApLsVersionBehPciEnum,
       "cfprApLsVersionBehVconMap": cfprApLsVersionBehVconMap,
       "cfprApLsVersionBehVnicMap": cfprApLsVersionBehVnicMap,
       "cfprApLsVersionBehVnicOrder": cfprApLsVersionBehVnicOrder,
       "cfprApLsZoneInitiatorMemberTable": cfprApLsZoneInitiatorMemberTable,
       "cfprApLsZoneInitiatorMemberEntry": cfprApLsZoneInitiatorMemberEntry,
       "cfprApLsZoneInitiatorMemberInstanceId": cfprApLsZoneInitiatorMemberInstanceId,
       "cfprApLsZoneInitiatorMemberDn": cfprApLsZoneInitiatorMemberDn,
       "cfprApLsZoneInitiatorMemberRn": cfprApLsZoneInitiatorMemberRn,
       "cfprApLsZoneInitiatorMemberEpDn": cfprApLsZoneInitiatorMemberEpDn,
       "cfprApLsZoneInitiatorMemberName": cfprApLsZoneInitiatorMemberName,
       "cfprApLsZoneInitiatorMemberUsrLbl": cfprApLsZoneInitiatorMemberUsrLbl,
       "cfprApLsZoneInitiatorMemberWwpn": cfprApLsZoneInitiatorMemberWwpn,
       "cfprApLsZoneTargetMemberTable": cfprApLsZoneTargetMemberTable,
       "cfprApLsZoneTargetMemberEntry": cfprApLsZoneTargetMemberEntry,
       "cfprApLsZoneTargetMemberInstanceId": cfprApLsZoneTargetMemberInstanceId,
       "cfprApLsZoneTargetMemberDn": cfprApLsZoneTargetMemberDn,
       "cfprApLsZoneTargetMemberRn": cfprApLsZoneTargetMemberRn,
       "cfprApLsZoneTargetMemberEpDn": cfprApLsZoneTargetMemberEpDn,
       "cfprApLsZoneTargetMemberName": cfprApLsZoneTargetMemberName,
       "cfprApLsZoneTargetMemberUsrLbl": cfprApLsZoneTargetMemberUsrLbl,
       "cfprApLsZoneTargetMemberWwpn": cfprApLsZoneTargetMemberWwpn}
)
