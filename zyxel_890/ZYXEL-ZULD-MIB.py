# SNMP MIB module (ZYXEL-ZULD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ZULD-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:33:26 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelZuld = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelZuldSetup_ObjectIdentity = ObjectIdentity
zyxelZuldSetup = _ZyxelZuldSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1)
)
_ZyZuldState_Type = EnabledStatus
_ZyZuldState_Object = MibScalar
zyZuldState = _ZyZuldState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1, 1),
    _ZyZuldState_Type()
)
zyZuldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyZuldState.setStatus("current")
_ZyxelZuldPortTable_Object = MibTable
zyxelZuldPortTable = _ZyxelZuldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelZuldPortTable.setStatus("current")
_ZyxelZuldPortEntry_Object = MibTableRow
zyxelZuldPortEntry = _ZyxelZuldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1, 2, 1)
)
zyxelZuldPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelZuldPortEntry.setStatus("current")
_ZyZuldPortState_Type = EnabledStatus
_ZyZuldPortState_Object = MibTableColumn
zyZuldPortState = _ZyZuldPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1, 2, 1, 1),
    _ZyZuldPortState_Type()
)
zyZuldPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyZuldPortState.setStatus("current")


class _ZyZuldPortMode_Type(Integer32):
    """Custom type zyZuldPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("aggressive", 2))
    )


_ZyZuldPortMode_Type.__name__ = "Integer32"
_ZyZuldPortMode_Object = MibTableColumn
zyZuldPortMode = _ZyZuldPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1, 2, 1, 2),
    _ZyZuldPortMode_Type()
)
zyZuldPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyZuldPortMode.setStatus("current")


class _ZyZuldPortProbeTime_Type(Integer32):
    """Custom type zyZuldPortProbeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65534),
    )


_ZyZuldPortProbeTime_Type.__name__ = "Integer32"
_ZyZuldPortProbeTime_Object = MibTableColumn
zyZuldPortProbeTime = _ZyZuldPortProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 1, 2, 1, 3),
    _ZyZuldPortProbeTime_Type()
)
zyZuldPortProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyZuldPortProbeTime.setStatus("current")
_ZyxelZuldStatus_ObjectIdentity = ObjectIdentity
zyxelZuldStatus = _ZyxelZuldStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2)
)
_ZyxelZuldPortStatusTable_Object = MibTable
zyxelZuldPortStatusTable = _ZyxelZuldPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelZuldPortStatusTable.setStatus("current")
_ZyxelZuldPortStatusEntry_Object = MibTableRow
zyxelZuldPortStatusEntry = _ZyxelZuldPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2, 1, 1)
)
zyxelZuldPortStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelZuldPortStatusEntry.setStatus("current")


class _ZyZuldPortLinkState_Type(Integer32):
    """Custom type zyZuldPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("linkdwon", 1),
          ("probe", 2),
          ("unidirectional", 3),
          ("bidirectional", 4),
          ("shutdown", 5))
    )


_ZyZuldPortLinkState_Type.__name__ = "Integer32"
_ZyZuldPortLinkState_Object = MibTableColumn
zyZuldPortLinkState = _ZyZuldPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2, 1, 1, 1),
    _ZyZuldPortLinkState_Type()
)
zyZuldPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyZuldPortLinkState.setStatus("current")
_ZyZuldPortRemoteMACAddress_Type = MacAddress
_ZyZuldPortRemoteMACAddress_Object = MibTableColumn
zyZuldPortRemoteMACAddress = _ZyZuldPortRemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2, 1, 1, 2),
    _ZyZuldPortRemoteMACAddress_Type()
)
zyZuldPortRemoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyZuldPortRemoteMACAddress.setStatus("current")
_ZyZuldPortRemotePort_Type = Integer32
_ZyZuldPortRemotePort_Object = MibTableColumn
zyZuldPortRemotePort = _ZyZuldPortRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2, 1, 1, 3),
    _ZyZuldPortRemotePort_Type()
)
zyZuldPortRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyZuldPortRemotePort.setStatus("current")
_ZyZuldPortRemoteOperation_Type = EnabledStatus
_ZyZuldPortRemoteOperation_Object = MibTableColumn
zyZuldPortRemoteOperation = _ZyZuldPortRemoteOperation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 2, 1, 1, 4),
    _ZyZuldPortRemoteOperation_Type()
)
zyZuldPortRemoteOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyZuldPortRemoteOperation.setStatus("current")
_ZyxelZuldTrapNotifications_ObjectIdentity = ObjectIdentity
zyxelZuldTrapNotifications = _ZyxelZuldTrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 3)
)

# Managed Objects groups


# Notification objects

zyZuldUnidirectionalDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 3, 1)
)
zyZuldUnidirectionalDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyZuldUnidirectionalDetected.setStatus(
        "current"
    )

zyZuldBidirectionalRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 110, 3, 2)
)
zyZuldBidirectionalRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyZuldBidirectionalRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ZULD-MIB",
    **{"zyxelZuld": zyxelZuld,
       "zyxelZuldSetup": zyxelZuldSetup,
       "zyZuldState": zyZuldState,
       "zyxelZuldPortTable": zyxelZuldPortTable,
       "zyxelZuldPortEntry": zyxelZuldPortEntry,
       "zyZuldPortState": zyZuldPortState,
       "zyZuldPortMode": zyZuldPortMode,
       "zyZuldPortProbeTime": zyZuldPortProbeTime,
       "zyxelZuldStatus": zyxelZuldStatus,
       "zyxelZuldPortStatusTable": zyxelZuldPortStatusTable,
       "zyxelZuldPortStatusEntry": zyxelZuldPortStatusEntry,
       "zyZuldPortLinkState": zyZuldPortLinkState,
       "zyZuldPortRemoteMACAddress": zyZuldPortRemoteMACAddress,
       "zyZuldPortRemotePort": zyZuldPortRemotePort,
       "zyZuldPortRemoteOperation": zyZuldPortRemoteOperation,
       "zyxelZuldTrapNotifications": zyxelZuldTrapNotifications,
       "zyZuldUnidirectionalDetected": zyZuldUnidirectionalDetected,
       "zyZuldBidirectionalRecovered": zyZuldBidirectionalRecovered}
)
