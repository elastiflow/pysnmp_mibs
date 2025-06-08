# SNMP MIB module (TROPIC-GMPLS-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-GMPLS-NOTIFICATION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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

(tnGmplsMIBModules,) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnGmplsMIBModules")

(tnNotificationObjs,
 tnTrapCategory,
 tnTrapCondition,
 tnTrapData,
 tnTrapDescr,
 tnTrapEntityType,
 tnTrapObjectID,
 tnTrapObjectIDType,
 tnTrapServiceAffecting,
 tnTrapTime) = mibBuilder.importSymbols(
    "TROPIC-NOTIFICATION-MIB",
    "tnNotificationObjs",
    "tnTrapCategory",
    "tnTrapCondition",
    "tnTrapData",
    "tnTrapDescr",
    "tnTrapEntityType",
    "tnTrapObjectID",
    "tnTrapObjectIDType",
    "tnTrapServiceAffecting",
    "tnTrapTime")


# MODULE-IDENTITY

tnGmplsNotificationMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    tnGmplsNotificationMIBModule.setRevisions(
        ("2013-06-27 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnNotificationsGmpls_ObjectIdentity = ObjectIdentity
tnNotificationsGmpls = _TnNotificationsGmpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8)
)
_TnAlarmNotificationsGmpls_ObjectIdentity = ObjectIdentity
tnAlarmNotificationsGmpls = _TnAlarmNotificationsGmpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1)
)
_TnAlarmNotificationsGmplsNode_ObjectIdentity = ObjectIdentity
tnAlarmNotificationsGmplsNode = _TnAlarmNotificationsGmplsNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1)
)
_TnAlarmNotificationsGmplsCpif_ObjectIdentity = ObjectIdentity
tnAlarmNotificationsGmplsCpif = _TnAlarmNotificationsGmplsCpif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3)
)
_TnAlarmNotificationsGmplsLsp_ObjectIdentity = ObjectIdentity
tnAlarmNotificationsGmplsLsp = _TnAlarmNotificationsGmplsLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4)
)
_TnEventNotificationsGmpls_ObjectIdentity = ObjectIdentity
tnEventNotificationsGmpls = _TnEventNotificationsGmpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2)
)
_TnEventNotificationsGmplsLsp_ObjectIdentity = ObjectIdentity
tnEventNotificationsGmplsLsp = _TnEventNotificationsGmplsLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 1)
)
_TnEventNotificationsGmplsDpif_ObjectIdentity = ObjectIdentity
tnEventNotificationsGmplsDpif = _TnEventNotificationsGmplsDpif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 2)
)
_TnEventNotificationsGmplsCpif_ObjectIdentity = ObjectIdentity
tnEventNotificationsGmplsCpif = _TnEventNotificationsGmplsCpif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3)
)

# Managed Objects groups


# Notification objects

tnGmplsRestorationDisabledRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 1)
)
tnGmplsRestorationDisabledRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsRestorationDisabledRaisedNotif.setStatus(
        "current"
    )

tnGmplsRestorationDisabledClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 2)
)
tnGmplsRestorationDisabledClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsRestorationDisabledClearedNotif.setStatus(
        "current"
    )

tnGmplsNodeDegradedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 3)
)
tnGmplsNodeDegradedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsNodeDegradedRaisedNotif.setStatus(
        "current"
    )

tnGmplsNodeDegradedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 4)
)
tnGmplsNodeDegradedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsNodeDegradedClearedNotif.setStatus(
        "current"
    )

tnGmplsInMigrationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 5)
)
tnGmplsInMigrationRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsInMigrationRaisedNotif.setStatus(
        "current"
    )

tnGmplsInMigrationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 6)
)
tnGmplsInMigrationClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsInMigrationClearedNotif.setStatus(
        "current"
    )

tnGmplsSubnodeUnreachableRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 7)
)
tnGmplsSubnodeUnreachableRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsSubnodeUnreachableRaisedNotif.setStatus(
        "current"
    )

tnGmplsSubnodeUnreachableClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 8)
)
tnGmplsSubnodeUnreachableClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsSubnodeUnreachableClearedNotif.setStatus(
        "current"
    )

tnGmplsNeUnreachableRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 9)
)
tnGmplsNeUnreachableRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapServiceAffecting"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsNeUnreachableRaisedNotif.setStatus(
        "current"
    )

tnGmplsNeUnreachableClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 10)
)
tnGmplsNeUnreachableClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapServiceAffecting"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsNeUnreachableClearedNotif.setStatus(
        "current"
    )

tnGmplsOpticalParameterFileErrRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 11)
)
tnGmplsOpticalParameterFileErrRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapServiceAffecting"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsOpticalParameterFileErrRaisedNotif.setStatus(
        "current"
    )

tnGmplsOpticalParameterFileErrClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 12)
)
tnGmplsOpticalParameterFileErrClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapServiceAffecting"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsOpticalParameterFileErrClearedNotif.setStatus(
        "current"
    )

tnGmplsEptUploadErrRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 13)
)
tnGmplsEptUploadErrRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapServiceAffecting"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsEptUploadErrRaisedNotif.setStatus(
        "current"
    )

tnGmplsEptUploadErrClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 1, 14)
)
tnGmplsEptUploadErrClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapServiceAffecting"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsEptUploadErrClearedNotif.setStatus(
        "current"
    )

tnGmplsCPNbrCommunicationDownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 1)
)
tnGmplsCPNbrCommunicationDownRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrCommunicationDownRaisedNotif.setStatus(
        "current"
    )

tnGmplsCPNbrCommunicationDownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 2)
)
tnGmplsCPNbrCommunicationDownClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrCommunicationDownClearedNotif.setStatus(
        "current"
    )

tnGmplsCPNbrCommunicationDegradedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 3)
)
tnGmplsCPNbrCommunicationDegradedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrCommunicationDegradedRaisedNotif.setStatus(
        "current"
    )

tnGmplsCPNbrCommunicationDegradedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 4)
)
tnGmplsCPNbrCommunicationDegradedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrCommunicationDegradedClearedNotif.setStatus(
        "current"
    )

tnGmplsRsvpCommunicationDownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 5)
)
tnGmplsRsvpCommunicationDownRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpCommunicationDownRaisedNotif.setStatus(
        "current"
    )

tnGmplsRsvpCommunicationDownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 6)
)
tnGmplsRsvpCommunicationDownClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpCommunicationDownClearedNotif.setStatus(
        "current"
    )

tnGmplsRsvpCommunicationDegradedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 7)
)
tnGmplsRsvpCommunicationDegradedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpCommunicationDegradedRaisedNotif.setStatus(
        "current"
    )

tnGmplsRsvpCommunicationDegradedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 8)
)
tnGmplsRsvpCommunicationDegradedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpCommunicationDegradedClearedNotif.setStatus(
        "current"
    )

tnGmplsDprCommunicationDownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 9)
)
tnGmplsDprCommunicationDownRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsDprCommunicationDownRaisedNotif.setStatus(
        "current"
    )

tnGmplsDprCommunicationDownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 10)
)
tnGmplsDprCommunicationDownClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsDprCommunicationDownClearedNotif.setStatus(
        "current"
    )

tnGmplsDprCommunicationDegradedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 11)
)
tnGmplsDprCommunicationDegradedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsDprCommunicationDegradedRaisedNotif.setStatus(
        "current"
    )

tnGmplsDprCommunicationDegradedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 12)
)
tnGmplsDprCommunicationDegradedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsDprCommunicationDegradedClearedNotif.setStatus(
        "current"
    )

tnGmplsDprNetworkVersionMismatchRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 13)
)
tnGmplsDprNetworkVersionMismatchRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsDprNetworkVersionMismatchRaisedNotif.setStatus(
        "current"
    )

tnGmplsDprNetworkVersionMismatchClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 14)
)
tnGmplsDprNetworkVersionMismatchClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsDprNetworkVersionMismatchClearedNotif.setStatus(
        "current"
    )

tnGmplsLmpCommunicationDownRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 15)
)
tnGmplsLmpCommunicationDownRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpCommunicationDownRaisedNotif.setStatus(
        "current"
    )

tnGmplsLmpCommunicationDownClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 16)
)
tnGmplsLmpCommunicationDownClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpCommunicationDownClearedNotif.setStatus(
        "current"
    )

tnGmplsLmpCommunicationDegradedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 17)
)
tnGmplsLmpCommunicationDegradedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpCommunicationDegradedRaisedNotif.setStatus(
        "current"
    )

tnGmplsLmpCommunicationDegradedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 3, 18)
)
tnGmplsLmpCommunicationDegradedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpCommunicationDegradedClearedNotif.setStatus(
        "current"
    )

tnGmplsLspReroutedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 1)
)
tnGmplsLspReroutedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspReroutedRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspReroutedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 2)
)
tnGmplsLspReroutedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspReroutedClearedNotif.setStatus(
        "current"
    )

tnGmplsLspReversionBlockedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 3)
)
tnGmplsLspReversionBlockedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspReversionBlockedRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspReversionBlockedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 4)
)
tnGmplsLspReversionBlockedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspReversionBlockedClearedNotif.setStatus(
        "current"
    )

tnGmplsLspBackupUnavailRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 5)
)
tnGmplsLspBackupUnavailRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspBackupUnavailRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspBackupUnavailClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 6)
)
tnGmplsLspBackupUnavailClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspBackupUnavailClearedNotif.setStatus(
        "current"
    )

tnGmplsLspActiveFailedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 7)
)
tnGmplsLspActiveFailedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspActiveFailedRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspActiveFailedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 8)
)
tnGmplsLspActiveFailedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspActiveFailedClearedNotif.setStatus(
        "current"
    )

tnGmplsLspNominalUnavailRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 9)
)
tnGmplsLspNominalUnavailRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspNominalUnavailRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspNominalUnavailClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 10)
)
tnGmplsLspNominalUnavailClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspNominalUnavailClearedNotif.setStatus(
        "current"
    )

tnGmplsLspActiveDegradedRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 11)
)
tnGmplsLspActiveDegradedRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspActiveDegradedRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspActiveDegradedClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 12)
)
tnGmplsLspActiveDegradedClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspActiveDegradedClearedNotif.setStatus(
        "current"
    )

tnGmplsLspChannelViolationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 13)
)
tnGmplsLspChannelViolationRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspChannelViolationRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspChannelViolationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 14)
)
tnGmplsLspChannelViolationClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspChannelViolationClearedNotif.setStatus(
        "current"
    )

tnGmplsLspColorViolationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 15)
)
tnGmplsLspColorViolationRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspColorViolationRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspColorViolationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 16)
)
tnGmplsLspColorViolationClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspColorViolationClearedNotif.setStatus(
        "current"
    )

tnGmplsLspOpticalFeasibilityViolationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 17)
)
tnGmplsLspOpticalFeasibilityViolationRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspOpticalFeasibilityViolationRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspOpticalFeasibilityViolationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 18)
)
tnGmplsLspOpticalFeasibilityViolationClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspOpticalFeasibilityViolationClearedNotif.setStatus(
        "current"
    )

tnGmplsLspSRGViolationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 19)
)
tnGmplsLspSRGViolationRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspSRGViolationRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspSRGViolationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 20)
)
tnGmplsLspSRGViolationClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspSRGViolationClearedNotif.setStatus(
        "current"
    )

tnGmplsLspLinkDiversityViolationRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 21)
)
tnGmplsLspLinkDiversityViolationRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspLinkDiversityViolationRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspLinkDiversityViolationClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 22)
)
tnGmplsLspLinkDiversityViolationClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspLinkDiversityViolationClearedNotif.setStatus(
        "current"
    )

tnGmplsLspApeInProgressRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 23)
)
tnGmplsLspApeInProgressRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspApeInProgressRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspApeInProgressClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 24)
)
tnGmplsLspApeInProgressClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspApeInProgressClearedNotif.setStatus(
        "current"
    )

tnGmplsLspTestModeRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 25)
)
tnGmplsLspTestModeRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspTestModeRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspTestModeClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 26)
)
tnGmplsLspTestModeClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspTestModeClearedNotif.setStatus(
        "current"
    )

tnGmplsLspReadyToRevertRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 27)
)
tnGmplsLspReadyToRevertRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspReadyToRevertRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspReadyToRevertClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 28)
)
tnGmplsLspReadyToRevertClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspReadyToRevertClearedNotif.setStatus(
        "current"
    )

tnGmplsLspEndpointFailureRaisedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 29)
)
tnGmplsLspEndpointFailureRaisedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspEndpointFailureRaisedNotif.setStatus(
        "current"
    )

tnGmplsLspEndpointFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 1, 4, 30)
)
tnGmplsLspEndpointFailureClearedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapEntityType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCondition"))
)
if mibBuilder.loadTexts:
    tnGmplsLspEndpointFailureClearedNotif.setStatus(
        "current"
    )

tnGmplsLspCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 1, 1)
)
tnGmplsLspCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsLspCreatedNotif.setStatus(
        "current"
    )

tnGmplsLspDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 1, 2)
)
tnGmplsLspDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsLspDeletedNotif.setStatus(
        "current"
    )

tnGmplsDBLinkCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 2, 1)
)
tnGmplsDBLinkCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsDBLinkCreatedNotif.setStatus(
        "current"
    )

tnGmplsDBLinkDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 2, 2)
)
tnGmplsDBLinkDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsDBLinkDeletedNotif.setStatus(
        "current"
    )

tnGmplsTELinkCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 2, 3)
)
tnGmplsTELinkCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsTELinkCreatedNotif.setStatus(
        "current"
    )

tnGmplsTELinkDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 2, 4)
)
tnGmplsTELinkDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsTELinkDeletedNotif.setStatus(
        "current"
    )

tnGmplsCPNbrCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 1)
)
tnGmplsCPNbrCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrCreatedNotif.setStatus(
        "current"
    )

tnGmplsCPNbrDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 2)
)
tnGmplsCPNbrDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsCPNbrDeletedNotif.setStatus(
        "current"
    )

tnGmplsRsvpIfCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 3)
)
tnGmplsRsvpIfCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpIfCreatedNotif.setStatus(
        "current"
    )

tnGmplsRsvpIfDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 4)
)
tnGmplsRsvpIfDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsRsvpIfDeletedNotif.setStatus(
        "current"
    )

tnGmplsDprIfCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 5)
)
tnGmplsDprIfCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsDprIfCreatedNotif.setStatus(
        "current"
    )

tnGmplsDprIfDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 6)
)
tnGmplsDprIfDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsDprIfDeletedNotif.setStatus(
        "current"
    )

tnGmplsLmpIfCreatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 7)
)
tnGmplsLmpIfCreatedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpIfCreatedNotif.setStatus(
        "current"
    )

tnGmplsLmpIfDeletedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2, 2, 8, 2, 3, 8)
)
tnGmplsLmpIfDeletedNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectIDType"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapObjectID"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnGmplsLmpIfDeletedNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GMPLS-NOTIFICATION-MIB",
    **{"tnGmplsNotificationMIBModule": tnGmplsNotificationMIBModule,
       "tnNotificationsGmpls": tnNotificationsGmpls,
       "tnAlarmNotificationsGmpls": tnAlarmNotificationsGmpls,
       "tnAlarmNotificationsGmplsNode": tnAlarmNotificationsGmplsNode,
       "tnGmplsRestorationDisabledRaisedNotif": tnGmplsRestorationDisabledRaisedNotif,
       "tnGmplsRestorationDisabledClearedNotif": tnGmplsRestorationDisabledClearedNotif,
       "tnGmplsNodeDegradedRaisedNotif": tnGmplsNodeDegradedRaisedNotif,
       "tnGmplsNodeDegradedClearedNotif": tnGmplsNodeDegradedClearedNotif,
       "tnGmplsInMigrationRaisedNotif": tnGmplsInMigrationRaisedNotif,
       "tnGmplsInMigrationClearedNotif": tnGmplsInMigrationClearedNotif,
       "tnGmplsSubnodeUnreachableRaisedNotif": tnGmplsSubnodeUnreachableRaisedNotif,
       "tnGmplsSubnodeUnreachableClearedNotif": tnGmplsSubnodeUnreachableClearedNotif,
       "tnGmplsNeUnreachableRaisedNotif": tnGmplsNeUnreachableRaisedNotif,
       "tnGmplsNeUnreachableClearedNotif": tnGmplsNeUnreachableClearedNotif,
       "tnGmplsOpticalParameterFileErrRaisedNotif": tnGmplsOpticalParameterFileErrRaisedNotif,
       "tnGmplsOpticalParameterFileErrClearedNotif": tnGmplsOpticalParameterFileErrClearedNotif,
       "tnGmplsEptUploadErrRaisedNotif": tnGmplsEptUploadErrRaisedNotif,
       "tnGmplsEptUploadErrClearedNotif": tnGmplsEptUploadErrClearedNotif,
       "tnAlarmNotificationsGmplsCpif": tnAlarmNotificationsGmplsCpif,
       "tnGmplsCPNbrCommunicationDownRaisedNotif": tnGmplsCPNbrCommunicationDownRaisedNotif,
       "tnGmplsCPNbrCommunicationDownClearedNotif": tnGmplsCPNbrCommunicationDownClearedNotif,
       "tnGmplsCPNbrCommunicationDegradedRaisedNotif": tnGmplsCPNbrCommunicationDegradedRaisedNotif,
       "tnGmplsCPNbrCommunicationDegradedClearedNotif": tnGmplsCPNbrCommunicationDegradedClearedNotif,
       "tnGmplsRsvpCommunicationDownRaisedNotif": tnGmplsRsvpCommunicationDownRaisedNotif,
       "tnGmplsRsvpCommunicationDownClearedNotif": tnGmplsRsvpCommunicationDownClearedNotif,
       "tnGmplsRsvpCommunicationDegradedRaisedNotif": tnGmplsRsvpCommunicationDegradedRaisedNotif,
       "tnGmplsRsvpCommunicationDegradedClearedNotif": tnGmplsRsvpCommunicationDegradedClearedNotif,
       "tnGmplsDprCommunicationDownRaisedNotif": tnGmplsDprCommunicationDownRaisedNotif,
       "tnGmplsDprCommunicationDownClearedNotif": tnGmplsDprCommunicationDownClearedNotif,
       "tnGmplsDprCommunicationDegradedRaisedNotif": tnGmplsDprCommunicationDegradedRaisedNotif,
       "tnGmplsDprCommunicationDegradedClearedNotif": tnGmplsDprCommunicationDegradedClearedNotif,
       "tnGmplsDprNetworkVersionMismatchRaisedNotif": tnGmplsDprNetworkVersionMismatchRaisedNotif,
       "tnGmplsDprNetworkVersionMismatchClearedNotif": tnGmplsDprNetworkVersionMismatchClearedNotif,
       "tnGmplsLmpCommunicationDownRaisedNotif": tnGmplsLmpCommunicationDownRaisedNotif,
       "tnGmplsLmpCommunicationDownClearedNotif": tnGmplsLmpCommunicationDownClearedNotif,
       "tnGmplsLmpCommunicationDegradedRaisedNotif": tnGmplsLmpCommunicationDegradedRaisedNotif,
       "tnGmplsLmpCommunicationDegradedClearedNotif": tnGmplsLmpCommunicationDegradedClearedNotif,
       "tnAlarmNotificationsGmplsLsp": tnAlarmNotificationsGmplsLsp,
       "tnGmplsLspReroutedRaisedNotif": tnGmplsLspReroutedRaisedNotif,
       "tnGmplsLspReroutedClearedNotif": tnGmplsLspReroutedClearedNotif,
       "tnGmplsLspReversionBlockedRaisedNotif": tnGmplsLspReversionBlockedRaisedNotif,
       "tnGmplsLspReversionBlockedClearedNotif": tnGmplsLspReversionBlockedClearedNotif,
       "tnGmplsLspBackupUnavailRaisedNotif": tnGmplsLspBackupUnavailRaisedNotif,
       "tnGmplsLspBackupUnavailClearedNotif": tnGmplsLspBackupUnavailClearedNotif,
       "tnGmplsLspActiveFailedRaisedNotif": tnGmplsLspActiveFailedRaisedNotif,
       "tnGmplsLspActiveFailedClearedNotif": tnGmplsLspActiveFailedClearedNotif,
       "tnGmplsLspNominalUnavailRaisedNotif": tnGmplsLspNominalUnavailRaisedNotif,
       "tnGmplsLspNominalUnavailClearedNotif": tnGmplsLspNominalUnavailClearedNotif,
       "tnGmplsLspActiveDegradedRaisedNotif": tnGmplsLspActiveDegradedRaisedNotif,
       "tnGmplsLspActiveDegradedClearedNotif": tnGmplsLspActiveDegradedClearedNotif,
       "tnGmplsLspChannelViolationRaisedNotif": tnGmplsLspChannelViolationRaisedNotif,
       "tnGmplsLspChannelViolationClearedNotif": tnGmplsLspChannelViolationClearedNotif,
       "tnGmplsLspColorViolationRaisedNotif": tnGmplsLspColorViolationRaisedNotif,
       "tnGmplsLspColorViolationClearedNotif": tnGmplsLspColorViolationClearedNotif,
       "tnGmplsLspOpticalFeasibilityViolationRaisedNotif": tnGmplsLspOpticalFeasibilityViolationRaisedNotif,
       "tnGmplsLspOpticalFeasibilityViolationClearedNotif": tnGmplsLspOpticalFeasibilityViolationClearedNotif,
       "tnGmplsLspSRGViolationRaisedNotif": tnGmplsLspSRGViolationRaisedNotif,
       "tnGmplsLspSRGViolationClearedNotif": tnGmplsLspSRGViolationClearedNotif,
       "tnGmplsLspLinkDiversityViolationRaisedNotif": tnGmplsLspLinkDiversityViolationRaisedNotif,
       "tnGmplsLspLinkDiversityViolationClearedNotif": tnGmplsLspLinkDiversityViolationClearedNotif,
       "tnGmplsLspApeInProgressRaisedNotif": tnGmplsLspApeInProgressRaisedNotif,
       "tnGmplsLspApeInProgressClearedNotif": tnGmplsLspApeInProgressClearedNotif,
       "tnGmplsLspTestModeRaisedNotif": tnGmplsLspTestModeRaisedNotif,
       "tnGmplsLspTestModeClearedNotif": tnGmplsLspTestModeClearedNotif,
       "tnGmplsLspReadyToRevertRaisedNotif": tnGmplsLspReadyToRevertRaisedNotif,
       "tnGmplsLspReadyToRevertClearedNotif": tnGmplsLspReadyToRevertClearedNotif,
       "tnGmplsLspEndpointFailureRaisedNotif": tnGmplsLspEndpointFailureRaisedNotif,
       "tnGmplsLspEndpointFailureClearedNotif": tnGmplsLspEndpointFailureClearedNotif,
       "tnEventNotificationsGmpls": tnEventNotificationsGmpls,
       "tnEventNotificationsGmplsLsp": tnEventNotificationsGmplsLsp,
       "tnGmplsLspCreatedNotif": tnGmplsLspCreatedNotif,
       "tnGmplsLspDeletedNotif": tnGmplsLspDeletedNotif,
       "tnEventNotificationsGmplsDpif": tnEventNotificationsGmplsDpif,
       "tnGmplsDBLinkCreatedNotif": tnGmplsDBLinkCreatedNotif,
       "tnGmplsDBLinkDeletedNotif": tnGmplsDBLinkDeletedNotif,
       "tnGmplsTELinkCreatedNotif": tnGmplsTELinkCreatedNotif,
       "tnGmplsTELinkDeletedNotif": tnGmplsTELinkDeletedNotif,
       "tnEventNotificationsGmplsCpif": tnEventNotificationsGmplsCpif,
       "tnGmplsCPNbrCreatedNotif": tnGmplsCPNbrCreatedNotif,
       "tnGmplsCPNbrDeletedNotif": tnGmplsCPNbrDeletedNotif,
       "tnGmplsRsvpIfCreatedNotif": tnGmplsRsvpIfCreatedNotif,
       "tnGmplsRsvpIfDeletedNotif": tnGmplsRsvpIfDeletedNotif,
       "tnGmplsDprIfCreatedNotif": tnGmplsDprIfCreatedNotif,
       "tnGmplsDprIfDeletedNotif": tnGmplsDprIfDeletedNotif,
       "tnGmplsLmpIfCreatedNotif": tnGmplsLmpIfCreatedNotif,
       "tnGmplsLmpIfDeletedNotif": tnGmplsLmpIfDeletedNotif}
)
