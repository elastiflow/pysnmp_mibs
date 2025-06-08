# SNMP MIB module (CISCO-FIREPOWER-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-CONFIG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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

(CfprConfigImpactResponseState,
 CfprConfigSorterDirection,
 CfprLsConfigIssues,
 CfprLsConfigState,
 CfprMoMoClassId,
 CfprTrigAckChanges,
 CfprTrigAckMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConfigImpactResponseState",
    "CfprConfigSorterDirection",
    "CfprLsConfigIssues",
    "CfprLsConfigState",
    "CfprMoMoClassId",
    "CfprTrigAckChanges",
    "CfprTrigAckMode")

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

cfprConfigObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprConfigImpactTable_Object = MibTable
cfprConfigImpactTable = _CfprConfigImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cfprConfigImpactTable.setStatus("current")
_CfprConfigImpactEntry_Object = MibTableRow
cfprConfigImpactEntry = _CfprConfigImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1)
)
cfprConfigImpactEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CONFIG-MIB", "cfprConfigImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cfprConfigImpactEntry.setStatus("current")
_CfprConfigImpactInstanceId_Type = CfprManagedObjectId
_CfprConfigImpactInstanceId_Object = MibTableColumn
cfprConfigImpactInstanceId = _CfprConfigImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 1),
    _CfprConfigImpactInstanceId_Type()
)
cfprConfigImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprConfigImpactInstanceId.setStatus("current")
_CfprConfigImpactDn_Type = CfprManagedObjectDn
_CfprConfigImpactDn_Object = MibTableColumn
cfprConfigImpactDn = _CfprConfigImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 2),
    _CfprConfigImpactDn_Type()
)
cfprConfigImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactDn.setStatus("current")
_CfprConfigImpactRn_Type = SnmpAdminString
_CfprConfigImpactRn_Object = MibTableColumn
cfprConfigImpactRn = _CfprConfigImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 3),
    _CfprConfigImpactRn_Type()
)
cfprConfigImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactRn.setStatus("current")
_CfprConfigImpactAffectedObj_Type = SnmpAdminString
_CfprConfigImpactAffectedObj_Object = MibTableColumn
cfprConfigImpactAffectedObj = _CfprConfigImpactAffectedObj_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 4),
    _CfprConfigImpactAffectedObj_Type()
)
cfprConfigImpactAffectedObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactAffectedObj.setStatus("current")
_CfprConfigImpactAffectedServer_Type = SnmpAdminString
_CfprConfigImpactAffectedServer_Object = MibTableColumn
cfprConfigImpactAffectedServer = _CfprConfigImpactAffectedServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 5),
    _CfprConfigImpactAffectedServer_Type()
)
cfprConfigImpactAffectedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactAffectedServer.setStatus("current")
_CfprConfigImpactChanges_Type = CfprTrigAckChanges
_CfprConfigImpactChanges_Object = MibTableColumn
cfprConfigImpactChanges = _CfprConfigImpactChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 6),
    _CfprConfigImpactChanges_Type()
)
cfprConfigImpactChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactChanges.setStatus("current")
_CfprConfigImpactConfigIssues_Type = CfprLsConfigIssues
_CfprConfigImpactConfigIssues_Object = MibTableColumn
cfprConfigImpactConfigIssues = _CfprConfigImpactConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 7),
    _CfprConfigImpactConfigIssues_Type()
)
cfprConfigImpactConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactConfigIssues.setStatus("current")
_CfprConfigImpactConfigQualifier_Type = CfprLsConfigIssues
_CfprConfigImpactConfigQualifier_Object = MibTableColumn
cfprConfigImpactConfigQualifier = _CfprConfigImpactConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 8),
    _CfprConfigImpactConfigQualifier_Type()
)
cfprConfigImpactConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactConfigQualifier.setStatus("current")
_CfprConfigImpactConfigState_Type = CfprLsConfigState
_CfprConfigImpactConfigState_Object = MibTableColumn
cfprConfigImpactConfigState = _CfprConfigImpactConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 9),
    _CfprConfigImpactConfigState_Type()
)
cfprConfigImpactConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactConfigState.setStatus("current")
_CfprConfigImpactDeploymentMode_Type = CfprTrigAckMode
_CfprConfigImpactDeploymentMode_Object = MibTableColumn
cfprConfigImpactDeploymentMode = _CfprConfigImpactDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 10),
    _CfprConfigImpactDeploymentMode_Type()
)
cfprConfigImpactDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactDeploymentMode.setStatus("current")
_CfprConfigImpactName_Type = SnmpAdminString
_CfprConfigImpactName_Object = MibTableColumn
cfprConfigImpactName = _CfprConfigImpactName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 11),
    _CfprConfigImpactName_Type()
)
cfprConfigImpactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactName.setStatus("current")
_CfprConfigImpactRebootRequired_Type = TruthValue
_CfprConfigImpactRebootRequired_Object = MibTableColumn
cfprConfigImpactRebootRequired = _CfprConfigImpactRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 1, 1, 12),
    _CfprConfigImpactRebootRequired_Type()
)
cfprConfigImpactRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigImpactRebootRequired.setStatus("current")
_CfprConfigManagedEpImpactResponseTable_Object = MibTable
cfprConfigManagedEpImpactResponseTable = _CfprConfigManagedEpImpactResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2)
)
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseTable.setStatus("current")
_CfprConfigManagedEpImpactResponseEntry_Object = MibTableRow
cfprConfigManagedEpImpactResponseEntry = _CfprConfigManagedEpImpactResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1)
)
cfprConfigManagedEpImpactResponseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CONFIG-MIB", "cfprConfigManagedEpImpactResponseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseEntry.setStatus("current")
_CfprConfigManagedEpImpactResponseInstanceId_Type = CfprManagedObjectId
_CfprConfigManagedEpImpactResponseInstanceId_Object = MibTableColumn
cfprConfigManagedEpImpactResponseInstanceId = _CfprConfigManagedEpImpactResponseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 1),
    _CfprConfigManagedEpImpactResponseInstanceId_Type()
)
cfprConfigManagedEpImpactResponseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseInstanceId.setStatus("current")
_CfprConfigManagedEpImpactResponseDn_Type = CfprManagedObjectDn
_CfprConfigManagedEpImpactResponseDn_Object = MibTableColumn
cfprConfigManagedEpImpactResponseDn = _CfprConfigManagedEpImpactResponseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 2),
    _CfprConfigManagedEpImpactResponseDn_Type()
)
cfprConfigManagedEpImpactResponseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseDn.setStatus("current")
_CfprConfigManagedEpImpactResponseRn_Type = SnmpAdminString
_CfprConfigManagedEpImpactResponseRn_Object = MibTableColumn
cfprConfigManagedEpImpactResponseRn = _CfprConfigManagedEpImpactResponseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 3),
    _CfprConfigManagedEpImpactResponseRn_Type()
)
cfprConfigManagedEpImpactResponseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseRn.setStatus("current")
_CfprConfigManagedEpImpactResponseAffectedServers_Type = Gauge32
_CfprConfigManagedEpImpactResponseAffectedServers_Object = MibTableColumn
cfprConfigManagedEpImpactResponseAffectedServers = _CfprConfigManagedEpImpactResponseAffectedServers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 4),
    _CfprConfigManagedEpImpactResponseAffectedServers_Type()
)
cfprConfigManagedEpImpactResponseAffectedServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseAffectedServers.setStatus("current")
_CfprConfigManagedEpImpactResponseAppConnectorId_Type = Gauge32
_CfprConfigManagedEpImpactResponseAppConnectorId_Object = MibTableColumn
cfprConfigManagedEpImpactResponseAppConnectorId = _CfprConfigManagedEpImpactResponseAppConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 5),
    _CfprConfigManagedEpImpactResponseAppConnectorId_Type()
)
cfprConfigManagedEpImpactResponseAppConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseAppConnectorId.setStatus("current")
_CfprConfigManagedEpImpactResponseEpName_Type = SnmpAdminString
_CfprConfigManagedEpImpactResponseEpName_Object = MibTableColumn
cfprConfigManagedEpImpactResponseEpName = _CfprConfigManagedEpImpactResponseEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 6),
    _CfprConfigManagedEpImpactResponseEpName_Type()
)
cfprConfigManagedEpImpactResponseEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseEpName.setStatus("current")
_CfprConfigManagedEpImpactResponseImpactAnalyzerId_Type = DateAndTime
_CfprConfigManagedEpImpactResponseImpactAnalyzerId_Object = MibTableColumn
cfprConfigManagedEpImpactResponseImpactAnalyzerId = _CfprConfigManagedEpImpactResponseImpactAnalyzerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 7),
    _CfprConfigManagedEpImpactResponseImpactAnalyzerId_Type()
)
cfprConfigManagedEpImpactResponseImpactAnalyzerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseImpactAnalyzerId.setStatus("current")
_CfprConfigManagedEpImpactResponseRebootRequired_Type = TruthValue
_CfprConfigManagedEpImpactResponseRebootRequired_Object = MibTableColumn
cfprConfigManagedEpImpactResponseRebootRequired = _CfprConfigManagedEpImpactResponseRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 8),
    _CfprConfigManagedEpImpactResponseRebootRequired_Type()
)
cfprConfigManagedEpImpactResponseRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseRebootRequired.setStatus("current")
_CfprConfigManagedEpImpactResponseSourceConnectorId_Type = Gauge32
_CfprConfigManagedEpImpactResponseSourceConnectorId_Object = MibTableColumn
cfprConfigManagedEpImpactResponseSourceConnectorId = _CfprConfigManagedEpImpactResponseSourceConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 9),
    _CfprConfigManagedEpImpactResponseSourceConnectorId_Type()
)
cfprConfigManagedEpImpactResponseSourceConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseSourceConnectorId.setStatus("current")
_CfprConfigManagedEpImpactResponseState_Type = CfprConfigImpactResponseState
_CfprConfigManagedEpImpactResponseState_Object = MibTableColumn
cfprConfigManagedEpImpactResponseState = _CfprConfigManagedEpImpactResponseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 2, 1, 10),
    _CfprConfigManagedEpImpactResponseState_Type()
)
cfprConfigManagedEpImpactResponseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigManagedEpImpactResponseState.setStatus("current")
_CfprConfigSorterTable_Object = MibTable
cfprConfigSorterTable = _CfprConfigSorterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3)
)
if mibBuilder.loadTexts:
    cfprConfigSorterTable.setStatus("current")
_CfprConfigSorterEntry_Object = MibTableRow
cfprConfigSorterEntry = _CfprConfigSorterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1)
)
cfprConfigSorterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CONFIG-MIB", "cfprConfigSorterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprConfigSorterEntry.setStatus("current")
_CfprConfigSorterInstanceId_Type = CfprManagedObjectId
_CfprConfigSorterInstanceId_Object = MibTableColumn
cfprConfigSorterInstanceId = _CfprConfigSorterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1, 1),
    _CfprConfigSorterInstanceId_Type()
)
cfprConfigSorterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprConfigSorterInstanceId.setStatus("current")
_CfprConfigSorterDn_Type = CfprManagedObjectDn
_CfprConfigSorterDn_Object = MibTableColumn
cfprConfigSorterDn = _CfprConfigSorterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1, 2),
    _CfprConfigSorterDn_Type()
)
cfprConfigSorterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigSorterDn.setStatus("current")
_CfprConfigSorterRn_Type = SnmpAdminString
_CfprConfigSorterRn_Object = MibTableColumn
cfprConfigSorterRn = _CfprConfigSorterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1, 3),
    _CfprConfigSorterRn_Type()
)
cfprConfigSorterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigSorterRn.setStatus("current")
_CfprConfigSorterDirection_Type = CfprConfigSorterDirection
_CfprConfigSorterDirection_Object = MibTableColumn
cfprConfigSorterDirection = _CfprConfigSorterDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1, 4),
    _CfprConfigSorterDirection_Type()
)
cfprConfigSorterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigSorterDirection.setStatus("current")
_CfprConfigSorterSortClass_Type = CfprMoMoClassId
_CfprConfigSorterSortClass_Object = MibTableColumn
cfprConfigSorterSortClass = _CfprConfigSorterSortClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1, 5),
    _CfprConfigSorterSortClass_Type()
)
cfprConfigSorterSortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigSorterSortClass.setStatus("current")
_CfprConfigSorterSortProp_Type = SnmpAdminString
_CfprConfigSorterSortProp_Object = MibTableColumn
cfprConfigSorterSortProp = _CfprConfigSorterSortProp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 13, 3, 1, 6),
    _CfprConfigSorterSortProp_Type()
)
cfprConfigSorterSortProp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprConfigSorterSortProp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-CONFIG-MIB",
    **{"cfprConfigObjects": cfprConfigObjects,
       "cfprConfigImpactTable": cfprConfigImpactTable,
       "cfprConfigImpactEntry": cfprConfigImpactEntry,
       "cfprConfigImpactInstanceId": cfprConfigImpactInstanceId,
       "cfprConfigImpactDn": cfprConfigImpactDn,
       "cfprConfigImpactRn": cfprConfigImpactRn,
       "cfprConfigImpactAffectedObj": cfprConfigImpactAffectedObj,
       "cfprConfigImpactAffectedServer": cfprConfigImpactAffectedServer,
       "cfprConfigImpactChanges": cfprConfigImpactChanges,
       "cfprConfigImpactConfigIssues": cfprConfigImpactConfigIssues,
       "cfprConfigImpactConfigQualifier": cfprConfigImpactConfigQualifier,
       "cfprConfigImpactConfigState": cfprConfigImpactConfigState,
       "cfprConfigImpactDeploymentMode": cfprConfigImpactDeploymentMode,
       "cfprConfigImpactName": cfprConfigImpactName,
       "cfprConfigImpactRebootRequired": cfprConfigImpactRebootRequired,
       "cfprConfigManagedEpImpactResponseTable": cfprConfigManagedEpImpactResponseTable,
       "cfprConfigManagedEpImpactResponseEntry": cfprConfigManagedEpImpactResponseEntry,
       "cfprConfigManagedEpImpactResponseInstanceId": cfprConfigManagedEpImpactResponseInstanceId,
       "cfprConfigManagedEpImpactResponseDn": cfprConfigManagedEpImpactResponseDn,
       "cfprConfigManagedEpImpactResponseRn": cfprConfigManagedEpImpactResponseRn,
       "cfprConfigManagedEpImpactResponseAffectedServers": cfprConfigManagedEpImpactResponseAffectedServers,
       "cfprConfigManagedEpImpactResponseAppConnectorId": cfprConfigManagedEpImpactResponseAppConnectorId,
       "cfprConfigManagedEpImpactResponseEpName": cfprConfigManagedEpImpactResponseEpName,
       "cfprConfigManagedEpImpactResponseImpactAnalyzerId": cfprConfigManagedEpImpactResponseImpactAnalyzerId,
       "cfprConfigManagedEpImpactResponseRebootRequired": cfprConfigManagedEpImpactResponseRebootRequired,
       "cfprConfigManagedEpImpactResponseSourceConnectorId": cfprConfigManagedEpImpactResponseSourceConnectorId,
       "cfprConfigManagedEpImpactResponseState": cfprConfigManagedEpImpactResponseState,
       "cfprConfigSorterTable": cfprConfigSorterTable,
       "cfprConfigSorterEntry": cfprConfigSorterEntry,
       "cfprConfigSorterInstanceId": cfprConfigSorterInstanceId,
       "cfprConfigSorterDn": cfprConfigSorterDn,
       "cfprConfigSorterRn": cfprConfigSorterRn,
       "cfprConfigSorterDirection": cfprConfigSorterDirection,
       "cfprConfigSorterSortClass": cfprConfigSorterSortClass,
       "cfprConfigSorterSortProp": cfprConfigSorterSortProp}
)
