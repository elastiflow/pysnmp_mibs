# SNMP MIB module (PEAKTLTHSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKTLTHSI-MIB.mib
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

(nsConverters,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "nsConverters")

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

peaktlthSIModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3)
)
if mibBuilder.loadTexts:
    peaktlthSIModule.setRevisions(
        ("2015-09-15 10:00",
         "2013-12-17 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TlthSIInput_Type(OctetString):
    """Custom type tlthSIInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TlthSIInput_Type.__name__ = "OctetString"
_TlthSIInput_Object = MibScalar
tlthSIInput = _TlthSIInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 1),
    _TlthSIInput_Type()
)
tlthSIInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlthSIInput.setStatus("current")


class _TlthSIWantedInput_Type(OctetString):
    """Custom type tlthSIWantedInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TlthSIWantedInput_Type.__name__ = "OctetString"
_TlthSIWantedInput_Object = MibScalar
tlthSIWantedInput = _TlthSIWantedInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 2),
    _TlthSIWantedInput_Type()
)
tlthSIWantedInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlthSIWantedInput.setStatus("current")


class _TlthSIOutput_Type(OctetString):
    """Custom type tlthSIOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TlthSIOutput_Type.__name__ = "OctetString"
_TlthSIOutput_Object = MibScalar
tlthSIOutput = _TlthSIOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 3),
    _TlthSIOutput_Type()
)
tlthSIOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlthSIOutput.setStatus("current")


class _TlthSIWantedOutput_Type(OctetString):
    """Custom type tlthSIWantedOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TlthSIWantedOutput_Type.__name__ = "OctetString"
_TlthSIWantedOutput_Object = MibScalar
tlthSIWantedOutput = _TlthSIWantedOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 4),
    _TlthSIWantedOutput_Type()
)
tlthSIWantedOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlthSIWantedOutput.setStatus("current")
_TlthSIConvGroups_ObjectIdentity = ObjectIdentity
tlthSIConvGroups = _TlthSIConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 110)
)
_TlthSIConvConformance_ObjectIdentity = ObjectIdentity
tlthSIConvConformance = _TlthSIConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 111)
)

# Managed Objects groups

tlthSICNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 110, 1)
)
tlthSICNFReqGrp.setObjects(
      *(("PEAKTLTHSI-MIB", "tlthSIInput"),
        ("PEAKTLTHSI-MIB", "tlthSIWantedInput"),
        ("PEAKTLTHSI-MIB", "tlthSIOutput"),
        ("PEAKTLTHSI-MIB", "tlthSIWantedOutput"))
)
if mibBuilder.loadTexts:
    tlthSICNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tlthSICNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 3, 111, 1)
)
tlthSICNFCompliance.setObjects(
    ("PEAKTLTHSI-MIB", "tlthSICNFReqGrp")
)
if mibBuilder.loadTexts:
    tlthSICNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKTLTHSI-MIB",
    **{"peaktlthSIModule": peaktlthSIModule,
       "tlthSIInput": tlthSIInput,
       "tlthSIWantedInput": tlthSIWantedInput,
       "tlthSIOutput": tlthSIOutput,
       "tlthSIWantedOutput": tlthSIWantedOutput,
       "tlthSIConvGroups": tlthSIConvGroups,
       "tlthSICNFReqGrp": tlthSICNFReqGrp,
       "tlthSIConvConformance": tlthSIConvConformance,
       "tlthSICNFCompliance": tlthSICNFCompliance}
)
