# SNMP MIB module (ZYXEL-LOOPGUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-LOOPGUARD-MIB.mib
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

zyxelLoopGuard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLoopGuardSetup_ObjectIdentity = ObjectIdentity
zyxelLoopGuardSetup = _ZyxelLoopGuardSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1)
)
_ZyLoopGuardState_Type = EnabledStatus
_ZyLoopGuardState_Object = MibScalar
zyLoopGuardState = _ZyLoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 1),
    _ZyLoopGuardState_Type()
)
zyLoopGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoopGuardState.setStatus("current")
_ZyxelLoopGuardPortTable_Object = MibTable
zyxelLoopGuardPortTable = _ZyxelLoopGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelLoopGuardPortTable.setStatus("current")
_ZyxelLoopGuardPortEntry_Object = MibTableRow
zyxelLoopGuardPortEntry = _ZyxelLoopGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 2, 1)
)
zyxelLoopGuardPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelLoopGuardPortEntry.setStatus("current")
_ZyLoopGuardPortState_Type = EnabledStatus
_ZyLoopGuardPortState_Object = MibTableColumn
zyLoopGuardPortState = _ZyLoopGuardPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 1, 2, 1, 1),
    _ZyLoopGuardPortState_Type()
)
zyLoopGuardPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLoopGuardPortState.setStatus("current")
_ZyxelLoopGuardNotifications_ObjectIdentity = ObjectIdentity
zyxelLoopGuardNotifications = _ZyxelLoopGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 2)
)

# Managed Objects groups


# Notification objects

zyLoopGuardLoopDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 45, 2, 1)
)
zyLoopGuardLoopDetect.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyLoopGuardLoopDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LOOPGUARD-MIB",
    **{"zyxelLoopGuard": zyxelLoopGuard,
       "zyxelLoopGuardSetup": zyxelLoopGuardSetup,
       "zyLoopGuardState": zyLoopGuardState,
       "zyxelLoopGuardPortTable": zyxelLoopGuardPortTable,
       "zyxelLoopGuardPortEntry": zyxelLoopGuardPortEntry,
       "zyLoopGuardPortState": zyLoopGuardPortState,
       "zyxelLoopGuardNotifications": zyxelLoopGuardNotifications,
       "zyLoopGuardLoopDetect": zyLoopGuardLoopDetect}
)
