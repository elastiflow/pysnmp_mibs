# SNMP MIB module (CISCO-FIREPOWER-CIMCVMEDIA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-CIMCVMEDIA-MIB.mib
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

(CfprCimcvmediaDeviceType,
 CfprCimcvmediaErrorType,
 CfprCimcvmediaMountConfigRetryOnMountFail,
 CfprCimcvmediaMountStatus,
 CfprCimcvmediaTransport,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprCimcvmediaDeviceType",
    "CfprCimcvmediaErrorType",
    "CfprCimcvmediaMountConfigRetryOnMountFail",
    "CfprCimcvmediaMountStatus",
    "CfprCimcvmediaTransport",
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

cfprCimcvmediaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprCimcvmediaActualMountEntryTable_Object = MibTable
cfprCimcvmediaActualMountEntryTable = _CfprCimcvmediaActualMountEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryTable.setStatus("current")
_CfprCimcvmediaActualMountEntryEntry_Object = MibTableRow
cfprCimcvmediaActualMountEntryEntry = _CfprCimcvmediaActualMountEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1)
)
cfprCimcvmediaActualMountEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CIMCVMEDIA-MIB", "cfprCimcvmediaActualMountEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryEntry.setStatus("current")
_CfprCimcvmediaActualMountEntryInstanceId_Type = CfprManagedObjectId
_CfprCimcvmediaActualMountEntryInstanceId_Object = MibTableColumn
cfprCimcvmediaActualMountEntryInstanceId = _CfprCimcvmediaActualMountEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 1),
    _CfprCimcvmediaActualMountEntryInstanceId_Type()
)
cfprCimcvmediaActualMountEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryInstanceId.setStatus("current")
_CfprCimcvmediaActualMountEntryDn_Type = CfprManagedObjectDn
_CfprCimcvmediaActualMountEntryDn_Object = MibTableColumn
cfprCimcvmediaActualMountEntryDn = _CfprCimcvmediaActualMountEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 2),
    _CfprCimcvmediaActualMountEntryDn_Type()
)
cfprCimcvmediaActualMountEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryDn.setStatus("current")
_CfprCimcvmediaActualMountEntryRn_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryRn_Object = MibTableColumn
cfprCimcvmediaActualMountEntryRn = _CfprCimcvmediaActualMountEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 3),
    _CfprCimcvmediaActualMountEntryRn_Type()
)
cfprCimcvmediaActualMountEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryRn.setStatus("current")
_CfprCimcvmediaActualMountEntryDeviceType_Type = CfprCimcvmediaDeviceType
_CfprCimcvmediaActualMountEntryDeviceType_Object = MibTableColumn
cfprCimcvmediaActualMountEntryDeviceType = _CfprCimcvmediaActualMountEntryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 4),
    _CfprCimcvmediaActualMountEntryDeviceType_Type()
)
cfprCimcvmediaActualMountEntryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryDeviceType.setStatus("current")
_CfprCimcvmediaActualMountEntryEncPwd_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryEncPwd_Object = MibTableColumn
cfprCimcvmediaActualMountEntryEncPwd = _CfprCimcvmediaActualMountEntryEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 5),
    _CfprCimcvmediaActualMountEntryEncPwd_Type()
)
cfprCimcvmediaActualMountEntryEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryEncPwd.setStatus("current")
_CfprCimcvmediaActualMountEntryErrorType_Type = CfprCimcvmediaErrorType
_CfprCimcvmediaActualMountEntryErrorType_Object = MibTableColumn
cfprCimcvmediaActualMountEntryErrorType = _CfprCimcvmediaActualMountEntryErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 6),
    _CfprCimcvmediaActualMountEntryErrorType_Type()
)
cfprCimcvmediaActualMountEntryErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryErrorType.setStatus("current")
_CfprCimcvmediaActualMountEntryImageFileName_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryImageFileName_Object = MibTableColumn
cfprCimcvmediaActualMountEntryImageFileName = _CfprCimcvmediaActualMountEntryImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 7),
    _CfprCimcvmediaActualMountEntryImageFileName_Type()
)
cfprCimcvmediaActualMountEntryImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryImageFileName.setStatus("current")
_CfprCimcvmediaActualMountEntryImagePath_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryImagePath_Object = MibTableColumn
cfprCimcvmediaActualMountEntryImagePath = _CfprCimcvmediaActualMountEntryImagePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 8),
    _CfprCimcvmediaActualMountEntryImagePath_Type()
)
cfprCimcvmediaActualMountEntryImagePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryImagePath.setStatus("current")
_CfprCimcvmediaActualMountEntryMappingName_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryMappingName_Object = MibTableColumn
cfprCimcvmediaActualMountEntryMappingName = _CfprCimcvmediaActualMountEntryMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 9),
    _CfprCimcvmediaActualMountEntryMappingName_Type()
)
cfprCimcvmediaActualMountEntryMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryMappingName.setStatus("current")
_CfprCimcvmediaActualMountEntryMountProtocol_Type = CfprCimcvmediaTransport
_CfprCimcvmediaActualMountEntryMountProtocol_Object = MibTableColumn
cfprCimcvmediaActualMountEntryMountProtocol = _CfprCimcvmediaActualMountEntryMountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 10),
    _CfprCimcvmediaActualMountEntryMountProtocol_Type()
)
cfprCimcvmediaActualMountEntryMountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryMountProtocol.setStatus("current")
_CfprCimcvmediaActualMountEntryOperMountStatus_Type = CfprCimcvmediaMountStatus
_CfprCimcvmediaActualMountEntryOperMountStatus_Object = MibTableColumn
cfprCimcvmediaActualMountEntryOperMountStatus = _CfprCimcvmediaActualMountEntryOperMountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 11),
    _CfprCimcvmediaActualMountEntryOperMountStatus_Type()
)
cfprCimcvmediaActualMountEntryOperMountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryOperMountStatus.setStatus("current")
_CfprCimcvmediaActualMountEntryPassword_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryPassword_Object = MibTableColumn
cfprCimcvmediaActualMountEntryPassword = _CfprCimcvmediaActualMountEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 12),
    _CfprCimcvmediaActualMountEntryPassword_Type()
)
cfprCimcvmediaActualMountEntryPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryPassword.setStatus("current")
_CfprCimcvmediaActualMountEntryPwdSet_Type = TruthValue
_CfprCimcvmediaActualMountEntryPwdSet_Object = MibTableColumn
cfprCimcvmediaActualMountEntryPwdSet = _CfprCimcvmediaActualMountEntryPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 13),
    _CfprCimcvmediaActualMountEntryPwdSet_Type()
)
cfprCimcvmediaActualMountEntryPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryPwdSet.setStatus("current")
_CfprCimcvmediaActualMountEntryRemoteHost_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryRemoteHost_Object = MibTableColumn
cfprCimcvmediaActualMountEntryRemoteHost = _CfprCimcvmediaActualMountEntryRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 14),
    _CfprCimcvmediaActualMountEntryRemoteHost_Type()
)
cfprCimcvmediaActualMountEntryRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryRemoteHost.setStatus("current")
_CfprCimcvmediaActualMountEntryRemoteIpAddress_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryRemoteIpAddress_Object = MibTableColumn
cfprCimcvmediaActualMountEntryRemoteIpAddress = _CfprCimcvmediaActualMountEntryRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 15),
    _CfprCimcvmediaActualMountEntryRemoteIpAddress_Type()
)
cfprCimcvmediaActualMountEntryRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryRemoteIpAddress.setStatus("current")
_CfprCimcvmediaActualMountEntryRemotePort_Type = Gauge32
_CfprCimcvmediaActualMountEntryRemotePort_Object = MibTableColumn
cfprCimcvmediaActualMountEntryRemotePort = _CfprCimcvmediaActualMountEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 16),
    _CfprCimcvmediaActualMountEntryRemotePort_Type()
)
cfprCimcvmediaActualMountEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryRemotePort.setStatus("current")
_CfprCimcvmediaActualMountEntryUserId_Type = SnmpAdminString
_CfprCimcvmediaActualMountEntryUserId_Object = MibTableColumn
cfprCimcvmediaActualMountEntryUserId = _CfprCimcvmediaActualMountEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 17),
    _CfprCimcvmediaActualMountEntryUserId_Type()
)
cfprCimcvmediaActualMountEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryUserId.setStatus("current")
_CfprCimcvmediaActualMountEntryVirtualDiskId_Type = Gauge32
_CfprCimcvmediaActualMountEntryVirtualDiskId_Object = MibTableColumn
cfprCimcvmediaActualMountEntryVirtualDiskId = _CfprCimcvmediaActualMountEntryVirtualDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 1, 1, 18),
    _CfprCimcvmediaActualMountEntryVirtualDiskId_Type()
)
cfprCimcvmediaActualMountEntryVirtualDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountEntryVirtualDiskId.setStatus("current")
_CfprCimcvmediaActualMountListTable_Object = MibTable
cfprCimcvmediaActualMountListTable = _CfprCimcvmediaActualMountListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 2)
)
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountListTable.setStatus("current")
_CfprCimcvmediaActualMountListEntry_Object = MibTableRow
cfprCimcvmediaActualMountListEntry = _CfprCimcvmediaActualMountListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 2, 1)
)
cfprCimcvmediaActualMountListEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CIMCVMEDIA-MIB", "cfprCimcvmediaActualMountListInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountListEntry.setStatus("current")
_CfprCimcvmediaActualMountListInstanceId_Type = CfprManagedObjectId
_CfprCimcvmediaActualMountListInstanceId_Object = MibTableColumn
cfprCimcvmediaActualMountListInstanceId = _CfprCimcvmediaActualMountListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 2, 1, 1),
    _CfprCimcvmediaActualMountListInstanceId_Type()
)
cfprCimcvmediaActualMountListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountListInstanceId.setStatus("current")
_CfprCimcvmediaActualMountListDn_Type = CfprManagedObjectDn
_CfprCimcvmediaActualMountListDn_Object = MibTableColumn
cfprCimcvmediaActualMountListDn = _CfprCimcvmediaActualMountListDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 2, 1, 2),
    _CfprCimcvmediaActualMountListDn_Type()
)
cfprCimcvmediaActualMountListDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountListDn.setStatus("current")
_CfprCimcvmediaActualMountListRn_Type = SnmpAdminString
_CfprCimcvmediaActualMountListRn_Object = MibTableColumn
cfprCimcvmediaActualMountListRn = _CfprCimcvmediaActualMountListRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 2, 1, 3),
    _CfprCimcvmediaActualMountListRn_Type()
)
cfprCimcvmediaActualMountListRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaActualMountListRn.setStatus("current")
_CfprCimcvmediaConfigMountEntryTable_Object = MibTable
cfprCimcvmediaConfigMountEntryTable = _CfprCimcvmediaConfigMountEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3)
)
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryTable.setStatus("current")
_CfprCimcvmediaConfigMountEntryEntry_Object = MibTableRow
cfprCimcvmediaConfigMountEntryEntry = _CfprCimcvmediaConfigMountEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1)
)
cfprCimcvmediaConfigMountEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CIMCVMEDIA-MIB", "cfprCimcvmediaConfigMountEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryEntry.setStatus("current")
_CfprCimcvmediaConfigMountEntryInstanceId_Type = CfprManagedObjectId
_CfprCimcvmediaConfigMountEntryInstanceId_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryInstanceId = _CfprCimcvmediaConfigMountEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 1),
    _CfprCimcvmediaConfigMountEntryInstanceId_Type()
)
cfprCimcvmediaConfigMountEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryInstanceId.setStatus("current")
_CfprCimcvmediaConfigMountEntryDn_Type = CfprManagedObjectDn
_CfprCimcvmediaConfigMountEntryDn_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryDn = _CfprCimcvmediaConfigMountEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 2),
    _CfprCimcvmediaConfigMountEntryDn_Type()
)
cfprCimcvmediaConfigMountEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryDn.setStatus("current")
_CfprCimcvmediaConfigMountEntryRn_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryRn_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryRn = _CfprCimcvmediaConfigMountEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 3),
    _CfprCimcvmediaConfigMountEntryRn_Type()
)
cfprCimcvmediaConfigMountEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryRn.setStatus("current")
_CfprCimcvmediaConfigMountEntryDescription_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryDescription_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryDescription = _CfprCimcvmediaConfigMountEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 4),
    _CfprCimcvmediaConfigMountEntryDescription_Type()
)
cfprCimcvmediaConfigMountEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryDescription.setStatus("current")
_CfprCimcvmediaConfigMountEntryDeviceType_Type = CfprCimcvmediaDeviceType
_CfprCimcvmediaConfigMountEntryDeviceType_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryDeviceType = _CfprCimcvmediaConfigMountEntryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 5),
    _CfprCimcvmediaConfigMountEntryDeviceType_Type()
)
cfprCimcvmediaConfigMountEntryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryDeviceType.setStatus("current")
_CfprCimcvmediaConfigMountEntryEncPwd_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryEncPwd_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryEncPwd = _CfprCimcvmediaConfigMountEntryEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 6),
    _CfprCimcvmediaConfigMountEntryEncPwd_Type()
)
cfprCimcvmediaConfigMountEntryEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryEncPwd.setStatus("current")
_CfprCimcvmediaConfigMountEntryImageFileName_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryImageFileName_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryImageFileName = _CfprCimcvmediaConfigMountEntryImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 7),
    _CfprCimcvmediaConfigMountEntryImageFileName_Type()
)
cfprCimcvmediaConfigMountEntryImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryImageFileName.setStatus("current")
_CfprCimcvmediaConfigMountEntryImagePath_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryImagePath_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryImagePath = _CfprCimcvmediaConfigMountEntryImagePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 8),
    _CfprCimcvmediaConfigMountEntryImagePath_Type()
)
cfprCimcvmediaConfigMountEntryImagePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryImagePath.setStatus("current")
_CfprCimcvmediaConfigMountEntryMappingName_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryMappingName_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryMappingName = _CfprCimcvmediaConfigMountEntryMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 9),
    _CfprCimcvmediaConfigMountEntryMappingName_Type()
)
cfprCimcvmediaConfigMountEntryMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryMappingName.setStatus("current")
_CfprCimcvmediaConfigMountEntryMountProtocol_Type = CfprCimcvmediaTransport
_CfprCimcvmediaConfigMountEntryMountProtocol_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryMountProtocol = _CfprCimcvmediaConfigMountEntryMountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 10),
    _CfprCimcvmediaConfigMountEntryMountProtocol_Type()
)
cfprCimcvmediaConfigMountEntryMountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryMountProtocol.setStatus("current")
_CfprCimcvmediaConfigMountEntryPassword_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryPassword_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryPassword = _CfprCimcvmediaConfigMountEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 11),
    _CfprCimcvmediaConfigMountEntryPassword_Type()
)
cfprCimcvmediaConfigMountEntryPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryPassword.setStatus("current")
_CfprCimcvmediaConfigMountEntryPwdSet_Type = TruthValue
_CfprCimcvmediaConfigMountEntryPwdSet_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryPwdSet = _CfprCimcvmediaConfigMountEntryPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 12),
    _CfprCimcvmediaConfigMountEntryPwdSet_Type()
)
cfprCimcvmediaConfigMountEntryPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryPwdSet.setStatus("current")
_CfprCimcvmediaConfigMountEntryRemoteHost_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryRemoteHost_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryRemoteHost = _CfprCimcvmediaConfigMountEntryRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 13),
    _CfprCimcvmediaConfigMountEntryRemoteHost_Type()
)
cfprCimcvmediaConfigMountEntryRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryRemoteHost.setStatus("current")
_CfprCimcvmediaConfigMountEntryRemoteIpAddress_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryRemoteIpAddress_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryRemoteIpAddress = _CfprCimcvmediaConfigMountEntryRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 14),
    _CfprCimcvmediaConfigMountEntryRemoteIpAddress_Type()
)
cfprCimcvmediaConfigMountEntryRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryRemoteIpAddress.setStatus("current")
_CfprCimcvmediaConfigMountEntryRemotePort_Type = Gauge32
_CfprCimcvmediaConfigMountEntryRemotePort_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryRemotePort = _CfprCimcvmediaConfigMountEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 15),
    _CfprCimcvmediaConfigMountEntryRemotePort_Type()
)
cfprCimcvmediaConfigMountEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryRemotePort.setStatus("current")
_CfprCimcvmediaConfigMountEntryUserId_Type = SnmpAdminString
_CfprCimcvmediaConfigMountEntryUserId_Object = MibTableColumn
cfprCimcvmediaConfigMountEntryUserId = _CfprCimcvmediaConfigMountEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 3, 1, 16),
    _CfprCimcvmediaConfigMountEntryUserId_Type()
)
cfprCimcvmediaConfigMountEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaConfigMountEntryUserId.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryTable_Object = MibTable
cfprCimcvmediaExtMgmtRuleEntryTable = _CfprCimcvmediaExtMgmtRuleEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4)
)
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryTable.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryEntry_Object = MibTableRow
cfprCimcvmediaExtMgmtRuleEntryEntry = _CfprCimcvmediaExtMgmtRuleEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1)
)
cfprCimcvmediaExtMgmtRuleEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CIMCVMEDIA-MIB", "cfprCimcvmediaExtMgmtRuleEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryEntry.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryInstanceId_Type = CfprManagedObjectId
_CfprCimcvmediaExtMgmtRuleEntryInstanceId_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryInstanceId = _CfprCimcvmediaExtMgmtRuleEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 1),
    _CfprCimcvmediaExtMgmtRuleEntryInstanceId_Type()
)
cfprCimcvmediaExtMgmtRuleEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryInstanceId.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryDn_Type = CfprManagedObjectDn
_CfprCimcvmediaExtMgmtRuleEntryDn_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryDn = _CfprCimcvmediaExtMgmtRuleEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 2),
    _CfprCimcvmediaExtMgmtRuleEntryDn_Type()
)
cfprCimcvmediaExtMgmtRuleEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryDn.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryRn_Type = SnmpAdminString
_CfprCimcvmediaExtMgmtRuleEntryRn_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryRn = _CfprCimcvmediaExtMgmtRuleEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 3),
    _CfprCimcvmediaExtMgmtRuleEntryRn_Type()
)
cfprCimcvmediaExtMgmtRuleEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryRn.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Type = InetAddressIPv4
_CfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr = _CfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 4),
    _CfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Type()
)
cfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryMappingName_Type = SnmpAdminString
_CfprCimcvmediaExtMgmtRuleEntryMappingName_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryMappingName = _CfprCimcvmediaExtMgmtRuleEntryMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 5),
    _CfprCimcvmediaExtMgmtRuleEntryMappingName_Type()
)
cfprCimcvmediaExtMgmtRuleEntryMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryMappingName.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Type = InetAddressIPv4
_CfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr = _CfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 6),
    _CfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Type()
)
cfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryMountProtocol_Type = CfprCimcvmediaTransport
_CfprCimcvmediaExtMgmtRuleEntryMountProtocol_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryMountProtocol = _CfprCimcvmediaExtMgmtRuleEntryMountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 7),
    _CfprCimcvmediaExtMgmtRuleEntryMountProtocol_Type()
)
cfprCimcvmediaExtMgmtRuleEntryMountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryMountProtocol.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Type = InetAddressIPv4
_CfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr = _CfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 8),
    _CfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Type()
)
cfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr.setStatus("current")
_CfprCimcvmediaExtMgmtRuleEntryRemotePort_Type = Gauge32
_CfprCimcvmediaExtMgmtRuleEntryRemotePort_Object = MibTableColumn
cfprCimcvmediaExtMgmtRuleEntryRemotePort = _CfprCimcvmediaExtMgmtRuleEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 4, 1, 9),
    _CfprCimcvmediaExtMgmtRuleEntryRemotePort_Type()
)
cfprCimcvmediaExtMgmtRuleEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaExtMgmtRuleEntryRemotePort.setStatus("current")
_CfprCimcvmediaMountConfigDefTable_Object = MibTable
cfprCimcvmediaMountConfigDefTable = _CfprCimcvmediaMountConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5)
)
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefTable.setStatus("current")
_CfprCimcvmediaMountConfigDefEntry_Object = MibTableRow
cfprCimcvmediaMountConfigDefEntry = _CfprCimcvmediaMountConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1)
)
cfprCimcvmediaMountConfigDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CIMCVMEDIA-MIB", "cfprCimcvmediaMountConfigDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefEntry.setStatus("current")
_CfprCimcvmediaMountConfigDefInstanceId_Type = CfprManagedObjectId
_CfprCimcvmediaMountConfigDefInstanceId_Object = MibTableColumn
cfprCimcvmediaMountConfigDefInstanceId = _CfprCimcvmediaMountConfigDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 1),
    _CfprCimcvmediaMountConfigDefInstanceId_Type()
)
cfprCimcvmediaMountConfigDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefInstanceId.setStatus("current")
_CfprCimcvmediaMountConfigDefDn_Type = CfprManagedObjectDn
_CfprCimcvmediaMountConfigDefDn_Object = MibTableColumn
cfprCimcvmediaMountConfigDefDn = _CfprCimcvmediaMountConfigDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 2),
    _CfprCimcvmediaMountConfigDefDn_Type()
)
cfprCimcvmediaMountConfigDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefDn.setStatus("current")
_CfprCimcvmediaMountConfigDefRn_Type = SnmpAdminString
_CfprCimcvmediaMountConfigDefRn_Object = MibTableColumn
cfprCimcvmediaMountConfigDefRn = _CfprCimcvmediaMountConfigDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 3),
    _CfprCimcvmediaMountConfigDefRn_Type()
)
cfprCimcvmediaMountConfigDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefRn.setStatus("current")
_CfprCimcvmediaMountConfigDefDescr_Type = SnmpAdminString
_CfprCimcvmediaMountConfigDefDescr_Object = MibTableColumn
cfprCimcvmediaMountConfigDefDescr = _CfprCimcvmediaMountConfigDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 4),
    _CfprCimcvmediaMountConfigDefDescr_Type()
)
cfprCimcvmediaMountConfigDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefDescr.setStatus("current")
_CfprCimcvmediaMountConfigDefIntId_Type = SnmpAdminString
_CfprCimcvmediaMountConfigDefIntId_Object = MibTableColumn
cfprCimcvmediaMountConfigDefIntId = _CfprCimcvmediaMountConfigDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 5),
    _CfprCimcvmediaMountConfigDefIntId_Type()
)
cfprCimcvmediaMountConfigDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefIntId.setStatus("current")
_CfprCimcvmediaMountConfigDefName_Type = SnmpAdminString
_CfprCimcvmediaMountConfigDefName_Object = MibTableColumn
cfprCimcvmediaMountConfigDefName = _CfprCimcvmediaMountConfigDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 6),
    _CfprCimcvmediaMountConfigDefName_Type()
)
cfprCimcvmediaMountConfigDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefName.setStatus("current")
_CfprCimcvmediaMountConfigDefPolicyLevel_Type = Gauge32
_CfprCimcvmediaMountConfigDefPolicyLevel_Object = MibTableColumn
cfprCimcvmediaMountConfigDefPolicyLevel = _CfprCimcvmediaMountConfigDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 7),
    _CfprCimcvmediaMountConfigDefPolicyLevel_Type()
)
cfprCimcvmediaMountConfigDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefPolicyLevel.setStatus("current")
_CfprCimcvmediaMountConfigDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCimcvmediaMountConfigDefPolicyOwner_Object = MibTableColumn
cfprCimcvmediaMountConfigDefPolicyOwner = _CfprCimcvmediaMountConfigDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 8),
    _CfprCimcvmediaMountConfigDefPolicyOwner_Type()
)
cfprCimcvmediaMountConfigDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefPolicyOwner.setStatus("current")
_CfprCimcvmediaMountConfigDefRetryOnMountFail_Type = CfprCimcvmediaMountConfigRetryOnMountFail
_CfprCimcvmediaMountConfigDefRetryOnMountFail_Object = MibTableColumn
cfprCimcvmediaMountConfigDefRetryOnMountFail = _CfprCimcvmediaMountConfigDefRetryOnMountFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 5, 1, 9),
    _CfprCimcvmediaMountConfigDefRetryOnMountFail_Type()
)
cfprCimcvmediaMountConfigDefRetryOnMountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigDefRetryOnMountFail.setStatus("current")
_CfprCimcvmediaMountConfigPolicyTable_Object = MibTable
cfprCimcvmediaMountConfigPolicyTable = _CfprCimcvmediaMountConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6)
)
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyTable.setStatus("current")
_CfprCimcvmediaMountConfigPolicyEntry_Object = MibTableRow
cfprCimcvmediaMountConfigPolicyEntry = _CfprCimcvmediaMountConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1)
)
cfprCimcvmediaMountConfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CIMCVMEDIA-MIB", "cfprCimcvmediaMountConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyEntry.setStatus("current")
_CfprCimcvmediaMountConfigPolicyInstanceId_Type = CfprManagedObjectId
_CfprCimcvmediaMountConfigPolicyInstanceId_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyInstanceId = _CfprCimcvmediaMountConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 1),
    _CfprCimcvmediaMountConfigPolicyInstanceId_Type()
)
cfprCimcvmediaMountConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyInstanceId.setStatus("current")
_CfprCimcvmediaMountConfigPolicyDn_Type = CfprManagedObjectDn
_CfprCimcvmediaMountConfigPolicyDn_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyDn = _CfprCimcvmediaMountConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 2),
    _CfprCimcvmediaMountConfigPolicyDn_Type()
)
cfprCimcvmediaMountConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyDn.setStatus("current")
_CfprCimcvmediaMountConfigPolicyRn_Type = SnmpAdminString
_CfprCimcvmediaMountConfigPolicyRn_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyRn = _CfprCimcvmediaMountConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 3),
    _CfprCimcvmediaMountConfigPolicyRn_Type()
)
cfprCimcvmediaMountConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyRn.setStatus("current")
_CfprCimcvmediaMountConfigPolicyDescr_Type = SnmpAdminString
_CfprCimcvmediaMountConfigPolicyDescr_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyDescr = _CfprCimcvmediaMountConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 4),
    _CfprCimcvmediaMountConfigPolicyDescr_Type()
)
cfprCimcvmediaMountConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyDescr.setStatus("current")
_CfprCimcvmediaMountConfigPolicyIntId_Type = SnmpAdminString
_CfprCimcvmediaMountConfigPolicyIntId_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyIntId = _CfprCimcvmediaMountConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 5),
    _CfprCimcvmediaMountConfigPolicyIntId_Type()
)
cfprCimcvmediaMountConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyIntId.setStatus("current")
_CfprCimcvmediaMountConfigPolicyName_Type = SnmpAdminString
_CfprCimcvmediaMountConfigPolicyName_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyName = _CfprCimcvmediaMountConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 6),
    _CfprCimcvmediaMountConfigPolicyName_Type()
)
cfprCimcvmediaMountConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyName.setStatus("current")
_CfprCimcvmediaMountConfigPolicyPolicyLevel_Type = Gauge32
_CfprCimcvmediaMountConfigPolicyPolicyLevel_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyPolicyLevel = _CfprCimcvmediaMountConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 7),
    _CfprCimcvmediaMountConfigPolicyPolicyLevel_Type()
)
cfprCimcvmediaMountConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyPolicyLevel.setStatus("current")
_CfprCimcvmediaMountConfigPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprCimcvmediaMountConfigPolicyPolicyOwner_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyPolicyOwner = _CfprCimcvmediaMountConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 8),
    _CfprCimcvmediaMountConfigPolicyPolicyOwner_Type()
)
cfprCimcvmediaMountConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyPolicyOwner.setStatus("current")
_CfprCimcvmediaMountConfigPolicyRetryOnMountFail_Type = CfprCimcvmediaMountConfigRetryOnMountFail
_CfprCimcvmediaMountConfigPolicyRetryOnMountFail_Object = MibTableColumn
cfprCimcvmediaMountConfigPolicyRetryOnMountFail = _CfprCimcvmediaMountConfigPolicyRetryOnMountFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 10, 6, 1, 9),
    _CfprCimcvmediaMountConfigPolicyRetryOnMountFail_Type()
)
cfprCimcvmediaMountConfigPolicyRetryOnMountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCimcvmediaMountConfigPolicyRetryOnMountFail.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-CIMCVMEDIA-MIB",
    **{"cfprCimcvmediaObjects": cfprCimcvmediaObjects,
       "cfprCimcvmediaActualMountEntryTable": cfprCimcvmediaActualMountEntryTable,
       "cfprCimcvmediaActualMountEntryEntry": cfprCimcvmediaActualMountEntryEntry,
       "cfprCimcvmediaActualMountEntryInstanceId": cfprCimcvmediaActualMountEntryInstanceId,
       "cfprCimcvmediaActualMountEntryDn": cfprCimcvmediaActualMountEntryDn,
       "cfprCimcvmediaActualMountEntryRn": cfprCimcvmediaActualMountEntryRn,
       "cfprCimcvmediaActualMountEntryDeviceType": cfprCimcvmediaActualMountEntryDeviceType,
       "cfprCimcvmediaActualMountEntryEncPwd": cfprCimcvmediaActualMountEntryEncPwd,
       "cfprCimcvmediaActualMountEntryErrorType": cfprCimcvmediaActualMountEntryErrorType,
       "cfprCimcvmediaActualMountEntryImageFileName": cfprCimcvmediaActualMountEntryImageFileName,
       "cfprCimcvmediaActualMountEntryImagePath": cfprCimcvmediaActualMountEntryImagePath,
       "cfprCimcvmediaActualMountEntryMappingName": cfprCimcvmediaActualMountEntryMappingName,
       "cfprCimcvmediaActualMountEntryMountProtocol": cfprCimcvmediaActualMountEntryMountProtocol,
       "cfprCimcvmediaActualMountEntryOperMountStatus": cfprCimcvmediaActualMountEntryOperMountStatus,
       "cfprCimcvmediaActualMountEntryPassword": cfprCimcvmediaActualMountEntryPassword,
       "cfprCimcvmediaActualMountEntryPwdSet": cfprCimcvmediaActualMountEntryPwdSet,
       "cfprCimcvmediaActualMountEntryRemoteHost": cfprCimcvmediaActualMountEntryRemoteHost,
       "cfprCimcvmediaActualMountEntryRemoteIpAddress": cfprCimcvmediaActualMountEntryRemoteIpAddress,
       "cfprCimcvmediaActualMountEntryRemotePort": cfprCimcvmediaActualMountEntryRemotePort,
       "cfprCimcvmediaActualMountEntryUserId": cfprCimcvmediaActualMountEntryUserId,
       "cfprCimcvmediaActualMountEntryVirtualDiskId": cfprCimcvmediaActualMountEntryVirtualDiskId,
       "cfprCimcvmediaActualMountListTable": cfprCimcvmediaActualMountListTable,
       "cfprCimcvmediaActualMountListEntry": cfprCimcvmediaActualMountListEntry,
       "cfprCimcvmediaActualMountListInstanceId": cfprCimcvmediaActualMountListInstanceId,
       "cfprCimcvmediaActualMountListDn": cfprCimcvmediaActualMountListDn,
       "cfprCimcvmediaActualMountListRn": cfprCimcvmediaActualMountListRn,
       "cfprCimcvmediaConfigMountEntryTable": cfprCimcvmediaConfigMountEntryTable,
       "cfprCimcvmediaConfigMountEntryEntry": cfprCimcvmediaConfigMountEntryEntry,
       "cfprCimcvmediaConfigMountEntryInstanceId": cfprCimcvmediaConfigMountEntryInstanceId,
       "cfprCimcvmediaConfigMountEntryDn": cfprCimcvmediaConfigMountEntryDn,
       "cfprCimcvmediaConfigMountEntryRn": cfprCimcvmediaConfigMountEntryRn,
       "cfprCimcvmediaConfigMountEntryDescription": cfprCimcvmediaConfigMountEntryDescription,
       "cfprCimcvmediaConfigMountEntryDeviceType": cfprCimcvmediaConfigMountEntryDeviceType,
       "cfprCimcvmediaConfigMountEntryEncPwd": cfprCimcvmediaConfigMountEntryEncPwd,
       "cfprCimcvmediaConfigMountEntryImageFileName": cfprCimcvmediaConfigMountEntryImageFileName,
       "cfprCimcvmediaConfigMountEntryImagePath": cfprCimcvmediaConfigMountEntryImagePath,
       "cfprCimcvmediaConfigMountEntryMappingName": cfprCimcvmediaConfigMountEntryMappingName,
       "cfprCimcvmediaConfigMountEntryMountProtocol": cfprCimcvmediaConfigMountEntryMountProtocol,
       "cfprCimcvmediaConfigMountEntryPassword": cfprCimcvmediaConfigMountEntryPassword,
       "cfprCimcvmediaConfigMountEntryPwdSet": cfprCimcvmediaConfigMountEntryPwdSet,
       "cfprCimcvmediaConfigMountEntryRemoteHost": cfprCimcvmediaConfigMountEntryRemoteHost,
       "cfprCimcvmediaConfigMountEntryRemoteIpAddress": cfprCimcvmediaConfigMountEntryRemoteIpAddress,
       "cfprCimcvmediaConfigMountEntryRemotePort": cfprCimcvmediaConfigMountEntryRemotePort,
       "cfprCimcvmediaConfigMountEntryUserId": cfprCimcvmediaConfigMountEntryUserId,
       "cfprCimcvmediaExtMgmtRuleEntryTable": cfprCimcvmediaExtMgmtRuleEntryTable,
       "cfprCimcvmediaExtMgmtRuleEntryEntry": cfprCimcvmediaExtMgmtRuleEntryEntry,
       "cfprCimcvmediaExtMgmtRuleEntryInstanceId": cfprCimcvmediaExtMgmtRuleEntryInstanceId,
       "cfprCimcvmediaExtMgmtRuleEntryDn": cfprCimcvmediaExtMgmtRuleEntryDn,
       "cfprCimcvmediaExtMgmtRuleEntryRn": cfprCimcvmediaExtMgmtRuleEntryRn,
       "cfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr": cfprCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr,
       "cfprCimcvmediaExtMgmtRuleEntryMappingName": cfprCimcvmediaExtMgmtRuleEntryMappingName,
       "cfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr": cfprCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr,
       "cfprCimcvmediaExtMgmtRuleEntryMountProtocol": cfprCimcvmediaExtMgmtRuleEntryMountProtocol,
       "cfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr": cfprCimcvmediaExtMgmtRuleEntryRemoteIpAddr,
       "cfprCimcvmediaExtMgmtRuleEntryRemotePort": cfprCimcvmediaExtMgmtRuleEntryRemotePort,
       "cfprCimcvmediaMountConfigDefTable": cfprCimcvmediaMountConfigDefTable,
       "cfprCimcvmediaMountConfigDefEntry": cfprCimcvmediaMountConfigDefEntry,
       "cfprCimcvmediaMountConfigDefInstanceId": cfprCimcvmediaMountConfigDefInstanceId,
       "cfprCimcvmediaMountConfigDefDn": cfprCimcvmediaMountConfigDefDn,
       "cfprCimcvmediaMountConfigDefRn": cfprCimcvmediaMountConfigDefRn,
       "cfprCimcvmediaMountConfigDefDescr": cfprCimcvmediaMountConfigDefDescr,
       "cfprCimcvmediaMountConfigDefIntId": cfprCimcvmediaMountConfigDefIntId,
       "cfprCimcvmediaMountConfigDefName": cfprCimcvmediaMountConfigDefName,
       "cfprCimcvmediaMountConfigDefPolicyLevel": cfprCimcvmediaMountConfigDefPolicyLevel,
       "cfprCimcvmediaMountConfigDefPolicyOwner": cfprCimcvmediaMountConfigDefPolicyOwner,
       "cfprCimcvmediaMountConfigDefRetryOnMountFail": cfprCimcvmediaMountConfigDefRetryOnMountFail,
       "cfprCimcvmediaMountConfigPolicyTable": cfprCimcvmediaMountConfigPolicyTable,
       "cfprCimcvmediaMountConfigPolicyEntry": cfprCimcvmediaMountConfigPolicyEntry,
       "cfprCimcvmediaMountConfigPolicyInstanceId": cfprCimcvmediaMountConfigPolicyInstanceId,
       "cfprCimcvmediaMountConfigPolicyDn": cfprCimcvmediaMountConfigPolicyDn,
       "cfprCimcvmediaMountConfigPolicyRn": cfprCimcvmediaMountConfigPolicyRn,
       "cfprCimcvmediaMountConfigPolicyDescr": cfprCimcvmediaMountConfigPolicyDescr,
       "cfprCimcvmediaMountConfigPolicyIntId": cfprCimcvmediaMountConfigPolicyIntId,
       "cfprCimcvmediaMountConfigPolicyName": cfprCimcvmediaMountConfigPolicyName,
       "cfprCimcvmediaMountConfigPolicyPolicyLevel": cfprCimcvmediaMountConfigPolicyPolicyLevel,
       "cfprCimcvmediaMountConfigPolicyPolicyOwner": cfprCimcvmediaMountConfigPolicyPolicyOwner,
       "cfprCimcvmediaMountConfigPolicyRetryOnMountFail": cfprCimcvmediaMountConfigPolicyRetryOnMountFail}
)
