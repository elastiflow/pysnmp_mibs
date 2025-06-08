# SNMP MIB module (EtherLike-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/EtherLike-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:46:41 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2,
 transmission) = mibBuilder.importSymbols(
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
    "mib-2",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etherMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 35)
)
if mibBuilder.loadTexts:
    etherMIB.setRevisions(
        ("2003-09-19 00:00",
         "1999-08-24 04:00",
         "1998-06-03 21:50",
         "1994-02-03 04:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7)
)
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("current")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("current")
_Dot3StatsIndex_Type = InterfaceIndex
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("current")
_Dot3StatsAlignmentErrors_Type = Counter32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("current")
_Dot3StatsFCSErrors_Type = Counter32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("current")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("current")
_Dot3StatsMultipleCollisionFrames_Type = Counter32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("current")
_Dot3StatsSQETestErrors_Type = Counter32
_Dot3StatsSQETestErrors_Object = MibTableColumn
dot3StatsSQETestErrors = _Dot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6),
    _Dot3StatsSQETestErrors_Type()
)
dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setStatus("current")
_Dot3StatsDeferredTransmissions_Type = Counter32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("current")
_Dot3StatsLateCollisions_Type = Counter32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("current")
_Dot3StatsExcessiveCollisions_Type = Counter32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("current")
_Dot3StatsInternalMacTransmitErrors_Type = Counter32
_Dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
dot3StatsInternalMacTransmitErrors = _Dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10),
    _Dot3StatsInternalMacTransmitErrors_Type()
)
dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setStatus("current")
_Dot3StatsCarrierSenseErrors_Type = Counter32
_Dot3StatsCarrierSenseErrors_Object = MibTableColumn
dot3StatsCarrierSenseErrors = _Dot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11),
    _Dot3StatsCarrierSenseErrors_Type()
)
dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setStatus("current")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("current")
_Dot3StatsInternalMacReceiveErrors_Type = Counter32
_Dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
dot3StatsInternalMacReceiveErrors = _Dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16),
    _Dot3StatsInternalMacReceiveErrors_Type()
)
dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setStatus("current")
_Dot3StatsEtherChipSet_Type = ObjectIdentifier
_Dot3StatsEtherChipSet_Object = MibTableColumn
dot3StatsEtherChipSet = _Dot3StatsEtherChipSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 17),
    _Dot3StatsEtherChipSet_Type()
)
dot3StatsEtherChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsEtherChipSet.setStatus("deprecated")
_Dot3StatsSymbolErrors_Type = Counter32
_Dot3StatsSymbolErrors_Object = MibTableColumn
dot3StatsSymbolErrors = _Dot3StatsSymbolErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 18),
    _Dot3StatsSymbolErrors_Type()
)
dot3StatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSymbolErrors.setStatus("current")


class _Dot3StatsDuplexStatus_Type(Integer32):
    """Custom type dot3StatsDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_Dot3StatsDuplexStatus_Type.__name__ = "Integer32"
_Dot3StatsDuplexStatus_Object = MibTableColumn
dot3StatsDuplexStatus = _Dot3StatsDuplexStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 19),
    _Dot3StatsDuplexStatus_Type()
)
dot3StatsDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDuplexStatus.setStatus("current")
_Dot3StatsRateControlAbility_Type = TruthValue
_Dot3StatsRateControlAbility_Object = MibTableColumn
dot3StatsRateControlAbility = _Dot3StatsRateControlAbility_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 20),
    _Dot3StatsRateControlAbility_Type()
)
dot3StatsRateControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsRateControlAbility.setStatus("current")


class _Dot3StatsRateControlStatus_Type(Integer32):
    """Custom type dot3StatsRateControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rateControlOff", 1),
          ("rateControlOn", 2),
          ("unknown", 3))
    )


_Dot3StatsRateControlStatus_Type.__name__ = "Integer32"
_Dot3StatsRateControlStatus_Object = MibTableColumn
dot3StatsRateControlStatus = _Dot3StatsRateControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 21),
    _Dot3StatsRateControlStatus_Type()
)
dot3StatsRateControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsRateControlStatus.setStatus("current")
_Dot3CollTable_Object = MibTable
dot3CollTable = _Dot3CollTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5)
)
if mibBuilder.loadTexts:
    dot3CollTable.setStatus("current")
_Dot3CollEntry_Object = MibTableRow
dot3CollEntry = _Dot3CollEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1)
)
dot3CollEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EtherLike-MIB", "dot3CollCount"),
)
if mibBuilder.loadTexts:
    dot3CollEntry.setStatus("current")


class _Dot3CollCount_Type(Integer32):
    """Custom type dot3CollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot3CollCount_Type.__name__ = "Integer32"
_Dot3CollCount_Object = MibTableColumn
dot3CollCount = _Dot3CollCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2),
    _Dot3CollCount_Type()
)
dot3CollCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3CollCount.setStatus("current")
_Dot3CollFrequencies_Type = Counter32
_Dot3CollFrequencies_Object = MibTableColumn
dot3CollFrequencies = _Dot3CollFrequencies_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3),
    _Dot3CollFrequencies_Type()
)
dot3CollFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollFrequencies.setStatus("current")
_Dot3Tests_ObjectIdentity = ObjectIdentity
dot3Tests = _Dot3Tests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6)
)
_Dot3TestTdr_ObjectIdentity = ObjectIdentity
dot3TestTdr = _Dot3TestTdr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 1)
)
if mibBuilder.loadTexts:
    dot3TestTdr.setStatus("deprecated")
_Dot3TestLoopBack_ObjectIdentity = ObjectIdentity
dot3TestLoopBack = _Dot3TestLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 2)
)
if mibBuilder.loadTexts:
    dot3TestLoopBack.setStatus("deprecated")
_Dot3Errors_ObjectIdentity = ObjectIdentity
dot3Errors = _Dot3Errors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7)
)
_Dot3ErrorInitError_ObjectIdentity = ObjectIdentity
dot3ErrorInitError = _Dot3ErrorInitError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 1)
)
if mibBuilder.loadTexts:
    dot3ErrorInitError.setStatus("deprecated")
_Dot3ErrorLoopbackError_ObjectIdentity = ObjectIdentity
dot3ErrorLoopbackError = _Dot3ErrorLoopbackError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 2)
)
if mibBuilder.loadTexts:
    dot3ErrorLoopbackError.setStatus("deprecated")
_Dot3ControlTable_Object = MibTable
dot3ControlTable = _Dot3ControlTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9)
)
if mibBuilder.loadTexts:
    dot3ControlTable.setStatus("current")
_Dot3ControlEntry_Object = MibTableRow
dot3ControlEntry = _Dot3ControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1)
)
dot3ControlEntry.setIndexNames(
    (0, "EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3ControlEntry.setStatus("current")


class _Dot3ControlFunctionsSupported_Type(Bits):
    """Custom type dot3ControlFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        ("pause", 0)
    )

_Dot3ControlFunctionsSupported_Type.__name__ = "Bits"
_Dot3ControlFunctionsSupported_Object = MibTableColumn
dot3ControlFunctionsSupported = _Dot3ControlFunctionsSupported_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 1),
    _Dot3ControlFunctionsSupported_Type()
)
dot3ControlFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlFunctionsSupported.setStatus("current")
_Dot3ControlInUnknownOpcodes_Type = Counter32
_Dot3ControlInUnknownOpcodes_Object = MibTableColumn
dot3ControlInUnknownOpcodes = _Dot3ControlInUnknownOpcodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 2),
    _Dot3ControlInUnknownOpcodes_Type()
)
dot3ControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ControlInUnknownOpcodes.setStatus("current")
_Dot3HCControlInUnknownOpcodes_Type = Counter64
_Dot3HCControlInUnknownOpcodes_Object = MibTableColumn
dot3HCControlInUnknownOpcodes = _Dot3HCControlInUnknownOpcodes_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 3),
    _Dot3HCControlInUnknownOpcodes_Type()
)
dot3HCControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCControlInUnknownOpcodes.setStatus("current")
_Dot3PauseTable_Object = MibTable
dot3PauseTable = _Dot3PauseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10)
)
if mibBuilder.loadTexts:
    dot3PauseTable.setStatus("current")
_Dot3PauseEntry_Object = MibTableRow
dot3PauseEntry = _Dot3PauseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1)
)
dot3PauseEntry.setIndexNames(
    (0, "EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3PauseEntry.setStatus("current")


class _Dot3PauseAdminMode_Type(Integer32):
    """Custom type dot3PauseAdminMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseAdminMode_Type.__name__ = "Integer32"
_Dot3PauseAdminMode_Object = MibTableColumn
dot3PauseAdminMode = _Dot3PauseAdminMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 1),
    _Dot3PauseAdminMode_Type()
)
dot3PauseAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3PauseAdminMode.setStatus("current")


class _Dot3PauseOperMode_Type(Integer32):
    """Custom type dot3PauseOperMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_Dot3PauseOperMode_Type.__name__ = "Integer32"
_Dot3PauseOperMode_Object = MibTableColumn
dot3PauseOperMode = _Dot3PauseOperMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 2),
    _Dot3PauseOperMode_Type()
)
dot3PauseOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3PauseOperMode.setStatus("current")
_Dot3InPauseFrames_Type = Counter32
_Dot3InPauseFrames_Object = MibTableColumn
dot3InPauseFrames = _Dot3InPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 3),
    _Dot3InPauseFrames_Type()
)
dot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3InPauseFrames.setStatus("current")
_Dot3OutPauseFrames_Type = Counter32
_Dot3OutPauseFrames_Object = MibTableColumn
dot3OutPauseFrames = _Dot3OutPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 4),
    _Dot3OutPauseFrames_Type()
)
dot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OutPauseFrames.setStatus("current")
_Dot3HCInPauseFrames_Type = Counter64
_Dot3HCInPauseFrames_Object = MibTableColumn
dot3HCInPauseFrames = _Dot3HCInPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 5),
    _Dot3HCInPauseFrames_Type()
)
dot3HCInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCInPauseFrames.setStatus("current")
_Dot3HCOutPauseFrames_Type = Counter64
_Dot3HCOutPauseFrames_Object = MibTableColumn
dot3HCOutPauseFrames = _Dot3HCOutPauseFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 6),
    _Dot3HCOutPauseFrames_Type()
)
dot3HCOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCOutPauseFrames.setStatus("current")
_Dot3HCStatsTable_Object = MibTable
dot3HCStatsTable = _Dot3HCStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11)
)
if mibBuilder.loadTexts:
    dot3HCStatsTable.setStatus("current")
_Dot3HCStatsEntry_Object = MibTableRow
dot3HCStatsEntry = _Dot3HCStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1)
)
dot3HCStatsEntry.setIndexNames(
    (0, "EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3HCStatsEntry.setStatus("current")
_Dot3HCStatsAlignmentErrors_Type = Counter64
_Dot3HCStatsAlignmentErrors_Object = MibTableColumn
dot3HCStatsAlignmentErrors = _Dot3HCStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 1),
    _Dot3HCStatsAlignmentErrors_Type()
)
dot3HCStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsAlignmentErrors.setStatus("current")
_Dot3HCStatsFCSErrors_Type = Counter64
_Dot3HCStatsFCSErrors_Object = MibTableColumn
dot3HCStatsFCSErrors = _Dot3HCStatsFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 2),
    _Dot3HCStatsFCSErrors_Type()
)
dot3HCStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsFCSErrors.setStatus("current")
_Dot3HCStatsInternalMacTransmitErrors_Type = Counter64
_Dot3HCStatsInternalMacTransmitErrors_Object = MibTableColumn
dot3HCStatsInternalMacTransmitErrors = _Dot3HCStatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 3),
    _Dot3HCStatsInternalMacTransmitErrors_Type()
)
dot3HCStatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsInternalMacTransmitErrors.setStatus("current")
_Dot3HCStatsFrameTooLongs_Type = Counter64
_Dot3HCStatsFrameTooLongs_Object = MibTableColumn
dot3HCStatsFrameTooLongs = _Dot3HCStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 4),
    _Dot3HCStatsFrameTooLongs_Type()
)
dot3HCStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsFrameTooLongs.setStatus("current")
_Dot3HCStatsInternalMacReceiveErrors_Type = Counter64
_Dot3HCStatsInternalMacReceiveErrors_Object = MibTableColumn
dot3HCStatsInternalMacReceiveErrors = _Dot3HCStatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 5),
    _Dot3HCStatsInternalMacReceiveErrors_Type()
)
dot3HCStatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsInternalMacReceiveErrors.setStatus("current")
_Dot3HCStatsSymbolErrors_Type = Counter64
_Dot3HCStatsSymbolErrors_Object = MibTableColumn
dot3HCStatsSymbolErrors = _Dot3HCStatsSymbolErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 6),
    _Dot3HCStatsSymbolErrors_Type()
)
dot3HCStatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3HCStatsSymbolErrors.setStatus("current")
_EtherMIBObjects_ObjectIdentity = ObjectIdentity
etherMIBObjects = _EtherMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 1)
)
_EtherConformance_ObjectIdentity = ObjectIdentity
etherConformance = _EtherConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2)
)
_EtherGroups_ObjectIdentity = ObjectIdentity
etherGroups = _EtherGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2, 1)
)
_EtherCompliances_ObjectIdentity = ObjectIdentity
etherCompliances = _EtherCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 35, 2, 2)
)

# Managed Objects groups

etherStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 1)
)
etherStatsGroup.setObjects(
      *(("EtherLike-MIB", "dot3StatsIndex"),
        ("EtherLike-MIB", "dot3StatsAlignmentErrors"),
        ("EtherLike-MIB", "dot3StatsFCSErrors"),
        ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsSQETestErrors"),
        ("EtherLike-MIB", "dot3StatsDeferredTransmissions"),
        ("EtherLike-MIB", "dot3StatsLateCollisions"),
        ("EtherLike-MIB", "dot3StatsExcessiveCollisions"),
        ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"),
        ("EtherLike-MIB", "dot3StatsFrameTooLongs"),
        ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("EtherLike-MIB", "dot3StatsEtherChipSet"))
)
if mibBuilder.loadTexts:
    etherStatsGroup.setStatus("deprecated")

etherCollisionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 2)
)
etherCollisionTableGroup.setObjects(
    ("EtherLike-MIB", "dot3CollFrequencies")
)
if mibBuilder.loadTexts:
    etherCollisionTableGroup.setStatus("current")

etherStats100MbsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 3)
)
etherStats100MbsGroup.setObjects(
      *(("EtherLike-MIB", "dot3StatsIndex"),
        ("EtherLike-MIB", "dot3StatsAlignmentErrors"),
        ("EtherLike-MIB", "dot3StatsFCSErrors"),
        ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsDeferredTransmissions"),
        ("EtherLike-MIB", "dot3StatsLateCollisions"),
        ("EtherLike-MIB", "dot3StatsExcessiveCollisions"),
        ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"),
        ("EtherLike-MIB", "dot3StatsFrameTooLongs"),
        ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"),
        ("EtherLike-MIB", "dot3StatsEtherChipSet"),
        ("EtherLike-MIB", "dot3StatsSymbolErrors"))
)
if mibBuilder.loadTexts:
    etherStats100MbsGroup.setStatus("deprecated")

etherStatsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 4)
)
etherStatsBaseGroup.setObjects(
      *(("EtherLike-MIB", "dot3StatsIndex"),
        ("EtherLike-MIB", "dot3StatsAlignmentErrors"),
        ("EtherLike-MIB", "dot3StatsFCSErrors"),
        ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsDeferredTransmissions"),
        ("EtherLike-MIB", "dot3StatsLateCollisions"),
        ("EtherLike-MIB", "dot3StatsExcessiveCollisions"),
        ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"),
        ("EtherLike-MIB", "dot3StatsFrameTooLongs"),
        ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"))
)
if mibBuilder.loadTexts:
    etherStatsBaseGroup.setStatus("deprecated")

etherStatsLowSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 5)
)
etherStatsLowSpeedGroup.setObjects(
    ("EtherLike-MIB", "dot3StatsSQETestErrors")
)
if mibBuilder.loadTexts:
    etherStatsLowSpeedGroup.setStatus("current")

etherStatsHighSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 6)
)
etherStatsHighSpeedGroup.setObjects(
    ("EtherLike-MIB", "dot3StatsSymbolErrors")
)
if mibBuilder.loadTexts:
    etherStatsHighSpeedGroup.setStatus("current")

etherDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 7)
)
etherDuplexGroup.setObjects(
    ("EtherLike-MIB", "dot3StatsDuplexStatus")
)
if mibBuilder.loadTexts:
    etherDuplexGroup.setStatus("current")

etherControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 8)
)
etherControlGroup.setObjects(
      *(("EtherLike-MIB", "dot3ControlFunctionsSupported"),
        ("EtherLike-MIB", "dot3ControlInUnknownOpcodes"))
)
if mibBuilder.loadTexts:
    etherControlGroup.setStatus("current")

etherControlPauseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 9)
)
etherControlPauseGroup.setObjects(
      *(("EtherLike-MIB", "dot3PauseAdminMode"),
        ("EtherLike-MIB", "dot3PauseOperMode"),
        ("EtherLike-MIB", "dot3InPauseFrames"),
        ("EtherLike-MIB", "dot3OutPauseFrames"))
)
if mibBuilder.loadTexts:
    etherControlPauseGroup.setStatus("current")

etherStatsBaseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 10)
)
etherStatsBaseGroup2.setObjects(
      *(("EtherLike-MIB", "dot3StatsIndex"),
        ("EtherLike-MIB", "dot3StatsAlignmentErrors"),
        ("EtherLike-MIB", "dot3StatsFCSErrors"),
        ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"),
        ("EtherLike-MIB", "dot3StatsFrameTooLongs"),
        ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"))
)
if mibBuilder.loadTexts:
    etherStatsBaseGroup2.setStatus("current")

etherStatsHalfDuplexGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 11)
)
etherStatsHalfDuplexGroup.setObjects(
      *(("EtherLike-MIB", "dot3StatsSingleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"),
        ("EtherLike-MIB", "dot3StatsDeferredTransmissions"),
        ("EtherLike-MIB", "dot3StatsLateCollisions"),
        ("EtherLike-MIB", "dot3StatsExcessiveCollisions"),
        ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"))
)
if mibBuilder.loadTexts:
    etherStatsHalfDuplexGroup.setStatus("current")

etherHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 12)
)
etherHCStatsGroup.setObjects(
      *(("EtherLike-MIB", "dot3HCStatsAlignmentErrors"),
        ("EtherLike-MIB", "dot3HCStatsFCSErrors"),
        ("EtherLike-MIB", "dot3HCStatsInternalMacTransmitErrors"),
        ("EtherLike-MIB", "dot3HCStatsFrameTooLongs"),
        ("EtherLike-MIB", "dot3HCStatsInternalMacReceiveErrors"),
        ("EtherLike-MIB", "dot3HCStatsSymbolErrors"))
)
if mibBuilder.loadTexts:
    etherHCStatsGroup.setStatus("current")

etherHCControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 13)
)
etherHCControlGroup.setObjects(
    ("EtherLike-MIB", "dot3HCControlInUnknownOpcodes")
)
if mibBuilder.loadTexts:
    etherHCControlGroup.setStatus("current")

etherHCControlPauseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 14)
)
etherHCControlPauseGroup.setObjects(
      *(("EtherLike-MIB", "dot3HCInPauseFrames"),
        ("EtherLike-MIB", "dot3HCOutPauseFrames"))
)
if mibBuilder.loadTexts:
    etherHCControlPauseGroup.setStatus("current")

etherRateControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 35, 2, 1, 15)
)
etherRateControlGroup.setObjects(
      *(("EtherLike-MIB", "dot3StatsRateControlAbility"),
        ("EtherLike-MIB", "dot3StatsRateControlStatus"))
)
if mibBuilder.loadTexts:
    etherRateControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etherCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 1)
)
etherCompliance.setObjects(
      *(("EtherLike-MIB", "etherStatsGroup"),
        ("EtherLike-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    etherCompliance.setStatus(
        "deprecated"
    )

ether100MbsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 2)
)
ether100MbsCompliance.setObjects(
      *(("EtherLike-MIB", "etherStats100MbsGroup"),
        ("EtherLike-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    ether100MbsCompliance.setStatus(
        "deprecated"
    )

dot3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 3)
)
dot3Compliance.setObjects(
      *(("EtherLike-MIB", "etherStatsBaseGroup"),
        ("EtherLike-MIB", "etherDuplexGroup"),
        ("EtherLike-MIB", "etherStatsLowSpeedGroup"),
        ("EtherLike-MIB", "etherStatsHighSpeedGroup"),
        ("EtherLike-MIB", "etherControlGroup"),
        ("EtherLike-MIB", "etherControlPauseGroup"),
        ("EtherLike-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    dot3Compliance.setStatus(
        "deprecated"
    )

dot3Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 35, 2, 2, 4)
)
dot3Compliance2.setObjects(
      *(("EtherLike-MIB", "etherStatsBaseGroup2"),
        ("EtherLike-MIB", "etherDuplexGroup"),
        ("EtherLike-MIB", "etherRateControlGroup"),
        ("EtherLike-MIB", "etherStatsLowSpeedGroup"),
        ("EtherLike-MIB", "etherStatsHighSpeedGroup"),
        ("EtherLike-MIB", "etherStatsHalfDuplexGroup"),
        ("EtherLike-MIB", "etherHCStatsGroup"),
        ("EtherLike-MIB", "etherControlGroup"),
        ("EtherLike-MIB", "etherHCControlGroup"),
        ("EtherLike-MIB", "etherControlPauseGroup"),
        ("EtherLike-MIB", "etherHCControlPauseGroup"),
        ("EtherLike-MIB", "etherCollisionTableGroup"))
)
if mibBuilder.loadTexts:
    dot3Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EtherLike-MIB",
    **{"dot3": dot3,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsSQETestErrors": dot3StatsSQETestErrors,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsInternalMacTransmitErrors": dot3StatsInternalMacTransmitErrors,
       "dot3StatsCarrierSenseErrors": dot3StatsCarrierSenseErrors,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsInternalMacReceiveErrors": dot3StatsInternalMacReceiveErrors,
       "dot3StatsEtherChipSet": dot3StatsEtherChipSet,
       "dot3StatsSymbolErrors": dot3StatsSymbolErrors,
       "dot3StatsDuplexStatus": dot3StatsDuplexStatus,
       "dot3StatsRateControlAbility": dot3StatsRateControlAbility,
       "dot3StatsRateControlStatus": dot3StatsRateControlStatus,
       "dot3CollTable": dot3CollTable,
       "dot3CollEntry": dot3CollEntry,
       "dot3CollCount": dot3CollCount,
       "dot3CollFrequencies": dot3CollFrequencies,
       "dot3Tests": dot3Tests,
       "dot3TestTdr": dot3TestTdr,
       "dot3TestLoopBack": dot3TestLoopBack,
       "dot3Errors": dot3Errors,
       "dot3ErrorInitError": dot3ErrorInitError,
       "dot3ErrorLoopbackError": dot3ErrorLoopbackError,
       "dot3ControlTable": dot3ControlTable,
       "dot3ControlEntry": dot3ControlEntry,
       "dot3ControlFunctionsSupported": dot3ControlFunctionsSupported,
       "dot3ControlInUnknownOpcodes": dot3ControlInUnknownOpcodes,
       "dot3HCControlInUnknownOpcodes": dot3HCControlInUnknownOpcodes,
       "dot3PauseTable": dot3PauseTable,
       "dot3PauseEntry": dot3PauseEntry,
       "dot3PauseAdminMode": dot3PauseAdminMode,
       "dot3PauseOperMode": dot3PauseOperMode,
       "dot3InPauseFrames": dot3InPauseFrames,
       "dot3OutPauseFrames": dot3OutPauseFrames,
       "dot3HCInPauseFrames": dot3HCInPauseFrames,
       "dot3HCOutPauseFrames": dot3HCOutPauseFrames,
       "dot3HCStatsTable": dot3HCStatsTable,
       "dot3HCStatsEntry": dot3HCStatsEntry,
       "dot3HCStatsAlignmentErrors": dot3HCStatsAlignmentErrors,
       "dot3HCStatsFCSErrors": dot3HCStatsFCSErrors,
       "dot3HCStatsInternalMacTransmitErrors": dot3HCStatsInternalMacTransmitErrors,
       "dot3HCStatsFrameTooLongs": dot3HCStatsFrameTooLongs,
       "dot3HCStatsInternalMacReceiveErrors": dot3HCStatsInternalMacReceiveErrors,
       "dot3HCStatsSymbolErrors": dot3HCStatsSymbolErrors,
       "etherMIB": etherMIB,
       "etherMIBObjects": etherMIBObjects,
       "etherConformance": etherConformance,
       "etherGroups": etherGroups,
       "etherStatsGroup": etherStatsGroup,
       "etherCollisionTableGroup": etherCollisionTableGroup,
       "etherStats100MbsGroup": etherStats100MbsGroup,
       "etherStatsBaseGroup": etherStatsBaseGroup,
       "etherStatsLowSpeedGroup": etherStatsLowSpeedGroup,
       "etherStatsHighSpeedGroup": etherStatsHighSpeedGroup,
       "etherDuplexGroup": etherDuplexGroup,
       "etherControlGroup": etherControlGroup,
       "etherControlPauseGroup": etherControlPauseGroup,
       "etherStatsBaseGroup2": etherStatsBaseGroup2,
       "etherStatsHalfDuplexGroup": etherStatsHalfDuplexGroup,
       "etherHCStatsGroup": etherHCStatsGroup,
       "etherHCControlGroup": etherHCControlGroup,
       "etherHCControlPauseGroup": etherHCControlPauseGroup,
       "etherRateControlGroup": etherRateControlGroup,
       "etherCompliances": etherCompliances,
       "etherCompliance": etherCompliance,
       "ether100MbsCompliance": ether100MbsCompliance,
       "dot3Compliance": dot3Compliance,
       "dot3Compliance2": dot3Compliance2}
)
