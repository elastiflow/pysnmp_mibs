# SNMP MIB module (MENLO-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/menlo_44734/MENLO-SECURITY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:24:01 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

menloSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44734)
)
if mibBuilder.loadTexts:
    menloSecurity.setRevisions(
        ("2015-12-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44734, 1)
)
_Msip_ObjectIdentity = ObjectIdentity
msip = _Msip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1)
)
_MsipNotifications_ObjectIdentity = ObjectIdentity
msipNotifications = _MsipNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3)
)
_MsipCriticalNotifications_ObjectIdentity = ObjectIdentity
msipCriticalNotifications = _MsipCriticalNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1)
)
_MsipGenericNotifications_ObjectIdentity = ObjectIdentity
msipGenericNotifications = _MsipGenericNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 2)
)
_MsipNotificationObjects_ObjectIdentity = ObjectIdentity
msipNotificationObjects = _MsipNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 6)
)
_MsipNotificationStatusCode_Type = Integer32
_MsipNotificationStatusCode_Object = MibScalar
msipNotificationStatusCode = _MsipNotificationStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 6, 1),
    _MsipNotificationStatusCode_Type()
)
msipNotificationStatusCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    msipNotificationStatusCode.setStatus("current")


class _MsipNotificationStatusDesc_Type(OctetString):
    """Custom type msipNotificationStatusDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MsipNotificationStatusDesc_Type.__name__ = "OctetString"
_MsipNotificationStatusDesc_Object = MibScalar
msipNotificationStatusDesc = _MsipNotificationStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 6, 2),
    _MsipNotificationStatusDesc_Type()
)
msipNotificationStatusDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    msipNotificationStatusDesc.setStatus("current")

# Managed Objects groups


# Notification objects

msipDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1, 1)
)
msipDownNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    msipDownNotification.setStatus(
        "current"
    )

authServerUnavailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1, 2)
)
authServerUnavailableNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    authServerUnavailableNotification.setStatus(
        "current"
    )

upstreamProxyUnavailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1, 3)
)
upstreamProxyUnavailableNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    upstreamProxyUnavailableNotification.setStatus(
        "current"
    )

invalidLicenseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1, 4)
)
invalidLicenseNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    invalidLicenseNotification.setStatus(
        "current"
    )

downstreamMtaUnavailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1, 5)
)
downstreamMtaUnavailableNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    downstreamMtaUnavailableNotification.setStatus(
        "current"
    )

resourceLimitExceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 1, 6)
)
resourceLimitExceededNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    resourceLimitExceededNotification.setStatus(
        "current"
    )

msipBootedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 2, 1)
)
msipBootedNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    msipBootedNotification.setStatus(
        "current"
    )

licenseExpiringInDaysNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 2, 2)
)
licenseExpiringInDaysNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    licenseExpiringInDaysNotification.setStatus(
        "current"
    )

authServerAvailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 2, 3)
)
authServerAvailableNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    authServerAvailableNotification.setStatus(
        "current"
    )

upstreamProxyAvailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 2, 4)
)
upstreamProxyAvailableNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    upstreamProxyAvailableNotification.setStatus(
        "current"
    )

downstreamMtaAvailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44734, 1, 1, 3, 2, 5)
)
downstreamMtaAvailableNotification.setObjects(
      *(("MENLO-SECURITY-MIB", "msipNotificationStatusCode"),
        ("MENLO-SECURITY-MIB", "msipNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    downstreamMtaAvailableNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MENLO-SECURITY-MIB",
    **{"menloSecurity": menloSecurity,
       "products": products,
       "msip": msip,
       "msipNotifications": msipNotifications,
       "msipCriticalNotifications": msipCriticalNotifications,
       "msipDownNotification": msipDownNotification,
       "authServerUnavailableNotification": authServerUnavailableNotification,
       "upstreamProxyUnavailableNotification": upstreamProxyUnavailableNotification,
       "invalidLicenseNotification": invalidLicenseNotification,
       "downstreamMtaUnavailableNotification": downstreamMtaUnavailableNotification,
       "resourceLimitExceededNotification": resourceLimitExceededNotification,
       "msipGenericNotifications": msipGenericNotifications,
       "msipBootedNotification": msipBootedNotification,
       "licenseExpiringInDaysNotification": licenseExpiringInDaysNotification,
       "authServerAvailableNotification": authServerAvailableNotification,
       "upstreamProxyAvailableNotification": upstreamProxyAvailableNotification,
       "downstreamMtaAvailableNotification": downstreamMtaAvailableNotification,
       "msipNotificationObjects": msipNotificationObjects,
       "msipNotificationStatusCode": msipNotificationStatusCode,
       "msipNotificationStatusDesc": msipNotificationStatusDesc}
)
