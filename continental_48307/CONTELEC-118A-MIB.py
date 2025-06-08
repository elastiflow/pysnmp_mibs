# SNMP MIB module (CONTELEC-118A-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/continental_48307/CONTELEC-118A-MIB.mib
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

(contelec,) = mibBuilder.importSymbols(
    "CONTELEC-COMMON-MIB",
    "contelec")

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

contelec118A = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2)
)
if mibBuilder.loadTexts:
    contelec118A.setRevisions(
        ("2017-09-06 10:46",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cec118AConformance_ObjectIdentity = ObjectIdentity
cec118AConformance = _Cec118AConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2, 2)
)
_Cec118ACompliances_ObjectIdentity = ObjectIdentity
cec118ACompliances = _Cec118ACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2, 2, 1)
)
_Cec118AGroups_ObjectIdentity = ObjectIdentity
cec118AGroups = _Cec118AGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2, 2, 2)
)
_Cec118Aobject_ObjectIdentity = ObjectIdentity
cec118Aobject = _Cec118Aobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3)
)
_Cec118ATraps_ObjectIdentity = ObjectIdentity
cec118ATraps = _Cec118ATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0)
)
_Cec118ASpecs_ObjectIdentity = ObjectIdentity
cec118ASpecs = _Cec118ASpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1)
)


class _Cec118AFrequency_Type(Integer32):
    """Custom type cec118AFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14000, 50000),
    )


_Cec118AFrequency_Type.__name__ = "Integer32"
_Cec118AFrequency_Object = MibScalar
cec118AFrequency = _Cec118AFrequency_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 1),
    _Cec118AFrequency_Type()
)
cec118AFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AFrequency.setStatus("current")
_Cec118AEQControl_Type = TruthValue
_Cec118AEQControl_Object = MibScalar
cec118AEQControl = _Cec118AEQControl_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 2),
    _Cec118AEQControl_Type()
)
cec118AEQControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AEQControl.setStatus("current")
_Cec118AEQReset_Type = TruthValue
_Cec118AEQReset_Object = MibScalar
cec118AEQReset = _Cec118AEQReset_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 3),
    _Cec118AEQReset_Type()
)
cec118AEQReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AEQReset.setStatus("current")


class _Cec118ACCORiseTime_Type(Unsigned32):
    """Custom type cec118ACCORiseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cec118ACCORiseTime_Type.__name__ = "Unsigned32"
_Cec118ACCORiseTime_Object = MibScalar
cec118ACCORiseTime = _Cec118ACCORiseTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 4),
    _Cec118ACCORiseTime_Type()
)
cec118ACCORiseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ACCORiseTime.setStatus("current")


class _Cec118ACCOFallTime_Type(Unsigned32):
    """Custom type cec118ACCOFallTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cec118ACCOFallTime_Type.__name__ = "Unsigned32"
_Cec118ACCOFallTime_Object = MibScalar
cec118ACCOFallTime = _Cec118ACCOFallTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 5),
    _Cec118ACCOFallTime_Type()
)
cec118ACCOFallTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ACCOFallTime.setStatus("current")


class _Cec118AA1ARiseTime_Type(Unsigned32):
    """Custom type cec118AA1ARiseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cec118AA1ARiseTime_Type.__name__ = "Unsigned32"
_Cec118AA1ARiseTime_Object = MibScalar
cec118AA1ARiseTime = _Cec118AA1ARiseTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 6),
    _Cec118AA1ARiseTime_Type()
)
cec118AA1ARiseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AA1ARiseTime.setStatus("current")


class _Cec118AA1AFallTime_Type(Unsigned32):
    """Custom type cec118AA1AFallTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cec118AA1AFallTime_Type.__name__ = "Unsigned32"
_Cec118AA1AFallTime_Object = MibScalar
cec118AA1AFallTime = _Cec118AA1AFallTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 7),
    _Cec118AA1AFallTime_Type()
)
cec118AA1AFallTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AA1AFallTime.setStatus("current")
_Cec118AModulationType_Type = TruthValue
_Cec118AModulationType_Object = MibScalar
cec118AModulationType = _Cec118AModulationType_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 8),
    _Cec118AModulationType_Type()
)
cec118AModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AModulationType.setStatus("current")


class _Cec118AEQNLOOP_Type(Unsigned32):
    """Custom type cec118AEQNLOOP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cec118AEQNLOOP_Type.__name__ = "Unsigned32"
_Cec118AEQNLOOP_Object = MibScalar
cec118AEQNLOOP = _Cec118AEQNLOOP_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 9),
    _Cec118AEQNLOOP_Type()
)
cec118AEQNLOOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AEQNLOOP.setStatus("current")


class _Cec118AEQConverge_Type(Integer32):
    """Custom type cec118AEQConverge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 6000),
    )


_Cec118AEQConverge_Type.__name__ = "Integer32"
_Cec118AEQConverge_Object = MibScalar
cec118AEQConverge = _Cec118AEQConverge_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 10),
    _Cec118AEQConverge_Type()
)
cec118AEQConverge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AEQConverge.setStatus("current")


class _Cec118ARFVInputScale_Type(Integer32):
    """Custom type cec118ARFVInputScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Cec118ARFVInputScale_Type.__name__ = "Integer32"
_Cec118ARFVInputScale_Object = MibScalar
cec118ARFVInputScale = _Cec118ARFVInputScale_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 11),
    _Cec118ARFVInputScale_Type()
)
cec118ARFVInputScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ARFVInputScale.setStatus("current")


class _Cec118ARampDelayOff_Type(Unsigned32):
    """Custom type cec118ARampDelayOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cec118ARampDelayOff_Type.__name__ = "Unsigned32"
_Cec118ARampDelayOff_Object = MibScalar
cec118ARampDelayOff = _Cec118ARampDelayOff_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 12),
    _Cec118ARampDelayOff_Type()
)
cec118ARampDelayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ARampDelayOff.setStatus("current")


class _Cec118ARampDelayOn_Type(Unsigned32):
    """Custom type cec118ARampDelayOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cec118ARampDelayOn_Type.__name__ = "Unsigned32"
_Cec118ARampDelayOn_Object = MibScalar
cec118ARampDelayOn = _Cec118ARampDelayOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 13),
    _Cec118ARampDelayOn_Type()
)
cec118ARampDelayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ARampDelayOn.setStatus("current")


class _Cec118AModRFInputLevel_Type(Integer32):
    """Custom type cec118AModRFInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AModRFInputLevel_Type.__name__ = "Integer32"
_Cec118AModRFInputLevel_Object = MibScalar
cec118AModRFInputLevel = _Cec118AModRFInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 14),
    _Cec118AModRFInputLevel_Type()
)
cec118AModRFInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AModRFInputLevel.setStatus("current")
_Cec118AModRFClip_Type = TruthValue
_Cec118AModRFClip_Object = MibScalar
cec118AModRFClip = _Cec118AModRFClip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 15),
    _Cec118AModRFClip_Type()
)
cec118AModRFClip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AModRFClip.setStatus("current")
_Cec118ALowRFDrive_Type = TruthValue
_Cec118ALowRFDrive_Object = MibScalar
cec118ALowRFDrive = _Cec118ALowRFDrive_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 16),
    _Cec118ALowRFDrive_Type()
)
cec118ALowRFDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ALowRFDrive.setStatus("current")
_Cec118AModIntSineWave_Type = TruthValue
_Cec118AModIntSineWave_Object = MibScalar
cec118AModIntSineWave = _Cec118AModIntSineWave_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 17),
    _Cec118AModIntSineWave_Type()
)
cec118AModIntSineWave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AModIntSineWave.setStatus("current")
_Cec118AEqIterCount_Type = Integer32
_Cec118AEqIterCount_Object = MibScalar
cec118AEqIterCount = _Cec118AEqIterCount_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 18),
    _Cec118AEqIterCount_Type()
)
cec118AEqIterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AEqIterCount.setStatus("current")


class _Cec118AAdaptiveStatus_Type(Bits):
    """Custom type cec118AAdaptiveStatus based on Bits"""
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

_Cec118AAdaptiveStatus_Type.__name__ = "Bits"
_Cec118AAdaptiveStatus_Object = MibScalar
cec118AAdaptiveStatus = _Cec118AAdaptiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 19),
    _Cec118AAdaptiveStatus_Type()
)
cec118AAdaptiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAdaptiveStatus.setStatus("current")


class _Cec118AOutputPower_Type(Integer32):
    """Custom type cec118AOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_Cec118AOutputPower_Type.__name__ = "Integer32"
_Cec118AOutputPower_Object = MibScalar
cec118AOutputPower = _Cec118AOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 20),
    _Cec118AOutputPower_Type()
)
cec118AOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AOutputPower.setStatus("current")


class _Cec118AReflectedPower_Type(Integer32):
    """Custom type cec118AReflectedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_Cec118AReflectedPower_Type.__name__ = "Integer32"
_Cec118AReflectedPower_Object = MibScalar
cec118AReflectedPower = _Cec118AReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 21),
    _Cec118AReflectedPower_Type()
)
cec118AReflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AReflectedPower.setStatus("current")


class _Cec118AImpedanceReal_Type(Integer32):
    """Custom type cec118AImpedanceReal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560),
    )


_Cec118AImpedanceReal_Type.__name__ = "Integer32"
_Cec118AImpedanceReal_Object = MibScalar
cec118AImpedanceReal = _Cec118AImpedanceReal_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 22),
    _Cec118AImpedanceReal_Type()
)
cec118AImpedanceReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AImpedanceReal.setStatus("current")


class _Cec118AImpedanceImag_Type(Integer32):
    """Custom type cec118AImpedanceImag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2560, 2560),
    )


_Cec118AImpedanceImag_Type.__name__ = "Integer32"
_Cec118AImpedanceImag_Object = MibScalar
cec118AImpedanceImag = _Cec118AImpedanceImag_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 23),
    _Cec118AImpedanceImag_Type()
)
cec118AImpedanceImag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AImpedanceImag.setStatus("current")


class _Cec118AVSWR_Type(Integer32):
    """Custom type cec118AVSWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cec118AVSWR_Type.__name__ = "Integer32"
_Cec118AVSWR_Object = MibScalar
cec118AVSWR = _Cec118AVSWR_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 24),
    _Cec118AVSWR_Type()
)
cec118AVSWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AVSWR.setStatus("current")
_Cec118AS11Real_Type = Integer32
_Cec118AS11Real_Object = MibScalar
cec118AS11Real = _Cec118AS11Real_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 25),
    _Cec118AS11Real_Type()
)
cec118AS11Real.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AS11Real.setStatus("current")
_Cec118AS11Imag_Type = Integer32
_Cec118AS11Imag_Object = MibScalar
cec118AS11Imag = _Cec118AS11Imag_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 26),
    _Cec118AS11Imag_Type()
)
cec118AS11Imag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AS11Imag.setStatus("current")


class _Cec118APARFCurrent_Type(Integer32):
    """Custom type cec118APARFCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118APARFCurrent_Type.__name__ = "Integer32"
_Cec118APARFCurrent_Object = MibScalar
cec118APARFCurrent = _Cec118APARFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 27),
    _Cec118APARFCurrent_Type()
)
cec118APARFCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118APARFCurrent.setStatus("current")


class _Cec118ACombinerCurrentSetPointTrip_Type(Integer32):
    """Custom type cec118ACombinerCurrentSetPointTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118ACombinerCurrentSetPointTrip_Type.__name__ = "Integer32"
_Cec118ACombinerCurrentSetPointTrip_Object = MibScalar
cec118ACombinerCurrentSetPointTrip = _Cec118ACombinerCurrentSetPointTrip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 28),
    _Cec118ACombinerCurrentSetPointTrip_Type()
)
cec118ACombinerCurrentSetPointTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ACombinerCurrentSetPointTrip.setStatus("current")


class _Cec118AOutputRFCurrent_Type(Integer32):
    """Custom type cec118AOutputRFCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AOutputRFCurrent_Type.__name__ = "Integer32"
_Cec118AOutputRFCurrent_Object = MibScalar
cec118AOutputRFCurrent = _Cec118AOutputRFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 29),
    _Cec118AOutputRFCurrent_Type()
)
cec118AOutputRFCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AOutputRFCurrent.setStatus("current")


class _Cec118AOutputRFCurrentSetPointTrip_Type(Integer32):
    """Custom type cec118AOutputRFCurrentSetPointTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AOutputRFCurrentSetPointTrip_Type.__name__ = "Integer32"
_Cec118AOutputRFCurrentSetPointTrip_Object = MibScalar
cec118AOutputRFCurrentSetPointTrip = _Cec118AOutputRFCurrentSetPointTrip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 30),
    _Cec118AOutputRFCurrentSetPointTrip_Type()
)
cec118AOutputRFCurrentSetPointTrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AOutputRFCurrentSetPointTrip.setStatus("current")


class _Cec118ASNR_Type(Integer32):
    """Custom type cec118ASNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Cec118ASNR_Type.__name__ = "Integer32"
_Cec118ASNR_Object = MibScalar
cec118ASNR = _Cec118ASNR_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 31),
    _Cec118ASNR_Type()
)
cec118ASNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ASNR.setStatus("current")
_Cec118ATSPLoopStatus_Type = TruthValue
_Cec118ATSPLoopStatus_Object = MibScalar
cec118ATSPLoopStatus = _Cec118ATSPLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 32),
    _Cec118ATSPLoopStatus_Type()
)
cec118ATSPLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ATSPLoopStatus.setStatus("current")
_Cec118AAntennaReverseInterlock_Type = TruthValue
_Cec118AAntennaReverseInterlock_Object = MibScalar
cec118AAntennaReverseInterlock = _Cec118AAntennaReverseInterlock_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 33),
    _Cec118AAntennaReverseInterlock_Type()
)
cec118AAntennaReverseInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAntennaReverseInterlock.setStatus("current")
_Cec118APACab1Doors_Type = TruthValue
_Cec118APACab1Doors_Object = MibScalar
cec118APACab1Doors = _Cec118APACab1Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 34),
    _Cec118APACab1Doors_Type()
)
cec118APACab1Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118APACab1Doors.setStatus("current")
_Cec118APACab2Doors_Type = TruthValue
_Cec118APACab2Doors_Object = MibScalar
cec118APACab2Doors = _Cec118APACab2Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 35),
    _Cec118APACab2Doors_Type()
)
cec118APACab2Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118APACab2Doors.setStatus("current")
_Cec118ATeeNetCab1Doors_Type = TruthValue
_Cec118ATeeNetCab1Doors_Object = MibScalar
cec118ATeeNetCab1Doors = _Cec118ATeeNetCab1Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 36),
    _Cec118ATeeNetCab1Doors_Type()
)
cec118ATeeNetCab1Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ATeeNetCab1Doors.setStatus("current")
_Cec118ATeeNetCab2Doors_Type = TruthValue
_Cec118ATeeNetCab2Doors_Object = MibScalar
cec118ATeeNetCab2Doors = _Cec118ATeeNetCab2Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 37),
    _Cec118ATeeNetCab2Doors_Type()
)
cec118ATeeNetCab2Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ATeeNetCab2Doors.setStatus("current")


class _Cec118ADCVoltagePA1_Type(Integer32):
    """Custom type cec118ADCVoltagePA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Cec118ADCVoltagePA1_Type.__name__ = "Integer32"
_Cec118ADCVoltagePA1_Object = MibScalar
cec118ADCVoltagePA1 = _Cec118ADCVoltagePA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 38),
    _Cec118ADCVoltagePA1_Type()
)
cec118ADCVoltagePA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCVoltagePA1.setStatus("current")


class _Cec118ADCVoltagePA2_Type(Integer32):
    """Custom type cec118ADCVoltagePA2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Cec118ADCVoltagePA2_Type.__name__ = "Integer32"
_Cec118ADCVoltagePA2_Object = MibScalar
cec118ADCVoltagePA2 = _Cec118ADCVoltagePA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 39),
    _Cec118ADCVoltagePA2_Type()
)
cec118ADCVoltagePA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCVoltagePA2.setStatus("current")


class _Cec118AAverageDCVoltage_Type(Integer32):
    """Custom type cec118AAverageDCVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Cec118AAverageDCVoltage_Type.__name__ = "Integer32"
_Cec118AAverageDCVoltage_Object = MibScalar
cec118AAverageDCVoltage = _Cec118AAverageDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 40),
    _Cec118AAverageDCVoltage_Type()
)
cec118AAverageDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAverageDCVoltage.setStatus("current")


class _Cec118ADCCurrentPA1_Type(Integer32):
    """Custom type cec118ADCCurrentPA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Cec118ADCCurrentPA1_Type.__name__ = "Integer32"
_Cec118ADCCurrentPA1_Object = MibScalar
cec118ADCCurrentPA1 = _Cec118ADCCurrentPA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 41),
    _Cec118ADCCurrentPA1_Type()
)
cec118ADCCurrentPA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCCurrentPA1.setStatus("current")


class _Cec118ADCCurrentPA2_Type(Integer32):
    """Custom type cec118ADCCurrentPA2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Cec118ADCCurrentPA2_Type.__name__ = "Integer32"
_Cec118ADCCurrentPA2_Object = MibScalar
cec118ADCCurrentPA2 = _Cec118ADCCurrentPA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 42),
    _Cec118ADCCurrentPA2_Type()
)
cec118ADCCurrentPA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCCurrentPA2.setStatus("current")


class _Cec118ATotalDCCurrent_Type(Integer32):
    """Custom type cec118ATotalDCCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cec118ATotalDCCurrent_Type.__name__ = "Integer32"
_Cec118ATotalDCCurrent_Object = MibScalar
cec118ATotalDCCurrent = _Cec118ATotalDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 43),
    _Cec118ATotalDCCurrent_Type()
)
cec118ATotalDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ATotalDCCurrent.setStatus("current")


class _Cec118ADCPowerSupplyTempStatus_Type(Bits):
    """Custom type cec118ADCPowerSupplyTempStatus based on Bits"""
    namedValues = NamedValues(
        *(("ps1OverTemperatureFault", 0),
          ("ps2OverTemperatureFault", 1))
    )

_Cec118ADCPowerSupplyTempStatus_Type.__name__ = "Bits"
_Cec118ADCPowerSupplyTempStatus_Object = MibScalar
cec118ADCPowerSupplyTempStatus = _Cec118ADCPowerSupplyTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 44),
    _Cec118ADCPowerSupplyTempStatus_Type()
)
cec118ADCPowerSupplyTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCPowerSupplyTempStatus.setStatus("current")


class _Cec118AOutputRFVoltage_Type(Integer32):
    """Custom type cec118AOutputRFVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_Cec118AOutputRFVoltage_Type.__name__ = "Integer32"
_Cec118AOutputRFVoltage_Object = MibScalar
cec118AOutputRFVoltage = _Cec118AOutputRFVoltage_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 45),
    _Cec118AOutputRFVoltage_Type()
)
cec118AOutputRFVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AOutputRFVoltage.setStatus("current")


class _Cec118AOutputRFVoltageSetPointTrip_Type(Integer32):
    """Custom type cec118AOutputRFVoltageSetPointTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_Cec118AOutputRFVoltageSetPointTrip_Type.__name__ = "Integer32"
_Cec118AOutputRFVoltageSetPointTrip_Object = MibScalar
cec118AOutputRFVoltageSetPointTrip = _Cec118AOutputRFVoltageSetPointTrip_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 46),
    _Cec118AOutputRFVoltageSetPointTrip_Type()
)
cec118AOutputRFVoltageSetPointTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AOutputRFVoltageSetPointTrip.setStatus("current")


class _Cec118APAPhase_Type(Integer32):
    """Custom type cec118APAPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_Cec118APAPhase_Type.__name__ = "Integer32"
_Cec118APAPhase_Object = MibScalar
cec118APAPhase = _Cec118APAPhase_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 47),
    _Cec118APAPhase_Type()
)
cec118APAPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118APAPhase.setStatus("current")


class _Cec118AModuleStatus1PA1_Type(Bits):
    """Custom type cec118AModuleStatus1PA1 based on Bits"""
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

_Cec118AModuleStatus1PA1_Type.__name__ = "Bits"
_Cec118AModuleStatus1PA1_Object = MibScalar
cec118AModuleStatus1PA1 = _Cec118AModuleStatus1PA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 48),
    _Cec118AModuleStatus1PA1_Type()
)
cec118AModuleStatus1PA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AModuleStatus1PA1.setStatus("current")


class _Cec118AModuleStatus2PA1_Type(Bits):
    """Custom type cec118AModuleStatus2PA1 based on Bits"""
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

_Cec118AModuleStatus2PA1_Type.__name__ = "Bits"
_Cec118AModuleStatus2PA1_Object = MibScalar
cec118AModuleStatus2PA1 = _Cec118AModuleStatus2PA1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 49),
    _Cec118AModuleStatus2PA1_Type()
)
cec118AModuleStatus2PA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AModuleStatus2PA1.setStatus("current")


class _Cec118AModuleStatus1PA2_Type(Bits):
    """Custom type cec118AModuleStatus1PA2 based on Bits"""
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

_Cec118AModuleStatus1PA2_Type.__name__ = "Bits"
_Cec118AModuleStatus1PA2_Object = MibScalar
cec118AModuleStatus1PA2 = _Cec118AModuleStatus1PA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 50),
    _Cec118AModuleStatus1PA2_Type()
)
cec118AModuleStatus1PA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AModuleStatus1PA2.setStatus("current")


class _Cec118AModuleStatus2PA2_Type(Bits):
    """Custom type cec118AModuleStatus2PA2 based on Bits"""
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

_Cec118AModuleStatus2PA2_Type.__name__ = "Bits"
_Cec118AModuleStatus2PA2_Object = MibScalar
cec118AModuleStatus2PA2 = _Cec118AModuleStatus2PA2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 51),
    _Cec118AModuleStatus2PA2_Type()
)
cec118AModuleStatus2PA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AModuleStatus2PA2.setStatus("current")
_Cec118AModuleResetCmd_Type = TruthValue
_Cec118AModuleResetCmd_Object = MibScalar
cec118AModuleResetCmd = _Cec118AModuleResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 52),
    _Cec118AModuleResetCmd_Type()
)
cec118AModuleResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AModuleResetCmd.setStatus("current")


class _Cec118AVariometer1PosnSet_Type(Integer32):
    """Custom type cec118AVariometer1PosnSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cec118AVariometer1PosnSet_Type.__name__ = "Integer32"
_Cec118AVariometer1PosnSet_Object = MibScalar
cec118AVariometer1PosnSet = _Cec118AVariometer1PosnSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 53),
    _Cec118AVariometer1PosnSet_Type()
)
cec118AVariometer1PosnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AVariometer1PosnSet.setStatus("current")


class _Cec118AVariometer2PosnSet_Type(Integer32):
    """Custom type cec118AVariometer2PosnSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cec118AVariometer2PosnSet_Type.__name__ = "Integer32"
_Cec118AVariometer2PosnSet_Object = MibScalar
cec118AVariometer2PosnSet = _Cec118AVariometer2PosnSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 54),
    _Cec118AVariometer2PosnSet_Type()
)
cec118AVariometer2PosnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AVariometer2PosnSet.setStatus("current")


class _Cec118ACapacitorPosnSet_Type(Integer32):
    """Custom type cec118ACapacitorPosnSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cec118ACapacitorPosnSet_Type.__name__ = "Integer32"
_Cec118ACapacitorPosnSet_Object = MibScalar
cec118ACapacitorPosnSet = _Cec118ACapacitorPosnSet_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 55),
    _Cec118ACapacitorPosnSet_Type()
)
cec118ACapacitorPosnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ACapacitorPosnSet.setStatus("current")


class _Cec118AVariometer1PosnStatus_Type(Integer32):
    """Custom type cec118AVariometer1PosnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cec118AVariometer1PosnStatus_Type.__name__ = "Integer32"
_Cec118AVariometer1PosnStatus_Object = MibScalar
cec118AVariometer1PosnStatus = _Cec118AVariometer1PosnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 56),
    _Cec118AVariometer1PosnStatus_Type()
)
cec118AVariometer1PosnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AVariometer1PosnStatus.setStatus("current")


class _Cec118AVariometer2PosnStatus_Type(Integer32):
    """Custom type cec118AVariometer2PosnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cec118AVariometer2PosnStatus_Type.__name__ = "Integer32"
_Cec118AVariometer2PosnStatus_Object = MibScalar
cec118AVariometer2PosnStatus = _Cec118AVariometer2PosnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 57),
    _Cec118AVariometer2PosnStatus_Type()
)
cec118AVariometer2PosnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AVariometer2PosnStatus.setStatus("current")


class _Cec118ACapacitorPosnStatus_Type(Integer32):
    """Custom type cec118ACapacitorPosnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_Cec118ACapacitorPosnStatus_Type.__name__ = "Integer32"
_Cec118ACapacitorPosnStatus_Object = MibScalar
cec118ACapacitorPosnStatus = _Cec118ACapacitorPosnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 58),
    _Cec118ACapacitorPosnStatus_Type()
)
cec118ACapacitorPosnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ACapacitorPosnStatus.setStatus("current")


class _Cec118AVariometer1ServoStatus_Type(Bits):
    """Custom type cec118AVariometer1ServoStatus based on Bits"""
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

_Cec118AVariometer1ServoStatus_Type.__name__ = "Bits"
_Cec118AVariometer1ServoStatus_Object = MibScalar
cec118AVariometer1ServoStatus = _Cec118AVariometer1ServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 59),
    _Cec118AVariometer1ServoStatus_Type()
)
cec118AVariometer1ServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AVariometer1ServoStatus.setStatus("current")


class _Cec118AVariometer2ServoStatus_Type(Bits):
    """Custom type cec118AVariometer2ServoStatus based on Bits"""
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

_Cec118AVariometer2ServoStatus_Type.__name__ = "Bits"
_Cec118AVariometer2ServoStatus_Object = MibScalar
cec118AVariometer2ServoStatus = _Cec118AVariometer2ServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 60),
    _Cec118AVariometer2ServoStatus_Type()
)
cec118AVariometer2ServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AVariometer2ServoStatus.setStatus("current")


class _Cec118ACapacitorServoStatus_Type(Bits):
    """Custom type cec118ACapacitorServoStatus based on Bits"""
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

_Cec118ACapacitorServoStatus_Type.__name__ = "Bits"
_Cec118ACapacitorServoStatus_Object = MibScalar
cec118ACapacitorServoStatus = _Cec118ACapacitorServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 61),
    _Cec118ACapacitorServoStatus_Type()
)
cec118ACapacitorServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ACapacitorServoStatus.setStatus("current")
_Cec118ATuneFault_Type = TruthValue
_Cec118ATuneFault_Object = MibScalar
cec118ATuneFault = _Cec118ATuneFault_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 62),
    _Cec118ATuneFault_Type()
)
cec118ATuneFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ATuneFault.setStatus("current")


class _Cec118ACapacitorSwStatus_Type(Bits):
    """Custom type cec118ACapacitorSwStatus based on Bits"""
    namedValues = NamedValues(
        *(("cap1SwitchedIn", 0),
          ("cap2SwitchedIn", 1),
          ("cap3SwitchedIn", 2),
          ("cap4SwitchedIn", 3))
    )

_Cec118ACapacitorSwStatus_Type.__name__ = "Bits"
_Cec118ACapacitorSwStatus_Object = MibScalar
cec118ACapacitorSwStatus = _Cec118ACapacitorSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 63),
    _Cec118ACapacitorSwStatus_Type()
)
cec118ACapacitorSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ACapacitorSwStatus.setStatus("current")
_Cec118AArcPACab1_Type = TruthValue
_Cec118AArcPACab1_Object = MibScalar
cec118AArcPACab1 = _Cec118AArcPACab1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 64),
    _Cec118AArcPACab1_Type()
)
cec118AArcPACab1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AArcPACab1.setStatus("current")
_Cec118AArcPACab2_Type = TruthValue
_Cec118AArcPACab2_Object = MibScalar
cec118AArcPACab2 = _Cec118AArcPACab2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 65),
    _Cec118AArcPACab2_Type()
)
cec118AArcPACab2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AArcPACab2.setStatus("current")
_Cec118AArcTeeNetVario1_Type = TruthValue
_Cec118AArcTeeNetVario1_Object = MibScalar
cec118AArcTeeNetVario1 = _Cec118AArcTeeNetVario1_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 66),
    _Cec118AArcTeeNetVario1_Type()
)
cec118AArcTeeNetVario1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AArcTeeNetVario1.setStatus("current")
_Cec118AArcTeeNetVario2_Type = TruthValue
_Cec118AArcTeeNetVario2_Object = MibScalar
cec118AArcTeeNetVario2 = _Cec118AArcTeeNetVario2_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 67),
    _Cec118AArcTeeNetVario2_Type()
)
cec118AArcTeeNetVario2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AArcTeeNetVario2.setStatus("current")
_Cec118AArcTeeNetCap_Type = TruthValue
_Cec118AArcTeeNetCap_Object = MibScalar
cec118AArcTeeNetCap = _Cec118AArcTeeNetCap_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 68),
    _Cec118AArcTeeNetCap_Type()
)
cec118AArcTeeNetCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AArcTeeNetCap.setStatus("current")
_Cec118AArcPACab1Test_Type = TruthValue
_Cec118AArcPACab1Test_Object = MibScalar
cec118AArcPACab1Test = _Cec118AArcPACab1Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 69),
    _Cec118AArcPACab1Test_Type()
)
cec118AArcPACab1Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AArcPACab1Test.setStatus("current")
_Cec118AArcPACab2Test_Type = TruthValue
_Cec118AArcPACab2Test_Object = MibScalar
cec118AArcPACab2Test = _Cec118AArcPACab2Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 70),
    _Cec118AArcPACab2Test_Type()
)
cec118AArcPACab2Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AArcPACab2Test.setStatus("current")
_Cec118AArcTeeNetVario1Test_Type = TruthValue
_Cec118AArcTeeNetVario1Test_Object = MibScalar
cec118AArcTeeNetVario1Test = _Cec118AArcTeeNetVario1Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 71),
    _Cec118AArcTeeNetVario1Test_Type()
)
cec118AArcTeeNetVario1Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AArcTeeNetVario1Test.setStatus("current")
_Cec118AArcTeeNetVario2Test_Type = TruthValue
_Cec118AArcTeeNetVario2Test_Object = MibScalar
cec118AArcTeeNetVario2Test = _Cec118AArcTeeNetVario2Test_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 72),
    _Cec118AArcTeeNetVario2Test_Type()
)
cec118AArcTeeNetVario2Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AArcTeeNetVario2Test.setStatus("current")
_Cec118AArcTeeNetCapTest_Type = TruthValue
_Cec118AArcTeeNetCapTest_Object = MibScalar
cec118AArcTeeNetCapTest = _Cec118AArcTeeNetCapTest_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 73),
    _Cec118AArcTeeNetCapTest_Type()
)
cec118AArcTeeNetCapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AArcTeeNetCapTest.setStatus("current")


class _Cec118AAntennaCurrentMagnitude_Type(Integer32):
    """Custom type cec118AAntennaCurrentMagnitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cec118AAntennaCurrentMagnitude_Type.__name__ = "Integer32"
_Cec118AAntennaCurrentMagnitude_Object = MibScalar
cec118AAntennaCurrentMagnitude = _Cec118AAntennaCurrentMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 74),
    _Cec118AAntennaCurrentMagnitude_Type()
)
cec118AAntennaCurrentMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAntennaCurrentMagnitude.setStatus("current")


class _Cec118AAntennaCurrentPhase_Type(Integer32):
    """Custom type cec118AAntennaCurrentPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1800, 1800),
    )


_Cec118AAntennaCurrentPhase_Type.__name__ = "Integer32"
_Cec118AAntennaCurrentPhase_Object = MibScalar
cec118AAntennaCurrentPhase = _Cec118AAntennaCurrentPhase_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 75),
    _Cec118AAntennaCurrentPhase_Type()
)
cec118AAntennaCurrentPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAntennaCurrentPhase.setStatus("current")
_Cec118AConnectedToDummyLoad_Type = TruthValue
_Cec118AConnectedToDummyLoad_Object = MibScalar
cec118AConnectedToDummyLoad = _Cec118AConnectedToDummyLoad_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 76),
    _Cec118AConnectedToDummyLoad_Type()
)
cec118AConnectedToDummyLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AConnectedToDummyLoad.setStatus("current")
_Cec118AConnectedToAntenna_Type = OctetString
_Cec118AConnectedToAntenna_Object = MibScalar
cec118AConnectedToAntenna = _Cec118AConnectedToAntenna_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 77),
    _Cec118AConnectedToAntenna_Type()
)
cec118AConnectedToAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AConnectedToAntenna.setStatus("current")
_Cec118AGroundSwitchStatus_Type = TruthValue
_Cec118AGroundSwitchStatus_Object = MibScalar
cec118AGroundSwitchStatus = _Cec118AGroundSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 78),
    _Cec118AGroundSwitchStatus_Type()
)
cec118AGroundSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AGroundSwitchStatus.setStatus("current")


class _Cec118ASupplyTemperature_Type(Integer32):
    """Custom type cec118ASupplyTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 1000),
    )


_Cec118ASupplyTemperature_Type.__name__ = "Integer32"
_Cec118ASupplyTemperature_Object = MibScalar
cec118ASupplyTemperature = _Cec118ASupplyTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 79),
    _Cec118ASupplyTemperature_Type()
)
cec118ASupplyTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ASupplyTemperature.setStatus("current")


class _Cec118AExhaustTemperature_Type(Integer32):
    """Custom type cec118AExhaustTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 1000),
    )


_Cec118AExhaustTemperature_Type.__name__ = "Integer32"
_Cec118AExhaustTemperature_Object = MibScalar
cec118AExhaustTemperature = _Cec118AExhaustTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 80),
    _Cec118AExhaustTemperature_Type()
)
cec118AExhaustTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AExhaustTemperature.setStatus("current")
_Cec118AHours_Type = Integer32
_Cec118AHours_Object = MibScalar
cec118AHours = _Cec118AHours_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 81),
    _Cec118AHours_Type()
)
cec118AHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AHours.setStatus("current")
_Cec118ADateAndTime_Type = DateAndTime
_Cec118ADateAndTime_Object = MibScalar
cec118ADateAndTime = _Cec118ADateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 82),
    _Cec118ADateAndTime_Type()
)
cec118ADateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADateAndTime.setStatus("current")
_Cec118AHardwareVersion_Type = OctetString
_Cec118AHardwareVersion_Object = MibScalar
cec118AHardwareVersion = _Cec118AHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 83),
    _Cec118AHardwareVersion_Type()
)
cec118AHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AHardwareVersion.setStatus("current")
_Cec118ASoftwareVersion_Type = OctetString
_Cec118ASoftwareVersion_Object = MibScalar
cec118ASoftwareVersion = _Cec118ASoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 84),
    _Cec118ASoftwareVersion_Type()
)
cec118ASoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ASoftwareVersion.setStatus("current")
_Cec118ASummaryFault_Type = TruthValue
_Cec118ASummaryFault_Object = MibScalar
cec118ASummaryFault = _Cec118ASummaryFault_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 85),
    _Cec118ASummaryFault_Type()
)
cec118ASummaryFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ASummaryFault.setStatus("current")
_Cec118AFaultResetCmd_Type = TruthValue
_Cec118AFaultResetCmd_Object = MibScalar
cec118AFaultResetCmd = _Cec118AFaultResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 86),
    _Cec118AFaultResetCmd_Type()
)
cec118AFaultResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AFaultResetCmd.setStatus("current")
_Cec118AOperate_Type = TruthValue
_Cec118AOperate_Object = MibScalar
cec118AOperate = _Cec118AOperate_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 87),
    _Cec118AOperate_Type()
)
cec118AOperate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AOperate.setStatus("current")
_Cec118AOperateStatus_Type = TruthValue
_Cec118AOperateStatus_Object = MibScalar
cec118AOperateStatus = _Cec118AOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 88),
    _Cec118AOperateStatus_Type()
)
cec118AOperateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AOperateStatus.setStatus("current")
_Cec118ADCOn_Type = TruthValue
_Cec118ADCOn_Object = MibScalar
cec118ADCOn = _Cec118ADCOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 89),
    _Cec118ADCOn_Type()
)
cec118ADCOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCOn.setStatus("current")
_Cec118ADCOnStatus_Type = TruthValue
_Cec118ADCOnStatus_Object = MibScalar
cec118ADCOnStatus = _Cec118ADCOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 90),
    _Cec118ADCOnStatus_Type()
)
cec118ADCOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ADCOnStatus.setStatus("current")
_Cec118AWFGPACab1Doors_Type = TruthValue
_Cec118AWFGPACab1Doors_Object = MibScalar
cec118AWFGPACab1Doors = _Cec118AWFGPACab1Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 91),
    _Cec118AWFGPACab1Doors_Type()
)
cec118AWFGPACab1Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AWFGPACab1Doors.setStatus("current")
_Cec118AWFGPACab2Doors_Type = TruthValue
_Cec118AWFGPACab2Doors_Object = MibScalar
cec118AWFGPACab2Doors = _Cec118AWFGPACab2Doors_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 92),
    _Cec118AWFGPACab2Doors_Type()
)
cec118AWFGPACab2Doors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AWFGPACab2Doors.setStatus("current")
_Cec118AACOn_Type = TruthValue
_Cec118AACOn_Object = MibScalar
cec118AACOn = _Cec118AACOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 93),
    _Cec118AACOn_Type()
)
cec118AACOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AACOn.setStatus("current")
_Cec118AACOnStatus_Type = TruthValue
_Cec118AACOnStatus_Object = MibScalar
cec118AACOnStatus = _Cec118AACOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 94),
    _Cec118AACOnStatus_Type()
)
cec118AACOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AACOnStatus.setStatus("current")
_Cec118AFansOn_Type = TruthValue
_Cec118AFansOn_Object = MibScalar
cec118AFansOn = _Cec118AFansOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 95),
    _Cec118AFansOn_Type()
)
cec118AFansOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AFansOn.setStatus("current")
_Cec118ACoolingOnStatus_Type = TruthValue
_Cec118ACoolingOnStatus_Object = MibScalar
cec118ACoolingOnStatus = _Cec118ACoolingOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 96),
    _Cec118ACoolingOnStatus_Type()
)
cec118ACoolingOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ACoolingOnStatus.setStatus("current")
_Cec118AExternalCoolingIsOn_Type = TruthValue
_Cec118AExternalCoolingIsOn_Object = MibScalar
cec118AExternalCoolingIsOn = _Cec118AExternalCoolingIsOn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 97),
    _Cec118AExternalCoolingIsOn_Type()
)
cec118AExternalCoolingIsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118AExternalCoolingIsOn.setStatus("current")


class _Cec118ARFLevelControlInput_Type(Integer32):
    """Custom type cec118ARFLevelControlInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118ARFLevelControlInput_Type.__name__ = "Integer32"
_Cec118ARFLevelControlInput_Object = MibScalar
cec118ARFLevelControlInput = _Cec118ARFLevelControlInput_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 98),
    _Cec118ARFLevelControlInput_Type()
)
cec118ARFLevelControlInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ARFLevelControlInput.setStatus("current")


class _Cec118APALevelPercentPower_Type(Integer32):
    """Custom type cec118APALevelPercentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118APALevelPercentPower_Type.__name__ = "Integer32"
_Cec118APALevelPercentPower_Object = MibScalar
cec118APALevelPercentPower = _Cec118APALevelPercentPower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 99),
    _Cec118APALevelPercentPower_Type()
)
cec118APALevelPercentPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118APALevelPercentPower.setStatus("current")
_Cec118ARemoteLocalStatus_Type = TruthValue
_Cec118ARemoteLocalStatus_Object = MibScalar
cec118ARemoteLocalStatus = _Cec118ARemoteLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 100),
    _Cec118ARemoteLocalStatus_Type()
)
cec118ARemoteLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118ARemoteLocalStatus.setStatus("current")


class _Cec118AAntSampleClipStatus_Type(Bits):
    """Custom type cec118AAntSampleClipStatus based on Bits"""
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

_Cec118AAntSampleClipStatus_Type.__name__ = "Bits"
_Cec118AAntSampleClipStatus_Object = MibScalar
cec118AAntSampleClipStatus = _Cec118AAntSampleClipStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 101),
    _Cec118AAntSampleClipStatus_Type()
)
cec118AAntSampleClipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAntSampleClipStatus.setStatus("current")


class _Cec118AAntSampleLowLevelStatus_Type(Bits):
    """Custom type cec118AAntSampleLowLevelStatus based on Bits"""
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

_Cec118AAntSampleLowLevelStatus_Type.__name__ = "Bits"
_Cec118AAntSampleLowLevelStatus_Object = MibScalar
cec118AAntSampleLowLevelStatus = _Cec118AAntSampleLowLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 102),
    _Cec118AAntSampleLowLevelStatus_Type()
)
cec118AAntSampleLowLevelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAntSampleLowLevelStatus.setStatus("current")


class _Cec118AAnt11SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt11SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt11SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt11SampleInputLevel_Object = MibScalar
cec118AAnt11SampleInputLevel = _Cec118AAnt11SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 103),
    _Cec118AAnt11SampleInputLevel_Type()
)
cec118AAnt11SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt11SampleInputLevel.setStatus("current")


class _Cec118AAnt12SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt12SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt12SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt12SampleInputLevel_Object = MibScalar
cec118AAnt12SampleInputLevel = _Cec118AAnt12SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 104),
    _Cec118AAnt12SampleInputLevel_Type()
)
cec118AAnt12SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt12SampleInputLevel.setStatus("current")


class _Cec118AAnt13SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt13SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt13SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt13SampleInputLevel_Object = MibScalar
cec118AAnt13SampleInputLevel = _Cec118AAnt13SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 105),
    _Cec118AAnt13SampleInputLevel_Type()
)
cec118AAnt13SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt13SampleInputLevel.setStatus("current")


class _Cec118AAnt14SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt14SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt14SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt14SampleInputLevel_Object = MibScalar
cec118AAnt14SampleInputLevel = _Cec118AAnt14SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 106),
    _Cec118AAnt14SampleInputLevel_Type()
)
cec118AAnt14SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt14SampleInputLevel.setStatus("current")


class _Cec118AAnt21SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt21SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt21SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt21SampleInputLevel_Object = MibScalar
cec118AAnt21SampleInputLevel = _Cec118AAnt21SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 107),
    _Cec118AAnt21SampleInputLevel_Type()
)
cec118AAnt21SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt21SampleInputLevel.setStatus("current")


class _Cec118AAnt22SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt22SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt22SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt22SampleInputLevel_Object = MibScalar
cec118AAnt22SampleInputLevel = _Cec118AAnt22SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 108),
    _Cec118AAnt22SampleInputLevel_Type()
)
cec118AAnt22SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt22SampleInputLevel.setStatus("current")


class _Cec118AAnt23SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt23SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt23SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt23SampleInputLevel_Object = MibScalar
cec118AAnt23SampleInputLevel = _Cec118AAnt23SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 109),
    _Cec118AAnt23SampleInputLevel_Type()
)
cec118AAnt23SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt23SampleInputLevel.setStatus("current")


class _Cec118AAnt24SampleInputLevel_Type(Integer32):
    """Custom type cec118AAnt24SampleInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cec118AAnt24SampleInputLevel_Type.__name__ = "Integer32"
_Cec118AAnt24SampleInputLevel_Object = MibScalar
cec118AAnt24SampleInputLevel = _Cec118AAnt24SampleInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 110),
    _Cec118AAnt24SampleInputLevel_Type()
)
cec118AAnt24SampleInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cec118AAnt24SampleInputLevel.setStatus("current")


class _Cec118ATxCtrlEq_Type(Integer32):
    """Custom type cec118ATxCtrlEq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cec118ATxCtrlEq_Type.__name__ = "Integer32"
_Cec118ATxCtrlEq_Object = MibScalar
cec118ATxCtrlEq = _Cec118ATxCtrlEq_Object(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 1, 111),
    _Cec118ATxCtrlEq_Type()
)
cec118ATxCtrlEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cec118ATxCtrlEq.setStatus("current")

# Managed Objects groups

cec118AGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48307, 2, 2, 2, 1)
)
cec118AGroup.setObjects(
      *(("CONTELEC-118A-MIB", "cec118AFrequency"),
        ("CONTELEC-118A-MIB", "cec118AEQControl"),
        ("CONTELEC-118A-MIB", "cec118AEQReset"),
        ("CONTELEC-118A-MIB", "cec118ACCORiseTime"),
        ("CONTELEC-118A-MIB", "cec118ACCOFallTime"),
        ("CONTELEC-118A-MIB", "cec118AA1ARiseTime"),
        ("CONTELEC-118A-MIB", "cec118AA1AFallTime"),
        ("CONTELEC-118A-MIB", "cec118AModulationType"),
        ("CONTELEC-118A-MIB", "cec118AEQNLOOP"),
        ("CONTELEC-118A-MIB", "cec118AEQConverge"),
        ("CONTELEC-118A-MIB", "cec118ARFVInputScale"),
        ("CONTELEC-118A-MIB", "cec118ARampDelayOff"),
        ("CONTELEC-118A-MIB", "cec118ARampDelayOn"),
        ("CONTELEC-118A-MIB", "cec118AModRFInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AModRFClip"),
        ("CONTELEC-118A-MIB", "cec118ALowRFDrive"),
        ("CONTELEC-118A-MIB", "cec118AModIntSineWave"),
        ("CONTELEC-118A-MIB", "cec118AEqIterCount"),
        ("CONTELEC-118A-MIB", "cec118AAdaptiveStatus"),
        ("CONTELEC-118A-MIB", "cec118AOutputPower"),
        ("CONTELEC-118A-MIB", "cec118AReflectedPower"),
        ("CONTELEC-118A-MIB", "cec118AImpedanceReal"),
        ("CONTELEC-118A-MIB", "cec118AImpedanceImag"),
        ("CONTELEC-118A-MIB", "cec118AVSWR"),
        ("CONTELEC-118A-MIB", "cec118AS11Real"),
        ("CONTELEC-118A-MIB", "cec118AS11Imag"),
        ("CONTELEC-118A-MIB", "cec118APARFCurrent"),
        ("CONTELEC-118A-MIB", "cec118ACombinerCurrentSetPointTrip"),
        ("CONTELEC-118A-MIB", "cec118AOutputRFCurrent"),
        ("CONTELEC-118A-MIB", "cec118AOutputRFCurrentSetPointTrip"),
        ("CONTELEC-118A-MIB", "cec118AOutputRFVoltage"),
        ("CONTELEC-118A-MIB", "cec118AOutputRFVoltageSetPointTrip"),
        ("CONTELEC-118A-MIB", "cec118ASNR"),
        ("CONTELEC-118A-MIB", "cec118ATSPLoopStatus"),
        ("CONTELEC-118A-MIB", "cec118AAntennaReverseInterlock"),
        ("CONTELEC-118A-MIB", "cec118APACab1Doors"),
        ("CONTELEC-118A-MIB", "cec118APACab2Doors"),
        ("CONTELEC-118A-MIB", "cec118AWFGPACab1Doors"),
        ("CONTELEC-118A-MIB", "cec118AWFGPACab2Doors"),
        ("CONTELEC-118A-MIB", "cec118ATeeNetCab1Doors"),
        ("CONTELEC-118A-MIB", "cec118ATeeNetCab2Doors"),
        ("CONTELEC-118A-MIB", "cec118ADCVoltagePA1"),
        ("CONTELEC-118A-MIB", "cec118ADCVoltagePA2"),
        ("CONTELEC-118A-MIB", "cec118AAverageDCVoltage"),
        ("CONTELEC-118A-MIB", "cec118ADCCurrentPA1"),
        ("CONTELEC-118A-MIB", "cec118ADCCurrentPA2"),
        ("CONTELEC-118A-MIB", "cec118ATotalDCCurrent"),
        ("CONTELEC-118A-MIB", "cec118ADCPowerSupplyTempStatus"),
        ("CONTELEC-118A-MIB", "cec118APAPhase"),
        ("CONTELEC-118A-MIB", "cec118AModuleStatus1PA1"),
        ("CONTELEC-118A-MIB", "cec118AModuleStatus2PA1"),
        ("CONTELEC-118A-MIB", "cec118AModuleStatus1PA2"),
        ("CONTELEC-118A-MIB", "cec118AModuleStatus2PA2"),
        ("CONTELEC-118A-MIB", "cec118AModuleResetCmd"),
        ("CONTELEC-118A-MIB", "cec118AVariometer1PosnSet"),
        ("CONTELEC-118A-MIB", "cec118AVariometer2PosnSet"),
        ("CONTELEC-118A-MIB", "cec118ACapacitorPosnSet"),
        ("CONTELEC-118A-MIB", "cec118AVariometer1PosnStatus"),
        ("CONTELEC-118A-MIB", "cec118AVariometer2PosnStatus"),
        ("CONTELEC-118A-MIB", "cec118ACapacitorPosnStatus"),
        ("CONTELEC-118A-MIB", "cec118AVariometer1ServoStatus"),
        ("CONTELEC-118A-MIB", "cec118AVariometer2ServoStatus"),
        ("CONTELEC-118A-MIB", "cec118ACapacitorServoStatus"),
        ("CONTELEC-118A-MIB", "cec118ATuneFault"),
        ("CONTELEC-118A-MIB", "cec118ACapacitorSwStatus"),
        ("CONTELEC-118A-MIB", "cec118AArcPACab1"),
        ("CONTELEC-118A-MIB", "cec118AArcPACab2"),
        ("CONTELEC-118A-MIB", "cec118AArcTeeNetVario1"),
        ("CONTELEC-118A-MIB", "cec118AArcTeeNetVario2"),
        ("CONTELEC-118A-MIB", "cec118AArcTeeNetCap"),
        ("CONTELEC-118A-MIB", "cec118AArcPACab1Test"),
        ("CONTELEC-118A-MIB", "cec118AArcPACab2Test"),
        ("CONTELEC-118A-MIB", "cec118AArcTeeNetVario1Test"),
        ("CONTELEC-118A-MIB", "cec118AArcTeeNetVario2Test"),
        ("CONTELEC-118A-MIB", "cec118AArcTeeNetCapTest"),
        ("CONTELEC-118A-MIB", "cec118AAntennaCurrentMagnitude"),
        ("CONTELEC-118A-MIB", "cec118AAntennaCurrentPhase"),
        ("CONTELEC-118A-MIB", "cec118AConnectedToDummyLoad"),
        ("CONTELEC-118A-MIB", "cec118AConnectedToAntenna"),
        ("CONTELEC-118A-MIB", "cec118AGroundSwitchStatus"),
        ("CONTELEC-118A-MIB", "cec118ASupplyTemperature"),
        ("CONTELEC-118A-MIB", "cec118AExhaustTemperature"),
        ("CONTELEC-118A-MIB", "cec118AHours"),
        ("CONTELEC-118A-MIB", "cec118ADateAndTime"),
        ("CONTELEC-118A-MIB", "cec118AHardwareVersion"),
        ("CONTELEC-118A-MIB", "cec118ASoftwareVersion"),
        ("CONTELEC-118A-MIB", "cec118ASummaryFault"),
        ("CONTELEC-118A-MIB", "cec118AFaultResetCmd"),
        ("CONTELEC-118A-MIB", "cec118AOperate"),
        ("CONTELEC-118A-MIB", "cec118AOperateStatus"),
        ("CONTELEC-118A-MIB", "cec118ADCOn"),
        ("CONTELEC-118A-MIB", "cec118ADCOnStatus"),
        ("CONTELEC-118A-MIB", "cec118AACOn"),
        ("CONTELEC-118A-MIB", "cec118AACOnStatus"),
        ("CONTELEC-118A-MIB", "cec118AFansOn"),
        ("CONTELEC-118A-MIB", "cec118ACoolingOnStatus"),
        ("CONTELEC-118A-MIB", "cec118AExternalCoolingIsOn"),
        ("CONTELEC-118A-MIB", "cec118ARFLevelControlInput"),
        ("CONTELEC-118A-MIB", "cec118APALevelPercentPower"),
        ("CONTELEC-118A-MIB", "cec118ARemoteLocalStatus"),
        ("CONTELEC-118A-MIB", "cec118AAntSampleClipStatus"),
        ("CONTELEC-118A-MIB", "cec118AAntSampleLowLevelStatus"),
        ("CONTELEC-118A-MIB", "cec118AAnt11SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt12SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt13SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt14SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt21SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt22SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt23SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118AAnt24SampleInputLevel"),
        ("CONTELEC-118A-MIB", "cec118ATxCtrlEq"))
)
if mibBuilder.loadTexts:
    cec118AGroup.setStatus("current")


# Notification objects

cec118AEqIterCompleteNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 5)
)
if mibBuilder.loadTexts:
    cec118AEqIterCompleteNotice.setStatus(
        "current"
    )

cec118AAdaptiveCorrectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 6)
)
if mibBuilder.loadTexts:
    cec118AAdaptiveCorrectionFault.setStatus(
        "current"
    )

cec118ALowRFDriveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 7)
)
if mibBuilder.loadTexts:
    cec118ALowRFDriveAlarm.setStatus(
        "current"
    )

cec118AModRFClipAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 8)
)
if mibBuilder.loadTexts:
    cec118AModRFClipAlarm.setStatus(
        "current"
    )

cec118ALowAntennaCurrentFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 9)
)
if mibBuilder.loadTexts:
    cec118ALowAntennaCurrentFault.setStatus(
        "current"
    )

cec118AFaultHighDCVoltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 10)
)
if mibBuilder.loadTexts:
    cec118AFaultHighDCVoltageAlarm.setStatus(
        "current"
    )

cec118AFaultHighDCCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 11)
)
if mibBuilder.loadTexts:
    cec118AFaultHighDCCurrentAlarm.setStatus(
        "current"
    )

cec118AFaultDCPowerSupplyTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 12)
)
if mibBuilder.loadTexts:
    cec118AFaultDCPowerSupplyTempAlarm.setStatus(
        "current"
    )

cec118AModuleFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 15)
)
if mibBuilder.loadTexts:
    cec118AModuleFaultAlarm.setStatus(
        "current"
    )

cec118AArcAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 16)
)
if mibBuilder.loadTexts:
    cec118AArcAlarm.setStatus(
        "current"
    )

cec118ADoorInterlockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 17)
)
if mibBuilder.loadTexts:
    cec118ADoorInterlockAlarm.setStatus(
        "current"
    )

cec118ACardInterlockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 18)
)
if mibBuilder.loadTexts:
    cec118ACardInterlockAlarm.setStatus(
        "current"
    )

cec118AGroundRelayInterlockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 19)
)
if mibBuilder.loadTexts:
    cec118AGroundRelayInterlockAlarm.setStatus(
        "current"
    )

cec118AAntennaCurrentClip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 22)
)
if mibBuilder.loadTexts:
    cec118AAntennaCurrentClip.setStatus(
        "current"
    )

cec118ACombinerCurrentTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 23)
)
if mibBuilder.loadTexts:
    cec118ACombinerCurrentTrip.setStatus(
        "current"
    )

cec118AOutputCurrentTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 24)
)
if mibBuilder.loadTexts:
    cec118AOutputCurrentTrip.setStatus(
        "current"
    )

cec118AOutputVoltageTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 2, 3, 0, 25)
)
if mibBuilder.loadTexts:
    cec118AOutputVoltageTrip.setStatus(
        "current"
    )


# Notifications groups

cec118ANotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48307, 2, 2, 2, 2)
)
cec118ANotificationGroup.setObjects(
      *(("CONTELEC-118A-MIB", "cec118AEqIterCompleteNotice"),
        ("CONTELEC-118A-MIB", "cec118AAdaptiveCorrectionFault"),
        ("CONTELEC-118A-MIB", "cec118ALowRFDriveAlarm"),
        ("CONTELEC-118A-MIB", "cec118AModRFClipAlarm"),
        ("CONTELEC-118A-MIB", "cec118ALowAntennaCurrentFault"),
        ("CONTELEC-118A-MIB", "cec118AFaultHighDCVoltageAlarm"),
        ("CONTELEC-118A-MIB", "cec118AFaultHighDCCurrentAlarm"),
        ("CONTELEC-118A-MIB", "cec118AFaultDCPowerSupplyTempAlarm"),
        ("CONTELEC-118A-MIB", "cec118AModuleFaultAlarm"),
        ("CONTELEC-118A-MIB", "cec118AArcAlarm"),
        ("CONTELEC-118A-MIB", "cec118ADoorInterlockAlarm"),
        ("CONTELEC-118A-MIB", "cec118ACardInterlockAlarm"),
        ("CONTELEC-118A-MIB", "cec118AGroundRelayInterlockAlarm"),
        ("CONTELEC-118A-MIB", "cec118AAntennaCurrentClip"),
        ("CONTELEC-118A-MIB", "cec118ACombinerCurrentTrip"),
        ("CONTELEC-118A-MIB", "cec118AOutputCurrentTrip"),
        ("CONTELEC-118A-MIB", "cec118AOutputVoltageTrip"))
)
if mibBuilder.loadTexts:
    cec118ANotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cec118ACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48307, 2, 2, 1, 1)
)
cec118ACompliance.setObjects(
      *(("CONTELEC-118A-MIB", "cec118AGroup"),
        ("CONTELEC-118A-MIB", "cec118ANotificationGroup"))
)
if mibBuilder.loadTexts:
    cec118ACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTELEC-118A-MIB",
    **{"contelec118A": contelec118A,
       "cec118AConformance": cec118AConformance,
       "cec118ACompliances": cec118ACompliances,
       "cec118ACompliance": cec118ACompliance,
       "cec118AGroups": cec118AGroups,
       "cec118AGroup": cec118AGroup,
       "cec118ANotificationGroup": cec118ANotificationGroup,
       "cec118Aobject": cec118Aobject,
       "cec118ATraps": cec118ATraps,
       "cec118AEqIterCompleteNotice": cec118AEqIterCompleteNotice,
       "cec118AAdaptiveCorrectionFault": cec118AAdaptiveCorrectionFault,
       "cec118ALowRFDriveAlarm": cec118ALowRFDriveAlarm,
       "cec118AModRFClipAlarm": cec118AModRFClipAlarm,
       "cec118ALowAntennaCurrentFault": cec118ALowAntennaCurrentFault,
       "cec118AFaultHighDCVoltageAlarm": cec118AFaultHighDCVoltageAlarm,
       "cec118AFaultHighDCCurrentAlarm": cec118AFaultHighDCCurrentAlarm,
       "cec118AFaultDCPowerSupplyTempAlarm": cec118AFaultDCPowerSupplyTempAlarm,
       "cec118AModuleFaultAlarm": cec118AModuleFaultAlarm,
       "cec118AArcAlarm": cec118AArcAlarm,
       "cec118ADoorInterlockAlarm": cec118ADoorInterlockAlarm,
       "cec118ACardInterlockAlarm": cec118ACardInterlockAlarm,
       "cec118AGroundRelayInterlockAlarm": cec118AGroundRelayInterlockAlarm,
       "cec118AAntennaCurrentClip": cec118AAntennaCurrentClip,
       "cec118ACombinerCurrentTrip": cec118ACombinerCurrentTrip,
       "cec118AOutputCurrentTrip": cec118AOutputCurrentTrip,
       "cec118AOutputVoltageTrip": cec118AOutputVoltageTrip,
       "cec118ASpecs": cec118ASpecs,
       "cec118AFrequency": cec118AFrequency,
       "cec118AEQControl": cec118AEQControl,
       "cec118AEQReset": cec118AEQReset,
       "cec118ACCORiseTime": cec118ACCORiseTime,
       "cec118ACCOFallTime": cec118ACCOFallTime,
       "cec118AA1ARiseTime": cec118AA1ARiseTime,
       "cec118AA1AFallTime": cec118AA1AFallTime,
       "cec118AModulationType": cec118AModulationType,
       "cec118AEQNLOOP": cec118AEQNLOOP,
       "cec118AEQConverge": cec118AEQConverge,
       "cec118ARFVInputScale": cec118ARFVInputScale,
       "cec118ARampDelayOff": cec118ARampDelayOff,
       "cec118ARampDelayOn": cec118ARampDelayOn,
       "cec118AModRFInputLevel": cec118AModRFInputLevel,
       "cec118AModRFClip": cec118AModRFClip,
       "cec118ALowRFDrive": cec118ALowRFDrive,
       "cec118AModIntSineWave": cec118AModIntSineWave,
       "cec118AEqIterCount": cec118AEqIterCount,
       "cec118AAdaptiveStatus": cec118AAdaptiveStatus,
       "cec118AOutputPower": cec118AOutputPower,
       "cec118AReflectedPower": cec118AReflectedPower,
       "cec118AImpedanceReal": cec118AImpedanceReal,
       "cec118AImpedanceImag": cec118AImpedanceImag,
       "cec118AVSWR": cec118AVSWR,
       "cec118AS11Real": cec118AS11Real,
       "cec118AS11Imag": cec118AS11Imag,
       "cec118APARFCurrent": cec118APARFCurrent,
       "cec118ACombinerCurrentSetPointTrip": cec118ACombinerCurrentSetPointTrip,
       "cec118AOutputRFCurrent": cec118AOutputRFCurrent,
       "cec118AOutputRFCurrentSetPointTrip": cec118AOutputRFCurrentSetPointTrip,
       "cec118ASNR": cec118ASNR,
       "cec118ATSPLoopStatus": cec118ATSPLoopStatus,
       "cec118AAntennaReverseInterlock": cec118AAntennaReverseInterlock,
       "cec118APACab1Doors": cec118APACab1Doors,
       "cec118APACab2Doors": cec118APACab2Doors,
       "cec118ATeeNetCab1Doors": cec118ATeeNetCab1Doors,
       "cec118ATeeNetCab2Doors": cec118ATeeNetCab2Doors,
       "cec118ADCVoltagePA1": cec118ADCVoltagePA1,
       "cec118ADCVoltagePA2": cec118ADCVoltagePA2,
       "cec118AAverageDCVoltage": cec118AAverageDCVoltage,
       "cec118ADCCurrentPA1": cec118ADCCurrentPA1,
       "cec118ADCCurrentPA2": cec118ADCCurrentPA2,
       "cec118ATotalDCCurrent": cec118ATotalDCCurrent,
       "cec118ADCPowerSupplyTempStatus": cec118ADCPowerSupplyTempStatus,
       "cec118AOutputRFVoltage": cec118AOutputRFVoltage,
       "cec118AOutputRFVoltageSetPointTrip": cec118AOutputRFVoltageSetPointTrip,
       "cec118APAPhase": cec118APAPhase,
       "cec118AModuleStatus1PA1": cec118AModuleStatus1PA1,
       "cec118AModuleStatus2PA1": cec118AModuleStatus2PA1,
       "cec118AModuleStatus1PA2": cec118AModuleStatus1PA2,
       "cec118AModuleStatus2PA2": cec118AModuleStatus2PA2,
       "cec118AModuleResetCmd": cec118AModuleResetCmd,
       "cec118AVariometer1PosnSet": cec118AVariometer1PosnSet,
       "cec118AVariometer2PosnSet": cec118AVariometer2PosnSet,
       "cec118ACapacitorPosnSet": cec118ACapacitorPosnSet,
       "cec118AVariometer1PosnStatus": cec118AVariometer1PosnStatus,
       "cec118AVariometer2PosnStatus": cec118AVariometer2PosnStatus,
       "cec118ACapacitorPosnStatus": cec118ACapacitorPosnStatus,
       "cec118AVariometer1ServoStatus": cec118AVariometer1ServoStatus,
       "cec118AVariometer2ServoStatus": cec118AVariometer2ServoStatus,
       "cec118ACapacitorServoStatus": cec118ACapacitorServoStatus,
       "cec118ATuneFault": cec118ATuneFault,
       "cec118ACapacitorSwStatus": cec118ACapacitorSwStatus,
       "cec118AArcPACab1": cec118AArcPACab1,
       "cec118AArcPACab2": cec118AArcPACab2,
       "cec118AArcTeeNetVario1": cec118AArcTeeNetVario1,
       "cec118AArcTeeNetVario2": cec118AArcTeeNetVario2,
       "cec118AArcTeeNetCap": cec118AArcTeeNetCap,
       "cec118AArcPACab1Test": cec118AArcPACab1Test,
       "cec118AArcPACab2Test": cec118AArcPACab2Test,
       "cec118AArcTeeNetVario1Test": cec118AArcTeeNetVario1Test,
       "cec118AArcTeeNetVario2Test": cec118AArcTeeNetVario2Test,
       "cec118AArcTeeNetCapTest": cec118AArcTeeNetCapTest,
       "cec118AAntennaCurrentMagnitude": cec118AAntennaCurrentMagnitude,
       "cec118AAntennaCurrentPhase": cec118AAntennaCurrentPhase,
       "cec118AConnectedToDummyLoad": cec118AConnectedToDummyLoad,
       "cec118AConnectedToAntenna": cec118AConnectedToAntenna,
       "cec118AGroundSwitchStatus": cec118AGroundSwitchStatus,
       "cec118ASupplyTemperature": cec118ASupplyTemperature,
       "cec118AExhaustTemperature": cec118AExhaustTemperature,
       "cec118AHours": cec118AHours,
       "cec118ADateAndTime": cec118ADateAndTime,
       "cec118AHardwareVersion": cec118AHardwareVersion,
       "cec118ASoftwareVersion": cec118ASoftwareVersion,
       "cec118ASummaryFault": cec118ASummaryFault,
       "cec118AFaultResetCmd": cec118AFaultResetCmd,
       "cec118AOperate": cec118AOperate,
       "cec118AOperateStatus": cec118AOperateStatus,
       "cec118ADCOn": cec118ADCOn,
       "cec118ADCOnStatus": cec118ADCOnStatus,
       "cec118AWFGPACab1Doors": cec118AWFGPACab1Doors,
       "cec118AWFGPACab2Doors": cec118AWFGPACab2Doors,
       "cec118AACOn": cec118AACOn,
       "cec118AACOnStatus": cec118AACOnStatus,
       "cec118AFansOn": cec118AFansOn,
       "cec118ACoolingOnStatus": cec118ACoolingOnStatus,
       "cec118AExternalCoolingIsOn": cec118AExternalCoolingIsOn,
       "cec118ARFLevelControlInput": cec118ARFLevelControlInput,
       "cec118APALevelPercentPower": cec118APALevelPercentPower,
       "cec118ARemoteLocalStatus": cec118ARemoteLocalStatus,
       "cec118AAntSampleClipStatus": cec118AAntSampleClipStatus,
       "cec118AAntSampleLowLevelStatus": cec118AAntSampleLowLevelStatus,
       "cec118AAnt11SampleInputLevel": cec118AAnt11SampleInputLevel,
       "cec118AAnt12SampleInputLevel": cec118AAnt12SampleInputLevel,
       "cec118AAnt13SampleInputLevel": cec118AAnt13SampleInputLevel,
       "cec118AAnt14SampleInputLevel": cec118AAnt14SampleInputLevel,
       "cec118AAnt21SampleInputLevel": cec118AAnt21SampleInputLevel,
       "cec118AAnt22SampleInputLevel": cec118AAnt22SampleInputLevel,
       "cec118AAnt23SampleInputLevel": cec118AAnt23SampleInputLevel,
       "cec118AAnt24SampleInputLevel": cec118AAnt24SampleInputLevel,
       "cec118ATxCtrlEq": cec118ATxCtrlEq}
)
