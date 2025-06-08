# SNMP MIB module (CISCO-FIREPOWER-AP-FEATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-FEATURE-MIB.mib
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

(CfprApFeatureSupportabilityType,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApFeatureSupportabilityType")

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

cfprApFeatureObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApFeatureContextEpTable_Object = MibTable
cfprApFeatureContextEpTable = _CfprApFeatureContextEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 1)
)
if mibBuilder.loadTexts:
    cfprApFeatureContextEpTable.setStatus("current")
_CfprApFeatureContextEpEntry_Object = MibTableRow
cfprApFeatureContextEpEntry = _CfprApFeatureContextEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 1, 1)
)
cfprApFeatureContextEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureContextEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureContextEpEntry.setStatus("current")
_CfprApFeatureContextEpInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureContextEpInstanceId_Object = MibTableColumn
cfprApFeatureContextEpInstanceId = _CfprApFeatureContextEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 1, 1, 1),
    _CfprApFeatureContextEpInstanceId_Type()
)
cfprApFeatureContextEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureContextEpInstanceId.setStatus("current")
_CfprApFeatureContextEpDn_Type = CfprApManagedObjectDn
_CfprApFeatureContextEpDn_Object = MibTableColumn
cfprApFeatureContextEpDn = _CfprApFeatureContextEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 1, 1, 2),
    _CfprApFeatureContextEpDn_Type()
)
cfprApFeatureContextEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureContextEpDn.setStatus("current")
_CfprApFeatureContextEpRn_Type = SnmpAdminString
_CfprApFeatureContextEpRn_Object = MibTableColumn
cfprApFeatureContextEpRn = _CfprApFeatureContextEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 1, 1, 3),
    _CfprApFeatureContextEpRn_Type()
)
cfprApFeatureContextEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureContextEpRn.setStatus("current")
_CfprApFeatureDefinitionTable_Object = MibTable
cfprApFeatureDefinitionTable = _CfprApFeatureDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2)
)
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionTable.setStatus("current")
_CfprApFeatureDefinitionEntry_Object = MibTableRow
cfprApFeatureDefinitionEntry = _CfprApFeatureDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1)
)
cfprApFeatureDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionEntry.setStatus("current")
_CfprApFeatureDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureDefinitionInstanceId_Object = MibTableColumn
cfprApFeatureDefinitionInstanceId = _CfprApFeatureDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1, 1),
    _CfprApFeatureDefinitionInstanceId_Type()
)
cfprApFeatureDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceId.setStatus("current")
_CfprApFeatureDefinitionDn_Type = CfprApManagedObjectDn
_CfprApFeatureDefinitionDn_Object = MibTableColumn
cfprApFeatureDefinitionDn = _CfprApFeatureDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1, 2),
    _CfprApFeatureDefinitionDn_Type()
)
cfprApFeatureDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionDn.setStatus("current")
_CfprApFeatureDefinitionRn_Type = SnmpAdminString
_CfprApFeatureDefinitionRn_Object = MibTableColumn
cfprApFeatureDefinitionRn = _CfprApFeatureDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1, 3),
    _CfprApFeatureDefinitionRn_Type()
)
cfprApFeatureDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRn.setStatus("current")
_CfprApFeatureDefinitionDescription_Type = SnmpAdminString
_CfprApFeatureDefinitionDescription_Object = MibTableColumn
cfprApFeatureDefinitionDescription = _CfprApFeatureDefinitionDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1, 4),
    _CfprApFeatureDefinitionDescription_Type()
)
cfprApFeatureDefinitionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionDescription.setStatus("current")
_CfprApFeatureDefinitionName_Type = SnmpAdminString
_CfprApFeatureDefinitionName_Object = MibTableColumn
cfprApFeatureDefinitionName = _CfprApFeatureDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1, 5),
    _CfprApFeatureDefinitionName_Type()
)
cfprApFeatureDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionName.setStatus("current")
_CfprApFeatureDefinitionRevision_Type = SnmpAdminString
_CfprApFeatureDefinitionRevision_Object = MibTableColumn
cfprApFeatureDefinitionRevision = _CfprApFeatureDefinitionRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 2, 1, 6),
    _CfprApFeatureDefinitionRevision_Type()
)
cfprApFeatureDefinitionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRevision.setStatus("current")
_CfprApFeatureDefinitionInstanceTable_Object = MibTable
cfprApFeatureDefinitionInstanceTable = _CfprApFeatureDefinitionInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3)
)
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceTable.setStatus("current")
_CfprApFeatureDefinitionInstanceEntry_Object = MibTableRow
cfprApFeatureDefinitionInstanceEntry = _CfprApFeatureDefinitionInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1)
)
cfprApFeatureDefinitionInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureDefinitionInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceEntry.setStatus("current")
_CfprApFeatureDefinitionInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureDefinitionInstanceInstanceId_Object = MibTableColumn
cfprApFeatureDefinitionInstanceInstanceId = _CfprApFeatureDefinitionInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 1),
    _CfprApFeatureDefinitionInstanceInstanceId_Type()
)
cfprApFeatureDefinitionInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceInstanceId.setStatus("current")
_CfprApFeatureDefinitionInstanceDn_Type = CfprApManagedObjectDn
_CfprApFeatureDefinitionInstanceDn_Object = MibTableColumn
cfprApFeatureDefinitionInstanceDn = _CfprApFeatureDefinitionInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 2),
    _CfprApFeatureDefinitionInstanceDn_Type()
)
cfprApFeatureDefinitionInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceDn.setStatus("current")
_CfprApFeatureDefinitionInstanceRn_Type = SnmpAdminString
_CfprApFeatureDefinitionInstanceRn_Object = MibTableColumn
cfprApFeatureDefinitionInstanceRn = _CfprApFeatureDefinitionInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 3),
    _CfprApFeatureDefinitionInstanceRn_Type()
)
cfprApFeatureDefinitionInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceRn.setStatus("current")
_CfprApFeatureDefinitionInstanceName_Type = SnmpAdminString
_CfprApFeatureDefinitionInstanceName_Object = MibTableColumn
cfprApFeatureDefinitionInstanceName = _CfprApFeatureDefinitionInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 4),
    _CfprApFeatureDefinitionInstanceName_Type()
)
cfprApFeatureDefinitionInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceName.setStatus("current")
_CfprApFeatureDefinitionInstanceRevision_Type = SnmpAdminString
_CfprApFeatureDefinitionInstanceRevision_Object = MibTableColumn
cfprApFeatureDefinitionInstanceRevision = _CfprApFeatureDefinitionInstanceRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 5),
    _CfprApFeatureDefinitionInstanceRevision_Type()
)
cfprApFeatureDefinitionInstanceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceRevision.setStatus("current")
_CfprApFeatureDefinitionInstanceSupportability_Type = CfprApFeatureSupportabilityType
_CfprApFeatureDefinitionInstanceSupportability_Object = MibTableColumn
cfprApFeatureDefinitionInstanceSupportability = _CfprApFeatureDefinitionInstanceSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 6),
    _CfprApFeatureDefinitionInstanceSupportability_Type()
)
cfprApFeatureDefinitionInstanceSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceSupportability.setStatus("current")
_CfprApFeatureDefinitionInstanceTargetDn_Type = SnmpAdminString
_CfprApFeatureDefinitionInstanceTargetDn_Object = MibTableColumn
cfprApFeatureDefinitionInstanceTargetDn = _CfprApFeatureDefinitionInstanceTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 3, 1, 7),
    _CfprApFeatureDefinitionInstanceTargetDn_Type()
)
cfprApFeatureDefinitionInstanceTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionInstanceTargetDn.setStatus("current")
_CfprApFeatureDefinitionRefTable_Object = MibTable
cfprApFeatureDefinitionRefTable = _CfprApFeatureDefinitionRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4)
)
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefTable.setStatus("current")
_CfprApFeatureDefinitionRefEntry_Object = MibTableRow
cfprApFeatureDefinitionRefEntry = _CfprApFeatureDefinitionRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1)
)
cfprApFeatureDefinitionRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureDefinitionRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefEntry.setStatus("current")
_CfprApFeatureDefinitionRefInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureDefinitionRefInstanceId_Object = MibTableColumn
cfprApFeatureDefinitionRefInstanceId = _CfprApFeatureDefinitionRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 1),
    _CfprApFeatureDefinitionRefInstanceId_Type()
)
cfprApFeatureDefinitionRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefInstanceId.setStatus("current")
_CfprApFeatureDefinitionRefDn_Type = CfprApManagedObjectDn
_CfprApFeatureDefinitionRefDn_Object = MibTableColumn
cfprApFeatureDefinitionRefDn = _CfprApFeatureDefinitionRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 2),
    _CfprApFeatureDefinitionRefDn_Type()
)
cfprApFeatureDefinitionRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefDn.setStatus("current")
_CfprApFeatureDefinitionRefRn_Type = SnmpAdminString
_CfprApFeatureDefinitionRefRn_Object = MibTableColumn
cfprApFeatureDefinitionRefRn = _CfprApFeatureDefinitionRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 3),
    _CfprApFeatureDefinitionRefRn_Type()
)
cfprApFeatureDefinitionRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefRn.setStatus("current")
_CfprApFeatureDefinitionRefName_Type = SnmpAdminString
_CfprApFeatureDefinitionRefName_Object = MibTableColumn
cfprApFeatureDefinitionRefName = _CfprApFeatureDefinitionRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 4),
    _CfprApFeatureDefinitionRefName_Type()
)
cfprApFeatureDefinitionRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefName.setStatus("current")
_CfprApFeatureDefinitionRefRevision_Type = SnmpAdminString
_CfprApFeatureDefinitionRefRevision_Object = MibTableColumn
cfprApFeatureDefinitionRefRevision = _CfprApFeatureDefinitionRefRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 5),
    _CfprApFeatureDefinitionRefRevision_Type()
)
cfprApFeatureDefinitionRefRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefRevision.setStatus("current")
_CfprApFeatureDefinitionRefSupportability_Type = CfprApFeatureSupportabilityType
_CfprApFeatureDefinitionRefSupportability_Object = MibTableColumn
cfprApFeatureDefinitionRefSupportability = _CfprApFeatureDefinitionRefSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 6),
    _CfprApFeatureDefinitionRefSupportability_Type()
)
cfprApFeatureDefinitionRefSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefSupportability.setStatus("current")
_CfprApFeatureDefinitionRefTargetDn_Type = SnmpAdminString
_CfprApFeatureDefinitionRefTargetDn_Object = MibTableColumn
cfprApFeatureDefinitionRefTargetDn = _CfprApFeatureDefinitionRefTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 4, 1, 7),
    _CfprApFeatureDefinitionRefTargetDn_Type()
)
cfprApFeatureDefinitionRefTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureDefinitionRefTargetDn.setStatus("current")
_CfprApFeatureFruCapProviderInstanceTable_Object = MibTable
cfprApFeatureFruCapProviderInstanceTable = _CfprApFeatureFruCapProviderInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5)
)
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceTable.setStatus("current")
_CfprApFeatureFruCapProviderInstanceEntry_Object = MibTableRow
cfprApFeatureFruCapProviderInstanceEntry = _CfprApFeatureFruCapProviderInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1)
)
cfprApFeatureFruCapProviderInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureFruCapProviderInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceEntry.setStatus("current")
_CfprApFeatureFruCapProviderInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureFruCapProviderInstanceInstanceId_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceInstanceId = _CfprApFeatureFruCapProviderInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 1),
    _CfprApFeatureFruCapProviderInstanceInstanceId_Type()
)
cfprApFeatureFruCapProviderInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceInstanceId.setStatus("current")
_CfprApFeatureFruCapProviderInstanceDn_Type = CfprApManagedObjectDn
_CfprApFeatureFruCapProviderInstanceDn_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceDn = _CfprApFeatureFruCapProviderInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 2),
    _CfprApFeatureFruCapProviderInstanceDn_Type()
)
cfprApFeatureFruCapProviderInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceDn.setStatus("current")
_CfprApFeatureFruCapProviderInstanceRn_Type = SnmpAdminString
_CfprApFeatureFruCapProviderInstanceRn_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceRn = _CfprApFeatureFruCapProviderInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 3),
    _CfprApFeatureFruCapProviderInstanceRn_Type()
)
cfprApFeatureFruCapProviderInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceRn.setStatus("current")
_CfprApFeatureFruCapProviderInstanceModel_Type = SnmpAdminString
_CfprApFeatureFruCapProviderInstanceModel_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceModel = _CfprApFeatureFruCapProviderInstanceModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 4),
    _CfprApFeatureFruCapProviderInstanceModel_Type()
)
cfprApFeatureFruCapProviderInstanceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceModel.setStatus("current")
_CfprApFeatureFruCapProviderInstanceRevision_Type = SnmpAdminString
_CfprApFeatureFruCapProviderInstanceRevision_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceRevision = _CfprApFeatureFruCapProviderInstanceRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 5),
    _CfprApFeatureFruCapProviderInstanceRevision_Type()
)
cfprApFeatureFruCapProviderInstanceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceRevision.setStatus("current")
_CfprApFeatureFruCapProviderInstanceSupportability_Type = CfprApFeatureSupportabilityType
_CfprApFeatureFruCapProviderInstanceSupportability_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceSupportability = _CfprApFeatureFruCapProviderInstanceSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 6),
    _CfprApFeatureFruCapProviderInstanceSupportability_Type()
)
cfprApFeatureFruCapProviderInstanceSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceSupportability.setStatus("current")
_CfprApFeatureFruCapProviderInstanceTargetDn_Type = SnmpAdminString
_CfprApFeatureFruCapProviderInstanceTargetDn_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceTargetDn = _CfprApFeatureFruCapProviderInstanceTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 7),
    _CfprApFeatureFruCapProviderInstanceTargetDn_Type()
)
cfprApFeatureFruCapProviderInstanceTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceTargetDn.setStatus("current")
_CfprApFeatureFruCapProviderInstanceVendor_Type = SnmpAdminString
_CfprApFeatureFruCapProviderInstanceVendor_Object = MibTableColumn
cfprApFeatureFruCapProviderInstanceVendor = _CfprApFeatureFruCapProviderInstanceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 5, 1, 8),
    _CfprApFeatureFruCapProviderInstanceVendor_Type()
)
cfprApFeatureFruCapProviderInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderInstanceVendor.setStatus("current")
_CfprApFeatureFruCapProviderRefTable_Object = MibTable
cfprApFeatureFruCapProviderRefTable = _CfprApFeatureFruCapProviderRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6)
)
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefTable.setStatus("current")
_CfprApFeatureFruCapProviderRefEntry_Object = MibTableRow
cfprApFeatureFruCapProviderRefEntry = _CfprApFeatureFruCapProviderRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1)
)
cfprApFeatureFruCapProviderRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureFruCapProviderRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefEntry.setStatus("current")
_CfprApFeatureFruCapProviderRefInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureFruCapProviderRefInstanceId_Object = MibTableColumn
cfprApFeatureFruCapProviderRefInstanceId = _CfprApFeatureFruCapProviderRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 1),
    _CfprApFeatureFruCapProviderRefInstanceId_Type()
)
cfprApFeatureFruCapProviderRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefInstanceId.setStatus("current")
_CfprApFeatureFruCapProviderRefDn_Type = CfprApManagedObjectDn
_CfprApFeatureFruCapProviderRefDn_Object = MibTableColumn
cfprApFeatureFruCapProviderRefDn = _CfprApFeatureFruCapProviderRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 2),
    _CfprApFeatureFruCapProviderRefDn_Type()
)
cfprApFeatureFruCapProviderRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefDn.setStatus("current")
_CfprApFeatureFruCapProviderRefRn_Type = SnmpAdminString
_CfprApFeatureFruCapProviderRefRn_Object = MibTableColumn
cfprApFeatureFruCapProviderRefRn = _CfprApFeatureFruCapProviderRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 3),
    _CfprApFeatureFruCapProviderRefRn_Type()
)
cfprApFeatureFruCapProviderRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefRn.setStatus("current")
_CfprApFeatureFruCapProviderRefModel_Type = SnmpAdminString
_CfprApFeatureFruCapProviderRefModel_Object = MibTableColumn
cfprApFeatureFruCapProviderRefModel = _CfprApFeatureFruCapProviderRefModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 4),
    _CfprApFeatureFruCapProviderRefModel_Type()
)
cfprApFeatureFruCapProviderRefModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefModel.setStatus("current")
_CfprApFeatureFruCapProviderRefRevision_Type = SnmpAdminString
_CfprApFeatureFruCapProviderRefRevision_Object = MibTableColumn
cfprApFeatureFruCapProviderRefRevision = _CfprApFeatureFruCapProviderRefRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 5),
    _CfprApFeatureFruCapProviderRefRevision_Type()
)
cfprApFeatureFruCapProviderRefRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefRevision.setStatus("current")
_CfprApFeatureFruCapProviderRefSupportability_Type = CfprApFeatureSupportabilityType
_CfprApFeatureFruCapProviderRefSupportability_Object = MibTableColumn
cfprApFeatureFruCapProviderRefSupportability = _CfprApFeatureFruCapProviderRefSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 6),
    _CfprApFeatureFruCapProviderRefSupportability_Type()
)
cfprApFeatureFruCapProviderRefSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefSupportability.setStatus("current")
_CfprApFeatureFruCapProviderRefTargetDn_Type = SnmpAdminString
_CfprApFeatureFruCapProviderRefTargetDn_Object = MibTableColumn
cfprApFeatureFruCapProviderRefTargetDn = _CfprApFeatureFruCapProviderRefTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 7),
    _CfprApFeatureFruCapProviderRefTargetDn_Type()
)
cfprApFeatureFruCapProviderRefTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefTargetDn.setStatus("current")
_CfprApFeatureFruCapProviderRefVendor_Type = SnmpAdminString
_CfprApFeatureFruCapProviderRefVendor_Object = MibTableColumn
cfprApFeatureFruCapProviderRefVendor = _CfprApFeatureFruCapProviderRefVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 6, 1, 8),
    _CfprApFeatureFruCapProviderRefVendor_Type()
)
cfprApFeatureFruCapProviderRefVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureFruCapProviderRefVendor.setStatus("current")
_CfprApFeatureProviderTable_Object = MibTable
cfprApFeatureProviderTable = _CfprApFeatureProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 7)
)
if mibBuilder.loadTexts:
    cfprApFeatureProviderTable.setStatus("current")
_CfprApFeatureProviderEntry_Object = MibTableRow
cfprApFeatureProviderEntry = _CfprApFeatureProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 7, 1)
)
cfprApFeatureProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureProviderEntry.setStatus("current")
_CfprApFeatureProviderInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureProviderInstanceId_Object = MibTableColumn
cfprApFeatureProviderInstanceId = _CfprApFeatureProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 7, 1, 1),
    _CfprApFeatureProviderInstanceId_Type()
)
cfprApFeatureProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceId.setStatus("current")
_CfprApFeatureProviderDn_Type = CfprApManagedObjectDn
_CfprApFeatureProviderDn_Object = MibTableColumn
cfprApFeatureProviderDn = _CfprApFeatureProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 7, 1, 2),
    _CfprApFeatureProviderDn_Type()
)
cfprApFeatureProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderDn.setStatus("current")
_CfprApFeatureProviderRn_Type = SnmpAdminString
_CfprApFeatureProviderRn_Object = MibTableColumn
cfprApFeatureProviderRn = _CfprApFeatureProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 7, 1, 3),
    _CfprApFeatureProviderRn_Type()
)
cfprApFeatureProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderRn.setStatus("current")
_CfprApFeatureProviderName_Type = SnmpAdminString
_CfprApFeatureProviderName_Object = MibTableColumn
cfprApFeatureProviderName = _CfprApFeatureProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 7, 1, 4),
    _CfprApFeatureProviderName_Type()
)
cfprApFeatureProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderName.setStatus("current")
_CfprApFeatureProviderInstanceTable_Object = MibTable
cfprApFeatureProviderInstanceTable = _CfprApFeatureProviderInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8)
)
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceTable.setStatus("current")
_CfprApFeatureProviderInstanceEntry_Object = MibTableRow
cfprApFeatureProviderInstanceEntry = _CfprApFeatureProviderInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8, 1)
)
cfprApFeatureProviderInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FEATURE-MIB", "cfprApFeatureProviderInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceEntry.setStatus("current")
_CfprApFeatureProviderInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApFeatureProviderInstanceInstanceId_Object = MibTableColumn
cfprApFeatureProviderInstanceInstanceId = _CfprApFeatureProviderInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8, 1, 1),
    _CfprApFeatureProviderInstanceInstanceId_Type()
)
cfprApFeatureProviderInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceInstanceId.setStatus("current")
_CfprApFeatureProviderInstanceDn_Type = CfprApManagedObjectDn
_CfprApFeatureProviderInstanceDn_Object = MibTableColumn
cfprApFeatureProviderInstanceDn = _CfprApFeatureProviderInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8, 1, 2),
    _CfprApFeatureProviderInstanceDn_Type()
)
cfprApFeatureProviderInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceDn.setStatus("current")
_CfprApFeatureProviderInstanceRn_Type = SnmpAdminString
_CfprApFeatureProviderInstanceRn_Object = MibTableColumn
cfprApFeatureProviderInstanceRn = _CfprApFeatureProviderInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8, 1, 3),
    _CfprApFeatureProviderInstanceRn_Type()
)
cfprApFeatureProviderInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceRn.setStatus("current")
_CfprApFeatureProviderInstanceName_Type = SnmpAdminString
_CfprApFeatureProviderInstanceName_Object = MibTableColumn
cfprApFeatureProviderInstanceName = _CfprApFeatureProviderInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8, 1, 4),
    _CfprApFeatureProviderInstanceName_Type()
)
cfprApFeatureProviderInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceName.setStatus("current")
_CfprApFeatureProviderInstanceOperProviderDn_Type = SnmpAdminString
_CfprApFeatureProviderInstanceOperProviderDn_Object = MibTableColumn
cfprApFeatureProviderInstanceOperProviderDn = _CfprApFeatureProviderInstanceOperProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 29, 8, 1, 5),
    _CfprApFeatureProviderInstanceOperProviderDn_Type()
)
cfprApFeatureProviderInstanceOperProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFeatureProviderInstanceOperProviderDn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-FEATURE-MIB",
    **{"cfprApFeatureObjects": cfprApFeatureObjects,
       "cfprApFeatureContextEpTable": cfprApFeatureContextEpTable,
       "cfprApFeatureContextEpEntry": cfprApFeatureContextEpEntry,
       "cfprApFeatureContextEpInstanceId": cfprApFeatureContextEpInstanceId,
       "cfprApFeatureContextEpDn": cfprApFeatureContextEpDn,
       "cfprApFeatureContextEpRn": cfprApFeatureContextEpRn,
       "cfprApFeatureDefinitionTable": cfprApFeatureDefinitionTable,
       "cfprApFeatureDefinitionEntry": cfprApFeatureDefinitionEntry,
       "cfprApFeatureDefinitionInstanceId": cfprApFeatureDefinitionInstanceId,
       "cfprApFeatureDefinitionDn": cfprApFeatureDefinitionDn,
       "cfprApFeatureDefinitionRn": cfprApFeatureDefinitionRn,
       "cfprApFeatureDefinitionDescription": cfprApFeatureDefinitionDescription,
       "cfprApFeatureDefinitionName": cfprApFeatureDefinitionName,
       "cfprApFeatureDefinitionRevision": cfprApFeatureDefinitionRevision,
       "cfprApFeatureDefinitionInstanceTable": cfprApFeatureDefinitionInstanceTable,
       "cfprApFeatureDefinitionInstanceEntry": cfprApFeatureDefinitionInstanceEntry,
       "cfprApFeatureDefinitionInstanceInstanceId": cfprApFeatureDefinitionInstanceInstanceId,
       "cfprApFeatureDefinitionInstanceDn": cfprApFeatureDefinitionInstanceDn,
       "cfprApFeatureDefinitionInstanceRn": cfprApFeatureDefinitionInstanceRn,
       "cfprApFeatureDefinitionInstanceName": cfprApFeatureDefinitionInstanceName,
       "cfprApFeatureDefinitionInstanceRevision": cfprApFeatureDefinitionInstanceRevision,
       "cfprApFeatureDefinitionInstanceSupportability": cfprApFeatureDefinitionInstanceSupportability,
       "cfprApFeatureDefinitionInstanceTargetDn": cfprApFeatureDefinitionInstanceTargetDn,
       "cfprApFeatureDefinitionRefTable": cfprApFeatureDefinitionRefTable,
       "cfprApFeatureDefinitionRefEntry": cfprApFeatureDefinitionRefEntry,
       "cfprApFeatureDefinitionRefInstanceId": cfprApFeatureDefinitionRefInstanceId,
       "cfprApFeatureDefinitionRefDn": cfprApFeatureDefinitionRefDn,
       "cfprApFeatureDefinitionRefRn": cfprApFeatureDefinitionRefRn,
       "cfprApFeatureDefinitionRefName": cfprApFeatureDefinitionRefName,
       "cfprApFeatureDefinitionRefRevision": cfprApFeatureDefinitionRefRevision,
       "cfprApFeatureDefinitionRefSupportability": cfprApFeatureDefinitionRefSupportability,
       "cfprApFeatureDefinitionRefTargetDn": cfprApFeatureDefinitionRefTargetDn,
       "cfprApFeatureFruCapProviderInstanceTable": cfprApFeatureFruCapProviderInstanceTable,
       "cfprApFeatureFruCapProviderInstanceEntry": cfprApFeatureFruCapProviderInstanceEntry,
       "cfprApFeatureFruCapProviderInstanceInstanceId": cfprApFeatureFruCapProviderInstanceInstanceId,
       "cfprApFeatureFruCapProviderInstanceDn": cfprApFeatureFruCapProviderInstanceDn,
       "cfprApFeatureFruCapProviderInstanceRn": cfprApFeatureFruCapProviderInstanceRn,
       "cfprApFeatureFruCapProviderInstanceModel": cfprApFeatureFruCapProviderInstanceModel,
       "cfprApFeatureFruCapProviderInstanceRevision": cfprApFeatureFruCapProviderInstanceRevision,
       "cfprApFeatureFruCapProviderInstanceSupportability": cfprApFeatureFruCapProviderInstanceSupportability,
       "cfprApFeatureFruCapProviderInstanceTargetDn": cfprApFeatureFruCapProviderInstanceTargetDn,
       "cfprApFeatureFruCapProviderInstanceVendor": cfprApFeatureFruCapProviderInstanceVendor,
       "cfprApFeatureFruCapProviderRefTable": cfprApFeatureFruCapProviderRefTable,
       "cfprApFeatureFruCapProviderRefEntry": cfprApFeatureFruCapProviderRefEntry,
       "cfprApFeatureFruCapProviderRefInstanceId": cfprApFeatureFruCapProviderRefInstanceId,
       "cfprApFeatureFruCapProviderRefDn": cfprApFeatureFruCapProviderRefDn,
       "cfprApFeatureFruCapProviderRefRn": cfprApFeatureFruCapProviderRefRn,
       "cfprApFeatureFruCapProviderRefModel": cfprApFeatureFruCapProviderRefModel,
       "cfprApFeatureFruCapProviderRefRevision": cfprApFeatureFruCapProviderRefRevision,
       "cfprApFeatureFruCapProviderRefSupportability": cfprApFeatureFruCapProviderRefSupportability,
       "cfprApFeatureFruCapProviderRefTargetDn": cfprApFeatureFruCapProviderRefTargetDn,
       "cfprApFeatureFruCapProviderRefVendor": cfprApFeatureFruCapProviderRefVendor,
       "cfprApFeatureProviderTable": cfprApFeatureProviderTable,
       "cfprApFeatureProviderEntry": cfprApFeatureProviderEntry,
       "cfprApFeatureProviderInstanceId": cfprApFeatureProviderInstanceId,
       "cfprApFeatureProviderDn": cfprApFeatureProviderDn,
       "cfprApFeatureProviderRn": cfprApFeatureProviderRn,
       "cfprApFeatureProviderName": cfprApFeatureProviderName,
       "cfprApFeatureProviderInstanceTable": cfprApFeatureProviderInstanceTable,
       "cfprApFeatureProviderInstanceEntry": cfprApFeatureProviderInstanceEntry,
       "cfprApFeatureProviderInstanceInstanceId": cfprApFeatureProviderInstanceInstanceId,
       "cfprApFeatureProviderInstanceDn": cfprApFeatureProviderInstanceDn,
       "cfprApFeatureProviderInstanceRn": cfprApFeatureProviderInstanceRn,
       "cfprApFeatureProviderInstanceName": cfprApFeatureProviderInstanceName,
       "cfprApFeatureProviderInstanceOperProviderDn": cfprApFeatureProviderInstanceOperProviderDn}
)
