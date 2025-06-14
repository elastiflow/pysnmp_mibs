# SNMP MIB module (BASIS-ONLINE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/BASIS-ONLINE-DIAG-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:03:53 2025
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

(axisDiagnostics,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "axisDiagnostics")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

basisOnlineDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 80)
)
if mibBuilder.loadTexts:
    basisOnlineDiagMIB.setRevisions(
        ("2003-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OnlineDiagnostics_ObjectIdentity = ObjectIdentity
onlineDiagnostics = _OnlineDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 3)
)


class _DiagType_Type(Integer32):
    """Custom type diagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("post", 1),
          ("onlinediag", 2))
    )


_DiagType_Type.__name__ = "Integer32"
_DiagType_Object = MibScalar
diagType = _DiagType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 1),
    _DiagType_Type()
)
diagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagType.setStatus("current")


class _DiagResult_Type(Integer32):
    """Custom type diagResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("failed", 2))
    )


_DiagResult_Type.__name__ = "Integer32"
_DiagResult_Object = MibScalar
diagResult = _DiagResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 2),
    _DiagResult_Type()
)
diagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagResult.setStatus("current")


class _DiagTestId_Type(Integer32):
    """Custom type diagTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiagTestId_Type.__name__ = "Integer32"
_DiagTestId_Object = MibScalar
diagTestId = _DiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 3),
    _DiagTestId_Type()
)
diagTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diagTestId.setStatus("current")
_BoDiagMIBConformance_ObjectIdentity = ObjectIdentity
boDiagMIBConformance = _BoDiagMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 80, 2)
)
_BoDiagMIBCompliances_ObjectIdentity = ObjectIdentity
boDiagMIBCompliances = _BoDiagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1)
)
_BoDiagMIBGroups_ObjectIdentity = ObjectIdentity
boDiagMIBGroups = _BoDiagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2)
)

# Managed Objects groups

boDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2, 1)
)
boDiagGroup.setObjects(
      *(("BASIS-ONLINE-DIAG-MIB", "diagType"),
        ("BASIS-ONLINE-DIAG-MIB", "diagResult"),
        ("BASIS-ONLINE-DIAG-MIB", "diagTestId"))
)
if mibBuilder.loadTexts:
    boDiagGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

boDiagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1, 1)
)
boDiagCompliance.setObjects(
    ("BASIS-ONLINE-DIAG-MIB", "boDiagGroup")
)
if mibBuilder.loadTexts:
    boDiagCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASIS-ONLINE-DIAG-MIB",
    **{"onlineDiagnostics": onlineDiagnostics,
       "diagType": diagType,
       "diagResult": diagResult,
       "diagTestId": diagTestId,
       "basisOnlineDiagMIB": basisOnlineDiagMIB,
       "boDiagMIBConformance": boDiagMIBConformance,
       "boDiagMIBCompliances": boDiagMIBCompliances,
       "boDiagCompliance": boDiagCompliance,
       "boDiagMIBGroups": boDiagMIBGroups,
       "boDiagGroup": boDiagGroup}
)
