# SNMP MIB module (CISCO-FIREPOWER-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-VM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:13 2025
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

(CfprAdaptorLinkState,
 CfprAdaptorServiceState,
 CfprConditionRemoteInvRslt,
 CfprDcxOperState,
 CfprExtvmmOwnership,
 CfprFabricAVlanAssocPrimaryVlanSwitchId,
 CfprFabricAVlanSharing,
 CfprFabricAVlanTransport,
 CfprFabricAVlanType,
 CfprFabricAVsanTransport,
 CfprFabricAVsanType,
 CfprFabricVlanAssocPrimaryVlanState,
 CfprFabricVlanOperState,
 CfprFabricVlanOverlapState,
 CfprFabricVnetEpIfRole,
 CfprFabricVnetEpLocale,
 CfprFabricVnetEpPolicyOwner,
 CfprFabricVsanOperState,
 CfprFabricZoningState,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprNetworkSwitchId,
 CfprNetworkVnetEpIfType,
 CfprOsOsType,
 CfprPolicyPolicyOwner,
 CfprVmAdaptorOwner,
 CfprVmComputeEpClInstType,
 CfprVmHbaType,
 CfprVmHvClInstType,
 CfprVmHvType,
 CfprVmInstType,
 CfprVmLifeCyclePolicyFsmCurrentFsm,
 CfprVmLifeCyclePolicyFsmStageName,
 CfprVmLifeCyclePolicyFsmTaskItem,
 CfprVmMgmtPlane,
 CfprVmNicType,
 CfprVmOsHvVendor,
 CfprVmStatus,
 CfprVmSwitchAdminState,
 CfprVmSwitchVendor,
 CfprVnicPortProfileType) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAdaptorLinkState",
    "CfprAdaptorServiceState",
    "CfprConditionRemoteInvRslt",
    "CfprDcxOperState",
    "CfprExtvmmOwnership",
    "CfprFabricAVlanAssocPrimaryVlanSwitchId",
    "CfprFabricAVlanSharing",
    "CfprFabricAVlanTransport",
    "CfprFabricAVlanType",
    "CfprFabricAVsanTransport",
    "CfprFabricAVsanType",
    "CfprFabricVlanAssocPrimaryVlanState",
    "CfprFabricVlanOperState",
    "CfprFabricVlanOverlapState",
    "CfprFabricVnetEpIfRole",
    "CfprFabricVnetEpLocale",
    "CfprFabricVnetEpPolicyOwner",
    "CfprFabricVsanOperState",
    "CfprFabricZoningState",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprNetworkSwitchId",
    "CfprNetworkVnetEpIfType",
    "CfprOsOsType",
    "CfprPolicyPolicyOwner",
    "CfprVmAdaptorOwner",
    "CfprVmComputeEpClInstType",
    "CfprVmHbaType",
    "CfprVmHvClInstType",
    "CfprVmHvType",
    "CfprVmInstType",
    "CfprVmLifeCyclePolicyFsmCurrentFsm",
    "CfprVmLifeCyclePolicyFsmStageName",
    "CfprVmLifeCyclePolicyFsmTaskItem",
    "CfprVmMgmtPlane",
    "CfprVmNicType",
    "CfprVmOsHvVendor",
    "CfprVmStatus",
    "CfprVmSwitchAdminState",
    "CfprVmSwitchVendor",
    "CfprVnicPortProfileType")

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

cfprVmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprVmComputeEpTable_Object = MibTable
cfprVmComputeEpTable = _CfprVmComputeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1)
)
if mibBuilder.loadTexts:
    cfprVmComputeEpTable.setStatus("current")
_CfprVmComputeEpEntry_Object = MibTableRow
cfprVmComputeEpEntry = _CfprVmComputeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1)
)
cfprVmComputeEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmComputeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmComputeEpEntry.setStatus("current")
_CfprVmComputeEpInstanceId_Type = CfprManagedObjectId
_CfprVmComputeEpInstanceId_Object = MibTableColumn
cfprVmComputeEpInstanceId = _CfprVmComputeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 1),
    _CfprVmComputeEpInstanceId_Type()
)
cfprVmComputeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmComputeEpInstanceId.setStatus("current")
_CfprVmComputeEpDn_Type = CfprManagedObjectDn
_CfprVmComputeEpDn_Object = MibTableColumn
cfprVmComputeEpDn = _CfprVmComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 2),
    _CfprVmComputeEpDn_Type()
)
cfprVmComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpDn.setStatus("current")
_CfprVmComputeEpRn_Type = SnmpAdminString
_CfprVmComputeEpRn_Object = MibTableColumn
cfprVmComputeEpRn = _CfprVmComputeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 3),
    _CfprVmComputeEpRn_Type()
)
cfprVmComputeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpRn.setStatus("current")
_CfprVmComputeEpClInstType_Type = CfprVmComputeEpClInstType
_CfprVmComputeEpClInstType_Object = MibTableColumn
cfprVmComputeEpClInstType = _CfprVmComputeEpClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 4),
    _CfprVmComputeEpClInstType_Type()
)
cfprVmComputeEpClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpClInstType.setStatus("current")
_CfprVmComputeEpComputeEpVendor_Type = SnmpAdminString
_CfprVmComputeEpComputeEpVendor_Object = MibTableColumn
cfprVmComputeEpComputeEpVendor = _CfprVmComputeEpComputeEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 5),
    _CfprVmComputeEpComputeEpVendor_Type()
)
cfprVmComputeEpComputeEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpComputeEpVendor.setStatus("current")
_CfprVmComputeEpDescr_Type = SnmpAdminString
_CfprVmComputeEpDescr_Object = MibTableColumn
cfprVmComputeEpDescr = _CfprVmComputeEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 6),
    _CfprVmComputeEpDescr_Type()
)
cfprVmComputeEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpDescr.setStatus("current")
_CfprVmComputeEpDvsDn_Type = SnmpAdminString
_CfprVmComputeEpDvsDn_Object = MibTableColumn
cfprVmComputeEpDvsDn = _CfprVmComputeEpDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 7),
    _CfprVmComputeEpDvsDn_Type()
)
cfprVmComputeEpDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpDvsDn.setStatus("current")
_CfprVmComputeEpDvsName_Type = SnmpAdminString
_CfprVmComputeEpDvsName_Object = MibTableColumn
cfprVmComputeEpDvsName = _CfprVmComputeEpDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 8),
    _CfprVmComputeEpDvsName_Type()
)
cfprVmComputeEpDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpDvsName.setStatus("current")
_CfprVmComputeEpHostName_Type = SnmpAdminString
_CfprVmComputeEpHostName_Object = MibTableColumn
cfprVmComputeEpHostName = _CfprVmComputeEpHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 9),
    _CfprVmComputeEpHostName_Type()
)
cfprVmComputeEpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpHostName.setStatus("current")
_CfprVmComputeEpIntId_Type = SnmpAdminString
_CfprVmComputeEpIntId_Object = MibTableColumn
cfprVmComputeEpIntId = _CfprVmComputeEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 10),
    _CfprVmComputeEpIntId_Type()
)
cfprVmComputeEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpIntId.setStatus("current")
_CfprVmComputeEpLsDn_Type = SnmpAdminString
_CfprVmComputeEpLsDn_Object = MibTableColumn
cfprVmComputeEpLsDn = _CfprVmComputeEpLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 11),
    _CfprVmComputeEpLsDn_Type()
)
cfprVmComputeEpLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpLsDn.setStatus("current")
_CfprVmComputeEpModel_Type = CfprOsOsType
_CfprVmComputeEpModel_Object = MibTableColumn
cfprVmComputeEpModel = _CfprVmComputeEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 12),
    _CfprVmComputeEpModel_Type()
)
cfprVmComputeEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpModel.setStatus("current")
_CfprVmComputeEpName_Type = SnmpAdminString
_CfprVmComputeEpName_Object = MibTableColumn
cfprVmComputeEpName = _CfprVmComputeEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 13),
    _CfprVmComputeEpName_Type()
)
cfprVmComputeEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpName.setStatus("current")
_CfprVmComputeEpPnDn_Type = SnmpAdminString
_CfprVmComputeEpPnDn_Object = MibTableColumn
cfprVmComputeEpPnDn = _CfprVmComputeEpPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 14),
    _CfprVmComputeEpPnDn_Type()
)
cfprVmComputeEpPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpPnDn.setStatus("current")
_CfprVmComputeEpPolicyLevel_Type = Gauge32
_CfprVmComputeEpPolicyLevel_Object = MibTableColumn
cfprVmComputeEpPolicyLevel = _CfprVmComputeEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 15),
    _CfprVmComputeEpPolicyLevel_Type()
)
cfprVmComputeEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpPolicyLevel.setStatus("current")
_CfprVmComputeEpPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmComputeEpPolicyOwner_Object = MibTableColumn
cfprVmComputeEpPolicyOwner = _CfprVmComputeEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 16),
    _CfprVmComputeEpPolicyOwner_Type()
)
cfprVmComputeEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpPolicyOwner.setStatus("current")
_CfprVmComputeEpStatusChangeTs_Type = DateAndTime
_CfprVmComputeEpStatusChangeTs_Object = MibTableColumn
cfprVmComputeEpStatusChangeTs = _CfprVmComputeEpStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 17),
    _CfprVmComputeEpStatusChangeTs_Type()
)
cfprVmComputeEpStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpStatusChangeTs.setStatus("current")
_CfprVmComputeEpUuid_Type = SnmpAdminString
_CfprVmComputeEpUuid_Object = MibTableColumn
cfprVmComputeEpUuid = _CfprVmComputeEpUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 18),
    _CfprVmComputeEpUuid_Type()
)
cfprVmComputeEpUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpUuid.setStatus("current")
_CfprVmComputeEpVStatus_Type = CfprVmStatus
_CfprVmComputeEpVStatus_Object = MibTableColumn
cfprVmComputeEpVStatus = _CfprVmComputeEpVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 19),
    _CfprVmComputeEpVStatus_Type()
)
cfprVmComputeEpVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpVStatus.setStatus("current")
_CfprVmComputeEpVendor_Type = CfprVmOsHvVendor
_CfprVmComputeEpVendor_Object = MibTableColumn
cfprVmComputeEpVendor = _CfprVmComputeEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 1, 1, 20),
    _CfprVmComputeEpVendor_Type()
)
cfprVmComputeEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmComputeEpVendor.setStatus("current")
_CfprVmDCTable_Object = MibTable
cfprVmDCTable = _CfprVmDCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2)
)
if mibBuilder.loadTexts:
    cfprVmDCTable.setStatus("current")
_CfprVmDCEntry_Object = MibTableRow
cfprVmDCEntry = _CfprVmDCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1)
)
cfprVmDCEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmDCInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmDCEntry.setStatus("current")
_CfprVmDCInstanceId_Type = CfprManagedObjectId
_CfprVmDCInstanceId_Object = MibTableColumn
cfprVmDCInstanceId = _CfprVmDCInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 1),
    _CfprVmDCInstanceId_Type()
)
cfprVmDCInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmDCInstanceId.setStatus("current")
_CfprVmDCDn_Type = CfprManagedObjectDn
_CfprVmDCDn_Object = MibTableColumn
cfprVmDCDn = _CfprVmDCDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 2),
    _CfprVmDCDn_Type()
)
cfprVmDCDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCDn.setStatus("current")
_CfprVmDCRn_Type = SnmpAdminString
_CfprVmDCRn_Object = MibTableColumn
cfprVmDCRn = _CfprVmDCRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 3),
    _CfprVmDCRn_Type()
)
cfprVmDCRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCRn.setStatus("current")
_CfprVmDCDescr_Type = SnmpAdminString
_CfprVmDCDescr_Object = MibTableColumn
cfprVmDCDescr = _CfprVmDCDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 4),
    _CfprVmDCDescr_Type()
)
cfprVmDCDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCDescr.setStatus("current")
_CfprVmDCIntId_Type = SnmpAdminString
_CfprVmDCIntId_Object = MibTableColumn
cfprVmDCIntId = _CfprVmDCIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 5),
    _CfprVmDCIntId_Type()
)
cfprVmDCIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCIntId.setStatus("current")
_CfprVmDCName_Type = SnmpAdminString
_CfprVmDCName_Object = MibTableColumn
cfprVmDCName = _CfprVmDCName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 6),
    _CfprVmDCName_Type()
)
cfprVmDCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCName.setStatus("current")
_CfprVmDCOwn_Type = CfprExtvmmOwnership
_CfprVmDCOwn_Object = MibTableColumn
cfprVmDCOwn = _CfprVmDCOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 7),
    _CfprVmDCOwn_Type()
)
cfprVmDCOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOwn.setStatus("current")
_CfprVmDCPolicyLevel_Type = Gauge32
_CfprVmDCPolicyLevel_Object = MibTableColumn
cfprVmDCPolicyLevel = _CfprVmDCPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 8),
    _CfprVmDCPolicyLevel_Type()
)
cfprVmDCPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCPolicyLevel.setStatus("current")
_CfprVmDCPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmDCPolicyOwner_Object = MibTableColumn
cfprVmDCPolicyOwner = _CfprVmDCPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 9),
    _CfprVmDCPolicyOwner_Type()
)
cfprVmDCPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCPolicyOwner.setStatus("current")
_CfprVmDCUuid_Type = SnmpAdminString
_CfprVmDCUuid_Object = MibTableColumn
cfprVmDCUuid = _CfprVmDCUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 2, 1, 10),
    _CfprVmDCUuid_Type()
)
cfprVmDCUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCUuid.setStatus("current")
_CfprVmDCOrgTable_Object = MibTable
cfprVmDCOrgTable = _CfprVmDCOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3)
)
if mibBuilder.loadTexts:
    cfprVmDCOrgTable.setStatus("current")
_CfprVmDCOrgEntry_Object = MibTableRow
cfprVmDCOrgEntry = _CfprVmDCOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1)
)
cfprVmDCOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmDCOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmDCOrgEntry.setStatus("current")
_CfprVmDCOrgInstanceId_Type = CfprManagedObjectId
_CfprVmDCOrgInstanceId_Object = MibTableColumn
cfprVmDCOrgInstanceId = _CfprVmDCOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 1),
    _CfprVmDCOrgInstanceId_Type()
)
cfprVmDCOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmDCOrgInstanceId.setStatus("current")
_CfprVmDCOrgDn_Type = CfprManagedObjectDn
_CfprVmDCOrgDn_Object = MibTableColumn
cfprVmDCOrgDn = _CfprVmDCOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 2),
    _CfprVmDCOrgDn_Type()
)
cfprVmDCOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgDn.setStatus("current")
_CfprVmDCOrgRn_Type = SnmpAdminString
_CfprVmDCOrgRn_Object = MibTableColumn
cfprVmDCOrgRn = _CfprVmDCOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 3),
    _CfprVmDCOrgRn_Type()
)
cfprVmDCOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgRn.setStatus("current")
_CfprVmDCOrgDescr_Type = SnmpAdminString
_CfprVmDCOrgDescr_Object = MibTableColumn
cfprVmDCOrgDescr = _CfprVmDCOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 4),
    _CfprVmDCOrgDescr_Type()
)
cfprVmDCOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgDescr.setStatus("current")
_CfprVmDCOrgIntId_Type = SnmpAdminString
_CfprVmDCOrgIntId_Object = MibTableColumn
cfprVmDCOrgIntId = _CfprVmDCOrgIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 5),
    _CfprVmDCOrgIntId_Type()
)
cfprVmDCOrgIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgIntId.setStatus("current")
_CfprVmDCOrgName_Type = SnmpAdminString
_CfprVmDCOrgName_Object = MibTableColumn
cfprVmDCOrgName = _CfprVmDCOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 6),
    _CfprVmDCOrgName_Type()
)
cfprVmDCOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgName.setStatus("current")
_CfprVmDCOrgOwn_Type = CfprExtvmmOwnership
_CfprVmDCOrgOwn_Object = MibTableColumn
cfprVmDCOrgOwn = _CfprVmDCOrgOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 7),
    _CfprVmDCOrgOwn_Type()
)
cfprVmDCOrgOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgOwn.setStatus("current")
_CfprVmDCOrgPolicyLevel_Type = Gauge32
_CfprVmDCOrgPolicyLevel_Object = MibTableColumn
cfprVmDCOrgPolicyLevel = _CfprVmDCOrgPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 8),
    _CfprVmDCOrgPolicyLevel_Type()
)
cfprVmDCOrgPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgPolicyLevel.setStatus("current")
_CfprVmDCOrgPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmDCOrgPolicyOwner_Object = MibTableColumn
cfprVmDCOrgPolicyOwner = _CfprVmDCOrgPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 9),
    _CfprVmDCOrgPolicyOwner_Type()
)
cfprVmDCOrgPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgPolicyOwner.setStatus("current")
_CfprVmDCOrgUuid_Type = SnmpAdminString
_CfprVmDCOrgUuid_Object = MibTableColumn
cfprVmDCOrgUuid = _CfprVmDCOrgUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 3, 1, 10),
    _CfprVmDCOrgUuid_Type()
)
cfprVmDCOrgUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmDCOrgUuid.setStatus("current")
_CfprVmEpTable_Object = MibTable
cfprVmEpTable = _CfprVmEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 4)
)
if mibBuilder.loadTexts:
    cfprVmEpTable.setStatus("current")
_CfprVmEpEntry_Object = MibTableRow
cfprVmEpEntry = _CfprVmEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 4, 1)
)
cfprVmEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmEpEntry.setStatus("current")
_CfprVmEpInstanceId_Type = CfprManagedObjectId
_CfprVmEpInstanceId_Object = MibTableColumn
cfprVmEpInstanceId = _CfprVmEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 4, 1, 1),
    _CfprVmEpInstanceId_Type()
)
cfprVmEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmEpInstanceId.setStatus("current")
_CfprVmEpDn_Type = CfprManagedObjectDn
_CfprVmEpDn_Object = MibTableColumn
cfprVmEpDn = _CfprVmEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 4, 1, 2),
    _CfprVmEpDn_Type()
)
cfprVmEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmEpDn.setStatus("current")
_CfprVmEpRn_Type = SnmpAdminString
_CfprVmEpRn_Object = MibTableColumn
cfprVmEpRn = _CfprVmEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 4, 1, 3),
    _CfprVmEpRn_Type()
)
cfprVmEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmEpRn.setStatus("current")
_CfprVmHbaTable_Object = MibTable
cfprVmHbaTable = _CfprVmHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5)
)
if mibBuilder.loadTexts:
    cfprVmHbaTable.setStatus("current")
_CfprVmHbaEntry_Object = MibTableRow
cfprVmHbaEntry = _CfprVmHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1)
)
cfprVmHbaEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmHbaInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmHbaEntry.setStatus("current")
_CfprVmHbaInstanceId_Type = CfprManagedObjectId
_CfprVmHbaInstanceId_Object = MibTableColumn
cfprVmHbaInstanceId = _CfprVmHbaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 1),
    _CfprVmHbaInstanceId_Type()
)
cfprVmHbaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmHbaInstanceId.setStatus("current")
_CfprVmHbaDn_Type = CfprManagedObjectDn
_CfprVmHbaDn_Object = MibTableColumn
cfprVmHbaDn = _CfprVmHbaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 2),
    _CfprVmHbaDn_Type()
)
cfprVmHbaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaDn.setStatus("current")
_CfprVmHbaRn_Type = SnmpAdminString
_CfprVmHbaRn_Object = MibTableColumn
cfprVmHbaRn = _CfprVmHbaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 3),
    _CfprVmHbaRn_Type()
)
cfprVmHbaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaRn.setStatus("current")
_CfprVmHbaDvsGenPortId_Type = SnmpAdminString
_CfprVmHbaDvsGenPortId_Object = MibTableColumn
cfprVmHbaDvsGenPortId = _CfprVmHbaDvsGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 4),
    _CfprVmHbaDvsGenPortId_Type()
)
cfprVmHbaDvsGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaDvsGenPortId.setStatus("current")
_CfprVmHbaDvsPortId_Type = Gauge32
_CfprVmHbaDvsPortId_Object = MibTableColumn
cfprVmHbaDvsPortId = _CfprVmHbaDvsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 5),
    _CfprVmHbaDvsPortId_Type()
)
cfprVmHbaDvsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaDvsPortId.setStatus("current")
_CfprVmHbaDvsSwitchId_Type = Gauge32
_CfprVmHbaDvsSwitchId_Object = MibTableColumn
cfprVmHbaDvsSwitchId = _CfprVmHbaDvsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 6),
    _CfprVmHbaDvsSwitchId_Type()
)
cfprVmHbaDvsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaDvsSwitchId.setStatus("current")
_CfprVmHbaHostIfDn_Type = SnmpAdminString
_CfprVmHbaHostIfDn_Object = MibTableColumn
cfprVmHbaHostIfDn = _CfprVmHbaHostIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 7),
    _CfprVmHbaHostIfDn_Type()
)
cfprVmHbaHostIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaHostIfDn.setStatus("current")
_CfprVmHbaName_Type = SnmpAdminString
_CfprVmHbaName_Object = MibTableColumn
cfprVmHbaName = _CfprVmHbaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 8),
    _CfprVmHbaName_Type()
)
cfprVmHbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaName.setStatus("current")
_CfprVmHbaOwner_Type = CfprVmAdaptorOwner
_CfprVmHbaOwner_Object = MibTableColumn
cfprVmHbaOwner = _CfprVmHbaOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 9),
    _CfprVmHbaOwner_Type()
)
cfprVmHbaOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaOwner.setStatus("current")
_CfprVmHbaPhSwitchId_Type = CfprNetworkSwitchId
_CfprVmHbaPhSwitchId_Object = MibTableColumn
cfprVmHbaPhSwitchId = _CfprVmHbaPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 10),
    _CfprVmHbaPhSwitchId_Type()
)
cfprVmHbaPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaPhSwitchId.setStatus("current")
_CfprVmHbaProfileId_Type = Gauge32
_CfprVmHbaProfileId_Object = MibTableColumn
cfprVmHbaProfileId = _CfprVmHbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 11),
    _CfprVmHbaProfileId_Type()
)
cfprVmHbaProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaProfileId.setStatus("current")
_CfprVmHbaProfileName_Type = SnmpAdminString
_CfprVmHbaProfileName_Object = MibTableColumn
cfprVmHbaProfileName = _CfprVmHbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 12),
    _CfprVmHbaProfileName_Type()
)
cfprVmHbaProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaProfileName.setStatus("current")
_CfprVmHbaStatusChangeTs_Type = DateAndTime
_CfprVmHbaStatusChangeTs_Object = MibTableColumn
cfprVmHbaStatusChangeTs = _CfprVmHbaStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 13),
    _CfprVmHbaStatusChangeTs_Type()
)
cfprVmHbaStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaStatusChangeTs.setStatus("current")
_CfprVmHbaSwitchId_Type = CfprNetworkSwitchId
_CfprVmHbaSwitchId_Object = MibTableColumn
cfprVmHbaSwitchId = _CfprVmHbaSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 14),
    _CfprVmHbaSwitchId_Type()
)
cfprVmHbaSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaSwitchId.setStatus("current")
_CfprVmHbaType_Type = CfprVmHbaType
_CfprVmHbaType_Object = MibTableColumn
cfprVmHbaType = _CfprVmHbaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 15),
    _CfprVmHbaType_Type()
)
cfprVmHbaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaType.setStatus("current")
_CfprVmHbaUuid_Type = SnmpAdminString
_CfprVmHbaUuid_Object = MibTableColumn
cfprVmHbaUuid = _CfprVmHbaUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 16),
    _CfprVmHbaUuid_Type()
)
cfprVmHbaUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaUuid.setStatus("current")
_CfprVmHbaVStatus_Type = CfprVmStatus
_CfprVmHbaVStatus_Object = MibTableColumn
cfprVmHbaVStatus = _CfprVmHbaVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 17),
    _CfprVmHbaVStatus_Type()
)
cfprVmHbaVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaVStatus.setStatus("current")
_CfprVmHbaVcDn_Type = SnmpAdminString
_CfprVmHbaVcDn_Object = MibTableColumn
cfprVmHbaVcDn = _CfprVmHbaVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 18),
    _CfprVmHbaVcDn_Type()
)
cfprVmHbaVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaVcDn.setStatus("current")
_CfprVmHbaVifId_Type = Gauge32
_CfprVmHbaVifId_Object = MibTableColumn
cfprVmHbaVifId = _CfprVmHbaVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 19),
    _CfprVmHbaVifId_Type()
)
cfprVmHbaVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaVifId.setStatus("current")
_CfprVmHbaVmndGuid_Type = SnmpAdminString
_CfprVmHbaVmndGuid_Object = MibTableColumn
cfprVmHbaVmndGuid = _CfprVmHbaVmndGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 20),
    _CfprVmHbaVmndGuid_Type()
)
cfprVmHbaVmndGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaVmndGuid.setStatus("current")
_CfprVmHbaVmndName_Type = SnmpAdminString
_CfprVmHbaVmndName_Object = MibTableColumn
cfprVmHbaVmndName = _CfprVmHbaVmndName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 21),
    _CfprVmHbaVmndName_Type()
)
cfprVmHbaVmndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaVmndName.setStatus("current")
_CfprVmHbaVnicDn_Type = SnmpAdminString
_CfprVmHbaVnicDn_Object = MibTableColumn
cfprVmHbaVnicDn = _CfprVmHbaVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 22),
    _CfprVmHbaVnicDn_Type()
)
cfprVmHbaVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaVnicDn.setStatus("current")
_CfprVmHbaWwnn_Type = Unsigned64
_CfprVmHbaWwnn_Object = MibTableColumn
cfprVmHbaWwnn = _CfprVmHbaWwnn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 23),
    _CfprVmHbaWwnn_Type()
)
cfprVmHbaWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaWwnn.setStatus("current")
_CfprVmHbaWwpn_Type = Unsigned64
_CfprVmHbaWwpn_Object = MibTableColumn
cfprVmHbaWwpn = _CfprVmHbaWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 5, 1, 24),
    _CfprVmHbaWwpn_Type()
)
cfprVmHbaWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHbaWwpn.setStatus("current")
_CfprVmHvTable_Object = MibTable
cfprVmHvTable = _CfprVmHvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6)
)
if mibBuilder.loadTexts:
    cfprVmHvTable.setStatus("current")
_CfprVmHvEntry_Object = MibTableRow
cfprVmHvEntry = _CfprVmHvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1)
)
cfprVmHvEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmHvInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmHvEntry.setStatus("current")
_CfprVmHvInstanceId_Type = CfprManagedObjectId
_CfprVmHvInstanceId_Object = MibTableColumn
cfprVmHvInstanceId = _CfprVmHvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 1),
    _CfprVmHvInstanceId_Type()
)
cfprVmHvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmHvInstanceId.setStatus("current")
_CfprVmHvDn_Type = CfprManagedObjectDn
_CfprVmHvDn_Object = MibTableColumn
cfprVmHvDn = _CfprVmHvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 2),
    _CfprVmHvDn_Type()
)
cfprVmHvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvDn.setStatus("current")
_CfprVmHvRn_Type = SnmpAdminString
_CfprVmHvRn_Object = MibTableColumn
cfprVmHvRn = _CfprVmHvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 3),
    _CfprVmHvRn_Type()
)
cfprVmHvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvRn.setStatus("current")
_CfprVmHvClInstType_Type = CfprVmHvClInstType
_CfprVmHvClInstType_Object = MibTableColumn
cfprVmHvClInstType = _CfprVmHvClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 4),
    _CfprVmHvClInstType_Type()
)
cfprVmHvClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvClInstType.setStatus("current")
_CfprVmHvDescr_Type = SnmpAdminString
_CfprVmHvDescr_Object = MibTableColumn
cfprVmHvDescr = _CfprVmHvDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 5),
    _CfprVmHvDescr_Type()
)
cfprVmHvDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvDescr.setStatus("current")
_CfprVmHvDvsDn_Type = SnmpAdminString
_CfprVmHvDvsDn_Object = MibTableColumn
cfprVmHvDvsDn = _CfprVmHvDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 6),
    _CfprVmHvDvsDn_Type()
)
cfprVmHvDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvDvsDn.setStatus("current")
_CfprVmHvDvsName_Type = SnmpAdminString
_CfprVmHvDvsName_Object = MibTableColumn
cfprVmHvDvsName = _CfprVmHvDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 7),
    _CfprVmHvDvsName_Type()
)
cfprVmHvDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvDvsName.setStatus("current")
_CfprVmHvFltAggr_Type = Unsigned64
_CfprVmHvFltAggr_Object = MibTableColumn
cfprVmHvFltAggr = _CfprVmHvFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 8),
    _CfprVmHvFltAggr_Type()
)
cfprVmHvFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvFltAggr.setStatus("current")
_CfprVmHvHvType_Type = CfprVmHvType
_CfprVmHvHvType_Object = MibTableColumn
cfprVmHvHvType = _CfprVmHvHvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 9),
    _CfprVmHvHvType_Type()
)
cfprVmHvHvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvHvType.setStatus("current")
_CfprVmHvIntId_Type = SnmpAdminString
_CfprVmHvIntId_Object = MibTableColumn
cfprVmHvIntId = _CfprVmHvIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 10),
    _CfprVmHvIntId_Type()
)
cfprVmHvIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvIntId.setStatus("current")
_CfprVmHvLsDn_Type = SnmpAdminString
_CfprVmHvLsDn_Object = MibTableColumn
cfprVmHvLsDn = _CfprVmHvLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 11),
    _CfprVmHvLsDn_Type()
)
cfprVmHvLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvLsDn.setStatus("current")
_CfprVmHvModel_Type = CfprOsOsType
_CfprVmHvModel_Object = MibTableColumn
cfprVmHvModel = _CfprVmHvModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 12),
    _CfprVmHvModel_Type()
)
cfprVmHvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvModel.setStatus("current")
_CfprVmHvName_Type = SnmpAdminString
_CfprVmHvName_Object = MibTableColumn
cfprVmHvName = _CfprVmHvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 13),
    _CfprVmHvName_Type()
)
cfprVmHvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvName.setStatus("current")
_CfprVmHvPnDn_Type = SnmpAdminString
_CfprVmHvPnDn_Object = MibTableColumn
cfprVmHvPnDn = _CfprVmHvPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 14),
    _CfprVmHvPnDn_Type()
)
cfprVmHvPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvPnDn.setStatus("current")
_CfprVmHvPolicyLevel_Type = Gauge32
_CfprVmHvPolicyLevel_Object = MibTableColumn
cfprVmHvPolicyLevel = _CfprVmHvPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 15),
    _CfprVmHvPolicyLevel_Type()
)
cfprVmHvPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvPolicyLevel.setStatus("current")
_CfprVmHvPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmHvPolicyOwner_Object = MibTableColumn
cfprVmHvPolicyOwner = _CfprVmHvPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 16),
    _CfprVmHvPolicyOwner_Type()
)
cfprVmHvPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvPolicyOwner.setStatus("current")
_CfprVmHvStatusChangeTs_Type = DateAndTime
_CfprVmHvStatusChangeTs_Object = MibTableColumn
cfprVmHvStatusChangeTs = _CfprVmHvStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 17),
    _CfprVmHvStatusChangeTs_Type()
)
cfprVmHvStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvStatusChangeTs.setStatus("current")
_CfprVmHvUuid_Type = SnmpAdminString
_CfprVmHvUuid_Object = MibTableColumn
cfprVmHvUuid = _CfprVmHvUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 18),
    _CfprVmHvUuid_Type()
)
cfprVmHvUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvUuid.setStatus("current")
_CfprVmHvVStatus_Type = CfprVmStatus
_CfprVmHvVStatus_Object = MibTableColumn
cfprVmHvVStatus = _CfprVmHvVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 19),
    _CfprVmHvVStatus_Type()
)
cfprVmHvVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvVStatus.setStatus("current")
_CfprVmHvVendor_Type = CfprVmOsHvVendor
_CfprVmHvVendor_Object = MibTableColumn
cfprVmHvVendor = _CfprVmHvVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 6, 1, 20),
    _CfprVmHvVendor_Type()
)
cfprVmHvVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmHvVendor.setStatus("current")
_CfprVmInstanceTable_Object = MibTable
cfprVmInstanceTable = _CfprVmInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7)
)
if mibBuilder.loadTexts:
    cfprVmInstanceTable.setStatus("current")
_CfprVmInstanceEntry_Object = MibTableRow
cfprVmInstanceEntry = _CfprVmInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1)
)
cfprVmInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmInstanceEntry.setStatus("current")
_CfprVmInstanceInstanceId_Type = CfprManagedObjectId
_CfprVmInstanceInstanceId_Object = MibTableColumn
cfprVmInstanceInstanceId = _CfprVmInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 1),
    _CfprVmInstanceInstanceId_Type()
)
cfprVmInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmInstanceInstanceId.setStatus("current")
_CfprVmInstanceDn_Type = CfprManagedObjectDn
_CfprVmInstanceDn_Object = MibTableColumn
cfprVmInstanceDn = _CfprVmInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 2),
    _CfprVmInstanceDn_Type()
)
cfprVmInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceDn.setStatus("current")
_CfprVmInstanceRn_Type = SnmpAdminString
_CfprVmInstanceRn_Object = MibTableColumn
cfprVmInstanceRn = _CfprVmInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 3),
    _CfprVmInstanceRn_Type()
)
cfprVmInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceRn.setStatus("current")
_CfprVmInstanceClInstType_Type = CfprVmInstType
_CfprVmInstanceClInstType_Object = MibTableColumn
cfprVmInstanceClInstType = _CfprVmInstanceClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 4),
    _CfprVmInstanceClInstType_Type()
)
cfprVmInstanceClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceClInstType.setStatus("current")
_CfprVmInstanceDescr_Type = SnmpAdminString
_CfprVmInstanceDescr_Object = MibTableColumn
cfprVmInstanceDescr = _CfprVmInstanceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 5),
    _CfprVmInstanceDescr_Type()
)
cfprVmInstanceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceDescr.setStatus("current")
_CfprVmInstanceDvsDn_Type = SnmpAdminString
_CfprVmInstanceDvsDn_Object = MibTableColumn
cfprVmInstanceDvsDn = _CfprVmInstanceDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 6),
    _CfprVmInstanceDvsDn_Type()
)
cfprVmInstanceDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceDvsDn.setStatus("current")
_CfprVmInstanceDvsName_Type = SnmpAdminString
_CfprVmInstanceDvsName_Object = MibTableColumn
cfprVmInstanceDvsName = _CfprVmInstanceDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 7),
    _CfprVmInstanceDvsName_Type()
)
cfprVmInstanceDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceDvsName.setStatus("current")
_CfprVmInstanceFltAggr_Type = Unsigned64
_CfprVmInstanceFltAggr_Object = MibTableColumn
cfprVmInstanceFltAggr = _CfprVmInstanceFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 8),
    _CfprVmInstanceFltAggr_Type()
)
cfprVmInstanceFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceFltAggr.setStatus("current")
_CfprVmInstanceHvDn_Type = SnmpAdminString
_CfprVmInstanceHvDn_Object = MibTableColumn
cfprVmInstanceHvDn = _CfprVmInstanceHvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 9),
    _CfprVmInstanceHvDn_Type()
)
cfprVmInstanceHvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceHvDn.setStatus("current")
_CfprVmInstanceHvType_Type = CfprVmHvType
_CfprVmInstanceHvType_Object = MibTableColumn
cfprVmInstanceHvType = _CfprVmInstanceHvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 10),
    _CfprVmInstanceHvType_Type()
)
cfprVmInstanceHvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceHvType.setStatus("current")
_CfprVmInstanceHvUuid_Type = SnmpAdminString
_CfprVmInstanceHvUuid_Object = MibTableColumn
cfprVmInstanceHvUuid = _CfprVmInstanceHvUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 11),
    _CfprVmInstanceHvUuid_Type()
)
cfprVmInstanceHvUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceHvUuid.setStatus("current")
_CfprVmInstanceIntId_Type = SnmpAdminString
_CfprVmInstanceIntId_Object = MibTableColumn
cfprVmInstanceIntId = _CfprVmInstanceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 12),
    _CfprVmInstanceIntId_Type()
)
cfprVmInstanceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceIntId.setStatus("current")
_CfprVmInstanceLsDn_Type = SnmpAdminString
_CfprVmInstanceLsDn_Object = MibTableColumn
cfprVmInstanceLsDn = _CfprVmInstanceLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 13),
    _CfprVmInstanceLsDn_Type()
)
cfprVmInstanceLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceLsDn.setStatus("current")
_CfprVmInstanceModel_Type = CfprOsOsType
_CfprVmInstanceModel_Object = MibTableColumn
cfprVmInstanceModel = _CfprVmInstanceModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 14),
    _CfprVmInstanceModel_Type()
)
cfprVmInstanceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceModel.setStatus("current")
_CfprVmInstanceName_Type = SnmpAdminString
_CfprVmInstanceName_Object = MibTableColumn
cfprVmInstanceName = _CfprVmInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 15),
    _CfprVmInstanceName_Type()
)
cfprVmInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceName.setStatus("current")
_CfprVmInstancePnDn_Type = SnmpAdminString
_CfprVmInstancePnDn_Object = MibTableColumn
cfprVmInstancePnDn = _CfprVmInstancePnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 16),
    _CfprVmInstancePnDn_Type()
)
cfprVmInstancePnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstancePnDn.setStatus("current")
_CfprVmInstancePolicyLevel_Type = Gauge32
_CfprVmInstancePolicyLevel_Object = MibTableColumn
cfprVmInstancePolicyLevel = _CfprVmInstancePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 17),
    _CfprVmInstancePolicyLevel_Type()
)
cfprVmInstancePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstancePolicyLevel.setStatus("current")
_CfprVmInstancePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmInstancePolicyOwner_Object = MibTableColumn
cfprVmInstancePolicyOwner = _CfprVmInstancePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 18),
    _CfprVmInstancePolicyOwner_Type()
)
cfprVmInstancePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstancePolicyOwner.setStatus("current")
_CfprVmInstanceStatusChangeTs_Type = DateAndTime
_CfprVmInstanceStatusChangeTs_Object = MibTableColumn
cfprVmInstanceStatusChangeTs = _CfprVmInstanceStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 19),
    _CfprVmInstanceStatusChangeTs_Type()
)
cfprVmInstanceStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceStatusChangeTs.setStatus("current")
_CfprVmInstanceUuid_Type = SnmpAdminString
_CfprVmInstanceUuid_Object = MibTableColumn
cfprVmInstanceUuid = _CfprVmInstanceUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 20),
    _CfprVmInstanceUuid_Type()
)
cfprVmInstanceUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceUuid.setStatus("current")
_CfprVmInstanceVStatus_Type = CfprVmStatus
_CfprVmInstanceVStatus_Object = MibTableColumn
cfprVmInstanceVStatus = _CfprVmInstanceVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 21),
    _CfprVmInstanceVStatus_Type()
)
cfprVmInstanceVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceVStatus.setStatus("current")
_CfprVmInstanceVendor_Type = CfprVmOsHvVendor
_CfprVmInstanceVendor_Object = MibTableColumn
cfprVmInstanceVendor = _CfprVmInstanceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 7, 1, 22),
    _CfprVmInstanceVendor_Type()
)
cfprVmInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmInstanceVendor.setStatus("current")
_CfprVmLifeCyclePolicyTable_Object = MibTable
cfprVmLifeCyclePolicyTable = _CfprVmLifeCyclePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8)
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyTable.setStatus("current")
_CfprVmLifeCyclePolicyEntry_Object = MibTableRow
cfprVmLifeCyclePolicyEntry = _CfprVmLifeCyclePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1)
)
cfprVmLifeCyclePolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmLifeCyclePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyEntry.setStatus("current")
_CfprVmLifeCyclePolicyInstanceId_Type = CfprManagedObjectId
_CfprVmLifeCyclePolicyInstanceId_Object = MibTableColumn
cfprVmLifeCyclePolicyInstanceId = _CfprVmLifeCyclePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 1),
    _CfprVmLifeCyclePolicyInstanceId_Type()
)
cfprVmLifeCyclePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyInstanceId.setStatus("current")
_CfprVmLifeCyclePolicyDn_Type = CfprManagedObjectDn
_CfprVmLifeCyclePolicyDn_Object = MibTableColumn
cfprVmLifeCyclePolicyDn = _CfprVmLifeCyclePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 2),
    _CfprVmLifeCyclePolicyDn_Type()
)
cfprVmLifeCyclePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyDn.setStatus("current")
_CfprVmLifeCyclePolicyRn_Type = SnmpAdminString
_CfprVmLifeCyclePolicyRn_Object = MibTableColumn
cfprVmLifeCyclePolicyRn = _CfprVmLifeCyclePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 3),
    _CfprVmLifeCyclePolicyRn_Type()
)
cfprVmLifeCyclePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyRn.setStatus("current")
_CfprVmLifeCyclePolicyDescr_Type = SnmpAdminString
_CfprVmLifeCyclePolicyDescr_Object = MibTableColumn
cfprVmLifeCyclePolicyDescr = _CfprVmLifeCyclePolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 4),
    _CfprVmLifeCyclePolicyDescr_Type()
)
cfprVmLifeCyclePolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyDescr.setStatus("current")
_CfprVmLifeCyclePolicyFsmDescr_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmDescr_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmDescr = _CfprVmLifeCyclePolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 5),
    _CfprVmLifeCyclePolicyFsmDescr_Type()
)
cfprVmLifeCyclePolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmDescr.setStatus("current")
_CfprVmLifeCyclePolicyFsmPrev_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmPrev_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmPrev = _CfprVmLifeCyclePolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 6),
    _CfprVmLifeCyclePolicyFsmPrev_Type()
)
cfprVmLifeCyclePolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmPrev.setStatus("current")
_CfprVmLifeCyclePolicyFsmProgr_Type = Gauge32
_CfprVmLifeCyclePolicyFsmProgr_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmProgr = _CfprVmLifeCyclePolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 7),
    _CfprVmLifeCyclePolicyFsmProgr_Type()
)
cfprVmLifeCyclePolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmProgr.setStatus("current")
_CfprVmLifeCyclePolicyFsmRmtInvErrCode_Type = Gauge32
_CfprVmLifeCyclePolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRmtInvErrCode = _CfprVmLifeCyclePolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 8),
    _CfprVmLifeCyclePolicyFsmRmtInvErrCode_Type()
)
cfprVmLifeCyclePolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRmtInvErrCode.setStatus("current")
_CfprVmLifeCyclePolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRmtInvErrDescr = _CfprVmLifeCyclePolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 9),
    _CfprVmLifeCyclePolicyFsmRmtInvErrDescr_Type()
)
cfprVmLifeCyclePolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRmtInvErrDescr.setStatus("current")
_CfprVmLifeCyclePolicyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprVmLifeCyclePolicyFsmRmtInvRslt_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRmtInvRslt = _CfprVmLifeCyclePolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 10),
    _CfprVmLifeCyclePolicyFsmRmtInvRslt_Type()
)
cfprVmLifeCyclePolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRmtInvRslt.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageDescr_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmStageDescr_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageDescr = _CfprVmLifeCyclePolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 11),
    _CfprVmLifeCyclePolicyFsmStageDescr_Type()
)
cfprVmLifeCyclePolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageDescr.setStatus("current")
_CfprVmLifeCyclePolicyFsmStamp_Type = DateAndTime
_CfprVmLifeCyclePolicyFsmStamp_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStamp = _CfprVmLifeCyclePolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 12),
    _CfprVmLifeCyclePolicyFsmStamp_Type()
)
cfprVmLifeCyclePolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStamp.setStatus("current")
_CfprVmLifeCyclePolicyFsmStatus_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmStatus_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStatus = _CfprVmLifeCyclePolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 13),
    _CfprVmLifeCyclePolicyFsmStatus_Type()
)
cfprVmLifeCyclePolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStatus.setStatus("current")
_CfprVmLifeCyclePolicyFsmTry_Type = Gauge32
_CfprVmLifeCyclePolicyFsmTry_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTry = _CfprVmLifeCyclePolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 14),
    _CfprVmLifeCyclePolicyFsmTry_Type()
)
cfprVmLifeCyclePolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTry.setStatus("current")
_CfprVmLifeCyclePolicyIntId_Type = SnmpAdminString
_CfprVmLifeCyclePolicyIntId_Object = MibTableColumn
cfprVmLifeCyclePolicyIntId = _CfprVmLifeCyclePolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 15),
    _CfprVmLifeCyclePolicyIntId_Type()
)
cfprVmLifeCyclePolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyIntId.setStatus("current")
_CfprVmLifeCyclePolicyName_Type = SnmpAdminString
_CfprVmLifeCyclePolicyName_Object = MibTableColumn
cfprVmLifeCyclePolicyName = _CfprVmLifeCyclePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 16),
    _CfprVmLifeCyclePolicyName_Type()
)
cfprVmLifeCyclePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyName.setStatus("current")
_CfprVmLifeCyclePolicyPolicyLevel_Type = Gauge32
_CfprVmLifeCyclePolicyPolicyLevel_Object = MibTableColumn
cfprVmLifeCyclePolicyPolicyLevel = _CfprVmLifeCyclePolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 17),
    _CfprVmLifeCyclePolicyPolicyLevel_Type()
)
cfprVmLifeCyclePolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyPolicyLevel.setStatus("current")
_CfprVmLifeCyclePolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmLifeCyclePolicyPolicyOwner_Object = MibTableColumn
cfprVmLifeCyclePolicyPolicyOwner = _CfprVmLifeCyclePolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 18),
    _CfprVmLifeCyclePolicyPolicyOwner_Type()
)
cfprVmLifeCyclePolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyPolicyOwner.setStatus("current")
_CfprVmLifeCyclePolicyVmRetention_Type = Gauge32
_CfprVmLifeCyclePolicyVmRetention_Object = MibTableColumn
cfprVmLifeCyclePolicyVmRetention = _CfprVmLifeCyclePolicyVmRetention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 19),
    _CfprVmLifeCyclePolicyVmRetention_Type()
)
cfprVmLifeCyclePolicyVmRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyVmRetention.setStatus("current")
_CfprVmLifeCyclePolicyVnicRetention_Type = Gauge32
_CfprVmLifeCyclePolicyVnicRetention_Object = MibTableColumn
cfprVmLifeCyclePolicyVnicRetention = _CfprVmLifeCyclePolicyVnicRetention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 8, 1, 20),
    _CfprVmLifeCyclePolicyVnicRetention_Type()
)
cfprVmLifeCyclePolicyVnicRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyVnicRetention.setStatus("current")
_CfprVmLifeCyclePolicyFsmTable_Object = MibTable
cfprVmLifeCyclePolicyFsmTable = _CfprVmLifeCyclePolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9)
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTable.setStatus("current")
_CfprVmLifeCyclePolicyFsmEntry_Object = MibTableRow
cfprVmLifeCyclePolicyFsmEntry = _CfprVmLifeCyclePolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1)
)
cfprVmLifeCyclePolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmLifeCyclePolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmEntry.setStatus("current")
_CfprVmLifeCyclePolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprVmLifeCyclePolicyFsmInstanceId_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmInstanceId = _CfprVmLifeCyclePolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 1),
    _CfprVmLifeCyclePolicyFsmInstanceId_Type()
)
cfprVmLifeCyclePolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmInstanceId.setStatus("current")
_CfprVmLifeCyclePolicyFsmDn_Type = CfprManagedObjectDn
_CfprVmLifeCyclePolicyFsmDn_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmDn = _CfprVmLifeCyclePolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 2),
    _CfprVmLifeCyclePolicyFsmDn_Type()
)
cfprVmLifeCyclePolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmDn.setStatus("current")
_CfprVmLifeCyclePolicyFsmRn_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmRn_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRn = _CfprVmLifeCyclePolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 3),
    _CfprVmLifeCyclePolicyFsmRn_Type()
)
cfprVmLifeCyclePolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRn.setStatus("current")
_CfprVmLifeCyclePolicyFsmCompletionTime_Type = DateAndTime
_CfprVmLifeCyclePolicyFsmCompletionTime_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmCompletionTime = _CfprVmLifeCyclePolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 4),
    _CfprVmLifeCyclePolicyFsmCompletionTime_Type()
)
cfprVmLifeCyclePolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmCompletionTime.setStatus("current")
_CfprVmLifeCyclePolicyFsmCurrentFsm_Type = CfprVmLifeCyclePolicyFsmCurrentFsm
_CfprVmLifeCyclePolicyFsmCurrentFsm_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmCurrentFsm = _CfprVmLifeCyclePolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 5),
    _CfprVmLifeCyclePolicyFsmCurrentFsm_Type()
)
cfprVmLifeCyclePolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmCurrentFsm.setStatus("current")
_CfprVmLifeCyclePolicyFsmDescrData_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmDescrData_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmDescrData = _CfprVmLifeCyclePolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 6),
    _CfprVmLifeCyclePolicyFsmDescrData_Type()
)
cfprVmLifeCyclePolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmDescrData.setStatus("current")
_CfprVmLifeCyclePolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprVmLifeCyclePolicyFsmFsmStatus_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmFsmStatus = _CfprVmLifeCyclePolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 7),
    _CfprVmLifeCyclePolicyFsmFsmStatus_Type()
)
cfprVmLifeCyclePolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmFsmStatus.setStatus("current")
_CfprVmLifeCyclePolicyFsmProgress_Type = Gauge32
_CfprVmLifeCyclePolicyFsmProgress_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmProgress = _CfprVmLifeCyclePolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 8),
    _CfprVmLifeCyclePolicyFsmProgress_Type()
)
cfprVmLifeCyclePolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmProgress.setStatus("current")
_CfprVmLifeCyclePolicyFsmRmtErrCode_Type = Gauge32
_CfprVmLifeCyclePolicyFsmRmtErrCode_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRmtErrCode = _CfprVmLifeCyclePolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 9),
    _CfprVmLifeCyclePolicyFsmRmtErrCode_Type()
)
cfprVmLifeCyclePolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRmtErrCode.setStatus("current")
_CfprVmLifeCyclePolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmRmtErrDescr_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRmtErrDescr = _CfprVmLifeCyclePolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 10),
    _CfprVmLifeCyclePolicyFsmRmtErrDescr_Type()
)
cfprVmLifeCyclePolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRmtErrDescr.setStatus("current")
_CfprVmLifeCyclePolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprVmLifeCyclePolicyFsmRmtRslt_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmRmtRslt = _CfprVmLifeCyclePolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 9, 1, 11),
    _CfprVmLifeCyclePolicyFsmRmtRslt_Type()
)
cfprVmLifeCyclePolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmRmtRslt.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageTable_Object = MibTable
cfprVmLifeCyclePolicyFsmStageTable = _CfprVmLifeCyclePolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10)
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageTable.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageEntry_Object = MibTableRow
cfprVmLifeCyclePolicyFsmStageEntry = _CfprVmLifeCyclePolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1)
)
cfprVmLifeCyclePolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmLifeCyclePolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageEntry.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprVmLifeCyclePolicyFsmStageInstanceId_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageInstanceId = _CfprVmLifeCyclePolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 1),
    _CfprVmLifeCyclePolicyFsmStageInstanceId_Type()
)
cfprVmLifeCyclePolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageInstanceId.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprVmLifeCyclePolicyFsmStageDn_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageDn = _CfprVmLifeCyclePolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 2),
    _CfprVmLifeCyclePolicyFsmStageDn_Type()
)
cfprVmLifeCyclePolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageDn.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageRn_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmStageRn_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageRn = _CfprVmLifeCyclePolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 3),
    _CfprVmLifeCyclePolicyFsmStageRn_Type()
)
cfprVmLifeCyclePolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageRn.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageDescrData_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmStageDescrData_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageDescrData = _CfprVmLifeCyclePolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 4),
    _CfprVmLifeCyclePolicyFsmStageDescrData_Type()
)
cfprVmLifeCyclePolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageDescrData.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprVmLifeCyclePolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageLastUpdateTime = _CfprVmLifeCyclePolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 5),
    _CfprVmLifeCyclePolicyFsmStageLastUpdateTime_Type()
)
cfprVmLifeCyclePolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageLastUpdateTime.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageName_Type = CfprVmLifeCyclePolicyFsmStageName
_CfprVmLifeCyclePolicyFsmStageName_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageName = _CfprVmLifeCyclePolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 6),
    _CfprVmLifeCyclePolicyFsmStageName_Type()
)
cfprVmLifeCyclePolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageName.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageOrder_Type = Gauge32
_CfprVmLifeCyclePolicyFsmStageOrder_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageOrder = _CfprVmLifeCyclePolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 7),
    _CfprVmLifeCyclePolicyFsmStageOrder_Type()
)
cfprVmLifeCyclePolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageOrder.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageRetry_Type = Gauge32
_CfprVmLifeCyclePolicyFsmStageRetry_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageRetry = _CfprVmLifeCyclePolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 8),
    _CfprVmLifeCyclePolicyFsmStageRetry_Type()
)
cfprVmLifeCyclePolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageRetry.setStatus("current")
_CfprVmLifeCyclePolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprVmLifeCyclePolicyFsmStageStageStatus_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmStageStageStatus = _CfprVmLifeCyclePolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 10, 1, 9),
    _CfprVmLifeCyclePolicyFsmStageStageStatus_Type()
)
cfprVmLifeCyclePolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmStageStageStatus.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskTable_Object = MibTable
cfprVmLifeCyclePolicyFsmTaskTable = _CfprVmLifeCyclePolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11)
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskTable.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskEntry_Object = MibTableRow
cfprVmLifeCyclePolicyFsmTaskEntry = _CfprVmLifeCyclePolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1)
)
cfprVmLifeCyclePolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmLifeCyclePolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskEntry.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprVmLifeCyclePolicyFsmTaskInstanceId_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskInstanceId = _CfprVmLifeCyclePolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 1),
    _CfprVmLifeCyclePolicyFsmTaskInstanceId_Type()
)
cfprVmLifeCyclePolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskInstanceId.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskDn_Type = CfprManagedObjectDn
_CfprVmLifeCyclePolicyFsmTaskDn_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskDn = _CfprVmLifeCyclePolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 2),
    _CfprVmLifeCyclePolicyFsmTaskDn_Type()
)
cfprVmLifeCyclePolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskDn.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskRn_Type = SnmpAdminString
_CfprVmLifeCyclePolicyFsmTaskRn_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskRn = _CfprVmLifeCyclePolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 3),
    _CfprVmLifeCyclePolicyFsmTaskRn_Type()
)
cfprVmLifeCyclePolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskRn.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskCompletion_Type = CfprFsmCompletion
_CfprVmLifeCyclePolicyFsmTaskCompletion_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskCompletion = _CfprVmLifeCyclePolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 4),
    _CfprVmLifeCyclePolicyFsmTaskCompletion_Type()
)
cfprVmLifeCyclePolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskCompletion.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskFlags_Type = CfprFsmFlags
_CfprVmLifeCyclePolicyFsmTaskFlags_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskFlags = _CfprVmLifeCyclePolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 5),
    _CfprVmLifeCyclePolicyFsmTaskFlags_Type()
)
cfprVmLifeCyclePolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskFlags.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskItem_Type = CfprVmLifeCyclePolicyFsmTaskItem
_CfprVmLifeCyclePolicyFsmTaskItem_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskItem = _CfprVmLifeCyclePolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 6),
    _CfprVmLifeCyclePolicyFsmTaskItem_Type()
)
cfprVmLifeCyclePolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskItem.setStatus("current")
_CfprVmLifeCyclePolicyFsmTaskSeqId_Type = Gauge32
_CfprVmLifeCyclePolicyFsmTaskSeqId_Object = MibTableColumn
cfprVmLifeCyclePolicyFsmTaskSeqId = _CfprVmLifeCyclePolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 11, 1, 7),
    _CfprVmLifeCyclePolicyFsmTaskSeqId_Type()
)
cfprVmLifeCyclePolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmLifeCyclePolicyFsmTaskSeqId.setStatus("current")
_CfprVmNicTable_Object = MibTable
cfprVmNicTable = _CfprVmNicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12)
)
if mibBuilder.loadTexts:
    cfprVmNicTable.setStatus("current")
_CfprVmNicEntry_Object = MibTableRow
cfprVmNicEntry = _CfprVmNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1)
)
cfprVmNicEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmNicInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmNicEntry.setStatus("current")
_CfprVmNicInstanceId_Type = CfprManagedObjectId
_CfprVmNicInstanceId_Object = MibTableColumn
cfprVmNicInstanceId = _CfprVmNicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 1),
    _CfprVmNicInstanceId_Type()
)
cfprVmNicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmNicInstanceId.setStatus("current")
_CfprVmNicDn_Type = CfprManagedObjectDn
_CfprVmNicDn_Object = MibTableColumn
cfprVmNicDn = _CfprVmNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 2),
    _CfprVmNicDn_Type()
)
cfprVmNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicDn.setStatus("current")
_CfprVmNicRn_Type = SnmpAdminString
_CfprVmNicRn_Object = MibTableColumn
cfprVmNicRn = _CfprVmNicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 3),
    _CfprVmNicRn_Type()
)
cfprVmNicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicRn.setStatus("current")
_CfprVmNicDvsGenPortId_Type = SnmpAdminString
_CfprVmNicDvsGenPortId_Object = MibTableColumn
cfprVmNicDvsGenPortId = _CfprVmNicDvsGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 4),
    _CfprVmNicDvsGenPortId_Type()
)
cfprVmNicDvsGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicDvsGenPortId.setStatus("current")
_CfprVmNicDvsPortId_Type = Gauge32
_CfprVmNicDvsPortId_Object = MibTableColumn
cfprVmNicDvsPortId = _CfprVmNicDvsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 5),
    _CfprVmNicDvsPortId_Type()
)
cfprVmNicDvsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicDvsPortId.setStatus("current")
_CfprVmNicDvsSwitchId_Type = Gauge32
_CfprVmNicDvsSwitchId_Object = MibTableColumn
cfprVmNicDvsSwitchId = _CfprVmNicDvsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 6),
    _CfprVmNicDvsSwitchId_Type()
)
cfprVmNicDvsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicDvsSwitchId.setStatus("current")
_CfprVmNicHostIfDn_Type = SnmpAdminString
_CfprVmNicHostIfDn_Object = MibTableColumn
cfprVmNicHostIfDn = _CfprVmNicHostIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 7),
    _CfprVmNicHostIfDn_Type()
)
cfprVmNicHostIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicHostIfDn.setStatus("current")
_CfprVmNicMacAddr_Type = MacAddress
_CfprVmNicMacAddr_Object = MibTableColumn
cfprVmNicMacAddr = _CfprVmNicMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 8),
    _CfprVmNicMacAddr_Type()
)
cfprVmNicMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicMacAddr.setStatus("current")
_CfprVmNicName_Type = SnmpAdminString
_CfprVmNicName_Object = MibTableColumn
cfprVmNicName = _CfprVmNicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 9),
    _CfprVmNicName_Type()
)
cfprVmNicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicName.setStatus("current")
_CfprVmNicOwner_Type = CfprVmAdaptorOwner
_CfprVmNicOwner_Object = MibTableColumn
cfprVmNicOwner = _CfprVmNicOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 10),
    _CfprVmNicOwner_Type()
)
cfprVmNicOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicOwner.setStatus("current")
_CfprVmNicPhSwitchId_Type = CfprNetworkSwitchId
_CfprVmNicPhSwitchId_Object = MibTableColumn
cfprVmNicPhSwitchId = _CfprVmNicPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 11),
    _CfprVmNicPhSwitchId_Type()
)
cfprVmNicPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicPhSwitchId.setStatus("current")
_CfprVmNicProfileId_Type = Gauge32
_CfprVmNicProfileId_Object = MibTableColumn
cfprVmNicProfileId = _CfprVmNicProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 12),
    _CfprVmNicProfileId_Type()
)
cfprVmNicProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicProfileId.setStatus("current")
_CfprVmNicProfileName_Type = SnmpAdminString
_CfprVmNicProfileName_Object = MibTableColumn
cfprVmNicProfileName = _CfprVmNicProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 13),
    _CfprVmNicProfileName_Type()
)
cfprVmNicProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicProfileName.setStatus("current")
_CfprVmNicStatusChangeTs_Type = DateAndTime
_CfprVmNicStatusChangeTs_Object = MibTableColumn
cfprVmNicStatusChangeTs = _CfprVmNicStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 14),
    _CfprVmNicStatusChangeTs_Type()
)
cfprVmNicStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicStatusChangeTs.setStatus("current")
_CfprVmNicSwitchId_Type = CfprNetworkSwitchId
_CfprVmNicSwitchId_Object = MibTableColumn
cfprVmNicSwitchId = _CfprVmNicSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 15),
    _CfprVmNicSwitchId_Type()
)
cfprVmNicSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicSwitchId.setStatus("current")
_CfprVmNicType_Type = CfprVmNicType
_CfprVmNicType_Object = MibTableColumn
cfprVmNicType = _CfprVmNicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 16),
    _CfprVmNicType_Type()
)
cfprVmNicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicType.setStatus("current")
_CfprVmNicUuid_Type = SnmpAdminString
_CfprVmNicUuid_Object = MibTableColumn
cfprVmNicUuid = _CfprVmNicUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 17),
    _CfprVmNicUuid_Type()
)
cfprVmNicUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicUuid.setStatus("current")
_CfprVmNicVStatus_Type = CfprVmStatus
_CfprVmNicVStatus_Object = MibTableColumn
cfprVmNicVStatus = _CfprVmNicVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 18),
    _CfprVmNicVStatus_Type()
)
cfprVmNicVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicVStatus.setStatus("current")
_CfprVmNicVcDn_Type = SnmpAdminString
_CfprVmNicVcDn_Object = MibTableColumn
cfprVmNicVcDn = _CfprVmNicVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 19),
    _CfprVmNicVcDn_Type()
)
cfprVmNicVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicVcDn.setStatus("current")
_CfprVmNicVifId_Type = Gauge32
_CfprVmNicVifId_Object = MibTableColumn
cfprVmNicVifId = _CfprVmNicVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 20),
    _CfprVmNicVifId_Type()
)
cfprVmNicVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicVifId.setStatus("current")
_CfprVmNicVmndGuid_Type = SnmpAdminString
_CfprVmNicVmndGuid_Object = MibTableColumn
cfprVmNicVmndGuid = _CfprVmNicVmndGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 21),
    _CfprVmNicVmndGuid_Type()
)
cfprVmNicVmndGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicVmndGuid.setStatus("current")
_CfprVmNicVmndName_Type = SnmpAdminString
_CfprVmNicVmndName_Object = MibTableColumn
cfprVmNicVmndName = _CfprVmNicVmndName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 22),
    _CfprVmNicVmndName_Type()
)
cfprVmNicVmndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicVmndName.setStatus("current")
_CfprVmNicVnicDn_Type = SnmpAdminString
_CfprVmNicVnicDn_Object = MibTableColumn
cfprVmNicVnicDn = _CfprVmNicVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 12, 1, 23),
    _CfprVmNicVnicDn_Type()
)
cfprVmNicVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmNicVnicDn.setStatus("current")
_CfprVmOrgTable_Object = MibTable
cfprVmOrgTable = _CfprVmOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13)
)
if mibBuilder.loadTexts:
    cfprVmOrgTable.setStatus("current")
_CfprVmOrgEntry_Object = MibTableRow
cfprVmOrgEntry = _CfprVmOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1)
)
cfprVmOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmOrgEntry.setStatus("current")
_CfprVmOrgInstanceId_Type = CfprManagedObjectId
_CfprVmOrgInstanceId_Object = MibTableColumn
cfprVmOrgInstanceId = _CfprVmOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 1),
    _CfprVmOrgInstanceId_Type()
)
cfprVmOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmOrgInstanceId.setStatus("current")
_CfprVmOrgDn_Type = CfprManagedObjectDn
_CfprVmOrgDn_Object = MibTableColumn
cfprVmOrgDn = _CfprVmOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 2),
    _CfprVmOrgDn_Type()
)
cfprVmOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgDn.setStatus("current")
_CfprVmOrgRn_Type = SnmpAdminString
_CfprVmOrgRn_Object = MibTableColumn
cfprVmOrgRn = _CfprVmOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 3),
    _CfprVmOrgRn_Type()
)
cfprVmOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgRn.setStatus("current")
_CfprVmOrgDescr_Type = SnmpAdminString
_CfprVmOrgDescr_Object = MibTableColumn
cfprVmOrgDescr = _CfprVmOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 4),
    _CfprVmOrgDescr_Type()
)
cfprVmOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgDescr.setStatus("current")
_CfprVmOrgIntId_Type = SnmpAdminString
_CfprVmOrgIntId_Object = MibTableColumn
cfprVmOrgIntId = _CfprVmOrgIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 5),
    _CfprVmOrgIntId_Type()
)
cfprVmOrgIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgIntId.setStatus("current")
_CfprVmOrgName_Type = SnmpAdminString
_CfprVmOrgName_Object = MibTableColumn
cfprVmOrgName = _CfprVmOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 6),
    _CfprVmOrgName_Type()
)
cfprVmOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgName.setStatus("current")
_CfprVmOrgOwn_Type = CfprExtvmmOwnership
_CfprVmOrgOwn_Object = MibTableColumn
cfprVmOrgOwn = _CfprVmOrgOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 7),
    _CfprVmOrgOwn_Type()
)
cfprVmOrgOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgOwn.setStatus("current")
_CfprVmOrgPolicyLevel_Type = Gauge32
_CfprVmOrgPolicyLevel_Object = MibTableColumn
cfprVmOrgPolicyLevel = _CfprVmOrgPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 8),
    _CfprVmOrgPolicyLevel_Type()
)
cfprVmOrgPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgPolicyLevel.setStatus("current")
_CfprVmOrgPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmOrgPolicyOwner_Object = MibTableColumn
cfprVmOrgPolicyOwner = _CfprVmOrgPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 9),
    _CfprVmOrgPolicyOwner_Type()
)
cfprVmOrgPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgPolicyOwner.setStatus("current")
_CfprVmOrgUuid_Type = SnmpAdminString
_CfprVmOrgUuid_Object = MibTableColumn
cfprVmOrgUuid = _CfprVmOrgUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 13, 1, 10),
    _CfprVmOrgUuid_Type()
)
cfprVmOrgUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmOrgUuid.setStatus("current")
_CfprVmSwitchTable_Object = MibTable
cfprVmSwitchTable = _CfprVmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14)
)
if mibBuilder.loadTexts:
    cfprVmSwitchTable.setStatus("current")
_CfprVmSwitchEntry_Object = MibTableRow
cfprVmSwitchEntry = _CfprVmSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1)
)
cfprVmSwitchEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmSwitchInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmSwitchEntry.setStatus("current")
_CfprVmSwitchInstanceId_Type = CfprManagedObjectId
_CfprVmSwitchInstanceId_Object = MibTableColumn
cfprVmSwitchInstanceId = _CfprVmSwitchInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 1),
    _CfprVmSwitchInstanceId_Type()
)
cfprVmSwitchInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmSwitchInstanceId.setStatus("current")
_CfprVmSwitchDn_Type = CfprManagedObjectDn
_CfprVmSwitchDn_Object = MibTableColumn
cfprVmSwitchDn = _CfprVmSwitchDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 2),
    _CfprVmSwitchDn_Type()
)
cfprVmSwitchDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchDn.setStatus("current")
_CfprVmSwitchRn_Type = SnmpAdminString
_CfprVmSwitchRn_Object = MibTableColumn
cfprVmSwitchRn = _CfprVmSwitchRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 3),
    _CfprVmSwitchRn_Type()
)
cfprVmSwitchRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchRn.setStatus("current")
_CfprVmSwitchAdminState_Type = CfprVmSwitchAdminState
_CfprVmSwitchAdminState_Object = MibTableColumn
cfprVmSwitchAdminState = _CfprVmSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 4),
    _CfprVmSwitchAdminState_Type()
)
cfprVmSwitchAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchAdminState.setStatus("current")
_CfprVmSwitchDescr_Type = SnmpAdminString
_CfprVmSwitchDescr_Object = MibTableColumn
cfprVmSwitchDescr = _CfprVmSwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 5),
    _CfprVmSwitchDescr_Type()
)
cfprVmSwitchDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchDescr.setStatus("current")
_CfprVmSwitchExtKey_Type = SnmpAdminString
_CfprVmSwitchExtKey_Object = MibTableColumn
cfprVmSwitchExtKey = _CfprVmSwitchExtKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 6),
    _CfprVmSwitchExtKey_Type()
)
cfprVmSwitchExtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchExtKey.setStatus("current")
_CfprVmSwitchFltAggr_Type = Unsigned64
_CfprVmSwitchFltAggr_Object = MibTableColumn
cfprVmSwitchFltAggr = _CfprVmSwitchFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 7),
    _CfprVmSwitchFltAggr_Type()
)
cfprVmSwitchFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchFltAggr.setStatus("current")
_CfprVmSwitchId_Type = SnmpAdminString
_CfprVmSwitchId_Object = MibTableColumn
cfprVmSwitchId = _CfprVmSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 8),
    _CfprVmSwitchId_Type()
)
cfprVmSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchId.setStatus("current")
_CfprVmSwitchIntId_Type = SnmpAdminString
_CfprVmSwitchIntId_Object = MibTableColumn
cfprVmSwitchIntId = _CfprVmSwitchIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 9),
    _CfprVmSwitchIntId_Type()
)
cfprVmSwitchIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchIntId.setStatus("current")
_CfprVmSwitchKeyInst_Type = Gauge32
_CfprVmSwitchKeyInst_Object = MibTableColumn
cfprVmSwitchKeyInst = _CfprVmSwitchKeyInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 10),
    _CfprVmSwitchKeyInst_Type()
)
cfprVmSwitchKeyInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchKeyInst.setStatus("current")
_CfprVmSwitchManager_Type = CfprVmMgmtPlane
_CfprVmSwitchManager_Object = MibTableColumn
cfprVmSwitchManager = _CfprVmSwitchManager_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 11),
    _CfprVmSwitchManager_Type()
)
cfprVmSwitchManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchManager.setStatus("current")
_CfprVmSwitchName_Type = SnmpAdminString
_CfprVmSwitchName_Object = MibTableColumn
cfprVmSwitchName = _CfprVmSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 12),
    _CfprVmSwitchName_Type()
)
cfprVmSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchName.setStatus("current")
_CfprVmSwitchOwn_Type = CfprExtvmmOwnership
_CfprVmSwitchOwn_Object = MibTableColumn
cfprVmSwitchOwn = _CfprVmSwitchOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 13),
    _CfprVmSwitchOwn_Type()
)
cfprVmSwitchOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchOwn.setStatus("current")
_CfprVmSwitchPolicyLevel_Type = Gauge32
_CfprVmSwitchPolicyLevel_Object = MibTableColumn
cfprVmSwitchPolicyLevel = _CfprVmSwitchPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 14),
    _CfprVmSwitchPolicyLevel_Type()
)
cfprVmSwitchPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchPolicyLevel.setStatus("current")
_CfprVmSwitchPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmSwitchPolicyOwner_Object = MibTableColumn
cfprVmSwitchPolicyOwner = _CfprVmSwitchPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 15),
    _CfprVmSwitchPolicyOwner_Type()
)
cfprVmSwitchPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchPolicyOwner.setStatus("current")
_CfprVmSwitchUuid_Type = SnmpAdminString
_CfprVmSwitchUuid_Object = MibTableColumn
cfprVmSwitchUuid = _CfprVmSwitchUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 16),
    _CfprVmSwitchUuid_Type()
)
cfprVmSwitchUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchUuid.setStatus("current")
_CfprVmSwitchVendor_Type = CfprVmSwitchVendor
_CfprVmSwitchVendor_Object = MibTableColumn
cfprVmSwitchVendor = _CfprVmSwitchVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 14, 1, 17),
    _CfprVmSwitchVendor_Type()
)
cfprVmSwitchVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmSwitchVendor.setStatus("current")
_CfprVmVifTable_Object = MibTable
cfprVmVifTable = _CfprVmVifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15)
)
if mibBuilder.loadTexts:
    cfprVmVifTable.setStatus("current")
_CfprVmVifEntry_Object = MibTableRow
cfprVmVifEntry = _CfprVmVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1)
)
cfprVmVifEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmVifInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmVifEntry.setStatus("current")
_CfprVmVifInstanceId_Type = CfprManagedObjectId
_CfprVmVifInstanceId_Object = MibTableColumn
cfprVmVifInstanceId = _CfprVmVifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 1),
    _CfprVmVifInstanceId_Type()
)
cfprVmVifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmVifInstanceId.setStatus("current")
_CfprVmVifDn_Type = CfprManagedObjectDn
_CfprVmVifDn_Object = MibTableColumn
cfprVmVifDn = _CfprVmVifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 2),
    _CfprVmVifDn_Type()
)
cfprVmVifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifDn.setStatus("current")
_CfprVmVifRn_Type = SnmpAdminString
_CfprVmVifRn_Object = MibTableColumn
cfprVmVifRn = _CfprVmVifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 3),
    _CfprVmVifRn_Type()
)
cfprVmVifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifRn.setStatus("current")
_CfprVmVifAdpVifId_Type = Gauge32
_CfprVmVifAdpVifId_Object = MibTableColumn
cfprVmVifAdpVifId = _CfprVmVifAdpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 4),
    _CfprVmVifAdpVifId_Type()
)
cfprVmVifAdpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifAdpVifId.setStatus("current")
_CfprVmVifCookie_Type = Gauge32
_CfprVmVifCookie_Object = MibTableColumn
cfprVmVifCookie = _CfprVmVifCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 5),
    _CfprVmVifCookie_Type()
)
cfprVmVifCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifCookie.setStatus("current")
_CfprVmVifLinkState_Type = CfprAdaptorLinkState
_CfprVmVifLinkState_Object = MibTableColumn
cfprVmVifLinkState = _CfprVmVifLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 6),
    _CfprVmVifLinkState_Type()
)
cfprVmVifLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifLinkState.setStatus("current")
_CfprVmVifOperState_Type = CfprDcxOperState
_CfprVmVifOperState_Object = MibTableColumn
cfprVmVifOperState = _CfprVmVifOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 7),
    _CfprVmVifOperState_Type()
)
cfprVmVifOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifOperState.setStatus("current")
_CfprVmVifPhSwitchId_Type = CfprNetworkSwitchId
_CfprVmVifPhSwitchId_Object = MibTableColumn
cfprVmVifPhSwitchId = _CfprVmVifPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 8),
    _CfprVmVifPhSwitchId_Type()
)
cfprVmVifPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhSwitchId.setStatus("current")
_CfprVmVifPhsAccessAggrPortId_Type = Gauge32
_CfprVmVifPhsAccessAggrPortId_Object = MibTableColumn
cfprVmVifPhsAccessAggrPortId = _CfprVmVifPhsAccessAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 9),
    _CfprVmVifPhsAccessAggrPortId_Type()
)
cfprVmVifPhsAccessAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhsAccessAggrPortId.setStatus("current")
_CfprVmVifPhsAccessCardId_Type = Gauge32
_CfprVmVifPhsAccessCardId_Object = MibTableColumn
cfprVmVifPhsAccessCardId = _CfprVmVifPhsAccessCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 10),
    _CfprVmVifPhsAccessCardId_Type()
)
cfprVmVifPhsAccessCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhsAccessCardId.setStatus("current")
_CfprVmVifPhsAccessPortId_Type = Gauge32
_CfprVmVifPhsAccessPortId_Object = MibTableColumn
cfprVmVifPhsAccessPortId = _CfprVmVifPhsAccessPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 11),
    _CfprVmVifPhsAccessPortId_Type()
)
cfprVmVifPhsAccessPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhsAccessPortId.setStatus("current")
_CfprVmVifPhsBorderAggrPortId_Type = Gauge32
_CfprVmVifPhsBorderAggrPortId_Object = MibTableColumn
cfprVmVifPhsBorderAggrPortId = _CfprVmVifPhsBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 12),
    _CfprVmVifPhsBorderAggrPortId_Type()
)
cfprVmVifPhsBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhsBorderAggrPortId.setStatus("current")
_CfprVmVifPhsBorderCardId_Type = Gauge32
_CfprVmVifPhsBorderCardId_Object = MibTableColumn
cfprVmVifPhsBorderCardId = _CfprVmVifPhsBorderCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 13),
    _CfprVmVifPhsBorderCardId_Type()
)
cfprVmVifPhsBorderCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhsBorderCardId.setStatus("current")
_CfprVmVifPhsBorderPortId_Type = Gauge32
_CfprVmVifPhsBorderPortId_Object = MibTableColumn
cfprVmVifPhsBorderPortId = _CfprVmVifPhsBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 14),
    _CfprVmVifPhsBorderPortId_Type()
)
cfprVmVifPhsBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifPhsBorderPortId.setStatus("current")
_CfprVmVifStateQual_Type = SnmpAdminString
_CfprVmVifStateQual_Object = MibTableColumn
cfprVmVifStateQual = _CfprVmVifStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 15),
    _CfprVmVifStateQual_Type()
)
cfprVmVifStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifStateQual.setStatus("current")
_CfprVmVifStatusChangeTs_Type = DateAndTime
_CfprVmVifStatusChangeTs_Object = MibTableColumn
cfprVmVifStatusChangeTs = _CfprVmVifStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 16),
    _CfprVmVifStatusChangeTs_Type()
)
cfprVmVifStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifStatusChangeTs.setStatus("current")
_CfprVmVifVStatus_Type = CfprVmStatus
_CfprVmVifVStatus_Object = MibTableColumn
cfprVmVifVStatus = _CfprVmVifVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 17),
    _CfprVmVifVStatus_Type()
)
cfprVmVifVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifVStatus.setStatus("current")
_CfprVmVifVcDn_Type = SnmpAdminString
_CfprVmVifVcDn_Object = MibTableColumn
cfprVmVifVcDn = _CfprVmVifVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 18),
    _CfprVmVifVcDn_Type()
)
cfprVmVifVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifVcDn.setStatus("current")
_CfprVmVifVifId_Type = Gauge32
_CfprVmVifVifId_Object = MibTableColumn
cfprVmVifVifId = _CfprVmVifVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 19),
    _CfprVmVifVifId_Type()
)
cfprVmVifVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifVifId.setStatus("current")
_CfprVmVifServiceState_Type = CfprAdaptorServiceState
_CfprVmVifServiceState_Object = MibTableColumn
cfprVmVifServiceState = _CfprVmVifServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 15, 1, 20),
    _CfprVmVifServiceState_Type()
)
cfprVmVifServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVifServiceState.setStatus("current")
_CfprVmVlanTable_Object = MibTable
cfprVmVlanTable = _CfprVmVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16)
)
if mibBuilder.loadTexts:
    cfprVmVlanTable.setStatus("current")
_CfprVmVlanEntry_Object = MibTableRow
cfprVmVlanEntry = _CfprVmVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1)
)
cfprVmVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmVlanEntry.setStatus("current")
_CfprVmVlanInstanceId_Type = CfprManagedObjectId
_CfprVmVlanInstanceId_Object = MibTableColumn
cfprVmVlanInstanceId = _CfprVmVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 1),
    _CfprVmVlanInstanceId_Type()
)
cfprVmVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmVlanInstanceId.setStatus("current")
_CfprVmVlanDn_Type = CfprManagedObjectDn
_CfprVmVlanDn_Object = MibTableColumn
cfprVmVlanDn = _CfprVmVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 2),
    _CfprVmVlanDn_Type()
)
cfprVmVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanDn.setStatus("current")
_CfprVmVlanRn_Type = SnmpAdminString
_CfprVmVlanRn_Object = MibTableColumn
cfprVmVlanRn = _CfprVmVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 3),
    _CfprVmVlanRn_Type()
)
cfprVmVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanRn.setStatus("current")
_CfprVmVlanAssocPrimaryVlanState_Type = CfprFabricVlanAssocPrimaryVlanState
_CfprVmVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprVmVlanAssocPrimaryVlanState = _CfprVmVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 4),
    _CfprVmVlanAssocPrimaryVlanState_Type()
)
cfprVmVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanAssocPrimaryVlanState.setStatus("current")
_CfprVmVlanAssocPrimaryVlanSwitchId_Type = CfprFabricAVlanAssocPrimaryVlanSwitchId
_CfprVmVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprVmVlanAssocPrimaryVlanSwitchId = _CfprVmVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 5),
    _CfprVmVlanAssocPrimaryVlanSwitchId_Type()
)
cfprVmVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprVmVlanEpDn_Type = SnmpAdminString
_CfprVmVlanEpDn_Object = MibTableColumn
cfprVmVlanEpDn = _CfprVmVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 6),
    _CfprVmVlanEpDn_Type()
)
cfprVmVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanEpDn.setStatus("current")
_CfprVmVlanId_Type = Gauge32
_CfprVmVlanId_Object = MibTableColumn
cfprVmVlanId = _CfprVmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 7),
    _CfprVmVlanId_Type()
)
cfprVmVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanId.setStatus("current")
_CfprVmVlanIfRole_Type = CfprFabricVnetEpIfRole
_CfprVmVlanIfRole_Object = MibTableColumn
cfprVmVlanIfRole = _CfprVmVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 8),
    _CfprVmVlanIfRole_Type()
)
cfprVmVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanIfRole.setStatus("current")
_CfprVmVlanIfType_Type = CfprNetworkVnetEpIfType
_CfprVmVlanIfType_Object = MibTableColumn
cfprVmVlanIfType = _CfprVmVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 9),
    _CfprVmVlanIfType_Type()
)
cfprVmVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanIfType.setStatus("current")
_CfprVmVlanLocale_Type = CfprFabricVnetEpLocale
_CfprVmVlanLocale_Object = MibTableColumn
cfprVmVlanLocale = _CfprVmVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 10),
    _CfprVmVlanLocale_Type()
)
cfprVmVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanLocale.setStatus("current")
_CfprVmVlanName_Type = SnmpAdminString
_CfprVmVlanName_Object = MibTableColumn
cfprVmVlanName = _CfprVmVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 11),
    _CfprVmVlanName_Type()
)
cfprVmVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanName.setStatus("current")
_CfprVmVlanOperState_Type = CfprFabricVlanOperState
_CfprVmVlanOperState_Object = MibTableColumn
cfprVmVlanOperState = _CfprVmVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 12),
    _CfprVmVlanOperState_Type()
)
cfprVmVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanOperState.setStatus("current")
_CfprVmVlanOverlapStateForA_Type = CfprFabricVlanOverlapState
_CfprVmVlanOverlapStateForA_Object = MibTableColumn
cfprVmVlanOverlapStateForA = _CfprVmVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 13),
    _CfprVmVlanOverlapStateForA_Type()
)
cfprVmVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanOverlapStateForA.setStatus("current")
_CfprVmVlanOverlapStateForB_Type = CfprFabricVlanOverlapState
_CfprVmVlanOverlapStateForB_Object = MibTableColumn
cfprVmVlanOverlapStateForB = _CfprVmVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 14),
    _CfprVmVlanOverlapStateForB_Type()
)
cfprVmVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanOverlapStateForB.setStatus("current")
_CfprVmVlanPeerDn_Type = SnmpAdminString
_CfprVmVlanPeerDn_Object = MibTableColumn
cfprVmVlanPeerDn = _CfprVmVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 15),
    _CfprVmVlanPeerDn_Type()
)
cfprVmVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanPeerDn.setStatus("current")
_CfprVmVlanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprVmVlanPolicyOwner_Object = MibTableColumn
cfprVmVlanPolicyOwner = _CfprVmVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 16),
    _CfprVmVlanPolicyOwner_Type()
)
cfprVmVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanPolicyOwner.setStatus("current")
_CfprVmVlanPubNwDn_Type = SnmpAdminString
_CfprVmVlanPubNwDn_Object = MibTableColumn
cfprVmVlanPubNwDn = _CfprVmVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 17),
    _CfprVmVlanPubNwDn_Type()
)
cfprVmVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanPubNwDn.setStatus("current")
_CfprVmVlanPubNwId_Type = Gauge32
_CfprVmVlanPubNwId_Object = MibTableColumn
cfprVmVlanPubNwId = _CfprVmVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 18),
    _CfprVmVlanPubNwId_Type()
)
cfprVmVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanPubNwId.setStatus("current")
_CfprVmVlanPubNwName_Type = SnmpAdminString
_CfprVmVlanPubNwName_Object = MibTableColumn
cfprVmVlanPubNwName = _CfprVmVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 19),
    _CfprVmVlanPubNwName_Type()
)
cfprVmVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanPubNwName.setStatus("current")
_CfprVmVlanSharing_Type = CfprFabricAVlanSharing
_CfprVmVlanSharing_Object = MibTableColumn
cfprVmVlanSharing = _CfprVmVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 20),
    _CfprVmVlanSharing_Type()
)
cfprVmVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanSharing.setStatus("current")
_CfprVmVlanSwitchId_Type = CfprNetworkSwitchId
_CfprVmVlanSwitchId_Object = MibTableColumn
cfprVmVlanSwitchId = _CfprVmVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 21),
    _CfprVmVlanSwitchId_Type()
)
cfprVmVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanSwitchId.setStatus("current")
_CfprVmVlanTransport_Type = CfprFabricAVlanTransport
_CfprVmVlanTransport_Object = MibTableColumn
cfprVmVlanTransport = _CfprVmVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 22),
    _CfprVmVlanTransport_Type()
)
cfprVmVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanTransport.setStatus("current")
_CfprVmVlanType_Type = CfprFabricAVlanType
_CfprVmVlanType_Object = MibTableColumn
cfprVmVlanType = _CfprVmVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 16, 1, 23),
    _CfprVmVlanType_Type()
)
cfprVmVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVlanType.setStatus("current")
_CfprVmVnicProfClTable_Object = MibTable
cfprVmVnicProfClTable = _CfprVmVnicProfClTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17)
)
if mibBuilder.loadTexts:
    cfprVmVnicProfClTable.setStatus("current")
_CfprVmVnicProfClEntry_Object = MibTableRow
cfprVmVnicProfClEntry = _CfprVmVnicProfClEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1)
)
cfprVmVnicProfClEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmVnicProfClInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmVnicProfClEntry.setStatus("current")
_CfprVmVnicProfClInstanceId_Type = CfprManagedObjectId
_CfprVmVnicProfClInstanceId_Object = MibTableColumn
cfprVmVnicProfClInstanceId = _CfprVmVnicProfClInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 1),
    _CfprVmVnicProfClInstanceId_Type()
)
cfprVmVnicProfClInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmVnicProfClInstanceId.setStatus("current")
_CfprVmVnicProfClDn_Type = CfprManagedObjectDn
_CfprVmVnicProfClDn_Object = MibTableColumn
cfprVmVnicProfClDn = _CfprVmVnicProfClDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 2),
    _CfprVmVnicProfClDn_Type()
)
cfprVmVnicProfClDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClDn.setStatus("current")
_CfprVmVnicProfClRn_Type = SnmpAdminString
_CfprVmVnicProfClRn_Object = MibTableColumn
cfprVmVnicProfClRn = _CfprVmVnicProfClRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 3),
    _CfprVmVnicProfClRn_Type()
)
cfprVmVnicProfClRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClRn.setStatus("current")
_CfprVmVnicProfClDcName_Type = SnmpAdminString
_CfprVmVnicProfClDcName_Object = MibTableColumn
cfprVmVnicProfClDcName = _CfprVmVnicProfClDcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 4),
    _CfprVmVnicProfClDcName_Type()
)
cfprVmVnicProfClDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClDcName.setStatus("current")
_CfprVmVnicProfClDescr_Type = SnmpAdminString
_CfprVmVnicProfClDescr_Object = MibTableColumn
cfprVmVnicProfClDescr = _CfprVmVnicProfClDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 5),
    _CfprVmVnicProfClDescr_Type()
)
cfprVmVnicProfClDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClDescr.setStatus("current")
_CfprVmVnicProfClIntId_Type = SnmpAdminString
_CfprVmVnicProfClIntId_Object = MibTableColumn
cfprVmVnicProfClIntId = _CfprVmVnicProfClIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 6),
    _CfprVmVnicProfClIntId_Type()
)
cfprVmVnicProfClIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClIntId.setStatus("current")
_CfprVmVnicProfClName_Type = SnmpAdminString
_CfprVmVnicProfClName_Object = MibTableColumn
cfprVmVnicProfClName = _CfprVmVnicProfClName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 7),
    _CfprVmVnicProfClName_Type()
)
cfprVmVnicProfClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClName.setStatus("current")
_CfprVmVnicProfClOrgPath_Type = SnmpAdminString
_CfprVmVnicProfClOrgPath_Object = MibTableColumn
cfprVmVnicProfClOrgPath = _CfprVmVnicProfClOrgPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 8),
    _CfprVmVnicProfClOrgPath_Type()
)
cfprVmVnicProfClOrgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClOrgPath.setStatus("current")
_CfprVmVnicProfClPolicyLevel_Type = Gauge32
_CfprVmVnicProfClPolicyLevel_Object = MibTableColumn
cfprVmVnicProfClPolicyLevel = _CfprVmVnicProfClPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 9),
    _CfprVmVnicProfClPolicyLevel_Type()
)
cfprVmVnicProfClPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClPolicyLevel.setStatus("current")
_CfprVmVnicProfClPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmVnicProfClPolicyOwner_Object = MibTableColumn
cfprVmVnicProfClPolicyOwner = _CfprVmVnicProfClPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 10),
    _CfprVmVnicProfClPolicyOwner_Type()
)
cfprVmVnicProfClPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClPolicyOwner.setStatus("current")
_CfprVmVnicProfClSwName_Type = SnmpAdminString
_CfprVmVnicProfClSwName_Object = MibTableColumn
cfprVmVnicProfClSwName = _CfprVmVnicProfClSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 17, 1, 11),
    _CfprVmVnicProfClSwName_Type()
)
cfprVmVnicProfClSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfClSwName.setStatus("current")
_CfprVmVnicProfInstTable_Object = MibTable
cfprVmVnicProfInstTable = _CfprVmVnicProfInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18)
)
if mibBuilder.loadTexts:
    cfprVmVnicProfInstTable.setStatus("current")
_CfprVmVnicProfInstEntry_Object = MibTableRow
cfprVmVnicProfInstEntry = _CfprVmVnicProfInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1)
)
cfprVmVnicProfInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmVnicProfInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmVnicProfInstEntry.setStatus("current")
_CfprVmVnicProfInstInstanceId_Type = CfprManagedObjectId
_CfprVmVnicProfInstInstanceId_Object = MibTableColumn
cfprVmVnicProfInstInstanceId = _CfprVmVnicProfInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 1),
    _CfprVmVnicProfInstInstanceId_Type()
)
cfprVmVnicProfInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstInstanceId.setStatus("current")
_CfprVmVnicProfInstDn_Type = CfprManagedObjectDn
_CfprVmVnicProfInstDn_Object = MibTableColumn
cfprVmVnicProfInstDn = _CfprVmVnicProfInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 2),
    _CfprVmVnicProfInstDn_Type()
)
cfprVmVnicProfInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstDn.setStatus("current")
_CfprVmVnicProfInstRn_Type = SnmpAdminString
_CfprVmVnicProfInstRn_Object = MibTableColumn
cfprVmVnicProfInstRn = _CfprVmVnicProfInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 3),
    _CfprVmVnicProfInstRn_Type()
)
cfprVmVnicProfInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstRn.setStatus("current")
_CfprVmVnicProfInstDescr_Type = SnmpAdminString
_CfprVmVnicProfInstDescr_Object = MibTableColumn
cfprVmVnicProfInstDescr = _CfprVmVnicProfInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 4),
    _CfprVmVnicProfInstDescr_Type()
)
cfprVmVnicProfInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstDescr.setStatus("current")
_CfprVmVnicProfInstIntId_Type = SnmpAdminString
_CfprVmVnicProfInstIntId_Object = MibTableColumn
cfprVmVnicProfInstIntId = _CfprVmVnicProfInstIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 5),
    _CfprVmVnicProfInstIntId_Type()
)
cfprVmVnicProfInstIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstIntId.setStatus("current")
_CfprVmVnicProfInstMaxPorts_Type = Gauge32
_CfprVmVnicProfInstMaxPorts_Object = MibTableColumn
cfprVmVnicProfInstMaxPorts = _CfprVmVnicProfInstMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 6),
    _CfprVmVnicProfInstMaxPorts_Type()
)
cfprVmVnicProfInstMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstMaxPorts.setStatus("current")
_CfprVmVnicProfInstName_Type = SnmpAdminString
_CfprVmVnicProfInstName_Object = MibTableColumn
cfprVmVnicProfInstName = _CfprVmVnicProfInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 7),
    _CfprVmVnicProfInstName_Type()
)
cfprVmVnicProfInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstName.setStatus("current")
_CfprVmVnicProfInstPolicyLevel_Type = Gauge32
_CfprVmVnicProfInstPolicyLevel_Object = MibTableColumn
cfprVmVnicProfInstPolicyLevel = _CfprVmVnicProfInstPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 8),
    _CfprVmVnicProfInstPolicyLevel_Type()
)
cfprVmVnicProfInstPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstPolicyLevel.setStatus("current")
_CfprVmVnicProfInstPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVmVnicProfInstPolicyOwner_Object = MibTableColumn
cfprVmVnicProfInstPolicyOwner = _CfprVmVnicProfInstPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 9),
    _CfprVmVnicProfInstPolicyOwner_Type()
)
cfprVmVnicProfInstPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstPolicyOwner.setStatus("current")
_CfprVmVnicProfInstProfDn_Type = SnmpAdminString
_CfprVmVnicProfInstProfDn_Object = MibTableColumn
cfprVmVnicProfInstProfDn = _CfprVmVnicProfInstProfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 10),
    _CfprVmVnicProfInstProfDn_Type()
)
cfprVmVnicProfInstProfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstProfDn.setStatus("current")
_CfprVmVnicProfInstProfileType_Type = CfprVnicPortProfileType
_CfprVmVnicProfInstProfileType_Object = MibTableColumn
cfprVmVnicProfInstProfileType = _CfprVmVnicProfInstProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 18, 1, 11),
    _CfprVmVnicProfInstProfileType_Type()
)
cfprVmVnicProfInstProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVnicProfInstProfileType.setStatus("current")
_CfprVmVsanTable_Object = MibTable
cfprVmVsanTable = _CfprVmVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19)
)
if mibBuilder.loadTexts:
    cfprVmVsanTable.setStatus("current")
_CfprVmVsanEntry_Object = MibTableRow
cfprVmVsanEntry = _CfprVmVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1)
)
cfprVmVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VM-MIB", "cfprVmVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVmVsanEntry.setStatus("current")
_CfprVmVsanInstanceId_Type = CfprManagedObjectId
_CfprVmVsanInstanceId_Object = MibTableColumn
cfprVmVsanInstanceId = _CfprVmVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 1),
    _CfprVmVsanInstanceId_Type()
)
cfprVmVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVmVsanInstanceId.setStatus("current")
_CfprVmVsanDn_Type = CfprManagedObjectDn
_CfprVmVsanDn_Object = MibTableColumn
cfprVmVsanDn = _CfprVmVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 2),
    _CfprVmVsanDn_Type()
)
cfprVmVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanDn.setStatus("current")
_CfprVmVsanRn_Type = SnmpAdminString
_CfprVmVsanRn_Object = MibTableColumn
cfprVmVsanRn = _CfprVmVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 3),
    _CfprVmVsanRn_Type()
)
cfprVmVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanRn.setStatus("current")
_CfprVmVsanEpDn_Type = SnmpAdminString
_CfprVmVsanEpDn_Object = MibTableColumn
cfprVmVsanEpDn = _CfprVmVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 4),
    _CfprVmVsanEpDn_Type()
)
cfprVmVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanEpDn.setStatus("current")
_CfprVmVsanFcoeVlan_Type = Gauge32
_CfprVmVsanFcoeVlan_Object = MibTableColumn
cfprVmVsanFcoeVlan = _CfprVmVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 5),
    _CfprVmVsanFcoeVlan_Type()
)
cfprVmVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanFcoeVlan.setStatus("current")
_CfprVmVsanId_Type = Gauge32
_CfprVmVsanId_Object = MibTableColumn
cfprVmVsanId = _CfprVmVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 6),
    _CfprVmVsanId_Type()
)
cfprVmVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanId.setStatus("current")
_CfprVmVsanIfRole_Type = CfprFabricVnetEpIfRole
_CfprVmVsanIfRole_Object = MibTableColumn
cfprVmVsanIfRole = _CfprVmVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 7),
    _CfprVmVsanIfRole_Type()
)
cfprVmVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanIfRole.setStatus("current")
_CfprVmVsanIfType_Type = CfprNetworkVnetEpIfType
_CfprVmVsanIfType_Object = MibTableColumn
cfprVmVsanIfType = _CfprVmVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 8),
    _CfprVmVsanIfType_Type()
)
cfprVmVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanIfType.setStatus("current")
_CfprVmVsanLocale_Type = CfprFabricVnetEpLocale
_CfprVmVsanLocale_Object = MibTableColumn
cfprVmVsanLocale = _CfprVmVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 9),
    _CfprVmVsanLocale_Type()
)
cfprVmVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanLocale.setStatus("current")
_CfprVmVsanName_Type = SnmpAdminString
_CfprVmVsanName_Object = MibTableColumn
cfprVmVsanName = _CfprVmVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 10),
    _CfprVmVsanName_Type()
)
cfprVmVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanName.setStatus("current")
_CfprVmVsanOperState_Type = CfprFabricVsanOperState
_CfprVmVsanOperState_Object = MibTableColumn
cfprVmVsanOperState = _CfprVmVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 11),
    _CfprVmVsanOperState_Type()
)
cfprVmVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanOperState.setStatus("current")
_CfprVmVsanPeerDn_Type = SnmpAdminString
_CfprVmVsanPeerDn_Object = MibTableColumn
cfprVmVsanPeerDn = _CfprVmVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 12),
    _CfprVmVsanPeerDn_Type()
)
cfprVmVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanPeerDn.setStatus("current")
_CfprVmVsanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprVmVsanPolicyOwner_Object = MibTableColumn
cfprVmVsanPolicyOwner = _CfprVmVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 13),
    _CfprVmVsanPolicyOwner_Type()
)
cfprVmVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanPolicyOwner.setStatus("current")
_CfprVmVsanSwitchId_Type = CfprNetworkSwitchId
_CfprVmVsanSwitchId_Object = MibTableColumn
cfprVmVsanSwitchId = _CfprVmVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 14),
    _CfprVmVsanSwitchId_Type()
)
cfprVmVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanSwitchId.setStatus("current")
_CfprVmVsanTransport_Type = CfprFabricAVsanTransport
_CfprVmVsanTransport_Object = MibTableColumn
cfprVmVsanTransport = _CfprVmVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 15),
    _CfprVmVsanTransport_Type()
)
cfprVmVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanTransport.setStatus("current")
_CfprVmVsanType_Type = CfprFabricAVsanType
_CfprVmVsanType_Object = MibTableColumn
cfprVmVsanType = _CfprVmVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 16),
    _CfprVmVsanType_Type()
)
cfprVmVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanType.setStatus("current")
_CfprVmVsanZoningState_Type = CfprFabricZoningState
_CfprVmVsanZoningState_Object = MibTableColumn
cfprVmVsanZoningState = _CfprVmVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 82, 19, 1, 17),
    _CfprVmVsanZoningState_Type()
)
cfprVmVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVmVsanZoningState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-VM-MIB",
    **{"cfprVmObjects": cfprVmObjects,
       "cfprVmComputeEpTable": cfprVmComputeEpTable,
       "cfprVmComputeEpEntry": cfprVmComputeEpEntry,
       "cfprVmComputeEpInstanceId": cfprVmComputeEpInstanceId,
       "cfprVmComputeEpDn": cfprVmComputeEpDn,
       "cfprVmComputeEpRn": cfprVmComputeEpRn,
       "cfprVmComputeEpClInstType": cfprVmComputeEpClInstType,
       "cfprVmComputeEpComputeEpVendor": cfprVmComputeEpComputeEpVendor,
       "cfprVmComputeEpDescr": cfprVmComputeEpDescr,
       "cfprVmComputeEpDvsDn": cfprVmComputeEpDvsDn,
       "cfprVmComputeEpDvsName": cfprVmComputeEpDvsName,
       "cfprVmComputeEpHostName": cfprVmComputeEpHostName,
       "cfprVmComputeEpIntId": cfprVmComputeEpIntId,
       "cfprVmComputeEpLsDn": cfprVmComputeEpLsDn,
       "cfprVmComputeEpModel": cfprVmComputeEpModel,
       "cfprVmComputeEpName": cfprVmComputeEpName,
       "cfprVmComputeEpPnDn": cfprVmComputeEpPnDn,
       "cfprVmComputeEpPolicyLevel": cfprVmComputeEpPolicyLevel,
       "cfprVmComputeEpPolicyOwner": cfprVmComputeEpPolicyOwner,
       "cfprVmComputeEpStatusChangeTs": cfprVmComputeEpStatusChangeTs,
       "cfprVmComputeEpUuid": cfprVmComputeEpUuid,
       "cfprVmComputeEpVStatus": cfprVmComputeEpVStatus,
       "cfprVmComputeEpVendor": cfprVmComputeEpVendor,
       "cfprVmDCTable": cfprVmDCTable,
       "cfprVmDCEntry": cfprVmDCEntry,
       "cfprVmDCInstanceId": cfprVmDCInstanceId,
       "cfprVmDCDn": cfprVmDCDn,
       "cfprVmDCRn": cfprVmDCRn,
       "cfprVmDCDescr": cfprVmDCDescr,
       "cfprVmDCIntId": cfprVmDCIntId,
       "cfprVmDCName": cfprVmDCName,
       "cfprVmDCOwn": cfprVmDCOwn,
       "cfprVmDCPolicyLevel": cfprVmDCPolicyLevel,
       "cfprVmDCPolicyOwner": cfprVmDCPolicyOwner,
       "cfprVmDCUuid": cfprVmDCUuid,
       "cfprVmDCOrgTable": cfprVmDCOrgTable,
       "cfprVmDCOrgEntry": cfprVmDCOrgEntry,
       "cfprVmDCOrgInstanceId": cfprVmDCOrgInstanceId,
       "cfprVmDCOrgDn": cfprVmDCOrgDn,
       "cfprVmDCOrgRn": cfprVmDCOrgRn,
       "cfprVmDCOrgDescr": cfprVmDCOrgDescr,
       "cfprVmDCOrgIntId": cfprVmDCOrgIntId,
       "cfprVmDCOrgName": cfprVmDCOrgName,
       "cfprVmDCOrgOwn": cfprVmDCOrgOwn,
       "cfprVmDCOrgPolicyLevel": cfprVmDCOrgPolicyLevel,
       "cfprVmDCOrgPolicyOwner": cfprVmDCOrgPolicyOwner,
       "cfprVmDCOrgUuid": cfprVmDCOrgUuid,
       "cfprVmEpTable": cfprVmEpTable,
       "cfprVmEpEntry": cfprVmEpEntry,
       "cfprVmEpInstanceId": cfprVmEpInstanceId,
       "cfprVmEpDn": cfprVmEpDn,
       "cfprVmEpRn": cfprVmEpRn,
       "cfprVmHbaTable": cfprVmHbaTable,
       "cfprVmHbaEntry": cfprVmHbaEntry,
       "cfprVmHbaInstanceId": cfprVmHbaInstanceId,
       "cfprVmHbaDn": cfprVmHbaDn,
       "cfprVmHbaRn": cfprVmHbaRn,
       "cfprVmHbaDvsGenPortId": cfprVmHbaDvsGenPortId,
       "cfprVmHbaDvsPortId": cfprVmHbaDvsPortId,
       "cfprVmHbaDvsSwitchId": cfprVmHbaDvsSwitchId,
       "cfprVmHbaHostIfDn": cfprVmHbaHostIfDn,
       "cfprVmHbaName": cfprVmHbaName,
       "cfprVmHbaOwner": cfprVmHbaOwner,
       "cfprVmHbaPhSwitchId": cfprVmHbaPhSwitchId,
       "cfprVmHbaProfileId": cfprVmHbaProfileId,
       "cfprVmHbaProfileName": cfprVmHbaProfileName,
       "cfprVmHbaStatusChangeTs": cfprVmHbaStatusChangeTs,
       "cfprVmHbaSwitchId": cfprVmHbaSwitchId,
       "cfprVmHbaType": cfprVmHbaType,
       "cfprVmHbaUuid": cfprVmHbaUuid,
       "cfprVmHbaVStatus": cfprVmHbaVStatus,
       "cfprVmHbaVcDn": cfprVmHbaVcDn,
       "cfprVmHbaVifId": cfprVmHbaVifId,
       "cfprVmHbaVmndGuid": cfprVmHbaVmndGuid,
       "cfprVmHbaVmndName": cfprVmHbaVmndName,
       "cfprVmHbaVnicDn": cfprVmHbaVnicDn,
       "cfprVmHbaWwnn": cfprVmHbaWwnn,
       "cfprVmHbaWwpn": cfprVmHbaWwpn,
       "cfprVmHvTable": cfprVmHvTable,
       "cfprVmHvEntry": cfprVmHvEntry,
       "cfprVmHvInstanceId": cfprVmHvInstanceId,
       "cfprVmHvDn": cfprVmHvDn,
       "cfprVmHvRn": cfprVmHvRn,
       "cfprVmHvClInstType": cfprVmHvClInstType,
       "cfprVmHvDescr": cfprVmHvDescr,
       "cfprVmHvDvsDn": cfprVmHvDvsDn,
       "cfprVmHvDvsName": cfprVmHvDvsName,
       "cfprVmHvFltAggr": cfprVmHvFltAggr,
       "cfprVmHvHvType": cfprVmHvHvType,
       "cfprVmHvIntId": cfprVmHvIntId,
       "cfprVmHvLsDn": cfprVmHvLsDn,
       "cfprVmHvModel": cfprVmHvModel,
       "cfprVmHvName": cfprVmHvName,
       "cfprVmHvPnDn": cfprVmHvPnDn,
       "cfprVmHvPolicyLevel": cfprVmHvPolicyLevel,
       "cfprVmHvPolicyOwner": cfprVmHvPolicyOwner,
       "cfprVmHvStatusChangeTs": cfprVmHvStatusChangeTs,
       "cfprVmHvUuid": cfprVmHvUuid,
       "cfprVmHvVStatus": cfprVmHvVStatus,
       "cfprVmHvVendor": cfprVmHvVendor,
       "cfprVmInstanceTable": cfprVmInstanceTable,
       "cfprVmInstanceEntry": cfprVmInstanceEntry,
       "cfprVmInstanceInstanceId": cfprVmInstanceInstanceId,
       "cfprVmInstanceDn": cfprVmInstanceDn,
       "cfprVmInstanceRn": cfprVmInstanceRn,
       "cfprVmInstanceClInstType": cfprVmInstanceClInstType,
       "cfprVmInstanceDescr": cfprVmInstanceDescr,
       "cfprVmInstanceDvsDn": cfprVmInstanceDvsDn,
       "cfprVmInstanceDvsName": cfprVmInstanceDvsName,
       "cfprVmInstanceFltAggr": cfprVmInstanceFltAggr,
       "cfprVmInstanceHvDn": cfprVmInstanceHvDn,
       "cfprVmInstanceHvType": cfprVmInstanceHvType,
       "cfprVmInstanceHvUuid": cfprVmInstanceHvUuid,
       "cfprVmInstanceIntId": cfprVmInstanceIntId,
       "cfprVmInstanceLsDn": cfprVmInstanceLsDn,
       "cfprVmInstanceModel": cfprVmInstanceModel,
       "cfprVmInstanceName": cfprVmInstanceName,
       "cfprVmInstancePnDn": cfprVmInstancePnDn,
       "cfprVmInstancePolicyLevel": cfprVmInstancePolicyLevel,
       "cfprVmInstancePolicyOwner": cfprVmInstancePolicyOwner,
       "cfprVmInstanceStatusChangeTs": cfprVmInstanceStatusChangeTs,
       "cfprVmInstanceUuid": cfprVmInstanceUuid,
       "cfprVmInstanceVStatus": cfprVmInstanceVStatus,
       "cfprVmInstanceVendor": cfprVmInstanceVendor,
       "cfprVmLifeCyclePolicyTable": cfprVmLifeCyclePolicyTable,
       "cfprVmLifeCyclePolicyEntry": cfprVmLifeCyclePolicyEntry,
       "cfprVmLifeCyclePolicyInstanceId": cfprVmLifeCyclePolicyInstanceId,
       "cfprVmLifeCyclePolicyDn": cfprVmLifeCyclePolicyDn,
       "cfprVmLifeCyclePolicyRn": cfprVmLifeCyclePolicyRn,
       "cfprVmLifeCyclePolicyDescr": cfprVmLifeCyclePolicyDescr,
       "cfprVmLifeCyclePolicyFsmDescr": cfprVmLifeCyclePolicyFsmDescr,
       "cfprVmLifeCyclePolicyFsmPrev": cfprVmLifeCyclePolicyFsmPrev,
       "cfprVmLifeCyclePolicyFsmProgr": cfprVmLifeCyclePolicyFsmProgr,
       "cfprVmLifeCyclePolicyFsmRmtInvErrCode": cfprVmLifeCyclePolicyFsmRmtInvErrCode,
       "cfprVmLifeCyclePolicyFsmRmtInvErrDescr": cfprVmLifeCyclePolicyFsmRmtInvErrDescr,
       "cfprVmLifeCyclePolicyFsmRmtInvRslt": cfprVmLifeCyclePolicyFsmRmtInvRslt,
       "cfprVmLifeCyclePolicyFsmStageDescr": cfprVmLifeCyclePolicyFsmStageDescr,
       "cfprVmLifeCyclePolicyFsmStamp": cfprVmLifeCyclePolicyFsmStamp,
       "cfprVmLifeCyclePolicyFsmStatus": cfprVmLifeCyclePolicyFsmStatus,
       "cfprVmLifeCyclePolicyFsmTry": cfprVmLifeCyclePolicyFsmTry,
       "cfprVmLifeCyclePolicyIntId": cfprVmLifeCyclePolicyIntId,
       "cfprVmLifeCyclePolicyName": cfprVmLifeCyclePolicyName,
       "cfprVmLifeCyclePolicyPolicyLevel": cfprVmLifeCyclePolicyPolicyLevel,
       "cfprVmLifeCyclePolicyPolicyOwner": cfprVmLifeCyclePolicyPolicyOwner,
       "cfprVmLifeCyclePolicyVmRetention": cfprVmLifeCyclePolicyVmRetention,
       "cfprVmLifeCyclePolicyVnicRetention": cfprVmLifeCyclePolicyVnicRetention,
       "cfprVmLifeCyclePolicyFsmTable": cfprVmLifeCyclePolicyFsmTable,
       "cfprVmLifeCyclePolicyFsmEntry": cfprVmLifeCyclePolicyFsmEntry,
       "cfprVmLifeCyclePolicyFsmInstanceId": cfprVmLifeCyclePolicyFsmInstanceId,
       "cfprVmLifeCyclePolicyFsmDn": cfprVmLifeCyclePolicyFsmDn,
       "cfprVmLifeCyclePolicyFsmRn": cfprVmLifeCyclePolicyFsmRn,
       "cfprVmLifeCyclePolicyFsmCompletionTime": cfprVmLifeCyclePolicyFsmCompletionTime,
       "cfprVmLifeCyclePolicyFsmCurrentFsm": cfprVmLifeCyclePolicyFsmCurrentFsm,
       "cfprVmLifeCyclePolicyFsmDescrData": cfprVmLifeCyclePolicyFsmDescrData,
       "cfprVmLifeCyclePolicyFsmFsmStatus": cfprVmLifeCyclePolicyFsmFsmStatus,
       "cfprVmLifeCyclePolicyFsmProgress": cfprVmLifeCyclePolicyFsmProgress,
       "cfprVmLifeCyclePolicyFsmRmtErrCode": cfprVmLifeCyclePolicyFsmRmtErrCode,
       "cfprVmLifeCyclePolicyFsmRmtErrDescr": cfprVmLifeCyclePolicyFsmRmtErrDescr,
       "cfprVmLifeCyclePolicyFsmRmtRslt": cfprVmLifeCyclePolicyFsmRmtRslt,
       "cfprVmLifeCyclePolicyFsmStageTable": cfprVmLifeCyclePolicyFsmStageTable,
       "cfprVmLifeCyclePolicyFsmStageEntry": cfprVmLifeCyclePolicyFsmStageEntry,
       "cfprVmLifeCyclePolicyFsmStageInstanceId": cfprVmLifeCyclePolicyFsmStageInstanceId,
       "cfprVmLifeCyclePolicyFsmStageDn": cfprVmLifeCyclePolicyFsmStageDn,
       "cfprVmLifeCyclePolicyFsmStageRn": cfprVmLifeCyclePolicyFsmStageRn,
       "cfprVmLifeCyclePolicyFsmStageDescrData": cfprVmLifeCyclePolicyFsmStageDescrData,
       "cfprVmLifeCyclePolicyFsmStageLastUpdateTime": cfprVmLifeCyclePolicyFsmStageLastUpdateTime,
       "cfprVmLifeCyclePolicyFsmStageName": cfprVmLifeCyclePolicyFsmStageName,
       "cfprVmLifeCyclePolicyFsmStageOrder": cfprVmLifeCyclePolicyFsmStageOrder,
       "cfprVmLifeCyclePolicyFsmStageRetry": cfprVmLifeCyclePolicyFsmStageRetry,
       "cfprVmLifeCyclePolicyFsmStageStageStatus": cfprVmLifeCyclePolicyFsmStageStageStatus,
       "cfprVmLifeCyclePolicyFsmTaskTable": cfprVmLifeCyclePolicyFsmTaskTable,
       "cfprVmLifeCyclePolicyFsmTaskEntry": cfprVmLifeCyclePolicyFsmTaskEntry,
       "cfprVmLifeCyclePolicyFsmTaskInstanceId": cfprVmLifeCyclePolicyFsmTaskInstanceId,
       "cfprVmLifeCyclePolicyFsmTaskDn": cfprVmLifeCyclePolicyFsmTaskDn,
       "cfprVmLifeCyclePolicyFsmTaskRn": cfprVmLifeCyclePolicyFsmTaskRn,
       "cfprVmLifeCyclePolicyFsmTaskCompletion": cfprVmLifeCyclePolicyFsmTaskCompletion,
       "cfprVmLifeCyclePolicyFsmTaskFlags": cfprVmLifeCyclePolicyFsmTaskFlags,
       "cfprVmLifeCyclePolicyFsmTaskItem": cfprVmLifeCyclePolicyFsmTaskItem,
       "cfprVmLifeCyclePolicyFsmTaskSeqId": cfprVmLifeCyclePolicyFsmTaskSeqId,
       "cfprVmNicTable": cfprVmNicTable,
       "cfprVmNicEntry": cfprVmNicEntry,
       "cfprVmNicInstanceId": cfprVmNicInstanceId,
       "cfprVmNicDn": cfprVmNicDn,
       "cfprVmNicRn": cfprVmNicRn,
       "cfprVmNicDvsGenPortId": cfprVmNicDvsGenPortId,
       "cfprVmNicDvsPortId": cfprVmNicDvsPortId,
       "cfprVmNicDvsSwitchId": cfprVmNicDvsSwitchId,
       "cfprVmNicHostIfDn": cfprVmNicHostIfDn,
       "cfprVmNicMacAddr": cfprVmNicMacAddr,
       "cfprVmNicName": cfprVmNicName,
       "cfprVmNicOwner": cfprVmNicOwner,
       "cfprVmNicPhSwitchId": cfprVmNicPhSwitchId,
       "cfprVmNicProfileId": cfprVmNicProfileId,
       "cfprVmNicProfileName": cfprVmNicProfileName,
       "cfprVmNicStatusChangeTs": cfprVmNicStatusChangeTs,
       "cfprVmNicSwitchId": cfprVmNicSwitchId,
       "cfprVmNicType": cfprVmNicType,
       "cfprVmNicUuid": cfprVmNicUuid,
       "cfprVmNicVStatus": cfprVmNicVStatus,
       "cfprVmNicVcDn": cfprVmNicVcDn,
       "cfprVmNicVifId": cfprVmNicVifId,
       "cfprVmNicVmndGuid": cfprVmNicVmndGuid,
       "cfprVmNicVmndName": cfprVmNicVmndName,
       "cfprVmNicVnicDn": cfprVmNicVnicDn,
       "cfprVmOrgTable": cfprVmOrgTable,
       "cfprVmOrgEntry": cfprVmOrgEntry,
       "cfprVmOrgInstanceId": cfprVmOrgInstanceId,
       "cfprVmOrgDn": cfprVmOrgDn,
       "cfprVmOrgRn": cfprVmOrgRn,
       "cfprVmOrgDescr": cfprVmOrgDescr,
       "cfprVmOrgIntId": cfprVmOrgIntId,
       "cfprVmOrgName": cfprVmOrgName,
       "cfprVmOrgOwn": cfprVmOrgOwn,
       "cfprVmOrgPolicyLevel": cfprVmOrgPolicyLevel,
       "cfprVmOrgPolicyOwner": cfprVmOrgPolicyOwner,
       "cfprVmOrgUuid": cfprVmOrgUuid,
       "cfprVmSwitchTable": cfprVmSwitchTable,
       "cfprVmSwitchEntry": cfprVmSwitchEntry,
       "cfprVmSwitchInstanceId": cfprVmSwitchInstanceId,
       "cfprVmSwitchDn": cfprVmSwitchDn,
       "cfprVmSwitchRn": cfprVmSwitchRn,
       "cfprVmSwitchAdminState": cfprVmSwitchAdminState,
       "cfprVmSwitchDescr": cfprVmSwitchDescr,
       "cfprVmSwitchExtKey": cfprVmSwitchExtKey,
       "cfprVmSwitchFltAggr": cfprVmSwitchFltAggr,
       "cfprVmSwitchId": cfprVmSwitchId,
       "cfprVmSwitchIntId": cfprVmSwitchIntId,
       "cfprVmSwitchKeyInst": cfprVmSwitchKeyInst,
       "cfprVmSwitchManager": cfprVmSwitchManager,
       "cfprVmSwitchName": cfprVmSwitchName,
       "cfprVmSwitchOwn": cfprVmSwitchOwn,
       "cfprVmSwitchPolicyLevel": cfprVmSwitchPolicyLevel,
       "cfprVmSwitchPolicyOwner": cfprVmSwitchPolicyOwner,
       "cfprVmSwitchUuid": cfprVmSwitchUuid,
       "cfprVmSwitchVendor": cfprVmSwitchVendor,
       "cfprVmVifTable": cfprVmVifTable,
       "cfprVmVifEntry": cfprVmVifEntry,
       "cfprVmVifInstanceId": cfprVmVifInstanceId,
       "cfprVmVifDn": cfprVmVifDn,
       "cfprVmVifRn": cfprVmVifRn,
       "cfprVmVifAdpVifId": cfprVmVifAdpVifId,
       "cfprVmVifCookie": cfprVmVifCookie,
       "cfprVmVifLinkState": cfprVmVifLinkState,
       "cfprVmVifOperState": cfprVmVifOperState,
       "cfprVmVifPhSwitchId": cfprVmVifPhSwitchId,
       "cfprVmVifPhsAccessAggrPortId": cfprVmVifPhsAccessAggrPortId,
       "cfprVmVifPhsAccessCardId": cfprVmVifPhsAccessCardId,
       "cfprVmVifPhsAccessPortId": cfprVmVifPhsAccessPortId,
       "cfprVmVifPhsBorderAggrPortId": cfprVmVifPhsBorderAggrPortId,
       "cfprVmVifPhsBorderCardId": cfprVmVifPhsBorderCardId,
       "cfprVmVifPhsBorderPortId": cfprVmVifPhsBorderPortId,
       "cfprVmVifStateQual": cfprVmVifStateQual,
       "cfprVmVifStatusChangeTs": cfprVmVifStatusChangeTs,
       "cfprVmVifVStatus": cfprVmVifVStatus,
       "cfprVmVifVcDn": cfprVmVifVcDn,
       "cfprVmVifVifId": cfprVmVifVifId,
       "cfprVmVifServiceState": cfprVmVifServiceState,
       "cfprVmVlanTable": cfprVmVlanTable,
       "cfprVmVlanEntry": cfprVmVlanEntry,
       "cfprVmVlanInstanceId": cfprVmVlanInstanceId,
       "cfprVmVlanDn": cfprVmVlanDn,
       "cfprVmVlanRn": cfprVmVlanRn,
       "cfprVmVlanAssocPrimaryVlanState": cfprVmVlanAssocPrimaryVlanState,
       "cfprVmVlanAssocPrimaryVlanSwitchId": cfprVmVlanAssocPrimaryVlanSwitchId,
       "cfprVmVlanEpDn": cfprVmVlanEpDn,
       "cfprVmVlanId": cfprVmVlanId,
       "cfprVmVlanIfRole": cfprVmVlanIfRole,
       "cfprVmVlanIfType": cfprVmVlanIfType,
       "cfprVmVlanLocale": cfprVmVlanLocale,
       "cfprVmVlanName": cfprVmVlanName,
       "cfprVmVlanOperState": cfprVmVlanOperState,
       "cfprVmVlanOverlapStateForA": cfprVmVlanOverlapStateForA,
       "cfprVmVlanOverlapStateForB": cfprVmVlanOverlapStateForB,
       "cfprVmVlanPeerDn": cfprVmVlanPeerDn,
       "cfprVmVlanPolicyOwner": cfprVmVlanPolicyOwner,
       "cfprVmVlanPubNwDn": cfprVmVlanPubNwDn,
       "cfprVmVlanPubNwId": cfprVmVlanPubNwId,
       "cfprVmVlanPubNwName": cfprVmVlanPubNwName,
       "cfprVmVlanSharing": cfprVmVlanSharing,
       "cfprVmVlanSwitchId": cfprVmVlanSwitchId,
       "cfprVmVlanTransport": cfprVmVlanTransport,
       "cfprVmVlanType": cfprVmVlanType,
       "cfprVmVnicProfClTable": cfprVmVnicProfClTable,
       "cfprVmVnicProfClEntry": cfprVmVnicProfClEntry,
       "cfprVmVnicProfClInstanceId": cfprVmVnicProfClInstanceId,
       "cfprVmVnicProfClDn": cfprVmVnicProfClDn,
       "cfprVmVnicProfClRn": cfprVmVnicProfClRn,
       "cfprVmVnicProfClDcName": cfprVmVnicProfClDcName,
       "cfprVmVnicProfClDescr": cfprVmVnicProfClDescr,
       "cfprVmVnicProfClIntId": cfprVmVnicProfClIntId,
       "cfprVmVnicProfClName": cfprVmVnicProfClName,
       "cfprVmVnicProfClOrgPath": cfprVmVnicProfClOrgPath,
       "cfprVmVnicProfClPolicyLevel": cfprVmVnicProfClPolicyLevel,
       "cfprVmVnicProfClPolicyOwner": cfprVmVnicProfClPolicyOwner,
       "cfprVmVnicProfClSwName": cfprVmVnicProfClSwName,
       "cfprVmVnicProfInstTable": cfprVmVnicProfInstTable,
       "cfprVmVnicProfInstEntry": cfprVmVnicProfInstEntry,
       "cfprVmVnicProfInstInstanceId": cfprVmVnicProfInstInstanceId,
       "cfprVmVnicProfInstDn": cfprVmVnicProfInstDn,
       "cfprVmVnicProfInstRn": cfprVmVnicProfInstRn,
       "cfprVmVnicProfInstDescr": cfprVmVnicProfInstDescr,
       "cfprVmVnicProfInstIntId": cfprVmVnicProfInstIntId,
       "cfprVmVnicProfInstMaxPorts": cfprVmVnicProfInstMaxPorts,
       "cfprVmVnicProfInstName": cfprVmVnicProfInstName,
       "cfprVmVnicProfInstPolicyLevel": cfprVmVnicProfInstPolicyLevel,
       "cfprVmVnicProfInstPolicyOwner": cfprVmVnicProfInstPolicyOwner,
       "cfprVmVnicProfInstProfDn": cfprVmVnicProfInstProfDn,
       "cfprVmVnicProfInstProfileType": cfprVmVnicProfInstProfileType,
       "cfprVmVsanTable": cfprVmVsanTable,
       "cfprVmVsanEntry": cfprVmVsanEntry,
       "cfprVmVsanInstanceId": cfprVmVsanInstanceId,
       "cfprVmVsanDn": cfprVmVsanDn,
       "cfprVmVsanRn": cfprVmVsanRn,
       "cfprVmVsanEpDn": cfprVmVsanEpDn,
       "cfprVmVsanFcoeVlan": cfprVmVsanFcoeVlan,
       "cfprVmVsanId": cfprVmVsanId,
       "cfprVmVsanIfRole": cfprVmVsanIfRole,
       "cfprVmVsanIfType": cfprVmVsanIfType,
       "cfprVmVsanLocale": cfprVmVsanLocale,
       "cfprVmVsanName": cfprVmVsanName,
       "cfprVmVsanOperState": cfprVmVsanOperState,
       "cfprVmVsanPeerDn": cfprVmVsanPeerDn,
       "cfprVmVsanPolicyOwner": cfprVmVsanPolicyOwner,
       "cfprVmVsanSwitchId": cfprVmVsanSwitchId,
       "cfprVmVsanTransport": cfprVmVsanTransport,
       "cfprVmVsanType": cfprVmVsanType,
       "cfprVmVsanZoningState": cfprVmVsanZoningState}
)
