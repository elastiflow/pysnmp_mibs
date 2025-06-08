# SNMP MIB module (SYS4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sys4_39996/SYS4-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:57:44 2025
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

sys4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39996)
)
if mibBuilder.loadTexts:
    sys4.setRevisions(
        ("2012-11-08 08:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sys4SNMP_ObjectIdentity = ObjectIdentity
sys4SNMP = _Sys4SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161)
)
if mibBuilder.loadTexts:
    sys4SNMP.setStatus("current")
_Sys4SNMPGlobalRegistrations_ObjectIdentity = ObjectIdentity
sys4SNMPGlobalRegistrations = _Sys4SNMPGlobalRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 1)
)
if mibBuilder.loadTexts:
    sys4SNMPGlobalRegistrations.setStatus("current")
_Sys4SNMPProdRegistrations_ObjectIdentity = ObjectIdentity
sys4SNMPProdRegistrations = _Sys4SNMPProdRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 1, 1)
)
if mibBuilder.loadTexts:
    sys4SNMPProdRegistrations.setStatus("current")
_Sys4SNMPProducts_ObjectIdentity = ObjectIdentity
sys4SNMPProducts = _Sys4SNMPProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 2)
)
if mibBuilder.loadTexts:
    sys4SNMPProducts.setStatus("current")
_Sys4SNMPExperimental_ObjectIdentity = ObjectIdentity
sys4SNMPExperimental = _Sys4SNMPExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99)
)
if mibBuilder.loadTexts:
    sys4SNMPExperimental.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYS4-MIB",
    **{"sys4": sys4,
       "sys4SNMP": sys4SNMP,
       "sys4SNMPGlobalRegistrations": sys4SNMPGlobalRegistrations,
       "sys4SNMPProdRegistrations": sys4SNMPProdRegistrations,
       "sys4SNMPProducts": sys4SNMPProducts,
       "sys4SNMPExperimental": sys4SNMPExperimental}
)
