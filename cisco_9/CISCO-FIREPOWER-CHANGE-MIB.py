# SNMP MIB module (CISCO-FIREPOWER-CHANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-CHANGE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
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

(CfprChangeStatus,
 CfprMoMoClassId) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprChangeStatus",
    "CfprMoMoClassId")

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

cfprChangeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprChangeChangedObjectRefTable_Object = MibTable
cfprChangeChangedObjectRefTable = _CfprChangeChangedObjectRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefTable.setStatus("current")
_CfprChangeChangedObjectRefEntry_Object = MibTableRow
cfprChangeChangedObjectRefEntry = _CfprChangeChangedObjectRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1)
)
cfprChangeChangedObjectRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CHANGE-MIB", "cfprChangeChangedObjectRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefEntry.setStatus("current")
_CfprChangeChangedObjectRefInstanceId_Type = CfprManagedObjectId
_CfprChangeChangedObjectRefInstanceId_Object = MibTableColumn
cfprChangeChangedObjectRefInstanceId = _CfprChangeChangedObjectRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 1),
    _CfprChangeChangedObjectRefInstanceId_Type()
)
cfprChangeChangedObjectRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefInstanceId.setStatus("current")
_CfprChangeChangedObjectRefDn_Type = CfprManagedObjectDn
_CfprChangeChangedObjectRefDn_Object = MibTableColumn
cfprChangeChangedObjectRefDn = _CfprChangeChangedObjectRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 2),
    _CfprChangeChangedObjectRefDn_Type()
)
cfprChangeChangedObjectRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefDn.setStatus("current")
_CfprChangeChangedObjectRefRn_Type = SnmpAdminString
_CfprChangeChangedObjectRefRn_Object = MibTableColumn
cfprChangeChangedObjectRefRn = _CfprChangeChangedObjectRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 3),
    _CfprChangeChangedObjectRefRn_Type()
)
cfprChangeChangedObjectRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefRn.setStatus("current")
_CfprChangeChangedObjectRefCentraleMoDn_Type = SnmpAdminString
_CfprChangeChangedObjectRefCentraleMoDn_Object = MibTableColumn
cfprChangeChangedObjectRefCentraleMoDn = _CfprChangeChangedObjectRefCentraleMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 4),
    _CfprChangeChangedObjectRefCentraleMoDn_Type()
)
cfprChangeChangedObjectRefCentraleMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefCentraleMoDn.setStatus("current")
_CfprChangeChangedObjectRefChangedMoClassId_Type = CfprMoMoClassId
_CfprChangeChangedObjectRefChangedMoClassId_Object = MibTableColumn
cfprChangeChangedObjectRefChangedMoClassId = _CfprChangeChangedObjectRefChangedMoClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 5),
    _CfprChangeChangedObjectRefChangedMoClassId_Type()
)
cfprChangeChangedObjectRefChangedMoClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefChangedMoClassId.setStatus("current")
_CfprChangeChangedObjectRefGuid_Type = SnmpAdminString
_CfprChangeChangedObjectRefGuid_Object = MibTableColumn
cfprChangeChangedObjectRefGuid = _CfprChangeChangedObjectRefGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 6),
    _CfprChangeChangedObjectRefGuid_Type()
)
cfprChangeChangedObjectRefGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefGuid.setStatus("current")
_CfprChangeChangedObjectRefId_Type = Gauge32
_CfprChangeChangedObjectRefId_Object = MibTableColumn
cfprChangeChangedObjectRefId = _CfprChangeChangedObjectRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 7),
    _CfprChangeChangedObjectRefId_Type()
)
cfprChangeChangedObjectRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefId.setStatus("current")
_CfprChangeChangedObjectRefOldCentraleMoDn_Type = SnmpAdminString
_CfprChangeChangedObjectRefOldCentraleMoDn_Object = MibTableColumn
cfprChangeChangedObjectRefOldCentraleMoDn = _CfprChangeChangedObjectRefOldCentraleMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 8),
    _CfprChangeChangedObjectRefOldCentraleMoDn_Type()
)
cfprChangeChangedObjectRefOldCentraleMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefOldCentraleMoDn.setStatus("current")
_CfprChangeChangedObjectRefRefObjStatus_Type = CfprChangeStatus
_CfprChangeChangedObjectRefRefObjStatus_Object = MibTableColumn
cfprChangeChangedObjectRefRefObjStatus = _CfprChangeChangedObjectRefRefObjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 9),
    _CfprChangeChangedObjectRefRefObjStatus_Type()
)
cfprChangeChangedObjectRefRefObjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefRefObjStatus.setStatus("current")
_CfprChangeChangedObjectRefFprmMoDn_Type = SnmpAdminString
_CfprChangeChangedObjectRefFprmMoDn_Object = MibTableColumn
cfprChangeChangedObjectRefFprmMoDn = _CfprChangeChangedObjectRefFprmMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 9, 1, 1, 10),
    _CfprChangeChangedObjectRefFprmMoDn_Type()
)
cfprChangeChangedObjectRefFprmMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprChangeChangedObjectRefFprmMoDn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-CHANGE-MIB",
    **{"cfprChangeObjects": cfprChangeObjects,
       "cfprChangeChangedObjectRefTable": cfprChangeChangedObjectRefTable,
       "cfprChangeChangedObjectRefEntry": cfprChangeChangedObjectRefEntry,
       "cfprChangeChangedObjectRefInstanceId": cfprChangeChangedObjectRefInstanceId,
       "cfprChangeChangedObjectRefDn": cfprChangeChangedObjectRefDn,
       "cfprChangeChangedObjectRefRn": cfprChangeChangedObjectRefRn,
       "cfprChangeChangedObjectRefCentraleMoDn": cfprChangeChangedObjectRefCentraleMoDn,
       "cfprChangeChangedObjectRefChangedMoClassId": cfprChangeChangedObjectRefChangedMoClassId,
       "cfprChangeChangedObjectRefGuid": cfprChangeChangedObjectRefGuid,
       "cfprChangeChangedObjectRefId": cfprChangeChangedObjectRefId,
       "cfprChangeChangedObjectRefOldCentraleMoDn": cfprChangeChangedObjectRefOldCentraleMoDn,
       "cfprChangeChangedObjectRefRefObjStatus": cfprChangeChangedObjectRefRefObjStatus,
       "cfprChangeChangedObjectRefFprmMoDn": cfprChangeChangedObjectRefFprmMoDn}
)
