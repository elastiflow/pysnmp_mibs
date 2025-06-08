# SNMP MIB module (ASETEK-RACKCDU-SMI-V1-MIB-V16) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asetek_39829/ASETEK-RACKCDU-SMI-V1-MIB-V16.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:36:05 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName,
 sysObjectID,
 sysServices,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName",
    "sysObjectID",
    "sysServices",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asetek_ObjectIdentity = ObjectIdentity
asetek = _Asetek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829)
)
_RackCDU_ObjectIdentity = ObjectIdentity
rackCDU = _RackCDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1, 3),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("mandatory")
_RackNumber_Type = DisplayString
_RackNumber_Object = MibScalar
rackNumber = _RackNumber_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1, 4),
    _RackNumber_Type()
)
rackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackNumber.setStatus("mandatory")
_Description_Type = DisplayString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1, 5),
    _Description_Type()
)
description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("warning", 2),
          ("error", 3),
          ("unknown", 5))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 1, 6),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2)
)
_NotifyTable_Object = MibTable
notifyTable = _NotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2, 1)
)
if mibBuilder.loadTexts:
    notifyTable.setStatus("mandatory")
_NotifyEntry_Object = MibTableRow
notifyEntry = _NotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2, 1, 1)
)
notifyEntry.setIndexNames(
    (0, "ASETEK-RACKCDU-SMI-V1-MIB-V16", "notifyReceiverNumber"),
)
if mibBuilder.loadTexts:
    notifyEntry.setStatus("mandatory")


class _NotifyReceiverNumber_Type(Integer32):
    """Custom type notifyReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_NotifyReceiverNumber_Type.__name__ = "Integer32"
_NotifyReceiverNumber_Object = MibTableColumn
notifyReceiverNumber = _NotifyReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2, 1, 1, 1),
    _NotifyReceiverNumber_Type()
)
notifyReceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyReceiverNumber.setStatus("mandatory")


class _NotifyEnabled_Type(Integer32):
    """Custom type notifyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NotifyEnabled_Type.__name__ = "Integer32"
_NotifyEnabled_Object = MibTableColumn
notifyEnabled = _NotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2, 1, 1, 2),
    _NotifyEnabled_Type()
)
notifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notifyEnabled.setStatus("mandatory")
_NotifyReceiverIPAddress_Type = IpAddress
_NotifyReceiverIPAddress_Object = MibTableColumn
notifyReceiverIPAddress = _NotifyReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2, 1, 1, 3),
    _NotifyReceiverIPAddress_Type()
)
notifyReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notifyReceiverIPAddress.setStatus("mandatory")


class _NotifyCommunity_Type(DisplayString):
    """Custom type notifyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_NotifyCommunity_Type.__name__ = "DisplayString"
_NotifyCommunity_Object = MibTableColumn
notifyCommunity = _NotifyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 2, 1, 1, 4),
    _NotifyCommunity_Type()
)
notifyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notifyCommunity.setStatus("mandatory")
_Measurements_ObjectIdentity = ObjectIdentity
measurements = _Measurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3)
)


class _TemperatureFacilityIn_Type(Integer32):
    """Custom type temperatureFacilityIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-870, 999),
    )


_TemperatureFacilityIn_Type.__name__ = "Integer32"
_TemperatureFacilityIn_Object = MibScalar
temperatureFacilityIn = _TemperatureFacilityIn_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 100),
    _TemperatureFacilityIn_Type()
)
temperatureFacilityIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureFacilityIn.setStatus("mandatory")


class _TemperatureFacilityOut_Type(Integer32):
    """Custom type temperatureFacilityOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-870, 999),
    )


_TemperatureFacilityOut_Type.__name__ = "Integer32"
_TemperatureFacilityOut_Object = MibScalar
temperatureFacilityOut = _TemperatureFacilityOut_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 101),
    _TemperatureFacilityOut_Type()
)
temperatureFacilityOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureFacilityOut.setStatus("mandatory")


class _TemperatureServerIn_Type(Integer32):
    """Custom type temperatureServerIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-870, 999),
    )


_TemperatureServerIn_Type.__name__ = "Integer32"
_TemperatureServerIn_Object = MibScalar
temperatureServerIn = _TemperatureServerIn_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 102),
    _TemperatureServerIn_Type()
)
temperatureServerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureServerIn.setStatus("mandatory")


class _TemperatureServerOut_Type(Integer32):
    """Custom type temperatureServerOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-870, 999),
    )


_TemperatureServerOut_Type.__name__ = "Integer32"
_TemperatureServerOut_Object = MibScalar
temperatureServerOut = _TemperatureServerOut_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 103),
    _TemperatureServerOut_Type()
)
temperatureServerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureServerOut.setStatus("mandatory")


class _TemperatureAmbient_Type(Integer32):
    """Custom type temperatureAmbient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-870, 999),
    )


_TemperatureAmbient_Type.__name__ = "Integer32"
_TemperatureAmbient_Object = MibScalar
temperatureAmbient = _TemperatureAmbient_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 104),
    _TemperatureAmbient_Type()
)
temperatureAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAmbient.setStatus("obsolete")
_PressureServer_Type = Gauge32
_PressureServer_Object = MibScalar
pressureServer = _PressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 105),
    _PressureServer_Type()
)
pressureServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressureServer.setStatus("mandatory")
_PressureFacility_Type = Gauge32
_PressureFacility_Object = MibScalar
pressureFacility = _PressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 106),
    _PressureFacility_Type()
)
pressureFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressureFacility.setStatus("mandatory")


class _ServerLeak_Type(Integer32):
    """Custom type serverLeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("leak", 2))
    )


_ServerLeak_Type.__name__ = "Integer32"
_ServerLeak_Object = MibScalar
serverLeak = _ServerLeak_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 107),
    _ServerLeak_Type()
)
serverLeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLeak.setStatus("mandatory")


class _ServerLevel_Type(Integer32):
    """Custom type serverLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("low", 2))
    )


_ServerLevel_Type.__name__ = "Integer32"
_ServerLevel_Object = MibScalar
serverLevel = _ServerLevel_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 108),
    _ServerLevel_Type()
)
serverLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLevel.setStatus("mandatory")
_FlowFacility_Type = Gauge32
_FlowFacility_Object = MibScalar
flowFacility = _FlowFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 109),
    _FlowFacility_Type()
)
flowFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowFacility.setStatus("mandatory")
_Heatload_Type = Gauge32
_Heatload_Object = MibScalar
heatload = _Heatload_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 110),
    _Heatload_Type()
)
heatload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatload.setStatus("mandatory")
_ControllerOut_Type = Gauge32
_ControllerOut_Object = MibScalar
controllerOut = _ControllerOut_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 3, 111),
    _ControllerOut_Type()
)
controllerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerOut.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4)
)


class _IpStoreFlash_Type(Integer32):
    """Custom type ipStoreFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("store", 2))
    )


_IpStoreFlash_Type.__name__ = "Integer32"
_IpStoreFlash_Object = MibScalar
ipStoreFlash = _IpStoreFlash_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 91),
    _IpStoreFlash_Type()
)
ipStoreFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStoreFlash.setStatus("mandatory")


class _ModeOfOperation_Type(Integer32):
    """Custom type modeOfOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("agent", 1),
          ("master", 2))
    )


_ModeOfOperation_Type.__name__ = "Integer32"
_ModeOfOperation_Object = MibScalar
modeOfOperation = _ModeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 92),
    _ModeOfOperation_Type()
)
modeOfOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modeOfOperation.setStatus("mandatory")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 93),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("mandatory")
_PriDNS_Type = IpAddress
_PriDNS_Object = MibScalar
priDNS = _PriDNS_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 94),
    _PriDNS_Type()
)
priDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priDNS.setStatus("mandatory")
_SecDNS_Type = IpAddress
_SecDNS_Object = MibScalar
secDNS = _SecDNS_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 95),
    _SecDNS_Type()
)
secDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secDNS.setStatus("mandatory")
_NetMask_Type = IpAddress
_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 96),
    _NetMask_Type()
)
netMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMask.setStatus("mandatory")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 97),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("mandatory")


class _IpSrc_Type(Integer32):
    """Custom type ipSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_IpSrc_Type.__name__ = "Integer32"
_IpSrc_Object = MibScalar
ipSrc = _IpSrc_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 98),
    _IpSrc_Type()
)
ipSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSrc.setStatus("mandatory")


class _IpReboot_Type(Integer32):
    """Custom type ipReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reboot", 2))
    )


_IpReboot_Type.__name__ = "Integer32"
_IpReboot_Object = MibScalar
ipReboot = _IpReboot_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 4, 99),
    _IpReboot_Type()
)
ipReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipReboot.setStatus("mandatory")
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5)
)
_GainProportional_Type = DisplayString
_GainProportional_Object = MibScalar
gainProportional = _GainProportional_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 80),
    _GainProportional_Type()
)
gainProportional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gainProportional.setStatus("mandatory")
_GainIntegral_Type = DisplayString
_GainIntegral_Object = MibScalar
gainIntegral = _GainIntegral_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 81),
    _GainIntegral_Type()
)
gainIntegral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gainIntegral.setStatus("mandatory")
_GainDifferential_Type = DisplayString
_GainDifferential_Object = MibScalar
gainDifferential = _GainDifferential_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 82),
    _GainDifferential_Type()
)
gainDifferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gainDifferential.setStatus("mandatory")
_DeltaOutMax_Type = Gauge32
_DeltaOutMax_Object = MibScalar
deltaOutMax = _DeltaOutMax_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 83),
    _DeltaOutMax_Type()
)
deltaOutMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaOutMax.setStatus("mandatory")
_LimitPwmMax_Type = Gauge32
_LimitPwmMax_Object = MibScalar
limitPwmMax = _LimitPwmMax_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 84),
    _LimitPwmMax_Type()
)
limitPwmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitPwmMax.setStatus("mandatory")
_LimitPwmMin_Type = Gauge32
_LimitPwmMin_Object = MibScalar
limitPwmMin = _LimitPwmMin_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 85),
    _LimitPwmMin_Type()
)
limitPwmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitPwmMin.setStatus("mandatory")


class _SetpointFacilityOut_Type(Integer32):
    """Custom type setpointFacilityOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SetpointFacilityOut_Type.__name__ = "Integer32"
_SetpointFacilityOut_Object = MibScalar
setpointFacilityOut = _SetpointFacilityOut_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 86),
    _SetpointFacilityOut_Type()
)
setpointFacilityOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpointFacilityOut.setStatus("mandatory")
_ControllerOutAlpha_Type = DisplayString
_ControllerOutAlpha_Object = MibScalar
controllerOutAlpha = _ControllerOutAlpha_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 5, 87),
    _ControllerOutAlpha_Type()
)
controllerOutAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controllerOutAlpha.setStatus("mandatory")
_Units_ObjectIdentity = ObjectIdentity
units = _Units_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 6)
)


class _FluidHeatCapacity_Type(Integer32):
    """Custom type fluidHeatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_FluidHeatCapacity_Type.__name__ = "Integer32"
_FluidHeatCapacity_Object = MibScalar
fluidHeatCapacity = _FluidHeatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 6, 70),
    _FluidHeatCapacity_Type()
)
fluidHeatCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fluidHeatCapacity.setStatus("mandatory")
_HeatAverageFactor_Type = Gauge32
_HeatAverageFactor_Object = MibScalar
heatAverageFactor = _HeatAverageFactor_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 6, 71),
    _HeatAverageFactor_Type()
)
heatAverageFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heatAverageFactor.setStatus("mandatory")
_HarnessVersion_Type = Gauge32
_HarnessVersion_Object = MibScalar
harnessVersion = _HarnessVersion_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 6, 72),
    _HarnessVersion_Type()
)
harnessVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    harnessVersion.setStatus("mandatory")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7)
)


class _SnmpTrapsAlarmEnable_Type(Integer32):
    """Custom type snmpTrapsAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SnmpTrapsAlarmEnable_Type.__name__ = "Integer32"
_SnmpTrapsAlarmEnable_Object = MibScalar
snmpTrapsAlarmEnable = _SnmpTrapsAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 150),
    _SnmpTrapsAlarmEnable_Type()
)
snmpTrapsAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsAlarmEnable.setStatus("mandatory")


class _SnmpTrapsWarningEnable_Type(Integer32):
    """Custom type snmpTrapsWarningEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SnmpTrapsWarningEnable_Type.__name__ = "Integer32"
_SnmpTrapsWarningEnable_Object = MibScalar
snmpTrapsWarningEnable = _SnmpTrapsWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 151),
    _SnmpTrapsWarningEnable_Type()
)
snmpTrapsWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsWarningEnable.setStatus("mandatory")


class _SmtpTrapsAlarmEnable_Type(Integer32):
    """Custom type smtpTrapsAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SmtpTrapsAlarmEnable_Type.__name__ = "Integer32"
_SmtpTrapsAlarmEnable_Object = MibScalar
smtpTrapsAlarmEnable = _SmtpTrapsAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 152),
    _SmtpTrapsAlarmEnable_Type()
)
smtpTrapsAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTrapsAlarmEnable.setStatus("mandatory")


class _SmtpTrapsWarningEnable_Type(Integer32):
    """Custom type smtpTrapsWarningEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SmtpTrapsWarningEnable_Type.__name__ = "Integer32"
_SmtpTrapsWarningEnable_Object = MibScalar
smtpTrapsWarningEnable = _SmtpTrapsWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 153),
    _SmtpTrapsWarningEnable_Type()
)
smtpTrapsWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTrapsWarningEnable.setStatus("mandatory")


class _WarningMinFi_Type(Integer32):
    """Custom type warningMinFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMinFi_Type.__name__ = "Integer32"
_WarningMinFi_Object = MibScalar
warningMinFi = _WarningMinFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 154),
    _WarningMinFi_Type()
)
warningMinFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinFi.setStatus("mandatory")


class _WarningMinEnableFi_Type(Integer32):
    """Custom type warningMinEnableFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnableFi_Type.__name__ = "Integer32"
_WarningMinEnableFi_Object = MibScalar
warningMinEnableFi = _WarningMinEnableFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 155),
    _WarningMinEnableFi_Type()
)
warningMinEnableFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnableFi.setStatus("mandatory")


class _WarningMaxFi_Type(Integer32):
    """Custom type warningMaxFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMaxFi_Type.__name__ = "Integer32"
_WarningMaxFi_Object = MibScalar
warningMaxFi = _WarningMaxFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 156),
    _WarningMaxFi_Type()
)
warningMaxFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxFi.setStatus("mandatory")


class _WarningMaxEnableFi_Type(Integer32):
    """Custom type warningMaxEnableFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnableFi_Type.__name__ = "Integer32"
_WarningMaxEnableFi_Object = MibScalar
warningMaxEnableFi = _WarningMaxEnableFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 157),
    _WarningMaxEnableFi_Type()
)
warningMaxEnableFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnableFi.setStatus("mandatory")


class _AlarmMinFi_Type(Integer32):
    """Custom type alarmMinFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMinFi_Type.__name__ = "Integer32"
_AlarmMinFi_Object = MibScalar
alarmMinFi = _AlarmMinFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 158),
    _AlarmMinFi_Type()
)
alarmMinFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinFi.setStatus("mandatory")


class _AlarmMinEnableFi_Type(Integer32):
    """Custom type alarmMinEnableFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnableFi_Type.__name__ = "Integer32"
_AlarmMinEnableFi_Object = MibScalar
alarmMinEnableFi = _AlarmMinEnableFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 159),
    _AlarmMinEnableFi_Type()
)
alarmMinEnableFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnableFi.setStatus("mandatory")


class _AlarmMaxFi_Type(Integer32):
    """Custom type alarmMaxFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMaxFi_Type.__name__ = "Integer32"
_AlarmMaxFi_Object = MibScalar
alarmMaxFi = _AlarmMaxFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 160),
    _AlarmMaxFi_Type()
)
alarmMaxFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxFi.setStatus("mandatory")


class _AlarmMaxEnableFi_Type(Integer32):
    """Custom type alarmMaxEnableFi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnableFi_Type.__name__ = "Integer32"
_AlarmMaxEnableFi_Object = MibScalar
alarmMaxEnableFi = _AlarmMaxEnableFi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 161),
    _AlarmMaxEnableFi_Type()
)
alarmMaxEnableFi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnableFi.setStatus("mandatory")


class _WarningMinFo_Type(Integer32):
    """Custom type warningMinFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMinFo_Type.__name__ = "Integer32"
_WarningMinFo_Object = MibScalar
warningMinFo = _WarningMinFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 162),
    _WarningMinFo_Type()
)
warningMinFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinFo.setStatus("mandatory")


class _WarningMinEnableFo_Type(Integer32):
    """Custom type warningMinEnableFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnableFo_Type.__name__ = "Integer32"
_WarningMinEnableFo_Object = MibScalar
warningMinEnableFo = _WarningMinEnableFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 163),
    _WarningMinEnableFo_Type()
)
warningMinEnableFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnableFo.setStatus("mandatory")


class _WarningMaxFo_Type(Integer32):
    """Custom type warningMaxFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMaxFo_Type.__name__ = "Integer32"
_WarningMaxFo_Object = MibScalar
warningMaxFo = _WarningMaxFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 164),
    _WarningMaxFo_Type()
)
warningMaxFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxFo.setStatus("mandatory")


class _WarningMaxEnableFo_Type(Integer32):
    """Custom type warningMaxEnableFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnableFo_Type.__name__ = "Integer32"
_WarningMaxEnableFo_Object = MibScalar
warningMaxEnableFo = _WarningMaxEnableFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 165),
    _WarningMaxEnableFo_Type()
)
warningMaxEnableFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnableFo.setStatus("mandatory")


class _AlarmMinFo_Type(Integer32):
    """Custom type alarmMinFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMinFo_Type.__name__ = "Integer32"
_AlarmMinFo_Object = MibScalar
alarmMinFo = _AlarmMinFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 166),
    _AlarmMinFo_Type()
)
alarmMinFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinFo.setStatus("mandatory")


class _AlarmMinEnableFo_Type(Integer32):
    """Custom type alarmMinEnableFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnableFo_Type.__name__ = "Integer32"
_AlarmMinEnableFo_Object = MibScalar
alarmMinEnableFo = _AlarmMinEnableFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 167),
    _AlarmMinEnableFo_Type()
)
alarmMinEnableFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnableFo.setStatus("mandatory")


class _AlarmMaxFo_Type(Integer32):
    """Custom type alarmMaxFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMaxFo_Type.__name__ = "Integer32"
_AlarmMaxFo_Object = MibScalar
alarmMaxFo = _AlarmMaxFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 168),
    _AlarmMaxFo_Type()
)
alarmMaxFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxFo.setStatus("mandatory")


class _AlarmMaxEnableFo_Type(Integer32):
    """Custom type alarmMaxEnableFo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnableFo_Type.__name__ = "Integer32"
_AlarmMaxEnableFo_Object = MibScalar
alarmMaxEnableFo = _AlarmMaxEnableFo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 169),
    _AlarmMaxEnableFo_Type()
)
alarmMaxEnableFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnableFo.setStatus("mandatory")


class _WarningMinSi_Type(Integer32):
    """Custom type warningMinSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMinSi_Type.__name__ = "Integer32"
_WarningMinSi_Object = MibScalar
warningMinSi = _WarningMinSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 170),
    _WarningMinSi_Type()
)
warningMinSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinSi.setStatus("mandatory")


class _WarningMinEnableSi_Type(Integer32):
    """Custom type warningMinEnableSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnableSi_Type.__name__ = "Integer32"
_WarningMinEnableSi_Object = MibScalar
warningMinEnableSi = _WarningMinEnableSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 171),
    _WarningMinEnableSi_Type()
)
warningMinEnableSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnableSi.setStatus("mandatory")


class _WarningMaxSi_Type(Integer32):
    """Custom type warningMaxSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMaxSi_Type.__name__ = "Integer32"
_WarningMaxSi_Object = MibScalar
warningMaxSi = _WarningMaxSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 172),
    _WarningMaxSi_Type()
)
warningMaxSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxSi.setStatus("mandatory")


class _WarningMaxEnableSi_Type(Integer32):
    """Custom type warningMaxEnableSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnableSi_Type.__name__ = "Integer32"
_WarningMaxEnableSi_Object = MibScalar
warningMaxEnableSi = _WarningMaxEnableSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 173),
    _WarningMaxEnableSi_Type()
)
warningMaxEnableSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnableSi.setStatus("mandatory")


class _AlarmMinSi_Type(Integer32):
    """Custom type alarmMinSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMinSi_Type.__name__ = "Integer32"
_AlarmMinSi_Object = MibScalar
alarmMinSi = _AlarmMinSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 174),
    _AlarmMinSi_Type()
)
alarmMinSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinSi.setStatus("mandatory")


class _AlarmMinEnableSi_Type(Integer32):
    """Custom type alarmMinEnableSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnableSi_Type.__name__ = "Integer32"
_AlarmMinEnableSi_Object = MibScalar
alarmMinEnableSi = _AlarmMinEnableSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 175),
    _AlarmMinEnableSi_Type()
)
alarmMinEnableSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnableSi.setStatus("mandatory")


class _AlarmMaxSi_Type(Integer32):
    """Custom type alarmMaxSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMaxSi_Type.__name__ = "Integer32"
_AlarmMaxSi_Object = MibScalar
alarmMaxSi = _AlarmMaxSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 176),
    _AlarmMaxSi_Type()
)
alarmMaxSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxSi.setStatus("mandatory")


class _AlarmMaxEnableSi_Type(Integer32):
    """Custom type alarmMaxEnableSi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnableSi_Type.__name__ = "Integer32"
_AlarmMaxEnableSi_Object = MibScalar
alarmMaxEnableSi = _AlarmMaxEnableSi_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 177),
    _AlarmMaxEnableSi_Type()
)
alarmMaxEnableSi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnableSi.setStatus("mandatory")


class _WarningMinSo_Type(Integer32):
    """Custom type warningMinSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMinSo_Type.__name__ = "Integer32"
_WarningMinSo_Object = MibScalar
warningMinSo = _WarningMinSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 178),
    _WarningMinSo_Type()
)
warningMinSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinSo.setStatus("mandatory")


class _WarningMinEnableSo_Type(Integer32):
    """Custom type warningMinEnableSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnableSo_Type.__name__ = "Integer32"
_WarningMinEnableSo_Object = MibScalar
warningMinEnableSo = _WarningMinEnableSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 179),
    _WarningMinEnableSo_Type()
)
warningMinEnableSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnableSo.setStatus("mandatory")


class _WarningMaxSo_Type(Integer32):
    """Custom type warningMaxSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_WarningMaxSo_Type.__name__ = "Integer32"
_WarningMaxSo_Object = MibScalar
warningMaxSo = _WarningMaxSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 180),
    _WarningMaxSo_Type()
)
warningMaxSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxSo.setStatus("mandatory")


class _WarningMaxEnableSo_Type(Integer32):
    """Custom type warningMaxEnableSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnableSo_Type.__name__ = "Integer32"
_WarningMaxEnableSo_Object = MibScalar
warningMaxEnableSo = _WarningMaxEnableSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 181),
    _WarningMaxEnableSo_Type()
)
warningMaxEnableSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnableSo.setStatus("mandatory")


class _AlarmMinSo_Type(Integer32):
    """Custom type alarmMinSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMinSo_Type.__name__ = "Integer32"
_AlarmMinSo_Object = MibScalar
alarmMinSo = _AlarmMinSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 182),
    _AlarmMinSo_Type()
)
alarmMinSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinSo.setStatus("mandatory")


class _AlarmMinEnableSo_Type(Integer32):
    """Custom type alarmMinEnableSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnableSo_Type.__name__ = "Integer32"
_AlarmMinEnableSo_Object = MibScalar
alarmMinEnableSo = _AlarmMinEnableSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 183),
    _AlarmMinEnableSo_Type()
)
alarmMinEnableSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnableSo.setStatus("mandatory")


class _AlarmMaxSo_Type(Integer32):
    """Custom type alarmMaxSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, 75),
    )


_AlarmMaxSo_Type.__name__ = "Integer32"
_AlarmMaxSo_Object = MibScalar
alarmMaxSo = _AlarmMaxSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 184),
    _AlarmMaxSo_Type()
)
alarmMaxSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxSo.setStatus("mandatory")


class _AlarmMaxEnableSo_Type(Integer32):
    """Custom type alarmMaxEnableSo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnableSo_Type.__name__ = "Integer32"
_AlarmMaxEnableSo_Object = MibScalar
alarmMaxEnableSo = _AlarmMaxEnableSo_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 185),
    _AlarmMaxEnableSo_Type()
)
alarmMaxEnableSo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnableSo.setStatus("mandatory")


class _WarningMinFlow_Type(Integer32):
    """Custom type warningMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500000),
    )


_WarningMinFlow_Type.__name__ = "Integer32"
_WarningMinFlow_Object = MibScalar
warningMinFlow = _WarningMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 186),
    _WarningMinFlow_Type()
)
warningMinFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinFlow.setStatus("mandatory")


class _WarningMinEnableFlow_Type(Integer32):
    """Custom type warningMinEnableFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnableFlow_Type.__name__ = "Integer32"
_WarningMinEnableFlow_Object = MibScalar
warningMinEnableFlow = _WarningMinEnableFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 187),
    _WarningMinEnableFlow_Type()
)
warningMinEnableFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnableFlow.setStatus("mandatory")


class _WarningMaxFlow_Type(Integer32):
    """Custom type warningMaxFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500000),
    )


_WarningMaxFlow_Type.__name__ = "Integer32"
_WarningMaxFlow_Object = MibScalar
warningMaxFlow = _WarningMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 188),
    _WarningMaxFlow_Type()
)
warningMaxFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxFlow.setStatus("mandatory")


class _WarningMaxEnableFlow_Type(Integer32):
    """Custom type warningMaxEnableFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnableFlow_Type.__name__ = "Integer32"
_WarningMaxEnableFlow_Object = MibScalar
warningMaxEnableFlow = _WarningMaxEnableFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 189),
    _WarningMaxEnableFlow_Type()
)
warningMaxEnableFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnableFlow.setStatus("mandatory")


class _AlarmMinFlow_Type(Integer32):
    """Custom type alarmMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500000),
    )


_AlarmMinFlow_Type.__name__ = "Integer32"
_AlarmMinFlow_Object = MibScalar
alarmMinFlow = _AlarmMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 190),
    _AlarmMinFlow_Type()
)
alarmMinFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinFlow.setStatus("mandatory")


class _AlarmMinEnableFlow_Type(Integer32):
    """Custom type alarmMinEnableFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnableFlow_Type.__name__ = "Integer32"
_AlarmMinEnableFlow_Object = MibScalar
alarmMinEnableFlow = _AlarmMinEnableFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 191),
    _AlarmMinEnableFlow_Type()
)
alarmMinEnableFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnableFlow.setStatus("mandatory")


class _AlarmMaxFlow_Type(Integer32):
    """Custom type alarmMaxFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500000),
    )


_AlarmMaxFlow_Type.__name__ = "Integer32"
_AlarmMaxFlow_Object = MibScalar
alarmMaxFlow = _AlarmMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 192),
    _AlarmMaxFlow_Type()
)
alarmMaxFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxFlow.setStatus("mandatory")


class _AlarmMaxEnableFlow_Type(Integer32):
    """Custom type alarmMaxEnableFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnableFlow_Type.__name__ = "Integer32"
_AlarmMaxEnableFlow_Object = MibScalar
alarmMaxEnableFlow = _AlarmMaxEnableFlow_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 193),
    _AlarmMaxEnableFlow_Type()
)
alarmMaxEnableFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnableFlow.setStatus("mandatory")


class _WarningMinPressureServer_Type(Integer32):
    """Custom type warningMinPressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_WarningMinPressureServer_Type.__name__ = "Integer32"
_WarningMinPressureServer_Object = MibScalar
warningMinPressureServer = _WarningMinPressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 194),
    _WarningMinPressureServer_Type()
)
warningMinPressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinPressureServer.setStatus("mandatory")


class _WarningMinEnablePressureServer_Type(Integer32):
    """Custom type warningMinEnablePressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnablePressureServer_Type.__name__ = "Integer32"
_WarningMinEnablePressureServer_Object = MibScalar
warningMinEnablePressureServer = _WarningMinEnablePressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 195),
    _WarningMinEnablePressureServer_Type()
)
warningMinEnablePressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnablePressureServer.setStatus("mandatory")


class _WarningMaxPressureServer_Type(Integer32):
    """Custom type warningMaxPressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_WarningMaxPressureServer_Type.__name__ = "Integer32"
_WarningMaxPressureServer_Object = MibScalar
warningMaxPressureServer = _WarningMaxPressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 196),
    _WarningMaxPressureServer_Type()
)
warningMaxPressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxPressureServer.setStatus("mandatory")


class _WarningMaxEnablePressureServer_Type(Integer32):
    """Custom type warningMaxEnablePressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnablePressureServer_Type.__name__ = "Integer32"
_WarningMaxEnablePressureServer_Object = MibScalar
warningMaxEnablePressureServer = _WarningMaxEnablePressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 197),
    _WarningMaxEnablePressureServer_Type()
)
warningMaxEnablePressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnablePressureServer.setStatus("mandatory")


class _AlarmMinPressureServer_Type(Integer32):
    """Custom type alarmMinPressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_AlarmMinPressureServer_Type.__name__ = "Integer32"
_AlarmMinPressureServer_Object = MibScalar
alarmMinPressureServer = _AlarmMinPressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 198),
    _AlarmMinPressureServer_Type()
)
alarmMinPressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinPressureServer.setStatus("mandatory")


class _AlarmMinEnablePressureServer_Type(Integer32):
    """Custom type alarmMinEnablePressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnablePressureServer_Type.__name__ = "Integer32"
_AlarmMinEnablePressureServer_Object = MibScalar
alarmMinEnablePressureServer = _AlarmMinEnablePressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 199),
    _AlarmMinEnablePressureServer_Type()
)
alarmMinEnablePressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnablePressureServer.setStatus("mandatory")


class _AlarmMaxPressureServer_Type(Integer32):
    """Custom type alarmMaxPressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_AlarmMaxPressureServer_Type.__name__ = "Integer32"
_AlarmMaxPressureServer_Object = MibScalar
alarmMaxPressureServer = _AlarmMaxPressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 200),
    _AlarmMaxPressureServer_Type()
)
alarmMaxPressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxPressureServer.setStatus("mandatory")


class _AlarmMaxEnablePressureServer_Type(Integer32):
    """Custom type alarmMaxEnablePressureServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnablePressureServer_Type.__name__ = "Integer32"
_AlarmMaxEnablePressureServer_Object = MibScalar
alarmMaxEnablePressureServer = _AlarmMaxEnablePressureServer_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 201),
    _AlarmMaxEnablePressureServer_Type()
)
alarmMaxEnablePressureServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnablePressureServer.setStatus("mandatory")


class _WarningMinPressureFacility_Type(Integer32):
    """Custom type warningMinPressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_WarningMinPressureFacility_Type.__name__ = "Integer32"
_WarningMinPressureFacility_Object = MibScalar
warningMinPressureFacility = _WarningMinPressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 202),
    _WarningMinPressureFacility_Type()
)
warningMinPressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinPressureFacility.setStatus("mandatory")


class _WarningMinEnablePressureFacility_Type(Integer32):
    """Custom type warningMinEnablePressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMinEnablePressureFacility_Type.__name__ = "Integer32"
_WarningMinEnablePressureFacility_Object = MibScalar
warningMinEnablePressureFacility = _WarningMinEnablePressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 203),
    _WarningMinEnablePressureFacility_Type()
)
warningMinEnablePressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMinEnablePressureFacility.setStatus("mandatory")


class _WarningMaxPressureFacility_Type(Integer32):
    """Custom type warningMaxPressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_WarningMaxPressureFacility_Type.__name__ = "Integer32"
_WarningMaxPressureFacility_Object = MibScalar
warningMaxPressureFacility = _WarningMaxPressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 204),
    _WarningMaxPressureFacility_Type()
)
warningMaxPressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxPressureFacility.setStatus("mandatory")


class _WarningMaxEnablePressureFacility_Type(Integer32):
    """Custom type warningMaxEnablePressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WarningMaxEnablePressureFacility_Type.__name__ = "Integer32"
_WarningMaxEnablePressureFacility_Object = MibScalar
warningMaxEnablePressureFacility = _WarningMaxEnablePressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 205),
    _WarningMaxEnablePressureFacility_Type()
)
warningMaxEnablePressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warningMaxEnablePressureFacility.setStatus("mandatory")


class _AlarmMinPressureFacility_Type(Integer32):
    """Custom type alarmMinPressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_AlarmMinPressureFacility_Type.__name__ = "Integer32"
_AlarmMinPressureFacility_Object = MibScalar
alarmMinPressureFacility = _AlarmMinPressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 206),
    _AlarmMinPressureFacility_Type()
)
alarmMinPressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinPressureFacility.setStatus("mandatory")


class _AlarmMinEnablePressureFacility_Type(Integer32):
    """Custom type alarmMinEnablePressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMinEnablePressureFacility_Type.__name__ = "Integer32"
_AlarmMinEnablePressureFacility_Object = MibScalar
alarmMinEnablePressureFacility = _AlarmMinEnablePressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 207),
    _AlarmMinEnablePressureFacility_Type()
)
alarmMinEnablePressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMinEnablePressureFacility.setStatus("mandatory")


class _AlarmMaxPressureFacility_Type(Integer32):
    """Custom type alarmMaxPressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_AlarmMaxPressureFacility_Type.__name__ = "Integer32"
_AlarmMaxPressureFacility_Object = MibScalar
alarmMaxPressureFacility = _AlarmMaxPressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 208),
    _AlarmMaxPressureFacility_Type()
)
alarmMaxPressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxPressureFacility.setStatus("mandatory")


class _AlarmMaxEnablePressureFacility_Type(Integer32):
    """Custom type alarmMaxEnablePressureFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmMaxEnablePressureFacility_Type.__name__ = "Integer32"
_AlarmMaxEnablePressureFacility_Object = MibScalar
alarmMaxEnablePressureFacility = _AlarmMaxEnablePressureFacility_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 209),
    _AlarmMaxEnablePressureFacility_Type()
)
alarmMaxEnablePressureFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaxEnablePressureFacility.setStatus("mandatory")


class _AlarmEnableLeak_Type(Integer32):
    """Custom type alarmEnableLeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmEnableLeak_Type.__name__ = "Integer32"
_AlarmEnableLeak_Object = MibScalar
alarmEnableLeak = _AlarmEnableLeak_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 210),
    _AlarmEnableLeak_Type()
)
alarmEnableLeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEnableLeak.setStatus("mandatory")


class _AlarmEnableLevel_Type(Integer32):
    """Custom type alarmEnableLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AlarmEnableLevel_Type.__name__ = "Integer32"
_AlarmEnableLevel_Object = MibScalar
alarmEnableLevel = _AlarmEnableLevel_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 7, 211),
    _AlarmEnableLevel_Type()
)
alarmEnableLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEnableLevel.setStatus("mandatory")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8)
)
_CduProdGroup_ObjectIdentity = ObjectIdentity
cduProdGroup = _CduProdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 1)
)
_CduSetupGroup_ObjectIdentity = ObjectIdentity
cduSetupGroup = _CduSetupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 2)
)
_CduMeasGroup_ObjectIdentity = ObjectIdentity
cduMeasGroup = _CduMeasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 3)
)
_CduMeasGroupRev2_ObjectIdentity = ObjectIdentity
cduMeasGroupRev2 = _CduMeasGroupRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 4)
)
_CduNetGroup_ObjectIdentity = ObjectIdentity
cduNetGroup = _CduNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 5)
)
_CduCntlGroup_ObjectIdentity = ObjectIdentity
cduCntlGroup = _CduCntlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 6)
)
_CduUnitGroup_ObjectIdentity = ObjectIdentity
cduUnitGroup = _CduUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 7)
)
_CduNotifyGroup_ObjectIdentity = ObjectIdentity
cduNotifyGroup = _CduNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 8)
)
_CduTrapGroup_ObjectIdentity = ObjectIdentity
cduTrapGroup = _CduTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 9)
)
_CduCompliances_ObjectIdentity = ObjectIdentity
cduCompliances = _CduCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 10)
)
_CduEventGroup_ObjectIdentity = ObjectIdentity
cduEventGroup = _CduEventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 11)
)
_CduTrapGroupRev2_ObjectIdentity = ObjectIdentity
cduTrapGroupRev2 = _CduTrapGroupRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 12)
)
_CduCompliancesRev2_ObjectIdentity = ObjectIdentity
cduCompliancesRev2 = _CduCompliancesRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 8, 13)
)
_EventDescriptors_ObjectIdentity = ObjectIdentity
eventDescriptors = _EventDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39829, 1, 9)
)
_EventDescription_Type = DisplayString
_EventDescription_Object = MibScalar
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 9, 1),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("mandatory")
_EventValue_Type = Integer32
_EventValue_Object = MibScalar
eventValue = _EventValue_Object(
    (1, 3, 6, 1, 4, 1, 39829, 1, 9, 2),
    _EventValue_Type()
)
eventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 500)
)
alarmNotify.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventValue"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"))
)
if mibBuilder.loadTexts:
    alarmNotify.setStatus(
        ""
    )

warningNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 501)
)
warningNotify.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventValue"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"))
)
if mibBuilder.loadTexts:
    warningNotify.setStatus(
        ""
    )

facilitySupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 504)
)
facilitySupplyWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureFacilityIn"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilitySupplyWarning.setStatus(
        ""
    )

facilityReturnWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 505)
)
facilityReturnWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureFacilityOut"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilityReturnWarning.setStatus(
        ""
    )

serverSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 506)
)
serverSupplyWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureServerIn"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    serverSupplyWarning.setStatus(
        ""
    )

serverReturnWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 507)
)
serverReturnWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureServerOut"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    serverReturnWarning.setStatus(
        ""
    )

facilityPressureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 508)
)
facilityPressureWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "pressureFacility"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilityPressureWarning.setStatus(
        ""
    )

serverPressureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 509)
)
serverPressureWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "pressureServer"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    serverPressureWarning.setStatus(
        ""
    )

facilityFlowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 512)
)
facilityFlowWarning.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "flowFacility"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilityFlowWarning.setStatus(
        ""
    )

facilitySupplyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 517)
)
facilitySupplyAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureFacilityIn"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilitySupplyAlarm.setStatus(
        ""
    )

facilityReturnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 518)
)
facilityReturnAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureFacilityOut"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilityReturnAlarm.setStatus(
        ""
    )

serverSupplyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 519)
)
serverSupplyAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureServerIn"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    serverSupplyAlarm.setStatus(
        ""
    )

serverReturnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 520)
)
serverReturnAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "temperatureServerOut"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    serverReturnAlarm.setStatus(
        ""
    )

facilityPressureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 521)
)
facilityPressureAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "pressureFacility"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilityPressureAlarm.setStatus(
        ""
    )

serverPressureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 522)
)
serverPressureAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "pressureServer"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    serverPressureAlarm.setStatus(
        ""
    )

leakDetectionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 523)
)
leakDetectionAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "serverLeak"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    leakDetectionAlarm.setStatus(
        ""
    )

liquidLevelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 524)
)
liquidLevelAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "serverLevel"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    liquidLevelAlarm.setStatus(
        ""
    )

facilityFlowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39829, 1, 0, 525)
)
facilityFlowAlarm.setObjects(
      *(("ASETEK-RACKCDU-SMI-V1-MIB-V16", "flowFacility"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "eventDescription"),
        ("ASETEK-RACKCDU-SMI-V1-MIB-V16", "rackNumber"))
)
if mibBuilder.loadTexts:
    facilityFlowAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASETEK-RACKCDU-SMI-V1-MIB-V16",
    **{"asetek": asetek,
       "rackCDU": rackCDU,
       "traps": traps,
       "alarmNotify": alarmNotify,
       "warningNotify": warningNotify,
       "facilitySupplyWarning": facilitySupplyWarning,
       "facilityReturnWarning": facilityReturnWarning,
       "serverSupplyWarning": serverSupplyWarning,
       "serverReturnWarning": serverReturnWarning,
       "facilityPressureWarning": facilityPressureWarning,
       "serverPressureWarning": serverPressureWarning,
       "facilityFlowWarning": facilityFlowWarning,
       "facilitySupplyAlarm": facilitySupplyAlarm,
       "facilityReturnAlarm": facilityReturnAlarm,
       "serverSupplyAlarm": serverSupplyAlarm,
       "serverReturnAlarm": serverReturnAlarm,
       "facilityPressureAlarm": facilityPressureAlarm,
       "serverPressureAlarm": serverPressureAlarm,
       "leakDetectionAlarm": leakDetectionAlarm,
       "liquidLevelAlarm": liquidLevelAlarm,
       "facilityFlowAlarm": facilityFlowAlarm,
       "product": product,
       "name": name,
       "version": version,
       "date": date,
       "rackNumber": rackNumber,
       "description": description,
       "status": status,
       "setup": setup,
       "notifyTable": notifyTable,
       "notifyEntry": notifyEntry,
       "notifyReceiverNumber": notifyReceiverNumber,
       "notifyEnabled": notifyEnabled,
       "notifyReceiverIPAddress": notifyReceiverIPAddress,
       "notifyCommunity": notifyCommunity,
       "measurements": measurements,
       "temperatureFacilityIn": temperatureFacilityIn,
       "temperatureFacilityOut": temperatureFacilityOut,
       "temperatureServerIn": temperatureServerIn,
       "temperatureServerOut": temperatureServerOut,
       "temperatureAmbient": temperatureAmbient,
       "pressureServer": pressureServer,
       "pressureFacility": pressureFacility,
       "serverLeak": serverLeak,
       "serverLevel": serverLevel,
       "flowFacility": flowFacility,
       "heatload": heatload,
       "controllerOut": controllerOut,
       "network": network,
       "ipStoreFlash": ipStoreFlash,
       "modeOfOperation": modeOfOperation,
       "ipAddr": ipAddr,
       "priDNS": priDNS,
       "secDNS": secDNS,
       "netMask": netMask,
       "gateway": gateway,
       "ipSrc": ipSrc,
       "ipReboot": ipReboot,
       "controller": controller,
       "gainProportional": gainProportional,
       "gainIntegral": gainIntegral,
       "gainDifferential": gainDifferential,
       "deltaOutMax": deltaOutMax,
       "limitPwmMax": limitPwmMax,
       "limitPwmMin": limitPwmMin,
       "setpointFacilityOut": setpointFacilityOut,
       "controllerOutAlpha": controllerOutAlpha,
       "units": units,
       "fluidHeatCapacity": fluidHeatCapacity,
       "heatAverageFactor": heatAverageFactor,
       "harnessVersion": harnessVersion,
       "notifications": notifications,
       "snmpTrapsAlarmEnable": snmpTrapsAlarmEnable,
       "snmpTrapsWarningEnable": snmpTrapsWarningEnable,
       "smtpTrapsAlarmEnable": smtpTrapsAlarmEnable,
       "smtpTrapsWarningEnable": smtpTrapsWarningEnable,
       "warningMinFi": warningMinFi,
       "warningMinEnableFi": warningMinEnableFi,
       "warningMaxFi": warningMaxFi,
       "warningMaxEnableFi": warningMaxEnableFi,
       "alarmMinFi": alarmMinFi,
       "alarmMinEnableFi": alarmMinEnableFi,
       "alarmMaxFi": alarmMaxFi,
       "alarmMaxEnableFi": alarmMaxEnableFi,
       "warningMinFo": warningMinFo,
       "warningMinEnableFo": warningMinEnableFo,
       "warningMaxFo": warningMaxFo,
       "warningMaxEnableFo": warningMaxEnableFo,
       "alarmMinFo": alarmMinFo,
       "alarmMinEnableFo": alarmMinEnableFo,
       "alarmMaxFo": alarmMaxFo,
       "alarmMaxEnableFo": alarmMaxEnableFo,
       "warningMinSi": warningMinSi,
       "warningMinEnableSi": warningMinEnableSi,
       "warningMaxSi": warningMaxSi,
       "warningMaxEnableSi": warningMaxEnableSi,
       "alarmMinSi": alarmMinSi,
       "alarmMinEnableSi": alarmMinEnableSi,
       "alarmMaxSi": alarmMaxSi,
       "alarmMaxEnableSi": alarmMaxEnableSi,
       "warningMinSo": warningMinSo,
       "warningMinEnableSo": warningMinEnableSo,
       "warningMaxSo": warningMaxSo,
       "warningMaxEnableSo": warningMaxEnableSo,
       "alarmMinSo": alarmMinSo,
       "alarmMinEnableSo": alarmMinEnableSo,
       "alarmMaxSo": alarmMaxSo,
       "alarmMaxEnableSo": alarmMaxEnableSo,
       "warningMinFlow": warningMinFlow,
       "warningMinEnableFlow": warningMinEnableFlow,
       "warningMaxFlow": warningMaxFlow,
       "warningMaxEnableFlow": warningMaxEnableFlow,
       "alarmMinFlow": alarmMinFlow,
       "alarmMinEnableFlow": alarmMinEnableFlow,
       "alarmMaxFlow": alarmMaxFlow,
       "alarmMaxEnableFlow": alarmMaxEnableFlow,
       "warningMinPressureServer": warningMinPressureServer,
       "warningMinEnablePressureServer": warningMinEnablePressureServer,
       "warningMaxPressureServer": warningMaxPressureServer,
       "warningMaxEnablePressureServer": warningMaxEnablePressureServer,
       "alarmMinPressureServer": alarmMinPressureServer,
       "alarmMinEnablePressureServer": alarmMinEnablePressureServer,
       "alarmMaxPressureServer": alarmMaxPressureServer,
       "alarmMaxEnablePressureServer": alarmMaxEnablePressureServer,
       "warningMinPressureFacility": warningMinPressureFacility,
       "warningMinEnablePressureFacility": warningMinEnablePressureFacility,
       "warningMaxPressureFacility": warningMaxPressureFacility,
       "warningMaxEnablePressureFacility": warningMaxEnablePressureFacility,
       "alarmMinPressureFacility": alarmMinPressureFacility,
       "alarmMinEnablePressureFacility": alarmMinEnablePressureFacility,
       "alarmMaxPressureFacility": alarmMaxPressureFacility,
       "alarmMaxEnablePressureFacility": alarmMaxEnablePressureFacility,
       "alarmEnableLeak": alarmEnableLeak,
       "alarmEnableLevel": alarmEnableLevel,
       "conformance": conformance,
       "cduProdGroup": cduProdGroup,
       "cduSetupGroup": cduSetupGroup,
       "cduMeasGroup": cduMeasGroup,
       "cduMeasGroupRev2": cduMeasGroupRev2,
       "cduNetGroup": cduNetGroup,
       "cduCntlGroup": cduCntlGroup,
       "cduUnitGroup": cduUnitGroup,
       "cduNotifyGroup": cduNotifyGroup,
       "cduTrapGroup": cduTrapGroup,
       "cduCompliances": cduCompliances,
       "cduEventGroup": cduEventGroup,
       "cduTrapGroupRev2": cduTrapGroupRev2,
       "cduCompliancesRev2": cduCompliancesRev2,
       "eventDescriptors": eventDescriptors,
       "eventDescription": eventDescription,
       "eventValue": eventValue}
)
