# SNMP MIB module (CISCO-FIREPOWER-AP-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-NETWORK-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:14 2025
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

(CfprApEquipmentSensorThresholdStatus,
 CfprApMgmtAdminState,
 CfprApNetworkElementOperability,
 CfprApNetworkIfStatsType,
 CfprApNetworkIfStatsUnits,
 CfprApNetworkInventoryStatus,
 CfprApNetworkSwitchId,
 CfprApNetworkVlanCountStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApEquipmentSensorThresholdStatus",
    "CfprApMgmtAdminState",
    "CfprApNetworkElementOperability",
    "CfprApNetworkIfStatsType",
    "CfprApNetworkIfStatsUnits",
    "CfprApNetworkInventoryStatus",
    "CfprApNetworkSwitchId",
    "CfprApNetworkVlanCountStatus")

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

cfprApNetworkObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApNetworkElementTable_Object = MibTable
cfprApNetworkElementTable = _CfprApNetworkElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1)
)
if mibBuilder.loadTexts:
    cfprApNetworkElementTable.setStatus("current")
_CfprApNetworkElementEntry_Object = MibTableRow
cfprApNetworkElementEntry = _CfprApNetworkElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1)
)
cfprApNetworkElementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkElementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkElementEntry.setStatus("current")
_CfprApNetworkElementInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkElementInstanceId_Object = MibTableColumn
cfprApNetworkElementInstanceId = _CfprApNetworkElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 1),
    _CfprApNetworkElementInstanceId_Type()
)
cfprApNetworkElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkElementInstanceId.setStatus("current")
_CfprApNetworkElementDn_Type = CfprApManagedObjectDn
_CfprApNetworkElementDn_Object = MibTableColumn
cfprApNetworkElementDn = _CfprApNetworkElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 2),
    _CfprApNetworkElementDn_Type()
)
cfprApNetworkElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementDn.setStatus("current")
_CfprApNetworkElementRn_Type = SnmpAdminString
_CfprApNetworkElementRn_Object = MibTableColumn
cfprApNetworkElementRn = _CfprApNetworkElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 3),
    _CfprApNetworkElementRn_Type()
)
cfprApNetworkElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementRn.setStatus("current")
_CfprApNetworkElementAdminInbandIfState_Type = CfprApMgmtAdminState
_CfprApNetworkElementAdminInbandIfState_Object = MibTableColumn
cfprApNetworkElementAdminInbandIfState = _CfprApNetworkElementAdminInbandIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 4),
    _CfprApNetworkElementAdminInbandIfState_Type()
)
cfprApNetworkElementAdminInbandIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementAdminInbandIfState.setStatus("current")
_CfprApNetworkElementDiffMemory_Type = Gauge32
_CfprApNetworkElementDiffMemory_Object = MibTableColumn
cfprApNetworkElementDiffMemory = _CfprApNetworkElementDiffMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 5),
    _CfprApNetworkElementDiffMemory_Type()
)
cfprApNetworkElementDiffMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementDiffMemory.setStatus("current")
_CfprApNetworkElementExpectedMemory_Type = Gauge32
_CfprApNetworkElementExpectedMemory_Object = MibTableColumn
cfprApNetworkElementExpectedMemory = _CfprApNetworkElementExpectedMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 6),
    _CfprApNetworkElementExpectedMemory_Type()
)
cfprApNetworkElementExpectedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementExpectedMemory.setStatus("current")
_CfprApNetworkElementFltAggr_Type = Unsigned64
_CfprApNetworkElementFltAggr_Object = MibTableColumn
cfprApNetworkElementFltAggr = _CfprApNetworkElementFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 7),
    _CfprApNetworkElementFltAggr_Type()
)
cfprApNetworkElementFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementFltAggr.setStatus("current")
_CfprApNetworkElementId_Type = CfprApNetworkSwitchId
_CfprApNetworkElementId_Object = MibTableColumn
cfprApNetworkElementId = _CfprApNetworkElementId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 8),
    _CfprApNetworkElementId_Type()
)
cfprApNetworkElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementId.setStatus("current")
_CfprApNetworkElementInbandIfGw_Type = InetAddressIPv4
_CfprApNetworkElementInbandIfGw_Object = MibTableColumn
cfprApNetworkElementInbandIfGw = _CfprApNetworkElementInbandIfGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 9),
    _CfprApNetworkElementInbandIfGw_Type()
)
cfprApNetworkElementInbandIfGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementInbandIfGw.setStatus("current")
_CfprApNetworkElementInbandIfIp_Type = InetAddressIPv4
_CfprApNetworkElementInbandIfIp_Object = MibTableColumn
cfprApNetworkElementInbandIfIp = _CfprApNetworkElementInbandIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 10),
    _CfprApNetworkElementInbandIfIp_Type()
)
cfprApNetworkElementInbandIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementInbandIfIp.setStatus("current")
_CfprApNetworkElementInbandIfMask_Type = InetAddressIPv4
_CfprApNetworkElementInbandIfMask_Object = MibTableColumn
cfprApNetworkElementInbandIfMask = _CfprApNetworkElementInbandIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 11),
    _CfprApNetworkElementInbandIfMask_Type()
)
cfprApNetworkElementInbandIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementInbandIfMask.setStatus("current")
_CfprApNetworkElementInbandIfVnet_Type = Gauge32
_CfprApNetworkElementInbandIfVnet_Object = MibTableColumn
cfprApNetworkElementInbandIfVnet = _CfprApNetworkElementInbandIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 12),
    _CfprApNetworkElementInbandIfVnet_Type()
)
cfprApNetworkElementInbandIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementInbandIfVnet.setStatus("current")
_CfprApNetworkElementInventoryStatus_Type = CfprApNetworkInventoryStatus
_CfprApNetworkElementInventoryStatus_Object = MibTableColumn
cfprApNetworkElementInventoryStatus = _CfprApNetworkElementInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 13),
    _CfprApNetworkElementInventoryStatus_Type()
)
cfprApNetworkElementInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementInventoryStatus.setStatus("current")
_CfprApNetworkElementModel_Type = SnmpAdminString
_CfprApNetworkElementModel_Object = MibTableColumn
cfprApNetworkElementModel = _CfprApNetworkElementModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 14),
    _CfprApNetworkElementModel_Type()
)
cfprApNetworkElementModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementModel.setStatus("current")
_CfprApNetworkElementOobIfGw_Type = InetAddressIPv4
_CfprApNetworkElementOobIfGw_Object = MibTableColumn
cfprApNetworkElementOobIfGw = _CfprApNetworkElementOobIfGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 15),
    _CfprApNetworkElementOobIfGw_Type()
)
cfprApNetworkElementOobIfGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementOobIfGw.setStatus("current")
_CfprApNetworkElementOobIfIp_Type = InetAddressIPv4
_CfprApNetworkElementOobIfIp_Object = MibTableColumn
cfprApNetworkElementOobIfIp = _CfprApNetworkElementOobIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 16),
    _CfprApNetworkElementOobIfIp_Type()
)
cfprApNetworkElementOobIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementOobIfIp.setStatus("current")
_CfprApNetworkElementOobIfMask_Type = InetAddressIPv4
_CfprApNetworkElementOobIfMask_Object = MibTableColumn
cfprApNetworkElementOobIfMask = _CfprApNetworkElementOobIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 17),
    _CfprApNetworkElementOobIfMask_Type()
)
cfprApNetworkElementOobIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementOobIfMask.setStatus("current")
_CfprApNetworkElementOperability_Type = CfprApNetworkElementOperability
_CfprApNetworkElementOperability_Object = MibTableColumn
cfprApNetworkElementOperability = _CfprApNetworkElementOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 18),
    _CfprApNetworkElementOperability_Type()
)
cfprApNetworkElementOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementOperability.setStatus("current")
_CfprApNetworkElementRevision_Type = SnmpAdminString
_CfprApNetworkElementRevision_Object = MibTableColumn
cfprApNetworkElementRevision = _CfprApNetworkElementRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 19),
    _CfprApNetworkElementRevision_Type()
)
cfprApNetworkElementRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementRevision.setStatus("current")
_CfprApNetworkElementSerial_Type = SnmpAdminString
_CfprApNetworkElementSerial_Object = MibTableColumn
cfprApNetworkElementSerial = _CfprApNetworkElementSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 20),
    _CfprApNetworkElementSerial_Type()
)
cfprApNetworkElementSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementSerial.setStatus("current")
_CfprApNetworkElementThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApNetworkElementThermal_Object = MibTableColumn
cfprApNetworkElementThermal = _CfprApNetworkElementThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 21),
    _CfprApNetworkElementThermal_Type()
)
cfprApNetworkElementThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementThermal.setStatus("current")
_CfprApNetworkElementTotalMemory_Type = Gauge32
_CfprApNetworkElementTotalMemory_Object = MibTableColumn
cfprApNetworkElementTotalMemory = _CfprApNetworkElementTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 22),
    _CfprApNetworkElementTotalMemory_Type()
)
cfprApNetworkElementTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementTotalMemory.setStatus("current")
_CfprApNetworkElementVendor_Type = SnmpAdminString
_CfprApNetworkElementVendor_Object = MibTableColumn
cfprApNetworkElementVendor = _CfprApNetworkElementVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 1, 1, 23),
    _CfprApNetworkElementVendor_Type()
)
cfprApNetworkElementVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkElementVendor.setStatus("current")
_CfprApNetworkIfStatsTable_Object = MibTable
cfprApNetworkIfStatsTable = _CfprApNetworkIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2)
)
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsTable.setStatus("current")
_CfprApNetworkIfStatsEntry_Object = MibTableRow
cfprApNetworkIfStatsEntry = _CfprApNetworkIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1)
)
cfprApNetworkIfStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkIfStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsEntry.setStatus("current")
_CfprApNetworkIfStatsInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkIfStatsInstanceId_Object = MibTableColumn
cfprApNetworkIfStatsInstanceId = _CfprApNetworkIfStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 1),
    _CfprApNetworkIfStatsInstanceId_Type()
)
cfprApNetworkIfStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsInstanceId.setStatus("current")
_CfprApNetworkIfStatsDn_Type = CfprApManagedObjectDn
_CfprApNetworkIfStatsDn_Object = MibTableColumn
cfprApNetworkIfStatsDn = _CfprApNetworkIfStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 2),
    _CfprApNetworkIfStatsDn_Type()
)
cfprApNetworkIfStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsDn.setStatus("current")
_CfprApNetworkIfStatsRn_Type = SnmpAdminString
_CfprApNetworkIfStatsRn_Object = MibTableColumn
cfprApNetworkIfStatsRn = _CfprApNetworkIfStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 3),
    _CfprApNetworkIfStatsRn_Type()
)
cfprApNetworkIfStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsRn.setStatus("current")
_CfprApNetworkIfStatsOut_Type = Unsigned64
_CfprApNetworkIfStatsOut_Object = MibTableColumn
cfprApNetworkIfStatsOut = _CfprApNetworkIfStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 4),
    _CfprApNetworkIfStatsOut_Type()
)
cfprApNetworkIfStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsOut.setStatus("current")
_CfprApNetworkIfStatsRin_Type = Unsigned64
_CfprApNetworkIfStatsRin_Object = MibTableColumn
cfprApNetworkIfStatsRin = _CfprApNetworkIfStatsRin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 5),
    _CfprApNetworkIfStatsRin_Type()
)
cfprApNetworkIfStatsRin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsRin.setStatus("current")
_CfprApNetworkIfStatsType_Type = CfprApNetworkIfStatsType
_CfprApNetworkIfStatsType_Object = MibTableColumn
cfprApNetworkIfStatsType = _CfprApNetworkIfStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 6),
    _CfprApNetworkIfStatsType_Type()
)
cfprApNetworkIfStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsType.setStatus("current")
_CfprApNetworkIfStatsUnits_Type = CfprApNetworkIfStatsUnits
_CfprApNetworkIfStatsUnits_Object = MibTableColumn
cfprApNetworkIfStatsUnits = _CfprApNetworkIfStatsUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 2, 1, 7),
    _CfprApNetworkIfStatsUnits_Type()
)
cfprApNetworkIfStatsUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkIfStatsUnits.setStatus("current")
_CfprApNetworkLanNeighborEntryTable_Object = MibTable
cfprApNetworkLanNeighborEntryTable = _CfprApNetworkLanNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3)
)
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryTable.setStatus("current")
_CfprApNetworkLanNeighborEntryEntry_Object = MibTableRow
cfprApNetworkLanNeighborEntryEntry = _CfprApNetworkLanNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1)
)
cfprApNetworkLanNeighborEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkLanNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryEntry.setStatus("current")
_CfprApNetworkLanNeighborEntryInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkLanNeighborEntryInstanceId_Object = MibTableColumn
cfprApNetworkLanNeighborEntryInstanceId = _CfprApNetworkLanNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 1),
    _CfprApNetworkLanNeighborEntryInstanceId_Type()
)
cfprApNetworkLanNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryInstanceId.setStatus("current")
_CfprApNetworkLanNeighborEntryDn_Type = CfprApManagedObjectDn
_CfprApNetworkLanNeighborEntryDn_Object = MibTableColumn
cfprApNetworkLanNeighborEntryDn = _CfprApNetworkLanNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 2),
    _CfprApNetworkLanNeighborEntryDn_Type()
)
cfprApNetworkLanNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryDn.setStatus("current")
_CfprApNetworkLanNeighborEntryRn_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryRn_Object = MibTableColumn
cfprApNetworkLanNeighborEntryRn = _CfprApNetworkLanNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 3),
    _CfprApNetworkLanNeighborEntryRn_Type()
)
cfprApNetworkLanNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryRn.setStatus("current")
_CfprApNetworkLanNeighborEntryCapabilities_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryCapabilities_Object = MibTableColumn
cfprApNetworkLanNeighborEntryCapabilities = _CfprApNetworkLanNeighborEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 4),
    _CfprApNetworkLanNeighborEntryCapabilities_Type()
)
cfprApNetworkLanNeighborEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryCapabilities.setStatus("current")
_CfprApNetworkLanNeighborEntryDeviceId_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryDeviceId_Object = MibTableColumn
cfprApNetworkLanNeighborEntryDeviceId = _CfprApNetworkLanNeighborEntryDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 5),
    _CfprApNetworkLanNeighborEntryDeviceId_Type()
)
cfprApNetworkLanNeighborEntryDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryDeviceId.setStatus("current")
_CfprApNetworkLanNeighborEntryFiPortDn_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryFiPortDn_Object = MibTableColumn
cfprApNetworkLanNeighborEntryFiPortDn = _CfprApNetworkLanNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 6),
    _CfprApNetworkLanNeighborEntryFiPortDn_Type()
)
cfprApNetworkLanNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryFiPortDn.setStatus("current")
_CfprApNetworkLanNeighborEntryIpV4Address_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryIpV4Address_Object = MibTableColumn
cfprApNetworkLanNeighborEntryIpV4Address = _CfprApNetworkLanNeighborEntryIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 7),
    _CfprApNetworkLanNeighborEntryIpV4Address_Type()
)
cfprApNetworkLanNeighborEntryIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryIpV4Address.setStatus("current")
_CfprApNetworkLanNeighborEntryIpV4MgmtAddress_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryIpV4MgmtAddress_Object = MibTableColumn
cfprApNetworkLanNeighborEntryIpV4MgmtAddress = _CfprApNetworkLanNeighborEntryIpV4MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 8),
    _CfprApNetworkLanNeighborEntryIpV4MgmtAddress_Type()
)
cfprApNetworkLanNeighborEntryIpV4MgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryIpV4MgmtAddress.setStatus("current")
_CfprApNetworkLanNeighborEntryLocalInterface_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryLocalInterface_Object = MibTableColumn
cfprApNetworkLanNeighborEntryLocalInterface = _CfprApNetworkLanNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 9),
    _CfprApNetworkLanNeighborEntryLocalInterface_Type()
)
cfprApNetworkLanNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryLocalInterface.setStatus("current")
_CfprApNetworkLanNeighborEntryNativeVlan_Type = Gauge32
_CfprApNetworkLanNeighborEntryNativeVlan_Object = MibTableColumn
cfprApNetworkLanNeighborEntryNativeVlan = _CfprApNetworkLanNeighborEntryNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 10),
    _CfprApNetworkLanNeighborEntryNativeVlan_Type()
)
cfprApNetworkLanNeighborEntryNativeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryNativeVlan.setStatus("current")
_CfprApNetworkLanNeighborEntryPlatform_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryPlatform_Object = MibTableColumn
cfprApNetworkLanNeighborEntryPlatform = _CfprApNetworkLanNeighborEntryPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 11),
    _CfprApNetworkLanNeighborEntryPlatform_Type()
)
cfprApNetworkLanNeighborEntryPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryPlatform.setStatus("current")
_CfprApNetworkLanNeighborEntryRemoteInterface_Type = SnmpAdminString
_CfprApNetworkLanNeighborEntryRemoteInterface_Object = MibTableColumn
cfprApNetworkLanNeighborEntryRemoteInterface = _CfprApNetworkLanNeighborEntryRemoteInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 3, 1, 12),
    _CfprApNetworkLanNeighborEntryRemoteInterface_Type()
)
cfprApNetworkLanNeighborEntryRemoteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborEntryRemoteInterface.setStatus("current")
_CfprApNetworkLanNeighborsTable_Object = MibTable
cfprApNetworkLanNeighborsTable = _CfprApNetworkLanNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 4)
)
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborsTable.setStatus("current")
_CfprApNetworkLanNeighborsEntry_Object = MibTableRow
cfprApNetworkLanNeighborsEntry = _CfprApNetworkLanNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 4, 1)
)
cfprApNetworkLanNeighborsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkLanNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborsEntry.setStatus("current")
_CfprApNetworkLanNeighborsInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkLanNeighborsInstanceId_Object = MibTableColumn
cfprApNetworkLanNeighborsInstanceId = _CfprApNetworkLanNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 4, 1, 1),
    _CfprApNetworkLanNeighborsInstanceId_Type()
)
cfprApNetworkLanNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborsInstanceId.setStatus("current")
_CfprApNetworkLanNeighborsDn_Type = CfprApManagedObjectDn
_CfprApNetworkLanNeighborsDn_Object = MibTableColumn
cfprApNetworkLanNeighborsDn = _CfprApNetworkLanNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 4, 1, 2),
    _CfprApNetworkLanNeighborsDn_Type()
)
cfprApNetworkLanNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborsDn.setStatus("current")
_CfprApNetworkLanNeighborsRn_Type = SnmpAdminString
_CfprApNetworkLanNeighborsRn_Object = MibTableColumn
cfprApNetworkLanNeighborsRn = _CfprApNetworkLanNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 4, 1, 3),
    _CfprApNetworkLanNeighborsRn_Type()
)
cfprApNetworkLanNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkLanNeighborsRn.setStatus("current")
_CfprApNetworkOperLevelTable_Object = MibTable
cfprApNetworkOperLevelTable = _CfprApNetworkOperLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5)
)
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelTable.setStatus("current")
_CfprApNetworkOperLevelEntry_Object = MibTableRow
cfprApNetworkOperLevelEntry = _CfprApNetworkOperLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1)
)
cfprApNetworkOperLevelEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkOperLevelInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelEntry.setStatus("current")
_CfprApNetworkOperLevelInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkOperLevelInstanceId_Object = MibTableColumn
cfprApNetworkOperLevelInstanceId = _CfprApNetworkOperLevelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 1),
    _CfprApNetworkOperLevelInstanceId_Type()
)
cfprApNetworkOperLevelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelInstanceId.setStatus("current")
_CfprApNetworkOperLevelDn_Type = CfprApManagedObjectDn
_CfprApNetworkOperLevelDn_Object = MibTableColumn
cfprApNetworkOperLevelDn = _CfprApNetworkOperLevelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 2),
    _CfprApNetworkOperLevelDn_Type()
)
cfprApNetworkOperLevelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelDn.setStatus("current")
_CfprApNetworkOperLevelRn_Type = SnmpAdminString
_CfprApNetworkOperLevelRn_Object = MibTableColumn
cfprApNetworkOperLevelRn = _CfprApNetworkOperLevelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 3),
    _CfprApNetworkOperLevelRn_Type()
)
cfprApNetworkOperLevelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelRn.setStatus("current")
_CfprApNetworkOperLevelId_Type = CfprApNetworkSwitchId
_CfprApNetworkOperLevelId_Object = MibTableColumn
cfprApNetworkOperLevelId = _CfprApNetworkOperLevelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 4),
    _CfprApNetworkOperLevelId_Type()
)
cfprApNetworkOperLevelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelId.setStatus("current")
_CfprApNetworkOperLevelMaxPrimaryVlanCount_Type = Gauge32
_CfprApNetworkOperLevelMaxPrimaryVlanCount_Object = MibTableColumn
cfprApNetworkOperLevelMaxPrimaryVlanCount = _CfprApNetworkOperLevelMaxPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 5),
    _CfprApNetworkOperLevelMaxPrimaryVlanCount_Type()
)
cfprApNetworkOperLevelMaxPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelMaxPrimaryVlanCount.setStatus("current")
_CfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type = Gauge32
_CfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object = MibTableColumn
cfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount = _CfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 6),
    _CfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type()
)
cfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setStatus("current")
_CfprApNetworkOperLevelMaxSecondaryVlanCount_Type = Gauge32
_CfprApNetworkOperLevelMaxSecondaryVlanCount_Object = MibTableColumn
cfprApNetworkOperLevelMaxSecondaryVlanCount = _CfprApNetworkOperLevelMaxSecondaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 7),
    _CfprApNetworkOperLevelMaxSecondaryVlanCount_Type()
)
cfprApNetworkOperLevelMaxSecondaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelMaxSecondaryVlanCount.setStatus("current")
_CfprApNetworkOperLevelPrimaryVlanCount_Type = Gauge32
_CfprApNetworkOperLevelPrimaryVlanCount_Object = MibTableColumn
cfprApNetworkOperLevelPrimaryVlanCount = _CfprApNetworkOperLevelPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 8),
    _CfprApNetworkOperLevelPrimaryVlanCount_Type()
)
cfprApNetworkOperLevelPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelPrimaryVlanCount.setStatus("current")
_CfprApNetworkOperLevelPrimaryVlanCountStatus_Type = CfprApNetworkVlanCountStatus
_CfprApNetworkOperLevelPrimaryVlanCountStatus_Object = MibTableColumn
cfprApNetworkOperLevelPrimaryVlanCountStatus = _CfprApNetworkOperLevelPrimaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 9),
    _CfprApNetworkOperLevelPrimaryVlanCountStatus_Type()
)
cfprApNetworkOperLevelPrimaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelPrimaryVlanCountStatus.setStatus("current")
_CfprApNetworkOperLevelSecondaryVlanCount_Type = Gauge32
_CfprApNetworkOperLevelSecondaryVlanCount_Object = MibTableColumn
cfprApNetworkOperLevelSecondaryVlanCount = _CfprApNetworkOperLevelSecondaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 10),
    _CfprApNetworkOperLevelSecondaryVlanCount_Type()
)
cfprApNetworkOperLevelSecondaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelSecondaryVlanCount.setStatus("current")
_CfprApNetworkOperLevelSecondaryVlanCountStatus_Type = CfprApNetworkVlanCountStatus
_CfprApNetworkOperLevelSecondaryVlanCountStatus_Object = MibTableColumn
cfprApNetworkOperLevelSecondaryVlanCountStatus = _CfprApNetworkOperLevelSecondaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 5, 1, 11),
    _CfprApNetworkOperLevelSecondaryVlanCountStatus_Type()
)
cfprApNetworkOperLevelSecondaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkOperLevelSecondaryVlanCountStatus.setStatus("current")
_CfprApNetworkSanNeighborEntryTable_Object = MibTable
cfprApNetworkSanNeighborEntryTable = _CfprApNetworkSanNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6)
)
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryTable.setStatus("current")
_CfprApNetworkSanNeighborEntryEntry_Object = MibTableRow
cfprApNetworkSanNeighborEntryEntry = _CfprApNetworkSanNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1)
)
cfprApNetworkSanNeighborEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkSanNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryEntry.setStatus("current")
_CfprApNetworkSanNeighborEntryInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkSanNeighborEntryInstanceId_Object = MibTableColumn
cfprApNetworkSanNeighborEntryInstanceId = _CfprApNetworkSanNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 1),
    _CfprApNetworkSanNeighborEntryInstanceId_Type()
)
cfprApNetworkSanNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryInstanceId.setStatus("current")
_CfprApNetworkSanNeighborEntryDn_Type = CfprApManagedObjectDn
_CfprApNetworkSanNeighborEntryDn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryDn = _CfprApNetworkSanNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 2),
    _CfprApNetworkSanNeighborEntryDn_Type()
)
cfprApNetworkSanNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryDn.setStatus("current")
_CfprApNetworkSanNeighborEntryRn_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryRn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryRn = _CfprApNetworkSanNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 3),
    _CfprApNetworkSanNeighborEntryRn_Type()
)
cfprApNetworkSanNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryRn.setStatus("current")
_CfprApNetworkSanNeighborEntryFabricMgmtAddr_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryFabricMgmtAddr_Object = MibTableColumn
cfprApNetworkSanNeighborEntryFabricMgmtAddr = _CfprApNetworkSanNeighborEntryFabricMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 4),
    _CfprApNetworkSanNeighborEntryFabricMgmtAddr_Type()
)
cfprApNetworkSanNeighborEntryFabricMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryFabricMgmtAddr.setStatus("current")
_CfprApNetworkSanNeighborEntryFabricNwwn_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryFabricNwwn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryFabricNwwn = _CfprApNetworkSanNeighborEntryFabricNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 5),
    _CfprApNetworkSanNeighborEntryFabricNwwn_Type()
)
cfprApNetworkSanNeighborEntryFabricNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryFabricNwwn.setStatus("current")
_CfprApNetworkSanNeighborEntryFabricPwwn_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryFabricPwwn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryFabricPwwn = _CfprApNetworkSanNeighborEntryFabricPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 6),
    _CfprApNetworkSanNeighborEntryFabricPwwn_Type()
)
cfprApNetworkSanNeighborEntryFabricPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryFabricPwwn.setStatus("current")
_CfprApNetworkSanNeighborEntryFiPortDn_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryFiPortDn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryFiPortDn = _CfprApNetworkSanNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 7),
    _CfprApNetworkSanNeighborEntryFiPortDn_Type()
)
cfprApNetworkSanNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryFiPortDn.setStatus("current")
_CfprApNetworkSanNeighborEntryLocalInterface_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryLocalInterface_Object = MibTableColumn
cfprApNetworkSanNeighborEntryLocalInterface = _CfprApNetworkSanNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 8),
    _CfprApNetworkSanNeighborEntryLocalInterface_Type()
)
cfprApNetworkSanNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryLocalInterface.setStatus("current")
_CfprApNetworkSanNeighborEntryMyNwwn_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryMyNwwn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryMyNwwn = _CfprApNetworkSanNeighborEntryMyNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 9),
    _CfprApNetworkSanNeighborEntryMyNwwn_Type()
)
cfprApNetworkSanNeighborEntryMyNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryMyNwwn.setStatus("current")
_CfprApNetworkSanNeighborEntryMyPwwn_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryMyPwwn_Object = MibTableColumn
cfprApNetworkSanNeighborEntryMyPwwn = _CfprApNetworkSanNeighborEntryMyPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 10),
    _CfprApNetworkSanNeighborEntryMyPwwn_Type()
)
cfprApNetworkSanNeighborEntryMyPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryMyPwwn.setStatus("current")
_CfprApNetworkSanNeighborEntryPortVsan_Type = SnmpAdminString
_CfprApNetworkSanNeighborEntryPortVsan_Object = MibTableColumn
cfprApNetworkSanNeighborEntryPortVsan = _CfprApNetworkSanNeighborEntryPortVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 6, 1, 11),
    _CfprApNetworkSanNeighborEntryPortVsan_Type()
)
cfprApNetworkSanNeighborEntryPortVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborEntryPortVsan.setStatus("current")
_CfprApNetworkSanNeighborsTable_Object = MibTable
cfprApNetworkSanNeighborsTable = _CfprApNetworkSanNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 7)
)
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborsTable.setStatus("current")
_CfprApNetworkSanNeighborsEntry_Object = MibTableRow
cfprApNetworkSanNeighborsEntry = _CfprApNetworkSanNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 7, 1)
)
cfprApNetworkSanNeighborsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-NETWORK-MIB", "cfprApNetworkSanNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborsEntry.setStatus("current")
_CfprApNetworkSanNeighborsInstanceId_Type = CfprApManagedObjectId
_CfprApNetworkSanNeighborsInstanceId_Object = MibTableColumn
cfprApNetworkSanNeighborsInstanceId = _CfprApNetworkSanNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 7, 1, 1),
    _CfprApNetworkSanNeighborsInstanceId_Type()
)
cfprApNetworkSanNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborsInstanceId.setStatus("current")
_CfprApNetworkSanNeighborsDn_Type = CfprApManagedObjectDn
_CfprApNetworkSanNeighborsDn_Object = MibTableColumn
cfprApNetworkSanNeighborsDn = _CfprApNetworkSanNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 7, 1, 2),
    _CfprApNetworkSanNeighborsDn_Type()
)
cfprApNetworkSanNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborsDn.setStatus("current")
_CfprApNetworkSanNeighborsRn_Type = SnmpAdminString
_CfprApNetworkSanNeighborsRn_Object = MibTableColumn
cfprApNetworkSanNeighborsRn = _CfprApNetworkSanNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 52, 7, 1, 3),
    _CfprApNetworkSanNeighborsRn_Type()
)
cfprApNetworkSanNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApNetworkSanNeighborsRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-NETWORK-MIB",
    **{"cfprApNetworkObjects": cfprApNetworkObjects,
       "cfprApNetworkElementTable": cfprApNetworkElementTable,
       "cfprApNetworkElementEntry": cfprApNetworkElementEntry,
       "cfprApNetworkElementInstanceId": cfprApNetworkElementInstanceId,
       "cfprApNetworkElementDn": cfprApNetworkElementDn,
       "cfprApNetworkElementRn": cfprApNetworkElementRn,
       "cfprApNetworkElementAdminInbandIfState": cfprApNetworkElementAdminInbandIfState,
       "cfprApNetworkElementDiffMemory": cfprApNetworkElementDiffMemory,
       "cfprApNetworkElementExpectedMemory": cfprApNetworkElementExpectedMemory,
       "cfprApNetworkElementFltAggr": cfprApNetworkElementFltAggr,
       "cfprApNetworkElementId": cfprApNetworkElementId,
       "cfprApNetworkElementInbandIfGw": cfprApNetworkElementInbandIfGw,
       "cfprApNetworkElementInbandIfIp": cfprApNetworkElementInbandIfIp,
       "cfprApNetworkElementInbandIfMask": cfprApNetworkElementInbandIfMask,
       "cfprApNetworkElementInbandIfVnet": cfprApNetworkElementInbandIfVnet,
       "cfprApNetworkElementInventoryStatus": cfprApNetworkElementInventoryStatus,
       "cfprApNetworkElementModel": cfprApNetworkElementModel,
       "cfprApNetworkElementOobIfGw": cfprApNetworkElementOobIfGw,
       "cfprApNetworkElementOobIfIp": cfprApNetworkElementOobIfIp,
       "cfprApNetworkElementOobIfMask": cfprApNetworkElementOobIfMask,
       "cfprApNetworkElementOperability": cfprApNetworkElementOperability,
       "cfprApNetworkElementRevision": cfprApNetworkElementRevision,
       "cfprApNetworkElementSerial": cfprApNetworkElementSerial,
       "cfprApNetworkElementThermal": cfprApNetworkElementThermal,
       "cfprApNetworkElementTotalMemory": cfprApNetworkElementTotalMemory,
       "cfprApNetworkElementVendor": cfprApNetworkElementVendor,
       "cfprApNetworkIfStatsTable": cfprApNetworkIfStatsTable,
       "cfprApNetworkIfStatsEntry": cfprApNetworkIfStatsEntry,
       "cfprApNetworkIfStatsInstanceId": cfprApNetworkIfStatsInstanceId,
       "cfprApNetworkIfStatsDn": cfprApNetworkIfStatsDn,
       "cfprApNetworkIfStatsRn": cfprApNetworkIfStatsRn,
       "cfprApNetworkIfStatsOut": cfprApNetworkIfStatsOut,
       "cfprApNetworkIfStatsRin": cfprApNetworkIfStatsRin,
       "cfprApNetworkIfStatsType": cfprApNetworkIfStatsType,
       "cfprApNetworkIfStatsUnits": cfprApNetworkIfStatsUnits,
       "cfprApNetworkLanNeighborEntryTable": cfprApNetworkLanNeighborEntryTable,
       "cfprApNetworkLanNeighborEntryEntry": cfprApNetworkLanNeighborEntryEntry,
       "cfprApNetworkLanNeighborEntryInstanceId": cfprApNetworkLanNeighborEntryInstanceId,
       "cfprApNetworkLanNeighborEntryDn": cfprApNetworkLanNeighborEntryDn,
       "cfprApNetworkLanNeighborEntryRn": cfprApNetworkLanNeighborEntryRn,
       "cfprApNetworkLanNeighborEntryCapabilities": cfprApNetworkLanNeighborEntryCapabilities,
       "cfprApNetworkLanNeighborEntryDeviceId": cfprApNetworkLanNeighborEntryDeviceId,
       "cfprApNetworkLanNeighborEntryFiPortDn": cfprApNetworkLanNeighborEntryFiPortDn,
       "cfprApNetworkLanNeighborEntryIpV4Address": cfprApNetworkLanNeighborEntryIpV4Address,
       "cfprApNetworkLanNeighborEntryIpV4MgmtAddress": cfprApNetworkLanNeighborEntryIpV4MgmtAddress,
       "cfprApNetworkLanNeighborEntryLocalInterface": cfprApNetworkLanNeighborEntryLocalInterface,
       "cfprApNetworkLanNeighborEntryNativeVlan": cfprApNetworkLanNeighborEntryNativeVlan,
       "cfprApNetworkLanNeighborEntryPlatform": cfprApNetworkLanNeighborEntryPlatform,
       "cfprApNetworkLanNeighborEntryRemoteInterface": cfprApNetworkLanNeighborEntryRemoteInterface,
       "cfprApNetworkLanNeighborsTable": cfprApNetworkLanNeighborsTable,
       "cfprApNetworkLanNeighborsEntry": cfprApNetworkLanNeighborsEntry,
       "cfprApNetworkLanNeighborsInstanceId": cfprApNetworkLanNeighborsInstanceId,
       "cfprApNetworkLanNeighborsDn": cfprApNetworkLanNeighborsDn,
       "cfprApNetworkLanNeighborsRn": cfprApNetworkLanNeighborsRn,
       "cfprApNetworkOperLevelTable": cfprApNetworkOperLevelTable,
       "cfprApNetworkOperLevelEntry": cfprApNetworkOperLevelEntry,
       "cfprApNetworkOperLevelInstanceId": cfprApNetworkOperLevelInstanceId,
       "cfprApNetworkOperLevelDn": cfprApNetworkOperLevelDn,
       "cfprApNetworkOperLevelRn": cfprApNetworkOperLevelRn,
       "cfprApNetworkOperLevelId": cfprApNetworkOperLevelId,
       "cfprApNetworkOperLevelMaxPrimaryVlanCount": cfprApNetworkOperLevelMaxPrimaryVlanCount,
       "cfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount": cfprApNetworkOperLevelMaxSecVlanPerPrimaryVlanCount,
       "cfprApNetworkOperLevelMaxSecondaryVlanCount": cfprApNetworkOperLevelMaxSecondaryVlanCount,
       "cfprApNetworkOperLevelPrimaryVlanCount": cfprApNetworkOperLevelPrimaryVlanCount,
       "cfprApNetworkOperLevelPrimaryVlanCountStatus": cfprApNetworkOperLevelPrimaryVlanCountStatus,
       "cfprApNetworkOperLevelSecondaryVlanCount": cfprApNetworkOperLevelSecondaryVlanCount,
       "cfprApNetworkOperLevelSecondaryVlanCountStatus": cfprApNetworkOperLevelSecondaryVlanCountStatus,
       "cfprApNetworkSanNeighborEntryTable": cfprApNetworkSanNeighborEntryTable,
       "cfprApNetworkSanNeighborEntryEntry": cfprApNetworkSanNeighborEntryEntry,
       "cfprApNetworkSanNeighborEntryInstanceId": cfprApNetworkSanNeighborEntryInstanceId,
       "cfprApNetworkSanNeighborEntryDn": cfprApNetworkSanNeighborEntryDn,
       "cfprApNetworkSanNeighborEntryRn": cfprApNetworkSanNeighborEntryRn,
       "cfprApNetworkSanNeighborEntryFabricMgmtAddr": cfprApNetworkSanNeighborEntryFabricMgmtAddr,
       "cfprApNetworkSanNeighborEntryFabricNwwn": cfprApNetworkSanNeighborEntryFabricNwwn,
       "cfprApNetworkSanNeighborEntryFabricPwwn": cfprApNetworkSanNeighborEntryFabricPwwn,
       "cfprApNetworkSanNeighborEntryFiPortDn": cfprApNetworkSanNeighborEntryFiPortDn,
       "cfprApNetworkSanNeighborEntryLocalInterface": cfprApNetworkSanNeighborEntryLocalInterface,
       "cfprApNetworkSanNeighborEntryMyNwwn": cfprApNetworkSanNeighborEntryMyNwwn,
       "cfprApNetworkSanNeighborEntryMyPwwn": cfprApNetworkSanNeighborEntryMyPwwn,
       "cfprApNetworkSanNeighborEntryPortVsan": cfprApNetworkSanNeighborEntryPortVsan,
       "cfprApNetworkSanNeighborsTable": cfprApNetworkSanNeighborsTable,
       "cfprApNetworkSanNeighborsEntry": cfprApNetworkSanNeighborsEntry,
       "cfprApNetworkSanNeighborsInstanceId": cfprApNetworkSanNeighborsInstanceId,
       "cfprApNetworkSanNeighborsDn": cfprApNetworkSanNeighborsDn,
       "cfprApNetworkSanNeighborsRn": cfprApNetworkSanNeighborsRn}
)
