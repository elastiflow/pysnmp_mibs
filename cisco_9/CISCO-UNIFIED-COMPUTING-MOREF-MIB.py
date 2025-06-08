# SNMP MIB module (CISCO-UNIFIED-COMPUTING-MOREF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-MOREF-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:59:13 2025
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

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsConditionRemoteInvRslt,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsMorefAdminState,
 CucsMorefImportRootFsmCurrentFsm,
 CucsMorefImportRootFsmStageName,
 CucsMorefImportRootFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsMorefAdminState",
    "CucsMorefImportRootFsmCurrentFsm",
    "CucsMorefImportRootFsmStageName",
    "CucsMorefImportRootFsmTaskItem")

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

cucsMorefObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsMorefFruRefTable_Object = MibTable
cucsMorefFruRefTable = _CucsMorefFruRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1)
)
if mibBuilder.loadTexts:
    cucsMorefFruRefTable.setStatus("current")
_CucsMorefFruRefEntry_Object = MibTableRow
cucsMorefFruRefEntry = _CucsMorefFruRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1)
)
cucsMorefFruRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefFruRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefFruRefEntry.setStatus("current")
_CucsMorefFruRefInstanceId_Type = CucsManagedObjectId
_CucsMorefFruRefInstanceId_Object = MibTableColumn
cucsMorefFruRefInstanceId = _CucsMorefFruRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 1),
    _CucsMorefFruRefInstanceId_Type()
)
cucsMorefFruRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefFruRefInstanceId.setStatus("current")
_CucsMorefFruRefDn_Type = CucsManagedObjectDn
_CucsMorefFruRefDn_Object = MibTableColumn
cucsMorefFruRefDn = _CucsMorefFruRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 2),
    _CucsMorefFruRefDn_Type()
)
cucsMorefFruRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefFruRefDn.setStatus("current")
_CucsMorefFruRefRn_Type = SnmpAdminString
_CucsMorefFruRefRn_Object = MibTableColumn
cucsMorefFruRefRn = _CucsMorefFruRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 3),
    _CucsMorefFruRefRn_Type()
)
cucsMorefFruRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefFruRefRn.setStatus("current")
_CucsMorefFruRefClassName_Type = SnmpAdminString
_CucsMorefFruRefClassName_Object = MibTableColumn
cucsMorefFruRefClassName = _CucsMorefFruRefClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 4),
    _CucsMorefFruRefClassName_Type()
)
cucsMorefFruRefClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefFruRefClassName.setStatus("current")
_CucsMorefFruRefModel_Type = SnmpAdminString
_CucsMorefFruRefModel_Object = MibTableColumn
cucsMorefFruRefModel = _CucsMorefFruRefModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 5),
    _CucsMorefFruRefModel_Type()
)
cucsMorefFruRefModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefFruRefModel.setStatus("current")
_CucsMorefFruRefSerial_Type = SnmpAdminString
_CucsMorefFruRefSerial_Object = MibTableColumn
cucsMorefFruRefSerial = _CucsMorefFruRefSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 6),
    _CucsMorefFruRefSerial_Type()
)
cucsMorefFruRefSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefFruRefSerial.setStatus("current")
_CucsMorefFruRefVendor_Type = SnmpAdminString
_CucsMorefFruRefVendor_Object = MibTableColumn
cucsMorefFruRefVendor = _CucsMorefFruRefVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 1, 1, 7),
    _CucsMorefFruRefVendor_Type()
)
cucsMorefFruRefVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefFruRefVendor.setStatus("current")
_CucsMorefImportRootTable_Object = MibTable
cucsMorefImportRootTable = _CucsMorefImportRootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2)
)
if mibBuilder.loadTexts:
    cucsMorefImportRootTable.setStatus("current")
_CucsMorefImportRootEntry_Object = MibTableRow
cucsMorefImportRootEntry = _CucsMorefImportRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1)
)
cucsMorefImportRootEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefImportRootInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefImportRootEntry.setStatus("current")
_CucsMorefImportRootInstanceId_Type = CucsManagedObjectId
_CucsMorefImportRootInstanceId_Object = MibTableColumn
cucsMorefImportRootInstanceId = _CucsMorefImportRootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 1),
    _CucsMorefImportRootInstanceId_Type()
)
cucsMorefImportRootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefImportRootInstanceId.setStatus("current")
_CucsMorefImportRootDn_Type = CucsManagedObjectDn
_CucsMorefImportRootDn_Object = MibTableColumn
cucsMorefImportRootDn = _CucsMorefImportRootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 2),
    _CucsMorefImportRootDn_Type()
)
cucsMorefImportRootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootDn.setStatus("current")
_CucsMorefImportRootRn_Type = SnmpAdminString
_CucsMorefImportRootRn_Object = MibTableColumn
cucsMorefImportRootRn = _CucsMorefImportRootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 3),
    _CucsMorefImportRootRn_Type()
)
cucsMorefImportRootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootRn.setStatus("current")
_CucsMorefImportRootFsmDescr_Type = SnmpAdminString
_CucsMorefImportRootFsmDescr_Object = MibTableColumn
cucsMorefImportRootFsmDescr = _CucsMorefImportRootFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 4),
    _CucsMorefImportRootFsmDescr_Type()
)
cucsMorefImportRootFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmDescr.setStatus("current")
_CucsMorefImportRootFsmPrev_Type = SnmpAdminString
_CucsMorefImportRootFsmPrev_Object = MibTableColumn
cucsMorefImportRootFsmPrev = _CucsMorefImportRootFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 5),
    _CucsMorefImportRootFsmPrev_Type()
)
cucsMorefImportRootFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmPrev.setStatus("current")
_CucsMorefImportRootFsmProgr_Type = Gauge32
_CucsMorefImportRootFsmProgr_Object = MibTableColumn
cucsMorefImportRootFsmProgr = _CucsMorefImportRootFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 6),
    _CucsMorefImportRootFsmProgr_Type()
)
cucsMorefImportRootFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmProgr.setStatus("current")
_CucsMorefImportRootFsmRmtInvErrCode_Type = Gauge32
_CucsMorefImportRootFsmRmtInvErrCode_Object = MibTableColumn
cucsMorefImportRootFsmRmtInvErrCode = _CucsMorefImportRootFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 7),
    _CucsMorefImportRootFsmRmtInvErrCode_Type()
)
cucsMorefImportRootFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRmtInvErrCode.setStatus("current")
_CucsMorefImportRootFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMorefImportRootFsmRmtInvErrDescr_Object = MibTableColumn
cucsMorefImportRootFsmRmtInvErrDescr = _CucsMorefImportRootFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 8),
    _CucsMorefImportRootFsmRmtInvErrDescr_Type()
)
cucsMorefImportRootFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRmtInvErrDescr.setStatus("current")
_CucsMorefImportRootFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMorefImportRootFsmRmtInvRslt_Object = MibTableColumn
cucsMorefImportRootFsmRmtInvRslt = _CucsMorefImportRootFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 9),
    _CucsMorefImportRootFsmRmtInvRslt_Type()
)
cucsMorefImportRootFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRmtInvRslt.setStatus("current")
_CucsMorefImportRootFsmStageDescr_Type = SnmpAdminString
_CucsMorefImportRootFsmStageDescr_Object = MibTableColumn
cucsMorefImportRootFsmStageDescr = _CucsMorefImportRootFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 10),
    _CucsMorefImportRootFsmStageDescr_Type()
)
cucsMorefImportRootFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageDescr.setStatus("current")
_CucsMorefImportRootFsmStamp_Type = DateAndTime
_CucsMorefImportRootFsmStamp_Object = MibTableColumn
cucsMorefImportRootFsmStamp = _CucsMorefImportRootFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 11),
    _CucsMorefImportRootFsmStamp_Type()
)
cucsMorefImportRootFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStamp.setStatus("current")
_CucsMorefImportRootFsmStatus_Type = SnmpAdminString
_CucsMorefImportRootFsmStatus_Object = MibTableColumn
cucsMorefImportRootFsmStatus = _CucsMorefImportRootFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 12),
    _CucsMorefImportRootFsmStatus_Type()
)
cucsMorefImportRootFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStatus.setStatus("current")
_CucsMorefImportRootFsmTry_Type = Gauge32
_CucsMorefImportRootFsmTry_Object = MibTableColumn
cucsMorefImportRootFsmTry = _CucsMorefImportRootFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 2, 1, 13),
    _CucsMorefImportRootFsmTry_Type()
)
cucsMorefImportRootFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTry.setStatus("current")
_CucsMorefImportRootFsmTable_Object = MibTable
cucsMorefImportRootFsmTable = _CucsMorefImportRootFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3)
)
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTable.setStatus("current")
_CucsMorefImportRootFsmEntry_Object = MibTableRow
cucsMorefImportRootFsmEntry = _CucsMorefImportRootFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1)
)
cucsMorefImportRootFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefImportRootFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmEntry.setStatus("current")
_CucsMorefImportRootFsmInstanceId_Type = CucsManagedObjectId
_CucsMorefImportRootFsmInstanceId_Object = MibTableColumn
cucsMorefImportRootFsmInstanceId = _CucsMorefImportRootFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 1),
    _CucsMorefImportRootFsmInstanceId_Type()
)
cucsMorefImportRootFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmInstanceId.setStatus("current")
_CucsMorefImportRootFsmDn_Type = CucsManagedObjectDn
_CucsMorefImportRootFsmDn_Object = MibTableColumn
cucsMorefImportRootFsmDn = _CucsMorefImportRootFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 2),
    _CucsMorefImportRootFsmDn_Type()
)
cucsMorefImportRootFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmDn.setStatus("current")
_CucsMorefImportRootFsmRn_Type = SnmpAdminString
_CucsMorefImportRootFsmRn_Object = MibTableColumn
cucsMorefImportRootFsmRn = _CucsMorefImportRootFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 3),
    _CucsMorefImportRootFsmRn_Type()
)
cucsMorefImportRootFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRn.setStatus("current")
_CucsMorefImportRootFsmCompletionTime_Type = DateAndTime
_CucsMorefImportRootFsmCompletionTime_Object = MibTableColumn
cucsMorefImportRootFsmCompletionTime = _CucsMorefImportRootFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 4),
    _CucsMorefImportRootFsmCompletionTime_Type()
)
cucsMorefImportRootFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmCompletionTime.setStatus("current")
_CucsMorefImportRootFsmCurrentFsm_Type = CucsMorefImportRootFsmCurrentFsm
_CucsMorefImportRootFsmCurrentFsm_Object = MibTableColumn
cucsMorefImportRootFsmCurrentFsm = _CucsMorefImportRootFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 5),
    _CucsMorefImportRootFsmCurrentFsm_Type()
)
cucsMorefImportRootFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmCurrentFsm.setStatus("current")
_CucsMorefImportRootFsmDescrData_Type = SnmpAdminString
_CucsMorefImportRootFsmDescrData_Object = MibTableColumn
cucsMorefImportRootFsmDescrData = _CucsMorefImportRootFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 6),
    _CucsMorefImportRootFsmDescrData_Type()
)
cucsMorefImportRootFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmDescrData.setStatus("current")
_CucsMorefImportRootFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMorefImportRootFsmFsmStatus_Object = MibTableColumn
cucsMorefImportRootFsmFsmStatus = _CucsMorefImportRootFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 7),
    _CucsMorefImportRootFsmFsmStatus_Type()
)
cucsMorefImportRootFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmFsmStatus.setStatus("current")
_CucsMorefImportRootFsmProgress_Type = Gauge32
_CucsMorefImportRootFsmProgress_Object = MibTableColumn
cucsMorefImportRootFsmProgress = _CucsMorefImportRootFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 8),
    _CucsMorefImportRootFsmProgress_Type()
)
cucsMorefImportRootFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmProgress.setStatus("current")
_CucsMorefImportRootFsmRmtErrCode_Type = Gauge32
_CucsMorefImportRootFsmRmtErrCode_Object = MibTableColumn
cucsMorefImportRootFsmRmtErrCode = _CucsMorefImportRootFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 9),
    _CucsMorefImportRootFsmRmtErrCode_Type()
)
cucsMorefImportRootFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRmtErrCode.setStatus("current")
_CucsMorefImportRootFsmRmtErrDescr_Type = SnmpAdminString
_CucsMorefImportRootFsmRmtErrDescr_Object = MibTableColumn
cucsMorefImportRootFsmRmtErrDescr = _CucsMorefImportRootFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 10),
    _CucsMorefImportRootFsmRmtErrDescr_Type()
)
cucsMorefImportRootFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRmtErrDescr.setStatus("current")
_CucsMorefImportRootFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMorefImportRootFsmRmtRslt_Object = MibTableColumn
cucsMorefImportRootFsmRmtRslt = _CucsMorefImportRootFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 3, 1, 11),
    _CucsMorefImportRootFsmRmtRslt_Type()
)
cucsMorefImportRootFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmRmtRslt.setStatus("current")
_CucsMorefImportRootFsmStageTable_Object = MibTable
cucsMorefImportRootFsmStageTable = _CucsMorefImportRootFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4)
)
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageTable.setStatus("current")
_CucsMorefImportRootFsmStageEntry_Object = MibTableRow
cucsMorefImportRootFsmStageEntry = _CucsMorefImportRootFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1)
)
cucsMorefImportRootFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefImportRootFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageEntry.setStatus("current")
_CucsMorefImportRootFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMorefImportRootFsmStageInstanceId_Object = MibTableColumn
cucsMorefImportRootFsmStageInstanceId = _CucsMorefImportRootFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 1),
    _CucsMorefImportRootFsmStageInstanceId_Type()
)
cucsMorefImportRootFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageInstanceId.setStatus("current")
_CucsMorefImportRootFsmStageDn_Type = CucsManagedObjectDn
_CucsMorefImportRootFsmStageDn_Object = MibTableColumn
cucsMorefImportRootFsmStageDn = _CucsMorefImportRootFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 2),
    _CucsMorefImportRootFsmStageDn_Type()
)
cucsMorefImportRootFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageDn.setStatus("current")
_CucsMorefImportRootFsmStageRn_Type = SnmpAdminString
_CucsMorefImportRootFsmStageRn_Object = MibTableColumn
cucsMorefImportRootFsmStageRn = _CucsMorefImportRootFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 3),
    _CucsMorefImportRootFsmStageRn_Type()
)
cucsMorefImportRootFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageRn.setStatus("current")
_CucsMorefImportRootFsmStageDescrData_Type = SnmpAdminString
_CucsMorefImportRootFsmStageDescrData_Object = MibTableColumn
cucsMorefImportRootFsmStageDescrData = _CucsMorefImportRootFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 4),
    _CucsMorefImportRootFsmStageDescrData_Type()
)
cucsMorefImportRootFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageDescrData.setStatus("current")
_CucsMorefImportRootFsmStageLastUpdateTime_Type = DateAndTime
_CucsMorefImportRootFsmStageLastUpdateTime_Object = MibTableColumn
cucsMorefImportRootFsmStageLastUpdateTime = _CucsMorefImportRootFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 5),
    _CucsMorefImportRootFsmStageLastUpdateTime_Type()
)
cucsMorefImportRootFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageLastUpdateTime.setStatus("current")
_CucsMorefImportRootFsmStageName_Type = CucsMorefImportRootFsmStageName
_CucsMorefImportRootFsmStageName_Object = MibTableColumn
cucsMorefImportRootFsmStageName = _CucsMorefImportRootFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 6),
    _CucsMorefImportRootFsmStageName_Type()
)
cucsMorefImportRootFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageName.setStatus("current")
_CucsMorefImportRootFsmStageOrder_Type = Gauge32
_CucsMorefImportRootFsmStageOrder_Object = MibTableColumn
cucsMorefImportRootFsmStageOrder = _CucsMorefImportRootFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 7),
    _CucsMorefImportRootFsmStageOrder_Type()
)
cucsMorefImportRootFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageOrder.setStatus("current")
_CucsMorefImportRootFsmStageRetry_Type = Gauge32
_CucsMorefImportRootFsmStageRetry_Object = MibTableColumn
cucsMorefImportRootFsmStageRetry = _CucsMorefImportRootFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 8),
    _CucsMorefImportRootFsmStageRetry_Type()
)
cucsMorefImportRootFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageRetry.setStatus("current")
_CucsMorefImportRootFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMorefImportRootFsmStageStageStatus_Object = MibTableColumn
cucsMorefImportRootFsmStageStageStatus = _CucsMorefImportRootFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 4, 1, 9),
    _CucsMorefImportRootFsmStageStageStatus_Type()
)
cucsMorefImportRootFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmStageStageStatus.setStatus("current")
_CucsMorefImportRootFsmTaskTable_Object = MibTable
cucsMorefImportRootFsmTaskTable = _CucsMorefImportRootFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5)
)
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskTable.setStatus("current")
_CucsMorefImportRootFsmTaskEntry_Object = MibTableRow
cucsMorefImportRootFsmTaskEntry = _CucsMorefImportRootFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1)
)
cucsMorefImportRootFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefImportRootFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskEntry.setStatus("current")
_CucsMorefImportRootFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMorefImportRootFsmTaskInstanceId_Object = MibTableColumn
cucsMorefImportRootFsmTaskInstanceId = _CucsMorefImportRootFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 1),
    _CucsMorefImportRootFsmTaskInstanceId_Type()
)
cucsMorefImportRootFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskInstanceId.setStatus("current")
_CucsMorefImportRootFsmTaskDn_Type = CucsManagedObjectDn
_CucsMorefImportRootFsmTaskDn_Object = MibTableColumn
cucsMorefImportRootFsmTaskDn = _CucsMorefImportRootFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 2),
    _CucsMorefImportRootFsmTaskDn_Type()
)
cucsMorefImportRootFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskDn.setStatus("current")
_CucsMorefImportRootFsmTaskRn_Type = SnmpAdminString
_CucsMorefImportRootFsmTaskRn_Object = MibTableColumn
cucsMorefImportRootFsmTaskRn = _CucsMorefImportRootFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 3),
    _CucsMorefImportRootFsmTaskRn_Type()
)
cucsMorefImportRootFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskRn.setStatus("current")
_CucsMorefImportRootFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMorefImportRootFsmTaskCompletion_Object = MibTableColumn
cucsMorefImportRootFsmTaskCompletion = _CucsMorefImportRootFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 4),
    _CucsMorefImportRootFsmTaskCompletion_Type()
)
cucsMorefImportRootFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskCompletion.setStatus("current")
_CucsMorefImportRootFsmTaskFlags_Type = CucsFsmFlags
_CucsMorefImportRootFsmTaskFlags_Object = MibTableColumn
cucsMorefImportRootFsmTaskFlags = _CucsMorefImportRootFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 5),
    _CucsMorefImportRootFsmTaskFlags_Type()
)
cucsMorefImportRootFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskFlags.setStatus("current")
_CucsMorefImportRootFsmTaskItem_Type = CucsMorefImportRootFsmTaskItem
_CucsMorefImportRootFsmTaskItem_Object = MibTableColumn
cucsMorefImportRootFsmTaskItem = _CucsMorefImportRootFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 6),
    _CucsMorefImportRootFsmTaskItem_Type()
)
cucsMorefImportRootFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskItem.setStatus("current")
_CucsMorefImportRootFsmTaskSeqId_Type = Gauge32
_CucsMorefImportRootFsmTaskSeqId_Object = MibTableColumn
cucsMorefImportRootFsmTaskSeqId = _CucsMorefImportRootFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 5, 1, 7),
    _CucsMorefImportRootFsmTaskSeqId_Type()
)
cucsMorefImportRootFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefImportRootFsmTaskSeqId.setStatus("current")
_CucsMorefPropTable_Object = MibTable
cucsMorefPropTable = _CucsMorefPropTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6)
)
if mibBuilder.loadTexts:
    cucsMorefPropTable.setStatus("current")
_CucsMorefPropEntry_Object = MibTableRow
cucsMorefPropEntry = _CucsMorefPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1)
)
cucsMorefPropEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefPropInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefPropEntry.setStatus("current")
_CucsMorefPropInstanceId_Type = CucsManagedObjectId
_CucsMorefPropInstanceId_Object = MibTableColumn
cucsMorefPropInstanceId = _CucsMorefPropInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1, 1),
    _CucsMorefPropInstanceId_Type()
)
cucsMorefPropInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefPropInstanceId.setStatus("current")
_CucsMorefPropDn_Type = CucsManagedObjectDn
_CucsMorefPropDn_Object = MibTableColumn
cucsMorefPropDn = _CucsMorefPropDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1, 2),
    _CucsMorefPropDn_Type()
)
cucsMorefPropDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefPropDn.setStatus("current")
_CucsMorefPropRn_Type = SnmpAdminString
_CucsMorefPropRn_Object = MibTableColumn
cucsMorefPropRn = _CucsMorefPropRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1, 3),
    _CucsMorefPropRn_Type()
)
cucsMorefPropRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefPropRn.setStatus("current")
_CucsMorefPropAdminState_Type = CucsMorefAdminState
_CucsMorefPropAdminState_Object = MibTableColumn
cucsMorefPropAdminState = _CucsMorefPropAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1, 4),
    _CucsMorefPropAdminState_Type()
)
cucsMorefPropAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefPropAdminState.setStatus("current")
_CucsMorefPropName_Type = SnmpAdminString
_CucsMorefPropName_Object = MibTableColumn
cucsMorefPropName = _CucsMorefPropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1, 5),
    _CucsMorefPropName_Type()
)
cucsMorefPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefPropName.setStatus("current")
_CucsMorefPropValue_Type = SnmpAdminString
_CucsMorefPropValue_Object = MibTableColumn
cucsMorefPropValue = _CucsMorefPropValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 6, 1, 6),
    _CucsMorefPropValue_Type()
)
cucsMorefPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefPropValue.setStatus("current")
_CucsMorefRefTable_Object = MibTable
cucsMorefRefTable = _CucsMorefRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 7)
)
if mibBuilder.loadTexts:
    cucsMorefRefTable.setStatus("current")
_CucsMorefRefEntry_Object = MibTableRow
cucsMorefRefEntry = _CucsMorefRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 7, 1)
)
cucsMorefRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MOREF-MIB", "cucsMorefRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMorefRefEntry.setStatus("current")
_CucsMorefRefInstanceId_Type = CucsManagedObjectId
_CucsMorefRefInstanceId_Object = MibTableColumn
cucsMorefRefInstanceId = _CucsMorefRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 7, 1, 1),
    _CucsMorefRefInstanceId_Type()
)
cucsMorefRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMorefRefInstanceId.setStatus("current")
_CucsMorefRefDn_Type = CucsManagedObjectDn
_CucsMorefRefDn_Object = MibTableColumn
cucsMorefRefDn = _CucsMorefRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 7, 1, 2),
    _CucsMorefRefDn_Type()
)
cucsMorefRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefRefDn.setStatus("current")
_CucsMorefRefRn_Type = SnmpAdminString
_CucsMorefRefRn_Object = MibTableColumn
cucsMorefRefRn = _CucsMorefRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 7, 1, 3),
    _CucsMorefRefRn_Type()
)
cucsMorefRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefRefRn.setStatus("current")
_CucsMorefRefMoRn_Type = SnmpAdminString
_CucsMorefRefMoRn_Object = MibTableColumn
cucsMorefRefMoRn = _CucsMorefRefMoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 92, 7, 1, 6),
    _CucsMorefRefMoRn_Type()
)
cucsMorefRefMoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMorefRefMoRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-MOREF-MIB",
    **{"cucsMorefObjects": cucsMorefObjects,
       "cucsMorefFruRefTable": cucsMorefFruRefTable,
       "cucsMorefFruRefEntry": cucsMorefFruRefEntry,
       "cucsMorefFruRefInstanceId": cucsMorefFruRefInstanceId,
       "cucsMorefFruRefDn": cucsMorefFruRefDn,
       "cucsMorefFruRefRn": cucsMorefFruRefRn,
       "cucsMorefFruRefClassName": cucsMorefFruRefClassName,
       "cucsMorefFruRefModel": cucsMorefFruRefModel,
       "cucsMorefFruRefSerial": cucsMorefFruRefSerial,
       "cucsMorefFruRefVendor": cucsMorefFruRefVendor,
       "cucsMorefImportRootTable": cucsMorefImportRootTable,
       "cucsMorefImportRootEntry": cucsMorefImportRootEntry,
       "cucsMorefImportRootInstanceId": cucsMorefImportRootInstanceId,
       "cucsMorefImportRootDn": cucsMorefImportRootDn,
       "cucsMorefImportRootRn": cucsMorefImportRootRn,
       "cucsMorefImportRootFsmDescr": cucsMorefImportRootFsmDescr,
       "cucsMorefImportRootFsmPrev": cucsMorefImportRootFsmPrev,
       "cucsMorefImportRootFsmProgr": cucsMorefImportRootFsmProgr,
       "cucsMorefImportRootFsmRmtInvErrCode": cucsMorefImportRootFsmRmtInvErrCode,
       "cucsMorefImportRootFsmRmtInvErrDescr": cucsMorefImportRootFsmRmtInvErrDescr,
       "cucsMorefImportRootFsmRmtInvRslt": cucsMorefImportRootFsmRmtInvRslt,
       "cucsMorefImportRootFsmStageDescr": cucsMorefImportRootFsmStageDescr,
       "cucsMorefImportRootFsmStamp": cucsMorefImportRootFsmStamp,
       "cucsMorefImportRootFsmStatus": cucsMorefImportRootFsmStatus,
       "cucsMorefImportRootFsmTry": cucsMorefImportRootFsmTry,
       "cucsMorefImportRootFsmTable": cucsMorefImportRootFsmTable,
       "cucsMorefImportRootFsmEntry": cucsMorefImportRootFsmEntry,
       "cucsMorefImportRootFsmInstanceId": cucsMorefImportRootFsmInstanceId,
       "cucsMorefImportRootFsmDn": cucsMorefImportRootFsmDn,
       "cucsMorefImportRootFsmRn": cucsMorefImportRootFsmRn,
       "cucsMorefImportRootFsmCompletionTime": cucsMorefImportRootFsmCompletionTime,
       "cucsMorefImportRootFsmCurrentFsm": cucsMorefImportRootFsmCurrentFsm,
       "cucsMorefImportRootFsmDescrData": cucsMorefImportRootFsmDescrData,
       "cucsMorefImportRootFsmFsmStatus": cucsMorefImportRootFsmFsmStatus,
       "cucsMorefImportRootFsmProgress": cucsMorefImportRootFsmProgress,
       "cucsMorefImportRootFsmRmtErrCode": cucsMorefImportRootFsmRmtErrCode,
       "cucsMorefImportRootFsmRmtErrDescr": cucsMorefImportRootFsmRmtErrDescr,
       "cucsMorefImportRootFsmRmtRslt": cucsMorefImportRootFsmRmtRslt,
       "cucsMorefImportRootFsmStageTable": cucsMorefImportRootFsmStageTable,
       "cucsMorefImportRootFsmStageEntry": cucsMorefImportRootFsmStageEntry,
       "cucsMorefImportRootFsmStageInstanceId": cucsMorefImportRootFsmStageInstanceId,
       "cucsMorefImportRootFsmStageDn": cucsMorefImportRootFsmStageDn,
       "cucsMorefImportRootFsmStageRn": cucsMorefImportRootFsmStageRn,
       "cucsMorefImportRootFsmStageDescrData": cucsMorefImportRootFsmStageDescrData,
       "cucsMorefImportRootFsmStageLastUpdateTime": cucsMorefImportRootFsmStageLastUpdateTime,
       "cucsMorefImportRootFsmStageName": cucsMorefImportRootFsmStageName,
       "cucsMorefImportRootFsmStageOrder": cucsMorefImportRootFsmStageOrder,
       "cucsMorefImportRootFsmStageRetry": cucsMorefImportRootFsmStageRetry,
       "cucsMorefImportRootFsmStageStageStatus": cucsMorefImportRootFsmStageStageStatus,
       "cucsMorefImportRootFsmTaskTable": cucsMorefImportRootFsmTaskTable,
       "cucsMorefImportRootFsmTaskEntry": cucsMorefImportRootFsmTaskEntry,
       "cucsMorefImportRootFsmTaskInstanceId": cucsMorefImportRootFsmTaskInstanceId,
       "cucsMorefImportRootFsmTaskDn": cucsMorefImportRootFsmTaskDn,
       "cucsMorefImportRootFsmTaskRn": cucsMorefImportRootFsmTaskRn,
       "cucsMorefImportRootFsmTaskCompletion": cucsMorefImportRootFsmTaskCompletion,
       "cucsMorefImportRootFsmTaskFlags": cucsMorefImportRootFsmTaskFlags,
       "cucsMorefImportRootFsmTaskItem": cucsMorefImportRootFsmTaskItem,
       "cucsMorefImportRootFsmTaskSeqId": cucsMorefImportRootFsmTaskSeqId,
       "cucsMorefPropTable": cucsMorefPropTable,
       "cucsMorefPropEntry": cucsMorefPropEntry,
       "cucsMorefPropInstanceId": cucsMorefPropInstanceId,
       "cucsMorefPropDn": cucsMorefPropDn,
       "cucsMorefPropRn": cucsMorefPropRn,
       "cucsMorefPropAdminState": cucsMorefPropAdminState,
       "cucsMorefPropName": cucsMorefPropName,
       "cucsMorefPropValue": cucsMorefPropValue,
       "cucsMorefRefTable": cucsMorefRefTable,
       "cucsMorefRefEntry": cucsMorefRefEntry,
       "cucsMorefRefInstanceId": cucsMorefRefInstanceId,
       "cucsMorefRefDn": cucsMorefRefDn,
       "cucsMorefRefRn": cucsMorefRefRn,
       "cucsMorefRefMoRn": cucsMorefRefMoRn}
)
