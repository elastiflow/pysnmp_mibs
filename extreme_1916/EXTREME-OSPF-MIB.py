# SNMP MIB module (EXTREME-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-OSPF-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(extremeVlanIfIndex,) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfIndex")

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

extremeOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeOspfInterfaceTable_Object = MibTable
extremeOspfInterfaceTable = _ExtremeOspfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15, 1)
)
if mibBuilder.loadTexts:
    extremeOspfInterfaceTable.setStatus("current")
_ExtremeOspfInterfaceEntry_Object = MibTableRow
extremeOspfInterfaceEntry = _ExtremeOspfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1)
)
extremeOspfInterfaceEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeOspfInterfaceEntry.setStatus("current")
_ExtremeOspfAreaId_Type = IpAddress
_ExtremeOspfAreaId_Object = MibTableColumn
extremeOspfAreaId = _ExtremeOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 1),
    _ExtremeOspfAreaId_Type()
)
extremeOspfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfAreaId.setStatus("current")
_ExtremeOspfInterfacePassive_Type = TruthValue
_ExtremeOspfInterfacePassive_Object = MibTableColumn
extremeOspfInterfacePassive = _ExtremeOspfInterfacePassive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 2),
    _ExtremeOspfInterfacePassive_Type()
)
extremeOspfInterfacePassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfInterfacePassive.setStatus("current")
_ExtremeOspfInterfaceStatus_Type = RowStatus
_ExtremeOspfInterfaceStatus_Object = MibTableColumn
extremeOspfInterfaceStatus = _ExtremeOspfInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 3),
    _ExtremeOspfInterfaceStatus_Type()
)
extremeOspfInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfInterfaceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-OSPF-MIB",
    **{"extremeOspf": extremeOspf,
       "extremeOspfInterfaceTable": extremeOspfInterfaceTable,
       "extremeOspfInterfaceEntry": extremeOspfInterfaceEntry,
       "extremeOspfAreaId": extremeOspfAreaId,
       "extremeOspfInterfacePassive": extremeOspfInterfacePassive,
       "extremeOspfInterfaceStatus": extremeOspfInterfaceStatus}
)
