# SNMP MIB module (CISCO-FIREPOWER-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-CAPABILITY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
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

(CfprCapabilityAdminState,
 CfprCapabilityCatalogueFsmCurrentFsm,
 CfprCapabilityCatalogueFsmStageName,
 CfprCapabilityCatalogueFsmTaskItem,
 CfprCapabilityFeatureStatus,
 CfprCapabilityMgmtExtensionFsmCurrentFsm,
 CfprCapabilityMgmtExtensionFsmStageName,
 CfprCapabilityMgmtExtensionFsmTaskItem,
 CfprCapabilityOperStatus,
 CfprCapabilityPlatform,
 CfprCapabilityUpdaterFsmCurrentFsm,
 CfprCapabilityUpdaterFsmStageName,
 CfprCapabilityUpdaterFsmTaskItem,
 CfprConditionRemoteInvRslt,
 CfprFirmwareTransport,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprCapabilityAdminState",
    "CfprCapabilityCatalogueFsmCurrentFsm",
    "CfprCapabilityCatalogueFsmStageName",
    "CfprCapabilityCatalogueFsmTaskItem",
    "CfprCapabilityFeatureStatus",
    "CfprCapabilityMgmtExtensionFsmCurrentFsm",
    "CfprCapabilityMgmtExtensionFsmStageName",
    "CfprCapabilityMgmtExtensionFsmTaskItem",
    "CfprCapabilityOperStatus",
    "CfprCapabilityPlatform",
    "CfprCapabilityUpdaterFsmCurrentFsm",
    "CfprCapabilityUpdaterFsmStageName",
    "CfprCapabilityUpdaterFsmTaskItem",
    "CfprConditionRemoteInvRslt",
    "CfprFirmwareTransport",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus")

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

cfprCapabilityObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprCapabilityCatalogueTable_Object = MibTable
cfprCapabilityCatalogueTable = _CfprCapabilityCatalogueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueTable.setStatus("current")
_CfprCapabilityCatalogueEntry_Object = MibTableRow
cfprCapabilityCatalogueEntry = _CfprCapabilityCatalogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1)
)
cfprCapabilityCatalogueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityCatalogueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueEntry.setStatus("current")
_CfprCapabilityCatalogueInstanceId_Type = CfprManagedObjectId
_CfprCapabilityCatalogueInstanceId_Object = MibTableColumn
cfprCapabilityCatalogueInstanceId = _CfprCapabilityCatalogueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 1),
    _CfprCapabilityCatalogueInstanceId_Type()
)
cfprCapabilityCatalogueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueInstanceId.setStatus("current")
_CfprCapabilityCatalogueDn_Type = CfprManagedObjectDn
_CfprCapabilityCatalogueDn_Object = MibTableColumn
cfprCapabilityCatalogueDn = _CfprCapabilityCatalogueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 2),
    _CfprCapabilityCatalogueDn_Type()
)
cfprCapabilityCatalogueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueDn.setStatus("current")
_CfprCapabilityCatalogueRn_Type = SnmpAdminString
_CfprCapabilityCatalogueRn_Object = MibTableColumn
cfprCapabilityCatalogueRn = _CfprCapabilityCatalogueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 3),
    _CfprCapabilityCatalogueRn_Type()
)
cfprCapabilityCatalogueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueRn.setStatus("current")
_CfprCapabilityCatalogueFileParseFailures_Type = Gauge32
_CfprCapabilityCatalogueFileParseFailures_Object = MibTableColumn
cfprCapabilityCatalogueFileParseFailures = _CfprCapabilityCatalogueFileParseFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 4),
    _CfprCapabilityCatalogueFileParseFailures_Type()
)
cfprCapabilityCatalogueFileParseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFileParseFailures.setStatus("current")
_CfprCapabilityCatalogueFilesParsed_Type = Gauge32
_CfprCapabilityCatalogueFilesParsed_Object = MibTableColumn
cfprCapabilityCatalogueFilesParsed = _CfprCapabilityCatalogueFilesParsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 5),
    _CfprCapabilityCatalogueFilesParsed_Type()
)
cfprCapabilityCatalogueFilesParsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFilesParsed.setStatus("current")
_CfprCapabilityCatalogueFsmDescr_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmDescr_Object = MibTableColumn
cfprCapabilityCatalogueFsmDescr = _CfprCapabilityCatalogueFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 6),
    _CfprCapabilityCatalogueFsmDescr_Type()
)
cfprCapabilityCatalogueFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmDescr.setStatus("current")
_CfprCapabilityCatalogueFsmPrev_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmPrev_Object = MibTableColumn
cfprCapabilityCatalogueFsmPrev = _CfprCapabilityCatalogueFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 7),
    _CfprCapabilityCatalogueFsmPrev_Type()
)
cfprCapabilityCatalogueFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmPrev.setStatus("current")
_CfprCapabilityCatalogueFsmProgr_Type = Gauge32
_CfprCapabilityCatalogueFsmProgr_Object = MibTableColumn
cfprCapabilityCatalogueFsmProgr = _CfprCapabilityCatalogueFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 8),
    _CfprCapabilityCatalogueFsmProgr_Type()
)
cfprCapabilityCatalogueFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmProgr.setStatus("current")
_CfprCapabilityCatalogueFsmRmtInvErrCode_Type = Gauge32
_CfprCapabilityCatalogueFsmRmtInvErrCode_Object = MibTableColumn
cfprCapabilityCatalogueFsmRmtInvErrCode = _CfprCapabilityCatalogueFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 9),
    _CfprCapabilityCatalogueFsmRmtInvErrCode_Type()
)
cfprCapabilityCatalogueFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRmtInvErrCode.setStatus("current")
_CfprCapabilityCatalogueFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmRmtInvErrDescr_Object = MibTableColumn
cfprCapabilityCatalogueFsmRmtInvErrDescr = _CfprCapabilityCatalogueFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 10),
    _CfprCapabilityCatalogueFsmRmtInvErrDescr_Type()
)
cfprCapabilityCatalogueFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRmtInvErrDescr.setStatus("current")
_CfprCapabilityCatalogueFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprCapabilityCatalogueFsmRmtInvRslt_Object = MibTableColumn
cfprCapabilityCatalogueFsmRmtInvRslt = _CfprCapabilityCatalogueFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 11),
    _CfprCapabilityCatalogueFsmRmtInvRslt_Type()
)
cfprCapabilityCatalogueFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRmtInvRslt.setStatus("current")
_CfprCapabilityCatalogueFsmStageDescr_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmStageDescr_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageDescr = _CfprCapabilityCatalogueFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 12),
    _CfprCapabilityCatalogueFsmStageDescr_Type()
)
cfprCapabilityCatalogueFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageDescr.setStatus("current")
_CfprCapabilityCatalogueFsmStamp_Type = DateAndTime
_CfprCapabilityCatalogueFsmStamp_Object = MibTableColumn
cfprCapabilityCatalogueFsmStamp = _CfprCapabilityCatalogueFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 13),
    _CfprCapabilityCatalogueFsmStamp_Type()
)
cfprCapabilityCatalogueFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStamp.setStatus("current")
_CfprCapabilityCatalogueFsmStatus_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmStatus_Object = MibTableColumn
cfprCapabilityCatalogueFsmStatus = _CfprCapabilityCatalogueFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 14),
    _CfprCapabilityCatalogueFsmStatus_Type()
)
cfprCapabilityCatalogueFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStatus.setStatus("current")
_CfprCapabilityCatalogueFsmTry_Type = Gauge32
_CfprCapabilityCatalogueFsmTry_Object = MibTableColumn
cfprCapabilityCatalogueFsmTry = _CfprCapabilityCatalogueFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 15),
    _CfprCapabilityCatalogueFsmTry_Type()
)
cfprCapabilityCatalogueFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTry.setStatus("current")
_CfprCapabilityCatalogueLoadErrors_Type = Gauge32
_CfprCapabilityCatalogueLoadErrors_Object = MibTableColumn
cfprCapabilityCatalogueLoadErrors = _CfprCapabilityCatalogueLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 16),
    _CfprCapabilityCatalogueLoadErrors_Type()
)
cfprCapabilityCatalogueLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueLoadErrors.setStatus("current")
_CfprCapabilityCatalogueLoadWarnings_Type = Gauge32
_CfprCapabilityCatalogueLoadWarnings_Object = MibTableColumn
cfprCapabilityCatalogueLoadWarnings = _CfprCapabilityCatalogueLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 17),
    _CfprCapabilityCatalogueLoadWarnings_Type()
)
cfprCapabilityCatalogueLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueLoadWarnings.setStatus("current")
_CfprCapabilityCatalogueProviderLoadFailures_Type = Gauge32
_CfprCapabilityCatalogueProviderLoadFailures_Object = MibTableColumn
cfprCapabilityCatalogueProviderLoadFailures = _CfprCapabilityCatalogueProviderLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 18),
    _CfprCapabilityCatalogueProviderLoadFailures_Type()
)
cfprCapabilityCatalogueProviderLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueProviderLoadFailures.setStatus("current")
_CfprCapabilityCatalogueProvidersLoaded_Type = Gauge32
_CfprCapabilityCatalogueProvidersLoaded_Object = MibTableColumn
cfprCapabilityCatalogueProvidersLoaded = _CfprCapabilityCatalogueProvidersLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 19),
    _CfprCapabilityCatalogueProvidersLoaded_Type()
)
cfprCapabilityCatalogueProvidersLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueProvidersLoaded.setStatus("current")
_CfprCapabilityCatalogueVersion_Type = SnmpAdminString
_CfprCapabilityCatalogueVersion_Object = MibTableColumn
cfprCapabilityCatalogueVersion = _CfprCapabilityCatalogueVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 20),
    _CfprCapabilityCatalogueVersion_Type()
)
cfprCapabilityCatalogueVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueVersion.setStatus("current")
_CfprCapabilityCatalogueBiosTokenVersion_Type = SnmpAdminString
_CfprCapabilityCatalogueBiosTokenVersion_Object = MibTableColumn
cfprCapabilityCatalogueBiosTokenVersion = _CfprCapabilityCatalogueBiosTokenVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 1, 1, 21),
    _CfprCapabilityCatalogueBiosTokenVersion_Type()
)
cfprCapabilityCatalogueBiosTokenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueBiosTokenVersion.setStatus("current")
_CfprCapabilityCatalogueFsmTable_Object = MibTable
cfprCapabilityCatalogueFsmTable = _CfprCapabilityCatalogueFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTable.setStatus("current")
_CfprCapabilityCatalogueFsmEntry_Object = MibTableRow
cfprCapabilityCatalogueFsmEntry = _CfprCapabilityCatalogueFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1)
)
cfprCapabilityCatalogueFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityCatalogueFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmEntry.setStatus("current")
_CfprCapabilityCatalogueFsmInstanceId_Type = CfprManagedObjectId
_CfprCapabilityCatalogueFsmInstanceId_Object = MibTableColumn
cfprCapabilityCatalogueFsmInstanceId = _CfprCapabilityCatalogueFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 1),
    _CfprCapabilityCatalogueFsmInstanceId_Type()
)
cfprCapabilityCatalogueFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmInstanceId.setStatus("current")
_CfprCapabilityCatalogueFsmDn_Type = CfprManagedObjectDn
_CfprCapabilityCatalogueFsmDn_Object = MibTableColumn
cfprCapabilityCatalogueFsmDn = _CfprCapabilityCatalogueFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 2),
    _CfprCapabilityCatalogueFsmDn_Type()
)
cfprCapabilityCatalogueFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmDn.setStatus("current")
_CfprCapabilityCatalogueFsmRn_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmRn_Object = MibTableColumn
cfprCapabilityCatalogueFsmRn = _CfprCapabilityCatalogueFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 3),
    _CfprCapabilityCatalogueFsmRn_Type()
)
cfprCapabilityCatalogueFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRn.setStatus("current")
_CfprCapabilityCatalogueFsmCompletionTime_Type = DateAndTime
_CfprCapabilityCatalogueFsmCompletionTime_Object = MibTableColumn
cfprCapabilityCatalogueFsmCompletionTime = _CfprCapabilityCatalogueFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 4),
    _CfprCapabilityCatalogueFsmCompletionTime_Type()
)
cfprCapabilityCatalogueFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmCompletionTime.setStatus("current")
_CfprCapabilityCatalogueFsmCurrentFsm_Type = CfprCapabilityCatalogueFsmCurrentFsm
_CfprCapabilityCatalogueFsmCurrentFsm_Object = MibTableColumn
cfprCapabilityCatalogueFsmCurrentFsm = _CfprCapabilityCatalogueFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 5),
    _CfprCapabilityCatalogueFsmCurrentFsm_Type()
)
cfprCapabilityCatalogueFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmCurrentFsm.setStatus("current")
_CfprCapabilityCatalogueFsmDescrData_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmDescrData_Object = MibTableColumn
cfprCapabilityCatalogueFsmDescrData = _CfprCapabilityCatalogueFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 6),
    _CfprCapabilityCatalogueFsmDescrData_Type()
)
cfprCapabilityCatalogueFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmDescrData.setStatus("current")
_CfprCapabilityCatalogueFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprCapabilityCatalogueFsmFsmStatus_Object = MibTableColumn
cfprCapabilityCatalogueFsmFsmStatus = _CfprCapabilityCatalogueFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 7),
    _CfprCapabilityCatalogueFsmFsmStatus_Type()
)
cfprCapabilityCatalogueFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmFsmStatus.setStatus("current")
_CfprCapabilityCatalogueFsmProgress_Type = Gauge32
_CfprCapabilityCatalogueFsmProgress_Object = MibTableColumn
cfprCapabilityCatalogueFsmProgress = _CfprCapabilityCatalogueFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 8),
    _CfprCapabilityCatalogueFsmProgress_Type()
)
cfprCapabilityCatalogueFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmProgress.setStatus("current")
_CfprCapabilityCatalogueFsmRmtErrCode_Type = Gauge32
_CfprCapabilityCatalogueFsmRmtErrCode_Object = MibTableColumn
cfprCapabilityCatalogueFsmRmtErrCode = _CfprCapabilityCatalogueFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 9),
    _CfprCapabilityCatalogueFsmRmtErrCode_Type()
)
cfprCapabilityCatalogueFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRmtErrCode.setStatus("current")
_CfprCapabilityCatalogueFsmRmtErrDescr_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmRmtErrDescr_Object = MibTableColumn
cfprCapabilityCatalogueFsmRmtErrDescr = _CfprCapabilityCatalogueFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 10),
    _CfprCapabilityCatalogueFsmRmtErrDescr_Type()
)
cfprCapabilityCatalogueFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRmtErrDescr.setStatus("current")
_CfprCapabilityCatalogueFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprCapabilityCatalogueFsmRmtRslt_Object = MibTableColumn
cfprCapabilityCatalogueFsmRmtRslt = _CfprCapabilityCatalogueFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 2, 1, 11),
    _CfprCapabilityCatalogueFsmRmtRslt_Type()
)
cfprCapabilityCatalogueFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmRmtRslt.setStatus("current")
_CfprCapabilityCatalogueFsmStageTable_Object = MibTable
cfprCapabilityCatalogueFsmStageTable = _CfprCapabilityCatalogueFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageTable.setStatus("current")
_CfprCapabilityCatalogueFsmStageEntry_Object = MibTableRow
cfprCapabilityCatalogueFsmStageEntry = _CfprCapabilityCatalogueFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1)
)
cfprCapabilityCatalogueFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityCatalogueFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageEntry.setStatus("current")
_CfprCapabilityCatalogueFsmStageInstanceId_Type = CfprManagedObjectId
_CfprCapabilityCatalogueFsmStageInstanceId_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageInstanceId = _CfprCapabilityCatalogueFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 1),
    _CfprCapabilityCatalogueFsmStageInstanceId_Type()
)
cfprCapabilityCatalogueFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageInstanceId.setStatus("current")
_CfprCapabilityCatalogueFsmStageDn_Type = CfprManagedObjectDn
_CfprCapabilityCatalogueFsmStageDn_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageDn = _CfprCapabilityCatalogueFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 2),
    _CfprCapabilityCatalogueFsmStageDn_Type()
)
cfprCapabilityCatalogueFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageDn.setStatus("current")
_CfprCapabilityCatalogueFsmStageRn_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmStageRn_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageRn = _CfprCapabilityCatalogueFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 3),
    _CfprCapabilityCatalogueFsmStageRn_Type()
)
cfprCapabilityCatalogueFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageRn.setStatus("current")
_CfprCapabilityCatalogueFsmStageDescrData_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmStageDescrData_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageDescrData = _CfprCapabilityCatalogueFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 4),
    _CfprCapabilityCatalogueFsmStageDescrData_Type()
)
cfprCapabilityCatalogueFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageDescrData.setStatus("current")
_CfprCapabilityCatalogueFsmStageLastUpdateTime_Type = DateAndTime
_CfprCapabilityCatalogueFsmStageLastUpdateTime_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageLastUpdateTime = _CfprCapabilityCatalogueFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 5),
    _CfprCapabilityCatalogueFsmStageLastUpdateTime_Type()
)
cfprCapabilityCatalogueFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageLastUpdateTime.setStatus("current")
_CfprCapabilityCatalogueFsmStageName_Type = CfprCapabilityCatalogueFsmStageName
_CfprCapabilityCatalogueFsmStageName_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageName = _CfprCapabilityCatalogueFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 6),
    _CfprCapabilityCatalogueFsmStageName_Type()
)
cfprCapabilityCatalogueFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageName.setStatus("current")
_CfprCapabilityCatalogueFsmStageOrder_Type = Gauge32
_CfprCapabilityCatalogueFsmStageOrder_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageOrder = _CfprCapabilityCatalogueFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 7),
    _CfprCapabilityCatalogueFsmStageOrder_Type()
)
cfprCapabilityCatalogueFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageOrder.setStatus("current")
_CfprCapabilityCatalogueFsmStageRetry_Type = Gauge32
_CfprCapabilityCatalogueFsmStageRetry_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageRetry = _CfprCapabilityCatalogueFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 8),
    _CfprCapabilityCatalogueFsmStageRetry_Type()
)
cfprCapabilityCatalogueFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageRetry.setStatus("current")
_CfprCapabilityCatalogueFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprCapabilityCatalogueFsmStageStageStatus_Object = MibTableColumn
cfprCapabilityCatalogueFsmStageStageStatus = _CfprCapabilityCatalogueFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 3, 1, 9),
    _CfprCapabilityCatalogueFsmStageStageStatus_Type()
)
cfprCapabilityCatalogueFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmStageStageStatus.setStatus("current")
_CfprCapabilityCatalogueFsmTaskTable_Object = MibTable
cfprCapabilityCatalogueFsmTaskTable = _CfprCapabilityCatalogueFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4)
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskTable.setStatus("current")
_CfprCapabilityCatalogueFsmTaskEntry_Object = MibTableRow
cfprCapabilityCatalogueFsmTaskEntry = _CfprCapabilityCatalogueFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1)
)
cfprCapabilityCatalogueFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityCatalogueFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskEntry.setStatus("current")
_CfprCapabilityCatalogueFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprCapabilityCatalogueFsmTaskInstanceId_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskInstanceId = _CfprCapabilityCatalogueFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 1),
    _CfprCapabilityCatalogueFsmTaskInstanceId_Type()
)
cfprCapabilityCatalogueFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskInstanceId.setStatus("current")
_CfprCapabilityCatalogueFsmTaskDn_Type = CfprManagedObjectDn
_CfprCapabilityCatalogueFsmTaskDn_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskDn = _CfprCapabilityCatalogueFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 2),
    _CfprCapabilityCatalogueFsmTaskDn_Type()
)
cfprCapabilityCatalogueFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskDn.setStatus("current")
_CfprCapabilityCatalogueFsmTaskRn_Type = SnmpAdminString
_CfprCapabilityCatalogueFsmTaskRn_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskRn = _CfprCapabilityCatalogueFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 3),
    _CfprCapabilityCatalogueFsmTaskRn_Type()
)
cfprCapabilityCatalogueFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskRn.setStatus("current")
_CfprCapabilityCatalogueFsmTaskCompletion_Type = CfprFsmCompletion
_CfprCapabilityCatalogueFsmTaskCompletion_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskCompletion = _CfprCapabilityCatalogueFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 4),
    _CfprCapabilityCatalogueFsmTaskCompletion_Type()
)
cfprCapabilityCatalogueFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskCompletion.setStatus("current")
_CfprCapabilityCatalogueFsmTaskFlags_Type = CfprFsmFlags
_CfprCapabilityCatalogueFsmTaskFlags_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskFlags = _CfprCapabilityCatalogueFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 5),
    _CfprCapabilityCatalogueFsmTaskFlags_Type()
)
cfprCapabilityCatalogueFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskFlags.setStatus("current")
_CfprCapabilityCatalogueFsmTaskItem_Type = CfprCapabilityCatalogueFsmTaskItem
_CfprCapabilityCatalogueFsmTaskItem_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskItem = _CfprCapabilityCatalogueFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 6),
    _CfprCapabilityCatalogueFsmTaskItem_Type()
)
cfprCapabilityCatalogueFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskItem.setStatus("current")
_CfprCapabilityCatalogueFsmTaskSeqId_Type = Gauge32
_CfprCapabilityCatalogueFsmTaskSeqId_Object = MibTableColumn
cfprCapabilityCatalogueFsmTaskSeqId = _CfprCapabilityCatalogueFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 4, 1, 7),
    _CfprCapabilityCatalogueFsmTaskSeqId_Type()
)
cfprCapabilityCatalogueFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityCatalogueFsmTaskSeqId.setStatus("current")
_CfprCapabilityEpTable_Object = MibTable
cfprCapabilityEpTable = _CfprCapabilityEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 5)
)
if mibBuilder.loadTexts:
    cfprCapabilityEpTable.setStatus("current")
_CfprCapabilityEpEntry_Object = MibTableRow
cfprCapabilityEpEntry = _CfprCapabilityEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 5, 1)
)
cfprCapabilityEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityEpEntry.setStatus("current")
_CfprCapabilityEpInstanceId_Type = CfprManagedObjectId
_CfprCapabilityEpInstanceId_Object = MibTableColumn
cfprCapabilityEpInstanceId = _CfprCapabilityEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 5, 1, 1),
    _CfprCapabilityEpInstanceId_Type()
)
cfprCapabilityEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityEpInstanceId.setStatus("current")
_CfprCapabilityEpDn_Type = CfprManagedObjectDn
_CfprCapabilityEpDn_Object = MibTableColumn
cfprCapabilityEpDn = _CfprCapabilityEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 5, 1, 2),
    _CfprCapabilityEpDn_Type()
)
cfprCapabilityEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityEpDn.setStatus("current")
_CfprCapabilityEpRn_Type = SnmpAdminString
_CfprCapabilityEpRn_Object = MibTableColumn
cfprCapabilityEpRn = _CfprCapabilityEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 5, 1, 3),
    _CfprCapabilityEpRn_Type()
)
cfprCapabilityEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityEpRn.setStatus("current")
_CfprCapabilityFeatureLimitsTable_Object = MibTable
cfprCapabilityFeatureLimitsTable = _CfprCapabilityFeatureLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6)
)
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsTable.setStatus("current")
_CfprCapabilityFeatureLimitsEntry_Object = MibTableRow
cfprCapabilityFeatureLimitsEntry = _CfprCapabilityFeatureLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1)
)
cfprCapabilityFeatureLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityFeatureLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsEntry.setStatus("current")
_CfprCapabilityFeatureLimitsInstanceId_Type = CfprManagedObjectId
_CfprCapabilityFeatureLimitsInstanceId_Object = MibTableColumn
cfprCapabilityFeatureLimitsInstanceId = _CfprCapabilityFeatureLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 1),
    _CfprCapabilityFeatureLimitsInstanceId_Type()
)
cfprCapabilityFeatureLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsInstanceId.setStatus("current")
_CfprCapabilityFeatureLimitsDn_Type = CfprManagedObjectDn
_CfprCapabilityFeatureLimitsDn_Object = MibTableColumn
cfprCapabilityFeatureLimitsDn = _CfprCapabilityFeatureLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 2),
    _CfprCapabilityFeatureLimitsDn_Type()
)
cfprCapabilityFeatureLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsDn.setStatus("current")
_CfprCapabilityFeatureLimitsRn_Type = SnmpAdminString
_CfprCapabilityFeatureLimitsRn_Object = MibTableColumn
cfprCapabilityFeatureLimitsRn = _CfprCapabilityFeatureLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 3),
    _CfprCapabilityFeatureLimitsRn_Type()
)
cfprCapabilityFeatureLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsRn.setStatus("current")
_CfprCapabilityFeatureLimitsDescr_Type = SnmpAdminString
_CfprCapabilityFeatureLimitsDescr_Object = MibTableColumn
cfprCapabilityFeatureLimitsDescr = _CfprCapabilityFeatureLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 4),
    _CfprCapabilityFeatureLimitsDescr_Type()
)
cfprCapabilityFeatureLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsDescr.setStatus("current")
_CfprCapabilityFeatureLimitsFeatureStatus_Type = CfprCapabilityFeatureStatus
_CfprCapabilityFeatureLimitsFeatureStatus_Object = MibTableColumn
cfprCapabilityFeatureLimitsFeatureStatus = _CfprCapabilityFeatureLimitsFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 5),
    _CfprCapabilityFeatureLimitsFeatureStatus_Type()
)
cfprCapabilityFeatureLimitsFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsFeatureStatus.setStatus("current")
_CfprCapabilityFeatureLimitsLimit_Type = Gauge32
_CfprCapabilityFeatureLimitsLimit_Object = MibTableColumn
cfprCapabilityFeatureLimitsLimit = _CfprCapabilityFeatureLimitsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 6),
    _CfprCapabilityFeatureLimitsLimit_Type()
)
cfprCapabilityFeatureLimitsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsLimit.setStatus("current")
_CfprCapabilityFeatureLimitsName_Type = SnmpAdminString
_CfprCapabilityFeatureLimitsName_Object = MibTableColumn
cfprCapabilityFeatureLimitsName = _CfprCapabilityFeatureLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 7),
    _CfprCapabilityFeatureLimitsName_Type()
)
cfprCapabilityFeatureLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsName.setStatus("current")
_CfprCapabilityFeatureLimitsPlatform_Type = CfprCapabilityPlatform
_CfprCapabilityFeatureLimitsPlatform_Object = MibTableColumn
cfprCapabilityFeatureLimitsPlatform = _CfprCapabilityFeatureLimitsPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 6, 1, 8),
    _CfprCapabilityFeatureLimitsPlatform_Type()
)
cfprCapabilityFeatureLimitsPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityFeatureLimitsPlatform.setStatus("current")
_CfprCapabilityMgmtExtensionTable_Object = MibTable
cfprCapabilityMgmtExtensionTable = _CfprCapabilityMgmtExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7)
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionTable.setStatus("current")
_CfprCapabilityMgmtExtensionEntry_Object = MibTableRow
cfprCapabilityMgmtExtensionEntry = _CfprCapabilityMgmtExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1)
)
cfprCapabilityMgmtExtensionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityMgmtExtensionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionEntry.setStatus("current")
_CfprCapabilityMgmtExtensionInstanceId_Type = CfprManagedObjectId
_CfprCapabilityMgmtExtensionInstanceId_Object = MibTableColumn
cfprCapabilityMgmtExtensionInstanceId = _CfprCapabilityMgmtExtensionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 1),
    _CfprCapabilityMgmtExtensionInstanceId_Type()
)
cfprCapabilityMgmtExtensionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionInstanceId.setStatus("current")
_CfprCapabilityMgmtExtensionDn_Type = CfprManagedObjectDn
_CfprCapabilityMgmtExtensionDn_Object = MibTableColumn
cfprCapabilityMgmtExtensionDn = _CfprCapabilityMgmtExtensionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 2),
    _CfprCapabilityMgmtExtensionDn_Type()
)
cfprCapabilityMgmtExtensionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionDn.setStatus("current")
_CfprCapabilityMgmtExtensionRn_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionRn_Object = MibTableColumn
cfprCapabilityMgmtExtensionRn = _CfprCapabilityMgmtExtensionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 3),
    _CfprCapabilityMgmtExtensionRn_Type()
)
cfprCapabilityMgmtExtensionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionRn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmDescr_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmDescr_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmDescr = _CfprCapabilityMgmtExtensionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 4),
    _CfprCapabilityMgmtExtensionFsmDescr_Type()
)
cfprCapabilityMgmtExtensionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmDescr.setStatus("current")
_CfprCapabilityMgmtExtensionFsmPrev_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmPrev_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmPrev = _CfprCapabilityMgmtExtensionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 5),
    _CfprCapabilityMgmtExtensionFsmPrev_Type()
)
cfprCapabilityMgmtExtensionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmPrev.setStatus("current")
_CfprCapabilityMgmtExtensionFsmProgr_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmProgr_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmProgr = _CfprCapabilityMgmtExtensionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 6),
    _CfprCapabilityMgmtExtensionFsmProgr_Type()
)
cfprCapabilityMgmtExtensionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmProgr.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRmtInvErrCode_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmRmtInvErrCode_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRmtInvErrCode = _CfprCapabilityMgmtExtensionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 7),
    _CfprCapabilityMgmtExtensionFsmRmtInvErrCode_Type()
)
cfprCapabilityMgmtExtensionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRmtInvErrCode.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmRmtInvErrDescr_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRmtInvErrDescr = _CfprCapabilityMgmtExtensionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 8),
    _CfprCapabilityMgmtExtensionFsmRmtInvErrDescr_Type()
)
cfprCapabilityMgmtExtensionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRmtInvErrDescr.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprCapabilityMgmtExtensionFsmRmtInvRslt_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRmtInvRslt = _CfprCapabilityMgmtExtensionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 9),
    _CfprCapabilityMgmtExtensionFsmRmtInvRslt_Type()
)
cfprCapabilityMgmtExtensionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRmtInvRslt.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageDescr_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmStageDescr_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageDescr = _CfprCapabilityMgmtExtensionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 10),
    _CfprCapabilityMgmtExtensionFsmStageDescr_Type()
)
cfprCapabilityMgmtExtensionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageDescr.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStamp_Type = DateAndTime
_CfprCapabilityMgmtExtensionFsmStamp_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStamp = _CfprCapabilityMgmtExtensionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 11),
    _CfprCapabilityMgmtExtensionFsmStamp_Type()
)
cfprCapabilityMgmtExtensionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStamp.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStatus_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmStatus_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStatus = _CfprCapabilityMgmtExtensionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 12),
    _CfprCapabilityMgmtExtensionFsmStatus_Type()
)
cfprCapabilityMgmtExtensionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStatus.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTry_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmTry_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTry = _CfprCapabilityMgmtExtensionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 7, 1, 13),
    _CfprCapabilityMgmtExtensionFsmTry_Type()
)
cfprCapabilityMgmtExtensionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTry.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTable_Object = MibTable
cfprCapabilityMgmtExtensionFsmTable = _CfprCapabilityMgmtExtensionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8)
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTable.setStatus("current")
_CfprCapabilityMgmtExtensionFsmEntry_Object = MibTableRow
cfprCapabilityMgmtExtensionFsmEntry = _CfprCapabilityMgmtExtensionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1)
)
cfprCapabilityMgmtExtensionFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityMgmtExtensionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmEntry.setStatus("current")
_CfprCapabilityMgmtExtensionFsmInstanceId_Type = CfprManagedObjectId
_CfprCapabilityMgmtExtensionFsmInstanceId_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmInstanceId = _CfprCapabilityMgmtExtensionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 1),
    _CfprCapabilityMgmtExtensionFsmInstanceId_Type()
)
cfprCapabilityMgmtExtensionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmInstanceId.setStatus("current")
_CfprCapabilityMgmtExtensionFsmDn_Type = CfprManagedObjectDn
_CfprCapabilityMgmtExtensionFsmDn_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmDn = _CfprCapabilityMgmtExtensionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 2),
    _CfprCapabilityMgmtExtensionFsmDn_Type()
)
cfprCapabilityMgmtExtensionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmDn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRn_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmRn_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRn = _CfprCapabilityMgmtExtensionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 3),
    _CfprCapabilityMgmtExtensionFsmRn_Type()
)
cfprCapabilityMgmtExtensionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmCompletionTime_Type = DateAndTime
_CfprCapabilityMgmtExtensionFsmCompletionTime_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmCompletionTime = _CfprCapabilityMgmtExtensionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 4),
    _CfprCapabilityMgmtExtensionFsmCompletionTime_Type()
)
cfprCapabilityMgmtExtensionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmCompletionTime.setStatus("current")
_CfprCapabilityMgmtExtensionFsmCurrentFsm_Type = CfprCapabilityMgmtExtensionFsmCurrentFsm
_CfprCapabilityMgmtExtensionFsmCurrentFsm_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmCurrentFsm = _CfprCapabilityMgmtExtensionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 5),
    _CfprCapabilityMgmtExtensionFsmCurrentFsm_Type()
)
cfprCapabilityMgmtExtensionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmCurrentFsm.setStatus("current")
_CfprCapabilityMgmtExtensionFsmDescrData_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmDescrData_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmDescrData = _CfprCapabilityMgmtExtensionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 6),
    _CfprCapabilityMgmtExtensionFsmDescrData_Type()
)
cfprCapabilityMgmtExtensionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmDescrData.setStatus("current")
_CfprCapabilityMgmtExtensionFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprCapabilityMgmtExtensionFsmFsmStatus_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmFsmStatus = _CfprCapabilityMgmtExtensionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 7),
    _CfprCapabilityMgmtExtensionFsmFsmStatus_Type()
)
cfprCapabilityMgmtExtensionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmFsmStatus.setStatus("current")
_CfprCapabilityMgmtExtensionFsmProgress_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmProgress_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmProgress = _CfprCapabilityMgmtExtensionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 8),
    _CfprCapabilityMgmtExtensionFsmProgress_Type()
)
cfprCapabilityMgmtExtensionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmProgress.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRmtErrCode_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmRmtErrCode_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRmtErrCode = _CfprCapabilityMgmtExtensionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 9),
    _CfprCapabilityMgmtExtensionFsmRmtErrCode_Type()
)
cfprCapabilityMgmtExtensionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRmtErrCode.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRmtErrDescr_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmRmtErrDescr_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRmtErrDescr = _CfprCapabilityMgmtExtensionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 10),
    _CfprCapabilityMgmtExtensionFsmRmtErrDescr_Type()
)
cfprCapabilityMgmtExtensionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRmtErrDescr.setStatus("current")
_CfprCapabilityMgmtExtensionFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprCapabilityMgmtExtensionFsmRmtRslt_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmRmtRslt = _CfprCapabilityMgmtExtensionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 8, 1, 11),
    _CfprCapabilityMgmtExtensionFsmRmtRslt_Type()
)
cfprCapabilityMgmtExtensionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmRmtRslt.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageTable_Object = MibTable
cfprCapabilityMgmtExtensionFsmStageTable = _CfprCapabilityMgmtExtensionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9)
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageTable.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageEntry_Object = MibTableRow
cfprCapabilityMgmtExtensionFsmStageEntry = _CfprCapabilityMgmtExtensionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1)
)
cfprCapabilityMgmtExtensionFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityMgmtExtensionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageEntry.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageInstanceId_Type = CfprManagedObjectId
_CfprCapabilityMgmtExtensionFsmStageInstanceId_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageInstanceId = _CfprCapabilityMgmtExtensionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 1),
    _CfprCapabilityMgmtExtensionFsmStageInstanceId_Type()
)
cfprCapabilityMgmtExtensionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageInstanceId.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageDn_Type = CfprManagedObjectDn
_CfprCapabilityMgmtExtensionFsmStageDn_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageDn = _CfprCapabilityMgmtExtensionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 2),
    _CfprCapabilityMgmtExtensionFsmStageDn_Type()
)
cfprCapabilityMgmtExtensionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageDn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageRn_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmStageRn_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageRn = _CfprCapabilityMgmtExtensionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 3),
    _CfprCapabilityMgmtExtensionFsmStageRn_Type()
)
cfprCapabilityMgmtExtensionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageRn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageDescrData_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmStageDescrData_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageDescrData = _CfprCapabilityMgmtExtensionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 4),
    _CfprCapabilityMgmtExtensionFsmStageDescrData_Type()
)
cfprCapabilityMgmtExtensionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageDescrData.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageLastUpdateTime_Type = DateAndTime
_CfprCapabilityMgmtExtensionFsmStageLastUpdateTime_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageLastUpdateTime = _CfprCapabilityMgmtExtensionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 5),
    _CfprCapabilityMgmtExtensionFsmStageLastUpdateTime_Type()
)
cfprCapabilityMgmtExtensionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageLastUpdateTime.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageName_Type = CfprCapabilityMgmtExtensionFsmStageName
_CfprCapabilityMgmtExtensionFsmStageName_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageName = _CfprCapabilityMgmtExtensionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 6),
    _CfprCapabilityMgmtExtensionFsmStageName_Type()
)
cfprCapabilityMgmtExtensionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageName.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageOrder_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmStageOrder_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageOrder = _CfprCapabilityMgmtExtensionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 7),
    _CfprCapabilityMgmtExtensionFsmStageOrder_Type()
)
cfprCapabilityMgmtExtensionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageOrder.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageRetry_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmStageRetry_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageRetry = _CfprCapabilityMgmtExtensionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 8),
    _CfprCapabilityMgmtExtensionFsmStageRetry_Type()
)
cfprCapabilityMgmtExtensionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageRetry.setStatus("current")
_CfprCapabilityMgmtExtensionFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprCapabilityMgmtExtensionFsmStageStageStatus_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmStageStageStatus = _CfprCapabilityMgmtExtensionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 9, 1, 9),
    _CfprCapabilityMgmtExtensionFsmStageStageStatus_Type()
)
cfprCapabilityMgmtExtensionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmStageStageStatus.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskTable_Object = MibTable
cfprCapabilityMgmtExtensionFsmTaskTable = _CfprCapabilityMgmtExtensionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10)
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskTable.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskEntry_Object = MibTableRow
cfprCapabilityMgmtExtensionFsmTaskEntry = _CfprCapabilityMgmtExtensionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1)
)
cfprCapabilityMgmtExtensionFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityMgmtExtensionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskEntry.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprCapabilityMgmtExtensionFsmTaskInstanceId_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskInstanceId = _CfprCapabilityMgmtExtensionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 1),
    _CfprCapabilityMgmtExtensionFsmTaskInstanceId_Type()
)
cfprCapabilityMgmtExtensionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskInstanceId.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskDn_Type = CfprManagedObjectDn
_CfprCapabilityMgmtExtensionFsmTaskDn_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskDn = _CfprCapabilityMgmtExtensionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 2),
    _CfprCapabilityMgmtExtensionFsmTaskDn_Type()
)
cfprCapabilityMgmtExtensionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskDn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskRn_Type = SnmpAdminString
_CfprCapabilityMgmtExtensionFsmTaskRn_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskRn = _CfprCapabilityMgmtExtensionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 3),
    _CfprCapabilityMgmtExtensionFsmTaskRn_Type()
)
cfprCapabilityMgmtExtensionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskRn.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskCompletion_Type = CfprFsmCompletion
_CfprCapabilityMgmtExtensionFsmTaskCompletion_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskCompletion = _CfprCapabilityMgmtExtensionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 4),
    _CfprCapabilityMgmtExtensionFsmTaskCompletion_Type()
)
cfprCapabilityMgmtExtensionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskCompletion.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskFlags_Type = CfprFsmFlags
_CfprCapabilityMgmtExtensionFsmTaskFlags_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskFlags = _CfprCapabilityMgmtExtensionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 5),
    _CfprCapabilityMgmtExtensionFsmTaskFlags_Type()
)
cfprCapabilityMgmtExtensionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskFlags.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskItem_Type = CfprCapabilityMgmtExtensionFsmTaskItem
_CfprCapabilityMgmtExtensionFsmTaskItem_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskItem = _CfprCapabilityMgmtExtensionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 6),
    _CfprCapabilityMgmtExtensionFsmTaskItem_Type()
)
cfprCapabilityMgmtExtensionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskItem.setStatus("current")
_CfprCapabilityMgmtExtensionFsmTaskSeqId_Type = Gauge32
_CfprCapabilityMgmtExtensionFsmTaskSeqId_Object = MibTableColumn
cfprCapabilityMgmtExtensionFsmTaskSeqId = _CfprCapabilityMgmtExtensionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 10, 1, 7),
    _CfprCapabilityMgmtExtensionFsmTaskSeqId_Type()
)
cfprCapabilityMgmtExtensionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityMgmtExtensionFsmTaskSeqId.setStatus("current")
_CfprCapabilityNetworkLimitsTable_Object = MibTable
cfprCapabilityNetworkLimitsTable = _CfprCapabilityNetworkLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 11)
)
if mibBuilder.loadTexts:
    cfprCapabilityNetworkLimitsTable.setStatus("current")
_CfprCapabilityNetworkLimitsEntry_Object = MibTableRow
cfprCapabilityNetworkLimitsEntry = _CfprCapabilityNetworkLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 11, 1)
)
cfprCapabilityNetworkLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityNetworkLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityNetworkLimitsEntry.setStatus("current")
_CfprCapabilityNetworkLimitsInstanceId_Type = CfprManagedObjectId
_CfprCapabilityNetworkLimitsInstanceId_Object = MibTableColumn
cfprCapabilityNetworkLimitsInstanceId = _CfprCapabilityNetworkLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 11, 1, 1),
    _CfprCapabilityNetworkLimitsInstanceId_Type()
)
cfprCapabilityNetworkLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityNetworkLimitsInstanceId.setStatus("current")
_CfprCapabilityNetworkLimitsDn_Type = CfprManagedObjectDn
_CfprCapabilityNetworkLimitsDn_Object = MibTableColumn
cfprCapabilityNetworkLimitsDn = _CfprCapabilityNetworkLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 11, 1, 2),
    _CfprCapabilityNetworkLimitsDn_Type()
)
cfprCapabilityNetworkLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityNetworkLimitsDn.setStatus("current")
_CfprCapabilityNetworkLimitsRn_Type = SnmpAdminString
_CfprCapabilityNetworkLimitsRn_Object = MibTableColumn
cfprCapabilityNetworkLimitsRn = _CfprCapabilityNetworkLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 11, 1, 3),
    _CfprCapabilityNetworkLimitsRn_Type()
)
cfprCapabilityNetworkLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityNetworkLimitsRn.setStatus("current")
_CfprCapabilityStorageLimitsTable_Object = MibTable
cfprCapabilityStorageLimitsTable = _CfprCapabilityStorageLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 12)
)
if mibBuilder.loadTexts:
    cfprCapabilityStorageLimitsTable.setStatus("current")
_CfprCapabilityStorageLimitsEntry_Object = MibTableRow
cfprCapabilityStorageLimitsEntry = _CfprCapabilityStorageLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 12, 1)
)
cfprCapabilityStorageLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityStorageLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityStorageLimitsEntry.setStatus("current")
_CfprCapabilityStorageLimitsInstanceId_Type = CfprManagedObjectId
_CfprCapabilityStorageLimitsInstanceId_Object = MibTableColumn
cfprCapabilityStorageLimitsInstanceId = _CfprCapabilityStorageLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 12, 1, 1),
    _CfprCapabilityStorageLimitsInstanceId_Type()
)
cfprCapabilityStorageLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityStorageLimitsInstanceId.setStatus("current")
_CfprCapabilityStorageLimitsDn_Type = CfprManagedObjectDn
_CfprCapabilityStorageLimitsDn_Object = MibTableColumn
cfprCapabilityStorageLimitsDn = _CfprCapabilityStorageLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 12, 1, 2),
    _CfprCapabilityStorageLimitsDn_Type()
)
cfprCapabilityStorageLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityStorageLimitsDn.setStatus("current")
_CfprCapabilityStorageLimitsRn_Type = SnmpAdminString
_CfprCapabilityStorageLimitsRn_Object = MibTableColumn
cfprCapabilityStorageLimitsRn = _CfprCapabilityStorageLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 12, 1, 3),
    _CfprCapabilityStorageLimitsRn_Type()
)
cfprCapabilityStorageLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityStorageLimitsRn.setStatus("current")
_CfprCapabilitySystemLimitsTable_Object = MibTable
cfprCapabilitySystemLimitsTable = _CfprCapabilitySystemLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 13)
)
if mibBuilder.loadTexts:
    cfprCapabilitySystemLimitsTable.setStatus("current")
_CfprCapabilitySystemLimitsEntry_Object = MibTableRow
cfprCapabilitySystemLimitsEntry = _CfprCapabilitySystemLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 13, 1)
)
cfprCapabilitySystemLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilitySystemLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilitySystemLimitsEntry.setStatus("current")
_CfprCapabilitySystemLimitsInstanceId_Type = CfprManagedObjectId
_CfprCapabilitySystemLimitsInstanceId_Object = MibTableColumn
cfprCapabilitySystemLimitsInstanceId = _CfprCapabilitySystemLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 13, 1, 1),
    _CfprCapabilitySystemLimitsInstanceId_Type()
)
cfprCapabilitySystemLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilitySystemLimitsInstanceId.setStatus("current")
_CfprCapabilitySystemLimitsDn_Type = CfprManagedObjectDn
_CfprCapabilitySystemLimitsDn_Object = MibTableColumn
cfprCapabilitySystemLimitsDn = _CfprCapabilitySystemLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 13, 1, 2),
    _CfprCapabilitySystemLimitsDn_Type()
)
cfprCapabilitySystemLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilitySystemLimitsDn.setStatus("current")
_CfprCapabilitySystemLimitsRn_Type = SnmpAdminString
_CfprCapabilitySystemLimitsRn_Object = MibTableColumn
cfprCapabilitySystemLimitsRn = _CfprCapabilitySystemLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 13, 1, 3),
    _CfprCapabilitySystemLimitsRn_Type()
)
cfprCapabilitySystemLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilitySystemLimitsRn.setStatus("current")
_CfprCapabilityUpdateTable_Object = MibTable
cfprCapabilityUpdateTable = _CfprCapabilityUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14)
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdateTable.setStatus("current")
_CfprCapabilityUpdateEntry_Object = MibTableRow
cfprCapabilityUpdateEntry = _CfprCapabilityUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1)
)
cfprCapabilityUpdateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityUpdateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdateEntry.setStatus("current")
_CfprCapabilityUpdateInstanceId_Type = CfprManagedObjectId
_CfprCapabilityUpdateInstanceId_Object = MibTableColumn
cfprCapabilityUpdateInstanceId = _CfprCapabilityUpdateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1, 1),
    _CfprCapabilityUpdateInstanceId_Type()
)
cfprCapabilityUpdateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityUpdateInstanceId.setStatus("current")
_CfprCapabilityUpdateDn_Type = CfprManagedObjectDn
_CfprCapabilityUpdateDn_Object = MibTableColumn
cfprCapabilityUpdateDn = _CfprCapabilityUpdateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1, 2),
    _CfprCapabilityUpdateDn_Type()
)
cfprCapabilityUpdateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdateDn.setStatus("current")
_CfprCapabilityUpdateRn_Type = SnmpAdminString
_CfprCapabilityUpdateRn_Object = MibTableColumn
cfprCapabilityUpdateRn = _CfprCapabilityUpdateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1, 3),
    _CfprCapabilityUpdateRn_Type()
)
cfprCapabilityUpdateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdateRn.setStatus("current")
_CfprCapabilityUpdateImageName_Type = SnmpAdminString
_CfprCapabilityUpdateImageName_Object = MibTableColumn
cfprCapabilityUpdateImageName = _CfprCapabilityUpdateImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1, 4),
    _CfprCapabilityUpdateImageName_Type()
)
cfprCapabilityUpdateImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdateImageName.setStatus("current")
_CfprCapabilityUpdateUpdateTs_Type = DateAndTime
_CfprCapabilityUpdateUpdateTs_Object = MibTableColumn
cfprCapabilityUpdateUpdateTs = _CfprCapabilityUpdateUpdateTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1, 5),
    _CfprCapabilityUpdateUpdateTs_Type()
)
cfprCapabilityUpdateUpdateTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdateUpdateTs.setStatus("current")
_CfprCapabilityUpdateVersion_Type = SnmpAdminString
_CfprCapabilityUpdateVersion_Object = MibTableColumn
cfprCapabilityUpdateVersion = _CfprCapabilityUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 14, 1, 6),
    _CfprCapabilityUpdateVersion_Type()
)
cfprCapabilityUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdateVersion.setStatus("current")
_CfprCapabilityUpdaterTable_Object = MibTable
cfprCapabilityUpdaterTable = _CfprCapabilityUpdaterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15)
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterTable.setStatus("current")
_CfprCapabilityUpdaterEntry_Object = MibTableRow
cfprCapabilityUpdaterEntry = _CfprCapabilityUpdaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1)
)
cfprCapabilityUpdaterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityUpdaterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterEntry.setStatus("current")
_CfprCapabilityUpdaterInstanceId_Type = CfprManagedObjectId
_CfprCapabilityUpdaterInstanceId_Object = MibTableColumn
cfprCapabilityUpdaterInstanceId = _CfprCapabilityUpdaterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 1),
    _CfprCapabilityUpdaterInstanceId_Type()
)
cfprCapabilityUpdaterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterInstanceId.setStatus("current")
_CfprCapabilityUpdaterDn_Type = CfprManagedObjectDn
_CfprCapabilityUpdaterDn_Object = MibTableColumn
cfprCapabilityUpdaterDn = _CfprCapabilityUpdaterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 2),
    _CfprCapabilityUpdaterDn_Type()
)
cfprCapabilityUpdaterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterDn.setStatus("current")
_CfprCapabilityUpdaterRn_Type = SnmpAdminString
_CfprCapabilityUpdaterRn_Object = MibTableColumn
cfprCapabilityUpdaterRn = _CfprCapabilityUpdaterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 3),
    _CfprCapabilityUpdaterRn_Type()
)
cfprCapabilityUpdaterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterRn.setStatus("current")
_CfprCapabilityUpdaterAdminState_Type = CfprCapabilityAdminState
_CfprCapabilityUpdaterAdminState_Object = MibTableColumn
cfprCapabilityUpdaterAdminState = _CfprCapabilityUpdaterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 4),
    _CfprCapabilityUpdaterAdminState_Type()
)
cfprCapabilityUpdaterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterAdminState.setStatus("current")
_CfprCapabilityUpdaterFileName_Type = SnmpAdminString
_CfprCapabilityUpdaterFileName_Object = MibTableColumn
cfprCapabilityUpdaterFileName = _CfprCapabilityUpdaterFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 5),
    _CfprCapabilityUpdaterFileName_Type()
)
cfprCapabilityUpdaterFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFileName.setStatus("current")
_CfprCapabilityUpdaterFsmDescr_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmDescr_Object = MibTableColumn
cfprCapabilityUpdaterFsmDescr = _CfprCapabilityUpdaterFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 6),
    _CfprCapabilityUpdaterFsmDescr_Type()
)
cfprCapabilityUpdaterFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmDescr.setStatus("current")
_CfprCapabilityUpdaterFsmPrev_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmPrev_Object = MibTableColumn
cfprCapabilityUpdaterFsmPrev = _CfprCapabilityUpdaterFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 7),
    _CfprCapabilityUpdaterFsmPrev_Type()
)
cfprCapabilityUpdaterFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmPrev.setStatus("current")
_CfprCapabilityUpdaterFsmProgr_Type = Gauge32
_CfprCapabilityUpdaterFsmProgr_Object = MibTableColumn
cfprCapabilityUpdaterFsmProgr = _CfprCapabilityUpdaterFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 8),
    _CfprCapabilityUpdaterFsmProgr_Type()
)
cfprCapabilityUpdaterFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmProgr.setStatus("current")
_CfprCapabilityUpdaterFsmRmtInvErrCode_Type = Gauge32
_CfprCapabilityUpdaterFsmRmtInvErrCode_Object = MibTableColumn
cfprCapabilityUpdaterFsmRmtInvErrCode = _CfprCapabilityUpdaterFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 9),
    _CfprCapabilityUpdaterFsmRmtInvErrCode_Type()
)
cfprCapabilityUpdaterFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRmtInvErrCode.setStatus("current")
_CfprCapabilityUpdaterFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmRmtInvErrDescr_Object = MibTableColumn
cfprCapabilityUpdaterFsmRmtInvErrDescr = _CfprCapabilityUpdaterFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 10),
    _CfprCapabilityUpdaterFsmRmtInvErrDescr_Type()
)
cfprCapabilityUpdaterFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRmtInvErrDescr.setStatus("current")
_CfprCapabilityUpdaterFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprCapabilityUpdaterFsmRmtInvRslt_Object = MibTableColumn
cfprCapabilityUpdaterFsmRmtInvRslt = _CfprCapabilityUpdaterFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 11),
    _CfprCapabilityUpdaterFsmRmtInvRslt_Type()
)
cfprCapabilityUpdaterFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRmtInvRslt.setStatus("current")
_CfprCapabilityUpdaterFsmStageDescr_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmStageDescr_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageDescr = _CfprCapabilityUpdaterFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 12),
    _CfprCapabilityUpdaterFsmStageDescr_Type()
)
cfprCapabilityUpdaterFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageDescr.setStatus("current")
_CfprCapabilityUpdaterFsmStamp_Type = DateAndTime
_CfprCapabilityUpdaterFsmStamp_Object = MibTableColumn
cfprCapabilityUpdaterFsmStamp = _CfprCapabilityUpdaterFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 13),
    _CfprCapabilityUpdaterFsmStamp_Type()
)
cfprCapabilityUpdaterFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStamp.setStatus("current")
_CfprCapabilityUpdaterFsmStatus_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmStatus_Object = MibTableColumn
cfprCapabilityUpdaterFsmStatus = _CfprCapabilityUpdaterFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 14),
    _CfprCapabilityUpdaterFsmStatus_Type()
)
cfprCapabilityUpdaterFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStatus.setStatus("current")
_CfprCapabilityUpdaterFsmTry_Type = Gauge32
_CfprCapabilityUpdaterFsmTry_Object = MibTableColumn
cfprCapabilityUpdaterFsmTry = _CfprCapabilityUpdaterFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 15),
    _CfprCapabilityUpdaterFsmTry_Type()
)
cfprCapabilityUpdaterFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTry.setStatus("current")
_CfprCapabilityUpdaterImageName_Type = SnmpAdminString
_CfprCapabilityUpdaterImageName_Object = MibTableColumn
cfprCapabilityUpdaterImageName = _CfprCapabilityUpdaterImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 16),
    _CfprCapabilityUpdaterImageName_Type()
)
cfprCapabilityUpdaterImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterImageName.setStatus("current")
_CfprCapabilityUpdaterOperState_Type = CfprCapabilityOperStatus
_CfprCapabilityUpdaterOperState_Object = MibTableColumn
cfprCapabilityUpdaterOperState = _CfprCapabilityUpdaterOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 17),
    _CfprCapabilityUpdaterOperState_Type()
)
cfprCapabilityUpdaterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterOperState.setStatus("current")
_CfprCapabilityUpdaterProtocol_Type = CfprFirmwareTransport
_CfprCapabilityUpdaterProtocol_Object = MibTableColumn
cfprCapabilityUpdaterProtocol = _CfprCapabilityUpdaterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 18),
    _CfprCapabilityUpdaterProtocol_Type()
)
cfprCapabilityUpdaterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterProtocol.setStatus("current")
_CfprCapabilityUpdaterPwd_Type = SnmpAdminString
_CfprCapabilityUpdaterPwd_Object = MibTableColumn
cfprCapabilityUpdaterPwd = _CfprCapabilityUpdaterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 19),
    _CfprCapabilityUpdaterPwd_Type()
)
cfprCapabilityUpdaterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterPwd.setStatus("current")
_CfprCapabilityUpdaterRemotePath_Type = SnmpAdminString
_CfprCapabilityUpdaterRemotePath_Object = MibTableColumn
cfprCapabilityUpdaterRemotePath = _CfprCapabilityUpdaterRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 20),
    _CfprCapabilityUpdaterRemotePath_Type()
)
cfprCapabilityUpdaterRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterRemotePath.setStatus("current")
_CfprCapabilityUpdaterServer_Type = SnmpAdminString
_CfprCapabilityUpdaterServer_Object = MibTableColumn
cfprCapabilityUpdaterServer = _CfprCapabilityUpdaterServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 21),
    _CfprCapabilityUpdaterServer_Type()
)
cfprCapabilityUpdaterServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterServer.setStatus("current")
_CfprCapabilityUpdaterUser_Type = SnmpAdminString
_CfprCapabilityUpdaterUser_Object = MibTableColumn
cfprCapabilityUpdaterUser = _CfprCapabilityUpdaterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 22),
    _CfprCapabilityUpdaterUser_Type()
)
cfprCapabilityUpdaterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterUser.setStatus("current")
_CfprCapabilityUpdaterVersion_Type = SnmpAdminString
_CfprCapabilityUpdaterVersion_Object = MibTableColumn
cfprCapabilityUpdaterVersion = _CfprCapabilityUpdaterVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 15, 1, 23),
    _CfprCapabilityUpdaterVersion_Type()
)
cfprCapabilityUpdaterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterVersion.setStatus("current")
_CfprCapabilityUpdaterFsmTable_Object = MibTable
cfprCapabilityUpdaterFsmTable = _CfprCapabilityUpdaterFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16)
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTable.setStatus("current")
_CfprCapabilityUpdaterFsmEntry_Object = MibTableRow
cfprCapabilityUpdaterFsmEntry = _CfprCapabilityUpdaterFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1)
)
cfprCapabilityUpdaterFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityUpdaterFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmEntry.setStatus("current")
_CfprCapabilityUpdaterFsmInstanceId_Type = CfprManagedObjectId
_CfprCapabilityUpdaterFsmInstanceId_Object = MibTableColumn
cfprCapabilityUpdaterFsmInstanceId = _CfprCapabilityUpdaterFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 1),
    _CfprCapabilityUpdaterFsmInstanceId_Type()
)
cfprCapabilityUpdaterFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmInstanceId.setStatus("current")
_CfprCapabilityUpdaterFsmDn_Type = CfprManagedObjectDn
_CfprCapabilityUpdaterFsmDn_Object = MibTableColumn
cfprCapabilityUpdaterFsmDn = _CfprCapabilityUpdaterFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 2),
    _CfprCapabilityUpdaterFsmDn_Type()
)
cfprCapabilityUpdaterFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmDn.setStatus("current")
_CfprCapabilityUpdaterFsmRn_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmRn_Object = MibTableColumn
cfprCapabilityUpdaterFsmRn = _CfprCapabilityUpdaterFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 3),
    _CfprCapabilityUpdaterFsmRn_Type()
)
cfprCapabilityUpdaterFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRn.setStatus("current")
_CfprCapabilityUpdaterFsmCompletionTime_Type = DateAndTime
_CfprCapabilityUpdaterFsmCompletionTime_Object = MibTableColumn
cfprCapabilityUpdaterFsmCompletionTime = _CfprCapabilityUpdaterFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 4),
    _CfprCapabilityUpdaterFsmCompletionTime_Type()
)
cfprCapabilityUpdaterFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmCompletionTime.setStatus("current")
_CfprCapabilityUpdaterFsmCurrentFsm_Type = CfprCapabilityUpdaterFsmCurrentFsm
_CfprCapabilityUpdaterFsmCurrentFsm_Object = MibTableColumn
cfprCapabilityUpdaterFsmCurrentFsm = _CfprCapabilityUpdaterFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 5),
    _CfprCapabilityUpdaterFsmCurrentFsm_Type()
)
cfprCapabilityUpdaterFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmCurrentFsm.setStatus("current")
_CfprCapabilityUpdaterFsmDescrData_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmDescrData_Object = MibTableColumn
cfprCapabilityUpdaterFsmDescrData = _CfprCapabilityUpdaterFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 6),
    _CfprCapabilityUpdaterFsmDescrData_Type()
)
cfprCapabilityUpdaterFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmDescrData.setStatus("current")
_CfprCapabilityUpdaterFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprCapabilityUpdaterFsmFsmStatus_Object = MibTableColumn
cfprCapabilityUpdaterFsmFsmStatus = _CfprCapabilityUpdaterFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 7),
    _CfprCapabilityUpdaterFsmFsmStatus_Type()
)
cfprCapabilityUpdaterFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmFsmStatus.setStatus("current")
_CfprCapabilityUpdaterFsmProgress_Type = Gauge32
_CfprCapabilityUpdaterFsmProgress_Object = MibTableColumn
cfprCapabilityUpdaterFsmProgress = _CfprCapabilityUpdaterFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 8),
    _CfprCapabilityUpdaterFsmProgress_Type()
)
cfprCapabilityUpdaterFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmProgress.setStatus("current")
_CfprCapabilityUpdaterFsmRmtErrCode_Type = Gauge32
_CfprCapabilityUpdaterFsmRmtErrCode_Object = MibTableColumn
cfprCapabilityUpdaterFsmRmtErrCode = _CfprCapabilityUpdaterFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 9),
    _CfprCapabilityUpdaterFsmRmtErrCode_Type()
)
cfprCapabilityUpdaterFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRmtErrCode.setStatus("current")
_CfprCapabilityUpdaterFsmRmtErrDescr_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmRmtErrDescr_Object = MibTableColumn
cfprCapabilityUpdaterFsmRmtErrDescr = _CfprCapabilityUpdaterFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 10),
    _CfprCapabilityUpdaterFsmRmtErrDescr_Type()
)
cfprCapabilityUpdaterFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRmtErrDescr.setStatus("current")
_CfprCapabilityUpdaterFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprCapabilityUpdaterFsmRmtRslt_Object = MibTableColumn
cfprCapabilityUpdaterFsmRmtRslt = _CfprCapabilityUpdaterFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 16, 1, 11),
    _CfprCapabilityUpdaterFsmRmtRslt_Type()
)
cfprCapabilityUpdaterFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmRmtRslt.setStatus("current")
_CfprCapabilityUpdaterFsmStageTable_Object = MibTable
cfprCapabilityUpdaterFsmStageTable = _CfprCapabilityUpdaterFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17)
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageTable.setStatus("current")
_CfprCapabilityUpdaterFsmStageEntry_Object = MibTableRow
cfprCapabilityUpdaterFsmStageEntry = _CfprCapabilityUpdaterFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1)
)
cfprCapabilityUpdaterFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityUpdaterFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageEntry.setStatus("current")
_CfprCapabilityUpdaterFsmStageInstanceId_Type = CfprManagedObjectId
_CfprCapabilityUpdaterFsmStageInstanceId_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageInstanceId = _CfprCapabilityUpdaterFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 1),
    _CfprCapabilityUpdaterFsmStageInstanceId_Type()
)
cfprCapabilityUpdaterFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageInstanceId.setStatus("current")
_CfprCapabilityUpdaterFsmStageDn_Type = CfprManagedObjectDn
_CfprCapabilityUpdaterFsmStageDn_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageDn = _CfprCapabilityUpdaterFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 2),
    _CfprCapabilityUpdaterFsmStageDn_Type()
)
cfprCapabilityUpdaterFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageDn.setStatus("current")
_CfprCapabilityUpdaterFsmStageRn_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmStageRn_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageRn = _CfprCapabilityUpdaterFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 3),
    _CfprCapabilityUpdaterFsmStageRn_Type()
)
cfprCapabilityUpdaterFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageRn.setStatus("current")
_CfprCapabilityUpdaterFsmStageDescrData_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmStageDescrData_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageDescrData = _CfprCapabilityUpdaterFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 4),
    _CfprCapabilityUpdaterFsmStageDescrData_Type()
)
cfprCapabilityUpdaterFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageDescrData.setStatus("current")
_CfprCapabilityUpdaterFsmStageLastUpdateTime_Type = DateAndTime
_CfprCapabilityUpdaterFsmStageLastUpdateTime_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageLastUpdateTime = _CfprCapabilityUpdaterFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 5),
    _CfprCapabilityUpdaterFsmStageLastUpdateTime_Type()
)
cfprCapabilityUpdaterFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageLastUpdateTime.setStatus("current")
_CfprCapabilityUpdaterFsmStageName_Type = CfprCapabilityUpdaterFsmStageName
_CfprCapabilityUpdaterFsmStageName_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageName = _CfprCapabilityUpdaterFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 6),
    _CfprCapabilityUpdaterFsmStageName_Type()
)
cfprCapabilityUpdaterFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageName.setStatus("current")
_CfprCapabilityUpdaterFsmStageOrder_Type = Gauge32
_CfprCapabilityUpdaterFsmStageOrder_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageOrder = _CfprCapabilityUpdaterFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 7),
    _CfprCapabilityUpdaterFsmStageOrder_Type()
)
cfprCapabilityUpdaterFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageOrder.setStatus("current")
_CfprCapabilityUpdaterFsmStageRetry_Type = Gauge32
_CfprCapabilityUpdaterFsmStageRetry_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageRetry = _CfprCapabilityUpdaterFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 8),
    _CfprCapabilityUpdaterFsmStageRetry_Type()
)
cfprCapabilityUpdaterFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageRetry.setStatus("current")
_CfprCapabilityUpdaterFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprCapabilityUpdaterFsmStageStageStatus_Object = MibTableColumn
cfprCapabilityUpdaterFsmStageStageStatus = _CfprCapabilityUpdaterFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 17, 1, 9),
    _CfprCapabilityUpdaterFsmStageStageStatus_Type()
)
cfprCapabilityUpdaterFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmStageStageStatus.setStatus("current")
_CfprCapabilityUpdaterFsmTaskTable_Object = MibTable
cfprCapabilityUpdaterFsmTaskTable = _CfprCapabilityUpdaterFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18)
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskTable.setStatus("current")
_CfprCapabilityUpdaterFsmTaskEntry_Object = MibTableRow
cfprCapabilityUpdaterFsmTaskEntry = _CfprCapabilityUpdaterFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1)
)
cfprCapabilityUpdaterFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-CAPABILITY-MIB", "cfprCapabilityUpdaterFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskEntry.setStatus("current")
_CfprCapabilityUpdaterFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprCapabilityUpdaterFsmTaskInstanceId_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskInstanceId = _CfprCapabilityUpdaterFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 1),
    _CfprCapabilityUpdaterFsmTaskInstanceId_Type()
)
cfprCapabilityUpdaterFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskInstanceId.setStatus("current")
_CfprCapabilityUpdaterFsmTaskDn_Type = CfprManagedObjectDn
_CfprCapabilityUpdaterFsmTaskDn_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskDn = _CfprCapabilityUpdaterFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 2),
    _CfprCapabilityUpdaterFsmTaskDn_Type()
)
cfprCapabilityUpdaterFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskDn.setStatus("current")
_CfprCapabilityUpdaterFsmTaskRn_Type = SnmpAdminString
_CfprCapabilityUpdaterFsmTaskRn_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskRn = _CfprCapabilityUpdaterFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 3),
    _CfprCapabilityUpdaterFsmTaskRn_Type()
)
cfprCapabilityUpdaterFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskRn.setStatus("current")
_CfprCapabilityUpdaterFsmTaskCompletion_Type = CfprFsmCompletion
_CfprCapabilityUpdaterFsmTaskCompletion_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskCompletion = _CfprCapabilityUpdaterFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 4),
    _CfprCapabilityUpdaterFsmTaskCompletion_Type()
)
cfprCapabilityUpdaterFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskCompletion.setStatus("current")
_CfprCapabilityUpdaterFsmTaskFlags_Type = CfprFsmFlags
_CfprCapabilityUpdaterFsmTaskFlags_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskFlags = _CfprCapabilityUpdaterFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 5),
    _CfprCapabilityUpdaterFsmTaskFlags_Type()
)
cfprCapabilityUpdaterFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskFlags.setStatus("current")
_CfprCapabilityUpdaterFsmTaskItem_Type = CfprCapabilityUpdaterFsmTaskItem
_CfprCapabilityUpdaterFsmTaskItem_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskItem = _CfprCapabilityUpdaterFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 6),
    _CfprCapabilityUpdaterFsmTaskItem_Type()
)
cfprCapabilityUpdaterFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskItem.setStatus("current")
_CfprCapabilityUpdaterFsmTaskSeqId_Type = Gauge32
_CfprCapabilityUpdaterFsmTaskSeqId_Object = MibTableColumn
cfprCapabilityUpdaterFsmTaskSeqId = _CfprCapabilityUpdaterFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 8, 18, 1, 7),
    _CfprCapabilityUpdaterFsmTaskSeqId_Type()
)
cfprCapabilityUpdaterFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprCapabilityUpdaterFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-CAPABILITY-MIB",
    **{"cfprCapabilityObjects": cfprCapabilityObjects,
       "cfprCapabilityCatalogueTable": cfprCapabilityCatalogueTable,
       "cfprCapabilityCatalogueEntry": cfprCapabilityCatalogueEntry,
       "cfprCapabilityCatalogueInstanceId": cfprCapabilityCatalogueInstanceId,
       "cfprCapabilityCatalogueDn": cfprCapabilityCatalogueDn,
       "cfprCapabilityCatalogueRn": cfprCapabilityCatalogueRn,
       "cfprCapabilityCatalogueFileParseFailures": cfprCapabilityCatalogueFileParseFailures,
       "cfprCapabilityCatalogueFilesParsed": cfprCapabilityCatalogueFilesParsed,
       "cfprCapabilityCatalogueFsmDescr": cfprCapabilityCatalogueFsmDescr,
       "cfprCapabilityCatalogueFsmPrev": cfprCapabilityCatalogueFsmPrev,
       "cfprCapabilityCatalogueFsmProgr": cfprCapabilityCatalogueFsmProgr,
       "cfprCapabilityCatalogueFsmRmtInvErrCode": cfprCapabilityCatalogueFsmRmtInvErrCode,
       "cfprCapabilityCatalogueFsmRmtInvErrDescr": cfprCapabilityCatalogueFsmRmtInvErrDescr,
       "cfprCapabilityCatalogueFsmRmtInvRslt": cfprCapabilityCatalogueFsmRmtInvRslt,
       "cfprCapabilityCatalogueFsmStageDescr": cfprCapabilityCatalogueFsmStageDescr,
       "cfprCapabilityCatalogueFsmStamp": cfprCapabilityCatalogueFsmStamp,
       "cfprCapabilityCatalogueFsmStatus": cfprCapabilityCatalogueFsmStatus,
       "cfprCapabilityCatalogueFsmTry": cfprCapabilityCatalogueFsmTry,
       "cfprCapabilityCatalogueLoadErrors": cfprCapabilityCatalogueLoadErrors,
       "cfprCapabilityCatalogueLoadWarnings": cfprCapabilityCatalogueLoadWarnings,
       "cfprCapabilityCatalogueProviderLoadFailures": cfprCapabilityCatalogueProviderLoadFailures,
       "cfprCapabilityCatalogueProvidersLoaded": cfprCapabilityCatalogueProvidersLoaded,
       "cfprCapabilityCatalogueVersion": cfprCapabilityCatalogueVersion,
       "cfprCapabilityCatalogueBiosTokenVersion": cfprCapabilityCatalogueBiosTokenVersion,
       "cfprCapabilityCatalogueFsmTable": cfprCapabilityCatalogueFsmTable,
       "cfprCapabilityCatalogueFsmEntry": cfprCapabilityCatalogueFsmEntry,
       "cfprCapabilityCatalogueFsmInstanceId": cfprCapabilityCatalogueFsmInstanceId,
       "cfprCapabilityCatalogueFsmDn": cfprCapabilityCatalogueFsmDn,
       "cfprCapabilityCatalogueFsmRn": cfprCapabilityCatalogueFsmRn,
       "cfprCapabilityCatalogueFsmCompletionTime": cfprCapabilityCatalogueFsmCompletionTime,
       "cfprCapabilityCatalogueFsmCurrentFsm": cfprCapabilityCatalogueFsmCurrentFsm,
       "cfprCapabilityCatalogueFsmDescrData": cfprCapabilityCatalogueFsmDescrData,
       "cfprCapabilityCatalogueFsmFsmStatus": cfprCapabilityCatalogueFsmFsmStatus,
       "cfprCapabilityCatalogueFsmProgress": cfprCapabilityCatalogueFsmProgress,
       "cfprCapabilityCatalogueFsmRmtErrCode": cfprCapabilityCatalogueFsmRmtErrCode,
       "cfprCapabilityCatalogueFsmRmtErrDescr": cfprCapabilityCatalogueFsmRmtErrDescr,
       "cfprCapabilityCatalogueFsmRmtRslt": cfprCapabilityCatalogueFsmRmtRslt,
       "cfprCapabilityCatalogueFsmStageTable": cfprCapabilityCatalogueFsmStageTable,
       "cfprCapabilityCatalogueFsmStageEntry": cfprCapabilityCatalogueFsmStageEntry,
       "cfprCapabilityCatalogueFsmStageInstanceId": cfprCapabilityCatalogueFsmStageInstanceId,
       "cfprCapabilityCatalogueFsmStageDn": cfprCapabilityCatalogueFsmStageDn,
       "cfprCapabilityCatalogueFsmStageRn": cfprCapabilityCatalogueFsmStageRn,
       "cfprCapabilityCatalogueFsmStageDescrData": cfprCapabilityCatalogueFsmStageDescrData,
       "cfprCapabilityCatalogueFsmStageLastUpdateTime": cfprCapabilityCatalogueFsmStageLastUpdateTime,
       "cfprCapabilityCatalogueFsmStageName": cfprCapabilityCatalogueFsmStageName,
       "cfprCapabilityCatalogueFsmStageOrder": cfprCapabilityCatalogueFsmStageOrder,
       "cfprCapabilityCatalogueFsmStageRetry": cfprCapabilityCatalogueFsmStageRetry,
       "cfprCapabilityCatalogueFsmStageStageStatus": cfprCapabilityCatalogueFsmStageStageStatus,
       "cfprCapabilityCatalogueFsmTaskTable": cfprCapabilityCatalogueFsmTaskTable,
       "cfprCapabilityCatalogueFsmTaskEntry": cfprCapabilityCatalogueFsmTaskEntry,
       "cfprCapabilityCatalogueFsmTaskInstanceId": cfprCapabilityCatalogueFsmTaskInstanceId,
       "cfprCapabilityCatalogueFsmTaskDn": cfprCapabilityCatalogueFsmTaskDn,
       "cfprCapabilityCatalogueFsmTaskRn": cfprCapabilityCatalogueFsmTaskRn,
       "cfprCapabilityCatalogueFsmTaskCompletion": cfprCapabilityCatalogueFsmTaskCompletion,
       "cfprCapabilityCatalogueFsmTaskFlags": cfprCapabilityCatalogueFsmTaskFlags,
       "cfprCapabilityCatalogueFsmTaskItem": cfprCapabilityCatalogueFsmTaskItem,
       "cfprCapabilityCatalogueFsmTaskSeqId": cfprCapabilityCatalogueFsmTaskSeqId,
       "cfprCapabilityEpTable": cfprCapabilityEpTable,
       "cfprCapabilityEpEntry": cfprCapabilityEpEntry,
       "cfprCapabilityEpInstanceId": cfprCapabilityEpInstanceId,
       "cfprCapabilityEpDn": cfprCapabilityEpDn,
       "cfprCapabilityEpRn": cfprCapabilityEpRn,
       "cfprCapabilityFeatureLimitsTable": cfprCapabilityFeatureLimitsTable,
       "cfprCapabilityFeatureLimitsEntry": cfprCapabilityFeatureLimitsEntry,
       "cfprCapabilityFeatureLimitsInstanceId": cfprCapabilityFeatureLimitsInstanceId,
       "cfprCapabilityFeatureLimitsDn": cfprCapabilityFeatureLimitsDn,
       "cfprCapabilityFeatureLimitsRn": cfprCapabilityFeatureLimitsRn,
       "cfprCapabilityFeatureLimitsDescr": cfprCapabilityFeatureLimitsDescr,
       "cfprCapabilityFeatureLimitsFeatureStatus": cfprCapabilityFeatureLimitsFeatureStatus,
       "cfprCapabilityFeatureLimitsLimit": cfprCapabilityFeatureLimitsLimit,
       "cfprCapabilityFeatureLimitsName": cfprCapabilityFeatureLimitsName,
       "cfprCapabilityFeatureLimitsPlatform": cfprCapabilityFeatureLimitsPlatform,
       "cfprCapabilityMgmtExtensionTable": cfprCapabilityMgmtExtensionTable,
       "cfprCapabilityMgmtExtensionEntry": cfprCapabilityMgmtExtensionEntry,
       "cfprCapabilityMgmtExtensionInstanceId": cfprCapabilityMgmtExtensionInstanceId,
       "cfprCapabilityMgmtExtensionDn": cfprCapabilityMgmtExtensionDn,
       "cfprCapabilityMgmtExtensionRn": cfprCapabilityMgmtExtensionRn,
       "cfprCapabilityMgmtExtensionFsmDescr": cfprCapabilityMgmtExtensionFsmDescr,
       "cfprCapabilityMgmtExtensionFsmPrev": cfprCapabilityMgmtExtensionFsmPrev,
       "cfprCapabilityMgmtExtensionFsmProgr": cfprCapabilityMgmtExtensionFsmProgr,
       "cfprCapabilityMgmtExtensionFsmRmtInvErrCode": cfprCapabilityMgmtExtensionFsmRmtInvErrCode,
       "cfprCapabilityMgmtExtensionFsmRmtInvErrDescr": cfprCapabilityMgmtExtensionFsmRmtInvErrDescr,
       "cfprCapabilityMgmtExtensionFsmRmtInvRslt": cfprCapabilityMgmtExtensionFsmRmtInvRslt,
       "cfprCapabilityMgmtExtensionFsmStageDescr": cfprCapabilityMgmtExtensionFsmStageDescr,
       "cfprCapabilityMgmtExtensionFsmStamp": cfprCapabilityMgmtExtensionFsmStamp,
       "cfprCapabilityMgmtExtensionFsmStatus": cfprCapabilityMgmtExtensionFsmStatus,
       "cfprCapabilityMgmtExtensionFsmTry": cfprCapabilityMgmtExtensionFsmTry,
       "cfprCapabilityMgmtExtensionFsmTable": cfprCapabilityMgmtExtensionFsmTable,
       "cfprCapabilityMgmtExtensionFsmEntry": cfprCapabilityMgmtExtensionFsmEntry,
       "cfprCapabilityMgmtExtensionFsmInstanceId": cfprCapabilityMgmtExtensionFsmInstanceId,
       "cfprCapabilityMgmtExtensionFsmDn": cfprCapabilityMgmtExtensionFsmDn,
       "cfprCapabilityMgmtExtensionFsmRn": cfprCapabilityMgmtExtensionFsmRn,
       "cfprCapabilityMgmtExtensionFsmCompletionTime": cfprCapabilityMgmtExtensionFsmCompletionTime,
       "cfprCapabilityMgmtExtensionFsmCurrentFsm": cfprCapabilityMgmtExtensionFsmCurrentFsm,
       "cfprCapabilityMgmtExtensionFsmDescrData": cfprCapabilityMgmtExtensionFsmDescrData,
       "cfprCapabilityMgmtExtensionFsmFsmStatus": cfprCapabilityMgmtExtensionFsmFsmStatus,
       "cfprCapabilityMgmtExtensionFsmProgress": cfprCapabilityMgmtExtensionFsmProgress,
       "cfprCapabilityMgmtExtensionFsmRmtErrCode": cfprCapabilityMgmtExtensionFsmRmtErrCode,
       "cfprCapabilityMgmtExtensionFsmRmtErrDescr": cfprCapabilityMgmtExtensionFsmRmtErrDescr,
       "cfprCapabilityMgmtExtensionFsmRmtRslt": cfprCapabilityMgmtExtensionFsmRmtRslt,
       "cfprCapabilityMgmtExtensionFsmStageTable": cfprCapabilityMgmtExtensionFsmStageTable,
       "cfprCapabilityMgmtExtensionFsmStageEntry": cfprCapabilityMgmtExtensionFsmStageEntry,
       "cfprCapabilityMgmtExtensionFsmStageInstanceId": cfprCapabilityMgmtExtensionFsmStageInstanceId,
       "cfprCapabilityMgmtExtensionFsmStageDn": cfprCapabilityMgmtExtensionFsmStageDn,
       "cfprCapabilityMgmtExtensionFsmStageRn": cfprCapabilityMgmtExtensionFsmStageRn,
       "cfprCapabilityMgmtExtensionFsmStageDescrData": cfprCapabilityMgmtExtensionFsmStageDescrData,
       "cfprCapabilityMgmtExtensionFsmStageLastUpdateTime": cfprCapabilityMgmtExtensionFsmStageLastUpdateTime,
       "cfprCapabilityMgmtExtensionFsmStageName": cfprCapabilityMgmtExtensionFsmStageName,
       "cfprCapabilityMgmtExtensionFsmStageOrder": cfprCapabilityMgmtExtensionFsmStageOrder,
       "cfprCapabilityMgmtExtensionFsmStageRetry": cfprCapabilityMgmtExtensionFsmStageRetry,
       "cfprCapabilityMgmtExtensionFsmStageStageStatus": cfprCapabilityMgmtExtensionFsmStageStageStatus,
       "cfprCapabilityMgmtExtensionFsmTaskTable": cfprCapabilityMgmtExtensionFsmTaskTable,
       "cfprCapabilityMgmtExtensionFsmTaskEntry": cfprCapabilityMgmtExtensionFsmTaskEntry,
       "cfprCapabilityMgmtExtensionFsmTaskInstanceId": cfprCapabilityMgmtExtensionFsmTaskInstanceId,
       "cfprCapabilityMgmtExtensionFsmTaskDn": cfprCapabilityMgmtExtensionFsmTaskDn,
       "cfprCapabilityMgmtExtensionFsmTaskRn": cfprCapabilityMgmtExtensionFsmTaskRn,
       "cfprCapabilityMgmtExtensionFsmTaskCompletion": cfprCapabilityMgmtExtensionFsmTaskCompletion,
       "cfprCapabilityMgmtExtensionFsmTaskFlags": cfprCapabilityMgmtExtensionFsmTaskFlags,
       "cfprCapabilityMgmtExtensionFsmTaskItem": cfprCapabilityMgmtExtensionFsmTaskItem,
       "cfprCapabilityMgmtExtensionFsmTaskSeqId": cfprCapabilityMgmtExtensionFsmTaskSeqId,
       "cfprCapabilityNetworkLimitsTable": cfprCapabilityNetworkLimitsTable,
       "cfprCapabilityNetworkLimitsEntry": cfprCapabilityNetworkLimitsEntry,
       "cfprCapabilityNetworkLimitsInstanceId": cfprCapabilityNetworkLimitsInstanceId,
       "cfprCapabilityNetworkLimitsDn": cfprCapabilityNetworkLimitsDn,
       "cfprCapabilityNetworkLimitsRn": cfprCapabilityNetworkLimitsRn,
       "cfprCapabilityStorageLimitsTable": cfprCapabilityStorageLimitsTable,
       "cfprCapabilityStorageLimitsEntry": cfprCapabilityStorageLimitsEntry,
       "cfprCapabilityStorageLimitsInstanceId": cfprCapabilityStorageLimitsInstanceId,
       "cfprCapabilityStorageLimitsDn": cfprCapabilityStorageLimitsDn,
       "cfprCapabilityStorageLimitsRn": cfprCapabilityStorageLimitsRn,
       "cfprCapabilitySystemLimitsTable": cfprCapabilitySystemLimitsTable,
       "cfprCapabilitySystemLimitsEntry": cfprCapabilitySystemLimitsEntry,
       "cfprCapabilitySystemLimitsInstanceId": cfprCapabilitySystemLimitsInstanceId,
       "cfprCapabilitySystemLimitsDn": cfprCapabilitySystemLimitsDn,
       "cfprCapabilitySystemLimitsRn": cfprCapabilitySystemLimitsRn,
       "cfprCapabilityUpdateTable": cfprCapabilityUpdateTable,
       "cfprCapabilityUpdateEntry": cfprCapabilityUpdateEntry,
       "cfprCapabilityUpdateInstanceId": cfprCapabilityUpdateInstanceId,
       "cfprCapabilityUpdateDn": cfprCapabilityUpdateDn,
       "cfprCapabilityUpdateRn": cfprCapabilityUpdateRn,
       "cfprCapabilityUpdateImageName": cfprCapabilityUpdateImageName,
       "cfprCapabilityUpdateUpdateTs": cfprCapabilityUpdateUpdateTs,
       "cfprCapabilityUpdateVersion": cfprCapabilityUpdateVersion,
       "cfprCapabilityUpdaterTable": cfprCapabilityUpdaterTable,
       "cfprCapabilityUpdaterEntry": cfprCapabilityUpdaterEntry,
       "cfprCapabilityUpdaterInstanceId": cfprCapabilityUpdaterInstanceId,
       "cfprCapabilityUpdaterDn": cfprCapabilityUpdaterDn,
       "cfprCapabilityUpdaterRn": cfprCapabilityUpdaterRn,
       "cfprCapabilityUpdaterAdminState": cfprCapabilityUpdaterAdminState,
       "cfprCapabilityUpdaterFileName": cfprCapabilityUpdaterFileName,
       "cfprCapabilityUpdaterFsmDescr": cfprCapabilityUpdaterFsmDescr,
       "cfprCapabilityUpdaterFsmPrev": cfprCapabilityUpdaterFsmPrev,
       "cfprCapabilityUpdaterFsmProgr": cfprCapabilityUpdaterFsmProgr,
       "cfprCapabilityUpdaterFsmRmtInvErrCode": cfprCapabilityUpdaterFsmRmtInvErrCode,
       "cfprCapabilityUpdaterFsmRmtInvErrDescr": cfprCapabilityUpdaterFsmRmtInvErrDescr,
       "cfprCapabilityUpdaterFsmRmtInvRslt": cfprCapabilityUpdaterFsmRmtInvRslt,
       "cfprCapabilityUpdaterFsmStageDescr": cfprCapabilityUpdaterFsmStageDescr,
       "cfprCapabilityUpdaterFsmStamp": cfprCapabilityUpdaterFsmStamp,
       "cfprCapabilityUpdaterFsmStatus": cfprCapabilityUpdaterFsmStatus,
       "cfprCapabilityUpdaterFsmTry": cfprCapabilityUpdaterFsmTry,
       "cfprCapabilityUpdaterImageName": cfprCapabilityUpdaterImageName,
       "cfprCapabilityUpdaterOperState": cfprCapabilityUpdaterOperState,
       "cfprCapabilityUpdaterProtocol": cfprCapabilityUpdaterProtocol,
       "cfprCapabilityUpdaterPwd": cfprCapabilityUpdaterPwd,
       "cfprCapabilityUpdaterRemotePath": cfprCapabilityUpdaterRemotePath,
       "cfprCapabilityUpdaterServer": cfprCapabilityUpdaterServer,
       "cfprCapabilityUpdaterUser": cfprCapabilityUpdaterUser,
       "cfprCapabilityUpdaterVersion": cfprCapabilityUpdaterVersion,
       "cfprCapabilityUpdaterFsmTable": cfprCapabilityUpdaterFsmTable,
       "cfprCapabilityUpdaterFsmEntry": cfprCapabilityUpdaterFsmEntry,
       "cfprCapabilityUpdaterFsmInstanceId": cfprCapabilityUpdaterFsmInstanceId,
       "cfprCapabilityUpdaterFsmDn": cfprCapabilityUpdaterFsmDn,
       "cfprCapabilityUpdaterFsmRn": cfprCapabilityUpdaterFsmRn,
       "cfprCapabilityUpdaterFsmCompletionTime": cfprCapabilityUpdaterFsmCompletionTime,
       "cfprCapabilityUpdaterFsmCurrentFsm": cfprCapabilityUpdaterFsmCurrentFsm,
       "cfprCapabilityUpdaterFsmDescrData": cfprCapabilityUpdaterFsmDescrData,
       "cfprCapabilityUpdaterFsmFsmStatus": cfprCapabilityUpdaterFsmFsmStatus,
       "cfprCapabilityUpdaterFsmProgress": cfprCapabilityUpdaterFsmProgress,
       "cfprCapabilityUpdaterFsmRmtErrCode": cfprCapabilityUpdaterFsmRmtErrCode,
       "cfprCapabilityUpdaterFsmRmtErrDescr": cfprCapabilityUpdaterFsmRmtErrDescr,
       "cfprCapabilityUpdaterFsmRmtRslt": cfprCapabilityUpdaterFsmRmtRslt,
       "cfprCapabilityUpdaterFsmStageTable": cfprCapabilityUpdaterFsmStageTable,
       "cfprCapabilityUpdaterFsmStageEntry": cfprCapabilityUpdaterFsmStageEntry,
       "cfprCapabilityUpdaterFsmStageInstanceId": cfprCapabilityUpdaterFsmStageInstanceId,
       "cfprCapabilityUpdaterFsmStageDn": cfprCapabilityUpdaterFsmStageDn,
       "cfprCapabilityUpdaterFsmStageRn": cfprCapabilityUpdaterFsmStageRn,
       "cfprCapabilityUpdaterFsmStageDescrData": cfprCapabilityUpdaterFsmStageDescrData,
       "cfprCapabilityUpdaterFsmStageLastUpdateTime": cfprCapabilityUpdaterFsmStageLastUpdateTime,
       "cfprCapabilityUpdaterFsmStageName": cfprCapabilityUpdaterFsmStageName,
       "cfprCapabilityUpdaterFsmStageOrder": cfprCapabilityUpdaterFsmStageOrder,
       "cfprCapabilityUpdaterFsmStageRetry": cfprCapabilityUpdaterFsmStageRetry,
       "cfprCapabilityUpdaterFsmStageStageStatus": cfprCapabilityUpdaterFsmStageStageStatus,
       "cfprCapabilityUpdaterFsmTaskTable": cfprCapabilityUpdaterFsmTaskTable,
       "cfprCapabilityUpdaterFsmTaskEntry": cfprCapabilityUpdaterFsmTaskEntry,
       "cfprCapabilityUpdaterFsmTaskInstanceId": cfprCapabilityUpdaterFsmTaskInstanceId,
       "cfprCapabilityUpdaterFsmTaskDn": cfprCapabilityUpdaterFsmTaskDn,
       "cfprCapabilityUpdaterFsmTaskRn": cfprCapabilityUpdaterFsmTaskRn,
       "cfprCapabilityUpdaterFsmTaskCompletion": cfprCapabilityUpdaterFsmTaskCompletion,
       "cfprCapabilityUpdaterFsmTaskFlags": cfprCapabilityUpdaterFsmTaskFlags,
       "cfprCapabilityUpdaterFsmTaskItem": cfprCapabilityUpdaterFsmTaskItem,
       "cfprCapabilityUpdaterFsmTaskSeqId": cfprCapabilityUpdaterFsmTaskSeqId}
)
