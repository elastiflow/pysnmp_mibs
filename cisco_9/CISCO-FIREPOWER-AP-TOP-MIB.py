# SNMP MIB module (CISCO-FIREPOWER-AP-TOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-TOP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:39 2025
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

(CfprApTopInfoPolicyState,
 CfprApTopMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApTopInfoPolicyState",
    "CfprApTopMode")

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

cfprApTopObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApTopInfoPolicyTable_Object = MibTable
cfprApTopInfoPolicyTable = _CfprApTopInfoPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 1)
)
if mibBuilder.loadTexts:
    cfprApTopInfoPolicyTable.setStatus("current")
_CfprApTopInfoPolicyEntry_Object = MibTableRow
cfprApTopInfoPolicyEntry = _CfprApTopInfoPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 1, 1)
)
cfprApTopInfoPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TOP-MIB", "cfprApTopInfoPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTopInfoPolicyEntry.setStatus("current")
_CfprApTopInfoPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApTopInfoPolicyInstanceId_Object = MibTableColumn
cfprApTopInfoPolicyInstanceId = _CfprApTopInfoPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 1, 1, 1),
    _CfprApTopInfoPolicyInstanceId_Type()
)
cfprApTopInfoPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTopInfoPolicyInstanceId.setStatus("current")
_CfprApTopInfoPolicyDn_Type = CfprApManagedObjectDn
_CfprApTopInfoPolicyDn_Object = MibTableColumn
cfprApTopInfoPolicyDn = _CfprApTopInfoPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 1, 1, 2),
    _CfprApTopInfoPolicyDn_Type()
)
cfprApTopInfoPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopInfoPolicyDn.setStatus("current")
_CfprApTopInfoPolicyRn_Type = SnmpAdminString
_CfprApTopInfoPolicyRn_Object = MibTableColumn
cfprApTopInfoPolicyRn = _CfprApTopInfoPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 1, 1, 3),
    _CfprApTopInfoPolicyRn_Type()
)
cfprApTopInfoPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopInfoPolicyRn.setStatus("current")
_CfprApTopInfoPolicyState_Type = CfprApTopInfoPolicyState
_CfprApTopInfoPolicyState_Object = MibTableColumn
cfprApTopInfoPolicyState = _CfprApTopInfoPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 1, 1, 4),
    _CfprApTopInfoPolicyState_Type()
)
cfprApTopInfoPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopInfoPolicyState.setStatus("current")
_CfprApTopMetaInfTable_Object = MibTable
cfprApTopMetaInfTable = _CfprApTopMetaInfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2)
)
if mibBuilder.loadTexts:
    cfprApTopMetaInfTable.setStatus("current")
_CfprApTopMetaInfEntry_Object = MibTableRow
cfprApTopMetaInfEntry = _CfprApTopMetaInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2, 1)
)
cfprApTopMetaInfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TOP-MIB", "cfprApTopMetaInfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTopMetaInfEntry.setStatus("current")
_CfprApTopMetaInfInstanceId_Type = CfprApManagedObjectId
_CfprApTopMetaInfInstanceId_Object = MibTableColumn
cfprApTopMetaInfInstanceId = _CfprApTopMetaInfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2, 1, 1),
    _CfprApTopMetaInfInstanceId_Type()
)
cfprApTopMetaInfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTopMetaInfInstanceId.setStatus("current")
_CfprApTopMetaInfDn_Type = CfprApManagedObjectDn
_CfprApTopMetaInfDn_Object = MibTableColumn
cfprApTopMetaInfDn = _CfprApTopMetaInfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2, 1, 2),
    _CfprApTopMetaInfDn_Type()
)
cfprApTopMetaInfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopMetaInfDn.setStatus("current")
_CfprApTopMetaInfRn_Type = SnmpAdminString
_CfprApTopMetaInfRn_Object = MibTableColumn
cfprApTopMetaInfRn = _CfprApTopMetaInfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2, 1, 3),
    _CfprApTopMetaInfRn_Type()
)
cfprApTopMetaInfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopMetaInfRn.setStatus("current")
_CfprApTopMetaInfEcode_Type = SnmpAdminString
_CfprApTopMetaInfEcode_Object = MibTableColumn
cfprApTopMetaInfEcode = _CfprApTopMetaInfEcode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2, 1, 4),
    _CfprApTopMetaInfEcode_Type()
)
cfprApTopMetaInfEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopMetaInfEcode.setStatus("current")
_CfprApTopMetaInfName_Type = SnmpAdminString
_CfprApTopMetaInfName_Object = MibTableColumn
cfprApTopMetaInfName = _CfprApTopMetaInfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 2, 1, 5),
    _CfprApTopMetaInfName_Type()
)
cfprApTopMetaInfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopMetaInfName.setStatus("current")
_CfprApTopRootTable_Object = MibTable
cfprApTopRootTable = _CfprApTopRootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 3)
)
if mibBuilder.loadTexts:
    cfprApTopRootTable.setStatus("current")
_CfprApTopRootEntry_Object = MibTableRow
cfprApTopRootEntry = _CfprApTopRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 3, 1)
)
cfprApTopRootEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TOP-MIB", "cfprApTopRootInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTopRootEntry.setStatus("current")
_CfprApTopRootInstanceId_Type = CfprApManagedObjectId
_CfprApTopRootInstanceId_Object = MibTableColumn
cfprApTopRootInstanceId = _CfprApTopRootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 3, 1, 1),
    _CfprApTopRootInstanceId_Type()
)
cfprApTopRootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTopRootInstanceId.setStatus("current")
_CfprApTopRootDn_Type = CfprApManagedObjectDn
_CfprApTopRootDn_Object = MibTableColumn
cfprApTopRootDn = _CfprApTopRootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 3, 1, 2),
    _CfprApTopRootDn_Type()
)
cfprApTopRootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopRootDn.setStatus("current")
_CfprApTopRootRn_Type = SnmpAdminString
_CfprApTopRootRn_Object = MibTableColumn
cfprApTopRootRn = _CfprApTopRootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 3, 1, 3),
    _CfprApTopRootRn_Type()
)
cfprApTopRootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopRootRn.setStatus("current")
_CfprApTopSysDefaultsTable_Object = MibTable
cfprApTopSysDefaultsTable = _CfprApTopSysDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 4)
)
if mibBuilder.loadTexts:
    cfprApTopSysDefaultsTable.setStatus("current")
_CfprApTopSysDefaultsEntry_Object = MibTableRow
cfprApTopSysDefaultsEntry = _CfprApTopSysDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 4, 1)
)
cfprApTopSysDefaultsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TOP-MIB", "cfprApTopSysDefaultsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTopSysDefaultsEntry.setStatus("current")
_CfprApTopSysDefaultsInstanceId_Type = CfprApManagedObjectId
_CfprApTopSysDefaultsInstanceId_Object = MibTableColumn
cfprApTopSysDefaultsInstanceId = _CfprApTopSysDefaultsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 4, 1, 1),
    _CfprApTopSysDefaultsInstanceId_Type()
)
cfprApTopSysDefaultsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTopSysDefaultsInstanceId.setStatus("current")
_CfprApTopSysDefaultsDn_Type = CfprApManagedObjectDn
_CfprApTopSysDefaultsDn_Object = MibTableColumn
cfprApTopSysDefaultsDn = _CfprApTopSysDefaultsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 4, 1, 2),
    _CfprApTopSysDefaultsDn_Type()
)
cfprApTopSysDefaultsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSysDefaultsDn.setStatus("current")
_CfprApTopSysDefaultsRn_Type = SnmpAdminString
_CfprApTopSysDefaultsRn_Object = MibTableColumn
cfprApTopSysDefaultsRn = _CfprApTopSysDefaultsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 4, 1, 3),
    _CfprApTopSysDefaultsRn_Type()
)
cfprApTopSysDefaultsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSysDefaultsRn.setStatus("current")
_CfprApTopSystemTable_Object = MibTable
cfprApTopSystemTable = _CfprApTopSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5)
)
if mibBuilder.loadTexts:
    cfprApTopSystemTable.setStatus("current")
_CfprApTopSystemEntry_Object = MibTableRow
cfprApTopSystemEntry = _CfprApTopSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1)
)
cfprApTopSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-TOP-MIB", "cfprApTopSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApTopSystemEntry.setStatus("current")
_CfprApTopSystemInstanceId_Type = CfprApManagedObjectId
_CfprApTopSystemInstanceId_Object = MibTableColumn
cfprApTopSystemInstanceId = _CfprApTopSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 1),
    _CfprApTopSystemInstanceId_Type()
)
cfprApTopSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApTopSystemInstanceId.setStatus("current")
_CfprApTopSystemDn_Type = CfprApManagedObjectDn
_CfprApTopSystemDn_Object = MibTableColumn
cfprApTopSystemDn = _CfprApTopSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 2),
    _CfprApTopSystemDn_Type()
)
cfprApTopSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemDn.setStatus("current")
_CfprApTopSystemRn_Type = SnmpAdminString
_CfprApTopSystemRn_Object = MibTableColumn
cfprApTopSystemRn = _CfprApTopSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 3),
    _CfprApTopSystemRn_Type()
)
cfprApTopSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemRn.setStatus("current")
_CfprApTopSystemAddress_Type = InetAddressIPv4
_CfprApTopSystemAddress_Object = MibTableColumn
cfprApTopSystemAddress = _CfprApTopSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 4),
    _CfprApTopSystemAddress_Type()
)
cfprApTopSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemAddress.setStatus("current")
_CfprApTopSystemCurrentTime_Type = DateAndTime
_CfprApTopSystemCurrentTime_Object = MibTableColumn
cfprApTopSystemCurrentTime = _CfprApTopSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 5),
    _CfprApTopSystemCurrentTime_Type()
)
cfprApTopSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemCurrentTime.setStatus("current")
_CfprApTopSystemDescr_Type = SnmpAdminString
_CfprApTopSystemDescr_Object = MibTableColumn
cfprApTopSystemDescr = _CfprApTopSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 6),
    _CfprApTopSystemDescr_Type()
)
cfprApTopSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemDescr.setStatus("current")
_CfprApTopSystemIpv6Addr_Type = InetAddressIPv6
_CfprApTopSystemIpv6Addr_Object = MibTableColumn
cfprApTopSystemIpv6Addr = _CfprApTopSystemIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 7),
    _CfprApTopSystemIpv6Addr_Type()
)
cfprApTopSystemIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemIpv6Addr.setStatus("current")
_CfprApTopSystemMode_Type = CfprApTopMode
_CfprApTopSystemMode_Object = MibTableColumn
cfprApTopSystemMode = _CfprApTopSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 8),
    _CfprApTopSystemMode_Type()
)
cfprApTopSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemMode.setStatus("current")
_CfprApTopSystemName_Type = SnmpAdminString
_CfprApTopSystemName_Object = MibTableColumn
cfprApTopSystemName = _CfprApTopSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 9),
    _CfprApTopSystemName_Type()
)
cfprApTopSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemName.setStatus("current")
_CfprApTopSystemOwner_Type = SnmpAdminString
_CfprApTopSystemOwner_Object = MibTableColumn
cfprApTopSystemOwner = _CfprApTopSystemOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 10),
    _CfprApTopSystemOwner_Type()
)
cfprApTopSystemOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemOwner.setStatus("current")
_CfprApTopSystemSite_Type = SnmpAdminString
_CfprApTopSystemSite_Object = MibTableColumn
cfprApTopSystemSite = _CfprApTopSystemSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 11),
    _CfprApTopSystemSite_Type()
)
cfprApTopSystemSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemSite.setStatus("current")
_CfprApTopSystemSystemUpTime_Type = TimeIntervalSec
_CfprApTopSystemSystemUpTime_Object = MibTableColumn
cfprApTopSystemSystemUpTime = _CfprApTopSystemSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 78, 5, 1, 12),
    _CfprApTopSystemSystemUpTime_Type()
)
cfprApTopSystemSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApTopSystemSystemUpTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-TOP-MIB",
    **{"cfprApTopObjects": cfprApTopObjects,
       "cfprApTopInfoPolicyTable": cfprApTopInfoPolicyTable,
       "cfprApTopInfoPolicyEntry": cfprApTopInfoPolicyEntry,
       "cfprApTopInfoPolicyInstanceId": cfprApTopInfoPolicyInstanceId,
       "cfprApTopInfoPolicyDn": cfprApTopInfoPolicyDn,
       "cfprApTopInfoPolicyRn": cfprApTopInfoPolicyRn,
       "cfprApTopInfoPolicyState": cfprApTopInfoPolicyState,
       "cfprApTopMetaInfTable": cfprApTopMetaInfTable,
       "cfprApTopMetaInfEntry": cfprApTopMetaInfEntry,
       "cfprApTopMetaInfInstanceId": cfprApTopMetaInfInstanceId,
       "cfprApTopMetaInfDn": cfprApTopMetaInfDn,
       "cfprApTopMetaInfRn": cfprApTopMetaInfRn,
       "cfprApTopMetaInfEcode": cfprApTopMetaInfEcode,
       "cfprApTopMetaInfName": cfprApTopMetaInfName,
       "cfprApTopRootTable": cfprApTopRootTable,
       "cfprApTopRootEntry": cfprApTopRootEntry,
       "cfprApTopRootInstanceId": cfprApTopRootInstanceId,
       "cfprApTopRootDn": cfprApTopRootDn,
       "cfprApTopRootRn": cfprApTopRootRn,
       "cfprApTopSysDefaultsTable": cfprApTopSysDefaultsTable,
       "cfprApTopSysDefaultsEntry": cfprApTopSysDefaultsEntry,
       "cfprApTopSysDefaultsInstanceId": cfprApTopSysDefaultsInstanceId,
       "cfprApTopSysDefaultsDn": cfprApTopSysDefaultsDn,
       "cfprApTopSysDefaultsRn": cfprApTopSysDefaultsRn,
       "cfprApTopSystemTable": cfprApTopSystemTable,
       "cfprApTopSystemEntry": cfprApTopSystemEntry,
       "cfprApTopSystemInstanceId": cfprApTopSystemInstanceId,
       "cfprApTopSystemDn": cfprApTopSystemDn,
       "cfprApTopSystemRn": cfprApTopSystemRn,
       "cfprApTopSystemAddress": cfprApTopSystemAddress,
       "cfprApTopSystemCurrentTime": cfprApTopSystemCurrentTime,
       "cfprApTopSystemDescr": cfprApTopSystemDescr,
       "cfprApTopSystemIpv6Addr": cfprApTopSystemIpv6Addr,
       "cfprApTopSystemMode": cfprApTopSystemMode,
       "cfprApTopSystemName": cfprApTopSystemName,
       "cfprApTopSystemOwner": cfprApTopSystemOwner,
       "cfprApTopSystemSite": cfprApTopSystemSite,
       "cfprApTopSystemSystemUpTime": cfprApTopSystemSystemUpTime}
)
