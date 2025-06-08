# SNMP MIB module (ZYXEL-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-OAM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:36:29 2025
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

zyxelOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelOamSetup_ObjectIdentity = ObjectIdentity
zyxelOamSetup = _ZyxelOamSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1)
)
_ZyOamState_Type = EnabledStatus
_ZyOamState_Object = MibScalar
zyOamState = _ZyOamState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 1),
    _ZyOamState_Type()
)
zyOamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamState.setStatus("current")
_ZyxelOamPortTable_Object = MibTable
zyxelOamPortTable = _ZyxelOamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelOamPortTable.setStatus("current")
_ZyxelOamPortEntry_Object = MibTableRow
zyxelOamPortEntry = _ZyxelOamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1)
)
zyxelOamPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelOamPortEntry.setStatus("current")
_ZyOamPortState_Type = EnabledStatus
_ZyOamPortState_Object = MibTableColumn
zyOamPortState = _ZyOamPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1, 1),
    _ZyOamPortState_Type()
)
zyOamPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamPortState.setStatus("current")


class _ZyOamPortFunctionsSupported_Type(Bits):
    """Custom type zyOamPortFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_ZyOamPortFunctionsSupported_Type.__name__ = "Bits"
_ZyOamPortFunctionsSupported_Object = MibTableColumn
zyOamPortFunctionsSupported = _ZyOamPortFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1, 2),
    _ZyOamPortFunctionsSupported_Type()
)
zyOamPortFunctionsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamPortFunctionsSupported.setStatus("current")
_ZyxelOamOuldSetup_ObjectIdentity = ObjectIdentity
zyxelOamOuldSetup = _ZyxelOamOuldSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2)
)


class _ZyOamOuldDiscoveryTimer_Type(Integer32):
    """Custom type zyOamOuldDiscoveryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ZyOamOuldDiscoveryTimer_Type.__name__ = "Integer32"
_ZyOamOuldDiscoveryTimer_Object = MibScalar
zyOamOuldDiscoveryTimer = _ZyOamOuldDiscoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2, 1),
    _ZyOamOuldDiscoveryTimer_Type()
)
zyOamOuldDiscoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamOuldDiscoveryTimer.setStatus("current")


class _ZyOamOuldRecoveryTimer_Type(Integer32):
    """Custom type zyOamOuldRecoveryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ZyOamOuldRecoveryTimer_Type.__name__ = "Integer32"
_ZyOamOuldRecoveryTimer_Object = MibScalar
zyOamOuldRecoveryTimer = _ZyOamOuldRecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2, 2),
    _ZyOamOuldRecoveryTimer_Type()
)
zyOamOuldRecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamOuldRecoveryTimer.setStatus("current")
_ZyxelOamOuldSetupPortTable_Object = MibTable
zyxelOamOuldSetupPortTable = _ZyxelOamOuldSetupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelOamOuldSetupPortTable.setStatus("current")
_ZyxelOamOuldSetupPortEntry_Object = MibTableRow
zyxelOamOuldSetupPortEntry = _ZyxelOamOuldSetupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2, 3, 1)
)
zyxelOamOuldSetupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelOamOuldSetupPortEntry.setStatus("current")
_ZyOamOuldState_Type = EnabledStatus
_ZyOamOuldState_Object = MibTableColumn
zyOamOuldState = _ZyOamOuldState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2, 3, 1, 1),
    _ZyOamOuldState_Type()
)
zyOamOuldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamOuldState.setStatus("current")
_ZyOamOuldAggressiveMode_Type = EnabledStatus
_ZyOamOuldAggressiveMode_Object = MibTableColumn
zyOamOuldAggressiveMode = _ZyOamOuldAggressiveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 2, 3, 1, 2),
    _ZyOamOuldAggressiveMode_Type()
)
zyOamOuldAggressiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamOuldAggressiveMode.setStatus("current")
_ZyxelOamOuldStatus_ObjectIdentity = ObjectIdentity
zyxelOamOuldStatus = _ZyxelOamOuldStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 3)
)
_ZyxelOamOuldStatusPortTable_Object = MibTable
zyxelOamOuldStatusPortTable = _ZyxelOamOuldStatusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 3, 1)
)
if mibBuilder.loadTexts:
    zyxelOamOuldStatusPortTable.setStatus("current")
_ZyxelOamOuldStatusPortEntry_Object = MibTableRow
zyxelOamOuldStatusPortEntry = _ZyxelOamOuldStatusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 3, 1, 1)
)
zyxelOamOuldStatusPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelOamOuldStatusPortEntry.setStatus("current")
_ZyOamOuldResult_Type = DisplayString
_ZyOamOuldResult_Object = MibTableColumn
zyOamOuldResult = _ZyOamOuldResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 3, 1, 1, 1),
    _ZyOamOuldResult_Type()
)
zyOamOuldResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOamOuldResult.setStatus("current")
_ZyOamOuldLinkStatus_Type = DisplayString
_ZyOamOuldLinkStatus_Object = MibTableColumn
zyOamOuldLinkStatus = _ZyOamOuldLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 3, 1, 1, 2),
    _ZyOamOuldLinkStatus_Type()
)
zyOamOuldLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOamOuldLinkStatus.setStatus("current")
_ZyOamOuldCountdown_Type = DisplayString
_ZyOamOuldCountdown_Object = MibTableColumn
zyOamOuldCountdown = _ZyOamOuldCountdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 3, 1, 1, 3),
    _ZyOamOuldCountdown_Type()
)
zyOamOuldCountdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOamOuldCountdown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-OAM-MIB",
    **{"zyxelOam": zyxelOam,
       "zyxelOamSetup": zyxelOamSetup,
       "zyOamState": zyOamState,
       "zyxelOamPortTable": zyxelOamPortTable,
       "zyxelOamPortEntry": zyxelOamPortEntry,
       "zyOamPortState": zyOamPortState,
       "zyOamPortFunctionsSupported": zyOamPortFunctionsSupported,
       "zyxelOamOuldSetup": zyxelOamOuldSetup,
       "zyOamOuldDiscoveryTimer": zyOamOuldDiscoveryTimer,
       "zyOamOuldRecoveryTimer": zyOamOuldRecoveryTimer,
       "zyxelOamOuldSetupPortTable": zyxelOamOuldSetupPortTable,
       "zyxelOamOuldSetupPortEntry": zyxelOamOuldSetupPortEntry,
       "zyOamOuldState": zyOamOuldState,
       "zyOamOuldAggressiveMode": zyOamOuldAggressiveMode,
       "zyxelOamOuldStatus": zyxelOamOuldStatus,
       "zyxelOamOuldStatusPortTable": zyxelOamOuldStatusPortTable,
       "zyxelOamOuldStatusPortEntry": zyxelOamOuldStatusPortEntry,
       "zyOamOuldResult": zyOamOuldResult,
       "zyOamOuldLinkStatus": zyOamOuldLinkStatus,
       "zyOamOuldCountdown": zyOamOuldCountdown}
)
