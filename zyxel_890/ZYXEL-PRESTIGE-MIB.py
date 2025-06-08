# SNMP MIB module (ZYXEL-PRESTIGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-PRESTIGE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:35:51 2025
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

(atportIndex,) = mibBuilder.importSymbols(
    "APPLETALK-MIB",
    "atportIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

(egpNeighAddr,
 ipRouteDest) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "egpNeighAddr",
    "ipRouteDest")

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
 NotificationType,
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
    "NotificationType",
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

(prestigeCommon,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "prestigeCommon")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrestigeSystem_ObjectIdentity = ObjectIdentity
prestigeSystem = _PrestigeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1)
)
_SysRasFWVersion_Type = DisplayString
_SysRasFWVersion_Object = MibScalar
sysRasFWVersion = _SysRasFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 1),
    _SysRasFWVersion_Type()
)
sysRasFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRasFWVersion.setStatus("mandatory")
_SysHWVersion_Type = DisplayString
_SysHWVersion_Object = MibScalar
sysHWVersion = _SysHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 2),
    _SysHWVersion_Type()
)
sysHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHWVersion.setStatus("mandatory")
_SysModemVersion_Type = DisplayString
_SysModemVersion_Object = MibScalar
sysModemVersion = _SysModemVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 3),
    _SysModemVersion_Type()
)
sysModemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModemVersion.setStatus("mandatory")


class _SysSysName_Type(DisplayString):
    """Custom type sysSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_SysSysName_Type.__name__ = "DisplayString"
_SysSysName_Object = MibScalar
sysSysName = _SysSysName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 4),
    _SysSysName_Type()
)
sysSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 5),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")


class _SysConatctPersion_Type(DisplayString):
    """Custom type sysConatctPersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_SysConatctPersion_Type.__name__ = "DisplayString"
_SysConatctPersion_Object = MibScalar
sysConatctPersion = _SysConatctPersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 6),
    _SysConatctPersion_Type()
)
sysConatctPersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConatctPersion.setStatus("mandatory")


class _SysProtocolRouteIp_Type(Integer32):
    """Custom type sysProtocolRouteIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_SysProtocolRouteIp_Type.__name__ = "Integer32"
_SysProtocolRouteIp_Object = MibScalar
sysProtocolRouteIp = _SysProtocolRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 7),
    _SysProtocolRouteIp_Type()
)
sysProtocolRouteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysProtocolRouteIp.setStatus("mandatory")


class _SysProtocolBridge_Type(Integer32):
    """Custom type sysProtocolBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_SysProtocolBridge_Type.__name__ = "Integer32"
_SysProtocolBridge_Object = MibScalar
sysProtocolBridge = _SysProtocolBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 8),
    _SysProtocolBridge_Type()
)
sysProtocolBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysProtocolBridge.setStatus("mandatory")


class _SysDomainName_Type(DisplayString):
    """Custom type sysDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_SysDomainName_Type.__name__ = "DisplayString"
_SysDomainName_Object = MibScalar
sysDomainName = _SysDomainName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 9),
    _SysDomainName_Type()
)
sysDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDomainName.setStatus("mandatory")


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 1, 10),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")
_PrestigeDynDns_ObjectIdentity = ObjectIdentity
prestigeDynDns = _PrestigeDynDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2)
)


class _DdnsActiveStatus_Type(Integer32):
    """Custom type ddnsActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_DdnsActiveStatus_Type.__name__ = "Integer32"
_DdnsActiveStatus_Object = MibScalar
ddnsActiveStatus = _DdnsActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 1),
    _DdnsActiveStatus_Type()
)
ddnsActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsActiveStatus.setStatus("mandatory")


class _DdnsServiceProvider_Type(Integer32):
    """Custom type ddnsServiceProvider based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dyndns", 2))
    )


_DdnsServiceProvider_Type.__name__ = "Integer32"
_DdnsServiceProvider_Object = MibScalar
ddnsServiceProvider = _DdnsServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 2),
    _DdnsServiceProvider_Type()
)
ddnsServiceProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsServiceProvider.setStatus("mandatory")


class _DdnsHost_Type(DisplayString):
    """Custom type ddnsHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DdnsHost_Type.__name__ = "DisplayString"
_DdnsHost_Object = MibScalar
ddnsHost = _DdnsHost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 3),
    _DdnsHost_Type()
)
ddnsHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsHost.setStatus("mandatory")


class _DdnsEmail_Type(DisplayString):
    """Custom type ddnsEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DdnsEmail_Type.__name__ = "DisplayString"
_DdnsEmail_Object = MibScalar
ddnsEmail = _DdnsEmail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 4),
    _DdnsEmail_Type()
)
ddnsEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsEmail.setStatus("mandatory")


class _DdnsUser_Type(DisplayString):
    """Custom type ddnsUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DdnsUser_Type.__name__ = "DisplayString"
_DdnsUser_Object = MibScalar
ddnsUser = _DdnsUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 5),
    _DdnsUser_Type()
)
ddnsUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsUser.setStatus("mandatory")


class _DdnsPassword_Type(DisplayString):
    """Custom type ddnsPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DdnsPassword_Type.__name__ = "DisplayString"
_DdnsPassword_Object = MibScalar
ddnsPassword = _DdnsPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 6),
    _DdnsPassword_Type()
)
ddnsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsPassword.setStatus("mandatory")


class _DdnsEnableWildcard_Type(Integer32):
    """Custom type ddnsEnableWildcard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_DdnsEnableWildcard_Type.__name__ = "Integer32"
_DdnsEnableWildcard_Object = MibScalar
ddnsEnableWildcard = _DdnsEnableWildcard_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 2, 7),
    _DdnsEnableWildcard_Type()
)
ddnsEnableWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsEnableWildcard.setStatus("mandatory")
_PrestigeLAN_ObjectIdentity = ObjectIdentity
prestigeLAN = _PrestigeLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3)
)
_LanFilter_ObjectIdentity = ObjectIdentity
lanFilter = _LanFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 1)
)


class _InProtocolFilterSet_Type(DisplayString):
    """Custom type inProtocolFilterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_InProtocolFilterSet_Type.__name__ = "DisplayString"
_InProtocolFilterSet_Object = MibScalar
inProtocolFilterSet = _InProtocolFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 1, 1),
    _InProtocolFilterSet_Type()
)
inProtocolFilterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inProtocolFilterSet.setStatus("mandatory")


class _InDeviceFilterSet_Type(DisplayString):
    """Custom type inDeviceFilterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_InDeviceFilterSet_Type.__name__ = "DisplayString"
_InDeviceFilterSet_Object = MibScalar
inDeviceFilterSet = _InDeviceFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 1, 2),
    _InDeviceFilterSet_Type()
)
inDeviceFilterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inDeviceFilterSet.setStatus("mandatory")


class _OutProtocolFilterSet_Type(DisplayString):
    """Custom type outProtocolFilterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OutProtocolFilterSet_Type.__name__ = "DisplayString"
_OutProtocolFilterSet_Object = MibScalar
outProtocolFilterSet = _OutProtocolFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 1, 3),
    _OutProtocolFilterSet_Type()
)
outProtocolFilterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outProtocolFilterSet.setStatus("mandatory")


class _OutDeviceFilterSet_Type(DisplayString):
    """Custom type outDeviceFilterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OutDeviceFilterSet_Type.__name__ = "DisplayString"
_OutDeviceFilterSet_Object = MibScalar
outDeviceFilterSet = _OutDeviceFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 1, 4),
    _OutDeviceFilterSet_Type()
)
outDeviceFilterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outDeviceFilterSet.setStatus("mandatory")
_LanDHCP_ObjectIdentity = ObjectIdentity
lanDHCP = _LanDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2)
)


class _DhcpStatus_Type(Integer32):
    """Custom type dhcpStatus based on Integer32"""
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
          ("server", 2),
          ("relay", 3))
    )


_DhcpStatus_Type.__name__ = "Integer32"
_DhcpStatus_Object = MibScalar
dhcpStatus = _DhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2, 1),
    _DhcpStatus_Type()
)
dhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStatus.setStatus("mandatory")
_DhcpStartIpAddr_Type = IpAddress
_DhcpStartIpAddr_Object = MibScalar
dhcpStartIpAddr = _DhcpStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2, 2),
    _DhcpStartIpAddr_Type()
)
dhcpStartIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStartIpAddr.setStatus("mandatory")
_DhcpPoolSize_Type = Integer32
_DhcpPoolSize_Object = MibScalar
dhcpPoolSize = _DhcpPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2, 3),
    _DhcpPoolSize_Type()
)
dhcpPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolSize.setStatus("mandatory")
_DhcpPrimaryDnsServer_Type = IpAddress
_DhcpPrimaryDnsServer_Object = MibScalar
dhcpPrimaryDnsServer = _DhcpPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2, 4),
    _DhcpPrimaryDnsServer_Type()
)
dhcpPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPrimaryDnsServer.setStatus("mandatory")
_DhcpSecondaryDnsServer_Type = IpAddress
_DhcpSecondaryDnsServer_Object = MibScalar
dhcpSecondaryDnsServer = _DhcpSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2, 5),
    _DhcpSecondaryDnsServer_Type()
)
dhcpSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSecondaryDnsServer.setStatus("mandatory")
_DhcpRemoteDhcpServer_Type = IpAddress
_DhcpRemoteDhcpServer_Object = MibScalar
dhcpRemoteDhcpServer = _DhcpRemoteDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 2, 6),
    _DhcpRemoteDhcpServer_Type()
)
dhcpRemoteDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRemoteDhcpServer.setStatus("mandatory")
_LanTcpIp_ObjectIdentity = ObjectIdentity
lanTcpIp = _LanTcpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 3)
)
_LanIpAddress_Type = IpAddress
_LanIpAddress_Object = MibScalar
lanIpAddress = _LanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 3, 1),
    _LanIpAddress_Type()
)
lanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpAddress.setStatus("mandatory")
_LanIpSubnetMask_Type = IpAddress
_LanIpSubnetMask_Object = MibScalar
lanIpSubnetMask = _LanIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 3, 2),
    _LanIpSubnetMask_Type()
)
lanIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpSubnetMask.setStatus("mandatory")


class _LanIpRipDirection_Type(Integer32):
    """Custom type lanIpRipDirection based on Integer32"""
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
        *(("none", 1),
          ("both", 2),
          ("in", 3),
          ("out", 4))
    )


_LanIpRipDirection_Type.__name__ = "Integer32"
_LanIpRipDirection_Object = MibScalar
lanIpRipDirection = _LanIpRipDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 3, 3),
    _LanIpRipDirection_Type()
)
lanIpRipDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpRipDirection.setStatus("mandatory")


class _LanIpRipVersion_Type(Integer32):
    """Custom type lanIpRipVersion based on Integer32"""
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
        *(("ohter", 1),
          ("rip1", 2),
          ("rip2B", 3),
          ("rip2M", 4))
    )


_LanIpRipVersion_Type.__name__ = "Integer32"
_LanIpRipVersion_Object = MibScalar
lanIpRipVersion = _LanIpRipVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 3, 4),
    _LanIpRipVersion_Type()
)
lanIpRipVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpRipVersion.setStatus("mandatory")


class _LanIpMulticast_Type(Integer32):
    """Custom type lanIpMulticast based on Integer32"""
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
          ("igmpv1", 2),
          ("igmpv2", 3))
    )


_LanIpMulticast_Type.__name__ = "Integer32"
_LanIpMulticast_Object = MibScalar
lanIpMulticast = _LanIpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 3, 5),
    _LanIpMulticast_Type()
)
lanIpMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpMulticast.setStatus("mandatory")
_LanWireless_ObjectIdentity = ObjectIdentity
lanWireless = _LanWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4)
)
_WlanTable_Object = MibTable
wlanTable = _WlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    wlanTable.setStatus("mandatory")
_WlanEntry_Object = MibTableRow
wlanEntry = _WlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1)
)
wlanEntry.setIndexNames(
    (0, "ZYXEL-PRESTIGE-MIB", "wlanCardID"),
    (0, "ZYXEL-PRESTIGE-MIB", "wlanESSID"),
)
if mibBuilder.loadTexts:
    wlanEntry.setStatus("mandatory")


class _WlanEssStatus_Type(Integer32):
    """Custom type wlanEssStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2),
          ("inactive", 3))
    )


_WlanEssStatus_Type.__name__ = "Integer32"
_WlanEssStatus_Object = MibTableColumn
wlanEssStatus = _WlanEssStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 1),
    _WlanEssStatus_Type()
)
wlanEssStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEssStatus.setStatus("mandatory")
_WlanCardID_Type = Integer32
_WlanCardID_Object = MibTableColumn
wlanCardID = _WlanCardID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 2),
    _WlanCardID_Type()
)
wlanCardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCardID.setStatus("mandatory")


class _WlanESSID_Type(DisplayString):
    """Custom type wlanESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WlanESSID_Type.__name__ = "DisplayString"
_WlanESSID_Object = MibTableColumn
wlanESSID = _WlanESSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 3),
    _WlanESSID_Type()
)
wlanESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanESSID.setStatus("mandatory")


class _WlanHideESSID_Type(Integer32):
    """Custom type wlanHideESSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_WlanHideESSID_Type.__name__ = "Integer32"
_WlanHideESSID_Object = MibTableColumn
wlanHideESSID = _WlanHideESSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 4),
    _WlanHideESSID_Type()
)
wlanHideESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHideESSID.setStatus("mandatory")
_WlanChannelID_Type = Integer32
_WlanChannelID_Object = MibTableColumn
wlanChannelID = _WlanChannelID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 5),
    _WlanChannelID_Type()
)
wlanChannelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanChannelID.setStatus("mandatory")
_WlanRTSThreshold_Type = Integer32
_WlanRTSThreshold_Object = MibTableColumn
wlanRTSThreshold = _WlanRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 6),
    _WlanRTSThreshold_Type()
)
wlanRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRTSThreshold.setStatus("mandatory")
_WlanFragThreshold_Type = Integer32
_WlanFragThreshold_Object = MibTableColumn
wlanFragThreshold = _WlanFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 7),
    _WlanFragThreshold_Type()
)
wlanFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanFragThreshold.setStatus("mandatory")


class _WlanWEPStatus_Type(Integer32):
    """Custom type wlanWEPStatus based on Integer32"""
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
        *(("other", 1),
          ("disable", 2),
          ("WEP-64-bit", 3),
          ("WEP-128-bit", 4))
    )


_WlanWEPStatus_Type.__name__ = "Integer32"
_WlanWEPStatus_Object = MibTableColumn
wlanWEPStatus = _WlanWEPStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 8),
    _WlanWEPStatus_Type()
)
wlanWEPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWEPStatus.setStatus("mandatory")
_WlanDefaultKey_Type = Integer32
_WlanDefaultKey_Object = MibTableColumn
wlanDefaultKey = _WlanDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 9),
    _WlanDefaultKey_Type()
)
wlanDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDefaultKey.setStatus("mandatory")


class _WlanWepKey1_Type(DisplayString):
    """Custom type wlanWepKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_WlanWepKey1_Type.__name__ = "DisplayString"
_WlanWepKey1_Object = MibTableColumn
wlanWepKey1 = _WlanWepKey1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 10),
    _WlanWepKey1_Type()
)
wlanWepKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey1.setStatus("mandatory")


class _WlanWepKey2_Type(DisplayString):
    """Custom type wlanWepKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_WlanWepKey2_Type.__name__ = "DisplayString"
_WlanWepKey2_Object = MibTableColumn
wlanWepKey2 = _WlanWepKey2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 11),
    _WlanWepKey2_Type()
)
wlanWepKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey2.setStatus("mandatory")


class _WlanWepKey3_Type(DisplayString):
    """Custom type wlanWepKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_WlanWepKey3_Type.__name__ = "DisplayString"
_WlanWepKey3_Object = MibTableColumn
wlanWepKey3 = _WlanWepKey3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 12),
    _WlanWepKey3_Type()
)
wlanWepKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey3.setStatus("mandatory")


class _WlanWepKey4_Type(DisplayString):
    """Custom type wlanWepKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_WlanWepKey4_Type.__name__ = "DisplayString"
_WlanWepKey4_Object = MibTableColumn
wlanWepKey4 = _WlanWepKey4_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 3, 4, 1, 1, 13),
    _WlanWepKey4_Type()
)
wlanWepKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKey4.setStatus("mandatory")
_PrestigeStaticRoute_ObjectIdentity = ObjectIdentity
prestigeStaticRoute = _PrestigeStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4)
)
_IpStaticRouteTable_Object = MibTable
ipStaticRouteTable = _IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipStaticRouteTable.setStatus("mandatory")
_IpStaticRouteEntry_Object = MibTableRow
ipStaticRouteEntry = _IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1)
)
ipStaticRouteEntry.setIndexNames(
    (0, "ZYXEL-PRESTIGE-MIB", "ipStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    ipStaticRouteEntry.setStatus("mandatory")
_IpStaticRouteIndex_Type = Integer32
_IpStaticRouteIndex_Object = MibTableColumn
ipStaticRouteIndex = _IpStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 1),
    _IpStaticRouteIndex_Type()
)
ipStaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteIndex.setStatus("mandatory")


class _IpStaticRouteName_Type(DisplayString):
    """Custom type ipStaticRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IpStaticRouteName_Type.__name__ = "DisplayString"
_IpStaticRouteName_Object = MibTableColumn
ipStaticRouteName = _IpStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 2),
    _IpStaticRouteName_Type()
)
ipStaticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteName.setStatus("mandatory")


class _IpStaticRouteActiveStatus_Type(Integer32):
    """Custom type ipStaticRouteActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_IpStaticRouteActiveStatus_Type.__name__ = "Integer32"
_IpStaticRouteActiveStatus_Object = MibTableColumn
ipStaticRouteActiveStatus = _IpStaticRouteActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 3),
    _IpStaticRouteActiveStatus_Type()
)
ipStaticRouteActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteActiveStatus.setStatus("mandatory")
_IpStaticRouteDestIpAddr_Type = IpAddress
_IpStaticRouteDestIpAddr_Object = MibTableColumn
ipStaticRouteDestIpAddr = _IpStaticRouteDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 4),
    _IpStaticRouteDestIpAddr_Type()
)
ipStaticRouteDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteDestIpAddr.setStatus("mandatory")
_IpStaticRouteSubnetMask_Type = IpAddress
_IpStaticRouteSubnetMask_Object = MibTableColumn
ipStaticRouteSubnetMask = _IpStaticRouteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 5),
    _IpStaticRouteSubnetMask_Type()
)
ipStaticRouteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteSubnetMask.setStatus("mandatory")
_IpStaticRouteGatewayIpAddr_Type = IpAddress
_IpStaticRouteGatewayIpAddr_Object = MibTableColumn
ipStaticRouteGatewayIpAddr = _IpStaticRouteGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 6),
    _IpStaticRouteGatewayIpAddr_Type()
)
ipStaticRouteGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticRouteGatewayIpAddr.setStatus("mandatory")
_IpStaticRouteMetric_Type = Integer32
_IpStaticRouteMetric_Object = MibTableColumn
ipStaticRouteMetric = _IpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 7),
    _IpStaticRouteMetric_Type()
)
ipStaticRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteMetric.setStatus("mandatory")


class _IpStaticRoutePirvate_Type(Integer32):
    """Custom type ipStaticRoutePirvate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_IpStaticRoutePirvate_Type.__name__ = "Integer32"
_IpStaticRoutePirvate_Object = MibTableColumn
ipStaticRoutePirvate = _IpStaticRoutePirvate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 1, 1, 8),
    _IpStaticRoutePirvate_Type()
)
ipStaticRoutePirvate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRoutePirvate.setStatus("mandatory")
_BridgeStaticRouteTable_Object = MibTable
bridgeStaticRouteTable = _BridgeStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    bridgeStaticRouteTable.setStatus("mandatory")
_BridgeStaticRouteEntry_Object = MibTableRow
bridgeStaticRouteEntry = _BridgeStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1)
)
bridgeStaticRouteEntry.setIndexNames(
    (0, "ZYXEL-PRESTIGE-MIB", "bridgeStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    bridgeStaticRouteEntry.setStatus("mandatory")
_BridgeStaticRouteIndex_Type = Integer32
_BridgeStaticRouteIndex_Object = MibTableColumn
bridgeStaticRouteIndex = _BridgeStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1, 1),
    _BridgeStaticRouteIndex_Type()
)
bridgeStaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStaticRouteIndex.setStatus("mandatory")


class _BridgeStaticRouteName_Type(DisplayString):
    """Custom type bridgeStaticRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_BridgeStaticRouteName_Type.__name__ = "DisplayString"
_BridgeStaticRouteName_Object = MibTableColumn
bridgeStaticRouteName = _BridgeStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1, 2),
    _BridgeStaticRouteName_Type()
)
bridgeStaticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStaticRouteName.setStatus("mandatory")


class _BridgeStaticRouteActiveStatus_Type(Integer32):
    """Custom type bridgeStaticRouteActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_BridgeStaticRouteActiveStatus_Type.__name__ = "Integer32"
_BridgeStaticRouteActiveStatus_Object = MibTableColumn
bridgeStaticRouteActiveStatus = _BridgeStaticRouteActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1, 3),
    _BridgeStaticRouteActiveStatus_Type()
)
bridgeStaticRouteActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStaticRouteActiveStatus.setStatus("mandatory")
_BridgeStaticRouteEtherAddr_Type = PhysAddress
_BridgeStaticRouteEtherAddr_Object = MibTableColumn
bridgeStaticRouteEtherAddr = _BridgeStaticRouteEtherAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1, 4),
    _BridgeStaticRouteEtherAddr_Type()
)
bridgeStaticRouteEtherAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStaticRouteEtherAddr.setStatus("mandatory")
_BridgeStaticRouteIpAddr_Type = IpAddress
_BridgeStaticRouteIpAddr_Object = MibTableColumn
bridgeStaticRouteIpAddr = _BridgeStaticRouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1, 5),
    _BridgeStaticRouteIpAddr_Type()
)
bridgeStaticRouteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStaticRouteIpAddr.setStatus("mandatory")
_BridgeStaticRouteGatewayNode_Type = Integer32
_BridgeStaticRouteGatewayNode_Object = MibTableColumn
bridgeStaticRouteGatewayNode = _BridgeStaticRouteGatewayNode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 4, 2, 1, 6),
    _BridgeStaticRouteGatewayNode_Type()
)
bridgeStaticRouteGatewayNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStaticRouteGatewayNode.setStatus("mandatory")
_PrestigeFilterConfig_ObjectIdentity = ObjectIdentity
prestigeFilterConfig = _PrestigeFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5)
)
_FilterSetTable_Object = MibTable
filterSetTable = _FilterSetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    filterSetTable.setStatus("mandatory")
_FilterSetEntry_Object = MibTableRow
filterSetEntry = _FilterSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 1, 1)
)
filterSetEntry.setIndexNames(
    (0, "ZYXEL-PRESTIGE-MIB", "filterSetIndex"),
)
if mibBuilder.loadTexts:
    filterSetEntry.setStatus("mandatory")
_FilterSetIndex_Type = Integer32
_FilterSetIndex_Object = MibTableColumn
filterSetIndex = _FilterSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 1, 1, 1),
    _FilterSetIndex_Type()
)
filterSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterSetIndex.setStatus("mandatory")


class _FilterSetComment_Type(DisplayString):
    """Custom type filterSetComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_FilterSetComment_Type.__name__ = "DisplayString"
_FilterSetComment_Object = MibTableColumn
filterSetComment = _FilterSetComment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 1, 1, 2),
    _FilterSetComment_Type()
)
filterSetComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSetComment.setStatus("mandatory")
_FilterRuleTable_Object = MibTable
filterRuleTable = _FilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    filterRuleTable.setStatus("mandatory")
_FilterRuleEntry_Object = MibTableRow
filterRuleEntry = _FilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1)
)
filterRuleEntry.setIndexNames(
    (0, "ZYXEL-PRESTIGE-MIB", "filterSetIndex"),
    (0, "ZYXEL-PRESTIGE-MIB", "filterRuleIndex"),
)
if mibBuilder.loadTexts:
    filterRuleEntry.setStatus("mandatory")
_FilterRuleIndex_Type = Integer32
_FilterRuleIndex_Object = MibTableColumn
filterRuleIndex = _FilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 1),
    _FilterRuleIndex_Type()
)
filterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterRuleIndex.setStatus("mandatory")


class _FilterRuleActiveStatus_Type(Integer32):
    """Custom type filterRuleActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_FilterRuleActiveStatus_Type.__name__ = "Integer32"
_FilterRuleActiveStatus_Object = MibTableColumn
filterRuleActiveStatus = _FilterRuleActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 2),
    _FilterRuleActiveStatus_Type()
)
filterRuleActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleActiveStatus.setStatus("mandatory")


class _FilterRuleType_Type(Integer32):
    """Custom type filterRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcpIp", 2),
          ("generic", 3))
    )


_FilterRuleType_Type.__name__ = "Integer32"
_FilterRuleType_Object = MibTableColumn
filterRuleType = _FilterRuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 3),
    _FilterRuleType_Type()
)
filterRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleType.setStatus("mandatory")


class _FilterRuleIpProtocol_Type(Integer32):
    """Custom type filterRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FilterRuleIpProtocol_Type.__name__ = "Integer32"
_FilterRuleIpProtocol_Object = MibTableColumn
filterRuleIpProtocol = _FilterRuleIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 4),
    _FilterRuleIpProtocol_Type()
)
filterRuleIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleIpProtocol.setStatus("mandatory")


class _FilterRuleIpSourceRoute_Type(Integer32):
    """Custom type filterRuleIpSourceRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_FilterRuleIpSourceRoute_Type.__name__ = "Integer32"
_FilterRuleIpSourceRoute_Object = MibTableColumn
filterRuleIpSourceRoute = _FilterRuleIpSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 5),
    _FilterRuleIpSourceRoute_Type()
)
filterRuleIpSourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleIpSourceRoute.setStatus("mandatory")
_FilterRuleDestIpAddr_Type = IpAddress
_FilterRuleDestIpAddr_Object = MibTableColumn
filterRuleDestIpAddr = _FilterRuleDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 6),
    _FilterRuleDestIpAddr_Type()
)
filterRuleDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleDestIpAddr.setStatus("mandatory")
_FilterRuleDestIpMask_Type = IpAddress
_FilterRuleDestIpMask_Object = MibTableColumn
filterRuleDestIpMask = _FilterRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 7),
    _FilterRuleDestIpMask_Type()
)
filterRuleDestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleDestIpMask.setStatus("mandatory")


class _FilterRuleDestPort_Type(Integer32):
    """Custom type filterRuleDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterRuleDestPort_Type.__name__ = "Integer32"
_FilterRuleDestPort_Object = MibTableColumn
filterRuleDestPort = _FilterRuleDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 8),
    _FilterRuleDestPort_Type()
)
filterRuleDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleDestPort.setStatus("mandatory")


class _FilterRuleDestPortComp_Type(Integer32):
    """Custom type filterRuleDestPortComp based on Integer32"""
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
        *(("none", 1),
          ("equal", 2),
          ("notequal", 3),
          ("less", 4),
          ("greater", 5))
    )


_FilterRuleDestPortComp_Type.__name__ = "Integer32"
_FilterRuleDestPortComp_Object = MibTableColumn
filterRuleDestPortComp = _FilterRuleDestPortComp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 9),
    _FilterRuleDestPortComp_Type()
)
filterRuleDestPortComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleDestPortComp.setStatus("mandatory")
_FilterRuleSourceIpAddr_Type = IpAddress
_FilterRuleSourceIpAddr_Object = MibTableColumn
filterRuleSourceIpAddr = _FilterRuleSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 10),
    _FilterRuleSourceIpAddr_Type()
)
filterRuleSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleSourceIpAddr.setStatus("mandatory")
_FilterRuleSourceIpMask_Type = IpAddress
_FilterRuleSourceIpMask_Object = MibTableColumn
filterRuleSourceIpMask = _FilterRuleSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 11),
    _FilterRuleSourceIpMask_Type()
)
filterRuleSourceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleSourceIpMask.setStatus("mandatory")


class _FilterRuleSourcePort_Type(Integer32):
    """Custom type filterRuleSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterRuleSourcePort_Type.__name__ = "Integer32"
_FilterRuleSourcePort_Object = MibTableColumn
filterRuleSourcePort = _FilterRuleSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 12),
    _FilterRuleSourcePort_Type()
)
filterRuleSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleSourcePort.setStatus("mandatory")


class _FilterRuleSourcePortComp_Type(Integer32):
    """Custom type filterRuleSourcePortComp based on Integer32"""
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
        *(("none", 1),
          ("equal", 2),
          ("notequal", 3),
          ("less", 4),
          ("greater", 5))
    )


_FilterRuleSourcePortComp_Type.__name__ = "Integer32"
_FilterRuleSourcePortComp_Object = MibTableColumn
filterRuleSourcePortComp = _FilterRuleSourcePortComp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 13),
    _FilterRuleSourcePortComp_Type()
)
filterRuleSourcePortComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleSourcePortComp.setStatus("mandatory")


class _FilterRuleTcpEstab_Type(Integer32):
    """Custom type filterRuleTcpEstab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_FilterRuleTcpEstab_Type.__name__ = "Integer32"
_FilterRuleTcpEstab_Object = MibTableColumn
filterRuleTcpEstab = _FilterRuleTcpEstab_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 14),
    _FilterRuleTcpEstab_Type()
)
filterRuleTcpEstab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleTcpEstab.setStatus("mandatory")


class _FilterRuleGenericOffset_Type(Integer32):
    """Custom type filterRuleGenericOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FilterRuleGenericOffset_Type.__name__ = "Integer32"
_FilterRuleGenericOffset_Object = MibTableColumn
filterRuleGenericOffset = _FilterRuleGenericOffset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 15),
    _FilterRuleGenericOffset_Type()
)
filterRuleGenericOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleGenericOffset.setStatus("mandatory")


class _FilterRuleGenericLength_Type(Integer32):
    """Custom type filterRuleGenericLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FilterRuleGenericLength_Type.__name__ = "Integer32"
_FilterRuleGenericLength_Object = MibTableColumn
filterRuleGenericLength = _FilterRuleGenericLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 16),
    _FilterRuleGenericLength_Type()
)
filterRuleGenericLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleGenericLength.setStatus("mandatory")


class _FilterRuleGenericMask_Type(OctetString):
    """Custom type filterRuleGenericMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FilterRuleGenericMask_Type.__name__ = "OctetString"
_FilterRuleGenericMask_Object = MibTableColumn
filterRuleGenericMask = _FilterRuleGenericMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 17),
    _FilterRuleGenericMask_Type()
)
filterRuleGenericMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleGenericMask.setStatus("mandatory")


class _FilterRuleGenericValue_Type(OctetString):
    """Custom type filterRuleGenericValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FilterRuleGenericValue_Type.__name__ = "OctetString"
_FilterRuleGenericValue_Object = MibTableColumn
filterRuleGenericValue = _FilterRuleGenericValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 18),
    _FilterRuleGenericValue_Type()
)
filterRuleGenericValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleGenericValue.setStatus("mandatory")


class _FilterRuleMore_Type(Integer32):
    """Custom type filterRuleMore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("yes", 2),
          ("no", 3))
    )


_FilterRuleMore_Type.__name__ = "Integer32"
_FilterRuleMore_Object = MibTableColumn
filterRuleMore = _FilterRuleMore_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 19),
    _FilterRuleMore_Type()
)
filterRuleMore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleMore.setStatus("mandatory")


class _FilterRuleLog_Type(Integer32):
    """Custom type filterRuleLog based on Integer32"""
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
        *(("none", 1),
          ("actMatched", 2),
          ("atcNotMatch", 3),
          ("both", 4))
    )


_FilterRuleLog_Type.__name__ = "Integer32"
_FilterRuleLog_Object = MibTableColumn
filterRuleLog = _FilterRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 20),
    _FilterRuleLog_Type()
)
filterRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleLog.setStatus("mandatory")


class _FilterRuleActMatched_Type(Integer32):
    """Custom type filterRuleActMatched based on Integer32"""
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
        *(("other", 1),
          ("checkNextRule", 2),
          ("forward", 3),
          ("drop", 4))
    )


_FilterRuleActMatched_Type.__name__ = "Integer32"
_FilterRuleActMatched_Object = MibTableColumn
filterRuleActMatched = _FilterRuleActMatched_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 21),
    _FilterRuleActMatched_Type()
)
filterRuleActMatched.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleActMatched.setStatus("mandatory")


class _FilterRuleActNotMatched_Type(Integer32):
    """Custom type filterRuleActNotMatched based on Integer32"""
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
        *(("other", 1),
          ("checkNextRule", 2),
          ("forward", 3),
          ("drop", 4))
    )


_FilterRuleActNotMatched_Type.__name__ = "Integer32"
_FilterRuleActNotMatched_Object = MibTableColumn
filterRuleActNotMatched = _FilterRuleActNotMatched_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 5, 2, 1, 22),
    _FilterRuleActNotMatched_Type()
)
filterRuleActNotMatched.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRuleActNotMatched.setStatus("mandatory")
_PrestigeXDSL_ObjectIdentity = ObjectIdentity
prestigeXDSL = _PrestigeXDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 6)
)
_PrestigeTraps_ObjectIdentity = ObjectIdentity
prestigeTraps = _PrestigeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 99)
)
_WhyReboot_Type = DisplayString
_WhyReboot_Object = MibScalar
whyReboot = _WhyReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 99, 1),
    _WhyReboot_Type()
)
whyReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whyReboot.setStatus("mandatory")

# Managed Objects groups


# Notification objects

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 2, 1, 0, 1)
)
reboot.setObjects(
    ("ZYXEL-PRESTIGE-MIB", "whyReboot")
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PRESTIGE-MIB",
    **{"reboot": reboot,
       "prestigeSystem": prestigeSystem,
       "sysRasFWVersion": sysRasFWVersion,
       "sysHWVersion": sysHWVersion,
       "sysModemVersion": sysModemVersion,
       "sysSysName": sysSysName,
       "sysLocation": sysLocation,
       "sysConatctPersion": sysConatctPersion,
       "sysProtocolRouteIp": sysProtocolRouteIp,
       "sysProtocolBridge": sysProtocolBridge,
       "sysDomainName": sysDomainName,
       "sysReset": sysReset,
       "prestigeDynDns": prestigeDynDns,
       "ddnsActiveStatus": ddnsActiveStatus,
       "ddnsServiceProvider": ddnsServiceProvider,
       "ddnsHost": ddnsHost,
       "ddnsEmail": ddnsEmail,
       "ddnsUser": ddnsUser,
       "ddnsPassword": ddnsPassword,
       "ddnsEnableWildcard": ddnsEnableWildcard,
       "prestigeLAN": prestigeLAN,
       "lanFilter": lanFilter,
       "inProtocolFilterSet": inProtocolFilterSet,
       "inDeviceFilterSet": inDeviceFilterSet,
       "outProtocolFilterSet": outProtocolFilterSet,
       "outDeviceFilterSet": outDeviceFilterSet,
       "lanDHCP": lanDHCP,
       "dhcpStatus": dhcpStatus,
       "dhcpStartIpAddr": dhcpStartIpAddr,
       "dhcpPoolSize": dhcpPoolSize,
       "dhcpPrimaryDnsServer": dhcpPrimaryDnsServer,
       "dhcpSecondaryDnsServer": dhcpSecondaryDnsServer,
       "dhcpRemoteDhcpServer": dhcpRemoteDhcpServer,
       "lanTcpIp": lanTcpIp,
       "lanIpAddress": lanIpAddress,
       "lanIpSubnetMask": lanIpSubnetMask,
       "lanIpRipDirection": lanIpRipDirection,
       "lanIpRipVersion": lanIpRipVersion,
       "lanIpMulticast": lanIpMulticast,
       "lanWireless": lanWireless,
       "wlanTable": wlanTable,
       "wlanEntry": wlanEntry,
       "wlanEssStatus": wlanEssStatus,
       "wlanCardID": wlanCardID,
       "wlanESSID": wlanESSID,
       "wlanHideESSID": wlanHideESSID,
       "wlanChannelID": wlanChannelID,
       "wlanRTSThreshold": wlanRTSThreshold,
       "wlanFragThreshold": wlanFragThreshold,
       "wlanWEPStatus": wlanWEPStatus,
       "wlanDefaultKey": wlanDefaultKey,
       "wlanWepKey1": wlanWepKey1,
       "wlanWepKey2": wlanWepKey2,
       "wlanWepKey3": wlanWepKey3,
       "wlanWepKey4": wlanWepKey4,
       "prestigeStaticRoute": prestigeStaticRoute,
       "ipStaticRouteTable": ipStaticRouteTable,
       "ipStaticRouteEntry": ipStaticRouteEntry,
       "ipStaticRouteIndex": ipStaticRouteIndex,
       "ipStaticRouteName": ipStaticRouteName,
       "ipStaticRouteActiveStatus": ipStaticRouteActiveStatus,
       "ipStaticRouteDestIpAddr": ipStaticRouteDestIpAddr,
       "ipStaticRouteSubnetMask": ipStaticRouteSubnetMask,
       "ipStaticRouteGatewayIpAddr": ipStaticRouteGatewayIpAddr,
       "ipStaticRouteMetric": ipStaticRouteMetric,
       "ipStaticRoutePirvate": ipStaticRoutePirvate,
       "bridgeStaticRouteTable": bridgeStaticRouteTable,
       "bridgeStaticRouteEntry": bridgeStaticRouteEntry,
       "bridgeStaticRouteIndex": bridgeStaticRouteIndex,
       "bridgeStaticRouteName": bridgeStaticRouteName,
       "bridgeStaticRouteActiveStatus": bridgeStaticRouteActiveStatus,
       "bridgeStaticRouteEtherAddr": bridgeStaticRouteEtherAddr,
       "bridgeStaticRouteIpAddr": bridgeStaticRouteIpAddr,
       "bridgeStaticRouteGatewayNode": bridgeStaticRouteGatewayNode,
       "prestigeFilterConfig": prestigeFilterConfig,
       "filterSetTable": filterSetTable,
       "filterSetEntry": filterSetEntry,
       "filterSetIndex": filterSetIndex,
       "filterSetComment": filterSetComment,
       "filterRuleTable": filterRuleTable,
       "filterRuleEntry": filterRuleEntry,
       "filterRuleIndex": filterRuleIndex,
       "filterRuleActiveStatus": filterRuleActiveStatus,
       "filterRuleType": filterRuleType,
       "filterRuleIpProtocol": filterRuleIpProtocol,
       "filterRuleIpSourceRoute": filterRuleIpSourceRoute,
       "filterRuleDestIpAddr": filterRuleDestIpAddr,
       "filterRuleDestIpMask": filterRuleDestIpMask,
       "filterRuleDestPort": filterRuleDestPort,
       "filterRuleDestPortComp": filterRuleDestPortComp,
       "filterRuleSourceIpAddr": filterRuleSourceIpAddr,
       "filterRuleSourceIpMask": filterRuleSourceIpMask,
       "filterRuleSourcePort": filterRuleSourcePort,
       "filterRuleSourcePortComp": filterRuleSourcePortComp,
       "filterRuleTcpEstab": filterRuleTcpEstab,
       "filterRuleGenericOffset": filterRuleGenericOffset,
       "filterRuleGenericLength": filterRuleGenericLength,
       "filterRuleGenericMask": filterRuleGenericMask,
       "filterRuleGenericValue": filterRuleGenericValue,
       "filterRuleMore": filterRuleMore,
       "filterRuleLog": filterRuleLog,
       "filterRuleActMatched": filterRuleActMatched,
       "filterRuleActNotMatched": filterRuleActNotMatched,
       "prestigeXDSL": prestigeXDSL,
       "prestigeTraps": prestigeTraps,
       "whyReboot": whyReboot}
)
