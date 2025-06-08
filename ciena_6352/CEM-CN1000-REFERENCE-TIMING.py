# SNMP MIB module (CEM-CN1000-REFERENCE-TIMING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-REFERENCE-TIMING.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

cemCN1000ReferenceTiming = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 9)
)
if mibBuilder.loadTexts:
    cemCN1000ReferenceTiming.setRevisions(
        ("2002-09-05 14:39",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrimaryReference_Type = InterfaceIndex
_PrimaryReference_Object = MibScalar
primaryReference = _PrimaryReference_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 1),
    _PrimaryReference_Type()
)
primaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryReference.setStatus("current")
_SecondaryReference_Type = InterfaceIndex
_SecondaryReference_Object = MibScalar
secondaryReference = _SecondaryReference_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 2),
    _SecondaryReference_Type()
)
secondaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryReference.setStatus("current")


class _ForcedReference_Type(Integer32):
    """Custom type forcedReference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("primary", 1),
          ("secondary", 2),
          ("freerun", 3),
          ("error", 4))
    )


_ForcedReference_Type.__name__ = "Integer32"
_ForcedReference_Object = MibScalar
forcedReference = _ForcedReference_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 3),
    _ForcedReference_Type()
)
forcedReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcedReference.setStatus("current")


class _ReversionEnable_Type(Integer32):
    """Custom type reversionEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ReversionEnable_Type.__name__ = "Integer32"
_ReversionEnable_Object = MibScalar
reversionEnable = _ReversionEnable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 4),
    _ReversionEnable_Type()
)
reversionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reversionEnable.setStatus("current")


class _CurrentReference_Type(Integer32):
    """Custom type currentReference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 0),
          ("primary", 1),
          ("secondary", 2),
          ("holdover", 3),
          ("noreference", 4),
          ("error", 5))
    )


_CurrentReference_Type.__name__ = "Integer32"
_CurrentReference_Object = MibScalar
currentReference = _CurrentReference_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 5),
    _CurrentReference_Type()
)
currentReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentReference.setStatus("current")


class _SysTimingState_Type(Integer32):
    """Custom type sysTimingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 0),
          ("normal", 1),
          ("holdover", 2),
          ("fastlock", 3),
          ("noactivepll", 4),
          ("error", 5))
    )


_SysTimingState_Type.__name__ = "Integer32"
_SysTimingState_Object = MibScalar
sysTimingState = _SysTimingState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 6),
    _SysTimingState_Type()
)
sysTimingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimingState.setStatus("current")
_ActiveTimingCard_Type = PhysicalIndex
_ActiveTimingCard_Object = MibScalar
activeTimingCard = _ActiveTimingCard_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 7),
    _ActiveTimingCard_Type()
)
activeTimingCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTimingCard.setStatus("current")


class _ForcedReferenceReporting_Type(Integer32):
    """Custom type forcedReferenceReporting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("minorAlarm", 1))
    )


_ForcedReferenceReporting_Type.__name__ = "Integer32"
_ForcedReferenceReporting_Object = MibScalar
forcedReferenceReporting = _ForcedReferenceReporting_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 8),
    _ForcedReferenceReporting_Type()
)
forcedReferenceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcedReferenceReporting.setStatus("current")


class _ReferenceLockoutReporting_Type(Integer32):
    """Custom type referenceLockoutReporting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("minorAlarm", 1))
    )


_ReferenceLockoutReporting_Type.__name__ = "Integer32"
_ReferenceLockoutReporting_Object = MibScalar
referenceLockoutReporting = _ReferenceLockoutReporting_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 9),
    _ReferenceLockoutReporting_Type()
)
referenceLockoutReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    referenceLockoutReporting.setStatus("current")


class _StratumLevel_Type(Integer32):
    """Custom type stratumLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("stratum1", 1),
          ("syncedTraceabilityUnknown", 2),
          ("stratum2", 3),
          ("transitNodeClock", 4),
          ("stratum3E", 5),
          ("stratum3", 6),
          ("sonetMinimumClock", 7),
          ("stratum4", 8),
          ("dontUseForSync", 9),
          ("reservedForNetworkSyncUse", 10))
    )


_StratumLevel_Type.__name__ = "Integer32"
_StratumLevel_Object = MibScalar
stratumLevel = _StratumLevel_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 10),
    _StratumLevel_Type()
)
stratumLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stratumLevel.setStatus("current")


class _PrimaryReferenceState_Type(Integer32):
    """Custom type primaryReferenceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 0),
          ("readyPending", 1),
          ("ready", 2),
          ("error", 3))
    )


_PrimaryReferenceState_Type.__name__ = "Integer32"
_PrimaryReferenceState_Object = MibScalar
primaryReferenceState = _PrimaryReferenceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 11),
    _PrimaryReferenceState_Type()
)
primaryReferenceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryReferenceState.setStatus("current")


class _SecondaryReferenceState_Type(Integer32):
    """Custom type secondaryReferenceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 0),
          ("readyPending", 1),
          ("ready", 2),
          ("error", 3))
    )


_SecondaryReferenceState_Type.__name__ = "Integer32"
_SecondaryReferenceState_Object = MibScalar
secondaryReferenceState = _SecondaryReferenceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 12),
    _SecondaryReferenceState_Type()
)
secondaryReferenceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryReferenceState.setStatus("current")


class _PrimaryReferenceLockout_Type(Integer32):
    """Custom type primaryReferenceLockout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PrimaryReferenceLockout_Type.__name__ = "Integer32"
_PrimaryReferenceLockout_Object = MibScalar
primaryReferenceLockout = _PrimaryReferenceLockout_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 13),
    _PrimaryReferenceLockout_Type()
)
primaryReferenceLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryReferenceLockout.setStatus("current")


class _SecondaryReferenceLockout_Type(Integer32):
    """Custom type secondaryReferenceLockout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SecondaryReferenceLockout_Type.__name__ = "Integer32"
_SecondaryReferenceLockout_Object = MibScalar
secondaryReferenceLockout = _SecondaryReferenceLockout_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 14),
    _SecondaryReferenceLockout_Type()
)
secondaryReferenceLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryReferenceLockout.setStatus("current")


class _SyncStatusReporting_Type(Integer32):
    """Custom type syncStatusReporting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("minorAlarm", 1))
    )


_SyncStatusReporting_Type.__name__ = "Integer32"
_SyncStatusReporting_Object = MibScalar
syncStatusReporting = _SyncStatusReporting_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 15),
    _SyncStatusReporting_Type()
)
syncStatusReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncStatusReporting.setStatus("current")


class _AlarmReporting_Type(Integer32):
    """Custom type alarmReporting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AlarmReporting_Type.__name__ = "Integer32"
_AlarmReporting_Object = MibScalar
alarmReporting = _AlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 16),
    _AlarmReporting_Type()
)
alarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmReporting.setStatus("current")
_LastSwitchTime_Type = TimeTicks
_LastSwitchTime_Object = MibScalar
lastSwitchTime = _LastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 17),
    _LastSwitchTime_Type()
)
lastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSwitchTime.setStatus("current")


class _TimingMode_Type(Integer32):
    """Custom type timingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 0),
          ("line", 1))
    )


_TimingMode_Type.__name__ = "Integer32"
_TimingMode_Object = MibScalar
timingMode = _TimingMode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 18),
    _TimingMode_Type()
)
timingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timingMode.setStatus("current")
_CemOC3PortTimingTable_Object = MibTable
cemOC3PortTimingTable = _CemOC3PortTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 19)
)
if mibBuilder.loadTexts:
    cemOC3PortTimingTable.setStatus("current")
_CemOC3PortTimingEntry_Object = MibTableRow
cemOC3PortTimingEntry = _CemOC3PortTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 19, 1)
)
cemOC3PortTimingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cemOC3PortTimingEntry.setStatus("current")


class _ForcedDUS_Type(Integer32):
    """Custom type forcedDUS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ForcedDUS_Type.__name__ = "Integer32"
_ForcedDUS_Object = MibTableColumn
forcedDUS = _ForcedDUS_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 19, 1, 1),
    _ForcedDUS_Type()
)
forcedDUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcedDUS.setStatus("current")


class _RxS1Byte_Type(Integer32):
    """Custom type rxS1Byte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RxS1Byte_Type.__name__ = "Integer32"
_RxS1Byte_Object = MibTableColumn
rxS1Byte = _RxS1Byte_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 19, 1, 2),
    _RxS1Byte_Type()
)
rxS1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxS1Byte.setStatus("current")
_CemTimingOperations_ObjectIdentity = ObjectIdentity
cemTimingOperations = _CemTimingOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 9, 21)
)


class _TimingReset_Type(Integer32):
    """Custom type timingReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TimingReset_Type.__name__ = "Integer32"
_TimingReset_Object = MibScalar
timingReset = _TimingReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 9, 21, 1),
    _TimingReset_Type()
)
timingReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timingReset.setStatus("current")

# Managed Objects groups

cemCN1000ReferenceTimingObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 9, 20)
)
cemCN1000ReferenceTimingObjects.setObjects(
      *(("CEM-CN1000-REFERENCE-TIMING", "primaryReference"),
        ("CEM-CN1000-REFERENCE-TIMING", "secondaryReference"),
        ("CEM-CN1000-REFERENCE-TIMING", "forcedReference"),
        ("CEM-CN1000-REFERENCE-TIMING", "reversionEnable"),
        ("CEM-CN1000-REFERENCE-TIMING", "currentReference"),
        ("CEM-CN1000-REFERENCE-TIMING", "sysTimingState"),
        ("CEM-CN1000-REFERENCE-TIMING", "activeTimingCard"),
        ("CEM-CN1000-REFERENCE-TIMING", "forcedReferenceReporting"),
        ("CEM-CN1000-REFERENCE-TIMING", "referenceLockoutReporting"),
        ("CEM-CN1000-REFERENCE-TIMING", "stratumLevel"),
        ("CEM-CN1000-REFERENCE-TIMING", "primaryReferenceState"),
        ("CEM-CN1000-REFERENCE-TIMING", "secondaryReferenceState"),
        ("CEM-CN1000-REFERENCE-TIMING", "primaryReferenceLockout"),
        ("CEM-CN1000-REFERENCE-TIMING", "secondaryReferenceLockout"),
        ("CEM-CN1000-REFERENCE-TIMING", "syncStatusReporting"),
        ("CEM-CN1000-REFERENCE-TIMING", "alarmReporting"),
        ("CEM-CN1000-REFERENCE-TIMING", "lastSwitchTime"),
        ("CEM-CN1000-REFERENCE-TIMING", "timingMode"),
        ("CEM-CN1000-REFERENCE-TIMING", "forcedDUS"),
        ("CEM-CN1000-REFERENCE-TIMING", "rxS1Byte"))
)
if mibBuilder.loadTexts:
    cemCN1000ReferenceTimingObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-REFERENCE-TIMING",
    **{"cemCN1000ReferenceTiming": cemCN1000ReferenceTiming,
       "primaryReference": primaryReference,
       "secondaryReference": secondaryReference,
       "forcedReference": forcedReference,
       "reversionEnable": reversionEnable,
       "currentReference": currentReference,
       "sysTimingState": sysTimingState,
       "activeTimingCard": activeTimingCard,
       "forcedReferenceReporting": forcedReferenceReporting,
       "referenceLockoutReporting": referenceLockoutReporting,
       "stratumLevel": stratumLevel,
       "primaryReferenceState": primaryReferenceState,
       "secondaryReferenceState": secondaryReferenceState,
       "primaryReferenceLockout": primaryReferenceLockout,
       "secondaryReferenceLockout": secondaryReferenceLockout,
       "syncStatusReporting": syncStatusReporting,
       "alarmReporting": alarmReporting,
       "lastSwitchTime": lastSwitchTime,
       "timingMode": timingMode,
       "cemOC3PortTimingTable": cemOC3PortTimingTable,
       "cemOC3PortTimingEntry": cemOC3PortTimingEntry,
       "forcedDUS": forcedDUS,
       "rxS1Byte": rxS1Byte,
       "cemCN1000ReferenceTimingObjects": cemCN1000ReferenceTimingObjects,
       "cemTimingOperations": cemTimingOperations,
       "timingReset": timingReset}
)
