# SNMP MIB module (CISCO-LWAPP-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-SYS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cldcClientAccessVLAN,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientAccessVLAN")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618)
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIB.setRevisions(
        ("2018-07-03 00:00",
         "2018-04-24 00:00",
         "2017-05-03 00:00",
         "2012-06-18 00:00",
         "2010-02-09 00:00",
         "2007-10-17 00:00",
         "2007-03-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappSysMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBNotifs = _CiscoLwappSysMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0)
)
_CiscoLwappSysMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBObjects = _CiscoLwappSysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1)
)
_ClsConfig_ObjectIdentity = ObjectIdentity
clsConfig = _ClsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1)
)


class _ClsDot3BridgeEnabled_Type(TruthValue):
    """Custom type clsDot3BridgeEnabled based on TruthValue"""
    defaultValue = 2


_ClsDot3BridgeEnabled_Type.__name__ = "TruthValue"
_ClsDot3BridgeEnabled_Object = MibScalar
clsDot3BridgeEnabled = _ClsDot3BridgeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 1),
    _ClsDot3BridgeEnabled_Type()
)
clsDot3BridgeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsDot3BridgeEnabled.setStatus("current")
_ClsConfigDownload_ObjectIdentity = ObjectIdentity
clsConfigDownload = _ClsConfigDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 2)
)


class _ClsDownloadFileType_Type(Integer32):
    """Custom type clsDownloadFileType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("code", 2),
          ("config", 3),
          ("webAuthCert", 4),
          ("webAdminCert", 5),
          ("signatures", 6),
          ("customWebAuth", 7),
          ("vendorDeviceCert", 8),
          ("vendorCaCert", 9),
          ("ipsecDeviceCert", 10),
          ("ipsecCaCert", 11),
          ("radiusavplist", 12),
          ("icon", 13),
          ("apimage", 14),
          ("naservcacert", 15),
          ("webhookcacert", 16))
    )


_ClsDownloadFileType_Type.__name__ = "Integer32"
_ClsDownloadFileType_Object = MibScalar
clsDownloadFileType = _ClsDownloadFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 2, 1),
    _ClsDownloadFileType_Type()
)
clsDownloadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsDownloadFileType.setStatus("current")


class _ClsDownloadCertificateKey_Type(SnmpAdminString):
    """Custom type clsDownloadCertificateKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClsDownloadCertificateKey_Type.__name__ = "SnmpAdminString"
_ClsDownloadCertificateKey_Object = MibScalar
clsDownloadCertificateKey = _ClsDownloadCertificateKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 2, 2),
    _ClsDownloadCertificateKey_Type()
)
clsDownloadCertificateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsDownloadCertificateKey.setStatus("current")
_ClsConfigUpload_ObjectIdentity = ObjectIdentity
clsConfigUpload = _ClsConfigUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3)
)


class _ClsUploadFileType_Type(Integer32):
    """Custom type clsUploadFileType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("config", 2),
          ("errorLog", 3),
          ("systemTrace", 4),
          ("trapLog", 5),
          ("crashFile", 6),
          ("signatures", 7),
          ("pac", 8),
          ("radioCoreDump", 9),
          ("invalidConfig", 10),
          ("debugfile", 11),
          ("pktCapture", 12),
          ("watchdogCrash", 13),
          ("panicCrash", 14),
          ("vendorDevCert", 15),
          ("vendorCaCert", 16),
          ("webAdminCert", 17),
          ("webAuthCert", 18),
          ("ipsecDeviceCert", 19),
          ("ipsecCaCert", 20),
          ("radiusavplist", 21),
          ("yangBundle", 22))
    )


_ClsUploadFileType_Type.__name__ = "Integer32"
_ClsUploadFileType_Object = MibScalar
clsUploadFileType = _ClsUploadFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 1),
    _ClsUploadFileType_Type()
)
clsUploadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadFileType.setStatus("current")


class _ClsUploadPacUsername_Type(SnmpAdminString):
    """Custom type clsUploadPacUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ClsUploadPacUsername_Type.__name__ = "SnmpAdminString"
_ClsUploadPacUsername_Object = MibScalar
clsUploadPacUsername = _ClsUploadPacUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 2),
    _ClsUploadPacUsername_Type()
)
clsUploadPacUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadPacUsername.setStatus("current")


class _ClsUploadPacPassword_Type(SnmpAdminString):
    """Custom type clsUploadPacPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClsUploadPacPassword_Type.__name__ = "SnmpAdminString"
_ClsUploadPacPassword_Object = MibScalar
clsUploadPacPassword = _ClsUploadPacPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 3),
    _ClsUploadPacPassword_Type()
)
clsUploadPacPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadPacPassword.setStatus("current")


class _ClsUploadPacValidity_Type(Unsigned32):
    """Custom type clsUploadPacValidity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClsUploadPacValidity_Type.__name__ = "Unsigned32"
_ClsUploadPacValidity_Object = MibScalar
clsUploadPacValidity = _ClsUploadPacValidity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 4),
    _ClsUploadPacValidity_Type()
)
clsUploadPacValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadPacValidity.setStatus("current")
if mibBuilder.loadTexts:
    clsUploadPacValidity.setUnits("days")
_ClsTransferConfigGroup_ObjectIdentity = ObjectIdentity
clsTransferConfigGroup = _ClsTransferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 4)
)


class _ClsTransferConfigFileEncryption_Type(Integer32):
    """Custom type clsTransferConfigFileEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ClsTransferConfigFileEncryption_Type.__name__ = "Integer32"
_ClsTransferConfigFileEncryption_Object = MibScalar
clsTransferConfigFileEncryption = _ClsTransferConfigFileEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 4, 1),
    _ClsTransferConfigFileEncryption_Type()
)
clsTransferConfigFileEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferConfigFileEncryption.setStatus("current")


class _ClsTransferConfigFileEncryptionKey_Type(SnmpAdminString):
    """Custom type clsTransferConfigFileEncryptionKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClsTransferConfigFileEncryptionKey_Type.__name__ = "SnmpAdminString"
_ClsTransferConfigFileEncryptionKey_Object = MibScalar
clsTransferConfigFileEncryptionKey = _ClsTransferConfigFileEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 4, 2),
    _ClsTransferConfigFileEncryptionKey_Type()
)
clsTransferConfigFileEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferConfigFileEncryptionKey.setStatus("current")
_ClsConfigGeneral_ObjectIdentity = ObjectIdentity
clsConfigGeneral = _ClsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5)
)
_ClsTimeZone_Type = Unsigned32
_ClsTimeZone_Object = MibScalar
clsTimeZone = _ClsTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 1),
    _ClsTimeZone_Type()
)
clsTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTimeZone.setStatus("current")
_ClsTimeZoneDescription_Type = SnmpAdminString
_ClsTimeZoneDescription_Object = MibScalar
clsTimeZoneDescription = _ClsTimeZoneDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 2),
    _ClsTimeZoneDescription_Type()
)
clsTimeZoneDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTimeZoneDescription.setStatus("current")
_ClsMaxClientsTrapThreshold_Type = Unsigned32
_ClsMaxClientsTrapThreshold_Object = MibScalar
clsMaxClientsTrapThreshold = _ClsMaxClientsTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 3),
    _ClsMaxClientsTrapThreshold_Type()
)
clsMaxClientsTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxClientsTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsMaxClientsTrapThreshold.setUnits("Percent")
_ClsMaxRFIDTagsTrapThreshold_Type = Unsigned32
_ClsMaxRFIDTagsTrapThreshold_Object = MibScalar
clsMaxRFIDTagsTrapThreshold = _ClsMaxRFIDTagsTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 4),
    _ClsMaxRFIDTagsTrapThreshold_Type()
)
clsMaxRFIDTagsTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsTrapThreshold.setUnits("Percent")
_ClsConfigNetworkGeneral_ObjectIdentity = ObjectIdentity
clsConfigNetworkGeneral = _ClsConfigNetworkGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5)
)
_ClsNetworkRouteConfigTable_Object = MibTable
clsNetworkRouteConfigTable = _ClsNetworkRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    clsNetworkRouteConfigTable.setStatus("current")
_ClsNetworkRouteConfigEntry_Object = MibTableRow
clsNetworkRouteConfigEntry = _ClsNetworkRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1)
)
clsNetworkRouteConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsNetworkRouteIPAddressType"),
    (0, "CISCO-LWAPP-SYS-MIB", "clsNetworkRouteIPAddress"),
)
if mibBuilder.loadTexts:
    clsNetworkRouteConfigEntry.setStatus("current")
_ClsNetworkRouteIPAddressType_Type = InetAddressType
_ClsNetworkRouteIPAddressType_Object = MibTableColumn
clsNetworkRouteIPAddressType = _ClsNetworkRouteIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1, 1),
    _ClsNetworkRouteIPAddressType_Type()
)
clsNetworkRouteIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsNetworkRouteIPAddressType.setStatus("current")
_ClsNetworkRouteIPAddress_Type = InetAddress
_ClsNetworkRouteIPAddress_Object = MibTableColumn
clsNetworkRouteIPAddress = _ClsNetworkRouteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1, 2),
    _ClsNetworkRouteIPAddress_Type()
)
clsNetworkRouteIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsNetworkRouteIPAddress.setStatus("current")


class _ClsNetworkRoutePrefixLength_Type(Unsigned32):
    """Custom type clsNetworkRoutePrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ClsNetworkRoutePrefixLength_Type.__name__ = "Unsigned32"
_ClsNetworkRoutePrefixLength_Object = MibTableColumn
clsNetworkRoutePrefixLength = _ClsNetworkRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1, 3),
    _ClsNetworkRoutePrefixLength_Type()
)
clsNetworkRoutePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsNetworkRoutePrefixLength.setStatus("current")
_ClsNetworkRouteGatewayType_Type = InetAddressType
_ClsNetworkRouteGatewayType_Object = MibTableColumn
clsNetworkRouteGatewayType = _ClsNetworkRouteGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1, 4),
    _ClsNetworkRouteGatewayType_Type()
)
clsNetworkRouteGatewayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsNetworkRouteGatewayType.setStatus("current")
_ClsNetworkRouteGateway_Type = InetAddress
_ClsNetworkRouteGateway_Object = MibTableColumn
clsNetworkRouteGateway = _ClsNetworkRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1, 5),
    _ClsNetworkRouteGateway_Type()
)
clsNetworkRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsNetworkRouteGateway.setStatus("current")
_ClsNetworkRouteStatus_Type = RowStatus
_ClsNetworkRouteStatus_Object = MibTableColumn
clsNetworkRouteStatus = _ClsNetworkRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 5, 1, 1, 6),
    _ClsNetworkRouteStatus_Type()
)
clsNetworkRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsNetworkRouteStatus.setStatus("current")


class _ClsSensorTemperature_Type(SnmpAdminString):
    """Custom type clsSensorTemperature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClsSensorTemperature_Type.__name__ = "SnmpAdminString"
_ClsSensorTemperature_Object = MibScalar
clsSensorTemperature = _ClsSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 6),
    _ClsSensorTemperature_Type()
)
clsSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSensorTemperature.setStatus("current")
if mibBuilder.loadTexts:
    clsSensorTemperature.setUnits("Centigrade")
_ClsLiConfigGeneral_ObjectIdentity = ObjectIdentity
clsLiConfigGeneral = _ClsLiConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 7)
)


class _ClsLiStatus_Type(TruthValue):
    """Custom type clsLiStatus based on TruthValue"""
    defaultValue = 2


_ClsLiStatus_Type.__name__ = "TruthValue"
_ClsLiStatus_Object = MibScalar
clsLiStatus = _ClsLiStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 7, 1),
    _ClsLiStatus_Type()
)
clsLiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLiStatus.setStatus("current")


class _ClsLiReportingInterval_Type(TimeInterval):
    """Custom type clsLiReportingInterval based on TimeInterval"""
    defaultValue = 60


_ClsLiReportingInterval_Type.__name__ = "TimeInterval"
_ClsLiReportingInterval_Object = MibScalar
clsLiReportingInterval = _ClsLiReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 7, 2),
    _ClsLiReportingInterval_Type()
)
clsLiReportingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLiReportingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsLiReportingInterval.setUnits("seconds")
_ClsLiAddressType_Type = InetAddressType
_ClsLiAddressType_Object = MibScalar
clsLiAddressType = _ClsLiAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 7, 3),
    _ClsLiAddressType_Type()
)
clsLiAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLiAddressType.setStatus("current")
_ClsLiAddress_Type = InetAddress
_ClsLiAddress_Object = MibScalar
clsLiAddress = _ClsLiAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 7, 4),
    _ClsLiAddress_Type()
)
clsLiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLiAddress.setStatus("current")
_ClsSyslogIpConfig_ObjectIdentity = ObjectIdentity
clsSyslogIpConfig = _ClsSyslogIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6)
)
_CLSysLogConfigTable_Object = MibTable
cLSysLogConfigTable = _CLSysLogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLSysLogConfigTable.setStatus("current")
_CLSysLogConfigEntry_Object = MibTableRow
cLSysLogConfigEntry = _CLSysLogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1)
)
cLSysLogConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "cLSysLogServerIndex"),
)
if mibBuilder.loadTexts:
    cLSysLogConfigEntry.setStatus("current")
_CLSysLogServerIndex_Type = Unsigned32
_CLSysLogServerIndex_Object = MibTableColumn
cLSysLogServerIndex = _CLSysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 1),
    _CLSysLogServerIndex_Type()
)
cLSysLogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSysLogServerIndex.setStatus("current")
_CLSysLogAddressType_Type = InetAddressType
_CLSysLogAddressType_Object = MibTableColumn
cLSysLogAddressType = _CLSysLogAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 2),
    _CLSysLogAddressType_Type()
)
cLSysLogAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSysLogAddressType.setStatus("current")
_CLSysLogAddress_Type = InetAddress
_CLSysLogAddress_Object = MibTableColumn
cLSysLogAddress = _CLSysLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 3),
    _CLSysLogAddress_Type()
)
cLSysLogAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSysLogAddress.setStatus("current")
_CLSysLogHostRowStatus_Type = RowStatus
_CLSysLogHostRowStatus_Object = MibTableColumn
cLSysLogHostRowStatus = _CLSysLogHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 4),
    _CLSysLogHostRowStatus_Type()
)
cLSysLogHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSysLogHostRowStatus.setStatus("current")


class _CLSysArpUnicastEnabled_Type(TruthValue):
    """Custom type cLSysArpUnicastEnabled based on TruthValue"""
    defaultValue = 2


_CLSysArpUnicastEnabled_Type.__name__ = "TruthValue"
_CLSysArpUnicastEnabled_Object = MibScalar
cLSysArpUnicastEnabled = _CLSysArpUnicastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 7),
    _CLSysArpUnicastEnabled_Type()
)
cLSysArpUnicastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysArpUnicastEnabled.setStatus("current")
_ClsTransferConfig_ObjectIdentity = ObjectIdentity
clsTransferConfig = _ClsTransferConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8)
)
_ClsTransferConfigTable_Object = MibTable
clsTransferConfigTable = _ClsTransferConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    clsTransferConfigTable.setStatus("current")
_ClsTransferConfigEntry_Object = MibTableRow
clsTransferConfigEntry = _ClsTransferConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1)
)
clsTransferConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsTransferType"),
    (0, "CISCO-LWAPP-SYS-MIB", "clsTransferMode"),
)
if mibBuilder.loadTexts:
    clsTransferConfigEntry.setStatus("current")


class _ClsTransferType_Type(Integer32):
    """Custom type clsTransferType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_ClsTransferType_Type.__name__ = "Integer32"
_ClsTransferType_Object = MibTableColumn
clsTransferType = _ClsTransferType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 1),
    _ClsTransferType_Type()
)
clsTransferType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsTransferType.setStatus("current")


class _ClsTransferMode_Type(Integer32):
    """Custom type clsTransferMode based on Integer32"""
    defaultValue = 1

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
        *(("tftp", 1),
          ("ftp", 2),
          ("sftp", 3),
          ("usb", 4))
    )


_ClsTransferMode_Type.__name__ = "Integer32"
_ClsTransferMode_Object = MibTableColumn
clsTransferMode = _ClsTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 2),
    _ClsTransferMode_Type()
)
clsTransferMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsTransferMode.setStatus("current")
_ClsTransferServerAddressType_Type = InetAddressType
_ClsTransferServerAddressType_Object = MibTableColumn
clsTransferServerAddressType = _ClsTransferServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 3),
    _ClsTransferServerAddressType_Type()
)
clsTransferServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferServerAddressType.setStatus("current")
_ClsTransferServerAddress_Type = InetAddress
_ClsTransferServerAddress_Object = MibTableColumn
clsTransferServerAddress = _ClsTransferServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 4),
    _ClsTransferServerAddress_Type()
)
clsTransferServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferServerAddress.setStatus("current")


class _ClsTransferPath_Type(SnmpAdminString):
    """Custom type clsTransferPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferPath_Type.__name__ = "SnmpAdminString"
_ClsTransferPath_Object = MibTableColumn
clsTransferPath = _ClsTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 5),
    _ClsTransferPath_Type()
)
clsTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferPath.setStatus("current")


class _ClsTransferFilename_Type(SnmpAdminString):
    """Custom type clsTransferFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferFilename_Type.__name__ = "SnmpAdminString"
_ClsTransferFilename_Object = MibTableColumn
clsTransferFilename = _ClsTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 6),
    _ClsTransferFilename_Type()
)
clsTransferFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFilename.setStatus("current")


class _ClsTransferFtpUsername_Type(SnmpAdminString):
    """Custom type clsTransferFtpUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClsTransferFtpUsername_Type.__name__ = "SnmpAdminString"
_ClsTransferFtpUsername_Object = MibTableColumn
clsTransferFtpUsername = _ClsTransferFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 7),
    _ClsTransferFtpUsername_Type()
)
clsTransferFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFtpUsername.setStatus("current")


class _ClsTransferFtpPassword_Type(SnmpAdminString):
    """Custom type clsTransferFtpPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClsTransferFtpPassword_Type.__name__ = "SnmpAdminString"
_ClsTransferFtpPassword_Object = MibTableColumn
clsTransferFtpPassword = _ClsTransferFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 8),
    _ClsTransferFtpPassword_Type()
)
clsTransferFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFtpPassword.setStatus("current")
_ClsTransferFtpPortNum_Type = InetPortNumber
_ClsTransferFtpPortNum_Object = MibTableColumn
clsTransferFtpPortNum = _ClsTransferFtpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 9),
    _ClsTransferFtpPortNum_Type()
)
clsTransferFtpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFtpPortNum.setStatus("current")


class _ClsTransferTftpMaxRetries_Type(Unsigned32):
    """Custom type clsTransferTftpMaxRetries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ClsTransferTftpMaxRetries_Type.__name__ = "Unsigned32"
_ClsTransferTftpMaxRetries_Object = MibTableColumn
clsTransferTftpMaxRetries = _ClsTransferTftpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 10),
    _ClsTransferTftpMaxRetries_Type()
)
clsTransferTftpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferTftpMaxRetries.setStatus("current")


class _ClsTransferTftpTimeout_Type(Unsigned32):
    """Custom type clsTransferTftpTimeout based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ClsTransferTftpTimeout_Type.__name__ = "Unsigned32"
_ClsTransferTftpTimeout_Object = MibTableColumn
clsTransferTftpTimeout = _ClsTransferTftpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 11),
    _ClsTransferTftpTimeout_Type()
)
clsTransferTftpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferTftpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    clsTransferTftpTimeout.setUnits("seconds")


class _ClsTransferStart_Type(Integer32):
    """Custom type clsTransferStart based on Integer32"""
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
        *(("none", 1),
          ("initiate", 2),
          ("initiatePeer", 3))
    )


_ClsTransferStart_Type.__name__ = "Integer32"
_ClsTransferStart_Object = MibTableColumn
clsTransferStart = _ClsTransferStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 12),
    _ClsTransferStart_Type()
)
clsTransferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStart.setStatus("current")


class _ClsTransferStatus_Type(Integer32):
    """Custom type clsTransferStatus based on Integer32"""
    defaultValue = 1

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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notInitiated", 2),
          ("transferStarting", 3),
          ("errorStarting", 4),
          ("wrongFileType", 5),
          ("updatingConfig", 6),
          ("invalidConfigFile", 7),
          ("writingToFlash", 8),
          ("failureWritingToFlash", 9),
          ("checkingCRC", 10),
          ("failedCRC", 11),
          ("unknownDirection", 12),
          ("transferSuccessful", 13),
          ("transferFailed", 14),
          ("bootBreakOff", 15),
          ("invalidTarFile", 16))
    )


_ClsTransferStatus_Type.__name__ = "Integer32"
_ClsTransferStatus_Object = MibTableColumn
clsTransferStatus = _ClsTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 13),
    _ClsTransferStatus_Type()
)
clsTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferStatus.setStatus("current")


class _ClsTransferStatusString_Type(SnmpAdminString):
    """Custom type clsTransferStatusString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClsTransferStatusString_Type.__name__ = "SnmpAdminString"
_ClsTransferStatusString_Object = MibTableColumn
clsTransferStatusString = _ClsTransferStatusString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 14),
    _ClsTransferStatusString_Type()
)
clsTransferStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferStatusString.setStatus("current")
_ClsStreamingTransferConfig_ObjectIdentity = ObjectIdentity
clsStreamingTransferConfig = _ClsStreamingTransferConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2)
)
_ClsApTransferTable_Object = MibTable
clsApTransferTable = _ClsApTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    clsApTransferTable.setStatus("current")
_ClsApTransferEntry_Object = MibTableRow
clsApTransferEntry = _ClsApTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1)
)
clsApTransferEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsApTransferSysMacAddress"),
)
if mibBuilder.loadTexts:
    clsApTransferEntry.setStatus("current")
_ClsApTransferSysMacAddress_Type = MacAddress
_ClsApTransferSysMacAddress_Object = MibTableColumn
clsApTransferSysMacAddress = _ClsApTransferSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 1),
    _ClsApTransferSysMacAddress_Type()
)
clsApTransferSysMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsApTransferSysMacAddress.setStatus("current")


class _ClsApPrimaryVers_Type(SnmpAdminString):
    """Custom type clsApPrimaryVers based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsApPrimaryVers_Type.__name__ = "SnmpAdminString"
_ClsApPrimaryVers_Object = MibTableColumn
clsApPrimaryVers = _ClsApPrimaryVers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 2),
    _ClsApPrimaryVers_Type()
)
clsApPrimaryVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApPrimaryVers.setStatus("current")


class _ClsApBackupVers_Type(SnmpAdminString):
    """Custom type clsApBackupVers based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsApBackupVers_Type.__name__ = "SnmpAdminString"
_ClsApBackupVers_Object = MibTableColumn
clsApBackupVers = _ClsApBackupVers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 3),
    _ClsApBackupVers_Type()
)
clsApBackupVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApBackupVers.setStatus("current")


class _ClsApPredStatus_Type(SnmpAdminString):
    """Custom type clsApPredStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsApPredStatus_Type.__name__ = "SnmpAdminString"
_ClsApPredStatus_Object = MibTableColumn
clsApPredStatus = _ClsApPredStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 4),
    _ClsApPredStatus_Type()
)
clsApPredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApPredStatus.setStatus("current")


class _ClsApPredFailReason_Type(SnmpAdminString):
    """Custom type clsApPredFailReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsApPredFailReason_Type.__name__ = "SnmpAdminString"
_ClsApPredFailReason_Object = MibTableColumn
clsApPredFailReason = _ClsApPredFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 5),
    _ClsApPredFailReason_Type()
)
clsApPredFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApPredFailReason.setStatus("current")


class _ClsApPredRetryCount_Type(Unsigned32):
    """Custom type clsApPredRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ClsApPredRetryCount_Type.__name__ = "Unsigned32"
_ClsApPredRetryCount_Object = MibTableColumn
clsApPredRetryCount = _ClsApPredRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 6),
    _ClsApPredRetryCount_Type()
)
clsApPredRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApPredRetryCount.setStatus("current")


class _ClsApPredNextRetryTime_Type(SnmpAdminString):
    """Custom type clsApPredNextRetryTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsApPredNextRetryTime_Type.__name__ = "SnmpAdminString"
_ClsApPredNextRetryTime_Object = MibTableColumn
clsApPredNextRetryTime = _ClsApPredNextRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 1, 1, 7),
    _ClsApPredNextRetryTime_Type()
)
clsApPredNextRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApPredNextRetryTime.setStatus("current")


class _ClsTransferStreamingMode_Type(Integer32):
    """Custom type clsTransferStreamingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("http", 2),
          ("cco", 3),
          ("https", 4),
          ("sftp", 5))
    )


_ClsTransferStreamingMode_Type.__name__ = "Integer32"
_ClsTransferStreamingMode_Object = MibScalar
clsTransferStreamingMode = _ClsTransferStreamingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 2),
    _ClsTransferStreamingMode_Type()
)
clsTransferStreamingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingMode.setStatus("current")


class _ClsTransferStreamingServerAddressType_Type(InetAddressType):
    """Custom type clsTransferStreamingServerAddressType based on InetAddressType"""
    defaultValue = 1


_ClsTransferStreamingServerAddressType_Type.__name__ = "InetAddressType"
_ClsTransferStreamingServerAddressType_Object = MibScalar
clsTransferStreamingServerAddressType = _ClsTransferStreamingServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 3),
    _ClsTransferStreamingServerAddressType_Type()
)
clsTransferStreamingServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingServerAddressType.setStatus("current")
_ClsTransferStreamingServerAddress_Type = InetAddress
_ClsTransferStreamingServerAddress_Object = MibScalar
clsTransferStreamingServerAddress = _ClsTransferStreamingServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 4),
    _ClsTransferStreamingServerAddress_Type()
)
clsTransferStreamingServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingServerAddress.setStatus("current")


class _ClsTransferStreamingPath_Type(SnmpAdminString):
    """Custom type clsTransferStreamingPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferStreamingPath_Type.__name__ = "SnmpAdminString"
_ClsTransferStreamingPath_Object = MibScalar
clsTransferStreamingPath = _ClsTransferStreamingPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 5),
    _ClsTransferStreamingPath_Type()
)
clsTransferStreamingPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingPath.setStatus("current")


class _ClsStreamingTransferStart_Type(Integer32):
    """Custom type clsStreamingTransferStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("none", 2))
    )


_ClsStreamingTransferStart_Type.__name__ = "Integer32"
_ClsStreamingTransferStart_Object = MibScalar
clsStreamingTransferStart = _ClsStreamingTransferStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 6),
    _ClsStreamingTransferStart_Type()
)
clsStreamingTransferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsStreamingTransferStart.setStatus("current")


class _ClsTransferHttpStreamingUsername_Type(SnmpAdminString):
    """Custom type clsTransferHttpStreamingUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferHttpStreamingUsername_Type.__name__ = "SnmpAdminString"
_ClsTransferHttpStreamingUsername_Object = MibScalar
clsTransferHttpStreamingUsername = _ClsTransferHttpStreamingUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 7),
    _ClsTransferHttpStreamingUsername_Type()
)
clsTransferHttpStreamingUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferHttpStreamingUsername.setStatus("current")


class _ClsTransferHttpStreamingPassword_Type(SnmpAdminString):
    """Custom type clsTransferHttpStreamingPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferHttpStreamingPassword_Type.__name__ = "SnmpAdminString"
_ClsTransferHttpStreamingPassword_Object = MibScalar
clsTransferHttpStreamingPassword = _ClsTransferHttpStreamingPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 8),
    _ClsTransferHttpStreamingPassword_Type()
)
clsTransferHttpStreamingPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferHttpStreamingPassword.setStatus("current")


class _ClsTransferHttpStreamingSuggestedVersion_Type(SnmpAdminString):
    """Custom type clsTransferHttpStreamingSuggestedVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferHttpStreamingSuggestedVersion_Type.__name__ = "SnmpAdminString"
_ClsTransferHttpStreamingSuggestedVersion_Object = MibScalar
clsTransferHttpStreamingSuggestedVersion = _ClsTransferHttpStreamingSuggestedVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 9),
    _ClsTransferHttpStreamingSuggestedVersion_Type()
)
clsTransferHttpStreamingSuggestedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferHttpStreamingSuggestedVersion.setStatus("current")


class _ClsTransferHttpStreamingLatestVersion_Type(SnmpAdminString):
    """Custom type clsTransferHttpStreamingLatestVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferHttpStreamingLatestVersion_Type.__name__ = "SnmpAdminString"
_ClsTransferHttpStreamingLatestVersion_Object = MibScalar
clsTransferHttpStreamingLatestVersion = _ClsTransferHttpStreamingLatestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 10),
    _ClsTransferHttpStreamingLatestVersion_Type()
)
clsTransferHttpStreamingLatestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferHttpStreamingLatestVersion.setStatus("current")


class _ClsTransferHttpStreamingCcoPoll_Type(SnmpAdminString):
    """Custom type clsTransferHttpStreamingCcoPoll based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferHttpStreamingCcoPoll_Type.__name__ = "SnmpAdminString"
_ClsTransferHttpStreamingCcoPoll_Object = MibScalar
clsTransferHttpStreamingCcoPoll = _ClsTransferHttpStreamingCcoPoll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 11),
    _ClsTransferHttpStreamingCcoPoll_Type()
)
clsTransferHttpStreamingCcoPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferHttpStreamingCcoPoll.setStatus("current")
_ClsTransferStreamingServerPort_Type = Integer32
_ClsTransferStreamingServerPort_Object = MibScalar
clsTransferStreamingServerPort = _ClsTransferStreamingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 12),
    _ClsTransferStreamingServerPort_Type()
)
clsTransferStreamingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingServerPort.setStatus("current")


class _ClsTransferStreamingUsername_Type(SnmpAdminString):
    """Custom type clsTransferStreamingUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferStreamingUsername_Type.__name__ = "SnmpAdminString"
_ClsTransferStreamingUsername_Object = MibScalar
clsTransferStreamingUsername = _ClsTransferStreamingUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 13),
    _ClsTransferStreamingUsername_Type()
)
clsTransferStreamingUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingUsername.setStatus("current")


class _ClsTransferStreamingPassword_Type(SnmpAdminString):
    """Custom type clsTransferStreamingPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferStreamingPassword_Type.__name__ = "SnmpAdminString"
_ClsTransferStreamingPassword_Object = MibScalar
clsTransferStreamingPassword = _ClsTransferStreamingPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 14),
    _ClsTransferStreamingPassword_Type()
)
clsTransferStreamingPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingPassword.setStatus("current")
_ClsTransferStreamingOptimizedJoinEnable_Type = TruthValue
_ClsTransferStreamingOptimizedJoinEnable_Object = MibScalar
clsTransferStreamingOptimizedJoinEnable = _ClsTransferStreamingOptimizedJoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 2, 15),
    _ClsTransferStreamingOptimizedJoinEnable_Type()
)
clsTransferStreamingOptimizedJoinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStreamingOptimizedJoinEnable.setStatus("current")


class _CLSysBroadcastForwardingEnabled_Type(TruthValue):
    """Custom type cLSysBroadcastForwardingEnabled based on TruthValue"""
    defaultValue = 2


_CLSysBroadcastForwardingEnabled_Type.__name__ = "TruthValue"
_CLSysBroadcastForwardingEnabled_Object = MibScalar
cLSysBroadcastForwardingEnabled = _CLSysBroadcastForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 9),
    _CLSysBroadcastForwardingEnabled_Type()
)
cLSysBroadcastForwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysBroadcastForwardingEnabled.setStatus("current")


class _CLSysLagModeEnabled_Type(TruthValue):
    """Custom type cLSysLagModeEnabled based on TruthValue"""
    defaultValue = 2


_CLSysLagModeEnabled_Type.__name__ = "TruthValue"
_CLSysLagModeEnabled_Object = MibScalar
cLSysLagModeEnabled = _CLSysLagModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 10),
    _CLSysLagModeEnabled_Type()
)
cLSysLagModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysLagModeEnabled.setStatus("current")


class _ClsConfigProductBranchVersion_Type(SnmpAdminString):
    """Custom type clsConfigProductBranchVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ClsConfigProductBranchVersion_Type.__name__ = "SnmpAdminString"
_ClsConfigProductBranchVersion_Object = MibScalar
clsConfigProductBranchVersion = _ClsConfigProductBranchVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 11),
    _ClsConfigProductBranchVersion_Type()
)
clsConfigProductBranchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsConfigProductBranchVersion.setStatus("current")


class _ClsConfigDhcpProxyEnabled_Type(TruthValue):
    """Custom type clsConfigDhcpProxyEnabled based on TruthValue"""
    defaultValue = 2


_ClsConfigDhcpProxyEnabled_Type.__name__ = "TruthValue"
_ClsConfigDhcpProxyEnabled_Object = MibScalar
clsConfigDhcpProxyEnabled = _ClsConfigDhcpProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 12),
    _ClsConfigDhcpProxyEnabled_Type()
)
clsConfigDhcpProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigDhcpProxyEnabled.setStatus("current")
_CLSysMulticastIGMP_ObjectIdentity = ObjectIdentity
cLSysMulticastIGMP = _CLSysMulticastIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13)
)


class _CLSysMulticastIGMPSnoopingEnabled_Type(TruthValue):
    """Custom type cLSysMulticastIGMPSnoopingEnabled based on TruthValue"""
    defaultValue = 2


_CLSysMulticastIGMPSnoopingEnabled_Type.__name__ = "TruthValue"
_CLSysMulticastIGMPSnoopingEnabled_Object = MibScalar
cLSysMulticastIGMPSnoopingEnabled = _CLSysMulticastIGMPSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 1),
    _CLSysMulticastIGMPSnoopingEnabled_Type()
)
cLSysMulticastIGMPSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPSnoopingEnabled.setStatus("current")
_CLSysMulticastIGMPSnoopingTimeout_Type = Unsigned32
_CLSysMulticastIGMPSnoopingTimeout_Object = MibScalar
cLSysMulticastIGMPSnoopingTimeout = _CLSysMulticastIGMPSnoopingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 2),
    _CLSysMulticastIGMPSnoopingTimeout_Type()
)
cLSysMulticastIGMPSnoopingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPSnoopingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPSnoopingTimeout.setUnits("Seconds")
_CLSysMulticastIGMPQueryInterval_Type = Unsigned32
_CLSysMulticastIGMPQueryInterval_Object = MibScalar
cLSysMulticastIGMPQueryInterval = _CLSysMulticastIGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 3),
    _CLSysMulticastIGMPQueryInterval_Type()
)
cLSysMulticastIGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPQueryInterval.setUnits("Seconds")


class _CLSysMulticastLLBridgingStatus_Type(TruthValue):
    """Custom type cLSysMulticastLLBridgingStatus based on TruthValue"""
    defaultValue = 2


_CLSysMulticastLLBridgingStatus_Type.__name__ = "TruthValue"
_CLSysMulticastLLBridgingStatus_Object = MibScalar
cLSysMulticastLLBridgingStatus = _CLSysMulticastLLBridgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 4),
    _CLSysMulticastLLBridgingStatus_Type()
)
cLSysMulticastLLBridgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastLLBridgingStatus.setStatus("current")
_CLSPortModeConfig_ObjectIdentity = ObjectIdentity
cLSPortModeConfig = _CLSPortModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14)
)
_ClsPortModeConfigTable_Object = MibTable
clsPortModeConfigTable = _ClsPortModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    clsPortModeConfigTable.setStatus("current")
_ClsPortModeConfigEntry_Object = MibTableRow
clsPortModeConfigEntry = _ClsPortModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1)
)
clsPortModeConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    clsPortModeConfigEntry.setStatus("current")


class _ClsPortDot1dBasePort_Type(Unsigned32):
    """Custom type clsPortDot1dBasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClsPortDot1dBasePort_Type.__name__ = "Unsigned32"
_ClsPortDot1dBasePort_Object = MibTableColumn
clsPortDot1dBasePort = _ClsPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 1),
    _ClsPortDot1dBasePort_Type()
)
clsPortDot1dBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsPortDot1dBasePort.setStatus("current")


class _ClsPortModePhysicalMode_Type(Integer32):
    """Custom type clsPortModePhysicalMode based on Integer32"""
    defaultValue = 1

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("half10", 2),
          ("full10", 3),
          ("half100", 4),
          ("full100", 5),
          ("full1000sx", 6),
          ("half1000", 7),
          ("full1000", 8),
          ("half10000", 9),
          ("full10000", 10))
    )


_ClsPortModePhysicalMode_Type.__name__ = "Integer32"
_ClsPortModePhysicalMode_Object = MibTableColumn
clsPortModePhysicalMode = _ClsPortModePhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 2),
    _ClsPortModePhysicalMode_Type()
)
clsPortModePhysicalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsPortModePhysicalMode.setStatus("current")


class _ClsPortModePhysicalStatus_Type(Integer32):
    """Custom type clsPortModePhysicalStatus based on Integer32"""
    defaultValue = 1

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("autonegotiate", 2),
          ("half10", 3),
          ("full10", 4),
          ("half100", 5),
          ("full100", 6),
          ("full1000sx", 7),
          ("half1000", 8),
          ("full1000", 9),
          ("half10000", 10),
          ("full10000", 11),
          ("half2500", 12),
          ("full2500", 13),
          ("half5000", 14),
          ("full5000", 15))
    )


_ClsPortModePhysicalStatus_Type.__name__ = "Integer32"
_ClsPortModePhysicalStatus_Object = MibTableColumn
clsPortModePhysicalStatus = _ClsPortModePhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 3),
    _ClsPortModePhysicalStatus_Type()
)
clsPortModePhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortModePhysicalStatus.setStatus("current")
_ClsPortModeSfpType_Type = SnmpAdminString
_ClsPortModeSfpType_Object = MibTableColumn
clsPortModeSfpType = _ClsPortModeSfpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 4),
    _ClsPortModeSfpType_Type()
)
clsPortModeSfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortModeSfpType.setStatus("current")
_ClsPortUpDownCount_Type = Counter32
_ClsPortUpDownCount_Object = MibTableColumn
clsPortUpDownCount = _ClsPortUpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 5),
    _ClsPortUpDownCount_Type()
)
clsPortUpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortUpDownCount.setStatus("current")


class _ClsPortModeMaxSpeed_Type(Integer32):
    """Custom type clsPortModeMaxSpeed based on Integer32"""
    defaultValue = 1

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
        *(("autonegotiate", 1),
          ("full1000", 2),
          ("full2500", 3),
          ("full5000", 4))
    )


_ClsPortModeMaxSpeed_Type.__name__ = "Integer32"
_ClsPortModeMaxSpeed_Object = MibTableColumn
clsPortModeMaxSpeed = _ClsPortModeMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 6),
    _ClsPortModeMaxSpeed_Type()
)
clsPortModeMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsPortModeMaxSpeed.setStatus("current")
_ClsCoreDump_ObjectIdentity = ObjectIdentity
clsCoreDump = _ClsCoreDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15)
)


class _ClsCoreDumpTransferEnable_Type(TruthValue):
    """Custom type clsCoreDumpTransferEnable based on TruthValue"""
    defaultValue = 2


_ClsCoreDumpTransferEnable_Type.__name__ = "TruthValue"
_ClsCoreDumpTransferEnable_Object = MibScalar
clsCoreDumpTransferEnable = _ClsCoreDumpTransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 1),
    _ClsCoreDumpTransferEnable_Type()
)
clsCoreDumpTransferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpTransferEnable.setStatus("current")


class _ClsCoreDumpTransferMode_Type(Integer32):
    """Custom type clsCoreDumpTransferMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ftp", 2))
    )


_ClsCoreDumpTransferMode_Type.__name__ = "Integer32"
_ClsCoreDumpTransferMode_Object = MibScalar
clsCoreDumpTransferMode = _ClsCoreDumpTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 2),
    _ClsCoreDumpTransferMode_Type()
)
clsCoreDumpTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpTransferMode.setStatus("current")
_ClsCoreDumpServerIPAddressType_Type = InetAddressType
_ClsCoreDumpServerIPAddressType_Object = MibScalar
clsCoreDumpServerIPAddressType = _ClsCoreDumpServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 3),
    _ClsCoreDumpServerIPAddressType_Type()
)
clsCoreDumpServerIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpServerIPAddressType.setStatus("current")
_ClsCoreDumpServerIPAddress_Type = InetAddress
_ClsCoreDumpServerIPAddress_Object = MibScalar
clsCoreDumpServerIPAddress = _ClsCoreDumpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 4),
    _ClsCoreDumpServerIPAddress_Type()
)
clsCoreDumpServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpServerIPAddress.setStatus("current")
_ClsCoreDumpFileName_Type = SnmpAdminString
_ClsCoreDumpFileName_Object = MibScalar
clsCoreDumpFileName = _ClsCoreDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 5),
    _ClsCoreDumpFileName_Type()
)
clsCoreDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpFileName.setStatus("current")
_ClsCoreDumpUserName_Type = SnmpAdminString
_ClsCoreDumpUserName_Object = MibScalar
clsCoreDumpUserName = _ClsCoreDumpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 6),
    _ClsCoreDumpUserName_Type()
)
clsCoreDumpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpUserName.setStatus("current")
_ClsCoreDumpPassword_Type = SnmpAdminString
_ClsCoreDumpPassword_Object = MibScalar
clsCoreDumpPassword = _ClsCoreDumpPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 7),
    _ClsCoreDumpPassword_Type()
)
clsCoreDumpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpPassword.setStatus("current")


class _ClsConfigMulticastEnabled_Type(TruthValue):
    """Custom type clsConfigMulticastEnabled based on TruthValue"""
    defaultValue = 2


_ClsConfigMulticastEnabled_Type.__name__ = "TruthValue"
_ClsConfigMulticastEnabled_Object = MibScalar
clsConfigMulticastEnabled = _ClsConfigMulticastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 16),
    _ClsConfigMulticastEnabled_Type()
)
clsConfigMulticastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigMulticastEnabled.setStatus("current")
_CLSysMulticastMLD_ObjectIdentity = ObjectIdentity
cLSysMulticastMLD = _CLSysMulticastMLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17)
)


class _CLSysMulticastMLDSnoopingEnabled_Type(TruthValue):
    """Custom type cLSysMulticastMLDSnoopingEnabled based on TruthValue"""
    defaultValue = 2


_CLSysMulticastMLDSnoopingEnabled_Type.__name__ = "TruthValue"
_CLSysMulticastMLDSnoopingEnabled_Object = MibScalar
cLSysMulticastMLDSnoopingEnabled = _CLSysMulticastMLDSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17, 1),
    _CLSysMulticastMLDSnoopingEnabled_Type()
)
cLSysMulticastMLDSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastMLDSnoopingEnabled.setStatus("current")


class _CLSysMulticastMLDSnoopingTimeout_Type(Unsigned32):
    """Custom type cLSysMulticastMLDSnoopingTimeout based on Unsigned32"""
    defaultValue = 60


_CLSysMulticastMLDSnoopingTimeout_Type.__name__ = "Unsigned32"
_CLSysMulticastMLDSnoopingTimeout_Object = MibScalar
cLSysMulticastMLDSnoopingTimeout = _CLSysMulticastMLDSnoopingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17, 2),
    _CLSysMulticastMLDSnoopingTimeout_Type()
)
cLSysMulticastMLDSnoopingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastMLDSnoopingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastMLDSnoopingTimeout.setUnits("Seconds")


class _CLSysMulticastMLDQueryInterval_Type(Unsigned32):
    """Custom type cLSysMulticastMLDQueryInterval based on Unsigned32"""
    defaultValue = 20


_CLSysMulticastMLDQueryInterval_Type.__name__ = "Unsigned32"
_CLSysMulticastMLDQueryInterval_Object = MibScalar
cLSysMulticastMLDQueryInterval = _CLSysMulticastMLDQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17, 3),
    _CLSysMulticastMLDQueryInterval_Type()
)
cLSysMulticastMLDQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastMLDQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastMLDQueryInterval.setUnits("Seconds")
_ClsConfigStats_ObjectIdentity = ObjectIdentity
clsConfigStats = _ClsConfigStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18)
)


class _ClsSysRealtimeStatsTimer_Type(Unsigned32):
    """Custom type clsSysRealtimeStatsTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ClsSysRealtimeStatsTimer_Type.__name__ = "Unsigned32"
_ClsSysRealtimeStatsTimer_Object = MibScalar
clsSysRealtimeStatsTimer = _ClsSysRealtimeStatsTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 1),
    _ClsSysRealtimeStatsTimer_Type()
)
clsSysRealtimeStatsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysRealtimeStatsTimer.setStatus("current")
if mibBuilder.loadTexts:
    clsSysRealtimeStatsTimer.setUnits("Seconds")


class _ClsSysNormalStatsTimer_Type(Unsigned32):
    """Custom type clsSysNormalStatsTimer based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_ClsSysNormalStatsTimer_Type.__name__ = "Unsigned32"
_ClsSysNormalStatsTimer_Object = MibScalar
clsSysNormalStatsTimer = _ClsSysNormalStatsTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 2),
    _ClsSysNormalStatsTimer_Type()
)
clsSysNormalStatsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysNormalStatsTimer.setStatus("current")
if mibBuilder.loadTexts:
    clsSysNormalStatsTimer.setUnits("Seconds")
_ClsSysStatsSamplingInterval_Type = Unsigned32
_ClsSysStatsSamplingInterval_Object = MibScalar
clsSysStatsSamplingInterval = _ClsSysStatsSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 3),
    _ClsSysStatsSamplingInterval_Type()
)
clsSysStatsSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysStatsSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysStatsSamplingInterval.setUnits("Seconds")
_ClsSysStatsAverageInterval_Type = Unsigned32
_ClsSysStatsAverageInterval_Object = MibScalar
clsSysStatsAverageInterval = _ClsSysStatsAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 4),
    _ClsSysStatsAverageInterval_Type()
)
clsSysStatsAverageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysStatsAverageInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysStatsAverageInterval.setUnits("Seconds")
_ClsAlarmObjects_ObjectIdentity = ObjectIdentity
clsAlarmObjects = _ClsAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 19)
)


class _ClsAlarmHoldTime_Type(Unsigned32):
    """Custom type clsAlarmHoldTime based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ClsAlarmHoldTime_Type.__name__ = "Unsigned32"
_ClsAlarmHoldTime_Object = MibScalar
clsAlarmHoldTime = _ClsAlarmHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 19, 1),
    _ClsAlarmHoldTime_Type()
)
clsAlarmHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsAlarmHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    clsAlarmHoldTime.setUnits("second")


class _ClsAlarmTrapRetransmitInterval_Type(Unsigned32):
    """Custom type clsAlarmTrapRetransmitInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClsAlarmTrapRetransmitInterval_Type.__name__ = "Unsigned32"
_ClsAlarmTrapRetransmitInterval_Object = MibScalar
clsAlarmTrapRetransmitInterval = _ClsAlarmTrapRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 19, 2),
    _ClsAlarmTrapRetransmitInterval_Type()
)
clsAlarmTrapRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsAlarmTrapRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsAlarmTrapRetransmitInterval.setUnits("second")
_ClsSysThresholdConfig_ObjectIdentity = ObjectIdentity
clsSysThresholdConfig = _ClsSysThresholdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20)
)


class _ClsSysControllerCpuUsageThreshold_Type(Unsigned32):
    """Custom type clsSysControllerCpuUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysControllerCpuUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysControllerCpuUsageThreshold_Object = MibScalar
clsSysControllerCpuUsageThreshold = _ClsSysControllerCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 1),
    _ClsSysControllerCpuUsageThreshold_Type()
)
clsSysControllerCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysControllerCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysControllerCpuUsageThreshold.setUnits("Percent")


class _ClsSysControllerMemoryUsageThreshold_Type(Unsigned32):
    """Custom type clsSysControllerMemoryUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysControllerMemoryUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysControllerMemoryUsageThreshold_Object = MibScalar
clsSysControllerMemoryUsageThreshold = _ClsSysControllerMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 2),
    _ClsSysControllerMemoryUsageThreshold_Type()
)
clsSysControllerMemoryUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysControllerMemoryUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysControllerMemoryUsageThreshold.setUnits("Percent")


class _ClsSysApCpuUsageThreshold_Type(Unsigned32):
    """Custom type clsSysApCpuUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysApCpuUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysApCpuUsageThreshold_Object = MibScalar
clsSysApCpuUsageThreshold = _ClsSysApCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 3),
    _ClsSysApCpuUsageThreshold_Type()
)
clsSysApCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysApCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysApCpuUsageThreshold.setUnits("Percent")


class _ClsSysApMemoryUsageThreshold_Type(Unsigned32):
    """Custom type clsSysApMemoryUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysApMemoryUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysApMemoryUsageThreshold_Object = MibScalar
clsSysApMemoryUsageThreshold = _ClsSysApMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 4),
    _ClsSysApMemoryUsageThreshold_Type()
)
clsSysApMemoryUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysApMemoryUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysApMemoryUsageThreshold.setUnits("Percent")
_ClsNMHeartBeat_ObjectIdentity = ObjectIdentity
clsNMHeartBeat = _ClsNMHeartBeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 21)
)


class _ClsNMHeartBeatEnable_Type(TruthValue):
    """Custom type clsNMHeartBeatEnable based on TruthValue"""
    defaultValue = 2


_ClsNMHeartBeatEnable_Type.__name__ = "TruthValue"
_ClsNMHeartBeatEnable_Object = MibScalar
clsNMHeartBeatEnable = _ClsNMHeartBeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 21, 1),
    _ClsNMHeartBeatEnable_Type()
)
clsNMHeartBeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNMHeartBeatEnable.setStatus("current")


class _ClsNMHeartBeatInterval_Type(Unsigned32):
    """Custom type clsNMHeartBeatInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClsNMHeartBeatInterval_Type.__name__ = "Unsigned32"
_ClsNMHeartBeatInterval_Object = MibScalar
clsNMHeartBeatInterval = _ClsNMHeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 21, 2),
    _ClsNMHeartBeatInterval_Type()
)
clsNMHeartBeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNMHeartBeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsNMHeartBeatInterval.setUnits("Seconds")


class _ClsSysLogEnabled_Type(TruthValue):
    """Custom type clsSysLogEnabled based on TruthValue"""
    defaultValue = 2


_ClsSysLogEnabled_Type.__name__ = "TruthValue"
_ClsSysLogEnabled_Object = MibScalar
clsSysLogEnabled = _ClsSysLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 22),
    _ClsSysLogEnabled_Type()
)
clsSysLogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysLogEnabled.setStatus("current")


class _ClsSysLogLevel_Type(Integer32):
    """Custom type clsSysLogLevel based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergencies", 1),
          ("alerts", 2),
          ("critical", 3),
          ("errors", 4),
          ("warnings", 5),
          ("notifications", 6),
          ("informational", 7),
          ("debugging", 8))
    )


_ClsSysLogLevel_Type.__name__ = "Integer32"
_ClsSysLogLevel_Object = MibScalar
clsSysLogLevel = _ClsSysLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 23),
    _ClsSysLogLevel_Type()
)
clsSysLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysLogLevel.setStatus("current")


class _ClsConfigApMaxCount_Type(Unsigned32):
    """Custom type clsConfigApMaxCount based on Unsigned32"""
    defaultValue = 0


_ClsConfigApMaxCount_Type.__name__ = "Unsigned32"
_ClsConfigApMaxCount_Object = MibScalar
clsConfigApMaxCount = _ClsConfigApMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 24),
    _ClsConfigApMaxCount_Type()
)
clsConfigApMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsConfigApMaxCount.setStatus("deprecated")
_CLSTrapSwitchConfig_ObjectIdentity = ObjectIdentity
cLSTrapSwitchConfig = _CLSTrapSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 25)
)
_ClsTrapBlacklistTable_Object = MibTable
clsTrapBlacklistTable = _ClsTrapBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 25, 1)
)
if mibBuilder.loadTexts:
    clsTrapBlacklistTable.setStatus("current")
_ClsTrapBlacklistEntry_Object = MibTableRow
clsTrapBlacklistEntry = _ClsTrapBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 25, 1, 1)
)
clsTrapBlacklistEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsBlacklistTrapIndex"),
)
if mibBuilder.loadTexts:
    clsTrapBlacklistEntry.setStatus("current")
_ClsBlacklistTrapIndex_Type = Unsigned32
_ClsBlacklistTrapIndex_Object = MibTableColumn
clsBlacklistTrapIndex = _ClsBlacklistTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 25, 1, 1, 1),
    _ClsBlacklistTrapIndex_Type()
)
clsBlacklistTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsBlacklistTrapIndex.setStatus("current")
_ClsTrapNameInBlacklist_Type = SnmpAdminString
_ClsTrapNameInBlacklist_Object = MibTableColumn
clsTrapNameInBlacklist = _ClsTrapNameInBlacklist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 25, 1, 1, 2),
    _ClsTrapNameInBlacklist_Type()
)
clsTrapNameInBlacklist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsTrapNameInBlacklist.setStatus("current")
_ClsTrapBlacklistRowStatus_Type = RowStatus
_ClsTrapBlacklistRowStatus_Object = MibTableColumn
clsTrapBlacklistRowStatus = _ClsTrapBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 25, 1, 1, 3),
    _ClsTrapBlacklistRowStatus_Type()
)
clsTrapBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsTrapBlacklistRowStatus.setStatus("current")
_ClsLinkLocalBridgingEnabled_Type = TruthValue
_ClsLinkLocalBridgingEnabled_Object = MibScalar
clsLinkLocalBridgingEnabled = _ClsLinkLocalBridgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 26),
    _ClsLinkLocalBridgingEnabled_Type()
)
clsLinkLocalBridgingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLinkLocalBridgingEnabled.setStatus("current")


class _ClsNetworkHttpProfCustomPort_Type(Unsigned32):
    """Custom type clsNetworkHttpProfCustomPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClsNetworkHttpProfCustomPort_Type.__name__ = "Unsigned32"
_ClsNetworkHttpProfCustomPort_Object = MibScalar
clsNetworkHttpProfCustomPort = _ClsNetworkHttpProfCustomPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 27),
    _ClsNetworkHttpProfCustomPort_Type()
)
clsNetworkHttpProfCustomPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNetworkHttpProfCustomPort.setStatus("current")
_ClsIconCfgTable_Object = MibTable
clsIconCfgTable = _ClsIconCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28)
)
if mibBuilder.loadTexts:
    clsIconCfgTable.setStatus("current")
_ClsIconCfgEntry_Object = MibTableRow
clsIconCfgEntry = _ClsIconCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1)
)
clsIconCfgEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsIconCfgFileName"),
)
if mibBuilder.loadTexts:
    clsIconCfgEntry.setStatus("current")


class _ClsIconCfgFileName_Type(SnmpAdminString):
    """Custom type clsIconCfgFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClsIconCfgFileName_Type.__name__ = "SnmpAdminString"
_ClsIconCfgFileName_Object = MibTableColumn
clsIconCfgFileName = _ClsIconCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1, 1),
    _ClsIconCfgFileName_Type()
)
clsIconCfgFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsIconCfgFileName.setStatus("current")


class _ClsIconCfgFileType_Type(SnmpAdminString):
    """Custom type clsIconCfgFileType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClsIconCfgFileType_Type.__name__ = "SnmpAdminString"
_ClsIconCfgFileType_Object = MibTableColumn
clsIconCfgFileType = _ClsIconCfgFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1, 2),
    _ClsIconCfgFileType_Type()
)
clsIconCfgFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsIconCfgFileType.setStatus("current")


class _ClsIconCfgLangCode_Type(SnmpAdminString):
    """Custom type clsIconCfgLangCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_ClsIconCfgLangCode_Type.__name__ = "SnmpAdminString"
_ClsIconCfgLangCode_Object = MibTableColumn
clsIconCfgLangCode = _ClsIconCfgLangCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1, 3),
    _ClsIconCfgLangCode_Type()
)
clsIconCfgLangCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsIconCfgLangCode.setStatus("current")


class _ClsIconCfgWidth_Type(Unsigned32):
    """Custom type clsIconCfgWidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClsIconCfgWidth_Type.__name__ = "Unsigned32"
_ClsIconCfgWidth_Object = MibTableColumn
clsIconCfgWidth = _ClsIconCfgWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1, 4),
    _ClsIconCfgWidth_Type()
)
clsIconCfgWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsIconCfgWidth.setStatus("current")


class _ClsIconCfgHeight_Type(Unsigned32):
    """Custom type clsIconCfgHeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClsIconCfgHeight_Type.__name__ = "Unsigned32"
_ClsIconCfgHeight_Object = MibTableColumn
clsIconCfgHeight = _ClsIconCfgHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1, 5),
    _ClsIconCfgHeight_Type()
)
clsIconCfgHeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsIconCfgHeight.setStatus("current")
_ClsIconCfgRowStatus_Type = RowStatus
_ClsIconCfgRowStatus_Object = MibTableColumn
clsIconCfgRowStatus = _ClsIconCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 28, 1, 6),
    _ClsIconCfgRowStatus_Type()
)
clsIconCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsIconCfgRowStatus.setStatus("current")


class _ClsNetworkHttpProxyPort_Type(Unsigned32):
    """Custom type clsNetworkHttpProxyPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClsNetworkHttpProxyPort_Type.__name__ = "Unsigned32"
_ClsNetworkHttpProxyPort_Object = MibScalar
clsNetworkHttpProxyPort = _ClsNetworkHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 29),
    _ClsNetworkHttpProxyPort_Type()
)
clsNetworkHttpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNetworkHttpProxyPort.setStatus("current")


class _ClsNetworkHttpProxyIpType_Type(InetAddressType):
    """Custom type clsNetworkHttpProxyIpType based on InetAddressType"""
    defaultValue = 0


_ClsNetworkHttpProxyIpType_Type.__name__ = "InetAddressType"
_ClsNetworkHttpProxyIpType_Object = MibScalar
clsNetworkHttpProxyIpType = _ClsNetworkHttpProxyIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 30),
    _ClsNetworkHttpProxyIpType_Type()
)
clsNetworkHttpProxyIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNetworkHttpProxyIpType.setStatus("current")
_ClsNetworkHttpProxyIp_Type = InetAddress
_ClsNetworkHttpProxyIp_Object = MibScalar
clsNetworkHttpProxyIp = _ClsNetworkHttpProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 31),
    _ClsNetworkHttpProxyIp_Type()
)
clsNetworkHttpProxyIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNetworkHttpProxyIp.setStatus("current")


class _ClsNetworkDnsServerIpType_Type(InetAddressType):
    """Custom type clsNetworkDnsServerIpType based on InetAddressType"""
    defaultValue = 0


_ClsNetworkDnsServerIpType_Type.__name__ = "InetAddressType"
_ClsNetworkDnsServerIpType_Object = MibScalar
clsNetworkDnsServerIpType = _ClsNetworkDnsServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 32),
    _ClsNetworkDnsServerIpType_Type()
)
clsNetworkDnsServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNetworkDnsServerIpType.setStatus("current")
_ClsNetworkDnsServerIp_Type = InetAddress
_ClsNetworkDnsServerIp_Object = MibScalar
clsNetworkDnsServerIp = _ClsNetworkDnsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 33),
    _ClsNetworkDnsServerIp_Type()
)
clsNetworkDnsServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNetworkDnsServerIp.setStatus("current")
_ClsConfigCalea_ObjectIdentity = ObjectIdentity
clsConfigCalea = _ClsConfigCalea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34)
)


class _ClsConfigCaleaEnabled_Type(TruthValue):
    """Custom type clsConfigCaleaEnabled based on TruthValue"""
    defaultValue = 2


_ClsConfigCaleaEnabled_Type.__name__ = "TruthValue"
_ClsConfigCaleaEnabled_Object = MibScalar
clsConfigCaleaEnabled = _ClsConfigCaleaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 1),
    _ClsConfigCaleaEnabled_Type()
)
clsConfigCaleaEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaEnabled.setStatus("current")
_ClsConfigCaleaServerIp_Type = IpAddress
_ClsConfigCaleaServerIp_Object = MibScalar
clsConfigCaleaServerIp = _ClsConfigCaleaServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 2),
    _ClsConfigCaleaServerIp_Type()
)
clsConfigCaleaServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaServerIp.setStatus("deprecated")


class _ClsConfigCaleaPort_Type(InetPortNumber):
    """Custom type clsConfigCaleaPort based on InetPortNumber"""
    defaultValue = 0


_ClsConfigCaleaPort_Type.__name__ = "InetPortNumber"
_ClsConfigCaleaPort_Object = MibScalar
clsConfigCaleaPort = _ClsConfigCaleaPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 3),
    _ClsConfigCaleaPort_Type()
)
clsConfigCaleaPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaPort.setStatus("current")


class _ClsConfigCaleaAccountingInterval_Type(Unsigned32):
    """Custom type clsConfigCaleaAccountingInterval based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ClsConfigCaleaAccountingInterval_Type.__name__ = "Unsigned32"
_ClsConfigCaleaAccountingInterval_Object = MibScalar
clsConfigCaleaAccountingInterval = _ClsConfigCaleaAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 4),
    _ClsConfigCaleaAccountingInterval_Type()
)
clsConfigCaleaAccountingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaAccountingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsConfigCaleaAccountingInterval.setUnits("Minutes")


class _ClsConfigCaleaVenue_Type(SnmpAdminString):
    """Custom type clsConfigCaleaVenue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ClsConfigCaleaVenue_Type.__name__ = "SnmpAdminString"
_ClsConfigCaleaVenue_Object = MibScalar
clsConfigCaleaVenue = _ClsConfigCaleaVenue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 5),
    _ClsConfigCaleaVenue_Type()
)
clsConfigCaleaVenue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaVenue.setStatus("current")


class _ClsConfigCaleaServerIpType_Type(InetAddressType):
    """Custom type clsConfigCaleaServerIpType based on InetAddressType"""
    defaultValue = 1


_ClsConfigCaleaServerIpType_Type.__name__ = "InetAddressType"
_ClsConfigCaleaServerIpType_Object = MibScalar
clsConfigCaleaServerIpType = _ClsConfigCaleaServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 6),
    _ClsConfigCaleaServerIpType_Type()
)
clsConfigCaleaServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaServerIpType.setStatus("current")
_ClsConfigCaleaServerIpAddr_Type = IpAddress
_ClsConfigCaleaServerIpAddr_Object = MibScalar
clsConfigCaleaServerIpAddr = _ClsConfigCaleaServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 34, 7),
    _ClsConfigCaleaServerIpAddr_Type()
)
clsConfigCaleaServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigCaleaServerIpAddr.setStatus("current")


class _ClSysLogIPSecStatus_Type(TruthValue):
    """Custom type clSysLogIPSecStatus based on TruthValue"""
    defaultValue = 2


_ClSysLogIPSecStatus_Type.__name__ = "TruthValue"
_ClSysLogIPSecStatus_Object = MibScalar
clSysLogIPSecStatus = _ClSysLogIPSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 35),
    _ClSysLogIPSecStatus_Type()
)
clSysLogIPSecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clSysLogIPSecStatus.setStatus("current")


class _ClSysLogIPSecProfName_Type(SnmpAdminString):
    """Custom type clSysLogIPSecProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ClSysLogIPSecProfName_Type.__name__ = "SnmpAdminString"
_ClSysLogIPSecProfName_Object = MibScalar
clSysLogIPSecProfName = _ClSysLogIPSecProfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 36),
    _ClSysLogIPSecProfName_Type()
)
clSysLogIPSecProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clSysLogIPSecProfName.setStatus("current")


class _ClsConfigArpUnicastEnabled_Type(TruthValue):
    """Custom type clsConfigArpUnicastEnabled based on TruthValue"""
    defaultValue = 2


_ClsConfigArpUnicastEnabled_Type.__name__ = "TruthValue"
_ClsConfigArpUnicastEnabled_Object = MibScalar
clsConfigArpUnicastEnabled = _ClsConfigArpUnicastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 37),
    _ClsConfigArpUnicastEnabled_Type()
)
clsConfigArpUnicastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigArpUnicastEnabled.setStatus("current")


class _ClsWGBForcedL2RoamEnabled_Type(TruthValue):
    """Custom type clsWGBForcedL2RoamEnabled based on TruthValue"""
    defaultValue = 2


_ClsWGBForcedL2RoamEnabled_Type.__name__ = "TruthValue"
_ClsWGBForcedL2RoamEnabled_Object = MibScalar
clsWGBForcedL2RoamEnabled = _ClsWGBForcedL2RoamEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 38),
    _ClsWGBForcedL2RoamEnabled_Type()
)
clsWGBForcedL2RoamEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsWGBForcedL2RoamEnabled.setStatus("current")


class _ClsUSBMode_Type(TruthValue):
    """Custom type clsUSBMode based on TruthValue"""
    defaultValue = 1


_ClsUSBMode_Type.__name__ = "TruthValue"
_ClsUSBMode_Object = MibScalar
clsUSBMode = _ClsUSBMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 40),
    _ClsUSBMode_Type()
)
clsUSBMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUSBMode.setStatus("current")


class _ClsCrashSystem_Type(TruthValue):
    """Custom type clsCrashSystem based on TruthValue"""
    defaultValue = 2


_ClsCrashSystem_Type.__name__ = "TruthValue"
_ClsCrashSystem_Object = MibScalar
clsCrashSystem = _ClsCrashSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 99),
    _ClsCrashSystem_Type()
)
clsCrashSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCrashSystem.setStatus("current")
_ClsStatus_ObjectIdentity = ObjectIdentity
clsStatus = _ClsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2)
)


class _CLSysLagModeInTransition_Type(TruthValue):
    """Custom type cLSysLagModeInTransition based on TruthValue"""
    defaultValue = 2


_CLSysLagModeInTransition_Type.__name__ = "TruthValue"
_CLSysLagModeInTransition_Object = MibScalar
cLSysLagModeInTransition = _CLSysLagModeInTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 1),
    _CLSysLagModeInTransition_Type()
)
cLSysLagModeInTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSysLagModeInTransition.setStatus("current")
_ClsRAIDStatusTable_Object = MibTable
clsRAIDStatusTable = _ClsRAIDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 2)
)
if mibBuilder.loadTexts:
    clsRAIDStatusTable.setStatus("current")
_ClsRAIDStatusEntry_Object = MibTableRow
clsRAIDStatusEntry = _ClsRAIDStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 2, 1)
)
clsRAIDStatusEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsRAIDDriveNumber"),
)
if mibBuilder.loadTexts:
    clsRAIDStatusEntry.setStatus("current")
_ClsRAIDDriveNumber_Type = Unsigned32
_ClsRAIDDriveNumber_Object = MibTableColumn
clsRAIDDriveNumber = _ClsRAIDDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 2, 1, 1),
    _ClsRAIDDriveNumber_Type()
)
clsRAIDDriveNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsRAIDDriveNumber.setStatus("current")


class _ClsRAIDStatus_Type(Integer32):
    """Custom type clsRAIDStatus based on Integer32"""
    defaultValue = 1

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
        *(("good", 1),
          ("bad", 2),
          ("badstartrebuild", 3),
          ("rebuilding", 4))
    )


_ClsRAIDStatus_Type.__name__ = "Integer32"
_ClsRAIDStatus_Object = MibTableColumn
clsRAIDStatus = _ClsRAIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 2, 1, 2),
    _ClsRAIDStatus_Type()
)
clsRAIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsRAIDStatus.setStatus("current")
_ClsRAIDRebuildPercentage_Type = Unsigned32
_ClsRAIDRebuildPercentage_Object = MibTableColumn
clsRAIDRebuildPercentage = _ClsRAIDRebuildPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 2, 1, 3),
    _ClsRAIDRebuildPercentage_Type()
)
clsRAIDRebuildPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsRAIDRebuildPercentage.setStatus("current")
if mibBuilder.loadTexts:
    clsRAIDRebuildPercentage.setUnits("Percent")
_ClsSysPingTestTable_Object = MibTable
clsSysPingTestTable = _ClsSysPingTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3)
)
if mibBuilder.loadTexts:
    clsSysPingTestTable.setStatus("current")
_ClsSysPingTestEntry_Object = MibTableRow
clsSysPingTestEntry = _ClsSysPingTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1)
)
clsSysPingTestEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsSysPingTestId"),
)
if mibBuilder.loadTexts:
    clsSysPingTestEntry.setStatus("current")
_ClsSysPingTestId_Type = Integer32
_ClsSysPingTestId_Object = MibTableColumn
clsSysPingTestId = _ClsSysPingTestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 1),
    _ClsSysPingTestId_Type()
)
clsSysPingTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsSysPingTestId.setStatus("current")
_ClsSysPingTestIPAddressType_Type = InetAddressType
_ClsSysPingTestIPAddressType_Object = MibTableColumn
clsSysPingTestIPAddressType = _ClsSysPingTestIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 2),
    _ClsSysPingTestIPAddressType_Type()
)
clsSysPingTestIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsSysPingTestIPAddressType.setStatus("current")
_ClsSysPingTestIPAddress_Type = InetAddress
_ClsSysPingTestIPAddress_Object = MibTableColumn
clsSysPingTestIPAddress = _ClsSysPingTestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 3),
    _ClsSysPingTestIPAddress_Type()
)
clsSysPingTestIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsSysPingTestIPAddress.setStatus("current")


class _ClsSysPingTestSendCount_Type(Integer32):
    """Custom type clsSysPingTestSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClsSysPingTestSendCount_Type.__name__ = "Integer32"
_ClsSysPingTestSendCount_Object = MibTableColumn
clsSysPingTestSendCount = _ClsSysPingTestSendCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 4),
    _ClsSysPingTestSendCount_Type()
)
clsSysPingTestSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsSysPingTestSendCount.setStatus("current")
if mibBuilder.loadTexts:
    clsSysPingTestSendCount.setUnits("Bytes")
_ClsSysPingTestReceivedCount_Type = Integer32
_ClsSysPingTestReceivedCount_Object = MibTableColumn
clsSysPingTestReceivedCount = _ClsSysPingTestReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 5),
    _ClsSysPingTestReceivedCount_Type()
)
clsSysPingTestReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPingTestReceivedCount.setStatus("current")
if mibBuilder.loadTexts:
    clsSysPingTestReceivedCount.setUnits("Bytes")


class _ClsSysPingTestStatus_Type(Integer32):
    """Custom type clsSysPingTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inprogress", 1),
          ("complete", 2))
    )


_ClsSysPingTestStatus_Type.__name__ = "Integer32"
_ClsSysPingTestStatus_Object = MibTableColumn
clsSysPingTestStatus = _ClsSysPingTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 6),
    _ClsSysPingTestStatus_Type()
)
clsSysPingTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPingTestStatus.setStatus("current")
_ClsSysPingTestMaxTimeInterval_Type = Unsigned32
_ClsSysPingTestMaxTimeInterval_Object = MibTableColumn
clsSysPingTestMaxTimeInterval = _ClsSysPingTestMaxTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 7),
    _ClsSysPingTestMaxTimeInterval_Type()
)
clsSysPingTestMaxTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPingTestMaxTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysPingTestMaxTimeInterval.setUnits("mSec")
_ClsSysPingTestMinTimeInterval_Type = Unsigned32
_ClsSysPingTestMinTimeInterval_Object = MibTableColumn
clsSysPingTestMinTimeInterval = _ClsSysPingTestMinTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 8),
    _ClsSysPingTestMinTimeInterval_Type()
)
clsSysPingTestMinTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPingTestMinTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysPingTestMinTimeInterval.setUnits("mSec")
_ClsSysPingTestAvgTimeInterval_Type = Unsigned32
_ClsSysPingTestAvgTimeInterval_Object = MibTableColumn
clsSysPingTestAvgTimeInterval = _ClsSysPingTestAvgTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 9),
    _ClsSysPingTestAvgTimeInterval_Type()
)
clsSysPingTestAvgTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPingTestAvgTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysPingTestAvgTimeInterval.setUnits("mSec")
_ClsSysPingTestRowStatus_Type = RowStatus
_ClsSysPingTestRowStatus_Object = MibTableColumn
clsSysPingTestRowStatus = _ClsSysPingTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 3, 1, 10),
    _ClsSysPingTestRowStatus_Type()
)
clsSysPingTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clsSysPingTestRowStatus.setStatus("current")
_ClsImageInfo_ObjectIdentity = ObjectIdentity
clsImageInfo = _ClsImageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 3)
)
_ClsEmergencyImageVersion_Type = SnmpAdminString
_ClsEmergencyImageVersion_Object = MibScalar
clsEmergencyImageVersion = _ClsEmergencyImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 3, 1),
    _ClsEmergencyImageVersion_Type()
)
clsEmergencyImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsEmergencyImageVersion.setStatus("current")
_ClsCpuInfo_ObjectIdentity = ObjectIdentity
clsCpuInfo = _ClsCpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 4)
)
_ClsAllCpuUsage_Type = SnmpAdminString
_ClsAllCpuUsage_Object = MibScalar
clsAllCpuUsage = _ClsAllCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 4, 1),
    _ClsAllCpuUsage_Type()
)
clsAllCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsAllCpuUsage.setStatus("current")
_ClsSecurityGroup_ObjectIdentity = ObjectIdentity
clsSecurityGroup = _ClsSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5)
)


class _ClsSecStrongPwdCaseCheck_Type(TruthValue):
    """Custom type clsSecStrongPwdCaseCheck based on TruthValue"""
    defaultValue = 2


_ClsSecStrongPwdCaseCheck_Type.__name__ = "TruthValue"
_ClsSecStrongPwdCaseCheck_Object = MibScalar
clsSecStrongPwdCaseCheck = _ClsSecStrongPwdCaseCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 1),
    _ClsSecStrongPwdCaseCheck_Type()
)
clsSecStrongPwdCaseCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdCaseCheck.setStatus("current")


class _ClsSecStrongPwdConsecutiveCheck_Type(TruthValue):
    """Custom type clsSecStrongPwdConsecutiveCheck based on TruthValue"""
    defaultValue = 2


_ClsSecStrongPwdConsecutiveCheck_Type.__name__ = "TruthValue"
_ClsSecStrongPwdConsecutiveCheck_Object = MibScalar
clsSecStrongPwdConsecutiveCheck = _ClsSecStrongPwdConsecutiveCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 2),
    _ClsSecStrongPwdConsecutiveCheck_Type()
)
clsSecStrongPwdConsecutiveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdConsecutiveCheck.setStatus("current")


class _ClsSecStrongPwdDefaultCheck_Type(TruthValue):
    """Custom type clsSecStrongPwdDefaultCheck based on TruthValue"""
    defaultValue = 2


_ClsSecStrongPwdDefaultCheck_Type.__name__ = "TruthValue"
_ClsSecStrongPwdDefaultCheck_Object = MibScalar
clsSecStrongPwdDefaultCheck = _ClsSecStrongPwdDefaultCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 3),
    _ClsSecStrongPwdDefaultCheck_Type()
)
clsSecStrongPwdDefaultCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdDefaultCheck.setStatus("current")


class _ClsSecStrongPwdAsUserNameCheck_Type(TruthValue):
    """Custom type clsSecStrongPwdAsUserNameCheck based on TruthValue"""
    defaultValue = 2


_ClsSecStrongPwdAsUserNameCheck_Type.__name__ = "TruthValue"
_ClsSecStrongPwdAsUserNameCheck_Object = MibScalar
clsSecStrongPwdAsUserNameCheck = _ClsSecStrongPwdAsUserNameCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 4),
    _ClsSecStrongPwdAsUserNameCheck_Type()
)
clsSecStrongPwdAsUserNameCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdAsUserNameCheck.setStatus("current")


class _ClsSecStrongPwdPositionCheck_Type(TruthValue):
    """Custom type clsSecStrongPwdPositionCheck based on TruthValue"""
    defaultValue = 2


_ClsSecStrongPwdPositionCheck_Type.__name__ = "TruthValue"
_ClsSecStrongPwdPositionCheck_Object = MibScalar
clsSecStrongPwdPositionCheck = _ClsSecStrongPwdPositionCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 5),
    _ClsSecStrongPwdPositionCheck_Type()
)
clsSecStrongPwdPositionCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdPositionCheck.setStatus("current")


class _ClsSecStrongPwdDigitCheck_Type(TruthValue):
    """Custom type clsSecStrongPwdDigitCheck based on TruthValue"""
    defaultValue = 2


_ClsSecStrongPwdDigitCheck_Type.__name__ = "TruthValue"
_ClsSecStrongPwdDigitCheck_Object = MibScalar
clsSecStrongPwdDigitCheck = _ClsSecStrongPwdDigitCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 6),
    _ClsSecStrongPwdDigitCheck_Type()
)
clsSecStrongPwdDigitCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdDigitCheck.setStatus("current")
_ClsSecStrongPwdMinLength_Type = Unsigned32
_ClsSecStrongPwdMinLength_Object = MibScalar
clsSecStrongPwdMinLength = _ClsSecStrongPwdMinLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 7),
    _ClsSecStrongPwdMinLength_Type()
)
clsSecStrongPwdMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdMinLength.setStatus("current")
_ClsSecStrongPwdMinUpperCase_Type = Unsigned32
_ClsSecStrongPwdMinUpperCase_Object = MibScalar
clsSecStrongPwdMinUpperCase = _ClsSecStrongPwdMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 8),
    _ClsSecStrongPwdMinUpperCase_Type()
)
clsSecStrongPwdMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdMinUpperCase.setStatus("current")
_ClsSecStrongPwdMinLowerCase_Type = Unsigned32
_ClsSecStrongPwdMinLowerCase_Object = MibScalar
clsSecStrongPwdMinLowerCase = _ClsSecStrongPwdMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 9),
    _ClsSecStrongPwdMinLowerCase_Type()
)
clsSecStrongPwdMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdMinLowerCase.setStatus("current")
_ClsSecStrongPwdMinDigits_Type = Unsigned32
_ClsSecStrongPwdMinDigits_Object = MibScalar
clsSecStrongPwdMinDigits = _ClsSecStrongPwdMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 10),
    _ClsSecStrongPwdMinDigits_Type()
)
clsSecStrongPwdMinDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdMinDigits.setStatus("current")
_ClsSecStrongPwdMinSpecialChar_Type = Unsigned32
_ClsSecStrongPwdMinSpecialChar_Object = MibScalar
clsSecStrongPwdMinSpecialChar = _ClsSecStrongPwdMinSpecialChar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 11),
    _ClsSecStrongPwdMinSpecialChar_Type()
)
clsSecStrongPwdMinSpecialChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdMinSpecialChar.setStatus("current")


class _ClsSecWlanCCEnable_Type(TruthValue):
    """Custom type clsSecWlanCCEnable based on TruthValue"""
    defaultValue = 2


_ClsSecWlanCCEnable_Type.__name__ = "TruthValue"
_ClsSecWlanCCEnable_Object = MibScalar
clsSecWlanCCEnable = _ClsSecWlanCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 12),
    _ClsSecWlanCCEnable_Type()
)
clsSecWlanCCEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSecWlanCCEnable.setStatus("current")


class _ClsSecUcaplEnable_Type(TruthValue):
    """Custom type clsSecUcaplEnable based on TruthValue"""
    defaultValue = 2


_ClsSecUcaplEnable_Type.__name__ = "TruthValue"
_ClsSecUcaplEnable_Object = MibScalar
clsSecUcaplEnable = _ClsSecUcaplEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 13),
    _ClsSecUcaplEnable_Type()
)
clsSecUcaplEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSecUcaplEnable.setStatus("current")


class _ClsSecMgmtUsrLockoutEnable_Type(TruthValue):
    """Custom type clsSecMgmtUsrLockoutEnable based on TruthValue"""
    defaultValue = 2


_ClsSecMgmtUsrLockoutEnable_Type.__name__ = "TruthValue"
_ClsSecMgmtUsrLockoutEnable_Object = MibScalar
clsSecMgmtUsrLockoutEnable = _ClsSecMgmtUsrLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 14),
    _ClsSecMgmtUsrLockoutEnable_Type()
)
clsSecMgmtUsrLockoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecMgmtUsrLockoutEnable.setStatus("current")
_ClsSecMgmtUsrLockoutTime_Type = Unsigned32
_ClsSecMgmtUsrLockoutTime_Object = MibScalar
clsSecMgmtUsrLockoutTime = _ClsSecMgmtUsrLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 15),
    _ClsSecMgmtUsrLockoutTime_Type()
)
clsSecMgmtUsrLockoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecMgmtUsrLockoutTime.setStatus("current")
_ClsSecMgmtUsrLockoutAttempts_Type = Unsigned32
_ClsSecMgmtUsrLockoutAttempts_Object = MibScalar
clsSecMgmtUsrLockoutAttempts = _ClsSecMgmtUsrLockoutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 16),
    _ClsSecMgmtUsrLockoutAttempts_Type()
)
clsSecMgmtUsrLockoutAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecMgmtUsrLockoutAttempts.setStatus("current")


class _ClsSecSnmpv3UsrLockoutEnable_Type(TruthValue):
    """Custom type clsSecSnmpv3UsrLockoutEnable based on TruthValue"""
    defaultValue = 2


_ClsSecSnmpv3UsrLockoutEnable_Type.__name__ = "TruthValue"
_ClsSecSnmpv3UsrLockoutEnable_Object = MibScalar
clsSecSnmpv3UsrLockoutEnable = _ClsSecSnmpv3UsrLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 17),
    _ClsSecSnmpv3UsrLockoutEnable_Type()
)
clsSecSnmpv3UsrLockoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecSnmpv3UsrLockoutEnable.setStatus("current")
_ClsSecSnmpv3UsrLockoutTime_Type = Unsigned32
_ClsSecSnmpv3UsrLockoutTime_Object = MibScalar
clsSecSnmpv3UsrLockoutTime = _ClsSecSnmpv3UsrLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 18),
    _ClsSecSnmpv3UsrLockoutTime_Type()
)
clsSecSnmpv3UsrLockoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecSnmpv3UsrLockoutTime.setStatus("current")
_ClsSecSnmpv3UsrLockoutAttempts_Type = Unsigned32
_ClsSecSnmpv3UsrLockoutAttempts_Object = MibScalar
clsSecSnmpv3UsrLockoutAttempts = _ClsSecSnmpv3UsrLockoutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 19),
    _ClsSecSnmpv3UsrLockoutAttempts_Type()
)
clsSecSnmpv3UsrLockoutAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecSnmpv3UsrLockoutAttempts.setStatus("current")


class _ClsSecMgmtUsrLockoutLifetime_Type(Unsigned32):
    """Custom type clsSecMgmtUsrLockoutLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_ClsSecMgmtUsrLockoutLifetime_Type.__name__ = "Unsigned32"
_ClsSecMgmtUsrLockoutLifetime_Object = MibScalar
clsSecMgmtUsrLockoutLifetime = _ClsSecMgmtUsrLockoutLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 20),
    _ClsSecMgmtUsrLockoutLifetime_Type()
)
clsSecMgmtUsrLockoutLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecMgmtUsrLockoutLifetime.setStatus("current")
if mibBuilder.loadTexts:
    clsSecMgmtUsrLockoutLifetime.setUnits("days")


class _ClsSecSnmpv3UsrLockoutLifetime_Type(Unsigned32):
    """Custom type clsSecSnmpv3UsrLockoutLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_ClsSecSnmpv3UsrLockoutLifetime_Type.__name__ = "Unsigned32"
_ClsSecSnmpv3UsrLockoutLifetime_Object = MibScalar
clsSecSnmpv3UsrLockoutLifetime = _ClsSecSnmpv3UsrLockoutLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 21),
    _ClsSecSnmpv3UsrLockoutLifetime_Type()
)
clsSecSnmpv3UsrLockoutLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecSnmpv3UsrLockoutLifetime.setStatus("current")
if mibBuilder.loadTexts:
    clsSecSnmpv3UsrLockoutLifetime.setUnits("days")
_CiscoLwappSysMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBNotifObjects = _CiscoLwappSysMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6)
)


class _ClsSecStrongPwdManagementUser_Type(SnmpAdminString):
    """Custom type clsSecStrongPwdManagementUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_ClsSecStrongPwdManagementUser_Type.__name__ = "SnmpAdminString"
_ClsSecStrongPwdManagementUser_Object = MibScalar
clsSecStrongPwdManagementUser = _ClsSecStrongPwdManagementUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 1),
    _ClsSecStrongPwdManagementUser_Type()
)
clsSecStrongPwdManagementUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSecStrongPwdManagementUser.setStatus("current")


class _ClsSecStrongPwdCheckType_Type(Integer32):
    """Custom type clsSecStrongPwdCheckType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("caseCheck", 1),
          ("consecutiveCheck", 2),
          ("defaultCheck", 3),
          ("usernameCheck", 4),
          ("allChecks", 5))
    )


_ClsSecStrongPwdCheckType_Type.__name__ = "Integer32"
_ClsSecStrongPwdCheckType_Object = MibScalar
clsSecStrongPwdCheckType = _ClsSecStrongPwdCheckType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 2),
    _ClsSecStrongPwdCheckType_Type()
)
clsSecStrongPwdCheckType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSecStrongPwdCheckType.setStatus("current")
_ClsSecStrongPwdCheckOption_Type = TruthValue
_ClsSecStrongPwdCheckOption_Object = MibScalar
clsSecStrongPwdCheckOption = _ClsSecStrongPwdCheckOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 3),
    _ClsSecStrongPwdCheckOption_Type()
)
clsSecStrongPwdCheckOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSecStrongPwdCheckOption.setStatus("current")
_ClsSysAlarmSet_Type = TruthValue
_ClsSysAlarmSet_Object = MibScalar
clsSysAlarmSet = _ClsSysAlarmSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 4),
    _ClsSysAlarmSet_Type()
)
clsSysAlarmSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsSysAlarmSet.setStatus("current")
_ClsSysMaxThresholdReachedClear_Type = TruthValue
_ClsSysMaxThresholdReachedClear_Object = MibScalar
clsSysMaxThresholdReachedClear = _ClsSysMaxThresholdReachedClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 5),
    _ClsSysMaxThresholdReachedClear_Type()
)
clsSysMaxThresholdReachedClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsSysMaxThresholdReachedClear.setStatus("current")


class _ClsTransferCfgAnalyzeResult_Type(Integer32):
    """Custom type clsTransferCfgAnalyzeResult based on Integer32"""
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
        *(("unknown", 1),
          ("keyMismatch", 2),
          ("fileMissing", 3),
          ("contentMismatch", 4))
    )


_ClsTransferCfgAnalyzeResult_Type.__name__ = "Integer32"
_ClsTransferCfgAnalyzeResult_Object = MibScalar
clsTransferCfgAnalyzeResult = _ClsTransferCfgAnalyzeResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 6),
    _ClsTransferCfgAnalyzeResult_Type()
)
clsTransferCfgAnalyzeResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsTransferCfgAnalyzeResult.setStatus("current")
_ClsWlcSwVersionBeforeUpgrade_Type = SnmpAdminString
_ClsWlcSwVersionBeforeUpgrade_Object = MibScalar
clsWlcSwVersionBeforeUpgrade = _ClsWlcSwVersionBeforeUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 7),
    _ClsWlcSwVersionBeforeUpgrade_Type()
)
clsWlcSwVersionBeforeUpgrade.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsWlcSwVersionBeforeUpgrade.setStatus("current")
_ClsWlcSwVersionAfterUpgrade_Type = SnmpAdminString
_ClsWlcSwVersionAfterUpgrade_Object = MibScalar
clsWlcSwVersionAfterUpgrade = _ClsWlcSwVersionAfterUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 8),
    _ClsWlcSwVersionAfterUpgrade_Type()
)
clsWlcSwVersionAfterUpgrade.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsWlcSwVersionAfterUpgrade.setStatus("current")


class _ClsWlcUpgradeFailReason_Type(Integer32):
    """Custom type clsWlcUpgradeFailReason based on Integer32"""
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
        *(("unknownReason", 1),
          ("fileTypeMismatch", 2),
          ("fileCheckFail", 3),
          ("fileBackupToFlashFail", 4))
    )


_ClsWlcUpgradeFailReason_Type.__name__ = "Integer32"
_ClsWlcUpgradeFailReason_Object = MibScalar
clsWlcUpgradeFailReason = _ClsWlcUpgradeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 9),
    _ClsWlcUpgradeFailReason_Type()
)
clsWlcUpgradeFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsWlcUpgradeFailReason.setStatus("current")
_ClsPortNumber_Type = InetPortNumber
_ClsPortNumber_Object = MibScalar
clsPortNumber = _ClsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 10),
    _ClsPortNumber_Type()
)
clsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortNumber.setStatus("current")
_ClsPortSpeed_Type = Unsigned32
_ClsPortSpeed_Object = MibScalar
clsPortSpeed = _ClsPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 11),
    _ClsPortSpeed_Type()
)
clsPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortSpeed.setStatus("current")
_ClsPortSlot_Type = Unsigned32
_ClsPortSlot_Object = MibScalar
clsPortSlot = _ClsPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 12),
    _ClsPortSlot_Type()
)
clsPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortSlot.setStatus("current")
_CiscoLwappSysMIBNotifControlObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBNotifControlObjects = _CiscoLwappSysMIBNotifControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7)
)


class _ClsSecStrongPwdCheckTrapEnabled_Type(TruthValue):
    """Custom type clsSecStrongPwdCheckTrapEnabled based on TruthValue"""
    defaultValue = 1


_ClsSecStrongPwdCheckTrapEnabled_Type.__name__ = "TruthValue"
_ClsSecStrongPwdCheckTrapEnabled_Object = MibScalar
clsSecStrongPwdCheckTrapEnabled = _ClsSecStrongPwdCheckTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 1),
    _ClsSecStrongPwdCheckTrapEnabled_Type()
)
clsSecStrongPwdCheckTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdCheckTrapEnabled.setStatus("current")


class _ClsMaxClientsTrapEnabled_Type(TruthValue):
    """Custom type clsMaxClientsTrapEnabled based on TruthValue"""
    defaultValue = 1


_ClsMaxClientsTrapEnabled_Type.__name__ = "TruthValue"
_ClsMaxClientsTrapEnabled_Object = MibScalar
clsMaxClientsTrapEnabled = _ClsMaxClientsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 2),
    _ClsMaxClientsTrapEnabled_Type()
)
clsMaxClientsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxClientsTrapEnabled.setStatus("current")


class _ClsMaxRFIDTagsTrapEnabled_Type(TruthValue):
    """Custom type clsMaxRFIDTagsTrapEnabled based on TruthValue"""
    defaultValue = 1


_ClsMaxRFIDTagsTrapEnabled_Type.__name__ = "TruthValue"
_ClsMaxRFIDTagsTrapEnabled_Object = MibScalar
clsMaxRFIDTagsTrapEnabled = _ClsMaxRFIDTagsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 3),
    _ClsMaxRFIDTagsTrapEnabled_Type()
)
clsMaxRFIDTagsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsTrapEnabled.setStatus("current")


class _ClsNacAlertTrapEnabled_Type(TruthValue):
    """Custom type clsNacAlertTrapEnabled based on TruthValue"""
    defaultValue = 1


_ClsNacAlertTrapEnabled_Type.__name__ = "TruthValue"
_ClsNacAlertTrapEnabled_Object = MibScalar
clsNacAlertTrapEnabled = _ClsNacAlertTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 4),
    _ClsNacAlertTrapEnabled_Type()
)
clsNacAlertTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNacAlertTrapEnabled.setStatus("current")


class _ClsMfpTrapEnabled_Type(TruthValue):
    """Custom type clsMfpTrapEnabled based on TruthValue"""
    defaultValue = 1


_ClsMfpTrapEnabled_Type.__name__ = "TruthValue"
_ClsMfpTrapEnabled_Object = MibScalar
clsMfpTrapEnabled = _ClsMfpTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 5),
    _ClsMfpTrapEnabled_Type()
)
clsMfpTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMfpTrapEnabled.setStatus("current")
_ClsSysInfo_ObjectIdentity = ObjectIdentity
clsSysInfo = _ClsSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8)
)
_ClsSysFlashSize_Type = Unsigned32
_ClsSysFlashSize_Object = MibScalar
clsSysFlashSize = _ClsSysFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 1),
    _ClsSysFlashSize_Type()
)
clsSysFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    clsSysFlashSize.setUnits("KBytes")
_ClsSysMemoryType_Type = SnmpAdminString
_ClsSysMemoryType_Object = MibScalar
clsSysMemoryType = _ClsSysMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 2),
    _ClsSysMemoryType_Type()
)
clsSysMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysMemoryType.setStatus("current")
_ClsSysMaxClients_Type = Unsigned32
_ClsSysMaxClients_Object = MibScalar
clsSysMaxClients = _ClsSysMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 3),
    _ClsSysMaxClients_Type()
)
clsSysMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysMaxClients.setStatus("current")
_ClsSysApConnectCount_Type = Unsigned32
_ClsSysApConnectCount_Object = MibScalar
clsSysApConnectCount = _ClsSysApConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 4),
    _ClsSysApConnectCount_Type()
)
clsSysApConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysApConnectCount.setStatus("current")


class _ClsSysNetId_Type(SnmpAdminString):
    """Custom type clsSysNetId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClsSysNetId_Type.__name__ = "SnmpAdminString"
_ClsSysNetId_Object = MibScalar
clsSysNetId = _ClsSysNetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 5),
    _ClsSysNetId_Type()
)
clsSysNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysNetId.setStatus("current")
_ClsSysCurrentMemoryUsage_Type = Unsigned32
_ClsSysCurrentMemoryUsage_Object = MibScalar
clsSysCurrentMemoryUsage = _ClsSysCurrentMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 6),
    _ClsSysCurrentMemoryUsage_Type()
)
clsSysCurrentMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCurrentMemoryUsage.setStatus("current")
_ClsSysAverageMemoryUsage_Type = Unsigned32
_ClsSysAverageMemoryUsage_Object = MibScalar
clsSysAverageMemoryUsage = _ClsSysAverageMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 7),
    _ClsSysAverageMemoryUsage_Type()
)
clsSysAverageMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysAverageMemoryUsage.setStatus("current")
_ClsSysCurrentCpuUsage_Type = Unsigned32
_ClsSysCurrentCpuUsage_Object = MibScalar
clsSysCurrentCpuUsage = _ClsSysCurrentCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 8),
    _ClsSysCurrentCpuUsage_Type()
)
clsSysCurrentCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCurrentCpuUsage.setStatus("current")
_ClsSysAverageCpuUsage_Type = Unsigned32
_ClsSysAverageCpuUsage_Object = MibScalar
clsSysAverageCpuUsage = _ClsSysAverageCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 9),
    _ClsSysAverageCpuUsage_Type()
)
clsSysAverageCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysAverageCpuUsage.setStatus("current")
_ClsSysCpuType_Type = SnmpAdminString
_ClsSysCpuType_Object = MibScalar
clsSysCpuType = _ClsSysCpuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 10),
    _ClsSysCpuType_Type()
)
clsSysCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCpuType.setStatus("current")
_ClsMaxRFIDTagsCount_Type = Unsigned32
_ClsMaxRFIDTagsCount_Object = MibScalar
clsMaxRFIDTagsCount = _ClsMaxRFIDTagsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 11),
    _ClsMaxRFIDTagsCount_Type()
)
clsMaxRFIDTagsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsCount.setStatus("current")
_ClsMaxClientsCount_Type = Unsigned32
_ClsMaxClientsCount_Object = MibScalar
clsMaxClientsCount = _ClsMaxClientsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 12),
    _ClsMaxClientsCount_Type()
)
clsMaxClientsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsMaxClientsCount.setStatus("current")
_ClsApAssocFailedCount_Type = Counter32
_ClsApAssocFailedCount_Object = MibScalar
clsApAssocFailedCount = _ClsApAssocFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 13),
    _ClsApAssocFailedCount_Type()
)
clsApAssocFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsApAssocFailedCount.setStatus("current")
_ClsCurrentPortalClientCount_Type = Unsigned32
_ClsCurrentPortalClientCount_Object = MibScalar
clsCurrentPortalClientCount = _ClsCurrentPortalClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 14),
    _ClsCurrentPortalClientCount_Type()
)
clsCurrentPortalClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsCurrentPortalClientCount.setStatus("current")
_ClsCurrentOnlineUsersCount_Type = Unsigned32
_ClsCurrentOnlineUsersCount_Object = MibScalar
clsCurrentOnlineUsersCount = _ClsCurrentOnlineUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 15),
    _ClsCurrentOnlineUsersCount_Type()
)
clsCurrentOnlineUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsCurrentOnlineUsersCount.setStatus("current")
_ClsSysAbnormalOfflineCount_Type = Unsigned32
_ClsSysAbnormalOfflineCount_Object = MibScalar
clsSysAbnormalOfflineCount = _ClsSysAbnormalOfflineCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 16),
    _ClsSysAbnormalOfflineCount_Type()
)
clsSysAbnormalOfflineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysAbnormalOfflineCount.setStatus("current")
_ClsSysFlashType_Type = SnmpAdminString
_ClsSysFlashType_Object = MibScalar
clsSysFlashType = _ClsSysFlashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 17),
    _ClsSysFlashType_Type()
)
clsSysFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysFlashType.setStatus("current")
_ClsSysOpenUsersCount_Type = Unsigned32
_ClsSysOpenUsersCount_Object = MibScalar
clsSysOpenUsersCount = _ClsSysOpenUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 18),
    _ClsSysOpenUsersCount_Type()
)
clsSysOpenUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysOpenUsersCount.setStatus("current")
_ClsSysWepPskUsersCount_Type = Unsigned32
_ClsSysWepPskUsersCount_Object = MibScalar
clsSysWepPskUsersCount = _ClsSysWepPskUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 19),
    _ClsSysWepPskUsersCount_Type()
)
clsSysWepPskUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysWepPskUsersCount.setStatus("current")
_ClsSysPeapSimUsersCount_Type = Unsigned32
_ClsSysPeapSimUsersCount_Object = MibScalar
clsSysPeapSimUsersCount = _ClsSysPeapSimUsersCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 20),
    _ClsSysPeapSimUsersCount_Type()
)
clsSysPeapSimUsersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPeapSimUsersCount.setStatus("current")
_ClsSysPeapSimReqCount_Type = Counter32
_ClsSysPeapSimReqCount_Object = MibScalar
clsSysPeapSimReqCount = _ClsSysPeapSimReqCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 21),
    _ClsSysPeapSimReqCount_Type()
)
clsSysPeapSimReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPeapSimReqCount.setStatus("current")
_ClsSysPeapSimReqSuccessCount_Type = Counter32
_ClsSysPeapSimReqSuccessCount_Object = MibScalar
clsSysPeapSimReqSuccessCount = _ClsSysPeapSimReqSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 22),
    _ClsSysPeapSimReqSuccessCount_Type()
)
clsSysPeapSimReqSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPeapSimReqSuccessCount.setStatus("current")
_ClsSysPeapSimReqFailureCount_Type = Counter32
_ClsSysPeapSimReqFailureCount_Object = MibScalar
clsSysPeapSimReqFailureCount = _ClsSysPeapSimReqFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 23),
    _ClsSysPeapSimReqFailureCount_Type()
)
clsSysPeapSimReqFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysPeapSimReqFailureCount.setStatus("current")


class _ClsSysNasId_Type(SnmpAdminString):
    """Custom type clsSysNasId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ClsSysNasId_Type.__name__ = "SnmpAdminString"
_ClsSysNasId_Object = MibScalar
clsSysNasId = _ClsSysNasId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 24),
    _ClsSysNasId_Type()
)
clsSysNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysNasId.setStatus("current")
_ClsSysCoChannelTrapRssiThreshold_Type = Integer32
_ClsSysCoChannelTrapRssiThreshold_Object = MibScalar
clsSysCoChannelTrapRssiThreshold = _ClsSysCoChannelTrapRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 25),
    _ClsSysCoChannelTrapRssiThreshold_Type()
)
clsSysCoChannelTrapRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysCoChannelTrapRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysCoChannelTrapRssiThreshold.setUnits("dBm")
_ClsSysAdjChannelTrapRssiThreshold_Type = Integer32
_ClsSysAdjChannelTrapRssiThreshold_Object = MibScalar
clsSysAdjChannelTrapRssiThreshold = _ClsSysAdjChannelTrapRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 26),
    _ClsSysAdjChannelTrapRssiThreshold_Type()
)
clsSysAdjChannelTrapRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysAdjChannelTrapRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysAdjChannelTrapRssiThreshold.setUnits("dBm")
_ClsSysClientTrapRssiThreshold_Type = Integer32
_ClsSysClientTrapRssiThreshold_Object = MibScalar
clsSysClientTrapRssiThreshold = _ClsSysClientTrapRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 27),
    _ClsSysClientTrapRssiThreshold_Type()
)
clsSysClientTrapRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysClientTrapRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysClientTrapRssiThreshold.setUnits("dBm")
_ClsSysCmxActiveConnections_Type = Unsigned32
_ClsSysCmxActiveConnections_Object = MibScalar
clsSysCmxActiveConnections = _ClsSysCmxActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 28),
    _ClsSysCmxActiveConnections_Type()
)
clsSysCmxActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCmxActiveConnections.setStatus("current")
_ClsLyncInfo_ObjectIdentity = ObjectIdentity
clsLyncInfo = _ClsLyncInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 9)
)


class _ClsLyncState_Type(TruthValue):
    """Custom type clsLyncState based on TruthValue"""
    defaultValue = 2


_ClsLyncState_Type.__name__ = "TruthValue"
_ClsLyncState_Object = MibScalar
clsLyncState = _ClsLyncState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 9, 1),
    _ClsLyncState_Type()
)
clsLyncState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLyncState.setStatus("current")
_ClsLyncPort_Type = InetPortNumber
_ClsLyncPort_Object = MibScalar
clsLyncPort = _ClsLyncPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 9, 2),
    _ClsLyncPort_Type()
)
clsLyncPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLyncPort.setStatus("current")


class _ClsLyncProtocol_Type(Integer32):
    """Custom type clsLyncProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("securehttp", 2))
    )


_ClsLyncProtocol_Type.__name__ = "Integer32"
_ClsLyncProtocol_Object = MibScalar
clsLyncProtocol = _ClsLyncProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 9, 3),
    _ClsLyncProtocol_Type()
)
clsLyncProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsLyncProtocol.setStatus("current")
_CiscoLwappSysMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBConform = _CiscoLwappSysMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2)
)
_CiscoLwappSysMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBCompliances = _CiscoLwappSysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1)
)
_CiscoLwappSysMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBGroups = _CiscoLwappSysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2)
)

# Managed Objects groups

ciscoLwappSysConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 1)
)
ciscoLwappSysConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsDot3BridgeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsDownloadFileType"),
        ("CISCO-LWAPP-SYS-MIB", "clsDownloadCertificateKey"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadFileType"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadPacUsername"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadPacPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadPacValidity"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroup.setStatus("current")

ciscoLwappSysConfigFileEncryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 2)
)
ciscoLwappSysConfigFileEncryptionGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsTransferConfigFileEncryption"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferConfigFileEncryptionKey"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigFileEncryptionGroup.setStatus("current")

ciscoLwappSysConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 3)
)
ciscoLwappSysConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsTimeZone"),
        ("CISCO-LWAPP-SYS-MIB", "clsTimeZoneDescription"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLogAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLogAddress"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLogHostRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysArpUnicastEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigArpUnicastEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkRoutePrefixLength"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkRouteGatewayType"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkRouteGateway"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkRouteStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroupSup1.setStatus("current")

ciscoLwappSysTransferOperationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 4)
)
ciscoLwappSysTransferOperationConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsTransferServerAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferServerAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferPath"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFilename"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFtpUsername"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFtpPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFtpPortNum"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferTftpMaxRetries"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferTftpTimeout"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStart"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStatusString"),
        ("CISCO-LWAPP-SYS-MIB", "clsApPrimaryVers"),
        ("CISCO-LWAPP-SYS-MIB", "clsApBackupVers"),
        ("CISCO-LWAPP-SYS-MIB", "clsApPredStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsApPredFailReason"),
        ("CISCO-LWAPP-SYS-MIB", "clsApPredRetryCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsApPredNextRetryTime"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingServerAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingServerAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingPath"),
        ("CISCO-LWAPP-SYS-MIB", "clsStreamingTransferStart"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferHttpStreamingUsername"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferHttpStreamingPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferHttpStreamingSuggestedVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferHttpStreamingLatestVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferHttpStreamingCcoPoll"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingServerPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingUsername"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStreamingOptimizedJoinEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysTransferOperationConfigGroup.setStatus("current")

ciscoLwappSysPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 5)
)
ciscoLwappSysPortConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsPortModePhysicalMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortModePhysicalStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortModeSfpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortUpDownCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortModeMaxSpeed"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysPortConfigGroup.setStatus("current")

ciscoLwappSysSecurityConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 6)
)
ciscoLwappSysSecurityConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCaseCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdConsecutiveCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdDefaultCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdAsUserNameCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdPositionCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdDigitCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdMinLength"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdMinUpperCase"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdMinLowerCase"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdMinDigits"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdMinSpecialChar"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecWlanCCEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecUcaplEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecMgmtUsrLockoutEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecMgmtUsrLockoutTime"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecMgmtUsrLockoutAttempts"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecSnmpv3UsrLockoutEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecSnmpv3UsrLockoutTime"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecSnmpv3UsrLockoutAttempts"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecMgmtUsrLockoutLifetime"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecSnmpv3UsrLockoutLifetime"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysSecurityConfigGroup.setStatus("current")

ciscoLwappSysIgmpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 7)
)
ciscoLwappSysIgmpConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "cLSysMulticastIGMPSnoopingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastIGMPSnoopingTimeout"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastIGMPQueryInterval"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastLLBridgingStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysIgmpConfigGroup.setStatus("current")

ciscoLwappSysSecNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 8)
)
ciscoLwappSysSecNotifObjsGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdManagementUser"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckOption"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAlarmSet"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMaxThresholdReachedClear"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferCfgAnalyzeResult"),
        ("CISCO-LWAPP-SYS-MIB", "clsWlcSwVersionBeforeUpgrade"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferCfgAnalyzeResult"),
        ("CISCO-LWAPP-SYS-MIB", "clsWlcSwVersionBeforeUpgrade"),
        ("CISCO-LWAPP-SYS-MIB", "clsWlcUpgradeFailReason"),
        ("CISCO-LWAPP-SYS-MIB", "clsWlcSwVersionAfterUpgrade"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortNumber"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortSpeed"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortSlot"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysSecNotifObjsGroup.setStatus("current")

ciscoLwappSysNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 10)
)
ciscoLwappSysNotifControlGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckTrapEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsTrapEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsTrapEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsNacAlertTrapEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsMfpTrapEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysNotifControlGroup.setStatus("current")

ciscoLwappSysConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 11)
)
ciscoLwappSysConfigGroupVer1.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsConfigProductBranchVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigDhcpProxyEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpTransferEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpTransferMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpFileName"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpUserName"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigMulticastEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsEmergencyImageVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsNMHeartBeatEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsNMHeartBeatInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysControllerCpuUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysControllerMemoryUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApCpuUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApMemoryUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsTrapNameInBlacklist"),
        ("CISCO-LWAPP-SYS-MIB", "clsTrapBlacklistRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsLinkLocalBridgingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProfCustomPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsWGBForcedL2RoamEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCrashSystem"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaServerIpAddr"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaServerIpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaAccountingInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaVenue"),
        ("CISCO-LWAPP-SYS-MIB", "clSysLogIPSecStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clSysLogIPSecProfName"),
        ("CISCO-LWAPP-SYS-MIB", "clsRAIDStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsRAIDRebuildPercentage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestIPAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestIPAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestSendCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestReceivedCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestMaxTimeInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestMinTimeInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestAvgTimeInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsSensorTemperature"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysBroadcastForwardingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpServerIPAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsAlarmHoldTime"),
        ("CISCO-LWAPP-SYS-MIB", "clsAlarmTrapRetransmitInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysLogEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysLogLevel"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgFileType"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgLangCode"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgWidth"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgHeight"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProxyIpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProxyIp"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkDnsServerIpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkDnsServerIp"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProxyPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpServerIPAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsAllCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsUSBMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroupVer1.setStatus("deprecated")

ciscoLwappSysStatsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 12)
)
ciscoLwappSysStatsConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysRealtimeStatsTimer"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysStatsSamplingInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysNormalStatsTimer"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysStatsAverageInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysStatsConfigGroup.setStatus("current")

ciscoLwappSysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 13)
)
ciscoLwappSysInfoGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysFlashSize"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMemoryType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMaxClients"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApConnectCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysNetId"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCurrentMemoryUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAverageMemoryUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCurrentCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAverageCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCpuType"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsApAssocFailedCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsCurrentPortalClientCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsCurrentOnlineUsersCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAbnormalOfflineCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysFlashType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysOpenUsersCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysWepPskUsersCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPeapSimUsersCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPeapSimReqCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPeapSimReqSuccessCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPeapSimReqFailureCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysNasId"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCoChannelTrapRssiThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAdjChannelTrapRssiThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysClientTrapRssiThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCmxActiveConnections"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeInTransition"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysInfoGroup.setStatus("current")

ciscoLwappLyncInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 14)
)
ciscoLwappLyncInfoGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsLyncState"),
        ("CISCO-LWAPP-SYS-MIB", "clsLyncPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsLyncProtocol"))
)
if mibBuilder.loadTexts:
    ciscoLwappLyncInfoGroup.setStatus("current")

ciscoLwappSysMulticastMLDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 15)
)
ciscoLwappSysMulticastMLDGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "cLSysMulticastMLDSnoopingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastMLDSnoopingTimeout"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastMLDQueryInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMulticastMLDGroup.setStatus("current")

ciscoLwappSysConfigGroupVer2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 16)
)
ciscoLwappSysConfigGroupVer2.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsConfigProductBranchVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigDhcpProxyEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpTransferEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpTransferMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpFileName"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpUserName"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigMulticastEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsEmergencyImageVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsNMHeartBeatEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsNMHeartBeatInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysControllerCpuUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysControllerMemoryUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApCpuUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApMemoryUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsTrapNameInBlacklist"),
        ("CISCO-LWAPP-SYS-MIB", "clsTrapBlacklistRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsLinkLocalBridgingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProfCustomPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsWGBForcedL2RoamEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCrashSystem"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaServerIpAddr"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaServerIpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaAccountingInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigCaleaVenue"),
        ("CISCO-LWAPP-SYS-MIB", "clSysLogIPSecStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clSysLogIPSecProfName"),
        ("CISCO-LWAPP-SYS-MIB", "clsRAIDStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsRAIDRebuildPercentage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestIPAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestIPAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestSendCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestReceivedCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestMaxTimeInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestMinTimeInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestAvgTimeInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysPingTestRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsSensorTemperature"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysBroadcastForwardingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpServerIPAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsAlarmHoldTime"),
        ("CISCO-LWAPP-SYS-MIB", "clsAlarmTrapRetransmitInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysLogEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysLogLevel"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgFileType"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgLangCode"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgWidth"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgHeight"),
        ("CISCO-LWAPP-SYS-MIB", "clsIconCfgRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProxyIpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProxyIp"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkDnsServerIpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkDnsServerIp"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsNetworkHttpProxyPort"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpServerIPAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsAllCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsUSBMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsLiStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsLiReportingInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsLiAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsLiAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroupVer2.setStatus("current")


# Notification objects

ciscoLwappSysInvalidXmlConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappSysInvalidXmlConfig.setStatus(
        "current"
    )

ciscoLwappNoVlanConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 2)
)
ciscoLwappNoVlanConfigured.setObjects(
    ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAccessVLAN")
)
if mibBuilder.loadTexts:
    ciscoLwappNoVlanConfigured.setStatus(
        "current"
    )

ciscoLwappStrongPwdCheckNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 3)
)
ciscoLwappStrongPwdCheckNotif.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdManagementUser"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckOption"))
)
if mibBuilder.loadTexts:
    ciscoLwappStrongPwdCheckNotif.setStatus(
        "current"
    )

ciscoLwappSysCpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 4)
)
ciscoLwappSysCpuUsageHigh.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysCurrentCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysCpuUsageHigh.setStatus(
        "current"
    )

ciscoLwappSysMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 5)
)
ciscoLwappSysMemoryUsageHigh.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysCurrentMemoryUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMemoryUsageHigh.setStatus(
        "current"
    )

ciscoLwappMaxRFIDTagsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 6)
)
ciscoLwappMaxRFIDTagsReached.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMaxThresholdReachedClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappMaxRFIDTagsReached.setStatus(
        "current"
    )

ciscoLwappMaxClientsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 7)
)
ciscoLwappMaxClientsReached.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsMaxClientsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMaxThresholdReachedClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappMaxClientsReached.setStatus(
        "current"
    )

ciscoLwappNMHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 8)
)
if mibBuilder.loadTexts:
    ciscoLwappNMHeartBeat.setStatus(
        "current"
    )

ciscoLwappCfgFileAnalyzeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 9)
)
ciscoLwappCfgFileAnalyzeFail.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsTransferFilename"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferCfgAnalyzeResult"))
)
if mibBuilder.loadTexts:
    ciscoLwappCfgFileAnalyzeFail.setStatus(
        "current"
    )

ciscoLwappWlcUpgradeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 10)
)
ciscoLwappWlcUpgradeFail.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsWlcSwVersionBeforeUpgrade"),
        ("CISCO-LWAPP-SYS-MIB", "clsWlcSwVersionAfterUpgrade"),
        ("CISCO-LWAPP-SYS-MIB", "clsWlcUpgradeFailReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlcUpgradeFail.setStatus(
        "current"
    )

ciscoLwappRAIDStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 11)
)
ciscoLwappRAIDStatus.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsRAIDStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsRAIDDriveNumber"),
        ("CISCO-LWAPP-SYS-MIB", "clsRAIDRebuildPercentage"))
)
if mibBuilder.loadTexts:
    ciscoLwappRAIDStatus.setStatus(
        "current"
    )

ciscoLwappPortLinkSpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 12)
)
ciscoLwappPortLinkSpeedTrap.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsPortNumber"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortSpeed"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortSlot"))
)
if mibBuilder.loadTexts:
    ciscoLwappPortLinkSpeedTrap.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappSysNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 9)
)
ciscoLwappSysNotifsGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysInvalidXmlConfig"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappNoVlanConfigured"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappStrongPwdCheckNotif"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysCpuUsageHigh"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysMemoryUsageHigh"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappMaxClientsReached"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappMaxClientsReached"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappNMHeartBeat"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappCfgFileAnalyzeFail"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappMaxRFIDTagsReached"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappWlcUpgradeFail"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappRAIDStatus"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappPortLinkSpeedTrap"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappSysMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 1)
)
ciscoLwappSysMIBCompliance.setObjects(
    ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 2)
)
ciscoLwappSysMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigFileEncryptionGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysTransferOperationConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 3)
)
ciscoLwappSysMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysPortConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysSecurityConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysIgmpConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysSecNotifObjsGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysNotifsGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysNotifControlGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroupVer1"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigFileEncryptionGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysTransferOperationConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 4)
)
ciscoLwappSysMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysPortConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysSecurityConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysIgmpConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysSecNotifObjsGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysNotifsGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysNotifControlGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappLyncInfoGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroupSup1"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysInfoGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysStatsConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysMulticastMLDGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroupVer1"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigFileEncryptionGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysTransferOperationConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 5)
)
ciscoLwappSysMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysPortConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysSecurityConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysIgmpConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysSecNotifObjsGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysNotifsGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysNotifControlGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappLyncInfoGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroupSup1"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysInfoGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysStatsConfigGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysMulticastMLDGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigGroupVer2"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysConfigFileEncryptionGroup"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysTransferOperationConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-SYS-MIB",
    **{"ciscoLwappSysMIB": ciscoLwappSysMIB,
       "ciscoLwappSysMIBNotifs": ciscoLwappSysMIBNotifs,
       "ciscoLwappSysInvalidXmlConfig": ciscoLwappSysInvalidXmlConfig,
       "ciscoLwappNoVlanConfigured": ciscoLwappNoVlanConfigured,
       "ciscoLwappStrongPwdCheckNotif": ciscoLwappStrongPwdCheckNotif,
       "ciscoLwappSysCpuUsageHigh": ciscoLwappSysCpuUsageHigh,
       "ciscoLwappSysMemoryUsageHigh": ciscoLwappSysMemoryUsageHigh,
       "ciscoLwappMaxRFIDTagsReached": ciscoLwappMaxRFIDTagsReached,
       "ciscoLwappMaxClientsReached": ciscoLwappMaxClientsReached,
       "ciscoLwappNMHeartBeat": ciscoLwappNMHeartBeat,
       "ciscoLwappCfgFileAnalyzeFail": ciscoLwappCfgFileAnalyzeFail,
       "ciscoLwappWlcUpgradeFail": ciscoLwappWlcUpgradeFail,
       "ciscoLwappRAIDStatus": ciscoLwappRAIDStatus,
       "ciscoLwappPortLinkSpeedTrap": ciscoLwappPortLinkSpeedTrap,
       "ciscoLwappSysMIBObjects": ciscoLwappSysMIBObjects,
       "clsConfig": clsConfig,
       "clsDot3BridgeEnabled": clsDot3BridgeEnabled,
       "clsConfigDownload": clsConfigDownload,
       "clsDownloadFileType": clsDownloadFileType,
       "clsDownloadCertificateKey": clsDownloadCertificateKey,
       "clsConfigUpload": clsConfigUpload,
       "clsUploadFileType": clsUploadFileType,
       "clsUploadPacUsername": clsUploadPacUsername,
       "clsUploadPacPassword": clsUploadPacPassword,
       "clsUploadPacValidity": clsUploadPacValidity,
       "clsTransferConfigGroup": clsTransferConfigGroup,
       "clsTransferConfigFileEncryption": clsTransferConfigFileEncryption,
       "clsTransferConfigFileEncryptionKey": clsTransferConfigFileEncryptionKey,
       "clsConfigGeneral": clsConfigGeneral,
       "clsTimeZone": clsTimeZone,
       "clsTimeZoneDescription": clsTimeZoneDescription,
       "clsMaxClientsTrapThreshold": clsMaxClientsTrapThreshold,
       "clsMaxRFIDTagsTrapThreshold": clsMaxRFIDTagsTrapThreshold,
       "clsConfigNetworkGeneral": clsConfigNetworkGeneral,
       "clsNetworkRouteConfigTable": clsNetworkRouteConfigTable,
       "clsNetworkRouteConfigEntry": clsNetworkRouteConfigEntry,
       "clsNetworkRouteIPAddressType": clsNetworkRouteIPAddressType,
       "clsNetworkRouteIPAddress": clsNetworkRouteIPAddress,
       "clsNetworkRoutePrefixLength": clsNetworkRoutePrefixLength,
       "clsNetworkRouteGatewayType": clsNetworkRouteGatewayType,
       "clsNetworkRouteGateway": clsNetworkRouteGateway,
       "clsNetworkRouteStatus": clsNetworkRouteStatus,
       "clsSensorTemperature": clsSensorTemperature,
       "clsLiConfigGeneral": clsLiConfigGeneral,
       "clsLiStatus": clsLiStatus,
       "clsLiReportingInterval": clsLiReportingInterval,
       "clsLiAddressType": clsLiAddressType,
       "clsLiAddress": clsLiAddress,
       "clsSyslogIpConfig": clsSyslogIpConfig,
       "cLSysLogConfigTable": cLSysLogConfigTable,
       "cLSysLogConfigEntry": cLSysLogConfigEntry,
       "cLSysLogServerIndex": cLSysLogServerIndex,
       "cLSysLogAddressType": cLSysLogAddressType,
       "cLSysLogAddress": cLSysLogAddress,
       "cLSysLogHostRowStatus": cLSysLogHostRowStatus,
       "cLSysArpUnicastEnabled": cLSysArpUnicastEnabled,
       "clsTransferConfig": clsTransferConfig,
       "clsTransferConfigTable": clsTransferConfigTable,
       "clsTransferConfigEntry": clsTransferConfigEntry,
       "clsTransferType": clsTransferType,
       "clsTransferMode": clsTransferMode,
       "clsTransferServerAddressType": clsTransferServerAddressType,
       "clsTransferServerAddress": clsTransferServerAddress,
       "clsTransferPath": clsTransferPath,
       "clsTransferFilename": clsTransferFilename,
       "clsTransferFtpUsername": clsTransferFtpUsername,
       "clsTransferFtpPassword": clsTransferFtpPassword,
       "clsTransferFtpPortNum": clsTransferFtpPortNum,
       "clsTransferTftpMaxRetries": clsTransferTftpMaxRetries,
       "clsTransferTftpTimeout": clsTransferTftpTimeout,
       "clsTransferStart": clsTransferStart,
       "clsTransferStatus": clsTransferStatus,
       "clsTransferStatusString": clsTransferStatusString,
       "clsStreamingTransferConfig": clsStreamingTransferConfig,
       "clsApTransferTable": clsApTransferTable,
       "clsApTransferEntry": clsApTransferEntry,
       "clsApTransferSysMacAddress": clsApTransferSysMacAddress,
       "clsApPrimaryVers": clsApPrimaryVers,
       "clsApBackupVers": clsApBackupVers,
       "clsApPredStatus": clsApPredStatus,
       "clsApPredFailReason": clsApPredFailReason,
       "clsApPredRetryCount": clsApPredRetryCount,
       "clsApPredNextRetryTime": clsApPredNextRetryTime,
       "clsTransferStreamingMode": clsTransferStreamingMode,
       "clsTransferStreamingServerAddressType": clsTransferStreamingServerAddressType,
       "clsTransferStreamingServerAddress": clsTransferStreamingServerAddress,
       "clsTransferStreamingPath": clsTransferStreamingPath,
       "clsStreamingTransferStart": clsStreamingTransferStart,
       "clsTransferHttpStreamingUsername": clsTransferHttpStreamingUsername,
       "clsTransferHttpStreamingPassword": clsTransferHttpStreamingPassword,
       "clsTransferHttpStreamingSuggestedVersion": clsTransferHttpStreamingSuggestedVersion,
       "clsTransferHttpStreamingLatestVersion": clsTransferHttpStreamingLatestVersion,
       "clsTransferHttpStreamingCcoPoll": clsTransferHttpStreamingCcoPoll,
       "clsTransferStreamingServerPort": clsTransferStreamingServerPort,
       "clsTransferStreamingUsername": clsTransferStreamingUsername,
       "clsTransferStreamingPassword": clsTransferStreamingPassword,
       "clsTransferStreamingOptimizedJoinEnable": clsTransferStreamingOptimizedJoinEnable,
       "cLSysBroadcastForwardingEnabled": cLSysBroadcastForwardingEnabled,
       "cLSysLagModeEnabled": cLSysLagModeEnabled,
       "clsConfigProductBranchVersion": clsConfigProductBranchVersion,
       "clsConfigDhcpProxyEnabled": clsConfigDhcpProxyEnabled,
       "cLSysMulticastIGMP": cLSysMulticastIGMP,
       "cLSysMulticastIGMPSnoopingEnabled": cLSysMulticastIGMPSnoopingEnabled,
       "cLSysMulticastIGMPSnoopingTimeout": cLSysMulticastIGMPSnoopingTimeout,
       "cLSysMulticastIGMPQueryInterval": cLSysMulticastIGMPQueryInterval,
       "cLSysMulticastLLBridgingStatus": cLSysMulticastLLBridgingStatus,
       "cLSPortModeConfig": cLSPortModeConfig,
       "clsPortModeConfigTable": clsPortModeConfigTable,
       "clsPortModeConfigEntry": clsPortModeConfigEntry,
       "clsPortDot1dBasePort": clsPortDot1dBasePort,
       "clsPortModePhysicalMode": clsPortModePhysicalMode,
       "clsPortModePhysicalStatus": clsPortModePhysicalStatus,
       "clsPortModeSfpType": clsPortModeSfpType,
       "clsPortUpDownCount": clsPortUpDownCount,
       "clsPortModeMaxSpeed": clsPortModeMaxSpeed,
       "clsCoreDump": clsCoreDump,
       "clsCoreDumpTransferEnable": clsCoreDumpTransferEnable,
       "clsCoreDumpTransferMode": clsCoreDumpTransferMode,
       "clsCoreDumpServerIPAddressType": clsCoreDumpServerIPAddressType,
       "clsCoreDumpServerIPAddress": clsCoreDumpServerIPAddress,
       "clsCoreDumpFileName": clsCoreDumpFileName,
       "clsCoreDumpUserName": clsCoreDumpUserName,
       "clsCoreDumpPassword": clsCoreDumpPassword,
       "clsConfigMulticastEnabled": clsConfigMulticastEnabled,
       "cLSysMulticastMLD": cLSysMulticastMLD,
       "cLSysMulticastMLDSnoopingEnabled": cLSysMulticastMLDSnoopingEnabled,
       "cLSysMulticastMLDSnoopingTimeout": cLSysMulticastMLDSnoopingTimeout,
       "cLSysMulticastMLDQueryInterval": cLSysMulticastMLDQueryInterval,
       "clsConfigStats": clsConfigStats,
       "clsSysRealtimeStatsTimer": clsSysRealtimeStatsTimer,
       "clsSysNormalStatsTimer": clsSysNormalStatsTimer,
       "clsSysStatsSamplingInterval": clsSysStatsSamplingInterval,
       "clsSysStatsAverageInterval": clsSysStatsAverageInterval,
       "clsAlarmObjects": clsAlarmObjects,
       "clsAlarmHoldTime": clsAlarmHoldTime,
       "clsAlarmTrapRetransmitInterval": clsAlarmTrapRetransmitInterval,
       "clsSysThresholdConfig": clsSysThresholdConfig,
       "clsSysControllerCpuUsageThreshold": clsSysControllerCpuUsageThreshold,
       "clsSysControllerMemoryUsageThreshold": clsSysControllerMemoryUsageThreshold,
       "clsSysApCpuUsageThreshold": clsSysApCpuUsageThreshold,
       "clsSysApMemoryUsageThreshold": clsSysApMemoryUsageThreshold,
       "clsNMHeartBeat": clsNMHeartBeat,
       "clsNMHeartBeatEnable": clsNMHeartBeatEnable,
       "clsNMHeartBeatInterval": clsNMHeartBeatInterval,
       "clsSysLogEnabled": clsSysLogEnabled,
       "clsSysLogLevel": clsSysLogLevel,
       "clsConfigApMaxCount": clsConfigApMaxCount,
       "cLSTrapSwitchConfig": cLSTrapSwitchConfig,
       "clsTrapBlacklistTable": clsTrapBlacklistTable,
       "clsTrapBlacklistEntry": clsTrapBlacklistEntry,
       "clsBlacklistTrapIndex": clsBlacklistTrapIndex,
       "clsTrapNameInBlacklist": clsTrapNameInBlacklist,
       "clsTrapBlacklistRowStatus": clsTrapBlacklistRowStatus,
       "clsLinkLocalBridgingEnabled": clsLinkLocalBridgingEnabled,
       "clsNetworkHttpProfCustomPort": clsNetworkHttpProfCustomPort,
       "clsIconCfgTable": clsIconCfgTable,
       "clsIconCfgEntry": clsIconCfgEntry,
       "clsIconCfgFileName": clsIconCfgFileName,
       "clsIconCfgFileType": clsIconCfgFileType,
       "clsIconCfgLangCode": clsIconCfgLangCode,
       "clsIconCfgWidth": clsIconCfgWidth,
       "clsIconCfgHeight": clsIconCfgHeight,
       "clsIconCfgRowStatus": clsIconCfgRowStatus,
       "clsNetworkHttpProxyPort": clsNetworkHttpProxyPort,
       "clsNetworkHttpProxyIpType": clsNetworkHttpProxyIpType,
       "clsNetworkHttpProxyIp": clsNetworkHttpProxyIp,
       "clsNetworkDnsServerIpType": clsNetworkDnsServerIpType,
       "clsNetworkDnsServerIp": clsNetworkDnsServerIp,
       "clsConfigCalea": clsConfigCalea,
       "clsConfigCaleaEnabled": clsConfigCaleaEnabled,
       "clsConfigCaleaServerIp": clsConfigCaleaServerIp,
       "clsConfigCaleaPort": clsConfigCaleaPort,
       "clsConfigCaleaAccountingInterval": clsConfigCaleaAccountingInterval,
       "clsConfigCaleaVenue": clsConfigCaleaVenue,
       "clsConfigCaleaServerIpType": clsConfigCaleaServerIpType,
       "clsConfigCaleaServerIpAddr": clsConfigCaleaServerIpAddr,
       "clSysLogIPSecStatus": clSysLogIPSecStatus,
       "clSysLogIPSecProfName": clSysLogIPSecProfName,
       "clsConfigArpUnicastEnabled": clsConfigArpUnicastEnabled,
       "clsWGBForcedL2RoamEnabled": clsWGBForcedL2RoamEnabled,
       "clsUSBMode": clsUSBMode,
       "clsCrashSystem": clsCrashSystem,
       "clsStatus": clsStatus,
       "cLSysLagModeInTransition": cLSysLagModeInTransition,
       "clsRAIDStatusTable": clsRAIDStatusTable,
       "clsRAIDStatusEntry": clsRAIDStatusEntry,
       "clsRAIDDriveNumber": clsRAIDDriveNumber,
       "clsRAIDStatus": clsRAIDStatus,
       "clsRAIDRebuildPercentage": clsRAIDRebuildPercentage,
       "clsSysPingTestTable": clsSysPingTestTable,
       "clsSysPingTestEntry": clsSysPingTestEntry,
       "clsSysPingTestId": clsSysPingTestId,
       "clsSysPingTestIPAddressType": clsSysPingTestIPAddressType,
       "clsSysPingTestIPAddress": clsSysPingTestIPAddress,
       "clsSysPingTestSendCount": clsSysPingTestSendCount,
       "clsSysPingTestReceivedCount": clsSysPingTestReceivedCount,
       "clsSysPingTestStatus": clsSysPingTestStatus,
       "clsSysPingTestMaxTimeInterval": clsSysPingTestMaxTimeInterval,
       "clsSysPingTestMinTimeInterval": clsSysPingTestMinTimeInterval,
       "clsSysPingTestAvgTimeInterval": clsSysPingTestAvgTimeInterval,
       "clsSysPingTestRowStatus": clsSysPingTestRowStatus,
       "clsImageInfo": clsImageInfo,
       "clsEmergencyImageVersion": clsEmergencyImageVersion,
       "clsCpuInfo": clsCpuInfo,
       "clsAllCpuUsage": clsAllCpuUsage,
       "clsSecurityGroup": clsSecurityGroup,
       "clsSecStrongPwdCaseCheck": clsSecStrongPwdCaseCheck,
       "clsSecStrongPwdConsecutiveCheck": clsSecStrongPwdConsecutiveCheck,
       "clsSecStrongPwdDefaultCheck": clsSecStrongPwdDefaultCheck,
       "clsSecStrongPwdAsUserNameCheck": clsSecStrongPwdAsUserNameCheck,
       "clsSecStrongPwdPositionCheck": clsSecStrongPwdPositionCheck,
       "clsSecStrongPwdDigitCheck": clsSecStrongPwdDigitCheck,
       "clsSecStrongPwdMinLength": clsSecStrongPwdMinLength,
       "clsSecStrongPwdMinUpperCase": clsSecStrongPwdMinUpperCase,
       "clsSecStrongPwdMinLowerCase": clsSecStrongPwdMinLowerCase,
       "clsSecStrongPwdMinDigits": clsSecStrongPwdMinDigits,
       "clsSecStrongPwdMinSpecialChar": clsSecStrongPwdMinSpecialChar,
       "clsSecWlanCCEnable": clsSecWlanCCEnable,
       "clsSecUcaplEnable": clsSecUcaplEnable,
       "clsSecMgmtUsrLockoutEnable": clsSecMgmtUsrLockoutEnable,
       "clsSecMgmtUsrLockoutTime": clsSecMgmtUsrLockoutTime,
       "clsSecMgmtUsrLockoutAttempts": clsSecMgmtUsrLockoutAttempts,
       "clsSecSnmpv3UsrLockoutEnable": clsSecSnmpv3UsrLockoutEnable,
       "clsSecSnmpv3UsrLockoutTime": clsSecSnmpv3UsrLockoutTime,
       "clsSecSnmpv3UsrLockoutAttempts": clsSecSnmpv3UsrLockoutAttempts,
       "clsSecMgmtUsrLockoutLifetime": clsSecMgmtUsrLockoutLifetime,
       "clsSecSnmpv3UsrLockoutLifetime": clsSecSnmpv3UsrLockoutLifetime,
       "ciscoLwappSysMIBNotifObjects": ciscoLwappSysMIBNotifObjects,
       "clsSecStrongPwdManagementUser": clsSecStrongPwdManagementUser,
       "clsSecStrongPwdCheckType": clsSecStrongPwdCheckType,
       "clsSecStrongPwdCheckOption": clsSecStrongPwdCheckOption,
       "clsSysAlarmSet": clsSysAlarmSet,
       "clsSysMaxThresholdReachedClear": clsSysMaxThresholdReachedClear,
       "clsTransferCfgAnalyzeResult": clsTransferCfgAnalyzeResult,
       "clsWlcSwVersionBeforeUpgrade": clsWlcSwVersionBeforeUpgrade,
       "clsWlcSwVersionAfterUpgrade": clsWlcSwVersionAfterUpgrade,
       "clsWlcUpgradeFailReason": clsWlcUpgradeFailReason,
       "clsPortNumber": clsPortNumber,
       "clsPortSpeed": clsPortSpeed,
       "clsPortSlot": clsPortSlot,
       "ciscoLwappSysMIBNotifControlObjects": ciscoLwappSysMIBNotifControlObjects,
       "clsSecStrongPwdCheckTrapEnabled": clsSecStrongPwdCheckTrapEnabled,
       "clsMaxClientsTrapEnabled": clsMaxClientsTrapEnabled,
       "clsMaxRFIDTagsTrapEnabled": clsMaxRFIDTagsTrapEnabled,
       "clsNacAlertTrapEnabled": clsNacAlertTrapEnabled,
       "clsMfpTrapEnabled": clsMfpTrapEnabled,
       "clsSysInfo": clsSysInfo,
       "clsSysFlashSize": clsSysFlashSize,
       "clsSysMemoryType": clsSysMemoryType,
       "clsSysMaxClients": clsSysMaxClients,
       "clsSysApConnectCount": clsSysApConnectCount,
       "clsSysNetId": clsSysNetId,
       "clsSysCurrentMemoryUsage": clsSysCurrentMemoryUsage,
       "clsSysAverageMemoryUsage": clsSysAverageMemoryUsage,
       "clsSysCurrentCpuUsage": clsSysCurrentCpuUsage,
       "clsSysAverageCpuUsage": clsSysAverageCpuUsage,
       "clsSysCpuType": clsSysCpuType,
       "clsMaxRFIDTagsCount": clsMaxRFIDTagsCount,
       "clsMaxClientsCount": clsMaxClientsCount,
       "clsApAssocFailedCount": clsApAssocFailedCount,
       "clsCurrentPortalClientCount": clsCurrentPortalClientCount,
       "clsCurrentOnlineUsersCount": clsCurrentOnlineUsersCount,
       "clsSysAbnormalOfflineCount": clsSysAbnormalOfflineCount,
       "clsSysFlashType": clsSysFlashType,
       "clsSysOpenUsersCount": clsSysOpenUsersCount,
       "clsSysWepPskUsersCount": clsSysWepPskUsersCount,
       "clsSysPeapSimUsersCount": clsSysPeapSimUsersCount,
       "clsSysPeapSimReqCount": clsSysPeapSimReqCount,
       "clsSysPeapSimReqSuccessCount": clsSysPeapSimReqSuccessCount,
       "clsSysPeapSimReqFailureCount": clsSysPeapSimReqFailureCount,
       "clsSysNasId": clsSysNasId,
       "clsSysCoChannelTrapRssiThreshold": clsSysCoChannelTrapRssiThreshold,
       "clsSysAdjChannelTrapRssiThreshold": clsSysAdjChannelTrapRssiThreshold,
       "clsSysClientTrapRssiThreshold": clsSysClientTrapRssiThreshold,
       "clsSysCmxActiveConnections": clsSysCmxActiveConnections,
       "clsLyncInfo": clsLyncInfo,
       "clsLyncState": clsLyncState,
       "clsLyncPort": clsLyncPort,
       "clsLyncProtocol": clsLyncProtocol,
       "ciscoLwappSysMIBConform": ciscoLwappSysMIBConform,
       "ciscoLwappSysMIBCompliances": ciscoLwappSysMIBCompliances,
       "ciscoLwappSysMIBCompliance": ciscoLwappSysMIBCompliance,
       "ciscoLwappSysMIBComplianceRev1": ciscoLwappSysMIBComplianceRev1,
       "ciscoLwappSysMIBComplianceRev2": ciscoLwappSysMIBComplianceRev2,
       "ciscoLwappSysMIBComplianceRev3": ciscoLwappSysMIBComplianceRev3,
       "ciscoLwappSysMIBComplianceRev4": ciscoLwappSysMIBComplianceRev4,
       "ciscoLwappSysMIBGroups": ciscoLwappSysMIBGroups,
       "ciscoLwappSysConfigGroup": ciscoLwappSysConfigGroup,
       "ciscoLwappSysConfigFileEncryptionGroup": ciscoLwappSysConfigFileEncryptionGroup,
       "ciscoLwappSysConfigGroupSup1": ciscoLwappSysConfigGroupSup1,
       "ciscoLwappSysTransferOperationConfigGroup": ciscoLwappSysTransferOperationConfigGroup,
       "ciscoLwappSysPortConfigGroup": ciscoLwappSysPortConfigGroup,
       "ciscoLwappSysSecurityConfigGroup": ciscoLwappSysSecurityConfigGroup,
       "ciscoLwappSysIgmpConfigGroup": ciscoLwappSysIgmpConfigGroup,
       "ciscoLwappSysSecNotifObjsGroup": ciscoLwappSysSecNotifObjsGroup,
       "ciscoLwappSysNotifsGroup": ciscoLwappSysNotifsGroup,
       "ciscoLwappSysNotifControlGroup": ciscoLwappSysNotifControlGroup,
       "ciscoLwappSysConfigGroupVer1": ciscoLwappSysConfigGroupVer1,
       "ciscoLwappSysStatsConfigGroup": ciscoLwappSysStatsConfigGroup,
       "ciscoLwappSysInfoGroup": ciscoLwappSysInfoGroup,
       "ciscoLwappLyncInfoGroup": ciscoLwappLyncInfoGroup,
       "ciscoLwappSysMulticastMLDGroup": ciscoLwappSysMulticastMLDGroup,
       "ciscoLwappSysConfigGroupVer2": ciscoLwappSysConfigGroupVer2}
)
