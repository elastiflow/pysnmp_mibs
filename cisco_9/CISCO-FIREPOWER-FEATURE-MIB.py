# SNMP MIB module (CISCO-FIREPOWER-FEATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-FEATURE-MIB.mib
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

(CfprFeatureSupportabilityType,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprFeatureSupportabilityType")

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

cfprFeatureObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprFeatureContextEpTable_Object = MibTable
cfprFeatureContextEpTable = _CfprFeatureContextEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 1)
)
if mibBuilder.loadTexts:
    cfprFeatureContextEpTable.setStatus("current")
_CfprFeatureContextEpEntry_Object = MibTableRow
cfprFeatureContextEpEntry = _CfprFeatureContextEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 1, 1)
)
cfprFeatureContextEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureContextEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureContextEpEntry.setStatus("current")
_CfprFeatureContextEpInstanceId_Type = CfprManagedObjectId
_CfprFeatureContextEpInstanceId_Object = MibTableColumn
cfprFeatureContextEpInstanceId = _CfprFeatureContextEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 1, 1, 1),
    _CfprFeatureContextEpInstanceId_Type()
)
cfprFeatureContextEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureContextEpInstanceId.setStatus("current")
_CfprFeatureContextEpDn_Type = CfprManagedObjectDn
_CfprFeatureContextEpDn_Object = MibTableColumn
cfprFeatureContextEpDn = _CfprFeatureContextEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 1, 1, 2),
    _CfprFeatureContextEpDn_Type()
)
cfprFeatureContextEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureContextEpDn.setStatus("current")
_CfprFeatureContextEpRn_Type = SnmpAdminString
_CfprFeatureContextEpRn_Object = MibTableColumn
cfprFeatureContextEpRn = _CfprFeatureContextEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 1, 1, 3),
    _CfprFeatureContextEpRn_Type()
)
cfprFeatureContextEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureContextEpRn.setStatus("current")
_CfprFeatureDefinitionTable_Object = MibTable
cfprFeatureDefinitionTable = _CfprFeatureDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2)
)
if mibBuilder.loadTexts:
    cfprFeatureDefinitionTable.setStatus("current")
_CfprFeatureDefinitionEntry_Object = MibTableRow
cfprFeatureDefinitionEntry = _CfprFeatureDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1)
)
cfprFeatureDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureDefinitionEntry.setStatus("current")
_CfprFeatureDefinitionInstanceId_Type = CfprManagedObjectId
_CfprFeatureDefinitionInstanceId_Object = MibTableColumn
cfprFeatureDefinitionInstanceId = _CfprFeatureDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1, 1),
    _CfprFeatureDefinitionInstanceId_Type()
)
cfprFeatureDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceId.setStatus("current")
_CfprFeatureDefinitionDn_Type = CfprManagedObjectDn
_CfprFeatureDefinitionDn_Object = MibTableColumn
cfprFeatureDefinitionDn = _CfprFeatureDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1, 2),
    _CfprFeatureDefinitionDn_Type()
)
cfprFeatureDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionDn.setStatus("current")
_CfprFeatureDefinitionRn_Type = SnmpAdminString
_CfprFeatureDefinitionRn_Object = MibTableColumn
cfprFeatureDefinitionRn = _CfprFeatureDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1, 3),
    _CfprFeatureDefinitionRn_Type()
)
cfprFeatureDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRn.setStatus("current")
_CfprFeatureDefinitionDescription_Type = SnmpAdminString
_CfprFeatureDefinitionDescription_Object = MibTableColumn
cfprFeatureDefinitionDescription = _CfprFeatureDefinitionDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1, 4),
    _CfprFeatureDefinitionDescription_Type()
)
cfprFeatureDefinitionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionDescription.setStatus("current")
_CfprFeatureDefinitionName_Type = SnmpAdminString
_CfprFeatureDefinitionName_Object = MibTableColumn
cfprFeatureDefinitionName = _CfprFeatureDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1, 5),
    _CfprFeatureDefinitionName_Type()
)
cfprFeatureDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionName.setStatus("current")
_CfprFeatureDefinitionRevision_Type = SnmpAdminString
_CfprFeatureDefinitionRevision_Object = MibTableColumn
cfprFeatureDefinitionRevision = _CfprFeatureDefinitionRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 2, 1, 6),
    _CfprFeatureDefinitionRevision_Type()
)
cfprFeatureDefinitionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRevision.setStatus("current")
_CfprFeatureDefinitionInstanceTable_Object = MibTable
cfprFeatureDefinitionInstanceTable = _CfprFeatureDefinitionInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3)
)
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceTable.setStatus("current")
_CfprFeatureDefinitionInstanceEntry_Object = MibTableRow
cfprFeatureDefinitionInstanceEntry = _CfprFeatureDefinitionInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1)
)
cfprFeatureDefinitionInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureDefinitionInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceEntry.setStatus("current")
_CfprFeatureDefinitionInstanceInstanceId_Type = CfprManagedObjectId
_CfprFeatureDefinitionInstanceInstanceId_Object = MibTableColumn
cfprFeatureDefinitionInstanceInstanceId = _CfprFeatureDefinitionInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 1),
    _CfprFeatureDefinitionInstanceInstanceId_Type()
)
cfprFeatureDefinitionInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceInstanceId.setStatus("current")
_CfprFeatureDefinitionInstanceDn_Type = CfprManagedObjectDn
_CfprFeatureDefinitionInstanceDn_Object = MibTableColumn
cfprFeatureDefinitionInstanceDn = _CfprFeatureDefinitionInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 2),
    _CfprFeatureDefinitionInstanceDn_Type()
)
cfprFeatureDefinitionInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceDn.setStatus("current")
_CfprFeatureDefinitionInstanceRn_Type = SnmpAdminString
_CfprFeatureDefinitionInstanceRn_Object = MibTableColumn
cfprFeatureDefinitionInstanceRn = _CfprFeatureDefinitionInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 3),
    _CfprFeatureDefinitionInstanceRn_Type()
)
cfprFeatureDefinitionInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceRn.setStatus("current")
_CfprFeatureDefinitionInstanceName_Type = SnmpAdminString
_CfprFeatureDefinitionInstanceName_Object = MibTableColumn
cfprFeatureDefinitionInstanceName = _CfprFeatureDefinitionInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 4),
    _CfprFeatureDefinitionInstanceName_Type()
)
cfprFeatureDefinitionInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceName.setStatus("current")
_CfprFeatureDefinitionInstanceRevision_Type = SnmpAdminString
_CfprFeatureDefinitionInstanceRevision_Object = MibTableColumn
cfprFeatureDefinitionInstanceRevision = _CfprFeatureDefinitionInstanceRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 5),
    _CfprFeatureDefinitionInstanceRevision_Type()
)
cfprFeatureDefinitionInstanceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceRevision.setStatus("current")
_CfprFeatureDefinitionInstanceSupportability_Type = CfprFeatureSupportabilityType
_CfprFeatureDefinitionInstanceSupportability_Object = MibTableColumn
cfprFeatureDefinitionInstanceSupportability = _CfprFeatureDefinitionInstanceSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 6),
    _CfprFeatureDefinitionInstanceSupportability_Type()
)
cfprFeatureDefinitionInstanceSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceSupportability.setStatus("current")
_CfprFeatureDefinitionInstanceTargetDn_Type = SnmpAdminString
_CfprFeatureDefinitionInstanceTargetDn_Object = MibTableColumn
cfprFeatureDefinitionInstanceTargetDn = _CfprFeatureDefinitionInstanceTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 3, 1, 7),
    _CfprFeatureDefinitionInstanceTargetDn_Type()
)
cfprFeatureDefinitionInstanceTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionInstanceTargetDn.setStatus("current")
_CfprFeatureDefinitionRefTable_Object = MibTable
cfprFeatureDefinitionRefTable = _CfprFeatureDefinitionRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4)
)
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefTable.setStatus("current")
_CfprFeatureDefinitionRefEntry_Object = MibTableRow
cfprFeatureDefinitionRefEntry = _CfprFeatureDefinitionRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1)
)
cfprFeatureDefinitionRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureDefinitionRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefEntry.setStatus("current")
_CfprFeatureDefinitionRefInstanceId_Type = CfprManagedObjectId
_CfprFeatureDefinitionRefInstanceId_Object = MibTableColumn
cfprFeatureDefinitionRefInstanceId = _CfprFeatureDefinitionRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 1),
    _CfprFeatureDefinitionRefInstanceId_Type()
)
cfprFeatureDefinitionRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefInstanceId.setStatus("current")
_CfprFeatureDefinitionRefDn_Type = CfprManagedObjectDn
_CfprFeatureDefinitionRefDn_Object = MibTableColumn
cfprFeatureDefinitionRefDn = _CfprFeatureDefinitionRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 2),
    _CfprFeatureDefinitionRefDn_Type()
)
cfprFeatureDefinitionRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefDn.setStatus("current")
_CfprFeatureDefinitionRefRn_Type = SnmpAdminString
_CfprFeatureDefinitionRefRn_Object = MibTableColumn
cfprFeatureDefinitionRefRn = _CfprFeatureDefinitionRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 3),
    _CfprFeatureDefinitionRefRn_Type()
)
cfprFeatureDefinitionRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefRn.setStatus("current")
_CfprFeatureDefinitionRefName_Type = SnmpAdminString
_CfprFeatureDefinitionRefName_Object = MibTableColumn
cfprFeatureDefinitionRefName = _CfprFeatureDefinitionRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 4),
    _CfprFeatureDefinitionRefName_Type()
)
cfprFeatureDefinitionRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefName.setStatus("current")
_CfprFeatureDefinitionRefRevision_Type = SnmpAdminString
_CfprFeatureDefinitionRefRevision_Object = MibTableColumn
cfprFeatureDefinitionRefRevision = _CfprFeatureDefinitionRefRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 5),
    _CfprFeatureDefinitionRefRevision_Type()
)
cfprFeatureDefinitionRefRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefRevision.setStatus("current")
_CfprFeatureDefinitionRefSupportability_Type = CfprFeatureSupportabilityType
_CfprFeatureDefinitionRefSupportability_Object = MibTableColumn
cfprFeatureDefinitionRefSupportability = _CfprFeatureDefinitionRefSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 6),
    _CfprFeatureDefinitionRefSupportability_Type()
)
cfprFeatureDefinitionRefSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefSupportability.setStatus("current")
_CfprFeatureDefinitionRefTargetDn_Type = SnmpAdminString
_CfprFeatureDefinitionRefTargetDn_Object = MibTableColumn
cfprFeatureDefinitionRefTargetDn = _CfprFeatureDefinitionRefTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 4, 1, 7),
    _CfprFeatureDefinitionRefTargetDn_Type()
)
cfprFeatureDefinitionRefTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureDefinitionRefTargetDn.setStatus("current")
_CfprFeatureFruCapProviderInstanceTable_Object = MibTable
cfprFeatureFruCapProviderInstanceTable = _CfprFeatureFruCapProviderInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5)
)
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceTable.setStatus("current")
_CfprFeatureFruCapProviderInstanceEntry_Object = MibTableRow
cfprFeatureFruCapProviderInstanceEntry = _CfprFeatureFruCapProviderInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1)
)
cfprFeatureFruCapProviderInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureFruCapProviderInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceEntry.setStatus("current")
_CfprFeatureFruCapProviderInstanceInstanceId_Type = CfprManagedObjectId
_CfprFeatureFruCapProviderInstanceInstanceId_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceInstanceId = _CfprFeatureFruCapProviderInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 1),
    _CfprFeatureFruCapProviderInstanceInstanceId_Type()
)
cfprFeatureFruCapProviderInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceInstanceId.setStatus("current")
_CfprFeatureFruCapProviderInstanceDn_Type = CfprManagedObjectDn
_CfprFeatureFruCapProviderInstanceDn_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceDn = _CfprFeatureFruCapProviderInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 2),
    _CfprFeatureFruCapProviderInstanceDn_Type()
)
cfprFeatureFruCapProviderInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceDn.setStatus("current")
_CfprFeatureFruCapProviderInstanceRn_Type = SnmpAdminString
_CfprFeatureFruCapProviderInstanceRn_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceRn = _CfprFeatureFruCapProviderInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 3),
    _CfprFeatureFruCapProviderInstanceRn_Type()
)
cfprFeatureFruCapProviderInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceRn.setStatus("current")
_CfprFeatureFruCapProviderInstanceModel_Type = SnmpAdminString
_CfprFeatureFruCapProviderInstanceModel_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceModel = _CfprFeatureFruCapProviderInstanceModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 4),
    _CfprFeatureFruCapProviderInstanceModel_Type()
)
cfprFeatureFruCapProviderInstanceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceModel.setStatus("current")
_CfprFeatureFruCapProviderInstanceRevision_Type = SnmpAdminString
_CfprFeatureFruCapProviderInstanceRevision_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceRevision = _CfprFeatureFruCapProviderInstanceRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 5),
    _CfprFeatureFruCapProviderInstanceRevision_Type()
)
cfprFeatureFruCapProviderInstanceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceRevision.setStatus("current")
_CfprFeatureFruCapProviderInstanceSupportability_Type = CfprFeatureSupportabilityType
_CfprFeatureFruCapProviderInstanceSupportability_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceSupportability = _CfprFeatureFruCapProviderInstanceSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 6),
    _CfprFeatureFruCapProviderInstanceSupportability_Type()
)
cfprFeatureFruCapProviderInstanceSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceSupportability.setStatus("current")
_CfprFeatureFruCapProviderInstanceTargetDn_Type = SnmpAdminString
_CfprFeatureFruCapProviderInstanceTargetDn_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceTargetDn = _CfprFeatureFruCapProviderInstanceTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 7),
    _CfprFeatureFruCapProviderInstanceTargetDn_Type()
)
cfprFeatureFruCapProviderInstanceTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceTargetDn.setStatus("current")
_CfprFeatureFruCapProviderInstanceVendor_Type = SnmpAdminString
_CfprFeatureFruCapProviderInstanceVendor_Object = MibTableColumn
cfprFeatureFruCapProviderInstanceVendor = _CfprFeatureFruCapProviderInstanceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 5, 1, 8),
    _CfprFeatureFruCapProviderInstanceVendor_Type()
)
cfprFeatureFruCapProviderInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderInstanceVendor.setStatus("current")
_CfprFeatureFruCapProviderRefTable_Object = MibTable
cfprFeatureFruCapProviderRefTable = _CfprFeatureFruCapProviderRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6)
)
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefTable.setStatus("current")
_CfprFeatureFruCapProviderRefEntry_Object = MibTableRow
cfprFeatureFruCapProviderRefEntry = _CfprFeatureFruCapProviderRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1)
)
cfprFeatureFruCapProviderRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureFruCapProviderRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefEntry.setStatus("current")
_CfprFeatureFruCapProviderRefInstanceId_Type = CfprManagedObjectId
_CfprFeatureFruCapProviderRefInstanceId_Object = MibTableColumn
cfprFeatureFruCapProviderRefInstanceId = _CfprFeatureFruCapProviderRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 1),
    _CfprFeatureFruCapProviderRefInstanceId_Type()
)
cfprFeatureFruCapProviderRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefInstanceId.setStatus("current")
_CfprFeatureFruCapProviderRefDn_Type = CfprManagedObjectDn
_CfprFeatureFruCapProviderRefDn_Object = MibTableColumn
cfprFeatureFruCapProviderRefDn = _CfprFeatureFruCapProviderRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 2),
    _CfprFeatureFruCapProviderRefDn_Type()
)
cfprFeatureFruCapProviderRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefDn.setStatus("current")
_CfprFeatureFruCapProviderRefRn_Type = SnmpAdminString
_CfprFeatureFruCapProviderRefRn_Object = MibTableColumn
cfprFeatureFruCapProviderRefRn = _CfprFeatureFruCapProviderRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 3),
    _CfprFeatureFruCapProviderRefRn_Type()
)
cfprFeatureFruCapProviderRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefRn.setStatus("current")
_CfprFeatureFruCapProviderRefModel_Type = SnmpAdminString
_CfprFeatureFruCapProviderRefModel_Object = MibTableColumn
cfprFeatureFruCapProviderRefModel = _CfprFeatureFruCapProviderRefModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 4),
    _CfprFeatureFruCapProviderRefModel_Type()
)
cfprFeatureFruCapProviderRefModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefModel.setStatus("current")
_CfprFeatureFruCapProviderRefRevision_Type = SnmpAdminString
_CfprFeatureFruCapProviderRefRevision_Object = MibTableColumn
cfprFeatureFruCapProviderRefRevision = _CfprFeatureFruCapProviderRefRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 5),
    _CfprFeatureFruCapProviderRefRevision_Type()
)
cfprFeatureFruCapProviderRefRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefRevision.setStatus("current")
_CfprFeatureFruCapProviderRefSupportability_Type = CfprFeatureSupportabilityType
_CfprFeatureFruCapProviderRefSupportability_Object = MibTableColumn
cfprFeatureFruCapProviderRefSupportability = _CfprFeatureFruCapProviderRefSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 6),
    _CfprFeatureFruCapProviderRefSupportability_Type()
)
cfprFeatureFruCapProviderRefSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefSupportability.setStatus("current")
_CfprFeatureFruCapProviderRefTargetDn_Type = SnmpAdminString
_CfprFeatureFruCapProviderRefTargetDn_Object = MibTableColumn
cfprFeatureFruCapProviderRefTargetDn = _CfprFeatureFruCapProviderRefTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 7),
    _CfprFeatureFruCapProviderRefTargetDn_Type()
)
cfprFeatureFruCapProviderRefTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefTargetDn.setStatus("current")
_CfprFeatureFruCapProviderRefVendor_Type = SnmpAdminString
_CfprFeatureFruCapProviderRefVendor_Object = MibTableColumn
cfprFeatureFruCapProviderRefVendor = _CfprFeatureFruCapProviderRefVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 6, 1, 8),
    _CfprFeatureFruCapProviderRefVendor_Type()
)
cfprFeatureFruCapProviderRefVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureFruCapProviderRefVendor.setStatus("current")
_CfprFeatureProviderTable_Object = MibTable
cfprFeatureProviderTable = _CfprFeatureProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 7)
)
if mibBuilder.loadTexts:
    cfprFeatureProviderTable.setStatus("current")
_CfprFeatureProviderEntry_Object = MibTableRow
cfprFeatureProviderEntry = _CfprFeatureProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 7, 1)
)
cfprFeatureProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureProviderEntry.setStatus("current")
_CfprFeatureProviderInstanceId_Type = CfprManagedObjectId
_CfprFeatureProviderInstanceId_Object = MibTableColumn
cfprFeatureProviderInstanceId = _CfprFeatureProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 7, 1, 1),
    _CfprFeatureProviderInstanceId_Type()
)
cfprFeatureProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceId.setStatus("current")
_CfprFeatureProviderDn_Type = CfprManagedObjectDn
_CfprFeatureProviderDn_Object = MibTableColumn
cfprFeatureProviderDn = _CfprFeatureProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 7, 1, 2),
    _CfprFeatureProviderDn_Type()
)
cfprFeatureProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderDn.setStatus("current")
_CfprFeatureProviderRn_Type = SnmpAdminString
_CfprFeatureProviderRn_Object = MibTableColumn
cfprFeatureProviderRn = _CfprFeatureProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 7, 1, 3),
    _CfprFeatureProviderRn_Type()
)
cfprFeatureProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderRn.setStatus("current")
_CfprFeatureProviderName_Type = SnmpAdminString
_CfprFeatureProviderName_Object = MibTableColumn
cfprFeatureProviderName = _CfprFeatureProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 7, 1, 4),
    _CfprFeatureProviderName_Type()
)
cfprFeatureProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderName.setStatus("current")
_CfprFeatureProviderInstanceTable_Object = MibTable
cfprFeatureProviderInstanceTable = _CfprFeatureProviderInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8)
)
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceTable.setStatus("current")
_CfprFeatureProviderInstanceEntry_Object = MibTableRow
cfprFeatureProviderInstanceEntry = _CfprFeatureProviderInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8, 1)
)
cfprFeatureProviderInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FEATURE-MIB", "cfprFeatureProviderInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceEntry.setStatus("current")
_CfprFeatureProviderInstanceInstanceId_Type = CfprManagedObjectId
_CfprFeatureProviderInstanceInstanceId_Object = MibTableColumn
cfprFeatureProviderInstanceInstanceId = _CfprFeatureProviderInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8, 1, 1),
    _CfprFeatureProviderInstanceInstanceId_Type()
)
cfprFeatureProviderInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceInstanceId.setStatus("current")
_CfprFeatureProviderInstanceDn_Type = CfprManagedObjectDn
_CfprFeatureProviderInstanceDn_Object = MibTableColumn
cfprFeatureProviderInstanceDn = _CfprFeatureProviderInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8, 1, 2),
    _CfprFeatureProviderInstanceDn_Type()
)
cfprFeatureProviderInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceDn.setStatus("current")
_CfprFeatureProviderInstanceRn_Type = SnmpAdminString
_CfprFeatureProviderInstanceRn_Object = MibTableColumn
cfprFeatureProviderInstanceRn = _CfprFeatureProviderInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8, 1, 3),
    _CfprFeatureProviderInstanceRn_Type()
)
cfprFeatureProviderInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceRn.setStatus("current")
_CfprFeatureProviderInstanceName_Type = SnmpAdminString
_CfprFeatureProviderInstanceName_Object = MibTableColumn
cfprFeatureProviderInstanceName = _CfprFeatureProviderInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8, 1, 4),
    _CfprFeatureProviderInstanceName_Type()
)
cfprFeatureProviderInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceName.setStatus("current")
_CfprFeatureProviderInstanceOperProviderDn_Type = SnmpAdminString
_CfprFeatureProviderInstanceOperProviderDn_Object = MibTableColumn
cfprFeatureProviderInstanceOperProviderDn = _CfprFeatureProviderInstanceOperProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 29, 8, 1, 5),
    _CfprFeatureProviderInstanceOperProviderDn_Type()
)
cfprFeatureProviderInstanceOperProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFeatureProviderInstanceOperProviderDn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-FEATURE-MIB",
    **{"cfprFeatureObjects": cfprFeatureObjects,
       "cfprFeatureContextEpTable": cfprFeatureContextEpTable,
       "cfprFeatureContextEpEntry": cfprFeatureContextEpEntry,
       "cfprFeatureContextEpInstanceId": cfprFeatureContextEpInstanceId,
       "cfprFeatureContextEpDn": cfprFeatureContextEpDn,
       "cfprFeatureContextEpRn": cfprFeatureContextEpRn,
       "cfprFeatureDefinitionTable": cfprFeatureDefinitionTable,
       "cfprFeatureDefinitionEntry": cfprFeatureDefinitionEntry,
       "cfprFeatureDefinitionInstanceId": cfprFeatureDefinitionInstanceId,
       "cfprFeatureDefinitionDn": cfprFeatureDefinitionDn,
       "cfprFeatureDefinitionRn": cfprFeatureDefinitionRn,
       "cfprFeatureDefinitionDescription": cfprFeatureDefinitionDescription,
       "cfprFeatureDefinitionName": cfprFeatureDefinitionName,
       "cfprFeatureDefinitionRevision": cfprFeatureDefinitionRevision,
       "cfprFeatureDefinitionInstanceTable": cfprFeatureDefinitionInstanceTable,
       "cfprFeatureDefinitionInstanceEntry": cfprFeatureDefinitionInstanceEntry,
       "cfprFeatureDefinitionInstanceInstanceId": cfprFeatureDefinitionInstanceInstanceId,
       "cfprFeatureDefinitionInstanceDn": cfprFeatureDefinitionInstanceDn,
       "cfprFeatureDefinitionInstanceRn": cfprFeatureDefinitionInstanceRn,
       "cfprFeatureDefinitionInstanceName": cfprFeatureDefinitionInstanceName,
       "cfprFeatureDefinitionInstanceRevision": cfprFeatureDefinitionInstanceRevision,
       "cfprFeatureDefinitionInstanceSupportability": cfprFeatureDefinitionInstanceSupportability,
       "cfprFeatureDefinitionInstanceTargetDn": cfprFeatureDefinitionInstanceTargetDn,
       "cfprFeatureDefinitionRefTable": cfprFeatureDefinitionRefTable,
       "cfprFeatureDefinitionRefEntry": cfprFeatureDefinitionRefEntry,
       "cfprFeatureDefinitionRefInstanceId": cfprFeatureDefinitionRefInstanceId,
       "cfprFeatureDefinitionRefDn": cfprFeatureDefinitionRefDn,
       "cfprFeatureDefinitionRefRn": cfprFeatureDefinitionRefRn,
       "cfprFeatureDefinitionRefName": cfprFeatureDefinitionRefName,
       "cfprFeatureDefinitionRefRevision": cfprFeatureDefinitionRefRevision,
       "cfprFeatureDefinitionRefSupportability": cfprFeatureDefinitionRefSupportability,
       "cfprFeatureDefinitionRefTargetDn": cfprFeatureDefinitionRefTargetDn,
       "cfprFeatureFruCapProviderInstanceTable": cfprFeatureFruCapProviderInstanceTable,
       "cfprFeatureFruCapProviderInstanceEntry": cfprFeatureFruCapProviderInstanceEntry,
       "cfprFeatureFruCapProviderInstanceInstanceId": cfprFeatureFruCapProviderInstanceInstanceId,
       "cfprFeatureFruCapProviderInstanceDn": cfprFeatureFruCapProviderInstanceDn,
       "cfprFeatureFruCapProviderInstanceRn": cfprFeatureFruCapProviderInstanceRn,
       "cfprFeatureFruCapProviderInstanceModel": cfprFeatureFruCapProviderInstanceModel,
       "cfprFeatureFruCapProviderInstanceRevision": cfprFeatureFruCapProviderInstanceRevision,
       "cfprFeatureFruCapProviderInstanceSupportability": cfprFeatureFruCapProviderInstanceSupportability,
       "cfprFeatureFruCapProviderInstanceTargetDn": cfprFeatureFruCapProviderInstanceTargetDn,
       "cfprFeatureFruCapProviderInstanceVendor": cfprFeatureFruCapProviderInstanceVendor,
       "cfprFeatureFruCapProviderRefTable": cfprFeatureFruCapProviderRefTable,
       "cfprFeatureFruCapProviderRefEntry": cfprFeatureFruCapProviderRefEntry,
       "cfprFeatureFruCapProviderRefInstanceId": cfprFeatureFruCapProviderRefInstanceId,
       "cfprFeatureFruCapProviderRefDn": cfprFeatureFruCapProviderRefDn,
       "cfprFeatureFruCapProviderRefRn": cfprFeatureFruCapProviderRefRn,
       "cfprFeatureFruCapProviderRefModel": cfprFeatureFruCapProviderRefModel,
       "cfprFeatureFruCapProviderRefRevision": cfprFeatureFruCapProviderRefRevision,
       "cfprFeatureFruCapProviderRefSupportability": cfprFeatureFruCapProviderRefSupportability,
       "cfprFeatureFruCapProviderRefTargetDn": cfprFeatureFruCapProviderRefTargetDn,
       "cfprFeatureFruCapProviderRefVendor": cfprFeatureFruCapProviderRefVendor,
       "cfprFeatureProviderTable": cfprFeatureProviderTable,
       "cfprFeatureProviderEntry": cfprFeatureProviderEntry,
       "cfprFeatureProviderInstanceId": cfprFeatureProviderInstanceId,
       "cfprFeatureProviderDn": cfprFeatureProviderDn,
       "cfprFeatureProviderRn": cfprFeatureProviderRn,
       "cfprFeatureProviderName": cfprFeatureProviderName,
       "cfprFeatureProviderInstanceTable": cfprFeatureProviderInstanceTable,
       "cfprFeatureProviderInstanceEntry": cfprFeatureProviderInstanceEntry,
       "cfprFeatureProviderInstanceInstanceId": cfprFeatureProviderInstanceInstanceId,
       "cfprFeatureProviderInstanceDn": cfprFeatureProviderInstanceDn,
       "cfprFeatureProviderInstanceRn": cfprFeatureProviderInstanceRn,
       "cfprFeatureProviderInstanceName": cfprFeatureProviderInstanceName,
       "cfprFeatureProviderInstanceOperProviderDn": cfprFeatureProviderInstanceOperProviderDn}
)
