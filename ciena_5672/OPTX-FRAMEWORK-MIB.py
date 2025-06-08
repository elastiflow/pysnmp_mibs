# SNMP MIB module (OPTX-FRAMEWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_5672/OPTX-FRAMEWORK-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:47:13 2025
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

(OptxAlarmStatusValue,
 OptxFaultType,
 OptxIfIndexType,
 OptxProbableCauseValue,
 OptxRestartValue,
 OptxThresholdType,
 onlineModule) = mibBuilder.importSymbols(
    "OPTX-ONLINE-MIB",
    "OptxAlarmStatusValue",
    "OptxFaultType",
    "OptxIfIndexType",
    "OptxProbableCauseValue",
    "OptxRestartValue",
    "OptxThresholdType",
    "onlineModule")

(DisplayString,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPV2-TC",
    "DisplayString",
    "RowStatus")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

onlineFramework = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10)
)
if mibBuilder.loadTexts:
    onlineFramework.setRevisions(
        ("1900-02-28 18:01",
         "1900-01-13 18:01",
         "1900-01-11 18:01",
         "1900-12-05 18:00",
         "1900-10-04 18:00",
         "1900-08-15 18:00",
         "1900-07-20 18:00",
         "1900-06-21 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptxEventNotification_ObjectIdentity = ObjectIdentity
optxEventNotification = _OptxEventNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1)
)
_OptxEventIfIndex_Type = OptxIfIndexType
_OptxEventIfIndex_Object = MibScalar
optxEventIfIndex = _OptxEventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 20),
    _OptxEventIfIndex_Type()
)
optxEventIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optxEventIfIndex.setStatus("current")
_OptxEventFaultType_Type = OptxFaultType
_OptxEventFaultType_Object = MibScalar
optxEventFaultType = _OptxEventFaultType_Object(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 21),
    _OptxEventFaultType_Type()
)
optxEventFaultType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optxEventFaultType.setStatus("current")
_OptxEventPerceivedSeverity_Type = OptxAlarmStatusValue
_OptxEventPerceivedSeverity_Object = MibScalar
optxEventPerceivedSeverity = _OptxEventPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 22),
    _OptxEventPerceivedSeverity_Type()
)
optxEventPerceivedSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optxEventPerceivedSeverity.setStatus("current")
_OptxEventProbableCause_Type = OptxProbableCauseValue
_OptxEventProbableCause_Object = MibScalar
optxEventProbableCause = _OptxEventProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 23),
    _OptxEventProbableCause_Type()
)
optxEventProbableCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optxEventProbableCause.setStatus("current")
_OptxEventRestartType_Type = OptxRestartValue
_OptxEventRestartType_Object = MibScalar
optxEventRestartType = _OptxEventRestartType_Object(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 24),
    _OptxEventRestartType_Type()
)
optxEventRestartType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optxEventRestartType.setStatus("current")

# Managed Objects groups


# Notification objects

optxEventColdRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 2)
)
optxEventColdRestart.setObjects(
    ("OPTX-FRAMEWORK-MIB", "optxEventIfIndex")
)
if mibBuilder.loadTexts:
    optxEventColdRestart.setStatus(
        "current"
    )

optxEventRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 3)
)
optxEventRestart.setObjects(
      *(("OPTX-FRAMEWORK-MIB", "optxEventIfIndex"),
        ("OPTX-FRAMEWORK-MIB", "optxEventRestartType"))
)
if mibBuilder.loadTexts:
    optxEventRestart.setStatus(
        "current"
    )

optxEventAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 4)
)
optxEventAlarm.setObjects(
      *(("OPTX-FRAMEWORK-MIB", "optxEventIfIndex"),
        ("OPTX-FRAMEWORK-MIB", "optxEventFaultType"),
        ("OPTX-FRAMEWORK-MIB", "optxEventPerceivedSeverity"),
        ("OPTX-FRAMEWORK-MIB", "optxEventProbableCause"))
)
if mibBuilder.loadTexts:
    optxEventAlarm.setStatus(
        "current"
    )

optxEventThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 5)
)
optxEventThreshold.setObjects(
    ("OPTX-FRAMEWORK-MIB", "optxEventIfIndex")
)
if mibBuilder.loadTexts:
    optxEventThreshold.setStatus(
        "current"
    )

optxEventProtectionSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 6)
)
optxEventProtectionSwitch.setObjects(
    ("OPTX-FRAMEWORK-MIB", "optxEventIfIndex")
)
if mibBuilder.loadTexts:
    optxEventProtectionSwitch.setStatus(
        "current"
    )

optxEventHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 7)
)
if mibBuilder.loadTexts:
    optxEventHeartBeat.setStatus(
        "current"
    )

optxEventBufferOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5672, 1, 10, 1, 8)
)
if mibBuilder.loadTexts:
    optxEventBufferOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTX-FRAMEWORK-MIB",
    **{"onlineFramework": onlineFramework,
       "optxEventNotification": optxEventNotification,
       "optxEventColdRestart": optxEventColdRestart,
       "optxEventRestart": optxEventRestart,
       "optxEventAlarm": optxEventAlarm,
       "optxEventThreshold": optxEventThreshold,
       "optxEventProtectionSwitch": optxEventProtectionSwitch,
       "optxEventHeartBeat": optxEventHeartBeat,
       "optxEventBufferOverflow": optxEventBufferOverflow,
       "optxEventIfIndex": optxEventIfIndex,
       "optxEventFaultType": optxEventFaultType,
       "optxEventPerceivedSeverity": optxEventPerceivedSeverity,
       "optxEventProbableCause": optxEventProbableCause,
       "optxEventRestartType": optxEventRestartType}
)
