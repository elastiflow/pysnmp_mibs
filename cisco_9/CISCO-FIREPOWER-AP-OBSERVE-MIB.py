# SNMP MIB module (CISCO-FIREPOWER-AP-OBSERVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-OBSERVE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:14 2025
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
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApMoMoClassId,
 CfprApObserveObservedFsmCurrentFsm,
 CfprApObserveObservedFsmStageName,
 CfprApObserveObservedFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApMoMoClassId",
    "CfprApObserveObservedFsmCurrentFsm",
    "CfprApObserveObservedFsmStageName",
    "CfprApObserveObservedFsmTaskItem")

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

cfprApObserveObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApObserveFilterTable_Object = MibTable
cfprApObserveFilterTable = _CfprApObserveFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1)
)
if mibBuilder.loadTexts:
    cfprApObserveFilterTable.setStatus("current")
_CfprApObserveFilterEntry_Object = MibTableRow
cfprApObserveFilterEntry = _CfprApObserveFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1)
)
cfprApObserveFilterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OBSERVE-MIB", "cfprApObserveFilterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApObserveFilterEntry.setStatus("current")
_CfprApObserveFilterInstanceId_Type = CfprApManagedObjectId
_CfprApObserveFilterInstanceId_Object = MibTableColumn
cfprApObserveFilterInstanceId = _CfprApObserveFilterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 1),
    _CfprApObserveFilterInstanceId_Type()
)
cfprApObserveFilterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApObserveFilterInstanceId.setStatus("current")
_CfprApObserveFilterDn_Type = CfprApManagedObjectDn
_CfprApObserveFilterDn_Object = MibTableColumn
cfprApObserveFilterDn = _CfprApObserveFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 2),
    _CfprApObserveFilterDn_Type()
)
cfprApObserveFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterDn.setStatus("current")
_CfprApObserveFilterRn_Type = SnmpAdminString
_CfprApObserveFilterRn_Object = MibTableColumn
cfprApObserveFilterRn = _CfprApObserveFilterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 3),
    _CfprApObserveFilterRn_Type()
)
cfprApObserveFilterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterRn.setStatus("current")
_CfprApObserveFilterAndOperation_Type = TruthValue
_CfprApObserveFilterAndOperation_Object = MibTableColumn
cfprApObserveFilterAndOperation = _CfprApObserveFilterAndOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 4),
    _CfprApObserveFilterAndOperation_Type()
)
cfprApObserveFilterAndOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterAndOperation.setStatus("current")
_CfprApObserveFilterChildClassId_Type = CfprApMoMoClassId
_CfprApObserveFilterChildClassId_Object = MibTableColumn
cfprApObserveFilterChildClassId = _CfprApObserveFilterChildClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 5),
    _CfprApObserveFilterChildClassId_Type()
)
cfprApObserveFilterChildClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterChildClassId.setStatus("current")
_CfprApObserveFilterFilterClassId_Type = CfprApMoMoClassId
_CfprApObserveFilterFilterClassId_Object = MibTableColumn
cfprApObserveFilterFilterClassId = _CfprApObserveFilterFilterClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 6),
    _CfprApObserveFilterFilterClassId_Type()
)
cfprApObserveFilterFilterClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterClassId.setStatus("current")
_CfprApObserveFilterFilterPropId1_Type = SnmpAdminString
_CfprApObserveFilterFilterPropId1_Object = MibTableColumn
cfprApObserveFilterFilterPropId1 = _CfprApObserveFilterFilterPropId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 7),
    _CfprApObserveFilterFilterPropId1_Type()
)
cfprApObserveFilterFilterPropId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterPropId1.setStatus("current")
_CfprApObserveFilterFilterPropId2_Type = SnmpAdminString
_CfprApObserveFilterFilterPropId2_Object = MibTableColumn
cfprApObserveFilterFilterPropId2 = _CfprApObserveFilterFilterPropId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 8),
    _CfprApObserveFilterFilterPropId2_Type()
)
cfprApObserveFilterFilterPropId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterPropId2.setStatus("current")
_CfprApObserveFilterFilterPropId3_Type = SnmpAdminString
_CfprApObserveFilterFilterPropId3_Object = MibTableColumn
cfprApObserveFilterFilterPropId3 = _CfprApObserveFilterFilterPropId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 9),
    _CfprApObserveFilterFilterPropId3_Type()
)
cfprApObserveFilterFilterPropId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterPropId3.setStatus("current")
_CfprApObserveFilterFilterPropValue1_Type = SnmpAdminString
_CfprApObserveFilterFilterPropValue1_Object = MibTableColumn
cfprApObserveFilterFilterPropValue1 = _CfprApObserveFilterFilterPropValue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 10),
    _CfprApObserveFilterFilterPropValue1_Type()
)
cfprApObserveFilterFilterPropValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterPropValue1.setStatus("current")
_CfprApObserveFilterFilterPropValue2_Type = SnmpAdminString
_CfprApObserveFilterFilterPropValue2_Object = MibTableColumn
cfprApObserveFilterFilterPropValue2 = _CfprApObserveFilterFilterPropValue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 11),
    _CfprApObserveFilterFilterPropValue2_Type()
)
cfprApObserveFilterFilterPropValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterPropValue2.setStatus("current")
_CfprApObserveFilterFilterPropValue3_Type = SnmpAdminString
_CfprApObserveFilterFilterPropValue3_Object = MibTableColumn
cfprApObserveFilterFilterPropValue3 = _CfprApObserveFilterFilterPropValue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 12),
    _CfprApObserveFilterFilterPropValue3_Type()
)
cfprApObserveFilterFilterPropValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterFilterPropValue3.setStatus("current")
_CfprApObserveFilterHierarchical_Type = TruthValue
_CfprApObserveFilterHierarchical_Object = MibTableColumn
cfprApObserveFilterHierarchical = _CfprApObserveFilterHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 13),
    _CfprApObserveFilterHierarchical_Type()
)
cfprApObserveFilterHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterHierarchical.setStatus("current")
_CfprApObserveFilterReplicateIfNoChild_Type = TruthValue
_CfprApObserveFilterReplicateIfNoChild_Object = MibTableColumn
cfprApObserveFilterReplicateIfNoChild = _CfprApObserveFilterReplicateIfNoChild_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 1, 1, 14),
    _CfprApObserveFilterReplicateIfNoChild_Type()
)
cfprApObserveFilterReplicateIfNoChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveFilterReplicateIfNoChild.setStatus("current")
_CfprApObserveObservedTable_Object = MibTable
cfprApObserveObservedTable = _CfprApObserveObservedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2)
)
if mibBuilder.loadTexts:
    cfprApObserveObservedTable.setStatus("current")
_CfprApObserveObservedEntry_Object = MibTableRow
cfprApObserveObservedEntry = _CfprApObserveObservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1)
)
cfprApObserveObservedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OBSERVE-MIB", "cfprApObserveObservedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApObserveObservedEntry.setStatus("current")
_CfprApObserveObservedInstanceId_Type = CfprApManagedObjectId
_CfprApObserveObservedInstanceId_Object = MibTableColumn
cfprApObserveObservedInstanceId = _CfprApObserveObservedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 1),
    _CfprApObserveObservedInstanceId_Type()
)
cfprApObserveObservedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApObserveObservedInstanceId.setStatus("current")
_CfprApObserveObservedDn_Type = CfprApManagedObjectDn
_CfprApObserveObservedDn_Object = MibTableColumn
cfprApObserveObservedDn = _CfprApObserveObservedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 2),
    _CfprApObserveObservedDn_Type()
)
cfprApObserveObservedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedDn.setStatus("current")
_CfprApObserveObservedRn_Type = SnmpAdminString
_CfprApObserveObservedRn_Object = MibTableColumn
cfprApObserveObservedRn = _CfprApObserveObservedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 3),
    _CfprApObserveObservedRn_Type()
)
cfprApObserveObservedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedRn.setStatus("current")
_CfprApObserveObservedDataSrcAppType_Type = SnmpAdminString
_CfprApObserveObservedDataSrcAppType_Object = MibTableColumn
cfprApObserveObservedDataSrcAppType = _CfprApObserveObservedDataSrcAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 4),
    _CfprApObserveObservedDataSrcAppType_Type()
)
cfprApObserveObservedDataSrcAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedDataSrcAppType.setStatus("current")
_CfprApObserveObservedDataSrcSysId_Type = Gauge32
_CfprApObserveObservedDataSrcSysId_Object = MibTableColumn
cfprApObserveObservedDataSrcSysId = _CfprApObserveObservedDataSrcSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 5),
    _CfprApObserveObservedDataSrcSysId_Type()
)
cfprApObserveObservedDataSrcSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedDataSrcSysId.setStatus("current")
_CfprApObserveObservedFsmDescr_Type = SnmpAdminString
_CfprApObserveObservedFsmDescr_Object = MibTableColumn
cfprApObserveObservedFsmDescr = _CfprApObserveObservedFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 6),
    _CfprApObserveObservedFsmDescr_Type()
)
cfprApObserveObservedFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmDescr.setStatus("current")
_CfprApObserveObservedFsmPrev_Type = SnmpAdminString
_CfprApObserveObservedFsmPrev_Object = MibTableColumn
cfprApObserveObservedFsmPrev = _CfprApObserveObservedFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 7),
    _CfprApObserveObservedFsmPrev_Type()
)
cfprApObserveObservedFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmPrev.setStatus("current")
_CfprApObserveObservedFsmProgr_Type = Gauge32
_CfprApObserveObservedFsmProgr_Object = MibTableColumn
cfprApObserveObservedFsmProgr = _CfprApObserveObservedFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 8),
    _CfprApObserveObservedFsmProgr_Type()
)
cfprApObserveObservedFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmProgr.setStatus("current")
_CfprApObserveObservedFsmRmtInvErrCode_Type = Gauge32
_CfprApObserveObservedFsmRmtInvErrCode_Object = MibTableColumn
cfprApObserveObservedFsmRmtInvErrCode = _CfprApObserveObservedFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 9),
    _CfprApObserveObservedFsmRmtInvErrCode_Type()
)
cfprApObserveObservedFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRmtInvErrCode.setStatus("current")
_CfprApObserveObservedFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApObserveObservedFsmRmtInvErrDescr_Object = MibTableColumn
cfprApObserveObservedFsmRmtInvErrDescr = _CfprApObserveObservedFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 10),
    _CfprApObserveObservedFsmRmtInvErrDescr_Type()
)
cfprApObserveObservedFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRmtInvErrDescr.setStatus("current")
_CfprApObserveObservedFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApObserveObservedFsmRmtInvRslt_Object = MibTableColumn
cfprApObserveObservedFsmRmtInvRslt = _CfprApObserveObservedFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 11),
    _CfprApObserveObservedFsmRmtInvRslt_Type()
)
cfprApObserveObservedFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRmtInvRslt.setStatus("current")
_CfprApObserveObservedFsmStageDescr_Type = SnmpAdminString
_CfprApObserveObservedFsmStageDescr_Object = MibTableColumn
cfprApObserveObservedFsmStageDescr = _CfprApObserveObservedFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 12),
    _CfprApObserveObservedFsmStageDescr_Type()
)
cfprApObserveObservedFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageDescr.setStatus("current")
_CfprApObserveObservedFsmStamp_Type = DateAndTime
_CfprApObserveObservedFsmStamp_Object = MibTableColumn
cfprApObserveObservedFsmStamp = _CfprApObserveObservedFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 13),
    _CfprApObserveObservedFsmStamp_Type()
)
cfprApObserveObservedFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStamp.setStatus("current")
_CfprApObserveObservedFsmStatus_Type = SnmpAdminString
_CfprApObserveObservedFsmStatus_Object = MibTableColumn
cfprApObserveObservedFsmStatus = _CfprApObserveObservedFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 14),
    _CfprApObserveObservedFsmStatus_Type()
)
cfprApObserveObservedFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStatus.setStatus("current")
_CfprApObserveObservedFsmTry_Type = Gauge32
_CfprApObserveObservedFsmTry_Object = MibTableColumn
cfprApObserveObservedFsmTry = _CfprApObserveObservedFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 15),
    _CfprApObserveObservedFsmTry_Type()
)
cfprApObserveObservedFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTry.setStatus("current")
_CfprApObserveObservedGenNum_Type = Gauge32
_CfprApObserveObservedGenNum_Object = MibTableColumn
cfprApObserveObservedGenNum = _CfprApObserveObservedGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 16),
    _CfprApObserveObservedGenNum_Type()
)
cfprApObserveObservedGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedGenNum.setStatus("current")
_CfprApObserveObservedHierarchical_Type = TruthValue
_CfprApObserveObservedHierarchical_Object = MibTableColumn
cfprApObserveObservedHierarchical = _CfprApObserveObservedHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 17),
    _CfprApObserveObservedHierarchical_Type()
)
cfprApObserveObservedHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedHierarchical.setStatus("current")
_CfprApObserveObservedId_Type = Gauge32
_CfprApObserveObservedId_Object = MibTableColumn
cfprApObserveObservedId = _CfprApObserveObservedId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 18),
    _CfprApObserveObservedId_Type()
)
cfprApObserveObservedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedId.setStatus("current")
_CfprApObserveObservedIsDeleted_Type = TruthValue
_CfprApObserveObservedIsDeleted_Object = MibTableColumn
cfprApObserveObservedIsDeleted = _CfprApObserveObservedIsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 19),
    _CfprApObserveObservedIsDeleted_Type()
)
cfprApObserveObservedIsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedIsDeleted.setStatus("current")
_CfprApObserveObservedObservedDn_Type = SnmpAdminString
_CfprApObserveObservedObservedDn_Object = MibTableColumn
cfprApObserveObservedObservedDn = _CfprApObserveObservedObservedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 2, 1, 20),
    _CfprApObserveObservedObservedDn_Type()
)
cfprApObserveObservedObservedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedObservedDn.setStatus("current")
_CfprApObserveObservedContTable_Object = MibTable
cfprApObserveObservedContTable = _CfprApObserveObservedContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 3)
)
if mibBuilder.loadTexts:
    cfprApObserveObservedContTable.setStatus("current")
_CfprApObserveObservedContEntry_Object = MibTableRow
cfprApObserveObservedContEntry = _CfprApObserveObservedContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 3, 1)
)
cfprApObserveObservedContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OBSERVE-MIB", "cfprApObserveObservedContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApObserveObservedContEntry.setStatus("current")
_CfprApObserveObservedContInstanceId_Type = CfprApManagedObjectId
_CfprApObserveObservedContInstanceId_Object = MibTableColumn
cfprApObserveObservedContInstanceId = _CfprApObserveObservedContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 3, 1, 1),
    _CfprApObserveObservedContInstanceId_Type()
)
cfprApObserveObservedContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApObserveObservedContInstanceId.setStatus("current")
_CfprApObserveObservedContDn_Type = CfprApManagedObjectDn
_CfprApObserveObservedContDn_Object = MibTableColumn
cfprApObserveObservedContDn = _CfprApObserveObservedContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 3, 1, 2),
    _CfprApObserveObservedContDn_Type()
)
cfprApObserveObservedContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedContDn.setStatus("current")
_CfprApObserveObservedContRn_Type = SnmpAdminString
_CfprApObserveObservedContRn_Object = MibTableColumn
cfprApObserveObservedContRn = _CfprApObserveObservedContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 3, 1, 3),
    _CfprApObserveObservedContRn_Type()
)
cfprApObserveObservedContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedContRn.setStatus("current")
_CfprApObserveObservedContIdCount_Type = Gauge32
_CfprApObserveObservedContIdCount_Object = MibTableColumn
cfprApObserveObservedContIdCount = _CfprApObserveObservedContIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 3, 1, 4),
    _CfprApObserveObservedContIdCount_Type()
)
cfprApObserveObservedContIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedContIdCount.setStatus("current")
_CfprApObserveObservedFsmTable_Object = MibTable
cfprApObserveObservedFsmTable = _CfprApObserveObservedFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4)
)
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTable.setStatus("current")
_CfprApObserveObservedFsmEntry_Object = MibTableRow
cfprApObserveObservedFsmEntry = _CfprApObserveObservedFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1)
)
cfprApObserveObservedFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OBSERVE-MIB", "cfprApObserveObservedFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmEntry.setStatus("current")
_CfprApObserveObservedFsmInstanceId_Type = CfprApManagedObjectId
_CfprApObserveObservedFsmInstanceId_Object = MibTableColumn
cfprApObserveObservedFsmInstanceId = _CfprApObserveObservedFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 1),
    _CfprApObserveObservedFsmInstanceId_Type()
)
cfprApObserveObservedFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmInstanceId.setStatus("current")
_CfprApObserveObservedFsmDn_Type = CfprApManagedObjectDn
_CfprApObserveObservedFsmDn_Object = MibTableColumn
cfprApObserveObservedFsmDn = _CfprApObserveObservedFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 2),
    _CfprApObserveObservedFsmDn_Type()
)
cfprApObserveObservedFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmDn.setStatus("current")
_CfprApObserveObservedFsmRn_Type = SnmpAdminString
_CfprApObserveObservedFsmRn_Object = MibTableColumn
cfprApObserveObservedFsmRn = _CfprApObserveObservedFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 3),
    _CfprApObserveObservedFsmRn_Type()
)
cfprApObserveObservedFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRn.setStatus("current")
_CfprApObserveObservedFsmCompletionTime_Type = DateAndTime
_CfprApObserveObservedFsmCompletionTime_Object = MibTableColumn
cfprApObserveObservedFsmCompletionTime = _CfprApObserveObservedFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 4),
    _CfprApObserveObservedFsmCompletionTime_Type()
)
cfprApObserveObservedFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmCompletionTime.setStatus("current")
_CfprApObserveObservedFsmCurrentFsm_Type = CfprApObserveObservedFsmCurrentFsm
_CfprApObserveObservedFsmCurrentFsm_Object = MibTableColumn
cfprApObserveObservedFsmCurrentFsm = _CfprApObserveObservedFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 5),
    _CfprApObserveObservedFsmCurrentFsm_Type()
)
cfprApObserveObservedFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmCurrentFsm.setStatus("current")
_CfprApObserveObservedFsmDescrData_Type = SnmpAdminString
_CfprApObserveObservedFsmDescrData_Object = MibTableColumn
cfprApObserveObservedFsmDescrData = _CfprApObserveObservedFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 6),
    _CfprApObserveObservedFsmDescrData_Type()
)
cfprApObserveObservedFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmDescrData.setStatus("current")
_CfprApObserveObservedFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApObserveObservedFsmFsmStatus_Object = MibTableColumn
cfprApObserveObservedFsmFsmStatus = _CfprApObserveObservedFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 7),
    _CfprApObserveObservedFsmFsmStatus_Type()
)
cfprApObserveObservedFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmFsmStatus.setStatus("current")
_CfprApObserveObservedFsmProgress_Type = Gauge32
_CfprApObserveObservedFsmProgress_Object = MibTableColumn
cfprApObserveObservedFsmProgress = _CfprApObserveObservedFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 8),
    _CfprApObserveObservedFsmProgress_Type()
)
cfprApObserveObservedFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmProgress.setStatus("current")
_CfprApObserveObservedFsmRmtErrCode_Type = Gauge32
_CfprApObserveObservedFsmRmtErrCode_Object = MibTableColumn
cfprApObserveObservedFsmRmtErrCode = _CfprApObserveObservedFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 9),
    _CfprApObserveObservedFsmRmtErrCode_Type()
)
cfprApObserveObservedFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRmtErrCode.setStatus("current")
_CfprApObserveObservedFsmRmtErrDescr_Type = SnmpAdminString
_CfprApObserveObservedFsmRmtErrDescr_Object = MibTableColumn
cfprApObserveObservedFsmRmtErrDescr = _CfprApObserveObservedFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 10),
    _CfprApObserveObservedFsmRmtErrDescr_Type()
)
cfprApObserveObservedFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRmtErrDescr.setStatus("current")
_CfprApObserveObservedFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApObserveObservedFsmRmtRslt_Object = MibTableColumn
cfprApObserveObservedFsmRmtRslt = _CfprApObserveObservedFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 4, 1, 11),
    _CfprApObserveObservedFsmRmtRslt_Type()
)
cfprApObserveObservedFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmRmtRslt.setStatus("current")
_CfprApObserveObservedFsmStageTable_Object = MibTable
cfprApObserveObservedFsmStageTable = _CfprApObserveObservedFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5)
)
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageTable.setStatus("current")
_CfprApObserveObservedFsmStageEntry_Object = MibTableRow
cfprApObserveObservedFsmStageEntry = _CfprApObserveObservedFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1)
)
cfprApObserveObservedFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OBSERVE-MIB", "cfprApObserveObservedFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageEntry.setStatus("current")
_CfprApObserveObservedFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApObserveObservedFsmStageInstanceId_Object = MibTableColumn
cfprApObserveObservedFsmStageInstanceId = _CfprApObserveObservedFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 1),
    _CfprApObserveObservedFsmStageInstanceId_Type()
)
cfprApObserveObservedFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageInstanceId.setStatus("current")
_CfprApObserveObservedFsmStageDn_Type = CfprApManagedObjectDn
_CfprApObserveObservedFsmStageDn_Object = MibTableColumn
cfprApObserveObservedFsmStageDn = _CfprApObserveObservedFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 2),
    _CfprApObserveObservedFsmStageDn_Type()
)
cfprApObserveObservedFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageDn.setStatus("current")
_CfprApObserveObservedFsmStageRn_Type = SnmpAdminString
_CfprApObserveObservedFsmStageRn_Object = MibTableColumn
cfprApObserveObservedFsmStageRn = _CfprApObserveObservedFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 3),
    _CfprApObserveObservedFsmStageRn_Type()
)
cfprApObserveObservedFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageRn.setStatus("current")
_CfprApObserveObservedFsmStageDescrData_Type = SnmpAdminString
_CfprApObserveObservedFsmStageDescrData_Object = MibTableColumn
cfprApObserveObservedFsmStageDescrData = _CfprApObserveObservedFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 4),
    _CfprApObserveObservedFsmStageDescrData_Type()
)
cfprApObserveObservedFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageDescrData.setStatus("current")
_CfprApObserveObservedFsmStageLastUpdateTime_Type = DateAndTime
_CfprApObserveObservedFsmStageLastUpdateTime_Object = MibTableColumn
cfprApObserveObservedFsmStageLastUpdateTime = _CfprApObserveObservedFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 5),
    _CfprApObserveObservedFsmStageLastUpdateTime_Type()
)
cfprApObserveObservedFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageLastUpdateTime.setStatus("current")
_CfprApObserveObservedFsmStageName_Type = CfprApObserveObservedFsmStageName
_CfprApObserveObservedFsmStageName_Object = MibTableColumn
cfprApObserveObservedFsmStageName = _CfprApObserveObservedFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 6),
    _CfprApObserveObservedFsmStageName_Type()
)
cfprApObserveObservedFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageName.setStatus("current")
_CfprApObserveObservedFsmStageOrder_Type = Gauge32
_CfprApObserveObservedFsmStageOrder_Object = MibTableColumn
cfprApObserveObservedFsmStageOrder = _CfprApObserveObservedFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 7),
    _CfprApObserveObservedFsmStageOrder_Type()
)
cfprApObserveObservedFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageOrder.setStatus("current")
_CfprApObserveObservedFsmStageRetry_Type = Gauge32
_CfprApObserveObservedFsmStageRetry_Object = MibTableColumn
cfprApObserveObservedFsmStageRetry = _CfprApObserveObservedFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 8),
    _CfprApObserveObservedFsmStageRetry_Type()
)
cfprApObserveObservedFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageRetry.setStatus("current")
_CfprApObserveObservedFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApObserveObservedFsmStageStageStatus_Object = MibTableColumn
cfprApObserveObservedFsmStageStageStatus = _CfprApObserveObservedFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 5, 1, 9),
    _CfprApObserveObservedFsmStageStageStatus_Type()
)
cfprApObserveObservedFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmStageStageStatus.setStatus("current")
_CfprApObserveObservedFsmTaskTable_Object = MibTable
cfprApObserveObservedFsmTaskTable = _CfprApObserveObservedFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6)
)
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskTable.setStatus("current")
_CfprApObserveObservedFsmTaskEntry_Object = MibTableRow
cfprApObserveObservedFsmTaskEntry = _CfprApObserveObservedFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1)
)
cfprApObserveObservedFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OBSERVE-MIB", "cfprApObserveObservedFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskEntry.setStatus("current")
_CfprApObserveObservedFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApObserveObservedFsmTaskInstanceId_Object = MibTableColumn
cfprApObserveObservedFsmTaskInstanceId = _CfprApObserveObservedFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 1),
    _CfprApObserveObservedFsmTaskInstanceId_Type()
)
cfprApObserveObservedFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskInstanceId.setStatus("current")
_CfprApObserveObservedFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApObserveObservedFsmTaskDn_Object = MibTableColumn
cfprApObserveObservedFsmTaskDn = _CfprApObserveObservedFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 2),
    _CfprApObserveObservedFsmTaskDn_Type()
)
cfprApObserveObservedFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskDn.setStatus("current")
_CfprApObserveObservedFsmTaskRn_Type = SnmpAdminString
_CfprApObserveObservedFsmTaskRn_Object = MibTableColumn
cfprApObserveObservedFsmTaskRn = _CfprApObserveObservedFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 3),
    _CfprApObserveObservedFsmTaskRn_Type()
)
cfprApObserveObservedFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskRn.setStatus("current")
_CfprApObserveObservedFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApObserveObservedFsmTaskCompletion_Object = MibTableColumn
cfprApObserveObservedFsmTaskCompletion = _CfprApObserveObservedFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 4),
    _CfprApObserveObservedFsmTaskCompletion_Type()
)
cfprApObserveObservedFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskCompletion.setStatus("current")
_CfprApObserveObservedFsmTaskFlags_Type = CfprApFsmFlags
_CfprApObserveObservedFsmTaskFlags_Object = MibTableColumn
cfprApObserveObservedFsmTaskFlags = _CfprApObserveObservedFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 5),
    _CfprApObserveObservedFsmTaskFlags_Type()
)
cfprApObserveObservedFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskFlags.setStatus("current")
_CfprApObserveObservedFsmTaskItem_Type = CfprApObserveObservedFsmTaskItem
_CfprApObserveObservedFsmTaskItem_Object = MibTableColumn
cfprApObserveObservedFsmTaskItem = _CfprApObserveObservedFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 6),
    _CfprApObserveObservedFsmTaskItem_Type()
)
cfprApObserveObservedFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskItem.setStatus("current")
_CfprApObserveObservedFsmTaskSeqId_Type = Gauge32
_CfprApObserveObservedFsmTaskSeqId_Object = MibTableColumn
cfprApObserveObservedFsmTaskSeqId = _CfprApObserveObservedFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 57, 6, 1, 7),
    _CfprApObserveObservedFsmTaskSeqId_Type()
)
cfprApObserveObservedFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApObserveObservedFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-OBSERVE-MIB",
    **{"cfprApObserveObjects": cfprApObserveObjects,
       "cfprApObserveFilterTable": cfprApObserveFilterTable,
       "cfprApObserveFilterEntry": cfprApObserveFilterEntry,
       "cfprApObserveFilterInstanceId": cfprApObserveFilterInstanceId,
       "cfprApObserveFilterDn": cfprApObserveFilterDn,
       "cfprApObserveFilterRn": cfprApObserveFilterRn,
       "cfprApObserveFilterAndOperation": cfprApObserveFilterAndOperation,
       "cfprApObserveFilterChildClassId": cfprApObserveFilterChildClassId,
       "cfprApObserveFilterFilterClassId": cfprApObserveFilterFilterClassId,
       "cfprApObserveFilterFilterPropId1": cfprApObserveFilterFilterPropId1,
       "cfprApObserveFilterFilterPropId2": cfprApObserveFilterFilterPropId2,
       "cfprApObserveFilterFilterPropId3": cfprApObserveFilterFilterPropId3,
       "cfprApObserveFilterFilterPropValue1": cfprApObserveFilterFilterPropValue1,
       "cfprApObserveFilterFilterPropValue2": cfprApObserveFilterFilterPropValue2,
       "cfprApObserveFilterFilterPropValue3": cfprApObserveFilterFilterPropValue3,
       "cfprApObserveFilterHierarchical": cfprApObserveFilterHierarchical,
       "cfprApObserveFilterReplicateIfNoChild": cfprApObserveFilterReplicateIfNoChild,
       "cfprApObserveObservedTable": cfprApObserveObservedTable,
       "cfprApObserveObservedEntry": cfprApObserveObservedEntry,
       "cfprApObserveObservedInstanceId": cfprApObserveObservedInstanceId,
       "cfprApObserveObservedDn": cfprApObserveObservedDn,
       "cfprApObserveObservedRn": cfprApObserveObservedRn,
       "cfprApObserveObservedDataSrcAppType": cfprApObserveObservedDataSrcAppType,
       "cfprApObserveObservedDataSrcSysId": cfprApObserveObservedDataSrcSysId,
       "cfprApObserveObservedFsmDescr": cfprApObserveObservedFsmDescr,
       "cfprApObserveObservedFsmPrev": cfprApObserveObservedFsmPrev,
       "cfprApObserveObservedFsmProgr": cfprApObserveObservedFsmProgr,
       "cfprApObserveObservedFsmRmtInvErrCode": cfprApObserveObservedFsmRmtInvErrCode,
       "cfprApObserveObservedFsmRmtInvErrDescr": cfprApObserveObservedFsmRmtInvErrDescr,
       "cfprApObserveObservedFsmRmtInvRslt": cfprApObserveObservedFsmRmtInvRslt,
       "cfprApObserveObservedFsmStageDescr": cfprApObserveObservedFsmStageDescr,
       "cfprApObserveObservedFsmStamp": cfprApObserveObservedFsmStamp,
       "cfprApObserveObservedFsmStatus": cfprApObserveObservedFsmStatus,
       "cfprApObserveObservedFsmTry": cfprApObserveObservedFsmTry,
       "cfprApObserveObservedGenNum": cfprApObserveObservedGenNum,
       "cfprApObserveObservedHierarchical": cfprApObserveObservedHierarchical,
       "cfprApObserveObservedId": cfprApObserveObservedId,
       "cfprApObserveObservedIsDeleted": cfprApObserveObservedIsDeleted,
       "cfprApObserveObservedObservedDn": cfprApObserveObservedObservedDn,
       "cfprApObserveObservedContTable": cfprApObserveObservedContTable,
       "cfprApObserveObservedContEntry": cfprApObserveObservedContEntry,
       "cfprApObserveObservedContInstanceId": cfprApObserveObservedContInstanceId,
       "cfprApObserveObservedContDn": cfprApObserveObservedContDn,
       "cfprApObserveObservedContRn": cfprApObserveObservedContRn,
       "cfprApObserveObservedContIdCount": cfprApObserveObservedContIdCount,
       "cfprApObserveObservedFsmTable": cfprApObserveObservedFsmTable,
       "cfprApObserveObservedFsmEntry": cfprApObserveObservedFsmEntry,
       "cfprApObserveObservedFsmInstanceId": cfprApObserveObservedFsmInstanceId,
       "cfprApObserveObservedFsmDn": cfprApObserveObservedFsmDn,
       "cfprApObserveObservedFsmRn": cfprApObserveObservedFsmRn,
       "cfprApObserveObservedFsmCompletionTime": cfprApObserveObservedFsmCompletionTime,
       "cfprApObserveObservedFsmCurrentFsm": cfprApObserveObservedFsmCurrentFsm,
       "cfprApObserveObservedFsmDescrData": cfprApObserveObservedFsmDescrData,
       "cfprApObserveObservedFsmFsmStatus": cfprApObserveObservedFsmFsmStatus,
       "cfprApObserveObservedFsmProgress": cfprApObserveObservedFsmProgress,
       "cfprApObserveObservedFsmRmtErrCode": cfprApObserveObservedFsmRmtErrCode,
       "cfprApObserveObservedFsmRmtErrDescr": cfprApObserveObservedFsmRmtErrDescr,
       "cfprApObserveObservedFsmRmtRslt": cfprApObserveObservedFsmRmtRslt,
       "cfprApObserveObservedFsmStageTable": cfprApObserveObservedFsmStageTable,
       "cfprApObserveObservedFsmStageEntry": cfprApObserveObservedFsmStageEntry,
       "cfprApObserveObservedFsmStageInstanceId": cfprApObserveObservedFsmStageInstanceId,
       "cfprApObserveObservedFsmStageDn": cfprApObserveObservedFsmStageDn,
       "cfprApObserveObservedFsmStageRn": cfprApObserveObservedFsmStageRn,
       "cfprApObserveObservedFsmStageDescrData": cfprApObserveObservedFsmStageDescrData,
       "cfprApObserveObservedFsmStageLastUpdateTime": cfprApObserveObservedFsmStageLastUpdateTime,
       "cfprApObserveObservedFsmStageName": cfprApObserveObservedFsmStageName,
       "cfprApObserveObservedFsmStageOrder": cfprApObserveObservedFsmStageOrder,
       "cfprApObserveObservedFsmStageRetry": cfprApObserveObservedFsmStageRetry,
       "cfprApObserveObservedFsmStageStageStatus": cfprApObserveObservedFsmStageStageStatus,
       "cfprApObserveObservedFsmTaskTable": cfprApObserveObservedFsmTaskTable,
       "cfprApObserveObservedFsmTaskEntry": cfprApObserveObservedFsmTaskEntry,
       "cfprApObserveObservedFsmTaskInstanceId": cfprApObserveObservedFsmTaskInstanceId,
       "cfprApObserveObservedFsmTaskDn": cfprApObserveObservedFsmTaskDn,
       "cfprApObserveObservedFsmTaskRn": cfprApObserveObservedFsmTaskRn,
       "cfprApObserveObservedFsmTaskCompletion": cfprApObserveObservedFsmTaskCompletion,
       "cfprApObserveObservedFsmTaskFlags": cfprApObserveObservedFsmTaskFlags,
       "cfprApObserveObservedFsmTaskItem": cfprApObserveObservedFsmTaskItem,
       "cfprApObserveObservedFsmTaskSeqId": cfprApObserveObservedFsmTaskSeqId}
)
