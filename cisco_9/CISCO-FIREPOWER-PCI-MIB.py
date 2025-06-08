# SNMP MIB module (CISCO-FIREPOWER-PCI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-PCI-MIB.mib
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

(CfprEquipmentDiscoveryState,
 CfprEquipmentOperability,
 CfprEquipmentPowerState,
 CfprEquipmentPresence,
 CfprEquipmentSensorThresholdStatus,
 CfprPciEquipSlotId) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprEquipmentDiscoveryState",
    "CfprEquipmentOperability",
    "CfprEquipmentPowerState",
    "CfprEquipmentPresence",
    "CfprEquipmentSensorThresholdStatus",
    "CfprPciEquipSlotId")

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

cfprPciObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprPciEquipSlotTable_Object = MibTable
cfprPciEquipSlotTable = _CfprPciEquipSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1)
)
if mibBuilder.loadTexts:
    cfprPciEquipSlotTable.setStatus("current")
_CfprPciEquipSlotEntry_Object = MibTableRow
cfprPciEquipSlotEntry = _CfprPciEquipSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1)
)
cfprPciEquipSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PCI-MIB", "cfprPciEquipSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPciEquipSlotEntry.setStatus("current")
_CfprPciEquipSlotInstanceId_Type = CfprManagedObjectId
_CfprPciEquipSlotInstanceId_Object = MibTableColumn
cfprPciEquipSlotInstanceId = _CfprPciEquipSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 1),
    _CfprPciEquipSlotInstanceId_Type()
)
cfprPciEquipSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPciEquipSlotInstanceId.setStatus("current")
_CfprPciEquipSlotDn_Type = CfprManagedObjectDn
_CfprPciEquipSlotDn_Object = MibTableColumn
cfprPciEquipSlotDn = _CfprPciEquipSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 2),
    _CfprPciEquipSlotDn_Type()
)
cfprPciEquipSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotDn.setStatus("current")
_CfprPciEquipSlotRn_Type = SnmpAdminString
_CfprPciEquipSlotRn_Object = MibTableColumn
cfprPciEquipSlotRn = _CfprPciEquipSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 3),
    _CfprPciEquipSlotRn_Type()
)
cfprPciEquipSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotRn.setStatus("current")
_CfprPciEquipSlotControllerReported_Type = SnmpAdminString
_CfprPciEquipSlotControllerReported_Object = MibTableColumn
cfprPciEquipSlotControllerReported = _CfprPciEquipSlotControllerReported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 4),
    _CfprPciEquipSlotControllerReported_Type()
)
cfprPciEquipSlotControllerReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotControllerReported.setStatus("current")
_CfprPciEquipSlotDiscoveryState_Type = CfprEquipmentDiscoveryState
_CfprPciEquipSlotDiscoveryState_Object = MibTableColumn
cfprPciEquipSlotDiscoveryState = _CfprPciEquipSlotDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 5),
    _CfprPciEquipSlotDiscoveryState_Type()
)
cfprPciEquipSlotDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotDiscoveryState.setStatus("current")
_CfprPciEquipSlotFltAggr_Type = Unsigned64
_CfprPciEquipSlotFltAggr_Object = MibTableColumn
cfprPciEquipSlotFltAggr = _CfprPciEquipSlotFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 6),
    _CfprPciEquipSlotFltAggr_Type()
)
cfprPciEquipSlotFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotFltAggr.setStatus("current")
_CfprPciEquipSlotHostReported_Type = SnmpAdminString
_CfprPciEquipSlotHostReported_Object = MibTableColumn
cfprPciEquipSlotHostReported = _CfprPciEquipSlotHostReported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 7),
    _CfprPciEquipSlotHostReported_Type()
)
cfprPciEquipSlotHostReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotHostReported.setStatus("current")
_CfprPciEquipSlotId_Type = CfprPciEquipSlotId
_CfprPciEquipSlotId_Object = MibTableColumn
cfprPciEquipSlotId = _CfprPciEquipSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 8),
    _CfprPciEquipSlotId_Type()
)
cfprPciEquipSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotId.setStatus("current")
_CfprPciEquipSlotMacLeft_Type = MacAddress
_CfprPciEquipSlotMacLeft_Object = MibTableColumn
cfprPciEquipSlotMacLeft = _CfprPciEquipSlotMacLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 9),
    _CfprPciEquipSlotMacLeft_Type()
)
cfprPciEquipSlotMacLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotMacLeft.setStatus("current")
_CfprPciEquipSlotMacRight_Type = MacAddress
_CfprPciEquipSlotMacRight_Object = MibTableColumn
cfprPciEquipSlotMacRight = _CfprPciEquipSlotMacRight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 10),
    _CfprPciEquipSlotMacRight_Type()
)
cfprPciEquipSlotMacRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotMacRight.setStatus("current")
_CfprPciEquipSlotModel_Type = SnmpAdminString
_CfprPciEquipSlotModel_Object = MibTableColumn
cfprPciEquipSlotModel = _CfprPciEquipSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 11),
    _CfprPciEquipSlotModel_Type()
)
cfprPciEquipSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotModel.setStatus("current")
_CfprPciEquipSlotRevision_Type = SnmpAdminString
_CfprPciEquipSlotRevision_Object = MibTableColumn
cfprPciEquipSlotRevision = _CfprPciEquipSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 12),
    _CfprPciEquipSlotRevision_Type()
)
cfprPciEquipSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotRevision.setStatus("current")
_CfprPciEquipSlotSerial_Type = SnmpAdminString
_CfprPciEquipSlotSerial_Object = MibTableColumn
cfprPciEquipSlotSerial = _CfprPciEquipSlotSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 13),
    _CfprPciEquipSlotSerial_Type()
)
cfprPciEquipSlotSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotSerial.setStatus("current")
_CfprPciEquipSlotSmbiosId_Type = Gauge32
_CfprPciEquipSlotSmbiosId_Object = MibTableColumn
cfprPciEquipSlotSmbiosId = _CfprPciEquipSlotSmbiosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 14),
    _CfprPciEquipSlotSmbiosId_Type()
)
cfprPciEquipSlotSmbiosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotSmbiosId.setStatus("current")
_CfprPciEquipSlotVendor_Type = SnmpAdminString
_CfprPciEquipSlotVendor_Object = MibTableColumn
cfprPciEquipSlotVendor = _CfprPciEquipSlotVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 1, 1, 15),
    _CfprPciEquipSlotVendor_Type()
)
cfprPciEquipSlotVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciEquipSlotVendor.setStatus("current")
_CfprPciUnitTable_Object = MibTable
cfprPciUnitTable = _CfprPciUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2)
)
if mibBuilder.loadTexts:
    cfprPciUnitTable.setStatus("current")
_CfprPciUnitEntry_Object = MibTableRow
cfprPciUnitEntry = _CfprPciUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1)
)
cfprPciUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-PCI-MIB", "cfprPciUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPciUnitEntry.setStatus("current")
_CfprPciUnitInstanceId_Type = CfprManagedObjectId
_CfprPciUnitInstanceId_Object = MibTableColumn
cfprPciUnitInstanceId = _CfprPciUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 1),
    _CfprPciUnitInstanceId_Type()
)
cfprPciUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPciUnitInstanceId.setStatus("current")
_CfprPciUnitDn_Type = CfprManagedObjectDn
_CfprPciUnitDn_Object = MibTableColumn
cfprPciUnitDn = _CfprPciUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 2),
    _CfprPciUnitDn_Type()
)
cfprPciUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitDn.setStatus("current")
_CfprPciUnitRn_Type = SnmpAdminString
_CfprPciUnitRn_Object = MibTableColumn
cfprPciUnitRn = _CfprPciUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 3),
    _CfprPciUnitRn_Type()
)
cfprPciUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitRn.setStatus("current")
_CfprPciUnitId_Type = Gauge32
_CfprPciUnitId_Object = MibTableColumn
cfprPciUnitId = _CfprPciUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 4),
    _CfprPciUnitId_Type()
)
cfprPciUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitId.setStatus("current")
_CfprPciUnitLocationDn_Type = SnmpAdminString
_CfprPciUnitLocationDn_Object = MibTableColumn
cfprPciUnitLocationDn = _CfprPciUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 5),
    _CfprPciUnitLocationDn_Type()
)
cfprPciUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitLocationDn.setStatus("current")
_CfprPciUnitModel_Type = SnmpAdminString
_CfprPciUnitModel_Object = MibTableColumn
cfprPciUnitModel = _CfprPciUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 6),
    _CfprPciUnitModel_Type()
)
cfprPciUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitModel.setStatus("current")
_CfprPciUnitOperQualifierReason_Type = SnmpAdminString
_CfprPciUnitOperQualifierReason_Object = MibTableColumn
cfprPciUnitOperQualifierReason = _CfprPciUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 7),
    _CfprPciUnitOperQualifierReason_Type()
)
cfprPciUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitOperQualifierReason.setStatus("current")
_CfprPciUnitOperState_Type = CfprEquipmentOperability
_CfprPciUnitOperState_Object = MibTableColumn
cfprPciUnitOperState = _CfprPciUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 8),
    _CfprPciUnitOperState_Type()
)
cfprPciUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitOperState.setStatus("current")
_CfprPciUnitOperability_Type = CfprEquipmentOperability
_CfprPciUnitOperability_Object = MibTableColumn
cfprPciUnitOperability = _CfprPciUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 9),
    _CfprPciUnitOperability_Type()
)
cfprPciUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitOperability.setStatus("current")
_CfprPciUnitPciAddr_Type = SnmpAdminString
_CfprPciUnitPciAddr_Object = MibTableColumn
cfprPciUnitPciAddr = _CfprPciUnitPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 10),
    _CfprPciUnitPciAddr_Type()
)
cfprPciUnitPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitPciAddr.setStatus("current")
_CfprPciUnitPciSlot_Type = SnmpAdminString
_CfprPciUnitPciSlot_Object = MibTableColumn
cfprPciUnitPciSlot = _CfprPciUnitPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 11),
    _CfprPciUnitPciSlot_Type()
)
cfprPciUnitPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitPciSlot.setStatus("current")
_CfprPciUnitPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprPciUnitPerf_Object = MibTableColumn
cfprPciUnitPerf = _CfprPciUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 12),
    _CfprPciUnitPerf_Type()
)
cfprPciUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitPerf.setStatus("current")
_CfprPciUnitPower_Type = CfprEquipmentPowerState
_CfprPciUnitPower_Object = MibTableColumn
cfprPciUnitPower = _CfprPciUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 13),
    _CfprPciUnitPower_Type()
)
cfprPciUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitPower.setStatus("current")
_CfprPciUnitPresence_Type = CfprEquipmentPresence
_CfprPciUnitPresence_Object = MibTableColumn
cfprPciUnitPresence = _CfprPciUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 14),
    _CfprPciUnitPresence_Type()
)
cfprPciUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitPresence.setStatus("current")
_CfprPciUnitRevision_Type = SnmpAdminString
_CfprPciUnitRevision_Object = MibTableColumn
cfprPciUnitRevision = _CfprPciUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 15),
    _CfprPciUnitRevision_Type()
)
cfprPciUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitRevision.setStatus("current")
_CfprPciUnitSerial_Type = SnmpAdminString
_CfprPciUnitSerial_Object = MibTableColumn
cfprPciUnitSerial = _CfprPciUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 16),
    _CfprPciUnitSerial_Type()
)
cfprPciUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitSerial.setStatus("current")
_CfprPciUnitThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprPciUnitThermal_Object = MibTableColumn
cfprPciUnitThermal = _CfprPciUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 17),
    _CfprPciUnitThermal_Type()
)
cfprPciUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitThermal.setStatus("current")
_CfprPciUnitVendor_Type = SnmpAdminString
_CfprPciUnitVendor_Object = MibTableColumn
cfprPciUnitVendor = _CfprPciUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 18),
    _CfprPciUnitVendor_Type()
)
cfprPciUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitVendor.setStatus("current")
_CfprPciUnitVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprPciUnitVoltage_Object = MibTableColumn
cfprPciUnitVoltage = _CfprPciUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 60, 2, 1, 19),
    _CfprPciUnitVoltage_Type()
)
cfprPciUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPciUnitVoltage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-PCI-MIB",
    **{"cfprPciObjects": cfprPciObjects,
       "cfprPciEquipSlotTable": cfprPciEquipSlotTable,
       "cfprPciEquipSlotEntry": cfprPciEquipSlotEntry,
       "cfprPciEquipSlotInstanceId": cfprPciEquipSlotInstanceId,
       "cfprPciEquipSlotDn": cfprPciEquipSlotDn,
       "cfprPciEquipSlotRn": cfprPciEquipSlotRn,
       "cfprPciEquipSlotControllerReported": cfprPciEquipSlotControllerReported,
       "cfprPciEquipSlotDiscoveryState": cfprPciEquipSlotDiscoveryState,
       "cfprPciEquipSlotFltAggr": cfprPciEquipSlotFltAggr,
       "cfprPciEquipSlotHostReported": cfprPciEquipSlotHostReported,
       "cfprPciEquipSlotId": cfprPciEquipSlotId,
       "cfprPciEquipSlotMacLeft": cfprPciEquipSlotMacLeft,
       "cfprPciEquipSlotMacRight": cfprPciEquipSlotMacRight,
       "cfprPciEquipSlotModel": cfprPciEquipSlotModel,
       "cfprPciEquipSlotRevision": cfprPciEquipSlotRevision,
       "cfprPciEquipSlotSerial": cfprPciEquipSlotSerial,
       "cfprPciEquipSlotSmbiosId": cfprPciEquipSlotSmbiosId,
       "cfprPciEquipSlotVendor": cfprPciEquipSlotVendor,
       "cfprPciUnitTable": cfprPciUnitTable,
       "cfprPciUnitEntry": cfprPciUnitEntry,
       "cfprPciUnitInstanceId": cfprPciUnitInstanceId,
       "cfprPciUnitDn": cfprPciUnitDn,
       "cfprPciUnitRn": cfprPciUnitRn,
       "cfprPciUnitId": cfprPciUnitId,
       "cfprPciUnitLocationDn": cfprPciUnitLocationDn,
       "cfprPciUnitModel": cfprPciUnitModel,
       "cfprPciUnitOperQualifierReason": cfprPciUnitOperQualifierReason,
       "cfprPciUnitOperState": cfprPciUnitOperState,
       "cfprPciUnitOperability": cfprPciUnitOperability,
       "cfprPciUnitPciAddr": cfprPciUnitPciAddr,
       "cfprPciUnitPciSlot": cfprPciUnitPciSlot,
       "cfprPciUnitPerf": cfprPciUnitPerf,
       "cfprPciUnitPower": cfprPciUnitPower,
       "cfprPciUnitPresence": cfprPciUnitPresence,
       "cfprPciUnitRevision": cfprPciUnitRevision,
       "cfprPciUnitSerial": cfprPciUnitSerial,
       "cfprPciUnitThermal": cfprPciUnitThermal,
       "cfprPciUnitVendor": cfprPciUnitVendor,
       "cfprPciUnitVoltage": cfprPciUnitVoltage}
)
