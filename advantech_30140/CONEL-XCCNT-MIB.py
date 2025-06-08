# SNMP MIB module (CONEL-XCCNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/advantech_30140/CONEL-XCCNT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:15:06 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 2)
)
_Xccnt_ObjectIdentity = ObjectIdentity
xccnt = _Xccnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1)
)
_XccntAn1_Type = Integer32
_XccntAn1_Object = MibScalar
xccntAn1 = _XccntAn1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 1),
    _XccntAn1_Type()
)
xccntAn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntAn1.setStatus("current")
_XccntAn2_Type = Integer32
_XccntAn2_Object = MibScalar
xccntAn2 = _XccntAn2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 2),
    _XccntAn2_Type()
)
xccntAn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntAn2.setStatus("current")
_XccntCnt1_Type = Counter32
_XccntCnt1_Object = MibScalar
xccntCnt1 = _XccntCnt1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 3),
    _XccntCnt1_Type()
)
xccntCnt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntCnt1.setStatus("current")
_XccntCnt2_Type = Counter32
_XccntCnt2_Object = MibScalar
xccntCnt2 = _XccntCnt2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 4),
    _XccntCnt2_Type()
)
xccntCnt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntCnt2.setStatus("current")
_XccntBin1_Type = Gauge32
_XccntBin1_Object = MibScalar
xccntBin1 = _XccntBin1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 5),
    _XccntBin1_Type()
)
xccntBin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin1.setStatus("current")
_XccntBin2_Type = Gauge32
_XccntBin2_Object = MibScalar
xccntBin2 = _XccntBin2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 6),
    _XccntBin2_Type()
)
xccntBin2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin2.setStatus("current")
_XccntBin3_Type = Gauge32
_XccntBin3_Object = MibScalar
xccntBin3 = _XccntBin3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 7),
    _XccntBin3_Type()
)
xccntBin3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin3.setStatus("current")
_XccntBin4_Type = Gauge32
_XccntBin4_Object = MibScalar
xccntBin4 = _XccntBin4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 8),
    _XccntBin4_Type()
)
xccntBin4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccntBin4.setStatus("current")
_XccntOut1_Type = Gauge32
_XccntOut1_Object = MibScalar
xccntOut1 = _XccntOut1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 2, 1, 9),
    _XccntOut1_Type()
)
xccntOut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xccntOut1.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-XCCNT-MIB",
    **{"conel": conel,
       "protocols": protocols,
       "xccnt": xccnt,
       "xccntAn1": xccntAn1,
       "xccntAn2": xccntAn2,
       "xccntCnt1": xccntCnt1,
       "xccntCnt2": xccntCnt2,
       "xccntBin1": xccntBin1,
       "xccntBin2": xccntBin2,
       "xccntBin3": xccntBin3,
       "xccntBin4": xccntBin4,
       "xccntOut1": xccntOut1}
)
