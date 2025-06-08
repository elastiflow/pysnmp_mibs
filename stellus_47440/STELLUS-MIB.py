# SNMP MIB module (STELLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stellus_47440/STELLUS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:03:25 2025
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
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
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

stellusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47440)
)
if mibBuilder.loadTexts:
    stellusMib.setRevisions(
        ("2016-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StellusMibObjects_ObjectIdentity = ObjectIdentity
stellusMibObjects = _StellusMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47440, 0)
)
_NotificationParams_ObjectIdentity = ObjectIdentity
notificationParams = _NotificationParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1)
)


class _Seq_Type(OctetString):
    """Custom type seq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Seq_Type.__name__ = "OctetString"
_Seq_Object = MibScalar
seq = _Seq_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 1),
    _Seq_Type()
)
seq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seq.setStatus("current")


class _ProcName_Type(OctetString):
    """Custom type procName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ProcName_Type.__name__ = "OctetString"
_ProcName_Object = MibScalar
procName = _ProcName_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 2),
    _ProcName_Type()
)
procName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procName.setStatus("current")


class _Reason_Type(OctetString):
    """Custom type reason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Reason_Type.__name__ = "OctetString"
_Reason_Object = MibScalar
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 3),
    _Reason_Type()
)
reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reason.setStatus("current")


class _Username_Type(OctetString):
    """Custom type username based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Username_Type.__name__ = "OctetString"
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 4),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _Userid_Type(OctetString):
    """Custom type userid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Userid_Type.__name__ = "OctetString"
_Userid_Object = MibScalar
userid = _Userid_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 5),
    _Userid_Type()
)
userid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userid.setStatus("current")


class _Hostname_Type(OctetString):
    """Custom type hostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hostname_Type.__name__ = "OctetString"
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 6),
    _Hostname_Type()
)
hostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostname.setStatus("current")


class _Adminaccount_Type(OctetString):
    """Custom type adminaccount based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Adminaccount_Type.__name__ = "OctetString"
_Adminaccount_Object = MibScalar
adminaccount = _Adminaccount_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 7),
    _Adminaccount_Type()
)
adminaccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminaccount.setStatus("current")


class _Port_Type(OctetString):
    """Custom type port based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Port_Type.__name__ = "OctetString"
_Port_Object = MibScalar
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 8),
    _Port_Type()
)
port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port.setStatus("current")


class _AlarmName_Type(OctetString):
    """Custom type alarmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmName_Type.__name__ = "OctetString"
_AlarmName_Object = MibScalar
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 9),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")


class _AlarmId_Type(OctetString):
    """Custom type alarmId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmId_Type.__name__ = "OctetString"
_AlarmId_Object = MibScalar
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 10),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")


class _NodeId_Type(OctetString):
    """Custom type nodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NodeId_Type.__name__ = "OctetString"
_NodeId_Object = MibScalar
nodeId = _NodeId_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 11),
    _NodeId_Type()
)
nodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeId.setStatus("current")


class _NotificationRuleName_Type(OctetString):
    """Custom type notificationRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotificationRuleName_Type.__name__ = "OctetString"
_NotificationRuleName_Object = MibScalar
notificationRuleName = _NotificationRuleName_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 12),
    _NotificationRuleName_Type()
)
notificationRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationRuleName.setStatus("current")


class _NotificationRuleId_Type(OctetString):
    """Custom type notificationRuleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NotificationRuleId_Type.__name__ = "OctetString"
_NotificationRuleId_Object = MibScalar
notificationRuleId = _NotificationRuleId_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 13),
    _NotificationRuleId_Type()
)
notificationRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationRuleId.setStatus("current")


class _ClearedByEventId_Type(OctetString):
    """Custom type clearedByEventId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClearedByEventId_Type.__name__ = "OctetString"
_ClearedByEventId_Object = MibScalar
clearedByEventId = _ClearedByEventId_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 14),
    _ClearedByEventId_Type()
)
clearedByEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearedByEventId.setStatus("current")


class _EventDescription_Type(OctetString):
    """Custom type eventDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EventDescription_Type.__name__ = "OctetString"
_EventDescription_Object = MibScalar
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 15),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")


class _Eventdefname_Type(OctetString):
    """Custom type eventdefname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Eventdefname_Type.__name__ = "OctetString"
_Eventdefname_Object = MibScalar
eventdefname = _Eventdefname_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 16),
    _Eventdefname_Type()
)
eventdefname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventdefname.setStatus("current")


class _Eventdefid_Type(OctetString):
    """Custom type eventdefid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Eventdefid_Type.__name__ = "OctetString"
_Eventdefid_Object = MibScalar
eventdefid = _Eventdefid_Object(
    (1, 3, 6, 1, 4, 1, 47440, 0, 1, 17),
    _Eventdefid_Type()
)
eventdefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventdefid.setStatus("current")
_StellusMibNotifications_ObjectIdentity = ObjectIdentity
stellusMibNotifications = _StellusMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47440, 1)
)
_StellusMibTraps_ObjectIdentity = ObjectIdentity
stellusMibTraps = _StellusMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0)
)

# Managed Objects groups


# Notification objects

testEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 1)
)
if mibBuilder.loadTexts:
    testEvent.setStatus(
        "current"
    )

sysmgrProcessCrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 2)
)
sysmgrProcessCrashed.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "procName"))
)
if mibBuilder.loadTexts:
    sysmgrProcessCrashed.setStatus(
        "current"
    )

sysmgrProcessHbMissExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 3)
)
sysmgrProcessHbMissExceeded.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "procName"))
)
if mibBuilder.loadTexts:
    sysmgrProcessHbMissExceeded.setStatus(
        "current"
    )

sysmgrSystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 4)
)
sysmgrSystemShutdown.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "reason"))
)
if mibBuilder.loadTexts:
    sysmgrSystemShutdown.setStatus(
        "current"
    )

sysmgrSystemReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 5)
)
sysmgrSystemReboot.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "reason"))
)
if mibBuilder.loadTexts:
    sysmgrSystemReboot.setStatus(
        "current"
    )

sysmgrBringupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 6)
)
sysmgrBringupFailed.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "reason"))
)
if mibBuilder.loadTexts:
    sysmgrBringupFailed.setStatus(
        "current"
    )

sysmgrGracefulShutdownFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 7)
)
sysmgrGracefulShutdownFailed.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "reason"))
)
if mibBuilder.loadTexts:
    sysmgrGracefulShutdownFailed.setStatus(
        "current"
    )

sysmgrRunningNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 8)
)
sysmgrRunningNormal.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "reason"))
)
if mibBuilder.loadTexts:
    sysmgrRunningNormal.setStatus(
        "current"
    )

sysmgrRunningDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 9)
)
sysmgrRunningDegraded.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "reason"))
)
if mibBuilder.loadTexts:
    sysmgrRunningDegraded.setStatus(
        "current"
    )

authSessionLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 10)
)
authSessionLogin.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"))
)
if mibBuilder.loadTexts:
    authSessionLogin.setStatus(
        "current"
    )

authUserLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 11)
)
authUserLocked.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"))
)
if mibBuilder.loadTexts:
    authUserLocked.setStatus(
        "current"
    )

authUserAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 12)
)
authUserAdded.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"))
)
if mibBuilder.loadTexts:
    authUserAdded.setStatus(
        "current"
    )

authUserDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 13)
)
authUserDeleted.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"))
)
if mibBuilder.loadTexts:
    authUserDeleted.setStatus(
        "current"
    )

authUserPasswordReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 14)
)
authUserPasswordReset.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"))
)
if mibBuilder.loadTexts:
    authUserPasswordReset.setStatus(
        "current"
    )

authServerUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 15)
)
authServerUpdated.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "hostname"),
        ("STELLUS-MIB", "adminaccount"),
        ("STELLUS-MIB", "port"))
)
if mibBuilder.loadTexts:
    authServerUpdated.setStatus(
        "current"
    )

alarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 16)
)
alarmCleared.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "alarmName"),
        ("STELLUS-MIB", "alarmId"))
)
if mibBuilder.loadTexts:
    alarmCleared.setStatus(
        "current"
    )

nodeNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 17)
)
nodeNotResponding.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "hostname"),
        ("STELLUS-MIB", "nodeId"))
)
if mibBuilder.loadTexts:
    nodeNotResponding.setStatus(
        "current"
    )

nodeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 18)
)
nodeRecovered.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "hostname"),
        ("STELLUS-MIB", "nodeId"))
)
if mibBuilder.loadTexts:
    nodeRecovered.setStatus(
        "current"
    )

nodeAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 19)
)
nodeAdded.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "hostname"),
        ("STELLUS-MIB", "nodeId"))
)
if mibBuilder.loadTexts:
    nodeAdded.setStatus(
        "current"
    )

nodeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 20)
)
nodeDeleted.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "hostname"),
        ("STELLUS-MIB", "nodeId"))
)
if mibBuilder.loadTexts:
    nodeDeleted.setStatus(
        "current"
    )

notificationRuleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 21)
)
notificationRuleAdded.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"),
        ("STELLUS-MIB", "notificationRuleName"),
        ("STELLUS-MIB", "notificationRuleId"))
)
if mibBuilder.loadTexts:
    notificationRuleAdded.setStatus(
        "current"
    )

notificationRuleUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 22)
)
notificationRuleUpdated.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"),
        ("STELLUS-MIB", "notificationRuleName"),
        ("STELLUS-MIB", "notificationRuleId"))
)
if mibBuilder.loadTexts:
    notificationRuleUpdated.setStatus(
        "current"
    )

notificationRuleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 23)
)
notificationRuleDeleted.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"),
        ("STELLUS-MIB", "notificationRuleName"),
        ("STELLUS-MIB", "notificationRuleId"))
)
if mibBuilder.loadTexts:
    notificationRuleDeleted.setStatus(
        "current"
    )

alarmClearedByEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 24)
)
alarmClearedByEvent.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "alarmName"),
        ("STELLUS-MIB", "alarmId"),
        ("STELLUS-MIB", "clearedByEventId"),
        ("STELLUS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    alarmClearedByEvent.setStatus(
        "current"
    )

smtpServerUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 25)
)
smtpServerUpdated.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"),
        ("STELLUS-MIB", "hostname"),
        ("STELLUS-MIB", "port"))
)
if mibBuilder.loadTexts:
    smtpServerUpdated.setStatus(
        "current"
    )

authUserUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 26)
)
authUserUpdated.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"))
)
if mibBuilder.loadTexts:
    authUserUpdated.setStatus(
        "current"
    )

eventDefinitionUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 47440, 1, 0, 27)
)
eventDefinitionUpdated.setObjects(
      *(("STELLUS-MIB", "seq"),
        ("STELLUS-MIB", "username"),
        ("STELLUS-MIB", "userid"),
        ("STELLUS-MIB", "eventdefname"),
        ("STELLUS-MIB", "eventdefid"))
)
if mibBuilder.loadTexts:
    eventDefinitionUpdated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STELLUS-MIB",
    **{"stellusMib": stellusMib,
       "stellusMibObjects": stellusMibObjects,
       "notificationParams": notificationParams,
       "seq": seq,
       "procName": procName,
       "reason": reason,
       "username": username,
       "userid": userid,
       "hostname": hostname,
       "adminaccount": adminaccount,
       "port": port,
       "alarmName": alarmName,
       "alarmId": alarmId,
       "nodeId": nodeId,
       "notificationRuleName": notificationRuleName,
       "notificationRuleId": notificationRuleId,
       "clearedByEventId": clearedByEventId,
       "eventDescription": eventDescription,
       "eventdefname": eventdefname,
       "eventdefid": eventdefid,
       "stellusMibNotifications": stellusMibNotifications,
       "stellusMibTraps": stellusMibTraps,
       "testEvent": testEvent,
       "sysmgrProcessCrashed": sysmgrProcessCrashed,
       "sysmgrProcessHbMissExceeded": sysmgrProcessHbMissExceeded,
       "sysmgrSystemShutdown": sysmgrSystemShutdown,
       "sysmgrSystemReboot": sysmgrSystemReboot,
       "sysmgrBringupFailed": sysmgrBringupFailed,
       "sysmgrGracefulShutdownFailed": sysmgrGracefulShutdownFailed,
       "sysmgrRunningNormal": sysmgrRunningNormal,
       "sysmgrRunningDegraded": sysmgrRunningDegraded,
       "authSessionLogin": authSessionLogin,
       "authUserLocked": authUserLocked,
       "authUserAdded": authUserAdded,
       "authUserDeleted": authUserDeleted,
       "authUserPasswordReset": authUserPasswordReset,
       "authServerUpdated": authServerUpdated,
       "alarmCleared": alarmCleared,
       "nodeNotResponding": nodeNotResponding,
       "nodeRecovered": nodeRecovered,
       "nodeAdded": nodeAdded,
       "nodeDeleted": nodeDeleted,
       "notificationRuleAdded": notificationRuleAdded,
       "notificationRuleUpdated": notificationRuleUpdated,
       "notificationRuleDeleted": notificationRuleDeleted,
       "alarmClearedByEvent": alarmClearedByEvent,
       "smtpServerUpdated": smtpServerUpdated,
       "authUserUpdated": authUserUpdated,
       "eventDefinitionUpdated": eventDefinitionUpdated}
)
