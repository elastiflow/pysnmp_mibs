# SNMP MIB module (NSN-SNMP-NBI-COMMONFUNCTIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_28458/NSN-SNMP-NBI-COMMONFUNCTIONS-MIB.mib
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

(nbiNetActSnmp,) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-REGISTRATION-MIB",
    "nbiNetActSnmp")

(NbiActiveInterfaceVersion,
 NbiChangedPeriodType,
 NbiEmsSynchronizationState,
 NbiEventTime,
 NbiEventTypeFilter,
 NbiFailureReason,
 NbiIpAddress,
 NbiNmsName,
 NbiNoOfResponseTraps,
 NbiNotSyncNEs,
 NbiObjectInstance,
 NbiObjectInstanceFilter,
 NbiPortNumber,
 NbiProcessingStatus,
 NbiRetransmitTrapIds,
 NbiRetransmitTrapType,
 NbiSequenceId,
 NbiSeverityFilter,
 NbiSupervisionPeriod,
 NbiUserLabel) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-TEXTUALCONVENTIONS-MIB",
    "NbiActiveInterfaceVersion",
    "NbiChangedPeriodType",
    "NbiEmsSynchronizationState",
    "NbiEventTime",
    "NbiEventTypeFilter",
    "NbiFailureReason",
    "NbiIpAddress",
    "NbiNmsName",
    "NbiNoOfResponseTraps",
    "NbiNotSyncNEs",
    "NbiObjectInstance",
    "NbiObjectInstanceFilter",
    "NbiPortNumber",
    "NbiProcessingStatus",
    "NbiRetransmitTrapIds",
    "NbiRetransmitTrapType",
    "NbiSequenceId",
    "NbiSeverityFilter",
    "NbiSupervisionPeriod",
    "NbiUserLabel")

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

nbiCommonFunctionsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2)
)
if mibBuilder.loadTexts:
    nbiCommonFunctionsMIB.setRevisions(
        ("2011-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbiCommonNotifications_ObjectIdentity = ObjectIdentity
nbiCommonNotifications = _NbiCommonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0)
)
_NbiControlNotifications_ObjectIdentity = ObjectIdentity
nbiControlNotifications = _NbiControlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 1)
)
_NbiReliableReportingNotifications_ObjectIdentity = ObjectIdentity
nbiReliableReportingNotifications = _NbiReliableReportingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 2)
)
_NbiCommonObjects_ObjectIdentity = ObjectIdentity
nbiCommonObjects = _NbiCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1)
)
_NbiRegistrationObjects_ObjectIdentity = ObjectIdentity
nbiRegistrationObjects = _NbiRegistrationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1)
)
_NbiNmsRegistrationTable_Object = MibTable
nbiNmsRegistrationTable = _NbiNmsRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nbiNmsRegistrationTable.setStatus("current")
_NbiNmsRegistrationEntry_Object = MibTableRow
nbiNmsRegistrationEntry = _NbiNmsRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1)
)
nbiNmsRegistrationEntry.setIndexNames(
    (1, "NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNmsRegistrationIndex"),
)
if mibBuilder.loadTexts:
    nbiNmsRegistrationEntry.setStatus("current")
_NbiNmsRegistrationIndex_Type = NbiNmsName
_NbiNmsRegistrationIndex_Object = MibTableColumn
nbiNmsRegistrationIndex = _NbiNmsRegistrationIndex_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 1),
    _NbiNmsRegistrationIndex_Type()
)
nbiNmsRegistrationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbiNmsRegistrationIndex.setStatus("current")
_NbiNmsIpAddress_Type = NbiIpAddress
_NbiNmsIpAddress_Object = MibTableColumn
nbiNmsIpAddress = _NbiNmsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 2),
    _NbiNmsIpAddress_Type()
)
nbiNmsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNmsIpAddress.setStatus("current")
_NbiTrapPortNumber_Type = NbiPortNumber
_NbiTrapPortNumber_Object = MibTableColumn
nbiTrapPortNumber = _NbiTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 3),
    _NbiTrapPortNumber_Type()
)
nbiTrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiTrapPortNumber.setStatus("current")
_NbiActiveInterfaceVersion_Type = NbiActiveInterfaceVersion
_NbiActiveInterfaceVersion_Object = MibTableColumn
nbiActiveInterfaceVersion = _NbiActiveInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 4),
    _NbiActiveInterfaceVersion_Type()
)
nbiActiveInterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiActiveInterfaceVersion.setStatus("current")


class _NbiEventTypeFilter_Type(NbiEventTypeFilter):
    """Custom type nbiEventTypeFilter based on NbiEventTypeFilter"""
    defaultBinValue = "1"


_NbiEventTypeFilter_Type.__name__ = "NbiEventTypeFilter"
_NbiEventTypeFilter_Object = MibTableColumn
nbiEventTypeFilter = _NbiEventTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 5),
    _NbiEventTypeFilter_Type()
)
nbiEventTypeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbiEventTypeFilter.setStatus("current")


class _NbiObjectInstanceFilter_Type(NbiObjectInstanceFilter):
    """Custom type nbiObjectInstanceFilter based on NbiObjectInstanceFilter"""
    defaultValue = OctetString("")


_NbiObjectInstanceFilter_Type.__name__ = "NbiObjectInstanceFilter"
_NbiObjectInstanceFilter_Object = MibTableColumn
nbiObjectInstanceFilter = _NbiObjectInstanceFilter_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 6),
    _NbiObjectInstanceFilter_Type()
)
nbiObjectInstanceFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbiObjectInstanceFilter.setStatus("current")


class _NbiSeverityFilter_Type(NbiSeverityFilter):
    """Custom type nbiSeverityFilter based on NbiSeverityFilter"""
    defaultBinValue = "01"


_NbiSeverityFilter_Type.__name__ = "NbiSeverityFilter"
_NbiSeverityFilter_Object = MibTableColumn
nbiSeverityFilter = _NbiSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 7),
    _NbiSeverityFilter_Type()
)
nbiSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbiSeverityFilter.setStatus("current")
_NbiNewestSequenceId_Type = NbiSequenceId
_NbiNewestSequenceId_Object = MibTableColumn
nbiNewestSequenceId = _NbiNewestSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 8),
    _NbiNewestSequenceId_Type()
)
nbiNewestSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiNewestSequenceId.setStatus("current")
_NbiOldestSequenceId_Type = NbiSequenceId
_NbiOldestSequenceId_Object = MibTableColumn
nbiOldestSequenceId = _NbiOldestSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 1, 1, 1, 9),
    _NbiOldestSequenceId_Type()
)
nbiOldestSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbiOldestSequenceId.setStatus("current")
_NbiControlObjects_ObjectIdentity = ObjectIdentity
nbiControlObjects = _NbiControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 2)
)


class _NbiHeartbeatPeriod_Type(NbiSupervisionPeriod):
    """Custom type nbiHeartbeatPeriod based on NbiSupervisionPeriod"""
    defaultValue = 5


_NbiHeartbeatPeriod_Type.__name__ = "NbiSupervisionPeriod"
_NbiHeartbeatPeriod_Object = MibScalar
nbiHeartbeatPeriod = _NbiHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 2, 1),
    _NbiHeartbeatPeriod_Type()
)
nbiHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiHeartbeatPeriod.setStatus("current")
_NbiReliableReportingObjects_ObjectIdentity = ObjectIdentity
nbiReliableReportingObjects = _NbiReliableReportingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3)
)
_NbiFailureReason_Type = NbiFailureReason
_NbiFailureReason_Object = MibScalar
nbiFailureReason = _NbiFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 1),
    _NbiFailureReason_Type()
)
nbiFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiFailureReason.setStatus("current")
_NbiNoOfResponseTraps_Type = NbiNoOfResponseTraps
_NbiNoOfResponseTraps_Object = MibScalar
nbiNoOfResponseTraps = _NbiNoOfResponseTraps_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 2),
    _NbiNoOfResponseTraps_Type()
)
nbiNoOfResponseTraps.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNoOfResponseTraps.setStatus("current")
_NbiNmsName_Type = NbiNmsName
_NbiNmsName_Object = MibScalar
nbiNmsName = _NbiNmsName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 3),
    _NbiNmsName_Type()
)
nbiNmsName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNmsName.setStatus("current")


class _NbiProcessingStatus_Type(NbiProcessingStatus):
    """Custom type nbiProcessingStatus based on NbiProcessingStatus"""
    defaultValue = 1


_NbiProcessingStatus_Type.__name__ = "NbiProcessingStatus"
_NbiProcessingStatus_Object = MibScalar
nbiProcessingStatus = _NbiProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 4),
    _NbiProcessingStatus_Type()
)
nbiProcessingStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiProcessingStatus.setStatus("current")
_NbiRetransmitTrapIds_Type = NbiRetransmitTrapIds
_NbiRetransmitTrapIds_Object = MibScalar
nbiRetransmitTrapIds = _NbiRetransmitTrapIds_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 5),
    _NbiRetransmitTrapIds_Type()
)
nbiRetransmitTrapIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiRetransmitTrapIds.setStatus("current")
_NbiRetransmitTrapType_Type = NbiRetransmitTrapType
_NbiRetransmitTrapType_Object = MibScalar
nbiRetransmitTrapType = _NbiRetransmitTrapType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 6),
    _NbiRetransmitTrapType_Type()
)
nbiRetransmitTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiRetransmitTrapType.setStatus("current")
_NbiSequenceId_Type = NbiSequenceId
_NbiSequenceId_Object = MibScalar
nbiSequenceId = _NbiSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 3, 7),
    _NbiSequenceId_Type()
)
nbiSequenceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiSequenceId.setStatus("current")
_NbiCommonGeneralOptionalObjects_ObjectIdentity = ObjectIdentity
nbiCommonGeneralOptionalObjects = _NbiCommonGeneralOptionalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 5)
)
_NbiRequestingNmsName_Type = NbiNmsName
_NbiRequestingNmsName_Object = MibScalar
nbiRequestingNmsName = _NbiRequestingNmsName_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 5, 1),
    _NbiRequestingNmsName_Type()
)
nbiRequestingNmsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbiRequestingNmsName.setStatus("current")
_NbiUserLabel_Type = NbiUserLabel
_NbiUserLabel_Object = MibScalar
nbiUserLabel = _NbiUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 5, 2),
    _NbiUserLabel_Type()
)
nbiUserLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiUserLabel.setStatus("current")
_NbiCommonGeneralMandatoryObjects_ObjectIdentity = ObjectIdentity
nbiCommonGeneralMandatoryObjects = _NbiCommonGeneralMandatoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6)
)
_NbiChangedPeriodType_Type = NbiChangedPeriodType
_NbiChangedPeriodType_Object = MibScalar
nbiChangedPeriodType = _NbiChangedPeriodType_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6, 1),
    _NbiChangedPeriodType_Type()
)
nbiChangedPeriodType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiChangedPeriodType.setStatus("current")
_NbiEmsSynchronizationState_Type = NbiEmsSynchronizationState
_NbiEmsSynchronizationState_Object = MibScalar
nbiEmsSynchronizationState = _NbiEmsSynchronizationState_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6, 2),
    _NbiEmsSynchronizationState_Type()
)
nbiEmsSynchronizationState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiEmsSynchronizationState.setStatus("current")
_NbiEventTime_Type = NbiEventTime
_NbiEventTime_Object = MibScalar
nbiEventTime = _NbiEventTime_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6, 3),
    _NbiEventTime_Type()
)
nbiEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiEventTime.setStatus("current")


class _NbiNotSyncNEs_Type(NbiNotSyncNEs):
    """Custom type nbiNotSyncNEs based on NbiNotSyncNEs"""
    defaultValue = OctetString("")


_NbiNotSyncNEs_Type.__name__ = "NbiNotSyncNEs"
_NbiNotSyncNEs_Object = MibScalar
nbiNotSyncNEs = _NbiNotSyncNEs_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6, 4),
    _NbiNotSyncNEs_Type()
)
nbiNotSyncNEs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiNotSyncNEs.setStatus("current")
_NbiObjectInstance_Type = NbiObjectInstance
_NbiObjectInstance_Object = MibScalar
nbiObjectInstance = _NbiObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6, 5),
    _NbiObjectInstance_Type()
)
nbiObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiObjectInstance.setStatus("current")
_NbiSupervisionPeriod_Type = NbiSupervisionPeriod
_NbiSupervisionPeriod_Object = MibScalar
nbiSupervisionPeriod = _NbiSupervisionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 1, 6, 6),
    _NbiSupervisionPeriod_Type()
)
nbiSupervisionPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbiSupervisionPeriod.setStatus("current")
_NbiCommonConformance_ObjectIdentity = ObjectIdentity
nbiCommonConformance = _NbiCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2)
)
_NbiCommonCompliances_ObjectIdentity = ObjectIdentity
nbiCommonCompliances = _NbiCommonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 1)
)
_NbiCommonGroups_ObjectIdentity = ObjectIdentity
nbiCommonGroups = _NbiCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2)
)

# Managed Objects groups

nbiCommonNBIControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 1)
)
nbiCommonNBIControlGroup.setObjects(
    ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiHeartbeatPeriod")
)
if mibBuilder.loadTexts:
    nbiCommonNBIControlGroup.setStatus("current")

nbiCommonReliableReportingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 2)
)
nbiCommonReliableReportingGroup.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNewestSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiOldestSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiFailureReason"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNmsName"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNoOfResponseTraps"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiProcessingStatus"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiRetransmitTrapIds"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiRetransmitTrapType"))
)
if mibBuilder.loadTexts:
    nbiCommonReliableReportingGroup.setStatus("current")

nbiCommonGeneralMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 3)
)
nbiCommonGeneralMandatoryGroup.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEmsSynchronizationState"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSupervisionPeriod"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstance"))
)
if mibBuilder.loadTexts:
    nbiCommonGeneralMandatoryGroup.setStatus("current")

nbiCommonNBIVersionOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 6)
)
nbiCommonNBIVersionOptionalGroup.setObjects(
    ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiActiveInterfaceVersion")
)
if mibBuilder.loadTexts:
    nbiCommonNBIVersionOptionalGroup.setStatus("current")

nbiCommonFilterSettingsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 7)
)
nbiCommonFilterSettingsOptionalGroup.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTypeFilter"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiObjectInstanceFilter"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSeverityFilter"))
)
if mibBuilder.loadTexts:
    nbiCommonFilterSettingsOptionalGroup.setStatus("current")

nbiCommonGeneralOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 8)
)
nbiCommonGeneralOptionalGroup.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNotSyncNEs"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiRequestingNmsName"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiUserLabel"))
)
if mibBuilder.loadTexts:
    nbiCommonGeneralOptionalGroup.setStatus("current")


# Notification objects

nbiChangedPeriodNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 1, 1)
)
nbiChangedPeriodNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiChangedPeriodType"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSupervisionPeriod"))
)
if mibBuilder.loadTexts:
    nbiChangedPeriodNotification.setStatus(
        "current"
    )

nbiHeartbeatNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 1, 2)
)
nbiHeartbeatNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"))
)
if mibBuilder.loadTexts:
    nbiHeartbeatNotification.setStatus(
        "current"
    )

nbiStartUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 1, 3)
)
nbiStartUpNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"))
)
if mibBuilder.loadTexts:
    nbiStartUpNotification.setStatus(
        "current"
    )

nbiShutDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 1, 4)
)
nbiShutDownNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"))
)
if mibBuilder.loadTexts:
    nbiShutDownNotification.setStatus(
        "current"
    )

nbiEndOfSequenceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 0, 2, 1)
)
nbiEndOfSequenceNotification.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiSequenceId"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEventTime"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiProcessingStatus"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNmsName"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiNoOfResponseTraps"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiFailureReason"))
)
if mibBuilder.loadTexts:
    nbiEndOfSequenceNotification.setStatus(
        "current"
    )


# Notifications groups

nbiCommonNotificationControlGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 4)
)
nbiCommonNotificationControlGroup.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiChangedPeriodNotification"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiHeartbeatNotification"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiStartUpNotification"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiShutDownNotification"))
)
if mibBuilder.loadTexts:
    nbiCommonNotificationControlGroup.setStatus(
        "current"
    )

nbiCommonReliableNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 2, 5)
)
nbiCommonReliableNotificationGroup.setObjects(
    ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiEndOfSequenceNotification")
)
if mibBuilder.loadTexts:
    nbiCommonReliableNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nbiCommonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 2, 2, 1, 1)
)
nbiCommonCompliance.setObjects(
      *(("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonNBIControlGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonReliableReportingGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonGeneralMandatoryGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonNotificationControlGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonReliableNotificationGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonNBIVersionOptionalGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonFilterSettingsOptionalGroup"),
        ("NSN-SNMP-NBI-COMMONFUNCTIONS-MIB", "nbiCommonGeneralOptionalGroup"))
)
if mibBuilder.loadTexts:
    nbiCommonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSN-SNMP-NBI-COMMONFUNCTIONS-MIB",
    **{"nbiCommonFunctionsMIB": nbiCommonFunctionsMIB,
       "nbiCommonNotifications": nbiCommonNotifications,
       "nbiControlNotifications": nbiControlNotifications,
       "nbiChangedPeriodNotification": nbiChangedPeriodNotification,
       "nbiHeartbeatNotification": nbiHeartbeatNotification,
       "nbiStartUpNotification": nbiStartUpNotification,
       "nbiShutDownNotification": nbiShutDownNotification,
       "nbiReliableReportingNotifications": nbiReliableReportingNotifications,
       "nbiEndOfSequenceNotification": nbiEndOfSequenceNotification,
       "nbiCommonObjects": nbiCommonObjects,
       "nbiRegistrationObjects": nbiRegistrationObjects,
       "nbiNmsRegistrationTable": nbiNmsRegistrationTable,
       "nbiNmsRegistrationEntry": nbiNmsRegistrationEntry,
       "nbiNmsRegistrationIndex": nbiNmsRegistrationIndex,
       "nbiNmsIpAddress": nbiNmsIpAddress,
       "nbiTrapPortNumber": nbiTrapPortNumber,
       "nbiActiveInterfaceVersion": nbiActiveInterfaceVersion,
       "nbiEventTypeFilter": nbiEventTypeFilter,
       "nbiObjectInstanceFilter": nbiObjectInstanceFilter,
       "nbiSeverityFilter": nbiSeverityFilter,
       "nbiNewestSequenceId": nbiNewestSequenceId,
       "nbiOldestSequenceId": nbiOldestSequenceId,
       "nbiControlObjects": nbiControlObjects,
       "nbiHeartbeatPeriod": nbiHeartbeatPeriod,
       "nbiReliableReportingObjects": nbiReliableReportingObjects,
       "nbiFailureReason": nbiFailureReason,
       "nbiNoOfResponseTraps": nbiNoOfResponseTraps,
       "nbiNmsName": nbiNmsName,
       "nbiProcessingStatus": nbiProcessingStatus,
       "nbiRetransmitTrapIds": nbiRetransmitTrapIds,
       "nbiRetransmitTrapType": nbiRetransmitTrapType,
       "nbiSequenceId": nbiSequenceId,
       "nbiCommonGeneralOptionalObjects": nbiCommonGeneralOptionalObjects,
       "nbiRequestingNmsName": nbiRequestingNmsName,
       "nbiUserLabel": nbiUserLabel,
       "nbiCommonGeneralMandatoryObjects": nbiCommonGeneralMandatoryObjects,
       "nbiChangedPeriodType": nbiChangedPeriodType,
       "nbiEmsSynchronizationState": nbiEmsSynchronizationState,
       "nbiEventTime": nbiEventTime,
       "nbiNotSyncNEs": nbiNotSyncNEs,
       "nbiObjectInstance": nbiObjectInstance,
       "nbiSupervisionPeriod": nbiSupervisionPeriod,
       "nbiCommonConformance": nbiCommonConformance,
       "nbiCommonCompliances": nbiCommonCompliances,
       "nbiCommonCompliance": nbiCommonCompliance,
       "nbiCommonGroups": nbiCommonGroups,
       "nbiCommonNBIControlGroup": nbiCommonNBIControlGroup,
       "nbiCommonReliableReportingGroup": nbiCommonReliableReportingGroup,
       "nbiCommonGeneralMandatoryGroup": nbiCommonGeneralMandatoryGroup,
       "nbiCommonNotificationControlGroup": nbiCommonNotificationControlGroup,
       "nbiCommonReliableNotificationGroup": nbiCommonReliableNotificationGroup,
       "nbiCommonNBIVersionOptionalGroup": nbiCommonNBIVersionOptionalGroup,
       "nbiCommonFilterSettingsOptionalGroup": nbiCommonFilterSettingsOptionalGroup,
       "nbiCommonGeneralOptionalGroup": nbiCommonGeneralOptionalGroup}
)
