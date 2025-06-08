# SNMP MIB module (CISCO-FIREPOWER-LSBOOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-LSBOOT-MIB.mib
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

(CfprLsbootADefBootMode,
 CfprLsbootAccessType,
 CfprLsbootDefaultLocalImageType,
 CfprLsbootIScsiAccess,
 CfprLsbootIScsiImagePathType,
 CfprLsbootIScsiType,
 CfprLsbootLanAccess,
 CfprLsbootLanBootProt,
 CfprLsbootLanImagePathType,
 CfprLsbootLanType,
 CfprLsbootLocalHddImageType,
 CfprLsbootPurpose,
 CfprLsbootSanAccess,
 CfprLsbootSanCatSanImagePathType,
 CfprLsbootSanCatSanImageType,
 CfprLsbootSanImagePathType,
 CfprLsbootSanImageType,
 CfprLsbootSanType,
 CfprLsbootStorageAccess,
 CfprLsbootStorageType,
 CfprLsbootUsbExternalImageType,
 CfprLsbootUsbFlashStorageImageType,
 CfprLsbootUsbInternalImageType,
 CfprLsbootVirtualMediaType,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprLsbootADefBootMode",
    "CfprLsbootAccessType",
    "CfprLsbootDefaultLocalImageType",
    "CfprLsbootIScsiAccess",
    "CfprLsbootIScsiImagePathType",
    "CfprLsbootIScsiType",
    "CfprLsbootLanAccess",
    "CfprLsbootLanBootProt",
    "CfprLsbootLanImagePathType",
    "CfprLsbootLanType",
    "CfprLsbootLocalHddImageType",
    "CfprLsbootPurpose",
    "CfprLsbootSanAccess",
    "CfprLsbootSanCatSanImagePathType",
    "CfprLsbootSanCatSanImageType",
    "CfprLsbootSanImagePathType",
    "CfprLsbootSanImageType",
    "CfprLsbootSanType",
    "CfprLsbootStorageAccess",
    "CfprLsbootStorageType",
    "CfprLsbootUsbExternalImageType",
    "CfprLsbootUsbFlashStorageImageType",
    "CfprLsbootUsbInternalImageType",
    "CfprLsbootVirtualMediaType",
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

cfprLsbootObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprLsbootBootSecurityTable_Object = MibTable
cfprLsbootBootSecurityTable = _CfprLsbootBootSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 1)
)
if mibBuilder.loadTexts:
    cfprLsbootBootSecurityTable.setStatus("current")
_CfprLsbootBootSecurityEntry_Object = MibTableRow
cfprLsbootBootSecurityEntry = _CfprLsbootBootSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 1, 1)
)
cfprLsbootBootSecurityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootBootSecurityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootBootSecurityEntry.setStatus("current")
_CfprLsbootBootSecurityInstanceId_Type = CfprManagedObjectId
_CfprLsbootBootSecurityInstanceId_Object = MibTableColumn
cfprLsbootBootSecurityInstanceId = _CfprLsbootBootSecurityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 1, 1, 1),
    _CfprLsbootBootSecurityInstanceId_Type()
)
cfprLsbootBootSecurityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootBootSecurityInstanceId.setStatus("current")
_CfprLsbootBootSecurityDn_Type = CfprManagedObjectDn
_CfprLsbootBootSecurityDn_Object = MibTableColumn
cfprLsbootBootSecurityDn = _CfprLsbootBootSecurityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 1, 1, 2),
    _CfprLsbootBootSecurityDn_Type()
)
cfprLsbootBootSecurityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootBootSecurityDn.setStatus("current")
_CfprLsbootBootSecurityRn_Type = SnmpAdminString
_CfprLsbootBootSecurityRn_Object = MibTableColumn
cfprLsbootBootSecurityRn = _CfprLsbootBootSecurityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 1, 1, 3),
    _CfprLsbootBootSecurityRn_Type()
)
cfprLsbootBootSecurityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootBootSecurityRn.setStatus("current")
_CfprLsbootBootSecuritySecureBoot_Type = TruthValue
_CfprLsbootBootSecuritySecureBoot_Object = MibTableColumn
cfprLsbootBootSecuritySecureBoot = _CfprLsbootBootSecuritySecureBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 1, 1, 4),
    _CfprLsbootBootSecuritySecureBoot_Type()
)
cfprLsbootBootSecuritySecureBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootBootSecuritySecureBoot.setStatus("current")
_CfprLsbootDefTable_Object = MibTable
cfprLsbootDefTable = _CfprLsbootDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2)
)
if mibBuilder.loadTexts:
    cfprLsbootDefTable.setStatus("current")
_CfprLsbootDefEntry_Object = MibTableRow
cfprLsbootDefEntry = _CfprLsbootDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1)
)
cfprLsbootDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootDefEntry.setStatus("current")
_CfprLsbootDefInstanceId_Type = CfprManagedObjectId
_CfprLsbootDefInstanceId_Object = MibTableColumn
cfprLsbootDefInstanceId = _CfprLsbootDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 1),
    _CfprLsbootDefInstanceId_Type()
)
cfprLsbootDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootDefInstanceId.setStatus("current")
_CfprLsbootDefDn_Type = CfprManagedObjectDn
_CfprLsbootDefDn_Object = MibTableColumn
cfprLsbootDefDn = _CfprLsbootDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 2),
    _CfprLsbootDefDn_Type()
)
cfprLsbootDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefDn.setStatus("current")
_CfprLsbootDefRn_Type = SnmpAdminString
_CfprLsbootDefRn_Object = MibTableColumn
cfprLsbootDefRn = _CfprLsbootDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 3),
    _CfprLsbootDefRn_Type()
)
cfprLsbootDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefRn.setStatus("current")
_CfprLsbootDefAdvBootOrderApplicable_Type = TruthValue
_CfprLsbootDefAdvBootOrderApplicable_Object = MibTableColumn
cfprLsbootDefAdvBootOrderApplicable = _CfprLsbootDefAdvBootOrderApplicable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 4),
    _CfprLsbootDefAdvBootOrderApplicable_Type()
)
cfprLsbootDefAdvBootOrderApplicable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefAdvBootOrderApplicable.setStatus("current")
_CfprLsbootDefBootMode_Type = CfprLsbootADefBootMode
_CfprLsbootDefBootMode_Object = MibTableColumn
cfprLsbootDefBootMode = _CfprLsbootDefBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 5),
    _CfprLsbootDefBootMode_Type()
)
cfprLsbootDefBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefBootMode.setStatus("current")
_CfprLsbootDefDescr_Type = SnmpAdminString
_CfprLsbootDefDescr_Object = MibTableColumn
cfprLsbootDefDescr = _CfprLsbootDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 6),
    _CfprLsbootDefDescr_Type()
)
cfprLsbootDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefDescr.setStatus("current")
_CfprLsbootDefEnforceVnicName_Type = TruthValue
_CfprLsbootDefEnforceVnicName_Object = MibTableColumn
cfprLsbootDefEnforceVnicName = _CfprLsbootDefEnforceVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 7),
    _CfprLsbootDefEnforceVnicName_Type()
)
cfprLsbootDefEnforceVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefEnforceVnicName.setStatus("current")
_CfprLsbootDefIntId_Type = SnmpAdminString
_CfprLsbootDefIntId_Object = MibTableColumn
cfprLsbootDefIntId = _CfprLsbootDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 8),
    _CfprLsbootDefIntId_Type()
)
cfprLsbootDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefIntId.setStatus("current")
_CfprLsbootDefName_Type = SnmpAdminString
_CfprLsbootDefName_Object = MibTableColumn
cfprLsbootDefName = _CfprLsbootDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 9),
    _CfprLsbootDefName_Type()
)
cfprLsbootDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefName.setStatus("current")
_CfprLsbootDefPolicyLevel_Type = Gauge32
_CfprLsbootDefPolicyLevel_Object = MibTableColumn
cfprLsbootDefPolicyLevel = _CfprLsbootDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 10),
    _CfprLsbootDefPolicyLevel_Type()
)
cfprLsbootDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefPolicyLevel.setStatus("current")
_CfprLsbootDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsbootDefPolicyOwner_Object = MibTableColumn
cfprLsbootDefPolicyOwner = _CfprLsbootDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 11),
    _CfprLsbootDefPolicyOwner_Type()
)
cfprLsbootDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefPolicyOwner.setStatus("current")
_CfprLsbootDefPurpose_Type = CfprLsbootPurpose
_CfprLsbootDefPurpose_Object = MibTableColumn
cfprLsbootDefPurpose = _CfprLsbootDefPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 12),
    _CfprLsbootDefPurpose_Type()
)
cfprLsbootDefPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefPurpose.setStatus("current")
_CfprLsbootDefRebootOnUpdate_Type = TruthValue
_CfprLsbootDefRebootOnUpdate_Object = MibTableColumn
cfprLsbootDefRebootOnUpdate = _CfprLsbootDefRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 2, 1, 13),
    _CfprLsbootDefRebootOnUpdate_Type()
)
cfprLsbootDefRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefRebootOnUpdate.setStatus("current")
_CfprLsbootDefaultLocalImageTable_Object = MibTable
cfprLsbootDefaultLocalImageTable = _CfprLsbootDefaultLocalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3)
)
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageTable.setStatus("current")
_CfprLsbootDefaultLocalImageEntry_Object = MibTableRow
cfprLsbootDefaultLocalImageEntry = _CfprLsbootDefaultLocalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3, 1)
)
cfprLsbootDefaultLocalImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootDefaultLocalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageEntry.setStatus("current")
_CfprLsbootDefaultLocalImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootDefaultLocalImageInstanceId_Object = MibTableColumn
cfprLsbootDefaultLocalImageInstanceId = _CfprLsbootDefaultLocalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3, 1, 1),
    _CfprLsbootDefaultLocalImageInstanceId_Type()
)
cfprLsbootDefaultLocalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageInstanceId.setStatus("current")
_CfprLsbootDefaultLocalImageDn_Type = CfprManagedObjectDn
_CfprLsbootDefaultLocalImageDn_Object = MibTableColumn
cfprLsbootDefaultLocalImageDn = _CfprLsbootDefaultLocalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3, 1, 2),
    _CfprLsbootDefaultLocalImageDn_Type()
)
cfprLsbootDefaultLocalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageDn.setStatus("current")
_CfprLsbootDefaultLocalImageRn_Type = SnmpAdminString
_CfprLsbootDefaultLocalImageRn_Object = MibTableColumn
cfprLsbootDefaultLocalImageRn = _CfprLsbootDefaultLocalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3, 1, 3),
    _CfprLsbootDefaultLocalImageRn_Type()
)
cfprLsbootDefaultLocalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageRn.setStatus("current")
_CfprLsbootDefaultLocalImageOrder_Type = Gauge32
_CfprLsbootDefaultLocalImageOrder_Object = MibTableColumn
cfprLsbootDefaultLocalImageOrder = _CfprLsbootDefaultLocalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3, 1, 4),
    _CfprLsbootDefaultLocalImageOrder_Type()
)
cfprLsbootDefaultLocalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageOrder.setStatus("current")
_CfprLsbootDefaultLocalImageType_Type = CfprLsbootDefaultLocalImageType
_CfprLsbootDefaultLocalImageType_Object = MibTableColumn
cfprLsbootDefaultLocalImageType = _CfprLsbootDefaultLocalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 3, 1, 5),
    _CfprLsbootDefaultLocalImageType_Type()
)
cfprLsbootDefaultLocalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootDefaultLocalImageType.setStatus("current")
_CfprLsbootIScsiTable_Object = MibTable
cfprLsbootIScsiTable = _CfprLsbootIScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4)
)
if mibBuilder.loadTexts:
    cfprLsbootIScsiTable.setStatus("current")
_CfprLsbootIScsiEntry_Object = MibTableRow
cfprLsbootIScsiEntry = _CfprLsbootIScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1)
)
cfprLsbootIScsiEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootIScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootIScsiEntry.setStatus("current")
_CfprLsbootIScsiInstanceId_Type = CfprManagedObjectId
_CfprLsbootIScsiInstanceId_Object = MibTableColumn
cfprLsbootIScsiInstanceId = _CfprLsbootIScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1, 1),
    _CfprLsbootIScsiInstanceId_Type()
)
cfprLsbootIScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootIScsiInstanceId.setStatus("current")
_CfprLsbootIScsiDn_Type = CfprManagedObjectDn
_CfprLsbootIScsiDn_Object = MibTableColumn
cfprLsbootIScsiDn = _CfprLsbootIScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1, 2),
    _CfprLsbootIScsiDn_Type()
)
cfprLsbootIScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiDn.setStatus("current")
_CfprLsbootIScsiRn_Type = SnmpAdminString
_CfprLsbootIScsiRn_Object = MibTableColumn
cfprLsbootIScsiRn = _CfprLsbootIScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1, 3),
    _CfprLsbootIScsiRn_Type()
)
cfprLsbootIScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiRn.setStatus("current")
_CfprLsbootIScsiAccess_Type = CfprLsbootIScsiAccess
_CfprLsbootIScsiAccess_Object = MibTableColumn
cfprLsbootIScsiAccess = _CfprLsbootIScsiAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1, 4),
    _CfprLsbootIScsiAccess_Type()
)
cfprLsbootIScsiAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiAccess.setStatus("current")
_CfprLsbootIScsiOrder_Type = Gauge32
_CfprLsbootIScsiOrder_Object = MibTableColumn
cfprLsbootIScsiOrder = _CfprLsbootIScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1, 5),
    _CfprLsbootIScsiOrder_Type()
)
cfprLsbootIScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiOrder.setStatus("current")
_CfprLsbootIScsiType_Type = CfprLsbootIScsiType
_CfprLsbootIScsiType_Object = MibTableColumn
cfprLsbootIScsiType = _CfprLsbootIScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 4, 1, 6),
    _CfprLsbootIScsiType_Type()
)
cfprLsbootIScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiType.setStatus("current")
_CfprLsbootIScsiImagePathTable_Object = MibTable
cfprLsbootIScsiImagePathTable = _CfprLsbootIScsiImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5)
)
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathTable.setStatus("current")
_CfprLsbootIScsiImagePathEntry_Object = MibTableRow
cfprLsbootIScsiImagePathEntry = _CfprLsbootIScsiImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1)
)
cfprLsbootIScsiImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootIScsiImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathEntry.setStatus("current")
_CfprLsbootIScsiImagePathInstanceId_Type = CfprManagedObjectId
_CfprLsbootIScsiImagePathInstanceId_Object = MibTableColumn
cfprLsbootIScsiImagePathInstanceId = _CfprLsbootIScsiImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1, 1),
    _CfprLsbootIScsiImagePathInstanceId_Type()
)
cfprLsbootIScsiImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathInstanceId.setStatus("current")
_CfprLsbootIScsiImagePathDn_Type = CfprManagedObjectDn
_CfprLsbootIScsiImagePathDn_Object = MibTableColumn
cfprLsbootIScsiImagePathDn = _CfprLsbootIScsiImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1, 2),
    _CfprLsbootIScsiImagePathDn_Type()
)
cfprLsbootIScsiImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathDn.setStatus("current")
_CfprLsbootIScsiImagePathRn_Type = SnmpAdminString
_CfprLsbootIScsiImagePathRn_Object = MibTableColumn
cfprLsbootIScsiImagePathRn = _CfprLsbootIScsiImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1, 3),
    _CfprLsbootIScsiImagePathRn_Type()
)
cfprLsbootIScsiImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathRn.setStatus("current")
_CfprLsbootIScsiImagePathISCSIVnicName_Type = SnmpAdminString
_CfprLsbootIScsiImagePathISCSIVnicName_Object = MibTableColumn
cfprLsbootIScsiImagePathISCSIVnicName = _CfprLsbootIScsiImagePathISCSIVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1, 4),
    _CfprLsbootIScsiImagePathISCSIVnicName_Type()
)
cfprLsbootIScsiImagePathISCSIVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathISCSIVnicName.setStatus("current")
_CfprLsbootIScsiImagePathType_Type = CfprLsbootIScsiImagePathType
_CfprLsbootIScsiImagePathType_Object = MibTableColumn
cfprLsbootIScsiImagePathType = _CfprLsbootIScsiImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1, 5),
    _CfprLsbootIScsiImagePathType_Type()
)
cfprLsbootIScsiImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathType.setStatus("current")
_CfprLsbootIScsiImagePathVnicName_Type = SnmpAdminString
_CfprLsbootIScsiImagePathVnicName_Object = MibTableColumn
cfprLsbootIScsiImagePathVnicName = _CfprLsbootIScsiImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 5, 1, 6),
    _CfprLsbootIScsiImagePathVnicName_Type()
)
cfprLsbootIScsiImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootIScsiImagePathVnicName.setStatus("current")
_CfprLsbootLanTable_Object = MibTable
cfprLsbootLanTable = _CfprLsbootLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6)
)
if mibBuilder.loadTexts:
    cfprLsbootLanTable.setStatus("current")
_CfprLsbootLanEntry_Object = MibTableRow
cfprLsbootLanEntry = _CfprLsbootLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1)
)
cfprLsbootLanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootLanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootLanEntry.setStatus("current")
_CfprLsbootLanInstanceId_Type = CfprManagedObjectId
_CfprLsbootLanInstanceId_Object = MibTableColumn
cfprLsbootLanInstanceId = _CfprLsbootLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 1),
    _CfprLsbootLanInstanceId_Type()
)
cfprLsbootLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootLanInstanceId.setStatus("current")
_CfprLsbootLanDn_Type = CfprManagedObjectDn
_CfprLsbootLanDn_Object = MibTableColumn
cfprLsbootLanDn = _CfprLsbootLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 2),
    _CfprLsbootLanDn_Type()
)
cfprLsbootLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanDn.setStatus("current")
_CfprLsbootLanRn_Type = SnmpAdminString
_CfprLsbootLanRn_Object = MibTableColumn
cfprLsbootLanRn = _CfprLsbootLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 3),
    _CfprLsbootLanRn_Type()
)
cfprLsbootLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanRn.setStatus("current")
_CfprLsbootLanAccess_Type = CfprLsbootLanAccess
_CfprLsbootLanAccess_Object = MibTableColumn
cfprLsbootLanAccess = _CfprLsbootLanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 4),
    _CfprLsbootLanAccess_Type()
)
cfprLsbootLanAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanAccess.setStatus("current")
_CfprLsbootLanOrder_Type = Gauge32
_CfprLsbootLanOrder_Object = MibTableColumn
cfprLsbootLanOrder = _CfprLsbootLanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 5),
    _CfprLsbootLanOrder_Type()
)
cfprLsbootLanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanOrder.setStatus("current")
_CfprLsbootLanProt_Type = CfprLsbootLanBootProt
_CfprLsbootLanProt_Object = MibTableColumn
cfprLsbootLanProt = _CfprLsbootLanProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 6),
    _CfprLsbootLanProt_Type()
)
cfprLsbootLanProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanProt.setStatus("current")
_CfprLsbootLanType_Type = CfprLsbootLanType
_CfprLsbootLanType_Object = MibTableColumn
cfprLsbootLanType = _CfprLsbootLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 6, 1, 7),
    _CfprLsbootLanType_Type()
)
cfprLsbootLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanType.setStatus("current")
_CfprLsbootLanImagePathTable_Object = MibTable
cfprLsbootLanImagePathTable = _CfprLsbootLanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7)
)
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathTable.setStatus("current")
_CfprLsbootLanImagePathEntry_Object = MibTableRow
cfprLsbootLanImagePathEntry = _CfprLsbootLanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1)
)
cfprLsbootLanImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootLanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathEntry.setStatus("current")
_CfprLsbootLanImagePathInstanceId_Type = CfprManagedObjectId
_CfprLsbootLanImagePathInstanceId_Object = MibTableColumn
cfprLsbootLanImagePathInstanceId = _CfprLsbootLanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 1),
    _CfprLsbootLanImagePathInstanceId_Type()
)
cfprLsbootLanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathInstanceId.setStatus("current")
_CfprLsbootLanImagePathDn_Type = CfprManagedObjectDn
_CfprLsbootLanImagePathDn_Object = MibTableColumn
cfprLsbootLanImagePathDn = _CfprLsbootLanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 2),
    _CfprLsbootLanImagePathDn_Type()
)
cfprLsbootLanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathDn.setStatus("current")
_CfprLsbootLanImagePathRn_Type = SnmpAdminString
_CfprLsbootLanImagePathRn_Object = MibTableColumn
cfprLsbootLanImagePathRn = _CfprLsbootLanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 3),
    _CfprLsbootLanImagePathRn_Type()
)
cfprLsbootLanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathRn.setStatus("current")
_CfprLsbootLanImagePathBootIpPolicyName_Type = SnmpAdminString
_CfprLsbootLanImagePathBootIpPolicyName_Object = MibTableColumn
cfprLsbootLanImagePathBootIpPolicyName = _CfprLsbootLanImagePathBootIpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 4),
    _CfprLsbootLanImagePathBootIpPolicyName_Type()
)
cfprLsbootLanImagePathBootIpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathBootIpPolicyName.setStatus("current")
_CfprLsbootLanImagePathISCSIVnicName_Type = SnmpAdminString
_CfprLsbootLanImagePathISCSIVnicName_Object = MibTableColumn
cfprLsbootLanImagePathISCSIVnicName = _CfprLsbootLanImagePathISCSIVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 5),
    _CfprLsbootLanImagePathISCSIVnicName_Type()
)
cfprLsbootLanImagePathISCSIVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathISCSIVnicName.setStatus("current")
_CfprLsbootLanImagePathImgPolicyName_Type = SnmpAdminString
_CfprLsbootLanImagePathImgPolicyName_Object = MibTableColumn
cfprLsbootLanImagePathImgPolicyName = _CfprLsbootLanImagePathImgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 6),
    _CfprLsbootLanImagePathImgPolicyName_Type()
)
cfprLsbootLanImagePathImgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathImgPolicyName.setStatus("current")
_CfprLsbootLanImagePathImgSecPolicyName_Type = SnmpAdminString
_CfprLsbootLanImagePathImgSecPolicyName_Object = MibTableColumn
cfprLsbootLanImagePathImgSecPolicyName = _CfprLsbootLanImagePathImgSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 7),
    _CfprLsbootLanImagePathImgSecPolicyName_Type()
)
cfprLsbootLanImagePathImgSecPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathImgSecPolicyName.setStatus("current")
_CfprLsbootLanImagePathProvSrvPolicyName_Type = SnmpAdminString
_CfprLsbootLanImagePathProvSrvPolicyName_Object = MibTableColumn
cfprLsbootLanImagePathProvSrvPolicyName = _CfprLsbootLanImagePathProvSrvPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 8),
    _CfprLsbootLanImagePathProvSrvPolicyName_Type()
)
cfprLsbootLanImagePathProvSrvPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathProvSrvPolicyName.setStatus("current")
_CfprLsbootLanImagePathType_Type = CfprLsbootLanImagePathType
_CfprLsbootLanImagePathType_Object = MibTableColumn
cfprLsbootLanImagePathType = _CfprLsbootLanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 9),
    _CfprLsbootLanImagePathType_Type()
)
cfprLsbootLanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathType.setStatus("current")
_CfprLsbootLanImagePathVnicName_Type = SnmpAdminString
_CfprLsbootLanImagePathVnicName_Object = MibTableColumn
cfprLsbootLanImagePathVnicName = _CfprLsbootLanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 7, 1, 10),
    _CfprLsbootLanImagePathVnicName_Type()
)
cfprLsbootLanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLanImagePathVnicName.setStatus("current")
_CfprLsbootLocalHddImageTable_Object = MibTable
cfprLsbootLocalHddImageTable = _CfprLsbootLocalHddImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8)
)
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageTable.setStatus("current")
_CfprLsbootLocalHddImageEntry_Object = MibTableRow
cfprLsbootLocalHddImageEntry = _CfprLsbootLocalHddImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8, 1)
)
cfprLsbootLocalHddImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootLocalHddImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageEntry.setStatus("current")
_CfprLsbootLocalHddImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootLocalHddImageInstanceId_Object = MibTableColumn
cfprLsbootLocalHddImageInstanceId = _CfprLsbootLocalHddImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8, 1, 1),
    _CfprLsbootLocalHddImageInstanceId_Type()
)
cfprLsbootLocalHddImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageInstanceId.setStatus("current")
_CfprLsbootLocalHddImageDn_Type = CfprManagedObjectDn
_CfprLsbootLocalHddImageDn_Object = MibTableColumn
cfprLsbootLocalHddImageDn = _CfprLsbootLocalHddImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8, 1, 2),
    _CfprLsbootLocalHddImageDn_Type()
)
cfprLsbootLocalHddImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageDn.setStatus("current")
_CfprLsbootLocalHddImageRn_Type = SnmpAdminString
_CfprLsbootLocalHddImageRn_Object = MibTableColumn
cfprLsbootLocalHddImageRn = _CfprLsbootLocalHddImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8, 1, 3),
    _CfprLsbootLocalHddImageRn_Type()
)
cfprLsbootLocalHddImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageRn.setStatus("current")
_CfprLsbootLocalHddImageOrder_Type = Gauge32
_CfprLsbootLocalHddImageOrder_Object = MibTableColumn
cfprLsbootLocalHddImageOrder = _CfprLsbootLocalHddImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8, 1, 4),
    _CfprLsbootLocalHddImageOrder_Type()
)
cfprLsbootLocalHddImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageOrder.setStatus("current")
_CfprLsbootLocalHddImageType_Type = CfprLsbootLocalHddImageType
_CfprLsbootLocalHddImageType_Object = MibTableColumn
cfprLsbootLocalHddImageType = _CfprLsbootLocalHddImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 8, 1, 5),
    _CfprLsbootLocalHddImageType_Type()
)
cfprLsbootLocalHddImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLocalHddImageType.setStatus("current")
_CfprLsbootLocalStorageTable_Object = MibTable
cfprLsbootLocalStorageTable = _CfprLsbootLocalStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 9)
)
if mibBuilder.loadTexts:
    cfprLsbootLocalStorageTable.setStatus("current")
_CfprLsbootLocalStorageEntry_Object = MibTableRow
cfprLsbootLocalStorageEntry = _CfprLsbootLocalStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 9, 1)
)
cfprLsbootLocalStorageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootLocalStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootLocalStorageEntry.setStatus("current")
_CfprLsbootLocalStorageInstanceId_Type = CfprManagedObjectId
_CfprLsbootLocalStorageInstanceId_Object = MibTableColumn
cfprLsbootLocalStorageInstanceId = _CfprLsbootLocalStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 9, 1, 1),
    _CfprLsbootLocalStorageInstanceId_Type()
)
cfprLsbootLocalStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootLocalStorageInstanceId.setStatus("current")
_CfprLsbootLocalStorageDn_Type = CfprManagedObjectDn
_CfprLsbootLocalStorageDn_Object = MibTableColumn
cfprLsbootLocalStorageDn = _CfprLsbootLocalStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 9, 1, 2),
    _CfprLsbootLocalStorageDn_Type()
)
cfprLsbootLocalStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLocalStorageDn.setStatus("current")
_CfprLsbootLocalStorageRn_Type = SnmpAdminString
_CfprLsbootLocalStorageRn_Object = MibTableColumn
cfprLsbootLocalStorageRn = _CfprLsbootLocalStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 9, 1, 3),
    _CfprLsbootLocalStorageRn_Type()
)
cfprLsbootLocalStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootLocalStorageRn.setStatus("current")
_CfprLsbootPolicyTable_Object = MibTable
cfprLsbootPolicyTable = _CfprLsbootPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10)
)
if mibBuilder.loadTexts:
    cfprLsbootPolicyTable.setStatus("current")
_CfprLsbootPolicyEntry_Object = MibTableRow
cfprLsbootPolicyEntry = _CfprLsbootPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1)
)
cfprLsbootPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootPolicyEntry.setStatus("current")
_CfprLsbootPolicyInstanceId_Type = CfprManagedObjectId
_CfprLsbootPolicyInstanceId_Object = MibTableColumn
cfprLsbootPolicyInstanceId = _CfprLsbootPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 1),
    _CfprLsbootPolicyInstanceId_Type()
)
cfprLsbootPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootPolicyInstanceId.setStatus("current")
_CfprLsbootPolicyDn_Type = CfprManagedObjectDn
_CfprLsbootPolicyDn_Object = MibTableColumn
cfprLsbootPolicyDn = _CfprLsbootPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 2),
    _CfprLsbootPolicyDn_Type()
)
cfprLsbootPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyDn.setStatus("current")
_CfprLsbootPolicyRn_Type = SnmpAdminString
_CfprLsbootPolicyRn_Object = MibTableColumn
cfprLsbootPolicyRn = _CfprLsbootPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 3),
    _CfprLsbootPolicyRn_Type()
)
cfprLsbootPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyRn.setStatus("current")
_CfprLsbootPolicyBootMode_Type = CfprLsbootADefBootMode
_CfprLsbootPolicyBootMode_Object = MibTableColumn
cfprLsbootPolicyBootMode = _CfprLsbootPolicyBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 4),
    _CfprLsbootPolicyBootMode_Type()
)
cfprLsbootPolicyBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyBootMode.setStatus("current")
_CfprLsbootPolicyDescr_Type = SnmpAdminString
_CfprLsbootPolicyDescr_Object = MibTableColumn
cfprLsbootPolicyDescr = _CfprLsbootPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 5),
    _CfprLsbootPolicyDescr_Type()
)
cfprLsbootPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyDescr.setStatus("current")
_CfprLsbootPolicyEnforceVnicName_Type = TruthValue
_CfprLsbootPolicyEnforceVnicName_Object = MibTableColumn
cfprLsbootPolicyEnforceVnicName = _CfprLsbootPolicyEnforceVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 6),
    _CfprLsbootPolicyEnforceVnicName_Type()
)
cfprLsbootPolicyEnforceVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyEnforceVnicName.setStatus("current")
_CfprLsbootPolicyIntId_Type = SnmpAdminString
_CfprLsbootPolicyIntId_Object = MibTableColumn
cfprLsbootPolicyIntId = _CfprLsbootPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 7),
    _CfprLsbootPolicyIntId_Type()
)
cfprLsbootPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyIntId.setStatus("current")
_CfprLsbootPolicyName_Type = SnmpAdminString
_CfprLsbootPolicyName_Object = MibTableColumn
cfprLsbootPolicyName = _CfprLsbootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 8),
    _CfprLsbootPolicyName_Type()
)
cfprLsbootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyName.setStatus("current")
_CfprLsbootPolicyPolicyLevel_Type = Gauge32
_CfprLsbootPolicyPolicyLevel_Object = MibTableColumn
cfprLsbootPolicyPolicyLevel = _CfprLsbootPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 9),
    _CfprLsbootPolicyPolicyLevel_Type()
)
cfprLsbootPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyPolicyLevel.setStatus("current")
_CfprLsbootPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsbootPolicyPolicyOwner_Object = MibTableColumn
cfprLsbootPolicyPolicyOwner = _CfprLsbootPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 10),
    _CfprLsbootPolicyPolicyOwner_Type()
)
cfprLsbootPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyPolicyOwner.setStatus("current")
_CfprLsbootPolicyPurpose_Type = CfprLsbootPurpose
_CfprLsbootPolicyPurpose_Object = MibTableColumn
cfprLsbootPolicyPurpose = _CfprLsbootPolicyPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 11),
    _CfprLsbootPolicyPurpose_Type()
)
cfprLsbootPolicyPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyPurpose.setStatus("current")
_CfprLsbootPolicyRebootOnUpdate_Type = TruthValue
_CfprLsbootPolicyRebootOnUpdate_Object = MibTableColumn
cfprLsbootPolicyRebootOnUpdate = _CfprLsbootPolicyRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 10, 1, 12),
    _CfprLsbootPolicyRebootOnUpdate_Type()
)
cfprLsbootPolicyRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootPolicyRebootOnUpdate.setStatus("current")
_CfprLsbootSanTable_Object = MibTable
cfprLsbootSanTable = _CfprLsbootSanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11)
)
if mibBuilder.loadTexts:
    cfprLsbootSanTable.setStatus("current")
_CfprLsbootSanEntry_Object = MibTableRow
cfprLsbootSanEntry = _CfprLsbootSanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1)
)
cfprLsbootSanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootSanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootSanEntry.setStatus("current")
_CfprLsbootSanInstanceId_Type = CfprManagedObjectId
_CfprLsbootSanInstanceId_Object = MibTableColumn
cfprLsbootSanInstanceId = _CfprLsbootSanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1, 1),
    _CfprLsbootSanInstanceId_Type()
)
cfprLsbootSanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootSanInstanceId.setStatus("current")
_CfprLsbootSanDn_Type = CfprManagedObjectDn
_CfprLsbootSanDn_Object = MibTableColumn
cfprLsbootSanDn = _CfprLsbootSanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1, 2),
    _CfprLsbootSanDn_Type()
)
cfprLsbootSanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanDn.setStatus("current")
_CfprLsbootSanRn_Type = SnmpAdminString
_CfprLsbootSanRn_Object = MibTableColumn
cfprLsbootSanRn = _CfprLsbootSanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1, 3),
    _CfprLsbootSanRn_Type()
)
cfprLsbootSanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanRn.setStatus("current")
_CfprLsbootSanAccess_Type = CfprLsbootSanAccess
_CfprLsbootSanAccess_Object = MibTableColumn
cfprLsbootSanAccess = _CfprLsbootSanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1, 4),
    _CfprLsbootSanAccess_Type()
)
cfprLsbootSanAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanAccess.setStatus("current")
_CfprLsbootSanOrder_Type = Gauge32
_CfprLsbootSanOrder_Object = MibTableColumn
cfprLsbootSanOrder = _CfprLsbootSanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1, 5),
    _CfprLsbootSanOrder_Type()
)
cfprLsbootSanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanOrder.setStatus("current")
_CfprLsbootSanType_Type = CfprLsbootSanType
_CfprLsbootSanType_Object = MibTableColumn
cfprLsbootSanType = _CfprLsbootSanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 11, 1, 6),
    _CfprLsbootSanType_Type()
)
cfprLsbootSanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanType.setStatus("current")
_CfprLsbootSanCatSanImageTable_Object = MibTable
cfprLsbootSanCatSanImageTable = _CfprLsbootSanCatSanImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12)
)
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageTable.setStatus("current")
_CfprLsbootSanCatSanImageEntry_Object = MibTableRow
cfprLsbootSanCatSanImageEntry = _CfprLsbootSanCatSanImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12, 1)
)
cfprLsbootSanCatSanImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootSanCatSanImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageEntry.setStatus("current")
_CfprLsbootSanCatSanImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootSanCatSanImageInstanceId_Object = MibTableColumn
cfprLsbootSanCatSanImageInstanceId = _CfprLsbootSanCatSanImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12, 1, 1),
    _CfprLsbootSanCatSanImageInstanceId_Type()
)
cfprLsbootSanCatSanImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageInstanceId.setStatus("current")
_CfprLsbootSanCatSanImageDn_Type = CfprManagedObjectDn
_CfprLsbootSanCatSanImageDn_Object = MibTableColumn
cfprLsbootSanCatSanImageDn = _CfprLsbootSanCatSanImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12, 1, 2),
    _CfprLsbootSanCatSanImageDn_Type()
)
cfprLsbootSanCatSanImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageDn.setStatus("current")
_CfprLsbootSanCatSanImageRn_Type = SnmpAdminString
_CfprLsbootSanCatSanImageRn_Object = MibTableColumn
cfprLsbootSanCatSanImageRn = _CfprLsbootSanCatSanImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12, 1, 3),
    _CfprLsbootSanCatSanImageRn_Type()
)
cfprLsbootSanCatSanImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageRn.setStatus("current")
_CfprLsbootSanCatSanImageType_Type = CfprLsbootSanCatSanImageType
_CfprLsbootSanCatSanImageType_Object = MibTableColumn
cfprLsbootSanCatSanImageType = _CfprLsbootSanCatSanImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12, 1, 4),
    _CfprLsbootSanCatSanImageType_Type()
)
cfprLsbootSanCatSanImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageType.setStatus("current")
_CfprLsbootSanCatSanImageVnicName_Type = SnmpAdminString
_CfprLsbootSanCatSanImageVnicName_Object = MibTableColumn
cfprLsbootSanCatSanImageVnicName = _CfprLsbootSanCatSanImageVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 12, 1, 5),
    _CfprLsbootSanCatSanImageVnicName_Type()
)
cfprLsbootSanCatSanImageVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImageVnicName.setStatus("current")
_CfprLsbootSanCatSanImagePathTable_Object = MibTable
cfprLsbootSanCatSanImagePathTable = _CfprLsbootSanCatSanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13)
)
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathTable.setStatus("current")
_CfprLsbootSanCatSanImagePathEntry_Object = MibTableRow
cfprLsbootSanCatSanImagePathEntry = _CfprLsbootSanCatSanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1)
)
cfprLsbootSanCatSanImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootSanCatSanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathEntry.setStatus("current")
_CfprLsbootSanCatSanImagePathInstanceId_Type = CfprManagedObjectId
_CfprLsbootSanCatSanImagePathInstanceId_Object = MibTableColumn
cfprLsbootSanCatSanImagePathInstanceId = _CfprLsbootSanCatSanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 1),
    _CfprLsbootSanCatSanImagePathInstanceId_Type()
)
cfprLsbootSanCatSanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathInstanceId.setStatus("current")
_CfprLsbootSanCatSanImagePathDn_Type = CfprManagedObjectDn
_CfprLsbootSanCatSanImagePathDn_Object = MibTableColumn
cfprLsbootSanCatSanImagePathDn = _CfprLsbootSanCatSanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 2),
    _CfprLsbootSanCatSanImagePathDn_Type()
)
cfprLsbootSanCatSanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathDn.setStatus("current")
_CfprLsbootSanCatSanImagePathRn_Type = SnmpAdminString
_CfprLsbootSanCatSanImagePathRn_Object = MibTableColumn
cfprLsbootSanCatSanImagePathRn = _CfprLsbootSanCatSanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 3),
    _CfprLsbootSanCatSanImagePathRn_Type()
)
cfprLsbootSanCatSanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathRn.setStatus("current")
_CfprLsbootSanCatSanImagePathLun_Type = SnmpAdminString
_CfprLsbootSanCatSanImagePathLun_Object = MibTableColumn
cfprLsbootSanCatSanImagePathLun = _CfprLsbootSanCatSanImagePathLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 4),
    _CfprLsbootSanCatSanImagePathLun_Type()
)
cfprLsbootSanCatSanImagePathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathLun.setStatus("current")
_CfprLsbootSanCatSanImagePathType_Type = CfprLsbootSanCatSanImagePathType
_CfprLsbootSanCatSanImagePathType_Object = MibTableColumn
cfprLsbootSanCatSanImagePathType = _CfprLsbootSanCatSanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 5),
    _CfprLsbootSanCatSanImagePathType_Type()
)
cfprLsbootSanCatSanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathType.setStatus("current")
_CfprLsbootSanCatSanImagePathVnicName_Type = SnmpAdminString
_CfprLsbootSanCatSanImagePathVnicName_Object = MibTableColumn
cfprLsbootSanCatSanImagePathVnicName = _CfprLsbootSanCatSanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 6),
    _CfprLsbootSanCatSanImagePathVnicName_Type()
)
cfprLsbootSanCatSanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathVnicName.setStatus("current")
_CfprLsbootSanCatSanImagePathWwn_Type = Unsigned64
_CfprLsbootSanCatSanImagePathWwn_Object = MibTableColumn
cfprLsbootSanCatSanImagePathWwn = _CfprLsbootSanCatSanImagePathWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 13, 1, 7),
    _CfprLsbootSanCatSanImagePathWwn_Type()
)
cfprLsbootSanCatSanImagePathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanCatSanImagePathWwn.setStatus("current")
_CfprLsbootSanImageTable_Object = MibTable
cfprLsbootSanImageTable = _CfprLsbootSanImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14)
)
if mibBuilder.loadTexts:
    cfprLsbootSanImageTable.setStatus("current")
_CfprLsbootSanImageEntry_Object = MibTableRow
cfprLsbootSanImageEntry = _CfprLsbootSanImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14, 1)
)
cfprLsbootSanImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootSanImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootSanImageEntry.setStatus("current")
_CfprLsbootSanImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootSanImageInstanceId_Object = MibTableColumn
cfprLsbootSanImageInstanceId = _CfprLsbootSanImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14, 1, 1),
    _CfprLsbootSanImageInstanceId_Type()
)
cfprLsbootSanImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootSanImageInstanceId.setStatus("current")
_CfprLsbootSanImageDn_Type = CfprManagedObjectDn
_CfprLsbootSanImageDn_Object = MibTableColumn
cfprLsbootSanImageDn = _CfprLsbootSanImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14, 1, 2),
    _CfprLsbootSanImageDn_Type()
)
cfprLsbootSanImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImageDn.setStatus("current")
_CfprLsbootSanImageRn_Type = SnmpAdminString
_CfprLsbootSanImageRn_Object = MibTableColumn
cfprLsbootSanImageRn = _CfprLsbootSanImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14, 1, 3),
    _CfprLsbootSanImageRn_Type()
)
cfprLsbootSanImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImageRn.setStatus("current")
_CfprLsbootSanImageType_Type = CfprLsbootSanImageType
_CfprLsbootSanImageType_Object = MibTableColumn
cfprLsbootSanImageType = _CfprLsbootSanImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14, 1, 4),
    _CfprLsbootSanImageType_Type()
)
cfprLsbootSanImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImageType.setStatus("current")
_CfprLsbootSanImageVnicName_Type = SnmpAdminString
_CfprLsbootSanImageVnicName_Object = MibTableColumn
cfprLsbootSanImageVnicName = _CfprLsbootSanImageVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 14, 1, 5),
    _CfprLsbootSanImageVnicName_Type()
)
cfprLsbootSanImageVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImageVnicName.setStatus("current")
_CfprLsbootSanImagePathTable_Object = MibTable
cfprLsbootSanImagePathTable = _CfprLsbootSanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15)
)
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathTable.setStatus("current")
_CfprLsbootSanImagePathEntry_Object = MibTableRow
cfprLsbootSanImagePathEntry = _CfprLsbootSanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1)
)
cfprLsbootSanImagePathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootSanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathEntry.setStatus("current")
_CfprLsbootSanImagePathInstanceId_Type = CfprManagedObjectId
_CfprLsbootSanImagePathInstanceId_Object = MibTableColumn
cfprLsbootSanImagePathInstanceId = _CfprLsbootSanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 1),
    _CfprLsbootSanImagePathInstanceId_Type()
)
cfprLsbootSanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathInstanceId.setStatus("current")
_CfprLsbootSanImagePathDn_Type = CfprManagedObjectDn
_CfprLsbootSanImagePathDn_Object = MibTableColumn
cfprLsbootSanImagePathDn = _CfprLsbootSanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 2),
    _CfprLsbootSanImagePathDn_Type()
)
cfprLsbootSanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathDn.setStatus("current")
_CfprLsbootSanImagePathRn_Type = SnmpAdminString
_CfprLsbootSanImagePathRn_Object = MibTableColumn
cfprLsbootSanImagePathRn = _CfprLsbootSanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 3),
    _CfprLsbootSanImagePathRn_Type()
)
cfprLsbootSanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathRn.setStatus("current")
_CfprLsbootSanImagePathLun_Type = SnmpAdminString
_CfprLsbootSanImagePathLun_Object = MibTableColumn
cfprLsbootSanImagePathLun = _CfprLsbootSanImagePathLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 4),
    _CfprLsbootSanImagePathLun_Type()
)
cfprLsbootSanImagePathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathLun.setStatus("current")
_CfprLsbootSanImagePathType_Type = CfprLsbootSanImagePathType
_CfprLsbootSanImagePathType_Object = MibTableColumn
cfprLsbootSanImagePathType = _CfprLsbootSanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 5),
    _CfprLsbootSanImagePathType_Type()
)
cfprLsbootSanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathType.setStatus("current")
_CfprLsbootSanImagePathVnicName_Type = SnmpAdminString
_CfprLsbootSanImagePathVnicName_Object = MibTableColumn
cfprLsbootSanImagePathVnicName = _CfprLsbootSanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 6),
    _CfprLsbootSanImagePathVnicName_Type()
)
cfprLsbootSanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathVnicName.setStatus("current")
_CfprLsbootSanImagePathWwn_Type = Unsigned64
_CfprLsbootSanImagePathWwn_Object = MibTableColumn
cfprLsbootSanImagePathWwn = _CfprLsbootSanImagePathWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 15, 1, 7),
    _CfprLsbootSanImagePathWwn_Type()
)
cfprLsbootSanImagePathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootSanImagePathWwn.setStatus("current")
_CfprLsbootStorageTable_Object = MibTable
cfprLsbootStorageTable = _CfprLsbootStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16)
)
if mibBuilder.loadTexts:
    cfprLsbootStorageTable.setStatus("current")
_CfprLsbootStorageEntry_Object = MibTableRow
cfprLsbootStorageEntry = _CfprLsbootStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1)
)
cfprLsbootStorageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootStorageEntry.setStatus("current")
_CfprLsbootStorageInstanceId_Type = CfprManagedObjectId
_CfprLsbootStorageInstanceId_Object = MibTableColumn
cfprLsbootStorageInstanceId = _CfprLsbootStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1, 1),
    _CfprLsbootStorageInstanceId_Type()
)
cfprLsbootStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootStorageInstanceId.setStatus("current")
_CfprLsbootStorageDn_Type = CfprManagedObjectDn
_CfprLsbootStorageDn_Object = MibTableColumn
cfprLsbootStorageDn = _CfprLsbootStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1, 2),
    _CfprLsbootStorageDn_Type()
)
cfprLsbootStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootStorageDn.setStatus("current")
_CfprLsbootStorageRn_Type = SnmpAdminString
_CfprLsbootStorageRn_Object = MibTableColumn
cfprLsbootStorageRn = _CfprLsbootStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1, 3),
    _CfprLsbootStorageRn_Type()
)
cfprLsbootStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootStorageRn.setStatus("current")
_CfprLsbootStorageAccess_Type = CfprLsbootStorageAccess
_CfprLsbootStorageAccess_Object = MibTableColumn
cfprLsbootStorageAccess = _CfprLsbootStorageAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1, 4),
    _CfprLsbootStorageAccess_Type()
)
cfprLsbootStorageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootStorageAccess.setStatus("current")
_CfprLsbootStorageOrder_Type = Gauge32
_CfprLsbootStorageOrder_Object = MibTableColumn
cfprLsbootStorageOrder = _CfprLsbootStorageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1, 5),
    _CfprLsbootStorageOrder_Type()
)
cfprLsbootStorageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootStorageOrder.setStatus("current")
_CfprLsbootStorageType_Type = CfprLsbootStorageType
_CfprLsbootStorageType_Object = MibTableColumn
cfprLsbootStorageType = _CfprLsbootStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 16, 1, 6),
    _CfprLsbootStorageType_Type()
)
cfprLsbootStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootStorageType.setStatus("current")
_CfprLsbootUsbExternalImageTable_Object = MibTable
cfprLsbootUsbExternalImageTable = _CfprLsbootUsbExternalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17)
)
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageTable.setStatus("current")
_CfprLsbootUsbExternalImageEntry_Object = MibTableRow
cfprLsbootUsbExternalImageEntry = _CfprLsbootUsbExternalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17, 1)
)
cfprLsbootUsbExternalImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootUsbExternalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageEntry.setStatus("current")
_CfprLsbootUsbExternalImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootUsbExternalImageInstanceId_Object = MibTableColumn
cfprLsbootUsbExternalImageInstanceId = _CfprLsbootUsbExternalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17, 1, 1),
    _CfprLsbootUsbExternalImageInstanceId_Type()
)
cfprLsbootUsbExternalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageInstanceId.setStatus("current")
_CfprLsbootUsbExternalImageDn_Type = CfprManagedObjectDn
_CfprLsbootUsbExternalImageDn_Object = MibTableColumn
cfprLsbootUsbExternalImageDn = _CfprLsbootUsbExternalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17, 1, 2),
    _CfprLsbootUsbExternalImageDn_Type()
)
cfprLsbootUsbExternalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageDn.setStatus("current")
_CfprLsbootUsbExternalImageRn_Type = SnmpAdminString
_CfprLsbootUsbExternalImageRn_Object = MibTableColumn
cfprLsbootUsbExternalImageRn = _CfprLsbootUsbExternalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17, 1, 3),
    _CfprLsbootUsbExternalImageRn_Type()
)
cfprLsbootUsbExternalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageRn.setStatus("current")
_CfprLsbootUsbExternalImageOrder_Type = Gauge32
_CfprLsbootUsbExternalImageOrder_Object = MibTableColumn
cfprLsbootUsbExternalImageOrder = _CfprLsbootUsbExternalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17, 1, 4),
    _CfprLsbootUsbExternalImageOrder_Type()
)
cfprLsbootUsbExternalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageOrder.setStatus("current")
_CfprLsbootUsbExternalImageType_Type = CfprLsbootUsbExternalImageType
_CfprLsbootUsbExternalImageType_Object = MibTableColumn
cfprLsbootUsbExternalImageType = _CfprLsbootUsbExternalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 17, 1, 5),
    _CfprLsbootUsbExternalImageType_Type()
)
cfprLsbootUsbExternalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbExternalImageType.setStatus("current")
_CfprLsbootUsbFlashStorageImageTable_Object = MibTable
cfprLsbootUsbFlashStorageImageTable = _CfprLsbootUsbFlashStorageImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18)
)
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageTable.setStatus("current")
_CfprLsbootUsbFlashStorageImageEntry_Object = MibTableRow
cfprLsbootUsbFlashStorageImageEntry = _CfprLsbootUsbFlashStorageImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18, 1)
)
cfprLsbootUsbFlashStorageImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootUsbFlashStorageImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageEntry.setStatus("current")
_CfprLsbootUsbFlashStorageImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootUsbFlashStorageImageInstanceId_Object = MibTableColumn
cfprLsbootUsbFlashStorageImageInstanceId = _CfprLsbootUsbFlashStorageImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18, 1, 1),
    _CfprLsbootUsbFlashStorageImageInstanceId_Type()
)
cfprLsbootUsbFlashStorageImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageInstanceId.setStatus("current")
_CfprLsbootUsbFlashStorageImageDn_Type = CfprManagedObjectDn
_CfprLsbootUsbFlashStorageImageDn_Object = MibTableColumn
cfprLsbootUsbFlashStorageImageDn = _CfprLsbootUsbFlashStorageImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18, 1, 2),
    _CfprLsbootUsbFlashStorageImageDn_Type()
)
cfprLsbootUsbFlashStorageImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageDn.setStatus("current")
_CfprLsbootUsbFlashStorageImageRn_Type = SnmpAdminString
_CfprLsbootUsbFlashStorageImageRn_Object = MibTableColumn
cfprLsbootUsbFlashStorageImageRn = _CfprLsbootUsbFlashStorageImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18, 1, 3),
    _CfprLsbootUsbFlashStorageImageRn_Type()
)
cfprLsbootUsbFlashStorageImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageRn.setStatus("current")
_CfprLsbootUsbFlashStorageImageOrder_Type = Gauge32
_CfprLsbootUsbFlashStorageImageOrder_Object = MibTableColumn
cfprLsbootUsbFlashStorageImageOrder = _CfprLsbootUsbFlashStorageImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18, 1, 4),
    _CfprLsbootUsbFlashStorageImageOrder_Type()
)
cfprLsbootUsbFlashStorageImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageOrder.setStatus("current")
_CfprLsbootUsbFlashStorageImageType_Type = CfprLsbootUsbFlashStorageImageType
_CfprLsbootUsbFlashStorageImageType_Object = MibTableColumn
cfprLsbootUsbFlashStorageImageType = _CfprLsbootUsbFlashStorageImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 18, 1, 5),
    _CfprLsbootUsbFlashStorageImageType_Type()
)
cfprLsbootUsbFlashStorageImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbFlashStorageImageType.setStatus("current")
_CfprLsbootUsbInternalImageTable_Object = MibTable
cfprLsbootUsbInternalImageTable = _CfprLsbootUsbInternalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19)
)
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageTable.setStatus("current")
_CfprLsbootUsbInternalImageEntry_Object = MibTableRow
cfprLsbootUsbInternalImageEntry = _CfprLsbootUsbInternalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19, 1)
)
cfprLsbootUsbInternalImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootUsbInternalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageEntry.setStatus("current")
_CfprLsbootUsbInternalImageInstanceId_Type = CfprManagedObjectId
_CfprLsbootUsbInternalImageInstanceId_Object = MibTableColumn
cfprLsbootUsbInternalImageInstanceId = _CfprLsbootUsbInternalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19, 1, 1),
    _CfprLsbootUsbInternalImageInstanceId_Type()
)
cfprLsbootUsbInternalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageInstanceId.setStatus("current")
_CfprLsbootUsbInternalImageDn_Type = CfprManagedObjectDn
_CfprLsbootUsbInternalImageDn_Object = MibTableColumn
cfprLsbootUsbInternalImageDn = _CfprLsbootUsbInternalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19, 1, 2),
    _CfprLsbootUsbInternalImageDn_Type()
)
cfprLsbootUsbInternalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageDn.setStatus("current")
_CfprLsbootUsbInternalImageRn_Type = SnmpAdminString
_CfprLsbootUsbInternalImageRn_Object = MibTableColumn
cfprLsbootUsbInternalImageRn = _CfprLsbootUsbInternalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19, 1, 3),
    _CfprLsbootUsbInternalImageRn_Type()
)
cfprLsbootUsbInternalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageRn.setStatus("current")
_CfprLsbootUsbInternalImageOrder_Type = Gauge32
_CfprLsbootUsbInternalImageOrder_Object = MibTableColumn
cfprLsbootUsbInternalImageOrder = _CfprLsbootUsbInternalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19, 1, 4),
    _CfprLsbootUsbInternalImageOrder_Type()
)
cfprLsbootUsbInternalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageOrder.setStatus("current")
_CfprLsbootUsbInternalImageType_Type = CfprLsbootUsbInternalImageType
_CfprLsbootUsbInternalImageType_Object = MibTableColumn
cfprLsbootUsbInternalImageType = _CfprLsbootUsbInternalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 19, 1, 5),
    _CfprLsbootUsbInternalImageType_Type()
)
cfprLsbootUsbInternalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootUsbInternalImageType.setStatus("current")
_CfprLsbootVirtualMediaTable_Object = MibTable
cfprLsbootVirtualMediaTable = _CfprLsbootVirtualMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20)
)
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaTable.setStatus("current")
_CfprLsbootVirtualMediaEntry_Object = MibTableRow
cfprLsbootVirtualMediaEntry = _CfprLsbootVirtualMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1)
)
cfprLsbootVirtualMediaEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSBOOT-MIB", "cfprLsbootVirtualMediaInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaEntry.setStatus("current")
_CfprLsbootVirtualMediaInstanceId_Type = CfprManagedObjectId
_CfprLsbootVirtualMediaInstanceId_Object = MibTableColumn
cfprLsbootVirtualMediaInstanceId = _CfprLsbootVirtualMediaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 1),
    _CfprLsbootVirtualMediaInstanceId_Type()
)
cfprLsbootVirtualMediaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaInstanceId.setStatus("current")
_CfprLsbootVirtualMediaDn_Type = CfprManagedObjectDn
_CfprLsbootVirtualMediaDn_Object = MibTableColumn
cfprLsbootVirtualMediaDn = _CfprLsbootVirtualMediaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 2),
    _CfprLsbootVirtualMediaDn_Type()
)
cfprLsbootVirtualMediaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaDn.setStatus("current")
_CfprLsbootVirtualMediaRn_Type = SnmpAdminString
_CfprLsbootVirtualMediaRn_Object = MibTableColumn
cfprLsbootVirtualMediaRn = _CfprLsbootVirtualMediaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 3),
    _CfprLsbootVirtualMediaRn_Type()
)
cfprLsbootVirtualMediaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaRn.setStatus("current")
_CfprLsbootVirtualMediaAccess_Type = CfprLsbootAccessType
_CfprLsbootVirtualMediaAccess_Object = MibTableColumn
cfprLsbootVirtualMediaAccess = _CfprLsbootVirtualMediaAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 4),
    _CfprLsbootVirtualMediaAccess_Type()
)
cfprLsbootVirtualMediaAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaAccess.setStatus("current")
_CfprLsbootVirtualMediaLunId_Type = SnmpAdminString
_CfprLsbootVirtualMediaLunId_Object = MibTableColumn
cfprLsbootVirtualMediaLunId = _CfprLsbootVirtualMediaLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 5),
    _CfprLsbootVirtualMediaLunId_Type()
)
cfprLsbootVirtualMediaLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaLunId.setStatus("current")
_CfprLsbootVirtualMediaMappingName_Type = SnmpAdminString
_CfprLsbootVirtualMediaMappingName_Object = MibTableColumn
cfprLsbootVirtualMediaMappingName = _CfprLsbootVirtualMediaMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 6),
    _CfprLsbootVirtualMediaMappingName_Type()
)
cfprLsbootVirtualMediaMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaMappingName.setStatus("current")
_CfprLsbootVirtualMediaOrder_Type = Gauge32
_CfprLsbootVirtualMediaOrder_Object = MibTableColumn
cfprLsbootVirtualMediaOrder = _CfprLsbootVirtualMediaOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 7),
    _CfprLsbootVirtualMediaOrder_Type()
)
cfprLsbootVirtualMediaOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaOrder.setStatus("current")
_CfprLsbootVirtualMediaType_Type = CfprLsbootVirtualMediaType
_CfprLsbootVirtualMediaType_Object = MibTableColumn
cfprLsbootVirtualMediaType = _CfprLsbootVirtualMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 47, 20, 1, 8),
    _CfprLsbootVirtualMediaType_Type()
)
cfprLsbootVirtualMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsbootVirtualMediaType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-LSBOOT-MIB",
    **{"cfprLsbootObjects": cfprLsbootObjects,
       "cfprLsbootBootSecurityTable": cfprLsbootBootSecurityTable,
       "cfprLsbootBootSecurityEntry": cfprLsbootBootSecurityEntry,
       "cfprLsbootBootSecurityInstanceId": cfprLsbootBootSecurityInstanceId,
       "cfprLsbootBootSecurityDn": cfprLsbootBootSecurityDn,
       "cfprLsbootBootSecurityRn": cfprLsbootBootSecurityRn,
       "cfprLsbootBootSecuritySecureBoot": cfprLsbootBootSecuritySecureBoot,
       "cfprLsbootDefTable": cfprLsbootDefTable,
       "cfprLsbootDefEntry": cfprLsbootDefEntry,
       "cfprLsbootDefInstanceId": cfprLsbootDefInstanceId,
       "cfprLsbootDefDn": cfprLsbootDefDn,
       "cfprLsbootDefRn": cfprLsbootDefRn,
       "cfprLsbootDefAdvBootOrderApplicable": cfprLsbootDefAdvBootOrderApplicable,
       "cfprLsbootDefBootMode": cfprLsbootDefBootMode,
       "cfprLsbootDefDescr": cfprLsbootDefDescr,
       "cfprLsbootDefEnforceVnicName": cfprLsbootDefEnforceVnicName,
       "cfprLsbootDefIntId": cfprLsbootDefIntId,
       "cfprLsbootDefName": cfprLsbootDefName,
       "cfprLsbootDefPolicyLevel": cfprLsbootDefPolicyLevel,
       "cfprLsbootDefPolicyOwner": cfprLsbootDefPolicyOwner,
       "cfprLsbootDefPurpose": cfprLsbootDefPurpose,
       "cfprLsbootDefRebootOnUpdate": cfprLsbootDefRebootOnUpdate,
       "cfprLsbootDefaultLocalImageTable": cfprLsbootDefaultLocalImageTable,
       "cfprLsbootDefaultLocalImageEntry": cfprLsbootDefaultLocalImageEntry,
       "cfprLsbootDefaultLocalImageInstanceId": cfprLsbootDefaultLocalImageInstanceId,
       "cfprLsbootDefaultLocalImageDn": cfprLsbootDefaultLocalImageDn,
       "cfprLsbootDefaultLocalImageRn": cfprLsbootDefaultLocalImageRn,
       "cfprLsbootDefaultLocalImageOrder": cfprLsbootDefaultLocalImageOrder,
       "cfprLsbootDefaultLocalImageType": cfprLsbootDefaultLocalImageType,
       "cfprLsbootIScsiTable": cfprLsbootIScsiTable,
       "cfprLsbootIScsiEntry": cfprLsbootIScsiEntry,
       "cfprLsbootIScsiInstanceId": cfprLsbootIScsiInstanceId,
       "cfprLsbootIScsiDn": cfprLsbootIScsiDn,
       "cfprLsbootIScsiRn": cfprLsbootIScsiRn,
       "cfprLsbootIScsiAccess": cfprLsbootIScsiAccess,
       "cfprLsbootIScsiOrder": cfprLsbootIScsiOrder,
       "cfprLsbootIScsiType": cfprLsbootIScsiType,
       "cfprLsbootIScsiImagePathTable": cfprLsbootIScsiImagePathTable,
       "cfprLsbootIScsiImagePathEntry": cfprLsbootIScsiImagePathEntry,
       "cfprLsbootIScsiImagePathInstanceId": cfprLsbootIScsiImagePathInstanceId,
       "cfprLsbootIScsiImagePathDn": cfprLsbootIScsiImagePathDn,
       "cfprLsbootIScsiImagePathRn": cfprLsbootIScsiImagePathRn,
       "cfprLsbootIScsiImagePathISCSIVnicName": cfprLsbootIScsiImagePathISCSIVnicName,
       "cfprLsbootIScsiImagePathType": cfprLsbootIScsiImagePathType,
       "cfprLsbootIScsiImagePathVnicName": cfprLsbootIScsiImagePathVnicName,
       "cfprLsbootLanTable": cfprLsbootLanTable,
       "cfprLsbootLanEntry": cfprLsbootLanEntry,
       "cfprLsbootLanInstanceId": cfprLsbootLanInstanceId,
       "cfprLsbootLanDn": cfprLsbootLanDn,
       "cfprLsbootLanRn": cfprLsbootLanRn,
       "cfprLsbootLanAccess": cfprLsbootLanAccess,
       "cfprLsbootLanOrder": cfprLsbootLanOrder,
       "cfprLsbootLanProt": cfprLsbootLanProt,
       "cfprLsbootLanType": cfprLsbootLanType,
       "cfprLsbootLanImagePathTable": cfprLsbootLanImagePathTable,
       "cfprLsbootLanImagePathEntry": cfprLsbootLanImagePathEntry,
       "cfprLsbootLanImagePathInstanceId": cfprLsbootLanImagePathInstanceId,
       "cfprLsbootLanImagePathDn": cfprLsbootLanImagePathDn,
       "cfprLsbootLanImagePathRn": cfprLsbootLanImagePathRn,
       "cfprLsbootLanImagePathBootIpPolicyName": cfprLsbootLanImagePathBootIpPolicyName,
       "cfprLsbootLanImagePathISCSIVnicName": cfprLsbootLanImagePathISCSIVnicName,
       "cfprLsbootLanImagePathImgPolicyName": cfprLsbootLanImagePathImgPolicyName,
       "cfprLsbootLanImagePathImgSecPolicyName": cfprLsbootLanImagePathImgSecPolicyName,
       "cfprLsbootLanImagePathProvSrvPolicyName": cfprLsbootLanImagePathProvSrvPolicyName,
       "cfprLsbootLanImagePathType": cfprLsbootLanImagePathType,
       "cfprLsbootLanImagePathVnicName": cfprLsbootLanImagePathVnicName,
       "cfprLsbootLocalHddImageTable": cfprLsbootLocalHddImageTable,
       "cfprLsbootLocalHddImageEntry": cfprLsbootLocalHddImageEntry,
       "cfprLsbootLocalHddImageInstanceId": cfprLsbootLocalHddImageInstanceId,
       "cfprLsbootLocalHddImageDn": cfprLsbootLocalHddImageDn,
       "cfprLsbootLocalHddImageRn": cfprLsbootLocalHddImageRn,
       "cfprLsbootLocalHddImageOrder": cfprLsbootLocalHddImageOrder,
       "cfprLsbootLocalHddImageType": cfprLsbootLocalHddImageType,
       "cfprLsbootLocalStorageTable": cfprLsbootLocalStorageTable,
       "cfprLsbootLocalStorageEntry": cfprLsbootLocalStorageEntry,
       "cfprLsbootLocalStorageInstanceId": cfprLsbootLocalStorageInstanceId,
       "cfprLsbootLocalStorageDn": cfprLsbootLocalStorageDn,
       "cfprLsbootLocalStorageRn": cfprLsbootLocalStorageRn,
       "cfprLsbootPolicyTable": cfprLsbootPolicyTable,
       "cfprLsbootPolicyEntry": cfprLsbootPolicyEntry,
       "cfprLsbootPolicyInstanceId": cfprLsbootPolicyInstanceId,
       "cfprLsbootPolicyDn": cfprLsbootPolicyDn,
       "cfprLsbootPolicyRn": cfprLsbootPolicyRn,
       "cfprLsbootPolicyBootMode": cfprLsbootPolicyBootMode,
       "cfprLsbootPolicyDescr": cfprLsbootPolicyDescr,
       "cfprLsbootPolicyEnforceVnicName": cfprLsbootPolicyEnforceVnicName,
       "cfprLsbootPolicyIntId": cfprLsbootPolicyIntId,
       "cfprLsbootPolicyName": cfprLsbootPolicyName,
       "cfprLsbootPolicyPolicyLevel": cfprLsbootPolicyPolicyLevel,
       "cfprLsbootPolicyPolicyOwner": cfprLsbootPolicyPolicyOwner,
       "cfprLsbootPolicyPurpose": cfprLsbootPolicyPurpose,
       "cfprLsbootPolicyRebootOnUpdate": cfprLsbootPolicyRebootOnUpdate,
       "cfprLsbootSanTable": cfprLsbootSanTable,
       "cfprLsbootSanEntry": cfprLsbootSanEntry,
       "cfprLsbootSanInstanceId": cfprLsbootSanInstanceId,
       "cfprLsbootSanDn": cfprLsbootSanDn,
       "cfprLsbootSanRn": cfprLsbootSanRn,
       "cfprLsbootSanAccess": cfprLsbootSanAccess,
       "cfprLsbootSanOrder": cfprLsbootSanOrder,
       "cfprLsbootSanType": cfprLsbootSanType,
       "cfprLsbootSanCatSanImageTable": cfprLsbootSanCatSanImageTable,
       "cfprLsbootSanCatSanImageEntry": cfprLsbootSanCatSanImageEntry,
       "cfprLsbootSanCatSanImageInstanceId": cfprLsbootSanCatSanImageInstanceId,
       "cfprLsbootSanCatSanImageDn": cfprLsbootSanCatSanImageDn,
       "cfprLsbootSanCatSanImageRn": cfprLsbootSanCatSanImageRn,
       "cfprLsbootSanCatSanImageType": cfprLsbootSanCatSanImageType,
       "cfprLsbootSanCatSanImageVnicName": cfprLsbootSanCatSanImageVnicName,
       "cfprLsbootSanCatSanImagePathTable": cfprLsbootSanCatSanImagePathTable,
       "cfprLsbootSanCatSanImagePathEntry": cfprLsbootSanCatSanImagePathEntry,
       "cfprLsbootSanCatSanImagePathInstanceId": cfprLsbootSanCatSanImagePathInstanceId,
       "cfprLsbootSanCatSanImagePathDn": cfprLsbootSanCatSanImagePathDn,
       "cfprLsbootSanCatSanImagePathRn": cfprLsbootSanCatSanImagePathRn,
       "cfprLsbootSanCatSanImagePathLun": cfprLsbootSanCatSanImagePathLun,
       "cfprLsbootSanCatSanImagePathType": cfprLsbootSanCatSanImagePathType,
       "cfprLsbootSanCatSanImagePathVnicName": cfprLsbootSanCatSanImagePathVnicName,
       "cfprLsbootSanCatSanImagePathWwn": cfprLsbootSanCatSanImagePathWwn,
       "cfprLsbootSanImageTable": cfprLsbootSanImageTable,
       "cfprLsbootSanImageEntry": cfprLsbootSanImageEntry,
       "cfprLsbootSanImageInstanceId": cfprLsbootSanImageInstanceId,
       "cfprLsbootSanImageDn": cfprLsbootSanImageDn,
       "cfprLsbootSanImageRn": cfprLsbootSanImageRn,
       "cfprLsbootSanImageType": cfprLsbootSanImageType,
       "cfprLsbootSanImageVnicName": cfprLsbootSanImageVnicName,
       "cfprLsbootSanImagePathTable": cfprLsbootSanImagePathTable,
       "cfprLsbootSanImagePathEntry": cfprLsbootSanImagePathEntry,
       "cfprLsbootSanImagePathInstanceId": cfprLsbootSanImagePathInstanceId,
       "cfprLsbootSanImagePathDn": cfprLsbootSanImagePathDn,
       "cfprLsbootSanImagePathRn": cfprLsbootSanImagePathRn,
       "cfprLsbootSanImagePathLun": cfprLsbootSanImagePathLun,
       "cfprLsbootSanImagePathType": cfprLsbootSanImagePathType,
       "cfprLsbootSanImagePathVnicName": cfprLsbootSanImagePathVnicName,
       "cfprLsbootSanImagePathWwn": cfprLsbootSanImagePathWwn,
       "cfprLsbootStorageTable": cfprLsbootStorageTable,
       "cfprLsbootStorageEntry": cfprLsbootStorageEntry,
       "cfprLsbootStorageInstanceId": cfprLsbootStorageInstanceId,
       "cfprLsbootStorageDn": cfprLsbootStorageDn,
       "cfprLsbootStorageRn": cfprLsbootStorageRn,
       "cfprLsbootStorageAccess": cfprLsbootStorageAccess,
       "cfprLsbootStorageOrder": cfprLsbootStorageOrder,
       "cfprLsbootStorageType": cfprLsbootStorageType,
       "cfprLsbootUsbExternalImageTable": cfprLsbootUsbExternalImageTable,
       "cfprLsbootUsbExternalImageEntry": cfprLsbootUsbExternalImageEntry,
       "cfprLsbootUsbExternalImageInstanceId": cfprLsbootUsbExternalImageInstanceId,
       "cfprLsbootUsbExternalImageDn": cfprLsbootUsbExternalImageDn,
       "cfprLsbootUsbExternalImageRn": cfprLsbootUsbExternalImageRn,
       "cfprLsbootUsbExternalImageOrder": cfprLsbootUsbExternalImageOrder,
       "cfprLsbootUsbExternalImageType": cfprLsbootUsbExternalImageType,
       "cfprLsbootUsbFlashStorageImageTable": cfprLsbootUsbFlashStorageImageTable,
       "cfprLsbootUsbFlashStorageImageEntry": cfprLsbootUsbFlashStorageImageEntry,
       "cfprLsbootUsbFlashStorageImageInstanceId": cfprLsbootUsbFlashStorageImageInstanceId,
       "cfprLsbootUsbFlashStorageImageDn": cfprLsbootUsbFlashStorageImageDn,
       "cfprLsbootUsbFlashStorageImageRn": cfprLsbootUsbFlashStorageImageRn,
       "cfprLsbootUsbFlashStorageImageOrder": cfprLsbootUsbFlashStorageImageOrder,
       "cfprLsbootUsbFlashStorageImageType": cfprLsbootUsbFlashStorageImageType,
       "cfprLsbootUsbInternalImageTable": cfprLsbootUsbInternalImageTable,
       "cfprLsbootUsbInternalImageEntry": cfprLsbootUsbInternalImageEntry,
       "cfprLsbootUsbInternalImageInstanceId": cfprLsbootUsbInternalImageInstanceId,
       "cfprLsbootUsbInternalImageDn": cfprLsbootUsbInternalImageDn,
       "cfprLsbootUsbInternalImageRn": cfprLsbootUsbInternalImageRn,
       "cfprLsbootUsbInternalImageOrder": cfprLsbootUsbInternalImageOrder,
       "cfprLsbootUsbInternalImageType": cfprLsbootUsbInternalImageType,
       "cfprLsbootVirtualMediaTable": cfprLsbootVirtualMediaTable,
       "cfprLsbootVirtualMediaEntry": cfprLsbootVirtualMediaEntry,
       "cfprLsbootVirtualMediaInstanceId": cfprLsbootVirtualMediaInstanceId,
       "cfprLsbootVirtualMediaDn": cfprLsbootVirtualMediaDn,
       "cfprLsbootVirtualMediaRn": cfprLsbootVirtualMediaRn,
       "cfprLsbootVirtualMediaAccess": cfprLsbootVirtualMediaAccess,
       "cfprLsbootVirtualMediaLunId": cfprLsbootVirtualMediaLunId,
       "cfprLsbootVirtualMediaMappingName": cfprLsbootVirtualMediaMappingName,
       "cfprLsbootVirtualMediaOrder": cfprLsbootVirtualMediaOrder,
       "cfprLsbootVirtualMediaType": cfprLsbootVirtualMediaType}
)
