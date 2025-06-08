# SNMP MIB module (PWTv1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/superior_power_42610/PWTv1-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:03:30 2025
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Powertek_ObjectIdentity = ObjectIdentity
powertek = _Powertek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4)
)
_Pwt_ObjectIdentity = ObjectIdentity
pwt = _Pwt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4)
)
_PduObjects_ObjectIdentity = ObjectIdentity
pduObjects = _PduObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1)
)
_PduIdent_ObjectIdentity = ObjectIdentity
pduIdent = _PduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 1)
)


class _PduIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type pduIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_PduIdentAgentSoftwareVersion_Object = MibScalar
pduIdentAgentSoftwareVersion = _PduIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 1, 1),
    _PduIdentAgentSoftwareVersion_Type()
)
pduIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIdentAgentSoftwareVersion.setStatus("mandatory")


class _PduIdentSerialNumber_Type(DisplayString):
    """Custom type pduIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduIdentSerialNumber_Type.__name__ = "DisplayString"
_PduIdentSerialNumber_Object = MibScalar
pduIdentSerialNumber = _PduIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 1, 2),
    _PduIdentSerialNumber_Type()
)
pduIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIdentSerialNumber.setStatus("mandatory")
_PduNetwork_ObjectIdentity = ObjectIdentity
pduNetwork = _PduNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2)
)
_PduNetworkTcpip_ObjectIdentity = ObjectIdentity
pduNetworkTcpip = _PduNetworkTcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1)
)


class _PduNetworkTcpipDhcpControl_Type(Integer32):
    """Custom type pduNetworkTcpipDhcpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkTcpipDhcpControl_Type.__name__ = "Integer32"
_PduNetworkTcpipDhcpControl_Object = MibScalar
pduNetworkTcpipDhcpControl = _PduNetworkTcpipDhcpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 1),
    _PduNetworkTcpipDhcpControl_Type()
)
pduNetworkTcpipDhcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipDhcpControl.setStatus("mandatory")
_PduNetworkTcpipIpv4_ObjectIdentity = ObjectIdentity
pduNetworkTcpipIpv4 = _PduNetworkTcpipIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2)
)
_PduNetworkTcpipIpv4Address_Type = IpAddress
_PduNetworkTcpipIpv4Address_Object = MibScalar
pduNetworkTcpipIpv4Address = _PduNetworkTcpipIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 1),
    _PduNetworkTcpipIpv4Address_Type()
)
pduNetworkTcpipIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4Address.setStatus("mandatory")
_PduNetworkTcpipIpv4Gateway_Type = IpAddress
_PduNetworkTcpipIpv4Gateway_Object = MibScalar
pduNetworkTcpipIpv4Gateway = _PduNetworkTcpipIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 2),
    _PduNetworkTcpipIpv4Gateway_Type()
)
pduNetworkTcpipIpv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4Gateway.setStatus("mandatory")
_PduNetworkTcpipIpv4Subnet_Type = IpAddress
_PduNetworkTcpipIpv4Subnet_Object = MibScalar
pduNetworkTcpipIpv4Subnet = _PduNetworkTcpipIpv4Subnet_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 3),
    _PduNetworkTcpipIpv4Subnet_Type()
)
pduNetworkTcpipIpv4Subnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4Subnet.setStatus("mandatory")
_PduNetworkTcpipIpv4PrimaryDNS_Type = IpAddress
_PduNetworkTcpipIpv4PrimaryDNS_Object = MibScalar
pduNetworkTcpipIpv4PrimaryDNS = _PduNetworkTcpipIpv4PrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 4),
    _PduNetworkTcpipIpv4PrimaryDNS_Type()
)
pduNetworkTcpipIpv4PrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4PrimaryDNS.setStatus("mandatory")
_PduNetworkTcpipIpv4SecondaryDNS_Type = IpAddress
_PduNetworkTcpipIpv4SecondaryDNS_Object = MibScalar
pduNetworkTcpipIpv4SecondaryDNS = _PduNetworkTcpipIpv4SecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 5),
    _PduNetworkTcpipIpv4SecondaryDNS_Type()
)
pduNetworkTcpipIpv4SecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4SecondaryDNS.setStatus("mandatory")
_PduNetworkTcpipIpv6_ObjectIdentity = ObjectIdentity
pduNetworkTcpipIpv6 = _PduNetworkTcpipIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3)
)


class _PduNetworkTcpipIpv6Control_Type(Integer32):
    """Custom type pduNetworkTcpipIpv6Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkTcpipIpv6Control_Type.__name__ = "Integer32"
_PduNetworkTcpipIpv6Control_Object = MibScalar
pduNetworkTcpipIpv6Control = _PduNetworkTcpipIpv6Control_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 1),
    _PduNetworkTcpipIpv6Control_Type()
)
pduNetworkTcpipIpv6Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Control.setStatus("mandatory")


class _PduNetworkTcpipIpv6AutoConfig_Type(Integer32):
    """Custom type pduNetworkTcpipIpv6AutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_PduNetworkTcpipIpv6AutoConfig_Type.__name__ = "Integer32"
_PduNetworkTcpipIpv6AutoConfig_Object = MibScalar
pduNetworkTcpipIpv6AutoConfig = _PduNetworkTcpipIpv6AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 2),
    _PduNetworkTcpipIpv6AutoConfig_Type()
)
pduNetworkTcpipIpv6AutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6AutoConfig.setStatus("mandatory")


class _PduNetworkTcpipIpv6Address_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6Address_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6Address_Object = MibScalar
pduNetworkTcpipIpv6Address = _PduNetworkTcpipIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 3),
    _PduNetworkTcpipIpv6Address_Type()
)
pduNetworkTcpipIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Address.setStatus("mandatory")
_PduNetworkTcpipIpv6Prefix_Type = Integer32
_PduNetworkTcpipIpv6Prefix_Object = MibScalar
pduNetworkTcpipIpv6Prefix = _PduNetworkTcpipIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 4),
    _PduNetworkTcpipIpv6Prefix_Type()
)
pduNetworkTcpipIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Prefix.setStatus("mandatory")


class _PduNetworkTcpipIpv6Router_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6Router_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6Router_Object = MibScalar
pduNetworkTcpipIpv6Router = _PduNetworkTcpipIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 5),
    _PduNetworkTcpipIpv6Router_Type()
)
pduNetworkTcpipIpv6Router.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Router.setStatus("mandatory")


class _PduNetworkTcpipIpv6PrimaryDNS_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6PrimaryDNS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6PrimaryDNS_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6PrimaryDNS_Object = MibScalar
pduNetworkTcpipIpv6PrimaryDNS = _PduNetworkTcpipIpv6PrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 6),
    _PduNetworkTcpipIpv6PrimaryDNS_Type()
)
pduNetworkTcpipIpv6PrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6PrimaryDNS.setStatus("mandatory")


class _PduNetworkTcpipIpv6SecondaryDNS_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6SecondaryDNS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6SecondaryDNS_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6SecondaryDNS_Object = MibScalar
pduNetworkTcpipIpv6SecondaryDNS = _PduNetworkTcpipIpv6SecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 7),
    _PduNetworkTcpipIpv6SecondaryDNS_Type()
)
pduNetworkTcpipIpv6SecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6SecondaryDNS.setStatus("mandatory")
_PduNetworkSecurity_ObjectIdentity = ObjectIdentity
pduNetworkSecurity = _PduNetworkSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2)
)


class _PduNetworkSecurityControl_Type(Integer32):
    """Custom type pduNetworkSecurityControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecurityControl_Type.__name__ = "Integer32"
_PduNetworkSecurityControl_Object = MibScalar
pduNetworkSecurityControl = _PduNetworkSecurityControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 1),
    _PduNetworkSecurityControl_Type()
)
pduNetworkSecurityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityControl.setStatus("mandatory")
_PduNetworkSecuritySsh_ObjectIdentity = ObjectIdentity
pduNetworkSecuritySsh = _PduNetworkSecuritySsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2)
)


class _PduNetworkSecuritySshControl_Type(Integer32):
    """Custom type pduNetworkSecuritySshControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecuritySshControl_Type.__name__ = "Integer32"
_PduNetworkSecuritySshControl_Object = MibScalar
pduNetworkSecuritySshControl = _PduNetworkSecuritySshControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 1),
    _PduNetworkSecuritySshControl_Type()
)
pduNetworkSecuritySshControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshControl.setStatus("mandatory")


class _PduNetworkSecuritySshInterval_Type(Integer32):
    """Custom type pduNetworkSecuritySshInterval based on Integer32"""
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
        *(("oneMinute", 1),
          ("fiveMinutes", 2),
          ("tenMinutes", 3),
          ("thirtyMinutes", 4))
    )


_PduNetworkSecuritySshInterval_Type.__name__ = "Integer32"
_PduNetworkSecuritySshInterval_Object = MibScalar
pduNetworkSecuritySshInterval = _PduNetworkSecuritySshInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 2),
    _PduNetworkSecuritySshInterval_Type()
)
pduNetworkSecuritySshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshInterval.setStatus("mandatory")


class _PduNetworkSecuritySshFailTimes_Type(Integer32):
    """Custom type pduNetworkSecuritySshFailTimes based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("thirty", 4),
          ("hundred", 5))
    )


_PduNetworkSecuritySshFailTimes_Type.__name__ = "Integer32"
_PduNetworkSecuritySshFailTimes_Object = MibScalar
pduNetworkSecuritySshFailTimes = _PduNetworkSecuritySshFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 3),
    _PduNetworkSecuritySshFailTimes_Type()
)
pduNetworkSecuritySshFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshFailTimes.setStatus("mandatory")


class _PduNetworkSecuritySshBlock_Type(Integer32):
    """Custom type pduNetworkSecuritySshBlock based on Integer32"""
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
        *(("fiveMinutes", 1),
          ("thirtyMinutes", 2),
          ("oneHour", 3),
          ("oneDay", 4))
    )


_PduNetworkSecuritySshBlock_Type.__name__ = "Integer32"
_PduNetworkSecuritySshBlock_Object = MibScalar
pduNetworkSecuritySshBlock = _PduNetworkSecuritySshBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 4),
    _PduNetworkSecuritySshBlock_Type()
)
pduNetworkSecuritySshBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshBlock.setStatus("mandatory")
_PduNetworkSecuritySnmp_ObjectIdentity = ObjectIdentity
pduNetworkSecuritySnmp = _PduNetworkSecuritySnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3)
)


class _PduNetworkSecuritySnmpControl_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecuritySnmpControl_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpControl_Object = MibScalar
pduNetworkSecuritySnmpControl = _PduNetworkSecuritySnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 1),
    _PduNetworkSecuritySnmpControl_Type()
)
pduNetworkSecuritySnmpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpControl.setStatus("mandatory")


class _PduNetworkSecuritySnmpInterval_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpInterval based on Integer32"""
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
        *(("oneMinute", 1),
          ("fiveMinutes", 2),
          ("tenMinutes", 3),
          ("thirtyMinutes", 4))
    )


_PduNetworkSecuritySnmpInterval_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpInterval_Object = MibScalar
pduNetworkSecuritySnmpInterval = _PduNetworkSecuritySnmpInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 2),
    _PduNetworkSecuritySnmpInterval_Type()
)
pduNetworkSecuritySnmpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpInterval.setStatus("mandatory")


class _PduNetworkSecuritySnmpFailTimes_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpFailTimes based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("thirty", 4),
          ("hundred", 5))
    )


_PduNetworkSecuritySnmpFailTimes_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpFailTimes_Object = MibScalar
pduNetworkSecuritySnmpFailTimes = _PduNetworkSecuritySnmpFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 3),
    _PduNetworkSecuritySnmpFailTimes_Type()
)
pduNetworkSecuritySnmpFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpFailTimes.setStatus("mandatory")


class _PduNetworkSecuritySnmpBlock_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpBlock based on Integer32"""
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
        *(("fiveMinutes", 1),
          ("thirtyMinutes", 2),
          ("oneHour", 3),
          ("oneDay", 4))
    )


_PduNetworkSecuritySnmpBlock_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpBlock_Object = MibScalar
pduNetworkSecuritySnmpBlock = _PduNetworkSecuritySnmpBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 4),
    _PduNetworkSecuritySnmpBlock_Type()
)
pduNetworkSecuritySnmpBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpBlock.setStatus("mandatory")
_PduNetworkSecurityHttp_ObjectIdentity = ObjectIdentity
pduNetworkSecurityHttp = _PduNetworkSecurityHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4)
)


class _PduNetworkSecurityHttpControl_Type(Integer32):
    """Custom type pduNetworkSecurityHttpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecurityHttpControl_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpControl_Object = MibScalar
pduNetworkSecurityHttpControl = _PduNetworkSecurityHttpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 1),
    _PduNetworkSecurityHttpControl_Type()
)
pduNetworkSecurityHttpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpControl.setStatus("mandatory")


class _PduNetworkSecurityHttpInterval_Type(Integer32):
    """Custom type pduNetworkSecurityHttpInterval based on Integer32"""
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
        *(("oneMinute", 1),
          ("fiveMinutes", 2),
          ("tenMinutes", 3),
          ("thirtyMinutes", 4))
    )


_PduNetworkSecurityHttpInterval_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpInterval_Object = MibScalar
pduNetworkSecurityHttpInterval = _PduNetworkSecurityHttpInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 2),
    _PduNetworkSecurityHttpInterval_Type()
)
pduNetworkSecurityHttpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpInterval.setStatus("mandatory")


class _PduNetworkSecurityHttpFailTimes_Type(Integer32):
    """Custom type pduNetworkSecurityHttpFailTimes based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("thirty", 4),
          ("hundred", 5))
    )


_PduNetworkSecurityHttpFailTimes_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpFailTimes_Object = MibScalar
pduNetworkSecurityHttpFailTimes = _PduNetworkSecurityHttpFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 3),
    _PduNetworkSecurityHttpFailTimes_Type()
)
pduNetworkSecurityHttpFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpFailTimes.setStatus("mandatory")


class _PduNetworkSecurityHttpBlock_Type(Integer32):
    """Custom type pduNetworkSecurityHttpBlock based on Integer32"""
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
        *(("fiveMinutes", 1),
          ("thirtyMinutes", 2),
          ("oneHour", 3),
          ("oneDay", 4))
    )


_PduNetworkSecurityHttpBlock_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpBlock_Object = MibScalar
pduNetworkSecurityHttpBlock = _PduNetworkSecurityHttpBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 4),
    _PduNetworkSecurityHttpBlock_Type()
)
pduNetworkSecurityHttpBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpBlock.setStatus("mandatory")
_PduNetworkService_ObjectIdentity = ObjectIdentity
pduNetworkService = _PduNetworkService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3)
)
_PduNetworkServiceSsh_ObjectIdentity = ObjectIdentity
pduNetworkServiceSsh = _PduNetworkServiceSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 1)
)


class _PduNetworkServiceSshControl_Type(Integer32):
    """Custom type pduNetworkServiceSshControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceSshControl_Type.__name__ = "Integer32"
_PduNetworkServiceSshControl_Object = MibScalar
pduNetworkServiceSshControl = _PduNetworkServiceSshControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 1, 1),
    _PduNetworkServiceSshControl_Type()
)
pduNetworkServiceSshControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSshControl.setStatus("mandatory")
_PduNetworkServiceSshPort_Type = Integer32
_PduNetworkServiceSshPort_Object = MibScalar
pduNetworkServiceSshPort = _PduNetworkServiceSshPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 1, 2),
    _PduNetworkServiceSshPort_Type()
)
pduNetworkServiceSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSshPort.setStatus("mandatory")
_PduNetworkServiceSsl_ObjectIdentity = ObjectIdentity
pduNetworkServiceSsl = _PduNetworkServiceSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2)
)


class _PduNetworkServiceSslControl_Type(Integer32):
    """Custom type pduNetworkServiceSslControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceSslControl_Type.__name__ = "Integer32"
_PduNetworkServiceSslControl_Object = MibScalar
pduNetworkServiceSslControl = _PduNetworkServiceSslControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2, 1),
    _PduNetworkServiceSslControl_Type()
)
pduNetworkServiceSslControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSslControl.setStatus("mandatory")
_PduNetworkServiceSslPort_Type = Integer32
_PduNetworkServiceSslPort_Object = MibScalar
pduNetworkServiceSslPort = _PduNetworkServiceSslPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2, 2),
    _PduNetworkServiceSslPort_Type()
)
pduNetworkServiceSslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSslPort.setStatus("mandatory")


class _PduNetworkServiceSslForce_Type(Integer32):
    """Custom type pduNetworkServiceSslForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceSslForce_Type.__name__ = "Integer32"
_PduNetworkServiceSslForce_Object = MibScalar
pduNetworkServiceSslForce = _PduNetworkServiceSslForce_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2, 3),
    _PduNetworkServiceSslForce_Type()
)
pduNetworkServiceSslForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSslForce.setStatus("mandatory")


class _PduNetworkServicePingControl_Type(Integer32):
    """Custom type pduNetworkServicePingControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServicePingControl_Type.__name__ = "Integer32"
_PduNetworkServicePingControl_Object = MibScalar
pduNetworkServicePingControl = _PduNetworkServicePingControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 3),
    _PduNetworkServicePingControl_Type()
)
pduNetworkServicePingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServicePingControl.setStatus("mandatory")
_PduNetworkServiceRadius_ObjectIdentity = ObjectIdentity
pduNetworkServiceRadius = _PduNetworkServiceRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4)
)


class _PduNetworkServiceRadiusControl_Type(Integer32):
    """Custom type pduNetworkServiceRadiusControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceRadiusControl_Type.__name__ = "Integer32"
_PduNetworkServiceRadiusControl_Object = MibScalar
pduNetworkServiceRadiusControl = _PduNetworkServiceRadiusControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 1),
    _PduNetworkServiceRadiusControl_Type()
)
pduNetworkServiceRadiusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusControl.setStatus("mandatory")


class _PduNetworkServiceRadiusIp_Type(DisplayString):
    """Custom type pduNetworkServiceRadiusIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkServiceRadiusIp_Type.__name__ = "DisplayString"
_PduNetworkServiceRadiusIp_Object = MibScalar
pduNetworkServiceRadiusIp = _PduNetworkServiceRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 2),
    _PduNetworkServiceRadiusIp_Type()
)
pduNetworkServiceRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusIp.setStatus("mandatory")
_PduNetworkServiceRadiusPort_Type = Integer32
_PduNetworkServiceRadiusPort_Object = MibScalar
pduNetworkServiceRadiusPort = _PduNetworkServiceRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 3),
    _PduNetworkServiceRadiusPort_Type()
)
pduNetworkServiceRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusPort.setStatus("mandatory")


class _PduNetworkServiceRadiusSecretKey_Type(DisplayString):
    """Custom type pduNetworkServiceRadiusSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduNetworkServiceRadiusSecretKey_Type.__name__ = "DisplayString"
_PduNetworkServiceRadiusSecretKey_Object = MibScalar
pduNetworkServiceRadiusSecretKey = _PduNetworkServiceRadiusSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 4),
    _PduNetworkServiceRadiusSecretKey_Type()
)
pduNetworkServiceRadiusSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusSecretKey.setStatus("mandatory")
_PduNetworkServiceRadiusTimeout_Type = Integer32
_PduNetworkServiceRadiusTimeout_Object = MibScalar
pduNetworkServiceRadiusTimeout = _PduNetworkServiceRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 5),
    _PduNetworkServiceRadiusTimeout_Type()
)
pduNetworkServiceRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusTimeout.setStatus("mandatory")
_PduNetworkServiceRadiusRetry_Type = Integer32
_PduNetworkServiceRadiusRetry_Object = MibScalar
pduNetworkServiceRadiusRetry = _PduNetworkServiceRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 6),
    _PduNetworkServiceRadiusRetry_Type()
)
pduNetworkServiceRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusRetry.setStatus("mandatory")
_PduSystem_ObjectIdentity = ObjectIdentity
pduSystem = _PduSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3)
)


class _PduSystemName_Type(DisplayString):
    """Custom type pduSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSystemName_Type.__name__ = "DisplayString"
_PduSystemName_Object = MibScalar
pduSystemName = _PduSystemName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 1),
    _PduSystemName_Type()
)
pduSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemName.setStatus("mandatory")


class _PduSystemContact_Type(DisplayString):
    """Custom type pduSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSystemContact_Type.__name__ = "DisplayString"
_PduSystemContact_Object = MibScalar
pduSystemContact = _PduSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 2),
    _PduSystemContact_Type()
)
pduSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemContact.setStatus("mandatory")


class _PduSystemLocation_Type(DisplayString):
    """Custom type pduSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSystemLocation_Type.__name__ = "DisplayString"
_PduSystemLocation_Object = MibScalar
pduSystemLocation = _PduSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 3),
    _PduSystemLocation_Type()
)
pduSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemLocation.setStatus("mandatory")
_PduSystemLogInterval_Type = Integer32
_PduSystemLogInterval_Object = MibScalar
pduSystemLogInterval = _PduSystemLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 4),
    _PduSystemLogInterval_Type()
)
pduSystemLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemLogInterval.setStatus("mandatory")


class _PduSystemWebRefresh_Type(Integer32):
    """Custom type pduSystemWebRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_PduSystemWebRefresh_Type.__name__ = "Integer32"
_PduSystemWebRefresh_Object = MibScalar
pduSystemWebRefresh = _PduSystemWebRefresh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 5),
    _PduSystemWebRefresh_Type()
)
pduSystemWebRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemWebRefresh.setStatus("mandatory")
_PduSystemTime_ObjectIdentity = ObjectIdentity
pduSystemTime = _PduSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6)
)
_PduSystemTimeDisplay_Type = DisplayString
_PduSystemTimeDisplay_Object = MibScalar
pduSystemTimeDisplay = _PduSystemTimeDisplay_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 1),
    _PduSystemTimeDisplay_Type()
)
pduSystemTimeDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSystemTimeDisplay.setStatus("mandatory")


class _PduSystemTimeZone_Type(Integer32):
    """Custom type pduSystemTimeZone based on Integer32"""
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
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("gMT-1200InternationalDateLineWest", 1),
          ("gMT-1200Eniwetok-Kwajalein", 2),
          ("gMT-1100MidwayIsland-Samoa", 3),
          ("gMT-1000Hawaii", 4),
          ("gMT-0900Alaska", 5),
          ("gMT-0800PacificTime-Tijuana", 6),
          ("gMT-0700Arizona-MountainTime", 7),
          ("gMT-0700Chihuahua-LaPaz-Mazatlan", 8),
          ("gMT-0700MountainTime", 9),
          ("gMT-0600CentralAmerica", 10),
          ("gMT-0600CentralTime", 11),
          ("gMT-0600Guadalajara-MexicoCity-Monterrey", 12),
          ("gMT-0600Saskatchewan", 13),
          ("gMT-0500Bogota-Lima-Quito", 14),
          ("gMT-0500EasternTime", 15),
          ("gMT-0500Indiana", 16),
          ("gMT-0400AtlanticTime", 17),
          ("gMT-0400Caracas-LaPaz", 18),
          ("gMT-0400Santiago", 19),
          ("gMT-0330Newfoundland", 20),
          ("gMT-0300Brasilia", 21),
          ("gMT-0300BuenosAires-Georgetown", 22),
          ("gMT-0300Greenland", 23),
          ("gMT-0200Mid-Atlantic", 24),
          ("gMT-0100Azores", 25),
          ("gMT-0100CapeVerdeIs", 26),
          ("gMT-0000Casablanca-Monrovia", 27),
          ("gMT-0000GreenwichMeanTime-Dublin-Edinburgh-Lisbon-London", 28),
          ("gMT0100Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 29),
          ("gMT0100Belgrade-Bratislava-Budapest-Ljubljana-Prague", 30),
          ("gMT0100Brussels-Copenhagen-Madrid-Paris", 31),
          ("gMT0100Sarajevo-Skopje-Warsaw-Zagreb", 32),
          ("gMT0100WestCentralAfrica", 33),
          ("gMT0200Athens-Istanbul-Minsk", 34),
          ("gMT0200Bucharest", 35),
          ("gMT0200Cairo", 36),
          ("gMT0200Harare-Pretoria", 37),
          ("gMT0200Helsinki-Kyiv-Riga-Sofia-Tallinn-Vilnius", 38),
          ("gMT0200Jerusalem", 39),
          ("gMT0300Baghdad", 40),
          ("gMT0300Kuwait-Riyadh", 41),
          ("gMT0300Moscow-StPetersburg-Volgograd", 42),
          ("gMT0300Nairobi", 43),
          ("gMT0330Tehran", 44),
          ("gMT0400AbuDhabi-Muscat", 45),
          ("gMT0400Baku-Tbilisi-Yerevan", 46),
          ("gMT0430Kabul", 47),
          ("gMT0500Ekaterinburg", 48),
          ("gMT0500Islamabad-Karachi-Tashkent", 49),
          ("gMT0530Bombay-Calcutta", 50),
          ("gMT0530Chennai-Kolkata-Mumbai-NewDelhi", 51),
          ("gMT0545Kathmandu", 52),
          ("gMT0600Almaty-Novosibirsk", 53),
          ("gMT0600Astana-Dhaka", 54),
          ("gMT0600SriJayawardenepura", 55),
          ("gMT0630Rangoon", 56),
          ("gMT0700Bangkok-Hanoi-Jakarta", 57),
          ("gMT0700Krasnoyarsk", 58),
          ("gMT0800Beijing-Chongqing-HongKong-Urumqi", 59),
          ("gMT0800Irkutsk-UlaanBataar", 60),
          ("gMT0800KualaLumpur-Singapore", 61),
          ("gMT0800Perth", 62),
          ("gMT0800Taipei", 63),
          ("gMT0900Osaka-Sapporo-Tokyo", 64),
          ("gMT0900Seoul", 65),
          ("gMT0900Yakutsk", 66),
          ("gMT0930Adelaide", 67),
          ("gMT0930Darwin", 68),
          ("gMT1000Brisbane", 69),
          ("gMT1000Canberra-Melbourne-Sydney", 70),
          ("gMT1000Guam-PortMoresby", 71),
          ("gMT1000Hobart", 72),
          ("gMT1000Vladivostok", 73),
          ("gMT1100Magadan-SolomonIs-NewCaledonia", 74),
          ("gMT1200Auckland-Wellington", 75),
          ("gMT1200Fiji-Kamchatka-MarshallIs", 76),
          ("gMT1300NukuAlofa", 77))
    )


_PduSystemTimeZone_Type.__name__ = "Integer32"
_PduSystemTimeZone_Object = MibScalar
pduSystemTimeZone = _PduSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 2),
    _PduSystemTimeZone_Type()
)
pduSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeZone.setStatus("mandatory")


class _PduSystemTimeFormat_Type(Integer32):
    """Custom type pduSystemTimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddmmyyyy", 1),
          ("mmddyyyy", 2),
          ("yyyymmdd", 3))
    )


_PduSystemTimeFormat_Type.__name__ = "Integer32"
_PduSystemTimeFormat_Object = MibScalar
pduSystemTimeFormat = _PduSystemTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 3),
    _PduSystemTimeFormat_Type()
)
pduSystemTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeFormat.setStatus("mandatory")


class _PduSystemTimeSetting_Type(Integer32):
    """Custom type pduSystemTimeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twentyFourHrFormat", 1),
          ("twelveHrFormat", 2))
    )


_PduSystemTimeSetting_Type.__name__ = "Integer32"
_PduSystemTimeSetting_Object = MibScalar
pduSystemTimeSetting = _PduSystemTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 4),
    _PduSystemTimeSetting_Type()
)
pduSystemTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeSetting.setStatus("mandatory")


class _PduSystemTimeDayLightSaving_Type(Integer32):
    """Custom type pduSystemTimeDayLightSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduSystemTimeDayLightSaving_Type.__name__ = "Integer32"
_PduSystemTimeDayLightSaving_Object = MibScalar
pduSystemTimeDayLightSaving = _PduSystemTimeDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 5),
    _PduSystemTimeDayLightSaving_Type()
)
pduSystemTimeDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeDayLightSaving.setStatus("mandatory")
_PduSystemTimeManual_ObjectIdentity = ObjectIdentity
pduSystemTimeManual = _PduSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 6)
)


class _PduSystemTimeManualDate_Type(DisplayString):
    """Custom type pduSystemTimeManualDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_PduSystemTimeManualDate_Type.__name__ = "DisplayString"
_PduSystemTimeManualDate_Object = MibScalar
pduSystemTimeManualDate = _PduSystemTimeManualDate_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 6, 1),
    _PduSystemTimeManualDate_Type()
)
pduSystemTimeManualDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeManualDate.setStatus("mandatory")


class _PduSystemTimeManualTime_Type(DisplayString):
    """Custom type pduSystemTimeManualTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PduSystemTimeManualTime_Type.__name__ = "DisplayString"
_PduSystemTimeManualTime_Object = MibScalar
pduSystemTimeManualTime = _PduSystemTimeManualTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 6, 2),
    _PduSystemTimeManualTime_Type()
)
pduSystemTimeManualTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeManualTime.setStatus("mandatory")
_PduSystemTimeNtp_ObjectIdentity = ObjectIdentity
pduSystemTimeNtp = _PduSystemTimeNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7)
)


class _PduSystemTimeNtpControl_Type(Integer32):
    """Custom type pduSystemTimeNtpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PduSystemTimeNtpControl_Type.__name__ = "Integer32"
_PduSystemTimeNtpControl_Object = MibScalar
pduSystemTimeNtpControl = _PduSystemTimeNtpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 1),
    _PduSystemTimeNtpControl_Type()
)
pduSystemTimeNtpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpControl.setStatus("mandatory")


class _PduSystemTimeNtpServer_Type(DisplayString):
    """Custom type pduSystemTimeNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduSystemTimeNtpServer_Type.__name__ = "DisplayString"
_PduSystemTimeNtpServer_Object = MibScalar
pduSystemTimeNtpServer = _PduSystemTimeNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 2),
    _PduSystemTimeNtpServer_Type()
)
pduSystemTimeNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpServer.setStatus("mandatory")
_PduSystemTimeNtpSyncInterval_Type = Integer32
_PduSystemTimeNtpSyncInterval_Object = MibScalar
pduSystemTimeNtpSyncInterval = _PduSystemTimeNtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 3),
    _PduSystemTimeNtpSyncInterval_Type()
)
pduSystemTimeNtpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpSyncInterval.setStatus("mandatory")


class _PduSystemTimeNtpSyncUnit_Type(Integer32):
    """Custom type pduSystemTimeNtpSyncUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 1),
          ("month", 2))
    )


_PduSystemTimeNtpSyncUnit_Type.__name__ = "Integer32"
_PduSystemTimeNtpSyncUnit_Object = MibScalar
pduSystemTimeNtpSyncUnit = _PduSystemTimeNtpSyncUnit_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 4),
    _PduSystemTimeNtpSyncUnit_Type()
)
pduSystemTimeNtpSyncUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpSyncUnit.setStatus("mandatory")


class _PduSystemResetToDefault_Type(Integer32):
    """Custom type pduSystemResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("reset", 2))
    )


_PduSystemResetToDefault_Type.__name__ = "Integer32"
_PduSystemResetToDefault_Object = MibScalar
pduSystemResetToDefault = _PduSystemResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 7),
    _PduSystemResetToDefault_Type()
)
pduSystemResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemResetToDefault.setStatus("mandatory")


class _PduSystemReboot_Type(Integer32):
    """Custom type pduSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("reboot", 2))
    )


_PduSystemReboot_Type.__name__ = "Integer32"
_PduSystemReboot_Object = MibScalar
pduSystemReboot = _PduSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 8),
    _PduSystemReboot_Type()
)
pduSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemReboot.setStatus("mandatory")
_PduSNMP_ObjectIdentity = ObjectIdentity
pduSNMP = _PduSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4)
)


class _PduSnmpControl_Type(Integer32):
    """Custom type pduSnmpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduSnmpControl_Type.__name__ = "Integer32"
_PduSnmpControl_Object = MibScalar
pduSnmpControl = _PduSnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 1),
    _PduSnmpControl_Type()
)
pduSnmpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpControl.setStatus("mandatory")
_PduSnmpPort_Type = Integer32
_PduSnmpPort_Object = MibScalar
pduSnmpPort = _PduSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 2),
    _PduSnmpPort_Type()
)
pduSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpPort.setStatus("mandatory")


class _PduSnmpVersion_Type(Integer32):
    """Custom type pduSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_PduSnmpVersion_Type.__name__ = "Integer32"
_PduSnmpVersion_Object = MibScalar
pduSnmpVersion = _PduSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 3),
    _PduSnmpVersion_Type()
)
pduSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpVersion.setStatus("mandatory")
_PduSnmpTrapsReceiversTable_Object = MibTable
pduSnmpTrapsReceiversTable = _PduSnmpTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    pduSnmpTrapsReceiversTable.setStatus("mandatory")
_PduSnmpTrapsReceiversEntry_Object = MibTableRow
pduSnmpTrapsReceiversEntry = _PduSnmpTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1)
)
pduSnmpTrapsReceiversEntry.setIndexNames(
    (0, "PWTv1-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    pduSnmpTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")


class _TrapsReceiverAddr_Type(DisplayString):
    """Custom type trapsReceiverAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TrapsReceiverAddr_Type.__name__ = "DisplayString"
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverEventLevel_Type(Integer32):
    """Custom type receiverEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("informational", 3))
    )


_ReceiverEventLevel_Type.__name__ = "Integer32"
_ReceiverEventLevel_Object = MibTableColumn
receiverEventLevel = _ReceiverEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 3),
    _ReceiverEventLevel_Type()
)
receiverEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverEventLevel.setStatus("mandatory")


class _ReceiverSnmpVer_Type(Integer32):
    """Custom type receiverSnmpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_ReceiverSnmpVer_Type.__name__ = "Integer32"
_ReceiverSnmpVer_Object = MibTableColumn
receiverSnmpVer = _ReceiverSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 4),
    _ReceiverSnmpVer_Type()
)
receiverSnmpVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverSnmpVer.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 5),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_PduEmail_ObjectIdentity = ObjectIdentity
pduEmail = _PduEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5)
)


class _PduEmailServer_Type(DisplayString):
    """Custom type pduEmailServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailServer_Type.__name__ = "DisplayString"
_PduEmailServer_Object = MibScalar
pduEmailServer = _PduEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 1),
    _PduEmailServer_Type()
)
pduEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailServer.setStatus("mandatory")
_PduEmailPort_Type = Integer32
_PduEmailPort_Object = MibScalar
pduEmailPort = _PduEmailPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 2),
    _PduEmailPort_Type()
)
pduEmailPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailPort.setStatus("mandatory")


class _PduEmailSenderEmail_Type(DisplayString):
    """Custom type pduEmailSenderEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSenderEmail_Type.__name__ = "DisplayString"
_PduEmailSenderEmail_Object = MibScalar
pduEmailSenderEmail = _PduEmailSenderEmail_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 3),
    _PduEmailSenderEmail_Type()
)
pduEmailSenderEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSenderEmail.setStatus("mandatory")


class _PduEmailPrefix_Type(DisplayString):
    """Custom type pduEmailPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailPrefix_Type.__name__ = "DisplayString"
_PduEmailPrefix_Object = MibScalar
pduEmailPrefix = _PduEmailPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 4),
    _PduEmailPrefix_Type()
)
pduEmailPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailPrefix.setStatus("mandatory")


class _PduEmailAuthControl_Type(Integer32):
    """Custom type pduEmailAuthControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmailAuthControl_Type.__name__ = "Integer32"
_PduEmailAuthControl_Object = MibScalar
pduEmailAuthControl = _PduEmailAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 5),
    _PduEmailAuthControl_Type()
)
pduEmailAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailAuthControl.setStatus("mandatory")


class _PduEmailAuthUsername_Type(DisplayString):
    """Custom type pduEmailAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailAuthUsername_Type.__name__ = "DisplayString"
_PduEmailAuthUsername_Object = MibScalar
pduEmailAuthUsername = _PduEmailAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 6),
    _PduEmailAuthUsername_Type()
)
pduEmailAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailAuthUsername.setStatus("mandatory")


class _PduEmailAuthPassword_Type(DisplayString):
    """Custom type pduEmailAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailAuthPassword_Type.__name__ = "DisplayString"
_PduEmailAuthPassword_Object = MibScalar
pduEmailAuthPassword = _PduEmailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 7),
    _PduEmailAuthPassword_Type()
)
pduEmailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailAuthPassword.setStatus("mandatory")
_PduEmailReceiversTable_Object = MibTable
pduEmailReceiversTable = _PduEmailReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8)
)
if mibBuilder.loadTexts:
    pduEmailReceiversTable.setStatus("mandatory")
_PduEmailReceiversEntry_Object = MibTableRow
pduEmailReceiversEntry = _PduEmailReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1)
)
pduEmailReceiversEntry.setIndexNames(
    (0, "PWTv1-MIB", "mailRecvIndex"),
)
if mibBuilder.loadTexts:
    pduEmailReceiversEntry.setStatus("mandatory")


class _MailRecvIndex_Type(Integer32):
    """Custom type mailRecvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MailRecvIndex_Type.__name__ = "Integer32"
_MailRecvIndex_Object = MibTableColumn
mailRecvIndex = _MailRecvIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 1),
    _MailRecvIndex_Type()
)
mailRecvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailRecvIndex.setStatus("mandatory")


class _MailRecvReceiverAddr_Type(DisplayString):
    """Custom type mailRecvReceiverAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MailRecvReceiverAddr_Type.__name__ = "DisplayString"
_MailRecvReceiverAddr_Object = MibTableColumn
mailRecvReceiverAddr = _MailRecvReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 2),
    _MailRecvReceiverAddr_Type()
)
mailRecvReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvReceiverAddr.setStatus("mandatory")


class _MailRecvEmailType_Type(Integer32):
    """Custom type mailRecvEmailType based on Integer32"""
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
          ("events", 2),
          ("status", 3),
          ("both", 4))
    )


_MailRecvEmailType_Type.__name__ = "Integer32"
_MailRecvEmailType_Object = MibTableColumn
mailRecvEmailType = _MailRecvEmailType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 3),
    _MailRecvEmailType_Type()
)
mailRecvEmailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvEmailType.setStatus("mandatory")


class _MailRecvEventLevel_Type(Integer32):
    """Custom type mailRecvEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("informational", 3))
    )


_MailRecvEventLevel_Type.__name__ = "Integer32"
_MailRecvEventLevel_Object = MibTableColumn
mailRecvEventLevel = _MailRecvEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 4),
    _MailRecvEventLevel_Type()
)
mailRecvEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvEventLevel.setStatus("mandatory")


class _MailRecvDescription_Type(DisplayString):
    """Custom type mailRecvDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MailRecvDescription_Type.__name__ = "DisplayString"
_MailRecvDescription_Object = MibTableColumn
mailRecvDescription = _MailRecvDescription_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 5),
    _MailRecvDescription_Type()
)
mailRecvDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvDescription.setStatus("mandatory")
_PduPwrMonitoring_ObjectIdentity = ObjectIdentity
pduPwrMonitoring = _PduPwrMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6)
)
_PduPwrMonitoringInlet_ObjectIdentity = ObjectIdentity
pduPwrMonitoringInlet = _PduPwrMonitoringInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1)
)
_PduPwrMonitoringInletNum_Type = Integer32
_PduPwrMonitoringInletNum_Object = MibScalar
pduPwrMonitoringInletNum = _PduPwrMonitoringInletNum_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 1),
    _PduPwrMonitoringInletNum_Type()
)
pduPwrMonitoringInletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringInletNum.setStatus("mandatory")
_PduPwrMonitoringInletStatusTable_Object = MibTable
pduPwrMonitoringInletStatusTable = _PduPwrMonitoringInletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletStatusTable.setStatus("mandatory")
_PduPwrMonitoringInletStatusEntry_Object = MibTableRow
pduPwrMonitoringInletStatusEntry = _PduPwrMonitoringInletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1)
)
pduPwrMonitoringInletStatusEntry.setIndexNames(
    (0, "PWTv1-MIB", "inletIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletStatusEntry.setStatus("mandatory")


class _InletIndex_Type(Integer32):
    """Custom type inletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InletIndex_Type.__name__ = "Integer32"
_InletIndex_Object = MibTableColumn
inletIndex = _InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 1),
    _InletIndex_Type()
)
inletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletIndex.setStatus("mandatory")
_InletPowerAll_Type = Integer32
_InletPowerAll_Object = MibTableColumn
inletPowerAll = _InletPowerAll_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 2),
    _InletPowerAll_Type()
)
inletPowerAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerAll.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerAll.setUnits("0.1W")
_InletResetFrom_Type = DisplayString
_InletResetFrom_Object = MibTableColumn
inletResetFrom = _InletResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 3),
    _InletResetFrom_Type()
)
inletResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletResetFrom.setStatus("mandatory")
_InletEnergy_Type = Integer32
_InletEnergy_Object = MibTableColumn
inletEnergy = _InletEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 4),
    _InletEnergy_Type()
)
inletEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletEnergy.setUnits("KWh")


class _InletStatus_Type(Integer32):
    """Custom type inletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatus_Type.__name__ = "Integer32"
_InletStatus_Object = MibTableColumn
inletStatus = _InletStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 5),
    _InletStatus_Type()
)
inletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatus.setStatus("mandatory")
_InletCurrPhase1b1_Type = Integer32
_InletCurrPhase1b1_Object = MibTableColumn
inletCurrPhase1b1 = _InletCurrPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 6),
    _InletCurrPhase1b1_Type()
)
inletCurrPhase1b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase1b1.setUnits("0.01A")
_InletCurrPhase2b1_Type = Integer32
_InletCurrPhase2b1_Object = MibTableColumn
inletCurrPhase2b1 = _InletCurrPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 7),
    _InletCurrPhase2b1_Type()
)
inletCurrPhase2b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase2b1.setUnits("0.01A")
_InletCurrPhase3b1_Type = Integer32
_InletCurrPhase3b1_Object = MibTableColumn
inletCurrPhase3b1 = _InletCurrPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 8),
    _InletCurrPhase3b1_Type()
)
inletCurrPhase3b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase3b1.setUnits("0.01A")
_InletCurrPhase1b2_Type = Integer32
_InletCurrPhase1b2_Object = MibTableColumn
inletCurrPhase1b2 = _InletCurrPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 9),
    _InletCurrPhase1b2_Type()
)
inletCurrPhase1b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase1b2.setUnits("0.01A")
_InletCurrPhase2b2_Type = Integer32
_InletCurrPhase2b2_Object = MibTableColumn
inletCurrPhase2b2 = _InletCurrPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 10),
    _InletCurrPhase2b2_Type()
)
inletCurrPhase2b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase2b2.setUnits("0.01A")
_InletCurrPhase3b2_Type = Integer32
_InletCurrPhase3b2_Object = MibTableColumn
inletCurrPhase3b2 = _InletCurrPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 11),
    _InletCurrPhase3b2_Type()
)
inletCurrPhase3b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase3b2.setUnits("0.01A")
_InletCurrPhase1_Type = Integer32
_InletCurrPhase1_Object = MibTableColumn
inletCurrPhase1 = _InletCurrPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 12),
    _InletCurrPhase1_Type()
)
inletCurrPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase1.setUnits("0.01A")
_InletCurrPhase2_Type = Integer32
_InletCurrPhase2_Object = MibTableColumn
inletCurrPhase2 = _InletCurrPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 13),
    _InletCurrPhase2_Type()
)
inletCurrPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase2.setUnits("0.01A")
_InletCurrPhase3_Type = Integer32
_InletCurrPhase3_Object = MibTableColumn
inletCurrPhase3 = _InletCurrPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 14),
    _InletCurrPhase3_Type()
)
inletCurrPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase3.setUnits("0.01A")
_InletVoltPhase1_Type = Integer32
_InletVoltPhase1_Object = MibTableColumn
inletVoltPhase1 = _InletVoltPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 15),
    _InletVoltPhase1_Type()
)
inletVoltPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVoltPhase1.setUnits("0.1V")
_InletVoltPhase2_Type = Integer32
_InletVoltPhase2_Object = MibTableColumn
inletVoltPhase2 = _InletVoltPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 16),
    _InletVoltPhase2_Type()
)
inletVoltPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVoltPhase2.setUnits("0.1V")
_InletVoltPhase3_Type = Integer32
_InletVoltPhase3_Object = MibTableColumn
inletVoltPhase3 = _InletVoltPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 17),
    _InletVoltPhase3_Type()
)
inletVoltPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVoltPhase3.setUnits("0.1V")
_InletPwrFactorPhase1b1_Type = Integer32
_InletPwrFactorPhase1b1_Object = MibTableColumn
inletPwrFactorPhase1b1 = _InletPwrFactorPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 18),
    _InletPwrFactorPhase1b1_Type()
)
inletPwrFactorPhase1b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase1b1.setUnits("0.1%")
_InletPwrFactorPhase2b1_Type = Integer32
_InletPwrFactorPhase2b1_Object = MibTableColumn
inletPwrFactorPhase2b1 = _InletPwrFactorPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 19),
    _InletPwrFactorPhase2b1_Type()
)
inletPwrFactorPhase2b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase2b1.setUnits("0.1%")
_InletPwrFactorPhase3b1_Type = Integer32
_InletPwrFactorPhase3b1_Object = MibTableColumn
inletPwrFactorPhase3b1 = _InletPwrFactorPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 20),
    _InletPwrFactorPhase3b1_Type()
)
inletPwrFactorPhase3b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase3b1.setUnits("0.1%")
_InletPwrFactorPhase1b2_Type = Integer32
_InletPwrFactorPhase1b2_Object = MibTableColumn
inletPwrFactorPhase1b2 = _InletPwrFactorPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 21),
    _InletPwrFactorPhase1b2_Type()
)
inletPwrFactorPhase1b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase1b2.setUnits("0.1%")
_InletPwrFactorPhase2b2_Type = Integer32
_InletPwrFactorPhase2b2_Object = MibTableColumn
inletPwrFactorPhase2b2 = _InletPwrFactorPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 22),
    _InletPwrFactorPhase2b2_Type()
)
inletPwrFactorPhase2b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase2b2.setUnits("0.1%")
_InletPwrFactorPhase3b2_Type = Integer32
_InletPwrFactorPhase3b2_Object = MibTableColumn
inletPwrFactorPhase3b2 = _InletPwrFactorPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 23),
    _InletPwrFactorPhase3b2_Type()
)
inletPwrFactorPhase3b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase3b2.setUnits("0.1%")
_InletPowerPhase1b1_Type = Integer32
_InletPowerPhase1b1_Object = MibTableColumn
inletPowerPhase1b1 = _InletPowerPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 24),
    _InletPowerPhase1b1_Type()
)
inletPowerPhase1b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase1b1.setUnits("0.1W")
_InletPowerPhase2b1_Type = Integer32
_InletPowerPhase2b1_Object = MibTableColumn
inletPowerPhase2b1 = _InletPowerPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 25),
    _InletPowerPhase2b1_Type()
)
inletPowerPhase2b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase2b1.setUnits("0.1W")
_InletPowerPhase3b1_Type = Integer32
_InletPowerPhase3b1_Object = MibTableColumn
inletPowerPhase3b1 = _InletPowerPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 26),
    _InletPowerPhase3b1_Type()
)
inletPowerPhase3b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase3b1.setUnits("0.1W")
_InletPowerPhase1b2_Type = Integer32
_InletPowerPhase1b2_Object = MibTableColumn
inletPowerPhase1b2 = _InletPowerPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 27),
    _InletPowerPhase1b2_Type()
)
inletPowerPhase1b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase1b2.setUnits("0.1W")
_InletPowerPhase2b2_Type = Integer32
_InletPowerPhase2b2_Object = MibTableColumn
inletPowerPhase2b2 = _InletPowerPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 28),
    _InletPowerPhase2b2_Type()
)
inletPowerPhase2b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase2b2.setUnits("0.1W")
_InletPowerPhase3b2_Type = Integer32
_InletPowerPhase3b2_Object = MibTableColumn
inletPowerPhase3b2 = _InletPowerPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 29),
    _InletPowerPhase3b2_Type()
)
inletPowerPhase3b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase3b2.setUnits("0.1W")
_InletPowerPhase1_Type = Integer32
_InletPowerPhase1_Object = MibTableColumn
inletPowerPhase1 = _InletPowerPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 30),
    _InletPowerPhase1_Type()
)
inletPowerPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase1.setUnits("0.1W")
_InletPowerPhase2_Type = Integer32
_InletPowerPhase2_Object = MibTableColumn
inletPowerPhase2 = _InletPowerPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 31),
    _InletPowerPhase2_Type()
)
inletPowerPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase2.setUnits("0.1W")
_InletPowerPhase3_Type = Integer32
_InletPowerPhase3_Object = MibTableColumn
inletPowerPhase3 = _InletPowerPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 32),
    _InletPowerPhase3_Type()
)
inletPowerPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase3.setUnits("0.1W")


class _InletStatusPhase1_Type(Integer32):
    """Custom type inletStatusPhase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatusPhase1_Type.__name__ = "Integer32"
_InletStatusPhase1_Object = MibTableColumn
inletStatusPhase1 = _InletStatusPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 33),
    _InletStatusPhase1_Type()
)
inletStatusPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusPhase1.setStatus("mandatory")


class _InletStatusPhase2_Type(Integer32):
    """Custom type inletStatusPhase2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatusPhase2_Type.__name__ = "Integer32"
_InletStatusPhase2_Object = MibTableColumn
inletStatusPhase2 = _InletStatusPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 34),
    _InletStatusPhase2_Type()
)
inletStatusPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusPhase2.setStatus("mandatory")


class _InletStatusPhase3_Type(Integer32):
    """Custom type inletStatusPhase3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatusPhase3_Type.__name__ = "Integer32"
_InletStatusPhase3_Object = MibTableColumn
inletStatusPhase3 = _InletStatusPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 35),
    _InletStatusPhase3_Type()
)
inletStatusPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusPhase3.setStatus("mandatory")
_InletAppPowerPhase1b1_Type = Integer32
_InletAppPowerPhase1b1_Object = MibTableColumn
inletAppPowerPhase1b1 = _InletAppPowerPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 36),
    _InletAppPowerPhase1b1_Type()
)
inletAppPowerPhase1b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase1b1.setUnits("0.1W")
_InletAppPowerPhase2b1_Type = Integer32
_InletAppPowerPhase2b1_Object = MibTableColumn
inletAppPowerPhase2b1 = _InletAppPowerPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 37),
    _InletAppPowerPhase2b1_Type()
)
inletAppPowerPhase2b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase2b1.setUnits("0.1W")
_InletAppPowerPhase3b1_Type = Integer32
_InletAppPowerPhase3b1_Object = MibTableColumn
inletAppPowerPhase3b1 = _InletAppPowerPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 38),
    _InletAppPowerPhase3b1_Type()
)
inletAppPowerPhase3b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase3b1.setUnits("0.1W")
_InletAppPowerPhase1b2_Type = Integer32
_InletAppPowerPhase1b2_Object = MibTableColumn
inletAppPowerPhase1b2 = _InletAppPowerPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 39),
    _InletAppPowerPhase1b2_Type()
)
inletAppPowerPhase1b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase1b2.setUnits("0.1W")
_InletAppPowerPhase2b2_Type = Integer32
_InletAppPowerPhase2b2_Object = MibTableColumn
inletAppPowerPhase2b2 = _InletAppPowerPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 40),
    _InletAppPowerPhase2b2_Type()
)
inletAppPowerPhase2b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase2b2.setUnits("0.1W")
_InletAppPowerPhase3b2_Type = Integer32
_InletAppPowerPhase3b2_Object = MibTableColumn
inletAppPowerPhase3b2 = _InletAppPowerPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 41),
    _InletAppPowerPhase3b2_Type()
)
inletAppPowerPhase3b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase3b2.setUnits("0.1W")
_InletAppPowerPhase1_Type = Integer32
_InletAppPowerPhase1_Object = MibTableColumn
inletAppPowerPhase1 = _InletAppPowerPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 42),
    _InletAppPowerPhase1_Type()
)
inletAppPowerPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase1.setUnits("0.1W")
_InletAppPowerPhase2_Type = Integer32
_InletAppPowerPhase2_Object = MibTableColumn
inletAppPowerPhase2 = _InletAppPowerPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 43),
    _InletAppPowerPhase2_Type()
)
inletAppPowerPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase2.setUnits("0.1W")
_InletAppPowerPhase3_Type = Integer32
_InletAppPowerPhase3_Object = MibTableColumn
inletAppPowerPhase3 = _InletAppPowerPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 44),
    _InletAppPowerPhase3_Type()
)
inletAppPowerPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppPowerPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppPowerPhase3.setUnits("0.1W")
_InletAppRcmCurrent_Type = Integer32
_InletAppRcmCurrent_Object = MibTableColumn
inletAppRcmCurrent = _InletAppRcmCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 45),
    _InletAppRcmCurrent_Type()
)
inletAppRcmCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletAppRcmCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletAppRcmCurrent.setUnits("0.1mA")
_InletLoadBalance_Type = Integer32
_InletLoadBalance_Object = MibTableColumn
inletLoadBalance = _InletLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 46),
    _InletLoadBalance_Type()
)
inletLoadBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLoadBalance.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletLoadBalance.setUnits("1%")


class _InletLoadBalanceStatus_Type(Integer32):
    """Custom type inletLoadBalanceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletLoadBalanceStatus_Type.__name__ = "Integer32"
_InletLoadBalanceStatus_Object = MibTableColumn
inletLoadBalanceStatus = _InletLoadBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 47),
    _InletLoadBalanceStatus_Type()
)
inletLoadBalanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLoadBalanceStatus.setStatus("mandatory")
_InletResetFromPhase1_Type = DisplayString
_InletResetFromPhase1_Object = MibTableColumn
inletResetFromPhase1 = _InletResetFromPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 48),
    _InletResetFromPhase1_Type()
)
inletResetFromPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletResetFromPhase1.setStatus("mandatory")
_InletEnergyPhase1_Type = Integer32
_InletEnergyPhase1_Object = MibTableColumn
inletEnergyPhase1 = _InletEnergyPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 49),
    _InletEnergyPhase1_Type()
)
inletEnergyPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletEnergyPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletEnergyPhase1.setUnits("KWh")
_InletResetFromPhase2_Type = DisplayString
_InletResetFromPhase2_Object = MibTableColumn
inletResetFromPhase2 = _InletResetFromPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 50),
    _InletResetFromPhase2_Type()
)
inletResetFromPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletResetFromPhase2.setStatus("mandatory")
_InletEnergyPhase2_Type = Integer32
_InletEnergyPhase2_Object = MibTableColumn
inletEnergyPhase2 = _InletEnergyPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 51),
    _InletEnergyPhase2_Type()
)
inletEnergyPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletEnergyPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletEnergyPhase2.setUnits("KWh")
_InletResetFromPhase3_Type = DisplayString
_InletResetFromPhase3_Object = MibTableColumn
inletResetFromPhase3 = _InletResetFromPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 52),
    _InletResetFromPhase3_Type()
)
inletResetFromPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletResetFromPhase3.setStatus("mandatory")
_InletEnergyPhase3_Type = Integer32
_InletEnergyPhase3_Object = MibTableColumn
inletEnergyPhase3 = _InletEnergyPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 53),
    _InletEnergyPhase3_Type()
)
inletEnergyPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletEnergyPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletEnergyPhase3.setUnits("KWh")
_InletFreqPhase1_Type = Integer32
_InletFreqPhase1_Object = MibTableColumn
inletFreqPhase1 = _InletFreqPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 54),
    _InletFreqPhase1_Type()
)
inletFreqPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletFreqPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletFreqPhase1.setUnits("0.01HZ")
_InletFreqPhase2_Type = Integer32
_InletFreqPhase2_Object = MibTableColumn
inletFreqPhase2 = _InletFreqPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 55),
    _InletFreqPhase2_Type()
)
inletFreqPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletFreqPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletFreqPhase2.setUnits("0.01HZ")
_InletFreqPhase3_Type = Integer32
_InletFreqPhase3_Object = MibTableColumn
inletFreqPhase3 = _InletFreqPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 56),
    _InletFreqPhase3_Type()
)
inletFreqPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletFreqPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletFreqPhase3.setUnits("0.01HZ")
_InletReactiveResetFrom_Type = DisplayString
_InletReactiveResetFrom_Object = MibTableColumn
inletReactiveResetFrom = _InletReactiveResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 57),
    _InletReactiveResetFrom_Type()
)
inletReactiveResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveResetFrom.setStatus("mandatory")
_InletReactiveEnergy_Type = Integer32
_InletReactiveEnergy_Object = MibTableColumn
inletReactiveEnergy = _InletReactiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 58),
    _InletReactiveEnergy_Type()
)
inletReactiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletReactiveEnergy.setUnits("KWh")
_InletReactiveResetFromPhase1_Type = DisplayString
_InletReactiveResetFromPhase1_Object = MibTableColumn
inletReactiveResetFromPhase1 = _InletReactiveResetFromPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 59),
    _InletReactiveResetFromPhase1_Type()
)
inletReactiveResetFromPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveResetFromPhase1.setStatus("mandatory")
_InletReactiveEnergyPhase1_Type = Integer32
_InletReactiveEnergyPhase1_Object = MibTableColumn
inletReactiveEnergyPhase1 = _InletReactiveEnergyPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 60),
    _InletReactiveEnergyPhase1_Type()
)
inletReactiveEnergyPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveEnergyPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletReactiveEnergyPhase1.setUnits("KWh")
_InletReactiveResetFromPhase2_Type = DisplayString
_InletReactiveResetFromPhase2_Object = MibTableColumn
inletReactiveResetFromPhase2 = _InletReactiveResetFromPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 61),
    _InletReactiveResetFromPhase2_Type()
)
inletReactiveResetFromPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveResetFromPhase2.setStatus("mandatory")
_InletReactiveEnergyPhase2_Type = Integer32
_InletReactiveEnergyPhase2_Object = MibTableColumn
inletReactiveEnergyPhase2 = _InletReactiveEnergyPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 62),
    _InletReactiveEnergyPhase2_Type()
)
inletReactiveEnergyPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveEnergyPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletReactiveEnergyPhase2.setUnits("KWh")
_InletReactiveResetFromPhase3_Type = DisplayString
_InletReactiveResetFromPhase3_Object = MibTableColumn
inletReactiveResetFromPhase3 = _InletReactiveResetFromPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 63),
    _InletReactiveResetFromPhase3_Type()
)
inletReactiveResetFromPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveResetFromPhase3.setStatus("mandatory")
_InletReactiveEnergyPhase3_Type = Integer32
_InletReactiveEnergyPhase3_Object = MibTableColumn
inletReactiveEnergyPhase3 = _InletReactiveEnergyPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 64),
    _InletReactiveEnergyPhase3_Type()
)
inletReactiveEnergyPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletReactiveEnergyPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletReactiveEnergyPhase3.setUnits("KWh")
_InletVarPowerPhase1b1_Type = Integer32
_InletVarPowerPhase1b1_Object = MibTableColumn
inletVarPowerPhase1b1 = _InletVarPowerPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 65),
    _InletVarPowerPhase1b1_Type()
)
inletVarPowerPhase1b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase1b1.setUnits("0.1W")
_InletVarPowerPhase2b1_Type = Integer32
_InletVarPowerPhase2b1_Object = MibTableColumn
inletVarPowerPhase2b1 = _InletVarPowerPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 66),
    _InletVarPowerPhase2b1_Type()
)
inletVarPowerPhase2b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase2b1.setUnits("0.1W")
_InletVarPowerPhase3b1_Type = Integer32
_InletVarPowerPhase3b1_Object = MibTableColumn
inletVarPowerPhase3b1 = _InletVarPowerPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 67),
    _InletVarPowerPhase3b1_Type()
)
inletVarPowerPhase3b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase3b1.setUnits("0.1W")
_InletVarPowerPhase1b2_Type = Integer32
_InletVarPowerPhase1b2_Object = MibTableColumn
inletVarPowerPhase1b2 = _InletVarPowerPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 68),
    _InletVarPowerPhase1b2_Type()
)
inletVarPowerPhase1b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase1b2.setUnits("0.1W")
_InletVarPowerPhase2b2_Type = Integer32
_InletVarPowerPhase2b2_Object = MibTableColumn
inletVarPowerPhase2b2 = _InletVarPowerPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 69),
    _InletVarPowerPhase2b2_Type()
)
inletVarPowerPhase2b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase2b2.setUnits("0.1W")
_InletVarPowerPhase3b2_Type = Integer32
_InletVarPowerPhase3b2_Object = MibTableColumn
inletVarPowerPhase3b2 = _InletVarPowerPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 70),
    _InletVarPowerPhase3b2_Type()
)
inletVarPowerPhase3b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase3b2.setUnits("0.1W")
_InletVarPowerPhase1_Type = Integer32
_InletVarPowerPhase1_Object = MibTableColumn
inletVarPowerPhase1 = _InletVarPowerPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 71),
    _InletVarPowerPhase1_Type()
)
inletVarPowerPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase1.setUnits("0.1W")
_InletVarPowerPhase2_Type = Integer32
_InletVarPowerPhase2_Object = MibTableColumn
inletVarPowerPhase2 = _InletVarPowerPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 72),
    _InletVarPowerPhase2_Type()
)
inletVarPowerPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase2.setUnits("0.1W")
_InletVarPowerPhase3_Type = Integer32
_InletVarPowerPhase3_Object = MibTableColumn
inletVarPowerPhase3 = _InletVarPowerPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 73),
    _InletVarPowerPhase3_Type()
)
inletVarPowerPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVarPowerPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVarPowerPhase3.setUnits("0.1W")
_PduPwrMonitoringInletCfgTable_Object = MibTable
pduPwrMonitoringInletCfgTable = _PduPwrMonitoringInletCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletCfgTable.setStatus("mandatory")
_PduPwrMonitoringInletCfgEntry_Object = MibTableRow
pduPwrMonitoringInletCfgEntry = _PduPwrMonitoringInletCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1)
)
pduPwrMonitoringInletCfgEntry.setIndexNames(
    (0, "PWTv1-MIB", "inletCfgIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletCfgEntry.setStatus("mandatory")


class _InletCfgIndex_Type(Integer32):
    """Custom type inletCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InletCfgIndex_Type.__name__ = "Integer32"
_InletCfgIndex_Object = MibTableColumn
inletCfgIndex = _InletCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 1),
    _InletCfgIndex_Type()
)
inletCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCfgIndex.setStatus("mandatory")
_InletCfgLoadCritical_Type = Integer32
_InletCfgLoadCritical_Object = MibTableColumn
inletCfgLoadCritical = _InletCfgLoadCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 2),
    _InletCfgLoadCritical_Type()
)
inletCfgLoadCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgLoadCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgLoadCritical.setUnits("0.1kW")
_InletCfgLoadWarning_Type = Integer32
_InletCfgLoadWarning_Object = MibTableColumn
inletCfgLoadWarning = _InletCfgLoadWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 3),
    _InletCfgLoadWarning_Type()
)
inletCfgLoadWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgLoadWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgLoadWarning.setUnits("0.1kW")
_InletCfgCurrCritPhase1b1_Type = Integer32
_InletCfgCurrCritPhase1b1_Object = MibTableColumn
inletCfgCurrCritPhase1b1 = _InletCfgCurrCritPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 4),
    _InletCfgCurrCritPhase1b1_Type()
)
inletCfgCurrCritPhase1b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase1b1.setUnits("0.1A")
_InletCfgCurrCritPhase2b1_Type = Integer32
_InletCfgCurrCritPhase2b1_Object = MibTableColumn
inletCfgCurrCritPhase2b1 = _InletCfgCurrCritPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 5),
    _InletCfgCurrCritPhase2b1_Type()
)
inletCfgCurrCritPhase2b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase2b1.setUnits("0.1A")
_InletCfgCurrCritPhase3b1_Type = Integer32
_InletCfgCurrCritPhase3b1_Object = MibTableColumn
inletCfgCurrCritPhase3b1 = _InletCfgCurrCritPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 6),
    _InletCfgCurrCritPhase3b1_Type()
)
inletCfgCurrCritPhase3b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase3b1.setUnits("0.1A")
_InletCfgCurrCritPhase1b2_Type = Integer32
_InletCfgCurrCritPhase1b2_Object = MibTableColumn
inletCfgCurrCritPhase1b2 = _InletCfgCurrCritPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 7),
    _InletCfgCurrCritPhase1b2_Type()
)
inletCfgCurrCritPhase1b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase1b2.setUnits("0.1A")
_InletCfgCurrCritPhase2b2_Type = Integer32
_InletCfgCurrCritPhase2b2_Object = MibTableColumn
inletCfgCurrCritPhase2b2 = _InletCfgCurrCritPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 8),
    _InletCfgCurrCritPhase2b2_Type()
)
inletCfgCurrCritPhase2b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase2b2.setUnits("0.1A")
_InletCfgCurrCritPhase3b2_Type = Integer32
_InletCfgCurrCritPhase3b2_Object = MibTableColumn
inletCfgCurrCritPhase3b2 = _InletCfgCurrCritPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 9),
    _InletCfgCurrCritPhase3b2_Type()
)
inletCfgCurrCritPhase3b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase3b2.setUnits("0.1A")
_InletCfgCurrWarnPhase1b1_Type = Integer32
_InletCfgCurrWarnPhase1b1_Object = MibTableColumn
inletCfgCurrWarnPhase1b1 = _InletCfgCurrWarnPhase1b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 10),
    _InletCfgCurrWarnPhase1b1_Type()
)
inletCfgCurrWarnPhase1b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase1b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase1b1.setUnits("0.1A")
_InletCfgCurrWarnPhase2b1_Type = Integer32
_InletCfgCurrWarnPhase2b1_Object = MibTableColumn
inletCfgCurrWarnPhase2b1 = _InletCfgCurrWarnPhase2b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 11),
    _InletCfgCurrWarnPhase2b1_Type()
)
inletCfgCurrWarnPhase2b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase2b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase2b1.setUnits("0.1A")
_InletCfgCurrWarnPhase3b1_Type = Integer32
_InletCfgCurrWarnPhase3b1_Object = MibTableColumn
inletCfgCurrWarnPhase3b1 = _InletCfgCurrWarnPhase3b1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 12),
    _InletCfgCurrWarnPhase3b1_Type()
)
inletCfgCurrWarnPhase3b1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase3b1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase3b1.setUnits("0.1A")
_InletCfgCurrWarnPhase1b2_Type = Integer32
_InletCfgCurrWarnPhase1b2_Object = MibTableColumn
inletCfgCurrWarnPhase1b2 = _InletCfgCurrWarnPhase1b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 13),
    _InletCfgCurrWarnPhase1b2_Type()
)
inletCfgCurrWarnPhase1b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase1b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase1b2.setUnits("0.1A")
_InletCfgCurrWarnPhase2b2_Type = Integer32
_InletCfgCurrWarnPhase2b2_Object = MibTableColumn
inletCfgCurrWarnPhase2b2 = _InletCfgCurrWarnPhase2b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 14),
    _InletCfgCurrWarnPhase2b2_Type()
)
inletCfgCurrWarnPhase2b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase2b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase2b2.setUnits("0.1A")
_InletCfgCurrWarnPhase3b2_Type = Integer32
_InletCfgCurrWarnPhase3b2_Object = MibTableColumn
inletCfgCurrWarnPhase3b2 = _InletCfgCurrWarnPhase3b2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 15),
    _InletCfgCurrWarnPhase3b2_Type()
)
inletCfgCurrWarnPhase3b2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase3b2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase3b2.setUnits("0.1A")
_InletCfgVoltCritPhase1_Type = Integer32
_InletCfgVoltCritPhase1_Object = MibTableColumn
inletCfgVoltCritPhase1 = _InletCfgVoltCritPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 16),
    _InletCfgVoltCritPhase1_Type()
)
inletCfgVoltCritPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase1.setUnits("0.1V")
_InletCfgVoltCritPhase2_Type = Integer32
_InletCfgVoltCritPhase2_Object = MibTableColumn
inletCfgVoltCritPhase2 = _InletCfgVoltCritPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 17),
    _InletCfgVoltCritPhase2_Type()
)
inletCfgVoltCritPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase2.setUnits("0.1V")
_InletCfgVoltCritPhase3_Type = Integer32
_InletCfgVoltCritPhase3_Object = MibTableColumn
inletCfgVoltCritPhase3 = _InletCfgVoltCritPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 18),
    _InletCfgVoltCritPhase3_Type()
)
inletCfgVoltCritPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase3.setUnits("0.1V")
_InletCfgVoltWarnPhase1_Type = Integer32
_InletCfgVoltWarnPhase1_Object = MibTableColumn
inletCfgVoltWarnPhase1 = _InletCfgVoltWarnPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 19),
    _InletCfgVoltWarnPhase1_Type()
)
inletCfgVoltWarnPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase1.setUnits("0.1V")
_InletCfgVoltWarnPhase2_Type = Integer32
_InletCfgVoltWarnPhase2_Object = MibTableColumn
inletCfgVoltWarnPhase2 = _InletCfgVoltWarnPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 20),
    _InletCfgVoltWarnPhase2_Type()
)
inletCfgVoltWarnPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase2.setUnits("0.1V")
_InletCfgVoltWarnPhase3_Type = Integer32
_InletCfgVoltWarnPhase3_Object = MibTableColumn
inletCfgVoltWarnPhase3 = _InletCfgVoltWarnPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 21),
    _InletCfgVoltWarnPhase3_Type()
)
inletCfgVoltWarnPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase3.setUnits("0.1V")
_InletCfgTotalCurrCritPhase1_Type = Integer32
_InletCfgTotalCurrCritPhase1_Object = MibTableColumn
inletCfgTotalCurrCritPhase1 = _InletCfgTotalCurrCritPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 22),
    _InletCfgTotalCurrCritPhase1_Type()
)
inletCfgTotalCurrCritPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgTotalCurrCritPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgTotalCurrCritPhase1.setUnits("0.1A")
_InletCfgTotalCurrCritPhase2_Type = Integer32
_InletCfgTotalCurrCritPhase2_Object = MibTableColumn
inletCfgTotalCurrCritPhase2 = _InletCfgTotalCurrCritPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 23),
    _InletCfgTotalCurrCritPhase2_Type()
)
inletCfgTotalCurrCritPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgTotalCurrCritPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgTotalCurrCritPhase2.setUnits("0.1A")
_InletCfgTotalCurrCritPhase3_Type = Integer32
_InletCfgTotalCurrCritPhase3_Object = MibTableColumn
inletCfgTotalCurrCritPhase3 = _InletCfgTotalCurrCritPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 24),
    _InletCfgTotalCurrCritPhase3_Type()
)
inletCfgTotalCurrCritPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgTotalCurrCritPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgTotalCurrCritPhase3.setUnits("0.1A")
_InletCfgTotalCurrWarnPhase1_Type = Integer32
_InletCfgTotalCurrWarnPhase1_Object = MibTableColumn
inletCfgTotalCurrWarnPhase1 = _InletCfgTotalCurrWarnPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 25),
    _InletCfgTotalCurrWarnPhase1_Type()
)
inletCfgTotalCurrWarnPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgTotalCurrWarnPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgTotalCurrWarnPhase1.setUnits("0.1A")
_InletCfgTotalCurrWarnPhase2_Type = Integer32
_InletCfgTotalCurrWarnPhase2_Object = MibTableColumn
inletCfgTotalCurrWarnPhase2 = _InletCfgTotalCurrWarnPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 26),
    _InletCfgTotalCurrWarnPhase2_Type()
)
inletCfgTotalCurrWarnPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgTotalCurrWarnPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgTotalCurrWarnPhase2.setUnits("0.1A")
_InletCfgTotalCurrWarnPhase3_Type = Integer32
_InletCfgTotalCurrWarnPhase3_Object = MibTableColumn
inletCfgTotalCurrWarnPhase3 = _InletCfgTotalCurrWarnPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 27),
    _InletCfgTotalCurrWarnPhase3_Type()
)
inletCfgTotalCurrWarnPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgTotalCurrWarnPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgTotalCurrWarnPhase3.setUnits("0.1A")
_InletCfgRcmCurrThreshold_Type = Integer32
_InletCfgRcmCurrThreshold_Object = MibTableColumn
inletCfgRcmCurrThreshold = _InletCfgRcmCurrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 28),
    _InletCfgRcmCurrThreshold_Type()
)
inletCfgRcmCurrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgRcmCurrThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgRcmCurrThreshold.setUnits("1mA")
_InletCfgLoadBalanceCrit_Type = Integer32
_InletCfgLoadBalanceCrit_Object = MibTableColumn
inletCfgLoadBalanceCrit = _InletCfgLoadBalanceCrit_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 29),
    _InletCfgLoadBalanceCrit_Type()
)
inletCfgLoadBalanceCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgLoadBalanceCrit.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgLoadBalanceCrit.setUnits("1%")
_InletCfgLoadBalanceWarn_Type = Integer32
_InletCfgLoadBalanceWarn_Object = MibTableColumn
inletCfgLoadBalanceWarn = _InletCfgLoadBalanceWarn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 30),
    _InletCfgLoadBalanceWarn_Type()
)
inletCfgLoadBalanceWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgLoadBalanceWarn.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgLoadBalanceWarn.setUnits("1%")
_PduPwrMonitoringOutlet_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutlet = _PduPwrMonitoringOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2)
)
_PduPwrMonitoringOutletPduA_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduA = _PduPwrMonitoringOutletPduA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1)
)
_PduPwrMonitoringOutletNumPduA_Type = Integer32
_PduPwrMonitoringOutletNumPduA_Object = MibScalar
pduPwrMonitoringOutletNumPduA = _PduPwrMonitoringOutletNumPduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 1),
    _PduPwrMonitoringOutletNumPduA_Type()
)
pduPwrMonitoringOutletNumPduA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduA.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduA_Object = MibTable
pduPwrMonitoringOutletStatusTablePduA = _PduPwrMonitoringOutletStatusTablePduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduA.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduAEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduAEntry = _PduPwrMonitoringOutletStatusPduAEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1)
)
pduPwrMonitoringOutletStatusPduAEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduAIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduAEntry.setStatus("mandatory")


class _OutletPduAIndex_Type(Integer32):
    """Custom type outletPduAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduAIndex_Type.__name__ = "Integer32"
_OutletPduAIndex_Object = MibTableColumn
outletPduAIndex = _OutletPduAIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 1),
    _OutletPduAIndex_Type()
)
outletPduAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAIndex.setStatus("mandatory")


class _OutletPduAState_Type(Integer32):
    """Custom type outletPduAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduAState_Type.__name__ = "Integer32"
_OutletPduAState_Object = MibTableColumn
outletPduAState = _OutletPduAState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 2),
    _OutletPduAState_Type()
)
outletPduAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAState.setStatus("mandatory")
_OutletPduACurrent_Type = Integer32
_OutletPduACurrent_Object = MibTableColumn
outletPduACurrent = _OutletPduACurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 3),
    _OutletPduACurrent_Type()
)
outletPduACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduACurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduACurrent.setUnits("0.01A")
_OutletPduAPwrFactor_Type = Integer32
_OutletPduAPwrFactor_Object = MibTableColumn
outletPduAPwrFactor = _OutletPduAPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 4),
    _OutletPduAPwrFactor_Type()
)
outletPduAPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAPwrFactor.setUnits("0.1%")
_OutletPduAPower_Type = Integer32
_OutletPduAPower_Object = MibTableColumn
outletPduAPower = _OutletPduAPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 5),
    _OutletPduAPower_Type()
)
outletPduAPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAPower.setUnits("0.1W")
_OutletPduAEnergy_Type = Integer32
_OutletPduAEnergy_Object = MibTableColumn
outletPduAEnergy = _OutletPduAEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 6),
    _OutletPduAEnergy_Type()
)
outletPduAEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAEnergy.setUnits("KWh")
_OutletPduAResetFrom_Type = DisplayString
_OutletPduAResetFrom_Object = MibTableColumn
outletPduAResetFrom = _OutletPduAResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 7),
    _OutletPduAResetFrom_Type()
)
outletPduAResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAResetFrom.setStatus("mandatory")


class _OutletPduAStatus_Type(Integer32):
    """Custom type outletPduAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduAStatus_Type.__name__ = "Integer32"
_OutletPduAStatus_Object = MibTableColumn
outletPduAStatus = _OutletPduAStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 8),
    _OutletPduAStatus_Type()
)
outletPduAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAStatus.setStatus("mandatory")
_OutletPduAAppPower_Type = Integer32
_OutletPduAAppPower_Object = MibTableColumn
outletPduAAppPower = _OutletPduAAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 9),
    _OutletPduAAppPower_Type()
)
outletPduAAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAAppPower.setUnits("0.1W")
_OutletPduAVoltage_Type = Integer32
_OutletPduAVoltage_Object = MibTableColumn
outletPduAVoltage = _OutletPduAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 10),
    _OutletPduAVoltage_Type()
)
outletPduAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduA_Object = MibTable
pduPwrMonitoringOutletCfgTablePduA = _PduPwrMonitoringOutletCfgTablePduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduA.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduAEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduAEntry = _PduPwrMonitoringOutletCfgPduAEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1)
)
pduPwrMonitoringOutletCfgPduAEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduAIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduAEntry.setStatus("mandatory")


class _OutletCfgPduAIndex_Type(Integer32):
    """Custom type outletCfgPduAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduAIndex_Type.__name__ = "Integer32"
_OutletCfgPduAIndex_Object = MibTableColumn
outletCfgPduAIndex = _OutletCfgPduAIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 1),
    _OutletCfgPduAIndex_Type()
)
outletCfgPduAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduAIndex.setStatus("mandatory")
_OutletCfgPduAName_Type = DisplayString
_OutletCfgPduAName_Object = MibTableColumn
outletCfgPduAName = _OutletCfgPduAName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 2),
    _OutletCfgPduAName_Type()
)
outletCfgPduAName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAName.setStatus("mandatory")


class _OutletCfgPduADelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduADelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduADelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduADelayOnStatus_Object = MibTableColumn
outletCfgPduADelayOnStatus = _OutletCfgPduADelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 3),
    _OutletCfgPduADelayOnStatus_Type()
)
outletCfgPduADelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOnStatus.setStatus("mandatory")
_OutletCfgPduADelayOnTime_Type = Integer32
_OutletCfgPduADelayOnTime_Object = MibTableColumn
outletCfgPduADelayOnTime = _OutletCfgPduADelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 4),
    _OutletCfgPduADelayOnTime_Type()
)
outletCfgPduADelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduADelayOnTime.setUnits("seconds")


class _OutletCfgPduADelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduADelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduADelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduADelayOffStatus_Object = MibTableColumn
outletCfgPduADelayOffStatus = _OutletCfgPduADelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 5),
    _OutletCfgPduADelayOffStatus_Type()
)
outletCfgPduADelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOffStatus.setStatus("mandatory")
_OutletCfgPduADelayOffTime_Type = Integer32
_OutletCfgPduADelayOffTime_Object = MibTableColumn
outletCfgPduADelayOffTime = _OutletCfgPduADelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 6),
    _OutletCfgPduADelayOffTime_Type()
)
outletCfgPduADelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduADelayOffTime.setUnits("seconds")
_OutletCfgPduAReboot_Type = Integer32
_OutletCfgPduAReboot_Object = MibTableColumn
outletCfgPduAReboot = _OutletCfgPduAReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 7),
    _OutletCfgPduAReboot_Type()
)
outletCfgPduAReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAReboot.setUnits("seconds")
_OutletCfgPduAOverCurrCritical_Type = Integer32
_OutletCfgPduAOverCurrCritical_Object = MibTableColumn
outletCfgPduAOverCurrCritical = _OutletCfgPduAOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 8),
    _OutletCfgPduAOverCurrCritical_Type()
)
outletCfgPduAOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrCritical.setUnits("0.1A")
_OutletCfgPduAOverCurrWarning_Type = Integer32
_OutletCfgPduAOverCurrWarning_Object = MibTableColumn
outletCfgPduAOverCurrWarning = _OutletCfgPduAOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 9),
    _OutletCfgPduAOverCurrWarning_Type()
)
outletCfgPduAOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrWarning.setUnits("0.1A")
_OutletCfgPduAOverPwrCritical_Type = Integer32
_OutletCfgPduAOverPwrCritical_Object = MibTableColumn
outletCfgPduAOverPwrCritical = _OutletCfgPduAOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 10),
    _OutletCfgPduAOverPwrCritical_Type()
)
outletCfgPduAOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrCritical.setUnits("1W")
_OutletCfgPduAOverPwrWarning_Type = Integer32
_OutletCfgPduAOverPwrWarning_Object = MibTableColumn
outletCfgPduAOverPwrWarning = _OutletCfgPduAOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 11),
    _OutletCfgPduAOverPwrWarning_Type()
)
outletCfgPduAOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduA_Object = MibTable
pduPwrMonitoringOutletCtlTablePduA = _PduPwrMonitoringOutletCtlTablePduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduA.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduAEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduAEntry = _PduPwrMonitoringOutletCtlPduAEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4, 1)
)
pduPwrMonitoringOutletCtlPduAEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduAIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduAEntry.setStatus("mandatory")


class _OutletCtlPduAIndex_Type(Integer32):
    """Custom type outletCtlPduAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduAIndex_Type.__name__ = "Integer32"
_OutletCtlPduAIndex_Object = MibTableColumn
outletCtlPduAIndex = _OutletCtlPduAIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4, 1, 1),
    _OutletCtlPduAIndex_Type()
)
outletCtlPduAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduAIndex.setStatus("mandatory")


class _OutletCtlPduAControl_Type(Integer32):
    """Custom type outletCtlPduAControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduAControl_Type.__name__ = "Integer32"
_OutletCtlPduAControl_Object = MibTableColumn
outletCtlPduAControl = _OutletCtlPduAControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4, 1, 2),
    _OutletCtlPduAControl_Type()
)
outletCtlPduAControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduAControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduB_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduB = _PduPwrMonitoringOutletPduB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2)
)
_PduPwrMonitoringOutletNumPduB_Type = Integer32
_PduPwrMonitoringOutletNumPduB_Object = MibScalar
pduPwrMonitoringOutletNumPduB = _PduPwrMonitoringOutletNumPduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 1),
    _PduPwrMonitoringOutletNumPduB_Type()
)
pduPwrMonitoringOutletNumPduB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduB.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduB_Object = MibTable
pduPwrMonitoringOutletStatusTablePduB = _PduPwrMonitoringOutletStatusTablePduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduB.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduBEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduBEntry = _PduPwrMonitoringOutletStatusPduBEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1)
)
pduPwrMonitoringOutletStatusPduBEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduBIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduBEntry.setStatus("mandatory")


class _OutletPduBIndex_Type(Integer32):
    """Custom type outletPduBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduBIndex_Type.__name__ = "Integer32"
_OutletPduBIndex_Object = MibTableColumn
outletPduBIndex = _OutletPduBIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 1),
    _OutletPduBIndex_Type()
)
outletPduBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBIndex.setStatus("mandatory")


class _OutletPduBState_Type(Integer32):
    """Custom type outletPduBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduBState_Type.__name__ = "Integer32"
_OutletPduBState_Object = MibTableColumn
outletPduBState = _OutletPduBState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 2),
    _OutletPduBState_Type()
)
outletPduBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBState.setStatus("mandatory")
_OutletPduBCurrent_Type = Integer32
_OutletPduBCurrent_Object = MibTableColumn
outletPduBCurrent = _OutletPduBCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 3),
    _OutletPduBCurrent_Type()
)
outletPduBCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBCurrent.setUnits("0.01A")
_OutletPduBPwrFactor_Type = Integer32
_OutletPduBPwrFactor_Object = MibTableColumn
outletPduBPwrFactor = _OutletPduBPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 4),
    _OutletPduBPwrFactor_Type()
)
outletPduBPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBPwrFactor.setUnits("0.1%")
_OutletPduBPower_Type = Integer32
_OutletPduBPower_Object = MibTableColumn
outletPduBPower = _OutletPduBPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 5),
    _OutletPduBPower_Type()
)
outletPduBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBPower.setUnits("0.1W")
_OutletPduBEnergy_Type = Integer32
_OutletPduBEnergy_Object = MibTableColumn
outletPduBEnergy = _OutletPduBEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 6),
    _OutletPduBEnergy_Type()
)
outletPduBEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBEnergy.setUnits("KWh")
_OutletPduBResetFrom_Type = DisplayString
_OutletPduBResetFrom_Object = MibTableColumn
outletPduBResetFrom = _OutletPduBResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 7),
    _OutletPduBResetFrom_Type()
)
outletPduBResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBResetFrom.setStatus("mandatory")


class _OutletPduBStatus_Type(Integer32):
    """Custom type outletPduBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduBStatus_Type.__name__ = "Integer32"
_OutletPduBStatus_Object = MibTableColumn
outletPduBStatus = _OutletPduBStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 8),
    _OutletPduBStatus_Type()
)
outletPduBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBStatus.setStatus("mandatory")
_OutletPduBAppPower_Type = Integer32
_OutletPduBAppPower_Object = MibTableColumn
outletPduBAppPower = _OutletPduBAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 9),
    _OutletPduBAppPower_Type()
)
outletPduBAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBAppPower.setUnits("0.1W")
_OutletPduBVoltage_Type = Integer32
_OutletPduBVoltage_Object = MibTableColumn
outletPduBVoltage = _OutletPduBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 10),
    _OutletPduBVoltage_Type()
)
outletPduBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduB_Object = MibTable
pduPwrMonitoringOutletCfgTablePduB = _PduPwrMonitoringOutletCfgTablePduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduB.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduBEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduBEntry = _PduPwrMonitoringOutletCfgPduBEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1)
)
pduPwrMonitoringOutletCfgPduBEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduBIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduBEntry.setStatus("mandatory")


class _OutletCfgPduBIndex_Type(Integer32):
    """Custom type outletCfgPduBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduBIndex_Type.__name__ = "Integer32"
_OutletCfgPduBIndex_Object = MibTableColumn
outletCfgPduBIndex = _OutletCfgPduBIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 1),
    _OutletCfgPduBIndex_Type()
)
outletCfgPduBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduBIndex.setStatus("mandatory")
_OutletCfgPduBName_Type = DisplayString
_OutletCfgPduBName_Object = MibTableColumn
outletCfgPduBName = _OutletCfgPduBName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 2),
    _OutletCfgPduBName_Type()
)
outletCfgPduBName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBName.setStatus("mandatory")


class _OutletCfgPduBDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduBDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduBDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduBDelayOnStatus_Object = MibTableColumn
outletCfgPduBDelayOnStatus = _OutletCfgPduBDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 3),
    _OutletCfgPduBDelayOnStatus_Type()
)
outletCfgPduBDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOnStatus.setStatus("mandatory")
_OutletCfgPduBDelayOnTime_Type = Integer32
_OutletCfgPduBDelayOnTime_Object = MibTableColumn
outletCfgPduBDelayOnTime = _OutletCfgPduBDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 4),
    _OutletCfgPduBDelayOnTime_Type()
)
outletCfgPduBDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOnTime.setUnits("seconds")


class _OutletCfgPduBDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduBDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduBDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduBDelayOffStatus_Object = MibTableColumn
outletCfgPduBDelayOffStatus = _OutletCfgPduBDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 5),
    _OutletCfgPduBDelayOffStatus_Type()
)
outletCfgPduBDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOffStatus.setStatus("mandatory")
_OutletCfgPduBDelayOffTime_Type = Integer32
_OutletCfgPduBDelayOffTime_Object = MibTableColumn
outletCfgPduBDelayOffTime = _OutletCfgPduBDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 6),
    _OutletCfgPduBDelayOffTime_Type()
)
outletCfgPduBDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOffTime.setUnits("seconds")
_OutletCfgPduBReboot_Type = Integer32
_OutletCfgPduBReboot_Object = MibTableColumn
outletCfgPduBReboot = _OutletCfgPduBReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 7),
    _OutletCfgPduBReboot_Type()
)
outletCfgPduBReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBReboot.setUnits("seconds")
_OutletCfgPduBOverCurrCritical_Type = Integer32
_OutletCfgPduBOverCurrCritical_Object = MibTableColumn
outletCfgPduBOverCurrCritical = _OutletCfgPduBOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 8),
    _OutletCfgPduBOverCurrCritical_Type()
)
outletCfgPduBOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrCritical.setUnits("0.1A")
_OutletCfgPduBOverCurrWarning_Type = Integer32
_OutletCfgPduBOverCurrWarning_Object = MibTableColumn
outletCfgPduBOverCurrWarning = _OutletCfgPduBOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 9),
    _OutletCfgPduBOverCurrWarning_Type()
)
outletCfgPduBOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrWarning.setUnits("0.1A")
_OutletCfgPduBOverPwrCritical_Type = Integer32
_OutletCfgPduBOverPwrCritical_Object = MibTableColumn
outletCfgPduBOverPwrCritical = _OutletCfgPduBOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 10),
    _OutletCfgPduBOverPwrCritical_Type()
)
outletCfgPduBOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrCritical.setUnits("1W")
_OutletCfgPduBOverPwrWarning_Type = Integer32
_OutletCfgPduBOverPwrWarning_Object = MibTableColumn
outletCfgPduBOverPwrWarning = _OutletCfgPduBOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 11),
    _OutletCfgPduBOverPwrWarning_Type()
)
outletCfgPduBOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduB_Object = MibTable
pduPwrMonitoringOutletCtlTablePduB = _PduPwrMonitoringOutletCtlTablePduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduB.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduBEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduBEntry = _PduPwrMonitoringOutletCtlPduBEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4, 1)
)
pduPwrMonitoringOutletCtlPduBEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduBIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduBEntry.setStatus("mandatory")


class _OutletCtlPduBIndex_Type(Integer32):
    """Custom type outletCtlPduBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduBIndex_Type.__name__ = "Integer32"
_OutletCtlPduBIndex_Object = MibTableColumn
outletCtlPduBIndex = _OutletCtlPduBIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4, 1, 1),
    _OutletCtlPduBIndex_Type()
)
outletCtlPduBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduBIndex.setStatus("mandatory")


class _OutletCtlPduBControl_Type(Integer32):
    """Custom type outletCtlPduBControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduBControl_Type.__name__ = "Integer32"
_OutletCtlPduBControl_Object = MibTableColumn
outletCtlPduBControl = _OutletCtlPduBControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4, 1, 2),
    _OutletCtlPduBControl_Type()
)
outletCtlPduBControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduBControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduC_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduC = _PduPwrMonitoringOutletPduC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3)
)
_PduPwrMonitoringOutletNumPduC_Type = Integer32
_PduPwrMonitoringOutletNumPduC_Object = MibScalar
pduPwrMonitoringOutletNumPduC = _PduPwrMonitoringOutletNumPduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 1),
    _PduPwrMonitoringOutletNumPduC_Type()
)
pduPwrMonitoringOutletNumPduC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduC.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduC_Object = MibTable
pduPwrMonitoringOutletStatusTablePduC = _PduPwrMonitoringOutletStatusTablePduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduC.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduCEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduCEntry = _PduPwrMonitoringOutletStatusPduCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1)
)
pduPwrMonitoringOutletStatusPduCEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduCIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduCEntry.setStatus("mandatory")


class _OutletPduCIndex_Type(Integer32):
    """Custom type outletPduCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduCIndex_Type.__name__ = "Integer32"
_OutletPduCIndex_Object = MibTableColumn
outletPduCIndex = _OutletPduCIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 1),
    _OutletPduCIndex_Type()
)
outletPduCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCIndex.setStatus("mandatory")


class _OutletPduCState_Type(Integer32):
    """Custom type outletPduCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduCState_Type.__name__ = "Integer32"
_OutletPduCState_Object = MibTableColumn
outletPduCState = _OutletPduCState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 2),
    _OutletPduCState_Type()
)
outletPduCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCState.setStatus("mandatory")
_OutletPduCCurrent_Type = Integer32
_OutletPduCCurrent_Object = MibTableColumn
outletPduCCurrent = _OutletPduCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 3),
    _OutletPduCCurrent_Type()
)
outletPduCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCCurrent.setUnits("0.01A")
_OutletPduCPwrFactor_Type = Integer32
_OutletPduCPwrFactor_Object = MibTableColumn
outletPduCPwrFactor = _OutletPduCPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 4),
    _OutletPduCPwrFactor_Type()
)
outletPduCPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCPwrFactor.setUnits("0.1%")
_OutletPduCPower_Type = Integer32
_OutletPduCPower_Object = MibTableColumn
outletPduCPower = _OutletPduCPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 5),
    _OutletPduCPower_Type()
)
outletPduCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCPower.setUnits("0.1W")
_OutletPduCEnergy_Type = Integer32
_OutletPduCEnergy_Object = MibTableColumn
outletPduCEnergy = _OutletPduCEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 6),
    _OutletPduCEnergy_Type()
)
outletPduCEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCEnergy.setUnits("KWh")
_OutletPduCResetFrom_Type = DisplayString
_OutletPduCResetFrom_Object = MibTableColumn
outletPduCResetFrom = _OutletPduCResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 7),
    _OutletPduCResetFrom_Type()
)
outletPduCResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCResetFrom.setStatus("mandatory")


class _OutletPduCStatus_Type(Integer32):
    """Custom type outletPduCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduCStatus_Type.__name__ = "Integer32"
_OutletPduCStatus_Object = MibTableColumn
outletPduCStatus = _OutletPduCStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 8),
    _OutletPduCStatus_Type()
)
outletPduCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCStatus.setStatus("mandatory")
_OutletPduCAppPower_Type = Integer32
_OutletPduCAppPower_Object = MibTableColumn
outletPduCAppPower = _OutletPduCAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 9),
    _OutletPduCAppPower_Type()
)
outletPduCAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCAppPower.setUnits("0.1W")
_OutletPduCVoltage_Type = Integer32
_OutletPduCVoltage_Object = MibTableColumn
outletPduCVoltage = _OutletPduCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 10),
    _OutletPduCVoltage_Type()
)
outletPduCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduC_Object = MibTable
pduPwrMonitoringOutletCfgTablePduC = _PduPwrMonitoringOutletCfgTablePduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduC.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduCEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduCEntry = _PduPwrMonitoringOutletCfgPduCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1)
)
pduPwrMonitoringOutletCfgPduCEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduCIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduCEntry.setStatus("mandatory")


class _OutletCfgPduCIndex_Type(Integer32):
    """Custom type outletCfgPduCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduCIndex_Type.__name__ = "Integer32"
_OutletCfgPduCIndex_Object = MibTableColumn
outletCfgPduCIndex = _OutletCfgPduCIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 1),
    _OutletCfgPduCIndex_Type()
)
outletCfgPduCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduCIndex.setStatus("mandatory")
_OutletCfgPduCName_Type = DisplayString
_OutletCfgPduCName_Object = MibTableColumn
outletCfgPduCName = _OutletCfgPduCName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 2),
    _OutletCfgPduCName_Type()
)
outletCfgPduCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCName.setStatus("mandatory")


class _OutletCfgPduCDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduCDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduCDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduCDelayOnStatus_Object = MibTableColumn
outletCfgPduCDelayOnStatus = _OutletCfgPduCDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 3),
    _OutletCfgPduCDelayOnStatus_Type()
)
outletCfgPduCDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOnStatus.setStatus("mandatory")
_OutletCfgPduCDelayOnTime_Type = Integer32
_OutletCfgPduCDelayOnTime_Object = MibTableColumn
outletCfgPduCDelayOnTime = _OutletCfgPduCDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 4),
    _OutletCfgPduCDelayOnTime_Type()
)
outletCfgPduCDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOnTime.setUnits("seconds")


class _OutletCfgPduCDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduCDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduCDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduCDelayOffStatus_Object = MibTableColumn
outletCfgPduCDelayOffStatus = _OutletCfgPduCDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 5),
    _OutletCfgPduCDelayOffStatus_Type()
)
outletCfgPduCDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOffStatus.setStatus("mandatory")
_OutletCfgPduCDelayOffTime_Type = Integer32
_OutletCfgPduCDelayOffTime_Object = MibTableColumn
outletCfgPduCDelayOffTime = _OutletCfgPduCDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 6),
    _OutletCfgPduCDelayOffTime_Type()
)
outletCfgPduCDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOffTime.setUnits("seconds")
_OutletCfgPduCReboot_Type = Integer32
_OutletCfgPduCReboot_Object = MibTableColumn
outletCfgPduCReboot = _OutletCfgPduCReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 7),
    _OutletCfgPduCReboot_Type()
)
outletCfgPduCReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCReboot.setUnits("seconds")
_OutletCfgPduCOverCurrCritical_Type = Integer32
_OutletCfgPduCOverCurrCritical_Object = MibTableColumn
outletCfgPduCOverCurrCritical = _OutletCfgPduCOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 8),
    _OutletCfgPduCOverCurrCritical_Type()
)
outletCfgPduCOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrCritical.setUnits("0.1A")
_OutletCfgPduCOverCurrWarning_Type = Integer32
_OutletCfgPduCOverCurrWarning_Object = MibTableColumn
outletCfgPduCOverCurrWarning = _OutletCfgPduCOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 9),
    _OutletCfgPduCOverCurrWarning_Type()
)
outletCfgPduCOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrWarning.setUnits("0.1A")
_OutletCfgPduCOverPwrCritical_Type = Integer32
_OutletCfgPduCOverPwrCritical_Object = MibTableColumn
outletCfgPduCOverPwrCritical = _OutletCfgPduCOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 10),
    _OutletCfgPduCOverPwrCritical_Type()
)
outletCfgPduCOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrCritical.setUnits("1W")
_OutletCfgPduCOverPwrWarning_Type = Integer32
_OutletCfgPduCOverPwrWarning_Object = MibTableColumn
outletCfgPduCOverPwrWarning = _OutletCfgPduCOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 11),
    _OutletCfgPduCOverPwrWarning_Type()
)
outletCfgPduCOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduC_Object = MibTable
pduPwrMonitoringOutletCtlTablePduC = _PduPwrMonitoringOutletCtlTablePduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduC.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduCEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduCEntry = _PduPwrMonitoringOutletCtlPduCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4, 1)
)
pduPwrMonitoringOutletCtlPduCEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduCIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduCEntry.setStatus("mandatory")


class _OutletCtlPduCIndex_Type(Integer32):
    """Custom type outletCtlPduCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduCIndex_Type.__name__ = "Integer32"
_OutletCtlPduCIndex_Object = MibTableColumn
outletCtlPduCIndex = _OutletCtlPduCIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4, 1, 1),
    _OutletCtlPduCIndex_Type()
)
outletCtlPduCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduCIndex.setStatus("mandatory")


class _OutletCtlPduCControl_Type(Integer32):
    """Custom type outletCtlPduCControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduCControl_Type.__name__ = "Integer32"
_OutletCtlPduCControl_Object = MibTableColumn
outletCtlPduCControl = _OutletCtlPduCControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4, 1, 2),
    _OutletCtlPduCControl_Type()
)
outletCtlPduCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduCControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduD_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduD = _PduPwrMonitoringOutletPduD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4)
)
_PduPwrMonitoringOutletNumPduD_Type = Integer32
_PduPwrMonitoringOutletNumPduD_Object = MibScalar
pduPwrMonitoringOutletNumPduD = _PduPwrMonitoringOutletNumPduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 1),
    _PduPwrMonitoringOutletNumPduD_Type()
)
pduPwrMonitoringOutletNumPduD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduD.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduD_Object = MibTable
pduPwrMonitoringOutletStatusTablePduD = _PduPwrMonitoringOutletStatusTablePduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduD.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduDEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduDEntry = _PduPwrMonitoringOutletStatusPduDEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1)
)
pduPwrMonitoringOutletStatusPduDEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduDIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduDEntry.setStatus("mandatory")


class _OutletPduDIndex_Type(Integer32):
    """Custom type outletPduDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduDIndex_Type.__name__ = "Integer32"
_OutletPduDIndex_Object = MibTableColumn
outletPduDIndex = _OutletPduDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 1),
    _OutletPduDIndex_Type()
)
outletPduDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDIndex.setStatus("mandatory")


class _OutletPduDState_Type(Integer32):
    """Custom type outletPduDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduDState_Type.__name__ = "Integer32"
_OutletPduDState_Object = MibTableColumn
outletPduDState = _OutletPduDState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 2),
    _OutletPduDState_Type()
)
outletPduDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDState.setStatus("mandatory")
_OutletPduDCurrent_Type = Integer32
_OutletPduDCurrent_Object = MibTableColumn
outletPduDCurrent = _OutletPduDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 3),
    _OutletPduDCurrent_Type()
)
outletPduDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDCurrent.setUnits("0.01A")
_OutletPduDPwrFactor_Type = Integer32
_OutletPduDPwrFactor_Object = MibTableColumn
outletPduDPwrFactor = _OutletPduDPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 4),
    _OutletPduDPwrFactor_Type()
)
outletPduDPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDPwrFactor.setUnits("0.1%")
_OutletPduDPower_Type = Integer32
_OutletPduDPower_Object = MibTableColumn
outletPduDPower = _OutletPduDPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 5),
    _OutletPduDPower_Type()
)
outletPduDPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDPower.setUnits("0.1W")
_OutletPduDEnergy_Type = Integer32
_OutletPduDEnergy_Object = MibTableColumn
outletPduDEnergy = _OutletPduDEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 6),
    _OutletPduDEnergy_Type()
)
outletPduDEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDEnergy.setUnits("KWh")
_OutletPduDResetFrom_Type = DisplayString
_OutletPduDResetFrom_Object = MibTableColumn
outletPduDResetFrom = _OutletPduDResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 7),
    _OutletPduDResetFrom_Type()
)
outletPduDResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDResetFrom.setStatus("mandatory")


class _OutletPduDStatus_Type(Integer32):
    """Custom type outletPduDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduDStatus_Type.__name__ = "Integer32"
_OutletPduDStatus_Object = MibTableColumn
outletPduDStatus = _OutletPduDStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 8),
    _OutletPduDStatus_Type()
)
outletPduDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDStatus.setStatus("mandatory")
_OutletPduDAppPower_Type = Integer32
_OutletPduDAppPower_Object = MibTableColumn
outletPduDAppPower = _OutletPduDAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 9),
    _OutletPduDAppPower_Type()
)
outletPduDAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDAppPower.setUnits("0.1W")
_OutletPduDVoltage_Type = Integer32
_OutletPduDVoltage_Object = MibTableColumn
outletPduDVoltage = _OutletPduDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 10),
    _OutletPduDVoltage_Type()
)
outletPduDVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduD_Object = MibTable
pduPwrMonitoringOutletCfgTablePduD = _PduPwrMonitoringOutletCfgTablePduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduD.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduDEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduDEntry = _PduPwrMonitoringOutletCfgPduDEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1)
)
pduPwrMonitoringOutletCfgPduDEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduDIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduDEntry.setStatus("mandatory")


class _OutletCfgPduDIndex_Type(Integer32):
    """Custom type outletCfgPduDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduDIndex_Type.__name__ = "Integer32"
_OutletCfgPduDIndex_Object = MibTableColumn
outletCfgPduDIndex = _OutletCfgPduDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 1),
    _OutletCfgPduDIndex_Type()
)
outletCfgPduDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduDIndex.setStatus("mandatory")
_OutletCfgPduDName_Type = DisplayString
_OutletCfgPduDName_Object = MibTableColumn
outletCfgPduDName = _OutletCfgPduDName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 2),
    _OutletCfgPduDName_Type()
)
outletCfgPduDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDName.setStatus("mandatory")


class _OutletCfgPduDDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduDDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduDDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduDDelayOnStatus_Object = MibTableColumn
outletCfgPduDDelayOnStatus = _OutletCfgPduDDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 3),
    _OutletCfgPduDDelayOnStatus_Type()
)
outletCfgPduDDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOnStatus.setStatus("mandatory")
_OutletCfgPduDDelayOnTime_Type = Integer32
_OutletCfgPduDDelayOnTime_Object = MibTableColumn
outletCfgPduDDelayOnTime = _OutletCfgPduDDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 4),
    _OutletCfgPduDDelayOnTime_Type()
)
outletCfgPduDDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOnTime.setUnits("seconds")


class _OutletCfgPduDDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduDDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduDDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduDDelayOffStatus_Object = MibTableColumn
outletCfgPduDDelayOffStatus = _OutletCfgPduDDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 5),
    _OutletCfgPduDDelayOffStatus_Type()
)
outletCfgPduDDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOffStatus.setStatus("mandatory")
_OutletCfgPduDDelayOffTime_Type = Integer32
_OutletCfgPduDDelayOffTime_Object = MibTableColumn
outletCfgPduDDelayOffTime = _OutletCfgPduDDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 6),
    _OutletCfgPduDDelayOffTime_Type()
)
outletCfgPduDDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOffTime.setUnits("seconds")
_OutletCfgPduDReboot_Type = Integer32
_OutletCfgPduDReboot_Object = MibTableColumn
outletCfgPduDReboot = _OutletCfgPduDReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 7),
    _OutletCfgPduDReboot_Type()
)
outletCfgPduDReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDReboot.setUnits("seconds")
_OutletCfgPduDOverCurrCritical_Type = Integer32
_OutletCfgPduDOverCurrCritical_Object = MibTableColumn
outletCfgPduDOverCurrCritical = _OutletCfgPduDOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 8),
    _OutletCfgPduDOverCurrCritical_Type()
)
outletCfgPduDOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrCritical.setUnits("0.1A")
_OutletCfgPduDOverCurrWarning_Type = Integer32
_OutletCfgPduDOverCurrWarning_Object = MibTableColumn
outletCfgPduDOverCurrWarning = _OutletCfgPduDOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 9),
    _OutletCfgPduDOverCurrWarning_Type()
)
outletCfgPduDOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrWarning.setUnits("0.1A")
_OutletCfgPduDOverPwrCritical_Type = Integer32
_OutletCfgPduDOverPwrCritical_Object = MibTableColumn
outletCfgPduDOverPwrCritical = _OutletCfgPduDOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 10),
    _OutletCfgPduDOverPwrCritical_Type()
)
outletCfgPduDOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrCritical.setUnits("1W")
_OutletCfgPduDOverPwrWarning_Type = Integer32
_OutletCfgPduDOverPwrWarning_Object = MibTableColumn
outletCfgPduDOverPwrWarning = _OutletCfgPduDOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 11),
    _OutletCfgPduDOverPwrWarning_Type()
)
outletCfgPduDOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduD_Object = MibTable
pduPwrMonitoringOutletCtlTablePduD = _PduPwrMonitoringOutletCtlTablePduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduD.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduDEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduDEntry = _PduPwrMonitoringOutletCtlPduDEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4, 1)
)
pduPwrMonitoringOutletCtlPduDEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduDIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduDEntry.setStatus("mandatory")


class _OutletCtlPduDIndex_Type(Integer32):
    """Custom type outletCtlPduDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduDIndex_Type.__name__ = "Integer32"
_OutletCtlPduDIndex_Object = MibTableColumn
outletCtlPduDIndex = _OutletCtlPduDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4, 1, 1),
    _OutletCtlPduDIndex_Type()
)
outletCtlPduDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduDIndex.setStatus("mandatory")


class _OutletCtlPduDControl_Type(Integer32):
    """Custom type outletCtlPduDControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduDControl_Type.__name__ = "Integer32"
_OutletCtlPduDControl_Object = MibTableColumn
outletCtlPduDControl = _OutletCtlPduDControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4, 1, 2),
    _OutletCtlPduDControl_Type()
)
outletCtlPduDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduDControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduE_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduE = _PduPwrMonitoringOutletPduE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5)
)
_PduPwrMonitoringOutletNumPduE_Type = Integer32
_PduPwrMonitoringOutletNumPduE_Object = MibScalar
pduPwrMonitoringOutletNumPduE = _PduPwrMonitoringOutletNumPduE_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 1),
    _PduPwrMonitoringOutletNumPduE_Type()
)
pduPwrMonitoringOutletNumPduE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduE.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduE_Object = MibTable
pduPwrMonitoringOutletStatusTablePduE = _PduPwrMonitoringOutletStatusTablePduE_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduE.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduEEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduEEntry = _PduPwrMonitoringOutletStatusPduEEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1)
)
pduPwrMonitoringOutletStatusPduEEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduEIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduEEntry.setStatus("mandatory")


class _OutletPduEIndex_Type(Integer32):
    """Custom type outletPduEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduEIndex_Type.__name__ = "Integer32"
_OutletPduEIndex_Object = MibTableColumn
outletPduEIndex = _OutletPduEIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 1),
    _OutletPduEIndex_Type()
)
outletPduEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEIndex.setStatus("mandatory")


class _OutletPduEState_Type(Integer32):
    """Custom type outletPduEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduEState_Type.__name__ = "Integer32"
_OutletPduEState_Object = MibTableColumn
outletPduEState = _OutletPduEState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 2),
    _OutletPduEState_Type()
)
outletPduEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEState.setStatus("mandatory")
_OutletPduECurrent_Type = Integer32
_OutletPduECurrent_Object = MibTableColumn
outletPduECurrent = _OutletPduECurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 3),
    _OutletPduECurrent_Type()
)
outletPduECurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduECurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduECurrent.setUnits("0.01A")
_OutletPduEPwrFactor_Type = Integer32
_OutletPduEPwrFactor_Object = MibTableColumn
outletPduEPwrFactor = _OutletPduEPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 4),
    _OutletPduEPwrFactor_Type()
)
outletPduEPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduEPwrFactor.setUnits("0.1%")
_OutletPduEPower_Type = Integer32
_OutletPduEPower_Object = MibTableColumn
outletPduEPower = _OutletPduEPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 5),
    _OutletPduEPower_Type()
)
outletPduEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduEPower.setUnits("0.1W")
_OutletPduEEnergy_Type = Integer32
_OutletPduEEnergy_Object = MibTableColumn
outletPduEEnergy = _OutletPduEEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 6),
    _OutletPduEEnergy_Type()
)
outletPduEEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduEEnergy.setUnits("KWh")
_OutletPduEResetFrom_Type = DisplayString
_OutletPduEResetFrom_Object = MibTableColumn
outletPduEResetFrom = _OutletPduEResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 7),
    _OutletPduEResetFrom_Type()
)
outletPduEResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEResetFrom.setStatus("mandatory")


class _OutletPduEStatus_Type(Integer32):
    """Custom type outletPduEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduEStatus_Type.__name__ = "Integer32"
_OutletPduEStatus_Object = MibTableColumn
outletPduEStatus = _OutletPduEStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 8),
    _OutletPduEStatus_Type()
)
outletPduEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEStatus.setStatus("mandatory")
_OutletPduEAppPower_Type = Integer32
_OutletPduEAppPower_Object = MibTableColumn
outletPduEAppPower = _OutletPduEAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 9),
    _OutletPduEAppPower_Type()
)
outletPduEAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduEAppPower.setUnits("0.1W")
_OutletPduEVoltage_Type = Integer32
_OutletPduEVoltage_Object = MibTableColumn
outletPduEVoltage = _OutletPduEVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 2, 1, 10),
    _OutletPduEVoltage_Type()
)
outletPduEVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduEVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduEVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduE_Object = MibTable
pduPwrMonitoringOutletCfgTablePduE = _PduPwrMonitoringOutletCfgTablePduE_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduE.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduEEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduEEntry = _PduPwrMonitoringOutletCfgPduEEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1)
)
pduPwrMonitoringOutletCfgPduEEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduEIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduEEntry.setStatus("mandatory")


class _OutletCfgPduEIndex_Type(Integer32):
    """Custom type outletCfgPduEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduEIndex_Type.__name__ = "Integer32"
_OutletCfgPduEIndex_Object = MibTableColumn
outletCfgPduEIndex = _OutletCfgPduEIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 1),
    _OutletCfgPduEIndex_Type()
)
outletCfgPduEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduEIndex.setStatus("mandatory")
_OutletCfgPduEName_Type = DisplayString
_OutletCfgPduEName_Object = MibTableColumn
outletCfgPduEName = _OutletCfgPduEName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 2),
    _OutletCfgPduEName_Type()
)
outletCfgPduEName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEName.setStatus("mandatory")


class _OutletCfgPduEDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduEDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduEDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduEDelayOnStatus_Object = MibTableColumn
outletCfgPduEDelayOnStatus = _OutletCfgPduEDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 3),
    _OutletCfgPduEDelayOnStatus_Type()
)
outletCfgPduEDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEDelayOnStatus.setStatus("mandatory")
_OutletCfgPduEDelayOnTime_Type = Integer32
_OutletCfgPduEDelayOnTime_Object = MibTableColumn
outletCfgPduEDelayOnTime = _OutletCfgPduEDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 4),
    _OutletCfgPduEDelayOnTime_Type()
)
outletCfgPduEDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEDelayOnTime.setUnits("seconds")


class _OutletCfgPduEDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduEDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduEDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduEDelayOffStatus_Object = MibTableColumn
outletCfgPduEDelayOffStatus = _OutletCfgPduEDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 5),
    _OutletCfgPduEDelayOffStatus_Type()
)
outletCfgPduEDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEDelayOffStatus.setStatus("mandatory")
_OutletCfgPduEDelayOffTime_Type = Integer32
_OutletCfgPduEDelayOffTime_Object = MibTableColumn
outletCfgPduEDelayOffTime = _OutletCfgPduEDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 6),
    _OutletCfgPduEDelayOffTime_Type()
)
outletCfgPduEDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEDelayOffTime.setUnits("seconds")
_OutletCfgPduEReboot_Type = Integer32
_OutletCfgPduEReboot_Object = MibTableColumn
outletCfgPduEReboot = _OutletCfgPduEReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 7),
    _OutletCfgPduEReboot_Type()
)
outletCfgPduEReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEReboot.setUnits("seconds")
_OutletCfgPduEOverCurrCritical_Type = Integer32
_OutletCfgPduEOverCurrCritical_Object = MibTableColumn
outletCfgPduEOverCurrCritical = _OutletCfgPduEOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 8),
    _OutletCfgPduEOverCurrCritical_Type()
)
outletCfgPduEOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEOverCurrCritical.setUnits("0.1A")
_OutletCfgPduEOverCurrWarning_Type = Integer32
_OutletCfgPduEOverCurrWarning_Object = MibTableColumn
outletCfgPduEOverCurrWarning = _OutletCfgPduEOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 9),
    _OutletCfgPduEOverCurrWarning_Type()
)
outletCfgPduEOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEOverCurrWarning.setUnits("0.1A")
_OutletCfgPduEOverPwrCritical_Type = Integer32
_OutletCfgPduEOverPwrCritical_Object = MibTableColumn
outletCfgPduEOverPwrCritical = _OutletCfgPduEOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 10),
    _OutletCfgPduEOverPwrCritical_Type()
)
outletCfgPduEOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEOverPwrCritical.setUnits("1W")
_OutletCfgPduEOverPwrWarning_Type = Integer32
_OutletCfgPduEOverPwrWarning_Object = MibTableColumn
outletCfgPduEOverPwrWarning = _OutletCfgPduEOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 3, 1, 11),
    _OutletCfgPduEOverPwrWarning_Type()
)
outletCfgPduEOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduEOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduEOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduE_Object = MibTable
pduPwrMonitoringOutletCtlTablePduE = _PduPwrMonitoringOutletCtlTablePduE_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduE.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduEEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduEEntry = _PduPwrMonitoringOutletCtlPduEEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 4, 1)
)
pduPwrMonitoringOutletCtlPduEEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduEIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduEEntry.setStatus("mandatory")


class _OutletCtlPduEIndex_Type(Integer32):
    """Custom type outletCtlPduEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduEIndex_Type.__name__ = "Integer32"
_OutletCtlPduEIndex_Object = MibTableColumn
outletCtlPduEIndex = _OutletCtlPduEIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 4, 1, 1),
    _OutletCtlPduEIndex_Type()
)
outletCtlPduEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduEIndex.setStatus("mandatory")


class _OutletCtlPduEControl_Type(Integer32):
    """Custom type outletCtlPduEControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduEControl_Type.__name__ = "Integer32"
_OutletCtlPduEControl_Object = MibTableColumn
outletCtlPduEControl = _OutletCtlPduEControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 5, 4, 1, 2),
    _OutletCtlPduEControl_Type()
)
outletCtlPduEControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduEControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduF_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduF = _PduPwrMonitoringOutletPduF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6)
)
_PduPwrMonitoringOutletNumPduF_Type = Integer32
_PduPwrMonitoringOutletNumPduF_Object = MibScalar
pduPwrMonitoringOutletNumPduF = _PduPwrMonitoringOutletNumPduF_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 1),
    _PduPwrMonitoringOutletNumPduF_Type()
)
pduPwrMonitoringOutletNumPduF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduF.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduF_Object = MibTable
pduPwrMonitoringOutletStatusTablePduF = _PduPwrMonitoringOutletStatusTablePduF_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduF.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduFEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduFEntry = _PduPwrMonitoringOutletStatusPduFEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1)
)
pduPwrMonitoringOutletStatusPduFEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduFIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduFEntry.setStatus("mandatory")


class _OutletPduFIndex_Type(Integer32):
    """Custom type outletPduFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduFIndex_Type.__name__ = "Integer32"
_OutletPduFIndex_Object = MibTableColumn
outletPduFIndex = _OutletPduFIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 1),
    _OutletPduFIndex_Type()
)
outletPduFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFIndex.setStatus("mandatory")


class _OutletPduFState_Type(Integer32):
    """Custom type outletPduFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduFState_Type.__name__ = "Integer32"
_OutletPduFState_Object = MibTableColumn
outletPduFState = _OutletPduFState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 2),
    _OutletPduFState_Type()
)
outletPduFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFState.setStatus("mandatory")
_OutletPduFCurrent_Type = Integer32
_OutletPduFCurrent_Object = MibTableColumn
outletPduFCurrent = _OutletPduFCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 3),
    _OutletPduFCurrent_Type()
)
outletPduFCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduFCurrent.setUnits("0.01A")
_OutletPduFPwrFactor_Type = Integer32
_OutletPduFPwrFactor_Object = MibTableColumn
outletPduFPwrFactor = _OutletPduFPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 4),
    _OutletPduFPwrFactor_Type()
)
outletPduFPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduFPwrFactor.setUnits("0.1%")
_OutletPduFPower_Type = Integer32
_OutletPduFPower_Object = MibTableColumn
outletPduFPower = _OutletPduFPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 5),
    _OutletPduFPower_Type()
)
outletPduFPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduFPower.setUnits("0.1W")
_OutletPduFEnergy_Type = Integer32
_OutletPduFEnergy_Object = MibTableColumn
outletPduFEnergy = _OutletPduFEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 6),
    _OutletPduFEnergy_Type()
)
outletPduFEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduFEnergy.setUnits("KWh")
_OutletPduFResetFrom_Type = DisplayString
_OutletPduFResetFrom_Object = MibTableColumn
outletPduFResetFrom = _OutletPduFResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 7),
    _OutletPduFResetFrom_Type()
)
outletPduFResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFResetFrom.setStatus("mandatory")


class _OutletPduFStatus_Type(Integer32):
    """Custom type outletPduFStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduFStatus_Type.__name__ = "Integer32"
_OutletPduFStatus_Object = MibTableColumn
outletPduFStatus = _OutletPduFStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 8),
    _OutletPduFStatus_Type()
)
outletPduFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFStatus.setStatus("mandatory")
_OutletPduFAppPower_Type = Integer32
_OutletPduFAppPower_Object = MibTableColumn
outletPduFAppPower = _OutletPduFAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 9),
    _OutletPduFAppPower_Type()
)
outletPduFAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduFAppPower.setUnits("0.1W")
_OutletPduFVoltage_Type = Integer32
_OutletPduFVoltage_Object = MibTableColumn
outletPduFVoltage = _OutletPduFVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 2, 1, 10),
    _OutletPduFVoltage_Type()
)
outletPduFVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduFVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduFVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduF_Object = MibTable
pduPwrMonitoringOutletCfgTablePduF = _PduPwrMonitoringOutletCfgTablePduF_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduF.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduFEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduFEntry = _PduPwrMonitoringOutletCfgPduFEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1)
)
pduPwrMonitoringOutletCfgPduFEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduFIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduFEntry.setStatus("mandatory")


class _OutletCfgPduFIndex_Type(Integer32):
    """Custom type outletCfgPduFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduFIndex_Type.__name__ = "Integer32"
_OutletCfgPduFIndex_Object = MibTableColumn
outletCfgPduFIndex = _OutletCfgPduFIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 1),
    _OutletCfgPduFIndex_Type()
)
outletCfgPduFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduFIndex.setStatus("mandatory")
_OutletCfgPduFName_Type = DisplayString
_OutletCfgPduFName_Object = MibTableColumn
outletCfgPduFName = _OutletCfgPduFName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 2),
    _OutletCfgPduFName_Type()
)
outletCfgPduFName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFName.setStatus("mandatory")


class _OutletCfgPduFDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduFDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduFDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduFDelayOnStatus_Object = MibTableColumn
outletCfgPduFDelayOnStatus = _OutletCfgPduFDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 3),
    _OutletCfgPduFDelayOnStatus_Type()
)
outletCfgPduFDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFDelayOnStatus.setStatus("mandatory")
_OutletCfgPduFDelayOnTime_Type = Integer32
_OutletCfgPduFDelayOnTime_Object = MibTableColumn
outletCfgPduFDelayOnTime = _OutletCfgPduFDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 4),
    _OutletCfgPduFDelayOnTime_Type()
)
outletCfgPduFDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFDelayOnTime.setUnits("seconds")


class _OutletCfgPduFDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduFDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduFDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduFDelayOffStatus_Object = MibTableColumn
outletCfgPduFDelayOffStatus = _OutletCfgPduFDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 5),
    _OutletCfgPduFDelayOffStatus_Type()
)
outletCfgPduFDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFDelayOffStatus.setStatus("mandatory")
_OutletCfgPduFDelayOffTime_Type = Integer32
_OutletCfgPduFDelayOffTime_Object = MibTableColumn
outletCfgPduFDelayOffTime = _OutletCfgPduFDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 6),
    _OutletCfgPduFDelayOffTime_Type()
)
outletCfgPduFDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFDelayOffTime.setUnits("seconds")
_OutletCfgPduFReboot_Type = Integer32
_OutletCfgPduFReboot_Object = MibTableColumn
outletCfgPduFReboot = _OutletCfgPduFReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 7),
    _OutletCfgPduFReboot_Type()
)
outletCfgPduFReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFReboot.setUnits("seconds")
_OutletCfgPduFOverCurrCritical_Type = Integer32
_OutletCfgPduFOverCurrCritical_Object = MibTableColumn
outletCfgPduFOverCurrCritical = _OutletCfgPduFOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 8),
    _OutletCfgPduFOverCurrCritical_Type()
)
outletCfgPduFOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFOverCurrCritical.setUnits("0.1A")
_OutletCfgPduFOverCurrWarning_Type = Integer32
_OutletCfgPduFOverCurrWarning_Object = MibTableColumn
outletCfgPduFOverCurrWarning = _OutletCfgPduFOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 9),
    _OutletCfgPduFOverCurrWarning_Type()
)
outletCfgPduFOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFOverCurrWarning.setUnits("0.1A")
_OutletCfgPduFOverPwrCritical_Type = Integer32
_OutletCfgPduFOverPwrCritical_Object = MibTableColumn
outletCfgPduFOverPwrCritical = _OutletCfgPduFOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 10),
    _OutletCfgPduFOverPwrCritical_Type()
)
outletCfgPduFOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFOverPwrCritical.setUnits("1W")
_OutletCfgPduFOverPwrWarning_Type = Integer32
_OutletCfgPduFOverPwrWarning_Object = MibTableColumn
outletCfgPduFOverPwrWarning = _OutletCfgPduFOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 3, 1, 11),
    _OutletCfgPduFOverPwrWarning_Type()
)
outletCfgPduFOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduFOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduFOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduF_Object = MibTable
pduPwrMonitoringOutletCtlTablePduF = _PduPwrMonitoringOutletCtlTablePduF_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduF.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduFEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduFEntry = _PduPwrMonitoringOutletCtlPduFEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 4, 1)
)
pduPwrMonitoringOutletCtlPduFEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduFIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduFEntry.setStatus("mandatory")


class _OutletCtlPduFIndex_Type(Integer32):
    """Custom type outletCtlPduFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduFIndex_Type.__name__ = "Integer32"
_OutletCtlPduFIndex_Object = MibTableColumn
outletCtlPduFIndex = _OutletCtlPduFIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 4, 1, 1),
    _OutletCtlPduFIndex_Type()
)
outletCtlPduFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduFIndex.setStatus("mandatory")


class _OutletCtlPduFControl_Type(Integer32):
    """Custom type outletCtlPduFControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduFControl_Type.__name__ = "Integer32"
_OutletCtlPduFControl_Object = MibTableColumn
outletCtlPduFControl = _OutletCtlPduFControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 6, 4, 1, 2),
    _OutletCtlPduFControl_Type()
)
outletCtlPduFControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduFControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduG_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduG = _PduPwrMonitoringOutletPduG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7)
)
_PduPwrMonitoringOutletNumPduG_Type = Integer32
_PduPwrMonitoringOutletNumPduG_Object = MibScalar
pduPwrMonitoringOutletNumPduG = _PduPwrMonitoringOutletNumPduG_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 1),
    _PduPwrMonitoringOutletNumPduG_Type()
)
pduPwrMonitoringOutletNumPduG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduG.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduG_Object = MibTable
pduPwrMonitoringOutletStatusTablePduG = _PduPwrMonitoringOutletStatusTablePduG_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduG.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduGEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduGEntry = _PduPwrMonitoringOutletStatusPduGEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1)
)
pduPwrMonitoringOutletStatusPduGEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduGIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduGEntry.setStatus("mandatory")


class _OutletPduGIndex_Type(Integer32):
    """Custom type outletPduGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduGIndex_Type.__name__ = "Integer32"
_OutletPduGIndex_Object = MibTableColumn
outletPduGIndex = _OutletPduGIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 1),
    _OutletPduGIndex_Type()
)
outletPduGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGIndex.setStatus("mandatory")


class _OutletPduGState_Type(Integer32):
    """Custom type outletPduGState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduGState_Type.__name__ = "Integer32"
_OutletPduGState_Object = MibTableColumn
outletPduGState = _OutletPduGState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 2),
    _OutletPduGState_Type()
)
outletPduGState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGState.setStatus("mandatory")
_OutletPduGCurrent_Type = Integer32
_OutletPduGCurrent_Object = MibTableColumn
outletPduGCurrent = _OutletPduGCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 3),
    _OutletPduGCurrent_Type()
)
outletPduGCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduGCurrent.setUnits("0.01A")
_OutletPduGPwrFactor_Type = Integer32
_OutletPduGPwrFactor_Object = MibTableColumn
outletPduGPwrFactor = _OutletPduGPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 4),
    _OutletPduGPwrFactor_Type()
)
outletPduGPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduGPwrFactor.setUnits("0.1%")
_OutletPduGPower_Type = Integer32
_OutletPduGPower_Object = MibTableColumn
outletPduGPower = _OutletPduGPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 5),
    _OutletPduGPower_Type()
)
outletPduGPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduGPower.setUnits("0.1W")
_OutletPduGEnergy_Type = Integer32
_OutletPduGEnergy_Object = MibTableColumn
outletPduGEnergy = _OutletPduGEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 6),
    _OutletPduGEnergy_Type()
)
outletPduGEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduGEnergy.setUnits("KWh")
_OutletPduGResetFrom_Type = DisplayString
_OutletPduGResetFrom_Object = MibTableColumn
outletPduGResetFrom = _OutletPduGResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 7),
    _OutletPduGResetFrom_Type()
)
outletPduGResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGResetFrom.setStatus("mandatory")


class _OutletPduGStatus_Type(Integer32):
    """Custom type outletPduGStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduGStatus_Type.__name__ = "Integer32"
_OutletPduGStatus_Object = MibTableColumn
outletPduGStatus = _OutletPduGStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 8),
    _OutletPduGStatus_Type()
)
outletPduGStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGStatus.setStatus("mandatory")
_OutletPduGAppPower_Type = Integer32
_OutletPduGAppPower_Object = MibTableColumn
outletPduGAppPower = _OutletPduGAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 9),
    _OutletPduGAppPower_Type()
)
outletPduGAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduGAppPower.setUnits("0.1W")
_OutletPduGVoltage_Type = Integer32
_OutletPduGVoltage_Object = MibTableColumn
outletPduGVoltage = _OutletPduGVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 2, 1, 10),
    _OutletPduGVoltage_Type()
)
outletPduGVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduGVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduGVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduG_Object = MibTable
pduPwrMonitoringOutletCfgTablePduG = _PduPwrMonitoringOutletCfgTablePduG_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduG.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduGEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduGEntry = _PduPwrMonitoringOutletCfgPduGEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1)
)
pduPwrMonitoringOutletCfgPduGEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduGIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduGEntry.setStatus("mandatory")


class _OutletCfgPduGIndex_Type(Integer32):
    """Custom type outletCfgPduGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduGIndex_Type.__name__ = "Integer32"
_OutletCfgPduGIndex_Object = MibTableColumn
outletCfgPduGIndex = _OutletCfgPduGIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 1),
    _OutletCfgPduGIndex_Type()
)
outletCfgPduGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduGIndex.setStatus("mandatory")
_OutletCfgPduGName_Type = DisplayString
_OutletCfgPduGName_Object = MibTableColumn
outletCfgPduGName = _OutletCfgPduGName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 2),
    _OutletCfgPduGName_Type()
)
outletCfgPduGName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGName.setStatus("mandatory")


class _OutletCfgPduGDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduGDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduGDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduGDelayOnStatus_Object = MibTableColumn
outletCfgPduGDelayOnStatus = _OutletCfgPduGDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 3),
    _OutletCfgPduGDelayOnStatus_Type()
)
outletCfgPduGDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGDelayOnStatus.setStatus("mandatory")
_OutletCfgPduGDelayOnTime_Type = Integer32
_OutletCfgPduGDelayOnTime_Object = MibTableColumn
outletCfgPduGDelayOnTime = _OutletCfgPduGDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 4),
    _OutletCfgPduGDelayOnTime_Type()
)
outletCfgPduGDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGDelayOnTime.setUnits("seconds")


class _OutletCfgPduGDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduGDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduGDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduGDelayOffStatus_Object = MibTableColumn
outletCfgPduGDelayOffStatus = _OutletCfgPduGDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 5),
    _OutletCfgPduGDelayOffStatus_Type()
)
outletCfgPduGDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGDelayOffStatus.setStatus("mandatory")
_OutletCfgPduGDelayOffTime_Type = Integer32
_OutletCfgPduGDelayOffTime_Object = MibTableColumn
outletCfgPduGDelayOffTime = _OutletCfgPduGDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 6),
    _OutletCfgPduGDelayOffTime_Type()
)
outletCfgPduGDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGDelayOffTime.setUnits("seconds")
_OutletCfgPduGReboot_Type = Integer32
_OutletCfgPduGReboot_Object = MibTableColumn
outletCfgPduGReboot = _OutletCfgPduGReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 7),
    _OutletCfgPduGReboot_Type()
)
outletCfgPduGReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGReboot.setUnits("seconds")
_OutletCfgPduGOverCurrCritical_Type = Integer32
_OutletCfgPduGOverCurrCritical_Object = MibTableColumn
outletCfgPduGOverCurrCritical = _OutletCfgPduGOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 8),
    _OutletCfgPduGOverCurrCritical_Type()
)
outletCfgPduGOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGOverCurrCritical.setUnits("0.1A")
_OutletCfgPduGOverCurrWarning_Type = Integer32
_OutletCfgPduGOverCurrWarning_Object = MibTableColumn
outletCfgPduGOverCurrWarning = _OutletCfgPduGOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 9),
    _OutletCfgPduGOverCurrWarning_Type()
)
outletCfgPduGOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGOverCurrWarning.setUnits("0.1A")
_OutletCfgPduGOverPwrCritical_Type = Integer32
_OutletCfgPduGOverPwrCritical_Object = MibTableColumn
outletCfgPduGOverPwrCritical = _OutletCfgPduGOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 10),
    _OutletCfgPduGOverPwrCritical_Type()
)
outletCfgPduGOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGOverPwrCritical.setUnits("1W")
_OutletCfgPduGOverPwrWarning_Type = Integer32
_OutletCfgPduGOverPwrWarning_Object = MibTableColumn
outletCfgPduGOverPwrWarning = _OutletCfgPduGOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 3, 1, 11),
    _OutletCfgPduGOverPwrWarning_Type()
)
outletCfgPduGOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduGOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduGOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduG_Object = MibTable
pduPwrMonitoringOutletCtlTablePduG = _PduPwrMonitoringOutletCtlTablePduG_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduG.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduGEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduGEntry = _PduPwrMonitoringOutletCtlPduGEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 4, 1)
)
pduPwrMonitoringOutletCtlPduGEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduGIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduGEntry.setStatus("mandatory")


class _OutletCtlPduGIndex_Type(Integer32):
    """Custom type outletCtlPduGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduGIndex_Type.__name__ = "Integer32"
_OutletCtlPduGIndex_Object = MibTableColumn
outletCtlPduGIndex = _OutletCtlPduGIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 4, 1, 1),
    _OutletCtlPduGIndex_Type()
)
outletCtlPduGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduGIndex.setStatus("mandatory")


class _OutletCtlPduGControl_Type(Integer32):
    """Custom type outletCtlPduGControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduGControl_Type.__name__ = "Integer32"
_OutletCtlPduGControl_Object = MibTableColumn
outletCtlPduGControl = _OutletCtlPduGControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 7, 4, 1, 2),
    _OutletCtlPduGControl_Type()
)
outletCtlPduGControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduGControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduH_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduH = _PduPwrMonitoringOutletPduH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8)
)
_PduPwrMonitoringOutletNumPduH_Type = Integer32
_PduPwrMonitoringOutletNumPduH_Object = MibScalar
pduPwrMonitoringOutletNumPduH = _PduPwrMonitoringOutletNumPduH_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 1),
    _PduPwrMonitoringOutletNumPduH_Type()
)
pduPwrMonitoringOutletNumPduH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduH.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduH_Object = MibTable
pduPwrMonitoringOutletStatusTablePduH = _PduPwrMonitoringOutletStatusTablePduH_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduH.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduHEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduHEntry = _PduPwrMonitoringOutletStatusPduHEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1)
)
pduPwrMonitoringOutletStatusPduHEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletPduHIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduHEntry.setStatus("mandatory")


class _OutletPduHIndex_Type(Integer32):
    """Custom type outletPduHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduHIndex_Type.__name__ = "Integer32"
_OutletPduHIndex_Object = MibTableColumn
outletPduHIndex = _OutletPduHIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 1),
    _OutletPduHIndex_Type()
)
outletPduHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHIndex.setStatus("mandatory")


class _OutletPduHState_Type(Integer32):
    """Custom type outletPduHState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduHState_Type.__name__ = "Integer32"
_OutletPduHState_Object = MibTableColumn
outletPduHState = _OutletPduHState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 2),
    _OutletPduHState_Type()
)
outletPduHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHState.setStatus("mandatory")
_OutletPduHCurrent_Type = Integer32
_OutletPduHCurrent_Object = MibTableColumn
outletPduHCurrent = _OutletPduHCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 3),
    _OutletPduHCurrent_Type()
)
outletPduHCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduHCurrent.setUnits("0.01A")
_OutletPduHPwrFactor_Type = Integer32
_OutletPduHPwrFactor_Object = MibTableColumn
outletPduHPwrFactor = _OutletPduHPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 4),
    _OutletPduHPwrFactor_Type()
)
outletPduHPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduHPwrFactor.setUnits("0.1%")
_OutletPduHPower_Type = Integer32
_OutletPduHPower_Object = MibTableColumn
outletPduHPower = _OutletPduHPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 5),
    _OutletPduHPower_Type()
)
outletPduHPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduHPower.setUnits("0.1W")
_OutletPduHEnergy_Type = Integer32
_OutletPduHEnergy_Object = MibTableColumn
outletPduHEnergy = _OutletPduHEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 6),
    _OutletPduHEnergy_Type()
)
outletPduHEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduHEnergy.setUnits("KWh")
_OutletPduHResetFrom_Type = DisplayString
_OutletPduHResetFrom_Object = MibTableColumn
outletPduHResetFrom = _OutletPduHResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 7),
    _OutletPduHResetFrom_Type()
)
outletPduHResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHResetFrom.setStatus("mandatory")


class _OutletPduHStatus_Type(Integer32):
    """Custom type outletPduHStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduHStatus_Type.__name__ = "Integer32"
_OutletPduHStatus_Object = MibTableColumn
outletPduHStatus = _OutletPduHStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 8),
    _OutletPduHStatus_Type()
)
outletPduHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHStatus.setStatus("mandatory")
_OutletPduHAppPower_Type = Integer32
_OutletPduHAppPower_Object = MibTableColumn
outletPduHAppPower = _OutletPduHAppPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 9),
    _OutletPduHAppPower_Type()
)
outletPduHAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHAppPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduHAppPower.setUnits("0.1W")
_OutletPduHVoltage_Type = Integer32
_OutletPduHVoltage_Object = MibTableColumn
outletPduHVoltage = _OutletPduHVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 2, 1, 10),
    _OutletPduHVoltage_Type()
)
outletPduHVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduHVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduHVoltage.setUnits("0.1V")
_PduPwrMonitoringOutletCfgTablePduH_Object = MibTable
pduPwrMonitoringOutletCfgTablePduH = _PduPwrMonitoringOutletCfgTablePduH_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduH.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduHEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduHEntry = _PduPwrMonitoringOutletCfgPduHEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1)
)
pduPwrMonitoringOutletCfgPduHEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCfgPduHIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduHEntry.setStatus("mandatory")


class _OutletCfgPduHIndex_Type(Integer32):
    """Custom type outletCfgPduHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduHIndex_Type.__name__ = "Integer32"
_OutletCfgPduHIndex_Object = MibTableColumn
outletCfgPduHIndex = _OutletCfgPduHIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 1),
    _OutletCfgPduHIndex_Type()
)
outletCfgPduHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduHIndex.setStatus("mandatory")
_OutletCfgPduHName_Type = DisplayString
_OutletCfgPduHName_Object = MibTableColumn
outletCfgPduHName = _OutletCfgPduHName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 2),
    _OutletCfgPduHName_Type()
)
outletCfgPduHName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHName.setStatus("mandatory")


class _OutletCfgPduHDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduHDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduHDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduHDelayOnStatus_Object = MibTableColumn
outletCfgPduHDelayOnStatus = _OutletCfgPduHDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 3),
    _OutletCfgPduHDelayOnStatus_Type()
)
outletCfgPduHDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHDelayOnStatus.setStatus("mandatory")
_OutletCfgPduHDelayOnTime_Type = Integer32
_OutletCfgPduHDelayOnTime_Object = MibTableColumn
outletCfgPduHDelayOnTime = _OutletCfgPduHDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 4),
    _OutletCfgPduHDelayOnTime_Type()
)
outletCfgPduHDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHDelayOnTime.setUnits("seconds")


class _OutletCfgPduHDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduHDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduHDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduHDelayOffStatus_Object = MibTableColumn
outletCfgPduHDelayOffStatus = _OutletCfgPduHDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 5),
    _OutletCfgPduHDelayOffStatus_Type()
)
outletCfgPduHDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHDelayOffStatus.setStatus("mandatory")
_OutletCfgPduHDelayOffTime_Type = Integer32
_OutletCfgPduHDelayOffTime_Object = MibTableColumn
outletCfgPduHDelayOffTime = _OutletCfgPduHDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 6),
    _OutletCfgPduHDelayOffTime_Type()
)
outletCfgPduHDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHDelayOffTime.setUnits("seconds")
_OutletCfgPduHReboot_Type = Integer32
_OutletCfgPduHReboot_Object = MibTableColumn
outletCfgPduHReboot = _OutletCfgPduHReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 7),
    _OutletCfgPduHReboot_Type()
)
outletCfgPduHReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHReboot.setUnits("seconds")
_OutletCfgPduHOverCurrCritical_Type = Integer32
_OutletCfgPduHOverCurrCritical_Object = MibTableColumn
outletCfgPduHOverCurrCritical = _OutletCfgPduHOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 8),
    _OutletCfgPduHOverCurrCritical_Type()
)
outletCfgPduHOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHOverCurrCritical.setUnits("0.1A")
_OutletCfgPduHOverCurrWarning_Type = Integer32
_OutletCfgPduHOverCurrWarning_Object = MibTableColumn
outletCfgPduHOverCurrWarning = _OutletCfgPduHOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 9),
    _OutletCfgPduHOverCurrWarning_Type()
)
outletCfgPduHOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHOverCurrWarning.setUnits("0.1A")
_OutletCfgPduHOverPwrCritical_Type = Integer32
_OutletCfgPduHOverPwrCritical_Object = MibTableColumn
outletCfgPduHOverPwrCritical = _OutletCfgPduHOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 10),
    _OutletCfgPduHOverPwrCritical_Type()
)
outletCfgPduHOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHOverPwrCritical.setUnits("1W")
_OutletCfgPduHOverPwrWarning_Type = Integer32
_OutletCfgPduHOverPwrWarning_Object = MibTableColumn
outletCfgPduHOverPwrWarning = _OutletCfgPduHOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 3, 1, 11),
    _OutletCfgPduHOverPwrWarning_Type()
)
outletCfgPduHOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduHOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduHOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduH_Object = MibTable
pduPwrMonitoringOutletCtlTablePduH = _PduPwrMonitoringOutletCtlTablePduH_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduH.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduHEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduHEntry = _PduPwrMonitoringOutletCtlPduHEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 4, 1)
)
pduPwrMonitoringOutletCtlPduHEntry.setIndexNames(
    (0, "PWTv1-MIB", "outletCtlPduHIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduHEntry.setStatus("mandatory")


class _OutletCtlPduHIndex_Type(Integer32):
    """Custom type outletCtlPduHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduHIndex_Type.__name__ = "Integer32"
_OutletCtlPduHIndex_Object = MibTableColumn
outletCtlPduHIndex = _OutletCtlPduHIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 4, 1, 1),
    _OutletCtlPduHIndex_Type()
)
outletCtlPduHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduHIndex.setStatus("mandatory")


class _OutletCtlPduHControl_Type(Integer32):
    """Custom type outletCtlPduHControl based on Integer32"""
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
        *(("nothing", 1),
          ("immediateOn", 2),
          ("delayedOn", 3),
          ("immediateOff", 4),
          ("delayedOff", 5),
          ("immediateCycle", 6),
          ("delayedCycle", 7))
    )


_OutletCtlPduHControl_Type.__name__ = "Integer32"
_OutletCtlPduHControl_Object = MibTableColumn
outletCtlPduHControl = _OutletCtlPduHControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 8, 4, 1, 2),
    _OutletCtlPduHControl_Type()
)
outletCtlPduHControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduHControl.setStatus("mandatory")
_PduEnvMonitoring_ObjectIdentity = ObjectIdentity
pduEnvMonitoring = _PduEnvMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7)
)
_PduEmdStatusTable_Object = MibTable
pduEmdStatusTable = _PduEmdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    pduEmdStatusTable.setStatus("mandatory")
_PduEnvMonitoringStatus_Object = MibTableRow
pduEnvMonitoringStatus = _PduEnvMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1)
)
pduEnvMonitoringStatus.setIndexNames(
    (0, "PWTv1-MIB", "pduEnvStatusIndex"),
)
if mibBuilder.loadTexts:
    pduEnvMonitoringStatus.setStatus("mandatory")


class _PduEnvStatusIndex_Type(Integer32):
    """Custom type pduEnvStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PduEnvStatusIndex_Type.__name__ = "Integer32"
_PduEnvStatusIndex_Object = MibTableColumn
pduEnvStatusIndex = _PduEnvStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 1),
    _PduEnvStatusIndex_Type()
)
pduEnvStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvStatusIndex.setStatus("mandatory")
_PduEnvMonitoringTemp_Type = Integer32
_PduEnvMonitoringTemp_Object = MibTableColumn
pduEnvMonitoringTemp = _PduEnvMonitoringTemp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 2),
    _PduEnvMonitoringTemp_Type()
)
pduEnvMonitoringTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringTemp.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTemp.setUnits("degC")
_PduEnvMonitoringHumi_Type = Integer32
_PduEnvMonitoringHumi_Object = MibTableColumn
pduEnvMonitoringHumi = _PduEnvMonitoringHumi_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 3),
    _PduEnvMonitoringHumi_Type()
)
pduEnvMonitoringHumi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumi.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumi.setUnits("0.1%")


class _PduEnvMonitoringTempAlarm_Type(Integer32):
    """Custom type pduEnvMonitoringTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduEnvMonitoringTempAlarm_Type.__name__ = "Integer32"
_PduEnvMonitoringTempAlarm_Object = MibTableColumn
pduEnvMonitoringTempAlarm = _PduEnvMonitoringTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 4),
    _PduEnvMonitoringTempAlarm_Type()
)
pduEnvMonitoringTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempAlarm.setStatus("mandatory")


class _PduEnvMonitoringHumiAlarm_Type(Integer32):
    """Custom type pduEnvMonitoringHumiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduEnvMonitoringHumiAlarm_Type.__name__ = "Integer32"
_PduEnvMonitoringHumiAlarm_Object = MibTableColumn
pduEnvMonitoringHumiAlarm = _PduEnvMonitoringHumiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 5),
    _PduEnvMonitoringHumiAlarm_Type()
)
pduEnvMonitoringHumiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiAlarm.setStatus("mandatory")


class _PduEnvMonitoringAlarm1_Type(Integer32):
    """Custom type pduEnvMonitoringAlarm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("inactive", 2),
          ("active", 3))
    )


_PduEnvMonitoringAlarm1_Type.__name__ = "Integer32"
_PduEnvMonitoringAlarm1_Object = MibTableColumn
pduEnvMonitoringAlarm1 = _PduEnvMonitoringAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 6),
    _PduEnvMonitoringAlarm1_Type()
)
pduEnvMonitoringAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringAlarm1.setStatus("mandatory")


class _PduEnvMonitoringAlarm2_Type(Integer32):
    """Custom type pduEnvMonitoringAlarm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("inactive", 2),
          ("active", 3))
    )


_PduEnvMonitoringAlarm2_Type.__name__ = "Integer32"
_PduEnvMonitoringAlarm2_Object = MibTableColumn
pduEnvMonitoringAlarm2 = _PduEnvMonitoringAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1, 7),
    _PduEnvMonitoringAlarm2_Type()
)
pduEnvMonitoringAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringAlarm2.setStatus("mandatory")
_PduEmdCfgTable_Object = MibTable
pduEmdCfgTable = _PduEmdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2)
)
if mibBuilder.loadTexts:
    pduEmdCfgTable.setStatus("mandatory")
_PduEnvMonitoringCfg_Object = MibTableRow
pduEnvMonitoringCfg = _PduEnvMonitoringCfg_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1)
)
pduEnvMonitoringCfg.setIndexNames(
    (0, "PWTv1-MIB", "pduEnvCfgIndex"),
)
if mibBuilder.loadTexts:
    pduEnvMonitoringCfg.setStatus("mandatory")


class _PduEnvCfgIndex_Type(Integer32):
    """Custom type pduEnvCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PduEnvCfgIndex_Type.__name__ = "Integer32"
_PduEnvCfgIndex_Object = MibTableColumn
pduEnvCfgIndex = _PduEnvCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 1),
    _PduEnvCfgIndex_Type()
)
pduEnvCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvCfgIndex.setStatus("mandatory")


class _PduEnvMonitoringControl_Type(Integer32):
    """Custom type pduEnvMonitoringControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEnvMonitoringControl_Type.__name__ = "Integer32"
_PduEnvMonitoringControl_Object = MibTableColumn
pduEnvMonitoringControl = _PduEnvMonitoringControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 2),
    _PduEnvMonitoringControl_Type()
)
pduEnvMonitoringControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringControl.setStatus("mandatory")
_PduEnvMonitoringTempHighCritical_Type = Integer32
_PduEnvMonitoringTempHighCritical_Object = MibTableColumn
pduEnvMonitoringTempHighCritical = _PduEnvMonitoringTempHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 3),
    _PduEnvMonitoringTempHighCritical_Type()
)
pduEnvMonitoringTempHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighCritical.setUnits("degC")
_PduEnvMonitoringTempHighWarning_Type = Integer32
_PduEnvMonitoringTempHighWarning_Object = MibTableColumn
pduEnvMonitoringTempHighWarning = _PduEnvMonitoringTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 4),
    _PduEnvMonitoringTempHighWarning_Type()
)
pduEnvMonitoringTempHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighWarning.setUnits("degC")
_PduEnvMonitoringTempLowCritical_Type = Integer32
_PduEnvMonitoringTempLowCritical_Object = MibTableColumn
pduEnvMonitoringTempLowCritical = _PduEnvMonitoringTempLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 5),
    _PduEnvMonitoringTempLowCritical_Type()
)
pduEnvMonitoringTempLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowCritical.setUnits("degC")
_PduEnvMonitoringTempLowWarning_Type = Integer32
_PduEnvMonitoringTempLowWarning_Object = MibTableColumn
pduEnvMonitoringTempLowWarning = _PduEnvMonitoringTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 6),
    _PduEnvMonitoringTempLowWarning_Type()
)
pduEnvMonitoringTempLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowWarning.setUnits("degC")
_PduEnvMonitoringTempHystersis_Type = Integer32
_PduEnvMonitoringTempHystersis_Object = MibTableColumn
pduEnvMonitoringTempHystersis = _PduEnvMonitoringTempHystersis_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 7),
    _PduEnvMonitoringTempHystersis_Type()
)
pduEnvMonitoringTempHystersis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHystersis.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHystersis.setUnits("degC")
_PduEnvMonitoringTempOffset_Type = Integer32
_PduEnvMonitoringTempOffset_Object = MibTableColumn
pduEnvMonitoringTempOffset = _PduEnvMonitoringTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 8),
    _PduEnvMonitoringTempOffset_Type()
)
pduEnvMonitoringTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempOffset.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempOffset.setUnits("degC")
_PduEnvMonitoringHumiHighCritical_Type = Integer32
_PduEnvMonitoringHumiHighCritical_Object = MibTableColumn
pduEnvMonitoringHumiHighCritical = _PduEnvMonitoringHumiHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 9),
    _PduEnvMonitoringHumiHighCritical_Type()
)
pduEnvMonitoringHumiHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighCritical.setUnits("0.1%")
_PduEnvMonitoringHumiHighWarning_Type = Integer32
_PduEnvMonitoringHumiHighWarning_Object = MibTableColumn
pduEnvMonitoringHumiHighWarning = _PduEnvMonitoringHumiHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 10),
    _PduEnvMonitoringHumiHighWarning_Type()
)
pduEnvMonitoringHumiHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighWarning.setUnits("0.1%")
_PduEnvMonitoringHumiLowCritical_Type = Integer32
_PduEnvMonitoringHumiLowCritical_Object = MibTableColumn
pduEnvMonitoringHumiLowCritical = _PduEnvMonitoringHumiLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 11),
    _PduEnvMonitoringHumiLowCritical_Type()
)
pduEnvMonitoringHumiLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowCritical.setUnits("0.1%")
_PduEnvMonitoringHumiLowWarning_Type = Integer32
_PduEnvMonitoringHumiLowWarning_Object = MibTableColumn
pduEnvMonitoringHumiLowWarning = _PduEnvMonitoringHumiLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 12),
    _PduEnvMonitoringHumiLowWarning_Type()
)
pduEnvMonitoringHumiLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowWarning.setUnits("0.1%")
_PduEnvMonitoringHumiHystersis_Type = Integer32
_PduEnvMonitoringHumiHystersis_Object = MibTableColumn
pduEnvMonitoringHumiHystersis = _PduEnvMonitoringHumiHystersis_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 13),
    _PduEnvMonitoringHumiHystersis_Type()
)
pduEnvMonitoringHumiHystersis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHystersis.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHystersis.setUnits("0.1%")
_PduEnvMonitoringHumiOffset_Type = Integer32
_PduEnvMonitoringHumiOffset_Object = MibTableColumn
pduEnvMonitoringHumiOffset = _PduEnvMonitoringHumiOffset_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 14),
    _PduEnvMonitoringHumiOffset_Type()
)
pduEnvMonitoringHumiOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiOffset.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiOffset.setUnits("0.1%")


class _PduEnvMonitoringAlarm1Setup_Type(Integer32):
    """Custom type pduEnvMonitoringAlarm1Setup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("no", 2),
          ("nc", 3))
    )


_PduEnvMonitoringAlarm1Setup_Type.__name__ = "Integer32"
_PduEnvMonitoringAlarm1Setup_Object = MibTableColumn
pduEnvMonitoringAlarm1Setup = _PduEnvMonitoringAlarm1Setup_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 15),
    _PduEnvMonitoringAlarm1Setup_Type()
)
pduEnvMonitoringAlarm1Setup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringAlarm1Setup.setStatus("mandatory")


class _PduEnvMonitoringAlarm2Setup_Type(Integer32):
    """Custom type pduEnvMonitoringAlarm2Setup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("no", 2),
          ("nc", 3))
    )


_PduEnvMonitoringAlarm2Setup_Type.__name__ = "Integer32"
_PduEnvMonitoringAlarm2Setup_Object = MibTableColumn
pduEnvMonitoringAlarm2Setup = _PduEnvMonitoringAlarm2Setup_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1, 16),
    _PduEnvMonitoringAlarm2Setup_Type()
)
pduEnvMonitoringAlarm2Setup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringAlarm2Setup.setStatus("mandatory")
_PduTraps_ObjectIdentity = ObjectIdentity
pduTraps = _PduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2)
)

# Managed Objects groups


# Notification objects

pduSystemColdBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 1)
)
if mibBuilder.loadTexts:
    pduSystemColdBoot.setStatus(
        ""
    )

pduSystemWarmBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 2)
)
if mibBuilder.loadTexts:
    pduSystemWarmBoot.setStatus(
        ""
    )

pduSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 3)
)
if mibBuilder.loadTexts:
    pduSystemRestart.setStatus(
        ""
    )

pduResetToDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 4)
)
if mibBuilder.loadTexts:
    pduResetToDefault.setStatus(
        ""
    )

pduFirmUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 5)
)
if mibBuilder.loadTexts:
    pduFirmUpgrade.setStatus(
        ""
    )

pduSystemLogClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 6)
)
if mibBuilder.loadTexts:
    pduSystemLogClear.setStatus(
        ""
    )

pduEventlogClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 7)
)
if mibBuilder.loadTexts:
    pduEventlogClear.setStatus(
        ""
    )

pduInletHistoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 8)
)
if mibBuilder.loadTexts:
    pduInletHistoryClear.setStatus(
        ""
    )

pduOutletHistoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 9)
)
if mibBuilder.loadTexts:
    pduOutletHistoryClear.setStatus(
        ""
    )

pduSystemTimeChangeUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 10)
)
if mibBuilder.loadTexts:
    pduSystemTimeChangeUser.setStatus(
        ""
    )

pduSystemTimeChangeNtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 11)
)
if mibBuilder.loadTexts:
    pduSystemTimeChangeNtp.setStatus(
        ""
    )

pduSystemTimeChangeRtc = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 12)
)
if mibBuilder.loadTexts:
    pduSystemTimeChangeRtc.setStatus(
        ""
    )

pduMailTestPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 13)
)
if mibBuilder.loadTexts:
    pduMailTestPass.setStatus(
        ""
    )

pduMailTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 14)
)
if mibBuilder.loadTexts:
    pduMailTestFail.setStatus(
        ""
    )

pduMailSentPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 15)
)
if mibBuilder.loadTexts:
    pduMailSentPass.setStatus(
        ""
    )

pduMailSentFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 16)
)
if mibBuilder.loadTexts:
    pduMailSentFail.setStatus(
        ""
    )

pduSystemCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 17)
)
if mibBuilder.loadTexts:
    pduSystemCfgChange.setStatus(
        ""
    )

pduSystemParamImport = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 18)
)
if mibBuilder.loadTexts:
    pduSystemParamImport.setStatus(
        ""
    )

pduInletCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 19)
)
if mibBuilder.loadTexts:
    pduInletCommLost.setStatus(
        ""
    )

pduInletCommRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 20)
)
if mibBuilder.loadTexts:
    pduInletCommRestore.setStatus(
        ""
    )

pduOutletCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 21)
)
if mibBuilder.loadTexts:
    pduOutletCommLost.setStatus(
        ""
    )

pduOutletCommRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 22)
)
if mibBuilder.loadTexts:
    pduOutletCommRestore.setStatus(
        ""
    )

pduOutletOnUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 23)
)
if mibBuilder.loadTexts:
    pduOutletOnUser.setStatus(
        ""
    )

pduOutletOnSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 24)
)
if mibBuilder.loadTexts:
    pduOutletOnSchedule.setStatus(
        ""
    )

pduOutletOffUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 25)
)
if mibBuilder.loadTexts:
    pduOutletOffUser.setStatus(
        ""
    )

pduOutletOffSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 26)
)
if mibBuilder.loadTexts:
    pduOutletOffSchedule.setStatus(
        ""
    )

pduOutletRebootUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 27)
)
if mibBuilder.loadTexts:
    pduOutletRebootUser.setStatus(
        ""
    )

pduOutletRebootSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 28)
)
if mibBuilder.loadTexts:
    pduOutletRebootSchedule.setStatus(
        ""
    )

pduInletEnergyReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 29)
)
if mibBuilder.loadTexts:
    pduInletEnergyReset.setStatus(
        ""
    )

pduOutletEnergyReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 30)
)
if mibBuilder.loadTexts:
    pduOutletEnergyReset.setStatus(
        ""
    )

pduSetUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 31)
)
if mibBuilder.loadTexts:
    pduSetUser.setStatus(
        ""
    )

pduDeletUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 32)
)
if mibBuilder.loadTexts:
    pduDeletUser.setStatus(
        ""
    )

pduUpgradeInletSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 33)
)
if mibBuilder.loadTexts:
    pduUpgradeInletSuccess.setStatus(
        ""
    )

pduUpgradeInletFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 34)
)
if mibBuilder.loadTexts:
    pduUpgradeInletFail.setStatus(
        ""
    )

pduUpgradeOutletSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 35)
)
if mibBuilder.loadTexts:
    pduUpgradeOutletSuccess.setStatus(
        ""
    )

pduUpgradeOutletFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 36)
)
if mibBuilder.loadTexts:
    pduUpgradeOutletFail.setStatus(
        ""
    )

pduEmdHistoryLogClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 37)
)
if mibBuilder.loadTexts:
    pduEmdHistoryLogClear.setStatus(
        ""
    )

pduAccountResetDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 38)
)
if mibBuilder.loadTexts:
    pduAccountResetDefault.setStatus(
        ""
    )

pduUpgradeExtEmdSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 39)
)
if mibBuilder.loadTexts:
    pduUpgradeExtEmdSuccess.setStatus(
        ""
    )

pduUpgradeExtEmdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 40)
)
if mibBuilder.loadTexts:
    pduUpgradeExtEmdFail.setStatus(
        ""
    )

pduGroupOutletChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 41)
)
if mibBuilder.loadTexts:
    pduGroupOutletChanged.setStatus(
        ""
    )

pduScheduleOutletChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 42)
)
if mibBuilder.loadTexts:
    pduScheduleOutletChanged.setStatus(
        ""
    )

pduGroupChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 43)
)
if mibBuilder.loadTexts:
    pduGroupChanged.setStatus(
        ""
    )

pduSnmpConflicts = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 44)
)
if mibBuilder.loadTexts:
    pduSnmpConflicts.setStatus(
        ""
    )

pduInletEnergyResetPhase1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 45)
)
if mibBuilder.loadTexts:
    pduInletEnergyResetPhase1.setStatus(
        ""
    )

pduInletEnergyResetPhase2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 46)
)
if mibBuilder.loadTexts:
    pduInletEnergyResetPhase2.setStatus(
        ""
    )

pduInletEnergyResetPhase3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 47)
)
if mibBuilder.loadTexts:
    pduInletEnergyResetPhase3.setStatus(
        ""
    )

pduInletREnergyReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 48)
)
if mibBuilder.loadTexts:
    pduInletREnergyReset.setStatus(
        ""
    )

pduInletREnergyResetPhase1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 49)
)
if mibBuilder.loadTexts:
    pduInletREnergyResetPhase1.setStatus(
        ""
    )

pduInletREnergyResetPhase2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 50)
)
if mibBuilder.loadTexts:
    pduInletREnergyResetPhase2.setStatus(
        ""
    )

pduInletREnergyResetPhase3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 51)
)
if mibBuilder.loadTexts:
    pduInletREnergyResetPhase3.setStatus(
        ""
    )

pduEmdTempHighWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 101)
)
if mibBuilder.loadTexts:
    pduEmdTempHighWarnToNormal.setStatus(
        ""
    )

pduEmdTempHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 102)
)
if mibBuilder.loadTexts:
    pduEmdTempHighWarn.setStatus(
        ""
    )

pduEmdTempLowWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 103)
)
if mibBuilder.loadTexts:
    pduEmdTempLowWarnToNormal.setStatus(
        ""
    )

pduEmdTempLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 104)
)
if mibBuilder.loadTexts:
    pduEmdTempLowWarn.setStatus(
        ""
    )

pduEmdTempHighCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 105)
)
if mibBuilder.loadTexts:
    pduEmdTempHighCritToWarn.setStatus(
        ""
    )

pduEmdTempHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 106)
)
if mibBuilder.loadTexts:
    pduEmdTempHighCritical.setStatus(
        ""
    )

pduEmdTempLowCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 107)
)
if mibBuilder.loadTexts:
    pduEmdTempLowCritToWarn.setStatus(
        ""
    )

pduEmdTempLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 108)
)
if mibBuilder.loadTexts:
    pduEmdTempLowCritical.setStatus(
        ""
    )

pduEmdHumiHighWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 109)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighWarnToNormal.setStatus(
        ""
    )

pduEmdHumiHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 110)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighWarn.setStatus(
        ""
    )

pduEmdHumiLowWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 111)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowWarnToNormal.setStatus(
        ""
    )

pduEmdHumiLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 112)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowWarn.setStatus(
        ""
    )

pduEmdHumiHighCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 113)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighCritToWarn.setStatus(
        ""
    )

pduEmdHumiHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 114)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighCritical.setStatus(
        ""
    )

pduEmdHumiLowCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 115)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowCritToWarn.setStatus(
        ""
    )

pduEmdHumiLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 116)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowCritical.setStatus(
        ""
    )

pduEmdAlarm1NotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 117)
)
if mibBuilder.loadTexts:
    pduEmdAlarm1NotActive.setStatus(
        ""
    )

pduEmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 118)
)
if mibBuilder.loadTexts:
    pduEmdAlarm1Active.setStatus(
        ""
    )

pduEmdAlarm2NotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 119)
)
if mibBuilder.loadTexts:
    pduEmdAlarm2NotActive.setStatus(
        ""
    )

pduEmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 120)
)
if mibBuilder.loadTexts:
    pduEmdAlarm2Active.setStatus(
        ""
    )

pduRs485Online = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 121)
)
if mibBuilder.loadTexts:
    pduRs485Online.setStatus(
        ""
    )

pduRs485Offline = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 122)
)
if mibBuilder.loadTexts:
    pduRs485Offline.setStatus(
        ""
    )

pduInletLoadCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 123)
)
if mibBuilder.loadTexts:
    pduInletLoadCritToWarn.setStatus(
        ""
    )

pduInletLoadCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 124)
)
if mibBuilder.loadTexts:
    pduInletLoadCritical.setStatus(
        ""
    )

pduInletLoadWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 125)
)
if mibBuilder.loadTexts:
    pduInletLoadWarnToNormal.setStatus(
        ""
    )

pduInletLoadWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 126)
)
if mibBuilder.loadTexts:
    pduInletLoadWarn.setStatus(
        ""
    )

pduInletCurrPhase1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 127)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 128)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1Critical.setStatus(
        ""
    )

pduInletCurrPhase1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 129)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 130)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1Warn.setStatus(
        ""
    )

pduInletCurrPhase2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 131)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 132)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2Critical.setStatus(
        ""
    )

pduInletCurrPhase2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 133)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 134)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2Warn.setStatus(
        ""
    )

pduInletCurrPhase3CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 135)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase3Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 136)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3Critical.setStatus(
        ""
    )

pduInletCurrPhase3WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 137)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase3Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 138)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3Warn.setStatus(
        ""
    )

pduInletVoltPhase1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 139)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 140)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1Critical.setStatus(
        ""
    )

pduInletVoltPhase1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 141)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 142)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1Warn.setStatus(
        ""
    )

pduInletVoltPhase2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 143)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 144)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2Critical.setStatus(
        ""
    )

pduInletVoltPhase2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 145)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 146)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2Warn.setStatus(
        ""
    )

pduInletVoltPhase3CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 147)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase3Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 148)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3Critical.setStatus(
        ""
    )

pduInletVoltPhase3WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 149)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase3Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 150)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3Warn.setStatus(
        ""
    )

pduOutletCurrCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 151)
)
if mibBuilder.loadTexts:
    pduOutletCurrCritToWarn.setStatus(
        ""
    )

pduOutletCurrCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 152)
)
if mibBuilder.loadTexts:
    pduOutletCurrCritical.setStatus(
        ""
    )

pduOutletCurrWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 153)
)
if mibBuilder.loadTexts:
    pduOutletCurrWarnToNormal.setStatus(
        ""
    )

pduOutletCurrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 154)
)
if mibBuilder.loadTexts:
    pduOutletCurrWarn.setStatus(
        ""
    )

pduOutletPwrCritTOWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 155)
)
if mibBuilder.loadTexts:
    pduOutletPwrCritTOWarn.setStatus(
        ""
    )

pduOutletPwrCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 156)
)
if mibBuilder.loadTexts:
    pduOutletPwrCritical.setStatus(
        ""
    )

pduOutletPwrWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 157)
)
if mibBuilder.loadTexts:
    pduOutletPwrWarnToNormal.setStatus(
        ""
    )

pduOutletPwrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 158)
)
if mibBuilder.loadTexts:
    pduOutletPwrWarn.setStatus(
        ""
    )

pduAlarm1Disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 159)
)
if mibBuilder.loadTexts:
    pduAlarm1Disabled.setStatus(
        ""
    )

pduAlarm2Disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 160)
)
if mibBuilder.loadTexts:
    pduAlarm2Disabled.setStatus(
        ""
    )

pduIntetResidualCurrect1Occured = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 161)
)
if mibBuilder.loadTexts:
    pduIntetResidualCurrect1Occured.setStatus(
        ""
    )

pduIntetResidualCurrect1Remove = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 162)
)
if mibBuilder.loadTexts:
    pduIntetResidualCurrect1Remove.setStatus(
        ""
    )

pduInletLoadBalanceCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 163)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceCritToWarn.setStatus(
        ""
    )

pduInletLoadBalanceCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 164)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceCritical.setStatus(
        ""
    )

pduInletLoadBalanceWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 165)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceWarnToNormal.setStatus(
        ""
    )

pduInletLoadBalanceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 166)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceWarn.setStatus(
        ""
    )

pduInletAcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 167)
)
if mibBuilder.loadTexts:
    pduInletAcFail.setStatus(
        ""
    )

pduInletAcRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 168)
)
if mibBuilder.loadTexts:
    pduInletAcRestore.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PWTv1-MIB",
    **{"powertek": powertek,
       "product": product,
       "pdu": pdu,
       "pwt": pwt,
       "pduObjects": pduObjects,
       "pduIdent": pduIdent,
       "pduIdentAgentSoftwareVersion": pduIdentAgentSoftwareVersion,
       "pduIdentSerialNumber": pduIdentSerialNumber,
       "pduNetwork": pduNetwork,
       "pduNetworkTcpip": pduNetworkTcpip,
       "pduNetworkTcpipDhcpControl": pduNetworkTcpipDhcpControl,
       "pduNetworkTcpipIpv4": pduNetworkTcpipIpv4,
       "pduNetworkTcpipIpv4Address": pduNetworkTcpipIpv4Address,
       "pduNetworkTcpipIpv4Gateway": pduNetworkTcpipIpv4Gateway,
       "pduNetworkTcpipIpv4Subnet": pduNetworkTcpipIpv4Subnet,
       "pduNetworkTcpipIpv4PrimaryDNS": pduNetworkTcpipIpv4PrimaryDNS,
       "pduNetworkTcpipIpv4SecondaryDNS": pduNetworkTcpipIpv4SecondaryDNS,
       "pduNetworkTcpipIpv6": pduNetworkTcpipIpv6,
       "pduNetworkTcpipIpv6Control": pduNetworkTcpipIpv6Control,
       "pduNetworkTcpipIpv6AutoConfig": pduNetworkTcpipIpv6AutoConfig,
       "pduNetworkTcpipIpv6Address": pduNetworkTcpipIpv6Address,
       "pduNetworkTcpipIpv6Prefix": pduNetworkTcpipIpv6Prefix,
       "pduNetworkTcpipIpv6Router": pduNetworkTcpipIpv6Router,
       "pduNetworkTcpipIpv6PrimaryDNS": pduNetworkTcpipIpv6PrimaryDNS,
       "pduNetworkTcpipIpv6SecondaryDNS": pduNetworkTcpipIpv6SecondaryDNS,
       "pduNetworkSecurity": pduNetworkSecurity,
       "pduNetworkSecurityControl": pduNetworkSecurityControl,
       "pduNetworkSecuritySsh": pduNetworkSecuritySsh,
       "pduNetworkSecuritySshControl": pduNetworkSecuritySshControl,
       "pduNetworkSecuritySshInterval": pduNetworkSecuritySshInterval,
       "pduNetworkSecuritySshFailTimes": pduNetworkSecuritySshFailTimes,
       "pduNetworkSecuritySshBlock": pduNetworkSecuritySshBlock,
       "pduNetworkSecuritySnmp": pduNetworkSecuritySnmp,
       "pduNetworkSecuritySnmpControl": pduNetworkSecuritySnmpControl,
       "pduNetworkSecuritySnmpInterval": pduNetworkSecuritySnmpInterval,
       "pduNetworkSecuritySnmpFailTimes": pduNetworkSecuritySnmpFailTimes,
       "pduNetworkSecuritySnmpBlock": pduNetworkSecuritySnmpBlock,
       "pduNetworkSecurityHttp": pduNetworkSecurityHttp,
       "pduNetworkSecurityHttpControl": pduNetworkSecurityHttpControl,
       "pduNetworkSecurityHttpInterval": pduNetworkSecurityHttpInterval,
       "pduNetworkSecurityHttpFailTimes": pduNetworkSecurityHttpFailTimes,
       "pduNetworkSecurityHttpBlock": pduNetworkSecurityHttpBlock,
       "pduNetworkService": pduNetworkService,
       "pduNetworkServiceSsh": pduNetworkServiceSsh,
       "pduNetworkServiceSshControl": pduNetworkServiceSshControl,
       "pduNetworkServiceSshPort": pduNetworkServiceSshPort,
       "pduNetworkServiceSsl": pduNetworkServiceSsl,
       "pduNetworkServiceSslControl": pduNetworkServiceSslControl,
       "pduNetworkServiceSslPort": pduNetworkServiceSslPort,
       "pduNetworkServiceSslForce": pduNetworkServiceSslForce,
       "pduNetworkServicePingControl": pduNetworkServicePingControl,
       "pduNetworkServiceRadius": pduNetworkServiceRadius,
       "pduNetworkServiceRadiusControl": pduNetworkServiceRadiusControl,
       "pduNetworkServiceRadiusIp": pduNetworkServiceRadiusIp,
       "pduNetworkServiceRadiusPort": pduNetworkServiceRadiusPort,
       "pduNetworkServiceRadiusSecretKey": pduNetworkServiceRadiusSecretKey,
       "pduNetworkServiceRadiusTimeout": pduNetworkServiceRadiusTimeout,
       "pduNetworkServiceRadiusRetry": pduNetworkServiceRadiusRetry,
       "pduSystem": pduSystem,
       "pduSystemName": pduSystemName,
       "pduSystemContact": pduSystemContact,
       "pduSystemLocation": pduSystemLocation,
       "pduSystemLogInterval": pduSystemLogInterval,
       "pduSystemWebRefresh": pduSystemWebRefresh,
       "pduSystemTime": pduSystemTime,
       "pduSystemTimeDisplay": pduSystemTimeDisplay,
       "pduSystemTimeZone": pduSystemTimeZone,
       "pduSystemTimeFormat": pduSystemTimeFormat,
       "pduSystemTimeSetting": pduSystemTimeSetting,
       "pduSystemTimeDayLightSaving": pduSystemTimeDayLightSaving,
       "pduSystemTimeManual": pduSystemTimeManual,
       "pduSystemTimeManualDate": pduSystemTimeManualDate,
       "pduSystemTimeManualTime": pduSystemTimeManualTime,
       "pduSystemTimeNtp": pduSystemTimeNtp,
       "pduSystemTimeNtpControl": pduSystemTimeNtpControl,
       "pduSystemTimeNtpServer": pduSystemTimeNtpServer,
       "pduSystemTimeNtpSyncInterval": pduSystemTimeNtpSyncInterval,
       "pduSystemTimeNtpSyncUnit": pduSystemTimeNtpSyncUnit,
       "pduSystemResetToDefault": pduSystemResetToDefault,
       "pduSystemReboot": pduSystemReboot,
       "pduSNMP": pduSNMP,
       "pduSnmpControl": pduSnmpControl,
       "pduSnmpPort": pduSnmpPort,
       "pduSnmpVersion": pduSnmpVersion,
       "pduSnmpTrapsReceiversTable": pduSnmpTrapsReceiversTable,
       "pduSnmpTrapsReceiversEntry": pduSnmpTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverEventLevel": receiverEventLevel,
       "receiverSnmpVer": receiverSnmpVer,
       "receiverDescription": receiverDescription,
       "pduEmail": pduEmail,
       "pduEmailServer": pduEmailServer,
       "pduEmailPort": pduEmailPort,
       "pduEmailSenderEmail": pduEmailSenderEmail,
       "pduEmailPrefix": pduEmailPrefix,
       "pduEmailAuthControl": pduEmailAuthControl,
       "pduEmailAuthUsername": pduEmailAuthUsername,
       "pduEmailAuthPassword": pduEmailAuthPassword,
       "pduEmailReceiversTable": pduEmailReceiversTable,
       "pduEmailReceiversEntry": pduEmailReceiversEntry,
       "mailRecvIndex": mailRecvIndex,
       "mailRecvReceiverAddr": mailRecvReceiverAddr,
       "mailRecvEmailType": mailRecvEmailType,
       "mailRecvEventLevel": mailRecvEventLevel,
       "mailRecvDescription": mailRecvDescription,
       "pduPwrMonitoring": pduPwrMonitoring,
       "pduPwrMonitoringInlet": pduPwrMonitoringInlet,
       "pduPwrMonitoringInletNum": pduPwrMonitoringInletNum,
       "pduPwrMonitoringInletStatusTable": pduPwrMonitoringInletStatusTable,
       "pduPwrMonitoringInletStatusEntry": pduPwrMonitoringInletStatusEntry,
       "inletIndex": inletIndex,
       "inletPowerAll": inletPowerAll,
       "inletResetFrom": inletResetFrom,
       "inletEnergy": inletEnergy,
       "inletStatus": inletStatus,
       "inletCurrPhase1b1": inletCurrPhase1b1,
       "inletCurrPhase2b1": inletCurrPhase2b1,
       "inletCurrPhase3b1": inletCurrPhase3b1,
       "inletCurrPhase1b2": inletCurrPhase1b2,
       "inletCurrPhase2b2": inletCurrPhase2b2,
       "inletCurrPhase3b2": inletCurrPhase3b2,
       "inletCurrPhase1": inletCurrPhase1,
       "inletCurrPhase2": inletCurrPhase2,
       "inletCurrPhase3": inletCurrPhase3,
       "inletVoltPhase1": inletVoltPhase1,
       "inletVoltPhase2": inletVoltPhase2,
       "inletVoltPhase3": inletVoltPhase3,
       "inletPwrFactorPhase1b1": inletPwrFactorPhase1b1,
       "inletPwrFactorPhase2b1": inletPwrFactorPhase2b1,
       "inletPwrFactorPhase3b1": inletPwrFactorPhase3b1,
       "inletPwrFactorPhase1b2": inletPwrFactorPhase1b2,
       "inletPwrFactorPhase2b2": inletPwrFactorPhase2b2,
       "inletPwrFactorPhase3b2": inletPwrFactorPhase3b2,
       "inletPowerPhase1b1": inletPowerPhase1b1,
       "inletPowerPhase2b1": inletPowerPhase2b1,
       "inletPowerPhase3b1": inletPowerPhase3b1,
       "inletPowerPhase1b2": inletPowerPhase1b2,
       "inletPowerPhase2b2": inletPowerPhase2b2,
       "inletPowerPhase3b2": inletPowerPhase3b2,
       "inletPowerPhase1": inletPowerPhase1,
       "inletPowerPhase2": inletPowerPhase2,
       "inletPowerPhase3": inletPowerPhase3,
       "inletStatusPhase1": inletStatusPhase1,
       "inletStatusPhase2": inletStatusPhase2,
       "inletStatusPhase3": inletStatusPhase3,
       "inletAppPowerPhase1b1": inletAppPowerPhase1b1,
       "inletAppPowerPhase2b1": inletAppPowerPhase2b1,
       "inletAppPowerPhase3b1": inletAppPowerPhase3b1,
       "inletAppPowerPhase1b2": inletAppPowerPhase1b2,
       "inletAppPowerPhase2b2": inletAppPowerPhase2b2,
       "inletAppPowerPhase3b2": inletAppPowerPhase3b2,
       "inletAppPowerPhase1": inletAppPowerPhase1,
       "inletAppPowerPhase2": inletAppPowerPhase2,
       "inletAppPowerPhase3": inletAppPowerPhase3,
       "inletAppRcmCurrent": inletAppRcmCurrent,
       "inletLoadBalance": inletLoadBalance,
       "inletLoadBalanceStatus": inletLoadBalanceStatus,
       "inletResetFromPhase1": inletResetFromPhase1,
       "inletEnergyPhase1": inletEnergyPhase1,
       "inletResetFromPhase2": inletResetFromPhase2,
       "inletEnergyPhase2": inletEnergyPhase2,
       "inletResetFromPhase3": inletResetFromPhase3,
       "inletEnergyPhase3": inletEnergyPhase3,
       "inletFreqPhase1": inletFreqPhase1,
       "inletFreqPhase2": inletFreqPhase2,
       "inletFreqPhase3": inletFreqPhase3,
       "inletReactiveResetFrom": inletReactiveResetFrom,
       "inletReactiveEnergy": inletReactiveEnergy,
       "inletReactiveResetFromPhase1": inletReactiveResetFromPhase1,
       "inletReactiveEnergyPhase1": inletReactiveEnergyPhase1,
       "inletReactiveResetFromPhase2": inletReactiveResetFromPhase2,
       "inletReactiveEnergyPhase2": inletReactiveEnergyPhase2,
       "inletReactiveResetFromPhase3": inletReactiveResetFromPhase3,
       "inletReactiveEnergyPhase3": inletReactiveEnergyPhase3,
       "inletVarPowerPhase1b1": inletVarPowerPhase1b1,
       "inletVarPowerPhase2b1": inletVarPowerPhase2b1,
       "inletVarPowerPhase3b1": inletVarPowerPhase3b1,
       "inletVarPowerPhase1b2": inletVarPowerPhase1b2,
       "inletVarPowerPhase2b2": inletVarPowerPhase2b2,
       "inletVarPowerPhase3b2": inletVarPowerPhase3b2,
       "inletVarPowerPhase1": inletVarPowerPhase1,
       "inletVarPowerPhase2": inletVarPowerPhase2,
       "inletVarPowerPhase3": inletVarPowerPhase3,
       "pduPwrMonitoringInletCfgTable": pduPwrMonitoringInletCfgTable,
       "pduPwrMonitoringInletCfgEntry": pduPwrMonitoringInletCfgEntry,
       "inletCfgIndex": inletCfgIndex,
       "inletCfgLoadCritical": inletCfgLoadCritical,
       "inletCfgLoadWarning": inletCfgLoadWarning,
       "inletCfgCurrCritPhase1b1": inletCfgCurrCritPhase1b1,
       "inletCfgCurrCritPhase2b1": inletCfgCurrCritPhase2b1,
       "inletCfgCurrCritPhase3b1": inletCfgCurrCritPhase3b1,
       "inletCfgCurrCritPhase1b2": inletCfgCurrCritPhase1b2,
       "inletCfgCurrCritPhase2b2": inletCfgCurrCritPhase2b2,
       "inletCfgCurrCritPhase3b2": inletCfgCurrCritPhase3b2,
       "inletCfgCurrWarnPhase1b1": inletCfgCurrWarnPhase1b1,
       "inletCfgCurrWarnPhase2b1": inletCfgCurrWarnPhase2b1,
       "inletCfgCurrWarnPhase3b1": inletCfgCurrWarnPhase3b1,
       "inletCfgCurrWarnPhase1b2": inletCfgCurrWarnPhase1b2,
       "inletCfgCurrWarnPhase2b2": inletCfgCurrWarnPhase2b2,
       "inletCfgCurrWarnPhase3b2": inletCfgCurrWarnPhase3b2,
       "inletCfgVoltCritPhase1": inletCfgVoltCritPhase1,
       "inletCfgVoltCritPhase2": inletCfgVoltCritPhase2,
       "inletCfgVoltCritPhase3": inletCfgVoltCritPhase3,
       "inletCfgVoltWarnPhase1": inletCfgVoltWarnPhase1,
       "inletCfgVoltWarnPhase2": inletCfgVoltWarnPhase2,
       "inletCfgVoltWarnPhase3": inletCfgVoltWarnPhase3,
       "inletCfgTotalCurrCritPhase1": inletCfgTotalCurrCritPhase1,
       "inletCfgTotalCurrCritPhase2": inletCfgTotalCurrCritPhase2,
       "inletCfgTotalCurrCritPhase3": inletCfgTotalCurrCritPhase3,
       "inletCfgTotalCurrWarnPhase1": inletCfgTotalCurrWarnPhase1,
       "inletCfgTotalCurrWarnPhase2": inletCfgTotalCurrWarnPhase2,
       "inletCfgTotalCurrWarnPhase3": inletCfgTotalCurrWarnPhase3,
       "inletCfgRcmCurrThreshold": inletCfgRcmCurrThreshold,
       "inletCfgLoadBalanceCrit": inletCfgLoadBalanceCrit,
       "inletCfgLoadBalanceWarn": inletCfgLoadBalanceWarn,
       "pduPwrMonitoringOutlet": pduPwrMonitoringOutlet,
       "pduPwrMonitoringOutletPduA": pduPwrMonitoringOutletPduA,
       "pduPwrMonitoringOutletNumPduA": pduPwrMonitoringOutletNumPduA,
       "pduPwrMonitoringOutletStatusTablePduA": pduPwrMonitoringOutletStatusTablePduA,
       "pduPwrMonitoringOutletStatusPduAEntry": pduPwrMonitoringOutletStatusPduAEntry,
       "outletPduAIndex": outletPduAIndex,
       "outletPduAState": outletPduAState,
       "outletPduACurrent": outletPduACurrent,
       "outletPduAPwrFactor": outletPduAPwrFactor,
       "outletPduAPower": outletPduAPower,
       "outletPduAEnergy": outletPduAEnergy,
       "outletPduAResetFrom": outletPduAResetFrom,
       "outletPduAStatus": outletPduAStatus,
       "outletPduAAppPower": outletPduAAppPower,
       "outletPduAVoltage": outletPduAVoltage,
       "pduPwrMonitoringOutletCfgTablePduA": pduPwrMonitoringOutletCfgTablePduA,
       "pduPwrMonitoringOutletCfgPduAEntry": pduPwrMonitoringOutletCfgPduAEntry,
       "outletCfgPduAIndex": outletCfgPduAIndex,
       "outletCfgPduAName": outletCfgPduAName,
       "outletCfgPduADelayOnStatus": outletCfgPduADelayOnStatus,
       "outletCfgPduADelayOnTime": outletCfgPduADelayOnTime,
       "outletCfgPduADelayOffStatus": outletCfgPduADelayOffStatus,
       "outletCfgPduADelayOffTime": outletCfgPduADelayOffTime,
       "outletCfgPduAReboot": outletCfgPduAReboot,
       "outletCfgPduAOverCurrCritical": outletCfgPduAOverCurrCritical,
       "outletCfgPduAOverCurrWarning": outletCfgPduAOverCurrWarning,
       "outletCfgPduAOverPwrCritical": outletCfgPduAOverPwrCritical,
       "outletCfgPduAOverPwrWarning": outletCfgPduAOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduA": pduPwrMonitoringOutletCtlTablePduA,
       "pduPwrMonitoringOutletCtlPduAEntry": pduPwrMonitoringOutletCtlPduAEntry,
       "outletCtlPduAIndex": outletCtlPduAIndex,
       "outletCtlPduAControl": outletCtlPduAControl,
       "pduPwrMonitoringOutletPduB": pduPwrMonitoringOutletPduB,
       "pduPwrMonitoringOutletNumPduB": pduPwrMonitoringOutletNumPduB,
       "pduPwrMonitoringOutletStatusTablePduB": pduPwrMonitoringOutletStatusTablePduB,
       "pduPwrMonitoringOutletStatusPduBEntry": pduPwrMonitoringOutletStatusPduBEntry,
       "outletPduBIndex": outletPduBIndex,
       "outletPduBState": outletPduBState,
       "outletPduBCurrent": outletPduBCurrent,
       "outletPduBPwrFactor": outletPduBPwrFactor,
       "outletPduBPower": outletPduBPower,
       "outletPduBEnergy": outletPduBEnergy,
       "outletPduBResetFrom": outletPduBResetFrom,
       "outletPduBStatus": outletPduBStatus,
       "outletPduBAppPower": outletPduBAppPower,
       "outletPduBVoltage": outletPduBVoltage,
       "pduPwrMonitoringOutletCfgTablePduB": pduPwrMonitoringOutletCfgTablePduB,
       "pduPwrMonitoringOutletCfgPduBEntry": pduPwrMonitoringOutletCfgPduBEntry,
       "outletCfgPduBIndex": outletCfgPduBIndex,
       "outletCfgPduBName": outletCfgPduBName,
       "outletCfgPduBDelayOnStatus": outletCfgPduBDelayOnStatus,
       "outletCfgPduBDelayOnTime": outletCfgPduBDelayOnTime,
       "outletCfgPduBDelayOffStatus": outletCfgPduBDelayOffStatus,
       "outletCfgPduBDelayOffTime": outletCfgPduBDelayOffTime,
       "outletCfgPduBReboot": outletCfgPduBReboot,
       "outletCfgPduBOverCurrCritical": outletCfgPduBOverCurrCritical,
       "outletCfgPduBOverCurrWarning": outletCfgPduBOverCurrWarning,
       "outletCfgPduBOverPwrCritical": outletCfgPduBOverPwrCritical,
       "outletCfgPduBOverPwrWarning": outletCfgPduBOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduB": pduPwrMonitoringOutletCtlTablePduB,
       "pduPwrMonitoringOutletCtlPduBEntry": pduPwrMonitoringOutletCtlPduBEntry,
       "outletCtlPduBIndex": outletCtlPduBIndex,
       "outletCtlPduBControl": outletCtlPduBControl,
       "pduPwrMonitoringOutletPduC": pduPwrMonitoringOutletPduC,
       "pduPwrMonitoringOutletNumPduC": pduPwrMonitoringOutletNumPduC,
       "pduPwrMonitoringOutletStatusTablePduC": pduPwrMonitoringOutletStatusTablePduC,
       "pduPwrMonitoringOutletStatusPduCEntry": pduPwrMonitoringOutletStatusPduCEntry,
       "outletPduCIndex": outletPduCIndex,
       "outletPduCState": outletPduCState,
       "outletPduCCurrent": outletPduCCurrent,
       "outletPduCPwrFactor": outletPduCPwrFactor,
       "outletPduCPower": outletPduCPower,
       "outletPduCEnergy": outletPduCEnergy,
       "outletPduCResetFrom": outletPduCResetFrom,
       "outletPduCStatus": outletPduCStatus,
       "outletPduCAppPower": outletPduCAppPower,
       "outletPduCVoltage": outletPduCVoltage,
       "pduPwrMonitoringOutletCfgTablePduC": pduPwrMonitoringOutletCfgTablePduC,
       "pduPwrMonitoringOutletCfgPduCEntry": pduPwrMonitoringOutletCfgPduCEntry,
       "outletCfgPduCIndex": outletCfgPduCIndex,
       "outletCfgPduCName": outletCfgPduCName,
       "outletCfgPduCDelayOnStatus": outletCfgPduCDelayOnStatus,
       "outletCfgPduCDelayOnTime": outletCfgPduCDelayOnTime,
       "outletCfgPduCDelayOffStatus": outletCfgPduCDelayOffStatus,
       "outletCfgPduCDelayOffTime": outletCfgPduCDelayOffTime,
       "outletCfgPduCReboot": outletCfgPduCReboot,
       "outletCfgPduCOverCurrCritical": outletCfgPduCOverCurrCritical,
       "outletCfgPduCOverCurrWarning": outletCfgPduCOverCurrWarning,
       "outletCfgPduCOverPwrCritical": outletCfgPduCOverPwrCritical,
       "outletCfgPduCOverPwrWarning": outletCfgPduCOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduC": pduPwrMonitoringOutletCtlTablePduC,
       "pduPwrMonitoringOutletCtlPduCEntry": pduPwrMonitoringOutletCtlPduCEntry,
       "outletCtlPduCIndex": outletCtlPduCIndex,
       "outletCtlPduCControl": outletCtlPduCControl,
       "pduPwrMonitoringOutletPduD": pduPwrMonitoringOutletPduD,
       "pduPwrMonitoringOutletNumPduD": pduPwrMonitoringOutletNumPduD,
       "pduPwrMonitoringOutletStatusTablePduD": pduPwrMonitoringOutletStatusTablePduD,
       "pduPwrMonitoringOutletStatusPduDEntry": pduPwrMonitoringOutletStatusPduDEntry,
       "outletPduDIndex": outletPduDIndex,
       "outletPduDState": outletPduDState,
       "outletPduDCurrent": outletPduDCurrent,
       "outletPduDPwrFactor": outletPduDPwrFactor,
       "outletPduDPower": outletPduDPower,
       "outletPduDEnergy": outletPduDEnergy,
       "outletPduDResetFrom": outletPduDResetFrom,
       "outletPduDStatus": outletPduDStatus,
       "outletPduDAppPower": outletPduDAppPower,
       "outletPduDVoltage": outletPduDVoltage,
       "pduPwrMonitoringOutletCfgTablePduD": pduPwrMonitoringOutletCfgTablePduD,
       "pduPwrMonitoringOutletCfgPduDEntry": pduPwrMonitoringOutletCfgPduDEntry,
       "outletCfgPduDIndex": outletCfgPduDIndex,
       "outletCfgPduDName": outletCfgPduDName,
       "outletCfgPduDDelayOnStatus": outletCfgPduDDelayOnStatus,
       "outletCfgPduDDelayOnTime": outletCfgPduDDelayOnTime,
       "outletCfgPduDDelayOffStatus": outletCfgPduDDelayOffStatus,
       "outletCfgPduDDelayOffTime": outletCfgPduDDelayOffTime,
       "outletCfgPduDReboot": outletCfgPduDReboot,
       "outletCfgPduDOverCurrCritical": outletCfgPduDOverCurrCritical,
       "outletCfgPduDOverCurrWarning": outletCfgPduDOverCurrWarning,
       "outletCfgPduDOverPwrCritical": outletCfgPduDOverPwrCritical,
       "outletCfgPduDOverPwrWarning": outletCfgPduDOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduD": pduPwrMonitoringOutletCtlTablePduD,
       "pduPwrMonitoringOutletCtlPduDEntry": pduPwrMonitoringOutletCtlPduDEntry,
       "outletCtlPduDIndex": outletCtlPduDIndex,
       "outletCtlPduDControl": outletCtlPduDControl,
       "pduPwrMonitoringOutletPduE": pduPwrMonitoringOutletPduE,
       "pduPwrMonitoringOutletNumPduE": pduPwrMonitoringOutletNumPduE,
       "pduPwrMonitoringOutletStatusTablePduE": pduPwrMonitoringOutletStatusTablePduE,
       "pduPwrMonitoringOutletStatusPduEEntry": pduPwrMonitoringOutletStatusPduEEntry,
       "outletPduEIndex": outletPduEIndex,
       "outletPduEState": outletPduEState,
       "outletPduECurrent": outletPduECurrent,
       "outletPduEPwrFactor": outletPduEPwrFactor,
       "outletPduEPower": outletPduEPower,
       "outletPduEEnergy": outletPduEEnergy,
       "outletPduEResetFrom": outletPduEResetFrom,
       "outletPduEStatus": outletPduEStatus,
       "outletPduEAppPower": outletPduEAppPower,
       "outletPduEVoltage": outletPduEVoltage,
       "pduPwrMonitoringOutletCfgTablePduE": pduPwrMonitoringOutletCfgTablePduE,
       "pduPwrMonitoringOutletCfgPduEEntry": pduPwrMonitoringOutletCfgPduEEntry,
       "outletCfgPduEIndex": outletCfgPduEIndex,
       "outletCfgPduEName": outletCfgPduEName,
       "outletCfgPduEDelayOnStatus": outletCfgPduEDelayOnStatus,
       "outletCfgPduEDelayOnTime": outletCfgPduEDelayOnTime,
       "outletCfgPduEDelayOffStatus": outletCfgPduEDelayOffStatus,
       "outletCfgPduEDelayOffTime": outletCfgPduEDelayOffTime,
       "outletCfgPduEReboot": outletCfgPduEReboot,
       "outletCfgPduEOverCurrCritical": outletCfgPduEOverCurrCritical,
       "outletCfgPduEOverCurrWarning": outletCfgPduEOverCurrWarning,
       "outletCfgPduEOverPwrCritical": outletCfgPduEOverPwrCritical,
       "outletCfgPduEOverPwrWarning": outletCfgPduEOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduE": pduPwrMonitoringOutletCtlTablePduE,
       "pduPwrMonitoringOutletCtlPduEEntry": pduPwrMonitoringOutletCtlPduEEntry,
       "outletCtlPduEIndex": outletCtlPduEIndex,
       "outletCtlPduEControl": outletCtlPduEControl,
       "pduPwrMonitoringOutletPduF": pduPwrMonitoringOutletPduF,
       "pduPwrMonitoringOutletNumPduF": pduPwrMonitoringOutletNumPduF,
       "pduPwrMonitoringOutletStatusTablePduF": pduPwrMonitoringOutletStatusTablePduF,
       "pduPwrMonitoringOutletStatusPduFEntry": pduPwrMonitoringOutletStatusPduFEntry,
       "outletPduFIndex": outletPduFIndex,
       "outletPduFState": outletPduFState,
       "outletPduFCurrent": outletPduFCurrent,
       "outletPduFPwrFactor": outletPduFPwrFactor,
       "outletPduFPower": outletPduFPower,
       "outletPduFEnergy": outletPduFEnergy,
       "outletPduFResetFrom": outletPduFResetFrom,
       "outletPduFStatus": outletPduFStatus,
       "outletPduFAppPower": outletPduFAppPower,
       "outletPduFVoltage": outletPduFVoltage,
       "pduPwrMonitoringOutletCfgTablePduF": pduPwrMonitoringOutletCfgTablePduF,
       "pduPwrMonitoringOutletCfgPduFEntry": pduPwrMonitoringOutletCfgPduFEntry,
       "outletCfgPduFIndex": outletCfgPduFIndex,
       "outletCfgPduFName": outletCfgPduFName,
       "outletCfgPduFDelayOnStatus": outletCfgPduFDelayOnStatus,
       "outletCfgPduFDelayOnTime": outletCfgPduFDelayOnTime,
       "outletCfgPduFDelayOffStatus": outletCfgPduFDelayOffStatus,
       "outletCfgPduFDelayOffTime": outletCfgPduFDelayOffTime,
       "outletCfgPduFReboot": outletCfgPduFReboot,
       "outletCfgPduFOverCurrCritical": outletCfgPduFOverCurrCritical,
       "outletCfgPduFOverCurrWarning": outletCfgPduFOverCurrWarning,
       "outletCfgPduFOverPwrCritical": outletCfgPduFOverPwrCritical,
       "outletCfgPduFOverPwrWarning": outletCfgPduFOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduF": pduPwrMonitoringOutletCtlTablePduF,
       "pduPwrMonitoringOutletCtlPduFEntry": pduPwrMonitoringOutletCtlPduFEntry,
       "outletCtlPduFIndex": outletCtlPduFIndex,
       "outletCtlPduFControl": outletCtlPduFControl,
       "pduPwrMonitoringOutletPduG": pduPwrMonitoringOutletPduG,
       "pduPwrMonitoringOutletNumPduG": pduPwrMonitoringOutletNumPduG,
       "pduPwrMonitoringOutletStatusTablePduG": pduPwrMonitoringOutletStatusTablePduG,
       "pduPwrMonitoringOutletStatusPduGEntry": pduPwrMonitoringOutletStatusPduGEntry,
       "outletPduGIndex": outletPduGIndex,
       "outletPduGState": outletPduGState,
       "outletPduGCurrent": outletPduGCurrent,
       "outletPduGPwrFactor": outletPduGPwrFactor,
       "outletPduGPower": outletPduGPower,
       "outletPduGEnergy": outletPduGEnergy,
       "outletPduGResetFrom": outletPduGResetFrom,
       "outletPduGStatus": outletPduGStatus,
       "outletPduGAppPower": outletPduGAppPower,
       "outletPduGVoltage": outletPduGVoltage,
       "pduPwrMonitoringOutletCfgTablePduG": pduPwrMonitoringOutletCfgTablePduG,
       "pduPwrMonitoringOutletCfgPduGEntry": pduPwrMonitoringOutletCfgPduGEntry,
       "outletCfgPduGIndex": outletCfgPduGIndex,
       "outletCfgPduGName": outletCfgPduGName,
       "outletCfgPduGDelayOnStatus": outletCfgPduGDelayOnStatus,
       "outletCfgPduGDelayOnTime": outletCfgPduGDelayOnTime,
       "outletCfgPduGDelayOffStatus": outletCfgPduGDelayOffStatus,
       "outletCfgPduGDelayOffTime": outletCfgPduGDelayOffTime,
       "outletCfgPduGReboot": outletCfgPduGReboot,
       "outletCfgPduGOverCurrCritical": outletCfgPduGOverCurrCritical,
       "outletCfgPduGOverCurrWarning": outletCfgPduGOverCurrWarning,
       "outletCfgPduGOverPwrCritical": outletCfgPduGOverPwrCritical,
       "outletCfgPduGOverPwrWarning": outletCfgPduGOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduG": pduPwrMonitoringOutletCtlTablePduG,
       "pduPwrMonitoringOutletCtlPduGEntry": pduPwrMonitoringOutletCtlPduGEntry,
       "outletCtlPduGIndex": outletCtlPduGIndex,
       "outletCtlPduGControl": outletCtlPduGControl,
       "pduPwrMonitoringOutletPduH": pduPwrMonitoringOutletPduH,
       "pduPwrMonitoringOutletNumPduH": pduPwrMonitoringOutletNumPduH,
       "pduPwrMonitoringOutletStatusTablePduH": pduPwrMonitoringOutletStatusTablePduH,
       "pduPwrMonitoringOutletStatusPduHEntry": pduPwrMonitoringOutletStatusPduHEntry,
       "outletPduHIndex": outletPduHIndex,
       "outletPduHState": outletPduHState,
       "outletPduHCurrent": outletPduHCurrent,
       "outletPduHPwrFactor": outletPduHPwrFactor,
       "outletPduHPower": outletPduHPower,
       "outletPduHEnergy": outletPduHEnergy,
       "outletPduHResetFrom": outletPduHResetFrom,
       "outletPduHStatus": outletPduHStatus,
       "outletPduHAppPower": outletPduHAppPower,
       "outletPduHVoltage": outletPduHVoltage,
       "pduPwrMonitoringOutletCfgTablePduH": pduPwrMonitoringOutletCfgTablePduH,
       "pduPwrMonitoringOutletCfgPduHEntry": pduPwrMonitoringOutletCfgPduHEntry,
       "outletCfgPduHIndex": outletCfgPduHIndex,
       "outletCfgPduHName": outletCfgPduHName,
       "outletCfgPduHDelayOnStatus": outletCfgPduHDelayOnStatus,
       "outletCfgPduHDelayOnTime": outletCfgPduHDelayOnTime,
       "outletCfgPduHDelayOffStatus": outletCfgPduHDelayOffStatus,
       "outletCfgPduHDelayOffTime": outletCfgPduHDelayOffTime,
       "outletCfgPduHReboot": outletCfgPduHReboot,
       "outletCfgPduHOverCurrCritical": outletCfgPduHOverCurrCritical,
       "outletCfgPduHOverCurrWarning": outletCfgPduHOverCurrWarning,
       "outletCfgPduHOverPwrCritical": outletCfgPduHOverPwrCritical,
       "outletCfgPduHOverPwrWarning": outletCfgPduHOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduH": pduPwrMonitoringOutletCtlTablePduH,
       "pduPwrMonitoringOutletCtlPduHEntry": pduPwrMonitoringOutletCtlPduHEntry,
       "outletCtlPduHIndex": outletCtlPduHIndex,
       "outletCtlPduHControl": outletCtlPduHControl,
       "pduEnvMonitoring": pduEnvMonitoring,
       "pduEmdStatusTable": pduEmdStatusTable,
       "pduEnvMonitoringStatus": pduEnvMonitoringStatus,
       "pduEnvStatusIndex": pduEnvStatusIndex,
       "pduEnvMonitoringTemp": pduEnvMonitoringTemp,
       "pduEnvMonitoringHumi": pduEnvMonitoringHumi,
       "pduEnvMonitoringTempAlarm": pduEnvMonitoringTempAlarm,
       "pduEnvMonitoringHumiAlarm": pduEnvMonitoringHumiAlarm,
       "pduEnvMonitoringAlarm1": pduEnvMonitoringAlarm1,
       "pduEnvMonitoringAlarm2": pduEnvMonitoringAlarm2,
       "pduEmdCfgTable": pduEmdCfgTable,
       "pduEnvMonitoringCfg": pduEnvMonitoringCfg,
       "pduEnvCfgIndex": pduEnvCfgIndex,
       "pduEnvMonitoringControl": pduEnvMonitoringControl,
       "pduEnvMonitoringTempHighCritical": pduEnvMonitoringTempHighCritical,
       "pduEnvMonitoringTempHighWarning": pduEnvMonitoringTempHighWarning,
       "pduEnvMonitoringTempLowCritical": pduEnvMonitoringTempLowCritical,
       "pduEnvMonitoringTempLowWarning": pduEnvMonitoringTempLowWarning,
       "pduEnvMonitoringTempHystersis": pduEnvMonitoringTempHystersis,
       "pduEnvMonitoringTempOffset": pduEnvMonitoringTempOffset,
       "pduEnvMonitoringHumiHighCritical": pduEnvMonitoringHumiHighCritical,
       "pduEnvMonitoringHumiHighWarning": pduEnvMonitoringHumiHighWarning,
       "pduEnvMonitoringHumiLowCritical": pduEnvMonitoringHumiLowCritical,
       "pduEnvMonitoringHumiLowWarning": pduEnvMonitoringHumiLowWarning,
       "pduEnvMonitoringHumiHystersis": pduEnvMonitoringHumiHystersis,
       "pduEnvMonitoringHumiOffset": pduEnvMonitoringHumiOffset,
       "pduEnvMonitoringAlarm1Setup": pduEnvMonitoringAlarm1Setup,
       "pduEnvMonitoringAlarm2Setup": pduEnvMonitoringAlarm2Setup,
       "pduTraps": pduTraps,
       "pduSystemColdBoot": pduSystemColdBoot,
       "pduSystemWarmBoot": pduSystemWarmBoot,
       "pduSystemRestart": pduSystemRestart,
       "pduResetToDefault": pduResetToDefault,
       "pduFirmUpgrade": pduFirmUpgrade,
       "pduSystemLogClear": pduSystemLogClear,
       "pduEventlogClear": pduEventlogClear,
       "pduInletHistoryClear": pduInletHistoryClear,
       "pduOutletHistoryClear": pduOutletHistoryClear,
       "pduSystemTimeChangeUser": pduSystemTimeChangeUser,
       "pduSystemTimeChangeNtp": pduSystemTimeChangeNtp,
       "pduSystemTimeChangeRtc": pduSystemTimeChangeRtc,
       "pduMailTestPass": pduMailTestPass,
       "pduMailTestFail": pduMailTestFail,
       "pduMailSentPass": pduMailSentPass,
       "pduMailSentFail": pduMailSentFail,
       "pduSystemCfgChange": pduSystemCfgChange,
       "pduSystemParamImport": pduSystemParamImport,
       "pduInletCommLost": pduInletCommLost,
       "pduInletCommRestore": pduInletCommRestore,
       "pduOutletCommLost": pduOutletCommLost,
       "pduOutletCommRestore": pduOutletCommRestore,
       "pduOutletOnUser": pduOutletOnUser,
       "pduOutletOnSchedule": pduOutletOnSchedule,
       "pduOutletOffUser": pduOutletOffUser,
       "pduOutletOffSchedule": pduOutletOffSchedule,
       "pduOutletRebootUser": pduOutletRebootUser,
       "pduOutletRebootSchedule": pduOutletRebootSchedule,
       "pduInletEnergyReset": pduInletEnergyReset,
       "pduOutletEnergyReset": pduOutletEnergyReset,
       "pduSetUser": pduSetUser,
       "pduDeletUser": pduDeletUser,
       "pduUpgradeInletSuccess": pduUpgradeInletSuccess,
       "pduUpgradeInletFail": pduUpgradeInletFail,
       "pduUpgradeOutletSuccess": pduUpgradeOutletSuccess,
       "pduUpgradeOutletFail": pduUpgradeOutletFail,
       "pduEmdHistoryLogClear": pduEmdHistoryLogClear,
       "pduAccountResetDefault": pduAccountResetDefault,
       "pduUpgradeExtEmdSuccess": pduUpgradeExtEmdSuccess,
       "pduUpgradeExtEmdFail": pduUpgradeExtEmdFail,
       "pduGroupOutletChanged": pduGroupOutletChanged,
       "pduScheduleOutletChanged": pduScheduleOutletChanged,
       "pduGroupChanged": pduGroupChanged,
       "pduSnmpConflicts": pduSnmpConflicts,
       "pduInletEnergyResetPhase1": pduInletEnergyResetPhase1,
       "pduInletEnergyResetPhase2": pduInletEnergyResetPhase2,
       "pduInletEnergyResetPhase3": pduInletEnergyResetPhase3,
       "pduInletREnergyReset": pduInletREnergyReset,
       "pduInletREnergyResetPhase1": pduInletREnergyResetPhase1,
       "pduInletREnergyResetPhase2": pduInletREnergyResetPhase2,
       "pduInletREnergyResetPhase3": pduInletREnergyResetPhase3,
       "pduEmdTempHighWarnToNormal": pduEmdTempHighWarnToNormal,
       "pduEmdTempHighWarn": pduEmdTempHighWarn,
       "pduEmdTempLowWarnToNormal": pduEmdTempLowWarnToNormal,
       "pduEmdTempLowWarn": pduEmdTempLowWarn,
       "pduEmdTempHighCritToWarn": pduEmdTempHighCritToWarn,
       "pduEmdTempHighCritical": pduEmdTempHighCritical,
       "pduEmdTempLowCritToWarn": pduEmdTempLowCritToWarn,
       "pduEmdTempLowCritical": pduEmdTempLowCritical,
       "pduEmdHumiHighWarnToNormal": pduEmdHumiHighWarnToNormal,
       "pduEmdHumiHighWarn": pduEmdHumiHighWarn,
       "pduEmdHumiLowWarnToNormal": pduEmdHumiLowWarnToNormal,
       "pduEmdHumiLowWarn": pduEmdHumiLowWarn,
       "pduEmdHumiHighCritToWarn": pduEmdHumiHighCritToWarn,
       "pduEmdHumiHighCritical": pduEmdHumiHighCritical,
       "pduEmdHumiLowCritToWarn": pduEmdHumiLowCritToWarn,
       "pduEmdHumiLowCritical": pduEmdHumiLowCritical,
       "pduEmdAlarm1NotActive": pduEmdAlarm1NotActive,
       "pduEmdAlarm1Active": pduEmdAlarm1Active,
       "pduEmdAlarm2NotActive": pduEmdAlarm2NotActive,
       "pduEmdAlarm2Active": pduEmdAlarm2Active,
       "pduRs485Online": pduRs485Online,
       "pduRs485Offline": pduRs485Offline,
       "pduInletLoadCritToWarn": pduInletLoadCritToWarn,
       "pduInletLoadCritical": pduInletLoadCritical,
       "pduInletLoadWarnToNormal": pduInletLoadWarnToNormal,
       "pduInletLoadWarn": pduInletLoadWarn,
       "pduInletCurrPhase1CritToWarn": pduInletCurrPhase1CritToWarn,
       "pduInletCurrPhase1Critical": pduInletCurrPhase1Critical,
       "pduInletCurrPhase1WarnToNormal": pduInletCurrPhase1WarnToNormal,
       "pduInletCurrPhase1Warn": pduInletCurrPhase1Warn,
       "pduInletCurrPhase2CritToWarn": pduInletCurrPhase2CritToWarn,
       "pduInletCurrPhase2Critical": pduInletCurrPhase2Critical,
       "pduInletCurrPhase2WarnToNormal": pduInletCurrPhase2WarnToNormal,
       "pduInletCurrPhase2Warn": pduInletCurrPhase2Warn,
       "pduInletCurrPhase3CritToWarn": pduInletCurrPhase3CritToWarn,
       "pduInletCurrPhase3Critical": pduInletCurrPhase3Critical,
       "pduInletCurrPhase3WarnToNormal": pduInletCurrPhase3WarnToNormal,
       "pduInletCurrPhase3Warn": pduInletCurrPhase3Warn,
       "pduInletVoltPhase1CritToWarn": pduInletVoltPhase1CritToWarn,
       "pduInletVoltPhase1Critical": pduInletVoltPhase1Critical,
       "pduInletVoltPhase1WarnToNormal": pduInletVoltPhase1WarnToNormal,
       "pduInletVoltPhase1Warn": pduInletVoltPhase1Warn,
       "pduInletVoltPhase2CritToWarn": pduInletVoltPhase2CritToWarn,
       "pduInletVoltPhase2Critical": pduInletVoltPhase2Critical,
       "pduInletVoltPhase2WarnToNormal": pduInletVoltPhase2WarnToNormal,
       "pduInletVoltPhase2Warn": pduInletVoltPhase2Warn,
       "pduInletVoltPhase3CritToWarn": pduInletVoltPhase3CritToWarn,
       "pduInletVoltPhase3Critical": pduInletVoltPhase3Critical,
       "pduInletVoltPhase3WarnToNormal": pduInletVoltPhase3WarnToNormal,
       "pduInletVoltPhase3Warn": pduInletVoltPhase3Warn,
       "pduOutletCurrCritToWarn": pduOutletCurrCritToWarn,
       "pduOutletCurrCritical": pduOutletCurrCritical,
       "pduOutletCurrWarnToNormal": pduOutletCurrWarnToNormal,
       "pduOutletCurrWarn": pduOutletCurrWarn,
       "pduOutletPwrCritTOWarn": pduOutletPwrCritTOWarn,
       "pduOutletPwrCritical": pduOutletPwrCritical,
       "pduOutletPwrWarnToNormal": pduOutletPwrWarnToNormal,
       "pduOutletPwrWarn": pduOutletPwrWarn,
       "pduAlarm1Disabled": pduAlarm1Disabled,
       "pduAlarm2Disabled": pduAlarm2Disabled,
       "pduIntetResidualCurrect1Occured": pduIntetResidualCurrect1Occured,
       "pduIntetResidualCurrect1Remove": pduIntetResidualCurrect1Remove,
       "pduInletLoadBalanceCritToWarn": pduInletLoadBalanceCritToWarn,
       "pduInletLoadBalanceCritical": pduInletLoadBalanceCritical,
       "pduInletLoadBalanceWarnToNormal": pduInletLoadBalanceWarnToNormal,
       "pduInletLoadBalanceWarn": pduInletLoadBalanceWarn,
       "pduInletAcFail": pduInletAcFail,
       "pduInletAcRestore": pduInletAcRestore}
)
