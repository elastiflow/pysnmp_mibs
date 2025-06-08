# SNMP MIB module (ZYXEL-MAC-PINNING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-MAC-PINNING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:16 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMacPinning = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacPinningSetup_ObjectIdentity = ObjectIdentity
zyxelMacPinningSetup = _ZyxelMacPinningSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1)
)
_ZyMacPinningState_Type = EnabledStatus
_ZyMacPinningState_Object = MibScalar
zyMacPinningState = _ZyMacPinningState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 1),
    _ZyMacPinningState_Type()
)
zyMacPinningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacPinningState.setStatus("current")
_ZyxelMacPinningPortTable_Object = MibTable
zyxelMacPinningPortTable = _ZyxelMacPinningPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelMacPinningPortTable.setStatus("current")
_ZyxelMacPinningPortEntry_Object = MibTableRow
zyxelMacPinningPortEntry = _ZyxelMacPinningPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1)
)
zyxelMacPinningPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMacPinningPortEntry.setStatus("current")
_ZyMacPinningPortState_Type = EnabledStatus
_ZyMacPinningPortState_Object = MibTableColumn
zyMacPinningPortState = _ZyMacPinningPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1, 1),
    _ZyMacPinningPortState_Type()
)
zyMacPinningPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacPinningPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MAC-PINNING-MIB",
    **{"zyxelMacPinning": zyxelMacPinning,
       "zyxelMacPinningSetup": zyxelMacPinningSetup,
       "zyMacPinningState": zyMacPinningState,
       "zyxelMacPinningPortTable": zyxelMacPinningPortTable,
       "zyxelMacPinningPortEntry": zyxelMacPinningPortEntry,
       "zyMacPinningPortState": zyMacPinningPortState}
)
