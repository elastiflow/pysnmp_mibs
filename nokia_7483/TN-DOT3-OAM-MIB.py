# SNMP MIB module (TN-DOT3-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-DOT3-OAM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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
 dot3OamPeerMacAddress) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamEntry",
    "dot3OamLoopbackEntry",
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

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")


# MODULE-IDENTITY

tnDOT3OAMMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 42)
)
if mibBuilder.loadTexts:
    tnDOT3OAMMIBModule.setRevisions(
        ("1908-07-01 00:00",
         "1908-01-01 00:00",
         "2006-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDot3OamObjs_ObjectIdentity = ObjectIdentity
tnDot3OamObjs = _TnDot3OamObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42)
)
_TnDot3OamEntryObjs_ObjectIdentity = ObjectIdentity
tnDot3OamEntryObjs = _TnDot3OamEntryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1)
)
_TnDot3OamTable_Object = MibTable
tnDot3OamTable = _TnDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot3OamTable.setStatus("current")
_TnDot3OamEntry_Object = MibTableRow
tnDot3OamEntry = _TnDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot3OamEntry.setStatus("current")
_TnDot3OamLastChanged_Type = TimeStamp
_TnDot3OamLastChanged_Object = MibTableColumn
tnDot3OamLastChanged = _TnDot3OamLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1, 1),
    _TnDot3OamLastChanged_Type()
)
tnDot3OamLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot3OamLastChanged.setStatus("current")


class _TnDot3OamInterval_Type(Unsigned32):
    """Custom type tnDot3OamInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_TnDot3OamInterval_Type.__name__ = "Unsigned32"
_TnDot3OamInterval_Object = MibTableColumn
tnDot3OamInterval = _TnDot3OamInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1, 2),
    _TnDot3OamInterval_Type()
)
tnDot3OamInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot3OamInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnDot3OamInterval.setUnits("100s of milliseconds")


class _TnDot3OamMultiplier_Type(Unsigned32):
    """Custom type tnDot3OamMultiplier based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_TnDot3OamMultiplier_Type.__name__ = "Unsigned32"
_TnDot3OamMultiplier_Object = MibTableColumn
tnDot3OamMultiplier = _TnDot3OamMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1, 3),
    _TnDot3OamMultiplier_Type()
)
tnDot3OamMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot3OamMultiplier.setStatus("current")


class _TnDot3OamTunneling_Type(TruthValue):
    """Custom type tnDot3OamTunneling based on TruthValue"""
    defaultValue = 2


_TnDot3OamTunneling_Type.__name__ = "TruthValue"
_TnDot3OamTunneling_Object = MibTableColumn
tnDot3OamTunneling = _TnDot3OamTunneling_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1, 4),
    _TnDot3OamTunneling_Type()
)
tnDot3OamTunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot3OamTunneling.setStatus("current")


class _TnDot3OamLooped_Type(TruthValue):
    """Custom type tnDot3OamLooped based on TruthValue"""
    defaultValue = 2


_TnDot3OamLooped_Type.__name__ = "TruthValue"
_TnDot3OamLooped_Object = MibTableColumn
tnDot3OamLooped = _TnDot3OamLooped_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1, 5),
    _TnDot3OamLooped_Type()
)
tnDot3OamLooped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot3OamLooped.setStatus("current")


class _TnDot3OamHoldTime_Type(Unsigned32):
    """Custom type tnDot3OamHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TnDot3OamHoldTime_Type.__name__ = "Unsigned32"
_TnDot3OamHoldTime_Object = MibTableColumn
tnDot3OamHoldTime = _TnDot3OamHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 1, 1, 1, 6),
    _TnDot3OamHoldTime_Type()
)
tnDot3OamHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot3OamHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tnDot3OamHoldTime.setUnits("seconds")
_TnDot3OamLoopbackObjs_ObjectIdentity = ObjectIdentity
tnDot3OamLoopbackObjs = _TnDot3OamLoopbackObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 2)
)
_TnDot3OamLoopbackTable_Object = MibTable
tnDot3OamLoopbackTable = _TnDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 2, 1)
)
if mibBuilder.loadTexts:
    tnDot3OamLoopbackTable.setStatus("current")
_TnDot3OamLoopbackEntry_Object = MibTableRow
tnDot3OamLoopbackEntry = _TnDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot3OamLoopbackEntry.setStatus("current")
_TnDot3OamLoopbackLastChanged_Type = TimeStamp
_TnDot3OamLoopbackLastChanged_Object = MibTableColumn
tnDot3OamLoopbackLastChanged = _TnDot3OamLoopbackLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 2, 1, 1, 1),
    _TnDot3OamLoopbackLastChanged_Type()
)
tnDot3OamLoopbackLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot3OamLoopbackLastChanged.setStatus("current")


class _TnDot3OamLoopbackLocalStatus_Type(Integer32):
    """Custom type tnDot3OamLoopbackLocalStatus based on Integer32"""
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


_TnDot3OamLoopbackLocalStatus_Type.__name__ = "Integer32"
_TnDot3OamLoopbackLocalStatus_Object = MibTableColumn
tnDot3OamLoopbackLocalStatus = _TnDot3OamLoopbackLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 42, 2, 1, 1, 2),
    _TnDot3OamLoopbackLocalStatus_Type()
)
tnDot3OamLoopbackLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot3OamLoopbackLocalStatus.setStatus("current")
_TnDot3OamNotifyPrefix_ObjectIdentity = ObjectIdentity
tnDot3OamNotifyPrefix = _TnDot3OamNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 42)
)
_TnDot3OamNotificationsPrefix_ObjectIdentity = ObjectIdentity
tnDot3OamNotificationsPrefix = _TnDot3OamNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 42, 42)
)
_TnDot3OamNotifications_ObjectIdentity = ObjectIdentity
tnDot3OamNotifications = _TnDot3OamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 42, 42, 0)
)
dot3OamEntry.registerAugmentions(
    ("TN-DOT3-OAM-MIB",
     "tnDot3OamEntry")
)
tnDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions(
    ("TN-DOT3-OAM-MIB",
     "tnDot3OamLoopbackEntry")
)
tnDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tnDot3OamPeerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 42, 42, 0, 1)
)
tnDot3OamPeerChanged.setObjects(
    ("DOT3-OAM-MIB", "dot3OamPeerMacAddress")
)
if mibBuilder.loadTexts:
    tnDot3OamPeerChanged.setStatus(
        "current"
    )

tnDot3OamLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 42, 42, 0, 2)
)
tnDot3OamLoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    tnDot3OamLoopDetected.setStatus(
        "current"
    )

tnDot3OamLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 42, 42, 0, 3)
)
tnDot3OamLoopCleared.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    tnDot3OamLoopCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DOT3-OAM-MIB",
    **{"tnDOT3OAMMIBModule": tnDOT3OAMMIBModule,
       "tnDot3OamObjs": tnDot3OamObjs,
       "tnDot3OamEntryObjs": tnDot3OamEntryObjs,
       "tnDot3OamTable": tnDot3OamTable,
       "tnDot3OamEntry": tnDot3OamEntry,
       "tnDot3OamLastChanged": tnDot3OamLastChanged,
       "tnDot3OamInterval": tnDot3OamInterval,
       "tnDot3OamMultiplier": tnDot3OamMultiplier,
       "tnDot3OamTunneling": tnDot3OamTunneling,
       "tnDot3OamLooped": tnDot3OamLooped,
       "tnDot3OamHoldTime": tnDot3OamHoldTime,
       "tnDot3OamLoopbackObjs": tnDot3OamLoopbackObjs,
       "tnDot3OamLoopbackTable": tnDot3OamLoopbackTable,
       "tnDot3OamLoopbackEntry": tnDot3OamLoopbackEntry,
       "tnDot3OamLoopbackLastChanged": tnDot3OamLoopbackLastChanged,
       "tnDot3OamLoopbackLocalStatus": tnDot3OamLoopbackLocalStatus,
       "tnDot3OamNotifyPrefix": tnDot3OamNotifyPrefix,
       "tnDot3OamNotificationsPrefix": tnDot3OamNotificationsPrefix,
       "tnDot3OamNotifications": tnDot3OamNotifications,
       "tnDot3OamPeerChanged": tnDot3OamPeerChanged,
       "tnDot3OamLoopDetected": tnDot3OamLoopDetected,
       "tnDot3OamLoopCleared": tnDot3OamLoopCleared}
)
