# SNMP MIB module (ARISTA-CV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-CV-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:35 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaCvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33)
)
if mibBuilder.loadTexts:
    aristaCvMIB.setRevisions(
        ("2023-05-02 00:00",
         "2022-07-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CvString(TextualConvention, OctetString):
    status = "current"
    displayHint = "65535t"


# MIB Managed Objects in the order of their OIDs

_AristaCvNotifications_ObjectIdentity = ObjectIdentity
aristaCvNotifications = _AristaCvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 0)
)
_AristaCvObjects_ObjectIdentity = ObjectIdentity
aristaCvObjects = _AristaCvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1)
)
_AristaCvAlertEventType_Type = CvString
_AristaCvAlertEventType_Object = MibScalar
aristaCvAlertEventType = _AristaCvAlertEventType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 1),
    _AristaCvAlertEventType_Type()
)
aristaCvAlertEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvAlertEventType.setStatus("current")
_AristaCvAlertDescription_Type = CvString
_AristaCvAlertDescription_Object = MibScalar
aristaCvAlertDescription = _AristaCvAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 2),
    _AristaCvAlertDescription_Type()
)
aristaCvAlertDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvAlertDescription.setStatus("current")


class _AristaCvAlertSeverity_Type(Integer32):
    """Custom type aristaCvAlertSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("info", 1),
          ("warning", 2),
          ("error", 3),
          ("critical", 4))
    )


_AristaCvAlertSeverity_Type.__name__ = "Integer32"
_AristaCvAlertSeverity_Object = MibScalar
aristaCvAlertSeverity = _AristaCvAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 3),
    _AristaCvAlertSeverity_Type()
)
aristaCvAlertSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvAlertSeverity.setStatus("current")
_AristaCvAlertTimestamp_Type = DateAndTime
_AristaCvAlertTimestamp_Object = MibScalar
aristaCvAlertTimestamp = _AristaCvAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 4),
    _AristaCvAlertTimestamp_Type()
)
aristaCvAlertTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvAlertTimestamp.setStatus("current")
_AristaCvAlertKey_Type = CvString
_AristaCvAlertKey_Object = MibScalar
aristaCvAlertKey = _AristaCvAlertKey_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 5),
    _AristaCvAlertKey_Type()
)
aristaCvAlertKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvAlertKey.setStatus("current")
_AristaCvAlertSource_Type = CvString
_AristaCvAlertSource_Object = MibScalar
aristaCvAlertSource = _AristaCvAlertSource_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 6),
    _AristaCvAlertSource_Type()
)
aristaCvAlertSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvAlertSource.setStatus("current")
_AristaCvComponents_Type = CvString
_AristaCvComponents_Object = MibScalar
aristaCvComponents = _AristaCvComponents_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 7),
    _AristaCvComponents_Type()
)
aristaCvComponents.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvComponents.setStatus("current")
_AristaCvRuleId_Type = CvString
_AristaCvRuleId_Object = MibScalar
aristaCvRuleId = _AristaCvRuleId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 8),
    _AristaCvRuleId_Type()
)
aristaCvRuleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aristaCvRuleId.setStatus("current")
_AristaCvConformance_ObjectIdentity = ObjectIdentity
aristaCvConformance = _AristaCvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 2)
)
_AristaCvCompliances_ObjectIdentity = ObjectIdentity
aristaCvCompliances = _AristaCvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 1)
)
_AristaCvGroups_ObjectIdentity = ObjectIdentity
aristaCvGroups = _AristaCvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 2)
)

# Managed Objects groups

aristaCvObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 2, 1)
)
aristaCvObjectsGroup.setObjects(
      *(("ARISTA-CV-MIB", "aristaCvAlertEventType"),
        ("ARISTA-CV-MIB", "aristaCvAlertDescription"),
        ("ARISTA-CV-MIB", "aristaCvAlertSeverity"),
        ("ARISTA-CV-MIB", "aristaCvAlertTimestamp"),
        ("ARISTA-CV-MIB", "aristaCvAlertKey"),
        ("ARISTA-CV-MIB", "aristaCvAlertSource"),
        ("ARISTA-CV-MIB", "aristaCvComponents"),
        ("ARISTA-CV-MIB", "aristaCvRuleId"))
)
if mibBuilder.loadTexts:
    aristaCvObjectsGroup.setStatus("current")


# Notification objects

aristaCvAlertFiringNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 0, 1)
)
aristaCvAlertFiringNotification.setObjects(
      *(("ARISTA-CV-MIB", "aristaCvAlertEventType"),
        ("ARISTA-CV-MIB", "aristaCvAlertDescription"),
        ("ARISTA-CV-MIB", "aristaCvAlertSeverity"),
        ("ARISTA-CV-MIB", "aristaCvAlertTimestamp"),
        ("ARISTA-CV-MIB", "aristaCvAlertKey"),
        ("ARISTA-CV-MIB", "aristaCvAlertSource"),
        ("ARISTA-CV-MIB", "aristaCvComponents"),
        ("ARISTA-CV-MIB", "aristaCvRuleId"))
)
if mibBuilder.loadTexts:
    aristaCvAlertFiringNotification.setStatus(
        "current"
    )

aristaCvAlertResolvedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 0, 2)
)
aristaCvAlertResolvedNotification.setObjects(
      *(("ARISTA-CV-MIB", "aristaCvAlertEventType"),
        ("ARISTA-CV-MIB", "aristaCvAlertDescription"),
        ("ARISTA-CV-MIB", "aristaCvAlertSeverity"),
        ("ARISTA-CV-MIB", "aristaCvAlertTimestamp"),
        ("ARISTA-CV-MIB", "aristaCvAlertKey"),
        ("ARISTA-CV-MIB", "aristaCvAlertSource"),
        ("ARISTA-CV-MIB", "aristaCvComponents"),
        ("ARISTA-CV-MIB", "aristaCvRuleId"))
)
if mibBuilder.loadTexts:
    aristaCvAlertResolvedNotification.setStatus(
        "current"
    )


# Notifications groups

aristaCvNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 2, 2)
)
aristaCvNotificationsGroup.setObjects(
      *(("ARISTA-CV-MIB", "aristaCvAlertFiringNotification"),
        ("ARISTA-CV-MIB", "aristaCvAlertResolvedNotification"))
)
if mibBuilder.loadTexts:
    aristaCvNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaCvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 1, 1)
)
aristaCvCompliance.setObjects(
      *(("ARISTA-CV-MIB", "aristaCvObjectsGroup"),
        ("ARISTA-CV-MIB", "aristaCvNotificationsGroup"))
)
if mibBuilder.loadTexts:
    aristaCvCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-CV-MIB",
    **{"CvString": CvString,
       "aristaCvMIB": aristaCvMIB,
       "aristaCvNotifications": aristaCvNotifications,
       "aristaCvAlertFiringNotification": aristaCvAlertFiringNotification,
       "aristaCvAlertResolvedNotification": aristaCvAlertResolvedNotification,
       "aristaCvObjects": aristaCvObjects,
       "aristaCvAlertEventType": aristaCvAlertEventType,
       "aristaCvAlertDescription": aristaCvAlertDescription,
       "aristaCvAlertSeverity": aristaCvAlertSeverity,
       "aristaCvAlertTimestamp": aristaCvAlertTimestamp,
       "aristaCvAlertKey": aristaCvAlertKey,
       "aristaCvAlertSource": aristaCvAlertSource,
       "aristaCvComponents": aristaCvComponents,
       "aristaCvRuleId": aristaCvRuleId,
       "aristaCvConformance": aristaCvConformance,
       "aristaCvCompliances": aristaCvCompliances,
       "aristaCvCompliance": aristaCvCompliance,
       "aristaCvGroups": aristaCvGroups,
       "aristaCvObjectsGroup": aristaCvObjectsGroup,
       "aristaCvNotificationsGroup": aristaCvNotificationsGroup}
)
