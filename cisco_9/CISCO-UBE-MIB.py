# SNMP MIB module (CISCO-UBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UBE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:58:44 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoUbeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764)
)
if mibBuilder.loadTexts:
    ciscoUbeMIB.setRevisions(
        ("2010-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUbeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUbeMIBObjects = _CiscoUbeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0)
)
_CubeEnabled_Type = TruthValue
_CubeEnabled_Object = MibScalar
cubeEnabled = _CubeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 1),
    _CubeEnabled_Type()
)
cubeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubeEnabled.setStatus("current")
_CubeVersion_Type = SnmpAdminString
_CubeVersion_Object = MibScalar
cubeVersion = _CubeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 2),
    _CubeVersion_Type()
)
cubeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubeVersion.setStatus("current")


class _CubeTotalSessionAllowed_Type(Unsigned32):
    """Custom type cubeTotalSessionAllowed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_CubeTotalSessionAllowed_Type.__name__ = "Unsigned32"
_CubeTotalSessionAllowed_Object = MibScalar
cubeTotalSessionAllowed = _CubeTotalSessionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 3),
    _CubeTotalSessionAllowed_Type()
)
cubeTotalSessionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubeTotalSessionAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cubeTotalSessionAllowed.setUnits("session")
_CiscoUbeMIBConform_ObjectIdentity = ObjectIdentity
ciscoUbeMIBConform = _CiscoUbeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1)
)
_CiscoUbeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUbeMIBCompliances = _CiscoUbeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1)
)
_CiscoUbeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUbeMIBGroups = _CiscoUbeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2)
)

# Managed Objects groups

ciscoUbeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2, 1)
)
ciscoUbeMIBGroup.setObjects(
      *(("CISCO-UBE-MIB", "cubeEnabled"),
        ("CISCO-UBE-MIB", "cubeVersion"),
        ("CISCO-UBE-MIB", "cubeTotalSessionAllowed"))
)
if mibBuilder.loadTexts:
    ciscoUbeMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCubeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1, 1)
)
ciscoCubeMIBCompliance.setObjects(
    ("CISCO-UBE-MIB", "ciscoUbeMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoCubeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UBE-MIB",
    **{"ciscoUbeMIB": ciscoUbeMIB,
       "ciscoUbeMIBObjects": ciscoUbeMIBObjects,
       "cubeEnabled": cubeEnabled,
       "cubeVersion": cubeVersion,
       "cubeTotalSessionAllowed": cubeTotalSessionAllowed,
       "ciscoUbeMIBConform": ciscoUbeMIBConform,
       "ciscoUbeMIBCompliances": ciscoUbeMIBCompliances,
       "ciscoCubeMIBCompliance": ciscoCubeMIBCompliance,
       "ciscoUbeMIBGroups": ciscoUbeMIBGroups,
       "ciscoUbeMIBGroup": ciscoUbeMIBGroup}
)
