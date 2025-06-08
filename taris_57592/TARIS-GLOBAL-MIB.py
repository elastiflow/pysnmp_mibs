# SNMP MIB module (TARIS-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/taris_57592/TARIS-GLOBAL-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:04:21 2025
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

tarisGlobalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 57592, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TarisFWVersions(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



class TarisPowerData(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



class TarisTemperatureData(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



# MIB Managed Objects in the order of their OIDs

_Taris_ObjectIdentity = ObjectIdentity
taris = _Taris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57592)
)
if mibBuilder.loadTexts:
    taris.setStatus("current")
_TarisReg_ObjectIdentity = ObjectIdentity
tarisReg = _TarisReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57592, 1)
)
if mibBuilder.loadTexts:
    tarisReg.setStatus("current")
_TarisModules_ObjectIdentity = ObjectIdentity
tarisModules = _TarisModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57592, 1, 1)
)
if mibBuilder.loadTexts:
    tarisModules.setStatus("current")
_TarisGeneric_ObjectIdentity = ObjectIdentity
tarisGeneric = _TarisGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57592, 2)
)
if mibBuilder.loadTexts:
    tarisGeneric.setStatus("current")
_TarisProducts_ObjectIdentity = ObjectIdentity
tarisProducts = _TarisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57592, 3)
)
if mibBuilder.loadTexts:
    tarisProducts.setStatus("current")
_TariscbipExtension_Type = Unsigned32
_TariscbipExtension_Object = MibScalar
tariscbipExtension = _TariscbipExtension_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 1),
    _TariscbipExtension_Type()
)
tariscbipExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipExtension.setStatus("current")
_TariscbipFirmwareVersion_Type = TarisFWVersions
_TariscbipFirmwareVersion_Object = MibScalar
tariscbipFirmwareVersion = _TariscbipFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 2),
    _TariscbipFirmwareVersion_Type()
)
tariscbipFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipFirmwareVersion.setStatus("current")
_TariscbipTemperature_Type = TarisTemperatureData
_TariscbipTemperature_Object = MibScalar
tariscbipTemperature = _TariscbipTemperature_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 3),
    _TariscbipTemperature_Type()
)
tariscbipTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tariscbipTemperature.setUnits("C")
_TariscbipBatery_Type = TarisPowerData
_TariscbipBatery_Object = MibScalar
tariscbipBatery = _TariscbipBatery_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 4),
    _TariscbipBatery_Type()
)
tariscbipBatery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipBatery.setStatus("current")
if mibBuilder.loadTexts:
    tariscbipBatery.setUnits("v")
_TariscbipPower_Type = TarisPowerData
_TariscbipPower_Object = MibScalar
tariscbipPower = _TariscbipPower_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 5),
    _TariscbipPower_Type()
)
tariscbipPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipPower.setStatus("current")
if mibBuilder.loadTexts:
    tariscbipPower.setUnits("v")


class _TariscbipEnclouserDoor_Type(Unsigned32):
    """Custom type tariscbipEnclouserDoor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TariscbipEnclouserDoor_Type.__name__ = "Unsigned32"
_TariscbipEnclouserDoor_Object = MibScalar
tariscbipEnclouserDoor = _TariscbipEnclouserDoor_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 6),
    _TariscbipEnclouserDoor_Type()
)
tariscbipEnclouserDoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipEnclouserDoor.setStatus("current")


class _TariscbipRuntime_Type(Unsigned32):
    """Custom type tariscbipRuntime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_TariscbipRuntime_Type.__name__ = "Unsigned32"
_TariscbipRuntime_Object = MibScalar
tariscbipRuntime = _TariscbipRuntime_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 7),
    _TariscbipRuntime_Type()
)
tariscbipRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipRuntime.setStatus("current")
_TariscbipACZ_Type = Integer32
_TariscbipACZ_Object = MibScalar
tariscbipACZ = _TariscbipACZ_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 8),
    _TariscbipACZ_Type()
)
tariscbipACZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipACZ.setStatus("current")
_TariscbipACY_Type = Integer32
_TariscbipACY_Object = MibScalar
tariscbipACY = _TariscbipACY_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 9),
    _TariscbipACY_Type()
)
tariscbipACY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipACY.setStatus("current")
_TariscbipMFH_Type = Integer32
_TariscbipMFH_Object = MibScalar
tariscbipMFH = _TariscbipMFH_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 10),
    _TariscbipMFH_Type()
)
tariscbipMFH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipMFH.setStatus("current")
_TariscbipMFL_Type = Integer32
_TariscbipMFL_Object = MibScalar
tariscbipMFL = _TariscbipMFL_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 11),
    _TariscbipMFL_Type()
)
tariscbipMFL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipMFL.setStatus("current")


class _TariscbipEcomodeStatus_Type(Unsigned32):
    """Custom type tariscbipEcomodeStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TariscbipEcomodeStatus_Type.__name__ = "Unsigned32"
_TariscbipEcomodeStatus_Object = MibScalar
tariscbipEcomodeStatus = _TariscbipEcomodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 12),
    _TariscbipEcomodeStatus_Type()
)
tariscbipEcomodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipEcomodeStatus.setStatus("current")


class _TariscbipEcomodeProgram_Type(Unsigned32):
    """Custom type tariscbipEcomodeProgram based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TariscbipEcomodeProgram_Type.__name__ = "Unsigned32"
_TariscbipEcomodeProgram_Object = MibScalar
tariscbipEcomodeProgram = _TariscbipEcomodeProgram_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 13),
    _TariscbipEcomodeProgram_Type()
)
tariscbipEcomodeProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tariscbipEcomodeProgram.setStatus("current")


class _TariscbipAlarmProgram_Type(Unsigned32):
    """Custom type tariscbipAlarmProgram based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TariscbipAlarmProgram_Type.__name__ = "Unsigned32"
_TariscbipAlarmProgram_Object = MibScalar
tariscbipAlarmProgram = _TariscbipAlarmProgram_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 14),
    _TariscbipAlarmProgram_Type()
)
tariscbipAlarmProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tariscbipAlarmProgram.setStatus("current")


class _TariscbipExternalLedProgram_Type(Unsigned32):
    """Custom type tariscbipExternalLedProgram based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TariscbipExternalLedProgram_Type.__name__ = "Unsigned32"
_TariscbipExternalLedProgram_Object = MibScalar
tariscbipExternalLedProgram = _TariscbipExternalLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 15),
    _TariscbipExternalLedProgram_Type()
)
tariscbipExternalLedProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tariscbipExternalLedProgram.setStatus("current")
_TariscbipCounterOne_Type = Integer32
_TariscbipCounterOne_Object = MibScalar
tariscbipCounterOne = _TariscbipCounterOne_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 16),
    _TariscbipCounterOne_Type()
)
tariscbipCounterOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterOne.setStatus("current")
_TariscbipCounterTwo_Type = Integer32
_TariscbipCounterTwo_Object = MibScalar
tariscbipCounterTwo = _TariscbipCounterTwo_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 17),
    _TariscbipCounterTwo_Type()
)
tariscbipCounterTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterTwo.setStatus("current")
_TariscbipCounterThree_Type = Integer32
_TariscbipCounterThree_Object = MibScalar
tariscbipCounterThree = _TariscbipCounterThree_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 18),
    _TariscbipCounterThree_Type()
)
tariscbipCounterThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterThree.setStatus("current")
_TariscbipCounterFour_Type = Integer32
_TariscbipCounterFour_Object = MibScalar
tariscbipCounterFour = _TariscbipCounterFour_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 19),
    _TariscbipCounterFour_Type()
)
tariscbipCounterFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterFour.setStatus("current")
_TariscbipCounterFive_Type = Integer32
_TariscbipCounterFive_Object = MibScalar
tariscbipCounterFive = _TariscbipCounterFive_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 20),
    _TariscbipCounterFive_Type()
)
tariscbipCounterFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterFive.setStatus("current")
_TariscbipCounterSix_Type = Integer32
_TariscbipCounterSix_Object = MibScalar
tariscbipCounterSix = _TariscbipCounterSix_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 21),
    _TariscbipCounterSix_Type()
)
tariscbipCounterSix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterSix.setStatus("current")
_TariscbipCounterSeven_Type = Integer32
_TariscbipCounterSeven_Object = MibScalar
tariscbipCounterSeven = _TariscbipCounterSeven_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 22),
    _TariscbipCounterSeven_Type()
)
tariscbipCounterSeven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterSeven.setStatus("current")
_TariscbipCounterEight_Type = Integer32
_TariscbipCounterEight_Object = MibScalar
tariscbipCounterEight = _TariscbipCounterEight_Object(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1, 23),
    _TariscbipCounterEight_Type()
)
tariscbipCounterEight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tariscbipCounterEight.setStatus("current")

# Managed Objects groups

tarisCallBoxIP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 57592, 3, 1)
)
tarisCallBoxIP.setObjects(
      *(("TARIS-GLOBAL-MIB", "tariscbipExtension"),
        ("TARIS-GLOBAL-MIB", "tariscbipFirmwareVersion"),
        ("TARIS-GLOBAL-MIB", "tariscbipTemperature"),
        ("TARIS-GLOBAL-MIB", "tariscbipBatery"),
        ("TARIS-GLOBAL-MIB", "tariscbipPower"),
        ("TARIS-GLOBAL-MIB", "tariscbipEnclouserDoor"),
        ("TARIS-GLOBAL-MIB", "tariscbipRuntime"),
        ("TARIS-GLOBAL-MIB", "tariscbipACZ"),
        ("TARIS-GLOBAL-MIB", "tariscbipACY"),
        ("TARIS-GLOBAL-MIB", "tariscbipMFH"),
        ("TARIS-GLOBAL-MIB", "tariscbipMFL"),
        ("TARIS-GLOBAL-MIB", "tariscbipEcomodeStatus"),
        ("TARIS-GLOBAL-MIB", "tariscbipEcomodeProgram"),
        ("TARIS-GLOBAL-MIB", "tariscbipAlarmProgram"),
        ("TARIS-GLOBAL-MIB", "tariscbipExternalLedProgram"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterOne"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterTwo"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterThree"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterFour"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterFive"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterSix"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterSeven"),
        ("TARIS-GLOBAL-MIB", "tariscbipCounterEight"))
)
if mibBuilder.loadTexts:
    tarisCallBoxIP.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TARIS-GLOBAL-MIB",
    **{"TarisFWVersions": TarisFWVersions,
       "TarisPowerData": TarisPowerData,
       "TarisTemperatureData": TarisTemperatureData,
       "taris": taris,
       "tarisReg": tarisReg,
       "tarisModules": tarisModules,
       "tarisGlobalModule": tarisGlobalModule,
       "tarisGeneric": tarisGeneric,
       "tarisProducts": tarisProducts,
       "tarisCallBoxIP": tarisCallBoxIP,
       "tariscbipExtension": tariscbipExtension,
       "tariscbipFirmwareVersion": tariscbipFirmwareVersion,
       "tariscbipTemperature": tariscbipTemperature,
       "tariscbipBatery": tariscbipBatery,
       "tariscbipPower": tariscbipPower,
       "tariscbipEnclouserDoor": tariscbipEnclouserDoor,
       "tariscbipRuntime": tariscbipRuntime,
       "tariscbipACZ": tariscbipACZ,
       "tariscbipACY": tariscbipACY,
       "tariscbipMFH": tariscbipMFH,
       "tariscbipMFL": tariscbipMFL,
       "tariscbipEcomodeStatus": tariscbipEcomodeStatus,
       "tariscbipEcomodeProgram": tariscbipEcomodeProgram,
       "tariscbipAlarmProgram": tariscbipAlarmProgram,
       "tariscbipExternalLedProgram": tariscbipExternalLedProgram,
       "tariscbipCounterOne": tariscbipCounterOne,
       "tariscbipCounterTwo": tariscbipCounterTwo,
       "tariscbipCounterThree": tariscbipCounterThree,
       "tariscbipCounterFour": tariscbipCounterFour,
       "tariscbipCounterFive": tariscbipCounterFive,
       "tariscbipCounterSix": tariscbipCounterSix,
       "tariscbipCounterSeven": tariscbipCounterSeven,
       "tariscbipCounterEight": tariscbipCounterEight}
)
