# SNMP MIB module (APEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APEMS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

apEMSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8)
)
if mibBuilder.loadTexts:
    apEMSModule.setRevisions(
        ("2012-07-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApEMSMIBObjects_ObjectIdentity = ObjectIdentity
apEMSMIBObjects = _ApEMSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 1)
)
_ApEMSNotificationObjects_ObjectIdentity = ObjectIdentity
apEMSNotificationObjects = _ApEMSNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2)
)


class _ApEMSDiscoveryMode_Type(Integer32):
    """Custom type apEMSDiscoveryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("discovery", 1),
          ("reDiscovery", 2))
    )


_ApEMSDiscoveryMode_Type.__name__ = "Integer32"
_ApEMSDiscoveryMode_Object = MibScalar
apEMSDiscoveryMode = _ApEMSDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 1),
    _ApEMSDiscoveryMode_Type()
)
apEMSDiscoveryMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSDiscoveryMode.setStatus("current")
_ApEMSNodeID_Type = DisplayString
_ApEMSNodeID_Object = MibScalar
apEMSNodeID = _ApEMSNodeID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 2),
    _ApEMSNodeID_Type()
)
apEMSNodeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSNodeID.setStatus("current")
_ApEMSStartTime_Type = DisplayString
_ApEMSStartTime_Object = MibScalar
apEMSStartTime = _ApEMSStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 3),
    _ApEMSStartTime_Type()
)
apEMSStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSStartTime.setStatus("current")
_ApEMSDateTime_Type = DisplayString
_ApEMSDateTime_Object = MibScalar
apEMSDateTime = _ApEMSDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 4),
    _ApEMSDateTime_Type()
)
apEMSDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSDateTime.setStatus("current")
_ApEMSUser_Type = DisplayString
_ApEMSUser_Object = MibScalar
apEMSUser = _ApEMSUser_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 5),
    _ApEMSUser_Type()
)
apEMSUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSUser.setStatus("current")
_ApEMSDeviceAddress_Type = DisplayString
_ApEMSDeviceAddress_Object = MibScalar
apEMSDeviceAddress = _ApEMSDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 6),
    _ApEMSDeviceAddress_Type()
)
apEMSDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSDeviceAddress.setStatus("current")


class _ApEMSFunction_Type(Integer32):
    """Custom type apEMSFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("discovery", 1),
          ("reDiscovery", 2),
          ("save", 3))
    )


_ApEMSFunction_Type.__name__ = "Integer32"
_ApEMSFunction_Object = MibScalar
apEMSFunction = _ApEMSFunction_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 2, 7),
    _ApEMSFunction_Type()
)
apEMSFunction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apEMSFunction.setStatus("current")
_ApEMSNotifications_ObjectIdentity = ObjectIdentity
apEMSNotifications = _ApEMSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3)
)
_ApEMSConfigNotificationsPrefix_ObjectIdentity = ObjectIdentity
apEMSConfigNotificationsPrefix = _ApEMSConfigNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1)
)
_ApEMSConfigNotifications_ObjectIdentity = ObjectIdentity
apEMSConfigNotifications = _ApEMSConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0)
)
_ApEMSDeviceHealthNotificationsPrefix_ObjectIdentity = ObjectIdentity
apEMSDeviceHealthNotificationsPrefix = _ApEMSDeviceHealthNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2)
)
_ApEMSDeviceHealthNotifications_ObjectIdentity = ObjectIdentity
apEMSDeviceHealthNotifications = _ApEMSDeviceHealthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2, 0)
)
_ApEMSModuleConformance_ObjectIdentity = ObjectIdentity
apEMSModuleConformance = _ApEMSModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4)
)
_ApEMSGroups_ObjectIdentity = ObjectIdentity
apEMSGroups = _ApEMSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 1)
)
_ApEMSNotificationsGroups_ObjectIdentity = ObjectIdentity
apEMSNotificationsGroups = _ApEMSNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 2)
)
_ApEMSNotificationObjectsGroups_ObjectIdentity = ObjectIdentity
apEMSNotificationObjectsGroups = _ApEMSNotificationObjectsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 3)
)

# Managed Objects groups

apEMSNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 3, 1)
)
apEMSNotificationObjectsGroup.setObjects(
      *(("APEMS-MIB", "apEMSDiscoveryMode"),
        ("APEMS-MIB", "apEMSNodeID"),
        ("APEMS-MIB", "apEMSStartTime"),
        ("APEMS-MIB", "apEMSDateTime"),
        ("APEMS-MIB", "apEMSUser"),
        ("APEMS-MIB", "apEMSDeviceAddress"),
        ("APEMS-MIB", "apEMSFunction"))
)
if mibBuilder.loadTexts:
    apEMSNotificationObjectsGroup.setStatus("current")


# Notification objects

apEMSDiscoveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 1)
)
apEMSDiscoveryFailure.setObjects(
      *(("APEMS-MIB", "apEMSDiscoveryMode"),
        ("APEMS-MIB", "apEMSNodeID"),
        ("APEMS-MIB", "apEMSStartTime"),
        ("APEMS-MIB", "apEMSDateTime"),
        ("APEMS-MIB", "apEMSUser"))
)
if mibBuilder.loadTexts:
    apEMSDiscoveryFailure.setStatus(
        "current"
    )

apEMSSaveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 2)
)
apEMSSaveFailure.setObjects(
      *(("APEMS-MIB", "apEMSNodeID"),
        ("APEMS-MIB", "apEMSStartTime"),
        ("APEMS-MIB", "apEMSDateTime"),
        ("APEMS-MIB", "apEMSUser"))
)
if mibBuilder.loadTexts:
    apEMSSaveFailure.setStatus(
        "current"
    )

apEMSActivateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 3)
)
apEMSActivateFailure.setObjects(
      *(("APEMS-MIB", "apEMSNodeID"),
        ("APEMS-MIB", "apEMSStartTime"),
        ("APEMS-MIB", "apEMSDateTime"),
        ("APEMS-MIB", "apEMSUser"))
)
if mibBuilder.loadTexts:
    apEMSActivateFailure.setStatus(
        "current"
    )

apEMSInvalidConfigDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 4)
)
apEMSInvalidConfigDiscovered.setObjects(
      *(("APEMS-MIB", "apEMSNodeID"),
        ("APEMS-MIB", "apEMSDateTime"))
)
if mibBuilder.loadTexts:
    apEMSInvalidConfigDiscovered.setStatus(
        "current"
    )

apEMSInvalidConfigInventory = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 1, 0, 5)
)
apEMSInvalidConfigInventory.setObjects(
      *(("APEMS-MIB", "apEMSFunction"),
        ("APEMS-MIB", "apEMSNodeID"),
        ("APEMS-MIB", "apEMSStartTime"),
        ("APEMS-MIB", "apEMSDateTime"),
        ("APEMS-MIB", "apEMSUser"))
)
if mibBuilder.loadTexts:
    apEMSInvalidConfigInventory.setStatus(
        "current"
    )

apEMSNodeUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2, 0, 1)
)
apEMSNodeUnreachable.setObjects(
      *(("APEMS-MIB", "apEMSDeviceAddress"),
        ("APEMS-MIB", "apEMSDateTime"))
)
if mibBuilder.loadTexts:
    apEMSNodeUnreachable.setStatus(
        "current"
    )

apEMSNodeUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 3, 2, 0, 2)
)
apEMSNodeUnreachableClear.setObjects(
      *(("APEMS-MIB", "apEMSDeviceAddress"),
        ("APEMS-MIB", "apEMSDateTime"))
)
if mibBuilder.loadTexts:
    apEMSNodeUnreachableClear.setStatus(
        "current"
    )


# Notifications groups

apEMSConfigNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 2, 1)
)
apEMSConfigNotificationsGroup.setObjects(
      *(("APEMS-MIB", "apEMSDiscoveryFailure"),
        ("APEMS-MIB", "apEMSSaveFailure"),
        ("APEMS-MIB", "apEMSActivateFailure"),
        ("APEMS-MIB", "apEMSInvalidConfigDiscovered"))
)
if mibBuilder.loadTexts:
    apEMSConfigNotificationsGroup.setStatus(
        "current"
    )

apEMSDeviceHealthNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 4, 2, 2)
)
apEMSDeviceHealthNotificationsGroup.setObjects(
      *(("APEMS-MIB", "apEMSNodeUnreachable"),
        ("APEMS-MIB", "apEMSNodeUnreachableClear"))
)
if mibBuilder.loadTexts:
    apEMSDeviceHealthNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APEMS-MIB",
    **{"apEMSModule": apEMSModule,
       "apEMSMIBObjects": apEMSMIBObjects,
       "apEMSNotificationObjects": apEMSNotificationObjects,
       "apEMSDiscoveryMode": apEMSDiscoveryMode,
       "apEMSNodeID": apEMSNodeID,
       "apEMSStartTime": apEMSStartTime,
       "apEMSDateTime": apEMSDateTime,
       "apEMSUser": apEMSUser,
       "apEMSDeviceAddress": apEMSDeviceAddress,
       "apEMSFunction": apEMSFunction,
       "apEMSNotifications": apEMSNotifications,
       "apEMSConfigNotificationsPrefix": apEMSConfigNotificationsPrefix,
       "apEMSConfigNotifications": apEMSConfigNotifications,
       "apEMSDiscoveryFailure": apEMSDiscoveryFailure,
       "apEMSSaveFailure": apEMSSaveFailure,
       "apEMSActivateFailure": apEMSActivateFailure,
       "apEMSInvalidConfigDiscovered": apEMSInvalidConfigDiscovered,
       "apEMSInvalidConfigInventory": apEMSInvalidConfigInventory,
       "apEMSDeviceHealthNotificationsPrefix": apEMSDeviceHealthNotificationsPrefix,
       "apEMSDeviceHealthNotifications": apEMSDeviceHealthNotifications,
       "apEMSNodeUnreachable": apEMSNodeUnreachable,
       "apEMSNodeUnreachableClear": apEMSNodeUnreachableClear,
       "apEMSModuleConformance": apEMSModuleConformance,
       "apEMSGroups": apEMSGroups,
       "apEMSNotificationsGroups": apEMSNotificationsGroups,
       "apEMSConfigNotificationsGroup": apEMSConfigNotificationsGroup,
       "apEMSDeviceHealthNotificationsGroup": apEMSDeviceHealthNotificationsGroup,
       "apEMSNotificationObjectsGroups": apEMSNotificationObjectsGroups,
       "apEMSNotificationObjectsGroup": apEMSNotificationObjectsGroup}
)
