# SNMP MIB module (TR-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/TR-RMON-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:24:23 2025
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_Rmon_ObjectIdentity = ObjectIdentity
rmon = _Rmon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 1)
)
_TokenRingStatsTable_Object = MibTable
tokenRingStatsTable = _TokenRingStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    tokenRingStatsTable.setStatus("mandatory")
_TokenRingStatsEntry_Object = MibTableRow
tokenRingStatsEntry = _TokenRingStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1)
)
tokenRingStatsEntry.setIndexNames(
    (0, "TR-RMON-MIB", "tokenRingStatsIndex"),
)
if mibBuilder.loadTexts:
    tokenRingStatsEntry.setStatus("mandatory")


class _TokenRingStatsIndex_Type(Integer32):
    """Custom type tokenRingStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingStatsIndex_Type.__name__ = "Integer32"
_TokenRingStatsIndex_Object = MibTableColumn
tokenRingStatsIndex = _TokenRingStatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 1),
    _TokenRingStatsIndex_Type()
)
tokenRingStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsIndex.setStatus("mandatory")
_TokenRingStatsDataSource_Type = ObjectIdentifier
_TokenRingStatsDataSource_Object = MibScalar
tokenRingStatsDataSource = _TokenRingStatsDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 2),
    _TokenRingStatsDataSource_Type()
)
tokenRingStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingStatsDataSource.setStatus("mandatory")
_TokenRingStatsDropEvents_Type = Counter32
_TokenRingStatsDropEvents_Object = MibTableColumn
tokenRingStatsDropEvents = _TokenRingStatsDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 3),
    _TokenRingStatsDropEvents_Type()
)
tokenRingStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDropEvents.setStatus("mandatory")
_TokenRingStatsOctets_Type = Counter32
_TokenRingStatsOctets_Object = MibTableColumn
tokenRingStatsOctets = _TokenRingStatsOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 4),
    _TokenRingStatsOctets_Type()
)
tokenRingStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsOctets.setStatus("mandatory")
_TokenRingStatsPkts_Type = Counter32
_TokenRingStatsPkts_Object = MibScalar
tokenRingStatsPkts = _TokenRingStatsPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 5),
    _TokenRingStatsPkts_Type()
)
tokenRingStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsPkts.setStatus("mandatory")
_TokenRingStatsDataBroadcastPkts_Type = Counter32
_TokenRingStatsDataBroadcastPkts_Object = MibScalar
tokenRingStatsDataBroadcastPkts = _TokenRingStatsDataBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 6),
    _TokenRingStatsDataBroadcastPkts_Type()
)
tokenRingStatsDataBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataBroadcastPkts.setStatus("mandatory")
_TokenRingStatsDataAllRoutesBroadcastPkts_Type = Counter32
_TokenRingStatsDataAllRoutesBroadcastPkts_Object = MibScalar
tokenRingStatsDataAllRoutesBroadcastPkts = _TokenRingStatsDataAllRoutesBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 7),
    _TokenRingStatsDataAllRoutesBroadcastPkts_Type()
)
tokenRingStatsDataAllRoutesBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataAllRoutesBroadcastPkts.setStatus("mandatory")
_TokenRingStatsDataMulticastPkts_Type = Counter32
_TokenRingStatsDataMulticastPkts_Object = MibScalar
tokenRingStatsDataMulticastPkts = _TokenRingStatsDataMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 8),
    _TokenRingStatsDataMulticastPkts_Type()
)
tokenRingStatsDataMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataMulticastPkts.setStatus("mandatory")
_TokenRingStatsMACOctets_Type = Counter32
_TokenRingStatsMACOctets_Object = MibScalar
tokenRingStatsMACOctets = _TokenRingStatsMACOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 9),
    _TokenRingStatsMACOctets_Type()
)
tokenRingStatsMACOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMACOctets.setStatus("mandatory")
_TokenRingStatsMACPkts_Type = Counter32
_TokenRingStatsMACPkts_Object = MibScalar
tokenRingStatsMACPkts = _TokenRingStatsMACPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 10),
    _TokenRingStatsMACPkts_Type()
)
tokenRingStatsMACPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMACPkts.setStatus("mandatory")
_TokenRingStatsRingPurgeEvents_Type = Counter32
_TokenRingStatsRingPurgeEvents_Object = MibTableColumn
tokenRingStatsRingPurgeEvents = _TokenRingStatsRingPurgeEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 11),
    _TokenRingStatsRingPurgeEvents_Type()
)
tokenRingStatsRingPurgeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsRingPurgeEvents.setStatus("mandatory")
_TokenRingStatsRingPurgePackets_Type = Counter32
_TokenRingStatsRingPurgePackets_Object = MibTableColumn
tokenRingStatsRingPurgePackets = _TokenRingStatsRingPurgePackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 12),
    _TokenRingStatsRingPurgePackets_Type()
)
tokenRingStatsRingPurgePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsRingPurgePackets.setStatus("mandatory")
_TokenRingStatsBeaconEvents_Type = Counter32
_TokenRingStatsBeaconEvents_Object = MibTableColumn
tokenRingStatsBeaconEvents = _TokenRingStatsBeaconEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 13),
    _TokenRingStatsBeaconEvents_Type()
)
tokenRingStatsBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsBeaconEvents.setStatus("mandatory")
_TokenRingStatsBeaconPackets_Type = Counter32
_TokenRingStatsBeaconPackets_Object = MibTableColumn
tokenRingStatsBeaconPackets = _TokenRingStatsBeaconPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 14),
    _TokenRingStatsBeaconPackets_Type()
)
tokenRingStatsBeaconPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsBeaconPackets.setStatus("mandatory")
_TokenRingStatsMonitorContentionEvents_Type = Counter32
_TokenRingStatsMonitorContentionEvents_Object = MibTableColumn
tokenRingStatsMonitorContentionEvents = _TokenRingStatsMonitorContentionEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 15),
    _TokenRingStatsMonitorContentionEvents_Type()
)
tokenRingStatsMonitorContentionEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMonitorContentionEvents.setStatus("mandatory")
_TokenRingStatsMonitorContentionPackets_Type = Counter32
_TokenRingStatsMonitorContentionPackets_Object = MibTableColumn
tokenRingStatsMonitorContentionPackets = _TokenRingStatsMonitorContentionPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 16),
    _TokenRingStatsMonitorContentionPackets_Type()
)
tokenRingStatsMonitorContentionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMonitorContentionPackets.setStatus("mandatory")
_TokenRingStatsNAUNChanges_Type = Counter32
_TokenRingStatsNAUNChanges_Object = MibTableColumn
tokenRingStatsNAUNChanges = _TokenRingStatsNAUNChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 17),
    _TokenRingStatsNAUNChanges_Type()
)
tokenRingStatsNAUNChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsNAUNChanges.setStatus("mandatory")
_TokenRingStatsLineErrors_Type = Counter32
_TokenRingStatsLineErrors_Object = MibTableColumn
tokenRingStatsLineErrors = _TokenRingStatsLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 18),
    _TokenRingStatsLineErrors_Type()
)
tokenRingStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsLineErrors.setStatus("mandatory")
_TokenRingStatsInternalErrors_Type = Counter32
_TokenRingStatsInternalErrors_Object = MibTableColumn
tokenRingStatsInternalErrors = _TokenRingStatsInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 19),
    _TokenRingStatsInternalErrors_Type()
)
tokenRingStatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsInternalErrors.setStatus("mandatory")
_TokenRingStatsBurstErrors_Type = Counter32
_TokenRingStatsBurstErrors_Object = MibTableColumn
tokenRingStatsBurstErrors = _TokenRingStatsBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 20),
    _TokenRingStatsBurstErrors_Type()
)
tokenRingStatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsBurstErrors.setStatus("mandatory")
_TokenRingStatsACErrors_Type = Counter32
_TokenRingStatsACErrors_Object = MibTableColumn
tokenRingStatsACErrors = _TokenRingStatsACErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 21),
    _TokenRingStatsACErrors_Type()
)
tokenRingStatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsACErrors.setStatus("mandatory")
_TokenRingStatsAbortErrors_Type = Counter32
_TokenRingStatsAbortErrors_Object = MibTableColumn
tokenRingStatsAbortErrors = _TokenRingStatsAbortErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 22),
    _TokenRingStatsAbortErrors_Type()
)
tokenRingStatsAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsAbortErrors.setStatus("mandatory")
_TokenRingStatsLostFramesErrors_Type = Counter32
_TokenRingStatsLostFramesErrors_Object = MibTableColumn
tokenRingStatsLostFramesErrors = _TokenRingStatsLostFramesErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 23),
    _TokenRingStatsLostFramesErrors_Type()
)
tokenRingStatsLostFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsLostFramesErrors.setStatus("mandatory")
_TokenRingStatsCongestionErrors_Type = Counter32
_TokenRingStatsCongestionErrors_Object = MibTableColumn
tokenRingStatsCongestionErrors = _TokenRingStatsCongestionErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 24),
    _TokenRingStatsCongestionErrors_Type()
)
tokenRingStatsCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsCongestionErrors.setStatus("mandatory")
_TokenRingStatsFrameCopiedErrors_Type = Counter32
_TokenRingStatsFrameCopiedErrors_Object = MibTableColumn
tokenRingStatsFrameCopiedErrors = _TokenRingStatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 25),
    _TokenRingStatsFrameCopiedErrors_Type()
)
tokenRingStatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsFrameCopiedErrors.setStatus("mandatory")
_TokenRingStatsFrequencyErrors_Type = Counter32
_TokenRingStatsFrequencyErrors_Object = MibTableColumn
tokenRingStatsFrequencyErrors = _TokenRingStatsFrequencyErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 26),
    _TokenRingStatsFrequencyErrors_Type()
)
tokenRingStatsFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsFrequencyErrors.setStatus("mandatory")
_TokenRingStatsTokenErrors_Type = Counter32
_TokenRingStatsTokenErrors_Object = MibTableColumn
tokenRingStatsTokenErrors = _TokenRingStatsTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 27),
    _TokenRingStatsTokenErrors_Type()
)
tokenRingStatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsTokenErrors.setStatus("mandatory")
_TokenRingStatsSoftErrorReports_Type = Counter32
_TokenRingStatsSoftErrorReports_Object = MibTableColumn
tokenRingStatsSoftErrorReports = _TokenRingStatsSoftErrorReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 28),
    _TokenRingStatsSoftErrorReports_Type()
)
tokenRingStatsSoftErrorReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsSoftErrorReports.setStatus("mandatory")
_TokenRingStatsDataPkts18to63Octets_Type = Counter32
_TokenRingStatsDataPkts18to63Octets_Object = MibTableColumn
tokenRingStatsDataPkts18to63Octets = _TokenRingStatsDataPkts18to63Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 29),
    _TokenRingStatsDataPkts18to63Octets_Type()
)
tokenRingStatsDataPkts18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts18to63Octets.setStatus("mandatory")
_TokenRingStatsDataPkts64to127Octets_Type = Counter32
_TokenRingStatsDataPkts64to127Octets_Object = MibTableColumn
tokenRingStatsDataPkts64to127Octets = _TokenRingStatsDataPkts64to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 30),
    _TokenRingStatsDataPkts64to127Octets_Type()
)
tokenRingStatsDataPkts64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts64to127Octets.setStatus("mandatory")
_TokenRingStatsDataPkts128to255Octets_Type = Counter32
_TokenRingStatsDataPkts128to255Octets_Object = MibTableColumn
tokenRingStatsDataPkts128to255Octets = _TokenRingStatsDataPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 31),
    _TokenRingStatsDataPkts128to255Octets_Type()
)
tokenRingStatsDataPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts128to255Octets.setStatus("mandatory")
_TokenRingStatsDataPkts256to511Octets_Type = Counter32
_TokenRingStatsDataPkts256to511Octets_Object = MibTableColumn
tokenRingStatsDataPkts256to511Octets = _TokenRingStatsDataPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 32),
    _TokenRingStatsDataPkts256to511Octets_Type()
)
tokenRingStatsDataPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts256to511Octets.setStatus("mandatory")
_TokenRingStatsDataPkts512to1023Octets_Type = Counter32
_TokenRingStatsDataPkts512to1023Octets_Object = MibTableColumn
tokenRingStatsDataPkts512to1023Octets = _TokenRingStatsDataPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 33),
    _TokenRingStatsDataPkts512to1023Octets_Type()
)
tokenRingStatsDataPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts512to1023Octets.setStatus("mandatory")
_TokenRingStatsDataPkts1024to2047Octets_Type = Counter32
_TokenRingStatsDataPkts1024to2047Octets_Object = MibTableColumn
tokenRingStatsDataPkts1024to2047Octets = _TokenRingStatsDataPkts1024to2047Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 34),
    _TokenRingStatsDataPkts1024to2047Octets_Type()
)
tokenRingStatsDataPkts1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts1024to2047Octets.setStatus("mandatory")
_TokenRingStatsDataPkts2048to4095Octets_Type = Counter32
_TokenRingStatsDataPkts2048to4095Octets_Object = MibTableColumn
tokenRingStatsDataPkts2048to4095Octets = _TokenRingStatsDataPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 35),
    _TokenRingStatsDataPkts2048to4095Octets_Type()
)
tokenRingStatsDataPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts2048to4095Octets.setStatus("mandatory")
_TokenRingStatsDataPkts4096to8191Octets_Type = Counter32
_TokenRingStatsDataPkts4096to8191Octets_Object = MibTableColumn
tokenRingStatsDataPkts4096to8191Octets = _TokenRingStatsDataPkts4096to8191Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 36),
    _TokenRingStatsDataPkts4096to8191Octets_Type()
)
tokenRingStatsDataPkts4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts4096to8191Octets.setStatus("mandatory")
_TokenRingStatsDataPkts8192to18000Octets_Type = Counter32
_TokenRingStatsDataPkts8192to18000Octets_Object = MibTableColumn
tokenRingStatsDataPkts8192to18000Octets = _TokenRingStatsDataPkts8192to18000Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 37),
    _TokenRingStatsDataPkts8192to18000Octets_Type()
)
tokenRingStatsDataPkts8192to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts8192to18000Octets.setStatus("mandatory")
_TokenRingStatsDataPkts18000orGreaterOctets_Type = Counter32
_TokenRingStatsDataPkts18000orGreaterOctets_Object = MibTableColumn
tokenRingStatsDataPkts18000orGreaterOctets = _TokenRingStatsDataPkts18000orGreaterOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 38),
    _TokenRingStatsDataPkts18000orGreaterOctets_Type()
)
tokenRingStatsDataPkts18000orGreaterOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts18000orGreaterOctets.setStatus("mandatory")
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 2)
)
_TokenRingHistoryTable_Object = MibTable
tokenRingHistoryTable = _TokenRingHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    tokenRingHistoryTable.setStatus("mandatory")
_TokenRingHistoryEntry_Object = MibTableRow
tokenRingHistoryEntry = _TokenRingHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1)
)
tokenRingHistoryEntry.setIndexNames(
    (0, "TR-RMON-MIB", "tokenRingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tokenRingHistoryEntry.setStatus("mandatory")


class _TokenRingHistoryIndex_Type(Integer32):
    """Custom type tokenRingHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingHistoryIndex_Type.__name__ = "Integer32"
_TokenRingHistoryIndex_Object = MibTableColumn
tokenRingHistoryIndex = _TokenRingHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 1),
    _TokenRingHistoryIndex_Type()
)
tokenRingHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryIndex.setStatus("mandatory")
_TokenRingHistorySampleIndex_Type = ObjectIdentifier
_TokenRingHistorySampleIndex_Object = MibTableColumn
tokenRingHistorySampleIndex = _TokenRingHistorySampleIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 2),
    _TokenRingHistorySampleIndex_Type()
)
tokenRingHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistorySampleIndex.setStatus("mandatory")
_TokenRingHistoryIntervalStart_Type = TimeTicks
_TokenRingHistoryIntervalStart_Object = MibTableColumn
tokenRingHistoryIntervalStart = _TokenRingHistoryIntervalStart_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 3),
    _TokenRingHistoryIntervalStart_Type()
)
tokenRingHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryIntervalStart.setStatus("mandatory")
_TokenRingHistoryDropEvents_Type = Counter32
_TokenRingHistoryDropEvents_Object = MibTableColumn
tokenRingHistoryDropEvents = _TokenRingHistoryDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 4),
    _TokenRingHistoryDropEvents_Type()
)
tokenRingHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDropEvents.setStatus("mandatory")
_TokenRingHistoryOctets_Type = Counter32
_TokenRingHistoryOctets_Object = MibTableColumn
tokenRingHistoryOctets = _TokenRingHistoryOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 5),
    _TokenRingHistoryOctets_Type()
)
tokenRingHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryOctets.setStatus("mandatory")
_TokenRingHistoryPkts_Type = Counter32
_TokenRingHistoryPkts_Object = MibScalar
tokenRingHistoryPkts = _TokenRingHistoryPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 6),
    _TokenRingHistoryPkts_Type()
)
tokenRingHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryPkts.setStatus("mandatory")
_TokenRingHistoryDataBroadcastPkts_Type = Counter32
_TokenRingHistoryDataBroadcastPkts_Object = MibScalar
tokenRingHistoryDataBroadcastPkts = _TokenRingHistoryDataBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 7),
    _TokenRingHistoryDataBroadcastPkts_Type()
)
tokenRingHistoryDataBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDataBroadcastPkts.setStatus("mandatory")
_TokenRingHistoryDataAllRoutesBroadcastPkts_Type = Counter32
_TokenRingHistoryDataAllRoutesBroadcastPkts_Object = MibScalar
tokenRingHistoryDataAllRoutesBroadcastPkts = _TokenRingHistoryDataAllRoutesBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 8),
    _TokenRingHistoryDataAllRoutesBroadcastPkts_Type()
)
tokenRingHistoryDataAllRoutesBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDataAllRoutesBroadcastPkts.setStatus("mandatory")
_TokenRingHistoryDataMulticastPkts_Type = Counter32
_TokenRingHistoryDataMulticastPkts_Object = MibScalar
tokenRingHistoryDataMulticastPkts = _TokenRingHistoryDataMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 9),
    _TokenRingHistoryDataMulticastPkts_Type()
)
tokenRingHistoryDataMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDataMulticastPkts.setStatus("mandatory")
_TokenRingHistoryMACOctets_Type = Counter32
_TokenRingHistoryMACOctets_Object = MibScalar
tokenRingHistoryMACOctets = _TokenRingHistoryMACOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 10),
    _TokenRingHistoryMACOctets_Type()
)
tokenRingHistoryMACOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMACOctets.setStatus("mandatory")
_TokenRingHistoryMACPkts_Type = Counter32
_TokenRingHistoryMACPkts_Object = MibScalar
tokenRingHistoryMACPkts = _TokenRingHistoryMACPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 11),
    _TokenRingHistoryMACPkts_Type()
)
tokenRingHistoryMACPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMACPkts.setStatus("mandatory")
_TokenRingHistoryRingPurgeEvents_Type = Counter32
_TokenRingHistoryRingPurgeEvents_Object = MibTableColumn
tokenRingHistoryRingPurgeEvents = _TokenRingHistoryRingPurgeEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 12),
    _TokenRingHistoryRingPurgeEvents_Type()
)
tokenRingHistoryRingPurgeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryRingPurgeEvents.setStatus("mandatory")
_TokenRingHistoryRingPurgePackets_Type = Counter32
_TokenRingHistoryRingPurgePackets_Object = MibTableColumn
tokenRingHistoryRingPurgePackets = _TokenRingHistoryRingPurgePackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 13),
    _TokenRingHistoryRingPurgePackets_Type()
)
tokenRingHistoryRingPurgePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryRingPurgePackets.setStatus("mandatory")
_TokenRingHistoryBeaconEvents_Type = Counter32
_TokenRingHistoryBeaconEvents_Object = MibTableColumn
tokenRingHistoryBeaconEvents = _TokenRingHistoryBeaconEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 14),
    _TokenRingHistoryBeaconEvents_Type()
)
tokenRingHistoryBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryBeaconEvents.setStatus("mandatory")
_TokenRingHistoryBeaconPackets_Type = Counter32
_TokenRingHistoryBeaconPackets_Object = MibTableColumn
tokenRingHistoryBeaconPackets = _TokenRingHistoryBeaconPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 15),
    _TokenRingHistoryBeaconPackets_Type()
)
tokenRingHistoryBeaconPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryBeaconPackets.setStatus("mandatory")
_TokenRingHistoryMonitorContentionEvents_Type = Counter32
_TokenRingHistoryMonitorContentionEvents_Object = MibTableColumn
tokenRingHistoryMonitorContentionEvents = _TokenRingHistoryMonitorContentionEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 16),
    _TokenRingHistoryMonitorContentionEvents_Type()
)
tokenRingHistoryMonitorContentionEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMonitorContentionEvents.setStatus("mandatory")
_TokenRingHistoryMonitorContentionPackets_Type = Counter32
_TokenRingHistoryMonitorContentionPackets_Object = MibTableColumn
tokenRingHistoryMonitorContentionPackets = _TokenRingHistoryMonitorContentionPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 17),
    _TokenRingHistoryMonitorContentionPackets_Type()
)
tokenRingHistoryMonitorContentionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMonitorContentionPackets.setStatus("mandatory")
_TokenRingHistoryNAUNChanges_Type = Counter32
_TokenRingHistoryNAUNChanges_Object = MibTableColumn
tokenRingHistoryNAUNChanges = _TokenRingHistoryNAUNChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 18),
    _TokenRingHistoryNAUNChanges_Type()
)
tokenRingHistoryNAUNChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryNAUNChanges.setStatus("mandatory")
_TokenRingHistoryLineErrors_Type = Counter32
_TokenRingHistoryLineErrors_Object = MibTableColumn
tokenRingHistoryLineErrors = _TokenRingHistoryLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 19),
    _TokenRingHistoryLineErrors_Type()
)
tokenRingHistoryLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryLineErrors.setStatus("mandatory")
_TokenRingHistoryInternalErrors_Type = Counter32
_TokenRingHistoryInternalErrors_Object = MibTableColumn
tokenRingHistoryInternalErrors = _TokenRingHistoryInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 20),
    _TokenRingHistoryInternalErrors_Type()
)
tokenRingHistoryInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryInternalErrors.setStatus("mandatory")
_TokenRingHistoryBurstErrors_Type = Counter32
_TokenRingHistoryBurstErrors_Object = MibTableColumn
tokenRingHistoryBurstErrors = _TokenRingHistoryBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 21),
    _TokenRingHistoryBurstErrors_Type()
)
tokenRingHistoryBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryBurstErrors.setStatus("mandatory")
_TokenRingHistoryACErrors_Type = Counter32
_TokenRingHistoryACErrors_Object = MibTableColumn
tokenRingHistoryACErrors = _TokenRingHistoryACErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 22),
    _TokenRingHistoryACErrors_Type()
)
tokenRingHistoryACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryACErrors.setStatus("mandatory")
_TokenRingHistoryAbortErrors_Type = Counter32
_TokenRingHistoryAbortErrors_Object = MibTableColumn
tokenRingHistoryAbortErrors = _TokenRingHistoryAbortErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 23),
    _TokenRingHistoryAbortErrors_Type()
)
tokenRingHistoryAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryAbortErrors.setStatus("mandatory")
_TokenRingHistoryLostFramesErrors_Type = Counter32
_TokenRingHistoryLostFramesErrors_Object = MibTableColumn
tokenRingHistoryLostFramesErrors = _TokenRingHistoryLostFramesErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 24),
    _TokenRingHistoryLostFramesErrors_Type()
)
tokenRingHistoryLostFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryLostFramesErrors.setStatus("mandatory")
_TokenRingHistoryCongestionErrors_Type = Counter32
_TokenRingHistoryCongestionErrors_Object = MibTableColumn
tokenRingHistoryCongestionErrors = _TokenRingHistoryCongestionErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 25),
    _TokenRingHistoryCongestionErrors_Type()
)
tokenRingHistoryCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryCongestionErrors.setStatus("mandatory")
_TokenRingHistoryFrameCopiedErrors_Type = Counter32
_TokenRingHistoryFrameCopiedErrors_Object = MibTableColumn
tokenRingHistoryFrameCopiedErrors = _TokenRingHistoryFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 26),
    _TokenRingHistoryFrameCopiedErrors_Type()
)
tokenRingHistoryFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryFrameCopiedErrors.setStatus("mandatory")
_TokenRingHistoryFrequencyErrors_Type = Counter32
_TokenRingHistoryFrequencyErrors_Object = MibTableColumn
tokenRingHistoryFrequencyErrors = _TokenRingHistoryFrequencyErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 27),
    _TokenRingHistoryFrequencyErrors_Type()
)
tokenRingHistoryFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryFrequencyErrors.setStatus("mandatory")
_TokenRingHistoryTokenErrors_Type = Counter32
_TokenRingHistoryTokenErrors_Object = MibTableColumn
tokenRingHistoryTokenErrors = _TokenRingHistoryTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 28),
    _TokenRingHistoryTokenErrors_Type()
)
tokenRingHistoryTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryTokenErrors.setStatus("mandatory")
_TokenRingHistorySoftErrorReports_Type = Counter32
_TokenRingHistorySoftErrorReports_Object = MibTableColumn
tokenRingHistorySoftErrorReports = _TokenRingHistorySoftErrorReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 29),
    _TokenRingHistorySoftErrorReports_Type()
)
tokenRingHistorySoftErrorReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistorySoftErrorReports.setStatus("mandatory")
_TokenRingHistoryActiveStations_Type = Integer32
_TokenRingHistoryActiveStations_Object = MibTableColumn
tokenRingHistoryActiveStations = _TokenRingHistoryActiveStations_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 30),
    _TokenRingHistoryActiveStations_Type()
)
tokenRingHistoryActiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryActiveStations.setStatus("mandatory")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 3)
)
_Hosts_ObjectIdentity = ObjectIdentity
hosts = _Hosts_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 4)
)
_HostTopN_ObjectIdentity = ObjectIdentity
hostTopN = _HostTopN_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 5)
)
_Matrix_ObjectIdentity = ObjectIdentity
matrix = _Matrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 6)
)
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 7)
)
_Capture_ObjectIdentity = ObjectIdentity
capture = _Capture_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 8)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 9)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 10)
)
_RingStationControlTable_Object = MibTable
ringStationControlTable = _RingStationControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1)
)
if mibBuilder.loadTexts:
    ringStationControlTable.setStatus("mandatory")
_RingStationControlEntry_Object = MibTableRow
ringStationControlEntry = _RingStationControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1)
)
ringStationControlEntry.setIndexNames(
    (0, "TR-RMON-MIB", "ringStationControlIfIndex"),
)
if mibBuilder.loadTexts:
    ringStationControlEntry.setStatus("mandatory")


class _RingStationControlIfIndex_Type(Integer32):
    """Custom type ringStationControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingStationControlIfIndex_Type.__name__ = "Integer32"
_RingStationControlIfIndex_Object = MibTableColumn
ringStationControlIfIndex = _RingStationControlIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 1),
    _RingStationControlIfIndex_Type()
)
ringStationControlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlIfIndex.setStatus("mandatory")


class _RingStationControlTableSize_Type(Integer32):
    """Custom type ringStationControlTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingStationControlTableSize_Type.__name__ = "Integer32"
_RingStationControlTableSize_Object = MibTableColumn
ringStationControlTableSize = _RingStationControlTableSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 2),
    _RingStationControlTableSize_Type()
)
ringStationControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlTableSize.setStatus("mandatory")


class _RingStationControlActiveStations_Type(Integer32):
    """Custom type ringStationControlActiveStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingStationControlActiveStations_Type.__name__ = "Integer32"
_RingStationControlActiveStations_Object = MibTableColumn
ringStationControlActiveStations = _RingStationControlActiveStations_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 3),
    _RingStationControlActiveStations_Type()
)
ringStationControlActiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlActiveStations.setStatus("mandatory")


class _RingStationControlRingState_Type(Integer32):
    """Custom type ringStationControlRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 1),
          ("ringPurgeState", 2),
          ("monitorContentionState", 3),
          ("beaconFrameStreamingState", 4),
          ("beaconBitStreamingState", 5),
          ("beaconRingSignalLossState", 6),
          ("beaconSetRecoveryModeState", 7))
    )


_RingStationControlRingState_Type.__name__ = "Integer32"
_RingStationControlRingState_Object = MibTableColumn
ringStationControlRingState = _RingStationControlRingState_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 4),
    _RingStationControlRingState_Type()
)
ringStationControlRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlRingState.setStatus("mandatory")


class _RingStationControlBeaconSender_Type(OctetString):
    """Custom type ringStationControlBeaconSender based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_RingStationControlBeaconSender_Type.__name__ = "OctetString"
_RingStationControlBeaconSender_Object = MibTableColumn
ringStationControlBeaconSender = _RingStationControlBeaconSender_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 5),
    _RingStationControlBeaconSender_Type()
)
ringStationControlBeaconSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlBeaconSender.setStatus("mandatory")


class _RingStationControlBeaconNAUN_Type(OctetString):
    """Custom type ringStationControlBeaconNAUN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_RingStationControlBeaconNAUN_Type.__name__ = "OctetString"
_RingStationControlBeaconNAUN_Object = MibTableColumn
ringStationControlBeaconNAUN = _RingStationControlBeaconNAUN_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 6),
    _RingStationControlBeaconNAUN_Type()
)
ringStationControlBeaconNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlBeaconNAUN.setStatus("mandatory")
_RingStationControlChanges_Type = Counter32
_RingStationControlChanges_Object = MibTableColumn
ringStationControlChanges = _RingStationControlChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 7),
    _RingStationControlChanges_Type()
)
ringStationControlChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlChanges.setStatus("mandatory")
_RingStationControlOwner_Type = OwnerString
_RingStationControlOwner_Object = MibTableColumn
ringStationControlOwner = _RingStationControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 8),
    _RingStationControlOwner_Type()
)
ringStationControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationControlOwner.setStatus("mandatory")


class _RingStationControlStatus_Type(Integer32):
    """Custom type ringStationControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_RingStationControlStatus_Type.__name__ = "Integer32"
_RingStationControlStatus_Object = MibTableColumn
ringStationControlStatus = _RingStationControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 9),
    _RingStationControlStatus_Type()
)
ringStationControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationControlStatus.setStatus("mandatory")
_RingStationTable_Object = MibTable
ringStationTable = _RingStationTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2)
)
if mibBuilder.loadTexts:
    ringStationTable.setStatus("mandatory")
_RingStationConfigTable_Object = MibTable
ringStationConfigTable = _RingStationConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2)
)
if mibBuilder.loadTexts:
    ringStationConfigTable.setStatus("mandatory")
_RingStationEntry_Object = MibTableRow
ringStationEntry = _RingStationEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1)
)
ringStationEntry.setIndexNames(
    (0, "TR-RMON-MIB", "ringStationIfIndex"),
    (0, "TR-RMON-MIB", "ringStationMacAddress"),
)
if mibBuilder.loadTexts:
    ringStationEntry.setStatus("mandatory")
_RingStationConfigEntry_Object = MibTableRow
ringStationConfigEntry = _RingStationConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1)
)
ringStationConfigEntry.setIndexNames(
    (0, "TR-RMON-MIB", "ringStationConfigIfIndex"),
    (0, "TR-RMON-MIB", "ringStationConfigMacAddress"),
)
if mibBuilder.loadTexts:
    ringStationConfigEntry.setStatus("mandatory")
_RingStationIfIndex_Type = Integer32
_RingStationIfIndex_Object = MibTableColumn
ringStationIfIndex = _RingStationIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 1),
    _RingStationIfIndex_Type()
)
ringStationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationIfIndex.setStatus("mandatory")
_RingStationConfigIfIndex_Type = Integer32
_RingStationConfigIfIndex_Object = MibTableColumn
ringStationConfigIfIndex = _RingStationConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 1),
    _RingStationConfigIfIndex_Type()
)
ringStationConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigIfIndex.setStatus("mandatory")


class _RingStationMACAddress_Type(OctetString):
    """Custom type ringStationMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_RingStationMACAddress_Type.__name__ = "OctetString"
_RingStationMACAddress_Object = MibScalar
ringStationMACAddress = _RingStationMACAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 2),
    _RingStationMACAddress_Type()
)
ringStationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationMACAddress.setStatus("mandatory")


class _RingStationConfigMACAddress_Type(OctetString):
    """Custom type ringStationConfigMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_RingStationConfigMACAddress_Type.__name__ = "OctetString"
_RingStationConfigMACAddress_Object = MibScalar
ringStationConfigMACAddress = _RingStationConfigMACAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 2),
    _RingStationConfigMACAddress_Type()
)
ringStationConfigMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigMACAddress.setStatus("mandatory")
_RingStationOrderIndex_Type = Integer32
_RingStationOrderIndex_Object = MibTableColumn
ringStationOrderIndex = _RingStationOrderIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 3),
    _RingStationOrderIndex_Type()
)
ringStationOrderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOrderIndex.setStatus("mandatory")


class _RingStationConfigRemove_Type(Integer32):
    """Custom type ringStationConfigRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 1),
          ("remove", 2))
    )


_RingStationConfigRemove_Type.__name__ = "Integer32"
_RingStationConfigRemove_Object = MibTableColumn
ringStationConfigRemove = _RingStationConfigRemove_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 3),
    _RingStationConfigRemove_Type()
)
ringStationConfigRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationConfigRemove.setStatus("mandatory")


class _RingStationStationStatus_Type(Integer32):
    """Custom type ringStationStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notInRingPoll", 3),
          ("forcedRemoval", 4))
    )


_RingStationStationStatus_Type.__name__ = "Integer32"
_RingStationStationStatus_Object = MibTableColumn
ringStationStationStatus = _RingStationStationStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 4),
    _RingStationStationStatus_Type()
)
ringStationStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationStationStatus.setStatus("mandatory")


class _RingStationConfigUpdate_Type(Integer32):
    """Custom type ringStationConfigUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 1),
          ("update", 2))
    )


_RingStationConfigUpdate_Type.__name__ = "Integer32"
_RingStationConfigUpdate_Object = MibScalar
ringStationConfigUpdate = _RingStationConfigUpdate_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 4),
    _RingStationConfigUpdate_Type()
)
ringStationConfigUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationConfigUpdate.setStatus("mandatory")
_RingStationLastEnterTime_Type = TimeTicks
_RingStationLastEnterTime_Object = MibTableColumn
ringStationLastEnterTime = _RingStationLastEnterTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 5),
    _RingStationLastEnterTime_Type()
)
ringStationLastEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLastEnterTime.setStatus("mandatory")
_RingStationLastExitTime_Type = TimeTicks
_RingStationLastExitTime_Object = MibTableColumn
ringStationLastExitTime = _RingStationLastExitTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 6),
    _RingStationLastExitTime_Type()
)
ringStationLastExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLastExitTime.setStatus("mandatory")
_RingStationDuplicateAddresses_Type = Counter32
_RingStationDuplicateAddresses_Object = MibTableColumn
ringStationDuplicateAddresses = _RingStationDuplicateAddresses_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 7),
    _RingStationDuplicateAddresses_Type()
)
ringStationDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationDuplicateAddresses.setStatus("mandatory")
_RingStationLineErrors_Type = Counter32
_RingStationLineErrors_Object = MibTableColumn
ringStationLineErrors = _RingStationLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 8),
    _RingStationLineErrors_Type()
)
ringStationLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLineErrors.setStatus("mandatory")
_RingStationInternalErrors_Type = Counter32
_RingStationInternalErrors_Object = MibTableColumn
ringStationInternalErrors = _RingStationInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 9),
    _RingStationInternalErrors_Type()
)
ringStationInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInternalErrors.setStatus("mandatory")
_RingStationBurstErrors_Type = Counter32
_RingStationBurstErrors_Object = MibTableColumn
ringStationBurstErrors = _RingStationBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 10),
    _RingStationBurstErrors_Type()
)
ringStationBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationBurstErrors.setStatus("mandatory")
_RingStationACErrors_Type = Counter32
_RingStationACErrors_Object = MibTableColumn
ringStationACErrors = _RingStationACErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 11),
    _RingStationACErrors_Type()
)
ringStationACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationACErrors.setStatus("mandatory")
_RingStationAbortErrors_Type = Counter32
_RingStationAbortErrors_Object = MibTableColumn
ringStationAbortErrors = _RingStationAbortErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 12),
    _RingStationAbortErrors_Type()
)
ringStationAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationAbortErrors.setStatus("mandatory")
_RingStationLostFramesErrors_Type = Counter32
_RingStationLostFramesErrors_Object = MibTableColumn
ringStationLostFramesErrors = _RingStationLostFramesErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 13),
    _RingStationLostFramesErrors_Type()
)
ringStationLostFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLostFramesErrors.setStatus("mandatory")
_RingStationCongestionErrors_Type = Counter32
_RingStationCongestionErrors_Object = MibScalar
ringStationCongestionErrors = _RingStationCongestionErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 14),
    _RingStationCongestionErrors_Type()
)
ringStationCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationCongestionErrors.setStatus("mandatory")
_RingStationFrameCopiedErrors_Type = Counter32
_RingStationFrameCopiedErrors_Object = MibTableColumn
ringStationFrameCopiedErrors = _RingStationFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 15),
    _RingStationFrameCopiedErrors_Type()
)
ringStationFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationFrameCopiedErrors.setStatus("mandatory")
_RingStationFrequencyErrors_Type = Counter32
_RingStationFrequencyErrors_Object = MibTableColumn
ringStationFrequencyErrors = _RingStationFrequencyErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 16),
    _RingStationFrequencyErrors_Type()
)
ringStationFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationFrequencyErrors.setStatus("mandatory")
_RingStationTokenErrors_Type = Counter32
_RingStationTokenErrors_Object = MibTableColumn
ringStationTokenErrors = _RingStationTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 17),
    _RingStationTokenErrors_Type()
)
ringStationTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationTokenErrors.setStatus("mandatory")
_RingStationInBeaconErrors_Type = Counter32
_RingStationInBeaconErrors_Object = MibTableColumn
ringStationInBeaconErrors = _RingStationInBeaconErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 18),
    _RingStationInBeaconErrors_Type()
)
ringStationInBeaconErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInBeaconErrors.setStatus("mandatory")
_RingStationOutBeaconErrors_Type = Counter32
_RingStationOutBeaconErrors_Object = MibTableColumn
ringStationOutBeaconErrors = _RingStationOutBeaconErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 19),
    _RingStationOutBeaconErrors_Type()
)
ringStationOutBeaconErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOutBeaconErrors.setStatus("mandatory")
_RingStationInsertions_Type = Counter32
_RingStationInsertions_Object = MibTableColumn
ringStationInsertions = _RingStationInsertions_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 20),
    _RingStationInsertions_Type()
)
ringStationInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInsertions.setStatus("mandatory")
_SourceRoutingStatsTable_Object = MibTable
sourceRoutingStatsTable = _SourceRoutingStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3)
)
if mibBuilder.loadTexts:
    sourceRoutingStatsTable.setStatus("mandatory")
_SourceRoutingStatsEntry_Object = MibTableRow
sourceRoutingStatsEntry = _SourceRoutingStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1)
)
sourceRoutingStatsEntry.setIndexNames(
    (0, "TR-RMON-MIB", "sourceRoutingStatsIfIndex"),
)
if mibBuilder.loadTexts:
    sourceRoutingStatsEntry.setStatus("mandatory")
_SourceRoutingStatsIfIndex_Type = Integer32
_SourceRoutingStatsIfIndex_Object = MibTableColumn
sourceRoutingStatsIfIndex = _SourceRoutingStatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 1),
    _SourceRoutingStatsIfIndex_Type()
)
sourceRoutingStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsIfIndex.setStatus("mandatory")
_SourceRoutingStatsRingNumber_Type = Integer32
_SourceRoutingStatsRingNumber_Object = MibTableColumn
sourceRoutingStatsRingNumber = _SourceRoutingStatsRingNumber_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 2),
    _SourceRoutingStatsRingNumber_Type()
)
sourceRoutingStatsRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsRingNumber.setStatus("mandatory")
_SourceRoutingStatsInFrames_Type = Counter32
_SourceRoutingStatsInFrames_Object = MibTableColumn
sourceRoutingStatsInFrames = _SourceRoutingStatsInFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 3),
    _SourceRoutingStatsInFrames_Type()
)
sourceRoutingStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsInFrames.setStatus("mandatory")
_SourceRoutingStatsOutFrames_Type = Counter32
_SourceRoutingStatsOutFrames_Object = MibTableColumn
sourceRoutingStatsOutFrames = _SourceRoutingStatsOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 4),
    _SourceRoutingStatsOutFrames_Type()
)
sourceRoutingStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsOutFrames.setStatus("mandatory")
_SourceRoutingStatsThroughFrames_Type = Counter32
_SourceRoutingStatsThroughFrames_Object = MibTableColumn
sourceRoutingStatsThroughFrames = _SourceRoutingStatsThroughFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 5),
    _SourceRoutingStatsThroughFrames_Type()
)
sourceRoutingStatsThroughFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsThroughFrames.setStatus("mandatory")
_SourceRoutingStatsAllRoutesBroadcastFrames_Type = Counter32
_SourceRoutingStatsAllRoutesBroadcastFrames_Object = MibTableColumn
sourceRoutingStatsAllRoutesBroadcastFrames = _SourceRoutingStatsAllRoutesBroadcastFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 6),
    _SourceRoutingStatsAllRoutesBroadcastFrames_Type()
)
sourceRoutingStatsAllRoutesBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsAllRoutesBroadcastFrames.setStatus("mandatory")
_SourceRoutingStatsSingleRoutesBroadcastFrames_Type = Counter32
_SourceRoutingStatsSingleRoutesBroadcastFrames_Object = MibScalar
sourceRoutingStatsSingleRoutesBroadcastFrames = _SourceRoutingStatsSingleRoutesBroadcastFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 7),
    _SourceRoutingStatsSingleRoutesBroadcastFrames_Type()
)
sourceRoutingStatsSingleRoutesBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsSingleRoutesBroadcastFrames.setStatus("mandatory")
_SourceRoutingStatsInOctets_Type = Counter32
_SourceRoutingStatsInOctets_Object = MibTableColumn
sourceRoutingStatsInOctets = _SourceRoutingStatsInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 8),
    _SourceRoutingStatsInOctets_Type()
)
sourceRoutingStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsInOctets.setStatus("mandatory")
_SourceRoutingStatsOutOctets_Type = Counter32
_SourceRoutingStatsOutOctets_Object = MibTableColumn
sourceRoutingStatsOutOctets = _SourceRoutingStatsOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 9),
    _SourceRoutingStatsOutOctets_Type()
)
sourceRoutingStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsOutOctets.setStatus("mandatory")
_SourceRoutingStatsThroughOctets_Type = Counter32
_SourceRoutingStatsThroughOctets_Object = MibTableColumn
sourceRoutingStatsThroughOctets = _SourceRoutingStatsThroughOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 10),
    _SourceRoutingStatsThroughOctets_Type()
)
sourceRoutingStatsThroughOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsThroughOctets.setStatus("mandatory")
_SourceRoutingStatsAllRoutesBroadcastOctets_Type = Counter32
_SourceRoutingStatsAllRoutesBroadcastOctets_Object = MibTableColumn
sourceRoutingStatsAllRoutesBroadcastOctets = _SourceRoutingStatsAllRoutesBroadcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 11),
    _SourceRoutingStatsAllRoutesBroadcastOctets_Type()
)
sourceRoutingStatsAllRoutesBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsAllRoutesBroadcastOctets.setStatus("mandatory")
_SourceRoutingStatsSingleRoutesBroadcastOctets_Type = Counter32
_SourceRoutingStatsSingleRoutesBroadcastOctets_Object = MibTableColumn
sourceRoutingStatsSingleRoutesBroadcastOctets = _SourceRoutingStatsSingleRoutesBroadcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 12),
    _SourceRoutingStatsSingleRoutesBroadcastOctets_Type()
)
sourceRoutingStatsSingleRoutesBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsSingleRoutesBroadcastOctets.setStatus("mandatory")
_SourceRoutingStats0HopsFrames_Type = Counter32
_SourceRoutingStats0HopsFrames_Object = MibTableColumn
sourceRoutingStats0HopsFrames = _SourceRoutingStats0HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 13),
    _SourceRoutingStats0HopsFrames_Type()
)
sourceRoutingStats0HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats0HopsFrames.setStatus("mandatory")
_SourceRoutingStats1HopFrames_Type = Counter32
_SourceRoutingStats1HopFrames_Object = MibTableColumn
sourceRoutingStats1HopFrames = _SourceRoutingStats1HopFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 14),
    _SourceRoutingStats1HopFrames_Type()
)
sourceRoutingStats1HopFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats1HopFrames.setStatus("mandatory")
_SourceRoutingStats2HopsFrames_Type = Counter32
_SourceRoutingStats2HopsFrames_Object = MibTableColumn
sourceRoutingStats2HopsFrames = _SourceRoutingStats2HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 15),
    _SourceRoutingStats2HopsFrames_Type()
)
sourceRoutingStats2HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats2HopsFrames.setStatus("mandatory")
_SourceRoutingStats3HopsFrames_Type = Counter32
_SourceRoutingStats3HopsFrames_Object = MibTableColumn
sourceRoutingStats3HopsFrames = _SourceRoutingStats3HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 16),
    _SourceRoutingStats3HopsFrames_Type()
)
sourceRoutingStats3HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats3HopsFrames.setStatus("mandatory")
_SourceRoutingStats4HopsFrames_Type = Counter32
_SourceRoutingStats4HopsFrames_Object = MibTableColumn
sourceRoutingStats4HopsFrames = _SourceRoutingStats4HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 17),
    _SourceRoutingStats4HopsFrames_Type()
)
sourceRoutingStats4HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats4HopsFrames.setStatus("mandatory")
_SourceRoutingStats5HopsFrames_Type = Counter32
_SourceRoutingStats5HopsFrames_Object = MibTableColumn
sourceRoutingStats5HopsFrames = _SourceRoutingStats5HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 18),
    _SourceRoutingStats5HopsFrames_Type()
)
sourceRoutingStats5HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats5HopsFrames.setStatus("mandatory")
_SourceRoutingStats6HopsFrames_Type = Counter32
_SourceRoutingStats6HopsFrames_Object = MibTableColumn
sourceRoutingStats6HopsFrames = _SourceRoutingStats6HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 19),
    _SourceRoutingStats6HopsFrames_Type()
)
sourceRoutingStats6HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats6HopsFrames.setStatus("mandatory")
_SourceRoutingStats7HopsFrames_Type = Counter32
_SourceRoutingStats7HopsFrames_Object = MibTableColumn
sourceRoutingStats7HopsFrames = _SourceRoutingStats7HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 20),
    _SourceRoutingStats7HopsFrames_Type()
)
sourceRoutingStats7HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats7HopsFrames.setStatus("mandatory")
_SourceRoutingStats8orMoreHopsFrames_Type = Counter32
_SourceRoutingStats8orMoreHopsFrames_Object = MibTableColumn
sourceRoutingStats8orMoreHopsFrames = _SourceRoutingStats8orMoreHopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 21),
    _SourceRoutingStats8orMoreHopsFrames_Type()
)
sourceRoutingStats8orMoreHopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats8orMoreHopsFrames.setStatus("mandatory")
_SourceRoutingStatsOwner_Type = OwnerString
_SourceRoutingStatsOwner_Object = MibTableColumn
sourceRoutingStatsOwner = _SourceRoutingStatsOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 22),
    _SourceRoutingStatsOwner_Type()
)
sourceRoutingStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceRoutingStatsOwner.setStatus("mandatory")


class _SourceRoutingStatsStatus_Type(Integer32):
    """Custom type sourceRoutingStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )


_SourceRoutingStatsStatus_Type.__name__ = "Integer32"
_SourceRoutingStatsStatus_Object = MibTableColumn
sourceRoutingStatsStatus = _SourceRoutingStatsStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 23),
    _SourceRoutingStatsStatus_Type()
)
sourceRoutingStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceRoutingStatsStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TR-RMON-MIB",
    **{"OwnerString": OwnerString,
       "mib-2": mib_2,
       "rmon": rmon,
       "statistics": statistics,
       "tokenRingStatsTable": tokenRingStatsTable,
       "tokenRingStatsEntry": tokenRingStatsEntry,
       "tokenRingStatsIndex": tokenRingStatsIndex,
       "tokenRingStatsDataSource": tokenRingStatsDataSource,
       "tokenRingStatsDropEvents": tokenRingStatsDropEvents,
       "tokenRingStatsOctets": tokenRingStatsOctets,
       "tokenRingStatsPkts": tokenRingStatsPkts,
       "tokenRingStatsDataBroadcastPkts": tokenRingStatsDataBroadcastPkts,
       "tokenRingStatsDataAllRoutesBroadcastPkts": tokenRingStatsDataAllRoutesBroadcastPkts,
       "tokenRingStatsDataMulticastPkts": tokenRingStatsDataMulticastPkts,
       "tokenRingStatsMACOctets": tokenRingStatsMACOctets,
       "tokenRingStatsMACPkts": tokenRingStatsMACPkts,
       "tokenRingStatsRingPurgeEvents": tokenRingStatsRingPurgeEvents,
       "tokenRingStatsRingPurgePackets": tokenRingStatsRingPurgePackets,
       "tokenRingStatsBeaconEvents": tokenRingStatsBeaconEvents,
       "tokenRingStatsBeaconPackets": tokenRingStatsBeaconPackets,
       "tokenRingStatsMonitorContentionEvents": tokenRingStatsMonitorContentionEvents,
       "tokenRingStatsMonitorContentionPackets": tokenRingStatsMonitorContentionPackets,
       "tokenRingStatsNAUNChanges": tokenRingStatsNAUNChanges,
       "tokenRingStatsLineErrors": tokenRingStatsLineErrors,
       "tokenRingStatsInternalErrors": tokenRingStatsInternalErrors,
       "tokenRingStatsBurstErrors": tokenRingStatsBurstErrors,
       "tokenRingStatsACErrors": tokenRingStatsACErrors,
       "tokenRingStatsAbortErrors": tokenRingStatsAbortErrors,
       "tokenRingStatsLostFramesErrors": tokenRingStatsLostFramesErrors,
       "tokenRingStatsCongestionErrors": tokenRingStatsCongestionErrors,
       "tokenRingStatsFrameCopiedErrors": tokenRingStatsFrameCopiedErrors,
       "tokenRingStatsFrequencyErrors": tokenRingStatsFrequencyErrors,
       "tokenRingStatsTokenErrors": tokenRingStatsTokenErrors,
       "tokenRingStatsSoftErrorReports": tokenRingStatsSoftErrorReports,
       "tokenRingStatsDataPkts18to63Octets": tokenRingStatsDataPkts18to63Octets,
       "tokenRingStatsDataPkts64to127Octets": tokenRingStatsDataPkts64to127Octets,
       "tokenRingStatsDataPkts128to255Octets": tokenRingStatsDataPkts128to255Octets,
       "tokenRingStatsDataPkts256to511Octets": tokenRingStatsDataPkts256to511Octets,
       "tokenRingStatsDataPkts512to1023Octets": tokenRingStatsDataPkts512to1023Octets,
       "tokenRingStatsDataPkts1024to2047Octets": tokenRingStatsDataPkts1024to2047Octets,
       "tokenRingStatsDataPkts2048to4095Octets": tokenRingStatsDataPkts2048to4095Octets,
       "tokenRingStatsDataPkts4096to8191Octets": tokenRingStatsDataPkts4096to8191Octets,
       "tokenRingStatsDataPkts8192to18000Octets": tokenRingStatsDataPkts8192to18000Octets,
       "tokenRingStatsDataPkts18000orGreaterOctets": tokenRingStatsDataPkts18000orGreaterOctets,
       "history": history,
       "tokenRingHistoryTable": tokenRingHistoryTable,
       "tokenRingHistoryEntry": tokenRingHistoryEntry,
       "tokenRingHistoryIndex": tokenRingHistoryIndex,
       "tokenRingHistorySampleIndex": tokenRingHistorySampleIndex,
       "tokenRingHistoryIntervalStart": tokenRingHistoryIntervalStart,
       "tokenRingHistoryDropEvents": tokenRingHistoryDropEvents,
       "tokenRingHistoryOctets": tokenRingHistoryOctets,
       "tokenRingHistoryPkts": tokenRingHistoryPkts,
       "tokenRingHistoryDataBroadcastPkts": tokenRingHistoryDataBroadcastPkts,
       "tokenRingHistoryDataAllRoutesBroadcastPkts": tokenRingHistoryDataAllRoutesBroadcastPkts,
       "tokenRingHistoryDataMulticastPkts": tokenRingHistoryDataMulticastPkts,
       "tokenRingHistoryMACOctets": tokenRingHistoryMACOctets,
       "tokenRingHistoryMACPkts": tokenRingHistoryMACPkts,
       "tokenRingHistoryRingPurgeEvents": tokenRingHistoryRingPurgeEvents,
       "tokenRingHistoryRingPurgePackets": tokenRingHistoryRingPurgePackets,
       "tokenRingHistoryBeaconEvents": tokenRingHistoryBeaconEvents,
       "tokenRingHistoryBeaconPackets": tokenRingHistoryBeaconPackets,
       "tokenRingHistoryMonitorContentionEvents": tokenRingHistoryMonitorContentionEvents,
       "tokenRingHistoryMonitorContentionPackets": tokenRingHistoryMonitorContentionPackets,
       "tokenRingHistoryNAUNChanges": tokenRingHistoryNAUNChanges,
       "tokenRingHistoryLineErrors": tokenRingHistoryLineErrors,
       "tokenRingHistoryInternalErrors": tokenRingHistoryInternalErrors,
       "tokenRingHistoryBurstErrors": tokenRingHistoryBurstErrors,
       "tokenRingHistoryACErrors": tokenRingHistoryACErrors,
       "tokenRingHistoryAbortErrors": tokenRingHistoryAbortErrors,
       "tokenRingHistoryLostFramesErrors": tokenRingHistoryLostFramesErrors,
       "tokenRingHistoryCongestionErrors": tokenRingHistoryCongestionErrors,
       "tokenRingHistoryFrameCopiedErrors": tokenRingHistoryFrameCopiedErrors,
       "tokenRingHistoryFrequencyErrors": tokenRingHistoryFrequencyErrors,
       "tokenRingHistoryTokenErrors": tokenRingHistoryTokenErrors,
       "tokenRingHistorySoftErrorReports": tokenRingHistorySoftErrorReports,
       "tokenRingHistoryActiveStations": tokenRingHistoryActiveStations,
       "alarm": alarm,
       "hosts": hosts,
       "hostTopN": hostTopN,
       "matrix": matrix,
       "filter": filter,
       "capture": capture,
       "event": event,
       "tokenRing": tokenRing,
       "ringStationControlTable": ringStationControlTable,
       "ringStationControlEntry": ringStationControlEntry,
       "ringStationControlIfIndex": ringStationControlIfIndex,
       "ringStationControlTableSize": ringStationControlTableSize,
       "ringStationControlActiveStations": ringStationControlActiveStations,
       "ringStationControlRingState": ringStationControlRingState,
       "ringStationControlBeaconSender": ringStationControlBeaconSender,
       "ringStationControlBeaconNAUN": ringStationControlBeaconNAUN,
       "ringStationControlChanges": ringStationControlChanges,
       "ringStationControlOwner": ringStationControlOwner,
       "ringStationControlStatus": ringStationControlStatus,
       "ringStationTable": ringStationTable,
       "ringStationConfigTable": ringStationConfigTable,
       "ringStationEntry": ringStationEntry,
       "ringStationConfigEntry": ringStationConfigEntry,
       "ringStationIfIndex": ringStationIfIndex,
       "ringStationConfigIfIndex": ringStationConfigIfIndex,
       "ringStationMACAddress": ringStationMACAddress,
       "ringStationConfigMACAddress": ringStationConfigMACAddress,
       "ringStationOrderIndex": ringStationOrderIndex,
       "ringStationConfigRemove": ringStationConfigRemove,
       "ringStationStationStatus": ringStationStationStatus,
       "ringStationConfigUpdate": ringStationConfigUpdate,
       "ringStationLastEnterTime": ringStationLastEnterTime,
       "ringStationLastExitTime": ringStationLastExitTime,
       "ringStationDuplicateAddresses": ringStationDuplicateAddresses,
       "ringStationLineErrors": ringStationLineErrors,
       "ringStationInternalErrors": ringStationInternalErrors,
       "ringStationBurstErrors": ringStationBurstErrors,
       "ringStationACErrors": ringStationACErrors,
       "ringStationAbortErrors": ringStationAbortErrors,
       "ringStationLostFramesErrors": ringStationLostFramesErrors,
       "ringStationCongestionErrors": ringStationCongestionErrors,
       "ringStationFrameCopiedErrors": ringStationFrameCopiedErrors,
       "ringStationFrequencyErrors": ringStationFrequencyErrors,
       "ringStationTokenErrors": ringStationTokenErrors,
       "ringStationInBeaconErrors": ringStationInBeaconErrors,
       "ringStationOutBeaconErrors": ringStationOutBeaconErrors,
       "ringStationInsertions": ringStationInsertions,
       "sourceRoutingStatsTable": sourceRoutingStatsTable,
       "sourceRoutingStatsEntry": sourceRoutingStatsEntry,
       "sourceRoutingStatsIfIndex": sourceRoutingStatsIfIndex,
       "sourceRoutingStatsRingNumber": sourceRoutingStatsRingNumber,
       "sourceRoutingStatsInFrames": sourceRoutingStatsInFrames,
       "sourceRoutingStatsOutFrames": sourceRoutingStatsOutFrames,
       "sourceRoutingStatsThroughFrames": sourceRoutingStatsThroughFrames,
       "sourceRoutingStatsAllRoutesBroadcastFrames": sourceRoutingStatsAllRoutesBroadcastFrames,
       "sourceRoutingStatsSingleRoutesBroadcastFrames": sourceRoutingStatsSingleRoutesBroadcastFrames,
       "sourceRoutingStatsInOctets": sourceRoutingStatsInOctets,
       "sourceRoutingStatsOutOctets": sourceRoutingStatsOutOctets,
       "sourceRoutingStatsThroughOctets": sourceRoutingStatsThroughOctets,
       "sourceRoutingStatsAllRoutesBroadcastOctets": sourceRoutingStatsAllRoutesBroadcastOctets,
       "sourceRoutingStatsSingleRoutesBroadcastOctets": sourceRoutingStatsSingleRoutesBroadcastOctets,
       "sourceRoutingStats0HopsFrames": sourceRoutingStats0HopsFrames,
       "sourceRoutingStats1HopFrames": sourceRoutingStats1HopFrames,
       "sourceRoutingStats2HopsFrames": sourceRoutingStats2HopsFrames,
       "sourceRoutingStats3HopsFrames": sourceRoutingStats3HopsFrames,
       "sourceRoutingStats4HopsFrames": sourceRoutingStats4HopsFrames,
       "sourceRoutingStats5HopsFrames": sourceRoutingStats5HopsFrames,
       "sourceRoutingStats6HopsFrames": sourceRoutingStats6HopsFrames,
       "sourceRoutingStats7HopsFrames": sourceRoutingStats7HopsFrames,
       "sourceRoutingStats8orMoreHopsFrames": sourceRoutingStats8orMoreHopsFrames,
       "sourceRoutingStatsOwner": sourceRoutingStatsOwner,
       "sourceRoutingStatsStatus": sourceRoutingStatsStatus}
)
