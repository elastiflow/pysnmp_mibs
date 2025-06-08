# SNMP MIB module (CISCO-LWAPP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-INTERFACE-MIB.mib
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686)
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIB.setRevisions(
        ("2017-04-27 00:00",
         "2010-08-22 00:00",
         "2009-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappInterfaceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBNotifs = _CiscoLwappInterfaceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 0)
)
_CiscoLwappInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBObjects = _CiscoLwappInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1)
)
_CiscoLwappInterfaceConfig_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceConfig = _CiscoLwappInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1)
)
_ClInterfaceConfigTable_Object = MibTable
clInterfaceConfigTable = _ClInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clInterfaceConfigTable.setStatus("current")
_ClInterfaceConfigEntry_Object = MibTableRow
clInterfaceConfigEntry = _ClInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1)
)
clInterfaceConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
)
if mibBuilder.loadTexts:
    clInterfaceConfigEntry.setStatus("current")


class _ClInterfaceName_Type(OctetString):
    """Custom type clInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClInterfaceName_Type.__name__ = "OctetString"
_ClInterfaceName_Object = MibTableColumn
clInterfaceName = _ClInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 1),
    _ClInterfaceName_Type()
)
clInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clInterfaceName.setStatus("current")


class _ClInterfaceWired_Type(TruthValue):
    """Custom type clInterfaceWired based on TruthValue"""
    defaultValue = 2


_ClInterfaceWired_Type.__name__ = "TruthValue"
_ClInterfaceWired_Object = MibTableColumn
clInterfaceWired = _ClInterfaceWired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 2),
    _ClInterfaceWired_Type()
)
clInterfaceWired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceWired.setStatus("current")


class _ClInterfaceQuarantineVlanId_Type(Unsigned32):
    """Custom type clInterfaceQuarantineVlanId based on Unsigned32"""
    defaultValue = 0


_ClInterfaceQuarantineVlanId_Type.__name__ = "Unsigned32"
_ClInterfaceQuarantineVlanId_Object = MibTableColumn
clInterfaceQuarantineVlanId = _ClInterfaceQuarantineVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 3),
    _ClInterfaceQuarantineVlanId_Type()
)
clInterfaceQuarantineVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceQuarantineVlanId.setStatus("current")


class _ClInterfaceDhcpOpt82Enabled_Type(TruthValue):
    """Custom type clInterfaceDhcpOpt82Enabled based on TruthValue"""
    defaultValue = 2


_ClInterfaceDhcpOpt82Enabled_Type.__name__ = "TruthValue"
_ClInterfaceDhcpOpt82Enabled_Object = MibTableColumn
clInterfaceDhcpOpt82Enabled = _ClInterfaceDhcpOpt82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 4),
    _ClInterfaceDhcpOpt82Enabled_Type()
)
clInterfaceDhcpOpt82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceDhcpOpt82Enabled.setStatus("current")


class _ClInterfaceDhcpProxyMode_Type(Integer32):
    """Custom type clInterfaceDhcpProxyMode based on Integer32"""
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
        *(("global", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_ClInterfaceDhcpProxyMode_Type.__name__ = "Integer32"
_ClInterfaceDhcpProxyMode_Object = MibTableColumn
clInterfaceDhcpProxyMode = _ClInterfaceDhcpProxyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 5),
    _ClInterfaceDhcpProxyMode_Type()
)
clInterfaceDhcpProxyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceDhcpProxyMode.setStatus("current")
_ClInterfaceMdnsProfileName_Type = SnmpAdminString
_ClInterfaceMdnsProfileName_Object = MibTableColumn
clInterfaceMdnsProfileName = _ClInterfaceMdnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 6),
    _ClInterfaceMdnsProfileName_Type()
)
clInterfaceMdnsProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceMdnsProfileName.setStatus("current")


class _ClInterfaceNasId_Type(SnmpAdminString):
    """Custom type clInterfaceNasId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ClInterfaceNasId_Type.__name__ = "SnmpAdminString"
_ClInterfaceNasId_Object = MibTableColumn
clInterfaceNasId = _ClInterfaceNasId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 7),
    _ClInterfaceNasId_Type()
)
clInterfaceNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceNasId.setStatus("current")


class _ClInterfaceMappingRedPort_Type(TruthValue):
    """Custom type clInterfaceMappingRedPort based on TruthValue"""
    defaultValue = 2


_ClInterfaceMappingRedPort_Type.__name__ = "TruthValue"
_ClInterfaceMappingRedPort_Object = MibTableColumn
clInterfaceMappingRedPort = _ClInterfaceMappingRedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 8),
    _ClInterfaceMappingRedPort_Type()
)
clInterfaceMappingRedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceMappingRedPort.setStatus("current")
_ClInterfacePrimaryIPv6AddrType_Type = InetAddressType
_ClInterfacePrimaryIPv6AddrType_Object = MibTableColumn
clInterfacePrimaryIPv6AddrType = _ClInterfacePrimaryIPv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 9),
    _ClInterfacePrimaryIPv6AddrType_Type()
)
clInterfacePrimaryIPv6AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfacePrimaryIPv6AddrType.setStatus("current")
_ClInterfacePrimaryIPv6Addr_Type = InetAddress
_ClInterfacePrimaryIPv6Addr_Object = MibTableColumn
clInterfacePrimaryIPv6Addr = _ClInterfacePrimaryIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 10),
    _ClInterfacePrimaryIPv6Addr_Type()
)
clInterfacePrimaryIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfacePrimaryIPv6Addr.setStatus("current")


class _ClInterfacePrimaryPrefixLen_Type(Unsigned32):
    """Custom type clInterfacePrimaryPrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ClInterfacePrimaryPrefixLen_Type.__name__ = "Unsigned32"
_ClInterfacePrimaryPrefixLen_Object = MibTableColumn
clInterfacePrimaryPrefixLen = _ClInterfacePrimaryPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 11),
    _ClInterfacePrimaryPrefixLen_Type()
)
clInterfacePrimaryPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfacePrimaryPrefixLen.setStatus("current")
_ClInterfacePrimaryIPv6GatewayType_Type = InetAddressType
_ClInterfacePrimaryIPv6GatewayType_Object = MibTableColumn
clInterfacePrimaryIPv6GatewayType = _ClInterfacePrimaryIPv6GatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 12),
    _ClInterfacePrimaryIPv6GatewayType_Type()
)
clInterfacePrimaryIPv6GatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfacePrimaryIPv6GatewayType.setStatus("current")
_ClInterfacePrimaryIPv6Gateway_Type = InetAddress
_ClInterfacePrimaryIPv6Gateway_Object = MibTableColumn
clInterfacePrimaryIPv6Gateway = _ClInterfacePrimaryIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 13),
    _ClInterfacePrimaryIPv6Gateway_Type()
)
clInterfacePrimaryIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfacePrimaryIPv6Gateway.setStatus("current")


class _ClInterfaceIPv6AclName_Type(SnmpAdminString):
    """Custom type clInterfaceIPv6AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClInterfaceIPv6AclName_Type.__name__ = "SnmpAdminString"
_ClInterfaceIPv6AclName_Object = MibTableColumn
clInterfaceIPv6AclName = _ClInterfaceIPv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 14),
    _ClInterfaceIPv6AclName_Type()
)
clInterfaceIPv6AclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceIPv6AclName.setStatus("current")
_ClInterfaceLinkLocalIDType_Type = InetAddressType
_ClInterfaceLinkLocalIDType_Object = MibTableColumn
clInterfaceLinkLocalIDType = _ClInterfaceLinkLocalIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 15),
    _ClInterfaceLinkLocalIDType_Type()
)
clInterfaceLinkLocalIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clInterfaceLinkLocalIDType.setStatus("current")
_ClInterfaceLinkLocalID_Type = InetAddress
_ClInterfaceLinkLocalID_Object = MibTableColumn
clInterfaceLinkLocalID = _ClInterfaceLinkLocalID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 16),
    _ClInterfaceLinkLocalID_Type()
)
clInterfaceLinkLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clInterfaceLinkLocalID.setStatus("current")


class _ClInterfaceIPv6SLAAC_Type(TruthValue):
    """Custom type clInterfaceIPv6SLAAC based on TruthValue"""
    defaultValue = 2


_ClInterfaceIPv6SLAAC_Type.__name__ = "TruthValue"
_ClInterfaceIPv6SLAAC_Object = MibTableColumn
clInterfaceIPv6SLAAC = _ClInterfaceIPv6SLAAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 17),
    _ClInterfaceIPv6SLAAC_Type()
)
clInterfaceIPv6SLAAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceIPv6SLAAC.setStatus("current")


class _ClInterfaceLinkSelectEnabled_Type(TruthValue):
    """Custom type clInterfaceLinkSelectEnabled based on TruthValue"""
    defaultValue = 2


_ClInterfaceLinkSelectEnabled_Type.__name__ = "TruthValue"
_ClInterfaceLinkSelectEnabled_Object = MibTableColumn
clInterfaceLinkSelectEnabled = _ClInterfaceLinkSelectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 18),
    _ClInterfaceLinkSelectEnabled_Type()
)
clInterfaceLinkSelectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceLinkSelectEnabled.setStatus("current")
_ClInterfaceLinkSelectRelaySrcIntf_Type = SnmpAdminString
_ClInterfaceLinkSelectRelaySrcIntf_Object = MibTableColumn
clInterfaceLinkSelectRelaySrcIntf = _ClInterfaceLinkSelectRelaySrcIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 19),
    _ClInterfaceLinkSelectRelaySrcIntf_Type()
)
clInterfaceLinkSelectRelaySrcIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceLinkSelectRelaySrcIntf.setStatus("current")


class _ClInterfaceVpnSelectEnabled_Type(TruthValue):
    """Custom type clInterfaceVpnSelectEnabled based on TruthValue"""
    defaultValue = 2


_ClInterfaceVpnSelectEnabled_Type.__name__ = "TruthValue"
_ClInterfaceVpnSelectEnabled_Object = MibTableColumn
clInterfaceVpnSelectEnabled = _ClInterfaceVpnSelectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 20),
    _ClInterfaceVpnSelectEnabled_Type()
)
clInterfaceVpnSelectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceVpnSelectEnabled.setStatus("current")
_ClInterfaceVpnSelectVpnId_Type = SnmpAdminString
_ClInterfaceVpnSelectVpnId_Object = MibTableColumn
clInterfaceVpnSelectVpnId = _ClInterfaceVpnSelectVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 21),
    _ClInterfaceVpnSelectVpnId_Type()
)
clInterfaceVpnSelectVpnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceVpnSelectVpnId.setStatus("current")
_ClInterfaceVpnselectVrfName_Type = SnmpAdminString
_ClInterfaceVpnselectVrfName_Object = MibTableColumn
clInterfaceVpnselectVrfName = _ClInterfaceVpnselectVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 22),
    _ClInterfaceVpnselectVrfName_Type()
)
clInterfaceVpnselectVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceVpnselectVrfName.setStatus("current")


class _ClInterfacePrimaryIpv6AddrStatus_Type(Integer32):
    """Custom type clInterfacePrimaryIpv6AddrStatus based on Integer32"""
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
        *(("none", 1),
          ("creating", 2),
          ("tentative", 3),
          ("incomplete", 4),
          ("verify", 5),
          ("reachable", 6),
          ("stale", 7),
          ("down", 8),
          ("unknown", 9),
          ("dad", 10))
    )


_ClInterfacePrimaryIpv6AddrStatus_Type.__name__ = "Integer32"
_ClInterfacePrimaryIpv6AddrStatus_Object = MibTableColumn
clInterfacePrimaryIpv6AddrStatus = _ClInterfacePrimaryIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 23),
    _ClInterfacePrimaryIpv6AddrStatus_Type()
)
clInterfacePrimaryIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clInterfacePrimaryIpv6AddrStatus.setStatus("current")


class _ClInterfaceLinkLocalIpv6AddrStatus_Type(Integer32):
    """Custom type clInterfaceLinkLocalIpv6AddrStatus based on Integer32"""
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
        *(("none", 1),
          ("creating", 2),
          ("tentative", 3),
          ("incomplete", 4),
          ("verify", 5),
          ("reachable", 6),
          ("stale", 7),
          ("down", 8),
          ("unknown", 9),
          ("dad", 10))
    )


_ClInterfaceLinkLocalIpv6AddrStatus_Type.__name__ = "Integer32"
_ClInterfaceLinkLocalIpv6AddrStatus_Object = MibTableColumn
clInterfaceLinkLocalIpv6AddrStatus = _ClInterfaceLinkLocalIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 24),
    _ClInterfaceLinkLocalIpv6AddrStatus_Type()
)
clInterfaceLinkLocalIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clInterfaceLinkLocalIpv6AddrStatus.setStatus("current")
_ClInterfaceGroupsConfigTable_Object = MibTable
clInterfaceGroupsConfigTable = _ClInterfaceGroupsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clInterfaceGroupsConfigTable.setStatus("current")
_ClInterfaceGroupsConfigEntry_Object = MibTableRow
clInterfaceGroupsConfigEntry = _ClInterfaceGroupsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1)
)
clInterfaceGroupsConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupName"),
)
if mibBuilder.loadTexts:
    clInterfaceGroupsConfigEntry.setStatus("current")
_ClInterfaceGroupName_Type = SnmpAdminString
_ClInterfaceGroupName_Object = MibTableColumn
clInterfaceGroupName = _ClInterfaceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 1),
    _ClInterfaceGroupName_Type()
)
clInterfaceGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clInterfaceGroupName.setStatus("current")
_ClInterfaceGroupDescr_Type = SnmpAdminString
_ClInterfaceGroupDescr_Object = MibTableColumn
clInterfaceGroupDescr = _ClInterfaceGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 2),
    _ClInterfaceGroupDescr_Type()
)
clInterfaceGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupDescr.setStatus("current")
_ClInterfaceGroupIsQuarantine_Type = TruthValue
_ClInterfaceGroupIsQuarantine_Object = MibTableColumn
clInterfaceGroupIsQuarantine = _ClInterfaceGroupIsQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 3),
    _ClInterfaceGroupIsQuarantine_Type()
)
clInterfaceGroupIsQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clInterfaceGroupIsQuarantine.setStatus("current")
_ClInterfaceGroupRowStatus_Type = RowStatus
_ClInterfaceGroupRowStatus_Object = MibTableColumn
clInterfaceGroupRowStatus = _ClInterfaceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 4),
    _ClInterfaceGroupRowStatus_Type()
)
clInterfaceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupRowStatus.setStatus("current")
_ClInterfaceGroupMdnsProfileName_Type = SnmpAdminString
_ClInterfaceGroupMdnsProfileName_Object = MibTableColumn
clInterfaceGroupMdnsProfileName = _ClInterfaceGroupMdnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 5),
    _ClInterfaceGroupMdnsProfileName_Type()
)
clInterfaceGroupMdnsProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupMdnsProfileName.setStatus("current")


class _ClInterfaceGroupFailDetectMode_Type(Integer32):
    """Custom type clInterfaceGroupFailDetectMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 0),
          ("nonaggressive", 1))
    )


_ClInterfaceGroupFailDetectMode_Type.__name__ = "Integer32"
_ClInterfaceGroupFailDetectMode_Object = MibTableColumn
clInterfaceGroupFailDetectMode = _ClInterfaceGroupFailDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 6),
    _ClInterfaceGroupFailDetectMode_Type()
)
clInterfaceGroupFailDetectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupFailDetectMode.setStatus("current")
_ClInterfaceGroupsMappingTable_Object = MibTable
clInterfaceGroupsMappingTable = _ClInterfaceGroupsMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clInterfaceGroupsMappingTable.setStatus("current")
_ClInterfaceGroupsMappingEntry_Object = MibTableRow
clInterfaceGroupsMappingEntry = _ClInterfaceGroupsMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 3, 1)
)
clInterfaceGroupsMappingEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupName"),
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
)
if mibBuilder.loadTexts:
    clInterfaceGroupsMappingEntry.setStatus("current")
_ClInterfaceGroupMappingRowStatus_Type = RowStatus
_ClInterfaceGroupMappingRowStatus_Object = MibTableColumn
clInterfaceGroupMappingRowStatus = _ClInterfaceGroupMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 3, 1, 1),
    _ClInterfaceGroupMappingRowStatus_Type()
)
clInterfaceGroupMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupMappingRowStatus.setStatus("current")
_CiscoLwappInterfaceInfo_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceInfo = _CiscoLwappInterfaceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2)
)
_CLInterfaceTable_Object = MibTable
cLInterfaceTable = _CLInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLInterfaceTable.setStatus("current")
_CLInterfaceEntry_Object = MibTableRow
cLInterfaceEntry = _CLInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2, 1, 1)
)
cLInterfaceEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
)
if mibBuilder.loadTexts:
    cLInterfaceEntry.setStatus("current")
_CLInterfacePreviousAddressType_Type = InetAddressType
_CLInterfacePreviousAddressType_Object = MibTableColumn
cLInterfacePreviousAddressType = _CLInterfacePreviousAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2, 1, 1, 1),
    _CLInterfacePreviousAddressType_Type()
)
cLInterfacePreviousAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLInterfacePreviousAddressType.setStatus("current")
_CLInterfacePreviousAddress_Type = InetAddress
_CLInterfacePreviousAddress_Object = MibTableColumn
cLInterfacePreviousAddress = _CLInterfacePreviousAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2, 1, 1, 2),
    _CLInterfacePreviousAddress_Type()
)
cLInterfacePreviousAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLInterfacePreviousAddress.setStatus("current")
_CLInterfaceCurrentAddressType_Type = InetAddressType
_CLInterfaceCurrentAddressType_Object = MibTableColumn
cLInterfaceCurrentAddressType = _CLInterfaceCurrentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2, 1, 1, 3),
    _CLInterfaceCurrentAddressType_Type()
)
cLInterfaceCurrentAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLInterfaceCurrentAddressType.setStatus("current")
_CLInterfaceCurrentAddress_Type = InetAddress
_CLInterfaceCurrentAddress_Object = MibTableColumn
cLInterfaceCurrentAddress = _CLInterfaceCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 2, 1, 1, 4),
    _CLInterfaceCurrentAddress_Type()
)
cLInterfaceCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLInterfaceCurrentAddress.setStatus("current")
_CiscoLwappInterfaceMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBConform = _CiscoLwappInterfaceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2)
)
_CiscoLwappInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBCompliances = _CiscoLwappInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1)
)
_CiscoLwappInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBGroups = _CiscoLwappInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2)
)

# Managed Objects groups

ciscoLwappInterfaceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 1)
)
ciscoLwappInterfaceConfigGroup.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceWired"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceQuarantineVlanId"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceConfigGroup.setStatus("deprecated")

ciscoLwappInterfaceGroupConfigSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 2)
)
ciscoLwappInterfaceGroupConfigSup1.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupDescr"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupIsQuarantine"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupRowStatus"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupMappingRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceGroupConfigSup1.setStatus("deprecated")

ciscoLwappInterfaceConfigGroupRev01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 3)
)
ciscoLwappInterfaceConfigGroupRev01.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceWired"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceQuarantineVlanId"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceDhcpOpt82Enabled"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceDhcpProxyMode"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceMdnsProfileName"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceNasId"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceMappingRedPort"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryIPv6AddrType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryIPv6Addr"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryPrefixLen"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryIPv6GatewayType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryIPv6Gateway"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceIPv6AclName"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceLinkLocalIDType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceLinkLocalID"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceIPv6SLAAC"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceLinkSelectEnabled"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceLinkSelectRelaySrcIntf"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceVpnSelectEnabled"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceVpnSelectVpnId"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceVpnselectVrfName"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryIpv6AddrStatus"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceLinkLocalIpv6AddrStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceConfigGroupRev01.setStatus("current")

ciscoLwappInterfaceGroupConfigSup1Rev01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 4)
)
ciscoLwappInterfaceGroupConfigSup1Rev01.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupDescr"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupIsQuarantine"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupRowStatus"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupMappingRowStatus"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupMdnsProfileName"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupFailDetectMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceGroupConfigSup1Rev01.setStatus("current")

ciscoLwappInterfaceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 5)
)
ciscoLwappInterfaceInfoGroup.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "cLInterfacePreviousAddressType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfacePreviousAddress"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfaceCurrentAddressType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfaceCurrentAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceInfoGroup.setStatus("current")


# Notification objects

ciscoLwappInterfaceAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 0, 1)
)
ciscoLwappInterfaceAddressChanged.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfacePreviousAddressType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfacePreviousAddress"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfaceCurrentAddressType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfaceCurrentAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceAddressChanged.setStatus(
        "current"
    )

ciscoLwappInterfaceIpv6AddressStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 0, 2)
)
ciscoLwappInterfaceIpv6AddressStatus.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfacePrimaryIpv6AddrStatus"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfaceCurrentAddressType"),
        ("CISCO-LWAPP-INTERFACE-MIB", "cLInterfaceCurrentAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceIpv6AddressStatus.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappInterfaceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 6)
)
ciscoLwappInterfaceNotificationGroup.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceAddressChanged"),
        ("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceIpv6AddressStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1, 1)
)
ciscoLwappInterfaceMIBCompliance.setObjects(
    ("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappInterfaceMIBComplianceRev01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1, 2)
)
ciscoLwappInterfaceMIBComplianceRev01.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceConfigGroup"),
        ("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceGroupConfigSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIBComplianceRev01.setStatus(
        "deprecated"
    )

ciscoLwappInterfaceMIBComplianceRev02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1, 3)
)
ciscoLwappInterfaceMIBComplianceRev02.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceConfigGroupRev01"),
        ("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceGroupConfigSup1Rev01"),
        ("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceInfoGroup"),
        ("CISCO-LWAPP-INTERFACE-MIB", "ciscoLwappInterfaceNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIBComplianceRev02.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-INTERFACE-MIB",
    **{"ciscoLwappInterfaceMIB": ciscoLwappInterfaceMIB,
       "ciscoLwappInterfaceMIBNotifs": ciscoLwappInterfaceMIBNotifs,
       "ciscoLwappInterfaceAddressChanged": ciscoLwappInterfaceAddressChanged,
       "ciscoLwappInterfaceIpv6AddressStatus": ciscoLwappInterfaceIpv6AddressStatus,
       "ciscoLwappInterfaceMIBObjects": ciscoLwappInterfaceMIBObjects,
       "ciscoLwappInterfaceConfig": ciscoLwappInterfaceConfig,
       "clInterfaceConfigTable": clInterfaceConfigTable,
       "clInterfaceConfigEntry": clInterfaceConfigEntry,
       "clInterfaceName": clInterfaceName,
       "clInterfaceWired": clInterfaceWired,
       "clInterfaceQuarantineVlanId": clInterfaceQuarantineVlanId,
       "clInterfaceDhcpOpt82Enabled": clInterfaceDhcpOpt82Enabled,
       "clInterfaceDhcpProxyMode": clInterfaceDhcpProxyMode,
       "clInterfaceMdnsProfileName": clInterfaceMdnsProfileName,
       "clInterfaceNasId": clInterfaceNasId,
       "clInterfaceMappingRedPort": clInterfaceMappingRedPort,
       "clInterfacePrimaryIPv6AddrType": clInterfacePrimaryIPv6AddrType,
       "clInterfacePrimaryIPv6Addr": clInterfacePrimaryIPv6Addr,
       "clInterfacePrimaryPrefixLen": clInterfacePrimaryPrefixLen,
       "clInterfacePrimaryIPv6GatewayType": clInterfacePrimaryIPv6GatewayType,
       "clInterfacePrimaryIPv6Gateway": clInterfacePrimaryIPv6Gateway,
       "clInterfaceIPv6AclName": clInterfaceIPv6AclName,
       "clInterfaceLinkLocalIDType": clInterfaceLinkLocalIDType,
       "clInterfaceLinkLocalID": clInterfaceLinkLocalID,
       "clInterfaceIPv6SLAAC": clInterfaceIPv6SLAAC,
       "clInterfaceLinkSelectEnabled": clInterfaceLinkSelectEnabled,
       "clInterfaceLinkSelectRelaySrcIntf": clInterfaceLinkSelectRelaySrcIntf,
       "clInterfaceVpnSelectEnabled": clInterfaceVpnSelectEnabled,
       "clInterfaceVpnSelectVpnId": clInterfaceVpnSelectVpnId,
       "clInterfaceVpnselectVrfName": clInterfaceVpnselectVrfName,
       "clInterfacePrimaryIpv6AddrStatus": clInterfacePrimaryIpv6AddrStatus,
       "clInterfaceLinkLocalIpv6AddrStatus": clInterfaceLinkLocalIpv6AddrStatus,
       "clInterfaceGroupsConfigTable": clInterfaceGroupsConfigTable,
       "clInterfaceGroupsConfigEntry": clInterfaceGroupsConfigEntry,
       "clInterfaceGroupName": clInterfaceGroupName,
       "clInterfaceGroupDescr": clInterfaceGroupDescr,
       "clInterfaceGroupIsQuarantine": clInterfaceGroupIsQuarantine,
       "clInterfaceGroupRowStatus": clInterfaceGroupRowStatus,
       "clInterfaceGroupMdnsProfileName": clInterfaceGroupMdnsProfileName,
       "clInterfaceGroupFailDetectMode": clInterfaceGroupFailDetectMode,
       "clInterfaceGroupsMappingTable": clInterfaceGroupsMappingTable,
       "clInterfaceGroupsMappingEntry": clInterfaceGroupsMappingEntry,
       "clInterfaceGroupMappingRowStatus": clInterfaceGroupMappingRowStatus,
       "ciscoLwappInterfaceInfo": ciscoLwappInterfaceInfo,
       "cLInterfaceTable": cLInterfaceTable,
       "cLInterfaceEntry": cLInterfaceEntry,
       "cLInterfacePreviousAddressType": cLInterfacePreviousAddressType,
       "cLInterfacePreviousAddress": cLInterfacePreviousAddress,
       "cLInterfaceCurrentAddressType": cLInterfaceCurrentAddressType,
       "cLInterfaceCurrentAddress": cLInterfaceCurrentAddress,
       "ciscoLwappInterfaceMIBConform": ciscoLwappInterfaceMIBConform,
       "ciscoLwappInterfaceMIBCompliances": ciscoLwappInterfaceMIBCompliances,
       "ciscoLwappInterfaceMIBCompliance": ciscoLwappInterfaceMIBCompliance,
       "ciscoLwappInterfaceMIBComplianceRev01": ciscoLwappInterfaceMIBComplianceRev01,
       "ciscoLwappInterfaceMIBComplianceRev02": ciscoLwappInterfaceMIBComplianceRev02,
       "ciscoLwappInterfaceMIBGroups": ciscoLwappInterfaceMIBGroups,
       "ciscoLwappInterfaceConfigGroup": ciscoLwappInterfaceConfigGroup,
       "ciscoLwappInterfaceGroupConfigSup1": ciscoLwappInterfaceGroupConfigSup1,
       "ciscoLwappInterfaceConfigGroupRev01": ciscoLwappInterfaceConfigGroupRev01,
       "ciscoLwappInterfaceGroupConfigSup1Rev01": ciscoLwappInterfaceGroupConfigSup1Rev01,
       "ciscoLwappInterfaceInfoGroup": ciscoLwappInterfaceInfoGroup,
       "ciscoLwappInterfaceNotificationGroup": ciscoLwappInterfaceNotificationGroup}
)
