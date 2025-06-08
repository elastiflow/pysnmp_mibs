# SNMP MIB module (CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/continental_48307/CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:57:19 2025
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

(cecVLF,) = mibBuilder.importSymbols(
    "CONTELEC-COMMON-MIB",
    "cecVLF")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

contelecVLFTransmitter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2)
)
if mibBuilder.loadTexts:
    contelecVLFTransmitter.setRevisions(
        ("2017-04-21 14:20",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ContelecVLFTXConformance_ObjectIdentity = ObjectIdentity
contelecVLFTXConformance = _ContelecVLFTXConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2)
)
_ContelecVLFTXCompliances_ObjectIdentity = ObjectIdentity
contelecVLFTXCompliances = _ContelecVLFTXCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 1)
)
_ContelecVLFTXGroups_ObjectIdentity = ObjectIdentity
contelecVLFTXGroups = _ContelecVLFTXGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 2)
)
_ContelecVLFTXobject_ObjectIdentity = ObjectIdentity
contelecVLFTXobject = _ContelecVLFTXobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3)
)
_ContelecVLFTXTraps_ObjectIdentity = ObjectIdentity
contelecVLFTXTraps = _ContelecVLFTXTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0)
)
_ContelecVLFTXSpecs_ObjectIdentity = ObjectIdentity
contelecVLFTXSpecs = _ContelecVLFTXSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1)
)


class _ContelecVLFTXFrequency_Type(Integer32):
    """Custom type contelecVLFTXFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14000, 50000),
    )


_ContelecVLFTXFrequency_Type.__name__ = "Integer32"
_ContelecVLFTXFrequency_Object = MibScalar
contelecVLFTXFrequency = _ContelecVLFTXFrequency_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 1),
    _ContelecVLFTXFrequency_Type()
)
contelecVLFTXFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXFrequency.setStatus("current")
_ContelecVLFTXEQControl_Type = TruthValue
_ContelecVLFTXEQControl_Object = MibScalar
contelecVLFTXEQControl = _ContelecVLFTXEQControl_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 2),
    _ContelecVLFTXEQControl_Type()
)
contelecVLFTXEQControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXEQControl.setStatus("current")


class _ContelecVLFTXCCORiseTime_Type(Unsigned32):
    """Custom type contelecVLFTXCCORiseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ContelecVLFTXCCORiseTime_Type.__name__ = "Unsigned32"
_ContelecVLFTXCCORiseTime_Object = MibScalar
contelecVLFTXCCORiseTime = _ContelecVLFTXCCORiseTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 3),
    _ContelecVLFTXCCORiseTime_Type()
)
contelecVLFTXCCORiseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXCCORiseTime.setStatus("current")


class _ContelecVLFTXCCOFallTime_Type(Unsigned32):
    """Custom type contelecVLFTXCCOFallTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ContelecVLFTXCCOFallTime_Type.__name__ = "Unsigned32"
_ContelecVLFTXCCOFallTime_Object = MibScalar
contelecVLFTXCCOFallTime = _ContelecVLFTXCCOFallTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 4),
    _ContelecVLFTXCCOFallTime_Type()
)
contelecVLFTXCCOFallTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXCCOFallTime.setStatus("current")


class _ContelecVLFTXA1ARiseTime_Type(Unsigned32):
    """Custom type contelecVLFTXA1ARiseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ContelecVLFTXA1ARiseTime_Type.__name__ = "Unsigned32"
_ContelecVLFTXA1ARiseTime_Object = MibScalar
contelecVLFTXA1ARiseTime = _ContelecVLFTXA1ARiseTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 5),
    _ContelecVLFTXA1ARiseTime_Type()
)
contelecVLFTXA1ARiseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXA1ARiseTime.setStatus("current")


class _ContelecVLFTXA1AFallTime_Type(Unsigned32):
    """Custom type contelecVLFTXA1AFallTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ContelecVLFTXA1AFallTime_Type.__name__ = "Unsigned32"
_ContelecVLFTXA1AFallTime_Object = MibScalar
contelecVLFTXA1AFallTime = _ContelecVLFTXA1AFallTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 6),
    _ContelecVLFTXA1AFallTime_Type()
)
contelecVLFTXA1AFallTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXA1AFallTime.setStatus("current")
_ContelecVLFTXModulationType_Type = TruthValue
_ContelecVLFTXModulationType_Object = MibScalar
contelecVLFTXModulationType = _ContelecVLFTXModulationType_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 7),
    _ContelecVLFTXModulationType_Type()
)
contelecVLFTXModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXModulationType.setStatus("current")


class _ContelecVLFTXEQNLOOP_Type(Unsigned32):
    """Custom type contelecVLFTXEQNLOOP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ContelecVLFTXEQNLOOP_Type.__name__ = "Unsigned32"
_ContelecVLFTXEQNLOOP_Object = MibScalar
contelecVLFTXEQNLOOP = _ContelecVLFTXEQNLOOP_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 8),
    _ContelecVLFTXEQNLOOP_Type()
)
contelecVLFTXEQNLOOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXEQNLOOP.setStatus("current")


class _ContelecVLFTXEQConverge_Type(Integer32):
    """Custom type contelecVLFTXEQConverge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 6000),
    )


_ContelecVLFTXEQConverge_Type.__name__ = "Integer32"
_ContelecVLFTXEQConverge_Object = MibScalar
contelecVLFTXEQConverge = _ContelecVLFTXEQConverge_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 9),
    _ContelecVLFTXEQConverge_Type()
)
contelecVLFTXEQConverge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXEQConverge.setStatus("current")


class _ContelecVLFTXRFVInputScale_Type(Integer32):
    """Custom type contelecVLFTXRFVInputScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ContelecVLFTXRFVInputScale_Type.__name__ = "Integer32"
_ContelecVLFTXRFVInputScale_Object = MibScalar
contelecVLFTXRFVInputScale = _ContelecVLFTXRFVInputScale_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 10),
    _ContelecVLFTXRFVInputScale_Type()
)
contelecVLFTXRFVInputScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXRFVInputScale.setStatus("current")


class _ContelecVLFTXRampDelayOff_Type(Unsigned32):
    """Custom type contelecVLFTXRampDelayOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ContelecVLFTXRampDelayOff_Type.__name__ = "Unsigned32"
_ContelecVLFTXRampDelayOff_Object = MibScalar
contelecVLFTXRampDelayOff = _ContelecVLFTXRampDelayOff_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 11),
    _ContelecVLFTXRampDelayOff_Type()
)
contelecVLFTXRampDelayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXRampDelayOff.setStatus("current")


class _ContelecVLFTXRampDelayOn_Type(Unsigned32):
    """Custom type contelecVLFTXRampDelayOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ContelecVLFTXRampDelayOn_Type.__name__ = "Unsigned32"
_ContelecVLFTXRampDelayOn_Object = MibScalar
contelecVLFTXRampDelayOn = _ContelecVLFTXRampDelayOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 12),
    _ContelecVLFTXRampDelayOn_Type()
)
contelecVLFTXRampDelayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXRampDelayOn.setStatus("current")


class _ContelecVLFTXModRFInputLevel_Type(Integer32):
    """Custom type contelecVLFTXModRFInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXModRFInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXModRFInputLevel_Object = MibScalar
contelecVLFTXModRFInputLevel = _ContelecVLFTXModRFInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 13),
    _ContelecVLFTXModRFInputLevel_Type()
)
contelecVLFTXModRFInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXModRFInputLevel.setStatus("current")
_ContelecVLFTXModRFClip_Type = TruthValue
_ContelecVLFTXModRFClip_Object = MibScalar
contelecVLFTXModRFClip = _ContelecVLFTXModRFClip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 14),
    _ContelecVLFTXModRFClip_Type()
)
contelecVLFTXModRFClip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXModRFClip.setStatus("current")
_ContelecVLFTXLowRFDrive_Type = TruthValue
_ContelecVLFTXLowRFDrive_Object = MibScalar
contelecVLFTXLowRFDrive = _ContelecVLFTXLowRFDrive_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 15),
    _ContelecVLFTXLowRFDrive_Type()
)
contelecVLFTXLowRFDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXLowRFDrive.setStatus("current")
_ContelecVLFTXModIntSineWave_Type = TruthValue
_ContelecVLFTXModIntSineWave_Object = MibScalar
contelecVLFTXModIntSineWave = _ContelecVLFTXModIntSineWave_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 16),
    _ContelecVLFTXModIntSineWave_Type()
)
contelecVLFTXModIntSineWave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXModIntSineWave.setStatus("current")


class _ContelecVLFTXAdaptiveStatus_Type(Bits):
    """Custom type contelecVLFTXAdaptiveStatus based on Bits"""
    namedValues = NamedValues(
        *(("tapEnergyTooHigh", 0),
          ("gMinTooLow", 1),
          ("gMaxTooHigh", 2),
          ("aModulatorSampleTooNegative", 3),
          ("aModulatorSampleTooPositive", 4),
          ("modulatorRMSInputTooLow", 5),
          ("modulatorRMSInputTooHigh", 6),
          ("antennaSampleTooNegative", 7),
          ("antennaSampleTooPositive", 8),
          ("antennaRMSSampleTooLow", 9),
          ("antennaRMSSampleTooHigh", 10),
          ("stabilityFault", 11),
          ("correlationFailure", 12),
          ("rmsDeviationTooLow", 13),
          ("noiseInModulatorOrAntennaSamples", 14))
    )

_ContelecVLFTXAdaptiveStatus_Type.__name__ = "Bits"
_ContelecVLFTXAdaptiveStatus_Object = MibScalar
contelecVLFTXAdaptiveStatus = _ContelecVLFTXAdaptiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 17),
    _ContelecVLFTXAdaptiveStatus_Type()
)
contelecVLFTXAdaptiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAdaptiveStatus.setStatus("current")


class _ContelecVLFTXOutputPower_Type(Integer32):
    """Custom type contelecVLFTXOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ContelecVLFTXOutputPower_Type.__name__ = "Integer32"
_ContelecVLFTXOutputPower_Object = MibScalar
contelecVLFTXOutputPower = _ContelecVLFTXOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 18),
    _ContelecVLFTXOutputPower_Type()
)
contelecVLFTXOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXOutputPower.setStatus("current")


class _ContelecVLFTXReflectedPower_Type(Integer32):
    """Custom type contelecVLFTXReflectedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ContelecVLFTXReflectedPower_Type.__name__ = "Integer32"
_ContelecVLFTXReflectedPower_Object = MibScalar
contelecVLFTXReflectedPower = _ContelecVLFTXReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 19),
    _ContelecVLFTXReflectedPower_Type()
)
contelecVLFTXReflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXReflectedPower.setStatus("current")


class _ContelecVLFTXImpedanceReal_Type(Integer32):
    """Custom type contelecVLFTXImpedanceReal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560),
    )


_ContelecVLFTXImpedanceReal_Type.__name__ = "Integer32"
_ContelecVLFTXImpedanceReal_Object = MibScalar
contelecVLFTXImpedanceReal = _ContelecVLFTXImpedanceReal_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 20),
    _ContelecVLFTXImpedanceReal_Type()
)
contelecVLFTXImpedanceReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXImpedanceReal.setStatus("current")


class _ContelecVLFTXImpedanceImag_Type(Integer32):
    """Custom type contelecVLFTXImpedanceImag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2560, 2560),
    )


_ContelecVLFTXImpedanceImag_Type.__name__ = "Integer32"
_ContelecVLFTXImpedanceImag_Object = MibScalar
contelecVLFTXImpedanceImag = _ContelecVLFTXImpedanceImag_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 21),
    _ContelecVLFTXImpedanceImag_Type()
)
contelecVLFTXImpedanceImag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXImpedanceImag.setStatus("current")


class _ContelecVLFTXVSWR_Type(Integer32):
    """Custom type contelecVLFTXVSWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_ContelecVLFTXVSWR_Type.__name__ = "Integer32"
_ContelecVLFTXVSWR_Object = MibScalar
contelecVLFTXVSWR = _ContelecVLFTXVSWR_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 22),
    _ContelecVLFTXVSWR_Type()
)
contelecVLFTXVSWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXVSWR.setStatus("current")
_ContelecVLFTXS11Real_Type = Integer32
_ContelecVLFTXS11Real_Object = MibScalar
contelecVLFTXS11Real = _ContelecVLFTXS11Real_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 23),
    _ContelecVLFTXS11Real_Type()
)
contelecVLFTXS11Real.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXS11Real.setStatus("current")
_ContelecVLFTXS11Imag_Type = Integer32
_ContelecVLFTXS11Imag_Object = MibScalar
contelecVLFTXS11Imag = _ContelecVLFTXS11Imag_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 24),
    _ContelecVLFTXS11Imag_Type()
)
contelecVLFTXS11Imag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXS11Imag.setStatus("current")


class _ContelecVLFTXPARFCurrent_Type(Integer32):
    """Custom type contelecVLFTXPARFCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXPARFCurrent_Type.__name__ = "Integer32"
_ContelecVLFTXPARFCurrent_Object = MibScalar
contelecVLFTXPARFCurrent = _ContelecVLFTXPARFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 25),
    _ContelecVLFTXPARFCurrent_Type()
)
contelecVLFTXPARFCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXPARFCurrent.setStatus("current")


class _ContelecVLFTXCombinerCurrentSetPointTrip_Type(Integer32):
    """Custom type contelecVLFTXCombinerCurrentSetPointTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXCombinerCurrentSetPointTrip_Type.__name__ = "Integer32"
_ContelecVLFTXCombinerCurrentSetPointTrip_Object = MibScalar
contelecVLFTXCombinerCurrentSetPointTrip = _ContelecVLFTXCombinerCurrentSetPointTrip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 26),
    _ContelecVLFTXCombinerCurrentSetPointTrip_Type()
)
contelecVLFTXCombinerCurrentSetPointTrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXCombinerCurrentSetPointTrip.setStatus("current")


class _ContelecVLFTXOutputRFCurrent_Type(Integer32):
    """Custom type contelecVLFTXOutputRFCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXOutputRFCurrent_Type.__name__ = "Integer32"
_ContelecVLFTXOutputRFCurrent_Object = MibScalar
contelecVLFTXOutputRFCurrent = _ContelecVLFTXOutputRFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 27),
    _ContelecVLFTXOutputRFCurrent_Type()
)
contelecVLFTXOutputRFCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXOutputRFCurrent.setStatus("current")


class _ContelecVLFTXOutputRFCurrentSetPointTrip_Type(Integer32):
    """Custom type contelecVLFTXOutputRFCurrentSetPointTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXOutputRFCurrentSetPointTrip_Type.__name__ = "Integer32"
_ContelecVLFTXOutputRFCurrentSetPointTrip_Object = MibScalar
contelecVLFTXOutputRFCurrentSetPointTrip = _ContelecVLFTXOutputRFCurrentSetPointTrip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 28),
    _ContelecVLFTXOutputRFCurrentSetPointTrip_Type()
)
contelecVLFTXOutputRFCurrentSetPointTrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXOutputRFCurrentSetPointTrip.setStatus("current")


class _ContelecVLFTXSNR_Type(Integer32):
    """Custom type contelecVLFTXSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ContelecVLFTXSNR_Type.__name__ = "Integer32"
_ContelecVLFTXSNR_Object = MibScalar
contelecVLFTXSNR = _ContelecVLFTXSNR_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 29),
    _ContelecVLFTXSNR_Type()
)
contelecVLFTXSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXSNR.setStatus("current")
_ContelecVLFTXTSPLoopStatus_Type = TruthValue
_ContelecVLFTXTSPLoopStatus_Object = MibScalar
contelecVLFTXTSPLoopStatus = _ContelecVLFTXTSPLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 30),
    _ContelecVLFTXTSPLoopStatus_Type()
)
contelecVLFTXTSPLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXTSPLoopStatus.setStatus("current")
_ContelecVLFTXAntennaReverseInterlock_Type = TruthValue
_ContelecVLFTXAntennaReverseInterlock_Object = MibScalar
contelecVLFTXAntennaReverseInterlock = _ContelecVLFTXAntennaReverseInterlock_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 31),
    _ContelecVLFTXAntennaReverseInterlock_Type()
)
contelecVLFTXAntennaReverseInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAntennaReverseInterlock.setStatus("current")
_ContelecVLFTXPACab1Doors_Type = TruthValue
_ContelecVLFTXPACab1Doors_Object = MibScalar
contelecVLFTXPACab1Doors = _ContelecVLFTXPACab1Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 32),
    _ContelecVLFTXPACab1Doors_Type()
)
contelecVLFTXPACab1Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXPACab1Doors.setStatus("current")
_ContelecVLFTXPACab2Doors_Type = TruthValue
_ContelecVLFTXPACab2Doors_Object = MibScalar
contelecVLFTXPACab2Doors = _ContelecVLFTXPACab2Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 33),
    _ContelecVLFTXPACab2Doors_Type()
)
contelecVLFTXPACab2Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXPACab2Doors.setStatus("current")
_ContelecVLFTXTeeNetCab1Doors_Type = TruthValue
_ContelecVLFTXTeeNetCab1Doors_Object = MibScalar
contelecVLFTXTeeNetCab1Doors = _ContelecVLFTXTeeNetCab1Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 34),
    _ContelecVLFTXTeeNetCab1Doors_Type()
)
contelecVLFTXTeeNetCab1Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXTeeNetCab1Doors.setStatus("current")
_ContelecVLFTXTeeNetCab2Doors_Type = TruthValue
_ContelecVLFTXTeeNetCab2Doors_Object = MibScalar
contelecVLFTXTeeNetCab2Doors = _ContelecVLFTXTeeNetCab2Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 35),
    _ContelecVLFTXTeeNetCab2Doors_Type()
)
contelecVLFTXTeeNetCab2Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXTeeNetCab2Doors.setStatus("current")


class _ContelecVLFTXDCVoltagePA1_Type(Integer32):
    """Custom type contelecVLFTXDCVoltagePA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ContelecVLFTXDCVoltagePA1_Type.__name__ = "Integer32"
_ContelecVLFTXDCVoltagePA1_Object = MibScalar
contelecVLFTXDCVoltagePA1 = _ContelecVLFTXDCVoltagePA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 36),
    _ContelecVLFTXDCVoltagePA1_Type()
)
contelecVLFTXDCVoltagePA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXDCVoltagePA1.setStatus("current")


class _ContelecVLFTXDCVoltagePA2_Type(Integer32):
    """Custom type contelecVLFTXDCVoltagePA2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ContelecVLFTXDCVoltagePA2_Type.__name__ = "Integer32"
_ContelecVLFTXDCVoltagePA2_Object = MibScalar
contelecVLFTXDCVoltagePA2 = _ContelecVLFTXDCVoltagePA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 37),
    _ContelecVLFTXDCVoltagePA2_Type()
)
contelecVLFTXDCVoltagePA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXDCVoltagePA2.setStatus("current")


class _ContelecVLFTXAverageDCVoltage_Type(Integer32):
    """Custom type contelecVLFTXAverageDCVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ContelecVLFTXAverageDCVoltage_Type.__name__ = "Integer32"
_ContelecVLFTXAverageDCVoltage_Object = MibScalar
contelecVLFTXAverageDCVoltage = _ContelecVLFTXAverageDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 38),
    _ContelecVLFTXAverageDCVoltage_Type()
)
contelecVLFTXAverageDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAverageDCVoltage.setStatus("current")


class _ContelecVLFTXDCCurrentPA1_Type(Integer32):
    """Custom type contelecVLFTXDCCurrentPA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ContelecVLFTXDCCurrentPA1_Type.__name__ = "Integer32"
_ContelecVLFTXDCCurrentPA1_Object = MibScalar
contelecVLFTXDCCurrentPA1 = _ContelecVLFTXDCCurrentPA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 39),
    _ContelecVLFTXDCCurrentPA1_Type()
)
contelecVLFTXDCCurrentPA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXDCCurrentPA1.setStatus("current")


class _ContelecVLFTXDCCurrentPA2_Type(Integer32):
    """Custom type contelecVLFTXDCCurrentPA2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ContelecVLFTXDCCurrentPA2_Type.__name__ = "Integer32"
_ContelecVLFTXDCCurrentPA2_Object = MibScalar
contelecVLFTXDCCurrentPA2 = _ContelecVLFTXDCCurrentPA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 40),
    _ContelecVLFTXDCCurrentPA2_Type()
)
contelecVLFTXDCCurrentPA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXDCCurrentPA2.setStatus("current")


class _ContelecVLFTXTotalDCCurrent_Type(Integer32):
    """Custom type contelecVLFTXTotalDCCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ContelecVLFTXTotalDCCurrent_Type.__name__ = "Integer32"
_ContelecVLFTXTotalDCCurrent_Object = MibScalar
contelecVLFTXTotalDCCurrent = _ContelecVLFTXTotalDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 41),
    _ContelecVLFTXTotalDCCurrent_Type()
)
contelecVLFTXTotalDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXTotalDCCurrent.setStatus("current")


class _ContelecVLFTXDCVoltageTripLevelLow_Type(Integer32):
    """Custom type contelecVLFTXDCVoltageTripLevelLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ContelecVLFTXDCVoltageTripLevelLow_Type.__name__ = "Integer32"
_ContelecVLFTXDCVoltageTripLevelLow_Object = MibScalar
contelecVLFTXDCVoltageTripLevelLow = _ContelecVLFTXDCVoltageTripLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 42),
    _ContelecVLFTXDCVoltageTripLevelLow_Type()
)
contelecVLFTXDCVoltageTripLevelLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXDCVoltageTripLevelLow.setStatus("current")


class _ContelecVLFTXDCVoltageTripLevelHigh_Type(Integer32):
    """Custom type contelecVLFTXDCVoltageTripLevelHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ContelecVLFTXDCVoltageTripLevelHigh_Type.__name__ = "Integer32"
_ContelecVLFTXDCVoltageTripLevelHigh_Object = MibScalar
contelecVLFTXDCVoltageTripLevelHigh = _ContelecVLFTXDCVoltageTripLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 43),
    _ContelecVLFTXDCVoltageTripLevelHigh_Type()
)
contelecVLFTXDCVoltageTripLevelHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXDCVoltageTripLevelHigh.setStatus("current")


class _ContelecVLFTXDCCurrentTripLevelLow_Type(Integer32):
    """Custom type contelecVLFTXDCCurrentTripLevelLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ContelecVLFTXDCCurrentTripLevelLow_Type.__name__ = "Integer32"
_ContelecVLFTXDCCurrentTripLevelLow_Object = MibScalar
contelecVLFTXDCCurrentTripLevelLow = _ContelecVLFTXDCCurrentTripLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 44),
    _ContelecVLFTXDCCurrentTripLevelLow_Type()
)
contelecVLFTXDCCurrentTripLevelLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXDCCurrentTripLevelLow.setStatus("current")


class _ContelecVLFTXDCCurrentTripLevelHigh_Type(Integer32):
    """Custom type contelecVLFTXDCCurrentTripLevelHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ContelecVLFTXDCCurrentTripLevelHigh_Type.__name__ = "Integer32"
_ContelecVLFTXDCCurrentTripLevelHigh_Object = MibScalar
contelecVLFTXDCCurrentTripLevelHigh = _ContelecVLFTXDCCurrentTripLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 45),
    _ContelecVLFTXDCCurrentTripLevelHigh_Type()
)
contelecVLFTXDCCurrentTripLevelHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXDCCurrentTripLevelHigh.setStatus("current")


class _ContelecVLFTXDCPowerSupplyTempStatus_Type(Bits):
    """Custom type contelecVLFTXDCPowerSupplyTempStatus based on Bits"""
    namedValues = NamedValues(
        *(("ps1OverTemperatureFault", 0),
          ("ps2OverTemperatureFault", 1))
    )

_ContelecVLFTXDCPowerSupplyTempStatus_Type.__name__ = "Bits"
_ContelecVLFTXDCPowerSupplyTempStatus_Object = MibScalar
contelecVLFTXDCPowerSupplyTempStatus = _ContelecVLFTXDCPowerSupplyTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 46),
    _ContelecVLFTXDCPowerSupplyTempStatus_Type()
)
contelecVLFTXDCPowerSupplyTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXDCPowerSupplyTempStatus.setStatus("current")
_ContelecVLFTXLowLevelSuppliesPA1_Type = TruthValue
_ContelecVLFTXLowLevelSuppliesPA1_Object = MibScalar
contelecVLFTXLowLevelSuppliesPA1 = _ContelecVLFTXLowLevelSuppliesPA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 47),
    _ContelecVLFTXLowLevelSuppliesPA1_Type()
)
contelecVLFTXLowLevelSuppliesPA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXLowLevelSuppliesPA1.setStatus("current")
_ContelecVLFTXLowLevelSuppliesPA2_Type = TruthValue
_ContelecVLFTXLowLevelSuppliesPA2_Object = MibScalar
contelecVLFTXLowLevelSuppliesPA2 = _ContelecVLFTXLowLevelSuppliesPA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 48),
    _ContelecVLFTXLowLevelSuppliesPA2_Type()
)
contelecVLFTXLowLevelSuppliesPA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXLowLevelSuppliesPA2.setStatus("current")


class _ContelecVLFTXPAPhase_Type(Integer32):
    """Custom type contelecVLFTXPAPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_ContelecVLFTXPAPhase_Type.__name__ = "Integer32"
_ContelecVLFTXPAPhase_Object = MibScalar
contelecVLFTXPAPhase = _ContelecVLFTXPAPhase_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 49),
    _ContelecVLFTXPAPhase_Type()
)
contelecVLFTXPAPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXPAPhase.setStatus("current")


class _ContelecVLFTXModuleStatus1PA1_Type(Bits):
    """Custom type contelecVLFTXModuleStatus1PA1 based on Bits"""
    namedValues = NamedValues(
        *(("pa1Module01OK", 0),
          ("pa1Module02OK", 1),
          ("pa1Module03OK", 2),
          ("pa1Module04OK", 3),
          ("pa1Module05OK", 4),
          ("pa1Module06OK", 5),
          ("pa1Module07OK", 6),
          ("pa1Module08OK", 7),
          ("pa1Module09OK", 8),
          ("pa1Module10OK", 9),
          ("pa1Module11OK", 10),
          ("pa1Module12OK", 11),
          ("pa1Module13OK", 12),
          ("pa1Module14OK", 13),
          ("pa1Module15OK", 14),
          ("pa1Module16OK", 15),
          ("pa1Module17OK", 16),
          ("pa1Module18OK", 17),
          ("pa1Module19OK", 18),
          ("pa1Module20OK", 19),
          ("pa1Module21OK", 20),
          ("pa1Module22OK", 21),
          ("pa1Module23OK", 22),
          ("pa1Module24OK", 23),
          ("pa1Module25OK", 24),
          ("pa1Module26OK", 25),
          ("pa1Module27OK", 26),
          ("pa1Module28OK", 27),
          ("pa1Module29OK", 28),
          ("pa1Module30OK", 29),
          ("pa1Module31OK", 30),
          ("pa1Module32OK", 31))
    )

_ContelecVLFTXModuleStatus1PA1_Type.__name__ = "Bits"
_ContelecVLFTXModuleStatus1PA1_Object = MibScalar
contelecVLFTXModuleStatus1PA1 = _ContelecVLFTXModuleStatus1PA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 50),
    _ContelecVLFTXModuleStatus1PA1_Type()
)
contelecVLFTXModuleStatus1PA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXModuleStatus1PA1.setStatus("current")


class _ContelecVLFTXModuleStatus2PA1_Type(Bits):
    """Custom type contelecVLFTXModuleStatus2PA1 based on Bits"""
    namedValues = NamedValues(
        *(("pa1Module33OK", 0),
          ("pa1Module34OK", 1),
          ("pa1Module35OK", 2),
          ("pa1Module36OK", 3),
          ("pa1Module37OK", 4),
          ("pa1Module38OK", 5),
          ("pa1Module39OK", 6),
          ("pa1Module40OK", 7),
          ("pa1Module41OK", 8),
          ("pa1Module42OK", 9),
          ("pa1Module43OK", 10),
          ("pa1Module44OK", 11),
          ("pa1Module45OK", 12),
          ("pa1Module46OK", 13),
          ("pa1Module47OK", 14),
          ("pa1Module48OK", 15),
          ("pa1Module49OK", 16),
          ("pa1Module50OK", 17),
          ("pa1Module51OK", 18),
          ("pa1Module52OK", 19),
          ("pa1Module53OK", 20),
          ("pa1Module54OK", 21),
          ("pa1Module55OK", 22),
          ("pa1Module56OK", 23),
          ("pa1Module57OK", 24),
          ("pa1Module58OK", 25),
          ("pa1Module59OK", 26),
          ("pa1Module60OK", 27),
          ("pa1Module61OK", 28),
          ("pa1Module62OK", 29),
          ("pa1Module63OK", 30),
          ("pa1Module64OK", 31))
    )

_ContelecVLFTXModuleStatus2PA1_Type.__name__ = "Bits"
_ContelecVLFTXModuleStatus2PA1_Object = MibScalar
contelecVLFTXModuleStatus2PA1 = _ContelecVLFTXModuleStatus2PA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 51),
    _ContelecVLFTXModuleStatus2PA1_Type()
)
contelecVLFTXModuleStatus2PA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXModuleStatus2PA1.setStatus("current")


class _ContelecVLFTXModuleStatus1PA2_Type(Bits):
    """Custom type contelecVLFTXModuleStatus1PA2 based on Bits"""
    namedValues = NamedValues(
        *(("pa2Module01OK", 0),
          ("pa2Module02OK", 1),
          ("pa2Module03OK", 2),
          ("pa2Module04OK", 3),
          ("pa2Module05OK", 4),
          ("pa2Module06OK", 5),
          ("pa2Module07OK", 6),
          ("pa2Module08OK", 7),
          ("pa2Module09OK", 8),
          ("pa2Module10OK", 9),
          ("pa2Module11OK", 10),
          ("pa2Module12OK", 11),
          ("pa2Module13OK", 12),
          ("pa2Module14OK", 13),
          ("pa2Module15OK", 14),
          ("pa2Module16OK", 15),
          ("pa2Module17OK", 16),
          ("pa2Module18OK", 17),
          ("pa2Module19OK", 18),
          ("pa2Module20OK", 19),
          ("pa2Module21OK", 20),
          ("pa2Module22OK", 21),
          ("pa2Module23OK", 22),
          ("pa2Module24OK", 23),
          ("pa2Module25OK", 24),
          ("pa2Module26OK", 25),
          ("pa2Module27OK", 26),
          ("pa2Module28OK", 27),
          ("pa2Module29OK", 28),
          ("pa2Module30OK", 29),
          ("pa2Module31OK", 30),
          ("pa2Module32OK", 31))
    )

_ContelecVLFTXModuleStatus1PA2_Type.__name__ = "Bits"
_ContelecVLFTXModuleStatus1PA2_Object = MibScalar
contelecVLFTXModuleStatus1PA2 = _ContelecVLFTXModuleStatus1PA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 52),
    _ContelecVLFTXModuleStatus1PA2_Type()
)
contelecVLFTXModuleStatus1PA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXModuleStatus1PA2.setStatus("current")


class _ContelecVLFTXModuleStatus2PA2_Type(Bits):
    """Custom type contelecVLFTXModuleStatus2PA2 based on Bits"""
    namedValues = NamedValues(
        *(("pa2Module33OK", 0),
          ("pa2Module34OK", 1),
          ("pa2Module35OK", 2),
          ("pa2Module36OK", 3),
          ("pa2Module37OK", 4),
          ("pa2Module38OK", 5),
          ("pa2Module39OK", 6),
          ("pa2Module40OK", 7),
          ("pa2Module41OK", 8),
          ("pa2Module42OK", 9),
          ("pa2Module43OK", 10),
          ("pa2Module44OK", 11),
          ("pa2Module45OK", 12),
          ("pa2Module46OK", 13),
          ("pa2Module47OK", 14),
          ("pa2Module48OK", 15),
          ("pa2Module49OK", 16),
          ("pa2Module50OK", 17),
          ("pa2Module51OK", 18),
          ("pa2Module52OK", 19),
          ("pa2Module53OK", 20),
          ("pa2Module54OK", 21),
          ("pa2Module55OK", 22),
          ("pa2Module56OK", 23),
          ("pa2Module57OK", 24),
          ("pa2Module58OK", 25),
          ("pa2Module59OK", 26),
          ("pa2Module60OK", 27),
          ("pa2Module61OK", 28),
          ("pa2Module62OK", 29),
          ("pa2Module63OK", 30),
          ("pa2Module64OK", 31))
    )

_ContelecVLFTXModuleStatus2PA2_Type.__name__ = "Bits"
_ContelecVLFTXModuleStatus2PA2_Object = MibScalar
contelecVLFTXModuleStatus2PA2 = _ContelecVLFTXModuleStatus2PA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 53),
    _ContelecVLFTXModuleStatus2PA2_Type()
)
contelecVLFTXModuleStatus2PA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXModuleStatus2PA2.setStatus("current")
_ContelecVLFTXModuleResetCmd_Type = TruthValue
_ContelecVLFTXModuleResetCmd_Object = MibScalar
contelecVLFTXModuleResetCmd = _ContelecVLFTXModuleResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 54),
    _ContelecVLFTXModuleResetCmd_Type()
)
contelecVLFTXModuleResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXModuleResetCmd.setStatus("current")


class _ContelecVLFTXVariometer1PosnSet_Type(Integer32):
    """Custom type contelecVLFTXVariometer1PosnSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_ContelecVLFTXVariometer1PosnSet_Type.__name__ = "Integer32"
_ContelecVLFTXVariometer1PosnSet_Object = MibScalar
contelecVLFTXVariometer1PosnSet = _ContelecVLFTXVariometer1PosnSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 55),
    _ContelecVLFTXVariometer1PosnSet_Type()
)
contelecVLFTXVariometer1PosnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXVariometer1PosnSet.setStatus("current")


class _ContelecVLFTXVariometer2PosnSet_Type(Integer32):
    """Custom type contelecVLFTXVariometer2PosnSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_ContelecVLFTXVariometer2PosnSet_Type.__name__ = "Integer32"
_ContelecVLFTXVariometer2PosnSet_Object = MibScalar
contelecVLFTXVariometer2PosnSet = _ContelecVLFTXVariometer2PosnSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 56),
    _ContelecVLFTXVariometer2PosnSet_Type()
)
contelecVLFTXVariometer2PosnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXVariometer2PosnSet.setStatus("current")


class _ContelecVLFTXCapacitorPosnSet_Type(Integer32):
    """Custom type contelecVLFTXCapacitorPosnSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_ContelecVLFTXCapacitorPosnSet_Type.__name__ = "Integer32"
_ContelecVLFTXCapacitorPosnSet_Object = MibScalar
contelecVLFTXCapacitorPosnSet = _ContelecVLFTXCapacitorPosnSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 57),
    _ContelecVLFTXCapacitorPosnSet_Type()
)
contelecVLFTXCapacitorPosnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXCapacitorPosnSet.setStatus("current")


class _ContelecVLFTXVariometer1PosnStatus_Type(Integer32):
    """Custom type contelecVLFTXVariometer1PosnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_ContelecVLFTXVariometer1PosnStatus_Type.__name__ = "Integer32"
_ContelecVLFTXVariometer1PosnStatus_Object = MibScalar
contelecVLFTXVariometer1PosnStatus = _ContelecVLFTXVariometer1PosnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 58),
    _ContelecVLFTXVariometer1PosnStatus_Type()
)
contelecVLFTXVariometer1PosnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXVariometer1PosnStatus.setStatus("current")


class _ContelecVLFTXVariometer2PosnStatus_Type(Integer32):
    """Custom type contelecVLFTXVariometer2PosnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_ContelecVLFTXVariometer2PosnStatus_Type.__name__ = "Integer32"
_ContelecVLFTXVariometer2PosnStatus_Object = MibScalar
contelecVLFTXVariometer2PosnStatus = _ContelecVLFTXVariometer2PosnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 59),
    _ContelecVLFTXVariometer2PosnStatus_Type()
)
contelecVLFTXVariometer2PosnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXVariometer2PosnStatus.setStatus("current")


class _ContelecVLFTXCapacitorPosnStatus_Type(Integer32):
    """Custom type contelecVLFTXCapacitorPosnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_ContelecVLFTXCapacitorPosnStatus_Type.__name__ = "Integer32"
_ContelecVLFTXCapacitorPosnStatus_Object = MibScalar
contelecVLFTXCapacitorPosnStatus = _ContelecVLFTXCapacitorPosnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 60),
    _ContelecVLFTXCapacitorPosnStatus_Type()
)
contelecVLFTXCapacitorPosnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXCapacitorPosnStatus.setStatus("current")


class _ContelecVLFTXVariometer1ServoStatus_Type(Bits):
    """Custom type contelecVLFTXVariometer1ServoStatus based on Bits"""
    namedValues = NamedValues(
        *(("noCommunicationsEthernet", 0),
          ("idle", 1),
          ("movingUp", 2),
          ("movingDown", 3),
          ("noCANBusCommuncations", 4),
          ("positionUnknown", 5),
          ("negativeLimit", 6),
          ("positiveLimit", 7),
          ("fault", 8),
          ("warning", 9),
          ("quickStop", 10),
          ("highVoltageTooLow", 11))
    )

_ContelecVLFTXVariometer1ServoStatus_Type.__name__ = "Bits"
_ContelecVLFTXVariometer1ServoStatus_Object = MibScalar
contelecVLFTXVariometer1ServoStatus = _ContelecVLFTXVariometer1ServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 61),
    _ContelecVLFTXVariometer1ServoStatus_Type()
)
contelecVLFTXVariometer1ServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXVariometer1ServoStatus.setStatus("current")


class _ContelecVLFTXVariometer2ServoStatus_Type(Bits):
    """Custom type contelecVLFTXVariometer2ServoStatus based on Bits"""
    namedValues = NamedValues(
        *(("noCommunicationsEthernet", 0),
          ("idle", 1),
          ("movingUp", 2),
          ("movingDown", 3),
          ("noCANBusCommuncations", 4),
          ("positionUnknown", 5),
          ("negativeLimit", 6),
          ("positiveLimit", 7),
          ("fault", 8),
          ("warning", 9),
          ("quickStop", 10),
          ("highVoltageTooLow", 11))
    )

_ContelecVLFTXVariometer2ServoStatus_Type.__name__ = "Bits"
_ContelecVLFTXVariometer2ServoStatus_Object = MibScalar
contelecVLFTXVariometer2ServoStatus = _ContelecVLFTXVariometer2ServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 62),
    _ContelecVLFTXVariometer2ServoStatus_Type()
)
contelecVLFTXVariometer2ServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXVariometer2ServoStatus.setStatus("current")


class _ContelecVLFTXCapacitorServoStatus_Type(Bits):
    """Custom type contelecVLFTXCapacitorServoStatus based on Bits"""
    namedValues = NamedValues(
        *(("noCommunicationsEthernet", 0),
          ("idle", 1),
          ("movingUp", 2),
          ("movingDown", 3),
          ("noCANBusCommuncations", 4),
          ("positionUnknown", 5),
          ("negativeLimit", 6),
          ("positiveLimit", 7),
          ("fault", 8),
          ("warning", 9),
          ("quickStop", 10),
          ("highVoltageTooLow", 11))
    )

_ContelecVLFTXCapacitorServoStatus_Type.__name__ = "Bits"
_ContelecVLFTXCapacitorServoStatus_Object = MibScalar
contelecVLFTXCapacitorServoStatus = _ContelecVLFTXCapacitorServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 63),
    _ContelecVLFTXCapacitorServoStatus_Type()
)
contelecVLFTXCapacitorServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXCapacitorServoStatus.setStatus("current")


class _ContelecVLFTXCapacitorSwSet_Type(Bits):
    """Custom type contelecVLFTXCapacitorSwSet based on Bits"""
    namedValues = NamedValues(
        *(("cap1SwitchIn", 0),
          ("cap2SwitchIn", 1),
          ("cap3SwitchIn", 2),
          ("cap4SwitchIn", 3))
    )

_ContelecVLFTXCapacitorSwSet_Type.__name__ = "Bits"
_ContelecVLFTXCapacitorSwSet_Object = MibScalar
contelecVLFTXCapacitorSwSet = _ContelecVLFTXCapacitorSwSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 64),
    _ContelecVLFTXCapacitorSwSet_Type()
)
contelecVLFTXCapacitorSwSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXCapacitorSwSet.setStatus("current")


class _ContelecVLFTXCapacitorSwStatus_Type(Bits):
    """Custom type contelecVLFTXCapacitorSwStatus based on Bits"""
    namedValues = NamedValues(
        *(("cap1SwitchedIn", 0),
          ("cap2SwitchedIn", 1),
          ("cap3SwitchedIn", 2),
          ("cap4SwitchedIn", 3))
    )

_ContelecVLFTXCapacitorSwStatus_Type.__name__ = "Bits"
_ContelecVLFTXCapacitorSwStatus_Object = MibScalar
contelecVLFTXCapacitorSwStatus = _ContelecVLFTXCapacitorSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 65),
    _ContelecVLFTXCapacitorSwStatus_Type()
)
contelecVLFTXCapacitorSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXCapacitorSwStatus.setStatus("current")
_ContelecVLFTXArcPACab1_Type = TruthValue
_ContelecVLFTXArcPACab1_Object = MibScalar
contelecVLFTXArcPACab1 = _ContelecVLFTXArcPACab1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 66),
    _ContelecVLFTXArcPACab1_Type()
)
contelecVLFTXArcPACab1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXArcPACab1.setStatus("current")
_ContelecVLFTXArcPACab2_Type = TruthValue
_ContelecVLFTXArcPACab2_Object = MibScalar
contelecVLFTXArcPACab2 = _ContelecVLFTXArcPACab2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 67),
    _ContelecVLFTXArcPACab2_Type()
)
contelecVLFTXArcPACab2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXArcPACab2.setStatus("current")
_ContelecVLFTXArcTeeNetVario1_Type = TruthValue
_ContelecVLFTXArcTeeNetVario1_Object = MibScalar
contelecVLFTXArcTeeNetVario1 = _ContelecVLFTXArcTeeNetVario1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 68),
    _ContelecVLFTXArcTeeNetVario1_Type()
)
contelecVLFTXArcTeeNetVario1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXArcTeeNetVario1.setStatus("current")
_ContelecVLFTXArcTeeNetVario2_Type = TruthValue
_ContelecVLFTXArcTeeNetVario2_Object = MibScalar
contelecVLFTXArcTeeNetVario2 = _ContelecVLFTXArcTeeNetVario2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 69),
    _ContelecVLFTXArcTeeNetVario2_Type()
)
contelecVLFTXArcTeeNetVario2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXArcTeeNetVario2.setStatus("current")
_ContelecVLFTXArcTeeNetCap_Type = TruthValue
_ContelecVLFTXArcTeeNetCap_Object = MibScalar
contelecVLFTXArcTeeNetCap = _ContelecVLFTXArcTeeNetCap_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 70),
    _ContelecVLFTXArcTeeNetCap_Type()
)
contelecVLFTXArcTeeNetCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXArcTeeNetCap.setStatus("current")
_ContelecVLFTXArcPACab1Test_Type = TruthValue
_ContelecVLFTXArcPACab1Test_Object = MibScalar
contelecVLFTXArcPACab1Test = _ContelecVLFTXArcPACab1Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 71),
    _ContelecVLFTXArcPACab1Test_Type()
)
contelecVLFTXArcPACab1Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXArcPACab1Test.setStatus("current")
_ContelecVLFTXArcPACab2Test_Type = TruthValue
_ContelecVLFTXArcPACab2Test_Object = MibScalar
contelecVLFTXArcPACab2Test = _ContelecVLFTXArcPACab2Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 72),
    _ContelecVLFTXArcPACab2Test_Type()
)
contelecVLFTXArcPACab2Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXArcPACab2Test.setStatus("current")
_ContelecVLFTXArcTeeNetVario1Test_Type = TruthValue
_ContelecVLFTXArcTeeNetVario1Test_Object = MibScalar
contelecVLFTXArcTeeNetVario1Test = _ContelecVLFTXArcTeeNetVario1Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 73),
    _ContelecVLFTXArcTeeNetVario1Test_Type()
)
contelecVLFTXArcTeeNetVario1Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXArcTeeNetVario1Test.setStatus("current")
_ContelecVLFTXArcTeeNetVario2Test_Type = TruthValue
_ContelecVLFTXArcTeeNetVario2Test_Object = MibScalar
contelecVLFTXArcTeeNetVario2Test = _ContelecVLFTXArcTeeNetVario2Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 74),
    _ContelecVLFTXArcTeeNetVario2Test_Type()
)
contelecVLFTXArcTeeNetVario2Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXArcTeeNetVario2Test.setStatus("current")
_ContelecVLFTXArcTeeNetCapTest_Type = TruthValue
_ContelecVLFTXArcTeeNetCapTest_Object = MibScalar
contelecVLFTXArcTeeNetCapTest = _ContelecVLFTXArcTeeNetCapTest_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 75),
    _ContelecVLFTXArcTeeNetCapTest_Type()
)
contelecVLFTXArcTeeNetCapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXArcTeeNetCapTest.setStatus("current")


class _ContelecVLFTXAntennaCurrentMagnitude_Type(Integer32):
    """Custom type contelecVLFTXAntennaCurrentMagnitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ContelecVLFTXAntennaCurrentMagnitude_Type.__name__ = "Integer32"
_ContelecVLFTXAntennaCurrentMagnitude_Object = MibScalar
contelecVLFTXAntennaCurrentMagnitude = _ContelecVLFTXAntennaCurrentMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 76),
    _ContelecVLFTXAntennaCurrentMagnitude_Type()
)
contelecVLFTXAntennaCurrentMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAntennaCurrentMagnitude.setStatus("current")


class _ContelecVLFTXAntennaCurrentPhase_Type(Integer32):
    """Custom type contelecVLFTXAntennaCurrentPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_ContelecVLFTXAntennaCurrentPhase_Type.__name__ = "Integer32"
_ContelecVLFTXAntennaCurrentPhase_Object = MibScalar
contelecVLFTXAntennaCurrentPhase = _ContelecVLFTXAntennaCurrentPhase_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 77),
    _ContelecVLFTXAntennaCurrentPhase_Type()
)
contelecVLFTXAntennaCurrentPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAntennaCurrentPhase.setStatus("current")
_ContelecVLFTXConnectedToDummyLoad_Type = TruthValue
_ContelecVLFTXConnectedToDummyLoad_Object = MibScalar
contelecVLFTXConnectedToDummyLoad = _ContelecVLFTXConnectedToDummyLoad_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 78),
    _ContelecVLFTXConnectedToDummyLoad_Type()
)
contelecVLFTXConnectedToDummyLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXConnectedToDummyLoad.setStatus("current")
_ContelecVLFTXGroundSwitchStatus_Type = TruthValue
_ContelecVLFTXGroundSwitchStatus_Object = MibScalar
contelecVLFTXGroundSwitchStatus = _ContelecVLFTXGroundSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 79),
    _ContelecVLFTXGroundSwitchStatus_Type()
)
contelecVLFTXGroundSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXGroundSwitchStatus.setStatus("current")


class _ContelecVLFTXSupplyTemperature_Type(Integer32):
    """Custom type contelecVLFTXSupplyTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 1000),
    )


_ContelecVLFTXSupplyTemperature_Type.__name__ = "Integer32"
_ContelecVLFTXSupplyTemperature_Object = MibScalar
contelecVLFTXSupplyTemperature = _ContelecVLFTXSupplyTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 80),
    _ContelecVLFTXSupplyTemperature_Type()
)
contelecVLFTXSupplyTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXSupplyTemperature.setStatus("current")


class _ContelecVLFTXExhaustTemperature_Type(Integer32):
    """Custom type contelecVLFTXExhaustTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 1000),
    )


_ContelecVLFTXExhaustTemperature_Type.__name__ = "Integer32"
_ContelecVLFTXExhaustTemperature_Object = MibScalar
contelecVLFTXExhaustTemperature = _ContelecVLFTXExhaustTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 81),
    _ContelecVLFTXExhaustTemperature_Type()
)
contelecVLFTXExhaustTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXExhaustTemperature.setStatus("current")
_ContelecVLFTXHours_Type = Integer32
_ContelecVLFTXHours_Object = MibScalar
contelecVLFTXHours = _ContelecVLFTXHours_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 82),
    _ContelecVLFTXHours_Type()
)
contelecVLFTXHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXHours.setStatus("current")
_ContelecVLFTXDateAndTime_Type = DateAndTime
_ContelecVLFTXDateAndTime_Object = MibScalar
contelecVLFTXDateAndTime = _ContelecVLFTXDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 83),
    _ContelecVLFTXDateAndTime_Type()
)
contelecVLFTXDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXDateAndTime.setStatus("current")
_ContelecVLFTXHardwareVersion_Type = OctetString
_ContelecVLFTXHardwareVersion_Object = MibScalar
contelecVLFTXHardwareVersion = _ContelecVLFTXHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 84),
    _ContelecVLFTXHardwareVersion_Type()
)
contelecVLFTXHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXHardwareVersion.setStatus("current")
_ContelecVLFTXSoftwareVersion_Type = OctetString
_ContelecVLFTXSoftwareVersion_Object = MibScalar
contelecVLFTXSoftwareVersion = _ContelecVLFTXSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 85),
    _ContelecVLFTXSoftwareVersion_Type()
)
contelecVLFTXSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXSoftwareVersion.setStatus("current")
_ContelecVLFTXSummaryFault_Type = TruthValue
_ContelecVLFTXSummaryFault_Object = MibScalar
contelecVLFTXSummaryFault = _ContelecVLFTXSummaryFault_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 86),
    _ContelecVLFTXSummaryFault_Type()
)
contelecVLFTXSummaryFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXSummaryFault.setStatus("current")
_ContelecVLFTXFaultResetCmd_Type = TruthValue
_ContelecVLFTXFaultResetCmd_Object = MibScalar
contelecVLFTXFaultResetCmd = _ContelecVLFTXFaultResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 87),
    _ContelecVLFTXFaultResetCmd_Type()
)
contelecVLFTXFaultResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXFaultResetCmd.setStatus("current")
_ContelecVLFTXOperate_Type = TruthValue
_ContelecVLFTXOperate_Object = MibScalar
contelecVLFTXOperate = _ContelecVLFTXOperate_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 88),
    _ContelecVLFTXOperate_Type()
)
contelecVLFTXOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXOperate.setStatus("current")
_ContelecVLFTXOperateStatus_Type = TruthValue
_ContelecVLFTXOperateStatus_Object = MibScalar
contelecVLFTXOperateStatus = _ContelecVLFTXOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 89),
    _ContelecVLFTXOperateStatus_Type()
)
contelecVLFTXOperateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXOperateStatus.setStatus("current")
_ContelecVLFTXDCOn_Type = TruthValue
_ContelecVLFTXDCOn_Object = MibScalar
contelecVLFTXDCOn = _ContelecVLFTXDCOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 90),
    _ContelecVLFTXDCOn_Type()
)
contelecVLFTXDCOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXDCOn.setStatus("current")
_ContelecVLFTXDCOnStatus_Type = TruthValue
_ContelecVLFTXDCOnStatus_Object = MibScalar
contelecVLFTXDCOnStatus = _ContelecVLFTXDCOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 91),
    _ContelecVLFTXDCOnStatus_Type()
)
contelecVLFTXDCOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXDCOnStatus.setStatus("current")


class _ContelecVLFTXBreakerStatus_Type(Bits):
    """Custom type contelecVLFTXBreakerStatus based on Bits"""
    namedValues = NamedValues(
        *(("txBreaker1Fault", 0),
          ("txBreaker2Fault", 1),
          ("txBreaker3Fault", 2),
          ("txBreaker4Fault", 3),
          ("txBreaker5Fault", 4),
          ("txBreaker6Fault", 5),
          ("txBreaker7Fault", 6),
          ("txBreaker8Fault", 7),
          ("txBreaker9Fault", 8))
    )

_ContelecVLFTXBreakerStatus_Type.__name__ = "Bits"
_ContelecVLFTXBreakerStatus_Object = MibScalar
contelecVLFTXBreakerStatus = _ContelecVLFTXBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 92),
    _ContelecVLFTXBreakerStatus_Type()
)
contelecVLFTXBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXBreakerStatus.setStatus("current")
_ContelecVLFTXContactor_Type = TruthValue
_ContelecVLFTXContactor_Object = MibScalar
contelecVLFTXContactor = _ContelecVLFTXContactor_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 93),
    _ContelecVLFTXContactor_Type()
)
contelecVLFTXContactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXContactor.setStatus("current")
_ContelecVLFTXACOn_Type = TruthValue
_ContelecVLFTXACOn_Object = MibScalar
contelecVLFTXACOn = _ContelecVLFTXACOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 94),
    _ContelecVLFTXACOn_Type()
)
contelecVLFTXACOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXACOn.setStatus("current")
_ContelecVLFTXACOnStatus_Type = TruthValue
_ContelecVLFTXACOnStatus_Object = MibScalar
contelecVLFTXACOnStatus = _ContelecVLFTXACOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 95),
    _ContelecVLFTXACOnStatus_Type()
)
contelecVLFTXACOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXACOnStatus.setStatus("current")
_ContelecVLFTXExternalCoolingIsOn_Type = TruthValue
_ContelecVLFTXExternalCoolingIsOn_Object = MibScalar
contelecVLFTXExternalCoolingIsOn = _ContelecVLFTXExternalCoolingIsOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 96),
    _ContelecVLFTXExternalCoolingIsOn_Type()
)
contelecVLFTXExternalCoolingIsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXExternalCoolingIsOn.setStatus("current")


class _ContelecVLFTXRFLevelControlInput_Type(Integer32):
    """Custom type contelecVLFTXRFLevelControlInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXRFLevelControlInput_Type.__name__ = "Integer32"
_ContelecVLFTXRFLevelControlInput_Object = MibScalar
contelecVLFTXRFLevelControlInput = _ContelecVLFTXRFLevelControlInput_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 97),
    _ContelecVLFTXRFLevelControlInput_Type()
)
contelecVLFTXRFLevelControlInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXRFLevelControlInput.setStatus("current")


class _ContelecVLFTXPALevelPercentPower_Type(Integer32):
    """Custom type contelecVLFTXPALevelPercentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXPALevelPercentPower_Type.__name__ = "Integer32"
_ContelecVLFTXPALevelPercentPower_Object = MibScalar
contelecVLFTXPALevelPercentPower = _ContelecVLFTXPALevelPercentPower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 98),
    _ContelecVLFTXPALevelPercentPower_Type()
)
contelecVLFTXPALevelPercentPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXPALevelPercentPower.setStatus("current")
_ContelecVLFTXRemoteLocalStatus_Type = TruthValue
_ContelecVLFTXRemoteLocalStatus_Object = MibScalar
contelecVLFTXRemoteLocalStatus = _ContelecVLFTXRemoteLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 99),
    _ContelecVLFTXRemoteLocalStatus_Type()
)
contelecVLFTXRemoteLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXRemoteLocalStatus.setStatus("current")


class _ContelecVLFTXAntSampleClipStatus_Type(Bits):
    """Custom type contelecVLFTXAntSampleClipStatus based on Bits"""
    namedValues = NamedValues(
        *(("ant11Clip", 0),
          ("ant12Clip", 1),
          ("ant13Clip", 2),
          ("ant14Clip", 3),
          ("ant21Clip", 4),
          ("ant22Clip", 5),
          ("ant23Clip", 6),
          ("ant24Clip", 7))
    )

_ContelecVLFTXAntSampleClipStatus_Type.__name__ = "Bits"
_ContelecVLFTXAntSampleClipStatus_Object = MibScalar
contelecVLFTXAntSampleClipStatus = _ContelecVLFTXAntSampleClipStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 100),
    _ContelecVLFTXAntSampleClipStatus_Type()
)
contelecVLFTXAntSampleClipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAntSampleClipStatus.setStatus("current")


class _ContelecVLFTXAntSampleLowLevelStatus_Type(Bits):
    """Custom type contelecVLFTXAntSampleLowLevelStatus based on Bits"""
    namedValues = NamedValues(
        *(("ant11LowLevel", 0),
          ("ant12LowLevel", 1),
          ("ant13LowLevel", 2),
          ("ant14LowLevel", 3),
          ("ant21LowLevel", 4),
          ("ant22LowLevel", 5),
          ("ant23LowLevel", 6),
          ("ant24LowLevel", 7))
    )

_ContelecVLFTXAntSampleLowLevelStatus_Type.__name__ = "Bits"
_ContelecVLFTXAntSampleLowLevelStatus_Object = MibScalar
contelecVLFTXAntSampleLowLevelStatus = _ContelecVLFTXAntSampleLowLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 101),
    _ContelecVLFTXAntSampleLowLevelStatus_Type()
)
contelecVLFTXAntSampleLowLevelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAntSampleLowLevelStatus.setStatus("current")


class _ContelecVLFTXAnt11SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt11SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt11SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt11SampleInputLevel_Object = MibScalar
contelecVLFTXAnt11SampleInputLevel = _ContelecVLFTXAnt11SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 102),
    _ContelecVLFTXAnt11SampleInputLevel_Type()
)
contelecVLFTXAnt11SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt11SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt12SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt12SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt12SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt12SampleInputLevel_Object = MibScalar
contelecVLFTXAnt12SampleInputLevel = _ContelecVLFTXAnt12SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 103),
    _ContelecVLFTXAnt12SampleInputLevel_Type()
)
contelecVLFTXAnt12SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt12SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt13SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt13SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt13SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt13SampleInputLevel_Object = MibScalar
contelecVLFTXAnt13SampleInputLevel = _ContelecVLFTXAnt13SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 104),
    _ContelecVLFTXAnt13SampleInputLevel_Type()
)
contelecVLFTXAnt13SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt13SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt14SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt14SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt14SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt14SampleInputLevel_Object = MibScalar
contelecVLFTXAnt14SampleInputLevel = _ContelecVLFTXAnt14SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 105),
    _ContelecVLFTXAnt14SampleInputLevel_Type()
)
contelecVLFTXAnt14SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt14SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt21SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt21SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt21SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt21SampleInputLevel_Object = MibScalar
contelecVLFTXAnt21SampleInputLevel = _ContelecVLFTXAnt21SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 106),
    _ContelecVLFTXAnt21SampleInputLevel_Type()
)
contelecVLFTXAnt21SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt21SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt22SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt22SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt22SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt22SampleInputLevel_Object = MibScalar
contelecVLFTXAnt22SampleInputLevel = _ContelecVLFTXAnt22SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 107),
    _ContelecVLFTXAnt22SampleInputLevel_Type()
)
contelecVLFTXAnt22SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt22SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt23SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt23SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt23SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt23SampleInputLevel_Object = MibScalar
contelecVLFTXAnt23SampleInputLevel = _ContelecVLFTXAnt23SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 108),
    _ContelecVLFTXAnt23SampleInputLevel_Type()
)
contelecVLFTXAnt23SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt23SampleInputLevel.setStatus("current")


class _ContelecVLFTXAnt24SampleInputLevel_Type(Integer32):
    """Custom type contelecVLFTXAnt24SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFTXAnt24SampleInputLevel_Type.__name__ = "Integer32"
_ContelecVLFTXAnt24SampleInputLevel_Object = MibScalar
contelecVLFTXAnt24SampleInputLevel = _ContelecVLFTXAnt24SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 109),
    _ContelecVLFTXAnt24SampleInputLevel_Type()
)
contelecVLFTXAnt24SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFTXAnt24SampleInputLevel.setStatus("current")


class _ContelecVLFTXTxCtrlVLFEQ_Type(Integer32):
    """Custom type contelecVLFTXTxCtrlVLFEQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ContelecVLFTXTxCtrlVLFEQ_Type.__name__ = "Integer32"
_ContelecVLFTXTxCtrlVLFEQ_Object = MibScalar
contelecVLFTXTxCtrlVLFEQ = _ContelecVLFTXTxCtrlVLFEQ_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 1, 110),
    _ContelecVLFTXTxCtrlVLFEQ_Type()
)
contelecVLFTXTxCtrlVLFEQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFTXTxCtrlVLFEQ.setStatus("current")

# Managed Objects groups

contelecVLFTXGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 2, 1)
)
contelecVLFTXGroup.setObjects(
      *(("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXFrequency"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXEQControl"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCCORiseTime"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCCOFallTime"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXA1ARiseTime"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXA1AFallTime"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModulationType"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXEQNLOOP"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXEQConverge"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXRFVInputScale"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXRampDelayOff"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXRampDelayOn"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModRFInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModRFClip"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowRFDrive"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModIntSineWave"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAdaptiveStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXOutputPower"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXReflectedPower"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXImpedanceReal"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXImpedanceImag"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVSWR"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXS11Real"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXS11Imag"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXPARFCurrent"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCombinerCurrentSetPointTrip"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXOutputRFCurrent"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXOutputRFCurrentSetPointTrip"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXSNR"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXTSPLoopStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAntennaReverseInterlock"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXPACab1Doors"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXPACab2Doors"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXTeeNetCab1Doors"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXTeeNetCab2Doors"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCVoltagePA1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCVoltagePA2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAverageDCVoltage"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCCurrentPA1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCCurrentPA2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXTotalDCCurrent"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCVoltageTripLevelLow"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCVoltageTripLevelHigh"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCCurrentTripLevelLow"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCCurrentTripLevelHigh"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCPowerSupplyTempStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowLevelSuppliesPA1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowLevelSuppliesPA2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXPAPhase"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModuleStatus1PA1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModuleStatus2PA1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModuleStatus1PA2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModuleStatus2PA2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModuleResetCmd"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVariometer1PosnSet"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVariometer2PosnSet"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCapacitorPosnSet"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVariometer1PosnStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVariometer2PosnStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCapacitorPosnStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVariometer1ServoStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXVariometer2ServoStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCapacitorServoStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCapacitorSwSet"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCapacitorSwStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcPACab1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcPACab2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcTeeNetVario1"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcTeeNetVario2"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcTeeNetCap"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcPACab1Test"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcPACab2Test"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcTeeNetVario1Test"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcTeeNetVario2Test"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcTeeNetCapTest"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAntennaCurrentMagnitude"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAntennaCurrentPhase"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXConnectedToDummyLoad"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXGroundSwitchStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXSupplyTemperature"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXExhaustTemperature"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXHours"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDateAndTime"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXHardwareVersion"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXSoftwareVersion"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXSummaryFault"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXFaultResetCmd"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXOperate"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXOperateStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCOn"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDCOnStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXBreakerStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXContactor"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXACOn"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXACOnStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXExternalCoolingIsOn"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXRFLevelControlInput"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXPALevelPercentPower"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXRemoteLocalStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAntSampleClipStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAntSampleLowLevelStatus"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt11SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt12SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt13SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt14SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt21SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt22SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt23SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAnt24SampleInputLevel"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXTxCtrlVLFEQ"))
)
if mibBuilder.loadTexts:
    contelecVLFTXGroup.setStatus("current")


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 1)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        "current"
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 2)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        "current"
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 3)
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        "current"
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 4)
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "current"
    )

contelecVLFTXAdaptiveCorrectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 5)
)
if mibBuilder.loadTexts:
    contelecVLFTXAdaptiveCorrectionFault.setStatus(
        "current"
    )

contelecVLFTXLowRFDriveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 6)
)
if mibBuilder.loadTexts:
    contelecVLFTXLowRFDriveAlarm.setStatus(
        "current"
    )

contelecVLFTXModRFClipAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 7)
)
if mibBuilder.loadTexts:
    contelecVLFTXModRFClipAlarm.setStatus(
        "current"
    )

contelecVLFTXLowAntennaCurrentFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 8)
)
if mibBuilder.loadTexts:
    contelecVLFTXLowAntennaCurrentFault.setStatus(
        "current"
    )

contelecVLFTXWarnHighDCCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 9)
)
if mibBuilder.loadTexts:
    contelecVLFTXWarnHighDCCurrentAlarm.setStatus(
        "current"
    )

contelecVLFTXFaultHighDCCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 10)
)
if mibBuilder.loadTexts:
    contelecVLFTXFaultHighDCCurrentAlarm.setStatus(
        "current"
    )

contelecVLFTXFaultDCPowerSupplyTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 11)
)
if mibBuilder.loadTexts:
    contelecVLFTXFaultDCPowerSupplyTempAlarm.setStatus(
        "current"
    )

contelecVLFTXWarnHighVoltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 12)
)
if mibBuilder.loadTexts:
    contelecVLFTXWarnHighVoltageAlarm.setStatus(
        "current"
    )

contelecVLFTXFaultHighVoltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 13)
)
if mibBuilder.loadTexts:
    contelecVLFTXFaultHighVoltageAlarm.setStatus(
        "current"
    )

contelecVLFTXModuleFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 14)
)
if mibBuilder.loadTexts:
    contelecVLFTXModuleFaultAlarm.setStatus(
        "current"
    )

contelecVLFTXArcAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 15)
)
if mibBuilder.loadTexts:
    contelecVLFTXArcAlarm.setStatus(
        "current"
    )

contelecVLFTXDoorInterlockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 16)
)
if mibBuilder.loadTexts:
    contelecVLFTXDoorInterlockAlarm.setStatus(
        "current"
    )

contelecVLFTXCardInterlockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 17)
)
if mibBuilder.loadTexts:
    contelecVLFTXCardInterlockAlarm.setStatus(
        "current"
    )

contelecVLFTXGroundRelayInterlockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 18)
)
if mibBuilder.loadTexts:
    contelecVLFTXGroundRelayInterlockAlarm.setStatus(
        "current"
    )

contelecVLFTXLowLevelSuppliesPA1LimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 19)
)
if mibBuilder.loadTexts:
    contelecVLFTXLowLevelSuppliesPA1LimitExceeded.setStatus(
        "current"
    )

contelecVLFTXLowLevelSuppliesPA2LimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 20)
)
if mibBuilder.loadTexts:
    contelecVLFTXLowLevelSuppliesPA2LimitExceeded.setStatus(
        "current"
    )

contelecVLFTXAntennaCurrentClip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 21)
)
if mibBuilder.loadTexts:
    contelecVLFTXAntennaCurrentClip.setStatus(
        "current"
    )

contelecVLFTXCombinerCurrentTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 22)
)
if mibBuilder.loadTexts:
    contelecVLFTXCombinerCurrentTrip.setStatus(
        "current"
    )

contelecVLFTXOutputCurrentTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 3, 0, 23)
)
if mibBuilder.loadTexts:
    contelecVLFTXOutputCurrentTrip.setStatus(
        "current"
    )


# Notifications groups

contelecVLFTXNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 2, 2)
)
contelecVLFTXNotificationGroup.setObjects(
      *(("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "coldStart"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "warmStart"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "linkDown"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "linkUp"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAdaptiveCorrectionFault"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowRFDriveAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModRFClipAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowAntennaCurrentFault"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXWarnHighDCCurrentAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXFaultHighDCCurrentAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXFaultDCPowerSupplyTempAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXWarnHighVoltageAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXFaultHighVoltageAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXModuleFaultAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXArcAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXDoorInterlockAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCardInterlockAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXGroundRelayInterlockAlarm"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowLevelSuppliesPA1LimitExceeded"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXLowLevelSuppliesPA2LimitExceeded"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXAntennaCurrentClip"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXCombinerCurrentTrip"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXOutputCurrentTrip"))
)
if mibBuilder.loadTexts:
    contelecVLFTXNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

contelecVLFTXCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 1, 1)
)
contelecVLFTXCompliance.setObjects(
      *(("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXGroup"),
        ("CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB", "contelecVLFTXNotificationGroup"))
)
if mibBuilder.loadTexts:
    contelecVLFTXCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTELEC-CLEAR-LAKE-TRANSMITTER-MIB",
    **{"contelecVLFTransmitter": contelecVLFTransmitter,
       "contelecVLFTXConformance": contelecVLFTXConformance,
       "contelecVLFTXCompliances": contelecVLFTXCompliances,
       "contelecVLFTXCompliance": contelecVLFTXCompliance,
       "contelecVLFTXGroups": contelecVLFTXGroups,
       "contelecVLFTXGroup": contelecVLFTXGroup,
       "contelecVLFTXNotificationGroup": contelecVLFTXNotificationGroup,
       "contelecVLFTXobject": contelecVLFTXobject,
       "contelecVLFTXTraps": contelecVLFTXTraps,
       "coldStart": coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "contelecVLFTXAdaptiveCorrectionFault": contelecVLFTXAdaptiveCorrectionFault,
       "contelecVLFTXLowRFDriveAlarm": contelecVLFTXLowRFDriveAlarm,
       "contelecVLFTXModRFClipAlarm": contelecVLFTXModRFClipAlarm,
       "contelecVLFTXLowAntennaCurrentFault": contelecVLFTXLowAntennaCurrentFault,
       "contelecVLFTXWarnHighDCCurrentAlarm": contelecVLFTXWarnHighDCCurrentAlarm,
       "contelecVLFTXFaultHighDCCurrentAlarm": contelecVLFTXFaultHighDCCurrentAlarm,
       "contelecVLFTXFaultDCPowerSupplyTempAlarm": contelecVLFTXFaultDCPowerSupplyTempAlarm,
       "contelecVLFTXWarnHighVoltageAlarm": contelecVLFTXWarnHighVoltageAlarm,
       "contelecVLFTXFaultHighVoltageAlarm": contelecVLFTXFaultHighVoltageAlarm,
       "contelecVLFTXModuleFaultAlarm": contelecVLFTXModuleFaultAlarm,
       "contelecVLFTXArcAlarm": contelecVLFTXArcAlarm,
       "contelecVLFTXDoorInterlockAlarm": contelecVLFTXDoorInterlockAlarm,
       "contelecVLFTXCardInterlockAlarm": contelecVLFTXCardInterlockAlarm,
       "contelecVLFTXGroundRelayInterlockAlarm": contelecVLFTXGroundRelayInterlockAlarm,
       "contelecVLFTXLowLevelSuppliesPA1LimitExceeded": contelecVLFTXLowLevelSuppliesPA1LimitExceeded,
       "contelecVLFTXLowLevelSuppliesPA2LimitExceeded": contelecVLFTXLowLevelSuppliesPA2LimitExceeded,
       "contelecVLFTXAntennaCurrentClip": contelecVLFTXAntennaCurrentClip,
       "contelecVLFTXCombinerCurrentTrip": contelecVLFTXCombinerCurrentTrip,
       "contelecVLFTXOutputCurrentTrip": contelecVLFTXOutputCurrentTrip,
       "contelecVLFTXSpecs": contelecVLFTXSpecs,
       "contelecVLFTXFrequency": contelecVLFTXFrequency,
       "contelecVLFTXEQControl": contelecVLFTXEQControl,
       "contelecVLFTXCCORiseTime": contelecVLFTXCCORiseTime,
       "contelecVLFTXCCOFallTime": contelecVLFTXCCOFallTime,
       "contelecVLFTXA1ARiseTime": contelecVLFTXA1ARiseTime,
       "contelecVLFTXA1AFallTime": contelecVLFTXA1AFallTime,
       "contelecVLFTXModulationType": contelecVLFTXModulationType,
       "contelecVLFTXEQNLOOP": contelecVLFTXEQNLOOP,
       "contelecVLFTXEQConverge": contelecVLFTXEQConverge,
       "contelecVLFTXRFVInputScale": contelecVLFTXRFVInputScale,
       "contelecVLFTXRampDelayOff": contelecVLFTXRampDelayOff,
       "contelecVLFTXRampDelayOn": contelecVLFTXRampDelayOn,
       "contelecVLFTXModRFInputLevel": contelecVLFTXModRFInputLevel,
       "contelecVLFTXModRFClip": contelecVLFTXModRFClip,
       "contelecVLFTXLowRFDrive": contelecVLFTXLowRFDrive,
       "contelecVLFTXModIntSineWave": contelecVLFTXModIntSineWave,
       "contelecVLFTXAdaptiveStatus": contelecVLFTXAdaptiveStatus,
       "contelecVLFTXOutputPower": contelecVLFTXOutputPower,
       "contelecVLFTXReflectedPower": contelecVLFTXReflectedPower,
       "contelecVLFTXImpedanceReal": contelecVLFTXImpedanceReal,
       "contelecVLFTXImpedanceImag": contelecVLFTXImpedanceImag,
       "contelecVLFTXVSWR": contelecVLFTXVSWR,
       "contelecVLFTXS11Real": contelecVLFTXS11Real,
       "contelecVLFTXS11Imag": contelecVLFTXS11Imag,
       "contelecVLFTXPARFCurrent": contelecVLFTXPARFCurrent,
       "contelecVLFTXCombinerCurrentSetPointTrip": contelecVLFTXCombinerCurrentSetPointTrip,
       "contelecVLFTXOutputRFCurrent": contelecVLFTXOutputRFCurrent,
       "contelecVLFTXOutputRFCurrentSetPointTrip": contelecVLFTXOutputRFCurrentSetPointTrip,
       "contelecVLFTXSNR": contelecVLFTXSNR,
       "contelecVLFTXTSPLoopStatus": contelecVLFTXTSPLoopStatus,
       "contelecVLFTXAntennaReverseInterlock": contelecVLFTXAntennaReverseInterlock,
       "contelecVLFTXPACab1Doors": contelecVLFTXPACab1Doors,
       "contelecVLFTXPACab2Doors": contelecVLFTXPACab2Doors,
       "contelecVLFTXTeeNetCab1Doors": contelecVLFTXTeeNetCab1Doors,
       "contelecVLFTXTeeNetCab2Doors": contelecVLFTXTeeNetCab2Doors,
       "contelecVLFTXDCVoltagePA1": contelecVLFTXDCVoltagePA1,
       "contelecVLFTXDCVoltagePA2": contelecVLFTXDCVoltagePA2,
       "contelecVLFTXAverageDCVoltage": contelecVLFTXAverageDCVoltage,
       "contelecVLFTXDCCurrentPA1": contelecVLFTXDCCurrentPA1,
       "contelecVLFTXDCCurrentPA2": contelecVLFTXDCCurrentPA2,
       "contelecVLFTXTotalDCCurrent": contelecVLFTXTotalDCCurrent,
       "contelecVLFTXDCVoltageTripLevelLow": contelecVLFTXDCVoltageTripLevelLow,
       "contelecVLFTXDCVoltageTripLevelHigh": contelecVLFTXDCVoltageTripLevelHigh,
       "contelecVLFTXDCCurrentTripLevelLow": contelecVLFTXDCCurrentTripLevelLow,
       "contelecVLFTXDCCurrentTripLevelHigh": contelecVLFTXDCCurrentTripLevelHigh,
       "contelecVLFTXDCPowerSupplyTempStatus": contelecVLFTXDCPowerSupplyTempStatus,
       "contelecVLFTXLowLevelSuppliesPA1": contelecVLFTXLowLevelSuppliesPA1,
       "contelecVLFTXLowLevelSuppliesPA2": contelecVLFTXLowLevelSuppliesPA2,
       "contelecVLFTXPAPhase": contelecVLFTXPAPhase,
       "contelecVLFTXModuleStatus1PA1": contelecVLFTXModuleStatus1PA1,
       "contelecVLFTXModuleStatus2PA1": contelecVLFTXModuleStatus2PA1,
       "contelecVLFTXModuleStatus1PA2": contelecVLFTXModuleStatus1PA2,
       "contelecVLFTXModuleStatus2PA2": contelecVLFTXModuleStatus2PA2,
       "contelecVLFTXModuleResetCmd": contelecVLFTXModuleResetCmd,
       "contelecVLFTXVariometer1PosnSet": contelecVLFTXVariometer1PosnSet,
       "contelecVLFTXVariometer2PosnSet": contelecVLFTXVariometer2PosnSet,
       "contelecVLFTXCapacitorPosnSet": contelecVLFTXCapacitorPosnSet,
       "contelecVLFTXVariometer1PosnStatus": contelecVLFTXVariometer1PosnStatus,
       "contelecVLFTXVariometer2PosnStatus": contelecVLFTXVariometer2PosnStatus,
       "contelecVLFTXCapacitorPosnStatus": contelecVLFTXCapacitorPosnStatus,
       "contelecVLFTXVariometer1ServoStatus": contelecVLFTXVariometer1ServoStatus,
       "contelecVLFTXVariometer2ServoStatus": contelecVLFTXVariometer2ServoStatus,
       "contelecVLFTXCapacitorServoStatus": contelecVLFTXCapacitorServoStatus,
       "contelecVLFTXCapacitorSwSet": contelecVLFTXCapacitorSwSet,
       "contelecVLFTXCapacitorSwStatus": contelecVLFTXCapacitorSwStatus,
       "contelecVLFTXArcPACab1": contelecVLFTXArcPACab1,
       "contelecVLFTXArcPACab2": contelecVLFTXArcPACab2,
       "contelecVLFTXArcTeeNetVario1": contelecVLFTXArcTeeNetVario1,
       "contelecVLFTXArcTeeNetVario2": contelecVLFTXArcTeeNetVario2,
       "contelecVLFTXArcTeeNetCap": contelecVLFTXArcTeeNetCap,
       "contelecVLFTXArcPACab1Test": contelecVLFTXArcPACab1Test,
       "contelecVLFTXArcPACab2Test": contelecVLFTXArcPACab2Test,
       "contelecVLFTXArcTeeNetVario1Test": contelecVLFTXArcTeeNetVario1Test,
       "contelecVLFTXArcTeeNetVario2Test": contelecVLFTXArcTeeNetVario2Test,
       "contelecVLFTXArcTeeNetCapTest": contelecVLFTXArcTeeNetCapTest,
       "contelecVLFTXAntennaCurrentMagnitude": contelecVLFTXAntennaCurrentMagnitude,
       "contelecVLFTXAntennaCurrentPhase": contelecVLFTXAntennaCurrentPhase,
       "contelecVLFTXConnectedToDummyLoad": contelecVLFTXConnectedToDummyLoad,
       "contelecVLFTXGroundSwitchStatus": contelecVLFTXGroundSwitchStatus,
       "contelecVLFTXSupplyTemperature": contelecVLFTXSupplyTemperature,
       "contelecVLFTXExhaustTemperature": contelecVLFTXExhaustTemperature,
       "contelecVLFTXHours": contelecVLFTXHours,
       "contelecVLFTXDateAndTime": contelecVLFTXDateAndTime,
       "contelecVLFTXHardwareVersion": contelecVLFTXHardwareVersion,
       "contelecVLFTXSoftwareVersion": contelecVLFTXSoftwareVersion,
       "contelecVLFTXSummaryFault": contelecVLFTXSummaryFault,
       "contelecVLFTXFaultResetCmd": contelecVLFTXFaultResetCmd,
       "contelecVLFTXOperate": contelecVLFTXOperate,
       "contelecVLFTXOperateStatus": contelecVLFTXOperateStatus,
       "contelecVLFTXDCOn": contelecVLFTXDCOn,
       "contelecVLFTXDCOnStatus": contelecVLFTXDCOnStatus,
       "contelecVLFTXBreakerStatus": contelecVLFTXBreakerStatus,
       "contelecVLFTXContactor": contelecVLFTXContactor,
       "contelecVLFTXACOn": contelecVLFTXACOn,
       "contelecVLFTXACOnStatus": contelecVLFTXACOnStatus,
       "contelecVLFTXExternalCoolingIsOn": contelecVLFTXExternalCoolingIsOn,
       "contelecVLFTXRFLevelControlInput": contelecVLFTXRFLevelControlInput,
       "contelecVLFTXPALevelPercentPower": contelecVLFTXPALevelPercentPower,
       "contelecVLFTXRemoteLocalStatus": contelecVLFTXRemoteLocalStatus,
       "contelecVLFTXAntSampleClipStatus": contelecVLFTXAntSampleClipStatus,
       "contelecVLFTXAntSampleLowLevelStatus": contelecVLFTXAntSampleLowLevelStatus,
       "contelecVLFTXAnt11SampleInputLevel": contelecVLFTXAnt11SampleInputLevel,
       "contelecVLFTXAnt12SampleInputLevel": contelecVLFTXAnt12SampleInputLevel,
       "contelecVLFTXAnt13SampleInputLevel": contelecVLFTXAnt13SampleInputLevel,
       "contelecVLFTXAnt14SampleInputLevel": contelecVLFTXAnt14SampleInputLevel,
       "contelecVLFTXAnt21SampleInputLevel": contelecVLFTXAnt21SampleInputLevel,
       "contelecVLFTXAnt22SampleInputLevel": contelecVLFTXAnt22SampleInputLevel,
       "contelecVLFTXAnt23SampleInputLevel": contelecVLFTXAnt23SampleInputLevel,
       "contelecVLFTXAnt24SampleInputLevel": contelecVLFTXAnt24SampleInputLevel,
       "contelecVLFTXTxCtrlVLFEQ": contelecVLFTXTxCtrlVLFEQ}
)
