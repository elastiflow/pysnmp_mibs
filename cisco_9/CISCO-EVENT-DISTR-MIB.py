# SNMP MIB module (CISCO-EVENT-DISTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-EVENT-DISTR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:14:07 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoEventDistrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127)
)
if mibBuilder.loadTexts:
    ciscoEventDistrMIB.setRevisions(
        ("1999-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEventDistrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEventDistrMIBObjects = _CiscoEventDistrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1)
)
_CedsEvent_ObjectIdentity = ObjectIdentity
cedsEvent = _CedsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1)
)


class _CedsEventID_Type(Integer32):
    """Custom type cedsEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CedsEventID_Type.__name__ = "Integer32"
_CedsEventID_Object = MibScalar
cedsEventID = _CedsEventID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 1),
    _CedsEventID_Type()
)
cedsEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventID.setStatus("current")


class _CedsEventIDName_Type(SnmpAdminString):
    """Custom type cedsEventIDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CedsEventIDName_Type.__name__ = "SnmpAdminString"
_CedsEventIDName_Object = MibScalar
cedsEventIDName = _CedsEventIDName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 2),
    _CedsEventIDName_Type()
)
cedsEventIDName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventIDName.setStatus("current")


class _CedsEventCategory_Type(Integer32):
    """Custom type cedsEventCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CedsEventCategory_Type.__name__ = "Integer32"
_CedsEventCategory_Object = MibScalar
cedsEventCategory = _CedsEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 3),
    _CedsEventCategory_Type()
)
cedsEventCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventCategory.setStatus("current")


class _CedsEventCategoryName_Type(SnmpAdminString):
    """Custom type cedsEventCategoryName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CedsEventCategoryName_Type.__name__ = "SnmpAdminString"
_CedsEventCategoryName_Object = MibScalar
cedsEventCategoryName = _CedsEventCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 4),
    _CedsEventCategoryName_Type()
)
cedsEventCategoryName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventCategoryName.setStatus("current")
_CedsEventCreatedTime_Type = DateAndTime
_CedsEventCreatedTime_Object = MibScalar
cedsEventCreatedTime = _CedsEventCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 5),
    _CedsEventCreatedTime_Type()
)
cedsEventCreatedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventCreatedTime.setStatus("current")
_CedsEventSentTime_Type = DateAndTime
_CedsEventSentTime_Object = MibScalar
cedsEventSentTime = _CedsEventSentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 6),
    _CedsEventSentTime_Type()
)
cedsEventSentTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventSentTime.setStatus("current")


class _CedsEventApplicationName_Type(SnmpAdminString):
    """Custom type cedsEventApplicationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CedsEventApplicationName_Type.__name__ = "SnmpAdminString"
_CedsEventApplicationName_Object = MibScalar
cedsEventApplicationName = _CedsEventApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 7),
    _CedsEventApplicationName_Type()
)
cedsEventApplicationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventApplicationName.setStatus("current")


class _CedsEventClassName_Type(DisplayString):
    """Custom type cedsEventClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CedsEventClassName_Type.__name__ = "DisplayString"
_CedsEventClassName_Object = MibScalar
cedsEventClassName = _CedsEventClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 8),
    _CedsEventClassName_Type()
)
cedsEventClassName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventClassName.setStatus("current")


class _CedsEventResourceType_Type(Integer32):
    """Custom type cedsEventResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CedsEventResourceType_Type.__name__ = "Integer32"
_CedsEventResourceType_Object = MibScalar
cedsEventResourceType = _CedsEventResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 9),
    _CedsEventResourceType_Type()
)
cedsEventResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventResourceType.setStatus("current")


class _CedsEventResourceTypeName_Type(SnmpAdminString):
    """Custom type cedsEventResourceTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CedsEventResourceTypeName_Type.__name__ = "SnmpAdminString"
_CedsEventResourceTypeName_Object = MibScalar
cedsEventResourceTypeName = _CedsEventResourceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 10),
    _CedsEventResourceTypeName_Type()
)
cedsEventResourceTypeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventResourceTypeName.setStatus("current")


class _CedsEventResourceAttribute_Type(Integer32):
    """Custom type cedsEventResourceAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CedsEventResourceAttribute_Type.__name__ = "Integer32"
_CedsEventResourceAttribute_Object = MibScalar
cedsEventResourceAttribute = _CedsEventResourceAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 11),
    _CedsEventResourceAttribute_Type()
)
cedsEventResourceAttribute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventResourceAttribute.setStatus("current")


class _CedsEventResourceAttributeName_Type(SnmpAdminString):
    """Custom type cedsEventResourceAttributeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CedsEventResourceAttributeName_Type.__name__ = "SnmpAdminString"
_CedsEventResourceAttributeName_Object = MibScalar
cedsEventResourceAttributeName = _CedsEventResourceAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 12),
    _CedsEventResourceAttributeName_Type()
)
cedsEventResourceAttributeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventResourceAttributeName.setStatus("current")


class _CedsEventResourceAttributeValue_Type(SnmpAdminString):
    """Custom type cedsEventResourceAttributeValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CedsEventResourceAttributeValue_Type.__name__ = "SnmpAdminString"
_CedsEventResourceAttributeValue_Object = MibScalar
cedsEventResourceAttributeValue = _CedsEventResourceAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 13),
    _CedsEventResourceAttributeValue_Type()
)
cedsEventResourceAttributeValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventResourceAttributeValue.setStatus("current")


class _CedsEventUniqueDataName_Type(SnmpAdminString):
    """Custom type cedsEventUniqueDataName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CedsEventUniqueDataName_Type.__name__ = "SnmpAdminString"
_CedsEventUniqueDataName_Object = MibScalar
cedsEventUniqueDataName = _CedsEventUniqueDataName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 14),
    _CedsEventUniqueDataName_Type()
)
cedsEventUniqueDataName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventUniqueDataName.setStatus("current")


class _CedsEventUniqueDataValue_Type(SnmpAdminString):
    """Custom type cedsEventUniqueDataValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CedsEventUniqueDataValue_Type.__name__ = "SnmpAdminString"
_CedsEventUniqueDataValue_Object = MibScalar
cedsEventUniqueDataValue = _CedsEventUniqueDataValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 1, 1, 15),
    _CedsEventUniqueDataValue_Type()
)
cedsEventUniqueDataValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cedsEventUniqueDataValue.setStatus("current")
_CiscoEventDistrMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoEventDistrMIBNotificationPrefix = _CiscoEventDistrMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 2)
)
_CiscoEventDistrMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEventDistrMIBNotifications = _CiscoEventDistrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 2, 0)
)
_CiscoEventDistrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEventDistrMIBConformance = _CiscoEventDistrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 3)
)
_CiscoEventDistrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEventDistrMIBCompliances = _CiscoEventDistrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 3, 1)
)
_CiscoEventDistrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEventDistrMIBGroups = _CiscoEventDistrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 3, 2)
)

# Managed Objects groups

ciscoEventDistrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 3, 2, 1)
)
ciscoEventDistrMIBGroup.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "cedsEventID"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventIDName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategory"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategoryName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCreatedTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventSentTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventApplicationName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventClassName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceType"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceTypeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttribute"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeValue"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataValue"))
)
if mibBuilder.loadTexts:
    ciscoEventDistrMIBGroup.setStatus("current")


# Notification objects

cedsCriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 2, 0, 1)
)
cedsCriticalEvent.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "cedsEventID"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventIDName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategory"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategoryName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCreatedTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventSentTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventApplicationName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventClassName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceType"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceTypeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttribute"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeValue"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataValue"))
)
if mibBuilder.loadTexts:
    cedsCriticalEvent.setStatus(
        "current"
    )

cedsMajorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 2, 0, 2)
)
cedsMajorEvent.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "cedsEventID"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventIDName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategory"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategoryName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCreatedTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventSentTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventApplicationName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventClassName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceType"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceTypeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttribute"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeValue"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataValue"))
)
if mibBuilder.loadTexts:
    cedsMajorEvent.setStatus(
        "current"
    )

cedsMinorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 2, 0, 3)
)
cedsMinorEvent.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "cedsEventID"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventIDName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategory"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategoryName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCreatedTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventSentTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventApplicationName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventClassName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceType"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceTypeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttribute"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeValue"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataValue"))
)
if mibBuilder.loadTexts:
    cedsMinorEvent.setStatus(
        "current"
    )

cedsInformationalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 2, 0, 4)
)
cedsInformationalEvent.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "cedsEventID"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventIDName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategory"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCategoryName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventCreatedTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventSentTime"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventApplicationName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventClassName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceType"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceTypeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttribute"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventResourceAttributeValue"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataName"),
        ("CISCO-EVENT-DISTR-MIB", "cedsEventUniqueDataValue"))
)
if mibBuilder.loadTexts:
    cedsInformationalEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoEventDistrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 3, 2, 2)
)
ciscoEventDistrNotificationGroup.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "cedsCriticalEvent"),
        ("CISCO-EVENT-DISTR-MIB", "cedsMajorEvent"),
        ("CISCO-EVENT-DISTR-MIB", "cedsMinorEvent"),
        ("CISCO-EVENT-DISTR-MIB", "cedsInformationalEvent"))
)
if mibBuilder.loadTexts:
    ciscoEventDistrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEventDistrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 127, 3, 1, 1)
)
ciscoEventDistrMIBCompliance.setObjects(
      *(("CISCO-EVENT-DISTR-MIB", "ciscoEventDistrMIBGroup"),
        ("CISCO-EVENT-DISTR-MIB", "ciscoEventDistrNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoEventDistrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EVENT-DISTR-MIB",
    **{"ciscoEventDistrMIB": ciscoEventDistrMIB,
       "ciscoEventDistrMIBObjects": ciscoEventDistrMIBObjects,
       "cedsEvent": cedsEvent,
       "cedsEventID": cedsEventID,
       "cedsEventIDName": cedsEventIDName,
       "cedsEventCategory": cedsEventCategory,
       "cedsEventCategoryName": cedsEventCategoryName,
       "cedsEventCreatedTime": cedsEventCreatedTime,
       "cedsEventSentTime": cedsEventSentTime,
       "cedsEventApplicationName": cedsEventApplicationName,
       "cedsEventClassName": cedsEventClassName,
       "cedsEventResourceType": cedsEventResourceType,
       "cedsEventResourceTypeName": cedsEventResourceTypeName,
       "cedsEventResourceAttribute": cedsEventResourceAttribute,
       "cedsEventResourceAttributeName": cedsEventResourceAttributeName,
       "cedsEventResourceAttributeValue": cedsEventResourceAttributeValue,
       "cedsEventUniqueDataName": cedsEventUniqueDataName,
       "cedsEventUniqueDataValue": cedsEventUniqueDataValue,
       "ciscoEventDistrMIBNotificationPrefix": ciscoEventDistrMIBNotificationPrefix,
       "ciscoEventDistrMIBNotifications": ciscoEventDistrMIBNotifications,
       "cedsCriticalEvent": cedsCriticalEvent,
       "cedsMajorEvent": cedsMajorEvent,
       "cedsMinorEvent": cedsMinorEvent,
       "cedsInformationalEvent": cedsInformationalEvent,
       "ciscoEventDistrMIBConformance": ciscoEventDistrMIBConformance,
       "ciscoEventDistrMIBCompliances": ciscoEventDistrMIBCompliances,
       "ciscoEventDistrMIBCompliance": ciscoEventDistrMIBCompliance,
       "ciscoEventDistrMIBGroups": ciscoEventDistrMIBGroups,
       "ciscoEventDistrMIBGroup": ciscoEventDistrMIBGroup,
       "ciscoEventDistrNotificationGroup": ciscoEventDistrNotificationGroup}
)
