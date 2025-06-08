# SNMP MIB module (CISCO-FIREPOWER-OS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-OS-MIB.mib
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
 CfprFsmFsmStageStatus,
 CfprHostagAction,
 CfprHostagAgentType,
 CfprHostagEvent,
 CfprOsBootingUpType,
 CfprOsControllerBootMode,
 CfprOsControllerFormatDisk,
 CfprOsControllerFsmCurrentFsm,
 CfprOsControllerFsmStageName,
 CfprOsControllerFsmTaskFlags,
 CfprOsControllerFsmTaskItem,
 CfprOsDeployState,
 CfprOsInitState,
 CfprOsInstallLicenseState,
 CfprOsOsMode,
 CfprOsOsType,
 CfprOsUpgradeReturnCode,
 CfprOsUpgradeState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFsmStageStatus",
    "CfprHostagAction",
    "CfprHostagAgentType",
    "CfprHostagEvent",
    "CfprOsBootingUpType",
    "CfprOsControllerBootMode",
    "CfprOsControllerFormatDisk",
    "CfprOsControllerFsmCurrentFsm",
    "CfprOsControllerFsmStageName",
    "CfprOsControllerFsmTaskFlags",
    "CfprOsControllerFsmTaskItem",
    "CfprOsDeployState",
    "CfprOsInitState",
    "CfprOsInstallLicenseState",
    "CfprOsOsMode",
    "CfprOsOsType",
    "CfprOsUpgradeReturnCode",
    "CfprOsUpgradeState")

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

cfprOsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprOsAgentTable_Object = MibTable
cfprOsAgentTable = _CfprOsAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1)
)
if mibBuilder.loadTexts:
    cfprOsAgentTable.setStatus("current")
_CfprOsAgentEntry_Object = MibTableRow
cfprOsAgentEntry = _CfprOsAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1)
)
cfprOsAgentEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OS-MIB", "cfprOsAgentInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOsAgentEntry.setStatus("current")
_CfprOsAgentInstanceId_Type = CfprManagedObjectId
_CfprOsAgentInstanceId_Object = MibTableColumn
cfprOsAgentInstanceId = _CfprOsAgentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 1),
    _CfprOsAgentInstanceId_Type()
)
cfprOsAgentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOsAgentInstanceId.setStatus("current")
_CfprOsAgentDn_Type = CfprManagedObjectDn
_CfprOsAgentDn_Object = MibTableColumn
cfprOsAgentDn = _CfprOsAgentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 2),
    _CfprOsAgentDn_Type()
)
cfprOsAgentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentDn.setStatus("current")
_CfprOsAgentRn_Type = SnmpAdminString
_CfprOsAgentRn_Object = MibTableColumn
cfprOsAgentRn = _CfprOsAgentRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 3),
    _CfprOsAgentRn_Type()
)
cfprOsAgentRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentRn.setStatus("current")
_CfprOsAgentLastCmd_Type = CfprHostagAction
_CfprOsAgentLastCmd_Object = MibTableColumn
cfprOsAgentLastCmd = _CfprOsAgentLastCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 4),
    _CfprOsAgentLastCmd_Type()
)
cfprOsAgentLastCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentLastCmd.setStatus("current")
_CfprOsAgentLastEvt_Type = CfprHostagEvent
_CfprOsAgentLastEvt_Object = MibTableColumn
cfprOsAgentLastEvt = _CfprOsAgentLastEvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 5),
    _CfprOsAgentLastEvt_Type()
)
cfprOsAgentLastEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentLastEvt.setStatus("current")
_CfprOsAgentLastEvtTs_Type = DateAndTime
_CfprOsAgentLastEvtTs_Object = MibTableColumn
cfprOsAgentLastEvtTs = _CfprOsAgentLastEvtTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 6),
    _CfprOsAgentLastEvtTs_Type()
)
cfprOsAgentLastEvtTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentLastEvtTs.setStatus("current")
_CfprOsAgentPrevCmd_Type = CfprHostagAction
_CfprOsAgentPrevCmd_Object = MibTableColumn
cfprOsAgentPrevCmd = _CfprOsAgentPrevCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 7),
    _CfprOsAgentPrevCmd_Type()
)
cfprOsAgentPrevCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentPrevCmd.setStatus("current")
_CfprOsAgentPrevEvt_Type = CfprHostagEvent
_CfprOsAgentPrevEvt_Object = MibTableColumn
cfprOsAgentPrevEvt = _CfprOsAgentPrevEvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 8),
    _CfprOsAgentPrevEvt_Type()
)
cfprOsAgentPrevEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentPrevEvt.setStatus("current")
_CfprOsAgentType_Type = CfprHostagAgentType
_CfprOsAgentType_Object = MibTableColumn
cfprOsAgentType = _CfprOsAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 9),
    _CfprOsAgentType_Type()
)
cfprOsAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentType.setStatus("current")
_CfprOsAgentVendor_Type = SnmpAdminString
_CfprOsAgentVendor_Object = MibTableColumn
cfprOsAgentVendor = _CfprOsAgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 10),
    _CfprOsAgentVendor_Type()
)
cfprOsAgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentVendor.setStatus("current")
_CfprOsAgentVersion_Type = SnmpAdminString
_CfprOsAgentVersion_Object = MibTableColumn
cfprOsAgentVersion = _CfprOsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 1, 1, 11),
    _CfprOsAgentVersion_Type()
)
cfprOsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsAgentVersion.setStatus("current")
_CfprOsControllerTable_Object = MibTable
cfprOsControllerTable = _CfprOsControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2)
)
if mibBuilder.loadTexts:
    cfprOsControllerTable.setStatus("current")
_CfprOsControllerEntry_Object = MibTableRow
cfprOsControllerEntry = _CfprOsControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1)
)
cfprOsControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OS-MIB", "cfprOsControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOsControllerEntry.setStatus("current")
_CfprOsControllerInstanceId_Type = CfprManagedObjectId
_CfprOsControllerInstanceId_Object = MibTableColumn
cfprOsControllerInstanceId = _CfprOsControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 1),
    _CfprOsControllerInstanceId_Type()
)
cfprOsControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOsControllerInstanceId.setStatus("current")
_CfprOsControllerDn_Type = CfprManagedObjectDn
_CfprOsControllerDn_Object = MibTableColumn
cfprOsControllerDn = _CfprOsControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 2),
    _CfprOsControllerDn_Type()
)
cfprOsControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerDn.setStatus("current")
_CfprOsControllerRn_Type = SnmpAdminString
_CfprOsControllerRn_Object = MibTableColumn
cfprOsControllerRn = _CfprOsControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 3),
    _CfprOsControllerRn_Type()
)
cfprOsControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerRn.setStatus("current")
_CfprOsControllerBootMode_Type = CfprOsControllerBootMode
_CfprOsControllerBootMode_Object = MibTableColumn
cfprOsControllerBootMode = _CfprOsControllerBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 4),
    _CfprOsControllerBootMode_Type()
)
cfprOsControllerBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerBootMode.setStatus("current")
_CfprOsControllerChassisId_Type = Gauge32
_CfprOsControllerChassisId_Object = MibTableColumn
cfprOsControllerChassisId = _CfprOsControllerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 5),
    _CfprOsControllerChassisId_Type()
)
cfprOsControllerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerChassisId.setStatus("current")
_CfprOsControllerDeployState_Type = CfprOsDeployState
_CfprOsControllerDeployState_Object = MibTableColumn
cfprOsControllerDeployState = _CfprOsControllerDeployState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 6),
    _CfprOsControllerDeployState_Type()
)
cfprOsControllerDeployState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerDeployState.setStatus("current")
_CfprOsControllerEnableDeployOS_Type = TruthValue
_CfprOsControllerEnableDeployOS_Object = MibTableColumn
cfprOsControllerEnableDeployOS = _CfprOsControllerEnableDeployOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 7),
    _CfprOsControllerEnableDeployOS_Type()
)
cfprOsControllerEnableDeployOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerEnableDeployOS.setStatus("current")
_CfprOsControllerFormatDisk_Type = CfprOsControllerFormatDisk
_CfprOsControllerFormatDisk_Object = MibTableColumn
cfprOsControllerFormatDisk = _CfprOsControllerFormatDisk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 8),
    _CfprOsControllerFormatDisk_Type()
)
cfprOsControllerFormatDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFormatDisk.setStatus("current")
_CfprOsControllerFsmDescr_Type = SnmpAdminString
_CfprOsControllerFsmDescr_Object = MibTableColumn
cfprOsControllerFsmDescr = _CfprOsControllerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 9),
    _CfprOsControllerFsmDescr_Type()
)
cfprOsControllerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmDescr.setStatus("current")
_CfprOsControllerFsmFlags_Type = SnmpAdminString
_CfprOsControllerFsmFlags_Object = MibTableColumn
cfprOsControllerFsmFlags = _CfprOsControllerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 10),
    _CfprOsControllerFsmFlags_Type()
)
cfprOsControllerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmFlags.setStatus("current")
_CfprOsControllerFsmPrev_Type = SnmpAdminString
_CfprOsControllerFsmPrev_Object = MibTableColumn
cfprOsControllerFsmPrev = _CfprOsControllerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 11),
    _CfprOsControllerFsmPrev_Type()
)
cfprOsControllerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmPrev.setStatus("current")
_CfprOsControllerFsmProgr_Type = Gauge32
_CfprOsControllerFsmProgr_Object = MibTableColumn
cfprOsControllerFsmProgr = _CfprOsControllerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 12),
    _CfprOsControllerFsmProgr_Type()
)
cfprOsControllerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmProgr.setStatus("current")
_CfprOsControllerFsmRmtInvErrCode_Type = Gauge32
_CfprOsControllerFsmRmtInvErrCode_Object = MibTableColumn
cfprOsControllerFsmRmtInvErrCode = _CfprOsControllerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 13),
    _CfprOsControllerFsmRmtInvErrCode_Type()
)
cfprOsControllerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRmtInvErrCode.setStatus("current")
_CfprOsControllerFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprOsControllerFsmRmtInvErrDescr_Object = MibTableColumn
cfprOsControllerFsmRmtInvErrDescr = _CfprOsControllerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 14),
    _CfprOsControllerFsmRmtInvErrDescr_Type()
)
cfprOsControllerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRmtInvErrDescr.setStatus("current")
_CfprOsControllerFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprOsControllerFsmRmtInvRslt_Object = MibTableColumn
cfprOsControllerFsmRmtInvRslt = _CfprOsControllerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 15),
    _CfprOsControllerFsmRmtInvRslt_Type()
)
cfprOsControllerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRmtInvRslt.setStatus("current")
_CfprOsControllerFsmStageDescr_Type = SnmpAdminString
_CfprOsControllerFsmStageDescr_Object = MibTableColumn
cfprOsControllerFsmStageDescr = _CfprOsControllerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 16),
    _CfprOsControllerFsmStageDescr_Type()
)
cfprOsControllerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageDescr.setStatus("current")
_CfprOsControllerFsmStamp_Type = DateAndTime
_CfprOsControllerFsmStamp_Object = MibTableColumn
cfprOsControllerFsmStamp = _CfprOsControllerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 17),
    _CfprOsControllerFsmStamp_Type()
)
cfprOsControllerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStamp.setStatus("current")
_CfprOsControllerFsmStatus_Type = SnmpAdminString
_CfprOsControllerFsmStatus_Object = MibTableColumn
cfprOsControllerFsmStatus = _CfprOsControllerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 18),
    _CfprOsControllerFsmStatus_Type()
)
cfprOsControllerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStatus.setStatus("current")
_CfprOsControllerFsmTry_Type = Gauge32
_CfprOsControllerFsmTry_Object = MibTableColumn
cfprOsControllerFsmTry = _CfprOsControllerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 19),
    _CfprOsControllerFsmTry_Type()
)
cfprOsControllerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTry.setStatus("current")
_CfprOsControllerHostname_Type = SnmpAdminString
_CfprOsControllerHostname_Object = MibTableColumn
cfprOsControllerHostname = _CfprOsControllerHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 20),
    _CfprOsControllerHostname_Type()
)
cfprOsControllerHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerHostname.setStatus("current")
_CfprOsControllerImageName_Type = SnmpAdminString
_CfprOsControllerImageName_Object = MibTableColumn
cfprOsControllerImageName = _CfprOsControllerImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 21),
    _CfprOsControllerImageName_Type()
)
cfprOsControllerImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerImageName.setStatus("current")
_CfprOsControllerImageSize_Type = Gauge32
_CfprOsControllerImageSize_Object = MibTableColumn
cfprOsControllerImageSize = _CfprOsControllerImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 22),
    _CfprOsControllerImageSize_Type()
)
cfprOsControllerImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerImageSize.setStatus("current")
_CfprOsControllerInitState_Type = CfprOsInitState
_CfprOsControllerInitState_Object = MibTableColumn
cfprOsControllerInitState = _CfprOsControllerInitState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 23),
    _CfprOsControllerInitState_Type()
)
cfprOsControllerInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerInitState.setStatus("current")
_CfprOsControllerMaxNumDeployFailureRecovery_Type = Gauge32
_CfprOsControllerMaxNumDeployFailureRecovery_Object = MibTableColumn
cfprOsControllerMaxNumDeployFailureRecovery = _CfprOsControllerMaxNumDeployFailureRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 24),
    _CfprOsControllerMaxNumDeployFailureRecovery_Type()
)
cfprOsControllerMaxNumDeployFailureRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerMaxNumDeployFailureRecovery.setStatus("current")
_CfprOsControllerMaxNumberVersionMismatched_Type = Gauge32
_CfprOsControllerMaxNumberVersionMismatched_Object = MibTableColumn
cfprOsControllerMaxNumberVersionMismatched = _CfprOsControllerMaxNumberVersionMismatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 25),
    _CfprOsControllerMaxNumberVersionMismatched_Type()
)
cfprOsControllerMaxNumberVersionMismatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerMaxNumberVersionMismatched.setStatus("current")
_CfprOsControllerModel_Type = SnmpAdminString
_CfprOsControllerModel_Object = MibTableColumn
cfprOsControllerModel = _CfprOsControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 26),
    _CfprOsControllerModel_Type()
)
cfprOsControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerModel.setStatus("current")
_CfprOsControllerName_Type = SnmpAdminString
_CfprOsControllerName_Object = MibTableColumn
cfprOsControllerName = _CfprOsControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 27),
    _CfprOsControllerName_Type()
)
cfprOsControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerName.setStatus("current")
_CfprOsControllerNumDeployFailureRecovery_Type = Gauge32
_CfprOsControllerNumDeployFailureRecovery_Object = MibTableColumn
cfprOsControllerNumDeployFailureRecovery = _CfprOsControllerNumDeployFailureRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 28),
    _CfprOsControllerNumDeployFailureRecovery_Type()
)
cfprOsControllerNumDeployFailureRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerNumDeployFailureRecovery.setStatus("current")
_CfprOsControllerNumberVersionMismatched_Type = Gauge32
_CfprOsControllerNumberVersionMismatched_Object = MibTableColumn
cfprOsControllerNumberVersionMismatched = _CfprOsControllerNumberVersionMismatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 29),
    _CfprOsControllerNumberVersionMismatched_Type()
)
cfprOsControllerNumberVersionMismatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerNumberVersionMismatched.setStatus("current")
_CfprOsControllerPnDn_Type = SnmpAdminString
_CfprOsControllerPnDn_Object = MibTableColumn
cfprOsControllerPnDn = _CfprOsControllerPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 30),
    _CfprOsControllerPnDn_Type()
)
cfprOsControllerPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerPnDn.setStatus("current")
_CfprOsControllerRevision_Type = SnmpAdminString
_CfprOsControllerRevision_Object = MibTableColumn
cfprOsControllerRevision = _CfprOsControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 31),
    _CfprOsControllerRevision_Type()
)
cfprOsControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerRevision.setStatus("current")
_CfprOsControllerRommonBuildDate_Type = SnmpAdminString
_CfprOsControllerRommonBuildDate_Object = MibTableColumn
cfprOsControllerRommonBuildDate = _CfprOsControllerRommonBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 32),
    _CfprOsControllerRommonBuildDate_Type()
)
cfprOsControllerRommonBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerRommonBuildDate.setStatus("current")
_CfprOsControllerRommonVersion_Type = SnmpAdminString
_CfprOsControllerRommonVersion_Object = MibTableColumn
cfprOsControllerRommonVersion = _CfprOsControllerRommonVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 33),
    _CfprOsControllerRommonVersion_Type()
)
cfprOsControllerRommonVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerRommonVersion.setStatus("current")
_CfprOsControllerSerial_Type = SnmpAdminString
_CfprOsControllerSerial_Object = MibTableColumn
cfprOsControllerSerial = _CfprOsControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 34),
    _CfprOsControllerSerial_Type()
)
cfprOsControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerSerial.setStatus("current")
_CfprOsControllerServiceStatus_Type = CfprOsBootingUpType
_CfprOsControllerServiceStatus_Object = MibTableColumn
cfprOsControllerServiceStatus = _CfprOsControllerServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 35),
    _CfprOsControllerServiceStatus_Type()
)
cfprOsControllerServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerServiceStatus.setStatus("current")
_CfprOsControllerSlotId_Type = Gauge32
_CfprOsControllerSlotId_Object = MibTableColumn
cfprOsControllerSlotId = _CfprOsControllerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 36),
    _CfprOsControllerSlotId_Type()
)
cfprOsControllerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerSlotId.setStatus("current")
_CfprOsControllerSsposMode_Type = CfprOsOsMode
_CfprOsControllerSsposMode_Object = MibTableColumn
cfprOsControllerSsposMode = _CfprOsControllerSsposMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 37),
    _CfprOsControllerSsposMode_Type()
)
cfprOsControllerSsposMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerSsposMode.setStatus("current")
_CfprOsControllerSupportTftpboot_Type = TruthValue
_CfprOsControllerSupportTftpboot_Object = MibTableColumn
cfprOsControllerSupportTftpboot = _CfprOsControllerSupportTftpboot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 38),
    _CfprOsControllerSupportTftpboot_Type()
)
cfprOsControllerSupportTftpboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerSupportTftpboot.setStatus("current")
_CfprOsControllerType_Type = CfprOsOsType
_CfprOsControllerType_Object = MibTableColumn
cfprOsControllerType = _CfprOsControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 39),
    _CfprOsControllerType_Type()
)
cfprOsControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerType.setStatus("current")
_CfprOsControllerUpgradeState_Type = CfprOsUpgradeState
_CfprOsControllerUpgradeState_Object = MibTableColumn
cfprOsControllerUpgradeState = _CfprOsControllerUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 40),
    _CfprOsControllerUpgradeState_Type()
)
cfprOsControllerUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerUpgradeState.setStatus("current")
_CfprOsControllerVendor_Type = SnmpAdminString
_CfprOsControllerVendor_Object = MibTableColumn
cfprOsControllerVendor = _CfprOsControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 41),
    _CfprOsControllerVendor_Type()
)
cfprOsControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerVendor.setStatus("current")
_CfprOsControllerVersion_Type = SnmpAdminString
_CfprOsControllerVersion_Object = MibTableColumn
cfprOsControllerVersion = _CfprOsControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 42),
    _CfprOsControllerVersion_Type()
)
cfprOsControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerVersion.setStatus("current")
_CfprOsControllerDmaSize_Type = SnmpAdminString
_CfprOsControllerDmaSize_Object = MibTableColumn
cfprOsControllerDmaSize = _CfprOsControllerDmaSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 43),
    _CfprOsControllerDmaSize_Type()
)
cfprOsControllerDmaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerDmaSize.setStatus("current")
_CfprOsControllerHeapSize_Type = SnmpAdminString
_CfprOsControllerHeapSize_Object = MibTableColumn
cfprOsControllerHeapSize = _CfprOsControllerHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 44),
    _CfprOsControllerHeapSize_Type()
)
cfprOsControllerHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerHeapSize.setStatus("current")
_CfprOsControllerHugePageSize_Type = SnmpAdminString
_CfprOsControllerHugePageSize_Object = MibTableColumn
cfprOsControllerHugePageSize = _CfprOsControllerHugePageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 45),
    _CfprOsControllerHugePageSize_Type()
)
cfprOsControllerHugePageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerHugePageSize.setStatus("current")
_CfprOsControllerInstallLicenseState_Type = CfprOsInstallLicenseState
_CfprOsControllerInstallLicenseState_Object = MibTableColumn
cfprOsControllerInstallLicenseState = _CfprOsControllerInstallLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 46),
    _CfprOsControllerInstallLicenseState_Type()
)
cfprOsControllerInstallLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerInstallLicenseState.setStatus("current")
_CfprOsControllerNumHugePages_Type = SnmpAdminString
_CfprOsControllerNumHugePages_Object = MibTableColumn
cfprOsControllerNumHugePages = _CfprOsControllerNumHugePages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 47),
    _CfprOsControllerNumHugePages_Type()
)
cfprOsControllerNumHugePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerNumHugePages.setStatus("current")
_CfprOsControllerPti_Type = SnmpAdminString
_CfprOsControllerPti_Object = MibTableColumn
cfprOsControllerPti = _CfprOsControllerPti_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 48),
    _CfprOsControllerPti_Type()
)
cfprOsControllerPti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerPti.setStatus("current")
_CfprOsControllerSecSmack_Type = TruthValue
_CfprOsControllerSecSmack_Object = MibTableColumn
cfprOsControllerSecSmack = _CfprOsControllerSecSmack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 49),
    _CfprOsControllerSecSmack_Type()
)
cfprOsControllerSecSmack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerSecSmack.setStatus("current")
_CfprOsControllerTurboMode_Type = TruthValue
_CfprOsControllerTurboMode_Object = MibTableColumn
cfprOsControllerTurboMode = _CfprOsControllerTurboMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 2, 1, 50),
    _CfprOsControllerTurboMode_Type()
)
cfprOsControllerTurboMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerTurboMode.setStatus("current")
_CfprOsControllerFsmTable_Object = MibTable
cfprOsControllerFsmTable = _CfprOsControllerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3)
)
if mibBuilder.loadTexts:
    cfprOsControllerFsmTable.setStatus("current")
_CfprOsControllerFsmEntry_Object = MibTableRow
cfprOsControllerFsmEntry = _CfprOsControllerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1)
)
cfprOsControllerFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OS-MIB", "cfprOsControllerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOsControllerFsmEntry.setStatus("current")
_CfprOsControllerFsmInstanceId_Type = CfprManagedObjectId
_CfprOsControllerFsmInstanceId_Object = MibTableColumn
cfprOsControllerFsmInstanceId = _CfprOsControllerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 1),
    _CfprOsControllerFsmInstanceId_Type()
)
cfprOsControllerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOsControllerFsmInstanceId.setStatus("current")
_CfprOsControllerFsmDn_Type = CfprManagedObjectDn
_CfprOsControllerFsmDn_Object = MibTableColumn
cfprOsControllerFsmDn = _CfprOsControllerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 2),
    _CfprOsControllerFsmDn_Type()
)
cfprOsControllerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmDn.setStatus("current")
_CfprOsControllerFsmRn_Type = SnmpAdminString
_CfprOsControllerFsmRn_Object = MibTableColumn
cfprOsControllerFsmRn = _CfprOsControllerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 3),
    _CfprOsControllerFsmRn_Type()
)
cfprOsControllerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRn.setStatus("current")
_CfprOsControllerFsmCompletionTime_Type = DateAndTime
_CfprOsControllerFsmCompletionTime_Object = MibTableColumn
cfprOsControllerFsmCompletionTime = _CfprOsControllerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 4),
    _CfprOsControllerFsmCompletionTime_Type()
)
cfprOsControllerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmCompletionTime.setStatus("current")
_CfprOsControllerFsmCurrentFsm_Type = CfprOsControllerFsmCurrentFsm
_CfprOsControllerFsmCurrentFsm_Object = MibTableColumn
cfprOsControllerFsmCurrentFsm = _CfprOsControllerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 5),
    _CfprOsControllerFsmCurrentFsm_Type()
)
cfprOsControllerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmCurrentFsm.setStatus("current")
_CfprOsControllerFsmDescrData_Type = SnmpAdminString
_CfprOsControllerFsmDescrData_Object = MibTableColumn
cfprOsControllerFsmDescrData = _CfprOsControllerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 6),
    _CfprOsControllerFsmDescrData_Type()
)
cfprOsControllerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmDescrData.setStatus("current")
_CfprOsControllerFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprOsControllerFsmFsmStatus_Object = MibTableColumn
cfprOsControllerFsmFsmStatus = _CfprOsControllerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 7),
    _CfprOsControllerFsmFsmStatus_Type()
)
cfprOsControllerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmFsmStatus.setStatus("current")
_CfprOsControllerFsmProgress_Type = Gauge32
_CfprOsControllerFsmProgress_Object = MibTableColumn
cfprOsControllerFsmProgress = _CfprOsControllerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 8),
    _CfprOsControllerFsmProgress_Type()
)
cfprOsControllerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmProgress.setStatus("current")
_CfprOsControllerFsmRmtErrCode_Type = Gauge32
_CfprOsControllerFsmRmtErrCode_Object = MibTableColumn
cfprOsControllerFsmRmtErrCode = _CfprOsControllerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 9),
    _CfprOsControllerFsmRmtErrCode_Type()
)
cfprOsControllerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRmtErrCode.setStatus("current")
_CfprOsControllerFsmRmtErrDescr_Type = SnmpAdminString
_CfprOsControllerFsmRmtErrDescr_Object = MibTableColumn
cfprOsControllerFsmRmtErrDescr = _CfprOsControllerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 10),
    _CfprOsControllerFsmRmtErrDescr_Type()
)
cfprOsControllerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRmtErrDescr.setStatus("current")
_CfprOsControllerFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprOsControllerFsmRmtRslt_Object = MibTableColumn
cfprOsControllerFsmRmtRslt = _CfprOsControllerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 3, 1, 11),
    _CfprOsControllerFsmRmtRslt_Type()
)
cfprOsControllerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmRmtRslt.setStatus("current")
_CfprOsControllerFsmStageTable_Object = MibTable
cfprOsControllerFsmStageTable = _CfprOsControllerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4)
)
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageTable.setStatus("current")
_CfprOsControllerFsmStageEntry_Object = MibTableRow
cfprOsControllerFsmStageEntry = _CfprOsControllerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1)
)
cfprOsControllerFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OS-MIB", "cfprOsControllerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageEntry.setStatus("current")
_CfprOsControllerFsmStageInstanceId_Type = CfprManagedObjectId
_CfprOsControllerFsmStageInstanceId_Object = MibTableColumn
cfprOsControllerFsmStageInstanceId = _CfprOsControllerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 1),
    _CfprOsControllerFsmStageInstanceId_Type()
)
cfprOsControllerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageInstanceId.setStatus("current")
_CfprOsControllerFsmStageDn_Type = CfprManagedObjectDn
_CfprOsControllerFsmStageDn_Object = MibTableColumn
cfprOsControllerFsmStageDn = _CfprOsControllerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 2),
    _CfprOsControllerFsmStageDn_Type()
)
cfprOsControllerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageDn.setStatus("current")
_CfprOsControllerFsmStageRn_Type = SnmpAdminString
_CfprOsControllerFsmStageRn_Object = MibTableColumn
cfprOsControllerFsmStageRn = _CfprOsControllerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 3),
    _CfprOsControllerFsmStageRn_Type()
)
cfprOsControllerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageRn.setStatus("current")
_CfprOsControllerFsmStageDescrData_Type = SnmpAdminString
_CfprOsControllerFsmStageDescrData_Object = MibTableColumn
cfprOsControllerFsmStageDescrData = _CfprOsControllerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 4),
    _CfprOsControllerFsmStageDescrData_Type()
)
cfprOsControllerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageDescrData.setStatus("current")
_CfprOsControllerFsmStageLastUpdateTime_Type = DateAndTime
_CfprOsControllerFsmStageLastUpdateTime_Object = MibTableColumn
cfprOsControllerFsmStageLastUpdateTime = _CfprOsControllerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 5),
    _CfprOsControllerFsmStageLastUpdateTime_Type()
)
cfprOsControllerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageLastUpdateTime.setStatus("current")
_CfprOsControllerFsmStageName_Type = CfprOsControllerFsmStageName
_CfprOsControllerFsmStageName_Object = MibTableColumn
cfprOsControllerFsmStageName = _CfprOsControllerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 6),
    _CfprOsControllerFsmStageName_Type()
)
cfprOsControllerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageName.setStatus("current")
_CfprOsControllerFsmStageOrder_Type = Gauge32
_CfprOsControllerFsmStageOrder_Object = MibTableColumn
cfprOsControllerFsmStageOrder = _CfprOsControllerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 7),
    _CfprOsControllerFsmStageOrder_Type()
)
cfprOsControllerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageOrder.setStatus("current")
_CfprOsControllerFsmStageRetry_Type = Gauge32
_CfprOsControllerFsmStageRetry_Object = MibTableColumn
cfprOsControllerFsmStageRetry = _CfprOsControllerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 8),
    _CfprOsControllerFsmStageRetry_Type()
)
cfprOsControllerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageRetry.setStatus("current")
_CfprOsControllerFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprOsControllerFsmStageStageStatus_Object = MibTableColumn
cfprOsControllerFsmStageStageStatus = _CfprOsControllerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 4, 1, 9),
    _CfprOsControllerFsmStageStageStatus_Type()
)
cfprOsControllerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmStageStageStatus.setStatus("current")
_CfprOsControllerFsmTaskTable_Object = MibTable
cfprOsControllerFsmTaskTable = _CfprOsControllerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5)
)
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskTable.setStatus("current")
_CfprOsControllerFsmTaskEntry_Object = MibTableRow
cfprOsControllerFsmTaskEntry = _CfprOsControllerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1)
)
cfprOsControllerFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OS-MIB", "cfprOsControllerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskEntry.setStatus("current")
_CfprOsControllerFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprOsControllerFsmTaskInstanceId_Object = MibTableColumn
cfprOsControllerFsmTaskInstanceId = _CfprOsControllerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 1),
    _CfprOsControllerFsmTaskInstanceId_Type()
)
cfprOsControllerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskInstanceId.setStatus("current")
_CfprOsControllerFsmTaskDn_Type = CfprManagedObjectDn
_CfprOsControllerFsmTaskDn_Object = MibTableColumn
cfprOsControllerFsmTaskDn = _CfprOsControllerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 2),
    _CfprOsControllerFsmTaskDn_Type()
)
cfprOsControllerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskDn.setStatus("current")
_CfprOsControllerFsmTaskRn_Type = SnmpAdminString
_CfprOsControllerFsmTaskRn_Object = MibTableColumn
cfprOsControllerFsmTaskRn = _CfprOsControllerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 3),
    _CfprOsControllerFsmTaskRn_Type()
)
cfprOsControllerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskRn.setStatus("current")
_CfprOsControllerFsmTaskCompletion_Type = CfprFsmCompletion
_CfprOsControllerFsmTaskCompletion_Object = MibTableColumn
cfprOsControllerFsmTaskCompletion = _CfprOsControllerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 4),
    _CfprOsControllerFsmTaskCompletion_Type()
)
cfprOsControllerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskCompletion.setStatus("current")
_CfprOsControllerFsmTaskFlags_Type = CfprOsControllerFsmTaskFlags
_CfprOsControllerFsmTaskFlags_Object = MibTableColumn
cfprOsControllerFsmTaskFlags = _CfprOsControllerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 5),
    _CfprOsControllerFsmTaskFlags_Type()
)
cfprOsControllerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskFlags.setStatus("current")
_CfprOsControllerFsmTaskItem_Type = CfprOsControllerFsmTaskItem
_CfprOsControllerFsmTaskItem_Object = MibTableColumn
cfprOsControllerFsmTaskItem = _CfprOsControllerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 6),
    _CfprOsControllerFsmTaskItem_Type()
)
cfprOsControllerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskItem.setStatus("current")
_CfprOsControllerFsmTaskSeqId_Type = Gauge32
_CfprOsControllerFsmTaskSeqId_Object = MibTableColumn
cfprOsControllerFsmTaskSeqId = _CfprOsControllerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 5, 1, 7),
    _CfprOsControllerFsmTaskSeqId_Type()
)
cfprOsControllerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsControllerFsmTaskSeqId.setStatus("current")
_CfprOsInstanceTable_Object = MibTable
cfprOsInstanceTable = _CfprOsInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6)
)
if mibBuilder.loadTexts:
    cfprOsInstanceTable.setStatus("current")
_CfprOsInstanceEntry_Object = MibTableRow
cfprOsInstanceEntry = _CfprOsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1)
)
cfprOsInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-OS-MIB", "cfprOsInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprOsInstanceEntry.setStatus("current")
_CfprOsInstanceInstanceId_Type = CfprManagedObjectId
_CfprOsInstanceInstanceId_Object = MibTableColumn
cfprOsInstanceInstanceId = _CfprOsInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 1),
    _CfprOsInstanceInstanceId_Type()
)
cfprOsInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprOsInstanceInstanceId.setStatus("current")
_CfprOsInstanceDn_Type = CfprManagedObjectDn
_CfprOsInstanceDn_Object = MibTableColumn
cfprOsInstanceDn = _CfprOsInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 2),
    _CfprOsInstanceDn_Type()
)
cfprOsInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceDn.setStatus("current")
_CfprOsInstanceRn_Type = SnmpAdminString
_CfprOsInstanceRn_Object = MibTableColumn
cfprOsInstanceRn = _CfprOsInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 3),
    _CfprOsInstanceRn_Type()
)
cfprOsInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceRn.setStatus("current")
_CfprOsInstanceHostname_Type = SnmpAdminString
_CfprOsInstanceHostname_Object = MibTableColumn
cfprOsInstanceHostname = _CfprOsInstanceHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 4),
    _CfprOsInstanceHostname_Type()
)
cfprOsInstanceHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceHostname.setStatus("current")
_CfprOsInstanceKernelName_Type = SnmpAdminString
_CfprOsInstanceKernelName_Object = MibTableColumn
cfprOsInstanceKernelName = _CfprOsInstanceKernelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 5),
    _CfprOsInstanceKernelName_Type()
)
cfprOsInstanceKernelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceKernelName.setStatus("current")
_CfprOsInstanceKernelRelease_Type = SnmpAdminString
_CfprOsInstanceKernelRelease_Object = MibTableColumn
cfprOsInstanceKernelRelease = _CfprOsInstanceKernelRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 6),
    _CfprOsInstanceKernelRelease_Type()
)
cfprOsInstanceKernelRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceKernelRelease.setStatus("current")
_CfprOsInstanceKernelVersion_Type = SnmpAdminString
_CfprOsInstanceKernelVersion_Object = MibTableColumn
cfprOsInstanceKernelVersion = _CfprOsInstanceKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 7),
    _CfprOsInstanceKernelVersion_Type()
)
cfprOsInstanceKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceKernelVersion.setStatus("current")
_CfprOsInstanceName_Type = SnmpAdminString
_CfprOsInstanceName_Object = MibTableColumn
cfprOsInstanceName = _CfprOsInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 8),
    _CfprOsInstanceName_Type()
)
cfprOsInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceName.setStatus("current")
_CfprOsInstanceType_Type = CfprOsOsType
_CfprOsInstanceType_Object = MibTableColumn
cfprOsInstanceType = _CfprOsInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 9),
    _CfprOsInstanceType_Type()
)
cfprOsInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceType.setStatus("current")
_CfprOsInstanceUpgradeProgress_Type = Gauge32
_CfprOsInstanceUpgradeProgress_Object = MibTableColumn
cfprOsInstanceUpgradeProgress = _CfprOsInstanceUpgradeProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 10),
    _CfprOsInstanceUpgradeProgress_Type()
)
cfprOsInstanceUpgradeProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceUpgradeProgress.setStatus("current")
_CfprOsInstanceUpgradeReturnCode_Type = CfprOsUpgradeReturnCode
_CfprOsInstanceUpgradeReturnCode_Object = MibTableColumn
cfprOsInstanceUpgradeReturnCode = _CfprOsInstanceUpgradeReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 59, 6, 1, 11),
    _CfprOsInstanceUpgradeReturnCode_Type()
)
cfprOsInstanceUpgradeReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprOsInstanceUpgradeReturnCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-OS-MIB",
    **{"cfprOsObjects": cfprOsObjects,
       "cfprOsAgentTable": cfprOsAgentTable,
       "cfprOsAgentEntry": cfprOsAgentEntry,
       "cfprOsAgentInstanceId": cfprOsAgentInstanceId,
       "cfprOsAgentDn": cfprOsAgentDn,
       "cfprOsAgentRn": cfprOsAgentRn,
       "cfprOsAgentLastCmd": cfprOsAgentLastCmd,
       "cfprOsAgentLastEvt": cfprOsAgentLastEvt,
       "cfprOsAgentLastEvtTs": cfprOsAgentLastEvtTs,
       "cfprOsAgentPrevCmd": cfprOsAgentPrevCmd,
       "cfprOsAgentPrevEvt": cfprOsAgentPrevEvt,
       "cfprOsAgentType": cfprOsAgentType,
       "cfprOsAgentVendor": cfprOsAgentVendor,
       "cfprOsAgentVersion": cfprOsAgentVersion,
       "cfprOsControllerTable": cfprOsControllerTable,
       "cfprOsControllerEntry": cfprOsControllerEntry,
       "cfprOsControllerInstanceId": cfprOsControllerInstanceId,
       "cfprOsControllerDn": cfprOsControllerDn,
       "cfprOsControllerRn": cfprOsControllerRn,
       "cfprOsControllerBootMode": cfprOsControllerBootMode,
       "cfprOsControllerChassisId": cfprOsControllerChassisId,
       "cfprOsControllerDeployState": cfprOsControllerDeployState,
       "cfprOsControllerEnableDeployOS": cfprOsControllerEnableDeployOS,
       "cfprOsControllerFormatDisk": cfprOsControllerFormatDisk,
       "cfprOsControllerFsmDescr": cfprOsControllerFsmDescr,
       "cfprOsControllerFsmFlags": cfprOsControllerFsmFlags,
       "cfprOsControllerFsmPrev": cfprOsControllerFsmPrev,
       "cfprOsControllerFsmProgr": cfprOsControllerFsmProgr,
       "cfprOsControllerFsmRmtInvErrCode": cfprOsControllerFsmRmtInvErrCode,
       "cfprOsControllerFsmRmtInvErrDescr": cfprOsControllerFsmRmtInvErrDescr,
       "cfprOsControllerFsmRmtInvRslt": cfprOsControllerFsmRmtInvRslt,
       "cfprOsControllerFsmStageDescr": cfprOsControllerFsmStageDescr,
       "cfprOsControllerFsmStamp": cfprOsControllerFsmStamp,
       "cfprOsControllerFsmStatus": cfprOsControllerFsmStatus,
       "cfprOsControllerFsmTry": cfprOsControllerFsmTry,
       "cfprOsControllerHostname": cfprOsControllerHostname,
       "cfprOsControllerImageName": cfprOsControllerImageName,
       "cfprOsControllerImageSize": cfprOsControllerImageSize,
       "cfprOsControllerInitState": cfprOsControllerInitState,
       "cfprOsControllerMaxNumDeployFailureRecovery": cfprOsControllerMaxNumDeployFailureRecovery,
       "cfprOsControllerMaxNumberVersionMismatched": cfprOsControllerMaxNumberVersionMismatched,
       "cfprOsControllerModel": cfprOsControllerModel,
       "cfprOsControllerName": cfprOsControllerName,
       "cfprOsControllerNumDeployFailureRecovery": cfprOsControllerNumDeployFailureRecovery,
       "cfprOsControllerNumberVersionMismatched": cfprOsControllerNumberVersionMismatched,
       "cfprOsControllerPnDn": cfprOsControllerPnDn,
       "cfprOsControllerRevision": cfprOsControllerRevision,
       "cfprOsControllerRommonBuildDate": cfprOsControllerRommonBuildDate,
       "cfprOsControllerRommonVersion": cfprOsControllerRommonVersion,
       "cfprOsControllerSerial": cfprOsControllerSerial,
       "cfprOsControllerServiceStatus": cfprOsControllerServiceStatus,
       "cfprOsControllerSlotId": cfprOsControllerSlotId,
       "cfprOsControllerSsposMode": cfprOsControllerSsposMode,
       "cfprOsControllerSupportTftpboot": cfprOsControllerSupportTftpboot,
       "cfprOsControllerType": cfprOsControllerType,
       "cfprOsControllerUpgradeState": cfprOsControllerUpgradeState,
       "cfprOsControllerVendor": cfprOsControllerVendor,
       "cfprOsControllerVersion": cfprOsControllerVersion,
       "cfprOsControllerDmaSize": cfprOsControllerDmaSize,
       "cfprOsControllerHeapSize": cfprOsControllerHeapSize,
       "cfprOsControllerHugePageSize": cfprOsControllerHugePageSize,
       "cfprOsControllerInstallLicenseState": cfprOsControllerInstallLicenseState,
       "cfprOsControllerNumHugePages": cfprOsControllerNumHugePages,
       "cfprOsControllerPti": cfprOsControllerPti,
       "cfprOsControllerSecSmack": cfprOsControllerSecSmack,
       "cfprOsControllerTurboMode": cfprOsControllerTurboMode,
       "cfprOsControllerFsmTable": cfprOsControllerFsmTable,
       "cfprOsControllerFsmEntry": cfprOsControllerFsmEntry,
       "cfprOsControllerFsmInstanceId": cfprOsControllerFsmInstanceId,
       "cfprOsControllerFsmDn": cfprOsControllerFsmDn,
       "cfprOsControllerFsmRn": cfprOsControllerFsmRn,
       "cfprOsControllerFsmCompletionTime": cfprOsControllerFsmCompletionTime,
       "cfprOsControllerFsmCurrentFsm": cfprOsControllerFsmCurrentFsm,
       "cfprOsControllerFsmDescrData": cfprOsControllerFsmDescrData,
       "cfprOsControllerFsmFsmStatus": cfprOsControllerFsmFsmStatus,
       "cfprOsControllerFsmProgress": cfprOsControllerFsmProgress,
       "cfprOsControllerFsmRmtErrCode": cfprOsControllerFsmRmtErrCode,
       "cfprOsControllerFsmRmtErrDescr": cfprOsControllerFsmRmtErrDescr,
       "cfprOsControllerFsmRmtRslt": cfprOsControllerFsmRmtRslt,
       "cfprOsControllerFsmStageTable": cfprOsControllerFsmStageTable,
       "cfprOsControllerFsmStageEntry": cfprOsControllerFsmStageEntry,
       "cfprOsControllerFsmStageInstanceId": cfprOsControllerFsmStageInstanceId,
       "cfprOsControllerFsmStageDn": cfprOsControllerFsmStageDn,
       "cfprOsControllerFsmStageRn": cfprOsControllerFsmStageRn,
       "cfprOsControllerFsmStageDescrData": cfprOsControllerFsmStageDescrData,
       "cfprOsControllerFsmStageLastUpdateTime": cfprOsControllerFsmStageLastUpdateTime,
       "cfprOsControllerFsmStageName": cfprOsControllerFsmStageName,
       "cfprOsControllerFsmStageOrder": cfprOsControllerFsmStageOrder,
       "cfprOsControllerFsmStageRetry": cfprOsControllerFsmStageRetry,
       "cfprOsControllerFsmStageStageStatus": cfprOsControllerFsmStageStageStatus,
       "cfprOsControllerFsmTaskTable": cfprOsControllerFsmTaskTable,
       "cfprOsControllerFsmTaskEntry": cfprOsControllerFsmTaskEntry,
       "cfprOsControllerFsmTaskInstanceId": cfprOsControllerFsmTaskInstanceId,
       "cfprOsControllerFsmTaskDn": cfprOsControllerFsmTaskDn,
       "cfprOsControllerFsmTaskRn": cfprOsControllerFsmTaskRn,
       "cfprOsControllerFsmTaskCompletion": cfprOsControllerFsmTaskCompletion,
       "cfprOsControllerFsmTaskFlags": cfprOsControllerFsmTaskFlags,
       "cfprOsControllerFsmTaskItem": cfprOsControllerFsmTaskItem,
       "cfprOsControllerFsmTaskSeqId": cfprOsControllerFsmTaskSeqId,
       "cfprOsInstanceTable": cfprOsInstanceTable,
       "cfprOsInstanceEntry": cfprOsInstanceEntry,
       "cfprOsInstanceInstanceId": cfprOsInstanceInstanceId,
       "cfprOsInstanceDn": cfprOsInstanceDn,
       "cfprOsInstanceRn": cfprOsInstanceRn,
       "cfprOsInstanceHostname": cfprOsInstanceHostname,
       "cfprOsInstanceKernelName": cfprOsInstanceKernelName,
       "cfprOsInstanceKernelRelease": cfprOsInstanceKernelRelease,
       "cfprOsInstanceKernelVersion": cfprOsInstanceKernelVersion,
       "cfprOsInstanceName": cfprOsInstanceName,
       "cfprOsInstanceType": cfprOsInstanceType,
       "cfprOsInstanceUpgradeProgress": cfprOsInstanceUpgradeProgress,
       "cfprOsInstanceUpgradeReturnCode": cfprOsInstanceUpgradeReturnCode}
)
