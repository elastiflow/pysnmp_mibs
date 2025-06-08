# SNMP MIB module (CUMULUS-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cumulus_40310/CUMULUS-COUNTERS-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:08:37 2025
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

(cumulusMib,) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "cumulusMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sysSpecificCounters = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 2)
)
if mibBuilder.loadTexts:
    sysSpecificCounters.setRevisions(
        ("2017-11-08 00:00",
         "2016-10-11 00:00",
         "2016-06-06 00:00",
         "2015-10-31 00:00",
         "2012-07-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiscardCounters_ObjectIdentity = ObjectIdentity
discardCounters = _DiscardCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1)
)
_DiscardCountersTable_Object = MibTable
discardCountersTable = _DiscardCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1)
)
if mibBuilder.loadTexts:
    discardCountersTable.setStatus("deprecated")
_DiscardCountersEntry_Object = MibTableRow
discardCountersEntry = _DiscardCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1)
)
discardCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    discardCountersEntry.setStatus("deprecated")
_DiscardCountersPortName_Type = DisplayString
_DiscardCountersPortName_Object = MibTableColumn
discardCountersPortName = _DiscardCountersPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 1),
    _DiscardCountersPortName_Type()
)
discardCountersPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discardCountersPortName.setStatus("deprecated")


class _L3v4InDiscards_Type(Counter32):
    """Custom type l3v4InDiscards based on Counter32"""
    defaultValue = 0


_L3v4InDiscards_Type.__name__ = "Counter32"
_L3v4InDiscards_Object = MibTableColumn
l3v4InDiscards = _L3v4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 2),
    _L3v4InDiscards_Type()
)
l3v4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3v4InDiscards.setStatus("deprecated")


class _BufferOverflowDiscards_Type(Counter32):
    """Custom type bufferOverflowDiscards based on Counter32"""
    defaultValue = 0


_BufferOverflowDiscards_Type.__name__ = "Counter32"
_BufferOverflowDiscards_Object = MibTableColumn
bufferOverflowDiscards = _BufferOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 3),
    _BufferOverflowDiscards_Type()
)
bufferOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferOverflowDiscards.setStatus("deprecated")


class _L3AclDiscards_Type(Counter32):
    """Custom type l3AclDiscards based on Counter32"""
    defaultValue = 0


_L3AclDiscards_Type.__name__ = "Counter32"
_L3AclDiscards_Object = MibTableColumn
l3AclDiscards = _L3AclDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 4),
    _L3AclDiscards_Type()
)
l3AclDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3AclDiscards.setStatus("deprecated")


class _L3v4BlackholeDiscards_Type(Counter32):
    """Custom type l3v4BlackholeDiscards based on Counter32"""
    defaultValue = 0


_L3v4BlackholeDiscards_Type.__name__ = "Counter32"
_L3v4BlackholeDiscards_Object = MibTableColumn
l3v4BlackholeDiscards = _L3v4BlackholeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 5),
    _L3v4BlackholeDiscards_Type()
)
l3v4BlackholeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3v4BlackholeDiscards.setStatus("deprecated")


class _EgressQOverflowDiscards_Type(Counter32):
    """Custom type egressQOverflowDiscards based on Counter32"""
    defaultValue = 0


_EgressQOverflowDiscards_Type.__name__ = "Counter32"
_EgressQOverflowDiscards_Object = MibTableColumn
egressQOverflowDiscards = _EgressQOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 6),
    _EgressQOverflowDiscards_Type()
)
egressQOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressQOverflowDiscards.setStatus("deprecated")


class _EgressNonQDiscards_Type(Counter32):
    """Custom type egressNonQDiscards based on Counter32"""
    defaultValue = 0


_EgressNonQDiscards_Type.__name__ = "Counter32"
_EgressNonQDiscards_Object = MibTableColumn
egressNonQDiscards = _EgressNonQDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 1, 1, 7),
    _EgressNonQDiscards_Type()
)
egressNonQDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressNonQDiscards.setStatus("deprecated")
_DiscardClCountersTable_Object = MibTable
discardClCountersTable = _DiscardClCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2)
)
if mibBuilder.loadTexts:
    discardClCountersTable.setStatus("current")
_DiscardClCountersEntry_Object = MibTableRow
discardClCountersEntry = _DiscardClCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1)
)
discardClCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    discardClCountersEntry.setStatus("current")
_ClPortName_Type = DisplayString
_ClPortName_Object = MibTableColumn
clPortName = _ClPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 1),
    _ClPortName_Type()
)
clPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortName.setStatus("current")


class _ClL3v4InDiscards_Type(Counter64):
    """Custom type clL3v4InDiscards based on Counter64"""
    defaultValue = 0


_ClL3v4InDiscards_Type.__name__ = "Counter64"
_ClL3v4InDiscards_Object = MibTableColumn
clL3v4InDiscards = _ClL3v4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 2),
    _ClL3v4InDiscards_Type()
)
clL3v4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clL3v4InDiscards.setStatus("current")


class _ClBufferOverflowDiscards_Type(Counter64):
    """Custom type clBufferOverflowDiscards based on Counter64"""
    defaultValue = 0


_ClBufferOverflowDiscards_Type.__name__ = "Counter64"
_ClBufferOverflowDiscards_Object = MibTableColumn
clBufferOverflowDiscards = _ClBufferOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 3),
    _ClBufferOverflowDiscards_Type()
)
clBufferOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clBufferOverflowDiscards.setStatus("current")


class _ClL3AclDiscards_Type(Counter64):
    """Custom type clL3AclDiscards based on Counter64"""
    defaultValue = 0


_ClL3AclDiscards_Type.__name__ = "Counter64"
_ClL3AclDiscards_Object = MibTableColumn
clL3AclDiscards = _ClL3AclDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 4),
    _ClL3AclDiscards_Type()
)
clL3AclDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clL3AclDiscards.setStatus("current")


class _ClL3v4BlackholeDiscards_Type(Counter64):
    """Custom type clL3v4BlackholeDiscards based on Counter64"""
    defaultValue = 0


_ClL3v4BlackholeDiscards_Type.__name__ = "Counter64"
_ClL3v4BlackholeDiscards_Object = MibTableColumn
clL3v4BlackholeDiscards = _ClL3v4BlackholeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 5),
    _ClL3v4BlackholeDiscards_Type()
)
clL3v4BlackholeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clL3v4BlackholeDiscards.setStatus("current")


class _ClEgressQOverflowDiscards_Type(Counter64):
    """Custom type clEgressQOverflowDiscards based on Counter64"""
    defaultValue = 0


_ClEgressQOverflowDiscards_Type.__name__ = "Counter64"
_ClEgressQOverflowDiscards_Object = MibTableColumn
clEgressQOverflowDiscards = _ClEgressQOverflowDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 6),
    _ClEgressQOverflowDiscards_Type()
)
clEgressQOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clEgressQOverflowDiscards.setStatus("current")


class _ClEgressNonQDiscards_Type(Counter64):
    """Custom type clEgressNonQDiscards based on Counter64"""
    defaultValue = 0


_ClEgressNonQDiscards_Type.__name__ = "Counter64"
_ClEgressNonQDiscards_Object = MibTableColumn
clEgressNonQDiscards = _ClEgressNonQDiscards_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 1, 2, 1, 7),
    _ClEgressNonQDiscards_Type()
)
clEgressNonQDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clEgressNonQDiscards.setStatus("current")
_InterfaceCounters_ObjectIdentity = ObjectIdentity
interfaceCounters = _InterfaceCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2)
)
_InterfaceCountersTable_Object = MibTable
interfaceCountersTable = _InterfaceCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceCountersTable.setStatus("deprecated")
_InterfaceCountersEntry_Object = MibTableRow
interfaceCountersEntry = _InterfaceCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1)
)
interfaceCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceCountersEntry.setStatus("deprecated")
_InterfaceCountersPortName_Type = DisplayString
_InterfaceCountersPortName_Object = MibTableColumn
interfaceCountersPortName = _InterfaceCountersPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 1),
    _InterfaceCountersPortName_Type()
)
interfaceCountersPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCountersPortName.setStatus("deprecated")
_IntInOctets_Type = Counter32
_IntInOctets_Object = MibTableColumn
intInOctets = _IntInOctets_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 2),
    _IntInOctets_Type()
)
intInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intInOctets.setStatus("deprecated")
_IntInUcastPkts_Type = Counter32
_IntInUcastPkts_Object = MibTableColumn
intInUcastPkts = _IntInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 3),
    _IntInUcastPkts_Type()
)
intInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intInUcastPkts.setStatus("deprecated")
_IntInBcastPkts_Type = Counter32
_IntInBcastPkts_Object = MibTableColumn
intInBcastPkts = _IntInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 4),
    _IntInBcastPkts_Type()
)
intInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intInBcastPkts.setStatus("deprecated")
_IntInMcastPkts_Type = Counter32
_IntInMcastPkts_Object = MibTableColumn
intInMcastPkts = _IntInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 5),
    _IntInMcastPkts_Type()
)
intInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intInMcastPkts.setStatus("deprecated")
_IntOutOctets_Type = Counter32
_IntOutOctets_Object = MibTableColumn
intOutOctets = _IntOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 6),
    _IntOutOctets_Type()
)
intOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intOutOctets.setStatus("deprecated")
_IntOutUcastPkts_Type = Counter32
_IntOutUcastPkts_Object = MibTableColumn
intOutUcastPkts = _IntOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 7),
    _IntOutUcastPkts_Type()
)
intOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intOutUcastPkts.setStatus("deprecated")
_IntOutBcastPkts_Type = Counter32
_IntOutBcastPkts_Object = MibTableColumn
intOutBcastPkts = _IntOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 8),
    _IntOutBcastPkts_Type()
)
intOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intOutBcastPkts.setStatus("deprecated")
_IntOutMcastPkts_Type = Counter32
_IntOutMcastPkts_Object = MibTableColumn
intOutMcastPkts = _IntOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 1, 1, 9),
    _IntOutMcastPkts_Type()
)
intOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intOutMcastPkts.setStatus("deprecated")
_InterfaceClCountersTable_Object = MibTable
interfaceClCountersTable = _InterfaceClCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2)
)
if mibBuilder.loadTexts:
    interfaceClCountersTable.setStatus("current")
_InterfaceClCountersEntry_Object = MibTableRow
interfaceClCountersEntry = _InterfaceClCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1)
)
interfaceClCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceClCountersEntry.setStatus("current")
_ClIntPortName_Type = DisplayString
_ClIntPortName_Object = MibTableColumn
clIntPortName = _ClIntPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 1),
    _ClIntPortName_Type()
)
clIntPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntPortName.setStatus("current")
_ClIntInOctets_Type = Counter64
_ClIntInOctets_Object = MibTableColumn
clIntInOctets = _ClIntInOctets_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 2),
    _ClIntInOctets_Type()
)
clIntInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInOctets.setStatus("current")
_ClIntInUcastPkts_Type = Counter64
_ClIntInUcastPkts_Object = MibTableColumn
clIntInUcastPkts = _ClIntInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 3),
    _ClIntInUcastPkts_Type()
)
clIntInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInUcastPkts.setStatus("current")
_ClIntInBcastPkts_Type = Counter64
_ClIntInBcastPkts_Object = MibTableColumn
clIntInBcastPkts = _ClIntInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 4),
    _ClIntInBcastPkts_Type()
)
clIntInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInBcastPkts.setStatus("current")
_ClIntInMcastPkts_Type = Counter64
_ClIntInMcastPkts_Object = MibTableColumn
clIntInMcastPkts = _ClIntInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 5),
    _ClIntInMcastPkts_Type()
)
clIntInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInMcastPkts.setStatus("current")
_ClIntOutOctets_Type = Counter64
_ClIntOutOctets_Object = MibTableColumn
clIntOutOctets = _ClIntOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 6),
    _ClIntOutOctets_Type()
)
clIntOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutOctets.setStatus("current")
_ClIntOutUcastPkts_Type = Counter64
_ClIntOutUcastPkts_Object = MibTableColumn
clIntOutUcastPkts = _ClIntOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 7),
    _ClIntOutUcastPkts_Type()
)
clIntOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutUcastPkts.setStatus("current")
_ClIntOutBcastPkts_Type = Counter64
_ClIntOutBcastPkts_Object = MibTableColumn
clIntOutBcastPkts = _ClIntOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 8),
    _ClIntOutBcastPkts_Type()
)
clIntOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutBcastPkts.setStatus("current")
_ClIntOutMcastPkts_Type = Counter64
_ClIntOutMcastPkts_Object = MibTableColumn
clIntOutMcastPkts = _ClIntOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 9),
    _ClIntOutMcastPkts_Type()
)
clIntOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutMcastPkts.setStatus("current")
_ClIntInEtherOctets_Type = Counter64
_ClIntInEtherOctets_Object = MibTableColumn
clIntInEtherOctets = _ClIntInEtherOctets_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 2, 1, 10),
    _ClIntInEtherOctets_Type()
)
clIntInEtherOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInEtherOctets.setStatus("current")
_PfcClCountersTable_Object = MibTable
pfcClCountersTable = _PfcClCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pfcClCountersTable.setStatus("current")
_PfcClCountersEntry_Object = MibTableRow
pfcClCountersEntry = _PfcClCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1)
)
pfcClCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pfcClCountersEntry.setStatus("current")
_ClIntPfcPortName_Type = DisplayString
_ClIntPfcPortName_Object = MibTableColumn
clIntPfcPortName = _ClIntPfcPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 1),
    _ClIntPfcPortName_Type()
)
clIntPfcPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntPfcPortName.setStatus("current")
_ClIntInPausePkt_Type = Counter64
_ClIntInPausePkt_Object = MibTableColumn
clIntInPausePkt = _ClIntInPausePkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 2),
    _ClIntInPausePkt_Type()
)
clIntInPausePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPausePkt.setStatus("current")
_ClIntOutPausePkt_Type = Counter64
_ClIntOutPausePkt_Object = MibTableColumn
clIntOutPausePkt = _ClIntOutPausePkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 3),
    _ClIntOutPausePkt_Type()
)
clIntOutPausePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPausePkt.setStatus("current")
_ClIntInPfc0Pkt_Type = Counter64
_ClIntInPfc0Pkt_Object = MibTableColumn
clIntInPfc0Pkt = _ClIntInPfc0Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 4),
    _ClIntInPfc0Pkt_Type()
)
clIntInPfc0Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc0Pkt.setStatus("current")
_ClIntOutPfc0Pkt_Type = Counter64
_ClIntOutPfc0Pkt_Object = MibTableColumn
clIntOutPfc0Pkt = _ClIntOutPfc0Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 5),
    _ClIntOutPfc0Pkt_Type()
)
clIntOutPfc0Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc0Pkt.setStatus("current")
_ClIntInPfc1Pkt_Type = Counter64
_ClIntInPfc1Pkt_Object = MibTableColumn
clIntInPfc1Pkt = _ClIntInPfc1Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 6),
    _ClIntInPfc1Pkt_Type()
)
clIntInPfc1Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc1Pkt.setStatus("current")
_ClIntOutPfc1Pkt_Type = Counter64
_ClIntOutPfc1Pkt_Object = MibTableColumn
clIntOutPfc1Pkt = _ClIntOutPfc1Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 7),
    _ClIntOutPfc1Pkt_Type()
)
clIntOutPfc1Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc1Pkt.setStatus("current")
_ClIntInPfc2Pkt_Type = Counter64
_ClIntInPfc2Pkt_Object = MibTableColumn
clIntInPfc2Pkt = _ClIntInPfc2Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 8),
    _ClIntInPfc2Pkt_Type()
)
clIntInPfc2Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc2Pkt.setStatus("current")
_ClIntOutPfc2Pkt_Type = Counter64
_ClIntOutPfc2Pkt_Object = MibTableColumn
clIntOutPfc2Pkt = _ClIntOutPfc2Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 9),
    _ClIntOutPfc2Pkt_Type()
)
clIntOutPfc2Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc2Pkt.setStatus("current")
_ClIntInPfc3Pkt_Type = Counter64
_ClIntInPfc3Pkt_Object = MibTableColumn
clIntInPfc3Pkt = _ClIntInPfc3Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 10),
    _ClIntInPfc3Pkt_Type()
)
clIntInPfc3Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc3Pkt.setStatus("current")
_ClIntOutPfc3Pkt_Type = Counter64
_ClIntOutPfc3Pkt_Object = MibTableColumn
clIntOutPfc3Pkt = _ClIntOutPfc3Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 11),
    _ClIntOutPfc3Pkt_Type()
)
clIntOutPfc3Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc3Pkt.setStatus("current")
_ClIntInPfc4Pkt_Type = Counter64
_ClIntInPfc4Pkt_Object = MibTableColumn
clIntInPfc4Pkt = _ClIntInPfc4Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 12),
    _ClIntInPfc4Pkt_Type()
)
clIntInPfc4Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc4Pkt.setStatus("current")
_ClIntOutPfc4Pkt_Type = Counter64
_ClIntOutPfc4Pkt_Object = MibTableColumn
clIntOutPfc4Pkt = _ClIntOutPfc4Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 13),
    _ClIntOutPfc4Pkt_Type()
)
clIntOutPfc4Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc4Pkt.setStatus("current")
_ClIntInPfc5Pkt_Type = Counter64
_ClIntInPfc5Pkt_Object = MibTableColumn
clIntInPfc5Pkt = _ClIntInPfc5Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 14),
    _ClIntInPfc5Pkt_Type()
)
clIntInPfc5Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc5Pkt.setStatus("current")
_ClIntOutPfc5Pkt_Type = Counter64
_ClIntOutPfc5Pkt_Object = MibTableColumn
clIntOutPfc5Pkt = _ClIntOutPfc5Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 15),
    _ClIntOutPfc5Pkt_Type()
)
clIntOutPfc5Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc5Pkt.setStatus("current")
_ClIntInPfc6Pkt_Type = Counter64
_ClIntInPfc6Pkt_Object = MibTableColumn
clIntInPfc6Pkt = _ClIntInPfc6Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 16),
    _ClIntInPfc6Pkt_Type()
)
clIntInPfc6Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc6Pkt.setStatus("current")
_ClIntOutPfc6Pkt_Type = Counter64
_ClIntOutPfc6Pkt_Object = MibTableColumn
clIntOutPfc6Pkt = _ClIntOutPfc6Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 17),
    _ClIntOutPfc6Pkt_Type()
)
clIntOutPfc6Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc6Pkt.setStatus("current")
_ClIntInPfc7Pkt_Type = Counter64
_ClIntInPfc7Pkt_Object = MibTableColumn
clIntInPfc7Pkt = _ClIntInPfc7Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 18),
    _ClIntInPfc7Pkt_Type()
)
clIntInPfc7Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntInPfc7Pkt.setStatus("current")
_ClIntOutPfc7Pkt_Type = Counter64
_ClIntOutPfc7Pkt_Object = MibTableColumn
clIntOutPfc7Pkt = _ClIntOutPfc7Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 3, 1, 19),
    _ClIntOutPfc7Pkt_Type()
)
clIntOutPfc7Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutPfc7Pkt.setStatus("current")
_TcClCountersTable_Object = MibTable
tcClCountersTable = _TcClCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tcClCountersTable.setStatus("current")
_TcClCountersEntry_Object = MibTableRow
tcClCountersEntry = _TcClCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1)
)
tcClCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tcClCountersEntry.setStatus("current")
_ClIntTcPortName_Type = DisplayString
_ClIntTcPortName_Object = MibTableColumn
clIntTcPortName = _ClIntTcPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 1),
    _ClIntTcPortName_Type()
)
clIntTcPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntTcPortName.setStatus("current")
_ClIntOutTc0Pkt_Type = Counter64
_ClIntOutTc0Pkt_Object = MibTableColumn
clIntOutTc0Pkt = _ClIntOutTc0Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 2),
    _ClIntOutTc0Pkt_Type()
)
clIntOutTc0Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc0Pkt.setStatus("current")
_ClIntOutTc0BuffDiscard_Type = Counter64
_ClIntOutTc0BuffDiscard_Object = MibTableColumn
clIntOutTc0BuffDiscard = _ClIntOutTc0BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 3),
    _ClIntOutTc0BuffDiscard_Type()
)
clIntOutTc0BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc0BuffDiscard.setStatus("current")
_ClIntOutTc0WredDiscard_Type = Counter64
_ClIntOutTc0WredDiscard_Object = MibTableColumn
clIntOutTc0WredDiscard = _ClIntOutTc0WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 4),
    _ClIntOutTc0WredDiscard_Type()
)
clIntOutTc0WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc0WredDiscard.setStatus("current")
_ClIntOutTc1Pkt_Type = Counter64
_ClIntOutTc1Pkt_Object = MibTableColumn
clIntOutTc1Pkt = _ClIntOutTc1Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 5),
    _ClIntOutTc1Pkt_Type()
)
clIntOutTc1Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc1Pkt.setStatus("current")
_ClIntOutTc1BuffDiscard_Type = Counter64
_ClIntOutTc1BuffDiscard_Object = MibTableColumn
clIntOutTc1BuffDiscard = _ClIntOutTc1BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 6),
    _ClIntOutTc1BuffDiscard_Type()
)
clIntOutTc1BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc1BuffDiscard.setStatus("current")
_ClIntOutTc1WredDiscard_Type = Counter64
_ClIntOutTc1WredDiscard_Object = MibTableColumn
clIntOutTc1WredDiscard = _ClIntOutTc1WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 7),
    _ClIntOutTc1WredDiscard_Type()
)
clIntOutTc1WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc1WredDiscard.setStatus("current")
_ClIntOutTc2Pkt_Type = Counter64
_ClIntOutTc2Pkt_Object = MibTableColumn
clIntOutTc2Pkt = _ClIntOutTc2Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 8),
    _ClIntOutTc2Pkt_Type()
)
clIntOutTc2Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc2Pkt.setStatus("current")
_ClIntOutTc2BuffDiscard_Type = Counter64
_ClIntOutTc2BuffDiscard_Object = MibTableColumn
clIntOutTc2BuffDiscard = _ClIntOutTc2BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 9),
    _ClIntOutTc2BuffDiscard_Type()
)
clIntOutTc2BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc2BuffDiscard.setStatus("current")
_ClIntOutTc2WredDiscard_Type = Counter64
_ClIntOutTc2WredDiscard_Object = MibTableColumn
clIntOutTc2WredDiscard = _ClIntOutTc2WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 10),
    _ClIntOutTc2WredDiscard_Type()
)
clIntOutTc2WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc2WredDiscard.setStatus("current")
_ClIntOutTc3Pkt_Type = Counter64
_ClIntOutTc3Pkt_Object = MibTableColumn
clIntOutTc3Pkt = _ClIntOutTc3Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 11),
    _ClIntOutTc3Pkt_Type()
)
clIntOutTc3Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc3Pkt.setStatus("current")
_ClIntOutTc3BuffDiscard_Type = Counter64
_ClIntOutTc3BuffDiscard_Object = MibTableColumn
clIntOutTc3BuffDiscard = _ClIntOutTc3BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 12),
    _ClIntOutTc3BuffDiscard_Type()
)
clIntOutTc3BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc3BuffDiscard.setStatus("current")
_ClIntOutTc3WredDiscard_Type = Counter64
_ClIntOutTc3WredDiscard_Object = MibTableColumn
clIntOutTc3WredDiscard = _ClIntOutTc3WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 13),
    _ClIntOutTc3WredDiscard_Type()
)
clIntOutTc3WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc3WredDiscard.setStatus("current")
_ClIntOutTc4Pkt_Type = Counter64
_ClIntOutTc4Pkt_Object = MibTableColumn
clIntOutTc4Pkt = _ClIntOutTc4Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 14),
    _ClIntOutTc4Pkt_Type()
)
clIntOutTc4Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc4Pkt.setStatus("current")
_ClIntOutTc4BuffDiscard_Type = Counter64
_ClIntOutTc4BuffDiscard_Object = MibTableColumn
clIntOutTc4BuffDiscard = _ClIntOutTc4BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 15),
    _ClIntOutTc4BuffDiscard_Type()
)
clIntOutTc4BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc4BuffDiscard.setStatus("current")
_ClIntOutTc4WredDiscard_Type = Counter64
_ClIntOutTc4WredDiscard_Object = MibTableColumn
clIntOutTc4WredDiscard = _ClIntOutTc4WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 16),
    _ClIntOutTc4WredDiscard_Type()
)
clIntOutTc4WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc4WredDiscard.setStatus("current")
_ClIntOutTc5Pkt_Type = Counter64
_ClIntOutTc5Pkt_Object = MibTableColumn
clIntOutTc5Pkt = _ClIntOutTc5Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 17),
    _ClIntOutTc5Pkt_Type()
)
clIntOutTc5Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc5Pkt.setStatus("current")
_ClIntOutTc5BuffDiscard_Type = Counter64
_ClIntOutTc5BuffDiscard_Object = MibTableColumn
clIntOutTc5BuffDiscard = _ClIntOutTc5BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 18),
    _ClIntOutTc5BuffDiscard_Type()
)
clIntOutTc5BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc5BuffDiscard.setStatus("current")
_ClIntOutTc5WredDiscard_Type = Counter64
_ClIntOutTc5WredDiscard_Object = MibTableColumn
clIntOutTc5WredDiscard = _ClIntOutTc5WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 19),
    _ClIntOutTc5WredDiscard_Type()
)
clIntOutTc5WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc5WredDiscard.setStatus("current")
_ClIntOutTc6Pkt_Type = Counter64
_ClIntOutTc6Pkt_Object = MibTableColumn
clIntOutTc6Pkt = _ClIntOutTc6Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 20),
    _ClIntOutTc6Pkt_Type()
)
clIntOutTc6Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc6Pkt.setStatus("current")
_ClIntOutTc6BuffDiscard_Type = Counter64
_ClIntOutTc6BuffDiscard_Object = MibTableColumn
clIntOutTc6BuffDiscard = _ClIntOutTc6BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 21),
    _ClIntOutTc6BuffDiscard_Type()
)
clIntOutTc6BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc6BuffDiscard.setStatus("current")
_ClIntOutTc6WredDiscard_Type = Counter64
_ClIntOutTc6WredDiscard_Object = MibTableColumn
clIntOutTc6WredDiscard = _ClIntOutTc6WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 22),
    _ClIntOutTc6WredDiscard_Type()
)
clIntOutTc6WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc6WredDiscard.setStatus("current")
_ClIntOutTc7Pkt_Type = Counter64
_ClIntOutTc7Pkt_Object = MibTableColumn
clIntOutTc7Pkt = _ClIntOutTc7Pkt_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 23),
    _ClIntOutTc7Pkt_Type()
)
clIntOutTc7Pkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc7Pkt.setStatus("current")
_ClIntOutTc7BuffDiscard_Type = Counter64
_ClIntOutTc7BuffDiscard_Object = MibTableColumn
clIntOutTc7BuffDiscard = _ClIntOutTc7BuffDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 24),
    _ClIntOutTc7BuffDiscard_Type()
)
clIntOutTc7BuffDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc7BuffDiscard.setStatus("current")
_ClIntOutTc7WredDiscard_Type = Counter64
_ClIntOutTc7WredDiscard_Object = MibTableColumn
clIntOutTc7WredDiscard = _ClIntOutTc7WredDiscard_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 4, 1, 25),
    _ClIntOutTc7WredDiscard_Type()
)
clIntOutTc7WredDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntOutTc7WredDiscard.setStatus("current")
_UpDownCountersTable_Object = MibTable
upDownCountersTable = _UpDownCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 5)
)
if mibBuilder.loadTexts:
    upDownCountersTable.setStatus("current")
_UpDownCountersEntry_Object = MibTableRow
upDownCountersEntry = _UpDownCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 5, 1)
)
upDownCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    upDownCountersEntry.setStatus("current")
_ClIntUpDownPortName_Type = DisplayString
_ClIntUpDownPortName_Object = MibTableColumn
clIntUpDownPortName = _ClIntUpDownPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 5, 1, 1),
    _ClIntUpDownPortName_Type()
)
clIntUpDownPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clIntUpDownPortName.setStatus("current")
_ClUpCount_Type = Counter64
_ClUpCount_Object = MibTableColumn
clUpCount = _ClUpCount_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 5, 1, 2),
    _ClUpCount_Type()
)
clUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clUpCount.setStatus("current")
_ClDownCount_Type = Counter64
_ClDownCount_Object = MibTableColumn
clDownCount = _ClDownCount_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 5, 1, 3),
    _ClDownCount_Type()
)
clDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clDownCount.setStatus("current")
_ClCarrierChangesCount_Type = Counter64
_ClCarrierChangesCount_Object = MibTableColumn
clCarrierChangesCount = _ClCarrierChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 40310, 2, 2, 5, 1, 4),
    _ClCarrierChangesCount_Type()
)
clCarrierChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCarrierChangesCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-COUNTERS-MIB",
    **{"sysSpecificCounters": sysSpecificCounters,
       "discardCounters": discardCounters,
       "discardCountersTable": discardCountersTable,
       "discardCountersEntry": discardCountersEntry,
       "discardCountersPortName": discardCountersPortName,
       "l3v4InDiscards": l3v4InDiscards,
       "bufferOverflowDiscards": bufferOverflowDiscards,
       "l3AclDiscards": l3AclDiscards,
       "l3v4BlackholeDiscards": l3v4BlackholeDiscards,
       "egressQOverflowDiscards": egressQOverflowDiscards,
       "egressNonQDiscards": egressNonQDiscards,
       "discardClCountersTable": discardClCountersTable,
       "discardClCountersEntry": discardClCountersEntry,
       "clPortName": clPortName,
       "clL3v4InDiscards": clL3v4InDiscards,
       "clBufferOverflowDiscards": clBufferOverflowDiscards,
       "clL3AclDiscards": clL3AclDiscards,
       "clL3v4BlackholeDiscards": clL3v4BlackholeDiscards,
       "clEgressQOverflowDiscards": clEgressQOverflowDiscards,
       "clEgressNonQDiscards": clEgressNonQDiscards,
       "interfaceCounters": interfaceCounters,
       "interfaceCountersTable": interfaceCountersTable,
       "interfaceCountersEntry": interfaceCountersEntry,
       "interfaceCountersPortName": interfaceCountersPortName,
       "intInOctets": intInOctets,
       "intInUcastPkts": intInUcastPkts,
       "intInBcastPkts": intInBcastPkts,
       "intInMcastPkts": intInMcastPkts,
       "intOutOctets": intOutOctets,
       "intOutUcastPkts": intOutUcastPkts,
       "intOutBcastPkts": intOutBcastPkts,
       "intOutMcastPkts": intOutMcastPkts,
       "interfaceClCountersTable": interfaceClCountersTable,
       "interfaceClCountersEntry": interfaceClCountersEntry,
       "clIntPortName": clIntPortName,
       "clIntInOctets": clIntInOctets,
       "clIntInUcastPkts": clIntInUcastPkts,
       "clIntInBcastPkts": clIntInBcastPkts,
       "clIntInMcastPkts": clIntInMcastPkts,
       "clIntOutOctets": clIntOutOctets,
       "clIntOutUcastPkts": clIntOutUcastPkts,
       "clIntOutBcastPkts": clIntOutBcastPkts,
       "clIntOutMcastPkts": clIntOutMcastPkts,
       "clIntInEtherOctets": clIntInEtherOctets,
       "pfcClCountersTable": pfcClCountersTable,
       "pfcClCountersEntry": pfcClCountersEntry,
       "clIntPfcPortName": clIntPfcPortName,
       "clIntInPausePkt": clIntInPausePkt,
       "clIntOutPausePkt": clIntOutPausePkt,
       "clIntInPfc0Pkt": clIntInPfc0Pkt,
       "clIntOutPfc0Pkt": clIntOutPfc0Pkt,
       "clIntInPfc1Pkt": clIntInPfc1Pkt,
       "clIntOutPfc1Pkt": clIntOutPfc1Pkt,
       "clIntInPfc2Pkt": clIntInPfc2Pkt,
       "clIntOutPfc2Pkt": clIntOutPfc2Pkt,
       "clIntInPfc3Pkt": clIntInPfc3Pkt,
       "clIntOutPfc3Pkt": clIntOutPfc3Pkt,
       "clIntInPfc4Pkt": clIntInPfc4Pkt,
       "clIntOutPfc4Pkt": clIntOutPfc4Pkt,
       "clIntInPfc5Pkt": clIntInPfc5Pkt,
       "clIntOutPfc5Pkt": clIntOutPfc5Pkt,
       "clIntInPfc6Pkt": clIntInPfc6Pkt,
       "clIntOutPfc6Pkt": clIntOutPfc6Pkt,
       "clIntInPfc7Pkt": clIntInPfc7Pkt,
       "clIntOutPfc7Pkt": clIntOutPfc7Pkt,
       "tcClCountersTable": tcClCountersTable,
       "tcClCountersEntry": tcClCountersEntry,
       "clIntTcPortName": clIntTcPortName,
       "clIntOutTc0Pkt": clIntOutTc0Pkt,
       "clIntOutTc0BuffDiscard": clIntOutTc0BuffDiscard,
       "clIntOutTc0WredDiscard": clIntOutTc0WredDiscard,
       "clIntOutTc1Pkt": clIntOutTc1Pkt,
       "clIntOutTc1BuffDiscard": clIntOutTc1BuffDiscard,
       "clIntOutTc1WredDiscard": clIntOutTc1WredDiscard,
       "clIntOutTc2Pkt": clIntOutTc2Pkt,
       "clIntOutTc2BuffDiscard": clIntOutTc2BuffDiscard,
       "clIntOutTc2WredDiscard": clIntOutTc2WredDiscard,
       "clIntOutTc3Pkt": clIntOutTc3Pkt,
       "clIntOutTc3BuffDiscard": clIntOutTc3BuffDiscard,
       "clIntOutTc3WredDiscard": clIntOutTc3WredDiscard,
       "clIntOutTc4Pkt": clIntOutTc4Pkt,
       "clIntOutTc4BuffDiscard": clIntOutTc4BuffDiscard,
       "clIntOutTc4WredDiscard": clIntOutTc4WredDiscard,
       "clIntOutTc5Pkt": clIntOutTc5Pkt,
       "clIntOutTc5BuffDiscard": clIntOutTc5BuffDiscard,
       "clIntOutTc5WredDiscard": clIntOutTc5WredDiscard,
       "clIntOutTc6Pkt": clIntOutTc6Pkt,
       "clIntOutTc6BuffDiscard": clIntOutTc6BuffDiscard,
       "clIntOutTc6WredDiscard": clIntOutTc6WredDiscard,
       "clIntOutTc7Pkt": clIntOutTc7Pkt,
       "clIntOutTc7BuffDiscard": clIntOutTc7BuffDiscard,
       "clIntOutTc7WredDiscard": clIntOutTc7WredDiscard,
       "upDownCountersTable": upDownCountersTable,
       "upDownCountersEntry": upDownCountersEntry,
       "clIntUpDownPortName": clIntUpDownPortName,
       "clUpCount": clUpCount,
       "clDownCount": clDownCount,
       "clCarrierChangesCount": clCarrierChangesCount}
)
