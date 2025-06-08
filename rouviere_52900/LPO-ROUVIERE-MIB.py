# SNMP MIB module (LPO-ROUVIERE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rouviere_52900/LPO-ROUVIERE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:55:59 2025
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

lpoRouviereMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52900)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LprMIBObjects_ObjectIdentity = ObjectIdentity
lprMIBObjects = _LprMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1)
)
_LprSnmpTutorial_ObjectIdentity = ObjectIdentity
lprSnmpTutorial = _LprSnmpTutorial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1)
)
_LprSnmpTutorialLeds_ObjectIdentity = ObjectIdentity
lprSnmpTutorialLeds = _LprSnmpTutorialLeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 1)
)


class _Led1_Type(Integer32):
    """Custom type led1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Led1_Type.__name__ = "Integer32"
_Led1_Object = MibScalar
led1 = _Led1_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 1, 1),
    _Led1_Type()
)
led1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    led1.setStatus("current")


class _Led2_Type(Integer32):
    """Custom type led2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Led2_Type.__name__ = "Integer32"
_Led2_Object = MibScalar
led2 = _Led2_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 1, 2),
    _Led2_Type()
)
led2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    led2.setStatus("current")


class _Led3_Type(Integer32):
    """Custom type led3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Led3_Type.__name__ = "Integer32"
_Led3_Object = MibScalar
led3 = _Led3_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 1, 3),
    _Led3_Type()
)
led3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    led3.setStatus("current")
_LprSnmpTutorialButtons_ObjectIdentity = ObjectIdentity
lprSnmpTutorialButtons = _LprSnmpTutorialButtons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 2)
)


class _Sw1_Type(Integer32):
    """Custom type sw1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sw1_Type.__name__ = "Integer32"
_Sw1_Object = MibScalar
sw1 = _Sw1_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 2, 1),
    _Sw1_Type()
)
sw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw1.setStatus("current")


class _Sw2_Type(Integer32):
    """Custom type sw2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sw2_Type.__name__ = "Integer32"
_Sw2_Object = MibScalar
sw2 = _Sw2_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 2, 2),
    _Sw2_Type()
)
sw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw2.setStatus("current")


class _Sw3_Type(Integer32):
    """Custom type sw3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sw3_Type.__name__ = "Integer32"
_Sw3_Object = MibScalar
sw3 = _Sw3_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 1, 2, 3),
    _Sw3_Type()
)
sw3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw3.setStatus("current")
_LprPointCast_ObjectIdentity = ObjectIdentity
lprPointCast = _LprPointCast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2)
)
_LprPointCastCoils_ObjectIdentity = ObjectIdentity
lprPointCastCoils = _LprPointCastCoils_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2, 1)
)


class _Coil1_Type(Integer32):
    """Custom type coil1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Coil1_Type.__name__ = "Integer32"
_Coil1_Object = MibScalar
coil1 = _Coil1_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2, 1, 1),
    _Coil1_Type()
)
coil1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coil1.setStatus("current")


class _Coil2_Type(Integer32):
    """Custom type coil2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Coil2_Type.__name__ = "Integer32"
_Coil2_Object = MibScalar
coil2 = _Coil2_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2, 1, 2),
    _Coil2_Type()
)
coil2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coil2.setStatus("current")


class _Coil3_Type(Integer32):
    """Custom type coil3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Coil3_Type.__name__ = "Integer32"
_Coil3_Object = MibScalar
coil3 = _Coil3_Object(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2, 1, 3),
    _Coil3_Type()
)
coil3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coil3.setStatus("current")
_LprPointCastDiscreteInputs_ObjectIdentity = ObjectIdentity
lprPointCastDiscreteInputs = _LprPointCastDiscreteInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2, 2)
)
_LprPointCastInputRegisters_ObjectIdentity = ObjectIdentity
lprPointCastInputRegisters = _LprPointCastInputRegisters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 1, 2, 3)
)
_LprMIBConformance_ObjectIdentity = ObjectIdentity
lprMIBConformance = _LprMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52900, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LPO-ROUVIERE-MIB",
    **{"lpoRouviereMIB": lpoRouviereMIB,
       "lprMIBObjects": lprMIBObjects,
       "lprSnmpTutorial": lprSnmpTutorial,
       "lprSnmpTutorialLeds": lprSnmpTutorialLeds,
       "led1": led1,
       "led2": led2,
       "led3": led3,
       "lprSnmpTutorialButtons": lprSnmpTutorialButtons,
       "sw1": sw1,
       "sw2": sw2,
       "sw3": sw3,
       "lprPointCast": lprPointCast,
       "lprPointCastCoils": lprPointCastCoils,
       "coil1": coil1,
       "coil2": coil2,
       "coil3": coil3,
       "lprPointCastDiscreteInputs": lprPointCastDiscreteInputs,
       "lprPointCastInputRegisters": lprPointCastInputRegisters,
       "lprMIBConformance": lprMIBConformance}
)
