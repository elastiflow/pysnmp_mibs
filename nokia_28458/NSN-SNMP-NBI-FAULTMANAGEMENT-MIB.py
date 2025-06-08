# SNMP MIB module (NSN-SNMP-NBI-FAULTMANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_28458/NSN-SNMP-NBI-FAULTMANAGEMENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:24:52 2025
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

(nbiEmsSynchronizationState,
 nbiEventTime,
 nbiNotSyncNEs,
 nbiObjectInstance,
 nbiRequestingNmsName,
 nbiSequenceId) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-COMMONFUNCTIONS-MIB",
    "nbiEmsSynchronizationState",
    "nbiEventTime",
    "nbiNotSyncNEs",
    "nbiObjectInstance",
    "nbiRequestingNmsName",
    "nbiSequenceId")

(nbiNetActSnmp,) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-REGISTRATION-MIB",
    "nbiNetActSnmp")

(NbiAckState,
 NbiAckTime,
 NbiAckUser,
 NbiAdditionalText,
 NbiAlarmHandling,
 NbiAlarmId,
 NbiAlarmIdList,
 NbiAlarmType,
 NbiClearTime,
 NbiClearUser,
 NbiCommentText,
 NbiCommentTime,
 NbiCommentUser,
 NbiDateAndTime,
 NbiEventTime,
 NbiGetAlarms,
 NbiGetAlarmsByStartingTime,
 NbiNumberOfAlarms,
 NbiObjectInstance,
 NbiPerceivedSeverity,
 NbiProbableCause,
 NbiProposedRepairAction,
 NbiSpecificProblem,
 NbiSupervisionPeriod) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-TEXTUALCONVENTIONS-MIB",
    "NbiAckState",
    "NbiAckTime",
    "NbiAckUser",
    "NbiAdditionalText",
    "NbiAlarmHandling",
    "NbiAlarmId",
    "NbiAlarmIdList",
    "NbiAlarmType",
    "NbiClearTime",
    "NbiClearUser",
    "NbiCommentText",
    "NbiCommentTime",
    "NbiCommentUser",
    "NbiDateAndTime",
    "NbiEventTime",
    "NbiGetAlarms",
    "NbiGetAlarmsByStartingTime",
    "NbiNumberOfAlarms",
    "NbiObjectInstance",
    "NbiPerceivedSeverity",
    "NbiProbableCause",
    "NbiProposedRepairAction",
    "NbiSpecificProblem",
    "NbiSupervisionPeriod")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nbiFaultManagementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3)
)
if mibBuilder.loadTexts:
    nbiFaultManagementMIB.setRevisions(
        ("2011-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbiFMNotifications_ObjectIdentity = ObjectIdentity
nbiFMNotifications = _NbiFMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0)
)
_NbiFMSpontaneousNotifications_ObjectIdentity = ObjectIdentity
nbiFMSpontaneousNotifications = _NbiFMSpontaneousNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 1)
)
_NbiFMOtherNotifications_ObjectIdentity = ObjectIdentity
nbiFMOtherNotifications = _NbiFMOtherNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 2)
)
_NbiFMObjects_ObjectIdentity = ObjectIdentity
nbiFMObjects = _NbiFMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1)
)
_NbiFMAlarmParameterObjects_ObjectIdentity = ObjectIdentity
nbiFMAlarmParameterObjects = _NbiFMAlarmParameterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1)
)
_NbiAckState_Type = NbiAckState
_NbiAckState_Object = MibScalar
nbiAckState = _NbiAckState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 1),
    _NbiAckState_Type()
)
nbiAckState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAckState.setStatus("current")


class _NbiAckTime_Type(NbiAckTime):
    """Custom type nbiAckTime based on NbiAckTime"""
    defaultValue = OctetString("")


_NbiAckTime_Type.__name__ = "NbiAckTime"
_NbiAckTime_Object = MibScalar
nbiAckTime = _NbiAckTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 2),
    _NbiAckTime_Type()
)
nbiAckTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAckTime.setStatus("current")


class _NbiAckUser_Type(NbiAckUser):
    """Custom type nbiAckUser based on NbiAckUser"""
    defaultValue = OctetString("")


_NbiAckUser_Type.__name__ = "NbiAckUser"
_NbiAckUser_Object = MibScalar
nbiAckUser = _NbiAckUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 3),
    _NbiAckUser_Type()
)
nbiAckUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAckUser.setStatus("current")


class _NbiAdditionalText_Type(NbiAdditionalText):
    """Custom type nbiAdditionalText based on NbiAdditionalText"""
    defaultValue = OctetString("")


_NbiAdditionalText_Type.__name__ = "NbiAdditionalText"
_NbiAdditionalText_Object = MibScalar
nbiAdditionalText = _NbiAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 4),
    _NbiAdditionalText_Type()
)
nbiAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAdditionalText.setStatus("current")


class _NbiAlarmId_Type(NbiAlarmId):
    """Custom type nbiAlarmId based on NbiAlarmId"""
    defaultValue = OctetString("1")


_NbiAlarmId_Type.__name__ = "NbiAlarmId"
_NbiAlarmId_Object = MibScalar
nbiAlarmId = _NbiAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 5),
    _NbiAlarmId_Type()
)
nbiAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAlarmId.setStatus("current")
_NbiAlarmTime_Type = NbiDateAndTime
_NbiAlarmTime_Object = MibScalar
nbiAlarmTime = _NbiAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 6),
    _NbiAlarmTime_Type()
)
nbiAlarmTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAlarmTime.setStatus("current")
_NbiAlarmType_Type = NbiAlarmType
_NbiAlarmType_Object = MibScalar
nbiAlarmType = _NbiAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 7),
    _NbiAlarmType_Type()
)
nbiAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiAlarmType.setStatus("current")


class _NbiClearTime_Type(NbiClearTime):
    """Custom type nbiClearTime based on NbiClearTime"""
    defaultValue = OctetString("")


_NbiClearTime_Type.__name__ = "NbiClearTime"
_NbiClearTime_Object = MibScalar
nbiClearTime = _NbiClearTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 8),
    _NbiClearTime_Type()
)
nbiClearTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiClearTime.setStatus("current")


class _NbiClearUser_Type(NbiClearUser):
    """Custom type nbiClearUser based on NbiClearUser"""
    defaultValue = OctetString("")


_NbiClearUser_Type.__name__ = "NbiClearUser"
_NbiClearUser_Object = MibScalar
nbiClearUser = _NbiClearUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 9),
    _NbiClearUser_Type()
)
nbiClearUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiClearUser.setStatus("current")


class _NbiCommentText_Type(NbiCommentText):
    """Custom type nbiCommentText based on NbiCommentText"""
    defaultValue = OctetString("")


_NbiCommentText_Type.__name__ = "NbiCommentText"
_NbiCommentText_Object = MibScalar
nbiCommentText = _NbiCommentText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 10),
    _NbiCommentText_Type()
)
nbiCommentText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiCommentText.setStatus("current")
_NbiCommentTime_Type = NbiCommentTime
_NbiCommentTime_Object = MibScalar
nbiCommentTime = _NbiCommentTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 11),
    _NbiCommentTime_Type()
)
nbiCommentTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiCommentTime.setStatus("current")


class _NbiCommentUser_Type(NbiCommentUser):
    """Custom type nbiCommentUser based on NbiCommentUser"""
    defaultValue = OctetString("")


_NbiCommentUser_Type.__name__ = "NbiCommentUser"
_NbiCommentUser_Object = MibScalar
nbiCommentUser = _NbiCommentUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 12),
    _NbiCommentUser_Type()
)
nbiCommentUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiCommentUser.setStatus("current")


class _NbiPerceivedSeverity_Type(NbiPerceivedSeverity):
    """Custom type nbiPerceivedSeverity based on NbiPerceivedSeverity"""
    defaultValue = 6


_NbiPerceivedSeverity_Type.__name__ = "NbiPerceivedSeverity"
_NbiPerceivedSeverity_Object = MibScalar
nbiPerceivedSeverity = _NbiPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 13),
    _NbiPerceivedSeverity_Type()
)
nbiPerceivedSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiPerceivedSeverity.setStatus("current")
_NbiProbableCause_Type = NbiProbableCause
_NbiProbableCause_Object = MibScalar
nbiProbableCause = _NbiProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 14),
    _NbiProbableCause_Type()
)
nbiProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiProbableCause.setStatus("current")


class _NbiProposedRepairAction_Type(NbiProposedRepairAction):
    """Custom type nbiProposedRepairAction based on NbiProposedRepairAction"""
    defaultValue = OctetString("")


_NbiProposedRepairAction_Type.__name__ = "NbiProposedRepairAction"
_NbiProposedRepairAction_Object = MibScalar
nbiProposedRepairAction = _NbiProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 15),
    _NbiProposedRepairAction_Type()
)
nbiProposedRepairAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiProposedRepairAction.setStatus("current")


class _NbiSpecificProblem_Type(NbiSpecificProblem):
    """Custom type nbiSpecificProblem based on NbiSpecificProblem"""
    defaultValue = OctetString("")


_NbiSpecificProblem_Type.__name__ = "NbiSpecificProblem"
_NbiSpecificProblem_Object = MibScalar
nbiSpecificProblem = _NbiSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 1, 16),
    _NbiSpecificProblem_Type()
)
nbiSpecificProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiSpecificProblem.setStatus("current")
_NbiFMAlarmHandlingObjects_ObjectIdentity = ObjectIdentity
nbiFMAlarmHandlingObjects = _NbiFMAlarmHandlingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 2)
)
_NbiAlarmIdList_Type = NbiAlarmIdList
_NbiAlarmIdList_Object = MibScalar
nbiAlarmIdList = _NbiAlarmIdList_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 2, 1),
    _NbiAlarmIdList_Type()
)
nbiAlarmIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiAlarmIdList.setStatus("current")
_NbiAcknowledgeAlarms_Type = NbiAlarmHandling
_NbiAcknowledgeAlarms_Object = MibScalar
nbiAcknowledgeAlarms = _NbiAcknowledgeAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 2, 2),
    _NbiAcknowledgeAlarms_Type()
)
nbiAcknowledgeAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiAcknowledgeAlarms.setStatus("current")
_NbiClearAlarms_Type = NbiAlarmHandling
_NbiClearAlarms_Object = MibScalar
nbiClearAlarms = _NbiClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 2, 3),
    _NbiClearAlarms_Type()
)
nbiClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiClearAlarms.setStatus("current")
_NbiCommentAlarms_Type = NbiAlarmHandling
_NbiCommentAlarms_Object = MibScalar
nbiCommentAlarms = _NbiCommentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 2, 4),
    _NbiCommentAlarms_Type()
)
nbiCommentAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiCommentAlarms.setStatus("current")
_NbiUnacknowledgeAlarms_Type = NbiAlarmHandling
_NbiUnacknowledgeAlarms_Object = MibScalar
nbiUnacknowledgeAlarms = _NbiUnacknowledgeAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 2, 5),
    _NbiUnacknowledgeAlarms_Type()
)
nbiUnacknowledgeAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiUnacknowledgeAlarms.setStatus("current")
_NbiFMSynchSingleNMSObjects_ObjectIdentity = ObjectIdentity
nbiFMSynchSingleNMSObjects = _NbiFMSynchSingleNMSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 3)
)


class _NbiGetAckAlarms_Type(NbiGetAlarms):
    """Custom type nbiGetAckAlarms based on NbiGetAlarms"""
    defaultValue = OctetString("")


_NbiGetAckAlarms_Type.__name__ = "NbiGetAlarms"
_NbiGetAckAlarms_Object = MibScalar
nbiGetAckAlarms = _NbiGetAckAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 3, 1),
    _NbiGetAckAlarms_Type()
)
nbiGetAckAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetAckAlarms.setStatus("current")


class _NbiGetActiveAlarms_Type(NbiGetAlarms):
    """Custom type nbiGetActiveAlarms based on NbiGetAlarms"""
    defaultValue = OctetString("")


_NbiGetActiveAlarms_Type.__name__ = "NbiGetAlarms"
_NbiGetActiveAlarms_Object = MibScalar
nbiGetActiveAlarms = _NbiGetActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 3, 2),
    _NbiGetActiveAlarms_Type()
)
nbiGetActiveAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetActiveAlarms.setStatus("current")


class _NbiGetAllAlarms_Type(NbiGetAlarms):
    """Custom type nbiGetAllAlarms based on NbiGetAlarms"""
    defaultValue = OctetString("")


_NbiGetAllAlarms_Type.__name__ = "NbiGetAlarms"
_NbiGetAllAlarms_Object = MibScalar
nbiGetAllAlarms = _NbiGetAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 3, 3),
    _NbiGetAllAlarms_Type()
)
nbiGetAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetAllAlarms.setStatus("current")


class _NbiGetClearedAlarms_Type(NbiGetAlarms):
    """Custom type nbiGetClearedAlarms based on NbiGetAlarms"""
    defaultValue = OctetString("")


_NbiGetClearedAlarms_Type.__name__ = "NbiGetAlarms"
_NbiGetClearedAlarms_Object = MibScalar
nbiGetClearedAlarms = _NbiGetClearedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 3, 4),
    _NbiGetClearedAlarms_Type()
)
nbiGetClearedAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetClearedAlarms.setStatus("current")
_NbiGetAlarmsByStartingTime_Type = NbiGetAlarmsByStartingTime
_NbiGetAlarmsByStartingTime_Object = MibScalar
nbiGetAlarmsByStartingTime = _NbiGetAlarmsByStartingTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 3, 5),
    _NbiGetAlarmsByStartingTime_Type()
)
nbiGetAlarmsByStartingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetAlarmsByStartingTime.setStatus("current")
_NbiFMSynchMultipleNMSObjects_ObjectIdentity = ObjectIdentity
nbiFMSynchMultipleNMSObjects = _NbiFMSynchMultipleNMSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4)
)
_NbiAckAlarmsTable_Object = MibTable
nbiAckAlarmsTable = _NbiAckAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    nbiAckAlarmsTable.setStatus("current")
_NbiAckAlarmsEntry_Object = MibTableRow
nbiAckAlarmsEntry = _NbiAckAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1)
)
nbiAckAlarmsEntry.setIndexNames(
    (0, "NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckTAlarmId"),
)
if mibBuilder.loadTexts:
    nbiAckAlarmsEntry.setStatus("current")


class _NbiAckTAlarmId_Type(NbiAlarmId):
    """Custom type nbiAckTAlarmId based on NbiAlarmId"""
    defaultValue = OctetString("1")


_NbiAckTAlarmId_Type.__name__ = "NbiAlarmId"
_NbiAckTAlarmId_Object = MibTableColumn
nbiAckTAlarmId = _NbiAckTAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 1),
    _NbiAckTAlarmId_Type()
)
nbiAckTAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbiAckTAlarmId.setStatus("current")
_NbiAckTAlarmType_Type = NbiAlarmType
_NbiAckTAlarmType_Object = MibTableColumn
nbiAckTAlarmType = _NbiAckTAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 2),
    _NbiAckTAlarmType_Type()
)
nbiAckTAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTAlarmType.setStatus("current")
_NbiAckTObjectInstance_Type = NbiObjectInstance
_NbiAckTObjectInstance_Object = MibTableColumn
nbiAckTObjectInstance = _NbiAckTObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 3),
    _NbiAckTObjectInstance_Type()
)
nbiAckTObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTObjectInstance.setStatus("current")
_NbiAckTEventTime_Type = NbiEventTime
_NbiAckTEventTime_Object = MibTableColumn
nbiAckTEventTime = _NbiAckTEventTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 4),
    _NbiAckTEventTime_Type()
)
nbiAckTEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTEventTime.setStatus("current")
_NbiAckTAlarmTime_Type = NbiDateAndTime
_NbiAckTAlarmTime_Object = MibTableColumn
nbiAckTAlarmTime = _NbiAckTAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 5),
    _NbiAckTAlarmTime_Type()
)
nbiAckTAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTAlarmTime.setStatus("current")
_NbiAckTProbableCause_Type = NbiProbableCause
_NbiAckTProbableCause_Object = MibTableColumn
nbiAckTProbableCause = _NbiAckTProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 6),
    _NbiAckTProbableCause_Type()
)
nbiAckTProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTProbableCause.setStatus("current")


class _NbiAckTSpecificProblem_Type(NbiSpecificProblem):
    """Custom type nbiAckTSpecificProblem based on NbiSpecificProblem"""
    defaultValue = OctetString("")


_NbiAckTSpecificProblem_Type.__name__ = "NbiSpecificProblem"
_NbiAckTSpecificProblem_Object = MibTableColumn
nbiAckTSpecificProblem = _NbiAckTSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 7),
    _NbiAckTSpecificProblem_Type()
)
nbiAckTSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTSpecificProblem.setStatus("current")


class _NbiAckTPerceivedSeverity_Type(NbiPerceivedSeverity):
    """Custom type nbiAckTPerceivedSeverity based on NbiPerceivedSeverity"""
    defaultValue = 6


_NbiAckTPerceivedSeverity_Type.__name__ = "NbiPerceivedSeverity"
_NbiAckTPerceivedSeverity_Object = MibTableColumn
nbiAckTPerceivedSeverity = _NbiAckTPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 8),
    _NbiAckTPerceivedSeverity_Type()
)
nbiAckTPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTPerceivedSeverity.setStatus("current")


class _NbiAckTProposedRepairAction_Type(NbiProposedRepairAction):
    """Custom type nbiAckTProposedRepairAction based on NbiProposedRepairAction"""
    defaultValue = OctetString("")


_NbiAckTProposedRepairAction_Type.__name__ = "NbiProposedRepairAction"
_NbiAckTProposedRepairAction_Object = MibTableColumn
nbiAckTProposedRepairAction = _NbiAckTProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 9),
    _NbiAckTProposedRepairAction_Type()
)
nbiAckTProposedRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTProposedRepairAction.setStatus("current")


class _NbiAckTAdditionalText_Type(NbiAdditionalText):
    """Custom type nbiAckTAdditionalText based on NbiAdditionalText"""
    defaultValue = OctetString("")


_NbiAckTAdditionalText_Type.__name__ = "NbiAdditionalText"
_NbiAckTAdditionalText_Object = MibTableColumn
nbiAckTAdditionalText = _NbiAckTAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 10),
    _NbiAckTAdditionalText_Type()
)
nbiAckTAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTAdditionalText.setStatus("current")
_NbiAckTAckState_Type = NbiAckState
_NbiAckTAckState_Object = MibTableColumn
nbiAckTAckState = _NbiAckTAckState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 11),
    _NbiAckTAckState_Type()
)
nbiAckTAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTAckState.setStatus("current")


class _NbiAckTAckTime_Type(NbiAckTime):
    """Custom type nbiAckTAckTime based on NbiAckTime"""
    defaultValue = OctetString("")


_NbiAckTAckTime_Type.__name__ = "NbiAckTime"
_NbiAckTAckTime_Object = MibTableColumn
nbiAckTAckTime = _NbiAckTAckTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 12),
    _NbiAckTAckTime_Type()
)
nbiAckTAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTAckTime.setStatus("current")


class _NbiAckTAckUser_Type(NbiAckUser):
    """Custom type nbiAckTAckUser based on NbiAckUser"""
    defaultValue = OctetString("")


_NbiAckTAckUser_Type.__name__ = "NbiAckUser"
_NbiAckTAckUser_Object = MibTableColumn
nbiAckTAckUser = _NbiAckTAckUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 1, 1, 13),
    _NbiAckTAckUser_Type()
)
nbiAckTAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAckTAckUser.setStatus("current")
_NbiActiveAlarmsTable_Object = MibTable
nbiActiveAlarmsTable = _NbiActiveAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    nbiActiveAlarmsTable.setStatus("current")
_NbiActiveAlarmsEntry_Object = MibTableRow
nbiActiveAlarmsEntry = _NbiActiveAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1)
)
nbiActiveAlarmsEntry.setIndexNames(
    (0, "NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiActTAlarmId"),
)
if mibBuilder.loadTexts:
    nbiActiveAlarmsEntry.setStatus("current")


class _NbiActTAlarmId_Type(NbiAlarmId):
    """Custom type nbiActTAlarmId based on NbiAlarmId"""
    defaultValue = OctetString("1")


_NbiActTAlarmId_Type.__name__ = "NbiAlarmId"
_NbiActTAlarmId_Object = MibTableColumn
nbiActTAlarmId = _NbiActTAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 1),
    _NbiActTAlarmId_Type()
)
nbiActTAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbiActTAlarmId.setStatus("current")
_NbiActTAlarmType_Type = NbiAlarmType
_NbiActTAlarmType_Object = MibTableColumn
nbiActTAlarmType = _NbiActTAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 2),
    _NbiActTAlarmType_Type()
)
nbiActTAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTAlarmType.setStatus("current")
_NbiActTObjectInstance_Type = NbiObjectInstance
_NbiActTObjectInstance_Object = MibTableColumn
nbiActTObjectInstance = _NbiActTObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 3),
    _NbiActTObjectInstance_Type()
)
nbiActTObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTObjectInstance.setStatus("current")
_NbiActTEventTime_Type = NbiEventTime
_NbiActTEventTime_Object = MibTableColumn
nbiActTEventTime = _NbiActTEventTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 4),
    _NbiActTEventTime_Type()
)
nbiActTEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTEventTime.setStatus("current")
_NbiActTAlarmTime_Type = NbiDateAndTime
_NbiActTAlarmTime_Object = MibTableColumn
nbiActTAlarmTime = _NbiActTAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 5),
    _NbiActTAlarmTime_Type()
)
nbiActTAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTAlarmTime.setStatus("current")
_NbiActTProbableCause_Type = NbiProbableCause
_NbiActTProbableCause_Object = MibTableColumn
nbiActTProbableCause = _NbiActTProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 6),
    _NbiActTProbableCause_Type()
)
nbiActTProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTProbableCause.setStatus("current")


class _NbiActTSpecificProblem_Type(NbiSpecificProblem):
    """Custom type nbiActTSpecificProblem based on NbiSpecificProblem"""
    defaultValue = OctetString("")


_NbiActTSpecificProblem_Type.__name__ = "NbiSpecificProblem"
_NbiActTSpecificProblem_Object = MibTableColumn
nbiActTSpecificProblem = _NbiActTSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 7),
    _NbiActTSpecificProblem_Type()
)
nbiActTSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTSpecificProblem.setStatus("current")


class _NbiActTPerceivedSeverity_Type(NbiPerceivedSeverity):
    """Custom type nbiActTPerceivedSeverity based on NbiPerceivedSeverity"""
    defaultValue = 6


_NbiActTPerceivedSeverity_Type.__name__ = "NbiPerceivedSeverity"
_NbiActTPerceivedSeverity_Object = MibTableColumn
nbiActTPerceivedSeverity = _NbiActTPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 8),
    _NbiActTPerceivedSeverity_Type()
)
nbiActTPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTPerceivedSeverity.setStatus("current")


class _NbiActTProposedRepairAction_Type(NbiProposedRepairAction):
    """Custom type nbiActTProposedRepairAction based on NbiProposedRepairAction"""
    defaultValue = OctetString("")


_NbiActTProposedRepairAction_Type.__name__ = "NbiProposedRepairAction"
_NbiActTProposedRepairAction_Object = MibTableColumn
nbiActTProposedRepairAction = _NbiActTProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 9),
    _NbiActTProposedRepairAction_Type()
)
nbiActTProposedRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTProposedRepairAction.setStatus("current")


class _NbiActTAdditionalText_Type(NbiAdditionalText):
    """Custom type nbiActTAdditionalText based on NbiAdditionalText"""
    defaultValue = OctetString("")


_NbiActTAdditionalText_Type.__name__ = "NbiAdditionalText"
_NbiActTAdditionalText_Object = MibTableColumn
nbiActTAdditionalText = _NbiActTAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 10),
    _NbiActTAdditionalText_Type()
)
nbiActTAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTAdditionalText.setStatus("current")
_NbiActTAckState_Type = NbiAckState
_NbiActTAckState_Object = MibTableColumn
nbiActTAckState = _NbiActTAckState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 11),
    _NbiActTAckState_Type()
)
nbiActTAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTAckState.setStatus("current")


class _NbiActTAckTime_Type(NbiAckTime):
    """Custom type nbiActTAckTime based on NbiAckTime"""
    defaultValue = OctetString("")


_NbiActTAckTime_Type.__name__ = "NbiAckTime"
_NbiActTAckTime_Object = MibTableColumn
nbiActTAckTime = _NbiActTAckTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 12),
    _NbiActTAckTime_Type()
)
nbiActTAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTAckTime.setStatus("current")


class _NbiActTAckUser_Type(NbiAckUser):
    """Custom type nbiActTAckUser based on NbiAckUser"""
    defaultValue = OctetString("")


_NbiActTAckUser_Type.__name__ = "NbiAckUser"
_NbiActTAckUser_Object = MibTableColumn
nbiActTAckUser = _NbiActTAckUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 2, 1, 13),
    _NbiActTAckUser_Type()
)
nbiActTAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActTAckUser.setStatus("current")
_NbiAllAlarmsTable_Object = MibTable
nbiAllAlarmsTable = _NbiAllAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    nbiAllAlarmsTable.setStatus("current")
_NbiAllAlarmsEntry_Object = MibTableRow
nbiAllAlarmsEntry = _NbiAllAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1)
)
nbiAllAlarmsEntry.setIndexNames(
    (0, "NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAllTAlarmId"),
)
if mibBuilder.loadTexts:
    nbiAllAlarmsEntry.setStatus("current")


class _NbiAllTAlarmId_Type(NbiAlarmId):
    """Custom type nbiAllTAlarmId based on NbiAlarmId"""
    defaultValue = OctetString("1")


_NbiAllTAlarmId_Type.__name__ = "NbiAlarmId"
_NbiAllTAlarmId_Object = MibTableColumn
nbiAllTAlarmId = _NbiAllTAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 1),
    _NbiAllTAlarmId_Type()
)
nbiAllTAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbiAllTAlarmId.setStatus("current")
_NbiAllTAlarmType_Type = NbiAlarmType
_NbiAllTAlarmType_Object = MibTableColumn
nbiAllTAlarmType = _NbiAllTAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 2),
    _NbiAllTAlarmType_Type()
)
nbiAllTAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTAlarmType.setStatus("current")
_NbiAllTObjectInstance_Type = NbiObjectInstance
_NbiAllTObjectInstance_Object = MibTableColumn
nbiAllTObjectInstance = _NbiAllTObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 3),
    _NbiAllTObjectInstance_Type()
)
nbiAllTObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTObjectInstance.setStatus("current")
_NbiAllTEventTime_Type = NbiEventTime
_NbiAllTEventTime_Object = MibTableColumn
nbiAllTEventTime = _NbiAllTEventTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 4),
    _NbiAllTEventTime_Type()
)
nbiAllTEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTEventTime.setStatus("current")
_NbiAllTAlarmTime_Type = NbiDateAndTime
_NbiAllTAlarmTime_Object = MibTableColumn
nbiAllTAlarmTime = _NbiAllTAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 5),
    _NbiAllTAlarmTime_Type()
)
nbiAllTAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTAlarmTime.setStatus("current")
_NbiAllTProbableCause_Type = NbiProbableCause
_NbiAllTProbableCause_Object = MibTableColumn
nbiAllTProbableCause = _NbiAllTProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 6),
    _NbiAllTProbableCause_Type()
)
nbiAllTProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTProbableCause.setStatus("current")


class _NbiAllTSpecificProblem_Type(NbiSpecificProblem):
    """Custom type nbiAllTSpecificProblem based on NbiSpecificProblem"""
    defaultValue = OctetString("")


_NbiAllTSpecificProblem_Type.__name__ = "NbiSpecificProblem"
_NbiAllTSpecificProblem_Object = MibTableColumn
nbiAllTSpecificProblem = _NbiAllTSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 7),
    _NbiAllTSpecificProblem_Type()
)
nbiAllTSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTSpecificProblem.setStatus("current")


class _NbiAllTPerceivedSeverity_Type(NbiPerceivedSeverity):
    """Custom type nbiAllTPerceivedSeverity based on NbiPerceivedSeverity"""
    defaultValue = 6


_NbiAllTPerceivedSeverity_Type.__name__ = "NbiPerceivedSeverity"
_NbiAllTPerceivedSeverity_Object = MibTableColumn
nbiAllTPerceivedSeverity = _NbiAllTPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 8),
    _NbiAllTPerceivedSeverity_Type()
)
nbiAllTPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTPerceivedSeverity.setStatus("current")


class _NbiAllTProposedRepairAction_Type(NbiProposedRepairAction):
    """Custom type nbiAllTProposedRepairAction based on NbiProposedRepairAction"""
    defaultValue = OctetString("")


_NbiAllTProposedRepairAction_Type.__name__ = "NbiProposedRepairAction"
_NbiAllTProposedRepairAction_Object = MibTableColumn
nbiAllTProposedRepairAction = _NbiAllTProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 9),
    _NbiAllTProposedRepairAction_Type()
)
nbiAllTProposedRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTProposedRepairAction.setStatus("current")


class _NbiAllTAdditionalText_Type(NbiAdditionalText):
    """Custom type nbiAllTAdditionalText based on NbiAdditionalText"""
    defaultValue = OctetString("")


_NbiAllTAdditionalText_Type.__name__ = "NbiAdditionalText"
_NbiAllTAdditionalText_Object = MibTableColumn
nbiAllTAdditionalText = _NbiAllTAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 10),
    _NbiAllTAdditionalText_Type()
)
nbiAllTAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTAdditionalText.setStatus("current")
_NbiAllTAckState_Type = NbiAckState
_NbiAllTAckState_Object = MibTableColumn
nbiAllTAckState = _NbiAllTAckState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 11),
    _NbiAllTAckState_Type()
)
nbiAllTAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTAckState.setStatus("current")


class _NbiAllTAckTime_Type(NbiAckTime):
    """Custom type nbiAllTAckTime based on NbiAckTime"""
    defaultValue = OctetString("")


_NbiAllTAckTime_Type.__name__ = "NbiAckTime"
_NbiAllTAckTime_Object = MibTableColumn
nbiAllTAckTime = _NbiAllTAckTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 12),
    _NbiAllTAckTime_Type()
)
nbiAllTAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTAckTime.setStatus("current")


class _NbiAllTAckUser_Type(NbiAckUser):
    """Custom type nbiAllTAckUser based on NbiAckUser"""
    defaultValue = OctetString("")


_NbiAllTAckUser_Type.__name__ = "NbiAckUser"
_NbiAllTAckUser_Object = MibTableColumn
nbiAllTAckUser = _NbiAllTAckUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 13),
    _NbiAllTAckUser_Type()
)
nbiAllTAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTAckUser.setStatus("current")


class _NbiAllTClearTime_Type(NbiClearTime):
    """Custom type nbiAllTClearTime based on NbiClearTime"""
    defaultValue = OctetString("")


_NbiAllTClearTime_Type.__name__ = "NbiClearTime"
_NbiAllTClearTime_Object = MibTableColumn
nbiAllTClearTime = _NbiAllTClearTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 14),
    _NbiAllTClearTime_Type()
)
nbiAllTClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTClearTime.setStatus("current")


class _NbiAllTClearUser_Type(NbiClearUser):
    """Custom type nbiAllTClearUser based on NbiClearUser"""
    defaultValue = OctetString("")


_NbiAllTClearUser_Type.__name__ = "NbiClearUser"
_NbiAllTClearUser_Object = MibTableColumn
nbiAllTClearUser = _NbiAllTClearUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 3, 1, 15),
    _NbiAllTClearUser_Type()
)
nbiAllTClearUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiAllTClearUser.setStatus("current")
_NbiClearedAlarmsTable_Object = MibTable
nbiClearedAlarmsTable = _NbiClearedAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    nbiClearedAlarmsTable.setStatus("current")
_NbiClearedAlarmsEntry_Object = MibTableRow
nbiClearedAlarmsEntry = _NbiClearedAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1)
)
nbiClearedAlarmsEntry.setIndexNames(
    (0, "NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCldTAlarmId"),
)
if mibBuilder.loadTexts:
    nbiClearedAlarmsEntry.setStatus("current")


class _NbiCldTAlarmId_Type(NbiAlarmId):
    """Custom type nbiCldTAlarmId based on NbiAlarmId"""
    defaultValue = OctetString("1")


_NbiCldTAlarmId_Type.__name__ = "NbiAlarmId"
_NbiCldTAlarmId_Object = MibTableColumn
nbiCldTAlarmId = _NbiCldTAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 1),
    _NbiCldTAlarmId_Type()
)
nbiCldTAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbiCldTAlarmId.setStatus("current")
_NbiCldTAlarmType_Type = NbiAlarmType
_NbiCldTAlarmType_Object = MibTableColumn
nbiCldTAlarmType = _NbiCldTAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 2),
    _NbiCldTAlarmType_Type()
)
nbiCldTAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTAlarmType.setStatus("current")
_NbiCldTObjectInstance_Type = NbiObjectInstance
_NbiCldTObjectInstance_Object = MibTableColumn
nbiCldTObjectInstance = _NbiCldTObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 3),
    _NbiCldTObjectInstance_Type()
)
nbiCldTObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTObjectInstance.setStatus("current")
_NbiCldTEventTime_Type = NbiEventTime
_NbiCldTEventTime_Object = MibTableColumn
nbiCldTEventTime = _NbiCldTEventTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 4),
    _NbiCldTEventTime_Type()
)
nbiCldTEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTEventTime.setStatus("current")
_NbiCldTAlarmTime_Type = NbiDateAndTime
_NbiCldTAlarmTime_Object = MibTableColumn
nbiCldTAlarmTime = _NbiCldTAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 5),
    _NbiCldTAlarmTime_Type()
)
nbiCldTAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTAlarmTime.setStatus("current")
_NbiCldTProbableCause_Type = NbiProbableCause
_NbiCldTProbableCause_Object = MibTableColumn
nbiCldTProbableCause = _NbiCldTProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 6),
    _NbiCldTProbableCause_Type()
)
nbiCldTProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTProbableCause.setStatus("current")


class _NbiCldTSpecificProblem_Type(NbiSpecificProblem):
    """Custom type nbiCldTSpecificProblem based on NbiSpecificProblem"""
    defaultValue = OctetString("")


_NbiCldTSpecificProblem_Type.__name__ = "NbiSpecificProblem"
_NbiCldTSpecificProblem_Object = MibTableColumn
nbiCldTSpecificProblem = _NbiCldTSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 7),
    _NbiCldTSpecificProblem_Type()
)
nbiCldTSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTSpecificProblem.setStatus("current")
_NbiCldTPerceivedSeverity_Type = NbiPerceivedSeverity
_NbiCldTPerceivedSeverity_Object = MibTableColumn
nbiCldTPerceivedSeverity = _NbiCldTPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 8),
    _NbiCldTPerceivedSeverity_Type()
)
nbiCldTPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTPerceivedSeverity.setStatus("current")


class _NbiCldTProposedRepairAction_Type(NbiProposedRepairAction):
    """Custom type nbiCldTProposedRepairAction based on NbiProposedRepairAction"""
    defaultValue = OctetString("")


_NbiCldTProposedRepairAction_Type.__name__ = "NbiProposedRepairAction"
_NbiCldTProposedRepairAction_Object = MibTableColumn
nbiCldTProposedRepairAction = _NbiCldTProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 9),
    _NbiCldTProposedRepairAction_Type()
)
nbiCldTProposedRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTProposedRepairAction.setStatus("current")


class _NbiCldTAdditionalText_Type(NbiAdditionalText):
    """Custom type nbiCldTAdditionalText based on NbiAdditionalText"""
    defaultValue = OctetString("")


_NbiCldTAdditionalText_Type.__name__ = "NbiAdditionalText"
_NbiCldTAdditionalText_Object = MibTableColumn
nbiCldTAdditionalText = _NbiCldTAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 10),
    _NbiCldTAdditionalText_Type()
)
nbiCldTAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTAdditionalText.setStatus("current")
_NbiCldTAckState_Type = NbiAckState
_NbiCldTAckState_Object = MibTableColumn
nbiCldTAckState = _NbiCldTAckState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 11),
    _NbiCldTAckState_Type()
)
nbiCldTAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTAckState.setStatus("current")


class _NbiCldTAckTime_Type(NbiAckTime):
    """Custom type nbiCldTAckTime based on NbiAckTime"""
    defaultValue = OctetString("")


_NbiCldTAckTime_Type.__name__ = "NbiAckTime"
_NbiCldTAckTime_Object = MibTableColumn
nbiCldTAckTime = _NbiCldTAckTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 12),
    _NbiCldTAckTime_Type()
)
nbiCldTAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTAckTime.setStatus("current")


class _NbiCldTAckUser_Type(NbiAckUser):
    """Custom type nbiCldTAckUser based on NbiAckUser"""
    defaultValue = OctetString("")


_NbiCldTAckUser_Type.__name__ = "NbiAckUser"
_NbiCldTAckUser_Object = MibTableColumn
nbiCldTAckUser = _NbiCldTAckUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 13),
    _NbiCldTAckUser_Type()
)
nbiCldTAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTAckUser.setStatus("current")


class _NbiCldTClearTime_Type(NbiClearTime):
    """Custom type nbiCldTClearTime based on NbiClearTime"""
    defaultValue = OctetString("")


_NbiCldTClearTime_Type.__name__ = "NbiClearTime"
_NbiCldTClearTime_Object = MibTableColumn
nbiCldTClearTime = _NbiCldTClearTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 14),
    _NbiCldTClearTime_Type()
)
nbiCldTClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTClearTime.setStatus("current")


class _NbiCldTClearUser_Type(NbiClearUser):
    """Custom type nbiCldTClearUser based on NbiClearUser"""
    defaultValue = OctetString("")


_NbiCldTClearUser_Type.__name__ = "NbiClearUser"
_NbiCldTClearUser_Object = MibTableColumn
nbiCldTClearUser = _NbiCldTClearUser_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 4, 4, 1, 15),
    _NbiCldTClearUser_Type()
)
nbiCldTClearUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiCldTClearUser.setStatus("current")
_NbiFMAlarmSummaryObjects_ObjectIdentity = ObjectIdentity
nbiFMAlarmSummaryObjects = _NbiFMAlarmSummaryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5)
)


class _NbiAlarmSummaryPeriod_Type(NbiSupervisionPeriod):
    """Custom type nbiAlarmSummaryPeriod based on NbiSupervisionPeriod"""
    defaultValue = 20


_NbiAlarmSummaryPeriod_Type.__name__ = "NbiSupervisionPeriod"
_NbiAlarmSummaryPeriod_Object = MibScalar
nbiAlarmSummaryPeriod = _NbiAlarmSummaryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 1),
    _NbiAlarmSummaryPeriod_Type()
)
nbiAlarmSummaryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiAlarmSummaryPeriod.setStatus("current")
_NbiGetAlarmSummary_Type = TruthValue
_NbiGetAlarmSummary_Object = MibScalar
nbiGetAlarmSummary = _NbiGetAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 2),
    _NbiGetAlarmSummary_Type()
)
nbiGetAlarmSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiGetAlarmSummary.setStatus("current")
_NbiNumberClearedAlarms_Type = NbiNumberOfAlarms
_NbiNumberClearedAlarms_Object = MibScalar
nbiNumberClearedAlarms = _NbiNumberClearedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 3),
    _NbiNumberClearedAlarms_Type()
)
nbiNumberClearedAlarms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNumberClearedAlarms.setStatus("current")
_NbiNumberCriticalAlarms_Type = NbiNumberOfAlarms
_NbiNumberCriticalAlarms_Object = MibScalar
nbiNumberCriticalAlarms = _NbiNumberCriticalAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 4),
    _NbiNumberCriticalAlarms_Type()
)
nbiNumberCriticalAlarms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNumberCriticalAlarms.setStatus("current")
_NbiNumberIndeterminateAlarms_Type = NbiNumberOfAlarms
_NbiNumberIndeterminateAlarms_Object = MibScalar
nbiNumberIndeterminateAlarms = _NbiNumberIndeterminateAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 5),
    _NbiNumberIndeterminateAlarms_Type()
)
nbiNumberIndeterminateAlarms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNumberIndeterminateAlarms.setStatus("current")
_NbiNumberMajorAlarms_Type = NbiNumberOfAlarms
_NbiNumberMajorAlarms_Object = MibScalar
nbiNumberMajorAlarms = _NbiNumberMajorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 6),
    _NbiNumberMajorAlarms_Type()
)
nbiNumberMajorAlarms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNumberMajorAlarms.setStatus("current")
_NbiNumberMinorAlarms_Type = NbiNumberOfAlarms
_NbiNumberMinorAlarms_Object = MibScalar
nbiNumberMinorAlarms = _NbiNumberMinorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 7),
    _NbiNumberMinorAlarms_Type()
)
nbiNumberMinorAlarms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNumberMinorAlarms.setStatus("current")
_NbiNumberWarningAlarms_Type = NbiNumberOfAlarms
_NbiNumberWarningAlarms_Object = MibScalar
nbiNumberWarningAlarms = _NbiNumberWarningAlarms_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 1, 5, 8),
    _NbiNumberWarningAlarms_Type()
)
nbiNumberWarningAlarms.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNumberWarningAlarms.setStatus("current")
_NbiFMConformance_ObjectIdentity = ObjectIdentity
nbiFMConformance = _NbiFMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2)
)
_NbiFMCompliances_ObjectIdentity = ObjectIdentity
nbiFMCompliances = _NbiFMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 1)
)
_NbiFMGroups_ObjectIdentity = ObjectIdentity
nbiFMGroups = _NbiFMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2)
)

# Managed Objects groups

nbiFMAlarmParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 1)
)
nbiFMAlarmParameterGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearUser"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiSpecificProblem"))
)
if mibBuilder.loadTexts:
    nbiFMAlarmParameterGroup.setStatus("current")

nbiFMAlarmHandlingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 2)
)
nbiFMAlarmHandlingGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmIdList"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAcknowledgeAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearAlarms"))
)
if mibBuilder.loadTexts:
    nbiFMAlarmHandlingGroup.setStatus("current")

nbiFMSynchronizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 3)
)
nbiFMSynchronizationGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiGetAckAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiGetActiveAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiGetAllAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiGetClearedAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiGetAlarmsByStartingTime"))
)
if mibBuilder.loadTexts:
    nbiFMSynchronizationGroup.setStatus("current")

nbiFMAlarmSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 4)
)
nbiFMAlarmSummaryGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmSummaryPeriod"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiGetAlarmSummary"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberClearedAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberCriticalAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberIndeterminateAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberMajorAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberMinorAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberWarningAlarms"))
)
if mibBuilder.loadTexts:
    nbiFMAlarmSummaryGroup.setStatus("current")

nbiFMConditionalParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 6)
)
nbiFMConditionalParameterGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckState"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckUser"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAdditionalText"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearUser"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentText"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentUser"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProposedRepairAction"))
)
if mibBuilder.loadTexts:
    nbiFMConditionalParameterGroup.setStatus("current")

nbiFMOptionalAlarmHandlingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 7)
)
nbiFMOptionalAlarmHandlingGroup.setObjects(
    ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentAlarms")
)
if mibBuilder.loadTexts:
    nbiFMOptionalAlarmHandlingGroup.setStatus("current")


# Notification objects

nbiAlarmNewNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 1, 1)
)
nbiAlarmNewNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiSpecificProblem"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProposedRepairAction"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAdditionalText"))
)
if mibBuilder.loadTexts:
    nbiAlarmNewNotification.setStatus(
        "current"
    )

nbiAlarmAckChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 1, 2)
)
nbiAlarmAckChangedNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckState"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckUser"))
)
if mibBuilder.loadTexts:
    nbiAlarmAckChangedNotification.setStatus(
        "current"
    )

nbiAlarmSeverityChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 1, 3)
)
nbiAlarmSeverityChangedNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"))
)
if mibBuilder.loadTexts:
    nbiAlarmSeverityChangedNotification.setStatus(
        "current"
    )

nbiAlarmCommentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 1, 4)
)
nbiAlarmCommentNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentText"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiCommentUser"))
)
if mibBuilder.loadTexts:
    nbiAlarmCommentNotification.setStatus(
        "current"
    )

nbiAlarmClearedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 1, 5)
)
nbiAlarmClearedNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearUser"))
)
if mibBuilder.loadTexts:
    nbiAlarmClearedNotification.setStatus(
        "current"
    )

nbiAlarmSyncNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 2, 1)
)
nbiAlarmSyncNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmId"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProbableCause"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiSpecificProblem"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiPerceivedSeverity"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiProposedRepairAction"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAdditionalText"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckState"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAckUser"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearTime"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiClearUser"))
)
if mibBuilder.loadTexts:
    nbiAlarmSyncNotification.setStatus(
        "current"
    )

nbiAlarmSummaryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 0, 2, 2)
)
nbiAlarmSummaryNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEmsSynchronizationState"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNotSyncNEs"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberCriticalAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberMajorAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberMinorAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberWarningAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberClearedAlarms"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiNumberIndeterminateAlarms"))
)
if mibBuilder.loadTexts:
    nbiAlarmSummaryNotification.setStatus(
        "current"
    )


# Notifications groups

nbiFMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 5)
)
nbiFMNotificationGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmNewNotification"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmAckChangedNotification"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmClearedNotification"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmSyncNotification"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmSummaryNotification"))
)
if mibBuilder.loadTexts:
    nbiFMNotificationGroup.setStatus(
        "current"
    )

nbiFMOptionalNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 2, 8)
)
nbiFMOptionalNotificationGroup.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmSeverityChangedNotification"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiAlarmCommentNotification"))
)
if mibBuilder.loadTexts:
    nbiFMOptionalNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nbiFMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 3, 2, 1, 1)
)
nbiFMCompliance.setObjects(
      *(("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMAlarmParameterGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMAlarmHandlingGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMSynchronizationGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMAlarmSummaryGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMNotificationGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMConditionalParameterGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMOptionalAlarmHandlingGroup"),
        ("NSN-SNMP-NBI-FAULTMANAGEMENT-MIB", "nbiFMOptionalNotificationGroup"))
)
if mibBuilder.loadTexts:
    nbiFMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSN-SNMP-NBI-FAULTMANAGEMENT-MIB",
    **{"nbiFaultManagementMIB": nbiFaultManagementMIB,
       "nbiFMNotifications": nbiFMNotifications,
       "nbiFMSpontaneousNotifications": nbiFMSpontaneousNotifications,
       "nbiAlarmNewNotification": nbiAlarmNewNotification,
       "nbiAlarmAckChangedNotification": nbiAlarmAckChangedNotification,
       "nbiAlarmSeverityChangedNotification": nbiAlarmSeverityChangedNotification,
       "nbiAlarmCommentNotification": nbiAlarmCommentNotification,
       "nbiAlarmClearedNotification": nbiAlarmClearedNotification,
       "nbiFMOtherNotifications": nbiFMOtherNotifications,
       "nbiAlarmSyncNotification": nbiAlarmSyncNotification,
       "nbiAlarmSummaryNotification": nbiAlarmSummaryNotification,
       "nbiFMObjects": nbiFMObjects,
       "nbiFMAlarmParameterObjects": nbiFMAlarmParameterObjects,
       "nbiAckState": nbiAckState,
       "nbiAckTime": nbiAckTime,
       "nbiAckUser": nbiAckUser,
       "nbiAdditionalText": nbiAdditionalText,
       "nbiAlarmId": nbiAlarmId,
       "nbiAlarmTime": nbiAlarmTime,
       "nbiAlarmType": nbiAlarmType,
       "nbiClearTime": nbiClearTime,
       "nbiClearUser": nbiClearUser,
       "nbiCommentText": nbiCommentText,
       "nbiCommentTime": nbiCommentTime,
       "nbiCommentUser": nbiCommentUser,
       "nbiPerceivedSeverity": nbiPerceivedSeverity,
       "nbiProbableCause": nbiProbableCause,
       "nbiProposedRepairAction": nbiProposedRepairAction,
       "nbiSpecificProblem": nbiSpecificProblem,
       "nbiFMAlarmHandlingObjects": nbiFMAlarmHandlingObjects,
       "nbiAlarmIdList": nbiAlarmIdList,
       "nbiAcknowledgeAlarms": nbiAcknowledgeAlarms,
       "nbiClearAlarms": nbiClearAlarms,
       "nbiCommentAlarms": nbiCommentAlarms,
       "nbiUnacknowledgeAlarms": nbiUnacknowledgeAlarms,
       "nbiFMSynchSingleNMSObjects": nbiFMSynchSingleNMSObjects,
       "nbiGetAckAlarms": nbiGetAckAlarms,
       "nbiGetActiveAlarms": nbiGetActiveAlarms,
       "nbiGetAllAlarms": nbiGetAllAlarms,
       "nbiGetClearedAlarms": nbiGetClearedAlarms,
       "nbiGetAlarmsByStartingTime": nbiGetAlarmsByStartingTime,
       "nbiFMSynchMultipleNMSObjects": nbiFMSynchMultipleNMSObjects,
       "nbiAckAlarmsTable": nbiAckAlarmsTable,
       "nbiAckAlarmsEntry": nbiAckAlarmsEntry,
       "nbiAckTAlarmId": nbiAckTAlarmId,
       "nbiAckTAlarmType": nbiAckTAlarmType,
       "nbiAckTObjectInstance": nbiAckTObjectInstance,
       "nbiAckTEventTime": nbiAckTEventTime,
       "nbiAckTAlarmTime": nbiAckTAlarmTime,
       "nbiAckTProbableCause": nbiAckTProbableCause,
       "nbiAckTSpecificProblem": nbiAckTSpecificProblem,
       "nbiAckTPerceivedSeverity": nbiAckTPerceivedSeverity,
       "nbiAckTProposedRepairAction": nbiAckTProposedRepairAction,
       "nbiAckTAdditionalText": nbiAckTAdditionalText,
       "nbiAckTAckState": nbiAckTAckState,
       "nbiAckTAckTime": nbiAckTAckTime,
       "nbiAckTAckUser": nbiAckTAckUser,
       "nbiActiveAlarmsTable": nbiActiveAlarmsTable,
       "nbiActiveAlarmsEntry": nbiActiveAlarmsEntry,
       "nbiActTAlarmId": nbiActTAlarmId,
       "nbiActTAlarmType": nbiActTAlarmType,
       "nbiActTObjectInstance": nbiActTObjectInstance,
       "nbiActTEventTime": nbiActTEventTime,
       "nbiActTAlarmTime": nbiActTAlarmTime,
       "nbiActTProbableCause": nbiActTProbableCause,
       "nbiActTSpecificProblem": nbiActTSpecificProblem,
       "nbiActTPerceivedSeverity": nbiActTPerceivedSeverity,
       "nbiActTProposedRepairAction": nbiActTProposedRepairAction,
       "nbiActTAdditionalText": nbiActTAdditionalText,
       "nbiActTAckState": nbiActTAckState,
       "nbiActTAckTime": nbiActTAckTime,
       "nbiActTAckUser": nbiActTAckUser,
       "nbiAllAlarmsTable": nbiAllAlarmsTable,
       "nbiAllAlarmsEntry": nbiAllAlarmsEntry,
       "nbiAllTAlarmId": nbiAllTAlarmId,
       "nbiAllTAlarmType": nbiAllTAlarmType,
       "nbiAllTObjectInstance": nbiAllTObjectInstance,
       "nbiAllTEventTime": nbiAllTEventTime,
       "nbiAllTAlarmTime": nbiAllTAlarmTime,
       "nbiAllTProbableCause": nbiAllTProbableCause,
       "nbiAllTSpecificProblem": nbiAllTSpecificProblem,
       "nbiAllTPerceivedSeverity": nbiAllTPerceivedSeverity,
       "nbiAllTProposedRepairAction": nbiAllTProposedRepairAction,
       "nbiAllTAdditionalText": nbiAllTAdditionalText,
       "nbiAllTAckState": nbiAllTAckState,
       "nbiAllTAckTime": nbiAllTAckTime,
       "nbiAllTAckUser": nbiAllTAckUser,
       "nbiAllTClearTime": nbiAllTClearTime,
       "nbiAllTClearUser": nbiAllTClearUser,
       "nbiClearedAlarmsTable": nbiClearedAlarmsTable,
       "nbiClearedAlarmsEntry": nbiClearedAlarmsEntry,
       "nbiCldTAlarmId": nbiCldTAlarmId,
       "nbiCldTAlarmType": nbiCldTAlarmType,
       "nbiCldTObjectInstance": nbiCldTObjectInstance,
       "nbiCldTEventTime": nbiCldTEventTime,
       "nbiCldTAlarmTime": nbiCldTAlarmTime,
       "nbiCldTProbableCause": nbiCldTProbableCause,
       "nbiCldTSpecificProblem": nbiCldTSpecificProblem,
       "nbiCldTPerceivedSeverity": nbiCldTPerceivedSeverity,
       "nbiCldTProposedRepairAction": nbiCldTProposedRepairAction,
       "nbiCldTAdditionalText": nbiCldTAdditionalText,
       "nbiCldTAckState": nbiCldTAckState,
       "nbiCldTAckTime": nbiCldTAckTime,
       "nbiCldTAckUser": nbiCldTAckUser,
       "nbiCldTClearTime": nbiCldTClearTime,
       "nbiCldTClearUser": nbiCldTClearUser,
       "nbiFMAlarmSummaryObjects": nbiFMAlarmSummaryObjects,
       "nbiAlarmSummaryPeriod": nbiAlarmSummaryPeriod,
       "nbiGetAlarmSummary": nbiGetAlarmSummary,
       "nbiNumberClearedAlarms": nbiNumberClearedAlarms,
       "nbiNumberCriticalAlarms": nbiNumberCriticalAlarms,
       "nbiNumberIndeterminateAlarms": nbiNumberIndeterminateAlarms,
       "nbiNumberMajorAlarms": nbiNumberMajorAlarms,
       "nbiNumberMinorAlarms": nbiNumberMinorAlarms,
       "nbiNumberWarningAlarms": nbiNumberWarningAlarms,
       "nbiFMConformance": nbiFMConformance,
       "nbiFMCompliances": nbiFMCompliances,
       "nbiFMCompliance": nbiFMCompliance,
       "nbiFMGroups": nbiFMGroups,
       "nbiFMAlarmParameterGroup": nbiFMAlarmParameterGroup,
       "nbiFMAlarmHandlingGroup": nbiFMAlarmHandlingGroup,
       "nbiFMSynchronizationGroup": nbiFMSynchronizationGroup,
       "nbiFMAlarmSummaryGroup": nbiFMAlarmSummaryGroup,
       "nbiFMNotificationGroup": nbiFMNotificationGroup,
       "nbiFMConditionalParameterGroup": nbiFMConditionalParameterGroup,
       "nbiFMOptionalAlarmHandlingGroup": nbiFMOptionalAlarmHandlingGroup,
       "nbiFMOptionalNotificationGroup": nbiFMOptionalNotificationGroup}
)
