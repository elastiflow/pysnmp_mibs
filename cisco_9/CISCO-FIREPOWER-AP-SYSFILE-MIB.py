# SNMP MIB module (CISCO-FIREPOWER-AP-SYSFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-SYSFILE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:39 2025
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
 CfprApNetworkSwitchId,
 CfprApSysfileMutationAction,
 CfprApSysfileMutationFsmCurrentFsm,
 CfprApSysfileMutationFsmStageName,
 CfprApSysfileMutationFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApNetworkSwitchId",
    "CfprApSysfileMutationAction",
    "CfprApSysfileMutationFsmCurrentFsm",
    "CfprApSysfileMutationFsmStageName",
    "CfprApSysfileMutationFsmTaskItem")

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

cfprApSysfileObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApSysfileDigestTable_Object = MibTable
cfprApSysfileDigestTable = _CfprApSysfileDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1)
)
if mibBuilder.loadTexts:
    cfprApSysfileDigestTable.setStatus("current")
_CfprApSysfileDigestEntry_Object = MibTableRow
cfprApSysfileDigestEntry = _CfprApSysfileDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1)
)
cfprApSysfileDigestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSFILE-MIB", "cfprApSysfileDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysfileDigestEntry.setStatus("current")
_CfprApSysfileDigestInstanceId_Type = CfprApManagedObjectId
_CfprApSysfileDigestInstanceId_Object = MibTableColumn
cfprApSysfileDigestInstanceId = _CfprApSysfileDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 1),
    _CfprApSysfileDigestInstanceId_Type()
)
cfprApSysfileDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysfileDigestInstanceId.setStatus("current")
_CfprApSysfileDigestDn_Type = CfprApManagedObjectDn
_CfprApSysfileDigestDn_Object = MibTableColumn
cfprApSysfileDigestDn = _CfprApSysfileDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 2),
    _CfprApSysfileDigestDn_Type()
)
cfprApSysfileDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestDn.setStatus("current")
_CfprApSysfileDigestRn_Type = SnmpAdminString
_CfprApSysfileDigestRn_Object = MibTableColumn
cfprApSysfileDigestRn = _CfprApSysfileDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 3),
    _CfprApSysfileDigestRn_Type()
)
cfprApSysfileDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestRn.setStatus("current")
_CfprApSysfileDigestCreationTS_Type = Unsigned64
_CfprApSysfileDigestCreationTS_Object = MibTableColumn
cfprApSysfileDigestCreationTS = _CfprApSysfileDigestCreationTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 4),
    _CfprApSysfileDigestCreationTS_Type()
)
cfprApSysfileDigestCreationTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestCreationTS.setStatus("current")
_CfprApSysfileDigestDescr_Type = SnmpAdminString
_CfprApSysfileDigestDescr_Object = MibTableColumn
cfprApSysfileDigestDescr = _CfprApSysfileDigestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 5),
    _CfprApSysfileDigestDescr_Type()
)
cfprApSysfileDigestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestDescr.setStatus("current")
_CfprApSysfileDigestName_Type = SnmpAdminString
_CfprApSysfileDigestName_Object = MibTableColumn
cfprApSysfileDigestName = _CfprApSysfileDigestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 6),
    _CfprApSysfileDigestName_Type()
)
cfprApSysfileDigestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestName.setStatus("current")
_CfprApSysfileDigestSize_Type = Gauge32
_CfprApSysfileDigestSize_Object = MibTableColumn
cfprApSysfileDigestSize = _CfprApSysfileDigestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 7),
    _CfprApSysfileDigestSize_Type()
)
cfprApSysfileDigestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestSize.setStatus("current")
_CfprApSysfileDigestSource_Type = SnmpAdminString
_CfprApSysfileDigestSource_Object = MibTableColumn
cfprApSysfileDigestSource = _CfprApSysfileDigestSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 8),
    _CfprApSysfileDigestSource_Type()
)
cfprApSysfileDigestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestSource.setStatus("current")
_CfprApSysfileDigestSwitchId_Type = CfprApNetworkSwitchId
_CfprApSysfileDigestSwitchId_Object = MibTableColumn
cfprApSysfileDigestSwitchId = _CfprApSysfileDigestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 9),
    _CfprApSysfileDigestSwitchId_Type()
)
cfprApSysfileDigestSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestSwitchId.setStatus("current")
_CfprApSysfileDigestTs_Type = DateAndTime
_CfprApSysfileDigestTs_Object = MibTableColumn
cfprApSysfileDigestTs = _CfprApSysfileDigestTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 10),
    _CfprApSysfileDigestTs_Type()
)
cfprApSysfileDigestTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestTs.setStatus("current")
_CfprApSysfileDigestUri_Type = SnmpAdminString
_CfprApSysfileDigestUri_Object = MibTableColumn
cfprApSysfileDigestUri = _CfprApSysfileDigestUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 1, 1, 11),
    _CfprApSysfileDigestUri_Type()
)
cfprApSysfileDigestUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileDigestUri.setStatus("current")
_CfprApSysfileMutationTable_Object = MibTable
cfprApSysfileMutationTable = _CfprApSysfileMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2)
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationTable.setStatus("current")
_CfprApSysfileMutationEntry_Object = MibTableRow
cfprApSysfileMutationEntry = _CfprApSysfileMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1)
)
cfprApSysfileMutationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSFILE-MIB", "cfprApSysfileMutationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationEntry.setStatus("current")
_CfprApSysfileMutationInstanceId_Type = CfprApManagedObjectId
_CfprApSysfileMutationInstanceId_Object = MibTableColumn
cfprApSysfileMutationInstanceId = _CfprApSysfileMutationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 1),
    _CfprApSysfileMutationInstanceId_Type()
)
cfprApSysfileMutationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysfileMutationInstanceId.setStatus("current")
_CfprApSysfileMutationDn_Type = CfprApManagedObjectDn
_CfprApSysfileMutationDn_Object = MibTableColumn
cfprApSysfileMutationDn = _CfprApSysfileMutationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 2),
    _CfprApSysfileMutationDn_Type()
)
cfprApSysfileMutationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationDn.setStatus("current")
_CfprApSysfileMutationRn_Type = SnmpAdminString
_CfprApSysfileMutationRn_Object = MibTableColumn
cfprApSysfileMutationRn = _CfprApSysfileMutationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 3),
    _CfprApSysfileMutationRn_Type()
)
cfprApSysfileMutationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationRn.setStatus("current")
_CfprApSysfileMutationAction_Type = CfprApSysfileMutationAction
_CfprApSysfileMutationAction_Object = MibTableColumn
cfprApSysfileMutationAction = _CfprApSysfileMutationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 4),
    _CfprApSysfileMutationAction_Type()
)
cfprApSysfileMutationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationAction.setStatus("current")
_CfprApSysfileMutationDescr_Type = SnmpAdminString
_CfprApSysfileMutationDescr_Object = MibTableColumn
cfprApSysfileMutationDescr = _CfprApSysfileMutationDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 5),
    _CfprApSysfileMutationDescr_Type()
)
cfprApSysfileMutationDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationDescr.setStatus("current")
_CfprApSysfileMutationFsmDescr_Type = SnmpAdminString
_CfprApSysfileMutationFsmDescr_Object = MibTableColumn
cfprApSysfileMutationFsmDescr = _CfprApSysfileMutationFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 6),
    _CfprApSysfileMutationFsmDescr_Type()
)
cfprApSysfileMutationFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmDescr.setStatus("current")
_CfprApSysfileMutationFsmPrev_Type = SnmpAdminString
_CfprApSysfileMutationFsmPrev_Object = MibTableColumn
cfprApSysfileMutationFsmPrev = _CfprApSysfileMutationFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 7),
    _CfprApSysfileMutationFsmPrev_Type()
)
cfprApSysfileMutationFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmPrev.setStatus("current")
_CfprApSysfileMutationFsmProgr_Type = Gauge32
_CfprApSysfileMutationFsmProgr_Object = MibTableColumn
cfprApSysfileMutationFsmProgr = _CfprApSysfileMutationFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 8),
    _CfprApSysfileMutationFsmProgr_Type()
)
cfprApSysfileMutationFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmProgr.setStatus("current")
_CfprApSysfileMutationFsmRmtInvErrCode_Type = Gauge32
_CfprApSysfileMutationFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysfileMutationFsmRmtInvErrCode = _CfprApSysfileMutationFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 9),
    _CfprApSysfileMutationFsmRmtInvErrCode_Type()
)
cfprApSysfileMutationFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRmtInvErrCode.setStatus("current")
_CfprApSysfileMutationFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysfileMutationFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysfileMutationFsmRmtInvErrDescr = _CfprApSysfileMutationFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 10),
    _CfprApSysfileMutationFsmRmtInvErrDescr_Type()
)
cfprApSysfileMutationFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRmtInvErrDescr.setStatus("current")
_CfprApSysfileMutationFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysfileMutationFsmRmtInvRslt_Object = MibTableColumn
cfprApSysfileMutationFsmRmtInvRslt = _CfprApSysfileMutationFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 11),
    _CfprApSysfileMutationFsmRmtInvRslt_Type()
)
cfprApSysfileMutationFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRmtInvRslt.setStatus("current")
_CfprApSysfileMutationFsmStageDescr_Type = SnmpAdminString
_CfprApSysfileMutationFsmStageDescr_Object = MibTableColumn
cfprApSysfileMutationFsmStageDescr = _CfprApSysfileMutationFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 12),
    _CfprApSysfileMutationFsmStageDescr_Type()
)
cfprApSysfileMutationFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageDescr.setStatus("current")
_CfprApSysfileMutationFsmStamp_Type = DateAndTime
_CfprApSysfileMutationFsmStamp_Object = MibTableColumn
cfprApSysfileMutationFsmStamp = _CfprApSysfileMutationFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 13),
    _CfprApSysfileMutationFsmStamp_Type()
)
cfprApSysfileMutationFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStamp.setStatus("current")
_CfprApSysfileMutationFsmStatus_Type = SnmpAdminString
_CfprApSysfileMutationFsmStatus_Object = MibTableColumn
cfprApSysfileMutationFsmStatus = _CfprApSysfileMutationFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 14),
    _CfprApSysfileMutationFsmStatus_Type()
)
cfprApSysfileMutationFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStatus.setStatus("current")
_CfprApSysfileMutationFsmTry_Type = Gauge32
_CfprApSysfileMutationFsmTry_Object = MibTableColumn
cfprApSysfileMutationFsmTry = _CfprApSysfileMutationFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 2, 1, 15),
    _CfprApSysfileMutationFsmTry_Type()
)
cfprApSysfileMutationFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTry.setStatus("current")
_CfprApSysfileMutationFsmTable_Object = MibTable
cfprApSysfileMutationFsmTable = _CfprApSysfileMutationFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3)
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTable.setStatus("current")
_CfprApSysfileMutationFsmEntry_Object = MibTableRow
cfprApSysfileMutationFsmEntry = _CfprApSysfileMutationFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1)
)
cfprApSysfileMutationFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSFILE-MIB", "cfprApSysfileMutationFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmEntry.setStatus("current")
_CfprApSysfileMutationFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysfileMutationFsmInstanceId_Object = MibTableColumn
cfprApSysfileMutationFsmInstanceId = _CfprApSysfileMutationFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 1),
    _CfprApSysfileMutationFsmInstanceId_Type()
)
cfprApSysfileMutationFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmInstanceId.setStatus("current")
_CfprApSysfileMutationFsmDn_Type = CfprApManagedObjectDn
_CfprApSysfileMutationFsmDn_Object = MibTableColumn
cfprApSysfileMutationFsmDn = _CfprApSysfileMutationFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 2),
    _CfprApSysfileMutationFsmDn_Type()
)
cfprApSysfileMutationFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmDn.setStatus("current")
_CfprApSysfileMutationFsmRn_Type = SnmpAdminString
_CfprApSysfileMutationFsmRn_Object = MibTableColumn
cfprApSysfileMutationFsmRn = _CfprApSysfileMutationFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 3),
    _CfprApSysfileMutationFsmRn_Type()
)
cfprApSysfileMutationFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRn.setStatus("current")
_CfprApSysfileMutationFsmCompletionTime_Type = DateAndTime
_CfprApSysfileMutationFsmCompletionTime_Object = MibTableColumn
cfprApSysfileMutationFsmCompletionTime = _CfprApSysfileMutationFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 4),
    _CfprApSysfileMutationFsmCompletionTime_Type()
)
cfprApSysfileMutationFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmCompletionTime.setStatus("current")
_CfprApSysfileMutationFsmCurrentFsm_Type = CfprApSysfileMutationFsmCurrentFsm
_CfprApSysfileMutationFsmCurrentFsm_Object = MibTableColumn
cfprApSysfileMutationFsmCurrentFsm = _CfprApSysfileMutationFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 5),
    _CfprApSysfileMutationFsmCurrentFsm_Type()
)
cfprApSysfileMutationFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmCurrentFsm.setStatus("current")
_CfprApSysfileMutationFsmDescrData_Type = SnmpAdminString
_CfprApSysfileMutationFsmDescrData_Object = MibTableColumn
cfprApSysfileMutationFsmDescrData = _CfprApSysfileMutationFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 6),
    _CfprApSysfileMutationFsmDescrData_Type()
)
cfprApSysfileMutationFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmDescrData.setStatus("current")
_CfprApSysfileMutationFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysfileMutationFsmFsmStatus_Object = MibTableColumn
cfprApSysfileMutationFsmFsmStatus = _CfprApSysfileMutationFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 7),
    _CfprApSysfileMutationFsmFsmStatus_Type()
)
cfprApSysfileMutationFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmFsmStatus.setStatus("current")
_CfprApSysfileMutationFsmProgress_Type = Gauge32
_CfprApSysfileMutationFsmProgress_Object = MibTableColumn
cfprApSysfileMutationFsmProgress = _CfprApSysfileMutationFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 8),
    _CfprApSysfileMutationFsmProgress_Type()
)
cfprApSysfileMutationFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmProgress.setStatus("current")
_CfprApSysfileMutationFsmRmtErrCode_Type = Gauge32
_CfprApSysfileMutationFsmRmtErrCode_Object = MibTableColumn
cfprApSysfileMutationFsmRmtErrCode = _CfprApSysfileMutationFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 9),
    _CfprApSysfileMutationFsmRmtErrCode_Type()
)
cfprApSysfileMutationFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRmtErrCode.setStatus("current")
_CfprApSysfileMutationFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysfileMutationFsmRmtErrDescr_Object = MibTableColumn
cfprApSysfileMutationFsmRmtErrDescr = _CfprApSysfileMutationFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 10),
    _CfprApSysfileMutationFsmRmtErrDescr_Type()
)
cfprApSysfileMutationFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRmtErrDescr.setStatus("current")
_CfprApSysfileMutationFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysfileMutationFsmRmtRslt_Object = MibTableColumn
cfprApSysfileMutationFsmRmtRslt = _CfprApSysfileMutationFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 3, 1, 11),
    _CfprApSysfileMutationFsmRmtRslt_Type()
)
cfprApSysfileMutationFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmRmtRslt.setStatus("current")
_CfprApSysfileMutationFsmStageTable_Object = MibTable
cfprApSysfileMutationFsmStageTable = _CfprApSysfileMutationFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4)
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageTable.setStatus("current")
_CfprApSysfileMutationFsmStageEntry_Object = MibTableRow
cfprApSysfileMutationFsmStageEntry = _CfprApSysfileMutationFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1)
)
cfprApSysfileMutationFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSFILE-MIB", "cfprApSysfileMutationFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageEntry.setStatus("current")
_CfprApSysfileMutationFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysfileMutationFsmStageInstanceId_Object = MibTableColumn
cfprApSysfileMutationFsmStageInstanceId = _CfprApSysfileMutationFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 1),
    _CfprApSysfileMutationFsmStageInstanceId_Type()
)
cfprApSysfileMutationFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageInstanceId.setStatus("current")
_CfprApSysfileMutationFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysfileMutationFsmStageDn_Object = MibTableColumn
cfprApSysfileMutationFsmStageDn = _CfprApSysfileMutationFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 2),
    _CfprApSysfileMutationFsmStageDn_Type()
)
cfprApSysfileMutationFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageDn.setStatus("current")
_CfprApSysfileMutationFsmStageRn_Type = SnmpAdminString
_CfprApSysfileMutationFsmStageRn_Object = MibTableColumn
cfprApSysfileMutationFsmStageRn = _CfprApSysfileMutationFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 3),
    _CfprApSysfileMutationFsmStageRn_Type()
)
cfprApSysfileMutationFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageRn.setStatus("current")
_CfprApSysfileMutationFsmStageDescrData_Type = SnmpAdminString
_CfprApSysfileMutationFsmStageDescrData_Object = MibTableColumn
cfprApSysfileMutationFsmStageDescrData = _CfprApSysfileMutationFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 4),
    _CfprApSysfileMutationFsmStageDescrData_Type()
)
cfprApSysfileMutationFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageDescrData.setStatus("current")
_CfprApSysfileMutationFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysfileMutationFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysfileMutationFsmStageLastUpdateTime = _CfprApSysfileMutationFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 5),
    _CfprApSysfileMutationFsmStageLastUpdateTime_Type()
)
cfprApSysfileMutationFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageLastUpdateTime.setStatus("current")
_CfprApSysfileMutationFsmStageName_Type = CfprApSysfileMutationFsmStageName
_CfprApSysfileMutationFsmStageName_Object = MibTableColumn
cfprApSysfileMutationFsmStageName = _CfprApSysfileMutationFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 6),
    _CfprApSysfileMutationFsmStageName_Type()
)
cfprApSysfileMutationFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageName.setStatus("current")
_CfprApSysfileMutationFsmStageOrder_Type = Gauge32
_CfprApSysfileMutationFsmStageOrder_Object = MibTableColumn
cfprApSysfileMutationFsmStageOrder = _CfprApSysfileMutationFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 7),
    _CfprApSysfileMutationFsmStageOrder_Type()
)
cfprApSysfileMutationFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageOrder.setStatus("current")
_CfprApSysfileMutationFsmStageRetry_Type = Gauge32
_CfprApSysfileMutationFsmStageRetry_Object = MibTableColumn
cfprApSysfileMutationFsmStageRetry = _CfprApSysfileMutationFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 8),
    _CfprApSysfileMutationFsmStageRetry_Type()
)
cfprApSysfileMutationFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageRetry.setStatus("current")
_CfprApSysfileMutationFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysfileMutationFsmStageStageStatus_Object = MibTableColumn
cfprApSysfileMutationFsmStageStageStatus = _CfprApSysfileMutationFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 4, 1, 9),
    _CfprApSysfileMutationFsmStageStageStatus_Type()
)
cfprApSysfileMutationFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmStageStageStatus.setStatus("current")
_CfprApSysfileMutationFsmTaskTable_Object = MibTable
cfprApSysfileMutationFsmTaskTable = _CfprApSysfileMutationFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5)
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskTable.setStatus("current")
_CfprApSysfileMutationFsmTaskEntry_Object = MibTableRow
cfprApSysfileMutationFsmTaskEntry = _CfprApSysfileMutationFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1)
)
cfprApSysfileMutationFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSFILE-MIB", "cfprApSysfileMutationFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskEntry.setStatus("current")
_CfprApSysfileMutationFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysfileMutationFsmTaskInstanceId_Object = MibTableColumn
cfprApSysfileMutationFsmTaskInstanceId = _CfprApSysfileMutationFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 1),
    _CfprApSysfileMutationFsmTaskInstanceId_Type()
)
cfprApSysfileMutationFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskInstanceId.setStatus("current")
_CfprApSysfileMutationFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysfileMutationFsmTaskDn_Object = MibTableColumn
cfprApSysfileMutationFsmTaskDn = _CfprApSysfileMutationFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 2),
    _CfprApSysfileMutationFsmTaskDn_Type()
)
cfprApSysfileMutationFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskDn.setStatus("current")
_CfprApSysfileMutationFsmTaskRn_Type = SnmpAdminString
_CfprApSysfileMutationFsmTaskRn_Object = MibTableColumn
cfprApSysfileMutationFsmTaskRn = _CfprApSysfileMutationFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 3),
    _CfprApSysfileMutationFsmTaskRn_Type()
)
cfprApSysfileMutationFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskRn.setStatus("current")
_CfprApSysfileMutationFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysfileMutationFsmTaskCompletion_Object = MibTableColumn
cfprApSysfileMutationFsmTaskCompletion = _CfprApSysfileMutationFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 4),
    _CfprApSysfileMutationFsmTaskCompletion_Type()
)
cfprApSysfileMutationFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskCompletion.setStatus("current")
_CfprApSysfileMutationFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysfileMutationFsmTaskFlags_Object = MibTableColumn
cfprApSysfileMutationFsmTaskFlags = _CfprApSysfileMutationFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 5),
    _CfprApSysfileMutationFsmTaskFlags_Type()
)
cfprApSysfileMutationFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskFlags.setStatus("current")
_CfprApSysfileMutationFsmTaskItem_Type = CfprApSysfileMutationFsmTaskItem
_CfprApSysfileMutationFsmTaskItem_Object = MibTableColumn
cfprApSysfileMutationFsmTaskItem = _CfprApSysfileMutationFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 6),
    _CfprApSysfileMutationFsmTaskItem_Type()
)
cfprApSysfileMutationFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskItem.setStatus("current")
_CfprApSysfileMutationFsmTaskSeqId_Type = Gauge32
_CfprApSysfileMutationFsmTaskSeqId_Object = MibTableColumn
cfprApSysfileMutationFsmTaskSeqId = _CfprApSysfileMutationFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 77, 5, 1, 7),
    _CfprApSysfileMutationFsmTaskSeqId_Type()
)
cfprApSysfileMutationFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysfileMutationFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-SYSFILE-MIB",
    **{"cfprApSysfileObjects": cfprApSysfileObjects,
       "cfprApSysfileDigestTable": cfprApSysfileDigestTable,
       "cfprApSysfileDigestEntry": cfprApSysfileDigestEntry,
       "cfprApSysfileDigestInstanceId": cfprApSysfileDigestInstanceId,
       "cfprApSysfileDigestDn": cfprApSysfileDigestDn,
       "cfprApSysfileDigestRn": cfprApSysfileDigestRn,
       "cfprApSysfileDigestCreationTS": cfprApSysfileDigestCreationTS,
       "cfprApSysfileDigestDescr": cfprApSysfileDigestDescr,
       "cfprApSysfileDigestName": cfprApSysfileDigestName,
       "cfprApSysfileDigestSize": cfprApSysfileDigestSize,
       "cfprApSysfileDigestSource": cfprApSysfileDigestSource,
       "cfprApSysfileDigestSwitchId": cfprApSysfileDigestSwitchId,
       "cfprApSysfileDigestTs": cfprApSysfileDigestTs,
       "cfprApSysfileDigestUri": cfprApSysfileDigestUri,
       "cfprApSysfileMutationTable": cfprApSysfileMutationTable,
       "cfprApSysfileMutationEntry": cfprApSysfileMutationEntry,
       "cfprApSysfileMutationInstanceId": cfprApSysfileMutationInstanceId,
       "cfprApSysfileMutationDn": cfprApSysfileMutationDn,
       "cfprApSysfileMutationRn": cfprApSysfileMutationRn,
       "cfprApSysfileMutationAction": cfprApSysfileMutationAction,
       "cfprApSysfileMutationDescr": cfprApSysfileMutationDescr,
       "cfprApSysfileMutationFsmDescr": cfprApSysfileMutationFsmDescr,
       "cfprApSysfileMutationFsmPrev": cfprApSysfileMutationFsmPrev,
       "cfprApSysfileMutationFsmProgr": cfprApSysfileMutationFsmProgr,
       "cfprApSysfileMutationFsmRmtInvErrCode": cfprApSysfileMutationFsmRmtInvErrCode,
       "cfprApSysfileMutationFsmRmtInvErrDescr": cfprApSysfileMutationFsmRmtInvErrDescr,
       "cfprApSysfileMutationFsmRmtInvRslt": cfprApSysfileMutationFsmRmtInvRslt,
       "cfprApSysfileMutationFsmStageDescr": cfprApSysfileMutationFsmStageDescr,
       "cfprApSysfileMutationFsmStamp": cfprApSysfileMutationFsmStamp,
       "cfprApSysfileMutationFsmStatus": cfprApSysfileMutationFsmStatus,
       "cfprApSysfileMutationFsmTry": cfprApSysfileMutationFsmTry,
       "cfprApSysfileMutationFsmTable": cfprApSysfileMutationFsmTable,
       "cfprApSysfileMutationFsmEntry": cfprApSysfileMutationFsmEntry,
       "cfprApSysfileMutationFsmInstanceId": cfprApSysfileMutationFsmInstanceId,
       "cfprApSysfileMutationFsmDn": cfprApSysfileMutationFsmDn,
       "cfprApSysfileMutationFsmRn": cfprApSysfileMutationFsmRn,
       "cfprApSysfileMutationFsmCompletionTime": cfprApSysfileMutationFsmCompletionTime,
       "cfprApSysfileMutationFsmCurrentFsm": cfprApSysfileMutationFsmCurrentFsm,
       "cfprApSysfileMutationFsmDescrData": cfprApSysfileMutationFsmDescrData,
       "cfprApSysfileMutationFsmFsmStatus": cfprApSysfileMutationFsmFsmStatus,
       "cfprApSysfileMutationFsmProgress": cfprApSysfileMutationFsmProgress,
       "cfprApSysfileMutationFsmRmtErrCode": cfprApSysfileMutationFsmRmtErrCode,
       "cfprApSysfileMutationFsmRmtErrDescr": cfprApSysfileMutationFsmRmtErrDescr,
       "cfprApSysfileMutationFsmRmtRslt": cfprApSysfileMutationFsmRmtRslt,
       "cfprApSysfileMutationFsmStageTable": cfprApSysfileMutationFsmStageTable,
       "cfprApSysfileMutationFsmStageEntry": cfprApSysfileMutationFsmStageEntry,
       "cfprApSysfileMutationFsmStageInstanceId": cfprApSysfileMutationFsmStageInstanceId,
       "cfprApSysfileMutationFsmStageDn": cfprApSysfileMutationFsmStageDn,
       "cfprApSysfileMutationFsmStageRn": cfprApSysfileMutationFsmStageRn,
       "cfprApSysfileMutationFsmStageDescrData": cfprApSysfileMutationFsmStageDescrData,
       "cfprApSysfileMutationFsmStageLastUpdateTime": cfprApSysfileMutationFsmStageLastUpdateTime,
       "cfprApSysfileMutationFsmStageName": cfprApSysfileMutationFsmStageName,
       "cfprApSysfileMutationFsmStageOrder": cfprApSysfileMutationFsmStageOrder,
       "cfprApSysfileMutationFsmStageRetry": cfprApSysfileMutationFsmStageRetry,
       "cfprApSysfileMutationFsmStageStageStatus": cfprApSysfileMutationFsmStageStageStatus,
       "cfprApSysfileMutationFsmTaskTable": cfprApSysfileMutationFsmTaskTable,
       "cfprApSysfileMutationFsmTaskEntry": cfprApSysfileMutationFsmTaskEntry,
       "cfprApSysfileMutationFsmTaskInstanceId": cfprApSysfileMutationFsmTaskInstanceId,
       "cfprApSysfileMutationFsmTaskDn": cfprApSysfileMutationFsmTaskDn,
       "cfprApSysfileMutationFsmTaskRn": cfprApSysfileMutationFsmTaskRn,
       "cfprApSysfileMutationFsmTaskCompletion": cfprApSysfileMutationFsmTaskCompletion,
       "cfprApSysfileMutationFsmTaskFlags": cfprApSysfileMutationFsmTaskFlags,
       "cfprApSysfileMutationFsmTaskItem": cfprApSysfileMutationFsmTaskItem,
       "cfprApSysfileMutationFsmTaskSeqId": cfprApSysfileMutationFsmTaskSeqId}
)
