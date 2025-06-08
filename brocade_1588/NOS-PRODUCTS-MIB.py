# SNMP MIB module (NOS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1588/NOS-PRODUCTS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:12:33 2025
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

(nos,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "nos")

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

nosProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiRegistration_ObjectIdentity = ObjectIdentity
bcsiRegistration = _BcsiRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1)
)
_BcsiChassisTypes_ObjectIdentity = ObjectIdentity
bcsiChassisTypes = _BcsiChassisTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1)
)
_Vdx6720P24_ObjectIdentity = ObjectIdentity
vdx6720P24 = _Vdx6720P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 1)
)
_Vdx6720P60_ObjectIdentity = ObjectIdentity
vdx6720P60 = _Vdx6720P60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 2)
)
_Vdx6730P32_ObjectIdentity = ObjectIdentity
vdx6730P32 = _Vdx6730P32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 3)
)
_Vdx6730P76_ObjectIdentity = ObjectIdentity
vdx6730P76 = _Vdx6730P76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 4)
)
_Vdx6710P54_ObjectIdentity = ObjectIdentity
vdx6710P54 = _Vdx6710P54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 5)
)
_Vdx6746_ObjectIdentity = ObjectIdentity
vdx6746 = _Vdx6746_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 112)
)
_BcsiCardTypes_ObjectIdentity = ObjectIdentity
bcsiCardTypes = _BcsiCardTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOS-PRODUCTS-MIB",
    **{"nosProducts": nosProducts,
       "bcsiRegistration": bcsiRegistration,
       "bcsiChassisTypes": bcsiChassisTypes,
       "vdx6720P24": vdx6720P24,
       "vdx6720P60": vdx6720P60,
       "vdx6730P32": vdx6730P32,
       "vdx6730P76": vdx6730P76,
       "vdx6710P54": vdx6710P54,
       "vdx6746": vdx6746,
       "bcsiCardTypes": bcsiCardTypes}
)
