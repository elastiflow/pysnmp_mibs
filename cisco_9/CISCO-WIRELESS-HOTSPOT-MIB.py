# SNMP MIB module (CISCO-WIRELESS-HOTSPOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WIRELESS-HOTSPOT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:15 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessHotspotMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863)
)
if mibBuilder.loadTexts:
    ciscoWirelessHotspotMIB.setRevisions(
        ("2020-06-18 00:00",
         "2019-06-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWirelessHotspotMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWirelessHotspotMIBNotifs = _CiscoWirelessHotspotMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 0)
)
_CiscoWirelessHotspotMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWirelessHotspotMIBObjects = _CiscoWirelessHotspotMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1)
)
_CiscoWirelessHotspotConfig_ObjectIdentity = ObjectIdentity
ciscoWirelessHotspotConfig = _CiscoWirelessHotspotConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1)
)
_CLHotspotAnqpServerConfigTable_Object = MibTable
cLHotspotAnqpServerConfigTable = _CLHotspotAnqpServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLHotspotAnqpServerConfigTable.setStatus("current")
_CLHotspotAnqpServerConfigEntry_Object = MibTableRow
cLHotspotAnqpServerConfigEntry = _CLHotspotAnqpServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1)
)
cLHotspotAnqpServerConfigEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
)
if mibBuilder.loadTexts:
    cLHotspotAnqpServerConfigEntry.setStatus("current")


class _CLHotspotAnqpServerName_Type(SnmpAdminString):
    """Custom type cLHotspotAnqpServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotAnqpServerName_Type.__name__ = "SnmpAdminString"
_CLHotspotAnqpServerName_Object = MibTableColumn
cLHotspotAnqpServerName = _CLHotspotAnqpServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 1),
    _CLHotspotAnqpServerName_Type()
)
cLHotspotAnqpServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerName.setStatus("current")
_CLHotspotAnqpServerRowStatus_Type = RowStatus
_CLHotspotAnqpServerRowStatus_Object = MibTableColumn
cLHotspotAnqpServerRowStatus = _CLHotspotAnqpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 2),
    _CLHotspotAnqpServerRowStatus_Type()
)
cLHotspotAnqpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerRowStatus.setStatus("current")
_CLHotspotAnqpServerDescription_Type = SnmpAdminString
_CLHotspotAnqpServerDescription_Object = MibTableColumn
cLHotspotAnqpServerDescription = _CLHotspotAnqpServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 3),
    _CLHotspotAnqpServerDescription_Type()
)
cLHotspotAnqpServerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerDescription.setStatus("current")
_CLHotspotAnqpServerInternetEnabled_Type = TruthValue
_CLHotspotAnqpServerInternetEnabled_Object = MibTableColumn
cLHotspotAnqpServerInternetEnabled = _CLHotspotAnqpServerInternetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 4),
    _CLHotspotAnqpServerInternetEnabled_Type()
)
cLHotspotAnqpServerInternetEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerInternetEnabled.setStatus("current")


class _CLHotspotAnqpServerNetworkType_Type(Integer32):
    """Custom type cLHotspotAnqpServerNetworkType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("guestPrivate", 2),
          ("chargeablePublic", 3),
          ("freePublic", 4),
          ("personalDevice", 5),
          ("emergency", 6),
          ("test", 7),
          ("wildcard", 8))
    )


_CLHotspotAnqpServerNetworkType_Type.__name__ = "Integer32"
_CLHotspotAnqpServerNetworkType_Object = MibTableColumn
cLHotspotAnqpServerNetworkType = _CLHotspotAnqpServerNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 5),
    _CLHotspotAnqpServerNetworkType_Type()
)
cLHotspotAnqpServerNetworkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerNetworkType.setStatus("current")


class _CLHotspotAnqpServerVenueType_Type(Integer32):
    """Custom type cLHotspotAnqpServerVenueType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
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
              66)
        )
    )
    namedValues = NamedValues(
        *(("unspecifiedUnspecified", 1),
          ("assemblyUnspecified", 2),
          ("assemblyArena", 3),
          ("assemblyStadium", 4),
          ("assemblyPassengerTerminal", 5),
          ("assemblyAmphitheater", 6),
          ("assemblyAmusementPark", 7),
          ("assemblyPlaceOfWorship", 8),
          ("assemblyConventionCenter", 9),
          ("assemblyLibrary", 10),
          ("assemblyMuseum", 11),
          ("assemblyRestaurant", 12),
          ("assemblyTheater", 13),
          ("assemblyBar", 14),
          ("assemblyCoffeeShop", 15),
          ("assemblyZoo", 16),
          ("assemblyEmergencyCoordCenter", 17),
          ("businessUnspecified", 18),
          ("businessDoctor", 19),
          ("businessBank", 20),
          ("businessFireStation", 21),
          ("businessPoliceStation", 22),
          ("businessPostOffice", 23),
          ("businessProfessionalOffice", 24),
          ("businessRdFacility", 25),
          ("businessAttorney", 26),
          ("educationalUnspecifiedEducational", 27),
          ("educationalPrimarySchool", 28),
          ("educationalSecondarySchool", 29),
          ("educationaluniversity", 30),
          ("industrialUnspecified", 31),
          ("industrialFactory", 32),
          ("institutionalUnspecified", 33),
          ("institutionalHospital", 34),
          ("institutionalLongTermCareFacility", 35),
          ("institutionalAlcoholDrugRehabCenter", 36),
          ("institutionalGroupHome", 37),
          ("institutionalJail", 38),
          ("mercantileUnspecified", 39),
          ("mercantileRetailStore", 40),
          ("mercantileGroceryMarket", 41),
          ("mercantileAutomotiveServiceStation", 42),
          ("mercantileShoppingMall", 43),
          ("mercantileGasStation", 44),
          ("residentialUnspecified", 45),
          ("residentialPrivate", 46),
          ("residentialHotel", 47),
          ("residentialDormitory", 48),
          ("residentialBoardingHouse", 49),
          ("storageUnspecified", 50),
          ("utilityUnspecified", 51),
          ("vehicularUnspecified", 52),
          ("vehicularAutomobileTruck", 53),
          ("vehicularAirplane", 54),
          ("vehicularBus", 55),
          ("vehicularFerry", 56),
          ("vehicularBoat", 57),
          ("vehicularTrain", 58),
          ("vehicularMotorbike", 59),
          ("outdoorUnspecified", 60),
          ("outdoorMuniMesh", 61),
          ("outdoorCityPark", 62),
          ("outdoorRestArea", 63),
          ("outdoorTrafficControl", 64),
          ("outdoorBusStop", 65),
          ("outdoorKiosk", 66))
    )


_CLHotspotAnqpServerVenueType_Type.__name__ = "Integer32"
_CLHotspotAnqpServerVenueType_Object = MibTableColumn
cLHotspotAnqpServerVenueType = _CLHotspotAnqpServerVenueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 6),
    _CLHotspotAnqpServerVenueType_Type()
)
cLHotspotAnqpServerVenueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerVenueType.setStatus("current")
_CLHotspotAnqpServerHessid_Type = MacAddress
_CLHotspotAnqpServerHessid_Object = MibTableColumn
cLHotspotAnqpServerHessid = _CLHotspotAnqpServerHessid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 7),
    _CLHotspotAnqpServerHessid_Type()
)
cLHotspotAnqpServerHessid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerHessid.setStatus("current")


class _CLHotspotGasRequestTimeout_Type(Unsigned32):
    """Custom type cLHotspotGasRequestTimeout based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CLHotspotGasRequestTimeout_Type.__name__ = "Unsigned32"
_CLHotspotGasRequestTimeout_Object = MibTableColumn
cLHotspotGasRequestTimeout = _CLHotspotGasRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 8),
    _CLHotspotGasRequestTimeout_Type()
)
cLHotspotGasRequestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotGasRequestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLHotspotGasRequestTimeout.setUnits("milliseconds")


class _CLHotspotAnqpFragmentationThreshold_Type(Unsigned32):
    """Custom type cLHotspotAnqpFragmentationThreshold based on Unsigned32"""
    defaultValue = 1294

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1294),
    )


_CLHotspotAnqpFragmentationThreshold_Type.__name__ = "Unsigned32"
_CLHotspotAnqpFragmentationThreshold_Object = MibTableColumn
cLHotspotAnqpFragmentationThreshold = _CLHotspotAnqpFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 9),
    _CLHotspotAnqpFragmentationThreshold_Type()
)
cLHotspotAnqpFragmentationThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpFragmentationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLHotspotAnqpFragmentationThreshold.setUnits("bytes")


class _CLHotspotAnqpDomainId_Type(Unsigned32):
    """Custom type cLHotspotAnqpDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLHotspotAnqpDomainId_Type.__name__ = "Unsigned32"
_CLHotspotAnqpDomainId_Object = MibTableColumn
cLHotspotAnqpDomainId = _CLHotspotAnqpDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 10),
    _CLHotspotAnqpDomainId_Type()
)
cLHotspotAnqpDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpDomainId.setStatus("current")
_CLHotspotAnqpDomainIdEnabled_Type = TruthValue
_CLHotspotAnqpDomainIdEnabled_Object = MibTableColumn
cLHotspotAnqpDomainIdEnabled = _CLHotspotAnqpDomainIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 11),
    _CLHotspotAnqpDomainIdEnabled_Type()
)
cLHotspotAnqpDomainIdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpDomainIdEnabled.setStatus("current")


class _CLHotspotAnqpServerIpv4AddressType_Type(Integer32):
    """Custom type cLHotspotAnqpServerIpv4AddressType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("public", 2),
          ("portRestricted", 3),
          ("singleNatedPrivate", 4),
          ("doubleNatedPrivate", 5),
          ("portRestrictedSingleNatedPrivate", 6),
          ("portRestrictedDoubleNatedPrivate", 7),
          ("notKnown", 8))
    )


_CLHotspotAnqpServerIpv4AddressType_Type.__name__ = "Integer32"
_CLHotspotAnqpServerIpv4AddressType_Object = MibTableColumn
cLHotspotAnqpServerIpv4AddressType = _CLHotspotAnqpServerIpv4AddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 12),
    _CLHotspotAnqpServerIpv4AddressType_Type()
)
cLHotspotAnqpServerIpv4AddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerIpv4AddressType.setStatus("current")


class _CLHotspotAnqpServerIpv6AddressType_Type(Integer32):
    """Custom type cLHotspotAnqpServerIpv6AddressType based on Integer32"""
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
        *(("notAvailable", 1),
          ("available", 2),
          ("notKnown", 3))
    )


_CLHotspotAnqpServerIpv6AddressType_Type.__name__ = "Integer32"
_CLHotspotAnqpServerIpv6AddressType_Object = MibTableColumn
cLHotspotAnqpServerIpv6AddressType = _CLHotspotAnqpServerIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 13),
    _CLHotspotAnqpServerIpv6AddressType_Type()
)
cLHotspotAnqpServerIpv6AddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpServerIpv6AddressType.setStatus("current")


class _CLHotspotAnqpOsuSsid_Type(SnmpAdminString):
    """Custom type cLHotspotAnqpOsuSsid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLHotspotAnqpOsuSsid_Type.__name__ = "SnmpAdminString"
_CLHotspotAnqpOsuSsid_Object = MibTableColumn
cLHotspotAnqpOsuSsid = _CLHotspotAnqpOsuSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 14),
    _CLHotspotAnqpOsuSsid_Type()
)
cLHotspotAnqpOsuSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAnqpOsuSsid.setStatus("current")


class _CLHotspotWanLinkStatus_Type(Integer32):
    """Custom type cLHotspotWanLinkStatus based on Integer32"""
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
        *(("notConfigured", 0),
          ("up", 1),
          ("down", 2),
          ("testState", 3))
    )


_CLHotspotWanLinkStatus_Type.__name__ = "Integer32"
_CLHotspotWanLinkStatus_Object = MibTableColumn
cLHotspotWanLinkStatus = _CLHotspotWanLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 15),
    _CLHotspotWanLinkStatus_Type()
)
cLHotspotWanLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanLinkStatus.setStatus("current")
_CLHotspotWanIsAtCapacity_Type = TruthValue
_CLHotspotWanIsAtCapacity_Object = MibTableColumn
cLHotspotWanIsAtCapacity = _CLHotspotWanIsAtCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 16),
    _CLHotspotWanIsAtCapacity_Type()
)
cLHotspotWanIsAtCapacity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanIsAtCapacity.setStatus("current")
_CLHotspotWanDownlinkSpeed_Type = Unsigned32
_CLHotspotWanDownlinkSpeed_Object = MibTableColumn
cLHotspotWanDownlinkSpeed = _CLHotspotWanDownlinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 17),
    _CLHotspotWanDownlinkSpeed_Type()
)
cLHotspotWanDownlinkSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanDownlinkSpeed.setStatus("current")
_CLHotspotWanUplinkSpeed_Type = Unsigned32
_CLHotspotWanUplinkSpeed_Object = MibTableColumn
cLHotspotWanUplinkSpeed = _CLHotspotWanUplinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 18),
    _CLHotspotWanUplinkSpeed_Type()
)
cLHotspotWanUplinkSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanUplinkSpeed.setStatus("current")


class _CLHotspotWanDownlinkLoad_Type(Unsigned32):
    """Custom type cLHotspotWanDownlinkLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CLHotspotWanDownlinkLoad_Type.__name__ = "Unsigned32"
_CLHotspotWanDownlinkLoad_Object = MibTableColumn
cLHotspotWanDownlinkLoad = _CLHotspotWanDownlinkLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 19),
    _CLHotspotWanDownlinkLoad_Type()
)
cLHotspotWanDownlinkLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanDownlinkLoad.setStatus("current")


class _CLHotspotWanUplinkLoad_Type(Unsigned32):
    """Custom type cLHotspotWanUplinkLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CLHotspotWanUplinkLoad_Type.__name__ = "Unsigned32"
_CLHotspotWanUplinkLoad_Object = MibTableColumn
cLHotspotWanUplinkLoad = _CLHotspotWanUplinkLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 20),
    _CLHotspotWanUplinkLoad_Type()
)
cLHotspotWanUplinkLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanUplinkLoad.setStatus("current")


class _CLHotspotWanLoadMeasDuration_Type(Unsigned32):
    """Custom type cLHotspotWanLoadMeasDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLHotspotWanLoadMeasDuration_Type.__name__ = "Unsigned32"
_CLHotspotWanLoadMeasDuration_Object = MibTableColumn
cLHotspotWanLoadMeasDuration = _CLHotspotWanLoadMeasDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 21),
    _CLHotspotWanLoadMeasDuration_Type()
)
cLHotspotWanLoadMeasDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotWanLoadMeasDuration.setStatus("current")
if mibBuilder.loadTexts:
    cLHotspotWanLoadMeasDuration.setUnits("tenths of seconds")


class _CLHotspotTermsConditionsFilename_Type(SnmpAdminString):
    """Custom type cLHotspotTermsConditionsFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 220),
    )


_CLHotspotTermsConditionsFilename_Type.__name__ = "SnmpAdminString"
_CLHotspotTermsConditionsFilename_Object = MibTableColumn
cLHotspotTermsConditionsFilename = _CLHotspotTermsConditionsFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 22),
    _CLHotspotTermsConditionsFilename_Type()
)
cLHotspotTermsConditionsFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotTermsConditionsFilename.setStatus("current")


class _CLHotspotTermsConditionsDate_Type(SnmpAdminString):
    """Custom type cLHotspotTermsConditionsDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CLHotspotTermsConditionsDate_Type.__name__ = "SnmpAdminString"
_CLHotspotTermsConditionsDate_Object = MibTableColumn
cLHotspotTermsConditionsDate = _CLHotspotTermsConditionsDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 23),
    _CLHotspotTermsConditionsDate_Type()
)
cLHotspotTermsConditionsDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotTermsConditionsDate.setStatus("current")


class _CLHotspotTermsConditionsTime_Type(SnmpAdminString):
    """Custom type cLHotspotTermsConditionsTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CLHotspotTermsConditionsTime_Type.__name__ = "SnmpAdminString"
_CLHotspotTermsConditionsTime_Object = MibTableColumn
cLHotspotTermsConditionsTime = _CLHotspotTermsConditionsTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 24),
    _CLHotspotTermsConditionsTime_Type()
)
cLHotspotTermsConditionsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotTermsConditionsTime.setStatus("current")


class _CLHotspotTermsConditionsUrlFilter_Type(SnmpAdminString):
    """Custom type cLHotspotTermsConditionsUrlFilter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CLHotspotTermsConditionsUrlFilter_Type.__name__ = "SnmpAdminString"
_CLHotspotTermsConditionsUrlFilter_Object = MibTableColumn
cLHotspotTermsConditionsUrlFilter = _CLHotspotTermsConditionsUrlFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 1, 1, 25),
    _CLHotspotTermsConditionsUrlFilter_Type()
)
cLHotspotTermsConditionsUrlFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotTermsConditionsUrlFilter.setStatus("current")
_CLHotspotRoamingOITable_Object = MibTable
cLHotspotRoamingOITable = _CLHotspotRoamingOITable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLHotspotRoamingOITable.setStatus("current")
_CLHotspotRoamingOIEntry_Object = MibTableRow
cLHotspotRoamingOIEntry = _CLHotspotRoamingOIEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 2, 1)
)
cLHotspotRoamingOIEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRoamingOI"),
)
if mibBuilder.loadTexts:
    cLHotspotRoamingOIEntry.setStatus("current")


class _CLHotspotRoamingOI_Type(OctetString):
    """Custom type cLHotspotRoamingOI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(10, 10),
    )


_CLHotspotRoamingOI_Type.__name__ = "OctetString"
_CLHotspotRoamingOI_Object = MibTableColumn
cLHotspotRoamingOI = _CLHotspotRoamingOI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 2, 1, 1),
    _CLHotspotRoamingOI_Type()
)
cLHotspotRoamingOI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotRoamingOI.setStatus("current")
_CLHotspotRoamingOIRowStatus_Type = RowStatus
_CLHotspotRoamingOIRowStatus_Object = MibTableColumn
cLHotspotRoamingOIRowStatus = _CLHotspotRoamingOIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 2, 1, 2),
    _CLHotspotRoamingOIRowStatus_Type()
)
cLHotspotRoamingOIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRoamingOIRowStatus.setStatus("current")


class _CLHotspotRoamingOIIsBeacon_Type(TruthValue):
    """Custom type cLHotspotRoamingOIIsBeacon based on TruthValue"""
    defaultValue = 2


_CLHotspotRoamingOIIsBeacon_Type.__name__ = "TruthValue"
_CLHotspotRoamingOIIsBeacon_Object = MibTableColumn
cLHotspotRoamingOIIsBeacon = _CLHotspotRoamingOIIsBeacon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 2, 1, 3),
    _CLHotspotRoamingOIIsBeacon_Type()
)
cLHotspotRoamingOIIsBeacon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRoamingOIIsBeacon.setStatus("current")
_CLHotspotDomainNameTable_Object = MibTable
cLHotspotDomainNameTable = _CLHotspotDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLHotspotDomainNameTable.setStatus("current")
_CLHotspotDomainNameEntry_Object = MibTableRow
cLHotspotDomainNameEntry = _CLHotspotDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 3, 1)
)
cLHotspotDomainNameEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotDomainName"),
)
if mibBuilder.loadTexts:
    cLHotspotDomainNameEntry.setStatus("current")


class _CLHotspotDomainName_Type(SnmpAdminString):
    """Custom type cLHotspotDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotDomainName_Type.__name__ = "SnmpAdminString"
_CLHotspotDomainName_Object = MibTableColumn
cLHotspotDomainName = _CLHotspotDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 3, 1, 1),
    _CLHotspotDomainName_Type()
)
cLHotspotDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotDomainName.setStatus("current")
_CLHotspotDomainNameRowStatus_Type = RowStatus
_CLHotspotDomainNameRowStatus_Object = MibTableColumn
cLHotspotDomainNameRowStatus = _CLHotspotDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 3, 1, 2),
    _CLHotspotDomainNameRowStatus_Type()
)
cLHotspotDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotDomainNameRowStatus.setStatus("current")
_CLHotspot3gppTable_Object = MibTable
cLHotspot3gppTable = _CLHotspot3gppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cLHotspot3gppTable.setStatus("current")
_CLHotspot3gppEntry_Object = MibTableRow
cLHotspot3gppEntry = _CLHotspot3gppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 4, 1)
)
cLHotspot3gppEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspot3gppNetworkCode"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspot3gppCountryCode"),
)
if mibBuilder.loadTexts:
    cLHotspot3gppEntry.setStatus("current")


class _CLHotspot3gppNetworkCode_Type(OctetString):
    """Custom type cLHotspot3gppNetworkCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
    )


_CLHotspot3gppNetworkCode_Type.__name__ = "OctetString"
_CLHotspot3gppNetworkCode_Object = MibTableColumn
cLHotspot3gppNetworkCode = _CLHotspot3gppNetworkCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 4, 1, 1),
    _CLHotspot3gppNetworkCode_Type()
)
cLHotspot3gppNetworkCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspot3gppNetworkCode.setStatus("current")


class _CLHotspot3gppCountryCode_Type(OctetString):
    """Custom type cLHotspot3gppCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_CLHotspot3gppCountryCode_Type.__name__ = "OctetString"
_CLHotspot3gppCountryCode_Object = MibTableColumn
cLHotspot3gppCountryCode = _CLHotspot3gppCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 4, 1, 2),
    _CLHotspot3gppCountryCode_Type()
)
cLHotspot3gppCountryCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspot3gppCountryCode.setStatus("current")
_CLHotspot3gppRowStatus_Type = RowStatus
_CLHotspot3gppRowStatus_Object = MibTableColumn
cLHotspot3gppRowStatus = _CLHotspot3gppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 4, 1, 3),
    _CLHotspot3gppRowStatus_Type()
)
cLHotspot3gppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspot3gppRowStatus.setStatus("current")
_CLHotspotRealmTable_Object = MibTable
cLHotspotRealmTable = _CLHotspotRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cLHotspotRealmTable.setStatus("current")
_CLHotspotRealmEntry_Object = MibTableRow
cLHotspotRealmEntry = _CLHotspotRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 5, 1)
)
cLHotspotRealmEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmName"),
)
if mibBuilder.loadTexts:
    cLHotspotRealmEntry.setStatus("current")


class _CLHotspotRealmName_Type(SnmpAdminString):
    """Custom type cLHotspotRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotRealmName_Type.__name__ = "SnmpAdminString"
_CLHotspotRealmName_Object = MibTableColumn
cLHotspotRealmName = _CLHotspotRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 5, 1, 1),
    _CLHotspotRealmName_Type()
)
cLHotspotRealmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotRealmName.setStatus("current")
_CLHotspotRealmRowStatus_Type = RowStatus
_CLHotspotRealmRowStatus_Object = MibTableColumn
cLHotspotRealmRowStatus = _CLHotspotRealmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 5, 1, 2),
    _CLHotspotRealmRowStatus_Type()
)
cLHotspotRealmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmRowStatus.setStatus("current")
_CLHotspotRealmEAPTable_Object = MibTable
cLHotspotRealmEAPTable = _CLHotspotRealmEAPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cLHotspotRealmEAPTable.setStatus("current")
_CLHotspotRealmEAPEntry_Object = MibTableRow
cLHotspotRealmEAPEntry = _CLHotspotRealmEAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 6, 1)
)
cLHotspotRealmEAPEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPMethod"),
)
if mibBuilder.loadTexts:
    cLHotspotRealmEAPEntry.setStatus("current")


class _CLHotspotRealmEAPMethod_Type(Integer32):
    """Custom type cLHotspotRealmEAPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eapTLS", 1),
          ("eapLEAP", 2),
          ("eapSIM", 3),
          ("eapTTLS", 4),
          ("eapAKA", 5),
          ("eapPEAP", 6),
          ("eapFAST", 7))
    )


_CLHotspotRealmEAPMethod_Type.__name__ = "Integer32"
_CLHotspotRealmEAPMethod_Object = MibTableColumn
cLHotspotRealmEAPMethod = _CLHotspotRealmEAPMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 6, 1, 1),
    _CLHotspotRealmEAPMethod_Type()
)
cLHotspotRealmEAPMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPMethod.setStatus("current")
_CLHotspotRealmEAPRowStatus_Type = RowStatus
_CLHotspotRealmEAPRowStatus_Object = MibTableColumn
cLHotspotRealmEAPRowStatus = _CLHotspotRealmEAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 6, 1, 2),
    _CLHotspotRealmEAPRowStatus_Type()
)
cLHotspotRealmEAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPRowStatus.setStatus("current")
_CLHotspotRealmEAPAuthTable_Object = MibTable
cLHotspotRealmEAPAuthTable = _CLHotspotRealmEAPAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthTable.setStatus("deprecated")
_CLHotspotRealmEAPAuthEntry_Object = MibTableRow
cLHotspotRealmEAPAuthEntry = _CLHotspotRealmEAPAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1)
)
cLHotspotRealmEAPAuthEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPMethod"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPAuthMethod"),
)
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthEntry.setStatus("deprecated")


class _CLHotspotRealmEAPAuthMethod_Type(Integer32):
    """Custom type cLHotspotRealmEAPAuthMethod based on Integer32"""
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
        *(("innerAuthNonEap", 1),
          ("innerAuthEap", 2),
          ("credential", 3),
          ("tunneledEapCredential", 4))
    )


_CLHotspotRealmEAPAuthMethod_Type.__name__ = "Integer32"
_CLHotspotRealmEAPAuthMethod_Object = MibTableColumn
cLHotspotRealmEAPAuthMethod = _CLHotspotRealmEAPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1, 1),
    _CLHotspotRealmEAPAuthMethod_Type()
)
cLHotspotRealmEAPAuthMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthMethod.setStatus("deprecated")
_CLHotspotRealmEAPAuthRowStatus_Type = RowStatus
_CLHotspotRealmEAPAuthRowStatus_Object = MibTableColumn
cLHotspotRealmEAPAuthRowStatus = _CLHotspotRealmEAPAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1, 2),
    _CLHotspotRealmEAPAuthRowStatus_Type()
)
cLHotspotRealmEAPAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthRowStatus.setStatus("deprecated")


class _CLHotspotRealmEAPAuthInnerAuthEAPType_Type(Integer32):
    """Custom type cLHotspotRealmEAPAuthInnerAuthEAPType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("eapTLS", 2),
          ("eapLEAP", 3),
          ("eapSIM", 4),
          ("eapTTLS", 5),
          ("eapAKA", 6),
          ("eapPEAP", 7),
          ("eapFAST", 8))
    )


_CLHotspotRealmEAPAuthInnerAuthEAPType_Type.__name__ = "Integer32"
_CLHotspotRealmEAPAuthInnerAuthEAPType_Object = MibTableColumn
cLHotspotRealmEAPAuthInnerAuthEAPType = _CLHotspotRealmEAPAuthInnerAuthEAPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1, 3),
    _CLHotspotRealmEAPAuthInnerAuthEAPType_Type()
)
cLHotspotRealmEAPAuthInnerAuthEAPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthInnerAuthEAPType.setStatus("deprecated")


class _CLHotspotRealmEAPAuthNonInnerAuthEAPType_Type(Integer32):
    """Custom type cLHotspotRealmEAPAuthNonInnerAuthEAPType based on Integer32"""
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
        *(("reserved", 1),
          ("pap", 2),
          ("chap", 3),
          ("mschap", 4),
          ("mschapV2", 5))
    )


_CLHotspotRealmEAPAuthNonInnerAuthEAPType_Type.__name__ = "Integer32"
_CLHotspotRealmEAPAuthNonInnerAuthEAPType_Object = MibTableColumn
cLHotspotRealmEAPAuthNonInnerAuthEAPType = _CLHotspotRealmEAPAuthNonInnerAuthEAPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1, 4),
    _CLHotspotRealmEAPAuthNonInnerAuthEAPType_Type()
)
cLHotspotRealmEAPAuthNonInnerAuthEAPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthNonInnerAuthEAPType.setStatus("deprecated")


class _CLHotspotRealmEAPAuthCredentialType_Type(Integer32):
    """Custom type cLHotspotRealmEAPAuthCredentialType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("sim", 2),
          ("usim", 3),
          ("nfc", 4),
          ("hwToken", 5),
          ("softoken", 6),
          ("certificate", 7),
          ("usernamePassword", 8),
          ("none", 9))
    )


_CLHotspotRealmEAPAuthCredentialType_Type.__name__ = "Integer32"
_CLHotspotRealmEAPAuthCredentialType_Object = MibTableColumn
cLHotspotRealmEAPAuthCredentialType = _CLHotspotRealmEAPAuthCredentialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1, 5),
    _CLHotspotRealmEAPAuthCredentialType_Type()
)
cLHotspotRealmEAPAuthCredentialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthCredentialType.setStatus("deprecated")


class _CLHotspotRealmEAPAuthTunneledEAPCredentialType_Type(Integer32):
    """Custom type cLHotspotRealmEAPAuthTunneledEAPCredentialType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("sim", 2),
          ("usim", 3),
          ("nfc", 4),
          ("hwToken", 5),
          ("softoken", 6),
          ("certificate", 7),
          ("usernamePassword", 8),
          ("anonymous", 9))
    )


_CLHotspotRealmEAPAuthTunneledEAPCredentialType_Type.__name__ = "Integer32"
_CLHotspotRealmEAPAuthTunneledEAPCredentialType_Object = MibTableColumn
cLHotspotRealmEAPAuthTunneledEAPCredentialType = _CLHotspotRealmEAPAuthTunneledEAPCredentialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 7, 1, 6),
    _CLHotspotRealmEAPAuthTunneledEAPCredentialType_Type()
)
cLHotspotRealmEAPAuthTunneledEAPCredentialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotRealmEAPAuthTunneledEAPCredentialType.setStatus("deprecated")
_CLHotspotConnectionCapabilityTable_Object = MibTable
cLHotspotConnectionCapabilityTable = _CLHotspotConnectionCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cLHotspotConnectionCapabilityTable.setStatus("current")
_CLHotspotConnectionCapabilityEntry_Object = MibTableRow
cLHotspotConnectionCapabilityEntry = _CLHotspotConnectionCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 8, 1)
)
cLHotspotConnectionCapabilityEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotConnectionCapabilityProtocol"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotConnectionCapabilityPort"),
)
if mibBuilder.loadTexts:
    cLHotspotConnectionCapabilityEntry.setStatus("current")


class _CLHotspotConnectionCapabilityProtocol_Type(Unsigned32):
    """Custom type cLHotspotConnectionCapabilityProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CLHotspotConnectionCapabilityProtocol_Type.__name__ = "Unsigned32"
_CLHotspotConnectionCapabilityProtocol_Object = MibTableColumn
cLHotspotConnectionCapabilityProtocol = _CLHotspotConnectionCapabilityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 8, 1, 1),
    _CLHotspotConnectionCapabilityProtocol_Type()
)
cLHotspotConnectionCapabilityProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotConnectionCapabilityProtocol.setStatus("current")


class _CLHotspotConnectionCapabilityPort_Type(Unsigned32):
    """Custom type cLHotspotConnectionCapabilityPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLHotspotConnectionCapabilityPort_Type.__name__ = "Unsigned32"
_CLHotspotConnectionCapabilityPort_Object = MibTableColumn
cLHotspotConnectionCapabilityPort = _CLHotspotConnectionCapabilityPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 8, 1, 2),
    _CLHotspotConnectionCapabilityPort_Type()
)
cLHotspotConnectionCapabilityPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotConnectionCapabilityPort.setStatus("current")
_CLHotspotConnectionCapabilityRowStatus_Type = RowStatus
_CLHotspotConnectionCapabilityRowStatus_Object = MibTableColumn
cLHotspotConnectionCapabilityRowStatus = _CLHotspotConnectionCapabilityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 8, 1, 3),
    _CLHotspotConnectionCapabilityRowStatus_Type()
)
cLHotspotConnectionCapabilityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotConnectionCapabilityRowStatus.setStatus("current")


class _CLHotspotConnectionCapabilityStatus_Type(Integer32):
    """Custom type cLHotspotConnectionCapabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2),
          ("unknown", 3))
    )


_CLHotspotConnectionCapabilityStatus_Type.__name__ = "Integer32"
_CLHotspotConnectionCapabilityStatus_Object = MibTableColumn
cLHotspotConnectionCapabilityStatus = _CLHotspotConnectionCapabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 8, 1, 4),
    _CLHotspotConnectionCapabilityStatus_Type()
)
cLHotspotConnectionCapabilityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotConnectionCapabilityStatus.setStatus("current")
_CLHotspotOperatorNameTable_Object = MibTable
cLHotspotOperatorNameTable = _CLHotspotOperatorNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cLHotspotOperatorNameTable.setStatus("current")
_CLHotspotOperatorNameEntry_Object = MibTableRow
cLHotspotOperatorNameEntry = _CLHotspotOperatorNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 9, 1)
)
cLHotspotOperatorNameEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatorNameLanguage"),
)
if mibBuilder.loadTexts:
    cLHotspotOperatorNameEntry.setStatus("current")


class _CLHotspotOperatorNameLanguage_Type(SnmpAdminString):
    """Custom type cLHotspotOperatorNameLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_CLHotspotOperatorNameLanguage_Type.__name__ = "SnmpAdminString"
_CLHotspotOperatorNameLanguage_Object = MibTableColumn
cLHotspotOperatorNameLanguage = _CLHotspotOperatorNameLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 9, 1, 1),
    _CLHotspotOperatorNameLanguage_Type()
)
cLHotspotOperatorNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotOperatorNameLanguage.setStatus("current")
_CLHotspotOperatorNameRowStatus_Type = RowStatus
_CLHotspotOperatorNameRowStatus_Object = MibTableColumn
cLHotspotOperatorNameRowStatus = _CLHotspotOperatorNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 9, 1, 2),
    _CLHotspotOperatorNameRowStatus_Type()
)
cLHotspotOperatorNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOperatorNameRowStatus.setStatus("current")


class _CLHotspotOperatorName_Type(SnmpAdminString):
    """Custom type cLHotspotOperatorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_CLHotspotOperatorName_Type.__name__ = "SnmpAdminString"
_CLHotspotOperatorName_Object = MibTableColumn
cLHotspotOperatorName = _CLHotspotOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 9, 1, 3),
    _CLHotspotOperatorName_Type()
)
cLHotspotOperatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOperatorName.setStatus("current")
_CLHotspotOsuProviderTable_Object = MibTable
cLHotspotOsuProviderTable = _CLHotspotOsuProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cLHotspotOsuProviderTable.setStatus("current")
_CLHotspotOsuProviderEntry_Object = MibTableRow
cLHotspotOsuProviderEntry = _CLHotspotOsuProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1)
)
cLHotspotOsuProviderEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderName"),
)
if mibBuilder.loadTexts:
    cLHotspotOsuProviderEntry.setStatus("current")


class _CLHotspotOsuProviderName_Type(SnmpAdminString):
    """Custom type cLHotspotOsuProviderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotOsuProviderName_Type.__name__ = "SnmpAdminString"
_CLHotspotOsuProviderName_Object = MibTableColumn
cLHotspotOsuProviderName = _CLHotspotOsuProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1, 1),
    _CLHotspotOsuProviderName_Type()
)
cLHotspotOsuProviderName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderName.setStatus("current")
_CLHotspotOsuProviderRowStatus_Type = RowStatus
_CLHotspotOsuProviderRowStatus_Object = MibTableColumn
cLHotspotOsuProviderRowStatus = _CLHotspotOsuProviderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1, 2),
    _CLHotspotOsuProviderRowStatus_Type()
)
cLHotspotOsuProviderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderRowStatus.setStatus("current")
_CLHotspotOsuProviderServerUri_Type = SnmpAdminString
_CLHotspotOsuProviderServerUri_Object = MibTableColumn
cLHotspotOsuProviderServerUri = _CLHotspotOsuProviderServerUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1, 3),
    _CLHotspotOsuProviderServerUri_Type()
)
cLHotspotOsuProviderServerUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderServerUri.setStatus("current")
_CLHotspotOsuProviderNai_Type = SnmpAdminString
_CLHotspotOsuProviderNai_Object = MibTableColumn
cLHotspotOsuProviderNai = _CLHotspotOsuProviderNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1, 4),
    _CLHotspotOsuProviderNai_Type()
)
cLHotspotOsuProviderNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderNai.setStatus("current")


class _CLHotspotOsuProviderPrimaryMethod_Type(Integer32):
    """Custom type cLHotspotOsuProviderPrimaryMethod based on Integer32"""
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
          ("omaDm", 2),
          ("soapXmlSpp", 3))
    )


_CLHotspotOsuProviderPrimaryMethod_Type.__name__ = "Integer32"
_CLHotspotOsuProviderPrimaryMethod_Object = MibTableColumn
cLHotspotOsuProviderPrimaryMethod = _CLHotspotOsuProviderPrimaryMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1, 5),
    _CLHotspotOsuProviderPrimaryMethod_Type()
)
cLHotspotOsuProviderPrimaryMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderPrimaryMethod.setStatus("current")


class _CLHotspotOsuProviderSecondaryMethod_Type(Integer32):
    """Custom type cLHotspotOsuProviderSecondaryMethod based on Integer32"""
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
          ("omaDm", 2),
          ("soapXmlSpp", 3))
    )


_CLHotspotOsuProviderSecondaryMethod_Type.__name__ = "Integer32"
_CLHotspotOsuProviderSecondaryMethod_Object = MibTableColumn
cLHotspotOsuProviderSecondaryMethod = _CLHotspotOsuProviderSecondaryMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 10, 1, 6),
    _CLHotspotOsuProviderSecondaryMethod_Type()
)
cLHotspotOsuProviderSecondaryMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderSecondaryMethod.setStatus("current")
_CLHotspotOsuProviderFriendlyNameTable_Object = MibTable
cLHotspotOsuProviderFriendlyNameTable = _CLHotspotOsuProviderFriendlyNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cLHotspotOsuProviderFriendlyNameTable.setStatus("current")
_CLHotspotOsuProviderFriendlyNameEntry_Object = MibTableRow
cLHotspotOsuProviderFriendlyNameEntry = _CLHotspotOsuProviderFriendlyNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 11, 1)
)
cLHotspotOsuProviderFriendlyNameEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyNameLanguage"),
)
if mibBuilder.loadTexts:
    cLHotspotOsuProviderFriendlyNameEntry.setStatus("current")


class _CLHotspotOsuProviderFriendlyNameLanguage_Type(SnmpAdminString):
    """Custom type cLHotspotOsuProviderFriendlyNameLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_CLHotspotOsuProviderFriendlyNameLanguage_Type.__name__ = "SnmpAdminString"
_CLHotspotOsuProviderFriendlyNameLanguage_Object = MibTableColumn
cLHotspotOsuProviderFriendlyNameLanguage = _CLHotspotOsuProviderFriendlyNameLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 11, 1, 1),
    _CLHotspotOsuProviderFriendlyNameLanguage_Type()
)
cLHotspotOsuProviderFriendlyNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderFriendlyNameLanguage.setStatus("current")
_CLHotspotOsuProviderFriendlyNameRowStatus_Type = RowStatus
_CLHotspotOsuProviderFriendlyNameRowStatus_Object = MibTableColumn
cLHotspotOsuProviderFriendlyNameRowStatus = _CLHotspotOsuProviderFriendlyNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 11, 1, 2),
    _CLHotspotOsuProviderFriendlyNameRowStatus_Type()
)
cLHotspotOsuProviderFriendlyNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderFriendlyNameRowStatus.setStatus("current")


class _CLHotspotOsuProviderFriendlyName_Type(SnmpAdminString):
    """Custom type cLHotspotOsuProviderFriendlyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotOsuProviderFriendlyName_Type.__name__ = "SnmpAdminString"
_CLHotspotOsuProviderFriendlyName_Object = MibTableColumn
cLHotspotOsuProviderFriendlyName = _CLHotspotOsuProviderFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 11, 1, 3),
    _CLHotspotOsuProviderFriendlyName_Type()
)
cLHotspotOsuProviderFriendlyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderFriendlyName.setStatus("current")
_CLHotspotOsuProviderFriendlyNameDescription_Type = SnmpAdminString
_CLHotspotOsuProviderFriendlyNameDescription_Object = MibTableColumn
cLHotspotOsuProviderFriendlyNameDescription = _CLHotspotOsuProviderFriendlyNameDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 11, 1, 4),
    _CLHotspotOsuProviderFriendlyNameDescription_Type()
)
cLHotspotOsuProviderFriendlyNameDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderFriendlyNameDescription.setStatus("current")
_CLHotspotOsuProviderIconTable_Object = MibTable
cLHotspotOsuProviderIconTable = _CLHotspotOsuProviderIconTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cLHotspotOsuProviderIconTable.setStatus("current")
_CLHotspotOsuProviderIconEntry_Object = MibTableRow
cLHotspotOsuProviderIconEntry = _CLHotspotOsuProviderIconEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 12, 1)
)
cLHotspotOsuProviderIconEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderIconFileName"),
)
if mibBuilder.loadTexts:
    cLHotspotOsuProviderIconEntry.setStatus("current")


class _CLHotspotOsuProviderIconFileName_Type(SnmpAdminString):
    """Custom type cLHotspotOsuProviderIconFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotOsuProviderIconFileName_Type.__name__ = "SnmpAdminString"
_CLHotspotOsuProviderIconFileName_Object = MibTableColumn
cLHotspotOsuProviderIconFileName = _CLHotspotOsuProviderIconFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 12, 1, 1),
    _CLHotspotOsuProviderIconFileName_Type()
)
cLHotspotOsuProviderIconFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderIconFileName.setStatus("current")
_CLHotspotOsuProviderIconRowStatus_Type = RowStatus
_CLHotspotOsuProviderIconRowStatus_Object = MibTableColumn
cLHotspotOsuProviderIconRowStatus = _CLHotspotOsuProviderIconRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 12, 1, 2),
    _CLHotspotOsuProviderIconRowStatus_Type()
)
cLHotspotOsuProviderIconRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOsuProviderIconRowStatus.setStatus("current")
_CLHotspotOperatingClassTable_Object = MibTable
cLHotspotOperatingClassTable = _CLHotspotOperatingClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cLHotspotOperatingClassTable.setStatus("current")
_CLHotspotOperatingClassEntry_Object = MibTableRow
cLHotspotOperatingClassEntry = _CLHotspotOperatingClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 13, 1)
)
cLHotspotOperatingClassEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatingClassId"),
)
if mibBuilder.loadTexts:
    cLHotspotOperatingClassEntry.setStatus("current")


class _CLHotspotOperatingClassId_Type(Unsigned32):
    """Custom type cLHotspotOperatingClassId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CLHotspotOperatingClassId_Type.__name__ = "Unsigned32"
_CLHotspotOperatingClassId_Object = MibTableColumn
cLHotspotOperatingClassId = _CLHotspotOperatingClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 13, 1, 1),
    _CLHotspotOperatingClassId_Type()
)
cLHotspotOperatingClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotOperatingClassId.setStatus("current")
_CLHotspotOperatingClassRowStatus_Type = RowStatus
_CLHotspotOperatingClassRowStatus_Object = MibTableColumn
cLHotspotOperatingClassRowStatus = _CLHotspotOperatingClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 13, 1, 2),
    _CLHotspotOperatingClassRowStatus_Type()
)
cLHotspotOperatingClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotOperatingClassRowStatus.setStatus("current")
_CLHotspotIconTable_Object = MibTable
cLHotspotIconTable = _CLHotspotIconTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cLHotspotIconTable.setStatus("current")
_CLHotspotIconEntry_Object = MibTableRow
cLHotspotIconEntry = _CLHotspotIconEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1)
)
cLHotspotIconEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconFileName"),
)
if mibBuilder.loadTexts:
    cLHotspotIconEntry.setStatus("current")


class _CLHotspotIconFileName_Type(SnmpAdminString):
    """Custom type cLHotspotIconFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotIconFileName_Type.__name__ = "SnmpAdminString"
_CLHotspotIconFileName_Object = MibTableColumn
cLHotspotIconFileName = _CLHotspotIconFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 1),
    _CLHotspotIconFileName_Type()
)
cLHotspotIconFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotIconFileName.setStatus("current")
_CLHotspotIconRowStatus_Type = RowStatus
_CLHotspotIconRowStatus_Object = MibTableColumn
cLHotspotIconRowStatus = _CLHotspotIconRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 2),
    _CLHotspotIconRowStatus_Type()
)
cLHotspotIconRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotIconRowStatus.setStatus("current")


class _CLHotspotIconPath_Type(SnmpAdminString):
    """Custom type cLHotspotIconPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(9, 9),
    )


_CLHotspotIconPath_Type.__name__ = "SnmpAdminString"
_CLHotspotIconPath_Object = MibTableColumn
cLHotspotIconPath = _CLHotspotIconPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 3),
    _CLHotspotIconPath_Type()
)
cLHotspotIconPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotIconPath.setStatus("current")


class _CLHotspotIconType_Type(SnmpAdminString):
    """Custom type cLHotspotIconType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLHotspotIconType_Type.__name__ = "SnmpAdminString"
_CLHotspotIconType_Object = MibTableColumn
cLHotspotIconType = _CLHotspotIconType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 4),
    _CLHotspotIconType_Type()
)
cLHotspotIconType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotIconType.setStatus("current")


class _CLHotspotIconLanguage_Type(SnmpAdminString):
    """Custom type cLHotspotIconLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_CLHotspotIconLanguage_Type.__name__ = "SnmpAdminString"
_CLHotspotIconLanguage_Object = MibTableColumn
cLHotspotIconLanguage = _CLHotspotIconLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 5),
    _CLHotspotIconLanguage_Type()
)
cLHotspotIconLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotIconLanguage.setStatus("current")


class _CLHotspotIconWidth_Type(Unsigned32):
    """Custom type cLHotspotIconWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLHotspotIconWidth_Type.__name__ = "Unsigned32"
_CLHotspotIconWidth_Object = MibTableColumn
cLHotspotIconWidth = _CLHotspotIconWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 6),
    _CLHotspotIconWidth_Type()
)
cLHotspotIconWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotIconWidth.setStatus("current")


class _CLHotspotIconHeight_Type(Unsigned32):
    """Custom type cLHotspotIconHeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLHotspotIconHeight_Type.__name__ = "Unsigned32"
_CLHotspotIconHeight_Object = MibTableColumn
cLHotspotIconHeight = _CLHotspotIconHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 14, 1, 7),
    _CLHotspotIconHeight_Type()
)
cLHotspotIconHeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotIconHeight.setStatus("current")
_CLHotspotVenueNameTable_Object = MibTable
cLHotspotVenueNameTable = _CLHotspotVenueNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cLHotspotVenueNameTable.setStatus("current")
_CLHotspotVenueNameEntry_Object = MibTableRow
cLHotspotVenueNameEntry = _CLHotspotVenueNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 15, 1)
)
cLHotspotVenueNameEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameLanguage"),
)
if mibBuilder.loadTexts:
    cLHotspotVenueNameEntry.setStatus("current")


class _CLHotspotVenueNameLanguage_Type(SnmpAdminString):
    """Custom type cLHotspotVenueNameLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_CLHotspotVenueNameLanguage_Type.__name__ = "SnmpAdminString"
_CLHotspotVenueNameLanguage_Object = MibTableColumn
cLHotspotVenueNameLanguage = _CLHotspotVenueNameLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 15, 1, 1),
    _CLHotspotVenueNameLanguage_Type()
)
cLHotspotVenueNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotVenueNameLanguage.setStatus("current")
_CLHotspotVenueNameRowStatus_Type = RowStatus
_CLHotspotVenueNameRowStatus_Object = MibTableColumn
cLHotspotVenueNameRowStatus = _CLHotspotVenueNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 15, 1, 2),
    _CLHotspotVenueNameRowStatus_Type()
)
cLHotspotVenueNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotVenueNameRowStatus.setStatus("current")


class _CLHotspotVenueNameDescription_Type(SnmpAdminString):
    """Custom type cLHotspotVenueNameDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_CLHotspotVenueNameDescription_Type.__name__ = "SnmpAdminString"
_CLHotspotVenueNameDescription_Object = MibTableColumn
cLHotspotVenueNameDescription = _CLHotspotVenueNameDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 15, 1, 3),
    _CLHotspotVenueNameDescription_Type()
)
cLHotspotVenueNameDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotVenueNameDescription.setStatus("current")
_CLHotspotVenueNameUrl_Type = SnmpAdminString
_CLHotspotVenueNameUrl_Object = MibTableColumn
cLHotspotVenueNameUrl = _CLHotspotVenueNameUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 15, 1, 4),
    _CLHotspotVenueNameUrl_Type()
)
cLHotspotVenueNameUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotVenueNameUrl.setStatus("current")
_CLHotspotNetworkAuthTable_Object = MibTable
cLHotspotNetworkAuthTable = _CLHotspotNetworkAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cLHotspotNetworkAuthTable.setStatus("current")
_CLHotspotNetworkAuthEntry_Object = MibTableRow
cLHotspotNetworkAuthEntry = _CLHotspotNetworkAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 16, 1)
)
cLHotspotNetworkAuthEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotNetworkAuthType"),
)
if mibBuilder.loadTexts:
    cLHotspotNetworkAuthEntry.setStatus("current")


class _CLHotspotNetworkAuthType_Type(Integer32):
    """Custom type cLHotspotNetworkAuthType based on Integer32"""
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
        *(("termsAndConditions", 1),
          ("onlineEnrollment", 2),
          ("httpHttpsRedirect", 3),
          ("dnsRedirect", 4))
    )


_CLHotspotNetworkAuthType_Type.__name__ = "Integer32"
_CLHotspotNetworkAuthType_Object = MibTableColumn
cLHotspotNetworkAuthType = _CLHotspotNetworkAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 16, 1, 1),
    _CLHotspotNetworkAuthType_Type()
)
cLHotspotNetworkAuthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotNetworkAuthType.setStatus("current")
_CLHotspotNetworkAuthRowStatus_Type = RowStatus
_CLHotspotNetworkAuthRowStatus_Object = MibTableColumn
cLHotspotNetworkAuthRowStatus = _CLHotspotNetworkAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 16, 1, 2),
    _CLHotspotNetworkAuthRowStatus_Type()
)
cLHotspotNetworkAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotNetworkAuthRowStatus.setStatus("current")
_CLHotspotNetworkAuthUrl_Type = SnmpAdminString
_CLHotspotNetworkAuthUrl_Object = MibTableColumn
cLHotspotNetworkAuthUrl = _CLHotspotNetworkAuthUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 16, 1, 3),
    _CLHotspotNetworkAuthUrl_Type()
)
cLHotspotNetworkAuthUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotNetworkAuthUrl.setStatus("current")
_CLHotspotAdviceChargeTable_Object = MibTable
cLHotspotAdviceChargeTable = _CLHotspotAdviceChargeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeTable.setStatus("current")
_CLHotspotAdviceChargeEntry_Object = MibTableRow
cLHotspotAdviceChargeEntry = _CLHotspotAdviceChargeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 17, 1)
)
cLHotspotAdviceChargeEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargeType"),
)
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeEntry.setStatus("current")


class _CLHotspotAdviceChargeType_Type(Integer32):
    """Custom type cLHotspotAdviceChargeType based on Integer32"""
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
        *(("time", 1),
          ("data", 2),
          ("timeAndData", 3),
          ("unlimited", 4))
    )


_CLHotspotAdviceChargeType_Type.__name__ = "Integer32"
_CLHotspotAdviceChargeType_Object = MibTableColumn
cLHotspotAdviceChargeType = _CLHotspotAdviceChargeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 17, 1, 1),
    _CLHotspotAdviceChargeType_Type()
)
cLHotspotAdviceChargeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeType.setStatus("current")
_CLHotspotAdviceChargeRowStatus_Type = RowStatus
_CLHotspotAdviceChargeRowStatus_Object = MibTableColumn
cLHotspotAdviceChargeRowStatus = _CLHotspotAdviceChargeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 17, 1, 2),
    _CLHotspotAdviceChargeRowStatus_Type()
)
cLHotspotAdviceChargeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeRowStatus.setStatus("current")
_CLHotspotAdviceChargePlanInfoTable_Object = MibTable
cLHotspotAdviceChargePlanInfoTable = _CLHotspotAdviceChargePlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoTable.setStatus("current")
_CLHotspotAdviceChargePlanInfoEntry_Object = MibTableRow
cLHotspotAdviceChargePlanInfoEntry = _CLHotspotAdviceChargePlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18, 1)
)
cLHotspotAdviceChargePlanInfoEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargeType"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargePlanInfoFilename"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargePlanInfoPath"),
)
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoEntry.setStatus("current")


class _CLHotspotAdviceChargePlanInfoFilename_Type(SnmpAdminString):
    """Custom type cLHotspotAdviceChargePlanInfoFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 220),
    )


_CLHotspotAdviceChargePlanInfoFilename_Type.__name__ = "SnmpAdminString"
_CLHotspotAdviceChargePlanInfoFilename_Object = MibTableColumn
cLHotspotAdviceChargePlanInfoFilename = _CLHotspotAdviceChargePlanInfoFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18, 1, 1),
    _CLHotspotAdviceChargePlanInfoFilename_Type()
)
cLHotspotAdviceChargePlanInfoFilename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoFilename.setStatus("current")


class _CLHotspotAdviceChargePlanInfoPath_Type(SnmpAdminString):
    """Custom type cLHotspotAdviceChargePlanInfoPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 231),
    )


_CLHotspotAdviceChargePlanInfoPath_Type.__name__ = "SnmpAdminString"
_CLHotspotAdviceChargePlanInfoPath_Object = MibTableColumn
cLHotspotAdviceChargePlanInfoPath = _CLHotspotAdviceChargePlanInfoPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18, 1, 2),
    _CLHotspotAdviceChargePlanInfoPath_Type()
)
cLHotspotAdviceChargePlanInfoPath.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoPath.setStatus("current")
_CLHotspotAdviceChargePlanInfoRowStatus_Type = RowStatus
_CLHotspotAdviceChargePlanInfoRowStatus_Object = MibTableColumn
cLHotspotAdviceChargePlanInfoRowStatus = _CLHotspotAdviceChargePlanInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18, 1, 3),
    _CLHotspotAdviceChargePlanInfoRowStatus_Type()
)
cLHotspotAdviceChargePlanInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoRowStatus.setStatus("current")


class _CLHotspotAdviceChargePlanInfoLanguage_Type(SnmpAdminString):
    """Custom type cLHotspotAdviceChargePlanInfoLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_CLHotspotAdviceChargePlanInfoLanguage_Type.__name__ = "SnmpAdminString"
_CLHotspotAdviceChargePlanInfoLanguage_Object = MibTableColumn
cLHotspotAdviceChargePlanInfoLanguage = _CLHotspotAdviceChargePlanInfoLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18, 1, 4),
    _CLHotspotAdviceChargePlanInfoLanguage_Type()
)
cLHotspotAdviceChargePlanInfoLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoLanguage.setStatus("current")


class _CLHotspotAdviceChargePlanInfoCurrency_Type(SnmpAdminString):
    """Custom type cLHotspotAdviceChargePlanInfoCurrency based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_CLHotspotAdviceChargePlanInfoCurrency_Type.__name__ = "SnmpAdminString"
_CLHotspotAdviceChargePlanInfoCurrency_Object = MibTableColumn
cLHotspotAdviceChargePlanInfoCurrency = _CLHotspotAdviceChargePlanInfoCurrency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 18, 1, 5),
    _CLHotspotAdviceChargePlanInfoCurrency_Type()
)
cLHotspotAdviceChargePlanInfoCurrency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargePlanInfoCurrency.setStatus("current")
_CLHotspotAdviceChargeNAIRealmTable_Object = MibTable
cLHotspotAdviceChargeNAIRealmTable = _CLHotspotAdviceChargeNAIRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeNAIRealmTable.setStatus("current")
_CLHotspotAdviceChargeNAIRealmEntry_Object = MibTableRow
cLHotspotAdviceChargeNAIRealmEntry = _CLHotspotAdviceChargeNAIRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 19, 1)
)
cLHotspotAdviceChargeNAIRealmEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargeType"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargeNAIRealmName"),
)
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeNAIRealmEntry.setStatus("current")


class _CLHotspotAdviceChargeNAIRealmName_Type(SnmpAdminString):
    """Custom type cLHotspotAdviceChargeNAIRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 220),
    )


_CLHotspotAdviceChargeNAIRealmName_Type.__name__ = "SnmpAdminString"
_CLHotspotAdviceChargeNAIRealmName_Object = MibTableColumn
cLHotspotAdviceChargeNAIRealmName = _CLHotspotAdviceChargeNAIRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 19, 1, 1),
    _CLHotspotAdviceChargeNAIRealmName_Type()
)
cLHotspotAdviceChargeNAIRealmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeNAIRealmName.setStatus("current")
_CLHotspotAdviceChargeNAIRealmRowStatus_Type = RowStatus
_CLHotspotAdviceChargeNAIRealmRowStatus_Object = MibTableColumn
cLHotspotAdviceChargeNAIRealmRowStatus = _CLHotspotAdviceChargeNAIRealmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 19, 1, 2),
    _CLHotspotAdviceChargeNAIRealmRowStatus_Type()
)
cLHotspotAdviceChargeNAIRealmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotAdviceChargeNAIRealmRowStatus.setStatus("current")
_CLHotspotEAPAuthTable_Object = MibTable
cLHotspotEAPAuthTable = _CLHotspotEAPAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cLHotspotEAPAuthTable.setStatus("current")
_CLHotspotEAPAuthEntry_Object = MibTableRow
cLHotspotEAPAuthEntry = _CLHotspotEAPAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 20, 1)
)
cLHotspotEAPAuthEntry.setIndexNames(
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmName"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPMethod"),
    (0, "CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotEAPAuthType"),
)
if mibBuilder.loadTexts:
    cLHotspotEAPAuthEntry.setStatus("current")


class _CLHotspotEAPAuthType_Type(Integer32):
    """Custom type cLHotspotEAPAuthType based on Integer32"""
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
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("innerAuthPap", 1),
          ("innerAuthChap", 2),
          ("innerAuthMschap", 3),
          ("innerAuthMschapv2", 4),
          ("innerAuthEapTls", 5),
          ("innerAuthEapLeap", 6),
          ("innerAuthEapSim", 7),
          ("innerAuthEapTtls", 8),
          ("innerAuthEapAka", 9),
          ("innerAuthEapPeap", 10),
          ("innerAuthEapFast", 11),
          ("credentialSim", 12),
          ("credentialUsim", 13),
          ("credentialNfc", 14),
          ("credentialHwToken", 15),
          ("credentialSoftoken", 16),
          ("credentialCertificate", 17),
          ("credentialUsernamePassword", 18),
          ("credentialNone", 19),
          ("tunneledEapCredentialSim", 20),
          ("tunneledEapCredentialUsim", 21),
          ("tunneledEapCredentialNfc", 22),
          ("tunneledEapCredentialHwToken", 23),
          ("tunneledEapCredentialSoftoken", 24),
          ("tunneledEapCredentialCertificate", 25),
          ("tunneledEapCredentialUsernamePassword", 26),
          ("tunneledEapCredentialAnonymous", 27))
    )


_CLHotspotEAPAuthType_Type.__name__ = "Integer32"
_CLHotspotEAPAuthType_Object = MibTableColumn
cLHotspotEAPAuthType = _CLHotspotEAPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 20, 1, 1),
    _CLHotspotEAPAuthType_Type()
)
cLHotspotEAPAuthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHotspotEAPAuthType.setStatus("current")
_CLHotspotEAPAuthRowStatus_Type = RowStatus
_CLHotspotEAPAuthRowStatus_Object = MibTableColumn
cLHotspotEAPAuthRowStatus = _CLHotspotEAPAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 1, 1, 20, 1, 2),
    _CLHotspotEAPAuthRowStatus_Type()
)
cLHotspotEAPAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHotspotEAPAuthRowStatus.setStatus("current")
_CiscoWirelessHotspotMIBConform_ObjectIdentity = ObjectIdentity
ciscoWirelessHotspotMIBConform = _CiscoWirelessHotspotMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2)
)
_CiscoWirelessHotspotCompliances_ObjectIdentity = ObjectIdentity
ciscoWirelessHotspotCompliances = _CiscoWirelessHotspotCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 1)
)
_CiscoWirelessHotspotGroups_ObjectIdentity = ObjectIdentity
ciscoWirelessHotspotGroups = _CiscoWirelessHotspotGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 2)
)

# Managed Objects groups

ciscoWirelessHotspotConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 2, 1)
)
ciscoWirelessHotspotConfigGroup1.setObjects(
      *(("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerDescription"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerInternetEnabled"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerNetworkType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerVenueType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerHessid"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotGasRequestTimeout"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpFragmentationThreshold"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpDomainId"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpDomainIdEnabled"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerIpv4AddressType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerIpv6AddressType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpOsuSsid"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanLinkStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanIsAtCapacity"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanDownlinkSpeed"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanUplinkSpeed"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanDownlinkLoad"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanUplinkLoad"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanLoadMeasDuration"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRoamingOIIsBeacon"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRoamingOIRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotDomainNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspot3gppRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPAuthInnerAuthEAPType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPAuthNonInnerAuthEAPType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPAuthCredentialType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPAuthTunneledEAPCredentialType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPAuthRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotConnectionCapabilityStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotConnectionCapabilityRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatorName"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatorNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderServerUri"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderNai"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderPrimaryMethod"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderSecondaryMethod"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyName"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyNameDescription"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderIconRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatingClassRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameDescription"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameUrl"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotNetworkAuthUrl"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotNetworkAuthRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWirelessHotspotConfigGroup1.setStatus("deprecated")

ciscoWirelessHotspotConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 2, 2)
)
ciscoWirelessHotspotConfigGroup2.setObjects(
      *(("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconPath"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconLanguage"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconWidth"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconHeight"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotIconRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWirelessHotspotConfigGroup2.setStatus("current")

ciscoWirelessHotspotConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 2, 3)
)
ciscoWirelessHotspotConfigGroup3.setObjects(
      *(("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerDescription"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerInternetEnabled"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerNetworkType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerVenueType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerHessid"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotGasRequestTimeout"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpFragmentationThreshold"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpDomainId"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpDomainIdEnabled"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerIpv4AddressType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerIpv6AddressType"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpOsuSsid"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanLinkStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanIsAtCapacity"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanDownlinkSpeed"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanUplinkSpeed"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanDownlinkLoad"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanUplinkLoad"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotWanLoadMeasDuration"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotTermsConditionsFilename"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotTermsConditionsDate"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotTermsConditionsTime"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotTermsConditionsUrlFilter"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAnqpServerRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRoamingOIIsBeacon"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRoamingOIRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotDomainNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspot3gppRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotRealmEAPRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotConnectionCapabilityStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotConnectionCapabilityRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatorName"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatorNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderServerUri"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderNai"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderPrimaryMethod"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderSecondaryMethod"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyName"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyNameDescription"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderFriendlyNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOsuProviderIconRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotOperatingClassRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameDescription"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameUrl"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotVenueNameRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotNetworkAuthUrl"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotNetworkAuthRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargeRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargePlanInfoRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargePlanInfoLanguage"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargePlanInfoCurrency"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotAdviceChargeNAIRealmRowStatus"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "cLHotspotEAPAuthRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWirelessHotspotConfigGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWirelessHotspotCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 1, 1)
)
ciscoWirelessHotspotCompliance.setObjects(
      *(("CISCO-WIRELESS-HOTSPOT-MIB", "ciscoWirelessHotspotConfigGroup1"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "ciscoWirelessHotspotConfigGroup2"))
)
if mibBuilder.loadTexts:
    ciscoWirelessHotspotCompliance.setStatus(
        "deprecated"
    )

ciscoWirelessHotspotComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 863, 2, 1, 2)
)
ciscoWirelessHotspotComplianceRev1.setObjects(
      *(("CISCO-WIRELESS-HOTSPOT-MIB", "ciscoWirelessHotspotConfigGroup2"),
        ("CISCO-WIRELESS-HOTSPOT-MIB", "ciscoWirelessHotspotConfigGroup3"))
)
if mibBuilder.loadTexts:
    ciscoWirelessHotspotComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-HOTSPOT-MIB",
    **{"ciscoWirelessHotspotMIB": ciscoWirelessHotspotMIB,
       "ciscoWirelessHotspotMIBNotifs": ciscoWirelessHotspotMIBNotifs,
       "ciscoWirelessHotspotMIBObjects": ciscoWirelessHotspotMIBObjects,
       "ciscoWirelessHotspotConfig": ciscoWirelessHotspotConfig,
       "cLHotspotAnqpServerConfigTable": cLHotspotAnqpServerConfigTable,
       "cLHotspotAnqpServerConfigEntry": cLHotspotAnqpServerConfigEntry,
       "cLHotspotAnqpServerName": cLHotspotAnqpServerName,
       "cLHotspotAnqpServerRowStatus": cLHotspotAnqpServerRowStatus,
       "cLHotspotAnqpServerDescription": cLHotspotAnqpServerDescription,
       "cLHotspotAnqpServerInternetEnabled": cLHotspotAnqpServerInternetEnabled,
       "cLHotspotAnqpServerNetworkType": cLHotspotAnqpServerNetworkType,
       "cLHotspotAnqpServerVenueType": cLHotspotAnqpServerVenueType,
       "cLHotspotAnqpServerHessid": cLHotspotAnqpServerHessid,
       "cLHotspotGasRequestTimeout": cLHotspotGasRequestTimeout,
       "cLHotspotAnqpFragmentationThreshold": cLHotspotAnqpFragmentationThreshold,
       "cLHotspotAnqpDomainId": cLHotspotAnqpDomainId,
       "cLHotspotAnqpDomainIdEnabled": cLHotspotAnqpDomainIdEnabled,
       "cLHotspotAnqpServerIpv4AddressType": cLHotspotAnqpServerIpv4AddressType,
       "cLHotspotAnqpServerIpv6AddressType": cLHotspotAnqpServerIpv6AddressType,
       "cLHotspotAnqpOsuSsid": cLHotspotAnqpOsuSsid,
       "cLHotspotWanLinkStatus": cLHotspotWanLinkStatus,
       "cLHotspotWanIsAtCapacity": cLHotspotWanIsAtCapacity,
       "cLHotspotWanDownlinkSpeed": cLHotspotWanDownlinkSpeed,
       "cLHotspotWanUplinkSpeed": cLHotspotWanUplinkSpeed,
       "cLHotspotWanDownlinkLoad": cLHotspotWanDownlinkLoad,
       "cLHotspotWanUplinkLoad": cLHotspotWanUplinkLoad,
       "cLHotspotWanLoadMeasDuration": cLHotspotWanLoadMeasDuration,
       "cLHotspotTermsConditionsFilename": cLHotspotTermsConditionsFilename,
       "cLHotspotTermsConditionsDate": cLHotspotTermsConditionsDate,
       "cLHotspotTermsConditionsTime": cLHotspotTermsConditionsTime,
       "cLHotspotTermsConditionsUrlFilter": cLHotspotTermsConditionsUrlFilter,
       "cLHotspotRoamingOITable": cLHotspotRoamingOITable,
       "cLHotspotRoamingOIEntry": cLHotspotRoamingOIEntry,
       "cLHotspotRoamingOI": cLHotspotRoamingOI,
       "cLHotspotRoamingOIRowStatus": cLHotspotRoamingOIRowStatus,
       "cLHotspotRoamingOIIsBeacon": cLHotspotRoamingOIIsBeacon,
       "cLHotspotDomainNameTable": cLHotspotDomainNameTable,
       "cLHotspotDomainNameEntry": cLHotspotDomainNameEntry,
       "cLHotspotDomainName": cLHotspotDomainName,
       "cLHotspotDomainNameRowStatus": cLHotspotDomainNameRowStatus,
       "cLHotspot3gppTable": cLHotspot3gppTable,
       "cLHotspot3gppEntry": cLHotspot3gppEntry,
       "cLHotspot3gppNetworkCode": cLHotspot3gppNetworkCode,
       "cLHotspot3gppCountryCode": cLHotspot3gppCountryCode,
       "cLHotspot3gppRowStatus": cLHotspot3gppRowStatus,
       "cLHotspotRealmTable": cLHotspotRealmTable,
       "cLHotspotRealmEntry": cLHotspotRealmEntry,
       "cLHotspotRealmName": cLHotspotRealmName,
       "cLHotspotRealmRowStatus": cLHotspotRealmRowStatus,
       "cLHotspotRealmEAPTable": cLHotspotRealmEAPTable,
       "cLHotspotRealmEAPEntry": cLHotspotRealmEAPEntry,
       "cLHotspotRealmEAPMethod": cLHotspotRealmEAPMethod,
       "cLHotspotRealmEAPRowStatus": cLHotspotRealmEAPRowStatus,
       "cLHotspotRealmEAPAuthTable": cLHotspotRealmEAPAuthTable,
       "cLHotspotRealmEAPAuthEntry": cLHotspotRealmEAPAuthEntry,
       "cLHotspotRealmEAPAuthMethod": cLHotspotRealmEAPAuthMethod,
       "cLHotspotRealmEAPAuthRowStatus": cLHotspotRealmEAPAuthRowStatus,
       "cLHotspotRealmEAPAuthInnerAuthEAPType": cLHotspotRealmEAPAuthInnerAuthEAPType,
       "cLHotspotRealmEAPAuthNonInnerAuthEAPType": cLHotspotRealmEAPAuthNonInnerAuthEAPType,
       "cLHotspotRealmEAPAuthCredentialType": cLHotspotRealmEAPAuthCredentialType,
       "cLHotspotRealmEAPAuthTunneledEAPCredentialType": cLHotspotRealmEAPAuthTunneledEAPCredentialType,
       "cLHotspotConnectionCapabilityTable": cLHotspotConnectionCapabilityTable,
       "cLHotspotConnectionCapabilityEntry": cLHotspotConnectionCapabilityEntry,
       "cLHotspotConnectionCapabilityProtocol": cLHotspotConnectionCapabilityProtocol,
       "cLHotspotConnectionCapabilityPort": cLHotspotConnectionCapabilityPort,
       "cLHotspotConnectionCapabilityRowStatus": cLHotspotConnectionCapabilityRowStatus,
       "cLHotspotConnectionCapabilityStatus": cLHotspotConnectionCapabilityStatus,
       "cLHotspotOperatorNameTable": cLHotspotOperatorNameTable,
       "cLHotspotOperatorNameEntry": cLHotspotOperatorNameEntry,
       "cLHotspotOperatorNameLanguage": cLHotspotOperatorNameLanguage,
       "cLHotspotOperatorNameRowStatus": cLHotspotOperatorNameRowStatus,
       "cLHotspotOperatorName": cLHotspotOperatorName,
       "cLHotspotOsuProviderTable": cLHotspotOsuProviderTable,
       "cLHotspotOsuProviderEntry": cLHotspotOsuProviderEntry,
       "cLHotspotOsuProviderName": cLHotspotOsuProviderName,
       "cLHotspotOsuProviderRowStatus": cLHotspotOsuProviderRowStatus,
       "cLHotspotOsuProviderServerUri": cLHotspotOsuProviderServerUri,
       "cLHotspotOsuProviderNai": cLHotspotOsuProviderNai,
       "cLHotspotOsuProviderPrimaryMethod": cLHotspotOsuProviderPrimaryMethod,
       "cLHotspotOsuProviderSecondaryMethod": cLHotspotOsuProviderSecondaryMethod,
       "cLHotspotOsuProviderFriendlyNameTable": cLHotspotOsuProviderFriendlyNameTable,
       "cLHotspotOsuProviderFriendlyNameEntry": cLHotspotOsuProviderFriendlyNameEntry,
       "cLHotspotOsuProviderFriendlyNameLanguage": cLHotspotOsuProviderFriendlyNameLanguage,
       "cLHotspotOsuProviderFriendlyNameRowStatus": cLHotspotOsuProviderFriendlyNameRowStatus,
       "cLHotspotOsuProviderFriendlyName": cLHotspotOsuProviderFriendlyName,
       "cLHotspotOsuProviderFriendlyNameDescription": cLHotspotOsuProviderFriendlyNameDescription,
       "cLHotspotOsuProviderIconTable": cLHotspotOsuProviderIconTable,
       "cLHotspotOsuProviderIconEntry": cLHotspotOsuProviderIconEntry,
       "cLHotspotOsuProviderIconFileName": cLHotspotOsuProviderIconFileName,
       "cLHotspotOsuProviderIconRowStatus": cLHotspotOsuProviderIconRowStatus,
       "cLHotspotOperatingClassTable": cLHotspotOperatingClassTable,
       "cLHotspotOperatingClassEntry": cLHotspotOperatingClassEntry,
       "cLHotspotOperatingClassId": cLHotspotOperatingClassId,
       "cLHotspotOperatingClassRowStatus": cLHotspotOperatingClassRowStatus,
       "cLHotspotIconTable": cLHotspotIconTable,
       "cLHotspotIconEntry": cLHotspotIconEntry,
       "cLHotspotIconFileName": cLHotspotIconFileName,
       "cLHotspotIconRowStatus": cLHotspotIconRowStatus,
       "cLHotspotIconPath": cLHotspotIconPath,
       "cLHotspotIconType": cLHotspotIconType,
       "cLHotspotIconLanguage": cLHotspotIconLanguage,
       "cLHotspotIconWidth": cLHotspotIconWidth,
       "cLHotspotIconHeight": cLHotspotIconHeight,
       "cLHotspotVenueNameTable": cLHotspotVenueNameTable,
       "cLHotspotVenueNameEntry": cLHotspotVenueNameEntry,
       "cLHotspotVenueNameLanguage": cLHotspotVenueNameLanguage,
       "cLHotspotVenueNameRowStatus": cLHotspotVenueNameRowStatus,
       "cLHotspotVenueNameDescription": cLHotspotVenueNameDescription,
       "cLHotspotVenueNameUrl": cLHotspotVenueNameUrl,
       "cLHotspotNetworkAuthTable": cLHotspotNetworkAuthTable,
       "cLHotspotNetworkAuthEntry": cLHotspotNetworkAuthEntry,
       "cLHotspotNetworkAuthType": cLHotspotNetworkAuthType,
       "cLHotspotNetworkAuthRowStatus": cLHotspotNetworkAuthRowStatus,
       "cLHotspotNetworkAuthUrl": cLHotspotNetworkAuthUrl,
       "cLHotspotAdviceChargeTable": cLHotspotAdviceChargeTable,
       "cLHotspotAdviceChargeEntry": cLHotspotAdviceChargeEntry,
       "cLHotspotAdviceChargeType": cLHotspotAdviceChargeType,
       "cLHotspotAdviceChargeRowStatus": cLHotspotAdviceChargeRowStatus,
       "cLHotspotAdviceChargePlanInfoTable": cLHotspotAdviceChargePlanInfoTable,
       "cLHotspotAdviceChargePlanInfoEntry": cLHotspotAdviceChargePlanInfoEntry,
       "cLHotspotAdviceChargePlanInfoFilename": cLHotspotAdviceChargePlanInfoFilename,
       "cLHotspotAdviceChargePlanInfoPath": cLHotspotAdviceChargePlanInfoPath,
       "cLHotspotAdviceChargePlanInfoRowStatus": cLHotspotAdviceChargePlanInfoRowStatus,
       "cLHotspotAdviceChargePlanInfoLanguage": cLHotspotAdviceChargePlanInfoLanguage,
       "cLHotspotAdviceChargePlanInfoCurrency": cLHotspotAdviceChargePlanInfoCurrency,
       "cLHotspotAdviceChargeNAIRealmTable": cLHotspotAdviceChargeNAIRealmTable,
       "cLHotspotAdviceChargeNAIRealmEntry": cLHotspotAdviceChargeNAIRealmEntry,
       "cLHotspotAdviceChargeNAIRealmName": cLHotspotAdviceChargeNAIRealmName,
       "cLHotspotAdviceChargeNAIRealmRowStatus": cLHotspotAdviceChargeNAIRealmRowStatus,
       "cLHotspotEAPAuthTable": cLHotspotEAPAuthTable,
       "cLHotspotEAPAuthEntry": cLHotspotEAPAuthEntry,
       "cLHotspotEAPAuthType": cLHotspotEAPAuthType,
       "cLHotspotEAPAuthRowStatus": cLHotspotEAPAuthRowStatus,
       "ciscoWirelessHotspotMIBConform": ciscoWirelessHotspotMIBConform,
       "ciscoWirelessHotspotCompliances": ciscoWirelessHotspotCompliances,
       "ciscoWirelessHotspotCompliance": ciscoWirelessHotspotCompliance,
       "ciscoWirelessHotspotComplianceRev1": ciscoWirelessHotspotComplianceRev1,
       "ciscoWirelessHotspotGroups": ciscoWirelessHotspotGroups,
       "ciscoWirelessHotspotConfigGroup1": ciscoWirelessHotspotConfigGroup1,
       "ciscoWirelessHotspotConfigGroup2": ciscoWirelessHotspotConfigGroup2,
       "ciscoWirelessHotspotConfigGroup3": ciscoWirelessHotspotConfigGroup3}
)
