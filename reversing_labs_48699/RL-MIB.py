# SNMP MIB module (RL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/reversing_labs_48699/RL-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:55:46 2025
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

rlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48699)
)
if mibBuilder.loadTexts:
    rlMIB.setRevisions(
        ("2016-10-25 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1)
)
_T1000_ObjectIdentity = ObjectIdentity
t1000 = _T1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1, 1)
)
_A1000_ObjectIdentity = ObjectIdentity
a1000 = _A1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1, 2)
)
_C1000_ObjectIdentity = ObjectIdentity
c1000 = _C1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1, 3)
)
_N1000_ObjectIdentity = ObjectIdentity
n1000 = _N1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1, 4)
)
_Tiscaleworker_ObjectIdentity = ObjectIdentity
tiscaleworker = _Tiscaleworker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1, 5)
)
_Tiscalehub_ObjectIdentity = ObjectIdentity
tiscalehub = _Tiscalehub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 1, 6)
)
_Director_ObjectIdentity = ObjectIdentity
director = _Director_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 2)
)
_Av_ObjectIdentity = ObjectIdentity
av = _Av_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 1, 3)
)
_RlMgmt_ObjectIdentity = ObjectIdentity
rlMgmt = _RlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48699, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RL-MIB",
    **{"rlMIB": rlMIB,
       "products": products,
       "device": device,
       "t1000": t1000,
       "a1000": a1000,
       "c1000": c1000,
       "n1000": n1000,
       "tiscaleworker": tiscaleworker,
       "tiscalehub": tiscalehub,
       "director": director,
       "av": av,
       "rlMgmt": rlMgmt}
)
