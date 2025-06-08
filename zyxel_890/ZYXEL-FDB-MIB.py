# SNMP MIB module (ZYXEL-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-FDB-MIB.mib
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

zyxelFdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacStatus_ObjectIdentity = ObjectIdentity
zyxelMacStatus = _ZyxelMacStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1)
)
_ZyMacFlush_Type = EnabledStatus
_ZyMacFlush_Object = MibScalar
zyMacFlush = _ZyMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 1),
    _ZyMacFlush_Type()
)
zyMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFlush.setStatus("current")
_ZyMacFlushPort_Type = Integer32
_ZyMacFlushPort_Object = MibScalar
zyMacFlushPort = _ZyMacFlushPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 2),
    _ZyMacFlushPort_Type()
)
zyMacFlushPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFlushPort.setStatus("current")
_ZyMacFlushVlan_Type = Integer32
_ZyMacFlushVlan_Object = MibScalar
zyMacFlushVlan = _ZyMacFlushVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 3),
    _ZyMacFlushVlan_Type()
)
zyMacFlushVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFlushVlan.setStatus("current")
_ZyxelMacStatusNotifications_ObjectIdentity = ObjectIdentity
zyxelMacStatusNotifications = _ZyxelMacStatusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2)
)

# Managed Objects groups


# Notification objects

zyMacForwardingTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 1)
)
if mibBuilder.loadTexts:
    zyMacForwardingTableFull.setStatus(
        "current"
    )

zyMacForwardingTableFullRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 2)
)
if mibBuilder.loadTexts:
    zyMacForwardingTableFullRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-FDB-MIB",
    **{"zyxelFdb": zyxelFdb,
       "zyxelMacStatus": zyxelMacStatus,
       "zyMacFlush": zyMacFlush,
       "zyMacFlushPort": zyMacFlushPort,
       "zyMacFlushVlan": zyMacFlushVlan,
       "zyxelMacStatusNotifications": zyxelMacStatusNotifications,
       "zyMacForwardingTableFull": zyMacForwardingTableFull,
       "zyMacForwardingTableFullRecovered": zyMacForwardingTableFullRecovered}
)
