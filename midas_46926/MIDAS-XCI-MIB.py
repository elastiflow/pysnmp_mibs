# SNMP MIB module (MIDAS-XCI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/midas_46926/MIDAS-XCI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:19 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

(KeyChange,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "KeyChange")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

midasXCIProductMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1)
)
if mibBuilder.loadTexts:
    midasXCIProductMIB.setRevisions(
        ("2018-05-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Midasgt_ObjectIdentity = ObjectIdentity
midasgt = _Midasgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1)
)
_ProductName_Type = DisplayString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_ProductDescription_Type = DisplayString
_ProductDescription_Object = MibScalar
productDescription = _ProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 2),
    _ProductDescription_Type()
)
productDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productDescription.setStatus("current")
_ProductSerialNbr_Type = DisplayString
_ProductSerialNbr_Object = MibScalar
productSerialNbr = _ProductSerialNbr_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 3),
    _ProductSerialNbr_Type()
)
productSerialNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNbr.setStatus("current")
_ApplicationPartNbr_Type = DisplayString
_ApplicationPartNbr_Object = MibScalar
applicationPartNbr = _ApplicationPartNbr_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 4),
    _ApplicationPartNbr_Type()
)
applicationPartNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPartNbr.setStatus("current")
_ApplicationVersion_Type = Integer32
_ApplicationVersion_Object = MibScalar
applicationVersion = _ApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 5),
    _ApplicationVersion_Type()
)
applicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationVersion.setStatus("current")
_BootloaderPartNbr_Type = DisplayString
_BootloaderPartNbr_Object = MibScalar
bootloaderPartNbr = _BootloaderPartNbr_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 6),
    _BootloaderPartNbr_Type()
)
bootloaderPartNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootloaderPartNbr.setStatus("current")
_BootloaderVersion_Type = Integer32
_BootloaderVersion_Object = MibScalar
bootloaderVersion = _BootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 7),
    _BootloaderVersion_Type()
)
bootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootloaderVersion.setStatus("current")
_HardwarePartNbr_Type = DisplayString
_HardwarePartNbr_Object = MibScalar
hardwarePartNbr = _HardwarePartNbr_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 8),
    _HardwarePartNbr_Type()
)
hardwarePartNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePartNbr.setStatus("current")
_HardwareID_Type = Integer32
_HardwareID_Object = MibScalar
hardwareID = _HardwareID_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 1, 9),
    _HardwareID_Type()
)
hardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareID.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2)
)
_Ipv4TrapTable_Object = MibTable
ipv4TrapTable = _Ipv4TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipv4TrapTable.setStatus("current")
_Ipv4TrapEntry_Object = MibTableRow
ipv4TrapEntry = _Ipv4TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 1, 1)
)
ipv4TrapEntry.setIndexNames(
    (0, "MIDAS-XCI-MIB", "ipv4TrapReceiverNumber"),
)
if mibBuilder.loadTexts:
    ipv4TrapEntry.setStatus("current")


class _Ipv4TrapReceiverNumber_Type(Integer32):
    """Custom type ipv4TrapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Ipv4TrapReceiverNumber_Type.__name__ = "Integer32"
_Ipv4TrapReceiverNumber_Object = MibTableColumn
ipv4TrapReceiverNumber = _Ipv4TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 1, 1, 1),
    _Ipv4TrapReceiverNumber_Type()
)
ipv4TrapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv4TrapReceiverNumber.setStatus("current")


class _Ipv4TrapEnabled_Type(Integer32):
    """Custom type ipv4TrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ipv4TrapEnabled_Type.__name__ = "Integer32"
_Ipv4TrapEnabled_Object = MibTableColumn
ipv4TrapEnabled = _Ipv4TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 1, 1, 2),
    _Ipv4TrapEnabled_Type()
)
ipv4TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapEnabled.setStatus("current")
_Ipv4TrapReceiverIPAddress_Type = IpAddress
_Ipv4TrapReceiverIPAddress_Object = MibTableColumn
ipv4TrapReceiverIPAddress = _Ipv4TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 1, 1, 3),
    _Ipv4TrapReceiverIPAddress_Type()
)
ipv4TrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapReceiverIPAddress.setStatus("current")


class _Ipv4TrapCommunity_Type(DisplayString):
    """Custom type ipv4TrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Ipv4TrapCommunity_Type.__name__ = "DisplayString"
_Ipv4TrapCommunity_Object = MibTableColumn
ipv4TrapCommunity = _Ipv4TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 1, 1, 4),
    _Ipv4TrapCommunity_Type()
)
ipv4TrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapCommunity.setStatus("current")
_Ipv4ManagerTable_Object = MibTable
ipv4ManagerTable = _Ipv4ManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipv4ManagerTable.setStatus("current")
_Ipv4ManagerEntry_Object = MibTableRow
ipv4ManagerEntry = _Ipv4ManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 3, 1)
)
ipv4ManagerEntry.setIndexNames(
    (0, "MIDAS-XCI-MIB", "ipv4ManagerNumber"),
)
if mibBuilder.loadTexts:
    ipv4ManagerEntry.setStatus("current")


class _Ipv4ManagerNumber_Type(Integer32):
    """Custom type ipv4ManagerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Ipv4ManagerNumber_Type.__name__ = "Integer32"
_Ipv4ManagerNumber_Object = MibTableColumn
ipv4ManagerNumber = _Ipv4ManagerNumber_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 3, 1, 1),
    _Ipv4ManagerNumber_Type()
)
ipv4ManagerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv4ManagerNumber.setStatus("current")


class _Ipv4ManagerEnabled_Type(Integer32):
    """Custom type ipv4ManagerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ipv4ManagerEnabled_Type.__name__ = "Integer32"
_Ipv4ManagerEnabled_Object = MibTableColumn
ipv4ManagerEnabled = _Ipv4ManagerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 3, 1, 2),
    _Ipv4ManagerEnabled_Type()
)
ipv4ManagerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4ManagerEnabled.setStatus("current")
_Ipv4ManagerIPAddress_Type = IpAddress
_Ipv4ManagerIPAddress_Object = MibTableColumn
ipv4ManagerIPAddress = _Ipv4ManagerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 3, 1, 3),
    _Ipv4ManagerIPAddress_Type()
)
ipv4ManagerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4ManagerIPAddress.setStatus("current")
_TankInformation_ObjectIdentity = ObjectIdentity
tankInformation = _TankInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tankInformation.setStatus("current")


class _TankLocation_Type(DisplayString):
    """Custom type tankLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TankLocation_Type.__name__ = "DisplayString"
_TankLocation_Object = MibScalar
tankLocation = _TankLocation_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 5, 1),
    _TankLocation_Type()
)
tankLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tankLocation.setStatus("current")


class _TankChassisID_Type(DisplayString):
    """Custom type tankChassisID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TankChassisID_Type.__name__ = "DisplayString"
_TankChassisID_Object = MibScalar
tankChassisID = _TankChassisID_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 5, 2),
    _TankChassisID_Type()
)
tankChassisID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tankChassisID.setStatus("current")


class _TankContactInfo_Type(DisplayString):
    """Custom type tankContactInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TankContactInfo_Type.__name__ = "DisplayString"
_TankContactInfo_Object = MibScalar
tankContactInfo = _TankContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 2, 5, 3),
    _TankContactInfo_Type()
)
tankContactInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tankContactInfo.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3)
)
_SystemState_ObjectIdentity = ObjectIdentity
systemState = _SystemState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 1)
)
if mibBuilder.loadTexts:
    systemState.setStatus("current")


class _OverallStatus_Type(Integer32):
    """Custom type overallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notice", 2),
          ("warning", 3),
          ("error", 4),
          ("unknown", 5))
    )


_OverallStatus_Type.__name__ = "Integer32"
_OverallStatus_Object = MibScalar
overallStatus = _OverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 1, 1),
    _OverallStatus_Type()
)
overallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overallStatus.setStatus("current")


class _RedundancyMode_Type(Integer32):
    """Custom type redundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 0),
          ("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_RedundancyMode_Type.__name__ = "Integer32"
_RedundancyMode_Object = MibScalar
redundancyMode = _RedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 1, 2),
    _RedundancyMode_Type()
)
redundancyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyMode.setStatus("current")


class _ControlType_Type(Integer32):
    """Custom type controlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("standby", 1),
          ("water", 2),
          ("pump", 3),
          ("max", 4),
          ("unknown", 5))
    )


_ControlType_Type.__name__ = "Integer32"
_ControlType_Object = MibScalar
controlType = _ControlType_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 1, 3),
    _ControlType_Type()
)
controlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlType.setStatus("current")
_LocalSensorData_ObjectIdentity = ObjectIdentity
localSensorData = _LocalSensorData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2)
)
if mibBuilder.loadTexts:
    localSensorData.setStatus("current")
_WaterInletTemperature_Type = Integer32
_WaterInletTemperature_Object = MibScalar
waterInletTemperature = _WaterInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 1),
    _WaterInletTemperature_Type()
)
waterInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterInletTemperature.setStatus("current")
if mibBuilder.loadTexts:
    waterInletTemperature.setUnits("deg C x10")
_WaterSaturation_Type = Integer32
_WaterSaturation_Object = MibScalar
waterSaturation = _WaterSaturation_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 2),
    _WaterSaturation_Type()
)
waterSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSaturation.setStatus("current")
if mibBuilder.loadTexts:
    waterSaturation.setUnits("% x10")
_OilInletTemperature_Type = Integer32
_OilInletTemperature_Object = MibScalar
oilInletTemperature = _OilInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 3),
    _OilInletTemperature_Type()
)
oilInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilInletTemperature.setStatus("current")
if mibBuilder.loadTexts:
    oilInletTemperature.setUnits("deg C x10")
_OilOutletTemperature_Type = Integer32
_OilOutletTemperature_Object = MibScalar
oilOutletTemperature = _OilOutletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 4),
    _OilOutletTemperature_Type()
)
oilOutletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilOutletTemperature.setStatus("current")
if mibBuilder.loadTexts:
    oilOutletTemperature.setUnits("deg C x10")
_OilTankTemperature_Type = Integer32
_OilTankTemperature_Object = MibScalar
oilTankTemperature = _OilTankTemperature_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 5),
    _OilTankTemperature_Type()
)
oilTankTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilTankTemperature.setStatus("current")
if mibBuilder.loadTexts:
    oilTankTemperature.setUnits("deg C x10")
_OilPressure_Type = Integer32
_OilPressure_Object = MibScalar
oilPressure = _OilPressure_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 6),
    _OilPressure_Type()
)
oilPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilPressure.setStatus("current")
if mibBuilder.loadTexts:
    oilPressure.setUnits("PSIG x10")


class _OilLowSwitch_Type(Integer32):
    """Custom type oilLowSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("coolantNotLow", 0),
          ("coolantLow", 1))
    )


_OilLowSwitch_Type.__name__ = "Integer32"
_OilLowSwitch_Object = MibScalar
oilLowSwitch = _OilLowSwitch_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 7),
    _OilLowSwitch_Type()
)
oilLowSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilLowSwitch.setStatus("current")


class _OilCriticallyLowSwitch_Type(Integer32):
    """Custom type oilCriticallyLowSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("coolantNotCriticallyLow", 0),
          ("coolantCriticallyLow", 1))
    )


_OilCriticallyLowSwitch_Type.__name__ = "Integer32"
_OilCriticallyLowSwitch_Object = MibScalar
oilCriticallyLowSwitch = _OilCriticallyLowSwitch_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 2, 8),
    _OilCriticallyLowSwitch_Type()
)
oilCriticallyLowSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilCriticallyLowSwitch.setStatus("current")
_OperationalData_ObjectIdentity = ObjectIdentity
operationalData = _OperationalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 3)
)
if mibBuilder.loadTexts:
    operationalData.setStatus("current")
_OilPumpSpeed_Type = Integer32
_OilPumpSpeed_Object = MibScalar
oilPumpSpeed = _OilPumpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 3, 1),
    _OilPumpSpeed_Type()
)
oilPumpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilPumpSpeed.setStatus("current")
if mibBuilder.loadTexts:
    oilPumpSpeed.setUnits("% x10")


class _OilValvePosition_Type(Integer32):
    """Custom type oilValvePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1),
          ("unknown", 2))
    )


_OilValvePosition_Type.__name__ = "Integer32"
_OilValvePosition_Object = MibScalar
oilValvePosition = _OilValvePosition_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 3, 2),
    _OilValvePosition_Type()
)
oilValvePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilValvePosition.setStatus("current")
_WaterValvePosition_Type = Integer32
_WaterValvePosition_Object = MibScalar
waterValvePosition = _WaterValvePosition_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 3, 3),
    _WaterValvePosition_Type()
)
waterValvePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterValvePosition.setStatus("current")
if mibBuilder.loadTexts:
    waterValvePosition.setUnits("% x10")


class _TimeOfDay_Type(DisplayString):
    """Custom type timeOfDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TimeOfDay_Type.__name__ = "DisplayString"
_TimeOfDay_Object = MibScalar
timeOfDay = _TimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 3, 4),
    _TimeOfDay_Type()
)
timeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfDay.setStatus("current")
_OperationalSettings_ObjectIdentity = ObjectIdentity
operationalSettings = _OperationalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4)
)
if mibBuilder.loadTexts:
    operationalSettings.setStatus("current")


class _StartTime_Type(DisplayString):
    """Custom type startTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_StartTime_Type.__name__ = "DisplayString"
_StartTime_Object = MibScalar
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 1),
    _StartTime_Type()
)
startTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startTime.setStatus("current")
_SetpointTemperature_Type = Integer32
_SetpointTemperature_Object = MibScalar
setpointTemperature = _SetpointTemperature_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 2),
    _SetpointTemperature_Type()
)
setpointTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpointTemperature.setStatus("current")
if mibBuilder.loadTexts:
    setpointTemperature.setUnits("deg C x10")
_OverTempWarning_Type = Integer32
_OverTempWarning_Object = MibScalar
overTempWarning = _OverTempWarning_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 3),
    _OverTempWarning_Type()
)
overTempWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overTempWarning.setStatus("current")
if mibBuilder.loadTexts:
    overTempWarning.setUnits("deg C x10")
_WaterTempErrorNotice_Type = Integer32
_WaterTempErrorNotice_Object = MibScalar
waterTempErrorNotice = _WaterTempErrorNotice_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 4),
    _WaterTempErrorNotice_Type()
)
waterTempErrorNotice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterTempErrorNotice.setStatus("current")
if mibBuilder.loadTexts:
    waterTempErrorNotice.setUnits("deg C x10")
_HighOilPressureThreshold_Type = Integer32
_HighOilPressureThreshold_Object = MibScalar
highOilPressureThreshold = _HighOilPressureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 5),
    _HighOilPressureThreshold_Type()
)
highOilPressureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highOilPressureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    highOilPressureThreshold.setUnits("PSIG x10")
_LowOilPressureThreshold_Type = Integer32
_LowOilPressureThreshold_Object = MibScalar
lowOilPressureThreshold = _LowOilPressureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 6),
    _LowOilPressureThreshold_Type()
)
lowOilPressureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowOilPressureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lowOilPressureThreshold.setUnits("PSIG x10")
_MaxPumpSpeed_Type = Integer32
_MaxPumpSpeed_Object = MibScalar
maxPumpSpeed = _MaxPumpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 7),
    _MaxPumpSpeed_Type()
)
maxPumpSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxPumpSpeed.setStatus("current")
if mibBuilder.loadTexts:
    maxPumpSpeed.setUnits("% x10")
_MaxDegCPerHrChange_Type = Integer32
_MaxDegCPerHrChange_Object = MibScalar
maxDegCPerHrChange = _MaxDegCPerHrChange_Object(
    (1, 3, 6, 1, 4, 1, 46926, 1, 3, 4, 8),
    _MaxDegCPerHrChange_Type()
)
maxDegCPerHrChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxDegCPerHrChange.setStatus("current")
if mibBuilder.loadTexts:
    maxDegCPerHrChange.setUnits("deg C/hr x10")

# Managed Objects groups


# Notification objects

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 46926, 1, 0, 1)
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        "deprecated"
    )

periodicTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 46926, 1, 0, 2)
)
if mibBuilder.loadTexts:
    periodicTrap.setStatus(
        "deprecated"
    )

startupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 46926, 1, 0, 3)
)
if mibBuilder.loadTexts:
    startupTrap.setStatus(
        "current"
    )

statusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 46926, 1, 0, 4)
)
if mibBuilder.loadTexts:
    statusChangeTrap.setStatus(
        "current"
    )

managementIpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 46926, 1, 0, 5)
)
if mibBuilder.loadTexts:
    managementIpTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIDAS-XCI-MIB",
    **{"midasgt": midasgt,
       "midasXCIProductMIB": midasXCIProductMIB,
       "trapNotifications": trapNotifications,
       "authenticationFailure": authenticationFailure,
       "periodicTrap": periodicTrap,
       "startupTrap": startupTrap,
       "statusChangeTrap": statusChangeTrap,
       "managementIpTrap": managementIpTrap,
       "product": product,
       "productName": productName,
       "productDescription": productDescription,
       "productSerialNbr": productSerialNbr,
       "applicationPartNbr": applicationPartNbr,
       "applicationVersion": applicationVersion,
       "bootloaderPartNbr": bootloaderPartNbr,
       "bootloaderVersion": bootloaderVersion,
       "hardwarePartNbr": hardwarePartNbr,
       "hardwareID": hardwareID,
       "setup": setup,
       "ipv4TrapTable": ipv4TrapTable,
       "ipv4TrapEntry": ipv4TrapEntry,
       "ipv4TrapReceiverNumber": ipv4TrapReceiverNumber,
       "ipv4TrapEnabled": ipv4TrapEnabled,
       "ipv4TrapReceiverIPAddress": ipv4TrapReceiverIPAddress,
       "ipv4TrapCommunity": ipv4TrapCommunity,
       "ipv4ManagerTable": ipv4ManagerTable,
       "ipv4ManagerEntry": ipv4ManagerEntry,
       "ipv4ManagerNumber": ipv4ManagerNumber,
       "ipv4ManagerEnabled": ipv4ManagerEnabled,
       "ipv4ManagerIPAddress": ipv4ManagerIPAddress,
       "tankInformation": tankInformation,
       "tankLocation": tankLocation,
       "tankChassisID": tankChassisID,
       "tankContactInfo": tankContactInfo,
       "control": control,
       "systemState": systemState,
       "overallStatus": overallStatus,
       "redundancyMode": redundancyMode,
       "controlType": controlType,
       "localSensorData": localSensorData,
       "waterInletTemperature": waterInletTemperature,
       "waterSaturation": waterSaturation,
       "oilInletTemperature": oilInletTemperature,
       "oilOutletTemperature": oilOutletTemperature,
       "oilTankTemperature": oilTankTemperature,
       "oilPressure": oilPressure,
       "oilLowSwitch": oilLowSwitch,
       "oilCriticallyLowSwitch": oilCriticallyLowSwitch,
       "operationalData": operationalData,
       "oilPumpSpeed": oilPumpSpeed,
       "oilValvePosition": oilValvePosition,
       "waterValvePosition": waterValvePosition,
       "timeOfDay": timeOfDay,
       "operationalSettings": operationalSettings,
       "startTime": startTime,
       "setpointTemperature": setpointTemperature,
       "overTempWarning": overTempWarning,
       "waterTempErrorNotice": waterTempErrorNotice,
       "highOilPressureThreshold": highOilPressureThreshold,
       "lowOilPressureThreshold": lowOilPressureThreshold,
       "maxPumpSpeed": maxPumpSpeed,
       "maxDegCPerHrChange": maxDegCPerHrChange}
)
