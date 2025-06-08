# SNMP MIB module (EXFO-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/EXFO-EVENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(exfoCommonMib,
 exfoModules) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoCommonMib",
    "exfoModules")

(ExfoSnmpType,) = mibBuilder.importSymbols(
    "EXFO-TC",
    "ExfoSnmpType")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

exfoEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EventSourceIndicator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resourceOperation", 0),
          ("managementOperation", 1),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnEvent_ObjectIdentity = ObjectIdentity
tmnEvent = _TmnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1)
)
if mibBuilder.loadTexts:
    tmnEvent.setStatus("current")
_TmnEventConf_ObjectIdentity = ObjectIdentity
tmnEventConf = _TmnEventConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnEventConf.setStatus("current")
_TmnEventGroups_ObjectIdentity = ObjectIdentity
tmnEventGroups = _TmnEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnEventGroups.setStatus("current")
_TmnEventCompls_ObjectIdentity = ObjectIdentity
tmnEventCompls = _TmnEventCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnEventCompls.setStatus("current")
_TmnEventObjs_ObjectIdentity = ObjectIdentity
tmnEventObjs = _TmnEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tmnEventObjs.setStatus("current")
_EventManagedObjectInstance_Type = VariablePointer
_EventManagedObjectInstance_Object = MibScalar
eventManagedObjectInstance = _EventManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 1),
    _EventManagedObjectInstance_Type()
)
eventManagedObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventManagedObjectInstance.setStatus("current")
_EventTime_Type = DateAndTime
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 3),
    _EventTime_Type()
)
eventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventSourceIndicator_Type = EventSourceIndicator
_EventSourceIndicator_Object = MibScalar
eventSourceIndicator = _EventSourceIndicator_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 4),
    _EventSourceIndicator_Type()
)
eventSourceIndicator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSourceIndicator.setStatus("current")
_EventAttrIdTable_Object = MibTable
eventAttrIdTable = _EventAttrIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    eventAttrIdTable.setStatus("current")
_EventAttrIdEntry_Object = MibTableRow
eventAttrIdEntry = _EventAttrIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 5, 1)
)
eventAttrIdEntry.setIndexNames(
    (0, "EXFO-EVENT-MIB", "eventAttrIdIndex"),
)
if mibBuilder.loadTexts:
    eventAttrIdEntry.setStatus("current")
_EventAttrIdIndex_Type = Unsigned32
_EventAttrIdIndex_Object = MibTableColumn
eventAttrIdIndex = _EventAttrIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 5, 1, 1),
    _EventAttrIdIndex_Type()
)
eventAttrIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventAttrIdIndex.setStatus("current")
_EventAttrIdAttributeId_Type = AutonomousType
_EventAttrIdAttributeId_Object = MibTableColumn
eventAttrIdAttributeId = _EventAttrIdAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 5, 1, 2),
    _EventAttrIdAttributeId_Type()
)
eventAttrIdAttributeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrIdAttributeId.setStatus("current")
_EventAttrValueChangeDefTable_Object = MibTable
eventAttrValueChangeDefTable = _EventAttrValueChangeDefTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    eventAttrValueChangeDefTable.setStatus("current")
_EventAttrValueChangeDefEntry_Object = MibTableRow
eventAttrValueChangeDefEntry = _EventAttrValueChangeDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1)
)
eventAttrValueChangeDefEntry.setIndexNames(
    (0, "EXFO-EVENT-MIB", "eventAttrValueChangeDefIndex"),
)
if mibBuilder.loadTexts:
    eventAttrValueChangeDefEntry.setStatus("current")
_EventAttrValueChangeDefIndex_Type = Unsigned32
_EventAttrValueChangeDefIndex_Object = MibTableColumn
eventAttrValueChangeDefIndex = _EventAttrValueChangeDefIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 1),
    _EventAttrValueChangeDefIndex_Type()
)
eventAttrValueChangeDefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefIndex.setStatus("current")
_EventAttrValueChangeDefAttributeId_Type = AutonomousType
_EventAttrValueChangeDefAttributeId_Object = MibTableColumn
eventAttrValueChangeDefAttributeId = _EventAttrValueChangeDefAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 2),
    _EventAttrValueChangeDefAttributeId_Type()
)
eventAttrValueChangeDefAttributeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefAttributeId.setStatus("current")
_EventAttrValueChangeDefAttributeValueType_Type = ExfoSnmpType
_EventAttrValueChangeDefAttributeValueType_Object = MibTableColumn
eventAttrValueChangeDefAttributeValueType = _EventAttrValueChangeDefAttributeValueType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 3),
    _EventAttrValueChangeDefAttributeValueType_Type()
)
eventAttrValueChangeDefAttributeValueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefAttributeValueType.setStatus("current")
_EventAttrValueChangeDefOldAttributeValueInteger_Type = Integer32
_EventAttrValueChangeDefOldAttributeValueInteger_Object = MibTableColumn
eventAttrValueChangeDefOldAttributeValueInteger = _EventAttrValueChangeDefOldAttributeValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 4),
    _EventAttrValueChangeDefOldAttributeValueInteger_Type()
)
eventAttrValueChangeDefOldAttributeValueInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefOldAttributeValueInteger.setStatus("current")


class _EventAttrValueChangeDefOldAttributeValueString_Type(OctetString):
    """Custom type eventAttrValueChangeDefOldAttributeValueString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventAttrValueChangeDefOldAttributeValueString_Type.__name__ = "OctetString"
_EventAttrValueChangeDefOldAttributeValueString_Object = MibTableColumn
eventAttrValueChangeDefOldAttributeValueString = _EventAttrValueChangeDefOldAttributeValueString_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 5),
    _EventAttrValueChangeDefOldAttributeValueString_Type()
)
eventAttrValueChangeDefOldAttributeValueString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefOldAttributeValueString.setStatus("current")
_EventAttrValueChangeDefNewAttributeValueInteger_Type = Integer32
_EventAttrValueChangeDefNewAttributeValueInteger_Object = MibTableColumn
eventAttrValueChangeDefNewAttributeValueInteger = _EventAttrValueChangeDefNewAttributeValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 6),
    _EventAttrValueChangeDefNewAttributeValueInteger_Type()
)
eventAttrValueChangeDefNewAttributeValueInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefNewAttributeValueInteger.setStatus("current")


class _EventAttrValueChangeDefNewAttributeValueString_Type(OctetString):
    """Custom type eventAttrValueChangeDefNewAttributeValueString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventAttrValueChangeDefNewAttributeValueString_Type.__name__ = "OctetString"
_EventAttrValueChangeDefNewAttributeValueString_Object = MibTableColumn
eventAttrValueChangeDefNewAttributeValueString = _EventAttrValueChangeDefNewAttributeValueString_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 6, 1, 7),
    _EventAttrValueChangeDefNewAttributeValueString_Type()
)
eventAttrValueChangeDefNewAttributeValueString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttrValueChangeDefNewAttributeValueString.setStatus("current")
_EventNotificationIdentifier_Type = Integer32
_EventNotificationIdentifier_Object = MibScalar
eventNotificationIdentifier = _EventNotificationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 7),
    _EventNotificationIdentifier_Type()
)
eventNotificationIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventNotificationIdentifier.setStatus("current")
_EventCorrNotifTable_Object = MibTable
eventCorrNotifTable = _EventCorrNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    eventCorrNotifTable.setStatus("current")
_EventCorrNotifEntry_Object = MibTableRow
eventCorrNotifEntry = _EventCorrNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 8, 1)
)
eventCorrNotifEntry.setIndexNames(
    (0, "EXFO-EVENT-MIB", "eventCorrNotifIndex"),
)
if mibBuilder.loadTexts:
    eventCorrNotifEntry.setStatus("current")
_EventCorrNotifIndex_Type = Unsigned32
_EventCorrNotifIndex_Object = MibTableColumn
eventCorrNotifIndex = _EventCorrNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 8, 1, 1),
    _EventCorrNotifIndex_Type()
)
eventCorrNotifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventCorrNotifIndex.setStatus("current")
_EventCorrNotifSourceObjectInst_Type = VariablePointer
_EventCorrNotifSourceObjectInst_Object = MibTableColumn
eventCorrNotifSourceObjectInst = _EventCorrNotifSourceObjectInst_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 8, 1, 2),
    _EventCorrNotifSourceObjectInst_Type()
)
eventCorrNotifSourceObjectInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCorrNotifSourceObjectInst.setStatus("current")
_EventCorrNotifNotificationIdentifier_Type = Integer32
_EventCorrNotifNotificationIdentifier_Object = MibTableColumn
eventCorrNotifNotificationIdentifier = _EventCorrNotifNotificationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 8, 1, 3),
    _EventCorrNotifNotificationIdentifier_Type()
)
eventCorrNotifNotificationIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCorrNotifNotificationIdentifier.setStatus("current")
_EventAdditionalText_Type = DisplayString
_EventAdditionalText_Object = MibScalar
eventAdditionalText = _EventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 9),
    _EventAdditionalText_Type()
)
eventAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAdditionalText.setStatus("current")
_EventAddInformTable_Object = MibTable
eventAddInformTable = _EventAddInformTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    eventAddInformTable.setStatus("current")
_EventAddInformEntry_Object = MibTableRow
eventAddInformEntry = _EventAddInformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1)
)
eventAddInformEntry.setIndexNames(
    (0, "EXFO-EVENT-MIB", "eventAddInformIndex"),
)
if mibBuilder.loadTexts:
    eventAddInformEntry.setStatus("current")
_EventAddInformIndex_Type = Unsigned32
_EventAddInformIndex_Object = MibTableColumn
eventAddInformIndex = _EventAddInformIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1, 1),
    _EventAddInformIndex_Type()
)
eventAddInformIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventAddInformIndex.setStatus("current")
_EventAddInformIdentifier_Type = VariablePointer
_EventAddInformIdentifier_Object = MibTableColumn
eventAddInformIdentifier = _EventAddInformIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1, 2),
    _EventAddInformIdentifier_Type()
)
eventAddInformIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAddInformIdentifier.setStatus("current")
_EventAddInformSignificance_Type = TruthValue
_EventAddInformSignificance_Object = MibTableColumn
eventAddInformSignificance = _EventAddInformSignificance_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1, 3),
    _EventAddInformSignificance_Type()
)
eventAddInformSignificance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAddInformSignificance.setStatus("current")
_EventAddInformValueType_Type = ExfoSnmpType
_EventAddInformValueType_Object = MibTableColumn
eventAddInformValueType = _EventAddInformValueType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1, 4),
    _EventAddInformValueType_Type()
)
eventAddInformValueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAddInformValueType.setStatus("current")
_EventAddInformValueInteger_Type = Integer32
_EventAddInformValueInteger_Object = MibTableColumn
eventAddInformValueInteger = _EventAddInformValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1, 5),
    _EventAddInformValueInteger_Type()
)
eventAddInformValueInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAddInformValueInteger.setStatus("current")


class _EventAddInformValueString_Type(OctetString):
    """Custom type eventAddInformValueString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventAddInformValueString_Type.__name__ = "OctetString"
_EventAddInformValueString_Object = MibTableColumn
eventAddInformValueString = _EventAddInformValueString_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 10, 1, 6),
    _EventAddInformValueString_Type()
)
eventAddInformValueString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAddInformValueString.setStatus("current")
_EventAttributeTable_Object = MibTable
eventAttributeTable = _EventAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    eventAttributeTable.setStatus("current")
_EventAttributeEntry_Object = MibTableRow
eventAttributeEntry = _EventAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11, 1)
)
eventAttributeEntry.setIndexNames(
    (0, "EXFO-EVENT-MIB", "eventAttributeIndex"),
)
if mibBuilder.loadTexts:
    eventAttributeEntry.setStatus("current")
_EventAttributeIndex_Type = Unsigned32
_EventAttributeIndex_Object = MibTableColumn
eventAttributeIndex = _EventAttributeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11, 1, 1),
    _EventAttributeIndex_Type()
)
eventAttributeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventAttributeIndex.setStatus("current")
_EventAttributeId_Type = AutonomousType
_EventAttributeId_Object = MibTableColumn
eventAttributeId = _EventAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11, 1, 2),
    _EventAttributeId_Type()
)
eventAttributeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttributeId.setStatus("current")
_EventAttributeValueType_Type = ExfoSnmpType
_EventAttributeValueType_Object = MibTableColumn
eventAttributeValueType = _EventAttributeValueType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11, 1, 3),
    _EventAttributeValueType_Type()
)
eventAttributeValueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttributeValueType.setStatus("current")
_EventAttributeValueInteger_Type = Integer32
_EventAttributeValueInteger_Object = MibTableColumn
eventAttributeValueInteger = _EventAttributeValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11, 1, 4),
    _EventAttributeValueInteger_Type()
)
eventAttributeValueInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttributeValueInteger.setStatus("current")


class _EventAttributeValueString_Type(OctetString):
    """Custom type eventAttributeValueString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventAttributeValueString_Type.__name__ = "OctetString"
_EventAttributeValueString_Object = MibTableColumn
eventAttributeValueString = _EventAttributeValueString_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 2, 11, 1, 5),
    _EventAttributeValueString_Type()
)
eventAttributeValueString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttributeValueString.setStatus("current")
_TmnEventEvents_ObjectIdentity = ObjectIdentity
tmnEventEvents = _TmnEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tmnEventEvents.setStatus("current")

# Managed Objects groups


# Notification objects

stateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 3, 1)
)
stateChange.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-EVENT-MIB", "eventSourceIndicator"),
        ("EXFO-EVENT-MIB", "eventAttrIdAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeValueType"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventCorrNotifSourceObjectInst"),
        ("EXFO-EVENT-MIB", "eventCorrNotifNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventAdditionalText"),
        ("EXFO-EVENT-MIB", "eventAddInformIdentifier"),
        ("EXFO-EVENT-MIB", "eventAddInformSignificance"),
        ("EXFO-EVENT-MIB", "eventAddInformValueType"),
        ("EXFO-EVENT-MIB", "eventAddInformValueInteger"),
        ("EXFO-EVENT-MIB", "eventAddInformValueString"))
)
if mibBuilder.loadTexts:
    stateChange.setStatus(
        "current"
    )

attributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 3, 2)
)
attributeValueChange.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-EVENT-MIB", "eventSourceIndicator"),
        ("EXFO-EVENT-MIB", "eventAttrIdAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeValueType"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventCorrNotifSourceObjectInst"),
        ("EXFO-EVENT-MIB", "eventCorrNotifNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventAdditionalText"),
        ("EXFO-EVENT-MIB", "eventAddInformIdentifier"),
        ("EXFO-EVENT-MIB", "eventAddInformSignificance"),
        ("EXFO-EVENT-MIB", "eventAddInformValueType"),
        ("EXFO-EVENT-MIB", "eventAddInformValueInteger"),
        ("EXFO-EVENT-MIB", "eventAddInformValueString"))
)
if mibBuilder.loadTexts:
    attributeValueChange.setStatus(
        "current"
    )

objectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 3, 3)
)
objectCreation.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-EVENT-MIB", "eventSourceIndicator"),
        ("EXFO-EVENT-MIB", "eventAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttributeValueType"),
        ("EXFO-EVENT-MIB", "eventAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventCorrNotifSourceObjectInst"),
        ("EXFO-EVENT-MIB", "eventCorrNotifNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventAdditionalText"),
        ("EXFO-EVENT-MIB", "eventAddInformIdentifier"),
        ("EXFO-EVENT-MIB", "eventAddInformSignificance"),
        ("EXFO-EVENT-MIB", "eventAddInformValueType"),
        ("EXFO-EVENT-MIB", "eventAddInformValueInteger"),
        ("EXFO-EVENT-MIB", "eventAddInformValueString"))
)
if mibBuilder.loadTexts:
    objectCreation.setStatus(
        "current"
    )

objectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 3, 4)
)
objectDeletion.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-EVENT-MIB", "eventSourceIndicator"),
        ("EXFO-EVENT-MIB", "eventAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttributeValueType"),
        ("EXFO-EVENT-MIB", "eventAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventCorrNotifSourceObjectInst"),
        ("EXFO-EVENT-MIB", "eventCorrNotifNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventAdditionalText"),
        ("EXFO-EVENT-MIB", "eventAddInformIdentifier"),
        ("EXFO-EVENT-MIB", "eventAddInformSignificance"),
        ("EXFO-EVENT-MIB", "eventAddInformValueType"),
        ("EXFO-EVENT-MIB", "eventAddInformValueInteger"),
        ("EXFO-EVENT-MIB", "eventAddInformValueString"))
)
if mibBuilder.loadTexts:
    objectDeletion.setStatus(
        "current"
    )


# Notifications groups

tmnEventStateNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 1, 1, 1)
)
tmnEventStateNotificationGroup.setObjects(
    ("EXFO-EVENT-MIB", "stateChange")
)
if mibBuilder.loadTexts:
    tmnEventStateNotificationGroup.setStatus(
        "current"
    )

tmnEventObjectNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 1, 1, 1, 2)
)
tmnEventObjectNotificationGroup.setObjects(
      *(("EXFO-EVENT-MIB", "attributeValueChange"),
        ("EXFO-EVENT-MIB", "objectCreation"),
        ("EXFO-EVENT-MIB", "objectDeletion"))
)
if mibBuilder.loadTexts:
    tmnEventObjectNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXFO-EVENT-MIB",
    **{"EventSourceIndicator": EventSourceIndicator,
       "exfoEventMib": exfoEventMib,
       "tmnEvent": tmnEvent,
       "tmnEventConf": tmnEventConf,
       "tmnEventGroups": tmnEventGroups,
       "tmnEventStateNotificationGroup": tmnEventStateNotificationGroup,
       "tmnEventObjectNotificationGroup": tmnEventObjectNotificationGroup,
       "tmnEventCompls": tmnEventCompls,
       "tmnEventObjs": tmnEventObjs,
       "eventManagedObjectInstance": eventManagedObjectInstance,
       "eventTime": eventTime,
       "eventSourceIndicator": eventSourceIndicator,
       "eventAttrIdTable": eventAttrIdTable,
       "eventAttrIdEntry": eventAttrIdEntry,
       "eventAttrIdIndex": eventAttrIdIndex,
       "eventAttrIdAttributeId": eventAttrIdAttributeId,
       "eventAttrValueChangeDefTable": eventAttrValueChangeDefTable,
       "eventAttrValueChangeDefEntry": eventAttrValueChangeDefEntry,
       "eventAttrValueChangeDefIndex": eventAttrValueChangeDefIndex,
       "eventAttrValueChangeDefAttributeId": eventAttrValueChangeDefAttributeId,
       "eventAttrValueChangeDefAttributeValueType": eventAttrValueChangeDefAttributeValueType,
       "eventAttrValueChangeDefOldAttributeValueInteger": eventAttrValueChangeDefOldAttributeValueInteger,
       "eventAttrValueChangeDefOldAttributeValueString": eventAttrValueChangeDefOldAttributeValueString,
       "eventAttrValueChangeDefNewAttributeValueInteger": eventAttrValueChangeDefNewAttributeValueInteger,
       "eventAttrValueChangeDefNewAttributeValueString": eventAttrValueChangeDefNewAttributeValueString,
       "eventNotificationIdentifier": eventNotificationIdentifier,
       "eventCorrNotifTable": eventCorrNotifTable,
       "eventCorrNotifEntry": eventCorrNotifEntry,
       "eventCorrNotifIndex": eventCorrNotifIndex,
       "eventCorrNotifSourceObjectInst": eventCorrNotifSourceObjectInst,
       "eventCorrNotifNotificationIdentifier": eventCorrNotifNotificationIdentifier,
       "eventAdditionalText": eventAdditionalText,
       "eventAddInformTable": eventAddInformTable,
       "eventAddInformEntry": eventAddInformEntry,
       "eventAddInformIndex": eventAddInformIndex,
       "eventAddInformIdentifier": eventAddInformIdentifier,
       "eventAddInformSignificance": eventAddInformSignificance,
       "eventAddInformValueType": eventAddInformValueType,
       "eventAddInformValueInteger": eventAddInformValueInteger,
       "eventAddInformValueString": eventAddInformValueString,
       "eventAttributeTable": eventAttributeTable,
       "eventAttributeEntry": eventAttributeEntry,
       "eventAttributeIndex": eventAttributeIndex,
       "eventAttributeId": eventAttributeId,
       "eventAttributeValueType": eventAttributeValueType,
       "eventAttributeValueInteger": eventAttributeValueInteger,
       "eventAttributeValueString": eventAttributeValueString,
       "tmnEventEvents": tmnEventEvents,
       "stateChange": stateChange,
       "attributeValueChange": attributeValueChange,
       "objectCreation": objectCreation,
       "objectDeletion": objectDeletion}
)
