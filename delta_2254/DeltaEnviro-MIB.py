# SNMP MIB module (DeltaEnviro-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_2254/DeltaEnviro-MIB.mib
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
_Enviro_ObjectIdentity = ObjectIdentity
enviro = _Enviro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41)
)
_DenviroIdent_ObjectIdentity = ObjectIdentity
denviroIdent = _DenviroIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1)
)


class _DenviroIdentManufacturer_Type(DisplayString):
    """Custom type denviroIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentManufacturer_Type.__name__ = "DisplayString"
_DenviroIdentManufacturer_Object = MibScalar
denviroIdentManufacturer = _DenviroIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 1),
    _DenviroIdentManufacturer_Type()
)
denviroIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroIdentManufacturer.setStatus("mandatory")


class _DenviroIdentModel_Type(DisplayString):
    """Custom type denviroIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentModel_Type.__name__ = "DisplayString"
_DenviroIdentModel_Object = MibScalar
denviroIdentModel = _DenviroIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 2),
    _DenviroIdentModel_Type()
)
denviroIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroIdentModel.setStatus("mandatory")


class _DenviroIdentSerialNumber_Type(DisplayString):
    """Custom type denviroIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DenviroIdentSerialNumber_Type.__name__ = "DisplayString"
_DenviroIdentSerialNumber_Object = MibScalar
denviroIdentSerialNumber = _DenviroIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 3),
    _DenviroIdentSerialNumber_Type()
)
denviroIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroIdentSerialNumber.setStatus("mandatory")


class _DenviroIdentAgentFirmwareVersion_Type(DisplayString):
    """Custom type denviroIdentAgentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DenviroIdentAgentFirmwareVersion_Type.__name__ = "DisplayString"
_DenviroIdentAgentFirmwareVersion_Object = MibScalar
denviroIdentAgentFirmwareVersion = _DenviroIdentAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 4),
    _DenviroIdentAgentFirmwareVersion_Type()
)
denviroIdentAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroIdentAgentFirmwareVersion.setStatus("mandatory")


class _DenviroIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type denviroIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DenviroIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_DenviroIdentAgentSoftwareVersion_Object = MibScalar
denviroIdentAgentSoftwareVersion = _DenviroIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 5),
    _DenviroIdentAgentSoftwareVersion_Type()
)
denviroIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroIdentAgentSoftwareVersion.setStatus("mandatory")


class _DenviroIdentName_Type(DisplayString):
    """Custom type denviroIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentName_Type.__name__ = "DisplayString"
_DenviroIdentName_Object = MibScalar
denviroIdentName = _DenviroIdentName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 6),
    _DenviroIdentName_Type()
)
denviroIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentName.setStatus("mandatory")


class _DenviroIdentSensorHub1Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub1Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub1Title_Object = MibScalar
denviroIdentSensorHub1Title = _DenviroIdentSensorHub1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 7),
    _DenviroIdentSensorHub1Title_Type()
)
denviroIdentSensorHub1Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub1Title.setStatus("mandatory")


class _DenviroIdentSensorHub2Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub2Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub2Title_Object = MibScalar
denviroIdentSensorHub2Title = _DenviroIdentSensorHub2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 8),
    _DenviroIdentSensorHub2Title_Type()
)
denviroIdentSensorHub2Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub2Title.setStatus("mandatory")


class _DenviroIdentSensorHub3Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub3Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub3Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub3Title_Object = MibScalar
denviroIdentSensorHub3Title = _DenviroIdentSensorHub3Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 9),
    _DenviroIdentSensorHub3Title_Type()
)
denviroIdentSensorHub3Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub3Title.setStatus("mandatory")


class _DenviroIdentSensorHub4Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub4Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub4Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub4Title_Object = MibScalar
denviroIdentSensorHub4Title = _DenviroIdentSensorHub4Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 10),
    _DenviroIdentSensorHub4Title_Type()
)
denviroIdentSensorHub4Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub4Title.setStatus("mandatory")


class _DenviroIdentSensorHub5Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub5Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub5Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub5Title_Object = MibScalar
denviroIdentSensorHub5Title = _DenviroIdentSensorHub5Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 11),
    _DenviroIdentSensorHub5Title_Type()
)
denviroIdentSensorHub5Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub5Title.setStatus("mandatory")


class _DenviroIdentSensorHub6Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub6Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub6Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub6Title_Object = MibScalar
denviroIdentSensorHub6Title = _DenviroIdentSensorHub6Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 12),
    _DenviroIdentSensorHub6Title_Type()
)
denviroIdentSensorHub6Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub6Title.setStatus("mandatory")


class _DenviroIdentSensorHub7Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub7Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub7Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub7Title_Object = MibScalar
denviroIdentSensorHub7Title = _DenviroIdentSensorHub7Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 13),
    _DenviroIdentSensorHub7Title_Type()
)
denviroIdentSensorHub7Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub7Title.setStatus("mandatory")


class _DenviroIdentSensorHub8Title_Type(DisplayString):
    """Custom type denviroIdentSensorHub8Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentSensorHub8Title_Type.__name__ = "DisplayString"
_DenviroIdentSensorHub8Title_Object = MibScalar
denviroIdentSensorHub8Title = _DenviroIdentSensorHub8Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 14),
    _DenviroIdentSensorHub8Title_Type()
)
denviroIdentSensorHub8Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentSensorHub8Title.setStatus("mandatory")


class _DenviroIdentAI1Title_Type(DisplayString):
    """Custom type denviroIdentAI1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentAI1Title_Type.__name__ = "DisplayString"
_DenviroIdentAI1Title_Object = MibScalar
denviroIdentAI1Title = _DenviroIdentAI1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 15),
    _DenviroIdentAI1Title_Type()
)
denviroIdentAI1Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentAI1Title.setStatus("mandatory")


class _DenviroIdentAI2Title_Type(DisplayString):
    """Custom type denviroIdentAI2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentAI2Title_Type.__name__ = "DisplayString"
_DenviroIdentAI2Title_Object = MibScalar
denviroIdentAI2Title = _DenviroIdentAI2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 16),
    _DenviroIdentAI2Title_Type()
)
denviroIdentAI2Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentAI2Title.setStatus("mandatory")


class _DenviroIdentAI3Title_Type(DisplayString):
    """Custom type denviroIdentAI3Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentAI3Title_Type.__name__ = "DisplayString"
_DenviroIdentAI3Title_Object = MibScalar
denviroIdentAI3Title = _DenviroIdentAI3Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 17),
    _DenviroIdentAI3Title_Type()
)
denviroIdentAI3Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentAI3Title.setStatus("mandatory")


class _DenviroIdentAI4Title_Type(DisplayString):
    """Custom type denviroIdentAI4Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentAI4Title_Type.__name__ = "DisplayString"
_DenviroIdentAI4Title_Object = MibScalar
denviroIdentAI4Title = _DenviroIdentAI4Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 18),
    _DenviroIdentAI4Title_Type()
)
denviroIdentAI4Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentAI4Title.setStatus("mandatory")


class _DenviroIdentDI1Title_Type(DisplayString):
    """Custom type denviroIdentDI1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentDI1Title_Type.__name__ = "DisplayString"
_DenviroIdentDI1Title_Object = MibScalar
denviroIdentDI1Title = _DenviroIdentDI1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 19),
    _DenviroIdentDI1Title_Type()
)
denviroIdentDI1Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentDI1Title.setStatus("mandatory")


class _DenviroIdentDI2Title_Type(DisplayString):
    """Custom type denviroIdentDI2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentDI2Title_Type.__name__ = "DisplayString"
_DenviroIdentDI2Title_Object = MibScalar
denviroIdentDI2Title = _DenviroIdentDI2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 20),
    _DenviroIdentDI2Title_Type()
)
denviroIdentDI2Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentDI2Title.setStatus("mandatory")


class _DenviroIdentDI3Title_Type(DisplayString):
    """Custom type denviroIdentDI3Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentDI3Title_Type.__name__ = "DisplayString"
_DenviroIdentDI3Title_Object = MibScalar
denviroIdentDI3Title = _DenviroIdentDI3Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 21),
    _DenviroIdentDI3Title_Type()
)
denviroIdentDI3Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentDI3Title.setStatus("mandatory")


class _DenviroIdentDI4Title_Type(DisplayString):
    """Custom type denviroIdentDI4Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentDI4Title_Type.__name__ = "DisplayString"
_DenviroIdentDI4Title_Object = MibScalar
denviroIdentDI4Title = _DenviroIdentDI4Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 22),
    _DenviroIdentDI4Title_Type()
)
denviroIdentDI4Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentDI4Title.setStatus("mandatory")


class _DenviroIdentDO1Title_Type(DisplayString):
    """Custom type denviroIdentDO1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentDO1Title_Type.__name__ = "DisplayString"
_DenviroIdentDO1Title_Object = MibScalar
denviroIdentDO1Title = _DenviroIdentDO1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 23),
    _DenviroIdentDO1Title_Type()
)
denviroIdentDO1Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentDO1Title.setStatus("mandatory")


class _DenviroIdentDO2Title_Type(DisplayString):
    """Custom type denviroIdentDO2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroIdentDO2Title_Type.__name__ = "DisplayString"
_DenviroIdentDO2Title_Object = MibScalar
denviroIdentDO2Title = _DenviroIdentDO2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 1, 24),
    _DenviroIdentDO2Title_Type()
)
denviroIdentDO2Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroIdentDO2Title.setStatus("mandatory")
_DenviroStatus_ObjectIdentity = ObjectIdentity
denviroStatus = _DenviroStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2)
)


class _DenviroStatusSensorHub1_Type(Integer32):
    """Custom type denviroStatusSensorHub1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub1_Type.__name__ = "Integer32"
_DenviroStatusSensorHub1_Object = MibScalar
denviroStatusSensorHub1 = _DenviroStatusSensorHub1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 1),
    _DenviroStatusSensorHub1_Type()
)
denviroStatusSensorHub1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub1.setStatus("mandatory")


class _DenviroStatusSensorHub2_Type(Integer32):
    """Custom type denviroStatusSensorHub2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub2_Type.__name__ = "Integer32"
_DenviroStatusSensorHub2_Object = MibScalar
denviroStatusSensorHub2 = _DenviroStatusSensorHub2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 2),
    _DenviroStatusSensorHub2_Type()
)
denviroStatusSensorHub2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub2.setStatus("mandatory")


class _DenviroStatusSensorHub3_Type(Integer32):
    """Custom type denviroStatusSensorHub3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub3_Type.__name__ = "Integer32"
_DenviroStatusSensorHub3_Object = MibScalar
denviroStatusSensorHub3 = _DenviroStatusSensorHub3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 3),
    _DenviroStatusSensorHub3_Type()
)
denviroStatusSensorHub3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub3.setStatus("mandatory")


class _DenviroStatusSensorHub4_Type(Integer32):
    """Custom type denviroStatusSensorHub4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub4_Type.__name__ = "Integer32"
_DenviroStatusSensorHub4_Object = MibScalar
denviroStatusSensorHub4 = _DenviroStatusSensorHub4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 4),
    _DenviroStatusSensorHub4_Type()
)
denviroStatusSensorHub4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub4.setStatus("mandatory")


class _DenviroStatusSensorHub5_Type(Integer32):
    """Custom type denviroStatusSensorHub5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub5_Type.__name__ = "Integer32"
_DenviroStatusSensorHub5_Object = MibScalar
denviroStatusSensorHub5 = _DenviroStatusSensorHub5_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 5),
    _DenviroStatusSensorHub5_Type()
)
denviroStatusSensorHub5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub5.setStatus("mandatory")


class _DenviroStatusSensorHub6_Type(Integer32):
    """Custom type denviroStatusSensorHub6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub6_Type.__name__ = "Integer32"
_DenviroStatusSensorHub6_Object = MibScalar
denviroStatusSensorHub6 = _DenviroStatusSensorHub6_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 6),
    _DenviroStatusSensorHub6_Type()
)
denviroStatusSensorHub6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub6.setStatus("mandatory")


class _DenviroStatusSensorHub7_Type(Integer32):
    """Custom type denviroStatusSensorHub7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub7_Type.__name__ = "Integer32"
_DenviroStatusSensorHub7_Object = MibScalar
denviroStatusSensorHub7 = _DenviroStatusSensorHub7_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 7),
    _DenviroStatusSensorHub7_Type()
)
denviroStatusSensorHub7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub7.setStatus("mandatory")


class _DenviroStatusSensorHub8_Type(Integer32):
    """Custom type denviroStatusSensorHub8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusSensorHub8_Type.__name__ = "Integer32"
_DenviroStatusSensorHub8_Object = MibScalar
denviroStatusSensorHub8 = _DenviroStatusSensorHub8_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 8),
    _DenviroStatusSensorHub8_Type()
)
denviroStatusSensorHub8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHub8.setStatus("mandatory")


class _DenviroStatusSensorHubPwr1_Type(Integer32):
    """Custom type denviroStatusSensorHubPwr1 based on Integer32"""
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


_DenviroStatusSensorHubPwr1_Type.__name__ = "Integer32"
_DenviroStatusSensorHubPwr1_Object = MibScalar
denviroStatusSensorHubPwr1 = _DenviroStatusSensorHubPwr1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 9),
    _DenviroStatusSensorHubPwr1_Type()
)
denviroStatusSensorHubPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHubPwr1.setStatus("mandatory")


class _DenviroStatusSensorHubPwr2_Type(Integer32):
    """Custom type denviroStatusSensorHubPwr2 based on Integer32"""
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


_DenviroStatusSensorHubPwr2_Type.__name__ = "Integer32"
_DenviroStatusSensorHubPwr2_Object = MibScalar
denviroStatusSensorHubPwr2 = _DenviroStatusSensorHubPwr2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 10),
    _DenviroStatusSensorHubPwr2_Type()
)
denviroStatusSensorHubPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusSensorHubPwr2.setStatus("mandatory")


class _DenviroStatusDI1_Type(Integer32):
    """Custom type denviroStatusDI1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusDI1_Type.__name__ = "Integer32"
_DenviroStatusDI1_Object = MibScalar
denviroStatusDI1 = _DenviroStatusDI1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 11),
    _DenviroStatusDI1_Type()
)
denviroStatusDI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusDI1.setStatus("mandatory")


class _DenviroStatusDI2_Type(Integer32):
    """Custom type denviroStatusDI2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusDI2_Type.__name__ = "Integer32"
_DenviroStatusDI2_Object = MibScalar
denviroStatusDI2 = _DenviroStatusDI2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 12),
    _DenviroStatusDI2_Type()
)
denviroStatusDI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusDI2.setStatus("mandatory")


class _DenviroStatusDI3_Type(Integer32):
    """Custom type denviroStatusDI3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusDI3_Type.__name__ = "Integer32"
_DenviroStatusDI3_Object = MibScalar
denviroStatusDI3 = _DenviroStatusDI3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 13),
    _DenviroStatusDI3_Type()
)
denviroStatusDI3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusDI3.setStatus("mandatory")


class _DenviroStatusDI4_Type(Integer32):
    """Custom type denviroStatusDI4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusDI4_Type.__name__ = "Integer32"
_DenviroStatusDI4_Object = MibScalar
denviroStatusDI4 = _DenviroStatusDI4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 14),
    _DenviroStatusDI4_Type()
)
denviroStatusDI4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusDI4.setStatus("mandatory")


class _DenviroStatusDO1_Type(Integer32):
    """Custom type denviroStatusDO1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusDO1_Type.__name__ = "Integer32"
_DenviroStatusDO1_Object = MibScalar
denviroStatusDO1 = _DenviroStatusDO1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 15),
    _DenviroStatusDO1_Type()
)
denviroStatusDO1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusDO1.setStatus("mandatory")


class _DenviroStatusDO2_Type(Integer32):
    """Custom type denviroStatusDO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroStatusDO2_Type.__name__ = "Integer32"
_DenviroStatusDO2_Object = MibScalar
denviroStatusDO2 = _DenviroStatusDO2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 16),
    _DenviroStatusDO2_Type()
)
denviroStatusDO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusDO2.setStatus("mandatory")
_DenviroMeasureAI1_Type = Integer32
_DenviroMeasureAI1_Object = MibScalar
denviroMeasureAI1 = _DenviroMeasureAI1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 17),
    _DenviroMeasureAI1_Type()
)
denviroMeasureAI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroMeasureAI1.setStatus("mandatory")
_DenviroMeasureAI2_Type = Integer32
_DenviroMeasureAI2_Object = MibScalar
denviroMeasureAI2 = _DenviroMeasureAI2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 18),
    _DenviroMeasureAI2_Type()
)
denviroMeasureAI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroMeasureAI2.setStatus("mandatory")
_DenviroMeasureAI3_Type = Integer32
_DenviroMeasureAI3_Object = MibScalar
denviroMeasureAI3 = _DenviroMeasureAI3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 19),
    _DenviroMeasureAI3_Type()
)
denviroMeasureAI3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroMeasureAI3.setStatus("mandatory")
_DenviroMeasureAI4_Type = Integer32
_DenviroMeasureAI4_Object = MibScalar
denviroMeasureAI4 = _DenviroMeasureAI4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 20),
    _DenviroMeasureAI4_Type()
)
denviroMeasureAI4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroMeasureAI4.setStatus("mandatory")


class _DenviroStatusAI1_Type(Integer32):
    """Custom type denviroStatusAI1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroStatusAI1_Type.__name__ = "Integer32"
_DenviroStatusAI1_Object = MibScalar
denviroStatusAI1 = _DenviroStatusAI1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 21),
    _DenviroStatusAI1_Type()
)
denviroStatusAI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusAI1.setStatus("mandatory")


class _DenviroStatusAI2_Type(Integer32):
    """Custom type denviroStatusAI2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroStatusAI2_Type.__name__ = "Integer32"
_DenviroStatusAI2_Object = MibScalar
denviroStatusAI2 = _DenviroStatusAI2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 22),
    _DenviroStatusAI2_Type()
)
denviroStatusAI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusAI2.setStatus("mandatory")


class _DenviroStatusAI3_Type(Integer32):
    """Custom type denviroStatusAI3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroStatusAI3_Type.__name__ = "Integer32"
_DenviroStatusAI3_Object = MibScalar
denviroStatusAI3 = _DenviroStatusAI3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 23),
    _DenviroStatusAI3_Type()
)
denviroStatusAI3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusAI3.setStatus("mandatory")


class _DenviroStatusAI4_Type(Integer32):
    """Custom type denviroStatusAI4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroStatusAI4_Type.__name__ = "Integer32"
_DenviroStatusAI4_Object = MibScalar
denviroStatusAI4 = _DenviroStatusAI4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 24),
    _DenviroStatusAI4_Type()
)
denviroStatusAI4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusAI4.setStatus("mandatory")


class _DenviroStatusCommunication_Type(Integer32):
    """Custom type denviroStatusCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("connect", 2))
    )


_DenviroStatusCommunication_Type.__name__ = "Integer32"
_DenviroStatusCommunication_Object = MibScalar
denviroStatusCommunication = _DenviroStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 25),
    _DenviroStatusCommunication_Type()
)
denviroStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusCommunication.setStatus("mandatory")


class _DenviroStatusShortCircuit_Type(Integer32):
    """Custom type denviroStatusShortCircuit based on Integer32"""
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


_DenviroStatusShortCircuit_Type.__name__ = "Integer32"
_DenviroStatusShortCircuit_Object = MibScalar
denviroStatusShortCircuit = _DenviroStatusShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 26),
    _DenviroStatusShortCircuit_Type()
)
denviroStatusShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusShortCircuit.setStatus("mandatory")


class _DenviroStatusOverCurrent_Type(Integer32):
    """Custom type denviroStatusOverCurrent based on Integer32"""
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


_DenviroStatusOverCurrent_Type.__name__ = "Integer32"
_DenviroStatusOverCurrent_Object = MibScalar
denviroStatusOverCurrent = _DenviroStatusOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 27),
    _DenviroStatusOverCurrent_Type()
)
denviroStatusOverCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusOverCurrent.setStatus("mandatory")


class _DenviroStatusOverVoltage_Type(Integer32):
    """Custom type denviroStatusOverVoltage based on Integer32"""
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


_DenviroStatusOverVoltage_Type.__name__ = "Integer32"
_DenviroStatusOverVoltage_Object = MibScalar
denviroStatusOverVoltage = _DenviroStatusOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 2, 28),
    _DenviroStatusOverVoltage_Type()
)
denviroStatusOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusOverVoltage.setStatus("mandatory")
_DenviroDeltaBus_ObjectIdentity = ObjectIdentity
denviroDeltaBus = _DenviroDeltaBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3)
)
_DenviroEMS1000DBNum_Type = Integer32
_DenviroEMS1000DBNum_Object = MibScalar
denviroEMS1000DBNum = _DenviroEMS1000DBNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 1),
    _DenviroEMS1000DBNum_Type()
)
denviroEMS1000DBNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBNum.setStatus("mandatory")
_DenviroEMS1000DBTable_Object = MibTable
denviroEMS1000DBTable = _DenviroEMS1000DBTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2)
)
if mibBuilder.loadTexts:
    denviroEMS1000DBTable.setStatus("mandatory")
_DenviroEMS1000DBEntry_Object = MibTableRow
denviroEMS1000DBEntry = _DenviroEMS1000DBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1)
)
denviroEMS1000DBEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroEMS1000DBID"),
)
if mibBuilder.loadTexts:
    denviroEMS1000DBEntry.setStatus("mandatory")


class _DenviroEMS1000DBTitle_Type(DisplayString):
    """Custom type denviroEMS1000DBTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1000DBTitle_Type.__name__ = "DisplayString"
_DenviroEMS1000DBTitle_Object = MibTableColumn
denviroEMS1000DBTitle = _DenviroEMS1000DBTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 1),
    _DenviroEMS1000DBTitle_Type()
)
denviroEMS1000DBTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBTitle.setStatus("mandatory")
_DenviroEMS1000DBTemperature_Type = Integer32
_DenviroEMS1000DBTemperature_Object = MibTableColumn
denviroEMS1000DBTemperature = _DenviroEMS1000DBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 2),
    _DenviroEMS1000DBTemperature_Type()
)
denviroEMS1000DBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBTemperature.setStatus("mandatory")
_DenviroEMS1000DBHumidity_Type = Integer32
_DenviroEMS1000DBHumidity_Object = MibTableColumn
denviroEMS1000DBHumidity = _DenviroEMS1000DBHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 3),
    _DenviroEMS1000DBHumidity_Type()
)
denviroEMS1000DBHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidity.setStatus("mandatory")


class _DenviroEMS1000DBInput1_Type(Integer32):
    """Custom type denviroEMS1000DBInput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1000DBInput1_Type.__name__ = "Integer32"
_DenviroEMS1000DBInput1_Object = MibTableColumn
denviroEMS1000DBInput1 = _DenviroEMS1000DBInput1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 4),
    _DenviroEMS1000DBInput1_Type()
)
denviroEMS1000DBInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBInput1.setStatus("mandatory")


class _DenviroEMS1000DBInput2_Type(Integer32):
    """Custom type denviroEMS1000DBInput2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1000DBInput2_Type.__name__ = "Integer32"
_DenviroEMS1000DBInput2_Object = MibTableColumn
denviroEMS1000DBInput2 = _DenviroEMS1000DBInput2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 5),
    _DenviroEMS1000DBInput2_Type()
)
denviroEMS1000DBInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBInput2.setStatus("mandatory")


class _DenviroEMS1000DBInput3_Type(Integer32):
    """Custom type denviroEMS1000DBInput3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1000DBInput3_Type.__name__ = "Integer32"
_DenviroEMS1000DBInput3_Object = MibTableColumn
denviroEMS1000DBInput3 = _DenviroEMS1000DBInput3_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 6),
    _DenviroEMS1000DBInput3_Type()
)
denviroEMS1000DBInput3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBInput3.setStatus("mandatory")


class _DenviroEMS1000DBInput4_Type(Integer32):
    """Custom type denviroEMS1000DBInput4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1000DBInput4_Type.__name__ = "Integer32"
_DenviroEMS1000DBInput4_Object = MibTableColumn
denviroEMS1000DBInput4 = _DenviroEMS1000DBInput4_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 7),
    _DenviroEMS1000DBInput4_Type()
)
denviroEMS1000DBInput4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBInput4.setStatus("mandatory")


class _DenviroEMS1000DBIn1Title_Type(DisplayString):
    """Custom type denviroEMS1000DBIn1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1000DBIn1Title_Type.__name__ = "DisplayString"
_DenviroEMS1000DBIn1Title_Object = MibTableColumn
denviroEMS1000DBIn1Title = _DenviroEMS1000DBIn1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 8),
    _DenviroEMS1000DBIn1Title_Type()
)
denviroEMS1000DBIn1Title.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBIn1Title.setStatus("mandatory")


class _DenviroEMS1000DBIn2Title_Type(DisplayString):
    """Custom type denviroEMS1000DBIn2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1000DBIn2Title_Type.__name__ = "DisplayString"
_DenviroEMS1000DBIn2Title_Object = MibTableColumn
denviroEMS1000DBIn2Title = _DenviroEMS1000DBIn2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 9),
    _DenviroEMS1000DBIn2Title_Type()
)
denviroEMS1000DBIn2Title.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBIn2Title.setStatus("mandatory")


class _DenviroEMS1000DBIn3Title_Type(DisplayString):
    """Custom type denviroEMS1000DBIn3Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1000DBIn3Title_Type.__name__ = "DisplayString"
_DenviroEMS1000DBIn3Title_Object = MibTableColumn
denviroEMS1000DBIn3Title = _DenviroEMS1000DBIn3Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 10),
    _DenviroEMS1000DBIn3Title_Type()
)
denviroEMS1000DBIn3Title.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBIn3Title.setStatus("mandatory")


class _DenviroEMS1000DBIn4Title_Type(DisplayString):
    """Custom type denviroEMS1000DBIn4Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1000DBIn4Title_Type.__name__ = "DisplayString"
_DenviroEMS1000DBIn4Title_Object = MibTableColumn
denviroEMS1000DBIn4Title = _DenviroEMS1000DBIn4Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 11),
    _DenviroEMS1000DBIn4Title_Type()
)
denviroEMS1000DBIn4Title.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBIn4Title.setStatus("mandatory")


class _DenviroEMS1000DBStatusComm_Type(Integer32):
    """Custom type denviroEMS1000DBStatusComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("connect", 2))
    )


_DenviroEMS1000DBStatusComm_Type.__name__ = "Integer32"
_DenviroEMS1000DBStatusComm_Object = MibTableColumn
denviroEMS1000DBStatusComm = _DenviroEMS1000DBStatusComm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 12),
    _DenviroEMS1000DBStatusComm_Type()
)
denviroEMS1000DBStatusComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBStatusComm.setStatus("mandatory")


class _DenviroEMS1000DBStatusTemperature_Type(Integer32):
    """Custom type denviroEMS1000DBStatusTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1000DBStatusTemperature_Type.__name__ = "Integer32"
_DenviroEMS1000DBStatusTemperature_Object = MibTableColumn
denviroEMS1000DBStatusTemperature = _DenviroEMS1000DBStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 13),
    _DenviroEMS1000DBStatusTemperature_Type()
)
denviroEMS1000DBStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBStatusTemperature.setStatus("mandatory")


class _DenviroEMS1000DBStatusHumidity_Type(Integer32):
    """Custom type denviroEMS1000DBStatusHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1000DBStatusHumidity_Type.__name__ = "Integer32"
_DenviroEMS1000DBStatusHumidity_Object = MibTableColumn
denviroEMS1000DBStatusHumidity = _DenviroEMS1000DBStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 14),
    _DenviroEMS1000DBStatusHumidity_Type()
)
denviroEMS1000DBStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBStatusHumidity.setStatus("mandatory")


class _DenviroEMS1000DBID_Type(Integer32):
    """Custom type denviroEMS1000DBID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DenviroEMS1000DBID_Type.__name__ = "Integer32"
_DenviroEMS1000DBID_Object = MibTableColumn
denviroEMS1000DBID = _DenviroEMS1000DBID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 15),
    _DenviroEMS1000DBID_Type()
)
denviroEMS1000DBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1000DBID.setStatus("mandatory")
_DenviroEMS1000DBTemperatureWarningThreshold_Type = Integer32
_DenviroEMS1000DBTemperatureWarningThreshold_Object = MibTableColumn
denviroEMS1000DBTemperatureWarningThreshold = _DenviroEMS1000DBTemperatureWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 16),
    _DenviroEMS1000DBTemperatureWarningThreshold_Type()
)
denviroEMS1000DBTemperatureWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBTemperatureWarningThreshold.setStatus("mandatory")
_DenviroEMS1000DBTemperatureWarningRecoverThreshold_Type = Integer32
_DenviroEMS1000DBTemperatureWarningRecoverThreshold_Object = MibTableColumn
denviroEMS1000DBTemperatureWarningRecoverThreshold = _DenviroEMS1000DBTemperatureWarningRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 17),
    _DenviroEMS1000DBTemperatureWarningRecoverThreshold_Type()
)
denviroEMS1000DBTemperatureWarningRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBTemperatureWarningRecoverThreshold.setStatus("mandatory")
_DenviroEMS1000DBTemperatureAlarmThreshold_Type = Integer32
_DenviroEMS1000DBTemperatureAlarmThreshold_Object = MibTableColumn
denviroEMS1000DBTemperatureAlarmThreshold = _DenviroEMS1000DBTemperatureAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 18),
    _DenviroEMS1000DBTemperatureAlarmThreshold_Type()
)
denviroEMS1000DBTemperatureAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBTemperatureAlarmThreshold.setStatus("mandatory")
_DenviroEMS1000DBTemperatureAlarmRecoverThreshold_Type = Integer32
_DenviroEMS1000DBTemperatureAlarmRecoverThreshold_Object = MibTableColumn
denviroEMS1000DBTemperatureAlarmRecoverThreshold = _DenviroEMS1000DBTemperatureAlarmRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 19),
    _DenviroEMS1000DBTemperatureAlarmRecoverThreshold_Type()
)
denviroEMS1000DBTemperatureAlarmRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBTemperatureAlarmRecoverThreshold.setStatus("mandatory")
_DenviroEMS1000DBHumidityWarningThreshold_Type = Integer32
_DenviroEMS1000DBHumidityWarningThreshold_Object = MibTableColumn
denviroEMS1000DBHumidityWarningThreshold = _DenviroEMS1000DBHumidityWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 20),
    _DenviroEMS1000DBHumidityWarningThreshold_Type()
)
denviroEMS1000DBHumidityWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityWarningThreshold.setStatus("mandatory")
_DenviroEMS1000DBHumidityWarningRecoverThreshold_Type = Integer32
_DenviroEMS1000DBHumidityWarningRecoverThreshold_Object = MibTableColumn
denviroEMS1000DBHumidityWarningRecoverThreshold = _DenviroEMS1000DBHumidityWarningRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 21),
    _DenviroEMS1000DBHumidityWarningRecoverThreshold_Type()
)
denviroEMS1000DBHumidityWarningRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityWarningRecoverThreshold.setStatus("mandatory")
_DenviroEMS1000DBHumidityAlarmThreshold_Type = Integer32
_DenviroEMS1000DBHumidityAlarmThreshold_Object = MibTableColumn
denviroEMS1000DBHumidityAlarmThreshold = _DenviroEMS1000DBHumidityAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 22),
    _DenviroEMS1000DBHumidityAlarmThreshold_Type()
)
denviroEMS1000DBHumidityAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityAlarmThreshold.setStatus("mandatory")
_DenviroEMS1000DBHumidityAlarmRecoverThreshold_Type = Integer32
_DenviroEMS1000DBHumidityAlarmRecoverThreshold_Object = MibTableColumn
denviroEMS1000DBHumidityAlarmRecoverThreshold = _DenviroEMS1000DBHumidityAlarmRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 2, 1, 23),
    _DenviroEMS1000DBHumidityAlarmRecoverThreshold_Type()
)
denviroEMS1000DBHumidityAlarmRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityAlarmRecoverThreshold.setStatus("mandatory")
_DenviroEMS1100DBNum_Type = Integer32
_DenviroEMS1100DBNum_Object = MibScalar
denviroEMS1100DBNum = _DenviroEMS1100DBNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 3),
    _DenviroEMS1100DBNum_Type()
)
denviroEMS1100DBNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1100DBNum.setStatus("mandatory")
_DenviroEMS1100DBTable_Object = MibTable
denviroEMS1100DBTable = _DenviroEMS1100DBTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4)
)
if mibBuilder.loadTexts:
    denviroEMS1100DBTable.setStatus("mandatory")
_DenviroEMS1100DBEntry_Object = MibTableRow
denviroEMS1100DBEntry = _DenviroEMS1100DBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1)
)
denviroEMS1100DBEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroEMS1100DBID"),
)
if mibBuilder.loadTexts:
    denviroEMS1100DBEntry.setStatus("mandatory")


class _DenviroEMS1100DBID_Type(Integer32):
    """Custom type denviroEMS1100DBID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DenviroEMS1100DBID_Type.__name__ = "Integer32"
_DenviroEMS1100DBID_Object = MibTableColumn
denviroEMS1100DBID = _DenviroEMS1100DBID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 1),
    _DenviroEMS1100DBID_Type()
)
denviroEMS1100DBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1100DBID.setStatus("mandatory")


class _DenviroEMS1100DBStatusComm_Type(Integer32):
    """Custom type denviroEMS1100DBStatusComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("connect", 2))
    )


_DenviroEMS1100DBStatusComm_Type.__name__ = "Integer32"
_DenviroEMS1100DBStatusComm_Object = MibTableColumn
denviroEMS1100DBStatusComm = _DenviroEMS1100DBStatusComm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 2),
    _DenviroEMS1100DBStatusComm_Type()
)
denviroEMS1100DBStatusComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1100DBStatusComm.setStatus("mandatory")


class _DenviroEMS1100DBTitle_Type(DisplayString):
    """Custom type denviroEMS1100DBTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1100DBTitle_Type.__name__ = "DisplayString"
_DenviroEMS1100DBTitle_Object = MibTableColumn
denviroEMS1100DBTitle = _DenviroEMS1100DBTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 3),
    _DenviroEMS1100DBTitle_Type()
)
denviroEMS1100DBTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBTitle.setStatus("mandatory")


class _DenviroEMS1100DBDO1Title_Type(DisplayString):
    """Custom type denviroEMS1100DBDO1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1100DBDO1Title_Type.__name__ = "DisplayString"
_DenviroEMS1100DBDO1Title_Object = MibTableColumn
denviroEMS1100DBDO1Title = _DenviroEMS1100DBDO1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 4),
    _DenviroEMS1100DBDO1Title_Type()
)
denviroEMS1100DBDO1Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO1Title.setStatus("mandatory")


class _DenviroEMS1100DBDO2Title_Type(DisplayString):
    """Custom type denviroEMS1100DBDO2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1100DBDO2Title_Type.__name__ = "DisplayString"
_DenviroEMS1100DBDO2Title_Object = MibTableColumn
denviroEMS1100DBDO2Title = _DenviroEMS1100DBDO2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 5),
    _DenviroEMS1100DBDO2Title_Type()
)
denviroEMS1100DBDO2Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO2Title.setStatus("mandatory")


class _DenviroEMS1100DBDO3Title_Type(DisplayString):
    """Custom type denviroEMS1100DBDO3Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1100DBDO3Title_Type.__name__ = "DisplayString"
_DenviroEMS1100DBDO3Title_Object = MibTableColumn
denviroEMS1100DBDO3Title = _DenviroEMS1100DBDO3Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 6),
    _DenviroEMS1100DBDO3Title_Type()
)
denviroEMS1100DBDO3Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO3Title.setStatus("mandatory")


class _DenviroEMS1100DBDO4Title_Type(DisplayString):
    """Custom type denviroEMS1100DBDO4Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1100DBDO4Title_Type.__name__ = "DisplayString"
_DenviroEMS1100DBDO4Title_Object = MibTableColumn
denviroEMS1100DBDO4Title = _DenviroEMS1100DBDO4Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 7),
    _DenviroEMS1100DBDO4Title_Type()
)
denviroEMS1100DBDO4Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO4Title.setStatus("mandatory")


class _DenviroEMS1100DBDO1Status_Type(Integer32):
    """Custom type denviroEMS1100DBDO1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroEMS1100DBDO1Status_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO1Status_Object = MibTableColumn
denviroEMS1100DBDO1Status = _DenviroEMS1100DBDO1Status_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 8),
    _DenviroEMS1100DBDO1Status_Type()
)
denviroEMS1100DBDO1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO1Status.setStatus("mandatory")


class _DenviroEMS1100DBDO2Status_Type(Integer32):
    """Custom type denviroEMS1100DBDO2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroEMS1100DBDO2Status_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO2Status_Object = MibTableColumn
denviroEMS1100DBDO2Status = _DenviroEMS1100DBDO2Status_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 9),
    _DenviroEMS1100DBDO2Status_Type()
)
denviroEMS1100DBDO2Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO2Status.setStatus("mandatory")


class _DenviroEMS1100DBDO3Status_Type(Integer32):
    """Custom type denviroEMS1100DBDO3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroEMS1100DBDO3Status_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO3Status_Object = MibTableColumn
denviroEMS1100DBDO3Status = _DenviroEMS1100DBDO3Status_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 10),
    _DenviroEMS1100DBDO3Status_Type()
)
denviroEMS1100DBDO3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO3Status.setStatus("mandatory")


class _DenviroEMS1100DBDO4Status_Type(Integer32):
    """Custom type denviroEMS1100DBDO4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroEMS1100DBDO4Status_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO4Status_Object = MibTableColumn
denviroEMS1100DBDO4Status = _DenviroEMS1100DBDO4Status_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 11),
    _DenviroEMS1100DBDO4Status_Type()
)
denviroEMS1100DBDO4Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO4Status.setStatus("mandatory")


class _DenviroEMS1100DBDO1Manual_Type(Integer32):
    """Custom type denviroEMS1100DBDO1Manual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroEMS1100DBDO1Manual_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO1Manual_Object = MibTableColumn
denviroEMS1100DBDO1Manual = _DenviroEMS1100DBDO1Manual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 12),
    _DenviroEMS1100DBDO1Manual_Type()
)
denviroEMS1100DBDO1Manual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO1Manual.setStatus("mandatory")


class _DenviroEMS1100DBDO2Manual_Type(Integer32):
    """Custom type denviroEMS1100DBDO2Manual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroEMS1100DBDO2Manual_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO2Manual_Object = MibTableColumn
denviroEMS1100DBDO2Manual = _DenviroEMS1100DBDO2Manual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 13),
    _DenviroEMS1100DBDO2Manual_Type()
)
denviroEMS1100DBDO2Manual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO2Manual.setStatus("mandatory")


class _DenviroEMS1100DBDO3Manual_Type(Integer32):
    """Custom type denviroEMS1100DBDO3Manual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroEMS1100DBDO3Manual_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO3Manual_Object = MibTableColumn
denviroEMS1100DBDO3Manual = _DenviroEMS1100DBDO3Manual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 14),
    _DenviroEMS1100DBDO3Manual_Type()
)
denviroEMS1100DBDO3Manual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO3Manual.setStatus("mandatory")


class _DenviroEMS1100DBDO4Manual_Type(Integer32):
    """Custom type denviroEMS1100DBDO4Manual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroEMS1100DBDO4Manual_Type.__name__ = "Integer32"
_DenviroEMS1100DBDO4Manual_Object = MibTableColumn
denviroEMS1100DBDO4Manual = _DenviroEMS1100DBDO4Manual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 4, 1, 15),
    _DenviroEMS1100DBDO4Manual_Type()
)
denviroEMS1100DBDO4Manual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1100DBDO4Manual.setStatus("mandatory")
_DenviroEMS1200DBNum_Type = Integer32
_DenviroEMS1200DBNum_Object = MibScalar
denviroEMS1200DBNum = _DenviroEMS1200DBNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 5),
    _DenviroEMS1200DBNum_Type()
)
denviroEMS1200DBNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBNum.setStatus("mandatory")
_DenviroEMS1200DBTable_Object = MibTable
denviroEMS1200DBTable = _DenviroEMS1200DBTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6)
)
if mibBuilder.loadTexts:
    denviroEMS1200DBTable.setStatus("mandatory")
_DenviroEMS1200DBEntry_Object = MibTableRow
denviroEMS1200DBEntry = _DenviroEMS1200DBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1)
)
denviroEMS1200DBEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroEMS1200DBID"),
)
if mibBuilder.loadTexts:
    denviroEMS1200DBEntry.setStatus("mandatory")


class _DenviroEMS1200DBID_Type(Integer32):
    """Custom type denviroEMS1200DBID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DenviroEMS1200DBID_Type.__name__ = "Integer32"
_DenviroEMS1200DBID_Object = MibTableColumn
denviroEMS1200DBID = _DenviroEMS1200DBID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 1),
    _DenviroEMS1200DBID_Type()
)
denviroEMS1200DBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBID.setStatus("mandatory")


class _DenviroEMS1200DBStatusComm_Type(Integer32):
    """Custom type denviroEMS1200DBStatusComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("connect", 2))
    )


_DenviroEMS1200DBStatusComm_Type.__name__ = "Integer32"
_DenviroEMS1200DBStatusComm_Object = MibTableColumn
denviroEMS1200DBStatusComm = _DenviroEMS1200DBStatusComm_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 2),
    _DenviroEMS1200DBStatusComm_Type()
)
denviroEMS1200DBStatusComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBStatusComm.setStatus("mandatory")


class _DenviroEMS1200DBTitle_Type(DisplayString):
    """Custom type denviroEMS1200DBTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1200DBTitle_Type.__name__ = "DisplayString"
_DenviroEMS1200DBTitle_Object = MibTableColumn
denviroEMS1200DBTitle = _DenviroEMS1200DBTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 3),
    _DenviroEMS1200DBTitle_Type()
)
denviroEMS1200DBTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBTitle.setStatus("mandatory")


class _DenviroEMS1200DBAI1Title_Type(DisplayString):
    """Custom type denviroEMS1200DBAI1Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1200DBAI1Title_Type.__name__ = "DisplayString"
_DenviroEMS1200DBAI1Title_Object = MibTableColumn
denviroEMS1200DBAI1Title = _DenviroEMS1200DBAI1Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 4),
    _DenviroEMS1200DBAI1Title_Type()
)
denviroEMS1200DBAI1Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBAI1Title.setStatus("mandatory")


class _DenviroEMS1200DBAI2Title_Type(DisplayString):
    """Custom type denviroEMS1200DBAI2Title based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1200DBAI2Title_Type.__name__ = "DisplayString"
_DenviroEMS1200DBAI2Title_Object = MibTableColumn
denviroEMS1200DBAI2Title = _DenviroEMS1200DBAI2Title_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 5),
    _DenviroEMS1200DBAI2Title_Type()
)
denviroEMS1200DBAI2Title.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBAI2Title.setStatus("mandatory")


class _DenviroEMS1200DBLeakageTitle_Type(DisplayString):
    """Custom type denviroEMS1200DBLeakageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1200DBLeakageTitle_Type.__name__ = "DisplayString"
_DenviroEMS1200DBLeakageTitle_Object = MibTableColumn
denviroEMS1200DBLeakageTitle = _DenviroEMS1200DBLeakageTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 6),
    _DenviroEMS1200DBLeakageTitle_Type()
)
denviroEMS1200DBLeakageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBLeakageTitle.setStatus("mandatory")


class _DenviroEMS1200DBAOTitle_Type(DisplayString):
    """Custom type denviroEMS1200DBAOTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroEMS1200DBAOTitle_Type.__name__ = "DisplayString"
_DenviroEMS1200DBAOTitle_Object = MibTableColumn
denviroEMS1200DBAOTitle = _DenviroEMS1200DBAOTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 7),
    _DenviroEMS1200DBAOTitle_Type()
)
denviroEMS1200DBAOTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBAOTitle.setStatus("mandatory")
_DenviroEMS1200DBAI1Value_Type = Integer32
_DenviroEMS1200DBAI1Value_Object = MibTableColumn
denviroEMS1200DBAI1Value = _DenviroEMS1200DBAI1Value_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 8),
    _DenviroEMS1200DBAI1Value_Type()
)
denviroEMS1200DBAI1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBAI1Value.setStatus("mandatory")
_DenviroEMS1200DBAI2Value_Type = Integer32
_DenviroEMS1200DBAI2Value_Object = MibTableColumn
denviroEMS1200DBAI2Value = _DenviroEMS1200DBAI2Value_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 9),
    _DenviroEMS1200DBAI2Value_Type()
)
denviroEMS1200DBAI2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBAI2Value.setStatus("mandatory")


class _DenviroEMS1200DBAI1Status_Type(Integer32):
    """Custom type denviroEMS1200DBAI1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1200DBAI1Status_Type.__name__ = "Integer32"
_DenviroEMS1200DBAI1Status_Object = MibTableColumn
denviroEMS1200DBAI1Status = _DenviroEMS1200DBAI1Status_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 10),
    _DenviroEMS1200DBAI1Status_Type()
)
denviroEMS1200DBAI1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBAI1Status.setStatus("mandatory")


class _DenviroEMS1200DBAI2Status_Type(Integer32):
    """Custom type denviroEMS1200DBAI2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1200DBAI2Status_Type.__name__ = "Integer32"
_DenviroEMS1200DBAI2Status_Object = MibTableColumn
denviroEMS1200DBAI2Status = _DenviroEMS1200DBAI2Status_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 11),
    _DenviroEMS1200DBAI2Status_Type()
)
denviroEMS1200DBAI2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBAI2Status.setStatus("mandatory")


class _DenviroEMS1200DBLeakageLevel_Type(Integer32):
    """Custom type denviroEMS1200DBLeakageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("middle", 2),
          ("high", 3))
    )


_DenviroEMS1200DBLeakageLevel_Type.__name__ = "Integer32"
_DenviroEMS1200DBLeakageLevel_Object = MibTableColumn
denviroEMS1200DBLeakageLevel = _DenviroEMS1200DBLeakageLevel_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 12),
    _DenviroEMS1200DBLeakageLevel_Type()
)
denviroEMS1200DBLeakageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBLeakageLevel.setStatus("mandatory")


class _DenviroEMS1200DBLeakageBuzzer_Type(Integer32):
    """Custom type denviroEMS1200DBLeakageBuzzer based on Integer32"""
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


_DenviroEMS1200DBLeakageBuzzer_Type.__name__ = "Integer32"
_DenviroEMS1200DBLeakageBuzzer_Object = MibTableColumn
denviroEMS1200DBLeakageBuzzer = _DenviroEMS1200DBLeakageBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 13),
    _DenviroEMS1200DBLeakageBuzzer_Type()
)
denviroEMS1200DBLeakageBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBLeakageBuzzer.setStatus("mandatory")


class _DenviroEMS1200DBLeakageStatus_Type(Integer32):
    """Custom type denviroEMS1200DBLeakageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroEMS1200DBLeakageStatus_Type.__name__ = "Integer32"
_DenviroEMS1200DBLeakageStatus_Object = MibTableColumn
denviroEMS1200DBLeakageStatus = _DenviroEMS1200DBLeakageStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 14),
    _DenviroEMS1200DBLeakageStatus_Type()
)
denviroEMS1200DBLeakageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBLeakageStatus.setStatus("mandatory")
_DenviroEMS1200DBAOControl_Type = Integer32
_DenviroEMS1200DBAOControl_Object = MibTableColumn
denviroEMS1200DBAOControl = _DenviroEMS1200DBAOControl_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 15),
    _DenviroEMS1200DBAOControl_Type()
)
denviroEMS1200DBAOControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBAOControl.setStatus("mandatory")


class _DenviroEMS1200DBAOStatus_Type(Integer32):
    """Custom type denviroEMS1200DBAOStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_DenviroEMS1200DBAOStatus_Type.__name__ = "Integer32"
_DenviroEMS1200DBAOStatus_Object = MibTableColumn
denviroEMS1200DBAOStatus = _DenviroEMS1200DBAOStatus_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 16),
    _DenviroEMS1200DBAOStatus_Type()
)
denviroEMS1200DBAOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroEMS1200DBAOStatus.setStatus("mandatory")


class _DenviroEMS1200DBAOManual_Type(Integer32):
    """Custom type denviroEMS1200DBAOManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroEMS1200DBAOManual_Type.__name__ = "Integer32"
_DenviroEMS1200DBAOManual_Object = MibTableColumn
denviroEMS1200DBAOManual = _DenviroEMS1200DBAOManual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 3, 6, 1, 17),
    _DenviroEMS1200DBAOManual_Type()
)
denviroEMS1200DBAOManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroEMS1200DBAOManual.setStatus("mandatory")
_DenviroRS485_ObjectIdentity = ObjectIdentity
denviroRS485 = _DenviroRS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4)
)
_DenviroNum485_Type = Integer32
_DenviroNum485_Object = MibScalar
denviroNum485 = _DenviroNum485_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 1),
    _DenviroNum485_Type()
)
denviroNum485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroNum485.setStatus("mandatory")
_Denviro485Table_Object = MibTable
denviro485Table = _Denviro485Table_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 2)
)
if mibBuilder.loadTexts:
    denviro485Table.setStatus("mandatory")
_Denviro485Entry_Object = MibTableRow
denviro485Entry = _Denviro485Entry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 2, 1)
)
denviro485Entry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviro485Port"),
    (0, "DeltaEnviro-MIB", "denviroID485"),
)
if mibBuilder.loadTexts:
    denviro485Entry.setStatus("mandatory")


class _DenviroTitle485_Type(DisplayString):
    """Custom type denviroTitle485 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroTitle485_Type.__name__ = "DisplayString"
_DenviroTitle485_Object = MibTableColumn
denviroTitle485 = _DenviroTitle485_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 2, 1, 1),
    _DenviroTitle485_Type()
)
denviroTitle485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroTitle485.setStatus("mandatory")


class _DenviroCommLost_Type(Integer32):
    """Custom type denviroCommLost based on Integer32"""
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


_DenviroCommLost_Type.__name__ = "Integer32"
_DenviroCommLost_Object = MibTableColumn
denviroCommLost = _DenviroCommLost_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 2, 1, 2),
    _DenviroCommLost_Type()
)
denviroCommLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroCommLost.setStatus("mandatory")


class _Denviro485Port_Type(Integer32):
    """Custom type denviro485Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs485-1", 1),
          ("rs485-2", 2))
    )


_Denviro485Port_Type.__name__ = "Integer32"
_Denviro485Port_Object = MibTableColumn
denviro485Port = _Denviro485Port_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 2, 1, 3),
    _Denviro485Port_Type()
)
denviro485Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviro485Port.setStatus("mandatory")


class _DenviroID485_Type(Integer32):
    """Custom type denviroID485 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroID485_Type.__name__ = "Integer32"
_DenviroID485_Object = MibTableColumn
denviroID485 = _DenviroID485_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 2, 1, 4),
    _DenviroID485_Type()
)
denviroID485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroID485.setStatus("mandatory")
_DenviroValueTable_Object = MibTable
denviroValueTable = _DenviroValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3)
)
if mibBuilder.loadTexts:
    denviroValueTable.setStatus("mandatory")
_DenviroValueEntry_Object = MibTableRow
denviroValueEntry = _DenviroValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1)
)
denviroValueEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroValue485Port"),
    (0, "DeltaEnviro-MIB", "denviroValueID485"),
    (0, "DeltaEnviro-MIB", "denviroValueIndex"),
)
if mibBuilder.loadTexts:
    denviroValueEntry.setStatus("mandatory")


class _DenviroValueTitle_Type(DisplayString):
    """Custom type denviroValueTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroValueTitle_Type.__name__ = "DisplayString"
_DenviroValueTitle_Object = MibTableColumn
denviroValueTitle = _DenviroValueTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 1),
    _DenviroValueTitle_Type()
)
denviroValueTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroValueTitle.setStatus("mandatory")
_DenviroValueValue_Type = Integer32
_DenviroValueValue_Object = MibTableColumn
denviroValueValue = _DenviroValueValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 2),
    _DenviroValueValue_Type()
)
denviroValueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroValueValue.setStatus("mandatory")
_DenviroValueScaleExp_Type = Integer32
_DenviroValueScaleExp_Object = MibTableColumn
denviroValueScaleExp = _DenviroValueScaleExp_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 3),
    _DenviroValueScaleExp_Type()
)
denviroValueScaleExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroValueScaleExp.setStatus("mandatory")


class _DenviroValueUnitString_Type(DisplayString):
    """Custom type denviroValueUnitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DenviroValueUnitString_Type.__name__ = "DisplayString"
_DenviroValueUnitString_Object = MibTableColumn
denviroValueUnitString = _DenviroValueUnitString_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 4),
    _DenviroValueUnitString_Type()
)
denviroValueUnitString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroValueUnitString.setStatus("mandatory")


class _DenviroValue485Port_Type(Integer32):
    """Custom type denviroValue485Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs485-1", 1),
          ("rs485-2", 2))
    )


_DenviroValue485Port_Type.__name__ = "Integer32"
_DenviroValue485Port_Object = MibTableColumn
denviroValue485Port = _DenviroValue485Port_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 5),
    _DenviroValue485Port_Type()
)
denviroValue485Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroValue485Port.setStatus("mandatory")


class _DenviroValueID485_Type(Integer32):
    """Custom type denviroValueID485 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroValueID485_Type.__name__ = "Integer32"
_DenviroValueID485_Object = MibTableColumn
denviroValueID485 = _DenviroValueID485_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 6),
    _DenviroValueID485_Type()
)
denviroValueID485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroValueID485.setStatus("mandatory")


class _DenviroValueIndex_Type(Integer32):
    """Custom type denviroValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DenviroValueIndex_Type.__name__ = "Integer32"
_DenviroValueIndex_Object = MibTableColumn
denviroValueIndex = _DenviroValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 3, 1, 7),
    _DenviroValueIndex_Type()
)
denviroValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroValueIndex.setStatus("mandatory")
_DenviroStatusTable_Object = MibTable
denviroStatusTable = _DenviroStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4)
)
if mibBuilder.loadTexts:
    denviroStatusTable.setStatus("mandatory")
_DenviroStatusEntry_Object = MibTableRow
denviroStatusEntry = _DenviroStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4, 1)
)
denviroStatusEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroStatus485Port"),
    (0, "DeltaEnviro-MIB", "denviroStatusID485"),
    (0, "DeltaEnviro-MIB", "denviroStatusIndex"),
)
if mibBuilder.loadTexts:
    denviroStatusEntry.setStatus("mandatory")


class _DenviroStatusTitle_Type(DisplayString):
    """Custom type denviroStatusTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroStatusTitle_Type.__name__ = "DisplayString"
_DenviroStatusTitle_Object = MibTableColumn
denviroStatusTitle = _DenviroStatusTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4, 1, 1),
    _DenviroStatusTitle_Type()
)
denviroStatusTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusTitle.setStatus("mandatory")


class _DenviroStatusValue_Type(Integer32):
    """Custom type denviroStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("alarm", 2),
          ("normal", 3))
    )


_DenviroStatusValue_Type.__name__ = "Integer32"
_DenviroStatusValue_Object = MibTableColumn
denviroStatusValue = _DenviroStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4, 1, 2),
    _DenviroStatusValue_Type()
)
denviroStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusValue.setStatus("mandatory")


class _DenviroStatus485Port_Type(Integer32):
    """Custom type denviroStatus485Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs485-1", 1),
          ("rs485-2", 2))
    )


_DenviroStatus485Port_Type.__name__ = "Integer32"
_DenviroStatus485Port_Object = MibTableColumn
denviroStatus485Port = _DenviroStatus485Port_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4, 1, 3),
    _DenviroStatus485Port_Type()
)
denviroStatus485Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatus485Port.setStatus("mandatory")


class _DenviroStatusID485_Type(Integer32):
    """Custom type denviroStatusID485 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroStatusID485_Type.__name__ = "Integer32"
_DenviroStatusID485_Object = MibTableColumn
denviroStatusID485 = _DenviroStatusID485_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4, 1, 4),
    _DenviroStatusID485_Type()
)
denviroStatusID485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroStatusID485.setStatus("mandatory")


class _DenviroStatusIndex_Type(Integer32):
    """Custom type denviroStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DenviroStatusIndex_Type.__name__ = "Integer32"
_DenviroStatusIndex_Object = MibTableColumn
denviroStatusIndex = _DenviroStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 4, 1, 5),
    _DenviroStatusIndex_Type()
)
denviroStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroStatusIndex.setStatus("mandatory")
_DenviroWritableValueTable_Object = MibTable
denviroWritableValueTable = _DenviroWritableValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5)
)
if mibBuilder.loadTexts:
    denviroWritableValueTable.setStatus("mandatory")
_DenviroWritableValueEntry_Object = MibTableRow
denviroWritableValueEntry = _DenviroWritableValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5, 1)
)
denviroWritableValueEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroWritableValue485Port"),
    (0, "DeltaEnviro-MIB", "denviroWritableValueID485"),
    (0, "DeltaEnviro-MIB", "denviroWritableValueIndex"),
)
if mibBuilder.loadTexts:
    denviroWritableValueEntry.setStatus("mandatory")


class _DenviroWritableValueTitle_Type(DisplayString):
    """Custom type denviroWritableValueTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroWritableValueTitle_Type.__name__ = "DisplayString"
_DenviroWritableValueTitle_Object = MibTableColumn
denviroWritableValueTitle = _DenviroWritableValueTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5, 1, 1),
    _DenviroWritableValueTitle_Type()
)
denviroWritableValueTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroWritableValueTitle.setStatus("mandatory")
_DenviroWritableValueValue_Type = Integer32
_DenviroWritableValueValue_Object = MibTableColumn
denviroWritableValueValue = _DenviroWritableValueValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5, 1, 2),
    _DenviroWritableValueValue_Type()
)
denviroWritableValueValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroWritableValueValue.setStatus("mandatory")


class _DenviroWritableValue485Port_Type(Integer32):
    """Custom type denviroWritableValue485Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs485-1", 1),
          ("rs485-2", 2))
    )


_DenviroWritableValue485Port_Type.__name__ = "Integer32"
_DenviroWritableValue485Port_Object = MibTableColumn
denviroWritableValue485Port = _DenviroWritableValue485Port_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5, 1, 3),
    _DenviroWritableValue485Port_Type()
)
denviroWritableValue485Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroWritableValue485Port.setStatus("mandatory")


class _DenviroWritableValueID485_Type(Integer32):
    """Custom type denviroWritableValueID485 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroWritableValueID485_Type.__name__ = "Integer32"
_DenviroWritableValueID485_Object = MibTableColumn
denviroWritableValueID485 = _DenviroWritableValueID485_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5, 1, 4),
    _DenviroWritableValueID485_Type()
)
denviroWritableValueID485.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroWritableValueID485.setStatus("mandatory")


class _DenviroWritableValueIndex_Type(Integer32):
    """Custom type denviroWritableValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DenviroWritableValueIndex_Type.__name__ = "Integer32"
_DenviroWritableValueIndex_Object = MibTableColumn
denviroWritableValueIndex = _DenviroWritableValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 4, 5, 1, 5),
    _DenviroWritableValueIndex_Type()
)
denviroWritableValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroWritableValueIndex.setStatus("mandatory")
_DenviroControl_ObjectIdentity = ObjectIdentity
denviroControl = _DenviroControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5)
)


class _DenviroCtrlHub1PwrManual_Type(Integer32):
    """Custom type denviroCtrlHub1PwrManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroCtrlHub1PwrManual_Type.__name__ = "Integer32"
_DenviroCtrlHub1PwrManual_Object = MibScalar
denviroCtrlHub1PwrManual = _DenviroCtrlHub1PwrManual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 1),
    _DenviroCtrlHub1PwrManual_Type()
)
denviroCtrlHub1PwrManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlHub1PwrManual.setStatus("mandatory")


class _DenviroCtrlHub2PwrManual_Type(Integer32):
    """Custom type denviroCtrlHub2PwrManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroCtrlHub2PwrManual_Type.__name__ = "Integer32"
_DenviroCtrlHub2PwrManual_Object = MibScalar
denviroCtrlHub2PwrManual = _DenviroCtrlHub2PwrManual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 2),
    _DenviroCtrlHub2PwrManual_Type()
)
denviroCtrlHub2PwrManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlHub2PwrManual.setStatus("mandatory")


class _DenviroCtrlHub1Pwr_Type(Integer32):
    """Custom type denviroCtrlHub1Pwr based on Integer32"""
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


_DenviroCtrlHub1Pwr_Type.__name__ = "Integer32"
_DenviroCtrlHub1Pwr_Object = MibScalar
denviroCtrlHub1Pwr = _DenviroCtrlHub1Pwr_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 3),
    _DenviroCtrlHub1Pwr_Type()
)
denviroCtrlHub1Pwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlHub1Pwr.setStatus("mandatory")


class _DenviroCtrlHub2Pwr_Type(Integer32):
    """Custom type denviroCtrlHub2Pwr based on Integer32"""
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


_DenviroCtrlHub2Pwr_Type.__name__ = "Integer32"
_DenviroCtrlHub2Pwr_Object = MibScalar
denviroCtrlHub2Pwr = _DenviroCtrlHub2Pwr_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 4),
    _DenviroCtrlHub2Pwr_Type()
)
denviroCtrlHub2Pwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlHub2Pwr.setStatus("mandatory")


class _DenviroCtrlDO1Manual_Type(Integer32):
    """Custom type denviroCtrlDO1Manual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroCtrlDO1Manual_Type.__name__ = "Integer32"
_DenviroCtrlDO1Manual_Object = MibScalar
denviroCtrlDO1Manual = _DenviroCtrlDO1Manual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 5),
    _DenviroCtrlDO1Manual_Type()
)
denviroCtrlDO1Manual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlDO1Manual.setStatus("mandatory")


class _DenviroCtrlDO2Manual_Type(Integer32):
    """Custom type denviroCtrlDO2Manual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_DenviroCtrlDO2Manual_Type.__name__ = "Integer32"
_DenviroCtrlDO2Manual_Object = MibScalar
denviroCtrlDO2Manual = _DenviroCtrlDO2Manual_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 6),
    _DenviroCtrlDO2Manual_Type()
)
denviroCtrlDO2Manual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlDO2Manual.setStatus("mandatory")


class _DenviroCtrlDO1_Type(Integer32):
    """Custom type denviroCtrlDO1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_DenviroCtrlDO1_Type.__name__ = "Integer32"
_DenviroCtrlDO1_Object = MibScalar
denviroCtrlDO1 = _DenviroCtrlDO1_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 7),
    _DenviroCtrlDO1_Type()
)
denviroCtrlDO1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlDO1.setStatus("mandatory")


class _DenviroCtrlDO2_Type(Integer32):
    """Custom type denviroCtrlDO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_DenviroCtrlDO2_Type.__name__ = "Integer32"
_DenviroCtrlDO2_Object = MibScalar
denviroCtrlDO2 = _DenviroCtrlDO2_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 5, 8),
    _DenviroCtrlDO2_Type()
)
denviroCtrlDO2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroCtrlDO2.setStatus("mandatory")
_DenviroPDU_ObjectIdentity = ObjectIdentity
denviroPDU = _DenviroPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 6)
)


class _DenviroPDUEnable_Type(Integer32):
    """Custom type denviroPDUEnable based on Integer32"""
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


_DenviroPDUEnable_Type.__name__ = "Integer32"
_DenviroPDUEnable_Object = MibScalar
denviroPDUEnable = _DenviroPDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 6, 1),
    _DenviroPDUEnable_Type()
)
denviroPDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroPDUEnable.setStatus("mandatory")
_DenviroReaction_ObjectIdentity = ObjectIdentity
denviroReaction = _DenviroReaction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7)
)
_DenviroReactionTable_Object = MibTable
denviroReactionTable = _DenviroReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 1)
)
if mibBuilder.loadTexts:
    denviroReactionTable.setStatus("mandatory")
_DenviroReactionEntry_Object = MibTableRow
denviroReactionEntry = _DenviroReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 1, 1)
)
denviroReactionEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroReactionRuleName"),
)
if mibBuilder.loadTexts:
    denviroReactionEntry.setStatus("mandatory")


class _DenviroReactionRuleName_Type(DisplayString):
    """Custom type denviroReactionRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroReactionRuleName_Type.__name__ = "DisplayString"
_DenviroReactionRuleName_Object = MibTableColumn
denviroReactionRuleName = _DenviroReactionRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 1, 1, 1),
    _DenviroReactionRuleName_Type()
)
denviroReactionRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroReactionRuleName.setStatus("mandatory")


class _DenviroReactionEnable_Type(Integer32):
    """Custom type denviroReactionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DenviroReactionEnable_Type.__name__ = "Integer32"
_DenviroReactionEnable_Object = MibTableColumn
denviroReactionEnable = _DenviroReactionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 1, 1, 2),
    _DenviroReactionEnable_Type()
)
denviroReactionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroReactionEnable.setStatus("mandatory")
_DenviroReactionCtrlValueTable_Object = MibTable
denviroReactionCtrlValueTable = _DenviroReactionCtrlValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 2)
)
if mibBuilder.loadTexts:
    denviroReactionCtrlValueTable.setStatus("mandatory")
_DenviroReactionCtrlValueEntry_Object = MibTableRow
denviroReactionCtrlValueEntry = _DenviroReactionCtrlValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 2, 1)
)
denviroReactionCtrlValueEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroReactionCtrlValueID"),
)
if mibBuilder.loadTexts:
    denviroReactionCtrlValueEntry.setStatus("mandatory")


class _DenviroReactionCtrlValueID_Type(Integer32):
    """Custom type denviroReactionCtrlValueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroReactionCtrlValueID_Type.__name__ = "Integer32"
_DenviroReactionCtrlValueID_Object = MibTableColumn
denviroReactionCtrlValueID = _DenviroReactionCtrlValueID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 2, 1, 1),
    _DenviroReactionCtrlValueID_Type()
)
denviroReactionCtrlValueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroReactionCtrlValueID.setStatus("mandatory")
_DenviroReactionCtrlValue_Type = Integer32
_DenviroReactionCtrlValue_Object = MibTableColumn
denviroReactionCtrlValue = _DenviroReactionCtrlValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 7, 2, 1, 2),
    _DenviroReactionCtrlValue_Type()
)
denviroReactionCtrlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroReactionCtrlValue.setStatus("mandatory")
_DenviroSNMPProtocol_ObjectIdentity = ObjectIdentity
denviroSNMPProtocol = _DenviroSNMPProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8)
)
_DenviroNumSNMPDevice_Type = Integer32
_DenviroNumSNMPDevice_Object = MibScalar
denviroNumSNMPDevice = _DenviroNumSNMPDevice_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 1),
    _DenviroNumSNMPDevice_Type()
)
denviroNumSNMPDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroNumSNMPDevice.setStatus("mandatory")
_DenviroSNMPDeviceTable_Object = MibTable
denviroSNMPDeviceTable = _DenviroSNMPDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2)
)
if mibBuilder.loadTexts:
    denviroSNMPDeviceTable.setStatus("mandatory")
_DenviroSNMPDeviceEntry_Object = MibTableRow
denviroSNMPDeviceEntry = _DenviroSNMPDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1)
)
denviroSNMPDeviceEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroSNMPDeviceIndex"),
)
if mibBuilder.loadTexts:
    denviroSNMPDeviceEntry.setStatus("mandatory")


class _DenviroSNMPDeviceIP_Type(DisplayString):
    """Custom type denviroSNMPDeviceIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroSNMPDeviceIP_Type.__name__ = "DisplayString"
_DenviroSNMPDeviceIP_Object = MibTableColumn
denviroSNMPDeviceIP = _DenviroSNMPDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1, 1),
    _DenviroSNMPDeviceIP_Type()
)
denviroSNMPDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPDeviceIP.setStatus("mandatory")
_DenviroSNMPDevicePort_Type = Integer32
_DenviroSNMPDevicePort_Object = MibTableColumn
denviroSNMPDevicePort = _DenviroSNMPDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1, 2),
    _DenviroSNMPDevicePort_Type()
)
denviroSNMPDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPDevicePort.setStatus("mandatory")


class _DenviroSNMPDeviceVersion_Type(DisplayString):
    """Custom type denviroSNMPDeviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroSNMPDeviceVersion_Type.__name__ = "DisplayString"
_DenviroSNMPDeviceVersion_Object = MibTableColumn
denviroSNMPDeviceVersion = _DenviroSNMPDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1, 3),
    _DenviroSNMPDeviceVersion_Type()
)
denviroSNMPDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPDeviceVersion.setStatus("mandatory")


class _DenviroSNMPDeviceCommunity_Type(DisplayString):
    """Custom type denviroSNMPDeviceCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroSNMPDeviceCommunity_Type.__name__ = "DisplayString"
_DenviroSNMPDeviceCommunity_Object = MibTableColumn
denviroSNMPDeviceCommunity = _DenviroSNMPDeviceCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1, 4),
    _DenviroSNMPDeviceCommunity_Type()
)
denviroSNMPDeviceCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPDeviceCommunity.setStatus("mandatory")


class _DenviroCommLink_Type(Integer32):
    """Custom type denviroCommLink based on Integer32"""
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


_DenviroCommLink_Type.__name__ = "Integer32"
_DenviroCommLink_Object = MibTableColumn
denviroCommLink = _DenviroCommLink_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1, 5),
    _DenviroCommLink_Type()
)
denviroCommLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroCommLink.setStatus("mandatory")


class _DenviroSNMPDeviceIndex_Type(Integer32):
    """Custom type denviroSNMPDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DenviroSNMPDeviceIndex_Type.__name__ = "Integer32"
_DenviroSNMPDeviceIndex_Object = MibTableColumn
denviroSNMPDeviceIndex = _DenviroSNMPDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 2, 1, 6),
    _DenviroSNMPDeviceIndex_Type()
)
denviroSNMPDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroSNMPDeviceIndex.setStatus("mandatory")
_DenviroSNMPProValueTable_Object = MibTable
denviroSNMPProValueTable = _DenviroSNMPProValueTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3)
)
if mibBuilder.loadTexts:
    denviroSNMPProValueTable.setStatus("mandatory")
_DenviroSNMPProValueEntry_Object = MibTableRow
denviroSNMPProValueEntry = _DenviroSNMPProValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1)
)
denviroSNMPProValueEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroSNMPProValueID"),
    (0, "DeltaEnviro-MIB", "denviroSNMPProValueIndex"),
)
if mibBuilder.loadTexts:
    denviroSNMPProValueEntry.setStatus("mandatory")


class _DenviroSNMPProValueTitle_Type(DisplayString):
    """Custom type denviroSNMPProValueTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroSNMPProValueTitle_Type.__name__ = "DisplayString"
_DenviroSNMPProValueTitle_Object = MibTableColumn
denviroSNMPProValueTitle = _DenviroSNMPProValueTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1, 1),
    _DenviroSNMPProValueTitle_Type()
)
denviroSNMPProValueTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProValueTitle.setStatus("mandatory")
_DenviroSNMPProValueValue_Type = Integer32
_DenviroSNMPProValueValue_Object = MibTableColumn
denviroSNMPProValueValue = _DenviroSNMPProValueValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1, 2),
    _DenviroSNMPProValueValue_Type()
)
denviroSNMPProValueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProValueValue.setStatus("mandatory")
_DenviroSNMPProValueScaleExp_Type = Integer32
_DenviroSNMPProValueScaleExp_Object = MibTableColumn
denviroSNMPProValueScaleExp = _DenviroSNMPProValueScaleExp_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1, 3),
    _DenviroSNMPProValueScaleExp_Type()
)
denviroSNMPProValueScaleExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProValueScaleExp.setStatus("mandatory")


class _DenviroSNMPProValueUnitString_Type(DisplayString):
    """Custom type denviroSNMPProValueUnitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DenviroSNMPProValueUnitString_Type.__name__ = "DisplayString"
_DenviroSNMPProValueUnitString_Object = MibTableColumn
denviroSNMPProValueUnitString = _DenviroSNMPProValueUnitString_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1, 4),
    _DenviroSNMPProValueUnitString_Type()
)
denviroSNMPProValueUnitString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProValueUnitString.setStatus("mandatory")


class _DenviroSNMPProValueID_Type(Integer32):
    """Custom type denviroSNMPProValueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroSNMPProValueID_Type.__name__ = "Integer32"
_DenviroSNMPProValueID_Object = MibTableColumn
denviroSNMPProValueID = _DenviroSNMPProValueID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1, 5),
    _DenviroSNMPProValueID_Type()
)
denviroSNMPProValueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProValueID.setStatus("mandatory")


class _DenviroSNMPProValueIndex_Type(Integer32):
    """Custom type denviroSNMPProValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DenviroSNMPProValueIndex_Type.__name__ = "Integer32"
_DenviroSNMPProValueIndex_Object = MibTableColumn
denviroSNMPProValueIndex = _DenviroSNMPProValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 3, 1, 6),
    _DenviroSNMPProValueIndex_Type()
)
denviroSNMPProValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroSNMPProValueIndex.setStatus("mandatory")
_DenviroSNMPProStringTable_Object = MibTable
denviroSNMPProStringTable = _DenviroSNMPProStringTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 4)
)
if mibBuilder.loadTexts:
    denviroSNMPProStringTable.setStatus("mandatory")
_DenviroSNMPProStringEntry_Object = MibTableRow
denviroSNMPProStringEntry = _DenviroSNMPProStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 4, 1)
)
denviroSNMPProStringEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroSNMPProStringID"),
    (0, "DeltaEnviro-MIB", "denviroSNMPProStringIndex"),
)
if mibBuilder.loadTexts:
    denviroSNMPProStringEntry.setStatus("mandatory")


class _DenviroSNMPProStringTitle_Type(DisplayString):
    """Custom type denviroSNMPProStringTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroSNMPProStringTitle_Type.__name__ = "DisplayString"
_DenviroSNMPProStringTitle_Object = MibTableColumn
denviroSNMPProStringTitle = _DenviroSNMPProStringTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 4, 1, 1),
    _DenviroSNMPProStringTitle_Type()
)
denviroSNMPProStringTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProStringTitle.setStatus("mandatory")
_DenviroSNMPProStringValue_Type = Integer32
_DenviroSNMPProStringValue_Object = MibTableColumn
denviroSNMPProStringValue = _DenviroSNMPProStringValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 4, 1, 2),
    _DenviroSNMPProStringValue_Type()
)
denviroSNMPProStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProStringValue.setStatus("mandatory")


class _DenviroSNMPProStringID_Type(Integer32):
    """Custom type denviroSNMPProStringID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroSNMPProStringID_Type.__name__ = "Integer32"
_DenviroSNMPProStringID_Object = MibTableColumn
denviroSNMPProStringID = _DenviroSNMPProStringID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 4, 1, 3),
    _DenviroSNMPProStringID_Type()
)
denviroSNMPProStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProStringID.setStatus("mandatory")


class _DenviroSNMPProStringIndex_Type(Integer32):
    """Custom type denviroSNMPProStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DenviroSNMPProStringIndex_Type.__name__ = "Integer32"
_DenviroSNMPProStringIndex_Object = MibTableColumn
denviroSNMPProStringIndex = _DenviroSNMPProStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 4, 1, 4),
    _DenviroSNMPProStringIndex_Type()
)
denviroSNMPProStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroSNMPProStringIndex.setStatus("mandatory")
_DenviroSNMPProWritableTable_Object = MibTable
denviroSNMPProWritableTable = _DenviroSNMPProWritableTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 5)
)
if mibBuilder.loadTexts:
    denviroSNMPProWritableTable.setStatus("mandatory")
_DenviroSNMPProWritableEntry_Object = MibTableRow
denviroSNMPProWritableEntry = _DenviroSNMPProWritableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 5, 1)
)
denviroSNMPProWritableEntry.setIndexNames(
    (0, "DeltaEnviro-MIB", "denviroSNMPProWritableID"),
    (0, "DeltaEnviro-MIB", "denviroSNMPProWritableIndex"),
)
if mibBuilder.loadTexts:
    denviroSNMPProWritableEntry.setStatus("mandatory")


class _DenviroSNMPProWritableTitle_Type(DisplayString):
    """Custom type denviroSNMPProWritableTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DenviroSNMPProWritableTitle_Type.__name__ = "DisplayString"
_DenviroSNMPProWritableTitle_Object = MibTableColumn
denviroSNMPProWritableTitle = _DenviroSNMPProWritableTitle_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 5, 1, 1),
    _DenviroSNMPProWritableTitle_Type()
)
denviroSNMPProWritableTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProWritableTitle.setStatus("mandatory")
_DenviroSNMPProWritableValue_Type = Integer32
_DenviroSNMPProWritableValue_Object = MibTableColumn
denviroSNMPProWritableValue = _DenviroSNMPProWritableValue_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 5, 1, 2),
    _DenviroSNMPProWritableValue_Type()
)
denviroSNMPProWritableValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    denviroSNMPProWritableValue.setStatus("mandatory")


class _DenviroSNMPProWritableID_Type(Integer32):
    """Custom type denviroSNMPProWritableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DenviroSNMPProWritableID_Type.__name__ = "Integer32"
_DenviroSNMPProWritableID_Object = MibTableColumn
denviroSNMPProWritableID = _DenviroSNMPProWritableID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 5, 1, 3),
    _DenviroSNMPProWritableID_Type()
)
denviroSNMPProWritableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denviroSNMPProWritableID.setStatus("mandatory")


class _DenviroSNMPProWritableIndex_Type(Integer32):
    """Custom type denviroSNMPProWritableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DenviroSNMPProWritableIndex_Type.__name__ = "Integer32"
_DenviroSNMPProWritableIndex_Object = MibTableColumn
denviroSNMPProWritableIndex = _DenviroSNMPProWritableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 8, 5, 1, 4),
    _DenviroSNMPProWritableIndex_Type()
)
denviroSNMPProWritableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    denviroSNMPProWritableIndex.setStatus("mandatory")
_DenviroTraps_ObjectIdentity = ObjectIdentity
denviroTraps = _DenviroTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20)
)

# Managed Objects groups


# Notification objects

denviroCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 1)
)
if mibBuilder.loadTexts:
    denviroCommunicationLost.setStatus(
        ""
    )

denviroCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 2)
)
if mibBuilder.loadTexts:
    denviroCommunicationEstablished.setStatus(
        ""
    )

denviroSensorHub1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 3)
)
denviroSensorHub1Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub1Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub1Alarm.setStatus(
        ""
    )

denviroSensorHub1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 4)
)
denviroSensorHub1Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub1Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub1Normal.setStatus(
        ""
    )

denviroSensorHub2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 5)
)
denviroSensorHub2Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub2Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub2Alarm.setStatus(
        ""
    )

denviroSensorHub2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 6)
)
denviroSensorHub2Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub2Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub2Normal.setStatus(
        ""
    )

denviroSensorHub3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 7)
)
denviroSensorHub3Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub3Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub3Alarm.setStatus(
        ""
    )

denviroSensorHub3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 8)
)
denviroSensorHub3Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub3Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub3Normal.setStatus(
        ""
    )

denviroSensorHub4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 9)
)
denviroSensorHub4Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub4Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub4Alarm.setStatus(
        ""
    )

denviroSensorHub4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 10)
)
denviroSensorHub4Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub4Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub4Normal.setStatus(
        ""
    )

denviroSensorHub5Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 11)
)
denviroSensorHub5Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub5Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub5Alarm.setStatus(
        ""
    )

denviroSensorHub5Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 12)
)
denviroSensorHub5Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub5Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub5Normal.setStatus(
        ""
    )

denviroSensorHub6Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 13)
)
denviroSensorHub6Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub6Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub6Alarm.setStatus(
        ""
    )

denviroSensorHub6Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 14)
)
denviroSensorHub6Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub6Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub6Normal.setStatus(
        ""
    )

denviroSensorHub7Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 15)
)
denviroSensorHub7Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub7Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub7Alarm.setStatus(
        ""
    )

denviroSensorHub7Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 16)
)
denviroSensorHub7Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub7Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub7Normal.setStatus(
        ""
    )

denviroSensorHub8Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 17)
)
denviroSensorHub8Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub8Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub8Alarm.setStatus(
        ""
    )

denviroSensorHub8Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 18)
)
denviroSensorHub8Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentSensorHub8Title")
)
if mibBuilder.loadTexts:
    denviroSensorHub8Normal.setStatus(
        ""
    )

denviroAI1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 19)
)
denviroAI1Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI1Title")
)
if mibBuilder.loadTexts:
    denviroAI1Alarm.setStatus(
        ""
    )

denviroAI1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 20)
)
denviroAI1Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI1Title")
)
if mibBuilder.loadTexts:
    denviroAI1Normal.setStatus(
        ""
    )

denviroAI2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 21)
)
denviroAI2Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI2Title")
)
if mibBuilder.loadTexts:
    denviroAI2Alarm.setStatus(
        ""
    )

denviroAI2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 22)
)
denviroAI2Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI2Title")
)
if mibBuilder.loadTexts:
    denviroAI2Normal.setStatus(
        ""
    )

denviroAI3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 23)
)
denviroAI3Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI3Title")
)
if mibBuilder.loadTexts:
    denviroAI3Alarm.setStatus(
        ""
    )

denviroAI3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 24)
)
denviroAI3Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI3Title")
)
if mibBuilder.loadTexts:
    denviroAI3Normal.setStatus(
        ""
    )

denviroAI4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 25)
)
denviroAI4Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI4Title")
)
if mibBuilder.loadTexts:
    denviroAI4Alarm.setStatus(
        ""
    )

denviroAI4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 26)
)
denviroAI4Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentAI4Title")
)
if mibBuilder.loadTexts:
    denviroAI4Normal.setStatus(
        ""
    )

denviroDI1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 27)
)
denviroDI1Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI1Title")
)
if mibBuilder.loadTexts:
    denviroDI1Alarm.setStatus(
        ""
    )

denviroDI1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 28)
)
denviroDI1Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI1Title")
)
if mibBuilder.loadTexts:
    denviroDI1Normal.setStatus(
        ""
    )

denviroDI2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 29)
)
denviroDI2Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI2Title")
)
if mibBuilder.loadTexts:
    denviroDI2Alarm.setStatus(
        ""
    )

denviroDI2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 30)
)
denviroDI2Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI2Title")
)
if mibBuilder.loadTexts:
    denviroDI2Normal.setStatus(
        ""
    )

denviroDI3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 31)
)
denviroDI3Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI3Title")
)
if mibBuilder.loadTexts:
    denviroDI3Alarm.setStatus(
        ""
    )

denviroDI3Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 32)
)
denviroDI3Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI3Title")
)
if mibBuilder.loadTexts:
    denviroDI3Normal.setStatus(
        ""
    )

denviroDI4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 33)
)
denviroDI4Alarm.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI4Title")
)
if mibBuilder.loadTexts:
    denviroDI4Alarm.setStatus(
        ""
    )

denviroDI4Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 34)
)
denviroDI4Normal.setObjects(
    ("DeltaEnviro-MIB", "denviroIdentDI4Title")
)
if mibBuilder.loadTexts:
    denviroDI4Normal.setStatus(
        ""
    )

denviroDBCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 35)
)
denviroDBCommunicationLost.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"))
)
if mibBuilder.loadTexts:
    denviroDBCommunicationLost.setStatus(
        ""
    )

denviroDBCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 36)
)
denviroDBCommunicationEstablished.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"))
)
if mibBuilder.loadTexts:
    denviroDBCommunicationEstablished.setStatus(
        ""
    )

denviroEMS1000DBTempWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 37)
)
denviroEMS1000DBTempWarn.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTemperature"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBTempWarn.setStatus(
        ""
    )

denviroEMS1000DBTempWarnRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 38)
)
denviroEMS1000DBTempWarnRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTemperature"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBTempWarnRecover.setStatus(
        ""
    )

denviroEMS1000DBTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 39)
)
denviroEMS1000DBTempAlarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTemperature"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBTempAlarm.setStatus(
        ""
    )

denviroEMS1000DBTempAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 40)
)
denviroEMS1000DBTempAlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTemperature"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBTempAlarmRecover.setStatus(
        ""
    )

denviroEMS1000DBHumidityWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 41)
)
denviroEMS1000DBHumidityWarn.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBHumidity"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityWarn.setStatus(
        ""
    )

denviroEMS1000DBHumidityWarnRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 42)
)
denviroEMS1000DBHumidityWarnRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBHumidity"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityWarnRecover.setStatus(
        ""
    )

denviroEMS1000DBHumidityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 43)
)
denviroEMS1000DBHumidityAlarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBHumidity"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityAlarm.setStatus(
        ""
    )

denviroEMS1000DBHumidityAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 44)
)
denviroEMS1000DBHumidityAlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBHumidity"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBHumidityAlarmRecover.setStatus(
        ""
    )

denviroEMS1000DBInput1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 45)
)
denviroEMS1000DBInput1Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn1Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput1Alarm.setStatus(
        ""
    )

denviroEMS1000DBInput1AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 46)
)
denviroEMS1000DBInput1AlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn1Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput1AlarmRecover.setStatus(
        ""
    )

denviroEMS1000DBInput2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 47)
)
denviroEMS1000DBInput2Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn2Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput2Alarm.setStatus(
        ""
    )

denviroEMS1000DBInput2AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 48)
)
denviroEMS1000DBInput2AlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn2Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput2AlarmRecover.setStatus(
        ""
    )

denviroEMS1000DBInput3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 49)
)
denviroEMS1000DBInput3Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn3Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput3Alarm.setStatus(
        ""
    )

denviroEMS1000DBInput3AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 50)
)
denviroEMS1000DBInput3AlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn3Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput3AlarmRecover.setStatus(
        ""
    )

denviroEMS1000DBInput4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 51)
)
denviroEMS1000DBInput4Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn4Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput4Alarm.setStatus(
        ""
    )

denviroEMS1000DBInput4AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 52)
)
denviroEMS1000DBInput4AlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1000DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBTitle"),
        ("DeltaEnviro-MIB", "denviroEMS1000DBIn4Title"))
)
if mibBuilder.loadTexts:
    denviroEMS1000DBInput4AlarmRecover.setStatus(
        ""
    )

denviroRS4851Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 53)
)
denviroRS4851Warn.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4851Warn.setStatus(
        ""
    )

denviroRS4851WarnRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 54)
)
denviroRS4851WarnRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4851WarnRecover.setStatus(
        ""
    )

denviroRS4851Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 55)
)
denviroRS4851Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4851Alarm.setStatus(
        ""
    )

denviroRS4851AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 56)
)
denviroRS4851AlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4851AlarmRecover.setStatus(
        ""
    )

denviroRS4852Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 57)
)
denviroRS4852Warn.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4852Warn.setStatus(
        ""
    )

denviroRS4852WarnRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 58)
)
denviroRS4852WarnRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4852WarnRecover.setStatus(
        ""
    )

denviroRS4852Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 59)
)
denviroRS4852Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4852Alarm.setStatus(
        ""
    )

denviroRS4852AlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 60)
)
denviroRS4852AlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroID485"),
        ("DeltaEnviro-MIB", "denviroTitle485"),
        ("DeltaEnviro-MIB", "denviroTitle485"))
)
if mibBuilder.loadTexts:
    denviroRS4852AlarmRecover.setStatus(
        ""
    )

denviroEMS1100DBRL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 61)
)
denviroEMS1100DBRL1.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL1.setStatus(
        ""
    )

denviroEMS1100DBRL1Recover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 62)
)
denviroEMS1100DBRL1Recover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL1Recover.setStatus(
        ""
    )

denviroEMS1100DBRL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 63)
)
denviroEMS1100DBRL2.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL2.setStatus(
        ""
    )

denviroEMS1100DBRL2Recover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 64)
)
denviroEMS1100DBRL2Recover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL2Recover.setStatus(
        ""
    )

denviroEMS1100DBRL3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 65)
)
denviroEMS1100DBRL3.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL3.setStatus(
        ""
    )

denviroEMS1100DBRL3Recover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 66)
)
denviroEMS1100DBRL3Recover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL3Recover.setStatus(
        ""
    )

denviroEMS1100DBRL4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 67)
)
denviroEMS1100DBRL4.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL4.setStatus(
        ""
    )

denviroEMS1100DBRL4Recover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 68)
)
denviroEMS1100DBRL4Recover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1100DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1100DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1100DBRL4Recover.setStatus(
        ""
    )

denviroEMS1200DBAI1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 69)
)
denviroEMS1200DBAI1Warn.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAI1Warn.setStatus(
        ""
    )

denviroEMS1200DBAI2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 70)
)
denviroEMS1200DBAI2Warn.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAI2Warn.setStatus(
        ""
    )

denviroEMS1200DBAI1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 71)
)
denviroEMS1200DBAI1Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAI1Alarm.setStatus(
        ""
    )

denviroEMS1200DBAI2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 72)
)
denviroEMS1200DBAI2Alarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAI2Alarm.setStatus(
        ""
    )

denviroEMS1200DBLeakAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 73)
)
denviroEMS1200DBLeakAlarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBLeakAlarm.setStatus(
        ""
    )

denviroEMS1200DBAI1Recover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 74)
)
denviroEMS1200DBAI1Recover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAI1Recover.setStatus(
        ""
    )

denviroEMS1200DBAI2Recover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 75)
)
denviroEMS1200DBAI2Recover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAI2Recover.setStatus(
        ""
    )

denviroEMS1200DBLeakRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 76)
)
denviroEMS1200DBLeakRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBLeakRecover.setStatus(
        ""
    )

denviroEMS1200DBAOAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 77)
)
denviroEMS1200DBAOAlarm.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAOAlarm.setStatus(
        ""
    )

denviroEMS1200DBAOAlarmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 78)
)
denviroEMS1200DBAOAlarmRecover.setObjects(
      *(("DeltaEnviro-MIB", "denviroEMS1200DBID"),
        ("DeltaEnviro-MIB", "denviroEMS1200DBTitle"))
)
if mibBuilder.loadTexts:
    denviroEMS1200DBAOAlarmRecover.setStatus(
        ""
    )

denviroReactionTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 41, 20, 0, 79)
)
denviroReactionTriggered.setObjects(
    ("DeltaEnviro-MIB", "denviroReactionRuleName")
)
if mibBuilder.loadTexts:
    denviroReactionTriggered.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaEnviro-MIB",
    **{"delta": delta,
       "ups": ups,
       "enviro": enviro,
       "denviroIdent": denviroIdent,
       "denviroIdentManufacturer": denviroIdentManufacturer,
       "denviroIdentModel": denviroIdentModel,
       "denviroIdentSerialNumber": denviroIdentSerialNumber,
       "denviroIdentAgentFirmwareVersion": denviroIdentAgentFirmwareVersion,
       "denviroIdentAgentSoftwareVersion": denviroIdentAgentSoftwareVersion,
       "denviroIdentName": denviroIdentName,
       "denviroIdentSensorHub1Title": denviroIdentSensorHub1Title,
       "denviroIdentSensorHub2Title": denviroIdentSensorHub2Title,
       "denviroIdentSensorHub3Title": denviroIdentSensorHub3Title,
       "denviroIdentSensorHub4Title": denviroIdentSensorHub4Title,
       "denviroIdentSensorHub5Title": denviroIdentSensorHub5Title,
       "denviroIdentSensorHub6Title": denviroIdentSensorHub6Title,
       "denviroIdentSensorHub7Title": denviroIdentSensorHub7Title,
       "denviroIdentSensorHub8Title": denviroIdentSensorHub8Title,
       "denviroIdentAI1Title": denviroIdentAI1Title,
       "denviroIdentAI2Title": denviroIdentAI2Title,
       "denviroIdentAI3Title": denviroIdentAI3Title,
       "denviroIdentAI4Title": denviroIdentAI4Title,
       "denviroIdentDI1Title": denviroIdentDI1Title,
       "denviroIdentDI2Title": denviroIdentDI2Title,
       "denviroIdentDI3Title": denviroIdentDI3Title,
       "denviroIdentDI4Title": denviroIdentDI4Title,
       "denviroIdentDO1Title": denviroIdentDO1Title,
       "denviroIdentDO2Title": denviroIdentDO2Title,
       "denviroStatus": denviroStatus,
       "denviroStatusSensorHub1": denviroStatusSensorHub1,
       "denviroStatusSensorHub2": denviroStatusSensorHub2,
       "denviroStatusSensorHub3": denviroStatusSensorHub3,
       "denviroStatusSensorHub4": denviroStatusSensorHub4,
       "denviroStatusSensorHub5": denviroStatusSensorHub5,
       "denviroStatusSensorHub6": denviroStatusSensorHub6,
       "denviroStatusSensorHub7": denviroStatusSensorHub7,
       "denviroStatusSensorHub8": denviroStatusSensorHub8,
       "denviroStatusSensorHubPwr1": denviroStatusSensorHubPwr1,
       "denviroStatusSensorHubPwr2": denviroStatusSensorHubPwr2,
       "denviroStatusDI1": denviroStatusDI1,
       "denviroStatusDI2": denviroStatusDI2,
       "denviroStatusDI3": denviroStatusDI3,
       "denviroStatusDI4": denviroStatusDI4,
       "denviroStatusDO1": denviroStatusDO1,
       "denviroStatusDO2": denviroStatusDO2,
       "denviroMeasureAI1": denviroMeasureAI1,
       "denviroMeasureAI2": denviroMeasureAI2,
       "denviroMeasureAI3": denviroMeasureAI3,
       "denviroMeasureAI4": denviroMeasureAI4,
       "denviroStatusAI1": denviroStatusAI1,
       "denviroStatusAI2": denviroStatusAI2,
       "denviroStatusAI3": denviroStatusAI3,
       "denviroStatusAI4": denviroStatusAI4,
       "denviroStatusCommunication": denviroStatusCommunication,
       "denviroStatusShortCircuit": denviroStatusShortCircuit,
       "denviroStatusOverCurrent": denviroStatusOverCurrent,
       "denviroStatusOverVoltage": denviroStatusOverVoltage,
       "denviroDeltaBus": denviroDeltaBus,
       "denviroEMS1000DBNum": denviroEMS1000DBNum,
       "denviroEMS1000DBTable": denviroEMS1000DBTable,
       "denviroEMS1000DBEntry": denviroEMS1000DBEntry,
       "denviroEMS1000DBTitle": denviroEMS1000DBTitle,
       "denviroEMS1000DBTemperature": denviroEMS1000DBTemperature,
       "denviroEMS1000DBHumidity": denviroEMS1000DBHumidity,
       "denviroEMS1000DBInput1": denviroEMS1000DBInput1,
       "denviroEMS1000DBInput2": denviroEMS1000DBInput2,
       "denviroEMS1000DBInput3": denviroEMS1000DBInput3,
       "denviroEMS1000DBInput4": denviroEMS1000DBInput4,
       "denviroEMS1000DBIn1Title": denviroEMS1000DBIn1Title,
       "denviroEMS1000DBIn2Title": denviroEMS1000DBIn2Title,
       "denviroEMS1000DBIn3Title": denviroEMS1000DBIn3Title,
       "denviroEMS1000DBIn4Title": denviroEMS1000DBIn4Title,
       "denviroEMS1000DBStatusComm": denviroEMS1000DBStatusComm,
       "denviroEMS1000DBStatusTemperature": denviroEMS1000DBStatusTemperature,
       "denviroEMS1000DBStatusHumidity": denviroEMS1000DBStatusHumidity,
       "denviroEMS1000DBID": denviroEMS1000DBID,
       "denviroEMS1000DBTemperatureWarningThreshold": denviroEMS1000DBTemperatureWarningThreshold,
       "denviroEMS1000DBTemperatureWarningRecoverThreshold": denviroEMS1000DBTemperatureWarningRecoverThreshold,
       "denviroEMS1000DBTemperatureAlarmThreshold": denviroEMS1000DBTemperatureAlarmThreshold,
       "denviroEMS1000DBTemperatureAlarmRecoverThreshold": denviroEMS1000DBTemperatureAlarmRecoverThreshold,
       "denviroEMS1000DBHumidityWarningThreshold": denviroEMS1000DBHumidityWarningThreshold,
       "denviroEMS1000DBHumidityWarningRecoverThreshold": denviroEMS1000DBHumidityWarningRecoverThreshold,
       "denviroEMS1000DBHumidityAlarmThreshold": denviroEMS1000DBHumidityAlarmThreshold,
       "denviroEMS1000DBHumidityAlarmRecoverThreshold": denviroEMS1000DBHumidityAlarmRecoverThreshold,
       "denviroEMS1100DBNum": denviroEMS1100DBNum,
       "denviroEMS1100DBTable": denviroEMS1100DBTable,
       "denviroEMS1100DBEntry": denviroEMS1100DBEntry,
       "denviroEMS1100DBID": denviroEMS1100DBID,
       "denviroEMS1100DBStatusComm": denviroEMS1100DBStatusComm,
       "denviroEMS1100DBTitle": denviroEMS1100DBTitle,
       "denviroEMS1100DBDO1Title": denviroEMS1100DBDO1Title,
       "denviroEMS1100DBDO2Title": denviroEMS1100DBDO2Title,
       "denviroEMS1100DBDO3Title": denviroEMS1100DBDO3Title,
       "denviroEMS1100DBDO4Title": denviroEMS1100DBDO4Title,
       "denviroEMS1100DBDO1Status": denviroEMS1100DBDO1Status,
       "denviroEMS1100DBDO2Status": denviroEMS1100DBDO2Status,
       "denviroEMS1100DBDO3Status": denviroEMS1100DBDO3Status,
       "denviroEMS1100DBDO4Status": denviroEMS1100DBDO4Status,
       "denviroEMS1100DBDO1Manual": denviroEMS1100DBDO1Manual,
       "denviroEMS1100DBDO2Manual": denviroEMS1100DBDO2Manual,
       "denviroEMS1100DBDO3Manual": denviroEMS1100DBDO3Manual,
       "denviroEMS1100DBDO4Manual": denviroEMS1100DBDO4Manual,
       "denviroEMS1200DBNum": denviroEMS1200DBNum,
       "denviroEMS1200DBTable": denviroEMS1200DBTable,
       "denviroEMS1200DBEntry": denviroEMS1200DBEntry,
       "denviroEMS1200DBID": denviroEMS1200DBID,
       "denviroEMS1200DBStatusComm": denviroEMS1200DBStatusComm,
       "denviroEMS1200DBTitle": denviroEMS1200DBTitle,
       "denviroEMS1200DBAI1Title": denviroEMS1200DBAI1Title,
       "denviroEMS1200DBAI2Title": denviroEMS1200DBAI2Title,
       "denviroEMS1200DBLeakageTitle": denviroEMS1200DBLeakageTitle,
       "denviroEMS1200DBAOTitle": denviroEMS1200DBAOTitle,
       "denviroEMS1200DBAI1Value": denviroEMS1200DBAI1Value,
       "denviroEMS1200DBAI2Value": denviroEMS1200DBAI2Value,
       "denviroEMS1200DBAI1Status": denviroEMS1200DBAI1Status,
       "denviroEMS1200DBAI2Status": denviroEMS1200DBAI2Status,
       "denviroEMS1200DBLeakageLevel": denviroEMS1200DBLeakageLevel,
       "denviroEMS1200DBLeakageBuzzer": denviroEMS1200DBLeakageBuzzer,
       "denviroEMS1200DBLeakageStatus": denviroEMS1200DBLeakageStatus,
       "denviroEMS1200DBAOControl": denviroEMS1200DBAOControl,
       "denviroEMS1200DBAOStatus": denviroEMS1200DBAOStatus,
       "denviroEMS1200DBAOManual": denviroEMS1200DBAOManual,
       "denviroRS485": denviroRS485,
       "denviroNum485": denviroNum485,
       "denviro485Table": denviro485Table,
       "denviro485Entry": denviro485Entry,
       "denviroTitle485": denviroTitle485,
       "denviroCommLost": denviroCommLost,
       "denviro485Port": denviro485Port,
       "denviroID485": denviroID485,
       "denviroValueTable": denviroValueTable,
       "denviroValueEntry": denviroValueEntry,
       "denviroValueTitle": denviroValueTitle,
       "denviroValueValue": denviroValueValue,
       "denviroValueScaleExp": denviroValueScaleExp,
       "denviroValueUnitString": denviroValueUnitString,
       "denviroValue485Port": denviroValue485Port,
       "denviroValueID485": denviroValueID485,
       "denviroValueIndex": denviroValueIndex,
       "denviroStatusTable": denviroStatusTable,
       "denviroStatusEntry": denviroStatusEntry,
       "denviroStatusTitle": denviroStatusTitle,
       "denviroStatusValue": denviroStatusValue,
       "denviroStatus485Port": denviroStatus485Port,
       "denviroStatusID485": denviroStatusID485,
       "denviroStatusIndex": denviroStatusIndex,
       "denviroWritableValueTable": denviroWritableValueTable,
       "denviroWritableValueEntry": denviroWritableValueEntry,
       "denviroWritableValueTitle": denviroWritableValueTitle,
       "denviroWritableValueValue": denviroWritableValueValue,
       "denviroWritableValue485Port": denviroWritableValue485Port,
       "denviroWritableValueID485": denviroWritableValueID485,
       "denviroWritableValueIndex": denviroWritableValueIndex,
       "denviroControl": denviroControl,
       "denviroCtrlHub1PwrManual": denviroCtrlHub1PwrManual,
       "denviroCtrlHub2PwrManual": denviroCtrlHub2PwrManual,
       "denviroCtrlHub1Pwr": denviroCtrlHub1Pwr,
       "denviroCtrlHub2Pwr": denviroCtrlHub2Pwr,
       "denviroCtrlDO1Manual": denviroCtrlDO1Manual,
       "denviroCtrlDO2Manual": denviroCtrlDO2Manual,
       "denviroCtrlDO1": denviroCtrlDO1,
       "denviroCtrlDO2": denviroCtrlDO2,
       "denviroPDU": denviroPDU,
       "denviroPDUEnable": denviroPDUEnable,
       "denviroReaction": denviroReaction,
       "denviroReactionTable": denviroReactionTable,
       "denviroReactionEntry": denviroReactionEntry,
       "denviroReactionRuleName": denviroReactionRuleName,
       "denviroReactionEnable": denviroReactionEnable,
       "denviroReactionCtrlValueTable": denviroReactionCtrlValueTable,
       "denviroReactionCtrlValueEntry": denviroReactionCtrlValueEntry,
       "denviroReactionCtrlValueID": denviroReactionCtrlValueID,
       "denviroReactionCtrlValue": denviroReactionCtrlValue,
       "denviroSNMPProtocol": denviroSNMPProtocol,
       "denviroNumSNMPDevice": denviroNumSNMPDevice,
       "denviroSNMPDeviceTable": denviroSNMPDeviceTable,
       "denviroSNMPDeviceEntry": denviroSNMPDeviceEntry,
       "denviroSNMPDeviceIP": denviroSNMPDeviceIP,
       "denviroSNMPDevicePort": denviroSNMPDevicePort,
       "denviroSNMPDeviceVersion": denviroSNMPDeviceVersion,
       "denviroSNMPDeviceCommunity": denviroSNMPDeviceCommunity,
       "denviroCommLink": denviroCommLink,
       "denviroSNMPDeviceIndex": denviroSNMPDeviceIndex,
       "denviroSNMPProValueTable": denviroSNMPProValueTable,
       "denviroSNMPProValueEntry": denviroSNMPProValueEntry,
       "denviroSNMPProValueTitle": denviroSNMPProValueTitle,
       "denviroSNMPProValueValue": denviroSNMPProValueValue,
       "denviroSNMPProValueScaleExp": denviroSNMPProValueScaleExp,
       "denviroSNMPProValueUnitString": denviroSNMPProValueUnitString,
       "denviroSNMPProValueID": denviroSNMPProValueID,
       "denviroSNMPProValueIndex": denviroSNMPProValueIndex,
       "denviroSNMPProStringTable": denviroSNMPProStringTable,
       "denviroSNMPProStringEntry": denviroSNMPProStringEntry,
       "denviroSNMPProStringTitle": denviroSNMPProStringTitle,
       "denviroSNMPProStringValue": denviroSNMPProStringValue,
       "denviroSNMPProStringID": denviroSNMPProStringID,
       "denviroSNMPProStringIndex": denviroSNMPProStringIndex,
       "denviroSNMPProWritableTable": denviroSNMPProWritableTable,
       "denviroSNMPProWritableEntry": denviroSNMPProWritableEntry,
       "denviroSNMPProWritableTitle": denviroSNMPProWritableTitle,
       "denviroSNMPProWritableValue": denviroSNMPProWritableValue,
       "denviroSNMPProWritableID": denviroSNMPProWritableID,
       "denviroSNMPProWritableIndex": denviroSNMPProWritableIndex,
       "denviroTraps": denviroTraps,
       "denviroCommunicationLost": denviroCommunicationLost,
       "denviroCommunicationEstablished": denviroCommunicationEstablished,
       "denviroSensorHub1Alarm": denviroSensorHub1Alarm,
       "denviroSensorHub1Normal": denviroSensorHub1Normal,
       "denviroSensorHub2Alarm": denviroSensorHub2Alarm,
       "denviroSensorHub2Normal": denviroSensorHub2Normal,
       "denviroSensorHub3Alarm": denviroSensorHub3Alarm,
       "denviroSensorHub3Normal": denviroSensorHub3Normal,
       "denviroSensorHub4Alarm": denviroSensorHub4Alarm,
       "denviroSensorHub4Normal": denviroSensorHub4Normal,
       "denviroSensorHub5Alarm": denviroSensorHub5Alarm,
       "denviroSensorHub5Normal": denviroSensorHub5Normal,
       "denviroSensorHub6Alarm": denviroSensorHub6Alarm,
       "denviroSensorHub6Normal": denviroSensorHub6Normal,
       "denviroSensorHub7Alarm": denviroSensorHub7Alarm,
       "denviroSensorHub7Normal": denviroSensorHub7Normal,
       "denviroSensorHub8Alarm": denviroSensorHub8Alarm,
       "denviroSensorHub8Normal": denviroSensorHub8Normal,
       "denviroAI1Alarm": denviroAI1Alarm,
       "denviroAI1Normal": denviroAI1Normal,
       "denviroAI2Alarm": denviroAI2Alarm,
       "denviroAI2Normal": denviroAI2Normal,
       "denviroAI3Alarm": denviroAI3Alarm,
       "denviroAI3Normal": denviroAI3Normal,
       "denviroAI4Alarm": denviroAI4Alarm,
       "denviroAI4Normal": denviroAI4Normal,
       "denviroDI1Alarm": denviroDI1Alarm,
       "denviroDI1Normal": denviroDI1Normal,
       "denviroDI2Alarm": denviroDI2Alarm,
       "denviroDI2Normal": denviroDI2Normal,
       "denviroDI3Alarm": denviroDI3Alarm,
       "denviroDI3Normal": denviroDI3Normal,
       "denviroDI4Alarm": denviroDI4Alarm,
       "denviroDI4Normal": denviroDI4Normal,
       "denviroDBCommunicationLost": denviroDBCommunicationLost,
       "denviroDBCommunicationEstablished": denviroDBCommunicationEstablished,
       "denviroEMS1000DBTempWarn": denviroEMS1000DBTempWarn,
       "denviroEMS1000DBTempWarnRecover": denviroEMS1000DBTempWarnRecover,
       "denviroEMS1000DBTempAlarm": denviroEMS1000DBTempAlarm,
       "denviroEMS1000DBTempAlarmRecover": denviroEMS1000DBTempAlarmRecover,
       "denviroEMS1000DBHumidityWarn": denviroEMS1000DBHumidityWarn,
       "denviroEMS1000DBHumidityWarnRecover": denviroEMS1000DBHumidityWarnRecover,
       "denviroEMS1000DBHumidityAlarm": denviroEMS1000DBHumidityAlarm,
       "denviroEMS1000DBHumidityAlarmRecover": denviroEMS1000DBHumidityAlarmRecover,
       "denviroEMS1000DBInput1Alarm": denviroEMS1000DBInput1Alarm,
       "denviroEMS1000DBInput1AlarmRecover": denviroEMS1000DBInput1AlarmRecover,
       "denviroEMS1000DBInput2Alarm": denviroEMS1000DBInput2Alarm,
       "denviroEMS1000DBInput2AlarmRecover": denviroEMS1000DBInput2AlarmRecover,
       "denviroEMS1000DBInput3Alarm": denviroEMS1000DBInput3Alarm,
       "denviroEMS1000DBInput3AlarmRecover": denviroEMS1000DBInput3AlarmRecover,
       "denviroEMS1000DBInput4Alarm": denviroEMS1000DBInput4Alarm,
       "denviroEMS1000DBInput4AlarmRecover": denviroEMS1000DBInput4AlarmRecover,
       "denviroRS4851Warn": denviroRS4851Warn,
       "denviroRS4851WarnRecover": denviroRS4851WarnRecover,
       "denviroRS4851Alarm": denviroRS4851Alarm,
       "denviroRS4851AlarmRecover": denviroRS4851AlarmRecover,
       "denviroRS4852Warn": denviroRS4852Warn,
       "denviroRS4852WarnRecover": denviroRS4852WarnRecover,
       "denviroRS4852Alarm": denviroRS4852Alarm,
       "denviroRS4852AlarmRecover": denviroRS4852AlarmRecover,
       "denviroEMS1100DBRL1": denviroEMS1100DBRL1,
       "denviroEMS1100DBRL1Recover": denviroEMS1100DBRL1Recover,
       "denviroEMS1100DBRL2": denviroEMS1100DBRL2,
       "denviroEMS1100DBRL2Recover": denviroEMS1100DBRL2Recover,
       "denviroEMS1100DBRL3": denviroEMS1100DBRL3,
       "denviroEMS1100DBRL3Recover": denviroEMS1100DBRL3Recover,
       "denviroEMS1100DBRL4": denviroEMS1100DBRL4,
       "denviroEMS1100DBRL4Recover": denviroEMS1100DBRL4Recover,
       "denviroEMS1200DBAI1Warn": denviroEMS1200DBAI1Warn,
       "denviroEMS1200DBAI2Warn": denviroEMS1200DBAI2Warn,
       "denviroEMS1200DBAI1Alarm": denviroEMS1200DBAI1Alarm,
       "denviroEMS1200DBAI2Alarm": denviroEMS1200DBAI2Alarm,
       "denviroEMS1200DBLeakAlarm": denviroEMS1200DBLeakAlarm,
       "denviroEMS1200DBAI1Recover": denviroEMS1200DBAI1Recover,
       "denviroEMS1200DBAI2Recover": denviroEMS1200DBAI2Recover,
       "denviroEMS1200DBLeakRecover": denviroEMS1200DBLeakRecover,
       "denviroEMS1200DBAOAlarm": denviroEMS1200DBAOAlarm,
       "denviroEMS1200DBAOAlarmRecover": denviroEMS1200DBAOAlarmRecover,
       "denviroReactionTriggered": denviroReactionTriggered}
)
