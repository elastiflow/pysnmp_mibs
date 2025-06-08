# SNMP MIB module (FORCE10-TRAP-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/FORCE10-TRAP-EVENT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:01 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

f10TrapEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6)
)
if mibBuilder.loadTexts:
    f10TrapEventMib.setRevisions(
        ("2013-01-01 00:00",
         "2005-10-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10TrapEventObjects_ObjectIdentity = ObjectIdentity
f10TrapEventObjects = _F10TrapEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1)
)
_F10HistoryTrapEvent_ObjectIdentity = ObjectIdentity
f10HistoryTrapEvent = _F10HistoryTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1)
)
_F10ChassisBootupTime_Type = DateAndTime
_F10ChassisBootupTime_Object = MibScalar
f10ChassisBootupTime = _F10ChassisBootupTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 1),
    _F10ChassisBootupTime_Type()
)
f10ChassisBootupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10ChassisBootupTime.setStatus("current")


class _F10LastTrapEventSeqId_Type(Integer32):
    """Custom type f10LastTrapEventSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_F10LastTrapEventSeqId_Type.__name__ = "Integer32"
_F10LastTrapEventSeqId_Object = MibScalar
f10LastTrapEventSeqId = _F10LastTrapEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 2),
    _F10LastTrapEventSeqId_Type()
)
f10LastTrapEventSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10LastTrapEventSeqId.setStatus("current")
_F10MaxHistoryTableSize_Type = Integer32
_F10MaxHistoryTableSize_Object = MibScalar
f10MaxHistoryTableSize = _F10MaxHistoryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 3),
    _F10MaxHistoryTableSize_Type()
)
f10MaxHistoryTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10MaxHistoryTableSize.setStatus("current")
_F10HistoryTrapEventTable_Object = MibTable
f10HistoryTrapEventTable = _F10HistoryTrapEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    f10HistoryTrapEventTable.setStatus("current")
_F10HistoryTrapEventEntry_Object = MibTableRow
f10HistoryTrapEventEntry = _F10HistoryTrapEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1)
)
f10HistoryTrapEventEntry.setIndexNames(
    (0, "FORCE10-TRAP-EVENT-MIB", "historyTrapEventSeqId"),
)
if mibBuilder.loadTexts:
    f10HistoryTrapEventEntry.setStatus("current")


class _HistoryTrapEventSeqId_Type(Integer32):
    """Custom type historyTrapEventSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HistoryTrapEventSeqId_Type.__name__ = "Integer32"
_HistoryTrapEventSeqId_Object = MibTableColumn
historyTrapEventSeqId = _HistoryTrapEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 1),
    _HistoryTrapEventSeqId_Type()
)
historyTrapEventSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyTrapEventSeqId.setStatus("current")
_HistoryTrapEventSeverity_Type = Integer32
_HistoryTrapEventSeverity_Object = MibTableColumn
historyTrapEventSeverity = _HistoryTrapEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 2),
    _HistoryTrapEventSeverity_Type()
)
historyTrapEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventSeverity.setStatus("current")
_HistoryTrapEventType_Type = Integer32
_HistoryTrapEventType_Object = MibTableColumn
historyTrapEventType = _HistoryTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 3),
    _HistoryTrapEventType_Type()
)
historyTrapEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventType.setStatus("current")
_HistoryTrapEventMsg_Type = DisplayString
_HistoryTrapEventMsg_Object = MibTableColumn
historyTrapEventMsg = _HistoryTrapEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 4),
    _HistoryTrapEventMsg_Type()
)
historyTrapEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventMsg.setStatus("current")
_HistoryTrapEventOid_Type = RowPointer
_HistoryTrapEventOid_Object = MibTableColumn
historyTrapEventOid = _HistoryTrapEventOid_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 5),
    _HistoryTrapEventOid_Type()
)
historyTrapEventOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventOid.setStatus("current")
_HistoryTrapEventSlot_Type = Integer32
_HistoryTrapEventSlot_Object = MibTableColumn
historyTrapEventSlot = _HistoryTrapEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 6),
    _HistoryTrapEventSlot_Type()
)
historyTrapEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventSlot.setStatus("current")
_HistoryTrapEventTimeStamp_Type = TimeTicks
_HistoryTrapEventTimeStamp_Object = MibTableColumn
historyTrapEventTimeStamp = _HistoryTrapEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 7),
    _HistoryTrapEventTimeStamp_Type()
)
historyTrapEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventTimeStamp.setStatus("current")
_HistoryTrapEventPort_Type = Integer32
_HistoryTrapEventPort_Object = MibTableColumn
historyTrapEventPort = _HistoryTrapEventPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 8),
    _HistoryTrapEventPort_Type()
)
historyTrapEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventPort.setStatus("current")
_F10ActiveTrapEvent_ObjectIdentity = ObjectIdentity
f10ActiveTrapEvent = _F10ActiveTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2)
)
_F10ActiveTrapEventTable_Object = MibTable
f10ActiveTrapEventTable = _F10ActiveTrapEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f10ActiveTrapEventTable.setStatus("current")
_F10ActiveTrapEventEntry_Object = MibTableRow
f10ActiveTrapEventEntry = _F10ActiveTrapEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1)
)
f10ActiveTrapEventEntry.setIndexNames(
    (0, "FORCE10-TRAP-EVENT-MIB", "activeTrapEventSeqId"),
)
if mibBuilder.loadTexts:
    f10ActiveTrapEventEntry.setStatus("current")


class _ActiveTrapEventSeqId_Type(Integer32):
    """Custom type activeTrapEventSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ActiveTrapEventSeqId_Type.__name__ = "Integer32"
_ActiveTrapEventSeqId_Object = MibTableColumn
activeTrapEventSeqId = _ActiveTrapEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 1),
    _ActiveTrapEventSeqId_Type()
)
activeTrapEventSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeTrapEventSeqId.setStatus("current")
_ActiveTrapEventSeverity_Type = Integer32
_ActiveTrapEventSeverity_Object = MibTableColumn
activeTrapEventSeverity = _ActiveTrapEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 2),
    _ActiveTrapEventSeverity_Type()
)
activeTrapEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventSeverity.setStatus("current")
_ActiveTrapEventType_Type = Integer32
_ActiveTrapEventType_Object = MibTableColumn
activeTrapEventType = _ActiveTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 3),
    _ActiveTrapEventType_Type()
)
activeTrapEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventType.setStatus("current")
_ActiveTrapEventMsg_Type = DisplayString
_ActiveTrapEventMsg_Object = MibTableColumn
activeTrapEventMsg = _ActiveTrapEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 4),
    _ActiveTrapEventMsg_Type()
)
activeTrapEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventMsg.setStatus("current")
_ActiveTrapEventOid_Type = RowPointer
_ActiveTrapEventOid_Object = MibTableColumn
activeTrapEventOid = _ActiveTrapEventOid_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 5),
    _ActiveTrapEventOid_Type()
)
activeTrapEventOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventOid.setStatus("current")
_ActiveTrapEventSlot_Type = Integer32
_ActiveTrapEventSlot_Object = MibTableColumn
activeTrapEventSlot = _ActiveTrapEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 6),
    _ActiveTrapEventSlot_Type()
)
activeTrapEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventSlot.setStatus("current")
_ActiveTrapEventTimeStamp_Type = TimeTicks
_ActiveTrapEventTimeStamp_Object = MibTableColumn
activeTrapEventTimeStamp = _ActiveTrapEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 7),
    _ActiveTrapEventTimeStamp_Type()
)
activeTrapEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventTimeStamp.setStatus("current")
_ActiveTrapEventPort_Type = Integer32
_ActiveTrapEventPort_Object = MibTableColumn
activeTrapEventPort = _ActiveTrapEventPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 8),
    _ActiveTrapEventPort_Type()
)
activeTrapEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventPort.setStatus("current")
_F10TrapVarbindEvent_ObjectIdentity = ObjectIdentity
f10TrapVarbindEvent = _F10TrapVarbindEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3)
)
_F10TrapEventVarbindTable_Object = MibTable
f10TrapEventVarbindTable = _F10TrapEventVarbindTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f10TrapEventVarbindTable.setStatus("current")
_F10TrapEventVarbindEntry_Object = MibTableRow
f10TrapEventVarbindEntry = _F10TrapEventVarbindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1)
)
f10TrapEventVarbindEntry.setIndexNames(
    (0, "FORCE10-TRAP-EVENT-MIB", "trapEventVarbindSeqId"),
    (0, "FORCE10-TRAP-EVENT-MIB", "trapEventVarbindId"),
)
if mibBuilder.loadTexts:
    f10TrapEventVarbindEntry.setStatus("current")


class _TrapEventVarbindSeqId_Type(Integer32):
    """Custom type trapEventVarbindSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapEventVarbindSeqId_Type.__name__ = "Integer32"
_TrapEventVarbindSeqId_Object = MibTableColumn
trapEventVarbindSeqId = _TrapEventVarbindSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 1),
    _TrapEventVarbindSeqId_Type()
)
trapEventVarbindSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventVarbindSeqId.setStatus("current")


class _TrapEventVarbindId_Type(Integer32):
    """Custom type trapEventVarbindId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TrapEventVarbindId_Type.__name__ = "Integer32"
_TrapEventVarbindId_Object = MibTableColumn
trapEventVarbindId = _TrapEventVarbindId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 2),
    _TrapEventVarbindId_Type()
)
trapEventVarbindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventVarbindId.setStatus("current")
_TrapEventVarbindOid_Type = ObjectIdentifier
_TrapEventVarbindOid_Object = MibTableColumn
trapEventVarbindOid = _TrapEventVarbindOid_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 3),
    _TrapEventVarbindOid_Type()
)
trapEventVarbindOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventVarbindOid.setStatus("current")
_TrapEventVarbindType_Type = Integer32
_TrapEventVarbindType_Object = MibTableColumn
trapEventVarbindType = _TrapEventVarbindType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 4),
    _TrapEventVarbindType_Type()
)
trapEventVarbindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventVarbindType.setStatus("current")
_TrapEventVarbindValue_Type = DisplayString
_TrapEventVarbindValue_Object = MibTableColumn
trapEventVarbindValue = _TrapEventVarbindValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 5),
    _TrapEventVarbindValue_Type()
)
trapEventVarbindValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventVarbindValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-TRAP-EVENT-MIB",
    **{"f10TrapEventMib": f10TrapEventMib,
       "f10TrapEventObjects": f10TrapEventObjects,
       "f10HistoryTrapEvent": f10HistoryTrapEvent,
       "f10ChassisBootupTime": f10ChassisBootupTime,
       "f10LastTrapEventSeqId": f10LastTrapEventSeqId,
       "f10MaxHistoryTableSize": f10MaxHistoryTableSize,
       "f10HistoryTrapEventTable": f10HistoryTrapEventTable,
       "f10HistoryTrapEventEntry": f10HistoryTrapEventEntry,
       "historyTrapEventSeqId": historyTrapEventSeqId,
       "historyTrapEventSeverity": historyTrapEventSeverity,
       "historyTrapEventType": historyTrapEventType,
       "historyTrapEventMsg": historyTrapEventMsg,
       "historyTrapEventOid": historyTrapEventOid,
       "historyTrapEventSlot": historyTrapEventSlot,
       "historyTrapEventTimeStamp": historyTrapEventTimeStamp,
       "historyTrapEventPort": historyTrapEventPort,
       "f10ActiveTrapEvent": f10ActiveTrapEvent,
       "f10ActiveTrapEventTable": f10ActiveTrapEventTable,
       "f10ActiveTrapEventEntry": f10ActiveTrapEventEntry,
       "activeTrapEventSeqId": activeTrapEventSeqId,
       "activeTrapEventSeverity": activeTrapEventSeverity,
       "activeTrapEventType": activeTrapEventType,
       "activeTrapEventMsg": activeTrapEventMsg,
       "activeTrapEventOid": activeTrapEventOid,
       "activeTrapEventSlot": activeTrapEventSlot,
       "activeTrapEventTimeStamp": activeTrapEventTimeStamp,
       "activeTrapEventPort": activeTrapEventPort,
       "f10TrapVarbindEvent": f10TrapVarbindEvent,
       "f10TrapEventVarbindTable": f10TrapEventVarbindTable,
       "f10TrapEventVarbindEntry": f10TrapEventVarbindEntry,
       "trapEventVarbindSeqId": trapEventVarbindSeqId,
       "trapEventVarbindId": trapEventVarbindId,
       "trapEventVarbindOid": trapEventVarbindOid,
       "trapEventVarbindType": trapEventVarbindType,
       "trapEventVarbindValue": trapEventVarbindValue}
)
