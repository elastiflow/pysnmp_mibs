# SNMP MIB module (ZYXEL-GREEN-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-GREEN-ETHERNET-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:07:44 2025
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

zyxelGreenEthernet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelGreenEthernetSetup_ObjectIdentity = ObjectIdentity
zyxelGreenEthernetSetup = _ZyxelGreenEthernetSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1)
)
_ZyGreenEthernetEeeState_Type = EnabledStatus
_ZyGreenEthernetEeeState_Object = MibScalar
zyGreenEthernetEeeState = _ZyGreenEthernetEeeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 1),
    _ZyGreenEthernetEeeState_Type()
)
zyGreenEthernetEeeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyGreenEthernetEeeState.setStatus("current")
_ZyGreenEthernetAutoPowerDownState_Type = EnabledStatus
_ZyGreenEthernetAutoPowerDownState_Object = MibScalar
zyGreenEthernetAutoPowerDownState = _ZyGreenEthernetAutoPowerDownState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 2),
    _ZyGreenEthernetAutoPowerDownState_Type()
)
zyGreenEthernetAutoPowerDownState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyGreenEthernetAutoPowerDownState.setStatus("current")
_ZyGreenEthernetShortReachState_Type = EnabledStatus
_ZyGreenEthernetShortReachState_Object = MibScalar
zyGreenEthernetShortReachState = _ZyGreenEthernetShortReachState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 3),
    _ZyGreenEthernetShortReachState_Type()
)
zyGreenEthernetShortReachState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyGreenEthernetShortReachState.setStatus("current")
_ZyxelGreenEthernetPortTable_Object = MibTable
zyxelGreenEthernetPortTable = _ZyxelGreenEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelGreenEthernetPortTable.setStatus("current")
_ZyxelGreenEthernetPortEntry_Object = MibTableRow
zyxelGreenEthernetPortEntry = _ZyxelGreenEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 4, 1)
)
zyxelGreenEthernetPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelGreenEthernetPortEntry.setStatus("current")
_ZyGreenEthernetEeePortState_Type = EnabledStatus
_ZyGreenEthernetEeePortState_Object = MibTableColumn
zyGreenEthernetEeePortState = _ZyGreenEthernetEeePortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 4, 1, 1),
    _ZyGreenEthernetEeePortState_Type()
)
zyGreenEthernetEeePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyGreenEthernetEeePortState.setStatus("current")
_ZyGreenEthernetAutoPowerDownPortState_Type = EnabledStatus
_ZyGreenEthernetAutoPowerDownPortState_Object = MibTableColumn
zyGreenEthernetAutoPowerDownPortState = _ZyGreenEthernetAutoPowerDownPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 4, 1, 2),
    _ZyGreenEthernetAutoPowerDownPortState_Type()
)
zyGreenEthernetAutoPowerDownPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyGreenEthernetAutoPowerDownPortState.setStatus("current")
_ZyGreenEthernetShortReachPortState_Type = EnabledStatus
_ZyGreenEthernetShortReachPortState_Object = MibTableColumn
zyGreenEthernetShortReachPortState = _ZyGreenEthernetShortReachPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 93, 1, 4, 1, 3),
    _ZyGreenEthernetShortReachPortState_Type()
)
zyGreenEthernetShortReachPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyGreenEthernetShortReachPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-GREEN-ETHERNET-MIB",
    **{"zyxelGreenEthernet": zyxelGreenEthernet,
       "zyxelGreenEthernetSetup": zyxelGreenEthernetSetup,
       "zyGreenEthernetEeeState": zyGreenEthernetEeeState,
       "zyGreenEthernetAutoPowerDownState": zyGreenEthernetAutoPowerDownState,
       "zyGreenEthernetShortReachState": zyGreenEthernetShortReachState,
       "zyxelGreenEthernetPortTable": zyxelGreenEthernetPortTable,
       "zyxelGreenEthernetPortEntry": zyxelGreenEthernetPortEntry,
       "zyGreenEthernetEeePortState": zyGreenEthernetEeePortState,
       "zyGreenEthernetAutoPowerDownPortState": zyGreenEthernetAutoPowerDownPortState,
       "zyGreenEthernetShortReachPortState": zyGreenEthernetShortReachPortState}
)
