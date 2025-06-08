# SNMP MIB module (GATESAIR-FLEXIVA-LX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gatesair_43768/GATESAIR-FLEXIVA-LX-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:36 2025
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

gates_air = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43768)
)
if mibBuilder.loadTexts:
    gates_air.setRevisions(
        ("2017-10-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lx_ObjectIdentity = ObjectIdentity
lx = _Lx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137)
)
_Aio_ObjectIdentity = ObjectIdentity
aio = _Aio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 1)
)
_AioRefclkAdj_Type = DisplayString
_AioRefclkAdj_Object = MibScalar
aioRefclkAdj = _AioRefclkAdj_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 1, 1),
    _AioRefclkAdj_Type()
)
aioRefclkAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aioRefclkAdj.setStatus("current")
if mibBuilder.loadTexts:
    aioRefclkAdj.setUnits("ppm")
_Alarm1_ObjectIdentity = ObjectIdentity
alarm1 = _Alarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2)
)
_Alarm1Email_ObjectIdentity = ObjectIdentity
alarm1Email = _Alarm1Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 1)
)
_Alarm1EmailActive_Type = DisplayString
_Alarm1EmailActive_Object = MibScalar
alarm1EmailActive = _Alarm1EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 1, 1),
    _Alarm1EmailActive_Type()
)
alarm1EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1EmailActive.setStatus("current")
_Alarm1FwdPowerThreshold_Type = DisplayString
_Alarm1FwdPowerThreshold_Object = MibScalar
alarm1FwdPowerThreshold = _Alarm1FwdPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 2),
    _Alarm1FwdPowerThreshold_Type()
)
alarm1FwdPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1FwdPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm1FwdPowerThreshold.setUnits("W")
_Alarm1ModulationThreshold_Type = DisplayString
_Alarm1ModulationThreshold_Object = MibScalar
alarm1ModulationThreshold = _Alarm1ModulationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 3),
    _Alarm1ModulationThreshold_Type()
)
alarm1ModulationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1ModulationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm1ModulationThreshold.setUnits("Hz")
_Alarm1OffDelay_Type = DisplayString
_Alarm1OffDelay_Object = MibScalar
alarm1OffDelay = _Alarm1OffDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 4),
    _Alarm1OffDelay_Type()
)
alarm1OffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1OffDelay.setStatus("current")
if mibBuilder.loadTexts:
    alarm1OffDelay.setUnits("s")
_Alarm1OnDelay_Type = DisplayString
_Alarm1OnDelay_Object = MibScalar
alarm1OnDelay = _Alarm1OnDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 5),
    _Alarm1OnDelay_Type()
)
alarm1OnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1OnDelay.setStatus("current")
if mibBuilder.loadTexts:
    alarm1OnDelay.setUnits("s")
_Alarm1Polarity_Type = DisplayString
_Alarm1Polarity_Object = MibScalar
alarm1Polarity = _Alarm1Polarity_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 6),
    _Alarm1Polarity_Type()
)
alarm1Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1Polarity.setStatus("current")
_Alarm1RevPowerThreshold_Type = DisplayString
_Alarm1RevPowerThreshold_Object = MibScalar
alarm1RevPowerThreshold = _Alarm1RevPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 7),
    _Alarm1RevPowerThreshold_Type()
)
alarm1RevPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1RevPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm1RevPowerThreshold.setUnits("W")
_Alarm1Source_Type = DisplayString
_Alarm1Source_Object = MibScalar
alarm1Source = _Alarm1Source_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 8),
    _Alarm1Source_Type()
)
alarm1Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1Source.setStatus("current")
_Alarm1Telemetrysource_Type = DisplayString
_Alarm1Telemetrysource_Object = MibScalar
alarm1Telemetrysource = _Alarm1Telemetrysource_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 9),
    _Alarm1Telemetrysource_Type()
)
alarm1Telemetrysource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1Telemetrysource.setStatus("current")
_Alarm1TempThreshold_Type = DisplayString
_Alarm1TempThreshold_Object = MibScalar
alarm1TempThreshold = _Alarm1TempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 10),
    _Alarm1TempThreshold_Type()
)
alarm1TempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1TempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm1TempThreshold.setUnits("C")
_Alarm1Trap_ObjectIdentity = ObjectIdentity
alarm1Trap = _Alarm1Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 11)
)
_Alarm1TrapActive_Type = DisplayString
_Alarm1TrapActive_Object = MibScalar
alarm1TrapActive = _Alarm1TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 11, 1),
    _Alarm1TrapActive_Type()
)
alarm1TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1TrapActive.setStatus("current")
_Alarm1Type_Type = DisplayString
_Alarm1Type_Object = MibScalar
alarm1Type = _Alarm1Type_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 2, 12),
    _Alarm1Type_Type()
)
alarm1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1Type.setStatus("current")
_Alarm2_ObjectIdentity = ObjectIdentity
alarm2 = _Alarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3)
)
_Alarm2Email_ObjectIdentity = ObjectIdentity
alarm2Email = _Alarm2Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 1)
)
_Alarm2EmailActive_Type = DisplayString
_Alarm2EmailActive_Object = MibScalar
alarm2EmailActive = _Alarm2EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 1, 1),
    _Alarm2EmailActive_Type()
)
alarm2EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2EmailActive.setStatus("current")
_Alarm2FwdPowerThreshold_Type = DisplayString
_Alarm2FwdPowerThreshold_Object = MibScalar
alarm2FwdPowerThreshold = _Alarm2FwdPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 2),
    _Alarm2FwdPowerThreshold_Type()
)
alarm2FwdPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2FwdPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm2FwdPowerThreshold.setUnits("W")
_Alarm2ModulationThreshold_Type = DisplayString
_Alarm2ModulationThreshold_Object = MibScalar
alarm2ModulationThreshold = _Alarm2ModulationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 3),
    _Alarm2ModulationThreshold_Type()
)
alarm2ModulationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2ModulationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm2ModulationThreshold.setUnits("Hz")
_Alarm2OffDelay_Type = DisplayString
_Alarm2OffDelay_Object = MibScalar
alarm2OffDelay = _Alarm2OffDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 4),
    _Alarm2OffDelay_Type()
)
alarm2OffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2OffDelay.setStatus("current")
if mibBuilder.loadTexts:
    alarm2OffDelay.setUnits("s")
_Alarm2OnDelay_Type = DisplayString
_Alarm2OnDelay_Object = MibScalar
alarm2OnDelay = _Alarm2OnDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 5),
    _Alarm2OnDelay_Type()
)
alarm2OnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2OnDelay.setStatus("current")
if mibBuilder.loadTexts:
    alarm2OnDelay.setUnits("s")
_Alarm2Polarity_Type = DisplayString
_Alarm2Polarity_Object = MibScalar
alarm2Polarity = _Alarm2Polarity_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 6),
    _Alarm2Polarity_Type()
)
alarm2Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2Polarity.setStatus("current")
_Alarm2RevPowerThreshold_Type = DisplayString
_Alarm2RevPowerThreshold_Object = MibScalar
alarm2RevPowerThreshold = _Alarm2RevPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 7),
    _Alarm2RevPowerThreshold_Type()
)
alarm2RevPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2RevPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm2RevPowerThreshold.setUnits("W")
_Alarm2Source_Type = DisplayString
_Alarm2Source_Object = MibScalar
alarm2Source = _Alarm2Source_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 8),
    _Alarm2Source_Type()
)
alarm2Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2Source.setStatus("current")
_Alarm2Telemetrysource_Type = DisplayString
_Alarm2Telemetrysource_Object = MibScalar
alarm2Telemetrysource = _Alarm2Telemetrysource_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 9),
    _Alarm2Telemetrysource_Type()
)
alarm2Telemetrysource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2Telemetrysource.setStatus("current")
_Alarm2TempThreshold_Type = DisplayString
_Alarm2TempThreshold_Object = MibScalar
alarm2TempThreshold = _Alarm2TempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 10),
    _Alarm2TempThreshold_Type()
)
alarm2TempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2TempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm2TempThreshold.setUnits("C")
_Alarm2Trap_ObjectIdentity = ObjectIdentity
alarm2Trap = _Alarm2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 11)
)
_Alarm2TrapActive_Type = DisplayString
_Alarm2TrapActive_Object = MibScalar
alarm2TrapActive = _Alarm2TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 11, 1),
    _Alarm2TrapActive_Type()
)
alarm2TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2TrapActive.setStatus("current")
_Alarm2Type_Type = DisplayString
_Alarm2Type_Object = MibScalar
alarm2Type = _Alarm2Type_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 3, 12),
    _Alarm2Type_Type()
)
alarm2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2Type.setStatus("current")
_Alarm3_ObjectIdentity = ObjectIdentity
alarm3 = _Alarm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4)
)
_Alarm3Email_ObjectIdentity = ObjectIdentity
alarm3Email = _Alarm3Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 1)
)
_Alarm3EmailActive_Type = DisplayString
_Alarm3EmailActive_Object = MibScalar
alarm3EmailActive = _Alarm3EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 1, 1),
    _Alarm3EmailActive_Type()
)
alarm3EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3EmailActive.setStatus("current")
_Alarm3FwdPowerThreshold_Type = DisplayString
_Alarm3FwdPowerThreshold_Object = MibScalar
alarm3FwdPowerThreshold = _Alarm3FwdPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 2),
    _Alarm3FwdPowerThreshold_Type()
)
alarm3FwdPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3FwdPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm3FwdPowerThreshold.setUnits("W")
_Alarm3ModulationThreshold_Type = DisplayString
_Alarm3ModulationThreshold_Object = MibScalar
alarm3ModulationThreshold = _Alarm3ModulationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 3),
    _Alarm3ModulationThreshold_Type()
)
alarm3ModulationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3ModulationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm3ModulationThreshold.setUnits("Hz")
_Alarm3OffDelay_Type = DisplayString
_Alarm3OffDelay_Object = MibScalar
alarm3OffDelay = _Alarm3OffDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 4),
    _Alarm3OffDelay_Type()
)
alarm3OffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3OffDelay.setStatus("current")
if mibBuilder.loadTexts:
    alarm3OffDelay.setUnits("s")
_Alarm3OnDelay_Type = DisplayString
_Alarm3OnDelay_Object = MibScalar
alarm3OnDelay = _Alarm3OnDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 5),
    _Alarm3OnDelay_Type()
)
alarm3OnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3OnDelay.setStatus("current")
if mibBuilder.loadTexts:
    alarm3OnDelay.setUnits("s")
_Alarm3Polarity_Type = DisplayString
_Alarm3Polarity_Object = MibScalar
alarm3Polarity = _Alarm3Polarity_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 6),
    _Alarm3Polarity_Type()
)
alarm3Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3Polarity.setStatus("current")
_Alarm3RevPowerThreshold_Type = DisplayString
_Alarm3RevPowerThreshold_Object = MibScalar
alarm3RevPowerThreshold = _Alarm3RevPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 7),
    _Alarm3RevPowerThreshold_Type()
)
alarm3RevPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3RevPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm3RevPowerThreshold.setUnits("W")
_Alarm3Source_Type = DisplayString
_Alarm3Source_Object = MibScalar
alarm3Source = _Alarm3Source_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 8),
    _Alarm3Source_Type()
)
alarm3Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3Source.setStatus("current")
_Alarm3Telemetrysource_Type = DisplayString
_Alarm3Telemetrysource_Object = MibScalar
alarm3Telemetrysource = _Alarm3Telemetrysource_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 9),
    _Alarm3Telemetrysource_Type()
)
alarm3Telemetrysource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3Telemetrysource.setStatus("current")
_Alarm3TempThreshold_Type = DisplayString
_Alarm3TempThreshold_Object = MibScalar
alarm3TempThreshold = _Alarm3TempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 10),
    _Alarm3TempThreshold_Type()
)
alarm3TempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3TempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarm3TempThreshold.setUnits("C")
_Alarm3Trap_ObjectIdentity = ObjectIdentity
alarm3Trap = _Alarm3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 11)
)
_Alarm3TrapActive_Type = DisplayString
_Alarm3TrapActive_Object = MibScalar
alarm3TrapActive = _Alarm3TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 11, 1),
    _Alarm3TrapActive_Type()
)
alarm3TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3TrapActive.setStatus("current")
_Alarm3Type_Type = DisplayString
_Alarm3Type_Object = MibScalar
alarm3Type = _Alarm3Type_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 4, 12),
    _Alarm3Type_Type()
)
alarm3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm3Type.setStatus("current")
_Audio_ObjectIdentity = ObjectIdentity
audio = _Audio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5)
)
_AudioDelay_Type = DisplayString
_AudioDelay_Object = MibScalar
audioDelay = _AudioDelay_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 1),
    _AudioDelay_Type()
)
audioDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDelay.setStatus("current")
if mibBuilder.loadTexts:
    audioDelay.setUnits("us")
_AudioInput_Type = DisplayString
_AudioInput_Object = MibScalar
audioInput = _AudioInput_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 2),
    _AudioInput_Type()
)
audioInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioInput.setStatus("current")
_AudioInputs_ObjectIdentity = ObjectIdentity
audioInputs = _AudioInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 3)
)
_AudioInputsAnalogRef_Type = DisplayString
_AudioInputsAnalogRef_Object = MibScalar
audioInputsAnalogRef = _AudioInputsAnalogRef_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 3, 1),
    _AudioInputsAnalogRef_Type()
)
audioInputsAnalogRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioInputsAnalogRef.setStatus("current")
if mibBuilder.loadTexts:
    audioInputsAnalogRef.setUnits("dBu")
_AudioInputsDigitalRef_Type = DisplayString
_AudioInputsDigitalRef_Object = MibScalar
audioInputsDigitalRef = _AudioInputsDigitalRef_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 3, 2),
    _AudioInputsDigitalRef_Type()
)
audioInputsDigitalRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioInputsDigitalRef.setStatus("current")
if mibBuilder.loadTexts:
    audioInputsDigitalRef.setUnits("dBFS")
_AudioProcessingPreset_Type = DisplayString
_AudioProcessingPreset_Object = MibScalar
audioProcessingPreset = _AudioProcessingPreset_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 4),
    _AudioProcessingPreset_Type()
)
audioProcessingPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioProcessingPreset.setStatus("current")
_AudioProcessorOff_Type = DisplayString
_AudioProcessorOff_Object = MibScalar
audioProcessorOff = _AudioProcessorOff_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 5),
    _AudioProcessorOff_Type()
)
audioProcessorOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioProcessorOff.setStatus("current")
_AudioRightTrim_Type = DisplayString
_AudioRightTrim_Object = MibScalar
audioRightTrim = _AudioRightTrim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 6),
    _AudioRightTrim_Type()
)
audioRightTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioRightTrim.setStatus("current")
if mibBuilder.loadTexts:
    audioRightTrim.setUnits("dB")
_AudioStereo_Type = DisplayString
_AudioStereo_Object = MibScalar
audioStereo = _AudioStereo_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 7),
    _AudioStereo_Type()
)
audioStereo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioStereo.setStatus("current")
_AudioTrim_Type = DisplayString
_AudioTrim_Object = MibScalar
audioTrim = _AudioTrim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 5, 8),
    _AudioTrim_Type()
)
audioTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioTrim.setStatus("current")
if mibBuilder.loadTexts:
    audioTrim.setUnits("dB")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6)
)
_EmailCounter_ObjectIdentity = ObjectIdentity
emailCounter = _EmailCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 1)
)
_EmailCounterToday_Type = DisplayString
_EmailCounterToday_Object = MibScalar
emailCounterToday = _EmailCounterToday_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 1, 1),
    _EmailCounterToday_Type()
)
emailCounterToday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailCounterToday.setStatus("current")
_EmailFrom_Type = DisplayString
_EmailFrom_Object = MibScalar
emailFrom = _EmailFrom_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 2),
    _EmailFrom_Type()
)
emailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailFrom.setStatus("current")
_EmailLimit_ObjectIdentity = ObjectIdentity
emailLimit = _EmailLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 3)
)
_EmailLimitDaily_Type = DisplayString
_EmailLimitDaily_Object = MibScalar
emailLimitDaily = _EmailLimitDaily_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 3, 1),
    _EmailLimitDaily_Type()
)
emailLimitDaily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailLimitDaily.setStatus("current")
_EmailMethod_Type = DisplayString
_EmailMethod_Object = MibScalar
emailMethod = _EmailMethod_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 4),
    _EmailMethod_Type()
)
emailMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailMethod.setStatus("current")
_EmailRecipient_Type = DisplayString
_EmailRecipient_Object = MibScalar
emailRecipient = _EmailRecipient_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 5),
    _EmailRecipient_Type()
)
emailRecipient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailRecipient.setStatus("current")
_EmailTest_ObjectIdentity = ObjectIdentity
emailTest = _EmailTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 6)
)
_EmailTestRecipient_Type = DisplayString
_EmailTestRecipient_Object = MibScalar
emailTestRecipient = _EmailTestRecipient_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 6, 1),
    _EmailTestRecipient_Type()
)
emailTestRecipient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailTestRecipient.setStatus("current")
_EmailTestSend_Type = DisplayString
_EmailTestSend_Object = MibScalar
emailTestSend = _EmailTestSend_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 6, 6, 2),
    _EmailTestSend_Type()
)
emailTestSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailTestSend.setStatus("current")
_Mpx_ObjectIdentity = ObjectIdentity
mpx = _Mpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7)
)
_MpxDigMpxIn_ObjectIdentity = ObjectIdentity
mpxDigMpxIn = _MpxDigMpxIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 1)
)
_MpxDigMpxInLevel_Type = DisplayString
_MpxDigMpxInLevel_Object = MibScalar
mpxDigMpxInLevel = _MpxDigMpxInLevel_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 1, 1),
    _MpxDigMpxInLevel_Type()
)
mpxDigMpxInLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxDigMpxInLevel.setStatus("current")
if mibBuilder.loadTexts:
    mpxDigMpxInLevel.setUnits("dBFS")
_MpxGen_ObjectIdentity = ObjectIdentity
mpxGen = _MpxGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2)
)
_MpxGenCompClipper_Type = DisplayString
_MpxGenCompClipper_Object = MibScalar
mpxGenCompClipper = _MpxGenCompClipper_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 1),
    _MpxGenCompClipper_Type()
)
mpxGenCompClipper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenCompClipper.setStatus("current")
if mibBuilder.loadTexts:
    mpxGenCompClipper.setUnits("dB")
_MpxGenLevel_Type = DisplayString
_MpxGenLevel_Object = MibScalar
mpxGenLevel = _MpxGenLevel_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 2),
    _MpxGenLevel_Type()
)
mpxGenLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenLevel.setStatus("current")
if mibBuilder.loadTexts:
    mpxGenLevel.setUnits("kHz")
_MpxGenPilotLevel_Type = DisplayString
_MpxGenPilotLevel_Object = MibScalar
mpxGenPilotLevel = _MpxGenPilotLevel_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 3),
    _MpxGenPilotLevel_Type()
)
mpxGenPilotLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenPilotLevel.setStatus("current")
if mibBuilder.loadTexts:
    mpxGenPilotLevel.setUnits("%")
_MpxGenPilotProtection_Type = DisplayString
_MpxGenPilotProtection_Object = MibScalar
mpxGenPilotProtection = _MpxGenPilotProtection_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 4),
    _MpxGenPilotProtection_Type()
)
mpxGenPilotProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenPilotProtection.setStatus("current")
_MpxGenPowerLimit_Type = DisplayString
_MpxGenPowerLimit_Object = MibScalar
mpxGenPowerLimit = _MpxGenPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 5),
    _MpxGenPowerLimit_Type()
)
mpxGenPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpxGenPowerLimit.setStatus("current")
_MpxGenPreemphasis_Type = DisplayString
_MpxGenPreemphasis_Object = MibScalar
mpxGenPreemphasis = _MpxGenPreemphasis_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 6),
    _MpxGenPreemphasis_Type()
)
mpxGenPreemphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenPreemphasis.setStatus("current")
_MpxGenRdsLevel_Type = DisplayString
_MpxGenRdsLevel_Object = MibScalar
mpxGenRdsLevel = _MpxGenRdsLevel_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 7),
    _MpxGenRdsLevel_Type()
)
mpxGenRdsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenRdsLevel.setStatus("current")
if mibBuilder.loadTexts:
    mpxGenRdsLevel.setUnits("%")
_MpxGenSource_Type = DisplayString
_MpxGenSource_Object = MibScalar
mpxGenSource = _MpxGenSource_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 2, 8),
    _MpxGenSource_Type()
)
mpxGenSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxGenSource.setStatus("current")
_MpxInput1_ObjectIdentity = ObjectIdentity
mpxInput1 = _MpxInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 3)
)
_MpxInput1Level_Type = DisplayString
_MpxInput1Level_Object = MibScalar
mpxInput1Level = _MpxInput1Level_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 3, 1),
    _MpxInput1Level_Type()
)
mpxInput1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxInput1Level.setStatus("current")
if mibBuilder.loadTexts:
    mpxInput1Level.setUnits("dBu")
_MpxInput1Trim_Type = DisplayString
_MpxInput1Trim_Object = MibScalar
mpxInput1Trim = _MpxInput1Trim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 3, 2),
    _MpxInput1Trim_Type()
)
mpxInput1Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxInput1Trim.setStatus("current")
if mibBuilder.loadTexts:
    mpxInput1Trim.setUnits("dB")
_MpxInput2_ObjectIdentity = ObjectIdentity
mpxInput2 = _MpxInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 4)
)
_MpxInput2Level_Type = DisplayString
_MpxInput2Level_Object = MibScalar
mpxInput2Level = _MpxInput2Level_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 4, 1),
    _MpxInput2Level_Type()
)
mpxInput2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxInput2Level.setStatus("current")
if mibBuilder.loadTexts:
    mpxInput2Level.setUnits("dBu")
_MpxInput2Trim_Type = DisplayString
_MpxInput2Trim_Object = MibScalar
mpxInput2Trim = _MpxInput2Trim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 4, 2),
    _MpxInput2Trim_Type()
)
mpxInput2Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxInput2Trim.setStatus("current")
if mibBuilder.loadTexts:
    mpxInput2Trim.setUnits("dB")
_MpxOutput1_ObjectIdentity = ObjectIdentity
mpxOutput1 = _MpxOutput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 5)
)
_MpxOutput1Level_Type = DisplayString
_MpxOutput1Level_Object = MibScalar
mpxOutput1Level = _MpxOutput1Level_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 5, 1),
    _MpxOutput1Level_Type()
)
mpxOutput1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxOutput1Level.setStatus("current")
if mibBuilder.loadTexts:
    mpxOutput1Level.setUnits("dBu")
_MpxOutput1Source_Type = DisplayString
_MpxOutput1Source_Object = MibScalar
mpxOutput1Source = _MpxOutput1Source_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 5, 2),
    _MpxOutput1Source_Type()
)
mpxOutput1Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxOutput1Source.setStatus("current")
_MpxOutput1Trim_Type = DisplayString
_MpxOutput1Trim_Object = MibScalar
mpxOutput1Trim = _MpxOutput1Trim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 5, 3),
    _MpxOutput1Trim_Type()
)
mpxOutput1Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxOutput1Trim.setStatus("current")
if mibBuilder.loadTexts:
    mpxOutput1Trim.setUnits("dB")
_MpxOutput2_ObjectIdentity = ObjectIdentity
mpxOutput2 = _MpxOutput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 6)
)
_MpxOutput2Level_Type = DisplayString
_MpxOutput2Level_Object = MibScalar
mpxOutput2Level = _MpxOutput2Level_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 6, 1),
    _MpxOutput2Level_Type()
)
mpxOutput2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxOutput2Level.setStatus("current")
if mibBuilder.loadTexts:
    mpxOutput2Level.setUnits("dBu")
_MpxOutput2Source_Type = DisplayString
_MpxOutput2Source_Object = MibScalar
mpxOutput2Source = _MpxOutput2Source_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 6, 2),
    _MpxOutput2Source_Type()
)
mpxOutput2Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxOutput2Source.setStatus("current")
_MpxOutput2Trim_Type = DisplayString
_MpxOutput2Trim_Object = MibScalar
mpxOutput2Trim = _MpxOutput2Trim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 6, 3),
    _MpxOutput2Trim_Type()
)
mpxOutput2Trim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxOutput2Trim.setStatus("current")
if mibBuilder.loadTexts:
    mpxOutput2Trim.setUnits("dB")
_MpxTuner_ObjectIdentity = ObjectIdentity
mpxTuner = _MpxTuner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 7)
)
_MpxTunerTrim_Type = DisplayString
_MpxTunerTrim_Object = MibScalar
mpxTunerTrim = _MpxTunerTrim_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 7, 7, 1),
    _MpxTunerTrim_Type()
)
mpxTunerTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxTunerTrim.setStatus("current")
if mibBuilder.loadTexts:
    mpxTunerTrim.setUnits("dBu")
_Powerscheduler_ObjectIdentity = ObjectIdentity
powerscheduler = _Powerscheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 8)
)
_PowerschedulerEnabled_Type = DisplayString
_PowerschedulerEnabled_Object = MibScalar
powerschedulerEnabled = _PowerschedulerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 8, 1),
    _PowerschedulerEnabled_Type()
)
powerschedulerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerschedulerEnabled.setStatus("current")
_PowerschedulerFinishtime_Type = DisplayString
_PowerschedulerFinishtime_Object = MibScalar
powerschedulerFinishtime = _PowerschedulerFinishtime_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 8, 2),
    _PowerschedulerFinishtime_Type()
)
powerschedulerFinishtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerschedulerFinishtime.setStatus("current")
_PowerschedulerPower_Type = DisplayString
_PowerschedulerPower_Object = MibScalar
powerschedulerPower = _PowerschedulerPower_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 8, 3),
    _PowerschedulerPower_Type()
)
powerschedulerPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerschedulerPower.setStatus("current")
if mibBuilder.loadTexts:
    powerschedulerPower.setUnits("W")
_PowerschedulerStarttime_Type = DisplayString
_PowerschedulerStarttime_Object = MibScalar
powerschedulerStarttime = _PowerschedulerStarttime_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 8, 4),
    _PowerschedulerStarttime_Type()
)
powerschedulerStarttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerschedulerStarttime.setStatus("current")
_Rds_ObjectIdentity = ObjectIdentity
rds = _Rds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9)
)
_RdsDsn1_ObjectIdentity = ObjectIdentity
rdsDsn1 = _RdsDsn1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1)
)
_RdsDsn1Psn0_ObjectIdentity = ObjectIdentity
rdsDsn1Psn0 = _RdsDsn1Psn0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1)
)
_RdsDsn1Psn0Af_ObjectIdentity = ObjectIdentity
rdsDsn1Psn0Af = _RdsDsn1Psn0Af_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1)
)
_RdsDsn1Psn0Af10a_Type = DisplayString
_RdsDsn1Psn0Af10a_Object = MibScalar
rdsDsn1Psn0Af10a = _RdsDsn1Psn0Af10a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 1),
    _RdsDsn1Psn0Af10a_Type()
)
rdsDsn1Psn0Af10a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af10a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af10a.setUnits("Hz")
_RdsDsn1Psn0Af10b_Type = DisplayString
_RdsDsn1Psn0Af10b_Object = MibScalar
rdsDsn1Psn0Af10b = _RdsDsn1Psn0Af10b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 2),
    _RdsDsn1Psn0Af10b_Type()
)
rdsDsn1Psn0Af10b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af10b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af10b.setUnits("Hz")
_RdsDsn1Psn0Af11a_Type = DisplayString
_RdsDsn1Psn0Af11a_Object = MibScalar
rdsDsn1Psn0Af11a = _RdsDsn1Psn0Af11a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 3),
    _RdsDsn1Psn0Af11a_Type()
)
rdsDsn1Psn0Af11a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af11a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af11a.setUnits("Hz")
_RdsDsn1Psn0Af11b_Type = DisplayString
_RdsDsn1Psn0Af11b_Object = MibScalar
rdsDsn1Psn0Af11b = _RdsDsn1Psn0Af11b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 4),
    _RdsDsn1Psn0Af11b_Type()
)
rdsDsn1Psn0Af11b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af11b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af11b.setUnits("Hz")
_RdsDsn1Psn0Af12a_Type = DisplayString
_RdsDsn1Psn0Af12a_Object = MibScalar
rdsDsn1Psn0Af12a = _RdsDsn1Psn0Af12a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 5),
    _RdsDsn1Psn0Af12a_Type()
)
rdsDsn1Psn0Af12a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af12a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af12a.setUnits("Hz")
_RdsDsn1Psn0Af12b_Type = DisplayString
_RdsDsn1Psn0Af12b_Object = MibScalar
rdsDsn1Psn0Af12b = _RdsDsn1Psn0Af12b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 6),
    _RdsDsn1Psn0Af12b_Type()
)
rdsDsn1Psn0Af12b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af12b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af12b.setUnits("Hz")
_RdsDsn1Psn0Af13a_Type = DisplayString
_RdsDsn1Psn0Af13a_Object = MibScalar
rdsDsn1Psn0Af13a = _RdsDsn1Psn0Af13a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 7),
    _RdsDsn1Psn0Af13a_Type()
)
rdsDsn1Psn0Af13a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af13a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af13a.setUnits("Hz")
_RdsDsn1Psn0Af13b_Type = DisplayString
_RdsDsn1Psn0Af13b_Object = MibScalar
rdsDsn1Psn0Af13b = _RdsDsn1Psn0Af13b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 8),
    _RdsDsn1Psn0Af13b_Type()
)
rdsDsn1Psn0Af13b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af13b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af13b.setUnits("Hz")
_RdsDsn1Psn0Af1b_Type = DisplayString
_RdsDsn1Psn0Af1b_Object = MibScalar
rdsDsn1Psn0Af1b = _RdsDsn1Psn0Af1b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 9),
    _RdsDsn1Psn0Af1b_Type()
)
rdsDsn1Psn0Af1b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af1b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af1b.setUnits("Hz")
_RdsDsn1Psn0Af2a_Type = DisplayString
_RdsDsn1Psn0Af2a_Object = MibScalar
rdsDsn1Psn0Af2a = _RdsDsn1Psn0Af2a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 10),
    _RdsDsn1Psn0Af2a_Type()
)
rdsDsn1Psn0Af2a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af2a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af2a.setUnits("Hz")
_RdsDsn1Psn0Af2b_Type = DisplayString
_RdsDsn1Psn0Af2b_Object = MibScalar
rdsDsn1Psn0Af2b = _RdsDsn1Psn0Af2b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 11),
    _RdsDsn1Psn0Af2b_Type()
)
rdsDsn1Psn0Af2b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af2b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af2b.setUnits("Hz")
_RdsDsn1Psn0Af3a_Type = DisplayString
_RdsDsn1Psn0Af3a_Object = MibScalar
rdsDsn1Psn0Af3a = _RdsDsn1Psn0Af3a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 12),
    _RdsDsn1Psn0Af3a_Type()
)
rdsDsn1Psn0Af3a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af3a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af3a.setUnits("Hz")
_RdsDsn1Psn0Af3b_Type = DisplayString
_RdsDsn1Psn0Af3b_Object = MibScalar
rdsDsn1Psn0Af3b = _RdsDsn1Psn0Af3b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 13),
    _RdsDsn1Psn0Af3b_Type()
)
rdsDsn1Psn0Af3b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af3b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af3b.setUnits("Hz")
_RdsDsn1Psn0Af4a_Type = DisplayString
_RdsDsn1Psn0Af4a_Object = MibScalar
rdsDsn1Psn0Af4a = _RdsDsn1Psn0Af4a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 14),
    _RdsDsn1Psn0Af4a_Type()
)
rdsDsn1Psn0Af4a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af4a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af4a.setUnits("Hz")
_RdsDsn1Psn0Af4b_Type = DisplayString
_RdsDsn1Psn0Af4b_Object = MibScalar
rdsDsn1Psn0Af4b = _RdsDsn1Psn0Af4b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 15),
    _RdsDsn1Psn0Af4b_Type()
)
rdsDsn1Psn0Af4b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af4b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af4b.setUnits("Hz")
_RdsDsn1Psn0Af5a_Type = DisplayString
_RdsDsn1Psn0Af5a_Object = MibScalar
rdsDsn1Psn0Af5a = _RdsDsn1Psn0Af5a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 16),
    _RdsDsn1Psn0Af5a_Type()
)
rdsDsn1Psn0Af5a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af5a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af5a.setUnits("Hz")
_RdsDsn1Psn0Af5b_Type = DisplayString
_RdsDsn1Psn0Af5b_Object = MibScalar
rdsDsn1Psn0Af5b = _RdsDsn1Psn0Af5b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 17),
    _RdsDsn1Psn0Af5b_Type()
)
rdsDsn1Psn0Af5b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af5b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af5b.setUnits("Hz")
_RdsDsn1Psn0Af6a_Type = DisplayString
_RdsDsn1Psn0Af6a_Object = MibScalar
rdsDsn1Psn0Af6a = _RdsDsn1Psn0Af6a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 18),
    _RdsDsn1Psn0Af6a_Type()
)
rdsDsn1Psn0Af6a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af6a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af6a.setUnits("Hz")
_RdsDsn1Psn0Af6b_Type = DisplayString
_RdsDsn1Psn0Af6b_Object = MibScalar
rdsDsn1Psn0Af6b = _RdsDsn1Psn0Af6b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 19),
    _RdsDsn1Psn0Af6b_Type()
)
rdsDsn1Psn0Af6b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af6b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af6b.setUnits("Hz")
_RdsDsn1Psn0Af7a_Type = DisplayString
_RdsDsn1Psn0Af7a_Object = MibScalar
rdsDsn1Psn0Af7a = _RdsDsn1Psn0Af7a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 20),
    _RdsDsn1Psn0Af7a_Type()
)
rdsDsn1Psn0Af7a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af7a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af7a.setUnits("Hz")
_RdsDsn1Psn0Af7b_Type = DisplayString
_RdsDsn1Psn0Af7b_Object = MibScalar
rdsDsn1Psn0Af7b = _RdsDsn1Psn0Af7b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 21),
    _RdsDsn1Psn0Af7b_Type()
)
rdsDsn1Psn0Af7b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af7b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af7b.setUnits("Hz")
_RdsDsn1Psn0Af8a_Type = DisplayString
_RdsDsn1Psn0Af8a_Object = MibScalar
rdsDsn1Psn0Af8a = _RdsDsn1Psn0Af8a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 22),
    _RdsDsn1Psn0Af8a_Type()
)
rdsDsn1Psn0Af8a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af8a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af8a.setUnits("Hz")
_RdsDsn1Psn0Af8b_Type = DisplayString
_RdsDsn1Psn0Af8b_Object = MibScalar
rdsDsn1Psn0Af8b = _RdsDsn1Psn0Af8b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 23),
    _RdsDsn1Psn0Af8b_Type()
)
rdsDsn1Psn0Af8b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af8b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af8b.setUnits("Hz")
_RdsDsn1Psn0Af9a_Type = DisplayString
_RdsDsn1Psn0Af9a_Object = MibScalar
rdsDsn1Psn0Af9a = _RdsDsn1Psn0Af9a_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 24),
    _RdsDsn1Psn0Af9a_Type()
)
rdsDsn1Psn0Af9a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af9a.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af9a.setUnits("Hz")
_RdsDsn1Psn0Af9b_Type = DisplayString
_RdsDsn1Psn0Af9b_Object = MibScalar
rdsDsn1Psn0Af9b = _RdsDsn1Psn0Af9b_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 25),
    _RdsDsn1Psn0Af9b_Type()
)
rdsDsn1Psn0Af9b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af9b.setStatus("current")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Af9b.setUnits("Hz")
_RdsDsn1Psn0AfCount_Type = DisplayString
_RdsDsn1Psn0AfCount_Object = MibScalar
rdsDsn1Psn0AfCount = _RdsDsn1Psn0AfCount_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 1, 26),
    _RdsDsn1Psn0AfCount_Type()
)
rdsDsn1Psn0AfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0AfCount.setStatus("current")
_RdsDsn1Psn0ArtificialHead_Type = DisplayString
_RdsDsn1Psn0ArtificialHead_Object = MibScalar
rdsDsn1Psn0ArtificialHead = _RdsDsn1Psn0ArtificialHead_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 2),
    _RdsDsn1Psn0ArtificialHead_Type()
)
rdsDsn1Psn0ArtificialHead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0ArtificialHead.setStatus("current")
_RdsDsn1Psn0Compressed_Type = DisplayString
_RdsDsn1Psn0Compressed_Object = MibScalar
rdsDsn1Psn0Compressed = _RdsDsn1Psn0Compressed_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 3),
    _RdsDsn1Psn0Compressed_Type()
)
rdsDsn1Psn0Compressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Compressed.setStatus("current")
_RdsDsn1Psn0Dynamicpty_Type = DisplayString
_RdsDsn1Psn0Dynamicpty_Object = MibScalar
rdsDsn1Psn0Dynamicpty = _RdsDsn1Psn0Dynamicpty_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 4),
    _RdsDsn1Psn0Dynamicpty_Type()
)
rdsDsn1Psn0Dynamicpty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Dynamicpty.setStatus("current")
_RdsDsn1Psn0Ms_Type = DisplayString
_RdsDsn1Psn0Ms_Object = MibScalar
rdsDsn1Psn0Ms = _RdsDsn1Psn0Ms_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 5),
    _RdsDsn1Psn0Ms_Type()
)
rdsDsn1Psn0Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Ms.setStatus("current")
_RdsDsn1Psn0Pi_Type = DisplayString
_RdsDsn1Psn0Pi_Object = MibScalar
rdsDsn1Psn0Pi = _RdsDsn1Psn0Pi_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 6),
    _RdsDsn1Psn0Pi_Type()
)
rdsDsn1Psn0Pi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Pi.setStatus("current")
_RdsDsn1Psn0Ps_Type = DisplayString
_RdsDsn1Psn0Ps_Object = MibScalar
rdsDsn1Psn0Ps = _RdsDsn1Psn0Ps_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 7),
    _RdsDsn1Psn0Ps_Type()
)
rdsDsn1Psn0Ps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Ps.setStatus("current")
_RdsDsn1Psn0Pty_Type = DisplayString
_RdsDsn1Psn0Pty_Object = MibScalar
rdsDsn1Psn0Pty = _RdsDsn1Psn0Pty_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 8),
    _RdsDsn1Psn0Pty_Type()
)
rdsDsn1Psn0Pty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Pty.setStatus("current")
_RdsDsn1Psn0PtyRbds_Type = DisplayString
_RdsDsn1Psn0PtyRbds_Object = MibScalar
rdsDsn1Psn0PtyRbds = _RdsDsn1Psn0PtyRbds_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 9),
    _RdsDsn1Psn0PtyRbds_Type()
)
rdsDsn1Psn0PtyRbds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0PtyRbds.setStatus("current")
_RdsDsn1Psn0Ptyn_Type = DisplayString
_RdsDsn1Psn0Ptyn_Object = MibScalar
rdsDsn1Psn0Ptyn = _RdsDsn1Psn0Ptyn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 10),
    _RdsDsn1Psn0Ptyn_Type()
)
rdsDsn1Psn0Ptyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Ptyn.setStatus("current")
_RdsDsn1Psn0Rt_Type = DisplayString
_RdsDsn1Psn0Rt_Object = MibScalar
rdsDsn1Psn0Rt = _RdsDsn1Psn0Rt_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 11),
    _RdsDsn1Psn0Rt_Type()
)
rdsDsn1Psn0Rt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Rt.setStatus("current")
_RdsDsn1Psn0Stereo_Type = DisplayString
_RdsDsn1Psn0Stereo_Object = MibScalar
rdsDsn1Psn0Stereo = _RdsDsn1Psn0Stereo_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 12),
    _RdsDsn1Psn0Stereo_Type()
)
rdsDsn1Psn0Stereo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Stereo.setStatus("current")
_RdsDsn1Psn0Ta_Type = DisplayString
_RdsDsn1Psn0Ta_Object = MibScalar
rdsDsn1Psn0Ta = _RdsDsn1Psn0Ta_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 13),
    _RdsDsn1Psn0Ta_Type()
)
rdsDsn1Psn0Ta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Ta.setStatus("current")
_RdsDsn1Psn0Tp_Type = DisplayString
_RdsDsn1Psn0Tp_Object = MibScalar
rdsDsn1Psn0Tp = _RdsDsn1Psn0Tp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 1, 1, 14),
    _RdsDsn1Psn0Tp_Type()
)
rdsDsn1Psn0Tp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsDsn1Psn0Tp.setStatus("current")
_RdsPtyCoding_Type = DisplayString
_RdsPtyCoding_Object = MibScalar
rdsPtyCoding = _RdsPtyCoding_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 9, 2),
    _RdsPtyCoding_Type()
)
rdsPtyCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsPtyCoding.setStatus("current")
_Sfn_ObjectIdentity = ObjectIdentity
sfn = _Sfn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 10)
)
_SfnExtRefClk_Type = DisplayString
_SfnExtRefClk_Object = MibScalar
sfnExtRefClk = _SfnExtRefClk_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 10, 1),
    _SfnExtRefClk_Type()
)
sfnExtRefClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfnExtRefClk.setStatus("current")
_SfnGpsSync_Type = DisplayString
_SfnGpsSync_Object = MibScalar
sfnGpsSync = _SfnGpsSync_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 10, 2),
    _SfnGpsSync_Type()
)
sfnGpsSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfnGpsSync.setStatus("current")
_SfnPilotPhase_Type = DisplayString
_SfnPilotPhase_Object = MibScalar
sfnPilotPhase = _SfnPilotPhase_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 10, 3),
    _SfnPilotPhase_Type()
)
sfnPilotPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfnPilotPhase.setStatus("current")
if mibBuilder.loadTexts:
    sfnPilotPhase.setUnits("deg")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 11)
)
_SmtpHost_Type = DisplayString
_SmtpHost_Object = MibScalar
smtpHost = _SmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 11, 1),
    _SmtpHost_Type()
)
smtpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpHost.setStatus("current")
_SmtpPassword_Type = DisplayString
_SmtpPassword_Object = MibScalar
smtpPassword = _SmtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 11, 2),
    _SmtpPassword_Type()
)
smtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPassword.setStatus("current")
_SmtpPort_Type = DisplayString
_SmtpPort_Object = MibScalar
smtpPort = _SmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 11, 3),
    _SmtpPort_Type()
)
smtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPort.setStatus("current")
_SmtpUsername_Type = DisplayString
_SmtpUsername_Object = MibScalar
smtpUsername = _SmtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 11, 4),
    _SmtpUsername_Type()
)
smtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpUsername.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12)
)
_SystemContact_Type = DisplayString
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 1),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")
_SystemDate_Type = DisplayString
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 2),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")
_SystemEthernet_ObjectIdentity = ObjectIdentity
systemEthernet = _SystemEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3)
)
_SystemEthernetDhcp_ObjectIdentity = ObjectIdentity
systemEthernetDhcp = _SystemEthernetDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 1)
)
_SystemEthernetDhcpDns1_Type = IpAddress
_SystemEthernetDhcpDns1_Object = MibScalar
systemEthernetDhcpDns1 = _SystemEthernetDhcpDns1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 1, 1),
    _SystemEthernetDhcpDns1_Type()
)
systemEthernetDhcpDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetDhcpDns1.setStatus("current")
_SystemEthernetDhcpDns2_Type = IpAddress
_SystemEthernetDhcpDns2_Object = MibScalar
systemEthernetDhcpDns2 = _SystemEthernetDhcpDns2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 1, 2),
    _SystemEthernetDhcpDns2_Type()
)
systemEthernetDhcpDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetDhcpDns2.setStatus("current")
_SystemEthernetDhcpGw_Type = IpAddress
_SystemEthernetDhcpGw_Object = MibScalar
systemEthernetDhcpGw = _SystemEthernetDhcpGw_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 1, 3),
    _SystemEthernetDhcpGw_Type()
)
systemEthernetDhcpGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetDhcpGw.setStatus("current")
_SystemEthernetDhcpIp_Type = IpAddress
_SystemEthernetDhcpIp_Object = MibScalar
systemEthernetDhcpIp = _SystemEthernetDhcpIp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 1, 4),
    _SystemEthernetDhcpIp_Type()
)
systemEthernetDhcpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetDhcpIp.setStatus("current")
_SystemEthernetDhcpSm_Type = IpAddress
_SystemEthernetDhcpSm_Object = MibScalar
systemEthernetDhcpSm = _SystemEthernetDhcpSm_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 1, 5),
    _SystemEthernetDhcpSm_Type()
)
systemEthernetDhcpSm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetDhcpSm.setStatus("current")
_SystemEthernetDhcpOn_Type = DisplayString
_SystemEthernetDhcpOn_Object = MibScalar
systemEthernetDhcpOn = _SystemEthernetDhcpOn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 2),
    _SystemEthernetDhcpOn_Type()
)
systemEthernetDhcpOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetDhcpOn.setStatus("current")
_SystemEthernetMac_Type = DisplayString
_SystemEthernetMac_Object = MibScalar
systemEthernetMac = _SystemEthernetMac_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 3),
    _SystemEthernetMac_Type()
)
systemEthernetMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEthernetMac.setStatus("current")
_SystemEthernetStatic_ObjectIdentity = ObjectIdentity
systemEthernetStatic = _SystemEthernetStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 4)
)
_SystemEthernetStaticDns1_Type = IpAddress
_SystemEthernetStaticDns1_Object = MibScalar
systemEthernetStaticDns1 = _SystemEthernetStaticDns1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 4, 1),
    _SystemEthernetStaticDns1_Type()
)
systemEthernetStaticDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetStaticDns1.setStatus("current")
_SystemEthernetStaticDns2_Type = IpAddress
_SystemEthernetStaticDns2_Object = MibScalar
systemEthernetStaticDns2 = _SystemEthernetStaticDns2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 4, 2),
    _SystemEthernetStaticDns2_Type()
)
systemEthernetStaticDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetStaticDns2.setStatus("current")
_SystemEthernetStaticGw_Type = IpAddress
_SystemEthernetStaticGw_Object = MibScalar
systemEthernetStaticGw = _SystemEthernetStaticGw_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 4, 3),
    _SystemEthernetStaticGw_Type()
)
systemEthernetStaticGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetStaticGw.setStatus("current")
_SystemEthernetStaticIp_Type = IpAddress
_SystemEthernetStaticIp_Object = MibScalar
systemEthernetStaticIp = _SystemEthernetStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 4, 4),
    _SystemEthernetStaticIp_Type()
)
systemEthernetStaticIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetStaticIp.setStatus("current")
_SystemEthernetStaticSm_Type = IpAddress
_SystemEthernetStaticSm_Object = MibScalar
systemEthernetStaticSm = _SystemEthernetStaticSm_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 3, 4, 5),
    _SystemEthernetStaticSm_Type()
)
systemEthernetStaticSm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEthernetStaticSm.setStatus("current")
_SystemFactoryReset_Type = DisplayString
_SystemFactoryReset_Object = MibScalar
systemFactoryReset = _SystemFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 4),
    _SystemFactoryReset_Type()
)
systemFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFactoryReset.setStatus("current")
_SystemHttpd_ObjectIdentity = ObjectIdentity
systemHttpd = _SystemHttpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 5)
)
_SystemHttpdActive_Type = DisplayString
_SystemHttpdActive_Object = MibScalar
systemHttpdActive = _SystemHttpdActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 5, 1),
    _SystemHttpdActive_Type()
)
systemHttpdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHttpdActive.setStatus("current")
_SystemHttpdPort_Type = DisplayString
_SystemHttpdPort_Object = MibScalar
systemHttpdPort = _SystemHttpdPort_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 5, 2),
    _SystemHttpdPort_Type()
)
systemHttpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHttpdPort.setStatus("current")
_SystemHttpdRemoteControlMessage_Type = DisplayString
_SystemHttpdRemoteControlMessage_Object = MibScalar
systemHttpdRemoteControlMessage = _SystemHttpdRemoteControlMessage_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 5, 3),
    _SystemHttpdRemoteControlMessage_Type()
)
systemHttpdRemoteControlMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHttpdRemoteControlMessage.setStatus("current")
_SystemLocation_Type = DisplayString
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 6),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")
_SystemLogging_ObjectIdentity = ObjectIdentity
systemLogging = _SystemLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7)
)
_SystemLoggingFile_ObjectIdentity = ObjectIdentity
systemLoggingFile = _SystemLoggingFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 1)
)
_SystemLoggingFileActive_Type = DisplayString
_SystemLoggingFileActive_Object = MibScalar
systemLoggingFileActive = _SystemLoggingFileActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 1, 1),
    _SystemLoggingFileActive_Type()
)
systemLoggingFileActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingFileActive.setStatus("current")
_SystemLoggingRs232_ObjectIdentity = ObjectIdentity
systemLoggingRs232 = _SystemLoggingRs232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 2)
)
_SystemLoggingRs232Active_Type = DisplayString
_SystemLoggingRs232Active_Object = MibScalar
systemLoggingRs232Active = _SystemLoggingRs232Active_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 2, 1),
    _SystemLoggingRs232Active_Type()
)
systemLoggingRs232Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingRs232Active.setStatus("current")
_SystemLoggingUdp_ObjectIdentity = ObjectIdentity
systemLoggingUdp = _SystemLoggingUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 3)
)
_SystemLoggingUdpActive_Type = DisplayString
_SystemLoggingUdpActive_Object = MibScalar
systemLoggingUdpActive = _SystemLoggingUdpActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 3, 1),
    _SystemLoggingUdpActive_Type()
)
systemLoggingUdpActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingUdpActive.setStatus("current")
_SystemLoggingUdpIp_Type = IpAddress
_SystemLoggingUdpIp_Object = MibScalar
systemLoggingUdpIp = _SystemLoggingUdpIp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 3, 2),
    _SystemLoggingUdpIp_Type()
)
systemLoggingUdpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingUdpIp.setStatus("current")
_SystemLoggingUdpPort_Type = DisplayString
_SystemLoggingUdpPort_Object = MibScalar
systemLoggingUdpPort = _SystemLoggingUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 7, 3, 3),
    _SystemLoggingUdpPort_Type()
)
systemLoggingUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoggingUdpPort.setStatus("current")
_SystemPassword_ObjectIdentity = ObjectIdentity
systemPassword = _SystemPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 8)
)
_SystemPasswordAdmin_Type = DisplayString
_SystemPasswordAdmin_Object = MibScalar
systemPasswordAdmin = _SystemPasswordAdmin_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 8, 1),
    _SystemPasswordAdmin_Type()
)
systemPasswordAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPasswordAdmin.setStatus("current")
_SystemProduct_ObjectIdentity = ObjectIdentity
systemProduct = _SystemProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 9)
)
_SystemProductBorn_Type = DisplayString
_SystemProductBorn_Object = MibScalar
systemProductBorn = _SystemProductBorn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 9, 1),
    _SystemProductBorn_Type()
)
systemProductBorn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProductBorn.setStatus("current")
_SystemProductId_Type = DisplayString
_SystemProductId_Object = MibScalar
systemProductId = _SystemProductId_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 9, 2),
    _SystemProductId_Type()
)
systemProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProductId.setStatus("current")
_SystemReboot_Type = DisplayString
_SystemReboot_Object = MibScalar
systemReboot = _SystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 10),
    _SystemReboot_Type()
)
systemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReboot.setStatus("current")
_SystemRs232d_ObjectIdentity = ObjectIdentity
systemRs232d = _SystemRs232d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 11)
)
_SystemRs232dActive_Type = DisplayString
_SystemRs232dActive_Object = MibScalar
systemRs232dActive = _SystemRs232dActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 11, 1),
    _SystemRs232dActive_Type()
)
systemRs232dActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRs232dActive.setStatus("current")
_SystemRs232dBaud_Type = DisplayString
_SystemRs232dBaud_Object = MibScalar
systemRs232dBaud = _SystemRs232dBaud_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 11, 2),
    _SystemRs232dBaud_Type()
)
systemRs232dBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRs232dBaud.setStatus("current")
_SystemScreen_ObjectIdentity = ObjectIdentity
systemScreen = _SystemScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 12)
)
_SystemScreenLock_ObjectIdentity = ObjectIdentity
systemScreenLock = _SystemScreenLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 12, 1)
)
_SystemScreenLockCode_Type = DisplayString
_SystemScreenLockCode_Object = MibScalar
systemScreenLockCode = _SystemScreenLockCode_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 12, 1, 1),
    _SystemScreenLockCode_Type()
)
systemScreenLockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScreenLockCode.setStatus("current")
_SystemScreenLockEnabled_Type = DisplayString
_SystemScreenLockEnabled_Object = MibScalar
systemScreenLockEnabled = _SystemScreenLockEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 12, 1, 2),
    _SystemScreenLockEnabled_Type()
)
systemScreenLockEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScreenLockEnabled.setStatus("current")
_SystemScreenScreensaverType_Type = DisplayString
_SystemScreenScreensaverType_Object = MibScalar
systemScreenScreensaverType = _SystemScreenScreensaverType_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 12, 2),
    _SystemScreenScreensaverType_Type()
)
systemScreenScreensaverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScreenScreensaverType.setStatus("current")
_SystemScreenTimeout_Type = DisplayString
_SystemScreenTimeout_Object = MibScalar
systemScreenTimeout = _SystemScreenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 12, 3),
    _SystemScreenTimeout_Type()
)
systemScreenTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScreenTimeout.setStatus("current")
_SystemSerialNumber_Type = DisplayString
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 13),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")
_SystemSnmpd_ObjectIdentity = ObjectIdentity
systemSnmpd = _SystemSnmpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14)
)
_SystemSnmpdActive_Type = DisplayString
_SystemSnmpdActive_Object = MibScalar
systemSnmpdActive = _SystemSnmpdActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 1),
    _SystemSnmpdActive_Type()
)
systemSnmpdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdActive.setStatus("current")
_SystemSnmpdCommunity_Type = DisplayString
_SystemSnmpdCommunity_Object = MibScalar
systemSnmpdCommunity = _SystemSnmpdCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 2),
    _SystemSnmpdCommunity_Type()
)
systemSnmpdCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdCommunity.setStatus("current")
_SystemSnmpdDescription_Type = DisplayString
_SystemSnmpdDescription_Object = MibScalar
systemSnmpdDescription = _SystemSnmpdDescription_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 3),
    _SystemSnmpdDescription_Type()
)
systemSnmpdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdDescription.setStatus("current")
_SystemSnmpdName_Type = DisplayString
_SystemSnmpdName_Object = MibScalar
systemSnmpdName = _SystemSnmpdName_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 4),
    _SystemSnmpdName_Type()
)
systemSnmpdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdName.setStatus("current")
_SystemSnmpdObjectId_Type = DisplayString
_SystemSnmpdObjectId_Object = MibScalar
systemSnmpdObjectId = _SystemSnmpdObjectId_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 5),
    _SystemSnmpdObjectId_Type()
)
systemSnmpdObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSnmpdObjectId.setStatus("current")
_SystemSnmpdPort_Type = DisplayString
_SystemSnmpdPort_Object = MibScalar
systemSnmpdPort = _SystemSnmpdPort_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 6),
    _SystemSnmpdPort_Type()
)
systemSnmpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdPort.setStatus("current")
_SystemSnmpdReadOnly_Type = DisplayString
_SystemSnmpdReadOnly_Object = MibScalar
systemSnmpdReadOnly = _SystemSnmpdReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 7),
    _SystemSnmpdReadOnly_Type()
)
systemSnmpdReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdReadOnly.setStatus("current")
_SystemSnmpdTrap_ObjectIdentity = ObjectIdentity
systemSnmpdTrap = _SystemSnmpdTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8)
)
_SystemSnmpdTrapDst1_ObjectIdentity = ObjectIdentity
systemSnmpdTrapDst1 = _SystemSnmpdTrapDst1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 1)
)
_SystemSnmpdTrapDst1Ip_Type = IpAddress
_SystemSnmpdTrapDst1Ip_Object = MibScalar
systemSnmpdTrapDst1Ip = _SystemSnmpdTrapDst1Ip_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 1, 1),
    _SystemSnmpdTrapDst1Ip_Type()
)
systemSnmpdTrapDst1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdTrapDst1Ip.setStatus("current")
_SystemSnmpdTrapDst1Port_Type = DisplayString
_SystemSnmpdTrapDst1Port_Object = MibScalar
systemSnmpdTrapDst1Port = _SystemSnmpdTrapDst1Port_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 1, 2),
    _SystemSnmpdTrapDst1Port_Type()
)
systemSnmpdTrapDst1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdTrapDst1Port.setStatus("current")
_SystemSnmpdTrapDst2_ObjectIdentity = ObjectIdentity
systemSnmpdTrapDst2 = _SystemSnmpdTrapDst2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 2)
)
_SystemSnmpdTrapDst2Ip_Type = IpAddress
_SystemSnmpdTrapDst2Ip_Object = MibScalar
systemSnmpdTrapDst2Ip = _SystemSnmpdTrapDst2Ip_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 2, 1),
    _SystemSnmpdTrapDst2Ip_Type()
)
systemSnmpdTrapDst2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdTrapDst2Ip.setStatus("current")
_SystemSnmpdTrapDst2Port_Type = DisplayString
_SystemSnmpdTrapDst2Port_Object = MibScalar
systemSnmpdTrapDst2Port = _SystemSnmpdTrapDst2Port_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 2, 2),
    _SystemSnmpdTrapDst2Port_Type()
)
systemSnmpdTrapDst2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdTrapDst2Port.setStatus("current")
_SystemSnmpdTrapTest_ObjectIdentity = ObjectIdentity
systemSnmpdTrapTest = _SystemSnmpdTrapTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 3)
)
_SystemSnmpdTrapTestSend_Type = DisplayString
_SystemSnmpdTrapTestSend_Object = MibScalar
systemSnmpdTrapTestSend = _SystemSnmpdTrapTestSend_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 14, 8, 3, 1),
    _SystemSnmpdTrapTestSend_Type()
)
systemSnmpdTrapTestSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSnmpdTrapTestSend.setStatus("current")
_SystemSoftware_ObjectIdentity = ObjectIdentity
systemSoftware = _SystemSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 15)
)
_SystemSoftwareVersion_Type = DisplayString
_SystemSoftwareVersion_Object = MibScalar
systemSoftwareVersion = _SystemSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 15, 1),
    _SystemSoftwareVersion_Type()
)
systemSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSoftwareVersion.setStatus("current")
_SystemTelnetd_ObjectIdentity = ObjectIdentity
systemTelnetd = _SystemTelnetd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 16)
)
_SystemTelnetdActive_Type = DisplayString
_SystemTelnetdActive_Object = MibScalar
systemTelnetdActive = _SystemTelnetdActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 16, 1),
    _SystemTelnetdActive_Type()
)
systemTelnetdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTelnetdActive.setStatus("current")
_SystemTelnetdPort_Type = DisplayString
_SystemTelnetdPort_Object = MibScalar
systemTelnetdPort = _SystemTelnetdPort_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 16, 2),
    _SystemTelnetdPort_Type()
)
systemTelnetdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTelnetdPort.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 17),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemUptime_Type = DisplayString
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 18),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemUsername_ObjectIdentity = ObjectIdentity
systemUsername = _SystemUsername_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 19)
)
_SystemUsernameAdmin_Type = DisplayString
_SystemUsernameAdmin_Object = MibScalar
systemUsernameAdmin = _SystemUsernameAdmin_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 12, 19, 1),
    _SystemUsernameAdmin_Type()
)
systemUsernameAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUsernameAdmin.setStatus("current")
_Transmitter_ObjectIdentity = ObjectIdentity
transmitter = _Transmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13)
)
_TransmitterFrequency_Type = DisplayString
_TransmitterFrequency_Object = MibScalar
transmitterFrequency = _TransmitterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 1),
    _TransmitterFrequency_Type()
)
transmitterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    transmitterFrequency.setUnits("Hz")
_TransmitterFsk_ObjectIdentity = ObjectIdentity
transmitterFsk = _TransmitterFsk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 2)
)
_TransmitterFskId_Type = DisplayString
_TransmitterFskId_Object = MibScalar
transmitterFskId = _TransmitterFskId_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 2, 1),
    _TransmitterFskId_Type()
)
transmitterFskId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterFskId.setStatus("current")
_TransmitterFskInterval_Type = DisplayString
_TransmitterFskInterval_Object = MibScalar
transmitterFskInterval = _TransmitterFskInterval_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 2, 2),
    _TransmitterFskInterval_Type()
)
transmitterFskInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterFskInterval.setStatus("current")
_TransmitterRfMute_ObjectIdentity = ObjectIdentity
transmitterRfMute = _TransmitterRfMute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 3)
)
_TransmitterRfMuteManualEnable_Type = DisplayString
_TransmitterRfMuteManualEnable_Object = MibScalar
transmitterRfMuteManualEnable = _TransmitterRfMuteManualEnable_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 3, 1),
    _TransmitterRfMuteManualEnable_Type()
)
transmitterRfMuteManualEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterRfMuteManualEnable.setStatus("current")
_TransmitterRfMuteTimeout_Type = DisplayString
_TransmitterRfMuteTimeout_Object = MibScalar
transmitterRfMuteTimeout = _TransmitterRfMuteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 3, 2),
    _TransmitterRfMuteTimeout_Type()
)
transmitterRfMuteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterRfMuteTimeout.setStatus("current")
_TransmitterSetPower_Type = DisplayString
_TransmitterSetPower_Object = MibScalar
transmitterSetPower = _TransmitterSetPower_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 13, 4),
    _TransmitterSetPower_Type()
)
transmitterSetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterSetPower.setStatus("current")
if mibBuilder.loadTexts:
    transmitterSetPower.setUnits("W")
_Trigger1_ObjectIdentity = ObjectIdentity
trigger1 = _Trigger1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14)
)
_Trigger1Action_Type = DisplayString
_Trigger1Action_Object = MibScalar
trigger1Action = _Trigger1Action_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 1),
    _Trigger1Action_Type()
)
trigger1Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger1Action.setStatus("current")
_Trigger1Active_Type = DisplayString
_Trigger1Active_Object = MibScalar
trigger1Active = _Trigger1Active_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 2),
    _Trigger1Active_Type()
)
trigger1Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger1Active.setStatus("current")
_Trigger1Email_ObjectIdentity = ObjectIdentity
trigger1Email = _Trigger1Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 3)
)
_Trigger1EmailActive_Type = DisplayString
_Trigger1EmailActive_Object = MibScalar
trigger1EmailActive = _Trigger1EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 3, 1),
    _Trigger1EmailActive_Type()
)
trigger1EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger1EmailActive.setStatus("current")
_Trigger1Message_ObjectIdentity = ObjectIdentity
trigger1Message = _Trigger1Message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 4)
)
_Trigger1MessageOn_Type = DisplayString
_Trigger1MessageOn_Object = MibScalar
trigger1MessageOn = _Trigger1MessageOn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 4, 1),
    _Trigger1MessageOn_Type()
)
trigger1MessageOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger1MessageOn.setStatus("current")
_Trigger1Trap_ObjectIdentity = ObjectIdentity
trigger1Trap = _Trigger1Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 5)
)
_Trigger1TrapActive_Type = DisplayString
_Trigger1TrapActive_Object = MibScalar
trigger1TrapActive = _Trigger1TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 14, 5, 1),
    _Trigger1TrapActive_Type()
)
trigger1TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger1TrapActive.setStatus("current")
_Trigger2_ObjectIdentity = ObjectIdentity
trigger2 = _Trigger2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15)
)
_Trigger2Action_Type = DisplayString
_Trigger2Action_Object = MibScalar
trigger2Action = _Trigger2Action_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 1),
    _Trigger2Action_Type()
)
trigger2Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger2Action.setStatus("current")
_Trigger2Active_Type = DisplayString
_Trigger2Active_Object = MibScalar
trigger2Active = _Trigger2Active_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 2),
    _Trigger2Active_Type()
)
trigger2Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger2Active.setStatus("current")
_Trigger2Email_ObjectIdentity = ObjectIdentity
trigger2Email = _Trigger2Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 3)
)
_Trigger2EmailActive_Type = DisplayString
_Trigger2EmailActive_Object = MibScalar
trigger2EmailActive = _Trigger2EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 3, 1),
    _Trigger2EmailActive_Type()
)
trigger2EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger2EmailActive.setStatus("current")
_Trigger2Message_ObjectIdentity = ObjectIdentity
trigger2Message = _Trigger2Message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 4)
)
_Trigger2MessageOn_Type = DisplayString
_Trigger2MessageOn_Object = MibScalar
trigger2MessageOn = _Trigger2MessageOn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 4, 1),
    _Trigger2MessageOn_Type()
)
trigger2MessageOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger2MessageOn.setStatus("current")
_Trigger2Trap_ObjectIdentity = ObjectIdentity
trigger2Trap = _Trigger2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 5)
)
_Trigger2TrapActive_Type = DisplayString
_Trigger2TrapActive_Object = MibScalar
trigger2TrapActive = _Trigger2TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 15, 5, 1),
    _Trigger2TrapActive_Type()
)
trigger2TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger2TrapActive.setStatus("current")
_Trigger3_ObjectIdentity = ObjectIdentity
trigger3 = _Trigger3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16)
)
_Trigger3Action_Type = DisplayString
_Trigger3Action_Object = MibScalar
trigger3Action = _Trigger3Action_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 1),
    _Trigger3Action_Type()
)
trigger3Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger3Action.setStatus("current")
_Trigger3Active_Type = DisplayString
_Trigger3Active_Object = MibScalar
trigger3Active = _Trigger3Active_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 2),
    _Trigger3Active_Type()
)
trigger3Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger3Active.setStatus("current")
_Trigger3Email_ObjectIdentity = ObjectIdentity
trigger3Email = _Trigger3Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 3)
)
_Trigger3EmailActive_Type = DisplayString
_Trigger3EmailActive_Object = MibScalar
trigger3EmailActive = _Trigger3EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 3, 1),
    _Trigger3EmailActive_Type()
)
trigger3EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger3EmailActive.setStatus("current")
_Trigger3Message_ObjectIdentity = ObjectIdentity
trigger3Message = _Trigger3Message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 4)
)
_Trigger3MessageOn_Type = DisplayString
_Trigger3MessageOn_Object = MibScalar
trigger3MessageOn = _Trigger3MessageOn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 4, 1),
    _Trigger3MessageOn_Type()
)
trigger3MessageOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger3MessageOn.setStatus("current")
_Trigger3Trap_ObjectIdentity = ObjectIdentity
trigger3Trap = _Trigger3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 5)
)
_Trigger3TrapActive_Type = DisplayString
_Trigger3TrapActive_Object = MibScalar
trigger3TrapActive = _Trigger3TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 16, 5, 1),
    _Trigger3TrapActive_Type()
)
trigger3TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger3TrapActive.setStatus("current")
_Trigger4_ObjectIdentity = ObjectIdentity
trigger4 = _Trigger4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17)
)
_Trigger4Action_Type = DisplayString
_Trigger4Action_Object = MibScalar
trigger4Action = _Trigger4Action_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 1),
    _Trigger4Action_Type()
)
trigger4Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger4Action.setStatus("current")
_Trigger4Active_Type = DisplayString
_Trigger4Active_Object = MibScalar
trigger4Active = _Trigger4Active_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 2),
    _Trigger4Active_Type()
)
trigger4Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger4Active.setStatus("current")
_Trigger4Email_ObjectIdentity = ObjectIdentity
trigger4Email = _Trigger4Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 3)
)
_Trigger4EmailActive_Type = DisplayString
_Trigger4EmailActive_Object = MibScalar
trigger4EmailActive = _Trigger4EmailActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 3, 1),
    _Trigger4EmailActive_Type()
)
trigger4EmailActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger4EmailActive.setStatus("current")
_Trigger4Message_ObjectIdentity = ObjectIdentity
trigger4Message = _Trigger4Message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 4)
)
_Trigger4MessageOn_Type = DisplayString
_Trigger4MessageOn_Object = MibScalar
trigger4MessageOn = _Trigger4MessageOn_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 4, 1),
    _Trigger4MessageOn_Type()
)
trigger4MessageOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger4MessageOn.setStatus("current")
_Trigger4Trap_ObjectIdentity = ObjectIdentity
trigger4Trap = _Trigger4Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 5)
)
_Trigger4TrapActive_Type = DisplayString
_Trigger4TrapActive_Object = MibScalar
trigger4TrapActive = _Trigger4TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 17, 5, 1),
    _Trigger4TrapActive_Type()
)
trigger4TrapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trigger4TrapActive.setStatus("current")
_Triggers_ObjectIdentity = ObjectIdentity
triggers = _Triggers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 18)
)
_TriggersRfmutestyle_Type = DisplayString
_TriggersRfmutestyle_Object = MibScalar
triggersRfmutestyle = _TriggersRfmutestyle_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 18, 1),
    _TriggersRfmutestyle_Type()
)
triggersRfmutestyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triggersRfmutestyle.setStatus("current")
_Meters_ObjectIdentity = ObjectIdentity
meters = _Meters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19)
)
_MetersAcrfeff_Type = DisplayString
_MetersAcrfeff_Object = MibScalar
metersAcrfeff = _MetersAcrfeff_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 1),
    _MetersAcrfeff_Type()
)
metersAcrfeff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersAcrfeff.setStatus("current")
_MetersAgc1_Type = DisplayString
_MetersAgc1_Object = MibScalar
metersAgc1 = _MetersAgc1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 2),
    _MetersAgc1_Type()
)
metersAgc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersAgc1.setStatus("current")
_MetersAgc2_Type = DisplayString
_MetersAgc2_Object = MibScalar
metersAgc2 = _MetersAgc2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 3),
    _MetersAgc2_Type()
)
metersAgc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersAgc2.setStatus("current")
_MetersAgc3_Type = DisplayString
_MetersAgc3_Object = MibScalar
metersAgc3 = _MetersAgc3_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 4),
    _MetersAgc3_Type()
)
metersAgc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersAgc3.setStatus("current")
_MetersAgc4_Type = DisplayString
_MetersAgc4_Object = MibScalar
metersAgc4 = _MetersAgc4_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 5),
    _MetersAgc4_Type()
)
metersAgc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersAgc4.setStatus("current")
_MetersFallback_Type = DisplayString
_MetersFallback_Object = MibScalar
metersFallback = _MetersFallback_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 6),
    _MetersFallback_Type()
)
metersFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersFallback.setStatus("current")
_MetersFanspeed_Type = DisplayString
_MetersFanspeed_Object = MibScalar
metersFanspeed = _MetersFanspeed_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 7),
    _MetersFanspeed_Type()
)
metersFanspeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersFanspeed.setStatus("current")
_MetersLim1_Type = DisplayString
_MetersLim1_Object = MibScalar
metersLim1 = _MetersLim1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 8),
    _MetersLim1_Type()
)
metersLim1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersLim1.setStatus("current")
_MetersLim2_Type = DisplayString
_MetersLim2_Object = MibScalar
metersLim2 = _MetersLim2_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 9),
    _MetersLim2_Type()
)
metersLim2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersLim2.setStatus("current")
_MetersLim3_Type = DisplayString
_MetersLim3_Object = MibScalar
metersLim3 = _MetersLim3_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 10),
    _MetersLim3_Type()
)
metersLim3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersLim3.setStatus("current")
_MetersLim4_Type = DisplayString
_MetersLim4_Object = MibScalar
metersLim4 = _MetersLim4_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 11),
    _MetersLim4_Type()
)
metersLim4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersLim4.setStatus("current")
_MetersMainsv_Type = DisplayString
_MetersMainsv_Object = MibScalar
metersMainsv = _MetersMainsv_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 12),
    _MetersMainsv_Type()
)
metersMainsv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersMainsv.setStatus("current")
_MetersPeakDeviation_Type = DisplayString
_MetersPeakDeviation_Object = MibScalar
metersPeakDeviation = _MetersPeakDeviation_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 13),
    _MetersPeakDeviation_Type()
)
metersPeakDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersPeakDeviation.setStatus("current")
_MetersPsu1temp1_Type = DisplayString
_MetersPsu1temp1_Object = MibScalar
metersPsu1temp1 = _MetersPsu1temp1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 14),
    _MetersPsu1temp1_Type()
)
metersPsu1temp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersPsu1temp1.setStatus("current")
_MetersPsu2temp1_Type = DisplayString
_MetersPsu2temp1_Object = MibScalar
metersPsu2temp1 = _MetersPsu2temp1_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 15),
    _MetersPsu2temp1_Type()
)
metersPsu2temp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersPsu2temp1.setStatus("current")
_MetersPsucurrent_Type = DisplayString
_MetersPsucurrent_Object = MibScalar
metersPsucurrent = _MetersPsucurrent_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 16),
    _MetersPsucurrent_Type()
)
metersPsucurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersPsucurrent.setStatus("current")
_MetersPsuvoltage_Type = DisplayString
_MetersPsuvoltage_Object = MibScalar
metersPsuvoltage = _MetersPsuvoltage_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 17),
    _MetersPsuvoltage_Type()
)
metersPsuvoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersPsuvoltage.setStatus("current")
_MetersTxInputL_Type = DisplayString
_MetersTxInputL_Object = MibScalar
metersTxInputL = _MetersTxInputL_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 18),
    _MetersTxInputL_Type()
)
metersTxInputL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersTxInputL.setStatus("current")
_MetersTxInputR_Type = DisplayString
_MetersTxInputR_Object = MibScalar
metersTxInputR = _MetersTxInputR_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 19),
    _MetersTxInputR_Type()
)
metersTxInputR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersTxInputR.setStatus("current")
_MetersTxOutputL_Type = DisplayString
_MetersTxOutputL_Object = MibScalar
metersTxOutputL = _MetersTxOutputL_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 20),
    _MetersTxOutputL_Type()
)
metersTxOutputL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersTxOutputL.setStatus("current")
_MetersTxOutputMpx_Type = DisplayString
_MetersTxOutputMpx_Object = MibScalar
metersTxOutputMpx = _MetersTxOutputMpx_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 21),
    _MetersTxOutputMpx_Type()
)
metersTxOutputMpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersTxOutputMpx.setStatus("current")
_MetersTxOutputR_Type = DisplayString
_MetersTxOutputR_Object = MibScalar
metersTxOutputR = _MetersTxOutputR_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 22),
    _MetersTxOutputR_Type()
)
metersTxOutputR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersTxOutputR.setStatus("current")
_MetersVSWRLimitActive_Type = DisplayString
_MetersVSWRLimitActive_Object = MibScalar
metersVSWRLimitActive = _MetersVSWRLimitActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 23),
    _MetersVSWRLimitActive_Type()
)
metersVSWRLimitActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersVSWRLimitActive.setStatus("current")
_MetersTempLimitActive_Type = DisplayString
_MetersTempLimitActive_Object = MibScalar
metersTempLimitActive = _MetersTempLimitActive_Object(
    (1, 3, 6, 1, 4, 1, 43768, 137, 19, 24),
    _MetersTempLimitActive_Type()
)
metersTempLimitActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    metersTempLimitActive.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 999999)
)
_ConformanceGroups_ObjectIdentity = ObjectIdentity
conformanceGroups = _ConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 999999, 1)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 137, 999999, 2)
)

# Managed Objects groups

allObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43768, 137, 999999, 1, 1)
)
allObjects.setObjects(
      *(("GATESAIR-FLEXIVA-LX-MIB", "aioRefclkAdj"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1FwdPowerThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1ModulationThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1OffDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1OnDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1Polarity"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1RevPowerThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1Source"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1Telemetrysource"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1TempThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm1Type"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2FwdPowerThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2ModulationThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2OffDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2OnDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2Polarity"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2RevPowerThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2Source"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2Telemetrysource"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2TempThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm2Type"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3FwdPowerThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3ModulationThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3OffDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3OnDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3Polarity"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3RevPowerThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3Source"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3Telemetrysource"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3TempThreshold"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "alarm3Type"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioDelay"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioInput"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioInputsAnalogRef"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioInputsDigitalRef"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioProcessingPreset"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioProcessorOff"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioRightTrim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioStereo"),
        ("GATESAIR-FLEXIVA-LX-MIB", "audioTrim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailCounterToday"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailFrom"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailLimitDaily"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailMethod"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailRecipient"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailTestRecipient"),
        ("GATESAIR-FLEXIVA-LX-MIB", "emailTestSend"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxDigMpxInLevel"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenCompClipper"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenLevel"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenPilotLevel"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenPilotProtection"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenPowerLimit"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenPreemphasis"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenRdsLevel"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxGenSource"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxInput1Level"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxInput1Trim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxInput2Level"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxInput2Trim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxOutput1Level"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxOutput1Source"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxOutput1Trim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxOutput2Level"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxOutput2Source"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxOutput2Trim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "mpxTunerTrim"),
        ("GATESAIR-FLEXIVA-LX-MIB", "powerschedulerEnabled"),
        ("GATESAIR-FLEXIVA-LX-MIB", "powerschedulerFinishtime"),
        ("GATESAIR-FLEXIVA-LX-MIB", "powerschedulerPower"),
        ("GATESAIR-FLEXIVA-LX-MIB", "powerschedulerStarttime"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af10a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af10b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af11a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af11b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af12a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af12b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af13a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af13b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af1b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af2a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af2b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af3a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af3b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af4a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af4b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af5a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af5b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af6a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af6b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af7a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af7b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af8a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af8b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af9a"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Af9b"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0AfCount"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0ArtificialHead"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Compressed"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Dynamicpty"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Ms"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Pi"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Ps"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Pty"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0PtyRbds"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Ptyn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Rt"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Stereo"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Ta"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsDsn1Psn0Tp"),
        ("GATESAIR-FLEXIVA-LX-MIB", "rdsPtyCoding"),
        ("GATESAIR-FLEXIVA-LX-MIB", "sfnExtRefClk"),
        ("GATESAIR-FLEXIVA-LX-MIB", "sfnGpsSync"),
        ("GATESAIR-FLEXIVA-LX-MIB", "sfnPilotPhase"),
        ("GATESAIR-FLEXIVA-LX-MIB", "smtpHost"),
        ("GATESAIR-FLEXIVA-LX-MIB", "smtpPassword"),
        ("GATESAIR-FLEXIVA-LX-MIB", "smtpPort"),
        ("GATESAIR-FLEXIVA-LX-MIB", "smtpUsername"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemContact"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemDate"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetDhcpDns1"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetDhcpDns2"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetDhcpGw"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetDhcpIp"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetDhcpSm"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetDhcpOn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetMac"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetStaticDns1"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetStaticDns2"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetStaticGw"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetStaticIp"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemEthernetStaticSm"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemFactoryReset"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemHttpdActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemHttpdPort"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemHttpdRemoteControlMessage"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemLocation"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemLoggingFileActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemLoggingRs232Active"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemLoggingUdpActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemLoggingUdpIp"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemLoggingUdpPort"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemPasswordAdmin"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemProductBorn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemProductId"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemReboot"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemRs232dActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemRs232dBaud"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemScreenLockCode"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemScreenLockEnabled"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemScreenScreensaverType"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemScreenTimeout"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSerialNumber"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdCommunity"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdDescription"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdName"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdObjectId"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdPort"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdReadOnly"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdTrapDst1Ip"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdTrapDst1Port"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdTrapDst2Ip"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdTrapDst2Port"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSnmpdTrapTestSend"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemSoftwareVersion"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemTelnetdActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemTelnetdPort"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemTime"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemUptime"),
        ("GATESAIR-FLEXIVA-LX-MIB", "systemUsernameAdmin"),
        ("GATESAIR-FLEXIVA-LX-MIB", "transmitterFrequency"),
        ("GATESAIR-FLEXIVA-LX-MIB", "transmitterFskId"),
        ("GATESAIR-FLEXIVA-LX-MIB", "transmitterFskInterval"),
        ("GATESAIR-FLEXIVA-LX-MIB", "transmitterRfMuteManualEnable"),
        ("GATESAIR-FLEXIVA-LX-MIB", "transmitterRfMuteTimeout"),
        ("GATESAIR-FLEXIVA-LX-MIB", "transmitterSetPower"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger1Action"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger1Active"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger1EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger1MessageOn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger1TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger2Action"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger2Active"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger2EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger2MessageOn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger2TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger3Action"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger3Active"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger3EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger3MessageOn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger3TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger4Action"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger4Active"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger4EmailActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger4MessageOn"),
        ("GATESAIR-FLEXIVA-LX-MIB", "trigger4TrapActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "triggersRfmutestyle"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersAcrfeff"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersAgc1"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersAgc2"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersAgc3"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersAgc4"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersFallback"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersFanspeed"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersLim1"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersLim2"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersLim3"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersLim4"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersMainsv"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersPeakDeviation"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersPsu1temp1"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersPsu2temp1"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersPsucurrent"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersPsuvoltage"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersTxInputL"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersTxInputR"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersTxOutputL"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersTxOutputMpx"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersTxOutputR"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersVSWRLimitActive"),
        ("GATESAIR-FLEXIVA-LX-MIB", "metersTempLimitActive"))
)
if mibBuilder.loadTexts:
    allObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43768, 137, 999999, 2, 1)
)
compliance.setObjects(
    ("GATESAIR-FLEXIVA-LX-MIB", "allObjects")
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GATESAIR-FLEXIVA-LX-MIB",
    **{"gates-air": gates_air,
       "lx": lx,
       "aio": aio,
       "aioRefclkAdj": aioRefclkAdj,
       "alarm1": alarm1,
       "alarm1Email": alarm1Email,
       "alarm1EmailActive": alarm1EmailActive,
       "alarm1FwdPowerThreshold": alarm1FwdPowerThreshold,
       "alarm1ModulationThreshold": alarm1ModulationThreshold,
       "alarm1OffDelay": alarm1OffDelay,
       "alarm1OnDelay": alarm1OnDelay,
       "alarm1Polarity": alarm1Polarity,
       "alarm1RevPowerThreshold": alarm1RevPowerThreshold,
       "alarm1Source": alarm1Source,
       "alarm1Telemetrysource": alarm1Telemetrysource,
       "alarm1TempThreshold": alarm1TempThreshold,
       "alarm1Trap": alarm1Trap,
       "alarm1TrapActive": alarm1TrapActive,
       "alarm1Type": alarm1Type,
       "alarm2": alarm2,
       "alarm2Email": alarm2Email,
       "alarm2EmailActive": alarm2EmailActive,
       "alarm2FwdPowerThreshold": alarm2FwdPowerThreshold,
       "alarm2ModulationThreshold": alarm2ModulationThreshold,
       "alarm2OffDelay": alarm2OffDelay,
       "alarm2OnDelay": alarm2OnDelay,
       "alarm2Polarity": alarm2Polarity,
       "alarm2RevPowerThreshold": alarm2RevPowerThreshold,
       "alarm2Source": alarm2Source,
       "alarm2Telemetrysource": alarm2Telemetrysource,
       "alarm2TempThreshold": alarm2TempThreshold,
       "alarm2Trap": alarm2Trap,
       "alarm2TrapActive": alarm2TrapActive,
       "alarm2Type": alarm2Type,
       "alarm3": alarm3,
       "alarm3Email": alarm3Email,
       "alarm3EmailActive": alarm3EmailActive,
       "alarm3FwdPowerThreshold": alarm3FwdPowerThreshold,
       "alarm3ModulationThreshold": alarm3ModulationThreshold,
       "alarm3OffDelay": alarm3OffDelay,
       "alarm3OnDelay": alarm3OnDelay,
       "alarm3Polarity": alarm3Polarity,
       "alarm3RevPowerThreshold": alarm3RevPowerThreshold,
       "alarm3Source": alarm3Source,
       "alarm3Telemetrysource": alarm3Telemetrysource,
       "alarm3TempThreshold": alarm3TempThreshold,
       "alarm3Trap": alarm3Trap,
       "alarm3TrapActive": alarm3TrapActive,
       "alarm3Type": alarm3Type,
       "audio": audio,
       "audioDelay": audioDelay,
       "audioInput": audioInput,
       "audioInputs": audioInputs,
       "audioInputsAnalogRef": audioInputsAnalogRef,
       "audioInputsDigitalRef": audioInputsDigitalRef,
       "audioProcessingPreset": audioProcessingPreset,
       "audioProcessorOff": audioProcessorOff,
       "audioRightTrim": audioRightTrim,
       "audioStereo": audioStereo,
       "audioTrim": audioTrim,
       "email": email,
       "emailCounter": emailCounter,
       "emailCounterToday": emailCounterToday,
       "emailFrom": emailFrom,
       "emailLimit": emailLimit,
       "emailLimitDaily": emailLimitDaily,
       "emailMethod": emailMethod,
       "emailRecipient": emailRecipient,
       "emailTest": emailTest,
       "emailTestRecipient": emailTestRecipient,
       "emailTestSend": emailTestSend,
       "mpx": mpx,
       "mpxDigMpxIn": mpxDigMpxIn,
       "mpxDigMpxInLevel": mpxDigMpxInLevel,
       "mpxGen": mpxGen,
       "mpxGenCompClipper": mpxGenCompClipper,
       "mpxGenLevel": mpxGenLevel,
       "mpxGenPilotLevel": mpxGenPilotLevel,
       "mpxGenPilotProtection": mpxGenPilotProtection,
       "mpxGenPowerLimit": mpxGenPowerLimit,
       "mpxGenPreemphasis": mpxGenPreemphasis,
       "mpxGenRdsLevel": mpxGenRdsLevel,
       "mpxGenSource": mpxGenSource,
       "mpxInput1": mpxInput1,
       "mpxInput1Level": mpxInput1Level,
       "mpxInput1Trim": mpxInput1Trim,
       "mpxInput2": mpxInput2,
       "mpxInput2Level": mpxInput2Level,
       "mpxInput2Trim": mpxInput2Trim,
       "mpxOutput1": mpxOutput1,
       "mpxOutput1Level": mpxOutput1Level,
       "mpxOutput1Source": mpxOutput1Source,
       "mpxOutput1Trim": mpxOutput1Trim,
       "mpxOutput2": mpxOutput2,
       "mpxOutput2Level": mpxOutput2Level,
       "mpxOutput2Source": mpxOutput2Source,
       "mpxOutput2Trim": mpxOutput2Trim,
       "mpxTuner": mpxTuner,
       "mpxTunerTrim": mpxTunerTrim,
       "powerscheduler": powerscheduler,
       "powerschedulerEnabled": powerschedulerEnabled,
       "powerschedulerFinishtime": powerschedulerFinishtime,
       "powerschedulerPower": powerschedulerPower,
       "powerschedulerStarttime": powerschedulerStarttime,
       "rds": rds,
       "rdsDsn1": rdsDsn1,
       "rdsDsn1Psn0": rdsDsn1Psn0,
       "rdsDsn1Psn0Af": rdsDsn1Psn0Af,
       "rdsDsn1Psn0Af10a": rdsDsn1Psn0Af10a,
       "rdsDsn1Psn0Af10b": rdsDsn1Psn0Af10b,
       "rdsDsn1Psn0Af11a": rdsDsn1Psn0Af11a,
       "rdsDsn1Psn0Af11b": rdsDsn1Psn0Af11b,
       "rdsDsn1Psn0Af12a": rdsDsn1Psn0Af12a,
       "rdsDsn1Psn0Af12b": rdsDsn1Psn0Af12b,
       "rdsDsn1Psn0Af13a": rdsDsn1Psn0Af13a,
       "rdsDsn1Psn0Af13b": rdsDsn1Psn0Af13b,
       "rdsDsn1Psn0Af1b": rdsDsn1Psn0Af1b,
       "rdsDsn1Psn0Af2a": rdsDsn1Psn0Af2a,
       "rdsDsn1Psn0Af2b": rdsDsn1Psn0Af2b,
       "rdsDsn1Psn0Af3a": rdsDsn1Psn0Af3a,
       "rdsDsn1Psn0Af3b": rdsDsn1Psn0Af3b,
       "rdsDsn1Psn0Af4a": rdsDsn1Psn0Af4a,
       "rdsDsn1Psn0Af4b": rdsDsn1Psn0Af4b,
       "rdsDsn1Psn0Af5a": rdsDsn1Psn0Af5a,
       "rdsDsn1Psn0Af5b": rdsDsn1Psn0Af5b,
       "rdsDsn1Psn0Af6a": rdsDsn1Psn0Af6a,
       "rdsDsn1Psn0Af6b": rdsDsn1Psn0Af6b,
       "rdsDsn1Psn0Af7a": rdsDsn1Psn0Af7a,
       "rdsDsn1Psn0Af7b": rdsDsn1Psn0Af7b,
       "rdsDsn1Psn0Af8a": rdsDsn1Psn0Af8a,
       "rdsDsn1Psn0Af8b": rdsDsn1Psn0Af8b,
       "rdsDsn1Psn0Af9a": rdsDsn1Psn0Af9a,
       "rdsDsn1Psn0Af9b": rdsDsn1Psn0Af9b,
       "rdsDsn1Psn0AfCount": rdsDsn1Psn0AfCount,
       "rdsDsn1Psn0ArtificialHead": rdsDsn1Psn0ArtificialHead,
       "rdsDsn1Psn0Compressed": rdsDsn1Psn0Compressed,
       "rdsDsn1Psn0Dynamicpty": rdsDsn1Psn0Dynamicpty,
       "rdsDsn1Psn0Ms": rdsDsn1Psn0Ms,
       "rdsDsn1Psn0Pi": rdsDsn1Psn0Pi,
       "rdsDsn1Psn0Ps": rdsDsn1Psn0Ps,
       "rdsDsn1Psn0Pty": rdsDsn1Psn0Pty,
       "rdsDsn1Psn0PtyRbds": rdsDsn1Psn0PtyRbds,
       "rdsDsn1Psn0Ptyn": rdsDsn1Psn0Ptyn,
       "rdsDsn1Psn0Rt": rdsDsn1Psn0Rt,
       "rdsDsn1Psn0Stereo": rdsDsn1Psn0Stereo,
       "rdsDsn1Psn0Ta": rdsDsn1Psn0Ta,
       "rdsDsn1Psn0Tp": rdsDsn1Psn0Tp,
       "rdsPtyCoding": rdsPtyCoding,
       "sfn": sfn,
       "sfnExtRefClk": sfnExtRefClk,
       "sfnGpsSync": sfnGpsSync,
       "sfnPilotPhase": sfnPilotPhase,
       "smtp": smtp,
       "smtpHost": smtpHost,
       "smtpPassword": smtpPassword,
       "smtpPort": smtpPort,
       "smtpUsername": smtpUsername,
       "system": system,
       "systemContact": systemContact,
       "systemDate": systemDate,
       "systemEthernet": systemEthernet,
       "systemEthernetDhcp": systemEthernetDhcp,
       "systemEthernetDhcpDns1": systemEthernetDhcpDns1,
       "systemEthernetDhcpDns2": systemEthernetDhcpDns2,
       "systemEthernetDhcpGw": systemEthernetDhcpGw,
       "systemEthernetDhcpIp": systemEthernetDhcpIp,
       "systemEthernetDhcpSm": systemEthernetDhcpSm,
       "systemEthernetDhcpOn": systemEthernetDhcpOn,
       "systemEthernetMac": systemEthernetMac,
       "systemEthernetStatic": systemEthernetStatic,
       "systemEthernetStaticDns1": systemEthernetStaticDns1,
       "systemEthernetStaticDns2": systemEthernetStaticDns2,
       "systemEthernetStaticGw": systemEthernetStaticGw,
       "systemEthernetStaticIp": systemEthernetStaticIp,
       "systemEthernetStaticSm": systemEthernetStaticSm,
       "systemFactoryReset": systemFactoryReset,
       "systemHttpd": systemHttpd,
       "systemHttpdActive": systemHttpdActive,
       "systemHttpdPort": systemHttpdPort,
       "systemHttpdRemoteControlMessage": systemHttpdRemoteControlMessage,
       "systemLocation": systemLocation,
       "systemLogging": systemLogging,
       "systemLoggingFile": systemLoggingFile,
       "systemLoggingFileActive": systemLoggingFileActive,
       "systemLoggingRs232": systemLoggingRs232,
       "systemLoggingRs232Active": systemLoggingRs232Active,
       "systemLoggingUdp": systemLoggingUdp,
       "systemLoggingUdpActive": systemLoggingUdpActive,
       "systemLoggingUdpIp": systemLoggingUdpIp,
       "systemLoggingUdpPort": systemLoggingUdpPort,
       "systemPassword": systemPassword,
       "systemPasswordAdmin": systemPasswordAdmin,
       "systemProduct": systemProduct,
       "systemProductBorn": systemProductBorn,
       "systemProductId": systemProductId,
       "systemReboot": systemReboot,
       "systemRs232d": systemRs232d,
       "systemRs232dActive": systemRs232dActive,
       "systemRs232dBaud": systemRs232dBaud,
       "systemScreen": systemScreen,
       "systemScreenLock": systemScreenLock,
       "systemScreenLockCode": systemScreenLockCode,
       "systemScreenLockEnabled": systemScreenLockEnabled,
       "systemScreenScreensaverType": systemScreenScreensaverType,
       "systemScreenTimeout": systemScreenTimeout,
       "systemSerialNumber": systemSerialNumber,
       "systemSnmpd": systemSnmpd,
       "systemSnmpdActive": systemSnmpdActive,
       "systemSnmpdCommunity": systemSnmpdCommunity,
       "systemSnmpdDescription": systemSnmpdDescription,
       "systemSnmpdName": systemSnmpdName,
       "systemSnmpdObjectId": systemSnmpdObjectId,
       "systemSnmpdPort": systemSnmpdPort,
       "systemSnmpdReadOnly": systemSnmpdReadOnly,
       "systemSnmpdTrap": systemSnmpdTrap,
       "systemSnmpdTrapDst1": systemSnmpdTrapDst1,
       "systemSnmpdTrapDst1Ip": systemSnmpdTrapDst1Ip,
       "systemSnmpdTrapDst1Port": systemSnmpdTrapDst1Port,
       "systemSnmpdTrapDst2": systemSnmpdTrapDst2,
       "systemSnmpdTrapDst2Ip": systemSnmpdTrapDst2Ip,
       "systemSnmpdTrapDst2Port": systemSnmpdTrapDst2Port,
       "systemSnmpdTrapTest": systemSnmpdTrapTest,
       "systemSnmpdTrapTestSend": systemSnmpdTrapTestSend,
       "systemSoftware": systemSoftware,
       "systemSoftwareVersion": systemSoftwareVersion,
       "systemTelnetd": systemTelnetd,
       "systemTelnetdActive": systemTelnetdActive,
       "systemTelnetdPort": systemTelnetdPort,
       "systemTime": systemTime,
       "systemUptime": systemUptime,
       "systemUsername": systemUsername,
       "systemUsernameAdmin": systemUsernameAdmin,
       "transmitter": transmitter,
       "transmitterFrequency": transmitterFrequency,
       "transmitterFsk": transmitterFsk,
       "transmitterFskId": transmitterFskId,
       "transmitterFskInterval": transmitterFskInterval,
       "transmitterRfMute": transmitterRfMute,
       "transmitterRfMuteManualEnable": transmitterRfMuteManualEnable,
       "transmitterRfMuteTimeout": transmitterRfMuteTimeout,
       "transmitterSetPower": transmitterSetPower,
       "trigger1": trigger1,
       "trigger1Action": trigger1Action,
       "trigger1Active": trigger1Active,
       "trigger1Email": trigger1Email,
       "trigger1EmailActive": trigger1EmailActive,
       "trigger1Message": trigger1Message,
       "trigger1MessageOn": trigger1MessageOn,
       "trigger1Trap": trigger1Trap,
       "trigger1TrapActive": trigger1TrapActive,
       "trigger2": trigger2,
       "trigger2Action": trigger2Action,
       "trigger2Active": trigger2Active,
       "trigger2Email": trigger2Email,
       "trigger2EmailActive": trigger2EmailActive,
       "trigger2Message": trigger2Message,
       "trigger2MessageOn": trigger2MessageOn,
       "trigger2Trap": trigger2Trap,
       "trigger2TrapActive": trigger2TrapActive,
       "trigger3": trigger3,
       "trigger3Action": trigger3Action,
       "trigger3Active": trigger3Active,
       "trigger3Email": trigger3Email,
       "trigger3EmailActive": trigger3EmailActive,
       "trigger3Message": trigger3Message,
       "trigger3MessageOn": trigger3MessageOn,
       "trigger3Trap": trigger3Trap,
       "trigger3TrapActive": trigger3TrapActive,
       "trigger4": trigger4,
       "trigger4Action": trigger4Action,
       "trigger4Active": trigger4Active,
       "trigger4Email": trigger4Email,
       "trigger4EmailActive": trigger4EmailActive,
       "trigger4Message": trigger4Message,
       "trigger4MessageOn": trigger4MessageOn,
       "trigger4Trap": trigger4Trap,
       "trigger4TrapActive": trigger4TrapActive,
       "triggers": triggers,
       "triggersRfmutestyle": triggersRfmutestyle,
       "meters": meters,
       "metersAcrfeff": metersAcrfeff,
       "metersAgc1": metersAgc1,
       "metersAgc2": metersAgc2,
       "metersAgc3": metersAgc3,
       "metersAgc4": metersAgc4,
       "metersFallback": metersFallback,
       "metersFanspeed": metersFanspeed,
       "metersLim1": metersLim1,
       "metersLim2": metersLim2,
       "metersLim3": metersLim3,
       "metersLim4": metersLim4,
       "metersMainsv": metersMainsv,
       "metersPeakDeviation": metersPeakDeviation,
       "metersPsu1temp1": metersPsu1temp1,
       "metersPsu2temp1": metersPsu2temp1,
       "metersPsucurrent": metersPsucurrent,
       "metersPsuvoltage": metersPsuvoltage,
       "metersTxInputL": metersTxInputL,
       "metersTxInputR": metersTxInputR,
       "metersTxOutputL": metersTxOutputL,
       "metersTxOutputMpx": metersTxOutputMpx,
       "metersTxOutputR": metersTxOutputR,
       "metersVSWRLimitActive": metersVSWRLimitActive,
       "metersTempLimitActive": metersTempLimitActive,
       "conformance": conformance,
       "conformanceGroups": conformanceGroups,
       "allObjects": allObjects,
       "compliances": compliances,
       "compliance": compliance}
)
