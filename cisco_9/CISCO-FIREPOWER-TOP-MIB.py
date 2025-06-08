# SNMP MIB module (CISCO-FIREPOWER-TOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-TOP-MIB.mib
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

(CfprTopInfoPolicyState,
 CfprTopMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprTopInfoPolicyState",
    "CfprTopMode")

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

cfprTopObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprTopInfoPolicyTable_Object = MibTable
cfprTopInfoPolicyTable = _CfprTopInfoPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 1)
)
if mibBuilder.loadTexts:
    cfprTopInfoPolicyTable.setStatus("current")
_CfprTopInfoPolicyEntry_Object = MibTableRow
cfprTopInfoPolicyEntry = _CfprTopInfoPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 1, 1)
)
cfprTopInfoPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TOP-MIB", "cfprTopInfoPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTopInfoPolicyEntry.setStatus("current")
_CfprTopInfoPolicyInstanceId_Type = CfprManagedObjectId
_CfprTopInfoPolicyInstanceId_Object = MibTableColumn
cfprTopInfoPolicyInstanceId = _CfprTopInfoPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 1, 1, 1),
    _CfprTopInfoPolicyInstanceId_Type()
)
cfprTopInfoPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTopInfoPolicyInstanceId.setStatus("current")
_CfprTopInfoPolicyDn_Type = CfprManagedObjectDn
_CfprTopInfoPolicyDn_Object = MibTableColumn
cfprTopInfoPolicyDn = _CfprTopInfoPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 1, 1, 2),
    _CfprTopInfoPolicyDn_Type()
)
cfprTopInfoPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopInfoPolicyDn.setStatus("current")
_CfprTopInfoPolicyRn_Type = SnmpAdminString
_CfprTopInfoPolicyRn_Object = MibTableColumn
cfprTopInfoPolicyRn = _CfprTopInfoPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 1, 1, 3),
    _CfprTopInfoPolicyRn_Type()
)
cfprTopInfoPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopInfoPolicyRn.setStatus("current")
_CfprTopInfoPolicyState_Type = CfprTopInfoPolicyState
_CfprTopInfoPolicyState_Object = MibTableColumn
cfprTopInfoPolicyState = _CfprTopInfoPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 1, 1, 4),
    _CfprTopInfoPolicyState_Type()
)
cfprTopInfoPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopInfoPolicyState.setStatus("current")
_CfprTopMetaInfTable_Object = MibTable
cfprTopMetaInfTable = _CfprTopMetaInfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2)
)
if mibBuilder.loadTexts:
    cfprTopMetaInfTable.setStatus("current")
_CfprTopMetaInfEntry_Object = MibTableRow
cfprTopMetaInfEntry = _CfprTopMetaInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1)
)
cfprTopMetaInfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TOP-MIB", "cfprTopMetaInfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTopMetaInfEntry.setStatus("current")
_CfprTopMetaInfInstanceId_Type = CfprManagedObjectId
_CfprTopMetaInfInstanceId_Object = MibTableColumn
cfprTopMetaInfInstanceId = _CfprTopMetaInfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1, 1),
    _CfprTopMetaInfInstanceId_Type()
)
cfprTopMetaInfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTopMetaInfInstanceId.setStatus("current")
_CfprTopMetaInfDn_Type = CfprManagedObjectDn
_CfprTopMetaInfDn_Object = MibTableColumn
cfprTopMetaInfDn = _CfprTopMetaInfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1, 2),
    _CfprTopMetaInfDn_Type()
)
cfprTopMetaInfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopMetaInfDn.setStatus("current")
_CfprTopMetaInfRn_Type = SnmpAdminString
_CfprTopMetaInfRn_Object = MibTableColumn
cfprTopMetaInfRn = _CfprTopMetaInfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1, 3),
    _CfprTopMetaInfRn_Type()
)
cfprTopMetaInfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopMetaInfRn.setStatus("current")
_CfprTopMetaInfEcode_Type = SnmpAdminString
_CfprTopMetaInfEcode_Object = MibTableColumn
cfprTopMetaInfEcode = _CfprTopMetaInfEcode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1, 4),
    _CfprTopMetaInfEcode_Type()
)
cfprTopMetaInfEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopMetaInfEcode.setStatus("current")
_CfprTopMetaInfName_Type = SnmpAdminString
_CfprTopMetaInfName_Object = MibTableColumn
cfprTopMetaInfName = _CfprTopMetaInfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1, 5),
    _CfprTopMetaInfName_Type()
)
cfprTopMetaInfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopMetaInfName.setStatus("current")
_CfprTopMetaInfEveri_Type = SnmpAdminString
_CfprTopMetaInfEveri_Object = MibTableColumn
cfprTopMetaInfEveri = _CfprTopMetaInfEveri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 2, 1, 6),
    _CfprTopMetaInfEveri_Type()
)
cfprTopMetaInfEveri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopMetaInfEveri.setStatus("current")
_CfprTopRootTable_Object = MibTable
cfprTopRootTable = _CfprTopRootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 3)
)
if mibBuilder.loadTexts:
    cfprTopRootTable.setStatus("current")
_CfprTopRootEntry_Object = MibTableRow
cfprTopRootEntry = _CfprTopRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 3, 1)
)
cfprTopRootEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TOP-MIB", "cfprTopRootInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTopRootEntry.setStatus("current")
_CfprTopRootInstanceId_Type = CfprManagedObjectId
_CfprTopRootInstanceId_Object = MibTableColumn
cfprTopRootInstanceId = _CfprTopRootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 3, 1, 1),
    _CfprTopRootInstanceId_Type()
)
cfprTopRootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTopRootInstanceId.setStatus("current")
_CfprTopRootDn_Type = CfprManagedObjectDn
_CfprTopRootDn_Object = MibTableColumn
cfprTopRootDn = _CfprTopRootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 3, 1, 2),
    _CfprTopRootDn_Type()
)
cfprTopRootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopRootDn.setStatus("current")
_CfprTopRootRn_Type = SnmpAdminString
_CfprTopRootRn_Object = MibTableColumn
cfprTopRootRn = _CfprTopRootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 3, 1, 3),
    _CfprTopRootRn_Type()
)
cfprTopRootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopRootRn.setStatus("current")
_CfprTopSysDefaultsTable_Object = MibTable
cfprTopSysDefaultsTable = _CfprTopSysDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 4)
)
if mibBuilder.loadTexts:
    cfprTopSysDefaultsTable.setStatus("current")
_CfprTopSysDefaultsEntry_Object = MibTableRow
cfprTopSysDefaultsEntry = _CfprTopSysDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 4, 1)
)
cfprTopSysDefaultsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TOP-MIB", "cfprTopSysDefaultsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTopSysDefaultsEntry.setStatus("current")
_CfprTopSysDefaultsInstanceId_Type = CfprManagedObjectId
_CfprTopSysDefaultsInstanceId_Object = MibTableColumn
cfprTopSysDefaultsInstanceId = _CfprTopSysDefaultsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 4, 1, 1),
    _CfprTopSysDefaultsInstanceId_Type()
)
cfprTopSysDefaultsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTopSysDefaultsInstanceId.setStatus("current")
_CfprTopSysDefaultsDn_Type = CfprManagedObjectDn
_CfprTopSysDefaultsDn_Object = MibTableColumn
cfprTopSysDefaultsDn = _CfprTopSysDefaultsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 4, 1, 2),
    _CfprTopSysDefaultsDn_Type()
)
cfprTopSysDefaultsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSysDefaultsDn.setStatus("current")
_CfprTopSysDefaultsRn_Type = SnmpAdminString
_CfprTopSysDefaultsRn_Object = MibTableColumn
cfprTopSysDefaultsRn = _CfprTopSysDefaultsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 4, 1, 3),
    _CfprTopSysDefaultsRn_Type()
)
cfprTopSysDefaultsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSysDefaultsRn.setStatus("current")
_CfprTopSystemTable_Object = MibTable
cfprTopSystemTable = _CfprTopSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5)
)
if mibBuilder.loadTexts:
    cfprTopSystemTable.setStatus("current")
_CfprTopSystemEntry_Object = MibTableRow
cfprTopSystemEntry = _CfprTopSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1)
)
cfprTopSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TOP-MIB", "cfprTopSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTopSystemEntry.setStatus("current")
_CfprTopSystemInstanceId_Type = CfprManagedObjectId
_CfprTopSystemInstanceId_Object = MibTableColumn
cfprTopSystemInstanceId = _CfprTopSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 1),
    _CfprTopSystemInstanceId_Type()
)
cfprTopSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTopSystemInstanceId.setStatus("current")
_CfprTopSystemDn_Type = CfprManagedObjectDn
_CfprTopSystemDn_Object = MibTableColumn
cfprTopSystemDn = _CfprTopSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 2),
    _CfprTopSystemDn_Type()
)
cfprTopSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemDn.setStatus("current")
_CfprTopSystemRn_Type = SnmpAdminString
_CfprTopSystemRn_Object = MibTableColumn
cfprTopSystemRn = _CfprTopSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 3),
    _CfprTopSystemRn_Type()
)
cfprTopSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemRn.setStatus("current")
_CfprTopSystemAddress_Type = InetAddressIPv4
_CfprTopSystemAddress_Object = MibTableColumn
cfprTopSystemAddress = _CfprTopSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 4),
    _CfprTopSystemAddress_Type()
)
cfprTopSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemAddress.setStatus("current")
_CfprTopSystemCurrentTime_Type = DateAndTime
_CfprTopSystemCurrentTime_Object = MibTableColumn
cfprTopSystemCurrentTime = _CfprTopSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 5),
    _CfprTopSystemCurrentTime_Type()
)
cfprTopSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemCurrentTime.setStatus("current")
_CfprTopSystemDescr_Type = SnmpAdminString
_CfprTopSystemDescr_Object = MibTableColumn
cfprTopSystemDescr = _CfprTopSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 6),
    _CfprTopSystemDescr_Type()
)
cfprTopSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemDescr.setStatus("current")
_CfprTopSystemIpv6Addr_Type = InetAddressIPv6
_CfprTopSystemIpv6Addr_Object = MibTableColumn
cfprTopSystemIpv6Addr = _CfprTopSystemIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 7),
    _CfprTopSystemIpv6Addr_Type()
)
cfprTopSystemIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemIpv6Addr.setStatus("current")
_CfprTopSystemMode_Type = CfprTopMode
_CfprTopSystemMode_Object = MibTableColumn
cfprTopSystemMode = _CfprTopSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 8),
    _CfprTopSystemMode_Type()
)
cfprTopSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemMode.setStatus("current")
_CfprTopSystemName_Type = SnmpAdminString
_CfprTopSystemName_Object = MibTableColumn
cfprTopSystemName = _CfprTopSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 9),
    _CfprTopSystemName_Type()
)
cfprTopSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemName.setStatus("current")
_CfprTopSystemOwner_Type = SnmpAdminString
_CfprTopSystemOwner_Object = MibTableColumn
cfprTopSystemOwner = _CfprTopSystemOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 10),
    _CfprTopSystemOwner_Type()
)
cfprTopSystemOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemOwner.setStatus("current")
_CfprTopSystemSite_Type = SnmpAdminString
_CfprTopSystemSite_Object = MibTableColumn
cfprTopSystemSite = _CfprTopSystemSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 11),
    _CfprTopSystemSite_Type()
)
cfprTopSystemSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemSite.setStatus("current")
_CfprTopSystemSystemUpTime_Type = TimeIntervalSec
_CfprTopSystemSystemUpTime_Object = MibTableColumn
cfprTopSystemSystemUpTime = _CfprTopSystemSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 12),
    _CfprTopSystemSystemUpTime_Type()
)
cfprTopSystemSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemSystemUpTime.setStatus("current")
_CfprTopSystemMgmtUrl_Type = SnmpAdminString
_CfprTopSystemMgmtUrl_Object = MibTableColumn
cfprTopSystemMgmtUrl = _CfprTopSystemMgmtUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 13),
    _CfprTopSystemMgmtUrl_Type()
)
cfprTopSystemMgmtUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemMgmtUrl.setStatus("current")
_CfprTopSystemInitialSetupComplete_Type = TruthValue
_CfprTopSystemInitialSetupComplete_Object = MibTableColumn
cfprTopSystemInitialSetupComplete = _CfprTopSystemInitialSetupComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 78, 5, 1, 14),
    _CfprTopSystemInitialSetupComplete_Type()
)
cfprTopSystemInitialSetupComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTopSystemInitialSetupComplete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-TOP-MIB",
    **{"cfprTopObjects": cfprTopObjects,
       "cfprTopInfoPolicyTable": cfprTopInfoPolicyTable,
       "cfprTopInfoPolicyEntry": cfprTopInfoPolicyEntry,
       "cfprTopInfoPolicyInstanceId": cfprTopInfoPolicyInstanceId,
       "cfprTopInfoPolicyDn": cfprTopInfoPolicyDn,
       "cfprTopInfoPolicyRn": cfprTopInfoPolicyRn,
       "cfprTopInfoPolicyState": cfprTopInfoPolicyState,
       "cfprTopMetaInfTable": cfprTopMetaInfTable,
       "cfprTopMetaInfEntry": cfprTopMetaInfEntry,
       "cfprTopMetaInfInstanceId": cfprTopMetaInfInstanceId,
       "cfprTopMetaInfDn": cfprTopMetaInfDn,
       "cfprTopMetaInfRn": cfprTopMetaInfRn,
       "cfprTopMetaInfEcode": cfprTopMetaInfEcode,
       "cfprTopMetaInfName": cfprTopMetaInfName,
       "cfprTopMetaInfEveri": cfprTopMetaInfEveri,
       "cfprTopRootTable": cfprTopRootTable,
       "cfprTopRootEntry": cfprTopRootEntry,
       "cfprTopRootInstanceId": cfprTopRootInstanceId,
       "cfprTopRootDn": cfprTopRootDn,
       "cfprTopRootRn": cfprTopRootRn,
       "cfprTopSysDefaultsTable": cfprTopSysDefaultsTable,
       "cfprTopSysDefaultsEntry": cfprTopSysDefaultsEntry,
       "cfprTopSysDefaultsInstanceId": cfprTopSysDefaultsInstanceId,
       "cfprTopSysDefaultsDn": cfprTopSysDefaultsDn,
       "cfprTopSysDefaultsRn": cfprTopSysDefaultsRn,
       "cfprTopSystemTable": cfprTopSystemTable,
       "cfprTopSystemEntry": cfprTopSystemEntry,
       "cfprTopSystemInstanceId": cfprTopSystemInstanceId,
       "cfprTopSystemDn": cfprTopSystemDn,
       "cfprTopSystemRn": cfprTopSystemRn,
       "cfprTopSystemAddress": cfprTopSystemAddress,
       "cfprTopSystemCurrentTime": cfprTopSystemCurrentTime,
       "cfprTopSystemDescr": cfprTopSystemDescr,
       "cfprTopSystemIpv6Addr": cfprTopSystemIpv6Addr,
       "cfprTopSystemMode": cfprTopSystemMode,
       "cfprTopSystemName": cfprTopSystemName,
       "cfprTopSystemOwner": cfprTopSystemOwner,
       "cfprTopSystemSite": cfprTopSystemSite,
       "cfprTopSystemSystemUpTime": cfprTopSystemSystemUpTime,
       "cfprTopSystemMgmtUrl": cfprTopSystemMgmtUrl,
       "cfprTopSystemInitialSetupComplete": cfprTopSystemInitialSetupComplete}
)
