# SNMP MIB module (CISCO-FIREPOWER-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-DOMAIN-MIB.mib
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

(CfprDomainFeatureType,
 CfprDomainFunctionalState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprDomainFeatureType",
    "CfprDomainFunctionalState")

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

cfprDomainObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprDomainEnvironmentFeatureTable_Object = MibTable
cfprDomainEnvironmentFeatureTable = _CfprDomainEnvironmentFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureTable.setStatus("current")
_CfprDomainEnvironmentFeatureEntry_Object = MibTableRow
cfprDomainEnvironmentFeatureEntry = _CfprDomainEnvironmentFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1)
)
cfprDomainEnvironmentFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainEnvironmentFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureEntry.setStatus("current")
_CfprDomainEnvironmentFeatureInstanceId_Type = CfprManagedObjectId
_CfprDomainEnvironmentFeatureInstanceId_Object = MibTableColumn
cfprDomainEnvironmentFeatureInstanceId = _CfprDomainEnvironmentFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 1),
    _CfprDomainEnvironmentFeatureInstanceId_Type()
)
cfprDomainEnvironmentFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureInstanceId.setStatus("current")
_CfprDomainEnvironmentFeatureDn_Type = CfprManagedObjectDn
_CfprDomainEnvironmentFeatureDn_Object = MibTableColumn
cfprDomainEnvironmentFeatureDn = _CfprDomainEnvironmentFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 2),
    _CfprDomainEnvironmentFeatureDn_Type()
)
cfprDomainEnvironmentFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureDn.setStatus("current")
_CfprDomainEnvironmentFeatureRn_Type = SnmpAdminString
_CfprDomainEnvironmentFeatureRn_Object = MibTableColumn
cfprDomainEnvironmentFeatureRn = _CfprDomainEnvironmentFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 3),
    _CfprDomainEnvironmentFeatureRn_Type()
)
cfprDomainEnvironmentFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureRn.setStatus("current")
_CfprDomainEnvironmentFeatureFltAggr_Type = Unsigned64
_CfprDomainEnvironmentFeatureFltAggr_Object = MibTableColumn
cfprDomainEnvironmentFeatureFltAggr = _CfprDomainEnvironmentFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 4),
    _CfprDomainEnvironmentFeatureFltAggr_Type()
)
cfprDomainEnvironmentFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureFltAggr.setStatus("current")
_CfprDomainEnvironmentFeatureFunctionalState_Type = CfprDomainFunctionalState
_CfprDomainEnvironmentFeatureFunctionalState_Object = MibTableColumn
cfprDomainEnvironmentFeatureFunctionalState = _CfprDomainEnvironmentFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 5),
    _CfprDomainEnvironmentFeatureFunctionalState_Type()
)
cfprDomainEnvironmentFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureFunctionalState.setStatus("current")
_CfprDomainEnvironmentFeatureName_Type = SnmpAdminString
_CfprDomainEnvironmentFeatureName_Object = MibTableColumn
cfprDomainEnvironmentFeatureName = _CfprDomainEnvironmentFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 6),
    _CfprDomainEnvironmentFeatureName_Type()
)
cfprDomainEnvironmentFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureName.setStatus("current")
_CfprDomainEnvironmentFeatureType_Type = CfprDomainFeatureType
_CfprDomainEnvironmentFeatureType_Object = MibTableColumn
cfprDomainEnvironmentFeatureType = _CfprDomainEnvironmentFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 1, 1, 7),
    _CfprDomainEnvironmentFeatureType_Type()
)
cfprDomainEnvironmentFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureType.setStatus("current")
_CfprDomainEnvironmentFeatureContTable_Object = MibTable
cfprDomainEnvironmentFeatureContTable = _CfprDomainEnvironmentFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 2)
)
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureContTable.setStatus("current")
_CfprDomainEnvironmentFeatureContEntry_Object = MibTableRow
cfprDomainEnvironmentFeatureContEntry = _CfprDomainEnvironmentFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 2, 1)
)
cfprDomainEnvironmentFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainEnvironmentFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureContEntry.setStatus("current")
_CfprDomainEnvironmentFeatureContInstanceId_Type = CfprManagedObjectId
_CfprDomainEnvironmentFeatureContInstanceId_Object = MibTableColumn
cfprDomainEnvironmentFeatureContInstanceId = _CfprDomainEnvironmentFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 2, 1, 1),
    _CfprDomainEnvironmentFeatureContInstanceId_Type()
)
cfprDomainEnvironmentFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureContInstanceId.setStatus("current")
_CfprDomainEnvironmentFeatureContDn_Type = CfprManagedObjectDn
_CfprDomainEnvironmentFeatureContDn_Object = MibTableColumn
cfprDomainEnvironmentFeatureContDn = _CfprDomainEnvironmentFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 2, 1, 2),
    _CfprDomainEnvironmentFeatureContDn_Type()
)
cfprDomainEnvironmentFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureContDn.setStatus("current")
_CfprDomainEnvironmentFeatureContRn_Type = SnmpAdminString
_CfprDomainEnvironmentFeatureContRn_Object = MibTableColumn
cfprDomainEnvironmentFeatureContRn = _CfprDomainEnvironmentFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 2, 1, 3),
    _CfprDomainEnvironmentFeatureContRn_Type()
)
cfprDomainEnvironmentFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureContRn.setStatus("current")
_CfprDomainEnvironmentFeatureContFltAggr_Type = Unsigned64
_CfprDomainEnvironmentFeatureContFltAggr_Object = MibTableColumn
cfprDomainEnvironmentFeatureContFltAggr = _CfprDomainEnvironmentFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 2, 1, 4),
    _CfprDomainEnvironmentFeatureContFltAggr_Type()
)
cfprDomainEnvironmentFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentFeatureContFltAggr.setStatus("current")
_CfprDomainEnvironmentParamTable_Object = MibTable
cfprDomainEnvironmentParamTable = _CfprDomainEnvironmentParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3)
)
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamTable.setStatus("current")
_CfprDomainEnvironmentParamEntry_Object = MibTableRow
cfprDomainEnvironmentParamEntry = _CfprDomainEnvironmentParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1)
)
cfprDomainEnvironmentParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainEnvironmentParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamEntry.setStatus("current")
_CfprDomainEnvironmentParamInstanceId_Type = CfprManagedObjectId
_CfprDomainEnvironmentParamInstanceId_Object = MibTableColumn
cfprDomainEnvironmentParamInstanceId = _CfprDomainEnvironmentParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1, 1),
    _CfprDomainEnvironmentParamInstanceId_Type()
)
cfprDomainEnvironmentParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamInstanceId.setStatus("current")
_CfprDomainEnvironmentParamDn_Type = CfprManagedObjectDn
_CfprDomainEnvironmentParamDn_Object = MibTableColumn
cfprDomainEnvironmentParamDn = _CfprDomainEnvironmentParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1, 2),
    _CfprDomainEnvironmentParamDn_Type()
)
cfprDomainEnvironmentParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamDn.setStatus("current")
_CfprDomainEnvironmentParamRn_Type = SnmpAdminString
_CfprDomainEnvironmentParamRn_Object = MibTableColumn
cfprDomainEnvironmentParamRn = _CfprDomainEnvironmentParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1, 3),
    _CfprDomainEnvironmentParamRn_Type()
)
cfprDomainEnvironmentParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamRn.setStatus("current")
_CfprDomainEnvironmentParamFltAggr_Type = Unsigned64
_CfprDomainEnvironmentParamFltAggr_Object = MibTableColumn
cfprDomainEnvironmentParamFltAggr = _CfprDomainEnvironmentParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1, 4),
    _CfprDomainEnvironmentParamFltAggr_Type()
)
cfprDomainEnvironmentParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamFltAggr.setStatus("current")
_CfprDomainEnvironmentParamName_Type = SnmpAdminString
_CfprDomainEnvironmentParamName_Object = MibTableColumn
cfprDomainEnvironmentParamName = _CfprDomainEnvironmentParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1, 5),
    _CfprDomainEnvironmentParamName_Type()
)
cfprDomainEnvironmentParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamName.setStatus("current")
_CfprDomainEnvironmentParamValue_Type = SnmpAdminString
_CfprDomainEnvironmentParamValue_Object = MibTableColumn
cfprDomainEnvironmentParamValue = _CfprDomainEnvironmentParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 3, 1, 6),
    _CfprDomainEnvironmentParamValue_Type()
)
cfprDomainEnvironmentParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainEnvironmentParamValue.setStatus("current")
_CfprDomainNetworkFeatureTable_Object = MibTable
cfprDomainNetworkFeatureTable = _CfprDomainNetworkFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4)
)
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureTable.setStatus("current")
_CfprDomainNetworkFeatureEntry_Object = MibTableRow
cfprDomainNetworkFeatureEntry = _CfprDomainNetworkFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1)
)
cfprDomainNetworkFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainNetworkFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureEntry.setStatus("current")
_CfprDomainNetworkFeatureInstanceId_Type = CfprManagedObjectId
_CfprDomainNetworkFeatureInstanceId_Object = MibTableColumn
cfprDomainNetworkFeatureInstanceId = _CfprDomainNetworkFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 1),
    _CfprDomainNetworkFeatureInstanceId_Type()
)
cfprDomainNetworkFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureInstanceId.setStatus("current")
_CfprDomainNetworkFeatureDn_Type = CfprManagedObjectDn
_CfprDomainNetworkFeatureDn_Object = MibTableColumn
cfprDomainNetworkFeatureDn = _CfprDomainNetworkFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 2),
    _CfprDomainNetworkFeatureDn_Type()
)
cfprDomainNetworkFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureDn.setStatus("current")
_CfprDomainNetworkFeatureRn_Type = SnmpAdminString
_CfprDomainNetworkFeatureRn_Object = MibTableColumn
cfprDomainNetworkFeatureRn = _CfprDomainNetworkFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 3),
    _CfprDomainNetworkFeatureRn_Type()
)
cfprDomainNetworkFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureRn.setStatus("current")
_CfprDomainNetworkFeatureFltAggr_Type = Unsigned64
_CfprDomainNetworkFeatureFltAggr_Object = MibTableColumn
cfprDomainNetworkFeatureFltAggr = _CfprDomainNetworkFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 4),
    _CfprDomainNetworkFeatureFltAggr_Type()
)
cfprDomainNetworkFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureFltAggr.setStatus("current")
_CfprDomainNetworkFeatureFunctionalState_Type = CfprDomainFunctionalState
_CfprDomainNetworkFeatureFunctionalState_Object = MibTableColumn
cfprDomainNetworkFeatureFunctionalState = _CfprDomainNetworkFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 5),
    _CfprDomainNetworkFeatureFunctionalState_Type()
)
cfprDomainNetworkFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureFunctionalState.setStatus("current")
_CfprDomainNetworkFeatureName_Type = SnmpAdminString
_CfprDomainNetworkFeatureName_Object = MibTableColumn
cfprDomainNetworkFeatureName = _CfprDomainNetworkFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 6),
    _CfprDomainNetworkFeatureName_Type()
)
cfprDomainNetworkFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureName.setStatus("current")
_CfprDomainNetworkFeatureType_Type = CfprDomainFeatureType
_CfprDomainNetworkFeatureType_Object = MibTableColumn
cfprDomainNetworkFeatureType = _CfprDomainNetworkFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 4, 1, 7),
    _CfprDomainNetworkFeatureType_Type()
)
cfprDomainNetworkFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureType.setStatus("current")
_CfprDomainNetworkFeatureContTable_Object = MibTable
cfprDomainNetworkFeatureContTable = _CfprDomainNetworkFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 5)
)
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureContTable.setStatus("current")
_CfprDomainNetworkFeatureContEntry_Object = MibTableRow
cfprDomainNetworkFeatureContEntry = _CfprDomainNetworkFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 5, 1)
)
cfprDomainNetworkFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainNetworkFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureContEntry.setStatus("current")
_CfprDomainNetworkFeatureContInstanceId_Type = CfprManagedObjectId
_CfprDomainNetworkFeatureContInstanceId_Object = MibTableColumn
cfprDomainNetworkFeatureContInstanceId = _CfprDomainNetworkFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 5, 1, 1),
    _CfprDomainNetworkFeatureContInstanceId_Type()
)
cfprDomainNetworkFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureContInstanceId.setStatus("current")
_CfprDomainNetworkFeatureContDn_Type = CfprManagedObjectDn
_CfprDomainNetworkFeatureContDn_Object = MibTableColumn
cfprDomainNetworkFeatureContDn = _CfprDomainNetworkFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 5, 1, 2),
    _CfprDomainNetworkFeatureContDn_Type()
)
cfprDomainNetworkFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureContDn.setStatus("current")
_CfprDomainNetworkFeatureContRn_Type = SnmpAdminString
_CfprDomainNetworkFeatureContRn_Object = MibTableColumn
cfprDomainNetworkFeatureContRn = _CfprDomainNetworkFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 5, 1, 3),
    _CfprDomainNetworkFeatureContRn_Type()
)
cfprDomainNetworkFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureContRn.setStatus("current")
_CfprDomainNetworkFeatureContFltAggr_Type = Unsigned64
_CfprDomainNetworkFeatureContFltAggr_Object = MibTableColumn
cfprDomainNetworkFeatureContFltAggr = _CfprDomainNetworkFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 5, 1, 4),
    _CfprDomainNetworkFeatureContFltAggr_Type()
)
cfprDomainNetworkFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkFeatureContFltAggr.setStatus("current")
_CfprDomainNetworkParamTable_Object = MibTable
cfprDomainNetworkParamTable = _CfprDomainNetworkParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6)
)
if mibBuilder.loadTexts:
    cfprDomainNetworkParamTable.setStatus("current")
_CfprDomainNetworkParamEntry_Object = MibTableRow
cfprDomainNetworkParamEntry = _CfprDomainNetworkParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1)
)
cfprDomainNetworkParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainNetworkParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainNetworkParamEntry.setStatus("current")
_CfprDomainNetworkParamInstanceId_Type = CfprManagedObjectId
_CfprDomainNetworkParamInstanceId_Object = MibTableColumn
cfprDomainNetworkParamInstanceId = _CfprDomainNetworkParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1, 1),
    _CfprDomainNetworkParamInstanceId_Type()
)
cfprDomainNetworkParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainNetworkParamInstanceId.setStatus("current")
_CfprDomainNetworkParamDn_Type = CfprManagedObjectDn
_CfprDomainNetworkParamDn_Object = MibTableColumn
cfprDomainNetworkParamDn = _CfprDomainNetworkParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1, 2),
    _CfprDomainNetworkParamDn_Type()
)
cfprDomainNetworkParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkParamDn.setStatus("current")
_CfprDomainNetworkParamRn_Type = SnmpAdminString
_CfprDomainNetworkParamRn_Object = MibTableColumn
cfprDomainNetworkParamRn = _CfprDomainNetworkParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1, 3),
    _CfprDomainNetworkParamRn_Type()
)
cfprDomainNetworkParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkParamRn.setStatus("current")
_CfprDomainNetworkParamFltAggr_Type = Unsigned64
_CfprDomainNetworkParamFltAggr_Object = MibTableColumn
cfprDomainNetworkParamFltAggr = _CfprDomainNetworkParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1, 4),
    _CfprDomainNetworkParamFltAggr_Type()
)
cfprDomainNetworkParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkParamFltAggr.setStatus("current")
_CfprDomainNetworkParamName_Type = SnmpAdminString
_CfprDomainNetworkParamName_Object = MibTableColumn
cfprDomainNetworkParamName = _CfprDomainNetworkParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1, 5),
    _CfprDomainNetworkParamName_Type()
)
cfprDomainNetworkParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkParamName.setStatus("current")
_CfprDomainNetworkParamValue_Type = SnmpAdminString
_CfprDomainNetworkParamValue_Object = MibTableColumn
cfprDomainNetworkParamValue = _CfprDomainNetworkParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 6, 1, 6),
    _CfprDomainNetworkParamValue_Type()
)
cfprDomainNetworkParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainNetworkParamValue.setStatus("current")
_CfprDomainServerFeatureTable_Object = MibTable
cfprDomainServerFeatureTable = _CfprDomainServerFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7)
)
if mibBuilder.loadTexts:
    cfprDomainServerFeatureTable.setStatus("current")
_CfprDomainServerFeatureEntry_Object = MibTableRow
cfprDomainServerFeatureEntry = _CfprDomainServerFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1)
)
cfprDomainServerFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainServerFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainServerFeatureEntry.setStatus("current")
_CfprDomainServerFeatureInstanceId_Type = CfprManagedObjectId
_CfprDomainServerFeatureInstanceId_Object = MibTableColumn
cfprDomainServerFeatureInstanceId = _CfprDomainServerFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 1),
    _CfprDomainServerFeatureInstanceId_Type()
)
cfprDomainServerFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureInstanceId.setStatus("current")
_CfprDomainServerFeatureDn_Type = CfprManagedObjectDn
_CfprDomainServerFeatureDn_Object = MibTableColumn
cfprDomainServerFeatureDn = _CfprDomainServerFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 2),
    _CfprDomainServerFeatureDn_Type()
)
cfprDomainServerFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureDn.setStatus("current")
_CfprDomainServerFeatureRn_Type = SnmpAdminString
_CfprDomainServerFeatureRn_Object = MibTableColumn
cfprDomainServerFeatureRn = _CfprDomainServerFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 3),
    _CfprDomainServerFeatureRn_Type()
)
cfprDomainServerFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureRn.setStatus("current")
_CfprDomainServerFeatureFltAggr_Type = Unsigned64
_CfprDomainServerFeatureFltAggr_Object = MibTableColumn
cfprDomainServerFeatureFltAggr = _CfprDomainServerFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 4),
    _CfprDomainServerFeatureFltAggr_Type()
)
cfprDomainServerFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureFltAggr.setStatus("current")
_CfprDomainServerFeatureFunctionalState_Type = CfprDomainFunctionalState
_CfprDomainServerFeatureFunctionalState_Object = MibTableColumn
cfprDomainServerFeatureFunctionalState = _CfprDomainServerFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 5),
    _CfprDomainServerFeatureFunctionalState_Type()
)
cfprDomainServerFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureFunctionalState.setStatus("current")
_CfprDomainServerFeatureName_Type = SnmpAdminString
_CfprDomainServerFeatureName_Object = MibTableColumn
cfprDomainServerFeatureName = _CfprDomainServerFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 6),
    _CfprDomainServerFeatureName_Type()
)
cfprDomainServerFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureName.setStatus("current")
_CfprDomainServerFeatureType_Type = CfprDomainFeatureType
_CfprDomainServerFeatureType_Object = MibTableColumn
cfprDomainServerFeatureType = _CfprDomainServerFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 7, 1, 7),
    _CfprDomainServerFeatureType_Type()
)
cfprDomainServerFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureType.setStatus("current")
_CfprDomainServerFeatureContTable_Object = MibTable
cfprDomainServerFeatureContTable = _CfprDomainServerFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 8)
)
if mibBuilder.loadTexts:
    cfprDomainServerFeatureContTable.setStatus("current")
_CfprDomainServerFeatureContEntry_Object = MibTableRow
cfprDomainServerFeatureContEntry = _CfprDomainServerFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 8, 1)
)
cfprDomainServerFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainServerFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainServerFeatureContEntry.setStatus("current")
_CfprDomainServerFeatureContInstanceId_Type = CfprManagedObjectId
_CfprDomainServerFeatureContInstanceId_Object = MibTableColumn
cfprDomainServerFeatureContInstanceId = _CfprDomainServerFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 8, 1, 1),
    _CfprDomainServerFeatureContInstanceId_Type()
)
cfprDomainServerFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureContInstanceId.setStatus("current")
_CfprDomainServerFeatureContDn_Type = CfprManagedObjectDn
_CfprDomainServerFeatureContDn_Object = MibTableColumn
cfprDomainServerFeatureContDn = _CfprDomainServerFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 8, 1, 2),
    _CfprDomainServerFeatureContDn_Type()
)
cfprDomainServerFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureContDn.setStatus("current")
_CfprDomainServerFeatureContRn_Type = SnmpAdminString
_CfprDomainServerFeatureContRn_Object = MibTableColumn
cfprDomainServerFeatureContRn = _CfprDomainServerFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 8, 1, 3),
    _CfprDomainServerFeatureContRn_Type()
)
cfprDomainServerFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureContRn.setStatus("current")
_CfprDomainServerFeatureContFltAggr_Type = Unsigned64
_CfprDomainServerFeatureContFltAggr_Object = MibTableColumn
cfprDomainServerFeatureContFltAggr = _CfprDomainServerFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 8, 1, 4),
    _CfprDomainServerFeatureContFltAggr_Type()
)
cfprDomainServerFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerFeatureContFltAggr.setStatus("current")
_CfprDomainServerParamTable_Object = MibTable
cfprDomainServerParamTable = _CfprDomainServerParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9)
)
if mibBuilder.loadTexts:
    cfprDomainServerParamTable.setStatus("current")
_CfprDomainServerParamEntry_Object = MibTableRow
cfprDomainServerParamEntry = _CfprDomainServerParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1)
)
cfprDomainServerParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainServerParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainServerParamEntry.setStatus("current")
_CfprDomainServerParamInstanceId_Type = CfprManagedObjectId
_CfprDomainServerParamInstanceId_Object = MibTableColumn
cfprDomainServerParamInstanceId = _CfprDomainServerParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1, 1),
    _CfprDomainServerParamInstanceId_Type()
)
cfprDomainServerParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainServerParamInstanceId.setStatus("current")
_CfprDomainServerParamDn_Type = CfprManagedObjectDn
_CfprDomainServerParamDn_Object = MibTableColumn
cfprDomainServerParamDn = _CfprDomainServerParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1, 2),
    _CfprDomainServerParamDn_Type()
)
cfprDomainServerParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerParamDn.setStatus("current")
_CfprDomainServerParamRn_Type = SnmpAdminString
_CfprDomainServerParamRn_Object = MibTableColumn
cfprDomainServerParamRn = _CfprDomainServerParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1, 3),
    _CfprDomainServerParamRn_Type()
)
cfprDomainServerParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerParamRn.setStatus("current")
_CfprDomainServerParamFltAggr_Type = Unsigned64
_CfprDomainServerParamFltAggr_Object = MibTableColumn
cfprDomainServerParamFltAggr = _CfprDomainServerParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1, 4),
    _CfprDomainServerParamFltAggr_Type()
)
cfprDomainServerParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerParamFltAggr.setStatus("current")
_CfprDomainServerParamName_Type = SnmpAdminString
_CfprDomainServerParamName_Object = MibTableColumn
cfprDomainServerParamName = _CfprDomainServerParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1, 5),
    _CfprDomainServerParamName_Type()
)
cfprDomainServerParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerParamName.setStatus("current")
_CfprDomainServerParamValue_Type = SnmpAdminString
_CfprDomainServerParamValue_Object = MibTableColumn
cfprDomainServerParamValue = _CfprDomainServerParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 9, 1, 6),
    _CfprDomainServerParamValue_Type()
)
cfprDomainServerParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainServerParamValue.setStatus("current")
_CfprDomainStorageFeatureTable_Object = MibTable
cfprDomainStorageFeatureTable = _CfprDomainStorageFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10)
)
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureTable.setStatus("current")
_CfprDomainStorageFeatureEntry_Object = MibTableRow
cfprDomainStorageFeatureEntry = _CfprDomainStorageFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1)
)
cfprDomainStorageFeatureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainStorageFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureEntry.setStatus("current")
_CfprDomainStorageFeatureInstanceId_Type = CfprManagedObjectId
_CfprDomainStorageFeatureInstanceId_Object = MibTableColumn
cfprDomainStorageFeatureInstanceId = _CfprDomainStorageFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 1),
    _CfprDomainStorageFeatureInstanceId_Type()
)
cfprDomainStorageFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureInstanceId.setStatus("current")
_CfprDomainStorageFeatureDn_Type = CfprManagedObjectDn
_CfprDomainStorageFeatureDn_Object = MibTableColumn
cfprDomainStorageFeatureDn = _CfprDomainStorageFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 2),
    _CfprDomainStorageFeatureDn_Type()
)
cfprDomainStorageFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureDn.setStatus("current")
_CfprDomainStorageFeatureRn_Type = SnmpAdminString
_CfprDomainStorageFeatureRn_Object = MibTableColumn
cfprDomainStorageFeatureRn = _CfprDomainStorageFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 3),
    _CfprDomainStorageFeatureRn_Type()
)
cfprDomainStorageFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureRn.setStatus("current")
_CfprDomainStorageFeatureFltAggr_Type = Unsigned64
_CfprDomainStorageFeatureFltAggr_Object = MibTableColumn
cfprDomainStorageFeatureFltAggr = _CfprDomainStorageFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 4),
    _CfprDomainStorageFeatureFltAggr_Type()
)
cfprDomainStorageFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureFltAggr.setStatus("current")
_CfprDomainStorageFeatureFunctionalState_Type = CfprDomainFunctionalState
_CfprDomainStorageFeatureFunctionalState_Object = MibTableColumn
cfprDomainStorageFeatureFunctionalState = _CfprDomainStorageFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 5),
    _CfprDomainStorageFeatureFunctionalState_Type()
)
cfprDomainStorageFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureFunctionalState.setStatus("current")
_CfprDomainStorageFeatureName_Type = SnmpAdminString
_CfprDomainStorageFeatureName_Object = MibTableColumn
cfprDomainStorageFeatureName = _CfprDomainStorageFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 6),
    _CfprDomainStorageFeatureName_Type()
)
cfprDomainStorageFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureName.setStatus("current")
_CfprDomainStorageFeatureType_Type = CfprDomainFeatureType
_CfprDomainStorageFeatureType_Object = MibTableColumn
cfprDomainStorageFeatureType = _CfprDomainStorageFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 10, 1, 7),
    _CfprDomainStorageFeatureType_Type()
)
cfprDomainStorageFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureType.setStatus("current")
_CfprDomainStorageFeatureContTable_Object = MibTable
cfprDomainStorageFeatureContTable = _CfprDomainStorageFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 11)
)
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureContTable.setStatus("current")
_CfprDomainStorageFeatureContEntry_Object = MibTableRow
cfprDomainStorageFeatureContEntry = _CfprDomainStorageFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 11, 1)
)
cfprDomainStorageFeatureContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainStorageFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureContEntry.setStatus("current")
_CfprDomainStorageFeatureContInstanceId_Type = CfprManagedObjectId
_CfprDomainStorageFeatureContInstanceId_Object = MibTableColumn
cfprDomainStorageFeatureContInstanceId = _CfprDomainStorageFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 11, 1, 1),
    _CfprDomainStorageFeatureContInstanceId_Type()
)
cfprDomainStorageFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureContInstanceId.setStatus("current")
_CfprDomainStorageFeatureContDn_Type = CfprManagedObjectDn
_CfprDomainStorageFeatureContDn_Object = MibTableColumn
cfprDomainStorageFeatureContDn = _CfprDomainStorageFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 11, 1, 2),
    _CfprDomainStorageFeatureContDn_Type()
)
cfprDomainStorageFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureContDn.setStatus("current")
_CfprDomainStorageFeatureContRn_Type = SnmpAdminString
_CfprDomainStorageFeatureContRn_Object = MibTableColumn
cfprDomainStorageFeatureContRn = _CfprDomainStorageFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 11, 1, 3),
    _CfprDomainStorageFeatureContRn_Type()
)
cfprDomainStorageFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureContRn.setStatus("current")
_CfprDomainStorageFeatureContFltAggr_Type = Unsigned64
_CfprDomainStorageFeatureContFltAggr_Object = MibTableColumn
cfprDomainStorageFeatureContFltAggr = _CfprDomainStorageFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 11, 1, 4),
    _CfprDomainStorageFeatureContFltAggr_Type()
)
cfprDomainStorageFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageFeatureContFltAggr.setStatus("current")
_CfprDomainStorageParamTable_Object = MibTable
cfprDomainStorageParamTable = _CfprDomainStorageParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12)
)
if mibBuilder.loadTexts:
    cfprDomainStorageParamTable.setStatus("current")
_CfprDomainStorageParamEntry_Object = MibTableRow
cfprDomainStorageParamEntry = _CfprDomainStorageParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1)
)
cfprDomainStorageParamEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DOMAIN-MIB", "cfprDomainStorageParamInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDomainStorageParamEntry.setStatus("current")
_CfprDomainStorageParamInstanceId_Type = CfprManagedObjectId
_CfprDomainStorageParamInstanceId_Object = MibTableColumn
cfprDomainStorageParamInstanceId = _CfprDomainStorageParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1, 1),
    _CfprDomainStorageParamInstanceId_Type()
)
cfprDomainStorageParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDomainStorageParamInstanceId.setStatus("current")
_CfprDomainStorageParamDn_Type = CfprManagedObjectDn
_CfprDomainStorageParamDn_Object = MibTableColumn
cfprDomainStorageParamDn = _CfprDomainStorageParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1, 2),
    _CfprDomainStorageParamDn_Type()
)
cfprDomainStorageParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageParamDn.setStatus("current")
_CfprDomainStorageParamRn_Type = SnmpAdminString
_CfprDomainStorageParamRn_Object = MibTableColumn
cfprDomainStorageParamRn = _CfprDomainStorageParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1, 3),
    _CfprDomainStorageParamRn_Type()
)
cfprDomainStorageParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageParamRn.setStatus("current")
_CfprDomainStorageParamFltAggr_Type = Unsigned64
_CfprDomainStorageParamFltAggr_Object = MibTableColumn
cfprDomainStorageParamFltAggr = _CfprDomainStorageParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1, 4),
    _CfprDomainStorageParamFltAggr_Type()
)
cfprDomainStorageParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageParamFltAggr.setStatus("current")
_CfprDomainStorageParamName_Type = SnmpAdminString
_CfprDomainStorageParamName_Object = MibTableColumn
cfprDomainStorageParamName = _CfprDomainStorageParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1, 5),
    _CfprDomainStorageParamName_Type()
)
cfprDomainStorageParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageParamName.setStatus("current")
_CfprDomainStorageParamValue_Type = SnmpAdminString
_CfprDomainStorageParamValue_Object = MibTableColumn
cfprDomainStorageParamValue = _CfprDomainStorageParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 17, 12, 1, 6),
    _CfprDomainStorageParamValue_Type()
)
cfprDomainStorageParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDomainStorageParamValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-DOMAIN-MIB",
    **{"cfprDomainObjects": cfprDomainObjects,
       "cfprDomainEnvironmentFeatureTable": cfprDomainEnvironmentFeatureTable,
       "cfprDomainEnvironmentFeatureEntry": cfprDomainEnvironmentFeatureEntry,
       "cfprDomainEnvironmentFeatureInstanceId": cfprDomainEnvironmentFeatureInstanceId,
       "cfprDomainEnvironmentFeatureDn": cfprDomainEnvironmentFeatureDn,
       "cfprDomainEnvironmentFeatureRn": cfprDomainEnvironmentFeatureRn,
       "cfprDomainEnvironmentFeatureFltAggr": cfprDomainEnvironmentFeatureFltAggr,
       "cfprDomainEnvironmentFeatureFunctionalState": cfprDomainEnvironmentFeatureFunctionalState,
       "cfprDomainEnvironmentFeatureName": cfprDomainEnvironmentFeatureName,
       "cfprDomainEnvironmentFeatureType": cfprDomainEnvironmentFeatureType,
       "cfprDomainEnvironmentFeatureContTable": cfprDomainEnvironmentFeatureContTable,
       "cfprDomainEnvironmentFeatureContEntry": cfprDomainEnvironmentFeatureContEntry,
       "cfprDomainEnvironmentFeatureContInstanceId": cfprDomainEnvironmentFeatureContInstanceId,
       "cfprDomainEnvironmentFeatureContDn": cfprDomainEnvironmentFeatureContDn,
       "cfprDomainEnvironmentFeatureContRn": cfprDomainEnvironmentFeatureContRn,
       "cfprDomainEnvironmentFeatureContFltAggr": cfprDomainEnvironmentFeatureContFltAggr,
       "cfprDomainEnvironmentParamTable": cfprDomainEnvironmentParamTable,
       "cfprDomainEnvironmentParamEntry": cfprDomainEnvironmentParamEntry,
       "cfprDomainEnvironmentParamInstanceId": cfprDomainEnvironmentParamInstanceId,
       "cfprDomainEnvironmentParamDn": cfprDomainEnvironmentParamDn,
       "cfprDomainEnvironmentParamRn": cfprDomainEnvironmentParamRn,
       "cfprDomainEnvironmentParamFltAggr": cfprDomainEnvironmentParamFltAggr,
       "cfprDomainEnvironmentParamName": cfprDomainEnvironmentParamName,
       "cfprDomainEnvironmentParamValue": cfprDomainEnvironmentParamValue,
       "cfprDomainNetworkFeatureTable": cfprDomainNetworkFeatureTable,
       "cfprDomainNetworkFeatureEntry": cfprDomainNetworkFeatureEntry,
       "cfprDomainNetworkFeatureInstanceId": cfprDomainNetworkFeatureInstanceId,
       "cfprDomainNetworkFeatureDn": cfprDomainNetworkFeatureDn,
       "cfprDomainNetworkFeatureRn": cfprDomainNetworkFeatureRn,
       "cfprDomainNetworkFeatureFltAggr": cfprDomainNetworkFeatureFltAggr,
       "cfprDomainNetworkFeatureFunctionalState": cfprDomainNetworkFeatureFunctionalState,
       "cfprDomainNetworkFeatureName": cfprDomainNetworkFeatureName,
       "cfprDomainNetworkFeatureType": cfprDomainNetworkFeatureType,
       "cfprDomainNetworkFeatureContTable": cfprDomainNetworkFeatureContTable,
       "cfprDomainNetworkFeatureContEntry": cfprDomainNetworkFeatureContEntry,
       "cfprDomainNetworkFeatureContInstanceId": cfprDomainNetworkFeatureContInstanceId,
       "cfprDomainNetworkFeatureContDn": cfprDomainNetworkFeatureContDn,
       "cfprDomainNetworkFeatureContRn": cfprDomainNetworkFeatureContRn,
       "cfprDomainNetworkFeatureContFltAggr": cfprDomainNetworkFeatureContFltAggr,
       "cfprDomainNetworkParamTable": cfprDomainNetworkParamTable,
       "cfprDomainNetworkParamEntry": cfprDomainNetworkParamEntry,
       "cfprDomainNetworkParamInstanceId": cfprDomainNetworkParamInstanceId,
       "cfprDomainNetworkParamDn": cfprDomainNetworkParamDn,
       "cfprDomainNetworkParamRn": cfprDomainNetworkParamRn,
       "cfprDomainNetworkParamFltAggr": cfprDomainNetworkParamFltAggr,
       "cfprDomainNetworkParamName": cfprDomainNetworkParamName,
       "cfprDomainNetworkParamValue": cfprDomainNetworkParamValue,
       "cfprDomainServerFeatureTable": cfprDomainServerFeatureTable,
       "cfprDomainServerFeatureEntry": cfprDomainServerFeatureEntry,
       "cfprDomainServerFeatureInstanceId": cfprDomainServerFeatureInstanceId,
       "cfprDomainServerFeatureDn": cfprDomainServerFeatureDn,
       "cfprDomainServerFeatureRn": cfprDomainServerFeatureRn,
       "cfprDomainServerFeatureFltAggr": cfprDomainServerFeatureFltAggr,
       "cfprDomainServerFeatureFunctionalState": cfprDomainServerFeatureFunctionalState,
       "cfprDomainServerFeatureName": cfprDomainServerFeatureName,
       "cfprDomainServerFeatureType": cfprDomainServerFeatureType,
       "cfprDomainServerFeatureContTable": cfprDomainServerFeatureContTable,
       "cfprDomainServerFeatureContEntry": cfprDomainServerFeatureContEntry,
       "cfprDomainServerFeatureContInstanceId": cfprDomainServerFeatureContInstanceId,
       "cfprDomainServerFeatureContDn": cfprDomainServerFeatureContDn,
       "cfprDomainServerFeatureContRn": cfprDomainServerFeatureContRn,
       "cfprDomainServerFeatureContFltAggr": cfprDomainServerFeatureContFltAggr,
       "cfprDomainServerParamTable": cfprDomainServerParamTable,
       "cfprDomainServerParamEntry": cfprDomainServerParamEntry,
       "cfprDomainServerParamInstanceId": cfprDomainServerParamInstanceId,
       "cfprDomainServerParamDn": cfprDomainServerParamDn,
       "cfprDomainServerParamRn": cfprDomainServerParamRn,
       "cfprDomainServerParamFltAggr": cfprDomainServerParamFltAggr,
       "cfprDomainServerParamName": cfprDomainServerParamName,
       "cfprDomainServerParamValue": cfprDomainServerParamValue,
       "cfprDomainStorageFeatureTable": cfprDomainStorageFeatureTable,
       "cfprDomainStorageFeatureEntry": cfprDomainStorageFeatureEntry,
       "cfprDomainStorageFeatureInstanceId": cfprDomainStorageFeatureInstanceId,
       "cfprDomainStorageFeatureDn": cfprDomainStorageFeatureDn,
       "cfprDomainStorageFeatureRn": cfprDomainStorageFeatureRn,
       "cfprDomainStorageFeatureFltAggr": cfprDomainStorageFeatureFltAggr,
       "cfprDomainStorageFeatureFunctionalState": cfprDomainStorageFeatureFunctionalState,
       "cfprDomainStorageFeatureName": cfprDomainStorageFeatureName,
       "cfprDomainStorageFeatureType": cfprDomainStorageFeatureType,
       "cfprDomainStorageFeatureContTable": cfprDomainStorageFeatureContTable,
       "cfprDomainStorageFeatureContEntry": cfprDomainStorageFeatureContEntry,
       "cfprDomainStorageFeatureContInstanceId": cfprDomainStorageFeatureContInstanceId,
       "cfprDomainStorageFeatureContDn": cfprDomainStorageFeatureContDn,
       "cfprDomainStorageFeatureContRn": cfprDomainStorageFeatureContRn,
       "cfprDomainStorageFeatureContFltAggr": cfprDomainStorageFeatureContFltAggr,
       "cfprDomainStorageParamTable": cfprDomainStorageParamTable,
       "cfprDomainStorageParamEntry": cfprDomainStorageParamEntry,
       "cfprDomainStorageParamInstanceId": cfprDomainStorageParamInstanceId,
       "cfprDomainStorageParamDn": cfprDomainStorageParamDn,
       "cfprDomainStorageParamRn": cfprDomainStorageParamRn,
       "cfprDomainStorageParamFltAggr": cfprDomainStorageParamFltAggr,
       "cfprDomainStorageParamName": cfprDomainStorageParamName,
       "cfprDomainStorageParamValue": cfprDomainStorageParamValue}
)
