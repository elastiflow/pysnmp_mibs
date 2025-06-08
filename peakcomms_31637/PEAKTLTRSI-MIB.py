# SNMP MIB module (PEAKTLTRSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKTLTRSI-MIB.mib
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

peaktltrSIModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5)
)
if mibBuilder.loadTexts:
    peaktltrSIModule.setRevisions(
        ("2015-10-14 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TltrSIInput_Type(OctetString):
    """Custom type tltrSIInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TltrSIInput_Type.__name__ = "OctetString"
_TltrSIInput_Object = MibScalar
tltrSIInput = _TltrSIInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 1),
    _TltrSIInput_Type()
)
tltrSIInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tltrSIInput.setStatus("current")


class _TltrSIWantedInput_Type(OctetString):
    """Custom type tltrSIWantedInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TltrSIWantedInput_Type.__name__ = "OctetString"
_TltrSIWantedInput_Object = MibScalar
tltrSIWantedInput = _TltrSIWantedInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 2),
    _TltrSIWantedInput_Type()
)
tltrSIWantedInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltrSIWantedInput.setStatus("current")


class _TltrSIOutput_Type(OctetString):
    """Custom type tltrSIOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TltrSIOutput_Type.__name__ = "OctetString"
_TltrSIOutput_Object = MibScalar
tltrSIOutput = _TltrSIOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 3),
    _TltrSIOutput_Type()
)
tltrSIOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tltrSIOutput.setStatus("current")


class _TltrSIWantedOutput_Type(OctetString):
    """Custom type tltrSIWantedOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_TltrSIWantedOutput_Type.__name__ = "OctetString"
_TltrSIWantedOutput_Object = MibScalar
tltrSIWantedOutput = _TltrSIWantedOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 4),
    _TltrSIWantedOutput_Type()
)
tltrSIWantedOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltrSIWantedOutput.setStatus("current")
_TltrSIConvGroups_ObjectIdentity = ObjectIdentity
tltrSIConvGroups = _TltrSIConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 110)
)
_TltrSIConvConformance_ObjectIdentity = ObjectIdentity
tltrSIConvConformance = _TltrSIConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 111)
)

# Managed Objects groups

tltrSICNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 110, 1)
)
tltrSICNFReqGrp.setObjects(
      *(("PEAKTLTRSI-MIB", "tltrSIInput"),
        ("PEAKTLTRSI-MIB", "tltrSIWantedInput"),
        ("PEAKTLTRSI-MIB", "tltrSIOutput"),
        ("PEAKTLTRSI-MIB", "tltrSIWantedOutput"))
)
if mibBuilder.loadTexts:
    tltrSICNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tltrSICNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 5, 111, 1)
)
tltrSICNFCompliance.setObjects(
    ("PEAKTLTRSI-MIB", "tltrSICNFReqGrp")
)
if mibBuilder.loadTexts:
    tltrSICNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKTLTRSI-MIB",
    **{"peaktltrSIModule": peaktltrSIModule,
       "tltrSIInput": tltrSIInput,
       "tltrSIWantedInput": tltrSIWantedInput,
       "tltrSIOutput": tltrSIOutput,
       "tltrSIWantedOutput": tltrSIWantedOutput,
       "tltrSIConvGroups": tltrSIConvGroups,
       "tltrSICNFReqGrp": tltrSICNFReqGrp,
       "tltrSIConvConformance": tltrSIConvConformance,
       "tltrSICNFCompliance": tltrSICNFCompliance}
)
