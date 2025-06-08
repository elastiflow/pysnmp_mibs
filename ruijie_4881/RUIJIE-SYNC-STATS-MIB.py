# SNMP MIB module (RUIJIE-SYNC-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SYNC-STATS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:11 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ruijieSyncStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51)
)
if mibBuilder.loadTexts:
    ruijieSyncStatsMIB.setRevisions(
        ("2009-05-20 14:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSyncStatsMibObjects_ObjectIdentity = ObjectIdentity
ruijieSyncStatsMibObjects = _RuijieSyncStatsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1)
)
_RuijieStatsSyncGlobal_ObjectIdentity = ObjectIdentity
ruijieStatsSyncGlobal = _RuijieStatsSyncGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 1)
)
_RuijieSyncStatsTable_Object = MibTable
ruijieSyncStatsTable = _RuijieSyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieSyncStatsTable.setStatus("current")
_RuijieSyncStatsEntry_Object = MibTableRow
ruijieSyncStatsEntry = _RuijieSyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1)
)
ruijieSyncStatsEntry.setIndexNames(
    (0, "RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsSlot"),
    (0, "RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsConn"),
    (0, "RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsChannel"),
)
if mibBuilder.loadTexts:
    ruijieSyncStatsEntry.setStatus("current")
_RuijieSyncStatsRowStatus_Type = RowStatus
_RuijieSyncStatsRowStatus_Object = MibTableColumn
ruijieSyncStatsRowStatus = _RuijieSyncStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 1),
    _RuijieSyncStatsRowStatus_Type()
)
ruijieSyncStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSyncStatsRowStatus.setStatus("current")


class _RuijieSyncStatsSlot_Type(Integer32):
    """Custom type ruijieSyncStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieSyncStatsSlot_Type.__name__ = "Integer32"
_RuijieSyncStatsSlot_Object = MibTableColumn
ruijieSyncStatsSlot = _RuijieSyncStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 2),
    _RuijieSyncStatsSlot_Type()
)
ruijieSyncStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsSlot.setStatus("current")


class _RuijieSyncStatsConn_Type(Integer32):
    """Custom type ruijieSyncStatsConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieSyncStatsConn_Type.__name__ = "Integer32"
_RuijieSyncStatsConn_Object = MibTableColumn
ruijieSyncStatsConn = _RuijieSyncStatsConn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 3),
    _RuijieSyncStatsConn_Type()
)
ruijieSyncStatsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsConn.setStatus("current")


class _RuijieSyncStatsChannel_Type(Integer32):
    """Custom type ruijieSyncStatsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieSyncStatsChannel_Type.__name__ = "Integer32"
_RuijieSyncStatsChannel_Object = MibTableColumn
ruijieSyncStatsChannel = _RuijieSyncStatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 4),
    _RuijieSyncStatsChannel_Type()
)
ruijieSyncStatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsChannel.setStatus("current")
_RuijieSyncStatsIfIndex_Type = InterfaceIndex
_RuijieSyncStatsIfIndex_Object = MibTableColumn
ruijieSyncStatsIfIndex = _RuijieSyncStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 5),
    _RuijieSyncStatsIfIndex_Type()
)
ruijieSyncStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsIfIndex.setStatus("current")


class _RuijieSyncStatsPortState_Type(Integer32):
    """Custom type ruijieSyncStatsPortState based on Integer32"""
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
        *(("init", 1),
          ("running", 2),
          ("up", 3),
          ("down", 4))
    )


_RuijieSyncStatsPortState_Type.__name__ = "Integer32"
_RuijieSyncStatsPortState_Object = MibTableColumn
ruijieSyncStatsPortState = _RuijieSyncStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 6),
    _RuijieSyncStatsPortState_Type()
)
ruijieSyncStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsPortState.setStatus("current")
_RuijieSyncStatsRxFrames_Type = Counter32
_RuijieSyncStatsRxFrames_Object = MibTableColumn
ruijieSyncStatsRxFrames = _RuijieSyncStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 7),
    _RuijieSyncStatsRxFrames_Type()
)
ruijieSyncStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxFrames.setStatus("current")
_RuijieSyncStatsRxOctets_Type = Counter32
_RuijieSyncStatsRxOctets_Object = MibTableColumn
ruijieSyncStatsRxOctets = _RuijieSyncStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 8),
    _RuijieSyncStatsRxOctets_Type()
)
ruijieSyncStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxOctets.setStatus("current")
_RuijieSyncStatsRxReplenFails_Type = Counter32
_RuijieSyncStatsRxReplenFails_Object = MibTableColumn
ruijieSyncStatsRxReplenFails = _RuijieSyncStatsRxReplenFails_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 9),
    _RuijieSyncStatsRxReplenFails_Type()
)
ruijieSyncStatsRxReplenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxReplenFails.setStatus("current")
_RuijieSyncStatsRxClockErrors_Type = Counter32
_RuijieSyncStatsRxClockErrors_Object = MibTableColumn
ruijieSyncStatsRxClockErrors = _RuijieSyncStatsRxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 10),
    _RuijieSyncStatsRxClockErrors_Type()
)
ruijieSyncStatsRxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxClockErrors.setStatus("current")
_RuijieSyncStatsRxDpllErrors_Type = Counter32
_RuijieSyncStatsRxDpllErrors_Object = MibTableColumn
ruijieSyncStatsRxDpllErrors = _RuijieSyncStatsRxDpllErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 11),
    _RuijieSyncStatsRxDpllErrors_Type()
)
ruijieSyncStatsRxDpllErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxDpllErrors.setStatus("current")
_RuijieSyncStatsRxFrameTooLongErrors_Type = Counter32
_RuijieSyncStatsRxFrameTooLongErrors_Object = MibTableColumn
ruijieSyncStatsRxFrameTooLongErrors = _RuijieSyncStatsRxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 12),
    _RuijieSyncStatsRxFrameTooLongErrors_Type()
)
ruijieSyncStatsRxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxFrameTooLongErrors.setStatus("current")
_RuijieSyncStatsRxFrameOctetAlignErrors_Type = Counter32
_RuijieSyncStatsRxFrameOctetAlignErrors_Object = MibTableColumn
ruijieSyncStatsRxFrameOctetAlignErrors = _RuijieSyncStatsRxFrameOctetAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 13),
    _RuijieSyncStatsRxFrameOctetAlignErrors_Type()
)
ruijieSyncStatsRxFrameOctetAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxFrameOctetAlignErrors.setStatus("current")
_RuijieSyncStatsRxAbortErrors_Type = Counter32
_RuijieSyncStatsRxAbortErrors_Object = MibTableColumn
ruijieSyncStatsRxAbortErrors = _RuijieSyncStatsRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 14),
    _RuijieSyncStatsRxAbortErrors_Type()
)
ruijieSyncStatsRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxAbortErrors.setStatus("current")
_RuijieSyncStatsRxCrcErrors_Type = Counter32
_RuijieSyncStatsRxCrcErrors_Object = MibTableColumn
ruijieSyncStatsRxCrcErrors = _RuijieSyncStatsRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 15),
    _RuijieSyncStatsRxCrcErrors_Type()
)
ruijieSyncStatsRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxCrcErrors.setStatus("current")
_RuijieSyncStatsRxRcvrOverrunErrors_Type = Counter32
_RuijieSyncStatsRxRcvrOverrunErrors_Object = MibTableColumn
ruijieSyncStatsRxRcvrOverrunErrors = _RuijieSyncStatsRxRcvrOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 16),
    _RuijieSyncStatsRxRcvrOverrunErrors_Type()
)
ruijieSyncStatsRxRcvrOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsRxRcvrOverrunErrors.setStatus("current")
_RuijieSyncStatsTxFrames_Type = Counter32
_RuijieSyncStatsTxFrames_Object = MibTableColumn
ruijieSyncStatsTxFrames = _RuijieSyncStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 17),
    _RuijieSyncStatsTxFrames_Type()
)
ruijieSyncStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsTxFrames.setStatus("current")
_RuijieSyncStatsTxOctets_Type = Counter32
_RuijieSyncStatsTxOctets_Object = MibTableColumn
ruijieSyncStatsTxOctets = _RuijieSyncStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 18),
    _RuijieSyncStatsTxOctets_Type()
)
ruijieSyncStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsTxOctets.setStatus("current")
_RuijieSyncStatsTxRingFullDropsErrors_Type = Counter32
_RuijieSyncStatsTxRingFullDropsErrors_Object = MibTableColumn
ruijieSyncStatsTxRingFullDropsErrors = _RuijieSyncStatsTxRingFullDropsErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 19),
    _RuijieSyncStatsTxRingFullDropsErrors_Type()
)
ruijieSyncStatsTxRingFullDropsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsTxRingFullDropsErrors.setStatus("current")
_RuijieSyncStatsTxClockErrors_Type = Counter32
_RuijieSyncStatsTxClockErrors_Object = MibTableColumn
ruijieSyncStatsTxClockErrors = _RuijieSyncStatsTxClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 20),
    _RuijieSyncStatsTxClockErrors_Type()
)
ruijieSyncStatsTxClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsTxClockErrors.setStatus("current")
_RuijieSyncStatsTxFrameTooLongErrors_Type = Counter32
_RuijieSyncStatsTxFrameTooLongErrors_Object = MibTableColumn
ruijieSyncStatsTxFrameTooLongErrors = _RuijieSyncStatsTxFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 21),
    _RuijieSyncStatsTxFrameTooLongErrors_Type()
)
ruijieSyncStatsTxFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsTxFrameTooLongErrors.setStatus("current")
_RuijieSyncStatsTxUnderrunErrors_Type = Counter32
_RuijieSyncStatsTxUnderrunErrors_Object = MibTableColumn
ruijieSyncStatsTxUnderrunErrors = _RuijieSyncStatsTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 1, 2, 1, 22),
    _RuijieSyncStatsTxUnderrunErrors_Type()
)
ruijieSyncStatsTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSyncStatsTxUnderrunErrors.setStatus("current")
_RuijieSyncStatsMibConformance_ObjectIdentity = ObjectIdentity
ruijieSyncStatsMibConformance = _RuijieSyncStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 2)
)
_RuijieSyncStatsMibCompliances_ObjectIdentity = ObjectIdentity
ruijieSyncStatsMibCompliances = _RuijieSyncStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 2, 1)
)
_RuijieSyncStatsMibGroups_ObjectIdentity = ObjectIdentity
ruijieSyncStatsMibGroups = _RuijieSyncStatsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 2, 2)
)

# Managed Objects groups

ruijieSyncStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 2, 2, 1)
)
ruijieSyncStatsGroup.setObjects(
      *(("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRowStatus"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsSlot"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsConn"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsChannel"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsIfIndex"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsPortState"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxFrames"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxOctets"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxReplenFails"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxClockErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxDpllErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxFrameTooLongErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxFrameOctetAlignErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxAbortErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxCrcErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsRxRcvrOverrunErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsTxFrames"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsTxOctets"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsTxRingFullDropsErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsTxClockErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsTxFrameTooLongErrors"),
        ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsTxUnderrunErrors"))
)
if mibBuilder.loadTexts:
    ruijieSyncStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSyncStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 51, 2, 1, 1)
)
ruijieSyncStatsMibCompliance.setObjects(
    ("RUIJIE-SYNC-STATS-MIB", "ruijieSyncStatsGroup")
)
if mibBuilder.loadTexts:
    ruijieSyncStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SYNC-STATS-MIB",
    **{"ruijieSyncStatsMIB": ruijieSyncStatsMIB,
       "ruijieSyncStatsMibObjects": ruijieSyncStatsMibObjects,
       "ruijieStatsSyncGlobal": ruijieStatsSyncGlobal,
       "ruijieSyncStatsTable": ruijieSyncStatsTable,
       "ruijieSyncStatsEntry": ruijieSyncStatsEntry,
       "ruijieSyncStatsRowStatus": ruijieSyncStatsRowStatus,
       "ruijieSyncStatsSlot": ruijieSyncStatsSlot,
       "ruijieSyncStatsConn": ruijieSyncStatsConn,
       "ruijieSyncStatsChannel": ruijieSyncStatsChannel,
       "ruijieSyncStatsIfIndex": ruijieSyncStatsIfIndex,
       "ruijieSyncStatsPortState": ruijieSyncStatsPortState,
       "ruijieSyncStatsRxFrames": ruijieSyncStatsRxFrames,
       "ruijieSyncStatsRxOctets": ruijieSyncStatsRxOctets,
       "ruijieSyncStatsRxReplenFails": ruijieSyncStatsRxReplenFails,
       "ruijieSyncStatsRxClockErrors": ruijieSyncStatsRxClockErrors,
       "ruijieSyncStatsRxDpllErrors": ruijieSyncStatsRxDpllErrors,
       "ruijieSyncStatsRxFrameTooLongErrors": ruijieSyncStatsRxFrameTooLongErrors,
       "ruijieSyncStatsRxFrameOctetAlignErrors": ruijieSyncStatsRxFrameOctetAlignErrors,
       "ruijieSyncStatsRxAbortErrors": ruijieSyncStatsRxAbortErrors,
       "ruijieSyncStatsRxCrcErrors": ruijieSyncStatsRxCrcErrors,
       "ruijieSyncStatsRxRcvrOverrunErrors": ruijieSyncStatsRxRcvrOverrunErrors,
       "ruijieSyncStatsTxFrames": ruijieSyncStatsTxFrames,
       "ruijieSyncStatsTxOctets": ruijieSyncStatsTxOctets,
       "ruijieSyncStatsTxRingFullDropsErrors": ruijieSyncStatsTxRingFullDropsErrors,
       "ruijieSyncStatsTxClockErrors": ruijieSyncStatsTxClockErrors,
       "ruijieSyncStatsTxFrameTooLongErrors": ruijieSyncStatsTxFrameTooLongErrors,
       "ruijieSyncStatsTxUnderrunErrors": ruijieSyncStatsTxUnderrunErrors,
       "ruijieSyncStatsMibConformance": ruijieSyncStatsMibConformance,
       "ruijieSyncStatsMibCompliances": ruijieSyncStatsMibCompliances,
       "ruijieSyncStatsMibCompliance": ruijieSyncStatsMibCompliance,
       "ruijieSyncStatsMibGroups": ruijieSyncStatsMibGroups,
       "ruijieSyncStatsGroup": ruijieSyncStatsGroup}
)
