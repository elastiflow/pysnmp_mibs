# SNMP MIB module (VERBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/verba_39067/VERBA-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:58 2025
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

verba = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39067)
)
if mibBuilder.loadTexts:
    verba.setRevisions(
        ("2012-06-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 101, 0)
)
_PassiveRecorder_ObjectIdentity = ObjectIdentity
passiveRecorder = _PassiveRecorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 102, 0)
)
_CiscoCentralRecorder_ObjectIdentity = ObjectIdentity
ciscoCentralRecorder = _CiscoCentralRecorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 103, 0)
)
_CiscoCentralDb_ObjectIdentity = ObjectIdentity
ciscoCentralDb = _CiscoCentralDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 104, 0)
)
_DialInRec_ObjectIdentity = ObjectIdentity
dialInRec = _DialInRec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 105, 0)
)
_GeneralMediaRec_ObjectIdentity = ObjectIdentity
generalMediaRec = _GeneralMediaRec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 106, 0)
)
_AvayaActiveRec_ObjectIdentity = ObjectIdentity
avayaActiveRec = _AvayaActiveRec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 107, 0)
)
_CiscoUCGatewayRec_ObjectIdentity = ObjectIdentity
ciscoUCGatewayRec = _CiscoUCGatewayRec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 108, 0)
)
_CiscoMediaSense_ObjectIdentity = ObjectIdentity
ciscoMediaSense = _CiscoMediaSense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 109, 0)
)
_DesktopAgent_ObjectIdentity = ObjectIdentity
desktopAgent = _DesktopAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 110, 0)
)
_LyncFilter_ObjectIdentity = ObjectIdentity
lyncFilter = _LyncFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0)
)
_LyncChatRecorder_ObjectIdentity = ObjectIdentity
lyncChatRecorder = _LyncChatRecorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 112, 0)
)
_NodeManager_ObjectIdentity = ObjectIdentity
nodeManager = _NodeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 113, 0)
)
_Importer_ObjectIdentity = ObjectIdentity
importer = _Importer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 114, 0)
)
_UnifiedRecorder_ObjectIdentity = ObjectIdentity
unifiedRecorder = _UnifiedRecorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0)
)
_CiscoComplianceRecorder_ObjectIdentity = ObjectIdentity
ciscoComplianceRecorder = _CiscoComplianceRecorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 116, 0)
)
_MediaCollectorProxy_ObjectIdentity = ObjectIdentity
mediaCollectorProxy = _MediaCollectorProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0)
)
_WebApplication_ObjectIdentity = ObjectIdentity
webApplication = _WebApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 118, 0)
)
_WebApplicationApply_ObjectIdentity = ObjectIdentity
webApplicationApply = _WebApplicationApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 118, 1)
)
_WebApplicationAd_ObjectIdentity = ObjectIdentity
webApplicationAd = _WebApplicationAd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 118, 2)
)
_CentileConnector_ObjectIdentity = ObjectIdentity
centileConnector = _CentileConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 150, 0)
)
_NotificationAttribute_ObjectIdentity = ObjectIdentity
notificationAttribute = _NotificationAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 200)
)


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 1),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("current")


class _ServiceName_Type(DisplayString):
    """Custom type serviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServiceName_Type.__name__ = "DisplayString"
_ServiceName_Object = MibScalar
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 3),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _DiskSpaceLowPath_Type(DisplayString):
    """Custom type diskSpaceLowPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskSpaceLowPath_Type.__name__ = "DisplayString"
_DiskSpaceLowPath_Object = MibScalar
diskSpaceLowPath = _DiskSpaceLowPath_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 4),
    _DiskSpaceLowPath_Type()
)
diskSpaceLowPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSpaceLowPath.setStatus("current")


class _CallId_Type(DisplayString):
    """Custom type callId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CallId_Type.__name__ = "DisplayString"
_CallId_Object = MibScalar
callId = _CallId_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 5),
    _CallId_Type()
)
callId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callId.setStatus("current")


class _ServiceDisplayName_Type(DisplayString):
    """Custom type serviceDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ServiceDisplayName_Type.__name__ = "DisplayString"
_ServiceDisplayName_Object = MibScalar
serviceDisplayName = _ServiceDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 6),
    _ServiceDisplayName_Type()
)
serviceDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceDisplayName.setStatus("current")


class _Path_Type(DisplayString):
    """Custom type path based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Path_Type.__name__ = "DisplayString"
_Path_Object = MibScalar
path = _Path_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 7),
    _Path_Type()
)
path.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    path.setStatus("current")


class _AttrInterface_Type(DisplayString):
    """Custom type attrInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttrInterface_Type.__name__ = "DisplayString"
_AttrInterface_Object = MibScalar
attrInterface = _AttrInterface_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 8),
    _AttrInterface_Type()
)
attrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attrInterface.setStatus("current")


class _AttrCertThumbprint_Type(DisplayString):
    """Custom type attrCertThumbprint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttrCertThumbprint_Type.__name__ = "DisplayString"
_AttrCertThumbprint_Object = MibScalar
attrCertThumbprint = _AttrCertThumbprint_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 9),
    _AttrCertThumbprint_Type()
)
attrCertThumbprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attrCertThumbprint.setStatus("current")


class _AttrCertFriendlyName_Type(DisplayString):
    """Custom type attrCertFriendlyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttrCertFriendlyName_Type.__name__ = "DisplayString"
_AttrCertFriendlyName_Object = MibScalar
attrCertFriendlyName = _AttrCertFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 10),
    _AttrCertFriendlyName_Type()
)
attrCertFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attrCertFriendlyName.setStatus("current")


class _AttrCertExpirationDate_Type(DisplayString):
    """Custom type attrCertExpirationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttrCertExpirationDate_Type.__name__ = "DisplayString"
_AttrCertExpirationDate_Object = MibScalar
attrCertExpirationDate = _AttrCertExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 11),
    _AttrCertExpirationDate_Type()
)
attrCertExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attrCertExpirationDate.setStatus("current")


class _AttrCertSubject_Type(DisplayString):
    """Custom type attrCertSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttrCertSubject_Type.__name__ = "DisplayString"
_AttrCertSubject_Object = MibScalar
attrCertSubject = _AttrCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 39067, 200, 12),
    _AttrCertSubject_Type()
)
attrCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attrCertSubject.setStatus("current")
_General2_ObjectIdentity = ObjectIdentity
general2 = _General2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39067, 999)
)

# Managed Objects groups


# Notification objects

generalMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 1)
)
if mibBuilder.loadTexts:
    generalMemoryLow.setStatus(
        "current"
    )

generalMemoryOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 2)
)
if mibBuilder.loadTexts:
    generalMemoryOK.setStatus(
        "current"
    )

generalDiskSpaceLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 3)
)
if mibBuilder.loadTexts:
    generalDiskSpaceLow.setStatus(
        "current"
    )

generalDiskSpaceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 4)
)
if mibBuilder.loadTexts:
    generalDiskSpaceOK.setStatus(
        "current"
    )

generalServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 5)
)
if mibBuilder.loadTexts:
    generalServiceDown.setStatus(
        "current"
    )

generalServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 6)
)
if mibBuilder.loadTexts:
    generalServiceUp.setStatus(
        "current"
    )

generalRecordingInactivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 7)
)
if mibBuilder.loadTexts:
    generalRecordingInactivity.setStatus(
        "current"
    )

generalConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 8)
)
if mibBuilder.loadTexts:
    generalConnectionDown.setStatus(
        "current"
    )

generalConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 9)
)
if mibBuilder.loadTexts:
    generalConnectionUp.setStatus(
        "current"
    )

generalDatabaseDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 10)
)
if mibBuilder.loadTexts:
    generalDatabaseDown.setStatus(
        "current"
    )

generalDatabaseUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 11)
)
if mibBuilder.loadTexts:
    generalDatabaseUp.setStatus(
        "current"
    )

generalDatabaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 12)
)
if mibBuilder.loadTexts:
    generalDatabaseError.setStatus(
        "current"
    )

generalPrerequisiteMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 13)
)
if mibBuilder.loadTexts:
    generalPrerequisiteMissing.setStatus(
        "current"
    )

generalRecordingActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 14)
)
if mibBuilder.loadTexts:
    generalRecordingActivity.setStatus(
        "current"
    )

generalCertificateAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 15)
)
if mibBuilder.loadTexts:
    generalCertificateAccess.setStatus(
        "current"
    )

generalCertificateExpires = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 16)
)
if mibBuilder.loadTexts:
    generalCertificateExpires.setStatus(
        "current"
    )

generalCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 17)
)
if mibBuilder.loadTexts:
    generalCertificateExpired.setStatus(
        "current"
    )

generalCertificateNotTrusted = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 18)
)
if mibBuilder.loadTexts:
    generalCertificateNotTrusted.setStatus(
        "current"
    )

generalCertificateRevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 19)
)
if mibBuilder.loadTexts:
    generalCertificateRevoked.setStatus(
        "current"
    )

generalCertificateKeyAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 20)
)
if mibBuilder.loadTexts:
    generalCertificateKeyAccess.setStatus(
        "current"
    )

generalConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 21)
)
if mibBuilder.loadTexts:
    generalConfigError.setStatus(
        "current"
    )

generalUndefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 100, 0, 999)
)
if mibBuilder.loadTexts:
    generalUndefined.setStatus(
        "current"
    )

storagePolicyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 101, 0, 1)
)
if mibBuilder.loadTexts:
    storagePolicyError.setStatus(
        "current"
    )

storagePolicyContinues = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 101, 0, 2)
)
if mibBuilder.loadTexts:
    storagePolicyContinues.setStatus(
        "current"
    )

storagePolicyFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 101, 0, 3)
)
if mibBuilder.loadTexts:
    storagePolicyFinished.setStatus(
        "current"
    )

storageCenteraPrivilegedDeleteAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 101, 0, 4)
)
if mibBuilder.loadTexts:
    storageCenteraPrivilegedDeleteAllowed.setStatus(
        "current"
    )

passiveCaptureDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 102, 0, 1)
)
if mibBuilder.loadTexts:
    passiveCaptureDown.setStatus(
        "current"
    )

passiveCaptureUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 102, 0, 2)
)
if mibBuilder.loadTexts:
    passiveCaptureUp.setStatus(
        "current"
    )

passiveCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 102, 0, 3)
)
if mibBuilder.loadTexts:
    passiveCallProcError.setStatus(
        "current"
    )

centralJtapiServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 103, 0, 1)
)
if mibBuilder.loadTexts:
    centralJtapiServiceDown.setStatus(
        "current"
    )

centralJtapiServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 103, 0, 2)
)
if mibBuilder.loadTexts:
    centralJtapiServiceUp.setStatus(
        "current"
    )

centralCallProcErrorCC = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 103, 0, 3)
)
if mibBuilder.loadTexts:
    centralCallProcErrorCC.setStatus(
        "current"
    )

centralDbCucmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 104, 0, 1)
)
if mibBuilder.loadTexts:
    centralDbCucmDown.setStatus(
        "current"
    )

centralDbCucmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 104, 0, 2)
)
if mibBuilder.loadTexts:
    centralDbCucmUp.setStatus(
        "current"
    )

centralDbCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 104, 0, 3)
)
if mibBuilder.loadTexts:
    centralDbCallProcError.setStatus(
        "current"
    )

dialCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 105, 0, 1)
)
if mibBuilder.loadTexts:
    dialCallProcError.setStatus(
        "current"
    )

generalMediaCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 106, 0, 1)
)
if mibBuilder.loadTexts:
    generalMediaCallProcError.setStatus(
        "current"
    )

avayaAesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 107, 0, 1)
)
if mibBuilder.loadTexts:
    avayaAesDown.setStatus(
        "current"
    )

avayaAesUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 107, 0, 2)
)
if mibBuilder.loadTexts:
    avayaAesUp.setStatus(
        "current"
    )

avayaMediaRecDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 107, 0, 3)
)
if mibBuilder.loadTexts:
    avayaMediaRecDown.setStatus(
        "current"
    )

avayaMediaRecUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 107, 0, 4)
)
if mibBuilder.loadTexts:
    avayaMediaRecUp.setStatus(
        "current"
    )

avayaCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 107, 0, 5)
)
if mibBuilder.loadTexts:
    avayaCallProcError.setStatus(
        "current"
    )

ucgatewayXccServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 108, 0, 1)
)
if mibBuilder.loadTexts:
    ucgatewayXccServiceDown.setStatus(
        "current"
    )

ucgatewayXccServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 108, 0, 2)
)
if mibBuilder.loadTexts:
    ucgatewayXccServiceUp.setStatus(
        "current"
    )

ucgatewayCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 108, 0, 3)
)
if mibBuilder.loadTexts:
    ucgatewayCallProcError.setStatus(
        "current"
    )

mediasenseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 109, 0, 1)
)
if mibBuilder.loadTexts:
    mediasenseConnectionDown.setStatus(
        "current"
    )

mediasenseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 109, 0, 2)
)
if mibBuilder.loadTexts:
    mediasenseConnectionUp.setStatus(
        "current"
    )

mediasenseCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 109, 0, 3)
)
if mibBuilder.loadTexts:
    mediasenseCallProcError.setStatus(
        "current"
    )

agentConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 110, 0, 1)
)
if mibBuilder.loadTexts:
    agentConnectionDown.setStatus(
        "current"
    )

agentConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 110, 0, 2)
)
if mibBuilder.loadTexts:
    agentConnectionUp.setStatus(
        "current"
    )

agentCapturingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 110, 0, 3)
)
if mibBuilder.loadTexts:
    agentCapturingError.setStatus(
        "current"
    )

filterRecorderTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 1)
)
if mibBuilder.loadTexts:
    filterRecorderTimeout.setStatus(
        "current"
    )

filterRecorderBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 2)
)
if mibBuilder.loadTexts:
    filterRecorderBack.setStatus(
        "current"
    )

filterLyncDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 3)
)
if mibBuilder.loadTexts:
    filterLyncDown.setStatus(
        "current"
    )

filterLyncUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 4)
)
if mibBuilder.loadTexts:
    filterLyncUp.setStatus(
        "current"
    )

filterMediaCollectorTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 5)
)
if mibBuilder.loadTexts:
    filterMediaCollectorTimeout.setStatus(
        "current"
    )

filterMediaCollectorBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 6)
)
if mibBuilder.loadTexts:
    filterMediaCollectorBack.setStatus(
        "current"
    )

filterAnnouncementTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 7)
)
if mibBuilder.loadTexts:
    filterAnnouncementTimeout.setStatus(
        "current"
    )

filterAnnouncementBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 8)
)
if mibBuilder.loadTexts:
    filterAnnouncementBack.setStatus(
        "current"
    )

filterLyncInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 9)
)
if mibBuilder.loadTexts:
    filterLyncInactive.setStatus(
        "current"
    )

filterCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 10)
)
if mibBuilder.loadTexts:
    filterCallProcError.setStatus(
        "current"
    )

filterConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 111, 0, 11)
)
if mibBuilder.loadTexts:
    filterConfigurationError.setStatus(
        "current"
    )

lyncIMDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 112, 0, 1)
)
if mibBuilder.loadTexts:
    lyncIMDown.setStatus(
        "current"
    )

lyncIMUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 112, 0, 2)
)
if mibBuilder.loadTexts:
    lyncIMUp.setStatus(
        "current"
    )

registrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 113, 0, 1)
)
if mibBuilder.loadTexts:
    registrationFailed.setStatus(
        "current"
    )

registrationReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 113, 0, 2)
)
if mibBuilder.loadTexts:
    registrationReady.setStatus(
        "current"
    )

importerImportFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 114, 0, 1)
)
if mibBuilder.loadTexts:
    importerImportFailure.setStatus(
        "current"
    )

importerRecordFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 114, 0, 2)
)
if mibBuilder.loadTexts:
    importerRecordFailure.setStatus(
        "current"
    )

importerRecheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 114, 0, 3)
)
if mibBuilder.loadTexts:
    importerRecheckFailure.setStatus(
        "current"
    )

importerMediaLengthMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 114, 0, 4)
)
if mibBuilder.loadTexts:
    importerMediaLengthMismatch.setStatus(
        "current"
    )

unifiedRecProviderDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 1)
)
if mibBuilder.loadTexts:
    unifiedRecProviderDown.setStatus(
        "current"
    )

unifiedRecProviderUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 2)
)
if mibBuilder.loadTexts:
    unifiedRecProviderUp.setStatus(
        "current"
    )

unifiedMediaRecDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 3)
)
if mibBuilder.loadTexts:
    unifiedMediaRecDown.setStatus(
        "current"
    )

unifiedMediaRecUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 4)
)
if mibBuilder.loadTexts:
    unifiedMediaRecUp.setStatus(
        "current"
    )

unifiedJtapiServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 5)
)
if mibBuilder.loadTexts:
    unifiedJtapiServiceDown.setStatus(
        "current"
    )

unifiedJtapiServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 6)
)
if mibBuilder.loadTexts:
    unifiedJtapiServiceUp.setStatus(
        "current"
    )

unifiedCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 7)
)
if mibBuilder.loadTexts:
    unifiedCallProcError.setStatus(
        "current"
    )

unifiedSipTrunkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 8)
)
if mibBuilder.loadTexts:
    unifiedSipTrunkDown.setStatus(
        "current"
    )

unifiedSipTrunkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 9)
)
if mibBuilder.loadTexts:
    unifiedSipTrunkUp.setStatus(
        "current"
    )

unifiedRecorderOverloadBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 10)
)
if mibBuilder.loadTexts:
    unifiedRecorderOverloadBegin.setStatus(
        "current"
    )

unifiedRecorderOverloadEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 11)
)
if mibBuilder.loadTexts:
    unifiedRecorderOverloadEnd.setStatus(
        "current"
    )

unifiedRecorderStandbyBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 12)
)
if mibBuilder.loadTexts:
    unifiedRecorderStandbyBegin.setStatus(
        "current"
    )

unifiedRecorderStandbyEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 13)
)
if mibBuilder.loadTexts:
    unifiedRecorderStandbyEnd.setStatus(
        "current"
    )

unifiedRecDirectorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 14)
)
if mibBuilder.loadTexts:
    unifiedRecDirectorDown.setStatus(
        "current"
    )

unifiedRecDirectorUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 115, 0, 15)
)
if mibBuilder.loadTexts:
    unifiedRecDirectorUp.setStatus(
        "current"
    )

impNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 116, 0, 1)
)
if mibBuilder.loadTexts:
    impNodeUp.setStatus(
        "current"
    )

impNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 116, 0, 2)
)
if mibBuilder.loadTexts:
    impNodeDown.setStatus(
        "current"
    )

jabberLoginTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 116, 0, 3)
)
if mibBuilder.loadTexts:
    jabberLoginTimeout.setStatus(
        "current"
    )

jabberMessageTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 116, 0, 4)
)
if mibBuilder.loadTexts:
    jabberMessageTimeout.setStatus(
        "current"
    )

messageQueueThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 116, 0, 5)
)
if mibBuilder.loadTexts:
    messageQueueThreshold.setStatus(
        "current"
    )

mcpxRecorderUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 1)
)
if mibBuilder.loadTexts:
    mcpxRecorderUp.setStatus(
        "current"
    )

mcpxRecorderDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 2)
)
if mibBuilder.loadTexts:
    mcpxRecorderDown.setStatus(
        "current"
    )

mcpxLyncFilterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 3)
)
if mibBuilder.loadTexts:
    mcpxLyncFilterUp.setStatus(
        "current"
    )

mcpxLyncFilterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 4)
)
if mibBuilder.loadTexts:
    mcpxLyncFilterDown.setStatus(
        "current"
    )

mcpxRecorderOverloadBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 5)
)
if mibBuilder.loadTexts:
    mcpxRecorderOverloadBegin.setStatus(
        "current"
    )

mcpxRecorderOverloadEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 6)
)
if mibBuilder.loadTexts:
    mcpxRecorderOverloadEnd.setStatus(
        "current"
    )

mcpxRecorderStandbyBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 7)
)
if mibBuilder.loadTexts:
    mcpxRecorderStandbyBegin.setStatus(
        "current"
    )

mcpxRecorderStandbyEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 8)
)
if mibBuilder.loadTexts:
    mcpxRecorderStandbyEnd.setStatus(
        "current"
    )

mcpxCallProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 117, 0, 9)
)
if mibBuilder.loadTexts:
    mcpxCallProcError.setStatus(
        "current"
    )

failedLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 118, 0, 1)
)
if mibBuilder.loadTexts:
    failedLogin.setStatus(
        "current"
    )

applyACLFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 118, 1, 1)
)
if mibBuilder.loadTexts:
    applyACLFailed.setStatus(
        "current"
    )

applyCommPoliciesFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 118, 1, 2)
)
if mibBuilder.loadTexts:
    applyCommPoliciesFailed.setStatus(
        "current"
    )

adSyncError = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 118, 2, 1)
)
if mibBuilder.loadTexts:
    adSyncError.setStatus(
        "current"
    )

diskAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 150, 0, 1)
)
if mibBuilder.loadTexts:
    diskAccess.setStatus(
        "current"
    )

databaseAccessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 150, 0, 2)
)
if mibBuilder.loadTexts:
    databaseAccessDown.setStatus(
        "current"
    )

databaseAccessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 150, 0, 3)
)
if mibBuilder.loadTexts:
    databaseAccessUp.setStatus(
        "current"
    )

unidentifiedEnterprise = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 150, 0, 4)
)
if mibBuilder.loadTexts:
    unidentifiedEnterprise.setStatus(
        "current"
    )

callProcErrorCentile = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 150, 0, 5)
)
if mibBuilder.loadTexts:
    callProcErrorCentile.setStatus(
        "current"
    )

folderAccessProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 999, 10)
)
if mibBuilder.loadTexts:
    folderAccessProblem.setStatus(
        "current"
    )

folderAccessOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 39067, 999, 11)
)
if mibBuilder.loadTexts:
    folderAccessOK.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERBA-MIB",
    **{"verba": verba,
       "general": general,
       "generalMemoryLow": generalMemoryLow,
       "generalMemoryOK": generalMemoryOK,
       "generalDiskSpaceLow": generalDiskSpaceLow,
       "generalDiskSpaceOK": generalDiskSpaceOK,
       "generalServiceDown": generalServiceDown,
       "generalServiceUp": generalServiceUp,
       "generalRecordingInactivity": generalRecordingInactivity,
       "generalConnectionDown": generalConnectionDown,
       "generalConnectionUp": generalConnectionUp,
       "generalDatabaseDown": generalDatabaseDown,
       "generalDatabaseUp": generalDatabaseUp,
       "generalDatabaseError": generalDatabaseError,
       "generalPrerequisiteMissing": generalPrerequisiteMissing,
       "generalRecordingActivity": generalRecordingActivity,
       "generalCertificateAccess": generalCertificateAccess,
       "generalCertificateExpires": generalCertificateExpires,
       "generalCertificateExpired": generalCertificateExpired,
       "generalCertificateNotTrusted": generalCertificateNotTrusted,
       "generalCertificateRevoked": generalCertificateRevoked,
       "generalCertificateKeyAccess": generalCertificateKeyAccess,
       "generalConfigError": generalConfigError,
       "generalUndefined": generalUndefined,
       "storage": storage,
       "storagePolicyError": storagePolicyError,
       "storagePolicyContinues": storagePolicyContinues,
       "storagePolicyFinished": storagePolicyFinished,
       "storageCenteraPrivilegedDeleteAllowed": storageCenteraPrivilegedDeleteAllowed,
       "passiveRecorder": passiveRecorder,
       "passiveCaptureDown": passiveCaptureDown,
       "passiveCaptureUp": passiveCaptureUp,
       "passiveCallProcError": passiveCallProcError,
       "ciscoCentralRecorder": ciscoCentralRecorder,
       "centralJtapiServiceDown": centralJtapiServiceDown,
       "centralJtapiServiceUp": centralJtapiServiceUp,
       "centralCallProcErrorCC": centralCallProcErrorCC,
       "ciscoCentralDb": ciscoCentralDb,
       "centralDbCucmDown": centralDbCucmDown,
       "centralDbCucmUp": centralDbCucmUp,
       "centralDbCallProcError": centralDbCallProcError,
       "dialInRec": dialInRec,
       "dialCallProcError": dialCallProcError,
       "generalMediaRec": generalMediaRec,
       "generalMediaCallProcError": generalMediaCallProcError,
       "avayaActiveRec": avayaActiveRec,
       "avayaAesDown": avayaAesDown,
       "avayaAesUp": avayaAesUp,
       "avayaMediaRecDown": avayaMediaRecDown,
       "avayaMediaRecUp": avayaMediaRecUp,
       "avayaCallProcError": avayaCallProcError,
       "ciscoUCGatewayRec": ciscoUCGatewayRec,
       "ucgatewayXccServiceDown": ucgatewayXccServiceDown,
       "ucgatewayXccServiceUp": ucgatewayXccServiceUp,
       "ucgatewayCallProcError": ucgatewayCallProcError,
       "ciscoMediaSense": ciscoMediaSense,
       "mediasenseConnectionDown": mediasenseConnectionDown,
       "mediasenseConnectionUp": mediasenseConnectionUp,
       "mediasenseCallProcError": mediasenseCallProcError,
       "desktopAgent": desktopAgent,
       "agentConnectionDown": agentConnectionDown,
       "agentConnectionUp": agentConnectionUp,
       "agentCapturingError": agentCapturingError,
       "lyncFilter": lyncFilter,
       "filterRecorderTimeout": filterRecorderTimeout,
       "filterRecorderBack": filterRecorderBack,
       "filterLyncDown": filterLyncDown,
       "filterLyncUp": filterLyncUp,
       "filterMediaCollectorTimeout": filterMediaCollectorTimeout,
       "filterMediaCollectorBack": filterMediaCollectorBack,
       "filterAnnouncementTimeout": filterAnnouncementTimeout,
       "filterAnnouncementBack": filterAnnouncementBack,
       "filterLyncInactive": filterLyncInactive,
       "filterCallProcError": filterCallProcError,
       "filterConfigurationError": filterConfigurationError,
       "lyncChatRecorder": lyncChatRecorder,
       "lyncIMDown": lyncIMDown,
       "lyncIMUp": lyncIMUp,
       "nodeManager": nodeManager,
       "registrationFailed": registrationFailed,
       "registrationReady": registrationReady,
       "importer": importer,
       "importerImportFailure": importerImportFailure,
       "importerRecordFailure": importerRecordFailure,
       "importerRecheckFailure": importerRecheckFailure,
       "importerMediaLengthMismatch": importerMediaLengthMismatch,
       "unifiedRecorder": unifiedRecorder,
       "unifiedRecProviderDown": unifiedRecProviderDown,
       "unifiedRecProviderUp": unifiedRecProviderUp,
       "unifiedMediaRecDown": unifiedMediaRecDown,
       "unifiedMediaRecUp": unifiedMediaRecUp,
       "unifiedJtapiServiceDown": unifiedJtapiServiceDown,
       "unifiedJtapiServiceUp": unifiedJtapiServiceUp,
       "unifiedCallProcError": unifiedCallProcError,
       "unifiedSipTrunkDown": unifiedSipTrunkDown,
       "unifiedSipTrunkUp": unifiedSipTrunkUp,
       "unifiedRecorderOverloadBegin": unifiedRecorderOverloadBegin,
       "unifiedRecorderOverloadEnd": unifiedRecorderOverloadEnd,
       "unifiedRecorderStandbyBegin": unifiedRecorderStandbyBegin,
       "unifiedRecorderStandbyEnd": unifiedRecorderStandbyEnd,
       "unifiedRecDirectorDown": unifiedRecDirectorDown,
       "unifiedRecDirectorUp": unifiedRecDirectorUp,
       "ciscoComplianceRecorder": ciscoComplianceRecorder,
       "impNodeUp": impNodeUp,
       "impNodeDown": impNodeDown,
       "jabberLoginTimeout": jabberLoginTimeout,
       "jabberMessageTimeout": jabberMessageTimeout,
       "messageQueueThreshold": messageQueueThreshold,
       "mediaCollectorProxy": mediaCollectorProxy,
       "mcpxRecorderUp": mcpxRecorderUp,
       "mcpxRecorderDown": mcpxRecorderDown,
       "mcpxLyncFilterUp": mcpxLyncFilterUp,
       "mcpxLyncFilterDown": mcpxLyncFilterDown,
       "mcpxRecorderOverloadBegin": mcpxRecorderOverloadBegin,
       "mcpxRecorderOverloadEnd": mcpxRecorderOverloadEnd,
       "mcpxRecorderStandbyBegin": mcpxRecorderStandbyBegin,
       "mcpxRecorderStandbyEnd": mcpxRecorderStandbyEnd,
       "mcpxCallProcError": mcpxCallProcError,
       "webApplication": webApplication,
       "failedLogin": failedLogin,
       "webApplicationApply": webApplicationApply,
       "applyACLFailed": applyACLFailed,
       "applyCommPoliciesFailed": applyCommPoliciesFailed,
       "webApplicationAd": webApplicationAd,
       "adSyncError": adSyncError,
       "centileConnector": centileConnector,
       "diskAccess": diskAccess,
       "databaseAccessDown": databaseAccessDown,
       "databaseAccessUp": databaseAccessUp,
       "unidentifiedEnterprise": unidentifiedEnterprise,
       "callProcErrorCentile": callProcErrorCentile,
       "notificationAttribute": notificationAttribute,
       "description": description,
       "serviceName": serviceName,
       "hostName": hostName,
       "diskSpaceLowPath": diskSpaceLowPath,
       "callId": callId,
       "serviceDisplayName": serviceDisplayName,
       "path": path,
       "attrInterface": attrInterface,
       "attrCertThumbprint": attrCertThumbprint,
       "attrCertFriendlyName": attrCertFriendlyName,
       "attrCertExpirationDate": attrCertExpirationDate,
       "attrCertSubject": attrCertSubject,
       "general2": general2,
       "folderAccessProblem": folderAccessProblem,
       "folderAccessOK": folderAccessOK}
)
