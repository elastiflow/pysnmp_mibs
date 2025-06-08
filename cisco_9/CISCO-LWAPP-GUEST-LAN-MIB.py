# SNMP MIB module (CISCO-LWAPP-GUEST-LAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-GUEST-LAN-MIB.mib
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

ciscoLwappGuestLanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868)
)
if mibBuilder.loadTexts:
    ciscoLwappGuestLanMIB.setRevisions(
        ("2018-10-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappGuestLanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappGuestLanMIBNotifs = _CiscoLwappGuestLanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 0)
)
_CiscoLwappGuestLanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappGuestLanMIBObjects = _CiscoLwappGuestLanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1)
)
_CiscoLwappGuestLanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappGuestLanConfig = _CiscoLwappGuestLanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1)
)
_CLGuestLanTable_Object = MibTable
cLGuestLanTable = _CLGuestLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLGuestLanTable.setStatus("current")
_CLGuestLanEntry_Object = MibTableRow
cLGuestLanEntry = _CLGuestLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1)
)
cLGuestLanEntry.setIndexNames(
    (0, "CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanIndex"),
)
if mibBuilder.loadTexts:
    cLGuestLanEntry.setStatus("current")


class _CLGuestLanIndex_Type(Unsigned32):
    """Custom type cLGuestLanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CLGuestLanIndex_Type.__name__ = "Unsigned32"
_CLGuestLanIndex_Object = MibTableColumn
cLGuestLanIndex = _CLGuestLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 1),
    _CLGuestLanIndex_Type()
)
cLGuestLanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLGuestLanIndex.setStatus("current")
_CLGuestLanRowStatus_Type = RowStatus
_CLGuestLanRowStatus_Object = MibTableColumn
cLGuestLanRowStatus = _CLGuestLanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 2),
    _CLGuestLanRowStatus_Type()
)
cLGuestLanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanRowStatus.setStatus("current")


class _CLGuestLanProfileName_Type(SnmpAdminString):
    """Custom type cLGuestLanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLGuestLanProfileName_Type.__name__ = "SnmpAdminString"
_CLGuestLanProfileName_Object = MibTableColumn
cLGuestLanProfileName = _CLGuestLanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 3),
    _CLGuestLanProfileName_Type()
)
cLGuestLanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanProfileName.setStatus("current")


class _CLGuestLanHasWiredVlan_Type(Integer32):
    """Custom type cLGuestLanHasWiredVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("withoutWiredVlan", 1),
          ("withWiredVlan", 2))
    )


_CLGuestLanHasWiredVlan_Type.__name__ = "Integer32"
_CLGuestLanHasWiredVlan_Object = MibTableColumn
cLGuestLanHasWiredVlan = _CLGuestLanHasWiredVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 4),
    _CLGuestLanHasWiredVlan_Type()
)
cLGuestLanHasWiredVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanHasWiredVlan.setStatus("current")


class _CLGuestLanWiredVlan_Type(Unsigned32):
    """Custom type cLGuestLanWiredVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CLGuestLanWiredVlan_Type.__name__ = "Unsigned32"
_CLGuestLanWiredVlan_Object = MibTableColumn
cLGuestLanWiredVlan = _CLGuestLanWiredVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 5),
    _CLGuestLanWiredVlan_Type()
)
cLGuestLanWiredVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanWiredVlan.setStatus("current")


class _CLGuestLanAuthenticationList_Type(SnmpAdminString):
    """Custom type cLGuestLanAuthenticationList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLGuestLanAuthenticationList_Type.__name__ = "SnmpAdminString"
_CLGuestLanAuthenticationList_Object = MibTableColumn
cLGuestLanAuthenticationList = _CLGuestLanAuthenticationList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 6),
    _CLGuestLanAuthenticationList_Type()
)
cLGuestLanAuthenticationList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanAuthenticationList.setStatus("current")


class _CLGuestLanAuthorizationList_Type(SnmpAdminString):
    """Custom type cLGuestLanAuthorizationList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLGuestLanAuthorizationList_Type.__name__ = "SnmpAdminString"
_CLGuestLanAuthorizationList_Object = MibTableColumn
cLGuestLanAuthorizationList = _CLGuestLanAuthorizationList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 7),
    _CLGuestLanAuthorizationList_Type()
)
cLGuestLanAuthorizationList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanAuthorizationList.setStatus("current")
_CLGuestLanSecurityWebAuth_Type = TruthValue
_CLGuestLanSecurityWebAuth_Object = MibTableColumn
cLGuestLanSecurityWebAuth = _CLGuestLanSecurityWebAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 8),
    _CLGuestLanSecurityWebAuth_Type()
)
cLGuestLanSecurityWebAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanSecurityWebAuth.setStatus("current")


class _CLGuestLanWebAuthParameter_Type(SnmpAdminString):
    """Custom type cLGuestLanWebAuthParameter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLGuestLanWebAuthParameter_Type.__name__ = "SnmpAdminString"
_CLGuestLanWebAuthParameter_Object = MibTableColumn
cLGuestLanWebAuthParameter = _CLGuestLanWebAuthParameter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 9),
    _CLGuestLanWebAuthParameter_Type()
)
cLGuestLanWebAuthParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanWebAuthParameter.setStatus("current")


class _CLGuestLanClientLimit_Type(Unsigned32):
    """Custom type cLGuestLanClientLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CLGuestLanClientLimit_Type.__name__ = "Unsigned32"
_CLGuestLanClientLimit_Object = MibTableColumn
cLGuestLanClientLimit = _CLGuestLanClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 10),
    _CLGuestLanClientLimit_Type()
)
cLGuestLanClientLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanClientLimit.setStatus("current")
_CLGuestLanStatus_Type = TruthValue
_CLGuestLanStatus_Object = MibTableColumn
cLGuestLanStatus = _CLGuestLanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 11),
    _CLGuestLanStatus_Type()
)
cLGuestLanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanStatus.setStatus("current")


class _CLGuestLanMdnsMode_Type(Integer32):
    """Custom type cLGuestLanMdnsMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 0),
          ("drop", 1),
          ("gateway", 2))
    )


_CLGuestLanMdnsMode_Type.__name__ = "Integer32"
_CLGuestLanMdnsMode_Object = MibTableColumn
cLGuestLanMdnsMode = _CLGuestLanMdnsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 1, 1, 12),
    _CLGuestLanMdnsMode_Type()
)
cLGuestLanMdnsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanMdnsMode.setStatus("current")
_CLGuestLanProfileToPolicyTable_Object = MibTable
cLGuestLanProfileToPolicyTable = _CLGuestLanProfileToPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLGuestLanProfileToPolicyTable.setStatus("current")
_CLGuestLanProfileToPolicyEntry_Object = MibTableRow
cLGuestLanProfileToPolicyEntry = _CLGuestLanProfileToPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 2, 1)
)
cLGuestLanProfileToPolicyEntry.setIndexNames(
    (0, "CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMapName"),
    (0, "CISCO-LWAPP-GUEST-LAN-MIB", "clGuestLanMapGuestLanProfileName"),
)
if mibBuilder.loadTexts:
    cLGuestLanProfileToPolicyEntry.setStatus("current")


class _CLGuestLanMapName_Type(SnmpAdminString):
    """Custom type cLGuestLanMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLGuestLanMapName_Type.__name__ = "SnmpAdminString"
_CLGuestLanMapName_Object = MibTableColumn
cLGuestLanMapName = _CLGuestLanMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 2, 1, 1),
    _CLGuestLanMapName_Type()
)
cLGuestLanMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLGuestLanMapName.setStatus("current")


class _ClGuestLanMapGuestLanProfileName_Type(SnmpAdminString):
    """Custom type clGuestLanMapGuestLanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClGuestLanMapGuestLanProfileName_Type.__name__ = "SnmpAdminString"
_ClGuestLanMapGuestLanProfileName_Object = MibTableColumn
clGuestLanMapGuestLanProfileName = _ClGuestLanMapGuestLanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 2, 1, 2),
    _ClGuestLanMapGuestLanProfileName_Type()
)
clGuestLanMapGuestLanProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGuestLanMapGuestLanProfileName.setStatus("current")
_CLGuestLanMapProfileToPolicyRowStatus_Type = RowStatus
_CLGuestLanMapProfileToPolicyRowStatus_Object = MibTableColumn
cLGuestLanMapProfileToPolicyRowStatus = _CLGuestLanMapProfileToPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 2, 1, 3),
    _CLGuestLanMapProfileToPolicyRowStatus_Type()
)
cLGuestLanMapProfileToPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanMapProfileToPolicyRowStatus.setStatus("current")


class _ClGuestLanMapPolicyProfileName_Type(SnmpAdminString):
    """Custom type clGuestLanMapPolicyProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClGuestLanMapPolicyProfileName_Type.__name__ = "SnmpAdminString"
_ClGuestLanMapPolicyProfileName_Object = MibTableColumn
clGuestLanMapPolicyProfileName = _ClGuestLanMapPolicyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 2, 1, 4),
    _ClGuestLanMapPolicyProfileName_Type()
)
clGuestLanMapPolicyProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGuestLanMapPolicyProfileName.setStatus("current")
_CLGuestLanGuestLanMapTable_Object = MibTable
cLGuestLanGuestLanMapTable = _CLGuestLanGuestLanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLGuestLanGuestLanMapTable.setStatus("current")
_CLGuestLanGuestLanMapEntry_Object = MibTableRow
cLGuestLanGuestLanMapEntry = _CLGuestLanGuestLanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 3, 1)
)
cLGuestLanGuestLanMapEntry.setIndexNames(
    (0, "CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanGuestLanMapName"),
)
if mibBuilder.loadTexts:
    cLGuestLanGuestLanMapEntry.setStatus("current")


class _CLGuestLanGuestLanMapName_Type(SnmpAdminString):
    """Custom type cLGuestLanGuestLanMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLGuestLanGuestLanMapName_Type.__name__ = "SnmpAdminString"
_CLGuestLanGuestLanMapName_Object = MibTableColumn
cLGuestLanGuestLanMapName = _CLGuestLanGuestLanMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 3, 1, 1),
    _CLGuestLanGuestLanMapName_Type()
)
cLGuestLanGuestLanMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLGuestLanGuestLanMapName.setStatus("current")
_CLGuestLanGuestLanMapRowStatus_Type = RowStatus
_CLGuestLanGuestLanMapRowStatus_Object = MibTableColumn
cLGuestLanGuestLanMapRowStatus = _CLGuestLanGuestLanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 3, 1, 2),
    _CLGuestLanGuestLanMapRowStatus_Type()
)
cLGuestLanGuestLanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGuestLanGuestLanMapRowStatus.setStatus("current")
_CLGuestLanMobileStationTable_Object = MibTable
cLGuestLanMobileStationTable = _CLGuestLanMobileStationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cLGuestLanMobileStationTable.setStatus("current")
_CLGuestLanMobileStationEntry_Object = MibTableRow
cLGuestLanMobileStationEntry = _CLGuestLanMobileStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1)
)
cLGuestLanMobileStationEntry.setIndexNames(
    (0, "CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationMacAddress"),
)
if mibBuilder.loadTexts:
    cLGuestLanMobileStationEntry.setStatus("current")
_CLGuestLanMobileStationMacAddress_Type = MacAddress
_CLGuestLanMobileStationMacAddress_Object = MibTableColumn
cLGuestLanMobileStationMacAddress = _CLGuestLanMobileStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 1),
    _CLGuestLanMobileStationMacAddress_Type()
)
cLGuestLanMobileStationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationMacAddress.setStatus("current")
_CLGuestLanMobileStationIpAddressType_Type = InetAddressType
_CLGuestLanMobileStationIpAddressType_Object = MibTableColumn
cLGuestLanMobileStationIpAddressType = _CLGuestLanMobileStationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 2),
    _CLGuestLanMobileStationIpAddressType_Type()
)
cLGuestLanMobileStationIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationIpAddressType.setStatus("current")
_CLGuestLanMobileStationIpAddress_Type = InetAddress
_CLGuestLanMobileStationIpAddress_Object = MibTableColumn
cLGuestLanMobileStationIpAddress = _CLGuestLanMobileStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 3),
    _CLGuestLanMobileStationIpAddress_Type()
)
cLGuestLanMobileStationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationIpAddress.setStatus("current")
_CLGuestLanMobileStationUserName_Type = SnmpAdminString
_CLGuestLanMobileStationUserName_Object = MibTableColumn
cLGuestLanMobileStationUserName = _CLGuestLanMobileStationUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 4),
    _CLGuestLanMobileStationUserName_Type()
)
cLGuestLanMobileStationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationUserName.setStatus("current")
_ClGuestLanMobileStationProfileName_Type = SnmpAdminString
_ClGuestLanMobileStationProfileName_Object = MibTableColumn
clGuestLanMobileStationProfileName = _ClGuestLanMobileStationProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 5),
    _ClGuestLanMobileStationProfileName_Type()
)
clGuestLanMobileStationProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGuestLanMobileStationProfileName.setStatus("current")
_CLGuestLanMobileStationAID_Type = Unsigned32
_CLGuestLanMobileStationAID_Object = MibTableColumn
cLGuestLanMobileStationAID = _CLGuestLanMobileStationAID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 6),
    _CLGuestLanMobileStationAID_Type()
)
cLGuestLanMobileStationAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationAID.setStatus("current")


class _CLGuestLanMobileStationStatus_Type(Integer32):
    """Custom type cLGuestLanMobileStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("idle", 0),
          ("aaaPending", 1),
          ("authenticated", 2),
          ("associated", 3),
          ("powersave", 4),
          ("disassociated", 5),
          ("tobedeleted", 6),
          ("probing", 7),
          ("blacklisted", 8))
    )


_CLGuestLanMobileStationStatus_Type.__name__ = "Integer32"
_CLGuestLanMobileStationStatus_Object = MibTableColumn
cLGuestLanMobileStationStatus = _CLGuestLanMobileStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 7),
    _CLGuestLanMobileStationStatus_Type()
)
cLGuestLanMobileStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationStatus.setStatus("current")


class _CLGuestLanMobileStationReasonCode_Type(Integer32):
    """Custom type cLGuestLanMobileStationReasonCode based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              99,
              101,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("previousAuthNotValid", 2),
          ("deauthenticationLeaving", 3),
          ("disassociationDueToInactivity", 4),
          ("disassociationAPBusy", 5),
          ("class2FrameFromNonAuthStation", 6),
          ("class2FrameFromNonAssStation", 7),
          ("disassociationStaHasLeft", 8),
          ("staReqAssociationWithoutAuth", 9),
          ("invalidInformationElement", 40),
          ("groupCipherInvalid", 41),
          ("unicastCipherInvalid", 42),
          ("akmpInvalid", 43),
          ("unsupportedRsnVersion", 44),
          ("invalidRsnIeCapabilities", 45),
          ("cipherSuiteRejected", 46),
          ("missingReasonCode", 99),
          ("maxAssociatedClientsReached", 101),
          ("unSpecifieQosFailure", 200),
          ("qosPolicyMismatch", 201),
          ("inSufficientBandwidth", 202),
          ("inValidQosParams", 203))
    )


_CLGuestLanMobileStationReasonCode_Type.__name__ = "Integer32"
_CLGuestLanMobileStationReasonCode_Object = MibTableColumn
cLGuestLanMobileStationReasonCode = _CLGuestLanMobileStationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 8),
    _CLGuestLanMobileStationReasonCode_Type()
)
cLGuestLanMobileStationReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationReasonCode.setStatus("current")


class _CLGuestLanMobileStationMobilityStatus_Type(Integer32):
    """Custom type cLGuestLanMobileStationMobilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unassociated", 0),
          ("local", 1),
          ("anchor", 2),
          ("foreign", 3),
          ("handoff", 4),
          ("unknown", 5),
          ("exportanchor", 6),
          ("exportforeign", 7))
    )


_CLGuestLanMobileStationMobilityStatus_Type.__name__ = "Integer32"
_CLGuestLanMobileStationMobilityStatus_Object = MibTableColumn
cLGuestLanMobileStationMobilityStatus = _CLGuestLanMobileStationMobilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 9),
    _CLGuestLanMobileStationMobilityStatus_Type()
)
cLGuestLanMobileStationMobilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationMobilityStatus.setStatus("current")
_CLGuestLanMobileStationAnchorAddressType_Type = InetAddressType
_CLGuestLanMobileStationAnchorAddressType_Object = MibTableColumn
cLGuestLanMobileStationAnchorAddressType = _CLGuestLanMobileStationAnchorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 10),
    _CLGuestLanMobileStationAnchorAddressType_Type()
)
cLGuestLanMobileStationAnchorAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationAnchorAddressType.setStatus("current")
_CLGuestLanMobileStationAnchorAddress_Type = InetAddress
_CLGuestLanMobileStationAnchorAddress_Object = MibTableColumn
cLGuestLanMobileStationAnchorAddress = _CLGuestLanMobileStationAnchorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 11),
    _CLGuestLanMobileStationAnchorAddress_Type()
)
cLGuestLanMobileStationAnchorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationAnchorAddress.setStatus("current")
_CLGuestLanMobileStationSessionTimeout_Type = Unsigned32
_CLGuestLanMobileStationSessionTimeout_Object = MibTableColumn
cLGuestLanMobileStationSessionTimeout = _CLGuestLanMobileStationSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 12),
    _CLGuestLanMobileStationSessionTimeout_Type()
)
cLGuestLanMobileStationSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationSessionTimeout.setStatus("current")


class _CLGuestLanMobileStationAuthenticationAlgorithm_Type(Integer32):
    """Custom type cLGuestLanMobileStationAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 0),
          ("sharedKey", 1),
          ("unknown", 2),
          ("openAndEap", 128))
    )


_CLGuestLanMobileStationAuthenticationAlgorithm_Type.__name__ = "Integer32"
_CLGuestLanMobileStationAuthenticationAlgorithm_Object = MibTableColumn
cLGuestLanMobileStationAuthenticationAlgorithm = _CLGuestLanMobileStationAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 13),
    _CLGuestLanMobileStationAuthenticationAlgorithm_Type()
)
cLGuestLanMobileStationAuthenticationAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationAuthenticationAlgorithm.setStatus("current")


class _CLGuestLanMobileStationDeleteAction_Type(Integer32):
    """Custom type cLGuestLanMobileStationDeleteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("delete", 1))
    )


_CLGuestLanMobileStationDeleteAction_Type.__name__ = "Integer32"
_CLGuestLanMobileStationDeleteAction_Object = MibTableColumn
cLGuestLanMobileStationDeleteAction = _CLGuestLanMobileStationDeleteAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 14),
    _CLGuestLanMobileStationDeleteAction_Type()
)
cLGuestLanMobileStationDeleteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationDeleteAction.setStatus("current")
_CLGuestLanMobileStationPolicyManagerState_Type = SnmpAdminString
_CLGuestLanMobileStationPolicyManagerState_Object = MibTableColumn
cLGuestLanMobileStationPolicyManagerState = _CLGuestLanMobileStationPolicyManagerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 15),
    _CLGuestLanMobileStationPolicyManagerState_Type()
)
cLGuestLanMobileStationPolicyManagerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationPolicyManagerState.setStatus("current")


class _CLGuestLanMobileStationSecurityPolicyStatus_Type(Integer32):
    """Custom type cLGuestLanMobileStationSecurityPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("completed", 0),
          ("notcompleted", 1))
    )


_CLGuestLanMobileStationSecurityPolicyStatus_Type.__name__ = "Integer32"
_CLGuestLanMobileStationSecurityPolicyStatus_Object = MibTableColumn
cLGuestLanMobileStationSecurityPolicyStatus = _CLGuestLanMobileStationSecurityPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 16),
    _CLGuestLanMobileStationSecurityPolicyStatus_Type()
)
cLGuestLanMobileStationSecurityPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationSecurityPolicyStatus.setStatus("current")


class _CLGuestLanMobileStationInterface_Type(SnmpAdminString):
    """Custom type cLGuestLanMobileStationInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLGuestLanMobileStationInterface_Type.__name__ = "SnmpAdminString"
_CLGuestLanMobileStationInterface_Object = MibTableColumn
cLGuestLanMobileStationInterface = _CLGuestLanMobileStationInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 17),
    _CLGuestLanMobileStationInterface_Type()
)
cLGuestLanMobileStationInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationInterface.setStatus("current")


class _CLGuestLanMobileStationVlanId_Type(Unsigned32):
    """Custom type cLGuestLanMobileStationVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CLGuestLanMobileStationVlanId_Type.__name__ = "Unsigned32"
_CLGuestLanMobileStationVlanId_Object = MibTableColumn
cLGuestLanMobileStationVlanId = _CLGuestLanMobileStationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 18),
    _CLGuestLanMobileStationVlanId_Type()
)
cLGuestLanMobileStationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationVlanId.setStatus("current")


class _CLGuestLanMobileStationPolicyType_Type(Integer32):
    """Custom type cLGuestLanMobileStationPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("wpa1", 1),
          ("wpa2", 2),
          ("wpa2vff", 3),
          ("notavailable", 4),
          ("unknown", 5))
    )


_CLGuestLanMobileStationPolicyType_Type.__name__ = "Integer32"
_CLGuestLanMobileStationPolicyType_Object = MibTableColumn
cLGuestLanMobileStationPolicyType = _CLGuestLanMobileStationPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 19),
    _CLGuestLanMobileStationPolicyType_Type()
)
cLGuestLanMobileStationPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationPolicyType.setStatus("current")


class _CLGuestLanMobileStationEncryptionCypher_Type(Integer32):
    """Custom type cLGuestLanMobileStationEncryptionCypher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("ccmpAes", 0),
          ("tkipMic", 1),
          ("wep40", 2),
          ("wep104", 3),
          ("wep128", 4),
          ("none", 5),
          ("tkipWep40", 6),
          ("tkipWep104", 7),
          ("gcmp128", 8),
          ("gcmp256", 9),
          ("ccmp256", 10),
          ("notavailable", 11),
          ("unknown", 12))
    )


_CLGuestLanMobileStationEncryptionCypher_Type.__name__ = "Integer32"
_CLGuestLanMobileStationEncryptionCypher_Object = MibTableColumn
cLGuestLanMobileStationEncryptionCypher = _CLGuestLanMobileStationEncryptionCypher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 20),
    _CLGuestLanMobileStationEncryptionCypher_Type()
)
cLGuestLanMobileStationEncryptionCypher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationEncryptionCypher.setStatus("current")


class _CLGuestLanMobileStationEapType_Type(Integer32):
    """Custom type cLGuestLanMobileStationEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eapTls", 0),
          ("ttls", 1),
          ("peap", 2),
          ("leap", 3),
          ("speke", 4),
          ("eapFast", 5),
          ("notavailable", 6),
          ("unknown", 7))
    )


_CLGuestLanMobileStationEapType_Type.__name__ = "Integer32"
_CLGuestLanMobileStationEapType_Object = MibTableColumn
cLGuestLanMobileStationEapType = _CLGuestLanMobileStationEapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 21),
    _CLGuestLanMobileStationEapType_Type()
)
cLGuestLanMobileStationEapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationEapType.setStatus("current")


class _CLGuestLanMobileStationStatusCode_Type(Unsigned32):
    """Custom type cLGuestLanMobileStationStatusCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLGuestLanMobileStationStatusCode_Type.__name__ = "Unsigned32"
_CLGuestLanMobileStationStatusCode_Object = MibTableColumn
cLGuestLanMobileStationStatusCode = _CLGuestLanMobileStationStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 22),
    _CLGuestLanMobileStationStatusCode_Type()
)
cLGuestLanMobileStationStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationStatusCode.setStatus("current")
_CLGuestLanMobileStationAAAOverridePassphrase_Type = TruthValue
_CLGuestLanMobileStationAAAOverridePassphrase_Object = MibTableColumn
cLGuestLanMobileStationAAAOverridePassphrase = _CLGuestLanMobileStationAAAOverridePassphrase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 1, 1, 4, 1, 23),
    _CLGuestLanMobileStationAAAOverridePassphrase_Type()
)
cLGuestLanMobileStationAAAOverridePassphrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLGuestLanMobileStationAAAOverridePassphrase.setStatus("current")
_CiscoLwappGuestLanConform_ObjectIdentity = ObjectIdentity
ciscoLwappGuestLanConform = _CiscoLwappGuestLanConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 2)
)
_CiscoLwappGuestLanCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappGuestLanCompliances = _CiscoLwappGuestLanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 2, 1)
)
_CiscoLwappGuestLanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappGuestLanMIBGroups = _CiscoLwappGuestLanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 2, 2)
)

# Managed Objects groups

ciscoLwappGuestLanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 2, 2, 1)
)
ciscoLwappGuestLanConfigGroup.setObjects(
      *(("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanRowStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanProfileName"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanHasWiredVlan"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanWiredVlan"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanAuthenticationList"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanAuthorizationList"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanSecurityWebAuth"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanWebAuthParameter"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanClientLimit"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanGuestLanMapRowStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMapProfileToPolicyRowStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "clGuestLanMapPolicyProfileName"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMdnsMode"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationIpAddressType"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationIpAddress"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationUserName"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "clGuestLanMobileStationProfileName"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationAID"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationReasonCode"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationMobilityStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationAnchorAddressType"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationAnchorAddress"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationSessionTimeout"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationAuthenticationAlgorithm"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationDeleteAction"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationPolicyManagerState"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationSecurityPolicyStatus"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationInterface"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationVlanId"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationPolicyType"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationEncryptionCypher"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationEapType"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationStatusCode"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanMobileStationAAAOverridePassphrase"))
)
if mibBuilder.loadTexts:
    ciscoLwappGuestLanConfigGroup.setStatus("current")


# Notification objects

cLGuestLanAllAnchorsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 0, 1)
)
cLGuestLanAllAnchorsDown.setObjects(
      *(("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanProfileName"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "clGuestLanMapPolicyProfileName"))
)
if mibBuilder.loadTexts:
    cLGuestLanAllAnchorsDown.setStatus(
        "current"
    )

cLGuestLanOneAnchorOnGuestLanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 0, 2)
)
cLGuestLanOneAnchorOnGuestLanUp.setObjects(
      *(("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanProfileName"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "clGuestLanMapPolicyProfileName"))
)
if mibBuilder.loadTexts:
    cLGuestLanOneAnchorOnGuestLanUp.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappGuestLanNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 2, 2, 2)
)
ciscoLwappGuestLanNotifsGroup.setObjects(
      *(("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanAllAnchorsDown"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "cLGuestLanOneAnchorOnGuestLanUp"))
)
if mibBuilder.loadTexts:
    ciscoLwappGuestLanNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappGuestLanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 868, 2, 1, 1)
)
ciscoLwappGuestLanCompliance.setObjects(
      *(("CISCO-LWAPP-GUEST-LAN-MIB", "ciscoLwappGuestLanConfigGroup"),
        ("CISCO-LWAPP-GUEST-LAN-MIB", "ciscoLwappGuestLanNotifsGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappGuestLanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-GUEST-LAN-MIB",
    **{"ciscoLwappGuestLanMIB": ciscoLwappGuestLanMIB,
       "ciscoLwappGuestLanMIBNotifs": ciscoLwappGuestLanMIBNotifs,
       "cLGuestLanAllAnchorsDown": cLGuestLanAllAnchorsDown,
       "cLGuestLanOneAnchorOnGuestLanUp": cLGuestLanOneAnchorOnGuestLanUp,
       "ciscoLwappGuestLanMIBObjects": ciscoLwappGuestLanMIBObjects,
       "ciscoLwappGuestLanConfig": ciscoLwappGuestLanConfig,
       "cLGuestLanTable": cLGuestLanTable,
       "cLGuestLanEntry": cLGuestLanEntry,
       "cLGuestLanIndex": cLGuestLanIndex,
       "cLGuestLanRowStatus": cLGuestLanRowStatus,
       "cLGuestLanProfileName": cLGuestLanProfileName,
       "cLGuestLanHasWiredVlan": cLGuestLanHasWiredVlan,
       "cLGuestLanWiredVlan": cLGuestLanWiredVlan,
       "cLGuestLanAuthenticationList": cLGuestLanAuthenticationList,
       "cLGuestLanAuthorizationList": cLGuestLanAuthorizationList,
       "cLGuestLanSecurityWebAuth": cLGuestLanSecurityWebAuth,
       "cLGuestLanWebAuthParameter": cLGuestLanWebAuthParameter,
       "cLGuestLanClientLimit": cLGuestLanClientLimit,
       "cLGuestLanStatus": cLGuestLanStatus,
       "cLGuestLanMdnsMode": cLGuestLanMdnsMode,
       "cLGuestLanProfileToPolicyTable": cLGuestLanProfileToPolicyTable,
       "cLGuestLanProfileToPolicyEntry": cLGuestLanProfileToPolicyEntry,
       "cLGuestLanMapName": cLGuestLanMapName,
       "clGuestLanMapGuestLanProfileName": clGuestLanMapGuestLanProfileName,
       "cLGuestLanMapProfileToPolicyRowStatus": cLGuestLanMapProfileToPolicyRowStatus,
       "clGuestLanMapPolicyProfileName": clGuestLanMapPolicyProfileName,
       "cLGuestLanGuestLanMapTable": cLGuestLanGuestLanMapTable,
       "cLGuestLanGuestLanMapEntry": cLGuestLanGuestLanMapEntry,
       "cLGuestLanGuestLanMapName": cLGuestLanGuestLanMapName,
       "cLGuestLanGuestLanMapRowStatus": cLGuestLanGuestLanMapRowStatus,
       "cLGuestLanMobileStationTable": cLGuestLanMobileStationTable,
       "cLGuestLanMobileStationEntry": cLGuestLanMobileStationEntry,
       "cLGuestLanMobileStationMacAddress": cLGuestLanMobileStationMacAddress,
       "cLGuestLanMobileStationIpAddressType": cLGuestLanMobileStationIpAddressType,
       "cLGuestLanMobileStationIpAddress": cLGuestLanMobileStationIpAddress,
       "cLGuestLanMobileStationUserName": cLGuestLanMobileStationUserName,
       "clGuestLanMobileStationProfileName": clGuestLanMobileStationProfileName,
       "cLGuestLanMobileStationAID": cLGuestLanMobileStationAID,
       "cLGuestLanMobileStationStatus": cLGuestLanMobileStationStatus,
       "cLGuestLanMobileStationReasonCode": cLGuestLanMobileStationReasonCode,
       "cLGuestLanMobileStationMobilityStatus": cLGuestLanMobileStationMobilityStatus,
       "cLGuestLanMobileStationAnchorAddressType": cLGuestLanMobileStationAnchorAddressType,
       "cLGuestLanMobileStationAnchorAddress": cLGuestLanMobileStationAnchorAddress,
       "cLGuestLanMobileStationSessionTimeout": cLGuestLanMobileStationSessionTimeout,
       "cLGuestLanMobileStationAuthenticationAlgorithm": cLGuestLanMobileStationAuthenticationAlgorithm,
       "cLGuestLanMobileStationDeleteAction": cLGuestLanMobileStationDeleteAction,
       "cLGuestLanMobileStationPolicyManagerState": cLGuestLanMobileStationPolicyManagerState,
       "cLGuestLanMobileStationSecurityPolicyStatus": cLGuestLanMobileStationSecurityPolicyStatus,
       "cLGuestLanMobileStationInterface": cLGuestLanMobileStationInterface,
       "cLGuestLanMobileStationVlanId": cLGuestLanMobileStationVlanId,
       "cLGuestLanMobileStationPolicyType": cLGuestLanMobileStationPolicyType,
       "cLGuestLanMobileStationEncryptionCypher": cLGuestLanMobileStationEncryptionCypher,
       "cLGuestLanMobileStationEapType": cLGuestLanMobileStationEapType,
       "cLGuestLanMobileStationStatusCode": cLGuestLanMobileStationStatusCode,
       "cLGuestLanMobileStationAAAOverridePassphrase": cLGuestLanMobileStationAAAOverridePassphrase,
       "ciscoLwappGuestLanConform": ciscoLwappGuestLanConform,
       "ciscoLwappGuestLanCompliances": ciscoLwappGuestLanCompliances,
       "ciscoLwappGuestLanCompliance": ciscoLwappGuestLanCompliance,
       "ciscoLwappGuestLanMIBGroups": ciscoLwappGuestLanMIBGroups,
       "ciscoLwappGuestLanConfigGroup": ciscoLwappGuestLanConfigGroup,
       "ciscoLwappGuestLanNotifsGroup": ciscoLwappGuestLanNotifsGroup}
)
