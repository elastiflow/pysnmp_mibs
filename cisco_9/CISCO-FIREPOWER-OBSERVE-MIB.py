# SNMP MIB module (CISCO-FIREPOWER-OBSERVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-OBSERVE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprMoMoClassId,
 CfprObserveObservedFsmCurrentFsm,
 CfprObserveObservedFsmStageName,
 CfprObserveObservedFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprMoMoClassId",
    "CfprObserveObservedFsmCurrentFsm",
    "CfprObserveObservedFsmStageName",
    "CfprObserveObservedFsmTaskItem")

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

cfprObserveObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprObserveFilterTable_Object = MibTable
cfprObserveFilterTable = _CfprObserveFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1)
)
if mibBuilder.loadTexts:
    cfprObserveFilterTable.setStatus("current")
_CfprObserveFilterEntry_Object = MibTableRow
cfprObserveFilterEntry = _CfprObserveFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1)
)
cfprObserveFilterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OBSERVE-MIB", "cfprObserveFilterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprObserveFilterEntry.setStatus("current")
_CfprObserveFilterInstanceId_Type = CfprManagedObjectId
_CfprObserveFilterInstanceId_Object = MibTableColumn
cfprObserveFilterInstanceId = _CfprObserveFilterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 1),
    _CfprObserveFilterInstanceId_Type()
)
cfprObserveFilterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprObserveFilterInstanceId.setStatus("current")
_CfprObserveFilterDn_Type = CfprManagedObjectDn
_CfprObserveFilterDn_Object = MibTableColumn
cfprObserveFilterDn = _CfprObserveFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 2),
    _CfprObserveFilterDn_Type()
)
cfprObserveFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterDn.setStatus("current")
_CfprObserveFilterRn_Type = SnmpAdminString
_CfprObserveFilterRn_Object = MibTableColumn
cfprObserveFilterRn = _CfprObserveFilterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 3),
    _CfprObserveFilterRn_Type()
)
cfprObserveFilterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterRn.setStatus("current")
_CfprObserveFilterAndOperation_Type = TruthValue
_CfprObserveFilterAndOperation_Object = MibTableColumn
cfprObserveFilterAndOperation = _CfprObserveFilterAndOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 4),
    _CfprObserveFilterAndOperation_Type()
)
cfprObserveFilterAndOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterAndOperation.setStatus("current")
_CfprObserveFilterChildClassId_Type = CfprMoMoClassId
_CfprObserveFilterChildClassId_Object = MibTableColumn
cfprObserveFilterChildClassId = _CfprObserveFilterChildClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 5),
    _CfprObserveFilterChildClassId_Type()
)
cfprObserveFilterChildClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterChildClassId.setStatus("current")
_CfprObserveFilterFilterClassId_Type = CfprMoMoClassId
_CfprObserveFilterFilterClassId_Object = MibTableColumn
cfprObserveFilterFilterClassId = _CfprObserveFilterFilterClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 6),
    _CfprObserveFilterFilterClassId_Type()
)
cfprObserveFilterFilterClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterClassId.setStatus("current")
_CfprObserveFilterFilterPropId1_Type = SnmpAdminString
_CfprObserveFilterFilterPropId1_Object = MibTableColumn
cfprObserveFilterFilterPropId1 = _CfprObserveFilterFilterPropId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 7),
    _CfprObserveFilterFilterPropId1_Type()
)
cfprObserveFilterFilterPropId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterPropId1.setStatus("current")
_CfprObserveFilterFilterPropId2_Type = SnmpAdminString
_CfprObserveFilterFilterPropId2_Object = MibTableColumn
cfprObserveFilterFilterPropId2 = _CfprObserveFilterFilterPropId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 8),
    _CfprObserveFilterFilterPropId2_Type()
)
cfprObserveFilterFilterPropId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterPropId2.setStatus("current")
_CfprObserveFilterFilterPropId3_Type = SnmpAdminString
_CfprObserveFilterFilterPropId3_Object = MibTableColumn
cfprObserveFilterFilterPropId3 = _CfprObserveFilterFilterPropId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 9),
    _CfprObserveFilterFilterPropId3_Type()
)
cfprObserveFilterFilterPropId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterPropId3.setStatus("current")
_CfprObserveFilterFilterPropValue1_Type = SnmpAdminString
_CfprObserveFilterFilterPropValue1_Object = MibTableColumn
cfprObserveFilterFilterPropValue1 = _CfprObserveFilterFilterPropValue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 10),
    _CfprObserveFilterFilterPropValue1_Type()
)
cfprObserveFilterFilterPropValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterPropValue1.setStatus("current")
_CfprObserveFilterFilterPropValue2_Type = SnmpAdminString
_CfprObserveFilterFilterPropValue2_Object = MibTableColumn
cfprObserveFilterFilterPropValue2 = _CfprObserveFilterFilterPropValue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 11),
    _CfprObserveFilterFilterPropValue2_Type()
)
cfprObserveFilterFilterPropValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterPropValue2.setStatus("current")
_CfprObserveFilterFilterPropValue3_Type = SnmpAdminString
_CfprObserveFilterFilterPropValue3_Object = MibTableColumn
cfprObserveFilterFilterPropValue3 = _CfprObserveFilterFilterPropValue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 12),
    _CfprObserveFilterFilterPropValue3_Type()
)
cfprObserveFilterFilterPropValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterFilterPropValue3.setStatus("current")
_CfprObserveFilterHierarchical_Type = TruthValue
_CfprObserveFilterHierarchical_Object = MibTableColumn
cfprObserveFilterHierarchical = _CfprObserveFilterHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 13),
    _CfprObserveFilterHierarchical_Type()
)
cfprObserveFilterHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterHierarchical.setStatus("current")
_CfprObserveFilterReplicateIfNoChild_Type = TruthValue
_CfprObserveFilterReplicateIfNoChild_Object = MibTableColumn
cfprObserveFilterReplicateIfNoChild = _CfprObserveFilterReplicateIfNoChild_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 1, 1, 14),
    _CfprObserveFilterReplicateIfNoChild_Type()
)
cfprObserveFilterReplicateIfNoChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveFilterReplicateIfNoChild.setStatus("current")
_CfprObserveObservedTable_Object = MibTable
cfprObserveObservedTable = _CfprObserveObservedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2)
)
if mibBuilder.loadTexts:
    cfprObserveObservedTable.setStatus("current")
_CfprObserveObservedEntry_Object = MibTableRow
cfprObserveObservedEntry = _CfprObserveObservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1)
)
cfprObserveObservedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OBSERVE-MIB", "cfprObserveObservedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprObserveObservedEntry.setStatus("current")
_CfprObserveObservedInstanceId_Type = CfprManagedObjectId
_CfprObserveObservedInstanceId_Object = MibTableColumn
cfprObserveObservedInstanceId = _CfprObserveObservedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 1),
    _CfprObserveObservedInstanceId_Type()
)
cfprObserveObservedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprObserveObservedInstanceId.setStatus("current")
_CfprObserveObservedDn_Type = CfprManagedObjectDn
_CfprObserveObservedDn_Object = MibTableColumn
cfprObserveObservedDn = _CfprObserveObservedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 2),
    _CfprObserveObservedDn_Type()
)
cfprObserveObservedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedDn.setStatus("current")
_CfprObserveObservedRn_Type = SnmpAdminString
_CfprObserveObservedRn_Object = MibTableColumn
cfprObserveObservedRn = _CfprObserveObservedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 3),
    _CfprObserveObservedRn_Type()
)
cfprObserveObservedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedRn.setStatus("current")
_CfprObserveObservedDataSrcAppType_Type = SnmpAdminString
_CfprObserveObservedDataSrcAppType_Object = MibTableColumn
cfprObserveObservedDataSrcAppType = _CfprObserveObservedDataSrcAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 4),
    _CfprObserveObservedDataSrcAppType_Type()
)
cfprObserveObservedDataSrcAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedDataSrcAppType.setStatus("current")
_CfprObserveObservedDataSrcSysId_Type = Gauge32
_CfprObserveObservedDataSrcSysId_Object = MibTableColumn
cfprObserveObservedDataSrcSysId = _CfprObserveObservedDataSrcSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 5),
    _CfprObserveObservedDataSrcSysId_Type()
)
cfprObserveObservedDataSrcSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedDataSrcSysId.setStatus("current")
_CfprObserveObservedFsmDescr_Type = SnmpAdminString
_CfprObserveObservedFsmDescr_Object = MibTableColumn
cfprObserveObservedFsmDescr = _CfprObserveObservedFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 6),
    _CfprObserveObservedFsmDescr_Type()
)
cfprObserveObservedFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmDescr.setStatus("current")
_CfprObserveObservedFsmPrev_Type = SnmpAdminString
_CfprObserveObservedFsmPrev_Object = MibTableColumn
cfprObserveObservedFsmPrev = _CfprObserveObservedFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 7),
    _CfprObserveObservedFsmPrev_Type()
)
cfprObserveObservedFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmPrev.setStatus("current")
_CfprObserveObservedFsmProgr_Type = Gauge32
_CfprObserveObservedFsmProgr_Object = MibTableColumn
cfprObserveObservedFsmProgr = _CfprObserveObservedFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 8),
    _CfprObserveObservedFsmProgr_Type()
)
cfprObserveObservedFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmProgr.setStatus("current")
_CfprObserveObservedFsmRmtInvErrCode_Type = Gauge32
_CfprObserveObservedFsmRmtInvErrCode_Object = MibTableColumn
cfprObserveObservedFsmRmtInvErrCode = _CfprObserveObservedFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 9),
    _CfprObserveObservedFsmRmtInvErrCode_Type()
)
cfprObserveObservedFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRmtInvErrCode.setStatus("current")
_CfprObserveObservedFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprObserveObservedFsmRmtInvErrDescr_Object = MibTableColumn
cfprObserveObservedFsmRmtInvErrDescr = _CfprObserveObservedFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 10),
    _CfprObserveObservedFsmRmtInvErrDescr_Type()
)
cfprObserveObservedFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRmtInvErrDescr.setStatus("current")
_CfprObserveObservedFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprObserveObservedFsmRmtInvRslt_Object = MibTableColumn
cfprObserveObservedFsmRmtInvRslt = _CfprObserveObservedFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 11),
    _CfprObserveObservedFsmRmtInvRslt_Type()
)
cfprObserveObservedFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRmtInvRslt.setStatus("current")
_CfprObserveObservedFsmStageDescr_Type = SnmpAdminString
_CfprObserveObservedFsmStageDescr_Object = MibTableColumn
cfprObserveObservedFsmStageDescr = _CfprObserveObservedFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 12),
    _CfprObserveObservedFsmStageDescr_Type()
)
cfprObserveObservedFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageDescr.setStatus("current")
_CfprObserveObservedFsmStamp_Type = DateAndTime
_CfprObserveObservedFsmStamp_Object = MibTableColumn
cfprObserveObservedFsmStamp = _CfprObserveObservedFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 13),
    _CfprObserveObservedFsmStamp_Type()
)
cfprObserveObservedFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStamp.setStatus("current")
_CfprObserveObservedFsmStatus_Type = SnmpAdminString
_CfprObserveObservedFsmStatus_Object = MibTableColumn
cfprObserveObservedFsmStatus = _CfprObserveObservedFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 14),
    _CfprObserveObservedFsmStatus_Type()
)
cfprObserveObservedFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStatus.setStatus("current")
_CfprObserveObservedFsmTry_Type = Gauge32
_CfprObserveObservedFsmTry_Object = MibTableColumn
cfprObserveObservedFsmTry = _CfprObserveObservedFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 15),
    _CfprObserveObservedFsmTry_Type()
)
cfprObserveObservedFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTry.setStatus("current")
_CfprObserveObservedGenNum_Type = Gauge32
_CfprObserveObservedGenNum_Object = MibTableColumn
cfprObserveObservedGenNum = _CfprObserveObservedGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 16),
    _CfprObserveObservedGenNum_Type()
)
cfprObserveObservedGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedGenNum.setStatus("current")
_CfprObserveObservedHierarchical_Type = TruthValue
_CfprObserveObservedHierarchical_Object = MibTableColumn
cfprObserveObservedHierarchical = _CfprObserveObservedHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 17),
    _CfprObserveObservedHierarchical_Type()
)
cfprObserveObservedHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedHierarchical.setStatus("current")
_CfprObserveObservedId_Type = Gauge32
_CfprObserveObservedId_Object = MibTableColumn
cfprObserveObservedId = _CfprObserveObservedId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 18),
    _CfprObserveObservedId_Type()
)
cfprObserveObservedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedId.setStatus("current")
_CfprObserveObservedIsDeleted_Type = TruthValue
_CfprObserveObservedIsDeleted_Object = MibTableColumn
cfprObserveObservedIsDeleted = _CfprObserveObservedIsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 19),
    _CfprObserveObservedIsDeleted_Type()
)
cfprObserveObservedIsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedIsDeleted.setStatus("current")
_CfprObserveObservedObservedDn_Type = SnmpAdminString
_CfprObserveObservedObservedDn_Object = MibTableColumn
cfprObserveObservedObservedDn = _CfprObserveObservedObservedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 2, 1, 20),
    _CfprObserveObservedObservedDn_Type()
)
cfprObserveObservedObservedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedObservedDn.setStatus("current")
_CfprObserveObservedContTable_Object = MibTable
cfprObserveObservedContTable = _CfprObserveObservedContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 3)
)
if mibBuilder.loadTexts:
    cfprObserveObservedContTable.setStatus("current")
_CfprObserveObservedContEntry_Object = MibTableRow
cfprObserveObservedContEntry = _CfprObserveObservedContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 3, 1)
)
cfprObserveObservedContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OBSERVE-MIB", "cfprObserveObservedContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprObserveObservedContEntry.setStatus("current")
_CfprObserveObservedContInstanceId_Type = CfprManagedObjectId
_CfprObserveObservedContInstanceId_Object = MibTableColumn
cfprObserveObservedContInstanceId = _CfprObserveObservedContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 3, 1, 1),
    _CfprObserveObservedContInstanceId_Type()
)
cfprObserveObservedContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprObserveObservedContInstanceId.setStatus("current")
_CfprObserveObservedContDn_Type = CfprManagedObjectDn
_CfprObserveObservedContDn_Object = MibTableColumn
cfprObserveObservedContDn = _CfprObserveObservedContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 3, 1, 2),
    _CfprObserveObservedContDn_Type()
)
cfprObserveObservedContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedContDn.setStatus("current")
_CfprObserveObservedContRn_Type = SnmpAdminString
_CfprObserveObservedContRn_Object = MibTableColumn
cfprObserveObservedContRn = _CfprObserveObservedContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 3, 1, 3),
    _CfprObserveObservedContRn_Type()
)
cfprObserveObservedContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedContRn.setStatus("current")
_CfprObserveObservedContIdCount_Type = Gauge32
_CfprObserveObservedContIdCount_Object = MibTableColumn
cfprObserveObservedContIdCount = _CfprObserveObservedContIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 3, 1, 4),
    _CfprObserveObservedContIdCount_Type()
)
cfprObserveObservedContIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedContIdCount.setStatus("current")
_CfprObserveObservedFsmTable_Object = MibTable
cfprObserveObservedFsmTable = _CfprObserveObservedFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4)
)
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTable.setStatus("current")
_CfprObserveObservedFsmEntry_Object = MibTableRow
cfprObserveObservedFsmEntry = _CfprObserveObservedFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1)
)
cfprObserveObservedFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OBSERVE-MIB", "cfprObserveObservedFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprObserveObservedFsmEntry.setStatus("current")
_CfprObserveObservedFsmInstanceId_Type = CfprManagedObjectId
_CfprObserveObservedFsmInstanceId_Object = MibTableColumn
cfprObserveObservedFsmInstanceId = _CfprObserveObservedFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 1),
    _CfprObserveObservedFsmInstanceId_Type()
)
cfprObserveObservedFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmInstanceId.setStatus("current")
_CfprObserveObservedFsmDn_Type = CfprManagedObjectDn
_CfprObserveObservedFsmDn_Object = MibTableColumn
cfprObserveObservedFsmDn = _CfprObserveObservedFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 2),
    _CfprObserveObservedFsmDn_Type()
)
cfprObserveObservedFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmDn.setStatus("current")
_CfprObserveObservedFsmRn_Type = SnmpAdminString
_CfprObserveObservedFsmRn_Object = MibTableColumn
cfprObserveObservedFsmRn = _CfprObserveObservedFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 3),
    _CfprObserveObservedFsmRn_Type()
)
cfprObserveObservedFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRn.setStatus("current")
_CfprObserveObservedFsmCompletionTime_Type = DateAndTime
_CfprObserveObservedFsmCompletionTime_Object = MibTableColumn
cfprObserveObservedFsmCompletionTime = _CfprObserveObservedFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 4),
    _CfprObserveObservedFsmCompletionTime_Type()
)
cfprObserveObservedFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmCompletionTime.setStatus("current")
_CfprObserveObservedFsmCurrentFsm_Type = CfprObserveObservedFsmCurrentFsm
_CfprObserveObservedFsmCurrentFsm_Object = MibTableColumn
cfprObserveObservedFsmCurrentFsm = _CfprObserveObservedFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 5),
    _CfprObserveObservedFsmCurrentFsm_Type()
)
cfprObserveObservedFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmCurrentFsm.setStatus("current")
_CfprObserveObservedFsmDescrData_Type = SnmpAdminString
_CfprObserveObservedFsmDescrData_Object = MibTableColumn
cfprObserveObservedFsmDescrData = _CfprObserveObservedFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 6),
    _CfprObserveObservedFsmDescrData_Type()
)
cfprObserveObservedFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmDescrData.setStatus("current")
_CfprObserveObservedFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprObserveObservedFsmFsmStatus_Object = MibTableColumn
cfprObserveObservedFsmFsmStatus = _CfprObserveObservedFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 7),
    _CfprObserveObservedFsmFsmStatus_Type()
)
cfprObserveObservedFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmFsmStatus.setStatus("current")
_CfprObserveObservedFsmProgress_Type = Gauge32
_CfprObserveObservedFsmProgress_Object = MibTableColumn
cfprObserveObservedFsmProgress = _CfprObserveObservedFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 8),
    _CfprObserveObservedFsmProgress_Type()
)
cfprObserveObservedFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmProgress.setStatus("current")
_CfprObserveObservedFsmRmtErrCode_Type = Gauge32
_CfprObserveObservedFsmRmtErrCode_Object = MibTableColumn
cfprObserveObservedFsmRmtErrCode = _CfprObserveObservedFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 9),
    _CfprObserveObservedFsmRmtErrCode_Type()
)
cfprObserveObservedFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRmtErrCode.setStatus("current")
_CfprObserveObservedFsmRmtErrDescr_Type = SnmpAdminString
_CfprObserveObservedFsmRmtErrDescr_Object = MibTableColumn
cfprObserveObservedFsmRmtErrDescr = _CfprObserveObservedFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 10),
    _CfprObserveObservedFsmRmtErrDescr_Type()
)
cfprObserveObservedFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRmtErrDescr.setStatus("current")
_CfprObserveObservedFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprObserveObservedFsmRmtRslt_Object = MibTableColumn
cfprObserveObservedFsmRmtRslt = _CfprObserveObservedFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 4, 1, 11),
    _CfprObserveObservedFsmRmtRslt_Type()
)
cfprObserveObservedFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmRmtRslt.setStatus("current")
_CfprObserveObservedFsmStageTable_Object = MibTable
cfprObserveObservedFsmStageTable = _CfprObserveObservedFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5)
)
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageTable.setStatus("current")
_CfprObserveObservedFsmStageEntry_Object = MibTableRow
cfprObserveObservedFsmStageEntry = _CfprObserveObservedFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1)
)
cfprObserveObservedFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OBSERVE-MIB", "cfprObserveObservedFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageEntry.setStatus("current")
_CfprObserveObservedFsmStageInstanceId_Type = CfprManagedObjectId
_CfprObserveObservedFsmStageInstanceId_Object = MibTableColumn
cfprObserveObservedFsmStageInstanceId = _CfprObserveObservedFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 1),
    _CfprObserveObservedFsmStageInstanceId_Type()
)
cfprObserveObservedFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageInstanceId.setStatus("current")
_CfprObserveObservedFsmStageDn_Type = CfprManagedObjectDn
_CfprObserveObservedFsmStageDn_Object = MibTableColumn
cfprObserveObservedFsmStageDn = _CfprObserveObservedFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 2),
    _CfprObserveObservedFsmStageDn_Type()
)
cfprObserveObservedFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageDn.setStatus("current")
_CfprObserveObservedFsmStageRn_Type = SnmpAdminString
_CfprObserveObservedFsmStageRn_Object = MibTableColumn
cfprObserveObservedFsmStageRn = _CfprObserveObservedFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 3),
    _CfprObserveObservedFsmStageRn_Type()
)
cfprObserveObservedFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageRn.setStatus("current")
_CfprObserveObservedFsmStageDescrData_Type = SnmpAdminString
_CfprObserveObservedFsmStageDescrData_Object = MibTableColumn
cfprObserveObservedFsmStageDescrData = _CfprObserveObservedFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 4),
    _CfprObserveObservedFsmStageDescrData_Type()
)
cfprObserveObservedFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageDescrData.setStatus("current")
_CfprObserveObservedFsmStageLastUpdateTime_Type = DateAndTime
_CfprObserveObservedFsmStageLastUpdateTime_Object = MibTableColumn
cfprObserveObservedFsmStageLastUpdateTime = _CfprObserveObservedFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 5),
    _CfprObserveObservedFsmStageLastUpdateTime_Type()
)
cfprObserveObservedFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageLastUpdateTime.setStatus("current")
_CfprObserveObservedFsmStageName_Type = CfprObserveObservedFsmStageName
_CfprObserveObservedFsmStageName_Object = MibTableColumn
cfprObserveObservedFsmStageName = _CfprObserveObservedFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 6),
    _CfprObserveObservedFsmStageName_Type()
)
cfprObserveObservedFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageName.setStatus("current")
_CfprObserveObservedFsmStageOrder_Type = Gauge32
_CfprObserveObservedFsmStageOrder_Object = MibTableColumn
cfprObserveObservedFsmStageOrder = _CfprObserveObservedFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 7),
    _CfprObserveObservedFsmStageOrder_Type()
)
cfprObserveObservedFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageOrder.setStatus("current")
_CfprObserveObservedFsmStageRetry_Type = Gauge32
_CfprObserveObservedFsmStageRetry_Object = MibTableColumn
cfprObserveObservedFsmStageRetry = _CfprObserveObservedFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 8),
    _CfprObserveObservedFsmStageRetry_Type()
)
cfprObserveObservedFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageRetry.setStatus("current")
_CfprObserveObservedFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprObserveObservedFsmStageStageStatus_Object = MibTableColumn
cfprObserveObservedFsmStageStageStatus = _CfprObserveObservedFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 5, 1, 9),
    _CfprObserveObservedFsmStageStageStatus_Type()
)
cfprObserveObservedFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmStageStageStatus.setStatus("current")
_CfprObserveObservedFsmTaskTable_Object = MibTable
cfprObserveObservedFsmTaskTable = _CfprObserveObservedFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6)
)
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskTable.setStatus("current")
_CfprObserveObservedFsmTaskEntry_Object = MibTableRow
cfprObserveObservedFsmTaskEntry = _CfprObserveObservedFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1)
)
cfprObserveObservedFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OBSERVE-MIB", "cfprObserveObservedFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskEntry.setStatus("current")
_CfprObserveObservedFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprObserveObservedFsmTaskInstanceId_Object = MibTableColumn
cfprObserveObservedFsmTaskInstanceId = _CfprObserveObservedFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 1),
    _CfprObserveObservedFsmTaskInstanceId_Type()
)
cfprObserveObservedFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskInstanceId.setStatus("current")
_CfprObserveObservedFsmTaskDn_Type = CfprManagedObjectDn
_CfprObserveObservedFsmTaskDn_Object = MibTableColumn
cfprObserveObservedFsmTaskDn = _CfprObserveObservedFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 2),
    _CfprObserveObservedFsmTaskDn_Type()
)
cfprObserveObservedFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskDn.setStatus("current")
_CfprObserveObservedFsmTaskRn_Type = SnmpAdminString
_CfprObserveObservedFsmTaskRn_Object = MibTableColumn
cfprObserveObservedFsmTaskRn = _CfprObserveObservedFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 3),
    _CfprObserveObservedFsmTaskRn_Type()
)
cfprObserveObservedFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskRn.setStatus("current")
_CfprObserveObservedFsmTaskCompletion_Type = CfprFsmCompletion
_CfprObserveObservedFsmTaskCompletion_Object = MibTableColumn
cfprObserveObservedFsmTaskCompletion = _CfprObserveObservedFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 4),
    _CfprObserveObservedFsmTaskCompletion_Type()
)
cfprObserveObservedFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskCompletion.setStatus("current")
_CfprObserveObservedFsmTaskFlags_Type = CfprFsmFlags
_CfprObserveObservedFsmTaskFlags_Object = MibTableColumn
cfprObserveObservedFsmTaskFlags = _CfprObserveObservedFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 5),
    _CfprObserveObservedFsmTaskFlags_Type()
)
cfprObserveObservedFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskFlags.setStatus("current")
_CfprObserveObservedFsmTaskItem_Type = CfprObserveObservedFsmTaskItem
_CfprObserveObservedFsmTaskItem_Object = MibTableColumn
cfprObserveObservedFsmTaskItem = _CfprObserveObservedFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 6),
    _CfprObserveObservedFsmTaskItem_Type()
)
cfprObserveObservedFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskItem.setStatus("current")
_CfprObserveObservedFsmTaskSeqId_Type = Gauge32
_CfprObserveObservedFsmTaskSeqId_Object = MibTableColumn
cfprObserveObservedFsmTaskSeqId = _CfprObserveObservedFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 57, 6, 1, 7),
    _CfprObserveObservedFsmTaskSeqId_Type()
)
cfprObserveObservedFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprObserveObservedFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-OBSERVE-MIB",
    **{"cfprObserveObjects": cfprObserveObjects,
       "cfprObserveFilterTable": cfprObserveFilterTable,
       "cfprObserveFilterEntry": cfprObserveFilterEntry,
       "cfprObserveFilterInstanceId": cfprObserveFilterInstanceId,
       "cfprObserveFilterDn": cfprObserveFilterDn,
       "cfprObserveFilterRn": cfprObserveFilterRn,
       "cfprObserveFilterAndOperation": cfprObserveFilterAndOperation,
       "cfprObserveFilterChildClassId": cfprObserveFilterChildClassId,
       "cfprObserveFilterFilterClassId": cfprObserveFilterFilterClassId,
       "cfprObserveFilterFilterPropId1": cfprObserveFilterFilterPropId1,
       "cfprObserveFilterFilterPropId2": cfprObserveFilterFilterPropId2,
       "cfprObserveFilterFilterPropId3": cfprObserveFilterFilterPropId3,
       "cfprObserveFilterFilterPropValue1": cfprObserveFilterFilterPropValue1,
       "cfprObserveFilterFilterPropValue2": cfprObserveFilterFilterPropValue2,
       "cfprObserveFilterFilterPropValue3": cfprObserveFilterFilterPropValue3,
       "cfprObserveFilterHierarchical": cfprObserveFilterHierarchical,
       "cfprObserveFilterReplicateIfNoChild": cfprObserveFilterReplicateIfNoChild,
       "cfprObserveObservedTable": cfprObserveObservedTable,
       "cfprObserveObservedEntry": cfprObserveObservedEntry,
       "cfprObserveObservedInstanceId": cfprObserveObservedInstanceId,
       "cfprObserveObservedDn": cfprObserveObservedDn,
       "cfprObserveObservedRn": cfprObserveObservedRn,
       "cfprObserveObservedDataSrcAppType": cfprObserveObservedDataSrcAppType,
       "cfprObserveObservedDataSrcSysId": cfprObserveObservedDataSrcSysId,
       "cfprObserveObservedFsmDescr": cfprObserveObservedFsmDescr,
       "cfprObserveObservedFsmPrev": cfprObserveObservedFsmPrev,
       "cfprObserveObservedFsmProgr": cfprObserveObservedFsmProgr,
       "cfprObserveObservedFsmRmtInvErrCode": cfprObserveObservedFsmRmtInvErrCode,
       "cfprObserveObservedFsmRmtInvErrDescr": cfprObserveObservedFsmRmtInvErrDescr,
       "cfprObserveObservedFsmRmtInvRslt": cfprObserveObservedFsmRmtInvRslt,
       "cfprObserveObservedFsmStageDescr": cfprObserveObservedFsmStageDescr,
       "cfprObserveObservedFsmStamp": cfprObserveObservedFsmStamp,
       "cfprObserveObservedFsmStatus": cfprObserveObservedFsmStatus,
       "cfprObserveObservedFsmTry": cfprObserveObservedFsmTry,
       "cfprObserveObservedGenNum": cfprObserveObservedGenNum,
       "cfprObserveObservedHierarchical": cfprObserveObservedHierarchical,
       "cfprObserveObservedId": cfprObserveObservedId,
       "cfprObserveObservedIsDeleted": cfprObserveObservedIsDeleted,
       "cfprObserveObservedObservedDn": cfprObserveObservedObservedDn,
       "cfprObserveObservedContTable": cfprObserveObservedContTable,
       "cfprObserveObservedContEntry": cfprObserveObservedContEntry,
       "cfprObserveObservedContInstanceId": cfprObserveObservedContInstanceId,
       "cfprObserveObservedContDn": cfprObserveObservedContDn,
       "cfprObserveObservedContRn": cfprObserveObservedContRn,
       "cfprObserveObservedContIdCount": cfprObserveObservedContIdCount,
       "cfprObserveObservedFsmTable": cfprObserveObservedFsmTable,
       "cfprObserveObservedFsmEntry": cfprObserveObservedFsmEntry,
       "cfprObserveObservedFsmInstanceId": cfprObserveObservedFsmInstanceId,
       "cfprObserveObservedFsmDn": cfprObserveObservedFsmDn,
       "cfprObserveObservedFsmRn": cfprObserveObservedFsmRn,
       "cfprObserveObservedFsmCompletionTime": cfprObserveObservedFsmCompletionTime,
       "cfprObserveObservedFsmCurrentFsm": cfprObserveObservedFsmCurrentFsm,
       "cfprObserveObservedFsmDescrData": cfprObserveObservedFsmDescrData,
       "cfprObserveObservedFsmFsmStatus": cfprObserveObservedFsmFsmStatus,
       "cfprObserveObservedFsmProgress": cfprObserveObservedFsmProgress,
       "cfprObserveObservedFsmRmtErrCode": cfprObserveObservedFsmRmtErrCode,
       "cfprObserveObservedFsmRmtErrDescr": cfprObserveObservedFsmRmtErrDescr,
       "cfprObserveObservedFsmRmtRslt": cfprObserveObservedFsmRmtRslt,
       "cfprObserveObservedFsmStageTable": cfprObserveObservedFsmStageTable,
       "cfprObserveObservedFsmStageEntry": cfprObserveObservedFsmStageEntry,
       "cfprObserveObservedFsmStageInstanceId": cfprObserveObservedFsmStageInstanceId,
       "cfprObserveObservedFsmStageDn": cfprObserveObservedFsmStageDn,
       "cfprObserveObservedFsmStageRn": cfprObserveObservedFsmStageRn,
       "cfprObserveObservedFsmStageDescrData": cfprObserveObservedFsmStageDescrData,
       "cfprObserveObservedFsmStageLastUpdateTime": cfprObserveObservedFsmStageLastUpdateTime,
       "cfprObserveObservedFsmStageName": cfprObserveObservedFsmStageName,
       "cfprObserveObservedFsmStageOrder": cfprObserveObservedFsmStageOrder,
       "cfprObserveObservedFsmStageRetry": cfprObserveObservedFsmStageRetry,
       "cfprObserveObservedFsmStageStageStatus": cfprObserveObservedFsmStageStageStatus,
       "cfprObserveObservedFsmTaskTable": cfprObserveObservedFsmTaskTable,
       "cfprObserveObservedFsmTaskEntry": cfprObserveObservedFsmTaskEntry,
       "cfprObserveObservedFsmTaskInstanceId": cfprObserveObservedFsmTaskInstanceId,
       "cfprObserveObservedFsmTaskDn": cfprObserveObservedFsmTaskDn,
       "cfprObserveObservedFsmTaskRn": cfprObserveObservedFsmTaskRn,
       "cfprObserveObservedFsmTaskCompletion": cfprObserveObservedFsmTaskCompletion,
       "cfprObserveObservedFsmTaskFlags": cfprObserveObservedFsmTaskFlags,
       "cfprObserveObservedFsmTaskItem": cfprObserveObservedFsmTaskItem,
       "cfprObserveObservedFsmTaskSeqId": cfprObserveObservedFsmTaskSeqId}
)
