# SNMP MIB module (DeltaPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_2254/DeltaPDU-MIB.mib
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
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2)
)
_Pduv3_ObjectIdentity = ObjectIdentity
pduv3 = _Pduv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32)
)
_DpduIdent_ObjectIdentity = ObjectIdentity
dpduIdent = _DpduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1)
)


class _DpduIdentManufacturer_Type(DisplayString):
    """Custom type dpduIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpduIdentManufacturer_Type.__name__ = "DisplayString"
_DpduIdentManufacturer_Object = MibScalar
dpduIdentManufacturer = _DpduIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 1),
    _DpduIdentManufacturer_Type()
)
dpduIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduIdentManufacturer.setStatus("mandatory")


class _DpduIdentName_Type(DisplayString):
    """Custom type dpduIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DpduIdentName_Type.__name__ = "DisplayString"
_DpduIdentName_Object = MibScalar
dpduIdentName = _DpduIdentName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 2),
    _DpduIdentName_Type()
)
dpduIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpduIdentName.setStatus("mandatory")


class _DpduIdentAttachedDevices_Type(DisplayString):
    """Custom type dpduIdentAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DpduIdentAttachedDevices_Type.__name__ = "DisplayString"
_DpduIdentAttachedDevices_Object = MibScalar
dpduIdentAttachedDevices = _DpduIdentAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 3),
    _DpduIdentAttachedDevices_Type()
)
dpduIdentAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpduIdentAttachedDevices.setStatus("mandatory")


class _DpduIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type dpduIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DpduIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_DpduIdentAgentSoftwareVersion_Object = MibScalar
dpduIdentAgentSoftwareVersion = _DpduIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 4),
    _DpduIdentAgentSoftwareVersion_Type()
)
dpduIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduIdentAgentSoftwareVersion.setStatus("mandatory")
_DpduPDUNum_Type = Integer32
_DpduPDUNum_Object = MibScalar
dpduPDUNum = _DpduPDUNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 5),
    _DpduPDUNum_Type()
)
dpduPDUNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduPDUNum.setStatus("mandatory")
_DpduIdentTable_Object = MibTable
dpduIdentTable = _DpduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6)
)
if mibBuilder.loadTexts:
    dpduIdentTable.setStatus("mandatory")
_DpduIdentEntry_Object = MibTableRow
dpduIdentEntry = _DpduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1)
)
dpduIdentEntry.setIndexNames(
    (0, "DeltaPDU-MIB", "dpduIdentPDUID"),
)
if mibBuilder.loadTexts:
    dpduIdentEntry.setStatus("mandatory")


class _DpduIdentPDUID_Type(Integer32):
    """Custom type dpduIdentPDUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DpduIdentPDUID_Type.__name__ = "Integer32"
_DpduIdentPDUID_Object = MibTableColumn
dpduIdentPDUID = _DpduIdentPDUID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 1),
    _DpduIdentPDUID_Type()
)
dpduIdentPDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduIdentPDUID.setStatus("mandatory")


class _DpduIdentEnabled_Type(Integer32):
    """Custom type dpduIdentEnabled based on Integer32"""
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


_DpduIdentEnabled_Type.__name__ = "Integer32"
_DpduIdentEnabled_Object = MibTableColumn
dpduIdentEnabled = _DpduIdentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 2),
    _DpduIdentEnabled_Type()
)
dpduIdentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpduIdentEnabled.setStatus("mandatory")


class _DpduIdentModel_Type(DisplayString):
    """Custom type dpduIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpduIdentModel_Type.__name__ = "DisplayString"
_DpduIdentModel_Object = MibTableColumn
dpduIdentModel = _DpduIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 3),
    _DpduIdentModel_Type()
)
dpduIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduIdentModel.setStatus("mandatory")


class _DpduIdentSerialNumber_Type(DisplayString):
    """Custom type dpduIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DpduIdentSerialNumber_Type.__name__ = "DisplayString"
_DpduIdentSerialNumber_Object = MibTableColumn
dpduIdentSerialNumber = _DpduIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 4),
    _DpduIdentSerialNumber_Type()
)
dpduIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduIdentSerialNumber.setStatus("mandatory")


class _DpduIdentPDUFirmwareVersion_Type(DisplayString):
    """Custom type dpduIdentPDUFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DpduIdentPDUFirmwareVersion_Type.__name__ = "DisplayString"
_DpduIdentPDUFirmwareVersion_Object = MibTableColumn
dpduIdentPDUFirmwareVersion = _DpduIdentPDUFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 5),
    _DpduIdentPDUFirmwareVersion_Type()
)
dpduIdentPDUFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduIdentPDUFirmwareVersion.setStatus("mandatory")


class _DpduIdentPDUName_Type(DisplayString):
    """Custom type dpduIdentPDUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DpduIdentPDUName_Type.__name__ = "DisplayString"
_DpduIdentPDUName_Object = MibTableColumn
dpduIdentPDUName = _DpduIdentPDUName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 6),
    _DpduIdentPDUName_Type()
)
dpduIdentPDUName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpduIdentPDUName.setStatus("mandatory")


class _DpduIdentPDUAttachedDevices_Type(DisplayString):
    """Custom type dpduIdentPDUAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DpduIdentPDUAttachedDevices_Type.__name__ = "DisplayString"
_DpduIdentPDUAttachedDevices_Object = MibTableColumn
dpduIdentPDUAttachedDevices = _DpduIdentPDUAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 1, 6, 1, 7),
    _DpduIdentPDUAttachedDevices_Type()
)
dpduIdentPDUAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpduIdentPDUAttachedDevices.setStatus("mandatory")
_DpduOutput_ObjectIdentity = ObjectIdentity
dpduOutput = _DpduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2)
)
_DpduOutputTable_Object = MibTable
dpduOutputTable = _DpduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1)
)
if mibBuilder.loadTexts:
    dpduOutputTable.setStatus("mandatory")
_DpduOutputEntry_Object = MibTableRow
dpduOutputEntry = _DpduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1)
)
dpduOutputEntry.setIndexNames(
    (0, "DeltaPDU-MIB", "dpduOutputPDUID"),
)
if mibBuilder.loadTexts:
    dpduOutputEntry.setStatus("mandatory")


class _DpduOutputPDUID_Type(Integer32):
    """Custom type dpduOutputPDUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DpduOutputPDUID_Type.__name__ = "Integer32"
_DpduOutputPDUID_Object = MibTableColumn
dpduOutputPDUID = _DpduOutputPDUID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 1),
    _DpduOutputPDUID_Type()
)
dpduOutputPDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputPDUID.setStatus("mandatory")
_DpduOutputFrequency_Type = Integer32
_DpduOutputFrequency_Object = MibTableColumn
dpduOutputFrequency = _DpduOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 2),
    _DpduOutputFrequency_Type()
)
dpduOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputFrequency.setUnits("0.1 Hertz")
_DpduOutputVoltage1_Type = Integer32
_DpduOutputVoltage1_Object = MibTableColumn
dpduOutputVoltage1 = _DpduOutputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 3),
    _DpduOutputVoltage1_Type()
)
dpduOutputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputVoltage1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputVoltage1.setUnits("0.1 V")
_DpduOutputCurrent1_Type = Integer32
_DpduOutputCurrent1_Object = MibTableColumn
dpduOutputCurrent1 = _DpduOutputCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 4),
    _DpduOutputCurrent1_Type()
)
dpduOutputCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrent1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrent1.setUnits("0.1 A")
_DpduOutputVoltage2_Type = Integer32
_DpduOutputVoltage2_Object = MibTableColumn
dpduOutputVoltage2 = _DpduOutputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 5),
    _DpduOutputVoltage2_Type()
)
dpduOutputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputVoltage2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputVoltage2.setUnits("0.1 V")
_DpduOutputCurrent2_Type = Integer32
_DpduOutputCurrent2_Object = MibTableColumn
dpduOutputCurrent2 = _DpduOutputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 6),
    _DpduOutputCurrent2_Type()
)
dpduOutputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrent2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrent2.setUnits("0.1 A")
_DpduOutputVoltage3_Type = Integer32
_DpduOutputVoltage3_Object = MibTableColumn
dpduOutputVoltage3 = _DpduOutputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 7),
    _DpduOutputVoltage3_Type()
)
dpduOutputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputVoltage3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputVoltage3.setUnits("0.1 V")
_DpduOutputCurrent3_Type = Integer32
_DpduOutputCurrent3_Object = MibTableColumn
dpduOutputCurrent3 = _DpduOutputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 8),
    _DpduOutputCurrent3_Type()
)
dpduOutputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrent3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrent3.setUnits("0.1 A")
_DpduOutputWattage1_Type = Integer32
_DpduOutputWattage1_Object = MibTableColumn
dpduOutputWattage1 = _DpduOutputWattage1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 9),
    _DpduOutputWattage1_Type()
)
dpduOutputWattage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattage1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattage1.setUnits("1 Watt")
_DpduOutputEnergy1_Type = Integer32
_DpduOutputEnergy1_Object = MibTableColumn
dpduOutputEnergy1 = _DpduOutputEnergy1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 10),
    _DpduOutputEnergy1_Type()
)
dpduOutputEnergy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergy1.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergy1.setUnits("0.1 kWh")
_DpduOutputWattage2_Type = Integer32
_DpduOutputWattage2_Object = MibTableColumn
dpduOutputWattage2 = _DpduOutputWattage2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 11),
    _DpduOutputWattage2_Type()
)
dpduOutputWattage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattage2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattage2.setUnits("1 Watt")
_DpduOutputEnergy2_Type = Integer32
_DpduOutputEnergy2_Object = MibTableColumn
dpduOutputEnergy2 = _DpduOutputEnergy2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 12),
    _DpduOutputEnergy2_Type()
)
dpduOutputEnergy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergy2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergy2.setUnits("0.1 kWh")
_DpduOutputWattage3_Type = Integer32
_DpduOutputWattage3_Object = MibTableColumn
dpduOutputWattage3 = _DpduOutputWattage3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 13),
    _DpduOutputWattage3_Type()
)
dpduOutputWattage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattage3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattage3.setUnits("1 Watt")
_DpduOutputEnergy3_Type = Integer32
_DpduOutputEnergy3_Object = MibTableColumn
dpduOutputEnergy3 = _DpduOutputEnergy3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 14),
    _DpduOutputEnergy3_Type()
)
dpduOutputEnergy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergy3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergy3.setUnits("0.1 kWh")
_DpduOutputWattageTotal_Type = Integer32
_DpduOutputWattageTotal_Object = MibTableColumn
dpduOutputWattageTotal = _DpduOutputWattageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 15),
    _DpduOutputWattageTotal_Type()
)
dpduOutputWattageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageTotal.setUnits("1 Watt")
_DpduOutputEnergyTotal_Type = Integer32
_DpduOutputEnergyTotal_Object = MibTableColumn
dpduOutputEnergyTotal = _DpduOutputEnergyTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 16),
    _DpduOutputEnergyTotal_Type()
)
dpduOutputEnergyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyTotal.setUnits("0.1 kWh")
_DpduOutputCurrentL1_2_Type = Integer32
_DpduOutputCurrentL1_2_Object = MibTableColumn
dpduOutputCurrentL1_2 = _DpduOutputCurrentL1_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 17),
    _DpduOutputCurrentL1_2_Type()
)
dpduOutputCurrentL1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL1_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL1_2.setUnits("0.1 A")
_DpduOutputCurrentL2_2_Type = Integer32
_DpduOutputCurrentL2_2_Object = MibTableColumn
dpduOutputCurrentL2_2 = _DpduOutputCurrentL2_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 18),
    _DpduOutputCurrentL2_2_Type()
)
dpduOutputCurrentL2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL2_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL2_2.setUnits("0.1 A")
_DpduOutputCurrentL3_2_Type = Integer32
_DpduOutputCurrentL3_2_Object = MibTableColumn
dpduOutputCurrentL3_2 = _DpduOutputCurrentL3_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 19),
    _DpduOutputCurrentL3_2_Type()
)
dpduOutputCurrentL3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL3_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL3_2.setUnits("0.1 A")
_DpduOutputWattageL1_2_Type = Integer32
_DpduOutputWattageL1_2_Object = MibTableColumn
dpduOutputWattageL1_2 = _DpduOutputWattageL1_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 20),
    _DpduOutputWattageL1_2_Type()
)
dpduOutputWattageL1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL1_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL1_2.setUnits("1 Watt")
_DpduOutputWattageL2_2_Type = Integer32
_DpduOutputWattageL2_2_Object = MibTableColumn
dpduOutputWattageL2_2 = _DpduOutputWattageL2_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 21),
    _DpduOutputWattageL2_2_Type()
)
dpduOutputWattageL2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL2_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL2_2.setUnits("1 Watt")
_DpduOutputWattageL3_2_Type = Integer32
_DpduOutputWattageL3_2_Object = MibTableColumn
dpduOutputWattageL3_2 = _DpduOutputWattageL3_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 22),
    _DpduOutputWattageL3_2_Type()
)
dpduOutputWattageL3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL3_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL3_2.setUnits("1 Watt")
_DpduOutputEnergyL1_2_Type = Integer32
_DpduOutputEnergyL1_2_Object = MibTableColumn
dpduOutputEnergyL1_2 = _DpduOutputEnergyL1_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 23),
    _DpduOutputEnergyL1_2_Type()
)
dpduOutputEnergyL1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyL1_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyL1_2.setUnits("0.1 kWh")
_DpduOutputEnergyL2_2_Type = Integer32
_DpduOutputEnergyL2_2_Object = MibTableColumn
dpduOutputEnergyL2_2 = _DpduOutputEnergyL2_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 24),
    _DpduOutputEnergyL2_2_Type()
)
dpduOutputEnergyL2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyL2_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyL2_2.setUnits("0.1 kWh")
_DpduOutputEnergyL3_2_Type = Integer32
_DpduOutputEnergyL3_2_Object = MibTableColumn
dpduOutputEnergyL3_2 = _DpduOutputEnergyL3_2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 25),
    _DpduOutputEnergyL3_2_Type()
)
dpduOutputEnergyL3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyL3_2.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyL3_2.setUnits("0.1 kWh")
_DpduOutputCurrentL1_3_Type = Integer32
_DpduOutputCurrentL1_3_Object = MibTableColumn
dpduOutputCurrentL1_3 = _DpduOutputCurrentL1_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 26),
    _DpduOutputCurrentL1_3_Type()
)
dpduOutputCurrentL1_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL1_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL1_3.setUnits("0.1 A")
_DpduOutputCurrentL2_3_Type = Integer32
_DpduOutputCurrentL2_3_Object = MibTableColumn
dpduOutputCurrentL2_3 = _DpduOutputCurrentL2_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 27),
    _DpduOutputCurrentL2_3_Type()
)
dpduOutputCurrentL2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL2_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL2_3.setUnits("0.1 A")
_DpduOutputCurrentL3_3_Type = Integer32
_DpduOutputCurrentL3_3_Object = MibTableColumn
dpduOutputCurrentL3_3 = _DpduOutputCurrentL3_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 28),
    _DpduOutputCurrentL3_3_Type()
)
dpduOutputCurrentL3_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL3_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL3_3.setUnits("0.1 A")
_DpduOutputWattageL1_3_Type = Integer32
_DpduOutputWattageL1_3_Object = MibTableColumn
dpduOutputWattageL1_3 = _DpduOutputWattageL1_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 29),
    _DpduOutputWattageL1_3_Type()
)
dpduOutputWattageL1_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL1_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL1_3.setUnits("1 Watt")
_DpduOutputWattageL2_3_Type = Integer32
_DpduOutputWattageL2_3_Object = MibTableColumn
dpduOutputWattageL2_3 = _DpduOutputWattageL2_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 30),
    _DpduOutputWattageL2_3_Type()
)
dpduOutputWattageL2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL2_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL2_3.setUnits("1 Watt")
_DpduOutputWattageL3_3_Type = Integer32
_DpduOutputWattageL3_3_Object = MibTableColumn
dpduOutputWattageL3_3 = _DpduOutputWattageL3_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 31),
    _DpduOutputWattageL3_3_Type()
)
dpduOutputWattageL3_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL3_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL3_3.setUnits("1 Watt")
_DpduOutputEnergyL1_3_Type = Integer32
_DpduOutputEnergyL1_3_Object = MibTableColumn
dpduOutputEnergyL1_3 = _DpduOutputEnergyL1_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 32),
    _DpduOutputEnergyL1_3_Type()
)
dpduOutputEnergyL1_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyL1_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyL1_3.setUnits("0.1 kWh")
_DpduOutputEnergyL2_3_Type = Integer32
_DpduOutputEnergyL2_3_Object = MibTableColumn
dpduOutputEnergyL2_3 = _DpduOutputEnergyL2_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 33),
    _DpduOutputEnergyL2_3_Type()
)
dpduOutputEnergyL2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyL2_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyL2_3.setUnits("0.1 kWh")
_DpduOutputEnergyL3_3_Type = Integer32
_DpduOutputEnergyL3_3_Object = MibTableColumn
dpduOutputEnergyL3_3 = _DpduOutputEnergyL3_3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 34),
    _DpduOutputEnergyL3_3_Type()
)
dpduOutputEnergyL3_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputEnergyL3_3.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputEnergyL3_3.setUnits("0.1 kWh")
_DpduOutputCurrentL1Total_Type = Integer32
_DpduOutputCurrentL1Total_Object = MibTableColumn
dpduOutputCurrentL1Total = _DpduOutputCurrentL1Total_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 35),
    _DpduOutputCurrentL1Total_Type()
)
dpduOutputCurrentL1Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL1Total.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL1Total.setUnits("0.1 A")
_DpduOutputCurrentL2Total_Type = Integer32
_DpduOutputCurrentL2Total_Object = MibTableColumn
dpduOutputCurrentL2Total = _DpduOutputCurrentL2Total_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 36),
    _DpduOutputCurrentL2Total_Type()
)
dpduOutputCurrentL2Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL2Total.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL2Total.setUnits("0.1 A")
_DpduOutputCurrentL3Total_Type = Integer32
_DpduOutputCurrentL3Total_Object = MibTableColumn
dpduOutputCurrentL3Total = _DpduOutputCurrentL3Total_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 37),
    _DpduOutputCurrentL3Total_Type()
)
dpduOutputCurrentL3Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentL3Total.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentL3Total.setUnits("0.1 A")
_DpduOutputCurrentTotal_Type = Integer32
_DpduOutputCurrentTotal_Object = MibTableColumn
dpduOutputCurrentTotal = _DpduOutputCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 38),
    _DpduOutputCurrentTotal_Type()
)
dpduOutputCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputCurrentTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputCurrentTotal.setUnits("0.1 A")
_DpduOutputWattageL1Total_Type = Integer32
_DpduOutputWattageL1Total_Object = MibTableColumn
dpduOutputWattageL1Total = _DpduOutputWattageL1Total_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 39),
    _DpduOutputWattageL1Total_Type()
)
dpduOutputWattageL1Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL1Total.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL1Total.setUnits("1 Watt")
_DpduOutputWattageL2Total_Type = Integer32
_DpduOutputWattageL2Total_Object = MibTableColumn
dpduOutputWattageL2Total = _DpduOutputWattageL2Total_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 40),
    _DpduOutputWattageL2Total_Type()
)
dpduOutputWattageL2Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL2Total.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL2Total.setUnits("1 Watt")
_DpduOutputWattageL3Total_Type = Integer32
_DpduOutputWattageL3Total_Object = MibTableColumn
dpduOutputWattageL3Total = _DpduOutputWattageL3Total_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 2, 1, 1, 41),
    _DpduOutputWattageL3Total_Type()
)
dpduOutputWattageL3Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduOutputWattageL3Total.setStatus("mandatory")
if mibBuilder.loadTexts:
    dpduOutputWattageL3Total.setUnits("1 Watt")
_DpduAlarm_ObjectIdentity = ObjectIdentity
dpduAlarm = _DpduAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3)
)
_DpduAlarmTable_Object = MibTable
dpduAlarmTable = _DpduAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1)
)
if mibBuilder.loadTexts:
    dpduAlarmTable.setStatus("mandatory")
_DpduAlarmEntry_Object = MibTableRow
dpduAlarmEntry = _DpduAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1)
)
dpduAlarmEntry.setIndexNames(
    (0, "DeltaPDU-MIB", "dpduAlarmPDUID"),
)
if mibBuilder.loadTexts:
    dpduAlarmEntry.setStatus("mandatory")


class _DpduAlarmPDUID_Type(Integer32):
    """Custom type dpduAlarmPDUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DpduAlarmPDUID_Type.__name__ = "Integer32"
_DpduAlarmPDUID_Object = MibTableColumn
dpduAlarmPDUID = _DpduAlarmPDUID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 1),
    _DpduAlarmPDUID_Type()
)
dpduAlarmPDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmPDUID.setStatus("mandatory")


class _DpduAlarmDisconnect_Type(Integer32):
    """Custom type dpduAlarmDisconnect based on Integer32"""
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


_DpduAlarmDisconnect_Type.__name__ = "Integer32"
_DpduAlarmDisconnect_Object = MibTableColumn
dpduAlarmDisconnect = _DpduAlarmDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 2),
    _DpduAlarmDisconnect_Type()
)
dpduAlarmDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmDisconnect.setStatus("mandatory")


class _DpduAlarmL1_1LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL1_1LoadMajor based on Integer32"""
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


_DpduAlarmL1_1LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL1_1LoadMajor_Object = MibTableColumn
dpduAlarmL1_1LoadMajor = _DpduAlarmL1_1LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 3),
    _DpduAlarmL1_1LoadMajor_Type()
)
dpduAlarmL1_1LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_1LoadMajor.setStatus("mandatory")


class _DpduAlarmL1_1LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL1_1LoadMinor based on Integer32"""
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


_DpduAlarmL1_1LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL1_1LoadMinor_Object = MibTableColumn
dpduAlarmL1_1LoadMinor = _DpduAlarmL1_1LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 4),
    _DpduAlarmL1_1LoadMinor_Type()
)
dpduAlarmL1_1LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_1LoadMinor.setStatus("mandatory")


class _DpduAlarmL1_1OutVoltMajor_Type(Integer32):
    """Custom type dpduAlarmL1_1OutVoltMajor based on Integer32"""
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


_DpduAlarmL1_1OutVoltMajor_Type.__name__ = "Integer32"
_DpduAlarmL1_1OutVoltMajor_Object = MibTableColumn
dpduAlarmL1_1OutVoltMajor = _DpduAlarmL1_1OutVoltMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 5),
    _DpduAlarmL1_1OutVoltMajor_Type()
)
dpduAlarmL1_1OutVoltMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_1OutVoltMajor.setStatus("mandatory")


class _DpduAlarmL1_1OutVoltMinor_Type(Integer32):
    """Custom type dpduAlarmL1_1OutVoltMinor based on Integer32"""
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


_DpduAlarmL1_1OutVoltMinor_Type.__name__ = "Integer32"
_DpduAlarmL1_1OutVoltMinor_Object = MibTableColumn
dpduAlarmL1_1OutVoltMinor = _DpduAlarmL1_1OutVoltMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 6),
    _DpduAlarmL1_1OutVoltMinor_Type()
)
dpduAlarmL1_1OutVoltMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_1OutVoltMinor.setStatus("mandatory")


class _DpduAlarmL2_1LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL2_1LoadMajor based on Integer32"""
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


_DpduAlarmL2_1LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL2_1LoadMajor_Object = MibTableColumn
dpduAlarmL2_1LoadMajor = _DpduAlarmL2_1LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 7),
    _DpduAlarmL2_1LoadMajor_Type()
)
dpduAlarmL2_1LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_1LoadMajor.setStatus("mandatory")


class _DpduAlarmL2_1LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL2_1LoadMinor based on Integer32"""
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


_DpduAlarmL2_1LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL2_1LoadMinor_Object = MibTableColumn
dpduAlarmL2_1LoadMinor = _DpduAlarmL2_1LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 8),
    _DpduAlarmL2_1LoadMinor_Type()
)
dpduAlarmL2_1LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_1LoadMinor.setStatus("mandatory")


class _DpduAlarmL2_1OutVoltMajor_Type(Integer32):
    """Custom type dpduAlarmL2_1OutVoltMajor based on Integer32"""
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


_DpduAlarmL2_1OutVoltMajor_Type.__name__ = "Integer32"
_DpduAlarmL2_1OutVoltMajor_Object = MibTableColumn
dpduAlarmL2_1OutVoltMajor = _DpduAlarmL2_1OutVoltMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 9),
    _DpduAlarmL2_1OutVoltMajor_Type()
)
dpduAlarmL2_1OutVoltMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_1OutVoltMajor.setStatus("mandatory")


class _DpduAlarmL2_1OutVoltMinor_Type(Integer32):
    """Custom type dpduAlarmL2_1OutVoltMinor based on Integer32"""
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


_DpduAlarmL2_1OutVoltMinor_Type.__name__ = "Integer32"
_DpduAlarmL2_1OutVoltMinor_Object = MibTableColumn
dpduAlarmL2_1OutVoltMinor = _DpduAlarmL2_1OutVoltMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 10),
    _DpduAlarmL2_1OutVoltMinor_Type()
)
dpduAlarmL2_1OutVoltMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_1OutVoltMinor.setStatus("mandatory")


class _DpduAlarmL3_1LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL3_1LoadMajor based on Integer32"""
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


_DpduAlarmL3_1LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL3_1LoadMajor_Object = MibTableColumn
dpduAlarmL3_1LoadMajor = _DpduAlarmL3_1LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 11),
    _DpduAlarmL3_1LoadMajor_Type()
)
dpduAlarmL3_1LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_1LoadMajor.setStatus("mandatory")


class _DpduAlarmL3_1LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL3_1LoadMinor based on Integer32"""
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


_DpduAlarmL3_1LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL3_1LoadMinor_Object = MibTableColumn
dpduAlarmL3_1LoadMinor = _DpduAlarmL3_1LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 12),
    _DpduAlarmL3_1LoadMinor_Type()
)
dpduAlarmL3_1LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_1LoadMinor.setStatus("mandatory")


class _DpduAlarmL3_1OutVoltMajor_Type(Integer32):
    """Custom type dpduAlarmL3_1OutVoltMajor based on Integer32"""
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


_DpduAlarmL3_1OutVoltMajor_Type.__name__ = "Integer32"
_DpduAlarmL3_1OutVoltMajor_Object = MibTableColumn
dpduAlarmL3_1OutVoltMajor = _DpduAlarmL3_1OutVoltMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 13),
    _DpduAlarmL3_1OutVoltMajor_Type()
)
dpduAlarmL3_1OutVoltMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_1OutVoltMajor.setStatus("mandatory")


class _DpduAlarmL3_1OutVoltMinor_Type(Integer32):
    """Custom type dpduAlarmL3_1OutVoltMinor based on Integer32"""
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


_DpduAlarmL3_1OutVoltMinor_Type.__name__ = "Integer32"
_DpduAlarmL3_1OutVoltMinor_Object = MibTableColumn
dpduAlarmL3_1OutVoltMinor = _DpduAlarmL3_1OutVoltMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 14),
    _DpduAlarmL3_1OutVoltMinor_Type()
)
dpduAlarmL3_1OutVoltMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_1OutVoltMinor.setStatus("mandatory")


class _DpduAlarmL123_1LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL123_1LoadMajor based on Integer32"""
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


_DpduAlarmL123_1LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL123_1LoadMajor_Object = MibTableColumn
dpduAlarmL123_1LoadMajor = _DpduAlarmL123_1LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 15),
    _DpduAlarmL123_1LoadMajor_Type()
)
dpduAlarmL123_1LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL123_1LoadMajor.setStatus("mandatory")


class _DpduAlarmL123_1LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL123_1LoadMinor based on Integer32"""
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


_DpduAlarmL123_1LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL123_1LoadMinor_Object = MibTableColumn
dpduAlarmL123_1LoadMinor = _DpduAlarmL123_1LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 16),
    _DpduAlarmL123_1LoadMinor_Type()
)
dpduAlarmL123_1LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL123_1LoadMinor.setStatus("mandatory")


class _DpduAlarmL1_1BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL1_1BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL1_1BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL1_1BreakerOpen_Object = MibTableColumn
dpduAlarmL1_1BreakerOpen = _DpduAlarmL1_1BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 17),
    _DpduAlarmL1_1BreakerOpen_Type()
)
dpduAlarmL1_1BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_1BreakerOpen.setStatus("mandatory")


class _DpduAlarmL2_1BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL2_1BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL2_1BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL2_1BreakerOpen_Object = MibTableColumn
dpduAlarmL2_1BreakerOpen = _DpduAlarmL2_1BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 18),
    _DpduAlarmL2_1BreakerOpen_Type()
)
dpduAlarmL2_1BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_1BreakerOpen.setStatus("mandatory")


class _DpduAlarmL3_1BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL3_1BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL3_1BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL3_1BreakerOpen_Object = MibTableColumn
dpduAlarmL3_1BreakerOpen = _DpduAlarmL3_1BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 19),
    _DpduAlarmL3_1BreakerOpen_Type()
)
dpduAlarmL3_1BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_1BreakerOpen.setStatus("mandatory")


class _DpduAlarmL1_2LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL1_2LoadMajor based on Integer32"""
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


_DpduAlarmL1_2LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL1_2LoadMajor_Object = MibTableColumn
dpduAlarmL1_2LoadMajor = _DpduAlarmL1_2LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 20),
    _DpduAlarmL1_2LoadMajor_Type()
)
dpduAlarmL1_2LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_2LoadMajor.setStatus("mandatory")


class _DpduAlarmL1_2LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL1_2LoadMinor based on Integer32"""
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


_DpduAlarmL1_2LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL1_2LoadMinor_Object = MibTableColumn
dpduAlarmL1_2LoadMinor = _DpduAlarmL1_2LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 21),
    _DpduAlarmL1_2LoadMinor_Type()
)
dpduAlarmL1_2LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_2LoadMinor.setStatus("mandatory")


class _DpduAlarmL2_2LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL2_2LoadMajor based on Integer32"""
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


_DpduAlarmL2_2LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL2_2LoadMajor_Object = MibTableColumn
dpduAlarmL2_2LoadMajor = _DpduAlarmL2_2LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 22),
    _DpduAlarmL2_2LoadMajor_Type()
)
dpduAlarmL2_2LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_2LoadMajor.setStatus("mandatory")


class _DpduAlarmL2_2LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL2_2LoadMinor based on Integer32"""
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


_DpduAlarmL2_2LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL2_2LoadMinor_Object = MibTableColumn
dpduAlarmL2_2LoadMinor = _DpduAlarmL2_2LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 23),
    _DpduAlarmL2_2LoadMinor_Type()
)
dpduAlarmL2_2LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_2LoadMinor.setStatus("mandatory")


class _DpduAlarmL3_2LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL3_2LoadMajor based on Integer32"""
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


_DpduAlarmL3_2LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL3_2LoadMajor_Object = MibTableColumn
dpduAlarmL3_2LoadMajor = _DpduAlarmL3_2LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 24),
    _DpduAlarmL3_2LoadMajor_Type()
)
dpduAlarmL3_2LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_2LoadMajor.setStatus("mandatory")


class _DpduAlarmL3_2LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL3_2LoadMinor based on Integer32"""
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


_DpduAlarmL3_2LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL3_2LoadMinor_Object = MibTableColumn
dpduAlarmL3_2LoadMinor = _DpduAlarmL3_2LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 25),
    _DpduAlarmL3_2LoadMinor_Type()
)
dpduAlarmL3_2LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_2LoadMinor.setStatus("mandatory")


class _DpduAlarmL1_2BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL1_2BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL1_2BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL1_2BreakerOpen_Object = MibTableColumn
dpduAlarmL1_2BreakerOpen = _DpduAlarmL1_2BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 26),
    _DpduAlarmL1_2BreakerOpen_Type()
)
dpduAlarmL1_2BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_2BreakerOpen.setStatus("mandatory")


class _DpduAlarmL2_2BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL2_2BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL2_2BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL2_2BreakerOpen_Object = MibTableColumn
dpduAlarmL2_2BreakerOpen = _DpduAlarmL2_2BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 27),
    _DpduAlarmL2_2BreakerOpen_Type()
)
dpduAlarmL2_2BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_2BreakerOpen.setStatus("mandatory")


class _DpduAlarmL3_2BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL3_2BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL3_2BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL3_2BreakerOpen_Object = MibTableColumn
dpduAlarmL3_2BreakerOpen = _DpduAlarmL3_2BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 28),
    _DpduAlarmL3_2BreakerOpen_Type()
)
dpduAlarmL3_2BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_2BreakerOpen.setStatus("mandatory")


class _DpduAlarmL1_3LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL1_3LoadMajor based on Integer32"""
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


_DpduAlarmL1_3LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL1_3LoadMajor_Object = MibTableColumn
dpduAlarmL1_3LoadMajor = _DpduAlarmL1_3LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 29),
    _DpduAlarmL1_3LoadMajor_Type()
)
dpduAlarmL1_3LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_3LoadMajor.setStatus("mandatory")


class _DpduAlarmL1_3LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL1_3LoadMinor based on Integer32"""
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


_DpduAlarmL1_3LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL1_3LoadMinor_Object = MibTableColumn
dpduAlarmL1_3LoadMinor = _DpduAlarmL1_3LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 30),
    _DpduAlarmL1_3LoadMinor_Type()
)
dpduAlarmL1_3LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_3LoadMinor.setStatus("mandatory")


class _DpduAlarmL2_3LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL2_3LoadMajor based on Integer32"""
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


_DpduAlarmL2_3LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL2_3LoadMajor_Object = MibTableColumn
dpduAlarmL2_3LoadMajor = _DpduAlarmL2_3LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 31),
    _DpduAlarmL2_3LoadMajor_Type()
)
dpduAlarmL2_3LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_3LoadMajor.setStatus("mandatory")


class _DpduAlarmL2_3LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL2_3LoadMinor based on Integer32"""
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


_DpduAlarmL2_3LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL2_3LoadMinor_Object = MibTableColumn
dpduAlarmL2_3LoadMinor = _DpduAlarmL2_3LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 32),
    _DpduAlarmL2_3LoadMinor_Type()
)
dpduAlarmL2_3LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_3LoadMinor.setStatus("mandatory")


class _DpduAlarmL3_3LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL3_3LoadMajor based on Integer32"""
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


_DpduAlarmL3_3LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL3_3LoadMajor_Object = MibTableColumn
dpduAlarmL3_3LoadMajor = _DpduAlarmL3_3LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 33),
    _DpduAlarmL3_3LoadMajor_Type()
)
dpduAlarmL3_3LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_3LoadMajor.setStatus("mandatory")


class _DpduAlarmL3_3LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL3_3LoadMinor based on Integer32"""
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


_DpduAlarmL3_3LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL3_3LoadMinor_Object = MibTableColumn
dpduAlarmL3_3LoadMinor = _DpduAlarmL3_3LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 34),
    _DpduAlarmL3_3LoadMinor_Type()
)
dpduAlarmL3_3LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_3LoadMinor.setStatus("mandatory")


class _DpduAlarmL1_3BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL1_3BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL1_3BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL1_3BreakerOpen_Object = MibTableColumn
dpduAlarmL1_3BreakerOpen = _DpduAlarmL1_3BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 35),
    _DpduAlarmL1_3BreakerOpen_Type()
)
dpduAlarmL1_3BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1_3BreakerOpen.setStatus("mandatory")


class _DpduAlarmL2_3BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL2_3BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL2_3BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL2_3BreakerOpen_Object = MibTableColumn
dpduAlarmL2_3BreakerOpen = _DpduAlarmL2_3BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 36),
    _DpduAlarmL2_3BreakerOpen_Type()
)
dpduAlarmL2_3BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2_3BreakerOpen.setStatus("mandatory")


class _DpduAlarmL3_3BreakerOpen_Type(Integer32):
    """Custom type dpduAlarmL3_3BreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_DpduAlarmL3_3BreakerOpen_Type.__name__ = "Integer32"
_DpduAlarmL3_3BreakerOpen_Object = MibTableColumn
dpduAlarmL3_3BreakerOpen = _DpduAlarmL3_3BreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 37),
    _DpduAlarmL3_3BreakerOpen_Type()
)
dpduAlarmL3_3BreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3_3BreakerOpen.setStatus("mandatory")


class _DpduAlarmL1LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL1LoadMajor based on Integer32"""
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


_DpduAlarmL1LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL1LoadMajor_Object = MibTableColumn
dpduAlarmL1LoadMajor = _DpduAlarmL1LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 38),
    _DpduAlarmL1LoadMajor_Type()
)
dpduAlarmL1LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1LoadMajor.setStatus("mandatory")


class _DpduAlarmL1LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL1LoadMinor based on Integer32"""
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


_DpduAlarmL1LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL1LoadMinor_Object = MibTableColumn
dpduAlarmL1LoadMinor = _DpduAlarmL1LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 39),
    _DpduAlarmL1LoadMinor_Type()
)
dpduAlarmL1LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL1LoadMinor.setStatus("mandatory")


class _DpduAlarmL2LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL2LoadMajor based on Integer32"""
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


_DpduAlarmL2LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL2LoadMajor_Object = MibTableColumn
dpduAlarmL2LoadMajor = _DpduAlarmL2LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 40),
    _DpduAlarmL2LoadMajor_Type()
)
dpduAlarmL2LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2LoadMajor.setStatus("mandatory")


class _DpduAlarmL2LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL2LoadMinor based on Integer32"""
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


_DpduAlarmL2LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL2LoadMinor_Object = MibTableColumn
dpduAlarmL2LoadMinor = _DpduAlarmL2LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 41),
    _DpduAlarmL2LoadMinor_Type()
)
dpduAlarmL2LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL2LoadMinor.setStatus("mandatory")


class _DpduAlarmL3LoadMajor_Type(Integer32):
    """Custom type dpduAlarmL3LoadMajor based on Integer32"""
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


_DpduAlarmL3LoadMajor_Type.__name__ = "Integer32"
_DpduAlarmL3LoadMajor_Object = MibTableColumn
dpduAlarmL3LoadMajor = _DpduAlarmL3LoadMajor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 42),
    _DpduAlarmL3LoadMajor_Type()
)
dpduAlarmL3LoadMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3LoadMajor.setStatus("mandatory")


class _DpduAlarmL3LoadMinor_Type(Integer32):
    """Custom type dpduAlarmL3LoadMinor based on Integer32"""
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


_DpduAlarmL3LoadMinor_Type.__name__ = "Integer32"
_DpduAlarmL3LoadMinor_Object = MibTableColumn
dpduAlarmL3LoadMinor = _DpduAlarmL3LoadMinor_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 3, 1, 1, 43),
    _DpduAlarmL3LoadMinor_Type()
)
dpduAlarmL3LoadMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpduAlarmL3LoadMinor.setStatus("mandatory")
_DpduTraps_ObjectIdentity = ObjectIdentity
dpduTraps = _DpduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20)
)

# Managed Objects groups


# Notification objects

dpduCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 1)
)
dpduCommunicationLost.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduCommunicationLost.setStatus(
        ""
    )

dpduCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 2)
)
dpduCommunicationEstablished.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduCommunicationEstablished.setStatus(
        ""
    )

dpduL1LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 3)
)
dpduL1LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMajorAlarm.setStatus(
        ""
    )

dpduL1LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 4)
)
dpduL1LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL1LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 5)
)
dpduL1LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMinorAlarm.setStatus(
        ""
    )

dpduL1LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 6)
)
dpduL1LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL1OutVoltMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 7)
)
dpduL1OutVoltMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1OutVoltMajorAlarm.setStatus(
        ""
    )

dpduL1OutVoltMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 8)
)
dpduL1OutVoltMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1OutVoltMajorAlarmRecover.setStatus(
        ""
    )

dpduL1OutVoltMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 9)
)
dpduL1OutVoltMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1OutVoltMinorAlarm.setStatus(
        ""
    )

dpduL1OutVoltMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 10)
)
dpduL1OutVoltMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1OutVoltMinorAlarmRecover.setStatus(
        ""
    )

dpduL2LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 11)
)
dpduL2LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMajorAlarm.setStatus(
        ""
    )

dpduL2LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 12)
)
dpduL2LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL2LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 13)
)
dpduL2LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMinorAlarm.setStatus(
        ""
    )

dpduL2LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 14)
)
dpduL2LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL2OutVoltMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 15)
)
dpduL2OutVoltMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2OutVoltMajorAlarm.setStatus(
        ""
    )

dpduL2OutVoltMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 16)
)
dpduL2OutVoltMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2OutVoltMajorAlarmRecover.setStatus(
        ""
    )

dpduL2OutVoltMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 17)
)
dpduL2OutVoltMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2OutVoltMinorAlarm.setStatus(
        ""
    )

dpduL2OutVoltMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 18)
)
dpduL2OutVoltMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2OutVoltMinorAlarmRecover.setStatus(
        ""
    )

dpduL3LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 19)
)
dpduL3LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMajorAlarm.setStatus(
        ""
    )

dpduL3LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 20)
)
dpduL3LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL3LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 21)
)
dpduL3LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMinorAlarm.setStatus(
        ""
    )

dpduL3LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 22)
)
dpduL3LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL3OutVoltMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 23)
)
dpduL3OutVoltMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3OutVoltMajorAlarm.setStatus(
        ""
    )

dpduL3OutVoltMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 24)
)
dpduL3OutVoltMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3OutVoltMajorAlarmRecover.setStatus(
        ""
    )

dpduL3OutVoltMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 25)
)
dpduL3OutVoltMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3OutVoltMinorAlarm.setStatus(
        ""
    )

dpduL3OutVoltMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 26)
)
dpduL3OutVoltMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3OutVoltMinorAlarmRecover.setStatus(
        ""
    )

dpduL12LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 27)
)
dpduL12LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL12LoadMajorAlarm.setStatus(
        ""
    )

dpduL12LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 28)
)
dpduL12LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL12LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL12LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 29)
)
dpduL12LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL12LoadMinorAlarm.setStatus(
        ""
    )

dpduL12LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 30)
)
dpduL12LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL12LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL1_1BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 31)
)
dpduL1_1BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_1BreakerOpen.setStatus(
        ""
    )

dpduL1_1BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 32)
)
dpduL1_1BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_1BreakerOpenRecover.setStatus(
        ""
    )

dpduL2_1BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 33)
)
dpduL2_1BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_1BreakerOpen.setStatus(
        ""
    )

dpduL2_1BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 34)
)
dpduL2_1BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_1BreakerOpenRecover.setStatus(
        ""
    )

dpduL3_1BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 35)
)
dpduL3_1BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_1BreakerOpen.setStatus(
        ""
    )

dpduL3_1BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 36)
)
dpduL3_1BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_1BreakerOpenRecover.setStatus(
        ""
    )

dpduL1_2LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 37)
)
dpduL1_2LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_2LoadMajorAlarm.setStatus(
        ""
    )

dpduL1_2LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 38)
)
dpduL1_2LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_2LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL1_2LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 39)
)
dpduL1_2LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_2LoadMinorAlarm.setStatus(
        ""
    )

dpduL1_2LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 40)
)
dpduL1_2LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_2LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL2_2LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 41)
)
dpduL2_2LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_2LoadMajorAlarm.setStatus(
        ""
    )

dpduL2_2LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 42)
)
dpduL2_2LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_2LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL2_2LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 43)
)
dpduL2_2LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_2LoadMinorAlarm.setStatus(
        ""
    )

dpduL2_2LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 44)
)
dpduL2_2LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_2LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL3_2LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 45)
)
dpduL3_2LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_2LoadMajorAlarm.setStatus(
        ""
    )

dpduL3_2LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 46)
)
dpduL3_2LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_2LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL3_2LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 47)
)
dpduL3_2LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_2LoadMinorAlarm.setStatus(
        ""
    )

dpduL3_2LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 48)
)
dpduL3_2LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_2LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL1_2BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 49)
)
dpduL1_2BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_2BreakerOpen.setStatus(
        ""
    )

dpduL1_2BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 50)
)
dpduL1_2BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_2BreakerOpenRecover.setStatus(
        ""
    )

dpduL2_2BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 51)
)
dpduL2_2BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_2BreakerOpen.setStatus(
        ""
    )

dpduL2_2BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 52)
)
dpduL2_2BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_2BreakerOpenRecover.setStatus(
        ""
    )

dpduL3_2BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 53)
)
dpduL3_2BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_2BreakerOpen.setStatus(
        ""
    )

dpduL3_2BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 54)
)
dpduL3_2BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_2BreakerOpenRecover.setStatus(
        ""
    )

dpduL1_3LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 55)
)
dpduL1_3LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_3LoadMajorAlarm.setStatus(
        ""
    )

dpduL1_3LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 56)
)
dpduL1_3LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_3LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL1_3LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 57)
)
dpduL1_3LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_3LoadMinorAlarm.setStatus(
        ""
    )

dpduL1_3LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 58)
)
dpduL1_3LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_3LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL2_3LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 59)
)
dpduL2_3LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_3LoadMajorAlarm.setStatus(
        ""
    )

dpduL2_3LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 60)
)
dpduL2_3LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_3LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL2_3LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 61)
)
dpduL2_3LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_3LoadMinorAlarm.setStatus(
        ""
    )

dpduL2_3LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 62)
)
dpduL2_3LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_3LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL3_3LoadMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 63)
)
dpduL3_3LoadMajorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_3LoadMajorAlarm.setStatus(
        ""
    )

dpduL3_3LoadMajorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 64)
)
dpduL3_3LoadMajorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_3LoadMajorAlarmRecover.setStatus(
        ""
    )

dpduL3_3LoadMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 65)
)
dpduL3_3LoadMinorAlarm.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_3LoadMinorAlarm.setStatus(
        ""
    )

dpduL3_3LoadMinorAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 66)
)
dpduL3_3LoadMinorAlarmRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_3LoadMinorAlarmRecover.setStatus(
        ""
    )

dpduL1_3BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 67)
)
dpduL1_3BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_3BreakerOpen.setStatus(
        ""
    )

dpduL1_3BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 68)
)
dpduL1_3BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1_3BreakerOpenRecover.setStatus(
        ""
    )

dpduL2_3BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 69)
)
dpduL2_3BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_3BreakerOpen.setStatus(
        ""
    )

dpduL2_3BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 70)
)
dpduL2_3BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2_3BreakerOpenRecover.setStatus(
        ""
    )

dpduL3_3BreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 71)
)
dpduL3_3BreakerOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_3BreakerOpen.setStatus(
        ""
    )

dpduL3_3BreakerOpenRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 72)
)
dpduL3_3BreakerOpenRecover.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3_3BreakerOpenRecover.setStatus(
        ""
    )

dpduL1LoadMajorAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 73)
)
dpduL1LoadMajorAlarm2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMajorAlarm2.setStatus(
        ""
    )

dpduL1LoadMajorAlarmRecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 74)
)
dpduL1LoadMajorAlarmRecover2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMajorAlarmRecover2.setStatus(
        ""
    )

dpduL1LoadMinorAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 75)
)
dpduL1LoadMinorAlarm2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMinorAlarm2.setStatus(
        ""
    )

dpduL1LoadMinorAlarmRecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 76)
)
dpduL1LoadMinorAlarmRecover2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL1LoadMinorAlarmRecover2.setStatus(
        ""
    )

dpduL2LoadMajorAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 77)
)
dpduL2LoadMajorAlarm2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMajorAlarm2.setStatus(
        ""
    )

dpduL2LoadMajorAlarmRecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 78)
)
dpduL2LoadMajorAlarmRecover2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMajorAlarmRecover2.setStatus(
        ""
    )

dpduL2LoadMinorAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 79)
)
dpduL2LoadMinorAlarm2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMinorAlarm2.setStatus(
        ""
    )

dpduL2LoadMinorAlarmRecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 80)
)
dpduL2LoadMinorAlarmRecover2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL2LoadMinorAlarmRecover2.setStatus(
        ""
    )

dpduL3LoadMajorAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 81)
)
dpduL3LoadMajorAlarm2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMajorAlarm2.setStatus(
        ""
    )

dpduL3LoadMajorAlarmRecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 82)
)
dpduL3LoadMajorAlarmRecover2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMajorAlarmRecover2.setStatus(
        ""
    )

dpduL3LoadMinorAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 83)
)
dpduL3LoadMinorAlarm2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMinorAlarm2.setStatus(
        ""
    )

dpduL3LoadMinorAlarmRecover2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 84)
)
dpduL3LoadMinorAlarmRecover2.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduL3LoadMinorAlarmRecover2.setStatus(
        ""
    )

dpduDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 85)
)
dpduDoorOpen.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduDoorOpen.setStatus(
        ""
    )

dpduDoorClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 32, 20, 0, 86)
)
dpduDoorClose.setObjects(
    ("DeltaPDU-MIB", "dpduAlarmPDUID")
)
if mibBuilder.loadTexts:
    dpduDoorClose.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaPDU-MIB",
    **{"delta": delta,
       "ups": ups,
       "pduv3": pduv3,
       "dpduIdent": dpduIdent,
       "dpduIdentManufacturer": dpduIdentManufacturer,
       "dpduIdentName": dpduIdentName,
       "dpduIdentAttachedDevices": dpduIdentAttachedDevices,
       "dpduIdentAgentSoftwareVersion": dpduIdentAgentSoftwareVersion,
       "dpduPDUNum": dpduPDUNum,
       "dpduIdentTable": dpduIdentTable,
       "dpduIdentEntry": dpduIdentEntry,
       "dpduIdentPDUID": dpduIdentPDUID,
       "dpduIdentEnabled": dpduIdentEnabled,
       "dpduIdentModel": dpduIdentModel,
       "dpduIdentSerialNumber": dpduIdentSerialNumber,
       "dpduIdentPDUFirmwareVersion": dpduIdentPDUFirmwareVersion,
       "dpduIdentPDUName": dpduIdentPDUName,
       "dpduIdentPDUAttachedDevices": dpduIdentPDUAttachedDevices,
       "dpduOutput": dpduOutput,
       "dpduOutputTable": dpduOutputTable,
       "dpduOutputEntry": dpduOutputEntry,
       "dpduOutputPDUID": dpduOutputPDUID,
       "dpduOutputFrequency": dpduOutputFrequency,
       "dpduOutputVoltage1": dpduOutputVoltage1,
       "dpduOutputCurrent1": dpduOutputCurrent1,
       "dpduOutputVoltage2": dpduOutputVoltage2,
       "dpduOutputCurrent2": dpduOutputCurrent2,
       "dpduOutputVoltage3": dpduOutputVoltage3,
       "dpduOutputCurrent3": dpduOutputCurrent3,
       "dpduOutputWattage1": dpduOutputWattage1,
       "dpduOutputEnergy1": dpduOutputEnergy1,
       "dpduOutputWattage2": dpduOutputWattage2,
       "dpduOutputEnergy2": dpduOutputEnergy2,
       "dpduOutputWattage3": dpduOutputWattage3,
       "dpduOutputEnergy3": dpduOutputEnergy3,
       "dpduOutputWattageTotal": dpduOutputWattageTotal,
       "dpduOutputEnergyTotal": dpduOutputEnergyTotal,
       "dpduOutputCurrentL1-2": dpduOutputCurrentL1_2,
       "dpduOutputCurrentL2-2": dpduOutputCurrentL2_2,
       "dpduOutputCurrentL3-2": dpduOutputCurrentL3_2,
       "dpduOutputWattageL1-2": dpduOutputWattageL1_2,
       "dpduOutputWattageL2-2": dpduOutputWattageL2_2,
       "dpduOutputWattageL3-2": dpduOutputWattageL3_2,
       "dpduOutputEnergyL1-2": dpduOutputEnergyL1_2,
       "dpduOutputEnergyL2-2": dpduOutputEnergyL2_2,
       "dpduOutputEnergyL3-2": dpduOutputEnergyL3_2,
       "dpduOutputCurrentL1-3": dpduOutputCurrentL1_3,
       "dpduOutputCurrentL2-3": dpduOutputCurrentL2_3,
       "dpduOutputCurrentL3-3": dpduOutputCurrentL3_3,
       "dpduOutputWattageL1-3": dpduOutputWattageL1_3,
       "dpduOutputWattageL2-3": dpduOutputWattageL2_3,
       "dpduOutputWattageL3-3": dpduOutputWattageL3_3,
       "dpduOutputEnergyL1-3": dpduOutputEnergyL1_3,
       "dpduOutputEnergyL2-3": dpduOutputEnergyL2_3,
       "dpduOutputEnergyL3-3": dpduOutputEnergyL3_3,
       "dpduOutputCurrentL1Total": dpduOutputCurrentL1Total,
       "dpduOutputCurrentL2Total": dpduOutputCurrentL2Total,
       "dpduOutputCurrentL3Total": dpduOutputCurrentL3Total,
       "dpduOutputCurrentTotal": dpduOutputCurrentTotal,
       "dpduOutputWattageL1Total": dpduOutputWattageL1Total,
       "dpduOutputWattageL2Total": dpduOutputWattageL2Total,
       "dpduOutputWattageL3Total": dpduOutputWattageL3Total,
       "dpduAlarm": dpduAlarm,
       "dpduAlarmTable": dpduAlarmTable,
       "dpduAlarmEntry": dpduAlarmEntry,
       "dpduAlarmPDUID": dpduAlarmPDUID,
       "dpduAlarmDisconnect": dpduAlarmDisconnect,
       "dpduAlarmL1-1LoadMajor": dpduAlarmL1_1LoadMajor,
       "dpduAlarmL1-1LoadMinor": dpduAlarmL1_1LoadMinor,
       "dpduAlarmL1-1OutVoltMajor": dpduAlarmL1_1OutVoltMajor,
       "dpduAlarmL1-1OutVoltMinor": dpduAlarmL1_1OutVoltMinor,
       "dpduAlarmL2-1LoadMajor": dpduAlarmL2_1LoadMajor,
       "dpduAlarmL2-1LoadMinor": dpduAlarmL2_1LoadMinor,
       "dpduAlarmL2-1OutVoltMajor": dpduAlarmL2_1OutVoltMajor,
       "dpduAlarmL2-1OutVoltMinor": dpduAlarmL2_1OutVoltMinor,
       "dpduAlarmL3-1LoadMajor": dpduAlarmL3_1LoadMajor,
       "dpduAlarmL3-1LoadMinor": dpduAlarmL3_1LoadMinor,
       "dpduAlarmL3-1OutVoltMajor": dpduAlarmL3_1OutVoltMajor,
       "dpduAlarmL3-1OutVoltMinor": dpduAlarmL3_1OutVoltMinor,
       "dpduAlarmL123-1LoadMajor": dpduAlarmL123_1LoadMajor,
       "dpduAlarmL123-1LoadMinor": dpduAlarmL123_1LoadMinor,
       "dpduAlarmL1-1BreakerOpen": dpduAlarmL1_1BreakerOpen,
       "dpduAlarmL2-1BreakerOpen": dpduAlarmL2_1BreakerOpen,
       "dpduAlarmL3-1BreakerOpen": dpduAlarmL3_1BreakerOpen,
       "dpduAlarmL1-2LoadMajor": dpduAlarmL1_2LoadMajor,
       "dpduAlarmL1-2LoadMinor": dpduAlarmL1_2LoadMinor,
       "dpduAlarmL2-2LoadMajor": dpduAlarmL2_2LoadMajor,
       "dpduAlarmL2-2LoadMinor": dpduAlarmL2_2LoadMinor,
       "dpduAlarmL3-2LoadMajor": dpduAlarmL3_2LoadMajor,
       "dpduAlarmL3-2LoadMinor": dpduAlarmL3_2LoadMinor,
       "dpduAlarmL1-2BreakerOpen": dpduAlarmL1_2BreakerOpen,
       "dpduAlarmL2-2BreakerOpen": dpduAlarmL2_2BreakerOpen,
       "dpduAlarmL3-2BreakerOpen": dpduAlarmL3_2BreakerOpen,
       "dpduAlarmL1-3LoadMajor": dpduAlarmL1_3LoadMajor,
       "dpduAlarmL1-3LoadMinor": dpduAlarmL1_3LoadMinor,
       "dpduAlarmL2-3LoadMajor": dpduAlarmL2_3LoadMajor,
       "dpduAlarmL2-3LoadMinor": dpduAlarmL2_3LoadMinor,
       "dpduAlarmL3-3LoadMajor": dpduAlarmL3_3LoadMajor,
       "dpduAlarmL3-3LoadMinor": dpduAlarmL3_3LoadMinor,
       "dpduAlarmL1-3BreakerOpen": dpduAlarmL1_3BreakerOpen,
       "dpduAlarmL2-3BreakerOpen": dpduAlarmL2_3BreakerOpen,
       "dpduAlarmL3-3BreakerOpen": dpduAlarmL3_3BreakerOpen,
       "dpduAlarmL1LoadMajor": dpduAlarmL1LoadMajor,
       "dpduAlarmL1LoadMinor": dpduAlarmL1LoadMinor,
       "dpduAlarmL2LoadMajor": dpduAlarmL2LoadMajor,
       "dpduAlarmL2LoadMinor": dpduAlarmL2LoadMinor,
       "dpduAlarmL3LoadMajor": dpduAlarmL3LoadMajor,
       "dpduAlarmL3LoadMinor": dpduAlarmL3LoadMinor,
       "dpduTraps": dpduTraps,
       "dpduCommunicationLost": dpduCommunicationLost,
       "dpduCommunicationEstablished": dpduCommunicationEstablished,
       "dpduL1LoadMajorAlarm": dpduL1LoadMajorAlarm,
       "dpduL1LoadMajorAlarmRecover": dpduL1LoadMajorAlarmRecover,
       "dpduL1LoadMinorAlarm": dpduL1LoadMinorAlarm,
       "dpduL1LoadMinorAlarmRecover": dpduL1LoadMinorAlarmRecover,
       "dpduL1OutVoltMajorAlarm": dpduL1OutVoltMajorAlarm,
       "dpduL1OutVoltMajorAlarmRecover": dpduL1OutVoltMajorAlarmRecover,
       "dpduL1OutVoltMinorAlarm": dpduL1OutVoltMinorAlarm,
       "dpduL1OutVoltMinorAlarmRecover": dpduL1OutVoltMinorAlarmRecover,
       "dpduL2LoadMajorAlarm": dpduL2LoadMajorAlarm,
       "dpduL2LoadMajorAlarmRecover": dpduL2LoadMajorAlarmRecover,
       "dpduL2LoadMinorAlarm": dpduL2LoadMinorAlarm,
       "dpduL2LoadMinorAlarmRecover": dpduL2LoadMinorAlarmRecover,
       "dpduL2OutVoltMajorAlarm": dpduL2OutVoltMajorAlarm,
       "dpduL2OutVoltMajorAlarmRecover": dpduL2OutVoltMajorAlarmRecover,
       "dpduL2OutVoltMinorAlarm": dpduL2OutVoltMinorAlarm,
       "dpduL2OutVoltMinorAlarmRecover": dpduL2OutVoltMinorAlarmRecover,
       "dpduL3LoadMajorAlarm": dpduL3LoadMajorAlarm,
       "dpduL3LoadMajorAlarmRecover": dpduL3LoadMajorAlarmRecover,
       "dpduL3LoadMinorAlarm": dpduL3LoadMinorAlarm,
       "dpduL3LoadMinorAlarmRecover": dpduL3LoadMinorAlarmRecover,
       "dpduL3OutVoltMajorAlarm": dpduL3OutVoltMajorAlarm,
       "dpduL3OutVoltMajorAlarmRecover": dpduL3OutVoltMajorAlarmRecover,
       "dpduL3OutVoltMinorAlarm": dpduL3OutVoltMinorAlarm,
       "dpduL3OutVoltMinorAlarmRecover": dpduL3OutVoltMinorAlarmRecover,
       "dpduL12LoadMajorAlarm": dpduL12LoadMajorAlarm,
       "dpduL12LoadMajorAlarmRecover": dpduL12LoadMajorAlarmRecover,
       "dpduL12LoadMinorAlarm": dpduL12LoadMinorAlarm,
       "dpduL12LoadMinorAlarmRecover": dpduL12LoadMinorAlarmRecover,
       "dpduL1-1BreakerOpen": dpduL1_1BreakerOpen,
       "dpduL1-1BreakerOpenRecover": dpduL1_1BreakerOpenRecover,
       "dpduL2-1BreakerOpen": dpduL2_1BreakerOpen,
       "dpduL2-1BreakerOpenRecover": dpduL2_1BreakerOpenRecover,
       "dpduL3-1BreakerOpen": dpduL3_1BreakerOpen,
       "dpduL3-1BreakerOpenRecover": dpduL3_1BreakerOpenRecover,
       "dpduL1-2LoadMajorAlarm": dpduL1_2LoadMajorAlarm,
       "dpduL1-2LoadMajorAlarmRecover": dpduL1_2LoadMajorAlarmRecover,
       "dpduL1-2LoadMinorAlarm": dpduL1_2LoadMinorAlarm,
       "dpduL1-2LoadMinorAlarmRecover": dpduL1_2LoadMinorAlarmRecover,
       "dpduL2-2LoadMajorAlarm": dpduL2_2LoadMajorAlarm,
       "dpduL2-2LoadMajorAlarmRecover": dpduL2_2LoadMajorAlarmRecover,
       "dpduL2-2LoadMinorAlarm": dpduL2_2LoadMinorAlarm,
       "dpduL2-2LoadMinorAlarmRecover": dpduL2_2LoadMinorAlarmRecover,
       "dpduL3-2LoadMajorAlarm": dpduL3_2LoadMajorAlarm,
       "dpduL3-2LoadMajorAlarmRecover": dpduL3_2LoadMajorAlarmRecover,
       "dpduL3-2LoadMinorAlarm": dpduL3_2LoadMinorAlarm,
       "dpduL3-2LoadMinorAlarmRecover": dpduL3_2LoadMinorAlarmRecover,
       "dpduL1-2BreakerOpen": dpduL1_2BreakerOpen,
       "dpduL1-2BreakerOpenRecover": dpduL1_2BreakerOpenRecover,
       "dpduL2-2BreakerOpen": dpduL2_2BreakerOpen,
       "dpduL2-2BreakerOpenRecover": dpduL2_2BreakerOpenRecover,
       "dpduL3-2BreakerOpen": dpduL3_2BreakerOpen,
       "dpduL3-2BreakerOpenRecover": dpduL3_2BreakerOpenRecover,
       "dpduL1-3LoadMajorAlarm": dpduL1_3LoadMajorAlarm,
       "dpduL1-3LoadMajorAlarmRecover": dpduL1_3LoadMajorAlarmRecover,
       "dpduL1-3LoadMinorAlarm": dpduL1_3LoadMinorAlarm,
       "dpduL1-3LoadMinorAlarmRecover": dpduL1_3LoadMinorAlarmRecover,
       "dpduL2-3LoadMajorAlarm": dpduL2_3LoadMajorAlarm,
       "dpduL2-3LoadMajorAlarmRecover": dpduL2_3LoadMajorAlarmRecover,
       "dpduL2-3LoadMinorAlarm": dpduL2_3LoadMinorAlarm,
       "dpduL2-3LoadMinorAlarmRecover": dpduL2_3LoadMinorAlarmRecover,
       "dpduL3-3LoadMajorAlarm": dpduL3_3LoadMajorAlarm,
       "dpduL3-3LoadMajorAlarmRecover": dpduL3_3LoadMajorAlarmRecover,
       "dpduL3-3LoadMinorAlarm": dpduL3_3LoadMinorAlarm,
       "dpduL3-3LoadMinorAlarmRecover": dpduL3_3LoadMinorAlarmRecover,
       "dpduL1-3BreakerOpen": dpduL1_3BreakerOpen,
       "dpduL1-3BreakerOpenRecover": dpduL1_3BreakerOpenRecover,
       "dpduL2-3BreakerOpen": dpduL2_3BreakerOpen,
       "dpduL2-3BreakerOpenRecover": dpduL2_3BreakerOpenRecover,
       "dpduL3-3BreakerOpen": dpduL3_3BreakerOpen,
       "dpduL3-3BreakerOpenRecover": dpduL3_3BreakerOpenRecover,
       "dpduL1LoadMajorAlarm2": dpduL1LoadMajorAlarm2,
       "dpduL1LoadMajorAlarmRecover2": dpduL1LoadMajorAlarmRecover2,
       "dpduL1LoadMinorAlarm2": dpduL1LoadMinorAlarm2,
       "dpduL1LoadMinorAlarmRecover2": dpduL1LoadMinorAlarmRecover2,
       "dpduL2LoadMajorAlarm2": dpduL2LoadMajorAlarm2,
       "dpduL2LoadMajorAlarmRecover2": dpduL2LoadMajorAlarmRecover2,
       "dpduL2LoadMinorAlarm2": dpduL2LoadMinorAlarm2,
       "dpduL2LoadMinorAlarmRecover2": dpduL2LoadMinorAlarmRecover2,
       "dpduL3LoadMajorAlarm2": dpduL3LoadMajorAlarm2,
       "dpduL3LoadMajorAlarmRecover2": dpduL3LoadMajorAlarmRecover2,
       "dpduL3LoadMinorAlarm2": dpduL3LoadMinorAlarm2,
       "dpduL3LoadMinorAlarmRecover2": dpduL3LoadMinorAlarmRecover2,
       "dpduDoorOpen": dpduDoorOpen,
       "dpduDoorClose": dpduDoorClose}
)
