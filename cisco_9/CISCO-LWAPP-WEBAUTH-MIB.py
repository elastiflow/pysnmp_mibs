# SNMP MIB module (CISCO-LWAPP-WEBAUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-WEBAUTH-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:06 2025
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

(cLApName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName")

(CLWebAuthType,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLWebAuthType")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappWebAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515)
)
if mibBuilder.loadTexts:
    ciscoLwappWebAuthMIB.setRevisions(
        ("2017-05-10 00:00",
         "2007-03-04 00:00",
         "2006-04-05 11:50")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWebAuthMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBNotifs = _CiscoLwappWebAuthMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0)
)
_CiscoLwappWebAuthMIBNotifObjs_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBNotifObjs = _CiscoLwappWebAuthMIBNotifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 1)
)


class _CLWAGuestUserName_Type(OctetString):
    """Custom type cLWAGuestUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CLWAGuestUserName_Type.__name__ = "OctetString"
_CLWAGuestUserName_Object = MibScalar
cLWAGuestUserName = _CLWAGuestUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 1, 1),
    _CLWAGuestUserName_Type()
)
cLWAGuestUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWAGuestUserName.setStatus("current")
_CiscoLwappWebAuthMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBObjects = _CiscoLwappWebAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2)
)
_CiscoLwappWebAuthConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthConfig = _CiscoLwappWebAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1)
)


class _CLWAWebAuthType_Type(Integer32):
    """Custom type cLWAWebAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalDefault", 1),
          ("internalCustom", 2),
          ("external", 3))
    )


_CLWAWebAuthType_Type.__name__ = "Integer32"
_CLWAWebAuthType_Object = MibScalar
cLWAWebAuthType = _CLWAWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 1),
    _CLWAWebAuthType_Type()
)
cLWAWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAWebAuthType.setStatus("current")


class _CLWAManufacturerLogo_Type(TruthValue):
    """Custom type cLWAManufacturerLogo based on TruthValue"""
    defaultValue = 1


_CLWAManufacturerLogo_Type.__name__ = "TruthValue"
_CLWAManufacturerLogo_Object = MibScalar
cLWAManufacturerLogo = _CLWAManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 2),
    _CLWAManufacturerLogo_Type()
)
cLWAManufacturerLogo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAManufacturerLogo.setStatus("current")
_CLWACustomLogoFileName_Type = SnmpAdminString
_CLWACustomLogoFileName_Object = MibScalar
cLWACustomLogoFileName = _CLWACustomLogoFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 3),
    _CLWACustomLogoFileName_Type()
)
cLWACustomLogoFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWACustomLogoFileName.setStatus("current")


class _CLWACustomWebTitle_Type(SnmpAdminString):
    """Custom type cLWACustomWebTitle based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLWACustomWebTitle_Type.__name__ = "SnmpAdminString"
_CLWACustomWebTitle_Object = MibScalar
cLWACustomWebTitle = _CLWACustomWebTitle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 4),
    _CLWACustomWebTitle_Type()
)
cLWACustomWebTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebTitle.setStatus("current")


class _CLWACustomWebMessage_Type(SnmpAdminString):
    """Custom type cLWACustomWebMessage based on SnmpAdminString"""
    defaultValue = OctetString("")


_CLWACustomWebMessage_Type.__name__ = "SnmpAdminString"
_CLWACustomWebMessage_Object = MibScalar
cLWACustomWebMessage = _CLWACustomWebMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 5),
    _CLWACustomWebMessage_Type()
)
cLWACustomWebMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebMessage.setStatus("deprecated")
_CLWACustomWebRedirectURL_Type = CiscoURLString
_CLWACustomWebRedirectURL_Object = MibScalar
cLWACustomWebRedirectURL = _CLWACustomWebRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 6),
    _CLWACustomWebRedirectURL_Type()
)
cLWACustomWebRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebRedirectURL.setStatus("current")
_CLWAExternalWebAuthURL_Type = CiscoURLString
_CLWAExternalWebAuthURL_Object = MibScalar
cLWAExternalWebAuthURL = _CLWAExternalWebAuthURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 7),
    _CLWAExternalWebAuthURL_Type()
)
cLWAExternalWebAuthURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAExternalWebAuthURL.setStatus("current")
_CLWebAuthWlanConfigTable_Object = MibTable
cLWebAuthWlanConfigTable = _CLWebAuthWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8)
)
if mibBuilder.loadTexts:
    cLWebAuthWlanConfigTable.setStatus("current")
_CLWebAuthWlanConfigEntry_Object = MibTableRow
cLWebAuthWlanConfigEntry = _CLWebAuthWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1)
)
cLWebAuthWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWebAuthWlanConfigEntry.setStatus("current")


class _CLWlanGlobalWebAuthConfig_Type(TruthValue):
    """Custom type cLWlanGlobalWebAuthConfig based on TruthValue"""
    defaultValue = 2


_CLWlanGlobalWebAuthConfig_Type.__name__ = "TruthValue"
_CLWlanGlobalWebAuthConfig_Object = MibTableColumn
cLWlanGlobalWebAuthConfig = _CLWlanGlobalWebAuthConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 1),
    _CLWlanGlobalWebAuthConfig_Type()
)
cLWlanGlobalWebAuthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanGlobalWebAuthConfig.setStatus("current")


class _CLWlanWebAuthType_Type(CLWebAuthType):
    """Custom type cLWlanWebAuthType based on CLWebAuthType"""
    defaultValue = 1


_CLWlanWebAuthType_Type.__name__ = "CLWebAuthType"
_CLWlanWebAuthType_Object = MibTableColumn
cLWlanWebAuthType = _CLWlanWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 2),
    _CLWlanWebAuthType_Type()
)
cLWlanWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWebAuthType.setStatus("current")
_CLWlanWebAuthLoginPage_Type = SnmpAdminString
_CLWlanWebAuthLoginPage_Object = MibTableColumn
cLWlanWebAuthLoginPage = _CLWlanWebAuthLoginPage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 3),
    _CLWlanWebAuthLoginPage_Type()
)
cLWlanWebAuthLoginPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWebAuthLoginPage.setStatus("current")
_CLWlanExternalWebAuthUrl_Type = CiscoURLString
_CLWlanExternalWebAuthUrl_Object = MibTableColumn
cLWlanExternalWebAuthUrl = _CLWlanExternalWebAuthUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 4),
    _CLWlanExternalWebAuthUrl_Type()
)
cLWlanExternalWebAuthUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanExternalWebAuthUrl.setStatus("current")
_CLWlanWebAuthLoginFailurePage_Type = SnmpAdminString
_CLWlanWebAuthLoginFailurePage_Object = MibTableColumn
cLWlanWebAuthLoginFailurePage = _CLWlanWebAuthLoginFailurePage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 5),
    _CLWlanWebAuthLoginFailurePage_Type()
)
cLWlanWebAuthLoginFailurePage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWebAuthLoginFailurePage.setStatus("current")
_CLWlanWebAuthLogoutPage_Type = SnmpAdminString
_CLWlanWebAuthLogoutPage_Object = MibTableColumn
cLWlanWebAuthLogoutPage = _CLWlanWebAuthLogoutPage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 6),
    _CLWlanWebAuthLogoutPage_Type()
)
cLWlanWebAuthLogoutPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWebAuthLogoutPage.setStatus("current")


class _CLWlanExternalWebAuthAcl_Type(SnmpAdminString):
    """Custom type cLWlanExternalWebAuthAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanExternalWebAuthAcl_Type.__name__ = "SnmpAdminString"
_CLWlanExternalWebAuthAcl_Object = MibTableColumn
cLWlanExternalWebAuthAcl = _CLWlanExternalWebAuthAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 7),
    _CLWlanExternalWebAuthAcl_Type()
)
cLWlanExternalWebAuthAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanExternalWebAuthAcl.setStatus("current")


class _CLWlanWebAuthCaptiveBypassMode_Type(Integer32):
    """Custom type cLWlanWebAuthCaptiveBypassMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("none", 3))
    )


_CLWlanWebAuthCaptiveBypassMode_Type.__name__ = "Integer32"
_CLWlanWebAuthCaptiveBypassMode_Object = MibTableColumn
cLWlanWebAuthCaptiveBypassMode = _CLWlanWebAuthCaptiveBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 8, 1, 8),
    _CLWlanWebAuthCaptiveBypassMode_Type()
)
cLWlanWebAuthCaptiveBypassMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWebAuthCaptiveBypassMode.setStatus("current")


class _CLWACustomWebMessageRev1_Type(OctetString):
    """Custom type cLWACustomWebMessageRev1 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_CLWACustomWebMessageRev1_Type.__name__ = "OctetString"
_CLWACustomWebMessageRev1_Object = MibScalar
cLWACustomWebMessageRev1 = _CLWACustomWebMessageRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 9),
    _CLWACustomWebMessageRev1_Type()
)
cLWACustomWebMessageRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebMessageRev1.setStatus("current")


class _CLWAProxyRedirectMode_Type(TruthValue):
    """Custom type cLWAProxyRedirectMode based on TruthValue"""
    defaultValue = 2


_CLWAProxyRedirectMode_Type.__name__ = "TruthValue"
_CLWAProxyRedirectMode_Object = MibScalar
cLWAProxyRedirectMode = _CLWAProxyRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 10),
    _CLWAProxyRedirectMode_Type()
)
cLWAProxyRedirectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAProxyRedirectMode.setStatus("current")


class _CLWAProxyRedirectPortNumber_Type(InetPortNumber):
    """Custom type cLWAProxyRedirectPortNumber based on InetPortNumber"""
    defaultValue = 80


_CLWAProxyRedirectPortNumber_Type.__name__ = "InetPortNumber"
_CLWAProxyRedirectPortNumber_Object = MibScalar
cLWAProxyRedirectPortNumber = _CLWAProxyRedirectPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 11),
    _CLWAProxyRedirectPortNumber_Type()
)
cLWAProxyRedirectPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAProxyRedirectPortNumber.setStatus("current")


class _CLWAWebAuthSecureWeb_Type(TruthValue):
    """Custom type cLWAWebAuthSecureWeb based on TruthValue"""
    defaultValue = 2


_CLWAWebAuthSecureWeb_Type.__name__ = "TruthValue"
_CLWAWebAuthSecureWeb_Object = MibScalar
cLWAWebAuthSecureWeb = _CLWAWebAuthSecureWeb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 12),
    _CLWAWebAuthSecureWeb_Type()
)
cLWAWebAuthSecureWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAWebAuthSecureWeb.setStatus("current")


class _CLWAWebAuthLoginSuccessPageMode_Type(Integer32):
    """Custom type cLWAWebAuthLoginSuccessPageMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("none", 2))
    )


_CLWAWebAuthLoginSuccessPageMode_Type.__name__ = "Integer32"
_CLWAWebAuthLoginSuccessPageMode_Object = MibScalar
cLWAWebAuthLoginSuccessPageMode = _CLWAWebAuthLoginSuccessPageMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 13),
    _CLWAWebAuthLoginSuccessPageMode_Type()
)
cLWAWebAuthLoginSuccessPageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAWebAuthLoginSuccessPageMode.setStatus("current")


class _CLWACaptiveBypassMode_Type(TruthValue):
    """Custom type cLWACaptiveBypassMode based on TruthValue"""
    defaultValue = 2


_CLWACaptiveBypassMode_Type.__name__ = "TruthValue"
_CLWACaptiveBypassMode_Object = MibScalar
cLWACaptiveBypassMode = _CLWACaptiveBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 14),
    _CLWACaptiveBypassMode_Type()
)
cLWACaptiveBypassMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACaptiveBypassMode.setStatus("current")
_CiscoLwappWebAuthExtConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthExtConfig = _CiscoLwappWebAuthExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2)
)
_CLWAExternalWebServerTable_Object = MibTable
cLWAExternalWebServerTable = _CLWAExternalWebServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cLWAExternalWebServerTable.setStatus("current")
_CLWAExternalWebServerEntry_Object = MibTableRow
cLWAExternalWebServerEntry = _CLWAExternalWebServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1)
)
cLWAExternalWebServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerIndex"),
)
if mibBuilder.loadTexts:
    cLWAExternalWebServerEntry.setStatus("current")


class _CLWAExternalWebServerIndex_Type(Unsigned32):
    """Custom type cLWAExternalWebServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWAExternalWebServerIndex_Type.__name__ = "Unsigned32"
_CLWAExternalWebServerIndex_Object = MibTableColumn
cLWAExternalWebServerIndex = _CLWAExternalWebServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 1),
    _CLWAExternalWebServerIndex_Type()
)
cLWAExternalWebServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWAExternalWebServerIndex.setStatus("current")
_CLWAExternalWebServerAddrType_Type = InetAddressType
_CLWAExternalWebServerAddrType_Object = MibTableColumn
cLWAExternalWebServerAddrType = _CLWAExternalWebServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 2),
    _CLWAExternalWebServerAddrType_Type()
)
cLWAExternalWebServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWAExternalWebServerAddrType.setStatus("current")
_CLWAExternalWebServerAddr_Type = InetAddress
_CLWAExternalWebServerAddr_Object = MibTableColumn
cLWAExternalWebServerAddr = _CLWAExternalWebServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 3),
    _CLWAExternalWebServerAddr_Type()
)
cLWAExternalWebServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWAExternalWebServerAddr.setStatus("current")
_CLWAExternalWebServerRowStatus_Type = RowStatus
_CLWAExternalWebServerRowStatus_Object = MibTableColumn
cLWAExternalWebServerRowStatus = _CLWAExternalWebServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 4),
    _CLWAExternalWebServerRowStatus_Type()
)
cLWAExternalWebServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWAExternalWebServerRowStatus.setStatus("current")
_CiscoLwappLocalNetUserConfig_ObjectIdentity = ObjectIdentity
ciscoLwappLocalNetUserConfig = _CiscoLwappLocalNetUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3)
)
_CLWALocalNetUserTable_Object = MibTable
cLWALocalNetUserTable = _CLWALocalNetUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cLWALocalNetUserTable.setStatus("current")
_CLWALocalNetUserEntry_Object = MibTableRow
cLWALocalNetUserEntry = _CLWALocalNetUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1)
)
cLWALocalNetUserEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserName"),
)
if mibBuilder.loadTexts:
    cLWALocalNetUserEntry.setStatus("current")
_CLWALocalNetUserName_Type = SnmpAdminString
_CLWALocalNetUserName_Object = MibTableColumn
cLWALocalNetUserName = _CLWALocalNetUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 1),
    _CLWALocalNetUserName_Type()
)
cLWALocalNetUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWALocalNetUserName.setStatus("current")
_CLWALocalNetUserIsGuest_Type = TruthValue
_CLWALocalNetUserIsGuest_Object = MibTableColumn
cLWALocalNetUserIsGuest = _CLWALocalNetUserIsGuest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 2),
    _CLWALocalNetUserIsGuest_Type()
)
cLWALocalNetUserIsGuest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWALocalNetUserIsGuest.setStatus("current")
_CLWALocalNetUserRole_Type = OctetString
_CLWALocalNetUserRole_Object = MibTableColumn
cLWALocalNetUserRole = _CLWALocalNetUserRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 3),
    _CLWALocalNetUserRole_Type()
)
cLWALocalNetUserRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWALocalNetUserRole.setStatus("current")
_CLWALocalNetUserLoginTime_Type = Unsigned32
_CLWALocalNetUserLoginTime_Object = MibTableColumn
cLWALocalNetUserLoginTime = _CLWALocalNetUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 4),
    _CLWALocalNetUserLoginTime_Type()
)
cLWALocalNetUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWALocalNetUserLoginTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWALocalNetUserLoginTime.setUnits("seconds")
_CLWALocalNetUserLoginCount_Type = Unsigned32
_CLWALocalNetUserLoginCount_Object = MibTableColumn
cLWALocalNetUserLoginCount = _CLWALocalNetUserLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 5),
    _CLWALocalNetUserLoginCount_Type()
)
cLWALocalNetUserLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWALocalNetUserLoginCount.setStatus("current")
_CLWALocalNetUserLifeTime_Type = TimeTicks
_CLWALocalNetUserLifeTime_Object = MibTableColumn
cLWALocalNetUserLifeTime = _CLWALocalNetUserLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 6),
    _CLWALocalNetUserLifeTime_Type()
)
cLWALocalNetUserLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWALocalNetUserLifeTime.setStatus("current")


class _CLWALocalNetUserMaxGuestRoles_Type(Unsigned32):
    """Custom type cLWALocalNetUserMaxGuestRoles based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWALocalNetUserMaxGuestRoles_Type.__name__ = "Unsigned32"
_CLWALocalNetUserMaxGuestRoles_Object = MibScalar
cLWALocalNetUserMaxGuestRoles = _CLWALocalNetUserMaxGuestRoles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 2),
    _CLWALocalNetUserMaxGuestRoles_Type()
)
cLWALocalNetUserMaxGuestRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWALocalNetUserMaxGuestRoles.setStatus("current")


class _CLWALocalNetUserGuestRolesCount_Type(Unsigned32):
    """Custom type cLWALocalNetUserGuestRolesCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWALocalNetUserGuestRolesCount_Type.__name__ = "Unsigned32"
_CLWALocalNetUserGuestRolesCount_Object = MibScalar
cLWALocalNetUserGuestRolesCount = _CLWALocalNetUserGuestRolesCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 3),
    _CLWALocalNetUserGuestRolesCount_Type()
)
cLWALocalNetUserGuestRolesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWALocalNetUserGuestRolesCount.setStatus("current")
_CLWALocalNetUserRoleTable_Object = MibTable
cLWALocalNetUserRoleTable = _CLWALocalNetUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4)
)
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleTable.setStatus("current")
_CLWALocalNetUserRoleEntry_Object = MibTableRow
cLWALocalNetUserRoleEntry = _CLWALocalNetUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1)
)
cLWALocalNetUserRoleEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRoleName"),
)
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleEntry.setStatus("current")
_CLWALocalNetUserRoleName_Type = SnmpAdminString
_CLWALocalNetUserRoleName_Object = MibTableColumn
cLWALocalNetUserRoleName = _CLWALocalNetUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1, 1),
    _CLWALocalNetUserRoleName_Type()
)
cLWALocalNetUserRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleName.setStatus("current")


class _CLWALocalNetUserRoleAverageDataRate_Type(Unsigned32):
    """Custom type cLWALocalNetUserRoleAverageDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CLWALocalNetUserRoleAverageDataRate_Type.__name__ = "Unsigned32"
_CLWALocalNetUserRoleAverageDataRate_Object = MibTableColumn
cLWALocalNetUserRoleAverageDataRate = _CLWALocalNetUserRoleAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1, 2),
    _CLWALocalNetUserRoleAverageDataRate_Type()
)
cLWALocalNetUserRoleAverageDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleAverageDataRate.setUnits("Kbps")


class _CLWALocalNetUserRoleBurstDataRate_Type(Unsigned32):
    """Custom type cLWALocalNetUserRoleBurstDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CLWALocalNetUserRoleBurstDataRate_Type.__name__ = "Unsigned32"
_CLWALocalNetUserRoleBurstDataRate_Object = MibTableColumn
cLWALocalNetUserRoleBurstDataRate = _CLWALocalNetUserRoleBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1, 3),
    _CLWALocalNetUserRoleBurstDataRate_Type()
)
cLWALocalNetUserRoleBurstDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleBurstDataRate.setUnits("Kbps")


class _CLWALocalNetUserRoleAvgRealTimeDataRate_Type(Unsigned32):
    """Custom type cLWALocalNetUserRoleAvgRealTimeDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CLWALocalNetUserRoleAvgRealTimeDataRate_Type.__name__ = "Unsigned32"
_CLWALocalNetUserRoleAvgRealTimeDataRate_Object = MibTableColumn
cLWALocalNetUserRoleAvgRealTimeDataRate = _CLWALocalNetUserRoleAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1, 4),
    _CLWALocalNetUserRoleAvgRealTimeDataRate_Type()
)
cLWALocalNetUserRoleAvgRealTimeDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleAvgRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleAvgRealTimeDataRate.setUnits("Kbps")


class _CLWALocalNetUserRoleBurstRealTimeDataRate_Type(Unsigned32):
    """Custom type cLWALocalNetUserRoleBurstRealTimeDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CLWALocalNetUserRoleBurstRealTimeDataRate_Type.__name__ = "Unsigned32"
_CLWALocalNetUserRoleBurstRealTimeDataRate_Object = MibTableColumn
cLWALocalNetUserRoleBurstRealTimeDataRate = _CLWALocalNetUserRoleBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1, 5),
    _CLWALocalNetUserRoleBurstRealTimeDataRate_Type()
)
cLWALocalNetUserRoleBurstRealTimeDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleBurstRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleBurstRealTimeDataRate.setUnits("Kbps")
_CLWALocalNetUserRoleRowStatus_Type = RowStatus
_CLWALocalNetUserRoleRowStatus_Object = MibTableColumn
cLWALocalNetUserRoleRowStatus = _CLWALocalNetUserRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 4, 1, 6),
    _CLWALocalNetUserRoleRowStatus_Type()
)
cLWALocalNetUserRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWALocalNetUserRoleRowStatus.setStatus("current")
_CiscoLwappWebPageList_ObjectIdentity = ObjectIdentity
ciscoLwappWebPageList = _CiscoLwappWebPageList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 4)
)
_CLWACustomizedWebPageListTable_Object = MibTable
cLWACustomizedWebPageListTable = _CLWACustomizedWebPageListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cLWACustomizedWebPageListTable.setStatus("current")
_CLWACustomizedWebPageListEntry_Object = MibTableRow
cLWACustomizedWebPageListEntry = _CLWACustomizedWebPageListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 4, 1, 1)
)
cLWACustomizedWebPageListEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomizedWebLoginPage"),
)
if mibBuilder.loadTexts:
    cLWACustomizedWebPageListEntry.setStatus("current")
_CLWACustomizedWebLoginPage_Type = SnmpAdminString
_CLWACustomizedWebLoginPage_Object = MibTableColumn
cLWACustomizedWebLoginPage = _CLWACustomizedWebLoginPage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 4, 1, 1, 1),
    _CLWACustomizedWebLoginPage_Type()
)
cLWACustomizedWebLoginPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWACustomizedWebLoginPage.setStatus("current")
_CiscoLwappGuestUserSessionStatus_ObjectIdentity = ObjectIdentity
ciscoLwappGuestUserSessionStatus = _CiscoLwappGuestUserSessionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5)
)
_CLGuestUserSessionStatusTable_Object = MibTable
cLGuestUserSessionStatusTable = _CLGuestUserSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cLGuestUserSessionStatusTable.setStatus("current")
_CLGuestUserSessionStatusEntry_Object = MibTableRow
cLGuestUserSessionStatusEntry = _CLGuestUserSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1)
)
cLGuestUserSessionStatusEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserName"),
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserSessionId"),
)
if mibBuilder.loadTexts:
    cLGuestUserSessionStatusEntry.setStatus("current")


class _CLGuestUserName_Type(OctetString):
    """Custom type cLGuestUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CLGuestUserName_Type.__name__ = "OctetString"
_CLGuestUserName_Object = MibTableColumn
cLGuestUserName = _CLGuestUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 1),
    _CLGuestUserName_Type()
)
cLGuestUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLGuestUserName.setStatus("current")
_CLGuestUserSessionId_Type = Unsigned32
_CLGuestUserSessionId_Object = MibTableColumn
cLGuestUserSessionId = _CLGuestUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 2),
    _CLGuestUserSessionId_Type()
)
cLGuestUserSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLGuestUserSessionId.setStatus("current")
_CLGuestUserClientMacAddress_Type = MacAddress
_CLGuestUserClientMacAddress_Object = MibTableColumn
cLGuestUserClientMacAddress = _CLGuestUserClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 3),
    _CLGuestUserClientMacAddress_Type()
)
cLGuestUserClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserClientMacAddress.setStatus("current")
_CLGuestUserClientIpAddressType_Type = InetAddressType
_CLGuestUserClientIpAddressType_Object = MibTableColumn
cLGuestUserClientIpAddressType = _CLGuestUserClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 4),
    _CLGuestUserClientIpAddressType_Type()
)
cLGuestUserClientIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserClientIpAddressType.setStatus("current")
_CLGuestUserClientIpAddress_Type = InetAddress
_CLGuestUserClientIpAddress_Object = MibTableColumn
cLGuestUserClientIpAddress = _CLGuestUserClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 5),
    _CLGuestUserClientIpAddress_Type()
)
cLGuestUserClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserClientIpAddress.setStatus("current")
_CLGuestUserApMacAddress_Type = MacAddress
_CLGuestUserApMacAddress_Object = MibTableColumn
cLGuestUserApMacAddress = _CLGuestUserApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 6),
    _CLGuestUserApMacAddress_Type()
)
cLGuestUserApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserApMacAddress.setStatus("current")
_CLGuestUserLoggedInTime_Type = Unsigned32
_CLGuestUserLoggedInTime_Object = MibTableColumn
cLGuestUserLoggedInTime = _CLGuestUserLoggedInTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 7),
    _CLGuestUserLoggedInTime_Type()
)
cLGuestUserLoggedInTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserLoggedInTime.setStatus("current")
if mibBuilder.loadTexts:
    cLGuestUserLoggedInTime.setUnits("seconds")
_CLGuestUserLoggedOutTime_Type = Unsigned32
_CLGuestUserLoggedOutTime_Object = MibTableColumn
cLGuestUserLoggedOutTime = _CLGuestUserLoggedOutTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 8),
    _CLGuestUserLoggedOutTime_Type()
)
cLGuestUserLoggedOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserLoggedOutTime.setStatus("current")
if mibBuilder.loadTexts:
    cLGuestUserLoggedOutTime.setUnits("seconds")
_CLGuestUserBytesReceived_Type = Counter64
_CLGuestUserBytesReceived_Object = MibTableColumn
cLGuestUserBytesReceived = _CLGuestUserBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 9),
    _CLGuestUserBytesReceived_Type()
)
cLGuestUserBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cLGuestUserBytesReceived.setUnits("Bytes")
_CLGuestUserBytesTransmitted_Type = Counter64
_CLGuestUserBytesTransmitted_Object = MibTableColumn
cLGuestUserBytesTransmitted = _CLGuestUserBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 5, 1, 1, 10),
    _CLGuestUserBytesTransmitted_Type()
)
cLGuestUserBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestUserBytesTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    cLGuestUserBytesTransmitted.setUnits("Bytes")
_CiscoLwappPortalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappPortalConfig = _CiscoLwappPortalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6)
)
_CLWAPortalConfigTable_Object = MibTable
cLWAPortalConfigTable = _CLWAPortalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cLWAPortalConfigTable.setStatus("current")
_CLWAPortalConfigEntry_Object = MibTableRow
cLWAPortalConfigEntry = _CLWAPortalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6, 1, 1)
)
cLWAPortalConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalIndex"),
)
if mibBuilder.loadTexts:
    cLWAPortalConfigEntry.setStatus("current")
_CLWAPortalIndex_Type = Unsigned32
_CLWAPortalIndex_Object = MibTableColumn
cLWAPortalIndex = _CLWAPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6, 1, 1, 1),
    _CLWAPortalIndex_Type()
)
cLWAPortalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWAPortalIndex.setStatus("current")
_CLWAPortalServerAddrType_Type = InetAddressType
_CLWAPortalServerAddrType_Object = MibTableColumn
cLWAPortalServerAddrType = _CLWAPortalServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6, 1, 1, 2),
    _CLWAPortalServerAddrType_Type()
)
cLWAPortalServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalServerAddrType.setStatus("current")
_CLWAPortalServerIp_Type = InetAddress
_CLWAPortalServerIp_Object = MibTableColumn
cLWAPortalServerIp = _CLWAPortalServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6, 1, 1, 3),
    _CLWAPortalServerIp_Type()
)
cLWAPortalServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalServerIp.setStatus("current")
_CLWAPortalUnreachSet_Type = TruthValue
_CLWAPortalUnreachSet_Object = MibTableColumn
cLWAPortalUnreachSet = _CLWAPortalUnreachSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 6, 1, 1, 4),
    _CLWAPortalUnreachSet_Type()
)
cLWAPortalUnreachSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalUnreachSet.setStatus("current")
_CiscoLwappPortalStats_ObjectIdentity = ObjectIdentity
ciscoLwappPortalStats = _CiscoLwappPortalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7)
)
_CLWAPortalCounterTable_Object = MibTable
cLWAPortalCounterTable = _CLWAPortalCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cLWAPortalCounterTable.setStatus("current")
_CLWAPortalCounterEntry_Object = MibTableRow
cLWAPortalCounterEntry = _CLWAPortalCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1)
)
cLWAPortalCounterEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalIndex"),
)
if mibBuilder.loadTexts:
    cLWAPortalCounterEntry.setStatus("current")
_CLWAPortalChallengeReq_Type = Counter32
_CLWAPortalChallengeReq_Object = MibTableColumn
cLWAPortalChallengeReq = _CLWAPortalChallengeReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 1),
    _CLWAPortalChallengeReq_Type()
)
cLWAPortalChallengeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalChallengeReq.setStatus("current")
_CLWAPortalChallengeAck_Type = Counter32
_CLWAPortalChallengeAck_Object = MibTableColumn
cLWAPortalChallengeAck = _CLWAPortalChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 2),
    _CLWAPortalChallengeAck_Type()
)
cLWAPortalChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalChallengeAck.setStatus("current")
_CLWAPortalChallengeErr_Type = Counter32
_CLWAPortalChallengeErr_Object = MibTableColumn
cLWAPortalChallengeErr = _CLWAPortalChallengeErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 3),
    _CLWAPortalChallengeErr_Type()
)
cLWAPortalChallengeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalChallengeErr.setStatus("current")
_CLWAPortalAuthenticationReq_Type = Counter32
_CLWAPortalAuthenticationReq_Object = MibTableColumn
cLWAPortalAuthenticationReq = _CLWAPortalAuthenticationReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 4),
    _CLWAPortalAuthenticationReq_Type()
)
cLWAPortalAuthenticationReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthenticationReq.setStatus("current")
_CLWAPortalAuthenticationAck_Type = Counter32
_CLWAPortalAuthenticationAck_Object = MibTableColumn
cLWAPortalAuthenticationAck = _CLWAPortalAuthenticationAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 5),
    _CLWAPortalAuthenticationAck_Type()
)
cLWAPortalAuthenticationAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthenticationAck.setStatus("current")
_CLWAPortalAuthenticationErr_Type = Counter32
_CLWAPortalAuthenticationErr_Object = MibTableColumn
cLWAPortalAuthenticationErr = _CLWAPortalAuthenticationErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 6),
    _CLWAPortalAuthenticationErr_Type()
)
cLWAPortalAuthenticationErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthenticationErr.setStatus("current")
_CLWAPortalLogoutReq_Type = Counter32
_CLWAPortalLogoutReq_Object = MibTableColumn
cLWAPortalLogoutReq = _CLWAPortalLogoutReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 7),
    _CLWAPortalLogoutReq_Type()
)
cLWAPortalLogoutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalLogoutReq.setStatus("current")
_CLWAPortalLogoutAck_Type = Counter32
_CLWAPortalLogoutAck_Object = MibTableColumn
cLWAPortalLogoutAck = _CLWAPortalLogoutAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 8),
    _CLWAPortalLogoutAck_Type()
)
cLWAPortalLogoutAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalLogoutAck.setStatus("current")
_CLWAPortalLogoutErr_Type = Counter32
_CLWAPortalLogoutErr_Object = MibTableColumn
cLWAPortalLogoutErr = _CLWAPortalLogoutErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 9),
    _CLWAPortalLogoutErr_Type()
)
cLWAPortalLogoutErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalLogoutErr.setStatus("current")
_CLWAPortalLogoutNTF_Type = Counter32
_CLWAPortalLogoutNTF_Object = MibTableColumn
cLWAPortalLogoutNTF = _CLWAPortalLogoutNTF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 10),
    _CLWAPortalLogoutNTF_Type()
)
cLWAPortalLogoutNTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalLogoutNTF.setStatus("current")
_CLWAPortalUnknownReq_Type = Counter32
_CLWAPortalUnknownReq_Object = MibTableColumn
cLWAPortalUnknownReq = _CLWAPortalUnknownReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 11),
    _CLWAPortalUnknownReq_Type()
)
cLWAPortalUnknownReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalUnknownReq.setStatus("current")
_CLWAPortalAuthenticatedClient_Type = Counter32
_CLWAPortalAuthenticatedClient_Object = MibTableColumn
cLWAPortalAuthenticatedClient = _CLWAPortalAuthenticatedClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 12),
    _CLWAPortalAuthenticatedClient_Type()
)
cLWAPortalAuthenticatedClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthenticatedClient.setStatus("current")
_CLWAPortalAuthenticatedMaxClient_Type = Counter32
_CLWAPortalAuthenticatedMaxClient_Object = MibTableColumn
cLWAPortalAuthenticatedMaxClient = _CLWAPortalAuthenticatedMaxClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 13),
    _CLWAPortalAuthenticatedMaxClient_Type()
)
cLWAPortalAuthenticatedMaxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthenticatedMaxClient.setStatus("current")
_CLWAPortalHttpReq_Type = Counter32
_CLWAPortalHttpReq_Object = MibTableColumn
cLWAPortalHttpReq = _CLWAPortalHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 7, 1, 1, 14),
    _CLWAPortalHttpReq_Type()
)
cLWAPortalHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalHttpReq.setStatus("current")
_CiscoLwappPortalTotalStats_ObjectIdentity = ObjectIdentity
ciscoLwappPortalTotalStats = _CiscoLwappPortalTotalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8)
)
_CLWAPortalDisconnectOnlineUsersCount_Type = Counter32
_CLWAPortalDisconnectOnlineUsersCount_Object = MibScalar
cLWAPortalDisconnectOnlineUsersCount = _CLWAPortalDisconnectOnlineUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8, 1),
    _CLWAPortalDisconnectOnlineUsersCount_Type()
)
cLWAPortalDisconnectOnlineUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalDisconnectOnlineUsersCount.setStatus("current")
_CLWAPortalConnectLostUsersCount_Type = Counter32
_CLWAPortalConnectLostUsersCount_Object = MibScalar
cLWAPortalConnectLostUsersCount = _CLWAPortalConnectLostUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8, 2),
    _CLWAPortalConnectLostUsersCount_Type()
)
cLWAPortalConnectLostUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalConnectLostUsersCount.setStatus("current")
_CLWAPortalAuthReqCount_Type = Counter32
_CLWAPortalAuthReqCount_Object = MibScalar
cLWAPortalAuthReqCount = _CLWAPortalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8, 3),
    _CLWAPortalAuthReqCount_Type()
)
cLWAPortalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthReqCount.setStatus("current")
_CLWAPortalAuthReqSucessCount_Type = Counter32
_CLWAPortalAuthReqSucessCount_Object = MibScalar
cLWAPortalAuthReqSucessCount = _CLWAPortalAuthReqSucessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8, 4),
    _CLWAPortalAuthReqSucessCount_Type()
)
cLWAPortalAuthReqSucessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthReqSucessCount.setStatus("current")
_CLWAPortalAuthReqFailureCount_Type = Counter32
_CLWAPortalAuthReqFailureCount_Object = MibScalar
cLWAPortalAuthReqFailureCount = _CLWAPortalAuthReqFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8, 5),
    _CLWAPortalAuthReqFailureCount_Type()
)
cLWAPortalAuthReqFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalAuthReqFailureCount.setStatus("current")
_CLWAPortalMaxAuthClient_Type = Integer32
_CLWAPortalMaxAuthClient_Object = MibScalar
cLWAPortalMaxAuthClient = _CLWAPortalMaxAuthClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 8, 6),
    _CLWAPortalMaxAuthClient_Type()
)
cLWAPortalMaxAuthClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWAPortalMaxAuthClient.setStatus("current")
_CiscoLwappWebAuthMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBConform = _CiscoLwappWebAuthMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3)
)
_CiscoLwappWebAuthMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBCompliances = _CiscoLwappWebAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1)
)
_CiscoLwappWebAuthMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBGroups = _CiscoLwappWebAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2)
)

# Managed Objects groups

cLWACustomWebAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 1)
)
cLWACustomWebAuthGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAManufacturerLogo"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomLogoFileName"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebTitle"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebMessage"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebRedirectURL"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthURL"))
)
if mibBuilder.loadTexts:
    cLWACustomWebAuthGroup.setStatus("deprecated")

cLWAExternalWebAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 2)
)
cLWAExternalWebAuthGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerAddrType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerAddr"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerRowStatus"))
)
if mibBuilder.loadTexts:
    cLWAExternalWebAuthGroup.setStatus("current")

cLWAGuestAccessNotifObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 3)
)
cLWAGuestAccessNotifObjGroup.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName")
)
if mibBuilder.loadTexts:
    cLWAGuestAccessNotifObjGroup.setStatus("current")

cLWAGuestUserConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 5)
)
cLWAGuestUserConfigGroup.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserIsGuest")
)
if mibBuilder.loadTexts:
    cLWAGuestUserConfigGroup.setStatus("current")

cLWAProxyRedirectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 6)
)
cLWAProxyRedirectGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAProxyRedirectMode"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAProxyRedirectPortNumber"))
)
if mibBuilder.loadTexts:
    cLWAProxyRedirectGroup.setStatus("current")

cLWAGuestUserStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 7)
)
cLWAGuestUserStatusGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientMacAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientIpAddressType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientIpAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserApMacAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserLoggedInTime"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserLoggedOutTime"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserBytesReceived"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserBytesTransmitted"))
)
if mibBuilder.loadTexts:
    cLWAGuestUserStatusGroup.setStatus("current")

cLWALocalNetUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 8)
)
cLWALocalNetUserGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRole"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserLoginTime"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserLoginCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserMaxGuestRoles"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserGuestRolesCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRoleAverageDataRate"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRoleBurstDataRate"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRoleAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRoleBurstRealTimeDataRate"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserLifeTime"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserRoleRowStatus"))
)
if mibBuilder.loadTexts:
    cLWALocalNetUserGroup.setStatus("current")

cLWAWebAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 10)
)
cLWAWebAuthGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanGlobalWebAuthConfig"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanWebAuthType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanWebAuthLoginPage"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanExternalWebAuthUrl"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanWebAuthLoginFailurePage"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanWebAuthLogoutPage"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomizedWebLoginPage"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanExternalWebAuthAcl"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWlanWebAuthCaptiveBypassMode"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalServerAddrType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalServerIp"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalUnreachSet"))
)
if mibBuilder.loadTexts:
    cLWAWebAuthGroup.setStatus("current")

cLWACustomWebAuthGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 11)
)
cLWACustomWebAuthGroupRev1.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAManufacturerLogo"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomLogoFileName"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebTitle"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebMessageRev1"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebRedirectURL"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthURL"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthSecureWeb"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthLoginSuccessPageMode"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACaptiveBypassMode"))
)
if mibBuilder.loadTexts:
    cLWACustomWebAuthGroupRev1.setStatus("current")

cLWAPortalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 12)
)
cLWAPortalStatsGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalChallengeReq"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalChallengeAck"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalChallengeErr"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthenticationReq"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthenticationAck"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthenticationErr"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalLogoutReq"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalLogoutAck"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalLogoutErr"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalLogoutNTF"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalUnknownReq"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthenticatedClient"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthenticatedMaxClient"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalHttpReq"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalDisconnectOnlineUsersCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalConnectLostUsersCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthReqCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthReqSucessCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalAuthReqFailureCount"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalMaxAuthClient"))
)
if mibBuilder.loadTexts:
    cLWAPortalStatsGroup.setStatus("current")


# Notification objects

cLWAGuestUserRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 1)
)
cLWAGuestUserRemoved.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName")
)
if mibBuilder.loadTexts:
    cLWAGuestUserRemoved.setStatus(
        "current"
    )

cLWAGuestUserAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 2)
)
cLWAGuestUserAdded.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName")
)
if mibBuilder.loadTexts:
    cLWAGuestUserAdded.setStatus(
        "current"
    )

cLWAGuestUserLoggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 3)
)
cLWAGuestUserLoggedIn.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientMacAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientIpAddressType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientIpAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    cLWAGuestUserLoggedIn.setStatus(
        "current"
    )

cLWAGuestUserLoggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 4)
)
cLWAGuestUserLoggedOut.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientMacAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientIpAddressType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserClientIpAddress"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLGuestUserApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    cLWAGuestUserLoggedOut.setStatus(
        "current"
    )

cLWAPortalUnreachNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 5)
)
cLWAPortalUnreachNotify.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalServerAddrType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalServerIp"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalUnreachSet"))
)
if mibBuilder.loadTexts:
    cLWAPortalUnreachNotify.setStatus(
        "current"
    )


# Notifications groups

cLWAGuestAccessNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 4)
)
cLWAGuestAccessNotifGroup.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserRemoved")
)
if mibBuilder.loadTexts:
    cLWAGuestAccessNotifGroup.setStatus(
        "current"
    )

cLWAGuestAccessNotifGroupSup01 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 9)
)
cLWAGuestAccessNotifGroupSup01.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserAdded"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserLoggedIn"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserLoggedOut"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalUnreachNotify"))
)
if mibBuilder.loadTexts:
    cLWAGuestAccessNotifGroupSup01.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cLWebAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 1)
)
cLWebAuthMIBCompliance.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebAuthGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifObjGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifGroup"))
)
if mibBuilder.loadTexts:
    cLWebAuthMIBCompliance.setStatus(
        "deprecated"
    )

cLWebAuthMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 2)
)
cLWebAuthMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebAuthGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifObjGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserConfigGroup"))
)
if mibBuilder.loadTexts:
    cLWebAuthMIBComplianceRev1.setStatus(
        "deprecated"
    )

cLWebAuthMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 3)
)
cLWebAuthMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebAuthGroupRev1"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifObjGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserConfigGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAProxyRedirectGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserStatusGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestAccessNotifGroupSup01"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthGroup"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAPortalStatsGroup"))
)
if mibBuilder.loadTexts:
    cLWebAuthMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WEBAUTH-MIB",
    **{"ciscoLwappWebAuthMIB": ciscoLwappWebAuthMIB,
       "ciscoLwappWebAuthMIBNotifs": ciscoLwappWebAuthMIBNotifs,
       "cLWAGuestUserRemoved": cLWAGuestUserRemoved,
       "cLWAGuestUserAdded": cLWAGuestUserAdded,
       "cLWAGuestUserLoggedIn": cLWAGuestUserLoggedIn,
       "cLWAGuestUserLoggedOut": cLWAGuestUserLoggedOut,
       "cLWAPortalUnreachNotify": cLWAPortalUnreachNotify,
       "ciscoLwappWebAuthMIBNotifObjs": ciscoLwappWebAuthMIBNotifObjs,
       "cLWAGuestUserName": cLWAGuestUserName,
       "ciscoLwappWebAuthMIBObjects": ciscoLwappWebAuthMIBObjects,
       "ciscoLwappWebAuthConfig": ciscoLwappWebAuthConfig,
       "cLWAWebAuthType": cLWAWebAuthType,
       "cLWAManufacturerLogo": cLWAManufacturerLogo,
       "cLWACustomLogoFileName": cLWACustomLogoFileName,
       "cLWACustomWebTitle": cLWACustomWebTitle,
       "cLWACustomWebMessage": cLWACustomWebMessage,
       "cLWACustomWebRedirectURL": cLWACustomWebRedirectURL,
       "cLWAExternalWebAuthURL": cLWAExternalWebAuthURL,
       "cLWebAuthWlanConfigTable": cLWebAuthWlanConfigTable,
       "cLWebAuthWlanConfigEntry": cLWebAuthWlanConfigEntry,
       "cLWlanGlobalWebAuthConfig": cLWlanGlobalWebAuthConfig,
       "cLWlanWebAuthType": cLWlanWebAuthType,
       "cLWlanWebAuthLoginPage": cLWlanWebAuthLoginPage,
       "cLWlanExternalWebAuthUrl": cLWlanExternalWebAuthUrl,
       "cLWlanWebAuthLoginFailurePage": cLWlanWebAuthLoginFailurePage,
       "cLWlanWebAuthLogoutPage": cLWlanWebAuthLogoutPage,
       "cLWlanExternalWebAuthAcl": cLWlanExternalWebAuthAcl,
       "cLWlanWebAuthCaptiveBypassMode": cLWlanWebAuthCaptiveBypassMode,
       "cLWACustomWebMessageRev1": cLWACustomWebMessageRev1,
       "cLWAProxyRedirectMode": cLWAProxyRedirectMode,
       "cLWAProxyRedirectPortNumber": cLWAProxyRedirectPortNumber,
       "cLWAWebAuthSecureWeb": cLWAWebAuthSecureWeb,
       "cLWAWebAuthLoginSuccessPageMode": cLWAWebAuthLoginSuccessPageMode,
       "cLWACaptiveBypassMode": cLWACaptiveBypassMode,
       "ciscoLwappWebAuthExtConfig": ciscoLwappWebAuthExtConfig,
       "cLWAExternalWebServerTable": cLWAExternalWebServerTable,
       "cLWAExternalWebServerEntry": cLWAExternalWebServerEntry,
       "cLWAExternalWebServerIndex": cLWAExternalWebServerIndex,
       "cLWAExternalWebServerAddrType": cLWAExternalWebServerAddrType,
       "cLWAExternalWebServerAddr": cLWAExternalWebServerAddr,
       "cLWAExternalWebServerRowStatus": cLWAExternalWebServerRowStatus,
       "ciscoLwappLocalNetUserConfig": ciscoLwappLocalNetUserConfig,
       "cLWALocalNetUserTable": cLWALocalNetUserTable,
       "cLWALocalNetUserEntry": cLWALocalNetUserEntry,
       "cLWALocalNetUserName": cLWALocalNetUserName,
       "cLWALocalNetUserIsGuest": cLWALocalNetUserIsGuest,
       "cLWALocalNetUserRole": cLWALocalNetUserRole,
       "cLWALocalNetUserLoginTime": cLWALocalNetUserLoginTime,
       "cLWALocalNetUserLoginCount": cLWALocalNetUserLoginCount,
       "cLWALocalNetUserLifeTime": cLWALocalNetUserLifeTime,
       "cLWALocalNetUserMaxGuestRoles": cLWALocalNetUserMaxGuestRoles,
       "cLWALocalNetUserGuestRolesCount": cLWALocalNetUserGuestRolesCount,
       "cLWALocalNetUserRoleTable": cLWALocalNetUserRoleTable,
       "cLWALocalNetUserRoleEntry": cLWALocalNetUserRoleEntry,
       "cLWALocalNetUserRoleName": cLWALocalNetUserRoleName,
       "cLWALocalNetUserRoleAverageDataRate": cLWALocalNetUserRoleAverageDataRate,
       "cLWALocalNetUserRoleBurstDataRate": cLWALocalNetUserRoleBurstDataRate,
       "cLWALocalNetUserRoleAvgRealTimeDataRate": cLWALocalNetUserRoleAvgRealTimeDataRate,
       "cLWALocalNetUserRoleBurstRealTimeDataRate": cLWALocalNetUserRoleBurstRealTimeDataRate,
       "cLWALocalNetUserRoleRowStatus": cLWALocalNetUserRoleRowStatus,
       "ciscoLwappWebPageList": ciscoLwappWebPageList,
       "cLWACustomizedWebPageListTable": cLWACustomizedWebPageListTable,
       "cLWACustomizedWebPageListEntry": cLWACustomizedWebPageListEntry,
       "cLWACustomizedWebLoginPage": cLWACustomizedWebLoginPage,
       "ciscoLwappGuestUserSessionStatus": ciscoLwappGuestUserSessionStatus,
       "cLGuestUserSessionStatusTable": cLGuestUserSessionStatusTable,
       "cLGuestUserSessionStatusEntry": cLGuestUserSessionStatusEntry,
       "cLGuestUserName": cLGuestUserName,
       "cLGuestUserSessionId": cLGuestUserSessionId,
       "cLGuestUserClientMacAddress": cLGuestUserClientMacAddress,
       "cLGuestUserClientIpAddressType": cLGuestUserClientIpAddressType,
       "cLGuestUserClientIpAddress": cLGuestUserClientIpAddress,
       "cLGuestUserApMacAddress": cLGuestUserApMacAddress,
       "cLGuestUserLoggedInTime": cLGuestUserLoggedInTime,
       "cLGuestUserLoggedOutTime": cLGuestUserLoggedOutTime,
       "cLGuestUserBytesReceived": cLGuestUserBytesReceived,
       "cLGuestUserBytesTransmitted": cLGuestUserBytesTransmitted,
       "ciscoLwappPortalConfig": ciscoLwappPortalConfig,
       "cLWAPortalConfigTable": cLWAPortalConfigTable,
       "cLWAPortalConfigEntry": cLWAPortalConfigEntry,
       "cLWAPortalIndex": cLWAPortalIndex,
       "cLWAPortalServerAddrType": cLWAPortalServerAddrType,
       "cLWAPortalServerIp": cLWAPortalServerIp,
       "cLWAPortalUnreachSet": cLWAPortalUnreachSet,
       "ciscoLwappPortalStats": ciscoLwappPortalStats,
       "cLWAPortalCounterTable": cLWAPortalCounterTable,
       "cLWAPortalCounterEntry": cLWAPortalCounterEntry,
       "cLWAPortalChallengeReq": cLWAPortalChallengeReq,
       "cLWAPortalChallengeAck": cLWAPortalChallengeAck,
       "cLWAPortalChallengeErr": cLWAPortalChallengeErr,
       "cLWAPortalAuthenticationReq": cLWAPortalAuthenticationReq,
       "cLWAPortalAuthenticationAck": cLWAPortalAuthenticationAck,
       "cLWAPortalAuthenticationErr": cLWAPortalAuthenticationErr,
       "cLWAPortalLogoutReq": cLWAPortalLogoutReq,
       "cLWAPortalLogoutAck": cLWAPortalLogoutAck,
       "cLWAPortalLogoutErr": cLWAPortalLogoutErr,
       "cLWAPortalLogoutNTF": cLWAPortalLogoutNTF,
       "cLWAPortalUnknownReq": cLWAPortalUnknownReq,
       "cLWAPortalAuthenticatedClient": cLWAPortalAuthenticatedClient,
       "cLWAPortalAuthenticatedMaxClient": cLWAPortalAuthenticatedMaxClient,
       "cLWAPortalHttpReq": cLWAPortalHttpReq,
       "ciscoLwappPortalTotalStats": ciscoLwappPortalTotalStats,
       "cLWAPortalDisconnectOnlineUsersCount": cLWAPortalDisconnectOnlineUsersCount,
       "cLWAPortalConnectLostUsersCount": cLWAPortalConnectLostUsersCount,
       "cLWAPortalAuthReqCount": cLWAPortalAuthReqCount,
       "cLWAPortalAuthReqSucessCount": cLWAPortalAuthReqSucessCount,
       "cLWAPortalAuthReqFailureCount": cLWAPortalAuthReqFailureCount,
       "cLWAPortalMaxAuthClient": cLWAPortalMaxAuthClient,
       "ciscoLwappWebAuthMIBConform": ciscoLwappWebAuthMIBConform,
       "ciscoLwappWebAuthMIBCompliances": ciscoLwappWebAuthMIBCompliances,
       "cLWebAuthMIBCompliance": cLWebAuthMIBCompliance,
       "cLWebAuthMIBComplianceRev1": cLWebAuthMIBComplianceRev1,
       "cLWebAuthMIBComplianceRev2": cLWebAuthMIBComplianceRev2,
       "ciscoLwappWebAuthMIBGroups": ciscoLwappWebAuthMIBGroups,
       "cLWACustomWebAuthGroup": cLWACustomWebAuthGroup,
       "cLWAExternalWebAuthGroup": cLWAExternalWebAuthGroup,
       "cLWAGuestAccessNotifObjGroup": cLWAGuestAccessNotifObjGroup,
       "cLWAGuestAccessNotifGroup": cLWAGuestAccessNotifGroup,
       "cLWAGuestUserConfigGroup": cLWAGuestUserConfigGroup,
       "cLWAProxyRedirectGroup": cLWAProxyRedirectGroup,
       "cLWAGuestUserStatusGroup": cLWAGuestUserStatusGroup,
       "cLWALocalNetUserGroup": cLWALocalNetUserGroup,
       "cLWAGuestAccessNotifGroupSup01": cLWAGuestAccessNotifGroupSup01,
       "cLWAWebAuthGroup": cLWAWebAuthGroup,
       "cLWACustomWebAuthGroupRev1": cLWACustomWebAuthGroupRev1,
       "cLWAPortalStatsGroup": cLWAPortalStatsGroup}
)
