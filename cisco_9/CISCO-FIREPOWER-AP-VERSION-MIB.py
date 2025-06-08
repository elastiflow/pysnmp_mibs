# SNMP MIB module (CISCO-FIREPOWER-AP-VERSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-VERSION-MIB.mib
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

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

cfprApVersionObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApVersionApplicationTable_Object = MibTable
cfprApVersionApplicationTable = _CfprApVersionApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1)
)
if mibBuilder.loadTexts:
    cfprApVersionApplicationTable.setStatus("current")
_CfprApVersionApplicationEntry_Object = MibTableRow
cfprApVersionApplicationEntry = _CfprApVersionApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1)
)
cfprApVersionApplicationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VERSION-MIB", "cfprApVersionApplicationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVersionApplicationEntry.setStatus("current")
_CfprApVersionApplicationInstanceId_Type = CfprApManagedObjectId
_CfprApVersionApplicationInstanceId_Object = MibTableColumn
cfprApVersionApplicationInstanceId = _CfprApVersionApplicationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1, 1),
    _CfprApVersionApplicationInstanceId_Type()
)
cfprApVersionApplicationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVersionApplicationInstanceId.setStatus("current")
_CfprApVersionApplicationDn_Type = CfprApManagedObjectDn
_CfprApVersionApplicationDn_Object = MibTableColumn
cfprApVersionApplicationDn = _CfprApVersionApplicationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1, 2),
    _CfprApVersionApplicationDn_Type()
)
cfprApVersionApplicationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionApplicationDn.setStatus("current")
_CfprApVersionApplicationRn_Type = SnmpAdminString
_CfprApVersionApplicationRn_Object = MibTableColumn
cfprApVersionApplicationRn = _CfprApVersionApplicationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1, 3),
    _CfprApVersionApplicationRn_Type()
)
cfprApVersionApplicationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionApplicationRn.setStatus("current")
_CfprApVersionApplicationDetail_Type = SnmpAdminString
_CfprApVersionApplicationDetail_Object = MibTableColumn
cfprApVersionApplicationDetail = _CfprApVersionApplicationDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1, 4),
    _CfprApVersionApplicationDetail_Type()
)
cfprApVersionApplicationDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionApplicationDetail.setStatus("current")
_CfprApVersionApplicationTime_Type = SnmpAdminString
_CfprApVersionApplicationTime_Object = MibTableColumn
cfprApVersionApplicationTime = _CfprApVersionApplicationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1, 5),
    _CfprApVersionApplicationTime_Type()
)
cfprApVersionApplicationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionApplicationTime.setStatus("current")
_CfprApVersionApplicationVersion_Type = SnmpAdminString
_CfprApVersionApplicationVersion_Object = MibTableColumn
cfprApVersionApplicationVersion = _CfprApVersionApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 1, 1, 6),
    _CfprApVersionApplicationVersion_Type()
)
cfprApVersionApplicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionApplicationVersion.setStatus("current")
_CfprApVersionEpTable_Object = MibTable
cfprApVersionEpTable = _CfprApVersionEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 2)
)
if mibBuilder.loadTexts:
    cfprApVersionEpTable.setStatus("current")
_CfprApVersionEpEntry_Object = MibTableRow
cfprApVersionEpEntry = _CfprApVersionEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 2, 1)
)
cfprApVersionEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VERSION-MIB", "cfprApVersionEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVersionEpEntry.setStatus("current")
_CfprApVersionEpInstanceId_Type = CfprApManagedObjectId
_CfprApVersionEpInstanceId_Object = MibTableColumn
cfprApVersionEpInstanceId = _CfprApVersionEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 2, 1, 1),
    _CfprApVersionEpInstanceId_Type()
)
cfprApVersionEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVersionEpInstanceId.setStatus("current")
_CfprApVersionEpDn_Type = CfprApManagedObjectDn
_CfprApVersionEpDn_Object = MibTableColumn
cfprApVersionEpDn = _CfprApVersionEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 2, 1, 2),
    _CfprApVersionEpDn_Type()
)
cfprApVersionEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionEpDn.setStatus("current")
_CfprApVersionEpRn_Type = SnmpAdminString
_CfprApVersionEpRn_Object = MibTableColumn
cfprApVersionEpRn = _CfprApVersionEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 81, 2, 1, 3),
    _CfprApVersionEpRn_Type()
)
cfprApVersionEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVersionEpRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-VERSION-MIB",
    **{"cfprApVersionObjects": cfprApVersionObjects,
       "cfprApVersionApplicationTable": cfprApVersionApplicationTable,
       "cfprApVersionApplicationEntry": cfprApVersionApplicationEntry,
       "cfprApVersionApplicationInstanceId": cfprApVersionApplicationInstanceId,
       "cfprApVersionApplicationDn": cfprApVersionApplicationDn,
       "cfprApVersionApplicationRn": cfprApVersionApplicationRn,
       "cfprApVersionApplicationDetail": cfprApVersionApplicationDetail,
       "cfprApVersionApplicationTime": cfprApVersionApplicationTime,
       "cfprApVersionApplicationVersion": cfprApVersionApplicationVersion,
       "cfprApVersionEpTable": cfprApVersionEpTable,
       "cfprApVersionEpEntry": cfprApVersionEpEntry,
       "cfprApVersionEpInstanceId": cfprApVersionEpInstanceId,
       "cfprApVersionEpDn": cfprApVersionEpDn,
       "cfprApVersionEpRn": cfprApVersionEpRn}
)
