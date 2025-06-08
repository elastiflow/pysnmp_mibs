# SNMP MIB module (QUASAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/techargos_57262/QUASAR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:04:30 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

techargos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 57262)
)
if mibBuilder.loadTexts:
    techargos.setRevisions(
        ("2022-04-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nms_ObjectIdentity = ObjectIdentity
nms = _Nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999)
)
_Nb_ObjectIdentity = ObjectIdentity
nb = _Nb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1)
)
if mibBuilder.loadTexts:
    nb.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 0)
)
if mibBuilder.loadTexts:
    notifications.setStatus("current")
_TrapFields_ObjectIdentity = ObjectIdentity
trapFields = _TrapFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1)
)
if mibBuilder.loadTexts:
    trapFields.setStatus("current")
_InvokeIdentifier_Type = Integer32
_InvokeIdentifier_Object = MibScalar
invokeIdentifier = _InvokeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 1),
    _InvokeIdentifier_Type()
)
invokeIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    invokeIdentifier.setStatus("current")
_Mode_Type = OctetString
_Mode_Object = MibScalar
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 2),
    _Mode_Type()
)
mode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mode.setStatus("current")
_ManagedObjectClass_Type = Integer32
_ManagedObjectClass_Object = MibScalar
managedObjectClass = _ManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 3),
    _ManagedObjectClass_Type()
)
managedObjectClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectClass.setStatus("current")
_ManagedObjectInstance_Type = Integer32
_ManagedObjectInstance_Object = MibScalar
managedObjectInstance = _ManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 4),
    _ManagedObjectInstance_Type()
)
managedObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectInstance.setStatus("current")
_EventType_Type = OctetString
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 5),
    _EventType_Type()
)
eventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventTime_Type = DateAndTime
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 6),
    _EventTime_Type()
)
eventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_ProbableCause_Type = OctetString
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 7),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    probableCause.setStatus("current")
_SpecificProblems_Type = OctetString
_SpecificProblems_Object = MibScalar
specificProblems = _SpecificProblems_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 8),
    _SpecificProblems_Type()
)
specificProblems.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    specificProblems.setStatus("current")
_PerceivedSeverity_Type = OctetString
_PerceivedSeverity_Object = MibScalar
perceivedSeverity = _PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 9),
    _PerceivedSeverity_Type()
)
perceivedSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    perceivedSeverity.setStatus("current")
_BackedUpStatus_Type = OctetString
_BackedUpStatus_Object = MibScalar
backedUpStatus = _BackedUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 10),
    _BackedUpStatus_Type()
)
backedUpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    backedUpStatus.setStatus("current")
_BackedUpObject_Type = OctetString
_BackedUpObject_Object = MibScalar
backedUpObject = _BackedUpObject_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 11),
    _BackedUpObject_Type()
)
backedUpObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    backedUpObject.setStatus("current")
_TrendIndication_Type = OctetString
_TrendIndication_Object = MibScalar
trendIndication = _TrendIndication_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 12),
    _TrendIndication_Type()
)
trendIndication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trendIndication.setStatus("current")
_ThresholdInformation_Type = OctetString
_ThresholdInformation_Object = MibScalar
thresholdInformation = _ThresholdInformation_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 13),
    _ThresholdInformation_Type()
)
thresholdInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdInformation.setStatus("current")
_NotificationIdentifier_Type = Integer32
_NotificationIdentifier_Object = MibScalar
notificationIdentifier = _NotificationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 14),
    _NotificationIdentifier_Type()
)
notificationIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationIdentifier.setStatus("current")
_CorrelatedNotifications_Type = OctetString
_CorrelatedNotifications_Object = MibScalar
correlatedNotifications = _CorrelatedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 15),
    _CorrelatedNotifications_Type()
)
correlatedNotifications.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    correlatedNotifications.setStatus("current")
_StateChangeDefinition_Type = OctetString
_StateChangeDefinition_Object = MibScalar
stateChangeDefinition = _StateChangeDefinition_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 16),
    _StateChangeDefinition_Type()
)
stateChangeDefinition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stateChangeDefinition.setStatus("current")
_MonitoredAttributes_Type = OctetString
_MonitoredAttributes_Object = MibScalar
monitoredAttributes = _MonitoredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 17),
    _MonitoredAttributes_Type()
)
monitoredAttributes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monitoredAttributes.setStatus("current")
_ProposedRepairActions_Type = OctetString
_ProposedRepairActions_Object = MibScalar
proposedRepairActions = _ProposedRepairActions_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 18),
    _ProposedRepairActions_Type()
)
proposedRepairActions.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    proposedRepairActions.setStatus("current")
_AdditionalText_Type = OctetString
_AdditionalText_Object = MibScalar
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 19),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    additionalText.setStatus("current")
_AdditionalInformation_Type = OctetString
_AdditionalInformation_Object = MibScalar
additionalInformation = _AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 20),
    _AdditionalInformation_Type()
)
additionalInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    additionalInformation.setStatus("current")
_CurrentTime_Type = DateAndTime
_CurrentTime_Object = MibScalar
currentTime = _CurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 21),
    _CurrentTime_Type()
)
currentTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentTime.setStatus("current")
_EventReply_Type = OctetString
_EventReply_Object = MibScalar
eventReply = _EventReply_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 22),
    _EventReply_Type()
)
eventReply.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventReply.setStatus("current")
_Errors_Type = OctetString
_Errors_Object = MibScalar
errors = _Errors_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 1, 23),
    _Errors_Type()
)
errors.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errors.setStatus("current")
_Actions_ObjectIdentity = ObjectIdentity
actions = _Actions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 2)
)
if mibBuilder.loadTexts:
    actions.setStatus("current")


class _Acknowledge_Type(Integer32):
    """Custom type acknowledge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Acknowledge_Type.__name__ = "Integer32"
_Acknowledge_Object = MibScalar
acknowledge = _Acknowledge_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 2, 1),
    _Acknowledge_Type()
)
acknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acknowledge.setStatus("current")


class _Unacknowledge_Type(Integer32):
    """Custom type unacknowledge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Unacknowledge_Type.__name__ = "Integer32"
_Unacknowledge_Object = MibScalar
unacknowledge = _Unacknowledge_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 2, 2),
    _Unacknowledge_Type()
)
unacknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unacknowledge.setStatus("current")


class _Clear_Type(Integer32):
    """Custom type clear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Clear_Type.__name__ = "Integer32"
_Clear_Object = MibScalar
clear = _Clear_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 2, 3),
    _Clear_Type()
)
clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clear.setStatus("current")
_Fields_ObjectIdentity = ObjectIdentity
fields = _Fields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3)
)
if mibBuilder.loadTexts:
    fields.setStatus("current")
_ZoneTable_Object = MibTable
zoneTable = _ZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zoneTable.setStatus("current")
_ZoneEntry_Object = MibTableRow
zoneEntry = _ZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1)
)
zoneEntry.setIndexNames(
    (0, "QUASAR-MIB", "ztZoneID"),
)
if mibBuilder.loadTexts:
    zoneEntry.setStatus("current")


class _ZtZoneID_Type(Integer32):
    """Custom type ztZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZtZoneID_Type.__name__ = "Integer32"
_ZtZoneID_Object = MibTableColumn
ztZoneID = _ZtZoneID_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1, 1),
    _ZtZoneID_Type()
)
ztZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztZoneID.setStatus("current")


class _ZtName_Type(OctetString):
    """Custom type ztName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZtName_Type.__name__ = "OctetString"
_ZtName_Object = MibTableColumn
ztName = _ZtName_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1, 2),
    _ZtName_Type()
)
ztName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztName.setStatus("current")


class _ZtDescription_Type(OctetString):
    """Custom type ztDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZtDescription_Type.__name__ = "OctetString"
_ZtDescription_Object = MibTableColumn
ztDescription = _ZtDescription_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1, 3),
    _ZtDescription_Type()
)
ztDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztDescription.setStatus("current")
_ZtLocation_Type = OctetString
_ZtLocation_Object = MibTableColumn
ztLocation = _ZtLocation_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1, 4),
    _ZtLocation_Type()
)
ztLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztLocation.setStatus("current")
_ZtSystemAdminContact_Type = OctetString
_ZtSystemAdminContact_Object = MibTableColumn
ztSystemAdminContact = _ZtSystemAdminContact_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1, 5),
    _ZtSystemAdminContact_Type()
)
ztSystemAdminContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztSystemAdminContact.setStatus("current")
_ZtSystemTechContact_Type = OctetString
_ZtSystemTechContact_Object = MibTableColumn
ztSystemTechContact = _ZtSystemTechContact_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 1, 1, 6),
    _ZtSystemTechContact_Type()
)
ztSystemTechContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ztSystemTechContact.setStatus("current")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("current")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1)
)
deviceEntry.setIndexNames(
    (0, "QUASAR-MIB", "dtDeviceID"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("current")


class _DtDeviceID_Type(Integer32):
    """Custom type dtDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtDeviceID_Type.__name__ = "Integer32"
_DtDeviceID_Object = MibTableColumn
dtDeviceID = _DtDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 1),
    _DtDeviceID_Type()
)
dtDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtDeviceID.setStatus("current")


class _DtName_Type(OctetString):
    """Custom type dtName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtName_Type.__name__ = "OctetString"
_DtName_Object = MibTableColumn
dtName = _DtName_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 2),
    _DtName_Type()
)
dtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtName.setStatus("current")
_DtType_Type = OctetString
_DtType_Object = MibTableColumn
dtType = _DtType_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 3),
    _DtType_Type()
)
dtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtType.setStatus("current")


class _DtModel_Type(OctetString):
    """Custom type dtModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtModel_Type.__name__ = "OctetString"
_DtModel_Object = MibTableColumn
dtModel = _DtModel_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 4),
    _DtModel_Type()
)
dtModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtModel.setStatus("current")


class _DtVendor_Type(OctetString):
    """Custom type dtVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtVendor_Type.__name__ = "OctetString"
_DtVendor_Object = MibTableColumn
dtVendor = _DtVendor_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 5),
    _DtVendor_Type()
)
dtVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtVendor.setStatus("current")


class _DtRole_Type(OctetString):
    """Custom type dtRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtRole_Type.__name__ = "OctetString"
_DtRole_Object = MibTableColumn
dtRole = _DtRole_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 6),
    _DtRole_Type()
)
dtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtRole.setStatus("current")


class _DtDescription_Type(OctetString):
    """Custom type dtDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtDescription_Type.__name__ = "OctetString"
_DtDescription_Object = MibTableColumn
dtDescription = _DtDescription_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 7),
    _DtDescription_Type()
)
dtDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtDescription.setStatus("current")


class _DtLocation_Type(OctetString):
    """Custom type dtLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtLocation_Type.__name__ = "OctetString"
_DtLocation_Object = MibTableColumn
dtLocation = _DtLocation_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 8),
    _DtLocation_Type()
)
dtLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtLocation.setStatus("current")
_DtDeviceStatus_Type = Integer32
_DtDeviceStatus_Object = MibTableColumn
dtDeviceStatus = _DtDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 9),
    _DtDeviceStatus_Type()
)
dtDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtDeviceStatus.setStatus("current")
_DtSystemAdminContact_Type = OctetString
_DtSystemAdminContact_Object = MibTableColumn
dtSystemAdminContact = _DtSystemAdminContact_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 10),
    _DtSystemAdminContact_Type()
)
dtSystemAdminContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtSystemAdminContact.setStatus("current")
_DtSystemTechContact_Type = OctetString
_DtSystemTechContact_Object = MibTableColumn
dtSystemTechContact = _DtSystemTechContact_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 2, 1, 11),
    _DtSystemTechContact_Type()
)
dtSystemTechContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtSystemTechContact.setStatus("current")
_InventoryInfo_Type = DisplayString
_InventoryInfo_Object = MibScalar
inventoryInfo = _InventoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 3),
    _InventoryInfo_Type()
)
inventoryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryInfo.setStatus("current")
_PerfomanceInfo_Type = DisplayString
_PerfomanceInfo_Object = MibScalar
perfomanceInfo = _PerfomanceInfo_Object(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 3, 4),
    _PerfomanceInfo_Type()
)
perfomanceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfomanceInfo.setStatus("current")
_NbConformance_ObjectIdentity = ObjectIdentity
nbConformance = _NbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2)
)
_NbGroups_ObjectIdentity = ObjectIdentity
nbGroups = _NbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 1)
)
_NbCompliances_ObjectIdentity = ObjectIdentity
nbCompliances = _NbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 2)
)

# Managed Objects groups

trapFieldsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 1, 2)
)
trapFieldsGroup.setObjects(
      *(("QUASAR-MIB", "invokeIdentifier"),
        ("QUASAR-MIB", "mode"),
        ("QUASAR-MIB", "managedObjectClass"),
        ("QUASAR-MIB", "managedObjectInstance"),
        ("QUASAR-MIB", "eventType"),
        ("QUASAR-MIB", "eventTime"),
        ("QUASAR-MIB", "probableCause"),
        ("QUASAR-MIB", "specificProblems"),
        ("QUASAR-MIB", "perceivedSeverity"),
        ("QUASAR-MIB", "backedUpStatus"),
        ("QUASAR-MIB", "backedUpObject"),
        ("QUASAR-MIB", "trendIndication"),
        ("QUASAR-MIB", "thresholdInformation"),
        ("QUASAR-MIB", "notificationIdentifier"),
        ("QUASAR-MIB", "correlatedNotifications"),
        ("QUASAR-MIB", "stateChangeDefinition"),
        ("QUASAR-MIB", "monitoredAttributes"),
        ("QUASAR-MIB", "proposedRepairActions"),
        ("QUASAR-MIB", "additionalText"),
        ("QUASAR-MIB", "additionalInformation"),
        ("QUASAR-MIB", "currentTime"),
        ("QUASAR-MIB", "eventReply"),
        ("QUASAR-MIB", "errors"))
)
if mibBuilder.loadTexts:
    trapFieldsGroup.setStatus("current")

actionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 1, 3)
)
actionGroup.setObjects(
      *(("QUASAR-MIB", "acknowledge"),
        ("QUASAR-MIB", "unacknowledge"),
        ("QUASAR-MIB", "clear"))
)
if mibBuilder.loadTexts:
    actionGroup.setStatus("current")

fieldsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 1, 4)
)
fieldsGroup.setObjects(
      *(("QUASAR-MIB", "ztZoneID"),
        ("QUASAR-MIB", "ztName"),
        ("QUASAR-MIB", "ztDescription"),
        ("QUASAR-MIB", "ztLocation"),
        ("QUASAR-MIB", "ztSystemAdminContact"),
        ("QUASAR-MIB", "ztSystemTechContact"),
        ("QUASAR-MIB", "dtDeviceID"),
        ("QUASAR-MIB", "dtName"),
        ("QUASAR-MIB", "dtType"),
        ("QUASAR-MIB", "dtModel"),
        ("QUASAR-MIB", "dtVendor"),
        ("QUASAR-MIB", "dtRole"),
        ("QUASAR-MIB", "dtDescription"),
        ("QUASAR-MIB", "dtLocation"),
        ("QUASAR-MIB", "dtDeviceStatus"),
        ("QUASAR-MIB", "dtSystemAdminContact"),
        ("QUASAR-MIB", "dtSystemTechContact"),
        ("QUASAR-MIB", "inventoryInfo"),
        ("QUASAR-MIB", "perfomanceInfo"))
)
if mibBuilder.loadTexts:
    fieldsGroup.setStatus("current")


# Notification objects

alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 57262, 999, 1, 0, 1)
)
alarm.setObjects(
      *(("QUASAR-MIB", "invokeIdentifier"),
        ("QUASAR-MIB", "mode"),
        ("QUASAR-MIB", "managedObjectClass"),
        ("QUASAR-MIB", "managedObjectInstance"),
        ("QUASAR-MIB", "eventType"),
        ("QUASAR-MIB", "eventTime"),
        ("QUASAR-MIB", "probableCause"),
        ("QUASAR-MIB", "specificProblems"),
        ("QUASAR-MIB", "perceivedSeverity"),
        ("QUASAR-MIB", "backedUpStatus"),
        ("QUASAR-MIB", "backedUpObject"),
        ("QUASAR-MIB", "trendIndication"),
        ("QUASAR-MIB", "thresholdInformation"),
        ("QUASAR-MIB", "notificationIdentifier"),
        ("QUASAR-MIB", "correlatedNotifications"),
        ("QUASAR-MIB", "stateChangeDefinition"),
        ("QUASAR-MIB", "monitoredAttributes"),
        ("QUASAR-MIB", "proposedRepairActions"),
        ("QUASAR-MIB", "additionalText"),
        ("QUASAR-MIB", "additionalInformation"),
        ("QUASAR-MIB", "currentTime"),
        ("QUASAR-MIB", "eventReply"),
        ("QUASAR-MIB", "errors"))
)
if mibBuilder.loadTexts:
    alarm.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 1, 1)
)
notificationGroup.setObjects(
    ("QUASAR-MIB", "alarm")
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nbComplianceExt = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 57262, 999, 2, 2, 1)
)
nbComplianceExt.setObjects(
      *(("QUASAR-MIB", "notificationGroup"),
        ("QUASAR-MIB", "trapFieldsGroup"),
        ("QUASAR-MIB", "actionGroup"),
        ("QUASAR-MIB", "fieldsGroup"))
)
if mibBuilder.loadTexts:
    nbComplianceExt.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QUASAR-MIB",
    **{"techargos": techargos,
       "nms": nms,
       "nb": nb,
       "notifications": notifications,
       "alarm": alarm,
       "trapFields": trapFields,
       "invokeIdentifier": invokeIdentifier,
       "mode": mode,
       "managedObjectClass": managedObjectClass,
       "managedObjectInstance": managedObjectInstance,
       "eventType": eventType,
       "eventTime": eventTime,
       "probableCause": probableCause,
       "specificProblems": specificProblems,
       "perceivedSeverity": perceivedSeverity,
       "backedUpStatus": backedUpStatus,
       "backedUpObject": backedUpObject,
       "trendIndication": trendIndication,
       "thresholdInformation": thresholdInformation,
       "notificationIdentifier": notificationIdentifier,
       "correlatedNotifications": correlatedNotifications,
       "stateChangeDefinition": stateChangeDefinition,
       "monitoredAttributes": monitoredAttributes,
       "proposedRepairActions": proposedRepairActions,
       "additionalText": additionalText,
       "additionalInformation": additionalInformation,
       "currentTime": currentTime,
       "eventReply": eventReply,
       "errors": errors,
       "actions": actions,
       "acknowledge": acknowledge,
       "unacknowledge": unacknowledge,
       "clear": clear,
       "fields": fields,
       "zoneTable": zoneTable,
       "zoneEntry": zoneEntry,
       "ztZoneID": ztZoneID,
       "ztName": ztName,
       "ztDescription": ztDescription,
       "ztLocation": ztLocation,
       "ztSystemAdminContact": ztSystemAdminContact,
       "ztSystemTechContact": ztSystemTechContact,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "dtDeviceID": dtDeviceID,
       "dtName": dtName,
       "dtType": dtType,
       "dtModel": dtModel,
       "dtVendor": dtVendor,
       "dtRole": dtRole,
       "dtDescription": dtDescription,
       "dtLocation": dtLocation,
       "dtDeviceStatus": dtDeviceStatus,
       "dtSystemAdminContact": dtSystemAdminContact,
       "dtSystemTechContact": dtSystemTechContact,
       "inventoryInfo": inventoryInfo,
       "perfomanceInfo": perfomanceInfo,
       "nbConformance": nbConformance,
       "nbGroups": nbGroups,
       "notificationGroup": notificationGroup,
       "trapFieldsGroup": trapFieldsGroup,
       "actionGroup": actionGroup,
       "fieldsGroup": fieldsGroup,
       "nbCompliances": nbCompliances,
       "nbComplianceExt": nbComplianceExt}
)
