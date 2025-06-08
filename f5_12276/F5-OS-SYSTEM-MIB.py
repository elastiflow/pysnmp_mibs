# SNMP MIB module (F5-OS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/f5_12276/F5-OS-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:59:23 2025
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

(platform,) = mibBuilder.importSymbols(
    "F5-COMMON-SMI-MIB",
    "platform")

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

f5OsSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3)
)
if mibBuilder.loadTexts:
    f5OsSystem.setRevisions(
        ("2022-04-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F5OsSystemModelOIDs_ObjectIdentity = ObjectIdentity
f5OsSystemModelOIDs = _F5OsSystemModelOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1)
)
_F5OsAppR5x00_ObjectIdentity = ObjectIdentity
f5OsAppR5x00 = _F5OsAppR5x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 1)
)
_F5OsAppR10x00_ObjectIdentity = ObjectIdentity
f5OsAppR10x00 = _F5OsAppR10x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 2)
)
_F5OsAppR2x00_ObjectIdentity = ObjectIdentity
f5OsAppR2x00 = _F5OsAppR2x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 3)
)
_F5OsAppR4x00_ObjectIdentity = ObjectIdentity
f5OsAppR4x00 = _F5OsAppR4x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 4)
)
_F5OsVelosCx410_ObjectIdentity = ObjectIdentity
f5OsVelosCx410 = _F5OsVelosCx410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 5)
)
_F5OsVelosCx410Partition_ObjectIdentity = ObjectIdentity
f5OsVelosCx410Partition = _F5OsVelosCx410Partition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-OS-SYSTEM-MIB",
    **{"f5OsSystem": f5OsSystem,
       "f5OsSystemModelOIDs": f5OsSystemModelOIDs,
       "f5OsAppR5x00": f5OsAppR5x00,
       "f5OsAppR10x00": f5OsAppR10x00,
       "f5OsAppR2x00": f5OsAppR2x00,
       "f5OsAppR4x00": f5OsAppR4x00,
       "f5OsVelosCx410": f5OsVelosCx410,
       "f5OsVelosCx410Partition": f5OsVelosCx410Partition}
)
