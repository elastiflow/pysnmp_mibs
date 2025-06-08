# SNMP MIB module (CISCO-FIREPOWER-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-NETWORK-MIB.mib
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

(CfprEquipmentSensorThresholdStatus,
 CfprMgmtAdminState,
 CfprNetworkElementOperability,
 CfprNetworkIfStatsType,
 CfprNetworkIfStatsUnits,
 CfprNetworkInventoryStatus,
 CfprNetworkSamConfigStatus,
 CfprNetworkSwitchId,
 CfprNetworkVlanCountStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprEquipmentSensorThresholdStatus",
    "CfprMgmtAdminState",
    "CfprNetworkElementOperability",
    "CfprNetworkIfStatsType",
    "CfprNetworkIfStatsUnits",
    "CfprNetworkInventoryStatus",
    "CfprNetworkSamConfigStatus",
    "CfprNetworkSwitchId",
    "CfprNetworkVlanCountStatus")

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

cfprNetworkObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprNetworkElementTable_Object = MibTable
cfprNetworkElementTable = _CfprNetworkElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1)
)
if mibBuilder.loadTexts:
    cfprNetworkElementTable.setStatus("current")
_CfprNetworkElementEntry_Object = MibTableRow
cfprNetworkElementEntry = _CfprNetworkElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1)
)
cfprNetworkElementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkElementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkElementEntry.setStatus("current")
_CfprNetworkElementInstanceId_Type = CfprManagedObjectId
_CfprNetworkElementInstanceId_Object = MibTableColumn
cfprNetworkElementInstanceId = _CfprNetworkElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 1),
    _CfprNetworkElementInstanceId_Type()
)
cfprNetworkElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkElementInstanceId.setStatus("current")
_CfprNetworkElementDn_Type = CfprManagedObjectDn
_CfprNetworkElementDn_Object = MibTableColumn
cfprNetworkElementDn = _CfprNetworkElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 2),
    _CfprNetworkElementDn_Type()
)
cfprNetworkElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementDn.setStatus("current")
_CfprNetworkElementRn_Type = SnmpAdminString
_CfprNetworkElementRn_Object = MibTableColumn
cfprNetworkElementRn = _CfprNetworkElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 3),
    _CfprNetworkElementRn_Type()
)
cfprNetworkElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementRn.setStatus("current")
_CfprNetworkElementAdminInbandIfState_Type = CfprMgmtAdminState
_CfprNetworkElementAdminInbandIfState_Object = MibTableColumn
cfprNetworkElementAdminInbandIfState = _CfprNetworkElementAdminInbandIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 4),
    _CfprNetworkElementAdminInbandIfState_Type()
)
cfprNetworkElementAdminInbandIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementAdminInbandIfState.setStatus("current")
_CfprNetworkElementDiffMemory_Type = Gauge32
_CfprNetworkElementDiffMemory_Object = MibTableColumn
cfprNetworkElementDiffMemory = _CfprNetworkElementDiffMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 5),
    _CfprNetworkElementDiffMemory_Type()
)
cfprNetworkElementDiffMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementDiffMemory.setStatus("current")
_CfprNetworkElementExpectedMemory_Type = Gauge32
_CfprNetworkElementExpectedMemory_Object = MibTableColumn
cfprNetworkElementExpectedMemory = _CfprNetworkElementExpectedMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 6),
    _CfprNetworkElementExpectedMemory_Type()
)
cfprNetworkElementExpectedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementExpectedMemory.setStatus("current")
_CfprNetworkElementFltAggr_Type = Unsigned64
_CfprNetworkElementFltAggr_Object = MibTableColumn
cfprNetworkElementFltAggr = _CfprNetworkElementFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 7),
    _CfprNetworkElementFltAggr_Type()
)
cfprNetworkElementFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementFltAggr.setStatus("current")
_CfprNetworkElementId_Type = CfprNetworkSwitchId
_CfprNetworkElementId_Object = MibTableColumn
cfprNetworkElementId = _CfprNetworkElementId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 8),
    _CfprNetworkElementId_Type()
)
cfprNetworkElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementId.setStatus("current")
_CfprNetworkElementInbandIfGw_Type = InetAddressIPv4
_CfprNetworkElementInbandIfGw_Object = MibTableColumn
cfprNetworkElementInbandIfGw = _CfprNetworkElementInbandIfGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 9),
    _CfprNetworkElementInbandIfGw_Type()
)
cfprNetworkElementInbandIfGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementInbandIfGw.setStatus("current")
_CfprNetworkElementInbandIfIp_Type = InetAddressIPv4
_CfprNetworkElementInbandIfIp_Object = MibTableColumn
cfprNetworkElementInbandIfIp = _CfprNetworkElementInbandIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 10),
    _CfprNetworkElementInbandIfIp_Type()
)
cfprNetworkElementInbandIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementInbandIfIp.setStatus("current")
_CfprNetworkElementInbandIfMask_Type = InetAddressIPv4
_CfprNetworkElementInbandIfMask_Object = MibTableColumn
cfprNetworkElementInbandIfMask = _CfprNetworkElementInbandIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 11),
    _CfprNetworkElementInbandIfMask_Type()
)
cfprNetworkElementInbandIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementInbandIfMask.setStatus("current")
_CfprNetworkElementInbandIfVnet_Type = Gauge32
_CfprNetworkElementInbandIfVnet_Object = MibTableColumn
cfprNetworkElementInbandIfVnet = _CfprNetworkElementInbandIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 12),
    _CfprNetworkElementInbandIfVnet_Type()
)
cfprNetworkElementInbandIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementInbandIfVnet.setStatus("current")
_CfprNetworkElementInventoryStatus_Type = CfprNetworkInventoryStatus
_CfprNetworkElementInventoryStatus_Object = MibTableColumn
cfprNetworkElementInventoryStatus = _CfprNetworkElementInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 13),
    _CfprNetworkElementInventoryStatus_Type()
)
cfprNetworkElementInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementInventoryStatus.setStatus("current")
_CfprNetworkElementModel_Type = SnmpAdminString
_CfprNetworkElementModel_Object = MibTableColumn
cfprNetworkElementModel = _CfprNetworkElementModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 14),
    _CfprNetworkElementModel_Type()
)
cfprNetworkElementModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementModel.setStatus("current")
_CfprNetworkElementOobIfGw_Type = InetAddressIPv4
_CfprNetworkElementOobIfGw_Object = MibTableColumn
cfprNetworkElementOobIfGw = _CfprNetworkElementOobIfGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 15),
    _CfprNetworkElementOobIfGw_Type()
)
cfprNetworkElementOobIfGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementOobIfGw.setStatus("current")
_CfprNetworkElementOobIfIp_Type = InetAddressIPv4
_CfprNetworkElementOobIfIp_Object = MibTableColumn
cfprNetworkElementOobIfIp = _CfprNetworkElementOobIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 16),
    _CfprNetworkElementOobIfIp_Type()
)
cfprNetworkElementOobIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementOobIfIp.setStatus("current")
_CfprNetworkElementOobIfMask_Type = InetAddressIPv4
_CfprNetworkElementOobIfMask_Object = MibTableColumn
cfprNetworkElementOobIfMask = _CfprNetworkElementOobIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 17),
    _CfprNetworkElementOobIfMask_Type()
)
cfprNetworkElementOobIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementOobIfMask.setStatus("current")
_CfprNetworkElementOperability_Type = CfprNetworkElementOperability
_CfprNetworkElementOperability_Object = MibTableColumn
cfprNetworkElementOperability = _CfprNetworkElementOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 18),
    _CfprNetworkElementOperability_Type()
)
cfprNetworkElementOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementOperability.setStatus("current")
_CfprNetworkElementRevision_Type = SnmpAdminString
_CfprNetworkElementRevision_Object = MibTableColumn
cfprNetworkElementRevision = _CfprNetworkElementRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 19),
    _CfprNetworkElementRevision_Type()
)
cfprNetworkElementRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementRevision.setStatus("current")
_CfprNetworkElementSerial_Type = SnmpAdminString
_CfprNetworkElementSerial_Object = MibTableColumn
cfprNetworkElementSerial = _CfprNetworkElementSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 20),
    _CfprNetworkElementSerial_Type()
)
cfprNetworkElementSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementSerial.setStatus("current")
_CfprNetworkElementThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprNetworkElementThermal_Object = MibTableColumn
cfprNetworkElementThermal = _CfprNetworkElementThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 21),
    _CfprNetworkElementThermal_Type()
)
cfprNetworkElementThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementThermal.setStatus("current")
_CfprNetworkElementTotalMemory_Type = Gauge32
_CfprNetworkElementTotalMemory_Object = MibTableColumn
cfprNetworkElementTotalMemory = _CfprNetworkElementTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 22),
    _CfprNetworkElementTotalMemory_Type()
)
cfprNetworkElementTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementTotalMemory.setStatus("current")
_CfprNetworkElementVendor_Type = SnmpAdminString
_CfprNetworkElementVendor_Object = MibTableColumn
cfprNetworkElementVendor = _CfprNetworkElementVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 23),
    _CfprNetworkElementVendor_Type()
)
cfprNetworkElementVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementVendor.setStatus("current")
_CfprNetworkElementIcapCount_Type = Gauge32
_CfprNetworkElementIcapCount_Object = MibTableColumn
cfprNetworkElementIcapCount = _CfprNetworkElementIcapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 24),
    _CfprNetworkElementIcapCount_Type()
)
cfprNetworkElementIcapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementIcapCount.setStatus("current")
_CfprNetworkElementIcapCountString_Type = SnmpAdminString
_CfprNetworkElementIcapCountString_Object = MibTableColumn
cfprNetworkElementIcapCountString = _CfprNetworkElementIcapCountString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 25),
    _CfprNetworkElementIcapCountString_Type()
)
cfprNetworkElementIcapCountString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementIcapCountString.setStatus("current")
_CfprNetworkElementMaxIcapCount_Type = Gauge32
_CfprNetworkElementMaxIcapCount_Object = MibTableColumn
cfprNetworkElementMaxIcapCount = _CfprNetworkElementMaxIcapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 26),
    _CfprNetworkElementMaxIcapCount_Type()
)
cfprNetworkElementMaxIcapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementMaxIcapCount.setStatus("current")
_CfprNetworkElementMaxVcapCount_Type = Gauge32
_CfprNetworkElementMaxVcapCount_Object = MibTableColumn
cfprNetworkElementMaxVcapCount = _CfprNetworkElementMaxVcapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 27),
    _CfprNetworkElementMaxVcapCount_Type()
)
cfprNetworkElementMaxVcapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementMaxVcapCount.setStatus("current")
_CfprNetworkElementSamConfigStatus_Type = CfprNetworkSamConfigStatus
_CfprNetworkElementSamConfigStatus_Object = MibTableColumn
cfprNetworkElementSamConfigStatus = _CfprNetworkElementSamConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 28),
    _CfprNetworkElementSamConfigStatus_Type()
)
cfprNetworkElementSamConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementSamConfigStatus.setStatus("current")
_CfprNetworkElementVcapCount_Type = Gauge32
_CfprNetworkElementVcapCount_Object = MibTableColumn
cfprNetworkElementVcapCount = _CfprNetworkElementVcapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 29),
    _CfprNetworkElementVcapCount_Type()
)
cfprNetworkElementVcapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementVcapCount.setStatus("current")
_CfprNetworkElementVcapCountString_Type = SnmpAdminString
_CfprNetworkElementVcapCountString_Object = MibTableColumn
cfprNetworkElementVcapCountString = _CfprNetworkElementVcapCountString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 30),
    _CfprNetworkElementVcapCountString_Type()
)
cfprNetworkElementVcapCountString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementVcapCountString.setStatus("current")
_CfprNetworkElementVid_Type = SnmpAdminString
_CfprNetworkElementVid_Object = MibTableColumn
cfprNetworkElementVid = _CfprNetworkElementVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 1, 1, 31),
    _CfprNetworkElementVid_Type()
)
cfprNetworkElementVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkElementVid.setStatus("current")
_CfprNetworkIfStatsTable_Object = MibTable
cfprNetworkIfStatsTable = _CfprNetworkIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2)
)
if mibBuilder.loadTexts:
    cfprNetworkIfStatsTable.setStatus("current")
_CfprNetworkIfStatsEntry_Object = MibTableRow
cfprNetworkIfStatsEntry = _CfprNetworkIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1)
)
cfprNetworkIfStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkIfStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkIfStatsEntry.setStatus("current")
_CfprNetworkIfStatsInstanceId_Type = CfprManagedObjectId
_CfprNetworkIfStatsInstanceId_Object = MibTableColumn
cfprNetworkIfStatsInstanceId = _CfprNetworkIfStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 1),
    _CfprNetworkIfStatsInstanceId_Type()
)
cfprNetworkIfStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsInstanceId.setStatus("current")
_CfprNetworkIfStatsDn_Type = CfprManagedObjectDn
_CfprNetworkIfStatsDn_Object = MibTableColumn
cfprNetworkIfStatsDn = _CfprNetworkIfStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 2),
    _CfprNetworkIfStatsDn_Type()
)
cfprNetworkIfStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsDn.setStatus("current")
_CfprNetworkIfStatsRn_Type = SnmpAdminString
_CfprNetworkIfStatsRn_Object = MibTableColumn
cfprNetworkIfStatsRn = _CfprNetworkIfStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 3),
    _CfprNetworkIfStatsRn_Type()
)
cfprNetworkIfStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsRn.setStatus("current")
_CfprNetworkIfStatsOut_Type = Unsigned64
_CfprNetworkIfStatsOut_Object = MibTableColumn
cfprNetworkIfStatsOut = _CfprNetworkIfStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 4),
    _CfprNetworkIfStatsOut_Type()
)
cfprNetworkIfStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsOut.setStatus("current")
_CfprNetworkIfStatsRin_Type = Unsigned64
_CfprNetworkIfStatsRin_Object = MibTableColumn
cfprNetworkIfStatsRin = _CfprNetworkIfStatsRin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 5),
    _CfprNetworkIfStatsRin_Type()
)
cfprNetworkIfStatsRin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsRin.setStatus("current")
_CfprNetworkIfStatsType_Type = CfprNetworkIfStatsType
_CfprNetworkIfStatsType_Object = MibTableColumn
cfprNetworkIfStatsType = _CfprNetworkIfStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 6),
    _CfprNetworkIfStatsType_Type()
)
cfprNetworkIfStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsType.setStatus("current")
_CfprNetworkIfStatsUnits_Type = CfprNetworkIfStatsUnits
_CfprNetworkIfStatsUnits_Object = MibTableColumn
cfprNetworkIfStatsUnits = _CfprNetworkIfStatsUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 2, 1, 7),
    _CfprNetworkIfStatsUnits_Type()
)
cfprNetworkIfStatsUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkIfStatsUnits.setStatus("current")
_CfprNetworkLanNeighborEntryTable_Object = MibTable
cfprNetworkLanNeighborEntryTable = _CfprNetworkLanNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3)
)
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryTable.setStatus("current")
_CfprNetworkLanNeighborEntryEntry_Object = MibTableRow
cfprNetworkLanNeighborEntryEntry = _CfprNetworkLanNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1)
)
cfprNetworkLanNeighborEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkLanNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryEntry.setStatus("current")
_CfprNetworkLanNeighborEntryInstanceId_Type = CfprManagedObjectId
_CfprNetworkLanNeighborEntryInstanceId_Object = MibTableColumn
cfprNetworkLanNeighborEntryInstanceId = _CfprNetworkLanNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 1),
    _CfprNetworkLanNeighborEntryInstanceId_Type()
)
cfprNetworkLanNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryInstanceId.setStatus("current")
_CfprNetworkLanNeighborEntryDn_Type = CfprManagedObjectDn
_CfprNetworkLanNeighborEntryDn_Object = MibTableColumn
cfprNetworkLanNeighborEntryDn = _CfprNetworkLanNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 2),
    _CfprNetworkLanNeighborEntryDn_Type()
)
cfprNetworkLanNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryDn.setStatus("current")
_CfprNetworkLanNeighborEntryRn_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryRn_Object = MibTableColumn
cfprNetworkLanNeighborEntryRn = _CfprNetworkLanNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 3),
    _CfprNetworkLanNeighborEntryRn_Type()
)
cfprNetworkLanNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryRn.setStatus("current")
_CfprNetworkLanNeighborEntryCapabilities_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryCapabilities_Object = MibTableColumn
cfprNetworkLanNeighborEntryCapabilities = _CfprNetworkLanNeighborEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 4),
    _CfprNetworkLanNeighborEntryCapabilities_Type()
)
cfprNetworkLanNeighborEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryCapabilities.setStatus("current")
_CfprNetworkLanNeighborEntryDeviceId_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryDeviceId_Object = MibTableColumn
cfprNetworkLanNeighborEntryDeviceId = _CfprNetworkLanNeighborEntryDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 5),
    _CfprNetworkLanNeighborEntryDeviceId_Type()
)
cfprNetworkLanNeighborEntryDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryDeviceId.setStatus("current")
_CfprNetworkLanNeighborEntryFiPortDn_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryFiPortDn_Object = MibTableColumn
cfprNetworkLanNeighborEntryFiPortDn = _CfprNetworkLanNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 6),
    _CfprNetworkLanNeighborEntryFiPortDn_Type()
)
cfprNetworkLanNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryFiPortDn.setStatus("current")
_CfprNetworkLanNeighborEntryIpV4Address_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryIpV4Address_Object = MibTableColumn
cfprNetworkLanNeighborEntryIpV4Address = _CfprNetworkLanNeighborEntryIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 7),
    _CfprNetworkLanNeighborEntryIpV4Address_Type()
)
cfprNetworkLanNeighborEntryIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryIpV4Address.setStatus("current")
_CfprNetworkLanNeighborEntryIpV4MgmtAddress_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryIpV4MgmtAddress_Object = MibTableColumn
cfprNetworkLanNeighborEntryIpV4MgmtAddress = _CfprNetworkLanNeighborEntryIpV4MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 8),
    _CfprNetworkLanNeighborEntryIpV4MgmtAddress_Type()
)
cfprNetworkLanNeighborEntryIpV4MgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryIpV4MgmtAddress.setStatus("current")
_CfprNetworkLanNeighborEntryLocalInterface_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryLocalInterface_Object = MibTableColumn
cfprNetworkLanNeighborEntryLocalInterface = _CfprNetworkLanNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 9),
    _CfprNetworkLanNeighborEntryLocalInterface_Type()
)
cfprNetworkLanNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryLocalInterface.setStatus("current")
_CfprNetworkLanNeighborEntryNativeVlan_Type = Gauge32
_CfprNetworkLanNeighborEntryNativeVlan_Object = MibTableColumn
cfprNetworkLanNeighborEntryNativeVlan = _CfprNetworkLanNeighborEntryNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 10),
    _CfprNetworkLanNeighborEntryNativeVlan_Type()
)
cfprNetworkLanNeighborEntryNativeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryNativeVlan.setStatus("current")
_CfprNetworkLanNeighborEntryPlatform_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryPlatform_Object = MibTableColumn
cfprNetworkLanNeighborEntryPlatform = _CfprNetworkLanNeighborEntryPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 11),
    _CfprNetworkLanNeighborEntryPlatform_Type()
)
cfprNetworkLanNeighborEntryPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryPlatform.setStatus("current")
_CfprNetworkLanNeighborEntryRemoteInterface_Type = SnmpAdminString
_CfprNetworkLanNeighborEntryRemoteInterface_Object = MibTableColumn
cfprNetworkLanNeighborEntryRemoteInterface = _CfprNetworkLanNeighborEntryRemoteInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 3, 1, 12),
    _CfprNetworkLanNeighborEntryRemoteInterface_Type()
)
cfprNetworkLanNeighborEntryRemoteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborEntryRemoteInterface.setStatus("current")
_CfprNetworkLanNeighborsTable_Object = MibTable
cfprNetworkLanNeighborsTable = _CfprNetworkLanNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 4)
)
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborsTable.setStatus("current")
_CfprNetworkLanNeighborsEntry_Object = MibTableRow
cfprNetworkLanNeighborsEntry = _CfprNetworkLanNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 4, 1)
)
cfprNetworkLanNeighborsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkLanNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborsEntry.setStatus("current")
_CfprNetworkLanNeighborsInstanceId_Type = CfprManagedObjectId
_CfprNetworkLanNeighborsInstanceId_Object = MibTableColumn
cfprNetworkLanNeighborsInstanceId = _CfprNetworkLanNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 4, 1, 1),
    _CfprNetworkLanNeighborsInstanceId_Type()
)
cfprNetworkLanNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborsInstanceId.setStatus("current")
_CfprNetworkLanNeighborsDn_Type = CfprManagedObjectDn
_CfprNetworkLanNeighborsDn_Object = MibTableColumn
cfprNetworkLanNeighborsDn = _CfprNetworkLanNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 4, 1, 2),
    _CfprNetworkLanNeighborsDn_Type()
)
cfprNetworkLanNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborsDn.setStatus("current")
_CfprNetworkLanNeighborsRn_Type = SnmpAdminString
_CfprNetworkLanNeighborsRn_Object = MibTableColumn
cfprNetworkLanNeighborsRn = _CfprNetworkLanNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 4, 1, 3),
    _CfprNetworkLanNeighborsRn_Type()
)
cfprNetworkLanNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkLanNeighborsRn.setStatus("current")
_CfprNetworkOperLevelTable_Object = MibTable
cfprNetworkOperLevelTable = _CfprNetworkOperLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5)
)
if mibBuilder.loadTexts:
    cfprNetworkOperLevelTable.setStatus("current")
_CfprNetworkOperLevelEntry_Object = MibTableRow
cfprNetworkOperLevelEntry = _CfprNetworkOperLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1)
)
cfprNetworkOperLevelEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkOperLevelInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkOperLevelEntry.setStatus("current")
_CfprNetworkOperLevelInstanceId_Type = CfprManagedObjectId
_CfprNetworkOperLevelInstanceId_Object = MibTableColumn
cfprNetworkOperLevelInstanceId = _CfprNetworkOperLevelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 1),
    _CfprNetworkOperLevelInstanceId_Type()
)
cfprNetworkOperLevelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelInstanceId.setStatus("current")
_CfprNetworkOperLevelDn_Type = CfprManagedObjectDn
_CfprNetworkOperLevelDn_Object = MibTableColumn
cfprNetworkOperLevelDn = _CfprNetworkOperLevelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 2),
    _CfprNetworkOperLevelDn_Type()
)
cfprNetworkOperLevelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelDn.setStatus("current")
_CfprNetworkOperLevelRn_Type = SnmpAdminString
_CfprNetworkOperLevelRn_Object = MibTableColumn
cfprNetworkOperLevelRn = _CfprNetworkOperLevelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 3),
    _CfprNetworkOperLevelRn_Type()
)
cfprNetworkOperLevelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelRn.setStatus("current")
_CfprNetworkOperLevelId_Type = CfprNetworkSwitchId
_CfprNetworkOperLevelId_Object = MibTableColumn
cfprNetworkOperLevelId = _CfprNetworkOperLevelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 4),
    _CfprNetworkOperLevelId_Type()
)
cfprNetworkOperLevelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelId.setStatus("current")
_CfprNetworkOperLevelMaxPrimaryVlanCount_Type = Gauge32
_CfprNetworkOperLevelMaxPrimaryVlanCount_Object = MibTableColumn
cfprNetworkOperLevelMaxPrimaryVlanCount = _CfprNetworkOperLevelMaxPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 5),
    _CfprNetworkOperLevelMaxPrimaryVlanCount_Type()
)
cfprNetworkOperLevelMaxPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelMaxPrimaryVlanCount.setStatus("current")
_CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type = Gauge32
_CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object = MibTableColumn
cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount = _CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 6),
    _CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type()
)
cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setStatus("current")
_CfprNetworkOperLevelMaxSecondaryVlanCount_Type = Gauge32
_CfprNetworkOperLevelMaxSecondaryVlanCount_Object = MibTableColumn
cfprNetworkOperLevelMaxSecondaryVlanCount = _CfprNetworkOperLevelMaxSecondaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 7),
    _CfprNetworkOperLevelMaxSecondaryVlanCount_Type()
)
cfprNetworkOperLevelMaxSecondaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelMaxSecondaryVlanCount.setStatus("current")
_CfprNetworkOperLevelPrimaryVlanCount_Type = Gauge32
_CfprNetworkOperLevelPrimaryVlanCount_Object = MibTableColumn
cfprNetworkOperLevelPrimaryVlanCount = _CfprNetworkOperLevelPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 8),
    _CfprNetworkOperLevelPrimaryVlanCount_Type()
)
cfprNetworkOperLevelPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelPrimaryVlanCount.setStatus("current")
_CfprNetworkOperLevelPrimaryVlanCountStatus_Type = CfprNetworkVlanCountStatus
_CfprNetworkOperLevelPrimaryVlanCountStatus_Object = MibTableColumn
cfprNetworkOperLevelPrimaryVlanCountStatus = _CfprNetworkOperLevelPrimaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 9),
    _CfprNetworkOperLevelPrimaryVlanCountStatus_Type()
)
cfprNetworkOperLevelPrimaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelPrimaryVlanCountStatus.setStatus("current")
_CfprNetworkOperLevelSecondaryVlanCount_Type = Gauge32
_CfprNetworkOperLevelSecondaryVlanCount_Object = MibTableColumn
cfprNetworkOperLevelSecondaryVlanCount = _CfprNetworkOperLevelSecondaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 10),
    _CfprNetworkOperLevelSecondaryVlanCount_Type()
)
cfprNetworkOperLevelSecondaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelSecondaryVlanCount.setStatus("current")
_CfprNetworkOperLevelSecondaryVlanCountStatus_Type = CfprNetworkVlanCountStatus
_CfprNetworkOperLevelSecondaryVlanCountStatus_Object = MibTableColumn
cfprNetworkOperLevelSecondaryVlanCountStatus = _CfprNetworkOperLevelSecondaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 5, 1, 11),
    _CfprNetworkOperLevelSecondaryVlanCountStatus_Type()
)
cfprNetworkOperLevelSecondaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkOperLevelSecondaryVlanCountStatus.setStatus("current")
_CfprNetworkSanNeighborEntryTable_Object = MibTable
cfprNetworkSanNeighborEntryTable = _CfprNetworkSanNeighborEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6)
)
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryTable.setStatus("current")
_CfprNetworkSanNeighborEntryEntry_Object = MibTableRow
cfprNetworkSanNeighborEntryEntry = _CfprNetworkSanNeighborEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1)
)
cfprNetworkSanNeighborEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkSanNeighborEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryEntry.setStatus("current")
_CfprNetworkSanNeighborEntryInstanceId_Type = CfprManagedObjectId
_CfprNetworkSanNeighborEntryInstanceId_Object = MibTableColumn
cfprNetworkSanNeighborEntryInstanceId = _CfprNetworkSanNeighborEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 1),
    _CfprNetworkSanNeighborEntryInstanceId_Type()
)
cfprNetworkSanNeighborEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryInstanceId.setStatus("current")
_CfprNetworkSanNeighborEntryDn_Type = CfprManagedObjectDn
_CfprNetworkSanNeighborEntryDn_Object = MibTableColumn
cfprNetworkSanNeighborEntryDn = _CfprNetworkSanNeighborEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 2),
    _CfprNetworkSanNeighborEntryDn_Type()
)
cfprNetworkSanNeighborEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryDn.setStatus("current")
_CfprNetworkSanNeighborEntryRn_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryRn_Object = MibTableColumn
cfprNetworkSanNeighborEntryRn = _CfprNetworkSanNeighborEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 3),
    _CfprNetworkSanNeighborEntryRn_Type()
)
cfprNetworkSanNeighborEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryRn.setStatus("current")
_CfprNetworkSanNeighborEntryFabricMgmtAddr_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryFabricMgmtAddr_Object = MibTableColumn
cfprNetworkSanNeighborEntryFabricMgmtAddr = _CfprNetworkSanNeighborEntryFabricMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 4),
    _CfprNetworkSanNeighborEntryFabricMgmtAddr_Type()
)
cfprNetworkSanNeighborEntryFabricMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryFabricMgmtAddr.setStatus("current")
_CfprNetworkSanNeighborEntryFabricNwwn_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryFabricNwwn_Object = MibTableColumn
cfprNetworkSanNeighborEntryFabricNwwn = _CfprNetworkSanNeighborEntryFabricNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 5),
    _CfprNetworkSanNeighborEntryFabricNwwn_Type()
)
cfprNetworkSanNeighborEntryFabricNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryFabricNwwn.setStatus("current")
_CfprNetworkSanNeighborEntryFabricPwwn_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryFabricPwwn_Object = MibTableColumn
cfprNetworkSanNeighborEntryFabricPwwn = _CfprNetworkSanNeighborEntryFabricPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 6),
    _CfprNetworkSanNeighborEntryFabricPwwn_Type()
)
cfprNetworkSanNeighborEntryFabricPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryFabricPwwn.setStatus("current")
_CfprNetworkSanNeighborEntryFiPortDn_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryFiPortDn_Object = MibTableColumn
cfprNetworkSanNeighborEntryFiPortDn = _CfprNetworkSanNeighborEntryFiPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 7),
    _CfprNetworkSanNeighborEntryFiPortDn_Type()
)
cfprNetworkSanNeighborEntryFiPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryFiPortDn.setStatus("current")
_CfprNetworkSanNeighborEntryLocalInterface_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryLocalInterface_Object = MibTableColumn
cfprNetworkSanNeighborEntryLocalInterface = _CfprNetworkSanNeighborEntryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 8),
    _CfprNetworkSanNeighborEntryLocalInterface_Type()
)
cfprNetworkSanNeighborEntryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryLocalInterface.setStatus("current")
_CfprNetworkSanNeighborEntryMyNwwn_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryMyNwwn_Object = MibTableColumn
cfprNetworkSanNeighborEntryMyNwwn = _CfprNetworkSanNeighborEntryMyNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 9),
    _CfprNetworkSanNeighborEntryMyNwwn_Type()
)
cfprNetworkSanNeighborEntryMyNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryMyNwwn.setStatus("current")
_CfprNetworkSanNeighborEntryMyPwwn_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryMyPwwn_Object = MibTableColumn
cfprNetworkSanNeighborEntryMyPwwn = _CfprNetworkSanNeighborEntryMyPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 10),
    _CfprNetworkSanNeighborEntryMyPwwn_Type()
)
cfprNetworkSanNeighborEntryMyPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryMyPwwn.setStatus("current")
_CfprNetworkSanNeighborEntryPortVsan_Type = SnmpAdminString
_CfprNetworkSanNeighborEntryPortVsan_Object = MibTableColumn
cfprNetworkSanNeighborEntryPortVsan = _CfprNetworkSanNeighborEntryPortVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 6, 1, 11),
    _CfprNetworkSanNeighborEntryPortVsan_Type()
)
cfprNetworkSanNeighborEntryPortVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborEntryPortVsan.setStatus("current")
_CfprNetworkSanNeighborsTable_Object = MibTable
cfprNetworkSanNeighborsTable = _CfprNetworkSanNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 7)
)
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborsTable.setStatus("current")
_CfprNetworkSanNeighborsEntry_Object = MibTableRow
cfprNetworkSanNeighborsEntry = _CfprNetworkSanNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 7, 1)
)
cfprNetworkSanNeighborsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NETWORK-MIB", "cfprNetworkSanNeighborsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborsEntry.setStatus("current")
_CfprNetworkSanNeighborsInstanceId_Type = CfprManagedObjectId
_CfprNetworkSanNeighborsInstanceId_Object = MibTableColumn
cfprNetworkSanNeighborsInstanceId = _CfprNetworkSanNeighborsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 7, 1, 1),
    _CfprNetworkSanNeighborsInstanceId_Type()
)
cfprNetworkSanNeighborsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborsInstanceId.setStatus("current")
_CfprNetworkSanNeighborsDn_Type = CfprManagedObjectDn
_CfprNetworkSanNeighborsDn_Object = MibTableColumn
cfprNetworkSanNeighborsDn = _CfprNetworkSanNeighborsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 7, 1, 2),
    _CfprNetworkSanNeighborsDn_Type()
)
cfprNetworkSanNeighborsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborsDn.setStatus("current")
_CfprNetworkSanNeighborsRn_Type = SnmpAdminString
_CfprNetworkSanNeighborsRn_Object = MibTableColumn
cfprNetworkSanNeighborsRn = _CfprNetworkSanNeighborsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 52, 7, 1, 3),
    _CfprNetworkSanNeighborsRn_Type()
)
cfprNetworkSanNeighborsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNetworkSanNeighborsRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-NETWORK-MIB",
    **{"cfprNetworkObjects": cfprNetworkObjects,
       "cfprNetworkElementTable": cfprNetworkElementTable,
       "cfprNetworkElementEntry": cfprNetworkElementEntry,
       "cfprNetworkElementInstanceId": cfprNetworkElementInstanceId,
       "cfprNetworkElementDn": cfprNetworkElementDn,
       "cfprNetworkElementRn": cfprNetworkElementRn,
       "cfprNetworkElementAdminInbandIfState": cfprNetworkElementAdminInbandIfState,
       "cfprNetworkElementDiffMemory": cfprNetworkElementDiffMemory,
       "cfprNetworkElementExpectedMemory": cfprNetworkElementExpectedMemory,
       "cfprNetworkElementFltAggr": cfprNetworkElementFltAggr,
       "cfprNetworkElementId": cfprNetworkElementId,
       "cfprNetworkElementInbandIfGw": cfprNetworkElementInbandIfGw,
       "cfprNetworkElementInbandIfIp": cfprNetworkElementInbandIfIp,
       "cfprNetworkElementInbandIfMask": cfprNetworkElementInbandIfMask,
       "cfprNetworkElementInbandIfVnet": cfprNetworkElementInbandIfVnet,
       "cfprNetworkElementInventoryStatus": cfprNetworkElementInventoryStatus,
       "cfprNetworkElementModel": cfprNetworkElementModel,
       "cfprNetworkElementOobIfGw": cfprNetworkElementOobIfGw,
       "cfprNetworkElementOobIfIp": cfprNetworkElementOobIfIp,
       "cfprNetworkElementOobIfMask": cfprNetworkElementOobIfMask,
       "cfprNetworkElementOperability": cfprNetworkElementOperability,
       "cfprNetworkElementRevision": cfprNetworkElementRevision,
       "cfprNetworkElementSerial": cfprNetworkElementSerial,
       "cfprNetworkElementThermal": cfprNetworkElementThermal,
       "cfprNetworkElementTotalMemory": cfprNetworkElementTotalMemory,
       "cfprNetworkElementVendor": cfprNetworkElementVendor,
       "cfprNetworkElementIcapCount": cfprNetworkElementIcapCount,
       "cfprNetworkElementIcapCountString": cfprNetworkElementIcapCountString,
       "cfprNetworkElementMaxIcapCount": cfprNetworkElementMaxIcapCount,
       "cfprNetworkElementMaxVcapCount": cfprNetworkElementMaxVcapCount,
       "cfprNetworkElementSamConfigStatus": cfprNetworkElementSamConfigStatus,
       "cfprNetworkElementVcapCount": cfprNetworkElementVcapCount,
       "cfprNetworkElementVcapCountString": cfprNetworkElementVcapCountString,
       "cfprNetworkElementVid": cfprNetworkElementVid,
       "cfprNetworkIfStatsTable": cfprNetworkIfStatsTable,
       "cfprNetworkIfStatsEntry": cfprNetworkIfStatsEntry,
       "cfprNetworkIfStatsInstanceId": cfprNetworkIfStatsInstanceId,
       "cfprNetworkIfStatsDn": cfprNetworkIfStatsDn,
       "cfprNetworkIfStatsRn": cfprNetworkIfStatsRn,
       "cfprNetworkIfStatsOut": cfprNetworkIfStatsOut,
       "cfprNetworkIfStatsRin": cfprNetworkIfStatsRin,
       "cfprNetworkIfStatsType": cfprNetworkIfStatsType,
       "cfprNetworkIfStatsUnits": cfprNetworkIfStatsUnits,
       "cfprNetworkLanNeighborEntryTable": cfprNetworkLanNeighborEntryTable,
       "cfprNetworkLanNeighborEntryEntry": cfprNetworkLanNeighborEntryEntry,
       "cfprNetworkLanNeighborEntryInstanceId": cfprNetworkLanNeighborEntryInstanceId,
       "cfprNetworkLanNeighborEntryDn": cfprNetworkLanNeighborEntryDn,
       "cfprNetworkLanNeighborEntryRn": cfprNetworkLanNeighborEntryRn,
       "cfprNetworkLanNeighborEntryCapabilities": cfprNetworkLanNeighborEntryCapabilities,
       "cfprNetworkLanNeighborEntryDeviceId": cfprNetworkLanNeighborEntryDeviceId,
       "cfprNetworkLanNeighborEntryFiPortDn": cfprNetworkLanNeighborEntryFiPortDn,
       "cfprNetworkLanNeighborEntryIpV4Address": cfprNetworkLanNeighborEntryIpV4Address,
       "cfprNetworkLanNeighborEntryIpV4MgmtAddress": cfprNetworkLanNeighborEntryIpV4MgmtAddress,
       "cfprNetworkLanNeighborEntryLocalInterface": cfprNetworkLanNeighborEntryLocalInterface,
       "cfprNetworkLanNeighborEntryNativeVlan": cfprNetworkLanNeighborEntryNativeVlan,
       "cfprNetworkLanNeighborEntryPlatform": cfprNetworkLanNeighborEntryPlatform,
       "cfprNetworkLanNeighborEntryRemoteInterface": cfprNetworkLanNeighborEntryRemoteInterface,
       "cfprNetworkLanNeighborsTable": cfprNetworkLanNeighborsTable,
       "cfprNetworkLanNeighborsEntry": cfprNetworkLanNeighborsEntry,
       "cfprNetworkLanNeighborsInstanceId": cfprNetworkLanNeighborsInstanceId,
       "cfprNetworkLanNeighborsDn": cfprNetworkLanNeighborsDn,
       "cfprNetworkLanNeighborsRn": cfprNetworkLanNeighborsRn,
       "cfprNetworkOperLevelTable": cfprNetworkOperLevelTable,
       "cfprNetworkOperLevelEntry": cfprNetworkOperLevelEntry,
       "cfprNetworkOperLevelInstanceId": cfprNetworkOperLevelInstanceId,
       "cfprNetworkOperLevelDn": cfprNetworkOperLevelDn,
       "cfprNetworkOperLevelRn": cfprNetworkOperLevelRn,
       "cfprNetworkOperLevelId": cfprNetworkOperLevelId,
       "cfprNetworkOperLevelMaxPrimaryVlanCount": cfprNetworkOperLevelMaxPrimaryVlanCount,
       "cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount": cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount,
       "cfprNetworkOperLevelMaxSecondaryVlanCount": cfprNetworkOperLevelMaxSecondaryVlanCount,
       "cfprNetworkOperLevelPrimaryVlanCount": cfprNetworkOperLevelPrimaryVlanCount,
       "cfprNetworkOperLevelPrimaryVlanCountStatus": cfprNetworkOperLevelPrimaryVlanCountStatus,
       "cfprNetworkOperLevelSecondaryVlanCount": cfprNetworkOperLevelSecondaryVlanCount,
       "cfprNetworkOperLevelSecondaryVlanCountStatus": cfprNetworkOperLevelSecondaryVlanCountStatus,
       "cfprNetworkSanNeighborEntryTable": cfprNetworkSanNeighborEntryTable,
       "cfprNetworkSanNeighborEntryEntry": cfprNetworkSanNeighborEntryEntry,
       "cfprNetworkSanNeighborEntryInstanceId": cfprNetworkSanNeighborEntryInstanceId,
       "cfprNetworkSanNeighborEntryDn": cfprNetworkSanNeighborEntryDn,
       "cfprNetworkSanNeighborEntryRn": cfprNetworkSanNeighborEntryRn,
       "cfprNetworkSanNeighborEntryFabricMgmtAddr": cfprNetworkSanNeighborEntryFabricMgmtAddr,
       "cfprNetworkSanNeighborEntryFabricNwwn": cfprNetworkSanNeighborEntryFabricNwwn,
       "cfprNetworkSanNeighborEntryFabricPwwn": cfprNetworkSanNeighborEntryFabricPwwn,
       "cfprNetworkSanNeighborEntryFiPortDn": cfprNetworkSanNeighborEntryFiPortDn,
       "cfprNetworkSanNeighborEntryLocalInterface": cfprNetworkSanNeighborEntryLocalInterface,
       "cfprNetworkSanNeighborEntryMyNwwn": cfprNetworkSanNeighborEntryMyNwwn,
       "cfprNetworkSanNeighborEntryMyPwwn": cfprNetworkSanNeighborEntryMyPwwn,
       "cfprNetworkSanNeighborEntryPortVsan": cfprNetworkSanNeighborEntryPortVsan,
       "cfprNetworkSanNeighborsTable": cfprNetworkSanNeighborsTable,
       "cfprNetworkSanNeighborsEntry": cfprNetworkSanNeighborsEntry,
       "cfprNetworkSanNeighborsInstanceId": cfprNetworkSanNeighborsInstanceId,
       "cfprNetworkSanNeighborsDn": cfprNetworkSanNeighborsDn,
       "cfprNetworkSanNeighborsRn": cfprNetworkSanNeighborsRn}
)
