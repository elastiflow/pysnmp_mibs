# SNMP MIB module (SCTE-HMS-GEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-GEN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:05 2025
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

(genIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "genIdent")

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



class _GenNumberOfGenerators_Type(Integer32):
    """Custom type genNumberOfGenerators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GenNumberOfGenerators_Type.__name__ = "Integer32"
_GenNumberOfGenerators_Object = MibScalar
genNumberOfGenerators = _GenNumberOfGenerators_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 1),
    _GenNumberOfGenerators_Type()
)
genNumberOfGenerators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genNumberOfGenerators.setStatus("mandatory")
_GenDeviceTable_Object = MibTable
genDeviceTable = _GenDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2)
)
if mibBuilder.loadTexts:
    genDeviceTable.setStatus("mandatory")
_GenDeviceEntry_Object = MibTableRow
genDeviceEntry = _GenDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1)
)
genDeviceEntry.setIndexNames(
    (0, "SCTE-HMS-GEN-MIB", "genDeviceAddress"),
)
if mibBuilder.loadTexts:
    genDeviceEntry.setStatus("mandatory")


class _GenDeviceAddress_Type(Integer32):
    """Custom type genDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GenDeviceAddress_Type.__name__ = "Integer32"
_GenDeviceAddress_Object = MibTableColumn
genDeviceAddress = _GenDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 1),
    _GenDeviceAddress_Type()
)
genDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDeviceAddress.setStatus("mandatory")


class _GenProtocolVersion_Type(Integer32):
    """Custom type genProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenProtocolVersion_Type.__name__ = "Integer32"
_GenProtocolVersion_Object = MibTableColumn
genProtocolVersion = _GenProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 2),
    _GenProtocolVersion_Type()
)
genProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolVersion.setStatus("mandatory")


class _GenSoftwareVersion_Type(OctetString):
    """Custom type genSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_GenSoftwareVersion_Type.__name__ = "OctetString"
_GenSoftwareVersion_Object = MibTableColumn
genSoftwareVersion = _GenSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 3),
    _GenSoftwareVersion_Type()
)
genSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSoftwareVersion.setStatus("mandatory")


class _GenDeviceId_Type(OctetString):
    """Custom type genDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixedLength = 32


_GenDeviceId_Type.__name__ = "OctetString"
_GenDeviceId_Object = MibTableColumn
genDeviceId = _GenDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 4),
    _GenDeviceId_Type()
)
genDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDeviceId.setStatus("mandatory")


class _GenGasHazardOption_Type(Integer32):
    """Custom type genGasHazardOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenGasHazardOption_Type.__name__ = "Integer32"
_GenGasHazardOption_Object = MibTableColumn
genGasHazardOption = _GenGasHazardOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 5),
    _GenGasHazardOption_Type()
)
genGasHazardOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGasHazardOption.setStatus("mandatory")


class _GenWaterIntrusionOption_Type(Integer32):
    """Custom type genWaterIntrusionOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenWaterIntrusionOption_Type.__name__ = "Integer32"
_GenWaterIntrusionOption_Object = MibTableColumn
genWaterIntrusionOption = _GenWaterIntrusionOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 6),
    _GenWaterIntrusionOption_Type()
)
genWaterIntrusionOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genWaterIntrusionOption.setStatus("mandatory")


class _GenPadShearOption_Type(Integer32):
    """Custom type genPadShearOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenPadShearOption_Type.__name__ = "Integer32"
_GenPadShearOption_Object = MibTableColumn
genPadShearOption = _GenPadShearOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 7),
    _GenPadShearOption_Type()
)
genPadShearOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPadShearOption.setStatus("mandatory")


class _GenDoorOption_Type(Integer32):
    """Custom type genDoorOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenDoorOption_Type.__name__ = "Integer32"
_GenDoorOption_Object = MibTableColumn
genDoorOption = _GenDoorOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 8),
    _GenDoorOption_Type()
)
genDoorOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDoorOption.setStatus("mandatory")


class _GenChargerOption_Type(Integer32):
    """Custom type genChargerOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenChargerOption_Type.__name__ = "Integer32"
_GenChargerOption_Object = MibTableColumn
genChargerOption = _GenChargerOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 9),
    _GenChargerOption_Type()
)
genChargerOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genChargerOption.setStatus("mandatory")


class _GenFuelOption_Type(Integer32):
    """Custom type genFuelOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenFuelOption_Type.__name__ = "Integer32"
_GenFuelOption_Object = MibTableColumn
genFuelOption = _GenFuelOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 10),
    _GenFuelOption_Type()
)
genFuelOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genFuelOption.setStatus("mandatory")


class _GenVBatIgnitionOption_Type(Integer32):
    """Custom type genVBatIgnitionOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenVBatIgnitionOption_Type.__name__ = "Integer32"
_GenVBatIgnitionOption_Object = MibTableColumn
genVBatIgnitionOption = _GenVBatIgnitionOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 11),
    _GenVBatIgnitionOption_Type()
)
genVBatIgnitionOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVBatIgnitionOption.setStatus("mandatory")


class _GenTempOption_Type(Integer32):
    """Custom type genTempOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenTempOption_Type.__name__ = "Integer32"
_GenTempOption_Object = MibTableColumn
genTempOption = _GenTempOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 12),
    _GenTempOption_Type()
)
genTempOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genTempOption.setStatus("mandatory")


class _GenGeneratorStatus_Type(Integer32):
    """Custom type genGeneratorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("runningTest", 2),
          ("running", 3),
          ("fail", 4))
    )


_GenGeneratorStatus_Type.__name__ = "Integer32"
_GenGeneratorStatus_Object = MibTableColumn
genGeneratorStatus = _GenGeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 13),
    _GenGeneratorStatus_Type()
)
genGeneratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGeneratorStatus.setStatus("mandatory")


class _GenGasHazard_Type(Integer32):
    """Custom type genGasHazard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenGasHazard_Type.__name__ = "Integer32"
_GenGasHazard_Object = MibTableColumn
genGasHazard = _GenGasHazard_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 14),
    _GenGasHazard_Type()
)
genGasHazard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGasHazard.setStatus("mandatory")


class _GenWaterIntrusion_Type(Integer32):
    """Custom type genWaterIntrusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenWaterIntrusion_Type.__name__ = "Integer32"
_GenWaterIntrusion_Object = MibTableColumn
genWaterIntrusion = _GenWaterIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 15),
    _GenWaterIntrusion_Type()
)
genWaterIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genWaterIntrusion.setStatus("mandatory")


class _GenPadShear_Type(Integer32):
    """Custom type genPadShear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenPadShear_Type.__name__ = "Integer32"
_GenPadShear_Object = MibTableColumn
genPadShear = _GenPadShear_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 16),
    _GenPadShear_Type()
)
genPadShear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPadShear.setStatus("mandatory")


class _GenEnclosureDoor_Type(Integer32):
    """Custom type genEnclosureDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenEnclosureDoor_Type.__name__ = "Integer32"
_GenEnclosureDoor_Object = MibTableColumn
genEnclosureDoor = _GenEnclosureDoor_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 17),
    _GenEnclosureDoor_Type()
)
genEnclosureDoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEnclosureDoor.setStatus("mandatory")


class _GenCharger_Type(Integer32):
    """Custom type genCharger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenCharger_Type.__name__ = "Integer32"
_GenCharger_Object = MibTableColumn
genCharger = _GenCharger_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 18),
    _GenCharger_Type()
)
genCharger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCharger.setStatus("mandatory")


class _GenFuel_Type(Integer32):
    """Custom type genFuel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenFuel_Type.__name__ = "Integer32"
_GenFuel_Object = MibTableColumn
genFuel = _GenFuel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 19),
    _GenFuel_Type()
)
genFuel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genFuel.setStatus("mandatory")


class _GenVBatIgnition_Type(Integer32):
    """Custom type genVBatIgnition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GenVBatIgnition_Type.__name__ = "Integer32"
_GenVBatIgnition_Object = MibTableColumn
genVBatIgnition = _GenVBatIgnition_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 20),
    _GenVBatIgnition_Type()
)
genVBatIgnition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVBatIgnition.setStatus("mandatory")


class _GenEnclosureTemperature_Type(Integer32):
    """Custom type genEnclosureTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_GenEnclosureTemperature_Type.__name__ = "Integer32"
_GenEnclosureTemperature_Object = MibTableColumn
genEnclosureTemperature = _GenEnclosureTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 21),
    _GenEnclosureTemperature_Type()
)
genEnclosureTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEnclosureTemperature.setStatus("mandatory")


class _GenEquipmentControl_Type(Integer32):
    """Custom type genEquipmentControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopGenerator", 1),
          ("startGenerator", 2),
          ("resetLatchedAlarms", 3))
    )


_GenEquipmentControl_Type.__name__ = "Integer32"
_GenEquipmentControl_Object = MibTableColumn
genEquipmentControl = _GenEquipmentControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 22),
    _GenEquipmentControl_Type()
)
genEquipmentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipmentControl.setStatus("optional")


class _GenOilOption_Type(Integer32):
    """Custom type genOilOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenOilOption_Type.__name__ = "Integer32"
_GenOilOption_Object = MibTableColumn
genOilOption = _GenOilOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 23),
    _GenOilOption_Type()
)
genOilOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOilOption.setStatus("mandatory")


class _GenMinorAlarmSupport_Type(Integer32):
    """Custom type genMinorAlarmSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenMinorAlarmSupport_Type.__name__ = "Integer32"
_GenMinorAlarmSupport_Object = MibTableColumn
genMinorAlarmSupport = _GenMinorAlarmSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 24),
    _GenMinorAlarmSupport_Type()
)
genMinorAlarmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMinorAlarmSupport.setStatus("mandatory")


class _GenMajorAlarmSupport_Type(Integer32):
    """Custom type genMajorAlarmSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_GenMajorAlarmSupport_Type.__name__ = "Integer32"
_GenMajorAlarmSupport_Object = MibTableColumn
genMajorAlarmSupport = _GenMajorAlarmSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 25),
    _GenMajorAlarmSupport_Type()
)
genMajorAlarmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMajorAlarmSupport.setStatus("mandatory")


class _GenOil_Type(Integer32):
    """Custom type genOil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenOil_Type.__name__ = "Integer32"
_GenOil_Object = MibTableColumn
genOil = _GenOil_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 26),
    _GenOil_Type()
)
genOil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOil.setStatus("optional")


class _GenMinorAlarm_Type(Integer32):
    """Custom type genMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenMinorAlarm_Type.__name__ = "Integer32"
_GenMinorAlarm_Object = MibTableColumn
genMinorAlarm = _GenMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 27),
    _GenMinorAlarm_Type()
)
genMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMinorAlarm.setStatus("optional")


class _GenMajorAlarm_Type(Integer32):
    """Custom type genMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("alarm", 2))
    )


_GenMajorAlarm_Type.__name__ = "Integer32"
_GenMajorAlarm_Object = MibTableColumn
genMajorAlarm = _GenMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 28),
    _GenMajorAlarm_Type()
)
genMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMajorAlarm.setStatus("optional")
_GenVendorOID_Type = ObjectIdentifier
_GenVendorOID_Object = MibTableColumn
genVendorOID = _GenVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6, 2, 1, 29),
    _GenVendorOID_Type()
)
genVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVendorOID.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-GEN-MIB",
    **{"genNumberOfGenerators": genNumberOfGenerators,
       "genDeviceTable": genDeviceTable,
       "genDeviceEntry": genDeviceEntry,
       "genDeviceAddress": genDeviceAddress,
       "genProtocolVersion": genProtocolVersion,
       "genSoftwareVersion": genSoftwareVersion,
       "genDeviceId": genDeviceId,
       "genGasHazardOption": genGasHazardOption,
       "genWaterIntrusionOption": genWaterIntrusionOption,
       "genPadShearOption": genPadShearOption,
       "genDoorOption": genDoorOption,
       "genChargerOption": genChargerOption,
       "genFuelOption": genFuelOption,
       "genVBatIgnitionOption": genVBatIgnitionOption,
       "genTempOption": genTempOption,
       "genGeneratorStatus": genGeneratorStatus,
       "genGasHazard": genGasHazard,
       "genWaterIntrusion": genWaterIntrusion,
       "genPadShear": genPadShear,
       "genEnclosureDoor": genEnclosureDoor,
       "genCharger": genCharger,
       "genFuel": genFuel,
       "genVBatIgnition": genVBatIgnition,
       "genEnclosureTemperature": genEnclosureTemperature,
       "genEquipmentControl": genEquipmentControl,
       "genOilOption": genOilOption,
       "genMinorAlarmSupport": genMinorAlarmSupport,
       "genMajorAlarmSupport": genMajorAlarmSupport,
       "genOil": genOil,
       "genMinorAlarm": genMinorAlarm,
       "genMajorAlarm": genMajorAlarm,
       "genVendorOID": genVendorOID}
)
