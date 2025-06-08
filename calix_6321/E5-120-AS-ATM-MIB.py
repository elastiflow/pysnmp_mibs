# SNMP MIB module (E5-120-AS-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/E5-120-AS-ATM-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:40:54 2025
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

(accessSwitchCommonATM,
 pvcVci,
 pvcVpi) = mibBuilder.importSymbols(
    "E5-120-MIB",
    "accessSwitchCommonATM",
    "pvcVci",
    "pvcVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsChannelStatusTable_Object = MibTable
asChannelStatusTable = _AsChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 99, 7)
)
if mibBuilder.loadTexts:
    asChannelStatusTable.setStatus("mandatory")
_AsChannelStatusEntry_Object = MibTableRow
asChannelStatusEntry = _AsChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 99, 7, 1)
)
asChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-120-MIB", "pvcVpi"),
    (0, "E5-120-MIB", "pvcVci"),
)
if mibBuilder.loadTexts:
    asChannelStatusEntry.setStatus("mandatory")
_AsChannelTxPackets_Type = Counter32
_AsChannelTxPackets_Object = MibTableColumn
asChannelTxPackets = _AsChannelTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 99, 7, 1, 1),
    _AsChannelTxPackets_Type()
)
asChannelTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelTxPackets.setStatus("mandatory")
_AsChannelRxPackets_Type = Counter32
_AsChannelRxPackets_Object = MibTableColumn
asChannelRxPackets = _AsChannelRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 99, 7, 1, 2),
    _AsChannelRxPackets_Type()
)
asChannelRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelRxPackets.setStatus("mandatory")
_AsChannelTxCells_Type = Counter32
_AsChannelTxCells_Object = MibTableColumn
asChannelTxCells = _AsChannelTxCells_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 99, 7, 1, 3),
    _AsChannelTxCells_Type()
)
asChannelTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelTxCells.setStatus("mandatory")
_AsChannelRxCells_Type = Counter32
_AsChannelRxCells_Object = MibTableColumn
asChannelRxCells = _AsChannelRxCells_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 99, 7, 1, 4),
    _AsChannelRxCells_Type()
)
asChannelRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelRxCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E5-120-AS-ATM-MIB",
    **{"asChannelStatusTable": asChannelStatusTable,
       "asChannelStatusEntry": asChannelStatusEntry,
       "asChannelTxPackets": asChannelTxPackets,
       "asChannelRxPackets": asChannelRxPackets,
       "asChannelTxCells": asChannelTxCells,
       "asChannelRxCells": asChannelRxCells}
)
