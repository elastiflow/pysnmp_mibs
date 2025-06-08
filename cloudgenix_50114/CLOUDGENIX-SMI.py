# SNMP MIB module (CLOUDGENIX-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cloudgenix_50114/CLOUDGENIX-SMI.mib
# Produced by pysmi-1.6.1 at Wed Jun  4 13:56:22 2025
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

cloudgenix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50114)
)
if mibBuilder.loadTexts:
    cloudgenix.setRevisions(
        ("2017-06-19 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CgxDegreesC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class CgxVolts(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


# MIB Managed Objects in the order of their OIDs

_CgxObjects_ObjectIdentity = ObjectIdentity
cgxObjects = _CgxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 1)
)
_CgxConformance_ObjectIdentity = ObjectIdentity
cgxConformance = _CgxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 2)
)
_CgxCompliances_ObjectIdentity = ObjectIdentity
cgxCompliances = _CgxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 2, 1)
)
_CgxGroups_ObjectIdentity = ObjectIdentity
cgxGroups = _CgxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 2, 2)
)
_CgxMgmt_ObjectIdentity = ObjectIdentity
cgxMgmt = _CgxMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10)
)
if mibBuilder.loadTexts:
    cgxMgmt.setStatus("current")
_CgxProducts_ObjectIdentity = ObjectIdentity
cgxProducts = _CgxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 11)
)
if mibBuilder.loadTexts:
    cgxProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cloudgenixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 50114, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cloudgenixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLOUDGENIX-SMI",
    **{"CgxDegreesC": CgxDegreesC,
       "CgxVolts": CgxVolts,
       "cloudgenix": cloudgenix,
       "cgxObjects": cgxObjects,
       "cgxConformance": cgxConformance,
       "cgxCompliances": cgxCompliances,
       "cloudgenixCompliance": cloudgenixCompliance,
       "cgxGroups": cgxGroups,
       "cgxMgmt": cgxMgmt,
       "cgxProducts": cgxProducts}
)
