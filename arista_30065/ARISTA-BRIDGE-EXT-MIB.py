# SNMP MIB module (ARISTA-BRIDGE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-BRIDGE-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:35 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(dot1qFdbId,
 dot1qTpFdbAddress,
 dot1qTpFdbPort) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qFdbId",
    "dot1qTpFdbAddress",
    "dot1qTpFdbPort")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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

aristaBridgeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2)
)
if mibBuilder.loadTexts:
    aristaBridgeExtMIB.setRevisions(
        ("2020-09-29 00:00",
         "2019-09-15 00:00",
         "2014-08-15 00:00",
         "2011-03-31 13:00",
         "2010-05-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaBridgeExtNotifications_ObjectIdentity = ObjectIdentity
aristaBridgeExtNotifications = _AristaBridgeExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 0)
)
_AristaDot1qTpFdbTable_Object = MibTable
aristaDot1qTpFdbTable = _AristaDot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aristaDot1qTpFdbTable.setStatus("current")
_AristaDot1qTpFdbEntry_Object = MibTableRow
aristaDot1qTpFdbEntry = _AristaDot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1)
)
aristaDot1qTpFdbEntry.setIndexNames(
    (0, "ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbTimeMark"),
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    aristaDot1qTpFdbEntry.setStatus("current")
_AristaDot1qTpFdbTimeMark_Type = TimeFilter
_AristaDot1qTpFdbTimeMark_Object = MibTableColumn
aristaDot1qTpFdbTimeMark = _AristaDot1qTpFdbTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 1),
    _AristaDot1qTpFdbTimeMark_Type()
)
aristaDot1qTpFdbTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDot1qTpFdbTimeMark.setStatus("current")
_AristaDot1qTpFdbNumMoves_Type = Counter32
_AristaDot1qTpFdbNumMoves_Object = MibTableColumn
aristaDot1qTpFdbNumMoves = _AristaDot1qTpFdbNumMoves_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 2),
    _AristaDot1qTpFdbNumMoves_Type()
)
aristaDot1qTpFdbNumMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDot1qTpFdbNumMoves.setStatus("current")
_AristaDot1qTpFdbLastMove_Type = TimeTicks
_AristaDot1qTpFdbLastMove_Object = MibTableColumn
aristaDot1qTpFdbLastMove = _AristaDot1qTpFdbLastMove_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 3),
    _AristaDot1qTpFdbLastMove_Type()
)
aristaDot1qTpFdbLastMove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDot1qTpFdbLastMove.setStatus("current")
_AristaBridgeExtConformance_ObjectIdentity = ObjectIdentity
aristaBridgeExtConformance = _AristaBridgeExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2)
)
_AristaBridgeExtGroups_ObjectIdentity = ObjectIdentity
aristaBridgeExtGroups = _AristaBridgeExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1)
)
_AristaBridgeExtCompliances_ObjectIdentity = ObjectIdentity
aristaBridgeExtCompliances = _AristaBridgeExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2)
)
_AristaMacStatsTable_Object = MibTable
aristaMacStatsTable = _AristaMacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 3)
)
if mibBuilder.loadTexts:
    aristaMacStatsTable.setStatus("current")
_AristaMacStatsEntry_Object = MibTableRow
aristaMacStatsEntry = _AristaMacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 3, 1)
)
aristaMacStatsEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "ARISTA-BRIDGE-EXT-MIB", "aristaMacStatsEntryType"),
)
if mibBuilder.loadTexts:
    aristaMacStatsEntry.setStatus("current")


class _AristaMacStatsEntryType_Type(Integer32):
    """Custom type aristaMacStatsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_AristaMacStatsEntryType_Type.__name__ = "Integer32"
_AristaMacStatsEntryType_Object = MibTableColumn
aristaMacStatsEntryType = _AristaMacStatsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 3, 1, 1),
    _AristaMacStatsEntryType_Type()
)
aristaMacStatsEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaMacStatsEntryType.setStatus("current")
_AristaMacStatsEntries_Type = Counter32
_AristaMacStatsEntries_Object = MibTableColumn
aristaMacStatsEntries = _AristaMacStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 3, 1, 2),
    _AristaMacStatsEntries_Type()
)
aristaMacStatsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaMacStatsEntries.setStatus("current")

# Managed Objects groups

aristaBridgeExtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 1)
)
aristaBridgeExtBaseGroup.setObjects(
      *(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"),
        ("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbLastMove"),
        ("ARISTA-BRIDGE-EXT-MIB", "aristaMacStatsEntries"))
)
if mibBuilder.loadTexts:
    aristaBridgeExtBaseGroup.setStatus("current")


# Notification objects

aristaMacMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 0, 1)
)
aristaMacMove.setObjects(
      *(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"),
        ("Q-BRIDGE-MIB", "dot1qTpFdbPort"))
)
if mibBuilder.loadTexts:
    aristaMacMove.setStatus(
        "current"
    )

aristaMacLearn = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 0, 2)
)
aristaMacLearn.setObjects(
    ("Q-BRIDGE-MIB", "dot1qTpFdbPort")
)
if mibBuilder.loadTexts:
    aristaMacLearn.setStatus(
        "current"
    )

aristaMacAge = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 0, 3)
)
aristaMacAge.setObjects(
    ("Q-BRIDGE-MIB", "dot1qTpFdbPort")
)
if mibBuilder.loadTexts:
    aristaMacAge.setStatus(
        "current"
    )


# Notifications groups

aristaBridgeExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 2)
)
aristaBridgeExtNotificationGroup.setObjects(
      *(("ARISTA-BRIDGE-EXT-MIB", "aristaMacMove"),
        ("ARISTA-BRIDGE-EXT-MIB", "aristaMacLearn"),
        ("ARISTA-BRIDGE-EXT-MIB", "aristaMacAge"))
)
if mibBuilder.loadTexts:
    aristaBridgeExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaBridgeExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 1)
)
aristaBridgeExtCompliance.setObjects(
    ("ARISTA-BRIDGE-EXT-MIB", "aristaBridgeExtBaseGroup")
)
if mibBuilder.loadTexts:
    aristaBridgeExtCompliance.setStatus(
        "current"
    )

aristaBridgeExtNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 2)
)
aristaBridgeExtNotificationCompliance.setObjects(
    ("ARISTA-BRIDGE-EXT-MIB", "aristaBridgeExtNotificationGroup")
)
if mibBuilder.loadTexts:
    aristaBridgeExtNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-BRIDGE-EXT-MIB",
    **{"aristaBridgeExtMIB": aristaBridgeExtMIB,
       "aristaBridgeExtNotifications": aristaBridgeExtNotifications,
       "aristaMacMove": aristaMacMove,
       "aristaMacLearn": aristaMacLearn,
       "aristaMacAge": aristaMacAge,
       "aristaDot1qTpFdbTable": aristaDot1qTpFdbTable,
       "aristaDot1qTpFdbEntry": aristaDot1qTpFdbEntry,
       "aristaDot1qTpFdbTimeMark": aristaDot1qTpFdbTimeMark,
       "aristaDot1qTpFdbNumMoves": aristaDot1qTpFdbNumMoves,
       "aristaDot1qTpFdbLastMove": aristaDot1qTpFdbLastMove,
       "aristaBridgeExtConformance": aristaBridgeExtConformance,
       "aristaBridgeExtGroups": aristaBridgeExtGroups,
       "aristaBridgeExtBaseGroup": aristaBridgeExtBaseGroup,
       "aristaBridgeExtNotificationGroup": aristaBridgeExtNotificationGroup,
       "aristaBridgeExtCompliances": aristaBridgeExtCompliances,
       "aristaBridgeExtCompliance": aristaBridgeExtCompliance,
       "aristaBridgeExtNotificationCompliance": aristaBridgeExtNotificationCompliance,
       "aristaMacStatsTable": aristaMacStatsTable,
       "aristaMacStatsEntry": aristaMacStatsEntry,
       "aristaMacStatsEntryType": aristaMacStatsEntryType,
       "aristaMacStatsEntries": aristaMacStatsEntries}
)
