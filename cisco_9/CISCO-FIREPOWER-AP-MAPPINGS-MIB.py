# SNMP MIB module (CISCO-FIREPOWER-AP-MAPPINGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-MAPPINGS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:13 2025
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
 ciscoFirepowerApMIB) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIB")

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

cfprApMappingsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApMappingsMoContainmentTable_Object = MibTable
cfprApMappingsMoContainmentTable = _CfprApMappingsMoContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cfprApMappingsMoContainmentTable.setStatus("current")
_CfprApMappingsMoContainmentEntry_Object = MibTableRow
cfprApMappingsMoContainmentEntry = _CfprApMappingsMoContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 1, 1)
)
cfprApMappingsMoContainmentEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MAPPINGS-MIB", "cfprApMappingsMoContainmentParentInstanceId"),
    (0, "CISCO-FIREPOWER-AP-MAPPINGS-MIB", "cfprApMappingsMoContainmentChildInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMappingsMoContainmentEntry.setStatus("current")
_CfprApMappingsMoContainmentParentInstanceId_Type = CfprApManagedObjectId
_CfprApMappingsMoContainmentParentInstanceId_Object = MibTableColumn
cfprApMappingsMoContainmentParentInstanceId = _CfprApMappingsMoContainmentParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 1, 1, 1),
    _CfprApMappingsMoContainmentParentInstanceId_Type()
)
cfprApMappingsMoContainmentParentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMappingsMoContainmentParentInstanceId.setStatus("current")
_CfprApMappingsMoContainmentChildInstanceId_Type = CfprApManagedObjectId
_CfprApMappingsMoContainmentChildInstanceId_Object = MibTableColumn
cfprApMappingsMoContainmentChildInstanceId = _CfprApMappingsMoContainmentChildInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 1, 1, 2),
    _CfprApMappingsMoContainmentChildInstanceId_Type()
)
cfprApMappingsMoContainmentChildInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMappingsMoContainmentChildInstanceId.setStatus("current")
_CfprApMappingsMoContainmentParentDn_Type = CfprApManagedObjectDn
_CfprApMappingsMoContainmentParentDn_Object = MibTableColumn
cfprApMappingsMoContainmentParentDn = _CfprApMappingsMoContainmentParentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 1, 1, 3),
    _CfprApMappingsMoContainmentParentDn_Type()
)
cfprApMappingsMoContainmentParentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMappingsMoContainmentParentDn.setStatus("current")
_CfprApMappingsMoContainmentChildDn_Type = CfprApManagedObjectDn
_CfprApMappingsMoContainmentChildDn_Object = MibTableColumn
cfprApMappingsMoContainmentChildDn = _CfprApMappingsMoContainmentChildDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 1, 1, 4),
    _CfprApMappingsMoContainmentChildDn_Type()
)
cfprApMappingsMoContainmentChildDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMappingsMoContainmentChildDn.setStatus("current")
_CfprApMappingsMoInverseContainmentTable_Object = MibTable
cfprApMappingsMoInverseContainmentTable = _CfprApMappingsMoInverseContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cfprApMappingsMoInverseContainmentTable.setStatus("current")
_CfprApMappingsMoInverseContainmentEntry_Object = MibTableRow
cfprApMappingsMoInverseContainmentEntry = _CfprApMappingsMoInverseContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 2, 1)
)
cfprApMappingsMoInverseContainmentEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MAPPINGS-MIB", "cfprApMappingsMoInverseContainmentChildInstanceId"),
    (0, "CISCO-FIREPOWER-AP-MAPPINGS-MIB", "cfprApMappingsMoInverseContainmentParentInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMappingsMoInverseContainmentEntry.setStatus("current")
_CfprApMappingsMoInverseContainmentChildInstanceId_Type = CfprApManagedObjectId
_CfprApMappingsMoInverseContainmentChildInstanceId_Object = MibTableColumn
cfprApMappingsMoInverseContainmentChildInstanceId = _CfprApMappingsMoInverseContainmentChildInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 2, 1, 1),
    _CfprApMappingsMoInverseContainmentChildInstanceId_Type()
)
cfprApMappingsMoInverseContainmentChildInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMappingsMoInverseContainmentChildInstanceId.setStatus("current")
_CfprApMappingsMoInverseContainmentParentInstanceId_Type = CfprApManagedObjectId
_CfprApMappingsMoInverseContainmentParentInstanceId_Object = MibTableColumn
cfprApMappingsMoInverseContainmentParentInstanceId = _CfprApMappingsMoInverseContainmentParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 2, 1, 2),
    _CfprApMappingsMoInverseContainmentParentInstanceId_Type()
)
cfprApMappingsMoInverseContainmentParentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMappingsMoInverseContainmentParentInstanceId.setStatus("current")
_CfprApMappingsMoInverseContainmentParentDn_Type = CfprApManagedObjectDn
_CfprApMappingsMoInverseContainmentParentDn_Object = MibTableColumn
cfprApMappingsMoInverseContainmentParentDn = _CfprApMappingsMoInverseContainmentParentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 2, 1, 3),
    _CfprApMappingsMoInverseContainmentParentDn_Type()
)
cfprApMappingsMoInverseContainmentParentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMappingsMoInverseContainmentParentDn.setStatus("current")
_CfprApMappingsMoInverseContainmentChildDn_Type = CfprApManagedObjectDn
_CfprApMappingsMoInverseContainmentChildDn_Object = MibTableColumn
cfprApMappingsMoInverseContainmentChildDn = _CfprApMappingsMoInverseContainmentChildDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 2, 1, 4),
    _CfprApMappingsMoInverseContainmentChildDn_Type()
)
cfprApMappingsMoInverseContainmentChildDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMappingsMoInverseContainmentChildDn.setStatus("current")
_CfprApMappingsDnToOidTable_Object = MibTable
cfprApMappingsDnToOidTable = _CfprApMappingsDnToOidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cfprApMappingsDnToOidTable.setStatus("current")
_CfprApMappingsDnToOidEntry_Object = MibTableRow
cfprApMappingsDnToOidEntry = _CfprApMappingsDnToOidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 3, 1)
)
cfprApMappingsDnToOidEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MAPPINGS-MIB", "cfprApMappingsDnToOidDn"),
)
if mibBuilder.loadTexts:
    cfprApMappingsDnToOidEntry.setStatus("current")
_CfprApMappingsDnToOidDn_Type = CfprApManagedObjectDn
_CfprApMappingsDnToOidDn_Object = MibTableColumn
cfprApMappingsDnToOidDn = _CfprApMappingsDnToOidDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 3, 1, 1),
    _CfprApMappingsDnToOidDn_Type()
)
cfprApMappingsDnToOidDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMappingsDnToOidDn.setStatus("current")
_CfprApMappingsDnToOidOid_Type = RowPointer
_CfprApMappingsDnToOidOid_Object = MibTableColumn
cfprApMappingsDnToOidOid = _CfprApMappingsDnToOidOid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 3, 3, 1, 2),
    _CfprApMappingsDnToOidOid_Type()
)
cfprApMappingsDnToOidOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMappingsDnToOidOid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-MAPPINGS-MIB",
    **{"cfprApMappingsObjects": cfprApMappingsObjects,
       "cfprApMappingsMoContainmentTable": cfprApMappingsMoContainmentTable,
       "cfprApMappingsMoContainmentEntry": cfprApMappingsMoContainmentEntry,
       "cfprApMappingsMoContainmentParentInstanceId": cfprApMappingsMoContainmentParentInstanceId,
       "cfprApMappingsMoContainmentChildInstanceId": cfprApMappingsMoContainmentChildInstanceId,
       "cfprApMappingsMoContainmentParentDn": cfprApMappingsMoContainmentParentDn,
       "cfprApMappingsMoContainmentChildDn": cfprApMappingsMoContainmentChildDn,
       "cfprApMappingsMoInverseContainmentTable": cfprApMappingsMoInverseContainmentTable,
       "cfprApMappingsMoInverseContainmentEntry": cfprApMappingsMoInverseContainmentEntry,
       "cfprApMappingsMoInverseContainmentChildInstanceId": cfprApMappingsMoInverseContainmentChildInstanceId,
       "cfprApMappingsMoInverseContainmentParentInstanceId": cfprApMappingsMoInverseContainmentParentInstanceId,
       "cfprApMappingsMoInverseContainmentParentDn": cfprApMappingsMoInverseContainmentParentDn,
       "cfprApMappingsMoInverseContainmentChildDn": cfprApMappingsMoInverseContainmentChildDn,
       "cfprApMappingsDnToOidTable": cfprApMappingsDnToOidTable,
       "cfprApMappingsDnToOidEntry": cfprApMappingsDnToOidEntry,
       "cfprApMappingsDnToOidDn": cfprApMappingsDnToOidDn,
       "cfprApMappingsDnToOidOid": cfprApMappingsDnToOidOid}
)
