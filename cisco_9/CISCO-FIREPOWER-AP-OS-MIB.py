# SNMP MIB module (CISCO-FIREPOWER-AP-OS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-OS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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

(CfprApHostagAction,
 CfprApHostagAgentType,
 CfprApHostagEvent,
 CfprApOsBootingUpType,
 CfprApOsControllerBootMode,
 CfprApOsControllerFormatDisk,
 CfprApOsDeployState,
 CfprApOsInitState,
 CfprApOsOsMode,
 CfprApOsOsType,
 CfprApOsUpgradeReturnCode,
 CfprApOsUpgradeState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApHostagAction",
    "CfprApHostagAgentType",
    "CfprApHostagEvent",
    "CfprApOsBootingUpType",
    "CfprApOsControllerBootMode",
    "CfprApOsControllerFormatDisk",
    "CfprApOsDeployState",
    "CfprApOsInitState",
    "CfprApOsOsMode",
    "CfprApOsOsType",
    "CfprApOsUpgradeReturnCode",
    "CfprApOsUpgradeState")

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

cfprApOsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApOsAgentTable_Object = MibTable
cfprApOsAgentTable = _CfprApOsAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1)
)
if mibBuilder.loadTexts:
    cfprApOsAgentTable.setStatus("current")
_CfprApOsAgentEntry_Object = MibTableRow
cfprApOsAgentEntry = _CfprApOsAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1)
)
cfprApOsAgentEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OS-MIB", "cfprApOsAgentInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApOsAgentEntry.setStatus("current")
_CfprApOsAgentInstanceId_Type = CfprApManagedObjectId
_CfprApOsAgentInstanceId_Object = MibTableColumn
cfprApOsAgentInstanceId = _CfprApOsAgentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 1),
    _CfprApOsAgentInstanceId_Type()
)
cfprApOsAgentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApOsAgentInstanceId.setStatus("current")
_CfprApOsAgentDn_Type = CfprApManagedObjectDn
_CfprApOsAgentDn_Object = MibTableColumn
cfprApOsAgentDn = _CfprApOsAgentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 2),
    _CfprApOsAgentDn_Type()
)
cfprApOsAgentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentDn.setStatus("current")
_CfprApOsAgentRn_Type = SnmpAdminString
_CfprApOsAgentRn_Object = MibTableColumn
cfprApOsAgentRn = _CfprApOsAgentRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 3),
    _CfprApOsAgentRn_Type()
)
cfprApOsAgentRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentRn.setStatus("current")
_CfprApOsAgentLastCmd_Type = CfprApHostagAction
_CfprApOsAgentLastCmd_Object = MibTableColumn
cfprApOsAgentLastCmd = _CfprApOsAgentLastCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 4),
    _CfprApOsAgentLastCmd_Type()
)
cfprApOsAgentLastCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentLastCmd.setStatus("current")
_CfprApOsAgentLastEvt_Type = CfprApHostagEvent
_CfprApOsAgentLastEvt_Object = MibTableColumn
cfprApOsAgentLastEvt = _CfprApOsAgentLastEvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 5),
    _CfprApOsAgentLastEvt_Type()
)
cfprApOsAgentLastEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentLastEvt.setStatus("current")
_CfprApOsAgentLastEvtTs_Type = DateAndTime
_CfprApOsAgentLastEvtTs_Object = MibTableColumn
cfprApOsAgentLastEvtTs = _CfprApOsAgentLastEvtTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 6),
    _CfprApOsAgentLastEvtTs_Type()
)
cfprApOsAgentLastEvtTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentLastEvtTs.setStatus("current")
_CfprApOsAgentPrevCmd_Type = CfprApHostagAction
_CfprApOsAgentPrevCmd_Object = MibTableColumn
cfprApOsAgentPrevCmd = _CfprApOsAgentPrevCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 7),
    _CfprApOsAgentPrevCmd_Type()
)
cfprApOsAgentPrevCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentPrevCmd.setStatus("current")
_CfprApOsAgentPrevEvt_Type = CfprApHostagEvent
_CfprApOsAgentPrevEvt_Object = MibTableColumn
cfprApOsAgentPrevEvt = _CfprApOsAgentPrevEvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 8),
    _CfprApOsAgentPrevEvt_Type()
)
cfprApOsAgentPrevEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentPrevEvt.setStatus("current")
_CfprApOsAgentType_Type = CfprApHostagAgentType
_CfprApOsAgentType_Object = MibTableColumn
cfprApOsAgentType = _CfprApOsAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 9),
    _CfprApOsAgentType_Type()
)
cfprApOsAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentType.setStatus("current")
_CfprApOsAgentVendor_Type = SnmpAdminString
_CfprApOsAgentVendor_Object = MibTableColumn
cfprApOsAgentVendor = _CfprApOsAgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 10),
    _CfprApOsAgentVendor_Type()
)
cfprApOsAgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentVendor.setStatus("current")
_CfprApOsAgentVersion_Type = SnmpAdminString
_CfprApOsAgentVersion_Object = MibTableColumn
cfprApOsAgentVersion = _CfprApOsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 1, 1, 11),
    _CfprApOsAgentVersion_Type()
)
cfprApOsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsAgentVersion.setStatus("current")
_CfprApOsControllerTable_Object = MibTable
cfprApOsControllerTable = _CfprApOsControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2)
)
if mibBuilder.loadTexts:
    cfprApOsControllerTable.setStatus("current")
_CfprApOsControllerEntry_Object = MibTableRow
cfprApOsControllerEntry = _CfprApOsControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1)
)
cfprApOsControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OS-MIB", "cfprApOsControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApOsControllerEntry.setStatus("current")
_CfprApOsControllerInstanceId_Type = CfprApManagedObjectId
_CfprApOsControllerInstanceId_Object = MibTableColumn
cfprApOsControllerInstanceId = _CfprApOsControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 1),
    _CfprApOsControllerInstanceId_Type()
)
cfprApOsControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApOsControllerInstanceId.setStatus("current")
_CfprApOsControllerDn_Type = CfprApManagedObjectDn
_CfprApOsControllerDn_Object = MibTableColumn
cfprApOsControllerDn = _CfprApOsControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 2),
    _CfprApOsControllerDn_Type()
)
cfprApOsControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerDn.setStatus("current")
_CfprApOsControllerRn_Type = SnmpAdminString
_CfprApOsControllerRn_Object = MibTableColumn
cfprApOsControllerRn = _CfprApOsControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 3),
    _CfprApOsControllerRn_Type()
)
cfprApOsControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerRn.setStatus("current")
_CfprApOsControllerBootMode_Type = CfprApOsControllerBootMode
_CfprApOsControllerBootMode_Object = MibTableColumn
cfprApOsControllerBootMode = _CfprApOsControllerBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 4),
    _CfprApOsControllerBootMode_Type()
)
cfprApOsControllerBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerBootMode.setStatus("current")
_CfprApOsControllerChassisId_Type = Gauge32
_CfprApOsControllerChassisId_Object = MibTableColumn
cfprApOsControllerChassisId = _CfprApOsControllerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 5),
    _CfprApOsControllerChassisId_Type()
)
cfprApOsControllerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerChassisId.setStatus("current")
_CfprApOsControllerDeployState_Type = CfprApOsDeployState
_CfprApOsControllerDeployState_Object = MibTableColumn
cfprApOsControllerDeployState = _CfprApOsControllerDeployState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 6),
    _CfprApOsControllerDeployState_Type()
)
cfprApOsControllerDeployState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerDeployState.setStatus("current")
_CfprApOsControllerDmaSize_Type = SnmpAdminString
_CfprApOsControllerDmaSize_Object = MibTableColumn
cfprApOsControllerDmaSize = _CfprApOsControllerDmaSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 7),
    _CfprApOsControllerDmaSize_Type()
)
cfprApOsControllerDmaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerDmaSize.setStatus("current")
_CfprApOsControllerEnableDeployOS_Type = TruthValue
_CfprApOsControllerEnableDeployOS_Object = MibTableColumn
cfprApOsControllerEnableDeployOS = _CfprApOsControllerEnableDeployOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 8),
    _CfprApOsControllerEnableDeployOS_Type()
)
cfprApOsControllerEnableDeployOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerEnableDeployOS.setStatus("current")
_CfprApOsControllerFormatDisk_Type = CfprApOsControllerFormatDisk
_CfprApOsControllerFormatDisk_Object = MibTableColumn
cfprApOsControllerFormatDisk = _CfprApOsControllerFormatDisk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 9),
    _CfprApOsControllerFormatDisk_Type()
)
cfprApOsControllerFormatDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerFormatDisk.setStatus("current")
_CfprApOsControllerHeapSize_Type = SnmpAdminString
_CfprApOsControllerHeapSize_Object = MibTableColumn
cfprApOsControllerHeapSize = _CfprApOsControllerHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 10),
    _CfprApOsControllerHeapSize_Type()
)
cfprApOsControllerHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerHeapSize.setStatus("current")
_CfprApOsControllerHostname_Type = SnmpAdminString
_CfprApOsControllerHostname_Object = MibTableColumn
cfprApOsControllerHostname = _CfprApOsControllerHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 11),
    _CfprApOsControllerHostname_Type()
)
cfprApOsControllerHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerHostname.setStatus("current")
_CfprApOsControllerHugePageSize_Type = SnmpAdminString
_CfprApOsControllerHugePageSize_Object = MibTableColumn
cfprApOsControllerHugePageSize = _CfprApOsControllerHugePageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 12),
    _CfprApOsControllerHugePageSize_Type()
)
cfprApOsControllerHugePageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerHugePageSize.setStatus("current")
_CfprApOsControllerImageName_Type = SnmpAdminString
_CfprApOsControllerImageName_Object = MibTableColumn
cfprApOsControllerImageName = _CfprApOsControllerImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 13),
    _CfprApOsControllerImageName_Type()
)
cfprApOsControllerImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerImageName.setStatus("current")
_CfprApOsControllerImageSize_Type = Gauge32
_CfprApOsControllerImageSize_Object = MibTableColumn
cfprApOsControllerImageSize = _CfprApOsControllerImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 14),
    _CfprApOsControllerImageSize_Type()
)
cfprApOsControllerImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerImageSize.setStatus("current")
_CfprApOsControllerInitState_Type = CfprApOsInitState
_CfprApOsControllerInitState_Object = MibTableColumn
cfprApOsControllerInitState = _CfprApOsControllerInitState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 15),
    _CfprApOsControllerInitState_Type()
)
cfprApOsControllerInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerInitState.setStatus("current")
_CfprApOsControllerMaxNumDeployFailureRecovery_Type = Gauge32
_CfprApOsControllerMaxNumDeployFailureRecovery_Object = MibTableColumn
cfprApOsControllerMaxNumDeployFailureRecovery = _CfprApOsControllerMaxNumDeployFailureRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 16),
    _CfprApOsControllerMaxNumDeployFailureRecovery_Type()
)
cfprApOsControllerMaxNumDeployFailureRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerMaxNumDeployFailureRecovery.setStatus("current")
_CfprApOsControllerMaxNumberVersionMismatched_Type = Gauge32
_CfprApOsControllerMaxNumberVersionMismatched_Object = MibTableColumn
cfprApOsControllerMaxNumberVersionMismatched = _CfprApOsControllerMaxNumberVersionMismatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 17),
    _CfprApOsControllerMaxNumberVersionMismatched_Type()
)
cfprApOsControllerMaxNumberVersionMismatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerMaxNumberVersionMismatched.setStatus("current")
_CfprApOsControllerModel_Type = SnmpAdminString
_CfprApOsControllerModel_Object = MibTableColumn
cfprApOsControllerModel = _CfprApOsControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 18),
    _CfprApOsControllerModel_Type()
)
cfprApOsControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerModel.setStatus("current")
_CfprApOsControllerName_Type = SnmpAdminString
_CfprApOsControllerName_Object = MibTableColumn
cfprApOsControllerName = _CfprApOsControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 19),
    _CfprApOsControllerName_Type()
)
cfprApOsControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerName.setStatus("current")
_CfprApOsControllerNumDeployFailureRecovery_Type = Gauge32
_CfprApOsControllerNumDeployFailureRecovery_Object = MibTableColumn
cfprApOsControllerNumDeployFailureRecovery = _CfprApOsControllerNumDeployFailureRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 20),
    _CfprApOsControllerNumDeployFailureRecovery_Type()
)
cfprApOsControllerNumDeployFailureRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerNumDeployFailureRecovery.setStatus("current")
_CfprApOsControllerNumHugePages_Type = SnmpAdminString
_CfprApOsControllerNumHugePages_Object = MibTableColumn
cfprApOsControllerNumHugePages = _CfprApOsControllerNumHugePages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 21),
    _CfprApOsControllerNumHugePages_Type()
)
cfprApOsControllerNumHugePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerNumHugePages.setStatus("current")
_CfprApOsControllerNumberVersionMismatched_Type = Gauge32
_CfprApOsControllerNumberVersionMismatched_Object = MibTableColumn
cfprApOsControllerNumberVersionMismatched = _CfprApOsControllerNumberVersionMismatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 22),
    _CfprApOsControllerNumberVersionMismatched_Type()
)
cfprApOsControllerNumberVersionMismatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerNumberVersionMismatched.setStatus("current")
_CfprApOsControllerPnDn_Type = SnmpAdminString
_CfprApOsControllerPnDn_Object = MibTableColumn
cfprApOsControllerPnDn = _CfprApOsControllerPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 23),
    _CfprApOsControllerPnDn_Type()
)
cfprApOsControllerPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerPnDn.setStatus("current")
_CfprApOsControllerRevision_Type = SnmpAdminString
_CfprApOsControllerRevision_Object = MibTableColumn
cfprApOsControllerRevision = _CfprApOsControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 24),
    _CfprApOsControllerRevision_Type()
)
cfprApOsControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerRevision.setStatus("current")
_CfprApOsControllerRommonBuildDate_Type = SnmpAdminString
_CfprApOsControllerRommonBuildDate_Object = MibTableColumn
cfprApOsControllerRommonBuildDate = _CfprApOsControllerRommonBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 25),
    _CfprApOsControllerRommonBuildDate_Type()
)
cfprApOsControllerRommonBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerRommonBuildDate.setStatus("current")
_CfprApOsControllerRommonVersion_Type = SnmpAdminString
_CfprApOsControllerRommonVersion_Object = MibTableColumn
cfprApOsControllerRommonVersion = _CfprApOsControllerRommonVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 26),
    _CfprApOsControllerRommonVersion_Type()
)
cfprApOsControllerRommonVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerRommonVersion.setStatus("current")
_CfprApOsControllerSerial_Type = SnmpAdminString
_CfprApOsControllerSerial_Object = MibTableColumn
cfprApOsControllerSerial = _CfprApOsControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 27),
    _CfprApOsControllerSerial_Type()
)
cfprApOsControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerSerial.setStatus("current")
_CfprApOsControllerServiceStatus_Type = CfprApOsBootingUpType
_CfprApOsControllerServiceStatus_Object = MibTableColumn
cfprApOsControllerServiceStatus = _CfprApOsControllerServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 28),
    _CfprApOsControllerServiceStatus_Type()
)
cfprApOsControllerServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerServiceStatus.setStatus("current")
_CfprApOsControllerSlotId_Type = Gauge32
_CfprApOsControllerSlotId_Object = MibTableColumn
cfprApOsControllerSlotId = _CfprApOsControllerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 29),
    _CfprApOsControllerSlotId_Type()
)
cfprApOsControllerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerSlotId.setStatus("current")
_CfprApOsControllerSsposMode_Type = CfprApOsOsMode
_CfprApOsControllerSsposMode_Object = MibTableColumn
cfprApOsControllerSsposMode = _CfprApOsControllerSsposMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 30),
    _CfprApOsControllerSsposMode_Type()
)
cfprApOsControllerSsposMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerSsposMode.setStatus("current")
_CfprApOsControllerSupportTftpboot_Type = TruthValue
_CfprApOsControllerSupportTftpboot_Object = MibTableColumn
cfprApOsControllerSupportTftpboot = _CfprApOsControllerSupportTftpboot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 31),
    _CfprApOsControllerSupportTftpboot_Type()
)
cfprApOsControllerSupportTftpboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerSupportTftpboot.setStatus("current")
_CfprApOsControllerType_Type = CfprApOsOsType
_CfprApOsControllerType_Object = MibTableColumn
cfprApOsControllerType = _CfprApOsControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 32),
    _CfprApOsControllerType_Type()
)
cfprApOsControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerType.setStatus("current")
_CfprApOsControllerUpgradeState_Type = CfprApOsUpgradeState
_CfprApOsControllerUpgradeState_Object = MibTableColumn
cfprApOsControllerUpgradeState = _CfprApOsControllerUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 33),
    _CfprApOsControllerUpgradeState_Type()
)
cfprApOsControllerUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerUpgradeState.setStatus("current")
_CfprApOsControllerVendor_Type = SnmpAdminString
_CfprApOsControllerVendor_Object = MibTableColumn
cfprApOsControllerVendor = _CfprApOsControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 34),
    _CfprApOsControllerVendor_Type()
)
cfprApOsControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerVendor.setStatus("current")
_CfprApOsControllerVersion_Type = SnmpAdminString
_CfprApOsControllerVersion_Object = MibTableColumn
cfprApOsControllerVersion = _CfprApOsControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 2, 1, 35),
    _CfprApOsControllerVersion_Type()
)
cfprApOsControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsControllerVersion.setStatus("current")
_CfprApOsInstanceTable_Object = MibTable
cfprApOsInstanceTable = _CfprApOsInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3)
)
if mibBuilder.loadTexts:
    cfprApOsInstanceTable.setStatus("current")
_CfprApOsInstanceEntry_Object = MibTableRow
cfprApOsInstanceEntry = _CfprApOsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1)
)
cfprApOsInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-OS-MIB", "cfprApOsInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApOsInstanceEntry.setStatus("current")
_CfprApOsInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApOsInstanceInstanceId_Object = MibTableColumn
cfprApOsInstanceInstanceId = _CfprApOsInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 1),
    _CfprApOsInstanceInstanceId_Type()
)
cfprApOsInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApOsInstanceInstanceId.setStatus("current")
_CfprApOsInstanceDn_Type = CfprApManagedObjectDn
_CfprApOsInstanceDn_Object = MibTableColumn
cfprApOsInstanceDn = _CfprApOsInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 2),
    _CfprApOsInstanceDn_Type()
)
cfprApOsInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceDn.setStatus("current")
_CfprApOsInstanceRn_Type = SnmpAdminString
_CfprApOsInstanceRn_Object = MibTableColumn
cfprApOsInstanceRn = _CfprApOsInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 3),
    _CfprApOsInstanceRn_Type()
)
cfprApOsInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceRn.setStatus("current")
_CfprApOsInstanceHostname_Type = SnmpAdminString
_CfprApOsInstanceHostname_Object = MibTableColumn
cfprApOsInstanceHostname = _CfprApOsInstanceHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 4),
    _CfprApOsInstanceHostname_Type()
)
cfprApOsInstanceHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceHostname.setStatus("current")
_CfprApOsInstanceKernelName_Type = SnmpAdminString
_CfprApOsInstanceKernelName_Object = MibTableColumn
cfprApOsInstanceKernelName = _CfprApOsInstanceKernelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 5),
    _CfprApOsInstanceKernelName_Type()
)
cfprApOsInstanceKernelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceKernelName.setStatus("current")
_CfprApOsInstanceKernelRelease_Type = SnmpAdminString
_CfprApOsInstanceKernelRelease_Object = MibTableColumn
cfprApOsInstanceKernelRelease = _CfprApOsInstanceKernelRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 6),
    _CfprApOsInstanceKernelRelease_Type()
)
cfprApOsInstanceKernelRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceKernelRelease.setStatus("current")
_CfprApOsInstanceKernelVersion_Type = SnmpAdminString
_CfprApOsInstanceKernelVersion_Object = MibTableColumn
cfprApOsInstanceKernelVersion = _CfprApOsInstanceKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 7),
    _CfprApOsInstanceKernelVersion_Type()
)
cfprApOsInstanceKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceKernelVersion.setStatus("current")
_CfprApOsInstanceName_Type = SnmpAdminString
_CfprApOsInstanceName_Object = MibTableColumn
cfprApOsInstanceName = _CfprApOsInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 8),
    _CfprApOsInstanceName_Type()
)
cfprApOsInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceName.setStatus("current")
_CfprApOsInstanceType_Type = CfprApOsOsType
_CfprApOsInstanceType_Object = MibTableColumn
cfprApOsInstanceType = _CfprApOsInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 9),
    _CfprApOsInstanceType_Type()
)
cfprApOsInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceType.setStatus("current")
_CfprApOsInstanceUpgradeProgress_Type = Gauge32
_CfprApOsInstanceUpgradeProgress_Object = MibTableColumn
cfprApOsInstanceUpgradeProgress = _CfprApOsInstanceUpgradeProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 10),
    _CfprApOsInstanceUpgradeProgress_Type()
)
cfprApOsInstanceUpgradeProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceUpgradeProgress.setStatus("current")
_CfprApOsInstanceUpgradeReturnCode_Type = CfprApOsUpgradeReturnCode
_CfprApOsInstanceUpgradeReturnCode_Object = MibTableColumn
cfprApOsInstanceUpgradeReturnCode = _CfprApOsInstanceUpgradeReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 59, 3, 1, 11),
    _CfprApOsInstanceUpgradeReturnCode_Type()
)
cfprApOsInstanceUpgradeReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApOsInstanceUpgradeReturnCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-OS-MIB",
    **{"cfprApOsObjects": cfprApOsObjects,
       "cfprApOsAgentTable": cfprApOsAgentTable,
       "cfprApOsAgentEntry": cfprApOsAgentEntry,
       "cfprApOsAgentInstanceId": cfprApOsAgentInstanceId,
       "cfprApOsAgentDn": cfprApOsAgentDn,
       "cfprApOsAgentRn": cfprApOsAgentRn,
       "cfprApOsAgentLastCmd": cfprApOsAgentLastCmd,
       "cfprApOsAgentLastEvt": cfprApOsAgentLastEvt,
       "cfprApOsAgentLastEvtTs": cfprApOsAgentLastEvtTs,
       "cfprApOsAgentPrevCmd": cfprApOsAgentPrevCmd,
       "cfprApOsAgentPrevEvt": cfprApOsAgentPrevEvt,
       "cfprApOsAgentType": cfprApOsAgentType,
       "cfprApOsAgentVendor": cfprApOsAgentVendor,
       "cfprApOsAgentVersion": cfprApOsAgentVersion,
       "cfprApOsControllerTable": cfprApOsControllerTable,
       "cfprApOsControllerEntry": cfprApOsControllerEntry,
       "cfprApOsControllerInstanceId": cfprApOsControllerInstanceId,
       "cfprApOsControllerDn": cfprApOsControllerDn,
       "cfprApOsControllerRn": cfprApOsControllerRn,
       "cfprApOsControllerBootMode": cfprApOsControllerBootMode,
       "cfprApOsControllerChassisId": cfprApOsControllerChassisId,
       "cfprApOsControllerDeployState": cfprApOsControllerDeployState,
       "cfprApOsControllerDmaSize": cfprApOsControllerDmaSize,
       "cfprApOsControllerEnableDeployOS": cfprApOsControllerEnableDeployOS,
       "cfprApOsControllerFormatDisk": cfprApOsControllerFormatDisk,
       "cfprApOsControllerHeapSize": cfprApOsControllerHeapSize,
       "cfprApOsControllerHostname": cfprApOsControllerHostname,
       "cfprApOsControllerHugePageSize": cfprApOsControllerHugePageSize,
       "cfprApOsControllerImageName": cfprApOsControllerImageName,
       "cfprApOsControllerImageSize": cfprApOsControllerImageSize,
       "cfprApOsControllerInitState": cfprApOsControllerInitState,
       "cfprApOsControllerMaxNumDeployFailureRecovery": cfprApOsControllerMaxNumDeployFailureRecovery,
       "cfprApOsControllerMaxNumberVersionMismatched": cfprApOsControllerMaxNumberVersionMismatched,
       "cfprApOsControllerModel": cfprApOsControllerModel,
       "cfprApOsControllerName": cfprApOsControllerName,
       "cfprApOsControllerNumDeployFailureRecovery": cfprApOsControllerNumDeployFailureRecovery,
       "cfprApOsControllerNumHugePages": cfprApOsControllerNumHugePages,
       "cfprApOsControllerNumberVersionMismatched": cfprApOsControllerNumberVersionMismatched,
       "cfprApOsControllerPnDn": cfprApOsControllerPnDn,
       "cfprApOsControllerRevision": cfprApOsControllerRevision,
       "cfprApOsControllerRommonBuildDate": cfprApOsControllerRommonBuildDate,
       "cfprApOsControllerRommonVersion": cfprApOsControllerRommonVersion,
       "cfprApOsControllerSerial": cfprApOsControllerSerial,
       "cfprApOsControllerServiceStatus": cfprApOsControllerServiceStatus,
       "cfprApOsControllerSlotId": cfprApOsControllerSlotId,
       "cfprApOsControllerSsposMode": cfprApOsControllerSsposMode,
       "cfprApOsControllerSupportTftpboot": cfprApOsControllerSupportTftpboot,
       "cfprApOsControllerType": cfprApOsControllerType,
       "cfprApOsControllerUpgradeState": cfprApOsControllerUpgradeState,
       "cfprApOsControllerVendor": cfprApOsControllerVendor,
       "cfprApOsControllerVersion": cfprApOsControllerVersion,
       "cfprApOsInstanceTable": cfprApOsInstanceTable,
       "cfprApOsInstanceEntry": cfprApOsInstanceEntry,
       "cfprApOsInstanceInstanceId": cfprApOsInstanceInstanceId,
       "cfprApOsInstanceDn": cfprApOsInstanceDn,
       "cfprApOsInstanceRn": cfprApOsInstanceRn,
       "cfprApOsInstanceHostname": cfprApOsInstanceHostname,
       "cfprApOsInstanceKernelName": cfprApOsInstanceKernelName,
       "cfprApOsInstanceKernelRelease": cfprApOsInstanceKernelRelease,
       "cfprApOsInstanceKernelVersion": cfprApOsInstanceKernelVersion,
       "cfprApOsInstanceName": cfprApOsInstanceName,
       "cfprApOsInstanceType": cfprApOsInstanceType,
       "cfprApOsInstanceUpgradeProgress": cfprApOsInstanceUpgradeProgress,
       "cfprApOsInstanceUpgradeReturnCode": cfprApOsInstanceUpgradeReturnCode}
)
