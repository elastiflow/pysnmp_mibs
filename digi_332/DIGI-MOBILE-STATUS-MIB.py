# SNMP MIB module (DIGI-MOBILE-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-MOBILE-STATUS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiMobileStatus,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiMobileStatus")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _MsConnectionEnabled_Type(OctetString):
    """Custom type msConnectionEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsConnectionEnabled_Type.__name__ = "OctetString"
_MsConnectionEnabled_Object = MibScalar
msConnectionEnabled = _MsConnectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 1),
    _MsConnectionEnabled_Type()
)
msConnectionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msConnectionEnabled.setStatus("mandatory")


class _MsServiceProvider_Type(OctetString):
    """Custom type msServiceProvider based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsServiceProvider_Type.__name__ = "OctetString"
_MsServiceProvider_Object = MibScalar
msServiceProvider = _MsServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 2),
    _MsServiceProvider_Type()
)
msServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msServiceProvider.setStatus("mandatory")


class _MsConnectionStatus_Type(OctetString):
    """Custom type msConnectionStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsConnectionStatus_Type.__name__ = "OctetString"
_MsConnectionStatus_Object = MibScalar
msConnectionStatus = _MsConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 3),
    _MsConnectionStatus_Type()
)
msConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msConnectionStatus.setStatus("mandatory")


class _MsConnectionType_Type(OctetString):
    """Custom type msConnectionType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsConnectionType_Type.__name__ = "OctetString"
_MsConnectionType_Object = MibScalar
msConnectionType = _MsConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 4),
    _MsConnectionType_Type()
)
msConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msConnectionType.setStatus("mandatory")


class _MsRssi2G_Type(OctetString):
    """Custom type msRssi2G based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsRssi2G_Type.__name__ = "OctetString"
_MsRssi2G_Object = MibScalar
msRssi2G = _MsRssi2G_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 5),
    _MsRssi2G_Type()
)
msRssi2G.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRssi2G.setStatus("mandatory")


class _MsRssi3G_Type(OctetString):
    """Custom type msRssi3G based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsRssi3G_Type.__name__ = "OctetString"
_MsRssi3G_Object = MibScalar
msRssi3G = _MsRssi3G_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 6),
    _MsRssi3G_Type()
)
msRssi3G.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRssi3G.setStatus("mandatory")


class _MsEcIo2G_Type(OctetString):
    """Custom type msEcIo2G based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsEcIo2G_Type.__name__ = "OctetString"
_MsEcIo2G_Object = MibScalar
msEcIo2G = _MsEcIo2G_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 7),
    _MsEcIo2G_Type()
)
msEcIo2G.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msEcIo2G.setStatus("mandatory")


class _MsEcIo3G_Type(OctetString):
    """Custom type msEcIo3G based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsEcIo3G_Type.__name__ = "OctetString"
_MsEcIo3G_Object = MibScalar
msEcIo3G = _MsEcIo3G_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 8),
    _MsEcIo3G_Type()
)
msEcIo3G.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msEcIo3G.setStatus("mandatory")


class _MsMobileIpAddress_Type(OctetString):
    """Custom type msMobileIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobileIpAddress_Type.__name__ = "OctetString"
_MsMobileIpAddress_Object = MibScalar
msMobileIpAddress = _MsMobileIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 9),
    _MsMobileIpAddress_Type()
)
msMobileIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobileIpAddress.setStatus("mandatory")


class _MsRegistrationStatus_Type(OctetString):
    """Custom type msRegistrationStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsRegistrationStatus_Type.__name__ = "OctetString"
_MsRegistrationStatus_Object = MibScalar
msRegistrationStatus = _MsRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 10),
    _MsRegistrationStatus_Type()
)
msRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRegistrationStatus.setStatus("mandatory")


class _MsGsmLocationAreaCode_Type(OctetString):
    """Custom type msGsmLocationAreaCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsGsmLocationAreaCode_Type.__name__ = "OctetString"
_MsGsmLocationAreaCode_Object = MibScalar
msGsmLocationAreaCode = _MsGsmLocationAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 11),
    _MsGsmLocationAreaCode_Type()
)
msGsmLocationAreaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msGsmLocationAreaCode.setStatus("mandatory")


class _MsGsmCellId_Type(OctetString):
    """Custom type msGsmCellId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsGsmCellId_Type.__name__ = "OctetString"
_MsGsmCellId_Object = MibScalar
msGsmCellId = _MsGsmCellId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 12),
    _MsGsmCellId_Type()
)
msGsmCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msGsmCellId.setStatus("mandatory")


class _MsCdmaSystemId_Type(OctetString):
    """Custom type msCdmaSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsCdmaSystemId_Type.__name__ = "OctetString"
_MsCdmaSystemId_Object = MibScalar
msCdmaSystemId = _MsCdmaSystemId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 13),
    _MsCdmaSystemId_Type()
)
msCdmaSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCdmaSystemId.setStatus("mandatory")


class _MsCdmaNetworkId_Type(OctetString):
    """Custom type msCdmaNetworkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsCdmaNetworkId_Type.__name__ = "OctetString"
_MsCdmaNetworkId_Object = MibScalar
msCdmaNetworkId = _MsCdmaNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 14),
    _MsCdmaNetworkId_Type()
)
msCdmaNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCdmaNetworkId.setStatus("mandatory")


class _MsCdmaBaseStationId_Type(OctetString):
    """Custom type msCdmaBaseStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsCdmaBaseStationId_Type.__name__ = "OctetString"
_MsCdmaBaseStationId_Object = MibScalar
msCdmaBaseStationId = _MsCdmaBaseStationId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 15),
    _MsCdmaBaseStationId_Type()
)
msCdmaBaseStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCdmaBaseStationId.setStatus("mandatory")


class _MsCdmaBaseStationLatLon_Type(OctetString):
    """Custom type msCdmaBaseStationLatLon based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsCdmaBaseStationLatLon_Type.__name__ = "OctetString"
_MsCdmaBaseStationLatLon_Object = MibScalar
msCdmaBaseStationLatLon = _MsCdmaBaseStationLatLon_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 16),
    _MsCdmaBaseStationLatLon_Type()
)
msCdmaBaseStationLatLon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCdmaBaseStationLatLon.setStatus("mandatory")


class _MsMobileCountryCode_Type(OctetString):
    """Custom type msMobileCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobileCountryCode_Type.__name__ = "OctetString"
_MsMobileCountryCode_Object = MibScalar
msMobileCountryCode = _MsMobileCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 17),
    _MsMobileCountryCode_Type()
)
msMobileCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobileCountryCode.setStatus("mandatory")


class _MsMobileNetworkCode_Type(OctetString):
    """Custom type msMobileNetworkCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobileNetworkCode_Type.__name__ = "OctetString"
_MsMobileNetworkCode_Object = MibScalar
msMobileNetworkCode = _MsMobileNetworkCode_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 18),
    _MsMobileNetworkCode_Type()
)
msMobileNetworkCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobileNetworkCode.setStatus("mandatory")


class _MsNetworkName_Type(OctetString):
    """Custom type msNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsNetworkName_Type.__name__ = "OctetString"
_MsNetworkName_Object = MibScalar
msNetworkName = _MsNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 19),
    _MsNetworkName_Type()
)
msNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msNetworkName.setStatus("mandatory")


class _MsServiceModeCellType_Type(OctetString):
    """Custom type msServiceModeCellType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsServiceModeCellType_Type.__name__ = "OctetString"
_MsServiceModeCellType_Object = MibScalar
msServiceModeCellType = _MsServiceModeCellType_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 20),
    _MsServiceModeCellType_Type()
)
msServiceModeCellType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msServiceModeCellType.setStatus("mandatory")


class _MsMobileBandClass_Type(OctetString):
    """Custom type msMobileBandClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobileBandClass_Type.__name__ = "OctetString"
_MsMobileBandClass_Object = MibScalar
msMobileBandClass = _MsMobileBandClass_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 21),
    _MsMobileBandClass_Type()
)
msMobileBandClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobileBandClass.setStatus("mandatory")


class _MsMobileFrequency_Type(OctetString):
    """Custom type msMobileFrequency based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobileFrequency_Type.__name__ = "OctetString"
_MsMobileFrequency_Object = MibScalar
msMobileFrequency = _MsMobileFrequency_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 22),
    _MsMobileFrequency_Type()
)
msMobileFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobileFrequency.setStatus("mandatory")


class _MsMobileChannel_Type(OctetString):
    """Custom type msMobileChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobileChannel_Type.__name__ = "OctetString"
_MsMobileChannel_Object = MibScalar
msMobileChannel = _MsMobileChannel_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 23),
    _MsMobileChannel_Type()
)
msMobileChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobileChannel.setStatus("mandatory")


class _MsModemManufacturer_Type(OctetString):
    """Custom type msModemManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsModemManufacturer_Type.__name__ = "OctetString"
_MsModemManufacturer_Object = MibScalar
msModemManufacturer = _MsModemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 24),
    _MsModemManufacturer_Type()
)
msModemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msModemManufacturer.setStatus("mandatory")


class _MsModemModelId_Type(OctetString):
    """Custom type msModemModelId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsModemModelId_Type.__name__ = "OctetString"
_MsModemModelId_Object = MibScalar
msModemModelId = _MsModemModelId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 25),
    _MsModemModelId_Type()
)
msModemModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msModemModelId.setStatus("mandatory")


class _MsModemRevisionId_Type(OctetString):
    """Custom type msModemRevisionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsModemRevisionId_Type.__name__ = "OctetString"
_MsModemRevisionId_Object = MibScalar
msModemRevisionId = _MsModemRevisionId_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 26),
    _MsModemRevisionId_Type()
)
msModemRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msModemRevisionId.setStatus("mandatory")


class _MsModemSerialNumber_Type(OctetString):
    """Custom type msModemSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsModemSerialNumber_Type.__name__ = "OctetString"
_MsModemSerialNumber_Object = MibScalar
msModemSerialNumber = _MsModemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 27),
    _MsModemSerialNumber_Type()
)
msModemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msModemSerialNumber.setStatus("mandatory")


class _MsModemMeid_Type(OctetString):
    """Custom type msModemMeid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsModemMeid_Type.__name__ = "OctetString"
_MsModemMeid_Object = MibScalar
msModemMeid = _MsModemMeid_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 28),
    _MsModemMeid_Type()
)
msModemMeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msModemMeid.setStatus("mandatory")


class _MsImsi_Type(OctetString):
    """Custom type msImsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsImsi_Type.__name__ = "OctetString"
_MsImsi_Object = MibScalar
msImsi = _MsImsi_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 29),
    _MsImsi_Type()
)
msImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msImsi.setStatus("mandatory")


class _MsIccid_Type(OctetString):
    """Custom type msIccid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsIccid_Type.__name__ = "OctetString"
_MsIccid_Object = MibScalar
msIccid = _MsIccid_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 30),
    _MsIccid_Type()
)
msIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msIccid.setStatus("mandatory")


class _MsMobilePhoneNumber_Type(OctetString):
    """Custom type msMobilePhoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsMobilePhoneNumber_Type.__name__ = "OctetString"
_MsMobilePhoneNumber_Object = MibScalar
msMobilePhoneNumber = _MsMobilePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 31),
    _MsMobilePhoneNumber_Type()
)
msMobilePhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMobilePhoneNumber.setStatus("mandatory")


class _MsCdmaPrlVersion_Type(OctetString):
    """Custom type msCdmaPrlVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsCdmaPrlVersion_Type.__name__ = "OctetString"
_MsCdmaPrlVersion_Object = MibScalar
msCdmaPrlVersion = _MsCdmaPrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 32),
    _MsCdmaPrlVersion_Type()
)
msCdmaPrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCdmaPrlVersion.setStatus("mandatory")


class _MsTotalBytesSent_Type(OctetString):
    """Custom type msTotalBytesSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsTotalBytesSent_Type.__name__ = "OctetString"
_MsTotalBytesSent_Object = MibScalar
msTotalBytesSent = _MsTotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 33),
    _MsTotalBytesSent_Type()
)
msTotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTotalBytesSent.setStatus("mandatory")


class _MsTotalBytesReceived_Type(OctetString):
    """Custom type msTotalBytesReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsTotalBytesReceived_Type.__name__ = "OctetString"
_MsTotalBytesReceived_Object = MibScalar
msTotalBytesReceived = _MsTotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 34),
    _MsTotalBytesReceived_Type()
)
msTotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTotalBytesReceived.setStatus("mandatory")


class _MsSessionBytesSent_Type(OctetString):
    """Custom type msSessionBytesSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsSessionBytesSent_Type.__name__ = "OctetString"
_MsSessionBytesSent_Object = MibScalar
msSessionBytesSent = _MsSessionBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 35),
    _MsSessionBytesSent_Type()
)
msSessionBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSessionBytesSent.setStatus("mandatory")


class _MsSessionBytesReceived_Type(OctetString):
    """Custom type msSessionBytesReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsSessionBytesReceived_Type.__name__ = "OctetString"
_MsSessionBytesReceived_Object = MibScalar
msSessionBytesReceived = _MsSessionBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 36),
    _MsSessionBytesReceived_Type()
)
msSessionBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSessionBytesReceived.setStatus("mandatory")


class _MsCurrentSessionDuration_Type(OctetString):
    """Custom type msCurrentSessionDuration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsCurrentSessionDuration_Type.__name__ = "OctetString"
_MsCurrentSessionDuration_Object = MibScalar
msCurrentSessionDuration = _MsCurrentSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 37),
    _MsCurrentSessionDuration_Type()
)
msCurrentSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCurrentSessionDuration.setStatus("mandatory")


class _MsSendIdle_Type(OctetString):
    """Custom type msSendIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsSendIdle_Type.__name__ = "OctetString"
_MsSendIdle_Object = MibScalar
msSendIdle = _MsSendIdle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 38),
    _MsSendIdle_Type()
)
msSendIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSendIdle.setStatus("mandatory")


class _MsReceiveIdle_Type(OctetString):
    """Custom type msReceiveIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MsReceiveIdle_Type.__name__ = "OctetString"
_MsReceiveIdle_Object = MibScalar
msReceiveIdle = _MsReceiveIdle_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4, 39),
    _MsReceiveIdle_Type()
)
msReceiveIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msReceiveIdle.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-MOBILE-STATUS-MIB",
    **{"msConnectionEnabled": msConnectionEnabled,
       "msServiceProvider": msServiceProvider,
       "msConnectionStatus": msConnectionStatus,
       "msConnectionType": msConnectionType,
       "msRssi2G": msRssi2G,
       "msRssi3G": msRssi3G,
       "msEcIo2G": msEcIo2G,
       "msEcIo3G": msEcIo3G,
       "msMobileIpAddress": msMobileIpAddress,
       "msRegistrationStatus": msRegistrationStatus,
       "msGsmLocationAreaCode": msGsmLocationAreaCode,
       "msGsmCellId": msGsmCellId,
       "msCdmaSystemId": msCdmaSystemId,
       "msCdmaNetworkId": msCdmaNetworkId,
       "msCdmaBaseStationId": msCdmaBaseStationId,
       "msCdmaBaseStationLatLon": msCdmaBaseStationLatLon,
       "msMobileCountryCode": msMobileCountryCode,
       "msMobileNetworkCode": msMobileNetworkCode,
       "msNetworkName": msNetworkName,
       "msServiceModeCellType": msServiceModeCellType,
       "msMobileBandClass": msMobileBandClass,
       "msMobileFrequency": msMobileFrequency,
       "msMobileChannel": msMobileChannel,
       "msModemManufacturer": msModemManufacturer,
       "msModemModelId": msModemModelId,
       "msModemRevisionId": msModemRevisionId,
       "msModemSerialNumber": msModemSerialNumber,
       "msModemMeid": msModemMeid,
       "msImsi": msImsi,
       "msIccid": msIccid,
       "msMobilePhoneNumber": msMobilePhoneNumber,
       "msCdmaPrlVersion": msCdmaPrlVersion,
       "msTotalBytesSent": msTotalBytesSent,
       "msTotalBytesReceived": msTotalBytesReceived,
       "msSessionBytesSent": msSessionBytesSent,
       "msSessionBytesReceived": msSessionBytesReceived,
       "msCurrentSessionDuration": msCurrentSessionDuration,
       "msSendIdle": msSendIdle,
       "msReceiveIdle": msReceiveIdle}
)
