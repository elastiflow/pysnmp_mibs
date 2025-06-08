# SNMP MIB module (CISCO-FIREPOWER-VERSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-VERSION-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:13 2025
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

cfprVersionObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprVersionApplicationTable_Object = MibTable
cfprVersionApplicationTable = _CfprVersionApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1)
)
if mibBuilder.loadTexts:
    cfprVersionApplicationTable.setStatus("current")
_CfprVersionApplicationEntry_Object = MibTableRow
cfprVersionApplicationEntry = _CfprVersionApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1)
)
cfprVersionApplicationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VERSION-MIB", "cfprVersionApplicationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVersionApplicationEntry.setStatus("current")
_CfprVersionApplicationInstanceId_Type = CfprManagedObjectId
_CfprVersionApplicationInstanceId_Object = MibTableColumn
cfprVersionApplicationInstanceId = _CfprVersionApplicationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1, 1),
    _CfprVersionApplicationInstanceId_Type()
)
cfprVersionApplicationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVersionApplicationInstanceId.setStatus("current")
_CfprVersionApplicationDn_Type = CfprManagedObjectDn
_CfprVersionApplicationDn_Object = MibTableColumn
cfprVersionApplicationDn = _CfprVersionApplicationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1, 2),
    _CfprVersionApplicationDn_Type()
)
cfprVersionApplicationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionApplicationDn.setStatus("current")
_CfprVersionApplicationRn_Type = SnmpAdminString
_CfprVersionApplicationRn_Object = MibTableColumn
cfprVersionApplicationRn = _CfprVersionApplicationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1, 3),
    _CfprVersionApplicationRn_Type()
)
cfprVersionApplicationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionApplicationRn.setStatus("current")
_CfprVersionApplicationDetail_Type = SnmpAdminString
_CfprVersionApplicationDetail_Object = MibTableColumn
cfprVersionApplicationDetail = _CfprVersionApplicationDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1, 4),
    _CfprVersionApplicationDetail_Type()
)
cfprVersionApplicationDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionApplicationDetail.setStatus("current")
_CfprVersionApplicationTime_Type = SnmpAdminString
_CfprVersionApplicationTime_Object = MibTableColumn
cfprVersionApplicationTime = _CfprVersionApplicationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1, 5),
    _CfprVersionApplicationTime_Type()
)
cfprVersionApplicationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionApplicationTime.setStatus("current")
_CfprVersionApplicationVersion_Type = SnmpAdminString
_CfprVersionApplicationVersion_Object = MibTableColumn
cfprVersionApplicationVersion = _CfprVersionApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 1, 1, 6),
    _CfprVersionApplicationVersion_Type()
)
cfprVersionApplicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionApplicationVersion.setStatus("current")
_CfprVersionEpTable_Object = MibTable
cfprVersionEpTable = _CfprVersionEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 2)
)
if mibBuilder.loadTexts:
    cfprVersionEpTable.setStatus("current")
_CfprVersionEpEntry_Object = MibTableRow
cfprVersionEpEntry = _CfprVersionEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 2, 1)
)
cfprVersionEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VERSION-MIB", "cfprVersionEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVersionEpEntry.setStatus("current")
_CfprVersionEpInstanceId_Type = CfprManagedObjectId
_CfprVersionEpInstanceId_Object = MibTableColumn
cfprVersionEpInstanceId = _CfprVersionEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 2, 1, 1),
    _CfprVersionEpInstanceId_Type()
)
cfprVersionEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVersionEpInstanceId.setStatus("current")
_CfprVersionEpDn_Type = CfprManagedObjectDn
_CfprVersionEpDn_Object = MibTableColumn
cfprVersionEpDn = _CfprVersionEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 2, 1, 2),
    _CfprVersionEpDn_Type()
)
cfprVersionEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionEpDn.setStatus("current")
_CfprVersionEpRn_Type = SnmpAdminString
_CfprVersionEpRn_Object = MibTableColumn
cfprVersionEpRn = _CfprVersionEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 81, 2, 1, 3),
    _CfprVersionEpRn_Type()
)
cfprVersionEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVersionEpRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-VERSION-MIB",
    **{"cfprVersionObjects": cfprVersionObjects,
       "cfprVersionApplicationTable": cfprVersionApplicationTable,
       "cfprVersionApplicationEntry": cfprVersionApplicationEntry,
       "cfprVersionApplicationInstanceId": cfprVersionApplicationInstanceId,
       "cfprVersionApplicationDn": cfprVersionApplicationDn,
       "cfprVersionApplicationRn": cfprVersionApplicationRn,
       "cfprVersionApplicationDetail": cfprVersionApplicationDetail,
       "cfprVersionApplicationTime": cfprVersionApplicationTime,
       "cfprVersionApplicationVersion": cfprVersionApplicationVersion,
       "cfprVersionEpTable": cfprVersionEpTable,
       "cfprVersionEpEntry": cfprVersionEpEntry,
       "cfprVersionEpInstanceId": cfprVersionEpInstanceId,
       "cfprVersionEpDn": cfprVersionEpDn,
       "cfprVersionEpRn": cfprVersionEpRn}
)
