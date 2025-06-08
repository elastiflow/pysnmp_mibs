# SNMP MIB module (ARISTA-PFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-PFC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(PacketType,) = mibBuilder.importSymbols(
    "ARISTA-QUEUE-MIB",
    "PacketType")

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

aristaPfcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11)
)
if mibBuilder.loadTexts:
    aristaPfcMIB.setRevisions(
        ("2017-01-17 00:00",
         "2014-08-15 00:00",
         "2013-02-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaPfcCOSIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_AristaPfc_ObjectIdentity = ObjectIdentity
aristaPfc = _AristaPfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1)
)
_AristaPfcPriorityTable_Object = MibTable
aristaPfcPriorityTable = _AristaPfcPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1)
)
if mibBuilder.loadTexts:
    aristaPfcPriorityTable.setStatus("current")
_AristaPfcPriorityEntry_Object = MibTableRow
aristaPfcPriorityEntry = _AristaPfcPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1)
)
aristaPfcPriorityEntry.setIndexNames(
    (0, "ARISTA-PFC-MIB", "aristaPfcIfIndex"),
    (0, "ARISTA-PFC-MIB", "aristaPfcPriorityIndex"),
)
if mibBuilder.loadTexts:
    aristaPfcPriorityEntry.setStatus("current")
_AristaPfcIfIndex_Type = InterfaceIndex
_AristaPfcIfIndex_Object = MibTableColumn
aristaPfcIfIndex = _AristaPfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 1),
    _AristaPfcIfIndex_Type()
)
aristaPfcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPfcIfIndex.setStatus("current")
_AristaPfcPriorityIndex_Type = AristaPfcCOSIndex
_AristaPfcPriorityIndex_Object = MibTableColumn
aristaPfcPriorityIndex = _AristaPfcPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 2),
    _AristaPfcPriorityIndex_Type()
)
aristaPfcPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPfcPriorityIndex.setStatus("current")
_AristaPfcPriorityRequests_Type = Counter64
_AristaPfcPriorityRequests_Object = MibTableColumn
aristaPfcPriorityRequests = _AristaPfcPriorityRequests_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 3),
    _AristaPfcPriorityRequests_Type()
)
aristaPfcPriorityRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPfcPriorityRequests.setStatus("current")
if mibBuilder.loadTexts:
    aristaPfcPriorityRequests.setUnits("Requests")
_AristaPfcPriorityIndications_Type = Counter64
_AristaPfcPriorityIndications_Object = MibTableColumn
aristaPfcPriorityIndications = _AristaPfcPriorityIndications_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 1, 1, 4),
    _AristaPfcPriorityIndications_Type()
)
aristaPfcPriorityIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPfcPriorityIndications.setStatus("current")
if mibBuilder.loadTexts:
    aristaPfcPriorityIndications.setUnits("Indications")
_AristaPfcWatchdogTxQueueTable_Object = MibTable
aristaPfcWatchdogTxQueueTable = _AristaPfcWatchdogTxQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2)
)
if mibBuilder.loadTexts:
    aristaPfcWatchdogTxQueueTable.setStatus("current")
_AristaPfcWatchdogTxQueueEntry_Object = MibTableRow
aristaPfcWatchdogTxQueueEntry = _AristaPfcWatchdogTxQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1)
)
aristaPfcWatchdogTxQueueEntry.setIndexNames(
    (0, "ARISTA-PFC-MIB", "aristaPfcWatchdogIfIndex"),
    (0, "ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueType"),
    (0, "ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueId"),
)
if mibBuilder.loadTexts:
    aristaPfcWatchdogTxQueueEntry.setStatus("current")
_AristaPfcWatchdogIfIndex_Type = InterfaceIndex
_AristaPfcWatchdogIfIndex_Object = MibTableColumn
aristaPfcWatchdogIfIndex = _AristaPfcWatchdogIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 1),
    _AristaPfcWatchdogIfIndex_Type()
)
aristaPfcWatchdogIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPfcWatchdogIfIndex.setStatus("current")
_AristaPfcWatchdogTxQueueType_Type = PacketType
_AristaPfcWatchdogTxQueueType_Object = MibTableColumn
aristaPfcWatchdogTxQueueType = _AristaPfcWatchdogTxQueueType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 2),
    _AristaPfcWatchdogTxQueueType_Type()
)
aristaPfcWatchdogTxQueueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPfcWatchdogTxQueueType.setStatus("current")


class _AristaPfcWatchdogTxQueueId_Type(Integer32):
    """Custom type aristaPfcWatchdogTxQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AristaPfcWatchdogTxQueueId_Type.__name__ = "Integer32"
_AristaPfcWatchdogTxQueueId_Object = MibTableColumn
aristaPfcWatchdogTxQueueId = _AristaPfcWatchdogTxQueueId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 3),
    _AristaPfcWatchdogTxQueueId_Type()
)
aristaPfcWatchdogTxQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPfcWatchdogTxQueueId.setStatus("current")
_AristaPfcWatchdogTxQueueStuckCount_Type = Integer32
_AristaPfcWatchdogTxQueueStuckCount_Object = MibTableColumn
aristaPfcWatchdogTxQueueStuckCount = _AristaPfcWatchdogTxQueueStuckCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 4),
    _AristaPfcWatchdogTxQueueStuckCount_Type()
)
aristaPfcWatchdogTxQueueStuckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPfcWatchdogTxQueueStuckCount.setStatus("current")
_AristaPfcWatchdogTxQueueRecoveredCount_Type = Integer32
_AristaPfcWatchdogTxQueueRecoveredCount_Object = MibTableColumn
aristaPfcWatchdogTxQueueRecoveredCount = _AristaPfcWatchdogTxQueueRecoveredCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 1, 2, 1, 5),
    _AristaPfcWatchdogTxQueueRecoveredCount_Type()
)
aristaPfcWatchdogTxQueueRecoveredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPfcWatchdogTxQueueRecoveredCount.setStatus("current")
_AristaPfcConformance_ObjectIdentity = ObjectIdentity
aristaPfcConformance = _AristaPfcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 2)
)
_AristaPfcCompliances_ObjectIdentity = ObjectIdentity
aristaPfcCompliances = _AristaPfcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1)
)
_AristaPfcGroups_ObjectIdentity = ObjectIdentity
aristaPfcGroups = _AristaPfcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2)
)

# Managed Objects groups

aristaPfcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 2, 1)
)
aristaPfcGroup.setObjects(
      *(("ARISTA-PFC-MIB", "aristaPfcPriorityRequests"),
        ("ARISTA-PFC-MIB", "aristaPfcPriorityIndications"),
        ("ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueStuckCount"),
        ("ARISTA-PFC-MIB", "aristaPfcWatchdogTxQueueRecoveredCount"))
)
if mibBuilder.loadTexts:
    aristaPfcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaPfcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 11, 2, 1, 1)
)
aristaPfcCompliance.setObjects(
    ("ARISTA-PFC-MIB", "aristaPfcGroup")
)
if mibBuilder.loadTexts:
    aristaPfcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-PFC-MIB",
    **{"AristaPfcCOSIndex": AristaPfcCOSIndex,
       "aristaPfcMIB": aristaPfcMIB,
       "aristaPfc": aristaPfc,
       "aristaPfcPriorityTable": aristaPfcPriorityTable,
       "aristaPfcPriorityEntry": aristaPfcPriorityEntry,
       "aristaPfcIfIndex": aristaPfcIfIndex,
       "aristaPfcPriorityIndex": aristaPfcPriorityIndex,
       "aristaPfcPriorityRequests": aristaPfcPriorityRequests,
       "aristaPfcPriorityIndications": aristaPfcPriorityIndications,
       "aristaPfcWatchdogTxQueueTable": aristaPfcWatchdogTxQueueTable,
       "aristaPfcWatchdogTxQueueEntry": aristaPfcWatchdogTxQueueEntry,
       "aristaPfcWatchdogIfIndex": aristaPfcWatchdogIfIndex,
       "aristaPfcWatchdogTxQueueType": aristaPfcWatchdogTxQueueType,
       "aristaPfcWatchdogTxQueueId": aristaPfcWatchdogTxQueueId,
       "aristaPfcWatchdogTxQueueStuckCount": aristaPfcWatchdogTxQueueStuckCount,
       "aristaPfcWatchdogTxQueueRecoveredCount": aristaPfcWatchdogTxQueueRecoveredCount,
       "aristaPfcConformance": aristaPfcConformance,
       "aristaPfcCompliances": aristaPfcCompliances,
       "aristaPfcCompliance": aristaPfcCompliance,
       "aristaPfcGroups": aristaPfcGroups,
       "aristaPfcGroup": aristaPfcGroup}
)
