# SNMP MIB module (JUNIPER-RPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-RPF-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:30:07 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxRpf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17)
)
if mibBuilder.loadTexts:
    jnxRpf.setRevisions(
        ("2002-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxRpfStats_ObjectIdentity = ObjectIdentity
jnxRpfStats = _JnxRpfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1)
)
_JnxRpfStatsTable_Object = MibTable
jnxRpfStatsTable = _JnxRpfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    jnxRpfStatsTable.setStatus("current")
_JnxRpfStatsEntry_Object = MibTableRow
jnxRpfStatsEntry = _JnxRpfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1)
)
jnxRpfStatsEntry.setIndexNames(
    (0, "JUNIPER-RPF-MIB", "jnxRpfStatsIfIndex"),
    (0, "JUNIPER-RPF-MIB", "jnxRpfStatsAddrFamily"),
)
if mibBuilder.loadTexts:
    jnxRpfStatsEntry.setStatus("current")
_JnxRpfStatsIfIndex_Type = InterfaceIndex
_JnxRpfStatsIfIndex_Object = MibTableColumn
jnxRpfStatsIfIndex = _JnxRpfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 1),
    _JnxRpfStatsIfIndex_Type()
)
jnxRpfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpfStatsIfIndex.setStatus("current")


class _JnxRpfStatsAddrFamily_Type(Integer32):
    """Custom type jnxRpfStatsAddrFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxRpfStatsAddrFamily_Type.__name__ = "Integer32"
_JnxRpfStatsAddrFamily_Object = MibTableColumn
jnxRpfStatsAddrFamily = _JnxRpfStatsAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 2),
    _JnxRpfStatsAddrFamily_Type()
)
jnxRpfStatsAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRpfStatsAddrFamily.setStatus("current")
_JnxRpfStatsPackets_Type = Counter64
_JnxRpfStatsPackets_Object = MibTableColumn
jnxRpfStatsPackets = _JnxRpfStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 3),
    _JnxRpfStatsPackets_Type()
)
jnxRpfStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpfStatsPackets.setStatus("current")
_JnxRpfStatsBytes_Type = Counter64
_JnxRpfStatsBytes_Object = MibTableColumn
jnxRpfStatsBytes = _JnxRpfStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 4),
    _JnxRpfStatsBytes_Type()
)
jnxRpfStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRpfStatsBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RPF-MIB",
    **{"jnxRpf": jnxRpf,
       "jnxRpfStats": jnxRpfStats,
       "jnxRpfStatsTable": jnxRpfStatsTable,
       "jnxRpfStatsEntry": jnxRpfStatsEntry,
       "jnxRpfStatsIfIndex": jnxRpfStatsIfIndex,
       "jnxRpfStatsAddrFamily": jnxRpfStatsAddrFamily,
       "jnxRpfStatsPackets": jnxRpfStatsPackets,
       "jnxRpfStatsBytes": jnxRpfStatsBytes}
)
