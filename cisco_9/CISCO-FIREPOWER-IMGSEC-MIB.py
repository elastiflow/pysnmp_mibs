# SNMP MIB module (CISCO-FIREPOWER-IMGSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IMGSEC-MIB.mib
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

(CfprImgsecKeyType,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprImgsecKeyType",
    "CfprPolicyPolicyOwner")

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

cfprImgsecObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprImgsecKeyTable_Object = MibTable
cfprImgsecKeyTable = _CfprImgsecKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1)
)
if mibBuilder.loadTexts:
    cfprImgsecKeyTable.setStatus("current")
_CfprImgsecKeyEntry_Object = MibTableRow
cfprImgsecKeyEntry = _CfprImgsecKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1, 1)
)
cfprImgsecKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IMGSEC-MIB", "cfprImgsecKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprImgsecKeyEntry.setStatus("current")
_CfprImgsecKeyInstanceId_Type = CfprManagedObjectId
_CfprImgsecKeyInstanceId_Object = MibTableColumn
cfprImgsecKeyInstanceId = _CfprImgsecKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1, 1, 1),
    _CfprImgsecKeyInstanceId_Type()
)
cfprImgsecKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprImgsecKeyInstanceId.setStatus("current")
_CfprImgsecKeyDn_Type = CfprManagedObjectDn
_CfprImgsecKeyDn_Object = MibTableColumn
cfprImgsecKeyDn = _CfprImgsecKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1, 1, 2),
    _CfprImgsecKeyDn_Type()
)
cfprImgsecKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecKeyDn.setStatus("current")
_CfprImgsecKeyRn_Type = SnmpAdminString
_CfprImgsecKeyRn_Object = MibTableColumn
cfprImgsecKeyRn = _CfprImgsecKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1, 1, 3),
    _CfprImgsecKeyRn_Type()
)
cfprImgsecKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecKeyRn.setStatus("current")
_CfprImgsecKeyType_Type = CfprImgsecKeyType
_CfprImgsecKeyType_Object = MibTableColumn
cfprImgsecKeyType = _CfprImgsecKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1, 1, 4),
    _CfprImgsecKeyType_Type()
)
cfprImgsecKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecKeyType.setStatus("current")
_CfprImgsecKeyValue_Type = SnmpAdminString
_CfprImgsecKeyValue_Object = MibTableColumn
cfprImgsecKeyValue = _CfprImgsecKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 1, 1, 5),
    _CfprImgsecKeyValue_Type()
)
cfprImgsecKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecKeyValue.setStatus("current")
_CfprImgsecPolicyTable_Object = MibTable
cfprImgsecPolicyTable = _CfprImgsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2)
)
if mibBuilder.loadTexts:
    cfprImgsecPolicyTable.setStatus("current")
_CfprImgsecPolicyEntry_Object = MibTableRow
cfprImgsecPolicyEntry = _CfprImgsecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1)
)
cfprImgsecPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IMGSEC-MIB", "cfprImgsecPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprImgsecPolicyEntry.setStatus("current")
_CfprImgsecPolicyInstanceId_Type = CfprManagedObjectId
_CfprImgsecPolicyInstanceId_Object = MibTableColumn
cfprImgsecPolicyInstanceId = _CfprImgsecPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 1),
    _CfprImgsecPolicyInstanceId_Type()
)
cfprImgsecPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprImgsecPolicyInstanceId.setStatus("current")
_CfprImgsecPolicyDn_Type = CfprManagedObjectDn
_CfprImgsecPolicyDn_Object = MibTableColumn
cfprImgsecPolicyDn = _CfprImgsecPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 2),
    _CfprImgsecPolicyDn_Type()
)
cfprImgsecPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyDn.setStatus("current")
_CfprImgsecPolicyRn_Type = SnmpAdminString
_CfprImgsecPolicyRn_Object = MibTableColumn
cfprImgsecPolicyRn = _CfprImgsecPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 3),
    _CfprImgsecPolicyRn_Type()
)
cfprImgsecPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyRn.setStatus("current")
_CfprImgsecPolicyDescr_Type = SnmpAdminString
_CfprImgsecPolicyDescr_Object = MibTableColumn
cfprImgsecPolicyDescr = _CfprImgsecPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 4),
    _CfprImgsecPolicyDescr_Type()
)
cfprImgsecPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyDescr.setStatus("current")
_CfprImgsecPolicyIntId_Type = SnmpAdminString
_CfprImgsecPolicyIntId_Object = MibTableColumn
cfprImgsecPolicyIntId = _CfprImgsecPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 5),
    _CfprImgsecPolicyIntId_Type()
)
cfprImgsecPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyIntId.setStatus("current")
_CfprImgsecPolicyName_Type = SnmpAdminString
_CfprImgsecPolicyName_Object = MibTableColumn
cfprImgsecPolicyName = _CfprImgsecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 6),
    _CfprImgsecPolicyName_Type()
)
cfprImgsecPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyName.setStatus("current")
_CfprImgsecPolicyPolicyLevel_Type = Gauge32
_CfprImgsecPolicyPolicyLevel_Object = MibTableColumn
cfprImgsecPolicyPolicyLevel = _CfprImgsecPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 7),
    _CfprImgsecPolicyPolicyLevel_Type()
)
cfprImgsecPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyPolicyLevel.setStatus("current")
_CfprImgsecPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprImgsecPolicyPolicyOwner_Object = MibTableColumn
cfprImgsecPolicyPolicyOwner = _CfprImgsecPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 38, 2, 1, 8),
    _CfprImgsecPolicyPolicyOwner_Type()
)
cfprImgsecPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgsecPolicyPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IMGSEC-MIB",
    **{"cfprImgsecObjects": cfprImgsecObjects,
       "cfprImgsecKeyTable": cfprImgsecKeyTable,
       "cfprImgsecKeyEntry": cfprImgsecKeyEntry,
       "cfprImgsecKeyInstanceId": cfprImgsecKeyInstanceId,
       "cfprImgsecKeyDn": cfprImgsecKeyDn,
       "cfprImgsecKeyRn": cfprImgsecKeyRn,
       "cfprImgsecKeyType": cfprImgsecKeyType,
       "cfprImgsecKeyValue": cfprImgsecKeyValue,
       "cfprImgsecPolicyTable": cfprImgsecPolicyTable,
       "cfprImgsecPolicyEntry": cfprImgsecPolicyEntry,
       "cfprImgsecPolicyInstanceId": cfprImgsecPolicyInstanceId,
       "cfprImgsecPolicyDn": cfprImgsecPolicyDn,
       "cfprImgsecPolicyRn": cfprImgsecPolicyRn,
       "cfprImgsecPolicyDescr": cfprImgsecPolicyDescr,
       "cfprImgsecPolicyIntId": cfprImgsecPolicyIntId,
       "cfprImgsecPolicyName": cfprImgsecPolicyName,
       "cfprImgsecPolicyPolicyLevel": cfprImgsecPolicyPolicyLevel,
       "cfprImgsecPolicyPolicyOwner": cfprImgsecPolicyPolicyOwner}
)
