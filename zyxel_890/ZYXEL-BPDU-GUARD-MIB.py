# SNMP MIB module (ZYXEL-BPDU-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-BPDU-GUARD-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:30:52 2025
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

zyxelBpduGuard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelBpduGuardSetup_ObjectIdentity = ObjectIdentity
zyxelBpduGuardSetup = _ZyxelBpduGuardSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 1)
)
_ZyBpduGuardState_Type = EnabledStatus
_ZyBpduGuardState_Object = MibScalar
zyBpduGuardState = _ZyBpduGuardState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 1, 1),
    _ZyBpduGuardState_Type()
)
zyBpduGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyBpduGuardState.setStatus("current")
_ZyxelBpduGuardPortTable_Object = MibTable
zyxelBpduGuardPortTable = _ZyxelBpduGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelBpduGuardPortTable.setStatus("current")
_ZyxelBpduGuardPortEntry_Object = MibTableRow
zyxelBpduGuardPortEntry = _ZyxelBpduGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 1, 2, 1)
)
zyxelBpduGuardPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelBpduGuardPortEntry.setStatus("current")
_ZyBpduGuardPortState_Type = EnabledStatus
_ZyBpduGuardPortState_Object = MibTableColumn
zyBpduGuardPortState = _ZyBpduGuardPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 1, 2, 1, 1),
    _ZyBpduGuardPortState_Type()
)
zyBpduGuardPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyBpduGuardPortState.setStatus("current")
_ZyxelBpduGuardStatus_ObjectIdentity = ObjectIdentity
zyxelBpduGuardStatus = _ZyxelBpduGuardStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 2)
)
_ZyxelBpduGuardPortInfoTable_Object = MibTable
zyxelBpduGuardPortInfoTable = _ZyxelBpduGuardPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelBpduGuardPortInfoTable.setStatus("current")
_ZyxelBpduGuardPortInfoEntry_Object = MibTableRow
zyxelBpduGuardPortInfoEntry = _ZyxelBpduGuardPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 2, 1, 1)
)
zyxelBpduGuardPortInfoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelBpduGuardPortInfoEntry.setStatus("current")


class _ZyBpduGuardPortInfoStatus_Type(Integer32):
    """Custom type zyBpduGuardPortInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("err-disable", 2))
    )


_ZyBpduGuardPortInfoStatus_Type.__name__ = "Integer32"
_ZyBpduGuardPortInfoStatus_Object = MibTableColumn
zyBpduGuardPortInfoStatus = _ZyBpduGuardPortInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 104, 2, 1, 1, 1),
    _ZyBpduGuardPortInfoStatus_Type()
)
zyBpduGuardPortInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyBpduGuardPortInfoStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-BPDU-GUARD-MIB",
    **{"zyxelBpduGuard": zyxelBpduGuard,
       "zyxelBpduGuardSetup": zyxelBpduGuardSetup,
       "zyBpduGuardState": zyBpduGuardState,
       "zyxelBpduGuardPortTable": zyxelBpduGuardPortTable,
       "zyxelBpduGuardPortEntry": zyxelBpduGuardPortEntry,
       "zyBpduGuardPortState": zyBpduGuardPortState,
       "zyxelBpduGuardStatus": zyxelBpduGuardStatus,
       "zyxelBpduGuardPortInfoTable": zyxelBpduGuardPortInfoTable,
       "zyxelBpduGuardPortInfoEntry": zyxelBpduGuardPortInfoEntry,
       "zyBpduGuardPortInfoStatus": zyBpduGuardPortInfoStatus}
)
