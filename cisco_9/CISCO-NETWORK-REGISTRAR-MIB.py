# SNMP MIB module (CISCO-NETWORK-REGISTRAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-NETWORK-REGISTRAR-MIB.mib
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoNetworkRegistrarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120)
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarMIB.setRevisions(
        ("2023-01-22 00:00",
         "2017-04-03 00:00",
         "2016-09-23 00:00",
         "2014-06-13 00:00",
         "2013-05-24 00:00",
         "2010-05-24 00:00",
         "2005-03-03 00:00",
         "2003-01-11 00:00",
         "1999-06-17 00:00",
         "1998-11-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnrPhysAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 18),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoNetworkRegistrarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetworkRegistrarMIBObjects = _CiscoNetworkRegistrarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1)
)
_CnrDHCP_ObjectIdentity = ObjectIdentity
cnrDHCP = _CnrDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1)
)
_CnrDHCPScopeTable_Object = MibTable
cnrDHCPScopeTable = _CnrDHCPScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnrDHCPScopeTable.setStatus("deprecated")
_CnrDHCPScopeEntry_Object = MibTableRow
cnrDHCPScopeEntry = _CnrDHCPScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1)
)
cnrDHCPScopeEntry.setIndexNames(
    (0, "CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeName"),
)
if mibBuilder.loadTexts:
    cnrDHCPScopeEntry.setStatus("deprecated")


class _CnrDHCPScopeName_Type(DisplayString):
    """Custom type cnrDHCPScopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CnrDHCPScopeName_Type.__name__ = "DisplayString"
_CnrDHCPScopeName_Object = MibTableColumn
cnrDHCPScopeName = _CnrDHCPScopeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 1),
    _CnrDHCPScopeName_Type()
)
cnrDHCPScopeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnrDHCPScopeName.setStatus("deprecated")
_CnrDHCPScopeFreeAddrLowThreshold_Type = Unsigned32
_CnrDHCPScopeFreeAddrLowThreshold_Object = MibTableColumn
cnrDHCPScopeFreeAddrLowThreshold = _CnrDHCPScopeFreeAddrLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 2),
    _CnrDHCPScopeFreeAddrLowThreshold_Type()
)
cnrDHCPScopeFreeAddrLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrDHCPScopeFreeAddrLowThreshold.setStatus("deprecated")
_CnrDHCPScopeFreeAddrHighThreshold_Type = Unsigned32
_CnrDHCPScopeFreeAddrHighThreshold_Object = MibTableColumn
cnrDHCPScopeFreeAddrHighThreshold = _CnrDHCPScopeFreeAddrHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 3),
    _CnrDHCPScopeFreeAddrHighThreshold_Type()
)
cnrDHCPScopeFreeAddrHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrDHCPScopeFreeAddrHighThreshold.setStatus("deprecated")
_CnrDHCPScopeFreeAddrValue_Type = Unsigned32
_CnrDHCPScopeFreeAddrValue_Object = MibTableColumn
cnrDHCPScopeFreeAddrValue = _CnrDHCPScopeFreeAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 4),
    _CnrDHCPScopeFreeAddrValue_Type()
)
cnrDHCPScopeFreeAddrValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrDHCPScopeFreeAddrValue.setStatus("deprecated")


class _CnrDHCPScopeFreeAddrUnits_Type(Integer32):
    """Custom type cnrDHCPScopeFreeAddrUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("value", 1),
          ("percent", 2))
    )


_CnrDHCPScopeFreeAddrUnits_Type.__name__ = "Integer32"
_CnrDHCPScopeFreeAddrUnits_Object = MibTableColumn
cnrDHCPScopeFreeAddrUnits = _CnrDHCPScopeFreeAddrUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 1, 1, 1, 5),
    _CnrDHCPScopeFreeAddrUnits_Type()
)
cnrDHCPScopeFreeAddrUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrDHCPScopeFreeAddrUnits.setStatus("deprecated")
_CnrNotifObjects_ObjectIdentity = ObjectIdentity
cnrNotifObjects = _CnrNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2)
)
_CnrNotifDupIpAddress_Type = IpAddress
_CnrNotifDupIpAddress_Object = MibScalar
cnrNotifDupIpAddress = _CnrNotifDupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 1),
    _CnrNotifDupIpAddress_Type()
)
cnrNotifDupIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDupIpAddress.setStatus("current")
_CnrNotifMACAddress_Type = CnrPhysAddress
_CnrNotifMACAddress_Object = MibScalar
cnrNotifMACAddress = _CnrNotifMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 2),
    _CnrNotifMACAddress_Type()
)
cnrNotifMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifMACAddress.setStatus("current")
_CnrNotifServer_Type = IpAddress
_CnrNotifServer_Object = MibScalar
cnrNotifServer = _CnrNotifServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 3),
    _CnrNotifServer_Type()
)
cnrNotifServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifServer.setStatus("current")


class _CnrNotifServerType_Type(Integer32):
    """Custom type cnrNotifServerType based on Integer32"""
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
        *(("dns", 1),
          ("dhcp", 2),
          ("ldap", 3),
          ("tftp", 4),
          ("ccm", 5))
    )


_CnrNotifServerType_Type.__name__ = "Integer32"
_CnrNotifServerType_Object = MibScalar
cnrNotifServerType = _CnrNotifServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 4),
    _CnrNotifServerType_Type()
)
cnrNotifServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifServerType.setStatus("current")


class _CnrNotifDupIpAddressDetectedBy_Type(Integer32):
    """Custom type cnrNotifDupIpAddressDetectedBy based on Integer32"""
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


_CnrNotifDupIpAddressDetectedBy_Type.__name__ = "Integer32"
_CnrNotifDupIpAddressDetectedBy_Object = MibScalar
cnrNotifDupIpAddressDetectedBy = _CnrNotifDupIpAddressDetectedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 5),
    _CnrNotifDupIpAddressDetectedBy_Type()
)
cnrNotifDupIpAddressDetectedBy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDupIpAddressDetectedBy.setStatus("current")
_CnrNotifContestedIpAddress_Type = IpAddress
_CnrNotifContestedIpAddress_Object = MibScalar
cnrNotifContestedIpAddress = _CnrNotifContestedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 6),
    _CnrNotifContestedIpAddress_Type()
)
cnrNotifContestedIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifContestedIpAddress.setStatus("current")
_CnrNotifDHCPScopeFreeAddrLow_Type = Unsigned32
_CnrNotifDHCPScopeFreeAddrLow_Object = MibScalar
cnrNotifDHCPScopeFreeAddrLow = _CnrNotifDHCPScopeFreeAddrLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 7),
    _CnrNotifDHCPScopeFreeAddrLow_Type()
)
cnrNotifDHCPScopeFreeAddrLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeFreeAddrLow.setStatus("current")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeFreeAddrLow.setUnits("percentage")
_CnrNotifDHCPScopeFreeAddrHigh_Type = Unsigned32
_CnrNotifDHCPScopeFreeAddrHigh_Object = MibScalar
cnrNotifDHCPScopeFreeAddrHigh = _CnrNotifDHCPScopeFreeAddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 8),
    _CnrNotifDHCPScopeFreeAddrHigh_Type()
)
cnrNotifDHCPScopeFreeAddrHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeFreeAddrHigh.setStatus("current")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeFreeAddrHigh.setUnits("percentage")
_CnrNotifDHCPScopeFreeAddrValue_Type = Gauge32
_CnrNotifDHCPScopeFreeAddrValue_Object = MibScalar
cnrNotifDHCPScopeFreeAddrValue = _CnrNotifDHCPScopeFreeAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 9),
    _CnrNotifDHCPScopeFreeAddrValue_Type()
)
cnrNotifDHCPScopeFreeAddrValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeFreeAddrValue.setStatus("current")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeFreeAddrValue.setUnits("IP addresses")


class _CnrNotifDHCPThresholdType_Type(Integer32):
    """Custom type cnrNotifDHCPThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scope", 1),
          ("network", 2),
          ("selectionTags", 3))
    )


_CnrNotifDHCPThresholdType_Type.__name__ = "Integer32"
_CnrNotifDHCPThresholdType_Object = MibScalar
cnrNotifDHCPThresholdType = _CnrNotifDHCPThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 10),
    _CnrNotifDHCPThresholdType_Type()
)
cnrNotifDHCPThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDHCPThresholdType.setStatus("current")


class _CnrNotifDHCPThresholdValue_Type(DisplayString):
    """Custom type cnrNotifDHCPThresholdValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CnrNotifDHCPThresholdValue_Type.__name__ = "DisplayString"
_CnrNotifDHCPThresholdValue_Object = MibScalar
cnrNotifDHCPThresholdValue = _CnrNotifDHCPThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 11),
    _CnrNotifDHCPThresholdValue_Type()
)
cnrNotifDHCPThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDHCPThresholdValue.setStatus("current")


class _CnrNotifDHCPScopeName_Type(DisplayString):
    """Custom type cnrNotifDHCPScopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CnrNotifDHCPScopeName_Type.__name__ = "DisplayString"
_CnrNotifDHCPScopeName_Object = MibScalar
cnrNotifDHCPScopeName = _CnrNotifDHCPScopeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 12),
    _CnrNotifDHCPScopeName_Type()
)
cnrNotifDHCPScopeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDHCPScopeName.setStatus("current")
_CnrNotifPrimarySubnetNumber_Type = DisplayString
_CnrNotifPrimarySubnetNumber_Object = MibScalar
cnrNotifPrimarySubnetNumber = _CnrNotifPrimarySubnetNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 13),
    _CnrNotifPrimarySubnetNumber_Type()
)
cnrNotifPrimarySubnetNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifPrimarySubnetNumber.setStatus("current")


class _CnrNotifRelatedServerType_Type(Integer32):
    """Custom type cnrNotifRelatedServerType based on Integer32"""
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
        *(("dnsPrimary", 1),
          ("ldap", 2),
          ("failoverPartner", 3),
          ("relay-agent", 4))
    )


_CnrNotifRelatedServerType_Type.__name__ = "Integer32"
_CnrNotifRelatedServerType_Object = MibScalar
cnrNotifRelatedServerType = _CnrNotifRelatedServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 14),
    _CnrNotifRelatedServerType_Type()
)
cnrNotifRelatedServerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifRelatedServerType.setStatus("current")
_CnrNotifDnsServerIpAddress_Type = IpAddress
_CnrNotifDnsServerIpAddress_Object = MibScalar
cnrNotifDnsServerIpAddress = _CnrNotifDnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 15),
    _CnrNotifDnsServerIpAddress_Type()
)
cnrNotifDnsServerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDnsServerIpAddress.setStatus("current")
_CnrNotifZoneName_Type = DisplayString
_CnrNotifZoneName_Object = MibScalar
cnrNotifZoneName = _CnrNotifZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 16),
    _CnrNotifZoneName_Type()
)
cnrNotifZoneName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifZoneName.setStatus("current")


class _CnrNotifDnsRemoteServersList_Type(DisplayString):
    """Custom type cnrNotifDnsRemoteServersList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CnrNotifDnsRemoteServersList_Type.__name__ = "DisplayString"
_CnrNotifDnsRemoteServersList_Object = MibScalar
cnrNotifDnsRemoteServersList = _CnrNotifDnsRemoteServersList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 17),
    _CnrNotifDnsRemoteServersList_Type()
)
cnrNotifDnsRemoteServersList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDnsRemoteServersList.setStatus("current")
_CnrNotifIPv6Server_Type = InetAddressIPv6
_CnrNotifIPv6Server_Object = MibScalar
cnrNotifIPv6Server = _CnrNotifIPv6Server_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 18),
    _CnrNotifIPv6Server_Type()
)
cnrNotifIPv6Server.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifIPv6Server.setStatus("current")


class _CnrNotifFailoverPairName_Type(SnmpAdminString):
    """Custom type cnrNotifFailoverPairName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnrNotifFailoverPairName_Type.__name__ = "SnmpAdminString"
_CnrNotifFailoverPairName_Object = MibScalar
cnrNotifFailoverPairName = _CnrNotifFailoverPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 19),
    _CnrNotifFailoverPairName_Type()
)
cnrNotifFailoverPairName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifFailoverPairName.setStatus("current")


class _CnrNotifFailoverCfgErrType_Type(Integer32):
    """Custom type cnrNotifFailoverCfgErrType based on Integer32"""
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
        *(("mclt-error", 1),
          ("hba-error", 2),
          ("backup-percentage-error", 3),
          ("server-address-error", 4),
          ("config-error", 5),
          ("internal-error", 6),
          ("backup-load-balancing-config-error", 7),
          ("main-load-balancing-config-error", 8))
    )


_CnrNotifFailoverCfgErrType_Type.__name__ = "Integer32"
_CnrNotifFailoverCfgErrType_Object = MibScalar
cnrNotifFailoverCfgErrType = _CnrNotifFailoverCfgErrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 20),
    _CnrNotifFailoverCfgErrType_Type()
)
cnrNotifFailoverCfgErrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifFailoverCfgErrType.setStatus("current")
_CnrNotifDnsServerIp6Address_Type = InetAddressIPv6
_CnrNotifDnsServerIp6Address_Object = MibScalar
cnrNotifDnsServerIp6Address = _CnrNotifDnsServerIp6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 21),
    _CnrNotifDnsServerIp6Address_Type()
)
cnrNotifDnsServerIp6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifDnsServerIp6Address.setStatus("current")
_CnrNotifMainIPAddress_Type = IpAddress
_CnrNotifMainIPAddress_Object = MibScalar
cnrNotifMainIPAddress = _CnrNotifMainIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 22),
    _CnrNotifMainIPAddress_Type()
)
cnrNotifMainIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifMainIPAddress.setStatus("current")
_CnrNotifMainIPv6Address_Type = InetAddressIPv6
_CnrNotifMainIPv6Address_Object = MibScalar
cnrNotifMainIPv6Address = _CnrNotifMainIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 23),
    _CnrNotifMainIPv6Address_Type()
)
cnrNotifMainIPv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifMainIPv6Address.setStatus("current")
_CnrNotifBackupIPAddress_Type = IpAddress
_CnrNotifBackupIPAddress_Object = MibScalar
cnrNotifBackupIPAddress = _CnrNotifBackupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 24),
    _CnrNotifBackupIPAddress_Type()
)
cnrNotifBackupIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifBackupIPAddress.setStatus("current")
_CnrNotifBackupIPv6Address_Type = InetAddressIPv6
_CnrNotifBackupIPv6Address_Object = MibScalar
cnrNotifBackupIPv6Address = _CnrNotifBackupIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 25),
    _CnrNotifBackupIPv6Address_Type()
)
cnrNotifBackupIPv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifBackupIPv6Address.setStatus("current")


class _CnrNotifSyncDirection_Type(Integer32):
    """Custom type cnrNotifSyncDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main-to-backup", 1),
          ("backup-to-main", 2))
    )


_CnrNotifSyncDirection_Type.__name__ = "Integer32"
_CnrNotifSyncDirection_Object = MibScalar
cnrNotifSyncDirection = _CnrNotifSyncDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 26),
    _CnrNotifSyncDirection_Type()
)
cnrNotifSyncDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifSyncDirection.setStatus("current")


class _CnrNotifSyncError_Type(SnmpAdminString):
    """Custom type cnrNotifSyncError based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnrNotifSyncError_Type.__name__ = "SnmpAdminString"
_CnrNotifSyncError_Object = MibScalar
cnrNotifSyncError = _CnrNotifSyncError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 2, 27),
    _CnrNotifSyncError_Type()
)
cnrNotifSyncError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnrNotifSyncError.setStatus("current")
_CnrNotifCfgObjects_ObjectIdentity = ObjectIdentity
cnrNotifCfgObjects = _CnrNotifCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3)
)


class _CnrEnableFreeAddressLow_Type(TruthValue):
    """Custom type cnrEnableFreeAddressLow based on TruthValue"""
    defaultValue = 2


_CnrEnableFreeAddressLow_Type.__name__ = "TruthValue"
_CnrEnableFreeAddressLow_Object = MibScalar
cnrEnableFreeAddressLow = _CnrEnableFreeAddressLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 1),
    _CnrEnableFreeAddressLow_Type()
)
cnrEnableFreeAddressLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableFreeAddressLow.setStatus("deprecated")


class _CnrEnableFreeAddressHigh_Type(TruthValue):
    """Custom type cnrEnableFreeAddressHigh based on TruthValue"""
    defaultValue = 2


_CnrEnableFreeAddressHigh_Type.__name__ = "TruthValue"
_CnrEnableFreeAddressHigh_Object = MibScalar
cnrEnableFreeAddressHigh = _CnrEnableFreeAddressHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 2),
    _CnrEnableFreeAddressHigh_Type()
)
cnrEnableFreeAddressHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableFreeAddressHigh.setStatus("deprecated")


class _CnrEnableServerStart_Type(TruthValue):
    """Custom type cnrEnableServerStart based on TruthValue"""
    defaultValue = 2


_CnrEnableServerStart_Type.__name__ = "TruthValue"
_CnrEnableServerStart_Object = MibScalar
cnrEnableServerStart = _CnrEnableServerStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 3),
    _CnrEnableServerStart_Type()
)
cnrEnableServerStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableServerStart.setStatus("current")


class _CnrEnableServerStop_Type(TruthValue):
    """Custom type cnrEnableServerStop based on TruthValue"""
    defaultValue = 2


_CnrEnableServerStop_Type.__name__ = "TruthValue"
_CnrEnableServerStop_Object = MibScalar
cnrEnableServerStop = _CnrEnableServerStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 4),
    _CnrEnableServerStop_Type()
)
cnrEnableServerStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableServerStop.setStatus("current")


class _CnrEnableDNSQueueTooBig_Type(TruthValue):
    """Custom type cnrEnableDNSQueueTooBig based on TruthValue"""
    defaultValue = 2


_CnrEnableDNSQueueTooBig_Type.__name__ = "TruthValue"
_CnrEnableDNSQueueTooBig_Object = MibScalar
cnrEnableDNSQueueTooBig = _CnrEnableDNSQueueTooBig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 5),
    _CnrEnableDNSQueueTooBig_Type()
)
cnrEnableDNSQueueTooBig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableDNSQueueTooBig.setStatus("current")


class _CnrEnableOtherServerNotResponding_Type(TruthValue):
    """Custom type cnrEnableOtherServerNotResponding based on TruthValue"""
    defaultValue = 2


_CnrEnableOtherServerNotResponding_Type.__name__ = "TruthValue"
_CnrEnableOtherServerNotResponding_Object = MibScalar
cnrEnableOtherServerNotResponding = _CnrEnableOtherServerNotResponding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 6),
    _CnrEnableOtherServerNotResponding_Type()
)
cnrEnableOtherServerNotResponding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableOtherServerNotResponding.setStatus("deprecated")


class _CnrEnableDuplicateAddress_Type(TruthValue):
    """Custom type cnrEnableDuplicateAddress based on TruthValue"""
    defaultValue = 2


_CnrEnableDuplicateAddress_Type.__name__ = "TruthValue"
_CnrEnableDuplicateAddress_Object = MibScalar
cnrEnableDuplicateAddress = _CnrEnableDuplicateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 7),
    _CnrEnableDuplicateAddress_Type()
)
cnrEnableDuplicateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableDuplicateAddress.setStatus("current")


class _CnrEnableAddressConflict_Type(TruthValue):
    """Custom type cnrEnableAddressConflict based on TruthValue"""
    defaultValue = 2


_CnrEnableAddressConflict_Type.__name__ = "TruthValue"
_CnrEnableAddressConflict_Object = MibScalar
cnrEnableAddressConflict = _CnrEnableAddressConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 8),
    _CnrEnableAddressConflict_Type()
)
cnrEnableAddressConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableAddressConflict.setStatus("current")


class _CnrEnableOtherServerResponding_Type(TruthValue):
    """Custom type cnrEnableOtherServerResponding based on TruthValue"""
    defaultValue = 2


_CnrEnableOtherServerResponding_Type.__name__ = "TruthValue"
_CnrEnableOtherServerResponding_Object = MibScalar
cnrEnableOtherServerResponding = _CnrEnableOtherServerResponding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 9),
    _CnrEnableOtherServerResponding_Type()
)
cnrEnableOtherServerResponding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableOtherServerResponding.setStatus("deprecated")


class _CnrEnableFailoverConfigMismatch_Type(TruthValue):
    """Custom type cnrEnableFailoverConfigMismatch based on TruthValue"""
    defaultValue = 2


_CnrEnableFailoverConfigMismatch_Type.__name__ = "TruthValue"
_CnrEnableFailoverConfigMismatch_Object = MibScalar
cnrEnableFailoverConfigMismatch = _CnrEnableFailoverConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 10),
    _CnrEnableFailoverConfigMismatch_Type()
)
cnrEnableFailoverConfigMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableFailoverConfigMismatch.setStatus("current")


class _CnrEnableFreeAddrLow_Type(TruthValue):
    """Custom type cnrEnableFreeAddrLow based on TruthValue"""
    defaultValue = 2


_CnrEnableFreeAddrLow_Type.__name__ = "TruthValue"
_CnrEnableFreeAddrLow_Object = MibScalar
cnrEnableFreeAddrLow = _CnrEnableFreeAddrLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 11),
    _CnrEnableFreeAddrLow_Type()
)
cnrEnableFreeAddrLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableFreeAddrLow.setStatus("current")


class _CnrEnableFreeAddrHigh_Type(TruthValue):
    """Custom type cnrEnableFreeAddrHigh based on TruthValue"""
    defaultValue = 2


_CnrEnableFreeAddrHigh_Type.__name__ = "TruthValue"
_CnrEnableFreeAddrHigh_Object = MibScalar
cnrEnableFreeAddrHigh = _CnrEnableFreeAddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 12),
    _CnrEnableFreeAddrHigh_Type()
)
cnrEnableFreeAddrHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableFreeAddrHigh.setStatus("current")


class _CnrEnableOtherServerNotResp_Type(TruthValue):
    """Custom type cnrEnableOtherServerNotResp based on TruthValue"""
    defaultValue = 2


_CnrEnableOtherServerNotResp_Type.__name__ = "TruthValue"
_CnrEnableOtherServerNotResp_Object = MibScalar
cnrEnableOtherServerNotResp = _CnrEnableOtherServerNotResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 13),
    _CnrEnableOtherServerNotResp_Type()
)
cnrEnableOtherServerNotResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableOtherServerNotResp.setStatus("current")


class _CnrEnableOtherServerResp_Type(TruthValue):
    """Custom type cnrEnableOtherServerResp based on TruthValue"""
    defaultValue = 2


_CnrEnableOtherServerResp_Type.__name__ = "TruthValue"
_CnrEnableOtherServerResp_Object = MibScalar
cnrEnableOtherServerResp = _CnrEnableOtherServerResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 14),
    _CnrEnableOtherServerResp_Type()
)
cnrEnableOtherServerResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableOtherServerResp.setStatus("current")


class _CnrEnableHaDnsPartnerDown_Type(TruthValue):
    """Custom type cnrEnableHaDnsPartnerDown based on TruthValue"""
    defaultValue = 2


_CnrEnableHaDnsPartnerDown_Type.__name__ = "TruthValue"
_CnrEnableHaDnsPartnerDown_Object = MibScalar
cnrEnableHaDnsPartnerDown = _CnrEnableHaDnsPartnerDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 15),
    _CnrEnableHaDnsPartnerDown_Type()
)
cnrEnableHaDnsPartnerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableHaDnsPartnerDown.setStatus("current")


class _CnrEnableHaDnsPartnerUp_Type(TruthValue):
    """Custom type cnrEnableHaDnsPartnerUp based on TruthValue"""
    defaultValue = 2


_CnrEnableHaDnsPartnerUp_Type.__name__ = "TruthValue"
_CnrEnableHaDnsPartnerUp_Object = MibScalar
cnrEnableHaDnsPartnerUp = _CnrEnableHaDnsPartnerUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 16),
    _CnrEnableHaDnsPartnerUp_Type()
)
cnrEnableHaDnsPartnerUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableHaDnsPartnerUp.setStatus("current")


class _CnrEnableMastersNotResp_Type(TruthValue):
    """Custom type cnrEnableMastersNotResp based on TruthValue"""
    defaultValue = 2


_CnrEnableMastersNotResp_Type.__name__ = "TruthValue"
_CnrEnableMastersNotResp_Object = MibScalar
cnrEnableMastersNotResp = _CnrEnableMastersNotResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 17),
    _CnrEnableMastersNotResp_Type()
)
cnrEnableMastersNotResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableMastersNotResp.setStatus("current")


class _CnrEnableMastersResp_Type(TruthValue):
    """Custom type cnrEnableMastersResp based on TruthValue"""
    defaultValue = 2


_CnrEnableMastersResp_Type.__name__ = "TruthValue"
_CnrEnableMastersResp_Object = MibScalar
cnrEnableMastersResp = _CnrEnableMastersResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 18),
    _CnrEnableMastersResp_Type()
)
cnrEnableMastersResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableMastersResp.setStatus("current")


class _CnrEnableSecondaryZoneExpired_Type(TruthValue):
    """Custom type cnrEnableSecondaryZoneExpired based on TruthValue"""
    defaultValue = 2


_CnrEnableSecondaryZoneExpired_Type.__name__ = "TruthValue"
_CnrEnableSecondaryZoneExpired_Object = MibScalar
cnrEnableSecondaryZoneExpired = _CnrEnableSecondaryZoneExpired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 19),
    _CnrEnableSecondaryZoneExpired_Type()
)
cnrEnableSecondaryZoneExpired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableSecondaryZoneExpired.setStatus("current")


class _CnrEnableDnsForwardersNotResp_Type(TruthValue):
    """Custom type cnrEnableDnsForwardersNotResp based on TruthValue"""
    defaultValue = 2


_CnrEnableDnsForwardersNotResp_Type.__name__ = "TruthValue"
_CnrEnableDnsForwardersNotResp_Object = MibScalar
cnrEnableDnsForwardersNotResp = _CnrEnableDnsForwardersNotResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 20),
    _CnrEnableDnsForwardersNotResp_Type()
)
cnrEnableDnsForwardersNotResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableDnsForwardersNotResp.setStatus("current")


class _CnrEnableDnsForwardersResp_Type(TruthValue):
    """Custom type cnrEnableDnsForwardersResp based on TruthValue"""
    defaultValue = 2


_CnrEnableDnsForwardersResp_Type.__name__ = "TruthValue"
_CnrEnableDnsForwardersResp_Object = MibScalar
cnrEnableDnsForwardersResp = _CnrEnableDnsForwardersResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 21),
    _CnrEnableDnsForwardersResp_Type()
)
cnrEnableDnsForwardersResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableDnsForwardersResp.setStatus("current")


class _CnrEnableHaDnsConfigErr_Type(TruthValue):
    """Custom type cnrEnableHaDnsConfigErr based on TruthValue"""
    defaultValue = 2


_CnrEnableHaDnsConfigErr_Type.__name__ = "TruthValue"
_CnrEnableHaDnsConfigErr_Object = MibScalar
cnrEnableHaDnsConfigErr = _CnrEnableHaDnsConfigErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 22),
    _CnrEnableHaDnsConfigErr_Type()
)
cnrEnableHaDnsConfigErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableHaDnsConfigErr.setStatus("current")


class _CnrEnableFailoverSyncFailure_Type(TruthValue):
    """Custom type cnrEnableFailoverSyncFailure based on TruthValue"""
    defaultValue = 2


_CnrEnableFailoverSyncFailure_Type.__name__ = "TruthValue"
_CnrEnableFailoverSyncFailure_Object = MibScalar
cnrEnableFailoverSyncFailure = _CnrEnableFailoverSyncFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 1, 3, 23),
    _CnrEnableFailoverSyncFailure_Type()
)
cnrEnableFailoverSyncFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnrEnableFailoverSyncFailure.setStatus("current")
_CiscoNetRegMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoNetRegMIBNotificationPrefix = _CiscoNetRegMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2)
)
_CiscoNetRegMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoNetRegMIBNotifications = _CiscoNetRegMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0)
)
_CiscoNetworkRegistrarMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNetworkRegistrarMIBConformance = _CiscoNetworkRegistrarMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3)
)
_CiscoNetworkRegistrarMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNetworkRegistrarMIBCompliances = _CiscoNetworkRegistrarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 1)
)
_CiscoNetworkRegistrarMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNetworkRegistrarMIBGroups = _CiscoNetworkRegistrarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2)
)

# Managed Objects groups

ciscoNetworkRegistrarDHCPScopeObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 1)
)
ciscoNetworkRegistrarDHCPScopeObjectsGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrLowThreshold"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrHighThreshold"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrUnits"))
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarDHCPScopeObjectsGroup.setStatus("deprecated")

ciscoNetworkRegistrarNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 2)
)
ciscoNetworkRegistrarNotifObjectsGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDupIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMACAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDupIpAddressDetectedBy"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServerType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifContestedIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarNotifObjectsGroup.setStatus("deprecated")

ciscoNetworkRegistrarNotifCfgObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 3)
)
ciscoNetworkRegistrarNotifCfgObjectsGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFreeAddressLow"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFreeAddressHigh"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableServerStart"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableServerStop"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableDNSQueueTooBig"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableOtherServerNotResponding"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableDuplicateAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableAddressConflict"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableOtherServerResponding"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFailoverConfigMismatch"))
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarNotifCfgObjectsGroup.setStatus("deprecated")

ciscoNetRegistrarNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 5)
)
ciscoNetRegistrarNotifInfoGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDupIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMACAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServerType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDupIpAddressDetectedBy"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifContestedIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrLow"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrHigh"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPThresholdType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPThresholdValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifPrimarySubnetNumber"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifRelatedServerType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifZoneName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsRemoteServersList"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifFailoverPairName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifFailoverCfgErrType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIp6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMainIPAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMainIPv6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifBackupIPAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifBackupIPv6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifSyncDirection"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifSyncError"))
)
if mibBuilder.loadTexts:
    ciscoNetRegistrarNotifInfoGroup.setStatus("current")

ciscoNetRegistrarNotEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 6)
)
ciscoNetRegistrarNotEnableGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableServerStart"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableServerStop"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableDNSQueueTooBig"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableDuplicateAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableAddressConflict"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFailoverConfigMismatch"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFreeAddrLow"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFreeAddrHigh"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableOtherServerNotResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableOtherServerResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableHaDnsPartnerDown"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableHaDnsPartnerUp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableMastersNotResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableMastersResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableSecondaryZoneExpired"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableDnsForwardersNotResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableDnsForwardersResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableHaDnsConfigErr"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrEnableFailoverSyncFailure"))
)
if mibBuilder.loadTexts:
    ciscoNetRegistrarNotEnableGroup.setStatus("current")


# Notification objects

ciscoNetRegFreeAddressLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 1)
)
ciscoNetRegFreeAddressLow.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrLowThreshold"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrUnits"))
)
if mibBuilder.loadTexts:
    ciscoNetRegFreeAddressLow.setStatus(
        "deprecated"
    )

ciscoNetRegFreeAddressHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 2)
)
ciscoNetRegFreeAddressHigh.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrHighThreshold"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrDHCPScopeFreeAddrUnits"))
)
if mibBuilder.loadTexts:
    ciscoNetRegFreeAddressHigh.setStatus(
        "deprecated"
    )

ciscoNetRegServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 3)
)
ciscoNetRegServerStart.setObjects(
    ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServerType")
)
if mibBuilder.loadTexts:
    ciscoNetRegServerStart.setStatus(
        "current"
    )

ciscoNetRegServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 4)
)
ciscoNetRegServerStop.setObjects(
    ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServerType")
)
if mibBuilder.loadTexts:
    ciscoNetRegServerStop.setStatus(
        "current"
    )

ciscoNetRegDNSQueueTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 5)
)
if mibBuilder.loadTexts:
    ciscoNetRegDNSQueueTooBig.setStatus(
        "current"
    )

ciscoNetRegOtherServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 6)
)
ciscoNetRegOtherServerNotResponding.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServerType"))
)
if mibBuilder.loadTexts:
    ciscoNetRegOtherServerNotResponding.setStatus(
        "deprecated"
    )

ciscoNetRegDuplicateAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 7)
)
ciscoNetRegDuplicateAddress.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDupIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMACAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDupIpAddressDetectedBy"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDuplicateAddress.setStatus(
        "current"
    )

ciscoNetRegAddressConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 8)
)
ciscoNetRegAddressConflict.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifContestedIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifFailoverPairName"))
)
if mibBuilder.loadTexts:
    ciscoNetRegAddressConflict.setStatus(
        "current"
    )

ciscoNetRegOtherServerResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 9)
)
ciscoNetRegOtherServerResponding.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServerType"))
)
if mibBuilder.loadTexts:
    ciscoNetRegOtherServerResponding.setStatus(
        "deprecated"
    )

ciscoNetRegFailoverConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 10)
)
ciscoNetRegFailoverConfigMismatch.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifFailoverPairName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifFailoverCfgErrType"))
)
if mibBuilder.loadTexts:
    ciscoNetRegFailoverConfigMismatch.setStatus(
        "current"
    )

ciscoNetRegFreeAddrLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 11)
)
ciscoNetRegFreeAddrLowThreshold.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrLow"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifPrimarySubnetNumber"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPThresholdType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPThresholdValue"))
)
if mibBuilder.loadTexts:
    ciscoNetRegFreeAddrLowThreshold.setStatus(
        "current"
    )

ciscoNetRegFreeAddrHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 12)
)
ciscoNetRegFreeAddrHighThreshold.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrHigh"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeFreeAddrValue"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPScopeName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifPrimarySubnetNumber"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPThresholdType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDHCPThresholdValue"))
)
if mibBuilder.loadTexts:
    ciscoNetRegFreeAddrHighThreshold.setStatus(
        "current"
    )

ciscoNetRegOtherServerNotResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 13)
)
ciscoNetRegOtherServerNotResp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifRelatedServerType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"))
)
if mibBuilder.loadTexts:
    ciscoNetRegOtherServerNotResp.setStatus(
        "current"
    )

ciscoNetRegOtherServerResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 14)
)
ciscoNetRegOtherServerResp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifRelatedServerType"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"))
)
if mibBuilder.loadTexts:
    ciscoNetRegOtherServerResp.setStatus(
        "current"
    )

ciscoNetRegHaDnsPartnerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 15)
)
ciscoNetRegHaDnsPartnerDown.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"))
)
if mibBuilder.loadTexts:
    ciscoNetRegHaDnsPartnerDown.setStatus(
        "current"
    )

ciscoNetRegHaDnsPartnerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 16)
)
ciscoNetRegHaDnsPartnerUp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"))
)
if mibBuilder.loadTexts:
    ciscoNetRegHaDnsPartnerUp.setStatus(
        "current"
    )

ciscoNetRegMastersNotResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 17)
)
ciscoNetRegMastersNotResp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIp6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifZoneName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsRemoteServersList"))
)
if mibBuilder.loadTexts:
    ciscoNetRegMastersNotResp.setStatus(
        "current"
    )

ciscoNetRegMastersResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 18)
)
ciscoNetRegMastersResp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIp6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifZoneName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsRemoteServersList"))
)
if mibBuilder.loadTexts:
    ciscoNetRegMastersResp.setStatus(
        "current"
    )

ciscoNetRegSecondaryZonesExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 19)
)
ciscoNetRegSecondaryZonesExpired.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIp6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifZoneName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsRemoteServersList"))
)
if mibBuilder.loadTexts:
    ciscoNetRegSecondaryZonesExpired.setStatus(
        "current"
    )

ciscoNetRegDnsForwardersNotResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 20)
)
ciscoNetRegDnsForwardersNotResp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsRemoteServersList"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDnsForwardersNotResp.setStatus(
        "deprecated"
    )

ciscoNetRegDnsForwardersResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 21)
)
ciscoNetRegDnsForwardersResp.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsServerIpAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifDnsRemoteServersList"))
)
if mibBuilder.loadTexts:
    ciscoNetRegDnsForwardersResp.setStatus(
        "deprecated"
    )

ciscoNetRegHaDnsConfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 22)
)
ciscoNetRegHaDnsConfigErr.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifServer"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifZoneName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifIPv6Server"))
)
if mibBuilder.loadTexts:
    ciscoNetRegHaDnsConfigErr.setStatus(
        "current"
    )

ciscoNetRegFailoverSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 2, 0, 23)
)
ciscoNetRegFailoverSyncFailure.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifFailoverPairName"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMainIPAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifMainIPv6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifBackupIPAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifBackupIPv6Address"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifSyncDirection"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "cnrNotifSyncError"))
)
if mibBuilder.loadTexts:
    ciscoNetRegFailoverSyncFailure.setStatus(
        "current"
    )


# Notifications groups

ciscoNetworkRegistrarNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 4)
)
ciscoNetworkRegistrarNotificationsGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFreeAddressLow"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFreeAddressHigh"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegServerStart"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegServerStop"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegDNSQueueTooBig"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegOtherServerNotResponding"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegDuplicateAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegAddressConflict"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegOtherServerResponding"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFailoverConfigMismatch"))
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarNotificationsGroup.setStatus(
        "deprecated"
    )

ciscoNetRegistrarNotificatGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 2, 7)
)
ciscoNetRegistrarNotificatGroup.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegServerStart"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegServerStop"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegDNSQueueTooBig"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFreeAddrLowThreshold"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFreeAddrHighThreshold"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegAddressConflict"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegDuplicateAddress"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegOtherServerNotResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegOtherServerResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFailoverConfigMismatch"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegHaDnsPartnerDown"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegHaDnsPartnerUp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegMastersNotResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegMastersResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegSecondaryZonesExpired"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegDnsForwardersNotResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegDnsForwardersResp"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegHaDnsConfigErr"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegFailoverSyncFailure"))
)
if mibBuilder.loadTexts:
    ciscoNetRegistrarNotificatGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoNetworkRegistrarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 1, 1)
)
ciscoNetworkRegistrarMIBCompliance.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetworkRegistrarDHCPScopeObjectsGroup"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetworkRegistrarNotifObjectsGroup"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetworkRegistrarNotifCfgObjectsGroup"))
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarMIBCompliance.setStatus(
        "deprecated"
    )

ciscoNetworkRegistrarMIBCompRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 120, 3, 1, 2)
)
ciscoNetworkRegistrarMIBCompRev1.setObjects(
      *(("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegistrarNotifInfoGroup"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegistrarNotEnableGroup"),
        ("CISCO-NETWORK-REGISTRAR-MIB", "ciscoNetRegistrarNotificatGroup"))
)
if mibBuilder.loadTexts:
    ciscoNetworkRegistrarMIBCompRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETWORK-REGISTRAR-MIB",
    **{"CnrPhysAddress": CnrPhysAddress,
       "ciscoNetworkRegistrarMIB": ciscoNetworkRegistrarMIB,
       "ciscoNetworkRegistrarMIBObjects": ciscoNetworkRegistrarMIBObjects,
       "cnrDHCP": cnrDHCP,
       "cnrDHCPScopeTable": cnrDHCPScopeTable,
       "cnrDHCPScopeEntry": cnrDHCPScopeEntry,
       "cnrDHCPScopeName": cnrDHCPScopeName,
       "cnrDHCPScopeFreeAddrLowThreshold": cnrDHCPScopeFreeAddrLowThreshold,
       "cnrDHCPScopeFreeAddrHighThreshold": cnrDHCPScopeFreeAddrHighThreshold,
       "cnrDHCPScopeFreeAddrValue": cnrDHCPScopeFreeAddrValue,
       "cnrDHCPScopeFreeAddrUnits": cnrDHCPScopeFreeAddrUnits,
       "cnrNotifObjects": cnrNotifObjects,
       "cnrNotifDupIpAddress": cnrNotifDupIpAddress,
       "cnrNotifMACAddress": cnrNotifMACAddress,
       "cnrNotifServer": cnrNotifServer,
       "cnrNotifServerType": cnrNotifServerType,
       "cnrNotifDupIpAddressDetectedBy": cnrNotifDupIpAddressDetectedBy,
       "cnrNotifContestedIpAddress": cnrNotifContestedIpAddress,
       "cnrNotifDHCPScopeFreeAddrLow": cnrNotifDHCPScopeFreeAddrLow,
       "cnrNotifDHCPScopeFreeAddrHigh": cnrNotifDHCPScopeFreeAddrHigh,
       "cnrNotifDHCPScopeFreeAddrValue": cnrNotifDHCPScopeFreeAddrValue,
       "cnrNotifDHCPThresholdType": cnrNotifDHCPThresholdType,
       "cnrNotifDHCPThresholdValue": cnrNotifDHCPThresholdValue,
       "cnrNotifDHCPScopeName": cnrNotifDHCPScopeName,
       "cnrNotifPrimarySubnetNumber": cnrNotifPrimarySubnetNumber,
       "cnrNotifRelatedServerType": cnrNotifRelatedServerType,
       "cnrNotifDnsServerIpAddress": cnrNotifDnsServerIpAddress,
       "cnrNotifZoneName": cnrNotifZoneName,
       "cnrNotifDnsRemoteServersList": cnrNotifDnsRemoteServersList,
       "cnrNotifIPv6Server": cnrNotifIPv6Server,
       "cnrNotifFailoverPairName": cnrNotifFailoverPairName,
       "cnrNotifFailoverCfgErrType": cnrNotifFailoverCfgErrType,
       "cnrNotifDnsServerIp6Address": cnrNotifDnsServerIp6Address,
       "cnrNotifMainIPAddress": cnrNotifMainIPAddress,
       "cnrNotifMainIPv6Address": cnrNotifMainIPv6Address,
       "cnrNotifBackupIPAddress": cnrNotifBackupIPAddress,
       "cnrNotifBackupIPv6Address": cnrNotifBackupIPv6Address,
       "cnrNotifSyncDirection": cnrNotifSyncDirection,
       "cnrNotifSyncError": cnrNotifSyncError,
       "cnrNotifCfgObjects": cnrNotifCfgObjects,
       "cnrEnableFreeAddressLow": cnrEnableFreeAddressLow,
       "cnrEnableFreeAddressHigh": cnrEnableFreeAddressHigh,
       "cnrEnableServerStart": cnrEnableServerStart,
       "cnrEnableServerStop": cnrEnableServerStop,
       "cnrEnableDNSQueueTooBig": cnrEnableDNSQueueTooBig,
       "cnrEnableOtherServerNotResponding": cnrEnableOtherServerNotResponding,
       "cnrEnableDuplicateAddress": cnrEnableDuplicateAddress,
       "cnrEnableAddressConflict": cnrEnableAddressConflict,
       "cnrEnableOtherServerResponding": cnrEnableOtherServerResponding,
       "cnrEnableFailoverConfigMismatch": cnrEnableFailoverConfigMismatch,
       "cnrEnableFreeAddrLow": cnrEnableFreeAddrLow,
       "cnrEnableFreeAddrHigh": cnrEnableFreeAddrHigh,
       "cnrEnableOtherServerNotResp": cnrEnableOtherServerNotResp,
       "cnrEnableOtherServerResp": cnrEnableOtherServerResp,
       "cnrEnableHaDnsPartnerDown": cnrEnableHaDnsPartnerDown,
       "cnrEnableHaDnsPartnerUp": cnrEnableHaDnsPartnerUp,
       "cnrEnableMastersNotResp": cnrEnableMastersNotResp,
       "cnrEnableMastersResp": cnrEnableMastersResp,
       "cnrEnableSecondaryZoneExpired": cnrEnableSecondaryZoneExpired,
       "cnrEnableDnsForwardersNotResp": cnrEnableDnsForwardersNotResp,
       "cnrEnableDnsForwardersResp": cnrEnableDnsForwardersResp,
       "cnrEnableHaDnsConfigErr": cnrEnableHaDnsConfigErr,
       "cnrEnableFailoverSyncFailure": cnrEnableFailoverSyncFailure,
       "ciscoNetRegMIBNotificationPrefix": ciscoNetRegMIBNotificationPrefix,
       "ciscoNetRegMIBNotifications": ciscoNetRegMIBNotifications,
       "ciscoNetRegFreeAddressLow": ciscoNetRegFreeAddressLow,
       "ciscoNetRegFreeAddressHigh": ciscoNetRegFreeAddressHigh,
       "ciscoNetRegServerStart": ciscoNetRegServerStart,
       "ciscoNetRegServerStop": ciscoNetRegServerStop,
       "ciscoNetRegDNSQueueTooBig": ciscoNetRegDNSQueueTooBig,
       "ciscoNetRegOtherServerNotResponding": ciscoNetRegOtherServerNotResponding,
       "ciscoNetRegDuplicateAddress": ciscoNetRegDuplicateAddress,
       "ciscoNetRegAddressConflict": ciscoNetRegAddressConflict,
       "ciscoNetRegOtherServerResponding": ciscoNetRegOtherServerResponding,
       "ciscoNetRegFailoverConfigMismatch": ciscoNetRegFailoverConfigMismatch,
       "ciscoNetRegFreeAddrLowThreshold": ciscoNetRegFreeAddrLowThreshold,
       "ciscoNetRegFreeAddrHighThreshold": ciscoNetRegFreeAddrHighThreshold,
       "ciscoNetRegOtherServerNotResp": ciscoNetRegOtherServerNotResp,
       "ciscoNetRegOtherServerResp": ciscoNetRegOtherServerResp,
       "ciscoNetRegHaDnsPartnerDown": ciscoNetRegHaDnsPartnerDown,
       "ciscoNetRegHaDnsPartnerUp": ciscoNetRegHaDnsPartnerUp,
       "ciscoNetRegMastersNotResp": ciscoNetRegMastersNotResp,
       "ciscoNetRegMastersResp": ciscoNetRegMastersResp,
       "ciscoNetRegSecondaryZonesExpired": ciscoNetRegSecondaryZonesExpired,
       "ciscoNetRegDnsForwardersNotResp": ciscoNetRegDnsForwardersNotResp,
       "ciscoNetRegDnsForwardersResp": ciscoNetRegDnsForwardersResp,
       "ciscoNetRegHaDnsConfigErr": ciscoNetRegHaDnsConfigErr,
       "ciscoNetRegFailoverSyncFailure": ciscoNetRegFailoverSyncFailure,
       "ciscoNetworkRegistrarMIBConformance": ciscoNetworkRegistrarMIBConformance,
       "ciscoNetworkRegistrarMIBCompliances": ciscoNetworkRegistrarMIBCompliances,
       "ciscoNetworkRegistrarMIBCompliance": ciscoNetworkRegistrarMIBCompliance,
       "ciscoNetworkRegistrarMIBCompRev1": ciscoNetworkRegistrarMIBCompRev1,
       "ciscoNetworkRegistrarMIBGroups": ciscoNetworkRegistrarMIBGroups,
       "ciscoNetworkRegistrarDHCPScopeObjectsGroup": ciscoNetworkRegistrarDHCPScopeObjectsGroup,
       "ciscoNetworkRegistrarNotifObjectsGroup": ciscoNetworkRegistrarNotifObjectsGroup,
       "ciscoNetworkRegistrarNotifCfgObjectsGroup": ciscoNetworkRegistrarNotifCfgObjectsGroup,
       "ciscoNetworkRegistrarNotificationsGroup": ciscoNetworkRegistrarNotificationsGroup,
       "ciscoNetRegistrarNotifInfoGroup": ciscoNetRegistrarNotifInfoGroup,
       "ciscoNetRegistrarNotEnableGroup": ciscoNetRegistrarNotEnableGroup,
       "ciscoNetRegistrarNotificatGroup": ciscoNetRegistrarNotificatGroup}
)
