# SNMP MIB module (CISCO-FIREPOWER-AP-LSBOOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-LSBOOT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApLsbootADefBootMode,
 CfprApLsbootAccessType,
 CfprApLsbootDefaultLocalImageType,
 CfprApLsbootIScsiAccess,
 CfprApLsbootIScsiImagePathType,
 CfprApLsbootIScsiType,
 CfprApLsbootLanAccess,
 CfprApLsbootLanBootProt,
 CfprApLsbootLanImagePathType,
 CfprApLsbootLanType,
 CfprApLsbootLocalHddImageType,
 CfprApLsbootPurpose,
 CfprApLsbootSanAccess,
 CfprApLsbootSanCatSanImagePathType,
 CfprApLsbootSanCatSanImageType,
 CfprApLsbootSanImagePathType,
 CfprApLsbootSanImageType,
 CfprApLsbootSanType,
 CfprApLsbootStorageAccess,
 CfprApLsbootStorageType,
 CfprApLsbootUsbExternalImageType,
 CfprApLsbootUsbFlashStorageImageType,
 CfprApLsbootUsbInternalImageType,
 CfprApLsbootVirtualMediaType,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApLsbootADefBootMode",
    "CfprApLsbootAccessType",
    "CfprApLsbootDefaultLocalImageType",
    "CfprApLsbootIScsiAccess",
    "CfprApLsbootIScsiImagePathType",
    "CfprApLsbootIScsiType",
    "CfprApLsbootLanAccess",
    "CfprApLsbootLanBootProt",
    "CfprApLsbootLanImagePathType",
    "CfprApLsbootLanType",
    "CfprApLsbootLocalHddImageType",
    "CfprApLsbootPurpose",
    "CfprApLsbootSanAccess",
    "CfprApLsbootSanCatSanImagePathType",
    "CfprApLsbootSanCatSanImageType",
    "CfprApLsbootSanImagePathType",
    "CfprApLsbootSanImageType",
    "CfprApLsbootSanType",
    "CfprApLsbootStorageAccess",
    "CfprApLsbootStorageType",
    "CfprApLsbootUsbExternalImageType",
    "CfprApLsbootUsbFlashStorageImageType",
    "CfprApLsbootUsbInternalImageType",
    "CfprApLsbootVirtualMediaType",
    "CfprApPolicyPolicyOwner")

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

cfprApLsbootObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApLsbootBootSecurityTable_Object = MibTable
cfprApLsbootBootSecurityTable = _CfprApLsbootBootSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 1)
)
if mibBuilder.loadTexts:
    cfprApLsbootBootSecurityTable.setStatus("current")
_CfprApLsbootBootSecurityEntry_Object = MibTableRow
cfprApLsbootBootSecurityEntry = _CfprApLsbootBootSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 1, 1)
)
cfprApLsbootBootSecurityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootBootSecurityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootBootSecurityEntry.setStatus("current")
_CfprApLsbootBootSecurityInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootBootSecurityInstanceId_Object = MibTableColumn
cfprApLsbootBootSecurityInstanceId = _CfprApLsbootBootSecurityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 1, 1, 1),
    _CfprApLsbootBootSecurityInstanceId_Type()
)
cfprApLsbootBootSecurityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootBootSecurityInstanceId.setStatus("current")
_CfprApLsbootBootSecurityDn_Type = CfprApManagedObjectDn
_CfprApLsbootBootSecurityDn_Object = MibTableColumn
cfprApLsbootBootSecurityDn = _CfprApLsbootBootSecurityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 1, 1, 2),
    _CfprApLsbootBootSecurityDn_Type()
)
cfprApLsbootBootSecurityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootBootSecurityDn.setStatus("current")
_CfprApLsbootBootSecurityRn_Type = SnmpAdminString
_CfprApLsbootBootSecurityRn_Object = MibTableColumn
cfprApLsbootBootSecurityRn = _CfprApLsbootBootSecurityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 1, 1, 3),
    _CfprApLsbootBootSecurityRn_Type()
)
cfprApLsbootBootSecurityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootBootSecurityRn.setStatus("current")
_CfprApLsbootBootSecuritySecureBoot_Type = TruthValue
_CfprApLsbootBootSecuritySecureBoot_Object = MibTableColumn
cfprApLsbootBootSecuritySecureBoot = _CfprApLsbootBootSecuritySecureBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 1, 1, 4),
    _CfprApLsbootBootSecuritySecureBoot_Type()
)
cfprApLsbootBootSecuritySecureBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootBootSecuritySecureBoot.setStatus("current")
_CfprApLsbootDefTable_Object = MibTable
cfprApLsbootDefTable = _CfprApLsbootDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2)
)
if mibBuilder.loadTexts:
    cfprApLsbootDefTable.setStatus("current")
_CfprApLsbootDefEntry_Object = MibTableRow
cfprApLsbootDefEntry = _CfprApLsbootDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1)
)
cfprApLsbootDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootDefEntry.setStatus("current")
_CfprApLsbootDefInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootDefInstanceId_Object = MibTableColumn
cfprApLsbootDefInstanceId = _CfprApLsbootDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 1),
    _CfprApLsbootDefInstanceId_Type()
)
cfprApLsbootDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootDefInstanceId.setStatus("current")
_CfprApLsbootDefDn_Type = CfprApManagedObjectDn
_CfprApLsbootDefDn_Object = MibTableColumn
cfprApLsbootDefDn = _CfprApLsbootDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 2),
    _CfprApLsbootDefDn_Type()
)
cfprApLsbootDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefDn.setStatus("current")
_CfprApLsbootDefRn_Type = SnmpAdminString
_CfprApLsbootDefRn_Object = MibTableColumn
cfprApLsbootDefRn = _CfprApLsbootDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 3),
    _CfprApLsbootDefRn_Type()
)
cfprApLsbootDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefRn.setStatus("current")
_CfprApLsbootDefAdvBootOrderApplicable_Type = TruthValue
_CfprApLsbootDefAdvBootOrderApplicable_Object = MibTableColumn
cfprApLsbootDefAdvBootOrderApplicable = _CfprApLsbootDefAdvBootOrderApplicable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 4),
    _CfprApLsbootDefAdvBootOrderApplicable_Type()
)
cfprApLsbootDefAdvBootOrderApplicable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefAdvBootOrderApplicable.setStatus("current")
_CfprApLsbootDefBootMode_Type = CfprApLsbootADefBootMode
_CfprApLsbootDefBootMode_Object = MibTableColumn
cfprApLsbootDefBootMode = _CfprApLsbootDefBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 5),
    _CfprApLsbootDefBootMode_Type()
)
cfprApLsbootDefBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefBootMode.setStatus("current")
_CfprApLsbootDefDescr_Type = SnmpAdminString
_CfprApLsbootDefDescr_Object = MibTableColumn
cfprApLsbootDefDescr = _CfprApLsbootDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 6),
    _CfprApLsbootDefDescr_Type()
)
cfprApLsbootDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefDescr.setStatus("current")
_CfprApLsbootDefEnforceVnicName_Type = TruthValue
_CfprApLsbootDefEnforceVnicName_Object = MibTableColumn
cfprApLsbootDefEnforceVnicName = _CfprApLsbootDefEnforceVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 7),
    _CfprApLsbootDefEnforceVnicName_Type()
)
cfprApLsbootDefEnforceVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefEnforceVnicName.setStatus("current")
_CfprApLsbootDefIntId_Type = SnmpAdminString
_CfprApLsbootDefIntId_Object = MibTableColumn
cfprApLsbootDefIntId = _CfprApLsbootDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 8),
    _CfprApLsbootDefIntId_Type()
)
cfprApLsbootDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefIntId.setStatus("current")
_CfprApLsbootDefName_Type = SnmpAdminString
_CfprApLsbootDefName_Object = MibTableColumn
cfprApLsbootDefName = _CfprApLsbootDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 9),
    _CfprApLsbootDefName_Type()
)
cfprApLsbootDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefName.setStatus("current")
_CfprApLsbootDefPolicyLevel_Type = Gauge32
_CfprApLsbootDefPolicyLevel_Object = MibTableColumn
cfprApLsbootDefPolicyLevel = _CfprApLsbootDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 10),
    _CfprApLsbootDefPolicyLevel_Type()
)
cfprApLsbootDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefPolicyLevel.setStatus("current")
_CfprApLsbootDefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsbootDefPolicyOwner_Object = MibTableColumn
cfprApLsbootDefPolicyOwner = _CfprApLsbootDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 11),
    _CfprApLsbootDefPolicyOwner_Type()
)
cfprApLsbootDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefPolicyOwner.setStatus("current")
_CfprApLsbootDefPurpose_Type = CfprApLsbootPurpose
_CfprApLsbootDefPurpose_Object = MibTableColumn
cfprApLsbootDefPurpose = _CfprApLsbootDefPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 12),
    _CfprApLsbootDefPurpose_Type()
)
cfprApLsbootDefPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefPurpose.setStatus("current")
_CfprApLsbootDefRebootOnUpdate_Type = TruthValue
_CfprApLsbootDefRebootOnUpdate_Object = MibTableColumn
cfprApLsbootDefRebootOnUpdate = _CfprApLsbootDefRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 2, 1, 13),
    _CfprApLsbootDefRebootOnUpdate_Type()
)
cfprApLsbootDefRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefRebootOnUpdate.setStatus("current")
_CfprApLsbootDefaultLocalImageTable_Object = MibTable
cfprApLsbootDefaultLocalImageTable = _CfprApLsbootDefaultLocalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3)
)
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageTable.setStatus("current")
_CfprApLsbootDefaultLocalImageEntry_Object = MibTableRow
cfprApLsbootDefaultLocalImageEntry = _CfprApLsbootDefaultLocalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3, 1)
)
cfprApLsbootDefaultLocalImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootDefaultLocalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageEntry.setStatus("current")
_CfprApLsbootDefaultLocalImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootDefaultLocalImageInstanceId_Object = MibTableColumn
cfprApLsbootDefaultLocalImageInstanceId = _CfprApLsbootDefaultLocalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3, 1, 1),
    _CfprApLsbootDefaultLocalImageInstanceId_Type()
)
cfprApLsbootDefaultLocalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageInstanceId.setStatus("current")
_CfprApLsbootDefaultLocalImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootDefaultLocalImageDn_Object = MibTableColumn
cfprApLsbootDefaultLocalImageDn = _CfprApLsbootDefaultLocalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3, 1, 2),
    _CfprApLsbootDefaultLocalImageDn_Type()
)
cfprApLsbootDefaultLocalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageDn.setStatus("current")
_CfprApLsbootDefaultLocalImageRn_Type = SnmpAdminString
_CfprApLsbootDefaultLocalImageRn_Object = MibTableColumn
cfprApLsbootDefaultLocalImageRn = _CfprApLsbootDefaultLocalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3, 1, 3),
    _CfprApLsbootDefaultLocalImageRn_Type()
)
cfprApLsbootDefaultLocalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageRn.setStatus("current")
_CfprApLsbootDefaultLocalImageOrder_Type = Gauge32
_CfprApLsbootDefaultLocalImageOrder_Object = MibTableColumn
cfprApLsbootDefaultLocalImageOrder = _CfprApLsbootDefaultLocalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3, 1, 4),
    _CfprApLsbootDefaultLocalImageOrder_Type()
)
cfprApLsbootDefaultLocalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageOrder.setStatus("current")
_CfprApLsbootDefaultLocalImageType_Type = CfprApLsbootDefaultLocalImageType
_CfprApLsbootDefaultLocalImageType_Object = MibTableColumn
cfprApLsbootDefaultLocalImageType = _CfprApLsbootDefaultLocalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 3, 1, 5),
    _CfprApLsbootDefaultLocalImageType_Type()
)
cfprApLsbootDefaultLocalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootDefaultLocalImageType.setStatus("current")
_CfprApLsbootIScsiTable_Object = MibTable
cfprApLsbootIScsiTable = _CfprApLsbootIScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4)
)
if mibBuilder.loadTexts:
    cfprApLsbootIScsiTable.setStatus("current")
_CfprApLsbootIScsiEntry_Object = MibTableRow
cfprApLsbootIScsiEntry = _CfprApLsbootIScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1)
)
cfprApLsbootIScsiEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootIScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootIScsiEntry.setStatus("current")
_CfprApLsbootIScsiInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootIScsiInstanceId_Object = MibTableColumn
cfprApLsbootIScsiInstanceId = _CfprApLsbootIScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1, 1),
    _CfprApLsbootIScsiInstanceId_Type()
)
cfprApLsbootIScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiInstanceId.setStatus("current")
_CfprApLsbootIScsiDn_Type = CfprApManagedObjectDn
_CfprApLsbootIScsiDn_Object = MibTableColumn
cfprApLsbootIScsiDn = _CfprApLsbootIScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1, 2),
    _CfprApLsbootIScsiDn_Type()
)
cfprApLsbootIScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiDn.setStatus("current")
_CfprApLsbootIScsiRn_Type = SnmpAdminString
_CfprApLsbootIScsiRn_Object = MibTableColumn
cfprApLsbootIScsiRn = _CfprApLsbootIScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1, 3),
    _CfprApLsbootIScsiRn_Type()
)
cfprApLsbootIScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiRn.setStatus("current")
_CfprApLsbootIScsiAccess_Type = CfprApLsbootIScsiAccess
_CfprApLsbootIScsiAccess_Object = MibTableColumn
cfprApLsbootIScsiAccess = _CfprApLsbootIScsiAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1, 4),
    _CfprApLsbootIScsiAccess_Type()
)
cfprApLsbootIScsiAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiAccess.setStatus("current")
_CfprApLsbootIScsiOrder_Type = Gauge32
_CfprApLsbootIScsiOrder_Object = MibTableColumn
cfprApLsbootIScsiOrder = _CfprApLsbootIScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1, 5),
    _CfprApLsbootIScsiOrder_Type()
)
cfprApLsbootIScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiOrder.setStatus("current")
_CfprApLsbootIScsiType_Type = CfprApLsbootIScsiType
_CfprApLsbootIScsiType_Object = MibTableColumn
cfprApLsbootIScsiType = _CfprApLsbootIScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 4, 1, 6),
    _CfprApLsbootIScsiType_Type()
)
cfprApLsbootIScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiType.setStatus("current")
_CfprApLsbootIScsiImagePathTable_Object = MibTable
cfprApLsbootIScsiImagePathTable = _CfprApLsbootIScsiImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5)
)
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathTable.setStatus("current")
_CfprApLsbootIScsiImagePathEntry_Object = MibTableRow
cfprApLsbootIScsiImagePathEntry = _CfprApLsbootIScsiImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1)
)
cfprApLsbootIScsiImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootIScsiImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathEntry.setStatus("current")
_CfprApLsbootIScsiImagePathInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootIScsiImagePathInstanceId_Object = MibTableColumn
cfprApLsbootIScsiImagePathInstanceId = _CfprApLsbootIScsiImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1, 1),
    _CfprApLsbootIScsiImagePathInstanceId_Type()
)
cfprApLsbootIScsiImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathInstanceId.setStatus("current")
_CfprApLsbootIScsiImagePathDn_Type = CfprApManagedObjectDn
_CfprApLsbootIScsiImagePathDn_Object = MibTableColumn
cfprApLsbootIScsiImagePathDn = _CfprApLsbootIScsiImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1, 2),
    _CfprApLsbootIScsiImagePathDn_Type()
)
cfprApLsbootIScsiImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathDn.setStatus("current")
_CfprApLsbootIScsiImagePathRn_Type = SnmpAdminString
_CfprApLsbootIScsiImagePathRn_Object = MibTableColumn
cfprApLsbootIScsiImagePathRn = _CfprApLsbootIScsiImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1, 3),
    _CfprApLsbootIScsiImagePathRn_Type()
)
cfprApLsbootIScsiImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathRn.setStatus("current")
_CfprApLsbootIScsiImagePathISCSIVnicName_Type = SnmpAdminString
_CfprApLsbootIScsiImagePathISCSIVnicName_Object = MibTableColumn
cfprApLsbootIScsiImagePathISCSIVnicName = _CfprApLsbootIScsiImagePathISCSIVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1, 4),
    _CfprApLsbootIScsiImagePathISCSIVnicName_Type()
)
cfprApLsbootIScsiImagePathISCSIVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathISCSIVnicName.setStatus("current")
_CfprApLsbootIScsiImagePathType_Type = CfprApLsbootIScsiImagePathType
_CfprApLsbootIScsiImagePathType_Object = MibTableColumn
cfprApLsbootIScsiImagePathType = _CfprApLsbootIScsiImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1, 5),
    _CfprApLsbootIScsiImagePathType_Type()
)
cfprApLsbootIScsiImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathType.setStatus("current")
_CfprApLsbootIScsiImagePathVnicName_Type = SnmpAdminString
_CfprApLsbootIScsiImagePathVnicName_Object = MibTableColumn
cfprApLsbootIScsiImagePathVnicName = _CfprApLsbootIScsiImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 5, 1, 6),
    _CfprApLsbootIScsiImagePathVnicName_Type()
)
cfprApLsbootIScsiImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootIScsiImagePathVnicName.setStatus("current")
_CfprApLsbootLanTable_Object = MibTable
cfprApLsbootLanTable = _CfprApLsbootLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6)
)
if mibBuilder.loadTexts:
    cfprApLsbootLanTable.setStatus("current")
_CfprApLsbootLanEntry_Object = MibTableRow
cfprApLsbootLanEntry = _CfprApLsbootLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1)
)
cfprApLsbootLanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootLanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootLanEntry.setStatus("current")
_CfprApLsbootLanInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootLanInstanceId_Object = MibTableColumn
cfprApLsbootLanInstanceId = _CfprApLsbootLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 1),
    _CfprApLsbootLanInstanceId_Type()
)
cfprApLsbootLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootLanInstanceId.setStatus("current")
_CfprApLsbootLanDn_Type = CfprApManagedObjectDn
_CfprApLsbootLanDn_Object = MibTableColumn
cfprApLsbootLanDn = _CfprApLsbootLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 2),
    _CfprApLsbootLanDn_Type()
)
cfprApLsbootLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanDn.setStatus("current")
_CfprApLsbootLanRn_Type = SnmpAdminString
_CfprApLsbootLanRn_Object = MibTableColumn
cfprApLsbootLanRn = _CfprApLsbootLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 3),
    _CfprApLsbootLanRn_Type()
)
cfprApLsbootLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanRn.setStatus("current")
_CfprApLsbootLanAccess_Type = CfprApLsbootLanAccess
_CfprApLsbootLanAccess_Object = MibTableColumn
cfprApLsbootLanAccess = _CfprApLsbootLanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 4),
    _CfprApLsbootLanAccess_Type()
)
cfprApLsbootLanAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanAccess.setStatus("current")
_CfprApLsbootLanOrder_Type = Gauge32
_CfprApLsbootLanOrder_Object = MibTableColumn
cfprApLsbootLanOrder = _CfprApLsbootLanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 5),
    _CfprApLsbootLanOrder_Type()
)
cfprApLsbootLanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanOrder.setStatus("current")
_CfprApLsbootLanProt_Type = CfprApLsbootLanBootProt
_CfprApLsbootLanProt_Object = MibTableColumn
cfprApLsbootLanProt = _CfprApLsbootLanProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 6),
    _CfprApLsbootLanProt_Type()
)
cfprApLsbootLanProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanProt.setStatus("current")
_CfprApLsbootLanType_Type = CfprApLsbootLanType
_CfprApLsbootLanType_Object = MibTableColumn
cfprApLsbootLanType = _CfprApLsbootLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 6, 1, 7),
    _CfprApLsbootLanType_Type()
)
cfprApLsbootLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanType.setStatus("current")
_CfprApLsbootLanImagePathTable_Object = MibTable
cfprApLsbootLanImagePathTable = _CfprApLsbootLanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7)
)
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathTable.setStatus("current")
_CfprApLsbootLanImagePathEntry_Object = MibTableRow
cfprApLsbootLanImagePathEntry = _CfprApLsbootLanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1)
)
cfprApLsbootLanImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootLanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathEntry.setStatus("current")
_CfprApLsbootLanImagePathInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootLanImagePathInstanceId_Object = MibTableColumn
cfprApLsbootLanImagePathInstanceId = _CfprApLsbootLanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 1),
    _CfprApLsbootLanImagePathInstanceId_Type()
)
cfprApLsbootLanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathInstanceId.setStatus("current")
_CfprApLsbootLanImagePathDn_Type = CfprApManagedObjectDn
_CfprApLsbootLanImagePathDn_Object = MibTableColumn
cfprApLsbootLanImagePathDn = _CfprApLsbootLanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 2),
    _CfprApLsbootLanImagePathDn_Type()
)
cfprApLsbootLanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathDn.setStatus("current")
_CfprApLsbootLanImagePathRn_Type = SnmpAdminString
_CfprApLsbootLanImagePathRn_Object = MibTableColumn
cfprApLsbootLanImagePathRn = _CfprApLsbootLanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 3),
    _CfprApLsbootLanImagePathRn_Type()
)
cfprApLsbootLanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathRn.setStatus("current")
_CfprApLsbootLanImagePathBootIpPolicyName_Type = SnmpAdminString
_CfprApLsbootLanImagePathBootIpPolicyName_Object = MibTableColumn
cfprApLsbootLanImagePathBootIpPolicyName = _CfprApLsbootLanImagePathBootIpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 4),
    _CfprApLsbootLanImagePathBootIpPolicyName_Type()
)
cfprApLsbootLanImagePathBootIpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathBootIpPolicyName.setStatus("current")
_CfprApLsbootLanImagePathISCSIVnicName_Type = SnmpAdminString
_CfprApLsbootLanImagePathISCSIVnicName_Object = MibTableColumn
cfprApLsbootLanImagePathISCSIVnicName = _CfprApLsbootLanImagePathISCSIVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 5),
    _CfprApLsbootLanImagePathISCSIVnicName_Type()
)
cfprApLsbootLanImagePathISCSIVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathISCSIVnicName.setStatus("current")
_CfprApLsbootLanImagePathImgPolicyName_Type = SnmpAdminString
_CfprApLsbootLanImagePathImgPolicyName_Object = MibTableColumn
cfprApLsbootLanImagePathImgPolicyName = _CfprApLsbootLanImagePathImgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 6),
    _CfprApLsbootLanImagePathImgPolicyName_Type()
)
cfprApLsbootLanImagePathImgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathImgPolicyName.setStatus("current")
_CfprApLsbootLanImagePathImgSecPolicyName_Type = SnmpAdminString
_CfprApLsbootLanImagePathImgSecPolicyName_Object = MibTableColumn
cfprApLsbootLanImagePathImgSecPolicyName = _CfprApLsbootLanImagePathImgSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 7),
    _CfprApLsbootLanImagePathImgSecPolicyName_Type()
)
cfprApLsbootLanImagePathImgSecPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathImgSecPolicyName.setStatus("current")
_CfprApLsbootLanImagePathProvSrvPolicyName_Type = SnmpAdminString
_CfprApLsbootLanImagePathProvSrvPolicyName_Object = MibTableColumn
cfprApLsbootLanImagePathProvSrvPolicyName = _CfprApLsbootLanImagePathProvSrvPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 8),
    _CfprApLsbootLanImagePathProvSrvPolicyName_Type()
)
cfprApLsbootLanImagePathProvSrvPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathProvSrvPolicyName.setStatus("current")
_CfprApLsbootLanImagePathType_Type = CfprApLsbootLanImagePathType
_CfprApLsbootLanImagePathType_Object = MibTableColumn
cfprApLsbootLanImagePathType = _CfprApLsbootLanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 9),
    _CfprApLsbootLanImagePathType_Type()
)
cfprApLsbootLanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathType.setStatus("current")
_CfprApLsbootLanImagePathVnicName_Type = SnmpAdminString
_CfprApLsbootLanImagePathVnicName_Object = MibTableColumn
cfprApLsbootLanImagePathVnicName = _CfprApLsbootLanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 7, 1, 10),
    _CfprApLsbootLanImagePathVnicName_Type()
)
cfprApLsbootLanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLanImagePathVnicName.setStatus("current")
_CfprApLsbootLocalHddImageTable_Object = MibTable
cfprApLsbootLocalHddImageTable = _CfprApLsbootLocalHddImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8)
)
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageTable.setStatus("current")
_CfprApLsbootLocalHddImageEntry_Object = MibTableRow
cfprApLsbootLocalHddImageEntry = _CfprApLsbootLocalHddImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8, 1)
)
cfprApLsbootLocalHddImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootLocalHddImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageEntry.setStatus("current")
_CfprApLsbootLocalHddImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootLocalHddImageInstanceId_Object = MibTableColumn
cfprApLsbootLocalHddImageInstanceId = _CfprApLsbootLocalHddImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8, 1, 1),
    _CfprApLsbootLocalHddImageInstanceId_Type()
)
cfprApLsbootLocalHddImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageInstanceId.setStatus("current")
_CfprApLsbootLocalHddImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootLocalHddImageDn_Object = MibTableColumn
cfprApLsbootLocalHddImageDn = _CfprApLsbootLocalHddImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8, 1, 2),
    _CfprApLsbootLocalHddImageDn_Type()
)
cfprApLsbootLocalHddImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageDn.setStatus("current")
_CfprApLsbootLocalHddImageRn_Type = SnmpAdminString
_CfprApLsbootLocalHddImageRn_Object = MibTableColumn
cfprApLsbootLocalHddImageRn = _CfprApLsbootLocalHddImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8, 1, 3),
    _CfprApLsbootLocalHddImageRn_Type()
)
cfprApLsbootLocalHddImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageRn.setStatus("current")
_CfprApLsbootLocalHddImageOrder_Type = Gauge32
_CfprApLsbootLocalHddImageOrder_Object = MibTableColumn
cfprApLsbootLocalHddImageOrder = _CfprApLsbootLocalHddImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8, 1, 4),
    _CfprApLsbootLocalHddImageOrder_Type()
)
cfprApLsbootLocalHddImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageOrder.setStatus("current")
_CfprApLsbootLocalHddImageType_Type = CfprApLsbootLocalHddImageType
_CfprApLsbootLocalHddImageType_Object = MibTableColumn
cfprApLsbootLocalHddImageType = _CfprApLsbootLocalHddImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 8, 1, 5),
    _CfprApLsbootLocalHddImageType_Type()
)
cfprApLsbootLocalHddImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLocalHddImageType.setStatus("current")
_CfprApLsbootLocalStorageTable_Object = MibTable
cfprApLsbootLocalStorageTable = _CfprApLsbootLocalStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 9)
)
if mibBuilder.loadTexts:
    cfprApLsbootLocalStorageTable.setStatus("current")
_CfprApLsbootLocalStorageEntry_Object = MibTableRow
cfprApLsbootLocalStorageEntry = _CfprApLsbootLocalStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 9, 1)
)
cfprApLsbootLocalStorageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootLocalStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootLocalStorageEntry.setStatus("current")
_CfprApLsbootLocalStorageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootLocalStorageInstanceId_Object = MibTableColumn
cfprApLsbootLocalStorageInstanceId = _CfprApLsbootLocalStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 9, 1, 1),
    _CfprApLsbootLocalStorageInstanceId_Type()
)
cfprApLsbootLocalStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootLocalStorageInstanceId.setStatus("current")
_CfprApLsbootLocalStorageDn_Type = CfprApManagedObjectDn
_CfprApLsbootLocalStorageDn_Object = MibTableColumn
cfprApLsbootLocalStorageDn = _CfprApLsbootLocalStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 9, 1, 2),
    _CfprApLsbootLocalStorageDn_Type()
)
cfprApLsbootLocalStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLocalStorageDn.setStatus("current")
_CfprApLsbootLocalStorageRn_Type = SnmpAdminString
_CfprApLsbootLocalStorageRn_Object = MibTableColumn
cfprApLsbootLocalStorageRn = _CfprApLsbootLocalStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 9, 1, 3),
    _CfprApLsbootLocalStorageRn_Type()
)
cfprApLsbootLocalStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootLocalStorageRn.setStatus("current")
_CfprApLsbootPolicyTable_Object = MibTable
cfprApLsbootPolicyTable = _CfprApLsbootPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10)
)
if mibBuilder.loadTexts:
    cfprApLsbootPolicyTable.setStatus("current")
_CfprApLsbootPolicyEntry_Object = MibTableRow
cfprApLsbootPolicyEntry = _CfprApLsbootPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1)
)
cfprApLsbootPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootPolicyEntry.setStatus("current")
_CfprApLsbootPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootPolicyInstanceId_Object = MibTableColumn
cfprApLsbootPolicyInstanceId = _CfprApLsbootPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 1),
    _CfprApLsbootPolicyInstanceId_Type()
)
cfprApLsbootPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyInstanceId.setStatus("current")
_CfprApLsbootPolicyDn_Type = CfprApManagedObjectDn
_CfprApLsbootPolicyDn_Object = MibTableColumn
cfprApLsbootPolicyDn = _CfprApLsbootPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 2),
    _CfprApLsbootPolicyDn_Type()
)
cfprApLsbootPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyDn.setStatus("current")
_CfprApLsbootPolicyRn_Type = SnmpAdminString
_CfprApLsbootPolicyRn_Object = MibTableColumn
cfprApLsbootPolicyRn = _CfprApLsbootPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 3),
    _CfprApLsbootPolicyRn_Type()
)
cfprApLsbootPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyRn.setStatus("current")
_CfprApLsbootPolicyBootMode_Type = CfprApLsbootADefBootMode
_CfprApLsbootPolicyBootMode_Object = MibTableColumn
cfprApLsbootPolicyBootMode = _CfprApLsbootPolicyBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 4),
    _CfprApLsbootPolicyBootMode_Type()
)
cfprApLsbootPolicyBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyBootMode.setStatus("current")
_CfprApLsbootPolicyDescr_Type = SnmpAdminString
_CfprApLsbootPolicyDescr_Object = MibTableColumn
cfprApLsbootPolicyDescr = _CfprApLsbootPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 5),
    _CfprApLsbootPolicyDescr_Type()
)
cfprApLsbootPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyDescr.setStatus("current")
_CfprApLsbootPolicyEnforceVnicName_Type = TruthValue
_CfprApLsbootPolicyEnforceVnicName_Object = MibTableColumn
cfprApLsbootPolicyEnforceVnicName = _CfprApLsbootPolicyEnforceVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 6),
    _CfprApLsbootPolicyEnforceVnicName_Type()
)
cfprApLsbootPolicyEnforceVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyEnforceVnicName.setStatus("current")
_CfprApLsbootPolicyIntId_Type = SnmpAdminString
_CfprApLsbootPolicyIntId_Object = MibTableColumn
cfprApLsbootPolicyIntId = _CfprApLsbootPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 7),
    _CfprApLsbootPolicyIntId_Type()
)
cfprApLsbootPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyIntId.setStatus("current")
_CfprApLsbootPolicyName_Type = SnmpAdminString
_CfprApLsbootPolicyName_Object = MibTableColumn
cfprApLsbootPolicyName = _CfprApLsbootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 8),
    _CfprApLsbootPolicyName_Type()
)
cfprApLsbootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyName.setStatus("current")
_CfprApLsbootPolicyPolicyLevel_Type = Gauge32
_CfprApLsbootPolicyPolicyLevel_Object = MibTableColumn
cfprApLsbootPolicyPolicyLevel = _CfprApLsbootPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 9),
    _CfprApLsbootPolicyPolicyLevel_Type()
)
cfprApLsbootPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyPolicyLevel.setStatus("current")
_CfprApLsbootPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsbootPolicyPolicyOwner_Object = MibTableColumn
cfprApLsbootPolicyPolicyOwner = _CfprApLsbootPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 10),
    _CfprApLsbootPolicyPolicyOwner_Type()
)
cfprApLsbootPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyPolicyOwner.setStatus("current")
_CfprApLsbootPolicyPurpose_Type = CfprApLsbootPurpose
_CfprApLsbootPolicyPurpose_Object = MibTableColumn
cfprApLsbootPolicyPurpose = _CfprApLsbootPolicyPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 11),
    _CfprApLsbootPolicyPurpose_Type()
)
cfprApLsbootPolicyPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyPurpose.setStatus("current")
_CfprApLsbootPolicyRebootOnUpdate_Type = TruthValue
_CfprApLsbootPolicyRebootOnUpdate_Object = MibTableColumn
cfprApLsbootPolicyRebootOnUpdate = _CfprApLsbootPolicyRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 10, 1, 12),
    _CfprApLsbootPolicyRebootOnUpdate_Type()
)
cfprApLsbootPolicyRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootPolicyRebootOnUpdate.setStatus("current")
_CfprApLsbootSanTable_Object = MibTable
cfprApLsbootSanTable = _CfprApLsbootSanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11)
)
if mibBuilder.loadTexts:
    cfprApLsbootSanTable.setStatus("current")
_CfprApLsbootSanEntry_Object = MibTableRow
cfprApLsbootSanEntry = _CfprApLsbootSanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1)
)
cfprApLsbootSanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootSanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootSanEntry.setStatus("current")
_CfprApLsbootSanInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootSanInstanceId_Object = MibTableColumn
cfprApLsbootSanInstanceId = _CfprApLsbootSanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1, 1),
    _CfprApLsbootSanInstanceId_Type()
)
cfprApLsbootSanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootSanInstanceId.setStatus("current")
_CfprApLsbootSanDn_Type = CfprApManagedObjectDn
_CfprApLsbootSanDn_Object = MibTableColumn
cfprApLsbootSanDn = _CfprApLsbootSanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1, 2),
    _CfprApLsbootSanDn_Type()
)
cfprApLsbootSanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanDn.setStatus("current")
_CfprApLsbootSanRn_Type = SnmpAdminString
_CfprApLsbootSanRn_Object = MibTableColumn
cfprApLsbootSanRn = _CfprApLsbootSanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1, 3),
    _CfprApLsbootSanRn_Type()
)
cfprApLsbootSanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanRn.setStatus("current")
_CfprApLsbootSanAccess_Type = CfprApLsbootSanAccess
_CfprApLsbootSanAccess_Object = MibTableColumn
cfprApLsbootSanAccess = _CfprApLsbootSanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1, 4),
    _CfprApLsbootSanAccess_Type()
)
cfprApLsbootSanAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanAccess.setStatus("current")
_CfprApLsbootSanOrder_Type = Gauge32
_CfprApLsbootSanOrder_Object = MibTableColumn
cfprApLsbootSanOrder = _CfprApLsbootSanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1, 5),
    _CfprApLsbootSanOrder_Type()
)
cfprApLsbootSanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanOrder.setStatus("current")
_CfprApLsbootSanType_Type = CfprApLsbootSanType
_CfprApLsbootSanType_Object = MibTableColumn
cfprApLsbootSanType = _CfprApLsbootSanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 11, 1, 6),
    _CfprApLsbootSanType_Type()
)
cfprApLsbootSanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanType.setStatus("current")
_CfprApLsbootSanCatSanImageTable_Object = MibTable
cfprApLsbootSanCatSanImageTable = _CfprApLsbootSanCatSanImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12)
)
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageTable.setStatus("current")
_CfprApLsbootSanCatSanImageEntry_Object = MibTableRow
cfprApLsbootSanCatSanImageEntry = _CfprApLsbootSanCatSanImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12, 1)
)
cfprApLsbootSanCatSanImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootSanCatSanImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageEntry.setStatus("current")
_CfprApLsbootSanCatSanImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootSanCatSanImageInstanceId_Object = MibTableColumn
cfprApLsbootSanCatSanImageInstanceId = _CfprApLsbootSanCatSanImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12, 1, 1),
    _CfprApLsbootSanCatSanImageInstanceId_Type()
)
cfprApLsbootSanCatSanImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageInstanceId.setStatus("current")
_CfprApLsbootSanCatSanImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootSanCatSanImageDn_Object = MibTableColumn
cfprApLsbootSanCatSanImageDn = _CfprApLsbootSanCatSanImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12, 1, 2),
    _CfprApLsbootSanCatSanImageDn_Type()
)
cfprApLsbootSanCatSanImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageDn.setStatus("current")
_CfprApLsbootSanCatSanImageRn_Type = SnmpAdminString
_CfprApLsbootSanCatSanImageRn_Object = MibTableColumn
cfprApLsbootSanCatSanImageRn = _CfprApLsbootSanCatSanImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12, 1, 3),
    _CfprApLsbootSanCatSanImageRn_Type()
)
cfprApLsbootSanCatSanImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageRn.setStatus("current")
_CfprApLsbootSanCatSanImageType_Type = CfprApLsbootSanCatSanImageType
_CfprApLsbootSanCatSanImageType_Object = MibTableColumn
cfprApLsbootSanCatSanImageType = _CfprApLsbootSanCatSanImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12, 1, 4),
    _CfprApLsbootSanCatSanImageType_Type()
)
cfprApLsbootSanCatSanImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageType.setStatus("current")
_CfprApLsbootSanCatSanImageVnicName_Type = SnmpAdminString
_CfprApLsbootSanCatSanImageVnicName_Object = MibTableColumn
cfprApLsbootSanCatSanImageVnicName = _CfprApLsbootSanCatSanImageVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 12, 1, 5),
    _CfprApLsbootSanCatSanImageVnicName_Type()
)
cfprApLsbootSanCatSanImageVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImageVnicName.setStatus("current")
_CfprApLsbootSanCatSanImagePathTable_Object = MibTable
cfprApLsbootSanCatSanImagePathTable = _CfprApLsbootSanCatSanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13)
)
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathTable.setStatus("current")
_CfprApLsbootSanCatSanImagePathEntry_Object = MibTableRow
cfprApLsbootSanCatSanImagePathEntry = _CfprApLsbootSanCatSanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1)
)
cfprApLsbootSanCatSanImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootSanCatSanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathEntry.setStatus("current")
_CfprApLsbootSanCatSanImagePathInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootSanCatSanImagePathInstanceId_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathInstanceId = _CfprApLsbootSanCatSanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 1),
    _CfprApLsbootSanCatSanImagePathInstanceId_Type()
)
cfprApLsbootSanCatSanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathInstanceId.setStatus("current")
_CfprApLsbootSanCatSanImagePathDn_Type = CfprApManagedObjectDn
_CfprApLsbootSanCatSanImagePathDn_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathDn = _CfprApLsbootSanCatSanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 2),
    _CfprApLsbootSanCatSanImagePathDn_Type()
)
cfprApLsbootSanCatSanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathDn.setStatus("current")
_CfprApLsbootSanCatSanImagePathRn_Type = SnmpAdminString
_CfprApLsbootSanCatSanImagePathRn_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathRn = _CfprApLsbootSanCatSanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 3),
    _CfprApLsbootSanCatSanImagePathRn_Type()
)
cfprApLsbootSanCatSanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathRn.setStatus("current")
_CfprApLsbootSanCatSanImagePathLun_Type = SnmpAdminString
_CfprApLsbootSanCatSanImagePathLun_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathLun = _CfprApLsbootSanCatSanImagePathLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 4),
    _CfprApLsbootSanCatSanImagePathLun_Type()
)
cfprApLsbootSanCatSanImagePathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathLun.setStatus("current")
_CfprApLsbootSanCatSanImagePathType_Type = CfprApLsbootSanCatSanImagePathType
_CfprApLsbootSanCatSanImagePathType_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathType = _CfprApLsbootSanCatSanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 5),
    _CfprApLsbootSanCatSanImagePathType_Type()
)
cfprApLsbootSanCatSanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathType.setStatus("current")
_CfprApLsbootSanCatSanImagePathVnicName_Type = SnmpAdminString
_CfprApLsbootSanCatSanImagePathVnicName_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathVnicName = _CfprApLsbootSanCatSanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 6),
    _CfprApLsbootSanCatSanImagePathVnicName_Type()
)
cfprApLsbootSanCatSanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathVnicName.setStatus("current")
_CfprApLsbootSanCatSanImagePathWwn_Type = Unsigned64
_CfprApLsbootSanCatSanImagePathWwn_Object = MibTableColumn
cfprApLsbootSanCatSanImagePathWwn = _CfprApLsbootSanCatSanImagePathWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 13, 1, 7),
    _CfprApLsbootSanCatSanImagePathWwn_Type()
)
cfprApLsbootSanCatSanImagePathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanCatSanImagePathWwn.setStatus("current")
_CfprApLsbootSanImageTable_Object = MibTable
cfprApLsbootSanImageTable = _CfprApLsbootSanImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14)
)
if mibBuilder.loadTexts:
    cfprApLsbootSanImageTable.setStatus("current")
_CfprApLsbootSanImageEntry_Object = MibTableRow
cfprApLsbootSanImageEntry = _CfprApLsbootSanImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14, 1)
)
cfprApLsbootSanImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootSanImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootSanImageEntry.setStatus("current")
_CfprApLsbootSanImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootSanImageInstanceId_Object = MibTableColumn
cfprApLsbootSanImageInstanceId = _CfprApLsbootSanImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14, 1, 1),
    _CfprApLsbootSanImageInstanceId_Type()
)
cfprApLsbootSanImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootSanImageInstanceId.setStatus("current")
_CfprApLsbootSanImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootSanImageDn_Object = MibTableColumn
cfprApLsbootSanImageDn = _CfprApLsbootSanImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14, 1, 2),
    _CfprApLsbootSanImageDn_Type()
)
cfprApLsbootSanImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImageDn.setStatus("current")
_CfprApLsbootSanImageRn_Type = SnmpAdminString
_CfprApLsbootSanImageRn_Object = MibTableColumn
cfprApLsbootSanImageRn = _CfprApLsbootSanImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14, 1, 3),
    _CfprApLsbootSanImageRn_Type()
)
cfprApLsbootSanImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImageRn.setStatus("current")
_CfprApLsbootSanImageType_Type = CfprApLsbootSanImageType
_CfprApLsbootSanImageType_Object = MibTableColumn
cfprApLsbootSanImageType = _CfprApLsbootSanImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14, 1, 4),
    _CfprApLsbootSanImageType_Type()
)
cfprApLsbootSanImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImageType.setStatus("current")
_CfprApLsbootSanImageVnicName_Type = SnmpAdminString
_CfprApLsbootSanImageVnicName_Object = MibTableColumn
cfprApLsbootSanImageVnicName = _CfprApLsbootSanImageVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 14, 1, 5),
    _CfprApLsbootSanImageVnicName_Type()
)
cfprApLsbootSanImageVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImageVnicName.setStatus("current")
_CfprApLsbootSanImagePathTable_Object = MibTable
cfprApLsbootSanImagePathTable = _CfprApLsbootSanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15)
)
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathTable.setStatus("current")
_CfprApLsbootSanImagePathEntry_Object = MibTableRow
cfprApLsbootSanImagePathEntry = _CfprApLsbootSanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1)
)
cfprApLsbootSanImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootSanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathEntry.setStatus("current")
_CfprApLsbootSanImagePathInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootSanImagePathInstanceId_Object = MibTableColumn
cfprApLsbootSanImagePathInstanceId = _CfprApLsbootSanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 1),
    _CfprApLsbootSanImagePathInstanceId_Type()
)
cfprApLsbootSanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathInstanceId.setStatus("current")
_CfprApLsbootSanImagePathDn_Type = CfprApManagedObjectDn
_CfprApLsbootSanImagePathDn_Object = MibTableColumn
cfprApLsbootSanImagePathDn = _CfprApLsbootSanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 2),
    _CfprApLsbootSanImagePathDn_Type()
)
cfprApLsbootSanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathDn.setStatus("current")
_CfprApLsbootSanImagePathRn_Type = SnmpAdminString
_CfprApLsbootSanImagePathRn_Object = MibTableColumn
cfprApLsbootSanImagePathRn = _CfprApLsbootSanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 3),
    _CfprApLsbootSanImagePathRn_Type()
)
cfprApLsbootSanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathRn.setStatus("current")
_CfprApLsbootSanImagePathLun_Type = SnmpAdminString
_CfprApLsbootSanImagePathLun_Object = MibTableColumn
cfprApLsbootSanImagePathLun = _CfprApLsbootSanImagePathLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 4),
    _CfprApLsbootSanImagePathLun_Type()
)
cfprApLsbootSanImagePathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathLun.setStatus("current")
_CfprApLsbootSanImagePathType_Type = CfprApLsbootSanImagePathType
_CfprApLsbootSanImagePathType_Object = MibTableColumn
cfprApLsbootSanImagePathType = _CfprApLsbootSanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 5),
    _CfprApLsbootSanImagePathType_Type()
)
cfprApLsbootSanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathType.setStatus("current")
_CfprApLsbootSanImagePathVnicName_Type = SnmpAdminString
_CfprApLsbootSanImagePathVnicName_Object = MibTableColumn
cfprApLsbootSanImagePathVnicName = _CfprApLsbootSanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 6),
    _CfprApLsbootSanImagePathVnicName_Type()
)
cfprApLsbootSanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathVnicName.setStatus("current")
_CfprApLsbootSanImagePathWwn_Type = Unsigned64
_CfprApLsbootSanImagePathWwn_Object = MibTableColumn
cfprApLsbootSanImagePathWwn = _CfprApLsbootSanImagePathWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 15, 1, 7),
    _CfprApLsbootSanImagePathWwn_Type()
)
cfprApLsbootSanImagePathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootSanImagePathWwn.setStatus("current")
_CfprApLsbootStorageTable_Object = MibTable
cfprApLsbootStorageTable = _CfprApLsbootStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16)
)
if mibBuilder.loadTexts:
    cfprApLsbootStorageTable.setStatus("current")
_CfprApLsbootStorageEntry_Object = MibTableRow
cfprApLsbootStorageEntry = _CfprApLsbootStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1)
)
cfprApLsbootStorageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootStorageEntry.setStatus("current")
_CfprApLsbootStorageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootStorageInstanceId_Object = MibTableColumn
cfprApLsbootStorageInstanceId = _CfprApLsbootStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1, 1),
    _CfprApLsbootStorageInstanceId_Type()
)
cfprApLsbootStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootStorageInstanceId.setStatus("current")
_CfprApLsbootStorageDn_Type = CfprApManagedObjectDn
_CfprApLsbootStorageDn_Object = MibTableColumn
cfprApLsbootStorageDn = _CfprApLsbootStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1, 2),
    _CfprApLsbootStorageDn_Type()
)
cfprApLsbootStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootStorageDn.setStatus("current")
_CfprApLsbootStorageRn_Type = SnmpAdminString
_CfprApLsbootStorageRn_Object = MibTableColumn
cfprApLsbootStorageRn = _CfprApLsbootStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1, 3),
    _CfprApLsbootStorageRn_Type()
)
cfprApLsbootStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootStorageRn.setStatus("current")
_CfprApLsbootStorageAccess_Type = CfprApLsbootStorageAccess
_CfprApLsbootStorageAccess_Object = MibTableColumn
cfprApLsbootStorageAccess = _CfprApLsbootStorageAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1, 4),
    _CfprApLsbootStorageAccess_Type()
)
cfprApLsbootStorageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootStorageAccess.setStatus("current")
_CfprApLsbootStorageOrder_Type = Gauge32
_CfprApLsbootStorageOrder_Object = MibTableColumn
cfprApLsbootStorageOrder = _CfprApLsbootStorageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1, 5),
    _CfprApLsbootStorageOrder_Type()
)
cfprApLsbootStorageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootStorageOrder.setStatus("current")
_CfprApLsbootStorageType_Type = CfprApLsbootStorageType
_CfprApLsbootStorageType_Object = MibTableColumn
cfprApLsbootStorageType = _CfprApLsbootStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 16, 1, 6),
    _CfprApLsbootStorageType_Type()
)
cfprApLsbootStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootStorageType.setStatus("current")
_CfprApLsbootUsbExternalImageTable_Object = MibTable
cfprApLsbootUsbExternalImageTable = _CfprApLsbootUsbExternalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17)
)
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageTable.setStatus("current")
_CfprApLsbootUsbExternalImageEntry_Object = MibTableRow
cfprApLsbootUsbExternalImageEntry = _CfprApLsbootUsbExternalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17, 1)
)
cfprApLsbootUsbExternalImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootUsbExternalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageEntry.setStatus("current")
_CfprApLsbootUsbExternalImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootUsbExternalImageInstanceId_Object = MibTableColumn
cfprApLsbootUsbExternalImageInstanceId = _CfprApLsbootUsbExternalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17, 1, 1),
    _CfprApLsbootUsbExternalImageInstanceId_Type()
)
cfprApLsbootUsbExternalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageInstanceId.setStatus("current")
_CfprApLsbootUsbExternalImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootUsbExternalImageDn_Object = MibTableColumn
cfprApLsbootUsbExternalImageDn = _CfprApLsbootUsbExternalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17, 1, 2),
    _CfprApLsbootUsbExternalImageDn_Type()
)
cfprApLsbootUsbExternalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageDn.setStatus("current")
_CfprApLsbootUsbExternalImageRn_Type = SnmpAdminString
_CfprApLsbootUsbExternalImageRn_Object = MibTableColumn
cfprApLsbootUsbExternalImageRn = _CfprApLsbootUsbExternalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17, 1, 3),
    _CfprApLsbootUsbExternalImageRn_Type()
)
cfprApLsbootUsbExternalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageRn.setStatus("current")
_CfprApLsbootUsbExternalImageOrder_Type = Gauge32
_CfprApLsbootUsbExternalImageOrder_Object = MibTableColumn
cfprApLsbootUsbExternalImageOrder = _CfprApLsbootUsbExternalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17, 1, 4),
    _CfprApLsbootUsbExternalImageOrder_Type()
)
cfprApLsbootUsbExternalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageOrder.setStatus("current")
_CfprApLsbootUsbExternalImageType_Type = CfprApLsbootUsbExternalImageType
_CfprApLsbootUsbExternalImageType_Object = MibTableColumn
cfprApLsbootUsbExternalImageType = _CfprApLsbootUsbExternalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 17, 1, 5),
    _CfprApLsbootUsbExternalImageType_Type()
)
cfprApLsbootUsbExternalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbExternalImageType.setStatus("current")
_CfprApLsbootUsbFlashStorageImageTable_Object = MibTable
cfprApLsbootUsbFlashStorageImageTable = _CfprApLsbootUsbFlashStorageImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18)
)
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageTable.setStatus("current")
_CfprApLsbootUsbFlashStorageImageEntry_Object = MibTableRow
cfprApLsbootUsbFlashStorageImageEntry = _CfprApLsbootUsbFlashStorageImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18, 1)
)
cfprApLsbootUsbFlashStorageImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootUsbFlashStorageImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageEntry.setStatus("current")
_CfprApLsbootUsbFlashStorageImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootUsbFlashStorageImageInstanceId_Object = MibTableColumn
cfprApLsbootUsbFlashStorageImageInstanceId = _CfprApLsbootUsbFlashStorageImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18, 1, 1),
    _CfprApLsbootUsbFlashStorageImageInstanceId_Type()
)
cfprApLsbootUsbFlashStorageImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageInstanceId.setStatus("current")
_CfprApLsbootUsbFlashStorageImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootUsbFlashStorageImageDn_Object = MibTableColumn
cfprApLsbootUsbFlashStorageImageDn = _CfprApLsbootUsbFlashStorageImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18, 1, 2),
    _CfprApLsbootUsbFlashStorageImageDn_Type()
)
cfprApLsbootUsbFlashStorageImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageDn.setStatus("current")
_CfprApLsbootUsbFlashStorageImageRn_Type = SnmpAdminString
_CfprApLsbootUsbFlashStorageImageRn_Object = MibTableColumn
cfprApLsbootUsbFlashStorageImageRn = _CfprApLsbootUsbFlashStorageImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18, 1, 3),
    _CfprApLsbootUsbFlashStorageImageRn_Type()
)
cfprApLsbootUsbFlashStorageImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageRn.setStatus("current")
_CfprApLsbootUsbFlashStorageImageOrder_Type = Gauge32
_CfprApLsbootUsbFlashStorageImageOrder_Object = MibTableColumn
cfprApLsbootUsbFlashStorageImageOrder = _CfprApLsbootUsbFlashStorageImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18, 1, 4),
    _CfprApLsbootUsbFlashStorageImageOrder_Type()
)
cfprApLsbootUsbFlashStorageImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageOrder.setStatus("current")
_CfprApLsbootUsbFlashStorageImageType_Type = CfprApLsbootUsbFlashStorageImageType
_CfprApLsbootUsbFlashStorageImageType_Object = MibTableColumn
cfprApLsbootUsbFlashStorageImageType = _CfprApLsbootUsbFlashStorageImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 18, 1, 5),
    _CfprApLsbootUsbFlashStorageImageType_Type()
)
cfprApLsbootUsbFlashStorageImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbFlashStorageImageType.setStatus("current")
_CfprApLsbootUsbInternalImageTable_Object = MibTable
cfprApLsbootUsbInternalImageTable = _CfprApLsbootUsbInternalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19)
)
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageTable.setStatus("current")
_CfprApLsbootUsbInternalImageEntry_Object = MibTableRow
cfprApLsbootUsbInternalImageEntry = _CfprApLsbootUsbInternalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19, 1)
)
cfprApLsbootUsbInternalImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootUsbInternalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageEntry.setStatus("current")
_CfprApLsbootUsbInternalImageInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootUsbInternalImageInstanceId_Object = MibTableColumn
cfprApLsbootUsbInternalImageInstanceId = _CfprApLsbootUsbInternalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19, 1, 1),
    _CfprApLsbootUsbInternalImageInstanceId_Type()
)
cfprApLsbootUsbInternalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageInstanceId.setStatus("current")
_CfprApLsbootUsbInternalImageDn_Type = CfprApManagedObjectDn
_CfprApLsbootUsbInternalImageDn_Object = MibTableColumn
cfprApLsbootUsbInternalImageDn = _CfprApLsbootUsbInternalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19, 1, 2),
    _CfprApLsbootUsbInternalImageDn_Type()
)
cfprApLsbootUsbInternalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageDn.setStatus("current")
_CfprApLsbootUsbInternalImageRn_Type = SnmpAdminString
_CfprApLsbootUsbInternalImageRn_Object = MibTableColumn
cfprApLsbootUsbInternalImageRn = _CfprApLsbootUsbInternalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19, 1, 3),
    _CfprApLsbootUsbInternalImageRn_Type()
)
cfprApLsbootUsbInternalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageRn.setStatus("current")
_CfprApLsbootUsbInternalImageOrder_Type = Gauge32
_CfprApLsbootUsbInternalImageOrder_Object = MibTableColumn
cfprApLsbootUsbInternalImageOrder = _CfprApLsbootUsbInternalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19, 1, 4),
    _CfprApLsbootUsbInternalImageOrder_Type()
)
cfprApLsbootUsbInternalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageOrder.setStatus("current")
_CfprApLsbootUsbInternalImageType_Type = CfprApLsbootUsbInternalImageType
_CfprApLsbootUsbInternalImageType_Object = MibTableColumn
cfprApLsbootUsbInternalImageType = _CfprApLsbootUsbInternalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 19, 1, 5),
    _CfprApLsbootUsbInternalImageType_Type()
)
cfprApLsbootUsbInternalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootUsbInternalImageType.setStatus("current")
_CfprApLsbootVirtualMediaTable_Object = MibTable
cfprApLsbootVirtualMediaTable = _CfprApLsbootVirtualMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20)
)
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaTable.setStatus("current")
_CfprApLsbootVirtualMediaEntry_Object = MibTableRow
cfprApLsbootVirtualMediaEntry = _CfprApLsbootVirtualMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1)
)
cfprApLsbootVirtualMediaEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSBOOT-MIB", "cfprApLsbootVirtualMediaInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaEntry.setStatus("current")
_CfprApLsbootVirtualMediaInstanceId_Type = CfprApManagedObjectId
_CfprApLsbootVirtualMediaInstanceId_Object = MibTableColumn
cfprApLsbootVirtualMediaInstanceId = _CfprApLsbootVirtualMediaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 1),
    _CfprApLsbootVirtualMediaInstanceId_Type()
)
cfprApLsbootVirtualMediaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaInstanceId.setStatus("current")
_CfprApLsbootVirtualMediaDn_Type = CfprApManagedObjectDn
_CfprApLsbootVirtualMediaDn_Object = MibTableColumn
cfprApLsbootVirtualMediaDn = _CfprApLsbootVirtualMediaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 2),
    _CfprApLsbootVirtualMediaDn_Type()
)
cfprApLsbootVirtualMediaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaDn.setStatus("current")
_CfprApLsbootVirtualMediaRn_Type = SnmpAdminString
_CfprApLsbootVirtualMediaRn_Object = MibTableColumn
cfprApLsbootVirtualMediaRn = _CfprApLsbootVirtualMediaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 3),
    _CfprApLsbootVirtualMediaRn_Type()
)
cfprApLsbootVirtualMediaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaRn.setStatus("current")
_CfprApLsbootVirtualMediaAccess_Type = CfprApLsbootAccessType
_CfprApLsbootVirtualMediaAccess_Object = MibTableColumn
cfprApLsbootVirtualMediaAccess = _CfprApLsbootVirtualMediaAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 4),
    _CfprApLsbootVirtualMediaAccess_Type()
)
cfprApLsbootVirtualMediaAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaAccess.setStatus("current")
_CfprApLsbootVirtualMediaLunId_Type = SnmpAdminString
_CfprApLsbootVirtualMediaLunId_Object = MibTableColumn
cfprApLsbootVirtualMediaLunId = _CfprApLsbootVirtualMediaLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 5),
    _CfprApLsbootVirtualMediaLunId_Type()
)
cfprApLsbootVirtualMediaLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaLunId.setStatus("current")
_CfprApLsbootVirtualMediaMappingName_Type = SnmpAdminString
_CfprApLsbootVirtualMediaMappingName_Object = MibTableColumn
cfprApLsbootVirtualMediaMappingName = _CfprApLsbootVirtualMediaMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 6),
    _CfprApLsbootVirtualMediaMappingName_Type()
)
cfprApLsbootVirtualMediaMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaMappingName.setStatus("current")
_CfprApLsbootVirtualMediaOrder_Type = Gauge32
_CfprApLsbootVirtualMediaOrder_Object = MibTableColumn
cfprApLsbootVirtualMediaOrder = _CfprApLsbootVirtualMediaOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 7),
    _CfprApLsbootVirtualMediaOrder_Type()
)
cfprApLsbootVirtualMediaOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaOrder.setStatus("current")
_CfprApLsbootVirtualMediaType_Type = CfprApLsbootVirtualMediaType
_CfprApLsbootVirtualMediaType_Object = MibTableColumn
cfprApLsbootVirtualMediaType = _CfprApLsbootVirtualMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 47, 20, 1, 8),
    _CfprApLsbootVirtualMediaType_Type()
)
cfprApLsbootVirtualMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsbootVirtualMediaType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-LSBOOT-MIB",
    **{"cfprApLsbootObjects": cfprApLsbootObjects,
       "cfprApLsbootBootSecurityTable": cfprApLsbootBootSecurityTable,
       "cfprApLsbootBootSecurityEntry": cfprApLsbootBootSecurityEntry,
       "cfprApLsbootBootSecurityInstanceId": cfprApLsbootBootSecurityInstanceId,
       "cfprApLsbootBootSecurityDn": cfprApLsbootBootSecurityDn,
       "cfprApLsbootBootSecurityRn": cfprApLsbootBootSecurityRn,
       "cfprApLsbootBootSecuritySecureBoot": cfprApLsbootBootSecuritySecureBoot,
       "cfprApLsbootDefTable": cfprApLsbootDefTable,
       "cfprApLsbootDefEntry": cfprApLsbootDefEntry,
       "cfprApLsbootDefInstanceId": cfprApLsbootDefInstanceId,
       "cfprApLsbootDefDn": cfprApLsbootDefDn,
       "cfprApLsbootDefRn": cfprApLsbootDefRn,
       "cfprApLsbootDefAdvBootOrderApplicable": cfprApLsbootDefAdvBootOrderApplicable,
       "cfprApLsbootDefBootMode": cfprApLsbootDefBootMode,
       "cfprApLsbootDefDescr": cfprApLsbootDefDescr,
       "cfprApLsbootDefEnforceVnicName": cfprApLsbootDefEnforceVnicName,
       "cfprApLsbootDefIntId": cfprApLsbootDefIntId,
       "cfprApLsbootDefName": cfprApLsbootDefName,
       "cfprApLsbootDefPolicyLevel": cfprApLsbootDefPolicyLevel,
       "cfprApLsbootDefPolicyOwner": cfprApLsbootDefPolicyOwner,
       "cfprApLsbootDefPurpose": cfprApLsbootDefPurpose,
       "cfprApLsbootDefRebootOnUpdate": cfprApLsbootDefRebootOnUpdate,
       "cfprApLsbootDefaultLocalImageTable": cfprApLsbootDefaultLocalImageTable,
       "cfprApLsbootDefaultLocalImageEntry": cfprApLsbootDefaultLocalImageEntry,
       "cfprApLsbootDefaultLocalImageInstanceId": cfprApLsbootDefaultLocalImageInstanceId,
       "cfprApLsbootDefaultLocalImageDn": cfprApLsbootDefaultLocalImageDn,
       "cfprApLsbootDefaultLocalImageRn": cfprApLsbootDefaultLocalImageRn,
       "cfprApLsbootDefaultLocalImageOrder": cfprApLsbootDefaultLocalImageOrder,
       "cfprApLsbootDefaultLocalImageType": cfprApLsbootDefaultLocalImageType,
       "cfprApLsbootIScsiTable": cfprApLsbootIScsiTable,
       "cfprApLsbootIScsiEntry": cfprApLsbootIScsiEntry,
       "cfprApLsbootIScsiInstanceId": cfprApLsbootIScsiInstanceId,
       "cfprApLsbootIScsiDn": cfprApLsbootIScsiDn,
       "cfprApLsbootIScsiRn": cfprApLsbootIScsiRn,
       "cfprApLsbootIScsiAccess": cfprApLsbootIScsiAccess,
       "cfprApLsbootIScsiOrder": cfprApLsbootIScsiOrder,
       "cfprApLsbootIScsiType": cfprApLsbootIScsiType,
       "cfprApLsbootIScsiImagePathTable": cfprApLsbootIScsiImagePathTable,
       "cfprApLsbootIScsiImagePathEntry": cfprApLsbootIScsiImagePathEntry,
       "cfprApLsbootIScsiImagePathInstanceId": cfprApLsbootIScsiImagePathInstanceId,
       "cfprApLsbootIScsiImagePathDn": cfprApLsbootIScsiImagePathDn,
       "cfprApLsbootIScsiImagePathRn": cfprApLsbootIScsiImagePathRn,
       "cfprApLsbootIScsiImagePathISCSIVnicName": cfprApLsbootIScsiImagePathISCSIVnicName,
       "cfprApLsbootIScsiImagePathType": cfprApLsbootIScsiImagePathType,
       "cfprApLsbootIScsiImagePathVnicName": cfprApLsbootIScsiImagePathVnicName,
       "cfprApLsbootLanTable": cfprApLsbootLanTable,
       "cfprApLsbootLanEntry": cfprApLsbootLanEntry,
       "cfprApLsbootLanInstanceId": cfprApLsbootLanInstanceId,
       "cfprApLsbootLanDn": cfprApLsbootLanDn,
       "cfprApLsbootLanRn": cfprApLsbootLanRn,
       "cfprApLsbootLanAccess": cfprApLsbootLanAccess,
       "cfprApLsbootLanOrder": cfprApLsbootLanOrder,
       "cfprApLsbootLanProt": cfprApLsbootLanProt,
       "cfprApLsbootLanType": cfprApLsbootLanType,
       "cfprApLsbootLanImagePathTable": cfprApLsbootLanImagePathTable,
       "cfprApLsbootLanImagePathEntry": cfprApLsbootLanImagePathEntry,
       "cfprApLsbootLanImagePathInstanceId": cfprApLsbootLanImagePathInstanceId,
       "cfprApLsbootLanImagePathDn": cfprApLsbootLanImagePathDn,
       "cfprApLsbootLanImagePathRn": cfprApLsbootLanImagePathRn,
       "cfprApLsbootLanImagePathBootIpPolicyName": cfprApLsbootLanImagePathBootIpPolicyName,
       "cfprApLsbootLanImagePathISCSIVnicName": cfprApLsbootLanImagePathISCSIVnicName,
       "cfprApLsbootLanImagePathImgPolicyName": cfprApLsbootLanImagePathImgPolicyName,
       "cfprApLsbootLanImagePathImgSecPolicyName": cfprApLsbootLanImagePathImgSecPolicyName,
       "cfprApLsbootLanImagePathProvSrvPolicyName": cfprApLsbootLanImagePathProvSrvPolicyName,
       "cfprApLsbootLanImagePathType": cfprApLsbootLanImagePathType,
       "cfprApLsbootLanImagePathVnicName": cfprApLsbootLanImagePathVnicName,
       "cfprApLsbootLocalHddImageTable": cfprApLsbootLocalHddImageTable,
       "cfprApLsbootLocalHddImageEntry": cfprApLsbootLocalHddImageEntry,
       "cfprApLsbootLocalHddImageInstanceId": cfprApLsbootLocalHddImageInstanceId,
       "cfprApLsbootLocalHddImageDn": cfprApLsbootLocalHddImageDn,
       "cfprApLsbootLocalHddImageRn": cfprApLsbootLocalHddImageRn,
       "cfprApLsbootLocalHddImageOrder": cfprApLsbootLocalHddImageOrder,
       "cfprApLsbootLocalHddImageType": cfprApLsbootLocalHddImageType,
       "cfprApLsbootLocalStorageTable": cfprApLsbootLocalStorageTable,
       "cfprApLsbootLocalStorageEntry": cfprApLsbootLocalStorageEntry,
       "cfprApLsbootLocalStorageInstanceId": cfprApLsbootLocalStorageInstanceId,
       "cfprApLsbootLocalStorageDn": cfprApLsbootLocalStorageDn,
       "cfprApLsbootLocalStorageRn": cfprApLsbootLocalStorageRn,
       "cfprApLsbootPolicyTable": cfprApLsbootPolicyTable,
       "cfprApLsbootPolicyEntry": cfprApLsbootPolicyEntry,
       "cfprApLsbootPolicyInstanceId": cfprApLsbootPolicyInstanceId,
       "cfprApLsbootPolicyDn": cfprApLsbootPolicyDn,
       "cfprApLsbootPolicyRn": cfprApLsbootPolicyRn,
       "cfprApLsbootPolicyBootMode": cfprApLsbootPolicyBootMode,
       "cfprApLsbootPolicyDescr": cfprApLsbootPolicyDescr,
       "cfprApLsbootPolicyEnforceVnicName": cfprApLsbootPolicyEnforceVnicName,
       "cfprApLsbootPolicyIntId": cfprApLsbootPolicyIntId,
       "cfprApLsbootPolicyName": cfprApLsbootPolicyName,
       "cfprApLsbootPolicyPolicyLevel": cfprApLsbootPolicyPolicyLevel,
       "cfprApLsbootPolicyPolicyOwner": cfprApLsbootPolicyPolicyOwner,
       "cfprApLsbootPolicyPurpose": cfprApLsbootPolicyPurpose,
       "cfprApLsbootPolicyRebootOnUpdate": cfprApLsbootPolicyRebootOnUpdate,
       "cfprApLsbootSanTable": cfprApLsbootSanTable,
       "cfprApLsbootSanEntry": cfprApLsbootSanEntry,
       "cfprApLsbootSanInstanceId": cfprApLsbootSanInstanceId,
       "cfprApLsbootSanDn": cfprApLsbootSanDn,
       "cfprApLsbootSanRn": cfprApLsbootSanRn,
       "cfprApLsbootSanAccess": cfprApLsbootSanAccess,
       "cfprApLsbootSanOrder": cfprApLsbootSanOrder,
       "cfprApLsbootSanType": cfprApLsbootSanType,
       "cfprApLsbootSanCatSanImageTable": cfprApLsbootSanCatSanImageTable,
       "cfprApLsbootSanCatSanImageEntry": cfprApLsbootSanCatSanImageEntry,
       "cfprApLsbootSanCatSanImageInstanceId": cfprApLsbootSanCatSanImageInstanceId,
       "cfprApLsbootSanCatSanImageDn": cfprApLsbootSanCatSanImageDn,
       "cfprApLsbootSanCatSanImageRn": cfprApLsbootSanCatSanImageRn,
       "cfprApLsbootSanCatSanImageType": cfprApLsbootSanCatSanImageType,
       "cfprApLsbootSanCatSanImageVnicName": cfprApLsbootSanCatSanImageVnicName,
       "cfprApLsbootSanCatSanImagePathTable": cfprApLsbootSanCatSanImagePathTable,
       "cfprApLsbootSanCatSanImagePathEntry": cfprApLsbootSanCatSanImagePathEntry,
       "cfprApLsbootSanCatSanImagePathInstanceId": cfprApLsbootSanCatSanImagePathInstanceId,
       "cfprApLsbootSanCatSanImagePathDn": cfprApLsbootSanCatSanImagePathDn,
       "cfprApLsbootSanCatSanImagePathRn": cfprApLsbootSanCatSanImagePathRn,
       "cfprApLsbootSanCatSanImagePathLun": cfprApLsbootSanCatSanImagePathLun,
       "cfprApLsbootSanCatSanImagePathType": cfprApLsbootSanCatSanImagePathType,
       "cfprApLsbootSanCatSanImagePathVnicName": cfprApLsbootSanCatSanImagePathVnicName,
       "cfprApLsbootSanCatSanImagePathWwn": cfprApLsbootSanCatSanImagePathWwn,
       "cfprApLsbootSanImageTable": cfprApLsbootSanImageTable,
       "cfprApLsbootSanImageEntry": cfprApLsbootSanImageEntry,
       "cfprApLsbootSanImageInstanceId": cfprApLsbootSanImageInstanceId,
       "cfprApLsbootSanImageDn": cfprApLsbootSanImageDn,
       "cfprApLsbootSanImageRn": cfprApLsbootSanImageRn,
       "cfprApLsbootSanImageType": cfprApLsbootSanImageType,
       "cfprApLsbootSanImageVnicName": cfprApLsbootSanImageVnicName,
       "cfprApLsbootSanImagePathTable": cfprApLsbootSanImagePathTable,
       "cfprApLsbootSanImagePathEntry": cfprApLsbootSanImagePathEntry,
       "cfprApLsbootSanImagePathInstanceId": cfprApLsbootSanImagePathInstanceId,
       "cfprApLsbootSanImagePathDn": cfprApLsbootSanImagePathDn,
       "cfprApLsbootSanImagePathRn": cfprApLsbootSanImagePathRn,
       "cfprApLsbootSanImagePathLun": cfprApLsbootSanImagePathLun,
       "cfprApLsbootSanImagePathType": cfprApLsbootSanImagePathType,
       "cfprApLsbootSanImagePathVnicName": cfprApLsbootSanImagePathVnicName,
       "cfprApLsbootSanImagePathWwn": cfprApLsbootSanImagePathWwn,
       "cfprApLsbootStorageTable": cfprApLsbootStorageTable,
       "cfprApLsbootStorageEntry": cfprApLsbootStorageEntry,
       "cfprApLsbootStorageInstanceId": cfprApLsbootStorageInstanceId,
       "cfprApLsbootStorageDn": cfprApLsbootStorageDn,
       "cfprApLsbootStorageRn": cfprApLsbootStorageRn,
       "cfprApLsbootStorageAccess": cfprApLsbootStorageAccess,
       "cfprApLsbootStorageOrder": cfprApLsbootStorageOrder,
       "cfprApLsbootStorageType": cfprApLsbootStorageType,
       "cfprApLsbootUsbExternalImageTable": cfprApLsbootUsbExternalImageTable,
       "cfprApLsbootUsbExternalImageEntry": cfprApLsbootUsbExternalImageEntry,
       "cfprApLsbootUsbExternalImageInstanceId": cfprApLsbootUsbExternalImageInstanceId,
       "cfprApLsbootUsbExternalImageDn": cfprApLsbootUsbExternalImageDn,
       "cfprApLsbootUsbExternalImageRn": cfprApLsbootUsbExternalImageRn,
       "cfprApLsbootUsbExternalImageOrder": cfprApLsbootUsbExternalImageOrder,
       "cfprApLsbootUsbExternalImageType": cfprApLsbootUsbExternalImageType,
       "cfprApLsbootUsbFlashStorageImageTable": cfprApLsbootUsbFlashStorageImageTable,
       "cfprApLsbootUsbFlashStorageImageEntry": cfprApLsbootUsbFlashStorageImageEntry,
       "cfprApLsbootUsbFlashStorageImageInstanceId": cfprApLsbootUsbFlashStorageImageInstanceId,
       "cfprApLsbootUsbFlashStorageImageDn": cfprApLsbootUsbFlashStorageImageDn,
       "cfprApLsbootUsbFlashStorageImageRn": cfprApLsbootUsbFlashStorageImageRn,
       "cfprApLsbootUsbFlashStorageImageOrder": cfprApLsbootUsbFlashStorageImageOrder,
       "cfprApLsbootUsbFlashStorageImageType": cfprApLsbootUsbFlashStorageImageType,
       "cfprApLsbootUsbInternalImageTable": cfprApLsbootUsbInternalImageTable,
       "cfprApLsbootUsbInternalImageEntry": cfprApLsbootUsbInternalImageEntry,
       "cfprApLsbootUsbInternalImageInstanceId": cfprApLsbootUsbInternalImageInstanceId,
       "cfprApLsbootUsbInternalImageDn": cfprApLsbootUsbInternalImageDn,
       "cfprApLsbootUsbInternalImageRn": cfprApLsbootUsbInternalImageRn,
       "cfprApLsbootUsbInternalImageOrder": cfprApLsbootUsbInternalImageOrder,
       "cfprApLsbootUsbInternalImageType": cfprApLsbootUsbInternalImageType,
       "cfprApLsbootVirtualMediaTable": cfprApLsbootVirtualMediaTable,
       "cfprApLsbootVirtualMediaEntry": cfprApLsbootVirtualMediaEntry,
       "cfprApLsbootVirtualMediaInstanceId": cfprApLsbootVirtualMediaInstanceId,
       "cfprApLsbootVirtualMediaDn": cfprApLsbootVirtualMediaDn,
       "cfprApLsbootVirtualMediaRn": cfprApLsbootVirtualMediaRn,
       "cfprApLsbootVirtualMediaAccess": cfprApLsbootVirtualMediaAccess,
       "cfprApLsbootVirtualMediaLunId": cfprApLsbootVirtualMediaLunId,
       "cfprApLsbootVirtualMediaMappingName": cfprApLsbootVirtualMediaMappingName,
       "cfprApLsbootVirtualMediaOrder": cfprApLsbootVirtualMediaOrder,
       "cfprApLsbootVirtualMediaType": cfprApLsbootVirtualMediaType}
)
