# SNMP MIB module (CISCO-FIREPOWER-AP-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-DOMAIN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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

(CfprApDomainFeatureType,
 CfprApDomainFunctionalState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApDomainFeatureType",
    "CfprApDomainFunctionalState")

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

cfprApDomainObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApDomainEnvironmentFeatureTable_Object = MibTable
cfprApDomainEnvironmentFeatureTable = _CfprApDomainEnvironmentFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureTable.setStatus("current")
_CfprApDomainEnvironmentFeatureEntry_Object = MibTableRow
cfprApDomainEnvironmentFeatureEntry = _CfprApDomainEnvironmentFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1)
)
cfprApDomainEnvironmentFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainEnvironmentFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureEntry.setStatus("current")
_CfprApDomainEnvironmentFeatureInstanceId_Type = CfprApManagedObjectId
_CfprApDomainEnvironmentFeatureInstanceId_Object = MibTableColumn
cfprApDomainEnvironmentFeatureInstanceId = _CfprApDomainEnvironmentFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 1),
    _CfprApDomainEnvironmentFeatureInstanceId_Type()
)
cfprApDomainEnvironmentFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureInstanceId.setStatus("current")
_CfprApDomainEnvironmentFeatureDn_Type = CfprApManagedObjectDn
_CfprApDomainEnvironmentFeatureDn_Object = MibTableColumn
cfprApDomainEnvironmentFeatureDn = _CfprApDomainEnvironmentFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 2),
    _CfprApDomainEnvironmentFeatureDn_Type()
)
cfprApDomainEnvironmentFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureDn.setStatus("current")
_CfprApDomainEnvironmentFeatureRn_Type = SnmpAdminString
_CfprApDomainEnvironmentFeatureRn_Object = MibTableColumn
cfprApDomainEnvironmentFeatureRn = _CfprApDomainEnvironmentFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 3),
    _CfprApDomainEnvironmentFeatureRn_Type()
)
cfprApDomainEnvironmentFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureRn.setStatus("current")
_CfprApDomainEnvironmentFeatureFltAggr_Type = Unsigned64
_CfprApDomainEnvironmentFeatureFltAggr_Object = MibTableColumn
cfprApDomainEnvironmentFeatureFltAggr = _CfprApDomainEnvironmentFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 4),
    _CfprApDomainEnvironmentFeatureFltAggr_Type()
)
cfprApDomainEnvironmentFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureFltAggr.setStatus("current")
_CfprApDomainEnvironmentFeatureFunctionalState_Type = CfprApDomainFunctionalState
_CfprApDomainEnvironmentFeatureFunctionalState_Object = MibTableColumn
cfprApDomainEnvironmentFeatureFunctionalState = _CfprApDomainEnvironmentFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 5),
    _CfprApDomainEnvironmentFeatureFunctionalState_Type()
)
cfprApDomainEnvironmentFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureFunctionalState.setStatus("current")
_CfprApDomainEnvironmentFeatureName_Type = SnmpAdminString
_CfprApDomainEnvironmentFeatureName_Object = MibTableColumn
cfprApDomainEnvironmentFeatureName = _CfprApDomainEnvironmentFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 6),
    _CfprApDomainEnvironmentFeatureName_Type()
)
cfprApDomainEnvironmentFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureName.setStatus("current")
_CfprApDomainEnvironmentFeatureType_Type = CfprApDomainFeatureType
_CfprApDomainEnvironmentFeatureType_Object = MibTableColumn
cfprApDomainEnvironmentFeatureType = _CfprApDomainEnvironmentFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 1, 1, 7),
    _CfprApDomainEnvironmentFeatureType_Type()
)
cfprApDomainEnvironmentFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureType.setStatus("current")
_CfprApDomainEnvironmentFeatureContTable_Object = MibTable
cfprApDomainEnvironmentFeatureContTable = _CfprApDomainEnvironmentFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 2)
)
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureContTable.setStatus("current")
_CfprApDomainEnvironmentFeatureContEntry_Object = MibTableRow
cfprApDomainEnvironmentFeatureContEntry = _CfprApDomainEnvironmentFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 2, 1)
)
cfprApDomainEnvironmentFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainEnvironmentFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureContEntry.setStatus("current")
_CfprApDomainEnvironmentFeatureContInstanceId_Type = CfprApManagedObjectId
_CfprApDomainEnvironmentFeatureContInstanceId_Object = MibTableColumn
cfprApDomainEnvironmentFeatureContInstanceId = _CfprApDomainEnvironmentFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 2, 1, 1),
    _CfprApDomainEnvironmentFeatureContInstanceId_Type()
)
cfprApDomainEnvironmentFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureContInstanceId.setStatus("current")
_CfprApDomainEnvironmentFeatureContDn_Type = CfprApManagedObjectDn
_CfprApDomainEnvironmentFeatureContDn_Object = MibTableColumn
cfprApDomainEnvironmentFeatureContDn = _CfprApDomainEnvironmentFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 2, 1, 2),
    _CfprApDomainEnvironmentFeatureContDn_Type()
)
cfprApDomainEnvironmentFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureContDn.setStatus("current")
_CfprApDomainEnvironmentFeatureContRn_Type = SnmpAdminString
_CfprApDomainEnvironmentFeatureContRn_Object = MibTableColumn
cfprApDomainEnvironmentFeatureContRn = _CfprApDomainEnvironmentFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 2, 1, 3),
    _CfprApDomainEnvironmentFeatureContRn_Type()
)
cfprApDomainEnvironmentFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureContRn.setStatus("current")
_CfprApDomainEnvironmentFeatureContFltAggr_Type = Unsigned64
_CfprApDomainEnvironmentFeatureContFltAggr_Object = MibTableColumn
cfprApDomainEnvironmentFeatureContFltAggr = _CfprApDomainEnvironmentFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 2, 1, 4),
    _CfprApDomainEnvironmentFeatureContFltAggr_Type()
)
cfprApDomainEnvironmentFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentFeatureContFltAggr.setStatus("current")
_CfprApDomainEnvironmentParamTable_Object = MibTable
cfprApDomainEnvironmentParamTable = _CfprApDomainEnvironmentParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3)
)
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamTable.setStatus("current")
_CfprApDomainEnvironmentParamEntry_Object = MibTableRow
cfprApDomainEnvironmentParamEntry = _CfprApDomainEnvironmentParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1)
)
cfprApDomainEnvironmentParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainEnvironmentParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamEntry.setStatus("current")
_CfprApDomainEnvironmentParamInstanceId_Type = CfprApManagedObjectId
_CfprApDomainEnvironmentParamInstanceId_Object = MibTableColumn
cfprApDomainEnvironmentParamInstanceId = _CfprApDomainEnvironmentParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1, 1),
    _CfprApDomainEnvironmentParamInstanceId_Type()
)
cfprApDomainEnvironmentParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamInstanceId.setStatus("current")
_CfprApDomainEnvironmentParamDn_Type = CfprApManagedObjectDn
_CfprApDomainEnvironmentParamDn_Object = MibTableColumn
cfprApDomainEnvironmentParamDn = _CfprApDomainEnvironmentParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1, 2),
    _CfprApDomainEnvironmentParamDn_Type()
)
cfprApDomainEnvironmentParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamDn.setStatus("current")
_CfprApDomainEnvironmentParamRn_Type = SnmpAdminString
_CfprApDomainEnvironmentParamRn_Object = MibTableColumn
cfprApDomainEnvironmentParamRn = _CfprApDomainEnvironmentParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1, 3),
    _CfprApDomainEnvironmentParamRn_Type()
)
cfprApDomainEnvironmentParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamRn.setStatus("current")
_CfprApDomainEnvironmentParamFltAggr_Type = Unsigned64
_CfprApDomainEnvironmentParamFltAggr_Object = MibTableColumn
cfprApDomainEnvironmentParamFltAggr = _CfprApDomainEnvironmentParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1, 4),
    _CfprApDomainEnvironmentParamFltAggr_Type()
)
cfprApDomainEnvironmentParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamFltAggr.setStatus("current")
_CfprApDomainEnvironmentParamName_Type = SnmpAdminString
_CfprApDomainEnvironmentParamName_Object = MibTableColumn
cfprApDomainEnvironmentParamName = _CfprApDomainEnvironmentParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1, 5),
    _CfprApDomainEnvironmentParamName_Type()
)
cfprApDomainEnvironmentParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamName.setStatus("current")
_CfprApDomainEnvironmentParamValue_Type = SnmpAdminString
_CfprApDomainEnvironmentParamValue_Object = MibTableColumn
cfprApDomainEnvironmentParamValue = _CfprApDomainEnvironmentParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 3, 1, 6),
    _CfprApDomainEnvironmentParamValue_Type()
)
cfprApDomainEnvironmentParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainEnvironmentParamValue.setStatus("current")
_CfprApDomainNetworkFeatureTable_Object = MibTable
cfprApDomainNetworkFeatureTable = _CfprApDomainNetworkFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4)
)
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureTable.setStatus("current")
_CfprApDomainNetworkFeatureEntry_Object = MibTableRow
cfprApDomainNetworkFeatureEntry = _CfprApDomainNetworkFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1)
)
cfprApDomainNetworkFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainNetworkFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureEntry.setStatus("current")
_CfprApDomainNetworkFeatureInstanceId_Type = CfprApManagedObjectId
_CfprApDomainNetworkFeatureInstanceId_Object = MibTableColumn
cfprApDomainNetworkFeatureInstanceId = _CfprApDomainNetworkFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 1),
    _CfprApDomainNetworkFeatureInstanceId_Type()
)
cfprApDomainNetworkFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureInstanceId.setStatus("current")
_CfprApDomainNetworkFeatureDn_Type = CfprApManagedObjectDn
_CfprApDomainNetworkFeatureDn_Object = MibTableColumn
cfprApDomainNetworkFeatureDn = _CfprApDomainNetworkFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 2),
    _CfprApDomainNetworkFeatureDn_Type()
)
cfprApDomainNetworkFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureDn.setStatus("current")
_CfprApDomainNetworkFeatureRn_Type = SnmpAdminString
_CfprApDomainNetworkFeatureRn_Object = MibTableColumn
cfprApDomainNetworkFeatureRn = _CfprApDomainNetworkFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 3),
    _CfprApDomainNetworkFeatureRn_Type()
)
cfprApDomainNetworkFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureRn.setStatus("current")
_CfprApDomainNetworkFeatureFltAggr_Type = Unsigned64
_CfprApDomainNetworkFeatureFltAggr_Object = MibTableColumn
cfprApDomainNetworkFeatureFltAggr = _CfprApDomainNetworkFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 4),
    _CfprApDomainNetworkFeatureFltAggr_Type()
)
cfprApDomainNetworkFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureFltAggr.setStatus("current")
_CfprApDomainNetworkFeatureFunctionalState_Type = CfprApDomainFunctionalState
_CfprApDomainNetworkFeatureFunctionalState_Object = MibTableColumn
cfprApDomainNetworkFeatureFunctionalState = _CfprApDomainNetworkFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 5),
    _CfprApDomainNetworkFeatureFunctionalState_Type()
)
cfprApDomainNetworkFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureFunctionalState.setStatus("current")
_CfprApDomainNetworkFeatureName_Type = SnmpAdminString
_CfprApDomainNetworkFeatureName_Object = MibTableColumn
cfprApDomainNetworkFeatureName = _CfprApDomainNetworkFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 6),
    _CfprApDomainNetworkFeatureName_Type()
)
cfprApDomainNetworkFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureName.setStatus("current")
_CfprApDomainNetworkFeatureType_Type = CfprApDomainFeatureType
_CfprApDomainNetworkFeatureType_Object = MibTableColumn
cfprApDomainNetworkFeatureType = _CfprApDomainNetworkFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 4, 1, 7),
    _CfprApDomainNetworkFeatureType_Type()
)
cfprApDomainNetworkFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureType.setStatus("current")
_CfprApDomainNetworkFeatureContTable_Object = MibTable
cfprApDomainNetworkFeatureContTable = _CfprApDomainNetworkFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 5)
)
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureContTable.setStatus("current")
_CfprApDomainNetworkFeatureContEntry_Object = MibTableRow
cfprApDomainNetworkFeatureContEntry = _CfprApDomainNetworkFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 5, 1)
)
cfprApDomainNetworkFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainNetworkFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureContEntry.setStatus("current")
_CfprApDomainNetworkFeatureContInstanceId_Type = CfprApManagedObjectId
_CfprApDomainNetworkFeatureContInstanceId_Object = MibTableColumn
cfprApDomainNetworkFeatureContInstanceId = _CfprApDomainNetworkFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 5, 1, 1),
    _CfprApDomainNetworkFeatureContInstanceId_Type()
)
cfprApDomainNetworkFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureContInstanceId.setStatus("current")
_CfprApDomainNetworkFeatureContDn_Type = CfprApManagedObjectDn
_CfprApDomainNetworkFeatureContDn_Object = MibTableColumn
cfprApDomainNetworkFeatureContDn = _CfprApDomainNetworkFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 5, 1, 2),
    _CfprApDomainNetworkFeatureContDn_Type()
)
cfprApDomainNetworkFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureContDn.setStatus("current")
_CfprApDomainNetworkFeatureContRn_Type = SnmpAdminString
_CfprApDomainNetworkFeatureContRn_Object = MibTableColumn
cfprApDomainNetworkFeatureContRn = _CfprApDomainNetworkFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 5, 1, 3),
    _CfprApDomainNetworkFeatureContRn_Type()
)
cfprApDomainNetworkFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureContRn.setStatus("current")
_CfprApDomainNetworkFeatureContFltAggr_Type = Unsigned64
_CfprApDomainNetworkFeatureContFltAggr_Object = MibTableColumn
cfprApDomainNetworkFeatureContFltAggr = _CfprApDomainNetworkFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 5, 1, 4),
    _CfprApDomainNetworkFeatureContFltAggr_Type()
)
cfprApDomainNetworkFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkFeatureContFltAggr.setStatus("current")
_CfprApDomainNetworkParamTable_Object = MibTable
cfprApDomainNetworkParamTable = _CfprApDomainNetworkParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6)
)
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamTable.setStatus("current")
_CfprApDomainNetworkParamEntry_Object = MibTableRow
cfprApDomainNetworkParamEntry = _CfprApDomainNetworkParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1)
)
cfprApDomainNetworkParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainNetworkParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamEntry.setStatus("current")
_CfprApDomainNetworkParamInstanceId_Type = CfprApManagedObjectId
_CfprApDomainNetworkParamInstanceId_Object = MibTableColumn
cfprApDomainNetworkParamInstanceId = _CfprApDomainNetworkParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1, 1),
    _CfprApDomainNetworkParamInstanceId_Type()
)
cfprApDomainNetworkParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamInstanceId.setStatus("current")
_CfprApDomainNetworkParamDn_Type = CfprApManagedObjectDn
_CfprApDomainNetworkParamDn_Object = MibTableColumn
cfprApDomainNetworkParamDn = _CfprApDomainNetworkParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1, 2),
    _CfprApDomainNetworkParamDn_Type()
)
cfprApDomainNetworkParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamDn.setStatus("current")
_CfprApDomainNetworkParamRn_Type = SnmpAdminString
_CfprApDomainNetworkParamRn_Object = MibTableColumn
cfprApDomainNetworkParamRn = _CfprApDomainNetworkParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1, 3),
    _CfprApDomainNetworkParamRn_Type()
)
cfprApDomainNetworkParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamRn.setStatus("current")
_CfprApDomainNetworkParamFltAggr_Type = Unsigned64
_CfprApDomainNetworkParamFltAggr_Object = MibTableColumn
cfprApDomainNetworkParamFltAggr = _CfprApDomainNetworkParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1, 4),
    _CfprApDomainNetworkParamFltAggr_Type()
)
cfprApDomainNetworkParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamFltAggr.setStatus("current")
_CfprApDomainNetworkParamName_Type = SnmpAdminString
_CfprApDomainNetworkParamName_Object = MibTableColumn
cfprApDomainNetworkParamName = _CfprApDomainNetworkParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1, 5),
    _CfprApDomainNetworkParamName_Type()
)
cfprApDomainNetworkParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamName.setStatus("current")
_CfprApDomainNetworkParamValue_Type = SnmpAdminString
_CfprApDomainNetworkParamValue_Object = MibTableColumn
cfprApDomainNetworkParamValue = _CfprApDomainNetworkParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 6, 1, 6),
    _CfprApDomainNetworkParamValue_Type()
)
cfprApDomainNetworkParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainNetworkParamValue.setStatus("current")
_CfprApDomainServerFeatureTable_Object = MibTable
cfprApDomainServerFeatureTable = _CfprApDomainServerFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7)
)
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureTable.setStatus("current")
_CfprApDomainServerFeatureEntry_Object = MibTableRow
cfprApDomainServerFeatureEntry = _CfprApDomainServerFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1)
)
cfprApDomainServerFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainServerFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureEntry.setStatus("current")
_CfprApDomainServerFeatureInstanceId_Type = CfprApManagedObjectId
_CfprApDomainServerFeatureInstanceId_Object = MibTableColumn
cfprApDomainServerFeatureInstanceId = _CfprApDomainServerFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 1),
    _CfprApDomainServerFeatureInstanceId_Type()
)
cfprApDomainServerFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureInstanceId.setStatus("current")
_CfprApDomainServerFeatureDn_Type = CfprApManagedObjectDn
_CfprApDomainServerFeatureDn_Object = MibTableColumn
cfprApDomainServerFeatureDn = _CfprApDomainServerFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 2),
    _CfprApDomainServerFeatureDn_Type()
)
cfprApDomainServerFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureDn.setStatus("current")
_CfprApDomainServerFeatureRn_Type = SnmpAdminString
_CfprApDomainServerFeatureRn_Object = MibTableColumn
cfprApDomainServerFeatureRn = _CfprApDomainServerFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 3),
    _CfprApDomainServerFeatureRn_Type()
)
cfprApDomainServerFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureRn.setStatus("current")
_CfprApDomainServerFeatureFltAggr_Type = Unsigned64
_CfprApDomainServerFeatureFltAggr_Object = MibTableColumn
cfprApDomainServerFeatureFltAggr = _CfprApDomainServerFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 4),
    _CfprApDomainServerFeatureFltAggr_Type()
)
cfprApDomainServerFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureFltAggr.setStatus("current")
_CfprApDomainServerFeatureFunctionalState_Type = CfprApDomainFunctionalState
_CfprApDomainServerFeatureFunctionalState_Object = MibTableColumn
cfprApDomainServerFeatureFunctionalState = _CfprApDomainServerFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 5),
    _CfprApDomainServerFeatureFunctionalState_Type()
)
cfprApDomainServerFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureFunctionalState.setStatus("current")
_CfprApDomainServerFeatureName_Type = SnmpAdminString
_CfprApDomainServerFeatureName_Object = MibTableColumn
cfprApDomainServerFeatureName = _CfprApDomainServerFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 6),
    _CfprApDomainServerFeatureName_Type()
)
cfprApDomainServerFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureName.setStatus("current")
_CfprApDomainServerFeatureType_Type = CfprApDomainFeatureType
_CfprApDomainServerFeatureType_Object = MibTableColumn
cfprApDomainServerFeatureType = _CfprApDomainServerFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 7, 1, 7),
    _CfprApDomainServerFeatureType_Type()
)
cfprApDomainServerFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureType.setStatus("current")
_CfprApDomainServerFeatureContTable_Object = MibTable
cfprApDomainServerFeatureContTable = _CfprApDomainServerFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 8)
)
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureContTable.setStatus("current")
_CfprApDomainServerFeatureContEntry_Object = MibTableRow
cfprApDomainServerFeatureContEntry = _CfprApDomainServerFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 8, 1)
)
cfprApDomainServerFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainServerFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureContEntry.setStatus("current")
_CfprApDomainServerFeatureContInstanceId_Type = CfprApManagedObjectId
_CfprApDomainServerFeatureContInstanceId_Object = MibTableColumn
cfprApDomainServerFeatureContInstanceId = _CfprApDomainServerFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 8, 1, 1),
    _CfprApDomainServerFeatureContInstanceId_Type()
)
cfprApDomainServerFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureContInstanceId.setStatus("current")
_CfprApDomainServerFeatureContDn_Type = CfprApManagedObjectDn
_CfprApDomainServerFeatureContDn_Object = MibTableColumn
cfprApDomainServerFeatureContDn = _CfprApDomainServerFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 8, 1, 2),
    _CfprApDomainServerFeatureContDn_Type()
)
cfprApDomainServerFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureContDn.setStatus("current")
_CfprApDomainServerFeatureContRn_Type = SnmpAdminString
_CfprApDomainServerFeatureContRn_Object = MibTableColumn
cfprApDomainServerFeatureContRn = _CfprApDomainServerFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 8, 1, 3),
    _CfprApDomainServerFeatureContRn_Type()
)
cfprApDomainServerFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureContRn.setStatus("current")
_CfprApDomainServerFeatureContFltAggr_Type = Unsigned64
_CfprApDomainServerFeatureContFltAggr_Object = MibTableColumn
cfprApDomainServerFeatureContFltAggr = _CfprApDomainServerFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 8, 1, 4),
    _CfprApDomainServerFeatureContFltAggr_Type()
)
cfprApDomainServerFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerFeatureContFltAggr.setStatus("current")
_CfprApDomainServerParamTable_Object = MibTable
cfprApDomainServerParamTable = _CfprApDomainServerParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9)
)
if mibBuilder.loadTexts:
    cfprApDomainServerParamTable.setStatus("current")
_CfprApDomainServerParamEntry_Object = MibTableRow
cfprApDomainServerParamEntry = _CfprApDomainServerParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1)
)
cfprApDomainServerParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainServerParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainServerParamEntry.setStatus("current")
_CfprApDomainServerParamInstanceId_Type = CfprApManagedObjectId
_CfprApDomainServerParamInstanceId_Object = MibTableColumn
cfprApDomainServerParamInstanceId = _CfprApDomainServerParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1, 1),
    _CfprApDomainServerParamInstanceId_Type()
)
cfprApDomainServerParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainServerParamInstanceId.setStatus("current")
_CfprApDomainServerParamDn_Type = CfprApManagedObjectDn
_CfprApDomainServerParamDn_Object = MibTableColumn
cfprApDomainServerParamDn = _CfprApDomainServerParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1, 2),
    _CfprApDomainServerParamDn_Type()
)
cfprApDomainServerParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerParamDn.setStatus("current")
_CfprApDomainServerParamRn_Type = SnmpAdminString
_CfprApDomainServerParamRn_Object = MibTableColumn
cfprApDomainServerParamRn = _CfprApDomainServerParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1, 3),
    _CfprApDomainServerParamRn_Type()
)
cfprApDomainServerParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerParamRn.setStatus("current")
_CfprApDomainServerParamFltAggr_Type = Unsigned64
_CfprApDomainServerParamFltAggr_Object = MibTableColumn
cfprApDomainServerParamFltAggr = _CfprApDomainServerParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1, 4),
    _CfprApDomainServerParamFltAggr_Type()
)
cfprApDomainServerParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerParamFltAggr.setStatus("current")
_CfprApDomainServerParamName_Type = SnmpAdminString
_CfprApDomainServerParamName_Object = MibTableColumn
cfprApDomainServerParamName = _CfprApDomainServerParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1, 5),
    _CfprApDomainServerParamName_Type()
)
cfprApDomainServerParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerParamName.setStatus("current")
_CfprApDomainServerParamValue_Type = SnmpAdminString
_CfprApDomainServerParamValue_Object = MibTableColumn
cfprApDomainServerParamValue = _CfprApDomainServerParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 9, 1, 6),
    _CfprApDomainServerParamValue_Type()
)
cfprApDomainServerParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainServerParamValue.setStatus("current")
_CfprApDomainStorageFeatureTable_Object = MibTable
cfprApDomainStorageFeatureTable = _CfprApDomainStorageFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10)
)
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureTable.setStatus("current")
_CfprApDomainStorageFeatureEntry_Object = MibTableRow
cfprApDomainStorageFeatureEntry = _CfprApDomainStorageFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1)
)
cfprApDomainStorageFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainStorageFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureEntry.setStatus("current")
_CfprApDomainStorageFeatureInstanceId_Type = CfprApManagedObjectId
_CfprApDomainStorageFeatureInstanceId_Object = MibTableColumn
cfprApDomainStorageFeatureInstanceId = _CfprApDomainStorageFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 1),
    _CfprApDomainStorageFeatureInstanceId_Type()
)
cfprApDomainStorageFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureInstanceId.setStatus("current")
_CfprApDomainStorageFeatureDn_Type = CfprApManagedObjectDn
_CfprApDomainStorageFeatureDn_Object = MibTableColumn
cfprApDomainStorageFeatureDn = _CfprApDomainStorageFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 2),
    _CfprApDomainStorageFeatureDn_Type()
)
cfprApDomainStorageFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureDn.setStatus("current")
_CfprApDomainStorageFeatureRn_Type = SnmpAdminString
_CfprApDomainStorageFeatureRn_Object = MibTableColumn
cfprApDomainStorageFeatureRn = _CfprApDomainStorageFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 3),
    _CfprApDomainStorageFeatureRn_Type()
)
cfprApDomainStorageFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureRn.setStatus("current")
_CfprApDomainStorageFeatureFltAggr_Type = Unsigned64
_CfprApDomainStorageFeatureFltAggr_Object = MibTableColumn
cfprApDomainStorageFeatureFltAggr = _CfprApDomainStorageFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 4),
    _CfprApDomainStorageFeatureFltAggr_Type()
)
cfprApDomainStorageFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureFltAggr.setStatus("current")
_CfprApDomainStorageFeatureFunctionalState_Type = CfprApDomainFunctionalState
_CfprApDomainStorageFeatureFunctionalState_Object = MibTableColumn
cfprApDomainStorageFeatureFunctionalState = _CfprApDomainStorageFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 5),
    _CfprApDomainStorageFeatureFunctionalState_Type()
)
cfprApDomainStorageFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureFunctionalState.setStatus("current")
_CfprApDomainStorageFeatureName_Type = SnmpAdminString
_CfprApDomainStorageFeatureName_Object = MibTableColumn
cfprApDomainStorageFeatureName = _CfprApDomainStorageFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 6),
    _CfprApDomainStorageFeatureName_Type()
)
cfprApDomainStorageFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureName.setStatus("current")
_CfprApDomainStorageFeatureType_Type = CfprApDomainFeatureType
_CfprApDomainStorageFeatureType_Object = MibTableColumn
cfprApDomainStorageFeatureType = _CfprApDomainStorageFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 10, 1, 7),
    _CfprApDomainStorageFeatureType_Type()
)
cfprApDomainStorageFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureType.setStatus("current")
_CfprApDomainStorageFeatureContTable_Object = MibTable
cfprApDomainStorageFeatureContTable = _CfprApDomainStorageFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 11)
)
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureContTable.setStatus("current")
_CfprApDomainStorageFeatureContEntry_Object = MibTableRow
cfprApDomainStorageFeatureContEntry = _CfprApDomainStorageFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 11, 1)
)
cfprApDomainStorageFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainStorageFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureContEntry.setStatus("current")
_CfprApDomainStorageFeatureContInstanceId_Type = CfprApManagedObjectId
_CfprApDomainStorageFeatureContInstanceId_Object = MibTableColumn
cfprApDomainStorageFeatureContInstanceId = _CfprApDomainStorageFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 11, 1, 1),
    _CfprApDomainStorageFeatureContInstanceId_Type()
)
cfprApDomainStorageFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureContInstanceId.setStatus("current")
_CfprApDomainStorageFeatureContDn_Type = CfprApManagedObjectDn
_CfprApDomainStorageFeatureContDn_Object = MibTableColumn
cfprApDomainStorageFeatureContDn = _CfprApDomainStorageFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 11, 1, 2),
    _CfprApDomainStorageFeatureContDn_Type()
)
cfprApDomainStorageFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureContDn.setStatus("current")
_CfprApDomainStorageFeatureContRn_Type = SnmpAdminString
_CfprApDomainStorageFeatureContRn_Object = MibTableColumn
cfprApDomainStorageFeatureContRn = _CfprApDomainStorageFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 11, 1, 3),
    _CfprApDomainStorageFeatureContRn_Type()
)
cfprApDomainStorageFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureContRn.setStatus("current")
_CfprApDomainStorageFeatureContFltAggr_Type = Unsigned64
_CfprApDomainStorageFeatureContFltAggr_Object = MibTableColumn
cfprApDomainStorageFeatureContFltAggr = _CfprApDomainStorageFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 11, 1, 4),
    _CfprApDomainStorageFeatureContFltAggr_Type()
)
cfprApDomainStorageFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageFeatureContFltAggr.setStatus("current")
_CfprApDomainStorageParamTable_Object = MibTable
cfprApDomainStorageParamTable = _CfprApDomainStorageParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12)
)
if mibBuilder.loadTexts:
    cfprApDomainStorageParamTable.setStatus("current")
_CfprApDomainStorageParamEntry_Object = MibTableRow
cfprApDomainStorageParamEntry = _CfprApDomainStorageParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1)
)
cfprApDomainStorageParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DOMAIN-MIB", "cfprApDomainStorageParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDomainStorageParamEntry.setStatus("current")
_CfprApDomainStorageParamInstanceId_Type = CfprApManagedObjectId
_CfprApDomainStorageParamInstanceId_Object = MibTableColumn
cfprApDomainStorageParamInstanceId = _CfprApDomainStorageParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1, 1),
    _CfprApDomainStorageParamInstanceId_Type()
)
cfprApDomainStorageParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDomainStorageParamInstanceId.setStatus("current")
_CfprApDomainStorageParamDn_Type = CfprApManagedObjectDn
_CfprApDomainStorageParamDn_Object = MibTableColumn
cfprApDomainStorageParamDn = _CfprApDomainStorageParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1, 2),
    _CfprApDomainStorageParamDn_Type()
)
cfprApDomainStorageParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageParamDn.setStatus("current")
_CfprApDomainStorageParamRn_Type = SnmpAdminString
_CfprApDomainStorageParamRn_Object = MibTableColumn
cfprApDomainStorageParamRn = _CfprApDomainStorageParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1, 3),
    _CfprApDomainStorageParamRn_Type()
)
cfprApDomainStorageParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageParamRn.setStatus("current")
_CfprApDomainStorageParamFltAggr_Type = Unsigned64
_CfprApDomainStorageParamFltAggr_Object = MibTableColumn
cfprApDomainStorageParamFltAggr = _CfprApDomainStorageParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1, 4),
    _CfprApDomainStorageParamFltAggr_Type()
)
cfprApDomainStorageParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageParamFltAggr.setStatus("current")
_CfprApDomainStorageParamName_Type = SnmpAdminString
_CfprApDomainStorageParamName_Object = MibTableColumn
cfprApDomainStorageParamName = _CfprApDomainStorageParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1, 5),
    _CfprApDomainStorageParamName_Type()
)
cfprApDomainStorageParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageParamName.setStatus("current")
_CfprApDomainStorageParamValue_Type = SnmpAdminString
_CfprApDomainStorageParamValue_Object = MibTableColumn
cfprApDomainStorageParamValue = _CfprApDomainStorageParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 17, 12, 1, 6),
    _CfprApDomainStorageParamValue_Type()
)
cfprApDomainStorageParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDomainStorageParamValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-DOMAIN-MIB",
    **{"cfprApDomainObjects": cfprApDomainObjects,
       "cfprApDomainEnvironmentFeatureTable": cfprApDomainEnvironmentFeatureTable,
       "cfprApDomainEnvironmentFeatureEntry": cfprApDomainEnvironmentFeatureEntry,
       "cfprApDomainEnvironmentFeatureInstanceId": cfprApDomainEnvironmentFeatureInstanceId,
       "cfprApDomainEnvironmentFeatureDn": cfprApDomainEnvironmentFeatureDn,
       "cfprApDomainEnvironmentFeatureRn": cfprApDomainEnvironmentFeatureRn,
       "cfprApDomainEnvironmentFeatureFltAggr": cfprApDomainEnvironmentFeatureFltAggr,
       "cfprApDomainEnvironmentFeatureFunctionalState": cfprApDomainEnvironmentFeatureFunctionalState,
       "cfprApDomainEnvironmentFeatureName": cfprApDomainEnvironmentFeatureName,
       "cfprApDomainEnvironmentFeatureType": cfprApDomainEnvironmentFeatureType,
       "cfprApDomainEnvironmentFeatureContTable": cfprApDomainEnvironmentFeatureContTable,
       "cfprApDomainEnvironmentFeatureContEntry": cfprApDomainEnvironmentFeatureContEntry,
       "cfprApDomainEnvironmentFeatureContInstanceId": cfprApDomainEnvironmentFeatureContInstanceId,
       "cfprApDomainEnvironmentFeatureContDn": cfprApDomainEnvironmentFeatureContDn,
       "cfprApDomainEnvironmentFeatureContRn": cfprApDomainEnvironmentFeatureContRn,
       "cfprApDomainEnvironmentFeatureContFltAggr": cfprApDomainEnvironmentFeatureContFltAggr,
       "cfprApDomainEnvironmentParamTable": cfprApDomainEnvironmentParamTable,
       "cfprApDomainEnvironmentParamEntry": cfprApDomainEnvironmentParamEntry,
       "cfprApDomainEnvironmentParamInstanceId": cfprApDomainEnvironmentParamInstanceId,
       "cfprApDomainEnvironmentParamDn": cfprApDomainEnvironmentParamDn,
       "cfprApDomainEnvironmentParamRn": cfprApDomainEnvironmentParamRn,
       "cfprApDomainEnvironmentParamFltAggr": cfprApDomainEnvironmentParamFltAggr,
       "cfprApDomainEnvironmentParamName": cfprApDomainEnvironmentParamName,
       "cfprApDomainEnvironmentParamValue": cfprApDomainEnvironmentParamValue,
       "cfprApDomainNetworkFeatureTable": cfprApDomainNetworkFeatureTable,
       "cfprApDomainNetworkFeatureEntry": cfprApDomainNetworkFeatureEntry,
       "cfprApDomainNetworkFeatureInstanceId": cfprApDomainNetworkFeatureInstanceId,
       "cfprApDomainNetworkFeatureDn": cfprApDomainNetworkFeatureDn,
       "cfprApDomainNetworkFeatureRn": cfprApDomainNetworkFeatureRn,
       "cfprApDomainNetworkFeatureFltAggr": cfprApDomainNetworkFeatureFltAggr,
       "cfprApDomainNetworkFeatureFunctionalState": cfprApDomainNetworkFeatureFunctionalState,
       "cfprApDomainNetworkFeatureName": cfprApDomainNetworkFeatureName,
       "cfprApDomainNetworkFeatureType": cfprApDomainNetworkFeatureType,
       "cfprApDomainNetworkFeatureContTable": cfprApDomainNetworkFeatureContTable,
       "cfprApDomainNetworkFeatureContEntry": cfprApDomainNetworkFeatureContEntry,
       "cfprApDomainNetworkFeatureContInstanceId": cfprApDomainNetworkFeatureContInstanceId,
       "cfprApDomainNetworkFeatureContDn": cfprApDomainNetworkFeatureContDn,
       "cfprApDomainNetworkFeatureContRn": cfprApDomainNetworkFeatureContRn,
       "cfprApDomainNetworkFeatureContFltAggr": cfprApDomainNetworkFeatureContFltAggr,
       "cfprApDomainNetworkParamTable": cfprApDomainNetworkParamTable,
       "cfprApDomainNetworkParamEntry": cfprApDomainNetworkParamEntry,
       "cfprApDomainNetworkParamInstanceId": cfprApDomainNetworkParamInstanceId,
       "cfprApDomainNetworkParamDn": cfprApDomainNetworkParamDn,
       "cfprApDomainNetworkParamRn": cfprApDomainNetworkParamRn,
       "cfprApDomainNetworkParamFltAggr": cfprApDomainNetworkParamFltAggr,
       "cfprApDomainNetworkParamName": cfprApDomainNetworkParamName,
       "cfprApDomainNetworkParamValue": cfprApDomainNetworkParamValue,
       "cfprApDomainServerFeatureTable": cfprApDomainServerFeatureTable,
       "cfprApDomainServerFeatureEntry": cfprApDomainServerFeatureEntry,
       "cfprApDomainServerFeatureInstanceId": cfprApDomainServerFeatureInstanceId,
       "cfprApDomainServerFeatureDn": cfprApDomainServerFeatureDn,
       "cfprApDomainServerFeatureRn": cfprApDomainServerFeatureRn,
       "cfprApDomainServerFeatureFltAggr": cfprApDomainServerFeatureFltAggr,
       "cfprApDomainServerFeatureFunctionalState": cfprApDomainServerFeatureFunctionalState,
       "cfprApDomainServerFeatureName": cfprApDomainServerFeatureName,
       "cfprApDomainServerFeatureType": cfprApDomainServerFeatureType,
       "cfprApDomainServerFeatureContTable": cfprApDomainServerFeatureContTable,
       "cfprApDomainServerFeatureContEntry": cfprApDomainServerFeatureContEntry,
       "cfprApDomainServerFeatureContInstanceId": cfprApDomainServerFeatureContInstanceId,
       "cfprApDomainServerFeatureContDn": cfprApDomainServerFeatureContDn,
       "cfprApDomainServerFeatureContRn": cfprApDomainServerFeatureContRn,
       "cfprApDomainServerFeatureContFltAggr": cfprApDomainServerFeatureContFltAggr,
       "cfprApDomainServerParamTable": cfprApDomainServerParamTable,
       "cfprApDomainServerParamEntry": cfprApDomainServerParamEntry,
       "cfprApDomainServerParamInstanceId": cfprApDomainServerParamInstanceId,
       "cfprApDomainServerParamDn": cfprApDomainServerParamDn,
       "cfprApDomainServerParamRn": cfprApDomainServerParamRn,
       "cfprApDomainServerParamFltAggr": cfprApDomainServerParamFltAggr,
       "cfprApDomainServerParamName": cfprApDomainServerParamName,
       "cfprApDomainServerParamValue": cfprApDomainServerParamValue,
       "cfprApDomainStorageFeatureTable": cfprApDomainStorageFeatureTable,
       "cfprApDomainStorageFeatureEntry": cfprApDomainStorageFeatureEntry,
       "cfprApDomainStorageFeatureInstanceId": cfprApDomainStorageFeatureInstanceId,
       "cfprApDomainStorageFeatureDn": cfprApDomainStorageFeatureDn,
       "cfprApDomainStorageFeatureRn": cfprApDomainStorageFeatureRn,
       "cfprApDomainStorageFeatureFltAggr": cfprApDomainStorageFeatureFltAggr,
       "cfprApDomainStorageFeatureFunctionalState": cfprApDomainStorageFeatureFunctionalState,
       "cfprApDomainStorageFeatureName": cfprApDomainStorageFeatureName,
       "cfprApDomainStorageFeatureType": cfprApDomainStorageFeatureType,
       "cfprApDomainStorageFeatureContTable": cfprApDomainStorageFeatureContTable,
       "cfprApDomainStorageFeatureContEntry": cfprApDomainStorageFeatureContEntry,
       "cfprApDomainStorageFeatureContInstanceId": cfprApDomainStorageFeatureContInstanceId,
       "cfprApDomainStorageFeatureContDn": cfprApDomainStorageFeatureContDn,
       "cfprApDomainStorageFeatureContRn": cfprApDomainStorageFeatureContRn,
       "cfprApDomainStorageFeatureContFltAggr": cfprApDomainStorageFeatureContFltAggr,
       "cfprApDomainStorageParamTable": cfprApDomainStorageParamTable,
       "cfprApDomainStorageParamEntry": cfprApDomainStorageParamEntry,
       "cfprApDomainStorageParamInstanceId": cfprApDomainStorageParamInstanceId,
       "cfprApDomainStorageParamDn": cfprApDomainStorageParamDn,
       "cfprApDomainStorageParamRn": cfprApDomainStorageParamRn,
       "cfprApDomainStorageParamFltAggr": cfprApDomainStorageParamFltAggr,
       "cfprApDomainStorageParamName": cfprApDomainStorageParamName,
       "cfprApDomainStorageParamValue": cfprApDomainStorageParamValue}
)
