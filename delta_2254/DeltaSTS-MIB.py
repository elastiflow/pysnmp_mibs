# SNMP MIB module (DeltaSTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_2254/DeltaSTS-MIB.mib
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
_Sts_ObjectIdentity = ObjectIdentity
sts = _Sts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61)
)
_StsAgent_ObjectIdentity = ObjectIdentity
stsAgent = _StsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 1)
)


class _StsAgentManufacturer_Type(DisplayString):
    """Custom type stsAgentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StsAgentManufacturer_Type.__name__ = "DisplayString"
_StsAgentManufacturer_Object = MibScalar
stsAgentManufacturer = _StsAgentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 1, 1),
    _StsAgentManufacturer_Type()
)
stsAgentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsAgentManufacturer.setStatus("mandatory")


class _StsAgentVersion_Type(DisplayString):
    """Custom type stsAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StsAgentVersion_Type.__name__ = "DisplayString"
_StsAgentVersion_Object = MibScalar
stsAgentVersion = _StsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 1, 2),
    _StsAgentVersion_Type()
)
stsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsAgentVersion.setStatus("mandatory")
_StsAgentDevLink_Type = Integer32
_StsAgentDevLink_Object = MibScalar
stsAgentDevLink = _StsAgentDevLink_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 1, 3),
    _StsAgentDevLink_Type()
)
stsAgentDevLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsAgentDevLink.setStatus("mandatory")
_StsIdent_ObjectIdentity = ObjectIdentity
stsIdent = _StsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2)
)


class _StsIdentManufacturer_Type(DisplayString):
    """Custom type stsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StsIdentManufacturer_Type.__name__ = "DisplayString"
_StsIdentManufacturer_Object = MibScalar
stsIdentManufacturer = _StsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 1),
    _StsIdentManufacturer_Type()
)
stsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentManufacturer.setStatus("mandatory")


class _StsIdentModel_Type(DisplayString):
    """Custom type stsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StsIdentModel_Type.__name__ = "DisplayString"
_StsIdentModel_Object = MibScalar
stsIdentModel = _StsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 2),
    _StsIdentModel_Type()
)
stsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentModel.setStatus("mandatory")


class _StsIdentSysSerialNumber_Type(DisplayString):
    """Custom type stsIdentSysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StsIdentSysSerialNumber_Type.__name__ = "DisplayString"
_StsIdentSysSerialNumber_Object = MibScalar
stsIdentSysSerialNumber = _StsIdentSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 3),
    _StsIdentSysSerialNumber_Type()
)
stsIdentSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentSysSerialNumber.setStatus("mandatory")


class _StsIdentSTS1SerialNumber_Type(DisplayString):
    """Custom type stsIdentSTS1SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StsIdentSTS1SerialNumber_Type.__name__ = "DisplayString"
_StsIdentSTS1SerialNumber_Object = MibScalar
stsIdentSTS1SerialNumber = _StsIdentSTS1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 4),
    _StsIdentSTS1SerialNumber_Type()
)
stsIdentSTS1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentSTS1SerialNumber.setStatus("mandatory")


class _StsIdentSTS2SerialNumber_Type(DisplayString):
    """Custom type stsIdentSTS2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StsIdentSTS2SerialNumber_Type.__name__ = "DisplayString"
_StsIdentSTS2SerialNumber_Object = MibScalar
stsIdentSTS2SerialNumber = _StsIdentSTS2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 5),
    _StsIdentSTS2SerialNumber_Type()
)
stsIdentSTS2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentSTS2SerialNumber.setStatus("mandatory")


class _StsIdentSTS1FWVersion_Type(DisplayString):
    """Custom type stsIdentSTS1FWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StsIdentSTS1FWVersion_Type.__name__ = "DisplayString"
_StsIdentSTS1FWVersion_Object = MibScalar
stsIdentSTS1FWVersion = _StsIdentSTS1FWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 6),
    _StsIdentSTS1FWVersion_Type()
)
stsIdentSTS1FWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentSTS1FWVersion.setStatus("mandatory")


class _StsIdentSTS2FWVersion_Type(DisplayString):
    """Custom type stsIdentSTS2FWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StsIdentSTS2FWVersion_Type.__name__ = "DisplayString"
_StsIdentSTS2FWVersion_Object = MibScalar
stsIdentSTS2FWVersion = _StsIdentSTS2FWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 7),
    _StsIdentSTS2FWVersion_Type()
)
stsIdentSTS2FWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentSTS2FWVersion.setStatus("mandatory")


class _StsIdentModuleType_Type(Integer32):
    """Custom type stsIdentModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type-3p3w", 1),
          ("type-3p4w", 2))
    )


_StsIdentModuleType_Type.__name__ = "Integer32"
_StsIdentModuleType_Object = MibScalar
stsIdentModuleType = _StsIdentModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 2, 8),
    _StsIdentModuleType_Type()
)
stsIdentModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsIdentModuleType.setStatus("mandatory")
_StsInput_ObjectIdentity = ObjectIdentity
stsInput = _StsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3)
)
_StsInputTable_Object = MibTable
stsInputTable = _StsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1)
)
if mibBuilder.loadTexts:
    stsInputTable.setStatus("mandatory")
_StsInputEntry_Object = MibTableRow
stsInputEntry = _StsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1)
)
stsInputEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsInputIndex"),
)
if mibBuilder.loadTexts:
    stsInputEntry.setStatus("mandatory")
_StsInputSource1PhaseVoltage_Type = Integer32
_StsInputSource1PhaseVoltage_Object = MibTableColumn
stsInputSource1PhaseVoltage = _StsInputSource1PhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 1),
    _StsInputSource1PhaseVoltage_Type()
)
stsInputSource1PhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1PhaseVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1PhaseVoltage.setUnits("0.1 V")
_StsInputSource1LineVoltage_Type = Integer32
_StsInputSource1LineVoltage_Object = MibTableColumn
stsInputSource1LineVoltage = _StsInputSource1LineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 2),
    _StsInputSource1LineVoltage_Type()
)
stsInputSource1LineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1LineVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1LineVoltage.setUnits("0.1 V")
_StsInputSource1Current_Type = Integer32
_StsInputSource1Current_Object = MibTableColumn
stsInputSource1Current = _StsInputSource1Current_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 3),
    _StsInputSource1Current_Type()
)
stsInputSource1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1Current.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1Current.setUnits("0.1 A")
_StsInputSource1KVA_Type = Integer32
_StsInputSource1KVA_Object = MibTableColumn
stsInputSource1KVA = _StsInputSource1KVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 4),
    _StsInputSource1KVA_Type()
)
stsInputSource1KVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1KVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1KVA.setUnits("0.1 kVA")
_StsInputSource1KW_Type = Integer32
_StsInputSource1KW_Object = MibTableColumn
stsInputSource1KW = _StsInputSource1KW_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 5),
    _StsInputSource1KW_Type()
)
stsInputSource1KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1KW.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1KW.setUnits("0.1 kW")


class _StsInputSource1Load_Type(Integer32):
    """Custom type stsInputSource1Load based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsInputSource1Load_Type.__name__ = "Integer32"
_StsInputSource1Load_Object = MibTableColumn
stsInputSource1Load = _StsInputSource1Load_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 6),
    _StsInputSource1Load_Type()
)
stsInputSource1Load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1Load.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1Load.setUnits("1 %")
_StsInputSource2PhaseVoltage_Type = Integer32
_StsInputSource2PhaseVoltage_Object = MibTableColumn
stsInputSource2PhaseVoltage = _StsInputSource2PhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 7),
    _StsInputSource2PhaseVoltage_Type()
)
stsInputSource2PhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2PhaseVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2PhaseVoltage.setUnits("0.1 V")
_StsInputSource2LineVoltage_Type = Integer32
_StsInputSource2LineVoltage_Object = MibTableColumn
stsInputSource2LineVoltage = _StsInputSource2LineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 8),
    _StsInputSource2LineVoltage_Type()
)
stsInputSource2LineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2LineVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2LineVoltage.setUnits("0.1 V")
_StsInputSource2Current_Type = Integer32
_StsInputSource2Current_Object = MibTableColumn
stsInputSource2Current = _StsInputSource2Current_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 9),
    _StsInputSource2Current_Type()
)
stsInputSource2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2Current.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2Current.setUnits("0.1 A")
_StsInputSource2KVA_Type = Integer32
_StsInputSource2KVA_Object = MibTableColumn
stsInputSource2KVA = _StsInputSource2KVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 10),
    _StsInputSource2KVA_Type()
)
stsInputSource2KVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2KVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2KVA.setUnits("0.1 kVA")
_StsInputSource2KW_Type = Integer32
_StsInputSource2KW_Object = MibTableColumn
stsInputSource2KW = _StsInputSource2KW_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 11),
    _StsInputSource2KW_Type()
)
stsInputSource2KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2KW.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2KW.setUnits("0.1 kW")


class _StsInputSource2Load_Type(Integer32):
    """Custom type stsInputSource2Load based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsInputSource2Load_Type.__name__ = "Integer32"
_StsInputSource2Load_Object = MibTableColumn
stsInputSource2Load = _StsInputSource2Load_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 12),
    _StsInputSource2Load_Type()
)
stsInputSource2Load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2Load.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2Load.setUnits("1 %")


class _StsInputIndex_Type(Integer32):
    """Custom type stsInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase-R", 1),
          ("phase-S", 2),
          ("phase-T", 3))
    )


_StsInputIndex_Type.__name__ = "Integer32"
_StsInputIndex_Object = MibTableColumn
stsInputIndex = _StsInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 1, 1, 13),
    _StsInputIndex_Type()
)
stsInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stsInputIndex.setStatus("mandatory")
_StsInputSource1NeutralCurrent_Type = Integer32
_StsInputSource1NeutralCurrent_Object = MibScalar
stsInputSource1NeutralCurrent = _StsInputSource1NeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 2),
    _StsInputSource1NeutralCurrent_Type()
)
stsInputSource1NeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1NeutralCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1NeutralCurrent.setUnits("0.1 A")
_StsInputSource1Frequency_Type = Integer32
_StsInputSource1Frequency_Object = MibScalar
stsInputSource1Frequency = _StsInputSource1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 3),
    _StsInputSource1Frequency_Type()
)
stsInputSource1Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1Frequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1Frequency.setUnits("0.1 Hz")
_StsInputSource1TotalKVA_Type = Integer32
_StsInputSource1TotalKVA_Object = MibScalar
stsInputSource1TotalKVA = _StsInputSource1TotalKVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 4),
    _StsInputSource1TotalKVA_Type()
)
stsInputSource1TotalKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1TotalKVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1TotalKVA.setUnits("0.1 kVA")
_StsInputSource1TotalKW_Type = Integer32
_StsInputSource1TotalKW_Object = MibScalar
stsInputSource1TotalKW = _StsInputSource1TotalKW_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 5),
    _StsInputSource1TotalKW_Type()
)
stsInputSource1TotalKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1TotalKW.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1TotalKW.setUnits("0.1 kW")


class _StsInputSource1NeutralLoad_Type(Integer32):
    """Custom type stsInputSource1NeutralLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsInputSource1NeutralLoad_Type.__name__ = "Integer32"
_StsInputSource1NeutralLoad_Object = MibScalar
stsInputSource1NeutralLoad = _StsInputSource1NeutralLoad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 6),
    _StsInputSource1NeutralLoad_Type()
)
stsInputSource1NeutralLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource1NeutralLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource1NeutralLoad.setUnits("1 %")
_StsInputSource2NeutralCurrent_Type = Integer32
_StsInputSource2NeutralCurrent_Object = MibScalar
stsInputSource2NeutralCurrent = _StsInputSource2NeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 7),
    _StsInputSource2NeutralCurrent_Type()
)
stsInputSource2NeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2NeutralCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2NeutralCurrent.setUnits("0.1 A")
_StsInputSource2Frequency_Type = Integer32
_StsInputSource2Frequency_Object = MibScalar
stsInputSource2Frequency = _StsInputSource2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 8),
    _StsInputSource2Frequency_Type()
)
stsInputSource2Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2Frequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2Frequency.setUnits("0.1 Hz")
_StsInputSource2TotalKVA_Type = Integer32
_StsInputSource2TotalKVA_Object = MibScalar
stsInputSource2TotalKVA = _StsInputSource2TotalKVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 9),
    _StsInputSource2TotalKVA_Type()
)
stsInputSource2TotalKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2TotalKVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2TotalKVA.setUnits("0.1 kVA")
_StsInputSource2TotalKW_Type = Integer32
_StsInputSource2TotalKW_Object = MibScalar
stsInputSource2TotalKW = _StsInputSource2TotalKW_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 10),
    _StsInputSource2TotalKW_Type()
)
stsInputSource2TotalKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2TotalKW.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2TotalKW.setUnits("0.1 kW")


class _StsInputSource2NeutralLoad_Type(Integer32):
    """Custom type stsInputSource2NeutralLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsInputSource2NeutralLoad_Type.__name__ = "Integer32"
_StsInputSource2NeutralLoad_Object = MibScalar
stsInputSource2NeutralLoad = _StsInputSource2NeutralLoad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 11),
    _StsInputSource2NeutralLoad_Type()
)
stsInputSource2NeutralLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputSource2NeutralLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputSource2NeutralLoad.setUnits("1 %")
_StsInputDifference_Type = Integer32
_StsInputDifference_Object = MibScalar
stsInputDifference = _StsInputDifference_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 3, 12),
    _StsInputDifference_Type()
)
stsInputDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsInputDifference.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsInputDifference.setUnits("0.1 Degree")
_StsOutput_ObjectIdentity = ObjectIdentity
stsOutput = _StsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4)
)
_StsOutputTable_Object = MibTable
stsOutputTable = _StsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1)
)
if mibBuilder.loadTexts:
    stsOutputTable.setStatus("mandatory")
_StsOutputEntry_Object = MibTableRow
stsOutputEntry = _StsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1)
)
stsOutputEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsOutputIndex"),
)
if mibBuilder.loadTexts:
    stsOutputEntry.setStatus("mandatory")
_StsOutputPhaseVoltage_Type = Integer32
_StsOutputPhaseVoltage_Object = MibTableColumn
stsOutputPhaseVoltage = _StsOutputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 1),
    _StsOutputPhaseVoltage_Type()
)
stsOutputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputPhaseVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputPhaseVoltage.setUnits("0.1 V")
_StsOutputLineVoltage_Type = Integer32
_StsOutputLineVoltage_Object = MibTableColumn
stsOutputLineVoltage = _StsOutputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 2),
    _StsOutputLineVoltage_Type()
)
stsOutputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputLineVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputLineVoltage.setUnits("0.1 V")
_StsOutputCurrent_Type = Integer32
_StsOutputCurrent_Object = MibTableColumn
stsOutputCurrent = _StsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 3),
    _StsOutputCurrent_Type()
)
stsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputCurrent.setUnits("0.1 A")


class _StsOutputPF_Type(Integer32):
    """Custom type stsOutputPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsOutputPF_Type.__name__ = "Integer32"
_StsOutputPF_Object = MibTableColumn
stsOutputPF = _StsOutputPF_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 4),
    _StsOutputPF_Type()
)
stsOutputPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputPF.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputPF.setUnits("0.01")


class _StsOutputCF_Type(Integer32):
    """Custom type stsOutputCF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsOutputCF_Type.__name__ = "Integer32"
_StsOutputCF_Object = MibTableColumn
stsOutputCF = _StsOutputCF_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 5),
    _StsOutputCF_Type()
)
stsOutputCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputCF.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputCF.setUnits("0.01")
_StsOutputKVA_Type = Integer32
_StsOutputKVA_Object = MibTableColumn
stsOutputKVA = _StsOutputKVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 6),
    _StsOutputKVA_Type()
)
stsOutputKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputKVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputKVA.setUnits("0.1 kVA")
_StsOutputKW_Type = Integer32
_StsOutputKW_Object = MibTableColumn
stsOutputKW = _StsOutputKW_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 7),
    _StsOutputKW_Type()
)
stsOutputKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputKW.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputKW.setUnits("0.1 kW")


class _StsOutputLoad_Type(Integer32):
    """Custom type stsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsOutputLoad_Type.__name__ = "Integer32"
_StsOutputLoad_Object = MibTableColumn
stsOutputLoad = _StsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 8),
    _StsOutputLoad_Type()
)
stsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputLoad.setUnits("1 %")


class _StsOutputIndex_Type(Integer32):
    """Custom type stsOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase-R", 1),
          ("phase-S", 2),
          ("phase-T", 3))
    )


_StsOutputIndex_Type.__name__ = "Integer32"
_StsOutputIndex_Object = MibTableColumn
stsOutputIndex = _StsOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 1, 1, 9),
    _StsOutputIndex_Type()
)
stsOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputIndex.setStatus("mandatory")
_StsOutputNeutralCurrent_Type = Integer32
_StsOutputNeutralCurrent_Object = MibScalar
stsOutputNeutralCurrent = _StsOutputNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 2),
    _StsOutputNeutralCurrent_Type()
)
stsOutputNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputNeutralCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputNeutralCurrent.setUnits("0.1 A")
_StsOutputFrequency_Type = Integer32
_StsOutputFrequency_Object = MibScalar
stsOutputFrequency = _StsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 3),
    _StsOutputFrequency_Type()
)
stsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputFrequency.setUnits("0.1 Hz")


class _StsOutputNeutralCF_Type(Integer32):
    """Custom type stsOutputNeutralCF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsOutputNeutralCF_Type.__name__ = "Integer32"
_StsOutputNeutralCF_Object = MibScalar
stsOutputNeutralCF = _StsOutputNeutralCF_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 4),
    _StsOutputNeutralCF_Type()
)
stsOutputNeutralCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputNeutralCF.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputNeutralCF.setUnits("0.01")


class _StsOutputTotalPF_Type(Integer32):
    """Custom type stsOutputTotalPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsOutputTotalPF_Type.__name__ = "Integer32"
_StsOutputTotalPF_Object = MibScalar
stsOutputTotalPF = _StsOutputTotalPF_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 5),
    _StsOutputTotalPF_Type()
)
stsOutputTotalPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputTotalPF.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputTotalPF.setUnits("0.01")
_StsOutputTotalKVA_Type = Integer32
_StsOutputTotalKVA_Object = MibScalar
stsOutputTotalKVA = _StsOutputTotalKVA_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 6),
    _StsOutputTotalKVA_Type()
)
stsOutputTotalKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputTotalKVA.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputTotalKVA.setUnits("0.1 kVA")
_StsOutputTotalKW_Type = Integer32
_StsOutputTotalKW_Object = MibScalar
stsOutputTotalKW = _StsOutputTotalKW_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 7),
    _StsOutputTotalKW_Type()
)
stsOutputTotalKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputTotalKW.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputTotalKW.setUnits("0.1 kW")


class _StsOutputNeturalLoad_Type(Integer32):
    """Custom type stsOutputNeturalLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsOutputNeturalLoad_Type.__name__ = "Integer32"
_StsOutputNeturalLoad_Object = MibScalar
stsOutputNeturalLoad = _StsOutputNeturalLoad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 8),
    _StsOutputNeturalLoad_Type()
)
stsOutputNeturalLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputNeturalLoad.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputNeturalLoad.setUnits("1 %")
_StsOutputKWH_Type = Integer32
_StsOutputKWH_Object = MibScalar
stsOutputKWH = _StsOutputKWH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 4, 9),
    _StsOutputKWH_Type()
)
stsOutputKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsOutputKWH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsOutputKWH.setUnits("0.1KWH")
_StsFanTable_Object = MibTable
stsFanTable = _StsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 5)
)
if mibBuilder.loadTexts:
    stsFanTable.setStatus("mandatory")
_StsFanEntry_Object = MibTableRow
stsFanEntry = _StsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 5, 1)
)
stsFanEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsFanIndex"),
)
if mibBuilder.loadTexts:
    stsFanEntry.setStatus("mandatory")


class _StsFans_Type(Integer32):
    """Custom type stsFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65281
        )
    )
    namedValues = NamedValues(
        ("invalid", 65281)
    )


_StsFans_Type.__name__ = "Integer32"
_StsFans_Object = MibTableColumn
stsFans = _StsFans_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 5, 1, 1),
    _StsFans_Type()
)
stsFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsFans.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsFans.setUnits("rpm")


class _StsFanIndex_Type(Integer32):
    """Custom type stsFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_StsFanIndex_Type.__name__ = "Integer32"
_StsFanIndex_Object = MibTableColumn
stsFanIndex = _StsFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 5, 1, 2),
    _StsFanIndex_Type()
)
stsFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsFanIndex.setStatus("mandatory")
_StsTemperature_ObjectIdentity = ObjectIdentity
stsTemperature = _StsTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6)
)
_StsTemperatureTable_Object = MibTable
stsTemperatureTable = _StsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1)
)
if mibBuilder.loadTexts:
    stsTemperatureTable.setStatus("mandatory")
_StsTemperatureEntry_Object = MibTableRow
stsTemperatureEntry = _StsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1)
)
stsTemperatureEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsTemperatureIndex"),
)
if mibBuilder.loadTexts:
    stsTemperatureEntry.setStatus("mandatory")
_StsTemperatureR1_Type = Integer32
_StsTemperatureR1_Object = MibTableColumn
stsTemperatureR1 = _StsTemperatureR1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 1),
    _StsTemperatureR1_Type()
)
stsTemperatureR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureR1.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureR1.setUnits("Degree")
_StsTemperatureS1_Type = Integer32
_StsTemperatureS1_Object = MibTableColumn
stsTemperatureS1 = _StsTemperatureS1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 2),
    _StsTemperatureS1_Type()
)
stsTemperatureS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureS1.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureS1.setUnits("Degree")
_StsTemperatureT1_Type = Integer32
_StsTemperatureT1_Object = MibTableColumn
stsTemperatureT1 = _StsTemperatureT1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 3),
    _StsTemperatureT1_Type()
)
stsTemperatureT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureT1.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureT1.setUnits("Degree")
_StsTemperatureN1_Type = Integer32
_StsTemperatureN1_Object = MibTableColumn
stsTemperatureN1 = _StsTemperatureN1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 4),
    _StsTemperatureN1_Type()
)
stsTemperatureN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureN1.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureN1.setUnits("Degree")
_StsTemperatureR2_Type = Integer32
_StsTemperatureR2_Object = MibTableColumn
stsTemperatureR2 = _StsTemperatureR2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 5),
    _StsTemperatureR2_Type()
)
stsTemperatureR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureR2.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureR2.setUnits("Degree")
_StsTemperatureS2_Type = Integer32
_StsTemperatureS2_Object = MibTableColumn
stsTemperatureS2 = _StsTemperatureS2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 6),
    _StsTemperatureS2_Type()
)
stsTemperatureS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureS2.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureS2.setUnits("Degree")
_StsTemperatureT2_Type = Integer32
_StsTemperatureT2_Object = MibTableColumn
stsTemperatureT2 = _StsTemperatureT2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 7),
    _StsTemperatureT2_Type()
)
stsTemperatureT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureT2.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureT2.setUnits("Degree")
_StsTemperatureN2_Type = Integer32
_StsTemperatureN2_Object = MibTableColumn
stsTemperatureN2 = _StsTemperatureN2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 8),
    _StsTemperatureN2_Type()
)
stsTemperatureN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureN2.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureN2.setUnits("Degree")


class _StsTemperatureIndex_Type(Integer32):
    """Custom type stsTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2))
    )


_StsTemperatureIndex_Type.__name__ = "Integer32"
_StsTemperatureIndex_Object = MibTableColumn
stsTemperatureIndex = _StsTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 1, 1, 9),
    _StsTemperatureIndex_Type()
)
stsTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureIndex.setStatus("mandatory")
_StsTemperatureAmbient_Type = Integer32
_StsTemperatureAmbient_Object = MibScalar
stsTemperatureAmbient = _StsTemperatureAmbient_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 6, 2),
    _StsTemperatureAmbient_Type()
)
stsTemperatureAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTemperatureAmbient.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsTemperatureAmbient.setUnits("Degree")
_StsStatistic_ObjectIdentity = ObjectIdentity
stsStatistic = _StsStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7)
)
_StsStatisticSource1Count_Type = Integer32
_StsStatisticSource1Count_Object = MibScalar
stsStatisticSource1Count = _StsStatisticSource1Count_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 1),
    _StsStatisticSource1Count_Type()
)
stsStatisticSource1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticSource1Count.setStatus("mandatory")
_StsStatisticSource2Count_Type = Integer32
_StsStatisticSource2Count_Object = MibScalar
stsStatisticSource2Count = _StsStatisticSource2Count_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 2),
    _StsStatisticSource2Count_Type()
)
stsStatisticSource2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticSource2Count.setStatus("mandatory")
_StsStatisticBypass1Count_Type = Integer32
_StsStatisticBypass1Count_Object = MibScalar
stsStatisticBypass1Count = _StsStatisticBypass1Count_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 3),
    _StsStatisticBypass1Count_Type()
)
stsStatisticBypass1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticBypass1Count.setStatus("mandatory")
_StsStatisticBypass2Count_Type = Integer32
_StsStatisticBypass2Count_Object = MibScalar
stsStatisticBypass2Count = _StsStatisticBypass2Count_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 4),
    _StsStatisticBypass2Count_Type()
)
stsStatisticBypass2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticBypass2Count.setStatus("mandatory")
_StsStatisticTransferCount_Type = Integer32
_StsStatisticTransferCount_Object = MibScalar
stsStatisticTransferCount = _StsStatisticTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 5),
    _StsStatisticTransferCount_Type()
)
stsStatisticTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticTransferCount.setStatus("mandatory")
_StsStatisticTimeTable_Object = MibTable
stsStatisticTimeTable = _StsStatisticTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 6)
)
if mibBuilder.loadTexts:
    stsStatisticTimeTable.setStatus("mandatory")
_StsStatisticTimeEntry_Object = MibTableRow
stsStatisticTimeEntry = _StsStatisticTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 6, 1)
)
stsStatisticTimeEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsStatisticIndex"),
)
if mibBuilder.loadTexts:
    stsStatisticTimeEntry.setStatus("mandatory")
_StsStatisticHours_Type = Integer32
_StsStatisticHours_Object = MibTableColumn
stsStatisticHours = _StsStatisticHours_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 6, 1, 1),
    _StsStatisticHours_Type()
)
stsStatisticHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticHours.setStatus("mandatory")
_StsStatisticMinutes_Type = Integer32
_StsStatisticMinutes_Object = MibTableColumn
stsStatisticMinutes = _StsStatisticMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 6, 1, 2),
    _StsStatisticMinutes_Type()
)
stsStatisticMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticMinutes.setStatus("mandatory")


class _StsStatisticIndex_Type(Integer32):
    """Custom type stsStatisticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source-1", 1),
          ("source-2", 2),
          ("all", 3))
    )


_StsStatisticIndex_Type.__name__ = "Integer32"
_StsStatisticIndex_Object = MibTableColumn
stsStatisticIndex = _StsStatisticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 7, 6, 1, 3),
    _StsStatisticIndex_Type()
)
stsStatisticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatisticIndex.setStatus("mandatory")
_StsStatus_ObjectIdentity = ObjectIdentity
stsStatus = _StsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8)
)
_StsStatusActiveCard_Type = Integer32
_StsStatusActiveCard_Object = MibScalar
stsStatusActiveCard = _StsStatusActiveCard_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 1),
    _StsStatusActiveCard_Type()
)
stsStatusActiveCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusActiveCard.setStatus("mandatory")
_StsStatusPowerFlow_ObjectIdentity = ObjectIdentity
stsStatusPowerFlow = _StsStatusPowerFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2)
)


class _StsStatusSource1_Type(Integer32):
    """Custom type stsStatusSource1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2),
          ("unkown", 3))
    )


_StsStatusSource1_Type.__name__ = "Integer32"
_StsStatusSource1_Object = MibScalar
stsStatusSource1 = _StsStatusSource1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 1),
    _StsStatusSource1_Type()
)
stsStatusSource1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusSource1.setStatus("mandatory")


class _StsStatusSource2_Type(Integer32):
    """Custom type stsStatusSource2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2),
          ("unkown", 3))
    )


_StsStatusSource2_Type.__name__ = "Integer32"
_StsStatusSource2_Object = MibScalar
stsStatusSource2 = _StsStatusSource2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 2),
    _StsStatusSource2_Type()
)
stsStatusSource2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusSource2.setStatus("mandatory")


class _StsStatusSource1MCCB_Type(Integer32):
    """Custom type stsStatusSource1MCCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusSource1MCCB_Type.__name__ = "Integer32"
_StsStatusSource1MCCB_Object = MibScalar
stsStatusSource1MCCB = _StsStatusSource1MCCB_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 3),
    _StsStatusSource1MCCB_Type()
)
stsStatusSource1MCCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusSource1MCCB.setStatus("mandatory")


class _StsStatusSource2MCCB_Type(Integer32):
    """Custom type stsStatusSource2MCCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusSource2MCCB_Type.__name__ = "Integer32"
_StsStatusSource2MCCB_Object = MibScalar
stsStatusSource2MCCB = _StsStatusSource2MCCB_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 4),
    _StsStatusSource2MCCB_Type()
)
stsStatusSource2MCCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusSource2MCCB.setStatus("mandatory")


class _StsStatusBypass1MCCB_Type(Integer32):
    """Custom type stsStatusBypass1MCCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusBypass1MCCB_Type.__name__ = "Integer32"
_StsStatusBypass1MCCB_Object = MibScalar
stsStatusBypass1MCCB = _StsStatusBypass1MCCB_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 5),
    _StsStatusBypass1MCCB_Type()
)
stsStatusBypass1MCCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusBypass1MCCB.setStatus("mandatory")


class _StsStatusBypass2MCCB_Type(Integer32):
    """Custom type stsStatusBypass2MCCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusBypass2MCCB_Type.__name__ = "Integer32"
_StsStatusBypass2MCCB_Object = MibScalar
stsStatusBypass2MCCB = _StsStatusBypass2MCCB_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 6),
    _StsStatusBypass2MCCB_Type()
)
stsStatusBypass2MCCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusBypass2MCCB.setStatus("mandatory")


class _StsStatusOutputMCCB1_Type(Integer32):
    """Custom type stsStatusOutputMCCB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cb-off", 1),
          ("cb-on", 2),
          ("not-exist", 3))
    )


_StsStatusOutputMCCB1_Type.__name__ = "Integer32"
_StsStatusOutputMCCB1_Object = MibScalar
stsStatusOutputMCCB1 = _StsStatusOutputMCCB1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 7),
    _StsStatusOutputMCCB1_Type()
)
stsStatusOutputMCCB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusOutputMCCB1.setStatus("mandatory")


class _StsStatusOutputMCCB2_Type(Integer32):
    """Custom type stsStatusOutputMCCB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cb-off", 1),
          ("cb-on", 2),
          ("not-exist", 3))
    )


_StsStatusOutputMCCB2_Type.__name__ = "Integer32"
_StsStatusOutputMCCB2_Object = MibScalar
stsStatusOutputMCCB2 = _StsStatusOutputMCCB2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 8),
    _StsStatusOutputMCCB2_Type()
)
stsStatusOutputMCCB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusOutputMCCB2.setStatus("mandatory")


class _StsStatusOutputMCCB3_Type(Integer32):
    """Custom type stsStatusOutputMCCB3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cb-off", 1),
          ("cb-on", 2),
          ("not-exist", 3))
    )


_StsStatusOutputMCCB3_Type.__name__ = "Integer32"
_StsStatusOutputMCCB3_Object = MibScalar
stsStatusOutputMCCB3 = _StsStatusOutputMCCB3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 9),
    _StsStatusOutputMCCB3_Type()
)
stsStatusOutputMCCB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusOutputMCCB3.setStatus("mandatory")


class _StsStatusSource1SCR_Type(Integer32):
    """Custom type stsStatusSource1SCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("fault", 3))
    )


_StsStatusSource1SCR_Type.__name__ = "Integer32"
_StsStatusSource1SCR_Object = MibScalar
stsStatusSource1SCR = _StsStatusSource1SCR_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 10),
    _StsStatusSource1SCR_Type()
)
stsStatusSource1SCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusSource1SCR.setStatus("mandatory")


class _StsStatusSource2SCR_Type(Integer32):
    """Custom type stsStatusSource2SCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("fault", 3))
    )


_StsStatusSource2SCR_Type.__name__ = "Integer32"
_StsStatusSource2SCR_Object = MibScalar
stsStatusSource2SCR = _StsStatusSource2SCR_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 11),
    _StsStatusSource2SCR_Type()
)
stsStatusSource2SCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusSource2SCR.setStatus("mandatory")


class _StsStatusLoadOnSource1_Type(Integer32):
    """Custom type stsStatusLoadOnSource1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusLoadOnSource1_Type.__name__ = "Integer32"
_StsStatusLoadOnSource1_Object = MibScalar
stsStatusLoadOnSource1 = _StsStatusLoadOnSource1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 12),
    _StsStatusLoadOnSource1_Type()
)
stsStatusLoadOnSource1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusLoadOnSource1.setStatus("mandatory")


class _StsStatusLoadOnSource2_Type(Integer32):
    """Custom type stsStatusLoadOnSource2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusLoadOnSource2_Type.__name__ = "Integer32"
_StsStatusLoadOnSource2_Object = MibScalar
stsStatusLoadOnSource2 = _StsStatusLoadOnSource2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 13),
    _StsStatusLoadOnSource2_Type()
)
stsStatusLoadOnSource2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusLoadOnSource2.setStatus("mandatory")


class _StsStatusLoadOnBypass1_Type(Integer32):
    """Custom type stsStatusLoadOnBypass1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusLoadOnBypass1_Type.__name__ = "Integer32"
_StsStatusLoadOnBypass1_Object = MibScalar
stsStatusLoadOnBypass1 = _StsStatusLoadOnBypass1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 14),
    _StsStatusLoadOnBypass1_Type()
)
stsStatusLoadOnBypass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusLoadOnBypass1.setStatus("mandatory")


class _StsStatusLoadOnBypass2_Type(Integer32):
    """Custom type stsStatusLoadOnBypass2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusLoadOnBypass2_Type.__name__ = "Integer32"
_StsStatusLoadOnBypass2_Object = MibScalar
stsStatusLoadOnBypass2 = _StsStatusLoadOnBypass2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 15),
    _StsStatusLoadOnBypass2_Type()
)
stsStatusLoadOnBypass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusLoadOnBypass2.setStatus("mandatory")


class _StsStatusLoad_Type(Integer32):
    """Custom type stsStatusLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2),
          ("unkown", 3))
    )


_StsStatusLoad_Type.__name__ = "Integer32"
_StsStatusLoad_Object = MibScalar
stsStatusLoad = _StsStatusLoad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 2, 16),
    _StsStatusLoad_Type()
)
stsStatusLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusLoad.setStatus("mandatory")
_StsStatusWarnSystemCode_Type = Integer32
_StsStatusWarnSystemCode_Object = MibScalar
stsStatusWarnSystemCode = _StsStatusWarnSystemCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 3),
    _StsStatusWarnSystemCode_Type()
)
stsStatusWarnSystemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSystemCode.setStatus("mandatory")
_StsStatusWarnSystem_ObjectIdentity = ObjectIdentity
stsStatusWarnSystem = _StsStatusWarnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4)
)


class _StsStatusWarnCard1MCU_Type(Integer32):
    """Custom type stsStatusWarnCard1MCU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnCard1MCU_Type.__name__ = "Integer32"
_StsStatusWarnCard1MCU_Object = MibScalar
stsStatusWarnCard1MCU = _StsStatusWarnCard1MCU_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 1),
    _StsStatusWarnCard1MCU_Type()
)
stsStatusWarnCard1MCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnCard1MCU.setStatus("mandatory")


class _StsStatusWarnCard2MCU_Type(Integer32):
    """Custom type stsStatusWarnCard2MCU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnCard2MCU_Type.__name__ = "Integer32"
_StsStatusWarnCard2MCU_Object = MibScalar
stsStatusWarnCard2MCU = _StsStatusWarnCard2MCU_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 2),
    _StsStatusWarnCard2MCU_Type()
)
stsStatusWarnCard2MCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnCard2MCU.setStatus("mandatory")


class _StsStatusWarnROM_Type(Integer32):
    """Custom type stsStatusWarnROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnROM_Type.__name__ = "Integer32"
_StsStatusWarnROM_Object = MibScalar
stsStatusWarnROM = _StsStatusWarnROM_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 3),
    _StsStatusWarnROM_Type()
)
stsStatusWarnROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnROM.setStatus("mandatory")


class _StsStatusWarnReplaceFilter_Type(Integer32):
    """Custom type stsStatusWarnReplaceFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnReplaceFilter_Type.__name__ = "Integer32"
_StsStatusWarnReplaceFilter_Object = MibScalar
stsStatusWarnReplaceFilter = _StsStatusWarnReplaceFilter_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 4),
    _StsStatusWarnReplaceFilter_Type()
)
stsStatusWarnReplaceFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnReplaceFilter.setStatus("mandatory")


class _StsStatusWarnComm_Type(Integer32):
    """Custom type stsStatusWarnComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnComm_Type.__name__ = "Integer32"
_StsStatusWarnComm_Object = MibScalar
stsStatusWarnComm = _StsStatusWarnComm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 5),
    _StsStatusWarnComm_Type()
)
stsStatusWarnComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnComm.setStatus("mandatory")


class _StsStatusWarnComm1_Type(Integer32):
    """Custom type stsStatusWarnComm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnComm1_Type.__name__ = "Integer32"
_StsStatusWarnComm1_Object = MibScalar
stsStatusWarnComm1 = _StsStatusWarnComm1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 6),
    _StsStatusWarnComm1_Type()
)
stsStatusWarnComm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnComm1.setStatus("mandatory")


class _StsStatusWarnComm2_Type(Integer32):
    """Custom type stsStatusWarnComm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnComm2_Type.__name__ = "Integer32"
_StsStatusWarnComm2_Object = MibScalar
stsStatusWarnComm2 = _StsStatusWarnComm2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 7),
    _StsStatusWarnComm2_Type()
)
stsStatusWarnComm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnComm2.setStatus("mandatory")


class _StsStatusWarnAuxPowerFuse_Type(Integer32):
    """Custom type stsStatusWarnAuxPowerFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnAuxPowerFuse_Type.__name__ = "Integer32"
_StsStatusWarnAuxPowerFuse_Object = MibScalar
stsStatusWarnAuxPowerFuse = _StsStatusWarnAuxPowerFuse_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 8),
    _StsStatusWarnAuxPowerFuse_Type()
)
stsStatusWarnAuxPowerFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnAuxPowerFuse.setStatus("mandatory")


class _StsStatusWarnAuxPowerCard_Type(Integer32):
    """Custom type stsStatusWarnAuxPowerCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnAuxPowerCard_Type.__name__ = "Integer32"
_StsStatusWarnAuxPowerCard_Object = MibScalar
stsStatusWarnAuxPowerCard = _StsStatusWarnAuxPowerCard_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 9),
    _StsStatusWarnAuxPowerCard_Type()
)
stsStatusWarnAuxPowerCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnAuxPowerCard.setStatus("mandatory")


class _StsStatusWarnAuxPowerFan_Type(Integer32):
    """Custom type stsStatusWarnAuxPowerFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnAuxPowerFan_Type.__name__ = "Integer32"
_StsStatusWarnAuxPowerFan_Object = MibScalar
stsStatusWarnAuxPowerFan = _StsStatusWarnAuxPowerFan_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 10),
    _StsStatusWarnAuxPowerFan_Type()
)
stsStatusWarnAuxPowerFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnAuxPowerFan.setStatus("mandatory")


class _StsStatusWarnEPO_Type(Integer32):
    """Custom type stsStatusWarnEPO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnEPO_Type.__name__ = "Integer32"
_StsStatusWarnEPO_Object = MibScalar
stsStatusWarnEPO = _StsStatusWarnEPO_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 11),
    _StsStatusWarnEPO_Type()
)
stsStatusWarnEPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnEPO.setStatus("mandatory")


class _StsStatusWarnBUZ_Type(Integer32):
    """Custom type stsStatusWarnBUZ based on Integer32"""
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
          ("serverity1", 2),
          ("serverity2", 3),
          ("serverity3", 4))
    )


_StsStatusWarnBUZ_Type.__name__ = "Integer32"
_StsStatusWarnBUZ_Object = MibScalar
stsStatusWarnBUZ = _StsStatusWarnBUZ_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 4, 12),
    _StsStatusWarnBUZ_Type()
)
stsStatusWarnBUZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnBUZ.setStatus("mandatory")
_StsStatusWarnRepairCode_Type = Integer32
_StsStatusWarnRepairCode_Object = MibScalar
stsStatusWarnRepairCode = _StsStatusWarnRepairCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 5),
    _StsStatusWarnRepairCode_Type()
)
stsStatusWarnRepairCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairCode.setStatus("mandatory")
_StsStatusWarnRepair_ObjectIdentity = ObjectIdentity
stsStatusWarnRepair = _StsStatusWarnRepair_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6)
)


class _StsStatusWarnRepairSTSCard1_Type(Integer32):
    """Custom type stsStatusWarnRepairSTSCard1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairSTSCard1_Type.__name__ = "Integer32"
_StsStatusWarnRepairSTSCard1_Object = MibScalar
stsStatusWarnRepairSTSCard1 = _StsStatusWarnRepairSTSCard1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 1),
    _StsStatusWarnRepairSTSCard1_Type()
)
stsStatusWarnRepairSTSCard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairSTSCard1.setStatus("mandatory")


class _StsStatusWarnRepairSTSCard2_Type(Integer32):
    """Custom type stsStatusWarnRepairSTSCard2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairSTSCard2_Type.__name__ = "Integer32"
_StsStatusWarnRepairSTSCard2_Object = MibScalar
stsStatusWarnRepairSTSCard2 = _StsStatusWarnRepairSTSCard2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 2),
    _StsStatusWarnRepairSTSCard2_Type()
)
stsStatusWarnRepairSTSCard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairSTSCard2.setStatus("mandatory")


class _StsStatusWarnRepairSTSModule1_Type(Integer32):
    """Custom type stsStatusWarnRepairSTSModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairSTSModule1_Type.__name__ = "Integer32"
_StsStatusWarnRepairSTSModule1_Object = MibScalar
stsStatusWarnRepairSTSModule1 = _StsStatusWarnRepairSTSModule1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 3),
    _StsStatusWarnRepairSTSModule1_Type()
)
stsStatusWarnRepairSTSModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairSTSModule1.setStatus("mandatory")


class _StsStatusWarnRepairSTSModule2_Type(Integer32):
    """Custom type stsStatusWarnRepairSTSModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairSTSModule2_Type.__name__ = "Integer32"
_StsStatusWarnRepairSTSModule2_Object = MibScalar
stsStatusWarnRepairSTSModule2 = _StsStatusWarnRepairSTSModule2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 4),
    _StsStatusWarnRepairSTSModule2_Type()
)
stsStatusWarnRepairSTSModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairSTSModule2.setStatus("mandatory")


class _StsStatusWarnRepairBreakerCard1_Type(Integer32):
    """Custom type stsStatusWarnRepairBreakerCard1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairBreakerCard1_Type.__name__ = "Integer32"
_StsStatusWarnRepairBreakerCard1_Object = MibScalar
stsStatusWarnRepairBreakerCard1 = _StsStatusWarnRepairBreakerCard1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 5),
    _StsStatusWarnRepairBreakerCard1_Type()
)
stsStatusWarnRepairBreakerCard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairBreakerCard1.setStatus("mandatory")


class _StsStatusWarnRepairAuxPowerCard1_Type(Integer32):
    """Custom type stsStatusWarnRepairAuxPowerCard1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairAuxPowerCard1_Type.__name__ = "Integer32"
_StsStatusWarnRepairAuxPowerCard1_Object = MibScalar
stsStatusWarnRepairAuxPowerCard1 = _StsStatusWarnRepairAuxPowerCard1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 6),
    _StsStatusWarnRepairAuxPowerCard1_Type()
)
stsStatusWarnRepairAuxPowerCard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairAuxPowerCard1.setStatus("mandatory")


class _StsStatusWarnRepairAuxPowerCard2_Type(Integer32):
    """Custom type stsStatusWarnRepairAuxPowerCard2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairAuxPowerCard2_Type.__name__ = "Integer32"
_StsStatusWarnRepairAuxPowerCard2_Object = MibScalar
stsStatusWarnRepairAuxPowerCard2 = _StsStatusWarnRepairAuxPowerCard2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 7),
    _StsStatusWarnRepairAuxPowerCard2_Type()
)
stsStatusWarnRepairAuxPowerCard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairAuxPowerCard2.setStatus("mandatory")


class _StsStatusWarnRepairAuxPowerCard3_Type(Integer32):
    """Custom type stsStatusWarnRepairAuxPowerCard3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRepairAuxPowerCard3_Type.__name__ = "Integer32"
_StsStatusWarnRepairAuxPowerCard3_Object = MibScalar
stsStatusWarnRepairAuxPowerCard3 = _StsStatusWarnRepairAuxPowerCard3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 6, 8),
    _StsStatusWarnRepairAuxPowerCard3_Type()
)
stsStatusWarnRepairAuxPowerCard3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRepairAuxPowerCard3.setStatus("mandatory")
_StsStatusWarnIOCode_Type = Integer32
_StsStatusWarnIOCode_Object = MibScalar
stsStatusWarnIOCode = _StsStatusWarnIOCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 7),
    _StsStatusWarnIOCode_Type()
)
stsStatusWarnIOCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnIOCode.setStatus("mandatory")
_StsStatusWarnIO_ObjectIdentity = ObjectIdentity
stsStatusWarnIO = _StsStatusWarnIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8)
)


class _StsStatusWarnSource1Fail_Type(Integer32):
    """Custom type stsStatusWarnSource1Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1Fail_Type.__name__ = "Integer32"
_StsStatusWarnSource1Fail_Object = MibScalar
stsStatusWarnSource1Fail = _StsStatusWarnSource1Fail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 1),
    _StsStatusWarnSource1Fail_Type()
)
stsStatusWarnSource1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1Fail.setStatus("mandatory")


class _StsStatusWarnSource1VoltAbnormal_Type(Integer32):
    """Custom type stsStatusWarnSource1VoltAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1VoltAbnormal_Type.__name__ = "Integer32"
_StsStatusWarnSource1VoltAbnormal_Object = MibScalar
stsStatusWarnSource1VoltAbnormal = _StsStatusWarnSource1VoltAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 2),
    _StsStatusWarnSource1VoltAbnormal_Type()
)
stsStatusWarnSource1VoltAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1VoltAbnormal.setStatus("mandatory")


class _StsStatusWarnSource1OverVolt_Type(Integer32):
    """Custom type stsStatusWarnSource1OverVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1OverVolt_Type.__name__ = "Integer32"
_StsStatusWarnSource1OverVolt_Object = MibScalar
stsStatusWarnSource1OverVolt = _StsStatusWarnSource1OverVolt_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 3),
    _StsStatusWarnSource1OverVolt_Type()
)
stsStatusWarnSource1OverVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1OverVolt.setStatus("mandatory")


class _StsStatusWarnSource1UnderVolt_Type(Integer32):
    """Custom type stsStatusWarnSource1UnderVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1UnderVolt_Type.__name__ = "Integer32"
_StsStatusWarnSource1UnderVolt_Object = MibScalar
stsStatusWarnSource1UnderVolt = _StsStatusWarnSource1UnderVolt_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 4),
    _StsStatusWarnSource1UnderVolt_Type()
)
stsStatusWarnSource1UnderVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1UnderVolt.setStatus("mandatory")


class _StsStatusWarnSource1FreqOutRange_Type(Integer32):
    """Custom type stsStatusWarnSource1FreqOutRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1FreqOutRange_Type.__name__ = "Integer32"
_StsStatusWarnSource1FreqOutRange_Object = MibScalar
stsStatusWarnSource1FreqOutRange = _StsStatusWarnSource1FreqOutRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 5),
    _StsStatusWarnSource1FreqOutRange_Type()
)
stsStatusWarnSource1FreqOutRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1FreqOutRange.setStatus("mandatory")


class _StsStatusWarnSource1PhaseSequence_Type(Integer32):
    """Custom type stsStatusWarnSource1PhaseSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1PhaseSequence_Type.__name__ = "Integer32"
_StsStatusWarnSource1PhaseSequence_Object = MibScalar
stsStatusWarnSource1PhaseSequence = _StsStatusWarnSource1PhaseSequence_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 6),
    _StsStatusWarnSource1PhaseSequence_Type()
)
stsStatusWarnSource1PhaseSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1PhaseSequence.setStatus("mandatory")


class _StsStatusWarnSource1BreakerTrip_Type(Integer32):
    """Custom type stsStatusWarnSource1BreakerTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1BreakerTrip_Type.__name__ = "Integer32"
_StsStatusWarnSource1BreakerTrip_Object = MibScalar
stsStatusWarnSource1BreakerTrip = _StsStatusWarnSource1BreakerTrip_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 7),
    _StsStatusWarnSource1BreakerTrip_Type()
)
stsStatusWarnSource1BreakerTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1BreakerTrip.setStatus("mandatory")


class _StsStatusWarnSource1Overload_Type(Integer32):
    """Custom type stsStatusWarnSource1Overload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1Overload_Type.__name__ = "Integer32"
_StsStatusWarnSource1Overload_Object = MibScalar
stsStatusWarnSource1Overload = _StsStatusWarnSource1Overload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 8),
    _StsStatusWarnSource1Overload_Type()
)
stsStatusWarnSource1Overload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1Overload.setStatus("mandatory")


class _StsStatusWarnSource2Fail_Type(Integer32):
    """Custom type stsStatusWarnSource2Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2Fail_Type.__name__ = "Integer32"
_StsStatusWarnSource2Fail_Object = MibScalar
stsStatusWarnSource2Fail = _StsStatusWarnSource2Fail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 9),
    _StsStatusWarnSource2Fail_Type()
)
stsStatusWarnSource2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2Fail.setStatus("mandatory")


class _StsStatusWarnSource2VoltAbnormal_Type(Integer32):
    """Custom type stsStatusWarnSource2VoltAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2VoltAbnormal_Type.__name__ = "Integer32"
_StsStatusWarnSource2VoltAbnormal_Object = MibScalar
stsStatusWarnSource2VoltAbnormal = _StsStatusWarnSource2VoltAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 10),
    _StsStatusWarnSource2VoltAbnormal_Type()
)
stsStatusWarnSource2VoltAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2VoltAbnormal.setStatus("mandatory")


class _StsStatusWarnSource2OverVolt_Type(Integer32):
    """Custom type stsStatusWarnSource2OverVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2OverVolt_Type.__name__ = "Integer32"
_StsStatusWarnSource2OverVolt_Object = MibScalar
stsStatusWarnSource2OverVolt = _StsStatusWarnSource2OverVolt_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 11),
    _StsStatusWarnSource2OverVolt_Type()
)
stsStatusWarnSource2OverVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2OverVolt.setStatus("mandatory")


class _StsStatusWarnSource2UnderVolt_Type(Integer32):
    """Custom type stsStatusWarnSource2UnderVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2UnderVolt_Type.__name__ = "Integer32"
_StsStatusWarnSource2UnderVolt_Object = MibScalar
stsStatusWarnSource2UnderVolt = _StsStatusWarnSource2UnderVolt_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 12),
    _StsStatusWarnSource2UnderVolt_Type()
)
stsStatusWarnSource2UnderVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2UnderVolt.setStatus("mandatory")


class _StsStatusWarnSource2FreqOutRange_Type(Integer32):
    """Custom type stsStatusWarnSource2FreqOutRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2FreqOutRange_Type.__name__ = "Integer32"
_StsStatusWarnSource2FreqOutRange_Object = MibScalar
stsStatusWarnSource2FreqOutRange = _StsStatusWarnSource2FreqOutRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 13),
    _StsStatusWarnSource2FreqOutRange_Type()
)
stsStatusWarnSource2FreqOutRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2FreqOutRange.setStatus("mandatory")


class _StsStatusWarnSource2PhaseSequence_Type(Integer32):
    """Custom type stsStatusWarnSource2PhaseSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2PhaseSequence_Type.__name__ = "Integer32"
_StsStatusWarnSource2PhaseSequence_Object = MibScalar
stsStatusWarnSource2PhaseSequence = _StsStatusWarnSource2PhaseSequence_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 14),
    _StsStatusWarnSource2PhaseSequence_Type()
)
stsStatusWarnSource2PhaseSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2PhaseSequence.setStatus("mandatory")


class _StsStatusWarnSource2BreakerTrip_Type(Integer32):
    """Custom type stsStatusWarnSource2BreakerTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2BreakerTrip_Type.__name__ = "Integer32"
_StsStatusWarnSource2BreakerTrip_Object = MibScalar
stsStatusWarnSource2BreakerTrip = _StsStatusWarnSource2BreakerTrip_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 15),
    _StsStatusWarnSource2BreakerTrip_Type()
)
stsStatusWarnSource2BreakerTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2BreakerTrip.setStatus("mandatory")


class _StsStatusWarnSource2Overload_Type(Integer32):
    """Custom type stsStatusWarnSource2Overload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2Overload_Type.__name__ = "Integer32"
_StsStatusWarnSource2Overload_Object = MibScalar
stsStatusWarnSource2Overload = _StsStatusWarnSource2Overload_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 16),
    _StsStatusWarnSource2Overload_Type()
)
stsStatusWarnSource2Overload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2Overload.setStatus("mandatory")


class _StsStatusWarnOutputOverLoad_Type(Integer32):
    """Custom type stsStatusWarnOutputOverLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnOutputOverLoad_Type.__name__ = "Integer32"
_StsStatusWarnOutputOverLoad_Object = MibScalar
stsStatusWarnOutputOverLoad = _StsStatusWarnOutputOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 17),
    _StsStatusWarnOutputOverLoad_Type()
)
stsStatusWarnOutputOverLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnOutputOverLoad.setStatus("mandatory")


class _StsStatusWarnOutputShortCircuit_Type(Integer32):
    """Custom type stsStatusWarnOutputShortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnOutputShortCircuit_Type.__name__ = "Integer32"
_StsStatusWarnOutputShortCircuit_Object = MibScalar
stsStatusWarnOutputShortCircuit = _StsStatusWarnOutputShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 18),
    _StsStatusWarnOutputShortCircuit_Type()
)
stsStatusWarnOutputShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnOutputShortCircuit.setStatus("mandatory")


class _StsStatusWarnPF_Type(Integer32):
    """Custom type stsStatusWarnPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnPF_Type.__name__ = "Integer32"
_StsStatusWarnPF_Object = MibScalar
stsStatusWarnPF = _StsStatusWarnPF_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 19),
    _StsStatusWarnPF_Type()
)
stsStatusWarnPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnPF.setStatus("mandatory")


class _StsStatusWarnCF_Type(Integer32):
    """Custom type stsStatusWarnCF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnCF_Type.__name__ = "Integer32"
_StsStatusWarnCF_Object = MibScalar
stsStatusWarnCF = _StsStatusWarnCF_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 20),
    _StsStatusWarnCF_Type()
)
stsStatusWarnCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnCF.setStatus("mandatory")


class _StsStatusWarnTransInhibited_Type(Integer32):
    """Custom type stsStatusWarnTransInhibited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTransInhibited_Type.__name__ = "Integer32"
_StsStatusWarnTransInhibited_Object = MibScalar
stsStatusWarnTransInhibited = _StsStatusWarnTransInhibited_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 21),
    _StsStatusWarnTransInhibited_Type()
)
stsStatusWarnTransInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTransInhibited.setStatus("mandatory")


class _StsStatusWarnRetransferFail_Type(Integer32):
    """Custom type stsStatusWarnRetransferFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnRetransferFail_Type.__name__ = "Integer32"
_StsStatusWarnRetransferFail_Object = MibScalar
stsStatusWarnRetransferFail = _StsStatusWarnRetransferFail_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 22),
    _StsStatusWarnRetransferFail_Type()
)
stsStatusWarnRetransferFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnRetransferFail.setStatus("mandatory")


class _StsStatusWarnInputSourceAsync_Type(Integer32):
    """Custom type stsStatusWarnInputSourceAsync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnInputSourceAsync_Type.__name__ = "Integer32"
_StsStatusWarnInputSourceAsync_Object = MibScalar
stsStatusWarnInputSourceAsync = _StsStatusWarnInputSourceAsync_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 23),
    _StsStatusWarnInputSourceAsync_Type()
)
stsStatusWarnInputSourceAsync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnInputSourceAsync.setStatus("mandatory")


class _StsStatusWarnOutputVoltAbnormal_Type(Integer32):
    """Custom type stsStatusWarnOutputVoltAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnOutputVoltAbnormal_Type.__name__ = "Integer32"
_StsStatusWarnOutputVoltAbnormal_Object = MibScalar
stsStatusWarnOutputVoltAbnormal = _StsStatusWarnOutputVoltAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 24),
    _StsStatusWarnOutputVoltAbnormal_Type()
)
stsStatusWarnOutputVoltAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnOutputVoltAbnormal.setStatus("mandatory")


class _StsStatusWarnSource1IPeakOver_Type(Integer32):
    """Custom type stsStatusWarnSource1IPeakOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource1IPeakOver_Type.__name__ = "Integer32"
_StsStatusWarnSource1IPeakOver_Object = MibScalar
stsStatusWarnSource1IPeakOver = _StsStatusWarnSource1IPeakOver_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 25),
    _StsStatusWarnSource1IPeakOver_Type()
)
stsStatusWarnSource1IPeakOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource1IPeakOver.setStatus("mandatory")


class _StsStatusWarnSource2IPeakOver_Type(Integer32):
    """Custom type stsStatusWarnSource2IPeakOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSource2IPeakOver_Type.__name__ = "Integer32"
_StsStatusWarnSource2IPeakOver_Object = MibScalar
stsStatusWarnSource2IPeakOver = _StsStatusWarnSource2IPeakOver_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 8, 26),
    _StsStatusWarnSource2IPeakOver_Type()
)
stsStatusWarnSource2IPeakOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSource2IPeakOver.setStatus("mandatory")
_StsStatusWarnTemperatureCode_Type = Integer32
_StsStatusWarnTemperatureCode_Object = MibScalar
stsStatusWarnTemperatureCode = _StsStatusWarnTemperatureCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 9),
    _StsStatusWarnTemperatureCode_Type()
)
stsStatusWarnTemperatureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTemperatureCode.setStatus("mandatory")
_StsStatusWarnTemperature_ObjectIdentity = ObjectIdentity
stsStatusWarnTemperature = _StsStatusWarnTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10)
)


class _StsStatusWarnTempSource1R1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1R1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1R1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1R1OH_Object = MibScalar
stsStatusWarnTempSource1R1OH = _StsStatusWarnTempSource1R1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 1),
    _StsStatusWarnTempSource1R1OH_Type()
)
stsStatusWarnTempSource1R1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1R1OH.setStatus("mandatory")


class _StsStatusWarnTempSource1S1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1S1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1S1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1S1OH_Object = MibScalar
stsStatusWarnTempSource1S1OH = _StsStatusWarnTempSource1S1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 2),
    _StsStatusWarnTempSource1S1OH_Type()
)
stsStatusWarnTempSource1S1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1S1OH.setStatus("mandatory")


class _StsStatusWarnTempSource1T1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1T1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1T1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1T1OH_Object = MibScalar
stsStatusWarnTempSource1T1OH = _StsStatusWarnTempSource1T1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 3),
    _StsStatusWarnTempSource1T1OH_Type()
)
stsStatusWarnTempSource1T1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1T1OH.setStatus("mandatory")


class _StsStatusWarnTempSource1N1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1N1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1N1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1N1OH_Object = MibScalar
stsStatusWarnTempSource1N1OH = _StsStatusWarnTempSource1N1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 4),
    _StsStatusWarnTempSource1N1OH_Type()
)
stsStatusWarnTempSource1N1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1N1OH.setStatus("mandatory")


class _StsStatusWarnTempSource1R2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1R2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1R2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1R2OH_Object = MibScalar
stsStatusWarnTempSource1R2OH = _StsStatusWarnTempSource1R2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 5),
    _StsStatusWarnTempSource1R2OH_Type()
)
stsStatusWarnTempSource1R2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1R2OH.setStatus("mandatory")


class _StsStatusWarnTempSource1S2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1S2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1S2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1S2OH_Object = MibScalar
stsStatusWarnTempSource1S2OH = _StsStatusWarnTempSource1S2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 6),
    _StsStatusWarnTempSource1S2OH_Type()
)
stsStatusWarnTempSource1S2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1S2OH.setStatus("mandatory")


class _StsStatusWarnTempSource1T2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1T2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1T2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1T2OH_Object = MibScalar
stsStatusWarnTempSource1T2OH = _StsStatusWarnTempSource1T2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 7),
    _StsStatusWarnTempSource1T2OH_Type()
)
stsStatusWarnTempSource1T2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1T2OH.setStatus("mandatory")


class _StsStatusWarnTempSource1N2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource1N2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1N2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1N2OH_Object = MibScalar
stsStatusWarnTempSource1N2OH = _StsStatusWarnTempSource1N2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 8),
    _StsStatusWarnTempSource1N2OH_Type()
)
stsStatusWarnTempSource1N2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1N2OH.setStatus("mandatory")


class _StsStatusWarnTempSource2R1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2R1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2R1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2R1OH_Object = MibScalar
stsStatusWarnTempSource2R1OH = _StsStatusWarnTempSource2R1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 9),
    _StsStatusWarnTempSource2R1OH_Type()
)
stsStatusWarnTempSource2R1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2R1OH.setStatus("mandatory")


class _StsStatusWarnTempSource2S1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2S1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2S1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2S1OH_Object = MibScalar
stsStatusWarnTempSource2S1OH = _StsStatusWarnTempSource2S1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 10),
    _StsStatusWarnTempSource2S1OH_Type()
)
stsStatusWarnTempSource2S1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2S1OH.setStatus("mandatory")


class _StsStatusWarnTempSource2T1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2T1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2T1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2T1OH_Object = MibScalar
stsStatusWarnTempSource2T1OH = _StsStatusWarnTempSource2T1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 11),
    _StsStatusWarnTempSource2T1OH_Type()
)
stsStatusWarnTempSource2T1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2T1OH.setStatus("mandatory")


class _StsStatusWarnTempSource2N1OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2N1OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2N1OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2N1OH_Object = MibScalar
stsStatusWarnTempSource2N1OH = _StsStatusWarnTempSource2N1OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 12),
    _StsStatusWarnTempSource2N1OH_Type()
)
stsStatusWarnTempSource2N1OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2N1OH.setStatus("mandatory")


class _StsStatusWarnTempSource2R2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2R2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2R2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2R2OH_Object = MibScalar
stsStatusWarnTempSource2R2OH = _StsStatusWarnTempSource2R2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 13),
    _StsStatusWarnTempSource2R2OH_Type()
)
stsStatusWarnTempSource2R2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2R2OH.setStatus("mandatory")


class _StsStatusWarnTempSource2S2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2S2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2S2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2S2OH_Object = MibScalar
stsStatusWarnTempSource2S2OH = _StsStatusWarnTempSource2S2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 14),
    _StsStatusWarnTempSource2S2OH_Type()
)
stsStatusWarnTempSource2S2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2S2OH.setStatus("mandatory")


class _StsStatusWarnTempSource2T2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2T2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2T2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2T2OH_Object = MibScalar
stsStatusWarnTempSource2T2OH = _StsStatusWarnTempSource2T2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 15),
    _StsStatusWarnTempSource2T2OH_Type()
)
stsStatusWarnTempSource2T2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2T2OH.setStatus("mandatory")


class _StsStatusWarnTempSource2N2OH_Type(Integer32):
    """Custom type stsStatusWarnTempSource2N2OH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2N2OH_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2N2OH_Object = MibScalar
stsStatusWarnTempSource2N2OH = _StsStatusWarnTempSource2N2OH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 16),
    _StsStatusWarnTempSource2N2OH_Type()
)
stsStatusWarnTempSource2N2OH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2N2OH.setStatus("mandatory")


class _StsStatusWarnTempSource1R1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1R1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1R1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1R1OHSD_Object = MibScalar
stsStatusWarnTempSource1R1OHSD = _StsStatusWarnTempSource1R1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 17),
    _StsStatusWarnTempSource1R1OHSD_Type()
)
stsStatusWarnTempSource1R1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1R1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1S1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1S1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1S1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1S1OHSD_Object = MibScalar
stsStatusWarnTempSource1S1OHSD = _StsStatusWarnTempSource1S1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 18),
    _StsStatusWarnTempSource1S1OHSD_Type()
)
stsStatusWarnTempSource1S1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1S1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1T1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1T1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1T1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1T1OHSD_Object = MibScalar
stsStatusWarnTempSource1T1OHSD = _StsStatusWarnTempSource1T1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 19),
    _StsStatusWarnTempSource1T1OHSD_Type()
)
stsStatusWarnTempSource1T1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1T1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1N1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1N1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1N1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1N1OHSD_Object = MibScalar
stsStatusWarnTempSource1N1OHSD = _StsStatusWarnTempSource1N1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 20),
    _StsStatusWarnTempSource1N1OHSD_Type()
)
stsStatusWarnTempSource1N1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1N1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1R2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1R2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1R2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1R2OHSD_Object = MibScalar
stsStatusWarnTempSource1R2OHSD = _StsStatusWarnTempSource1R2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 21),
    _StsStatusWarnTempSource1R2OHSD_Type()
)
stsStatusWarnTempSource1R2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1R2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1S2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1S2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1S2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1S2OHSD_Object = MibScalar
stsStatusWarnTempSource1S2OHSD = _StsStatusWarnTempSource1S2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 22),
    _StsStatusWarnTempSource1S2OHSD_Type()
)
stsStatusWarnTempSource1S2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1S2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1T2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1T2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1T2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1T2OHSD_Object = MibScalar
stsStatusWarnTempSource1T2OHSD = _StsStatusWarnTempSource1T2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 23),
    _StsStatusWarnTempSource1T2OHSD_Type()
)
stsStatusWarnTempSource1T2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1T2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource1N2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource1N2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource1N2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource1N2OHSD_Object = MibScalar
stsStatusWarnTempSource1N2OHSD = _StsStatusWarnTempSource1N2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 24),
    _StsStatusWarnTempSource1N2OHSD_Type()
)
stsStatusWarnTempSource1N2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource1N2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2R1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2R1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2R1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2R1OHSD_Object = MibScalar
stsStatusWarnTempSource2R1OHSD = _StsStatusWarnTempSource2R1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 25),
    _StsStatusWarnTempSource2R1OHSD_Type()
)
stsStatusWarnTempSource2R1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2R1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2S1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2S1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2S1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2S1OHSD_Object = MibScalar
stsStatusWarnTempSource2S1OHSD = _StsStatusWarnTempSource2S1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 26),
    _StsStatusWarnTempSource2S1OHSD_Type()
)
stsStatusWarnTempSource2S1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2S1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2T1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2T1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2T1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2T1OHSD_Object = MibScalar
stsStatusWarnTempSource2T1OHSD = _StsStatusWarnTempSource2T1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 27),
    _StsStatusWarnTempSource2T1OHSD_Type()
)
stsStatusWarnTempSource2T1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2T1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2N1OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2N1OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2N1OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2N1OHSD_Object = MibScalar
stsStatusWarnTempSource2N1OHSD = _StsStatusWarnTempSource2N1OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 28),
    _StsStatusWarnTempSource2N1OHSD_Type()
)
stsStatusWarnTempSource2N1OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2N1OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2R2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2R2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2R2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2R2OHSD_Object = MibScalar
stsStatusWarnTempSource2R2OHSD = _StsStatusWarnTempSource2R2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 29),
    _StsStatusWarnTempSource2R2OHSD_Type()
)
stsStatusWarnTempSource2R2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2R2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2S2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2S2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2S2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2S2OHSD_Object = MibScalar
stsStatusWarnTempSource2S2OHSD = _StsStatusWarnTempSource2S2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 30),
    _StsStatusWarnTempSource2S2OHSD_Type()
)
stsStatusWarnTempSource2S2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2S2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2T2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2T2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2T2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2T2OHSD_Object = MibScalar
stsStatusWarnTempSource2T2OHSD = _StsStatusWarnTempSource2T2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 31),
    _StsStatusWarnTempSource2T2OHSD_Type()
)
stsStatusWarnTempSource2T2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2T2OHSD.setStatus("mandatory")


class _StsStatusWarnTempSource2N2OHSD_Type(Integer32):
    """Custom type stsStatusWarnTempSource2N2OHSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnTempSource2N2OHSD_Type.__name__ = "Integer32"
_StsStatusWarnTempSource2N2OHSD_Object = MibScalar
stsStatusWarnTempSource2N2OHSD = _StsStatusWarnTempSource2N2OHSD_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 10, 32),
    _StsStatusWarnTempSource2N2OHSD_Type()
)
stsStatusWarnTempSource2N2OHSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnTempSource2N2OHSD.setStatus("mandatory")
_StsStatusWarnNTCCode_Type = Integer32
_StsStatusWarnNTCCode_Object = MibScalar
stsStatusWarnNTCCode = _StsStatusWarnNTCCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 11),
    _StsStatusWarnNTCCode_Type()
)
stsStatusWarnNTCCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCCode.setStatus("mandatory")
_StsStatusWarnNTC_ObjectIdentity = ObjectIdentity
stsStatusWarnNTC = _StsStatusWarnNTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12)
)


class _StsStatusWarnNTCAmbient_Type(Integer32):
    """Custom type stsStatusWarnNTCAmbient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCAmbient_Type.__name__ = "Integer32"
_StsStatusWarnNTCAmbient_Object = MibScalar
stsStatusWarnNTCAmbient = _StsStatusWarnNTCAmbient_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 1),
    _StsStatusWarnNTCAmbient_Type()
)
stsStatusWarnNTCAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCAmbient.setStatus("mandatory")


class _StsStatusWarnNTCSource1R1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1R1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1R1_Object = MibScalar
stsStatusWarnNTCSource1R1 = _StsStatusWarnNTCSource1R1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 2),
    _StsStatusWarnNTCSource1R1_Type()
)
stsStatusWarnNTCSource1R1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1R1.setStatus("mandatory")


class _StsStatusWarnNTCSource1S1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1S1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1S1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1S1_Object = MibScalar
stsStatusWarnNTCSource1S1 = _StsStatusWarnNTCSource1S1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 3),
    _StsStatusWarnNTCSource1S1_Type()
)
stsStatusWarnNTCSource1S1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1S1.setStatus("mandatory")


class _StsStatusWarnNTCSource1T1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1T1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1T1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1T1_Object = MibScalar
stsStatusWarnNTCSource1T1 = _StsStatusWarnNTCSource1T1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 4),
    _StsStatusWarnNTCSource1T1_Type()
)
stsStatusWarnNTCSource1T1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1T1.setStatus("mandatory")


class _StsStatusWarnNTCSource1N1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1N1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1N1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1N1_Object = MibScalar
stsStatusWarnNTCSource1N1 = _StsStatusWarnNTCSource1N1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 5),
    _StsStatusWarnNTCSource1N1_Type()
)
stsStatusWarnNTCSource1N1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1N1.setStatus("mandatory")


class _StsStatusWarnNTCSource1R2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1R2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1R2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1R2_Object = MibScalar
stsStatusWarnNTCSource1R2 = _StsStatusWarnNTCSource1R2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 6),
    _StsStatusWarnNTCSource1R2_Type()
)
stsStatusWarnNTCSource1R2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1R2.setStatus("mandatory")


class _StsStatusWarnNTCSource1S2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1S2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1S2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1S2_Object = MibScalar
stsStatusWarnNTCSource1S2 = _StsStatusWarnNTCSource1S2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 7),
    _StsStatusWarnNTCSource1S2_Type()
)
stsStatusWarnNTCSource1S2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1S2.setStatus("mandatory")


class _StsStatusWarnNTCSource1T2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1T2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1T2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1T2_Object = MibScalar
stsStatusWarnNTCSource1T2 = _StsStatusWarnNTCSource1T2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 8),
    _StsStatusWarnNTCSource1T2_Type()
)
stsStatusWarnNTCSource1T2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1T2.setStatus("mandatory")


class _StsStatusWarnNTCSource1N2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource1N2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource1N2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource1N2_Object = MibScalar
stsStatusWarnNTCSource1N2 = _StsStatusWarnNTCSource1N2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 9),
    _StsStatusWarnNTCSource1N2_Type()
)
stsStatusWarnNTCSource1N2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource1N2.setStatus("mandatory")


class _StsStatusWarnNTCSource2R1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2R1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2R1_Object = MibScalar
stsStatusWarnNTCSource2R1 = _StsStatusWarnNTCSource2R1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 10),
    _StsStatusWarnNTCSource2R1_Type()
)
stsStatusWarnNTCSource2R1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2R1.setStatus("mandatory")


class _StsStatusWarnNTCSource2S1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2S1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2S1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2S1_Object = MibScalar
stsStatusWarnNTCSource2S1 = _StsStatusWarnNTCSource2S1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 11),
    _StsStatusWarnNTCSource2S1_Type()
)
stsStatusWarnNTCSource2S1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2S1.setStatus("mandatory")


class _StsStatusWarnNTCSource2T1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2T1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2T1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2T1_Object = MibScalar
stsStatusWarnNTCSource2T1 = _StsStatusWarnNTCSource2T1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 12),
    _StsStatusWarnNTCSource2T1_Type()
)
stsStatusWarnNTCSource2T1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2T1.setStatus("mandatory")


class _StsStatusWarnNTCSource2N1_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2N1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2N1_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2N1_Object = MibScalar
stsStatusWarnNTCSource2N1 = _StsStatusWarnNTCSource2N1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 13),
    _StsStatusWarnNTCSource2N1_Type()
)
stsStatusWarnNTCSource2N1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2N1.setStatus("mandatory")


class _StsStatusWarnNTCSource2R2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2R2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2R2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2R2_Object = MibScalar
stsStatusWarnNTCSource2R2 = _StsStatusWarnNTCSource2R2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 14),
    _StsStatusWarnNTCSource2R2_Type()
)
stsStatusWarnNTCSource2R2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2R2.setStatus("mandatory")


class _StsStatusWarnNTCSource2S2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2S2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2S2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2S2_Object = MibScalar
stsStatusWarnNTCSource2S2 = _StsStatusWarnNTCSource2S2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 15),
    _StsStatusWarnNTCSource2S2_Type()
)
stsStatusWarnNTCSource2S2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2S2.setStatus("mandatory")


class _StsStatusWarnNTCSource2T2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2T2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2T2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2T2_Object = MibScalar
stsStatusWarnNTCSource2T2 = _StsStatusWarnNTCSource2T2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 16),
    _StsStatusWarnNTCSource2T2_Type()
)
stsStatusWarnNTCSource2T2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2T2.setStatus("mandatory")


class _StsStatusWarnNTCSource2N2_Type(Integer32):
    """Custom type stsStatusWarnNTCSource2N2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnNTCSource2N2_Type.__name__ = "Integer32"
_StsStatusWarnNTCSource2N2_Object = MibScalar
stsStatusWarnNTCSource2N2 = _StsStatusWarnNTCSource2N2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 12, 17),
    _StsStatusWarnNTCSource2N2_Type()
)
stsStatusWarnNTCSource2N2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnNTCSource2N2.setStatus("mandatory")
_StsStatusWarnFanCode1_Type = Integer32
_StsStatusWarnFanCode1_Object = MibScalar
stsStatusWarnFanCode1 = _StsStatusWarnFanCode1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 13),
    _StsStatusWarnFanCode1_Type()
)
stsStatusWarnFanCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnFanCode1.setStatus("mandatory")
_StsStatusWarnFanCode2_Type = Integer32
_StsStatusWarnFanCode2_Object = MibScalar
stsStatusWarnFanCode2 = _StsStatusWarnFanCode2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 14),
    _StsStatusWarnFanCode2_Type()
)
stsStatusWarnFanCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnFanCode2.setStatus("mandatory")
_StsStatusWarnFan_ObjectIdentity = ObjectIdentity
stsStatusWarnFan = _StsStatusWarnFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 15)
)
_StsStatusWarnFanTable_Object = MibTable
stsStatusWarnFanTable = _StsStatusWarnFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 15, 1)
)
if mibBuilder.loadTexts:
    stsStatusWarnFanTable.setStatus("mandatory")
_StsStatusWarnFanEntry_Object = MibTableRow
stsStatusWarnFanEntry = _StsStatusWarnFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 15, 1, 1)
)
stsStatusWarnFanEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsStatusWarnFanIndex"),
)
if mibBuilder.loadTexts:
    stsStatusWarnFanEntry.setStatus("mandatory")


class _StsStatusWarnFans_Type(Integer32):
    """Custom type stsStatusWarnFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnFans_Type.__name__ = "Integer32"
_StsStatusWarnFans_Object = MibTableColumn
stsStatusWarnFans = _StsStatusWarnFans_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 15, 1, 1, 1),
    _StsStatusWarnFans_Type()
)
stsStatusWarnFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnFans.setStatus("mandatory")


class _StsStatusWarnFanIndex_Type(Integer32):
    """Custom type stsStatusWarnFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_StsStatusWarnFanIndex_Type.__name__ = "Integer32"
_StsStatusWarnFanIndex_Object = MibTableColumn
stsStatusWarnFanIndex = _StsStatusWarnFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 15, 1, 1, 2),
    _StsStatusWarnFanIndex_Type()
)
stsStatusWarnFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnFanIndex.setStatus("mandatory")
_StsStatusWarnSCRCode_Type = Integer32
_StsStatusWarnSCRCode_Object = MibScalar
stsStatusWarnSCRCode = _StsStatusWarnSCRCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 16),
    _StsStatusWarnSCRCode_Type()
)
stsStatusWarnSCRCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRCode.setStatus("mandatory")
_StsStatusWarnSCR_ObjectIdentity = ObjectIdentity
stsStatusWarnSCR = _StsStatusWarnSCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17)
)
_StsStatusWarnSCRTable_Object = MibTable
stsStatusWarnSCRTable = _StsStatusWarnSCRTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1)
)
if mibBuilder.loadTexts:
    stsStatusWarnSCRTable.setStatus("mandatory")
_StsStatusWarnSCREntry_Object = MibTableRow
stsStatusWarnSCREntry = _StsStatusWarnSCREntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1)
)
stsStatusWarnSCREntry.setIndexNames(
    (0, "DeltaSTS-MIB", "stsStatusWarnSCRIndex"),
)
if mibBuilder.loadTexts:
    stsStatusWarnSCREntry.setStatus("mandatory")


class _StsStatusWarnSCRS1Open_Type(Integer32):
    """Custom type stsStatusWarnSCRS1Open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSCRS1Open_Type.__name__ = "Integer32"
_StsStatusWarnSCRS1Open_Object = MibTableColumn
stsStatusWarnSCRS1Open = _StsStatusWarnSCRS1Open_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 1),
    _StsStatusWarnSCRS1Open_Type()
)
stsStatusWarnSCRS1Open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRS1Open.setStatus("mandatory")


class _StsStatusWarnSCRS1ShortOff_Type(Integer32):
    """Custom type stsStatusWarnSCRS1ShortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSCRS1ShortOff_Type.__name__ = "Integer32"
_StsStatusWarnSCRS1ShortOff_Object = MibTableColumn
stsStatusWarnSCRS1ShortOff = _StsStatusWarnSCRS1ShortOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 2),
    _StsStatusWarnSCRS1ShortOff_Type()
)
stsStatusWarnSCRS1ShortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRS1ShortOff.setStatus("mandatory")


class _StsStatusWarnSCRS1ShortOn_Type(Integer32):
    """Custom type stsStatusWarnSCRS1ShortOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSCRS1ShortOn_Type.__name__ = "Integer32"
_StsStatusWarnSCRS1ShortOn_Object = MibTableColumn
stsStatusWarnSCRS1ShortOn = _StsStatusWarnSCRS1ShortOn_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 3),
    _StsStatusWarnSCRS1ShortOn_Type()
)
stsStatusWarnSCRS1ShortOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRS1ShortOn.setStatus("mandatory")


class _StsStatusWarnSCRS2Open_Type(Integer32):
    """Custom type stsStatusWarnSCRS2Open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSCRS2Open_Type.__name__ = "Integer32"
_StsStatusWarnSCRS2Open_Object = MibTableColumn
stsStatusWarnSCRS2Open = _StsStatusWarnSCRS2Open_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 4),
    _StsStatusWarnSCRS2Open_Type()
)
stsStatusWarnSCRS2Open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRS2Open.setStatus("mandatory")


class _StsStatusWarnSCRS2ShortOff_Type(Integer32):
    """Custom type stsStatusWarnSCRS2ShortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSCRS2ShortOff_Type.__name__ = "Integer32"
_StsStatusWarnSCRS2ShortOff_Object = MibTableColumn
stsStatusWarnSCRS2ShortOff = _StsStatusWarnSCRS2ShortOff_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 5),
    _StsStatusWarnSCRS2ShortOff_Type()
)
stsStatusWarnSCRS2ShortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRS2ShortOff.setStatus("mandatory")


class _StsStatusWarnSCRS2ShortOn_Type(Integer32):
    """Custom type stsStatusWarnSCRS2ShortOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StsStatusWarnSCRS2ShortOn_Type.__name__ = "Integer32"
_StsStatusWarnSCRS2ShortOn_Object = MibTableColumn
stsStatusWarnSCRS2ShortOn = _StsStatusWarnSCRS2ShortOn_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 6),
    _StsStatusWarnSCRS2ShortOn_Type()
)
stsStatusWarnSCRS2ShortOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRS2ShortOn.setStatus("mandatory")


class _StsStatusWarnSCRIndex_Type(Integer32):
    """Custom type stsStatusWarnSCRIndex based on Integer32"""
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
        *(("phase-1", 1),
          ("phase-2", 2),
          ("phase-3", 3),
          ("phase-N", 4))
    )


_StsStatusWarnSCRIndex_Type.__name__ = "Integer32"
_StsStatusWarnSCRIndex_Object = MibTableColumn
stsStatusWarnSCRIndex = _StsStatusWarnSCRIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 8, 17, 1, 1, 7),
    _StsStatusWarnSCRIndex_Type()
)
stsStatusWarnSCRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsStatusWarnSCRIndex.setStatus("mandatory")
_StsConfig_ObjectIdentity = ObjectIdentity
stsConfig = _StsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9)
)
_StsConfigSys_ObjectIdentity = ObjectIdentity
stsConfigSys = _StsConfigSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 1)
)
_StsConfigSysVoltRating_Type = Integer32
_StsConfigSysVoltRating_Object = MibScalar
stsConfigSysVoltRating = _StsConfigSysVoltRating_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 1, 1),
    _StsConfigSysVoltRating_Type()
)
stsConfigSysVoltRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigSysVoltRating.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigSysVoltRating.setUnits("1V")
_StsConfigSysFreqRating_Type = Integer32
_StsConfigSysFreqRating_Object = MibScalar
stsConfigSysFreqRating = _StsConfigSysFreqRating_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 1, 2),
    _StsConfigSysFreqRating_Type()
)
stsConfigSysFreqRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigSysFreqRating.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigSysFreqRating.setUnits("1Hz")
_StsConfigSysCurrentRating_Type = Integer32
_StsConfigSysCurrentRating_Object = MibScalar
stsConfigSysCurrentRating = _StsConfigSysCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 1, 3),
    _StsConfigSysCurrentRating_Type()
)
stsConfigSysCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigSysCurrentRating.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigSysCurrentRating.setUnits("1A")
_StsConfigSysTemperatureUnit_Type = Integer32
_StsConfigSysTemperatureUnit_Object = MibScalar
stsConfigSysTemperatureUnit = _StsConfigSysTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 1, 4),
    _StsConfigSysTemperatureUnit_Type()
)
stsConfigSysTemperatureUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigSysTemperatureUnit.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigSysTemperatureUnit.setUnits("Degree")
_StsConfigInput_ObjectIdentity = ObjectIdentity
stsConfigInput = _StsConfigInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2)
)


class _StsConfigInputPreferredSource_Type(Integer32):
    """Custom type stsConfigInputPreferredSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2))
    )


_StsConfigInputPreferredSource_Type.__name__ = "Integer32"
_StsConfigInputPreferredSource_Object = MibScalar
stsConfigInputPreferredSource = _StsConfigInputPreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 1),
    _StsConfigInputPreferredSource_Type()
)
stsConfigInputPreferredSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputPreferredSource.setStatus("mandatory")
_StsConfigInputPhaseSyncRangeH_Type = Integer32
_StsConfigInputPhaseSyncRangeH_Object = MibScalar
stsConfigInputPhaseSyncRangeH = _StsConfigInputPhaseSyncRangeH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 2),
    _StsConfigInputPhaseSyncRangeH_Type()
)
stsConfigInputPhaseSyncRangeH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigInputPhaseSyncRangeH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputPhaseSyncRangeH.setUnits("Degree")
_StsConfigInputPhaseSyncRangeL_Type = Integer32
_StsConfigInputPhaseSyncRangeL_Object = MibScalar
stsConfigInputPhaseSyncRangeL = _StsConfigInputPhaseSyncRangeL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 3),
    _StsConfigInputPhaseSyncRangeL_Type()
)
stsConfigInputPhaseSyncRangeL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigInputPhaseSyncRangeL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputPhaseSyncRangeL.setUnits("Degree")
_StsConfigInputPhaseSyncRange_Type = Integer32
_StsConfigInputPhaseSyncRange_Object = MibScalar
stsConfigInputPhaseSyncRange = _StsConfigInputPhaseSyncRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 4),
    _StsConfigInputPhaseSyncRange_Type()
)
stsConfigInputPhaseSyncRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputPhaseSyncRange.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputPhaseSyncRange.setUnits("Degree")
_StsConfigInputAsyncTranRangeH_Type = Integer32
_StsConfigInputAsyncTranRangeH_Object = MibScalar
stsConfigInputAsyncTranRangeH = _StsConfigInputAsyncTranRangeH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 5),
    _StsConfigInputAsyncTranRangeH_Type()
)
stsConfigInputAsyncTranRangeH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigInputAsyncTranRangeH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputAsyncTranRangeH.setUnits("0.5AC")
_StsConfigInputAsyncTranRangeL_Type = Integer32
_StsConfigInputAsyncTranRangeL_Object = MibScalar
stsConfigInputAsyncTranRangeL = _StsConfigInputAsyncTranRangeL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 6),
    _StsConfigInputAsyncTranRangeL_Type()
)
stsConfigInputAsyncTranRangeL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigInputAsyncTranRangeL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputAsyncTranRangeL.setUnits("0.5AC")
_StsConfigInputAsyncTranRange_Type = Integer32
_StsConfigInputAsyncTranRange_Object = MibScalar
stsConfigInputAsyncTranRange = _StsConfigInputAsyncTranRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 7),
    _StsConfigInputAsyncTranRange_Type()
)
stsConfigInputAsyncTranRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputAsyncTranRange.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputAsyncTranRange.setUnits("0.5AC")
_StsConfigInputSource1VoltRnageH_Type = Integer32
_StsConfigInputSource1VoltRnageH_Object = MibScalar
stsConfigInputSource1VoltRnageH = _StsConfigInputSource1VoltRnageH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 8),
    _StsConfigInputSource1VoltRnageH_Type()
)
stsConfigInputSource1VoltRnageH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource1VoltRnageH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource1VoltRnageH.setUnits("%")
_StsConfigInputSource1VoltRnageL_Type = Integer32
_StsConfigInputSource1VoltRnageL_Object = MibScalar
stsConfigInputSource1VoltRnageL = _StsConfigInputSource1VoltRnageL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 9),
    _StsConfigInputSource1VoltRnageL_Type()
)
stsConfigInputSource1VoltRnageL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource1VoltRnageL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource1VoltRnageL.setUnits("%")
_StsConfigInputSource2VoltRnageH_Type = Integer32
_StsConfigInputSource2VoltRnageH_Object = MibScalar
stsConfigInputSource2VoltRnageH = _StsConfigInputSource2VoltRnageH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 10),
    _StsConfigInputSource2VoltRnageH_Type()
)
stsConfigInputSource2VoltRnageH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource2VoltRnageH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource2VoltRnageH.setUnits("%")
_StsConfigInputSource2VoltRnageL_Type = Integer32
_StsConfigInputSource2VoltRnageL_Object = MibScalar
stsConfigInputSource2VoltRnageL = _StsConfigInputSource2VoltRnageL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 11),
    _StsConfigInputSource2VoltRnageL_Type()
)
stsConfigInputSource2VoltRnageL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource2VoltRnageL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource2VoltRnageL.setUnits("%")
_StsConfigInputSource1FreqRangeH_Type = Integer32
_StsConfigInputSource1FreqRangeH_Object = MibScalar
stsConfigInputSource1FreqRangeH = _StsConfigInputSource1FreqRangeH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 12),
    _StsConfigInputSource1FreqRangeH_Type()
)
stsConfigInputSource1FreqRangeH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource1FreqRangeH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource1FreqRangeH.setUnits("0.1Hz")
_StsConfigInputSource1FreqRangeL_Type = Integer32
_StsConfigInputSource1FreqRangeL_Object = MibScalar
stsConfigInputSource1FreqRangeL = _StsConfigInputSource1FreqRangeL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 13),
    _StsConfigInputSource1FreqRangeL_Type()
)
stsConfigInputSource1FreqRangeL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource1FreqRangeL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource1FreqRangeL.setUnits("0.1Hz")
_StsConfigInputSource2FreqRangeH_Type = Integer32
_StsConfigInputSource2FreqRangeH_Object = MibScalar
stsConfigInputSource2FreqRangeH = _StsConfigInputSource2FreqRangeH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 14),
    _StsConfigInputSource2FreqRangeH_Type()
)
stsConfigInputSource2FreqRangeH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource2FreqRangeH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource2FreqRangeH.setUnits("0.1Hz")
_StsConfigInputSource2FreqRangeL_Type = Integer32
_StsConfigInputSource2FreqRangeL_Object = MibScalar
stsConfigInputSource2FreqRangeL = _StsConfigInputSource2FreqRangeL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 2, 15),
    _StsConfigInputSource2FreqRangeL_Type()
)
stsConfigInputSource2FreqRangeL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputSource2FreqRangeL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigInputSource2FreqRangeL.setUnits("0.1Hz")
_StsConfigControl_ObjectIdentity = ObjectIdentity
stsConfigControl = _StsConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3)
)


class _StsConfigTransferMode_Type(Integer32):
    """Custom type stsConfigTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_StsConfigTransferMode_Type.__name__ = "Integer32"
_StsConfigTransferMode_Object = MibScalar
stsConfigTransferMode = _StsConfigTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 1),
    _StsConfigTransferMode_Type()
)
stsConfigTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigTransferMode.setStatus("mandatory")


class _StsConfigRetransfer_Type(Integer32):
    """Custom type stsConfigRetransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StsConfigRetransfer_Type.__name__ = "Integer32"
_StsConfigRetransfer_Object = MibScalar
stsConfigRetransfer = _StsConfigRetransfer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 2),
    _StsConfigRetransfer_Type()
)
stsConfigRetransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigRetransfer.setStatus("mandatory")
_StsConfigTransferDelayRangeH_Type = Integer32
_StsConfigTransferDelayRangeH_Object = MibScalar
stsConfigTransferDelayRangeH = _StsConfigTransferDelayRangeH_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 3),
    _StsConfigTransferDelayRangeH_Type()
)
stsConfigTransferDelayRangeH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigTransferDelayRangeH.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigTransferDelayRangeH.setUnits("1 Sec")
_StsConfigTransferDelayRangeL_Type = Integer32
_StsConfigTransferDelayRangeL_Object = MibScalar
stsConfigTransferDelayRangeL = _StsConfigTransferDelayRangeL_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 4),
    _StsConfigTransferDelayRangeL_Type()
)
stsConfigTransferDelayRangeL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsConfigTransferDelayRangeL.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigTransferDelayRangeL.setUnits("1 Sec")
_StsConfigTransferDelayRange_Type = Integer32
_StsConfigTransferDelayRange_Object = MibScalar
stsConfigTransferDelayRange = _StsConfigTransferDelayRange_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 5),
    _StsConfigTransferDelayRange_Type()
)
stsConfigTransferDelayRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigTransferDelayRange.setStatus("mandatory")
if mibBuilder.loadTexts:
    stsConfigTransferDelayRange.setUnits("1 Sec")


class _StsConfigBuzzer_Type(Integer32):
    """Custom type stsConfigBuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StsConfigBuzzer_Type.__name__ = "Integer32"
_StsConfigBuzzer_Object = MibScalar
stsConfigBuzzer = _StsConfigBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 6),
    _StsConfigBuzzer_Type()
)
stsConfigBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigBuzzer.setStatus("mandatory")
_StsConfigClearSTS1EventLog_Type = Integer32
_StsConfigClearSTS1EventLog_Object = MibScalar
stsConfigClearSTS1EventLog = _StsConfigClearSTS1EventLog_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 7),
    _StsConfigClearSTS1EventLog_Type()
)
stsConfigClearSTS1EventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigClearSTS1EventLog.setStatus("mandatory")
_StsConfigClearSTS2EventLog_Type = Integer32
_StsConfigClearSTS2EventLog_Object = MibScalar
stsConfigClearSTS2EventLog = _StsConfigClearSTS2EventLog_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 8),
    _StsConfigClearSTS2EventLog_Type()
)
stsConfigClearSTS2EventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigClearSTS2EventLog.setStatus("mandatory")
_StsConfigClearStatistic_Type = Integer32
_StsConfigClearStatistic_Object = MibScalar
stsConfigClearStatistic = _StsConfigClearStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 3, 9),
    _StsConfigClearStatistic_Type()
)
stsConfigClearStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigClearStatistic.setStatus("mandatory")
_StsConfigDryContact_ObjectIdentity = ObjectIdentity
stsConfigDryContact = _StsConfigDryContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4)
)


class _StsConfigInputDryContEvent1_Type(Integer32):
    """Custom type stsConfigInputDryContEvent1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dummy", 1)
    )


_StsConfigInputDryContEvent1_Type.__name__ = "Integer32"
_StsConfigInputDryContEvent1_Object = MibScalar
stsConfigInputDryContEvent1 = _StsConfigInputDryContEvent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 1),
    _StsConfigInputDryContEvent1_Type()
)
stsConfigInputDryContEvent1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContEvent1.setStatus("mandatory")


class _StsConfigInputDryContEvent2_Type(Integer32):
    """Custom type stsConfigInputDryContEvent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dummy", 1)
    )


_StsConfigInputDryContEvent2_Type.__name__ = "Integer32"
_StsConfigInputDryContEvent2_Object = MibScalar
stsConfigInputDryContEvent2 = _StsConfigInputDryContEvent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 2),
    _StsConfigInputDryContEvent2_Type()
)
stsConfigInputDryContEvent2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContEvent2.setStatus("mandatory")


class _StsConfigInputDryContEvent3_Type(Integer32):
    """Custom type stsConfigInputDryContEvent3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dummy", 1)
    )


_StsConfigInputDryContEvent3_Type.__name__ = "Integer32"
_StsConfigInputDryContEvent3_Object = MibScalar
stsConfigInputDryContEvent3 = _StsConfigInputDryContEvent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 3),
    _StsConfigInputDryContEvent3_Type()
)
stsConfigInputDryContEvent3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContEvent3.setStatus("mandatory")


class _StsConfigInputDryContEvent4_Type(Integer32):
    """Custom type stsConfigInputDryContEvent4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dummy", 1)
    )


_StsConfigInputDryContEvent4_Type.__name__ = "Integer32"
_StsConfigInputDryContEvent4_Object = MibScalar
stsConfigInputDryContEvent4 = _StsConfigInputDryContEvent4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 4),
    _StsConfigInputDryContEvent4_Type()
)
stsConfigInputDryContEvent4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContEvent4.setStatus("mandatory")


class _StsConfigInputDryContType1_Type(Integer32):
    """Custom type stsConfigInputDryContType1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigInputDryContType1_Type.__name__ = "Integer32"
_StsConfigInputDryContType1_Object = MibScalar
stsConfigInputDryContType1 = _StsConfigInputDryContType1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 5),
    _StsConfigInputDryContType1_Type()
)
stsConfigInputDryContType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContType1.setStatus("mandatory")


class _StsConfigInputDryContType2_Type(Integer32):
    """Custom type stsConfigInputDryContType2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigInputDryContType2_Type.__name__ = "Integer32"
_StsConfigInputDryContType2_Object = MibScalar
stsConfigInputDryContType2 = _StsConfigInputDryContType2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 6),
    _StsConfigInputDryContType2_Type()
)
stsConfigInputDryContType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContType2.setStatus("mandatory")


class _StsConfigInputDryContType3_Type(Integer32):
    """Custom type stsConfigInputDryContType3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigInputDryContType3_Type.__name__ = "Integer32"
_StsConfigInputDryContType3_Object = MibScalar
stsConfigInputDryContType3 = _StsConfigInputDryContType3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 7),
    _StsConfigInputDryContType3_Type()
)
stsConfigInputDryContType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContType3.setStatus("mandatory")


class _StsConfigInputDryContType4_Type(Integer32):
    """Custom type stsConfigInputDryContType4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigInputDryContType4_Type.__name__ = "Integer32"
_StsConfigInputDryContType4_Object = MibScalar
stsConfigInputDryContType4 = _StsConfigInputDryContType4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 8),
    _StsConfigInputDryContType4_Type()
)
stsConfigInputDryContType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigInputDryContType4.setStatus("mandatory")


class _StsConfigOutputDryContEvent1_Type(Integer32):
    """Custom type stsConfigOutputDryContEvent1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("on-preferred-source", 2),
          ("on-alternate-source", 3),
          ("on-source-1", 4),
          ("on-source-2", 5),
          ("on-manual-bypass-1", 6),
          ("on-manual-bypass-2", 7),
          ("source-1-abnormal", 8),
          ("source-2-abnormal", 9),
          ("sts-1-over-temp", 10),
          ("sts-2-over-temp", 11),
          ("sts-1-abnormal", 12),
          ("sts-2-abnormal", 13),
          ("mcu-abnormal", 14),
          ("inner-com-abnormal", 15),
          ("epo-active", 16),
          ("overload", 17),
          ("source1-source2-phase-async", 18),
          ("summary-alarm", 19))
    )


_StsConfigOutputDryContEvent1_Type.__name__ = "Integer32"
_StsConfigOutputDryContEvent1_Object = MibScalar
stsConfigOutputDryContEvent1 = _StsConfigOutputDryContEvent1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 9),
    _StsConfigOutputDryContEvent1_Type()
)
stsConfigOutputDryContEvent1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContEvent1.setStatus("mandatory")


class _StsConfigOutputDryContEvent2_Type(Integer32):
    """Custom type stsConfigOutputDryContEvent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("on-preferred-source", 2),
          ("on-alternate-source", 3),
          ("on-source-1", 4),
          ("on-source-2", 5),
          ("on-manual-bypass-1", 6),
          ("on-manual-bypass-2", 7),
          ("source-1-abnormal", 8),
          ("source-2-abnormal", 9),
          ("sts-1-over-temp", 10),
          ("sts-2-over-temp", 11),
          ("sts-1-abnormal", 12),
          ("sts-2-abnormal", 13),
          ("mcu-abnormal", 14),
          ("inner-com-abnormal", 15),
          ("epo-active", 16),
          ("overload", 17),
          ("source1-source2-phase-async", 18),
          ("summary-alarm", 19))
    )


_StsConfigOutputDryContEvent2_Type.__name__ = "Integer32"
_StsConfigOutputDryContEvent2_Object = MibScalar
stsConfigOutputDryContEvent2 = _StsConfigOutputDryContEvent2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 10),
    _StsConfigOutputDryContEvent2_Type()
)
stsConfigOutputDryContEvent2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContEvent2.setStatus("mandatory")


class _StsConfigOutputDryContEvent3_Type(Integer32):
    """Custom type stsConfigOutputDryContEvent3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("on-preferred-source", 2),
          ("on-alternate-source", 3),
          ("on-source-1", 4),
          ("on-source-2", 5),
          ("on-manual-bypass-1", 6),
          ("on-manual-bypass-2", 7),
          ("source-1-abnormal", 8),
          ("source-2-abnormal", 9),
          ("sts-1-over-temp", 10),
          ("sts-2-over-temp", 11),
          ("sts-1-abnormal", 12),
          ("sts-2-abnormal", 13),
          ("mcu-abnormal", 14),
          ("inner-com-abnormal", 15),
          ("epo-active", 16),
          ("overload", 17),
          ("source1-source2-phase-async", 18),
          ("summary-alarm", 19))
    )


_StsConfigOutputDryContEvent3_Type.__name__ = "Integer32"
_StsConfigOutputDryContEvent3_Object = MibScalar
stsConfigOutputDryContEvent3 = _StsConfigOutputDryContEvent3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 11),
    _StsConfigOutputDryContEvent3_Type()
)
stsConfigOutputDryContEvent3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContEvent3.setStatus("mandatory")


class _StsConfigOutputDryContEvent4_Type(Integer32):
    """Custom type stsConfigOutputDryContEvent4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("on-preferred-source", 2),
          ("on-alternate-source", 3),
          ("on-source-1", 4),
          ("on-source-2", 5),
          ("on-manual-bypass-1", 6),
          ("on-manual-bypass-2", 7),
          ("source-1-abnormal", 8),
          ("source-2-abnormal", 9),
          ("sts-1-over-temp", 10),
          ("sts-2-over-temp", 11),
          ("sts-1-abnormal", 12),
          ("sts-2-abnormal", 13),
          ("mcu-abnormal", 14),
          ("inner-com-abnormal", 15),
          ("epo-active", 16),
          ("overload", 17),
          ("source1-source2-phase-async", 18),
          ("summary-alarm", 19))
    )


_StsConfigOutputDryContEvent4_Type.__name__ = "Integer32"
_StsConfigOutputDryContEvent4_Object = MibScalar
stsConfigOutputDryContEvent4 = _StsConfigOutputDryContEvent4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 12),
    _StsConfigOutputDryContEvent4_Type()
)
stsConfigOutputDryContEvent4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContEvent4.setStatus("mandatory")


class _StsConfigOutputDryContEvent5_Type(Integer32):
    """Custom type stsConfigOutputDryContEvent5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("on-preferred-source", 2),
          ("on-alternate-source", 3),
          ("on-source-1", 4),
          ("on-source-2", 5),
          ("on-manual-bypass-1", 6),
          ("on-manual-bypass-2", 7),
          ("source-1-abnormal", 8),
          ("source-2-abnormal", 9),
          ("sts-1-over-temp", 10),
          ("sts-2-over-temp", 11),
          ("sts-1-abnormal", 12),
          ("sts-2-abnormal", 13),
          ("mcu-abnormal", 14),
          ("inner-com-abnormal", 15),
          ("epo-active", 16),
          ("overload", 17),
          ("source1-source2-phase-async", 18),
          ("summary-alarm", 19))
    )


_StsConfigOutputDryContEvent5_Type.__name__ = "Integer32"
_StsConfigOutputDryContEvent5_Object = MibScalar
stsConfigOutputDryContEvent5 = _StsConfigOutputDryContEvent5_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 13),
    _StsConfigOutputDryContEvent5_Type()
)
stsConfigOutputDryContEvent5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContEvent5.setStatus("mandatory")


class _StsConfigOutputDryContEvent6_Type(Integer32):
    """Custom type stsConfigOutputDryContEvent6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("on-preferred-source", 2),
          ("on-alternate-source", 3),
          ("on-source-1", 4),
          ("on-source-2", 5),
          ("on-manual-bypass-1", 6),
          ("on-manual-bypass-2", 7),
          ("source-1-abnormal", 8),
          ("source-2-abnormal", 9),
          ("sts-1-over-temp", 10),
          ("sts-2-over-temp", 11),
          ("sts-1-abnormal", 12),
          ("sts-2-abnormal", 13),
          ("mcu-abnormal", 14),
          ("inner-com-abnormal", 15),
          ("epo-active", 16),
          ("overload", 17),
          ("source1-source2-phase-async", 18),
          ("summary-alarm", 19))
    )


_StsConfigOutputDryContEvent6_Type.__name__ = "Integer32"
_StsConfigOutputDryContEvent6_Object = MibScalar
stsConfigOutputDryContEvent6 = _StsConfigOutputDryContEvent6_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 14),
    _StsConfigOutputDryContEvent6_Type()
)
stsConfigOutputDryContEvent6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContEvent6.setStatus("mandatory")


class _StsConfigOutputDryContType1_Type(Integer32):
    """Custom type stsConfigOutputDryContType1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigOutputDryContType1_Type.__name__ = "Integer32"
_StsConfigOutputDryContType1_Object = MibScalar
stsConfigOutputDryContType1 = _StsConfigOutputDryContType1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 15),
    _StsConfigOutputDryContType1_Type()
)
stsConfigOutputDryContType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContType1.setStatus("mandatory")


class _StsConfigOutputDryContType2_Type(Integer32):
    """Custom type stsConfigOutputDryContType2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigOutputDryContType2_Type.__name__ = "Integer32"
_StsConfigOutputDryContType2_Object = MibScalar
stsConfigOutputDryContType2 = _StsConfigOutputDryContType2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 16),
    _StsConfigOutputDryContType2_Type()
)
stsConfigOutputDryContType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContType2.setStatus("mandatory")


class _StsConfigOutputDryContType3_Type(Integer32):
    """Custom type stsConfigOutputDryContType3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigOutputDryContType3_Type.__name__ = "Integer32"
_StsConfigOutputDryContType3_Object = MibScalar
stsConfigOutputDryContType3 = _StsConfigOutputDryContType3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 17),
    _StsConfigOutputDryContType3_Type()
)
stsConfigOutputDryContType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContType3.setStatus("mandatory")


class _StsConfigOutputDryContType4_Type(Integer32):
    """Custom type stsConfigOutputDryContType4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigOutputDryContType4_Type.__name__ = "Integer32"
_StsConfigOutputDryContType4_Object = MibScalar
stsConfigOutputDryContType4 = _StsConfigOutputDryContType4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 18),
    _StsConfigOutputDryContType4_Type()
)
stsConfigOutputDryContType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContType4.setStatus("mandatory")


class _StsConfigOutputDryContType5_Type(Integer32):
    """Custom type stsConfigOutputDryContType5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigOutputDryContType5_Type.__name__ = "Integer32"
_StsConfigOutputDryContType5_Object = MibScalar
stsConfigOutputDryContType5 = _StsConfigOutputDryContType5_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 19),
    _StsConfigOutputDryContType5_Type()
)
stsConfigOutputDryContType5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContType5.setStatus("mandatory")


class _StsConfigOutputDryContType6_Type(Integer32):
    """Custom type stsConfigOutputDryContType6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomally-close", 1),
          ("nomally-open", 2))
    )


_StsConfigOutputDryContType6_Type.__name__ = "Integer32"
_StsConfigOutputDryContType6_Object = MibScalar
stsConfigOutputDryContType6 = _StsConfigOutputDryContType6_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 4, 20),
    _StsConfigOutputDryContType6_Type()
)
stsConfigOutputDryContType6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigOutputDryContType6.setStatus("mandatory")
_StsConfigLocal_ObjectIdentity = ObjectIdentity
stsConfigLocal = _StsConfigLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 5)
)


class _StsConfigFormat_Type(Integer32):
    """Custom type stsConfigFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("date-M-D-Y", 1),
          ("date-Y-M-D", 2),
          ("date-D-M-Y", 3))
    )


_StsConfigFormat_Type.__name__ = "Integer32"
_StsConfigFormat_Object = MibScalar
stsConfigFormat = _StsConfigFormat_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 5, 1),
    _StsConfigFormat_Type()
)
stsConfigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigFormat.setStatus("mandatory")
_StsConfigLCDContrast_Type = Integer32
_StsConfigLCDContrast_Object = MibScalar
stsConfigLCDContrast = _StsConfigLCDContrast_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 5, 2),
    _StsConfigLCDContrast_Type()
)
stsConfigLCDContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigLCDContrast.setStatus("mandatory")


class _StsConfigLCDSleep_Type(Integer32):
    """Custom type stsConfigLCDSleep based on Integer32"""
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
        *(("min-1", 1),
          ("min-3", 2),
          ("min-5", 3),
          ("never", 4))
    )


_StsConfigLCDSleep_Type.__name__ = "Integer32"
_StsConfigLCDSleep_Object = MibScalar
stsConfigLCDSleep = _StsConfigLCDSleep_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 9, 5, 3),
    _StsConfigLCDSleep_Type()
)
stsConfigLCDSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsConfigLCDSleep.setStatus("mandatory")
_StsLog_ObjectIdentity = ObjectIdentity
stsLog = _StsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10)
)
_Sts1LogNum_Type = Integer32
_Sts1LogNum_Object = MibScalar
sts1LogNum = _Sts1LogNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 1),
    _Sts1LogNum_Type()
)
sts1LogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogNum.setStatus("mandatory")
_Sts1LogTable_Object = MibTable
sts1LogTable = _Sts1LogTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2)
)
if mibBuilder.loadTexts:
    sts1LogTable.setStatus("mandatory")
_Sts1LogEntry_Object = MibTableRow
sts1LogEntry = _Sts1LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1)
)
sts1LogEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "sts1LogIndex"),
)
if mibBuilder.loadTexts:
    sts1LogEntry.setStatus("mandatory")


class _Sts1LogIndex_Type(Integer32):
    """Custom type sts1LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Sts1LogIndex_Type.__name__ = "Integer32"
_Sts1LogIndex_Object = MibTableColumn
sts1LogIndex = _Sts1LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1, 1),
    _Sts1LogIndex_Type()
)
sts1LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogIndex.setStatus("mandatory")


class _Sts1LogDate_Type(DisplayString):
    """Custom type sts1LogDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Sts1LogDate_Type.__name__ = "DisplayString"
_Sts1LogDate_Object = MibTableColumn
sts1LogDate = _Sts1LogDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1, 2),
    _Sts1LogDate_Type()
)
sts1LogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogDate.setStatus("mandatory")
_Sts1LogMainCode_Type = Integer32
_Sts1LogMainCode_Object = MibTableColumn
sts1LogMainCode = _Sts1LogMainCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1, 3),
    _Sts1LogMainCode_Type()
)
sts1LogMainCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogMainCode.setStatus("mandatory")
_Sts1LogSubCode_Type = Integer32
_Sts1LogSubCode_Object = MibTableColumn
sts1LogSubCode = _Sts1LogSubCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1, 4),
    _Sts1LogSubCode_Type()
)
sts1LogSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogSubCode.setStatus("mandatory")
_Sts1LogSecurity_Type = Integer32
_Sts1LogSecurity_Object = MibTableColumn
sts1LogSecurity = _Sts1LogSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1, 5),
    _Sts1LogSecurity_Type()
)
sts1LogSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogSecurity.setStatus("mandatory")


class _Sts1LogMsg_Type(DisplayString):
    """Custom type sts1LogMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Sts1LogMsg_Type.__name__ = "DisplayString"
_Sts1LogMsg_Object = MibTableColumn
sts1LogMsg = _Sts1LogMsg_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 2, 1, 6),
    _Sts1LogMsg_Type()
)
sts1LogMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts1LogMsg.setStatus("mandatory")
_Sts2LogNum_Type = Integer32
_Sts2LogNum_Object = MibScalar
sts2LogNum = _Sts2LogNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 3),
    _Sts2LogNum_Type()
)
sts2LogNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogNum.setStatus("mandatory")
_Sts2LogTable_Object = MibTable
sts2LogTable = _Sts2LogTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4)
)
if mibBuilder.loadTexts:
    sts2LogTable.setStatus("mandatory")
_Sts2LogEntry_Object = MibTableRow
sts2LogEntry = _Sts2LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1)
)
sts2LogEntry.setIndexNames(
    (0, "DeltaSTS-MIB", "sts2LogIndex"),
)
if mibBuilder.loadTexts:
    sts2LogEntry.setStatus("mandatory")


class _Sts2LogIndex_Type(Integer32):
    """Custom type sts2LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Sts2LogIndex_Type.__name__ = "Integer32"
_Sts2LogIndex_Object = MibTableColumn
sts2LogIndex = _Sts2LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1, 1),
    _Sts2LogIndex_Type()
)
sts2LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogIndex.setStatus("mandatory")


class _Sts2LogDate_Type(DisplayString):
    """Custom type sts2LogDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Sts2LogDate_Type.__name__ = "DisplayString"
_Sts2LogDate_Object = MibTableColumn
sts2LogDate = _Sts2LogDate_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1, 2),
    _Sts2LogDate_Type()
)
sts2LogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogDate.setStatus("mandatory")
_Sts2LogMainCode_Type = Integer32
_Sts2LogMainCode_Object = MibTableColumn
sts2LogMainCode = _Sts2LogMainCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1, 3),
    _Sts2LogMainCode_Type()
)
sts2LogMainCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogMainCode.setStatus("mandatory")
_Sts2LogSubCode_Type = Integer32
_Sts2LogSubCode_Object = MibTableColumn
sts2LogSubCode = _Sts2LogSubCode_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1, 4),
    _Sts2LogSubCode_Type()
)
sts2LogSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogSubCode.setStatus("mandatory")
_Sts2LogSecurity_Type = Integer32
_Sts2LogSecurity_Object = MibTableColumn
sts2LogSecurity = _Sts2LogSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1, 5),
    _Sts2LogSecurity_Type()
)
sts2LogSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogSecurity.setStatus("mandatory")


class _Sts2LogMsg_Type(DisplayString):
    """Custom type sts2LogMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Sts2LogMsg_Type.__name__ = "DisplayString"
_Sts2LogMsg_Object = MibTableColumn
sts2LogMsg = _Sts2LogMsg_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 10, 4, 1, 6),
    _Sts2LogMsg_Type()
)
sts2LogMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sts2LogMsg.setStatus("mandatory")
_StsTrapArgs_ObjectIdentity = ObjectIdentity
stsTrapArgs = _StsTrapArgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 11)
)
_StsDescription_Type = DisplayString
_StsDescription_Object = MibScalar
stsDescription = _StsDescription_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 11, 1),
    _StsDescription_Type()
)
stsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsDescription.setStatus("mandatory")
_StsTimeTicks_Type = TimeTicks
_StsTimeTicks_Object = MibScalar
stsTimeTicks = _StsTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 11, 2),
    _StsTimeTicks_Type()
)
stsTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsTimeTicks.setStatus("mandatory")
_StsTraps_ObjectIdentity = ObjectIdentity
stsTraps = _StsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20)
)

# Managed Objects groups


# Notification objects

stsTrapCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 1)
)
if mibBuilder.loadTexts:
    stsTrapCommLost.setStatus(
        ""
    )

stsTrapCommEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 2)
)
if mibBuilder.loadTexts:
    stsTrapCommEstablished.setStatus(
        ""
    )

stsTrapSystemAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 3)
)
if mibBuilder.loadTexts:
    stsTrapSystemAlarm.setStatus(
        ""
    )

stsTrapSystemAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 4)
)
if mibBuilder.loadTexts:
    stsTrapSystemAlarmRecover.setStatus(
        ""
    )

stsTrapRepairAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 5)
)
if mibBuilder.loadTexts:
    stsTrapRepairAlarm.setStatus(
        ""
    )

stsTrapRepairAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 6)
)
if mibBuilder.loadTexts:
    stsTrapRepairAlarmRecover.setStatus(
        ""
    )

stsTrapIOAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 7)
)
if mibBuilder.loadTexts:
    stsTrapIOAlarm.setStatus(
        ""
    )

stsTrapIOAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 8)
)
if mibBuilder.loadTexts:
    stsTrapIOAlarmRecover.setStatus(
        ""
    )

stsTrapTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 9)
)
if mibBuilder.loadTexts:
    stsTrapTemperatureAlarm.setStatus(
        ""
    )

stsTrapTemperatureAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 10)
)
if mibBuilder.loadTexts:
    stsTrapTemperatureAlarmRecover.setStatus(
        ""
    )

stsTrapNTCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 11)
)
if mibBuilder.loadTexts:
    stsTrapNTCAlarm.setStatus(
        ""
    )

stsTrapNTCAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 12)
)
if mibBuilder.loadTexts:
    stsTrapNTCAlarmRecover.setStatus(
        ""
    )

stsTrapFanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 13)
)
if mibBuilder.loadTexts:
    stsTrapFanAlarm.setStatus(
        ""
    )

stsTrapFanAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 14)
)
if mibBuilder.loadTexts:
    stsTrapFanAlarmRecover.setStatus(
        ""
    )

stsTrapSCRAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 15)
)
if mibBuilder.loadTexts:
    stsTrapSCRAlarm.setStatus(
        ""
    )

stsTrapSTSAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 61, 20, 0, 16)
)
if mibBuilder.loadTexts:
    stsTrapSTSAlarmRecover.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaSTS-MIB",
    **{"delta": delta,
       "ups": ups,
       "sts": sts,
       "stsAgent": stsAgent,
       "stsAgentManufacturer": stsAgentManufacturer,
       "stsAgentVersion": stsAgentVersion,
       "stsAgentDevLink": stsAgentDevLink,
       "stsIdent": stsIdent,
       "stsIdentManufacturer": stsIdentManufacturer,
       "stsIdentModel": stsIdentModel,
       "stsIdentSysSerialNumber": stsIdentSysSerialNumber,
       "stsIdentSTS1SerialNumber": stsIdentSTS1SerialNumber,
       "stsIdentSTS2SerialNumber": stsIdentSTS2SerialNumber,
       "stsIdentSTS1FWVersion": stsIdentSTS1FWVersion,
       "stsIdentSTS2FWVersion": stsIdentSTS2FWVersion,
       "stsIdentModuleType": stsIdentModuleType,
       "stsInput": stsInput,
       "stsInputTable": stsInputTable,
       "stsInputEntry": stsInputEntry,
       "stsInputSource1PhaseVoltage": stsInputSource1PhaseVoltage,
       "stsInputSource1LineVoltage": stsInputSource1LineVoltage,
       "stsInputSource1Current": stsInputSource1Current,
       "stsInputSource1KVA": stsInputSource1KVA,
       "stsInputSource1KW": stsInputSource1KW,
       "stsInputSource1Load": stsInputSource1Load,
       "stsInputSource2PhaseVoltage": stsInputSource2PhaseVoltage,
       "stsInputSource2LineVoltage": stsInputSource2LineVoltage,
       "stsInputSource2Current": stsInputSource2Current,
       "stsInputSource2KVA": stsInputSource2KVA,
       "stsInputSource2KW": stsInputSource2KW,
       "stsInputSource2Load": stsInputSource2Load,
       "stsInputIndex": stsInputIndex,
       "stsInputSource1NeutralCurrent": stsInputSource1NeutralCurrent,
       "stsInputSource1Frequency": stsInputSource1Frequency,
       "stsInputSource1TotalKVA": stsInputSource1TotalKVA,
       "stsInputSource1TotalKW": stsInputSource1TotalKW,
       "stsInputSource1NeutralLoad": stsInputSource1NeutralLoad,
       "stsInputSource2NeutralCurrent": stsInputSource2NeutralCurrent,
       "stsInputSource2Frequency": stsInputSource2Frequency,
       "stsInputSource2TotalKVA": stsInputSource2TotalKVA,
       "stsInputSource2TotalKW": stsInputSource2TotalKW,
       "stsInputSource2NeutralLoad": stsInputSource2NeutralLoad,
       "stsInputDifference": stsInputDifference,
       "stsOutput": stsOutput,
       "stsOutputTable": stsOutputTable,
       "stsOutputEntry": stsOutputEntry,
       "stsOutputPhaseVoltage": stsOutputPhaseVoltage,
       "stsOutputLineVoltage": stsOutputLineVoltage,
       "stsOutputCurrent": stsOutputCurrent,
       "stsOutputPF": stsOutputPF,
       "stsOutputCF": stsOutputCF,
       "stsOutputKVA": stsOutputKVA,
       "stsOutputKW": stsOutputKW,
       "stsOutputLoad": stsOutputLoad,
       "stsOutputIndex": stsOutputIndex,
       "stsOutputNeutralCurrent": stsOutputNeutralCurrent,
       "stsOutputFrequency": stsOutputFrequency,
       "stsOutputNeutralCF": stsOutputNeutralCF,
       "stsOutputTotalPF": stsOutputTotalPF,
       "stsOutputTotalKVA": stsOutputTotalKVA,
       "stsOutputTotalKW": stsOutputTotalKW,
       "stsOutputNeturalLoad": stsOutputNeturalLoad,
       "stsOutputKWH": stsOutputKWH,
       "stsFanTable": stsFanTable,
       "stsFanEntry": stsFanEntry,
       "stsFans": stsFans,
       "stsFanIndex": stsFanIndex,
       "stsTemperature": stsTemperature,
       "stsTemperatureTable": stsTemperatureTable,
       "stsTemperatureEntry": stsTemperatureEntry,
       "stsTemperatureR1": stsTemperatureR1,
       "stsTemperatureS1": stsTemperatureS1,
       "stsTemperatureT1": stsTemperatureT1,
       "stsTemperatureN1": stsTemperatureN1,
       "stsTemperatureR2": stsTemperatureR2,
       "stsTemperatureS2": stsTemperatureS2,
       "stsTemperatureT2": stsTemperatureT2,
       "stsTemperatureN2": stsTemperatureN2,
       "stsTemperatureIndex": stsTemperatureIndex,
       "stsTemperatureAmbient": stsTemperatureAmbient,
       "stsStatistic": stsStatistic,
       "stsStatisticSource1Count": stsStatisticSource1Count,
       "stsStatisticSource2Count": stsStatisticSource2Count,
       "stsStatisticBypass1Count": stsStatisticBypass1Count,
       "stsStatisticBypass2Count": stsStatisticBypass2Count,
       "stsStatisticTransferCount": stsStatisticTransferCount,
       "stsStatisticTimeTable": stsStatisticTimeTable,
       "stsStatisticTimeEntry": stsStatisticTimeEntry,
       "stsStatisticHours": stsStatisticHours,
       "stsStatisticMinutes": stsStatisticMinutes,
       "stsStatisticIndex": stsStatisticIndex,
       "stsStatus": stsStatus,
       "stsStatusActiveCard": stsStatusActiveCard,
       "stsStatusPowerFlow": stsStatusPowerFlow,
       "stsStatusSource1": stsStatusSource1,
       "stsStatusSource2": stsStatusSource2,
       "stsStatusSource1MCCB": stsStatusSource1MCCB,
       "stsStatusSource2MCCB": stsStatusSource2MCCB,
       "stsStatusBypass1MCCB": stsStatusBypass1MCCB,
       "stsStatusBypass2MCCB": stsStatusBypass2MCCB,
       "stsStatusOutputMCCB1": stsStatusOutputMCCB1,
       "stsStatusOutputMCCB2": stsStatusOutputMCCB2,
       "stsStatusOutputMCCB3": stsStatusOutputMCCB3,
       "stsStatusSource1SCR": stsStatusSource1SCR,
       "stsStatusSource2SCR": stsStatusSource2SCR,
       "stsStatusLoadOnSource1": stsStatusLoadOnSource1,
       "stsStatusLoadOnSource2": stsStatusLoadOnSource2,
       "stsStatusLoadOnBypass1": stsStatusLoadOnBypass1,
       "stsStatusLoadOnBypass2": stsStatusLoadOnBypass2,
       "stsStatusLoad": stsStatusLoad,
       "stsStatusWarnSystemCode": stsStatusWarnSystemCode,
       "stsStatusWarnSystem": stsStatusWarnSystem,
       "stsStatusWarnCard1MCU": stsStatusWarnCard1MCU,
       "stsStatusWarnCard2MCU": stsStatusWarnCard2MCU,
       "stsStatusWarnROM": stsStatusWarnROM,
       "stsStatusWarnReplaceFilter": stsStatusWarnReplaceFilter,
       "stsStatusWarnComm": stsStatusWarnComm,
       "stsStatusWarnComm1": stsStatusWarnComm1,
       "stsStatusWarnComm2": stsStatusWarnComm2,
       "stsStatusWarnAuxPowerFuse": stsStatusWarnAuxPowerFuse,
       "stsStatusWarnAuxPowerCard": stsStatusWarnAuxPowerCard,
       "stsStatusWarnAuxPowerFan": stsStatusWarnAuxPowerFan,
       "stsStatusWarnEPO": stsStatusWarnEPO,
       "stsStatusWarnBUZ": stsStatusWarnBUZ,
       "stsStatusWarnRepairCode": stsStatusWarnRepairCode,
       "stsStatusWarnRepair": stsStatusWarnRepair,
       "stsStatusWarnRepairSTSCard1": stsStatusWarnRepairSTSCard1,
       "stsStatusWarnRepairSTSCard2": stsStatusWarnRepairSTSCard2,
       "stsStatusWarnRepairSTSModule1": stsStatusWarnRepairSTSModule1,
       "stsStatusWarnRepairSTSModule2": stsStatusWarnRepairSTSModule2,
       "stsStatusWarnRepairBreakerCard1": stsStatusWarnRepairBreakerCard1,
       "stsStatusWarnRepairAuxPowerCard1": stsStatusWarnRepairAuxPowerCard1,
       "stsStatusWarnRepairAuxPowerCard2": stsStatusWarnRepairAuxPowerCard2,
       "stsStatusWarnRepairAuxPowerCard3": stsStatusWarnRepairAuxPowerCard3,
       "stsStatusWarnIOCode": stsStatusWarnIOCode,
       "stsStatusWarnIO": stsStatusWarnIO,
       "stsStatusWarnSource1Fail": stsStatusWarnSource1Fail,
       "stsStatusWarnSource1VoltAbnormal": stsStatusWarnSource1VoltAbnormal,
       "stsStatusWarnSource1OverVolt": stsStatusWarnSource1OverVolt,
       "stsStatusWarnSource1UnderVolt": stsStatusWarnSource1UnderVolt,
       "stsStatusWarnSource1FreqOutRange": stsStatusWarnSource1FreqOutRange,
       "stsStatusWarnSource1PhaseSequence": stsStatusWarnSource1PhaseSequence,
       "stsStatusWarnSource1BreakerTrip": stsStatusWarnSource1BreakerTrip,
       "stsStatusWarnSource1Overload": stsStatusWarnSource1Overload,
       "stsStatusWarnSource2Fail": stsStatusWarnSource2Fail,
       "stsStatusWarnSource2VoltAbnormal": stsStatusWarnSource2VoltAbnormal,
       "stsStatusWarnSource2OverVolt": stsStatusWarnSource2OverVolt,
       "stsStatusWarnSource2UnderVolt": stsStatusWarnSource2UnderVolt,
       "stsStatusWarnSource2FreqOutRange": stsStatusWarnSource2FreqOutRange,
       "stsStatusWarnSource2PhaseSequence": stsStatusWarnSource2PhaseSequence,
       "stsStatusWarnSource2BreakerTrip": stsStatusWarnSource2BreakerTrip,
       "stsStatusWarnSource2Overload": stsStatusWarnSource2Overload,
       "stsStatusWarnOutputOverLoad": stsStatusWarnOutputOverLoad,
       "stsStatusWarnOutputShortCircuit": stsStatusWarnOutputShortCircuit,
       "stsStatusWarnPF": stsStatusWarnPF,
       "stsStatusWarnCF": stsStatusWarnCF,
       "stsStatusWarnTransInhibited": stsStatusWarnTransInhibited,
       "stsStatusWarnRetransferFail": stsStatusWarnRetransferFail,
       "stsStatusWarnInputSourceAsync": stsStatusWarnInputSourceAsync,
       "stsStatusWarnOutputVoltAbnormal": stsStatusWarnOutputVoltAbnormal,
       "stsStatusWarnSource1IPeakOver": stsStatusWarnSource1IPeakOver,
       "stsStatusWarnSource2IPeakOver": stsStatusWarnSource2IPeakOver,
       "stsStatusWarnTemperatureCode": stsStatusWarnTemperatureCode,
       "stsStatusWarnTemperature": stsStatusWarnTemperature,
       "stsStatusWarnTempSource1R1OH": stsStatusWarnTempSource1R1OH,
       "stsStatusWarnTempSource1S1OH": stsStatusWarnTempSource1S1OH,
       "stsStatusWarnTempSource1T1OH": stsStatusWarnTempSource1T1OH,
       "stsStatusWarnTempSource1N1OH": stsStatusWarnTempSource1N1OH,
       "stsStatusWarnTempSource1R2OH": stsStatusWarnTempSource1R2OH,
       "stsStatusWarnTempSource1S2OH": stsStatusWarnTempSource1S2OH,
       "stsStatusWarnTempSource1T2OH": stsStatusWarnTempSource1T2OH,
       "stsStatusWarnTempSource1N2OH": stsStatusWarnTempSource1N2OH,
       "stsStatusWarnTempSource2R1OH": stsStatusWarnTempSource2R1OH,
       "stsStatusWarnTempSource2S1OH": stsStatusWarnTempSource2S1OH,
       "stsStatusWarnTempSource2T1OH": stsStatusWarnTempSource2T1OH,
       "stsStatusWarnTempSource2N1OH": stsStatusWarnTempSource2N1OH,
       "stsStatusWarnTempSource2R2OH": stsStatusWarnTempSource2R2OH,
       "stsStatusWarnTempSource2S2OH": stsStatusWarnTempSource2S2OH,
       "stsStatusWarnTempSource2T2OH": stsStatusWarnTempSource2T2OH,
       "stsStatusWarnTempSource2N2OH": stsStatusWarnTempSource2N2OH,
       "stsStatusWarnTempSource1R1OHSD": stsStatusWarnTempSource1R1OHSD,
       "stsStatusWarnTempSource1S1OHSD": stsStatusWarnTempSource1S1OHSD,
       "stsStatusWarnTempSource1T1OHSD": stsStatusWarnTempSource1T1OHSD,
       "stsStatusWarnTempSource1N1OHSD": stsStatusWarnTempSource1N1OHSD,
       "stsStatusWarnTempSource1R2OHSD": stsStatusWarnTempSource1R2OHSD,
       "stsStatusWarnTempSource1S2OHSD": stsStatusWarnTempSource1S2OHSD,
       "stsStatusWarnTempSource1T2OHSD": stsStatusWarnTempSource1T2OHSD,
       "stsStatusWarnTempSource1N2OHSD": stsStatusWarnTempSource1N2OHSD,
       "stsStatusWarnTempSource2R1OHSD": stsStatusWarnTempSource2R1OHSD,
       "stsStatusWarnTempSource2S1OHSD": stsStatusWarnTempSource2S1OHSD,
       "stsStatusWarnTempSource2T1OHSD": stsStatusWarnTempSource2T1OHSD,
       "stsStatusWarnTempSource2N1OHSD": stsStatusWarnTempSource2N1OHSD,
       "stsStatusWarnTempSource2R2OHSD": stsStatusWarnTempSource2R2OHSD,
       "stsStatusWarnTempSource2S2OHSD": stsStatusWarnTempSource2S2OHSD,
       "stsStatusWarnTempSource2T2OHSD": stsStatusWarnTempSource2T2OHSD,
       "stsStatusWarnTempSource2N2OHSD": stsStatusWarnTempSource2N2OHSD,
       "stsStatusWarnNTCCode": stsStatusWarnNTCCode,
       "stsStatusWarnNTC": stsStatusWarnNTC,
       "stsStatusWarnNTCAmbient": stsStatusWarnNTCAmbient,
       "stsStatusWarnNTCSource1R1": stsStatusWarnNTCSource1R1,
       "stsStatusWarnNTCSource1S1": stsStatusWarnNTCSource1S1,
       "stsStatusWarnNTCSource1T1": stsStatusWarnNTCSource1T1,
       "stsStatusWarnNTCSource1N1": stsStatusWarnNTCSource1N1,
       "stsStatusWarnNTCSource1R2": stsStatusWarnNTCSource1R2,
       "stsStatusWarnNTCSource1S2": stsStatusWarnNTCSource1S2,
       "stsStatusWarnNTCSource1T2": stsStatusWarnNTCSource1T2,
       "stsStatusWarnNTCSource1N2": stsStatusWarnNTCSource1N2,
       "stsStatusWarnNTCSource2R1": stsStatusWarnNTCSource2R1,
       "stsStatusWarnNTCSource2S1": stsStatusWarnNTCSource2S1,
       "stsStatusWarnNTCSource2T1": stsStatusWarnNTCSource2T1,
       "stsStatusWarnNTCSource2N1": stsStatusWarnNTCSource2N1,
       "stsStatusWarnNTCSource2R2": stsStatusWarnNTCSource2R2,
       "stsStatusWarnNTCSource2S2": stsStatusWarnNTCSource2S2,
       "stsStatusWarnNTCSource2T2": stsStatusWarnNTCSource2T2,
       "stsStatusWarnNTCSource2N2": stsStatusWarnNTCSource2N2,
       "stsStatusWarnFanCode1": stsStatusWarnFanCode1,
       "stsStatusWarnFanCode2": stsStatusWarnFanCode2,
       "stsStatusWarnFan": stsStatusWarnFan,
       "stsStatusWarnFanTable": stsStatusWarnFanTable,
       "stsStatusWarnFanEntry": stsStatusWarnFanEntry,
       "stsStatusWarnFans": stsStatusWarnFans,
       "stsStatusWarnFanIndex": stsStatusWarnFanIndex,
       "stsStatusWarnSCRCode": stsStatusWarnSCRCode,
       "stsStatusWarnSCR": stsStatusWarnSCR,
       "stsStatusWarnSCRTable": stsStatusWarnSCRTable,
       "stsStatusWarnSCREntry": stsStatusWarnSCREntry,
       "stsStatusWarnSCRS1Open": stsStatusWarnSCRS1Open,
       "stsStatusWarnSCRS1ShortOff": stsStatusWarnSCRS1ShortOff,
       "stsStatusWarnSCRS1ShortOn": stsStatusWarnSCRS1ShortOn,
       "stsStatusWarnSCRS2Open": stsStatusWarnSCRS2Open,
       "stsStatusWarnSCRS2ShortOff": stsStatusWarnSCRS2ShortOff,
       "stsStatusWarnSCRS2ShortOn": stsStatusWarnSCRS2ShortOn,
       "stsStatusWarnSCRIndex": stsStatusWarnSCRIndex,
       "stsConfig": stsConfig,
       "stsConfigSys": stsConfigSys,
       "stsConfigSysVoltRating": stsConfigSysVoltRating,
       "stsConfigSysFreqRating": stsConfigSysFreqRating,
       "stsConfigSysCurrentRating": stsConfigSysCurrentRating,
       "stsConfigSysTemperatureUnit": stsConfigSysTemperatureUnit,
       "stsConfigInput": stsConfigInput,
       "stsConfigInputPreferredSource": stsConfigInputPreferredSource,
       "stsConfigInputPhaseSyncRangeH": stsConfigInputPhaseSyncRangeH,
       "stsConfigInputPhaseSyncRangeL": stsConfigInputPhaseSyncRangeL,
       "stsConfigInputPhaseSyncRange": stsConfigInputPhaseSyncRange,
       "stsConfigInputAsyncTranRangeH": stsConfigInputAsyncTranRangeH,
       "stsConfigInputAsyncTranRangeL": stsConfigInputAsyncTranRangeL,
       "stsConfigInputAsyncTranRange": stsConfigInputAsyncTranRange,
       "stsConfigInputSource1VoltRnageH": stsConfigInputSource1VoltRnageH,
       "stsConfigInputSource1VoltRnageL": stsConfigInputSource1VoltRnageL,
       "stsConfigInputSource2VoltRnageH": stsConfigInputSource2VoltRnageH,
       "stsConfigInputSource2VoltRnageL": stsConfigInputSource2VoltRnageL,
       "stsConfigInputSource1FreqRangeH": stsConfigInputSource1FreqRangeH,
       "stsConfigInputSource1FreqRangeL": stsConfigInputSource1FreqRangeL,
       "stsConfigInputSource2FreqRangeH": stsConfigInputSource2FreqRangeH,
       "stsConfigInputSource2FreqRangeL": stsConfigInputSource2FreqRangeL,
       "stsConfigControl": stsConfigControl,
       "stsConfigTransferMode": stsConfigTransferMode,
       "stsConfigRetransfer": stsConfigRetransfer,
       "stsConfigTransferDelayRangeH": stsConfigTransferDelayRangeH,
       "stsConfigTransferDelayRangeL": stsConfigTransferDelayRangeL,
       "stsConfigTransferDelayRange": stsConfigTransferDelayRange,
       "stsConfigBuzzer": stsConfigBuzzer,
       "stsConfigClearSTS1EventLog": stsConfigClearSTS1EventLog,
       "stsConfigClearSTS2EventLog": stsConfigClearSTS2EventLog,
       "stsConfigClearStatistic": stsConfigClearStatistic,
       "stsConfigDryContact": stsConfigDryContact,
       "stsConfigInputDryContEvent1": stsConfigInputDryContEvent1,
       "stsConfigInputDryContEvent2": stsConfigInputDryContEvent2,
       "stsConfigInputDryContEvent3": stsConfigInputDryContEvent3,
       "stsConfigInputDryContEvent4": stsConfigInputDryContEvent4,
       "stsConfigInputDryContType1": stsConfigInputDryContType1,
       "stsConfigInputDryContType2": stsConfigInputDryContType2,
       "stsConfigInputDryContType3": stsConfigInputDryContType3,
       "stsConfigInputDryContType4": stsConfigInputDryContType4,
       "stsConfigOutputDryContEvent1": stsConfigOutputDryContEvent1,
       "stsConfigOutputDryContEvent2": stsConfigOutputDryContEvent2,
       "stsConfigOutputDryContEvent3": stsConfigOutputDryContEvent3,
       "stsConfigOutputDryContEvent4": stsConfigOutputDryContEvent4,
       "stsConfigOutputDryContEvent5": stsConfigOutputDryContEvent5,
       "stsConfigOutputDryContEvent6": stsConfigOutputDryContEvent6,
       "stsConfigOutputDryContType1": stsConfigOutputDryContType1,
       "stsConfigOutputDryContType2": stsConfigOutputDryContType2,
       "stsConfigOutputDryContType3": stsConfigOutputDryContType3,
       "stsConfigOutputDryContType4": stsConfigOutputDryContType4,
       "stsConfigOutputDryContType5": stsConfigOutputDryContType5,
       "stsConfigOutputDryContType6": stsConfigOutputDryContType6,
       "stsConfigLocal": stsConfigLocal,
       "stsConfigFormat": stsConfigFormat,
       "stsConfigLCDContrast": stsConfigLCDContrast,
       "stsConfigLCDSleep": stsConfigLCDSleep,
       "stsLog": stsLog,
       "sts1LogNum": sts1LogNum,
       "sts1LogTable": sts1LogTable,
       "sts1LogEntry": sts1LogEntry,
       "sts1LogIndex": sts1LogIndex,
       "sts1LogDate": sts1LogDate,
       "sts1LogMainCode": sts1LogMainCode,
       "sts1LogSubCode": sts1LogSubCode,
       "sts1LogSecurity": sts1LogSecurity,
       "sts1LogMsg": sts1LogMsg,
       "sts2LogNum": sts2LogNum,
       "sts2LogTable": sts2LogTable,
       "sts2LogEntry": sts2LogEntry,
       "sts2LogIndex": sts2LogIndex,
       "sts2LogDate": sts2LogDate,
       "sts2LogMainCode": sts2LogMainCode,
       "sts2LogSubCode": sts2LogSubCode,
       "sts2LogSecurity": sts2LogSecurity,
       "sts2LogMsg": sts2LogMsg,
       "stsTrapArgs": stsTrapArgs,
       "stsDescription": stsDescription,
       "stsTimeTicks": stsTimeTicks,
       "stsTraps": stsTraps,
       "stsTrapCommLost": stsTrapCommLost,
       "stsTrapCommEstablished": stsTrapCommEstablished,
       "stsTrapSystemAlarm": stsTrapSystemAlarm,
       "stsTrapSystemAlarmRecover": stsTrapSystemAlarmRecover,
       "stsTrapRepairAlarm": stsTrapRepairAlarm,
       "stsTrapRepairAlarmRecover": stsTrapRepairAlarmRecover,
       "stsTrapIOAlarm": stsTrapIOAlarm,
       "stsTrapIOAlarmRecover": stsTrapIOAlarmRecover,
       "stsTrapTemperatureAlarm": stsTrapTemperatureAlarm,
       "stsTrapTemperatureAlarmRecover": stsTrapTemperatureAlarmRecover,
       "stsTrapNTCAlarm": stsTrapNTCAlarm,
       "stsTrapNTCAlarmRecover": stsTrapNTCAlarmRecover,
       "stsTrapFanAlarm": stsTrapFanAlarm,
       "stsTrapFanAlarmRecover": stsTrapFanAlarmRecover,
       "stsTrapSCRAlarm": stsTrapSCRAlarm,
       "stsTrapSTSAlarmRecover": stsTrapSTSAlarmRecover}
)
