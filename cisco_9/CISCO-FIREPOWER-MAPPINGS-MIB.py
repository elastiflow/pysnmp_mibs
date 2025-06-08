# SNMP MIB module (CISCO-FIREPOWER-MAPPINGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-MAPPINGS-MIB.mib
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
 ciscoFirepowerMIB) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIB")

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

cfprMappingsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprMappingsMoContainmentTable_Object = MibTable
cfprMappingsMoContainmentTable = _CfprMappingsMoContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 1)
)
if mibBuilder.loadTexts:
    cfprMappingsMoContainmentTable.setStatus("current")
_CfprMappingsMoContainmentEntry_Object = MibTableRow
cfprMappingsMoContainmentEntry = _CfprMappingsMoContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 1, 1)
)
cfprMappingsMoContainmentEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MAPPINGS-MIB", "cfprMappingsMoContainmentParentInstanceId"),
    (0, "CISCO-FIREPOWER-MAPPINGS-MIB", "cfprMappingsMoContainmentChildInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMappingsMoContainmentEntry.setStatus("current")
_CfprMappingsMoContainmentParentInstanceId_Type = CfprManagedObjectId
_CfprMappingsMoContainmentParentInstanceId_Object = MibTableColumn
cfprMappingsMoContainmentParentInstanceId = _CfprMappingsMoContainmentParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 1, 1, 1),
    _CfprMappingsMoContainmentParentInstanceId_Type()
)
cfprMappingsMoContainmentParentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMappingsMoContainmentParentInstanceId.setStatus("current")
_CfprMappingsMoContainmentChildInstanceId_Type = CfprManagedObjectId
_CfprMappingsMoContainmentChildInstanceId_Object = MibTableColumn
cfprMappingsMoContainmentChildInstanceId = _CfprMappingsMoContainmentChildInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 1, 1, 2),
    _CfprMappingsMoContainmentChildInstanceId_Type()
)
cfprMappingsMoContainmentChildInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMappingsMoContainmentChildInstanceId.setStatus("current")
_CfprMappingsMoContainmentParentDn_Type = CfprManagedObjectDn
_CfprMappingsMoContainmentParentDn_Object = MibTableColumn
cfprMappingsMoContainmentParentDn = _CfprMappingsMoContainmentParentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 1, 1, 3),
    _CfprMappingsMoContainmentParentDn_Type()
)
cfprMappingsMoContainmentParentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMappingsMoContainmentParentDn.setStatus("current")
_CfprMappingsMoContainmentChildDn_Type = CfprManagedObjectDn
_CfprMappingsMoContainmentChildDn_Object = MibTableColumn
cfprMappingsMoContainmentChildDn = _CfprMappingsMoContainmentChildDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 1, 1, 4),
    _CfprMappingsMoContainmentChildDn_Type()
)
cfprMappingsMoContainmentChildDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMappingsMoContainmentChildDn.setStatus("current")
_CfprMappingsMoInverseContainmentTable_Object = MibTable
cfprMappingsMoInverseContainmentTable = _CfprMappingsMoInverseContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 2)
)
if mibBuilder.loadTexts:
    cfprMappingsMoInverseContainmentTable.setStatus("current")
_CfprMappingsMoInverseContainmentEntry_Object = MibTableRow
cfprMappingsMoInverseContainmentEntry = _CfprMappingsMoInverseContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 2, 1)
)
cfprMappingsMoInverseContainmentEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MAPPINGS-MIB", "cfprMappingsMoInverseContainmentChildInstanceId"),
    (0, "CISCO-FIREPOWER-MAPPINGS-MIB", "cfprMappingsMoInverseContainmentParentInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMappingsMoInverseContainmentEntry.setStatus("current")
_CfprMappingsMoInverseContainmentChildInstanceId_Type = CfprManagedObjectId
_CfprMappingsMoInverseContainmentChildInstanceId_Object = MibTableColumn
cfprMappingsMoInverseContainmentChildInstanceId = _CfprMappingsMoInverseContainmentChildInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 2, 1, 1),
    _CfprMappingsMoInverseContainmentChildInstanceId_Type()
)
cfprMappingsMoInverseContainmentChildInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMappingsMoInverseContainmentChildInstanceId.setStatus("current")
_CfprMappingsMoInverseContainmentParentInstanceId_Type = CfprManagedObjectId
_CfprMappingsMoInverseContainmentParentInstanceId_Object = MibTableColumn
cfprMappingsMoInverseContainmentParentInstanceId = _CfprMappingsMoInverseContainmentParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 2, 1, 2),
    _CfprMappingsMoInverseContainmentParentInstanceId_Type()
)
cfprMappingsMoInverseContainmentParentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMappingsMoInverseContainmentParentInstanceId.setStatus("current")
_CfprMappingsMoInverseContainmentParentDn_Type = CfprManagedObjectDn
_CfprMappingsMoInverseContainmentParentDn_Object = MibTableColumn
cfprMappingsMoInverseContainmentParentDn = _CfprMappingsMoInverseContainmentParentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 2, 1, 3),
    _CfprMappingsMoInverseContainmentParentDn_Type()
)
cfprMappingsMoInverseContainmentParentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMappingsMoInverseContainmentParentDn.setStatus("current")
_CfprMappingsMoInverseContainmentChildDn_Type = CfprManagedObjectDn
_CfprMappingsMoInverseContainmentChildDn_Object = MibTableColumn
cfprMappingsMoInverseContainmentChildDn = _CfprMappingsMoInverseContainmentChildDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 2, 1, 4),
    _CfprMappingsMoInverseContainmentChildDn_Type()
)
cfprMappingsMoInverseContainmentChildDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMappingsMoInverseContainmentChildDn.setStatus("current")
_CfprMappingsDnToOidTable_Object = MibTable
cfprMappingsDnToOidTable = _CfprMappingsDnToOidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 3)
)
if mibBuilder.loadTexts:
    cfprMappingsDnToOidTable.setStatus("current")
_CfprMappingsDnToOidEntry_Object = MibTableRow
cfprMappingsDnToOidEntry = _CfprMappingsDnToOidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 3, 1)
)
cfprMappingsDnToOidEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MAPPINGS-MIB", "cfprMappingsDnToOidDn"),
)
if mibBuilder.loadTexts:
    cfprMappingsDnToOidEntry.setStatus("current")
_CfprMappingsDnToOidDn_Type = CfprManagedObjectDn
_CfprMappingsDnToOidDn_Object = MibTableColumn
cfprMappingsDnToOidDn = _CfprMappingsDnToOidDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 3, 1, 1),
    _CfprMappingsDnToOidDn_Type()
)
cfprMappingsDnToOidDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMappingsDnToOidDn.setStatus("current")
_CfprMappingsDnToOidOid_Type = RowPointer
_CfprMappingsDnToOidOid_Object = MibTableColumn
cfprMappingsDnToOidOid = _CfprMappingsDnToOidOid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 3, 3, 1, 2),
    _CfprMappingsDnToOidOid_Type()
)
cfprMappingsDnToOidOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMappingsDnToOidOid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-MAPPINGS-MIB",
    **{"cfprMappingsObjects": cfprMappingsObjects,
       "cfprMappingsMoContainmentTable": cfprMappingsMoContainmentTable,
       "cfprMappingsMoContainmentEntry": cfprMappingsMoContainmentEntry,
       "cfprMappingsMoContainmentParentInstanceId": cfprMappingsMoContainmentParentInstanceId,
       "cfprMappingsMoContainmentChildInstanceId": cfprMappingsMoContainmentChildInstanceId,
       "cfprMappingsMoContainmentParentDn": cfprMappingsMoContainmentParentDn,
       "cfprMappingsMoContainmentChildDn": cfprMappingsMoContainmentChildDn,
       "cfprMappingsMoInverseContainmentTable": cfprMappingsMoInverseContainmentTable,
       "cfprMappingsMoInverseContainmentEntry": cfprMappingsMoInverseContainmentEntry,
       "cfprMappingsMoInverseContainmentChildInstanceId": cfprMappingsMoInverseContainmentChildInstanceId,
       "cfprMappingsMoInverseContainmentParentInstanceId": cfprMappingsMoInverseContainmentParentInstanceId,
       "cfprMappingsMoInverseContainmentParentDn": cfprMappingsMoInverseContainmentParentDn,
       "cfprMappingsMoInverseContainmentChildDn": cfprMappingsMoInverseContainmentChildDn,
       "cfprMappingsDnToOidTable": cfprMappingsDnToOidTable,
       "cfprMappingsDnToOidEntry": cfprMappingsDnToOidEntry,
       "cfprMappingsDnToOidDn": cfprMappingsDnToOidDn,
       "cfprMappingsDnToOidOid": cfprMappingsDnToOidOid}
)
