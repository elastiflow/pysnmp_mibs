# SNMP MIB module (TIMETRA-DOT3-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-DOT3-OAM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:31 2025
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

(dot3OamEntry,
 dot3OamLoopbackEntry,
 dot3OamPeerEntry,
 dot3OamPeerMacAddress) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamEntry",
    "dot3OamLoopbackEntry",
    "dot3OamPeerEntry",
    "dot3OamPeerMacAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")


# MODULE-IDENTITY

timetraDOT3OAMMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 42)
)
if mibBuilder.loadTexts:
    timetraDOT3OAMMIBModule.setRevisions(
        ("2012-07-01 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "2006-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxDot3OamMIBConformance_ObjectIdentity = ObjectIdentity
tmnxDot3OamMIBConformance = _TmnxDot3OamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42)
)
_TmnxDot3OamMIBCompliances_ObjectIdentity = ObjectIdentity
tmnxDot3OamMIBCompliances = _TmnxDot3OamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1)
)
_TmnxDot3OamMIBGroups_ObjectIdentity = ObjectIdentity
tmnxDot3OamMIBGroups = _TmnxDot3OamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2)
)
_TmnxDot3OamObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamObjs = _TmnxDot3OamObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42)
)
_TmnxDot3OamEntryObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamEntryObjs = _TmnxDot3OamEntryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1)
)
_TmnxDot3OamTable_Object = MibTable
tmnxDot3OamTable = _TmnxDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamTable.setStatus("current")
_TmnxDot3OamEntry_Object = MibTableRow
tmnxDot3OamEntry = _TmnxDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamEntry.setStatus("current")
_TmnxDot3OamLastChanged_Type = TimeStamp
_TmnxDot3OamLastChanged_Object = MibTableColumn
tmnxDot3OamLastChanged = _TmnxDot3OamLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 1),
    _TmnxDot3OamLastChanged_Type()
)
tmnxDot3OamLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamLastChanged.setStatus("current")


class _TmnxDot3OamInterval_Type(Unsigned32):
    """Custom type tmnxDot3OamInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_TmnxDot3OamInterval_Type.__name__ = "Unsigned32"
_TmnxDot3OamInterval_Object = MibTableColumn
tmnxDot3OamInterval = _TmnxDot3OamInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 2),
    _TmnxDot3OamInterval_Type()
)
tmnxDot3OamInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamInterval.setUnits("100s of milliseconds")


class _TmnxDot3OamMultiplier_Type(Unsigned32):
    """Custom type tmnxDot3OamMultiplier based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_TmnxDot3OamMultiplier_Type.__name__ = "Unsigned32"
_TmnxDot3OamMultiplier_Object = MibTableColumn
tmnxDot3OamMultiplier = _TmnxDot3OamMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 3),
    _TmnxDot3OamMultiplier_Type()
)
tmnxDot3OamMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamMultiplier.setStatus("current")


class _TmnxDot3OamTunneling_Type(TruthValue):
    """Custom type tmnxDot3OamTunneling based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamTunneling_Type.__name__ = "TruthValue"
_TmnxDot3OamTunneling_Object = MibTableColumn
tmnxDot3OamTunneling = _TmnxDot3OamTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 4),
    _TmnxDot3OamTunneling_Type()
)
tmnxDot3OamTunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamTunneling.setStatus("current")


class _TmnxDot3OamLooped_Type(TruthValue):
    """Custom type tmnxDot3OamLooped based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamLooped_Type.__name__ = "TruthValue"
_TmnxDot3OamLooped_Object = MibTableColumn
tmnxDot3OamLooped = _TmnxDot3OamLooped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 5),
    _TmnxDot3OamLooped_Type()
)
tmnxDot3OamLooped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamLooped.setStatus("current")


class _TmnxDot3OamHoldTime_Type(Unsigned32):
    """Custom type tmnxDot3OamHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TmnxDot3OamHoldTime_Type.__name__ = "Unsigned32"
_TmnxDot3OamHoldTime_Object = MibTableColumn
tmnxDot3OamHoldTime = _TmnxDot3OamHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 6),
    _TmnxDot3OamHoldTime_Type()
)
tmnxDot3OamHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamHoldTime.setUnits("seconds")


class _TmnxDot3OamIgnoreEfmState_Type(TruthValue):
    """Custom type tmnxDot3OamIgnoreEfmState based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamIgnoreEfmState_Type.__name__ = "TruthValue"
_TmnxDot3OamIgnoreEfmState_Object = MibTableColumn
tmnxDot3OamIgnoreEfmState = _TmnxDot3OamIgnoreEfmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 7),
    _TmnxDot3OamIgnoreEfmState_Type()
)
tmnxDot3OamIgnoreEfmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamIgnoreEfmState.setStatus("current")


class _TmnxDot3OamGraceTxEnabled_Type(TruthValue):
    """Custom type tmnxDot3OamGraceTxEnabled based on TruthValue"""
    defaultValue = 1


_TmnxDot3OamGraceTxEnabled_Type.__name__ = "TruthValue"
_TmnxDot3OamGraceTxEnabled_Object = MibTableColumn
tmnxDot3OamGraceTxEnabled = _TmnxDot3OamGraceTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 8),
    _TmnxDot3OamGraceTxEnabled_Type()
)
tmnxDot3OamGraceTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamGraceTxEnabled.setStatus("current")
_TmnxDot3OamGraceTxState_Type = TruthValue
_TmnxDot3OamGraceTxState_Object = MibTableColumn
tmnxDot3OamGraceTxState = _TmnxDot3OamGraceTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 9),
    _TmnxDot3OamGraceTxState_Type()
)
tmnxDot3OamGraceTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamGraceTxState.setStatus("current")
_TmnxDot3OamLoopbackObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamLoopbackObjs = _TmnxDot3OamLoopbackObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2)
)
_TmnxDot3OamLoopbackTable_Object = MibTable
tmnxDot3OamLoopbackTable = _TmnxDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackTable.setStatus("current")
_TmnxDot3OamLoopbackEntry_Object = MibTableRow
tmnxDot3OamLoopbackEntry = _TmnxDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackEntry.setStatus("current")
_TmnxDot3OamLoopbackLastChanged_Type = TimeStamp
_TmnxDot3OamLoopbackLastChanged_Object = MibTableColumn
tmnxDot3OamLoopbackLastChanged = _TmnxDot3OamLoopbackLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1, 1),
    _TmnxDot3OamLoopbackLastChanged_Type()
)
tmnxDot3OamLoopbackLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackLastChanged.setStatus("current")


class _TmnxDot3OamLoopbackLocalStatus_Type(Integer32):
    """Custom type tmnxDot3OamLoopbackLocalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("localLoopback", 2))
    )


_TmnxDot3OamLoopbackLocalStatus_Type.__name__ = "Integer32"
_TmnxDot3OamLoopbackLocalStatus_Object = MibTableColumn
tmnxDot3OamLoopbackLocalStatus = _TmnxDot3OamLoopbackLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1, 2),
    _TmnxDot3OamLoopbackLocalStatus_Type()
)
tmnxDot3OamLoopbackLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackLocalStatus.setStatus("current")
_TmnxDot3OamGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamGlobalObjs = _TmnxDot3OamGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3)
)
_TmnxDot3OamSystemScalarsGroup_ObjectIdentity = ObjectIdentity
tmnxDot3OamSystemScalarsGroup = _TmnxDot3OamSystemScalarsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3, 1)
)


class _TmnxDot3OamSystemGraceTxEnable_Type(TruthValue):
    """Custom type tmnxDot3OamSystemGraceTxEnable based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamSystemGraceTxEnable_Type.__name__ = "TruthValue"
_TmnxDot3OamSystemGraceTxEnable_Object = MibScalar
tmnxDot3OamSystemGraceTxEnable = _TmnxDot3OamSystemGraceTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3, 1, 1),
    _TmnxDot3OamSystemGraceTxEnable_Type()
)
tmnxDot3OamSystemGraceTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamSystemGraceTxEnable.setStatus("current")
_TmnxDot3OamPeerTable_Object = MibTable
tmnxDot3OamPeerTable = _TmnxDot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 4)
)
if mibBuilder.loadTexts:
    tmnxDot3OamPeerTable.setStatus("current")
_TmnxDot3OamPeerEntry_Object = MibTableRow
tmnxDot3OamPeerEntry = _TmnxDot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamPeerEntry.setStatus("current")
_TmnxDot3OamPeerGraceRx_Type = TruthValue
_TmnxDot3OamPeerGraceRx_Object = MibTableColumn
tmnxDot3OamPeerGraceRx = _TmnxDot3OamPeerGraceRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 4, 1, 1),
    _TmnxDot3OamPeerGraceRx_Type()
)
tmnxDot3OamPeerGraceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamPeerGraceRx.setStatus("current")
_TmnxDot3OamNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDot3OamNotifyPrefix = _TmnxDot3OamNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42)
)
_TmnxDot3OamNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxDot3OamNotificationsPrefix = _TmnxDot3OamNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42)
)
_TmnxDot3OamNotifications_ObjectIdentity = ObjectIdentity
tmnxDot3OamNotifications = _TmnxDot3OamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0)
)
dot3OamEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamEntry")
)
tmnxDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamLoopbackEntry")
)
tmnxDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
dot3OamPeerEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamPeerEntry")
)
tmnxDot3OamPeerEntry.setIndexNames(*dot3OamPeerEntry.getIndexNames())

# Managed Objects groups

tmnxDot3OamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 1)
)
tmnxDot3OamGroup.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamInterval"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamMultiplier"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTunneling"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamGroup.setStatus("obsolete")

tmnxDot3OamLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 2)
)
tmnxDot3OamLoopbackGroup.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackLocalStatus"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackGroup.setStatus("current")

tmnxDot3OamV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 5)
)
tmnxDot3OamV6v0Group.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamInterval"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamMultiplier"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTunneling"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLooped"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamV6v0Group.setStatus("current")

tmnxDot3OamV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 6)
)
tmnxDot3OamV6v1Group.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamHoldTime")
)
if mibBuilder.loadTexts:
    tmnxDot3OamV6v1Group.setStatus("current")

tmnxDot3OamV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 7)
)
tmnxDot3OamV11v0Group.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamIgnoreEfmState")
)
if mibBuilder.loadTexts:
    tmnxDot3OamV11v0Group.setStatus("current")

tmnxDot3OamGraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 8)
)
tmnxDot3OamGraceGroup.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSystemGraceTxEnable"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceTxEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceTxState"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerGraceRx"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamGraceGroup.setStatus("current")


# Notification objects

tmnxDot3OamPeerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 1)
)
tmnxDot3OamPeerChanged.setObjects(
    ("DOT3-OAM-MIB", "dot3OamPeerMacAddress")
)
if mibBuilder.loadTexts:
    tmnxDot3OamPeerChanged.setStatus(
        "current"
    )

tmnxDot3OamLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 2)
)
tmnxDot3OamLoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopDetected.setStatus(
        "current"
    )

tmnxDot3OamLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 3)
)
tmnxDot3OamLoopCleared.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopCleared.setStatus(
        "current"
    )


# Notifications groups

tmnxDot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 3)
)
tmnxDot3OamNotificationGroup.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerChanged")
)
if mibBuilder.loadTexts:
    tmnxDot3OamNotificationGroup.setStatus(
        "obsolete"
    )

tmnxDot3OamNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 4)
)
tmnxDot3OamNotificationV6v0Group.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopDetected"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopCleared"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamNotificationV6v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDot3OamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 1)
)
tmnxDot3OamMIBCompliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBCompliance.setStatus(
        "obsolete"
    )

tmnxDot3OamMIBV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 2)
)
tmnxDot3OamMIBV6v0Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxDot3OamMIBV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 3)
)
tmnxDot3OamMIBV6v1Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v1Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxDot3OamMIBV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 4)
)
tmnxDot3OamMIBV11v0Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v1Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV11v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceGroup"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV11v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DOT3-OAM-MIB",
    **{"timetraDOT3OAMMIBModule": timetraDOT3OAMMIBModule,
       "tmnxDot3OamMIBConformance": tmnxDot3OamMIBConformance,
       "tmnxDot3OamMIBCompliances": tmnxDot3OamMIBCompliances,
       "tmnxDot3OamMIBCompliance": tmnxDot3OamMIBCompliance,
       "tmnxDot3OamMIBV6v0Compliance": tmnxDot3OamMIBV6v0Compliance,
       "tmnxDot3OamMIBV6v1Compliance": tmnxDot3OamMIBV6v1Compliance,
       "tmnxDot3OamMIBV11v0Compliance": tmnxDot3OamMIBV11v0Compliance,
       "tmnxDot3OamMIBGroups": tmnxDot3OamMIBGroups,
       "tmnxDot3OamGroup": tmnxDot3OamGroup,
       "tmnxDot3OamLoopbackGroup": tmnxDot3OamLoopbackGroup,
       "tmnxDot3OamNotificationGroup": tmnxDot3OamNotificationGroup,
       "tmnxDot3OamNotificationV6v0Group": tmnxDot3OamNotificationV6v0Group,
       "tmnxDot3OamV6v0Group": tmnxDot3OamV6v0Group,
       "tmnxDot3OamV6v1Group": tmnxDot3OamV6v1Group,
       "tmnxDot3OamV11v0Group": tmnxDot3OamV11v0Group,
       "tmnxDot3OamGraceGroup": tmnxDot3OamGraceGroup,
       "tmnxDot3OamObjs": tmnxDot3OamObjs,
       "tmnxDot3OamEntryObjs": tmnxDot3OamEntryObjs,
       "tmnxDot3OamTable": tmnxDot3OamTable,
       "tmnxDot3OamEntry": tmnxDot3OamEntry,
       "tmnxDot3OamLastChanged": tmnxDot3OamLastChanged,
       "tmnxDot3OamInterval": tmnxDot3OamInterval,
       "tmnxDot3OamMultiplier": tmnxDot3OamMultiplier,
       "tmnxDot3OamTunneling": tmnxDot3OamTunneling,
       "tmnxDot3OamLooped": tmnxDot3OamLooped,
       "tmnxDot3OamHoldTime": tmnxDot3OamHoldTime,
       "tmnxDot3OamIgnoreEfmState": tmnxDot3OamIgnoreEfmState,
       "tmnxDot3OamGraceTxEnabled": tmnxDot3OamGraceTxEnabled,
       "tmnxDot3OamGraceTxState": tmnxDot3OamGraceTxState,
       "tmnxDot3OamLoopbackObjs": tmnxDot3OamLoopbackObjs,
       "tmnxDot3OamLoopbackTable": tmnxDot3OamLoopbackTable,
       "tmnxDot3OamLoopbackEntry": tmnxDot3OamLoopbackEntry,
       "tmnxDot3OamLoopbackLastChanged": tmnxDot3OamLoopbackLastChanged,
       "tmnxDot3OamLoopbackLocalStatus": tmnxDot3OamLoopbackLocalStatus,
       "tmnxDot3OamGlobalObjs": tmnxDot3OamGlobalObjs,
       "tmnxDot3OamSystemScalarsGroup": tmnxDot3OamSystemScalarsGroup,
       "tmnxDot3OamSystemGraceTxEnable": tmnxDot3OamSystemGraceTxEnable,
       "tmnxDot3OamPeerTable": tmnxDot3OamPeerTable,
       "tmnxDot3OamPeerEntry": tmnxDot3OamPeerEntry,
       "tmnxDot3OamPeerGraceRx": tmnxDot3OamPeerGraceRx,
       "tmnxDot3OamNotifyPrefix": tmnxDot3OamNotifyPrefix,
       "tmnxDot3OamNotificationsPrefix": tmnxDot3OamNotificationsPrefix,
       "tmnxDot3OamNotifications": tmnxDot3OamNotifications,
       "tmnxDot3OamPeerChanged": tmnxDot3OamPeerChanged,
       "tmnxDot3OamLoopDetected": tmnxDot3OamLoopDetected,
       "tmnxDot3OamLoopCleared": tmnxDot3OamLoopCleared}
)
