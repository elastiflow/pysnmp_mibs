# SNMP MIB module (CISCO-NETREG-DHCPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-NETREG-DHCPV6-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:23 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoNetRegDhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139)
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6MIB.setRevisions(
        ("2022-05-09 00:00",
         "2017-04-18 00:00",
         "2013-05-24 00:00",
         "2010-05-12 00:00",
         "2007-11-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNetRegDhcpv6MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6MIBNotifs = _CiscoNetRegDhcpv6MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0)
)
_CiscoNetRegDhcpv6MIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6MIBObjects = _CiscoNetRegDhcpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1)
)
_CiscoNetRegDhcpv6NotifObjects_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6NotifObjects = _CiscoNetRegDhcpv6NotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1)
)


class _Cnrdhcpv6LinkName_Type(SnmpAdminString):
    """Custom type cnrdhcpv6LinkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cnrdhcpv6LinkName_Type.__name__ = "SnmpAdminString"
_Cnrdhcpv6LinkName_Object = MibScalar
cnrdhcpv6LinkName = _Cnrdhcpv6LinkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 1),
    _Cnrdhcpv6LinkName_Type()
)
cnrdhcpv6LinkName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6LinkName.setStatus("current")
_Cnrdhcpv6FreeAddressValue_Type = Gauge32
_Cnrdhcpv6FreeAddressValue_Object = MibScalar
cnrdhcpv6FreeAddressValue = _Cnrdhcpv6FreeAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 2),
    _Cnrdhcpv6FreeAddressValue_Type()
)
cnrdhcpv6FreeAddressValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6FreeAddressValue.setStatus("current")


class _Cnrdhcpv6Threshold_Type(Gauge32):
    """Custom type cnrdhcpv6Threshold based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cnrdhcpv6Threshold_Type.__name__ = "Gauge32"
_Cnrdhcpv6Threshold_Object = MibScalar
cnrdhcpv6Threshold = _Cnrdhcpv6Threshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 3),
    _Cnrdhcpv6Threshold_Type()
)
cnrdhcpv6Threshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6Threshold.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6Threshold.setUnits("percentage")
_Cnrdhcpv6PrefixAddress_Type = InetAddressIPv6
_Cnrdhcpv6PrefixAddress_Object = MibScalar
cnrdhcpv6PrefixAddress = _Cnrdhcpv6PrefixAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 4),
    _Cnrdhcpv6PrefixAddress_Type()
)
cnrdhcpv6PrefixAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6PrefixAddress.setStatus("current")
_Cnrdhcpv6PrefixLength_Type = InetAddressPrefixLength
_Cnrdhcpv6PrefixLength_Object = MibScalar
cnrdhcpv6PrefixLength = _Cnrdhcpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 5),
    _Cnrdhcpv6PrefixLength_Type()
)
cnrdhcpv6PrefixLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6PrefixLength.setStatus("current")


class _Cnrdhcpv6ThresholdType_Type(Integer32):
    """Custom type cnrdhcpv6ThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("prefix", 1),
          ("link", 2),
          ("selectionTags", 3))
    )


_Cnrdhcpv6ThresholdType_Type.__name__ = "Integer32"
_Cnrdhcpv6ThresholdType_Object = MibScalar
cnrdhcpv6ThresholdType = _Cnrdhcpv6ThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 6),
    _Cnrdhcpv6ThresholdType_Type()
)
cnrdhcpv6ThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6ThresholdType.setStatus("current")


class _Cnrdhcpv6TypeDesc_Type(SnmpAdminString):
    """Custom type cnrdhcpv6TypeDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cnrdhcpv6TypeDesc_Type.__name__ = "SnmpAdminString"
_Cnrdhcpv6TypeDesc_Object = MibScalar
cnrdhcpv6TypeDesc = _Cnrdhcpv6TypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 7),
    _Cnrdhcpv6TypeDesc_Type()
)
cnrdhcpv6TypeDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6TypeDesc.setStatus("current")
_Cnrdhcpv6DupIpv6Address_Type = InetAddressIPv6
_Cnrdhcpv6DupIpv6Address_Object = MibScalar
cnrdhcpv6DupIpv6Address = _Cnrdhcpv6DupIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 8),
    _Cnrdhcpv6DupIpv6Address_Type()
)
cnrdhcpv6DupIpv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6DupIpv6Address.setStatus("current")


class _Cnrdhcpv6ClientId_Type(SnmpAdminString):
    """Custom type cnrdhcpv6ClientId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_Cnrdhcpv6ClientId_Type.__name__ = "SnmpAdminString"
_Cnrdhcpv6ClientId_Object = MibScalar
cnrdhcpv6ClientId = _Cnrdhcpv6ClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 9),
    _Cnrdhcpv6ClientId_Type()
)
cnrdhcpv6ClientId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6ClientId.setStatus("current")
_Cnrdhcpv6ClientLookupKey_Type = SnmpAdminString
_Cnrdhcpv6ClientLookupKey_Object = MibScalar
cnrdhcpv6ClientLookupKey = _Cnrdhcpv6ClientLookupKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 10),
    _Cnrdhcpv6ClientLookupKey_Type()
)
cnrdhcpv6ClientLookupKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6ClientLookupKey.setStatus("current")


class _Cnrdhcpv6DupIpv6AddressDetectedBy_Type(Integer32):
    """Custom type cnrdhcpv6DupIpv6AddressDetectedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpClient", 1),
          ("dhcpServer", 2))
    )


_Cnrdhcpv6DupIpv6AddressDetectedBy_Type.__name__ = "Integer32"
_Cnrdhcpv6DupIpv6AddressDetectedBy_Object = MibScalar
cnrdhcpv6DupIpv6AddressDetectedBy = _Cnrdhcpv6DupIpv6AddressDetectedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 11),
    _Cnrdhcpv6DupIpv6AddressDetectedBy_Type()
)
cnrdhcpv6DupIpv6AddressDetectedBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6DupIpv6AddressDetectedBy.setStatus("current")
_Cnrdhcpv6DupPrefix_Type = InetAddressIPv6
_Cnrdhcpv6DupPrefix_Object = MibScalar
cnrdhcpv6DupPrefix = _Cnrdhcpv6DupPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 12),
    _Cnrdhcpv6DupPrefix_Type()
)
cnrdhcpv6DupPrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6DupPrefix.setStatus("deprecated")
_Cnrdhcpv6DupPrefixLength_Type = InetAddressPrefixLength
_Cnrdhcpv6DupPrefixLength_Object = MibScalar
cnrdhcpv6DupPrefixLength = _Cnrdhcpv6DupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 13),
    _Cnrdhcpv6DupPrefixLength_Type()
)
cnrdhcpv6DupPrefixLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6DupPrefixLength.setStatus("deprecated")


class _Cnrdhcpv6DupPrefixDetectedBy_Type(Integer32):
    """Custom type cnrdhcpv6DupPrefixDetectedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpServer", 1),
          ("dhcpClient", 2))
    )


_Cnrdhcpv6DupPrefixDetectedBy_Type.__name__ = "Integer32"
_Cnrdhcpv6DupPrefixDetectedBy_Object = MibScalar
cnrdhcpv6DupPrefixDetectedBy = _Cnrdhcpv6DupPrefixDetectedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 14),
    _Cnrdhcpv6DupPrefixDetectedBy_Type()
)
cnrdhcpv6DupPrefixDetectedBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6DupPrefixDetectedBy.setStatus("deprecated")
_Cnrdhcpv6PartnerServerAddr_Type = IpAddress
_Cnrdhcpv6PartnerServerAddr_Object = MibScalar
cnrdhcpv6PartnerServerAddr = _Cnrdhcpv6PartnerServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 15),
    _Cnrdhcpv6PartnerServerAddr_Type()
)
cnrdhcpv6PartnerServerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6PartnerServerAddr.setStatus("current")
_Cnrdhcpv6PartnerServerIpv6Addr_Type = InetAddressIPv6
_Cnrdhcpv6PartnerServerIpv6Addr_Object = MibScalar
cnrdhcpv6PartnerServerIpv6Addr = _Cnrdhcpv6PartnerServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 16),
    _Cnrdhcpv6PartnerServerIpv6Addr_Type()
)
cnrdhcpv6PartnerServerIpv6Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6PartnerServerIpv6Addr.setStatus("current")
_Cnrdhcpv6ContestedIpv6Address_Type = InetAddressIPv6
_Cnrdhcpv6ContestedIpv6Address_Object = MibScalar
cnrdhcpv6ContestedIpv6Address = _Cnrdhcpv6ContestedIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 17),
    _Cnrdhcpv6ContestedIpv6Address_Type()
)
cnrdhcpv6ContestedIpv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6ContestedIpv6Address.setStatus("current")
_Cnrdhcpv6ContestedIpv6Prefix_Type = InetAddressIPv6
_Cnrdhcpv6ContestedIpv6Prefix_Object = MibScalar
cnrdhcpv6ContestedIpv6Prefix = _Cnrdhcpv6ContestedIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 18),
    _Cnrdhcpv6ContestedIpv6Prefix_Type()
)
cnrdhcpv6ContestedIpv6Prefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6ContestedIpv6Prefix.setStatus("current")
_Cnrdhcpv6ContestedIpv6PrefixLength_Type = InetAddressPrefixLength
_Cnrdhcpv6ContestedIpv6PrefixLength_Object = MibScalar
cnrdhcpv6ContestedIpv6PrefixLength = _Cnrdhcpv6ContestedIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 19),
    _Cnrdhcpv6ContestedIpv6PrefixLength_Type()
)
cnrdhcpv6ContestedIpv6PrefixLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6ContestedIpv6PrefixLength.setStatus("current")


class _Cnrdhcpv6FailoverPairName_Type(SnmpAdminString):
    """Custom type cnrdhcpv6FailoverPairName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cnrdhcpv6FailoverPairName_Type.__name__ = "SnmpAdminString"
_Cnrdhcpv6FailoverPairName_Object = MibScalar
cnrdhcpv6FailoverPairName = _Cnrdhcpv6FailoverPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 1, 20),
    _Cnrdhcpv6FailoverPairName_Type()
)
cnrdhcpv6FailoverPairName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrdhcpv6FailoverPairName.setStatus("current")
_CiscoNetRegDhcpv6TotalCounters_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6TotalCounters = _CiscoNetRegDhcpv6TotalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2)
)
_Cnrdhcpv6TotalPacketsRcvd_Type = Counter32
_Cnrdhcpv6TotalPacketsRcvd_Object = MibScalar
cnrdhcpv6TotalPacketsRcvd = _Cnrdhcpv6TotalPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 1),
    _Cnrdhcpv6TotalPacketsRcvd_Type()
)
cnrdhcpv6TotalPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsRcvd.setUnits("packets")
_Cnrdhcpv6TotalPacketsRcvdRelay_Type = Counter32
_Cnrdhcpv6TotalPacketsRcvdRelay_Object = MibScalar
cnrdhcpv6TotalPacketsRcvdRelay = _Cnrdhcpv6TotalPacketsRcvdRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 2),
    _Cnrdhcpv6TotalPacketsRcvdRelay_Type()
)
cnrdhcpv6TotalPacketsRcvdRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsRcvdRelay.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsRcvdRelay.setUnits("packets")
_Cnrdhcpv6TotalSolicits_Type = Counter32
_Cnrdhcpv6TotalSolicits_Object = MibScalar
cnrdhcpv6TotalSolicits = _Cnrdhcpv6TotalSolicits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 3),
    _Cnrdhcpv6TotalSolicits_Type()
)
cnrdhcpv6TotalSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalSolicits.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalSolicits.setUnits("messages")
_Cnrdhcpv6TotalRequests_Type = Counter32
_Cnrdhcpv6TotalRequests_Object = MibScalar
cnrdhcpv6TotalRequests = _Cnrdhcpv6TotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 4),
    _Cnrdhcpv6TotalRequests_Type()
)
cnrdhcpv6TotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalRequests.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalRequests.setUnits("messages")
_Cnrdhcpv6TotalConfirms_Type = Counter32
_Cnrdhcpv6TotalConfirms_Object = MibScalar
cnrdhcpv6TotalConfirms = _Cnrdhcpv6TotalConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 5),
    _Cnrdhcpv6TotalConfirms_Type()
)
cnrdhcpv6TotalConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalConfirms.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalConfirms.setUnits("messages")
_Cnrdhcpv6TotalRenews_Type = Counter32
_Cnrdhcpv6TotalRenews_Object = MibScalar
cnrdhcpv6TotalRenews = _Cnrdhcpv6TotalRenews_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 6),
    _Cnrdhcpv6TotalRenews_Type()
)
cnrdhcpv6TotalRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalRenews.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalRenews.setUnits("messages")
_Cnrdhcpv6TotalRebinds_Type = Counter32
_Cnrdhcpv6TotalRebinds_Object = MibScalar
cnrdhcpv6TotalRebinds = _Cnrdhcpv6TotalRebinds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 7),
    _Cnrdhcpv6TotalRebinds_Type()
)
cnrdhcpv6TotalRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalRebinds.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalRebinds.setUnits("messages")
_Cnrdhcpv6TotalReleases_Type = Counter32
_Cnrdhcpv6TotalReleases_Object = MibScalar
cnrdhcpv6TotalReleases = _Cnrdhcpv6TotalReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 8),
    _Cnrdhcpv6TotalReleases_Type()
)
cnrdhcpv6TotalReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReleases.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReleases.setUnits("messages")
_Cnrdhcpv6TotalDeclines_Type = Counter32
_Cnrdhcpv6TotalDeclines_Object = MibScalar
cnrdhcpv6TotalDeclines = _Cnrdhcpv6TotalDeclines_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 9),
    _Cnrdhcpv6TotalDeclines_Type()
)
cnrdhcpv6TotalDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDeclines.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDeclines.setUnits("messages")
_Cnrdhcpv6TotalInfoRequests_Type = Counter32
_Cnrdhcpv6TotalInfoRequests_Object = MibScalar
cnrdhcpv6TotalInfoRequests = _Cnrdhcpv6TotalInfoRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 10),
    _Cnrdhcpv6TotalInfoRequests_Type()
)
cnrdhcpv6TotalInfoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalInfoRequests.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalInfoRequests.setUnits("messages")
_Cnrdhcpv6TotalInvalidPackets_Type = Counter32
_Cnrdhcpv6TotalInvalidPackets_Object = MibScalar
cnrdhcpv6TotalInvalidPackets = _Cnrdhcpv6TotalInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 11),
    _Cnrdhcpv6TotalInvalidPackets_Type()
)
cnrdhcpv6TotalInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalInvalidPackets.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalInvalidPackets.setUnits("packets")
_Cnrdhcpv6TotalPacketsSent_Type = Counter32
_Cnrdhcpv6TotalPacketsSent_Object = MibScalar
cnrdhcpv6TotalPacketsSent = _Cnrdhcpv6TotalPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 12),
    _Cnrdhcpv6TotalPacketsSent_Type()
)
cnrdhcpv6TotalPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsSent.setUnits("packets")
_Cnrdhcpv6TotalPacketsSentRelay_Type = Counter32
_Cnrdhcpv6TotalPacketsSentRelay_Object = MibScalar
cnrdhcpv6TotalPacketsSentRelay = _Cnrdhcpv6TotalPacketsSentRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 13),
    _Cnrdhcpv6TotalPacketsSentRelay_Type()
)
cnrdhcpv6TotalPacketsSentRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsSentRelay.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalPacketsSentRelay.setUnits("messages")
_Cnrdhcpv6TotalAdvertises_Type = Counter32
_Cnrdhcpv6TotalAdvertises_Object = MibScalar
cnrdhcpv6TotalAdvertises = _Cnrdhcpv6TotalAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 14),
    _Cnrdhcpv6TotalAdvertises_Type()
)
cnrdhcpv6TotalAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalAdvertises.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalAdvertises.setUnits("messages")
_Cnrdhcpv6TotalReplies_Type = Counter32
_Cnrdhcpv6TotalReplies_Object = MibScalar
cnrdhcpv6TotalReplies = _Cnrdhcpv6TotalReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 15),
    _Cnrdhcpv6TotalReplies_Type()
)
cnrdhcpv6TotalReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReplies.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReplies.setUnits("messages")
_Cnrdhcpv6TotalReconfigures_Type = Counter32
_Cnrdhcpv6TotalReconfigures_Object = MibScalar
cnrdhcpv6TotalReconfigures = _Cnrdhcpv6TotalReconfigures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 16),
    _Cnrdhcpv6TotalReconfigures_Type()
)
cnrdhcpv6TotalReconfigures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReconfigures.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReconfigures.setUnits("messages")
_Cnrdhcpv6TotalAuthFails_Type = Counter32
_Cnrdhcpv6TotalAuthFails_Object = MibScalar
cnrdhcpv6TotalAuthFails = _Cnrdhcpv6TotalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 17),
    _Cnrdhcpv6TotalAuthFails_Type()
)
cnrdhcpv6TotalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalAuthFails.setUnits("packets")
_Cnrdhcpv6TotalDiscards_Type = Counter32
_Cnrdhcpv6TotalDiscards_Object = MibScalar
cnrdhcpv6TotalDiscards = _Cnrdhcpv6TotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 18),
    _Cnrdhcpv6TotalDiscards_Type()
)
cnrdhcpv6TotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDiscards.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDiscards.setUnits("packets")
_Cnrdhcpv6TotalDuplicates_Type = Counter32
_Cnrdhcpv6TotalDuplicates_Object = MibScalar
cnrdhcpv6TotalDuplicates = _Cnrdhcpv6TotalDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 19),
    _Cnrdhcpv6TotalDuplicates_Type()
)
cnrdhcpv6TotalDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDuplicates.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDuplicates.setUnits("packets")
_Cnrdhcpv6TotalInvalidClients_Type = Counter32
_Cnrdhcpv6TotalInvalidClients_Object = MibScalar
cnrdhcpv6TotalInvalidClients = _Cnrdhcpv6TotalInvalidClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 20),
    _Cnrdhcpv6TotalInvalidClients_Type()
)
cnrdhcpv6TotalInvalidClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalInvalidClients.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalInvalidClients.setUnits("packets")
_Cnrdhcpv6TotalUnknownLinks_Type = Counter32
_Cnrdhcpv6TotalUnknownLinks_Object = MibScalar
cnrdhcpv6TotalUnknownLinks = _Cnrdhcpv6TotalUnknownLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 21),
    _Cnrdhcpv6TotalUnknownLinks_Type()
)
cnrdhcpv6TotalUnknownLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalUnknownLinks.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalUnknownLinks.setUnits("packets")
_Cnrdhcpv6TotalDroppedOthers_Type = Counter32
_Cnrdhcpv6TotalDroppedOthers_Object = MibScalar
cnrdhcpv6TotalDroppedOthers = _Cnrdhcpv6TotalDroppedOthers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 22),
    _Cnrdhcpv6TotalDroppedOthers_Type()
)
cnrdhcpv6TotalDroppedOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDroppedOthers.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDroppedOthers.setUnits("packets")
_Cnrdhcpv6TotalDroppedConfig_Type = Counter32
_Cnrdhcpv6TotalDroppedConfig_Object = MibScalar
cnrdhcpv6TotalDroppedConfig = _Cnrdhcpv6TotalDroppedConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 23),
    _Cnrdhcpv6TotalDroppedConfig_Type()
)
cnrdhcpv6TotalDroppedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDroppedConfig.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalDroppedConfig.setUnits("packets")
_Cnrdhcpv6TotalActiveLeases_Type = Gauge32
_Cnrdhcpv6TotalActiveLeases_Object = MibScalar
cnrdhcpv6TotalActiveLeases = _Cnrdhcpv6TotalActiveLeases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 24),
    _Cnrdhcpv6TotalActiveLeases_Type()
)
cnrdhcpv6TotalActiveLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalActiveLeases.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalActiveLeases.setUnits("leases")
_Cnrdhcpv6TotalAllocatedLeases_Type = Gauge32
_Cnrdhcpv6TotalAllocatedLeases_Object = MibScalar
cnrdhcpv6TotalAllocatedLeases = _Cnrdhcpv6TotalAllocatedLeases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 25),
    _Cnrdhcpv6TotalAllocatedLeases_Type()
)
cnrdhcpv6TotalAllocatedLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalAllocatedLeases.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalAllocatedLeases.setUnits("leases")
_Cnrdhcpv6TotalReservedLeases_Type = Gauge32
_Cnrdhcpv6TotalReservedLeases_Object = MibScalar
cnrdhcpv6TotalReservedLeases = _Cnrdhcpv6TotalReservedLeases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 26),
    _Cnrdhcpv6TotalReservedLeases_Type()
)
cnrdhcpv6TotalReservedLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReservedLeases.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReservedLeases.setUnits("leases")
_Cnrdhcpv6TotalReservedActiveLeases_Type = Gauge32
_Cnrdhcpv6TotalReservedActiveLeases_Object = MibScalar
cnrdhcpv6TotalReservedActiveLeases = _Cnrdhcpv6TotalReservedActiveLeases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 27),
    _Cnrdhcpv6TotalReservedActiveLeases_Type()
)
cnrdhcpv6TotalReservedActiveLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReservedActiveLeases.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalReservedActiveLeases.setUnits("leases")
_Cnrdhcpv6TotalLeaseQueries_Type = Counter32
_Cnrdhcpv6TotalLeaseQueries_Object = MibScalar
cnrdhcpv6TotalLeaseQueries = _Cnrdhcpv6TotalLeaseQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 28),
    _Cnrdhcpv6TotalLeaseQueries_Type()
)
cnrdhcpv6TotalLeaseQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalLeaseQueries.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalLeaseQueries.setUnits("messages")
_Cnrdhcpv6TotalLeaseQueryReplies_Type = Counter32
_Cnrdhcpv6TotalLeaseQueryReplies_Object = MibScalar
cnrdhcpv6TotalLeaseQueryReplies = _Cnrdhcpv6TotalLeaseQueryReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 29),
    _Cnrdhcpv6TotalLeaseQueryReplies_Type()
)
cnrdhcpv6TotalLeaseQueryReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalLeaseQueryReplies.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalLeaseQueryReplies.setUnits("messages")
_Cnrdhcpv6TotalExtensionErrors_Type = Counter32
_Cnrdhcpv6TotalExtensionErrors_Object = MibScalar
cnrdhcpv6TotalExtensionErrors = _Cnrdhcpv6TotalExtensionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 30),
    _Cnrdhcpv6TotalExtensionErrors_Type()
)
cnrdhcpv6TotalExtensionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalExtensionErrors.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalExtensionErrors.setUnits("packets")
_Cnrdhcpv6TotalExtensionDrops_Type = Counter32
_Cnrdhcpv6TotalExtensionDrops_Object = MibScalar
cnrdhcpv6TotalExtensionDrops = _Cnrdhcpv6TotalExtensionDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 2, 31),
    _Cnrdhcpv6TotalExtensionDrops_Type()
)
cnrdhcpv6TotalExtensionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalExtensionDrops.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6TotalExtensionDrops.setUnits("packets")
_CiscoNetRegDhcpv6PeriodCounters_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6PeriodCounters = _CiscoNetRegDhcpv6PeriodCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3)
)
_Cnrdhcpv6PeriodPacketsRcvd_Type = Counter32
_Cnrdhcpv6PeriodPacketsRcvd_Object = MibScalar
cnrdhcpv6PeriodPacketsRcvd = _Cnrdhcpv6PeriodPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 1),
    _Cnrdhcpv6PeriodPacketsRcvd_Type()
)
cnrdhcpv6PeriodPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsRcvd.setUnits("packets")
_Cnrdhcpv6PeriodPacketsRcvdRelay_Type = Counter32
_Cnrdhcpv6PeriodPacketsRcvdRelay_Object = MibScalar
cnrdhcpv6PeriodPacketsRcvdRelay = _Cnrdhcpv6PeriodPacketsRcvdRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 2),
    _Cnrdhcpv6PeriodPacketsRcvdRelay_Type()
)
cnrdhcpv6PeriodPacketsRcvdRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsRcvdRelay.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsRcvdRelay.setUnits("packets")
_Cnrdhcpv6PeriodSolicits_Type = Counter32
_Cnrdhcpv6PeriodSolicits_Object = MibScalar
cnrdhcpv6PeriodSolicits = _Cnrdhcpv6PeriodSolicits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 3),
    _Cnrdhcpv6PeriodSolicits_Type()
)
cnrdhcpv6PeriodSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodSolicits.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodSolicits.setUnits("messages")
_Cnrdhcpv6PeriodRequests_Type = Counter32
_Cnrdhcpv6PeriodRequests_Object = MibScalar
cnrdhcpv6PeriodRequests = _Cnrdhcpv6PeriodRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 4),
    _Cnrdhcpv6PeriodRequests_Type()
)
cnrdhcpv6PeriodRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodRequests.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodRequests.setUnits("messages")
_Cnrdhcpv6PeriodConfirms_Type = Counter32
_Cnrdhcpv6PeriodConfirms_Object = MibScalar
cnrdhcpv6PeriodConfirms = _Cnrdhcpv6PeriodConfirms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 5),
    _Cnrdhcpv6PeriodConfirms_Type()
)
cnrdhcpv6PeriodConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodConfirms.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodConfirms.setUnits("messages")
_Cnrdhcpv6PeriodRenews_Type = Counter32
_Cnrdhcpv6PeriodRenews_Object = MibScalar
cnrdhcpv6PeriodRenews = _Cnrdhcpv6PeriodRenews_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 6),
    _Cnrdhcpv6PeriodRenews_Type()
)
cnrdhcpv6PeriodRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodRenews.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodRenews.setUnits("messages")
_Cnrdhcpv6PeriodRebinds_Type = Counter32
_Cnrdhcpv6PeriodRebinds_Object = MibScalar
cnrdhcpv6PeriodRebinds = _Cnrdhcpv6PeriodRebinds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 7),
    _Cnrdhcpv6PeriodRebinds_Type()
)
cnrdhcpv6PeriodRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodRebinds.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodRebinds.setUnits("messages")
_Cnrdhcpv6PeriodReleases_Type = Counter32
_Cnrdhcpv6PeriodReleases_Object = MibScalar
cnrdhcpv6PeriodReleases = _Cnrdhcpv6PeriodReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 8),
    _Cnrdhcpv6PeriodReleases_Type()
)
cnrdhcpv6PeriodReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodReleases.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodReleases.setUnits("messages")
_Cnrdhcpv6PeriodDeclines_Type = Counter32
_Cnrdhcpv6PeriodDeclines_Object = MibScalar
cnrdhcpv6PeriodDeclines = _Cnrdhcpv6PeriodDeclines_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 9),
    _Cnrdhcpv6PeriodDeclines_Type()
)
cnrdhcpv6PeriodDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDeclines.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDeclines.setUnits("messages")
_Cnrdhcpv6PeriodInfoRequests_Type = Counter32
_Cnrdhcpv6PeriodInfoRequests_Object = MibScalar
cnrdhcpv6PeriodInfoRequests = _Cnrdhcpv6PeriodInfoRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 10),
    _Cnrdhcpv6PeriodInfoRequests_Type()
)
cnrdhcpv6PeriodInfoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodInfoRequests.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodInfoRequests.setUnits("messages")
_Cnrdhcpv6PeriodInvalidPackets_Type = Counter32
_Cnrdhcpv6PeriodInvalidPackets_Object = MibScalar
cnrdhcpv6PeriodInvalidPackets = _Cnrdhcpv6PeriodInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 11),
    _Cnrdhcpv6PeriodInvalidPackets_Type()
)
cnrdhcpv6PeriodInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodInvalidPackets.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodInvalidPackets.setUnits("packets")
_Cnrdhcpv6PeriodPacketsSent_Type = Counter32
_Cnrdhcpv6PeriodPacketsSent_Object = MibScalar
cnrdhcpv6PeriodPacketsSent = _Cnrdhcpv6PeriodPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 12),
    _Cnrdhcpv6PeriodPacketsSent_Type()
)
cnrdhcpv6PeriodPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsSent.setUnits("packets")
_Cnrdhcpv6PeriodPacketsSentRelay_Type = Counter32
_Cnrdhcpv6PeriodPacketsSentRelay_Object = MibScalar
cnrdhcpv6PeriodPacketsSentRelay = _Cnrdhcpv6PeriodPacketsSentRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 13),
    _Cnrdhcpv6PeriodPacketsSentRelay_Type()
)
cnrdhcpv6PeriodPacketsSentRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsSentRelay.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodPacketsSentRelay.setUnits("messages")
_Cnrdhcpv6PeriodAdvertises_Type = Counter32
_Cnrdhcpv6PeriodAdvertises_Object = MibScalar
cnrdhcpv6PeriodAdvertises = _Cnrdhcpv6PeriodAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 14),
    _Cnrdhcpv6PeriodAdvertises_Type()
)
cnrdhcpv6PeriodAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodAdvertises.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodAdvertises.setUnits("packets")
_Cnrdhcpv6PeriodReplies_Type = Counter32
_Cnrdhcpv6PeriodReplies_Object = MibScalar
cnrdhcpv6PeriodReplies = _Cnrdhcpv6PeriodReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 15),
    _Cnrdhcpv6PeriodReplies_Type()
)
cnrdhcpv6PeriodReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodReplies.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodReplies.setUnits("messages")
_Cnrdhcpv6PeriodReconfigures_Type = Counter32
_Cnrdhcpv6PeriodReconfigures_Object = MibScalar
cnrdhcpv6PeriodReconfigures = _Cnrdhcpv6PeriodReconfigures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 16),
    _Cnrdhcpv6PeriodReconfigures_Type()
)
cnrdhcpv6PeriodReconfigures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodReconfigures.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodReconfigures.setUnits("messages")
_Cnrdhcpv6PeriodAuthFails_Type = Counter32
_Cnrdhcpv6PeriodAuthFails_Object = MibScalar
cnrdhcpv6PeriodAuthFails = _Cnrdhcpv6PeriodAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 17),
    _Cnrdhcpv6PeriodAuthFails_Type()
)
cnrdhcpv6PeriodAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodAuthFails.setUnits("packets")
_Cnrdhcpv6PeriodDiscards_Type = Counter32
_Cnrdhcpv6PeriodDiscards_Object = MibScalar
cnrdhcpv6PeriodDiscards = _Cnrdhcpv6PeriodDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 18),
    _Cnrdhcpv6PeriodDiscards_Type()
)
cnrdhcpv6PeriodDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDiscards.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDiscards.setUnits("packets")
_Cnrdhcpv6PeriodDuplicates_Type = Counter32
_Cnrdhcpv6PeriodDuplicates_Object = MibScalar
cnrdhcpv6PeriodDuplicates = _Cnrdhcpv6PeriodDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 19),
    _Cnrdhcpv6PeriodDuplicates_Type()
)
cnrdhcpv6PeriodDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDuplicates.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDuplicates.setUnits("packets")
_Cnrdhcpv6PeriodInvalidClients_Type = Counter32
_Cnrdhcpv6PeriodInvalidClients_Object = MibScalar
cnrdhcpv6PeriodInvalidClients = _Cnrdhcpv6PeriodInvalidClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 20),
    _Cnrdhcpv6PeriodInvalidClients_Type()
)
cnrdhcpv6PeriodInvalidClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodInvalidClients.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodInvalidClients.setUnits("packets")
_Cnrdhcpv6PeriodUnknownLinks_Type = Counter32
_Cnrdhcpv6PeriodUnknownLinks_Object = MibScalar
cnrdhcpv6PeriodUnknownLinks = _Cnrdhcpv6PeriodUnknownLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 21),
    _Cnrdhcpv6PeriodUnknownLinks_Type()
)
cnrdhcpv6PeriodUnknownLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodUnknownLinks.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodUnknownLinks.setUnits("packets")
_Cnrdhcpv6PeriodDroppedOthers_Type = Counter32
_Cnrdhcpv6PeriodDroppedOthers_Object = MibScalar
cnrdhcpv6PeriodDroppedOthers = _Cnrdhcpv6PeriodDroppedOthers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 22),
    _Cnrdhcpv6PeriodDroppedOthers_Type()
)
cnrdhcpv6PeriodDroppedOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDroppedOthers.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDroppedOthers.setUnits("packets")
_Cnrdhcpv6PeriodDroppedConfig_Type = Counter32
_Cnrdhcpv6PeriodDroppedConfig_Object = MibScalar
cnrdhcpv6PeriodDroppedConfig = _Cnrdhcpv6PeriodDroppedConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 23),
    _Cnrdhcpv6PeriodDroppedConfig_Type()
)
cnrdhcpv6PeriodDroppedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDroppedConfig.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodDroppedConfig.setUnits("packets")
_Cnrdhcpv6PeriodLeaseQueries_Type = Counter32
_Cnrdhcpv6PeriodLeaseQueries_Object = MibScalar
cnrdhcpv6PeriodLeaseQueries = _Cnrdhcpv6PeriodLeaseQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 24),
    _Cnrdhcpv6PeriodLeaseQueries_Type()
)
cnrdhcpv6PeriodLeaseQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodLeaseQueries.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodLeaseQueries.setUnits("messages")
_Cnrdhcpv6PeriodLeaseQueryReplies_Type = Counter32
_Cnrdhcpv6PeriodLeaseQueryReplies_Object = MibScalar
cnrdhcpv6PeriodLeaseQueryReplies = _Cnrdhcpv6PeriodLeaseQueryReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 25),
    _Cnrdhcpv6PeriodLeaseQueryReplies_Type()
)
cnrdhcpv6PeriodLeaseQueryReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodLeaseQueryReplies.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodLeaseQueryReplies.setUnits("messages")
_Cnrdhcpv6PeriodStartTime_Type = TimeStamp
_Cnrdhcpv6PeriodStartTime_Object = MibScalar
cnrdhcpv6PeriodStartTime = _Cnrdhcpv6PeriodStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 26),
    _Cnrdhcpv6PeriodStartTime_Type()
)
cnrdhcpv6PeriodStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodStartTime.setStatus("current")
_Cnrdhcpv6PeriodEndTime_Type = TimeStamp
_Cnrdhcpv6PeriodEndTime_Object = MibScalar
cnrdhcpv6PeriodEndTime = _Cnrdhcpv6PeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 27),
    _Cnrdhcpv6PeriodEndTime_Type()
)
cnrdhcpv6PeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodEndTime.setStatus("current")
_Cnrdhcpv6PeriodExtensionErrors_Type = Counter32
_Cnrdhcpv6PeriodExtensionErrors_Object = MibScalar
cnrdhcpv6PeriodExtensionErrors = _Cnrdhcpv6PeriodExtensionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 28),
    _Cnrdhcpv6PeriodExtensionErrors_Type()
)
cnrdhcpv6PeriodExtensionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodExtensionErrors.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodExtensionErrors.setUnits("packets")
_Cnrdhcpv6PeriodExtensionDrops_Type = Counter32
_Cnrdhcpv6PeriodExtensionDrops_Object = MibScalar
cnrdhcpv6PeriodExtensionDrops = _Cnrdhcpv6PeriodExtensionDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 3, 29),
    _Cnrdhcpv6PeriodExtensionDrops_Type()
)
cnrdhcpv6PeriodExtensionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodExtensionDrops.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6PeriodExtensionDrops.setUnits("packets")
_CiscoNetRegDhcpv6FailoverCounters_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6FailoverCounters = _CiscoNetRegDhcpv6FailoverCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4)
)
_Cnrdhcpv6FOStateRcvd_Type = Counter32
_Cnrdhcpv6FOStateRcvd_Object = MibScalar
cnrdhcpv6FOStateRcvd = _Cnrdhcpv6FOStateRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 1),
    _Cnrdhcpv6FOStateRcvd_Type()
)
cnrdhcpv6FOStateRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOStateRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOStateRcvd.setUnits("messages")
_Cnrdhcpv6FOBindingUpdsRcvd_Type = Counter32
_Cnrdhcpv6FOBindingUpdsRcvd_Object = MibScalar
cnrdhcpv6FOBindingUpdsRcvd = _Cnrdhcpv6FOBindingUpdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 2),
    _Cnrdhcpv6FOBindingUpdsRcvd_Type()
)
cnrdhcpv6FOBindingUpdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingUpdsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingUpdsRcvd.setUnits("messages")
_Cnrdhcpv6FOBindingAcksRcvd_Type = Counter32
_Cnrdhcpv6FOBindingAcksRcvd_Object = MibScalar
cnrdhcpv6FOBindingAcksRcvd = _Cnrdhcpv6FOBindingAcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 3),
    _Cnrdhcpv6FOBindingAcksRcvd_Type()
)
cnrdhcpv6FOBindingAcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingAcksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingAcksRcvd.setUnits("messages")
_Cnrdhcpv6FOBindingNaksRcvd_Type = Counter32
_Cnrdhcpv6FOBindingNaksRcvd_Object = MibScalar
cnrdhcpv6FOBindingNaksRcvd = _Cnrdhcpv6FOBindingNaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 4),
    _Cnrdhcpv6FOBindingNaksRcvd_Type()
)
cnrdhcpv6FOBindingNaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingNaksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingNaksRcvd.setUnits("messages")
_Cnrdhcpv6FOConnectRcvd_Type = Counter32
_Cnrdhcpv6FOConnectRcvd_Object = MibScalar
cnrdhcpv6FOConnectRcvd = _Cnrdhcpv6FOConnectRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 5),
    _Cnrdhcpv6FOConnectRcvd_Type()
)
cnrdhcpv6FOConnectRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectRcvd.setUnits("messages")
_Cnrdhcpv6FOConnectAckRcvd_Type = Counter32
_Cnrdhcpv6FOConnectAckRcvd_Object = MibScalar
cnrdhcpv6FOConnectAckRcvd = _Cnrdhcpv6FOConnectAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 6),
    _Cnrdhcpv6FOConnectAckRcvd_Type()
)
cnrdhcpv6FOConnectAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectAckRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectAckRcvd.setUnits("messages")
_Cnrdhcpv6FOContactRcvd_Type = Counter32
_Cnrdhcpv6FOContactRcvd_Object = MibScalar
cnrdhcpv6FOContactRcvd = _Cnrdhcpv6FOContactRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 7),
    _Cnrdhcpv6FOContactRcvd_Type()
)
cnrdhcpv6FOContactRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOContactRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOContactRcvd.setUnits("messages")
_Cnrdhcpv6FODisconnectRcvd_Type = Counter32
_Cnrdhcpv6FODisconnectRcvd_Object = MibScalar
cnrdhcpv6FODisconnectRcvd = _Cnrdhcpv6FODisconnectRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 8),
    _Cnrdhcpv6FODisconnectRcvd_Type()
)
cnrdhcpv6FODisconnectRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FODisconnectRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FODisconnectRcvd.setUnits("messages")
_Cnrdhcpv6FOUpdateReqRcvd_Type = Counter32
_Cnrdhcpv6FOUpdateReqRcvd_Object = MibScalar
cnrdhcpv6FOUpdateReqRcvd = _Cnrdhcpv6FOUpdateReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 9),
    _Cnrdhcpv6FOUpdateReqRcvd_Type()
)
cnrdhcpv6FOUpdateReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateReqRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateReqRcvd.setUnits("messages")
_Cnrdhcpv6FOUpdateDoneRcvd_Type = Counter32
_Cnrdhcpv6FOUpdateDoneRcvd_Object = MibScalar
cnrdhcpv6FOUpdateDoneRcvd = _Cnrdhcpv6FOUpdateDoneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 10),
    _Cnrdhcpv6FOUpdateDoneRcvd_Type()
)
cnrdhcpv6FOUpdateDoneRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateDoneRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateDoneRcvd.setUnits("messages")
_Cnrdhcpv6FOPoolRequestsRcvd_Type = Counter32
_Cnrdhcpv6FOPoolRequestsRcvd_Object = MibScalar
cnrdhcpv6FOPoolRequestsRcvd = _Cnrdhcpv6FOPoolRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 11),
    _Cnrdhcpv6FOPoolRequestsRcvd_Type()
)
cnrdhcpv6FOPoolRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolRequestsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolRequestsRcvd.setUnits("messages")
_Cnrdhcpv6FOPoolResponseRcvd_Type = Counter32
_Cnrdhcpv6FOPoolResponseRcvd_Object = MibScalar
cnrdhcpv6FOPoolResponseRcvd = _Cnrdhcpv6FOPoolResponseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 12),
    _Cnrdhcpv6FOPoolResponseRcvd_Type()
)
cnrdhcpv6FOPoolResponseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolResponseRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolResponseRcvd.setUnits("messages")
_Cnrdhcpv6FOStateSent_Type = Counter32
_Cnrdhcpv6FOStateSent_Object = MibScalar
cnrdhcpv6FOStateSent = _Cnrdhcpv6FOStateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 13),
    _Cnrdhcpv6FOStateSent_Type()
)
cnrdhcpv6FOStateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOStateSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOStateSent.setUnits("messages")
_Cnrdhcpv6FOBindingUpdsSent_Type = Counter32
_Cnrdhcpv6FOBindingUpdsSent_Object = MibScalar
cnrdhcpv6FOBindingUpdsSent = _Cnrdhcpv6FOBindingUpdsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 14),
    _Cnrdhcpv6FOBindingUpdsSent_Type()
)
cnrdhcpv6FOBindingUpdsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingUpdsSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingUpdsSent.setUnits("messages")
_Cnrdhcpv6FOBindingAcksSent_Type = Counter32
_Cnrdhcpv6FOBindingAcksSent_Object = MibScalar
cnrdhcpv6FOBindingAcksSent = _Cnrdhcpv6FOBindingAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 15),
    _Cnrdhcpv6FOBindingAcksSent_Type()
)
cnrdhcpv6FOBindingAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingAcksSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingAcksSent.setUnits("messages")
_Cnrdhcpv6FOBindingNaksSent_Type = Counter32
_Cnrdhcpv6FOBindingNaksSent_Object = MibScalar
cnrdhcpv6FOBindingNaksSent = _Cnrdhcpv6FOBindingNaksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 16),
    _Cnrdhcpv6FOBindingNaksSent_Type()
)
cnrdhcpv6FOBindingNaksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingNaksSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOBindingNaksSent.setUnits("messages")
_Cnrdhcpv6FOConnectSent_Type = Counter32
_Cnrdhcpv6FOConnectSent_Object = MibScalar
cnrdhcpv6FOConnectSent = _Cnrdhcpv6FOConnectSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 17),
    _Cnrdhcpv6FOConnectSent_Type()
)
cnrdhcpv6FOConnectSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectSent.setUnits("messages")
_Cnrdhcpv6FOConnectAckSent_Type = Counter32
_Cnrdhcpv6FOConnectAckSent_Object = MibScalar
cnrdhcpv6FOConnectAckSent = _Cnrdhcpv6FOConnectAckSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 18),
    _Cnrdhcpv6FOConnectAckSent_Type()
)
cnrdhcpv6FOConnectAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectAckSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOConnectAckSent.setUnits("messages")
_Cnrdhcpv6FOContactSent_Type = Counter32
_Cnrdhcpv6FOContactSent_Object = MibScalar
cnrdhcpv6FOContactSent = _Cnrdhcpv6FOContactSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 19),
    _Cnrdhcpv6FOContactSent_Type()
)
cnrdhcpv6FOContactSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOContactSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOContactSent.setUnits("messages")
_Cnrdhcpv6FODisconnectSent_Type = Counter32
_Cnrdhcpv6FODisconnectSent_Object = MibScalar
cnrdhcpv6FODisconnectSent = _Cnrdhcpv6FODisconnectSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 20),
    _Cnrdhcpv6FODisconnectSent_Type()
)
cnrdhcpv6FODisconnectSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FODisconnectSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FODisconnectSent.setUnits("messages")
_Cnrdhcpv6FOUpdateReqSent_Type = Counter32
_Cnrdhcpv6FOUpdateReqSent_Object = MibScalar
cnrdhcpv6FOUpdateReqSent = _Cnrdhcpv6FOUpdateReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 21),
    _Cnrdhcpv6FOUpdateReqSent_Type()
)
cnrdhcpv6FOUpdateReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateReqSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateReqSent.setUnits("messages")
_Cnrdhcpv6FOUpdateDoneSent_Type = Counter32
_Cnrdhcpv6FOUpdateDoneSent_Object = MibScalar
cnrdhcpv6FOUpdateDoneSent = _Cnrdhcpv6FOUpdateDoneSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 22),
    _Cnrdhcpv6FOUpdateDoneSent_Type()
)
cnrdhcpv6FOUpdateDoneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateDoneSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOUpdateDoneSent.setUnits("messages")
_Cnrdhcpv6FOPoolRequestSent_Type = Counter32
_Cnrdhcpv6FOPoolRequestSent_Object = MibScalar
cnrdhcpv6FOPoolRequestSent = _Cnrdhcpv6FOPoolRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 23),
    _Cnrdhcpv6FOPoolRequestSent_Type()
)
cnrdhcpv6FOPoolRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolRequestSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolRequestSent.setUnits("messages")
_Cnrdhcpv6FOPoolResponsesSent_Type = Counter32
_Cnrdhcpv6FOPoolResponsesSent_Object = MibScalar
cnrdhcpv6FOPoolResponsesSent = _Cnrdhcpv6FOPoolResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 24),
    _Cnrdhcpv6FOPoolResponsesSent_Type()
)
cnrdhcpv6FOPoolResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolResponsesSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPoolResponsesSent.setUnits("messages")
_Cnrdhcpv6FOInvalidMsgsRcvd_Type = Counter32
_Cnrdhcpv6FOInvalidMsgsRcvd_Object = MibScalar
cnrdhcpv6FOInvalidMsgsRcvd = _Cnrdhcpv6FOInvalidMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 25),
    _Cnrdhcpv6FOInvalidMsgsRcvd_Type()
)
cnrdhcpv6FOInvalidMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOInvalidMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOInvalidMsgsRcvd.setUnits("messages")
_Cnrdhcpv6FODiscardedMsgs_Type = Counter32
_Cnrdhcpv6FODiscardedMsgs_Object = MibScalar
cnrdhcpv6FODiscardedMsgs = _Cnrdhcpv6FODiscardedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 26),
    _Cnrdhcpv6FODiscardedMsgs_Type()
)
cnrdhcpv6FODiscardedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FODiscardedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FODiscardedMsgs.setUnits("messages")
_Cnrdhcpv6FOSuccessConn_Type = Counter32
_Cnrdhcpv6FOSuccessConn_Object = MibScalar
cnrdhcpv6FOSuccessConn = _Cnrdhcpv6FOSuccessConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 27),
    _Cnrdhcpv6FOSuccessConn_Type()
)
cnrdhcpv6FOSuccessConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOSuccessConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOSuccessConn.setUnits("connections")
_Cnrdhcpv6FOFailedConn_Type = Counter32
_Cnrdhcpv6FOFailedConn_Object = MibScalar
cnrdhcpv6FOFailedConn = _Cnrdhcpv6FOFailedConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 28),
    _Cnrdhcpv6FOFailedConn_Type()
)
cnrdhcpv6FOFailedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOFailedConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOFailedConn.setUnits("connections")
_Cnrdhcpv6FOInvalidConn_Type = Counter32
_Cnrdhcpv6FOInvalidConn_Object = MibScalar
cnrdhcpv6FOInvalidConn = _Cnrdhcpv6FOInvalidConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 29),
    _Cnrdhcpv6FOInvalidConn_Type()
)
cnrdhcpv6FOInvalidConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOInvalidConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOInvalidConn.setUnits("connections")
_Cnrdhcpv6FOSelfTermConn_Type = Counter32
_Cnrdhcpv6FOSelfTermConn_Object = MibScalar
cnrdhcpv6FOSelfTermConn = _Cnrdhcpv6FOSelfTermConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 30),
    _Cnrdhcpv6FOSelfTermConn_Type()
)
cnrdhcpv6FOSelfTermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOSelfTermConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOSelfTermConn.setUnits("connections")
_Cnrdhcpv6FOPeerTermConn_Type = Counter32
_Cnrdhcpv6FOPeerTermConn_Object = MibScalar
cnrdhcpv6FOPeerTermConn = _Cnrdhcpv6FOPeerTermConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 4, 31),
    _Cnrdhcpv6FOPeerTermConn_Type()
)
cnrdhcpv6FOPeerTermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeerTermConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeerTermConn.setUnits("connections")
_CiscoNetRegDhcpv6FailoverPeriodCounters_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6FailoverPeriodCounters = _CiscoNetRegDhcpv6FailoverPeriodCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5)
)
_Cnrdhcpv6FOPeriodStateRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodStateRcvd_Object = MibScalar
cnrdhcpv6FOPeriodStateRcvd = _Cnrdhcpv6FOPeriodStateRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 1),
    _Cnrdhcpv6FOPeriodStateRcvd_Type()
)
cnrdhcpv6FOPeriodStateRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodStateRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodStateRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodBindingUpdsRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodBindingUpdsRcvd_Object = MibScalar
cnrdhcpv6FOPeriodBindingUpdsRcvd = _Cnrdhcpv6FOPeriodBindingUpdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 2),
    _Cnrdhcpv6FOPeriodBindingUpdsRcvd_Type()
)
cnrdhcpv6FOPeriodBindingUpdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingUpdsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingUpdsRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodBindingAcksRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodBindingAcksRcvd_Object = MibScalar
cnrdhcpv6FOPeriodBindingAcksRcvd = _Cnrdhcpv6FOPeriodBindingAcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 3),
    _Cnrdhcpv6FOPeriodBindingAcksRcvd_Type()
)
cnrdhcpv6FOPeriodBindingAcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingAcksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingAcksRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodBindingNaksRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodBindingNaksRcvd_Object = MibScalar
cnrdhcpv6FOPeriodBindingNaksRcvd = _Cnrdhcpv6FOPeriodBindingNaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 4),
    _Cnrdhcpv6FOPeriodBindingNaksRcvd_Type()
)
cnrdhcpv6FOPeriodBindingNaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingNaksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingNaksRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodConnectRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodConnectRcvd_Object = MibScalar
cnrdhcpv6FOPeriodConnectRcvd = _Cnrdhcpv6FOPeriodConnectRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 5),
    _Cnrdhcpv6FOPeriodConnectRcvd_Type()
)
cnrdhcpv6FOPeriodConnectRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodConnectAckRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodConnectAckRcvd_Object = MibScalar
cnrdhcpv6FOPeriodConnectAckRcvd = _Cnrdhcpv6FOPeriodConnectAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 6),
    _Cnrdhcpv6FOPeriodConnectAckRcvd_Type()
)
cnrdhcpv6FOPeriodConnectAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectAckRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectAckRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodContactRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodContactRcvd_Object = MibScalar
cnrdhcpv6FOPeriodContactRcvd = _Cnrdhcpv6FOPeriodContactRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 7),
    _Cnrdhcpv6FOPeriodContactRcvd_Type()
)
cnrdhcpv6FOPeriodContactRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodContactRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodContactRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodDisconnectRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodDisconnectRcvd_Object = MibScalar
cnrdhcpv6FOPeriodDisconnectRcvd = _Cnrdhcpv6FOPeriodDisconnectRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 8),
    _Cnrdhcpv6FOPeriodDisconnectRcvd_Type()
)
cnrdhcpv6FOPeriodDisconnectRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodDisconnectRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodDisconnectRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodUpdateReqRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodUpdateReqRcvd_Object = MibScalar
cnrdhcpv6FOPeriodUpdateReqRcvd = _Cnrdhcpv6FOPeriodUpdateReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 9),
    _Cnrdhcpv6FOPeriodUpdateReqRcvd_Type()
)
cnrdhcpv6FOPeriodUpdateReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateReqRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateReqRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodUpdateDoneRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodUpdateDoneRcvd_Object = MibScalar
cnrdhcpv6FOPeriodUpdateDoneRcvd = _Cnrdhcpv6FOPeriodUpdateDoneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 10),
    _Cnrdhcpv6FOPeriodUpdateDoneRcvd_Type()
)
cnrdhcpv6FOPeriodUpdateDoneRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateDoneRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateDoneRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodPoolRequestsRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodPoolRequestsRcvd_Object = MibScalar
cnrdhcpv6FOPeriodPoolRequestsRcvd = _Cnrdhcpv6FOPeriodPoolRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 11),
    _Cnrdhcpv6FOPeriodPoolRequestsRcvd_Type()
)
cnrdhcpv6FOPeriodPoolRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolRequestsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolRequestsRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodPoolResponseRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodPoolResponseRcvd_Object = MibScalar
cnrdhcpv6FOPeriodPoolResponseRcvd = _Cnrdhcpv6FOPeriodPoolResponseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 12),
    _Cnrdhcpv6FOPeriodPoolResponseRcvd_Type()
)
cnrdhcpv6FOPeriodPoolResponseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolResponseRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolResponseRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodStateSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodStateSent_Object = MibScalar
cnrdhcpv6FOPeriodStateSent = _Cnrdhcpv6FOPeriodStateSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 13),
    _Cnrdhcpv6FOPeriodStateSent_Type()
)
cnrdhcpv6FOPeriodStateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodStateSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodStateSent.setUnits("messages")
_Cnrdhcpv6FOPeriodBindingUpdsSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodBindingUpdsSent_Object = MibScalar
cnrdhcpv6FOPeriodBindingUpdsSent = _Cnrdhcpv6FOPeriodBindingUpdsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 14),
    _Cnrdhcpv6FOPeriodBindingUpdsSent_Type()
)
cnrdhcpv6FOPeriodBindingUpdsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingUpdsSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingUpdsSent.setUnits("messages")
_Cnrdhcpv6FOPeriodBindingAcksSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodBindingAcksSent_Object = MibScalar
cnrdhcpv6FOPeriodBindingAcksSent = _Cnrdhcpv6FOPeriodBindingAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 15),
    _Cnrdhcpv6FOPeriodBindingAcksSent_Type()
)
cnrdhcpv6FOPeriodBindingAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingAcksSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingAcksSent.setUnits("messages")
_Cnrdhcpv6FOPeriodBindingNaksSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodBindingNaksSent_Object = MibScalar
cnrdhcpv6FOPeriodBindingNaksSent = _Cnrdhcpv6FOPeriodBindingNaksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 16),
    _Cnrdhcpv6FOPeriodBindingNaksSent_Type()
)
cnrdhcpv6FOPeriodBindingNaksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingNaksSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodBindingNaksSent.setUnits("messages")
_Cnrdhcpv6FOPeriodConnectSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodConnectSent_Object = MibScalar
cnrdhcpv6FOPeriodConnectSent = _Cnrdhcpv6FOPeriodConnectSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 17),
    _Cnrdhcpv6FOPeriodConnectSent_Type()
)
cnrdhcpv6FOPeriodConnectSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectSent.setUnits("messages")
_Cnrdhcpv6FOPeriodConnectAckSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodConnectAckSent_Object = MibScalar
cnrdhcpv6FOPeriodConnectAckSent = _Cnrdhcpv6FOPeriodConnectAckSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 18),
    _Cnrdhcpv6FOPeriodConnectAckSent_Type()
)
cnrdhcpv6FOPeriodConnectAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectAckSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodConnectAckSent.setUnits("messages")
_Cnrdhcpv6FOPeriodContactSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodContactSent_Object = MibScalar
cnrdhcpv6FOPeriodContactSent = _Cnrdhcpv6FOPeriodContactSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 19),
    _Cnrdhcpv6FOPeriodContactSent_Type()
)
cnrdhcpv6FOPeriodContactSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodContactSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodContactSent.setUnits("messages")
_Cnrdhcpv6FOPeriodDisconnectSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodDisconnectSent_Object = MibScalar
cnrdhcpv6FOPeriodDisconnectSent = _Cnrdhcpv6FOPeriodDisconnectSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 20),
    _Cnrdhcpv6FOPeriodDisconnectSent_Type()
)
cnrdhcpv6FOPeriodDisconnectSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodDisconnectSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodDisconnectSent.setUnits("messages")
_Cnrdhcpv6FOPeriodUpdateReqSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodUpdateReqSent_Object = MibScalar
cnrdhcpv6FOPeriodUpdateReqSent = _Cnrdhcpv6FOPeriodUpdateReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 21),
    _Cnrdhcpv6FOPeriodUpdateReqSent_Type()
)
cnrdhcpv6FOPeriodUpdateReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateReqSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateReqSent.setUnits("messages")
_Cnrdhcpv6FOPeriodUpdateDoneSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodUpdateDoneSent_Object = MibScalar
cnrdhcpv6FOPeriodUpdateDoneSent = _Cnrdhcpv6FOPeriodUpdateDoneSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 22),
    _Cnrdhcpv6FOPeriodUpdateDoneSent_Type()
)
cnrdhcpv6FOPeriodUpdateDoneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateDoneSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodUpdateDoneSent.setUnits("messages")
_Cnrdhcpv6FOPeriodPoolRequestSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodPoolRequestSent_Object = MibScalar
cnrdhcpv6FOPeriodPoolRequestSent = _Cnrdhcpv6FOPeriodPoolRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 23),
    _Cnrdhcpv6FOPeriodPoolRequestSent_Type()
)
cnrdhcpv6FOPeriodPoolRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolRequestSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolRequestSent.setUnits("messages")
_Cnrdhcpv6FOPeriodPoolResponsesSent_Type = Unsigned32
_Cnrdhcpv6FOPeriodPoolResponsesSent_Object = MibScalar
cnrdhcpv6FOPeriodPoolResponsesSent = _Cnrdhcpv6FOPeriodPoolResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 24),
    _Cnrdhcpv6FOPeriodPoolResponsesSent_Type()
)
cnrdhcpv6FOPeriodPoolResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolResponsesSent.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPoolResponsesSent.setUnits("messages")
_Cnrdhcpv6FOPeriodInvalidMsgsRcvd_Type = Unsigned32
_Cnrdhcpv6FOPeriodInvalidMsgsRcvd_Object = MibScalar
cnrdhcpv6FOPeriodInvalidMsgsRcvd = _Cnrdhcpv6FOPeriodInvalidMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 25),
    _Cnrdhcpv6FOPeriodInvalidMsgsRcvd_Type()
)
cnrdhcpv6FOPeriodInvalidMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodInvalidMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodInvalidMsgsRcvd.setUnits("messages")
_Cnrdhcpv6FOPeriodDiscardedMsgs_Type = Unsigned32
_Cnrdhcpv6FOPeriodDiscardedMsgs_Object = MibScalar
cnrdhcpv6FOPeriodDiscardedMsgs = _Cnrdhcpv6FOPeriodDiscardedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 26),
    _Cnrdhcpv6FOPeriodDiscardedMsgs_Type()
)
cnrdhcpv6FOPeriodDiscardedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodDiscardedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodDiscardedMsgs.setUnits("messages")
_Cnrdhcpv6FOPeriodSuccessConn_Type = Unsigned32
_Cnrdhcpv6FOPeriodSuccessConn_Object = MibScalar
cnrdhcpv6FOPeriodSuccessConn = _Cnrdhcpv6FOPeriodSuccessConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 27),
    _Cnrdhcpv6FOPeriodSuccessConn_Type()
)
cnrdhcpv6FOPeriodSuccessConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodSuccessConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodSuccessConn.setUnits("connections")
_Cnrdhcpv6FOPeriodFailedConn_Type = Unsigned32
_Cnrdhcpv6FOPeriodFailedConn_Object = MibScalar
cnrdhcpv6FOPeriodFailedConn = _Cnrdhcpv6FOPeriodFailedConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 28),
    _Cnrdhcpv6FOPeriodFailedConn_Type()
)
cnrdhcpv6FOPeriodFailedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodFailedConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodFailedConn.setUnits("connections")
_Cnrdhcpv6FOPeriodInvalidConn_Type = Unsigned32
_Cnrdhcpv6FOPeriodInvalidConn_Object = MibScalar
cnrdhcpv6FOPeriodInvalidConn = _Cnrdhcpv6FOPeriodInvalidConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 29),
    _Cnrdhcpv6FOPeriodInvalidConn_Type()
)
cnrdhcpv6FOPeriodInvalidConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodInvalidConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodInvalidConn.setUnits("connections")
_Cnrdhcpv6FOPeriodSelfTermConn_Type = Unsigned32
_Cnrdhcpv6FOPeriodSelfTermConn_Object = MibScalar
cnrdhcpv6FOPeriodSelfTermConn = _Cnrdhcpv6FOPeriodSelfTermConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 30),
    _Cnrdhcpv6FOPeriodSelfTermConn_Type()
)
cnrdhcpv6FOPeriodSelfTermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodSelfTermConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodSelfTermConn.setUnits("connections")
_Cnrdhcpv6FOPeriodPeerTermConn_Type = Unsigned32
_Cnrdhcpv6FOPeriodPeerTermConn_Object = MibScalar
cnrdhcpv6FOPeriodPeerTermConn = _Cnrdhcpv6FOPeriodPeerTermConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 31),
    _Cnrdhcpv6FOPeriodPeerTermConn_Type()
)
cnrdhcpv6FOPeriodPeerTermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPeerTermConn.setStatus("current")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodPeerTermConn.setUnits("connections")
_Cnrdhcpv6FOPeriodStartTime_Type = TimeStamp
_Cnrdhcpv6FOPeriodStartTime_Object = MibScalar
cnrdhcpv6FOPeriodStartTime = _Cnrdhcpv6FOPeriodStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 32),
    _Cnrdhcpv6FOPeriodStartTime_Type()
)
cnrdhcpv6FOPeriodStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodStartTime.setStatus("current")
_Cnrdhcpv6FOPeriodEndTime_Type = TimeStamp
_Cnrdhcpv6FOPeriodEndTime_Object = MibScalar
cnrdhcpv6FOPeriodEndTime = _Cnrdhcpv6FOPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 1, 5, 33),
    _Cnrdhcpv6FOPeriodEndTime_Type()
)
cnrdhcpv6FOPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnrdhcpv6FOPeriodEndTime.setStatus("current")
_CiscoNetRegDhcpv6MIBConform_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6MIBConform = _CiscoNetRegDhcpv6MIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2)
)
_CiscoNetRegDhcpv6MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6MIBCompliances = _CiscoNetRegDhcpv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 1)
)
_CiscoNetRegDhcpv6MIBGroups_ObjectIdentity = ObjectIdentity
ciscoNetRegDhcpv6MIBGroups = _CiscoNetRegDhcpv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2)
)

# Managed Objects groups

ciscoNetRegDhcpv6TotalCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2, 1)
)
ciscoNetRegDhcpv6TotalCountersGroup.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalPacketsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalPacketsRcvdRelay"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalSolicits"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalRequests"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalConfirms"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalRenews"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalRebinds"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalReleases"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalDeclines"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalInfoRequests"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalInvalidPackets"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalPacketsSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalPacketsSentRelay"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalAdvertises"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalReplies"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalReconfigures"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalAuthFails"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalDiscards"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalDuplicates"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalInvalidClients"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalUnknownLinks"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalDroppedConfig"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalDroppedOthers"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalActiveLeases"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalAllocatedLeases"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalReservedLeases"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalReservedActiveLeases"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalLeaseQueries"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalLeaseQueryReplies"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalExtensionErrors"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TotalExtensionDrops"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6TotalCountersGroup.setStatus("current")

ciscoNetRegDhcpv6NotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2, 3)
)
ciscoNetRegDhcpv6NotificationObjectsGroup.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupIpv6Address"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ClientId"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ClientLookupKey"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupIpv6AddressDetectedBy"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6LinkName"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FreeAddressValue"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6Threshold"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PrefixAddress"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ThresholdType"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TypeDesc"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupPrefix"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupPrefixDetectedBy"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupPrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PartnerServerAddr"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PartnerServerIpv6Addr"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ContestedIpv6Address"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ContestedIpv6Prefix"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ContestedIpv6PrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FailoverPairName"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6NotificationObjectsGroup.setStatus("current")

ciscoNetRegDhcpv6PeriodCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2, 4)
)
ciscoNetRegDhcpv6PeriodCountersGroup.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodPacketsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodPacketsRcvdRelay"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodSolicits"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodRequests"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodConfirms"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodRenews"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodRebinds"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodReleases"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodDeclines"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodInfoRequests"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodInvalidPackets"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodPacketsSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodPacketsSentRelay"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodAdvertises"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodReplies"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodReconfigures"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodAuthFails"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodDiscards"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodDuplicates"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodInvalidClients"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodUnknownLinks"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodDroppedConfig"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodDroppedOthers"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodLeaseQueries"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodLeaseQueryReplies"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodStartTime"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodEndTime"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodExtensionErrors"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PeriodExtensionDrops"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6PeriodCountersGroup.setStatus("current")

ciscoNetRegDhcpv6FailoverCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2, 5)
)
ciscoNetRegDhcpv6FailoverCountersGroup.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOStateRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOBindingUpdsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOBindingAcksRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOBindingNaksRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOConnectRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOConnectAckRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOContactRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FODisconnectRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOUpdateReqRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOUpdateDoneRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPoolRequestsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPoolResponseRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOStateSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOBindingUpdsSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOBindingAcksSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOBindingNaksSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOConnectSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOConnectAckSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOContactSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FODisconnectSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOUpdateReqSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOUpdateDoneSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPoolRequestSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPoolResponsesSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOInvalidMsgsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FODiscardedMsgs"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOSuccessConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOFailedConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOInvalidConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOSelfTermConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeerTermConn"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6FailoverCountersGroup.setStatus("current")

ciscoNetRegDhcpv6FailoverPeriodCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2, 6)
)
ciscoNetRegDhcpv6FailoverPeriodCountersGroup.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodStateRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodBindingUpdsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodBindingAcksRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodBindingNaksRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodConnectRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodConnectAckRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodContactRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodDisconnectRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodUpdateReqRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodUpdateDoneRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodPoolRequestsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodPoolResponseRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodStateSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodBindingUpdsSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodBindingAcksSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodBindingNaksSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodConnectSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodConnectAckSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodContactSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodDisconnectSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodUpdateReqSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodUpdateDoneSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodPoolRequestSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodPoolResponsesSent"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodInvalidMsgsRcvd"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodDiscardedMsgs"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodSuccessConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodFailedConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodInvalidConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodSelfTermConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodPeerTermConn"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodStartTime"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FOPeriodEndTime"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6FailoverPeriodCountersGroup.setStatus("current")


# Notification objects

ciscoNetRegDhcpv6AddressShortageStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0, 1)
)
ciscoNetRegDhcpv6AddressShortageStart.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6LinkName"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FreeAddressValue"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6Threshold"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PrefixAddress"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ThresholdType"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TypeDesc"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6AddressShortageStart.setStatus(
        "current"
    )

ciscoNetRegDhcpv6AddressShortageStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0, 2)
)
ciscoNetRegDhcpv6AddressShortageStop.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6LinkName"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FreeAddressValue"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6Threshold"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PrefixAddress"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ThresholdType"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6TypeDesc"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6AddressShortageStop.setStatus(
        "current"
    )

ciscoNetRegDhcpv6DuplicateAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0, 3)
)
ciscoNetRegDhcpv6DuplicateAddress.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupIpv6Address"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ClientId"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ClientLookupKey"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupIpv6AddressDetectedBy"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6DuplicateAddress.setStatus(
        "current"
    )

ciscoNetRegDhcpv6DuplicatePrefix = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0, 4)
)
ciscoNetRegDhcpv6DuplicatePrefix.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupPrefix"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupPrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ClientId"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ClientLookupKey"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6DupPrefixDetectedBy"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6DuplicatePrefix.setStatus(
        "deprecated"
    )

ciscoNetRegDhcpv6AddressConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0, 5)
)
ciscoNetRegDhcpv6AddressConflict.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PartnerServerAddr"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PartnerServerIpv6Addr"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ContestedIpv6Address"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FailoverPairName"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6AddressConflict.setStatus(
        "current"
    )

ciscoNetRegDhcpv6PrefixConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 0, 6)
)
ciscoNetRegDhcpv6PrefixConflict.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PartnerServerAddr"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6PartnerServerIpv6Addr"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ContestedIpv6Prefix"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6ContestedIpv6PrefixLength"),
        ("CISCO-NETREG-DHCPV6-MIB", "cnrdhcpv6FailoverPairName"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6PrefixConflict.setStatus(
        "current"
    )


# Notifications groups

ciscoNetRegDhcpv6NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 2, 2)
)
ciscoNetRegDhcpv6NotificationsGroup.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6AddressShortageStart"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6AddressShortageStop"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6DuplicateAddress"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6DuplicatePrefix"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6AddressConflict"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6PrefixConflict"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoNetRegDhcpv6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 139, 2, 1, 1)
)
ciscoNetRegDhcpv6MIBCompliance.setObjects(
      *(("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6TotalCountersGroup"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6NotificationsGroup"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6NotificationObjectsGroup"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6PeriodCountersGroup"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6FailoverCountersGroup"),
        ("CISCO-NETREG-DHCPV6-MIB", "ciscoNetRegDhcpv6FailoverPeriodCountersGroup"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDhcpv6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETREG-DHCPV6-MIB",
    **{"ciscoNetRegDhcpv6MIB": ciscoNetRegDhcpv6MIB,
       "ciscoNetRegDhcpv6MIBNotifs": ciscoNetRegDhcpv6MIBNotifs,
       "ciscoNetRegDhcpv6AddressShortageStart": ciscoNetRegDhcpv6AddressShortageStart,
       "ciscoNetRegDhcpv6AddressShortageStop": ciscoNetRegDhcpv6AddressShortageStop,
       "ciscoNetRegDhcpv6DuplicateAddress": ciscoNetRegDhcpv6DuplicateAddress,
       "ciscoNetRegDhcpv6DuplicatePrefix": ciscoNetRegDhcpv6DuplicatePrefix,
       "ciscoNetRegDhcpv6AddressConflict": ciscoNetRegDhcpv6AddressConflict,
       "ciscoNetRegDhcpv6PrefixConflict": ciscoNetRegDhcpv6PrefixConflict,
       "ciscoNetRegDhcpv6MIBObjects": ciscoNetRegDhcpv6MIBObjects,
       "ciscoNetRegDhcpv6NotifObjects": ciscoNetRegDhcpv6NotifObjects,
       "cnrdhcpv6LinkName": cnrdhcpv6LinkName,
       "cnrdhcpv6FreeAddressValue": cnrdhcpv6FreeAddressValue,
       "cnrdhcpv6Threshold": cnrdhcpv6Threshold,
       "cnrdhcpv6PrefixAddress": cnrdhcpv6PrefixAddress,
       "cnrdhcpv6PrefixLength": cnrdhcpv6PrefixLength,
       "cnrdhcpv6ThresholdType": cnrdhcpv6ThresholdType,
       "cnrdhcpv6TypeDesc": cnrdhcpv6TypeDesc,
       "cnrdhcpv6DupIpv6Address": cnrdhcpv6DupIpv6Address,
       "cnrdhcpv6ClientId": cnrdhcpv6ClientId,
       "cnrdhcpv6ClientLookupKey": cnrdhcpv6ClientLookupKey,
       "cnrdhcpv6DupIpv6AddressDetectedBy": cnrdhcpv6DupIpv6AddressDetectedBy,
       "cnrdhcpv6DupPrefix": cnrdhcpv6DupPrefix,
       "cnrdhcpv6DupPrefixLength": cnrdhcpv6DupPrefixLength,
       "cnrdhcpv6DupPrefixDetectedBy": cnrdhcpv6DupPrefixDetectedBy,
       "cnrdhcpv6PartnerServerAddr": cnrdhcpv6PartnerServerAddr,
       "cnrdhcpv6PartnerServerIpv6Addr": cnrdhcpv6PartnerServerIpv6Addr,
       "cnrdhcpv6ContestedIpv6Address": cnrdhcpv6ContestedIpv6Address,
       "cnrdhcpv6ContestedIpv6Prefix": cnrdhcpv6ContestedIpv6Prefix,
       "cnrdhcpv6ContestedIpv6PrefixLength": cnrdhcpv6ContestedIpv6PrefixLength,
       "cnrdhcpv6FailoverPairName": cnrdhcpv6FailoverPairName,
       "ciscoNetRegDhcpv6TotalCounters": ciscoNetRegDhcpv6TotalCounters,
       "cnrdhcpv6TotalPacketsRcvd": cnrdhcpv6TotalPacketsRcvd,
       "cnrdhcpv6TotalPacketsRcvdRelay": cnrdhcpv6TotalPacketsRcvdRelay,
       "cnrdhcpv6TotalSolicits": cnrdhcpv6TotalSolicits,
       "cnrdhcpv6TotalRequests": cnrdhcpv6TotalRequests,
       "cnrdhcpv6TotalConfirms": cnrdhcpv6TotalConfirms,
       "cnrdhcpv6TotalRenews": cnrdhcpv6TotalRenews,
       "cnrdhcpv6TotalRebinds": cnrdhcpv6TotalRebinds,
       "cnrdhcpv6TotalReleases": cnrdhcpv6TotalReleases,
       "cnrdhcpv6TotalDeclines": cnrdhcpv6TotalDeclines,
       "cnrdhcpv6TotalInfoRequests": cnrdhcpv6TotalInfoRequests,
       "cnrdhcpv6TotalInvalidPackets": cnrdhcpv6TotalInvalidPackets,
       "cnrdhcpv6TotalPacketsSent": cnrdhcpv6TotalPacketsSent,
       "cnrdhcpv6TotalPacketsSentRelay": cnrdhcpv6TotalPacketsSentRelay,
       "cnrdhcpv6TotalAdvertises": cnrdhcpv6TotalAdvertises,
       "cnrdhcpv6TotalReplies": cnrdhcpv6TotalReplies,
       "cnrdhcpv6TotalReconfigures": cnrdhcpv6TotalReconfigures,
       "cnrdhcpv6TotalAuthFails": cnrdhcpv6TotalAuthFails,
       "cnrdhcpv6TotalDiscards": cnrdhcpv6TotalDiscards,
       "cnrdhcpv6TotalDuplicates": cnrdhcpv6TotalDuplicates,
       "cnrdhcpv6TotalInvalidClients": cnrdhcpv6TotalInvalidClients,
       "cnrdhcpv6TotalUnknownLinks": cnrdhcpv6TotalUnknownLinks,
       "cnrdhcpv6TotalDroppedOthers": cnrdhcpv6TotalDroppedOthers,
       "cnrdhcpv6TotalDroppedConfig": cnrdhcpv6TotalDroppedConfig,
       "cnrdhcpv6TotalActiveLeases": cnrdhcpv6TotalActiveLeases,
       "cnrdhcpv6TotalAllocatedLeases": cnrdhcpv6TotalAllocatedLeases,
       "cnrdhcpv6TotalReservedLeases": cnrdhcpv6TotalReservedLeases,
       "cnrdhcpv6TotalReservedActiveLeases": cnrdhcpv6TotalReservedActiveLeases,
       "cnrdhcpv6TotalLeaseQueries": cnrdhcpv6TotalLeaseQueries,
       "cnrdhcpv6TotalLeaseQueryReplies": cnrdhcpv6TotalLeaseQueryReplies,
       "cnrdhcpv6TotalExtensionErrors": cnrdhcpv6TotalExtensionErrors,
       "cnrdhcpv6TotalExtensionDrops": cnrdhcpv6TotalExtensionDrops,
       "ciscoNetRegDhcpv6PeriodCounters": ciscoNetRegDhcpv6PeriodCounters,
       "cnrdhcpv6PeriodPacketsRcvd": cnrdhcpv6PeriodPacketsRcvd,
       "cnrdhcpv6PeriodPacketsRcvdRelay": cnrdhcpv6PeriodPacketsRcvdRelay,
       "cnrdhcpv6PeriodSolicits": cnrdhcpv6PeriodSolicits,
       "cnrdhcpv6PeriodRequests": cnrdhcpv6PeriodRequests,
       "cnrdhcpv6PeriodConfirms": cnrdhcpv6PeriodConfirms,
       "cnrdhcpv6PeriodRenews": cnrdhcpv6PeriodRenews,
       "cnrdhcpv6PeriodRebinds": cnrdhcpv6PeriodRebinds,
       "cnrdhcpv6PeriodReleases": cnrdhcpv6PeriodReleases,
       "cnrdhcpv6PeriodDeclines": cnrdhcpv6PeriodDeclines,
       "cnrdhcpv6PeriodInfoRequests": cnrdhcpv6PeriodInfoRequests,
       "cnrdhcpv6PeriodInvalidPackets": cnrdhcpv6PeriodInvalidPackets,
       "cnrdhcpv6PeriodPacketsSent": cnrdhcpv6PeriodPacketsSent,
       "cnrdhcpv6PeriodPacketsSentRelay": cnrdhcpv6PeriodPacketsSentRelay,
       "cnrdhcpv6PeriodAdvertises": cnrdhcpv6PeriodAdvertises,
       "cnrdhcpv6PeriodReplies": cnrdhcpv6PeriodReplies,
       "cnrdhcpv6PeriodReconfigures": cnrdhcpv6PeriodReconfigures,
       "cnrdhcpv6PeriodAuthFails": cnrdhcpv6PeriodAuthFails,
       "cnrdhcpv6PeriodDiscards": cnrdhcpv6PeriodDiscards,
       "cnrdhcpv6PeriodDuplicates": cnrdhcpv6PeriodDuplicates,
       "cnrdhcpv6PeriodInvalidClients": cnrdhcpv6PeriodInvalidClients,
       "cnrdhcpv6PeriodUnknownLinks": cnrdhcpv6PeriodUnknownLinks,
       "cnrdhcpv6PeriodDroppedOthers": cnrdhcpv6PeriodDroppedOthers,
       "cnrdhcpv6PeriodDroppedConfig": cnrdhcpv6PeriodDroppedConfig,
       "cnrdhcpv6PeriodLeaseQueries": cnrdhcpv6PeriodLeaseQueries,
       "cnrdhcpv6PeriodLeaseQueryReplies": cnrdhcpv6PeriodLeaseQueryReplies,
       "cnrdhcpv6PeriodStartTime": cnrdhcpv6PeriodStartTime,
       "cnrdhcpv6PeriodEndTime": cnrdhcpv6PeriodEndTime,
       "cnrdhcpv6PeriodExtensionErrors": cnrdhcpv6PeriodExtensionErrors,
       "cnrdhcpv6PeriodExtensionDrops": cnrdhcpv6PeriodExtensionDrops,
       "ciscoNetRegDhcpv6FailoverCounters": ciscoNetRegDhcpv6FailoverCounters,
       "cnrdhcpv6FOStateRcvd": cnrdhcpv6FOStateRcvd,
       "cnrdhcpv6FOBindingUpdsRcvd": cnrdhcpv6FOBindingUpdsRcvd,
       "cnrdhcpv6FOBindingAcksRcvd": cnrdhcpv6FOBindingAcksRcvd,
       "cnrdhcpv6FOBindingNaksRcvd": cnrdhcpv6FOBindingNaksRcvd,
       "cnrdhcpv6FOConnectRcvd": cnrdhcpv6FOConnectRcvd,
       "cnrdhcpv6FOConnectAckRcvd": cnrdhcpv6FOConnectAckRcvd,
       "cnrdhcpv6FOContactRcvd": cnrdhcpv6FOContactRcvd,
       "cnrdhcpv6FODisconnectRcvd": cnrdhcpv6FODisconnectRcvd,
       "cnrdhcpv6FOUpdateReqRcvd": cnrdhcpv6FOUpdateReqRcvd,
       "cnrdhcpv6FOUpdateDoneRcvd": cnrdhcpv6FOUpdateDoneRcvd,
       "cnrdhcpv6FOPoolRequestsRcvd": cnrdhcpv6FOPoolRequestsRcvd,
       "cnrdhcpv6FOPoolResponseRcvd": cnrdhcpv6FOPoolResponseRcvd,
       "cnrdhcpv6FOStateSent": cnrdhcpv6FOStateSent,
       "cnrdhcpv6FOBindingUpdsSent": cnrdhcpv6FOBindingUpdsSent,
       "cnrdhcpv6FOBindingAcksSent": cnrdhcpv6FOBindingAcksSent,
       "cnrdhcpv6FOBindingNaksSent": cnrdhcpv6FOBindingNaksSent,
       "cnrdhcpv6FOConnectSent": cnrdhcpv6FOConnectSent,
       "cnrdhcpv6FOConnectAckSent": cnrdhcpv6FOConnectAckSent,
       "cnrdhcpv6FOContactSent": cnrdhcpv6FOContactSent,
       "cnrdhcpv6FODisconnectSent": cnrdhcpv6FODisconnectSent,
       "cnrdhcpv6FOUpdateReqSent": cnrdhcpv6FOUpdateReqSent,
       "cnrdhcpv6FOUpdateDoneSent": cnrdhcpv6FOUpdateDoneSent,
       "cnrdhcpv6FOPoolRequestSent": cnrdhcpv6FOPoolRequestSent,
       "cnrdhcpv6FOPoolResponsesSent": cnrdhcpv6FOPoolResponsesSent,
       "cnrdhcpv6FOInvalidMsgsRcvd": cnrdhcpv6FOInvalidMsgsRcvd,
       "cnrdhcpv6FODiscardedMsgs": cnrdhcpv6FODiscardedMsgs,
       "cnrdhcpv6FOSuccessConn": cnrdhcpv6FOSuccessConn,
       "cnrdhcpv6FOFailedConn": cnrdhcpv6FOFailedConn,
       "cnrdhcpv6FOInvalidConn": cnrdhcpv6FOInvalidConn,
       "cnrdhcpv6FOSelfTermConn": cnrdhcpv6FOSelfTermConn,
       "cnrdhcpv6FOPeerTermConn": cnrdhcpv6FOPeerTermConn,
       "ciscoNetRegDhcpv6FailoverPeriodCounters": ciscoNetRegDhcpv6FailoverPeriodCounters,
       "cnrdhcpv6FOPeriodStateRcvd": cnrdhcpv6FOPeriodStateRcvd,
       "cnrdhcpv6FOPeriodBindingUpdsRcvd": cnrdhcpv6FOPeriodBindingUpdsRcvd,
       "cnrdhcpv6FOPeriodBindingAcksRcvd": cnrdhcpv6FOPeriodBindingAcksRcvd,
       "cnrdhcpv6FOPeriodBindingNaksRcvd": cnrdhcpv6FOPeriodBindingNaksRcvd,
       "cnrdhcpv6FOPeriodConnectRcvd": cnrdhcpv6FOPeriodConnectRcvd,
       "cnrdhcpv6FOPeriodConnectAckRcvd": cnrdhcpv6FOPeriodConnectAckRcvd,
       "cnrdhcpv6FOPeriodContactRcvd": cnrdhcpv6FOPeriodContactRcvd,
       "cnrdhcpv6FOPeriodDisconnectRcvd": cnrdhcpv6FOPeriodDisconnectRcvd,
       "cnrdhcpv6FOPeriodUpdateReqRcvd": cnrdhcpv6FOPeriodUpdateReqRcvd,
       "cnrdhcpv6FOPeriodUpdateDoneRcvd": cnrdhcpv6FOPeriodUpdateDoneRcvd,
       "cnrdhcpv6FOPeriodPoolRequestsRcvd": cnrdhcpv6FOPeriodPoolRequestsRcvd,
       "cnrdhcpv6FOPeriodPoolResponseRcvd": cnrdhcpv6FOPeriodPoolResponseRcvd,
       "cnrdhcpv6FOPeriodStateSent": cnrdhcpv6FOPeriodStateSent,
       "cnrdhcpv6FOPeriodBindingUpdsSent": cnrdhcpv6FOPeriodBindingUpdsSent,
       "cnrdhcpv6FOPeriodBindingAcksSent": cnrdhcpv6FOPeriodBindingAcksSent,
       "cnrdhcpv6FOPeriodBindingNaksSent": cnrdhcpv6FOPeriodBindingNaksSent,
       "cnrdhcpv6FOPeriodConnectSent": cnrdhcpv6FOPeriodConnectSent,
       "cnrdhcpv6FOPeriodConnectAckSent": cnrdhcpv6FOPeriodConnectAckSent,
       "cnrdhcpv6FOPeriodContactSent": cnrdhcpv6FOPeriodContactSent,
       "cnrdhcpv6FOPeriodDisconnectSent": cnrdhcpv6FOPeriodDisconnectSent,
       "cnrdhcpv6FOPeriodUpdateReqSent": cnrdhcpv6FOPeriodUpdateReqSent,
       "cnrdhcpv6FOPeriodUpdateDoneSent": cnrdhcpv6FOPeriodUpdateDoneSent,
       "cnrdhcpv6FOPeriodPoolRequestSent": cnrdhcpv6FOPeriodPoolRequestSent,
       "cnrdhcpv6FOPeriodPoolResponsesSent": cnrdhcpv6FOPeriodPoolResponsesSent,
       "cnrdhcpv6FOPeriodInvalidMsgsRcvd": cnrdhcpv6FOPeriodInvalidMsgsRcvd,
       "cnrdhcpv6FOPeriodDiscardedMsgs": cnrdhcpv6FOPeriodDiscardedMsgs,
       "cnrdhcpv6FOPeriodSuccessConn": cnrdhcpv6FOPeriodSuccessConn,
       "cnrdhcpv6FOPeriodFailedConn": cnrdhcpv6FOPeriodFailedConn,
       "cnrdhcpv6FOPeriodInvalidConn": cnrdhcpv6FOPeriodInvalidConn,
       "cnrdhcpv6FOPeriodSelfTermConn": cnrdhcpv6FOPeriodSelfTermConn,
       "cnrdhcpv6FOPeriodPeerTermConn": cnrdhcpv6FOPeriodPeerTermConn,
       "cnrdhcpv6FOPeriodStartTime": cnrdhcpv6FOPeriodStartTime,
       "cnrdhcpv6FOPeriodEndTime": cnrdhcpv6FOPeriodEndTime,
       "ciscoNetRegDhcpv6MIBConform": ciscoNetRegDhcpv6MIBConform,
       "ciscoNetRegDhcpv6MIBCompliances": ciscoNetRegDhcpv6MIBCompliances,
       "ciscoNetRegDhcpv6MIBCompliance": ciscoNetRegDhcpv6MIBCompliance,
       "ciscoNetRegDhcpv6MIBGroups": ciscoNetRegDhcpv6MIBGroups,
       "ciscoNetRegDhcpv6TotalCountersGroup": ciscoNetRegDhcpv6TotalCountersGroup,
       "ciscoNetRegDhcpv6NotificationsGroup": ciscoNetRegDhcpv6NotificationsGroup,
       "ciscoNetRegDhcpv6NotificationObjectsGroup": ciscoNetRegDhcpv6NotificationObjectsGroup,
       "ciscoNetRegDhcpv6PeriodCountersGroup": ciscoNetRegDhcpv6PeriodCountersGroup,
       "ciscoNetRegDhcpv6FailoverCountersGroup": ciscoNetRegDhcpv6FailoverCountersGroup,
       "ciscoNetRegDhcpv6FailoverPeriodCountersGroup": ciscoNetRegDhcpv6FailoverPeriodCountersGroup}
)
