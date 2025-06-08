# SNMP MIB module (RUIJIE-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TUNNEL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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


# MODULE-IDENTITY

ruijieTunnelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 114)
)
if mibBuilder.loadTexts:
    ruijieTunnelMib.setRevisions(
        ("2012-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieTunnelObjects_ObjectIdentity = ObjectIdentity
ruijieTunnelObjects = _RuijieTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 114, 1)
)
_RuijieTunnelTable_Object = MibTable
ruijieTunnelTable = _RuijieTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 114, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieTunnelTable.setStatus("current")
_RuijieTunnelEntry_Object = MibTableRow
ruijieTunnelEntry = _RuijieTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 114, 1, 1, 1)
)
ruijieTunnelEntry.setIndexNames(
    (0, "RUIJIE-TUNNEL-MIB", "ruijieTunnelIp"),
)
if mibBuilder.loadTexts:
    ruijieTunnelEntry.setStatus("current")
_RuijieTunnelIp_Type = IpAddress
_RuijieTunnelIp_Object = MibTableColumn
ruijieTunnelIp = _RuijieTunnelIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 114, 1, 1, 1, 1),
    _RuijieTunnelIp_Type()
)
ruijieTunnelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTunnelIp.setStatus("current")
_RuijieTunnelOutIfindex_Type = Integer32
_RuijieTunnelOutIfindex_Object = MibTableColumn
ruijieTunnelOutIfindex = _RuijieTunnelOutIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 114, 1, 1, 1, 2),
    _RuijieTunnelOutIfindex_Type()
)
ruijieTunnelOutIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTunnelOutIfindex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TUNNEL-MIB",
    **{"ruijieTunnelMib": ruijieTunnelMib,
       "ruijieTunnelObjects": ruijieTunnelObjects,
       "ruijieTunnelTable": ruijieTunnelTable,
       "ruijieTunnelEntry": ruijieTunnelEntry,
       "ruijieTunnelIp": ruijieTunnelIp,
       "ruijieTunnelOutIfindex": ruijieTunnelOutIfindex}
)
