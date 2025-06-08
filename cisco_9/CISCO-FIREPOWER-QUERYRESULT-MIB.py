# SNMP MIB module (CISCO-FIREPOWER-QUERYRESULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-QUERYRESULT-MIB.mib
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

cfprQueryresultObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprQueryresultDependencyTable_Object = MibTable
cfprQueryresultDependencyTable = _CfprQueryresultDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1)
)
if mibBuilder.loadTexts:
    cfprQueryresultDependencyTable.setStatus("current")
_CfprQueryresultDependencyEntry_Object = MibTableRow
cfprQueryresultDependencyEntry = _CfprQueryresultDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1)
)
cfprQueryresultDependencyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QUERYRESULT-MIB", "cfprQueryresultDependencyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQueryresultDependencyEntry.setStatus("current")
_CfprQueryresultDependencyInstanceId_Type = CfprManagedObjectId
_CfprQueryresultDependencyInstanceId_Object = MibTableColumn
cfprQueryresultDependencyInstanceId = _CfprQueryresultDependencyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 1),
    _CfprQueryresultDependencyInstanceId_Type()
)
cfprQueryresultDependencyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyInstanceId.setStatus("current")
_CfprQueryresultDependencyDn_Type = CfprManagedObjectDn
_CfprQueryresultDependencyDn_Object = MibTableColumn
cfprQueryresultDependencyDn = _CfprQueryresultDependencyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 2),
    _CfprQueryresultDependencyDn_Type()
)
cfprQueryresultDependencyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyDn.setStatus("current")
_CfprQueryresultDependencyRn_Type = SnmpAdminString
_CfprQueryresultDependencyRn_Object = MibTableColumn
cfprQueryresultDependencyRn = _CfprQueryresultDependencyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 3),
    _CfprQueryresultDependencyRn_Type()
)
cfprQueryresultDependencyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyRn.setStatus("current")
_CfprQueryresultDependencyClassType_Type = SnmpAdminString
_CfprQueryresultDependencyClassType_Object = MibTableColumn
cfprQueryresultDependencyClassType = _CfprQueryresultDependencyClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 4),
    _CfprQueryresultDependencyClassType_Type()
)
cfprQueryresultDependencyClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyClassType.setStatus("current")
_CfprQueryresultDependencyIsImportable_Type = TruthValue
_CfprQueryresultDependencyIsImportable_Object = MibTableColumn
cfprQueryresultDependencyIsImportable = _CfprQueryresultDependencyIsImportable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 5),
    _CfprQueryresultDependencyIsImportable_Type()
)
cfprQueryresultDependencyIsImportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyIsImportable.setStatus("current")
_CfprQueryresultDependencyPolicyOwner_Type = SnmpAdminString
_CfprQueryresultDependencyPolicyOwner_Object = MibTableColumn
cfprQueryresultDependencyPolicyOwner = _CfprQueryresultDependencyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 6),
    _CfprQueryresultDependencyPolicyOwner_Type()
)
cfprQueryresultDependencyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyPolicyOwner.setStatus("current")
_CfprQueryresultDependencyRefConvertedDn_Type = SnmpAdminString
_CfprQueryresultDependencyRefConvertedDn_Object = MibTableColumn
cfprQueryresultDependencyRefConvertedDn = _CfprQueryresultDependencyRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 7),
    _CfprQueryresultDependencyRefConvertedDn_Type()
)
cfprQueryresultDependencyRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyRefConvertedDn.setStatus("current")
_CfprQueryresultDependencyRefDn_Type = SnmpAdminString
_CfprQueryresultDependencyRefDn_Object = MibTableColumn
cfprQueryresultDependencyRefDn = _CfprQueryresultDependencyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 8),
    _CfprQueryresultDependencyRefDn_Type()
)
cfprQueryresultDependencyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyRefDn.setStatus("current")
_CfprQueryresultDependencyRefName_Type = SnmpAdminString
_CfprQueryresultDependencyRefName_Object = MibTableColumn
cfprQueryresultDependencyRefName = _CfprQueryresultDependencyRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 1, 1, 9),
    _CfprQueryresultDependencyRefName_Type()
)
cfprQueryresultDependencyRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultDependencyRefName.setStatus("current")
_CfprQueryresultUsageTable_Object = MibTable
cfprQueryresultUsageTable = _CfprQueryresultUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2)
)
if mibBuilder.loadTexts:
    cfprQueryresultUsageTable.setStatus("current")
_CfprQueryresultUsageEntry_Object = MibTableRow
cfprQueryresultUsageEntry = _CfprQueryresultUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1)
)
cfprQueryresultUsageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QUERYRESULT-MIB", "cfprQueryresultUsageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQueryresultUsageEntry.setStatus("current")
_CfprQueryresultUsageInstanceId_Type = CfprManagedObjectId
_CfprQueryresultUsageInstanceId_Object = MibTableColumn
cfprQueryresultUsageInstanceId = _CfprQueryresultUsageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 1),
    _CfprQueryresultUsageInstanceId_Type()
)
cfprQueryresultUsageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQueryresultUsageInstanceId.setStatus("current")
_CfprQueryresultUsageDn_Type = CfprManagedObjectDn
_CfprQueryresultUsageDn_Object = MibTableColumn
cfprQueryresultUsageDn = _CfprQueryresultUsageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 2),
    _CfprQueryresultUsageDn_Type()
)
cfprQueryresultUsageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageDn.setStatus("current")
_CfprQueryresultUsageRn_Type = SnmpAdminString
_CfprQueryresultUsageRn_Object = MibTableColumn
cfprQueryresultUsageRn = _CfprQueryresultUsageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 3),
    _CfprQueryresultUsageRn_Type()
)
cfprQueryresultUsageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageRn.setStatus("current")
_CfprQueryresultUsageClassType_Type = SnmpAdminString
_CfprQueryresultUsageClassType_Object = MibTableColumn
cfprQueryresultUsageClassType = _CfprQueryresultUsageClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 4),
    _CfprQueryresultUsageClassType_Type()
)
cfprQueryresultUsageClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageClassType.setStatus("current")
_CfprQueryresultUsageIsServiceTemplate_Type = TruthValue
_CfprQueryresultUsageIsServiceTemplate_Object = MibTableColumn
cfprQueryresultUsageIsServiceTemplate = _CfprQueryresultUsageIsServiceTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 5),
    _CfprQueryresultUsageIsServiceTemplate_Type()
)
cfprQueryresultUsageIsServiceTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageIsServiceTemplate.setStatus("current")
_CfprQueryresultUsagePolicyOwner_Type = SnmpAdminString
_CfprQueryresultUsagePolicyOwner_Object = MibTableColumn
cfprQueryresultUsagePolicyOwner = _CfprQueryresultUsagePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 6),
    _CfprQueryresultUsagePolicyOwner_Type()
)
cfprQueryresultUsagePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsagePolicyOwner.setStatus("current")
_CfprQueryresultUsageRefConvertedDn_Type = SnmpAdminString
_CfprQueryresultUsageRefConvertedDn_Object = MibTableColumn
cfprQueryresultUsageRefConvertedDn = _CfprQueryresultUsageRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 7),
    _CfprQueryresultUsageRefConvertedDn_Type()
)
cfprQueryresultUsageRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageRefConvertedDn.setStatus("current")
_CfprQueryresultUsageRefDn_Type = SnmpAdminString
_CfprQueryresultUsageRefDn_Object = MibTableColumn
cfprQueryresultUsageRefDn = _CfprQueryresultUsageRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 8),
    _CfprQueryresultUsageRefDn_Type()
)
cfprQueryresultUsageRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageRefDn.setStatus("current")
_CfprQueryresultUsageRefName_Type = SnmpAdminString
_CfprQueryresultUsageRefName_Object = MibTableColumn
cfprQueryresultUsageRefName = _CfprQueryresultUsageRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 68, 2, 1, 9),
    _CfprQueryresultUsageRefName_Type()
)
cfprQueryresultUsageRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQueryresultUsageRefName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-QUERYRESULT-MIB",
    **{"cfprQueryresultObjects": cfprQueryresultObjects,
       "cfprQueryresultDependencyTable": cfprQueryresultDependencyTable,
       "cfprQueryresultDependencyEntry": cfprQueryresultDependencyEntry,
       "cfprQueryresultDependencyInstanceId": cfprQueryresultDependencyInstanceId,
       "cfprQueryresultDependencyDn": cfprQueryresultDependencyDn,
       "cfprQueryresultDependencyRn": cfprQueryresultDependencyRn,
       "cfprQueryresultDependencyClassType": cfprQueryresultDependencyClassType,
       "cfprQueryresultDependencyIsImportable": cfprQueryresultDependencyIsImportable,
       "cfprQueryresultDependencyPolicyOwner": cfprQueryresultDependencyPolicyOwner,
       "cfprQueryresultDependencyRefConvertedDn": cfprQueryresultDependencyRefConvertedDn,
       "cfprQueryresultDependencyRefDn": cfprQueryresultDependencyRefDn,
       "cfprQueryresultDependencyRefName": cfprQueryresultDependencyRefName,
       "cfprQueryresultUsageTable": cfprQueryresultUsageTable,
       "cfprQueryresultUsageEntry": cfprQueryresultUsageEntry,
       "cfprQueryresultUsageInstanceId": cfprQueryresultUsageInstanceId,
       "cfprQueryresultUsageDn": cfprQueryresultUsageDn,
       "cfprQueryresultUsageRn": cfprQueryresultUsageRn,
       "cfprQueryresultUsageClassType": cfprQueryresultUsageClassType,
       "cfprQueryresultUsageIsServiceTemplate": cfprQueryresultUsageIsServiceTemplate,
       "cfprQueryresultUsagePolicyOwner": cfprQueryresultUsagePolicyOwner,
       "cfprQueryresultUsageRefConvertedDn": cfprQueryresultUsageRefConvertedDn,
       "cfprQueryresultUsageRefDn": cfprQueryresultUsageRefDn,
       "cfprQueryresultUsageRefName": cfprQueryresultUsageRefName}
)
