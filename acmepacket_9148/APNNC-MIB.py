# SNMP MIB module (APNNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APNNC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:26 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(apEMSModule,) = mibBuilder.importSymbols(
    "APEMS-MIB",
    "apEMSModule")

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

apNNCModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5)
)
if mibBuilder.loadTexts:
    apNNCModule.setRevisions(
        ("2012-08-20 00:00",
         "2012-07-16 00:00",
         "2013-10-11 00:00",
         "2013-10-14 00:00",
         "2014-02-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApNNCMIBObjects_ObjectIdentity = ObjectIdentity
apNNCMIBObjects = _ApNNCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 1)
)
_ApNNCNotificationObjects_ObjectIdentity = ObjectIdentity
apNNCNotificationObjects = _ApNNCNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2)
)
_ApNNCServerAddressRemote_Type = DisplayString
_ApNNCServerAddressRemote_Object = MibScalar
apNNCServerAddressRemote = _ApNNCServerAddressRemote_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 1),
    _ApNNCServerAddressRemote_Type()
)
apNNCServerAddressRemote.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerAddressRemote.setStatus("current")
_ApNNCServerNameRemote_Type = DisplayString
_ApNNCServerNameRemote_Object = MibScalar
apNNCServerNameRemote = _ApNNCServerNameRemote_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 2),
    _ApNNCServerNameRemote_Type()
)
apNNCServerNameRemote.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerNameRemote.setStatus("current")
_ApNNCServerAddressLocal_Type = DisplayString
_ApNNCServerAddressLocal_Object = MibScalar
apNNCServerAddressLocal = _ApNNCServerAddressLocal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 3),
    _ApNNCServerAddressLocal_Type()
)
apNNCServerAddressLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerAddressLocal.setStatus("current")
_ApNNCServerNameLocal_Type = DisplayString
_ApNNCServerNameLocal_Object = MibScalar
apNNCServerNameLocal = _ApNNCServerNameLocal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 4),
    _ApNNCServerNameLocal_Type()
)
apNNCServerNameLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerNameLocal.setStatus("current")


class _ApNNCFailureReason_Type(DisplayString):
    """Custom type apNNCFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApNNCFailureReason_Type.__name__ = "DisplayString"
_ApNNCFailureReason_Object = MibScalar
apNNCFailureReason = _ApNNCFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 5),
    _ApNNCFailureReason_Type()
)
apNNCFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCFailureReason.setStatus("current")
_ApNNCAggregationTimePercent_Type = DisplayString
_ApNNCAggregationTimePercent_Object = MibScalar
apNNCAggregationTimePercent = _ApNNCAggregationTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 6),
    _ApNNCAggregationTimePercent_Type()
)
apNNCAggregationTimePercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCAggregationTimePercent.setStatus("deprecated")
_ApNNCAggregationLagPercent_Type = Integer32
_ApNNCAggregationLagPercent_Object = MibScalar
apNNCAggregationLagPercent = _ApNNCAggregationLagPercent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 7),
    _ApNNCAggregationLagPercent_Type()
)
apNNCAggregationLagPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCAggregationLagPercent.setStatus("current")
if mibBuilder.loadTexts:
    apNNCAggregationLagPercent.setUnits("%")
_ApNNCNotifications_ObjectIdentity = ObjectIdentity
apNNCNotifications = _ApNNCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3)
)
_ApNNCServerHealthNotificationsPrefix_ObjectIdentity = ObjectIdentity
apNNCServerHealthNotificationsPrefix = _ApNNCServerHealthNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1)
)
_ApNNCServerHealthNotifications_ObjectIdentity = ObjectIdentity
apNNCServerHealthNotifications = _ApNNCServerHealthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0)
)
_ApNNCReportingNotificationsPrefix_ObjectIdentity = ObjectIdentity
apNNCReportingNotificationsPrefix = _ApNNCReportingNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2)
)
_ApNNCReportingNotifications_ObjectIdentity = ObjectIdentity
apNNCReportingNotifications = _ApNNCReportingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0)
)
_ApNNCModuleConformance_ObjectIdentity = ObjectIdentity
apNNCModuleConformance = _ApNNCModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4)
)
_ApNNCGroups_ObjectIdentity = ObjectIdentity
apNNCGroups = _ApNNCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 1)
)
_ApNNCNotificationsGroups_ObjectIdentity = ObjectIdentity
apNNCNotificationsGroups = _ApNNCNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2)
)
_ApNNCNotificationObjectsGroups_ObjectIdentity = ObjectIdentity
apNNCNotificationObjectsGroups = _ApNNCNotificationObjectsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3)
)

# Managed Objects groups

apNNCServerHealthObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 1)
)
apNNCServerHealthObjectsGroup.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCServerAddressRemote"),
        ("APNNC-MIB", "apNNCServerNameRemote"))
)
if mibBuilder.loadTexts:
    apNNCServerHealthObjectsGroup.setStatus("current")

apNNCFailureObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 2)
)
apNNCFailureObjectsGroup.setObjects(
    ("APNNC-MIB", "apNNCFailureReason")
)
if mibBuilder.loadTexts:
    apNNCFailureObjectsGroup.setStatus("current")

apNNCTimePercentObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 3)
)
apNNCTimePercentObjectsGroup.setObjects(
    ("APNNC-MIB", "apNNCAggregationTimePercent")
)
if mibBuilder.loadTexts:
    apNNCTimePercentObjectsGroup.setStatus("deprecated")

apNNCTimePercentObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 4)
)
apNNCTimePercentObjGroup.setObjects(
    ("APNNC-MIB", "apNNCAggregationLagPercent")
)
if mibBuilder.loadTexts:
    apNNCTimePercentObjGroup.setStatus("current")


# Notification objects

apNNCServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 1)
)
apNNCServerUnreachable.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCServerAddressRemote"),
        ("APNNC-MIB", "apNNCServerNameRemote"))
)
if mibBuilder.loadTexts:
    apNNCServerUnreachable.setStatus(
        "current"
    )

apNNCServerUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 2)
)
apNNCServerUnreachableClear.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCServerAddressRemote"),
        ("APNNC-MIB", "apNNCServerNameRemote"))
)
if mibBuilder.loadTexts:
    apNNCServerUnreachableClear.setStatus(
        "current"
    )

apNNCReportingHdrDetectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 1)
)
apNNCReportingHdrDetectionFailure.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCFailureReason"))
)
if mibBuilder.loadTexts:
    apNNCReportingHdrDetectionFailure.setStatus(
        "current"
    )

apNNCReportingHdrAggregationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 2)
)
apNNCReportingHdrAggregationFailure.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCFailureReason"),
        ("APNNC-MIB", "apNNCAggregationTimePercent"))
)
if mibBuilder.loadTexts:
    apNNCReportingHdrAggregationFailure.setStatus(
        "deprecated"
    )

apNNCReportingHdrAggregationFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 3)
)
apNNCReportingHdrAggregationFailureClear.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCFailureReason"),
        ("APNNC-MIB", "apNNCAggregationTimePercent"))
)
if mibBuilder.loadTexts:
    apNNCReportingHdrAggregationFailureClear.setStatus(
        "deprecated"
    )

apNNCReportingHdrAggregationLagFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 4)
)
apNNCReportingHdrAggregationLagFailure.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCFailureReason"),
        ("APNNC-MIB", "apNNCAggregationLagPercent"))
)
if mibBuilder.loadTexts:
    apNNCReportingHdrAggregationLagFailure.setStatus(
        "current"
    )

apNNCReportingHdrAggregationLagFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 2, 0, 5)
)
apNNCReportingHdrAggregationLagFailureClear.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCFailureReason"),
        ("APNNC-MIB", "apNNCAggregationLagPercent"))
)
if mibBuilder.loadTexts:
    apNNCReportingHdrAggregationLagFailureClear.setStatus(
        "current"
    )


# Notifications groups

apNNCServerHealthNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 1)
)
apNNCServerHealthNotificationsGroup.setObjects(
      *(("APNNC-MIB", "apNNCServerUnreachable"),
        ("APNNC-MIB", "apNNCServerUnreachableClear"))
)
if mibBuilder.loadTexts:
    apNNCServerHealthNotificationsGroup.setStatus(
        "current"
    )

apNNCReportingNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 2)
)
apNNCReportingNotificationsGroup.setObjects(
    ("APNNC-MIB", "apNNCReportingHdrDetectionFailure")
)
if mibBuilder.loadTexts:
    apNNCReportingNotificationsGroup.setStatus(
        "current"
    )

apNNCReportingAggrNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 3)
)
apNNCReportingAggrNotifsGroup.setObjects(
      *(("APNNC-MIB", "apNNCReportingHdrAggregationFailure"),
        ("APNNC-MIB", "apNNCReportingHdrAggregationFailureClear"))
)
if mibBuilder.loadTexts:
    apNNCReportingAggrNotifsGroup.setStatus(
        "deprecated"
    )

apNNCReportingAggregationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 4)
)
apNNCReportingAggregationNotificationGroup.setObjects(
      *(("APNNC-MIB", "apNNCReportingHdrAggregationLagFailure"),
        ("APNNC-MIB", "apNNCReportingHdrAggregationLagFailureClear"))
)
if mibBuilder.loadTexts:
    apNNCReportingAggregationNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APNNC-MIB",
    **{"apNNCModule": apNNCModule,
       "apNNCMIBObjects": apNNCMIBObjects,
       "apNNCNotificationObjects": apNNCNotificationObjects,
       "apNNCServerAddressRemote": apNNCServerAddressRemote,
       "apNNCServerNameRemote": apNNCServerNameRemote,
       "apNNCServerAddressLocal": apNNCServerAddressLocal,
       "apNNCServerNameLocal": apNNCServerNameLocal,
       "apNNCFailureReason": apNNCFailureReason,
       "apNNCAggregationTimePercent": apNNCAggregationTimePercent,
       "apNNCAggregationLagPercent": apNNCAggregationLagPercent,
       "apNNCNotifications": apNNCNotifications,
       "apNNCServerHealthNotificationsPrefix": apNNCServerHealthNotificationsPrefix,
       "apNNCServerHealthNotifications": apNNCServerHealthNotifications,
       "apNNCServerUnreachable": apNNCServerUnreachable,
       "apNNCServerUnreachableClear": apNNCServerUnreachableClear,
       "apNNCReportingNotificationsPrefix": apNNCReportingNotificationsPrefix,
       "apNNCReportingNotifications": apNNCReportingNotifications,
       "apNNCReportingHdrDetectionFailure": apNNCReportingHdrDetectionFailure,
       "apNNCReportingHdrAggregationFailure": apNNCReportingHdrAggregationFailure,
       "apNNCReportingHdrAggregationFailureClear": apNNCReportingHdrAggregationFailureClear,
       "apNNCReportingHdrAggregationLagFailure": apNNCReportingHdrAggregationLagFailure,
       "apNNCReportingHdrAggregationLagFailureClear": apNNCReportingHdrAggregationLagFailureClear,
       "apNNCModuleConformance": apNNCModuleConformance,
       "apNNCGroups": apNNCGroups,
       "apNNCNotificationsGroups": apNNCNotificationsGroups,
       "apNNCServerHealthNotificationsGroup": apNNCServerHealthNotificationsGroup,
       "apNNCReportingNotificationsGroup": apNNCReportingNotificationsGroup,
       "apNNCReportingAggrNotifsGroup": apNNCReportingAggrNotifsGroup,
       "apNNCReportingAggregationNotificationGroup": apNNCReportingAggregationNotificationGroup,
       "apNNCNotificationObjectsGroups": apNNCNotificationObjectsGroups,
       "apNNCServerHealthObjectsGroup": apNNCServerHealthObjectsGroup,
       "apNNCFailureObjectsGroup": apNNCFailureObjectsGroup,
       "apNNCTimePercentObjectsGroup": apNNCTimePercentObjectsGroup,
       "apNNCTimePercentObjGroup": apNNCTimePercentObjGroup}
)
