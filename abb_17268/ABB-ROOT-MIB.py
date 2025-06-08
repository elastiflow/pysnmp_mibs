# SNMP MIB module (ABB-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/ABB-ROOT-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

utilityCommProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818)
)
if mibBuilder.loadTexts:
    utilityCommProducts.setRevisions(
        ("2016-09-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Abb_ObjectIdentity = ObjectIdentity
abb = _Abb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268)
)
_Fox_ObjectIdentity = ObjectIdentity
fox = _Fox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1)
)
_Acc_ObjectIdentity = ObjectIdentity
acc = _Acc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 2)
)
_Plc_ObjectIdentity = ObjectIdentity
plc = _Plc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 3)
)
_Tpe_ObjectIdentity = ObjectIdentity
tpe = _Tpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 4)
)
_RtuISW_ObjectIdentity = ObjectIdentity
rtuISW = _RtuISW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 5)
)
_ArFamilyCommProducts_ObjectIdentity = ObjectIdentity
arFamilyCommProducts = _ArFamilyCommProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ABB-ROOT-MIB",
    **{"abb": abb,
       "utilityCommProducts": utilityCommProducts,
       "fox": fox,
       "acc": acc,
       "plc": plc,
       "tpe": tpe,
       "rtuISW": rtuISW,
       "arFamilyCommProducts": arFamilyCommProducts}
)
