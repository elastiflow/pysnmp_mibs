# SNMP MIB module (VMFIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/windmobile_44039/VMFIX-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 13:41:47 2025
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

_WindMobile_ObjectIdentity = ObjectIdentity
windMobile = _WindMobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039)
)
_Vmas_ObjectIdentity = ObjectIdentity
vmas = _Vmas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101)
)
_FREEROOTDISKVMAS_ObjectIdentity = ObjectIdentity
fREEROOTDISKVMAS = _FREEROOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1)
)
_I1100fREEROOTDISKVMAS_ObjectIdentity = ObjectIdentity
i1100fREEROOTDISKVMAS = _I1100fREEROOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1100)
)


class _Severityi1100fREEROOTDISKVMAS_Type(OctetString):
    """Custom type severityi1100fREEROOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100fREEROOTDISKVMAS_Type.__name__ = "OctetString"
_Severityi1100fREEROOTDISKVMAS_Object = MibScalar
severityi1100fREEROOTDISKVMAS = _Severityi1100fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1100, 1),
    _Severityi1100fREEROOTDISKVMAS_Type()
)
severityi1100fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100fREEROOTDISKVMAS.setStatus("mandatory")


class _Messagei1100fREEROOTDISKVMAS_Type(OctetString):
    """Custom type messagei1100fREEROOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100fREEROOTDISKVMAS_Type.__name__ = "OctetString"
_Messagei1100fREEROOTDISKVMAS_Object = MibScalar
messagei1100fREEROOTDISKVMAS = _Messagei1100fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1100, 2),
    _Messagei1100fREEROOTDISKVMAS_Type()
)
messagei1100fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100fREEROOTDISKVMAS.setStatus("mandatory")


class _Valuei1100fREEROOTDISKVMAS_Type(Integer32):
    """Custom type valuei1100fREEROOTDISKVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100fREEROOTDISKVMAS_Type.__name__ = "Integer32"
_Valuei1100fREEROOTDISKVMAS_Object = MibScalar
valuei1100fREEROOTDISKVMAS = _Valuei1100fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1100, 3),
    _Valuei1100fREEROOTDISKVMAS_Type()
)
valuei1100fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100fREEROOTDISKVMAS.setStatus("mandatory")
_I1101fREEROOTDISKVMASV1_ObjectIdentity = ObjectIdentity
i1101fREEROOTDISKVMASV1 = _I1101fREEROOTDISKVMASV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1101)
)
_I1200fREEROOTDISKVMAS_ObjectIdentity = ObjectIdentity
i1200fREEROOTDISKVMAS = _I1200fREEROOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1200)
)


class _Severityi1200fREEROOTDISKVMAS_Type(OctetString):
    """Custom type severityi1200fREEROOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200fREEROOTDISKVMAS_Type.__name__ = "OctetString"
_Severityi1200fREEROOTDISKVMAS_Object = MibScalar
severityi1200fREEROOTDISKVMAS = _Severityi1200fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1200, 1),
    _Severityi1200fREEROOTDISKVMAS_Type()
)
severityi1200fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200fREEROOTDISKVMAS.setStatus("mandatory")


class _Messagei1200fREEROOTDISKVMAS_Type(OctetString):
    """Custom type messagei1200fREEROOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200fREEROOTDISKVMAS_Type.__name__ = "OctetString"
_Messagei1200fREEROOTDISKVMAS_Object = MibScalar
messagei1200fREEROOTDISKVMAS = _Messagei1200fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1200, 2),
    _Messagei1200fREEROOTDISKVMAS_Type()
)
messagei1200fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200fREEROOTDISKVMAS.setStatus("mandatory")


class _Valuei1200fREEROOTDISKVMAS_Type(Integer32):
    """Custom type valuei1200fREEROOTDISKVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200fREEROOTDISKVMAS_Type.__name__ = "Integer32"
_Valuei1200fREEROOTDISKVMAS_Object = MibScalar
valuei1200fREEROOTDISKVMAS = _Valuei1200fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1200, 3),
    _Valuei1200fREEROOTDISKVMAS_Type()
)
valuei1200fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200fREEROOTDISKVMAS.setStatus("mandatory")
_I1300fREEROOTDISKVMAS_ObjectIdentity = ObjectIdentity
i1300fREEROOTDISKVMAS = _I1300fREEROOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1300)
)


class _Severityi1300fREEROOTDISKVMAS_Type(OctetString):
    """Custom type severityi1300fREEROOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300fREEROOTDISKVMAS_Type.__name__ = "OctetString"
_Severityi1300fREEROOTDISKVMAS_Object = MibScalar
severityi1300fREEROOTDISKVMAS = _Severityi1300fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1300, 1),
    _Severityi1300fREEROOTDISKVMAS_Type()
)
severityi1300fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300fREEROOTDISKVMAS.setStatus("mandatory")


class _Messagei1300fREEROOTDISKVMAS_Type(OctetString):
    """Custom type messagei1300fREEROOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300fREEROOTDISKVMAS_Type.__name__ = "OctetString"
_Messagei1300fREEROOTDISKVMAS_Object = MibScalar
messagei1300fREEROOTDISKVMAS = _Messagei1300fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1300, 2),
    _Messagei1300fREEROOTDISKVMAS_Type()
)
messagei1300fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300fREEROOTDISKVMAS.setStatus("mandatory")


class _Valuei1300fREEROOTDISKVMAS_Type(Integer32):
    """Custom type valuei1300fREEROOTDISKVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300fREEROOTDISKVMAS_Type.__name__ = "Integer32"
_Valuei1300fREEROOTDISKVMAS_Object = MibScalar
valuei1300fREEROOTDISKVMAS = _Valuei1300fREEROOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1300, 3),
    _Valuei1300fREEROOTDISKVMAS_Type()
)
valuei1300fREEROOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300fREEROOTDISKVMAS.setStatus("mandatory")
_FREEBOOTDISKVMAS_ObjectIdentity = ObjectIdentity
fREEBOOTDISKVMAS = _FREEBOOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2)
)
_I1100fREEBOOTDISKVMAS_ObjectIdentity = ObjectIdentity
i1100fREEBOOTDISKVMAS = _I1100fREEBOOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1100)
)


class _Severityi1100fREEBOOTDISKVMAS_Type(OctetString):
    """Custom type severityi1100fREEBOOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100fREEBOOTDISKVMAS_Type.__name__ = "OctetString"
_Severityi1100fREEBOOTDISKVMAS_Object = MibScalar
severityi1100fREEBOOTDISKVMAS = _Severityi1100fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1100, 1),
    _Severityi1100fREEBOOTDISKVMAS_Type()
)
severityi1100fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100fREEBOOTDISKVMAS.setStatus("mandatory")


class _Messagei1100fREEBOOTDISKVMAS_Type(OctetString):
    """Custom type messagei1100fREEBOOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100fREEBOOTDISKVMAS_Type.__name__ = "OctetString"
_Messagei1100fREEBOOTDISKVMAS_Object = MibScalar
messagei1100fREEBOOTDISKVMAS = _Messagei1100fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1100, 2),
    _Messagei1100fREEBOOTDISKVMAS_Type()
)
messagei1100fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100fREEBOOTDISKVMAS.setStatus("mandatory")


class _Valuei1100fREEBOOTDISKVMAS_Type(Integer32):
    """Custom type valuei1100fREEBOOTDISKVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100fREEBOOTDISKVMAS_Type.__name__ = "Integer32"
_Valuei1100fREEBOOTDISKVMAS_Object = MibScalar
valuei1100fREEBOOTDISKVMAS = _Valuei1100fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1100, 3),
    _Valuei1100fREEBOOTDISKVMAS_Type()
)
valuei1100fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100fREEBOOTDISKVMAS.setStatus("mandatory")
_I1200fREEBOOTDISKVMAS_ObjectIdentity = ObjectIdentity
i1200fREEBOOTDISKVMAS = _I1200fREEBOOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1200)
)


class _Severityi1200fREEBOOTDISKVMAS_Type(OctetString):
    """Custom type severityi1200fREEBOOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200fREEBOOTDISKVMAS_Type.__name__ = "OctetString"
_Severityi1200fREEBOOTDISKVMAS_Object = MibScalar
severityi1200fREEBOOTDISKVMAS = _Severityi1200fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1200, 1),
    _Severityi1200fREEBOOTDISKVMAS_Type()
)
severityi1200fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200fREEBOOTDISKVMAS.setStatus("mandatory")


class _Messagei1200fREEBOOTDISKVMAS_Type(OctetString):
    """Custom type messagei1200fREEBOOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200fREEBOOTDISKVMAS_Type.__name__ = "OctetString"
_Messagei1200fREEBOOTDISKVMAS_Object = MibScalar
messagei1200fREEBOOTDISKVMAS = _Messagei1200fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1200, 2),
    _Messagei1200fREEBOOTDISKVMAS_Type()
)
messagei1200fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200fREEBOOTDISKVMAS.setStatus("mandatory")


class _Valuei1200fREEBOOTDISKVMAS_Type(Integer32):
    """Custom type valuei1200fREEBOOTDISKVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200fREEBOOTDISKVMAS_Type.__name__ = "Integer32"
_Valuei1200fREEBOOTDISKVMAS_Object = MibScalar
valuei1200fREEBOOTDISKVMAS = _Valuei1200fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1200, 3),
    _Valuei1200fREEBOOTDISKVMAS_Type()
)
valuei1200fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200fREEBOOTDISKVMAS.setStatus("mandatory")
_I1300fREEBOOTDISKVMAS_ObjectIdentity = ObjectIdentity
i1300fREEBOOTDISKVMAS = _I1300fREEBOOTDISKVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1300)
)


class _Severityi1300fREEBOOTDISKVMAS_Type(OctetString):
    """Custom type severityi1300fREEBOOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300fREEBOOTDISKVMAS_Type.__name__ = "OctetString"
_Severityi1300fREEBOOTDISKVMAS_Object = MibScalar
severityi1300fREEBOOTDISKVMAS = _Severityi1300fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1300, 1),
    _Severityi1300fREEBOOTDISKVMAS_Type()
)
severityi1300fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300fREEBOOTDISKVMAS.setStatus("mandatory")


class _Messagei1300fREEBOOTDISKVMAS_Type(OctetString):
    """Custom type messagei1300fREEBOOTDISKVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300fREEBOOTDISKVMAS_Type.__name__ = "OctetString"
_Messagei1300fREEBOOTDISKVMAS_Object = MibScalar
messagei1300fREEBOOTDISKVMAS = _Messagei1300fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1300, 2),
    _Messagei1300fREEBOOTDISKVMAS_Type()
)
messagei1300fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300fREEBOOTDISKVMAS.setStatus("mandatory")


class _Valuei1300fREEBOOTDISKVMAS_Type(Integer32):
    """Custom type valuei1300fREEBOOTDISKVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300fREEBOOTDISKVMAS_Type.__name__ = "Integer32"
_Valuei1300fREEBOOTDISKVMAS_Object = MibScalar
valuei1300fREEBOOTDISKVMAS = _Valuei1300fREEBOOTDISKVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1300, 3),
    _Valuei1300fREEBOOTDISKVMAS_Type()
)
valuei1300fREEBOOTDISKVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300fREEBOOTDISKVMAS.setStatus("mandatory")
_FREEMEMORYVMAS_ObjectIdentity = ObjectIdentity
fREEMEMORYVMAS = _FREEMEMORYVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3)
)
_I1100fREEMEMORYVMAS_ObjectIdentity = ObjectIdentity
i1100fREEMEMORYVMAS = _I1100fREEMEMORYVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1100)
)


class _Severityi1100fREEMEMORYVMAS_Type(OctetString):
    """Custom type severityi1100fREEMEMORYVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100fREEMEMORYVMAS_Type.__name__ = "OctetString"
_Severityi1100fREEMEMORYVMAS_Object = MibScalar
severityi1100fREEMEMORYVMAS = _Severityi1100fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1100, 1),
    _Severityi1100fREEMEMORYVMAS_Type()
)
severityi1100fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100fREEMEMORYVMAS.setStatus("mandatory")


class _Messagei1100fREEMEMORYVMAS_Type(OctetString):
    """Custom type messagei1100fREEMEMORYVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100fREEMEMORYVMAS_Type.__name__ = "OctetString"
_Messagei1100fREEMEMORYVMAS_Object = MibScalar
messagei1100fREEMEMORYVMAS = _Messagei1100fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1100, 2),
    _Messagei1100fREEMEMORYVMAS_Type()
)
messagei1100fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100fREEMEMORYVMAS.setStatus("mandatory")


class _Valuei1100fREEMEMORYVMAS_Type(Integer32):
    """Custom type valuei1100fREEMEMORYVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100fREEMEMORYVMAS_Type.__name__ = "Integer32"
_Valuei1100fREEMEMORYVMAS_Object = MibScalar
valuei1100fREEMEMORYVMAS = _Valuei1100fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1100, 3),
    _Valuei1100fREEMEMORYVMAS_Type()
)
valuei1100fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100fREEMEMORYVMAS.setStatus("mandatory")
_I1200fREEMEMORYVMAS_ObjectIdentity = ObjectIdentity
i1200fREEMEMORYVMAS = _I1200fREEMEMORYVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1200)
)


class _Severityi1200fREEMEMORYVMAS_Type(OctetString):
    """Custom type severityi1200fREEMEMORYVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200fREEMEMORYVMAS_Type.__name__ = "OctetString"
_Severityi1200fREEMEMORYVMAS_Object = MibScalar
severityi1200fREEMEMORYVMAS = _Severityi1200fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1200, 1),
    _Severityi1200fREEMEMORYVMAS_Type()
)
severityi1200fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200fREEMEMORYVMAS.setStatus("mandatory")


class _Messagei1200fREEMEMORYVMAS_Type(OctetString):
    """Custom type messagei1200fREEMEMORYVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200fREEMEMORYVMAS_Type.__name__ = "OctetString"
_Messagei1200fREEMEMORYVMAS_Object = MibScalar
messagei1200fREEMEMORYVMAS = _Messagei1200fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1200, 2),
    _Messagei1200fREEMEMORYVMAS_Type()
)
messagei1200fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200fREEMEMORYVMAS.setStatus("mandatory")


class _Valuei1200fREEMEMORYVMAS_Type(Integer32):
    """Custom type valuei1200fREEMEMORYVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200fREEMEMORYVMAS_Type.__name__ = "Integer32"
_Valuei1200fREEMEMORYVMAS_Object = MibScalar
valuei1200fREEMEMORYVMAS = _Valuei1200fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1200, 3),
    _Valuei1200fREEMEMORYVMAS_Type()
)
valuei1200fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200fREEMEMORYVMAS.setStatus("mandatory")
_I1300fREEMEMORYVMAS_ObjectIdentity = ObjectIdentity
i1300fREEMEMORYVMAS = _I1300fREEMEMORYVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1300)
)


class _Severityi1300fREEMEMORYVMAS_Type(OctetString):
    """Custom type severityi1300fREEMEMORYVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300fREEMEMORYVMAS_Type.__name__ = "OctetString"
_Severityi1300fREEMEMORYVMAS_Object = MibScalar
severityi1300fREEMEMORYVMAS = _Severityi1300fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1300, 1),
    _Severityi1300fREEMEMORYVMAS_Type()
)
severityi1300fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300fREEMEMORYVMAS.setStatus("mandatory")


class _Messagei1300fREEMEMORYVMAS_Type(OctetString):
    """Custom type messagei1300fREEMEMORYVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300fREEMEMORYVMAS_Type.__name__ = "OctetString"
_Messagei1300fREEMEMORYVMAS_Object = MibScalar
messagei1300fREEMEMORYVMAS = _Messagei1300fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1300, 2),
    _Messagei1300fREEMEMORYVMAS_Type()
)
messagei1300fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300fREEMEMORYVMAS.setStatus("mandatory")


class _Valuei1300fREEMEMORYVMAS_Type(Integer32):
    """Custom type valuei1300fREEMEMORYVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300fREEMEMORYVMAS_Type.__name__ = "Integer32"
_Valuei1300fREEMEMORYVMAS_Object = MibScalar
valuei1300fREEMEMORYVMAS = _Valuei1300fREEMEMORYVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1300, 3),
    _Valuei1300fREEMEMORYVMAS_Type()
)
valuei1300fREEMEMORYVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300fREEMEMORYVMAS.setStatus("mandatory")
_CPULOADVMAS_ObjectIdentity = ObjectIdentity
cPULOADVMAS = _CPULOADVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4)
)
_I1100cPULOADVMAS_ObjectIdentity = ObjectIdentity
i1100cPULOADVMAS = _I1100cPULOADVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1100)
)


class _Severityi1100cPULOADVMAS_Type(OctetString):
    """Custom type severityi1100cPULOADVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100cPULOADVMAS_Type.__name__ = "OctetString"
_Severityi1100cPULOADVMAS_Object = MibScalar
severityi1100cPULOADVMAS = _Severityi1100cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1100, 1),
    _Severityi1100cPULOADVMAS_Type()
)
severityi1100cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100cPULOADVMAS.setStatus("mandatory")


class _Messagei1100cPULOADVMAS_Type(OctetString):
    """Custom type messagei1100cPULOADVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100cPULOADVMAS_Type.__name__ = "OctetString"
_Messagei1100cPULOADVMAS_Object = MibScalar
messagei1100cPULOADVMAS = _Messagei1100cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1100, 2),
    _Messagei1100cPULOADVMAS_Type()
)
messagei1100cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100cPULOADVMAS.setStatus("mandatory")


class _Valuei1100cPULOADVMAS_Type(Integer32):
    """Custom type valuei1100cPULOADVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100cPULOADVMAS_Type.__name__ = "Integer32"
_Valuei1100cPULOADVMAS_Object = MibScalar
valuei1100cPULOADVMAS = _Valuei1100cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1100, 3),
    _Valuei1100cPULOADVMAS_Type()
)
valuei1100cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100cPULOADVMAS.setStatus("mandatory")
_I1200cPULOADVMAS_ObjectIdentity = ObjectIdentity
i1200cPULOADVMAS = _I1200cPULOADVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1200)
)


class _Severityi1200cPULOADVMAS_Type(OctetString):
    """Custom type severityi1200cPULOADVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200cPULOADVMAS_Type.__name__ = "OctetString"
_Severityi1200cPULOADVMAS_Object = MibScalar
severityi1200cPULOADVMAS = _Severityi1200cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1200, 1),
    _Severityi1200cPULOADVMAS_Type()
)
severityi1200cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200cPULOADVMAS.setStatus("mandatory")


class _Messagei1200cPULOADVMAS_Type(OctetString):
    """Custom type messagei1200cPULOADVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200cPULOADVMAS_Type.__name__ = "OctetString"
_Messagei1200cPULOADVMAS_Object = MibScalar
messagei1200cPULOADVMAS = _Messagei1200cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1200, 2),
    _Messagei1200cPULOADVMAS_Type()
)
messagei1200cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200cPULOADVMAS.setStatus("mandatory")


class _Valuei1200cPULOADVMAS_Type(Integer32):
    """Custom type valuei1200cPULOADVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200cPULOADVMAS_Type.__name__ = "Integer32"
_Valuei1200cPULOADVMAS_Object = MibScalar
valuei1200cPULOADVMAS = _Valuei1200cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1200, 3),
    _Valuei1200cPULOADVMAS_Type()
)
valuei1200cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200cPULOADVMAS.setStatus("mandatory")
_I1300cPULOADVMAS_ObjectIdentity = ObjectIdentity
i1300cPULOADVMAS = _I1300cPULOADVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1300)
)


class _Severityi1300cPULOADVMAS_Type(OctetString):
    """Custom type severityi1300cPULOADVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300cPULOADVMAS_Type.__name__ = "OctetString"
_Severityi1300cPULOADVMAS_Object = MibScalar
severityi1300cPULOADVMAS = _Severityi1300cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1300, 1),
    _Severityi1300cPULOADVMAS_Type()
)
severityi1300cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300cPULOADVMAS.setStatus("mandatory")


class _Messagei1300cPULOADVMAS_Type(OctetString):
    """Custom type messagei1300cPULOADVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300cPULOADVMAS_Type.__name__ = "OctetString"
_Messagei1300cPULOADVMAS_Object = MibScalar
messagei1300cPULOADVMAS = _Messagei1300cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1300, 2),
    _Messagei1300cPULOADVMAS_Type()
)
messagei1300cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300cPULOADVMAS.setStatus("mandatory")


class _Valuei1300cPULOADVMAS_Type(Integer32):
    """Custom type valuei1300cPULOADVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300cPULOADVMAS_Type.__name__ = "Integer32"
_Valuei1300cPULOADVMAS_Object = MibScalar
valuei1300cPULOADVMAS = _Valuei1300cPULOADVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1300, 3),
    _Valuei1300cPULOADVMAS_Type()
)
valuei1300cPULOADVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300cPULOADVMAS.setStatus("mandatory")
_FREESWAPVMAS_ObjectIdentity = ObjectIdentity
fREESWAPVMAS = _FREESWAPVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5)
)
_I1100fREESWAPVMAS_ObjectIdentity = ObjectIdentity
i1100fREESWAPVMAS = _I1100fREESWAPVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1100)
)


class _Severityi1100fREESWAPVMAS_Type(OctetString):
    """Custom type severityi1100fREESWAPVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100fREESWAPVMAS_Type.__name__ = "OctetString"
_Severityi1100fREESWAPVMAS_Object = MibScalar
severityi1100fREESWAPVMAS = _Severityi1100fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1100, 1),
    _Severityi1100fREESWAPVMAS_Type()
)
severityi1100fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100fREESWAPVMAS.setStatus("mandatory")


class _Messagei1100fREESWAPVMAS_Type(OctetString):
    """Custom type messagei1100fREESWAPVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100fREESWAPVMAS_Type.__name__ = "OctetString"
_Messagei1100fREESWAPVMAS_Object = MibScalar
messagei1100fREESWAPVMAS = _Messagei1100fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1100, 2),
    _Messagei1100fREESWAPVMAS_Type()
)
messagei1100fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100fREESWAPVMAS.setStatus("mandatory")


class _Valuei1100fREESWAPVMAS_Type(Integer32):
    """Custom type valuei1100fREESWAPVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100fREESWAPVMAS_Type.__name__ = "Integer32"
_Valuei1100fREESWAPVMAS_Object = MibScalar
valuei1100fREESWAPVMAS = _Valuei1100fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1100, 3),
    _Valuei1100fREESWAPVMAS_Type()
)
valuei1100fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100fREESWAPVMAS.setStatus("mandatory")
_I1200fREESWAPVMAS_ObjectIdentity = ObjectIdentity
i1200fREESWAPVMAS = _I1200fREESWAPVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1200)
)


class _Severityi1200fREESWAPVMAS_Type(OctetString):
    """Custom type severityi1200fREESWAPVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200fREESWAPVMAS_Type.__name__ = "OctetString"
_Severityi1200fREESWAPVMAS_Object = MibScalar
severityi1200fREESWAPVMAS = _Severityi1200fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1200, 1),
    _Severityi1200fREESWAPVMAS_Type()
)
severityi1200fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200fREESWAPVMAS.setStatus("mandatory")


class _Messagei1200fREESWAPVMAS_Type(OctetString):
    """Custom type messagei1200fREESWAPVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200fREESWAPVMAS_Type.__name__ = "OctetString"
_Messagei1200fREESWAPVMAS_Object = MibScalar
messagei1200fREESWAPVMAS = _Messagei1200fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1200, 2),
    _Messagei1200fREESWAPVMAS_Type()
)
messagei1200fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200fREESWAPVMAS.setStatus("mandatory")


class _Valuei1200fREESWAPVMAS_Type(Integer32):
    """Custom type valuei1200fREESWAPVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200fREESWAPVMAS_Type.__name__ = "Integer32"
_Valuei1200fREESWAPVMAS_Object = MibScalar
valuei1200fREESWAPVMAS = _Valuei1200fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1200, 3),
    _Valuei1200fREESWAPVMAS_Type()
)
valuei1200fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200fREESWAPVMAS.setStatus("mandatory")
_I1300fREESWAPVMAS_ObjectIdentity = ObjectIdentity
i1300fREESWAPVMAS = _I1300fREESWAPVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1300)
)


class _Severityi1300fREESWAPVMAS_Type(OctetString):
    """Custom type severityi1300fREESWAPVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300fREESWAPVMAS_Type.__name__ = "OctetString"
_Severityi1300fREESWAPVMAS_Object = MibScalar
severityi1300fREESWAPVMAS = _Severityi1300fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1300, 1),
    _Severityi1300fREESWAPVMAS_Type()
)
severityi1300fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300fREESWAPVMAS.setStatus("mandatory")


class _Messagei1300fREESWAPVMAS_Type(OctetString):
    """Custom type messagei1300fREESWAPVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300fREESWAPVMAS_Type.__name__ = "OctetString"
_Messagei1300fREESWAPVMAS_Object = MibScalar
messagei1300fREESWAPVMAS = _Messagei1300fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1300, 2),
    _Messagei1300fREESWAPVMAS_Type()
)
messagei1300fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300fREESWAPVMAS.setStatus("mandatory")


class _Valuei1300fREESWAPVMAS_Type(Integer32):
    """Custom type valuei1300fREESWAPVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300fREESWAPVMAS_Type.__name__ = "Integer32"
_Valuei1300fREESWAPVMAS_Object = MibScalar
valuei1300fREESWAPVMAS = _Valuei1300fREESWAPVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1300, 3),
    _Valuei1300fREESWAPVMAS_Type()
)
valuei1300fREESWAPVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300fREESWAPVMAS.setStatus("mandatory")
_ETHINTSTATUSVMAS_ObjectIdentity = ObjectIdentity
eTHINTSTATUSVMAS = _ETHINTSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6)
)
_I1100eTHINTSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100eTHINTSTATUSVMAS = _I1100eTHINTSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1100)
)


class _Severityi1100eTHINTSTATUSVMAS_Type(OctetString):
    """Custom type severityi1100eTHINTSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100eTHINTSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100eTHINTSTATUSVMAS_Object = MibScalar
severityi1100eTHINTSTATUSVMAS = _Severityi1100eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1100, 1),
    _Severityi1100eTHINTSTATUSVMAS_Type()
)
severityi1100eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100eTHINTSTATUSVMAS.setStatus("mandatory")


class _Messagei1100eTHINTSTATUSVMAS_Type(OctetString):
    """Custom type messagei1100eTHINTSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100eTHINTSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100eTHINTSTATUSVMAS_Object = MibScalar
messagei1100eTHINTSTATUSVMAS = _Messagei1100eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1100, 2),
    _Messagei1100eTHINTSTATUSVMAS_Type()
)
messagei1100eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100eTHINTSTATUSVMAS.setStatus("mandatory")


class _Valuei1100eTHINTSTATUSVMAS_Type(Integer32):
    """Custom type valuei1100eTHINTSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100eTHINTSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100eTHINTSTATUSVMAS_Object = MibScalar
valuei1100eTHINTSTATUSVMAS = _Valuei1100eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1100, 3),
    _Valuei1100eTHINTSTATUSVMAS_Type()
)
valuei1100eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100eTHINTSTATUSVMAS.setStatus("mandatory")
_I1200eTHINTSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200eTHINTSTATUSVMAS = _I1200eTHINTSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1200)
)


class _Severityi1200eTHINTSTATUSVMAS_Type(OctetString):
    """Custom type severityi1200eTHINTSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200eTHINTSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200eTHINTSTATUSVMAS_Object = MibScalar
severityi1200eTHINTSTATUSVMAS = _Severityi1200eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1200, 1),
    _Severityi1200eTHINTSTATUSVMAS_Type()
)
severityi1200eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200eTHINTSTATUSVMAS.setStatus("mandatory")


class _Messagei1200eTHINTSTATUSVMAS_Type(OctetString):
    """Custom type messagei1200eTHINTSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200eTHINTSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200eTHINTSTATUSVMAS_Object = MibScalar
messagei1200eTHINTSTATUSVMAS = _Messagei1200eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1200, 2),
    _Messagei1200eTHINTSTATUSVMAS_Type()
)
messagei1200eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200eTHINTSTATUSVMAS.setStatus("mandatory")


class _Valuei1200eTHINTSTATUSVMAS_Type(Integer32):
    """Custom type valuei1200eTHINTSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200eTHINTSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200eTHINTSTATUSVMAS_Object = MibScalar
valuei1200eTHINTSTATUSVMAS = _Valuei1200eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1200, 3),
    _Valuei1200eTHINTSTATUSVMAS_Type()
)
valuei1200eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200eTHINTSTATUSVMAS.setStatus("mandatory")
_I1300eTHINTSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300eTHINTSTATUSVMAS = _I1300eTHINTSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1300)
)


class _Severityi1300eTHINTSTATUSVMAS_Type(OctetString):
    """Custom type severityi1300eTHINTSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300eTHINTSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300eTHINTSTATUSVMAS_Object = MibScalar
severityi1300eTHINTSTATUSVMAS = _Severityi1300eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1300, 1),
    _Severityi1300eTHINTSTATUSVMAS_Type()
)
severityi1300eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300eTHINTSTATUSVMAS.setStatus("mandatory")


class _Messagei1300eTHINTSTATUSVMAS_Type(OctetString):
    """Custom type messagei1300eTHINTSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300eTHINTSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300eTHINTSTATUSVMAS_Object = MibScalar
messagei1300eTHINTSTATUSVMAS = _Messagei1300eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1300, 2),
    _Messagei1300eTHINTSTATUSVMAS_Type()
)
messagei1300eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300eTHINTSTATUSVMAS.setStatus("mandatory")


class _Valuei1300eTHINTSTATUSVMAS_Type(Integer32):
    """Custom type valuei1300eTHINTSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300eTHINTSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300eTHINTSTATUSVMAS_Object = MibScalar
valuei1300eTHINTSTATUSVMAS = _Valuei1300eTHINTSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1300, 3),
    _Valuei1300eTHINTSTATUSVMAS_Type()
)
valuei1300eTHINTSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300eTHINTSTATUSVMAS.setStatus("mandatory")
_CRONSTATUSVMAS_ObjectIdentity = ObjectIdentity
cRONSTATUSVMAS = _CRONSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7)
)
_I1100cRONSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100cRONSTATUSVMAS = _I1100cRONSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1100)
)


class _Severityi1100cRONSTATUSVMAS_Type(OctetString):
    """Custom type severityi1100cRONSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100cRONSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100cRONSTATUSVMAS_Object = MibScalar
severityi1100cRONSTATUSVMAS = _Severityi1100cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1100, 1),
    _Severityi1100cRONSTATUSVMAS_Type()
)
severityi1100cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100cRONSTATUSVMAS.setStatus("mandatory")


class _Messagei1100cRONSTATUSVMAS_Type(OctetString):
    """Custom type messagei1100cRONSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100cRONSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100cRONSTATUSVMAS_Object = MibScalar
messagei1100cRONSTATUSVMAS = _Messagei1100cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1100, 2),
    _Messagei1100cRONSTATUSVMAS_Type()
)
messagei1100cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100cRONSTATUSVMAS.setStatus("mandatory")


class _Valuei1100cRONSTATUSVMAS_Type(Integer32):
    """Custom type valuei1100cRONSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100cRONSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100cRONSTATUSVMAS_Object = MibScalar
valuei1100cRONSTATUSVMAS = _Valuei1100cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1100, 3),
    _Valuei1100cRONSTATUSVMAS_Type()
)
valuei1100cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100cRONSTATUSVMAS.setStatus("mandatory")
_I1200cRONSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200cRONSTATUSVMAS = _I1200cRONSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1200)
)


class _Severityi1200cRONSTATUSVMAS_Type(OctetString):
    """Custom type severityi1200cRONSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200cRONSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200cRONSTATUSVMAS_Object = MibScalar
severityi1200cRONSTATUSVMAS = _Severityi1200cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1200, 1),
    _Severityi1200cRONSTATUSVMAS_Type()
)
severityi1200cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200cRONSTATUSVMAS.setStatus("mandatory")


class _Messagei1200cRONSTATUSVMAS_Type(OctetString):
    """Custom type messagei1200cRONSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200cRONSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200cRONSTATUSVMAS_Object = MibScalar
messagei1200cRONSTATUSVMAS = _Messagei1200cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1200, 2),
    _Messagei1200cRONSTATUSVMAS_Type()
)
messagei1200cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200cRONSTATUSVMAS.setStatus("mandatory")


class _Valuei1200cRONSTATUSVMAS_Type(Integer32):
    """Custom type valuei1200cRONSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200cRONSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200cRONSTATUSVMAS_Object = MibScalar
valuei1200cRONSTATUSVMAS = _Valuei1200cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1200, 3),
    _Valuei1200cRONSTATUSVMAS_Type()
)
valuei1200cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200cRONSTATUSVMAS.setStatus("mandatory")
_I1300cRONSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300cRONSTATUSVMAS = _I1300cRONSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1300)
)


class _Severityi1300cRONSTATUSVMAS_Type(OctetString):
    """Custom type severityi1300cRONSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300cRONSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300cRONSTATUSVMAS_Object = MibScalar
severityi1300cRONSTATUSVMAS = _Severityi1300cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1300, 1),
    _Severityi1300cRONSTATUSVMAS_Type()
)
severityi1300cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300cRONSTATUSVMAS.setStatus("mandatory")


class _Messagei1300cRONSTATUSVMAS_Type(OctetString):
    """Custom type messagei1300cRONSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300cRONSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300cRONSTATUSVMAS_Object = MibScalar
messagei1300cRONSTATUSVMAS = _Messagei1300cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1300, 2),
    _Messagei1300cRONSTATUSVMAS_Type()
)
messagei1300cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300cRONSTATUSVMAS.setStatus("mandatory")


class _Valuei1300cRONSTATUSVMAS_Type(Integer32):
    """Custom type valuei1300cRONSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300cRONSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300cRONSTATUSVMAS_Object = MibScalar
valuei1300cRONSTATUSVMAS = _Valuei1300cRONSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1300, 3),
    _Valuei1300cRONSTATUSVMAS_Type()
)
valuei1300cRONSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300cRONSTATUSVMAS.setStatus("mandatory")
_MONITSTATUSVMAS_ObjectIdentity = ObjectIdentity
mONITSTATUSVMAS = _MONITSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8)
)
_I1100mONITSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100mONITSTATUSVMAS = _I1100mONITSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1100)
)


class _Severityi1100mONITSTATUSVMAS_Type(OctetString):
    """Custom type severityi1100mONITSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100mONITSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100mONITSTATUSVMAS_Object = MibScalar
severityi1100mONITSTATUSVMAS = _Severityi1100mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1100, 1),
    _Severityi1100mONITSTATUSVMAS_Type()
)
severityi1100mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100mONITSTATUSVMAS.setStatus("mandatory")


class _Messagei1100mONITSTATUSVMAS_Type(OctetString):
    """Custom type messagei1100mONITSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100mONITSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100mONITSTATUSVMAS_Object = MibScalar
messagei1100mONITSTATUSVMAS = _Messagei1100mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1100, 2),
    _Messagei1100mONITSTATUSVMAS_Type()
)
messagei1100mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100mONITSTATUSVMAS.setStatus("mandatory")


class _Valuei1100mONITSTATUSVMAS_Type(Integer32):
    """Custom type valuei1100mONITSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100mONITSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100mONITSTATUSVMAS_Object = MibScalar
valuei1100mONITSTATUSVMAS = _Valuei1100mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1100, 3),
    _Valuei1100mONITSTATUSVMAS_Type()
)
valuei1100mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100mONITSTATUSVMAS.setStatus("mandatory")
_I1200mONITSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200mONITSTATUSVMAS = _I1200mONITSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1200)
)


class _Severityi1200mONITSTATUSVMAS_Type(OctetString):
    """Custom type severityi1200mONITSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200mONITSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200mONITSTATUSVMAS_Object = MibScalar
severityi1200mONITSTATUSVMAS = _Severityi1200mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1200, 1),
    _Severityi1200mONITSTATUSVMAS_Type()
)
severityi1200mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200mONITSTATUSVMAS.setStatus("mandatory")


class _Messagei1200mONITSTATUSVMAS_Type(OctetString):
    """Custom type messagei1200mONITSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200mONITSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200mONITSTATUSVMAS_Object = MibScalar
messagei1200mONITSTATUSVMAS = _Messagei1200mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1200, 2),
    _Messagei1200mONITSTATUSVMAS_Type()
)
messagei1200mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200mONITSTATUSVMAS.setStatus("mandatory")


class _Valuei1200mONITSTATUSVMAS_Type(Integer32):
    """Custom type valuei1200mONITSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200mONITSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200mONITSTATUSVMAS_Object = MibScalar
valuei1200mONITSTATUSVMAS = _Valuei1200mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1200, 3),
    _Valuei1200mONITSTATUSVMAS_Type()
)
valuei1200mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200mONITSTATUSVMAS.setStatus("mandatory")
_I1300mONITSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300mONITSTATUSVMAS = _I1300mONITSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1300)
)


class _Severityi1300mONITSTATUSVMAS_Type(OctetString):
    """Custom type severityi1300mONITSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300mONITSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300mONITSTATUSVMAS_Object = MibScalar
severityi1300mONITSTATUSVMAS = _Severityi1300mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1300, 1),
    _Severityi1300mONITSTATUSVMAS_Type()
)
severityi1300mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300mONITSTATUSVMAS.setStatus("mandatory")


class _Messagei1300mONITSTATUSVMAS_Type(OctetString):
    """Custom type messagei1300mONITSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300mONITSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300mONITSTATUSVMAS_Object = MibScalar
messagei1300mONITSTATUSVMAS = _Messagei1300mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1300, 2),
    _Messagei1300mONITSTATUSVMAS_Type()
)
messagei1300mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300mONITSTATUSVMAS.setStatus("mandatory")


class _Valuei1300mONITSTATUSVMAS_Type(Integer32):
    """Custom type valuei1300mONITSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300mONITSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300mONITSTATUSVMAS_Object = MibScalar
valuei1300mONITSTATUSVMAS = _Valuei1300mONITSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1300, 3),
    _Valuei1300mONITSTATUSVMAS_Type()
)
valuei1300mONITSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300mONITSTATUSVMAS.setStatus("mandatory")
_DNSMASQSTATUSVMAS_ObjectIdentity = ObjectIdentity
dNSMASQSTATUSVMAS = _DNSMASQSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9)
)
_I1100dNSMASQSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100dNSMASQSTATUSVMAS = _I1100dNSMASQSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1100)
)


class _Severityi1100dNSMASQSTATUSVMAS_Type(OctetString):
    """Custom type severityi1100dNSMASQSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100dNSMASQSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100dNSMASQSTATUSVMAS_Object = MibScalar
severityi1100dNSMASQSTATUSVMAS = _Severityi1100dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1100, 1),
    _Severityi1100dNSMASQSTATUSVMAS_Type()
)
severityi1100dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100dNSMASQSTATUSVMAS.setStatus("mandatory")


class _Messagei1100dNSMASQSTATUSVMAS_Type(OctetString):
    """Custom type messagei1100dNSMASQSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100dNSMASQSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100dNSMASQSTATUSVMAS_Object = MibScalar
messagei1100dNSMASQSTATUSVMAS = _Messagei1100dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1100, 2),
    _Messagei1100dNSMASQSTATUSVMAS_Type()
)
messagei1100dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100dNSMASQSTATUSVMAS.setStatus("mandatory")


class _Valuei1100dNSMASQSTATUSVMAS_Type(Integer32):
    """Custom type valuei1100dNSMASQSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100dNSMASQSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100dNSMASQSTATUSVMAS_Object = MibScalar
valuei1100dNSMASQSTATUSVMAS = _Valuei1100dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1100, 3),
    _Valuei1100dNSMASQSTATUSVMAS_Type()
)
valuei1100dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100dNSMASQSTATUSVMAS.setStatus("mandatory")
_I1200dNSMASQSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200dNSMASQSTATUSVMAS = _I1200dNSMASQSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1200)
)


class _Severityi1200dNSMASQSTATUSVMAS_Type(OctetString):
    """Custom type severityi1200dNSMASQSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200dNSMASQSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200dNSMASQSTATUSVMAS_Object = MibScalar
severityi1200dNSMASQSTATUSVMAS = _Severityi1200dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1200, 1),
    _Severityi1200dNSMASQSTATUSVMAS_Type()
)
severityi1200dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200dNSMASQSTATUSVMAS.setStatus("mandatory")


class _Messagei1200dNSMASQSTATUSVMAS_Type(OctetString):
    """Custom type messagei1200dNSMASQSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200dNSMASQSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200dNSMASQSTATUSVMAS_Object = MibScalar
messagei1200dNSMASQSTATUSVMAS = _Messagei1200dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1200, 2),
    _Messagei1200dNSMASQSTATUSVMAS_Type()
)
messagei1200dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200dNSMASQSTATUSVMAS.setStatus("mandatory")


class _Valuei1200dNSMASQSTATUSVMAS_Type(Integer32):
    """Custom type valuei1200dNSMASQSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200dNSMASQSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200dNSMASQSTATUSVMAS_Object = MibScalar
valuei1200dNSMASQSTATUSVMAS = _Valuei1200dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1200, 3),
    _Valuei1200dNSMASQSTATUSVMAS_Type()
)
valuei1200dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200dNSMASQSTATUSVMAS.setStatus("mandatory")
_I1300dNSMASQSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300dNSMASQSTATUSVMAS = _I1300dNSMASQSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1300)
)


class _Severityi1300dNSMASQSTATUSVMAS_Type(OctetString):
    """Custom type severityi1300dNSMASQSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300dNSMASQSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300dNSMASQSTATUSVMAS_Object = MibScalar
severityi1300dNSMASQSTATUSVMAS = _Severityi1300dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1300, 1),
    _Severityi1300dNSMASQSTATUSVMAS_Type()
)
severityi1300dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300dNSMASQSTATUSVMAS.setStatus("mandatory")


class _Messagei1300dNSMASQSTATUSVMAS_Type(OctetString):
    """Custom type messagei1300dNSMASQSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300dNSMASQSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300dNSMASQSTATUSVMAS_Object = MibScalar
messagei1300dNSMASQSTATUSVMAS = _Messagei1300dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1300, 2),
    _Messagei1300dNSMASQSTATUSVMAS_Type()
)
messagei1300dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300dNSMASQSTATUSVMAS.setStatus("mandatory")


class _Valuei1300dNSMASQSTATUSVMAS_Type(Integer32):
    """Custom type valuei1300dNSMASQSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300dNSMASQSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300dNSMASQSTATUSVMAS_Object = MibScalar
valuei1300dNSMASQSTATUSVMAS = _Valuei1300dNSMASQSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1300, 3),
    _Valuei1300dNSMASQSTATUSVMAS_Type()
)
valuei1300dNSMASQSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300dNSMASQSTATUSVMAS.setStatus("mandatory")
_HB2STATUSVMAS_ObjectIdentity = ObjectIdentity
hB2STATUSVMAS = _HB2STATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11)
)
_I1100hB2STATUSVMAS_ObjectIdentity = ObjectIdentity
i1100hB2STATUSVMAS = _I1100hB2STATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1100)
)


class _Severityi1100hB2STATUSVMAS_Type(OctetString):
    """Custom type severityi1100hB2STATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100hB2STATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100hB2STATUSVMAS_Object = MibScalar
severityi1100hB2STATUSVMAS = _Severityi1100hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1100, 1),
    _Severityi1100hB2STATUSVMAS_Type()
)
severityi1100hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100hB2STATUSVMAS.setStatus("mandatory")


class _Messagei1100hB2STATUSVMAS_Type(OctetString):
    """Custom type messagei1100hB2STATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100hB2STATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100hB2STATUSVMAS_Object = MibScalar
messagei1100hB2STATUSVMAS = _Messagei1100hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1100, 2),
    _Messagei1100hB2STATUSVMAS_Type()
)
messagei1100hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100hB2STATUSVMAS.setStatus("mandatory")


class _Valuei1100hB2STATUSVMAS_Type(Integer32):
    """Custom type valuei1100hB2STATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100hB2STATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100hB2STATUSVMAS_Object = MibScalar
valuei1100hB2STATUSVMAS = _Valuei1100hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1100, 3),
    _Valuei1100hB2STATUSVMAS_Type()
)
valuei1100hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100hB2STATUSVMAS.setStatus("mandatory")
_I1200hB2STATUSVMAS_ObjectIdentity = ObjectIdentity
i1200hB2STATUSVMAS = _I1200hB2STATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1200)
)


class _Severityi1200hB2STATUSVMAS_Type(OctetString):
    """Custom type severityi1200hB2STATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200hB2STATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200hB2STATUSVMAS_Object = MibScalar
severityi1200hB2STATUSVMAS = _Severityi1200hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1200, 1),
    _Severityi1200hB2STATUSVMAS_Type()
)
severityi1200hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200hB2STATUSVMAS.setStatus("mandatory")


class _Messagei1200hB2STATUSVMAS_Type(OctetString):
    """Custom type messagei1200hB2STATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200hB2STATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200hB2STATUSVMAS_Object = MibScalar
messagei1200hB2STATUSVMAS = _Messagei1200hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1200, 2),
    _Messagei1200hB2STATUSVMAS_Type()
)
messagei1200hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200hB2STATUSVMAS.setStatus("mandatory")


class _Valuei1200hB2STATUSVMAS_Type(Integer32):
    """Custom type valuei1200hB2STATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200hB2STATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200hB2STATUSVMAS_Object = MibScalar
valuei1200hB2STATUSVMAS = _Valuei1200hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1200, 3),
    _Valuei1200hB2STATUSVMAS_Type()
)
valuei1200hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200hB2STATUSVMAS.setStatus("mandatory")
_I1300hB2STATUSVMAS_ObjectIdentity = ObjectIdentity
i1300hB2STATUSVMAS = _I1300hB2STATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1300)
)


class _Severityi1300hB2STATUSVMAS_Type(OctetString):
    """Custom type severityi1300hB2STATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300hB2STATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300hB2STATUSVMAS_Object = MibScalar
severityi1300hB2STATUSVMAS = _Severityi1300hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1300, 1),
    _Severityi1300hB2STATUSVMAS_Type()
)
severityi1300hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300hB2STATUSVMAS.setStatus("mandatory")


class _Messagei1300hB2STATUSVMAS_Type(OctetString):
    """Custom type messagei1300hB2STATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300hB2STATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300hB2STATUSVMAS_Object = MibScalar
messagei1300hB2STATUSVMAS = _Messagei1300hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1300, 2),
    _Messagei1300hB2STATUSVMAS_Type()
)
messagei1300hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300hB2STATUSVMAS.setStatus("mandatory")


class _Valuei1300hB2STATUSVMAS_Type(Integer32):
    """Custom type valuei1300hB2STATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300hB2STATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300hB2STATUSVMAS_Object = MibScalar
valuei1300hB2STATUSVMAS = _Valuei1300hB2STATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1300, 3),
    _Valuei1300hB2STATUSVMAS_Type()
)
valuei1300hB2STATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300hB2STATUSVMAS.setStatus("mandatory")
_TOMCATSTATUSVMAS_ObjectIdentity = ObjectIdentity
tOMCATSTATUSVMAS = _TOMCATSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13)
)
_I1100tOMCATSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100tOMCATSTATUSVMAS = _I1100tOMCATSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1100)
)


class _Severityi1100tOMCATSTATUSVMAS_Type(OctetString):
    """Custom type severityi1100tOMCATSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100tOMCATSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100tOMCATSTATUSVMAS_Object = MibScalar
severityi1100tOMCATSTATUSVMAS = _Severityi1100tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1100, 1),
    _Severityi1100tOMCATSTATUSVMAS_Type()
)
severityi1100tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100tOMCATSTATUSVMAS.setStatus("mandatory")


class _Messagei1100tOMCATSTATUSVMAS_Type(OctetString):
    """Custom type messagei1100tOMCATSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100tOMCATSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100tOMCATSTATUSVMAS_Object = MibScalar
messagei1100tOMCATSTATUSVMAS = _Messagei1100tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1100, 2),
    _Messagei1100tOMCATSTATUSVMAS_Type()
)
messagei1100tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100tOMCATSTATUSVMAS.setStatus("mandatory")


class _Valuei1100tOMCATSTATUSVMAS_Type(Integer32):
    """Custom type valuei1100tOMCATSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100tOMCATSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100tOMCATSTATUSVMAS_Object = MibScalar
valuei1100tOMCATSTATUSVMAS = _Valuei1100tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1100, 3),
    _Valuei1100tOMCATSTATUSVMAS_Type()
)
valuei1100tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100tOMCATSTATUSVMAS.setStatus("mandatory")
_I1200tOMCATSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200tOMCATSTATUSVMAS = _I1200tOMCATSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1200)
)


class _Severityi1200tOMCATSTATUSVMAS_Type(OctetString):
    """Custom type severityi1200tOMCATSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200tOMCATSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200tOMCATSTATUSVMAS_Object = MibScalar
severityi1200tOMCATSTATUSVMAS = _Severityi1200tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1200, 1),
    _Severityi1200tOMCATSTATUSVMAS_Type()
)
severityi1200tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200tOMCATSTATUSVMAS.setStatus("mandatory")


class _Messagei1200tOMCATSTATUSVMAS_Type(OctetString):
    """Custom type messagei1200tOMCATSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200tOMCATSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200tOMCATSTATUSVMAS_Object = MibScalar
messagei1200tOMCATSTATUSVMAS = _Messagei1200tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1200, 2),
    _Messagei1200tOMCATSTATUSVMAS_Type()
)
messagei1200tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200tOMCATSTATUSVMAS.setStatus("mandatory")


class _Valuei1200tOMCATSTATUSVMAS_Type(Integer32):
    """Custom type valuei1200tOMCATSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200tOMCATSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200tOMCATSTATUSVMAS_Object = MibScalar
valuei1200tOMCATSTATUSVMAS = _Valuei1200tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1200, 3),
    _Valuei1200tOMCATSTATUSVMAS_Type()
)
valuei1200tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200tOMCATSTATUSVMAS.setStatus("mandatory")
_I1300tOMCATSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300tOMCATSTATUSVMAS = _I1300tOMCATSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1300)
)


class _Severityi1300tOMCATSTATUSVMAS_Type(OctetString):
    """Custom type severityi1300tOMCATSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300tOMCATSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300tOMCATSTATUSVMAS_Object = MibScalar
severityi1300tOMCATSTATUSVMAS = _Severityi1300tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1300, 1),
    _Severityi1300tOMCATSTATUSVMAS_Type()
)
severityi1300tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300tOMCATSTATUSVMAS.setStatus("mandatory")


class _Messagei1300tOMCATSTATUSVMAS_Type(OctetString):
    """Custom type messagei1300tOMCATSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300tOMCATSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300tOMCATSTATUSVMAS_Object = MibScalar
messagei1300tOMCATSTATUSVMAS = _Messagei1300tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1300, 2),
    _Messagei1300tOMCATSTATUSVMAS_Type()
)
messagei1300tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300tOMCATSTATUSVMAS.setStatus("mandatory")


class _Valuei1300tOMCATSTATUSVMAS_Type(Integer32):
    """Custom type valuei1300tOMCATSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300tOMCATSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300tOMCATSTATUSVMAS_Object = MibScalar
valuei1300tOMCATSTATUSVMAS = _Valuei1300tOMCATSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1300, 3),
    _Valuei1300tOMCATSTATUSVMAS_Type()
)
valuei1300tOMCATSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300tOMCATSTATUSVMAS.setStatus("mandatory")
_CPUSTATUSVMAS_ObjectIdentity = ObjectIdentity
cPUSTATUSVMAS = _CPUSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18)
)
_I1100cPUSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100cPUSTATUSVMAS = _I1100cPUSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1100)
)


class _Severityi1100cPUSTATUSVMAS_Type(OctetString):
    """Custom type severityi1100cPUSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100cPUSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100cPUSTATUSVMAS_Object = MibScalar
severityi1100cPUSTATUSVMAS = _Severityi1100cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1100, 1),
    _Severityi1100cPUSTATUSVMAS_Type()
)
severityi1100cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100cPUSTATUSVMAS.setStatus("mandatory")


class _Messagei1100cPUSTATUSVMAS_Type(OctetString):
    """Custom type messagei1100cPUSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100cPUSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100cPUSTATUSVMAS_Object = MibScalar
messagei1100cPUSTATUSVMAS = _Messagei1100cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1100, 2),
    _Messagei1100cPUSTATUSVMAS_Type()
)
messagei1100cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100cPUSTATUSVMAS.setStatus("mandatory")


class _Valuei1100cPUSTATUSVMAS_Type(Integer32):
    """Custom type valuei1100cPUSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100cPUSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100cPUSTATUSVMAS_Object = MibScalar
valuei1100cPUSTATUSVMAS = _Valuei1100cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1100, 3),
    _Valuei1100cPUSTATUSVMAS_Type()
)
valuei1100cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100cPUSTATUSVMAS.setStatus("mandatory")
_I1200cPUSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200cPUSTATUSVMAS = _I1200cPUSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1200)
)


class _Severityi1200cPUSTATUSVMAS_Type(OctetString):
    """Custom type severityi1200cPUSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200cPUSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200cPUSTATUSVMAS_Object = MibScalar
severityi1200cPUSTATUSVMAS = _Severityi1200cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1200, 1),
    _Severityi1200cPUSTATUSVMAS_Type()
)
severityi1200cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200cPUSTATUSVMAS.setStatus("mandatory")


class _Messagei1200cPUSTATUSVMAS_Type(OctetString):
    """Custom type messagei1200cPUSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200cPUSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200cPUSTATUSVMAS_Object = MibScalar
messagei1200cPUSTATUSVMAS = _Messagei1200cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1200, 2),
    _Messagei1200cPUSTATUSVMAS_Type()
)
messagei1200cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200cPUSTATUSVMAS.setStatus("mandatory")


class _Valuei1200cPUSTATUSVMAS_Type(Integer32):
    """Custom type valuei1200cPUSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200cPUSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200cPUSTATUSVMAS_Object = MibScalar
valuei1200cPUSTATUSVMAS = _Valuei1200cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1200, 3),
    _Valuei1200cPUSTATUSVMAS_Type()
)
valuei1200cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200cPUSTATUSVMAS.setStatus("mandatory")
_I1300cPUSTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300cPUSTATUSVMAS = _I1300cPUSTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1300)
)


class _Severityi1300cPUSTATUSVMAS_Type(OctetString):
    """Custom type severityi1300cPUSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300cPUSTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300cPUSTATUSVMAS_Object = MibScalar
severityi1300cPUSTATUSVMAS = _Severityi1300cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1300, 1),
    _Severityi1300cPUSTATUSVMAS_Type()
)
severityi1300cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300cPUSTATUSVMAS.setStatus("mandatory")


class _Messagei1300cPUSTATUSVMAS_Type(OctetString):
    """Custom type messagei1300cPUSTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300cPUSTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300cPUSTATUSVMAS_Object = MibScalar
messagei1300cPUSTATUSVMAS = _Messagei1300cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1300, 2),
    _Messagei1300cPUSTATUSVMAS_Type()
)
messagei1300cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300cPUSTATUSVMAS.setStatus("mandatory")


class _Valuei1300cPUSTATUSVMAS_Type(Integer32):
    """Custom type valuei1300cPUSTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300cPUSTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300cPUSTATUSVMAS_Object = MibScalar
valuei1300cPUSTATUSVMAS = _Valuei1300cPUSTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1300, 3),
    _Valuei1300cPUSTATUSVMAS_Type()
)
valuei1300cPUSTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300cPUSTATUSVMAS.setStatus("mandatory")
_VMCORESTATUSVMAS_ObjectIdentity = ObjectIdentity
vMCORESTATUSVMAS = _VMCORESTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20)
)
_I1100vMCORESTATUSVMAS_ObjectIdentity = ObjectIdentity
i1100vMCORESTATUSVMAS = _I1100vMCORESTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1100)
)


class _Severityi1100vMCORESTATUSVMAS_Type(OctetString):
    """Custom type severityi1100vMCORESTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1100vMCORESTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1100vMCORESTATUSVMAS_Object = MibScalar
severityi1100vMCORESTATUSVMAS = _Severityi1100vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1100, 1),
    _Severityi1100vMCORESTATUSVMAS_Type()
)
severityi1100vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1100vMCORESTATUSVMAS.setStatus("mandatory")


class _Messagei1100vMCORESTATUSVMAS_Type(OctetString):
    """Custom type messagei1100vMCORESTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1100vMCORESTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1100vMCORESTATUSVMAS_Object = MibScalar
messagei1100vMCORESTATUSVMAS = _Messagei1100vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1100, 2),
    _Messagei1100vMCORESTATUSVMAS_Type()
)
messagei1100vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1100vMCORESTATUSVMAS.setStatus("mandatory")


class _Valuei1100vMCORESTATUSVMAS_Type(Integer32):
    """Custom type valuei1100vMCORESTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1100vMCORESTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1100vMCORESTATUSVMAS_Object = MibScalar
valuei1100vMCORESTATUSVMAS = _Valuei1100vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1100, 3),
    _Valuei1100vMCORESTATUSVMAS_Type()
)
valuei1100vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1100vMCORESTATUSVMAS.setStatus("mandatory")
_I1200vMCORESTATUSVMAS_ObjectIdentity = ObjectIdentity
i1200vMCORESTATUSVMAS = _I1200vMCORESTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1200)
)


class _Severityi1200vMCORESTATUSVMAS_Type(OctetString):
    """Custom type severityi1200vMCORESTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1200vMCORESTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1200vMCORESTATUSVMAS_Object = MibScalar
severityi1200vMCORESTATUSVMAS = _Severityi1200vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1200, 1),
    _Severityi1200vMCORESTATUSVMAS_Type()
)
severityi1200vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1200vMCORESTATUSVMAS.setStatus("mandatory")


class _Messagei1200vMCORESTATUSVMAS_Type(OctetString):
    """Custom type messagei1200vMCORESTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1200vMCORESTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1200vMCORESTATUSVMAS_Object = MibScalar
messagei1200vMCORESTATUSVMAS = _Messagei1200vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1200, 2),
    _Messagei1200vMCORESTATUSVMAS_Type()
)
messagei1200vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1200vMCORESTATUSVMAS.setStatus("mandatory")


class _Valuei1200vMCORESTATUSVMAS_Type(Integer32):
    """Custom type valuei1200vMCORESTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1200vMCORESTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1200vMCORESTATUSVMAS_Object = MibScalar
valuei1200vMCORESTATUSVMAS = _Valuei1200vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1200, 3),
    _Valuei1200vMCORESTATUSVMAS_Type()
)
valuei1200vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1200vMCORESTATUSVMAS.setStatus("mandatory")
_I1300vMCORESTATUSVMAS_ObjectIdentity = ObjectIdentity
i1300vMCORESTATUSVMAS = _I1300vMCORESTATUSVMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1300)
)


class _Severityi1300vMCORESTATUSVMAS_Type(OctetString):
    """Custom type severityi1300vMCORESTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi1300vMCORESTATUSVMAS_Type.__name__ = "OctetString"
_Severityi1300vMCORESTATUSVMAS_Object = MibScalar
severityi1300vMCORESTATUSVMAS = _Severityi1300vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1300, 1),
    _Severityi1300vMCORESTATUSVMAS_Type()
)
severityi1300vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi1300vMCORESTATUSVMAS.setStatus("mandatory")


class _Messagei1300vMCORESTATUSVMAS_Type(OctetString):
    """Custom type messagei1300vMCORESTATUSVMAS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei1300vMCORESTATUSVMAS_Type.__name__ = "OctetString"
_Messagei1300vMCORESTATUSVMAS_Object = MibScalar
messagei1300vMCORESTATUSVMAS = _Messagei1300vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1300, 2),
    _Messagei1300vMCORESTATUSVMAS_Type()
)
messagei1300vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei1300vMCORESTATUSVMAS.setStatus("mandatory")


class _Valuei1300vMCORESTATUSVMAS_Type(Integer32):
    """Custom type valuei1300vMCORESTATUSVMAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei1300vMCORESTATUSVMAS_Type.__name__ = "Integer32"
_Valuei1300vMCORESTATUSVMAS_Object = MibScalar
valuei1300vMCORESTATUSVMAS = _Valuei1300vMCORESTATUSVMAS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1300, 3),
    _Valuei1300vMCORESTATUSVMAS_Type()
)
valuei1300vMCORESTATUSVMAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei1300vMCORESTATUSVMAS.setStatus("mandatory")
_Vmms_ObjectIdentity = ObjectIdentity
vmms = _Vmms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102)
)
_FREEROOTDISKVMMS_ObjectIdentity = ObjectIdentity
fREEROOTDISKVMMS = _FREEROOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1)
)
_I2100fREEROOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2100fREEROOTDISKVMMS = _I2100fREEROOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2100)
)


class _Severityi2100fREEROOTDISKVMMS_Type(OctetString):
    """Custom type severityi2100fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2100fREEROOTDISKVMMS_Object = MibScalar
severityi2100fREEROOTDISKVMMS = _Severityi2100fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2100, 1),
    _Severityi2100fREEROOTDISKVMMS_Type()
)
severityi2100fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100fREEROOTDISKVMMS.setStatus("mandatory")


class _Messagei2100fREEROOTDISKVMMS_Type(OctetString):
    """Custom type messagei2100fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2100fREEROOTDISKVMMS_Object = MibScalar
messagei2100fREEROOTDISKVMMS = _Messagei2100fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2100, 2),
    _Messagei2100fREEROOTDISKVMMS_Type()
)
messagei2100fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100fREEROOTDISKVMMS.setStatus("mandatory")


class _Valuei2100fREEROOTDISKVMMS_Type(Integer32):
    """Custom type valuei2100fREEROOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100fREEROOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2100fREEROOTDISKVMMS_Object = MibScalar
valuei2100fREEROOTDISKVMMS = _Valuei2100fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2100, 3),
    _Valuei2100fREEROOTDISKVMMS_Type()
)
valuei2100fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100fREEROOTDISKVMMS.setStatus("mandatory")
_I2200fREEROOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2200fREEROOTDISKVMMS = _I2200fREEROOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2200)
)


class _Severityi2200fREEROOTDISKVMMS_Type(OctetString):
    """Custom type severityi2200fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2200fREEROOTDISKVMMS_Object = MibScalar
severityi2200fREEROOTDISKVMMS = _Severityi2200fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2200, 1),
    _Severityi2200fREEROOTDISKVMMS_Type()
)
severityi2200fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200fREEROOTDISKVMMS.setStatus("mandatory")


class _Messagei2200fREEROOTDISKVMMS_Type(OctetString):
    """Custom type messagei2200fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2200fREEROOTDISKVMMS_Object = MibScalar
messagei2200fREEROOTDISKVMMS = _Messagei2200fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2200, 2),
    _Messagei2200fREEROOTDISKVMMS_Type()
)
messagei2200fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200fREEROOTDISKVMMS.setStatus("mandatory")


class _Valuei2200fREEROOTDISKVMMS_Type(Integer32):
    """Custom type valuei2200fREEROOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200fREEROOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2200fREEROOTDISKVMMS_Object = MibScalar
valuei2200fREEROOTDISKVMMS = _Valuei2200fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2200, 3),
    _Valuei2200fREEROOTDISKVMMS_Type()
)
valuei2200fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200fREEROOTDISKVMMS.setStatus("mandatory")
_I2300fREEROOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2300fREEROOTDISKVMMS = _I2300fREEROOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2300)
)


class _Severityi2300fREEROOTDISKVMMS_Type(OctetString):
    """Custom type severityi2300fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2300fREEROOTDISKVMMS_Object = MibScalar
severityi2300fREEROOTDISKVMMS = _Severityi2300fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2300, 1),
    _Severityi2300fREEROOTDISKVMMS_Type()
)
severityi2300fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300fREEROOTDISKVMMS.setStatus("mandatory")


class _Messagei2300fREEROOTDISKVMMS_Type(OctetString):
    """Custom type messagei2300fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2300fREEROOTDISKVMMS_Object = MibScalar
messagei2300fREEROOTDISKVMMS = _Messagei2300fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2300, 2),
    _Messagei2300fREEROOTDISKVMMS_Type()
)
messagei2300fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300fREEROOTDISKVMMS.setStatus("mandatory")


class _Valuei2300fREEROOTDISKVMMS_Type(Integer32):
    """Custom type valuei2300fREEROOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300fREEROOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2300fREEROOTDISKVMMS_Object = MibScalar
valuei2300fREEROOTDISKVMMS = _Valuei2300fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2300, 3),
    _Valuei2300fREEROOTDISKVMMS_Type()
)
valuei2300fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300fREEROOTDISKVMMS.setStatus("mandatory")
_I2400fREEROOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2400fREEROOTDISKVMMS = _I2400fREEROOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2400)
)


class _Severityi2400fREEROOTDISKVMMS_Type(OctetString):
    """Custom type severityi2400fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2400fREEROOTDISKVMMS_Object = MibScalar
severityi2400fREEROOTDISKVMMS = _Severityi2400fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2400, 1),
    _Severityi2400fREEROOTDISKVMMS_Type()
)
severityi2400fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400fREEROOTDISKVMMS.setStatus("mandatory")


class _Messagei2400fREEROOTDISKVMMS_Type(OctetString):
    """Custom type messagei2400fREEROOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400fREEROOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2400fREEROOTDISKVMMS_Object = MibScalar
messagei2400fREEROOTDISKVMMS = _Messagei2400fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2400, 2),
    _Messagei2400fREEROOTDISKVMMS_Type()
)
messagei2400fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400fREEROOTDISKVMMS.setStatus("mandatory")


class _Valuei2400fREEROOTDISKVMMS_Type(Integer32):
    """Custom type valuei2400fREEROOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400fREEROOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2400fREEROOTDISKVMMS_Object = MibScalar
valuei2400fREEROOTDISKVMMS = _Valuei2400fREEROOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2400, 3),
    _Valuei2400fREEROOTDISKVMMS_Type()
)
valuei2400fREEROOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400fREEROOTDISKVMMS.setStatus("mandatory")
_FREEBOOTDISKVMMS_ObjectIdentity = ObjectIdentity
fREEBOOTDISKVMMS = _FREEBOOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2)
)
_I2100fREEBOOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2100fREEBOOTDISKVMMS = _I2100fREEBOOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2100)
)


class _Severityi2100fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type severityi2100fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2100fREEBOOTDISKVMMS_Object = MibScalar
severityi2100fREEBOOTDISKVMMS = _Severityi2100fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2100, 1),
    _Severityi2100fREEBOOTDISKVMMS_Type()
)
severityi2100fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100fREEBOOTDISKVMMS.setStatus("mandatory")


class _Messagei2100fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type messagei2100fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2100fREEBOOTDISKVMMS_Object = MibScalar
messagei2100fREEBOOTDISKVMMS = _Messagei2100fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2100, 2),
    _Messagei2100fREEBOOTDISKVMMS_Type()
)
messagei2100fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100fREEBOOTDISKVMMS.setStatus("mandatory")


class _Valuei2100fREEBOOTDISKVMMS_Type(Integer32):
    """Custom type valuei2100fREEBOOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100fREEBOOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2100fREEBOOTDISKVMMS_Object = MibScalar
valuei2100fREEBOOTDISKVMMS = _Valuei2100fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2100, 3),
    _Valuei2100fREEBOOTDISKVMMS_Type()
)
valuei2100fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100fREEBOOTDISKVMMS.setStatus("mandatory")
_I2200fREEBOOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2200fREEBOOTDISKVMMS = _I2200fREEBOOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2200)
)


class _Severityi2200fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type severityi2200fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2200fREEBOOTDISKVMMS_Object = MibScalar
severityi2200fREEBOOTDISKVMMS = _Severityi2200fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2200, 1),
    _Severityi2200fREEBOOTDISKVMMS_Type()
)
severityi2200fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200fREEBOOTDISKVMMS.setStatus("mandatory")


class _Messagei2200fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type messagei2200fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2200fREEBOOTDISKVMMS_Object = MibScalar
messagei2200fREEBOOTDISKVMMS = _Messagei2200fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2200, 2),
    _Messagei2200fREEBOOTDISKVMMS_Type()
)
messagei2200fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200fREEBOOTDISKVMMS.setStatus("mandatory")


class _Valuei2200fREEBOOTDISKVMMS_Type(Integer32):
    """Custom type valuei2200fREEBOOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200fREEBOOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2200fREEBOOTDISKVMMS_Object = MibScalar
valuei2200fREEBOOTDISKVMMS = _Valuei2200fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2200, 3),
    _Valuei2200fREEBOOTDISKVMMS_Type()
)
valuei2200fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200fREEBOOTDISKVMMS.setStatus("mandatory")
_I2300fREEBOOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2300fREEBOOTDISKVMMS = _I2300fREEBOOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2300)
)


class _Severityi2300fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type severityi2300fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2300fREEBOOTDISKVMMS_Object = MibScalar
severityi2300fREEBOOTDISKVMMS = _Severityi2300fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2300, 1),
    _Severityi2300fREEBOOTDISKVMMS_Type()
)
severityi2300fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300fREEBOOTDISKVMMS.setStatus("mandatory")


class _Messagei2300fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type messagei2300fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2300fREEBOOTDISKVMMS_Object = MibScalar
messagei2300fREEBOOTDISKVMMS = _Messagei2300fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2300, 2),
    _Messagei2300fREEBOOTDISKVMMS_Type()
)
messagei2300fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300fREEBOOTDISKVMMS.setStatus("mandatory")


class _Valuei2300fREEBOOTDISKVMMS_Type(Integer32):
    """Custom type valuei2300fREEBOOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300fREEBOOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2300fREEBOOTDISKVMMS_Object = MibScalar
valuei2300fREEBOOTDISKVMMS = _Valuei2300fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2300, 3),
    _Valuei2300fREEBOOTDISKVMMS_Type()
)
valuei2300fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300fREEBOOTDISKVMMS.setStatus("mandatory")
_I2400fREEBOOTDISKVMMS_ObjectIdentity = ObjectIdentity
i2400fREEBOOTDISKVMMS = _I2400fREEBOOTDISKVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2400)
)


class _Severityi2400fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type severityi2400fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Severityi2400fREEBOOTDISKVMMS_Object = MibScalar
severityi2400fREEBOOTDISKVMMS = _Severityi2400fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2400, 1),
    _Severityi2400fREEBOOTDISKVMMS_Type()
)
severityi2400fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400fREEBOOTDISKVMMS.setStatus("mandatory")


class _Messagei2400fREEBOOTDISKVMMS_Type(OctetString):
    """Custom type messagei2400fREEBOOTDISKVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400fREEBOOTDISKVMMS_Type.__name__ = "OctetString"
_Messagei2400fREEBOOTDISKVMMS_Object = MibScalar
messagei2400fREEBOOTDISKVMMS = _Messagei2400fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2400, 2),
    _Messagei2400fREEBOOTDISKVMMS_Type()
)
messagei2400fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400fREEBOOTDISKVMMS.setStatus("mandatory")


class _Valuei2400fREEBOOTDISKVMMS_Type(Integer32):
    """Custom type valuei2400fREEBOOTDISKVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400fREEBOOTDISKVMMS_Type.__name__ = "Integer32"
_Valuei2400fREEBOOTDISKVMMS_Object = MibScalar
valuei2400fREEBOOTDISKVMMS = _Valuei2400fREEBOOTDISKVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2400, 3),
    _Valuei2400fREEBOOTDISKVMMS_Type()
)
valuei2400fREEBOOTDISKVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400fREEBOOTDISKVMMS.setStatus("mandatory")
_FREEMEMORYVMMS_ObjectIdentity = ObjectIdentity
fREEMEMORYVMMS = _FREEMEMORYVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3)
)
_I2100fREEMEMORYVMMS_ObjectIdentity = ObjectIdentity
i2100fREEMEMORYVMMS = _I2100fREEMEMORYVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2100)
)


class _Severityi2100fREEMEMORYVMMS_Type(OctetString):
    """Custom type severityi2100fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Severityi2100fREEMEMORYVMMS_Object = MibScalar
severityi2100fREEMEMORYVMMS = _Severityi2100fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2100, 1),
    _Severityi2100fREEMEMORYVMMS_Type()
)
severityi2100fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100fREEMEMORYVMMS.setStatus("mandatory")


class _Messagei2100fREEMEMORYVMMS_Type(OctetString):
    """Custom type messagei2100fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Messagei2100fREEMEMORYVMMS_Object = MibScalar
messagei2100fREEMEMORYVMMS = _Messagei2100fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2100, 2),
    _Messagei2100fREEMEMORYVMMS_Type()
)
messagei2100fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100fREEMEMORYVMMS.setStatus("mandatory")


class _Valuei2100fREEMEMORYVMMS_Type(Integer32):
    """Custom type valuei2100fREEMEMORYVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100fREEMEMORYVMMS_Type.__name__ = "Integer32"
_Valuei2100fREEMEMORYVMMS_Object = MibScalar
valuei2100fREEMEMORYVMMS = _Valuei2100fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2100, 3),
    _Valuei2100fREEMEMORYVMMS_Type()
)
valuei2100fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100fREEMEMORYVMMS.setStatus("mandatory")
_I2200fREEMEMORYVMMS_ObjectIdentity = ObjectIdentity
i2200fREEMEMORYVMMS = _I2200fREEMEMORYVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2200)
)


class _Severityi2200fREEMEMORYVMMS_Type(OctetString):
    """Custom type severityi2200fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Severityi2200fREEMEMORYVMMS_Object = MibScalar
severityi2200fREEMEMORYVMMS = _Severityi2200fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2200, 1),
    _Severityi2200fREEMEMORYVMMS_Type()
)
severityi2200fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200fREEMEMORYVMMS.setStatus("mandatory")


class _Messagei2200fREEMEMORYVMMS_Type(OctetString):
    """Custom type messagei2200fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Messagei2200fREEMEMORYVMMS_Object = MibScalar
messagei2200fREEMEMORYVMMS = _Messagei2200fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2200, 2),
    _Messagei2200fREEMEMORYVMMS_Type()
)
messagei2200fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200fREEMEMORYVMMS.setStatus("mandatory")


class _Valuei2200fREEMEMORYVMMS_Type(Integer32):
    """Custom type valuei2200fREEMEMORYVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200fREEMEMORYVMMS_Type.__name__ = "Integer32"
_Valuei2200fREEMEMORYVMMS_Object = MibScalar
valuei2200fREEMEMORYVMMS = _Valuei2200fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2200, 3),
    _Valuei2200fREEMEMORYVMMS_Type()
)
valuei2200fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200fREEMEMORYVMMS.setStatus("mandatory")
_I2300fREEMEMORYVMMS_ObjectIdentity = ObjectIdentity
i2300fREEMEMORYVMMS = _I2300fREEMEMORYVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2300)
)


class _Severityi2300fREEMEMORYVMMS_Type(OctetString):
    """Custom type severityi2300fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Severityi2300fREEMEMORYVMMS_Object = MibScalar
severityi2300fREEMEMORYVMMS = _Severityi2300fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2300, 1),
    _Severityi2300fREEMEMORYVMMS_Type()
)
severityi2300fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300fREEMEMORYVMMS.setStatus("mandatory")


class _Messagei2300fREEMEMORYVMMS_Type(OctetString):
    """Custom type messagei2300fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Messagei2300fREEMEMORYVMMS_Object = MibScalar
messagei2300fREEMEMORYVMMS = _Messagei2300fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2300, 2),
    _Messagei2300fREEMEMORYVMMS_Type()
)
messagei2300fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300fREEMEMORYVMMS.setStatus("mandatory")


class _Valuei2300fREEMEMORYVMMS_Type(Integer32):
    """Custom type valuei2300fREEMEMORYVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300fREEMEMORYVMMS_Type.__name__ = "Integer32"
_Valuei2300fREEMEMORYVMMS_Object = MibScalar
valuei2300fREEMEMORYVMMS = _Valuei2300fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2300, 3),
    _Valuei2300fREEMEMORYVMMS_Type()
)
valuei2300fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300fREEMEMORYVMMS.setStatus("mandatory")
_I2400fREEMEMORYVMMS_ObjectIdentity = ObjectIdentity
i2400fREEMEMORYVMMS = _I2400fREEMEMORYVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2400)
)


class _Severityi2400fREEMEMORYVMMS_Type(OctetString):
    """Custom type severityi2400fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Severityi2400fREEMEMORYVMMS_Object = MibScalar
severityi2400fREEMEMORYVMMS = _Severityi2400fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2400, 1),
    _Severityi2400fREEMEMORYVMMS_Type()
)
severityi2400fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400fREEMEMORYVMMS.setStatus("mandatory")


class _Messagei2400fREEMEMORYVMMS_Type(OctetString):
    """Custom type messagei2400fREEMEMORYVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400fREEMEMORYVMMS_Type.__name__ = "OctetString"
_Messagei2400fREEMEMORYVMMS_Object = MibScalar
messagei2400fREEMEMORYVMMS = _Messagei2400fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2400, 2),
    _Messagei2400fREEMEMORYVMMS_Type()
)
messagei2400fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400fREEMEMORYVMMS.setStatus("mandatory")


class _Valuei2400fREEMEMORYVMMS_Type(Integer32):
    """Custom type valuei2400fREEMEMORYVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400fREEMEMORYVMMS_Type.__name__ = "Integer32"
_Valuei2400fREEMEMORYVMMS_Object = MibScalar
valuei2400fREEMEMORYVMMS = _Valuei2400fREEMEMORYVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2400, 3),
    _Valuei2400fREEMEMORYVMMS_Type()
)
valuei2400fREEMEMORYVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400fREEMEMORYVMMS.setStatus("mandatory")
_CPULOADVMMS_ObjectIdentity = ObjectIdentity
cPULOADVMMS = _CPULOADVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4)
)
_I2100cPULOADVMMS_ObjectIdentity = ObjectIdentity
i2100cPULOADVMMS = _I2100cPULOADVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2100)
)


class _Severityi2100cPULOADVMMS_Type(OctetString):
    """Custom type severityi2100cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100cPULOADVMMS_Type.__name__ = "OctetString"
_Severityi2100cPULOADVMMS_Object = MibScalar
severityi2100cPULOADVMMS = _Severityi2100cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2100, 1),
    _Severityi2100cPULOADVMMS_Type()
)
severityi2100cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100cPULOADVMMS.setStatus("mandatory")


class _Messagei2100cPULOADVMMS_Type(OctetString):
    """Custom type messagei2100cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100cPULOADVMMS_Type.__name__ = "OctetString"
_Messagei2100cPULOADVMMS_Object = MibScalar
messagei2100cPULOADVMMS = _Messagei2100cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2100, 2),
    _Messagei2100cPULOADVMMS_Type()
)
messagei2100cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100cPULOADVMMS.setStatus("mandatory")


class _Valuei2100cPULOADVMMS_Type(Integer32):
    """Custom type valuei2100cPULOADVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100cPULOADVMMS_Type.__name__ = "Integer32"
_Valuei2100cPULOADVMMS_Object = MibScalar
valuei2100cPULOADVMMS = _Valuei2100cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2100, 3),
    _Valuei2100cPULOADVMMS_Type()
)
valuei2100cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100cPULOADVMMS.setStatus("mandatory")
_I2200cPULOADVMMS_ObjectIdentity = ObjectIdentity
i2200cPULOADVMMS = _I2200cPULOADVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2200)
)


class _Severityi2200cPULOADVMMS_Type(OctetString):
    """Custom type severityi2200cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200cPULOADVMMS_Type.__name__ = "OctetString"
_Severityi2200cPULOADVMMS_Object = MibScalar
severityi2200cPULOADVMMS = _Severityi2200cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2200, 1),
    _Severityi2200cPULOADVMMS_Type()
)
severityi2200cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200cPULOADVMMS.setStatus("mandatory")


class _Messagei2200cPULOADVMMS_Type(OctetString):
    """Custom type messagei2200cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200cPULOADVMMS_Type.__name__ = "OctetString"
_Messagei2200cPULOADVMMS_Object = MibScalar
messagei2200cPULOADVMMS = _Messagei2200cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2200, 2),
    _Messagei2200cPULOADVMMS_Type()
)
messagei2200cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200cPULOADVMMS.setStatus("mandatory")


class _Valuei2200cPULOADVMMS_Type(Integer32):
    """Custom type valuei2200cPULOADVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200cPULOADVMMS_Type.__name__ = "Integer32"
_Valuei2200cPULOADVMMS_Object = MibScalar
valuei2200cPULOADVMMS = _Valuei2200cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2200, 3),
    _Valuei2200cPULOADVMMS_Type()
)
valuei2200cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200cPULOADVMMS.setStatus("mandatory")
_I2300cPULOADVMMS_ObjectIdentity = ObjectIdentity
i2300cPULOADVMMS = _I2300cPULOADVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2300)
)


class _Severityi2300cPULOADVMMS_Type(OctetString):
    """Custom type severityi2300cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300cPULOADVMMS_Type.__name__ = "OctetString"
_Severityi2300cPULOADVMMS_Object = MibScalar
severityi2300cPULOADVMMS = _Severityi2300cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2300, 1),
    _Severityi2300cPULOADVMMS_Type()
)
severityi2300cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300cPULOADVMMS.setStatus("mandatory")


class _Messagei2300cPULOADVMMS_Type(OctetString):
    """Custom type messagei2300cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300cPULOADVMMS_Type.__name__ = "OctetString"
_Messagei2300cPULOADVMMS_Object = MibScalar
messagei2300cPULOADVMMS = _Messagei2300cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2300, 2),
    _Messagei2300cPULOADVMMS_Type()
)
messagei2300cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300cPULOADVMMS.setStatus("mandatory")


class _Valuei2300cPULOADVMMS_Type(Integer32):
    """Custom type valuei2300cPULOADVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300cPULOADVMMS_Type.__name__ = "Integer32"
_Valuei2300cPULOADVMMS_Object = MibScalar
valuei2300cPULOADVMMS = _Valuei2300cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2300, 3),
    _Valuei2300cPULOADVMMS_Type()
)
valuei2300cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300cPULOADVMMS.setStatus("mandatory")
_I2400cPULOADVMMS_ObjectIdentity = ObjectIdentity
i2400cPULOADVMMS = _I2400cPULOADVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2400)
)


class _Severityi2400cPULOADVMMS_Type(OctetString):
    """Custom type severityi2400cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400cPULOADVMMS_Type.__name__ = "OctetString"
_Severityi2400cPULOADVMMS_Object = MibScalar
severityi2400cPULOADVMMS = _Severityi2400cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2400, 1),
    _Severityi2400cPULOADVMMS_Type()
)
severityi2400cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400cPULOADVMMS.setStatus("mandatory")


class _Messagei2400cPULOADVMMS_Type(OctetString):
    """Custom type messagei2400cPULOADVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400cPULOADVMMS_Type.__name__ = "OctetString"
_Messagei2400cPULOADVMMS_Object = MibScalar
messagei2400cPULOADVMMS = _Messagei2400cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2400, 2),
    _Messagei2400cPULOADVMMS_Type()
)
messagei2400cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400cPULOADVMMS.setStatus("mandatory")


class _Valuei2400cPULOADVMMS_Type(Integer32):
    """Custom type valuei2400cPULOADVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400cPULOADVMMS_Type.__name__ = "Integer32"
_Valuei2400cPULOADVMMS_Object = MibScalar
valuei2400cPULOADVMMS = _Valuei2400cPULOADVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2400, 3),
    _Valuei2400cPULOADVMMS_Type()
)
valuei2400cPULOADVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400cPULOADVMMS.setStatus("mandatory")
_FREESWAPVMMS_ObjectIdentity = ObjectIdentity
fREESWAPVMMS = _FREESWAPVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5)
)
_I2100fREESWAPVMMS_ObjectIdentity = ObjectIdentity
i2100fREESWAPVMMS = _I2100fREESWAPVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2100)
)


class _Severityi2100fREESWAPVMMS_Type(OctetString):
    """Custom type severityi2100fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100fREESWAPVMMS_Type.__name__ = "OctetString"
_Severityi2100fREESWAPVMMS_Object = MibScalar
severityi2100fREESWAPVMMS = _Severityi2100fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2100, 1),
    _Severityi2100fREESWAPVMMS_Type()
)
severityi2100fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100fREESWAPVMMS.setStatus("mandatory")


class _Messagei2100fREESWAPVMMS_Type(OctetString):
    """Custom type messagei2100fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100fREESWAPVMMS_Type.__name__ = "OctetString"
_Messagei2100fREESWAPVMMS_Object = MibScalar
messagei2100fREESWAPVMMS = _Messagei2100fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2100, 2),
    _Messagei2100fREESWAPVMMS_Type()
)
messagei2100fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100fREESWAPVMMS.setStatus("mandatory")


class _Valuei2100fREESWAPVMMS_Type(Integer32):
    """Custom type valuei2100fREESWAPVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100fREESWAPVMMS_Type.__name__ = "Integer32"
_Valuei2100fREESWAPVMMS_Object = MibScalar
valuei2100fREESWAPVMMS = _Valuei2100fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2100, 3),
    _Valuei2100fREESWAPVMMS_Type()
)
valuei2100fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100fREESWAPVMMS.setStatus("mandatory")
_I2200fREESWAPVMMS_ObjectIdentity = ObjectIdentity
i2200fREESWAPVMMS = _I2200fREESWAPVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2200)
)


class _Severityi2200fREESWAPVMMS_Type(OctetString):
    """Custom type severityi2200fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200fREESWAPVMMS_Type.__name__ = "OctetString"
_Severityi2200fREESWAPVMMS_Object = MibScalar
severityi2200fREESWAPVMMS = _Severityi2200fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2200, 1),
    _Severityi2200fREESWAPVMMS_Type()
)
severityi2200fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200fREESWAPVMMS.setStatus("mandatory")


class _Messagei2200fREESWAPVMMS_Type(OctetString):
    """Custom type messagei2200fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200fREESWAPVMMS_Type.__name__ = "OctetString"
_Messagei2200fREESWAPVMMS_Object = MibScalar
messagei2200fREESWAPVMMS = _Messagei2200fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2200, 2),
    _Messagei2200fREESWAPVMMS_Type()
)
messagei2200fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200fREESWAPVMMS.setStatus("mandatory")


class _Valuei2200fREESWAPVMMS_Type(Integer32):
    """Custom type valuei2200fREESWAPVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200fREESWAPVMMS_Type.__name__ = "Integer32"
_Valuei2200fREESWAPVMMS_Object = MibScalar
valuei2200fREESWAPVMMS = _Valuei2200fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2200, 3),
    _Valuei2200fREESWAPVMMS_Type()
)
valuei2200fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200fREESWAPVMMS.setStatus("mandatory")
_I2300fREESWAPVMMS_ObjectIdentity = ObjectIdentity
i2300fREESWAPVMMS = _I2300fREESWAPVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2300)
)


class _Severityi2300fREESWAPVMMS_Type(OctetString):
    """Custom type severityi2300fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300fREESWAPVMMS_Type.__name__ = "OctetString"
_Severityi2300fREESWAPVMMS_Object = MibScalar
severityi2300fREESWAPVMMS = _Severityi2300fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2300, 1),
    _Severityi2300fREESWAPVMMS_Type()
)
severityi2300fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300fREESWAPVMMS.setStatus("mandatory")


class _Messagei2300fREESWAPVMMS_Type(OctetString):
    """Custom type messagei2300fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300fREESWAPVMMS_Type.__name__ = "OctetString"
_Messagei2300fREESWAPVMMS_Object = MibScalar
messagei2300fREESWAPVMMS = _Messagei2300fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2300, 2),
    _Messagei2300fREESWAPVMMS_Type()
)
messagei2300fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300fREESWAPVMMS.setStatus("mandatory")


class _Valuei2300fREESWAPVMMS_Type(Integer32):
    """Custom type valuei2300fREESWAPVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300fREESWAPVMMS_Type.__name__ = "Integer32"
_Valuei2300fREESWAPVMMS_Object = MibScalar
valuei2300fREESWAPVMMS = _Valuei2300fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2300, 3),
    _Valuei2300fREESWAPVMMS_Type()
)
valuei2300fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300fREESWAPVMMS.setStatus("mandatory")
_I2400fREESWAPVMMS_ObjectIdentity = ObjectIdentity
i2400fREESWAPVMMS = _I2400fREESWAPVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2400)
)


class _Severityi2400fREESWAPVMMS_Type(OctetString):
    """Custom type severityi2400fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400fREESWAPVMMS_Type.__name__ = "OctetString"
_Severityi2400fREESWAPVMMS_Object = MibScalar
severityi2400fREESWAPVMMS = _Severityi2400fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2400, 1),
    _Severityi2400fREESWAPVMMS_Type()
)
severityi2400fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400fREESWAPVMMS.setStatus("mandatory")


class _Messagei2400fREESWAPVMMS_Type(OctetString):
    """Custom type messagei2400fREESWAPVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400fREESWAPVMMS_Type.__name__ = "OctetString"
_Messagei2400fREESWAPVMMS_Object = MibScalar
messagei2400fREESWAPVMMS = _Messagei2400fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2400, 2),
    _Messagei2400fREESWAPVMMS_Type()
)
messagei2400fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400fREESWAPVMMS.setStatus("mandatory")


class _Valuei2400fREESWAPVMMS_Type(Integer32):
    """Custom type valuei2400fREESWAPVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400fREESWAPVMMS_Type.__name__ = "Integer32"
_Valuei2400fREESWAPVMMS_Object = MibScalar
valuei2400fREESWAPVMMS = _Valuei2400fREESWAPVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2400, 3),
    _Valuei2400fREESWAPVMMS_Type()
)
valuei2400fREESWAPVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400fREESWAPVMMS.setStatus("mandatory")
_ETHINTSTATUSVMMS_ObjectIdentity = ObjectIdentity
eTHINTSTATUSVMMS = _ETHINTSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6)
)
_I2100eTHINTSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2100eTHINTSTATUSVMMS = _I2100eTHINTSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2100)
)


class _Severityi2100eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type severityi2100eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100eTHINTSTATUSVMMS_Object = MibScalar
severityi2100eTHINTSTATUSVMMS = _Severityi2100eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2100, 1),
    _Severityi2100eTHINTSTATUSVMMS_Type()
)
severityi2100eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100eTHINTSTATUSVMMS.setStatus("mandatory")


class _Messagei2100eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type messagei2100eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100eTHINTSTATUSVMMS_Object = MibScalar
messagei2100eTHINTSTATUSVMMS = _Messagei2100eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2100, 2),
    _Messagei2100eTHINTSTATUSVMMS_Type()
)
messagei2100eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100eTHINTSTATUSVMMS.setStatus("mandatory")


class _Valuei2100eTHINTSTATUSVMMS_Type(Integer32):
    """Custom type valuei2100eTHINTSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100eTHINTSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100eTHINTSTATUSVMMS_Object = MibScalar
valuei2100eTHINTSTATUSVMMS = _Valuei2100eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2100, 3),
    _Valuei2100eTHINTSTATUSVMMS_Type()
)
valuei2100eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100eTHINTSTATUSVMMS.setStatus("mandatory")
_I2200eTHINTSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2200eTHINTSTATUSVMMS = _I2200eTHINTSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2200)
)


class _Severityi2200eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type severityi2200eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200eTHINTSTATUSVMMS_Object = MibScalar
severityi2200eTHINTSTATUSVMMS = _Severityi2200eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2200, 1),
    _Severityi2200eTHINTSTATUSVMMS_Type()
)
severityi2200eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200eTHINTSTATUSVMMS.setStatus("mandatory")


class _Messagei2200eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type messagei2200eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200eTHINTSTATUSVMMS_Object = MibScalar
messagei2200eTHINTSTATUSVMMS = _Messagei2200eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2200, 2),
    _Messagei2200eTHINTSTATUSVMMS_Type()
)
messagei2200eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200eTHINTSTATUSVMMS.setStatus("mandatory")


class _Valuei2200eTHINTSTATUSVMMS_Type(Integer32):
    """Custom type valuei2200eTHINTSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200eTHINTSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200eTHINTSTATUSVMMS_Object = MibScalar
valuei2200eTHINTSTATUSVMMS = _Valuei2200eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2200, 3),
    _Valuei2200eTHINTSTATUSVMMS_Type()
)
valuei2200eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200eTHINTSTATUSVMMS.setStatus("mandatory")
_I2300eTHINTSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2300eTHINTSTATUSVMMS = _I2300eTHINTSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2300)
)


class _Severityi2300eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type severityi2300eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300eTHINTSTATUSVMMS_Object = MibScalar
severityi2300eTHINTSTATUSVMMS = _Severityi2300eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2300, 1),
    _Severityi2300eTHINTSTATUSVMMS_Type()
)
severityi2300eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300eTHINTSTATUSVMMS.setStatus("mandatory")


class _Messagei2300eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type messagei2300eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300eTHINTSTATUSVMMS_Object = MibScalar
messagei2300eTHINTSTATUSVMMS = _Messagei2300eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2300, 2),
    _Messagei2300eTHINTSTATUSVMMS_Type()
)
messagei2300eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300eTHINTSTATUSVMMS.setStatus("mandatory")


class _Valuei2300eTHINTSTATUSVMMS_Type(Integer32):
    """Custom type valuei2300eTHINTSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300eTHINTSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300eTHINTSTATUSVMMS_Object = MibScalar
valuei2300eTHINTSTATUSVMMS = _Valuei2300eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2300, 3),
    _Valuei2300eTHINTSTATUSVMMS_Type()
)
valuei2300eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300eTHINTSTATUSVMMS.setStatus("mandatory")
_I2400eTHINTSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2400eTHINTSTATUSVMMS = _I2400eTHINTSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2400)
)


class _Severityi2400eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type severityi2400eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400eTHINTSTATUSVMMS_Object = MibScalar
severityi2400eTHINTSTATUSVMMS = _Severityi2400eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2400, 1),
    _Severityi2400eTHINTSTATUSVMMS_Type()
)
severityi2400eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400eTHINTSTATUSVMMS.setStatus("mandatory")


class _Messagei2400eTHINTSTATUSVMMS_Type(OctetString):
    """Custom type messagei2400eTHINTSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400eTHINTSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400eTHINTSTATUSVMMS_Object = MibScalar
messagei2400eTHINTSTATUSVMMS = _Messagei2400eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2400, 2),
    _Messagei2400eTHINTSTATUSVMMS_Type()
)
messagei2400eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400eTHINTSTATUSVMMS.setStatus("mandatory")


class _Valuei2400eTHINTSTATUSVMMS_Type(Integer32):
    """Custom type valuei2400eTHINTSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400eTHINTSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400eTHINTSTATUSVMMS_Object = MibScalar
valuei2400eTHINTSTATUSVMMS = _Valuei2400eTHINTSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2400, 3),
    _Valuei2400eTHINTSTATUSVMMS_Type()
)
valuei2400eTHINTSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400eTHINTSTATUSVMMS.setStatus("mandatory")
_CRONSTATUSVMMS_ObjectIdentity = ObjectIdentity
cRONSTATUSVMMS = _CRONSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7)
)
_I2100cRONSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2100cRONSTATUSVMMS = _I2100cRONSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2100)
)


class _Severityi2100cRONSTATUSVMMS_Type(OctetString):
    """Custom type severityi2100cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100cRONSTATUSVMMS_Object = MibScalar
severityi2100cRONSTATUSVMMS = _Severityi2100cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2100, 1),
    _Severityi2100cRONSTATUSVMMS_Type()
)
severityi2100cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100cRONSTATUSVMMS.setStatus("mandatory")


class _Messagei2100cRONSTATUSVMMS_Type(OctetString):
    """Custom type messagei2100cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100cRONSTATUSVMMS_Object = MibScalar
messagei2100cRONSTATUSVMMS = _Messagei2100cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2100, 2),
    _Messagei2100cRONSTATUSVMMS_Type()
)
messagei2100cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100cRONSTATUSVMMS.setStatus("mandatory")


class _Valuei2100cRONSTATUSVMMS_Type(Integer32):
    """Custom type valuei2100cRONSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100cRONSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100cRONSTATUSVMMS_Object = MibScalar
valuei2100cRONSTATUSVMMS = _Valuei2100cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2100, 3),
    _Valuei2100cRONSTATUSVMMS_Type()
)
valuei2100cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100cRONSTATUSVMMS.setStatus("mandatory")
_I2200cRONSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2200cRONSTATUSVMMS = _I2200cRONSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2200)
)


class _Severityi2200cRONSTATUSVMMS_Type(OctetString):
    """Custom type severityi2200cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200cRONSTATUSVMMS_Object = MibScalar
severityi2200cRONSTATUSVMMS = _Severityi2200cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2200, 1),
    _Severityi2200cRONSTATUSVMMS_Type()
)
severityi2200cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200cRONSTATUSVMMS.setStatus("mandatory")


class _Messagei2200cRONSTATUSVMMS_Type(OctetString):
    """Custom type messagei2200cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200cRONSTATUSVMMS_Object = MibScalar
messagei2200cRONSTATUSVMMS = _Messagei2200cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2200, 2),
    _Messagei2200cRONSTATUSVMMS_Type()
)
messagei2200cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200cRONSTATUSVMMS.setStatus("mandatory")


class _Valuei2200cRONSTATUSVMMS_Type(Integer32):
    """Custom type valuei2200cRONSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200cRONSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200cRONSTATUSVMMS_Object = MibScalar
valuei2200cRONSTATUSVMMS = _Valuei2200cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2200, 3),
    _Valuei2200cRONSTATUSVMMS_Type()
)
valuei2200cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200cRONSTATUSVMMS.setStatus("mandatory")
_I2300cRONSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2300cRONSTATUSVMMS = _I2300cRONSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2300)
)


class _Severityi2300cRONSTATUSVMMS_Type(OctetString):
    """Custom type severityi2300cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300cRONSTATUSVMMS_Object = MibScalar
severityi2300cRONSTATUSVMMS = _Severityi2300cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2300, 1),
    _Severityi2300cRONSTATUSVMMS_Type()
)
severityi2300cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300cRONSTATUSVMMS.setStatus("mandatory")


class _Messagei2300cRONSTATUSVMMS_Type(OctetString):
    """Custom type messagei2300cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300cRONSTATUSVMMS_Object = MibScalar
messagei2300cRONSTATUSVMMS = _Messagei2300cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2300, 2),
    _Messagei2300cRONSTATUSVMMS_Type()
)
messagei2300cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300cRONSTATUSVMMS.setStatus("mandatory")


class _Valuei2300cRONSTATUSVMMS_Type(Integer32):
    """Custom type valuei2300cRONSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300cRONSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300cRONSTATUSVMMS_Object = MibScalar
valuei2300cRONSTATUSVMMS = _Valuei2300cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2300, 3),
    _Valuei2300cRONSTATUSVMMS_Type()
)
valuei2300cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300cRONSTATUSVMMS.setStatus("mandatory")
_I2400cRONSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2400cRONSTATUSVMMS = _I2400cRONSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2400)
)


class _Severityi2400cRONSTATUSVMMS_Type(OctetString):
    """Custom type severityi2400cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400cRONSTATUSVMMS_Object = MibScalar
severityi2400cRONSTATUSVMMS = _Severityi2400cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2400, 1),
    _Severityi2400cRONSTATUSVMMS_Type()
)
severityi2400cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400cRONSTATUSVMMS.setStatus("mandatory")


class _Messagei2400cRONSTATUSVMMS_Type(OctetString):
    """Custom type messagei2400cRONSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400cRONSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400cRONSTATUSVMMS_Object = MibScalar
messagei2400cRONSTATUSVMMS = _Messagei2400cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2400, 2),
    _Messagei2400cRONSTATUSVMMS_Type()
)
messagei2400cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400cRONSTATUSVMMS.setStatus("mandatory")


class _Valuei2400cRONSTATUSVMMS_Type(Integer32):
    """Custom type valuei2400cRONSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400cRONSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400cRONSTATUSVMMS_Object = MibScalar
valuei2400cRONSTATUSVMMS = _Valuei2400cRONSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2400, 3),
    _Valuei2400cRONSTATUSVMMS_Type()
)
valuei2400cRONSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400cRONSTATUSVMMS.setStatus("mandatory")
_MONITSTATUSVMMS_ObjectIdentity = ObjectIdentity
mONITSTATUSVMMS = _MONITSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8)
)
_I2100mONITSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2100mONITSTATUSVMMS = _I2100mONITSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2100)
)


class _Severityi2100mONITSTATUSVMMS_Type(OctetString):
    """Custom type severityi2100mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100mONITSTATUSVMMS_Object = MibScalar
severityi2100mONITSTATUSVMMS = _Severityi2100mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2100, 1),
    _Severityi2100mONITSTATUSVMMS_Type()
)
severityi2100mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100mONITSTATUSVMMS.setStatus("mandatory")


class _Messagei2100mONITSTATUSVMMS_Type(OctetString):
    """Custom type messagei2100mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100mONITSTATUSVMMS_Object = MibScalar
messagei2100mONITSTATUSVMMS = _Messagei2100mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2100, 2),
    _Messagei2100mONITSTATUSVMMS_Type()
)
messagei2100mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100mONITSTATUSVMMS.setStatus("mandatory")


class _Valuei2100mONITSTATUSVMMS_Type(Integer32):
    """Custom type valuei2100mONITSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100mONITSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100mONITSTATUSVMMS_Object = MibScalar
valuei2100mONITSTATUSVMMS = _Valuei2100mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2100, 3),
    _Valuei2100mONITSTATUSVMMS_Type()
)
valuei2100mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100mONITSTATUSVMMS.setStatus("mandatory")
_I2200mONITSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2200mONITSTATUSVMMS = _I2200mONITSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2200)
)


class _Severityi2200mONITSTATUSVMMS_Type(OctetString):
    """Custom type severityi2200mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200mONITSTATUSVMMS_Object = MibScalar
severityi2200mONITSTATUSVMMS = _Severityi2200mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2200, 1),
    _Severityi2200mONITSTATUSVMMS_Type()
)
severityi2200mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200mONITSTATUSVMMS.setStatus("mandatory")


class _Messagei2200mONITSTATUSVMMS_Type(OctetString):
    """Custom type messagei2200mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200mONITSTATUSVMMS_Object = MibScalar
messagei2200mONITSTATUSVMMS = _Messagei2200mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2200, 2),
    _Messagei2200mONITSTATUSVMMS_Type()
)
messagei2200mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200mONITSTATUSVMMS.setStatus("mandatory")


class _Valuei2200mONITSTATUSVMMS_Type(Integer32):
    """Custom type valuei2200mONITSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200mONITSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200mONITSTATUSVMMS_Object = MibScalar
valuei2200mONITSTATUSVMMS = _Valuei2200mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2200, 3),
    _Valuei2200mONITSTATUSVMMS_Type()
)
valuei2200mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200mONITSTATUSVMMS.setStatus("mandatory")
_I2300mONITSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2300mONITSTATUSVMMS = _I2300mONITSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2300)
)


class _Severityi2300mONITSTATUSVMMS_Type(OctetString):
    """Custom type severityi2300mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300mONITSTATUSVMMS_Object = MibScalar
severityi2300mONITSTATUSVMMS = _Severityi2300mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2300, 1),
    _Severityi2300mONITSTATUSVMMS_Type()
)
severityi2300mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300mONITSTATUSVMMS.setStatus("mandatory")


class _Messagei2300mONITSTATUSVMMS_Type(OctetString):
    """Custom type messagei2300mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300mONITSTATUSVMMS_Object = MibScalar
messagei2300mONITSTATUSVMMS = _Messagei2300mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2300, 2),
    _Messagei2300mONITSTATUSVMMS_Type()
)
messagei2300mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300mONITSTATUSVMMS.setStatus("mandatory")


class _Valuei2300mONITSTATUSVMMS_Type(Integer32):
    """Custom type valuei2300mONITSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300mONITSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300mONITSTATUSVMMS_Object = MibScalar
valuei2300mONITSTATUSVMMS = _Valuei2300mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2300, 3),
    _Valuei2300mONITSTATUSVMMS_Type()
)
valuei2300mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300mONITSTATUSVMMS.setStatus("mandatory")
_I2400mONITSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2400mONITSTATUSVMMS = _I2400mONITSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2400)
)


class _Severityi2400mONITSTATUSVMMS_Type(OctetString):
    """Custom type severityi2400mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400mONITSTATUSVMMS_Object = MibScalar
severityi2400mONITSTATUSVMMS = _Severityi2400mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2400, 1),
    _Severityi2400mONITSTATUSVMMS_Type()
)
severityi2400mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400mONITSTATUSVMMS.setStatus("mandatory")


class _Messagei2400mONITSTATUSVMMS_Type(OctetString):
    """Custom type messagei2400mONITSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400mONITSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400mONITSTATUSVMMS_Object = MibScalar
messagei2400mONITSTATUSVMMS = _Messagei2400mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2400, 2),
    _Messagei2400mONITSTATUSVMMS_Type()
)
messagei2400mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400mONITSTATUSVMMS.setStatus("mandatory")


class _Valuei2400mONITSTATUSVMMS_Type(Integer32):
    """Custom type valuei2400mONITSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400mONITSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400mONITSTATUSVMMS_Object = MibScalar
valuei2400mONITSTATUSVMMS = _Valuei2400mONITSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2400, 3),
    _Valuei2400mONITSTATUSVMMS_Type()
)
valuei2400mONITSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400mONITSTATUSVMMS.setStatus("mandatory")
_DNSMASQSTATUSVMMS_ObjectIdentity = ObjectIdentity
dNSMASQSTATUSVMMS = _DNSMASQSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9)
)
_I2100dNSMASQSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2100dNSMASQSTATUSVMMS = _I2100dNSMASQSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2100)
)


class _Severityi2100dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type severityi2100dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100dNSMASQSTATUSVMMS_Object = MibScalar
severityi2100dNSMASQSTATUSVMMS = _Severityi2100dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2100, 1),
    _Severityi2100dNSMASQSTATUSVMMS_Type()
)
severityi2100dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Messagei2100dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type messagei2100dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100dNSMASQSTATUSVMMS_Object = MibScalar
messagei2100dNSMASQSTATUSVMMS = _Messagei2100dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2100, 2),
    _Messagei2100dNSMASQSTATUSVMMS_Type()
)
messagei2100dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Valuei2100dNSMASQSTATUSVMMS_Type(Integer32):
    """Custom type valuei2100dNSMASQSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100dNSMASQSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100dNSMASQSTATUSVMMS_Object = MibScalar
valuei2100dNSMASQSTATUSVMMS = _Valuei2100dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2100, 3),
    _Valuei2100dNSMASQSTATUSVMMS_Type()
)
valuei2100dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100dNSMASQSTATUSVMMS.setStatus("mandatory")
_I2200dNSMASQSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2200dNSMASQSTATUSVMMS = _I2200dNSMASQSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2200)
)


class _Severityi2200dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type severityi2200dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200dNSMASQSTATUSVMMS_Object = MibScalar
severityi2200dNSMASQSTATUSVMMS = _Severityi2200dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2200, 1),
    _Severityi2200dNSMASQSTATUSVMMS_Type()
)
severityi2200dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Messagei2200dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type messagei2200dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200dNSMASQSTATUSVMMS_Object = MibScalar
messagei2200dNSMASQSTATUSVMMS = _Messagei2200dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2200, 2),
    _Messagei2200dNSMASQSTATUSVMMS_Type()
)
messagei2200dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Valuei2200dNSMASQSTATUSVMMS_Type(Integer32):
    """Custom type valuei2200dNSMASQSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200dNSMASQSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200dNSMASQSTATUSVMMS_Object = MibScalar
valuei2200dNSMASQSTATUSVMMS = _Valuei2200dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2200, 3),
    _Valuei2200dNSMASQSTATUSVMMS_Type()
)
valuei2200dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200dNSMASQSTATUSVMMS.setStatus("mandatory")
_I2300dNSMASQSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2300dNSMASQSTATUSVMMS = _I2300dNSMASQSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2300)
)


class _Severityi2300dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type severityi2300dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300dNSMASQSTATUSVMMS_Object = MibScalar
severityi2300dNSMASQSTATUSVMMS = _Severityi2300dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2300, 1),
    _Severityi2300dNSMASQSTATUSVMMS_Type()
)
severityi2300dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Messagei2300dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type messagei2300dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300dNSMASQSTATUSVMMS_Object = MibScalar
messagei2300dNSMASQSTATUSVMMS = _Messagei2300dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2300, 2),
    _Messagei2300dNSMASQSTATUSVMMS_Type()
)
messagei2300dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Valuei2300dNSMASQSTATUSVMMS_Type(Integer32):
    """Custom type valuei2300dNSMASQSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300dNSMASQSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300dNSMASQSTATUSVMMS_Object = MibScalar
valuei2300dNSMASQSTATUSVMMS = _Valuei2300dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2300, 3),
    _Valuei2300dNSMASQSTATUSVMMS_Type()
)
valuei2300dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300dNSMASQSTATUSVMMS.setStatus("mandatory")
_I2400dNSMASQSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2400dNSMASQSTATUSVMMS = _I2400dNSMASQSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2400)
)


class _Severityi2400dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type severityi2400dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400dNSMASQSTATUSVMMS_Object = MibScalar
severityi2400dNSMASQSTATUSVMMS = _Severityi2400dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2400, 1),
    _Severityi2400dNSMASQSTATUSVMMS_Type()
)
severityi2400dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Messagei2400dNSMASQSTATUSVMMS_Type(OctetString):
    """Custom type messagei2400dNSMASQSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400dNSMASQSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400dNSMASQSTATUSVMMS_Object = MibScalar
messagei2400dNSMASQSTATUSVMMS = _Messagei2400dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2400, 2),
    _Messagei2400dNSMASQSTATUSVMMS_Type()
)
messagei2400dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400dNSMASQSTATUSVMMS.setStatus("mandatory")


class _Valuei2400dNSMASQSTATUSVMMS_Type(Integer32):
    """Custom type valuei2400dNSMASQSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400dNSMASQSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400dNSMASQSTATUSVMMS_Object = MibScalar
valuei2400dNSMASQSTATUSVMMS = _Valuei2400dNSMASQSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2400, 3),
    _Valuei2400dNSMASQSTATUSVMMS_Type()
)
valuei2400dNSMASQSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400dNSMASQSTATUSVMMS.setStatus("mandatory")
_HB2STATUSVMMS_ObjectIdentity = ObjectIdentity
hB2STATUSVMMS = _HB2STATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11)
)
_I2100hB2STATUSVMMS_ObjectIdentity = ObjectIdentity
i2100hB2STATUSVMMS = _I2100hB2STATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2100)
)


class _Severityi2100hB2STATUSVMMS_Type(OctetString):
    """Custom type severityi2100hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100hB2STATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100hB2STATUSVMMS_Object = MibScalar
severityi2100hB2STATUSVMMS = _Severityi2100hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2100, 1),
    _Severityi2100hB2STATUSVMMS_Type()
)
severityi2100hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100hB2STATUSVMMS.setStatus("mandatory")


class _Messagei2100hB2STATUSVMMS_Type(OctetString):
    """Custom type messagei2100hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100hB2STATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100hB2STATUSVMMS_Object = MibScalar
messagei2100hB2STATUSVMMS = _Messagei2100hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2100, 2),
    _Messagei2100hB2STATUSVMMS_Type()
)
messagei2100hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100hB2STATUSVMMS.setStatus("mandatory")


class _Valuei2100hB2STATUSVMMS_Type(Integer32):
    """Custom type valuei2100hB2STATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100hB2STATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100hB2STATUSVMMS_Object = MibScalar
valuei2100hB2STATUSVMMS = _Valuei2100hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2100, 3),
    _Valuei2100hB2STATUSVMMS_Type()
)
valuei2100hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100hB2STATUSVMMS.setStatus("mandatory")
_I2200hB2STATUSVMMS_ObjectIdentity = ObjectIdentity
i2200hB2STATUSVMMS = _I2200hB2STATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2200)
)


class _Severityi2200hB2STATUSVMMS_Type(OctetString):
    """Custom type severityi2200hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200hB2STATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200hB2STATUSVMMS_Object = MibScalar
severityi2200hB2STATUSVMMS = _Severityi2200hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2200, 1),
    _Severityi2200hB2STATUSVMMS_Type()
)
severityi2200hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200hB2STATUSVMMS.setStatus("mandatory")


class _Messagei2200hB2STATUSVMMS_Type(OctetString):
    """Custom type messagei2200hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200hB2STATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200hB2STATUSVMMS_Object = MibScalar
messagei2200hB2STATUSVMMS = _Messagei2200hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2200, 2),
    _Messagei2200hB2STATUSVMMS_Type()
)
messagei2200hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200hB2STATUSVMMS.setStatus("mandatory")


class _Valuei2200hB2STATUSVMMS_Type(Integer32):
    """Custom type valuei2200hB2STATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200hB2STATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200hB2STATUSVMMS_Object = MibScalar
valuei2200hB2STATUSVMMS = _Valuei2200hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2200, 3),
    _Valuei2200hB2STATUSVMMS_Type()
)
valuei2200hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200hB2STATUSVMMS.setStatus("mandatory")
_I2300hB2STATUSVMMS_ObjectIdentity = ObjectIdentity
i2300hB2STATUSVMMS = _I2300hB2STATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2300)
)


class _Severityi2300hB2STATUSVMMS_Type(OctetString):
    """Custom type severityi2300hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300hB2STATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300hB2STATUSVMMS_Object = MibScalar
severityi2300hB2STATUSVMMS = _Severityi2300hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2300, 1),
    _Severityi2300hB2STATUSVMMS_Type()
)
severityi2300hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300hB2STATUSVMMS.setStatus("mandatory")


class _Messagei2300hB2STATUSVMMS_Type(OctetString):
    """Custom type messagei2300hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300hB2STATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300hB2STATUSVMMS_Object = MibScalar
messagei2300hB2STATUSVMMS = _Messagei2300hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2300, 2),
    _Messagei2300hB2STATUSVMMS_Type()
)
messagei2300hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300hB2STATUSVMMS.setStatus("mandatory")


class _Valuei2300hB2STATUSVMMS_Type(Integer32):
    """Custom type valuei2300hB2STATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300hB2STATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300hB2STATUSVMMS_Object = MibScalar
valuei2300hB2STATUSVMMS = _Valuei2300hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2300, 3),
    _Valuei2300hB2STATUSVMMS_Type()
)
valuei2300hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300hB2STATUSVMMS.setStatus("mandatory")
_I2400hB2STATUSVMMS_ObjectIdentity = ObjectIdentity
i2400hB2STATUSVMMS = _I2400hB2STATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2400)
)


class _Severityi2400hB2STATUSVMMS_Type(OctetString):
    """Custom type severityi2400hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400hB2STATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400hB2STATUSVMMS_Object = MibScalar
severityi2400hB2STATUSVMMS = _Severityi2400hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2400, 1),
    _Severityi2400hB2STATUSVMMS_Type()
)
severityi2400hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400hB2STATUSVMMS.setStatus("mandatory")


class _Messagei2400hB2STATUSVMMS_Type(OctetString):
    """Custom type messagei2400hB2STATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400hB2STATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400hB2STATUSVMMS_Object = MibScalar
messagei2400hB2STATUSVMMS = _Messagei2400hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2400, 2),
    _Messagei2400hB2STATUSVMMS_Type()
)
messagei2400hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400hB2STATUSVMMS.setStatus("mandatory")


class _Valuei2400hB2STATUSVMMS_Type(Integer32):
    """Custom type valuei2400hB2STATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400hB2STATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400hB2STATUSVMMS_Object = MibScalar
valuei2400hB2STATUSVMMS = _Valuei2400hB2STATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2400, 3),
    _Valuei2400hB2STATUSVMMS_Type()
)
valuei2400hB2STATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400hB2STATUSVMMS.setStatus("mandatory")
_HB2MWDIASTATUSVMMS_ObjectIdentity = ObjectIdentity
hB2MWDIASTATUSVMMS = _HB2MWDIASTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12)
)
_I2100hB2MWDIASTATUSVMMS_ObjectIdentity = ObjectIdentity
i2100hB2MWDIASTATUSVMMS = _I2100hB2MWDIASTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2100)
)


class _Severityi2100hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type severityi2100hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100hB2MWDIASTATUSVMMS_Object = MibScalar
severityi2100hB2MWDIASTATUSVMMS = _Severityi2100hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2100, 1),
    _Severityi2100hB2MWDIASTATUSVMMS_Type()
)
severityi2100hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Messagei2100hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type messagei2100hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100hB2MWDIASTATUSVMMS_Object = MibScalar
messagei2100hB2MWDIASTATUSVMMS = _Messagei2100hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2100, 2),
    _Messagei2100hB2MWDIASTATUSVMMS_Type()
)
messagei2100hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Valuei2100hB2MWDIASTATUSVMMS_Type(Integer32):
    """Custom type valuei2100hB2MWDIASTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100hB2MWDIASTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100hB2MWDIASTATUSVMMS_Object = MibScalar
valuei2100hB2MWDIASTATUSVMMS = _Valuei2100hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2100, 3),
    _Valuei2100hB2MWDIASTATUSVMMS_Type()
)
valuei2100hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100hB2MWDIASTATUSVMMS.setStatus("mandatory")
_I2200hB2MWDIASTATUSVMMS_ObjectIdentity = ObjectIdentity
i2200hB2MWDIASTATUSVMMS = _I2200hB2MWDIASTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2200)
)


class _Severityi2200hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type severityi2200hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200hB2MWDIASTATUSVMMS_Object = MibScalar
severityi2200hB2MWDIASTATUSVMMS = _Severityi2200hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2200, 1),
    _Severityi2200hB2MWDIASTATUSVMMS_Type()
)
severityi2200hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Messagei2200hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type messagei2200hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200hB2MWDIASTATUSVMMS_Object = MibScalar
messagei2200hB2MWDIASTATUSVMMS = _Messagei2200hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2200, 2),
    _Messagei2200hB2MWDIASTATUSVMMS_Type()
)
messagei2200hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Valuei2200hB2MWDIASTATUSVMMS_Type(Integer32):
    """Custom type valuei2200hB2MWDIASTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200hB2MWDIASTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200hB2MWDIASTATUSVMMS_Object = MibScalar
valuei2200hB2MWDIASTATUSVMMS = _Valuei2200hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2200, 3),
    _Valuei2200hB2MWDIASTATUSVMMS_Type()
)
valuei2200hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200hB2MWDIASTATUSVMMS.setStatus("mandatory")
_I2300hB2MWDIASTATUSVMMS_ObjectIdentity = ObjectIdentity
i2300hB2MWDIASTATUSVMMS = _I2300hB2MWDIASTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2300)
)


class _Severityi2300hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type severityi2300hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300hB2MWDIASTATUSVMMS_Object = MibScalar
severityi2300hB2MWDIASTATUSVMMS = _Severityi2300hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2300, 1),
    _Severityi2300hB2MWDIASTATUSVMMS_Type()
)
severityi2300hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Messagei2300hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type messagei2300hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300hB2MWDIASTATUSVMMS_Object = MibScalar
messagei2300hB2MWDIASTATUSVMMS = _Messagei2300hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2300, 2),
    _Messagei2300hB2MWDIASTATUSVMMS_Type()
)
messagei2300hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Valuei2300hB2MWDIASTATUSVMMS_Type(Integer32):
    """Custom type valuei2300hB2MWDIASTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300hB2MWDIASTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300hB2MWDIASTATUSVMMS_Object = MibScalar
valuei2300hB2MWDIASTATUSVMMS = _Valuei2300hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2300, 3),
    _Valuei2300hB2MWDIASTATUSVMMS_Type()
)
valuei2300hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300hB2MWDIASTATUSVMMS.setStatus("mandatory")
_I2400hB2MWDIASTATUSVMMS_ObjectIdentity = ObjectIdentity
i2400hB2MWDIASTATUSVMMS = _I2400hB2MWDIASTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2400)
)


class _Severityi2400hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type severityi2400hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400hB2MWDIASTATUSVMMS_Object = MibScalar
severityi2400hB2MWDIASTATUSVMMS = _Severityi2400hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2400, 1),
    _Severityi2400hB2MWDIASTATUSVMMS_Type()
)
severityi2400hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Messagei2400hB2MWDIASTATUSVMMS_Type(OctetString):
    """Custom type messagei2400hB2MWDIASTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400hB2MWDIASTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400hB2MWDIASTATUSVMMS_Object = MibScalar
messagei2400hB2MWDIASTATUSVMMS = _Messagei2400hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2400, 2),
    _Messagei2400hB2MWDIASTATUSVMMS_Type()
)
messagei2400hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400hB2MWDIASTATUSVMMS.setStatus("mandatory")


class _Valuei2400hB2MWDIASTATUSVMMS_Type(Integer32):
    """Custom type valuei2400hB2MWDIASTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400hB2MWDIASTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400hB2MWDIASTATUSVMMS_Object = MibScalar
valuei2400hB2MWDIASTATUSVMMS = _Valuei2400hB2MWDIASTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2400, 3),
    _Valuei2400hB2MWDIASTATUSVMMS_Type()
)
valuei2400hB2MWDIASTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400hB2MWDIASTATUSVMMS.setStatus("mandatory")
_CPUSTATUSVMMS_ObjectIdentity = ObjectIdentity
cPUSTATUSVMMS = _CPUSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18)
)
_I2100cPUSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2100cPUSTATUSVMMS = _I2100cPUSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2100)
)


class _Severityi2100cPUSTATUSVMMS_Type(OctetString):
    """Custom type severityi2100cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2100cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2100cPUSTATUSVMMS_Object = MibScalar
severityi2100cPUSTATUSVMMS = _Severityi2100cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2100, 1),
    _Severityi2100cPUSTATUSVMMS_Type()
)
severityi2100cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2100cPUSTATUSVMMS.setStatus("mandatory")


class _Messagei2100cPUSTATUSVMMS_Type(OctetString):
    """Custom type messagei2100cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2100cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2100cPUSTATUSVMMS_Object = MibScalar
messagei2100cPUSTATUSVMMS = _Messagei2100cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2100, 2),
    _Messagei2100cPUSTATUSVMMS_Type()
)
messagei2100cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2100cPUSTATUSVMMS.setStatus("mandatory")


class _Valuei2100cPUSTATUSVMMS_Type(Integer32):
    """Custom type valuei2100cPUSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2100cPUSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2100cPUSTATUSVMMS_Object = MibScalar
valuei2100cPUSTATUSVMMS = _Valuei2100cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2100, 3),
    _Valuei2100cPUSTATUSVMMS_Type()
)
valuei2100cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2100cPUSTATUSVMMS.setStatus("mandatory")
_I2200cPUSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2200cPUSTATUSVMMS = _I2200cPUSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2200)
)


class _Severityi2200cPUSTATUSVMMS_Type(OctetString):
    """Custom type severityi2200cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2200cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2200cPUSTATUSVMMS_Object = MibScalar
severityi2200cPUSTATUSVMMS = _Severityi2200cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2200, 1),
    _Severityi2200cPUSTATUSVMMS_Type()
)
severityi2200cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2200cPUSTATUSVMMS.setStatus("mandatory")


class _Messagei2200cPUSTATUSVMMS_Type(OctetString):
    """Custom type messagei2200cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2200cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2200cPUSTATUSVMMS_Object = MibScalar
messagei2200cPUSTATUSVMMS = _Messagei2200cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2200, 2),
    _Messagei2200cPUSTATUSVMMS_Type()
)
messagei2200cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2200cPUSTATUSVMMS.setStatus("mandatory")


class _Valuei2200cPUSTATUSVMMS_Type(Integer32):
    """Custom type valuei2200cPUSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2200cPUSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2200cPUSTATUSVMMS_Object = MibScalar
valuei2200cPUSTATUSVMMS = _Valuei2200cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2200, 3),
    _Valuei2200cPUSTATUSVMMS_Type()
)
valuei2200cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2200cPUSTATUSVMMS.setStatus("mandatory")
_I2300cPUSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2300cPUSTATUSVMMS = _I2300cPUSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2300)
)


class _Severityi2300cPUSTATUSVMMS_Type(OctetString):
    """Custom type severityi2300cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2300cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2300cPUSTATUSVMMS_Object = MibScalar
severityi2300cPUSTATUSVMMS = _Severityi2300cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2300, 1),
    _Severityi2300cPUSTATUSVMMS_Type()
)
severityi2300cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2300cPUSTATUSVMMS.setStatus("mandatory")


class _Messagei2300cPUSTATUSVMMS_Type(OctetString):
    """Custom type messagei2300cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2300cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2300cPUSTATUSVMMS_Object = MibScalar
messagei2300cPUSTATUSVMMS = _Messagei2300cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2300, 2),
    _Messagei2300cPUSTATUSVMMS_Type()
)
messagei2300cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2300cPUSTATUSVMMS.setStatus("mandatory")


class _Valuei2300cPUSTATUSVMMS_Type(Integer32):
    """Custom type valuei2300cPUSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2300cPUSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2300cPUSTATUSVMMS_Object = MibScalar
valuei2300cPUSTATUSVMMS = _Valuei2300cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2300, 3),
    _Valuei2300cPUSTATUSVMMS_Type()
)
valuei2300cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2300cPUSTATUSVMMS.setStatus("mandatory")
_I2400cPUSTATUSVMMS_ObjectIdentity = ObjectIdentity
i2400cPUSTATUSVMMS = _I2400cPUSTATUSVMMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2400)
)


class _Severityi2400cPUSTATUSVMMS_Type(OctetString):
    """Custom type severityi2400cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi2400cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Severityi2400cPUSTATUSVMMS_Object = MibScalar
severityi2400cPUSTATUSVMMS = _Severityi2400cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2400, 1),
    _Severityi2400cPUSTATUSVMMS_Type()
)
severityi2400cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi2400cPUSTATUSVMMS.setStatus("mandatory")


class _Messagei2400cPUSTATUSVMMS_Type(OctetString):
    """Custom type messagei2400cPUSTATUSVMMS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei2400cPUSTATUSVMMS_Type.__name__ = "OctetString"
_Messagei2400cPUSTATUSVMMS_Object = MibScalar
messagei2400cPUSTATUSVMMS = _Messagei2400cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2400, 2),
    _Messagei2400cPUSTATUSVMMS_Type()
)
messagei2400cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei2400cPUSTATUSVMMS.setStatus("mandatory")


class _Valuei2400cPUSTATUSVMMS_Type(Integer32):
    """Custom type valuei2400cPUSTATUSVMMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei2400cPUSTATUSVMMS_Type.__name__ = "Integer32"
_Valuei2400cPUSTATUSVMMS_Object = MibScalar
valuei2400cPUSTATUSVMMS = _Valuei2400cPUSTATUSVMMS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2400, 3),
    _Valuei2400cPUSTATUSVMMS_Type()
)
valuei2400cPUSTATUSVMMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei2400cPUSTATUSVMMS.setStatus("mandatory")
_Vmdb_ObjectIdentity = ObjectIdentity
vmdb = _Vmdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103)
)
_FREEROOTDISKVMDB_ObjectIdentity = ObjectIdentity
fREEROOTDISKVMDB = _FREEROOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1)
)
_I3100fREEROOTDISKVMDB_ObjectIdentity = ObjectIdentity
i3100fREEROOTDISKVMDB = _I3100fREEROOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3100)
)


class _Severityi3100fREEROOTDISKVMDB_Type(OctetString):
    """Custom type severityi3100fREEROOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100fREEROOTDISKVMDB_Type.__name__ = "OctetString"
_Severityi3100fREEROOTDISKVMDB_Object = MibScalar
severityi3100fREEROOTDISKVMDB = _Severityi3100fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3100, 1),
    _Severityi3100fREEROOTDISKVMDB_Type()
)
severityi3100fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100fREEROOTDISKVMDB.setStatus("mandatory")


class _Messagei3100fREEROOTDISKVMDB_Type(OctetString):
    """Custom type messagei3100fREEROOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100fREEROOTDISKVMDB_Type.__name__ = "OctetString"
_Messagei3100fREEROOTDISKVMDB_Object = MibScalar
messagei3100fREEROOTDISKVMDB = _Messagei3100fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3100, 2),
    _Messagei3100fREEROOTDISKVMDB_Type()
)
messagei3100fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100fREEROOTDISKVMDB.setStatus("mandatory")


class _Valuei3100fREEROOTDISKVMDB_Type(Integer32):
    """Custom type valuei3100fREEROOTDISKVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100fREEROOTDISKVMDB_Type.__name__ = "Integer32"
_Valuei3100fREEROOTDISKVMDB_Object = MibScalar
valuei3100fREEROOTDISKVMDB = _Valuei3100fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3100, 3),
    _Valuei3100fREEROOTDISKVMDB_Type()
)
valuei3100fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100fREEROOTDISKVMDB.setStatus("mandatory")
_I3200fREEROOTDISKVMDB_ObjectIdentity = ObjectIdentity
i3200fREEROOTDISKVMDB = _I3200fREEROOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3200)
)


class _Severityi3200fREEROOTDISKVMDB_Type(OctetString):
    """Custom type severityi3200fREEROOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200fREEROOTDISKVMDB_Type.__name__ = "OctetString"
_Severityi3200fREEROOTDISKVMDB_Object = MibScalar
severityi3200fREEROOTDISKVMDB = _Severityi3200fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3200, 1),
    _Severityi3200fREEROOTDISKVMDB_Type()
)
severityi3200fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200fREEROOTDISKVMDB.setStatus("mandatory")


class _Messagei3200fREEROOTDISKVMDB_Type(OctetString):
    """Custom type messagei3200fREEROOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200fREEROOTDISKVMDB_Type.__name__ = "OctetString"
_Messagei3200fREEROOTDISKVMDB_Object = MibScalar
messagei3200fREEROOTDISKVMDB = _Messagei3200fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3200, 2),
    _Messagei3200fREEROOTDISKVMDB_Type()
)
messagei3200fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200fREEROOTDISKVMDB.setStatus("mandatory")


class _Valuei3200fREEROOTDISKVMDB_Type(Integer32):
    """Custom type valuei3200fREEROOTDISKVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200fREEROOTDISKVMDB_Type.__name__ = "Integer32"
_Valuei3200fREEROOTDISKVMDB_Object = MibScalar
valuei3200fREEROOTDISKVMDB = _Valuei3200fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3200, 3),
    _Valuei3200fREEROOTDISKVMDB_Type()
)
valuei3200fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200fREEROOTDISKVMDB.setStatus("mandatory")
_I3300fREEROOTDISKVMDB_ObjectIdentity = ObjectIdentity
i3300fREEROOTDISKVMDB = _I3300fREEROOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3300)
)


class _Severityi3300fREEROOTDISKVMDB_Type(OctetString):
    """Custom type severityi3300fREEROOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300fREEROOTDISKVMDB_Type.__name__ = "OctetString"
_Severityi3300fREEROOTDISKVMDB_Object = MibScalar
severityi3300fREEROOTDISKVMDB = _Severityi3300fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3300, 1),
    _Severityi3300fREEROOTDISKVMDB_Type()
)
severityi3300fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300fREEROOTDISKVMDB.setStatus("mandatory")


class _Messagei3300fREEROOTDISKVMDB_Type(OctetString):
    """Custom type messagei3300fREEROOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300fREEROOTDISKVMDB_Type.__name__ = "OctetString"
_Messagei3300fREEROOTDISKVMDB_Object = MibScalar
messagei3300fREEROOTDISKVMDB = _Messagei3300fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3300, 2),
    _Messagei3300fREEROOTDISKVMDB_Type()
)
messagei3300fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300fREEROOTDISKVMDB.setStatus("mandatory")


class _Valuei3300fREEROOTDISKVMDB_Type(Integer32):
    """Custom type valuei3300fREEROOTDISKVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300fREEROOTDISKVMDB_Type.__name__ = "Integer32"
_Valuei3300fREEROOTDISKVMDB_Object = MibScalar
valuei3300fREEROOTDISKVMDB = _Valuei3300fREEROOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3300, 3),
    _Valuei3300fREEROOTDISKVMDB_Type()
)
valuei3300fREEROOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300fREEROOTDISKVMDB.setStatus("mandatory")
_FREEBOOTDISKVMDB_ObjectIdentity = ObjectIdentity
fREEBOOTDISKVMDB = _FREEBOOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2)
)
_I3100fREEBOOTDISKVMDB_ObjectIdentity = ObjectIdentity
i3100fREEBOOTDISKVMDB = _I3100fREEBOOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3100)
)


class _Severityi3100fREEBOOTDISKVMDB_Type(OctetString):
    """Custom type severityi3100fREEBOOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100fREEBOOTDISKVMDB_Type.__name__ = "OctetString"
_Severityi3100fREEBOOTDISKVMDB_Object = MibScalar
severityi3100fREEBOOTDISKVMDB = _Severityi3100fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3100, 1),
    _Severityi3100fREEBOOTDISKVMDB_Type()
)
severityi3100fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100fREEBOOTDISKVMDB.setStatus("mandatory")


class _Messagei3100fREEBOOTDISKVMDB_Type(OctetString):
    """Custom type messagei3100fREEBOOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100fREEBOOTDISKVMDB_Type.__name__ = "OctetString"
_Messagei3100fREEBOOTDISKVMDB_Object = MibScalar
messagei3100fREEBOOTDISKVMDB = _Messagei3100fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3100, 2),
    _Messagei3100fREEBOOTDISKVMDB_Type()
)
messagei3100fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100fREEBOOTDISKVMDB.setStatus("mandatory")


class _Valuei3100fREEBOOTDISKVMDB_Type(Integer32):
    """Custom type valuei3100fREEBOOTDISKVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100fREEBOOTDISKVMDB_Type.__name__ = "Integer32"
_Valuei3100fREEBOOTDISKVMDB_Object = MibScalar
valuei3100fREEBOOTDISKVMDB = _Valuei3100fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3100, 3),
    _Valuei3100fREEBOOTDISKVMDB_Type()
)
valuei3100fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100fREEBOOTDISKVMDB.setStatus("mandatory")
_I3200fREEBOOTDISKVMDB_ObjectIdentity = ObjectIdentity
i3200fREEBOOTDISKVMDB = _I3200fREEBOOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3200)
)


class _Severityi3200fREEBOOTDISKVMDB_Type(OctetString):
    """Custom type severityi3200fREEBOOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200fREEBOOTDISKVMDB_Type.__name__ = "OctetString"
_Severityi3200fREEBOOTDISKVMDB_Object = MibScalar
severityi3200fREEBOOTDISKVMDB = _Severityi3200fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3200, 1),
    _Severityi3200fREEBOOTDISKVMDB_Type()
)
severityi3200fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200fREEBOOTDISKVMDB.setStatus("mandatory")


class _Messagei3200fREEBOOTDISKVMDB_Type(OctetString):
    """Custom type messagei3200fREEBOOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200fREEBOOTDISKVMDB_Type.__name__ = "OctetString"
_Messagei3200fREEBOOTDISKVMDB_Object = MibScalar
messagei3200fREEBOOTDISKVMDB = _Messagei3200fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3200, 2),
    _Messagei3200fREEBOOTDISKVMDB_Type()
)
messagei3200fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200fREEBOOTDISKVMDB.setStatus("mandatory")


class _Valuei3200fREEBOOTDISKVMDB_Type(Integer32):
    """Custom type valuei3200fREEBOOTDISKVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200fREEBOOTDISKVMDB_Type.__name__ = "Integer32"
_Valuei3200fREEBOOTDISKVMDB_Object = MibScalar
valuei3200fREEBOOTDISKVMDB = _Valuei3200fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3200, 3),
    _Valuei3200fREEBOOTDISKVMDB_Type()
)
valuei3200fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200fREEBOOTDISKVMDB.setStatus("mandatory")
_I3300fREEBOOTDISKVMDB_ObjectIdentity = ObjectIdentity
i3300fREEBOOTDISKVMDB = _I3300fREEBOOTDISKVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3300)
)


class _Severityi3300fREEBOOTDISKVMDB_Type(OctetString):
    """Custom type severityi3300fREEBOOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300fREEBOOTDISKVMDB_Type.__name__ = "OctetString"
_Severityi3300fREEBOOTDISKVMDB_Object = MibScalar
severityi3300fREEBOOTDISKVMDB = _Severityi3300fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3300, 1),
    _Severityi3300fREEBOOTDISKVMDB_Type()
)
severityi3300fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300fREEBOOTDISKVMDB.setStatus("mandatory")


class _Messagei3300fREEBOOTDISKVMDB_Type(OctetString):
    """Custom type messagei3300fREEBOOTDISKVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300fREEBOOTDISKVMDB_Type.__name__ = "OctetString"
_Messagei3300fREEBOOTDISKVMDB_Object = MibScalar
messagei3300fREEBOOTDISKVMDB = _Messagei3300fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3300, 2),
    _Messagei3300fREEBOOTDISKVMDB_Type()
)
messagei3300fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300fREEBOOTDISKVMDB.setStatus("mandatory")


class _Valuei3300fREEBOOTDISKVMDB_Type(Integer32):
    """Custom type valuei3300fREEBOOTDISKVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300fREEBOOTDISKVMDB_Type.__name__ = "Integer32"
_Valuei3300fREEBOOTDISKVMDB_Object = MibScalar
valuei3300fREEBOOTDISKVMDB = _Valuei3300fREEBOOTDISKVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3300, 3),
    _Valuei3300fREEBOOTDISKVMDB_Type()
)
valuei3300fREEBOOTDISKVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300fREEBOOTDISKVMDB.setStatus("mandatory")
_FREEMEMORYVMDB_ObjectIdentity = ObjectIdentity
fREEMEMORYVMDB = _FREEMEMORYVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3)
)
_I3100fREEMEMORYVMDB_ObjectIdentity = ObjectIdentity
i3100fREEMEMORYVMDB = _I3100fREEMEMORYVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3100)
)


class _Severityi3100fREEMEMORYVMDB_Type(OctetString):
    """Custom type severityi3100fREEMEMORYVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100fREEMEMORYVMDB_Type.__name__ = "OctetString"
_Severityi3100fREEMEMORYVMDB_Object = MibScalar
severityi3100fREEMEMORYVMDB = _Severityi3100fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3100, 1),
    _Severityi3100fREEMEMORYVMDB_Type()
)
severityi3100fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100fREEMEMORYVMDB.setStatus("mandatory")


class _Messagei3100fREEMEMORYVMDB_Type(OctetString):
    """Custom type messagei3100fREEMEMORYVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100fREEMEMORYVMDB_Type.__name__ = "OctetString"
_Messagei3100fREEMEMORYVMDB_Object = MibScalar
messagei3100fREEMEMORYVMDB = _Messagei3100fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3100, 2),
    _Messagei3100fREEMEMORYVMDB_Type()
)
messagei3100fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100fREEMEMORYVMDB.setStatus("mandatory")


class _Valuei3100fREEMEMORYVMDB_Type(Integer32):
    """Custom type valuei3100fREEMEMORYVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100fREEMEMORYVMDB_Type.__name__ = "Integer32"
_Valuei3100fREEMEMORYVMDB_Object = MibScalar
valuei3100fREEMEMORYVMDB = _Valuei3100fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3100, 3),
    _Valuei3100fREEMEMORYVMDB_Type()
)
valuei3100fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100fREEMEMORYVMDB.setStatus("mandatory")
_I3200fREEMEMORYVMDB_ObjectIdentity = ObjectIdentity
i3200fREEMEMORYVMDB = _I3200fREEMEMORYVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3200)
)


class _Severityi3200fREEMEMORYVMDB_Type(OctetString):
    """Custom type severityi3200fREEMEMORYVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200fREEMEMORYVMDB_Type.__name__ = "OctetString"
_Severityi3200fREEMEMORYVMDB_Object = MibScalar
severityi3200fREEMEMORYVMDB = _Severityi3200fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3200, 1),
    _Severityi3200fREEMEMORYVMDB_Type()
)
severityi3200fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200fREEMEMORYVMDB.setStatus("mandatory")


class _Messagei3200fREEMEMORYVMDB_Type(OctetString):
    """Custom type messagei3200fREEMEMORYVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200fREEMEMORYVMDB_Type.__name__ = "OctetString"
_Messagei3200fREEMEMORYVMDB_Object = MibScalar
messagei3200fREEMEMORYVMDB = _Messagei3200fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3200, 2),
    _Messagei3200fREEMEMORYVMDB_Type()
)
messagei3200fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200fREEMEMORYVMDB.setStatus("mandatory")


class _Valuei3200fREEMEMORYVMDB_Type(Integer32):
    """Custom type valuei3200fREEMEMORYVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200fREEMEMORYVMDB_Type.__name__ = "Integer32"
_Valuei3200fREEMEMORYVMDB_Object = MibScalar
valuei3200fREEMEMORYVMDB = _Valuei3200fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3200, 3),
    _Valuei3200fREEMEMORYVMDB_Type()
)
valuei3200fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200fREEMEMORYVMDB.setStatus("mandatory")
_I3300fREEMEMORYVMDB_ObjectIdentity = ObjectIdentity
i3300fREEMEMORYVMDB = _I3300fREEMEMORYVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3300)
)


class _Severityi3300fREEMEMORYVMDB_Type(OctetString):
    """Custom type severityi3300fREEMEMORYVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300fREEMEMORYVMDB_Type.__name__ = "OctetString"
_Severityi3300fREEMEMORYVMDB_Object = MibScalar
severityi3300fREEMEMORYVMDB = _Severityi3300fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3300, 1),
    _Severityi3300fREEMEMORYVMDB_Type()
)
severityi3300fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300fREEMEMORYVMDB.setStatus("mandatory")


class _Messagei3300fREEMEMORYVMDB_Type(OctetString):
    """Custom type messagei3300fREEMEMORYVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300fREEMEMORYVMDB_Type.__name__ = "OctetString"
_Messagei3300fREEMEMORYVMDB_Object = MibScalar
messagei3300fREEMEMORYVMDB = _Messagei3300fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3300, 2),
    _Messagei3300fREEMEMORYVMDB_Type()
)
messagei3300fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300fREEMEMORYVMDB.setStatus("mandatory")


class _Valuei3300fREEMEMORYVMDB_Type(Integer32):
    """Custom type valuei3300fREEMEMORYVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300fREEMEMORYVMDB_Type.__name__ = "Integer32"
_Valuei3300fREEMEMORYVMDB_Object = MibScalar
valuei3300fREEMEMORYVMDB = _Valuei3300fREEMEMORYVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3300, 3),
    _Valuei3300fREEMEMORYVMDB_Type()
)
valuei3300fREEMEMORYVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300fREEMEMORYVMDB.setStatus("mandatory")
_CPULOADVMDB_ObjectIdentity = ObjectIdentity
cPULOADVMDB = _CPULOADVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4)
)
_I3100cPULOADVMDB_ObjectIdentity = ObjectIdentity
i3100cPULOADVMDB = _I3100cPULOADVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3100)
)


class _Severityi3100cPULOADVMDB_Type(OctetString):
    """Custom type severityi3100cPULOADVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100cPULOADVMDB_Type.__name__ = "OctetString"
_Severityi3100cPULOADVMDB_Object = MibScalar
severityi3100cPULOADVMDB = _Severityi3100cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3100, 1),
    _Severityi3100cPULOADVMDB_Type()
)
severityi3100cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100cPULOADVMDB.setStatus("mandatory")


class _Messagei3100cPULOADVMDB_Type(OctetString):
    """Custom type messagei3100cPULOADVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100cPULOADVMDB_Type.__name__ = "OctetString"
_Messagei3100cPULOADVMDB_Object = MibScalar
messagei3100cPULOADVMDB = _Messagei3100cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3100, 2),
    _Messagei3100cPULOADVMDB_Type()
)
messagei3100cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100cPULOADVMDB.setStatus("mandatory")


class _Valuei3100cPULOADVMDB_Type(Integer32):
    """Custom type valuei3100cPULOADVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100cPULOADVMDB_Type.__name__ = "Integer32"
_Valuei3100cPULOADVMDB_Object = MibScalar
valuei3100cPULOADVMDB = _Valuei3100cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3100, 3),
    _Valuei3100cPULOADVMDB_Type()
)
valuei3100cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100cPULOADVMDB.setStatus("mandatory")
_I3200cPULOADVMDB_ObjectIdentity = ObjectIdentity
i3200cPULOADVMDB = _I3200cPULOADVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3200)
)


class _Severityi3200cPULOADVMDB_Type(OctetString):
    """Custom type severityi3200cPULOADVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200cPULOADVMDB_Type.__name__ = "OctetString"
_Severityi3200cPULOADVMDB_Object = MibScalar
severityi3200cPULOADVMDB = _Severityi3200cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3200, 1),
    _Severityi3200cPULOADVMDB_Type()
)
severityi3200cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200cPULOADVMDB.setStatus("mandatory")


class _Messagei3200cPULOADVMDB_Type(OctetString):
    """Custom type messagei3200cPULOADVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200cPULOADVMDB_Type.__name__ = "OctetString"
_Messagei3200cPULOADVMDB_Object = MibScalar
messagei3200cPULOADVMDB = _Messagei3200cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3200, 2),
    _Messagei3200cPULOADVMDB_Type()
)
messagei3200cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200cPULOADVMDB.setStatus("mandatory")


class _Valuei3200cPULOADVMDB_Type(Integer32):
    """Custom type valuei3200cPULOADVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200cPULOADVMDB_Type.__name__ = "Integer32"
_Valuei3200cPULOADVMDB_Object = MibScalar
valuei3200cPULOADVMDB = _Valuei3200cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3200, 3),
    _Valuei3200cPULOADVMDB_Type()
)
valuei3200cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200cPULOADVMDB.setStatus("mandatory")
_I3300cPULOADVMDB_ObjectIdentity = ObjectIdentity
i3300cPULOADVMDB = _I3300cPULOADVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3300)
)


class _Severityi3300cPULOADVMDB_Type(OctetString):
    """Custom type severityi3300cPULOADVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300cPULOADVMDB_Type.__name__ = "OctetString"
_Severityi3300cPULOADVMDB_Object = MibScalar
severityi3300cPULOADVMDB = _Severityi3300cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3300, 1),
    _Severityi3300cPULOADVMDB_Type()
)
severityi3300cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300cPULOADVMDB.setStatus("mandatory")


class _Messagei3300cPULOADVMDB_Type(OctetString):
    """Custom type messagei3300cPULOADVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300cPULOADVMDB_Type.__name__ = "OctetString"
_Messagei3300cPULOADVMDB_Object = MibScalar
messagei3300cPULOADVMDB = _Messagei3300cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3300, 2),
    _Messagei3300cPULOADVMDB_Type()
)
messagei3300cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300cPULOADVMDB.setStatus("mandatory")


class _Valuei3300cPULOADVMDB_Type(Integer32):
    """Custom type valuei3300cPULOADVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300cPULOADVMDB_Type.__name__ = "Integer32"
_Valuei3300cPULOADVMDB_Object = MibScalar
valuei3300cPULOADVMDB = _Valuei3300cPULOADVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3300, 3),
    _Valuei3300cPULOADVMDB_Type()
)
valuei3300cPULOADVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300cPULOADVMDB.setStatus("mandatory")
_FREESWAPVMDB_ObjectIdentity = ObjectIdentity
fREESWAPVMDB = _FREESWAPVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5)
)
_I3100fREESWAPVMDB_ObjectIdentity = ObjectIdentity
i3100fREESWAPVMDB = _I3100fREESWAPVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3100)
)


class _Severityi3100fREESWAPVMDB_Type(OctetString):
    """Custom type severityi3100fREESWAPVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100fREESWAPVMDB_Type.__name__ = "OctetString"
_Severityi3100fREESWAPVMDB_Object = MibScalar
severityi3100fREESWAPVMDB = _Severityi3100fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3100, 1),
    _Severityi3100fREESWAPVMDB_Type()
)
severityi3100fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100fREESWAPVMDB.setStatus("mandatory")


class _Messagei3100fREESWAPVMDB_Type(OctetString):
    """Custom type messagei3100fREESWAPVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100fREESWAPVMDB_Type.__name__ = "OctetString"
_Messagei3100fREESWAPVMDB_Object = MibScalar
messagei3100fREESWAPVMDB = _Messagei3100fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3100, 2),
    _Messagei3100fREESWAPVMDB_Type()
)
messagei3100fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100fREESWAPVMDB.setStatus("mandatory")


class _Valuei3100fREESWAPVMDB_Type(Integer32):
    """Custom type valuei3100fREESWAPVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100fREESWAPVMDB_Type.__name__ = "Integer32"
_Valuei3100fREESWAPVMDB_Object = MibScalar
valuei3100fREESWAPVMDB = _Valuei3100fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3100, 3),
    _Valuei3100fREESWAPVMDB_Type()
)
valuei3100fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100fREESWAPVMDB.setStatus("mandatory")
_I3200fREESWAPVMDB_ObjectIdentity = ObjectIdentity
i3200fREESWAPVMDB = _I3200fREESWAPVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3200)
)


class _Severityi3200fREESWAPVMDB_Type(OctetString):
    """Custom type severityi3200fREESWAPVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200fREESWAPVMDB_Type.__name__ = "OctetString"
_Severityi3200fREESWAPVMDB_Object = MibScalar
severityi3200fREESWAPVMDB = _Severityi3200fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3200, 1),
    _Severityi3200fREESWAPVMDB_Type()
)
severityi3200fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200fREESWAPVMDB.setStatus("mandatory")


class _Messagei3200fREESWAPVMDB_Type(OctetString):
    """Custom type messagei3200fREESWAPVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200fREESWAPVMDB_Type.__name__ = "OctetString"
_Messagei3200fREESWAPVMDB_Object = MibScalar
messagei3200fREESWAPVMDB = _Messagei3200fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3200, 2),
    _Messagei3200fREESWAPVMDB_Type()
)
messagei3200fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200fREESWAPVMDB.setStatus("mandatory")


class _Valuei3200fREESWAPVMDB_Type(Integer32):
    """Custom type valuei3200fREESWAPVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200fREESWAPVMDB_Type.__name__ = "Integer32"
_Valuei3200fREESWAPVMDB_Object = MibScalar
valuei3200fREESWAPVMDB = _Valuei3200fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3200, 3),
    _Valuei3200fREESWAPVMDB_Type()
)
valuei3200fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200fREESWAPVMDB.setStatus("mandatory")
_I3300fREESWAPVMDB_ObjectIdentity = ObjectIdentity
i3300fREESWAPVMDB = _I3300fREESWAPVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3300)
)


class _Severityi3300fREESWAPVMDB_Type(OctetString):
    """Custom type severityi3300fREESWAPVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300fREESWAPVMDB_Type.__name__ = "OctetString"
_Severityi3300fREESWAPVMDB_Object = MibScalar
severityi3300fREESWAPVMDB = _Severityi3300fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3300, 1),
    _Severityi3300fREESWAPVMDB_Type()
)
severityi3300fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300fREESWAPVMDB.setStatus("mandatory")


class _Messagei3300fREESWAPVMDB_Type(OctetString):
    """Custom type messagei3300fREESWAPVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300fREESWAPVMDB_Type.__name__ = "OctetString"
_Messagei3300fREESWAPVMDB_Object = MibScalar
messagei3300fREESWAPVMDB = _Messagei3300fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3300, 2),
    _Messagei3300fREESWAPVMDB_Type()
)
messagei3300fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300fREESWAPVMDB.setStatus("mandatory")


class _Valuei3300fREESWAPVMDB_Type(Integer32):
    """Custom type valuei3300fREESWAPVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300fREESWAPVMDB_Type.__name__ = "Integer32"
_Valuei3300fREESWAPVMDB_Object = MibScalar
valuei3300fREESWAPVMDB = _Valuei3300fREESWAPVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3300, 3),
    _Valuei3300fREESWAPVMDB_Type()
)
valuei3300fREESWAPVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300fREESWAPVMDB.setStatus("mandatory")
_ETHINTSTATUSVMDB_ObjectIdentity = ObjectIdentity
eTHINTSTATUSVMDB = _ETHINTSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6)
)
_I3100eTHINTSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3100eTHINTSTATUSVMDB = _I3100eTHINTSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3100)
)


class _Severityi3100eTHINTSTATUSVMDB_Type(OctetString):
    """Custom type severityi3100eTHINTSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100eTHINTSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100eTHINTSTATUSVMDB_Object = MibScalar
severityi3100eTHINTSTATUSVMDB = _Severityi3100eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3100, 1),
    _Severityi3100eTHINTSTATUSVMDB_Type()
)
severityi3100eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100eTHINTSTATUSVMDB.setStatus("mandatory")


class _Messagei3100eTHINTSTATUSVMDB_Type(OctetString):
    """Custom type messagei3100eTHINTSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100eTHINTSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100eTHINTSTATUSVMDB_Object = MibScalar
messagei3100eTHINTSTATUSVMDB = _Messagei3100eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3100, 2),
    _Messagei3100eTHINTSTATUSVMDB_Type()
)
messagei3100eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100eTHINTSTATUSVMDB.setStatus("mandatory")


class _Valuei3100eTHINTSTATUSVMDBe_Type(Integer32):
    """Custom type valuei3100eTHINTSTATUSVMDBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100eTHINTSTATUSVMDBe_Type.__name__ = "Integer32"
_Valuei3100eTHINTSTATUSVMDBe_Object = MibScalar
valuei3100eTHINTSTATUSVMDBe = _Valuei3100eTHINTSTATUSVMDBe_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3100, 3),
    _Valuei3100eTHINTSTATUSVMDBe_Type()
)
valuei3100eTHINTSTATUSVMDBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100eTHINTSTATUSVMDBe.setStatus("mandatory")
_I3200eTHINTSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3200eTHINTSTATUSVMDB = _I3200eTHINTSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3200)
)


class _Severityi3200eTHINTSTATUSVMDB_Type(OctetString):
    """Custom type severityi3200eTHINTSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200eTHINTSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200eTHINTSTATUSVMDB_Object = MibScalar
severityi3200eTHINTSTATUSVMDB = _Severityi3200eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3200, 1),
    _Severityi3200eTHINTSTATUSVMDB_Type()
)
severityi3200eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200eTHINTSTATUSVMDB.setStatus("mandatory")


class _Messagei3200eTHINTSTATUSVMDB_Type(OctetString):
    """Custom type messagei3200eTHINTSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200eTHINTSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200eTHINTSTATUSVMDB_Object = MibScalar
messagei3200eTHINTSTATUSVMDB = _Messagei3200eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3200, 2),
    _Messagei3200eTHINTSTATUSVMDB_Type()
)
messagei3200eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200eTHINTSTATUSVMDB.setStatus("mandatory")


class _Valuei3200eTHINTSTATUSVMDB_Type(Integer32):
    """Custom type valuei3200eTHINTSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200eTHINTSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200eTHINTSTATUSVMDB_Object = MibScalar
valuei3200eTHINTSTATUSVMDB = _Valuei3200eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3200, 3),
    _Valuei3200eTHINTSTATUSVMDB_Type()
)
valuei3200eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200eTHINTSTATUSVMDB.setStatus("mandatory")
_I3300eTHINTSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3300eTHINTSTATUSVMDB = _I3300eTHINTSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3300)
)


class _Severityi3300eTHINTSTATUSVMDB_Type(OctetString):
    """Custom type severityi3300eTHINTSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300eTHINTSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300eTHINTSTATUSVMDB_Object = MibScalar
severityi3300eTHINTSTATUSVMDB = _Severityi3300eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3300, 1),
    _Severityi3300eTHINTSTATUSVMDB_Type()
)
severityi3300eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300eTHINTSTATUSVMDB.setStatus("mandatory")


class _Messagei3300eTHINTSTATUSVMDB_Type(OctetString):
    """Custom type messagei3300eTHINTSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300eTHINTSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300eTHINTSTATUSVMDB_Object = MibScalar
messagei3300eTHINTSTATUSVMDB = _Messagei3300eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3300, 2),
    _Messagei3300eTHINTSTATUSVMDB_Type()
)
messagei3300eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300eTHINTSTATUSVMDB.setStatus("mandatory")


class _Valuei3300eTHINTSTATUSVMDB_Type(Integer32):
    """Custom type valuei3300eTHINTSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300eTHINTSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300eTHINTSTATUSVMDB_Object = MibScalar
valuei3300eTHINTSTATUSVMDB = _Valuei3300eTHINTSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3300, 3),
    _Valuei3300eTHINTSTATUSVMDB_Type()
)
valuei3300eTHINTSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300eTHINTSTATUSVMDB.setStatus("mandatory")
_CRONSTATUSVMDB_ObjectIdentity = ObjectIdentity
cRONSTATUSVMDB = _CRONSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7)
)
_I3100cRONSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3100cRONSTATUSVMDB = _I3100cRONSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3100)
)


class _Severityi3100cRONSTATUSVMDB_Type(OctetString):
    """Custom type severityi3100cRONSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100cRONSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100cRONSTATUSVMDB_Object = MibScalar
severityi3100cRONSTATUSVMDB = _Severityi3100cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3100, 1),
    _Severityi3100cRONSTATUSVMDB_Type()
)
severityi3100cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100cRONSTATUSVMDB.setStatus("mandatory")


class _Messagei3100cRONSTATUSVMDB_Type(OctetString):
    """Custom type messagei3100cRONSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100cRONSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100cRONSTATUSVMDB_Object = MibScalar
messagei3100cRONSTATUSVMDB = _Messagei3100cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3100, 2),
    _Messagei3100cRONSTATUSVMDB_Type()
)
messagei3100cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100cRONSTATUSVMDB.setStatus("mandatory")


class _Valuei3100cRONSTATUSVMDB_Type(Integer32):
    """Custom type valuei3100cRONSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100cRONSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3100cRONSTATUSVMDB_Object = MibScalar
valuei3100cRONSTATUSVMDB = _Valuei3100cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3100, 3),
    _Valuei3100cRONSTATUSVMDB_Type()
)
valuei3100cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100cRONSTATUSVMDB.setStatus("mandatory")
_I3200cRONSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3200cRONSTATUSVMDB = _I3200cRONSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3200)
)


class _Severityi3200cRONSTATUSVMDB_Type(OctetString):
    """Custom type severityi3200cRONSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200cRONSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200cRONSTATUSVMDB_Object = MibScalar
severityi3200cRONSTATUSVMDB = _Severityi3200cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3200, 1),
    _Severityi3200cRONSTATUSVMDB_Type()
)
severityi3200cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200cRONSTATUSVMDB.setStatus("mandatory")


class _Messagei3200cRONSTATUSVMDB_Type(OctetString):
    """Custom type messagei3200cRONSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200cRONSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200cRONSTATUSVMDB_Object = MibScalar
messagei3200cRONSTATUSVMDB = _Messagei3200cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3200, 2),
    _Messagei3200cRONSTATUSVMDB_Type()
)
messagei3200cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200cRONSTATUSVMDB.setStatus("mandatory")


class _Valuei3200cRONSTATUSVMDB_Type(Integer32):
    """Custom type valuei3200cRONSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200cRONSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200cRONSTATUSVMDB_Object = MibScalar
valuei3200cRONSTATUSVMDB = _Valuei3200cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3200, 3),
    _Valuei3200cRONSTATUSVMDB_Type()
)
valuei3200cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200cRONSTATUSVMDB.setStatus("mandatory")
_I3300cRONSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3300cRONSTATUSVMDB = _I3300cRONSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3300)
)


class _Severityi3300cRONSTATUSVMDB_Type(OctetString):
    """Custom type severityi3300cRONSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300cRONSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300cRONSTATUSVMDB_Object = MibScalar
severityi3300cRONSTATUSVMDB = _Severityi3300cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3300, 1),
    _Severityi3300cRONSTATUSVMDB_Type()
)
severityi3300cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300cRONSTATUSVMDB.setStatus("mandatory")


class _Messagei3300cRONSTATUSVMDB_Type(OctetString):
    """Custom type messagei3300cRONSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300cRONSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300cRONSTATUSVMDB_Object = MibScalar
messagei3300cRONSTATUSVMDB = _Messagei3300cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3300, 2),
    _Messagei3300cRONSTATUSVMDB_Type()
)
messagei3300cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300cRONSTATUSVMDB.setStatus("mandatory")


class _Valuei3300cRONSTATUSVMDB_Type(Integer32):
    """Custom type valuei3300cRONSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300cRONSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300cRONSTATUSVMDB_Object = MibScalar
valuei3300cRONSTATUSVMDB = _Valuei3300cRONSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3300, 3),
    _Valuei3300cRONSTATUSVMDB_Type()
)
valuei3300cRONSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300cRONSTATUSVMDB.setStatus("mandatory")
_MONITSTATUSVMDB_ObjectIdentity = ObjectIdentity
mONITSTATUSVMDB = _MONITSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8)
)
_I3100mONITSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3100mONITSTATUSVMDB = _I3100mONITSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3100)
)


class _Severityi3100mONITSTATUSVMDB_Type(OctetString):
    """Custom type severityi3100mONITSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100mONITSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100mONITSTATUSVMDB_Object = MibScalar
severityi3100mONITSTATUSVMDB = _Severityi3100mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3100, 1),
    _Severityi3100mONITSTATUSVMDB_Type()
)
severityi3100mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100mONITSTATUSVMDB.setStatus("mandatory")


class _Messagei3100mONITSTATUSVMDB_Type(OctetString):
    """Custom type messagei3100mONITSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100mONITSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100mONITSTATUSVMDB_Object = MibScalar
messagei3100mONITSTATUSVMDB = _Messagei3100mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3100, 2),
    _Messagei3100mONITSTATUSVMDB_Type()
)
messagei3100mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100mONITSTATUSVMDB.setStatus("mandatory")


class _Valuei3100mONITSTATUSVMDB_Type(Integer32):
    """Custom type valuei3100mONITSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100mONITSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3100mONITSTATUSVMDB_Object = MibScalar
valuei3100mONITSTATUSVMDB = _Valuei3100mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3100, 3),
    _Valuei3100mONITSTATUSVMDB_Type()
)
valuei3100mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100mONITSTATUSVMDB.setStatus("mandatory")
_I3200mONITSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3200mONITSTATUSVMDB = _I3200mONITSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3200)
)


class _Severityi3200mONITSTATUSVMDB_Type(OctetString):
    """Custom type severityi3200mONITSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200mONITSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200mONITSTATUSVMDB_Object = MibScalar
severityi3200mONITSTATUSVMDB = _Severityi3200mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3200, 1),
    _Severityi3200mONITSTATUSVMDB_Type()
)
severityi3200mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200mONITSTATUSVMDB.setStatus("mandatory")


class _Messagei3200mONITSTATUSVMDB_Type(OctetString):
    """Custom type messagei3200mONITSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200mONITSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200mONITSTATUSVMDB_Object = MibScalar
messagei3200mONITSTATUSVMDB = _Messagei3200mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3200, 2),
    _Messagei3200mONITSTATUSVMDB_Type()
)
messagei3200mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200mONITSTATUSVMDB.setStatus("mandatory")


class _Valuei3200mONITSTATUSVMDB_Type(Integer32):
    """Custom type valuei3200mONITSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200mONITSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200mONITSTATUSVMDB_Object = MibScalar
valuei3200mONITSTATUSVMDB = _Valuei3200mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3200, 3),
    _Valuei3200mONITSTATUSVMDB_Type()
)
valuei3200mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200mONITSTATUSVMDB.setStatus("mandatory")
_I3300mONITSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3300mONITSTATUSVMDB = _I3300mONITSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3300)
)


class _Severityi3300mONITSTATUSVMDB_Type(OctetString):
    """Custom type severityi3300mONITSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300mONITSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300mONITSTATUSVMDB_Object = MibScalar
severityi3300mONITSTATUSVMDB = _Severityi3300mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3300, 1),
    _Severityi3300mONITSTATUSVMDB_Type()
)
severityi3300mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300mONITSTATUSVMDB.setStatus("mandatory")


class _Messagei3300mONITSTATUSVMDB_Type(OctetString):
    """Custom type messagei3300mONITSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300mONITSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300mONITSTATUSVMDB_Object = MibScalar
messagei3300mONITSTATUSVMDB = _Messagei3300mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3300, 2),
    _Messagei3300mONITSTATUSVMDB_Type()
)
messagei3300mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300mONITSTATUSVMDB.setStatus("mandatory")


class _Valuei3300mONITSTATUSVMDB_Type(Integer32):
    """Custom type valuei3300mONITSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300mONITSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300mONITSTATUSVMDB_Object = MibScalar
valuei3300mONITSTATUSVMDB = _Valuei3300mONITSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3300, 3),
    _Valuei3300mONITSTATUSVMDB_Type()
)
valuei3300mONITSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300mONITSTATUSVMDB.setStatus("mandatory")
_POSTGRESSTATUSVMDB_ObjectIdentity = ObjectIdentity
pOSTGRESSTATUSVMDB = _POSTGRESSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15)
)
_I3100pOSTGRESSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3100pOSTGRESSTATUSVMDB = _I3100pOSTGRESSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3100)
)


class _Severityi3100pOSTGRESSTATUSVMDB_Type(OctetString):
    """Custom type severityi3100pOSTGRESSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100pOSTGRESSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100pOSTGRESSTATUSVMDB_Object = MibScalar
severityi3100pOSTGRESSTATUSVMDB = _Severityi3100pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3100, 1),
    _Severityi3100pOSTGRESSTATUSVMDB_Type()
)
severityi3100pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100pOSTGRESSTATUSVMDB.setStatus("mandatory")


class _Messagei3100pOSTGRESSTATUSVMDB_Type(OctetString):
    """Custom type messagei3100pOSTGRESSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100pOSTGRESSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100pOSTGRESSTATUSVMDB_Object = MibScalar
messagei3100pOSTGRESSTATUSVMDB = _Messagei3100pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3100, 2),
    _Messagei3100pOSTGRESSTATUSVMDB_Type()
)
messagei3100pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100pOSTGRESSTATUSVMDB.setStatus("mandatory")


class _Valuei3100pOSTGRESSTATUSVMDB_Type(Integer32):
    """Custom type valuei3100pOSTGRESSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100pOSTGRESSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3100pOSTGRESSTATUSVMDB_Object = MibScalar
valuei3100pOSTGRESSTATUSVMDB = _Valuei3100pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3100, 3),
    _Valuei3100pOSTGRESSTATUSVMDB_Type()
)
valuei3100pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100pOSTGRESSTATUSVMDB.setStatus("mandatory")
_I3200pOSTGRESSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3200pOSTGRESSTATUSVMDB = _I3200pOSTGRESSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3200)
)


class _Severityi3200pOSTGRESSTATUSVMDB_Type(OctetString):
    """Custom type severityi3200pOSTGRESSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200pOSTGRESSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200pOSTGRESSTATUSVMDB_Object = MibScalar
severityi3200pOSTGRESSTATUSVMDB = _Severityi3200pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3200, 1),
    _Severityi3200pOSTGRESSTATUSVMDB_Type()
)
severityi3200pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200pOSTGRESSTATUSVMDB.setStatus("mandatory")


class _Messagei3200pOSTGRESSTATUSVMDB_Type(OctetString):
    """Custom type messagei3200pOSTGRESSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200pOSTGRESSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200pOSTGRESSTATUSVMDB_Object = MibScalar
messagei3200pOSTGRESSTATUSVMDB = _Messagei3200pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3200, 2),
    _Messagei3200pOSTGRESSTATUSVMDB_Type()
)
messagei3200pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200pOSTGRESSTATUSVMDB.setStatus("mandatory")


class _Valuei3200pOSTGRESSTATUSVMDB_Type(Integer32):
    """Custom type valuei3200pOSTGRESSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200pOSTGRESSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200pOSTGRESSTATUSVMDB_Object = MibScalar
valuei3200pOSTGRESSTATUSVMDB = _Valuei3200pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3200, 3),
    _Valuei3200pOSTGRESSTATUSVMDB_Type()
)
valuei3200pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200pOSTGRESSTATUSVMDB.setStatus("mandatory")
_I3300pOSTGRESSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3300pOSTGRESSTATUSVMDB = _I3300pOSTGRESSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3300)
)


class _Severityi3300pOSTGRESSTATUSVMDB_Type(OctetString):
    """Custom type severityi3300pOSTGRESSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300pOSTGRESSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300pOSTGRESSTATUSVMDB_Object = MibScalar
severityi3300pOSTGRESSTATUSVMDB = _Severityi3300pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3300, 1),
    _Severityi3300pOSTGRESSTATUSVMDB_Type()
)
severityi3300pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300pOSTGRESSTATUSVMDB.setStatus("mandatory")


class _Messagei3300pOSTGRESSTATUSVMDB_Type(OctetString):
    """Custom type messagei3300pOSTGRESSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300pOSTGRESSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300pOSTGRESSTATUSVMDB_Object = MibScalar
messagei3300pOSTGRESSTATUSVMDB = _Messagei3300pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3300, 2),
    _Messagei3300pOSTGRESSTATUSVMDB_Type()
)
messagei3300pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300pOSTGRESSTATUSVMDB.setStatus("mandatory")


class _Valuei3300pOSTGRESSTATUSVMDB_Type(Integer32):
    """Custom type valuei3300pOSTGRESSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300pOSTGRESSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300pOSTGRESSTATUSVMDB_Object = MibScalar
valuei3300pOSTGRESSTATUSVMDB = _Valuei3300pOSTGRESSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3300, 3),
    _Valuei3300pOSTGRESSTATUSVMDB_Type()
)
valuei3300pOSTGRESSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300pOSTGRESSTATUSVMDB.setStatus("mandatory")
_PGPOOLSTATUSVMDB_ObjectIdentity = ObjectIdentity
pGPOOLSTATUSVMDB = _PGPOOLSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16)
)
_I3100pGPOOLSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3100pGPOOLSTATUSVMDB = _I3100pGPOOLSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3100)
)


class _Severityi3100pGPOOLSTATUSVMDB_Type(OctetString):
    """Custom type severityi3100pGPOOLSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100pGPOOLSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100pGPOOLSTATUSVMDB_Object = MibScalar
severityi3100pGPOOLSTATUSVMDB = _Severityi3100pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3100, 1),
    _Severityi3100pGPOOLSTATUSVMDB_Type()
)
severityi3100pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100pGPOOLSTATUSVMDB.setStatus("mandatory")


class _Messagei3100pGPOOLSTATUSVMDB_Type(OctetString):
    """Custom type messagei3100pGPOOLSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100pGPOOLSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100pGPOOLSTATUSVMDB_Object = MibScalar
messagei3100pGPOOLSTATUSVMDB = _Messagei3100pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3100, 2),
    _Messagei3100pGPOOLSTATUSVMDB_Type()
)
messagei3100pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100pGPOOLSTATUSVMDB.setStatus("mandatory")


class _Valuei3100pGPOOLSTATUSVMDB_Type(Integer32):
    """Custom type valuei3100pGPOOLSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100pGPOOLSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3100pGPOOLSTATUSVMDB_Object = MibScalar
valuei3100pGPOOLSTATUSVMDB = _Valuei3100pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3100, 3),
    _Valuei3100pGPOOLSTATUSVMDB_Type()
)
valuei3100pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100pGPOOLSTATUSVMDB.setStatus("mandatory")
_I3200pGPOOLSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3200pGPOOLSTATUSVMDB = _I3200pGPOOLSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3200)
)


class _Severityi3200pGPOOLSTATUSVMDB_Type(OctetString):
    """Custom type severityi3200pGPOOLSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200pGPOOLSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200pGPOOLSTATUSVMDB_Object = MibScalar
severityi3200pGPOOLSTATUSVMDB = _Severityi3200pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3200, 1),
    _Severityi3200pGPOOLSTATUSVMDB_Type()
)
severityi3200pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200pGPOOLSTATUSVMDB.setStatus("mandatory")


class _Messagei3200pGPOOLSTATUSVMDB_Type(OctetString):
    """Custom type messagei3200pGPOOLSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200pGPOOLSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200pGPOOLSTATUSVMDB_Object = MibScalar
messagei3200pGPOOLSTATUSVMDB = _Messagei3200pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3200, 2),
    _Messagei3200pGPOOLSTATUSVMDB_Type()
)
messagei3200pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200pGPOOLSTATUSVMDB.setStatus("mandatory")


class _Valuei3200pGPOOLSTATUSVMDB_Type(Integer32):
    """Custom type valuei3200pGPOOLSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200pGPOOLSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200pGPOOLSTATUSVMDB_Object = MibScalar
valuei3200pGPOOLSTATUSVMDB = _Valuei3200pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3200, 3),
    _Valuei3200pGPOOLSTATUSVMDB_Type()
)
valuei3200pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200pGPOOLSTATUSVMDB.setStatus("mandatory")
_I3300pGPOOLSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3300pGPOOLSTATUSVMDB = _I3300pGPOOLSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3300)
)


class _Severityi3300pGPOOLSTATUSVMDB_Type(OctetString):
    """Custom type severityi3300pGPOOLSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300pGPOOLSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300pGPOOLSTATUSVMDB_Object = MibScalar
severityi3300pGPOOLSTATUSVMDB = _Severityi3300pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3300, 1),
    _Severityi3300pGPOOLSTATUSVMDB_Type()
)
severityi3300pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300pGPOOLSTATUSVMDB.setStatus("mandatory")


class _Messagei3300pGPOOLSTATUSVMDB_Type(OctetString):
    """Custom type messagei3300pGPOOLSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300pGPOOLSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300pGPOOLSTATUSVMDB_Object = MibScalar
messagei3300pGPOOLSTATUSVMDB = _Messagei3300pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3300, 2),
    _Messagei3300pGPOOLSTATUSVMDB_Type()
)
messagei3300pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300pGPOOLSTATUSVMDB.setStatus("mandatory")


class _Valuei3300pGPOOLSTATUSVMDB_Type(Integer32):
    """Custom type valuei3300pGPOOLSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300pGPOOLSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300pGPOOLSTATUSVMDB_Object = MibScalar
valuei3300pGPOOLSTATUSVMDB = _Valuei3300pGPOOLSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3300, 3),
    _Valuei3300pGPOOLSTATUSVMDB_Type()
)
valuei3300pGPOOLSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300pGPOOLSTATUSVMDB.setStatus("mandatory")
_PGAGENTSATUSVMDB_ObjectIdentity = ObjectIdentity
pGAGENTSATUSVMDB = _PGAGENTSATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17)
)
_I3100pGAGENTSATUSVMDB_ObjectIdentity = ObjectIdentity
i3100pGAGENTSATUSVMDB = _I3100pGAGENTSATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3100)
)


class _Severityi3100pGAGENTSATUSVMDB_Type(OctetString):
    """Custom type severityi3100pGAGENTSATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100pGAGENTSATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100pGAGENTSATUSVMDB_Object = MibScalar
severityi3100pGAGENTSATUSVMDB = _Severityi3100pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3100, 1),
    _Severityi3100pGAGENTSATUSVMDB_Type()
)
severityi3100pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100pGAGENTSATUSVMDB.setStatus("mandatory")


class _Messagei3100pGAGENTSATUSVMDB_Type(OctetString):
    """Custom type messagei3100pGAGENTSATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100pGAGENTSATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100pGAGENTSATUSVMDB_Object = MibScalar
messagei3100pGAGENTSATUSVMDB = _Messagei3100pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3100, 2),
    _Messagei3100pGAGENTSATUSVMDB_Type()
)
messagei3100pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100pGAGENTSATUSVMDB.setStatus("mandatory")


class _Valuei3100pGAGENTSATUSVMDB_Type(Integer32):
    """Custom type valuei3100pGAGENTSATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100pGAGENTSATUSVMDB_Type.__name__ = "Integer32"
_Valuei3100pGAGENTSATUSVMDB_Object = MibScalar
valuei3100pGAGENTSATUSVMDB = _Valuei3100pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3100, 3),
    _Valuei3100pGAGENTSATUSVMDB_Type()
)
valuei3100pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100pGAGENTSATUSVMDB.setStatus("mandatory")
_I3200pGAGENTSATUSVMDB_ObjectIdentity = ObjectIdentity
i3200pGAGENTSATUSVMDB = _I3200pGAGENTSATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3200)
)


class _Severityi3200pGAGENTSATUSVMDB_Type(OctetString):
    """Custom type severityi3200pGAGENTSATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200pGAGENTSATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200pGAGENTSATUSVMDB_Object = MibScalar
severityi3200pGAGENTSATUSVMDB = _Severityi3200pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3200, 1),
    _Severityi3200pGAGENTSATUSVMDB_Type()
)
severityi3200pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200pGAGENTSATUSVMDB.setStatus("mandatory")


class _Messagei3200pGAGENTSATUSVMDB_Type(OctetString):
    """Custom type messagei3200pGAGENTSATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200pGAGENTSATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200pGAGENTSATUSVMDB_Object = MibScalar
messagei3200pGAGENTSATUSVMDB = _Messagei3200pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3200, 2),
    _Messagei3200pGAGENTSATUSVMDB_Type()
)
messagei3200pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200pGAGENTSATUSVMDB.setStatus("mandatory")


class _Valuei3200pGAGENTSATUSVMDB_Type(Integer32):
    """Custom type valuei3200pGAGENTSATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200pGAGENTSATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200pGAGENTSATUSVMDB_Object = MibScalar
valuei3200pGAGENTSATUSVMDB = _Valuei3200pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3200, 3),
    _Valuei3200pGAGENTSATUSVMDB_Type()
)
valuei3200pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200pGAGENTSATUSVMDB.setStatus("mandatory")
_I3300pGAGENTSATUSVMDB_ObjectIdentity = ObjectIdentity
i3300pGAGENTSATUSVMDB = _I3300pGAGENTSATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3300)
)


class _Severityi3300pGAGENTSATUSVMDB_Type(OctetString):
    """Custom type severityi3300pGAGENTSATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300pGAGENTSATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300pGAGENTSATUSVMDB_Object = MibScalar
severityi3300pGAGENTSATUSVMDB = _Severityi3300pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3300, 1),
    _Severityi3300pGAGENTSATUSVMDB_Type()
)
severityi3300pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300pGAGENTSATUSVMDB.setStatus("mandatory")


class _Messagei3300pGAGENTSATUSVMDB_Type(OctetString):
    """Custom type messagei3300pGAGENTSATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300pGAGENTSATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300pGAGENTSATUSVMDB_Object = MibScalar
messagei3300pGAGENTSATUSVMDB = _Messagei3300pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3300, 2),
    _Messagei3300pGAGENTSATUSVMDB_Type()
)
messagei3300pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300pGAGENTSATUSVMDB.setStatus("mandatory")


class _Valuei3300pGAGENTSATUSVMDB_Type(Integer32):
    """Custom type valuei3300pGAGENTSATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300pGAGENTSATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300pGAGENTSATUSVMDB_Object = MibScalar
valuei3300pGAGENTSATUSVMDB = _Valuei3300pGAGENTSATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3300, 3),
    _Valuei3300pGAGENTSATUSVMDB_Type()
)
valuei3300pGAGENTSATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300pGAGENTSATUSVMDB.setStatus("mandatory")
_CPUSTATUSVMDB_ObjectIdentity = ObjectIdentity
cPUSTATUSVMDB = _CPUSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18)
)
_I3100cPUSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3100cPUSTATUSVMDB = _I3100cPUSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3100)
)


class _Severityi3100cPUSTATUSVMDB_Type(OctetString):
    """Custom type severityi3100cPUSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3100cPUSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3100cPUSTATUSVMDB_Object = MibScalar
severityi3100cPUSTATUSVMDB = _Severityi3100cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3100, 1),
    _Severityi3100cPUSTATUSVMDB_Type()
)
severityi3100cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3100cPUSTATUSVMDB.setStatus("mandatory")


class _Messagei3100cPUSTATUSVMDB_Type(OctetString):
    """Custom type messagei3100cPUSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3100cPUSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3100cPUSTATUSVMDB_Object = MibScalar
messagei3100cPUSTATUSVMDB = _Messagei3100cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3100, 2),
    _Messagei3100cPUSTATUSVMDB_Type()
)
messagei3100cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3100cPUSTATUSVMDB.setStatus("mandatory")


class _Valuei3100cPUSTATUSVMDB_Type(Integer32):
    """Custom type valuei3100cPUSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3100cPUSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3100cPUSTATUSVMDB_Object = MibScalar
valuei3100cPUSTATUSVMDB = _Valuei3100cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3100, 3),
    _Valuei3100cPUSTATUSVMDB_Type()
)
valuei3100cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3100cPUSTATUSVMDB.setStatus("mandatory")
_I3200cPUSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3200cPUSTATUSVMDB = _I3200cPUSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3200)
)


class _Severityi3200cPUSTATUSVMDB_Type(OctetString):
    """Custom type severityi3200cPUSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3200cPUSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3200cPUSTATUSVMDB_Object = MibScalar
severityi3200cPUSTATUSVMDB = _Severityi3200cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3200, 1),
    _Severityi3200cPUSTATUSVMDB_Type()
)
severityi3200cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3200cPUSTATUSVMDB.setStatus("mandatory")


class _Messagei3200cPUSTATUSVMDB_Type(OctetString):
    """Custom type messagei3200cPUSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3200cPUSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3200cPUSTATUSVMDB_Object = MibScalar
messagei3200cPUSTATUSVMDB = _Messagei3200cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3200, 2),
    _Messagei3200cPUSTATUSVMDB_Type()
)
messagei3200cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3200cPUSTATUSVMDB.setStatus("mandatory")


class _Valuei3200cPUSTATUSVMDB_Type(Integer32):
    """Custom type valuei3200cPUSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3200cPUSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3200cPUSTATUSVMDB_Object = MibScalar
valuei3200cPUSTATUSVMDB = _Valuei3200cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3200, 3),
    _Valuei3200cPUSTATUSVMDB_Type()
)
valuei3200cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3200cPUSTATUSVMDB.setStatus("mandatory")
_I3300cPUSTATUSVMDB_ObjectIdentity = ObjectIdentity
i3300cPUSTATUSVMDB = _I3300cPUSTATUSVMDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3300)
)


class _Severityi3300cPUSTATUSVMDB_Type(OctetString):
    """Custom type severityi3300cPUSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi3300cPUSTATUSVMDB_Type.__name__ = "OctetString"
_Severityi3300cPUSTATUSVMDB_Object = MibScalar
severityi3300cPUSTATUSVMDB = _Severityi3300cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3300, 1),
    _Severityi3300cPUSTATUSVMDB_Type()
)
severityi3300cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi3300cPUSTATUSVMDB.setStatus("mandatory")


class _Messagei3300cPUSTATUSVMDB_Type(OctetString):
    """Custom type messagei3300cPUSTATUSVMDB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei3300cPUSTATUSVMDB_Type.__name__ = "OctetString"
_Messagei3300cPUSTATUSVMDB_Object = MibScalar
messagei3300cPUSTATUSVMDB = _Messagei3300cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3300, 2),
    _Messagei3300cPUSTATUSVMDB_Type()
)
messagei3300cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei3300cPUSTATUSVMDB.setStatus("mandatory")


class _Valuei3300cPUSTATUSVMDB_Type(Integer32):
    """Custom type valuei3300cPUSTATUSVMDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei3300cPUSTATUSVMDB_Type.__name__ = "Integer32"
_Valuei3300cPUSTATUSVMDB_Object = MibScalar
valuei3300cPUSTATUSVMDB = _Valuei3300cPUSTATUSVMDB_Object(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3300, 3),
    _Valuei3300cPUSTATUSVMDB_Type()
)
valuei3300cPUSTATUSVMDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei3300cPUSTATUSVMDB.setStatus("mandatory")
_Vmic_ObjectIdentity = ObjectIdentity
vmic = _Vmic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104)
)
_FREEROOTDISKVMIC_ObjectIdentity = ObjectIdentity
fREEROOTDISKVMIC = _FREEROOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1)
)
_I4100fREEROOTDISKVMIC_ObjectIdentity = ObjectIdentity
i4100fREEROOTDISKVMIC = _I4100fREEROOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4100)
)


class _Severityi4100fREEROOTDISKVMIC_Type(OctetString):
    """Custom type severityi4100fREEROOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100fREEROOTDISKVMIC_Type.__name__ = "OctetString"
_Severityi4100fREEROOTDISKVMIC_Object = MibScalar
severityi4100fREEROOTDISKVMIC = _Severityi4100fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4100, 1),
    _Severityi4100fREEROOTDISKVMIC_Type()
)
severityi4100fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100fREEROOTDISKVMIC.setStatus("mandatory")


class _Messagei4100fREEROOTDISKVMIC_Type(OctetString):
    """Custom type messagei4100fREEROOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100fREEROOTDISKVMIC_Type.__name__ = "OctetString"
_Messagei4100fREEROOTDISKVMIC_Object = MibScalar
messagei4100fREEROOTDISKVMIC = _Messagei4100fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4100, 2),
    _Messagei4100fREEROOTDISKVMIC_Type()
)
messagei4100fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100fREEROOTDISKVMIC.setStatus("mandatory")


class _Valuei4100fREEROOTDISKVMIC_Type(Integer32):
    """Custom type valuei4100fREEROOTDISKVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100fREEROOTDISKVMIC_Type.__name__ = "Integer32"
_Valuei4100fREEROOTDISKVMIC_Object = MibScalar
valuei4100fREEROOTDISKVMIC = _Valuei4100fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4100, 3),
    _Valuei4100fREEROOTDISKVMIC_Type()
)
valuei4100fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100fREEROOTDISKVMIC.setStatus("mandatory")
_I4200fREEROOTDISKVMIC_ObjectIdentity = ObjectIdentity
i4200fREEROOTDISKVMIC = _I4200fREEROOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4200)
)


class _Severityi4200fREEROOTDISKVMIC_Type(OctetString):
    """Custom type severityi4200fREEROOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200fREEROOTDISKVMIC_Type.__name__ = "OctetString"
_Severityi4200fREEROOTDISKVMIC_Object = MibScalar
severityi4200fREEROOTDISKVMIC = _Severityi4200fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4200, 1),
    _Severityi4200fREEROOTDISKVMIC_Type()
)
severityi4200fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200fREEROOTDISKVMIC.setStatus("mandatory")


class _Messagei4200fREEROOTDISKVMIC_Type(OctetString):
    """Custom type messagei4200fREEROOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200fREEROOTDISKVMIC_Type.__name__ = "OctetString"
_Messagei4200fREEROOTDISKVMIC_Object = MibScalar
messagei4200fREEROOTDISKVMIC = _Messagei4200fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4200, 2),
    _Messagei4200fREEROOTDISKVMIC_Type()
)
messagei4200fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200fREEROOTDISKVMIC.setStatus("mandatory")


class _Valuei4200fREEROOTDISKVMIC_Type(Integer32):
    """Custom type valuei4200fREEROOTDISKVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200fREEROOTDISKVMIC_Type.__name__ = "Integer32"
_Valuei4200fREEROOTDISKVMIC_Object = MibScalar
valuei4200fREEROOTDISKVMIC = _Valuei4200fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4200, 3),
    _Valuei4200fREEROOTDISKVMIC_Type()
)
valuei4200fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200fREEROOTDISKVMIC.setStatus("mandatory")
_I4300fREEROOTDISKVMIC_ObjectIdentity = ObjectIdentity
i4300fREEROOTDISKVMIC = _I4300fREEROOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4300)
)


class _Severityi4300fREEROOTDISKVMIC_Type(OctetString):
    """Custom type severityi4300fREEROOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300fREEROOTDISKVMIC_Type.__name__ = "OctetString"
_Severityi4300fREEROOTDISKVMIC_Object = MibScalar
severityi4300fREEROOTDISKVMIC = _Severityi4300fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4300, 1),
    _Severityi4300fREEROOTDISKVMIC_Type()
)
severityi4300fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300fREEROOTDISKVMIC.setStatus("mandatory")


class _Messagei4300fREEROOTDISKVMIC_Type(OctetString):
    """Custom type messagei4300fREEROOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300fREEROOTDISKVMIC_Type.__name__ = "OctetString"
_Messagei4300fREEROOTDISKVMIC_Object = MibScalar
messagei4300fREEROOTDISKVMIC = _Messagei4300fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4300, 2),
    _Messagei4300fREEROOTDISKVMIC_Type()
)
messagei4300fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300fREEROOTDISKVMIC.setStatus("mandatory")


class _Valuei4300fREEROOTDISKVMIC_Type(Integer32):
    """Custom type valuei4300fREEROOTDISKVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300fREEROOTDISKVMIC_Type.__name__ = "Integer32"
_Valuei4300fREEROOTDISKVMIC_Object = MibScalar
valuei4300fREEROOTDISKVMIC = _Valuei4300fREEROOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4300, 3),
    _Valuei4300fREEROOTDISKVMIC_Type()
)
valuei4300fREEROOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300fREEROOTDISKVMIC.setStatus("mandatory")
_FREEBOOTDISKVMIC_ObjectIdentity = ObjectIdentity
fREEBOOTDISKVMIC = _FREEBOOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2)
)
_I4100fREEBOOTDISKVMIC_ObjectIdentity = ObjectIdentity
i4100fREEBOOTDISKVMIC = _I4100fREEBOOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4100)
)


class _Severityi4100fREEBOOTDISKVMIC_Type(OctetString):
    """Custom type severityi4100fREEBOOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100fREEBOOTDISKVMIC_Type.__name__ = "OctetString"
_Severityi4100fREEBOOTDISKVMIC_Object = MibScalar
severityi4100fREEBOOTDISKVMIC = _Severityi4100fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4100, 1),
    _Severityi4100fREEBOOTDISKVMIC_Type()
)
severityi4100fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100fREEBOOTDISKVMIC.setStatus("mandatory")


class _Messagei4100fREEBOOTDISKVMIC_Type(OctetString):
    """Custom type messagei4100fREEBOOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100fREEBOOTDISKVMIC_Type.__name__ = "OctetString"
_Messagei4100fREEBOOTDISKVMIC_Object = MibScalar
messagei4100fREEBOOTDISKVMIC = _Messagei4100fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4100, 2),
    _Messagei4100fREEBOOTDISKVMIC_Type()
)
messagei4100fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100fREEBOOTDISKVMIC.setStatus("mandatory")


class _Valuei4100fREEBOOTDISKVMIC_Type(Integer32):
    """Custom type valuei4100fREEBOOTDISKVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100fREEBOOTDISKVMIC_Type.__name__ = "Integer32"
_Valuei4100fREEBOOTDISKVMIC_Object = MibScalar
valuei4100fREEBOOTDISKVMIC = _Valuei4100fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4100, 3),
    _Valuei4100fREEBOOTDISKVMIC_Type()
)
valuei4100fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100fREEBOOTDISKVMIC.setStatus("mandatory")
_I4200fREEBOOTDISKVMIC_ObjectIdentity = ObjectIdentity
i4200fREEBOOTDISKVMIC = _I4200fREEBOOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4200)
)


class _Severityi4200fREEBOOTDISKVMIC_Type(OctetString):
    """Custom type severityi4200fREEBOOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200fREEBOOTDISKVMIC_Type.__name__ = "OctetString"
_Severityi4200fREEBOOTDISKVMIC_Object = MibScalar
severityi4200fREEBOOTDISKVMIC = _Severityi4200fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4200, 1),
    _Severityi4200fREEBOOTDISKVMIC_Type()
)
severityi4200fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200fREEBOOTDISKVMIC.setStatus("mandatory")


class _Messagei4200fREEBOOTDISKVMIC_Type(OctetString):
    """Custom type messagei4200fREEBOOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200fREEBOOTDISKVMIC_Type.__name__ = "OctetString"
_Messagei4200fREEBOOTDISKVMIC_Object = MibScalar
messagei4200fREEBOOTDISKVMIC = _Messagei4200fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4200, 2),
    _Messagei4200fREEBOOTDISKVMIC_Type()
)
messagei4200fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200fREEBOOTDISKVMIC.setStatus("mandatory")


class _Valuei4200fREEBOOTDISKVMIC_Type(Integer32):
    """Custom type valuei4200fREEBOOTDISKVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200fREEBOOTDISKVMIC_Type.__name__ = "Integer32"
_Valuei4200fREEBOOTDISKVMIC_Object = MibScalar
valuei4200fREEBOOTDISKVMIC = _Valuei4200fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4200, 3),
    _Valuei4200fREEBOOTDISKVMIC_Type()
)
valuei4200fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200fREEBOOTDISKVMIC.setStatus("mandatory")
_I4300fREEBOOTDISKVMIC_ObjectIdentity = ObjectIdentity
i4300fREEBOOTDISKVMIC = _I4300fREEBOOTDISKVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4300)
)


class _Severityi4300fREEBOOTDISKVMIC_Type(OctetString):
    """Custom type severityi4300fREEBOOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300fREEBOOTDISKVMIC_Type.__name__ = "OctetString"
_Severityi4300fREEBOOTDISKVMIC_Object = MibScalar
severityi4300fREEBOOTDISKVMIC = _Severityi4300fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4300, 1),
    _Severityi4300fREEBOOTDISKVMIC_Type()
)
severityi4300fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300fREEBOOTDISKVMIC.setStatus("mandatory")


class _Messagei4300fREEBOOTDISKVMIC_Type(OctetString):
    """Custom type messagei4300fREEBOOTDISKVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300fREEBOOTDISKVMIC_Type.__name__ = "OctetString"
_Messagei4300fREEBOOTDISKVMIC_Object = MibScalar
messagei4300fREEBOOTDISKVMIC = _Messagei4300fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4300, 2),
    _Messagei4300fREEBOOTDISKVMIC_Type()
)
messagei4300fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300fREEBOOTDISKVMIC.setStatus("mandatory")


class _Valuei4300fREEBOOTDISKVMIC_Type(Integer32):
    """Custom type valuei4300fREEBOOTDISKVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300fREEBOOTDISKVMIC_Type.__name__ = "Integer32"
_Valuei4300fREEBOOTDISKVMIC_Object = MibScalar
valuei4300fREEBOOTDISKVMIC = _Valuei4300fREEBOOTDISKVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4300, 3),
    _Valuei4300fREEBOOTDISKVMIC_Type()
)
valuei4300fREEBOOTDISKVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300fREEBOOTDISKVMIC.setStatus("mandatory")
_FREEMEMORYVMIC_ObjectIdentity = ObjectIdentity
fREEMEMORYVMIC = _FREEMEMORYVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3)
)
_I4100fREEMEMORYVMIC_ObjectIdentity = ObjectIdentity
i4100fREEMEMORYVMIC = _I4100fREEMEMORYVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4100)
)


class _Severityi4100fREEMEMORYVMIC_Type(OctetString):
    """Custom type severityi4100fREEMEMORYVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100fREEMEMORYVMIC_Type.__name__ = "OctetString"
_Severityi4100fREEMEMORYVMIC_Object = MibScalar
severityi4100fREEMEMORYVMIC = _Severityi4100fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4100, 1),
    _Severityi4100fREEMEMORYVMIC_Type()
)
severityi4100fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100fREEMEMORYVMIC.setStatus("mandatory")


class _Messagei4100fREEMEMORYVMIC_Type(OctetString):
    """Custom type messagei4100fREEMEMORYVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100fREEMEMORYVMIC_Type.__name__ = "OctetString"
_Messagei4100fREEMEMORYVMIC_Object = MibScalar
messagei4100fREEMEMORYVMIC = _Messagei4100fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4100, 2),
    _Messagei4100fREEMEMORYVMIC_Type()
)
messagei4100fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100fREEMEMORYVMIC.setStatus("mandatory")


class _Valuei4100fREEMEMORYVMIC_Type(Integer32):
    """Custom type valuei4100fREEMEMORYVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100fREEMEMORYVMIC_Type.__name__ = "Integer32"
_Valuei4100fREEMEMORYVMIC_Object = MibScalar
valuei4100fREEMEMORYVMIC = _Valuei4100fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4100, 3),
    _Valuei4100fREEMEMORYVMIC_Type()
)
valuei4100fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100fREEMEMORYVMIC.setStatus("mandatory")
_I4200fREEMEMORYVMIC_ObjectIdentity = ObjectIdentity
i4200fREEMEMORYVMIC = _I4200fREEMEMORYVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4200)
)


class _Severityi4200fREEMEMORYVMIC_Type(OctetString):
    """Custom type severityi4200fREEMEMORYVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200fREEMEMORYVMIC_Type.__name__ = "OctetString"
_Severityi4200fREEMEMORYVMIC_Object = MibScalar
severityi4200fREEMEMORYVMIC = _Severityi4200fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4200, 1),
    _Severityi4200fREEMEMORYVMIC_Type()
)
severityi4200fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200fREEMEMORYVMIC.setStatus("mandatory")


class _Messagei4200fREEMEMORYVMIC_Type(OctetString):
    """Custom type messagei4200fREEMEMORYVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200fREEMEMORYVMIC_Type.__name__ = "OctetString"
_Messagei4200fREEMEMORYVMIC_Object = MibScalar
messagei4200fREEMEMORYVMIC = _Messagei4200fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4200, 2),
    _Messagei4200fREEMEMORYVMIC_Type()
)
messagei4200fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200fREEMEMORYVMIC.setStatus("mandatory")


class _Valuei4200fREEMEMORYVMIC_Type(Integer32):
    """Custom type valuei4200fREEMEMORYVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200fREEMEMORYVMIC_Type.__name__ = "Integer32"
_Valuei4200fREEMEMORYVMIC_Object = MibScalar
valuei4200fREEMEMORYVMIC = _Valuei4200fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4200, 3),
    _Valuei4200fREEMEMORYVMIC_Type()
)
valuei4200fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200fREEMEMORYVMIC.setStatus("mandatory")
_I4300fREEMEMORYVMIC_ObjectIdentity = ObjectIdentity
i4300fREEMEMORYVMIC = _I4300fREEMEMORYVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4300)
)


class _Severityi4300fREEMEMORYVMIC_Type(OctetString):
    """Custom type severityi4300fREEMEMORYVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300fREEMEMORYVMIC_Type.__name__ = "OctetString"
_Severityi4300fREEMEMORYVMIC_Object = MibScalar
severityi4300fREEMEMORYVMIC = _Severityi4300fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4300, 1),
    _Severityi4300fREEMEMORYVMIC_Type()
)
severityi4300fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300fREEMEMORYVMIC.setStatus("mandatory")


class _Messagei4300fREEMEMORYVMIC_Type(OctetString):
    """Custom type messagei4300fREEMEMORYVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300fREEMEMORYVMIC_Type.__name__ = "OctetString"
_Messagei4300fREEMEMORYVMIC_Object = MibScalar
messagei4300fREEMEMORYVMIC = _Messagei4300fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4300, 2),
    _Messagei4300fREEMEMORYVMIC_Type()
)
messagei4300fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300fREEMEMORYVMIC.setStatus("mandatory")


class _Valuei4300fREEMEMORYVMIC_Type(Integer32):
    """Custom type valuei4300fREEMEMORYVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300fREEMEMORYVMIC_Type.__name__ = "Integer32"
_Valuei4300fREEMEMORYVMIC_Object = MibScalar
valuei4300fREEMEMORYVMIC = _Valuei4300fREEMEMORYVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4300, 3),
    _Valuei4300fREEMEMORYVMIC_Type()
)
valuei4300fREEMEMORYVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300fREEMEMORYVMIC.setStatus("mandatory")
_CPULOADVMIC_ObjectIdentity = ObjectIdentity
cPULOADVMIC = _CPULOADVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4)
)
_I4100cPULOADVMIC_ObjectIdentity = ObjectIdentity
i4100cPULOADVMIC = _I4100cPULOADVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4100)
)


class _Severityi4100cPULOADVMIC_Type(OctetString):
    """Custom type severityi4100cPULOADVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100cPULOADVMIC_Type.__name__ = "OctetString"
_Severityi4100cPULOADVMIC_Object = MibScalar
severityi4100cPULOADVMIC = _Severityi4100cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4100, 1),
    _Severityi4100cPULOADVMIC_Type()
)
severityi4100cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100cPULOADVMIC.setStatus("mandatory")


class _Messagei4100cPULOADVMIC_Type(OctetString):
    """Custom type messagei4100cPULOADVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100cPULOADVMIC_Type.__name__ = "OctetString"
_Messagei4100cPULOADVMIC_Object = MibScalar
messagei4100cPULOADVMIC = _Messagei4100cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4100, 2),
    _Messagei4100cPULOADVMIC_Type()
)
messagei4100cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100cPULOADVMIC.setStatus("mandatory")


class _Valuei4100cPULOADVMIC_Type(Integer32):
    """Custom type valuei4100cPULOADVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100cPULOADVMIC_Type.__name__ = "Integer32"
_Valuei4100cPULOADVMIC_Object = MibScalar
valuei4100cPULOADVMIC = _Valuei4100cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4100, 3),
    _Valuei4100cPULOADVMIC_Type()
)
valuei4100cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100cPULOADVMIC.setStatus("mandatory")
_I4200cPULOADVMIC_ObjectIdentity = ObjectIdentity
i4200cPULOADVMIC = _I4200cPULOADVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4200)
)


class _Severityi4200cPULOADVMIC_Type(OctetString):
    """Custom type severityi4200cPULOADVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200cPULOADVMIC_Type.__name__ = "OctetString"
_Severityi4200cPULOADVMIC_Object = MibScalar
severityi4200cPULOADVMIC = _Severityi4200cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4200, 1),
    _Severityi4200cPULOADVMIC_Type()
)
severityi4200cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200cPULOADVMIC.setStatus("mandatory")


class _Messagei4200cPULOADVMIC_Type(OctetString):
    """Custom type messagei4200cPULOADVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200cPULOADVMIC_Type.__name__ = "OctetString"
_Messagei4200cPULOADVMIC_Object = MibScalar
messagei4200cPULOADVMIC = _Messagei4200cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4200, 2),
    _Messagei4200cPULOADVMIC_Type()
)
messagei4200cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200cPULOADVMIC.setStatus("mandatory")


class _Valuei4200cPULOADVMIC_Type(Integer32):
    """Custom type valuei4200cPULOADVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200cPULOADVMIC_Type.__name__ = "Integer32"
_Valuei4200cPULOADVMIC_Object = MibScalar
valuei4200cPULOADVMIC = _Valuei4200cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4200, 3),
    _Valuei4200cPULOADVMIC_Type()
)
valuei4200cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200cPULOADVMIC.setStatus("mandatory")
_I4300cPULOADVMIC_ObjectIdentity = ObjectIdentity
i4300cPULOADVMIC = _I4300cPULOADVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4300)
)


class _Severityi4300cPULOADVMIC_Type(OctetString):
    """Custom type severityi4300cPULOADVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300cPULOADVMIC_Type.__name__ = "OctetString"
_Severityi4300cPULOADVMIC_Object = MibScalar
severityi4300cPULOADVMIC = _Severityi4300cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4300, 1),
    _Severityi4300cPULOADVMIC_Type()
)
severityi4300cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300cPULOADVMIC.setStatus("mandatory")


class _Messagei4300cPULOADVMIC_Type(OctetString):
    """Custom type messagei4300cPULOADVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300cPULOADVMIC_Type.__name__ = "OctetString"
_Messagei4300cPULOADVMIC_Object = MibScalar
messagei4300cPULOADVMIC = _Messagei4300cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4300, 2),
    _Messagei4300cPULOADVMIC_Type()
)
messagei4300cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300cPULOADVMIC.setStatus("mandatory")


class _Valuei4300cPULOADVMIC_Type(Integer32):
    """Custom type valuei4300cPULOADVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300cPULOADVMIC_Type.__name__ = "Integer32"
_Valuei4300cPULOADVMIC_Object = MibScalar
valuei4300cPULOADVMIC = _Valuei4300cPULOADVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4300, 3),
    _Valuei4300cPULOADVMIC_Type()
)
valuei4300cPULOADVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300cPULOADVMIC.setStatus("mandatory")
_FREESWAPVMIC_ObjectIdentity = ObjectIdentity
fREESWAPVMIC = _FREESWAPVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5)
)
_I4100fREESWAPVMIC_ObjectIdentity = ObjectIdentity
i4100fREESWAPVMIC = _I4100fREESWAPVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4100)
)


class _Severityi4100fREESWAPVMIC_Type(OctetString):
    """Custom type severityi4100fREESWAPVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100fREESWAPVMIC_Type.__name__ = "OctetString"
_Severityi4100fREESWAPVMIC_Object = MibScalar
severityi4100fREESWAPVMIC = _Severityi4100fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4100, 1),
    _Severityi4100fREESWAPVMIC_Type()
)
severityi4100fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100fREESWAPVMIC.setStatus("mandatory")


class _Messagei4100fREESWAPVMIC_Type(OctetString):
    """Custom type messagei4100fREESWAPVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100fREESWAPVMIC_Type.__name__ = "OctetString"
_Messagei4100fREESWAPVMIC_Object = MibScalar
messagei4100fREESWAPVMIC = _Messagei4100fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4100, 2),
    _Messagei4100fREESWAPVMIC_Type()
)
messagei4100fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100fREESWAPVMIC.setStatus("mandatory")


class _Valuei4100fREESWAPVMIC_Type(Integer32):
    """Custom type valuei4100fREESWAPVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100fREESWAPVMIC_Type.__name__ = "Integer32"
_Valuei4100fREESWAPVMIC_Object = MibScalar
valuei4100fREESWAPVMIC = _Valuei4100fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4100, 3),
    _Valuei4100fREESWAPVMIC_Type()
)
valuei4100fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100fREESWAPVMIC.setStatus("mandatory")
_I4200fREESWAPVMIC_ObjectIdentity = ObjectIdentity
i4200fREESWAPVMIC = _I4200fREESWAPVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4200)
)


class _Severityi4200fREESWAPVMIC_Type(OctetString):
    """Custom type severityi4200fREESWAPVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200fREESWAPVMIC_Type.__name__ = "OctetString"
_Severityi4200fREESWAPVMIC_Object = MibScalar
severityi4200fREESWAPVMIC = _Severityi4200fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4200, 1),
    _Severityi4200fREESWAPVMIC_Type()
)
severityi4200fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200fREESWAPVMIC.setStatus("mandatory")


class _Messagei4200fREESWAPVMIC_Type(OctetString):
    """Custom type messagei4200fREESWAPVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200fREESWAPVMIC_Type.__name__ = "OctetString"
_Messagei4200fREESWAPVMIC_Object = MibScalar
messagei4200fREESWAPVMIC = _Messagei4200fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4200, 2),
    _Messagei4200fREESWAPVMIC_Type()
)
messagei4200fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200fREESWAPVMIC.setStatus("mandatory")


class _Valuei4200fREESWAPVMIC_Type(Integer32):
    """Custom type valuei4200fREESWAPVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200fREESWAPVMIC_Type.__name__ = "Integer32"
_Valuei4200fREESWAPVMIC_Object = MibScalar
valuei4200fREESWAPVMIC = _Valuei4200fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4200, 3),
    _Valuei4200fREESWAPVMIC_Type()
)
valuei4200fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200fREESWAPVMIC.setStatus("mandatory")
_I4300fREESWAPVMIC_ObjectIdentity = ObjectIdentity
i4300fREESWAPVMIC = _I4300fREESWAPVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4300)
)


class _Severityi4300fREESWAPVMIC_Type(OctetString):
    """Custom type severityi4300fREESWAPVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300fREESWAPVMIC_Type.__name__ = "OctetString"
_Severityi4300fREESWAPVMIC_Object = MibScalar
severityi4300fREESWAPVMIC = _Severityi4300fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4300, 1),
    _Severityi4300fREESWAPVMIC_Type()
)
severityi4300fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300fREESWAPVMIC.setStatus("mandatory")


class _Messagei4300fREESWAPVMIC_Type(OctetString):
    """Custom type messagei4300fREESWAPVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300fREESWAPVMIC_Type.__name__ = "OctetString"
_Messagei4300fREESWAPVMIC_Object = MibScalar
messagei4300fREESWAPVMIC = _Messagei4300fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4300, 2),
    _Messagei4300fREESWAPVMIC_Type()
)
messagei4300fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300fREESWAPVMIC.setStatus("mandatory")


class _Valuei4300fREESWAPVMIC_Type(Integer32):
    """Custom type valuei4300fREESWAPVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300fREESWAPVMIC_Type.__name__ = "Integer32"
_Valuei4300fREESWAPVMIC_Object = MibScalar
valuei4300fREESWAPVMIC = _Valuei4300fREESWAPVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4300, 3),
    _Valuei4300fREESWAPVMIC_Type()
)
valuei4300fREESWAPVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300fREESWAPVMIC.setStatus("mandatory")
_ETHINTSTATUSVMIC_ObjectIdentity = ObjectIdentity
eTHINTSTATUSVMIC = _ETHINTSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6)
)
_I4100eTHINTSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4100eTHINTSTATUSVMIC = _I4100eTHINTSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4100)
)


class _Severityi4100eTHINTSTATUSVMIC_Type(OctetString):
    """Custom type severityi4100eTHINTSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100eTHINTSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4100eTHINTSTATUSVMIC_Object = MibScalar
severityi4100eTHINTSTATUSVMIC = _Severityi4100eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4100, 1),
    _Severityi4100eTHINTSTATUSVMIC_Type()
)
severityi4100eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100eTHINTSTATUSVMIC.setStatus("mandatory")


class _Messagei4100eTHINTSTATUSVMIC_Type(OctetString):
    """Custom type messagei4100eTHINTSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100eTHINTSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4100eTHINTSTATUSVMIC_Object = MibScalar
messagei4100eTHINTSTATUSVMIC = _Messagei4100eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4100, 2),
    _Messagei4100eTHINTSTATUSVMIC_Type()
)
messagei4100eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100eTHINTSTATUSVMIC.setStatus("mandatory")


class _Valuei4100eTHINTSTATUSVMIC_Type(Integer32):
    """Custom type valuei4100eTHINTSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100eTHINTSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4100eTHINTSTATUSVMIC_Object = MibScalar
valuei4100eTHINTSTATUSVMIC = _Valuei4100eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4100, 3),
    _Valuei4100eTHINTSTATUSVMIC_Type()
)
valuei4100eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100eTHINTSTATUSVMIC.setStatus("mandatory")
_I4200eTHINTSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4200eTHINTSTATUSVMIC = _I4200eTHINTSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4200)
)


class _Severityi4200eTHINTSTATUSVMIC_Type(OctetString):
    """Custom type severityi4200eTHINTSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200eTHINTSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4200eTHINTSTATUSVMIC_Object = MibScalar
severityi4200eTHINTSTATUSVMIC = _Severityi4200eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4200, 1),
    _Severityi4200eTHINTSTATUSVMIC_Type()
)
severityi4200eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200eTHINTSTATUSVMIC.setStatus("mandatory")


class _Messagei4200eTHINTSTATUSVMIC_Type(OctetString):
    """Custom type messagei4200eTHINTSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200eTHINTSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4200eTHINTSTATUSVMIC_Object = MibScalar
messagei4200eTHINTSTATUSVMIC = _Messagei4200eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4200, 2),
    _Messagei4200eTHINTSTATUSVMIC_Type()
)
messagei4200eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200eTHINTSTATUSVMIC.setStatus("mandatory")


class _Valuei4200eTHINTSTATUSVMIC_Type(Integer32):
    """Custom type valuei4200eTHINTSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200eTHINTSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4200eTHINTSTATUSVMIC_Object = MibScalar
valuei4200eTHINTSTATUSVMIC = _Valuei4200eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4200, 3),
    _Valuei4200eTHINTSTATUSVMIC_Type()
)
valuei4200eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200eTHINTSTATUSVMIC.setStatus("mandatory")
_I4300eTHINTSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4300eTHINTSTATUSVMIC = _I4300eTHINTSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4300)
)


class _Severityi4300eTHINTSTATUSVMIC_Type(OctetString):
    """Custom type severityi4300eTHINTSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300eTHINTSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4300eTHINTSTATUSVMIC_Object = MibScalar
severityi4300eTHINTSTATUSVMIC = _Severityi4300eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4300, 1),
    _Severityi4300eTHINTSTATUSVMIC_Type()
)
severityi4300eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300eTHINTSTATUSVMIC.setStatus("mandatory")


class _Messagei4300eTHINTSTATUSVMIC_Type(OctetString):
    """Custom type messagei4300eTHINTSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300eTHINTSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4300eTHINTSTATUSVMIC_Object = MibScalar
messagei4300eTHINTSTATUSVMIC = _Messagei4300eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4300, 2),
    _Messagei4300eTHINTSTATUSVMIC_Type()
)
messagei4300eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300eTHINTSTATUSVMIC.setStatus("mandatory")


class _Valuei4300eTHINTSTATUSVMIC_Type(Integer32):
    """Custom type valuei4300eTHINTSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300eTHINTSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4300eTHINTSTATUSVMIC_Object = MibScalar
valuei4300eTHINTSTATUSVMIC = _Valuei4300eTHINTSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4300, 3),
    _Valuei4300eTHINTSTATUSVMIC_Type()
)
valuei4300eTHINTSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300eTHINTSTATUSVMIC.setStatus("mandatory")
_CRONSTATUSVMIC_ObjectIdentity = ObjectIdentity
cRONSTATUSVMIC = _CRONSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7)
)
_I4100cRONSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4100cRONSTATUSVMIC = _I4100cRONSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4100)
)


class _Severityi4100cRONSTATUSVMIC_Type(OctetString):
    """Custom type severityi4100cRONSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100cRONSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4100cRONSTATUSVMIC_Object = MibScalar
severityi4100cRONSTATUSVMIC = _Severityi4100cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4100, 1),
    _Severityi4100cRONSTATUSVMIC_Type()
)
severityi4100cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100cRONSTATUSVMIC.setStatus("mandatory")


class _Messagei4100cRONSTATUSVMIC_Type(OctetString):
    """Custom type messagei4100cRONSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100cRONSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4100cRONSTATUSVMIC_Object = MibScalar
messagei4100cRONSTATUSVMIC = _Messagei4100cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4100, 2),
    _Messagei4100cRONSTATUSVMIC_Type()
)
messagei4100cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100cRONSTATUSVMIC.setStatus("mandatory")


class _Valuei4100cRONSTATUSVMIC_Type(Integer32):
    """Custom type valuei4100cRONSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100cRONSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4100cRONSTATUSVMIC_Object = MibScalar
valuei4100cRONSTATUSVMIC = _Valuei4100cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4100, 3),
    _Valuei4100cRONSTATUSVMIC_Type()
)
valuei4100cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100cRONSTATUSVMIC.setStatus("mandatory")
_I4200cRONSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4200cRONSTATUSVMIC = _I4200cRONSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4200)
)


class _Severityi4200cRONSTATUSVMIC_Type(OctetString):
    """Custom type severityi4200cRONSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200cRONSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4200cRONSTATUSVMIC_Object = MibScalar
severityi4200cRONSTATUSVMIC = _Severityi4200cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4200, 1),
    _Severityi4200cRONSTATUSVMIC_Type()
)
severityi4200cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200cRONSTATUSVMIC.setStatus("mandatory")


class _Messagei4200cRONSTATUSVMIC_Type(OctetString):
    """Custom type messagei4200cRONSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200cRONSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4200cRONSTATUSVMIC_Object = MibScalar
messagei4200cRONSTATUSVMIC = _Messagei4200cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4200, 2),
    _Messagei4200cRONSTATUSVMIC_Type()
)
messagei4200cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200cRONSTATUSVMIC.setStatus("mandatory")


class _Valuei4200cRONSTATUSVMIC_Type(Integer32):
    """Custom type valuei4200cRONSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200cRONSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4200cRONSTATUSVMIC_Object = MibScalar
valuei4200cRONSTATUSVMIC = _Valuei4200cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4200, 3),
    _Valuei4200cRONSTATUSVMIC_Type()
)
valuei4200cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200cRONSTATUSVMIC.setStatus("mandatory")
_I4300cRONSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4300cRONSTATUSVMIC = _I4300cRONSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4300)
)


class _Severityi4300cRONSTATUSVMIC_Type(OctetString):
    """Custom type severityi4300cRONSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300cRONSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4300cRONSTATUSVMIC_Object = MibScalar
severityi4300cRONSTATUSVMIC = _Severityi4300cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4300, 1),
    _Severityi4300cRONSTATUSVMIC_Type()
)
severityi4300cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300cRONSTATUSVMIC.setStatus("mandatory")


class _Messagei4300cRONSTATUSVMIC_Type(OctetString):
    """Custom type messagei4300cRONSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300cRONSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4300cRONSTATUSVMIC_Object = MibScalar
messagei4300cRONSTATUSVMIC = _Messagei4300cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4300, 2),
    _Messagei4300cRONSTATUSVMIC_Type()
)
messagei4300cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300cRONSTATUSVMIC.setStatus("mandatory")


class _Valuei4300cRONSTATUSVMIC_Type(Integer32):
    """Custom type valuei4300cRONSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300cRONSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4300cRONSTATUSVMIC_Object = MibScalar
valuei4300cRONSTATUSVMIC = _Valuei4300cRONSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4300, 3),
    _Valuei4300cRONSTATUSVMIC_Type()
)
valuei4300cRONSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300cRONSTATUSVMIC.setStatus("mandatory")
_MONITSTATUSVMIC_ObjectIdentity = ObjectIdentity
mONITSTATUSVMIC = _MONITSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8)
)
_I4100mONITSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4100mONITSTATUSVMIC = _I4100mONITSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4100)
)


class _Severityi4100mONITSTATUSVMIC_Type(OctetString):
    """Custom type severityi4100mONITSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100mONITSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4100mONITSTATUSVMIC_Object = MibScalar
severityi4100mONITSTATUSVMIC = _Severityi4100mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4100, 1),
    _Severityi4100mONITSTATUSVMIC_Type()
)
severityi4100mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100mONITSTATUSVMIC.setStatus("mandatory")


class _Messagei4100mONITSTATUSVMIC_Type(OctetString):
    """Custom type messagei4100mONITSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100mONITSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4100mONITSTATUSVMIC_Object = MibScalar
messagei4100mONITSTATUSVMIC = _Messagei4100mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4100, 2),
    _Messagei4100mONITSTATUSVMIC_Type()
)
messagei4100mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100mONITSTATUSVMIC.setStatus("mandatory")


class _Valuei4100mONITSTATUSVMIC_Type(Integer32):
    """Custom type valuei4100mONITSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100mONITSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4100mONITSTATUSVMIC_Object = MibScalar
valuei4100mONITSTATUSVMIC = _Valuei4100mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4100, 3),
    _Valuei4100mONITSTATUSVMIC_Type()
)
valuei4100mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100mONITSTATUSVMIC.setStatus("mandatory")
_I4200mONITSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4200mONITSTATUSVMIC = _I4200mONITSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4200)
)


class _Severityi4200mONITSTATUSVMIC_Type(OctetString):
    """Custom type severityi4200mONITSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200mONITSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4200mONITSTATUSVMIC_Object = MibScalar
severityi4200mONITSTATUSVMIC = _Severityi4200mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4200, 1),
    _Severityi4200mONITSTATUSVMIC_Type()
)
severityi4200mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200mONITSTATUSVMIC.setStatus("mandatory")


class _Messagei4200mONITSTATUSVMIC_Type(OctetString):
    """Custom type messagei4200mONITSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200mONITSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4200mONITSTATUSVMIC_Object = MibScalar
messagei4200mONITSTATUSVMIC = _Messagei4200mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4200, 2),
    _Messagei4200mONITSTATUSVMIC_Type()
)
messagei4200mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200mONITSTATUSVMIC.setStatus("mandatory")


class _Valuei4200mONITSTATUSVMIC_Type(Integer32):
    """Custom type valuei4200mONITSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200mONITSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4200mONITSTATUSVMIC_Object = MibScalar
valuei4200mONITSTATUSVMIC = _Valuei4200mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4200, 3),
    _Valuei4200mONITSTATUSVMIC_Type()
)
valuei4200mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200mONITSTATUSVMIC.setStatus("mandatory")
_I4300mONITSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4300mONITSTATUSVMIC = _I4300mONITSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4300)
)


class _Severityi4300mONITSTATUSVMIC_Type(OctetString):
    """Custom type severityi4300mONITSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300mONITSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4300mONITSTATUSVMIC_Object = MibScalar
severityi4300mONITSTATUSVMIC = _Severityi4300mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4300, 1),
    _Severityi4300mONITSTATUSVMIC_Type()
)
severityi4300mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300mONITSTATUSVMIC.setStatus("mandatory")


class _Messagei4300mONITSTATUSVMIC_Type(OctetString):
    """Custom type messagei4300mONITSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300mONITSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4300mONITSTATUSVMIC_Object = MibScalar
messagei4300mONITSTATUSVMIC = _Messagei4300mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4300, 2),
    _Messagei4300mONITSTATUSVMIC_Type()
)
messagei4300mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300mONITSTATUSVMIC.setStatus("mandatory")


class _Valuei4300mONITSTATUSVMIC_Type(Integer32):
    """Custom type valuei4300mONITSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300mONITSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4300mONITSTATUSVMIC_Object = MibScalar
valuei4300mONITSTATUSVMIC = _Valuei4300mONITSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4300, 3),
    _Valuei4300mONITSTATUSVMIC_Type()
)
valuei4300mONITSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300mONITSTATUSVMIC.setStatus("mandatory")
_CPUSTATUSVMIC_ObjectIdentity = ObjectIdentity
cPUSTATUSVMIC = _CPUSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18)
)
_I4100cPUSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4100cPUSTATUSVMIC = _I4100cPUSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4100)
)


class _Severityi4100cPUSTATUSVMIC_Type(OctetString):
    """Custom type severityi4100cPUSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100cPUSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4100cPUSTATUSVMIC_Object = MibScalar
severityi4100cPUSTATUSVMIC = _Severityi4100cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4100, 1),
    _Severityi4100cPUSTATUSVMIC_Type()
)
severityi4100cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100cPUSTATUSVMIC.setStatus("mandatory")


class _Messagei4100cPUSTATUSVMIC_Type(OctetString):
    """Custom type messagei4100cPUSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100cPUSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4100cPUSTATUSVMIC_Object = MibScalar
messagei4100cPUSTATUSVMIC = _Messagei4100cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4100, 2),
    _Messagei4100cPUSTATUSVMIC_Type()
)
messagei4100cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100cPUSTATUSVMIC.setStatus("mandatory")


class _Valuei4100cPUSTATUSVMIC_Type(Integer32):
    """Custom type valuei4100cPUSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100cPUSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4100cPUSTATUSVMIC_Object = MibScalar
valuei4100cPUSTATUSVMIC = _Valuei4100cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4100, 3),
    _Valuei4100cPUSTATUSVMIC_Type()
)
valuei4100cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100cPUSTATUSVMIC.setStatus("mandatory")
_I4200cPUSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4200cPUSTATUSVMIC = _I4200cPUSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4200)
)


class _Severityi4200cPUSTATUSVMIC_Type(OctetString):
    """Custom type severityi4200cPUSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200cPUSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4200cPUSTATUSVMIC_Object = MibScalar
severityi4200cPUSTATUSVMIC = _Severityi4200cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4200, 1),
    _Severityi4200cPUSTATUSVMIC_Type()
)
severityi4200cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200cPUSTATUSVMIC.setStatus("mandatory")


class _Messagei4200cPUSTATUSVMIC_Type(OctetString):
    """Custom type messagei4200cPUSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200cPUSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4200cPUSTATUSVMIC_Object = MibScalar
messagei4200cPUSTATUSVMIC = _Messagei4200cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4200, 2),
    _Messagei4200cPUSTATUSVMIC_Type()
)
messagei4200cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200cPUSTATUSVMIC.setStatus("mandatory")


class _Valuei4200cPUSTATUSVMIC_Type(Integer32):
    """Custom type valuei4200cPUSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200cPUSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4200cPUSTATUSVMIC_Object = MibScalar
valuei4200cPUSTATUSVMIC = _Valuei4200cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4200, 3),
    _Valuei4200cPUSTATUSVMIC_Type()
)
valuei4200cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200cPUSTATUSVMIC.setStatus("mandatory")
_I4300cPUSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4300cPUSTATUSVMIC = _I4300cPUSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4300)
)


class _Severityi4300cPUSTATUSVMIC_Type(OctetString):
    """Custom type severityi4300cPUSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300cPUSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4300cPUSTATUSVMIC_Object = MibScalar
severityi4300cPUSTATUSVMIC = _Severityi4300cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4300, 1),
    _Severityi4300cPUSTATUSVMIC_Type()
)
severityi4300cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300cPUSTATUSVMIC.setStatus("mandatory")


class _Messagei4300cPUSTATUSVMIC_Type(OctetString):
    """Custom type messagei4300cPUSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300cPUSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4300cPUSTATUSVMIC_Object = MibScalar
messagei4300cPUSTATUSVMIC = _Messagei4300cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4300, 2),
    _Messagei4300cPUSTATUSVMIC_Type()
)
messagei4300cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300cPUSTATUSVMIC.setStatus("mandatory")


class _Valuei4300cPUSTATUSVMIC_Type(Integer32):
    """Custom type valuei4300cPUSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300cPUSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4300cPUSTATUSVMIC_Object = MibScalar
valuei4300cPUSTATUSVMIC = _Valuei4300cPUSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4300, 3),
    _Valuei4300cPUSTATUSVMIC_Type()
)
valuei4300cPUSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300cPUSTATUSVMIC.setStatus("mandatory")
_VMPANELSTATUSVMIC_ObjectIdentity = ObjectIdentity
vMPANELSTATUSVMIC = _VMPANELSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21)
)
_I4100vMPANELSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4100vMPANELSTATUSVMIC = _I4100vMPANELSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4100)
)


class _Severityi4100vMPANELSTATUSVMIC_Type(OctetString):
    """Custom type severityi4100vMPANELSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4100vMPANELSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4100vMPANELSTATUSVMIC_Object = MibScalar
severityi4100vMPANELSTATUSVMIC = _Severityi4100vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4100, 1),
    _Severityi4100vMPANELSTATUSVMIC_Type()
)
severityi4100vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4100vMPANELSTATUSVMIC.setStatus("mandatory")


class _Messagei4100vMPANELSTATUSVMIC_Type(OctetString):
    """Custom type messagei4100vMPANELSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4100vMPANELSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4100vMPANELSTATUSVMIC_Object = MibScalar
messagei4100vMPANELSTATUSVMIC = _Messagei4100vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4100, 2),
    _Messagei4100vMPANELSTATUSVMIC_Type()
)
messagei4100vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4100vMPANELSTATUSVMIC.setStatus("mandatory")


class _Valuei4100vMPANELSTATUSVMIC_Type(Integer32):
    """Custom type valuei4100vMPANELSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4100vMPANELSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4100vMPANELSTATUSVMIC_Object = MibScalar
valuei4100vMPANELSTATUSVMIC = _Valuei4100vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4100, 3),
    _Valuei4100vMPANELSTATUSVMIC_Type()
)
valuei4100vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4100vMPANELSTATUSVMIC.setStatus("mandatory")
_I4200vMPANELSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4200vMPANELSTATUSVMIC = _I4200vMPANELSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4200)
)


class _Severityi4200vMPANELSTATUSVMIC_Type(OctetString):
    """Custom type severityi4200vMPANELSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4200vMPANELSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4200vMPANELSTATUSVMIC_Object = MibScalar
severityi4200vMPANELSTATUSVMIC = _Severityi4200vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4200, 1),
    _Severityi4200vMPANELSTATUSVMIC_Type()
)
severityi4200vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4200vMPANELSTATUSVMIC.setStatus("mandatory")


class _Messagei4200vMPANELSTATUSVMIC_Type(OctetString):
    """Custom type messagei4200vMPANELSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4200vMPANELSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4200vMPANELSTATUSVMIC_Object = MibScalar
messagei4200vMPANELSTATUSVMIC = _Messagei4200vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4200, 2),
    _Messagei4200vMPANELSTATUSVMIC_Type()
)
messagei4200vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4200vMPANELSTATUSVMIC.setStatus("mandatory")


class _Valuei4200vMPANELSTATUSVMIC_Type(Integer32):
    """Custom type valuei4200vMPANELSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4200vMPANELSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4200vMPANELSTATUSVMIC_Object = MibScalar
valuei4200vMPANELSTATUSVMIC = _Valuei4200vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4200, 3),
    _Valuei4200vMPANELSTATUSVMIC_Type()
)
valuei4200vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4200vMPANELSTATUSVMIC.setStatus("mandatory")
_I4300vMPANELSTATUSVMIC_ObjectIdentity = ObjectIdentity
i4300vMPANELSTATUSVMIC = _I4300vMPANELSTATUSVMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4300)
)


class _Severityi4300vMPANELSTATUSVMIC_Type(OctetString):
    """Custom type severityi4300vMPANELSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi4300vMPANELSTATUSVMIC_Type.__name__ = "OctetString"
_Severityi4300vMPANELSTATUSVMIC_Object = MibScalar
severityi4300vMPANELSTATUSVMIC = _Severityi4300vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4300, 1),
    _Severityi4300vMPANELSTATUSVMIC_Type()
)
severityi4300vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi4300vMPANELSTATUSVMIC.setStatus("mandatory")


class _Messagei4300vMPANELSTATUSVMIC_Type(OctetString):
    """Custom type messagei4300vMPANELSTATUSVMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei4300vMPANELSTATUSVMIC_Type.__name__ = "OctetString"
_Messagei4300vMPANELSTATUSVMIC_Object = MibScalar
messagei4300vMPANELSTATUSVMIC = _Messagei4300vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4300, 2),
    _Messagei4300vMPANELSTATUSVMIC_Type()
)
messagei4300vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei4300vMPANELSTATUSVMIC.setStatus("mandatory")


class _Valuei4300vMPANELSTATUSVMIC_Type(Integer32):
    """Custom type valuei4300vMPANELSTATUSVMIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei4300vMPANELSTATUSVMIC_Type.__name__ = "Integer32"
_Valuei4300vMPANELSTATUSVMIC_Object = MibScalar
valuei4300vMPANELSTATUSVMIC = _Valuei4300vMPANELSTATUSVMIC_Object(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4300, 3),
    _Valuei4300vMPANELSTATUSVMIC_Type()
)
valuei4300vMPANELSTATUSVMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei4300vMPANELSTATUSVMIC.setStatus("mandatory")
_Vmlvs_ObjectIdentity = ObjectIdentity
vmlvs = _Vmlvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105)
)
_FREEROOTDISKVMLVS_ObjectIdentity = ObjectIdentity
fREEROOTDISKVMLVS = _FREEROOTDISKVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1)
)
_I5100fREEROOTDISKVMLVS_ObjectIdentity = ObjectIdentity
i5100fREEROOTDISKVMLVS = _I5100fREEROOTDISKVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5100)
)


class _Severityi5100fREEROOTDISKVMLVS_Type(OctetString):
    """Custom type severityi5100fREEROOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100fREEROOTDISKVMLVS_Type.__name__ = "OctetString"
_Severityi5100fREEROOTDISKVMLVS_Object = MibScalar
severityi5100fREEROOTDISKVMLVS = _Severityi5100fREEROOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5100, 1),
    _Severityi5100fREEROOTDISKVMLVS_Type()
)
severityi5100fREEROOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100fREEROOTDISKVMLVS.setStatus("mandatory")


class _Messagei5100fREEROOTDISKVMLVS_Type(OctetString):
    """Custom type messagei5100fREEROOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100fREEROOTDISKVMLVS_Type.__name__ = "OctetString"
_Messagei5100fREEROOTDISKVMLVS_Object = MibScalar
messagei5100fREEROOTDISKVMLVS = _Messagei5100fREEROOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5100, 2),
    _Messagei5100fREEROOTDISKVMLVS_Type()
)
messagei5100fREEROOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100fREEROOTDISKVMLVS.setStatus("mandatory")


class _Valuei5100fREEROOTDISKVMLVS_Type(Integer32):
    """Custom type valuei5100fREEROOTDISKVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100fREEROOTDISKVMLVS_Type.__name__ = "Integer32"
_Valuei5100fREEROOTDISKVMLVS_Object = MibScalar
valuei5100fREEROOTDISKVMLVS = _Valuei5100fREEROOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5100, 3),
    _Valuei5100fREEROOTDISKVMLVS_Type()
)
valuei5100fREEROOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100fREEROOTDISKVMLVS.setStatus("mandatory")
_I5200fREEROOTDISKVMLVS_ObjectIdentity = ObjectIdentity
i5200fREEROOTDISKVMLVS = _I5200fREEROOTDISKVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5200)
)


class _Severityi5200fREEROOTDISKVMLVS_Type(OctetString):
    """Custom type severityi5200fREEROOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200fREEROOTDISKVMLVS_Type.__name__ = "OctetString"
_Severityi5200fREEROOTDISKVMLVS_Object = MibScalar
severityi5200fREEROOTDISKVMLVS = _Severityi5200fREEROOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5200, 1),
    _Severityi5200fREEROOTDISKVMLVS_Type()
)
severityi5200fREEROOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200fREEROOTDISKVMLVS.setStatus("mandatory")


class _Messagei5200fREEROOTDISKVMLVS_Type(OctetString):
    """Custom type messagei5200fREEROOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200fREEROOTDISKVMLVS_Type.__name__ = "OctetString"
_Messagei5200fREEROOTDISKVMLVS_Object = MibScalar
messagei5200fREEROOTDISKVMLVS = _Messagei5200fREEROOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5200, 2),
    _Messagei5200fREEROOTDISKVMLVS_Type()
)
messagei5200fREEROOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200fREEROOTDISKVMLVS.setStatus("mandatory")


class _Valuei5200fREEROOTDISKVMLVS_Type(Integer32):
    """Custom type valuei5200fREEROOTDISKVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200fREEROOTDISKVMLVS_Type.__name__ = "Integer32"
_Valuei5200fREEROOTDISKVMLVS_Object = MibScalar
valuei5200fREEROOTDISKVMLVS = _Valuei5200fREEROOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5200, 3),
    _Valuei5200fREEROOTDISKVMLVS_Type()
)
valuei5200fREEROOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200fREEROOTDISKVMLVS.setStatus("mandatory")
_FREEBOOTDISKVMLVS_ObjectIdentity = ObjectIdentity
fREEBOOTDISKVMLVS = _FREEBOOTDISKVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2)
)
_I5100fREEBOOTDISKVMLVS_ObjectIdentity = ObjectIdentity
i5100fREEBOOTDISKVMLVS = _I5100fREEBOOTDISKVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5100)
)


class _Severityi5100fREEBOOTDISKVMLVS_Type(OctetString):
    """Custom type severityi5100fREEBOOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100fREEBOOTDISKVMLVS_Type.__name__ = "OctetString"
_Severityi5100fREEBOOTDISKVMLVS_Object = MibScalar
severityi5100fREEBOOTDISKVMLVS = _Severityi5100fREEBOOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5100, 1),
    _Severityi5100fREEBOOTDISKVMLVS_Type()
)
severityi5100fREEBOOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100fREEBOOTDISKVMLVS.setStatus("mandatory")


class _Messagei5100fREEBOOTDISKVMLVS_Type(OctetString):
    """Custom type messagei5100fREEBOOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100fREEBOOTDISKVMLVS_Type.__name__ = "OctetString"
_Messagei5100fREEBOOTDISKVMLVS_Object = MibScalar
messagei5100fREEBOOTDISKVMLVS = _Messagei5100fREEBOOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5100, 2),
    _Messagei5100fREEBOOTDISKVMLVS_Type()
)
messagei5100fREEBOOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100fREEBOOTDISKVMLVS.setStatus("mandatory")


class _Valuei5100fREEBOOTDISKVMLVS_Type(Integer32):
    """Custom type valuei5100fREEBOOTDISKVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100fREEBOOTDISKVMLVS_Type.__name__ = "Integer32"
_Valuei5100fREEBOOTDISKVMLVS_Object = MibScalar
valuei5100fREEBOOTDISKVMLVS = _Valuei5100fREEBOOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5100, 3),
    _Valuei5100fREEBOOTDISKVMLVS_Type()
)
valuei5100fREEBOOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100fREEBOOTDISKVMLVS.setStatus("mandatory")
_I5200fREEBOOTDISKVMLVS_ObjectIdentity = ObjectIdentity
i5200fREEBOOTDISKVMLVS = _I5200fREEBOOTDISKVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5200)
)


class _Severityi5200fREEBOOTDISKVMLVS_Type(OctetString):
    """Custom type severityi5200fREEBOOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200fREEBOOTDISKVMLVS_Type.__name__ = "OctetString"
_Severityi5200fREEBOOTDISKVMLVS_Object = MibScalar
severityi5200fREEBOOTDISKVMLVS = _Severityi5200fREEBOOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5200, 1),
    _Severityi5200fREEBOOTDISKVMLVS_Type()
)
severityi5200fREEBOOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200fREEBOOTDISKVMLVS.setStatus("mandatory")


class _Messagei5200fREEBOOTDISKVMLVS_Type(OctetString):
    """Custom type messagei5200fREEBOOTDISKVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200fREEBOOTDISKVMLVS_Type.__name__ = "OctetString"
_Messagei5200fREEBOOTDISKVMLVS_Object = MibScalar
messagei5200fREEBOOTDISKVMLVS = _Messagei5200fREEBOOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5200, 2),
    _Messagei5200fREEBOOTDISKVMLVS_Type()
)
messagei5200fREEBOOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200fREEBOOTDISKVMLVS.setStatus("mandatory")


class _Valuei5200fREEBOOTDISKVMLVS_Type(Integer32):
    """Custom type valuei5200fREEBOOTDISKVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200fREEBOOTDISKVMLVS_Type.__name__ = "Integer32"
_Valuei5200fREEBOOTDISKVMLVS_Object = MibScalar
valuei5200fREEBOOTDISKVMLVS = _Valuei5200fREEBOOTDISKVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5200, 3),
    _Valuei5200fREEBOOTDISKVMLVS_Type()
)
valuei5200fREEBOOTDISKVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200fREEBOOTDISKVMLVS.setStatus("mandatory")
_FREEMEMORYVMLVS_ObjectIdentity = ObjectIdentity
fREEMEMORYVMLVS = _FREEMEMORYVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3)
)
_I5100fREEMEMORYVMLVS_ObjectIdentity = ObjectIdentity
i5100fREEMEMORYVMLVS = _I5100fREEMEMORYVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5100)
)


class _Severityi5100fREEMEMORYVMLVS_Type(OctetString):
    """Custom type severityi5100fREEMEMORYVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100fREEMEMORYVMLVS_Type.__name__ = "OctetString"
_Severityi5100fREEMEMORYVMLVS_Object = MibScalar
severityi5100fREEMEMORYVMLVS = _Severityi5100fREEMEMORYVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5100, 1),
    _Severityi5100fREEMEMORYVMLVS_Type()
)
severityi5100fREEMEMORYVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100fREEMEMORYVMLVS.setStatus("mandatory")


class _Messagei5100fREEMEMORYVMLVS_Type(OctetString):
    """Custom type messagei5100fREEMEMORYVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100fREEMEMORYVMLVS_Type.__name__ = "OctetString"
_Messagei5100fREEMEMORYVMLVS_Object = MibScalar
messagei5100fREEMEMORYVMLVS = _Messagei5100fREEMEMORYVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5100, 2),
    _Messagei5100fREEMEMORYVMLVS_Type()
)
messagei5100fREEMEMORYVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100fREEMEMORYVMLVS.setStatus("mandatory")


class _Valuei5100fREEMEMORYVMLVS_Type(Integer32):
    """Custom type valuei5100fREEMEMORYVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100fREEMEMORYVMLVS_Type.__name__ = "Integer32"
_Valuei5100fREEMEMORYVMLVS_Object = MibScalar
valuei5100fREEMEMORYVMLVS = _Valuei5100fREEMEMORYVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5100, 3),
    _Valuei5100fREEMEMORYVMLVS_Type()
)
valuei5100fREEMEMORYVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100fREEMEMORYVMLVS.setStatus("mandatory")
_I5200fREEMEMORYVMLVS_ObjectIdentity = ObjectIdentity
i5200fREEMEMORYVMLVS = _I5200fREEMEMORYVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5200)
)


class _Severityi5200fREEMEMORYVMLVS_Type(OctetString):
    """Custom type severityi5200fREEMEMORYVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200fREEMEMORYVMLVS_Type.__name__ = "OctetString"
_Severityi5200fREEMEMORYVMLVS_Object = MibScalar
severityi5200fREEMEMORYVMLVS = _Severityi5200fREEMEMORYVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5200, 1),
    _Severityi5200fREEMEMORYVMLVS_Type()
)
severityi5200fREEMEMORYVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200fREEMEMORYVMLVS.setStatus("mandatory")


class _Messagei5200fREEMEMORYVMLVS_Type(OctetString):
    """Custom type messagei5200fREEMEMORYVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200fREEMEMORYVMLVS_Type.__name__ = "OctetString"
_Messagei5200fREEMEMORYVMLVS_Object = MibScalar
messagei5200fREEMEMORYVMLVS = _Messagei5200fREEMEMORYVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5200, 2),
    _Messagei5200fREEMEMORYVMLVS_Type()
)
messagei5200fREEMEMORYVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200fREEMEMORYVMLVS.setStatus("mandatory")


class _Valuei5200fREEMEMORYVMLVS_Type(Integer32):
    """Custom type valuei5200fREEMEMORYVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200fREEMEMORYVMLVS_Type.__name__ = "Integer32"
_Valuei5200fREEMEMORYVMLVS_Object = MibScalar
valuei5200fREEMEMORYVMLVS = _Valuei5200fREEMEMORYVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5200, 3),
    _Valuei5200fREEMEMORYVMLVS_Type()
)
valuei5200fREEMEMORYVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200fREEMEMORYVMLVS.setStatus("mandatory")
_CPULOADVMLVS_ObjectIdentity = ObjectIdentity
cPULOADVMLVS = _CPULOADVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4)
)
_I5100cPULOADVMLVS_ObjectIdentity = ObjectIdentity
i5100cPULOADVMLVS = _I5100cPULOADVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5100)
)


class _Severityi5100cPULOADVMLVS_Type(OctetString):
    """Custom type severityi5100cPULOADVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100cPULOADVMLVS_Type.__name__ = "OctetString"
_Severityi5100cPULOADVMLVS_Object = MibScalar
severityi5100cPULOADVMLVS = _Severityi5100cPULOADVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5100, 1),
    _Severityi5100cPULOADVMLVS_Type()
)
severityi5100cPULOADVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100cPULOADVMLVS.setStatus("mandatory")


class _Messagei5100cPULOADVMLVS_Type(OctetString):
    """Custom type messagei5100cPULOADVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100cPULOADVMLVS_Type.__name__ = "OctetString"
_Messagei5100cPULOADVMLVS_Object = MibScalar
messagei5100cPULOADVMLVS = _Messagei5100cPULOADVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5100, 2),
    _Messagei5100cPULOADVMLVS_Type()
)
messagei5100cPULOADVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100cPULOADVMLVS.setStatus("mandatory")


class _Valuei5100cPULOADVMLVS_Type(Integer32):
    """Custom type valuei5100cPULOADVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100cPULOADVMLVS_Type.__name__ = "Integer32"
_Valuei5100cPULOADVMLVS_Object = MibScalar
valuei5100cPULOADVMLVS = _Valuei5100cPULOADVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5100, 3),
    _Valuei5100cPULOADVMLVS_Type()
)
valuei5100cPULOADVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100cPULOADVMLVS.setStatus("mandatory")
_I5200cPULOADVMLVS_ObjectIdentity = ObjectIdentity
i5200cPULOADVMLVS = _I5200cPULOADVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5200)
)


class _Severityi5200cPULOADVMLVS_Type(OctetString):
    """Custom type severityi5200cPULOADVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200cPULOADVMLVS_Type.__name__ = "OctetString"
_Severityi5200cPULOADVMLVS_Object = MibScalar
severityi5200cPULOADVMLVS = _Severityi5200cPULOADVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5200, 1),
    _Severityi5200cPULOADVMLVS_Type()
)
severityi5200cPULOADVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200cPULOADVMLVS.setStatus("mandatory")


class _Messagei5200cPULOADVMLVS_Type(OctetString):
    """Custom type messagei5200cPULOADVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200cPULOADVMLVS_Type.__name__ = "OctetString"
_Messagei5200cPULOADVMLVS_Object = MibScalar
messagei5200cPULOADVMLVS = _Messagei5200cPULOADVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5200, 2),
    _Messagei5200cPULOADVMLVS_Type()
)
messagei5200cPULOADVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200cPULOADVMLVS.setStatus("mandatory")


class _Valuei5200cPULOADVMLVS_Type(Integer32):
    """Custom type valuei5200cPULOADVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200cPULOADVMLVS_Type.__name__ = "Integer32"
_Valuei5200cPULOADVMLVS_Object = MibScalar
valuei5200cPULOADVMLVS = _Valuei5200cPULOADVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5200, 3),
    _Valuei5200cPULOADVMLVS_Type()
)
valuei5200cPULOADVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200cPULOADVMLVS.setStatus("mandatory")
_FREESWAPVMLVS_ObjectIdentity = ObjectIdentity
fREESWAPVMLVS = _FREESWAPVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5)
)
_I5100fREESWAPVMLVS_ObjectIdentity = ObjectIdentity
i5100fREESWAPVMLVS = _I5100fREESWAPVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5100)
)


class _Severityi5100fREESWAPVMLVS_Type(OctetString):
    """Custom type severityi5100fREESWAPVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100fREESWAPVMLVS_Type.__name__ = "OctetString"
_Severityi5100fREESWAPVMLVS_Object = MibScalar
severityi5100fREESWAPVMLVS = _Severityi5100fREESWAPVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5100, 1),
    _Severityi5100fREESWAPVMLVS_Type()
)
severityi5100fREESWAPVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100fREESWAPVMLVS.setStatus("mandatory")


class _Messagei5100fREESWAPVMLVS_Type(OctetString):
    """Custom type messagei5100fREESWAPVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100fREESWAPVMLVS_Type.__name__ = "OctetString"
_Messagei5100fREESWAPVMLVS_Object = MibScalar
messagei5100fREESWAPVMLVS = _Messagei5100fREESWAPVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5100, 2),
    _Messagei5100fREESWAPVMLVS_Type()
)
messagei5100fREESWAPVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100fREESWAPVMLVS.setStatus("mandatory")


class _Valuei5100fREESWAPVMLVS_Type(Integer32):
    """Custom type valuei5100fREESWAPVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100fREESWAPVMLVS_Type.__name__ = "Integer32"
_Valuei5100fREESWAPVMLVS_Object = MibScalar
valuei5100fREESWAPVMLVS = _Valuei5100fREESWAPVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5100, 3),
    _Valuei5100fREESWAPVMLVS_Type()
)
valuei5100fREESWAPVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100fREESWAPVMLVS.setStatus("mandatory")
_I5200fREESWAPVMLVS_ObjectIdentity = ObjectIdentity
i5200fREESWAPVMLVS = _I5200fREESWAPVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5200)
)


class _Severityi5200fREESWAPVMLVS_Type(OctetString):
    """Custom type severityi5200fREESWAPVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200fREESWAPVMLVS_Type.__name__ = "OctetString"
_Severityi5200fREESWAPVMLVS_Object = MibScalar
severityi5200fREESWAPVMLVS = _Severityi5200fREESWAPVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5200, 1),
    _Severityi5200fREESWAPVMLVS_Type()
)
severityi5200fREESWAPVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200fREESWAPVMLVS.setStatus("mandatory")


class _Messagei5200fREESWAPVMLVS_Type(OctetString):
    """Custom type messagei5200fREESWAPVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200fREESWAPVMLVS_Type.__name__ = "OctetString"
_Messagei5200fREESWAPVMLVS_Object = MibScalar
messagei5200fREESWAPVMLVS = _Messagei5200fREESWAPVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5200, 2),
    _Messagei5200fREESWAPVMLVS_Type()
)
messagei5200fREESWAPVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200fREESWAPVMLVS.setStatus("mandatory")


class _Valuei5200fREESWAPVMLVS_Type(Integer32):
    """Custom type valuei5200fREESWAPVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200fREESWAPVMLVS_Type.__name__ = "Integer32"
_Valuei5200fREESWAPVMLVS_Object = MibScalar
valuei5200fREESWAPVMLVS = _Valuei5200fREESWAPVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5200, 3),
    _Valuei5200fREESWAPVMLVS_Type()
)
valuei5200fREESWAPVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200fREESWAPVMLVS.setStatus("mandatory")
_ETHINTSTATUSVMLVS_ObjectIdentity = ObjectIdentity
eTHINTSTATUSVMLVS = _ETHINTSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6)
)
_I5100eTHINTSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5100eTHINTSTATUSVMLVS = _I5100eTHINTSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5100)
)


class _Severityi5100eTHINTSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5100eTHINTSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100eTHINTSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5100eTHINTSTATUSVMLVS_Object = MibScalar
severityi5100eTHINTSTATUSVMLVS = _Severityi5100eTHINTSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5100, 1),
    _Severityi5100eTHINTSTATUSVMLVS_Type()
)
severityi5100eTHINTSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100eTHINTSTATUSVMLVS.setStatus("mandatory")


class _Messagei5100eTHINTSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5100eTHINTSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100eTHINTSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5100eTHINTSTATUSVMLVS_Object = MibScalar
messagei5100eTHINTSTATUSVMLVS = _Messagei5100eTHINTSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5100, 2),
    _Messagei5100eTHINTSTATUSVMLVS_Type()
)
messagei5100eTHINTSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100eTHINTSTATUSVMLVS.setStatus("mandatory")


class _Valuei5100eTHINTSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5100eTHINTSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100eTHINTSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5100eTHINTSTATUSVMLVS_Object = MibScalar
valuei5100eTHINTSTATUSVMLVS = _Valuei5100eTHINTSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5100, 3),
    _Valuei5100eTHINTSTATUSVMLVS_Type()
)
valuei5100eTHINTSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100eTHINTSTATUSVMLVS.setStatus("mandatory")
_I5200eTHINTSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5200eTHINTSTATUSVMLVS = _I5200eTHINTSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5200)
)


class _Severityi5200eTHINTSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5200eTHINTSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200eTHINTSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5200eTHINTSTATUSVMLVS_Object = MibScalar
severityi5200eTHINTSTATUSVMLVS = _Severityi5200eTHINTSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5200, 1),
    _Severityi5200eTHINTSTATUSVMLVS_Type()
)
severityi5200eTHINTSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200eTHINTSTATUSVMLVS.setStatus("mandatory")


class _Messagei5200eTHINTSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5200eTHINTSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200eTHINTSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5200eTHINTSTATUSVMLVS_Object = MibScalar
messagei5200eTHINTSTATUSVMLVS = _Messagei5200eTHINTSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5200, 2),
    _Messagei5200eTHINTSTATUSVMLVS_Type()
)
messagei5200eTHINTSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200eTHINTSTATUSVMLVS.setStatus("mandatory")


class _Valuei5200eTHINTSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5200eTHINTSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200eTHINTSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5200eTHINTSTATUSVMLVS_Object = MibScalar
valuei5200eTHINTSTATUSVMLVS = _Valuei5200eTHINTSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5200, 3),
    _Valuei5200eTHINTSTATUSVMLVS_Type()
)
valuei5200eTHINTSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200eTHINTSTATUSVMLVS.setStatus("mandatory")
_CRONSTATUSVMLVS_ObjectIdentity = ObjectIdentity
cRONSTATUSVMLVS = _CRONSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7)
)
_I5100cRONSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5100cRONSTATUSVMLVS = _I5100cRONSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5100)
)


class _Severityi5100cRONSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5100cRONSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100cRONSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5100cRONSTATUSVMLVS_Object = MibScalar
severityi5100cRONSTATUSVMLVS = _Severityi5100cRONSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5100, 1),
    _Severityi5100cRONSTATUSVMLVS_Type()
)
severityi5100cRONSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100cRONSTATUSVMLVS.setStatus("mandatory")


class _Messagei5100cRONSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5100cRONSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100cRONSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5100cRONSTATUSVMLVS_Object = MibScalar
messagei5100cRONSTATUSVMLVS = _Messagei5100cRONSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5100, 2),
    _Messagei5100cRONSTATUSVMLVS_Type()
)
messagei5100cRONSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100cRONSTATUSVMLVS.setStatus("mandatory")


class _Valuei5100cRONSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5100cRONSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100cRONSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5100cRONSTATUSVMLVS_Object = MibScalar
valuei5100cRONSTATUSVMLVS = _Valuei5100cRONSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5100, 3),
    _Valuei5100cRONSTATUSVMLVS_Type()
)
valuei5100cRONSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100cRONSTATUSVMLVS.setStatus("mandatory")
_I5200cRONSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5200cRONSTATUSVMLVS = _I5200cRONSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5200)
)


class _Severityi5200cRONSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5200cRONSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200cRONSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5200cRONSTATUSVMLVS_Object = MibScalar
severityi5200cRONSTATUSVMLVS = _Severityi5200cRONSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5200, 1),
    _Severityi5200cRONSTATUSVMLVS_Type()
)
severityi5200cRONSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200cRONSTATUSVMLVS.setStatus("mandatory")


class _Messagei5200cRONSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5200cRONSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200cRONSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5200cRONSTATUSVMLVS_Object = MibScalar
messagei5200cRONSTATUSVMLVS = _Messagei5200cRONSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5200, 2),
    _Messagei5200cRONSTATUSVMLVS_Type()
)
messagei5200cRONSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200cRONSTATUSVMLVS.setStatus("mandatory")


class _Valuei5200cRONSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5200cRONSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200cRONSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5200cRONSTATUSVMLVS_Object = MibScalar
valuei5200cRONSTATUSVMLVS = _Valuei5200cRONSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5200, 3),
    _Valuei5200cRONSTATUSVMLVS_Type()
)
valuei5200cRONSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200cRONSTATUSVMLVS.setStatus("mandatory")
_MONITSTATUSVMLVS_ObjectIdentity = ObjectIdentity
mONITSTATUSVMLVS = _MONITSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8)
)
_I5100mONITSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5100mONITSTATUSVMLVS = _I5100mONITSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5100)
)


class _Severityi5100mONITSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5100mONITSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100mONITSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5100mONITSTATUSVMLVS_Object = MibScalar
severityi5100mONITSTATUSVMLVS = _Severityi5100mONITSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5100, 1),
    _Severityi5100mONITSTATUSVMLVS_Type()
)
severityi5100mONITSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100mONITSTATUSVMLVS.setStatus("mandatory")


class _Messagei5100mONITSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5100mONITSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100mONITSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5100mONITSTATUSVMLVS_Object = MibScalar
messagei5100mONITSTATUSVMLVS = _Messagei5100mONITSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5100, 2),
    _Messagei5100mONITSTATUSVMLVS_Type()
)
messagei5100mONITSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100mONITSTATUSVMLVS.setStatus("mandatory")


class _Valuei5100mONITSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5100mONITSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100mONITSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5100mONITSTATUSVMLVS_Object = MibScalar
valuei5100mONITSTATUSVMLVS = _Valuei5100mONITSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5100, 3),
    _Valuei5100mONITSTATUSVMLVS_Type()
)
valuei5100mONITSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100mONITSTATUSVMLVS.setStatus("mandatory")
_I5200mONITSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5200mONITSTATUSVMLVS = _I5200mONITSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5200)
)


class _Severityi5200mONITSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5200mONITSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200mONITSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5200mONITSTATUSVMLVS_Object = MibScalar
severityi5200mONITSTATUSVMLVS = _Severityi5200mONITSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5200, 1),
    _Severityi5200mONITSTATUSVMLVS_Type()
)
severityi5200mONITSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200mONITSTATUSVMLVS.setStatus("mandatory")


class _Messagei5200mONITSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5200mONITSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200mONITSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5200mONITSTATUSVMLVS_Object = MibScalar
messagei5200mONITSTATUSVMLVS = _Messagei5200mONITSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5200, 2),
    _Messagei5200mONITSTATUSVMLVS_Type()
)
messagei5200mONITSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200mONITSTATUSVMLVS.setStatus("mandatory")


class _Valuei5200mONITSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5200mONITSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200mONITSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5200mONITSTATUSVMLVS_Object = MibScalar
valuei5200mONITSTATUSVMLVS = _Valuei5200mONITSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5200, 3),
    _Valuei5200mONITSTATUSVMLVS_Type()
)
valuei5200mONITSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200mONITSTATUSVMLVS.setStatus("mandatory")
_PULSESTATUSVMLVS_ObjectIdentity = ObjectIdentity
pULSESTATUSVMLVS = _PULSESTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10)
)
_I5100pULSESTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5100pULSESTATUSVMLVS = _I5100pULSESTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5100)
)


class _Severityi5100pULSESTATUSVMLVS_Type(OctetString):
    """Custom type severityi5100pULSESTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100pULSESTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5100pULSESTATUSVMLVS_Object = MibScalar
severityi5100pULSESTATUSVMLVS = _Severityi5100pULSESTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5100, 1),
    _Severityi5100pULSESTATUSVMLVS_Type()
)
severityi5100pULSESTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100pULSESTATUSVMLVS.setStatus("mandatory")


class _Messagei5100pULSESTATUSVMLVS_Type(OctetString):
    """Custom type messagei5100pULSESTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100pULSESTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5100pULSESTATUSVMLVS_Object = MibScalar
messagei5100pULSESTATUSVMLVS = _Messagei5100pULSESTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5100, 2),
    _Messagei5100pULSESTATUSVMLVS_Type()
)
messagei5100pULSESTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100pULSESTATUSVMLVS.setStatus("mandatory")


class _Valuei5100pULSESTATUSVMLVS_Type(Integer32):
    """Custom type valuei5100pULSESTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100pULSESTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5100pULSESTATUSVMLVS_Object = MibScalar
valuei5100pULSESTATUSVMLVS = _Valuei5100pULSESTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5100, 3),
    _Valuei5100pULSESTATUSVMLVS_Type()
)
valuei5100pULSESTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100pULSESTATUSVMLVS.setStatus("mandatory")
_I5200pULSESTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5200pULSESTATUSVMLVS = _I5200pULSESTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5200)
)


class _Severityi5200pULSESTATUSVMLVS_Type(OctetString):
    """Custom type severityi5200pULSESTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200pULSESTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5200pULSESTATUSVMLVS_Object = MibScalar
severityi5200pULSESTATUSVMLVS = _Severityi5200pULSESTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5200, 1),
    _Severityi5200pULSESTATUSVMLVS_Type()
)
severityi5200pULSESTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200pULSESTATUSVMLVS.setStatus("mandatory")


class _Messagei5200pULSESTATUSVMLVS_Type(OctetString):
    """Custom type messagei5200pULSESTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200pULSESTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5200pULSESTATUSVMLVS_Object = MibScalar
messagei5200pULSESTATUSVMLVS = _Messagei5200pULSESTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5200, 2),
    _Messagei5200pULSESTATUSVMLVS_Type()
)
messagei5200pULSESTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200pULSESTATUSVMLVS.setStatus("mandatory")


class _Valuei5200pULSESTATUSVMLVS_Type(Integer32):
    """Custom type valuei5200pULSESTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200pULSESTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5200pULSESTATUSVMLVS_Object = MibScalar
valuei5200pULSESTATUSVMLVS = _Valuei5200pULSESTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5200, 3),
    _Valuei5200pULSESTATUSVMLVS_Type()
)
valuei5200pULSESTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200pULSESTATUSVMLVS.setStatus("mandatory")
_CPUSTATUSVMLVS_ObjectIdentity = ObjectIdentity
cPUSTATUSVMLVS = _CPUSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18)
)
_I5100cPUSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5100cPUSTATUSVMLVS = _I5100cPUSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5100)
)


class _Severityi5100cPUSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5100cPUSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100cPUSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5100cPUSTATUSVMLVS_Object = MibScalar
severityi5100cPUSTATUSVMLVS = _Severityi5100cPUSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5100, 1),
    _Severityi5100cPUSTATUSVMLVS_Type()
)
severityi5100cPUSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100cPUSTATUSVMLVS.setStatus("mandatory")


class _Messagei5100cPUSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5100cPUSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100cPUSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5100cPUSTATUSVMLVS_Object = MibScalar
messagei5100cPUSTATUSVMLVS = _Messagei5100cPUSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5100, 2),
    _Messagei5100cPUSTATUSVMLVS_Type()
)
messagei5100cPUSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100cPUSTATUSVMLVS.setStatus("mandatory")


class _Valuei5100cPUSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5100cPUSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100cPUSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5100cPUSTATUSVMLVS_Object = MibScalar
valuei5100cPUSTATUSVMLVS = _Valuei5100cPUSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5100, 3),
    _Valuei5100cPUSTATUSVMLVS_Type()
)
valuei5100cPUSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100cPUSTATUSVMLVS.setStatus("mandatory")
_I5200cPUSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5200cPUSTATUSVMLVS = _I5200cPUSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5200)
)


class _Severityi5200cPUSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5200cPUSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200cPUSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5200cPUSTATUSVMLVS_Object = MibScalar
severityi5200cPUSTATUSVMLVS = _Severityi5200cPUSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5200, 1),
    _Severityi5200cPUSTATUSVMLVS_Type()
)
severityi5200cPUSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200cPUSTATUSVMLVS.setStatus("mandatory")


class _Messagei5200cPUSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5200cPUSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200cPUSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5200cPUSTATUSVMLVS_Object = MibScalar
messagei5200cPUSTATUSVMLVS = _Messagei5200cPUSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5200, 2),
    _Messagei5200cPUSTATUSVMLVS_Type()
)
messagei5200cPUSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200cPUSTATUSVMLVS.setStatus("mandatory")


class _Valuei5200cPUSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5200cPUSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200cPUSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5200cPUSTATUSVMLVS_Object = MibScalar
valuei5200cPUSTATUSVMLVS = _Valuei5200cPUSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5200, 3),
    _Valuei5200cPUSTATUSVMLVS_Type()
)
valuei5200cPUSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200cPUSTATUSVMLVS.setStatus("mandatory")
_LVSSTATUSVMLVS_ObjectIdentity = ObjectIdentity
lVSSTATUSVMLVS = _LVSSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22)
)
_I5100lVSSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5100lVSSTATUSVMLVS = _I5100lVSSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5100)
)


class _Severityi5100lVSSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5100lVSSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5100lVSSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5100lVSSTATUSVMLVS_Object = MibScalar
severityi5100lVSSTATUSVMLVS = _Severityi5100lVSSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5100, 1),
    _Severityi5100lVSSTATUSVMLVS_Type()
)
severityi5100lVSSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5100lVSSTATUSVMLVS.setStatus("mandatory")


class _Messagei5100lVSSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5100lVSSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5100lVSSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5100lVSSTATUSVMLVS_Object = MibScalar
messagei5100lVSSTATUSVMLVS = _Messagei5100lVSSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5100, 2),
    _Messagei5100lVSSTATUSVMLVS_Type()
)
messagei5100lVSSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5100lVSSTATUSVMLVS.setStatus("mandatory")


class _Valuei5100lVSSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5100lVSSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5100lVSSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5100lVSSTATUSVMLVS_Object = MibScalar
valuei5100lVSSTATUSVMLVS = _Valuei5100lVSSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5100, 3),
    _Valuei5100lVSSTATUSVMLVS_Type()
)
valuei5100lVSSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5100lVSSTATUSVMLVS.setStatus("mandatory")
_I5200lVSSTATUSVMLVS_ObjectIdentity = ObjectIdentity
i5200lVSSTATUSVMLVS = _I5200lVSSTATUSVMLVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5200)
)


class _Severityi5200lVSSTATUSVMLVS_Type(OctetString):
    """Custom type severityi5200lVSSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Severityi5200lVSSTATUSVMLVS_Type.__name__ = "OctetString"
_Severityi5200lVSSTATUSVMLVS_Object = MibScalar
severityi5200lVSSTATUSVMLVS = _Severityi5200lVSSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5200, 1),
    _Severityi5200lVSSTATUSVMLVS_Type()
)
severityi5200lVSSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityi5200lVSSTATUSVMLVS.setStatus("mandatory")


class _Messagei5200lVSSTATUSVMLVS_Type(OctetString):
    """Custom type messagei5200lVSSTATUSVMLVS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Messagei5200lVSSTATUSVMLVS_Type.__name__ = "OctetString"
_Messagei5200lVSSTATUSVMLVS_Object = MibScalar
messagei5200lVSSTATUSVMLVS = _Messagei5200lVSSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5200, 2),
    _Messagei5200lVSSTATUSVMLVS_Type()
)
messagei5200lVSSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    messagei5200lVSSTATUSVMLVS.setStatus("mandatory")


class _Valuei5200lVSSTATUSVMLVS_Type(Integer32):
    """Custom type valuei5200lVSSTATUSVMLVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483641, 2147483647),
    )


_Valuei5200lVSSTATUSVMLVS_Type.__name__ = "Integer32"
_Valuei5200lVSSTATUSVMLVS_Object = MibScalar
valuei5200lVSSTATUSVMLVS = _Valuei5200lVSSTATUSVMLVS_Object(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5200, 3),
    _Valuei5200lVSSTATUSVMLVS_Type()
)
valuei5200lVSSTATUSVMLVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuei5200lVSSTATUSVMLVS.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tRAPi1101fREEROOTDISKVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1101, 0, 1)
)
tRAPi1101fREEROOTDISKVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100fREEROOTDISKVMAS"),
        ("VMFIX-MIB", "messagei1100fREEROOTDISKVMAS"),
        ("VMFIX-MIB", "valuei1100fREEROOTDISKVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1101fREEROOTDISKVMAS.setStatus(
        ""
    )

tRAPi1200fREEROOTDISKVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1200, 0, 5)
)
tRAPi1200fREEROOTDISKVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200fREEROOTDISKVMAS"),
        ("VMFIX-MIB", "messagei1200fREEROOTDISKVMAS"),
        ("VMFIX-MIB", "valuei1200fREEROOTDISKVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200fREEROOTDISKVMAS.setStatus(
        ""
    )

tRAPi1300fREEROOTDISKVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 1, 1300, 0, 5)
)
tRAPi1300fREEROOTDISKVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300fREEROOTDISKVMAS"),
        ("VMFIX-MIB", "messagei1300fREEROOTDISKVMAS"),
        ("VMFIX-MIB", "valuei1300fREEROOTDISKVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300fREEROOTDISKVMAS.setStatus(
        ""
    )

tRAPi1100fREEBOOTDISKVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1100, 0, 1)
)
tRAPi1100fREEBOOTDISKVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100fREEBOOTDISKVMAS"),
        ("VMFIX-MIB", "messagei1100fREEBOOTDISKVMAS"),
        ("VMFIX-MIB", "valuei1100fREEBOOTDISKVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100fREEBOOTDISKVMAS.setStatus(
        ""
    )

tRAPi1200fREEBOOTDISKVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1200, 0, 5)
)
tRAPi1200fREEBOOTDISKVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200fREEBOOTDISKVMAS"),
        ("VMFIX-MIB", "messagei1200fREEBOOTDISKVMAS"),
        ("VMFIX-MIB", "valuei1200fREEBOOTDISKVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200fREEBOOTDISKVMAS.setStatus(
        ""
    )

tRAPi1300fREEBOOTDISKVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 2, 1300, 0, 5)
)
tRAPi1300fREEBOOTDISKVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300fREEBOOTDISKVMAS"),
        ("VMFIX-MIB", "messagei1300fREEBOOTDISKVMAS"),
        ("VMFIX-MIB", "valuei1300fREEBOOTDISKVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300fREEBOOTDISKVMAS.setStatus(
        ""
    )

tRAPi1100fREEMEMORYVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1100, 0, 1)
)
tRAPi1100fREEMEMORYVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100fREEMEMORYVMAS"),
        ("VMFIX-MIB", "messagei1100fREEMEMORYVMAS"),
        ("VMFIX-MIB", "valuei1100fREEMEMORYVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100fREEMEMORYVMAS.setStatus(
        ""
    )

tRAPi1200fREEMEMORYVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1200, 0, 5)
)
tRAPi1200fREEMEMORYVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200fREEMEMORYVMAS"),
        ("VMFIX-MIB", "messagei1200fREEMEMORYVMAS"),
        ("VMFIX-MIB", "valuei1200fREEMEMORYVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200fREEMEMORYVMAS.setStatus(
        ""
    )

tRAPi1300fREEMEMORYVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 3, 1300, 0, 5)
)
tRAPi1300fREEMEMORYVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300fREEMEMORYVMAS"),
        ("VMFIX-MIB", "messagei1300fREEMEMORYVMAS"),
        ("VMFIX-MIB", "valuei1300fREEMEMORYVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300fREEMEMORYVMAS.setStatus(
        ""
    )

tRAPi1100cPULOADVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1100, 0, 1)
)
tRAPi1100cPULOADVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100cPULOADVMAS"),
        ("VMFIX-MIB", "messagei1100cPULOADVMAS"),
        ("VMFIX-MIB", "valuei1100cPULOADVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100cPULOADVMAS.setStatus(
        ""
    )

tRAPi1200cPULOADVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1200, 0, 5)
)
tRAPi1200cPULOADVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200cPULOADVMAS"),
        ("VMFIX-MIB", "messagei1200cPULOADVMAS"),
        ("VMFIX-MIB", "valuei1200cPULOADVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200cPULOADVMAS.setStatus(
        ""
    )

tRAPi1300cPULOADVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 4, 1300, 0, 5)
)
tRAPi1300cPULOADVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300cPULOADVMAS"),
        ("VMFIX-MIB", "messagei1300cPULOADVMAS"),
        ("VMFIX-MIB", "valuei1300cPULOADVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300cPULOADVMAS.setStatus(
        ""
    )

tRAPi1100fREESWAPVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1100, 0, 1)
)
tRAPi1100fREESWAPVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100fREESWAPVMAS"),
        ("VMFIX-MIB", "messagei1100fREESWAPVMAS"),
        ("VMFIX-MIB", "valuei1100fREESWAPVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100fREESWAPVMAS.setStatus(
        ""
    )

tRAPi1200fREESWAPVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1200, 0, 5)
)
tRAPi1200fREESWAPVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200fREESWAPVMAS"),
        ("VMFIX-MIB", "messagei1200fREESWAPVMAS"),
        ("VMFIX-MIB", "valuei1200fREESWAPVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200fREESWAPVMAS.setStatus(
        ""
    )

tRAPi1300fREESWAPVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 5, 1300, 0, 5)
)
tRAPi1300fREESWAPVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300fREESWAPVMAS"),
        ("VMFIX-MIB", "messagei1300fREESWAPVMAS"),
        ("VMFIX-MIB", "valuei1300fREESWAPVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300fREESWAPVMAS.setStatus(
        ""
    )

tRAPi1100eTHINTSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1100, 0, 1)
)
tRAPi1100eTHINTSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100eTHINTSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100eTHINTSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100eTHINTSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100eTHINTSTATUSVMAS.setStatus(
        ""
    )

tRAPi1200eTHINTSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1200, 0, 5)
)
tRAPi1200eTHINTSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200eTHINTSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200eTHINTSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200eTHINTSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200eTHINTSTATUSVMAS.setStatus(
        ""
    )

tRAPi1300eTHINTSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 6, 1300, 0, 5)
)
tRAPi1300eTHINTSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300eTHINTSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300eTHINTSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300eTHINTSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300eTHINTSTATUSVMAS.setStatus(
        ""
    )

tRAPi1100cRONSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1100, 0, 1)
)
tRAPi1100cRONSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100cRONSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100cRONSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100cRONSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100cRONSTATUSVMAS.setStatus(
        ""
    )

tRAPi1200cRONSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1200, 0, 5)
)
tRAPi1200cRONSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200cRONSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200cRONSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200cRONSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200cRONSTATUSVMAS.setStatus(
        ""
    )

tRAPi1300cRONSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 7, 1300, 0, 5)
)
tRAPi1300cRONSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300cRONSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300cRONSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300cRONSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300cRONSTATUSVMAS.setStatus(
        ""
    )

tRAPi1100mONITSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1100, 0, 1)
)
tRAPi1100mONITSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100mONITSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100mONITSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100mONITSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100mONITSTATUSVMAS.setStatus(
        ""
    )

tRAPi1200mONITSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1200, 0, 5)
)
tRAPi1200mONITSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200mONITSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200mONITSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200mONITSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200mONITSTATUSVMAS.setStatus(
        ""
    )

tRAPi1300mONITSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 8, 1300, 0, 5)
)
tRAPi1300mONITSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300mONITSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300mONITSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300mONITSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300mONITSTATUSVMAS.setStatus(
        ""
    )

tRAPi1100dNSMASQSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1100, 0, 1)
)
tRAPi1100dNSMASQSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100dNSMASQSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100dNSMASQSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100dNSMASQSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100dNSMASQSTATUSVMAS.setStatus(
        ""
    )

tRAPi1200dNSMASQSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1200, 0, 5)
)
tRAPi1200dNSMASQSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200dNSMASQSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200dNSMASQSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200dNSMASQSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200dNSMASQSTATUSVMAS.setStatus(
        ""
    )

tRAPi1300dNSMASQSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 9, 1300, 0, 5)
)
tRAPi1300dNSMASQSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300dNSMASQSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300dNSMASQSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300dNSMASQSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300dNSMASQSTATUSVMAS.setStatus(
        ""
    )

tRAPi1100hB2STATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1100, 0, 1)
)
tRAPi1100hB2STATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100hB2STATUSVMAS"),
        ("VMFIX-MIB", "messagei1100hB2STATUSVMAS"),
        ("VMFIX-MIB", "valuei1100hB2STATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100hB2STATUSVMAS.setStatus(
        ""
    )

tRAPi1200hB2STATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1200, 0, 5)
)
tRAPi1200hB2STATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200hB2STATUSVMAS"),
        ("VMFIX-MIB", "messagei1200hB2STATUSVMAS"),
        ("VMFIX-MIB", "valuei1200hB2STATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200hB2STATUSVMAS.setStatus(
        ""
    )

tRAPi1300hB2STATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 11, 1300, 0, 5)
)
tRAPi1300hB2STATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300hB2STATUSVMAS"),
        ("VMFIX-MIB", "messagei1300hB2STATUSVMAS"),
        ("VMFIX-MIB", "valuei1300hB2STATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300hB2STATUSVMAS.setStatus(
        ""
    )

tRAPi1100tOMCATSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1100, 0, 1)
)
tRAPi1100tOMCATSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100tOMCATSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100tOMCATSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100tOMCATSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100tOMCATSTATUSVMAS.setStatus(
        ""
    )

tRAPi1200tOMCATSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1200, 0, 5)
)
tRAPi1200tOMCATSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200tOMCATSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200tOMCATSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200tOMCATSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200tOMCATSTATUSVMAS.setStatus(
        ""
    )

tRAPi1300tOMCATSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 13, 1300, 0, 5)
)
tRAPi1300tOMCATSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300tOMCATSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300tOMCATSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300tOMCATSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300tOMCATSTATUSVMAS.setStatus(
        ""
    )

tRAPi1100cPUSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1100, 0, 1)
)
tRAPi1100cPUSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100cPUSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100cPUSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100cPUSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100cPUSTATUSVMAS.setStatus(
        ""
    )

tRAPi1200cPUSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1200, 0, 5)
)
tRAPi1200cPUSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200cPUSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200cPUSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200cPUSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200cPUSTATUSVMAS.setStatus(
        ""
    )

tRAPi1300cPUSTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 18, 1300, 0, 5)
)
tRAPi1300cPUSTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300cPUSTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300cPUSTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300cPUSTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300cPUSTATUSVMAS.setStatus(
        ""
    )

tRAPi1100vMCORESTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1100, 0, 1)
)
tRAPi1100vMCORESTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1100vMCORESTATUSVMAS"),
        ("VMFIX-MIB", "messagei1100vMCORESTATUSVMAS"),
        ("VMFIX-MIB", "valuei1100vMCORESTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1100vMCORESTATUSVMAS.setStatus(
        ""
    )

tRAPi1200vMCORESTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1200, 0, 5)
)
tRAPi1200vMCORESTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1200vMCORESTATUSVMAS"),
        ("VMFIX-MIB", "messagei1200vMCORESTATUSVMAS"),
        ("VMFIX-MIB", "valuei1200vMCORESTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1200vMCORESTATUSVMAS.setStatus(
        ""
    )

tRAPi1300vMCORESTATUSVMAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 101, 20, 1300, 0, 5)
)
tRAPi1300vMCORESTATUSVMAS.setObjects(
      *(("VMFIX-MIB", "severityi1300vMCORESTATUSVMAS"),
        ("VMFIX-MIB", "messagei1300vMCORESTATUSVMAS"),
        ("VMFIX-MIB", "valuei1300vMCORESTATUSVMAS"))
)
if mibBuilder.loadTexts:
    tRAPi1300vMCORESTATUSVMAS.setStatus(
        ""
    )

tRAPi2100fREEROOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2100, 0, 5)
)
tRAPi2100fREEROOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2100fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2100fREEROOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100fREEROOTDISKVMMS.setStatus(
        ""
    )

tRAPi2200fREEROOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2200, 0, 5)
)
tRAPi2200fREEROOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2200fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2200fREEROOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200fREEROOTDISKVMMS.setStatus(
        ""
    )

tRAPi2300fREEROOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2300, 0, 5)
)
tRAPi2300fREEROOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2300fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2300fREEROOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300fREEROOTDISKVMMS.setStatus(
        ""
    )

tRAPi2400fREEROOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 1, 2400, 0, 5)
)
tRAPi2400fREEROOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2400fREEROOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2400fREEROOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400fREEROOTDISKVMMS.setStatus(
        ""
    )

tRAPi2100fREEBOOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2100, 0, 5)
)
tRAPi2100fREEBOOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2100fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2100fREEBOOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100fREEBOOTDISKVMMS.setStatus(
        ""
    )

tRAPi2200fREEBOOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2200, 0, 5)
)
tRAPi2200fREEBOOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2200fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2200fREEBOOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200fREEBOOTDISKVMMS.setStatus(
        ""
    )

tRAPi2300fREEBOOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2300, 0, 5)
)
tRAPi2300fREEBOOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2300fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2300fREEBOOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300fREEBOOTDISKVMMS.setStatus(
        ""
    )

tRAPi2400fREEBOOTDISKVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 2, 2400, 0, 5)
)
tRAPi2400fREEBOOTDISKVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "messagei2400fREEBOOTDISKVMMS"),
        ("VMFIX-MIB", "valuei2400fREEBOOTDISKVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400fREEBOOTDISKVMMS.setStatus(
        ""
    )

tRAPi2100fREEMEMORYVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2100, 0, 5)
)
tRAPi2100fREEMEMORYVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100fREEMEMORYVMMS"),
        ("VMFIX-MIB", "messagei2100fREEMEMORYVMMS"),
        ("VMFIX-MIB", "valuei2100fREEMEMORYVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100fREEMEMORYVMMS.setStatus(
        ""
    )

tRAPi2200fREEMEMORYVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2200, 0, 5)
)
tRAPi2200fREEMEMORYVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200fREEMEMORYVMMS"),
        ("VMFIX-MIB", "messagei2200fREEMEMORYVMMS"),
        ("VMFIX-MIB", "valuei2200fREEMEMORYVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200fREEMEMORYVMMS.setStatus(
        ""
    )

tRAPi2300fREEMEMORYVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2300, 0, 5)
)
tRAPi2300fREEMEMORYVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300fREEMEMORYVMMS"),
        ("VMFIX-MIB", "messagei2300fREEMEMORYVMMS"),
        ("VMFIX-MIB", "valuei2300fREEMEMORYVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300fREEMEMORYVMMS.setStatus(
        ""
    )

tRAPi2400fREEMEMORYVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 3, 2400, 0, 5)
)
tRAPi2400fREEMEMORYVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400fREEMEMORYVMMS"),
        ("VMFIX-MIB", "messagei2400fREEMEMORYVMMS"),
        ("VMFIX-MIB", "valuei2400fREEMEMORYVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400fREEMEMORYVMMS.setStatus(
        ""
    )

tRAPi2100cPULOADVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2100, 0, 5)
)
tRAPi2100cPULOADVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100cPULOADVMMS"),
        ("VMFIX-MIB", "messagei2100cPULOADVMMS"),
        ("VMFIX-MIB", "valuei2100cPULOADVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100cPULOADVMMS.setStatus(
        ""
    )

tRAPi2200cPULOADVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2200, 0, 5)
)
tRAPi2200cPULOADVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200cPULOADVMMS"),
        ("VMFIX-MIB", "messagei2200cPULOADVMMS"),
        ("VMFIX-MIB", "valuei2200cPULOADVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200cPULOADVMMS.setStatus(
        ""
    )

tRAPi2300cPULOADVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2300, 0, 5)
)
tRAPi2300cPULOADVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300cPULOADVMMS"),
        ("VMFIX-MIB", "messagei2300cPULOADVMMS"),
        ("VMFIX-MIB", "valuei2300cPULOADVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300cPULOADVMMS.setStatus(
        ""
    )

tRAPi2400cPULOADVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 4, 2400, 0, 5)
)
tRAPi2400cPULOADVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400cPULOADVMMS"),
        ("VMFIX-MIB", "messagei2400cPULOADVMMS"),
        ("VMFIX-MIB", "valuei2400cPULOADVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400cPULOADVMMS.setStatus(
        ""
    )

tRAPi2100fREESWAPVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2100, 0, 5)
)
tRAPi2100fREESWAPVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100fREESWAPVMMS"),
        ("VMFIX-MIB", "messagei2100fREESWAPVMMS"),
        ("VMFIX-MIB", "valuei2100fREESWAPVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100fREESWAPVMMS.setStatus(
        ""
    )

tRAPi2200fREESWAPVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2200, 0, 5)
)
tRAPi2200fREESWAPVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200fREESWAPVMMS"),
        ("VMFIX-MIB", "messagei2200fREESWAPVMMS"),
        ("VMFIX-MIB", "valuei2200fREESWAPVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200fREESWAPVMMS.setStatus(
        ""
    )

tRAPi2300fREESWAPVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2300, 0, 5)
)
tRAPi2300fREESWAPVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300fREESWAPVMMS"),
        ("VMFIX-MIB", "messagei2300fREESWAPVMMS"),
        ("VMFIX-MIB", "valuei2300fREESWAPVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300fREESWAPVMMS.setStatus(
        ""
    )

tRAPi2400fREESWAPVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 5, 2400, 0, 5)
)
tRAPi2400fREESWAPVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400fREESWAPVMMS"),
        ("VMFIX-MIB", "messagei2400fREESWAPVMMS"),
        ("VMFIX-MIB", "valuei2400fREESWAPVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400fREESWAPVMMS.setStatus(
        ""
    )

tRAPi2100eTHINTSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2100, 0, 5)
)
tRAPi2100eTHINTSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2100eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2100eTHINTSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100eTHINTSTATUSVMMS.setStatus(
        ""
    )

tRAPi2200eTHINTSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2200, 0, 5)
)
tRAPi2200eTHINTSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2200eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2200eTHINTSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200eTHINTSTATUSVMMS.setStatus(
        ""
    )

tRAPi2300eTHINTSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2300, 0, 5)
)
tRAPi2300eTHINTSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2300eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2300eTHINTSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300eTHINTSTATUSVMMS.setStatus(
        ""
    )

tRAPi2400eTHINTSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 6, 2400, 0, 5)
)
tRAPi2400eTHINTSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2400eTHINTSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2400eTHINTSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400eTHINTSTATUSVMMS.setStatus(
        ""
    )

tRAPi2100cRONSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2100, 0, 5)
)
tRAPi2100cRONSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100cRONSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2100cRONSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2100cRONSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100cRONSTATUSVMMS.setStatus(
        ""
    )

tRAPi2200cRONSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2200, 0, 5)
)
tRAPi2200cRONSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200cRONSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2200cRONSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2200cRONSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200cRONSTATUSVMMS.setStatus(
        ""
    )

tRAPi2300cRONSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2300, 0, 5)
)
tRAPi2300cRONSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300cRONSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2300cRONSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2300cRONSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300cRONSTATUSVMMS.setStatus(
        ""
    )

tRAPi2400cRONSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 7, 2400, 0, 5)
)
tRAPi2400cRONSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400cRONSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2400cRONSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2400cRONSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400cRONSTATUSVMMS.setStatus(
        ""
    )

tRAPi2100mONITSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2100, 0, 5)
)
tRAPi2100mONITSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100mONITSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2100mONITSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2100mONITSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100mONITSTATUSVMMS.setStatus(
        ""
    )

tRAPi2200mONITSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2200, 0, 5)
)
tRAPi2200mONITSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200mONITSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2200mONITSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2200mONITSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200mONITSTATUSVMMS.setStatus(
        ""
    )

tRAPi2300mONITSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2300, 0, 5)
)
tRAPi2300mONITSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300mONITSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2300mONITSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2300mONITSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300mONITSTATUSVMMS.setStatus(
        ""
    )

tRAPi2400mONITSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 8, 2400, 0, 5)
)
tRAPi2400mONITSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400mONITSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2400mONITSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2400mONITSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400mONITSTATUSVMMS.setStatus(
        ""
    )

tRAPi2100dNSMASQSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2100, 0, 5)
)
tRAPi2100dNSMASQSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2100dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2100dNSMASQSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100dNSMASQSTATUSVMMS.setStatus(
        ""
    )

tRAPi2200dNSMASQSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2200, 0, 5)
)
tRAPi2200dNSMASQSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2200dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2200dNSMASQSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200dNSMASQSTATUSVMMS.setStatus(
        ""
    )

tRAPi2300dNSMASQSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2300, 0, 5)
)
tRAPi2300dNSMASQSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2300dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2300dNSMASQSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300dNSMASQSTATUSVMMS.setStatus(
        ""
    )

tRAPi2400dNSMASQSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 9, 2400, 0, 5)
)
tRAPi2400dNSMASQSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2400dNSMASQSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2400dNSMASQSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400dNSMASQSTATUSVMMS.setStatus(
        ""
    )

tRAPi2100hB2STATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2100, 0, 5)
)
tRAPi2100hB2STATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100hB2STATUSVMMS"),
        ("VMFIX-MIB", "messagei2100hB2STATUSVMMS"),
        ("VMFIX-MIB", "valuei2100hB2STATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100hB2STATUSVMMS.setStatus(
        ""
    )

tRAPi2200hB2STATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2200, 0, 5)
)
tRAPi2200hB2STATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200hB2STATUSVMMS"),
        ("VMFIX-MIB", "messagei2200hB2STATUSVMMS"),
        ("VMFIX-MIB", "valuei2200hB2STATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200hB2STATUSVMMS.setStatus(
        ""
    )

tRAPi2300hB2STATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2300, 0, 5)
)
tRAPi2300hB2STATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300hB2STATUSVMMS"),
        ("VMFIX-MIB", "messagei2300hB2STATUSVMMS"),
        ("VMFIX-MIB", "valuei2300hB2STATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300hB2STATUSVMMS.setStatus(
        ""
    )

tRAPi2400hB2STATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 11, 2400, 0, 5)
)
tRAPi2400hB2STATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400hB2STATUSVMMS"),
        ("VMFIX-MIB", "messagei2400hB2STATUSVMMS"),
        ("VMFIX-MIB", "valuei2400hB2STATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400hB2STATUSVMMS.setStatus(
        ""
    )

tRAPi2100hB2MWDIASTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2100, 0, 5)
)
tRAPi2100hB2MWDIASTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "messagei2100hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "valuei2100hB2MWDIASTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100hB2MWDIASTATUSVMMS.setStatus(
        ""
    )

tRAPi2200hB2MWDIASTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2200, 0, 5)
)
tRAPi2200hB2MWDIASTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "messagei2200hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "valuei2200hB2MWDIASTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200hB2MWDIASTATUSVMMS.setStatus(
        ""
    )

tRAPi2300hB2MWDIASTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2300, 0, 5)
)
tRAPi2300hB2MWDIASTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "messagei2300hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "valuei2300hB2MWDIASTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300hB2MWDIASTATUSVMMS.setStatus(
        ""
    )

tRAPi2400hB2MWDIASTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 12, 2400, 0, 5)
)
tRAPi2400hB2MWDIASTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "messagei2400hB2MWDIASTATUSVMMS"),
        ("VMFIX-MIB", "valuei2400hB2MWDIASTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400hB2MWDIASTATUSVMMS.setStatus(
        ""
    )

tRAPi2100cPUSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2100, 0, 5)
)
tRAPi2100cPUSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2100cPUSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2100cPUSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2100cPUSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2100cPUSTATUSVMMS.setStatus(
        ""
    )

tRAPi2200cPUSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2200, 0, 5)
)
tRAPi2200cPUSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2200cPUSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2200cPUSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2200cPUSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2200cPUSTATUSVMMS.setStatus(
        ""
    )

tRAPi2300cPUSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2300, 0, 5)
)
tRAPi2300cPUSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2300cPUSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2300cPUSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2300cPUSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2300cPUSTATUSVMMS.setStatus(
        ""
    )

tRAPi2400cPUSTATUSVMMS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 102, 18, 2400, 0, 5)
)
tRAPi2400cPUSTATUSVMMS.setObjects(
      *(("VMFIX-MIB", "severityi2400cPUSTATUSVMMS"),
        ("VMFIX-MIB", "messagei2400cPUSTATUSVMMS"),
        ("VMFIX-MIB", "valuei2400cPUSTATUSVMMS"))
)
if mibBuilder.loadTexts:
    tRAPi2400cPUSTATUSVMMS.setStatus(
        ""
    )

tRAPi3100fREEROOTDISKVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3100, 0, 5)
)
tRAPi3100fREEROOTDISKVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100fREEROOTDISKVMDB"),
        ("VMFIX-MIB", "messagei3100fREEROOTDISKVMDB"),
        ("VMFIX-MIB", "valuei3100fREEROOTDISKVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100fREEROOTDISKVMDB.setStatus(
        ""
    )

tRAPi3200fREEROOTDISKVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3200, 0, 5)
)
tRAPi3200fREEROOTDISKVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200fREEROOTDISKVMDB"),
        ("VMFIX-MIB", "messagei3200fREEROOTDISKVMDB"),
        ("VMFIX-MIB", "valuei3200fREEROOTDISKVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200fREEROOTDISKVMDB.setStatus(
        ""
    )

tRAPi3300fREEROOTDISKVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 1, 3300, 0, 5)
)
tRAPi3300fREEROOTDISKVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300fREEROOTDISKVMDB"),
        ("VMFIX-MIB", "messagei3300fREEROOTDISKVMDB"),
        ("VMFIX-MIB", "valuei3300fREEROOTDISKVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300fREEROOTDISKVMDB.setStatus(
        ""
    )

tRAPi3100fREEBOOTDISKVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3100, 0, 5)
)
tRAPi3100fREEBOOTDISKVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100fREEBOOTDISKVMDB"),
        ("VMFIX-MIB", "messagei3100fREEBOOTDISKVMDB"),
        ("VMFIX-MIB", "valuei3100fREEBOOTDISKVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100fREEBOOTDISKVMDB.setStatus(
        ""
    )

tRAPi3200fREEBOOTDISKVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3200, 0, 5)
)
tRAPi3200fREEBOOTDISKVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200fREEBOOTDISKVMDB"),
        ("VMFIX-MIB", "messagei3200fREEBOOTDISKVMDB"),
        ("VMFIX-MIB", "valuei3200fREEBOOTDISKVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200fREEBOOTDISKVMDB.setStatus(
        ""
    )

tRAPi3300fREEBOOTDISKVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 2, 3300, 0, 5)
)
tRAPi3300fREEBOOTDISKVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300fREEBOOTDISKVMDB"),
        ("VMFIX-MIB", "messagei3300fREEBOOTDISKVMDB"),
        ("VMFIX-MIB", "valuei3300fREEBOOTDISKVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300fREEBOOTDISKVMDB.setStatus(
        ""
    )

tRAPi3100fREEMEMORYVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3100, 0, 5)
)
tRAPi3100fREEMEMORYVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100fREEMEMORYVMDB"),
        ("VMFIX-MIB", "messagei3100fREEMEMORYVMDB"),
        ("VMFIX-MIB", "valuei3100fREEMEMORYVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100fREEMEMORYVMDB.setStatus(
        ""
    )

tRAPi3200fREEMEMORYVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3200, 0, 5)
)
tRAPi3200fREEMEMORYVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200fREEMEMORYVMDB"),
        ("VMFIX-MIB", "messagei3200fREEMEMORYVMDB"),
        ("VMFIX-MIB", "valuei3200fREEMEMORYVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200fREEMEMORYVMDB.setStatus(
        ""
    )

tRAPi3300fREEMEMORYVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 3, 3300, 0, 5)
)
tRAPi3300fREEMEMORYVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300fREEMEMORYVMDB"),
        ("VMFIX-MIB", "messagei3300fREEMEMORYVMDB"),
        ("VMFIX-MIB", "valuei3300fREEMEMORYVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300fREEMEMORYVMDB.setStatus(
        ""
    )

tRAPi3100cPULOADVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3100, 0, 5)
)
tRAPi3100cPULOADVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100cPULOADVMDB"),
        ("VMFIX-MIB", "messagei3100cPULOADVMDB"),
        ("VMFIX-MIB", "valuei3100cPULOADVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100cPULOADVMDB.setStatus(
        ""
    )

tRAPi3200cPULOADVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3200, 0, 5)
)
tRAPi3200cPULOADVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200cPULOADVMDB"),
        ("VMFIX-MIB", "messagei3200cPULOADVMDB"),
        ("VMFIX-MIB", "valuei3200cPULOADVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200cPULOADVMDB.setStatus(
        ""
    )

tRAPi3300cPULOADVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 4, 3300, 0, 5)
)
tRAPi3300cPULOADVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300cPULOADVMDB"),
        ("VMFIX-MIB", "messagei3300cPULOADVMDB"),
        ("VMFIX-MIB", "valuei3300cPULOADVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300cPULOADVMDB.setStatus(
        ""
    )

tRAPi3100fREESWAPVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3100, 0, 5)
)
tRAPi3100fREESWAPVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100fREESWAPVMDB"),
        ("VMFIX-MIB", "messagei3100fREESWAPVMDB"),
        ("VMFIX-MIB", "valuei3100fREESWAPVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100fREESWAPVMDB.setStatus(
        ""
    )

tRAPi3200fREESWAPVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3200, 0, 5)
)
tRAPi3200fREESWAPVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200fREESWAPVMDB"),
        ("VMFIX-MIB", "messagei3200fREESWAPVMDB"),
        ("VMFIX-MIB", "valuei3200fREESWAPVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200fREESWAPVMDB.setStatus(
        ""
    )

tRAPi3300fREESWAPVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 5, 3300, 0, 5)
)
tRAPi3300fREESWAPVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300fREESWAPVMDB"),
        ("VMFIX-MIB", "messagei3300fREESWAPVMDB"),
        ("VMFIX-MIB", "valuei3300fREESWAPVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300fREESWAPVMDB.setStatus(
        ""
    )

tRAPi3100eTHINTSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3100, 0, 5)
)
tRAPi3100eTHINTSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100eTHINTSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3100eTHINTSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3100eTHINTSTATUSVMDBe"))
)
if mibBuilder.loadTexts:
    tRAPi3100eTHINTSTATUSVMDB.setStatus(
        ""
    )

tRAPi3200eTHINTSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3200, 0, 5)
)
tRAPi3200eTHINTSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200eTHINTSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3200eTHINTSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3200eTHINTSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200eTHINTSTATUSVMDB.setStatus(
        ""
    )

tRAPi3300eTHINTSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 6, 3300, 0, 5)
)
tRAPi3300eTHINTSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300eTHINTSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3300eTHINTSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3300eTHINTSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300eTHINTSTATUSVMDB.setStatus(
        ""
    )

tRAPi3100cRONSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3100, 0, 5)
)
tRAPi3100cRONSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100cRONSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3100cRONSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3100cRONSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100cRONSTATUSVMDB.setStatus(
        ""
    )

tRAPi3200cRONSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3200, 0, 5)
)
tRAPi3200cRONSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200cRONSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3200cRONSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3200cRONSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200cRONSTATUSVMDB.setStatus(
        ""
    )

tRAPi3300cRONSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 7, 3300, 0, 5)
)
tRAPi3300cRONSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300cRONSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3300cRONSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3300cRONSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300cRONSTATUSVMDB.setStatus(
        ""
    )

tRAPi3100mONITSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3100, 0, 5)
)
tRAPi3100mONITSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100mONITSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3100mONITSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3100mONITSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100mONITSTATUSVMDB.setStatus(
        ""
    )

tRAPi3200mONITSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3200, 0, 5)
)
tRAPi3200mONITSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200mONITSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3200mONITSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3200mONITSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200mONITSTATUSVMDB.setStatus(
        ""
    )

tRAPi3300mONITSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 8, 3300, 0, 5)
)
tRAPi3300mONITSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300mONITSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3300mONITSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3300mONITSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300mONITSTATUSVMDB.setStatus(
        ""
    )

tRAPi3100pOSTGRESSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3100, 0, 5)
)
tRAPi3100pOSTGRESSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100pOSTGRESSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3100pOSTGRESSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3100pOSTGRESSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100pOSTGRESSTATUSVMDB.setStatus(
        ""
    )

tRAPi3200pOSTGRESSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3200, 0, 5)
)
tRAPi3200pOSTGRESSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200pOSTGRESSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3200pOSTGRESSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3200pOSTGRESSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200pOSTGRESSTATUSVMDB.setStatus(
        ""
    )

tRAPi3300pOSTGRESSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 15, 3300, 0, 5)
)
tRAPi3300pOSTGRESSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300pOSTGRESSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3300pOSTGRESSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3300pOSTGRESSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300pOSTGRESSTATUSVMDB.setStatus(
        ""
    )

tRAPi3100pGPOOLSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3100, 0, 5)
)
tRAPi3100pGPOOLSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100pGPOOLSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3100pGPOOLSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3100pGPOOLSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100pGPOOLSTATUSVMDB.setStatus(
        ""
    )

tRAPi3200pGPOOLSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3200, 0, 5)
)
tRAPi3200pGPOOLSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200pGPOOLSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3200pGPOOLSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3200pGPOOLSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200pGPOOLSTATUSVMDB.setStatus(
        ""
    )

tRAPi3300pGPOOLSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 16, 3300, 0, 5)
)
tRAPi3300pGPOOLSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300pGPOOLSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3300pGPOOLSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3300pGPOOLSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300pGPOOLSTATUSVMDB.setStatus(
        ""
    )

tRAPi3100pGAGENTSATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3100, 0, 5)
)
tRAPi3100pGAGENTSATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100pGAGENTSATUSVMDB"),
        ("VMFIX-MIB", "messagei3100pGAGENTSATUSVMDB"),
        ("VMFIX-MIB", "valuei3100pGAGENTSATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100pGAGENTSATUSVMDB.setStatus(
        ""
    )

tRAPi3200pGAGENTSATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3200, 0, 5)
)
tRAPi3200pGAGENTSATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200pGAGENTSATUSVMDB"),
        ("VMFIX-MIB", "messagei3200pGAGENTSATUSVMDB"),
        ("VMFIX-MIB", "valuei3200pGAGENTSATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200pGAGENTSATUSVMDB.setStatus(
        ""
    )

tRAPi3300pGAGENTSATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 17, 3300, 0, 5)
)
tRAPi3300pGAGENTSATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300pGAGENTSATUSVMDB"),
        ("VMFIX-MIB", "messagei3300pGAGENTSATUSVMDB"),
        ("VMFIX-MIB", "valuei3300pGAGENTSATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300pGAGENTSATUSVMDB.setStatus(
        ""
    )

tRAPi3100cPUSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3100, 0, 5)
)
tRAPi3100cPUSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3100cPUSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3100cPUSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3100cPUSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3100cPUSTATUSVMDB.setStatus(
        ""
    )

tRAPi3200cPUSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3200, 0, 5)
)
tRAPi3200cPUSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3200cPUSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3200cPUSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3200cPUSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3200cPUSTATUSVMDB.setStatus(
        ""
    )

tRAPi3300cPUSTATUSVMDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 103, 18, 3300, 0, 5)
)
tRAPi3300cPUSTATUSVMDB.setObjects(
      *(("VMFIX-MIB", "severityi3300cPUSTATUSVMDB"),
        ("VMFIX-MIB", "messagei3300cPUSTATUSVMDB"),
        ("VMFIX-MIB", "valuei3300cPUSTATUSVMDB"))
)
if mibBuilder.loadTexts:
    tRAPi3300cPUSTATUSVMDB.setStatus(
        ""
    )

tRAPi4100fREEROOTDISKVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4100, 0, 5)
)
tRAPi4100fREEROOTDISKVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100fREEROOTDISKVMIC"),
        ("VMFIX-MIB", "messagei4100fREEROOTDISKVMIC"),
        ("VMFIX-MIB", "valuei4100fREEROOTDISKVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100fREEROOTDISKVMIC.setStatus(
        ""
    )

tRAPi4200fREEROOTDISKVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4200, 0, 5)
)
tRAPi4200fREEROOTDISKVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200fREEROOTDISKVMIC"),
        ("VMFIX-MIB", "messagei4200fREEROOTDISKVMIC"),
        ("VMFIX-MIB", "valuei4200fREEROOTDISKVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200fREEROOTDISKVMIC.setStatus(
        ""
    )

tRAPi4300fREEROOTDISKVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 1, 4300, 0, 5)
)
tRAPi4300fREEROOTDISKVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300fREEROOTDISKVMIC"),
        ("VMFIX-MIB", "messagei4300fREEROOTDISKVMIC"),
        ("VMFIX-MIB", "valuei4300fREEROOTDISKVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300fREEROOTDISKVMIC.setStatus(
        ""
    )

tRAPi4100fREEBOOTDISKVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4100, 0, 5)
)
tRAPi4100fREEBOOTDISKVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100fREEBOOTDISKVMIC"),
        ("VMFIX-MIB", "messagei4100fREEBOOTDISKVMIC"),
        ("VMFIX-MIB", "valuei4100fREEBOOTDISKVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100fREEBOOTDISKVMIC.setStatus(
        ""
    )

tRAPi4200fREEBOOTDISKVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4200, 0, 5)
)
tRAPi4200fREEBOOTDISKVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200fREEBOOTDISKVMIC"),
        ("VMFIX-MIB", "messagei4200fREEBOOTDISKVMIC"),
        ("VMFIX-MIB", "valuei4200fREEBOOTDISKVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200fREEBOOTDISKVMIC.setStatus(
        ""
    )

tRAPi4300fREEBOOTDISKVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 2, 4300, 0, 5)
)
tRAPi4300fREEBOOTDISKVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300fREEBOOTDISKVMIC"),
        ("VMFIX-MIB", "messagei4300fREEBOOTDISKVMIC"),
        ("VMFIX-MIB", "valuei4300fREEBOOTDISKVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300fREEBOOTDISKVMIC.setStatus(
        ""
    )

tRAPi4100fREEMEMORYVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4100, 0, 5)
)
tRAPi4100fREEMEMORYVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100fREEMEMORYVMIC"),
        ("VMFIX-MIB", "messagei4100fREEMEMORYVMIC"),
        ("VMFIX-MIB", "valuei4100fREEMEMORYVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100fREEMEMORYVMIC.setStatus(
        ""
    )

tRAPi4200fREEMEMORYVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4200, 0, 5)
)
tRAPi4200fREEMEMORYVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200fREEMEMORYVMIC"),
        ("VMFIX-MIB", "messagei4200fREEMEMORYVMIC"),
        ("VMFIX-MIB", "valuei4200fREEMEMORYVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200fREEMEMORYVMIC.setStatus(
        ""
    )

tRAPi4300fREEMEMORYVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 3, 4300, 0, 5)
)
tRAPi4300fREEMEMORYVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300fREEMEMORYVMIC"),
        ("VMFIX-MIB", "messagei4300fREEMEMORYVMIC"),
        ("VMFIX-MIB", "valuei4300fREEMEMORYVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300fREEMEMORYVMIC.setStatus(
        ""
    )

tRAPi4100cPULOADVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4100, 0, 5)
)
tRAPi4100cPULOADVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100cPULOADVMIC"),
        ("VMFIX-MIB", "messagei4100cPULOADVMIC"),
        ("VMFIX-MIB", "valuei4100cPULOADVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100cPULOADVMIC.setStatus(
        ""
    )

tRAPi4200cPULOADVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4200, 0, 5)
)
tRAPi4200cPULOADVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200cPULOADVMIC"),
        ("VMFIX-MIB", "messagei4200cPULOADVMIC"),
        ("VMFIX-MIB", "valuei4200cPULOADVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200cPULOADVMIC.setStatus(
        ""
    )

tRAPi4300cPULOADVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 4, 4300, 0, 5)
)
tRAPi4300cPULOADVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300cPULOADVMIC"),
        ("VMFIX-MIB", "messagei4300cPULOADVMIC"),
        ("VMFIX-MIB", "valuei4300cPULOADVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300cPULOADVMIC.setStatus(
        ""
    )

tRAPi4100fREESWAPVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4100, 0, 5)
)
tRAPi4100fREESWAPVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100fREESWAPVMIC"),
        ("VMFIX-MIB", "messagei4100fREESWAPVMIC"),
        ("VMFIX-MIB", "valuei4100fREESWAPVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100fREESWAPVMIC.setStatus(
        ""
    )

tRAPi4200fREESWAPVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4200, 0, 5)
)
tRAPi4200fREESWAPVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200fREESWAPVMIC"),
        ("VMFIX-MIB", "messagei4200fREESWAPVMIC"),
        ("VMFIX-MIB", "valuei4200fREESWAPVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200fREESWAPVMIC.setStatus(
        ""
    )

tRAPi4300fREESWAPVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 5, 4300, 0, 5)
)
tRAPi4300fREESWAPVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300fREESWAPVMIC"),
        ("VMFIX-MIB", "messagei4300fREESWAPVMIC"),
        ("VMFIX-MIB", "valuei4300fREESWAPVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300fREESWAPVMIC.setStatus(
        ""
    )

tRAPi4100eTHINTSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4100, 0, 5)
)
tRAPi4100eTHINTSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100eTHINTSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4100eTHINTSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4100eTHINTSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100eTHINTSTATUSVMIC.setStatus(
        ""
    )

tRAPi4200eTHINTSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4200, 0, 5)
)
tRAPi4200eTHINTSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200eTHINTSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4200eTHINTSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4200eTHINTSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200eTHINTSTATUSVMIC.setStatus(
        ""
    )

tRAPi4300eTHINTSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 6, 4300, 0, 5)
)
tRAPi4300eTHINTSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300eTHINTSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4300eTHINTSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4300eTHINTSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300eTHINTSTATUSVMIC.setStatus(
        ""
    )

tRAPi4100cRONSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4100, 0, 5)
)
tRAPi4100cRONSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100cRONSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4100cRONSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4100cRONSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100cRONSTATUSVMIC.setStatus(
        ""
    )

tRAPi4200cRONSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4200, 0, 5)
)
tRAPi4200cRONSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200cRONSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4200cRONSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4200cRONSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200cRONSTATUSVMIC.setStatus(
        ""
    )

tRAPi4300cRONSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 7, 4300, 0, 5)
)
tRAPi4300cRONSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300cRONSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4300cRONSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4300cRONSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300cRONSTATUSVMIC.setStatus(
        ""
    )

tRAPi4100mONITSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4100, 0, 5)
)
tRAPi4100mONITSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100mONITSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4100mONITSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4100mONITSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100mONITSTATUSVMIC.setStatus(
        ""
    )

tRAPi4200mONITSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4200, 0, 5)
)
tRAPi4200mONITSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200mONITSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4200mONITSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4200mONITSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200mONITSTATUSVMIC.setStatus(
        ""
    )

tRAPi4300mONITSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 8, 4300, 0, 5)
)
tRAPi4300mONITSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300mONITSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4300mONITSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4300mONITSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300mONITSTATUSVMIC.setStatus(
        ""
    )

tRAPi4100cPUSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4100, 0, 5)
)
tRAPi4100cPUSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100cPUSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4100cPUSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4100cPUSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4100cPUSTATUSVMIC.setStatus(
        ""
    )

tRAPi4200cPUSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4200, 0, 5)
)
tRAPi4200cPUSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200cPUSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4200cPUSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4200cPUSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200cPUSTATUSVMIC.setStatus(
        ""
    )

tRAPi4300cPUSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 18, 4300, 0, 5)
)
tRAPi4300cPUSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300cPUSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4300cPUSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4300cPUSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300cPUSTATUSVMIC.setStatus(
        ""
    )

trapi4100vMPANELSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4100, 0, 5)
)
trapi4100vMPANELSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4100vMPANELSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4100vMPANELSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4100vMPANELSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    trapi4100vMPANELSTATUSVMIC.setStatus(
        ""
    )

tRAPi4200vMPANELSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4200, 0, 5)
)
tRAPi4200vMPANELSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4200vMPANELSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4200vMPANELSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4200vMPANELSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4200vMPANELSTATUSVMIC.setStatus(
        ""
    )

tRAPi4300vMPANELSTATUSVMIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 104, 21, 4300, 0, 5)
)
tRAPi4300vMPANELSTATUSVMIC.setObjects(
      *(("VMFIX-MIB", "severityi4300vMPANELSTATUSVMIC"),
        ("VMFIX-MIB", "messagei4300vMPANELSTATUSVMIC"),
        ("VMFIX-MIB", "valuei4300vMPANELSTATUSVMIC"))
)
if mibBuilder.loadTexts:
    tRAPi4300vMPANELSTATUSVMIC.setStatus(
        ""
    )

tRAPi5100fREEROOTDISKVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5100, 0, 5)
)
tRAPi5100fREEROOTDISKVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100fREEROOTDISKVMLVS"),
        ("VMFIX-MIB", "messagei5100fREEROOTDISKVMLVS"),
        ("VMFIX-MIB", "valuei5100fREEROOTDISKVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100fREEROOTDISKVMLVS.setStatus(
        ""
    )

tRAPi5200fREEROOTDISKVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 1, 5200, 0, 5)
)
tRAPi5200fREEROOTDISKVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200fREEROOTDISKVMLVS"),
        ("VMFIX-MIB", "messagei5200fREEROOTDISKVMLVS"),
        ("VMFIX-MIB", "valuei5200fREEROOTDISKVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200fREEROOTDISKVMLVS.setStatus(
        ""
    )

tRAPi5100fREEBOOTDISKVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5100, 0, 5)
)
tRAPi5100fREEBOOTDISKVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100fREEBOOTDISKVMLVS"),
        ("VMFIX-MIB", "messagei5100fREEBOOTDISKVMLVS"),
        ("VMFIX-MIB", "valuei5100fREEBOOTDISKVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100fREEBOOTDISKVMLVS.setStatus(
        ""
    )

tRAPi5200fREEBOOTDISKVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 2, 5200, 0, 5)
)
tRAPi5200fREEBOOTDISKVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200fREEBOOTDISKVMLVS"),
        ("VMFIX-MIB", "messagei5200fREEBOOTDISKVMLVS"),
        ("VMFIX-MIB", "valuei5200fREEBOOTDISKVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200fREEBOOTDISKVMLVS.setStatus(
        ""
    )

tRAPi5100fREEMEMORYVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5100, 0, 5)
)
tRAPi5100fREEMEMORYVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100fREEMEMORYVMLVS"),
        ("VMFIX-MIB", "messagei5100fREEMEMORYVMLVS"),
        ("VMFIX-MIB", "valuei5100fREEMEMORYVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100fREEMEMORYVMLVS.setStatus(
        ""
    )

tRAPi5200fREEMEMORYVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 3, 5200, 0, 5)
)
tRAPi5200fREEMEMORYVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200fREEMEMORYVMLVS"),
        ("VMFIX-MIB", "messagei5200fREEMEMORYVMLVS"),
        ("VMFIX-MIB", "valuei5200fREEMEMORYVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200fREEMEMORYVMLVS.setStatus(
        ""
    )

tRAPi5100cPULOADVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5100, 0, 5)
)
tRAPi5100cPULOADVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100cPULOADVMLVS"),
        ("VMFIX-MIB", "messagei5100cPULOADVMLVS"),
        ("VMFIX-MIB", "valuei5100cPULOADVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100cPULOADVMLVS.setStatus(
        ""
    )

tRAPi5200cPULOADVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 4, 5200, 0, 5)
)
tRAPi5200cPULOADVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200cPULOADVMLVS"),
        ("VMFIX-MIB", "messagei5200cPULOADVMLVS"),
        ("VMFIX-MIB", "valuei5200cPULOADVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200cPULOADVMLVS.setStatus(
        ""
    )

tRAPi5100fREESWAPVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5100, 0, 5)
)
tRAPi5100fREESWAPVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100fREESWAPVMLVS"),
        ("VMFIX-MIB", "messagei5100fREESWAPVMLVS"),
        ("VMFIX-MIB", "valuei5100fREESWAPVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100fREESWAPVMLVS.setStatus(
        ""
    )

tRAPi5200fREESWAPVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 5, 5200, 0, 5)
)
tRAPi5200fREESWAPVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200fREESWAPVMLVS"),
        ("VMFIX-MIB", "messagei5200fREESWAPVMLVS"),
        ("VMFIX-MIB", "valuei5200fREESWAPVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200fREESWAPVMLVS.setStatus(
        ""
    )

tRAPi5100eTHINTSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5100, 0, 5)
)
tRAPi5100eTHINTSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100eTHINTSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5100eTHINTSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5100eTHINTSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100eTHINTSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5200eTHINTSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 6, 5200, 0, 5)
)
tRAPi5200eTHINTSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200eTHINTSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5200eTHINTSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5200eTHINTSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200eTHINTSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5100cRONSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5100, 0, 5)
)
tRAPi5100cRONSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100cRONSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5100cRONSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5100cRONSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100cRONSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5200cRONSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 7, 5200, 0, 5)
)
tRAPi5200cRONSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200cRONSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5200cRONSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5200cRONSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200cRONSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5100mONITSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5100, 0, 5)
)
tRAPi5100mONITSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100mONITSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5100mONITSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5100mONITSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100mONITSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5200mONITSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 8, 5200, 0, 5)
)
tRAPi5200mONITSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200mONITSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5200mONITSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5200mONITSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200mONITSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5100pULSESTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5100, 0, 5)
)
tRAPi5100pULSESTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100pULSESTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5100pULSESTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5100pULSESTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100pULSESTATUSVMLVS.setStatus(
        ""
    )

tRAPi5200pULSESTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 10, 5200, 0, 5)
)
tRAPi5200pULSESTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200pULSESTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5200pULSESTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5200pULSESTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200pULSESTATUSVMLVS.setStatus(
        ""
    )

tRAPi5100cPUSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5100, 0, 5)
)
tRAPi5100cPUSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100cPUSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5100cPUSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5100cPUSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100cPUSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5200cPUSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 18, 5200, 0, 5)
)
tRAPi5200cPUSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200cPUSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5200cPUSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5200cPUSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200cPUSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5100lVSSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5100, 0, 5)
)
tRAPi5100lVSSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5100lVSSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5100lVSSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5100lVSSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5100lVSSTATUSVMLVS.setStatus(
        ""
    )

tRAPi5200lVSSTATUSVMLVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 44039, 105, 22, 5200, 0, 5)
)
tRAPi5200lVSSTATUSVMLVS.setObjects(
      *(("VMFIX-MIB", "severityi5200lVSSTATUSVMLVS"),
        ("VMFIX-MIB", "messagei5200lVSSTATUSVMLVS"),
        ("VMFIX-MIB", "valuei5200lVSSTATUSVMLVS"))
)
if mibBuilder.loadTexts:
    tRAPi5200lVSSTATUSVMLVS.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMFIX-MIB",
    **{"windMobile": windMobile,
       "vmas": vmas,
       "fREEROOTDISKVMAS": fREEROOTDISKVMAS,
       "i1100fREEROOTDISKVMAS": i1100fREEROOTDISKVMAS,
       "severityi1100fREEROOTDISKVMAS": severityi1100fREEROOTDISKVMAS,
       "messagei1100fREEROOTDISKVMAS": messagei1100fREEROOTDISKVMAS,
       "valuei1100fREEROOTDISKVMAS": valuei1100fREEROOTDISKVMAS,
       "i1101fREEROOTDISKVMASV1": i1101fREEROOTDISKVMASV1,
       "tRAPi1101fREEROOTDISKVMAS": tRAPi1101fREEROOTDISKVMAS,
       "i1200fREEROOTDISKVMAS": i1200fREEROOTDISKVMAS,
       "tRAPi1200fREEROOTDISKVMAS": tRAPi1200fREEROOTDISKVMAS,
       "severityi1200fREEROOTDISKVMAS": severityi1200fREEROOTDISKVMAS,
       "messagei1200fREEROOTDISKVMAS": messagei1200fREEROOTDISKVMAS,
       "valuei1200fREEROOTDISKVMAS": valuei1200fREEROOTDISKVMAS,
       "i1300fREEROOTDISKVMAS": i1300fREEROOTDISKVMAS,
       "tRAPi1300fREEROOTDISKVMAS": tRAPi1300fREEROOTDISKVMAS,
       "severityi1300fREEROOTDISKVMAS": severityi1300fREEROOTDISKVMAS,
       "messagei1300fREEROOTDISKVMAS": messagei1300fREEROOTDISKVMAS,
       "valuei1300fREEROOTDISKVMAS": valuei1300fREEROOTDISKVMAS,
       "fREEBOOTDISKVMAS": fREEBOOTDISKVMAS,
       "i1100fREEBOOTDISKVMAS": i1100fREEBOOTDISKVMAS,
       "tRAPi1100fREEBOOTDISKVMAS": tRAPi1100fREEBOOTDISKVMAS,
       "severityi1100fREEBOOTDISKVMAS": severityi1100fREEBOOTDISKVMAS,
       "messagei1100fREEBOOTDISKVMAS": messagei1100fREEBOOTDISKVMAS,
       "valuei1100fREEBOOTDISKVMAS": valuei1100fREEBOOTDISKVMAS,
       "i1200fREEBOOTDISKVMAS": i1200fREEBOOTDISKVMAS,
       "tRAPi1200fREEBOOTDISKVMAS": tRAPi1200fREEBOOTDISKVMAS,
       "severityi1200fREEBOOTDISKVMAS": severityi1200fREEBOOTDISKVMAS,
       "messagei1200fREEBOOTDISKVMAS": messagei1200fREEBOOTDISKVMAS,
       "valuei1200fREEBOOTDISKVMAS": valuei1200fREEBOOTDISKVMAS,
       "i1300fREEBOOTDISKVMAS": i1300fREEBOOTDISKVMAS,
       "tRAPi1300fREEBOOTDISKVMAS": tRAPi1300fREEBOOTDISKVMAS,
       "severityi1300fREEBOOTDISKVMAS": severityi1300fREEBOOTDISKVMAS,
       "messagei1300fREEBOOTDISKVMAS": messagei1300fREEBOOTDISKVMAS,
       "valuei1300fREEBOOTDISKVMAS": valuei1300fREEBOOTDISKVMAS,
       "fREEMEMORYVMAS": fREEMEMORYVMAS,
       "i1100fREEMEMORYVMAS": i1100fREEMEMORYVMAS,
       "tRAPi1100fREEMEMORYVMAS": tRAPi1100fREEMEMORYVMAS,
       "severityi1100fREEMEMORYVMAS": severityi1100fREEMEMORYVMAS,
       "messagei1100fREEMEMORYVMAS": messagei1100fREEMEMORYVMAS,
       "valuei1100fREEMEMORYVMAS": valuei1100fREEMEMORYVMAS,
       "i1200fREEMEMORYVMAS": i1200fREEMEMORYVMAS,
       "tRAPi1200fREEMEMORYVMAS": tRAPi1200fREEMEMORYVMAS,
       "severityi1200fREEMEMORYVMAS": severityi1200fREEMEMORYVMAS,
       "messagei1200fREEMEMORYVMAS": messagei1200fREEMEMORYVMAS,
       "valuei1200fREEMEMORYVMAS": valuei1200fREEMEMORYVMAS,
       "i1300fREEMEMORYVMAS": i1300fREEMEMORYVMAS,
       "tRAPi1300fREEMEMORYVMAS": tRAPi1300fREEMEMORYVMAS,
       "severityi1300fREEMEMORYVMAS": severityi1300fREEMEMORYVMAS,
       "messagei1300fREEMEMORYVMAS": messagei1300fREEMEMORYVMAS,
       "valuei1300fREEMEMORYVMAS": valuei1300fREEMEMORYVMAS,
       "cPULOADVMAS": cPULOADVMAS,
       "i1100cPULOADVMAS": i1100cPULOADVMAS,
       "tRAPi1100cPULOADVMAS": tRAPi1100cPULOADVMAS,
       "severityi1100cPULOADVMAS": severityi1100cPULOADVMAS,
       "messagei1100cPULOADVMAS": messagei1100cPULOADVMAS,
       "valuei1100cPULOADVMAS": valuei1100cPULOADVMAS,
       "i1200cPULOADVMAS": i1200cPULOADVMAS,
       "tRAPi1200cPULOADVMAS": tRAPi1200cPULOADVMAS,
       "severityi1200cPULOADVMAS": severityi1200cPULOADVMAS,
       "messagei1200cPULOADVMAS": messagei1200cPULOADVMAS,
       "valuei1200cPULOADVMAS": valuei1200cPULOADVMAS,
       "i1300cPULOADVMAS": i1300cPULOADVMAS,
       "tRAPi1300cPULOADVMAS": tRAPi1300cPULOADVMAS,
       "severityi1300cPULOADVMAS": severityi1300cPULOADVMAS,
       "messagei1300cPULOADVMAS": messagei1300cPULOADVMAS,
       "valuei1300cPULOADVMAS": valuei1300cPULOADVMAS,
       "fREESWAPVMAS": fREESWAPVMAS,
       "i1100fREESWAPVMAS": i1100fREESWAPVMAS,
       "tRAPi1100fREESWAPVMAS": tRAPi1100fREESWAPVMAS,
       "severityi1100fREESWAPVMAS": severityi1100fREESWAPVMAS,
       "messagei1100fREESWAPVMAS": messagei1100fREESWAPVMAS,
       "valuei1100fREESWAPVMAS": valuei1100fREESWAPVMAS,
       "i1200fREESWAPVMAS": i1200fREESWAPVMAS,
       "tRAPi1200fREESWAPVMAS": tRAPi1200fREESWAPVMAS,
       "severityi1200fREESWAPVMAS": severityi1200fREESWAPVMAS,
       "messagei1200fREESWAPVMAS": messagei1200fREESWAPVMAS,
       "valuei1200fREESWAPVMAS": valuei1200fREESWAPVMAS,
       "i1300fREESWAPVMAS": i1300fREESWAPVMAS,
       "tRAPi1300fREESWAPVMAS": tRAPi1300fREESWAPVMAS,
       "severityi1300fREESWAPVMAS": severityi1300fREESWAPVMAS,
       "messagei1300fREESWAPVMAS": messagei1300fREESWAPVMAS,
       "valuei1300fREESWAPVMAS": valuei1300fREESWAPVMAS,
       "eTHINTSTATUSVMAS": eTHINTSTATUSVMAS,
       "i1100eTHINTSTATUSVMAS": i1100eTHINTSTATUSVMAS,
       "tRAPi1100eTHINTSTATUSVMAS": tRAPi1100eTHINTSTATUSVMAS,
       "severityi1100eTHINTSTATUSVMAS": severityi1100eTHINTSTATUSVMAS,
       "messagei1100eTHINTSTATUSVMAS": messagei1100eTHINTSTATUSVMAS,
       "valuei1100eTHINTSTATUSVMAS": valuei1100eTHINTSTATUSVMAS,
       "i1200eTHINTSTATUSVMAS": i1200eTHINTSTATUSVMAS,
       "tRAPi1200eTHINTSTATUSVMAS": tRAPi1200eTHINTSTATUSVMAS,
       "severityi1200eTHINTSTATUSVMAS": severityi1200eTHINTSTATUSVMAS,
       "messagei1200eTHINTSTATUSVMAS": messagei1200eTHINTSTATUSVMAS,
       "valuei1200eTHINTSTATUSVMAS": valuei1200eTHINTSTATUSVMAS,
       "i1300eTHINTSTATUSVMAS": i1300eTHINTSTATUSVMAS,
       "tRAPi1300eTHINTSTATUSVMAS": tRAPi1300eTHINTSTATUSVMAS,
       "severityi1300eTHINTSTATUSVMAS": severityi1300eTHINTSTATUSVMAS,
       "messagei1300eTHINTSTATUSVMAS": messagei1300eTHINTSTATUSVMAS,
       "valuei1300eTHINTSTATUSVMAS": valuei1300eTHINTSTATUSVMAS,
       "cRONSTATUSVMAS": cRONSTATUSVMAS,
       "i1100cRONSTATUSVMAS": i1100cRONSTATUSVMAS,
       "tRAPi1100cRONSTATUSVMAS": tRAPi1100cRONSTATUSVMAS,
       "severityi1100cRONSTATUSVMAS": severityi1100cRONSTATUSVMAS,
       "messagei1100cRONSTATUSVMAS": messagei1100cRONSTATUSVMAS,
       "valuei1100cRONSTATUSVMAS": valuei1100cRONSTATUSVMAS,
       "i1200cRONSTATUSVMAS": i1200cRONSTATUSVMAS,
       "tRAPi1200cRONSTATUSVMAS": tRAPi1200cRONSTATUSVMAS,
       "severityi1200cRONSTATUSVMAS": severityi1200cRONSTATUSVMAS,
       "messagei1200cRONSTATUSVMAS": messagei1200cRONSTATUSVMAS,
       "valuei1200cRONSTATUSVMAS": valuei1200cRONSTATUSVMAS,
       "i1300cRONSTATUSVMAS": i1300cRONSTATUSVMAS,
       "tRAPi1300cRONSTATUSVMAS": tRAPi1300cRONSTATUSVMAS,
       "severityi1300cRONSTATUSVMAS": severityi1300cRONSTATUSVMAS,
       "messagei1300cRONSTATUSVMAS": messagei1300cRONSTATUSVMAS,
       "valuei1300cRONSTATUSVMAS": valuei1300cRONSTATUSVMAS,
       "mONITSTATUSVMAS": mONITSTATUSVMAS,
       "i1100mONITSTATUSVMAS": i1100mONITSTATUSVMAS,
       "tRAPi1100mONITSTATUSVMAS": tRAPi1100mONITSTATUSVMAS,
       "severityi1100mONITSTATUSVMAS": severityi1100mONITSTATUSVMAS,
       "messagei1100mONITSTATUSVMAS": messagei1100mONITSTATUSVMAS,
       "valuei1100mONITSTATUSVMAS": valuei1100mONITSTATUSVMAS,
       "i1200mONITSTATUSVMAS": i1200mONITSTATUSVMAS,
       "tRAPi1200mONITSTATUSVMAS": tRAPi1200mONITSTATUSVMAS,
       "severityi1200mONITSTATUSVMAS": severityi1200mONITSTATUSVMAS,
       "messagei1200mONITSTATUSVMAS": messagei1200mONITSTATUSVMAS,
       "valuei1200mONITSTATUSVMAS": valuei1200mONITSTATUSVMAS,
       "i1300mONITSTATUSVMAS": i1300mONITSTATUSVMAS,
       "tRAPi1300mONITSTATUSVMAS": tRAPi1300mONITSTATUSVMAS,
       "severityi1300mONITSTATUSVMAS": severityi1300mONITSTATUSVMAS,
       "messagei1300mONITSTATUSVMAS": messagei1300mONITSTATUSVMAS,
       "valuei1300mONITSTATUSVMAS": valuei1300mONITSTATUSVMAS,
       "dNSMASQSTATUSVMAS": dNSMASQSTATUSVMAS,
       "i1100dNSMASQSTATUSVMAS": i1100dNSMASQSTATUSVMAS,
       "tRAPi1100dNSMASQSTATUSVMAS": tRAPi1100dNSMASQSTATUSVMAS,
       "severityi1100dNSMASQSTATUSVMAS": severityi1100dNSMASQSTATUSVMAS,
       "messagei1100dNSMASQSTATUSVMAS": messagei1100dNSMASQSTATUSVMAS,
       "valuei1100dNSMASQSTATUSVMAS": valuei1100dNSMASQSTATUSVMAS,
       "i1200dNSMASQSTATUSVMAS": i1200dNSMASQSTATUSVMAS,
       "tRAPi1200dNSMASQSTATUSVMAS": tRAPi1200dNSMASQSTATUSVMAS,
       "severityi1200dNSMASQSTATUSVMAS": severityi1200dNSMASQSTATUSVMAS,
       "messagei1200dNSMASQSTATUSVMAS": messagei1200dNSMASQSTATUSVMAS,
       "valuei1200dNSMASQSTATUSVMAS": valuei1200dNSMASQSTATUSVMAS,
       "i1300dNSMASQSTATUSVMAS": i1300dNSMASQSTATUSVMAS,
       "tRAPi1300dNSMASQSTATUSVMAS": tRAPi1300dNSMASQSTATUSVMAS,
       "severityi1300dNSMASQSTATUSVMAS": severityi1300dNSMASQSTATUSVMAS,
       "messagei1300dNSMASQSTATUSVMAS": messagei1300dNSMASQSTATUSVMAS,
       "valuei1300dNSMASQSTATUSVMAS": valuei1300dNSMASQSTATUSVMAS,
       "hB2STATUSVMAS": hB2STATUSVMAS,
       "i1100hB2STATUSVMAS": i1100hB2STATUSVMAS,
       "tRAPi1100hB2STATUSVMAS": tRAPi1100hB2STATUSVMAS,
       "severityi1100hB2STATUSVMAS": severityi1100hB2STATUSVMAS,
       "messagei1100hB2STATUSVMAS": messagei1100hB2STATUSVMAS,
       "valuei1100hB2STATUSVMAS": valuei1100hB2STATUSVMAS,
       "i1200hB2STATUSVMAS": i1200hB2STATUSVMAS,
       "tRAPi1200hB2STATUSVMAS": tRAPi1200hB2STATUSVMAS,
       "severityi1200hB2STATUSVMAS": severityi1200hB2STATUSVMAS,
       "messagei1200hB2STATUSVMAS": messagei1200hB2STATUSVMAS,
       "valuei1200hB2STATUSVMAS": valuei1200hB2STATUSVMAS,
       "i1300hB2STATUSVMAS": i1300hB2STATUSVMAS,
       "tRAPi1300hB2STATUSVMAS": tRAPi1300hB2STATUSVMAS,
       "severityi1300hB2STATUSVMAS": severityi1300hB2STATUSVMAS,
       "messagei1300hB2STATUSVMAS": messagei1300hB2STATUSVMAS,
       "valuei1300hB2STATUSVMAS": valuei1300hB2STATUSVMAS,
       "tOMCATSTATUSVMAS": tOMCATSTATUSVMAS,
       "i1100tOMCATSTATUSVMAS": i1100tOMCATSTATUSVMAS,
       "tRAPi1100tOMCATSTATUSVMAS": tRAPi1100tOMCATSTATUSVMAS,
       "severityi1100tOMCATSTATUSVMAS": severityi1100tOMCATSTATUSVMAS,
       "messagei1100tOMCATSTATUSVMAS": messagei1100tOMCATSTATUSVMAS,
       "valuei1100tOMCATSTATUSVMAS": valuei1100tOMCATSTATUSVMAS,
       "i1200tOMCATSTATUSVMAS": i1200tOMCATSTATUSVMAS,
       "tRAPi1200tOMCATSTATUSVMAS": tRAPi1200tOMCATSTATUSVMAS,
       "severityi1200tOMCATSTATUSVMAS": severityi1200tOMCATSTATUSVMAS,
       "messagei1200tOMCATSTATUSVMAS": messagei1200tOMCATSTATUSVMAS,
       "valuei1200tOMCATSTATUSVMAS": valuei1200tOMCATSTATUSVMAS,
       "i1300tOMCATSTATUSVMAS": i1300tOMCATSTATUSVMAS,
       "tRAPi1300tOMCATSTATUSVMAS": tRAPi1300tOMCATSTATUSVMAS,
       "severityi1300tOMCATSTATUSVMAS": severityi1300tOMCATSTATUSVMAS,
       "messagei1300tOMCATSTATUSVMAS": messagei1300tOMCATSTATUSVMAS,
       "valuei1300tOMCATSTATUSVMAS": valuei1300tOMCATSTATUSVMAS,
       "cPUSTATUSVMAS": cPUSTATUSVMAS,
       "i1100cPUSTATUSVMAS": i1100cPUSTATUSVMAS,
       "tRAPi1100cPUSTATUSVMAS": tRAPi1100cPUSTATUSVMAS,
       "severityi1100cPUSTATUSVMAS": severityi1100cPUSTATUSVMAS,
       "messagei1100cPUSTATUSVMAS": messagei1100cPUSTATUSVMAS,
       "valuei1100cPUSTATUSVMAS": valuei1100cPUSTATUSVMAS,
       "i1200cPUSTATUSVMAS": i1200cPUSTATUSVMAS,
       "tRAPi1200cPUSTATUSVMAS": tRAPi1200cPUSTATUSVMAS,
       "severityi1200cPUSTATUSVMAS": severityi1200cPUSTATUSVMAS,
       "messagei1200cPUSTATUSVMAS": messagei1200cPUSTATUSVMAS,
       "valuei1200cPUSTATUSVMAS": valuei1200cPUSTATUSVMAS,
       "i1300cPUSTATUSVMAS": i1300cPUSTATUSVMAS,
       "tRAPi1300cPUSTATUSVMAS": tRAPi1300cPUSTATUSVMAS,
       "severityi1300cPUSTATUSVMAS": severityi1300cPUSTATUSVMAS,
       "messagei1300cPUSTATUSVMAS": messagei1300cPUSTATUSVMAS,
       "valuei1300cPUSTATUSVMAS": valuei1300cPUSTATUSVMAS,
       "vMCORESTATUSVMAS": vMCORESTATUSVMAS,
       "i1100vMCORESTATUSVMAS": i1100vMCORESTATUSVMAS,
       "tRAPi1100vMCORESTATUSVMAS": tRAPi1100vMCORESTATUSVMAS,
       "severityi1100vMCORESTATUSVMAS": severityi1100vMCORESTATUSVMAS,
       "messagei1100vMCORESTATUSVMAS": messagei1100vMCORESTATUSVMAS,
       "valuei1100vMCORESTATUSVMAS": valuei1100vMCORESTATUSVMAS,
       "i1200vMCORESTATUSVMAS": i1200vMCORESTATUSVMAS,
       "tRAPi1200vMCORESTATUSVMAS": tRAPi1200vMCORESTATUSVMAS,
       "severityi1200vMCORESTATUSVMAS": severityi1200vMCORESTATUSVMAS,
       "messagei1200vMCORESTATUSVMAS": messagei1200vMCORESTATUSVMAS,
       "valuei1200vMCORESTATUSVMAS": valuei1200vMCORESTATUSVMAS,
       "i1300vMCORESTATUSVMAS": i1300vMCORESTATUSVMAS,
       "tRAPi1300vMCORESTATUSVMAS": tRAPi1300vMCORESTATUSVMAS,
       "severityi1300vMCORESTATUSVMAS": severityi1300vMCORESTATUSVMAS,
       "messagei1300vMCORESTATUSVMAS": messagei1300vMCORESTATUSVMAS,
       "valuei1300vMCORESTATUSVMAS": valuei1300vMCORESTATUSVMAS,
       "vmms": vmms,
       "fREEROOTDISKVMMS": fREEROOTDISKVMMS,
       "i2100fREEROOTDISKVMMS": i2100fREEROOTDISKVMMS,
       "tRAPi2100fREEROOTDISKVMMS": tRAPi2100fREEROOTDISKVMMS,
       "severityi2100fREEROOTDISKVMMS": severityi2100fREEROOTDISKVMMS,
       "messagei2100fREEROOTDISKVMMS": messagei2100fREEROOTDISKVMMS,
       "valuei2100fREEROOTDISKVMMS": valuei2100fREEROOTDISKVMMS,
       "i2200fREEROOTDISKVMMS": i2200fREEROOTDISKVMMS,
       "tRAPi2200fREEROOTDISKVMMS": tRAPi2200fREEROOTDISKVMMS,
       "severityi2200fREEROOTDISKVMMS": severityi2200fREEROOTDISKVMMS,
       "messagei2200fREEROOTDISKVMMS": messagei2200fREEROOTDISKVMMS,
       "valuei2200fREEROOTDISKVMMS": valuei2200fREEROOTDISKVMMS,
       "i2300fREEROOTDISKVMMS": i2300fREEROOTDISKVMMS,
       "tRAPi2300fREEROOTDISKVMMS": tRAPi2300fREEROOTDISKVMMS,
       "severityi2300fREEROOTDISKVMMS": severityi2300fREEROOTDISKVMMS,
       "messagei2300fREEROOTDISKVMMS": messagei2300fREEROOTDISKVMMS,
       "valuei2300fREEROOTDISKVMMS": valuei2300fREEROOTDISKVMMS,
       "i2400fREEROOTDISKVMMS": i2400fREEROOTDISKVMMS,
       "tRAPi2400fREEROOTDISKVMMS": tRAPi2400fREEROOTDISKVMMS,
       "severityi2400fREEROOTDISKVMMS": severityi2400fREEROOTDISKVMMS,
       "messagei2400fREEROOTDISKVMMS": messagei2400fREEROOTDISKVMMS,
       "valuei2400fREEROOTDISKVMMS": valuei2400fREEROOTDISKVMMS,
       "fREEBOOTDISKVMMS": fREEBOOTDISKVMMS,
       "i2100fREEBOOTDISKVMMS": i2100fREEBOOTDISKVMMS,
       "tRAPi2100fREEBOOTDISKVMMS": tRAPi2100fREEBOOTDISKVMMS,
       "severityi2100fREEBOOTDISKVMMS": severityi2100fREEBOOTDISKVMMS,
       "messagei2100fREEBOOTDISKVMMS": messagei2100fREEBOOTDISKVMMS,
       "valuei2100fREEBOOTDISKVMMS": valuei2100fREEBOOTDISKVMMS,
       "i2200fREEBOOTDISKVMMS": i2200fREEBOOTDISKVMMS,
       "tRAPi2200fREEBOOTDISKVMMS": tRAPi2200fREEBOOTDISKVMMS,
       "severityi2200fREEBOOTDISKVMMS": severityi2200fREEBOOTDISKVMMS,
       "messagei2200fREEBOOTDISKVMMS": messagei2200fREEBOOTDISKVMMS,
       "valuei2200fREEBOOTDISKVMMS": valuei2200fREEBOOTDISKVMMS,
       "i2300fREEBOOTDISKVMMS": i2300fREEBOOTDISKVMMS,
       "tRAPi2300fREEBOOTDISKVMMS": tRAPi2300fREEBOOTDISKVMMS,
       "severityi2300fREEBOOTDISKVMMS": severityi2300fREEBOOTDISKVMMS,
       "messagei2300fREEBOOTDISKVMMS": messagei2300fREEBOOTDISKVMMS,
       "valuei2300fREEBOOTDISKVMMS": valuei2300fREEBOOTDISKVMMS,
       "i2400fREEBOOTDISKVMMS": i2400fREEBOOTDISKVMMS,
       "tRAPi2400fREEBOOTDISKVMMS": tRAPi2400fREEBOOTDISKVMMS,
       "severityi2400fREEBOOTDISKVMMS": severityi2400fREEBOOTDISKVMMS,
       "messagei2400fREEBOOTDISKVMMS": messagei2400fREEBOOTDISKVMMS,
       "valuei2400fREEBOOTDISKVMMS": valuei2400fREEBOOTDISKVMMS,
       "fREEMEMORYVMMS": fREEMEMORYVMMS,
       "i2100fREEMEMORYVMMS": i2100fREEMEMORYVMMS,
       "tRAPi2100fREEMEMORYVMMS": tRAPi2100fREEMEMORYVMMS,
       "severityi2100fREEMEMORYVMMS": severityi2100fREEMEMORYVMMS,
       "messagei2100fREEMEMORYVMMS": messagei2100fREEMEMORYVMMS,
       "valuei2100fREEMEMORYVMMS": valuei2100fREEMEMORYVMMS,
       "i2200fREEMEMORYVMMS": i2200fREEMEMORYVMMS,
       "tRAPi2200fREEMEMORYVMMS": tRAPi2200fREEMEMORYVMMS,
       "severityi2200fREEMEMORYVMMS": severityi2200fREEMEMORYVMMS,
       "messagei2200fREEMEMORYVMMS": messagei2200fREEMEMORYVMMS,
       "valuei2200fREEMEMORYVMMS": valuei2200fREEMEMORYVMMS,
       "i2300fREEMEMORYVMMS": i2300fREEMEMORYVMMS,
       "tRAPi2300fREEMEMORYVMMS": tRAPi2300fREEMEMORYVMMS,
       "severityi2300fREEMEMORYVMMS": severityi2300fREEMEMORYVMMS,
       "messagei2300fREEMEMORYVMMS": messagei2300fREEMEMORYVMMS,
       "valuei2300fREEMEMORYVMMS": valuei2300fREEMEMORYVMMS,
       "i2400fREEMEMORYVMMS": i2400fREEMEMORYVMMS,
       "tRAPi2400fREEMEMORYVMMS": tRAPi2400fREEMEMORYVMMS,
       "severityi2400fREEMEMORYVMMS": severityi2400fREEMEMORYVMMS,
       "messagei2400fREEMEMORYVMMS": messagei2400fREEMEMORYVMMS,
       "valuei2400fREEMEMORYVMMS": valuei2400fREEMEMORYVMMS,
       "cPULOADVMMS": cPULOADVMMS,
       "i2100cPULOADVMMS": i2100cPULOADVMMS,
       "tRAPi2100cPULOADVMMS": tRAPi2100cPULOADVMMS,
       "severityi2100cPULOADVMMS": severityi2100cPULOADVMMS,
       "messagei2100cPULOADVMMS": messagei2100cPULOADVMMS,
       "valuei2100cPULOADVMMS": valuei2100cPULOADVMMS,
       "i2200cPULOADVMMS": i2200cPULOADVMMS,
       "tRAPi2200cPULOADVMMS": tRAPi2200cPULOADVMMS,
       "severityi2200cPULOADVMMS": severityi2200cPULOADVMMS,
       "messagei2200cPULOADVMMS": messagei2200cPULOADVMMS,
       "valuei2200cPULOADVMMS": valuei2200cPULOADVMMS,
       "i2300cPULOADVMMS": i2300cPULOADVMMS,
       "tRAPi2300cPULOADVMMS": tRAPi2300cPULOADVMMS,
       "severityi2300cPULOADVMMS": severityi2300cPULOADVMMS,
       "messagei2300cPULOADVMMS": messagei2300cPULOADVMMS,
       "valuei2300cPULOADVMMS": valuei2300cPULOADVMMS,
       "i2400cPULOADVMMS": i2400cPULOADVMMS,
       "tRAPi2400cPULOADVMMS": tRAPi2400cPULOADVMMS,
       "severityi2400cPULOADVMMS": severityi2400cPULOADVMMS,
       "messagei2400cPULOADVMMS": messagei2400cPULOADVMMS,
       "valuei2400cPULOADVMMS": valuei2400cPULOADVMMS,
       "fREESWAPVMMS": fREESWAPVMMS,
       "i2100fREESWAPVMMS": i2100fREESWAPVMMS,
       "tRAPi2100fREESWAPVMMS": tRAPi2100fREESWAPVMMS,
       "severityi2100fREESWAPVMMS": severityi2100fREESWAPVMMS,
       "messagei2100fREESWAPVMMS": messagei2100fREESWAPVMMS,
       "valuei2100fREESWAPVMMS": valuei2100fREESWAPVMMS,
       "i2200fREESWAPVMMS": i2200fREESWAPVMMS,
       "tRAPi2200fREESWAPVMMS": tRAPi2200fREESWAPVMMS,
       "severityi2200fREESWAPVMMS": severityi2200fREESWAPVMMS,
       "messagei2200fREESWAPVMMS": messagei2200fREESWAPVMMS,
       "valuei2200fREESWAPVMMS": valuei2200fREESWAPVMMS,
       "i2300fREESWAPVMMS": i2300fREESWAPVMMS,
       "tRAPi2300fREESWAPVMMS": tRAPi2300fREESWAPVMMS,
       "severityi2300fREESWAPVMMS": severityi2300fREESWAPVMMS,
       "messagei2300fREESWAPVMMS": messagei2300fREESWAPVMMS,
       "valuei2300fREESWAPVMMS": valuei2300fREESWAPVMMS,
       "i2400fREESWAPVMMS": i2400fREESWAPVMMS,
       "tRAPi2400fREESWAPVMMS": tRAPi2400fREESWAPVMMS,
       "severityi2400fREESWAPVMMS": severityi2400fREESWAPVMMS,
       "messagei2400fREESWAPVMMS": messagei2400fREESWAPVMMS,
       "valuei2400fREESWAPVMMS": valuei2400fREESWAPVMMS,
       "eTHINTSTATUSVMMS": eTHINTSTATUSVMMS,
       "i2100eTHINTSTATUSVMMS": i2100eTHINTSTATUSVMMS,
       "tRAPi2100eTHINTSTATUSVMMS": tRAPi2100eTHINTSTATUSVMMS,
       "severityi2100eTHINTSTATUSVMMS": severityi2100eTHINTSTATUSVMMS,
       "messagei2100eTHINTSTATUSVMMS": messagei2100eTHINTSTATUSVMMS,
       "valuei2100eTHINTSTATUSVMMS": valuei2100eTHINTSTATUSVMMS,
       "i2200eTHINTSTATUSVMMS": i2200eTHINTSTATUSVMMS,
       "tRAPi2200eTHINTSTATUSVMMS": tRAPi2200eTHINTSTATUSVMMS,
       "severityi2200eTHINTSTATUSVMMS": severityi2200eTHINTSTATUSVMMS,
       "messagei2200eTHINTSTATUSVMMS": messagei2200eTHINTSTATUSVMMS,
       "valuei2200eTHINTSTATUSVMMS": valuei2200eTHINTSTATUSVMMS,
       "i2300eTHINTSTATUSVMMS": i2300eTHINTSTATUSVMMS,
       "tRAPi2300eTHINTSTATUSVMMS": tRAPi2300eTHINTSTATUSVMMS,
       "severityi2300eTHINTSTATUSVMMS": severityi2300eTHINTSTATUSVMMS,
       "messagei2300eTHINTSTATUSVMMS": messagei2300eTHINTSTATUSVMMS,
       "valuei2300eTHINTSTATUSVMMS": valuei2300eTHINTSTATUSVMMS,
       "i2400eTHINTSTATUSVMMS": i2400eTHINTSTATUSVMMS,
       "tRAPi2400eTHINTSTATUSVMMS": tRAPi2400eTHINTSTATUSVMMS,
       "severityi2400eTHINTSTATUSVMMS": severityi2400eTHINTSTATUSVMMS,
       "messagei2400eTHINTSTATUSVMMS": messagei2400eTHINTSTATUSVMMS,
       "valuei2400eTHINTSTATUSVMMS": valuei2400eTHINTSTATUSVMMS,
       "cRONSTATUSVMMS": cRONSTATUSVMMS,
       "i2100cRONSTATUSVMMS": i2100cRONSTATUSVMMS,
       "tRAPi2100cRONSTATUSVMMS": tRAPi2100cRONSTATUSVMMS,
       "severityi2100cRONSTATUSVMMS": severityi2100cRONSTATUSVMMS,
       "messagei2100cRONSTATUSVMMS": messagei2100cRONSTATUSVMMS,
       "valuei2100cRONSTATUSVMMS": valuei2100cRONSTATUSVMMS,
       "i2200cRONSTATUSVMMS": i2200cRONSTATUSVMMS,
       "tRAPi2200cRONSTATUSVMMS": tRAPi2200cRONSTATUSVMMS,
       "severityi2200cRONSTATUSVMMS": severityi2200cRONSTATUSVMMS,
       "messagei2200cRONSTATUSVMMS": messagei2200cRONSTATUSVMMS,
       "valuei2200cRONSTATUSVMMS": valuei2200cRONSTATUSVMMS,
       "i2300cRONSTATUSVMMS": i2300cRONSTATUSVMMS,
       "tRAPi2300cRONSTATUSVMMS": tRAPi2300cRONSTATUSVMMS,
       "severityi2300cRONSTATUSVMMS": severityi2300cRONSTATUSVMMS,
       "messagei2300cRONSTATUSVMMS": messagei2300cRONSTATUSVMMS,
       "valuei2300cRONSTATUSVMMS": valuei2300cRONSTATUSVMMS,
       "i2400cRONSTATUSVMMS": i2400cRONSTATUSVMMS,
       "tRAPi2400cRONSTATUSVMMS": tRAPi2400cRONSTATUSVMMS,
       "severityi2400cRONSTATUSVMMS": severityi2400cRONSTATUSVMMS,
       "messagei2400cRONSTATUSVMMS": messagei2400cRONSTATUSVMMS,
       "valuei2400cRONSTATUSVMMS": valuei2400cRONSTATUSVMMS,
       "mONITSTATUSVMMS": mONITSTATUSVMMS,
       "i2100mONITSTATUSVMMS": i2100mONITSTATUSVMMS,
       "tRAPi2100mONITSTATUSVMMS": tRAPi2100mONITSTATUSVMMS,
       "severityi2100mONITSTATUSVMMS": severityi2100mONITSTATUSVMMS,
       "messagei2100mONITSTATUSVMMS": messagei2100mONITSTATUSVMMS,
       "valuei2100mONITSTATUSVMMS": valuei2100mONITSTATUSVMMS,
       "i2200mONITSTATUSVMMS": i2200mONITSTATUSVMMS,
       "tRAPi2200mONITSTATUSVMMS": tRAPi2200mONITSTATUSVMMS,
       "severityi2200mONITSTATUSVMMS": severityi2200mONITSTATUSVMMS,
       "messagei2200mONITSTATUSVMMS": messagei2200mONITSTATUSVMMS,
       "valuei2200mONITSTATUSVMMS": valuei2200mONITSTATUSVMMS,
       "i2300mONITSTATUSVMMS": i2300mONITSTATUSVMMS,
       "tRAPi2300mONITSTATUSVMMS": tRAPi2300mONITSTATUSVMMS,
       "severityi2300mONITSTATUSVMMS": severityi2300mONITSTATUSVMMS,
       "messagei2300mONITSTATUSVMMS": messagei2300mONITSTATUSVMMS,
       "valuei2300mONITSTATUSVMMS": valuei2300mONITSTATUSVMMS,
       "i2400mONITSTATUSVMMS": i2400mONITSTATUSVMMS,
       "tRAPi2400mONITSTATUSVMMS": tRAPi2400mONITSTATUSVMMS,
       "severityi2400mONITSTATUSVMMS": severityi2400mONITSTATUSVMMS,
       "messagei2400mONITSTATUSVMMS": messagei2400mONITSTATUSVMMS,
       "valuei2400mONITSTATUSVMMS": valuei2400mONITSTATUSVMMS,
       "dNSMASQSTATUSVMMS": dNSMASQSTATUSVMMS,
       "i2100dNSMASQSTATUSVMMS": i2100dNSMASQSTATUSVMMS,
       "tRAPi2100dNSMASQSTATUSVMMS": tRAPi2100dNSMASQSTATUSVMMS,
       "severityi2100dNSMASQSTATUSVMMS": severityi2100dNSMASQSTATUSVMMS,
       "messagei2100dNSMASQSTATUSVMMS": messagei2100dNSMASQSTATUSVMMS,
       "valuei2100dNSMASQSTATUSVMMS": valuei2100dNSMASQSTATUSVMMS,
       "i2200dNSMASQSTATUSVMMS": i2200dNSMASQSTATUSVMMS,
       "tRAPi2200dNSMASQSTATUSVMMS": tRAPi2200dNSMASQSTATUSVMMS,
       "severityi2200dNSMASQSTATUSVMMS": severityi2200dNSMASQSTATUSVMMS,
       "messagei2200dNSMASQSTATUSVMMS": messagei2200dNSMASQSTATUSVMMS,
       "valuei2200dNSMASQSTATUSVMMS": valuei2200dNSMASQSTATUSVMMS,
       "i2300dNSMASQSTATUSVMMS": i2300dNSMASQSTATUSVMMS,
       "tRAPi2300dNSMASQSTATUSVMMS": tRAPi2300dNSMASQSTATUSVMMS,
       "severityi2300dNSMASQSTATUSVMMS": severityi2300dNSMASQSTATUSVMMS,
       "messagei2300dNSMASQSTATUSVMMS": messagei2300dNSMASQSTATUSVMMS,
       "valuei2300dNSMASQSTATUSVMMS": valuei2300dNSMASQSTATUSVMMS,
       "i2400dNSMASQSTATUSVMMS": i2400dNSMASQSTATUSVMMS,
       "tRAPi2400dNSMASQSTATUSVMMS": tRAPi2400dNSMASQSTATUSVMMS,
       "severityi2400dNSMASQSTATUSVMMS": severityi2400dNSMASQSTATUSVMMS,
       "messagei2400dNSMASQSTATUSVMMS": messagei2400dNSMASQSTATUSVMMS,
       "valuei2400dNSMASQSTATUSVMMS": valuei2400dNSMASQSTATUSVMMS,
       "hB2STATUSVMMS": hB2STATUSVMMS,
       "i2100hB2STATUSVMMS": i2100hB2STATUSVMMS,
       "tRAPi2100hB2STATUSVMMS": tRAPi2100hB2STATUSVMMS,
       "severityi2100hB2STATUSVMMS": severityi2100hB2STATUSVMMS,
       "messagei2100hB2STATUSVMMS": messagei2100hB2STATUSVMMS,
       "valuei2100hB2STATUSVMMS": valuei2100hB2STATUSVMMS,
       "i2200hB2STATUSVMMS": i2200hB2STATUSVMMS,
       "tRAPi2200hB2STATUSVMMS": tRAPi2200hB2STATUSVMMS,
       "severityi2200hB2STATUSVMMS": severityi2200hB2STATUSVMMS,
       "messagei2200hB2STATUSVMMS": messagei2200hB2STATUSVMMS,
       "valuei2200hB2STATUSVMMS": valuei2200hB2STATUSVMMS,
       "i2300hB2STATUSVMMS": i2300hB2STATUSVMMS,
       "tRAPi2300hB2STATUSVMMS": tRAPi2300hB2STATUSVMMS,
       "severityi2300hB2STATUSVMMS": severityi2300hB2STATUSVMMS,
       "messagei2300hB2STATUSVMMS": messagei2300hB2STATUSVMMS,
       "valuei2300hB2STATUSVMMS": valuei2300hB2STATUSVMMS,
       "i2400hB2STATUSVMMS": i2400hB2STATUSVMMS,
       "tRAPi2400hB2STATUSVMMS": tRAPi2400hB2STATUSVMMS,
       "severityi2400hB2STATUSVMMS": severityi2400hB2STATUSVMMS,
       "messagei2400hB2STATUSVMMS": messagei2400hB2STATUSVMMS,
       "valuei2400hB2STATUSVMMS": valuei2400hB2STATUSVMMS,
       "hB2MWDIASTATUSVMMS": hB2MWDIASTATUSVMMS,
       "i2100hB2MWDIASTATUSVMMS": i2100hB2MWDIASTATUSVMMS,
       "tRAPi2100hB2MWDIASTATUSVMMS": tRAPi2100hB2MWDIASTATUSVMMS,
       "severityi2100hB2MWDIASTATUSVMMS": severityi2100hB2MWDIASTATUSVMMS,
       "messagei2100hB2MWDIASTATUSVMMS": messagei2100hB2MWDIASTATUSVMMS,
       "valuei2100hB2MWDIASTATUSVMMS": valuei2100hB2MWDIASTATUSVMMS,
       "i2200hB2MWDIASTATUSVMMS": i2200hB2MWDIASTATUSVMMS,
       "tRAPi2200hB2MWDIASTATUSVMMS": tRAPi2200hB2MWDIASTATUSVMMS,
       "severityi2200hB2MWDIASTATUSVMMS": severityi2200hB2MWDIASTATUSVMMS,
       "messagei2200hB2MWDIASTATUSVMMS": messagei2200hB2MWDIASTATUSVMMS,
       "valuei2200hB2MWDIASTATUSVMMS": valuei2200hB2MWDIASTATUSVMMS,
       "i2300hB2MWDIASTATUSVMMS": i2300hB2MWDIASTATUSVMMS,
       "tRAPi2300hB2MWDIASTATUSVMMS": tRAPi2300hB2MWDIASTATUSVMMS,
       "severityi2300hB2MWDIASTATUSVMMS": severityi2300hB2MWDIASTATUSVMMS,
       "messagei2300hB2MWDIASTATUSVMMS": messagei2300hB2MWDIASTATUSVMMS,
       "valuei2300hB2MWDIASTATUSVMMS": valuei2300hB2MWDIASTATUSVMMS,
       "i2400hB2MWDIASTATUSVMMS": i2400hB2MWDIASTATUSVMMS,
       "tRAPi2400hB2MWDIASTATUSVMMS": tRAPi2400hB2MWDIASTATUSVMMS,
       "severityi2400hB2MWDIASTATUSVMMS": severityi2400hB2MWDIASTATUSVMMS,
       "messagei2400hB2MWDIASTATUSVMMS": messagei2400hB2MWDIASTATUSVMMS,
       "valuei2400hB2MWDIASTATUSVMMS": valuei2400hB2MWDIASTATUSVMMS,
       "cPUSTATUSVMMS": cPUSTATUSVMMS,
       "i2100cPUSTATUSVMMS": i2100cPUSTATUSVMMS,
       "tRAPi2100cPUSTATUSVMMS": tRAPi2100cPUSTATUSVMMS,
       "severityi2100cPUSTATUSVMMS": severityi2100cPUSTATUSVMMS,
       "messagei2100cPUSTATUSVMMS": messagei2100cPUSTATUSVMMS,
       "valuei2100cPUSTATUSVMMS": valuei2100cPUSTATUSVMMS,
       "i2200cPUSTATUSVMMS": i2200cPUSTATUSVMMS,
       "tRAPi2200cPUSTATUSVMMS": tRAPi2200cPUSTATUSVMMS,
       "severityi2200cPUSTATUSVMMS": severityi2200cPUSTATUSVMMS,
       "messagei2200cPUSTATUSVMMS": messagei2200cPUSTATUSVMMS,
       "valuei2200cPUSTATUSVMMS": valuei2200cPUSTATUSVMMS,
       "i2300cPUSTATUSVMMS": i2300cPUSTATUSVMMS,
       "tRAPi2300cPUSTATUSVMMS": tRAPi2300cPUSTATUSVMMS,
       "severityi2300cPUSTATUSVMMS": severityi2300cPUSTATUSVMMS,
       "messagei2300cPUSTATUSVMMS": messagei2300cPUSTATUSVMMS,
       "valuei2300cPUSTATUSVMMS": valuei2300cPUSTATUSVMMS,
       "i2400cPUSTATUSVMMS": i2400cPUSTATUSVMMS,
       "tRAPi2400cPUSTATUSVMMS": tRAPi2400cPUSTATUSVMMS,
       "severityi2400cPUSTATUSVMMS": severityi2400cPUSTATUSVMMS,
       "messagei2400cPUSTATUSVMMS": messagei2400cPUSTATUSVMMS,
       "valuei2400cPUSTATUSVMMS": valuei2400cPUSTATUSVMMS,
       "vmdb": vmdb,
       "fREEROOTDISKVMDB": fREEROOTDISKVMDB,
       "i3100fREEROOTDISKVMDB": i3100fREEROOTDISKVMDB,
       "tRAPi3100fREEROOTDISKVMDB": tRAPi3100fREEROOTDISKVMDB,
       "severityi3100fREEROOTDISKVMDB": severityi3100fREEROOTDISKVMDB,
       "messagei3100fREEROOTDISKVMDB": messagei3100fREEROOTDISKVMDB,
       "valuei3100fREEROOTDISKVMDB": valuei3100fREEROOTDISKVMDB,
       "i3200fREEROOTDISKVMDB": i3200fREEROOTDISKVMDB,
       "tRAPi3200fREEROOTDISKVMDB": tRAPi3200fREEROOTDISKVMDB,
       "severityi3200fREEROOTDISKVMDB": severityi3200fREEROOTDISKVMDB,
       "messagei3200fREEROOTDISKVMDB": messagei3200fREEROOTDISKVMDB,
       "valuei3200fREEROOTDISKVMDB": valuei3200fREEROOTDISKVMDB,
       "i3300fREEROOTDISKVMDB": i3300fREEROOTDISKVMDB,
       "tRAPi3300fREEROOTDISKVMDB": tRAPi3300fREEROOTDISKVMDB,
       "severityi3300fREEROOTDISKVMDB": severityi3300fREEROOTDISKVMDB,
       "messagei3300fREEROOTDISKVMDB": messagei3300fREEROOTDISKVMDB,
       "valuei3300fREEROOTDISKVMDB": valuei3300fREEROOTDISKVMDB,
       "fREEBOOTDISKVMDB": fREEBOOTDISKVMDB,
       "i3100fREEBOOTDISKVMDB": i3100fREEBOOTDISKVMDB,
       "tRAPi3100fREEBOOTDISKVMDB": tRAPi3100fREEBOOTDISKVMDB,
       "severityi3100fREEBOOTDISKVMDB": severityi3100fREEBOOTDISKVMDB,
       "messagei3100fREEBOOTDISKVMDB": messagei3100fREEBOOTDISKVMDB,
       "valuei3100fREEBOOTDISKVMDB": valuei3100fREEBOOTDISKVMDB,
       "i3200fREEBOOTDISKVMDB": i3200fREEBOOTDISKVMDB,
       "tRAPi3200fREEBOOTDISKVMDB": tRAPi3200fREEBOOTDISKVMDB,
       "severityi3200fREEBOOTDISKVMDB": severityi3200fREEBOOTDISKVMDB,
       "messagei3200fREEBOOTDISKVMDB": messagei3200fREEBOOTDISKVMDB,
       "valuei3200fREEBOOTDISKVMDB": valuei3200fREEBOOTDISKVMDB,
       "i3300fREEBOOTDISKVMDB": i3300fREEBOOTDISKVMDB,
       "tRAPi3300fREEBOOTDISKVMDB": tRAPi3300fREEBOOTDISKVMDB,
       "severityi3300fREEBOOTDISKVMDB": severityi3300fREEBOOTDISKVMDB,
       "messagei3300fREEBOOTDISKVMDB": messagei3300fREEBOOTDISKVMDB,
       "valuei3300fREEBOOTDISKVMDB": valuei3300fREEBOOTDISKVMDB,
       "fREEMEMORYVMDB": fREEMEMORYVMDB,
       "i3100fREEMEMORYVMDB": i3100fREEMEMORYVMDB,
       "tRAPi3100fREEMEMORYVMDB": tRAPi3100fREEMEMORYVMDB,
       "severityi3100fREEMEMORYVMDB": severityi3100fREEMEMORYVMDB,
       "messagei3100fREEMEMORYVMDB": messagei3100fREEMEMORYVMDB,
       "valuei3100fREEMEMORYVMDB": valuei3100fREEMEMORYVMDB,
       "i3200fREEMEMORYVMDB": i3200fREEMEMORYVMDB,
       "tRAPi3200fREEMEMORYVMDB": tRAPi3200fREEMEMORYVMDB,
       "severityi3200fREEMEMORYVMDB": severityi3200fREEMEMORYVMDB,
       "messagei3200fREEMEMORYVMDB": messagei3200fREEMEMORYVMDB,
       "valuei3200fREEMEMORYVMDB": valuei3200fREEMEMORYVMDB,
       "i3300fREEMEMORYVMDB": i3300fREEMEMORYVMDB,
       "tRAPi3300fREEMEMORYVMDB": tRAPi3300fREEMEMORYVMDB,
       "severityi3300fREEMEMORYVMDB": severityi3300fREEMEMORYVMDB,
       "messagei3300fREEMEMORYVMDB": messagei3300fREEMEMORYVMDB,
       "valuei3300fREEMEMORYVMDB": valuei3300fREEMEMORYVMDB,
       "cPULOADVMDB": cPULOADVMDB,
       "i3100cPULOADVMDB": i3100cPULOADVMDB,
       "tRAPi3100cPULOADVMDB": tRAPi3100cPULOADVMDB,
       "severityi3100cPULOADVMDB": severityi3100cPULOADVMDB,
       "messagei3100cPULOADVMDB": messagei3100cPULOADVMDB,
       "valuei3100cPULOADVMDB": valuei3100cPULOADVMDB,
       "i3200cPULOADVMDB": i3200cPULOADVMDB,
       "tRAPi3200cPULOADVMDB": tRAPi3200cPULOADVMDB,
       "severityi3200cPULOADVMDB": severityi3200cPULOADVMDB,
       "messagei3200cPULOADVMDB": messagei3200cPULOADVMDB,
       "valuei3200cPULOADVMDB": valuei3200cPULOADVMDB,
       "i3300cPULOADVMDB": i3300cPULOADVMDB,
       "tRAPi3300cPULOADVMDB": tRAPi3300cPULOADVMDB,
       "severityi3300cPULOADVMDB": severityi3300cPULOADVMDB,
       "messagei3300cPULOADVMDB": messagei3300cPULOADVMDB,
       "valuei3300cPULOADVMDB": valuei3300cPULOADVMDB,
       "fREESWAPVMDB": fREESWAPVMDB,
       "i3100fREESWAPVMDB": i3100fREESWAPVMDB,
       "tRAPi3100fREESWAPVMDB": tRAPi3100fREESWAPVMDB,
       "severityi3100fREESWAPVMDB": severityi3100fREESWAPVMDB,
       "messagei3100fREESWAPVMDB": messagei3100fREESWAPVMDB,
       "valuei3100fREESWAPVMDB": valuei3100fREESWAPVMDB,
       "i3200fREESWAPVMDB": i3200fREESWAPVMDB,
       "tRAPi3200fREESWAPVMDB": tRAPi3200fREESWAPVMDB,
       "severityi3200fREESWAPVMDB": severityi3200fREESWAPVMDB,
       "messagei3200fREESWAPVMDB": messagei3200fREESWAPVMDB,
       "valuei3200fREESWAPVMDB": valuei3200fREESWAPVMDB,
       "i3300fREESWAPVMDB": i3300fREESWAPVMDB,
       "tRAPi3300fREESWAPVMDB": tRAPi3300fREESWAPVMDB,
       "severityi3300fREESWAPVMDB": severityi3300fREESWAPVMDB,
       "messagei3300fREESWAPVMDB": messagei3300fREESWAPVMDB,
       "valuei3300fREESWAPVMDB": valuei3300fREESWAPVMDB,
       "eTHINTSTATUSVMDB": eTHINTSTATUSVMDB,
       "i3100eTHINTSTATUSVMDB": i3100eTHINTSTATUSVMDB,
       "tRAPi3100eTHINTSTATUSVMDB": tRAPi3100eTHINTSTATUSVMDB,
       "severityi3100eTHINTSTATUSVMDB": severityi3100eTHINTSTATUSVMDB,
       "messagei3100eTHINTSTATUSVMDB": messagei3100eTHINTSTATUSVMDB,
       "valuei3100eTHINTSTATUSVMDBe": valuei3100eTHINTSTATUSVMDBe,
       "i3200eTHINTSTATUSVMDB": i3200eTHINTSTATUSVMDB,
       "tRAPi3200eTHINTSTATUSVMDB": tRAPi3200eTHINTSTATUSVMDB,
       "severityi3200eTHINTSTATUSVMDB": severityi3200eTHINTSTATUSVMDB,
       "messagei3200eTHINTSTATUSVMDB": messagei3200eTHINTSTATUSVMDB,
       "valuei3200eTHINTSTATUSVMDB": valuei3200eTHINTSTATUSVMDB,
       "i3300eTHINTSTATUSVMDB": i3300eTHINTSTATUSVMDB,
       "tRAPi3300eTHINTSTATUSVMDB": tRAPi3300eTHINTSTATUSVMDB,
       "severityi3300eTHINTSTATUSVMDB": severityi3300eTHINTSTATUSVMDB,
       "messagei3300eTHINTSTATUSVMDB": messagei3300eTHINTSTATUSVMDB,
       "valuei3300eTHINTSTATUSVMDB": valuei3300eTHINTSTATUSVMDB,
       "cRONSTATUSVMDB": cRONSTATUSVMDB,
       "i3100cRONSTATUSVMDB": i3100cRONSTATUSVMDB,
       "tRAPi3100cRONSTATUSVMDB": tRAPi3100cRONSTATUSVMDB,
       "severityi3100cRONSTATUSVMDB": severityi3100cRONSTATUSVMDB,
       "messagei3100cRONSTATUSVMDB": messagei3100cRONSTATUSVMDB,
       "valuei3100cRONSTATUSVMDB": valuei3100cRONSTATUSVMDB,
       "i3200cRONSTATUSVMDB": i3200cRONSTATUSVMDB,
       "tRAPi3200cRONSTATUSVMDB": tRAPi3200cRONSTATUSVMDB,
       "severityi3200cRONSTATUSVMDB": severityi3200cRONSTATUSVMDB,
       "messagei3200cRONSTATUSVMDB": messagei3200cRONSTATUSVMDB,
       "valuei3200cRONSTATUSVMDB": valuei3200cRONSTATUSVMDB,
       "i3300cRONSTATUSVMDB": i3300cRONSTATUSVMDB,
       "tRAPi3300cRONSTATUSVMDB": tRAPi3300cRONSTATUSVMDB,
       "severityi3300cRONSTATUSVMDB": severityi3300cRONSTATUSVMDB,
       "messagei3300cRONSTATUSVMDB": messagei3300cRONSTATUSVMDB,
       "valuei3300cRONSTATUSVMDB": valuei3300cRONSTATUSVMDB,
       "mONITSTATUSVMDB": mONITSTATUSVMDB,
       "i3100mONITSTATUSVMDB": i3100mONITSTATUSVMDB,
       "tRAPi3100mONITSTATUSVMDB": tRAPi3100mONITSTATUSVMDB,
       "severityi3100mONITSTATUSVMDB": severityi3100mONITSTATUSVMDB,
       "messagei3100mONITSTATUSVMDB": messagei3100mONITSTATUSVMDB,
       "valuei3100mONITSTATUSVMDB": valuei3100mONITSTATUSVMDB,
       "i3200mONITSTATUSVMDB": i3200mONITSTATUSVMDB,
       "tRAPi3200mONITSTATUSVMDB": tRAPi3200mONITSTATUSVMDB,
       "severityi3200mONITSTATUSVMDB": severityi3200mONITSTATUSVMDB,
       "messagei3200mONITSTATUSVMDB": messagei3200mONITSTATUSVMDB,
       "valuei3200mONITSTATUSVMDB": valuei3200mONITSTATUSVMDB,
       "i3300mONITSTATUSVMDB": i3300mONITSTATUSVMDB,
       "tRAPi3300mONITSTATUSVMDB": tRAPi3300mONITSTATUSVMDB,
       "severityi3300mONITSTATUSVMDB": severityi3300mONITSTATUSVMDB,
       "messagei3300mONITSTATUSVMDB": messagei3300mONITSTATUSVMDB,
       "valuei3300mONITSTATUSVMDB": valuei3300mONITSTATUSVMDB,
       "pOSTGRESSTATUSVMDB": pOSTGRESSTATUSVMDB,
       "i3100pOSTGRESSTATUSVMDB": i3100pOSTGRESSTATUSVMDB,
       "tRAPi3100pOSTGRESSTATUSVMDB": tRAPi3100pOSTGRESSTATUSVMDB,
       "severityi3100pOSTGRESSTATUSVMDB": severityi3100pOSTGRESSTATUSVMDB,
       "messagei3100pOSTGRESSTATUSVMDB": messagei3100pOSTGRESSTATUSVMDB,
       "valuei3100pOSTGRESSTATUSVMDB": valuei3100pOSTGRESSTATUSVMDB,
       "i3200pOSTGRESSTATUSVMDB": i3200pOSTGRESSTATUSVMDB,
       "tRAPi3200pOSTGRESSTATUSVMDB": tRAPi3200pOSTGRESSTATUSVMDB,
       "severityi3200pOSTGRESSTATUSVMDB": severityi3200pOSTGRESSTATUSVMDB,
       "messagei3200pOSTGRESSTATUSVMDB": messagei3200pOSTGRESSTATUSVMDB,
       "valuei3200pOSTGRESSTATUSVMDB": valuei3200pOSTGRESSTATUSVMDB,
       "i3300pOSTGRESSTATUSVMDB": i3300pOSTGRESSTATUSVMDB,
       "tRAPi3300pOSTGRESSTATUSVMDB": tRAPi3300pOSTGRESSTATUSVMDB,
       "severityi3300pOSTGRESSTATUSVMDB": severityi3300pOSTGRESSTATUSVMDB,
       "messagei3300pOSTGRESSTATUSVMDB": messagei3300pOSTGRESSTATUSVMDB,
       "valuei3300pOSTGRESSTATUSVMDB": valuei3300pOSTGRESSTATUSVMDB,
       "pGPOOLSTATUSVMDB": pGPOOLSTATUSVMDB,
       "i3100pGPOOLSTATUSVMDB": i3100pGPOOLSTATUSVMDB,
       "tRAPi3100pGPOOLSTATUSVMDB": tRAPi3100pGPOOLSTATUSVMDB,
       "severityi3100pGPOOLSTATUSVMDB": severityi3100pGPOOLSTATUSVMDB,
       "messagei3100pGPOOLSTATUSVMDB": messagei3100pGPOOLSTATUSVMDB,
       "valuei3100pGPOOLSTATUSVMDB": valuei3100pGPOOLSTATUSVMDB,
       "i3200pGPOOLSTATUSVMDB": i3200pGPOOLSTATUSVMDB,
       "tRAPi3200pGPOOLSTATUSVMDB": tRAPi3200pGPOOLSTATUSVMDB,
       "severityi3200pGPOOLSTATUSVMDB": severityi3200pGPOOLSTATUSVMDB,
       "messagei3200pGPOOLSTATUSVMDB": messagei3200pGPOOLSTATUSVMDB,
       "valuei3200pGPOOLSTATUSVMDB": valuei3200pGPOOLSTATUSVMDB,
       "i3300pGPOOLSTATUSVMDB": i3300pGPOOLSTATUSVMDB,
       "tRAPi3300pGPOOLSTATUSVMDB": tRAPi3300pGPOOLSTATUSVMDB,
       "severityi3300pGPOOLSTATUSVMDB": severityi3300pGPOOLSTATUSVMDB,
       "messagei3300pGPOOLSTATUSVMDB": messagei3300pGPOOLSTATUSVMDB,
       "valuei3300pGPOOLSTATUSVMDB": valuei3300pGPOOLSTATUSVMDB,
       "pGAGENTSATUSVMDB": pGAGENTSATUSVMDB,
       "i3100pGAGENTSATUSVMDB": i3100pGAGENTSATUSVMDB,
       "tRAPi3100pGAGENTSATUSVMDB": tRAPi3100pGAGENTSATUSVMDB,
       "severityi3100pGAGENTSATUSVMDB": severityi3100pGAGENTSATUSVMDB,
       "messagei3100pGAGENTSATUSVMDB": messagei3100pGAGENTSATUSVMDB,
       "valuei3100pGAGENTSATUSVMDB": valuei3100pGAGENTSATUSVMDB,
       "i3200pGAGENTSATUSVMDB": i3200pGAGENTSATUSVMDB,
       "tRAPi3200pGAGENTSATUSVMDB": tRAPi3200pGAGENTSATUSVMDB,
       "severityi3200pGAGENTSATUSVMDB": severityi3200pGAGENTSATUSVMDB,
       "messagei3200pGAGENTSATUSVMDB": messagei3200pGAGENTSATUSVMDB,
       "valuei3200pGAGENTSATUSVMDB": valuei3200pGAGENTSATUSVMDB,
       "i3300pGAGENTSATUSVMDB": i3300pGAGENTSATUSVMDB,
       "tRAPi3300pGAGENTSATUSVMDB": tRAPi3300pGAGENTSATUSVMDB,
       "severityi3300pGAGENTSATUSVMDB": severityi3300pGAGENTSATUSVMDB,
       "messagei3300pGAGENTSATUSVMDB": messagei3300pGAGENTSATUSVMDB,
       "valuei3300pGAGENTSATUSVMDB": valuei3300pGAGENTSATUSVMDB,
       "cPUSTATUSVMDB": cPUSTATUSVMDB,
       "i3100cPUSTATUSVMDB": i3100cPUSTATUSVMDB,
       "tRAPi3100cPUSTATUSVMDB": tRAPi3100cPUSTATUSVMDB,
       "severityi3100cPUSTATUSVMDB": severityi3100cPUSTATUSVMDB,
       "messagei3100cPUSTATUSVMDB": messagei3100cPUSTATUSVMDB,
       "valuei3100cPUSTATUSVMDB": valuei3100cPUSTATUSVMDB,
       "i3200cPUSTATUSVMDB": i3200cPUSTATUSVMDB,
       "tRAPi3200cPUSTATUSVMDB": tRAPi3200cPUSTATUSVMDB,
       "severityi3200cPUSTATUSVMDB": severityi3200cPUSTATUSVMDB,
       "messagei3200cPUSTATUSVMDB": messagei3200cPUSTATUSVMDB,
       "valuei3200cPUSTATUSVMDB": valuei3200cPUSTATUSVMDB,
       "i3300cPUSTATUSVMDB": i3300cPUSTATUSVMDB,
       "tRAPi3300cPUSTATUSVMDB": tRAPi3300cPUSTATUSVMDB,
       "severityi3300cPUSTATUSVMDB": severityi3300cPUSTATUSVMDB,
       "messagei3300cPUSTATUSVMDB": messagei3300cPUSTATUSVMDB,
       "valuei3300cPUSTATUSVMDB": valuei3300cPUSTATUSVMDB,
       "vmic": vmic,
       "fREEROOTDISKVMIC": fREEROOTDISKVMIC,
       "i4100fREEROOTDISKVMIC": i4100fREEROOTDISKVMIC,
       "tRAPi4100fREEROOTDISKVMIC": tRAPi4100fREEROOTDISKVMIC,
       "severityi4100fREEROOTDISKVMIC": severityi4100fREEROOTDISKVMIC,
       "messagei4100fREEROOTDISKVMIC": messagei4100fREEROOTDISKVMIC,
       "valuei4100fREEROOTDISKVMIC": valuei4100fREEROOTDISKVMIC,
       "i4200fREEROOTDISKVMIC": i4200fREEROOTDISKVMIC,
       "tRAPi4200fREEROOTDISKVMIC": tRAPi4200fREEROOTDISKVMIC,
       "severityi4200fREEROOTDISKVMIC": severityi4200fREEROOTDISKVMIC,
       "messagei4200fREEROOTDISKVMIC": messagei4200fREEROOTDISKVMIC,
       "valuei4200fREEROOTDISKVMIC": valuei4200fREEROOTDISKVMIC,
       "i4300fREEROOTDISKVMIC": i4300fREEROOTDISKVMIC,
       "tRAPi4300fREEROOTDISKVMIC": tRAPi4300fREEROOTDISKVMIC,
       "severityi4300fREEROOTDISKVMIC": severityi4300fREEROOTDISKVMIC,
       "messagei4300fREEROOTDISKVMIC": messagei4300fREEROOTDISKVMIC,
       "valuei4300fREEROOTDISKVMIC": valuei4300fREEROOTDISKVMIC,
       "fREEBOOTDISKVMIC": fREEBOOTDISKVMIC,
       "i4100fREEBOOTDISKVMIC": i4100fREEBOOTDISKVMIC,
       "tRAPi4100fREEBOOTDISKVMIC": tRAPi4100fREEBOOTDISKVMIC,
       "severityi4100fREEBOOTDISKVMIC": severityi4100fREEBOOTDISKVMIC,
       "messagei4100fREEBOOTDISKVMIC": messagei4100fREEBOOTDISKVMIC,
       "valuei4100fREEBOOTDISKVMIC": valuei4100fREEBOOTDISKVMIC,
       "i4200fREEBOOTDISKVMIC": i4200fREEBOOTDISKVMIC,
       "tRAPi4200fREEBOOTDISKVMIC": tRAPi4200fREEBOOTDISKVMIC,
       "severityi4200fREEBOOTDISKVMIC": severityi4200fREEBOOTDISKVMIC,
       "messagei4200fREEBOOTDISKVMIC": messagei4200fREEBOOTDISKVMIC,
       "valuei4200fREEBOOTDISKVMIC": valuei4200fREEBOOTDISKVMIC,
       "i4300fREEBOOTDISKVMIC": i4300fREEBOOTDISKVMIC,
       "tRAPi4300fREEBOOTDISKVMIC": tRAPi4300fREEBOOTDISKVMIC,
       "severityi4300fREEBOOTDISKVMIC": severityi4300fREEBOOTDISKVMIC,
       "messagei4300fREEBOOTDISKVMIC": messagei4300fREEBOOTDISKVMIC,
       "valuei4300fREEBOOTDISKVMIC": valuei4300fREEBOOTDISKVMIC,
       "fREEMEMORYVMIC": fREEMEMORYVMIC,
       "i4100fREEMEMORYVMIC": i4100fREEMEMORYVMIC,
       "tRAPi4100fREEMEMORYVMIC": tRAPi4100fREEMEMORYVMIC,
       "severityi4100fREEMEMORYVMIC": severityi4100fREEMEMORYVMIC,
       "messagei4100fREEMEMORYVMIC": messagei4100fREEMEMORYVMIC,
       "valuei4100fREEMEMORYVMIC": valuei4100fREEMEMORYVMIC,
       "i4200fREEMEMORYVMIC": i4200fREEMEMORYVMIC,
       "tRAPi4200fREEMEMORYVMIC": tRAPi4200fREEMEMORYVMIC,
       "severityi4200fREEMEMORYVMIC": severityi4200fREEMEMORYVMIC,
       "messagei4200fREEMEMORYVMIC": messagei4200fREEMEMORYVMIC,
       "valuei4200fREEMEMORYVMIC": valuei4200fREEMEMORYVMIC,
       "i4300fREEMEMORYVMIC": i4300fREEMEMORYVMIC,
       "tRAPi4300fREEMEMORYVMIC": tRAPi4300fREEMEMORYVMIC,
       "severityi4300fREEMEMORYVMIC": severityi4300fREEMEMORYVMIC,
       "messagei4300fREEMEMORYVMIC": messagei4300fREEMEMORYVMIC,
       "valuei4300fREEMEMORYVMIC": valuei4300fREEMEMORYVMIC,
       "cPULOADVMIC": cPULOADVMIC,
       "i4100cPULOADVMIC": i4100cPULOADVMIC,
       "tRAPi4100cPULOADVMIC": tRAPi4100cPULOADVMIC,
       "severityi4100cPULOADVMIC": severityi4100cPULOADVMIC,
       "messagei4100cPULOADVMIC": messagei4100cPULOADVMIC,
       "valuei4100cPULOADVMIC": valuei4100cPULOADVMIC,
       "i4200cPULOADVMIC": i4200cPULOADVMIC,
       "tRAPi4200cPULOADVMIC": tRAPi4200cPULOADVMIC,
       "severityi4200cPULOADVMIC": severityi4200cPULOADVMIC,
       "messagei4200cPULOADVMIC": messagei4200cPULOADVMIC,
       "valuei4200cPULOADVMIC": valuei4200cPULOADVMIC,
       "i4300cPULOADVMIC": i4300cPULOADVMIC,
       "tRAPi4300cPULOADVMIC": tRAPi4300cPULOADVMIC,
       "severityi4300cPULOADVMIC": severityi4300cPULOADVMIC,
       "messagei4300cPULOADVMIC": messagei4300cPULOADVMIC,
       "valuei4300cPULOADVMIC": valuei4300cPULOADVMIC,
       "fREESWAPVMIC": fREESWAPVMIC,
       "i4100fREESWAPVMIC": i4100fREESWAPVMIC,
       "tRAPi4100fREESWAPVMIC": tRAPi4100fREESWAPVMIC,
       "severityi4100fREESWAPVMIC": severityi4100fREESWAPVMIC,
       "messagei4100fREESWAPVMIC": messagei4100fREESWAPVMIC,
       "valuei4100fREESWAPVMIC": valuei4100fREESWAPVMIC,
       "i4200fREESWAPVMIC": i4200fREESWAPVMIC,
       "tRAPi4200fREESWAPVMIC": tRAPi4200fREESWAPVMIC,
       "severityi4200fREESWAPVMIC": severityi4200fREESWAPVMIC,
       "messagei4200fREESWAPVMIC": messagei4200fREESWAPVMIC,
       "valuei4200fREESWAPVMIC": valuei4200fREESWAPVMIC,
       "i4300fREESWAPVMIC": i4300fREESWAPVMIC,
       "tRAPi4300fREESWAPVMIC": tRAPi4300fREESWAPVMIC,
       "severityi4300fREESWAPVMIC": severityi4300fREESWAPVMIC,
       "messagei4300fREESWAPVMIC": messagei4300fREESWAPVMIC,
       "valuei4300fREESWAPVMIC": valuei4300fREESWAPVMIC,
       "eTHINTSTATUSVMIC": eTHINTSTATUSVMIC,
       "i4100eTHINTSTATUSVMIC": i4100eTHINTSTATUSVMIC,
       "tRAPi4100eTHINTSTATUSVMIC": tRAPi4100eTHINTSTATUSVMIC,
       "severityi4100eTHINTSTATUSVMIC": severityi4100eTHINTSTATUSVMIC,
       "messagei4100eTHINTSTATUSVMIC": messagei4100eTHINTSTATUSVMIC,
       "valuei4100eTHINTSTATUSVMIC": valuei4100eTHINTSTATUSVMIC,
       "i4200eTHINTSTATUSVMIC": i4200eTHINTSTATUSVMIC,
       "tRAPi4200eTHINTSTATUSVMIC": tRAPi4200eTHINTSTATUSVMIC,
       "severityi4200eTHINTSTATUSVMIC": severityi4200eTHINTSTATUSVMIC,
       "messagei4200eTHINTSTATUSVMIC": messagei4200eTHINTSTATUSVMIC,
       "valuei4200eTHINTSTATUSVMIC": valuei4200eTHINTSTATUSVMIC,
       "i4300eTHINTSTATUSVMIC": i4300eTHINTSTATUSVMIC,
       "tRAPi4300eTHINTSTATUSVMIC": tRAPi4300eTHINTSTATUSVMIC,
       "severityi4300eTHINTSTATUSVMIC": severityi4300eTHINTSTATUSVMIC,
       "messagei4300eTHINTSTATUSVMIC": messagei4300eTHINTSTATUSVMIC,
       "valuei4300eTHINTSTATUSVMIC": valuei4300eTHINTSTATUSVMIC,
       "cRONSTATUSVMIC": cRONSTATUSVMIC,
       "i4100cRONSTATUSVMIC": i4100cRONSTATUSVMIC,
       "tRAPi4100cRONSTATUSVMIC": tRAPi4100cRONSTATUSVMIC,
       "severityi4100cRONSTATUSVMIC": severityi4100cRONSTATUSVMIC,
       "messagei4100cRONSTATUSVMIC": messagei4100cRONSTATUSVMIC,
       "valuei4100cRONSTATUSVMIC": valuei4100cRONSTATUSVMIC,
       "i4200cRONSTATUSVMIC": i4200cRONSTATUSVMIC,
       "tRAPi4200cRONSTATUSVMIC": tRAPi4200cRONSTATUSVMIC,
       "severityi4200cRONSTATUSVMIC": severityi4200cRONSTATUSVMIC,
       "messagei4200cRONSTATUSVMIC": messagei4200cRONSTATUSVMIC,
       "valuei4200cRONSTATUSVMIC": valuei4200cRONSTATUSVMIC,
       "i4300cRONSTATUSVMIC": i4300cRONSTATUSVMIC,
       "tRAPi4300cRONSTATUSVMIC": tRAPi4300cRONSTATUSVMIC,
       "severityi4300cRONSTATUSVMIC": severityi4300cRONSTATUSVMIC,
       "messagei4300cRONSTATUSVMIC": messagei4300cRONSTATUSVMIC,
       "valuei4300cRONSTATUSVMIC": valuei4300cRONSTATUSVMIC,
       "mONITSTATUSVMIC": mONITSTATUSVMIC,
       "i4100mONITSTATUSVMIC": i4100mONITSTATUSVMIC,
       "tRAPi4100mONITSTATUSVMIC": tRAPi4100mONITSTATUSVMIC,
       "severityi4100mONITSTATUSVMIC": severityi4100mONITSTATUSVMIC,
       "messagei4100mONITSTATUSVMIC": messagei4100mONITSTATUSVMIC,
       "valuei4100mONITSTATUSVMIC": valuei4100mONITSTATUSVMIC,
       "i4200mONITSTATUSVMIC": i4200mONITSTATUSVMIC,
       "tRAPi4200mONITSTATUSVMIC": tRAPi4200mONITSTATUSVMIC,
       "severityi4200mONITSTATUSVMIC": severityi4200mONITSTATUSVMIC,
       "messagei4200mONITSTATUSVMIC": messagei4200mONITSTATUSVMIC,
       "valuei4200mONITSTATUSVMIC": valuei4200mONITSTATUSVMIC,
       "i4300mONITSTATUSVMIC": i4300mONITSTATUSVMIC,
       "tRAPi4300mONITSTATUSVMIC": tRAPi4300mONITSTATUSVMIC,
       "severityi4300mONITSTATUSVMIC": severityi4300mONITSTATUSVMIC,
       "messagei4300mONITSTATUSVMIC": messagei4300mONITSTATUSVMIC,
       "valuei4300mONITSTATUSVMIC": valuei4300mONITSTATUSVMIC,
       "cPUSTATUSVMIC": cPUSTATUSVMIC,
       "i4100cPUSTATUSVMIC": i4100cPUSTATUSVMIC,
       "tRAPi4100cPUSTATUSVMIC": tRAPi4100cPUSTATUSVMIC,
       "severityi4100cPUSTATUSVMIC": severityi4100cPUSTATUSVMIC,
       "messagei4100cPUSTATUSVMIC": messagei4100cPUSTATUSVMIC,
       "valuei4100cPUSTATUSVMIC": valuei4100cPUSTATUSVMIC,
       "i4200cPUSTATUSVMIC": i4200cPUSTATUSVMIC,
       "tRAPi4200cPUSTATUSVMIC": tRAPi4200cPUSTATUSVMIC,
       "severityi4200cPUSTATUSVMIC": severityi4200cPUSTATUSVMIC,
       "messagei4200cPUSTATUSVMIC": messagei4200cPUSTATUSVMIC,
       "valuei4200cPUSTATUSVMIC": valuei4200cPUSTATUSVMIC,
       "i4300cPUSTATUSVMIC": i4300cPUSTATUSVMIC,
       "tRAPi4300cPUSTATUSVMIC": tRAPi4300cPUSTATUSVMIC,
       "severityi4300cPUSTATUSVMIC": severityi4300cPUSTATUSVMIC,
       "messagei4300cPUSTATUSVMIC": messagei4300cPUSTATUSVMIC,
       "valuei4300cPUSTATUSVMIC": valuei4300cPUSTATUSVMIC,
       "vMPANELSTATUSVMIC": vMPANELSTATUSVMIC,
       "i4100vMPANELSTATUSVMIC": i4100vMPANELSTATUSVMIC,
       "trapi4100vMPANELSTATUSVMIC": trapi4100vMPANELSTATUSVMIC,
       "severityi4100vMPANELSTATUSVMIC": severityi4100vMPANELSTATUSVMIC,
       "messagei4100vMPANELSTATUSVMIC": messagei4100vMPANELSTATUSVMIC,
       "valuei4100vMPANELSTATUSVMIC": valuei4100vMPANELSTATUSVMIC,
       "i4200vMPANELSTATUSVMIC": i4200vMPANELSTATUSVMIC,
       "tRAPi4200vMPANELSTATUSVMIC": tRAPi4200vMPANELSTATUSVMIC,
       "severityi4200vMPANELSTATUSVMIC": severityi4200vMPANELSTATUSVMIC,
       "messagei4200vMPANELSTATUSVMIC": messagei4200vMPANELSTATUSVMIC,
       "valuei4200vMPANELSTATUSVMIC": valuei4200vMPANELSTATUSVMIC,
       "i4300vMPANELSTATUSVMIC": i4300vMPANELSTATUSVMIC,
       "tRAPi4300vMPANELSTATUSVMIC": tRAPi4300vMPANELSTATUSVMIC,
       "severityi4300vMPANELSTATUSVMIC": severityi4300vMPANELSTATUSVMIC,
       "messagei4300vMPANELSTATUSVMIC": messagei4300vMPANELSTATUSVMIC,
       "valuei4300vMPANELSTATUSVMIC": valuei4300vMPANELSTATUSVMIC,
       "vmlvs": vmlvs,
       "fREEROOTDISKVMLVS": fREEROOTDISKVMLVS,
       "i5100fREEROOTDISKVMLVS": i5100fREEROOTDISKVMLVS,
       "tRAPi5100fREEROOTDISKVMLVS": tRAPi5100fREEROOTDISKVMLVS,
       "severityi5100fREEROOTDISKVMLVS": severityi5100fREEROOTDISKVMLVS,
       "messagei5100fREEROOTDISKVMLVS": messagei5100fREEROOTDISKVMLVS,
       "valuei5100fREEROOTDISKVMLVS": valuei5100fREEROOTDISKVMLVS,
       "i5200fREEROOTDISKVMLVS": i5200fREEROOTDISKVMLVS,
       "tRAPi5200fREEROOTDISKVMLVS": tRAPi5200fREEROOTDISKVMLVS,
       "severityi5200fREEROOTDISKVMLVS": severityi5200fREEROOTDISKVMLVS,
       "messagei5200fREEROOTDISKVMLVS": messagei5200fREEROOTDISKVMLVS,
       "valuei5200fREEROOTDISKVMLVS": valuei5200fREEROOTDISKVMLVS,
       "fREEBOOTDISKVMLVS": fREEBOOTDISKVMLVS,
       "i5100fREEBOOTDISKVMLVS": i5100fREEBOOTDISKVMLVS,
       "tRAPi5100fREEBOOTDISKVMLVS": tRAPi5100fREEBOOTDISKVMLVS,
       "severityi5100fREEBOOTDISKVMLVS": severityi5100fREEBOOTDISKVMLVS,
       "messagei5100fREEBOOTDISKVMLVS": messagei5100fREEBOOTDISKVMLVS,
       "valuei5100fREEBOOTDISKVMLVS": valuei5100fREEBOOTDISKVMLVS,
       "i5200fREEBOOTDISKVMLVS": i5200fREEBOOTDISKVMLVS,
       "tRAPi5200fREEBOOTDISKVMLVS": tRAPi5200fREEBOOTDISKVMLVS,
       "severityi5200fREEBOOTDISKVMLVS": severityi5200fREEBOOTDISKVMLVS,
       "messagei5200fREEBOOTDISKVMLVS": messagei5200fREEBOOTDISKVMLVS,
       "valuei5200fREEBOOTDISKVMLVS": valuei5200fREEBOOTDISKVMLVS,
       "fREEMEMORYVMLVS": fREEMEMORYVMLVS,
       "i5100fREEMEMORYVMLVS": i5100fREEMEMORYVMLVS,
       "tRAPi5100fREEMEMORYVMLVS": tRAPi5100fREEMEMORYVMLVS,
       "severityi5100fREEMEMORYVMLVS": severityi5100fREEMEMORYVMLVS,
       "messagei5100fREEMEMORYVMLVS": messagei5100fREEMEMORYVMLVS,
       "valuei5100fREEMEMORYVMLVS": valuei5100fREEMEMORYVMLVS,
       "i5200fREEMEMORYVMLVS": i5200fREEMEMORYVMLVS,
       "tRAPi5200fREEMEMORYVMLVS": tRAPi5200fREEMEMORYVMLVS,
       "severityi5200fREEMEMORYVMLVS": severityi5200fREEMEMORYVMLVS,
       "messagei5200fREEMEMORYVMLVS": messagei5200fREEMEMORYVMLVS,
       "valuei5200fREEMEMORYVMLVS": valuei5200fREEMEMORYVMLVS,
       "cPULOADVMLVS": cPULOADVMLVS,
       "i5100cPULOADVMLVS": i5100cPULOADVMLVS,
       "tRAPi5100cPULOADVMLVS": tRAPi5100cPULOADVMLVS,
       "severityi5100cPULOADVMLVS": severityi5100cPULOADVMLVS,
       "messagei5100cPULOADVMLVS": messagei5100cPULOADVMLVS,
       "valuei5100cPULOADVMLVS": valuei5100cPULOADVMLVS,
       "i5200cPULOADVMLVS": i5200cPULOADVMLVS,
       "tRAPi5200cPULOADVMLVS": tRAPi5200cPULOADVMLVS,
       "severityi5200cPULOADVMLVS": severityi5200cPULOADVMLVS,
       "messagei5200cPULOADVMLVS": messagei5200cPULOADVMLVS,
       "valuei5200cPULOADVMLVS": valuei5200cPULOADVMLVS,
       "fREESWAPVMLVS": fREESWAPVMLVS,
       "i5100fREESWAPVMLVS": i5100fREESWAPVMLVS,
       "tRAPi5100fREESWAPVMLVS": tRAPi5100fREESWAPVMLVS,
       "severityi5100fREESWAPVMLVS": severityi5100fREESWAPVMLVS,
       "messagei5100fREESWAPVMLVS": messagei5100fREESWAPVMLVS,
       "valuei5100fREESWAPVMLVS": valuei5100fREESWAPVMLVS,
       "i5200fREESWAPVMLVS": i5200fREESWAPVMLVS,
       "tRAPi5200fREESWAPVMLVS": tRAPi5200fREESWAPVMLVS,
       "severityi5200fREESWAPVMLVS": severityi5200fREESWAPVMLVS,
       "messagei5200fREESWAPVMLVS": messagei5200fREESWAPVMLVS,
       "valuei5200fREESWAPVMLVS": valuei5200fREESWAPVMLVS,
       "eTHINTSTATUSVMLVS": eTHINTSTATUSVMLVS,
       "i5100eTHINTSTATUSVMLVS": i5100eTHINTSTATUSVMLVS,
       "tRAPi5100eTHINTSTATUSVMLVS": tRAPi5100eTHINTSTATUSVMLVS,
       "severityi5100eTHINTSTATUSVMLVS": severityi5100eTHINTSTATUSVMLVS,
       "messagei5100eTHINTSTATUSVMLVS": messagei5100eTHINTSTATUSVMLVS,
       "valuei5100eTHINTSTATUSVMLVS": valuei5100eTHINTSTATUSVMLVS,
       "i5200eTHINTSTATUSVMLVS": i5200eTHINTSTATUSVMLVS,
       "tRAPi5200eTHINTSTATUSVMLVS": tRAPi5200eTHINTSTATUSVMLVS,
       "severityi5200eTHINTSTATUSVMLVS": severityi5200eTHINTSTATUSVMLVS,
       "messagei5200eTHINTSTATUSVMLVS": messagei5200eTHINTSTATUSVMLVS,
       "valuei5200eTHINTSTATUSVMLVS": valuei5200eTHINTSTATUSVMLVS,
       "cRONSTATUSVMLVS": cRONSTATUSVMLVS,
       "i5100cRONSTATUSVMLVS": i5100cRONSTATUSVMLVS,
       "tRAPi5100cRONSTATUSVMLVS": tRAPi5100cRONSTATUSVMLVS,
       "severityi5100cRONSTATUSVMLVS": severityi5100cRONSTATUSVMLVS,
       "messagei5100cRONSTATUSVMLVS": messagei5100cRONSTATUSVMLVS,
       "valuei5100cRONSTATUSVMLVS": valuei5100cRONSTATUSVMLVS,
       "i5200cRONSTATUSVMLVS": i5200cRONSTATUSVMLVS,
       "tRAPi5200cRONSTATUSVMLVS": tRAPi5200cRONSTATUSVMLVS,
       "severityi5200cRONSTATUSVMLVS": severityi5200cRONSTATUSVMLVS,
       "messagei5200cRONSTATUSVMLVS": messagei5200cRONSTATUSVMLVS,
       "valuei5200cRONSTATUSVMLVS": valuei5200cRONSTATUSVMLVS,
       "mONITSTATUSVMLVS": mONITSTATUSVMLVS,
       "i5100mONITSTATUSVMLVS": i5100mONITSTATUSVMLVS,
       "tRAPi5100mONITSTATUSVMLVS": tRAPi5100mONITSTATUSVMLVS,
       "severityi5100mONITSTATUSVMLVS": severityi5100mONITSTATUSVMLVS,
       "messagei5100mONITSTATUSVMLVS": messagei5100mONITSTATUSVMLVS,
       "valuei5100mONITSTATUSVMLVS": valuei5100mONITSTATUSVMLVS,
       "i5200mONITSTATUSVMLVS": i5200mONITSTATUSVMLVS,
       "tRAPi5200mONITSTATUSVMLVS": tRAPi5200mONITSTATUSVMLVS,
       "severityi5200mONITSTATUSVMLVS": severityi5200mONITSTATUSVMLVS,
       "messagei5200mONITSTATUSVMLVS": messagei5200mONITSTATUSVMLVS,
       "valuei5200mONITSTATUSVMLVS": valuei5200mONITSTATUSVMLVS,
       "pULSESTATUSVMLVS": pULSESTATUSVMLVS,
       "i5100pULSESTATUSVMLVS": i5100pULSESTATUSVMLVS,
       "tRAPi5100pULSESTATUSVMLVS": tRAPi5100pULSESTATUSVMLVS,
       "severityi5100pULSESTATUSVMLVS": severityi5100pULSESTATUSVMLVS,
       "messagei5100pULSESTATUSVMLVS": messagei5100pULSESTATUSVMLVS,
       "valuei5100pULSESTATUSVMLVS": valuei5100pULSESTATUSVMLVS,
       "i5200pULSESTATUSVMLVS": i5200pULSESTATUSVMLVS,
       "tRAPi5200pULSESTATUSVMLVS": tRAPi5200pULSESTATUSVMLVS,
       "severityi5200pULSESTATUSVMLVS": severityi5200pULSESTATUSVMLVS,
       "messagei5200pULSESTATUSVMLVS": messagei5200pULSESTATUSVMLVS,
       "valuei5200pULSESTATUSVMLVS": valuei5200pULSESTATUSVMLVS,
       "cPUSTATUSVMLVS": cPUSTATUSVMLVS,
       "i5100cPUSTATUSVMLVS": i5100cPUSTATUSVMLVS,
       "tRAPi5100cPUSTATUSVMLVS": tRAPi5100cPUSTATUSVMLVS,
       "severityi5100cPUSTATUSVMLVS": severityi5100cPUSTATUSVMLVS,
       "messagei5100cPUSTATUSVMLVS": messagei5100cPUSTATUSVMLVS,
       "valuei5100cPUSTATUSVMLVS": valuei5100cPUSTATUSVMLVS,
       "i5200cPUSTATUSVMLVS": i5200cPUSTATUSVMLVS,
       "tRAPi5200cPUSTATUSVMLVS": tRAPi5200cPUSTATUSVMLVS,
       "severityi5200cPUSTATUSVMLVS": severityi5200cPUSTATUSVMLVS,
       "messagei5200cPUSTATUSVMLVS": messagei5200cPUSTATUSVMLVS,
       "valuei5200cPUSTATUSVMLVS": valuei5200cPUSTATUSVMLVS,
       "lVSSTATUSVMLVS": lVSSTATUSVMLVS,
       "i5100lVSSTATUSVMLVS": i5100lVSSTATUSVMLVS,
       "tRAPi5100lVSSTATUSVMLVS": tRAPi5100lVSSTATUSVMLVS,
       "severityi5100lVSSTATUSVMLVS": severityi5100lVSSTATUSVMLVS,
       "messagei5100lVSSTATUSVMLVS": messagei5100lVSSTATUSVMLVS,
       "valuei5100lVSSTATUSVMLVS": valuei5100lVSSTATUSVMLVS,
       "i5200lVSSTATUSVMLVS": i5200lVSSTATUSVMLVS,
       "tRAPi5200lVSSTATUSVMLVS": tRAPi5200lVSSTATUSVMLVS,
       "severityi5200lVSSTATUSVMLVS": severityi5200lVSSTATUSVMLVS,
       "messagei5200lVSSTATUSVMLVS": messagei5200lVSSTATUSVMLVS,
       "valuei5200lVSSTATUSVMLVS": valuei5200lVSSTATUSVMLVS}
)
