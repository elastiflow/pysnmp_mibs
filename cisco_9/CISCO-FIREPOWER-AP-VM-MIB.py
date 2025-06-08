# SNMP MIB module (CISCO-FIREPOWER-AP-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-VM-MIB.mib
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApAdaptorLinkState,
 CfprApAdaptorServiceState,
 CfprApDcxOperState,
 CfprApExtvmmOwnership,
 CfprApFabricAVlanAssocPrimaryVlanSwitchId,
 CfprApFabricAVlanSharing,
 CfprApFabricAVlanTransport,
 CfprApFabricAVlanType,
 CfprApFabricAVsanTransport,
 CfprApFabricAVsanType,
 CfprApFabricVlanAssocPrimaryVlanState,
 CfprApFabricVlanOperState,
 CfprApFabricVlanOverlapState,
 CfprApFabricVnetEpIfRole,
 CfprApFabricVnetEpLocale,
 CfprApFabricVnetEpPolicyOwner,
 CfprApFabricVsanOperState,
 CfprApFabricZoningState,
 CfprApNetworkSwitchId,
 CfprApNetworkVnetEpIfType,
 CfprApOsOsType,
 CfprApPolicyPolicyOwner,
 CfprApVmAdaptorOwner,
 CfprApVmComputeEpClInstType,
 CfprApVmHbaType,
 CfprApVmHvClInstType,
 CfprApVmHvType,
 CfprApVmInstType,
 CfprApVmMgmtPlane,
 CfprApVmNicType,
 CfprApVmOsHvVendor,
 CfprApVmStatus,
 CfprApVmSwitchAdminState,
 CfprApVmSwitchVendor,
 CfprApVnicPortProfileType) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAdaptorLinkState",
    "CfprApAdaptorServiceState",
    "CfprApDcxOperState",
    "CfprApExtvmmOwnership",
    "CfprApFabricAVlanAssocPrimaryVlanSwitchId",
    "CfprApFabricAVlanSharing",
    "CfprApFabricAVlanTransport",
    "CfprApFabricAVlanType",
    "CfprApFabricAVsanTransport",
    "CfprApFabricAVsanType",
    "CfprApFabricVlanAssocPrimaryVlanState",
    "CfprApFabricVlanOperState",
    "CfprApFabricVlanOverlapState",
    "CfprApFabricVnetEpIfRole",
    "CfprApFabricVnetEpLocale",
    "CfprApFabricVnetEpPolicyOwner",
    "CfprApFabricVsanOperState",
    "CfprApFabricZoningState",
    "CfprApNetworkSwitchId",
    "CfprApNetworkVnetEpIfType",
    "CfprApOsOsType",
    "CfprApPolicyPolicyOwner",
    "CfprApVmAdaptorOwner",
    "CfprApVmComputeEpClInstType",
    "CfprApVmHbaType",
    "CfprApVmHvClInstType",
    "CfprApVmHvType",
    "CfprApVmInstType",
    "CfprApVmMgmtPlane",
    "CfprApVmNicType",
    "CfprApVmOsHvVendor",
    "CfprApVmStatus",
    "CfprApVmSwitchAdminState",
    "CfprApVmSwitchVendor",
    "CfprApVnicPortProfileType")

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

cfprApVmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApVmComputeEpTable_Object = MibTable
cfprApVmComputeEpTable = _CfprApVmComputeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1)
)
if mibBuilder.loadTexts:
    cfprApVmComputeEpTable.setStatus("current")
_CfprApVmComputeEpEntry_Object = MibTableRow
cfprApVmComputeEpEntry = _CfprApVmComputeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1)
)
cfprApVmComputeEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmComputeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmComputeEpEntry.setStatus("current")
_CfprApVmComputeEpInstanceId_Type = CfprApManagedObjectId
_CfprApVmComputeEpInstanceId_Object = MibTableColumn
cfprApVmComputeEpInstanceId = _CfprApVmComputeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 1),
    _CfprApVmComputeEpInstanceId_Type()
)
cfprApVmComputeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmComputeEpInstanceId.setStatus("current")
_CfprApVmComputeEpDn_Type = CfprApManagedObjectDn
_CfprApVmComputeEpDn_Object = MibTableColumn
cfprApVmComputeEpDn = _CfprApVmComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 2),
    _CfprApVmComputeEpDn_Type()
)
cfprApVmComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpDn.setStatus("current")
_CfprApVmComputeEpRn_Type = SnmpAdminString
_CfprApVmComputeEpRn_Object = MibTableColumn
cfprApVmComputeEpRn = _CfprApVmComputeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 3),
    _CfprApVmComputeEpRn_Type()
)
cfprApVmComputeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpRn.setStatus("current")
_CfprApVmComputeEpClInstType_Type = CfprApVmComputeEpClInstType
_CfprApVmComputeEpClInstType_Object = MibTableColumn
cfprApVmComputeEpClInstType = _CfprApVmComputeEpClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 4),
    _CfprApVmComputeEpClInstType_Type()
)
cfprApVmComputeEpClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpClInstType.setStatus("current")
_CfprApVmComputeEpComputeEpVendor_Type = SnmpAdminString
_CfprApVmComputeEpComputeEpVendor_Object = MibTableColumn
cfprApVmComputeEpComputeEpVendor = _CfprApVmComputeEpComputeEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 5),
    _CfprApVmComputeEpComputeEpVendor_Type()
)
cfprApVmComputeEpComputeEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpComputeEpVendor.setStatus("current")
_CfprApVmComputeEpDescr_Type = SnmpAdminString
_CfprApVmComputeEpDescr_Object = MibTableColumn
cfprApVmComputeEpDescr = _CfprApVmComputeEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 6),
    _CfprApVmComputeEpDescr_Type()
)
cfprApVmComputeEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpDescr.setStatus("current")
_CfprApVmComputeEpDvsDn_Type = SnmpAdminString
_CfprApVmComputeEpDvsDn_Object = MibTableColumn
cfprApVmComputeEpDvsDn = _CfprApVmComputeEpDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 7),
    _CfprApVmComputeEpDvsDn_Type()
)
cfprApVmComputeEpDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpDvsDn.setStatus("current")
_CfprApVmComputeEpDvsName_Type = SnmpAdminString
_CfprApVmComputeEpDvsName_Object = MibTableColumn
cfprApVmComputeEpDvsName = _CfprApVmComputeEpDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 8),
    _CfprApVmComputeEpDvsName_Type()
)
cfprApVmComputeEpDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpDvsName.setStatus("current")
_CfprApVmComputeEpHostName_Type = SnmpAdminString
_CfprApVmComputeEpHostName_Object = MibTableColumn
cfprApVmComputeEpHostName = _CfprApVmComputeEpHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 9),
    _CfprApVmComputeEpHostName_Type()
)
cfprApVmComputeEpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpHostName.setStatus("current")
_CfprApVmComputeEpIntId_Type = SnmpAdminString
_CfprApVmComputeEpIntId_Object = MibTableColumn
cfprApVmComputeEpIntId = _CfprApVmComputeEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 10),
    _CfprApVmComputeEpIntId_Type()
)
cfprApVmComputeEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpIntId.setStatus("current")
_CfprApVmComputeEpLsDn_Type = SnmpAdminString
_CfprApVmComputeEpLsDn_Object = MibTableColumn
cfprApVmComputeEpLsDn = _CfprApVmComputeEpLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 11),
    _CfprApVmComputeEpLsDn_Type()
)
cfprApVmComputeEpLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpLsDn.setStatus("current")
_CfprApVmComputeEpModel_Type = CfprApOsOsType
_CfprApVmComputeEpModel_Object = MibTableColumn
cfprApVmComputeEpModel = _CfprApVmComputeEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 12),
    _CfprApVmComputeEpModel_Type()
)
cfprApVmComputeEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpModel.setStatus("current")
_CfprApVmComputeEpName_Type = SnmpAdminString
_CfprApVmComputeEpName_Object = MibTableColumn
cfprApVmComputeEpName = _CfprApVmComputeEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 13),
    _CfprApVmComputeEpName_Type()
)
cfprApVmComputeEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpName.setStatus("current")
_CfprApVmComputeEpPnDn_Type = SnmpAdminString
_CfprApVmComputeEpPnDn_Object = MibTableColumn
cfprApVmComputeEpPnDn = _CfprApVmComputeEpPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 14),
    _CfprApVmComputeEpPnDn_Type()
)
cfprApVmComputeEpPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpPnDn.setStatus("current")
_CfprApVmComputeEpPolicyLevel_Type = Gauge32
_CfprApVmComputeEpPolicyLevel_Object = MibTableColumn
cfprApVmComputeEpPolicyLevel = _CfprApVmComputeEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 15),
    _CfprApVmComputeEpPolicyLevel_Type()
)
cfprApVmComputeEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpPolicyLevel.setStatus("current")
_CfprApVmComputeEpPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmComputeEpPolicyOwner_Object = MibTableColumn
cfprApVmComputeEpPolicyOwner = _CfprApVmComputeEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 16),
    _CfprApVmComputeEpPolicyOwner_Type()
)
cfprApVmComputeEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpPolicyOwner.setStatus("current")
_CfprApVmComputeEpStatusChangeTs_Type = DateAndTime
_CfprApVmComputeEpStatusChangeTs_Object = MibTableColumn
cfprApVmComputeEpStatusChangeTs = _CfprApVmComputeEpStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 17),
    _CfprApVmComputeEpStatusChangeTs_Type()
)
cfprApVmComputeEpStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpStatusChangeTs.setStatus("current")
_CfprApVmComputeEpUuid_Type = SnmpAdminString
_CfprApVmComputeEpUuid_Object = MibTableColumn
cfprApVmComputeEpUuid = _CfprApVmComputeEpUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 18),
    _CfprApVmComputeEpUuid_Type()
)
cfprApVmComputeEpUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpUuid.setStatus("current")
_CfprApVmComputeEpVStatus_Type = CfprApVmStatus
_CfprApVmComputeEpVStatus_Object = MibTableColumn
cfprApVmComputeEpVStatus = _CfprApVmComputeEpVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 19),
    _CfprApVmComputeEpVStatus_Type()
)
cfprApVmComputeEpVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpVStatus.setStatus("current")
_CfprApVmComputeEpVendor_Type = CfprApVmOsHvVendor
_CfprApVmComputeEpVendor_Object = MibTableColumn
cfprApVmComputeEpVendor = _CfprApVmComputeEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 1, 1, 20),
    _CfprApVmComputeEpVendor_Type()
)
cfprApVmComputeEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmComputeEpVendor.setStatus("current")
_CfprApVmDCTable_Object = MibTable
cfprApVmDCTable = _CfprApVmDCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2)
)
if mibBuilder.loadTexts:
    cfprApVmDCTable.setStatus("current")
_CfprApVmDCEntry_Object = MibTableRow
cfprApVmDCEntry = _CfprApVmDCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1)
)
cfprApVmDCEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmDCInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmDCEntry.setStatus("current")
_CfprApVmDCInstanceId_Type = CfprApManagedObjectId
_CfprApVmDCInstanceId_Object = MibTableColumn
cfprApVmDCInstanceId = _CfprApVmDCInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 1),
    _CfprApVmDCInstanceId_Type()
)
cfprApVmDCInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmDCInstanceId.setStatus("current")
_CfprApVmDCDn_Type = CfprApManagedObjectDn
_CfprApVmDCDn_Object = MibTableColumn
cfprApVmDCDn = _CfprApVmDCDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 2),
    _CfprApVmDCDn_Type()
)
cfprApVmDCDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCDn.setStatus("current")
_CfprApVmDCRn_Type = SnmpAdminString
_CfprApVmDCRn_Object = MibTableColumn
cfprApVmDCRn = _CfprApVmDCRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 3),
    _CfprApVmDCRn_Type()
)
cfprApVmDCRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCRn.setStatus("current")
_CfprApVmDCDescr_Type = SnmpAdminString
_CfprApVmDCDescr_Object = MibTableColumn
cfprApVmDCDescr = _CfprApVmDCDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 4),
    _CfprApVmDCDescr_Type()
)
cfprApVmDCDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCDescr.setStatus("current")
_CfprApVmDCIntId_Type = SnmpAdminString
_CfprApVmDCIntId_Object = MibTableColumn
cfprApVmDCIntId = _CfprApVmDCIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 5),
    _CfprApVmDCIntId_Type()
)
cfprApVmDCIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCIntId.setStatus("current")
_CfprApVmDCName_Type = SnmpAdminString
_CfprApVmDCName_Object = MibTableColumn
cfprApVmDCName = _CfprApVmDCName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 6),
    _CfprApVmDCName_Type()
)
cfprApVmDCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCName.setStatus("current")
_CfprApVmDCOwn_Type = CfprApExtvmmOwnership
_CfprApVmDCOwn_Object = MibTableColumn
cfprApVmDCOwn = _CfprApVmDCOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 7),
    _CfprApVmDCOwn_Type()
)
cfprApVmDCOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOwn.setStatus("current")
_CfprApVmDCPolicyLevel_Type = Gauge32
_CfprApVmDCPolicyLevel_Object = MibTableColumn
cfprApVmDCPolicyLevel = _CfprApVmDCPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 8),
    _CfprApVmDCPolicyLevel_Type()
)
cfprApVmDCPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCPolicyLevel.setStatus("current")
_CfprApVmDCPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmDCPolicyOwner_Object = MibTableColumn
cfprApVmDCPolicyOwner = _CfprApVmDCPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 9),
    _CfprApVmDCPolicyOwner_Type()
)
cfprApVmDCPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCPolicyOwner.setStatus("current")
_CfprApVmDCUuid_Type = SnmpAdminString
_CfprApVmDCUuid_Object = MibTableColumn
cfprApVmDCUuid = _CfprApVmDCUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 2, 1, 10),
    _CfprApVmDCUuid_Type()
)
cfprApVmDCUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCUuid.setStatus("current")
_CfprApVmDCOrgTable_Object = MibTable
cfprApVmDCOrgTable = _CfprApVmDCOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3)
)
if mibBuilder.loadTexts:
    cfprApVmDCOrgTable.setStatus("current")
_CfprApVmDCOrgEntry_Object = MibTableRow
cfprApVmDCOrgEntry = _CfprApVmDCOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1)
)
cfprApVmDCOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmDCOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmDCOrgEntry.setStatus("current")
_CfprApVmDCOrgInstanceId_Type = CfprApManagedObjectId
_CfprApVmDCOrgInstanceId_Object = MibTableColumn
cfprApVmDCOrgInstanceId = _CfprApVmDCOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 1),
    _CfprApVmDCOrgInstanceId_Type()
)
cfprApVmDCOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmDCOrgInstanceId.setStatus("current")
_CfprApVmDCOrgDn_Type = CfprApManagedObjectDn
_CfprApVmDCOrgDn_Object = MibTableColumn
cfprApVmDCOrgDn = _CfprApVmDCOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 2),
    _CfprApVmDCOrgDn_Type()
)
cfprApVmDCOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgDn.setStatus("current")
_CfprApVmDCOrgRn_Type = SnmpAdminString
_CfprApVmDCOrgRn_Object = MibTableColumn
cfprApVmDCOrgRn = _CfprApVmDCOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 3),
    _CfprApVmDCOrgRn_Type()
)
cfprApVmDCOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgRn.setStatus("current")
_CfprApVmDCOrgDescr_Type = SnmpAdminString
_CfprApVmDCOrgDescr_Object = MibTableColumn
cfprApVmDCOrgDescr = _CfprApVmDCOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 4),
    _CfprApVmDCOrgDescr_Type()
)
cfprApVmDCOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgDescr.setStatus("current")
_CfprApVmDCOrgIntId_Type = SnmpAdminString
_CfprApVmDCOrgIntId_Object = MibTableColumn
cfprApVmDCOrgIntId = _CfprApVmDCOrgIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 5),
    _CfprApVmDCOrgIntId_Type()
)
cfprApVmDCOrgIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgIntId.setStatus("current")
_CfprApVmDCOrgName_Type = SnmpAdminString
_CfprApVmDCOrgName_Object = MibTableColumn
cfprApVmDCOrgName = _CfprApVmDCOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 6),
    _CfprApVmDCOrgName_Type()
)
cfprApVmDCOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgName.setStatus("current")
_CfprApVmDCOrgOwn_Type = CfprApExtvmmOwnership
_CfprApVmDCOrgOwn_Object = MibTableColumn
cfprApVmDCOrgOwn = _CfprApVmDCOrgOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 7),
    _CfprApVmDCOrgOwn_Type()
)
cfprApVmDCOrgOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgOwn.setStatus("current")
_CfprApVmDCOrgPolicyLevel_Type = Gauge32
_CfprApVmDCOrgPolicyLevel_Object = MibTableColumn
cfprApVmDCOrgPolicyLevel = _CfprApVmDCOrgPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 8),
    _CfprApVmDCOrgPolicyLevel_Type()
)
cfprApVmDCOrgPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgPolicyLevel.setStatus("current")
_CfprApVmDCOrgPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmDCOrgPolicyOwner_Object = MibTableColumn
cfprApVmDCOrgPolicyOwner = _CfprApVmDCOrgPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 9),
    _CfprApVmDCOrgPolicyOwner_Type()
)
cfprApVmDCOrgPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgPolicyOwner.setStatus("current")
_CfprApVmDCOrgUuid_Type = SnmpAdminString
_CfprApVmDCOrgUuid_Object = MibTableColumn
cfprApVmDCOrgUuid = _CfprApVmDCOrgUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 3, 1, 10),
    _CfprApVmDCOrgUuid_Type()
)
cfprApVmDCOrgUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmDCOrgUuid.setStatus("current")
_CfprApVmEpTable_Object = MibTable
cfprApVmEpTable = _CfprApVmEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 4)
)
if mibBuilder.loadTexts:
    cfprApVmEpTable.setStatus("current")
_CfprApVmEpEntry_Object = MibTableRow
cfprApVmEpEntry = _CfprApVmEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 4, 1)
)
cfprApVmEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmEpEntry.setStatus("current")
_CfprApVmEpInstanceId_Type = CfprApManagedObjectId
_CfprApVmEpInstanceId_Object = MibTableColumn
cfprApVmEpInstanceId = _CfprApVmEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 4, 1, 1),
    _CfprApVmEpInstanceId_Type()
)
cfprApVmEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmEpInstanceId.setStatus("current")
_CfprApVmEpDn_Type = CfprApManagedObjectDn
_CfprApVmEpDn_Object = MibTableColumn
cfprApVmEpDn = _CfprApVmEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 4, 1, 2),
    _CfprApVmEpDn_Type()
)
cfprApVmEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmEpDn.setStatus("current")
_CfprApVmEpRn_Type = SnmpAdminString
_CfprApVmEpRn_Object = MibTableColumn
cfprApVmEpRn = _CfprApVmEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 4, 1, 3),
    _CfprApVmEpRn_Type()
)
cfprApVmEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmEpRn.setStatus("current")
_CfprApVmHbaTable_Object = MibTable
cfprApVmHbaTable = _CfprApVmHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5)
)
if mibBuilder.loadTexts:
    cfprApVmHbaTable.setStatus("current")
_CfprApVmHbaEntry_Object = MibTableRow
cfprApVmHbaEntry = _CfprApVmHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1)
)
cfprApVmHbaEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmHbaInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmHbaEntry.setStatus("current")
_CfprApVmHbaInstanceId_Type = CfprApManagedObjectId
_CfprApVmHbaInstanceId_Object = MibTableColumn
cfprApVmHbaInstanceId = _CfprApVmHbaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 1),
    _CfprApVmHbaInstanceId_Type()
)
cfprApVmHbaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmHbaInstanceId.setStatus("current")
_CfprApVmHbaDn_Type = CfprApManagedObjectDn
_CfprApVmHbaDn_Object = MibTableColumn
cfprApVmHbaDn = _CfprApVmHbaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 2),
    _CfprApVmHbaDn_Type()
)
cfprApVmHbaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaDn.setStatus("current")
_CfprApVmHbaRn_Type = SnmpAdminString
_CfprApVmHbaRn_Object = MibTableColumn
cfprApVmHbaRn = _CfprApVmHbaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 3),
    _CfprApVmHbaRn_Type()
)
cfprApVmHbaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaRn.setStatus("current")
_CfprApVmHbaDvsGenPortId_Type = SnmpAdminString
_CfprApVmHbaDvsGenPortId_Object = MibTableColumn
cfprApVmHbaDvsGenPortId = _CfprApVmHbaDvsGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 4),
    _CfprApVmHbaDvsGenPortId_Type()
)
cfprApVmHbaDvsGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaDvsGenPortId.setStatus("current")
_CfprApVmHbaDvsPortId_Type = Gauge32
_CfprApVmHbaDvsPortId_Object = MibTableColumn
cfprApVmHbaDvsPortId = _CfprApVmHbaDvsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 5),
    _CfprApVmHbaDvsPortId_Type()
)
cfprApVmHbaDvsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaDvsPortId.setStatus("current")
_CfprApVmHbaDvsSwitchId_Type = Gauge32
_CfprApVmHbaDvsSwitchId_Object = MibTableColumn
cfprApVmHbaDvsSwitchId = _CfprApVmHbaDvsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 6),
    _CfprApVmHbaDvsSwitchId_Type()
)
cfprApVmHbaDvsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaDvsSwitchId.setStatus("current")
_CfprApVmHbaHostIfDn_Type = SnmpAdminString
_CfprApVmHbaHostIfDn_Object = MibTableColumn
cfprApVmHbaHostIfDn = _CfprApVmHbaHostIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 7),
    _CfprApVmHbaHostIfDn_Type()
)
cfprApVmHbaHostIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaHostIfDn.setStatus("current")
_CfprApVmHbaName_Type = SnmpAdminString
_CfprApVmHbaName_Object = MibTableColumn
cfprApVmHbaName = _CfprApVmHbaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 8),
    _CfprApVmHbaName_Type()
)
cfprApVmHbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaName.setStatus("current")
_CfprApVmHbaOwner_Type = CfprApVmAdaptorOwner
_CfprApVmHbaOwner_Object = MibTableColumn
cfprApVmHbaOwner = _CfprApVmHbaOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 9),
    _CfprApVmHbaOwner_Type()
)
cfprApVmHbaOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaOwner.setStatus("current")
_CfprApVmHbaPhSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmHbaPhSwitchId_Object = MibTableColumn
cfprApVmHbaPhSwitchId = _CfprApVmHbaPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 10),
    _CfprApVmHbaPhSwitchId_Type()
)
cfprApVmHbaPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaPhSwitchId.setStatus("current")
_CfprApVmHbaProfileId_Type = Gauge32
_CfprApVmHbaProfileId_Object = MibTableColumn
cfprApVmHbaProfileId = _CfprApVmHbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 11),
    _CfprApVmHbaProfileId_Type()
)
cfprApVmHbaProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaProfileId.setStatus("current")
_CfprApVmHbaProfileName_Type = SnmpAdminString
_CfprApVmHbaProfileName_Object = MibTableColumn
cfprApVmHbaProfileName = _CfprApVmHbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 12),
    _CfprApVmHbaProfileName_Type()
)
cfprApVmHbaProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaProfileName.setStatus("current")
_CfprApVmHbaStatusChangeTs_Type = DateAndTime
_CfprApVmHbaStatusChangeTs_Object = MibTableColumn
cfprApVmHbaStatusChangeTs = _CfprApVmHbaStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 13),
    _CfprApVmHbaStatusChangeTs_Type()
)
cfprApVmHbaStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaStatusChangeTs.setStatus("current")
_CfprApVmHbaSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmHbaSwitchId_Object = MibTableColumn
cfprApVmHbaSwitchId = _CfprApVmHbaSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 14),
    _CfprApVmHbaSwitchId_Type()
)
cfprApVmHbaSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaSwitchId.setStatus("current")
_CfprApVmHbaType_Type = CfprApVmHbaType
_CfprApVmHbaType_Object = MibTableColumn
cfprApVmHbaType = _CfprApVmHbaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 15),
    _CfprApVmHbaType_Type()
)
cfprApVmHbaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaType.setStatus("current")
_CfprApVmHbaUuid_Type = SnmpAdminString
_CfprApVmHbaUuid_Object = MibTableColumn
cfprApVmHbaUuid = _CfprApVmHbaUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 16),
    _CfprApVmHbaUuid_Type()
)
cfprApVmHbaUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaUuid.setStatus("current")
_CfprApVmHbaVStatus_Type = CfprApVmStatus
_CfprApVmHbaVStatus_Object = MibTableColumn
cfprApVmHbaVStatus = _CfprApVmHbaVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 17),
    _CfprApVmHbaVStatus_Type()
)
cfprApVmHbaVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaVStatus.setStatus("current")
_CfprApVmHbaVcDn_Type = SnmpAdminString
_CfprApVmHbaVcDn_Object = MibTableColumn
cfprApVmHbaVcDn = _CfprApVmHbaVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 18),
    _CfprApVmHbaVcDn_Type()
)
cfprApVmHbaVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaVcDn.setStatus("current")
_CfprApVmHbaVifId_Type = Gauge32
_CfprApVmHbaVifId_Object = MibTableColumn
cfprApVmHbaVifId = _CfprApVmHbaVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 19),
    _CfprApVmHbaVifId_Type()
)
cfprApVmHbaVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaVifId.setStatus("current")
_CfprApVmHbaVmndGuid_Type = SnmpAdminString
_CfprApVmHbaVmndGuid_Object = MibTableColumn
cfprApVmHbaVmndGuid = _CfprApVmHbaVmndGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 20),
    _CfprApVmHbaVmndGuid_Type()
)
cfprApVmHbaVmndGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaVmndGuid.setStatus("current")
_CfprApVmHbaVmndName_Type = SnmpAdminString
_CfprApVmHbaVmndName_Object = MibTableColumn
cfprApVmHbaVmndName = _CfprApVmHbaVmndName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 21),
    _CfprApVmHbaVmndName_Type()
)
cfprApVmHbaVmndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaVmndName.setStatus("current")
_CfprApVmHbaVnicDn_Type = SnmpAdminString
_CfprApVmHbaVnicDn_Object = MibTableColumn
cfprApVmHbaVnicDn = _CfprApVmHbaVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 22),
    _CfprApVmHbaVnicDn_Type()
)
cfprApVmHbaVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaVnicDn.setStatus("current")
_CfprApVmHbaWwnn_Type = Unsigned64
_CfprApVmHbaWwnn_Object = MibTableColumn
cfprApVmHbaWwnn = _CfprApVmHbaWwnn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 23),
    _CfprApVmHbaWwnn_Type()
)
cfprApVmHbaWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaWwnn.setStatus("current")
_CfprApVmHbaWwpn_Type = Unsigned64
_CfprApVmHbaWwpn_Object = MibTableColumn
cfprApVmHbaWwpn = _CfprApVmHbaWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 5, 1, 24),
    _CfprApVmHbaWwpn_Type()
)
cfprApVmHbaWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHbaWwpn.setStatus("current")
_CfprApVmHvTable_Object = MibTable
cfprApVmHvTable = _CfprApVmHvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6)
)
if mibBuilder.loadTexts:
    cfprApVmHvTable.setStatus("current")
_CfprApVmHvEntry_Object = MibTableRow
cfprApVmHvEntry = _CfprApVmHvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1)
)
cfprApVmHvEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmHvInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmHvEntry.setStatus("current")
_CfprApVmHvInstanceId_Type = CfprApManagedObjectId
_CfprApVmHvInstanceId_Object = MibTableColumn
cfprApVmHvInstanceId = _CfprApVmHvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 1),
    _CfprApVmHvInstanceId_Type()
)
cfprApVmHvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmHvInstanceId.setStatus("current")
_CfprApVmHvDn_Type = CfprApManagedObjectDn
_CfprApVmHvDn_Object = MibTableColumn
cfprApVmHvDn = _CfprApVmHvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 2),
    _CfprApVmHvDn_Type()
)
cfprApVmHvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvDn.setStatus("current")
_CfprApVmHvRn_Type = SnmpAdminString
_CfprApVmHvRn_Object = MibTableColumn
cfprApVmHvRn = _CfprApVmHvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 3),
    _CfprApVmHvRn_Type()
)
cfprApVmHvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvRn.setStatus("current")
_CfprApVmHvClInstType_Type = CfprApVmHvClInstType
_CfprApVmHvClInstType_Object = MibTableColumn
cfprApVmHvClInstType = _CfprApVmHvClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 4),
    _CfprApVmHvClInstType_Type()
)
cfprApVmHvClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvClInstType.setStatus("current")
_CfprApVmHvDescr_Type = SnmpAdminString
_CfprApVmHvDescr_Object = MibTableColumn
cfprApVmHvDescr = _CfprApVmHvDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 5),
    _CfprApVmHvDescr_Type()
)
cfprApVmHvDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvDescr.setStatus("current")
_CfprApVmHvDvsDn_Type = SnmpAdminString
_CfprApVmHvDvsDn_Object = MibTableColumn
cfprApVmHvDvsDn = _CfprApVmHvDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 6),
    _CfprApVmHvDvsDn_Type()
)
cfprApVmHvDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvDvsDn.setStatus("current")
_CfprApVmHvDvsName_Type = SnmpAdminString
_CfprApVmHvDvsName_Object = MibTableColumn
cfprApVmHvDvsName = _CfprApVmHvDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 7),
    _CfprApVmHvDvsName_Type()
)
cfprApVmHvDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvDvsName.setStatus("current")
_CfprApVmHvFltAggr_Type = Unsigned64
_CfprApVmHvFltAggr_Object = MibTableColumn
cfprApVmHvFltAggr = _CfprApVmHvFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 8),
    _CfprApVmHvFltAggr_Type()
)
cfprApVmHvFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvFltAggr.setStatus("current")
_CfprApVmHvHvType_Type = CfprApVmHvType
_CfprApVmHvHvType_Object = MibTableColumn
cfprApVmHvHvType = _CfprApVmHvHvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 9),
    _CfprApVmHvHvType_Type()
)
cfprApVmHvHvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvHvType.setStatus("current")
_CfprApVmHvIntId_Type = SnmpAdminString
_CfprApVmHvIntId_Object = MibTableColumn
cfprApVmHvIntId = _CfprApVmHvIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 10),
    _CfprApVmHvIntId_Type()
)
cfprApVmHvIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvIntId.setStatus("current")
_CfprApVmHvLsDn_Type = SnmpAdminString
_CfprApVmHvLsDn_Object = MibTableColumn
cfprApVmHvLsDn = _CfprApVmHvLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 11),
    _CfprApVmHvLsDn_Type()
)
cfprApVmHvLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvLsDn.setStatus("current")
_CfprApVmHvModel_Type = CfprApOsOsType
_CfprApVmHvModel_Object = MibTableColumn
cfprApVmHvModel = _CfprApVmHvModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 12),
    _CfprApVmHvModel_Type()
)
cfprApVmHvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvModel.setStatus("current")
_CfprApVmHvName_Type = SnmpAdminString
_CfprApVmHvName_Object = MibTableColumn
cfprApVmHvName = _CfprApVmHvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 13),
    _CfprApVmHvName_Type()
)
cfprApVmHvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvName.setStatus("current")
_CfprApVmHvPnDn_Type = SnmpAdminString
_CfprApVmHvPnDn_Object = MibTableColumn
cfprApVmHvPnDn = _CfprApVmHvPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 14),
    _CfprApVmHvPnDn_Type()
)
cfprApVmHvPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvPnDn.setStatus("current")
_CfprApVmHvPolicyLevel_Type = Gauge32
_CfprApVmHvPolicyLevel_Object = MibTableColumn
cfprApVmHvPolicyLevel = _CfprApVmHvPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 15),
    _CfprApVmHvPolicyLevel_Type()
)
cfprApVmHvPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvPolicyLevel.setStatus("current")
_CfprApVmHvPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmHvPolicyOwner_Object = MibTableColumn
cfprApVmHvPolicyOwner = _CfprApVmHvPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 16),
    _CfprApVmHvPolicyOwner_Type()
)
cfprApVmHvPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvPolicyOwner.setStatus("current")
_CfprApVmHvStatusChangeTs_Type = DateAndTime
_CfprApVmHvStatusChangeTs_Object = MibTableColumn
cfprApVmHvStatusChangeTs = _CfprApVmHvStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 17),
    _CfprApVmHvStatusChangeTs_Type()
)
cfprApVmHvStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvStatusChangeTs.setStatus("current")
_CfprApVmHvUuid_Type = SnmpAdminString
_CfprApVmHvUuid_Object = MibTableColumn
cfprApVmHvUuid = _CfprApVmHvUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 18),
    _CfprApVmHvUuid_Type()
)
cfprApVmHvUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvUuid.setStatus("current")
_CfprApVmHvVStatus_Type = CfprApVmStatus
_CfprApVmHvVStatus_Object = MibTableColumn
cfprApVmHvVStatus = _CfprApVmHvVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 19),
    _CfprApVmHvVStatus_Type()
)
cfprApVmHvVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvVStatus.setStatus("current")
_CfprApVmHvVendor_Type = CfprApVmOsHvVendor
_CfprApVmHvVendor_Object = MibTableColumn
cfprApVmHvVendor = _CfprApVmHvVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 6, 1, 20),
    _CfprApVmHvVendor_Type()
)
cfprApVmHvVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmHvVendor.setStatus("current")
_CfprApVmInstanceTable_Object = MibTable
cfprApVmInstanceTable = _CfprApVmInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7)
)
if mibBuilder.loadTexts:
    cfprApVmInstanceTable.setStatus("current")
_CfprApVmInstanceEntry_Object = MibTableRow
cfprApVmInstanceEntry = _CfprApVmInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1)
)
cfprApVmInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmInstanceEntry.setStatus("current")
_CfprApVmInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApVmInstanceInstanceId_Object = MibTableColumn
cfprApVmInstanceInstanceId = _CfprApVmInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 1),
    _CfprApVmInstanceInstanceId_Type()
)
cfprApVmInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmInstanceInstanceId.setStatus("current")
_CfprApVmInstanceDn_Type = CfprApManagedObjectDn
_CfprApVmInstanceDn_Object = MibTableColumn
cfprApVmInstanceDn = _CfprApVmInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 2),
    _CfprApVmInstanceDn_Type()
)
cfprApVmInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceDn.setStatus("current")
_CfprApVmInstanceRn_Type = SnmpAdminString
_CfprApVmInstanceRn_Object = MibTableColumn
cfprApVmInstanceRn = _CfprApVmInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 3),
    _CfprApVmInstanceRn_Type()
)
cfprApVmInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceRn.setStatus("current")
_CfprApVmInstanceClInstType_Type = CfprApVmInstType
_CfprApVmInstanceClInstType_Object = MibTableColumn
cfprApVmInstanceClInstType = _CfprApVmInstanceClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 4),
    _CfprApVmInstanceClInstType_Type()
)
cfprApVmInstanceClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceClInstType.setStatus("current")
_CfprApVmInstanceDescr_Type = SnmpAdminString
_CfprApVmInstanceDescr_Object = MibTableColumn
cfprApVmInstanceDescr = _CfprApVmInstanceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 5),
    _CfprApVmInstanceDescr_Type()
)
cfprApVmInstanceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceDescr.setStatus("current")
_CfprApVmInstanceDvsDn_Type = SnmpAdminString
_CfprApVmInstanceDvsDn_Object = MibTableColumn
cfprApVmInstanceDvsDn = _CfprApVmInstanceDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 6),
    _CfprApVmInstanceDvsDn_Type()
)
cfprApVmInstanceDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceDvsDn.setStatus("current")
_CfprApVmInstanceDvsName_Type = SnmpAdminString
_CfprApVmInstanceDvsName_Object = MibTableColumn
cfprApVmInstanceDvsName = _CfprApVmInstanceDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 7),
    _CfprApVmInstanceDvsName_Type()
)
cfprApVmInstanceDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceDvsName.setStatus("current")
_CfprApVmInstanceFltAggr_Type = Unsigned64
_CfprApVmInstanceFltAggr_Object = MibTableColumn
cfprApVmInstanceFltAggr = _CfprApVmInstanceFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 8),
    _CfprApVmInstanceFltAggr_Type()
)
cfprApVmInstanceFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceFltAggr.setStatus("current")
_CfprApVmInstanceHvDn_Type = SnmpAdminString
_CfprApVmInstanceHvDn_Object = MibTableColumn
cfprApVmInstanceHvDn = _CfprApVmInstanceHvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 9),
    _CfprApVmInstanceHvDn_Type()
)
cfprApVmInstanceHvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceHvDn.setStatus("current")
_CfprApVmInstanceHvType_Type = CfprApVmHvType
_CfprApVmInstanceHvType_Object = MibTableColumn
cfprApVmInstanceHvType = _CfprApVmInstanceHvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 10),
    _CfprApVmInstanceHvType_Type()
)
cfprApVmInstanceHvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceHvType.setStatus("current")
_CfprApVmInstanceHvUuid_Type = SnmpAdminString
_CfprApVmInstanceHvUuid_Object = MibTableColumn
cfprApVmInstanceHvUuid = _CfprApVmInstanceHvUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 11),
    _CfprApVmInstanceHvUuid_Type()
)
cfprApVmInstanceHvUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceHvUuid.setStatus("current")
_CfprApVmInstanceIntId_Type = SnmpAdminString
_CfprApVmInstanceIntId_Object = MibTableColumn
cfprApVmInstanceIntId = _CfprApVmInstanceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 12),
    _CfprApVmInstanceIntId_Type()
)
cfprApVmInstanceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceIntId.setStatus("current")
_CfprApVmInstanceLsDn_Type = SnmpAdminString
_CfprApVmInstanceLsDn_Object = MibTableColumn
cfprApVmInstanceLsDn = _CfprApVmInstanceLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 13),
    _CfprApVmInstanceLsDn_Type()
)
cfprApVmInstanceLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceLsDn.setStatus("current")
_CfprApVmInstanceModel_Type = CfprApOsOsType
_CfprApVmInstanceModel_Object = MibTableColumn
cfprApVmInstanceModel = _CfprApVmInstanceModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 14),
    _CfprApVmInstanceModel_Type()
)
cfprApVmInstanceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceModel.setStatus("current")
_CfprApVmInstanceName_Type = SnmpAdminString
_CfprApVmInstanceName_Object = MibTableColumn
cfprApVmInstanceName = _CfprApVmInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 15),
    _CfprApVmInstanceName_Type()
)
cfprApVmInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceName.setStatus("current")
_CfprApVmInstancePnDn_Type = SnmpAdminString
_CfprApVmInstancePnDn_Object = MibTableColumn
cfprApVmInstancePnDn = _CfprApVmInstancePnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 16),
    _CfprApVmInstancePnDn_Type()
)
cfprApVmInstancePnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstancePnDn.setStatus("current")
_CfprApVmInstancePolicyLevel_Type = Gauge32
_CfprApVmInstancePolicyLevel_Object = MibTableColumn
cfprApVmInstancePolicyLevel = _CfprApVmInstancePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 17),
    _CfprApVmInstancePolicyLevel_Type()
)
cfprApVmInstancePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstancePolicyLevel.setStatus("current")
_CfprApVmInstancePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmInstancePolicyOwner_Object = MibTableColumn
cfprApVmInstancePolicyOwner = _CfprApVmInstancePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 18),
    _CfprApVmInstancePolicyOwner_Type()
)
cfprApVmInstancePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstancePolicyOwner.setStatus("current")
_CfprApVmInstanceStatusChangeTs_Type = DateAndTime
_CfprApVmInstanceStatusChangeTs_Object = MibTableColumn
cfprApVmInstanceStatusChangeTs = _CfprApVmInstanceStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 19),
    _CfprApVmInstanceStatusChangeTs_Type()
)
cfprApVmInstanceStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceStatusChangeTs.setStatus("current")
_CfprApVmInstanceUuid_Type = SnmpAdminString
_CfprApVmInstanceUuid_Object = MibTableColumn
cfprApVmInstanceUuid = _CfprApVmInstanceUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 20),
    _CfprApVmInstanceUuid_Type()
)
cfprApVmInstanceUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceUuid.setStatus("current")
_CfprApVmInstanceVStatus_Type = CfprApVmStatus
_CfprApVmInstanceVStatus_Object = MibTableColumn
cfprApVmInstanceVStatus = _CfprApVmInstanceVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 21),
    _CfprApVmInstanceVStatus_Type()
)
cfprApVmInstanceVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceVStatus.setStatus("current")
_CfprApVmInstanceVendor_Type = CfprApVmOsHvVendor
_CfprApVmInstanceVendor_Object = MibTableColumn
cfprApVmInstanceVendor = _CfprApVmInstanceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 7, 1, 22),
    _CfprApVmInstanceVendor_Type()
)
cfprApVmInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmInstanceVendor.setStatus("current")
_CfprApVmLifeCyclePolicyTable_Object = MibTable
cfprApVmLifeCyclePolicyTable = _CfprApVmLifeCyclePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8)
)
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyTable.setStatus("current")
_CfprApVmLifeCyclePolicyEntry_Object = MibTableRow
cfprApVmLifeCyclePolicyEntry = _CfprApVmLifeCyclePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1)
)
cfprApVmLifeCyclePolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmLifeCyclePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyEntry.setStatus("current")
_CfprApVmLifeCyclePolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVmLifeCyclePolicyInstanceId_Object = MibTableColumn
cfprApVmLifeCyclePolicyInstanceId = _CfprApVmLifeCyclePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 1),
    _CfprApVmLifeCyclePolicyInstanceId_Type()
)
cfprApVmLifeCyclePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyInstanceId.setStatus("current")
_CfprApVmLifeCyclePolicyDn_Type = CfprApManagedObjectDn
_CfprApVmLifeCyclePolicyDn_Object = MibTableColumn
cfprApVmLifeCyclePolicyDn = _CfprApVmLifeCyclePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 2),
    _CfprApVmLifeCyclePolicyDn_Type()
)
cfprApVmLifeCyclePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyDn.setStatus("current")
_CfprApVmLifeCyclePolicyRn_Type = SnmpAdminString
_CfprApVmLifeCyclePolicyRn_Object = MibTableColumn
cfprApVmLifeCyclePolicyRn = _CfprApVmLifeCyclePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 3),
    _CfprApVmLifeCyclePolicyRn_Type()
)
cfprApVmLifeCyclePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyRn.setStatus("current")
_CfprApVmLifeCyclePolicyDescr_Type = SnmpAdminString
_CfprApVmLifeCyclePolicyDescr_Object = MibTableColumn
cfprApVmLifeCyclePolicyDescr = _CfprApVmLifeCyclePolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 4),
    _CfprApVmLifeCyclePolicyDescr_Type()
)
cfprApVmLifeCyclePolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyDescr.setStatus("current")
_CfprApVmLifeCyclePolicyIntId_Type = SnmpAdminString
_CfprApVmLifeCyclePolicyIntId_Object = MibTableColumn
cfprApVmLifeCyclePolicyIntId = _CfprApVmLifeCyclePolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 5),
    _CfprApVmLifeCyclePolicyIntId_Type()
)
cfprApVmLifeCyclePolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyIntId.setStatus("current")
_CfprApVmLifeCyclePolicyName_Type = SnmpAdminString
_CfprApVmLifeCyclePolicyName_Object = MibTableColumn
cfprApVmLifeCyclePolicyName = _CfprApVmLifeCyclePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 6),
    _CfprApVmLifeCyclePolicyName_Type()
)
cfprApVmLifeCyclePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyName.setStatus("current")
_CfprApVmLifeCyclePolicyPolicyLevel_Type = Gauge32
_CfprApVmLifeCyclePolicyPolicyLevel_Object = MibTableColumn
cfprApVmLifeCyclePolicyPolicyLevel = _CfprApVmLifeCyclePolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 7),
    _CfprApVmLifeCyclePolicyPolicyLevel_Type()
)
cfprApVmLifeCyclePolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyPolicyLevel.setStatus("current")
_CfprApVmLifeCyclePolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmLifeCyclePolicyPolicyOwner_Object = MibTableColumn
cfprApVmLifeCyclePolicyPolicyOwner = _CfprApVmLifeCyclePolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 8),
    _CfprApVmLifeCyclePolicyPolicyOwner_Type()
)
cfprApVmLifeCyclePolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyPolicyOwner.setStatus("current")
_CfprApVmLifeCyclePolicyVmRetention_Type = Gauge32
_CfprApVmLifeCyclePolicyVmRetention_Object = MibTableColumn
cfprApVmLifeCyclePolicyVmRetention = _CfprApVmLifeCyclePolicyVmRetention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 9),
    _CfprApVmLifeCyclePolicyVmRetention_Type()
)
cfprApVmLifeCyclePolicyVmRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyVmRetention.setStatus("current")
_CfprApVmLifeCyclePolicyVnicRetention_Type = Gauge32
_CfprApVmLifeCyclePolicyVnicRetention_Object = MibTableColumn
cfprApVmLifeCyclePolicyVnicRetention = _CfprApVmLifeCyclePolicyVnicRetention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 8, 1, 10),
    _CfprApVmLifeCyclePolicyVnicRetention_Type()
)
cfprApVmLifeCyclePolicyVnicRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmLifeCyclePolicyVnicRetention.setStatus("current")
_CfprApVmNicTable_Object = MibTable
cfprApVmNicTable = _CfprApVmNicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9)
)
if mibBuilder.loadTexts:
    cfprApVmNicTable.setStatus("current")
_CfprApVmNicEntry_Object = MibTableRow
cfprApVmNicEntry = _CfprApVmNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1)
)
cfprApVmNicEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmNicInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmNicEntry.setStatus("current")
_CfprApVmNicInstanceId_Type = CfprApManagedObjectId
_CfprApVmNicInstanceId_Object = MibTableColumn
cfprApVmNicInstanceId = _CfprApVmNicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 1),
    _CfprApVmNicInstanceId_Type()
)
cfprApVmNicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmNicInstanceId.setStatus("current")
_CfprApVmNicDn_Type = CfprApManagedObjectDn
_CfprApVmNicDn_Object = MibTableColumn
cfprApVmNicDn = _CfprApVmNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 2),
    _CfprApVmNicDn_Type()
)
cfprApVmNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicDn.setStatus("current")
_CfprApVmNicRn_Type = SnmpAdminString
_CfprApVmNicRn_Object = MibTableColumn
cfprApVmNicRn = _CfprApVmNicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 3),
    _CfprApVmNicRn_Type()
)
cfprApVmNicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicRn.setStatus("current")
_CfprApVmNicDvsGenPortId_Type = SnmpAdminString
_CfprApVmNicDvsGenPortId_Object = MibTableColumn
cfprApVmNicDvsGenPortId = _CfprApVmNicDvsGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 4),
    _CfprApVmNicDvsGenPortId_Type()
)
cfprApVmNicDvsGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicDvsGenPortId.setStatus("current")
_CfprApVmNicDvsPortId_Type = Gauge32
_CfprApVmNicDvsPortId_Object = MibTableColumn
cfprApVmNicDvsPortId = _CfprApVmNicDvsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 5),
    _CfprApVmNicDvsPortId_Type()
)
cfprApVmNicDvsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicDvsPortId.setStatus("current")
_CfprApVmNicDvsSwitchId_Type = Gauge32
_CfprApVmNicDvsSwitchId_Object = MibTableColumn
cfprApVmNicDvsSwitchId = _CfprApVmNicDvsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 6),
    _CfprApVmNicDvsSwitchId_Type()
)
cfprApVmNicDvsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicDvsSwitchId.setStatus("current")
_CfprApVmNicHostIfDn_Type = SnmpAdminString
_CfprApVmNicHostIfDn_Object = MibTableColumn
cfprApVmNicHostIfDn = _CfprApVmNicHostIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 7),
    _CfprApVmNicHostIfDn_Type()
)
cfprApVmNicHostIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicHostIfDn.setStatus("current")
_CfprApVmNicMacAddr_Type = MacAddress
_CfprApVmNicMacAddr_Object = MibTableColumn
cfprApVmNicMacAddr = _CfprApVmNicMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 8),
    _CfprApVmNicMacAddr_Type()
)
cfprApVmNicMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicMacAddr.setStatus("current")
_CfprApVmNicName_Type = SnmpAdminString
_CfprApVmNicName_Object = MibTableColumn
cfprApVmNicName = _CfprApVmNicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 9),
    _CfprApVmNicName_Type()
)
cfprApVmNicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicName.setStatus("current")
_CfprApVmNicOwner_Type = CfprApVmAdaptorOwner
_CfprApVmNicOwner_Object = MibTableColumn
cfprApVmNicOwner = _CfprApVmNicOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 10),
    _CfprApVmNicOwner_Type()
)
cfprApVmNicOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicOwner.setStatus("current")
_CfprApVmNicPhSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmNicPhSwitchId_Object = MibTableColumn
cfprApVmNicPhSwitchId = _CfprApVmNicPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 11),
    _CfprApVmNicPhSwitchId_Type()
)
cfprApVmNicPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicPhSwitchId.setStatus("current")
_CfprApVmNicProfileId_Type = Gauge32
_CfprApVmNicProfileId_Object = MibTableColumn
cfprApVmNicProfileId = _CfprApVmNicProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 12),
    _CfprApVmNicProfileId_Type()
)
cfprApVmNicProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicProfileId.setStatus("current")
_CfprApVmNicProfileName_Type = SnmpAdminString
_CfprApVmNicProfileName_Object = MibTableColumn
cfprApVmNicProfileName = _CfprApVmNicProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 13),
    _CfprApVmNicProfileName_Type()
)
cfprApVmNicProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicProfileName.setStatus("current")
_CfprApVmNicStatusChangeTs_Type = DateAndTime
_CfprApVmNicStatusChangeTs_Object = MibTableColumn
cfprApVmNicStatusChangeTs = _CfprApVmNicStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 14),
    _CfprApVmNicStatusChangeTs_Type()
)
cfprApVmNicStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicStatusChangeTs.setStatus("current")
_CfprApVmNicSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmNicSwitchId_Object = MibTableColumn
cfprApVmNicSwitchId = _CfprApVmNicSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 15),
    _CfprApVmNicSwitchId_Type()
)
cfprApVmNicSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicSwitchId.setStatus("current")
_CfprApVmNicType_Type = CfprApVmNicType
_CfprApVmNicType_Object = MibTableColumn
cfprApVmNicType = _CfprApVmNicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 16),
    _CfprApVmNicType_Type()
)
cfprApVmNicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicType.setStatus("current")
_CfprApVmNicUuid_Type = SnmpAdminString
_CfprApVmNicUuid_Object = MibTableColumn
cfprApVmNicUuid = _CfprApVmNicUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 17),
    _CfprApVmNicUuid_Type()
)
cfprApVmNicUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicUuid.setStatus("current")
_CfprApVmNicVStatus_Type = CfprApVmStatus
_CfprApVmNicVStatus_Object = MibTableColumn
cfprApVmNicVStatus = _CfprApVmNicVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 18),
    _CfprApVmNicVStatus_Type()
)
cfprApVmNicVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicVStatus.setStatus("current")
_CfprApVmNicVcDn_Type = SnmpAdminString
_CfprApVmNicVcDn_Object = MibTableColumn
cfprApVmNicVcDn = _CfprApVmNicVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 19),
    _CfprApVmNicVcDn_Type()
)
cfprApVmNicVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicVcDn.setStatus("current")
_CfprApVmNicVifId_Type = Gauge32
_CfprApVmNicVifId_Object = MibTableColumn
cfprApVmNicVifId = _CfprApVmNicVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 20),
    _CfprApVmNicVifId_Type()
)
cfprApVmNicVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicVifId.setStatus("current")
_CfprApVmNicVmndGuid_Type = SnmpAdminString
_CfprApVmNicVmndGuid_Object = MibTableColumn
cfprApVmNicVmndGuid = _CfprApVmNicVmndGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 21),
    _CfprApVmNicVmndGuid_Type()
)
cfprApVmNicVmndGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicVmndGuid.setStatus("current")
_CfprApVmNicVmndName_Type = SnmpAdminString
_CfprApVmNicVmndName_Object = MibTableColumn
cfprApVmNicVmndName = _CfprApVmNicVmndName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 22),
    _CfprApVmNicVmndName_Type()
)
cfprApVmNicVmndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicVmndName.setStatus("current")
_CfprApVmNicVnicDn_Type = SnmpAdminString
_CfprApVmNicVnicDn_Object = MibTableColumn
cfprApVmNicVnicDn = _CfprApVmNicVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 9, 1, 23),
    _CfprApVmNicVnicDn_Type()
)
cfprApVmNicVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmNicVnicDn.setStatus("current")
_CfprApVmOrgTable_Object = MibTable
cfprApVmOrgTable = _CfprApVmOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10)
)
if mibBuilder.loadTexts:
    cfprApVmOrgTable.setStatus("current")
_CfprApVmOrgEntry_Object = MibTableRow
cfprApVmOrgEntry = _CfprApVmOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1)
)
cfprApVmOrgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmOrgEntry.setStatus("current")
_CfprApVmOrgInstanceId_Type = CfprApManagedObjectId
_CfprApVmOrgInstanceId_Object = MibTableColumn
cfprApVmOrgInstanceId = _CfprApVmOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 1),
    _CfprApVmOrgInstanceId_Type()
)
cfprApVmOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmOrgInstanceId.setStatus("current")
_CfprApVmOrgDn_Type = CfprApManagedObjectDn
_CfprApVmOrgDn_Object = MibTableColumn
cfprApVmOrgDn = _CfprApVmOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 2),
    _CfprApVmOrgDn_Type()
)
cfprApVmOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgDn.setStatus("current")
_CfprApVmOrgRn_Type = SnmpAdminString
_CfprApVmOrgRn_Object = MibTableColumn
cfprApVmOrgRn = _CfprApVmOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 3),
    _CfprApVmOrgRn_Type()
)
cfprApVmOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgRn.setStatus("current")
_CfprApVmOrgDescr_Type = SnmpAdminString
_CfprApVmOrgDescr_Object = MibTableColumn
cfprApVmOrgDescr = _CfprApVmOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 4),
    _CfprApVmOrgDescr_Type()
)
cfprApVmOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgDescr.setStatus("current")
_CfprApVmOrgIntId_Type = SnmpAdminString
_CfprApVmOrgIntId_Object = MibTableColumn
cfprApVmOrgIntId = _CfprApVmOrgIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 5),
    _CfprApVmOrgIntId_Type()
)
cfprApVmOrgIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgIntId.setStatus("current")
_CfprApVmOrgName_Type = SnmpAdminString
_CfprApVmOrgName_Object = MibTableColumn
cfprApVmOrgName = _CfprApVmOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 6),
    _CfprApVmOrgName_Type()
)
cfprApVmOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgName.setStatus("current")
_CfprApVmOrgOwn_Type = CfprApExtvmmOwnership
_CfprApVmOrgOwn_Object = MibTableColumn
cfprApVmOrgOwn = _CfprApVmOrgOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 7),
    _CfprApVmOrgOwn_Type()
)
cfprApVmOrgOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgOwn.setStatus("current")
_CfprApVmOrgPolicyLevel_Type = Gauge32
_CfprApVmOrgPolicyLevel_Object = MibTableColumn
cfprApVmOrgPolicyLevel = _CfprApVmOrgPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 8),
    _CfprApVmOrgPolicyLevel_Type()
)
cfprApVmOrgPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgPolicyLevel.setStatus("current")
_CfprApVmOrgPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmOrgPolicyOwner_Object = MibTableColumn
cfprApVmOrgPolicyOwner = _CfprApVmOrgPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 9),
    _CfprApVmOrgPolicyOwner_Type()
)
cfprApVmOrgPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgPolicyOwner.setStatus("current")
_CfprApVmOrgUuid_Type = SnmpAdminString
_CfprApVmOrgUuid_Object = MibTableColumn
cfprApVmOrgUuid = _CfprApVmOrgUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 10, 1, 10),
    _CfprApVmOrgUuid_Type()
)
cfprApVmOrgUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmOrgUuid.setStatus("current")
_CfprApVmSwitchTable_Object = MibTable
cfprApVmSwitchTable = _CfprApVmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11)
)
if mibBuilder.loadTexts:
    cfprApVmSwitchTable.setStatus("current")
_CfprApVmSwitchEntry_Object = MibTableRow
cfprApVmSwitchEntry = _CfprApVmSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1)
)
cfprApVmSwitchEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmSwitchInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmSwitchEntry.setStatus("current")
_CfprApVmSwitchInstanceId_Type = CfprApManagedObjectId
_CfprApVmSwitchInstanceId_Object = MibTableColumn
cfprApVmSwitchInstanceId = _CfprApVmSwitchInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 1),
    _CfprApVmSwitchInstanceId_Type()
)
cfprApVmSwitchInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmSwitchInstanceId.setStatus("current")
_CfprApVmSwitchDn_Type = CfprApManagedObjectDn
_CfprApVmSwitchDn_Object = MibTableColumn
cfprApVmSwitchDn = _CfprApVmSwitchDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 2),
    _CfprApVmSwitchDn_Type()
)
cfprApVmSwitchDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchDn.setStatus("current")
_CfprApVmSwitchRn_Type = SnmpAdminString
_CfprApVmSwitchRn_Object = MibTableColumn
cfprApVmSwitchRn = _CfprApVmSwitchRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 3),
    _CfprApVmSwitchRn_Type()
)
cfprApVmSwitchRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchRn.setStatus("current")
_CfprApVmSwitchAdminState_Type = CfprApVmSwitchAdminState
_CfprApVmSwitchAdminState_Object = MibTableColumn
cfprApVmSwitchAdminState = _CfprApVmSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 4),
    _CfprApVmSwitchAdminState_Type()
)
cfprApVmSwitchAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchAdminState.setStatus("current")
_CfprApVmSwitchDescr_Type = SnmpAdminString
_CfprApVmSwitchDescr_Object = MibTableColumn
cfprApVmSwitchDescr = _CfprApVmSwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 5),
    _CfprApVmSwitchDescr_Type()
)
cfprApVmSwitchDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchDescr.setStatus("current")
_CfprApVmSwitchExtKey_Type = SnmpAdminString
_CfprApVmSwitchExtKey_Object = MibTableColumn
cfprApVmSwitchExtKey = _CfprApVmSwitchExtKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 6),
    _CfprApVmSwitchExtKey_Type()
)
cfprApVmSwitchExtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchExtKey.setStatus("current")
_CfprApVmSwitchFltAggr_Type = Unsigned64
_CfprApVmSwitchFltAggr_Object = MibTableColumn
cfprApVmSwitchFltAggr = _CfprApVmSwitchFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 7),
    _CfprApVmSwitchFltAggr_Type()
)
cfprApVmSwitchFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchFltAggr.setStatus("current")
_CfprApVmSwitchId_Type = SnmpAdminString
_CfprApVmSwitchId_Object = MibTableColumn
cfprApVmSwitchId = _CfprApVmSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 8),
    _CfprApVmSwitchId_Type()
)
cfprApVmSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchId.setStatus("current")
_CfprApVmSwitchIntId_Type = SnmpAdminString
_CfprApVmSwitchIntId_Object = MibTableColumn
cfprApVmSwitchIntId = _CfprApVmSwitchIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 9),
    _CfprApVmSwitchIntId_Type()
)
cfprApVmSwitchIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchIntId.setStatus("current")
_CfprApVmSwitchKeyInst_Type = Gauge32
_CfprApVmSwitchKeyInst_Object = MibTableColumn
cfprApVmSwitchKeyInst = _CfprApVmSwitchKeyInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 10),
    _CfprApVmSwitchKeyInst_Type()
)
cfprApVmSwitchKeyInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchKeyInst.setStatus("current")
_CfprApVmSwitchManager_Type = CfprApVmMgmtPlane
_CfprApVmSwitchManager_Object = MibTableColumn
cfprApVmSwitchManager = _CfprApVmSwitchManager_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 11),
    _CfprApVmSwitchManager_Type()
)
cfprApVmSwitchManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchManager.setStatus("current")
_CfprApVmSwitchName_Type = SnmpAdminString
_CfprApVmSwitchName_Object = MibTableColumn
cfprApVmSwitchName = _CfprApVmSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 12),
    _CfprApVmSwitchName_Type()
)
cfprApVmSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchName.setStatus("current")
_CfprApVmSwitchOwn_Type = CfprApExtvmmOwnership
_CfprApVmSwitchOwn_Object = MibTableColumn
cfprApVmSwitchOwn = _CfprApVmSwitchOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 13),
    _CfprApVmSwitchOwn_Type()
)
cfprApVmSwitchOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchOwn.setStatus("current")
_CfprApVmSwitchPolicyLevel_Type = Gauge32
_CfprApVmSwitchPolicyLevel_Object = MibTableColumn
cfprApVmSwitchPolicyLevel = _CfprApVmSwitchPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 14),
    _CfprApVmSwitchPolicyLevel_Type()
)
cfprApVmSwitchPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchPolicyLevel.setStatus("current")
_CfprApVmSwitchPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmSwitchPolicyOwner_Object = MibTableColumn
cfprApVmSwitchPolicyOwner = _CfprApVmSwitchPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 15),
    _CfprApVmSwitchPolicyOwner_Type()
)
cfprApVmSwitchPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchPolicyOwner.setStatus("current")
_CfprApVmSwitchUuid_Type = SnmpAdminString
_CfprApVmSwitchUuid_Object = MibTableColumn
cfprApVmSwitchUuid = _CfprApVmSwitchUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 16),
    _CfprApVmSwitchUuid_Type()
)
cfprApVmSwitchUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchUuid.setStatus("current")
_CfprApVmSwitchVendor_Type = CfprApVmSwitchVendor
_CfprApVmSwitchVendor_Object = MibTableColumn
cfprApVmSwitchVendor = _CfprApVmSwitchVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 11, 1, 17),
    _CfprApVmSwitchVendor_Type()
)
cfprApVmSwitchVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmSwitchVendor.setStatus("current")
_CfprApVmVifTable_Object = MibTable
cfprApVmVifTable = _CfprApVmVifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12)
)
if mibBuilder.loadTexts:
    cfprApVmVifTable.setStatus("current")
_CfprApVmVifEntry_Object = MibTableRow
cfprApVmVifEntry = _CfprApVmVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1)
)
cfprApVmVifEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmVifInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmVifEntry.setStatus("current")
_CfprApVmVifInstanceId_Type = CfprApManagedObjectId
_CfprApVmVifInstanceId_Object = MibTableColumn
cfprApVmVifInstanceId = _CfprApVmVifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 1),
    _CfprApVmVifInstanceId_Type()
)
cfprApVmVifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmVifInstanceId.setStatus("current")
_CfprApVmVifDn_Type = CfprApManagedObjectDn
_CfprApVmVifDn_Object = MibTableColumn
cfprApVmVifDn = _CfprApVmVifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 2),
    _CfprApVmVifDn_Type()
)
cfprApVmVifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifDn.setStatus("current")
_CfprApVmVifRn_Type = SnmpAdminString
_CfprApVmVifRn_Object = MibTableColumn
cfprApVmVifRn = _CfprApVmVifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 3),
    _CfprApVmVifRn_Type()
)
cfprApVmVifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifRn.setStatus("current")
_CfprApVmVifAdpVifId_Type = Gauge32
_CfprApVmVifAdpVifId_Object = MibTableColumn
cfprApVmVifAdpVifId = _CfprApVmVifAdpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 4),
    _CfprApVmVifAdpVifId_Type()
)
cfprApVmVifAdpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifAdpVifId.setStatus("current")
_CfprApVmVifCookie_Type = Gauge32
_CfprApVmVifCookie_Object = MibTableColumn
cfprApVmVifCookie = _CfprApVmVifCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 5),
    _CfprApVmVifCookie_Type()
)
cfprApVmVifCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifCookie.setStatus("current")
_CfprApVmVifLinkState_Type = CfprApAdaptorLinkState
_CfprApVmVifLinkState_Object = MibTableColumn
cfprApVmVifLinkState = _CfprApVmVifLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 6),
    _CfprApVmVifLinkState_Type()
)
cfprApVmVifLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifLinkState.setStatus("current")
_CfprApVmVifOperState_Type = CfprApDcxOperState
_CfprApVmVifOperState_Object = MibTableColumn
cfprApVmVifOperState = _CfprApVmVifOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 7),
    _CfprApVmVifOperState_Type()
)
cfprApVmVifOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifOperState.setStatus("current")
_CfprApVmVifPhSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmVifPhSwitchId_Object = MibTableColumn
cfprApVmVifPhSwitchId = _CfprApVmVifPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 8),
    _CfprApVmVifPhSwitchId_Type()
)
cfprApVmVifPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhSwitchId.setStatus("current")
_CfprApVmVifPhsAccessAggrPortId_Type = Gauge32
_CfprApVmVifPhsAccessAggrPortId_Object = MibTableColumn
cfprApVmVifPhsAccessAggrPortId = _CfprApVmVifPhsAccessAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 9),
    _CfprApVmVifPhsAccessAggrPortId_Type()
)
cfprApVmVifPhsAccessAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhsAccessAggrPortId.setStatus("current")
_CfprApVmVifPhsAccessCardId_Type = Gauge32
_CfprApVmVifPhsAccessCardId_Object = MibTableColumn
cfprApVmVifPhsAccessCardId = _CfprApVmVifPhsAccessCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 10),
    _CfprApVmVifPhsAccessCardId_Type()
)
cfprApVmVifPhsAccessCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhsAccessCardId.setStatus("current")
_CfprApVmVifPhsAccessPortId_Type = Gauge32
_CfprApVmVifPhsAccessPortId_Object = MibTableColumn
cfprApVmVifPhsAccessPortId = _CfprApVmVifPhsAccessPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 11),
    _CfprApVmVifPhsAccessPortId_Type()
)
cfprApVmVifPhsAccessPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhsAccessPortId.setStatus("current")
_CfprApVmVifPhsBorderAggrPortId_Type = Gauge32
_CfprApVmVifPhsBorderAggrPortId_Object = MibTableColumn
cfprApVmVifPhsBorderAggrPortId = _CfprApVmVifPhsBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 12),
    _CfprApVmVifPhsBorderAggrPortId_Type()
)
cfprApVmVifPhsBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhsBorderAggrPortId.setStatus("current")
_CfprApVmVifPhsBorderCardId_Type = Gauge32
_CfprApVmVifPhsBorderCardId_Object = MibTableColumn
cfprApVmVifPhsBorderCardId = _CfprApVmVifPhsBorderCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 13),
    _CfprApVmVifPhsBorderCardId_Type()
)
cfprApVmVifPhsBorderCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhsBorderCardId.setStatus("current")
_CfprApVmVifPhsBorderPortId_Type = Gauge32
_CfprApVmVifPhsBorderPortId_Object = MibTableColumn
cfprApVmVifPhsBorderPortId = _CfprApVmVifPhsBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 14),
    _CfprApVmVifPhsBorderPortId_Type()
)
cfprApVmVifPhsBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifPhsBorderPortId.setStatus("current")
_CfprApVmVifServiceState_Type = CfprApAdaptorServiceState
_CfprApVmVifServiceState_Object = MibTableColumn
cfprApVmVifServiceState = _CfprApVmVifServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 15),
    _CfprApVmVifServiceState_Type()
)
cfprApVmVifServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifServiceState.setStatus("current")
_CfprApVmVifStateQual_Type = SnmpAdminString
_CfprApVmVifStateQual_Object = MibTableColumn
cfprApVmVifStateQual = _CfprApVmVifStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 16),
    _CfprApVmVifStateQual_Type()
)
cfprApVmVifStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifStateQual.setStatus("current")
_CfprApVmVifStatusChangeTs_Type = DateAndTime
_CfprApVmVifStatusChangeTs_Object = MibTableColumn
cfprApVmVifStatusChangeTs = _CfprApVmVifStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 17),
    _CfprApVmVifStatusChangeTs_Type()
)
cfprApVmVifStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifStatusChangeTs.setStatus("current")
_CfprApVmVifVStatus_Type = CfprApVmStatus
_CfprApVmVifVStatus_Object = MibTableColumn
cfprApVmVifVStatus = _CfprApVmVifVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 18),
    _CfprApVmVifVStatus_Type()
)
cfprApVmVifVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifVStatus.setStatus("current")
_CfprApVmVifVcDn_Type = SnmpAdminString
_CfprApVmVifVcDn_Object = MibTableColumn
cfprApVmVifVcDn = _CfprApVmVifVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 19),
    _CfprApVmVifVcDn_Type()
)
cfprApVmVifVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifVcDn.setStatus("current")
_CfprApVmVifVifId_Type = Gauge32
_CfprApVmVifVifId_Object = MibTableColumn
cfprApVmVifVifId = _CfprApVmVifVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 12, 1, 20),
    _CfprApVmVifVifId_Type()
)
cfprApVmVifVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVifVifId.setStatus("current")
_CfprApVmVlanTable_Object = MibTable
cfprApVmVlanTable = _CfprApVmVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13)
)
if mibBuilder.loadTexts:
    cfprApVmVlanTable.setStatus("current")
_CfprApVmVlanEntry_Object = MibTableRow
cfprApVmVlanEntry = _CfprApVmVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1)
)
cfprApVmVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmVlanEntry.setStatus("current")
_CfprApVmVlanInstanceId_Type = CfprApManagedObjectId
_CfprApVmVlanInstanceId_Object = MibTableColumn
cfprApVmVlanInstanceId = _CfprApVmVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 1),
    _CfprApVmVlanInstanceId_Type()
)
cfprApVmVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmVlanInstanceId.setStatus("current")
_CfprApVmVlanDn_Type = CfprApManagedObjectDn
_CfprApVmVlanDn_Object = MibTableColumn
cfprApVmVlanDn = _CfprApVmVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 2),
    _CfprApVmVlanDn_Type()
)
cfprApVmVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanDn.setStatus("current")
_CfprApVmVlanRn_Type = SnmpAdminString
_CfprApVmVlanRn_Object = MibTableColumn
cfprApVmVlanRn = _CfprApVmVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 3),
    _CfprApVmVlanRn_Type()
)
cfprApVmVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanRn.setStatus("current")
_CfprApVmVlanAssocPrimaryVlanState_Type = CfprApFabricVlanAssocPrimaryVlanState
_CfprApVmVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprApVmVlanAssocPrimaryVlanState = _CfprApVmVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 4),
    _CfprApVmVlanAssocPrimaryVlanState_Type()
)
cfprApVmVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanAssocPrimaryVlanState.setStatus("current")
_CfprApVmVlanAssocPrimaryVlanSwitchId_Type = CfprApFabricAVlanAssocPrimaryVlanSwitchId
_CfprApVmVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprApVmVlanAssocPrimaryVlanSwitchId = _CfprApVmVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 5),
    _CfprApVmVlanAssocPrimaryVlanSwitchId_Type()
)
cfprApVmVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprApVmVlanEpDn_Type = SnmpAdminString
_CfprApVmVlanEpDn_Object = MibTableColumn
cfprApVmVlanEpDn = _CfprApVmVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 6),
    _CfprApVmVlanEpDn_Type()
)
cfprApVmVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanEpDn.setStatus("current")
_CfprApVmVlanId_Type = Gauge32
_CfprApVmVlanId_Object = MibTableColumn
cfprApVmVlanId = _CfprApVmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 7),
    _CfprApVmVlanId_Type()
)
cfprApVmVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanId.setStatus("current")
_CfprApVmVlanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApVmVlanIfRole_Object = MibTableColumn
cfprApVmVlanIfRole = _CfprApVmVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 8),
    _CfprApVmVlanIfRole_Type()
)
cfprApVmVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanIfRole.setStatus("current")
_CfprApVmVlanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApVmVlanIfType_Object = MibTableColumn
cfprApVmVlanIfType = _CfprApVmVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 9),
    _CfprApVmVlanIfType_Type()
)
cfprApVmVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanIfType.setStatus("current")
_CfprApVmVlanLocale_Type = CfprApFabricVnetEpLocale
_CfprApVmVlanLocale_Object = MibTableColumn
cfprApVmVlanLocale = _CfprApVmVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 10),
    _CfprApVmVlanLocale_Type()
)
cfprApVmVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanLocale.setStatus("current")
_CfprApVmVlanName_Type = SnmpAdminString
_CfprApVmVlanName_Object = MibTableColumn
cfprApVmVlanName = _CfprApVmVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 11),
    _CfprApVmVlanName_Type()
)
cfprApVmVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanName.setStatus("current")
_CfprApVmVlanOperState_Type = CfprApFabricVlanOperState
_CfprApVmVlanOperState_Object = MibTableColumn
cfprApVmVlanOperState = _CfprApVmVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 12),
    _CfprApVmVlanOperState_Type()
)
cfprApVmVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanOperState.setStatus("current")
_CfprApVmVlanOverlapStateForA_Type = CfprApFabricVlanOverlapState
_CfprApVmVlanOverlapStateForA_Object = MibTableColumn
cfprApVmVlanOverlapStateForA = _CfprApVmVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 13),
    _CfprApVmVlanOverlapStateForA_Type()
)
cfprApVmVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanOverlapStateForA.setStatus("current")
_CfprApVmVlanOverlapStateForB_Type = CfprApFabricVlanOverlapState
_CfprApVmVlanOverlapStateForB_Object = MibTableColumn
cfprApVmVlanOverlapStateForB = _CfprApVmVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 14),
    _CfprApVmVlanOverlapStateForB_Type()
)
cfprApVmVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanOverlapStateForB.setStatus("current")
_CfprApVmVlanPeerDn_Type = SnmpAdminString
_CfprApVmVlanPeerDn_Object = MibTableColumn
cfprApVmVlanPeerDn = _CfprApVmVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 15),
    _CfprApVmVlanPeerDn_Type()
)
cfprApVmVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanPeerDn.setStatus("current")
_CfprApVmVlanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApVmVlanPolicyOwner_Object = MibTableColumn
cfprApVmVlanPolicyOwner = _CfprApVmVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 16),
    _CfprApVmVlanPolicyOwner_Type()
)
cfprApVmVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanPolicyOwner.setStatus("current")
_CfprApVmVlanPubNwDn_Type = SnmpAdminString
_CfprApVmVlanPubNwDn_Object = MibTableColumn
cfprApVmVlanPubNwDn = _CfprApVmVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 17),
    _CfprApVmVlanPubNwDn_Type()
)
cfprApVmVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanPubNwDn.setStatus("current")
_CfprApVmVlanPubNwId_Type = Gauge32
_CfprApVmVlanPubNwId_Object = MibTableColumn
cfprApVmVlanPubNwId = _CfprApVmVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 18),
    _CfprApVmVlanPubNwId_Type()
)
cfprApVmVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanPubNwId.setStatus("current")
_CfprApVmVlanPubNwName_Type = SnmpAdminString
_CfprApVmVlanPubNwName_Object = MibTableColumn
cfprApVmVlanPubNwName = _CfprApVmVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 19),
    _CfprApVmVlanPubNwName_Type()
)
cfprApVmVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanPubNwName.setStatus("current")
_CfprApVmVlanSharing_Type = CfprApFabricAVlanSharing
_CfprApVmVlanSharing_Object = MibTableColumn
cfprApVmVlanSharing = _CfprApVmVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 20),
    _CfprApVmVlanSharing_Type()
)
cfprApVmVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanSharing.setStatus("current")
_CfprApVmVlanSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmVlanSwitchId_Object = MibTableColumn
cfprApVmVlanSwitchId = _CfprApVmVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 21),
    _CfprApVmVlanSwitchId_Type()
)
cfprApVmVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanSwitchId.setStatus("current")
_CfprApVmVlanTransport_Type = CfprApFabricAVlanTransport
_CfprApVmVlanTransport_Object = MibTableColumn
cfprApVmVlanTransport = _CfprApVmVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 22),
    _CfprApVmVlanTransport_Type()
)
cfprApVmVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanTransport.setStatus("current")
_CfprApVmVlanType_Type = CfprApFabricAVlanType
_CfprApVmVlanType_Object = MibTableColumn
cfprApVmVlanType = _CfprApVmVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 13, 1, 23),
    _CfprApVmVlanType_Type()
)
cfprApVmVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVlanType.setStatus("current")
_CfprApVmVnicProfClTable_Object = MibTable
cfprApVmVnicProfClTable = _CfprApVmVnicProfClTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14)
)
if mibBuilder.loadTexts:
    cfprApVmVnicProfClTable.setStatus("current")
_CfprApVmVnicProfClEntry_Object = MibTableRow
cfprApVmVnicProfClEntry = _CfprApVmVnicProfClEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1)
)
cfprApVmVnicProfClEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmVnicProfClInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmVnicProfClEntry.setStatus("current")
_CfprApVmVnicProfClInstanceId_Type = CfprApManagedObjectId
_CfprApVmVnicProfClInstanceId_Object = MibTableColumn
cfprApVmVnicProfClInstanceId = _CfprApVmVnicProfClInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 1),
    _CfprApVmVnicProfClInstanceId_Type()
)
cfprApVmVnicProfClInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClInstanceId.setStatus("current")
_CfprApVmVnicProfClDn_Type = CfprApManagedObjectDn
_CfprApVmVnicProfClDn_Object = MibTableColumn
cfprApVmVnicProfClDn = _CfprApVmVnicProfClDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 2),
    _CfprApVmVnicProfClDn_Type()
)
cfprApVmVnicProfClDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClDn.setStatus("current")
_CfprApVmVnicProfClRn_Type = SnmpAdminString
_CfprApVmVnicProfClRn_Object = MibTableColumn
cfprApVmVnicProfClRn = _CfprApVmVnicProfClRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 3),
    _CfprApVmVnicProfClRn_Type()
)
cfprApVmVnicProfClRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClRn.setStatus("current")
_CfprApVmVnicProfClDcName_Type = SnmpAdminString
_CfprApVmVnicProfClDcName_Object = MibTableColumn
cfprApVmVnicProfClDcName = _CfprApVmVnicProfClDcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 4),
    _CfprApVmVnicProfClDcName_Type()
)
cfprApVmVnicProfClDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClDcName.setStatus("current")
_CfprApVmVnicProfClDescr_Type = SnmpAdminString
_CfprApVmVnicProfClDescr_Object = MibTableColumn
cfprApVmVnicProfClDescr = _CfprApVmVnicProfClDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 5),
    _CfprApVmVnicProfClDescr_Type()
)
cfprApVmVnicProfClDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClDescr.setStatus("current")
_CfprApVmVnicProfClIntId_Type = SnmpAdminString
_CfprApVmVnicProfClIntId_Object = MibTableColumn
cfprApVmVnicProfClIntId = _CfprApVmVnicProfClIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 6),
    _CfprApVmVnicProfClIntId_Type()
)
cfprApVmVnicProfClIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClIntId.setStatus("current")
_CfprApVmVnicProfClName_Type = SnmpAdminString
_CfprApVmVnicProfClName_Object = MibTableColumn
cfprApVmVnicProfClName = _CfprApVmVnicProfClName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 7),
    _CfprApVmVnicProfClName_Type()
)
cfprApVmVnicProfClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClName.setStatus("current")
_CfprApVmVnicProfClOrgPath_Type = SnmpAdminString
_CfprApVmVnicProfClOrgPath_Object = MibTableColumn
cfprApVmVnicProfClOrgPath = _CfprApVmVnicProfClOrgPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 8),
    _CfprApVmVnicProfClOrgPath_Type()
)
cfprApVmVnicProfClOrgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClOrgPath.setStatus("current")
_CfprApVmVnicProfClPolicyLevel_Type = Gauge32
_CfprApVmVnicProfClPolicyLevel_Object = MibTableColumn
cfprApVmVnicProfClPolicyLevel = _CfprApVmVnicProfClPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 9),
    _CfprApVmVnicProfClPolicyLevel_Type()
)
cfprApVmVnicProfClPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClPolicyLevel.setStatus("current")
_CfprApVmVnicProfClPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmVnicProfClPolicyOwner_Object = MibTableColumn
cfprApVmVnicProfClPolicyOwner = _CfprApVmVnicProfClPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 10),
    _CfprApVmVnicProfClPolicyOwner_Type()
)
cfprApVmVnicProfClPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClPolicyOwner.setStatus("current")
_CfprApVmVnicProfClSwName_Type = SnmpAdminString
_CfprApVmVnicProfClSwName_Object = MibTableColumn
cfprApVmVnicProfClSwName = _CfprApVmVnicProfClSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 14, 1, 11),
    _CfprApVmVnicProfClSwName_Type()
)
cfprApVmVnicProfClSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfClSwName.setStatus("current")
_CfprApVmVnicProfInstTable_Object = MibTable
cfprApVmVnicProfInstTable = _CfprApVmVnicProfInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15)
)
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstTable.setStatus("current")
_CfprApVmVnicProfInstEntry_Object = MibTableRow
cfprApVmVnicProfInstEntry = _CfprApVmVnicProfInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1)
)
cfprApVmVnicProfInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmVnicProfInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstEntry.setStatus("current")
_CfprApVmVnicProfInstInstanceId_Type = CfprApManagedObjectId
_CfprApVmVnicProfInstInstanceId_Object = MibTableColumn
cfprApVmVnicProfInstInstanceId = _CfprApVmVnicProfInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 1),
    _CfprApVmVnicProfInstInstanceId_Type()
)
cfprApVmVnicProfInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstInstanceId.setStatus("current")
_CfprApVmVnicProfInstDn_Type = CfprApManagedObjectDn
_CfprApVmVnicProfInstDn_Object = MibTableColumn
cfprApVmVnicProfInstDn = _CfprApVmVnicProfInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 2),
    _CfprApVmVnicProfInstDn_Type()
)
cfprApVmVnicProfInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstDn.setStatus("current")
_CfprApVmVnicProfInstRn_Type = SnmpAdminString
_CfprApVmVnicProfInstRn_Object = MibTableColumn
cfprApVmVnicProfInstRn = _CfprApVmVnicProfInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 3),
    _CfprApVmVnicProfInstRn_Type()
)
cfprApVmVnicProfInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstRn.setStatus("current")
_CfprApVmVnicProfInstDescr_Type = SnmpAdminString
_CfprApVmVnicProfInstDescr_Object = MibTableColumn
cfprApVmVnicProfInstDescr = _CfprApVmVnicProfInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 4),
    _CfprApVmVnicProfInstDescr_Type()
)
cfprApVmVnicProfInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstDescr.setStatus("current")
_CfprApVmVnicProfInstIntId_Type = SnmpAdminString
_CfprApVmVnicProfInstIntId_Object = MibTableColumn
cfprApVmVnicProfInstIntId = _CfprApVmVnicProfInstIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 5),
    _CfprApVmVnicProfInstIntId_Type()
)
cfprApVmVnicProfInstIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstIntId.setStatus("current")
_CfprApVmVnicProfInstMaxPorts_Type = Gauge32
_CfprApVmVnicProfInstMaxPorts_Object = MibTableColumn
cfprApVmVnicProfInstMaxPorts = _CfprApVmVnicProfInstMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 6),
    _CfprApVmVnicProfInstMaxPorts_Type()
)
cfprApVmVnicProfInstMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstMaxPorts.setStatus("current")
_CfprApVmVnicProfInstName_Type = SnmpAdminString
_CfprApVmVnicProfInstName_Object = MibTableColumn
cfprApVmVnicProfInstName = _CfprApVmVnicProfInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 7),
    _CfprApVmVnicProfInstName_Type()
)
cfprApVmVnicProfInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstName.setStatus("current")
_CfprApVmVnicProfInstPolicyLevel_Type = Gauge32
_CfprApVmVnicProfInstPolicyLevel_Object = MibTableColumn
cfprApVmVnicProfInstPolicyLevel = _CfprApVmVnicProfInstPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 8),
    _CfprApVmVnicProfInstPolicyLevel_Type()
)
cfprApVmVnicProfInstPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstPolicyLevel.setStatus("current")
_CfprApVmVnicProfInstPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVmVnicProfInstPolicyOwner_Object = MibTableColumn
cfprApVmVnicProfInstPolicyOwner = _CfprApVmVnicProfInstPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 9),
    _CfprApVmVnicProfInstPolicyOwner_Type()
)
cfprApVmVnicProfInstPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstPolicyOwner.setStatus("current")
_CfprApVmVnicProfInstProfDn_Type = SnmpAdminString
_CfprApVmVnicProfInstProfDn_Object = MibTableColumn
cfprApVmVnicProfInstProfDn = _CfprApVmVnicProfInstProfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 10),
    _CfprApVmVnicProfInstProfDn_Type()
)
cfprApVmVnicProfInstProfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstProfDn.setStatus("current")
_CfprApVmVnicProfInstProfileType_Type = CfprApVnicPortProfileType
_CfprApVmVnicProfInstProfileType_Object = MibTableColumn
cfprApVmVnicProfInstProfileType = _CfprApVmVnicProfInstProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 15, 1, 11),
    _CfprApVmVnicProfInstProfileType_Type()
)
cfprApVmVnicProfInstProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVnicProfInstProfileType.setStatus("current")
_CfprApVmVsanTable_Object = MibTable
cfprApVmVsanTable = _CfprApVmVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16)
)
if mibBuilder.loadTexts:
    cfprApVmVsanTable.setStatus("current")
_CfprApVmVsanEntry_Object = MibTableRow
cfprApVmVsanEntry = _CfprApVmVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1)
)
cfprApVmVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VM-MIB", "cfprApVmVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVmVsanEntry.setStatus("current")
_CfprApVmVsanInstanceId_Type = CfprApManagedObjectId
_CfprApVmVsanInstanceId_Object = MibTableColumn
cfprApVmVsanInstanceId = _CfprApVmVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 1),
    _CfprApVmVsanInstanceId_Type()
)
cfprApVmVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVmVsanInstanceId.setStatus("current")
_CfprApVmVsanDn_Type = CfprApManagedObjectDn
_CfprApVmVsanDn_Object = MibTableColumn
cfprApVmVsanDn = _CfprApVmVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 2),
    _CfprApVmVsanDn_Type()
)
cfprApVmVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanDn.setStatus("current")
_CfprApVmVsanRn_Type = SnmpAdminString
_CfprApVmVsanRn_Object = MibTableColumn
cfprApVmVsanRn = _CfprApVmVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 3),
    _CfprApVmVsanRn_Type()
)
cfprApVmVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanRn.setStatus("current")
_CfprApVmVsanEpDn_Type = SnmpAdminString
_CfprApVmVsanEpDn_Object = MibTableColumn
cfprApVmVsanEpDn = _CfprApVmVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 4),
    _CfprApVmVsanEpDn_Type()
)
cfprApVmVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanEpDn.setStatus("current")
_CfprApVmVsanFcoeVlan_Type = Gauge32
_CfprApVmVsanFcoeVlan_Object = MibTableColumn
cfprApVmVsanFcoeVlan = _CfprApVmVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 5),
    _CfprApVmVsanFcoeVlan_Type()
)
cfprApVmVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanFcoeVlan.setStatus("current")
_CfprApVmVsanId_Type = Gauge32
_CfprApVmVsanId_Object = MibTableColumn
cfprApVmVsanId = _CfprApVmVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 6),
    _CfprApVmVsanId_Type()
)
cfprApVmVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanId.setStatus("current")
_CfprApVmVsanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApVmVsanIfRole_Object = MibTableColumn
cfprApVmVsanIfRole = _CfprApVmVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 7),
    _CfprApVmVsanIfRole_Type()
)
cfprApVmVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanIfRole.setStatus("current")
_CfprApVmVsanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApVmVsanIfType_Object = MibTableColumn
cfprApVmVsanIfType = _CfprApVmVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 8),
    _CfprApVmVsanIfType_Type()
)
cfprApVmVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanIfType.setStatus("current")
_CfprApVmVsanLocale_Type = CfprApFabricVnetEpLocale
_CfprApVmVsanLocale_Object = MibTableColumn
cfprApVmVsanLocale = _CfprApVmVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 9),
    _CfprApVmVsanLocale_Type()
)
cfprApVmVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanLocale.setStatus("current")
_CfprApVmVsanName_Type = SnmpAdminString
_CfprApVmVsanName_Object = MibTableColumn
cfprApVmVsanName = _CfprApVmVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 10),
    _CfprApVmVsanName_Type()
)
cfprApVmVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanName.setStatus("current")
_CfprApVmVsanOperState_Type = CfprApFabricVsanOperState
_CfprApVmVsanOperState_Object = MibTableColumn
cfprApVmVsanOperState = _CfprApVmVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 11),
    _CfprApVmVsanOperState_Type()
)
cfprApVmVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanOperState.setStatus("current")
_CfprApVmVsanPeerDn_Type = SnmpAdminString
_CfprApVmVsanPeerDn_Object = MibTableColumn
cfprApVmVsanPeerDn = _CfprApVmVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 12),
    _CfprApVmVsanPeerDn_Type()
)
cfprApVmVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanPeerDn.setStatus("current")
_CfprApVmVsanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApVmVsanPolicyOwner_Object = MibTableColumn
cfprApVmVsanPolicyOwner = _CfprApVmVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 13),
    _CfprApVmVsanPolicyOwner_Type()
)
cfprApVmVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanPolicyOwner.setStatus("current")
_CfprApVmVsanSwitchId_Type = CfprApNetworkSwitchId
_CfprApVmVsanSwitchId_Object = MibTableColumn
cfprApVmVsanSwitchId = _CfprApVmVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 14),
    _CfprApVmVsanSwitchId_Type()
)
cfprApVmVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanSwitchId.setStatus("current")
_CfprApVmVsanTransport_Type = CfprApFabricAVsanTransport
_CfprApVmVsanTransport_Object = MibTableColumn
cfprApVmVsanTransport = _CfprApVmVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 15),
    _CfprApVmVsanTransport_Type()
)
cfprApVmVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanTransport.setStatus("current")
_CfprApVmVsanType_Type = CfprApFabricAVsanType
_CfprApVmVsanType_Object = MibTableColumn
cfprApVmVsanType = _CfprApVmVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 16),
    _CfprApVmVsanType_Type()
)
cfprApVmVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanType.setStatus("current")
_CfprApVmVsanZoningState_Type = CfprApFabricZoningState
_CfprApVmVsanZoningState_Object = MibTableColumn
cfprApVmVsanZoningState = _CfprApVmVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 82, 16, 1, 17),
    _CfprApVmVsanZoningState_Type()
)
cfprApVmVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVmVsanZoningState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-VM-MIB",
    **{"cfprApVmObjects": cfprApVmObjects,
       "cfprApVmComputeEpTable": cfprApVmComputeEpTable,
       "cfprApVmComputeEpEntry": cfprApVmComputeEpEntry,
       "cfprApVmComputeEpInstanceId": cfprApVmComputeEpInstanceId,
       "cfprApVmComputeEpDn": cfprApVmComputeEpDn,
       "cfprApVmComputeEpRn": cfprApVmComputeEpRn,
       "cfprApVmComputeEpClInstType": cfprApVmComputeEpClInstType,
       "cfprApVmComputeEpComputeEpVendor": cfprApVmComputeEpComputeEpVendor,
       "cfprApVmComputeEpDescr": cfprApVmComputeEpDescr,
       "cfprApVmComputeEpDvsDn": cfprApVmComputeEpDvsDn,
       "cfprApVmComputeEpDvsName": cfprApVmComputeEpDvsName,
       "cfprApVmComputeEpHostName": cfprApVmComputeEpHostName,
       "cfprApVmComputeEpIntId": cfprApVmComputeEpIntId,
       "cfprApVmComputeEpLsDn": cfprApVmComputeEpLsDn,
       "cfprApVmComputeEpModel": cfprApVmComputeEpModel,
       "cfprApVmComputeEpName": cfprApVmComputeEpName,
       "cfprApVmComputeEpPnDn": cfprApVmComputeEpPnDn,
       "cfprApVmComputeEpPolicyLevel": cfprApVmComputeEpPolicyLevel,
       "cfprApVmComputeEpPolicyOwner": cfprApVmComputeEpPolicyOwner,
       "cfprApVmComputeEpStatusChangeTs": cfprApVmComputeEpStatusChangeTs,
       "cfprApVmComputeEpUuid": cfprApVmComputeEpUuid,
       "cfprApVmComputeEpVStatus": cfprApVmComputeEpVStatus,
       "cfprApVmComputeEpVendor": cfprApVmComputeEpVendor,
       "cfprApVmDCTable": cfprApVmDCTable,
       "cfprApVmDCEntry": cfprApVmDCEntry,
       "cfprApVmDCInstanceId": cfprApVmDCInstanceId,
       "cfprApVmDCDn": cfprApVmDCDn,
       "cfprApVmDCRn": cfprApVmDCRn,
       "cfprApVmDCDescr": cfprApVmDCDescr,
       "cfprApVmDCIntId": cfprApVmDCIntId,
       "cfprApVmDCName": cfprApVmDCName,
       "cfprApVmDCOwn": cfprApVmDCOwn,
       "cfprApVmDCPolicyLevel": cfprApVmDCPolicyLevel,
       "cfprApVmDCPolicyOwner": cfprApVmDCPolicyOwner,
       "cfprApVmDCUuid": cfprApVmDCUuid,
       "cfprApVmDCOrgTable": cfprApVmDCOrgTable,
       "cfprApVmDCOrgEntry": cfprApVmDCOrgEntry,
       "cfprApVmDCOrgInstanceId": cfprApVmDCOrgInstanceId,
       "cfprApVmDCOrgDn": cfprApVmDCOrgDn,
       "cfprApVmDCOrgRn": cfprApVmDCOrgRn,
       "cfprApVmDCOrgDescr": cfprApVmDCOrgDescr,
       "cfprApVmDCOrgIntId": cfprApVmDCOrgIntId,
       "cfprApVmDCOrgName": cfprApVmDCOrgName,
       "cfprApVmDCOrgOwn": cfprApVmDCOrgOwn,
       "cfprApVmDCOrgPolicyLevel": cfprApVmDCOrgPolicyLevel,
       "cfprApVmDCOrgPolicyOwner": cfprApVmDCOrgPolicyOwner,
       "cfprApVmDCOrgUuid": cfprApVmDCOrgUuid,
       "cfprApVmEpTable": cfprApVmEpTable,
       "cfprApVmEpEntry": cfprApVmEpEntry,
       "cfprApVmEpInstanceId": cfprApVmEpInstanceId,
       "cfprApVmEpDn": cfprApVmEpDn,
       "cfprApVmEpRn": cfprApVmEpRn,
       "cfprApVmHbaTable": cfprApVmHbaTable,
       "cfprApVmHbaEntry": cfprApVmHbaEntry,
       "cfprApVmHbaInstanceId": cfprApVmHbaInstanceId,
       "cfprApVmHbaDn": cfprApVmHbaDn,
       "cfprApVmHbaRn": cfprApVmHbaRn,
       "cfprApVmHbaDvsGenPortId": cfprApVmHbaDvsGenPortId,
       "cfprApVmHbaDvsPortId": cfprApVmHbaDvsPortId,
       "cfprApVmHbaDvsSwitchId": cfprApVmHbaDvsSwitchId,
       "cfprApVmHbaHostIfDn": cfprApVmHbaHostIfDn,
       "cfprApVmHbaName": cfprApVmHbaName,
       "cfprApVmHbaOwner": cfprApVmHbaOwner,
       "cfprApVmHbaPhSwitchId": cfprApVmHbaPhSwitchId,
       "cfprApVmHbaProfileId": cfprApVmHbaProfileId,
       "cfprApVmHbaProfileName": cfprApVmHbaProfileName,
       "cfprApVmHbaStatusChangeTs": cfprApVmHbaStatusChangeTs,
       "cfprApVmHbaSwitchId": cfprApVmHbaSwitchId,
       "cfprApVmHbaType": cfprApVmHbaType,
       "cfprApVmHbaUuid": cfprApVmHbaUuid,
       "cfprApVmHbaVStatus": cfprApVmHbaVStatus,
       "cfprApVmHbaVcDn": cfprApVmHbaVcDn,
       "cfprApVmHbaVifId": cfprApVmHbaVifId,
       "cfprApVmHbaVmndGuid": cfprApVmHbaVmndGuid,
       "cfprApVmHbaVmndName": cfprApVmHbaVmndName,
       "cfprApVmHbaVnicDn": cfprApVmHbaVnicDn,
       "cfprApVmHbaWwnn": cfprApVmHbaWwnn,
       "cfprApVmHbaWwpn": cfprApVmHbaWwpn,
       "cfprApVmHvTable": cfprApVmHvTable,
       "cfprApVmHvEntry": cfprApVmHvEntry,
       "cfprApVmHvInstanceId": cfprApVmHvInstanceId,
       "cfprApVmHvDn": cfprApVmHvDn,
       "cfprApVmHvRn": cfprApVmHvRn,
       "cfprApVmHvClInstType": cfprApVmHvClInstType,
       "cfprApVmHvDescr": cfprApVmHvDescr,
       "cfprApVmHvDvsDn": cfprApVmHvDvsDn,
       "cfprApVmHvDvsName": cfprApVmHvDvsName,
       "cfprApVmHvFltAggr": cfprApVmHvFltAggr,
       "cfprApVmHvHvType": cfprApVmHvHvType,
       "cfprApVmHvIntId": cfprApVmHvIntId,
       "cfprApVmHvLsDn": cfprApVmHvLsDn,
       "cfprApVmHvModel": cfprApVmHvModel,
       "cfprApVmHvName": cfprApVmHvName,
       "cfprApVmHvPnDn": cfprApVmHvPnDn,
       "cfprApVmHvPolicyLevel": cfprApVmHvPolicyLevel,
       "cfprApVmHvPolicyOwner": cfprApVmHvPolicyOwner,
       "cfprApVmHvStatusChangeTs": cfprApVmHvStatusChangeTs,
       "cfprApVmHvUuid": cfprApVmHvUuid,
       "cfprApVmHvVStatus": cfprApVmHvVStatus,
       "cfprApVmHvVendor": cfprApVmHvVendor,
       "cfprApVmInstanceTable": cfprApVmInstanceTable,
       "cfprApVmInstanceEntry": cfprApVmInstanceEntry,
       "cfprApVmInstanceInstanceId": cfprApVmInstanceInstanceId,
       "cfprApVmInstanceDn": cfprApVmInstanceDn,
       "cfprApVmInstanceRn": cfprApVmInstanceRn,
       "cfprApVmInstanceClInstType": cfprApVmInstanceClInstType,
       "cfprApVmInstanceDescr": cfprApVmInstanceDescr,
       "cfprApVmInstanceDvsDn": cfprApVmInstanceDvsDn,
       "cfprApVmInstanceDvsName": cfprApVmInstanceDvsName,
       "cfprApVmInstanceFltAggr": cfprApVmInstanceFltAggr,
       "cfprApVmInstanceHvDn": cfprApVmInstanceHvDn,
       "cfprApVmInstanceHvType": cfprApVmInstanceHvType,
       "cfprApVmInstanceHvUuid": cfprApVmInstanceHvUuid,
       "cfprApVmInstanceIntId": cfprApVmInstanceIntId,
       "cfprApVmInstanceLsDn": cfprApVmInstanceLsDn,
       "cfprApVmInstanceModel": cfprApVmInstanceModel,
       "cfprApVmInstanceName": cfprApVmInstanceName,
       "cfprApVmInstancePnDn": cfprApVmInstancePnDn,
       "cfprApVmInstancePolicyLevel": cfprApVmInstancePolicyLevel,
       "cfprApVmInstancePolicyOwner": cfprApVmInstancePolicyOwner,
       "cfprApVmInstanceStatusChangeTs": cfprApVmInstanceStatusChangeTs,
       "cfprApVmInstanceUuid": cfprApVmInstanceUuid,
       "cfprApVmInstanceVStatus": cfprApVmInstanceVStatus,
       "cfprApVmInstanceVendor": cfprApVmInstanceVendor,
       "cfprApVmLifeCyclePolicyTable": cfprApVmLifeCyclePolicyTable,
       "cfprApVmLifeCyclePolicyEntry": cfprApVmLifeCyclePolicyEntry,
       "cfprApVmLifeCyclePolicyInstanceId": cfprApVmLifeCyclePolicyInstanceId,
       "cfprApVmLifeCyclePolicyDn": cfprApVmLifeCyclePolicyDn,
       "cfprApVmLifeCyclePolicyRn": cfprApVmLifeCyclePolicyRn,
       "cfprApVmLifeCyclePolicyDescr": cfprApVmLifeCyclePolicyDescr,
       "cfprApVmLifeCyclePolicyIntId": cfprApVmLifeCyclePolicyIntId,
       "cfprApVmLifeCyclePolicyName": cfprApVmLifeCyclePolicyName,
       "cfprApVmLifeCyclePolicyPolicyLevel": cfprApVmLifeCyclePolicyPolicyLevel,
       "cfprApVmLifeCyclePolicyPolicyOwner": cfprApVmLifeCyclePolicyPolicyOwner,
       "cfprApVmLifeCyclePolicyVmRetention": cfprApVmLifeCyclePolicyVmRetention,
       "cfprApVmLifeCyclePolicyVnicRetention": cfprApVmLifeCyclePolicyVnicRetention,
       "cfprApVmNicTable": cfprApVmNicTable,
       "cfprApVmNicEntry": cfprApVmNicEntry,
       "cfprApVmNicInstanceId": cfprApVmNicInstanceId,
       "cfprApVmNicDn": cfprApVmNicDn,
       "cfprApVmNicRn": cfprApVmNicRn,
       "cfprApVmNicDvsGenPortId": cfprApVmNicDvsGenPortId,
       "cfprApVmNicDvsPortId": cfprApVmNicDvsPortId,
       "cfprApVmNicDvsSwitchId": cfprApVmNicDvsSwitchId,
       "cfprApVmNicHostIfDn": cfprApVmNicHostIfDn,
       "cfprApVmNicMacAddr": cfprApVmNicMacAddr,
       "cfprApVmNicName": cfprApVmNicName,
       "cfprApVmNicOwner": cfprApVmNicOwner,
       "cfprApVmNicPhSwitchId": cfprApVmNicPhSwitchId,
       "cfprApVmNicProfileId": cfprApVmNicProfileId,
       "cfprApVmNicProfileName": cfprApVmNicProfileName,
       "cfprApVmNicStatusChangeTs": cfprApVmNicStatusChangeTs,
       "cfprApVmNicSwitchId": cfprApVmNicSwitchId,
       "cfprApVmNicType": cfprApVmNicType,
       "cfprApVmNicUuid": cfprApVmNicUuid,
       "cfprApVmNicVStatus": cfprApVmNicVStatus,
       "cfprApVmNicVcDn": cfprApVmNicVcDn,
       "cfprApVmNicVifId": cfprApVmNicVifId,
       "cfprApVmNicVmndGuid": cfprApVmNicVmndGuid,
       "cfprApVmNicVmndName": cfprApVmNicVmndName,
       "cfprApVmNicVnicDn": cfprApVmNicVnicDn,
       "cfprApVmOrgTable": cfprApVmOrgTable,
       "cfprApVmOrgEntry": cfprApVmOrgEntry,
       "cfprApVmOrgInstanceId": cfprApVmOrgInstanceId,
       "cfprApVmOrgDn": cfprApVmOrgDn,
       "cfprApVmOrgRn": cfprApVmOrgRn,
       "cfprApVmOrgDescr": cfprApVmOrgDescr,
       "cfprApVmOrgIntId": cfprApVmOrgIntId,
       "cfprApVmOrgName": cfprApVmOrgName,
       "cfprApVmOrgOwn": cfprApVmOrgOwn,
       "cfprApVmOrgPolicyLevel": cfprApVmOrgPolicyLevel,
       "cfprApVmOrgPolicyOwner": cfprApVmOrgPolicyOwner,
       "cfprApVmOrgUuid": cfprApVmOrgUuid,
       "cfprApVmSwitchTable": cfprApVmSwitchTable,
       "cfprApVmSwitchEntry": cfprApVmSwitchEntry,
       "cfprApVmSwitchInstanceId": cfprApVmSwitchInstanceId,
       "cfprApVmSwitchDn": cfprApVmSwitchDn,
       "cfprApVmSwitchRn": cfprApVmSwitchRn,
       "cfprApVmSwitchAdminState": cfprApVmSwitchAdminState,
       "cfprApVmSwitchDescr": cfprApVmSwitchDescr,
       "cfprApVmSwitchExtKey": cfprApVmSwitchExtKey,
       "cfprApVmSwitchFltAggr": cfprApVmSwitchFltAggr,
       "cfprApVmSwitchId": cfprApVmSwitchId,
       "cfprApVmSwitchIntId": cfprApVmSwitchIntId,
       "cfprApVmSwitchKeyInst": cfprApVmSwitchKeyInst,
       "cfprApVmSwitchManager": cfprApVmSwitchManager,
       "cfprApVmSwitchName": cfprApVmSwitchName,
       "cfprApVmSwitchOwn": cfprApVmSwitchOwn,
       "cfprApVmSwitchPolicyLevel": cfprApVmSwitchPolicyLevel,
       "cfprApVmSwitchPolicyOwner": cfprApVmSwitchPolicyOwner,
       "cfprApVmSwitchUuid": cfprApVmSwitchUuid,
       "cfprApVmSwitchVendor": cfprApVmSwitchVendor,
       "cfprApVmVifTable": cfprApVmVifTable,
       "cfprApVmVifEntry": cfprApVmVifEntry,
       "cfprApVmVifInstanceId": cfprApVmVifInstanceId,
       "cfprApVmVifDn": cfprApVmVifDn,
       "cfprApVmVifRn": cfprApVmVifRn,
       "cfprApVmVifAdpVifId": cfprApVmVifAdpVifId,
       "cfprApVmVifCookie": cfprApVmVifCookie,
       "cfprApVmVifLinkState": cfprApVmVifLinkState,
       "cfprApVmVifOperState": cfprApVmVifOperState,
       "cfprApVmVifPhSwitchId": cfprApVmVifPhSwitchId,
       "cfprApVmVifPhsAccessAggrPortId": cfprApVmVifPhsAccessAggrPortId,
       "cfprApVmVifPhsAccessCardId": cfprApVmVifPhsAccessCardId,
       "cfprApVmVifPhsAccessPortId": cfprApVmVifPhsAccessPortId,
       "cfprApVmVifPhsBorderAggrPortId": cfprApVmVifPhsBorderAggrPortId,
       "cfprApVmVifPhsBorderCardId": cfprApVmVifPhsBorderCardId,
       "cfprApVmVifPhsBorderPortId": cfprApVmVifPhsBorderPortId,
       "cfprApVmVifServiceState": cfprApVmVifServiceState,
       "cfprApVmVifStateQual": cfprApVmVifStateQual,
       "cfprApVmVifStatusChangeTs": cfprApVmVifStatusChangeTs,
       "cfprApVmVifVStatus": cfprApVmVifVStatus,
       "cfprApVmVifVcDn": cfprApVmVifVcDn,
       "cfprApVmVifVifId": cfprApVmVifVifId,
       "cfprApVmVlanTable": cfprApVmVlanTable,
       "cfprApVmVlanEntry": cfprApVmVlanEntry,
       "cfprApVmVlanInstanceId": cfprApVmVlanInstanceId,
       "cfprApVmVlanDn": cfprApVmVlanDn,
       "cfprApVmVlanRn": cfprApVmVlanRn,
       "cfprApVmVlanAssocPrimaryVlanState": cfprApVmVlanAssocPrimaryVlanState,
       "cfprApVmVlanAssocPrimaryVlanSwitchId": cfprApVmVlanAssocPrimaryVlanSwitchId,
       "cfprApVmVlanEpDn": cfprApVmVlanEpDn,
       "cfprApVmVlanId": cfprApVmVlanId,
       "cfprApVmVlanIfRole": cfprApVmVlanIfRole,
       "cfprApVmVlanIfType": cfprApVmVlanIfType,
       "cfprApVmVlanLocale": cfprApVmVlanLocale,
       "cfprApVmVlanName": cfprApVmVlanName,
       "cfprApVmVlanOperState": cfprApVmVlanOperState,
       "cfprApVmVlanOverlapStateForA": cfprApVmVlanOverlapStateForA,
       "cfprApVmVlanOverlapStateForB": cfprApVmVlanOverlapStateForB,
       "cfprApVmVlanPeerDn": cfprApVmVlanPeerDn,
       "cfprApVmVlanPolicyOwner": cfprApVmVlanPolicyOwner,
       "cfprApVmVlanPubNwDn": cfprApVmVlanPubNwDn,
       "cfprApVmVlanPubNwId": cfprApVmVlanPubNwId,
       "cfprApVmVlanPubNwName": cfprApVmVlanPubNwName,
       "cfprApVmVlanSharing": cfprApVmVlanSharing,
       "cfprApVmVlanSwitchId": cfprApVmVlanSwitchId,
       "cfprApVmVlanTransport": cfprApVmVlanTransport,
       "cfprApVmVlanType": cfprApVmVlanType,
       "cfprApVmVnicProfClTable": cfprApVmVnicProfClTable,
       "cfprApVmVnicProfClEntry": cfprApVmVnicProfClEntry,
       "cfprApVmVnicProfClInstanceId": cfprApVmVnicProfClInstanceId,
       "cfprApVmVnicProfClDn": cfprApVmVnicProfClDn,
       "cfprApVmVnicProfClRn": cfprApVmVnicProfClRn,
       "cfprApVmVnicProfClDcName": cfprApVmVnicProfClDcName,
       "cfprApVmVnicProfClDescr": cfprApVmVnicProfClDescr,
       "cfprApVmVnicProfClIntId": cfprApVmVnicProfClIntId,
       "cfprApVmVnicProfClName": cfprApVmVnicProfClName,
       "cfprApVmVnicProfClOrgPath": cfprApVmVnicProfClOrgPath,
       "cfprApVmVnicProfClPolicyLevel": cfprApVmVnicProfClPolicyLevel,
       "cfprApVmVnicProfClPolicyOwner": cfprApVmVnicProfClPolicyOwner,
       "cfprApVmVnicProfClSwName": cfprApVmVnicProfClSwName,
       "cfprApVmVnicProfInstTable": cfprApVmVnicProfInstTable,
       "cfprApVmVnicProfInstEntry": cfprApVmVnicProfInstEntry,
       "cfprApVmVnicProfInstInstanceId": cfprApVmVnicProfInstInstanceId,
       "cfprApVmVnicProfInstDn": cfprApVmVnicProfInstDn,
       "cfprApVmVnicProfInstRn": cfprApVmVnicProfInstRn,
       "cfprApVmVnicProfInstDescr": cfprApVmVnicProfInstDescr,
       "cfprApVmVnicProfInstIntId": cfprApVmVnicProfInstIntId,
       "cfprApVmVnicProfInstMaxPorts": cfprApVmVnicProfInstMaxPorts,
       "cfprApVmVnicProfInstName": cfprApVmVnicProfInstName,
       "cfprApVmVnicProfInstPolicyLevel": cfprApVmVnicProfInstPolicyLevel,
       "cfprApVmVnicProfInstPolicyOwner": cfprApVmVnicProfInstPolicyOwner,
       "cfprApVmVnicProfInstProfDn": cfprApVmVnicProfInstProfDn,
       "cfprApVmVnicProfInstProfileType": cfprApVmVnicProfInstProfileType,
       "cfprApVmVsanTable": cfprApVmVsanTable,
       "cfprApVmVsanEntry": cfprApVmVsanEntry,
       "cfprApVmVsanInstanceId": cfprApVmVsanInstanceId,
       "cfprApVmVsanDn": cfprApVmVsanDn,
       "cfprApVmVsanRn": cfprApVmVsanRn,
       "cfprApVmVsanEpDn": cfprApVmVsanEpDn,
       "cfprApVmVsanFcoeVlan": cfprApVmVsanFcoeVlan,
       "cfprApVmVsanId": cfprApVmVsanId,
       "cfprApVmVsanIfRole": cfprApVmVsanIfRole,
       "cfprApVmVsanIfType": cfprApVmVsanIfType,
       "cfprApVmVsanLocale": cfprApVmVsanLocale,
       "cfprApVmVsanName": cfprApVmVsanName,
       "cfprApVmVsanOperState": cfprApVmVsanOperState,
       "cfprApVmVsanPeerDn": cfprApVmVsanPeerDn,
       "cfprApVmVsanPolicyOwner": cfprApVmVsanPolicyOwner,
       "cfprApVmVsanSwitchId": cfprApVmVsanSwitchId,
       "cfprApVmVsanTransport": cfprApVmVsanTransport,
       "cfprApVmVsanType": cfprApVmVsanType,
       "cfprApVmVsanZoningState": cfprApVmVsanZoningState}
)
