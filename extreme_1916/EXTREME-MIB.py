# SNMP MIB module (EXTREME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Extreme_ObjectIdentity = ObjectIdentity
extreme = _Extreme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916)
)
_ExtremeProduct_ObjectIdentity = ObjectIdentity
extremeProduct = _ExtremeProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2)
)
_Summit1_ObjectIdentity = ObjectIdentity
summit1 = _Summit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 1)
)
_Summit2_ObjectIdentity = ObjectIdentity
summit2 = _Summit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 2)
)

# Managed Objects groups


# Notification objects

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 6)
)
overheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

fanfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 7)
)
fanfailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanfailed.setStatus(
        ""
    )

fanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 8)
)
fanOK.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanOK.setStatus(
        ""
    )

invalidLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 9)
)
invalidLoginAttempt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    invalidLoginAttempt.setStatus(
        ""
    )

powerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 10)
)
powerSupplyFail.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    powerSupplyFail.setStatus(
        ""
    )

powerSupplyGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 11)
)
powerSupplyGood.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    powerSupplyGood.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MIB",
    **{"extreme": extreme,
       "overheat": overheat,
       "fanfailed": fanfailed,
       "fanOK": fanOK,
       "invalidLoginAttempt": invalidLoginAttempt,
       "powerSupplyFail": powerSupplyFail,
       "powerSupplyGood": powerSupplyGood,
       "extremeProduct": extremeProduct,
       "summit1": summit1,
       "summit2": summit2}
)
