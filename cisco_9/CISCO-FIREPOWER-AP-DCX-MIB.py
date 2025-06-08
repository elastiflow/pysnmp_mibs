# SNMP MIB module (CISCO-FIREPOWER-AP-DCX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-DCX-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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
 CfprApDcxAdminState,
 CfprApDcxNsAllocStatus,
 CfprApDcxOperState,
 CfprApDcxProtState,
 CfprApDcxState,
 CfprApDcxVIfProtRole,
 CfprApDpsecForgedTransmit,
 CfprApFabricTrafficDirection,
 CfprApFsmLifecycle,
 CfprApNetworkConnectionType,
 CfprApNetworkLocale,
 CfprApNetworkPortRole,
 CfprApNetworkPortType,
 CfprApNetworkSide,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApNwctrlAdminState,
 CfprApNwctrlLinkFailAction,
 CfprApNwctrlRegistrationMode,
 CfprApQosHostControl,
 CfprApVnicInstantiation) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAdaptorLinkState",
    "CfprApAdaptorServiceState",
    "CfprApDcxAdminState",
    "CfprApDcxNsAllocStatus",
    "CfprApDcxOperState",
    "CfprApDcxProtState",
    "CfprApDcxState",
    "CfprApDcxVIfProtRole",
    "CfprApDpsecForgedTransmit",
    "CfprApFabricTrafficDirection",
    "CfprApFsmLifecycle",
    "CfprApNetworkConnectionType",
    "CfprApNetworkLocale",
    "CfprApNetworkPortRole",
    "CfprApNetworkPortType",
    "CfprApNetworkSide",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
    "CfprApNwctrlAdminState",
    "CfprApNwctrlLinkFailAction",
    "CfprApNwctrlRegistrationMode",
    "CfprApQosHostControl",
    "CfprApVnicInstantiation")

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

cfprApDcxObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApDcxFcoeVifEpTable_Object = MibTable
cfprApDcxFcoeVifEpTable = _CfprApDcxFcoeVifEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cfprApDcxFcoeVifEpTable.setStatus("current")
_CfprApDcxFcoeVifEpEntry_Object = MibTableRow
cfprApDcxFcoeVifEpEntry = _CfprApDcxFcoeVifEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 1, 1)
)
cfprApDcxFcoeVifEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DCX-MIB", "cfprApDcxFcoeVifEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDcxFcoeVifEpEntry.setStatus("current")
_CfprApDcxFcoeVifEpInstanceId_Type = CfprApManagedObjectId
_CfprApDcxFcoeVifEpInstanceId_Object = MibTableColumn
cfprApDcxFcoeVifEpInstanceId = _CfprApDcxFcoeVifEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 1, 1, 1),
    _CfprApDcxFcoeVifEpInstanceId_Type()
)
cfprApDcxFcoeVifEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDcxFcoeVifEpInstanceId.setStatus("current")
_CfprApDcxFcoeVifEpDn_Type = CfprApManagedObjectDn
_CfprApDcxFcoeVifEpDn_Object = MibTableColumn
cfprApDcxFcoeVifEpDn = _CfprApDcxFcoeVifEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 1, 1, 2),
    _CfprApDcxFcoeVifEpDn_Type()
)
cfprApDcxFcoeVifEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxFcoeVifEpDn.setStatus("current")
_CfprApDcxFcoeVifEpRn_Type = SnmpAdminString
_CfprApDcxFcoeVifEpRn_Object = MibTableColumn
cfprApDcxFcoeVifEpRn = _CfprApDcxFcoeVifEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 1, 1, 3),
    _CfprApDcxFcoeVifEpRn_Type()
)
cfprApDcxFcoeVifEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxFcoeVifEpRn.setStatus("current")
_CfprApDcxFcoeVifEpId_Type = Gauge32
_CfprApDcxFcoeVifEpId_Object = MibTableColumn
cfprApDcxFcoeVifEpId = _CfprApDcxFcoeVifEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 1, 1, 4),
    _CfprApDcxFcoeVifEpId_Type()
)
cfprApDcxFcoeVifEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxFcoeVifEpId.setStatus("current")
_CfprApDcxNsTable_Object = MibTable
cfprApDcxNsTable = _CfprApDcxNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    cfprApDcxNsTable.setStatus("current")
_CfprApDcxNsEntry_Object = MibTableRow
cfprApDcxNsEntry = _CfprApDcxNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1)
)
cfprApDcxNsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DCX-MIB", "cfprApDcxNsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDcxNsEntry.setStatus("current")
_CfprApDcxNsInstanceId_Type = CfprApManagedObjectId
_CfprApDcxNsInstanceId_Object = MibTableColumn
cfprApDcxNsInstanceId = _CfprApDcxNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 1),
    _CfprApDcxNsInstanceId_Type()
)
cfprApDcxNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDcxNsInstanceId.setStatus("current")
_CfprApDcxNsDn_Type = CfprApManagedObjectDn
_CfprApDcxNsDn_Object = MibTableColumn
cfprApDcxNsDn = _CfprApDcxNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 2),
    _CfprApDcxNsDn_Type()
)
cfprApDcxNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsDn.setStatus("current")
_CfprApDcxNsRn_Type = SnmpAdminString
_CfprApDcxNsRn_Object = MibTableColumn
cfprApDcxNsRn = _CfprApDcxNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 3),
    _CfprApDcxNsRn_Type()
)
cfprApDcxNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsRn.setStatus("current")
_CfprApDcxNsAllocStatus_Type = CfprApDcxNsAllocStatus
_CfprApDcxNsAllocStatus_Object = MibTableColumn
cfprApDcxNsAllocStatus = _CfprApDcxNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 4),
    _CfprApDcxNsAllocStatus_Type()
)
cfprApDcxNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsAllocStatus.setStatus("current")
_CfprApDcxNsSide_Type = CfprApNetworkSide
_CfprApDcxNsSide_Object = MibTableColumn
cfprApDcxNsSide = _CfprApDcxNsSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 5),
    _CfprApDcxNsSide_Type()
)
cfprApDcxNsSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsSide.setStatus("current")
_CfprApDcxNsSize_Type = Gauge32
_CfprApDcxNsSize_Object = MibTableColumn
cfprApDcxNsSize = _CfprApDcxNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 6),
    _CfprApDcxNsSize_Type()
)
cfprApDcxNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsSize.setStatus("current")
_CfprApDcxNsSwitchId_Type = CfprApNetworkSwitchId
_CfprApDcxNsSwitchId_Object = MibTableColumn
cfprApDcxNsSwitchId = _CfprApDcxNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 7),
    _CfprApDcxNsSwitchId_Type()
)
cfprApDcxNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsSwitchId.setStatus("current")
_CfprApDcxNsUsed_Type = Gauge32
_CfprApDcxNsUsed_Object = MibTableColumn
cfprApDcxNsUsed = _CfprApDcxNsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 2, 1, 8),
    _CfprApDcxNsUsed_Type()
)
cfprApDcxNsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxNsUsed.setStatus("current")
_CfprApDcxUniverseTable_Object = MibTable
cfprApDcxUniverseTable = _CfprApDcxUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    cfprApDcxUniverseTable.setStatus("current")
_CfprApDcxUniverseEntry_Object = MibTableRow
cfprApDcxUniverseEntry = _CfprApDcxUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 3, 1)
)
cfprApDcxUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DCX-MIB", "cfprApDcxUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDcxUniverseEntry.setStatus("current")
_CfprApDcxUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApDcxUniverseInstanceId_Object = MibTableColumn
cfprApDcxUniverseInstanceId = _CfprApDcxUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 3, 1, 1),
    _CfprApDcxUniverseInstanceId_Type()
)
cfprApDcxUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDcxUniverseInstanceId.setStatus("current")
_CfprApDcxUniverseDn_Type = CfprApManagedObjectDn
_CfprApDcxUniverseDn_Object = MibTableColumn
cfprApDcxUniverseDn = _CfprApDcxUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 3, 1, 2),
    _CfprApDcxUniverseDn_Type()
)
cfprApDcxUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxUniverseDn.setStatus("current")
_CfprApDcxUniverseRn_Type = SnmpAdminString
_CfprApDcxUniverseRn_Object = MibTableColumn
cfprApDcxUniverseRn = _CfprApDcxUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 3, 1, 3),
    _CfprApDcxUniverseRn_Type()
)
cfprApDcxUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxUniverseRn.setStatus("current")
_CfprApDcxVIfTable_Object = MibTable
cfprApDcxVIfTable = _CfprApDcxVIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    cfprApDcxVIfTable.setStatus("current")
_CfprApDcxVIfEntry_Object = MibTableRow
cfprApDcxVIfEntry = _CfprApDcxVIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1)
)
cfprApDcxVIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DCX-MIB", "cfprApDcxVIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDcxVIfEntry.setStatus("current")
_CfprApDcxVIfInstanceId_Type = CfprApManagedObjectId
_CfprApDcxVIfInstanceId_Object = MibTableColumn
cfprApDcxVIfInstanceId = _CfprApDcxVIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 1),
    _CfprApDcxVIfInstanceId_Type()
)
cfprApDcxVIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDcxVIfInstanceId.setStatus("current")
_CfprApDcxVIfDn_Type = CfprApManagedObjectDn
_CfprApDcxVIfDn_Object = MibTableColumn
cfprApDcxVIfDn = _CfprApDcxVIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 2),
    _CfprApDcxVIfDn_Type()
)
cfprApDcxVIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfDn.setStatus("current")
_CfprApDcxVIfRn_Type = SnmpAdminString
_CfprApDcxVIfRn_Object = MibTableColumn
cfprApDcxVIfRn = _CfprApDcxVIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 3),
    _CfprApDcxVIfRn_Type()
)
cfprApDcxVIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfRn.setStatus("current")
_CfprApDcxVIfAdminState_Type = CfprApDcxAdminState
_CfprApDcxVIfAdminState_Object = MibTableColumn
cfprApDcxVIfAdminState = _CfprApDcxVIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 4),
    _CfprApDcxVIfAdminState_Type()
)
cfprApDcxVIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfAdminState.setStatus("current")
_CfprApDcxVIfCookie_Type = Unsigned64
_CfprApDcxVIfCookie_Object = MibTableColumn
cfprApDcxVIfCookie = _CfprApDcxVIfCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 5),
    _CfprApDcxVIfCookie_Type()
)
cfprApDcxVIfCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfCookie.setStatus("current")
_CfprApDcxVIfEpDn_Type = SnmpAdminString
_CfprApDcxVIfEpDn_Object = MibTableColumn
cfprApDcxVIfEpDn = _CfprApDcxVIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 6),
    _CfprApDcxVIfEpDn_Type()
)
cfprApDcxVIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfEpDn.setStatus("current")
_CfprApDcxVIfId_Type = Gauge32
_CfprApDcxVIfId_Object = MibTableColumn
cfprApDcxVIfId = _CfprApDcxVIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 7),
    _CfprApDcxVIfId_Type()
)
cfprApDcxVIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfId.setStatus("current")
_CfprApDcxVIfIfRole_Type = CfprApNetworkPortRole
_CfprApDcxVIfIfRole_Object = MibTableColumn
cfprApDcxVIfIfRole = _CfprApDcxVIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 8),
    _CfprApDcxVIfIfRole_Type()
)
cfprApDcxVIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfIfRole.setStatus("current")
_CfprApDcxVIfIfType_Type = CfprApNetworkPortType
_CfprApDcxVIfIfType_Object = MibTableColumn
cfprApDcxVIfIfType = _CfprApDcxVIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 9),
    _CfprApDcxVIfIfType_Type()
)
cfprApDcxVIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfIfType.setStatus("current")
_CfprApDcxVIfInstType_Type = CfprApVnicInstantiation
_CfprApDcxVIfInstType_Object = MibTableColumn
cfprApDcxVIfInstType = _CfprApDcxVIfInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 10),
    _CfprApDcxVIfInstType_Type()
)
cfprApDcxVIfInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfInstType.setStatus("current")
_CfprApDcxVIfLc_Type = CfprApFsmLifecycle
_CfprApDcxVIfLc_Object = MibTableColumn
cfprApDcxVIfLc = _CfprApDcxVIfLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 11),
    _CfprApDcxVIfLc_Type()
)
cfprApDcxVIfLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfLc.setStatus("current")
_CfprApDcxVIfLinkState_Type = CfprApAdaptorLinkState
_CfprApDcxVIfLinkState_Object = MibTableColumn
cfprApDcxVIfLinkState = _CfprApDcxVIfLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 12),
    _CfprApDcxVIfLinkState_Type()
)
cfprApDcxVIfLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfLinkState.setStatus("current")
_CfprApDcxVIfLocale_Type = CfprApNetworkLocale
_CfprApDcxVIfLocale_Object = MibTableColumn
cfprApDcxVIfLocale = _CfprApDcxVIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 13),
    _CfprApDcxVIfLocale_Type()
)
cfprApDcxVIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfLocale.setStatus("current")
_CfprApDcxVIfName_Type = SnmpAdminString
_CfprApDcxVIfName_Object = MibTableColumn
cfprApDcxVIfName = _CfprApDcxVIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 14),
    _CfprApDcxVIfName_Type()
)
cfprApDcxVIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfName.setStatus("current")
_CfprApDcxVIfOperState_Type = CfprApDcxOperState
_CfprApDcxVIfOperState_Object = MibTableColumn
cfprApDcxVIfOperState = _CfprApDcxVIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 15),
    _CfprApDcxVIfOperState_Type()
)
cfprApDcxVIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfOperState.setStatus("current")
_CfprApDcxVIfPeerDn_Type = SnmpAdminString
_CfprApDcxVIfPeerDn_Object = MibTableColumn
cfprApDcxVIfPeerDn = _CfprApDcxVIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 16),
    _CfprApDcxVIfPeerDn_Type()
)
cfprApDcxVIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfPeerDn.setStatus("current")
_CfprApDcxVIfProtPeerId_Type = Gauge32
_CfprApDcxVIfProtPeerId_Object = MibTableColumn
cfprApDcxVIfProtPeerId = _CfprApDcxVIfProtPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 17),
    _CfprApDcxVIfProtPeerId_Type()
)
cfprApDcxVIfProtPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfProtPeerId.setStatus("current")
_CfprApDcxVIfProtRole_Type = CfprApDcxVIfProtRole
_CfprApDcxVIfProtRole_Object = MibTableColumn
cfprApDcxVIfProtRole = _CfprApDcxVIfProtRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 18),
    _CfprApDcxVIfProtRole_Type()
)
cfprApDcxVIfProtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfProtRole.setStatus("current")
_CfprApDcxVIfProtState_Type = CfprApDcxProtState
_CfprApDcxVIfProtState_Object = MibTableColumn
cfprApDcxVIfProtState = _CfprApDcxVIfProtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 19),
    _CfprApDcxVIfProtState_Type()
)
cfprApDcxVIfProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfProtState.setStatus("current")
_CfprApDcxVIfQosControl_Type = CfprApQosHostControl
_CfprApDcxVIfQosControl_Object = MibTableColumn
cfprApDcxVIfQosControl = _CfprApDcxVIfQosControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 20),
    _CfprApDcxVIfQosControl_Type()
)
cfprApDcxVIfQosControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfQosControl.setStatus("current")
_CfprApDcxVIfServiceState_Type = CfprApAdaptorServiceState
_CfprApDcxVIfServiceState_Object = MibTableColumn
cfprApDcxVIfServiceState = _CfprApDcxVIfServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 21),
    _CfprApDcxVIfServiceState_Type()
)
cfprApDcxVIfServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfServiceState.setStatus("current")
_CfprApDcxVIfState_Type = CfprApDcxState
_CfprApDcxVIfState_Object = MibTableColumn
cfprApDcxVIfState = _CfprApDcxVIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 22),
    _CfprApDcxVIfState_Type()
)
cfprApDcxVIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfState.setStatus("current")
_CfprApDcxVIfSwitchId_Type = CfprApNetworkSwitchId
_CfprApDcxVIfSwitchId_Object = MibTableColumn
cfprApDcxVIfSwitchId = _CfprApDcxVIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 23),
    _CfprApDcxVIfSwitchId_Type()
)
cfprApDcxVIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfSwitchId.setStatus("current")
_CfprApDcxVIfTag_Type = Gauge32
_CfprApDcxVIfTag_Object = MibTableColumn
cfprApDcxVIfTag = _CfprApDcxVIfTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 24),
    _CfprApDcxVIfTag_Type()
)
cfprApDcxVIfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfTag.setStatus("current")
_CfprApDcxVIfTransport_Type = CfprApNetworkTransport
_CfprApDcxVIfTransport_Object = MibTableColumn
cfprApDcxVIfTransport = _CfprApDcxVIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 25),
    _CfprApDcxVIfTransport_Type()
)
cfprApDcxVIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfTransport.setStatus("current")
_CfprApDcxVIfType_Type = CfprApNetworkConnectionType
_CfprApDcxVIfType_Object = MibTableColumn
cfprApDcxVIfType = _CfprApDcxVIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 4, 1, 26),
    _CfprApDcxVIfType_Type()
)
cfprApDcxVIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVIfType.setStatus("current")
_CfprApDcxVcTable_Object = MibTable
cfprApDcxVcTable = _CfprApDcxVcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5)
)
if mibBuilder.loadTexts:
    cfprApDcxVcTable.setStatus("current")
_CfprApDcxVcEntry_Object = MibTableRow
cfprApDcxVcEntry = _CfprApDcxVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1)
)
cfprApDcxVcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DCX-MIB", "cfprApDcxVcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDcxVcEntry.setStatus("current")
_CfprApDcxVcInstanceId_Type = CfprApManagedObjectId
_CfprApDcxVcInstanceId_Object = MibTableColumn
cfprApDcxVcInstanceId = _CfprApDcxVcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 1),
    _CfprApDcxVcInstanceId_Type()
)
cfprApDcxVcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDcxVcInstanceId.setStatus("current")
_CfprApDcxVcDn_Type = CfprApManagedObjectDn
_CfprApDcxVcDn_Object = MibTableColumn
cfprApDcxVcDn = _CfprApDcxVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 2),
    _CfprApDcxVcDn_Type()
)
cfprApDcxVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcDn.setStatus("current")
_CfprApDcxVcRn_Type = SnmpAdminString
_CfprApDcxVcRn_Object = MibTableColumn
cfprApDcxVcRn = _CfprApDcxVcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 3),
    _CfprApDcxVcRn_Type()
)
cfprApDcxVcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcRn.setStatus("current")
_CfprApDcxVcAdminState_Type = CfprApDcxAdminState
_CfprApDcxVcAdminState_Object = MibTableColumn
cfprApDcxVcAdminState = _CfprApDcxVcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 4),
    _CfprApDcxVcAdminState_Type()
)
cfprApDcxVcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcAdminState.setStatus("current")
_CfprApDcxVcAllowDtagVlan_Type = TruthValue
_CfprApDcxVcAllowDtagVlan_Object = MibTableColumn
cfprApDcxVcAllowDtagVlan = _CfprApDcxVcAllowDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 5),
    _CfprApDcxVcAllowDtagVlan_Type()
)
cfprApDcxVcAllowDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcAllowDtagVlan.setStatus("current")
_CfprApDcxVcBorderAggrPortId_Type = Gauge32
_CfprApDcxVcBorderAggrPortId_Object = MibTableColumn
cfprApDcxVcBorderAggrPortId = _CfprApDcxVcBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 6),
    _CfprApDcxVcBorderAggrPortId_Type()
)
cfprApDcxVcBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcBorderAggrPortId.setStatus("current")
_CfprApDcxVcBorderPortId_Type = Gauge32
_CfprApDcxVcBorderPortId_Object = MibTableColumn
cfprApDcxVcBorderPortId = _CfprApDcxVcBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 7),
    _CfprApDcxVcBorderPortId_Type()
)
cfprApDcxVcBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcBorderPortId.setStatus("current")
_CfprApDcxVcBorderSlotId_Type = Gauge32
_CfprApDcxVcBorderSlotId_Object = MibTableColumn
cfprApDcxVcBorderSlotId = _CfprApDcxVcBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 8),
    _CfprApDcxVcBorderSlotId_Type()
)
cfprApDcxVcBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcBorderSlotId.setStatus("current")
_CfprApDcxVcBorderVfcId_Type = Gauge32
_CfprApDcxVcBorderVfcId_Object = MibTableColumn
cfprApDcxVcBorderVfcId = _CfprApDcxVcBorderVfcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 9),
    _CfprApDcxVcBorderVfcId_Type()
)
cfprApDcxVcBorderVfcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcBorderVfcId.setStatus("current")
_CfprApDcxVcCdp_Type = CfprApNwctrlAdminState
_CfprApDcxVcCdp_Object = MibTableColumn
cfprApDcxVcCdp = _CfprApDcxVcCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 10),
    _CfprApDcxVcCdp_Type()
)
cfprApDcxVcCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcCdp.setStatus("current")
_CfprApDcxVcCookie_Type = Unsigned64
_CfprApDcxVcCookie_Object = MibTableColumn
cfprApDcxVcCookie = _CfprApDcxVcCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 11),
    _CfprApDcxVcCookie_Type()
)
cfprApDcxVcCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcCookie.setStatus("current")
_CfprApDcxVcCos_Type = Gauge32
_CfprApDcxVcCos_Object = MibTableColumn
cfprApDcxVcCos = _CfprApDcxVcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 12),
    _CfprApDcxVcCos_Type()
)
cfprApDcxVcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcCos.setStatus("current")
_CfprApDcxVcDerivedFromId_Type = Gauge32
_CfprApDcxVcDerivedFromId_Object = MibTableColumn
cfprApDcxVcDerivedFromId = _CfprApDcxVcDerivedFromId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 13),
    _CfprApDcxVcDerivedFromId_Type()
)
cfprApDcxVcDerivedFromId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcDerivedFromId.setStatus("current")
_CfprApDcxVcEncap_Type = Gauge32
_CfprApDcxVcEncap_Object = MibTableColumn
cfprApDcxVcEncap = _CfprApDcxVcEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 14),
    _CfprApDcxVcEncap_Type()
)
cfprApDcxVcEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcEncap.setStatus("current")
_CfprApDcxVcFcoeId_Type = Gauge32
_CfprApDcxVcFcoeId_Object = MibTableColumn
cfprApDcxVcFcoeId = _CfprApDcxVcFcoeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 15),
    _CfprApDcxVcFcoeId_Type()
)
cfprApDcxVcFcoeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcFcoeId.setStatus("current")
_CfprApDcxVcFltAggr_Type = Unsigned64
_CfprApDcxVcFltAggr_Object = MibTableColumn
cfprApDcxVcFltAggr = _CfprApDcxVcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 16),
    _CfprApDcxVcFltAggr_Type()
)
cfprApDcxVcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcFltAggr.setStatus("current")
_CfprApDcxVcForgeMac_Type = CfprApDpsecForgedTransmit
_CfprApDcxVcForgeMac_Object = MibTableColumn
cfprApDcxVcForgeMac = _CfprApDcxVcForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 17),
    _CfprApDcxVcForgeMac_Type()
)
cfprApDcxVcForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcForgeMac.setStatus("current")
_CfprApDcxVcId_Type = Gauge32
_CfprApDcxVcId_Object = MibTableColumn
cfprApDcxVcId = _CfprApDcxVcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 18),
    _CfprApDcxVcId_Type()
)
cfprApDcxVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcId.setStatus("current")
_CfprApDcxVcInstType_Type = CfprApVnicInstantiation
_CfprApDcxVcInstType_Object = MibTableColumn
cfprApDcxVcInstType = _CfprApDcxVcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 19),
    _CfprApDcxVcInstType_Type()
)
cfprApDcxVcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcInstType.setStatus("current")
_CfprApDcxVcLc_Type = CfprApFsmLifecycle
_CfprApDcxVcLc_Object = MibTableColumn
cfprApDcxVcLc = _CfprApDcxVcLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 20),
    _CfprApDcxVcLc_Type()
)
cfprApDcxVcLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcLc.setStatus("current")
_CfprApDcxVcLinkState_Type = CfprApAdaptorLinkState
_CfprApDcxVcLinkState_Object = MibTableColumn
cfprApDcxVcLinkState = _CfprApDcxVcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 21),
    _CfprApDcxVcLinkState_Type()
)
cfprApDcxVcLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcLinkState.setStatus("current")
_CfprApDcxVcLocale_Type = CfprApNetworkLocale
_CfprApDcxVcLocale_Object = MibTableColumn
cfprApDcxVcLocale = _CfprApDcxVcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 22),
    _CfprApDcxVcLocale_Type()
)
cfprApDcxVcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcLocale.setStatus("current")
_CfprApDcxVcMacRegisterMode_Type = CfprApNwctrlRegistrationMode
_CfprApDcxVcMacRegisterMode_Object = MibTableColumn
cfprApDcxVcMacRegisterMode = _CfprApDcxVcMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 23),
    _CfprApDcxVcMacRegisterMode_Type()
)
cfprApDcxVcMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcMacRegisterMode.setStatus("current")
_CfprApDcxVcMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApDcxVcMonTrafDir_Object = MibTableColumn
cfprApDcxVcMonTrafDir = _CfprApDcxVcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 24),
    _CfprApDcxVcMonTrafDir_Type()
)
cfprApDcxVcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcMonTrafDir.setStatus("current")
_CfprApDcxVcName_Type = SnmpAdminString
_CfprApDcxVcName_Object = MibTableColumn
cfprApDcxVcName = _CfprApDcxVcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 25),
    _CfprApDcxVcName_Type()
)
cfprApDcxVcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcName.setStatus("current")
_CfprApDcxVcOperBorderAggrPortId_Type = Gauge32
_CfprApDcxVcOperBorderAggrPortId_Object = MibTableColumn
cfprApDcxVcOperBorderAggrPortId = _CfprApDcxVcOperBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 26),
    _CfprApDcxVcOperBorderAggrPortId_Type()
)
cfprApDcxVcOperBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcOperBorderAggrPortId.setStatus("current")
_CfprApDcxVcOperBorderPortId_Type = Gauge32
_CfprApDcxVcOperBorderPortId_Object = MibTableColumn
cfprApDcxVcOperBorderPortId = _CfprApDcxVcOperBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 27),
    _CfprApDcxVcOperBorderPortId_Type()
)
cfprApDcxVcOperBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcOperBorderPortId.setStatus("current")
_CfprApDcxVcOperBorderSlotId_Type = Gauge32
_CfprApDcxVcOperBorderSlotId_Object = MibTableColumn
cfprApDcxVcOperBorderSlotId = _CfprApDcxVcOperBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 28),
    _CfprApDcxVcOperBorderSlotId_Type()
)
cfprApDcxVcOperBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcOperBorderSlotId.setStatus("current")
_CfprApDcxVcOperState_Type = CfprApDcxOperState
_CfprApDcxVcOperState_Object = MibTableColumn
cfprApDcxVcOperState = _CfprApDcxVcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 29),
    _CfprApDcxVcOperState_Type()
)
cfprApDcxVcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcOperState.setStatus("current")
_CfprApDcxVcPeerId_Type = Gauge32
_CfprApDcxVcPeerId_Object = MibTableColumn
cfprApDcxVcPeerId = _CfprApDcxVcPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 30),
    _CfprApDcxVcPeerId_Type()
)
cfprApDcxVcPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcPeerId.setStatus("current")
_CfprApDcxVcProtState_Type = CfprApDcxProtState
_CfprApDcxVcProtState_Object = MibTableColumn
cfprApDcxVcProtState = _CfprApDcxVcProtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 31),
    _CfprApDcxVcProtState_Type()
)
cfprApDcxVcProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcProtState.setStatus("current")
_CfprApDcxVcQosPolicyDn_Type = SnmpAdminString
_CfprApDcxVcQosPolicyDn_Object = MibTableColumn
cfprApDcxVcQosPolicyDn = _CfprApDcxVcQosPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 32),
    _CfprApDcxVcQosPolicyDn_Type()
)
cfprApDcxVcQosPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcQosPolicyDn.setStatus("current")
_CfprApDcxVcQosPolicyId_Type = SnmpAdminString
_CfprApDcxVcQosPolicyId_Object = MibTableColumn
cfprApDcxVcQosPolicyId = _CfprApDcxVcQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 33),
    _CfprApDcxVcQosPolicyId_Type()
)
cfprApDcxVcQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcQosPolicyId.setStatus("current")
_CfprApDcxVcRole_Type = CfprApNetworkPortRole
_CfprApDcxVcRole_Object = MibTableColumn
cfprApDcxVcRole = _CfprApDcxVcRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 34),
    _CfprApDcxVcRole_Type()
)
cfprApDcxVcRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcRole.setStatus("current")
_CfprApDcxVcServiceState_Type = CfprApAdaptorServiceState
_CfprApDcxVcServiceState_Object = MibTableColumn
cfprApDcxVcServiceState = _CfprApDcxVcServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 35),
    _CfprApDcxVcServiceState_Type()
)
cfprApDcxVcServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcServiceState.setStatus("current")
_CfprApDcxVcState_Type = CfprApDcxState
_CfprApDcxVcState_Object = MibTableColumn
cfprApDcxVcState = _CfprApDcxVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 36),
    _CfprApDcxVcState_Type()
)
cfprApDcxVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcState.setStatus("current")
_CfprApDcxVcStateQual_Type = SnmpAdminString
_CfprApDcxVcStateQual_Object = MibTableColumn
cfprApDcxVcStateQual = _CfprApDcxVcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 37),
    _CfprApDcxVcStateQual_Type()
)
cfprApDcxVcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcStateQual.setStatus("current")
_CfprApDcxVcSwitchId_Type = CfprApNetworkSwitchId
_CfprApDcxVcSwitchId_Object = MibTableColumn
cfprApDcxVcSwitchId = _CfprApDcxVcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 38),
    _CfprApDcxVcSwitchId_Type()
)
cfprApDcxVcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcSwitchId.setStatus("current")
_CfprApDcxVcTag_Type = Gauge32
_CfprApDcxVcTag_Object = MibTableColumn
cfprApDcxVcTag = _CfprApDcxVcTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 39),
    _CfprApDcxVcTag_Type()
)
cfprApDcxVcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcTag.setStatus("current")
_CfprApDcxVcTransport_Type = CfprApNetworkTransport
_CfprApDcxVcTransport_Object = MibTableColumn
cfprApDcxVcTransport = _CfprApDcxVcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 40),
    _CfprApDcxVcTransport_Type()
)
cfprApDcxVcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcTransport.setStatus("current")
_CfprApDcxVcType_Type = CfprApNetworkConnectionType
_CfprApDcxVcType_Object = MibTableColumn
cfprApDcxVcType = _CfprApDcxVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 41),
    _CfprApDcxVcType_Type()
)
cfprApDcxVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcType.setStatus("current")
_CfprApDcxVcUplinkFailAction_Type = CfprApNwctrlLinkFailAction
_CfprApDcxVcUplinkFailAction_Object = MibTableColumn
cfprApDcxVcUplinkFailAction = _CfprApDcxVcUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 42),
    _CfprApDcxVcUplinkFailAction_Type()
)
cfprApDcxVcUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcUplinkFailAction.setStatus("current")
_CfprApDcxVcVnic_Type = SnmpAdminString
_CfprApDcxVcVnic_Object = MibTableColumn
cfprApDcxVcVnic = _CfprApDcxVcVnic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 5, 1, 43),
    _CfprApDcxVcVnic_Type()
)
cfprApDcxVcVnic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVcVnic.setStatus("current")
_CfprApDcxVifEpTable_Object = MibTable
cfprApDcxVifEpTable = _CfprApDcxVifEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 6)
)
if mibBuilder.loadTexts:
    cfprApDcxVifEpTable.setStatus("current")
_CfprApDcxVifEpEntry_Object = MibTableRow
cfprApDcxVifEpEntry = _CfprApDcxVifEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 6, 1)
)
cfprApDcxVifEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DCX-MIB", "cfprApDcxVifEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDcxVifEpEntry.setStatus("current")
_CfprApDcxVifEpInstanceId_Type = CfprApManagedObjectId
_CfprApDcxVifEpInstanceId_Object = MibTableColumn
cfprApDcxVifEpInstanceId = _CfprApDcxVifEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 6, 1, 1),
    _CfprApDcxVifEpInstanceId_Type()
)
cfprApDcxVifEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDcxVifEpInstanceId.setStatus("current")
_CfprApDcxVifEpDn_Type = CfprApManagedObjectDn
_CfprApDcxVifEpDn_Object = MibTableColumn
cfprApDcxVifEpDn = _CfprApDcxVifEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 6, 1, 2),
    _CfprApDcxVifEpDn_Type()
)
cfprApDcxVifEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVifEpDn.setStatus("current")
_CfprApDcxVifEpRn_Type = SnmpAdminString
_CfprApDcxVifEpRn_Object = MibTableColumn
cfprApDcxVifEpRn = _CfprApDcxVifEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 6, 1, 3),
    _CfprApDcxVifEpRn_Type()
)
cfprApDcxVifEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVifEpRn.setStatus("current")
_CfprApDcxVifEpId_Type = Gauge32
_CfprApDcxVifEpId_Object = MibTableColumn
cfprApDcxVifEpId = _CfprApDcxVifEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 14, 6, 1, 4),
    _CfprApDcxVifEpId_Type()
)
cfprApDcxVifEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDcxVifEpId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-DCX-MIB",
    **{"cfprApDcxObjects": cfprApDcxObjects,
       "cfprApDcxFcoeVifEpTable": cfprApDcxFcoeVifEpTable,
       "cfprApDcxFcoeVifEpEntry": cfprApDcxFcoeVifEpEntry,
       "cfprApDcxFcoeVifEpInstanceId": cfprApDcxFcoeVifEpInstanceId,
       "cfprApDcxFcoeVifEpDn": cfprApDcxFcoeVifEpDn,
       "cfprApDcxFcoeVifEpRn": cfprApDcxFcoeVifEpRn,
       "cfprApDcxFcoeVifEpId": cfprApDcxFcoeVifEpId,
       "cfprApDcxNsTable": cfprApDcxNsTable,
       "cfprApDcxNsEntry": cfprApDcxNsEntry,
       "cfprApDcxNsInstanceId": cfprApDcxNsInstanceId,
       "cfprApDcxNsDn": cfprApDcxNsDn,
       "cfprApDcxNsRn": cfprApDcxNsRn,
       "cfprApDcxNsAllocStatus": cfprApDcxNsAllocStatus,
       "cfprApDcxNsSide": cfprApDcxNsSide,
       "cfprApDcxNsSize": cfprApDcxNsSize,
       "cfprApDcxNsSwitchId": cfprApDcxNsSwitchId,
       "cfprApDcxNsUsed": cfprApDcxNsUsed,
       "cfprApDcxUniverseTable": cfprApDcxUniverseTable,
       "cfprApDcxUniverseEntry": cfprApDcxUniverseEntry,
       "cfprApDcxUniverseInstanceId": cfprApDcxUniverseInstanceId,
       "cfprApDcxUniverseDn": cfprApDcxUniverseDn,
       "cfprApDcxUniverseRn": cfprApDcxUniverseRn,
       "cfprApDcxVIfTable": cfprApDcxVIfTable,
       "cfprApDcxVIfEntry": cfprApDcxVIfEntry,
       "cfprApDcxVIfInstanceId": cfprApDcxVIfInstanceId,
       "cfprApDcxVIfDn": cfprApDcxVIfDn,
       "cfprApDcxVIfRn": cfprApDcxVIfRn,
       "cfprApDcxVIfAdminState": cfprApDcxVIfAdminState,
       "cfprApDcxVIfCookie": cfprApDcxVIfCookie,
       "cfprApDcxVIfEpDn": cfprApDcxVIfEpDn,
       "cfprApDcxVIfId": cfprApDcxVIfId,
       "cfprApDcxVIfIfRole": cfprApDcxVIfIfRole,
       "cfprApDcxVIfIfType": cfprApDcxVIfIfType,
       "cfprApDcxVIfInstType": cfprApDcxVIfInstType,
       "cfprApDcxVIfLc": cfprApDcxVIfLc,
       "cfprApDcxVIfLinkState": cfprApDcxVIfLinkState,
       "cfprApDcxVIfLocale": cfprApDcxVIfLocale,
       "cfprApDcxVIfName": cfprApDcxVIfName,
       "cfprApDcxVIfOperState": cfprApDcxVIfOperState,
       "cfprApDcxVIfPeerDn": cfprApDcxVIfPeerDn,
       "cfprApDcxVIfProtPeerId": cfprApDcxVIfProtPeerId,
       "cfprApDcxVIfProtRole": cfprApDcxVIfProtRole,
       "cfprApDcxVIfProtState": cfprApDcxVIfProtState,
       "cfprApDcxVIfQosControl": cfprApDcxVIfQosControl,
       "cfprApDcxVIfServiceState": cfprApDcxVIfServiceState,
       "cfprApDcxVIfState": cfprApDcxVIfState,
       "cfprApDcxVIfSwitchId": cfprApDcxVIfSwitchId,
       "cfprApDcxVIfTag": cfprApDcxVIfTag,
       "cfprApDcxVIfTransport": cfprApDcxVIfTransport,
       "cfprApDcxVIfType": cfprApDcxVIfType,
       "cfprApDcxVcTable": cfprApDcxVcTable,
       "cfprApDcxVcEntry": cfprApDcxVcEntry,
       "cfprApDcxVcInstanceId": cfprApDcxVcInstanceId,
       "cfprApDcxVcDn": cfprApDcxVcDn,
       "cfprApDcxVcRn": cfprApDcxVcRn,
       "cfprApDcxVcAdminState": cfprApDcxVcAdminState,
       "cfprApDcxVcAllowDtagVlan": cfprApDcxVcAllowDtagVlan,
       "cfprApDcxVcBorderAggrPortId": cfprApDcxVcBorderAggrPortId,
       "cfprApDcxVcBorderPortId": cfprApDcxVcBorderPortId,
       "cfprApDcxVcBorderSlotId": cfprApDcxVcBorderSlotId,
       "cfprApDcxVcBorderVfcId": cfprApDcxVcBorderVfcId,
       "cfprApDcxVcCdp": cfprApDcxVcCdp,
       "cfprApDcxVcCookie": cfprApDcxVcCookie,
       "cfprApDcxVcCos": cfprApDcxVcCos,
       "cfprApDcxVcDerivedFromId": cfprApDcxVcDerivedFromId,
       "cfprApDcxVcEncap": cfprApDcxVcEncap,
       "cfprApDcxVcFcoeId": cfprApDcxVcFcoeId,
       "cfprApDcxVcFltAggr": cfprApDcxVcFltAggr,
       "cfprApDcxVcForgeMac": cfprApDcxVcForgeMac,
       "cfprApDcxVcId": cfprApDcxVcId,
       "cfprApDcxVcInstType": cfprApDcxVcInstType,
       "cfprApDcxVcLc": cfprApDcxVcLc,
       "cfprApDcxVcLinkState": cfprApDcxVcLinkState,
       "cfprApDcxVcLocale": cfprApDcxVcLocale,
       "cfprApDcxVcMacRegisterMode": cfprApDcxVcMacRegisterMode,
       "cfprApDcxVcMonTrafDir": cfprApDcxVcMonTrafDir,
       "cfprApDcxVcName": cfprApDcxVcName,
       "cfprApDcxVcOperBorderAggrPortId": cfprApDcxVcOperBorderAggrPortId,
       "cfprApDcxVcOperBorderPortId": cfprApDcxVcOperBorderPortId,
       "cfprApDcxVcOperBorderSlotId": cfprApDcxVcOperBorderSlotId,
       "cfprApDcxVcOperState": cfprApDcxVcOperState,
       "cfprApDcxVcPeerId": cfprApDcxVcPeerId,
       "cfprApDcxVcProtState": cfprApDcxVcProtState,
       "cfprApDcxVcQosPolicyDn": cfprApDcxVcQosPolicyDn,
       "cfprApDcxVcQosPolicyId": cfprApDcxVcQosPolicyId,
       "cfprApDcxVcRole": cfprApDcxVcRole,
       "cfprApDcxVcServiceState": cfprApDcxVcServiceState,
       "cfprApDcxVcState": cfprApDcxVcState,
       "cfprApDcxVcStateQual": cfprApDcxVcStateQual,
       "cfprApDcxVcSwitchId": cfprApDcxVcSwitchId,
       "cfprApDcxVcTag": cfprApDcxVcTag,
       "cfprApDcxVcTransport": cfprApDcxVcTransport,
       "cfprApDcxVcType": cfprApDcxVcType,
       "cfprApDcxVcUplinkFailAction": cfprApDcxVcUplinkFailAction,
       "cfprApDcxVcVnic": cfprApDcxVcVnic,
       "cfprApDcxVifEpTable": cfprApDcxVifEpTable,
       "cfprApDcxVifEpEntry": cfprApDcxVifEpEntry,
       "cfprApDcxVifEpInstanceId": cfprApDcxVifEpInstanceId,
       "cfprApDcxVifEpDn": cfprApDcxVifEpDn,
       "cfprApDcxVifEpRn": cfprApDcxVifEpRn,
       "cfprApDcxVifEpId": cfprApDcxVifEpId}
)
