# SNMP MIB module (DeltaTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_6785/DeltaTP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:50:40 2025
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

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785)
)
_Tp_ObjectIdentity = ObjectIdentity
tp = _Tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1)
)
_Ats_ObjectIdentity = ObjectIdentity
ats = _Ats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12)
)
_AtsInfo_ObjectIdentity = ObjectIdentity
atsInfo = _AtsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1)
)


class _AtsName_Type(DisplayString):
    """Custom type atsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtsName_Type.__name__ = "DisplayString"
_AtsName_Object = MibScalar
atsName = _AtsName_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 1),
    _AtsName_Type()
)
atsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsName.setStatus("mandatory")


class _AtsFactoryDate_Type(DisplayString):
    """Custom type atsFactoryDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtsFactoryDate_Type.__name__ = "DisplayString"
_AtsFactoryDate_Object = MibScalar
atsFactoryDate = _AtsFactoryDate_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 2),
    _AtsFactoryDate_Type()
)
atsFactoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsFactoryDate.setStatus("mandatory")


class _AtsModelName_Type(DisplayString):
    """Custom type atsModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AtsModelName_Type.__name__ = "DisplayString"
_AtsModelName_Object = MibScalar
atsModelName = _AtsModelName_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 3),
    _AtsModelName_Type()
)
atsModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsModelName.setStatus("mandatory")


class _AtsSerialNumber_Type(DisplayString):
    """Custom type atsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AtsSerialNumber_Type.__name__ = "DisplayString"
_AtsSerialNumber_Object = MibScalar
atsSerialNumber = _AtsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 4),
    _AtsSerialNumber_Type()
)
atsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsSerialNumber.setStatus("mandatory")


class _AtsHardwareRevision_Type(DisplayString):
    """Custom type atsHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AtsHardwareRevision_Type.__name__ = "DisplayString"
_AtsHardwareRevision_Object = MibScalar
atsHardwareRevision = _AtsHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 5),
    _AtsHardwareRevision_Type()
)
atsHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsHardwareRevision.setStatus("mandatory")


class _LcdFirmwareRevision_Type(DisplayString):
    """Custom type lcdFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LcdFirmwareRevision_Type.__name__ = "DisplayString"
_LcdFirmwareRevision_Object = MibScalar
lcdFirmwareRevision = _LcdFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 6),
    _LcdFirmwareRevision_Type()
)
lcdFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcdFirmwareRevision.setStatus("mandatory")


class _WebFirmwareRevision_Type(DisplayString):
    """Custom type webFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WebFirmwareRevision_Type.__name__ = "DisplayString"
_WebFirmwareRevision_Object = MibScalar
webFirmwareRevision = _WebFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 7),
    _WebFirmwareRevision_Type()
)
webFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webFirmwareRevision.setStatus("mandatory")


class _CtlFirmwareRevision_Type(DisplayString):
    """Custom type ctlFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CtlFirmwareRevision_Type.__name__ = "DisplayString"
_CtlFirmwareRevision_Object = MibScalar
ctlFirmwareRevision = _CtlFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 8),
    _CtlFirmwareRevision_Type()
)
ctlFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlFirmwareRevision.setStatus("mandatory")


class _SystemDate_Type(DisplayString):
    """Custom type systemDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SystemDate_Type.__name__ = "DisplayString"
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 9),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("mandatory")


class _SystemTime_Type(DisplayString):
    """Custom type systemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SystemTime_Type.__name__ = "DisplayString"
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 1, 10),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("mandatory")
_AtsMonitor_ObjectIdentity = ObjectIdentity
atsMonitor = _AtsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2)
)


class _AtsStatus_Type(Integer32):
    """Custom type atsStatus based on Integer32"""
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
        *(("normal", 0),
          ("minor", 1),
          ("major", 2),
          ("critical", 3))
    )


_AtsStatus_Type.__name__ = "Integer32"
_AtsStatus_Object = MibScalar
atsStatus = _AtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 1),
    _AtsStatus_Type()
)
atsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatus.setStatus("mandatory")
_AtsInputAFreq_Type = Integer32
_AtsInputAFreq_Object = MibScalar
atsInputAFreq = _AtsInputAFreq_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 2),
    _AtsInputAFreq_Type()
)
atsInputAFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAFreq.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputAFreq.setUnits("0.1Hz")
_AtsInputBFreq_Type = Integer32
_AtsInputBFreq_Object = MibScalar
atsInputBFreq = _AtsInputBFreq_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 3),
    _AtsInputBFreq_Type()
)
atsInputBFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBFreq.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputBFreq.setUnits("0.1HZ")
_AtsInputAVoltageL1_L2_Type = Integer32
_AtsInputAVoltageL1_L2_Object = MibScalar
atsInputAVoltageL1_L2 = _AtsInputAVoltageL1_L2_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 4),
    _AtsInputAVoltageL1_L2_Type()
)
atsInputAVoltageL1_L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAVoltageL1_L2.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputAVoltageL1_L2.setUnits("0.1 Vrms")
_AtsInputAVoltageL2_L3_Type = Integer32
_AtsInputAVoltageL2_L3_Object = MibScalar
atsInputAVoltageL2_L3 = _AtsInputAVoltageL2_L3_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 5),
    _AtsInputAVoltageL2_L3_Type()
)
atsInputAVoltageL2_L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAVoltageL2_L3.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputAVoltageL2_L3.setUnits("0.1 Vrms")
_AtsInputAVoltageL3_L1_Type = Integer32
_AtsInputAVoltageL3_L1_Object = MibScalar
atsInputAVoltageL3_L1 = _AtsInputAVoltageL3_L1_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 6),
    _AtsInputAVoltageL3_L1_Type()
)
atsInputAVoltageL3_L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAVoltageL3_L1.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputAVoltageL3_L1.setUnits("0.1 Vrms")
_AtsInputBVoltageL1_L2_Type = Integer32
_AtsInputBVoltageL1_L2_Object = MibScalar
atsInputBVoltageL1_L2 = _AtsInputBVoltageL1_L2_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 7),
    _AtsInputBVoltageL1_L2_Type()
)
atsInputBVoltageL1_L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBVoltageL1_L2.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputBVoltageL1_L2.setUnits("0.1 Vrms")
_AtsInputBVoltageL2_L3_Type = Integer32
_AtsInputBVoltageL2_L3_Object = MibScalar
atsInputBVoltageL2_L3 = _AtsInputBVoltageL2_L3_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 8),
    _AtsInputBVoltageL2_L3_Type()
)
atsInputBVoltageL2_L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBVoltageL2_L3.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputBVoltageL2_L3.setUnits("0.1 Vrms")
_AtsInputBVoltageL3_L1_Type = Integer32
_AtsInputBVoltageL3_L1_Object = MibScalar
atsInputBVoltageL3_L1 = _AtsInputBVoltageL3_L1_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 9),
    _AtsInputBVoltageL3_L1_Type()
)
atsInputBVoltageL3_L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBVoltageL3_L1.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputBVoltageL3_L1.setUnits("0.1 Vrms")
_AtsOutputVoltageL1_L2_Type = Integer32
_AtsOutputVoltageL1_L2_Object = MibScalar
atsOutputVoltageL1_L2 = _AtsOutputVoltageL1_L2_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 10),
    _AtsOutputVoltageL1_L2_Type()
)
atsOutputVoltageL1_L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputVoltageL1_L2.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputVoltageL1_L2.setUnits("0.1 Vrms")
_AtsOutputVoltageL2_L3_Type = Integer32
_AtsOutputVoltageL2_L3_Object = MibScalar
atsOutputVoltageL2_L3 = _AtsOutputVoltageL2_L3_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 11),
    _AtsOutputVoltageL2_L3_Type()
)
atsOutputVoltageL2_L3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputVoltageL2_L3.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputVoltageL2_L3.setUnits("0.1 Vrms")
_AtsOutputVoltageL3_L1_Type = Integer32
_AtsOutputVoltageL3_L1_Object = MibScalar
atsOutputVoltageL3_L1 = _AtsOutputVoltageL3_L1_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 12),
    _AtsOutputVoltageL3_L1_Type()
)
atsOutputVoltageL3_L1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputVoltageL3_L1.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputVoltageL3_L1.setUnits("0.1 Vrms")
_AtsOutputCurrentL1_Type = Integer32
_AtsOutputCurrentL1_Object = MibScalar
atsOutputCurrentL1 = _AtsOutputCurrentL1_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 13),
    _AtsOutputCurrentL1_Type()
)
atsOutputCurrentL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrentL1.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrentL1.setUnits("0.01 Arms")
_AtsOutputCurrentL2_Type = Integer32
_AtsOutputCurrentL2_Object = MibScalar
atsOutputCurrentL2 = _AtsOutputCurrentL2_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 14),
    _AtsOutputCurrentL2_Type()
)
atsOutputCurrentL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrentL2.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrentL2.setUnits("0.01 Arms")
_AtsOutputCurrentL3_Type = Integer32
_AtsOutputCurrentL3_Object = MibScalar
atsOutputCurrentL3 = _AtsOutputCurrentL3_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 15),
    _AtsOutputCurrentL3_Type()
)
atsOutputCurrentL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrentL3.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrentL3.setUnits("0.01 Arms")
_AtsOutputTotalCurrent_Type = Integer32
_AtsOutputTotalCurrent_Object = MibScalar
atsOutputTotalCurrent = _AtsOutputTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 16),
    _AtsOutputTotalCurrent_Type()
)
atsOutputTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputTotalCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputTotalCurrent.setUnits("0.01 Arms")
_AtsOutputPowerFactor_Type = Integer32
_AtsOutputPowerFactor_Object = MibScalar
atsOutputPowerFactor = _AtsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 17),
    _AtsOutputPowerFactor_Type()
)
atsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputPowerFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputPowerFactor.setUnits("0.001")
_AtsAmbientTemperature_Type = Integer32
_AtsAmbientTemperature_Object = MibScalar
atsAmbientTemperature = _AtsAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 18),
    _AtsAmbientTemperature_Type()
)
atsAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsAmbientTemperature.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsAmbientTemperature.setUnits("C")
_AtsOutputPowerRealTotal_Type = Integer32
_AtsOutputPowerRealTotal_Object = MibScalar
atsOutputPowerRealTotal = _AtsOutputPowerRealTotal_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 21),
    _AtsOutputPowerRealTotal_Type()
)
atsOutputPowerRealTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputPowerRealTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputPowerRealTotal.setUnits("Watts")
_AtsOutputPowerApparentTotal_Type = Integer32
_AtsOutputPowerApparentTotal_Object = MibScalar
atsOutputPowerApparentTotal = _AtsOutputPowerApparentTotal_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 25),
    _AtsOutputPowerApparentTotal_Type()
)
atsOutputPowerApparentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputPowerApparentTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputPowerApparentTotal.setUnits("VA")
_AtsInputAOverVoltageThreshold_Type = Integer32
_AtsInputAOverVoltageThreshold_Object = MibScalar
atsInputAOverVoltageThreshold = _AtsInputAOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 26),
    _AtsInputAOverVoltageThreshold_Type()
)
atsInputAOverVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAOverVoltageThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputAOverVoltageThreshold.setUnits("0.1 Vrms")
_AtsInputALowVoltageThreshold_Type = Integer32
_AtsInputALowVoltageThreshold_Object = MibScalar
atsInputALowVoltageThreshold = _AtsInputALowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 27),
    _AtsInputALowVoltageThreshold_Type()
)
atsInputALowVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputALowVoltageThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputALowVoltageThreshold.setUnits("0.1 Vrms")
_AtsInputBOverVoltageThreshold_Type = Integer32
_AtsInputBOverVoltageThreshold_Object = MibScalar
atsInputBOverVoltageThreshold = _AtsInputBOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 28),
    _AtsInputBOverVoltageThreshold_Type()
)
atsInputBOverVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBOverVoltageThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputBOverVoltageThreshold.setUnits("0.1 Vrms")
_AtsInputBLowVoltageThreshold_Type = Integer32
_AtsInputBLowVoltageThreshold_Object = MibScalar
atsInputBLowVoltageThreshold = _AtsInputBLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 29),
    _AtsInputBLowVoltageThreshold_Type()
)
atsInputBLowVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBLowVoltageThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputBLowVoltageThreshold.setUnits("0.1 Vrms")
_AtsOutputOverVoltageThreshold_Type = Integer32
_AtsOutputOverVoltageThreshold_Object = MibScalar
atsOutputOverVoltageThreshold = _AtsOutputOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 30),
    _AtsOutputOverVoltageThreshold_Type()
)
atsOutputOverVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputOverVoltageThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputOverVoltageThreshold.setUnits("0.1 Vrms")
_AtsOutputLowVoltageThreshold_Type = Integer32
_AtsOutputLowVoltageThreshold_Object = MibScalar
atsOutputLowVoltageThreshold = _AtsOutputLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 31),
    _AtsOutputLowVoltageThreshold_Type()
)
atsOutputLowVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputLowVoltageThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputLowVoltageThreshold.setUnits("0.1 Vrms")
_AtsOutputOverCurrentThreshold_Type = Integer32
_AtsOutputOverCurrentThreshold_Object = MibScalar
atsOutputOverCurrentThreshold = _AtsOutputOverCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 32),
    _AtsOutputOverCurrentThreshold_Type()
)
atsOutputOverCurrentThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputOverCurrentThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputOverCurrentThreshold.setUnits("0.1 Arms")
_AtsOutputCurrentAccuracyLess20PercentLoad_Type = Integer32
_AtsOutputCurrentAccuracyLess20PercentLoad_Object = MibScalar
atsOutputCurrentAccuracyLess20PercentLoad = _AtsOutputCurrentAccuracyLess20PercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 33),
    _AtsOutputCurrentAccuracyLess20PercentLoad_Type()
)
atsOutputCurrentAccuracyLess20PercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrentAccuracyLess20PercentLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrentAccuracyLess20PercentLoad.setUnits("%")
_AtsOutputCurrentAccuracyMore20PercentLoad_Type = Integer32
_AtsOutputCurrentAccuracyMore20PercentLoad_Object = MibScalar
atsOutputCurrentAccuracyMore20PercentLoad = _AtsOutputCurrentAccuracyMore20PercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 34),
    _AtsOutputCurrentAccuracyMore20PercentLoad_Type()
)
atsOutputCurrentAccuracyMore20PercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrentAccuracyMore20PercentLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrentAccuracyMore20PercentLoad.setUnits("%")
_AtsOutputCurrentResolution_Type = Integer32
_AtsOutputCurrentResolution_Object = MibScalar
atsOutputCurrentResolution = _AtsOutputCurrentResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 35),
    _AtsOutputCurrentResolution_Type()
)
atsOutputCurrentResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrentResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrentResolution.setUnits("0.01")
_AtsOutputVoltageAccuracy_Type = Integer32
_AtsOutputVoltageAccuracy_Object = MibScalar
atsOutputVoltageAccuracy = _AtsOutputVoltageAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 36),
    _AtsOutputVoltageAccuracy_Type()
)
atsOutputVoltageAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputVoltageAccuracy.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputVoltageAccuracy.setUnits("%")
_AtsOutputVoltageResolution_Type = Integer32
_AtsOutputVoltageResolution_Object = MibScalar
atsOutputVoltageResolution = _AtsOutputVoltageResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 37),
    _AtsOutputVoltageResolution_Type()
)
atsOutputVoltageResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputVoltageResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputVoltageResolution.setUnits("0.1")
_AtsOutputFreqAccuracy_Type = Integer32
_AtsOutputFreqAccuracy_Object = MibScalar
atsOutputFreqAccuracy = _AtsOutputFreqAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 38),
    _AtsOutputFreqAccuracy_Type()
)
atsOutputFreqAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputFreqAccuracy.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputFreqAccuracy.setUnits("Hz")
_AtsOutputFreqResolution_Type = Integer32
_AtsOutputFreqResolution_Object = MibScalar
atsOutputFreqResolution = _AtsOutputFreqResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 39),
    _AtsOutputFreqResolution_Type()
)
atsOutputFreqResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputFreqResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputFreqResolution.setUnits("0.1")
_AtsOutputApparentPowerAccuracyLess20PercentLoad_Type = Integer32
_AtsOutputApparentPowerAccuracyLess20PercentLoad_Object = MibScalar
atsOutputApparentPowerAccuracyLess20PercentLoad = _AtsOutputApparentPowerAccuracyLess20PercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 40),
    _AtsOutputApparentPowerAccuracyLess20PercentLoad_Type()
)
atsOutputApparentPowerAccuracyLess20PercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputApparentPowerAccuracyLess20PercentLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputApparentPowerAccuracyLess20PercentLoad.setUnits("%")
_AtsOutputApparentPowerAccuracyMore20PercentLoad_Type = Integer32
_AtsOutputApparentPowerAccuracyMore20PercentLoad_Object = MibScalar
atsOutputApparentPowerAccuracyMore20PercentLoad = _AtsOutputApparentPowerAccuracyMore20PercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 41),
    _AtsOutputApparentPowerAccuracyMore20PercentLoad_Type()
)
atsOutputApparentPowerAccuracyMore20PercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputApparentPowerAccuracyMore20PercentLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputApparentPowerAccuracyMore20PercentLoad.setUnits("%")
_AtsOutputApparentPowerResolution_Type = Integer32
_AtsOutputApparentPowerResolution_Object = MibScalar
atsOutputApparentPowerResolution = _AtsOutputApparentPowerResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 42),
    _AtsOutputApparentPowerResolution_Type()
)
atsOutputApparentPowerResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputApparentPowerResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputApparentPowerResolution.setUnits("0.01")
_AtsOutputRealPowerAccuracyLess20PercentLoad_Type = Integer32
_AtsOutputRealPowerAccuracyLess20PercentLoad_Object = MibScalar
atsOutputRealPowerAccuracyLess20PercentLoad = _AtsOutputRealPowerAccuracyLess20PercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 43),
    _AtsOutputRealPowerAccuracyLess20PercentLoad_Type()
)
atsOutputRealPowerAccuracyLess20PercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputRealPowerAccuracyLess20PercentLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputRealPowerAccuracyLess20PercentLoad.setUnits("%")
_AtsOutputRealPowerAccuracyMore20PercentLoad_Type = Integer32
_AtsOutputRealPowerAccuracyMore20PercentLoad_Object = MibScalar
atsOutputRealPowerAccuracyMore20PercentLoad = _AtsOutputRealPowerAccuracyMore20PercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 45),
    _AtsOutputRealPowerAccuracyMore20PercentLoad_Type()
)
atsOutputRealPowerAccuracyMore20PercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputRealPowerAccuracyMore20PercentLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputRealPowerAccuracyMore20PercentLoad.setUnits("%")
_AtsOutputRealPowerResolution_Type = Integer32
_AtsOutputRealPowerResolution_Object = MibScalar
atsOutputRealPowerResolution = _AtsOutputRealPowerResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 46),
    _AtsOutputRealPowerResolution_Type()
)
atsOutputRealPowerResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputRealPowerResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputRealPowerResolution.setUnits("0.01")
_AtsOutputPowerFactorAccuracy_Type = Integer32
_AtsOutputPowerFactorAccuracy_Object = MibScalar
atsOutputPowerFactorAccuracy = _AtsOutputPowerFactorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 47),
    _AtsOutputPowerFactorAccuracy_Type()
)
atsOutputPowerFactorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputPowerFactorAccuracy.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputPowerFactorAccuracy.setUnits("%")
_AtsOutputPowerFactorResolution_Type = Integer32
_AtsOutputPowerFactorResolution_Object = MibScalar
atsOutputPowerFactorResolution = _AtsOutputPowerFactorResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 48),
    _AtsOutputPowerFactorResolution_Type()
)
atsOutputPowerFactorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputPowerFactorResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputPowerFactorResolution.setUnits("0.001")
_AtsTemperatureAccuracy_Type = Integer32
_AtsTemperatureAccuracy_Object = MibScalar
atsTemperatureAccuracy = _AtsTemperatureAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 49),
    _AtsTemperatureAccuracy_Type()
)
atsTemperatureAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsTemperatureAccuracy.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsTemperatureAccuracy.setUnits("%")
_AtsTemperatureResolution_Type = Integer32
_AtsTemperatureResolution_Object = MibScalar
atsTemperatureResolution = _AtsTemperatureResolution_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 2, 50),
    _AtsTemperatureResolution_Type()
)
atsTemperatureResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsTemperatureResolution.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsTemperatureResolution.setUnits("C")
_AtsAlarm_ObjectIdentity = ObjectIdentity
atsAlarm = _AtsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3)
)


class _AtsInputAOverVoltage_Type(Integer32):
    """Custom type atsInputAOverVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputAOverVoltage_Type.__name__ = "Integer32"
_AtsInputAOverVoltage_Object = MibScalar
atsInputAOverVoltage = _AtsInputAOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 1),
    _AtsInputAOverVoltage_Type()
)
atsInputAOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAOverVoltage.setStatus("mandatory")


class _AtsInputALowVoltage_Type(Integer32):
    """Custom type atsInputALowVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputALowVoltage_Type.__name__ = "Integer32"
_AtsInputALowVoltage_Object = MibScalar
atsInputALowVoltage = _AtsInputALowVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 2),
    _AtsInputALowVoltage_Type()
)
atsInputALowVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputALowVoltage.setStatus("mandatory")


class _AtsInputAFail_Type(Integer32):
    """Custom type atsInputAFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputAFail_Type.__name__ = "Integer32"
_AtsInputAFail_Object = MibScalar
atsInputAFail = _AtsInputAFail_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 3),
    _AtsInputAFail_Type()
)
atsInputAFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAFail.setStatus("mandatory")


class _AtsInputBOverVoltage_Type(Integer32):
    """Custom type atsInputBOverVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputBOverVoltage_Type.__name__ = "Integer32"
_AtsInputBOverVoltage_Object = MibScalar
atsInputBOverVoltage = _AtsInputBOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 4),
    _AtsInputBOverVoltage_Type()
)
atsInputBOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBOverVoltage.setStatus("mandatory")


class _AtsInputBLowVoltage_Type(Integer32):
    """Custom type atsInputBLowVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputBLowVoltage_Type.__name__ = "Integer32"
_AtsInputBLowVoltage_Object = MibScalar
atsInputBLowVoltage = _AtsInputBLowVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 5),
    _AtsInputBLowVoltage_Type()
)
atsInputBLowVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBLowVoltage.setStatus("mandatory")


class _AtsInputBFail_Type(Integer32):
    """Custom type atsInputBFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputBFail_Type.__name__ = "Integer32"
_AtsInputBFail_Object = MibScalar
atsInputBFail = _AtsInputBFail_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 6),
    _AtsInputBFail_Type()
)
atsInputBFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBFail.setStatus("mandatory")


class _AtsOutputOverVoltage_Type(Integer32):
    """Custom type atsOutputOverVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsOutputOverVoltage_Type.__name__ = "Integer32"
_AtsOutputOverVoltage_Object = MibScalar
atsOutputOverVoltage = _AtsOutputOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 7),
    _AtsOutputOverVoltage_Type()
)
atsOutputOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputOverVoltage.setStatus("mandatory")


class _AtsOutputLowVoltage_Type(Integer32):
    """Custom type atsOutputLowVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsOutputLowVoltage_Type.__name__ = "Integer32"
_AtsOutputLowVoltage_Object = MibScalar
atsOutputLowVoltage = _AtsOutputLowVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 8),
    _AtsOutputLowVoltage_Type()
)
atsOutputLowVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputLowVoltage.setStatus("mandatory")


class _AtsOutputOverCurrent_Type(Integer32):
    """Custom type atsOutputOverCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsOutputOverCurrent_Type.__name__ = "Integer32"
_AtsOutputOverCurrent_Object = MibScalar
atsOutputOverCurrent = _AtsOutputOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 9),
    _AtsOutputOverCurrent_Type()
)
atsOutputOverCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputOverCurrent.setStatus("mandatory")


class _AtsOverTemperature_Type(Integer32):
    """Custom type atsOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsOverTemperature_Type.__name__ = "Integer32"
_AtsOverTemperature_Object = MibScalar
atsOverTemperature = _AtsOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 10),
    _AtsOverTemperature_Type()
)
atsOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOverTemperature.setStatus("mandatory")


class _AtsOverTemperatureAmbient_Type(Integer32):
    """Custom type atsOverTemperatureAmbient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsOverTemperatureAmbient_Type.__name__ = "Integer32"
_AtsOverTemperatureAmbient_Object = MibScalar
atsOverTemperatureAmbient = _AtsOverTemperatureAmbient_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 11),
    _AtsOverTemperatureAmbient_Type()
)
atsOverTemperatureAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOverTemperatureAmbient.setStatus("mandatory")


class _AtsCommunicationFail_Type(Integer32):
    """Custom type atsCommunicationFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsCommunicationFail_Type.__name__ = "Integer32"
_AtsCommunicationFail_Object = MibScalar
atsCommunicationFail = _AtsCommunicationFail_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 12),
    _AtsCommunicationFail_Type()
)
atsCommunicationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsCommunicationFail.setStatus("mandatory")


class _AtsInputAOverFrequency_Type(Integer32):
    """Custom type atsInputAOverFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputAOverFrequency_Type.__name__ = "Integer32"
_AtsInputAOverFrequency_Object = MibScalar
atsInputAOverFrequency = _AtsInputAOverFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 13),
    _AtsInputAOverFrequency_Type()
)
atsInputAOverFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAOverFrequency.setStatus("mandatory")


class _AtsInputAUnderFrequency_Type(Integer32):
    """Custom type atsInputAUnderFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputAUnderFrequency_Type.__name__ = "Integer32"
_AtsInputAUnderFrequency_Object = MibScalar
atsInputAUnderFrequency = _AtsInputAUnderFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 14),
    _AtsInputAUnderFrequency_Type()
)
atsInputAUnderFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAUnderFrequency.setStatus("mandatory")


class _AtsInputBOverFrequency_Type(Integer32):
    """Custom type atsInputBOverFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputBOverFrequency_Type.__name__ = "Integer32"
_AtsInputBOverFrequency_Object = MibScalar
atsInputBOverFrequency = _AtsInputBOverFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 15),
    _AtsInputBOverFrequency_Type()
)
atsInputBOverFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBOverFrequency.setStatus("mandatory")


class _AtsInputBUnderFrequency_Type(Integer32):
    """Custom type atsInputBUnderFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AtsInputBUnderFrequency_Type.__name__ = "Integer32"
_AtsInputBUnderFrequency_Object = MibScalar
atsInputBUnderFrequency = _AtsInputBUnderFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 3, 16),
    _AtsInputBUnderFrequency_Type()
)
atsInputBUnderFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBUnderFrequency.setStatus("mandatory")
_ModuleControl_ObjectIdentity = ObjectIdentity
moduleControl = _ModuleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 4)
)


class _AtsModeSwitch_Type(Integer32):
    """Custom type atsModeSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inputA", 0),
          ("inputB", 1))
    )


_AtsModeSwitch_Type.__name__ = "Integer32"
_AtsModeSwitch_Object = MibScalar
atsModeSwitch = _AtsModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 4, 1),
    _AtsModeSwitch_Type()
)
atsModeSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsModeSwitch.setStatus("mandatory")
_AtsTransferCount_Type = Integer32
_AtsTransferCount_Object = MibScalar
atsTransferCount = _AtsTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 4, 2),
    _AtsTransferCount_Type()
)
atsTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsTransferCount.setStatus("mandatory")


class _AtsInputAHealthySource_Type(Integer32):
    """Custom type atsInputAHealthySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("healthy", 1))
    )


_AtsInputAHealthySource_Type.__name__ = "Integer32"
_AtsInputAHealthySource_Object = MibScalar
atsInputAHealthySource = _AtsInputAHealthySource_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 4, 3),
    _AtsInputAHealthySource_Type()
)
atsInputAHealthySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputAHealthySource.setStatus("mandatory")


class _AtsInputBHealthySource_Type(Integer32):
    """Custom type atsInputBHealthySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("healthy", 1))
    )


_AtsInputBHealthySource_Type.__name__ = "Integer32"
_AtsInputBHealthySource_Object = MibScalar
atsInputBHealthySource = _AtsInputBHealthySource_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 4, 4),
    _AtsInputBHealthySource_Type()
)
atsInputBHealthySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputBHealthySource.setStatus("mandatory")


class _AtsPreferredSourceConfiguration_Type(Integer32):
    """Custom type atsPreferredSourceConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inputA", 0),
          ("inputB", 1))
    )


_AtsPreferredSourceConfiguration_Type.__name__ = "Integer32"
_AtsPreferredSourceConfiguration_Object = MibScalar
atsPreferredSourceConfiguration = _AtsPreferredSourceConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 4, 5),
    _AtsPreferredSourceConfiguration_Type()
)
atsPreferredSourceConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsPreferredSourceConfiguration.setStatus("mandatory")
_TcpIPMode_ObjectIdentity = ObjectIdentity
tcpIPMode = _TcpIPMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5)
)


class _IpMode_Type(Integer32):
    """Custom type ipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("staticIP", 0),
          ("dhcp", 1))
    )


_IpMode_Type.__name__ = "Integer32"
_IpMode_Object = MibScalar
ipMode = _IpMode_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5, 1),
    _IpMode_Type()
)
ipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMode.setStatus("mandatory")


class _MacAddr_Type(DisplayString):
    """Custom type macAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MacAddr_Type.__name__ = "DisplayString"
_MacAddr_Object = MibScalar
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5, 2),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("mandatory")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5, 3),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("mandatory")
_NetMaskAddr_Type = IpAddress
_NetMaskAddr_Object = MibScalar
netMaskAddr = _NetMaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5, 4),
    _NetMaskAddr_Type()
)
netMaskAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMaskAddr.setStatus("mandatory")
_GatewayAddr_Type = IpAddress
_GatewayAddr_Object = MibScalar
gatewayAddr = _GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5, 5),
    _GatewayAddr_Type()
)
gatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayAddr.setStatus("mandatory")


class _WebFunctionMode_Type(Integer32):
    """Custom type webFunctionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WebFunctionMode_Type.__name__ = "Integer32"
_WebFunctionMode_Object = MibScalar
webFunctionMode = _WebFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 5, 6),
    _WebFunctionMode_Type()
)
webFunctionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webFunctionMode.setStatus("mandatory")
_SnmpSetting_ObjectIdentity = ObjectIdentity
snmpSetting = _SnmpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 6)
)
_TrapAddress1_Type = IpAddress
_TrapAddress1_Object = MibScalar
trapAddress1 = _TrapAddress1_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 6, 1),
    _TrapAddress1_Type()
)
trapAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAddress1.setStatus("mandatory")
_TrapAddress2_Type = IpAddress
_TrapAddress2_Object = MibScalar
trapAddress2 = _TrapAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 6, 2),
    _TrapAddress2_Type()
)
trapAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAddress2.setStatus("mandatory")
_FwUpgrade_ObjectIdentity = ObjectIdentity
fwUpgrade = _FwUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7)
)
_TftpServerAddress_Type = IpAddress
_TftpServerAddress_Object = MibScalar
tftpServerAddress = _TftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 1),
    _TftpServerAddress_Type()
)
tftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerAddress.setStatus("mandatory")


class _TftpWEBFileName_Type(DisplayString):
    """Custom type tftpWEBFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TftpWEBFileName_Type.__name__ = "DisplayString"
_TftpWEBFileName_Object = MibScalar
tftpWEBFileName = _TftpWEBFileName_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 2),
    _TftpWEBFileName_Type()
)
tftpWEBFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpWEBFileName.setStatus("mandatory")


class _TftpLCDFileName_Type(DisplayString):
    """Custom type tftpLCDFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TftpLCDFileName_Type.__name__ = "DisplayString"
_TftpLCDFileName_Object = MibScalar
tftpLCDFileName = _TftpLCDFileName_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 3),
    _TftpLCDFileName_Type()
)
tftpLCDFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpLCDFileName.setStatus("mandatory")


class _WebFirmwareRev_Type(DisplayString):
    """Custom type webFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WebFirmwareRev_Type.__name__ = "DisplayString"
_WebFirmwareRev_Object = MibScalar
webFirmwareRev = _WebFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 4),
    _WebFirmwareRev_Type()
)
webFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webFirmwareRev.setStatus("mandatory")


class _LcdFirmwareRev_Type(DisplayString):
    """Custom type lcdFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LcdFirmwareRev_Type.__name__ = "DisplayString"
_LcdFirmwareRev_Object = MibScalar
lcdFirmwareRev = _LcdFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 5),
    _LcdFirmwareRev_Type()
)
lcdFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcdFirmwareRev.setStatus("mandatory")


class _WebUpgradeFunction_Type(Integer32):
    """Custom type webUpgradeFunction based on Integer32"""
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
        *(("normal", 0),
          ("trigger", 1),
          ("upgrading", 2),
          ("fail", 3))
    )


_WebUpgradeFunction_Type.__name__ = "Integer32"
_WebUpgradeFunction_Object = MibScalar
webUpgradeFunction = _WebUpgradeFunction_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 6),
    _WebUpgradeFunction_Type()
)
webUpgradeFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webUpgradeFunction.setStatus("mandatory")


class _LcdUpgradeFunction_Type(Integer32):
    """Custom type lcdUpgradeFunction based on Integer32"""
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
        *(("normal", 0),
          ("trigger", 1),
          ("upgrading", 2),
          ("fail", 3))
    )


_LcdUpgradeFunction_Type.__name__ = "Integer32"
_LcdUpgradeFunction_Object = MibScalar
lcdUpgradeFunction = _LcdUpgradeFunction_Object(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 7, 7),
    _LcdUpgradeFunction_Type()
)
lcdUpgradeFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcdUpgradeFunction.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100)
)

# Managed Objects groups


# Notification objects

inputAOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 1)
)
if mibBuilder.loadTexts:
    inputAOverVoltage.setStatus(
        ""
    )

r_InputAOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 2)
)
if mibBuilder.loadTexts:
    r_InputAOverVoltage.setStatus(
        ""
    )

inputALowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 3)
)
if mibBuilder.loadTexts:
    inputALowVoltage.setStatus(
        ""
    )

r_InputALowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 4)
)
if mibBuilder.loadTexts:
    r_InputALowVoltage.setStatus(
        ""
    )

inputAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 5)
)
if mibBuilder.loadTexts:
    inputAFail.setStatus(
        ""
    )

r_InputAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 6)
)
if mibBuilder.loadTexts:
    r_InputAFail.setStatus(
        ""
    )

inputBOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 7)
)
if mibBuilder.loadTexts:
    inputBOverVoltage.setStatus(
        ""
    )

r_InputBOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 8)
)
if mibBuilder.loadTexts:
    r_InputBOverVoltage.setStatus(
        ""
    )

inputBLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 9)
)
if mibBuilder.loadTexts:
    inputBLowVoltage.setStatus(
        ""
    )

r_InputBLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 10)
)
if mibBuilder.loadTexts:
    r_InputBLowVoltage.setStatus(
        ""
    )

inputBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 11)
)
if mibBuilder.loadTexts:
    inputBFail.setStatus(
        ""
    )

r_InputBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 12)
)
if mibBuilder.loadTexts:
    r_InputBFail.setStatus(
        ""
    )

outputOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 13)
)
if mibBuilder.loadTexts:
    outputOverVoltage.setStatus(
        ""
    )

r_outputOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 14)
)
if mibBuilder.loadTexts:
    r_outputOverVoltage.setStatus(
        ""
    )

outputLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 15)
)
if mibBuilder.loadTexts:
    outputLowVoltage.setStatus(
        ""
    )

r_outputLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 16)
)
if mibBuilder.loadTexts:
    r_outputLowVoltage.setStatus(
        ""
    )

outputOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 17)
)
if mibBuilder.loadTexts:
    outputOverCurrent.setStatus(
        ""
    )

r_outputOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 18)
)
if mibBuilder.loadTexts:
    r_outputOverCurrent.setStatus(
        ""
    )

overTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 19)
)
if mibBuilder.loadTexts:
    overTemperature.setStatus(
        ""
    )

r_overTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 20)
)
if mibBuilder.loadTexts:
    r_overTemperature.setStatus(
        ""
    )

ambientOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 21)
)
if mibBuilder.loadTexts:
    ambientOverTemperature.setStatus(
        ""
    )

r_ambientOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 22)
)
if mibBuilder.loadTexts:
    r_ambientOverTemperature.setStatus(
        ""
    )

atsCommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 23)
)
if mibBuilder.loadTexts:
    atsCommFail.setStatus(
        ""
    )

r_atsCommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 24)
)
if mibBuilder.loadTexts:
    r_atsCommFail.setStatus(
        ""
    )

inputAOverFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 25)
)
if mibBuilder.loadTexts:
    inputAOverFrequency.setStatus(
        ""
    )

r_InputAOverFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 26)
)
if mibBuilder.loadTexts:
    r_InputAOverFrequency.setStatus(
        ""
    )

inputAUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 27)
)
if mibBuilder.loadTexts:
    inputAUnderFrequency.setStatus(
        ""
    )

r_InputAUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 28)
)
if mibBuilder.loadTexts:
    r_InputAUnderFrequency.setStatus(
        ""
    )

inputBOverFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 29)
)
if mibBuilder.loadTexts:
    inputBOverFrequency.setStatus(
        ""
    )

r_InputBOverFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 30)
)
if mibBuilder.loadTexts:
    r_InputBOverFrequency.setStatus(
        ""
    )

inputBUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 31)
)
if mibBuilder.loadTexts:
    inputBUnderFrequency.setStatus(
        ""
    )

r_InputBUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6785, 1, 12, 100, 0, 32)
)
if mibBuilder.loadTexts:
    r_InputBUnderFrequency.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaTP-MIB",
    **{"delta": delta,
       "tp": tp,
       "ats": ats,
       "atsInfo": atsInfo,
       "atsName": atsName,
       "atsFactoryDate": atsFactoryDate,
       "atsModelName": atsModelName,
       "atsSerialNumber": atsSerialNumber,
       "atsHardwareRevision": atsHardwareRevision,
       "lcdFirmwareRevision": lcdFirmwareRevision,
       "webFirmwareRevision": webFirmwareRevision,
       "ctlFirmwareRevision": ctlFirmwareRevision,
       "systemDate": systemDate,
       "systemTime": systemTime,
       "atsMonitor": atsMonitor,
       "atsStatus": atsStatus,
       "atsInputAFreq": atsInputAFreq,
       "atsInputBFreq": atsInputBFreq,
       "atsInputAVoltageL1-L2": atsInputAVoltageL1_L2,
       "atsInputAVoltageL2-L3": atsInputAVoltageL2_L3,
       "atsInputAVoltageL3-L1": atsInputAVoltageL3_L1,
       "atsInputBVoltageL1-L2": atsInputBVoltageL1_L2,
       "atsInputBVoltageL2-L3": atsInputBVoltageL2_L3,
       "atsInputBVoltageL3-L1": atsInputBVoltageL3_L1,
       "atsOutputVoltageL1-L2": atsOutputVoltageL1_L2,
       "atsOutputVoltageL2-L3": atsOutputVoltageL2_L3,
       "atsOutputVoltageL3-L1": atsOutputVoltageL3_L1,
       "atsOutputCurrentL1": atsOutputCurrentL1,
       "atsOutputCurrentL2": atsOutputCurrentL2,
       "atsOutputCurrentL3": atsOutputCurrentL3,
       "atsOutputTotalCurrent": atsOutputTotalCurrent,
       "atsOutputPowerFactor": atsOutputPowerFactor,
       "atsAmbientTemperature": atsAmbientTemperature,
       "atsOutputPowerRealTotal": atsOutputPowerRealTotal,
       "atsOutputPowerApparentTotal": atsOutputPowerApparentTotal,
       "atsInputAOverVoltageThreshold": atsInputAOverVoltageThreshold,
       "atsInputALowVoltageThreshold": atsInputALowVoltageThreshold,
       "atsInputBOverVoltageThreshold": atsInputBOverVoltageThreshold,
       "atsInputBLowVoltageThreshold": atsInputBLowVoltageThreshold,
       "atsOutputOverVoltageThreshold": atsOutputOverVoltageThreshold,
       "atsOutputLowVoltageThreshold": atsOutputLowVoltageThreshold,
       "atsOutputOverCurrentThreshold": atsOutputOverCurrentThreshold,
       "atsOutputCurrentAccuracyLess20PercentLoad": atsOutputCurrentAccuracyLess20PercentLoad,
       "atsOutputCurrentAccuracyMore20PercentLoad": atsOutputCurrentAccuracyMore20PercentLoad,
       "atsOutputCurrentResolution": atsOutputCurrentResolution,
       "atsOutputVoltageAccuracy": atsOutputVoltageAccuracy,
       "atsOutputVoltageResolution": atsOutputVoltageResolution,
       "atsOutputFreqAccuracy": atsOutputFreqAccuracy,
       "atsOutputFreqResolution": atsOutputFreqResolution,
       "atsOutputApparentPowerAccuracyLess20PercentLoad": atsOutputApparentPowerAccuracyLess20PercentLoad,
       "atsOutputApparentPowerAccuracyMore20PercentLoad": atsOutputApparentPowerAccuracyMore20PercentLoad,
       "atsOutputApparentPowerResolution": atsOutputApparentPowerResolution,
       "atsOutputRealPowerAccuracyLess20PercentLoad": atsOutputRealPowerAccuracyLess20PercentLoad,
       "atsOutputRealPowerAccuracyMore20PercentLoad": atsOutputRealPowerAccuracyMore20PercentLoad,
       "atsOutputRealPowerResolution": atsOutputRealPowerResolution,
       "atsOutputPowerFactorAccuracy": atsOutputPowerFactorAccuracy,
       "atsOutputPowerFactorResolution": atsOutputPowerFactorResolution,
       "atsTemperatureAccuracy": atsTemperatureAccuracy,
       "atsTemperatureResolution": atsTemperatureResolution,
       "atsAlarm": atsAlarm,
       "atsInputAOverVoltage": atsInputAOverVoltage,
       "atsInputALowVoltage": atsInputALowVoltage,
       "atsInputAFail": atsInputAFail,
       "atsInputBOverVoltage": atsInputBOverVoltage,
       "atsInputBLowVoltage": atsInputBLowVoltage,
       "atsInputBFail": atsInputBFail,
       "atsOutputOverVoltage": atsOutputOverVoltage,
       "atsOutputLowVoltage": atsOutputLowVoltage,
       "atsOutputOverCurrent": atsOutputOverCurrent,
       "atsOverTemperature": atsOverTemperature,
       "atsOverTemperatureAmbient": atsOverTemperatureAmbient,
       "atsCommunicationFail": atsCommunicationFail,
       "atsInputAOverFrequency": atsInputAOverFrequency,
       "atsInputAUnderFrequency": atsInputAUnderFrequency,
       "atsInputBOverFrequency": atsInputBOverFrequency,
       "atsInputBUnderFrequency": atsInputBUnderFrequency,
       "moduleControl": moduleControl,
       "atsModeSwitch": atsModeSwitch,
       "atsTransferCount": atsTransferCount,
       "atsInputAHealthySource": atsInputAHealthySource,
       "atsInputBHealthySource": atsInputBHealthySource,
       "atsPreferredSourceConfiguration": atsPreferredSourceConfiguration,
       "tcpIPMode": tcpIPMode,
       "ipMode": ipMode,
       "macAddr": macAddr,
       "ipAddr": ipAddr,
       "netMaskAddr": netMaskAddr,
       "gatewayAddr": gatewayAddr,
       "webFunctionMode": webFunctionMode,
       "snmpSetting": snmpSetting,
       "trapAddress1": trapAddress1,
       "trapAddress2": trapAddress2,
       "fwUpgrade": fwUpgrade,
       "tftpServerAddress": tftpServerAddress,
       "tftpWEBFileName": tftpWEBFileName,
       "tftpLCDFileName": tftpLCDFileName,
       "webFirmwareRev": webFirmwareRev,
       "lcdFirmwareRev": lcdFirmwareRev,
       "webUpgradeFunction": webUpgradeFunction,
       "lcdUpgradeFunction": lcdUpgradeFunction,
       "traps": traps,
       "inputAOverVoltage": inputAOverVoltage,
       "r_InputAOverVoltage": r_InputAOverVoltage,
       "inputALowVoltage": inputALowVoltage,
       "r_InputALowVoltage": r_InputALowVoltage,
       "inputAFail": inputAFail,
       "r_InputAFail": r_InputAFail,
       "inputBOverVoltage": inputBOverVoltage,
       "r_InputBOverVoltage": r_InputBOverVoltage,
       "inputBLowVoltage": inputBLowVoltage,
       "r_InputBLowVoltage": r_InputBLowVoltage,
       "inputBFail": inputBFail,
       "r_InputBFail": r_InputBFail,
       "outputOverVoltage": outputOverVoltage,
       "r_outputOverVoltage": r_outputOverVoltage,
       "outputLowVoltage": outputLowVoltage,
       "r_outputLowVoltage": r_outputLowVoltage,
       "outputOverCurrent": outputOverCurrent,
       "r_outputOverCurrent": r_outputOverCurrent,
       "overTemperature": overTemperature,
       "r_overTemperature": r_overTemperature,
       "ambientOverTemperature": ambientOverTemperature,
       "r_ambientOverTemperature": r_ambientOverTemperature,
       "atsCommFail": atsCommFail,
       "r_atsCommFail": r_atsCommFail,
       "inputAOverFrequency": inputAOverFrequency,
       "r_InputAOverFrequency": r_InputAOverFrequency,
       "inputAUnderFrequency": inputAUnderFrequency,
       "r_InputAUnderFrequency": r_InputAUnderFrequency,
       "inputBOverFrequency": inputBOverFrequency,
       "r_InputBOverFrequency": r_InputBOverFrequency,
       "inputBUnderFrequency": inputBUnderFrequency,
       "r_InputBUnderFrequency": r_InputBUnderFrequency}
)
