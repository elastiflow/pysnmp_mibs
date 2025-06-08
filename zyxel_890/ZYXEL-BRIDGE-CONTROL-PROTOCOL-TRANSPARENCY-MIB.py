# SNMP MIB module (ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB.mib
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

zyxelBridgeControlProtocolTransparency = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelBridgeControlProtocolTransparencySetup_ObjectIdentity = ObjectIdentity
zyxelBridgeControlProtocolTransparencySetup = _ZyxelBridgeControlProtocolTransparencySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1)
)
_ZyBridgeControlProtocolTransparencyState_Type = EnabledStatus
_ZyBridgeControlProtocolTransparencyState_Object = MibScalar
zyBridgeControlProtocolTransparencyState = _ZyBridgeControlProtocolTransparencyState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 1),
    _ZyBridgeControlProtocolTransparencyState_Type()
)
zyBridgeControlProtocolTransparencyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyBridgeControlProtocolTransparencyState.setStatus("current")
_ZyxelBridgeControlProtocolTransparencyPortTable_Object = MibTable
zyxelBridgeControlProtocolTransparencyPortTable = _ZyxelBridgeControlProtocolTransparencyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelBridgeControlProtocolTransparencyPortTable.setStatus("current")
_ZyxelBridgeControlProtocolTransparencyPortEntry_Object = MibTableRow
zyxelBridgeControlProtocolTransparencyPortEntry = _ZyxelBridgeControlProtocolTransparencyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1)
)
zyxelBridgeControlProtocolTransparencyPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelBridgeControlProtocolTransparencyPortEntry.setStatus("current")


class _ZyBridgeControlProtocolTransparencyPortMode_Type(Integer32):
    """Custom type zyBridgeControlProtocolTransparencyPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("peer", 0),
          ("tunnel", 1),
          ("discard", 2),
          ("network", 3))
    )


_ZyBridgeControlProtocolTransparencyPortMode_Type.__name__ = "Integer32"
_ZyBridgeControlProtocolTransparencyPortMode_Object = MibTableColumn
zyBridgeControlProtocolTransparencyPortMode = _ZyBridgeControlProtocolTransparencyPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1, 1),
    _ZyBridgeControlProtocolTransparencyPortMode_Type()
)
zyBridgeControlProtocolTransparencyPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyBridgeControlProtocolTransparencyPortMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB",
    **{"zyxelBridgeControlProtocolTransparency": zyxelBridgeControlProtocolTransparency,
       "zyxelBridgeControlProtocolTransparencySetup": zyxelBridgeControlProtocolTransparencySetup,
       "zyBridgeControlProtocolTransparencyState": zyBridgeControlProtocolTransparencyState,
       "zyxelBridgeControlProtocolTransparencyPortTable": zyxelBridgeControlProtocolTransparencyPortTable,
       "zyxelBridgeControlProtocolTransparencyPortEntry": zyxelBridgeControlProtocolTransparencyPortEntry,
       "zyBridgeControlProtocolTransparencyPortMode": zyBridgeControlProtocolTransparencyPortMode}
)
