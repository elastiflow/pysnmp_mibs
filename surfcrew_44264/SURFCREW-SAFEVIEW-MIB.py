# SNMP MIB module (SURFCREW-SAFEVIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/surfcrew_44264/SURFCREW-SAFEVIEW-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:03:35 2025
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

surfcrew = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44264)
)
if mibBuilder.loadTexts:
    surfcrew.setRevisions(
        ("2015-12-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44264, 1)
)
_Safeview_ObjectIdentity = ObjectIdentity
safeview = _Safeview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1)
)
_SafeviewNotifications_ObjectIdentity = ObjectIdentity
safeviewNotifications = _SafeviewNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3)
)
_SafeviewCriticalNotifications_ObjectIdentity = ObjectIdentity
safeviewCriticalNotifications = _SafeviewCriticalNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 1)
)
_SafeviewGenericNotifications_ObjectIdentity = ObjectIdentity
safeviewGenericNotifications = _SafeviewGenericNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 2)
)
_SafeviewNotificationObjects_ObjectIdentity = ObjectIdentity
safeviewNotificationObjects = _SafeviewNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 6)
)
_SafeviewNotificationStatusCode_Type = Integer32
_SafeviewNotificationStatusCode_Object = MibScalar
safeviewNotificationStatusCode = _SafeviewNotificationStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 6, 1),
    _SafeviewNotificationStatusCode_Type()
)
safeviewNotificationStatusCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    safeviewNotificationStatusCode.setStatus("current")


class _SafeviewNotificationStatusDesc_Type(OctetString):
    """Custom type safeviewNotificationStatusDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SafeviewNotificationStatusDesc_Type.__name__ = "OctetString"
_SafeviewNotificationStatusDesc_Object = MibScalar
safeviewNotificationStatusDesc = _SafeviewNotificationStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 6, 2),
    _SafeviewNotificationStatusDesc_Type()
)
safeviewNotificationStatusDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    safeviewNotificationStatusDesc.setStatus("current")

# Managed Objects groups


# Notification objects

safeviewDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 1, 1)
)
safeviewDownNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    safeviewDownNotification.setStatus(
        "current"
    )

authServerUnavailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 1, 2)
)
authServerUnavailableNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    authServerUnavailableNotification.setStatus(
        "current"
    )

upstreamProxyUnavailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 1, 3)
)
upstreamProxyUnavailableNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    upstreamProxyUnavailableNotification.setStatus(
        "current"
    )

invalidLicenseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 1, 4)
)
invalidLicenseNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    invalidLicenseNotification.setStatus(
        "current"
    )

downstreamMtaUnavailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 1, 5)
)
downstreamMtaUnavailableNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    downstreamMtaUnavailableNotification.setStatus(
        "current"
    )

safeviewBootedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 2, 1)
)
safeviewBootedNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    safeviewBootedNotification.setStatus(
        "current"
    )

licenseExpiringInDaysNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 2, 2)
)
licenseExpiringInDaysNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    licenseExpiringInDaysNotification.setStatus(
        "current"
    )

authServerAvailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 2, 3)
)
authServerAvailableNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    authServerAvailableNotification.setStatus(
        "current"
    )

upstreamProxyAvailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 2, 4)
)
upstreamProxyAvailableNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
)
if mibBuilder.loadTexts:
    upstreamProxyAvailableNotification.setStatus(
        "current"
    )

downstreamMtaAvailableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44264, 1, 1, 3, 2, 5)
)
downstreamMtaAvailableNotification.setObjects(
      *(("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusCode"),
        ("SURFCREW-SAFEVIEW-MIB", "safeviewNotificationStatusDesc"))
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
    "SURFCREW-SAFEVIEW-MIB",
    **{"surfcrew": surfcrew,
       "products": products,
       "safeview": safeview,
       "safeviewNotifications": safeviewNotifications,
       "safeviewCriticalNotifications": safeviewCriticalNotifications,
       "safeviewDownNotification": safeviewDownNotification,
       "authServerUnavailableNotification": authServerUnavailableNotification,
       "upstreamProxyUnavailableNotification": upstreamProxyUnavailableNotification,
       "invalidLicenseNotification": invalidLicenseNotification,
       "downstreamMtaUnavailableNotification": downstreamMtaUnavailableNotification,
       "safeviewGenericNotifications": safeviewGenericNotifications,
       "safeviewBootedNotification": safeviewBootedNotification,
       "licenseExpiringInDaysNotification": licenseExpiringInDaysNotification,
       "authServerAvailableNotification": authServerAvailableNotification,
       "upstreamProxyAvailableNotification": upstreamProxyAvailableNotification,
       "downstreamMtaAvailableNotification": downstreamMtaAvailableNotification,
       "safeviewNotificationObjects": safeviewNotificationObjects,
       "safeviewNotificationStatusCode": safeviewNotificationStatusCode,
       "safeviewNotificationStatusDesc": safeviewNotificationStatusDesc}
)
