# SNMP MIB module (CISCO-FIREPOWER-AP-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-CAPABILITY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:13 2025
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

(CfprApCapabilityAdminState,
 CfprApCapabilityCatalogueFsmCurrentFsm,
 CfprApCapabilityCatalogueFsmStageName,
 CfprApCapabilityCatalogueFsmTaskItem,
 CfprApCapabilityFeatureStatus,
 CfprApCapabilityMgmtExtensionFsmCurrentFsm,
 CfprApCapabilityMgmtExtensionFsmStageName,
 CfprApCapabilityMgmtExtensionFsmTaskItem,
 CfprApCapabilityOperStatus,
 CfprApCapabilityPlatform,
 CfprApCapabilityUpdaterFsmCurrentFsm,
 CfprApCapabilityUpdaterFsmStageName,
 CfprApCapabilityUpdaterFsmTaskItem,
 CfprApConditionRemoteInvRslt,
 CfprApFirmwareTransport,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApCapabilityAdminState",
    "CfprApCapabilityCatalogueFsmCurrentFsm",
    "CfprApCapabilityCatalogueFsmStageName",
    "CfprApCapabilityCatalogueFsmTaskItem",
    "CfprApCapabilityFeatureStatus",
    "CfprApCapabilityMgmtExtensionFsmCurrentFsm",
    "CfprApCapabilityMgmtExtensionFsmStageName",
    "CfprApCapabilityMgmtExtensionFsmTaskItem",
    "CfprApCapabilityOperStatus",
    "CfprApCapabilityPlatform",
    "CfprApCapabilityUpdaterFsmCurrentFsm",
    "CfprApCapabilityUpdaterFsmStageName",
    "CfprApCapabilityUpdaterFsmTaskItem",
    "CfprApConditionRemoteInvRslt",
    "CfprApFirmwareTransport",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus")

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

cfprApCapabilityObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApCapabilityCatalogueTable_Object = MibTable
cfprApCapabilityCatalogueTable = _CfprApCapabilityCatalogueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueTable.setStatus("current")
_CfprApCapabilityCatalogueEntry_Object = MibTableRow
cfprApCapabilityCatalogueEntry = _CfprApCapabilityCatalogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1)
)
cfprApCapabilityCatalogueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityCatalogueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueEntry.setStatus("current")
_CfprApCapabilityCatalogueInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityCatalogueInstanceId_Object = MibTableColumn
cfprApCapabilityCatalogueInstanceId = _CfprApCapabilityCatalogueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 1),
    _CfprApCapabilityCatalogueInstanceId_Type()
)
cfprApCapabilityCatalogueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueInstanceId.setStatus("current")
_CfprApCapabilityCatalogueDn_Type = CfprApManagedObjectDn
_CfprApCapabilityCatalogueDn_Object = MibTableColumn
cfprApCapabilityCatalogueDn = _CfprApCapabilityCatalogueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 2),
    _CfprApCapabilityCatalogueDn_Type()
)
cfprApCapabilityCatalogueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueDn.setStatus("current")
_CfprApCapabilityCatalogueRn_Type = SnmpAdminString
_CfprApCapabilityCatalogueRn_Object = MibTableColumn
cfprApCapabilityCatalogueRn = _CfprApCapabilityCatalogueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 3),
    _CfprApCapabilityCatalogueRn_Type()
)
cfprApCapabilityCatalogueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueRn.setStatus("current")
_CfprApCapabilityCatalogueFileParseFailures_Type = Gauge32
_CfprApCapabilityCatalogueFileParseFailures_Object = MibTableColumn
cfprApCapabilityCatalogueFileParseFailures = _CfprApCapabilityCatalogueFileParseFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 4),
    _CfprApCapabilityCatalogueFileParseFailures_Type()
)
cfprApCapabilityCatalogueFileParseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFileParseFailures.setStatus("current")
_CfprApCapabilityCatalogueFilesParsed_Type = Gauge32
_CfprApCapabilityCatalogueFilesParsed_Object = MibTableColumn
cfprApCapabilityCatalogueFilesParsed = _CfprApCapabilityCatalogueFilesParsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 5),
    _CfprApCapabilityCatalogueFilesParsed_Type()
)
cfprApCapabilityCatalogueFilesParsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFilesParsed.setStatus("current")
_CfprApCapabilityCatalogueFsmDescr_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmDescr_Object = MibTableColumn
cfprApCapabilityCatalogueFsmDescr = _CfprApCapabilityCatalogueFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 6),
    _CfprApCapabilityCatalogueFsmDescr_Type()
)
cfprApCapabilityCatalogueFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmDescr.setStatus("current")
_CfprApCapabilityCatalogueFsmPrev_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmPrev_Object = MibTableColumn
cfprApCapabilityCatalogueFsmPrev = _CfprApCapabilityCatalogueFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 7),
    _CfprApCapabilityCatalogueFsmPrev_Type()
)
cfprApCapabilityCatalogueFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmPrev.setStatus("current")
_CfprApCapabilityCatalogueFsmProgr_Type = Gauge32
_CfprApCapabilityCatalogueFsmProgr_Object = MibTableColumn
cfprApCapabilityCatalogueFsmProgr = _CfprApCapabilityCatalogueFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 8),
    _CfprApCapabilityCatalogueFsmProgr_Type()
)
cfprApCapabilityCatalogueFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmProgr.setStatus("current")
_CfprApCapabilityCatalogueFsmRmtInvErrCode_Type = Gauge32
_CfprApCapabilityCatalogueFsmRmtInvErrCode_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRmtInvErrCode = _CfprApCapabilityCatalogueFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 9),
    _CfprApCapabilityCatalogueFsmRmtInvErrCode_Type()
)
cfprApCapabilityCatalogueFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRmtInvErrCode.setStatus("current")
_CfprApCapabilityCatalogueFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmRmtInvErrDescr_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRmtInvErrDescr = _CfprApCapabilityCatalogueFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 10),
    _CfprApCapabilityCatalogueFsmRmtInvErrDescr_Type()
)
cfprApCapabilityCatalogueFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRmtInvErrDescr.setStatus("current")
_CfprApCapabilityCatalogueFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCapabilityCatalogueFsmRmtInvRslt_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRmtInvRslt = _CfprApCapabilityCatalogueFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 11),
    _CfprApCapabilityCatalogueFsmRmtInvRslt_Type()
)
cfprApCapabilityCatalogueFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRmtInvRslt.setStatus("current")
_CfprApCapabilityCatalogueFsmStageDescr_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmStageDescr_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageDescr = _CfprApCapabilityCatalogueFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 12),
    _CfprApCapabilityCatalogueFsmStageDescr_Type()
)
cfprApCapabilityCatalogueFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageDescr.setStatus("current")
_CfprApCapabilityCatalogueFsmStamp_Type = DateAndTime
_CfprApCapabilityCatalogueFsmStamp_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStamp = _CfprApCapabilityCatalogueFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 13),
    _CfprApCapabilityCatalogueFsmStamp_Type()
)
cfprApCapabilityCatalogueFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStamp.setStatus("current")
_CfprApCapabilityCatalogueFsmStatus_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmStatus_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStatus = _CfprApCapabilityCatalogueFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 14),
    _CfprApCapabilityCatalogueFsmStatus_Type()
)
cfprApCapabilityCatalogueFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStatus.setStatus("current")
_CfprApCapabilityCatalogueFsmTry_Type = Gauge32
_CfprApCapabilityCatalogueFsmTry_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTry = _CfprApCapabilityCatalogueFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 15),
    _CfprApCapabilityCatalogueFsmTry_Type()
)
cfprApCapabilityCatalogueFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTry.setStatus("current")
_CfprApCapabilityCatalogueLoadErrors_Type = Gauge32
_CfprApCapabilityCatalogueLoadErrors_Object = MibTableColumn
cfprApCapabilityCatalogueLoadErrors = _CfprApCapabilityCatalogueLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 16),
    _CfprApCapabilityCatalogueLoadErrors_Type()
)
cfprApCapabilityCatalogueLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueLoadErrors.setStatus("current")
_CfprApCapabilityCatalogueLoadWarnings_Type = Gauge32
_CfprApCapabilityCatalogueLoadWarnings_Object = MibTableColumn
cfprApCapabilityCatalogueLoadWarnings = _CfprApCapabilityCatalogueLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 17),
    _CfprApCapabilityCatalogueLoadWarnings_Type()
)
cfprApCapabilityCatalogueLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueLoadWarnings.setStatus("current")
_CfprApCapabilityCatalogueProviderLoadFailures_Type = Gauge32
_CfprApCapabilityCatalogueProviderLoadFailures_Object = MibTableColumn
cfprApCapabilityCatalogueProviderLoadFailures = _CfprApCapabilityCatalogueProviderLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 18),
    _CfprApCapabilityCatalogueProviderLoadFailures_Type()
)
cfprApCapabilityCatalogueProviderLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueProviderLoadFailures.setStatus("current")
_CfprApCapabilityCatalogueProvidersLoaded_Type = Gauge32
_CfprApCapabilityCatalogueProvidersLoaded_Object = MibTableColumn
cfprApCapabilityCatalogueProvidersLoaded = _CfprApCapabilityCatalogueProvidersLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 19),
    _CfprApCapabilityCatalogueProvidersLoaded_Type()
)
cfprApCapabilityCatalogueProvidersLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueProvidersLoaded.setStatus("current")
_CfprApCapabilityCatalogueVersion_Type = SnmpAdminString
_CfprApCapabilityCatalogueVersion_Object = MibTableColumn
cfprApCapabilityCatalogueVersion = _CfprApCapabilityCatalogueVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 1, 1, 20),
    _CfprApCapabilityCatalogueVersion_Type()
)
cfprApCapabilityCatalogueVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueVersion.setStatus("current")
_CfprApCapabilityCatalogueFsmTable_Object = MibTable
cfprApCapabilityCatalogueFsmTable = _CfprApCapabilityCatalogueFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTable.setStatus("current")
_CfprApCapabilityCatalogueFsmEntry_Object = MibTableRow
cfprApCapabilityCatalogueFsmEntry = _CfprApCapabilityCatalogueFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1)
)
cfprApCapabilityCatalogueFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityCatalogueFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmEntry.setStatus("current")
_CfprApCapabilityCatalogueFsmInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityCatalogueFsmInstanceId_Object = MibTableColumn
cfprApCapabilityCatalogueFsmInstanceId = _CfprApCapabilityCatalogueFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 1),
    _CfprApCapabilityCatalogueFsmInstanceId_Type()
)
cfprApCapabilityCatalogueFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmInstanceId.setStatus("current")
_CfprApCapabilityCatalogueFsmDn_Type = CfprApManagedObjectDn
_CfprApCapabilityCatalogueFsmDn_Object = MibTableColumn
cfprApCapabilityCatalogueFsmDn = _CfprApCapabilityCatalogueFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 2),
    _CfprApCapabilityCatalogueFsmDn_Type()
)
cfprApCapabilityCatalogueFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmDn.setStatus("current")
_CfprApCapabilityCatalogueFsmRn_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmRn_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRn = _CfprApCapabilityCatalogueFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 3),
    _CfprApCapabilityCatalogueFsmRn_Type()
)
cfprApCapabilityCatalogueFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRn.setStatus("current")
_CfprApCapabilityCatalogueFsmCompletionTime_Type = DateAndTime
_CfprApCapabilityCatalogueFsmCompletionTime_Object = MibTableColumn
cfprApCapabilityCatalogueFsmCompletionTime = _CfprApCapabilityCatalogueFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 4),
    _CfprApCapabilityCatalogueFsmCompletionTime_Type()
)
cfprApCapabilityCatalogueFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmCompletionTime.setStatus("current")
_CfprApCapabilityCatalogueFsmCurrentFsm_Type = CfprApCapabilityCatalogueFsmCurrentFsm
_CfprApCapabilityCatalogueFsmCurrentFsm_Object = MibTableColumn
cfprApCapabilityCatalogueFsmCurrentFsm = _CfprApCapabilityCatalogueFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 5),
    _CfprApCapabilityCatalogueFsmCurrentFsm_Type()
)
cfprApCapabilityCatalogueFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmCurrentFsm.setStatus("current")
_CfprApCapabilityCatalogueFsmDescrData_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmDescrData_Object = MibTableColumn
cfprApCapabilityCatalogueFsmDescrData = _CfprApCapabilityCatalogueFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 6),
    _CfprApCapabilityCatalogueFsmDescrData_Type()
)
cfprApCapabilityCatalogueFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmDescrData.setStatus("current")
_CfprApCapabilityCatalogueFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApCapabilityCatalogueFsmFsmStatus_Object = MibTableColumn
cfprApCapabilityCatalogueFsmFsmStatus = _CfprApCapabilityCatalogueFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 7),
    _CfprApCapabilityCatalogueFsmFsmStatus_Type()
)
cfprApCapabilityCatalogueFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmFsmStatus.setStatus("current")
_CfprApCapabilityCatalogueFsmProgress_Type = Gauge32
_CfprApCapabilityCatalogueFsmProgress_Object = MibTableColumn
cfprApCapabilityCatalogueFsmProgress = _CfprApCapabilityCatalogueFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 8),
    _CfprApCapabilityCatalogueFsmProgress_Type()
)
cfprApCapabilityCatalogueFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmProgress.setStatus("current")
_CfprApCapabilityCatalogueFsmRmtErrCode_Type = Gauge32
_CfprApCapabilityCatalogueFsmRmtErrCode_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRmtErrCode = _CfprApCapabilityCatalogueFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 9),
    _CfprApCapabilityCatalogueFsmRmtErrCode_Type()
)
cfprApCapabilityCatalogueFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRmtErrCode.setStatus("current")
_CfprApCapabilityCatalogueFsmRmtErrDescr_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmRmtErrDescr_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRmtErrDescr = _CfprApCapabilityCatalogueFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 10),
    _CfprApCapabilityCatalogueFsmRmtErrDescr_Type()
)
cfprApCapabilityCatalogueFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRmtErrDescr.setStatus("current")
_CfprApCapabilityCatalogueFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCapabilityCatalogueFsmRmtRslt_Object = MibTableColumn
cfprApCapabilityCatalogueFsmRmtRslt = _CfprApCapabilityCatalogueFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 2, 1, 11),
    _CfprApCapabilityCatalogueFsmRmtRslt_Type()
)
cfprApCapabilityCatalogueFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmRmtRslt.setStatus("current")
_CfprApCapabilityCatalogueFsmStageTable_Object = MibTable
cfprApCapabilityCatalogueFsmStageTable = _CfprApCapabilityCatalogueFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageTable.setStatus("current")
_CfprApCapabilityCatalogueFsmStageEntry_Object = MibTableRow
cfprApCapabilityCatalogueFsmStageEntry = _CfprApCapabilityCatalogueFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1)
)
cfprApCapabilityCatalogueFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityCatalogueFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageEntry.setStatus("current")
_CfprApCapabilityCatalogueFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityCatalogueFsmStageInstanceId_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageInstanceId = _CfprApCapabilityCatalogueFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 1),
    _CfprApCapabilityCatalogueFsmStageInstanceId_Type()
)
cfprApCapabilityCatalogueFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageInstanceId.setStatus("current")
_CfprApCapabilityCatalogueFsmStageDn_Type = CfprApManagedObjectDn
_CfprApCapabilityCatalogueFsmStageDn_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageDn = _CfprApCapabilityCatalogueFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 2),
    _CfprApCapabilityCatalogueFsmStageDn_Type()
)
cfprApCapabilityCatalogueFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageDn.setStatus("current")
_CfprApCapabilityCatalogueFsmStageRn_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmStageRn_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageRn = _CfprApCapabilityCatalogueFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 3),
    _CfprApCapabilityCatalogueFsmStageRn_Type()
)
cfprApCapabilityCatalogueFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageRn.setStatus("current")
_CfprApCapabilityCatalogueFsmStageDescrData_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmStageDescrData_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageDescrData = _CfprApCapabilityCatalogueFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 4),
    _CfprApCapabilityCatalogueFsmStageDescrData_Type()
)
cfprApCapabilityCatalogueFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageDescrData.setStatus("current")
_CfprApCapabilityCatalogueFsmStageLastUpdateTime_Type = DateAndTime
_CfprApCapabilityCatalogueFsmStageLastUpdateTime_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageLastUpdateTime = _CfprApCapabilityCatalogueFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 5),
    _CfprApCapabilityCatalogueFsmStageLastUpdateTime_Type()
)
cfprApCapabilityCatalogueFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageLastUpdateTime.setStatus("current")
_CfprApCapabilityCatalogueFsmStageName_Type = CfprApCapabilityCatalogueFsmStageName
_CfprApCapabilityCatalogueFsmStageName_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageName = _CfprApCapabilityCatalogueFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 6),
    _CfprApCapabilityCatalogueFsmStageName_Type()
)
cfprApCapabilityCatalogueFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageName.setStatus("current")
_CfprApCapabilityCatalogueFsmStageOrder_Type = Gauge32
_CfprApCapabilityCatalogueFsmStageOrder_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageOrder = _CfprApCapabilityCatalogueFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 7),
    _CfprApCapabilityCatalogueFsmStageOrder_Type()
)
cfprApCapabilityCatalogueFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageOrder.setStatus("current")
_CfprApCapabilityCatalogueFsmStageRetry_Type = Gauge32
_CfprApCapabilityCatalogueFsmStageRetry_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageRetry = _CfprApCapabilityCatalogueFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 8),
    _CfprApCapabilityCatalogueFsmStageRetry_Type()
)
cfprApCapabilityCatalogueFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageRetry.setStatus("current")
_CfprApCapabilityCatalogueFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApCapabilityCatalogueFsmStageStageStatus_Object = MibTableColumn
cfprApCapabilityCatalogueFsmStageStageStatus = _CfprApCapabilityCatalogueFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 3, 1, 9),
    _CfprApCapabilityCatalogueFsmStageStageStatus_Type()
)
cfprApCapabilityCatalogueFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmStageStageStatus.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskTable_Object = MibTable
cfprApCapabilityCatalogueFsmTaskTable = _CfprApCapabilityCatalogueFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskTable.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskEntry_Object = MibTableRow
cfprApCapabilityCatalogueFsmTaskEntry = _CfprApCapabilityCatalogueFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1)
)
cfprApCapabilityCatalogueFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityCatalogueFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskEntry.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityCatalogueFsmTaskInstanceId_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskInstanceId = _CfprApCapabilityCatalogueFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 1),
    _CfprApCapabilityCatalogueFsmTaskInstanceId_Type()
)
cfprApCapabilityCatalogueFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskInstanceId.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApCapabilityCatalogueFsmTaskDn_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskDn = _CfprApCapabilityCatalogueFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 2),
    _CfprApCapabilityCatalogueFsmTaskDn_Type()
)
cfprApCapabilityCatalogueFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskDn.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskRn_Type = SnmpAdminString
_CfprApCapabilityCatalogueFsmTaskRn_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskRn = _CfprApCapabilityCatalogueFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 3),
    _CfprApCapabilityCatalogueFsmTaskRn_Type()
)
cfprApCapabilityCatalogueFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskRn.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApCapabilityCatalogueFsmTaskCompletion_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskCompletion = _CfprApCapabilityCatalogueFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 4),
    _CfprApCapabilityCatalogueFsmTaskCompletion_Type()
)
cfprApCapabilityCatalogueFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskCompletion.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskFlags_Type = CfprApFsmFlags
_CfprApCapabilityCatalogueFsmTaskFlags_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskFlags = _CfprApCapabilityCatalogueFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 5),
    _CfprApCapabilityCatalogueFsmTaskFlags_Type()
)
cfprApCapabilityCatalogueFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskFlags.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskItem_Type = CfprApCapabilityCatalogueFsmTaskItem
_CfprApCapabilityCatalogueFsmTaskItem_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskItem = _CfprApCapabilityCatalogueFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 6),
    _CfprApCapabilityCatalogueFsmTaskItem_Type()
)
cfprApCapabilityCatalogueFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskItem.setStatus("current")
_CfprApCapabilityCatalogueFsmTaskSeqId_Type = Gauge32
_CfprApCapabilityCatalogueFsmTaskSeqId_Object = MibTableColumn
cfprApCapabilityCatalogueFsmTaskSeqId = _CfprApCapabilityCatalogueFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 4, 1, 7),
    _CfprApCapabilityCatalogueFsmTaskSeqId_Type()
)
cfprApCapabilityCatalogueFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityCatalogueFsmTaskSeqId.setStatus("current")
_CfprApCapabilityEpTable_Object = MibTable
cfprApCapabilityEpTable = _CfprApCapabilityEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    cfprApCapabilityEpTable.setStatus("current")
_CfprApCapabilityEpEntry_Object = MibTableRow
cfprApCapabilityEpEntry = _CfprApCapabilityEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 5, 1)
)
cfprApCapabilityEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityEpEntry.setStatus("current")
_CfprApCapabilityEpInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityEpInstanceId_Object = MibTableColumn
cfprApCapabilityEpInstanceId = _CfprApCapabilityEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 5, 1, 1),
    _CfprApCapabilityEpInstanceId_Type()
)
cfprApCapabilityEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityEpInstanceId.setStatus("current")
_CfprApCapabilityEpDn_Type = CfprApManagedObjectDn
_CfprApCapabilityEpDn_Object = MibTableColumn
cfprApCapabilityEpDn = _CfprApCapabilityEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 5, 1, 2),
    _CfprApCapabilityEpDn_Type()
)
cfprApCapabilityEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityEpDn.setStatus("current")
_CfprApCapabilityEpRn_Type = SnmpAdminString
_CfprApCapabilityEpRn_Object = MibTableColumn
cfprApCapabilityEpRn = _CfprApCapabilityEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 5, 1, 3),
    _CfprApCapabilityEpRn_Type()
)
cfprApCapabilityEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityEpRn.setStatus("current")
_CfprApCapabilityFeatureLimitsTable_Object = MibTable
cfprApCapabilityFeatureLimitsTable = _CfprApCapabilityFeatureLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6)
)
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsTable.setStatus("current")
_CfprApCapabilityFeatureLimitsEntry_Object = MibTableRow
cfprApCapabilityFeatureLimitsEntry = _CfprApCapabilityFeatureLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1)
)
cfprApCapabilityFeatureLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityFeatureLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsEntry.setStatus("current")
_CfprApCapabilityFeatureLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityFeatureLimitsInstanceId_Object = MibTableColumn
cfprApCapabilityFeatureLimitsInstanceId = _CfprApCapabilityFeatureLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 1),
    _CfprApCapabilityFeatureLimitsInstanceId_Type()
)
cfprApCapabilityFeatureLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsInstanceId.setStatus("current")
_CfprApCapabilityFeatureLimitsDn_Type = CfprApManagedObjectDn
_CfprApCapabilityFeatureLimitsDn_Object = MibTableColumn
cfprApCapabilityFeatureLimitsDn = _CfprApCapabilityFeatureLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 2),
    _CfprApCapabilityFeatureLimitsDn_Type()
)
cfprApCapabilityFeatureLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsDn.setStatus("current")
_CfprApCapabilityFeatureLimitsRn_Type = SnmpAdminString
_CfprApCapabilityFeatureLimitsRn_Object = MibTableColumn
cfprApCapabilityFeatureLimitsRn = _CfprApCapabilityFeatureLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 3),
    _CfprApCapabilityFeatureLimitsRn_Type()
)
cfprApCapabilityFeatureLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsRn.setStatus("current")
_CfprApCapabilityFeatureLimitsDescr_Type = SnmpAdminString
_CfprApCapabilityFeatureLimitsDescr_Object = MibTableColumn
cfprApCapabilityFeatureLimitsDescr = _CfprApCapabilityFeatureLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 4),
    _CfprApCapabilityFeatureLimitsDescr_Type()
)
cfprApCapabilityFeatureLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsDescr.setStatus("current")
_CfprApCapabilityFeatureLimitsFeatureStatus_Type = CfprApCapabilityFeatureStatus
_CfprApCapabilityFeatureLimitsFeatureStatus_Object = MibTableColumn
cfprApCapabilityFeatureLimitsFeatureStatus = _CfprApCapabilityFeatureLimitsFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 5),
    _CfprApCapabilityFeatureLimitsFeatureStatus_Type()
)
cfprApCapabilityFeatureLimitsFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsFeatureStatus.setStatus("current")
_CfprApCapabilityFeatureLimitsLimit_Type = Gauge32
_CfprApCapabilityFeatureLimitsLimit_Object = MibTableColumn
cfprApCapabilityFeatureLimitsLimit = _CfprApCapabilityFeatureLimitsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 6),
    _CfprApCapabilityFeatureLimitsLimit_Type()
)
cfprApCapabilityFeatureLimitsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsLimit.setStatus("current")
_CfprApCapabilityFeatureLimitsName_Type = SnmpAdminString
_CfprApCapabilityFeatureLimitsName_Object = MibTableColumn
cfprApCapabilityFeatureLimitsName = _CfprApCapabilityFeatureLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 7),
    _CfprApCapabilityFeatureLimitsName_Type()
)
cfprApCapabilityFeatureLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsName.setStatus("current")
_CfprApCapabilityFeatureLimitsPlatform_Type = CfprApCapabilityPlatform
_CfprApCapabilityFeatureLimitsPlatform_Object = MibTableColumn
cfprApCapabilityFeatureLimitsPlatform = _CfprApCapabilityFeatureLimitsPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 6, 1, 8),
    _CfprApCapabilityFeatureLimitsPlatform_Type()
)
cfprApCapabilityFeatureLimitsPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityFeatureLimitsPlatform.setStatus("current")
_CfprApCapabilityMgmtExtensionTable_Object = MibTable
cfprApCapabilityMgmtExtensionTable = _CfprApCapabilityMgmtExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7)
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionTable.setStatus("current")
_CfprApCapabilityMgmtExtensionEntry_Object = MibTableRow
cfprApCapabilityMgmtExtensionEntry = _CfprApCapabilityMgmtExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1)
)
cfprApCapabilityMgmtExtensionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityMgmtExtensionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionEntry.setStatus("current")
_CfprApCapabilityMgmtExtensionInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityMgmtExtensionInstanceId_Object = MibTableColumn
cfprApCapabilityMgmtExtensionInstanceId = _CfprApCapabilityMgmtExtensionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 1),
    _CfprApCapabilityMgmtExtensionInstanceId_Type()
)
cfprApCapabilityMgmtExtensionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionInstanceId.setStatus("current")
_CfprApCapabilityMgmtExtensionDn_Type = CfprApManagedObjectDn
_CfprApCapabilityMgmtExtensionDn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionDn = _CfprApCapabilityMgmtExtensionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 2),
    _CfprApCapabilityMgmtExtensionDn_Type()
)
cfprApCapabilityMgmtExtensionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionDn.setStatus("current")
_CfprApCapabilityMgmtExtensionRn_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionRn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionRn = _CfprApCapabilityMgmtExtensionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 3),
    _CfprApCapabilityMgmtExtensionRn_Type()
)
cfprApCapabilityMgmtExtensionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionRn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmDescr_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmDescr_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmDescr = _CfprApCapabilityMgmtExtensionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 4),
    _CfprApCapabilityMgmtExtensionFsmDescr_Type()
)
cfprApCapabilityMgmtExtensionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmDescr.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmPrev_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmPrev_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmPrev = _CfprApCapabilityMgmtExtensionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 5),
    _CfprApCapabilityMgmtExtensionFsmPrev_Type()
)
cfprApCapabilityMgmtExtensionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmPrev.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmProgr_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmProgr_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmProgr = _CfprApCapabilityMgmtExtensionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 6),
    _CfprApCapabilityMgmtExtensionFsmProgr_Type()
)
cfprApCapabilityMgmtExtensionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmProgr.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRmtInvErrCode_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmRmtInvErrCode_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRmtInvErrCode = _CfprApCapabilityMgmtExtensionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 7),
    _CfprApCapabilityMgmtExtensionFsmRmtInvErrCode_Type()
)
cfprApCapabilityMgmtExtensionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRmtInvErrCode.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmRmtInvErrDescr_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRmtInvErrDescr = _CfprApCapabilityMgmtExtensionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 8),
    _CfprApCapabilityMgmtExtensionFsmRmtInvErrDescr_Type()
)
cfprApCapabilityMgmtExtensionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRmtInvErrDescr.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCapabilityMgmtExtensionFsmRmtInvRslt_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRmtInvRslt = _CfprApCapabilityMgmtExtensionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 9),
    _CfprApCapabilityMgmtExtensionFsmRmtInvRslt_Type()
)
cfprApCapabilityMgmtExtensionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRmtInvRslt.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageDescr_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmStageDescr_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageDescr = _CfprApCapabilityMgmtExtensionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 10),
    _CfprApCapabilityMgmtExtensionFsmStageDescr_Type()
)
cfprApCapabilityMgmtExtensionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageDescr.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStamp_Type = DateAndTime
_CfprApCapabilityMgmtExtensionFsmStamp_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStamp = _CfprApCapabilityMgmtExtensionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 11),
    _CfprApCapabilityMgmtExtensionFsmStamp_Type()
)
cfprApCapabilityMgmtExtensionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStamp.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStatus_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmStatus_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStatus = _CfprApCapabilityMgmtExtensionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 12),
    _CfprApCapabilityMgmtExtensionFsmStatus_Type()
)
cfprApCapabilityMgmtExtensionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStatus.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTry_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmTry_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTry = _CfprApCapabilityMgmtExtensionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 7, 1, 13),
    _CfprApCapabilityMgmtExtensionFsmTry_Type()
)
cfprApCapabilityMgmtExtensionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTry.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTable_Object = MibTable
cfprApCapabilityMgmtExtensionFsmTable = _CfprApCapabilityMgmtExtensionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8)
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTable.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmEntry_Object = MibTableRow
cfprApCapabilityMgmtExtensionFsmEntry = _CfprApCapabilityMgmtExtensionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1)
)
cfprApCapabilityMgmtExtensionFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityMgmtExtensionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmEntry.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityMgmtExtensionFsmInstanceId_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmInstanceId = _CfprApCapabilityMgmtExtensionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 1),
    _CfprApCapabilityMgmtExtensionFsmInstanceId_Type()
)
cfprApCapabilityMgmtExtensionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmInstanceId.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmDn_Type = CfprApManagedObjectDn
_CfprApCapabilityMgmtExtensionFsmDn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmDn = _CfprApCapabilityMgmtExtensionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 2),
    _CfprApCapabilityMgmtExtensionFsmDn_Type()
)
cfprApCapabilityMgmtExtensionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmDn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRn_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmRn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRn = _CfprApCapabilityMgmtExtensionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 3),
    _CfprApCapabilityMgmtExtensionFsmRn_Type()
)
cfprApCapabilityMgmtExtensionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmCompletionTime_Type = DateAndTime
_CfprApCapabilityMgmtExtensionFsmCompletionTime_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmCompletionTime = _CfprApCapabilityMgmtExtensionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 4),
    _CfprApCapabilityMgmtExtensionFsmCompletionTime_Type()
)
cfprApCapabilityMgmtExtensionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmCompletionTime.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmCurrentFsm_Type = CfprApCapabilityMgmtExtensionFsmCurrentFsm
_CfprApCapabilityMgmtExtensionFsmCurrentFsm_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmCurrentFsm = _CfprApCapabilityMgmtExtensionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 5),
    _CfprApCapabilityMgmtExtensionFsmCurrentFsm_Type()
)
cfprApCapabilityMgmtExtensionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmCurrentFsm.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmDescrData_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmDescrData_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmDescrData = _CfprApCapabilityMgmtExtensionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 6),
    _CfprApCapabilityMgmtExtensionFsmDescrData_Type()
)
cfprApCapabilityMgmtExtensionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmDescrData.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApCapabilityMgmtExtensionFsmFsmStatus_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmFsmStatus = _CfprApCapabilityMgmtExtensionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 7),
    _CfprApCapabilityMgmtExtensionFsmFsmStatus_Type()
)
cfprApCapabilityMgmtExtensionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmFsmStatus.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmProgress_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmProgress_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmProgress = _CfprApCapabilityMgmtExtensionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 8),
    _CfprApCapabilityMgmtExtensionFsmProgress_Type()
)
cfprApCapabilityMgmtExtensionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmProgress.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRmtErrCode_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmRmtErrCode_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRmtErrCode = _CfprApCapabilityMgmtExtensionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 9),
    _CfprApCapabilityMgmtExtensionFsmRmtErrCode_Type()
)
cfprApCapabilityMgmtExtensionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRmtErrCode.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRmtErrDescr_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmRmtErrDescr_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRmtErrDescr = _CfprApCapabilityMgmtExtensionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 10),
    _CfprApCapabilityMgmtExtensionFsmRmtErrDescr_Type()
)
cfprApCapabilityMgmtExtensionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRmtErrDescr.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCapabilityMgmtExtensionFsmRmtRslt_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmRmtRslt = _CfprApCapabilityMgmtExtensionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 8, 1, 11),
    _CfprApCapabilityMgmtExtensionFsmRmtRslt_Type()
)
cfprApCapabilityMgmtExtensionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmRmtRslt.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageTable_Object = MibTable
cfprApCapabilityMgmtExtensionFsmStageTable = _CfprApCapabilityMgmtExtensionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9)
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageTable.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageEntry_Object = MibTableRow
cfprApCapabilityMgmtExtensionFsmStageEntry = _CfprApCapabilityMgmtExtensionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1)
)
cfprApCapabilityMgmtExtensionFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityMgmtExtensionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageEntry.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityMgmtExtensionFsmStageInstanceId_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageInstanceId = _CfprApCapabilityMgmtExtensionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 1),
    _CfprApCapabilityMgmtExtensionFsmStageInstanceId_Type()
)
cfprApCapabilityMgmtExtensionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageInstanceId.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageDn_Type = CfprApManagedObjectDn
_CfprApCapabilityMgmtExtensionFsmStageDn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageDn = _CfprApCapabilityMgmtExtensionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 2),
    _CfprApCapabilityMgmtExtensionFsmStageDn_Type()
)
cfprApCapabilityMgmtExtensionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageDn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageRn_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmStageRn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageRn = _CfprApCapabilityMgmtExtensionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 3),
    _CfprApCapabilityMgmtExtensionFsmStageRn_Type()
)
cfprApCapabilityMgmtExtensionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageRn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageDescrData_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmStageDescrData_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageDescrData = _CfprApCapabilityMgmtExtensionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 4),
    _CfprApCapabilityMgmtExtensionFsmStageDescrData_Type()
)
cfprApCapabilityMgmtExtensionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageDescrData.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageLastUpdateTime_Type = DateAndTime
_CfprApCapabilityMgmtExtensionFsmStageLastUpdateTime_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageLastUpdateTime = _CfprApCapabilityMgmtExtensionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 5),
    _CfprApCapabilityMgmtExtensionFsmStageLastUpdateTime_Type()
)
cfprApCapabilityMgmtExtensionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageLastUpdateTime.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageName_Type = CfprApCapabilityMgmtExtensionFsmStageName
_CfprApCapabilityMgmtExtensionFsmStageName_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageName = _CfprApCapabilityMgmtExtensionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 6),
    _CfprApCapabilityMgmtExtensionFsmStageName_Type()
)
cfprApCapabilityMgmtExtensionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageName.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageOrder_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmStageOrder_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageOrder = _CfprApCapabilityMgmtExtensionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 7),
    _CfprApCapabilityMgmtExtensionFsmStageOrder_Type()
)
cfprApCapabilityMgmtExtensionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageOrder.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageRetry_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmStageRetry_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageRetry = _CfprApCapabilityMgmtExtensionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 8),
    _CfprApCapabilityMgmtExtensionFsmStageRetry_Type()
)
cfprApCapabilityMgmtExtensionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageRetry.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApCapabilityMgmtExtensionFsmStageStageStatus_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmStageStageStatus = _CfprApCapabilityMgmtExtensionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 9, 1, 9),
    _CfprApCapabilityMgmtExtensionFsmStageStageStatus_Type()
)
cfprApCapabilityMgmtExtensionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmStageStageStatus.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskTable_Object = MibTable
cfprApCapabilityMgmtExtensionFsmTaskTable = _CfprApCapabilityMgmtExtensionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10)
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskTable.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskEntry_Object = MibTableRow
cfprApCapabilityMgmtExtensionFsmTaskEntry = _CfprApCapabilityMgmtExtensionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1)
)
cfprApCapabilityMgmtExtensionFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityMgmtExtensionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskEntry.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityMgmtExtensionFsmTaskInstanceId_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskInstanceId = _CfprApCapabilityMgmtExtensionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 1),
    _CfprApCapabilityMgmtExtensionFsmTaskInstanceId_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskInstanceId.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApCapabilityMgmtExtensionFsmTaskDn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskDn = _CfprApCapabilityMgmtExtensionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 2),
    _CfprApCapabilityMgmtExtensionFsmTaskDn_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskDn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskRn_Type = SnmpAdminString
_CfprApCapabilityMgmtExtensionFsmTaskRn_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskRn = _CfprApCapabilityMgmtExtensionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 3),
    _CfprApCapabilityMgmtExtensionFsmTaskRn_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskRn.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApCapabilityMgmtExtensionFsmTaskCompletion_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskCompletion = _CfprApCapabilityMgmtExtensionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 4),
    _CfprApCapabilityMgmtExtensionFsmTaskCompletion_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskCompletion.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskFlags_Type = CfprApFsmFlags
_CfprApCapabilityMgmtExtensionFsmTaskFlags_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskFlags = _CfprApCapabilityMgmtExtensionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 5),
    _CfprApCapabilityMgmtExtensionFsmTaskFlags_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskFlags.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskItem_Type = CfprApCapabilityMgmtExtensionFsmTaskItem
_CfprApCapabilityMgmtExtensionFsmTaskItem_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskItem = _CfprApCapabilityMgmtExtensionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 6),
    _CfprApCapabilityMgmtExtensionFsmTaskItem_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskItem.setStatus("current")
_CfprApCapabilityMgmtExtensionFsmTaskSeqId_Type = Gauge32
_CfprApCapabilityMgmtExtensionFsmTaskSeqId_Object = MibTableColumn
cfprApCapabilityMgmtExtensionFsmTaskSeqId = _CfprApCapabilityMgmtExtensionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 10, 1, 7),
    _CfprApCapabilityMgmtExtensionFsmTaskSeqId_Type()
)
cfprApCapabilityMgmtExtensionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityMgmtExtensionFsmTaskSeqId.setStatus("current")
_CfprApCapabilityNetworkLimitsTable_Object = MibTable
cfprApCapabilityNetworkLimitsTable = _CfprApCapabilityNetworkLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 11)
)
if mibBuilder.loadTexts:
    cfprApCapabilityNetworkLimitsTable.setStatus("current")
_CfprApCapabilityNetworkLimitsEntry_Object = MibTableRow
cfprApCapabilityNetworkLimitsEntry = _CfprApCapabilityNetworkLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 11, 1)
)
cfprApCapabilityNetworkLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityNetworkLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityNetworkLimitsEntry.setStatus("current")
_CfprApCapabilityNetworkLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityNetworkLimitsInstanceId_Object = MibTableColumn
cfprApCapabilityNetworkLimitsInstanceId = _CfprApCapabilityNetworkLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 11, 1, 1),
    _CfprApCapabilityNetworkLimitsInstanceId_Type()
)
cfprApCapabilityNetworkLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityNetworkLimitsInstanceId.setStatus("current")
_CfprApCapabilityNetworkLimitsDn_Type = CfprApManagedObjectDn
_CfprApCapabilityNetworkLimitsDn_Object = MibTableColumn
cfprApCapabilityNetworkLimitsDn = _CfprApCapabilityNetworkLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 11, 1, 2),
    _CfprApCapabilityNetworkLimitsDn_Type()
)
cfprApCapabilityNetworkLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityNetworkLimitsDn.setStatus("current")
_CfprApCapabilityNetworkLimitsRn_Type = SnmpAdminString
_CfprApCapabilityNetworkLimitsRn_Object = MibTableColumn
cfprApCapabilityNetworkLimitsRn = _CfprApCapabilityNetworkLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 11, 1, 3),
    _CfprApCapabilityNetworkLimitsRn_Type()
)
cfprApCapabilityNetworkLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityNetworkLimitsRn.setStatus("current")
_CfprApCapabilityStorageLimitsTable_Object = MibTable
cfprApCapabilityStorageLimitsTable = _CfprApCapabilityStorageLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 12)
)
if mibBuilder.loadTexts:
    cfprApCapabilityStorageLimitsTable.setStatus("current")
_CfprApCapabilityStorageLimitsEntry_Object = MibTableRow
cfprApCapabilityStorageLimitsEntry = _CfprApCapabilityStorageLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 12, 1)
)
cfprApCapabilityStorageLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityStorageLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityStorageLimitsEntry.setStatus("current")
_CfprApCapabilityStorageLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityStorageLimitsInstanceId_Object = MibTableColumn
cfprApCapabilityStorageLimitsInstanceId = _CfprApCapabilityStorageLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 12, 1, 1),
    _CfprApCapabilityStorageLimitsInstanceId_Type()
)
cfprApCapabilityStorageLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityStorageLimitsInstanceId.setStatus("current")
_CfprApCapabilityStorageLimitsDn_Type = CfprApManagedObjectDn
_CfprApCapabilityStorageLimitsDn_Object = MibTableColumn
cfprApCapabilityStorageLimitsDn = _CfprApCapabilityStorageLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 12, 1, 2),
    _CfprApCapabilityStorageLimitsDn_Type()
)
cfprApCapabilityStorageLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityStorageLimitsDn.setStatus("current")
_CfprApCapabilityStorageLimitsRn_Type = SnmpAdminString
_CfprApCapabilityStorageLimitsRn_Object = MibTableColumn
cfprApCapabilityStorageLimitsRn = _CfprApCapabilityStorageLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 12, 1, 3),
    _CfprApCapabilityStorageLimitsRn_Type()
)
cfprApCapabilityStorageLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityStorageLimitsRn.setStatus("current")
_CfprApCapabilitySystemLimitsTable_Object = MibTable
cfprApCapabilitySystemLimitsTable = _CfprApCapabilitySystemLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 13)
)
if mibBuilder.loadTexts:
    cfprApCapabilitySystemLimitsTable.setStatus("current")
_CfprApCapabilitySystemLimitsEntry_Object = MibTableRow
cfprApCapabilitySystemLimitsEntry = _CfprApCapabilitySystemLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 13, 1)
)
cfprApCapabilitySystemLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilitySystemLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilitySystemLimitsEntry.setStatus("current")
_CfprApCapabilitySystemLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilitySystemLimitsInstanceId_Object = MibTableColumn
cfprApCapabilitySystemLimitsInstanceId = _CfprApCapabilitySystemLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 13, 1, 1),
    _CfprApCapabilitySystemLimitsInstanceId_Type()
)
cfprApCapabilitySystemLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilitySystemLimitsInstanceId.setStatus("current")
_CfprApCapabilitySystemLimitsDn_Type = CfprApManagedObjectDn
_CfprApCapabilitySystemLimitsDn_Object = MibTableColumn
cfprApCapabilitySystemLimitsDn = _CfprApCapabilitySystemLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 13, 1, 2),
    _CfprApCapabilitySystemLimitsDn_Type()
)
cfprApCapabilitySystemLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilitySystemLimitsDn.setStatus("current")
_CfprApCapabilitySystemLimitsRn_Type = SnmpAdminString
_CfprApCapabilitySystemLimitsRn_Object = MibTableColumn
cfprApCapabilitySystemLimitsRn = _CfprApCapabilitySystemLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 13, 1, 3),
    _CfprApCapabilitySystemLimitsRn_Type()
)
cfprApCapabilitySystemLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilitySystemLimitsRn.setStatus("current")
_CfprApCapabilityUpdateTable_Object = MibTable
cfprApCapabilityUpdateTable = _CfprApCapabilityUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14)
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateTable.setStatus("current")
_CfprApCapabilityUpdateEntry_Object = MibTableRow
cfprApCapabilityUpdateEntry = _CfprApCapabilityUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1)
)
cfprApCapabilityUpdateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityUpdateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateEntry.setStatus("current")
_CfprApCapabilityUpdateInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityUpdateInstanceId_Object = MibTableColumn
cfprApCapabilityUpdateInstanceId = _CfprApCapabilityUpdateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1, 1),
    _CfprApCapabilityUpdateInstanceId_Type()
)
cfprApCapabilityUpdateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateInstanceId.setStatus("current")
_CfprApCapabilityUpdateDn_Type = CfprApManagedObjectDn
_CfprApCapabilityUpdateDn_Object = MibTableColumn
cfprApCapabilityUpdateDn = _CfprApCapabilityUpdateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1, 2),
    _CfprApCapabilityUpdateDn_Type()
)
cfprApCapabilityUpdateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateDn.setStatus("current")
_CfprApCapabilityUpdateRn_Type = SnmpAdminString
_CfprApCapabilityUpdateRn_Object = MibTableColumn
cfprApCapabilityUpdateRn = _CfprApCapabilityUpdateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1, 3),
    _CfprApCapabilityUpdateRn_Type()
)
cfprApCapabilityUpdateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateRn.setStatus("current")
_CfprApCapabilityUpdateImageName_Type = SnmpAdminString
_CfprApCapabilityUpdateImageName_Object = MibTableColumn
cfprApCapabilityUpdateImageName = _CfprApCapabilityUpdateImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1, 4),
    _CfprApCapabilityUpdateImageName_Type()
)
cfprApCapabilityUpdateImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateImageName.setStatus("current")
_CfprApCapabilityUpdateUpdateTs_Type = DateAndTime
_CfprApCapabilityUpdateUpdateTs_Object = MibTableColumn
cfprApCapabilityUpdateUpdateTs = _CfprApCapabilityUpdateUpdateTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1, 5),
    _CfprApCapabilityUpdateUpdateTs_Type()
)
cfprApCapabilityUpdateUpdateTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateUpdateTs.setStatus("current")
_CfprApCapabilityUpdateVersion_Type = SnmpAdminString
_CfprApCapabilityUpdateVersion_Object = MibTableColumn
cfprApCapabilityUpdateVersion = _CfprApCapabilityUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 14, 1, 6),
    _CfprApCapabilityUpdateVersion_Type()
)
cfprApCapabilityUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdateVersion.setStatus("current")
_CfprApCapabilityUpdaterTable_Object = MibTable
cfprApCapabilityUpdaterTable = _CfprApCapabilityUpdaterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15)
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterTable.setStatus("current")
_CfprApCapabilityUpdaterEntry_Object = MibTableRow
cfprApCapabilityUpdaterEntry = _CfprApCapabilityUpdaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1)
)
cfprApCapabilityUpdaterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityUpdaterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterEntry.setStatus("current")
_CfprApCapabilityUpdaterInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityUpdaterInstanceId_Object = MibTableColumn
cfprApCapabilityUpdaterInstanceId = _CfprApCapabilityUpdaterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 1),
    _CfprApCapabilityUpdaterInstanceId_Type()
)
cfprApCapabilityUpdaterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterInstanceId.setStatus("current")
_CfprApCapabilityUpdaterDn_Type = CfprApManagedObjectDn
_CfprApCapabilityUpdaterDn_Object = MibTableColumn
cfprApCapabilityUpdaterDn = _CfprApCapabilityUpdaterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 2),
    _CfprApCapabilityUpdaterDn_Type()
)
cfprApCapabilityUpdaterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterDn.setStatus("current")
_CfprApCapabilityUpdaterRn_Type = SnmpAdminString
_CfprApCapabilityUpdaterRn_Object = MibTableColumn
cfprApCapabilityUpdaterRn = _CfprApCapabilityUpdaterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 3),
    _CfprApCapabilityUpdaterRn_Type()
)
cfprApCapabilityUpdaterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterRn.setStatus("current")
_CfprApCapabilityUpdaterAdminState_Type = CfprApCapabilityAdminState
_CfprApCapabilityUpdaterAdminState_Object = MibTableColumn
cfprApCapabilityUpdaterAdminState = _CfprApCapabilityUpdaterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 4),
    _CfprApCapabilityUpdaterAdminState_Type()
)
cfprApCapabilityUpdaterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterAdminState.setStatus("current")
_CfprApCapabilityUpdaterFileName_Type = SnmpAdminString
_CfprApCapabilityUpdaterFileName_Object = MibTableColumn
cfprApCapabilityUpdaterFileName = _CfprApCapabilityUpdaterFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 5),
    _CfprApCapabilityUpdaterFileName_Type()
)
cfprApCapabilityUpdaterFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFileName.setStatus("current")
_CfprApCapabilityUpdaterFsmDescr_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmDescr_Object = MibTableColumn
cfprApCapabilityUpdaterFsmDescr = _CfprApCapabilityUpdaterFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 6),
    _CfprApCapabilityUpdaterFsmDescr_Type()
)
cfprApCapabilityUpdaterFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmDescr.setStatus("current")
_CfprApCapabilityUpdaterFsmPrev_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmPrev_Object = MibTableColumn
cfprApCapabilityUpdaterFsmPrev = _CfprApCapabilityUpdaterFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 7),
    _CfprApCapabilityUpdaterFsmPrev_Type()
)
cfprApCapabilityUpdaterFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmPrev.setStatus("current")
_CfprApCapabilityUpdaterFsmProgr_Type = Gauge32
_CfprApCapabilityUpdaterFsmProgr_Object = MibTableColumn
cfprApCapabilityUpdaterFsmProgr = _CfprApCapabilityUpdaterFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 8),
    _CfprApCapabilityUpdaterFsmProgr_Type()
)
cfprApCapabilityUpdaterFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmProgr.setStatus("current")
_CfprApCapabilityUpdaterFsmRmtInvErrCode_Type = Gauge32
_CfprApCapabilityUpdaterFsmRmtInvErrCode_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRmtInvErrCode = _CfprApCapabilityUpdaterFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 9),
    _CfprApCapabilityUpdaterFsmRmtInvErrCode_Type()
)
cfprApCapabilityUpdaterFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRmtInvErrCode.setStatus("current")
_CfprApCapabilityUpdaterFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmRmtInvErrDescr_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRmtInvErrDescr = _CfprApCapabilityUpdaterFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 10),
    _CfprApCapabilityUpdaterFsmRmtInvErrDescr_Type()
)
cfprApCapabilityUpdaterFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRmtInvErrDescr.setStatus("current")
_CfprApCapabilityUpdaterFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCapabilityUpdaterFsmRmtInvRslt_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRmtInvRslt = _CfprApCapabilityUpdaterFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 11),
    _CfprApCapabilityUpdaterFsmRmtInvRslt_Type()
)
cfprApCapabilityUpdaterFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRmtInvRslt.setStatus("current")
_CfprApCapabilityUpdaterFsmStageDescr_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmStageDescr_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageDescr = _CfprApCapabilityUpdaterFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 12),
    _CfprApCapabilityUpdaterFsmStageDescr_Type()
)
cfprApCapabilityUpdaterFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageDescr.setStatus("current")
_CfprApCapabilityUpdaterFsmStamp_Type = DateAndTime
_CfprApCapabilityUpdaterFsmStamp_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStamp = _CfprApCapabilityUpdaterFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 13),
    _CfprApCapabilityUpdaterFsmStamp_Type()
)
cfprApCapabilityUpdaterFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStamp.setStatus("current")
_CfprApCapabilityUpdaterFsmStatus_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmStatus_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStatus = _CfprApCapabilityUpdaterFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 14),
    _CfprApCapabilityUpdaterFsmStatus_Type()
)
cfprApCapabilityUpdaterFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStatus.setStatus("current")
_CfprApCapabilityUpdaterFsmTry_Type = Gauge32
_CfprApCapabilityUpdaterFsmTry_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTry = _CfprApCapabilityUpdaterFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 15),
    _CfprApCapabilityUpdaterFsmTry_Type()
)
cfprApCapabilityUpdaterFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTry.setStatus("current")
_CfprApCapabilityUpdaterImageName_Type = SnmpAdminString
_CfprApCapabilityUpdaterImageName_Object = MibTableColumn
cfprApCapabilityUpdaterImageName = _CfprApCapabilityUpdaterImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 16),
    _CfprApCapabilityUpdaterImageName_Type()
)
cfprApCapabilityUpdaterImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterImageName.setStatus("current")
_CfprApCapabilityUpdaterOperState_Type = CfprApCapabilityOperStatus
_CfprApCapabilityUpdaterOperState_Object = MibTableColumn
cfprApCapabilityUpdaterOperState = _CfprApCapabilityUpdaterOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 17),
    _CfprApCapabilityUpdaterOperState_Type()
)
cfprApCapabilityUpdaterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterOperState.setStatus("current")
_CfprApCapabilityUpdaterProtocol_Type = CfprApFirmwareTransport
_CfprApCapabilityUpdaterProtocol_Object = MibTableColumn
cfprApCapabilityUpdaterProtocol = _CfprApCapabilityUpdaterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 18),
    _CfprApCapabilityUpdaterProtocol_Type()
)
cfprApCapabilityUpdaterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterProtocol.setStatus("current")
_CfprApCapabilityUpdaterPwd_Type = SnmpAdminString
_CfprApCapabilityUpdaterPwd_Object = MibTableColumn
cfprApCapabilityUpdaterPwd = _CfprApCapabilityUpdaterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 19),
    _CfprApCapabilityUpdaterPwd_Type()
)
cfprApCapabilityUpdaterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterPwd.setStatus("current")
_CfprApCapabilityUpdaterRemotePath_Type = SnmpAdminString
_CfprApCapabilityUpdaterRemotePath_Object = MibTableColumn
cfprApCapabilityUpdaterRemotePath = _CfprApCapabilityUpdaterRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 20),
    _CfprApCapabilityUpdaterRemotePath_Type()
)
cfprApCapabilityUpdaterRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterRemotePath.setStatus("current")
_CfprApCapabilityUpdaterServer_Type = SnmpAdminString
_CfprApCapabilityUpdaterServer_Object = MibTableColumn
cfprApCapabilityUpdaterServer = _CfprApCapabilityUpdaterServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 21),
    _CfprApCapabilityUpdaterServer_Type()
)
cfprApCapabilityUpdaterServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterServer.setStatus("current")
_CfprApCapabilityUpdaterUser_Type = SnmpAdminString
_CfprApCapabilityUpdaterUser_Object = MibTableColumn
cfprApCapabilityUpdaterUser = _CfprApCapabilityUpdaterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 22),
    _CfprApCapabilityUpdaterUser_Type()
)
cfprApCapabilityUpdaterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterUser.setStatus("current")
_CfprApCapabilityUpdaterVersion_Type = SnmpAdminString
_CfprApCapabilityUpdaterVersion_Object = MibTableColumn
cfprApCapabilityUpdaterVersion = _CfprApCapabilityUpdaterVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 15, 1, 23),
    _CfprApCapabilityUpdaterVersion_Type()
)
cfprApCapabilityUpdaterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterVersion.setStatus("current")
_CfprApCapabilityUpdaterFsmTable_Object = MibTable
cfprApCapabilityUpdaterFsmTable = _CfprApCapabilityUpdaterFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16)
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTable.setStatus("current")
_CfprApCapabilityUpdaterFsmEntry_Object = MibTableRow
cfprApCapabilityUpdaterFsmEntry = _CfprApCapabilityUpdaterFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1)
)
cfprApCapabilityUpdaterFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityUpdaterFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmEntry.setStatus("current")
_CfprApCapabilityUpdaterFsmInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityUpdaterFsmInstanceId_Object = MibTableColumn
cfprApCapabilityUpdaterFsmInstanceId = _CfprApCapabilityUpdaterFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 1),
    _CfprApCapabilityUpdaterFsmInstanceId_Type()
)
cfprApCapabilityUpdaterFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmInstanceId.setStatus("current")
_CfprApCapabilityUpdaterFsmDn_Type = CfprApManagedObjectDn
_CfprApCapabilityUpdaterFsmDn_Object = MibTableColumn
cfprApCapabilityUpdaterFsmDn = _CfprApCapabilityUpdaterFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 2),
    _CfprApCapabilityUpdaterFsmDn_Type()
)
cfprApCapabilityUpdaterFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmDn.setStatus("current")
_CfprApCapabilityUpdaterFsmRn_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmRn_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRn = _CfprApCapabilityUpdaterFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 3),
    _CfprApCapabilityUpdaterFsmRn_Type()
)
cfprApCapabilityUpdaterFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRn.setStatus("current")
_CfprApCapabilityUpdaterFsmCompletionTime_Type = DateAndTime
_CfprApCapabilityUpdaterFsmCompletionTime_Object = MibTableColumn
cfprApCapabilityUpdaterFsmCompletionTime = _CfprApCapabilityUpdaterFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 4),
    _CfprApCapabilityUpdaterFsmCompletionTime_Type()
)
cfprApCapabilityUpdaterFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmCompletionTime.setStatus("current")
_CfprApCapabilityUpdaterFsmCurrentFsm_Type = CfprApCapabilityUpdaterFsmCurrentFsm
_CfprApCapabilityUpdaterFsmCurrentFsm_Object = MibTableColumn
cfprApCapabilityUpdaterFsmCurrentFsm = _CfprApCapabilityUpdaterFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 5),
    _CfprApCapabilityUpdaterFsmCurrentFsm_Type()
)
cfprApCapabilityUpdaterFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmCurrentFsm.setStatus("current")
_CfprApCapabilityUpdaterFsmDescrData_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmDescrData_Object = MibTableColumn
cfprApCapabilityUpdaterFsmDescrData = _CfprApCapabilityUpdaterFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 6),
    _CfprApCapabilityUpdaterFsmDescrData_Type()
)
cfprApCapabilityUpdaterFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmDescrData.setStatus("current")
_CfprApCapabilityUpdaterFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApCapabilityUpdaterFsmFsmStatus_Object = MibTableColumn
cfprApCapabilityUpdaterFsmFsmStatus = _CfprApCapabilityUpdaterFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 7),
    _CfprApCapabilityUpdaterFsmFsmStatus_Type()
)
cfprApCapabilityUpdaterFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmFsmStatus.setStatus("current")
_CfprApCapabilityUpdaterFsmProgress_Type = Gauge32
_CfprApCapabilityUpdaterFsmProgress_Object = MibTableColumn
cfprApCapabilityUpdaterFsmProgress = _CfprApCapabilityUpdaterFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 8),
    _CfprApCapabilityUpdaterFsmProgress_Type()
)
cfprApCapabilityUpdaterFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmProgress.setStatus("current")
_CfprApCapabilityUpdaterFsmRmtErrCode_Type = Gauge32
_CfprApCapabilityUpdaterFsmRmtErrCode_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRmtErrCode = _CfprApCapabilityUpdaterFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 9),
    _CfprApCapabilityUpdaterFsmRmtErrCode_Type()
)
cfprApCapabilityUpdaterFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRmtErrCode.setStatus("current")
_CfprApCapabilityUpdaterFsmRmtErrDescr_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmRmtErrDescr_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRmtErrDescr = _CfprApCapabilityUpdaterFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 10),
    _CfprApCapabilityUpdaterFsmRmtErrDescr_Type()
)
cfprApCapabilityUpdaterFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRmtErrDescr.setStatus("current")
_CfprApCapabilityUpdaterFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApCapabilityUpdaterFsmRmtRslt_Object = MibTableColumn
cfprApCapabilityUpdaterFsmRmtRslt = _CfprApCapabilityUpdaterFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 16, 1, 11),
    _CfprApCapabilityUpdaterFsmRmtRslt_Type()
)
cfprApCapabilityUpdaterFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmRmtRslt.setStatus("current")
_CfprApCapabilityUpdaterFsmStageTable_Object = MibTable
cfprApCapabilityUpdaterFsmStageTable = _CfprApCapabilityUpdaterFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17)
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageTable.setStatus("current")
_CfprApCapabilityUpdaterFsmStageEntry_Object = MibTableRow
cfprApCapabilityUpdaterFsmStageEntry = _CfprApCapabilityUpdaterFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1)
)
cfprApCapabilityUpdaterFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityUpdaterFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageEntry.setStatus("current")
_CfprApCapabilityUpdaterFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityUpdaterFsmStageInstanceId_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageInstanceId = _CfprApCapabilityUpdaterFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 1),
    _CfprApCapabilityUpdaterFsmStageInstanceId_Type()
)
cfprApCapabilityUpdaterFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageInstanceId.setStatus("current")
_CfprApCapabilityUpdaterFsmStageDn_Type = CfprApManagedObjectDn
_CfprApCapabilityUpdaterFsmStageDn_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageDn = _CfprApCapabilityUpdaterFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 2),
    _CfprApCapabilityUpdaterFsmStageDn_Type()
)
cfprApCapabilityUpdaterFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageDn.setStatus("current")
_CfprApCapabilityUpdaterFsmStageRn_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmStageRn_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageRn = _CfprApCapabilityUpdaterFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 3),
    _CfprApCapabilityUpdaterFsmStageRn_Type()
)
cfprApCapabilityUpdaterFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageRn.setStatus("current")
_CfprApCapabilityUpdaterFsmStageDescrData_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmStageDescrData_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageDescrData = _CfprApCapabilityUpdaterFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 4),
    _CfprApCapabilityUpdaterFsmStageDescrData_Type()
)
cfprApCapabilityUpdaterFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageDescrData.setStatus("current")
_CfprApCapabilityUpdaterFsmStageLastUpdateTime_Type = DateAndTime
_CfprApCapabilityUpdaterFsmStageLastUpdateTime_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageLastUpdateTime = _CfprApCapabilityUpdaterFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 5),
    _CfprApCapabilityUpdaterFsmStageLastUpdateTime_Type()
)
cfprApCapabilityUpdaterFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageLastUpdateTime.setStatus("current")
_CfprApCapabilityUpdaterFsmStageName_Type = CfprApCapabilityUpdaterFsmStageName
_CfprApCapabilityUpdaterFsmStageName_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageName = _CfprApCapabilityUpdaterFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 6),
    _CfprApCapabilityUpdaterFsmStageName_Type()
)
cfprApCapabilityUpdaterFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageName.setStatus("current")
_CfprApCapabilityUpdaterFsmStageOrder_Type = Gauge32
_CfprApCapabilityUpdaterFsmStageOrder_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageOrder = _CfprApCapabilityUpdaterFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 7),
    _CfprApCapabilityUpdaterFsmStageOrder_Type()
)
cfprApCapabilityUpdaterFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageOrder.setStatus("current")
_CfprApCapabilityUpdaterFsmStageRetry_Type = Gauge32
_CfprApCapabilityUpdaterFsmStageRetry_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageRetry = _CfprApCapabilityUpdaterFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 8),
    _CfprApCapabilityUpdaterFsmStageRetry_Type()
)
cfprApCapabilityUpdaterFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageRetry.setStatus("current")
_CfprApCapabilityUpdaterFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApCapabilityUpdaterFsmStageStageStatus_Object = MibTableColumn
cfprApCapabilityUpdaterFsmStageStageStatus = _CfprApCapabilityUpdaterFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 17, 1, 9),
    _CfprApCapabilityUpdaterFsmStageStageStatus_Type()
)
cfprApCapabilityUpdaterFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmStageStageStatus.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskTable_Object = MibTable
cfprApCapabilityUpdaterFsmTaskTable = _CfprApCapabilityUpdaterFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18)
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskTable.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskEntry_Object = MibTableRow
cfprApCapabilityUpdaterFsmTaskEntry = _CfprApCapabilityUpdaterFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1)
)
cfprApCapabilityUpdaterFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-CAPABILITY-MIB", "cfprApCapabilityUpdaterFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskEntry.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApCapabilityUpdaterFsmTaskInstanceId_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskInstanceId = _CfprApCapabilityUpdaterFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 1),
    _CfprApCapabilityUpdaterFsmTaskInstanceId_Type()
)
cfprApCapabilityUpdaterFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskInstanceId.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApCapabilityUpdaterFsmTaskDn_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskDn = _CfprApCapabilityUpdaterFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 2),
    _CfprApCapabilityUpdaterFsmTaskDn_Type()
)
cfprApCapabilityUpdaterFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskDn.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskRn_Type = SnmpAdminString
_CfprApCapabilityUpdaterFsmTaskRn_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskRn = _CfprApCapabilityUpdaterFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 3),
    _CfprApCapabilityUpdaterFsmTaskRn_Type()
)
cfprApCapabilityUpdaterFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskRn.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApCapabilityUpdaterFsmTaskCompletion_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskCompletion = _CfprApCapabilityUpdaterFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 4),
    _CfprApCapabilityUpdaterFsmTaskCompletion_Type()
)
cfprApCapabilityUpdaterFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskCompletion.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskFlags_Type = CfprApFsmFlags
_CfprApCapabilityUpdaterFsmTaskFlags_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskFlags = _CfprApCapabilityUpdaterFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 5),
    _CfprApCapabilityUpdaterFsmTaskFlags_Type()
)
cfprApCapabilityUpdaterFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskFlags.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskItem_Type = CfprApCapabilityUpdaterFsmTaskItem
_CfprApCapabilityUpdaterFsmTaskItem_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskItem = _CfprApCapabilityUpdaterFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 6),
    _CfprApCapabilityUpdaterFsmTaskItem_Type()
)
cfprApCapabilityUpdaterFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskItem.setStatus("current")
_CfprApCapabilityUpdaterFsmTaskSeqId_Type = Gauge32
_CfprApCapabilityUpdaterFsmTaskSeqId_Object = MibTableColumn
cfprApCapabilityUpdaterFsmTaskSeqId = _CfprApCapabilityUpdaterFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 8, 18, 1, 7),
    _CfprApCapabilityUpdaterFsmTaskSeqId_Type()
)
cfprApCapabilityUpdaterFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApCapabilityUpdaterFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-CAPABILITY-MIB",
    **{"cfprApCapabilityObjects": cfprApCapabilityObjects,
       "cfprApCapabilityCatalogueTable": cfprApCapabilityCatalogueTable,
       "cfprApCapabilityCatalogueEntry": cfprApCapabilityCatalogueEntry,
       "cfprApCapabilityCatalogueInstanceId": cfprApCapabilityCatalogueInstanceId,
       "cfprApCapabilityCatalogueDn": cfprApCapabilityCatalogueDn,
       "cfprApCapabilityCatalogueRn": cfprApCapabilityCatalogueRn,
       "cfprApCapabilityCatalogueFileParseFailures": cfprApCapabilityCatalogueFileParseFailures,
       "cfprApCapabilityCatalogueFilesParsed": cfprApCapabilityCatalogueFilesParsed,
       "cfprApCapabilityCatalogueFsmDescr": cfprApCapabilityCatalogueFsmDescr,
       "cfprApCapabilityCatalogueFsmPrev": cfprApCapabilityCatalogueFsmPrev,
       "cfprApCapabilityCatalogueFsmProgr": cfprApCapabilityCatalogueFsmProgr,
       "cfprApCapabilityCatalogueFsmRmtInvErrCode": cfprApCapabilityCatalogueFsmRmtInvErrCode,
       "cfprApCapabilityCatalogueFsmRmtInvErrDescr": cfprApCapabilityCatalogueFsmRmtInvErrDescr,
       "cfprApCapabilityCatalogueFsmRmtInvRslt": cfprApCapabilityCatalogueFsmRmtInvRslt,
       "cfprApCapabilityCatalogueFsmStageDescr": cfprApCapabilityCatalogueFsmStageDescr,
       "cfprApCapabilityCatalogueFsmStamp": cfprApCapabilityCatalogueFsmStamp,
       "cfprApCapabilityCatalogueFsmStatus": cfprApCapabilityCatalogueFsmStatus,
       "cfprApCapabilityCatalogueFsmTry": cfprApCapabilityCatalogueFsmTry,
       "cfprApCapabilityCatalogueLoadErrors": cfprApCapabilityCatalogueLoadErrors,
       "cfprApCapabilityCatalogueLoadWarnings": cfprApCapabilityCatalogueLoadWarnings,
       "cfprApCapabilityCatalogueProviderLoadFailures": cfprApCapabilityCatalogueProviderLoadFailures,
       "cfprApCapabilityCatalogueProvidersLoaded": cfprApCapabilityCatalogueProvidersLoaded,
       "cfprApCapabilityCatalogueVersion": cfprApCapabilityCatalogueVersion,
       "cfprApCapabilityCatalogueFsmTable": cfprApCapabilityCatalogueFsmTable,
       "cfprApCapabilityCatalogueFsmEntry": cfprApCapabilityCatalogueFsmEntry,
       "cfprApCapabilityCatalogueFsmInstanceId": cfprApCapabilityCatalogueFsmInstanceId,
       "cfprApCapabilityCatalogueFsmDn": cfprApCapabilityCatalogueFsmDn,
       "cfprApCapabilityCatalogueFsmRn": cfprApCapabilityCatalogueFsmRn,
       "cfprApCapabilityCatalogueFsmCompletionTime": cfprApCapabilityCatalogueFsmCompletionTime,
       "cfprApCapabilityCatalogueFsmCurrentFsm": cfprApCapabilityCatalogueFsmCurrentFsm,
       "cfprApCapabilityCatalogueFsmDescrData": cfprApCapabilityCatalogueFsmDescrData,
       "cfprApCapabilityCatalogueFsmFsmStatus": cfprApCapabilityCatalogueFsmFsmStatus,
       "cfprApCapabilityCatalogueFsmProgress": cfprApCapabilityCatalogueFsmProgress,
       "cfprApCapabilityCatalogueFsmRmtErrCode": cfprApCapabilityCatalogueFsmRmtErrCode,
       "cfprApCapabilityCatalogueFsmRmtErrDescr": cfprApCapabilityCatalogueFsmRmtErrDescr,
       "cfprApCapabilityCatalogueFsmRmtRslt": cfprApCapabilityCatalogueFsmRmtRslt,
       "cfprApCapabilityCatalogueFsmStageTable": cfprApCapabilityCatalogueFsmStageTable,
       "cfprApCapabilityCatalogueFsmStageEntry": cfprApCapabilityCatalogueFsmStageEntry,
       "cfprApCapabilityCatalogueFsmStageInstanceId": cfprApCapabilityCatalogueFsmStageInstanceId,
       "cfprApCapabilityCatalogueFsmStageDn": cfprApCapabilityCatalogueFsmStageDn,
       "cfprApCapabilityCatalogueFsmStageRn": cfprApCapabilityCatalogueFsmStageRn,
       "cfprApCapabilityCatalogueFsmStageDescrData": cfprApCapabilityCatalogueFsmStageDescrData,
       "cfprApCapabilityCatalogueFsmStageLastUpdateTime": cfprApCapabilityCatalogueFsmStageLastUpdateTime,
       "cfprApCapabilityCatalogueFsmStageName": cfprApCapabilityCatalogueFsmStageName,
       "cfprApCapabilityCatalogueFsmStageOrder": cfprApCapabilityCatalogueFsmStageOrder,
       "cfprApCapabilityCatalogueFsmStageRetry": cfprApCapabilityCatalogueFsmStageRetry,
       "cfprApCapabilityCatalogueFsmStageStageStatus": cfprApCapabilityCatalogueFsmStageStageStatus,
       "cfprApCapabilityCatalogueFsmTaskTable": cfprApCapabilityCatalogueFsmTaskTable,
       "cfprApCapabilityCatalogueFsmTaskEntry": cfprApCapabilityCatalogueFsmTaskEntry,
       "cfprApCapabilityCatalogueFsmTaskInstanceId": cfprApCapabilityCatalogueFsmTaskInstanceId,
       "cfprApCapabilityCatalogueFsmTaskDn": cfprApCapabilityCatalogueFsmTaskDn,
       "cfprApCapabilityCatalogueFsmTaskRn": cfprApCapabilityCatalogueFsmTaskRn,
       "cfprApCapabilityCatalogueFsmTaskCompletion": cfprApCapabilityCatalogueFsmTaskCompletion,
       "cfprApCapabilityCatalogueFsmTaskFlags": cfprApCapabilityCatalogueFsmTaskFlags,
       "cfprApCapabilityCatalogueFsmTaskItem": cfprApCapabilityCatalogueFsmTaskItem,
       "cfprApCapabilityCatalogueFsmTaskSeqId": cfprApCapabilityCatalogueFsmTaskSeqId,
       "cfprApCapabilityEpTable": cfprApCapabilityEpTable,
       "cfprApCapabilityEpEntry": cfprApCapabilityEpEntry,
       "cfprApCapabilityEpInstanceId": cfprApCapabilityEpInstanceId,
       "cfprApCapabilityEpDn": cfprApCapabilityEpDn,
       "cfprApCapabilityEpRn": cfprApCapabilityEpRn,
       "cfprApCapabilityFeatureLimitsTable": cfprApCapabilityFeatureLimitsTable,
       "cfprApCapabilityFeatureLimitsEntry": cfprApCapabilityFeatureLimitsEntry,
       "cfprApCapabilityFeatureLimitsInstanceId": cfprApCapabilityFeatureLimitsInstanceId,
       "cfprApCapabilityFeatureLimitsDn": cfprApCapabilityFeatureLimitsDn,
       "cfprApCapabilityFeatureLimitsRn": cfprApCapabilityFeatureLimitsRn,
       "cfprApCapabilityFeatureLimitsDescr": cfprApCapabilityFeatureLimitsDescr,
       "cfprApCapabilityFeatureLimitsFeatureStatus": cfprApCapabilityFeatureLimitsFeatureStatus,
       "cfprApCapabilityFeatureLimitsLimit": cfprApCapabilityFeatureLimitsLimit,
       "cfprApCapabilityFeatureLimitsName": cfprApCapabilityFeatureLimitsName,
       "cfprApCapabilityFeatureLimitsPlatform": cfprApCapabilityFeatureLimitsPlatform,
       "cfprApCapabilityMgmtExtensionTable": cfprApCapabilityMgmtExtensionTable,
       "cfprApCapabilityMgmtExtensionEntry": cfprApCapabilityMgmtExtensionEntry,
       "cfprApCapabilityMgmtExtensionInstanceId": cfprApCapabilityMgmtExtensionInstanceId,
       "cfprApCapabilityMgmtExtensionDn": cfprApCapabilityMgmtExtensionDn,
       "cfprApCapabilityMgmtExtensionRn": cfprApCapabilityMgmtExtensionRn,
       "cfprApCapabilityMgmtExtensionFsmDescr": cfprApCapabilityMgmtExtensionFsmDescr,
       "cfprApCapabilityMgmtExtensionFsmPrev": cfprApCapabilityMgmtExtensionFsmPrev,
       "cfprApCapabilityMgmtExtensionFsmProgr": cfprApCapabilityMgmtExtensionFsmProgr,
       "cfprApCapabilityMgmtExtensionFsmRmtInvErrCode": cfprApCapabilityMgmtExtensionFsmRmtInvErrCode,
       "cfprApCapabilityMgmtExtensionFsmRmtInvErrDescr": cfprApCapabilityMgmtExtensionFsmRmtInvErrDescr,
       "cfprApCapabilityMgmtExtensionFsmRmtInvRslt": cfprApCapabilityMgmtExtensionFsmRmtInvRslt,
       "cfprApCapabilityMgmtExtensionFsmStageDescr": cfprApCapabilityMgmtExtensionFsmStageDescr,
       "cfprApCapabilityMgmtExtensionFsmStamp": cfprApCapabilityMgmtExtensionFsmStamp,
       "cfprApCapabilityMgmtExtensionFsmStatus": cfprApCapabilityMgmtExtensionFsmStatus,
       "cfprApCapabilityMgmtExtensionFsmTry": cfprApCapabilityMgmtExtensionFsmTry,
       "cfprApCapabilityMgmtExtensionFsmTable": cfprApCapabilityMgmtExtensionFsmTable,
       "cfprApCapabilityMgmtExtensionFsmEntry": cfprApCapabilityMgmtExtensionFsmEntry,
       "cfprApCapabilityMgmtExtensionFsmInstanceId": cfprApCapabilityMgmtExtensionFsmInstanceId,
       "cfprApCapabilityMgmtExtensionFsmDn": cfprApCapabilityMgmtExtensionFsmDn,
       "cfprApCapabilityMgmtExtensionFsmRn": cfprApCapabilityMgmtExtensionFsmRn,
       "cfprApCapabilityMgmtExtensionFsmCompletionTime": cfprApCapabilityMgmtExtensionFsmCompletionTime,
       "cfprApCapabilityMgmtExtensionFsmCurrentFsm": cfprApCapabilityMgmtExtensionFsmCurrentFsm,
       "cfprApCapabilityMgmtExtensionFsmDescrData": cfprApCapabilityMgmtExtensionFsmDescrData,
       "cfprApCapabilityMgmtExtensionFsmFsmStatus": cfprApCapabilityMgmtExtensionFsmFsmStatus,
       "cfprApCapabilityMgmtExtensionFsmProgress": cfprApCapabilityMgmtExtensionFsmProgress,
       "cfprApCapabilityMgmtExtensionFsmRmtErrCode": cfprApCapabilityMgmtExtensionFsmRmtErrCode,
       "cfprApCapabilityMgmtExtensionFsmRmtErrDescr": cfprApCapabilityMgmtExtensionFsmRmtErrDescr,
       "cfprApCapabilityMgmtExtensionFsmRmtRslt": cfprApCapabilityMgmtExtensionFsmRmtRslt,
       "cfprApCapabilityMgmtExtensionFsmStageTable": cfprApCapabilityMgmtExtensionFsmStageTable,
       "cfprApCapabilityMgmtExtensionFsmStageEntry": cfprApCapabilityMgmtExtensionFsmStageEntry,
       "cfprApCapabilityMgmtExtensionFsmStageInstanceId": cfprApCapabilityMgmtExtensionFsmStageInstanceId,
       "cfprApCapabilityMgmtExtensionFsmStageDn": cfprApCapabilityMgmtExtensionFsmStageDn,
       "cfprApCapabilityMgmtExtensionFsmStageRn": cfprApCapabilityMgmtExtensionFsmStageRn,
       "cfprApCapabilityMgmtExtensionFsmStageDescrData": cfprApCapabilityMgmtExtensionFsmStageDescrData,
       "cfprApCapabilityMgmtExtensionFsmStageLastUpdateTime": cfprApCapabilityMgmtExtensionFsmStageLastUpdateTime,
       "cfprApCapabilityMgmtExtensionFsmStageName": cfprApCapabilityMgmtExtensionFsmStageName,
       "cfprApCapabilityMgmtExtensionFsmStageOrder": cfprApCapabilityMgmtExtensionFsmStageOrder,
       "cfprApCapabilityMgmtExtensionFsmStageRetry": cfprApCapabilityMgmtExtensionFsmStageRetry,
       "cfprApCapabilityMgmtExtensionFsmStageStageStatus": cfprApCapabilityMgmtExtensionFsmStageStageStatus,
       "cfprApCapabilityMgmtExtensionFsmTaskTable": cfprApCapabilityMgmtExtensionFsmTaskTable,
       "cfprApCapabilityMgmtExtensionFsmTaskEntry": cfprApCapabilityMgmtExtensionFsmTaskEntry,
       "cfprApCapabilityMgmtExtensionFsmTaskInstanceId": cfprApCapabilityMgmtExtensionFsmTaskInstanceId,
       "cfprApCapabilityMgmtExtensionFsmTaskDn": cfprApCapabilityMgmtExtensionFsmTaskDn,
       "cfprApCapabilityMgmtExtensionFsmTaskRn": cfprApCapabilityMgmtExtensionFsmTaskRn,
       "cfprApCapabilityMgmtExtensionFsmTaskCompletion": cfprApCapabilityMgmtExtensionFsmTaskCompletion,
       "cfprApCapabilityMgmtExtensionFsmTaskFlags": cfprApCapabilityMgmtExtensionFsmTaskFlags,
       "cfprApCapabilityMgmtExtensionFsmTaskItem": cfprApCapabilityMgmtExtensionFsmTaskItem,
       "cfprApCapabilityMgmtExtensionFsmTaskSeqId": cfprApCapabilityMgmtExtensionFsmTaskSeqId,
       "cfprApCapabilityNetworkLimitsTable": cfprApCapabilityNetworkLimitsTable,
       "cfprApCapabilityNetworkLimitsEntry": cfprApCapabilityNetworkLimitsEntry,
       "cfprApCapabilityNetworkLimitsInstanceId": cfprApCapabilityNetworkLimitsInstanceId,
       "cfprApCapabilityNetworkLimitsDn": cfprApCapabilityNetworkLimitsDn,
       "cfprApCapabilityNetworkLimitsRn": cfprApCapabilityNetworkLimitsRn,
       "cfprApCapabilityStorageLimitsTable": cfprApCapabilityStorageLimitsTable,
       "cfprApCapabilityStorageLimitsEntry": cfprApCapabilityStorageLimitsEntry,
       "cfprApCapabilityStorageLimitsInstanceId": cfprApCapabilityStorageLimitsInstanceId,
       "cfprApCapabilityStorageLimitsDn": cfprApCapabilityStorageLimitsDn,
       "cfprApCapabilityStorageLimitsRn": cfprApCapabilityStorageLimitsRn,
       "cfprApCapabilitySystemLimitsTable": cfprApCapabilitySystemLimitsTable,
       "cfprApCapabilitySystemLimitsEntry": cfprApCapabilitySystemLimitsEntry,
       "cfprApCapabilitySystemLimitsInstanceId": cfprApCapabilitySystemLimitsInstanceId,
       "cfprApCapabilitySystemLimitsDn": cfprApCapabilitySystemLimitsDn,
       "cfprApCapabilitySystemLimitsRn": cfprApCapabilitySystemLimitsRn,
       "cfprApCapabilityUpdateTable": cfprApCapabilityUpdateTable,
       "cfprApCapabilityUpdateEntry": cfprApCapabilityUpdateEntry,
       "cfprApCapabilityUpdateInstanceId": cfprApCapabilityUpdateInstanceId,
       "cfprApCapabilityUpdateDn": cfprApCapabilityUpdateDn,
       "cfprApCapabilityUpdateRn": cfprApCapabilityUpdateRn,
       "cfprApCapabilityUpdateImageName": cfprApCapabilityUpdateImageName,
       "cfprApCapabilityUpdateUpdateTs": cfprApCapabilityUpdateUpdateTs,
       "cfprApCapabilityUpdateVersion": cfprApCapabilityUpdateVersion,
       "cfprApCapabilityUpdaterTable": cfprApCapabilityUpdaterTable,
       "cfprApCapabilityUpdaterEntry": cfprApCapabilityUpdaterEntry,
       "cfprApCapabilityUpdaterInstanceId": cfprApCapabilityUpdaterInstanceId,
       "cfprApCapabilityUpdaterDn": cfprApCapabilityUpdaterDn,
       "cfprApCapabilityUpdaterRn": cfprApCapabilityUpdaterRn,
       "cfprApCapabilityUpdaterAdminState": cfprApCapabilityUpdaterAdminState,
       "cfprApCapabilityUpdaterFileName": cfprApCapabilityUpdaterFileName,
       "cfprApCapabilityUpdaterFsmDescr": cfprApCapabilityUpdaterFsmDescr,
       "cfprApCapabilityUpdaterFsmPrev": cfprApCapabilityUpdaterFsmPrev,
       "cfprApCapabilityUpdaterFsmProgr": cfprApCapabilityUpdaterFsmProgr,
       "cfprApCapabilityUpdaterFsmRmtInvErrCode": cfprApCapabilityUpdaterFsmRmtInvErrCode,
       "cfprApCapabilityUpdaterFsmRmtInvErrDescr": cfprApCapabilityUpdaterFsmRmtInvErrDescr,
       "cfprApCapabilityUpdaterFsmRmtInvRslt": cfprApCapabilityUpdaterFsmRmtInvRslt,
       "cfprApCapabilityUpdaterFsmStageDescr": cfprApCapabilityUpdaterFsmStageDescr,
       "cfprApCapabilityUpdaterFsmStamp": cfprApCapabilityUpdaterFsmStamp,
       "cfprApCapabilityUpdaterFsmStatus": cfprApCapabilityUpdaterFsmStatus,
       "cfprApCapabilityUpdaterFsmTry": cfprApCapabilityUpdaterFsmTry,
       "cfprApCapabilityUpdaterImageName": cfprApCapabilityUpdaterImageName,
       "cfprApCapabilityUpdaterOperState": cfprApCapabilityUpdaterOperState,
       "cfprApCapabilityUpdaterProtocol": cfprApCapabilityUpdaterProtocol,
       "cfprApCapabilityUpdaterPwd": cfprApCapabilityUpdaterPwd,
       "cfprApCapabilityUpdaterRemotePath": cfprApCapabilityUpdaterRemotePath,
       "cfprApCapabilityUpdaterServer": cfprApCapabilityUpdaterServer,
       "cfprApCapabilityUpdaterUser": cfprApCapabilityUpdaterUser,
       "cfprApCapabilityUpdaterVersion": cfprApCapabilityUpdaterVersion,
       "cfprApCapabilityUpdaterFsmTable": cfprApCapabilityUpdaterFsmTable,
       "cfprApCapabilityUpdaterFsmEntry": cfprApCapabilityUpdaterFsmEntry,
       "cfprApCapabilityUpdaterFsmInstanceId": cfprApCapabilityUpdaterFsmInstanceId,
       "cfprApCapabilityUpdaterFsmDn": cfprApCapabilityUpdaterFsmDn,
       "cfprApCapabilityUpdaterFsmRn": cfprApCapabilityUpdaterFsmRn,
       "cfprApCapabilityUpdaterFsmCompletionTime": cfprApCapabilityUpdaterFsmCompletionTime,
       "cfprApCapabilityUpdaterFsmCurrentFsm": cfprApCapabilityUpdaterFsmCurrentFsm,
       "cfprApCapabilityUpdaterFsmDescrData": cfprApCapabilityUpdaterFsmDescrData,
       "cfprApCapabilityUpdaterFsmFsmStatus": cfprApCapabilityUpdaterFsmFsmStatus,
       "cfprApCapabilityUpdaterFsmProgress": cfprApCapabilityUpdaterFsmProgress,
       "cfprApCapabilityUpdaterFsmRmtErrCode": cfprApCapabilityUpdaterFsmRmtErrCode,
       "cfprApCapabilityUpdaterFsmRmtErrDescr": cfprApCapabilityUpdaterFsmRmtErrDescr,
       "cfprApCapabilityUpdaterFsmRmtRslt": cfprApCapabilityUpdaterFsmRmtRslt,
       "cfprApCapabilityUpdaterFsmStageTable": cfprApCapabilityUpdaterFsmStageTable,
       "cfprApCapabilityUpdaterFsmStageEntry": cfprApCapabilityUpdaterFsmStageEntry,
       "cfprApCapabilityUpdaterFsmStageInstanceId": cfprApCapabilityUpdaterFsmStageInstanceId,
       "cfprApCapabilityUpdaterFsmStageDn": cfprApCapabilityUpdaterFsmStageDn,
       "cfprApCapabilityUpdaterFsmStageRn": cfprApCapabilityUpdaterFsmStageRn,
       "cfprApCapabilityUpdaterFsmStageDescrData": cfprApCapabilityUpdaterFsmStageDescrData,
       "cfprApCapabilityUpdaterFsmStageLastUpdateTime": cfprApCapabilityUpdaterFsmStageLastUpdateTime,
       "cfprApCapabilityUpdaterFsmStageName": cfprApCapabilityUpdaterFsmStageName,
       "cfprApCapabilityUpdaterFsmStageOrder": cfprApCapabilityUpdaterFsmStageOrder,
       "cfprApCapabilityUpdaterFsmStageRetry": cfprApCapabilityUpdaterFsmStageRetry,
       "cfprApCapabilityUpdaterFsmStageStageStatus": cfprApCapabilityUpdaterFsmStageStageStatus,
       "cfprApCapabilityUpdaterFsmTaskTable": cfprApCapabilityUpdaterFsmTaskTable,
       "cfprApCapabilityUpdaterFsmTaskEntry": cfprApCapabilityUpdaterFsmTaskEntry,
       "cfprApCapabilityUpdaterFsmTaskInstanceId": cfprApCapabilityUpdaterFsmTaskInstanceId,
       "cfprApCapabilityUpdaterFsmTaskDn": cfprApCapabilityUpdaterFsmTaskDn,
       "cfprApCapabilityUpdaterFsmTaskRn": cfprApCapabilityUpdaterFsmTaskRn,
       "cfprApCapabilityUpdaterFsmTaskCompletion": cfprApCapabilityUpdaterFsmTaskCompletion,
       "cfprApCapabilityUpdaterFsmTaskFlags": cfprApCapabilityUpdaterFsmTaskFlags,
       "cfprApCapabilityUpdaterFsmTaskItem": cfprApCapabilityUpdaterFsmTaskItem,
       "cfprApCapabilityUpdaterFsmTaskSeqId": cfprApCapabilityUpdaterFsmTaskSeqId}
)
