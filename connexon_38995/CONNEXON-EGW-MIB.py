# SNMP MIB module (CONNEXON-EGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/connexon_38995/CONNEXON-EGW-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:57:15 2025
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

emergencyGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1)
)
if mibBuilder.loadTexts:
    emergencyGatewayMIB.setRevisions(
        ("2011-12-20 00:00",
         "2011-12-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Connexon_ObjectIdentity = ObjectIdentity
connexon = _Connexon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38995)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38995, 1)
)
_EmergencyGateway_ObjectIdentity = ObjectIdentity
emergencyGateway = _EmergencyGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1)
)
_ConnexonEgwMIBNotifications_ObjectIdentity = ObjectIdentity
connexonEgwMIBNotifications = _ConnexonEgwMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0)
)
_ConnexonEgwMIBNotifObjects_ObjectIdentity = ObjectIdentity
connexonEgwMIBNotifObjects = _ConnexonEgwMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0)
)


class _ConnexonEgwAlarmType_Type(Integer32):
    """Custom type connexonEgwAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("serverNoStatusFound", 1),
          ("cpmCiscoCtiCheckFailed", 2),
          ("mailServerDown", 3),
          ("ctiBusyForTooLong", 4),
          ("logPrematureDisconnect", 5),
          ("primaryServerDown", 6),
          ("cpmCiscoCtiEmpty", 7),
          ("ccmCtiLoginFailed", 8),
          ("ccmCtiServerDown", 9),
          ("ccmCtiServerUp", 10),
          ("ccmAxlQueryFailed", 11),
          ("mysqlDBConnectFailed", 12),
          ("callTo911PrimaryFailed", 13),
          ("callTo911TertiaryFailed", 14),
          ("callTo911SecondaryFailed", 15),
          ("cpmPbxNotFound", 16),
          ("soapCallFailed", 17),
          ("callToECRCPbxWarningFailed", 18),
          ("snmpScanInvalidIP", 19),
          ("rlmNotifierCtiLoginFailed", 20),
          ("rlmNotifierPushFailed", 21),
          ("ocsRlmPushFailed", 22),
          ("maximumEndpointsExceeded", 23),
          ("ctiRtpEventTimeout", 26),
          ("ctiWatchdog", 27),
          ("ccmSnmpIPUnreachable", 28),
          ("extensionMissing", 29),
          ("wlanSnmpScanUnreachable", 30),
          ("licensingGracePeriodOver", 31),
          ("licensingActivationSuccess", 32),
          ("licensingEnteringGracePeriod", 33),
          ("licensingGracePeriodReminder", 34),
          ("callCDRMainFailed", 35),
          ("callCDRLeg2Failed", 36),
          ("callToSecurityDeskWarningFailed", 37),
          ("callToSecurityDeskCriticalFailed", 38),
          ("callToECRCPbxCriticalFailed", 39),
          ("callToLocalTrunkingWarningFailed", 40),
          ("callToLocalTrunkingCritFailed", 41),
          ("callToECRCErsCriticalFailed", 42),
          ("callToECRCErsWarningFailed", 43),
          ("callToCallbackWarningFailed", 44),
          ("callToCallbackCriticalFailed", 45),
          ("callToFallbackCriticalFailed", 46),
          ("callTo911PrimaryWarning", 47),
          ("cpmInstructionsCallFailure", 48),
          ("snmpScanTooLong", 49),
          ("resolvingDomains", 50),
          ("cdrExportAutomatedTask", 51),
          ("alcatelLucentImport", 52),
          ("userLoginFailure", 53),
          ("ldapServerFailure", 54),
          ("ldapDirectoryFailure", 55),
          ("broadworksUnreachableWS", 56),
          ("carrierTenantMissing", 57),
          ("broadworksMissingWS", 58),
          ("carrierTenantDisabled", 59),
          ("egwHostEvent", 60),
          ("egwServiceEvent", 61),
          ("snmpTrapFailure", 62),
          ("testTrap", 63),
          ("unreachablePBX", 64),
          ("unreachableERS", 65),
          ("allRoutesAreDown", 66),
          ("layer2DiscoveryPeerCheckFailed", 67),
          ("layer2DiscoveryCouldNotScanSwitch", 68),
          ("layer2DiscoveryDuplicateMACFound", 69),
          ("layer2DiscoveryInvalidScan", 70),
          ("layer2DiscoveryMACLocationHasChanged", 71),
          ("layer2DiscoveryMACLocationHasChangedToECRC", 72),
          ("locationServerMisconfiguration", 73),
          ("locationServerCallerIPUnavailable", 74),
          ("locationServerTimedOut", 75))
    )


_ConnexonEgwAlarmType_Type.__name__ = "Integer32"
_ConnexonEgwAlarmType_Object = MibScalar
connexonEgwAlarmType = _ConnexonEgwAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 1),
    _ConnexonEgwAlarmType_Type()
)
connexonEgwAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlarmType.setStatus("current")


class _ConnexonEgwAlarmLevel_Type(Integer32):
    """Custom type connexonEgwAlarmLevel based on Integer32"""
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
        *(("critical", 1),
          ("warning", 2),
          ("info", 3),
          ("rac", 4))
    )


_ConnexonEgwAlarmLevel_Type.__name__ = "Integer32"
_ConnexonEgwAlarmLevel_Object = MibScalar
connexonEgwAlarmLevel = _ConnexonEgwAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 2),
    _ConnexonEgwAlarmLevel_Type()
)
connexonEgwAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlarmLevel.setStatus("current")


class _ConnexonEgwAlarmText_Type(OctetString):
    """Custom type connexonEgwAlarmText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ConnexonEgwAlarmText_Type.__name__ = "OctetString"
_ConnexonEgwAlarmText_Object = MibScalar
connexonEgwAlarmText = _ConnexonEgwAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 3),
    _ConnexonEgwAlarmText_Type()
)
connexonEgwAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlarmText.setStatus("current")


class _ConnexonEgwAlertCallback_Type(OctetString):
    """Custom type connexonEgwAlertCallback based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConnexonEgwAlertCallback_Type.__name__ = "OctetString"
_ConnexonEgwAlertCallback_Object = MibScalar
connexonEgwAlertCallback = _ConnexonEgwAlertCallback_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 4),
    _ConnexonEgwAlertCallback_Type()
)
connexonEgwAlertCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertCallback.setStatus("current")


class _ConnexonEgwAlertEndpoint_Type(OctetString):
    """Custom type connexonEgwAlertEndpoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConnexonEgwAlertEndpoint_Type.__name__ = "OctetString"
_ConnexonEgwAlertEndpoint_Object = MibScalar
connexonEgwAlertEndpoint = _ConnexonEgwAlertEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 5),
    _ConnexonEgwAlertEndpoint_Type()
)
connexonEgwAlertEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertEndpoint.setStatus("current")


class _ConnexonEgwAlertCallingPartyName_Type(OctetString):
    """Custom type connexonEgwAlertCallingPartyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConnexonEgwAlertCallingPartyName_Type.__name__ = "OctetString"
_ConnexonEgwAlertCallingPartyName_Object = MibScalar
connexonEgwAlertCallingPartyName = _ConnexonEgwAlertCallingPartyName_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 6),
    _ConnexonEgwAlertCallingPartyName_Type()
)
connexonEgwAlertCallingPartyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertCallingPartyName.setStatus("current")


class _ConnexonEgwAlertIpPbxName_Type(OctetString):
    """Custom type connexonEgwAlertIpPbxName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_ConnexonEgwAlertIpPbxName_Type.__name__ = "OctetString"
_ConnexonEgwAlertIpPbxName_Object = MibScalar
connexonEgwAlertIpPbxName = _ConnexonEgwAlertIpPbxName_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 7),
    _ConnexonEgwAlertIpPbxName_Type()
)
connexonEgwAlertIpPbxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertIpPbxName.setStatus("current")


class _ConnexonEgwAlertTimestamp_Type(OctetString):
    """Custom type connexonEgwAlertTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_ConnexonEgwAlertTimestamp_Type.__name__ = "OctetString"
_ConnexonEgwAlertTimestamp_Object = MibScalar
connexonEgwAlertTimestamp = _ConnexonEgwAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 8),
    _ConnexonEgwAlertTimestamp_Type()
)
connexonEgwAlertTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertTimestamp.setStatus("current")


class _ConnexonEgwAlertUrlData_Type(OctetString):
    """Custom type connexonEgwAlertUrlData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ConnexonEgwAlertUrlData_Type.__name__ = "OctetString"
_ConnexonEgwAlertUrlData_Object = MibScalar
connexonEgwAlertUrlData = _ConnexonEgwAlertUrlData_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 9),
    _ConnexonEgwAlertUrlData_Type()
)
connexonEgwAlertUrlData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertUrlData.setStatus("current")


class _ConnexonEgwAlertLocation_Type(OctetString):
    """Custom type connexonEgwAlertLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ConnexonEgwAlertLocation_Type.__name__ = "OctetString"
_ConnexonEgwAlertLocation_Object = MibScalar
connexonEgwAlertLocation = _ConnexonEgwAlertLocation_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 10),
    _ConnexonEgwAlertLocation_Type()
)
connexonEgwAlertLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwAlertLocation.setStatus("current")


class _ConnexonEgwServerType_Type(Integer32):
    """Custom type connexonEgwServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("standalone", 3))
    )


_ConnexonEgwServerType_Type.__name__ = "Integer32"
_ConnexonEgwServerType_Object = MibScalar
connexonEgwServerType = _ConnexonEgwServerType_Object(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 0, 11),
    _ConnexonEgwServerType_Type()
)
connexonEgwServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connexonEgwServerType.setStatus("current")
_ConnexonEgwMIBGroups_ObjectIdentity = ObjectIdentity
connexonEgwMIBGroups = _ConnexonEgwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 1)
)

# Managed Objects groups

connexonEgwMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 1, 1)
)
connexonEgwMIBObjectGroup.setObjects(
      *(("CONNEXON-EGW-MIB", "connexonEgwAlarmType"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlarmLevel"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlarmText"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertCallback"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertEndpoint"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertCallingPartyName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertIpPbxName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertTimestamp"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertUrlData"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertLocation"),
        ("CONNEXON-EGW-MIB", "connexonEgwServerType"))
)
if mibBuilder.loadTexts:
    connexonEgwMIBObjectGroup.setStatus("current")


# Notification objects

connexonEgwApplicationAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 1)
)
connexonEgwApplicationAlarmNotif.setObjects(
      *(("CONNEXON-EGW-MIB", "connexonEgwAlarmType"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlarmLevel"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlarmText"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertTimestamp"),
        ("CONNEXON-EGW-MIB", "connexonEgwServerType"))
)
if mibBuilder.loadTexts:
    connexonEgwApplicationAlarmNotif.setStatus(
        "current"
    )

connexonEgwCrisisAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 2)
)
connexonEgwCrisisAlert.setObjects(
      *(("CONNEXON-EGW-MIB", "connexonEgwAlertCallback"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertEndpoint"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertCallingPartyName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertIpPbxName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertTimestamp"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertUrlData"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertLocation"),
        ("CONNEXON-EGW-MIB", "connexonEgwServerType"))
)
if mibBuilder.loadTexts:
    connexonEgwCrisisAlert.setStatus(
        "current"
    )

connexonEgwUnprovisionedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 3)
)
connexonEgwUnprovisionedAlert.setObjects(
      *(("CONNEXON-EGW-MIB", "connexonEgwAlertCallback"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertEndpoint"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertCallingPartyName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertIpPbxName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertTimestamp"),
        ("CONNEXON-EGW-MIB", "connexonEgwServerType"))
)
if mibBuilder.loadTexts:
    connexonEgwUnprovisionedAlert.setStatus(
        "current"
    )

connexonEgwOffCampusAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 0, 4)
)
connexonEgwOffCampusAlert.setObjects(
      *(("CONNEXON-EGW-MIB", "connexonEgwAlertCallback"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertEndpoint"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertCallingPartyName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertIpPbxName"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertTimestamp"),
        ("CONNEXON-EGW-MIB", "connexonEgwAlertLocation"),
        ("CONNEXON-EGW-MIB", "connexonEgwServerType"))
)
if mibBuilder.loadTexts:
    connexonEgwOffCampusAlert.setStatus(
        "current"
    )


# Notifications groups

connexonEgwAlarms = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 1, 2)
)
connexonEgwAlarms.setObjects(
    ("CONNEXON-EGW-MIB", "connexonEgwApplicationAlarmNotif")
)
if mibBuilder.loadTexts:
    connexonEgwAlarms.setStatus(
        "current"
    )

connexonEgwAlerts = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38995, 1, 1, 1, 1, 3)
)
connexonEgwAlerts.setObjects(
      *(("CONNEXON-EGW-MIB", "connexonEgwCrisisAlert"),
        ("CONNEXON-EGW-MIB", "connexonEgwUnprovisionedAlert"),
        ("CONNEXON-EGW-MIB", "connexonEgwOffCampusAlert"))
)
if mibBuilder.loadTexts:
    connexonEgwAlerts.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONNEXON-EGW-MIB",
    **{"connexon": connexon,
       "products": products,
       "emergencyGateway": emergencyGateway,
       "emergencyGatewayMIB": emergencyGatewayMIB,
       "connexonEgwMIBNotifications": connexonEgwMIBNotifications,
       "connexonEgwMIBNotifObjects": connexonEgwMIBNotifObjects,
       "connexonEgwAlarmType": connexonEgwAlarmType,
       "connexonEgwAlarmLevel": connexonEgwAlarmLevel,
       "connexonEgwAlarmText": connexonEgwAlarmText,
       "connexonEgwAlertCallback": connexonEgwAlertCallback,
       "connexonEgwAlertEndpoint": connexonEgwAlertEndpoint,
       "connexonEgwAlertCallingPartyName": connexonEgwAlertCallingPartyName,
       "connexonEgwAlertIpPbxName": connexonEgwAlertIpPbxName,
       "connexonEgwAlertTimestamp": connexonEgwAlertTimestamp,
       "connexonEgwAlertUrlData": connexonEgwAlertUrlData,
       "connexonEgwAlertLocation": connexonEgwAlertLocation,
       "connexonEgwServerType": connexonEgwServerType,
       "connexonEgwApplicationAlarmNotif": connexonEgwApplicationAlarmNotif,
       "connexonEgwCrisisAlert": connexonEgwCrisisAlert,
       "connexonEgwUnprovisionedAlert": connexonEgwUnprovisionedAlert,
       "connexonEgwOffCampusAlert": connexonEgwOffCampusAlert,
       "connexonEgwMIBGroups": connexonEgwMIBGroups,
       "connexonEgwMIBObjectGroup": connexonEgwMIBObjectGroup,
       "connexonEgwAlarms": connexonEgwAlarms,
       "connexonEgwAlerts": connexonEgwAlerts}
)
