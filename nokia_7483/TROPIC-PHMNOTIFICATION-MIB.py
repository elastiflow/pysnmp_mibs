# SNMP MIB module (TROPIC-PHMNOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-PHMNOTIFICATION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tnPhMNotificationMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPhMNotificationMIB",
    "tnSystemModules")

(tnTrapCategory,
 tnTrapData,
 tnTrapDescr,
 tnTrapTime) = mibBuilder.importSymbols(
    "TROPIC-NOTIFICATION-MIB",
    "tnTrapCategory",
    "tnTrapData",
    "tnTrapDescr",
    "tnTrapTime")


# MODULE-IDENTITY

tnPhMNotificationMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnPhMNotificationMIBModule.setRevisions(
        ("2010-11-08 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnPhMNotificationConf_ObjectIdentity = ObjectIdentity
tnPhMNotificationConf = _TnPhMNotificationConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 1)
)
_TnPhMNotificationGroups_ObjectIdentity = ObjectIdentity
tnPhMNotificationGroups = _TnPhMNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 1, 1)
)
_TnPhMNotificationCompliances_ObjectIdentity = ObjectIdentity
tnPhMNotificationCompliances = _TnPhMNotificationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 1, 2)
)
_TnPhMNotificationObjs_ObjectIdentity = ObjectIdentity
tnPhMNotificationObjs = _TnPhMNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2)
)
_TnPhMNotifications_ObjectIdentity = ObjectIdentity
tnPhMNotifications = _TnPhMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1)
)
_TnSystemPhMNotifications_ObjectIdentity = ObjectIdentity
tnSystemPhMNotifications = _TnSystemPhMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1)
)
_TnV2SystemPhMNotifications_ObjectIdentity = ObjectIdentity
tnV2SystemPhMNotifications = _TnV2SystemPhMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0)
)

# Managed Objects groups


# Notification objects

tnEmsUndefinedConditionRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 1)
)
tnEmsUndefinedConditionRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsUndefinedConditionRaisedNotif.setStatus(
        "current"
    )

tnEmsUndefinedConditionClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 2)
)
tnEmsUndefinedConditionClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsUndefinedConditionClearedNotif.setStatus(
        "current"
    )

tnEmsTrapRegistrationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 3)
)
tnEmsTrapRegistrationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTrapRegistrationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsTrapRegistrationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 4)
)
tnEmsTrapRegistrationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTrapRegistrationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsActiveAlarmResyncFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 5)
)
tnEmsActiveAlarmResyncFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsActiveAlarmResyncFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsActiveAlarmResyncFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 6)
)
tnEmsActiveAlarmResyncFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsActiveAlarmResyncFailureClearedNotif.setStatus(
        "current"
    )

tnEmsHistoricalAlarmResyncFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 7)
)
tnEmsHistoricalAlarmResyncFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsHistoricalAlarmResyncFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsHistoricalAlarmResyncFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 8)
)
tnEmsHistoricalAlarmResyncFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsHistoricalAlarmResyncFailureClearedNotif.setStatus(
        "current"
    )

tnEmsCardOutOfSyncRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 9)
)
tnEmsCardOutOfSyncRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsCardOutOfSyncRaisedNotif.setStatus(
        "current"
    )

tnEmsCardOutOfSyncClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 10)
)
tnEmsCardOutOfSyncClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsCardOutOfSyncClearedNotif.setStatus(
        "current"
    )

tnEmsTopologyOutOfSyncRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 11)
)
tnEmsTopologyOutOfSyncRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTopologyOutOfSyncRaisedNotif.setStatus(
        "current"
    )

tnEmsTopologyOutOfSyncClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 12)
)
tnEmsTopologyOutOfSyncClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTopologyOutOfSyncClearedNotif.setStatus(
        "current"
    )

tnEmsUnknownNETypeRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 13)
)
tnEmsUnknownNETypeRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsUnknownNETypeRaisedNotif.setStatus(
        "current"
    )

tnEmsUnknownNETypeClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 14)
)
tnEmsUnknownNETypeClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsUnknownNETypeClearedNotif.setStatus(
        "current"
    )

tnEmsTunnelCreationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 15)
)
tnEmsTunnelCreationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTunnelCreationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsTunnelCreationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 16)
)
tnEmsTunnelCreationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTunnelCreationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsTunnelDeletionFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 17)
)
tnEmsTunnelDeletionFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTunnelDeletionFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsTunnelDeletionFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 18)
)
tnEmsTunnelDeletionFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsTunnelDeletionFailureClearedNotif.setStatus(
        "current"
    )

tnEmsSetEmsAsNTPServerFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 19)
)
tnEmsSetEmsAsNTPServerFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsSetEmsAsNTPServerFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsSetEmsAsNTPServerFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 20)
)
tnEmsSetEmsAsNTPServerFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsSetEmsAsNTPServerFailureClearedNotif.setStatus(
        "current"
    )

tnEmsPowerCommissionInProgressRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 21)
)
tnEmsPowerCommissionInProgressRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsPowerCommissionInProgressRaisedNotif.setStatus(
        "current"
    )

tnEmsPowerCommissionInProgressClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 22)
)
tnEmsPowerCommissionInProgressClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsPowerCommissionInProgressClearedNotif.setStatus(
        "current"
    )

tnEmsDuplicateNEMgmtIPAddressRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 23)
)
tnEmsDuplicateNEMgmtIPAddressRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsDuplicateNEMgmtIPAddressRaisedNotif.setStatus(
        "current"
    )

tnEmsDuplicateNEMgmtIPAddressClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 24)
)
tnEmsDuplicateNEMgmtIPAddressClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsDuplicateNEMgmtIPAddressClearedNotif.setStatus(
        "current"
    )

tnEmsDiscoveryFailedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 25)
)
tnEmsDiscoveryFailedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsDiscoveryFailedRaisedNotif.setStatus(
        "current"
    )

tnEmsDiscoveryFailedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 26)
)
tnEmsDiscoveryFailedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsDiscoveryFailedClearedNotif.setStatus(
        "current"
    )

tnEmsStandbyServerUnavailableRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 27)
)
tnEmsStandbyServerUnavailableRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsStandbyServerUnavailableRaisedNotif.setStatus(
        "current"
    )

tnEmsStandbyServerUnavailableClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 28)
)
tnEmsStandbyServerUnavailableClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsStandbyServerUnavailableClearedNotif.setStatus(
        "current"
    )

tnEmsLocalToRemoteDbReplicationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 29)
)
tnEmsLocalToRemoteDbReplicationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsLocalToRemoteDbReplicationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsLocalToRemoteDbReplicationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 30)
)
tnEmsLocalToRemoteDbReplicationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsLocalToRemoteDbReplicationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsRemoteToLocalDbReplicationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 31)
)
tnEmsRemoteToLocalDbReplicationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsRemoteToLocalDbReplicationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsRemoteToLocalDbReplicationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 32)
)
tnEmsRemoteToLocalDbReplicationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsRemoteToLocalDbReplicationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsNeBackupFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 33)
)
tnEmsNeBackupFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeBackupFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsNeBackupFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 34)
)
tnEmsNeBackupFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeBackupFailureClearedNotif.setStatus(
        "current"
    )

tnEmsNeBackupReplicationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 35)
)
tnEmsNeBackupReplicationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeBackupReplicationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsNeBackupReplicationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 36)
)
tnEmsNeBackupReplicationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeBackupReplicationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsNeSwdlFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 37)
)
tnEmsNeSwdlFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeSwdlFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsNeSwdlFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 38)
)
tnEmsNeSwdlFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeSwdlFailureClearedNotif.setStatus(
        "current"
    )

tnEmsNeSwdlPreactivationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 39)
)
tnEmsNeSwdlPreactivationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeSwdlPreactivationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsNeSwdlPreactivationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 40)
)
tnEmsNeSwdlPreactivationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsNeSwdlPreactivationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsServiceDefinitionDeletedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 41)
)
tnEmsServiceDefinitionDeletedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsServiceDefinitionDeletedRaisedNotif.setStatus(
        "current"
    )

tnEmsServiceDefinitionDeletedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 42)
)
tnEmsServiceDefinitionDeletedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsServiceDefinitionDeletedClearedNotif.setStatus(
        "current"
    )

tnEmsFileReplicationFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 43)
)
tnEmsFileReplicationFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsFileReplicationFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsFileReplicationFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 44)
)
tnEmsFileReplicationFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsFileReplicationFailureClearedNotif.setStatus(
        "current"
    )

tnEmsCommFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 45)
)
tnEmsCommFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsCommFailureRaisedNotif.setStatus(
        "current"
    )

tnEmsCommFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8, 2, 1, 1, 0, 46)
)
tnEmsCommFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnEmsCommFailureClearedNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-PHMNOTIFICATION-MIB",
    **{"tnPhMNotificationMIBModule": tnPhMNotificationMIBModule,
       "tnPhMNotificationConf": tnPhMNotificationConf,
       "tnPhMNotificationGroups": tnPhMNotificationGroups,
       "tnPhMNotificationCompliances": tnPhMNotificationCompliances,
       "tnPhMNotificationObjs": tnPhMNotificationObjs,
       "tnPhMNotifications": tnPhMNotifications,
       "tnSystemPhMNotifications": tnSystemPhMNotifications,
       "tnV2SystemPhMNotifications": tnV2SystemPhMNotifications,
       "tnEmsUndefinedConditionRaisedNotif": tnEmsUndefinedConditionRaisedNotif,
       "tnEmsUndefinedConditionClearedNotif": tnEmsUndefinedConditionClearedNotif,
       "tnEmsTrapRegistrationFailureRaisedNotif": tnEmsTrapRegistrationFailureRaisedNotif,
       "tnEmsTrapRegistrationFailureClearedNotif": tnEmsTrapRegistrationFailureClearedNotif,
       "tnEmsActiveAlarmResyncFailureRaisedNotif": tnEmsActiveAlarmResyncFailureRaisedNotif,
       "tnEmsActiveAlarmResyncFailureClearedNotif": tnEmsActiveAlarmResyncFailureClearedNotif,
       "tnEmsHistoricalAlarmResyncFailureRaisedNotif": tnEmsHistoricalAlarmResyncFailureRaisedNotif,
       "tnEmsHistoricalAlarmResyncFailureClearedNotif": tnEmsHistoricalAlarmResyncFailureClearedNotif,
       "tnEmsCardOutOfSyncRaisedNotif": tnEmsCardOutOfSyncRaisedNotif,
       "tnEmsCardOutOfSyncClearedNotif": tnEmsCardOutOfSyncClearedNotif,
       "tnEmsTopologyOutOfSyncRaisedNotif": tnEmsTopologyOutOfSyncRaisedNotif,
       "tnEmsTopologyOutOfSyncClearedNotif": tnEmsTopologyOutOfSyncClearedNotif,
       "tnEmsUnknownNETypeRaisedNotif": tnEmsUnknownNETypeRaisedNotif,
       "tnEmsUnknownNETypeClearedNotif": tnEmsUnknownNETypeClearedNotif,
       "tnEmsTunnelCreationFailureRaisedNotif": tnEmsTunnelCreationFailureRaisedNotif,
       "tnEmsTunnelCreationFailureClearedNotif": tnEmsTunnelCreationFailureClearedNotif,
       "tnEmsTunnelDeletionFailureRaisedNotif": tnEmsTunnelDeletionFailureRaisedNotif,
       "tnEmsTunnelDeletionFailureClearedNotif": tnEmsTunnelDeletionFailureClearedNotif,
       "tnEmsSetEmsAsNTPServerFailureRaisedNotif": tnEmsSetEmsAsNTPServerFailureRaisedNotif,
       "tnEmsSetEmsAsNTPServerFailureClearedNotif": tnEmsSetEmsAsNTPServerFailureClearedNotif,
       "tnEmsPowerCommissionInProgressRaisedNotif": tnEmsPowerCommissionInProgressRaisedNotif,
       "tnEmsPowerCommissionInProgressClearedNotif": tnEmsPowerCommissionInProgressClearedNotif,
       "tnEmsDuplicateNEMgmtIPAddressRaisedNotif": tnEmsDuplicateNEMgmtIPAddressRaisedNotif,
       "tnEmsDuplicateNEMgmtIPAddressClearedNotif": tnEmsDuplicateNEMgmtIPAddressClearedNotif,
       "tnEmsDiscoveryFailedRaisedNotif": tnEmsDiscoveryFailedRaisedNotif,
       "tnEmsDiscoveryFailedClearedNotif": tnEmsDiscoveryFailedClearedNotif,
       "tnEmsStandbyServerUnavailableRaisedNotif": tnEmsStandbyServerUnavailableRaisedNotif,
       "tnEmsStandbyServerUnavailableClearedNotif": tnEmsStandbyServerUnavailableClearedNotif,
       "tnEmsLocalToRemoteDbReplicationFailureRaisedNotif": tnEmsLocalToRemoteDbReplicationFailureRaisedNotif,
       "tnEmsLocalToRemoteDbReplicationFailureClearedNotif": tnEmsLocalToRemoteDbReplicationFailureClearedNotif,
       "tnEmsRemoteToLocalDbReplicationFailureRaisedNotif": tnEmsRemoteToLocalDbReplicationFailureRaisedNotif,
       "tnEmsRemoteToLocalDbReplicationFailureClearedNotif": tnEmsRemoteToLocalDbReplicationFailureClearedNotif,
       "tnEmsNeBackupFailureRaisedNotif": tnEmsNeBackupFailureRaisedNotif,
       "tnEmsNeBackupFailureClearedNotif": tnEmsNeBackupFailureClearedNotif,
       "tnEmsNeBackupReplicationFailureRaisedNotif": tnEmsNeBackupReplicationFailureRaisedNotif,
       "tnEmsNeBackupReplicationFailureClearedNotif": tnEmsNeBackupReplicationFailureClearedNotif,
       "tnEmsNeSwdlFailureRaisedNotif": tnEmsNeSwdlFailureRaisedNotif,
       "tnEmsNeSwdlFailureClearedNotif": tnEmsNeSwdlFailureClearedNotif,
       "tnEmsNeSwdlPreactivationFailureRaisedNotif": tnEmsNeSwdlPreactivationFailureRaisedNotif,
       "tnEmsNeSwdlPreactivationFailureClearedNotif": tnEmsNeSwdlPreactivationFailureClearedNotif,
       "tnEmsServiceDefinitionDeletedRaisedNotif": tnEmsServiceDefinitionDeletedRaisedNotif,
       "tnEmsServiceDefinitionDeletedClearedNotif": tnEmsServiceDefinitionDeletedClearedNotif,
       "tnEmsFileReplicationFailureRaisedNotif": tnEmsFileReplicationFailureRaisedNotif,
       "tnEmsFileReplicationFailureClearedNotif": tnEmsFileReplicationFailureClearedNotif,
       "tnEmsCommFailureRaisedNotif": tnEmsCommFailureRaisedNotif,
       "tnEmsCommFailureClearedNotif": tnEmsCommFailureClearedNotif}
)
