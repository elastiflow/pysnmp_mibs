# SNMP MIB module (MA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/comm5_48795/MA.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:50:32 2025
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

comm5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48795)
)


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MA_ObjectIdentity = ObjectIdentity
MA = _MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48795, 2)
)
_Configuration_ObjectIdentity = ObjectIdentity
Configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48795, 2, 1)
)
_CfgIP_Type = IpAddress
_CfgIP_Object = MibScalar
cfgIP = _CfgIP_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 1, 1),
    _CfgIP_Type()
)
cfgIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIP.setStatus("current")
_CfgMAC_Type = PhysAddress
_CfgMAC_Object = MibScalar
cfgMAC = _CfgMAC_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 1, 2),
    _CfgMAC_Type()
)
cfgMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgMAC.setStatus("current")
_RelayCTRL_ObjectIdentity = ObjectIdentity
RelayCTRL = _RelayCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48795, 2, 2)
)


class _Relay1_Type(Integer32):
    """Custom type relay1 based on Integer32"""
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


_Relay1_Type.__name__ = "Integer32"
_Relay1_Object = MibScalar
relay1 = _Relay1_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 2, 1),
    _Relay1_Type()
)
relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1.setStatus("current")


class _Relay2_Type(Integer32):
    """Custom type relay2 based on Integer32"""
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


_Relay2_Type.__name__ = "Integer32"
_Relay2_Object = MibScalar
relay2 = _Relay2_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 2, 2),
    _Relay2_Type()
)
relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2.setStatus("current")


class _Relay3_Type(Integer32):
    """Custom type relay3 based on Integer32"""
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


_Relay3_Type.__name__ = "Integer32"
_Relay3_Object = MibScalar
relay3 = _Relay3_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 2, 3),
    _Relay3_Type()
)
relay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3.setStatus("current")


class _Relay4_Type(Integer32):
    """Custom type relay4 based on Integer32"""
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


_Relay4_Type.__name__ = "Integer32"
_Relay4_Object = MibScalar
relay4 = _Relay4_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 2, 4),
    _Relay4_Type()
)
relay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4.setStatus("current")
_InputCTRL_ObjectIdentity = ObjectIdentity
InputCTRL = _InputCTRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3)
)


class _DigitalInput1_Type(Integer32):
    """Custom type digitalInput1 based on Integer32"""
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


_DigitalInput1_Type.__name__ = "Integer32"
_DigitalInput1_Object = MibScalar
digitalInput1 = _DigitalInput1_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 1),
    _DigitalInput1_Type()
)
digitalInput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput1.setStatus("mandatory")


class _DigitalInput2_Type(Integer32):
    """Custom type digitalInput2 based on Integer32"""
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


_DigitalInput2_Type.__name__ = "Integer32"
_DigitalInput2_Object = MibScalar
digitalInput2 = _DigitalInput2_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 2),
    _DigitalInput2_Type()
)
digitalInput2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput2.setStatus("mandatory")


class _DigitalInput3_Type(Integer32):
    """Custom type digitalInput3 based on Integer32"""
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


_DigitalInput3_Type.__name__ = "Integer32"
_DigitalInput3_Object = MibScalar
digitalInput3 = _DigitalInput3_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 3),
    _DigitalInput3_Type()
)
digitalInput3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput3.setStatus("mandatory")


class _DigitalInput4_Type(Integer32):
    """Custom type digitalInput4 based on Integer32"""
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


_DigitalInput4_Type.__name__ = "Integer32"
_DigitalInput4_Object = MibScalar
digitalInput4 = _DigitalInput4_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 4),
    _DigitalInput4_Type()
)
digitalInput4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput4.setStatus("mandatory")


class _DigitalInput5_Type(Integer32):
    """Custom type digitalInput5 based on Integer32"""
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


_DigitalInput5_Type.__name__ = "Integer32"
_DigitalInput5_Object = MibScalar
digitalInput5 = _DigitalInput5_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 5),
    _DigitalInput5_Type()
)
digitalInput5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput5.setStatus("mandatory")


class _DigitalInput6_Type(Integer32):
    """Custom type digitalInput6 based on Integer32"""
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


_DigitalInput6_Type.__name__ = "Integer32"
_DigitalInput6_Object = MibScalar
digitalInput6 = _DigitalInput6_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 6),
    _DigitalInput6_Type()
)
digitalInput6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput6.setStatus("mandatory")


class _DigitalInput7_Type(Integer32):
    """Custom type digitalInput7 based on Integer32"""
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


_DigitalInput7_Type.__name__ = "Integer32"
_DigitalInput7_Object = MibScalar
digitalInput7 = _DigitalInput7_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 7),
    _DigitalInput7_Type()
)
digitalInput7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput7.setStatus("mandatory")


class _DigitalInput8_Type(Integer32):
    """Custom type digitalInput8 based on Integer32"""
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


_DigitalInput8_Type.__name__ = "Integer32"
_DigitalInput8_Object = MibScalar
digitalInput8 = _DigitalInput8_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 8),
    _DigitalInput8_Type()
)
digitalInput8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput8.setStatus("mandatory")
_DigitalInputDWord_Type = Integer32
_DigitalInputDWord_Object = MibScalar
digitalInputDWord = _DigitalInputDWord_Object(
    (1, 3, 6, 1, 4, 1, 48795, 2, 3, 33),
    _DigitalInputDWord_Type()
)
digitalInputDWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputDWord.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MA",
    **{"PhysAddress": PhysAddress,
       "comm5": comm5,
       "MA": MA,
       "Configuration": Configuration,
       "cfgIP": cfgIP,
       "cfgMAC": cfgMAC,
       "RelayCTRL": RelayCTRL,
       "relay1": relay1,
       "relay2": relay2,
       "relay3": relay3,
       "relay4": relay4,
       "InputCTRL": InputCTRL,
       "digitalInput1": digitalInput1,
       "digitalInput2": digitalInput2,
       "digitalInput3": digitalInput3,
       "digitalInput4": digitalInput4,
       "digitalInput5": digitalInput5,
       "digitalInput6": digitalInput6,
       "digitalInput7": digitalInput7,
       "digitalInput8": digitalInput8,
       "digitalInputDWord": digitalInputDWord}
)
