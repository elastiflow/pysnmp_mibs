# SNMP MIB module (CISCO-FIREPOWER-AP-GMETA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-GMETA-MIB.mib
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

(CfprApConditionRemoteInvRslt,
 CfprApExtpolConnType,
 CfprApFsmCompletion,
 CfprApFsmFsmStageStatus,
 CfprApGmetaCategory,
 CfprApGmetaHolderFsmCurrentFsm,
 CfprApGmetaHolderFsmStageName,
 CfprApGmetaHolderFsmTaskFlags,
 CfprApGmetaHolderFsmTaskItem,
 CfprApGmetaInventoryStatus,
 CfprApGmetaPollInterval,
 CfprApMoMoClassId) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApExtpolConnType",
    "CfprApFsmCompletion",
    "CfprApFsmFsmStageStatus",
    "CfprApGmetaCategory",
    "CfprApGmetaHolderFsmCurrentFsm",
    "CfprApGmetaHolderFsmStageName",
    "CfprApGmetaHolderFsmTaskFlags",
    "CfprApGmetaHolderFsmTaskItem",
    "CfprApGmetaInventoryStatus",
    "CfprApGmetaPollInterval",
    "CfprApMoMoClassId")

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

cfprApGmetaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApGmetaClassTable_Object = MibTable
cfprApGmetaClassTable = _CfprApGmetaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1)
)
if mibBuilder.loadTexts:
    cfprApGmetaClassTable.setStatus("current")
_CfprApGmetaClassEntry_Object = MibTableRow
cfprApGmetaClassEntry = _CfprApGmetaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1)
)
cfprApGmetaClassEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaClassInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaClassEntry.setStatus("current")
_CfprApGmetaClassInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaClassInstanceId_Object = MibTableColumn
cfprApGmetaClassInstanceId = _CfprApGmetaClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 1),
    _CfprApGmetaClassInstanceId_Type()
)
cfprApGmetaClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaClassInstanceId.setStatus("current")
_CfprApGmetaClassDn_Type = CfprApManagedObjectDn
_CfprApGmetaClassDn_Object = MibTableColumn
cfprApGmetaClassDn = _CfprApGmetaClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 2),
    _CfprApGmetaClassDn_Type()
)
cfprApGmetaClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassDn.setStatus("current")
_CfprApGmetaClassRn_Type = SnmpAdminString
_CfprApGmetaClassRn_Object = MibTableColumn
cfprApGmetaClassRn = _CfprApGmetaClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 3),
    _CfprApGmetaClassRn_Type()
)
cfprApGmetaClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassRn.setStatus("current")
_CfprApGmetaClassAdminPropMask_Type = Unsigned64
_CfprApGmetaClassAdminPropMask_Object = MibTableColumn
cfprApGmetaClassAdminPropMask = _CfprApGmetaClassAdminPropMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 4),
    _CfprApGmetaClassAdminPropMask_Type()
)
cfprApGmetaClassAdminPropMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassAdminPropMask.setStatus("current")
_CfprApGmetaClassEpClassId_Type = CfprApMoMoClassId
_CfprApGmetaClassEpClassId_Object = MibTableColumn
cfprApGmetaClassEpClassId = _CfprApGmetaClassEpClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 5),
    _CfprApGmetaClassEpClassId_Type()
)
cfprApGmetaClassEpClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassEpClassId.setStatus("current")
_CfprApGmetaClassId_Type = Gauge32
_CfprApGmetaClassId_Object = MibTableColumn
cfprApGmetaClassId = _CfprApGmetaClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 6),
    _CfprApGmetaClassId_Type()
)
cfprApGmetaClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassId.setStatus("current")
_CfprApGmetaClassName_Type = SnmpAdminString
_CfprApGmetaClassName_Object = MibTableColumn
cfprApGmetaClassName = _CfprApGmetaClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 7),
    _CfprApGmetaClassName_Type()
)
cfprApGmetaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassName.setStatus("current")
_CfprApGmetaClassOperPropMask_Type = Unsigned64
_CfprApGmetaClassOperPropMask_Object = MibTableColumn
cfprApGmetaClassOperPropMask = _CfprApGmetaClassOperPropMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 1, 1, 8),
    _CfprApGmetaClassOperPropMask_Type()
)
cfprApGmetaClassOperPropMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaClassOperPropMask.setStatus("current")
_CfprApGmetaEpTable_Object = MibTable
cfprApGmetaEpTable = _CfprApGmetaEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 2)
)
if mibBuilder.loadTexts:
    cfprApGmetaEpTable.setStatus("current")
_CfprApGmetaEpEntry_Object = MibTableRow
cfprApGmetaEpEntry = _CfprApGmetaEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 2, 1)
)
cfprApGmetaEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaEpEntry.setStatus("current")
_CfprApGmetaEpInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaEpInstanceId_Object = MibTableColumn
cfprApGmetaEpInstanceId = _CfprApGmetaEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 2, 1, 1),
    _CfprApGmetaEpInstanceId_Type()
)
cfprApGmetaEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaEpInstanceId.setStatus("current")
_CfprApGmetaEpDn_Type = CfprApManagedObjectDn
_CfprApGmetaEpDn_Object = MibTableColumn
cfprApGmetaEpDn = _CfprApGmetaEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 2, 1, 2),
    _CfprApGmetaEpDn_Type()
)
cfprApGmetaEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaEpDn.setStatus("current")
_CfprApGmetaEpRn_Type = SnmpAdminString
_CfprApGmetaEpRn_Object = MibTableColumn
cfprApGmetaEpRn = _CfprApGmetaEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 2, 1, 3),
    _CfprApGmetaEpRn_Type()
)
cfprApGmetaEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaEpRn.setStatus("current")
_CfprApGmetaHolderTable_Object = MibTable
cfprApGmetaHolderTable = _CfprApGmetaHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3)
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderTable.setStatus("current")
_CfprApGmetaHolderEntry_Object = MibTableRow
cfprApGmetaHolderEntry = _CfprApGmetaHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1)
)
cfprApGmetaHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderEntry.setStatus("current")
_CfprApGmetaHolderInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaHolderInstanceId_Object = MibTableColumn
cfprApGmetaHolderInstanceId = _CfprApGmetaHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 1),
    _CfprApGmetaHolderInstanceId_Type()
)
cfprApGmetaHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaHolderInstanceId.setStatus("current")
_CfprApGmetaHolderDn_Type = CfprApManagedObjectDn
_CfprApGmetaHolderDn_Object = MibTableColumn
cfprApGmetaHolderDn = _CfprApGmetaHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 2),
    _CfprApGmetaHolderDn_Type()
)
cfprApGmetaHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderDn.setStatus("current")
_CfprApGmetaHolderRn_Type = SnmpAdminString
_CfprApGmetaHolderRn_Object = MibTableColumn
cfprApGmetaHolderRn = _CfprApGmetaHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 3),
    _CfprApGmetaHolderRn_Type()
)
cfprApGmetaHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderRn.setStatus("current")
_CfprApGmetaHolderCategory_Type = CfprApGmetaCategory
_CfprApGmetaHolderCategory_Object = MibTableColumn
cfprApGmetaHolderCategory = _CfprApGmetaHolderCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 4),
    _CfprApGmetaHolderCategory_Type()
)
cfprApGmetaHolderCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderCategory.setStatus("current")
_CfprApGmetaHolderFsmDescr_Type = SnmpAdminString
_CfprApGmetaHolderFsmDescr_Object = MibTableColumn
cfprApGmetaHolderFsmDescr = _CfprApGmetaHolderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 5),
    _CfprApGmetaHolderFsmDescr_Type()
)
cfprApGmetaHolderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmDescr.setStatus("current")
_CfprApGmetaHolderFsmFlags_Type = SnmpAdminString
_CfprApGmetaHolderFsmFlags_Object = MibTableColumn
cfprApGmetaHolderFsmFlags = _CfprApGmetaHolderFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 6),
    _CfprApGmetaHolderFsmFlags_Type()
)
cfprApGmetaHolderFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmFlags.setStatus("current")
_CfprApGmetaHolderFsmPrev_Type = SnmpAdminString
_CfprApGmetaHolderFsmPrev_Object = MibTableColumn
cfprApGmetaHolderFsmPrev = _CfprApGmetaHolderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 7),
    _CfprApGmetaHolderFsmPrev_Type()
)
cfprApGmetaHolderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmPrev.setStatus("current")
_CfprApGmetaHolderFsmProgr_Type = Gauge32
_CfprApGmetaHolderFsmProgr_Object = MibTableColumn
cfprApGmetaHolderFsmProgr = _CfprApGmetaHolderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 8),
    _CfprApGmetaHolderFsmProgr_Type()
)
cfprApGmetaHolderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmProgr.setStatus("current")
_CfprApGmetaHolderFsmRmtInvErrCode_Type = Gauge32
_CfprApGmetaHolderFsmRmtInvErrCode_Object = MibTableColumn
cfprApGmetaHolderFsmRmtInvErrCode = _CfprApGmetaHolderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 9),
    _CfprApGmetaHolderFsmRmtInvErrCode_Type()
)
cfprApGmetaHolderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRmtInvErrCode.setStatus("current")
_CfprApGmetaHolderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApGmetaHolderFsmRmtInvErrDescr_Object = MibTableColumn
cfprApGmetaHolderFsmRmtInvErrDescr = _CfprApGmetaHolderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 10),
    _CfprApGmetaHolderFsmRmtInvErrDescr_Type()
)
cfprApGmetaHolderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRmtInvErrDescr.setStatus("current")
_CfprApGmetaHolderFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApGmetaHolderFsmRmtInvRslt_Object = MibTableColumn
cfprApGmetaHolderFsmRmtInvRslt = _CfprApGmetaHolderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 11),
    _CfprApGmetaHolderFsmRmtInvRslt_Type()
)
cfprApGmetaHolderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRmtInvRslt.setStatus("current")
_CfprApGmetaHolderFsmStageDescr_Type = SnmpAdminString
_CfprApGmetaHolderFsmStageDescr_Object = MibTableColumn
cfprApGmetaHolderFsmStageDescr = _CfprApGmetaHolderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 12),
    _CfprApGmetaHolderFsmStageDescr_Type()
)
cfprApGmetaHolderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageDescr.setStatus("current")
_CfprApGmetaHolderFsmStamp_Type = DateAndTime
_CfprApGmetaHolderFsmStamp_Object = MibTableColumn
cfprApGmetaHolderFsmStamp = _CfprApGmetaHolderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 13),
    _CfprApGmetaHolderFsmStamp_Type()
)
cfprApGmetaHolderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStamp.setStatus("current")
_CfprApGmetaHolderFsmStatus_Type = SnmpAdminString
_CfprApGmetaHolderFsmStatus_Object = MibTableColumn
cfprApGmetaHolderFsmStatus = _CfprApGmetaHolderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 14),
    _CfprApGmetaHolderFsmStatus_Type()
)
cfprApGmetaHolderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStatus.setStatus("current")
_CfprApGmetaHolderFsmTry_Type = Gauge32
_CfprApGmetaHolderFsmTry_Object = MibTableColumn
cfprApGmetaHolderFsmTry = _CfprApGmetaHolderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 15),
    _CfprApGmetaHolderFsmTry_Type()
)
cfprApGmetaHolderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTry.setStatus("current")
_CfprApGmetaHolderInventoryStatus_Type = CfprApGmetaInventoryStatus
_CfprApGmetaHolderInventoryStatus_Object = MibTableColumn
cfprApGmetaHolderInventoryStatus = _CfprApGmetaHolderInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 16),
    _CfprApGmetaHolderInventoryStatus_Type()
)
cfprApGmetaHolderInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderInventoryStatus.setStatus("current")
_CfprApGmetaHolderPollInterval_Type = CfprApGmetaPollInterval
_CfprApGmetaHolderPollInterval_Object = MibTableColumn
cfprApGmetaHolderPollInterval = _CfprApGmetaHolderPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 17),
    _CfprApGmetaHolderPollInterval_Type()
)
cfprApGmetaHolderPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderPollInterval.setStatus("current")
_CfprApGmetaHolderProvider_Type = CfprApExtpolConnType
_CfprApGmetaHolderProvider_Object = MibTableColumn
cfprApGmetaHolderProvider = _CfprApGmetaHolderProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 3, 1, 18),
    _CfprApGmetaHolderProvider_Type()
)
cfprApGmetaHolderProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderProvider.setStatus("current")
_CfprApGmetaHolderFsmTable_Object = MibTable
cfprApGmetaHolderFsmTable = _CfprApGmetaHolderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4)
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTable.setStatus("current")
_CfprApGmetaHolderFsmEntry_Object = MibTableRow
cfprApGmetaHolderFsmEntry = _CfprApGmetaHolderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1)
)
cfprApGmetaHolderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaHolderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmEntry.setStatus("current")
_CfprApGmetaHolderFsmInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaHolderFsmInstanceId_Object = MibTableColumn
cfprApGmetaHolderFsmInstanceId = _CfprApGmetaHolderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 1),
    _CfprApGmetaHolderFsmInstanceId_Type()
)
cfprApGmetaHolderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmInstanceId.setStatus("current")
_CfprApGmetaHolderFsmDn_Type = CfprApManagedObjectDn
_CfprApGmetaHolderFsmDn_Object = MibTableColumn
cfprApGmetaHolderFsmDn = _CfprApGmetaHolderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 2),
    _CfprApGmetaHolderFsmDn_Type()
)
cfprApGmetaHolderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmDn.setStatus("current")
_CfprApGmetaHolderFsmRn_Type = SnmpAdminString
_CfprApGmetaHolderFsmRn_Object = MibTableColumn
cfprApGmetaHolderFsmRn = _CfprApGmetaHolderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 3),
    _CfprApGmetaHolderFsmRn_Type()
)
cfprApGmetaHolderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRn.setStatus("current")
_CfprApGmetaHolderFsmCompletionTime_Type = DateAndTime
_CfprApGmetaHolderFsmCompletionTime_Object = MibTableColumn
cfprApGmetaHolderFsmCompletionTime = _CfprApGmetaHolderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 4),
    _CfprApGmetaHolderFsmCompletionTime_Type()
)
cfprApGmetaHolderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmCompletionTime.setStatus("current")
_CfprApGmetaHolderFsmCurrentFsm_Type = CfprApGmetaHolderFsmCurrentFsm
_CfprApGmetaHolderFsmCurrentFsm_Object = MibTableColumn
cfprApGmetaHolderFsmCurrentFsm = _CfprApGmetaHolderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 5),
    _CfprApGmetaHolderFsmCurrentFsm_Type()
)
cfprApGmetaHolderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmCurrentFsm.setStatus("current")
_CfprApGmetaHolderFsmDescrData_Type = SnmpAdminString
_CfprApGmetaHolderFsmDescrData_Object = MibTableColumn
cfprApGmetaHolderFsmDescrData = _CfprApGmetaHolderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 6),
    _CfprApGmetaHolderFsmDescrData_Type()
)
cfprApGmetaHolderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmDescrData.setStatus("current")
_CfprApGmetaHolderFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApGmetaHolderFsmFsmStatus_Object = MibTableColumn
cfprApGmetaHolderFsmFsmStatus = _CfprApGmetaHolderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 7),
    _CfprApGmetaHolderFsmFsmStatus_Type()
)
cfprApGmetaHolderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmFsmStatus.setStatus("current")
_CfprApGmetaHolderFsmProgress_Type = Gauge32
_CfprApGmetaHolderFsmProgress_Object = MibTableColumn
cfprApGmetaHolderFsmProgress = _CfprApGmetaHolderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 8),
    _CfprApGmetaHolderFsmProgress_Type()
)
cfprApGmetaHolderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmProgress.setStatus("current")
_CfprApGmetaHolderFsmRmtErrCode_Type = Gauge32
_CfprApGmetaHolderFsmRmtErrCode_Object = MibTableColumn
cfprApGmetaHolderFsmRmtErrCode = _CfprApGmetaHolderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 9),
    _CfprApGmetaHolderFsmRmtErrCode_Type()
)
cfprApGmetaHolderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRmtErrCode.setStatus("current")
_CfprApGmetaHolderFsmRmtErrDescr_Type = SnmpAdminString
_CfprApGmetaHolderFsmRmtErrDescr_Object = MibTableColumn
cfprApGmetaHolderFsmRmtErrDescr = _CfprApGmetaHolderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 10),
    _CfprApGmetaHolderFsmRmtErrDescr_Type()
)
cfprApGmetaHolderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRmtErrDescr.setStatus("current")
_CfprApGmetaHolderFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApGmetaHolderFsmRmtRslt_Object = MibTableColumn
cfprApGmetaHolderFsmRmtRslt = _CfprApGmetaHolderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 4, 1, 11),
    _CfprApGmetaHolderFsmRmtRslt_Type()
)
cfprApGmetaHolderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmRmtRslt.setStatus("current")
_CfprApGmetaHolderFsmStageTable_Object = MibTable
cfprApGmetaHolderFsmStageTable = _CfprApGmetaHolderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5)
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageTable.setStatus("current")
_CfprApGmetaHolderFsmStageEntry_Object = MibTableRow
cfprApGmetaHolderFsmStageEntry = _CfprApGmetaHolderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1)
)
cfprApGmetaHolderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaHolderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageEntry.setStatus("current")
_CfprApGmetaHolderFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaHolderFsmStageInstanceId_Object = MibTableColumn
cfprApGmetaHolderFsmStageInstanceId = _CfprApGmetaHolderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 1),
    _CfprApGmetaHolderFsmStageInstanceId_Type()
)
cfprApGmetaHolderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageInstanceId.setStatus("current")
_CfprApGmetaHolderFsmStageDn_Type = CfprApManagedObjectDn
_CfprApGmetaHolderFsmStageDn_Object = MibTableColumn
cfprApGmetaHolderFsmStageDn = _CfprApGmetaHolderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 2),
    _CfprApGmetaHolderFsmStageDn_Type()
)
cfprApGmetaHolderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageDn.setStatus("current")
_CfprApGmetaHolderFsmStageRn_Type = SnmpAdminString
_CfprApGmetaHolderFsmStageRn_Object = MibTableColumn
cfprApGmetaHolderFsmStageRn = _CfprApGmetaHolderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 3),
    _CfprApGmetaHolderFsmStageRn_Type()
)
cfprApGmetaHolderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageRn.setStatus("current")
_CfprApGmetaHolderFsmStageDescrData_Type = SnmpAdminString
_CfprApGmetaHolderFsmStageDescrData_Object = MibTableColumn
cfprApGmetaHolderFsmStageDescrData = _CfprApGmetaHolderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 4),
    _CfprApGmetaHolderFsmStageDescrData_Type()
)
cfprApGmetaHolderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageDescrData.setStatus("current")
_CfprApGmetaHolderFsmStageLastUpdateTime_Type = DateAndTime
_CfprApGmetaHolderFsmStageLastUpdateTime_Object = MibTableColumn
cfprApGmetaHolderFsmStageLastUpdateTime = _CfprApGmetaHolderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 5),
    _CfprApGmetaHolderFsmStageLastUpdateTime_Type()
)
cfprApGmetaHolderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageLastUpdateTime.setStatus("current")
_CfprApGmetaHolderFsmStageName_Type = CfprApGmetaHolderFsmStageName
_CfprApGmetaHolderFsmStageName_Object = MibTableColumn
cfprApGmetaHolderFsmStageName = _CfprApGmetaHolderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 6),
    _CfprApGmetaHolderFsmStageName_Type()
)
cfprApGmetaHolderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageName.setStatus("current")
_CfprApGmetaHolderFsmStageOrder_Type = Gauge32
_CfprApGmetaHolderFsmStageOrder_Object = MibTableColumn
cfprApGmetaHolderFsmStageOrder = _CfprApGmetaHolderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 7),
    _CfprApGmetaHolderFsmStageOrder_Type()
)
cfprApGmetaHolderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageOrder.setStatus("current")
_CfprApGmetaHolderFsmStageRetry_Type = Gauge32
_CfprApGmetaHolderFsmStageRetry_Object = MibTableColumn
cfprApGmetaHolderFsmStageRetry = _CfprApGmetaHolderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 8),
    _CfprApGmetaHolderFsmStageRetry_Type()
)
cfprApGmetaHolderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageRetry.setStatus("current")
_CfprApGmetaHolderFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApGmetaHolderFsmStageStageStatus_Object = MibTableColumn
cfprApGmetaHolderFsmStageStageStatus = _CfprApGmetaHolderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 5, 1, 9),
    _CfprApGmetaHolderFsmStageStageStatus_Type()
)
cfprApGmetaHolderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmStageStageStatus.setStatus("current")
_CfprApGmetaHolderFsmTaskTable_Object = MibTable
cfprApGmetaHolderFsmTaskTable = _CfprApGmetaHolderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6)
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskTable.setStatus("current")
_CfprApGmetaHolderFsmTaskEntry_Object = MibTableRow
cfprApGmetaHolderFsmTaskEntry = _CfprApGmetaHolderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1)
)
cfprApGmetaHolderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaHolderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskEntry.setStatus("current")
_CfprApGmetaHolderFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaHolderFsmTaskInstanceId_Object = MibTableColumn
cfprApGmetaHolderFsmTaskInstanceId = _CfprApGmetaHolderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 1),
    _CfprApGmetaHolderFsmTaskInstanceId_Type()
)
cfprApGmetaHolderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskInstanceId.setStatus("current")
_CfprApGmetaHolderFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApGmetaHolderFsmTaskDn_Object = MibTableColumn
cfprApGmetaHolderFsmTaskDn = _CfprApGmetaHolderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 2),
    _CfprApGmetaHolderFsmTaskDn_Type()
)
cfprApGmetaHolderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskDn.setStatus("current")
_CfprApGmetaHolderFsmTaskRn_Type = SnmpAdminString
_CfprApGmetaHolderFsmTaskRn_Object = MibTableColumn
cfprApGmetaHolderFsmTaskRn = _CfprApGmetaHolderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 3),
    _CfprApGmetaHolderFsmTaskRn_Type()
)
cfprApGmetaHolderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskRn.setStatus("current")
_CfprApGmetaHolderFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApGmetaHolderFsmTaskCompletion_Object = MibTableColumn
cfprApGmetaHolderFsmTaskCompletion = _CfprApGmetaHolderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 4),
    _CfprApGmetaHolderFsmTaskCompletion_Type()
)
cfprApGmetaHolderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskCompletion.setStatus("current")
_CfprApGmetaHolderFsmTaskFlags_Type = CfprApGmetaHolderFsmTaskFlags
_CfprApGmetaHolderFsmTaskFlags_Object = MibTableColumn
cfprApGmetaHolderFsmTaskFlags = _CfprApGmetaHolderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 5),
    _CfprApGmetaHolderFsmTaskFlags_Type()
)
cfprApGmetaHolderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskFlags.setStatus("current")
_CfprApGmetaHolderFsmTaskItem_Type = CfprApGmetaHolderFsmTaskItem
_CfprApGmetaHolderFsmTaskItem_Object = MibTableColumn
cfprApGmetaHolderFsmTaskItem = _CfprApGmetaHolderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 6),
    _CfprApGmetaHolderFsmTaskItem_Type()
)
cfprApGmetaHolderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskItem.setStatus("current")
_CfprApGmetaHolderFsmTaskSeqId_Type = Gauge32
_CfprApGmetaHolderFsmTaskSeqId_Object = MibTableColumn
cfprApGmetaHolderFsmTaskSeqId = _CfprApGmetaHolderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 6, 1, 7),
    _CfprApGmetaHolderFsmTaskSeqId_Type()
)
cfprApGmetaHolderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaHolderFsmTaskSeqId.setStatus("current")
_CfprApGmetaPolicyMapElementTable_Object = MibTable
cfprApGmetaPolicyMapElementTable = _CfprApGmetaPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 7)
)
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapElementTable.setStatus("current")
_CfprApGmetaPolicyMapElementEntry_Object = MibTableRow
cfprApGmetaPolicyMapElementEntry = _CfprApGmetaPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 7, 1)
)
cfprApGmetaPolicyMapElementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaPolicyMapElementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapElementEntry.setStatus("current")
_CfprApGmetaPolicyMapElementInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaPolicyMapElementInstanceId_Object = MibTableColumn
cfprApGmetaPolicyMapElementInstanceId = _CfprApGmetaPolicyMapElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 7, 1, 1),
    _CfprApGmetaPolicyMapElementInstanceId_Type()
)
cfprApGmetaPolicyMapElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapElementInstanceId.setStatus("current")
_CfprApGmetaPolicyMapElementDn_Type = CfprApManagedObjectDn
_CfprApGmetaPolicyMapElementDn_Object = MibTableColumn
cfprApGmetaPolicyMapElementDn = _CfprApGmetaPolicyMapElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 7, 1, 2),
    _CfprApGmetaPolicyMapElementDn_Type()
)
cfprApGmetaPolicyMapElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapElementDn.setStatus("current")
_CfprApGmetaPolicyMapElementRn_Type = SnmpAdminString
_CfprApGmetaPolicyMapElementRn_Object = MibTableColumn
cfprApGmetaPolicyMapElementRn = _CfprApGmetaPolicyMapElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 7, 1, 3),
    _CfprApGmetaPolicyMapElementRn_Type()
)
cfprApGmetaPolicyMapElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapElementRn.setStatus("current")
_CfprApGmetaPolicyMapElementName_Type = SnmpAdminString
_CfprApGmetaPolicyMapElementName_Object = MibTableColumn
cfprApGmetaPolicyMapElementName = _CfprApGmetaPolicyMapElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 7, 1, 4),
    _CfprApGmetaPolicyMapElementName_Type()
)
cfprApGmetaPolicyMapElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapElementName.setStatus("current")
_CfprApGmetaPolicyMapHolderTable_Object = MibTable
cfprApGmetaPolicyMapHolderTable = _CfprApGmetaPolicyMapHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 8)
)
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapHolderTable.setStatus("current")
_CfprApGmetaPolicyMapHolderEntry_Object = MibTableRow
cfprApGmetaPolicyMapHolderEntry = _CfprApGmetaPolicyMapHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 8, 1)
)
cfprApGmetaPolicyMapHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaPolicyMapHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapHolderEntry.setStatus("current")
_CfprApGmetaPolicyMapHolderInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaPolicyMapHolderInstanceId_Object = MibTableColumn
cfprApGmetaPolicyMapHolderInstanceId = _CfprApGmetaPolicyMapHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 8, 1, 1),
    _CfprApGmetaPolicyMapHolderInstanceId_Type()
)
cfprApGmetaPolicyMapHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapHolderInstanceId.setStatus("current")
_CfprApGmetaPolicyMapHolderDn_Type = CfprApManagedObjectDn
_CfprApGmetaPolicyMapHolderDn_Object = MibTableColumn
cfprApGmetaPolicyMapHolderDn = _CfprApGmetaPolicyMapHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 8, 1, 2),
    _CfprApGmetaPolicyMapHolderDn_Type()
)
cfprApGmetaPolicyMapHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapHolderDn.setStatus("current")
_CfprApGmetaPolicyMapHolderRn_Type = SnmpAdminString
_CfprApGmetaPolicyMapHolderRn_Object = MibTableColumn
cfprApGmetaPolicyMapHolderRn = _CfprApGmetaPolicyMapHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 8, 1, 3),
    _CfprApGmetaPolicyMapHolderRn_Type()
)
cfprApGmetaPolicyMapHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPolicyMapHolderRn.setStatus("current")
_CfprApGmetaPropTable_Object = MibTable
cfprApGmetaPropTable = _CfprApGmetaPropTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9)
)
if mibBuilder.loadTexts:
    cfprApGmetaPropTable.setStatus("current")
_CfprApGmetaPropEntry_Object = MibTableRow
cfprApGmetaPropEntry = _CfprApGmetaPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1)
)
cfprApGmetaPropEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-GMETA-MIB", "cfprApGmetaPropInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApGmetaPropEntry.setStatus("current")
_CfprApGmetaPropInstanceId_Type = CfprApManagedObjectId
_CfprApGmetaPropInstanceId_Object = MibTableColumn
cfprApGmetaPropInstanceId = _CfprApGmetaPropInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1, 1),
    _CfprApGmetaPropInstanceId_Type()
)
cfprApGmetaPropInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApGmetaPropInstanceId.setStatus("current")
_CfprApGmetaPropDn_Type = CfprApManagedObjectDn
_CfprApGmetaPropDn_Object = MibTableColumn
cfprApGmetaPropDn = _CfprApGmetaPropDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1, 2),
    _CfprApGmetaPropDn_Type()
)
cfprApGmetaPropDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPropDn.setStatus("current")
_CfprApGmetaPropRn_Type = SnmpAdminString
_CfprApGmetaPropRn_Object = MibTableColumn
cfprApGmetaPropRn = _CfprApGmetaPropRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1, 3),
    _CfprApGmetaPropRn_Type()
)
cfprApGmetaPropRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPropRn.setStatus("current")
_CfprApGmetaPropName_Type = SnmpAdminString
_CfprApGmetaPropName_Object = MibTableColumn
cfprApGmetaPropName = _CfprApGmetaPropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1, 4),
    _CfprApGmetaPropName_Type()
)
cfprApGmetaPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPropName.setStatus("current")
_CfprApGmetaPropOrder_Type = Gauge32
_CfprApGmetaPropOrder_Object = MibTableColumn
cfprApGmetaPropOrder = _CfprApGmetaPropOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1, 5),
    _CfprApGmetaPropOrder_Type()
)
cfprApGmetaPropOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPropOrder.setStatus("current")
_CfprApGmetaPropPropId_Type = SnmpAdminString
_CfprApGmetaPropPropId_Object = MibTableColumn
cfprApGmetaPropPropId = _CfprApGmetaPropPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 33, 9, 1, 6),
    _CfprApGmetaPropPropId_Type()
)
cfprApGmetaPropPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApGmetaPropPropId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-GMETA-MIB",
    **{"cfprApGmetaObjects": cfprApGmetaObjects,
       "cfprApGmetaClassTable": cfprApGmetaClassTable,
       "cfprApGmetaClassEntry": cfprApGmetaClassEntry,
       "cfprApGmetaClassInstanceId": cfprApGmetaClassInstanceId,
       "cfprApGmetaClassDn": cfprApGmetaClassDn,
       "cfprApGmetaClassRn": cfprApGmetaClassRn,
       "cfprApGmetaClassAdminPropMask": cfprApGmetaClassAdminPropMask,
       "cfprApGmetaClassEpClassId": cfprApGmetaClassEpClassId,
       "cfprApGmetaClassId": cfprApGmetaClassId,
       "cfprApGmetaClassName": cfprApGmetaClassName,
       "cfprApGmetaClassOperPropMask": cfprApGmetaClassOperPropMask,
       "cfprApGmetaEpTable": cfprApGmetaEpTable,
       "cfprApGmetaEpEntry": cfprApGmetaEpEntry,
       "cfprApGmetaEpInstanceId": cfprApGmetaEpInstanceId,
       "cfprApGmetaEpDn": cfprApGmetaEpDn,
       "cfprApGmetaEpRn": cfprApGmetaEpRn,
       "cfprApGmetaHolderTable": cfprApGmetaHolderTable,
       "cfprApGmetaHolderEntry": cfprApGmetaHolderEntry,
       "cfprApGmetaHolderInstanceId": cfprApGmetaHolderInstanceId,
       "cfprApGmetaHolderDn": cfprApGmetaHolderDn,
       "cfprApGmetaHolderRn": cfprApGmetaHolderRn,
       "cfprApGmetaHolderCategory": cfprApGmetaHolderCategory,
       "cfprApGmetaHolderFsmDescr": cfprApGmetaHolderFsmDescr,
       "cfprApGmetaHolderFsmFlags": cfprApGmetaHolderFsmFlags,
       "cfprApGmetaHolderFsmPrev": cfprApGmetaHolderFsmPrev,
       "cfprApGmetaHolderFsmProgr": cfprApGmetaHolderFsmProgr,
       "cfprApGmetaHolderFsmRmtInvErrCode": cfprApGmetaHolderFsmRmtInvErrCode,
       "cfprApGmetaHolderFsmRmtInvErrDescr": cfprApGmetaHolderFsmRmtInvErrDescr,
       "cfprApGmetaHolderFsmRmtInvRslt": cfprApGmetaHolderFsmRmtInvRslt,
       "cfprApGmetaHolderFsmStageDescr": cfprApGmetaHolderFsmStageDescr,
       "cfprApGmetaHolderFsmStamp": cfprApGmetaHolderFsmStamp,
       "cfprApGmetaHolderFsmStatus": cfprApGmetaHolderFsmStatus,
       "cfprApGmetaHolderFsmTry": cfprApGmetaHolderFsmTry,
       "cfprApGmetaHolderInventoryStatus": cfprApGmetaHolderInventoryStatus,
       "cfprApGmetaHolderPollInterval": cfprApGmetaHolderPollInterval,
       "cfprApGmetaHolderProvider": cfprApGmetaHolderProvider,
       "cfprApGmetaHolderFsmTable": cfprApGmetaHolderFsmTable,
       "cfprApGmetaHolderFsmEntry": cfprApGmetaHolderFsmEntry,
       "cfprApGmetaHolderFsmInstanceId": cfprApGmetaHolderFsmInstanceId,
       "cfprApGmetaHolderFsmDn": cfprApGmetaHolderFsmDn,
       "cfprApGmetaHolderFsmRn": cfprApGmetaHolderFsmRn,
       "cfprApGmetaHolderFsmCompletionTime": cfprApGmetaHolderFsmCompletionTime,
       "cfprApGmetaHolderFsmCurrentFsm": cfprApGmetaHolderFsmCurrentFsm,
       "cfprApGmetaHolderFsmDescrData": cfprApGmetaHolderFsmDescrData,
       "cfprApGmetaHolderFsmFsmStatus": cfprApGmetaHolderFsmFsmStatus,
       "cfprApGmetaHolderFsmProgress": cfprApGmetaHolderFsmProgress,
       "cfprApGmetaHolderFsmRmtErrCode": cfprApGmetaHolderFsmRmtErrCode,
       "cfprApGmetaHolderFsmRmtErrDescr": cfprApGmetaHolderFsmRmtErrDescr,
       "cfprApGmetaHolderFsmRmtRslt": cfprApGmetaHolderFsmRmtRslt,
       "cfprApGmetaHolderFsmStageTable": cfprApGmetaHolderFsmStageTable,
       "cfprApGmetaHolderFsmStageEntry": cfprApGmetaHolderFsmStageEntry,
       "cfprApGmetaHolderFsmStageInstanceId": cfprApGmetaHolderFsmStageInstanceId,
       "cfprApGmetaHolderFsmStageDn": cfprApGmetaHolderFsmStageDn,
       "cfprApGmetaHolderFsmStageRn": cfprApGmetaHolderFsmStageRn,
       "cfprApGmetaHolderFsmStageDescrData": cfprApGmetaHolderFsmStageDescrData,
       "cfprApGmetaHolderFsmStageLastUpdateTime": cfprApGmetaHolderFsmStageLastUpdateTime,
       "cfprApGmetaHolderFsmStageName": cfprApGmetaHolderFsmStageName,
       "cfprApGmetaHolderFsmStageOrder": cfprApGmetaHolderFsmStageOrder,
       "cfprApGmetaHolderFsmStageRetry": cfprApGmetaHolderFsmStageRetry,
       "cfprApGmetaHolderFsmStageStageStatus": cfprApGmetaHolderFsmStageStageStatus,
       "cfprApGmetaHolderFsmTaskTable": cfprApGmetaHolderFsmTaskTable,
       "cfprApGmetaHolderFsmTaskEntry": cfprApGmetaHolderFsmTaskEntry,
       "cfprApGmetaHolderFsmTaskInstanceId": cfprApGmetaHolderFsmTaskInstanceId,
       "cfprApGmetaHolderFsmTaskDn": cfprApGmetaHolderFsmTaskDn,
       "cfprApGmetaHolderFsmTaskRn": cfprApGmetaHolderFsmTaskRn,
       "cfprApGmetaHolderFsmTaskCompletion": cfprApGmetaHolderFsmTaskCompletion,
       "cfprApGmetaHolderFsmTaskFlags": cfprApGmetaHolderFsmTaskFlags,
       "cfprApGmetaHolderFsmTaskItem": cfprApGmetaHolderFsmTaskItem,
       "cfprApGmetaHolderFsmTaskSeqId": cfprApGmetaHolderFsmTaskSeqId,
       "cfprApGmetaPolicyMapElementTable": cfprApGmetaPolicyMapElementTable,
       "cfprApGmetaPolicyMapElementEntry": cfprApGmetaPolicyMapElementEntry,
       "cfprApGmetaPolicyMapElementInstanceId": cfprApGmetaPolicyMapElementInstanceId,
       "cfprApGmetaPolicyMapElementDn": cfprApGmetaPolicyMapElementDn,
       "cfprApGmetaPolicyMapElementRn": cfprApGmetaPolicyMapElementRn,
       "cfprApGmetaPolicyMapElementName": cfprApGmetaPolicyMapElementName,
       "cfprApGmetaPolicyMapHolderTable": cfprApGmetaPolicyMapHolderTable,
       "cfprApGmetaPolicyMapHolderEntry": cfprApGmetaPolicyMapHolderEntry,
       "cfprApGmetaPolicyMapHolderInstanceId": cfprApGmetaPolicyMapHolderInstanceId,
       "cfprApGmetaPolicyMapHolderDn": cfprApGmetaPolicyMapHolderDn,
       "cfprApGmetaPolicyMapHolderRn": cfprApGmetaPolicyMapHolderRn,
       "cfprApGmetaPropTable": cfprApGmetaPropTable,
       "cfprApGmetaPropEntry": cfprApGmetaPropEntry,
       "cfprApGmetaPropInstanceId": cfprApGmetaPropInstanceId,
       "cfprApGmetaPropDn": cfprApGmetaPropDn,
       "cfprApGmetaPropRn": cfprApGmetaPropRn,
       "cfprApGmetaPropName": cfprApGmetaPropName,
       "cfprApGmetaPropOrder": cfprApGmetaPropOrder,
       "cfprApGmetaPropPropId": cfprApGmetaPropPropId}
)
