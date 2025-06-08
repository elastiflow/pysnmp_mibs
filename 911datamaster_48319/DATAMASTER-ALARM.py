# SNMP MIB module (DATAMASTER-ALARM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/911datamaster_48319/DATAMASTER-ALARM.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:12:23 2025
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

datamaster = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48319)
)
if mibBuilder.loadTexts:
    datamaster.setRevisions(
        ("2016-09-13 17:42",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48319, 1)
)
if mibBuilder.loadTexts:
    alarm.setStatus("current")
_Title_Type = DisplayString
_Title_Object = MibScalar
title = _Title_Object(
    (1, 3, 6, 1, 4, 1, 48319, 1, 1),
    _Title_Type()
)
title.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    title.setStatus("current")
_Severity_Type = DisplayString
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 48319, 1, 2),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_DateTime_Type = DisplayString
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 48319, 1, 3),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_NodeID_Type = DisplayString
_NodeID_Object = MibScalar
nodeID = _NodeID_Object(
    (1, 3, 6, 1, 4, 1, 48319, 1, 4),
    _NodeID_Type()
)
nodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeID.setStatus("current")
_EventData_Type = DisplayString
_EventData_Object = MibScalar
eventData = _EventData_Object(
    (1, 3, 6, 1, 4, 1, 48319, 1, 5),
    _EventData_Type()
)
eventData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventData.setStatus("current")

# Managed Objects groups


# Notification objects

dmHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 100)
)
if mibBuilder.loadTexts:
    dmHeartbeat.setStatus(
        "current"
    )

dmALIDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 110)
)
if mibBuilder.loadTexts:
    dmALIDown.setStatus(
        "current"
    )

dmALIup = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 111)
)
if mibBuilder.loadTexts:
    dmALIup.setStatus(
        "current"
    )

dmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 120)
)
if mibBuilder.loadTexts:
    dmLinkDown.setStatus(
        "current"
    )

dmLinkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 121)
)
if mibBuilder.loadTexts:
    dmLinkup.setStatus(
        "current"
    )

dmSynchronizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 130)
)
if mibBuilder.loadTexts:
    dmSynchronizationFailure.setStatus(
        "current"
    )

dmImportFileNotReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 140)
)
if mibBuilder.loadTexts:
    dmImportFileNotReceived.setStatus(
        "current"
    )

dmFileImportFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 150)
)
if mibBuilder.loadTexts:
    dmFileImportFailure.setStatus(
        "current"
    )

dmSelectiveRouterUpdateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 160)
)
if mibBuilder.loadTexts:
    dmSelectiveRouterUpdateFailure.setStatus(
        "current"
    )

dmRapidHeartbeatReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 170)
)
if mibBuilder.loadTexts:
    dmRapidHeartbeatReceived.setStatus(
        "current"
    )

dmLinkNoiseReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 48319, 1, 180)
)
if mibBuilder.loadTexts:
    dmLinkNoiseReceived.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATAMASTER-ALARM",
    **{"datamaster": datamaster,
       "alarm": alarm,
       "title": title,
       "severity": severity,
       "dateTime": dateTime,
       "nodeID": nodeID,
       "eventData": eventData,
       "dmHeartbeat": dmHeartbeat,
       "dmALIDown": dmALIDown,
       "dmALIup": dmALIup,
       "dmLinkDown": dmLinkDown,
       "dmLinkup": dmLinkup,
       "dmSynchronizationFailure": dmSynchronizationFailure,
       "dmImportFileNotReceived": dmImportFileNotReceived,
       "dmFileImportFailure": dmFileImportFailure,
       "dmSelectiveRouterUpdateFailure": dmSelectiveRouterUpdateFailure,
       "dmRapidHeartbeatReceived": dmRapidHeartbeatReceived,
       "dmLinkNoiseReceived": dmLinkNoiseReceived}
)
