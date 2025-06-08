# SNMP MIB module (INODESL-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/enghouse_46906/INODESL-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:06:44 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enghouse_ObjectIdentity = ObjectIdentity
enghouse = _Enghouse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46906)
)
_Inode3_ObjectIdentity = ObjectIdentity
inode3 = _Inode3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46906, 2)
)
_InodeSL_ObjectIdentity = ObjectIdentity
inodeSL = _InodeSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 1)
)
_Instance_Type = DisplayString
_Instance_Object = MibScalar
instance = _Instance_Object(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 1, 1),
    _Instance_Type()
)
instance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instance.setStatus("mandatory")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 1, 2),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("mandatory")
_Message_Type = DisplayString
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 1, 3),
    _Message_Type()
)
message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    message.setStatus("mandatory")
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 1, 4),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")
_TrapAlarms_ObjectIdentity = ObjectIdentity
trapAlarms = _TrapAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2)
)
_TrapEvents_ObjectIdentity = ObjectIdentity
trapEvents = _TrapEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3)
)

# Managed Objects groups


# Notification objects

slProcessRunningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 1)
)
slProcessRunningAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slProcessRunningAlarm.setStatus(
        ""
    )

slSystemExceptionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 2)
)
slSystemExceptionAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slSystemExceptionAlarm.setStatus(
        ""
    )

slDatabaseInitializationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 3)
)
slDatabaseInitializationAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slDatabaseInitializationAlarm.setStatus(
        ""
    )

slStatisticsErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 4)
)
slStatisticsErrorAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slStatisticsErrorAlarm.setStatus(
        ""
    )

slTCPIPMaintSocketErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 5)
)
slTCPIPMaintSocketErrorAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slTCPIPMaintSocketErrorAlarm.setStatus(
        ""
    )

slTCPIPFESocketErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 6)
)
slTCPIPFESocketErrorAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slTCPIPFESocketErrorAlarm.setStatus(
        ""
    )

slEnumBackendErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 7)
)
slEnumBackendErrorAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slEnumBackendErrorAlarm.setStatus(
        ""
    )

slCCStatisticsErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 8)
)
slCCStatisticsErrorAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slCCStatisticsErrorAlarm.setStatus(
        ""
    )

slCCStatusListErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 2, 0, 9)
)
slCCStatusListErrorAlarm.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slCCStatusListErrorAlarm.setStatus(
        ""
    )

slProcessMessageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 100)
)
slProcessMessageEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slProcessMessageEvent.setStatus(
        ""
    )

slDispatcherEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 101)
)
slDispatcherEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slDispatcherEvent.setStatus(
        ""
    )

slEnumBeErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 102)
)
slEnumBeErrorEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slEnumBeErrorEvent.setStatus(
        ""
    )

slServiceNumberPortingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 103)
)
slServiceNumberPortingEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slServiceNumberPortingEvent.setStatus(
        ""
    )

slServiceNumberTranslEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 104)
)
slServiceNumberTranslEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slServiceNumberTranslEvent.setStatus(
        ""
    )

slServiceCallControlEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 105)
)
slServiceCallControlEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slServiceCallControlEvent.setStatus(
        ""
    )

slServiceRoutingEngineEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 46906, 2, 1, 3, 0, 106)
)
slServiceRoutingEngineEvent.setObjects(
      *(("INODESL-TRAP-MIB", "instance"),
        ("INODESL-TRAP-MIB", "severity"),
        ("INODESL-TRAP-MIB", "message"),
        ("INODESL-TRAP-MIB", "name"))
)
if mibBuilder.loadTexts:
    slServiceRoutingEngineEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INODESL-TRAP-MIB",
    **{"enghouse": enghouse,
       "inode3": inode3,
       "inodeSL": inodeSL,
       "objects": objects,
       "instance": instance,
       "severity": severity,
       "message": message,
       "name": name,
       "trapAlarms": trapAlarms,
       "slProcessRunningAlarm": slProcessRunningAlarm,
       "slSystemExceptionAlarm": slSystemExceptionAlarm,
       "slDatabaseInitializationAlarm": slDatabaseInitializationAlarm,
       "slStatisticsErrorAlarm": slStatisticsErrorAlarm,
       "slTCPIPMaintSocketErrorAlarm": slTCPIPMaintSocketErrorAlarm,
       "slTCPIPFESocketErrorAlarm": slTCPIPFESocketErrorAlarm,
       "slEnumBackendErrorAlarm": slEnumBackendErrorAlarm,
       "slCCStatisticsErrorAlarm": slCCStatisticsErrorAlarm,
       "slCCStatusListErrorAlarm": slCCStatusListErrorAlarm,
       "trapEvents": trapEvents,
       "slProcessMessageEvent": slProcessMessageEvent,
       "slDispatcherEvent": slDispatcherEvent,
       "slEnumBeErrorEvent": slEnumBeErrorEvent,
       "slServiceNumberPortingEvent": slServiceNumberPortingEvent,
       "slServiceNumberTranslEvent": slServiceNumberTranslEvent,
       "slServiceCallControlEvent": slServiceCallControlEvent,
       "slServiceRoutingEngineEvent": slServiceRoutingEngineEvent}
)
