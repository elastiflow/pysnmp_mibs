# SNMP MIB module (CISCO-FIREPOWER-NWCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-NWCTRL-MIB.mib
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

(CfprEquipmentCardAdminState,
 CfprEquipmentPowerState,
 CfprFabricAdminState,
 CfprFabricSSAPortType,
 CfprNwctrlAdminState,
 CfprNwctrlCardAction,
 CfprNwctrlConfigState,
 CfprNwctrlLinkFailAction,
 CfprNwctrlOirState,
 CfprNwctrlRegistrationMode,
 CfprPolicyPolicyOwner,
 CfprPortDuplex,
 CfprPortEthSpeed) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprEquipmentCardAdminState",
    "CfprEquipmentPowerState",
    "CfprFabricAdminState",
    "CfprFabricSSAPortType",
    "CfprNwctrlAdminState",
    "CfprNwctrlCardAction",
    "CfprNwctrlConfigState",
    "CfprNwctrlLinkFailAction",
    "CfprNwctrlOirState",
    "CfprNwctrlRegistrationMode",
    "CfprPolicyPolicyOwner",
    "CfprPortDuplex",
    "CfprPortEthSpeed")

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

cfprNwctrlObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprNwctrlDefinitionTable_Object = MibTable
cfprNwctrlDefinitionTable = _CfprNwctrlDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1)
)
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionTable.setStatus("current")
_CfprNwctrlDefinitionEntry_Object = MibTableRow
cfprNwctrlDefinitionEntry = _CfprNwctrlDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1)
)
cfprNwctrlDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NWCTRL-MIB", "cfprNwctrlDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionEntry.setStatus("current")
_CfprNwctrlDefinitionInstanceId_Type = CfprManagedObjectId
_CfprNwctrlDefinitionInstanceId_Object = MibTableColumn
cfprNwctrlDefinitionInstanceId = _CfprNwctrlDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 1),
    _CfprNwctrlDefinitionInstanceId_Type()
)
cfprNwctrlDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionInstanceId.setStatus("current")
_CfprNwctrlDefinitionDn_Type = CfprManagedObjectDn
_CfprNwctrlDefinitionDn_Object = MibTableColumn
cfprNwctrlDefinitionDn = _CfprNwctrlDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 2),
    _CfprNwctrlDefinitionDn_Type()
)
cfprNwctrlDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionDn.setStatus("current")
_CfprNwctrlDefinitionRn_Type = SnmpAdminString
_CfprNwctrlDefinitionRn_Object = MibTableColumn
cfprNwctrlDefinitionRn = _CfprNwctrlDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 3),
    _CfprNwctrlDefinitionRn_Type()
)
cfprNwctrlDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionRn.setStatus("current")
_CfprNwctrlDefinitionCdp_Type = CfprNwctrlAdminState
_CfprNwctrlDefinitionCdp_Object = MibTableColumn
cfprNwctrlDefinitionCdp = _CfprNwctrlDefinitionCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 4),
    _CfprNwctrlDefinitionCdp_Type()
)
cfprNwctrlDefinitionCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionCdp.setStatus("current")
_CfprNwctrlDefinitionDescr_Type = SnmpAdminString
_CfprNwctrlDefinitionDescr_Object = MibTableColumn
cfprNwctrlDefinitionDescr = _CfprNwctrlDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 5),
    _CfprNwctrlDefinitionDescr_Type()
)
cfprNwctrlDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionDescr.setStatus("current")
_CfprNwctrlDefinitionIntId_Type = SnmpAdminString
_CfprNwctrlDefinitionIntId_Object = MibTableColumn
cfprNwctrlDefinitionIntId = _CfprNwctrlDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 6),
    _CfprNwctrlDefinitionIntId_Type()
)
cfprNwctrlDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionIntId.setStatus("current")
_CfprNwctrlDefinitionMacRegisterMode_Type = CfprNwctrlRegistrationMode
_CfprNwctrlDefinitionMacRegisterMode_Object = MibTableColumn
cfprNwctrlDefinitionMacRegisterMode = _CfprNwctrlDefinitionMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 7),
    _CfprNwctrlDefinitionMacRegisterMode_Type()
)
cfprNwctrlDefinitionMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionMacRegisterMode.setStatus("current")
_CfprNwctrlDefinitionName_Type = SnmpAdminString
_CfprNwctrlDefinitionName_Object = MibTableColumn
cfprNwctrlDefinitionName = _CfprNwctrlDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 8),
    _CfprNwctrlDefinitionName_Type()
)
cfprNwctrlDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionName.setStatus("current")
_CfprNwctrlDefinitionPolicyLevel_Type = Gauge32
_CfprNwctrlDefinitionPolicyLevel_Object = MibTableColumn
cfprNwctrlDefinitionPolicyLevel = _CfprNwctrlDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 9),
    _CfprNwctrlDefinitionPolicyLevel_Type()
)
cfprNwctrlDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionPolicyLevel.setStatus("current")
_CfprNwctrlDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprNwctrlDefinitionPolicyOwner_Object = MibTableColumn
cfprNwctrlDefinitionPolicyOwner = _CfprNwctrlDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 10),
    _CfprNwctrlDefinitionPolicyOwner_Type()
)
cfprNwctrlDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionPolicyOwner.setStatus("current")
_CfprNwctrlDefinitionUplinkFailAction_Type = CfprNwctrlLinkFailAction
_CfprNwctrlDefinitionUplinkFailAction_Object = MibTableColumn
cfprNwctrlDefinitionUplinkFailAction = _CfprNwctrlDefinitionUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 11),
    _CfprNwctrlDefinitionUplinkFailAction_Type()
)
cfprNwctrlDefinitionUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionUplinkFailAction.setStatus("current")
_CfprNwctrlDefinitionLldpReceive_Type = CfprNwctrlAdminState
_CfprNwctrlDefinitionLldpReceive_Object = MibTableColumn
cfprNwctrlDefinitionLldpReceive = _CfprNwctrlDefinitionLldpReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 12),
    _CfprNwctrlDefinitionLldpReceive_Type()
)
cfprNwctrlDefinitionLldpReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionLldpReceive.setStatus("current")
_CfprNwctrlDefinitionLldpTransmit_Type = CfprNwctrlAdminState
_CfprNwctrlDefinitionLldpTransmit_Object = MibTableColumn
cfprNwctrlDefinitionLldpTransmit = _CfprNwctrlDefinitionLldpTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 1, 1, 13),
    _CfprNwctrlDefinitionLldpTransmit_Type()
)
cfprNwctrlDefinitionLldpTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlDefinitionLldpTransmit.setStatus("current")
_CfprNwctrlCardConfigTable_Object = MibTable
cfprNwctrlCardConfigTable = _CfprNwctrlCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2)
)
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigTable.setStatus("current")
_CfprNwctrlCardConfigEntry_Object = MibTableRow
cfprNwctrlCardConfigEntry = _CfprNwctrlCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1)
)
cfprNwctrlCardConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NWCTRL-MIB", "cfprNwctrlCardConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigEntry.setStatus("current")
_CfprNwctrlCardConfigInstanceId_Type = CfprManagedObjectId
_CfprNwctrlCardConfigInstanceId_Object = MibTableColumn
cfprNwctrlCardConfigInstanceId = _CfprNwctrlCardConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 1),
    _CfprNwctrlCardConfigInstanceId_Type()
)
cfprNwctrlCardConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigInstanceId.setStatus("current")
_CfprNwctrlCardConfigDn_Type = CfprManagedObjectDn
_CfprNwctrlCardConfigDn_Object = MibTableColumn
cfprNwctrlCardConfigDn = _CfprNwctrlCardConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 2),
    _CfprNwctrlCardConfigDn_Type()
)
cfprNwctrlCardConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigDn.setStatus("current")
_CfprNwctrlCardConfigRn_Type = SnmpAdminString
_CfprNwctrlCardConfigRn_Object = MibTableColumn
cfprNwctrlCardConfigRn = _CfprNwctrlCardConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 3),
    _CfprNwctrlCardConfigRn_Type()
)
cfprNwctrlCardConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigRn.setStatus("current")
_CfprNwctrlCardConfigAction_Type = CfprNwctrlCardAction
_CfprNwctrlCardConfigAction_Object = MibTableColumn
cfprNwctrlCardConfigAction = _CfprNwctrlCardConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 4),
    _CfprNwctrlCardConfigAction_Type()
)
cfprNwctrlCardConfigAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigAction.setStatus("current")
_CfprNwctrlCardConfigAdminState_Type = CfprEquipmentCardAdminState
_CfprNwctrlCardConfigAdminState_Object = MibTableColumn
cfprNwctrlCardConfigAdminState = _CfprNwctrlCardConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 5),
    _CfprNwctrlCardConfigAdminState_Type()
)
cfprNwctrlCardConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigAdminState.setStatus("current")
_CfprNwctrlCardConfigConfigState_Type = CfprNwctrlConfigState
_CfprNwctrlCardConfigConfigState_Object = MibTableColumn
cfprNwctrlCardConfigConfigState = _CfprNwctrlCardConfigConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 6),
    _CfprNwctrlCardConfigConfigState_Type()
)
cfprNwctrlCardConfigConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigConfigState.setStatus("current")
_CfprNwctrlCardConfigFltAggr_Type = Unsigned64
_CfprNwctrlCardConfigFltAggr_Object = MibTableColumn
cfprNwctrlCardConfigFltAggr = _CfprNwctrlCardConfigFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 7),
    _CfprNwctrlCardConfigFltAggr_Type()
)
cfprNwctrlCardConfigFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigFltAggr.setStatus("current")
_CfprNwctrlCardConfigModel_Type = SnmpAdminString
_CfprNwctrlCardConfigModel_Object = MibTableColumn
cfprNwctrlCardConfigModel = _CfprNwctrlCardConfigModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 8),
    _CfprNwctrlCardConfigModel_Type()
)
cfprNwctrlCardConfigModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigModel.setStatus("current")
_CfprNwctrlCardConfigOirState_Type = CfprNwctrlOirState
_CfprNwctrlCardConfigOirState_Object = MibTableColumn
cfprNwctrlCardConfigOirState = _CfprNwctrlCardConfigOirState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 9),
    _CfprNwctrlCardConfigOirState_Type()
)
cfprNwctrlCardConfigOirState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigOirState.setStatus("current")
_CfprNwctrlCardConfigOperState_Type = CfprEquipmentPowerState
_CfprNwctrlCardConfigOperState_Object = MibTableColumn
cfprNwctrlCardConfigOperState = _CfprNwctrlCardConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 10),
    _CfprNwctrlCardConfigOperState_Type()
)
cfprNwctrlCardConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigOperState.setStatus("current")
_CfprNwctrlCardConfigPresence_Type = TruthValue
_CfprNwctrlCardConfigPresence_Object = MibTableColumn
cfprNwctrlCardConfigPresence = _CfprNwctrlCardConfigPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 11),
    _CfprNwctrlCardConfigPresence_Type()
)
cfprNwctrlCardConfigPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigPresence.setStatus("current")
_CfprNwctrlCardConfigRevision_Type = SnmpAdminString
_CfprNwctrlCardConfigRevision_Object = MibTableColumn
cfprNwctrlCardConfigRevision = _CfprNwctrlCardConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 12),
    _CfprNwctrlCardConfigRevision_Type()
)
cfprNwctrlCardConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigRevision.setStatus("current")
_CfprNwctrlCardConfigSlotId_Type = Gauge32
_CfprNwctrlCardConfigSlotId_Object = MibTableColumn
cfprNwctrlCardConfigSlotId = _CfprNwctrlCardConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 13),
    _CfprNwctrlCardConfigSlotId_Type()
)
cfprNwctrlCardConfigSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigSlotId.setStatus("current")
_CfprNwctrlCardConfigTs_Type = DateAndTime
_CfprNwctrlCardConfigTs_Object = MibTableColumn
cfprNwctrlCardConfigTs = _CfprNwctrlCardConfigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 14),
    _CfprNwctrlCardConfigTs_Type()
)
cfprNwctrlCardConfigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigTs.setStatus("current")
_CfprNwctrlCardConfigVendor_Type = SnmpAdminString
_CfprNwctrlCardConfigVendor_Object = MibTableColumn
cfprNwctrlCardConfigVendor = _CfprNwctrlCardConfigVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 2, 1, 15),
    _CfprNwctrlCardConfigVendor_Type()
)
cfprNwctrlCardConfigVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlCardConfigVendor.setStatus("current")
_CfprNwctrlPortConfigTable_Object = MibTable
cfprNwctrlPortConfigTable = _CfprNwctrlPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3)
)
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigTable.setStatus("current")
_CfprNwctrlPortConfigEntry_Object = MibTableRow
cfprNwctrlPortConfigEntry = _CfprNwctrlPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1)
)
cfprNwctrlPortConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NWCTRL-MIB", "cfprNwctrlPortConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigEntry.setStatus("current")
_CfprNwctrlPortConfigInstanceId_Type = CfprManagedObjectId
_CfprNwctrlPortConfigInstanceId_Object = MibTableColumn
cfprNwctrlPortConfigInstanceId = _CfprNwctrlPortConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 1),
    _CfprNwctrlPortConfigInstanceId_Type()
)
cfprNwctrlPortConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigInstanceId.setStatus("current")
_CfprNwctrlPortConfigDn_Type = CfprManagedObjectDn
_CfprNwctrlPortConfigDn_Object = MibTableColumn
cfprNwctrlPortConfigDn = _CfprNwctrlPortConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 2),
    _CfprNwctrlPortConfigDn_Type()
)
cfprNwctrlPortConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigDn.setStatus("current")
_CfprNwctrlPortConfigRn_Type = SnmpAdminString
_CfprNwctrlPortConfigRn_Object = MibTableColumn
cfprNwctrlPortConfigRn = _CfprNwctrlPortConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 3),
    _CfprNwctrlPortConfigRn_Type()
)
cfprNwctrlPortConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigRn.setStatus("current")
_CfprNwctrlPortConfigAdminDuplex_Type = CfprPortDuplex
_CfprNwctrlPortConfigAdminDuplex_Object = MibTableColumn
cfprNwctrlPortConfigAdminDuplex = _CfprNwctrlPortConfigAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 4),
    _CfprNwctrlPortConfigAdminDuplex_Type()
)
cfprNwctrlPortConfigAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAdminDuplex.setStatus("current")
_CfprNwctrlPortConfigAdminSpeed_Type = CfprPortEthSpeed
_CfprNwctrlPortConfigAdminSpeed_Object = MibTableColumn
cfprNwctrlPortConfigAdminSpeed = _CfprNwctrlPortConfigAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 5),
    _CfprNwctrlPortConfigAdminSpeed_Type()
)
cfprNwctrlPortConfigAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAdminSpeed.setStatus("current")
_CfprNwctrlPortConfigAdminState_Type = CfprFabricAdminState
_CfprNwctrlPortConfigAdminState_Object = MibTableColumn
cfprNwctrlPortConfigAdminState = _CfprNwctrlPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 6),
    _CfprNwctrlPortConfigAdminState_Type()
)
cfprNwctrlPortConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAdminState.setStatus("current")
_CfprNwctrlPortConfigAggrId_Type = Gauge32
_CfprNwctrlPortConfigAggrId_Object = MibTableColumn
cfprNwctrlPortConfigAggrId = _CfprNwctrlPortConfigAggrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 7),
    _CfprNwctrlPortConfigAggrId_Type()
)
cfprNwctrlPortConfigAggrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAggrId.setStatus("current")
_CfprNwctrlPortConfigAllowSharing_Type = TruthValue
_CfprNwctrlPortConfigAllowSharing_Object = MibTableColumn
cfprNwctrlPortConfigAllowSharing = _CfprNwctrlPortConfigAllowSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 8),
    _CfprNwctrlPortConfigAllowSharing_Type()
)
cfprNwctrlPortConfigAllowSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAllowSharing.setStatus("current")
_CfprNwctrlPortConfigAutoNeg_Type = TruthValue
_CfprNwctrlPortConfigAutoNeg_Object = MibTableColumn
cfprNwctrlPortConfigAutoNeg = _CfprNwctrlPortConfigAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 9),
    _CfprNwctrlPortConfigAutoNeg_Type()
)
cfprNwctrlPortConfigAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAutoNeg.setStatus("current")
_CfprNwctrlPortConfigFlowCtrlPolicy_Type = SnmpAdminString
_CfprNwctrlPortConfigFlowCtrlPolicy_Object = MibTableColumn
cfprNwctrlPortConfigFlowCtrlPolicy = _CfprNwctrlPortConfigFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 10),
    _CfprNwctrlPortConfigFlowCtrlPolicy_Type()
)
cfprNwctrlPortConfigFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigFlowCtrlPolicy.setStatus("current")
_CfprNwctrlPortConfigPcId_Type = Gauge32
_CfprNwctrlPortConfigPcId_Object = MibTableColumn
cfprNwctrlPortConfigPcId = _CfprNwctrlPortConfigPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 11),
    _CfprNwctrlPortConfigPcId_Type()
)
cfprNwctrlPortConfigPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigPcId.setStatus("current")
_CfprNwctrlPortConfigPortId_Type = Gauge32
_CfprNwctrlPortConfigPortId_Object = MibTableColumn
cfprNwctrlPortConfigPortId = _CfprNwctrlPortConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 12),
    _CfprNwctrlPortConfigPortId_Type()
)
cfprNwctrlPortConfigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigPortId.setStatus("current")
_CfprNwctrlPortConfigSlotId_Type = Gauge32
_CfprNwctrlPortConfigSlotId_Object = MibTableColumn
cfprNwctrlPortConfigSlotId = _CfprNwctrlPortConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 13),
    _CfprNwctrlPortConfigSlotId_Type()
)
cfprNwctrlPortConfigSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigSlotId.setStatus("current")
_CfprNwctrlPortConfigSsaPortType_Type = CfprFabricSSAPortType
_CfprNwctrlPortConfigSsaPortType_Object = MibTableColumn
cfprNwctrlPortConfigSsaPortType = _CfprNwctrlPortConfigSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 14),
    _CfprNwctrlPortConfigSsaPortType_Type()
)
cfprNwctrlPortConfigSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigSsaPortType.setStatus("current")
_CfprNwctrlPortConfigTs_Type = DateAndTime
_CfprNwctrlPortConfigTs_Object = MibTableColumn
cfprNwctrlPortConfigTs = _CfprNwctrlPortConfigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 15),
    _CfprNwctrlPortConfigTs_Type()
)
cfprNwctrlPortConfigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigTs.setStatus("current")
_CfprNwctrlPortConfigNwCtrlPolicyName_Type = SnmpAdminString
_CfprNwctrlPortConfigNwCtrlPolicyName_Object = MibTableColumn
cfprNwctrlPortConfigNwCtrlPolicyName = _CfprNwctrlPortConfigNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 16),
    _CfprNwctrlPortConfigNwCtrlPolicyName_Type()
)
cfprNwctrlPortConfigNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigNwCtrlPolicyName.setStatus("current")
_CfprNwctrlPortConfigAllowAneg_Type = TruthValue
_CfprNwctrlPortConfigAllowAneg_Object = MibTableColumn
cfprNwctrlPortConfigAllowAneg = _CfprNwctrlPortConfigAllowAneg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 3, 1, 17),
    _CfprNwctrlPortConfigAllowAneg_Type()
)
cfprNwctrlPortConfigAllowAneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlPortConfigAllowAneg.setStatus("current")
_CfprNwctrlSubIfTable_Object = MibTable
cfprNwctrlSubIfTable = _CfprNwctrlSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4)
)
if mibBuilder.loadTexts:
    cfprNwctrlSubIfTable.setStatus("current")
_CfprNwctrlSubIfEntry_Object = MibTableRow
cfprNwctrlSubIfEntry = _CfprNwctrlSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1)
)
cfprNwctrlSubIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-NWCTRL-MIB", "cfprNwctrlSubIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprNwctrlSubIfEntry.setStatus("current")
_CfprNwctrlSubIfInstanceId_Type = CfprManagedObjectId
_CfprNwctrlSubIfInstanceId_Object = MibTableColumn
cfprNwctrlSubIfInstanceId = _CfprNwctrlSubIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 1),
    _CfprNwctrlSubIfInstanceId_Type()
)
cfprNwctrlSubIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfInstanceId.setStatus("current")
_CfprNwctrlSubIfDn_Type = CfprManagedObjectDn
_CfprNwctrlSubIfDn_Object = MibTableColumn
cfprNwctrlSubIfDn = _CfprNwctrlSubIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 2),
    _CfprNwctrlSubIfDn_Type()
)
cfprNwctrlSubIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfDn.setStatus("current")
_CfprNwctrlSubIfRn_Type = SnmpAdminString
_CfprNwctrlSubIfRn_Object = MibTableColumn
cfprNwctrlSubIfRn = _CfprNwctrlSubIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 3),
    _CfprNwctrlSubIfRn_Type()
)
cfprNwctrlSubIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfRn.setStatus("current")
_CfprNwctrlSubIfAdminState_Type = CfprFabricAdminState
_CfprNwctrlSubIfAdminState_Object = MibTableColumn
cfprNwctrlSubIfAdminState = _CfprNwctrlSubIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 4),
    _CfprNwctrlSubIfAdminState_Type()
)
cfprNwctrlSubIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfAdminState.setStatus("current")
_CfprNwctrlSubIfAllowSharing_Type = TruthValue
_CfprNwctrlSubIfAllowSharing_Object = MibTableColumn
cfprNwctrlSubIfAllowSharing = _CfprNwctrlSubIfAllowSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 5),
    _CfprNwctrlSubIfAllowSharing_Type()
)
cfprNwctrlSubIfAllowSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfAllowSharing.setStatus("current")
_CfprNwctrlSubIfSsaPortType_Type = CfprFabricSSAPortType
_CfprNwctrlSubIfSsaPortType_Object = MibTableColumn
cfprNwctrlSubIfSsaPortType = _CfprNwctrlSubIfSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 6),
    _CfprNwctrlSubIfSsaPortType_Type()
)
cfprNwctrlSubIfSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfSsaPortType.setStatus("current")
_CfprNwctrlSubIfSubId_Type = Gauge32
_CfprNwctrlSubIfSubId_Object = MibTableColumn
cfprNwctrlSubIfSubId = _CfprNwctrlSubIfSubId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 7),
    _CfprNwctrlSubIfSubId_Type()
)
cfprNwctrlSubIfSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfSubId.setStatus("current")
_CfprNwctrlSubIfVlanId_Type = Integer32
_CfprNwctrlSubIfVlanId_Object = MibTableColumn
cfprNwctrlSubIfVlanId = _CfprNwctrlSubIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 56, 4, 1, 8),
    _CfprNwctrlSubIfVlanId_Type()
)
cfprNwctrlSubIfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprNwctrlSubIfVlanId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-NWCTRL-MIB",
    **{"cfprNwctrlObjects": cfprNwctrlObjects,
       "cfprNwctrlDefinitionTable": cfprNwctrlDefinitionTable,
       "cfprNwctrlDefinitionEntry": cfprNwctrlDefinitionEntry,
       "cfprNwctrlDefinitionInstanceId": cfprNwctrlDefinitionInstanceId,
       "cfprNwctrlDefinitionDn": cfprNwctrlDefinitionDn,
       "cfprNwctrlDefinitionRn": cfprNwctrlDefinitionRn,
       "cfprNwctrlDefinitionCdp": cfprNwctrlDefinitionCdp,
       "cfprNwctrlDefinitionDescr": cfprNwctrlDefinitionDescr,
       "cfprNwctrlDefinitionIntId": cfprNwctrlDefinitionIntId,
       "cfprNwctrlDefinitionMacRegisterMode": cfprNwctrlDefinitionMacRegisterMode,
       "cfprNwctrlDefinitionName": cfprNwctrlDefinitionName,
       "cfprNwctrlDefinitionPolicyLevel": cfprNwctrlDefinitionPolicyLevel,
       "cfprNwctrlDefinitionPolicyOwner": cfprNwctrlDefinitionPolicyOwner,
       "cfprNwctrlDefinitionUplinkFailAction": cfprNwctrlDefinitionUplinkFailAction,
       "cfprNwctrlDefinitionLldpReceive": cfprNwctrlDefinitionLldpReceive,
       "cfprNwctrlDefinitionLldpTransmit": cfprNwctrlDefinitionLldpTransmit,
       "cfprNwctrlCardConfigTable": cfprNwctrlCardConfigTable,
       "cfprNwctrlCardConfigEntry": cfprNwctrlCardConfigEntry,
       "cfprNwctrlCardConfigInstanceId": cfprNwctrlCardConfigInstanceId,
       "cfprNwctrlCardConfigDn": cfprNwctrlCardConfigDn,
       "cfprNwctrlCardConfigRn": cfprNwctrlCardConfigRn,
       "cfprNwctrlCardConfigAction": cfprNwctrlCardConfigAction,
       "cfprNwctrlCardConfigAdminState": cfprNwctrlCardConfigAdminState,
       "cfprNwctrlCardConfigConfigState": cfprNwctrlCardConfigConfigState,
       "cfprNwctrlCardConfigFltAggr": cfprNwctrlCardConfigFltAggr,
       "cfprNwctrlCardConfigModel": cfprNwctrlCardConfigModel,
       "cfprNwctrlCardConfigOirState": cfprNwctrlCardConfigOirState,
       "cfprNwctrlCardConfigOperState": cfprNwctrlCardConfigOperState,
       "cfprNwctrlCardConfigPresence": cfprNwctrlCardConfigPresence,
       "cfprNwctrlCardConfigRevision": cfprNwctrlCardConfigRevision,
       "cfprNwctrlCardConfigSlotId": cfprNwctrlCardConfigSlotId,
       "cfprNwctrlCardConfigTs": cfprNwctrlCardConfigTs,
       "cfprNwctrlCardConfigVendor": cfprNwctrlCardConfigVendor,
       "cfprNwctrlPortConfigTable": cfprNwctrlPortConfigTable,
       "cfprNwctrlPortConfigEntry": cfprNwctrlPortConfigEntry,
       "cfprNwctrlPortConfigInstanceId": cfprNwctrlPortConfigInstanceId,
       "cfprNwctrlPortConfigDn": cfprNwctrlPortConfigDn,
       "cfprNwctrlPortConfigRn": cfprNwctrlPortConfigRn,
       "cfprNwctrlPortConfigAdminDuplex": cfprNwctrlPortConfigAdminDuplex,
       "cfprNwctrlPortConfigAdminSpeed": cfprNwctrlPortConfigAdminSpeed,
       "cfprNwctrlPortConfigAdminState": cfprNwctrlPortConfigAdminState,
       "cfprNwctrlPortConfigAggrId": cfprNwctrlPortConfigAggrId,
       "cfprNwctrlPortConfigAllowSharing": cfprNwctrlPortConfigAllowSharing,
       "cfprNwctrlPortConfigAutoNeg": cfprNwctrlPortConfigAutoNeg,
       "cfprNwctrlPortConfigFlowCtrlPolicy": cfprNwctrlPortConfigFlowCtrlPolicy,
       "cfprNwctrlPortConfigPcId": cfprNwctrlPortConfigPcId,
       "cfprNwctrlPortConfigPortId": cfprNwctrlPortConfigPortId,
       "cfprNwctrlPortConfigSlotId": cfprNwctrlPortConfigSlotId,
       "cfprNwctrlPortConfigSsaPortType": cfprNwctrlPortConfigSsaPortType,
       "cfprNwctrlPortConfigTs": cfprNwctrlPortConfigTs,
       "cfprNwctrlPortConfigNwCtrlPolicyName": cfprNwctrlPortConfigNwCtrlPolicyName,
       "cfprNwctrlPortConfigAllowAneg": cfprNwctrlPortConfigAllowAneg,
       "cfprNwctrlSubIfTable": cfprNwctrlSubIfTable,
       "cfprNwctrlSubIfEntry": cfprNwctrlSubIfEntry,
       "cfprNwctrlSubIfInstanceId": cfprNwctrlSubIfInstanceId,
       "cfprNwctrlSubIfDn": cfprNwctrlSubIfDn,
       "cfprNwctrlSubIfRn": cfprNwctrlSubIfRn,
       "cfprNwctrlSubIfAdminState": cfprNwctrlSubIfAdminState,
       "cfprNwctrlSubIfAllowSharing": cfprNwctrlSubIfAllowSharing,
       "cfprNwctrlSubIfSsaPortType": cfprNwctrlSubIfSsaPortType,
       "cfprNwctrlSubIfSubId": cfprNwctrlSubIfSubId,
       "cfprNwctrlSubIfVlanId": cfprNwctrlSubIfVlanId}
)
