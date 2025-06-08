# SNMP MIB module (EatonSTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exide_534/EatonSTS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:56:03 2025
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

_Eaton_ObjectIdentity = ObjectIdentity
eaton = _Eaton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534)
)
_Sts_ObjectIdentity = ObjectIdentity
sts = _Sts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10)
)
_Ats_ObjectIdentity = ObjectIdentity
ats = _Ats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1)
)
_AtsAgent_ObjectIdentity = ObjectIdentity
atsAgent = _AtsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 1)
)


class _AtsAgentManufacturer_Type(DisplayString):
    """Custom type atsAgentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtsAgentManufacturer_Type.__name__ = "DisplayString"
_AtsAgentManufacturer_Object = MibScalar
atsAgentManufacturer = _AtsAgentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 1, 1),
    _AtsAgentManufacturer_Type()
)
atsAgentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsAgentManufacturer.setStatus("mandatory")


class _AtsAgentVersion_Type(DisplayString):
    """Custom type atsAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtsAgentVersion_Type.__name__ = "DisplayString"
_AtsAgentVersion_Object = MibScalar
atsAgentVersion = _AtsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 1, 2),
    _AtsAgentVersion_Type()
)
atsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsAgentVersion.setStatus("mandatory")
_AtsAgentModbus_ObjectIdentity = ObjectIdentity
atsAgentModbus = _AtsAgentModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 1, 3)
)


class _AtsAgentModbusLink_Type(Integer32):
    """Custom type atsAgentModbusLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("un-linked", 2))
    )


_AtsAgentModbusLink_Type.__name__ = "Integer32"
_AtsAgentModbusLink_Object = MibScalar
atsAgentModbusLink = _AtsAgentModbusLink_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 1, 3, 1),
    _AtsAgentModbusLink_Type()
)
atsAgentModbusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsAgentModbusLink.setStatus("mandatory")
_AtsIdent_ObjectIdentity = ObjectIdentity
atsIdent = _AtsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 2)
)


class _AtsIdentModel_Type(DisplayString):
    """Custom type atsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtsIdentModel_Type.__name__ = "DisplayString"
_AtsIdentModel_Object = MibScalar
atsIdentModel = _AtsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 2, 1),
    _AtsIdentModel_Type()
)
atsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentModel.setStatus("mandatory")


class _AtsIdentFWVersion_Type(DisplayString):
    """Custom type atsIdentFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtsIdentFWVersion_Type.__name__ = "DisplayString"
_AtsIdentFWVersion_Object = MibScalar
atsIdentFWVersion = _AtsIdentFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 2, 2),
    _AtsIdentFWVersion_Type()
)
atsIdentFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentFWVersion.setStatus("mandatory")


class _AtsIdentRelease_Type(DisplayString):
    """Custom type atsIdentRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtsIdentRelease_Type.__name__ = "DisplayString"
_AtsIdentRelease_Object = MibScalar
atsIdentRelease = _AtsIdentRelease_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 2, 3),
    _AtsIdentRelease_Type()
)
atsIdentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentRelease.setStatus("mandatory")


class _AtsIdentSerialNumber_Type(DisplayString):
    """Custom type atsIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtsIdentSerialNumber_Type.__name__ = "DisplayString"
_AtsIdentSerialNumber_Object = MibScalar
atsIdentSerialNumber = _AtsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 2, 4),
    _AtsIdentSerialNumber_Type()
)
atsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsIdentSerialNumber.setStatus("mandatory")


class _AtsIdentIDCodes_Type(DisplayString):
    """Custom type atsIdentIDCodes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtsIdentIDCodes_Type.__name__ = "DisplayString"
_AtsIdentIDCodes_Object = MibScalar
atsIdentIDCodes = _AtsIdentIDCodes_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 2, 5),
    _AtsIdentIDCodes_Type()
)
atsIdentIDCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsIdentIDCodes.setStatus("mandatory")
_AtsMeasure_ObjectIdentity = ObjectIdentity
atsMeasure = _AtsMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3)
)
_AtsInputTable_Object = MibTable
atsInputTable = _AtsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atsInputTable.setStatus("mandatory")
_AtsInputEntry_Object = MibTableRow
atsInputEntry = _AtsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 1, 1)
)
atsInputEntry.setIndexNames(
    (0, "EatonSTS-MIB", "atsInputIndex"),
)
if mibBuilder.loadTexts:
    atsInputEntry.setStatus("mandatory")


class _AtsInputIndex_Type(Integer32):
    """Custom type atsInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source-1", 1),
          ("source-2", 2))
    )


_AtsInputIndex_Type.__name__ = "Integer32"
_AtsInputIndex_Object = MibTableColumn
atsInputIndex = _AtsInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 1, 1, 1),
    _AtsInputIndex_Type()
)
atsInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputIndex.setStatus("mandatory")
_AtsInputVoltage_Type = Integer32
_AtsInputVoltage_Object = MibTableColumn
atsInputVoltage = _AtsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 1, 1, 2),
    _AtsInputVoltage_Type()
)
atsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputVoltage.setUnits("0.1 V")
_AtsInputFrequency_Type = Integer32
_AtsInputFrequency_Object = MibTableColumn
atsInputFrequency = _AtsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 1, 1, 3),
    _AtsInputFrequency_Type()
)
atsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsInputFrequency.setUnits("0.1 Hz")
_AtsOutput_ObjectIdentity = ObjectIdentity
atsOutput = _AtsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 2)
)
_AtsOutputVoltage_Type = Integer32
_AtsOutputVoltage_Object = MibScalar
atsOutputVoltage = _AtsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 2, 1),
    _AtsOutputVoltage_Type()
)
atsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputVoltage.setUnits("0.1 V")
_AtsOutputCurrent_Type = Integer32
_AtsOutputCurrent_Object = MibScalar
atsOutputCurrent = _AtsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 2, 2),
    _AtsOutputCurrent_Type()
)
atsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsOutputCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsOutputCurrent.setUnits("0.1 A")
_AtsMeasureTemperatureC_Type = Integer32
_AtsMeasureTemperatureC_Object = MibScalar
atsMeasureTemperatureC = _AtsMeasureTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 3),
    _AtsMeasureTemperatureC_Type()
)
atsMeasureTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMeasureTemperatureC.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsMeasureTemperatureC.setUnits("1 Celsius")
_AtsMeasureTemperatureF_Type = Integer32
_AtsMeasureTemperatureF_Object = MibScalar
atsMeasureTemperatureF = _AtsMeasureTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 4),
    _AtsMeasureTemperatureF_Type()
)
atsMeasureTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMeasureTemperatureF.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsMeasureTemperatureF.setUnits("1 Fahrenheit")
_AtsMessureRunTime_Type = Integer32
_AtsMessureRunTime_Object = MibScalar
atsMessureRunTime = _AtsMessureRunTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 5),
    _AtsMessureRunTime_Type()
)
atsMessureRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMessureRunTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsMessureRunTime.setUnits("1 second")
_AtsMessureTransferedTimes_Type = Integer32
_AtsMessureTransferedTimes_Object = MibScalar
atsMessureTransferedTimes = _AtsMessureTransferedTimes_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 6),
    _AtsMessureTransferedTimes_Type()
)
atsMessureTransferedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMessureTransferedTimes.setStatus("mandatory")


class _AtsMessureOperationMode_Type(Integer32):
    """Custom type atsMessureOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("initialization", 1),
          ("diagnosis", 2),
          ("off", 3),
          ("source-1", 4),
          ("source-2", 5),
          ("safe", 6),
          ("fault", 7))
    )


_AtsMessureOperationMode_Type.__name__ = "Integer32"
_AtsMessureOperationMode_Object = MibScalar
atsMessureOperationMode = _AtsMessureOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 3, 7),
    _AtsMessureOperationMode_Type()
)
atsMessureOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsMessureOperationMode.setStatus("mandatory")
_AtsStatus_ObjectIdentity = ObjectIdentity
atsStatus = _AtsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4)
)
_AtsInputFlowIndicator_Type = Integer32
_AtsInputFlowIndicator_Object = MibScalar
atsInputFlowIndicator = _AtsInputFlowIndicator_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 1),
    _AtsInputFlowIndicator_Type()
)
atsInputFlowIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFlowIndicator.setStatus("mandatory")
_AtsInputFlowTable_Object = MibTable
atsInputFlowTable = _AtsInputFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 2)
)
if mibBuilder.loadTexts:
    atsInputFlowTable.setStatus("mandatory")
_AtsInputFlowEntry_Object = MibTableRow
atsInputFlowEntry = _AtsInputFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 2, 1)
)
atsInputFlowEntry.setIndexNames(
    (0, "EatonSTS-MIB", "atsInputFlowIndex"),
)
if mibBuilder.loadTexts:
    atsInputFlowEntry.setStatus("mandatory")


class _AtsInputFlowIndex_Type(Integer32):
    """Custom type atsInputFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source-1", 1),
          ("source-2", 2))
    )


_AtsInputFlowIndex_Type.__name__ = "Integer32"
_AtsInputFlowIndex_Object = MibTableColumn
atsInputFlowIndex = _AtsInputFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 2, 1, 1),
    _AtsInputFlowIndex_Type()
)
atsInputFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFlowIndex.setStatus("mandatory")


class _AtsInputFlowRelay_Type(Integer32):
    """Custom type atsInputFlowRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AtsInputFlowRelay_Type.__name__ = "Integer32"
_AtsInputFlowRelay_Object = MibTableColumn
atsInputFlowRelay = _AtsInputFlowRelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 2, 1, 2),
    _AtsInputFlowRelay_Type()
)
atsInputFlowRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFlowRelay.setStatus("mandatory")


class _AtsInputFlowSCR_Type(Integer32):
    """Custom type atsInputFlowSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AtsInputFlowSCR_Type.__name__ = "Integer32"
_AtsInputFlowSCR_Object = MibTableColumn
atsInputFlowSCR = _AtsInputFlowSCR_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 2, 1, 3),
    _AtsInputFlowSCR_Type()
)
atsInputFlowSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFlowSCR.setStatus("mandatory")


class _AtsInputFlowParallelRelay_Type(Integer32):
    """Custom type atsInputFlowParallelRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AtsInputFlowParallelRelay_Type.__name__ = "Integer32"
_AtsInputFlowParallelRelay_Object = MibTableColumn
atsInputFlowParallelRelay = _AtsInputFlowParallelRelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 2, 1, 4),
    _AtsInputFlowParallelRelay_Type()
)
atsInputFlowParallelRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFlowParallelRelay.setStatus("mandatory")
_AtsInputFailureIndicator_Type = Integer32
_AtsInputFailureIndicator_Object = MibScalar
atsInputFailureIndicator = _AtsInputFailureIndicator_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 3),
    _AtsInputFailureIndicator_Type()
)
atsInputFailureIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureIndicator.setStatus("mandatory")
_AtsInputFailureTable_Object = MibTable
atsInputFailureTable = _AtsInputFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4)
)
if mibBuilder.loadTexts:
    atsInputFailureTable.setStatus("mandatory")
_AtsInputFailureEntry_Object = MibTableRow
atsInputFailureEntry = _AtsInputFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1)
)
atsInputFailureEntry.setIndexNames(
    (0, "EatonSTS-MIB", "atsInputFailureIndex"),
)
if mibBuilder.loadTexts:
    atsInputFailureEntry.setStatus("mandatory")


class _AtsInputFailureIndex_Type(Integer32):
    """Custom type atsInputFailureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source-1", 1),
          ("source-2", 2))
    )


_AtsInputFailureIndex_Type.__name__ = "Integer32"
_AtsInputFailureIndex_Object = MibTableColumn
atsInputFailureIndex = _AtsInputFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 1),
    _AtsInputFailureIndex_Type()
)
atsInputFailureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureIndex.setStatus("mandatory")


class _AtsInputFailureRelayOpen_Type(Integer32):
    """Custom type atsInputFailureRelayOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureRelayOpen_Type.__name__ = "Integer32"
_AtsInputFailureRelayOpen_Object = MibTableColumn
atsInputFailureRelayOpen = _AtsInputFailureRelayOpen_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 2),
    _AtsInputFailureRelayOpen_Type()
)
atsInputFailureRelayOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureRelayOpen.setStatus("mandatory")


class _AtsInputFailureRelayShort_Type(Integer32):
    """Custom type atsInputFailureRelayShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureRelayShort_Type.__name__ = "Integer32"
_AtsInputFailureRelayShort_Object = MibTableColumn
atsInputFailureRelayShort = _AtsInputFailureRelayShort_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 3),
    _AtsInputFailureRelayShort_Type()
)
atsInputFailureRelayShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureRelayShort.setStatus("mandatory")


class _AtsInputFailureSCROpen_Type(Integer32):
    """Custom type atsInputFailureSCROpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureSCROpen_Type.__name__ = "Integer32"
_AtsInputFailureSCROpen_Object = MibTableColumn
atsInputFailureSCROpen = _AtsInputFailureSCROpen_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 4),
    _AtsInputFailureSCROpen_Type()
)
atsInputFailureSCROpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureSCROpen.setStatus("mandatory")


class _AtsInputFailureSCRShort_Type(Integer32):
    """Custom type atsInputFailureSCRShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureSCRShort_Type.__name__ = "Integer32"
_AtsInputFailureSCRShort_Object = MibTableColumn
atsInputFailureSCRShort = _AtsInputFailureSCRShort_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 5),
    _AtsInputFailureSCRShort_Type()
)
atsInputFailureSCRShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureSCRShort.setStatus("mandatory")


class _AtsInputFailureSCRThermal_Type(Integer32):
    """Custom type atsInputFailureSCRThermal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureSCRThermal_Type.__name__ = "Integer32"
_AtsInputFailureSCRThermal_Object = MibTableColumn
atsInputFailureSCRThermal = _AtsInputFailureSCRThermal_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 6),
    _AtsInputFailureSCRThermal_Type()
)
atsInputFailureSCRThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureSCRThermal.setStatus("mandatory")


class _AtsInputFailureAuxPower_Type(Integer32):
    """Custom type atsInputFailureAuxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureAuxPower_Type.__name__ = "Integer32"
_AtsInputFailureAuxPower_Object = MibTableColumn
atsInputFailureAuxPower = _AtsInputFailureAuxPower_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 7),
    _AtsInputFailureAuxPower_Type()
)
atsInputFailureAuxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureAuxPower.setStatus("mandatory")


class _AtsInputFailureDrop_Type(Integer32):
    """Custom type atsInputFailureDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureDrop_Type.__name__ = "Integer32"
_AtsInputFailureDrop_Object = MibTableColumn
atsInputFailureDrop = _AtsInputFailureDrop_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 8),
    _AtsInputFailureDrop_Type()
)
atsInputFailureDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureDrop.setStatus("mandatory")


class _AtsInputFailureBrownout_Type(Integer32):
    """Custom type atsInputFailureBrownout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureBrownout_Type.__name__ = "Integer32"
_AtsInputFailureBrownout_Object = MibTableColumn
atsInputFailureBrownout = _AtsInputFailureBrownout_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 9),
    _AtsInputFailureBrownout_Type()
)
atsInputFailureBrownout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureBrownout.setStatus("mandatory")


class _AtsInputFailureFrequency_Type(Integer32):
    """Custom type atsInputFailureFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureFrequency_Type.__name__ = "Integer32"
_AtsInputFailureFrequency_Object = MibTableColumn
atsInputFailureFrequency = _AtsInputFailureFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 10),
    _AtsInputFailureFrequency_Type()
)
atsInputFailureFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureFrequency.setStatus("mandatory")


class _AtsInputFailureNotOperable_Type(Integer32):
    """Custom type atsInputFailureNotOperable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsInputFailureNotOperable_Type.__name__ = "Integer32"
_AtsInputFailureNotOperable_Object = MibTableColumn
atsInputFailureNotOperable = _AtsInputFailureNotOperable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 4, 1, 11),
    _AtsInputFailureNotOperable_Type()
)
atsInputFailureNotOperable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsInputFailureNotOperable.setStatus("mandatory")
_AtsFailureIndicator_Type = Integer32
_AtsFailureIndicator_Object = MibScalar
atsFailureIndicator = _AtsFailureIndicator_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 5),
    _AtsFailureIndicator_Type()
)
atsFailureIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsFailureIndicator.setStatus("mandatory")
_AtsFailure_ObjectIdentity = ObjectIdentity
atsFailure = _AtsFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 6)
)


class _AtsFailureSwitchFault_Type(Integer32):
    """Custom type atsFailureSwitchFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsFailureSwitchFault_Type.__name__ = "Integer32"
_AtsFailureSwitchFault_Object = MibScalar
atsFailureSwitchFault = _AtsFailureSwitchFault_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 6, 1),
    _AtsFailureSwitchFault_Type()
)
atsFailureSwitchFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsFailureSwitchFault.setStatus("mandatory")


class _AtsFailureNoOutput_Type(Integer32):
    """Custom type atsFailureNoOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsFailureNoOutput_Type.__name__ = "Integer32"
_AtsFailureNoOutput_Object = MibScalar
atsFailureNoOutput = _AtsFailureNoOutput_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 6, 2),
    _AtsFailureNoOutput_Type()
)
atsFailureNoOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsFailureNoOutput.setStatus("mandatory")


class _AtsFailureOutputOC_Type(Integer32):
    """Custom type atsFailureOutputOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsFailureOutputOC_Type.__name__ = "Integer32"
_AtsFailureOutputOC_Object = MibScalar
atsFailureOutputOC = _AtsFailureOutputOC_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 6, 3),
    _AtsFailureOutputOC_Type()
)
atsFailureOutputOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsFailureOutputOC.setStatus("mandatory")


class _AtsFailureOverTemperature_Type(Integer32):
    """Custom type atsFailureOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("normal", 2))
    )


_AtsFailureOverTemperature_Type.__name__ = "Integer32"
_AtsFailureOverTemperature_Object = MibScalar
atsFailureOverTemperature = _AtsFailureOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 4, 6, 4),
    _AtsFailureOverTemperature_Type()
)
atsFailureOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsFailureOverTemperature.setStatus("mandatory")
_AtsLog_ObjectIdentity = ObjectIdentity
atsLog = _AtsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5)
)
_AtsLogNum_Type = Integer32
_AtsLogNum_Object = MibScalar
atsLogNum = _AtsLogNum_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 1),
    _AtsLogNum_Type()
)
atsLogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLogNum.setStatus("mandatory")
_AtsLogTable_Object = MibTable
atsLogTable = _AtsLogTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 2)
)
if mibBuilder.loadTexts:
    atsLogTable.setStatus("mandatory")
_AtsLogEntry_Object = MibTableRow
atsLogEntry = _AtsLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 2, 1)
)
atsLogEntry.setIndexNames(
    (0, "EatonSTS-MIB", "atsLogIndex"),
)
if mibBuilder.loadTexts:
    atsLogEntry.setStatus("mandatory")


class _AtsLogIndex_Type(Integer32):
    """Custom type atsLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtsLogIndex_Type.__name__ = "Integer32"
_AtsLogIndex_Object = MibTableColumn
atsLogIndex = _AtsLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 2, 1, 1),
    _AtsLogIndex_Type()
)
atsLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLogIndex.setStatus("mandatory")
_AtsLogTime_Type = TimeTicks
_AtsLogTime_Object = MibTableColumn
atsLogTime = _AtsLogTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 2, 1, 2),
    _AtsLogTime_Type()
)
atsLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLogTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsLogTime.setUnits("1 Second")
_AtsLogCode_Type = Integer32
_AtsLogCode_Object = MibTableColumn
atsLogCode = _AtsLogCode_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 2, 1, 3),
    _AtsLogCode_Type()
)
atsLogCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLogCode.setStatus("mandatory")


class _AtsLogTimeText_Type(DisplayString):
    """Custom type atsLogTimeText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AtsLogTimeText_Type.__name__ = "DisplayString"
_AtsLogTimeText_Object = MibTableColumn
atsLogTimeText = _AtsLogTimeText_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 5, 2, 1, 4),
    _AtsLogTimeText_Type()
)
atsLogTimeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsLogTimeText.setStatus("mandatory")
_AtsConfig_ObjectIdentity = ObjectIdentity
atsConfig = _AtsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6)
)
_AtsConfigTime_ObjectIdentity = ObjectIdentity
atsConfigTime = _AtsConfigTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 1)
)
_AtsConfigTimeRTC_Type = Integer32
_AtsConfigTimeRTC_Object = MibScalar
atsConfigTimeRTC = _AtsConfigTimeRTC_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 1, 1),
    _AtsConfigTimeRTC_Type()
)
atsConfigTimeRTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigTimeRTC.setStatus("mandatory")


class _AtsConfigTimeTextDate_Type(DisplayString):
    """Custom type atsConfigTimeTextDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AtsConfigTimeTextDate_Type.__name__ = "DisplayString"
_AtsConfigTimeTextDate_Object = MibScalar
atsConfigTimeTextDate = _AtsConfigTimeTextDate_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 1, 2),
    _AtsConfigTimeTextDate_Type()
)
atsConfigTimeTextDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigTimeTextDate.setStatus("mandatory")


class _AtsConfigTimeTextTime_Type(DisplayString):
    """Custom type atsConfigTimeTextTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtsConfigTimeTextTime_Type.__name__ = "DisplayString"
_AtsConfigTimeTextTime_Object = MibScalar
atsConfigTimeTextTime = _AtsConfigTimeTextTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 1, 3),
    _AtsConfigTimeTextTime_Type()
)
atsConfigTimeTextTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigTimeTextTime.setStatus("mandatory")
_AtsConfigInputTable_Object = MibTable
atsConfigInputTable = _AtsConfigInputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2)
)
if mibBuilder.loadTexts:
    atsConfigInputTable.setStatus("mandatory")
_AtsConfigInputEntry_Object = MibTableRow
atsConfigInputEntry = _AtsConfigInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1)
)
atsConfigInputEntry.setIndexNames(
    (0, "EatonSTS-MIB", "atsConfigInputIndex"),
)
if mibBuilder.loadTexts:
    atsConfigInputEntry.setStatus("mandatory")


class _AtsConfigInputIndex_Type(Integer32):
    """Custom type atsConfigInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AtsConfigInputIndex_Type.__name__ = "Integer32"
_AtsConfigInputIndex_Object = MibTableColumn
atsConfigInputIndex = _AtsConfigInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 1),
    _AtsConfigInputIndex_Type()
)
atsConfigInputIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputIndex.setStatus("mandatory")
_AtsConfigInputTrip_Type = Integer32
_AtsConfigInputTrip_Object = MibTableColumn
atsConfigInputTrip = _AtsConfigInputTrip_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 2),
    _AtsConfigInputTrip_Type()
)
atsConfigInputTrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputTrip.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputTrip.setUnits("0.1 V")
_AtsConfigInputBrownoutLow_Type = Integer32
_AtsConfigInputBrownoutLow_Object = MibTableColumn
atsConfigInputBrownoutLow = _AtsConfigInputBrownoutLow_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 3),
    _AtsConfigInputBrownoutLow_Type()
)
atsConfigInputBrownoutLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputBrownoutLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputBrownoutLow.setUnits("0.1 V")
_AtsConfigInputBrownoutHigh_Type = Integer32
_AtsConfigInputBrownoutHigh_Object = MibTableColumn
atsConfigInputBrownoutHigh = _AtsConfigInputBrownoutHigh_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 4),
    _AtsConfigInputBrownoutHigh_Type()
)
atsConfigInputBrownoutHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputBrownoutHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputBrownoutHigh.setUnits("0.1 V")
_AtsConfigInputRecover_Type = Integer32
_AtsConfigInputRecover_Object = MibTableColumn
atsConfigInputRecover = _AtsConfigInputRecover_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 5),
    _AtsConfigInputRecover_Type()
)
atsConfigInputRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputRecover.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputRecover.setUnits("0.1 Second")
_AtsConfigInputMaxVoltage_Type = Integer32
_AtsConfigInputMaxVoltage_Object = MibTableColumn
atsConfigInputMaxVoltage = _AtsConfigInputMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 6),
    _AtsConfigInputMaxVoltage_Type()
)
atsConfigInputMaxVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputMaxVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputMaxVoltage.setUnits("1 V")
_AtsConfigInputMaxTime_Type = Integer32
_AtsConfigInputMaxTime_Object = MibTableColumn
atsConfigInputMaxTime = _AtsConfigInputMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 7),
    _AtsConfigInputMaxTime_Type()
)
atsConfigInputMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigInputMaxTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputMaxTime.setUnits("0.1 Second")
_AtsConfigInputDelayTime_Type = Integer32
_AtsConfigInputDelayTime_Object = MibTableColumn
atsConfigInputDelayTime = _AtsConfigInputDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 2, 1, 8),
    _AtsConfigInputDelayTime_Type()
)
atsConfigInputDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsConfigInputDelayTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputDelayTime.setUnits("0.1 Second")
_AtsConfigInputVoltageRating_Type = Integer32
_AtsConfigInputVoltageRating_Object = MibScalar
atsConfigInputVoltageRating = _AtsConfigInputVoltageRating_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 3),
    _AtsConfigInputVoltageRating_Type()
)
atsConfigInputVoltageRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsConfigInputVoltageRating.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigInputVoltageRating.setUnits("0.1 V")
_AtsConfigRandomTime_Type = Integer32
_AtsConfigRandomTime_Object = MibScalar
atsConfigRandomTime = _AtsConfigRandomTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 4),
    _AtsConfigRandomTime_Type()
)
atsConfigRandomTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsConfigRandomTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsConfigRandomTime.setUnits("0.1 Second")


class _AtsConfigPreferred_Type(Integer32):
    """Custom type atsConfigPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source-1", 1),
          ("source-2", 2))
    )


_AtsConfigPreferred_Type.__name__ = "Integer32"
_AtsConfigPreferred_Object = MibScalar
atsConfigPreferred = _AtsConfigPreferred_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 5),
    _AtsConfigPreferred_Type()
)
atsConfigPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigPreferred.setStatus("mandatory")


class _AtsConfigSensitivity_Type(Integer32):
    """Custom type atsConfigSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_AtsConfigSensitivity_Type.__name__ = "Integer32"
_AtsConfigSensitivity_Object = MibScalar
atsConfigSensitivity = _AtsConfigSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 6),
    _AtsConfigSensitivity_Type()
)
atsConfigSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigSensitivity.setStatus("mandatory")


class _AtsConfigTest_Type(Integer32):
    """Custom type atsConfigTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AtsConfigTest_Type.__name__ = "Integer32"
_AtsConfigTest_Object = MibScalar
atsConfigTest = _AtsConfigTest_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 6, 7),
    _AtsConfigTest_Type()
)
atsConfigTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsConfigTest.setStatus("mandatory")
_AtsUpgrade_ObjectIdentity = ObjectIdentity
atsUpgrade = _AtsUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 7)
)


class _AtsUpgradeProcess_Type(Integer32):
    """Custom type atsUpgradeProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("run", 2),
          ("error", 3))
    )


_AtsUpgradeProcess_Type.__name__ = "Integer32"
_AtsUpgradeProcess_Object = MibScalar
atsUpgradeProcess = _AtsUpgradeProcess_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 7, 1),
    _AtsUpgradeProcess_Type()
)
atsUpgradeProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsUpgradeProcess.setStatus("mandatory")


class _AtsUpgradeStep_Type(Integer32):
    """Custom type atsUpgradeStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("fileid", 2),
          ("auth", 3),
          ("addr", 4),
          ("erase", 5),
          ("program", 6),
          ("read", 7))
    )


_AtsUpgradeStep_Type.__name__ = "Integer32"
_AtsUpgradeStep_Object = MibScalar
atsUpgradeStep = _AtsUpgradeStep_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 7, 2),
    _AtsUpgradeStep_Type()
)
atsUpgradeStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsUpgradeStep.setStatus("mandatory")
_AtsUpgradePercentage_Type = Integer32
_AtsUpgradePercentage_Object = MibScalar
atsUpgradePercentage = _AtsUpgradePercentage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 7, 3),
    _AtsUpgradePercentage_Type()
)
atsUpgradePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsUpgradePercentage.setStatus("mandatory")
if mibBuilder.loadTexts:
    atsUpgradePercentage.setUnits("0.1%")
_AtsTraps_ObjectIdentity = ObjectIdentity
atsTraps = _AtsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20)
)

# Managed Objects groups


# Notification objects

atsTrapCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 1)
)
if mibBuilder.loadTexts:
    atsTrapCommLost.setStatus(
        ""
    )

atsTrapCommEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 2)
)
if mibBuilder.loadTexts:
    atsTrapCommEstablished.setStatus(
        ""
    )

atsTrapConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 3)
)
if mibBuilder.loadTexts:
    atsTrapConfigChange.setStatus(
        ""
    )

atsTrapFlowChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 4)
)
if mibBuilder.loadTexts:
    atsTrapFlowChange.setStatus(
        ""
    )

atsTrapInput1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 5)
)
if mibBuilder.loadTexts:
    atsTrapInput1Alarm.setStatus(
        ""
    )

atsTrapInput1AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 6)
)
if mibBuilder.loadTexts:
    atsTrapInput1AlarmRecover.setStatus(
        ""
    )

atsTrapInput2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 7)
)
if mibBuilder.loadTexts:
    atsTrapInput2Alarm.setStatus(
        ""
    )

atsTrapInput2AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 8)
)
if mibBuilder.loadTexts:
    atsTrapInput2AlarmRecover.setStatus(
        ""
    )

atsTrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 9)
)
if mibBuilder.loadTexts:
    atsTrapAlarm.setStatus(
        ""
    )

atsTrapAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 10)
)
if mibBuilder.loadTexts:
    atsTrapAlarmRecover.setStatus(
        ""
    )

atsTrapUpgradeBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 11)
)
if mibBuilder.loadTexts:
    atsTrapUpgradeBegin.setStatus(
        ""
    )

atsTrapUpgradeEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 1, 20, 0, 12)
)
if mibBuilder.loadTexts:
    atsTrapUpgradeEnd.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EatonSTS-MIB",
    **{"eaton": eaton,
       "sts": sts,
       "ats": ats,
       "atsAgent": atsAgent,
       "atsAgentManufacturer": atsAgentManufacturer,
       "atsAgentVersion": atsAgentVersion,
       "atsAgentModbus": atsAgentModbus,
       "atsAgentModbusLink": atsAgentModbusLink,
       "atsIdent": atsIdent,
       "atsIdentModel": atsIdentModel,
       "atsIdentFWVersion": atsIdentFWVersion,
       "atsIdentRelease": atsIdentRelease,
       "atsIdentSerialNumber": atsIdentSerialNumber,
       "atsIdentIDCodes": atsIdentIDCodes,
       "atsMeasure": atsMeasure,
       "atsInputTable": atsInputTable,
       "atsInputEntry": atsInputEntry,
       "atsInputIndex": atsInputIndex,
       "atsInputVoltage": atsInputVoltage,
       "atsInputFrequency": atsInputFrequency,
       "atsOutput": atsOutput,
       "atsOutputVoltage": atsOutputVoltage,
       "atsOutputCurrent": atsOutputCurrent,
       "atsMeasureTemperatureC": atsMeasureTemperatureC,
       "atsMeasureTemperatureF": atsMeasureTemperatureF,
       "atsMessureRunTime": atsMessureRunTime,
       "atsMessureTransferedTimes": atsMessureTransferedTimes,
       "atsMessureOperationMode": atsMessureOperationMode,
       "atsStatus": atsStatus,
       "atsInputFlowIndicator": atsInputFlowIndicator,
       "atsInputFlowTable": atsInputFlowTable,
       "atsInputFlowEntry": atsInputFlowEntry,
       "atsInputFlowIndex": atsInputFlowIndex,
       "atsInputFlowRelay": atsInputFlowRelay,
       "atsInputFlowSCR": atsInputFlowSCR,
       "atsInputFlowParallelRelay": atsInputFlowParallelRelay,
       "atsInputFailureIndicator": atsInputFailureIndicator,
       "atsInputFailureTable": atsInputFailureTable,
       "atsInputFailureEntry": atsInputFailureEntry,
       "atsInputFailureIndex": atsInputFailureIndex,
       "atsInputFailureRelayOpen": atsInputFailureRelayOpen,
       "atsInputFailureRelayShort": atsInputFailureRelayShort,
       "atsInputFailureSCROpen": atsInputFailureSCROpen,
       "atsInputFailureSCRShort": atsInputFailureSCRShort,
       "atsInputFailureSCRThermal": atsInputFailureSCRThermal,
       "atsInputFailureAuxPower": atsInputFailureAuxPower,
       "atsInputFailureDrop": atsInputFailureDrop,
       "atsInputFailureBrownout": atsInputFailureBrownout,
       "atsInputFailureFrequency": atsInputFailureFrequency,
       "atsInputFailureNotOperable": atsInputFailureNotOperable,
       "atsFailureIndicator": atsFailureIndicator,
       "atsFailure": atsFailure,
       "atsFailureSwitchFault": atsFailureSwitchFault,
       "atsFailureNoOutput": atsFailureNoOutput,
       "atsFailureOutputOC": atsFailureOutputOC,
       "atsFailureOverTemperature": atsFailureOverTemperature,
       "atsLog": atsLog,
       "atsLogNum": atsLogNum,
       "atsLogTable": atsLogTable,
       "atsLogEntry": atsLogEntry,
       "atsLogIndex": atsLogIndex,
       "atsLogTime": atsLogTime,
       "atsLogCode": atsLogCode,
       "atsLogTimeText": atsLogTimeText,
       "atsConfig": atsConfig,
       "atsConfigTime": atsConfigTime,
       "atsConfigTimeRTC": atsConfigTimeRTC,
       "atsConfigTimeTextDate": atsConfigTimeTextDate,
       "atsConfigTimeTextTime": atsConfigTimeTextTime,
       "atsConfigInputTable": atsConfigInputTable,
       "atsConfigInputEntry": atsConfigInputEntry,
       "atsConfigInputIndex": atsConfigInputIndex,
       "atsConfigInputTrip": atsConfigInputTrip,
       "atsConfigInputBrownoutLow": atsConfigInputBrownoutLow,
       "atsConfigInputBrownoutHigh": atsConfigInputBrownoutHigh,
       "atsConfigInputRecover": atsConfigInputRecover,
       "atsConfigInputMaxVoltage": atsConfigInputMaxVoltage,
       "atsConfigInputMaxTime": atsConfigInputMaxTime,
       "atsConfigInputDelayTime": atsConfigInputDelayTime,
       "atsConfigInputVoltageRating": atsConfigInputVoltageRating,
       "atsConfigRandomTime": atsConfigRandomTime,
       "atsConfigPreferred": atsConfigPreferred,
       "atsConfigSensitivity": atsConfigSensitivity,
       "atsConfigTest": atsConfigTest,
       "atsUpgrade": atsUpgrade,
       "atsUpgradeProcess": atsUpgradeProcess,
       "atsUpgradeStep": atsUpgradeStep,
       "atsUpgradePercentage": atsUpgradePercentage,
       "atsTraps": atsTraps,
       "atsTrapCommLost": atsTrapCommLost,
       "atsTrapCommEstablished": atsTrapCommEstablished,
       "atsTrapConfigChange": atsTrapConfigChange,
       "atsTrapFlowChange": atsTrapFlowChange,
       "atsTrapInput1Alarm": atsTrapInput1Alarm,
       "atsTrapInput1AlarmRecover": atsTrapInput1AlarmRecover,
       "atsTrapInput2Alarm": atsTrapInput2Alarm,
       "atsTrapInput2AlarmRecover": atsTrapInput2AlarmRecover,
       "atsTrapAlarm": atsTrapAlarm,
       "atsTrapAlarmRecover": atsTrapAlarmRecover,
       "atsTrapUpgradeBegin": atsTrapUpgradeBegin,
       "atsTrapUpgradeEnd": atsTrapUpgradeEnd}
)
