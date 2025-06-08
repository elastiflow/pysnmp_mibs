# SNMP MIB module (PEAKTLTR2225-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKTLTR2225-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(indvUnits,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "indvUnits")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

peakTLTR2225Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060)
)
if mibBuilder.loadTexts:
    peakTLTR2225Module.setRevisions(
        ("2015-09-15 10:00",
         "2015-04-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tltr2225Attenuation_Type = OctetString
_Tltr2225Attenuation_Object = MibScalar
tltr2225Attenuation = _Tltr2225Attenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 1),
    _Tltr2225Attenuation_Type()
)
tltr2225Attenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltr2225Attenuation.setStatus("current")


class _Tltr2225Input_Type(OctetString):
    """Custom type tltr2225Input based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Tltr2225Input_Type.__name__ = "OctetString"
_Tltr2225Input_Object = MibScalar
tltr2225Input = _Tltr2225Input_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 2),
    _Tltr2225Input_Type()
)
tltr2225Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tltr2225Input.setStatus("current")


class _Tltr2225Output_Type(OctetString):
    """Custom type tltr2225Output based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Tltr2225Output_Type.__name__ = "OctetString"
_Tltr2225Output_Object = MibScalar
tltr2225Output = _Tltr2225Output_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 3),
    _Tltr2225Output_Type()
)
tltr2225Output.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tltr2225Output.setStatus("current")


class _Tltr2225WantedInput_Type(OctetString):
    """Custom type tltr2225WantedInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Tltr2225WantedInput_Type.__name__ = "OctetString"
_Tltr2225WantedInput_Object = MibScalar
tltr2225WantedInput = _Tltr2225WantedInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 4),
    _Tltr2225WantedInput_Type()
)
tltr2225WantedInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltr2225WantedInput.setStatus("current")


class _Tltr2225WantedOutput_Type(OctetString):
    """Custom type tltr2225WantedOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Tltr2225WantedOutput_Type.__name__ = "OctetString"
_Tltr2225WantedOutput_Object = MibScalar
tltr2225WantedOutput = _Tltr2225WantedOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 5),
    _Tltr2225WantedOutput_Type()
)
tltr2225WantedOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltr2225WantedOutput.setStatus("current")
_Tltr2225ConvGroups_ObjectIdentity = ObjectIdentity
tltr2225ConvGroups = _Tltr2225ConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 110)
)
_Tltr2225ConvConformance_ObjectIdentity = ObjectIdentity
tltr2225ConvConformance = _Tltr2225ConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 111)
)

# Managed Objects groups

tltr2225AttenGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 110, 1)
)
tltr2225AttenGrp.setObjects(
    ("PEAKTLTR2225-MIB", "tltr2225Attenuation")
)
if mibBuilder.loadTexts:
    tltr2225AttenGrp.setStatus("current")

tltr2225InputGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 110, 2)
)
tltr2225InputGrp.setObjects(
      *(("PEAKTLTR2225-MIB", "tltr2225Input"),
        ("PEAKTLTR2225-MIB", "tltr2225WantedInput"))
)
if mibBuilder.loadTexts:
    tltr2225InputGrp.setStatus("current")

tltr2225OutputGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 110, 3)
)
tltr2225OutputGrp.setObjects(
      *(("PEAKTLTR2225-MIB", "tltr2225Output"),
        ("PEAKTLTR2225-MIB", "tltr2225WantedOutput"))
)
if mibBuilder.loadTexts:
    tltr2225OutputGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tltr2225CNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 5060, 111, 1)
)
tltr2225CNFCompliance.setObjects(
      *(("PEAKTLTR2225-MIB", "tltr2225AttenGrp"),
        ("PEAKTLTR2225-MIB", "tltr2225InputGrp"),
        ("PEAKTLTR2225-MIB", "tltr2225OutputGrp"))
)
if mibBuilder.loadTexts:
    tltr2225CNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKTLTR2225-MIB",
    **{"peakTLTR2225Module": peakTLTR2225Module,
       "tltr2225Attenuation": tltr2225Attenuation,
       "tltr2225Input": tltr2225Input,
       "tltr2225Output": tltr2225Output,
       "tltr2225WantedInput": tltr2225WantedInput,
       "tltr2225WantedOutput": tltr2225WantedOutput,
       "tltr2225ConvGroups": tltr2225ConvGroups,
       "tltr2225AttenGrp": tltr2225AttenGrp,
       "tltr2225InputGrp": tltr2225InputGrp,
       "tltr2225OutputGrp": tltr2225OutputGrp,
       "tltr2225ConvConformance": tltr2225ConvConformance,
       "tltr2225CNFCompliance": tltr2225CNFCompliance}
)
