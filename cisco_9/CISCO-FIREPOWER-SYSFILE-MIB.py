# SNMP MIB module (CISCO-FIREPOWER-SYSFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-SYSFILE-MIB.mib
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
 CfprNetworkSwitchId,
 CfprSysfileMutationAction,
 CfprSysfileMutationFsmCurrentFsm,
 CfprSysfileMutationFsmStageName,
 CfprSysfileMutationFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprNetworkSwitchId",
    "CfprSysfileMutationAction",
    "CfprSysfileMutationFsmCurrentFsm",
    "CfprSysfileMutationFsmStageName",
    "CfprSysfileMutationFsmTaskItem")

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

cfprSysfileObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprSysfileDigestTable_Object = MibTable
cfprSysfileDigestTable = _CfprSysfileDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1)
)
if mibBuilder.loadTexts:
    cfprSysfileDigestTable.setStatus("current")
_CfprSysfileDigestEntry_Object = MibTableRow
cfprSysfileDigestEntry = _CfprSysfileDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1)
)
cfprSysfileDigestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSFILE-MIB", "cfprSysfileDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysfileDigestEntry.setStatus("current")
_CfprSysfileDigestInstanceId_Type = CfprManagedObjectId
_CfprSysfileDigestInstanceId_Object = MibTableColumn
cfprSysfileDigestInstanceId = _CfprSysfileDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 1),
    _CfprSysfileDigestInstanceId_Type()
)
cfprSysfileDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysfileDigestInstanceId.setStatus("current")
_CfprSysfileDigestDn_Type = CfprManagedObjectDn
_CfprSysfileDigestDn_Object = MibTableColumn
cfprSysfileDigestDn = _CfprSysfileDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 2),
    _CfprSysfileDigestDn_Type()
)
cfprSysfileDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestDn.setStatus("current")
_CfprSysfileDigestRn_Type = SnmpAdminString
_CfprSysfileDigestRn_Object = MibTableColumn
cfprSysfileDigestRn = _CfprSysfileDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 3),
    _CfprSysfileDigestRn_Type()
)
cfprSysfileDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestRn.setStatus("current")
_CfprSysfileDigestCreationTS_Type = Unsigned64
_CfprSysfileDigestCreationTS_Object = MibTableColumn
cfprSysfileDigestCreationTS = _CfprSysfileDigestCreationTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 4),
    _CfprSysfileDigestCreationTS_Type()
)
cfprSysfileDigestCreationTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestCreationTS.setStatus("current")
_CfprSysfileDigestDescr_Type = SnmpAdminString
_CfprSysfileDigestDescr_Object = MibTableColumn
cfprSysfileDigestDescr = _CfprSysfileDigestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 5),
    _CfprSysfileDigestDescr_Type()
)
cfprSysfileDigestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestDescr.setStatus("current")
_CfprSysfileDigestName_Type = SnmpAdminString
_CfprSysfileDigestName_Object = MibTableColumn
cfprSysfileDigestName = _CfprSysfileDigestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 6),
    _CfprSysfileDigestName_Type()
)
cfprSysfileDigestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestName.setStatus("current")
_CfprSysfileDigestSize_Type = Gauge32
_CfprSysfileDigestSize_Object = MibTableColumn
cfprSysfileDigestSize = _CfprSysfileDigestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 7),
    _CfprSysfileDigestSize_Type()
)
cfprSysfileDigestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestSize.setStatus("current")
_CfprSysfileDigestSource_Type = SnmpAdminString
_CfprSysfileDigestSource_Object = MibTableColumn
cfprSysfileDigestSource = _CfprSysfileDigestSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 8),
    _CfprSysfileDigestSource_Type()
)
cfprSysfileDigestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestSource.setStatus("current")
_CfprSysfileDigestSwitchId_Type = CfprNetworkSwitchId
_CfprSysfileDigestSwitchId_Object = MibTableColumn
cfprSysfileDigestSwitchId = _CfprSysfileDigestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 9),
    _CfprSysfileDigestSwitchId_Type()
)
cfprSysfileDigestSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestSwitchId.setStatus("current")
_CfprSysfileDigestTs_Type = DateAndTime
_CfprSysfileDigestTs_Object = MibTableColumn
cfprSysfileDigestTs = _CfprSysfileDigestTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 10),
    _CfprSysfileDigestTs_Type()
)
cfprSysfileDigestTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestTs.setStatus("current")
_CfprSysfileDigestUri_Type = SnmpAdminString
_CfprSysfileDigestUri_Object = MibTableColumn
cfprSysfileDigestUri = _CfprSysfileDigestUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 1, 1, 11),
    _CfprSysfileDigestUri_Type()
)
cfprSysfileDigestUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileDigestUri.setStatus("current")
_CfprSysfileMutationTable_Object = MibTable
cfprSysfileMutationTable = _CfprSysfileMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2)
)
if mibBuilder.loadTexts:
    cfprSysfileMutationTable.setStatus("current")
_CfprSysfileMutationEntry_Object = MibTableRow
cfprSysfileMutationEntry = _CfprSysfileMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1)
)
cfprSysfileMutationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSFILE-MIB", "cfprSysfileMutationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysfileMutationEntry.setStatus("current")
_CfprSysfileMutationInstanceId_Type = CfprManagedObjectId
_CfprSysfileMutationInstanceId_Object = MibTableColumn
cfprSysfileMutationInstanceId = _CfprSysfileMutationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 1),
    _CfprSysfileMutationInstanceId_Type()
)
cfprSysfileMutationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysfileMutationInstanceId.setStatus("current")
_CfprSysfileMutationDn_Type = CfprManagedObjectDn
_CfprSysfileMutationDn_Object = MibTableColumn
cfprSysfileMutationDn = _CfprSysfileMutationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 2),
    _CfprSysfileMutationDn_Type()
)
cfprSysfileMutationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationDn.setStatus("current")
_CfprSysfileMutationRn_Type = SnmpAdminString
_CfprSysfileMutationRn_Object = MibTableColumn
cfprSysfileMutationRn = _CfprSysfileMutationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 3),
    _CfprSysfileMutationRn_Type()
)
cfprSysfileMutationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationRn.setStatus("current")
_CfprSysfileMutationAction_Type = CfprSysfileMutationAction
_CfprSysfileMutationAction_Object = MibTableColumn
cfprSysfileMutationAction = _CfprSysfileMutationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 4),
    _CfprSysfileMutationAction_Type()
)
cfprSysfileMutationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationAction.setStatus("current")
_CfprSysfileMutationDescr_Type = SnmpAdminString
_CfprSysfileMutationDescr_Object = MibTableColumn
cfprSysfileMutationDescr = _CfprSysfileMutationDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 5),
    _CfprSysfileMutationDescr_Type()
)
cfprSysfileMutationDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationDescr.setStatus("current")
_CfprSysfileMutationFsmDescr_Type = SnmpAdminString
_CfprSysfileMutationFsmDescr_Object = MibTableColumn
cfprSysfileMutationFsmDescr = _CfprSysfileMutationFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 6),
    _CfprSysfileMutationFsmDescr_Type()
)
cfprSysfileMutationFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmDescr.setStatus("current")
_CfprSysfileMutationFsmPrev_Type = SnmpAdminString
_CfprSysfileMutationFsmPrev_Object = MibTableColumn
cfprSysfileMutationFsmPrev = _CfprSysfileMutationFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 7),
    _CfprSysfileMutationFsmPrev_Type()
)
cfprSysfileMutationFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmPrev.setStatus("current")
_CfprSysfileMutationFsmProgr_Type = Gauge32
_CfprSysfileMutationFsmProgr_Object = MibTableColumn
cfprSysfileMutationFsmProgr = _CfprSysfileMutationFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 8),
    _CfprSysfileMutationFsmProgr_Type()
)
cfprSysfileMutationFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmProgr.setStatus("current")
_CfprSysfileMutationFsmRmtInvErrCode_Type = Gauge32
_CfprSysfileMutationFsmRmtInvErrCode_Object = MibTableColumn
cfprSysfileMutationFsmRmtInvErrCode = _CfprSysfileMutationFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 9),
    _CfprSysfileMutationFsmRmtInvErrCode_Type()
)
cfprSysfileMutationFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRmtInvErrCode.setStatus("current")
_CfprSysfileMutationFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSysfileMutationFsmRmtInvErrDescr_Object = MibTableColumn
cfprSysfileMutationFsmRmtInvErrDescr = _CfprSysfileMutationFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 10),
    _CfprSysfileMutationFsmRmtInvErrDescr_Type()
)
cfprSysfileMutationFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRmtInvErrDescr.setStatus("current")
_CfprSysfileMutationFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSysfileMutationFsmRmtInvRslt_Object = MibTableColumn
cfprSysfileMutationFsmRmtInvRslt = _CfprSysfileMutationFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 11),
    _CfprSysfileMutationFsmRmtInvRslt_Type()
)
cfprSysfileMutationFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRmtInvRslt.setStatus("current")
_CfprSysfileMutationFsmStageDescr_Type = SnmpAdminString
_CfprSysfileMutationFsmStageDescr_Object = MibTableColumn
cfprSysfileMutationFsmStageDescr = _CfprSysfileMutationFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 12),
    _CfprSysfileMutationFsmStageDescr_Type()
)
cfprSysfileMutationFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageDescr.setStatus("current")
_CfprSysfileMutationFsmStamp_Type = DateAndTime
_CfprSysfileMutationFsmStamp_Object = MibTableColumn
cfprSysfileMutationFsmStamp = _CfprSysfileMutationFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 13),
    _CfprSysfileMutationFsmStamp_Type()
)
cfprSysfileMutationFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStamp.setStatus("current")
_CfprSysfileMutationFsmStatus_Type = SnmpAdminString
_CfprSysfileMutationFsmStatus_Object = MibTableColumn
cfprSysfileMutationFsmStatus = _CfprSysfileMutationFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 14),
    _CfprSysfileMutationFsmStatus_Type()
)
cfprSysfileMutationFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStatus.setStatus("current")
_CfprSysfileMutationFsmTry_Type = Gauge32
_CfprSysfileMutationFsmTry_Object = MibTableColumn
cfprSysfileMutationFsmTry = _CfprSysfileMutationFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 2, 1, 15),
    _CfprSysfileMutationFsmTry_Type()
)
cfprSysfileMutationFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTry.setStatus("current")
_CfprSysfileMutationFsmTable_Object = MibTable
cfprSysfileMutationFsmTable = _CfprSysfileMutationFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3)
)
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTable.setStatus("current")
_CfprSysfileMutationFsmEntry_Object = MibTableRow
cfprSysfileMutationFsmEntry = _CfprSysfileMutationFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1)
)
cfprSysfileMutationFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSFILE-MIB", "cfprSysfileMutationFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmEntry.setStatus("current")
_CfprSysfileMutationFsmInstanceId_Type = CfprManagedObjectId
_CfprSysfileMutationFsmInstanceId_Object = MibTableColumn
cfprSysfileMutationFsmInstanceId = _CfprSysfileMutationFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 1),
    _CfprSysfileMutationFsmInstanceId_Type()
)
cfprSysfileMutationFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmInstanceId.setStatus("current")
_CfprSysfileMutationFsmDn_Type = CfprManagedObjectDn
_CfprSysfileMutationFsmDn_Object = MibTableColumn
cfprSysfileMutationFsmDn = _CfprSysfileMutationFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 2),
    _CfprSysfileMutationFsmDn_Type()
)
cfprSysfileMutationFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmDn.setStatus("current")
_CfprSysfileMutationFsmRn_Type = SnmpAdminString
_CfprSysfileMutationFsmRn_Object = MibTableColumn
cfprSysfileMutationFsmRn = _CfprSysfileMutationFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 3),
    _CfprSysfileMutationFsmRn_Type()
)
cfprSysfileMutationFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRn.setStatus("current")
_CfprSysfileMutationFsmCompletionTime_Type = DateAndTime
_CfprSysfileMutationFsmCompletionTime_Object = MibTableColumn
cfprSysfileMutationFsmCompletionTime = _CfprSysfileMutationFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 4),
    _CfprSysfileMutationFsmCompletionTime_Type()
)
cfprSysfileMutationFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmCompletionTime.setStatus("current")
_CfprSysfileMutationFsmCurrentFsm_Type = CfprSysfileMutationFsmCurrentFsm
_CfprSysfileMutationFsmCurrentFsm_Object = MibTableColumn
cfprSysfileMutationFsmCurrentFsm = _CfprSysfileMutationFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 5),
    _CfprSysfileMutationFsmCurrentFsm_Type()
)
cfprSysfileMutationFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmCurrentFsm.setStatus("current")
_CfprSysfileMutationFsmDescrData_Type = SnmpAdminString
_CfprSysfileMutationFsmDescrData_Object = MibTableColumn
cfprSysfileMutationFsmDescrData = _CfprSysfileMutationFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 6),
    _CfprSysfileMutationFsmDescrData_Type()
)
cfprSysfileMutationFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmDescrData.setStatus("current")
_CfprSysfileMutationFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSysfileMutationFsmFsmStatus_Object = MibTableColumn
cfprSysfileMutationFsmFsmStatus = _CfprSysfileMutationFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 7),
    _CfprSysfileMutationFsmFsmStatus_Type()
)
cfprSysfileMutationFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmFsmStatus.setStatus("current")
_CfprSysfileMutationFsmProgress_Type = Gauge32
_CfprSysfileMutationFsmProgress_Object = MibTableColumn
cfprSysfileMutationFsmProgress = _CfprSysfileMutationFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 8),
    _CfprSysfileMutationFsmProgress_Type()
)
cfprSysfileMutationFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmProgress.setStatus("current")
_CfprSysfileMutationFsmRmtErrCode_Type = Gauge32
_CfprSysfileMutationFsmRmtErrCode_Object = MibTableColumn
cfprSysfileMutationFsmRmtErrCode = _CfprSysfileMutationFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 9),
    _CfprSysfileMutationFsmRmtErrCode_Type()
)
cfprSysfileMutationFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRmtErrCode.setStatus("current")
_CfprSysfileMutationFsmRmtErrDescr_Type = SnmpAdminString
_CfprSysfileMutationFsmRmtErrDescr_Object = MibTableColumn
cfprSysfileMutationFsmRmtErrDescr = _CfprSysfileMutationFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 10),
    _CfprSysfileMutationFsmRmtErrDescr_Type()
)
cfprSysfileMutationFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRmtErrDescr.setStatus("current")
_CfprSysfileMutationFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSysfileMutationFsmRmtRslt_Object = MibTableColumn
cfprSysfileMutationFsmRmtRslt = _CfprSysfileMutationFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 3, 1, 11),
    _CfprSysfileMutationFsmRmtRslt_Type()
)
cfprSysfileMutationFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmRmtRslt.setStatus("current")
_CfprSysfileMutationFsmStageTable_Object = MibTable
cfprSysfileMutationFsmStageTable = _CfprSysfileMutationFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4)
)
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageTable.setStatus("current")
_CfprSysfileMutationFsmStageEntry_Object = MibTableRow
cfprSysfileMutationFsmStageEntry = _CfprSysfileMutationFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1)
)
cfprSysfileMutationFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSFILE-MIB", "cfprSysfileMutationFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageEntry.setStatus("current")
_CfprSysfileMutationFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSysfileMutationFsmStageInstanceId_Object = MibTableColumn
cfprSysfileMutationFsmStageInstanceId = _CfprSysfileMutationFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 1),
    _CfprSysfileMutationFsmStageInstanceId_Type()
)
cfprSysfileMutationFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageInstanceId.setStatus("current")
_CfprSysfileMutationFsmStageDn_Type = CfprManagedObjectDn
_CfprSysfileMutationFsmStageDn_Object = MibTableColumn
cfprSysfileMutationFsmStageDn = _CfprSysfileMutationFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 2),
    _CfprSysfileMutationFsmStageDn_Type()
)
cfprSysfileMutationFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageDn.setStatus("current")
_CfprSysfileMutationFsmStageRn_Type = SnmpAdminString
_CfprSysfileMutationFsmStageRn_Object = MibTableColumn
cfprSysfileMutationFsmStageRn = _CfprSysfileMutationFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 3),
    _CfprSysfileMutationFsmStageRn_Type()
)
cfprSysfileMutationFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageRn.setStatus("current")
_CfprSysfileMutationFsmStageDescrData_Type = SnmpAdminString
_CfprSysfileMutationFsmStageDescrData_Object = MibTableColumn
cfprSysfileMutationFsmStageDescrData = _CfprSysfileMutationFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 4),
    _CfprSysfileMutationFsmStageDescrData_Type()
)
cfprSysfileMutationFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageDescrData.setStatus("current")
_CfprSysfileMutationFsmStageLastUpdateTime_Type = DateAndTime
_CfprSysfileMutationFsmStageLastUpdateTime_Object = MibTableColumn
cfprSysfileMutationFsmStageLastUpdateTime = _CfprSysfileMutationFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 5),
    _CfprSysfileMutationFsmStageLastUpdateTime_Type()
)
cfprSysfileMutationFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageLastUpdateTime.setStatus("current")
_CfprSysfileMutationFsmStageName_Type = CfprSysfileMutationFsmStageName
_CfprSysfileMutationFsmStageName_Object = MibTableColumn
cfprSysfileMutationFsmStageName = _CfprSysfileMutationFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 6),
    _CfprSysfileMutationFsmStageName_Type()
)
cfprSysfileMutationFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageName.setStatus("current")
_CfprSysfileMutationFsmStageOrder_Type = Gauge32
_CfprSysfileMutationFsmStageOrder_Object = MibTableColumn
cfprSysfileMutationFsmStageOrder = _CfprSysfileMutationFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 7),
    _CfprSysfileMutationFsmStageOrder_Type()
)
cfprSysfileMutationFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageOrder.setStatus("current")
_CfprSysfileMutationFsmStageRetry_Type = Gauge32
_CfprSysfileMutationFsmStageRetry_Object = MibTableColumn
cfprSysfileMutationFsmStageRetry = _CfprSysfileMutationFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 8),
    _CfprSysfileMutationFsmStageRetry_Type()
)
cfprSysfileMutationFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageRetry.setStatus("current")
_CfprSysfileMutationFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSysfileMutationFsmStageStageStatus_Object = MibTableColumn
cfprSysfileMutationFsmStageStageStatus = _CfprSysfileMutationFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 4, 1, 9),
    _CfprSysfileMutationFsmStageStageStatus_Type()
)
cfprSysfileMutationFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmStageStageStatus.setStatus("current")
_CfprSysfileMutationFsmTaskTable_Object = MibTable
cfprSysfileMutationFsmTaskTable = _CfprSysfileMutationFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5)
)
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskTable.setStatus("current")
_CfprSysfileMutationFsmTaskEntry_Object = MibTableRow
cfprSysfileMutationFsmTaskEntry = _CfprSysfileMutationFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1)
)
cfprSysfileMutationFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SYSFILE-MIB", "cfprSysfileMutationFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskEntry.setStatus("current")
_CfprSysfileMutationFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSysfileMutationFsmTaskInstanceId_Object = MibTableColumn
cfprSysfileMutationFsmTaskInstanceId = _CfprSysfileMutationFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 1),
    _CfprSysfileMutationFsmTaskInstanceId_Type()
)
cfprSysfileMutationFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskInstanceId.setStatus("current")
_CfprSysfileMutationFsmTaskDn_Type = CfprManagedObjectDn
_CfprSysfileMutationFsmTaskDn_Object = MibTableColumn
cfprSysfileMutationFsmTaskDn = _CfprSysfileMutationFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 2),
    _CfprSysfileMutationFsmTaskDn_Type()
)
cfprSysfileMutationFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskDn.setStatus("current")
_CfprSysfileMutationFsmTaskRn_Type = SnmpAdminString
_CfprSysfileMutationFsmTaskRn_Object = MibTableColumn
cfprSysfileMutationFsmTaskRn = _CfprSysfileMutationFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 3),
    _CfprSysfileMutationFsmTaskRn_Type()
)
cfprSysfileMutationFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskRn.setStatus("current")
_CfprSysfileMutationFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSysfileMutationFsmTaskCompletion_Object = MibTableColumn
cfprSysfileMutationFsmTaskCompletion = _CfprSysfileMutationFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 4),
    _CfprSysfileMutationFsmTaskCompletion_Type()
)
cfprSysfileMutationFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskCompletion.setStatus("current")
_CfprSysfileMutationFsmTaskFlags_Type = CfprFsmFlags
_CfprSysfileMutationFsmTaskFlags_Object = MibTableColumn
cfprSysfileMutationFsmTaskFlags = _CfprSysfileMutationFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 5),
    _CfprSysfileMutationFsmTaskFlags_Type()
)
cfprSysfileMutationFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskFlags.setStatus("current")
_CfprSysfileMutationFsmTaskItem_Type = CfprSysfileMutationFsmTaskItem
_CfprSysfileMutationFsmTaskItem_Object = MibTableColumn
cfprSysfileMutationFsmTaskItem = _CfprSysfileMutationFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 6),
    _CfprSysfileMutationFsmTaskItem_Type()
)
cfprSysfileMutationFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskItem.setStatus("current")
_CfprSysfileMutationFsmTaskSeqId_Type = Gauge32
_CfprSysfileMutationFsmTaskSeqId_Object = MibTableColumn
cfprSysfileMutationFsmTaskSeqId = _CfprSysfileMutationFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 77, 5, 1, 7),
    _CfprSysfileMutationFsmTaskSeqId_Type()
)
cfprSysfileMutationFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSysfileMutationFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-SYSFILE-MIB",
    **{"cfprSysfileObjects": cfprSysfileObjects,
       "cfprSysfileDigestTable": cfprSysfileDigestTable,
       "cfprSysfileDigestEntry": cfprSysfileDigestEntry,
       "cfprSysfileDigestInstanceId": cfprSysfileDigestInstanceId,
       "cfprSysfileDigestDn": cfprSysfileDigestDn,
       "cfprSysfileDigestRn": cfprSysfileDigestRn,
       "cfprSysfileDigestCreationTS": cfprSysfileDigestCreationTS,
       "cfprSysfileDigestDescr": cfprSysfileDigestDescr,
       "cfprSysfileDigestName": cfprSysfileDigestName,
       "cfprSysfileDigestSize": cfprSysfileDigestSize,
       "cfprSysfileDigestSource": cfprSysfileDigestSource,
       "cfprSysfileDigestSwitchId": cfprSysfileDigestSwitchId,
       "cfprSysfileDigestTs": cfprSysfileDigestTs,
       "cfprSysfileDigestUri": cfprSysfileDigestUri,
       "cfprSysfileMutationTable": cfprSysfileMutationTable,
       "cfprSysfileMutationEntry": cfprSysfileMutationEntry,
       "cfprSysfileMutationInstanceId": cfprSysfileMutationInstanceId,
       "cfprSysfileMutationDn": cfprSysfileMutationDn,
       "cfprSysfileMutationRn": cfprSysfileMutationRn,
       "cfprSysfileMutationAction": cfprSysfileMutationAction,
       "cfprSysfileMutationDescr": cfprSysfileMutationDescr,
       "cfprSysfileMutationFsmDescr": cfprSysfileMutationFsmDescr,
       "cfprSysfileMutationFsmPrev": cfprSysfileMutationFsmPrev,
       "cfprSysfileMutationFsmProgr": cfprSysfileMutationFsmProgr,
       "cfprSysfileMutationFsmRmtInvErrCode": cfprSysfileMutationFsmRmtInvErrCode,
       "cfprSysfileMutationFsmRmtInvErrDescr": cfprSysfileMutationFsmRmtInvErrDescr,
       "cfprSysfileMutationFsmRmtInvRslt": cfprSysfileMutationFsmRmtInvRslt,
       "cfprSysfileMutationFsmStageDescr": cfprSysfileMutationFsmStageDescr,
       "cfprSysfileMutationFsmStamp": cfprSysfileMutationFsmStamp,
       "cfprSysfileMutationFsmStatus": cfprSysfileMutationFsmStatus,
       "cfprSysfileMutationFsmTry": cfprSysfileMutationFsmTry,
       "cfprSysfileMutationFsmTable": cfprSysfileMutationFsmTable,
       "cfprSysfileMutationFsmEntry": cfprSysfileMutationFsmEntry,
       "cfprSysfileMutationFsmInstanceId": cfprSysfileMutationFsmInstanceId,
       "cfprSysfileMutationFsmDn": cfprSysfileMutationFsmDn,
       "cfprSysfileMutationFsmRn": cfprSysfileMutationFsmRn,
       "cfprSysfileMutationFsmCompletionTime": cfprSysfileMutationFsmCompletionTime,
       "cfprSysfileMutationFsmCurrentFsm": cfprSysfileMutationFsmCurrentFsm,
       "cfprSysfileMutationFsmDescrData": cfprSysfileMutationFsmDescrData,
       "cfprSysfileMutationFsmFsmStatus": cfprSysfileMutationFsmFsmStatus,
       "cfprSysfileMutationFsmProgress": cfprSysfileMutationFsmProgress,
       "cfprSysfileMutationFsmRmtErrCode": cfprSysfileMutationFsmRmtErrCode,
       "cfprSysfileMutationFsmRmtErrDescr": cfprSysfileMutationFsmRmtErrDescr,
       "cfprSysfileMutationFsmRmtRslt": cfprSysfileMutationFsmRmtRslt,
       "cfprSysfileMutationFsmStageTable": cfprSysfileMutationFsmStageTable,
       "cfprSysfileMutationFsmStageEntry": cfprSysfileMutationFsmStageEntry,
       "cfprSysfileMutationFsmStageInstanceId": cfprSysfileMutationFsmStageInstanceId,
       "cfprSysfileMutationFsmStageDn": cfprSysfileMutationFsmStageDn,
       "cfprSysfileMutationFsmStageRn": cfprSysfileMutationFsmStageRn,
       "cfprSysfileMutationFsmStageDescrData": cfprSysfileMutationFsmStageDescrData,
       "cfprSysfileMutationFsmStageLastUpdateTime": cfprSysfileMutationFsmStageLastUpdateTime,
       "cfprSysfileMutationFsmStageName": cfprSysfileMutationFsmStageName,
       "cfprSysfileMutationFsmStageOrder": cfprSysfileMutationFsmStageOrder,
       "cfprSysfileMutationFsmStageRetry": cfprSysfileMutationFsmStageRetry,
       "cfprSysfileMutationFsmStageStageStatus": cfprSysfileMutationFsmStageStageStatus,
       "cfprSysfileMutationFsmTaskTable": cfprSysfileMutationFsmTaskTable,
       "cfprSysfileMutationFsmTaskEntry": cfprSysfileMutationFsmTaskEntry,
       "cfprSysfileMutationFsmTaskInstanceId": cfprSysfileMutationFsmTaskInstanceId,
       "cfprSysfileMutationFsmTaskDn": cfprSysfileMutationFsmTaskDn,
       "cfprSysfileMutationFsmTaskRn": cfprSysfileMutationFsmTaskRn,
       "cfprSysfileMutationFsmTaskCompletion": cfprSysfileMutationFsmTaskCompletion,
       "cfprSysfileMutationFsmTaskFlags": cfprSysfileMutationFsmTaskFlags,
       "cfprSysfileMutationFsmTaskItem": cfprSysfileMutationFsmTaskItem,
       "cfprSysfileMutationFsmTaskSeqId": cfprSysfileMutationFsmTaskSeqId}
)
