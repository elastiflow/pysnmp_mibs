# SNMP MIB module (CISCOSB-ProtectedPorts-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-ProtectedPorts-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:46 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlProtectedPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132)
)
if mibBuilder.loadTexts:
    rlProtectedPorts.setRevisions(
        ("2008-05-03 12:34",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlProtectedPortsTable_Object = MibTable
rlProtectedPortsTable = _RlProtectedPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1)
)
if mibBuilder.loadTexts:
    rlProtectedPortsTable.setStatus("current")
_RlProtectedPortsEntry_Object = MibTableRow
rlProtectedPortsEntry = _RlProtectedPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1)
)
rlProtectedPortsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtectedPortsEntry.setStatus("current")


class _RlProtectedPortType_Type(Integer32):
    """Custom type rlProtectedPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-protected", 1),
          ("protected", 2))
    )


_RlProtectedPortType_Type.__name__ = "Integer32"
_RlProtectedPortType_Object = MibTableColumn
rlProtectedPortType = _RlProtectedPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1, 1),
    _RlProtectedPortType_Type()
)
rlProtectedPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortType.setStatus("current")


class _RlProtectedPortCommunity_Type(Integer32):
    """Custom type rlProtectedPortCommunity based on Integer32"""
    defaultValue = 0


_RlProtectedPortCommunity_Type.__name__ = "Integer32"
_RlProtectedPortCommunity_Object = MibTableColumn
rlProtectedPortCommunity = _RlProtectedPortCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1, 2),
    _RlProtectedPortCommunity_Type()
)
rlProtectedPortCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortCommunity.setStatus("current")
_RlProtectedPortsStatusTable_Object = MibTable
rlProtectedPortsStatusTable = _RlProtectedPortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2)
)
if mibBuilder.loadTexts:
    rlProtectedPortsStatusTable.setStatus("current")
_RlProtectedPortsStatusEntry_Object = MibTableRow
rlProtectedPortsStatusEntry = _RlProtectedPortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2, 1)
)
rlProtectedPortsStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtectedPortsStatusEntry.setStatus("current")
_RlProtectedPortEgressPorts_Type = PortList
_RlProtectedPortEgressPorts_Object = MibTableColumn
rlProtectedPortEgressPorts = _RlProtectedPortEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2, 1, 1),
    _RlProtectedPortEgressPorts_Type()
)
rlProtectedPortEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlProtectedPortEgressPorts.setStatus("current")


class _RlProtectedPortsGlobalEnable_Type(TruthValue):
    """Custom type rlProtectedPortsGlobalEnable based on TruthValue"""
    defaultValue = 2


_RlProtectedPortsGlobalEnable_Type.__name__ = "TruthValue"
_RlProtectedPortsGlobalEnable_Object = MibScalar
rlProtectedPortsGlobalEnable = _RlProtectedPortsGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 3),
    _RlProtectedPortsGlobalEnable_Type()
)
rlProtectedPortsGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortsGlobalEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-ProtectedPorts-MIB",
    **{"rlProtectedPorts": rlProtectedPorts,
       "rlProtectedPortsTable": rlProtectedPortsTable,
       "rlProtectedPortsEntry": rlProtectedPortsEntry,
       "rlProtectedPortType": rlProtectedPortType,
       "rlProtectedPortCommunity": rlProtectedPortCommunity,
       "rlProtectedPortsStatusTable": rlProtectedPortsStatusTable,
       "rlProtectedPortsStatusEntry": rlProtectedPortsStatusEntry,
       "rlProtectedPortEgressPorts": rlProtectedPortEgressPorts,
       "rlProtectedPortsGlobalEnable": rlProtectedPortsGlobalEnable}
)
