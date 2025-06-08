# SNMP MIB module (DeltaIDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_2254/DeltaIDC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:49:11 2025
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
    (1, 3, 6, 1, 4, 1, 2254)
)
_Idc_ObjectIdentity = ObjectIdentity
idc = _Idc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1)
)


class _PduName_Type(DisplayString):
    """Custom type pduName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduName_Type.__name__ = "DisplayString"
_PduName_Object = MibScalar
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 1),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("current")


class _PduDescription_Type(DisplayString):
    """Custom type pduDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PduDescription_Type.__name__ = "DisplayString"
_PduDescription_Object = MibScalar
pduDescription = _PduDescription_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 2),
    _PduDescription_Type()
)
pduDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDescription.setStatus("current")


class _PduModelName_Type(DisplayString):
    """Custom type pduModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduModelName_Type.__name__ = "DisplayString"
_PduModelName_Object = MibScalar
pduModelName = _PduModelName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 3),
    _PduModelName_Type()
)
pduModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduModelName.setStatus("mandatory")


class _PduSerialNumber_Type(DisplayString):
    """Custom type pduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PduSerialNumber_Type.__name__ = "DisplayString"
_PduSerialNumber_Object = MibScalar
pduSerialNumber = _PduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 4),
    _PduSerialNumber_Type()
)
pduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSerialNumber.setStatus("current")


class _PduPartNumber_Type(DisplayString):
    """Custom type pduPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PduPartNumber_Type.__name__ = "DisplayString"
_PduPartNumber_Object = MibScalar
pduPartNumber = _PduPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 5),
    _PduPartNumber_Type()
)
pduPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPartNumber.setStatus("current")


class _PduFWVersion_Type(DisplayString):
    """Custom type pduFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduFWVersion_Type.__name__ = "DisplayString"
_PduFWVersion_Object = MibScalar
pduFWVersion = _PduFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 20),
    _PduFWVersion_Type()
)
pduFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFWVersion.setStatus("mandatory")
_PduMeterTable_Object = MibTable
pduMeterTable = _PduMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 21)
)
if mibBuilder.loadTexts:
    pduMeterTable.setStatus("current")
_PduMeterEntry_Object = MibTableRow
pduMeterEntry = _PduMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 21, 1)
)
pduMeterEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduMeterNumber"),
)
if mibBuilder.loadTexts:
    pduMeterEntry.setStatus("current")


class _PduMeterNumber_Type(Integer32):
    """Custom type pduMeterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduMeterNumber_Type.__name__ = "Integer32"
_PduMeterNumber_Object = MibTableColumn
pduMeterNumber = _PduMeterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 21, 1, 1),
    _PduMeterNumber_Type()
)
pduMeterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduMeterNumber.setStatus("current")


class _PduMeterVersion_Type(DisplayString):
    """Custom type pduMeterVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduMeterVersion_Type.__name__ = "DisplayString"
_PduMeterVersion_Object = MibTableColumn
pduMeterVersion = _PduMeterVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 21, 1, 2),
    _PduMeterVersion_Type()
)
pduMeterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeterVersion.setStatus("mandatory")


class _PduMeterSerial_Type(DisplayString):
    """Custom type pduMeterSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PduMeterSerial_Type.__name__ = "DisplayString"
_PduMeterSerial_Object = MibTableColumn
pduMeterSerial = _PduMeterSerial_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 21, 1, 4),
    _PduMeterSerial_Type()
)
pduMeterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeterSerial.setStatus("mandatory")


class _PduMeterDate_Type(DisplayString):
    """Custom type pduMeterDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PduMeterDate_Type.__name__ = "DisplayString"
_PduMeterDate_Object = MibTableColumn
pduMeterDate = _PduMeterDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 1, 21, 1, 5),
    _PduMeterDate_Type()
)
pduMeterDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeterDate.setStatus("mandatory")
_InputData_ObjectIdentity = ObjectIdentity
inputData = _InputData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2)
)


class _InputPhaseCount_Type(Integer32):
    """Custom type inputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("three", 3))
    )


_InputPhaseCount_Type.__name__ = "Integer32"
_InputPhaseCount_Object = MibScalar
inputPhaseCount = _InputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 1),
    _InputPhaseCount_Type()
)
inputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPhaseCount.setStatus("current")
_InputFrequency_Type = Unsigned32
_InputFrequency_Object = MibScalar
inputFrequency = _InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 2),
    _InputFrequency_Type()
)
inputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFrequency.setStatus("current")
_InputTotalCurrent_Type = Unsigned32
_InputTotalCurrent_Object = MibScalar
inputTotalCurrent = _InputTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 3),
    _InputTotalCurrent_Type()
)
inputTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalCurrent.setStatus("current")
_InputTotalPower_Type = Unsigned32
_InputTotalPower_Object = MibScalar
inputTotalPower = _InputTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 4),
    _InputTotalPower_Type()
)
inputTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalPower.setStatus("current")
_InputTotalEnergy_Type = Unsigned32
_InputTotalEnergy_Object = MibScalar
inputTotalEnergy = _InputTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 5),
    _InputTotalEnergy_Type()
)
inputTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalEnergy.setStatus("current")
_InputTotalReactivePower_Type = Unsigned32
_InputTotalReactivePower_Object = MibScalar
inputTotalReactivePower = _InputTotalReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 6),
    _InputTotalReactivePower_Type()
)
inputTotalReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalReactivePower.setStatus("current")
_InputTotalApparentPower_Type = Unsigned32
_InputTotalApparentPower_Object = MibScalar
inputTotalApparentPower = _InputTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 7),
    _InputTotalApparentPower_Type()
)
inputTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalApparentPower.setStatus("current")


class _InputClearTotalEnergy_Type(Integer32):
    """Custom type inputClearTotalEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_InputClearTotalEnergy_Type.__name__ = "Integer32"
_InputClearTotalEnergy_Object = MibScalar
inputClearTotalEnergy = _InputClearTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 8),
    _InputClearTotalEnergy_Type()
)
inputClearTotalEnergy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputClearTotalEnergy.setStatus("current")
_InputDataTable_Object = MibTable
inputDataTable = _InputDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9)
)
if mibBuilder.loadTexts:
    inputDataTable.setStatus("current")
_InputDataEntry_Object = MibTableRow
inputDataEntry = _InputDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1)
)
inputDataEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "inputPhaseNumber"),
)
if mibBuilder.loadTexts:
    inputDataEntry.setStatus("current")


class _InputPhaseNumber_Type(Integer32):
    """Custom type inputPhaseNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InputPhaseNumber_Type.__name__ = "Integer32"
_InputPhaseNumber_Object = MibTableColumn
inputPhaseNumber = _InputPhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 1),
    _InputPhaseNumber_Type()
)
inputPhaseNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputPhaseNumber.setStatus("current")
_InputVoltage_Type = Unsigned32
_InputVoltage_Object = MibTableColumn
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 2),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("current")
_InputCurrent_Type = Unsigned32
_InputCurrent_Object = MibTableColumn
inputCurrent = _InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 5),
    _InputCurrent_Type()
)
inputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrent.setStatus("current")
_InputPower_Type = Unsigned32
_InputPower_Object = MibTableColumn
inputPower = _InputPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 6),
    _InputPower_Type()
)
inputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPower.setStatus("current")
_InputEnergy_Type = Unsigned32
_InputEnergy_Object = MibTableColumn
inputEnergy = _InputEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 7),
    _InputEnergy_Type()
)
inputEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputEnergy.setStatus("current")
_InputReactivePower_Type = Unsigned32
_InputReactivePower_Object = MibTableColumn
inputReactivePower = _InputReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 8),
    _InputReactivePower_Type()
)
inputReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputReactivePower.setStatus("current")
_InputApparentPower_Type = Unsigned32
_InputApparentPower_Object = MibTableColumn
inputApparentPower = _InputApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 9),
    _InputApparentPower_Type()
)
inputApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputApparentPower.setStatus("current")
_InputPowerFactor_Type = Unsigned32
_InputPowerFactor_Object = MibTableColumn
inputPowerFactor = _InputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 10),
    _InputPowerFactor_Type()
)
inputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPowerFactor.setStatus("current")
_InputThdVoltage_Type = Unsigned32
_InputThdVoltage_Object = MibTableColumn
inputThdVoltage = _InputThdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 11),
    _InputThdVoltage_Type()
)
inputThdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputThdVoltage.setStatus("current")
_InputThdCurrent_Type = Unsigned32
_InputThdCurrent_Object = MibTableColumn
inputThdCurrent = _InputThdCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 12),
    _InputThdCurrent_Type()
)
inputThdCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputThdCurrent.setStatus("current")
_InputLineVoltage_Type = Unsigned32
_InputLineVoltage_Object = MibTableColumn
inputLineVoltage = _InputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 13),
    _InputLineVoltage_Type()
)
inputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLineVoltage.setStatus("current")
_InputLineCurrent_Type = Unsigned32
_InputLineCurrent_Object = MibTableColumn
inputLineCurrent = _InputLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 2, 9, 1, 14),
    _InputLineCurrent_Type()
)
inputLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLineCurrent.setStatus("current")
_OutputOutlet_ObjectIdentity = ObjectIdentity
outputOutlet = _OutputOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3)
)


class _PduPhaseCount_Type(Integer32):
    """Custom type pduPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("three", 3))
    )


_PduPhaseCount_Type.__name__ = "Integer32"
_PduPhaseCount_Object = MibScalar
pduPhaseCount = _PduPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 1),
    _PduPhaseCount_Type()
)
pduPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCount.setStatus("current")
_PduOutletCount_Type = Integer32
_PduOutletCount_Object = MibScalar
pduOutletCount = _PduOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 2),
    _PduOutletCount_Type()
)
pduOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletCount.setStatus("current")
_PduOutletTable_Object = MibTable
pduOutletTable = _PduOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pduOutletTable.setStatus("current")
_PduOutletEntry_Object = MibTableRow
pduOutletEntry = _PduOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1)
)
pduOutletEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduOutletNumber"),
)
if mibBuilder.loadTexts:
    pduOutletEntry.setStatus("current")


class _PduOutletNumber_Type(Integer32):
    """Custom type pduOutletNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduOutletNumber_Type.__name__ = "Integer32"
_PduOutletNumber_Object = MibTableColumn
pduOutletNumber = _PduOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 1),
    _PduOutletNumber_Type()
)
pduOutletNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletNumber.setStatus("current")


class _PduOutletName_Type(DisplayString):
    """Custom type pduOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PduOutletName_Type.__name__ = "DisplayString"
_PduOutletName_Object = MibTableColumn
pduOutletName = _PduOutletName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 2),
    _PduOutletName_Type()
)
pduOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletName.setStatus("current")


class _PduOutletDescription_Type(DisplayString):
    """Custom type pduOutletDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduOutletDescription_Type.__name__ = "DisplayString"
_PduOutletDescription_Object = MibTableColumn
pduOutletDescription = _PduOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 3),
    _PduOutletDescription_Type()
)
pduOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletDescription.setStatus("current")
_PduOutletVoltage1_Type = Unsigned32
_PduOutletVoltage1_Object = MibTableColumn
pduOutletVoltage1 = _PduOutletVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 4),
    _PduOutletVoltage1_Type()
)
pduOutletVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletVoltage1.setStatus("current")
_PduOutletVoltage2_Type = Unsigned32
_PduOutletVoltage2_Object = MibTableColumn
pduOutletVoltage2 = _PduOutletVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 5),
    _PduOutletVoltage2_Type()
)
pduOutletVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletVoltage2.setStatus("current")
_PduOutletVoltage3_Type = Unsigned32
_PduOutletVoltage3_Object = MibTableColumn
pduOutletVoltage3 = _PduOutletVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 6),
    _PduOutletVoltage3_Type()
)
pduOutletVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletVoltage3.setStatus("current")
_PduOutletCurrent_Type = Unsigned32
_PduOutletCurrent_Object = MibTableColumn
pduOutletCurrent = _PduOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 7),
    _PduOutletCurrent_Type()
)
pduOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletCurrent.setStatus("current")
_PduOutletPowerFactor_Type = Unsigned32
_PduOutletPowerFactor_Object = MibTableColumn
pduOutletPowerFactor = _PduOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 8),
    _PduOutletPowerFactor_Type()
)
pduOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletPowerFactor.setStatus("current")
_PduOutletPower_Type = Unsigned32
_PduOutletPower_Object = MibTableColumn
pduOutletPower = _PduOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 9),
    _PduOutletPower_Type()
)
pduOutletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletPower.setStatus("current")


class _PduOutletState_Type(Integer32):
    """Custom type pduOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("error", -1),
          ("off", 0),
          ("on", 1),
          ("cycling", 2),
          ("delaySwitch10", 3),
          ("delaySwitch30", 4),
          ("delaySwitch60", 5))
    )


_PduOutletState_Type.__name__ = "Integer32"
_PduOutletState_Object = MibTableColumn
pduOutletState = _PduOutletState_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 12),
    _PduOutletState_Type()
)
pduOutletState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletState.setStatus("current")
_PduOutletIndividualDelayTimer_Type = Unsigned32
_PduOutletIndividualDelayTimer_Object = MibTableColumn
pduOutletIndividualDelayTimer = _PduOutletIndividualDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 13),
    _PduOutletIndividualDelayTimer_Type()
)
pduOutletIndividualDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletIndividualDelayTimer.setStatus("current")
_PduOutletEnergy_Type = Unsigned32
_PduOutletEnergy_Object = MibTableColumn
pduOutletEnergy = _PduOutletEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 14),
    _PduOutletEnergy_Type()
)
pduOutletEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletEnergy.setStatus("current")
_PduOutletReactivePower_Type = Unsigned32
_PduOutletReactivePower_Object = MibTableColumn
pduOutletReactivePower = _PduOutletReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 15),
    _PduOutletReactivePower_Type()
)
pduOutletReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletReactivePower.setStatus("current")
_PduOutletApparentPower_Type = Unsigned32
_PduOutletApparentPower_Object = MibTableColumn
pduOutletApparentPower = _PduOutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 16),
    _PduOutletApparentPower_Type()
)
pduOutletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletApparentPower.setStatus("current")


class _PduOutletEnergyReset_Type(Integer32):
    """Custom type pduOutletEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_PduOutletEnergyReset_Type.__name__ = "Integer32"
_PduOutletEnergyReset_Object = MibTableColumn
pduOutletEnergyReset = _PduOutletEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 3, 3, 1, 17),
    _PduOutletEnergyReset_Type()
)
pduOutletEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletEnergyReset.setStatus("current")
_OutputData_ObjectIdentity = ObjectIdentity
outputData = _OutputData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4)
)
_PduOutputMeterCount_Type = Integer32
_PduOutputMeterCount_Object = MibScalar
pduOutputMeterCount = _PduOutputMeterCount_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 1),
    _PduOutputMeterCount_Type()
)
pduOutputMeterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterCount.setStatus("current")
_PduOutputMeterTable_Object = MibTable
pduOutputMeterTable = _PduOutputMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5)
)
if mibBuilder.loadTexts:
    pduOutputMeterTable.setStatus("current")
_PduOutputMeterEntry_Object = MibTableRow
pduOutputMeterEntry = _PduOutputMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1)
)
pduOutputMeterEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduOutputMeterNumber"),
)
if mibBuilder.loadTexts:
    pduOutputMeterEntry.setStatus("current")


class _PduOutputMeterNumber_Type(Integer32):
    """Custom type pduOutputMeterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduOutputMeterNumber_Type.__name__ = "Integer32"
_PduOutputMeterNumber_Object = MibTableColumn
pduOutputMeterNumber = _PduOutputMeterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 1),
    _PduOutputMeterNumber_Type()
)
pduOutputMeterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutputMeterNumber.setStatus("current")
_PduOutputMeterLineFrequency_Type = Unsigned32
_PduOutputMeterLineFrequency_Object = MibTableColumn
pduOutputMeterLineFrequency = _PduOutputMeterLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 2),
    _PduOutputMeterLineFrequency_Type()
)
pduOutputMeterLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterLineFrequency.setStatus("current")
_PduOutputMeterVoltage1_Type = Unsigned32
_PduOutputMeterVoltage1_Object = MibTableColumn
pduOutputMeterVoltage1 = _PduOutputMeterVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 3),
    _PduOutputMeterVoltage1_Type()
)
pduOutputMeterVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterVoltage1.setStatus("current")
_PduOutputMeterVoltage2_Type = Unsigned32
_PduOutputMeterVoltage2_Object = MibTableColumn
pduOutputMeterVoltage2 = _PduOutputMeterVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 4),
    _PduOutputMeterVoltage2_Type()
)
pduOutputMeterVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterVoltage2.setStatus("current")
_PduOutputMeterVoltage3_Type = Unsigned32
_PduOutputMeterVoltage3_Object = MibTableColumn
pduOutputMeterVoltage3 = _PduOutputMeterVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 5),
    _PduOutputMeterVoltage3_Type()
)
pduOutputMeterVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterVoltage3.setStatus("current")
_PduOutputMeterCurrent_Type = Unsigned32
_PduOutputMeterCurrent_Object = MibTableColumn
pduOutputMeterCurrent = _PduOutputMeterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 6),
    _PduOutputMeterCurrent_Type()
)
pduOutputMeterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterCurrent.setStatus("current")
_PduOutputMeterPower_Type = Unsigned32
_PduOutputMeterPower_Object = MibTableColumn
pduOutputMeterPower = _PduOutputMeterPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 7),
    _PduOutputMeterPower_Type()
)
pduOutputMeterPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterPower.setStatus("current")
_PduOutputMeterEnergy_Type = Unsigned32
_PduOutputMeterEnergy_Object = MibTableColumn
pduOutputMeterEnergy = _PduOutputMeterEnergy_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 8),
    _PduOutputMeterEnergy_Type()
)
pduOutputMeterEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterEnergy.setStatus("current")
_PduOutputMeterReactivePower_Type = Unsigned32
_PduOutputMeterReactivePower_Object = MibTableColumn
pduOutputMeterReactivePower = _PduOutputMeterReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 9),
    _PduOutputMeterReactivePower_Type()
)
pduOutputMeterReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterReactivePower.setStatus("current")
_PduOutputMeterApparentPower_Type = Unsigned32
_PduOutputMeterApparentPower_Object = MibTableColumn
pduOutputMeterApparentPower = _PduOutputMeterApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 4, 5, 1, 10),
    _PduOutputMeterApparentPower_Type()
)
pduOutputMeterApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputMeterApparentPower.setStatus("current")
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5)
)
_PduExtMonitorCount_Type = Integer32
_PduExtMonitorCount_Object = MibScalar
pduExtMonitorCount = _PduExtMonitorCount_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5, 1),
    _PduExtMonitorCount_Type()
)
pduExtMonitorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExtMonitorCount.setStatus("current")
_PduExtMonitorTable_Object = MibTable
pduExtMonitorTable = _PduExtMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5, 2)
)
if mibBuilder.loadTexts:
    pduExtMonitorTable.setStatus("current")
_PduExtMonitorEntry_Object = MibTableRow
pduExtMonitorEntry = _PduExtMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5, 2, 1)
)
pduExtMonitorEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduExtMonitorNumber"),
)
if mibBuilder.loadTexts:
    pduExtMonitorEntry.setStatus("current")


class _PduExtMonitorNumber_Type(Integer32):
    """Custom type pduExtMonitorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExtMonitorNumber_Type.__name__ = "Integer32"
_PduExtMonitorNumber_Object = MibTableColumn
pduExtMonitorNumber = _PduExtMonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5, 2, 1, 1),
    _PduExtMonitorNumber_Type()
)
pduExtMonitorNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExtMonitorNumber.setStatus("current")
_PduExtThermal_Type = Unsigned32
_PduExtThermal_Object = MibTableColumn
pduExtThermal = _PduExtThermal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5, 2, 1, 2),
    _PduExtThermal_Type()
)
pduExtThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExtThermal.setStatus("current")
_PduExtHumidity_Type = Unsigned32
_PduExtHumidity_Object = MibTableColumn
pduExtHumidity = _PduExtHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 5, 2, 1, 3),
    _PduExtHumidity_Type()
)
pduExtHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExtHumidity.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6)
)
_PduVoltageWarningTable_Object = MibTable
pduVoltageWarningTable = _PduVoltageWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pduVoltageWarningTable.setStatus("current")
_PduVoltageWarningEntry_Object = MibTableRow
pduVoltageWarningEntry = _PduVoltageWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1)
)
pduVoltageWarningEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduVoltageWarningNumber"),
)
if mibBuilder.loadTexts:
    pduVoltageWarningEntry.setStatus("current")


class _PduVoltageWarningNumber_Type(Integer32):
    """Custom type pduVoltageWarningNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduVoltageWarningNumber_Type.__name__ = "Integer32"
_PduVoltageWarningNumber_Object = MibTableColumn
pduVoltageWarningNumber = _PduVoltageWarningNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 1),
    _PduVoltageWarningNumber_Type()
)
pduVoltageWarningNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduVoltageWarningNumber.setStatus("current")


class _PduOutputHighVoltage1Warning_Type(Integer32):
    """Custom type pduOutputHighVoltage1Warning based on Integer32"""
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


_PduOutputHighVoltage1Warning_Type.__name__ = "Integer32"
_PduOutputHighVoltage1Warning_Object = MibTableColumn
pduOutputHighVoltage1Warning = _PduOutputHighVoltage1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 2),
    _PduOutputHighVoltage1Warning_Type()
)
pduOutputHighVoltage1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputHighVoltage1Warning.setStatus("current")


class _PduOutputHighVoltage2Warning_Type(Integer32):
    """Custom type pduOutputHighVoltage2Warning based on Integer32"""
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


_PduOutputHighVoltage2Warning_Type.__name__ = "Integer32"
_PduOutputHighVoltage2Warning_Object = MibTableColumn
pduOutputHighVoltage2Warning = _PduOutputHighVoltage2Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 3),
    _PduOutputHighVoltage2Warning_Type()
)
pduOutputHighVoltage2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputHighVoltage2Warning.setStatus("current")


class _PduOutputHighVoltage3Warning_Type(Integer32):
    """Custom type pduOutputHighVoltage3Warning based on Integer32"""
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


_PduOutputHighVoltage3Warning_Type.__name__ = "Integer32"
_PduOutputHighVoltage3Warning_Object = MibTableColumn
pduOutputHighVoltage3Warning = _PduOutputHighVoltage3Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 4),
    _PduOutputHighVoltage3Warning_Type()
)
pduOutputHighVoltage3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputHighVoltage3Warning.setStatus("current")


class _PduInputHighVoltage1Warning_Type(Integer32):
    """Custom type pduInputHighVoltage1Warning based on Integer32"""
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


_PduInputHighVoltage1Warning_Type.__name__ = "Integer32"
_PduInputHighVoltage1Warning_Object = MibTableColumn
pduInputHighVoltage1Warning = _PduInputHighVoltage1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 5),
    _PduInputHighVoltage1Warning_Type()
)
pduInputHighVoltage1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputHighVoltage1Warning.setStatus("current")


class _PduInputHighVoltage2Warning_Type(Integer32):
    """Custom type pduInputHighVoltage2Warning based on Integer32"""
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


_PduInputHighVoltage2Warning_Type.__name__ = "Integer32"
_PduInputHighVoltage2Warning_Object = MibTableColumn
pduInputHighVoltage2Warning = _PduInputHighVoltage2Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 6),
    _PduInputHighVoltage2Warning_Type()
)
pduInputHighVoltage2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputHighVoltage2Warning.setStatus("current")


class _PduInputHighVoltage3Warning_Type(Integer32):
    """Custom type pduInputHighVoltage3Warning based on Integer32"""
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


_PduInputHighVoltage3Warning_Type.__name__ = "Integer32"
_PduInputHighVoltage3Warning_Object = MibTableColumn
pduInputHighVoltage3Warning = _PduInputHighVoltage3Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 7),
    _PduInputHighVoltage3Warning_Type()
)
pduInputHighVoltage3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputHighVoltage3Warning.setStatus("current")


class _PduOutputLowVoltage1Warning_Type(Integer32):
    """Custom type pduOutputLowVoltage1Warning based on Integer32"""
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


_PduOutputLowVoltage1Warning_Type.__name__ = "Integer32"
_PduOutputLowVoltage1Warning_Object = MibTableColumn
pduOutputLowVoltage1Warning = _PduOutputLowVoltage1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 8),
    _PduOutputLowVoltage1Warning_Type()
)
pduOutputLowVoltage1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputLowVoltage1Warning.setStatus("current")


class _PduOutputLowVoltage2Warning_Type(Integer32):
    """Custom type pduOutputLowVoltage2Warning based on Integer32"""
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


_PduOutputLowVoltage2Warning_Type.__name__ = "Integer32"
_PduOutputLowVoltage2Warning_Object = MibTableColumn
pduOutputLowVoltage2Warning = _PduOutputLowVoltage2Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 9),
    _PduOutputLowVoltage2Warning_Type()
)
pduOutputLowVoltage2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputLowVoltage2Warning.setStatus("current")


class _PduOutputLowVoltage3Warning_Type(Integer32):
    """Custom type pduOutputLowVoltage3Warning based on Integer32"""
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


_PduOutputLowVoltage3Warning_Type.__name__ = "Integer32"
_PduOutputLowVoltage3Warning_Object = MibTableColumn
pduOutputLowVoltage3Warning = _PduOutputLowVoltage3Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 10),
    _PduOutputLowVoltage3Warning_Type()
)
pduOutputLowVoltage3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputLowVoltage3Warning.setStatus("current")


class _PduInputLowVoltage1Warning_Type(Integer32):
    """Custom type pduInputLowVoltage1Warning based on Integer32"""
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


_PduInputLowVoltage1Warning_Type.__name__ = "Integer32"
_PduInputLowVoltage1Warning_Object = MibTableColumn
pduInputLowVoltage1Warning = _PduInputLowVoltage1Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 11),
    _PduInputLowVoltage1Warning_Type()
)
pduInputLowVoltage1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputLowVoltage1Warning.setStatus("current")


class _PduInputLowVoltage2Warning_Type(Integer32):
    """Custom type pduInputLowVoltage2Warning based on Integer32"""
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


_PduInputLowVoltage2Warning_Type.__name__ = "Integer32"
_PduInputLowVoltage2Warning_Object = MibTableColumn
pduInputLowVoltage2Warning = _PduInputLowVoltage2Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 12),
    _PduInputLowVoltage2Warning_Type()
)
pduInputLowVoltage2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputLowVoltage2Warning.setStatus("current")


class _PduInputLowVoltage3Warning_Type(Integer32):
    """Custom type pduInputLowVoltage3Warning based on Integer32"""
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


_PduInputLowVoltage3Warning_Type.__name__ = "Integer32"
_PduInputLowVoltage3Warning_Object = MibTableColumn
pduInputLowVoltage3Warning = _PduInputLowVoltage3Warning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 13),
    _PduInputLowVoltage3Warning_Type()
)
pduInputLowVoltage3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputLowVoltage3Warning.setStatus("current")
_PduOutputHighVoltageWarningThreshold_Type = Unsigned32
_PduOutputHighVoltageWarningThreshold_Object = MibTableColumn
pduOutputHighVoltageWarningThreshold = _PduOutputHighVoltageWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 14),
    _PduOutputHighVoltageWarningThreshold_Type()
)
pduOutputHighVoltageWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutputHighVoltageWarningThreshold.setStatus("current")
_PduInputHighVoltageWarningThreshold_Type = Unsigned32
_PduInputHighVoltageWarningThreshold_Object = MibTableColumn
pduInputHighVoltageWarningThreshold = _PduInputHighVoltageWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 15),
    _PduInputHighVoltageWarningThreshold_Type()
)
pduInputHighVoltageWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputHighVoltageWarningThreshold.setStatus("current")
_PduOutputlowVoltageWarningThreshold_Type = Unsigned32
_PduOutputlowVoltageWarningThreshold_Object = MibScalar
pduOutputlowVoltageWarningThreshold = _PduOutputlowVoltageWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 16),
    _PduOutputlowVoltageWarningThreshold_Type()
)
pduOutputlowVoltageWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutputlowVoltageWarningThreshold.setStatus("current")
_PduInputlowVoltageWarningThreshold_Type = Unsigned32
_PduInputlowVoltageWarningThreshold_Object = MibScalar
pduInputlowVoltageWarningThreshold = _PduInputlowVoltageWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 1, 1, 17),
    _PduInputlowVoltageWarningThreshold_Type()
)
pduInputlowVoltageWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputlowVoltageWarningThreshold.setStatus("current")
_PduOutputCurrentWarningTable_Object = MibTable
pduOutputCurrentWarningTable = _PduOutputCurrentWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 2)
)
if mibBuilder.loadTexts:
    pduOutputCurrentWarningTable.setStatus("current")
_PduOutputCurrentWarningEntry_Object = MibTableRow
pduOutputCurrentWarningEntry = _PduOutputCurrentWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 2, 1)
)
pduOutputCurrentWarningEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduOutputCurrentWarningNumber"),
)
if mibBuilder.loadTexts:
    pduOutputCurrentWarningEntry.setStatus("current")


class _PduOutputCurrentWarningNumber_Type(Integer32):
    """Custom type pduOutputCurrentWarningNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduOutputCurrentWarningNumber_Type.__name__ = "Integer32"
_PduOutputCurrentWarningNumber_Object = MibTableColumn
pduOutputCurrentWarningNumber = _PduOutputCurrentWarningNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 2, 1, 1),
    _PduOutputCurrentWarningNumber_Type()
)
pduOutputCurrentWarningNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutputCurrentWarningNumber.setStatus("current")


class _PduOutputCurrentWarning_Type(Integer32):
    """Custom type pduOutputCurrentWarning based on Integer32"""
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


_PduOutputCurrentWarning_Type.__name__ = "Integer32"
_PduOutputCurrentWarning_Object = MibTableColumn
pduOutputCurrentWarning = _PduOutputCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 2, 1, 2),
    _PduOutputCurrentWarning_Type()
)
pduOutputCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputCurrentWarning.setStatus("current")
_PduOutputCurrentWarningThreshold_Type = Unsigned32
_PduOutputCurrentWarningThreshold_Object = MibTableColumn
pduOutputCurrentWarningThreshold = _PduOutputCurrentWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 2, 1, 3),
    _PduOutputCurrentWarningThreshold_Type()
)
pduOutputCurrentWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutputCurrentWarningThreshold.setStatus("current")
_PduInputCurrentWarningTable_Object = MibTable
pduInputCurrentWarningTable = _PduInputCurrentWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 3)
)
if mibBuilder.loadTexts:
    pduInputCurrentWarningTable.setStatus("current")
_PduInputCurrentWarningEntry_Object = MibTableRow
pduInputCurrentWarningEntry = _PduInputCurrentWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 3, 1)
)
pduInputCurrentWarningEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduInputCurrentWarningNumber"),
)
if mibBuilder.loadTexts:
    pduInputCurrentWarningEntry.setStatus("current")


class _PduInputCurrentWarningNumber_Type(Integer32):
    """Custom type pduInputCurrentWarningNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduInputCurrentWarningNumber_Type.__name__ = "Integer32"
_PduInputCurrentWarningNumber_Object = MibTableColumn
pduInputCurrentWarningNumber = _PduInputCurrentWarningNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 3, 1, 1),
    _PduInputCurrentWarningNumber_Type()
)
pduInputCurrentWarningNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputCurrentWarningNumber.setStatus("current")


class _PduInputCurrentWarning_Type(Integer32):
    """Custom type pduInputCurrentWarning based on Integer32"""
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


_PduInputCurrentWarning_Type.__name__ = "Integer32"
_PduInputCurrentWarning_Object = MibTableColumn
pduInputCurrentWarning = _PduInputCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 3, 1, 2),
    _PduInputCurrentWarning_Type()
)
pduInputCurrentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputCurrentWarning.setStatus("current")
_PduInputCurrentWarningThreshold_Type = Unsigned32
_PduInputCurrentWarningThreshold_Object = MibTableColumn
pduInputCurrentWarningThreshold = _PduInputCurrentWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 3, 1, 3),
    _PduInputCurrentWarningThreshold_Type()
)
pduInputCurrentWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputCurrentWarningThreshold.setStatus("current")
_PduExtMonitorWarningTable_Object = MibTable
pduExtMonitorWarningTable = _PduExtMonitorWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4)
)
if mibBuilder.loadTexts:
    pduExtMonitorWarningTable.setStatus("current")
_PduExtMonitorWarningEntry_Object = MibTableRow
pduExtMonitorWarningEntry = _PduExtMonitorWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4, 1)
)
pduExtMonitorWarningEntry.setIndexNames(
    (0, "DeltaIDC-MIB", "pduExtMonitorWarningNumber"),
)
if mibBuilder.loadTexts:
    pduExtMonitorWarningEntry.setStatus("current")


class _PduExtMonitorWarningNumber_Type(Integer32):
    """Custom type pduExtMonitorWarningNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExtMonitorWarningNumber_Type.__name__ = "Integer32"
_PduExtMonitorWarningNumber_Object = MibTableColumn
pduExtMonitorWarningNumber = _PduExtMonitorWarningNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4, 1, 1),
    _PduExtMonitorWarningNumber_Type()
)
pduExtMonitorWarningNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExtMonitorWarningNumber.setStatus("current")


class _PduExtThermalWarning_Type(Integer32):
    """Custom type pduExtThermalWarning based on Integer32"""
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


_PduExtThermalWarning_Type.__name__ = "Integer32"
_PduExtThermalWarning_Object = MibTableColumn
pduExtThermalWarning = _PduExtThermalWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4, 1, 2),
    _PduExtThermalWarning_Type()
)
pduExtThermalWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExtThermalWarning.setStatus("current")


class _PduExtHumidityWarning_Type(Integer32):
    """Custom type pduExtHumidityWarning based on Integer32"""
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


_PduExtHumidityWarning_Type.__name__ = "Integer32"
_PduExtHumidityWarning_Object = MibTableColumn
pduExtHumidityWarning = _PduExtHumidityWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4, 1, 3),
    _PduExtHumidityWarning_Type()
)
pduExtHumidityWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExtHumidityWarning.setStatus("current")
_PduExtThermalWarningThreshold_Type = Unsigned32
_PduExtThermalWarningThreshold_Object = MibTableColumn
pduExtThermalWarningThreshold = _PduExtThermalWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4, 1, 4),
    _PduExtThermalWarningThreshold_Type()
)
pduExtThermalWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExtThermalWarningThreshold.setStatus("current")


class _PduExtHumidityWarningThreshold_Type(Unsigned32):
    """Custom type pduExtHumidityWarningThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduExtHumidityWarningThreshold_Type.__name__ = "Unsigned32"
_PduExtHumidityWarningThreshold_Object = MibTableColumn
pduExtHumidityWarningThreshold = _PduExtHumidityWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 6, 4, 1, 5),
    _PduExtHumidityWarningThreshold_Type()
)
pduExtHumidityWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExtHumidityWarningThreshold.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7)
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
        *(("StaticIP", 0),
          ("DHCP", 1))
    )


_IpMode_Type.__name__ = "Integer32"
_IpMode_Object = MibScalar
ipMode = _IpMode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7, 1),
    _IpMode_Type()
)
ipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMode.setStatus("mandatory")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7, 2),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("mandatory")
_NetMaskAddress_Type = IpAddress
_NetMaskAddress_Object = MibScalar
netMaskAddress = _NetMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7, 3),
    _NetMaskAddress_Type()
)
netMaskAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMaskAddress.setStatus("mandatory")
_GatewayAddress_Type = IpAddress
_GatewayAddress_Object = MibScalar
gatewayAddress = _GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7, 4),
    _GatewayAddress_Type()
)
gatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayAddress.setStatus("mandatory")
_SnmpTrapAddress1_Type = IpAddress
_SnmpTrapAddress1_Object = MibScalar
snmpTrapAddress1 = _SnmpTrapAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7, 5),
    _SnmpTrapAddress1_Type()
)
snmpTrapAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapAddress1.setStatus("mandatory")
_SnmpTrapAddress2_Type = IpAddress
_SnmpTrapAddress2_Object = MibScalar
snmpTrapAddress2 = _SnmpTrapAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 7, 6),
    _SnmpTrapAddress2_Type()
)
snmpTrapAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapAddress2.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100)
)
_TrapData_ObjectIdentity = ObjectIdentity
trapData = _TrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1)
)
_PduTrapDataObjects_ObjectIdentity = ObjectIdentity
pduTrapDataObjects = _PduTrapDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1)
)


class _PduObjectIndex_Type(Unsigned32):
    """Custom type pduObjectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduObjectIndex_Type.__name__ = "Unsigned32"
_PduObjectIndex_Object = MibScalar
pduObjectIndex = _PduObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 1),
    _PduObjectIndex_Type()
)
pduObjectIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduObjectIndex.setStatus("current")


class _PduObjectType_Type(Integer32):
    """Custom type pduObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pdu", 0),
          ("outlet", 1),
          ("meter", 2))
    )


_PduObjectType_Type.__name__ = "Integer32"
_PduObjectType_Object = MibScalar
pduObjectType = _PduObjectType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 2),
    _PduObjectType_Type()
)
pduObjectType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduObjectType.setStatus("current")
_PduObjectID_Type = DisplayString
_PduObjectID_Object = MibScalar
pduObjectID = _PduObjectID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 3),
    _PduObjectID_Type()
)
pduObjectID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduObjectID.setStatus("current")


class _PduSeverity_Type(Integer32):
    """Custom type pduSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("informational", 0),
          ("warning", 1))
    )


_PduSeverity_Type.__name__ = "Integer32"
_PduSeverity_Object = MibScalar
pduSeverity = _PduSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 4),
    _PduSeverity_Type()
)
pduSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduSeverity.setStatus("current")
_PduTrapDescription_Type = DisplayString
_PduTrapDescription_Object = MibScalar
pduTrapDescription = _PduTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 5),
    _PduTrapDescription_Type()
)
pduTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduTrapDescription.setStatus("current")


class _PduState_Type(Integer32):
    """Custom type pduState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 0),
          ("powerOn", 1),
          ("reboot", 2),
          ("delayedOn", 3),
          ("delayedOff", 4))
    )


_PduState_Type.__name__ = "Integer32"
_PduState_Object = MibScalar
pduState = _PduState_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 6),
    _PduState_Type()
)
pduState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduState.setStatus("current")


class _PduWarning_Type(Integer32):
    """Custom type pduWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_PduWarning_Type.__name__ = "Integer32"
_PduWarning_Object = MibScalar
pduWarning = _PduWarning_Object(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1, 1, 7),
    _PduWarning_Type()
)
pduWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduWarning.setStatus("current")

# Managed Objects groups


# Notification objects

pduVoltageWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 1)
)
pduVoltageWarningTrap.setObjects(
      *(("DeltaIDC-MIB", "pduObjectIndex"),
        ("DeltaIDC-MIB", "pduObjectType"),
        ("DeltaIDC-MIB", "pduObjectID"),
        ("DeltaIDC-MIB", "pduSeverity"),
        ("DeltaIDC-MIB", "pduWarning"),
        ("DeltaIDC-MIB", "pduTrapDescription"))
)
if mibBuilder.loadTexts:
    pduVoltageWarningTrap.setStatus(
        "current"
    )

pduCurrentWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 2)
)
pduCurrentWarningTrap.setObjects(
      *(("DeltaIDC-MIB", "pduObjectIndex"),
        ("DeltaIDC-MIB", "pduObjectType"),
        ("DeltaIDC-MIB", "pduObjectID"),
        ("DeltaIDC-MIB", "pduSeverity"),
        ("DeltaIDC-MIB", "pduWarning"),
        ("DeltaIDC-MIB", "pduTrapDescription"))
)
if mibBuilder.loadTexts:
    pduCurrentWarningTrap.setStatus(
        "current"
    )

pduExtThermalWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 3)
)
pduExtThermalWarningTrap.setObjects(
      *(("DeltaIDC-MIB", "pduObjectIndex"),
        ("DeltaIDC-MIB", "pduObjectType"),
        ("DeltaIDC-MIB", "pduObjectID"),
        ("DeltaIDC-MIB", "pduSeverity"),
        ("DeltaIDC-MIB", "pduWarning"),
        ("DeltaIDC-MIB", "pduTrapDescription"))
)
if mibBuilder.loadTexts:
    pduExtThermalWarningTrap.setStatus(
        "current"
    )

pduExtHumidityWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 4)
)
pduExtHumidityWarningTrap.setObjects(
      *(("DeltaIDC-MIB", "pduObjectIndex"),
        ("DeltaIDC-MIB", "pduObjectType"),
        ("DeltaIDC-MIB", "pduObjectID"),
        ("DeltaIDC-MIB", "pduSeverity"),
        ("DeltaIDC-MIB", "pduWarning"),
        ("DeltaIDC-MIB", "pduTrapDescription"))
)
if mibBuilder.loadTexts:
    pduExtHumidityWarningTrap.setStatus(
        "current"
    )

pduOutletStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 169, 2, 100, 7)
)
pduOutletStateChangeTrap.setObjects(
      *(("DeltaIDC-MIB", "pduObjectIndex"),
        ("DeltaIDC-MIB", "pduObjectID"),
        ("DeltaIDC-MIB", "pduState"),
        ("DeltaIDC-MIB", "pduTrapDescription"))
)
if mibBuilder.loadTexts:
    pduOutletStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaIDC-MIB",
    **{"delta": delta,
       "idc": idc,
       "pdu": pdu,
       "sysInfo": sysInfo,
       "pduName": pduName,
       "pduDescription": pduDescription,
       "pduModelName": pduModelName,
       "pduSerialNumber": pduSerialNumber,
       "pduPartNumber": pduPartNumber,
       "pduFWVersion": pduFWVersion,
       "pduMeterTable": pduMeterTable,
       "pduMeterEntry": pduMeterEntry,
       "pduMeterNumber": pduMeterNumber,
       "pduMeterVersion": pduMeterVersion,
       "pduMeterSerial": pduMeterSerial,
       "pduMeterDate": pduMeterDate,
       "inputData": inputData,
       "inputPhaseCount": inputPhaseCount,
       "inputFrequency": inputFrequency,
       "inputTotalCurrent": inputTotalCurrent,
       "inputTotalPower": inputTotalPower,
       "inputTotalEnergy": inputTotalEnergy,
       "inputTotalReactivePower": inputTotalReactivePower,
       "inputTotalApparentPower": inputTotalApparentPower,
       "inputClearTotalEnergy": inputClearTotalEnergy,
       "inputDataTable": inputDataTable,
       "inputDataEntry": inputDataEntry,
       "inputPhaseNumber": inputPhaseNumber,
       "inputVoltage": inputVoltage,
       "inputCurrent": inputCurrent,
       "inputPower": inputPower,
       "inputEnergy": inputEnergy,
       "inputReactivePower": inputReactivePower,
       "inputApparentPower": inputApparentPower,
       "inputPowerFactor": inputPowerFactor,
       "inputThdVoltage": inputThdVoltage,
       "inputThdCurrent": inputThdCurrent,
       "inputLineVoltage": inputLineVoltage,
       "inputLineCurrent": inputLineCurrent,
       "outputOutlet": outputOutlet,
       "pduPhaseCount": pduPhaseCount,
       "pduOutletCount": pduOutletCount,
       "pduOutletTable": pduOutletTable,
       "pduOutletEntry": pduOutletEntry,
       "pduOutletNumber": pduOutletNumber,
       "pduOutletName": pduOutletName,
       "pduOutletDescription": pduOutletDescription,
       "pduOutletVoltage1": pduOutletVoltage1,
       "pduOutletVoltage2": pduOutletVoltage2,
       "pduOutletVoltage3": pduOutletVoltage3,
       "pduOutletCurrent": pduOutletCurrent,
       "pduOutletPowerFactor": pduOutletPowerFactor,
       "pduOutletPower": pduOutletPower,
       "pduOutletState": pduOutletState,
       "pduOutletIndividualDelayTimer": pduOutletIndividualDelayTimer,
       "pduOutletEnergy": pduOutletEnergy,
       "pduOutletReactivePower": pduOutletReactivePower,
       "pduOutletApparentPower": pduOutletApparentPower,
       "pduOutletEnergyReset": pduOutletEnergyReset,
       "outputData": outputData,
       "pduOutputMeterCount": pduOutputMeterCount,
       "pduOutputMeterTable": pduOutputMeterTable,
       "pduOutputMeterEntry": pduOutputMeterEntry,
       "pduOutputMeterNumber": pduOutputMeterNumber,
       "pduOutputMeterLineFrequency": pduOutputMeterLineFrequency,
       "pduOutputMeterVoltage1": pduOutputMeterVoltage1,
       "pduOutputMeterVoltage2": pduOutputMeterVoltage2,
       "pduOutputMeterVoltage3": pduOutputMeterVoltage3,
       "pduOutputMeterCurrent": pduOutputMeterCurrent,
       "pduOutputMeterPower": pduOutputMeterPower,
       "pduOutputMeterEnergy": pduOutputMeterEnergy,
       "pduOutputMeterReactivePower": pduOutputMeterReactivePower,
       "pduOutputMeterApparentPower": pduOutputMeterApparentPower,
       "environment": environment,
       "pduExtMonitorCount": pduExtMonitorCount,
       "pduExtMonitorTable": pduExtMonitorTable,
       "pduExtMonitorEntry": pduExtMonitorEntry,
       "pduExtMonitorNumber": pduExtMonitorNumber,
       "pduExtThermal": pduExtThermal,
       "pduExtHumidity": pduExtHumidity,
       "alarm": alarm,
       "pduVoltageWarningTable": pduVoltageWarningTable,
       "pduVoltageWarningEntry": pduVoltageWarningEntry,
       "pduVoltageWarningNumber": pduVoltageWarningNumber,
       "pduOutputHighVoltage1Warning": pduOutputHighVoltage1Warning,
       "pduOutputHighVoltage2Warning": pduOutputHighVoltage2Warning,
       "pduOutputHighVoltage3Warning": pduOutputHighVoltage3Warning,
       "pduInputHighVoltage1Warning": pduInputHighVoltage1Warning,
       "pduInputHighVoltage2Warning": pduInputHighVoltage2Warning,
       "pduInputHighVoltage3Warning": pduInputHighVoltage3Warning,
       "pduOutputLowVoltage1Warning": pduOutputLowVoltage1Warning,
       "pduOutputLowVoltage2Warning": pduOutputLowVoltage2Warning,
       "pduOutputLowVoltage3Warning": pduOutputLowVoltage3Warning,
       "pduInputLowVoltage1Warning": pduInputLowVoltage1Warning,
       "pduInputLowVoltage2Warning": pduInputLowVoltage2Warning,
       "pduInputLowVoltage3Warning": pduInputLowVoltage3Warning,
       "pduOutputHighVoltageWarningThreshold": pduOutputHighVoltageWarningThreshold,
       "pduInputHighVoltageWarningThreshold": pduInputHighVoltageWarningThreshold,
       "pduOutputlowVoltageWarningThreshold": pduOutputlowVoltageWarningThreshold,
       "pduInputlowVoltageWarningThreshold": pduInputlowVoltageWarningThreshold,
       "pduOutputCurrentWarningTable": pduOutputCurrentWarningTable,
       "pduOutputCurrentWarningEntry": pduOutputCurrentWarningEntry,
       "pduOutputCurrentWarningNumber": pduOutputCurrentWarningNumber,
       "pduOutputCurrentWarning": pduOutputCurrentWarning,
       "pduOutputCurrentWarningThreshold": pduOutputCurrentWarningThreshold,
       "pduInputCurrentWarningTable": pduInputCurrentWarningTable,
       "pduInputCurrentWarningEntry": pduInputCurrentWarningEntry,
       "pduInputCurrentWarningNumber": pduInputCurrentWarningNumber,
       "pduInputCurrentWarning": pduInputCurrentWarning,
       "pduInputCurrentWarningThreshold": pduInputCurrentWarningThreshold,
       "pduExtMonitorWarningTable": pduExtMonitorWarningTable,
       "pduExtMonitorWarningEntry": pduExtMonitorWarningEntry,
       "pduExtMonitorWarningNumber": pduExtMonitorWarningNumber,
       "pduExtThermalWarning": pduExtThermalWarning,
       "pduExtHumidityWarning": pduExtHumidityWarning,
       "pduExtThermalWarningThreshold": pduExtThermalWarningThreshold,
       "pduExtHumidityWarningThreshold": pduExtHumidityWarningThreshold,
       "networkSetting": networkSetting,
       "ipMode": ipMode,
       "ipAddress": ipAddress,
       "netMaskAddress": netMaskAddress,
       "gatewayAddress": gatewayAddress,
       "snmpTrapAddress1": snmpTrapAddress1,
       "snmpTrapAddress2": snmpTrapAddress2,
       "traps": traps,
       "trapData": trapData,
       "pduVoltageWarningTrap": pduVoltageWarningTrap,
       "pduTrapDataObjects": pduTrapDataObjects,
       "pduObjectIndex": pduObjectIndex,
       "pduObjectType": pduObjectType,
       "pduObjectID": pduObjectID,
       "pduSeverity": pduSeverity,
       "pduTrapDescription": pduTrapDescription,
       "pduState": pduState,
       "pduWarning": pduWarning,
       "pduCurrentWarningTrap": pduCurrentWarningTrap,
       "pduExtThermalWarningTrap": pduExtThermalWarningTrap,
       "pduExtHumidityWarningTrap": pduExtHumidityWarningTrap,
       "pduOutletStateChangeTrap": pduOutletStateChangeTrap}
)
