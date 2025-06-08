# SNMP MIB module (CISCO-FIREPOWER-GMETA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-GMETA-MIB.mib
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

(CfprConditionRemoteInvRslt,
 CfprExtpolConnType,
 CfprFsmCompletion,
 CfprFsmFsmStageStatus,
 CfprGmetaCategory,
 CfprGmetaHolderFsmCurrentFsm,
 CfprGmetaHolderFsmStageName,
 CfprGmetaHolderFsmTaskFlags,
 CfprGmetaHolderFsmTaskItem,
 CfprGmetaInventoryStatus,
 CfprGmetaPollInterval,
 CfprMoMoClassId) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprExtpolConnType",
    "CfprFsmCompletion",
    "CfprFsmFsmStageStatus",
    "CfprGmetaCategory",
    "CfprGmetaHolderFsmCurrentFsm",
    "CfprGmetaHolderFsmStageName",
    "CfprGmetaHolderFsmTaskFlags",
    "CfprGmetaHolderFsmTaskItem",
    "CfprGmetaInventoryStatus",
    "CfprGmetaPollInterval",
    "CfprMoMoClassId")

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

cfprGmetaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprGmetaClassTable_Object = MibTable
cfprGmetaClassTable = _CfprGmetaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1)
)
if mibBuilder.loadTexts:
    cfprGmetaClassTable.setStatus("current")
_CfprGmetaClassEntry_Object = MibTableRow
cfprGmetaClassEntry = _CfprGmetaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1)
)
cfprGmetaClassEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaClassInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaClassEntry.setStatus("current")
_CfprGmetaClassInstanceId_Type = CfprManagedObjectId
_CfprGmetaClassInstanceId_Object = MibTableColumn
cfprGmetaClassInstanceId = _CfprGmetaClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 1),
    _CfprGmetaClassInstanceId_Type()
)
cfprGmetaClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaClassInstanceId.setStatus("current")
_CfprGmetaClassDn_Type = CfprManagedObjectDn
_CfprGmetaClassDn_Object = MibTableColumn
cfprGmetaClassDn = _CfprGmetaClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 2),
    _CfprGmetaClassDn_Type()
)
cfprGmetaClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassDn.setStatus("current")
_CfprGmetaClassRn_Type = SnmpAdminString
_CfprGmetaClassRn_Object = MibTableColumn
cfprGmetaClassRn = _CfprGmetaClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 3),
    _CfprGmetaClassRn_Type()
)
cfprGmetaClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassRn.setStatus("current")
_CfprGmetaClassAdminPropMask_Type = Unsigned64
_CfprGmetaClassAdminPropMask_Object = MibTableColumn
cfprGmetaClassAdminPropMask = _CfprGmetaClassAdminPropMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 4),
    _CfprGmetaClassAdminPropMask_Type()
)
cfprGmetaClassAdminPropMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassAdminPropMask.setStatus("current")
_CfprGmetaClassEpClassId_Type = CfprMoMoClassId
_CfprGmetaClassEpClassId_Object = MibTableColumn
cfprGmetaClassEpClassId = _CfprGmetaClassEpClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 5),
    _CfprGmetaClassEpClassId_Type()
)
cfprGmetaClassEpClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassEpClassId.setStatus("current")
_CfprGmetaClassId_Type = Gauge32
_CfprGmetaClassId_Object = MibTableColumn
cfprGmetaClassId = _CfprGmetaClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 6),
    _CfprGmetaClassId_Type()
)
cfprGmetaClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassId.setStatus("current")
_CfprGmetaClassName_Type = SnmpAdminString
_CfprGmetaClassName_Object = MibTableColumn
cfprGmetaClassName = _CfprGmetaClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 7),
    _CfprGmetaClassName_Type()
)
cfprGmetaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassName.setStatus("current")
_CfprGmetaClassOperPropMask_Type = Unsigned64
_CfprGmetaClassOperPropMask_Object = MibTableColumn
cfprGmetaClassOperPropMask = _CfprGmetaClassOperPropMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 1, 1, 8),
    _CfprGmetaClassOperPropMask_Type()
)
cfprGmetaClassOperPropMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaClassOperPropMask.setStatus("current")
_CfprGmetaEpTable_Object = MibTable
cfprGmetaEpTable = _CfprGmetaEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 2)
)
if mibBuilder.loadTexts:
    cfprGmetaEpTable.setStatus("current")
_CfprGmetaEpEntry_Object = MibTableRow
cfprGmetaEpEntry = _CfprGmetaEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 2, 1)
)
cfprGmetaEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaEpEntry.setStatus("current")
_CfprGmetaEpInstanceId_Type = CfprManagedObjectId
_CfprGmetaEpInstanceId_Object = MibTableColumn
cfprGmetaEpInstanceId = _CfprGmetaEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 2, 1, 1),
    _CfprGmetaEpInstanceId_Type()
)
cfprGmetaEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaEpInstanceId.setStatus("current")
_CfprGmetaEpDn_Type = CfprManagedObjectDn
_CfprGmetaEpDn_Object = MibTableColumn
cfprGmetaEpDn = _CfprGmetaEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 2, 1, 2),
    _CfprGmetaEpDn_Type()
)
cfprGmetaEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaEpDn.setStatus("current")
_CfprGmetaEpRn_Type = SnmpAdminString
_CfprGmetaEpRn_Object = MibTableColumn
cfprGmetaEpRn = _CfprGmetaEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 2, 1, 3),
    _CfprGmetaEpRn_Type()
)
cfprGmetaEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaEpRn.setStatus("current")
_CfprGmetaHolderTable_Object = MibTable
cfprGmetaHolderTable = _CfprGmetaHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3)
)
if mibBuilder.loadTexts:
    cfprGmetaHolderTable.setStatus("current")
_CfprGmetaHolderEntry_Object = MibTableRow
cfprGmetaHolderEntry = _CfprGmetaHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1)
)
cfprGmetaHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaHolderEntry.setStatus("current")
_CfprGmetaHolderInstanceId_Type = CfprManagedObjectId
_CfprGmetaHolderInstanceId_Object = MibTableColumn
cfprGmetaHolderInstanceId = _CfprGmetaHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 1),
    _CfprGmetaHolderInstanceId_Type()
)
cfprGmetaHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaHolderInstanceId.setStatus("current")
_CfprGmetaHolderDn_Type = CfprManagedObjectDn
_CfprGmetaHolderDn_Object = MibTableColumn
cfprGmetaHolderDn = _CfprGmetaHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 2),
    _CfprGmetaHolderDn_Type()
)
cfprGmetaHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderDn.setStatus("current")
_CfprGmetaHolderRn_Type = SnmpAdminString
_CfprGmetaHolderRn_Object = MibTableColumn
cfprGmetaHolderRn = _CfprGmetaHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 3),
    _CfprGmetaHolderRn_Type()
)
cfprGmetaHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderRn.setStatus("current")
_CfprGmetaHolderCategory_Type = CfprGmetaCategory
_CfprGmetaHolderCategory_Object = MibTableColumn
cfprGmetaHolderCategory = _CfprGmetaHolderCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 4),
    _CfprGmetaHolderCategory_Type()
)
cfprGmetaHolderCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderCategory.setStatus("current")
_CfprGmetaHolderFsmDescr_Type = SnmpAdminString
_CfprGmetaHolderFsmDescr_Object = MibTableColumn
cfprGmetaHolderFsmDescr = _CfprGmetaHolderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 5),
    _CfprGmetaHolderFsmDescr_Type()
)
cfprGmetaHolderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmDescr.setStatus("current")
_CfprGmetaHolderFsmFlags_Type = SnmpAdminString
_CfprGmetaHolderFsmFlags_Object = MibTableColumn
cfprGmetaHolderFsmFlags = _CfprGmetaHolderFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 6),
    _CfprGmetaHolderFsmFlags_Type()
)
cfprGmetaHolderFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmFlags.setStatus("current")
_CfprGmetaHolderFsmPrev_Type = SnmpAdminString
_CfprGmetaHolderFsmPrev_Object = MibTableColumn
cfprGmetaHolderFsmPrev = _CfprGmetaHolderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 7),
    _CfprGmetaHolderFsmPrev_Type()
)
cfprGmetaHolderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmPrev.setStatus("current")
_CfprGmetaHolderFsmProgr_Type = Gauge32
_CfprGmetaHolderFsmProgr_Object = MibTableColumn
cfprGmetaHolderFsmProgr = _CfprGmetaHolderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 8),
    _CfprGmetaHolderFsmProgr_Type()
)
cfprGmetaHolderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmProgr.setStatus("current")
_CfprGmetaHolderFsmRmtInvErrCode_Type = Gauge32
_CfprGmetaHolderFsmRmtInvErrCode_Object = MibTableColumn
cfprGmetaHolderFsmRmtInvErrCode = _CfprGmetaHolderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 9),
    _CfprGmetaHolderFsmRmtInvErrCode_Type()
)
cfprGmetaHolderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRmtInvErrCode.setStatus("current")
_CfprGmetaHolderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprGmetaHolderFsmRmtInvErrDescr_Object = MibTableColumn
cfprGmetaHolderFsmRmtInvErrDescr = _CfprGmetaHolderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 10),
    _CfprGmetaHolderFsmRmtInvErrDescr_Type()
)
cfprGmetaHolderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRmtInvErrDescr.setStatus("current")
_CfprGmetaHolderFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprGmetaHolderFsmRmtInvRslt_Object = MibTableColumn
cfprGmetaHolderFsmRmtInvRslt = _CfprGmetaHolderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 11),
    _CfprGmetaHolderFsmRmtInvRslt_Type()
)
cfprGmetaHolderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRmtInvRslt.setStatus("current")
_CfprGmetaHolderFsmStageDescr_Type = SnmpAdminString
_CfprGmetaHolderFsmStageDescr_Object = MibTableColumn
cfprGmetaHolderFsmStageDescr = _CfprGmetaHolderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 12),
    _CfprGmetaHolderFsmStageDescr_Type()
)
cfprGmetaHolderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageDescr.setStatus("current")
_CfprGmetaHolderFsmStamp_Type = DateAndTime
_CfprGmetaHolderFsmStamp_Object = MibTableColumn
cfprGmetaHolderFsmStamp = _CfprGmetaHolderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 13),
    _CfprGmetaHolderFsmStamp_Type()
)
cfprGmetaHolderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStamp.setStatus("current")
_CfprGmetaHolderFsmStatus_Type = SnmpAdminString
_CfprGmetaHolderFsmStatus_Object = MibTableColumn
cfprGmetaHolderFsmStatus = _CfprGmetaHolderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 14),
    _CfprGmetaHolderFsmStatus_Type()
)
cfprGmetaHolderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStatus.setStatus("current")
_CfprGmetaHolderFsmTry_Type = Gauge32
_CfprGmetaHolderFsmTry_Object = MibTableColumn
cfprGmetaHolderFsmTry = _CfprGmetaHolderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 15),
    _CfprGmetaHolderFsmTry_Type()
)
cfprGmetaHolderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTry.setStatus("current")
_CfprGmetaHolderInventoryStatus_Type = CfprGmetaInventoryStatus
_CfprGmetaHolderInventoryStatus_Object = MibTableColumn
cfprGmetaHolderInventoryStatus = _CfprGmetaHolderInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 16),
    _CfprGmetaHolderInventoryStatus_Type()
)
cfprGmetaHolderInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderInventoryStatus.setStatus("current")
_CfprGmetaHolderPollInterval_Type = CfprGmetaPollInterval
_CfprGmetaHolderPollInterval_Object = MibTableColumn
cfprGmetaHolderPollInterval = _CfprGmetaHolderPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 17),
    _CfprGmetaHolderPollInterval_Type()
)
cfprGmetaHolderPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderPollInterval.setStatus("current")
_CfprGmetaHolderProvider_Type = CfprExtpolConnType
_CfprGmetaHolderProvider_Object = MibTableColumn
cfprGmetaHolderProvider = _CfprGmetaHolderProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 3, 1, 18),
    _CfprGmetaHolderProvider_Type()
)
cfprGmetaHolderProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderProvider.setStatus("current")
_CfprGmetaHolderFsmTable_Object = MibTable
cfprGmetaHolderFsmTable = _CfprGmetaHolderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4)
)
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTable.setStatus("current")
_CfprGmetaHolderFsmEntry_Object = MibTableRow
cfprGmetaHolderFsmEntry = _CfprGmetaHolderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1)
)
cfprGmetaHolderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaHolderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmEntry.setStatus("current")
_CfprGmetaHolderFsmInstanceId_Type = CfprManagedObjectId
_CfprGmetaHolderFsmInstanceId_Object = MibTableColumn
cfprGmetaHolderFsmInstanceId = _CfprGmetaHolderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 1),
    _CfprGmetaHolderFsmInstanceId_Type()
)
cfprGmetaHolderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmInstanceId.setStatus("current")
_CfprGmetaHolderFsmDn_Type = CfprManagedObjectDn
_CfprGmetaHolderFsmDn_Object = MibTableColumn
cfprGmetaHolderFsmDn = _CfprGmetaHolderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 2),
    _CfprGmetaHolderFsmDn_Type()
)
cfprGmetaHolderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmDn.setStatus("current")
_CfprGmetaHolderFsmRn_Type = SnmpAdminString
_CfprGmetaHolderFsmRn_Object = MibTableColumn
cfprGmetaHolderFsmRn = _CfprGmetaHolderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 3),
    _CfprGmetaHolderFsmRn_Type()
)
cfprGmetaHolderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRn.setStatus("current")
_CfprGmetaHolderFsmCompletionTime_Type = DateAndTime
_CfprGmetaHolderFsmCompletionTime_Object = MibTableColumn
cfprGmetaHolderFsmCompletionTime = _CfprGmetaHolderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 4),
    _CfprGmetaHolderFsmCompletionTime_Type()
)
cfprGmetaHolderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmCompletionTime.setStatus("current")
_CfprGmetaHolderFsmCurrentFsm_Type = CfprGmetaHolderFsmCurrentFsm
_CfprGmetaHolderFsmCurrentFsm_Object = MibTableColumn
cfprGmetaHolderFsmCurrentFsm = _CfprGmetaHolderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 5),
    _CfprGmetaHolderFsmCurrentFsm_Type()
)
cfprGmetaHolderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmCurrentFsm.setStatus("current")
_CfprGmetaHolderFsmDescrData_Type = SnmpAdminString
_CfprGmetaHolderFsmDescrData_Object = MibTableColumn
cfprGmetaHolderFsmDescrData = _CfprGmetaHolderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 6),
    _CfprGmetaHolderFsmDescrData_Type()
)
cfprGmetaHolderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmDescrData.setStatus("current")
_CfprGmetaHolderFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprGmetaHolderFsmFsmStatus_Object = MibTableColumn
cfprGmetaHolderFsmFsmStatus = _CfprGmetaHolderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 7),
    _CfprGmetaHolderFsmFsmStatus_Type()
)
cfprGmetaHolderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmFsmStatus.setStatus("current")
_CfprGmetaHolderFsmProgress_Type = Gauge32
_CfprGmetaHolderFsmProgress_Object = MibTableColumn
cfprGmetaHolderFsmProgress = _CfprGmetaHolderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 8),
    _CfprGmetaHolderFsmProgress_Type()
)
cfprGmetaHolderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmProgress.setStatus("current")
_CfprGmetaHolderFsmRmtErrCode_Type = Gauge32
_CfprGmetaHolderFsmRmtErrCode_Object = MibTableColumn
cfprGmetaHolderFsmRmtErrCode = _CfprGmetaHolderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 9),
    _CfprGmetaHolderFsmRmtErrCode_Type()
)
cfprGmetaHolderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRmtErrCode.setStatus("current")
_CfprGmetaHolderFsmRmtErrDescr_Type = SnmpAdminString
_CfprGmetaHolderFsmRmtErrDescr_Object = MibTableColumn
cfprGmetaHolderFsmRmtErrDescr = _CfprGmetaHolderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 10),
    _CfprGmetaHolderFsmRmtErrDescr_Type()
)
cfprGmetaHolderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRmtErrDescr.setStatus("current")
_CfprGmetaHolderFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprGmetaHolderFsmRmtRslt_Object = MibTableColumn
cfprGmetaHolderFsmRmtRslt = _CfprGmetaHolderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 4, 1, 11),
    _CfprGmetaHolderFsmRmtRslt_Type()
)
cfprGmetaHolderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmRmtRslt.setStatus("current")
_CfprGmetaHolderFsmStageTable_Object = MibTable
cfprGmetaHolderFsmStageTable = _CfprGmetaHolderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5)
)
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageTable.setStatus("current")
_CfprGmetaHolderFsmStageEntry_Object = MibTableRow
cfprGmetaHolderFsmStageEntry = _CfprGmetaHolderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1)
)
cfprGmetaHolderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaHolderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageEntry.setStatus("current")
_CfprGmetaHolderFsmStageInstanceId_Type = CfprManagedObjectId
_CfprGmetaHolderFsmStageInstanceId_Object = MibTableColumn
cfprGmetaHolderFsmStageInstanceId = _CfprGmetaHolderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 1),
    _CfprGmetaHolderFsmStageInstanceId_Type()
)
cfprGmetaHolderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageInstanceId.setStatus("current")
_CfprGmetaHolderFsmStageDn_Type = CfprManagedObjectDn
_CfprGmetaHolderFsmStageDn_Object = MibTableColumn
cfprGmetaHolderFsmStageDn = _CfprGmetaHolderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 2),
    _CfprGmetaHolderFsmStageDn_Type()
)
cfprGmetaHolderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageDn.setStatus("current")
_CfprGmetaHolderFsmStageRn_Type = SnmpAdminString
_CfprGmetaHolderFsmStageRn_Object = MibTableColumn
cfprGmetaHolderFsmStageRn = _CfprGmetaHolderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 3),
    _CfprGmetaHolderFsmStageRn_Type()
)
cfprGmetaHolderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageRn.setStatus("current")
_CfprGmetaHolderFsmStageDescrData_Type = SnmpAdminString
_CfprGmetaHolderFsmStageDescrData_Object = MibTableColumn
cfprGmetaHolderFsmStageDescrData = _CfprGmetaHolderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 4),
    _CfprGmetaHolderFsmStageDescrData_Type()
)
cfprGmetaHolderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageDescrData.setStatus("current")
_CfprGmetaHolderFsmStageLastUpdateTime_Type = DateAndTime
_CfprGmetaHolderFsmStageLastUpdateTime_Object = MibTableColumn
cfprGmetaHolderFsmStageLastUpdateTime = _CfprGmetaHolderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 5),
    _CfprGmetaHolderFsmStageLastUpdateTime_Type()
)
cfprGmetaHolderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageLastUpdateTime.setStatus("current")
_CfprGmetaHolderFsmStageName_Type = CfprGmetaHolderFsmStageName
_CfprGmetaHolderFsmStageName_Object = MibTableColumn
cfprGmetaHolderFsmStageName = _CfprGmetaHolderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 6),
    _CfprGmetaHolderFsmStageName_Type()
)
cfprGmetaHolderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageName.setStatus("current")
_CfprGmetaHolderFsmStageOrder_Type = Gauge32
_CfprGmetaHolderFsmStageOrder_Object = MibTableColumn
cfprGmetaHolderFsmStageOrder = _CfprGmetaHolderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 7),
    _CfprGmetaHolderFsmStageOrder_Type()
)
cfprGmetaHolderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageOrder.setStatus("current")
_CfprGmetaHolderFsmStageRetry_Type = Gauge32
_CfprGmetaHolderFsmStageRetry_Object = MibTableColumn
cfprGmetaHolderFsmStageRetry = _CfprGmetaHolderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 8),
    _CfprGmetaHolderFsmStageRetry_Type()
)
cfprGmetaHolderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageRetry.setStatus("current")
_CfprGmetaHolderFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprGmetaHolderFsmStageStageStatus_Object = MibTableColumn
cfprGmetaHolderFsmStageStageStatus = _CfprGmetaHolderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 5, 1, 9),
    _CfprGmetaHolderFsmStageStageStatus_Type()
)
cfprGmetaHolderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmStageStageStatus.setStatus("current")
_CfprGmetaHolderFsmTaskTable_Object = MibTable
cfprGmetaHolderFsmTaskTable = _CfprGmetaHolderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6)
)
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskTable.setStatus("current")
_CfprGmetaHolderFsmTaskEntry_Object = MibTableRow
cfprGmetaHolderFsmTaskEntry = _CfprGmetaHolderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1)
)
cfprGmetaHolderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaHolderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskEntry.setStatus("current")
_CfprGmetaHolderFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprGmetaHolderFsmTaskInstanceId_Object = MibTableColumn
cfprGmetaHolderFsmTaskInstanceId = _CfprGmetaHolderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 1),
    _CfprGmetaHolderFsmTaskInstanceId_Type()
)
cfprGmetaHolderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskInstanceId.setStatus("current")
_CfprGmetaHolderFsmTaskDn_Type = CfprManagedObjectDn
_CfprGmetaHolderFsmTaskDn_Object = MibTableColumn
cfprGmetaHolderFsmTaskDn = _CfprGmetaHolderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 2),
    _CfprGmetaHolderFsmTaskDn_Type()
)
cfprGmetaHolderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskDn.setStatus("current")
_CfprGmetaHolderFsmTaskRn_Type = SnmpAdminString
_CfprGmetaHolderFsmTaskRn_Object = MibTableColumn
cfprGmetaHolderFsmTaskRn = _CfprGmetaHolderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 3),
    _CfprGmetaHolderFsmTaskRn_Type()
)
cfprGmetaHolderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskRn.setStatus("current")
_CfprGmetaHolderFsmTaskCompletion_Type = CfprFsmCompletion
_CfprGmetaHolderFsmTaskCompletion_Object = MibTableColumn
cfprGmetaHolderFsmTaskCompletion = _CfprGmetaHolderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 4),
    _CfprGmetaHolderFsmTaskCompletion_Type()
)
cfprGmetaHolderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskCompletion.setStatus("current")
_CfprGmetaHolderFsmTaskFlags_Type = CfprGmetaHolderFsmTaskFlags
_CfprGmetaHolderFsmTaskFlags_Object = MibTableColumn
cfprGmetaHolderFsmTaskFlags = _CfprGmetaHolderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 5),
    _CfprGmetaHolderFsmTaskFlags_Type()
)
cfprGmetaHolderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskFlags.setStatus("current")
_CfprGmetaHolderFsmTaskItem_Type = CfprGmetaHolderFsmTaskItem
_CfprGmetaHolderFsmTaskItem_Object = MibTableColumn
cfprGmetaHolderFsmTaskItem = _CfprGmetaHolderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 6),
    _CfprGmetaHolderFsmTaskItem_Type()
)
cfprGmetaHolderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskItem.setStatus("current")
_CfprGmetaHolderFsmTaskSeqId_Type = Gauge32
_CfprGmetaHolderFsmTaskSeqId_Object = MibTableColumn
cfprGmetaHolderFsmTaskSeqId = _CfprGmetaHolderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 6, 1, 7),
    _CfprGmetaHolderFsmTaskSeqId_Type()
)
cfprGmetaHolderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaHolderFsmTaskSeqId.setStatus("current")
_CfprGmetaPolicyMapElementTable_Object = MibTable
cfprGmetaPolicyMapElementTable = _CfprGmetaPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 7)
)
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapElementTable.setStatus("current")
_CfprGmetaPolicyMapElementEntry_Object = MibTableRow
cfprGmetaPolicyMapElementEntry = _CfprGmetaPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 7, 1)
)
cfprGmetaPolicyMapElementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaPolicyMapElementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapElementEntry.setStatus("current")
_CfprGmetaPolicyMapElementInstanceId_Type = CfprManagedObjectId
_CfprGmetaPolicyMapElementInstanceId_Object = MibTableColumn
cfprGmetaPolicyMapElementInstanceId = _CfprGmetaPolicyMapElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 7, 1, 1),
    _CfprGmetaPolicyMapElementInstanceId_Type()
)
cfprGmetaPolicyMapElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapElementInstanceId.setStatus("current")
_CfprGmetaPolicyMapElementDn_Type = CfprManagedObjectDn
_CfprGmetaPolicyMapElementDn_Object = MibTableColumn
cfprGmetaPolicyMapElementDn = _CfprGmetaPolicyMapElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 7, 1, 2),
    _CfprGmetaPolicyMapElementDn_Type()
)
cfprGmetaPolicyMapElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapElementDn.setStatus("current")
_CfprGmetaPolicyMapElementRn_Type = SnmpAdminString
_CfprGmetaPolicyMapElementRn_Object = MibTableColumn
cfprGmetaPolicyMapElementRn = _CfprGmetaPolicyMapElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 7, 1, 3),
    _CfprGmetaPolicyMapElementRn_Type()
)
cfprGmetaPolicyMapElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapElementRn.setStatus("current")
_CfprGmetaPolicyMapElementName_Type = SnmpAdminString
_CfprGmetaPolicyMapElementName_Object = MibTableColumn
cfprGmetaPolicyMapElementName = _CfprGmetaPolicyMapElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 7, 1, 4),
    _CfprGmetaPolicyMapElementName_Type()
)
cfprGmetaPolicyMapElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapElementName.setStatus("current")
_CfprGmetaPolicyMapHolderTable_Object = MibTable
cfprGmetaPolicyMapHolderTable = _CfprGmetaPolicyMapHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 8)
)
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapHolderTable.setStatus("current")
_CfprGmetaPolicyMapHolderEntry_Object = MibTableRow
cfprGmetaPolicyMapHolderEntry = _CfprGmetaPolicyMapHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 8, 1)
)
cfprGmetaPolicyMapHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaPolicyMapHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapHolderEntry.setStatus("current")
_CfprGmetaPolicyMapHolderInstanceId_Type = CfprManagedObjectId
_CfprGmetaPolicyMapHolderInstanceId_Object = MibTableColumn
cfprGmetaPolicyMapHolderInstanceId = _CfprGmetaPolicyMapHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 8, 1, 1),
    _CfprGmetaPolicyMapHolderInstanceId_Type()
)
cfprGmetaPolicyMapHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapHolderInstanceId.setStatus("current")
_CfprGmetaPolicyMapHolderDn_Type = CfprManagedObjectDn
_CfprGmetaPolicyMapHolderDn_Object = MibTableColumn
cfprGmetaPolicyMapHolderDn = _CfprGmetaPolicyMapHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 8, 1, 2),
    _CfprGmetaPolicyMapHolderDn_Type()
)
cfprGmetaPolicyMapHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapHolderDn.setStatus("current")
_CfprGmetaPolicyMapHolderRn_Type = SnmpAdminString
_CfprGmetaPolicyMapHolderRn_Object = MibTableColumn
cfprGmetaPolicyMapHolderRn = _CfprGmetaPolicyMapHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 8, 1, 3),
    _CfprGmetaPolicyMapHolderRn_Type()
)
cfprGmetaPolicyMapHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPolicyMapHolderRn.setStatus("current")
_CfprGmetaPropTable_Object = MibTable
cfprGmetaPropTable = _CfprGmetaPropTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9)
)
if mibBuilder.loadTexts:
    cfprGmetaPropTable.setStatus("current")
_CfprGmetaPropEntry_Object = MibTableRow
cfprGmetaPropEntry = _CfprGmetaPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1)
)
cfprGmetaPropEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-GMETA-MIB", "cfprGmetaPropInstanceId"),
)
if mibBuilder.loadTexts:
    cfprGmetaPropEntry.setStatus("current")
_CfprGmetaPropInstanceId_Type = CfprManagedObjectId
_CfprGmetaPropInstanceId_Object = MibTableColumn
cfprGmetaPropInstanceId = _CfprGmetaPropInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1, 1),
    _CfprGmetaPropInstanceId_Type()
)
cfprGmetaPropInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprGmetaPropInstanceId.setStatus("current")
_CfprGmetaPropDn_Type = CfprManagedObjectDn
_CfprGmetaPropDn_Object = MibTableColumn
cfprGmetaPropDn = _CfprGmetaPropDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1, 2),
    _CfprGmetaPropDn_Type()
)
cfprGmetaPropDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPropDn.setStatus("current")
_CfprGmetaPropRn_Type = SnmpAdminString
_CfprGmetaPropRn_Object = MibTableColumn
cfprGmetaPropRn = _CfprGmetaPropRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1, 3),
    _CfprGmetaPropRn_Type()
)
cfprGmetaPropRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPropRn.setStatus("current")
_CfprGmetaPropName_Type = SnmpAdminString
_CfprGmetaPropName_Object = MibTableColumn
cfprGmetaPropName = _CfprGmetaPropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1, 4),
    _CfprGmetaPropName_Type()
)
cfprGmetaPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPropName.setStatus("current")
_CfprGmetaPropOrder_Type = Gauge32
_CfprGmetaPropOrder_Object = MibTableColumn
cfprGmetaPropOrder = _CfprGmetaPropOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1, 5),
    _CfprGmetaPropOrder_Type()
)
cfprGmetaPropOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPropOrder.setStatus("current")
_CfprGmetaPropPropId_Type = SnmpAdminString
_CfprGmetaPropPropId_Object = MibTableColumn
cfprGmetaPropPropId = _CfprGmetaPropPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 33, 9, 1, 6),
    _CfprGmetaPropPropId_Type()
)
cfprGmetaPropPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprGmetaPropPropId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-GMETA-MIB",
    **{"cfprGmetaObjects": cfprGmetaObjects,
       "cfprGmetaClassTable": cfprGmetaClassTable,
       "cfprGmetaClassEntry": cfprGmetaClassEntry,
       "cfprGmetaClassInstanceId": cfprGmetaClassInstanceId,
       "cfprGmetaClassDn": cfprGmetaClassDn,
       "cfprGmetaClassRn": cfprGmetaClassRn,
       "cfprGmetaClassAdminPropMask": cfprGmetaClassAdminPropMask,
       "cfprGmetaClassEpClassId": cfprGmetaClassEpClassId,
       "cfprGmetaClassId": cfprGmetaClassId,
       "cfprGmetaClassName": cfprGmetaClassName,
       "cfprGmetaClassOperPropMask": cfprGmetaClassOperPropMask,
       "cfprGmetaEpTable": cfprGmetaEpTable,
       "cfprGmetaEpEntry": cfprGmetaEpEntry,
       "cfprGmetaEpInstanceId": cfprGmetaEpInstanceId,
       "cfprGmetaEpDn": cfprGmetaEpDn,
       "cfprGmetaEpRn": cfprGmetaEpRn,
       "cfprGmetaHolderTable": cfprGmetaHolderTable,
       "cfprGmetaHolderEntry": cfprGmetaHolderEntry,
       "cfprGmetaHolderInstanceId": cfprGmetaHolderInstanceId,
       "cfprGmetaHolderDn": cfprGmetaHolderDn,
       "cfprGmetaHolderRn": cfprGmetaHolderRn,
       "cfprGmetaHolderCategory": cfprGmetaHolderCategory,
       "cfprGmetaHolderFsmDescr": cfprGmetaHolderFsmDescr,
       "cfprGmetaHolderFsmFlags": cfprGmetaHolderFsmFlags,
       "cfprGmetaHolderFsmPrev": cfprGmetaHolderFsmPrev,
       "cfprGmetaHolderFsmProgr": cfprGmetaHolderFsmProgr,
       "cfprGmetaHolderFsmRmtInvErrCode": cfprGmetaHolderFsmRmtInvErrCode,
       "cfprGmetaHolderFsmRmtInvErrDescr": cfprGmetaHolderFsmRmtInvErrDescr,
       "cfprGmetaHolderFsmRmtInvRslt": cfprGmetaHolderFsmRmtInvRslt,
       "cfprGmetaHolderFsmStageDescr": cfprGmetaHolderFsmStageDescr,
       "cfprGmetaHolderFsmStamp": cfprGmetaHolderFsmStamp,
       "cfprGmetaHolderFsmStatus": cfprGmetaHolderFsmStatus,
       "cfprGmetaHolderFsmTry": cfprGmetaHolderFsmTry,
       "cfprGmetaHolderInventoryStatus": cfprGmetaHolderInventoryStatus,
       "cfprGmetaHolderPollInterval": cfprGmetaHolderPollInterval,
       "cfprGmetaHolderProvider": cfprGmetaHolderProvider,
       "cfprGmetaHolderFsmTable": cfprGmetaHolderFsmTable,
       "cfprGmetaHolderFsmEntry": cfprGmetaHolderFsmEntry,
       "cfprGmetaHolderFsmInstanceId": cfprGmetaHolderFsmInstanceId,
       "cfprGmetaHolderFsmDn": cfprGmetaHolderFsmDn,
       "cfprGmetaHolderFsmRn": cfprGmetaHolderFsmRn,
       "cfprGmetaHolderFsmCompletionTime": cfprGmetaHolderFsmCompletionTime,
       "cfprGmetaHolderFsmCurrentFsm": cfprGmetaHolderFsmCurrentFsm,
       "cfprGmetaHolderFsmDescrData": cfprGmetaHolderFsmDescrData,
       "cfprGmetaHolderFsmFsmStatus": cfprGmetaHolderFsmFsmStatus,
       "cfprGmetaHolderFsmProgress": cfprGmetaHolderFsmProgress,
       "cfprGmetaHolderFsmRmtErrCode": cfprGmetaHolderFsmRmtErrCode,
       "cfprGmetaHolderFsmRmtErrDescr": cfprGmetaHolderFsmRmtErrDescr,
       "cfprGmetaHolderFsmRmtRslt": cfprGmetaHolderFsmRmtRslt,
       "cfprGmetaHolderFsmStageTable": cfprGmetaHolderFsmStageTable,
       "cfprGmetaHolderFsmStageEntry": cfprGmetaHolderFsmStageEntry,
       "cfprGmetaHolderFsmStageInstanceId": cfprGmetaHolderFsmStageInstanceId,
       "cfprGmetaHolderFsmStageDn": cfprGmetaHolderFsmStageDn,
       "cfprGmetaHolderFsmStageRn": cfprGmetaHolderFsmStageRn,
       "cfprGmetaHolderFsmStageDescrData": cfprGmetaHolderFsmStageDescrData,
       "cfprGmetaHolderFsmStageLastUpdateTime": cfprGmetaHolderFsmStageLastUpdateTime,
       "cfprGmetaHolderFsmStageName": cfprGmetaHolderFsmStageName,
       "cfprGmetaHolderFsmStageOrder": cfprGmetaHolderFsmStageOrder,
       "cfprGmetaHolderFsmStageRetry": cfprGmetaHolderFsmStageRetry,
       "cfprGmetaHolderFsmStageStageStatus": cfprGmetaHolderFsmStageStageStatus,
       "cfprGmetaHolderFsmTaskTable": cfprGmetaHolderFsmTaskTable,
       "cfprGmetaHolderFsmTaskEntry": cfprGmetaHolderFsmTaskEntry,
       "cfprGmetaHolderFsmTaskInstanceId": cfprGmetaHolderFsmTaskInstanceId,
       "cfprGmetaHolderFsmTaskDn": cfprGmetaHolderFsmTaskDn,
       "cfprGmetaHolderFsmTaskRn": cfprGmetaHolderFsmTaskRn,
       "cfprGmetaHolderFsmTaskCompletion": cfprGmetaHolderFsmTaskCompletion,
       "cfprGmetaHolderFsmTaskFlags": cfprGmetaHolderFsmTaskFlags,
       "cfprGmetaHolderFsmTaskItem": cfprGmetaHolderFsmTaskItem,
       "cfprGmetaHolderFsmTaskSeqId": cfprGmetaHolderFsmTaskSeqId,
       "cfprGmetaPolicyMapElementTable": cfprGmetaPolicyMapElementTable,
       "cfprGmetaPolicyMapElementEntry": cfprGmetaPolicyMapElementEntry,
       "cfprGmetaPolicyMapElementInstanceId": cfprGmetaPolicyMapElementInstanceId,
       "cfprGmetaPolicyMapElementDn": cfprGmetaPolicyMapElementDn,
       "cfprGmetaPolicyMapElementRn": cfprGmetaPolicyMapElementRn,
       "cfprGmetaPolicyMapElementName": cfprGmetaPolicyMapElementName,
       "cfprGmetaPolicyMapHolderTable": cfprGmetaPolicyMapHolderTable,
       "cfprGmetaPolicyMapHolderEntry": cfprGmetaPolicyMapHolderEntry,
       "cfprGmetaPolicyMapHolderInstanceId": cfprGmetaPolicyMapHolderInstanceId,
       "cfprGmetaPolicyMapHolderDn": cfprGmetaPolicyMapHolderDn,
       "cfprGmetaPolicyMapHolderRn": cfprGmetaPolicyMapHolderRn,
       "cfprGmetaPropTable": cfprGmetaPropTable,
       "cfprGmetaPropEntry": cfprGmetaPropEntry,
       "cfprGmetaPropInstanceId": cfprGmetaPropInstanceId,
       "cfprGmetaPropDn": cfprGmetaPropDn,
       "cfprGmetaPropRn": cfprGmetaPropRn,
       "cfprGmetaPropName": cfprGmetaPropName,
       "cfprGmetaPropOrder": cfprGmetaPropOrder,
       "cfprGmetaPropPropId": cfprGmetaPropPropId}
)
