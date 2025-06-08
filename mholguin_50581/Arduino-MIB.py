# SNMP MIB module (Arduino-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mholguin_50581/Arduino-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:29:05 2025
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

(ModuleIdentity,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "ModuleIdentity")

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

arduinoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50581)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50581, 1)
)


class _SysAnalogReference_Type(Integer32):
    """Custom type sysAnalogReference based on Integer32"""
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
        *(("default", 0),
          ("internal", 1),
          ("internal1V1", 2),
          ("internal2V56", 3),
          ("external", 4))
    )


_SysAnalogReference_Type.__name__ = "Integer32"
_SysAnalogReference_Object = MibScalar
sysAnalogReference = _SysAnalogReference_Object(
    (1, 3, 6, 1, 4, 1, 50581, 1, 1),
    _SysAnalogReference_Type()
)
sysAnalogReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAnalogReference.setStatus("current")


class _SysStatus_Type(Integer32):
    """Custom type sysStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halt", 0),
          ("running", 1),
          ("idle", 2))
    )


_SysStatus_Type.__name__ = "Integer32"
_SysStatus_Object = MibScalar
sysStatus = _SysStatus_Object(
    (1, 3, 6, 1, 4, 1, 50581, 1, 2),
    _SysStatus_Type()
)
sysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatus.setStatus("current")


class _SysFreeMem_Type(Integer32):
    """Custom type sysFreeMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SysFreeMem_Type.__name__ = "Integer32"
_SysFreeMem_Object = MibScalar
sysFreeMem = _SysFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 50581, 1, 3),
    _SysFreeMem_Type()
)
sysFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFreeMem.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50581, 2)
)


class _CfgD0_Type(Integer32):
    """Custom type cfgD0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("output", 0),
          ("input", 1),
          ("pullupInput", 2))
    )


_CfgD0_Type.__name__ = "Integer32"
_CfgD0_Object = MibScalar
cfgD0 = _CfgD0_Object(
    (1, 3, 6, 1, 4, 1, 50581, 2, 1),
    _CfgD0_Type()
)
cfgD0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgD0.setStatus("current")
_Value_ObjectIdentity = ObjectIdentity
value = _Value_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50581, 3)
)


class _ValA0_Type(Integer32):
    """Custom type valA0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ValA0_Type.__name__ = "Integer32"
_ValA0_Object = MibScalar
valA0 = _ValA0_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 1),
    _ValA0_Type()
)
valA0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valA0.setStatus("current")


class _ValA1_Type(Integer32):
    """Custom type valA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ValA1_Type.__name__ = "Integer32"
_ValA1_Object = MibScalar
valA1 = _ValA1_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 2),
    _ValA1_Type()
)
valA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valA1.setStatus("current")


class _ValA2_Type(Integer32):
    """Custom type valA2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ValA2_Type.__name__ = "Integer32"
_ValA2_Object = MibScalar
valA2 = _ValA2_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 3),
    _ValA2_Type()
)
valA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valA2.setStatus("current")


class _ValA3_Type(Integer32):
    """Custom type valA3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ValA3_Type.__name__ = "Integer32"
_ValA3_Object = MibScalar
valA3 = _ValA3_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 4),
    _ValA3_Type()
)
valA3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valA3.setStatus("current")


class _ValA4_Type(Integer32):
    """Custom type valA4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ValA4_Type.__name__ = "Integer32"
_ValA4_Object = MibScalar
valA4 = _ValA4_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 5),
    _ValA4_Type()
)
valA4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valA4.setStatus("current")


class _ValA5_Type(Integer32):
    """Custom type valA5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ValA5_Type.__name__ = "Integer32"
_ValA5_Object = MibScalar
valA5 = _ValA5_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 6),
    _ValA5_Type()
)
valA5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valA5.setStatus("current")


class _ValD0_Type(Integer32):
    """Custom type valD0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD0_Type.__name__ = "Integer32"
_ValD0_Object = MibScalar
valD0 = _ValD0_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 7),
    _ValD0_Type()
)
valD0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD0.setStatus("current")


class _ValD1_Type(Integer32):
    """Custom type valD1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD1_Type.__name__ = "Integer32"
_ValD1_Object = MibScalar
valD1 = _ValD1_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 8),
    _ValD1_Type()
)
valD1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD1.setStatus("current")


class _ValD2_Type(Integer32):
    """Custom type valD2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD2_Type.__name__ = "Integer32"
_ValD2_Object = MibScalar
valD2 = _ValD2_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 9),
    _ValD2_Type()
)
valD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD2.setStatus("current")


class _ValD3_Type(Integer32):
    """Custom type valD3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD3_Type.__name__ = "Integer32"
_ValD3_Object = MibScalar
valD3 = _ValD3_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 10),
    _ValD3_Type()
)
valD3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD3.setStatus("current")


class _ValD4_Type(Integer32):
    """Custom type valD4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD4_Type.__name__ = "Integer32"
_ValD4_Object = MibScalar
valD4 = _ValD4_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 11),
    _ValD4_Type()
)
valD4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD4.setStatus("current")


class _ValD5_Type(Integer32):
    """Custom type valD5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD5_Type.__name__ = "Integer32"
_ValD5_Object = MibScalar
valD5 = _ValD5_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 12),
    _ValD5_Type()
)
valD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD5.setStatus("current")


class _ValD6_Type(Integer32):
    """Custom type valD6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD6_Type.__name__ = "Integer32"
_ValD6_Object = MibScalar
valD6 = _ValD6_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 13),
    _ValD6_Type()
)
valD6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD6.setStatus("current")


class _ValD7_Type(Integer32):
    """Custom type valD7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD7_Type.__name__ = "Integer32"
_ValD7_Object = MibScalar
valD7 = _ValD7_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 14),
    _ValD7_Type()
)
valD7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD7.setStatus("current")


class _ValD8_Type(Integer32):
    """Custom type valD8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD8_Type.__name__ = "Integer32"
_ValD8_Object = MibScalar
valD8 = _ValD8_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 15),
    _ValD8_Type()
)
valD8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD8.setStatus("current")


class _ValD9_Type(Integer32):
    """Custom type valD9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD9_Type.__name__ = "Integer32"
_ValD9_Object = MibScalar
valD9 = _ValD9_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 16),
    _ValD9_Type()
)
valD9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD9.setStatus("current")


class _ValD10_Type(Integer32):
    """Custom type valD10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD10_Type.__name__ = "Integer32"
_ValD10_Object = MibScalar
valD10 = _ValD10_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 17),
    _ValD10_Type()
)
valD10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD10.setStatus("current")


class _ValD11_Type(Integer32):
    """Custom type valD11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD11_Type.__name__ = "Integer32"
_ValD11_Object = MibScalar
valD11 = _ValD11_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 18),
    _ValD11_Type()
)
valD11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD11.setStatus("current")


class _ValD12_Type(Integer32):
    """Custom type valD12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD12_Type.__name__ = "Integer32"
_ValD12_Object = MibScalar
valD12 = _ValD12_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 19),
    _ValD12_Type()
)
valD12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD12.setStatus("current")


class _ValD13_Type(Integer32):
    """Custom type valD13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ValD13_Type.__name__ = "Integer32"
_ValD13_Object = MibScalar
valD13 = _ValD13_Object(
    (1, 3, 6, 1, 4, 1, 50581, 3, 20),
    _ValD13_Type()
)
valD13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valD13.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Arduino-MIB",
    **{"arduinoMIB": arduinoMIB,
       "system": system,
       "sysAnalogReference": sysAnalogReference,
       "sysStatus": sysStatus,
       "sysFreeMem": sysFreeMem,
       "configuration": configuration,
       "cfgD0": cfgD0,
       "value": value,
       "valA0": valA0,
       "valA1": valA1,
       "valA2": valA2,
       "valA3": valA3,
       "valA4": valA4,
       "valA5": valA5,
       "valD0": valD0,
       "valD1": valD1,
       "valD2": valD2,
       "valD3": valD3,
       "valD4": valD4,
       "valD5": valD5,
       "valD6": valD6,
       "valD7": valD7,
       "valD8": valD8,
       "valD9": valD9,
       "valD10": valD10,
       "valD11": valD11,
       "valD12": valD12,
       "valD13": valD13}
)
