# SNMP MIB module (CISCO-FIREPOWER-DCX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-DCX-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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
 CfprDcxAdminState,
 CfprDcxNsAllocStatus,
 CfprDcxOperState,
 CfprDcxProtState,
 CfprDcxState,
 CfprDcxVIfProtRole,
 CfprDpsecForgedTransmit,
 CfprFabricTrafficDirection,
 CfprFsmLifecycle,
 CfprNetworkConnectionType,
 CfprNetworkLocale,
 CfprNetworkPortRole,
 CfprNetworkPortType,
 CfprNetworkSide,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprNwctrlAdminState,
 CfprNwctrlLinkFailAction,
 CfprNwctrlRegistrationMode,
 CfprQosHostControl,
 CfprVnicInstantiation) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAdaptorLinkState",
    "CfprAdaptorServiceState",
    "CfprDcxAdminState",
    "CfprDcxNsAllocStatus",
    "CfprDcxOperState",
    "CfprDcxProtState",
    "CfprDcxState",
    "CfprDcxVIfProtRole",
    "CfprDpsecForgedTransmit",
    "CfprFabricTrafficDirection",
    "CfprFsmLifecycle",
    "CfprNetworkConnectionType",
    "CfprNetworkLocale",
    "CfprNetworkPortRole",
    "CfprNetworkPortType",
    "CfprNetworkSide",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
    "CfprNwctrlAdminState",
    "CfprNwctrlLinkFailAction",
    "CfprNwctrlRegistrationMode",
    "CfprQosHostControl",
    "CfprVnicInstantiation")

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

cfprDcxObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprDcxFcoeVifEpTable_Object = MibTable
cfprDcxFcoeVifEpTable = _CfprDcxFcoeVifEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cfprDcxFcoeVifEpTable.setStatus("current")
_CfprDcxFcoeVifEpEntry_Object = MibTableRow
cfprDcxFcoeVifEpEntry = _CfprDcxFcoeVifEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 1, 1)
)
cfprDcxFcoeVifEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DCX-MIB", "cfprDcxFcoeVifEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDcxFcoeVifEpEntry.setStatus("current")
_CfprDcxFcoeVifEpInstanceId_Type = CfprManagedObjectId
_CfprDcxFcoeVifEpInstanceId_Object = MibTableColumn
cfprDcxFcoeVifEpInstanceId = _CfprDcxFcoeVifEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 1, 1, 1),
    _CfprDcxFcoeVifEpInstanceId_Type()
)
cfprDcxFcoeVifEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDcxFcoeVifEpInstanceId.setStatus("current")
_CfprDcxFcoeVifEpDn_Type = CfprManagedObjectDn
_CfprDcxFcoeVifEpDn_Object = MibTableColumn
cfprDcxFcoeVifEpDn = _CfprDcxFcoeVifEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 1, 1, 2),
    _CfprDcxFcoeVifEpDn_Type()
)
cfprDcxFcoeVifEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxFcoeVifEpDn.setStatus("current")
_CfprDcxFcoeVifEpRn_Type = SnmpAdminString
_CfprDcxFcoeVifEpRn_Object = MibTableColumn
cfprDcxFcoeVifEpRn = _CfprDcxFcoeVifEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 1, 1, 3),
    _CfprDcxFcoeVifEpRn_Type()
)
cfprDcxFcoeVifEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxFcoeVifEpRn.setStatus("current")
_CfprDcxFcoeVifEpId_Type = Gauge32
_CfprDcxFcoeVifEpId_Object = MibTableColumn
cfprDcxFcoeVifEpId = _CfprDcxFcoeVifEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 1, 1, 4),
    _CfprDcxFcoeVifEpId_Type()
)
cfprDcxFcoeVifEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxFcoeVifEpId.setStatus("current")
_CfprDcxNsTable_Object = MibTable
cfprDcxNsTable = _CfprDcxNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2)
)
if mibBuilder.loadTexts:
    cfprDcxNsTable.setStatus("current")
_CfprDcxNsEntry_Object = MibTableRow
cfprDcxNsEntry = _CfprDcxNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1)
)
cfprDcxNsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DCX-MIB", "cfprDcxNsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDcxNsEntry.setStatus("current")
_CfprDcxNsInstanceId_Type = CfprManagedObjectId
_CfprDcxNsInstanceId_Object = MibTableColumn
cfprDcxNsInstanceId = _CfprDcxNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 1),
    _CfprDcxNsInstanceId_Type()
)
cfprDcxNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDcxNsInstanceId.setStatus("current")
_CfprDcxNsDn_Type = CfprManagedObjectDn
_CfprDcxNsDn_Object = MibTableColumn
cfprDcxNsDn = _CfprDcxNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 2),
    _CfprDcxNsDn_Type()
)
cfprDcxNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsDn.setStatus("current")
_CfprDcxNsRn_Type = SnmpAdminString
_CfprDcxNsRn_Object = MibTableColumn
cfprDcxNsRn = _CfprDcxNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 3),
    _CfprDcxNsRn_Type()
)
cfprDcxNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsRn.setStatus("current")
_CfprDcxNsAllocStatus_Type = CfprDcxNsAllocStatus
_CfprDcxNsAllocStatus_Object = MibTableColumn
cfprDcxNsAllocStatus = _CfprDcxNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 4),
    _CfprDcxNsAllocStatus_Type()
)
cfprDcxNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsAllocStatus.setStatus("current")
_CfprDcxNsSide_Type = CfprNetworkSide
_CfprDcxNsSide_Object = MibTableColumn
cfprDcxNsSide = _CfprDcxNsSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 5),
    _CfprDcxNsSide_Type()
)
cfprDcxNsSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsSide.setStatus("current")
_CfprDcxNsSize_Type = Gauge32
_CfprDcxNsSize_Object = MibTableColumn
cfprDcxNsSize = _CfprDcxNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 6),
    _CfprDcxNsSize_Type()
)
cfprDcxNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsSize.setStatus("current")
_CfprDcxNsSwitchId_Type = CfprNetworkSwitchId
_CfprDcxNsSwitchId_Object = MibTableColumn
cfprDcxNsSwitchId = _CfprDcxNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 7),
    _CfprDcxNsSwitchId_Type()
)
cfprDcxNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsSwitchId.setStatus("current")
_CfprDcxNsUsed_Type = Gauge32
_CfprDcxNsUsed_Object = MibTableColumn
cfprDcxNsUsed = _CfprDcxNsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 2, 1, 8),
    _CfprDcxNsUsed_Type()
)
cfprDcxNsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxNsUsed.setStatus("current")
_CfprDcxUniverseTable_Object = MibTable
cfprDcxUniverseTable = _CfprDcxUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 3)
)
if mibBuilder.loadTexts:
    cfprDcxUniverseTable.setStatus("current")
_CfprDcxUniverseEntry_Object = MibTableRow
cfprDcxUniverseEntry = _CfprDcxUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 3, 1)
)
cfprDcxUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DCX-MIB", "cfprDcxUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDcxUniverseEntry.setStatus("current")
_CfprDcxUniverseInstanceId_Type = CfprManagedObjectId
_CfprDcxUniverseInstanceId_Object = MibTableColumn
cfprDcxUniverseInstanceId = _CfprDcxUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 3, 1, 1),
    _CfprDcxUniverseInstanceId_Type()
)
cfprDcxUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDcxUniverseInstanceId.setStatus("current")
_CfprDcxUniverseDn_Type = CfprManagedObjectDn
_CfprDcxUniverseDn_Object = MibTableColumn
cfprDcxUniverseDn = _CfprDcxUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 3, 1, 2),
    _CfprDcxUniverseDn_Type()
)
cfprDcxUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxUniverseDn.setStatus("current")
_CfprDcxUniverseRn_Type = SnmpAdminString
_CfprDcxUniverseRn_Object = MibTableColumn
cfprDcxUniverseRn = _CfprDcxUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 3, 1, 3),
    _CfprDcxUniverseRn_Type()
)
cfprDcxUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxUniverseRn.setStatus("current")
_CfprDcxVIfTable_Object = MibTable
cfprDcxVIfTable = _CfprDcxVIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4)
)
if mibBuilder.loadTexts:
    cfprDcxVIfTable.setStatus("current")
_CfprDcxVIfEntry_Object = MibTableRow
cfprDcxVIfEntry = _CfprDcxVIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1)
)
cfprDcxVIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DCX-MIB", "cfprDcxVIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDcxVIfEntry.setStatus("current")
_CfprDcxVIfInstanceId_Type = CfprManagedObjectId
_CfprDcxVIfInstanceId_Object = MibTableColumn
cfprDcxVIfInstanceId = _CfprDcxVIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 1),
    _CfprDcxVIfInstanceId_Type()
)
cfprDcxVIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDcxVIfInstanceId.setStatus("current")
_CfprDcxVIfDn_Type = CfprManagedObjectDn
_CfprDcxVIfDn_Object = MibTableColumn
cfprDcxVIfDn = _CfprDcxVIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 2),
    _CfprDcxVIfDn_Type()
)
cfprDcxVIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfDn.setStatus("current")
_CfprDcxVIfRn_Type = SnmpAdminString
_CfprDcxVIfRn_Object = MibTableColumn
cfprDcxVIfRn = _CfprDcxVIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 3),
    _CfprDcxVIfRn_Type()
)
cfprDcxVIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfRn.setStatus("current")
_CfprDcxVIfAdminState_Type = CfprDcxAdminState
_CfprDcxVIfAdminState_Object = MibTableColumn
cfprDcxVIfAdminState = _CfprDcxVIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 4),
    _CfprDcxVIfAdminState_Type()
)
cfprDcxVIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfAdminState.setStatus("current")
_CfprDcxVIfCookie_Type = Unsigned64
_CfprDcxVIfCookie_Object = MibTableColumn
cfprDcxVIfCookie = _CfprDcxVIfCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 5),
    _CfprDcxVIfCookie_Type()
)
cfprDcxVIfCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfCookie.setStatus("current")
_CfprDcxVIfEpDn_Type = SnmpAdminString
_CfprDcxVIfEpDn_Object = MibTableColumn
cfprDcxVIfEpDn = _CfprDcxVIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 6),
    _CfprDcxVIfEpDn_Type()
)
cfprDcxVIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfEpDn.setStatus("current")
_CfprDcxVIfId_Type = Gauge32
_CfprDcxVIfId_Object = MibTableColumn
cfprDcxVIfId = _CfprDcxVIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 7),
    _CfprDcxVIfId_Type()
)
cfprDcxVIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfId.setStatus("current")
_CfprDcxVIfIfRole_Type = CfprNetworkPortRole
_CfprDcxVIfIfRole_Object = MibTableColumn
cfprDcxVIfIfRole = _CfprDcxVIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 8),
    _CfprDcxVIfIfRole_Type()
)
cfprDcxVIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfIfRole.setStatus("current")
_CfprDcxVIfIfType_Type = CfprNetworkPortType
_CfprDcxVIfIfType_Object = MibTableColumn
cfprDcxVIfIfType = _CfprDcxVIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 9),
    _CfprDcxVIfIfType_Type()
)
cfprDcxVIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfIfType.setStatus("current")
_CfprDcxVIfInstType_Type = CfprVnicInstantiation
_CfprDcxVIfInstType_Object = MibTableColumn
cfprDcxVIfInstType = _CfprDcxVIfInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 10),
    _CfprDcxVIfInstType_Type()
)
cfprDcxVIfInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfInstType.setStatus("current")
_CfprDcxVIfLc_Type = CfprFsmLifecycle
_CfprDcxVIfLc_Object = MibTableColumn
cfprDcxVIfLc = _CfprDcxVIfLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 11),
    _CfprDcxVIfLc_Type()
)
cfprDcxVIfLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfLc.setStatus("current")
_CfprDcxVIfLinkState_Type = CfprAdaptorLinkState
_CfprDcxVIfLinkState_Object = MibTableColumn
cfprDcxVIfLinkState = _CfprDcxVIfLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 12),
    _CfprDcxVIfLinkState_Type()
)
cfprDcxVIfLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfLinkState.setStatus("current")
_CfprDcxVIfLocale_Type = CfprNetworkLocale
_CfprDcxVIfLocale_Object = MibTableColumn
cfprDcxVIfLocale = _CfprDcxVIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 13),
    _CfprDcxVIfLocale_Type()
)
cfprDcxVIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfLocale.setStatus("current")
_CfprDcxVIfName_Type = SnmpAdminString
_CfprDcxVIfName_Object = MibTableColumn
cfprDcxVIfName = _CfprDcxVIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 14),
    _CfprDcxVIfName_Type()
)
cfprDcxVIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfName.setStatus("current")
_CfprDcxVIfOperState_Type = CfprDcxOperState
_CfprDcxVIfOperState_Object = MibTableColumn
cfprDcxVIfOperState = _CfprDcxVIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 15),
    _CfprDcxVIfOperState_Type()
)
cfprDcxVIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfOperState.setStatus("current")
_CfprDcxVIfPeerDn_Type = SnmpAdminString
_CfprDcxVIfPeerDn_Object = MibTableColumn
cfprDcxVIfPeerDn = _CfprDcxVIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 16),
    _CfprDcxVIfPeerDn_Type()
)
cfprDcxVIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfPeerDn.setStatus("current")
_CfprDcxVIfProtPeerId_Type = Gauge32
_CfprDcxVIfProtPeerId_Object = MibTableColumn
cfprDcxVIfProtPeerId = _CfprDcxVIfProtPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 17),
    _CfprDcxVIfProtPeerId_Type()
)
cfprDcxVIfProtPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfProtPeerId.setStatus("current")
_CfprDcxVIfProtRole_Type = CfprDcxVIfProtRole
_CfprDcxVIfProtRole_Object = MibTableColumn
cfprDcxVIfProtRole = _CfprDcxVIfProtRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 18),
    _CfprDcxVIfProtRole_Type()
)
cfprDcxVIfProtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfProtRole.setStatus("current")
_CfprDcxVIfProtState_Type = CfprDcxProtState
_CfprDcxVIfProtState_Object = MibTableColumn
cfprDcxVIfProtState = _CfprDcxVIfProtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 19),
    _CfprDcxVIfProtState_Type()
)
cfprDcxVIfProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfProtState.setStatus("current")
_CfprDcxVIfQosControl_Type = CfprQosHostControl
_CfprDcxVIfQosControl_Object = MibTableColumn
cfprDcxVIfQosControl = _CfprDcxVIfQosControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 20),
    _CfprDcxVIfQosControl_Type()
)
cfprDcxVIfQosControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfQosControl.setStatus("current")
_CfprDcxVIfState_Type = CfprDcxState
_CfprDcxVIfState_Object = MibTableColumn
cfprDcxVIfState = _CfprDcxVIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 21),
    _CfprDcxVIfState_Type()
)
cfprDcxVIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfState.setStatus("current")
_CfprDcxVIfSwitchId_Type = CfprNetworkSwitchId
_CfprDcxVIfSwitchId_Object = MibTableColumn
cfprDcxVIfSwitchId = _CfprDcxVIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 22),
    _CfprDcxVIfSwitchId_Type()
)
cfprDcxVIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfSwitchId.setStatus("current")
_CfprDcxVIfTag_Type = Gauge32
_CfprDcxVIfTag_Object = MibTableColumn
cfprDcxVIfTag = _CfprDcxVIfTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 23),
    _CfprDcxVIfTag_Type()
)
cfprDcxVIfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfTag.setStatus("current")
_CfprDcxVIfTransport_Type = CfprNetworkTransport
_CfprDcxVIfTransport_Object = MibTableColumn
cfprDcxVIfTransport = _CfprDcxVIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 24),
    _CfprDcxVIfTransport_Type()
)
cfprDcxVIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfTransport.setStatus("current")
_CfprDcxVIfType_Type = CfprNetworkConnectionType
_CfprDcxVIfType_Object = MibTableColumn
cfprDcxVIfType = _CfprDcxVIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 25),
    _CfprDcxVIfType_Type()
)
cfprDcxVIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfType.setStatus("current")
_CfprDcxVIfServiceState_Type = CfprAdaptorServiceState
_CfprDcxVIfServiceState_Object = MibTableColumn
cfprDcxVIfServiceState = _CfprDcxVIfServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 26),
    _CfprDcxVIfServiceState_Type()
)
cfprDcxVIfServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfServiceState.setStatus("current")
_CfprDcxVIfVcAdminState_Type = CfprDcxAdminState
_CfprDcxVIfVcAdminState_Object = MibTableColumn
cfprDcxVIfVcAdminState = _CfprDcxVIfVcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 4, 1, 27),
    _CfprDcxVIfVcAdminState_Type()
)
cfprDcxVIfVcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVIfVcAdminState.setStatus("current")
_CfprDcxVcTable_Object = MibTable
cfprDcxVcTable = _CfprDcxVcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5)
)
if mibBuilder.loadTexts:
    cfprDcxVcTable.setStatus("current")
_CfprDcxVcEntry_Object = MibTableRow
cfprDcxVcEntry = _CfprDcxVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1)
)
cfprDcxVcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DCX-MIB", "cfprDcxVcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDcxVcEntry.setStatus("current")
_CfprDcxVcInstanceId_Type = CfprManagedObjectId
_CfprDcxVcInstanceId_Object = MibTableColumn
cfprDcxVcInstanceId = _CfprDcxVcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 1),
    _CfprDcxVcInstanceId_Type()
)
cfprDcxVcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDcxVcInstanceId.setStatus("current")
_CfprDcxVcDn_Type = CfprManagedObjectDn
_CfprDcxVcDn_Object = MibTableColumn
cfprDcxVcDn = _CfprDcxVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 2),
    _CfprDcxVcDn_Type()
)
cfprDcxVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcDn.setStatus("current")
_CfprDcxVcRn_Type = SnmpAdminString
_CfprDcxVcRn_Object = MibTableColumn
cfprDcxVcRn = _CfprDcxVcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 3),
    _CfprDcxVcRn_Type()
)
cfprDcxVcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcRn.setStatus("current")
_CfprDcxVcAdminState_Type = CfprDcxAdminState
_CfprDcxVcAdminState_Object = MibTableColumn
cfprDcxVcAdminState = _CfprDcxVcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 4),
    _CfprDcxVcAdminState_Type()
)
cfprDcxVcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcAdminState.setStatus("current")
_CfprDcxVcAllowDtagVlan_Type = TruthValue
_CfprDcxVcAllowDtagVlan_Object = MibTableColumn
cfprDcxVcAllowDtagVlan = _CfprDcxVcAllowDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 5),
    _CfprDcxVcAllowDtagVlan_Type()
)
cfprDcxVcAllowDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcAllowDtagVlan.setStatus("current")
_CfprDcxVcBorderAggrPortId_Type = Gauge32
_CfprDcxVcBorderAggrPortId_Object = MibTableColumn
cfprDcxVcBorderAggrPortId = _CfprDcxVcBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 6),
    _CfprDcxVcBorderAggrPortId_Type()
)
cfprDcxVcBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcBorderAggrPortId.setStatus("current")
_CfprDcxVcBorderPortId_Type = Gauge32
_CfprDcxVcBorderPortId_Object = MibTableColumn
cfprDcxVcBorderPortId = _CfprDcxVcBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 7),
    _CfprDcxVcBorderPortId_Type()
)
cfprDcxVcBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcBorderPortId.setStatus("current")
_CfprDcxVcBorderSlotId_Type = Gauge32
_CfprDcxVcBorderSlotId_Object = MibTableColumn
cfprDcxVcBorderSlotId = _CfprDcxVcBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 8),
    _CfprDcxVcBorderSlotId_Type()
)
cfprDcxVcBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcBorderSlotId.setStatus("current")
_CfprDcxVcBorderVfcId_Type = Gauge32
_CfprDcxVcBorderVfcId_Object = MibTableColumn
cfprDcxVcBorderVfcId = _CfprDcxVcBorderVfcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 9),
    _CfprDcxVcBorderVfcId_Type()
)
cfprDcxVcBorderVfcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcBorderVfcId.setStatus("current")
_CfprDcxVcCdp_Type = CfprNwctrlAdminState
_CfprDcxVcCdp_Object = MibTableColumn
cfprDcxVcCdp = _CfprDcxVcCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 10),
    _CfprDcxVcCdp_Type()
)
cfprDcxVcCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcCdp.setStatus("current")
_CfprDcxVcCookie_Type = Unsigned64
_CfprDcxVcCookie_Object = MibTableColumn
cfprDcxVcCookie = _CfprDcxVcCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 11),
    _CfprDcxVcCookie_Type()
)
cfprDcxVcCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcCookie.setStatus("current")
_CfprDcxVcCos_Type = Gauge32
_CfprDcxVcCos_Object = MibTableColumn
cfprDcxVcCos = _CfprDcxVcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 12),
    _CfprDcxVcCos_Type()
)
cfprDcxVcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcCos.setStatus("current")
_CfprDcxVcDerivedFromId_Type = Gauge32
_CfprDcxVcDerivedFromId_Object = MibTableColumn
cfprDcxVcDerivedFromId = _CfprDcxVcDerivedFromId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 13),
    _CfprDcxVcDerivedFromId_Type()
)
cfprDcxVcDerivedFromId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcDerivedFromId.setStatus("current")
_CfprDcxVcEncap_Type = Gauge32
_CfprDcxVcEncap_Object = MibTableColumn
cfprDcxVcEncap = _CfprDcxVcEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 14),
    _CfprDcxVcEncap_Type()
)
cfprDcxVcEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcEncap.setStatus("current")
_CfprDcxVcFcoeId_Type = Gauge32
_CfprDcxVcFcoeId_Object = MibTableColumn
cfprDcxVcFcoeId = _CfprDcxVcFcoeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 15),
    _CfprDcxVcFcoeId_Type()
)
cfprDcxVcFcoeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcFcoeId.setStatus("current")
_CfprDcxVcFltAggr_Type = Unsigned64
_CfprDcxVcFltAggr_Object = MibTableColumn
cfprDcxVcFltAggr = _CfprDcxVcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 16),
    _CfprDcxVcFltAggr_Type()
)
cfprDcxVcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcFltAggr.setStatus("current")
_CfprDcxVcForgeMac_Type = CfprDpsecForgedTransmit
_CfprDcxVcForgeMac_Object = MibTableColumn
cfprDcxVcForgeMac = _CfprDcxVcForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 17),
    _CfprDcxVcForgeMac_Type()
)
cfprDcxVcForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcForgeMac.setStatus("current")
_CfprDcxVcId_Type = Gauge32
_CfprDcxVcId_Object = MibTableColumn
cfprDcxVcId = _CfprDcxVcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 18),
    _CfprDcxVcId_Type()
)
cfprDcxVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcId.setStatus("current")
_CfprDcxVcInstType_Type = CfprVnicInstantiation
_CfprDcxVcInstType_Object = MibTableColumn
cfprDcxVcInstType = _CfprDcxVcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 19),
    _CfprDcxVcInstType_Type()
)
cfprDcxVcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcInstType.setStatus("current")
_CfprDcxVcLc_Type = CfprFsmLifecycle
_CfprDcxVcLc_Object = MibTableColumn
cfprDcxVcLc = _CfprDcxVcLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 20),
    _CfprDcxVcLc_Type()
)
cfprDcxVcLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcLc.setStatus("current")
_CfprDcxVcLinkState_Type = CfprAdaptorLinkState
_CfprDcxVcLinkState_Object = MibTableColumn
cfprDcxVcLinkState = _CfprDcxVcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 21),
    _CfprDcxVcLinkState_Type()
)
cfprDcxVcLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcLinkState.setStatus("current")
_CfprDcxVcLocale_Type = CfprNetworkLocale
_CfprDcxVcLocale_Object = MibTableColumn
cfprDcxVcLocale = _CfprDcxVcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 22),
    _CfprDcxVcLocale_Type()
)
cfprDcxVcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcLocale.setStatus("current")
_CfprDcxVcMacRegisterMode_Type = CfprNwctrlRegistrationMode
_CfprDcxVcMacRegisterMode_Object = MibTableColumn
cfprDcxVcMacRegisterMode = _CfprDcxVcMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 23),
    _CfprDcxVcMacRegisterMode_Type()
)
cfprDcxVcMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcMacRegisterMode.setStatus("current")
_CfprDcxVcMonTrafDir_Type = CfprFabricTrafficDirection
_CfprDcxVcMonTrafDir_Object = MibTableColumn
cfprDcxVcMonTrafDir = _CfprDcxVcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 24),
    _CfprDcxVcMonTrafDir_Type()
)
cfprDcxVcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcMonTrafDir.setStatus("current")
_CfprDcxVcName_Type = SnmpAdminString
_CfprDcxVcName_Object = MibTableColumn
cfprDcxVcName = _CfprDcxVcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 25),
    _CfprDcxVcName_Type()
)
cfprDcxVcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcName.setStatus("current")
_CfprDcxVcOperBorderAggrPortId_Type = Gauge32
_CfprDcxVcOperBorderAggrPortId_Object = MibTableColumn
cfprDcxVcOperBorderAggrPortId = _CfprDcxVcOperBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 26),
    _CfprDcxVcOperBorderAggrPortId_Type()
)
cfprDcxVcOperBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcOperBorderAggrPortId.setStatus("current")
_CfprDcxVcOperBorderPortId_Type = Gauge32
_CfprDcxVcOperBorderPortId_Object = MibTableColumn
cfprDcxVcOperBorderPortId = _CfprDcxVcOperBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 27),
    _CfprDcxVcOperBorderPortId_Type()
)
cfprDcxVcOperBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcOperBorderPortId.setStatus("current")
_CfprDcxVcOperBorderSlotId_Type = Gauge32
_CfprDcxVcOperBorderSlotId_Object = MibTableColumn
cfprDcxVcOperBorderSlotId = _CfprDcxVcOperBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 28),
    _CfprDcxVcOperBorderSlotId_Type()
)
cfprDcxVcOperBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcOperBorderSlotId.setStatus("current")
_CfprDcxVcOperState_Type = CfprDcxOperState
_CfprDcxVcOperState_Object = MibTableColumn
cfprDcxVcOperState = _CfprDcxVcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 29),
    _CfprDcxVcOperState_Type()
)
cfprDcxVcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcOperState.setStatus("current")
_CfprDcxVcPeerId_Type = Gauge32
_CfprDcxVcPeerId_Object = MibTableColumn
cfprDcxVcPeerId = _CfprDcxVcPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 30),
    _CfprDcxVcPeerId_Type()
)
cfprDcxVcPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcPeerId.setStatus("current")
_CfprDcxVcProtState_Type = CfprDcxProtState
_CfprDcxVcProtState_Object = MibTableColumn
cfprDcxVcProtState = _CfprDcxVcProtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 31),
    _CfprDcxVcProtState_Type()
)
cfprDcxVcProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcProtState.setStatus("current")
_CfprDcxVcQosPolicyDn_Type = SnmpAdminString
_CfprDcxVcQosPolicyDn_Object = MibTableColumn
cfprDcxVcQosPolicyDn = _CfprDcxVcQosPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 32),
    _CfprDcxVcQosPolicyDn_Type()
)
cfprDcxVcQosPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcQosPolicyDn.setStatus("current")
_CfprDcxVcQosPolicyId_Type = SnmpAdminString
_CfprDcxVcQosPolicyId_Object = MibTableColumn
cfprDcxVcQosPolicyId = _CfprDcxVcQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 33),
    _CfprDcxVcQosPolicyId_Type()
)
cfprDcxVcQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcQosPolicyId.setStatus("current")
_CfprDcxVcRole_Type = CfprNetworkPortRole
_CfprDcxVcRole_Object = MibTableColumn
cfprDcxVcRole = _CfprDcxVcRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 34),
    _CfprDcxVcRole_Type()
)
cfprDcxVcRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcRole.setStatus("current")
_CfprDcxVcState_Type = CfprDcxState
_CfprDcxVcState_Object = MibTableColumn
cfprDcxVcState = _CfprDcxVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 35),
    _CfprDcxVcState_Type()
)
cfprDcxVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcState.setStatus("current")
_CfprDcxVcStateQual_Type = SnmpAdminString
_CfprDcxVcStateQual_Object = MibTableColumn
cfprDcxVcStateQual = _CfprDcxVcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 36),
    _CfprDcxVcStateQual_Type()
)
cfprDcxVcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcStateQual.setStatus("current")
_CfprDcxVcSwitchId_Type = CfprNetworkSwitchId
_CfprDcxVcSwitchId_Object = MibTableColumn
cfprDcxVcSwitchId = _CfprDcxVcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 37),
    _CfprDcxVcSwitchId_Type()
)
cfprDcxVcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcSwitchId.setStatus("current")
_CfprDcxVcTag_Type = Gauge32
_CfprDcxVcTag_Object = MibTableColumn
cfprDcxVcTag = _CfprDcxVcTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 38),
    _CfprDcxVcTag_Type()
)
cfprDcxVcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcTag.setStatus("current")
_CfprDcxVcTransport_Type = CfprNetworkTransport
_CfprDcxVcTransport_Object = MibTableColumn
cfprDcxVcTransport = _CfprDcxVcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 39),
    _CfprDcxVcTransport_Type()
)
cfprDcxVcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcTransport.setStatus("current")
_CfprDcxVcType_Type = CfprNetworkConnectionType
_CfprDcxVcType_Object = MibTableColumn
cfprDcxVcType = _CfprDcxVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 40),
    _CfprDcxVcType_Type()
)
cfprDcxVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcType.setStatus("current")
_CfprDcxVcUplinkFailAction_Type = CfprNwctrlLinkFailAction
_CfprDcxVcUplinkFailAction_Object = MibTableColumn
cfprDcxVcUplinkFailAction = _CfprDcxVcUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 41),
    _CfprDcxVcUplinkFailAction_Type()
)
cfprDcxVcUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcUplinkFailAction.setStatus("current")
_CfprDcxVcVnic_Type = SnmpAdminString
_CfprDcxVcVnic_Object = MibTableColumn
cfprDcxVcVnic = _CfprDcxVcVnic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 42),
    _CfprDcxVcVnic_Type()
)
cfprDcxVcVnic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcVnic.setStatus("current")
_CfprDcxVcServiceState_Type = CfprAdaptorServiceState
_CfprDcxVcServiceState_Object = MibTableColumn
cfprDcxVcServiceState = _CfprDcxVcServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 5, 1, 43),
    _CfprDcxVcServiceState_Type()
)
cfprDcxVcServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVcServiceState.setStatus("current")
_CfprDcxVifEpTable_Object = MibTable
cfprDcxVifEpTable = _CfprDcxVifEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 6)
)
if mibBuilder.loadTexts:
    cfprDcxVifEpTable.setStatus("current")
_CfprDcxVifEpEntry_Object = MibTableRow
cfprDcxVifEpEntry = _CfprDcxVifEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 6, 1)
)
cfprDcxVifEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DCX-MIB", "cfprDcxVifEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDcxVifEpEntry.setStatus("current")
_CfprDcxVifEpInstanceId_Type = CfprManagedObjectId
_CfprDcxVifEpInstanceId_Object = MibTableColumn
cfprDcxVifEpInstanceId = _CfprDcxVifEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 6, 1, 1),
    _CfprDcxVifEpInstanceId_Type()
)
cfprDcxVifEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDcxVifEpInstanceId.setStatus("current")
_CfprDcxVifEpDn_Type = CfprManagedObjectDn
_CfprDcxVifEpDn_Object = MibTableColumn
cfprDcxVifEpDn = _CfprDcxVifEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 6, 1, 2),
    _CfprDcxVifEpDn_Type()
)
cfprDcxVifEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVifEpDn.setStatus("current")
_CfprDcxVifEpRn_Type = SnmpAdminString
_CfprDcxVifEpRn_Object = MibTableColumn
cfprDcxVifEpRn = _CfprDcxVifEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 6, 1, 3),
    _CfprDcxVifEpRn_Type()
)
cfprDcxVifEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVifEpRn.setStatus("current")
_CfprDcxVifEpId_Type = Gauge32
_CfprDcxVifEpId_Object = MibTableColumn
cfprDcxVifEpId = _CfprDcxVifEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 14, 6, 1, 4),
    _CfprDcxVifEpId_Type()
)
cfprDcxVifEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDcxVifEpId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-DCX-MIB",
    **{"cfprDcxObjects": cfprDcxObjects,
       "cfprDcxFcoeVifEpTable": cfprDcxFcoeVifEpTable,
       "cfprDcxFcoeVifEpEntry": cfprDcxFcoeVifEpEntry,
       "cfprDcxFcoeVifEpInstanceId": cfprDcxFcoeVifEpInstanceId,
       "cfprDcxFcoeVifEpDn": cfprDcxFcoeVifEpDn,
       "cfprDcxFcoeVifEpRn": cfprDcxFcoeVifEpRn,
       "cfprDcxFcoeVifEpId": cfprDcxFcoeVifEpId,
       "cfprDcxNsTable": cfprDcxNsTable,
       "cfprDcxNsEntry": cfprDcxNsEntry,
       "cfprDcxNsInstanceId": cfprDcxNsInstanceId,
       "cfprDcxNsDn": cfprDcxNsDn,
       "cfprDcxNsRn": cfprDcxNsRn,
       "cfprDcxNsAllocStatus": cfprDcxNsAllocStatus,
       "cfprDcxNsSide": cfprDcxNsSide,
       "cfprDcxNsSize": cfprDcxNsSize,
       "cfprDcxNsSwitchId": cfprDcxNsSwitchId,
       "cfprDcxNsUsed": cfprDcxNsUsed,
       "cfprDcxUniverseTable": cfprDcxUniverseTable,
       "cfprDcxUniverseEntry": cfprDcxUniverseEntry,
       "cfprDcxUniverseInstanceId": cfprDcxUniverseInstanceId,
       "cfprDcxUniverseDn": cfprDcxUniverseDn,
       "cfprDcxUniverseRn": cfprDcxUniverseRn,
       "cfprDcxVIfTable": cfprDcxVIfTable,
       "cfprDcxVIfEntry": cfprDcxVIfEntry,
       "cfprDcxVIfInstanceId": cfprDcxVIfInstanceId,
       "cfprDcxVIfDn": cfprDcxVIfDn,
       "cfprDcxVIfRn": cfprDcxVIfRn,
       "cfprDcxVIfAdminState": cfprDcxVIfAdminState,
       "cfprDcxVIfCookie": cfprDcxVIfCookie,
       "cfprDcxVIfEpDn": cfprDcxVIfEpDn,
       "cfprDcxVIfId": cfprDcxVIfId,
       "cfprDcxVIfIfRole": cfprDcxVIfIfRole,
       "cfprDcxVIfIfType": cfprDcxVIfIfType,
       "cfprDcxVIfInstType": cfprDcxVIfInstType,
       "cfprDcxVIfLc": cfprDcxVIfLc,
       "cfprDcxVIfLinkState": cfprDcxVIfLinkState,
       "cfprDcxVIfLocale": cfprDcxVIfLocale,
       "cfprDcxVIfName": cfprDcxVIfName,
       "cfprDcxVIfOperState": cfprDcxVIfOperState,
       "cfprDcxVIfPeerDn": cfprDcxVIfPeerDn,
       "cfprDcxVIfProtPeerId": cfprDcxVIfProtPeerId,
       "cfprDcxVIfProtRole": cfprDcxVIfProtRole,
       "cfprDcxVIfProtState": cfprDcxVIfProtState,
       "cfprDcxVIfQosControl": cfprDcxVIfQosControl,
       "cfprDcxVIfState": cfprDcxVIfState,
       "cfprDcxVIfSwitchId": cfprDcxVIfSwitchId,
       "cfprDcxVIfTag": cfprDcxVIfTag,
       "cfprDcxVIfTransport": cfprDcxVIfTransport,
       "cfprDcxVIfType": cfprDcxVIfType,
       "cfprDcxVIfServiceState": cfprDcxVIfServiceState,
       "cfprDcxVIfVcAdminState": cfprDcxVIfVcAdminState,
       "cfprDcxVcTable": cfprDcxVcTable,
       "cfprDcxVcEntry": cfprDcxVcEntry,
       "cfprDcxVcInstanceId": cfprDcxVcInstanceId,
       "cfprDcxVcDn": cfprDcxVcDn,
       "cfprDcxVcRn": cfprDcxVcRn,
       "cfprDcxVcAdminState": cfprDcxVcAdminState,
       "cfprDcxVcAllowDtagVlan": cfprDcxVcAllowDtagVlan,
       "cfprDcxVcBorderAggrPortId": cfprDcxVcBorderAggrPortId,
       "cfprDcxVcBorderPortId": cfprDcxVcBorderPortId,
       "cfprDcxVcBorderSlotId": cfprDcxVcBorderSlotId,
       "cfprDcxVcBorderVfcId": cfprDcxVcBorderVfcId,
       "cfprDcxVcCdp": cfprDcxVcCdp,
       "cfprDcxVcCookie": cfprDcxVcCookie,
       "cfprDcxVcCos": cfprDcxVcCos,
       "cfprDcxVcDerivedFromId": cfprDcxVcDerivedFromId,
       "cfprDcxVcEncap": cfprDcxVcEncap,
       "cfprDcxVcFcoeId": cfprDcxVcFcoeId,
       "cfprDcxVcFltAggr": cfprDcxVcFltAggr,
       "cfprDcxVcForgeMac": cfprDcxVcForgeMac,
       "cfprDcxVcId": cfprDcxVcId,
       "cfprDcxVcInstType": cfprDcxVcInstType,
       "cfprDcxVcLc": cfprDcxVcLc,
       "cfprDcxVcLinkState": cfprDcxVcLinkState,
       "cfprDcxVcLocale": cfprDcxVcLocale,
       "cfprDcxVcMacRegisterMode": cfprDcxVcMacRegisterMode,
       "cfprDcxVcMonTrafDir": cfprDcxVcMonTrafDir,
       "cfprDcxVcName": cfprDcxVcName,
       "cfprDcxVcOperBorderAggrPortId": cfprDcxVcOperBorderAggrPortId,
       "cfprDcxVcOperBorderPortId": cfprDcxVcOperBorderPortId,
       "cfprDcxVcOperBorderSlotId": cfprDcxVcOperBorderSlotId,
       "cfprDcxVcOperState": cfprDcxVcOperState,
       "cfprDcxVcPeerId": cfprDcxVcPeerId,
       "cfprDcxVcProtState": cfprDcxVcProtState,
       "cfprDcxVcQosPolicyDn": cfprDcxVcQosPolicyDn,
       "cfprDcxVcQosPolicyId": cfprDcxVcQosPolicyId,
       "cfprDcxVcRole": cfprDcxVcRole,
       "cfprDcxVcState": cfprDcxVcState,
       "cfprDcxVcStateQual": cfprDcxVcStateQual,
       "cfprDcxVcSwitchId": cfprDcxVcSwitchId,
       "cfprDcxVcTag": cfprDcxVcTag,
       "cfprDcxVcTransport": cfprDcxVcTransport,
       "cfprDcxVcType": cfprDcxVcType,
       "cfprDcxVcUplinkFailAction": cfprDcxVcUplinkFailAction,
       "cfprDcxVcVnic": cfprDcxVcVnic,
       "cfprDcxVcServiceState": cfprDcxVcServiceState,
       "cfprDcxVifEpTable": cfprDcxVifEpTable,
       "cfprDcxVifEpEntry": cfprDcxVifEpEntry,
       "cfprDcxVifEpInstanceId": cfprDcxVifEpInstanceId,
       "cfprDcxVifEpDn": cfprDcxVifEpDn,
       "cfprDcxVifEpRn": cfprDcxVifEpRn,
       "cfprDcxVifEpId": cfprDcxVifEpId}
)
