# SNMP MIB module (RUIJIE-IPSEC2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IPSEC2-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieIPSec2MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieIPSecNegoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2),
          ("invalidType", 2147483647))
    )



class RuijieEncapMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transport", 2),
          ("invalidMode", 2147483647))
    )



class RuijieEncryptAlgo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              12,
              128,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("desCbc", 2),
          ("threedesCbc", 3),
          ("aesCbc", 12),
          ("sm1Cbc", 128),
          ("invalidAlg", 2147483647))
    )



class RuijieAuthAlgo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 2),
          ("sha", 3),
          ("invalidAlg", 2147483647))
    )



class RuijieDiffHellmanGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("modp768", 1),
          ("modp1024", 2),
          ("invalidMode", 2147483647))
    )



class RuijieIPSecTunnelState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establishing", 1),
          ("active", 2),
          ("expiring", 3))
    )



class RuijieSaProtocol(TextualConvention, Integer32):
    status = "current"
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
        *(("reserved", 0),
          ("isakmp", 1),
          ("ah", 2),
          ("esp", 3))
    )



class RuijieTrafficType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv4AddrSubnet", 2),
          ("ipv6Addr", 3),
          ("ipv6AddrSubnet", 4),
          ("ipv4AddrRange", 5),
          ("ipv6AddrRange", 6))
    )



class RuijieIPSec2NegoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2),
          ("invalidType", 2147483647))
    )



class RuijieIPSec2TunnelState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establishing", 1),
          ("active", 2),
          ("expiring", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieIPSec2Objects_ObjectIdentity = ObjectIdentity
ruijieIPSec2Objects = _RuijieIPSec2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1)
)
_RuijieIPSec2TunnelTable_Object = MibTable
ruijieIPSec2TunnelTable = _RuijieIPSec2TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelTable.setStatus("current")
_RuijieIPSec2TunnelEntry_Object = MibTableRow
ruijieIPSec2TunnelEntry = _RuijieIPSec2TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1)
)
ruijieIPSec2TunnelEntry.setIndexNames(
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunIfIndex"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteAddr"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalType"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalProtocol"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr1"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr2"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalPort"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr1"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr2"),
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemotePort"),
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelEntry.setStatus("current")


class _RuijieIPSec2TunIfIndex_Type(Integer32):
    """Custom type ruijieIPSec2TunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunIfIndex_Type.__name__ = "Integer32"
_RuijieIPSec2TunIfIndex_Object = MibTableColumn
ruijieIPSec2TunIfIndex = _RuijieIPSec2TunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 1),
    _RuijieIPSec2TunIfIndex_Type()
)
ruijieIPSec2TunIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunIfIndex.setStatus("current")
_RuijieIPSec2TunnelTrafficIndex_Type = Integer32
_RuijieIPSec2TunnelTrafficIndex_Object = MibTableColumn
ruijieIPSec2TunnelTrafficIndex = _RuijieIPSec2TunnelTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 2),
    _RuijieIPSec2TunnelTrafficIndex_Type()
)
ruijieIPSec2TunnelTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelTrafficIndex.setStatus("current")


class _RuijieIPSec2TunIndex_Type(Integer32):
    """Custom type ruijieIPSec2TunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunIndex_Type.__name__ = "Integer32"
_RuijieIPSec2TunIndex_Object = MibTableColumn
ruijieIPSec2TunIndex = _RuijieIPSec2TunIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 3),
    _RuijieIPSec2TunIndex_Type()
)
ruijieIPSec2TunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunIndex.setStatus("current")


class _RuijieIPSec2TunIKETunnelIndex_Type(Integer32):
    """Custom type ruijieIPSec2TunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunIKETunnelIndex_Type.__name__ = "Integer32"
_RuijieIPSec2TunIKETunnelIndex_Object = MibTableColumn
ruijieIPSec2TunIKETunnelIndex = _RuijieIPSec2TunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 5),
    _RuijieIPSec2TunIKETunnelIndex_Type()
)
ruijieIPSec2TunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunIKETunnelIndex.setStatus("current")
_RuijieIPSec2TunnelAhOutSaIndex_Type = Integer32
_RuijieIPSec2TunnelAhOutSaIndex_Object = MibTableColumn
ruijieIPSec2TunnelAhOutSaIndex = _RuijieIPSec2TunnelAhOutSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 6),
    _RuijieIPSec2TunnelAhOutSaIndex_Type()
)
ruijieIPSec2TunnelAhOutSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelAhOutSaIndex.setStatus("current")


class _RuijieIPSec2TunnelAhInSaIndex_Type(Integer32):
    """Custom type ruijieIPSec2TunnelAhInSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunnelAhInSaIndex_Type.__name__ = "Integer32"
_RuijieIPSec2TunnelAhInSaIndex_Object = MibTableColumn
ruijieIPSec2TunnelAhInSaIndex = _RuijieIPSec2TunnelAhInSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 7),
    _RuijieIPSec2TunnelAhInSaIndex_Type()
)
ruijieIPSec2TunnelAhInSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelAhInSaIndex.setStatus("current")


class _RuijieIPSec2TunnelEspOutSaIndex_Type(Integer32):
    """Custom type ruijieIPSec2TunnelEspOutSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunnelEspOutSaIndex_Type.__name__ = "Integer32"
_RuijieIPSec2TunnelEspOutSaIndex_Object = MibTableColumn
ruijieIPSec2TunnelEspOutSaIndex = _RuijieIPSec2TunnelEspOutSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 8),
    _RuijieIPSec2TunnelEspOutSaIndex_Type()
)
ruijieIPSec2TunnelEspOutSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelEspOutSaIndex.setStatus("current")
_RuijieIPSec2TunnelEspInSaIndex_Type = Integer32
_RuijieIPSec2TunnelEspInSaIndex_Object = MibTableColumn
ruijieIPSec2TunnelEspInSaIndex = _RuijieIPSec2TunnelEspInSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 9),
    _RuijieIPSec2TunnelEspInSaIndex_Type()
)
ruijieIPSec2TunnelEspInSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelEspInSaIndex.setStatus("current")
_RuijieIPSec2TunLocalAddr_Type = IpAddress
_RuijieIPSec2TunLocalAddr_Object = MibTableColumn
ruijieIPSec2TunLocalAddr = _RuijieIPSec2TunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 10),
    _RuijieIPSec2TunLocalAddr_Type()
)
ruijieIPSec2TunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunLocalAddr.setStatus("current")
_RuijieIPSec2TunRemoteAddr_Type = IpAddress
_RuijieIPSec2TunRemoteAddr_Object = MibTableColumn
ruijieIPSec2TunRemoteAddr = _RuijieIPSec2TunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 11),
    _RuijieIPSec2TunRemoteAddr_Type()
)
ruijieIPSec2TunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunRemoteAddr.setStatus("current")
_RuijieIPSec2TunLocalHostname_Type = DisplayString
_RuijieIPSec2TunLocalHostname_Object = MibTableColumn
ruijieIPSec2TunLocalHostname = _RuijieIPSec2TunLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 12),
    _RuijieIPSec2TunLocalHostname_Type()
)
ruijieIPSec2TunLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunLocalHostname.setStatus("current")
_RuijieIPSec2TunRemoteHostname_Type = DisplayString
_RuijieIPSec2TunRemoteHostname_Object = MibTableColumn
ruijieIPSec2TunRemoteHostname = _RuijieIPSec2TunRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 13),
    _RuijieIPSec2TunRemoteHostname_Type()
)
ruijieIPSec2TunRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunRemoteHostname.setStatus("current")
_RuijieIPSec2TunKeyType_Type = RuijieIPSec2NegoType
_RuijieIPSec2TunKeyType_Object = MibTableColumn
ruijieIPSec2TunKeyType = _RuijieIPSec2TunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 14),
    _RuijieIPSec2TunKeyType_Type()
)
ruijieIPSec2TunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunKeyType.setStatus("current")
_RuijieIPSec2TunEncapMode_Type = RuijieEncapMode
_RuijieIPSec2TunEncapMode_Object = MibTableColumn
ruijieIPSec2TunEncapMode = _RuijieIPSec2TunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 15),
    _RuijieIPSec2TunEncapMode_Type()
)
ruijieIPSec2TunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunEncapMode.setStatus("current")


class _RuijieIPSec2TunInitiator_Type(Integer32):
    """Custom type ruijieIPSec2TunInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("none", 2147483647))
    )


_RuijieIPSec2TunInitiator_Type.__name__ = "Integer32"
_RuijieIPSec2TunInitiator_Object = MibTableColumn
ruijieIPSec2TunInitiator = _RuijieIPSec2TunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 16),
    _RuijieIPSec2TunInitiator_Type()
)
ruijieIPSec2TunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInitiator.setStatus("current")


class _RuijieIPSec2TunLifeSize_Type(Integer32):
    """Custom type ruijieIPSec2TunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunLifeSize_Type.__name__ = "Integer32"
_RuijieIPSec2TunLifeSize_Object = MibTableColumn
ruijieIPSec2TunLifeSize = _RuijieIPSec2TunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 17),
    _RuijieIPSec2TunLifeSize_Type()
)
ruijieIPSec2TunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunLifeSize.setStatus("current")


class _RuijieIPSec2TunLifeTime_Type(Integer32):
    """Custom type ruijieIPSec2TunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunLifeTime_Type.__name__ = "Integer32"
_RuijieIPSec2TunLifeTime_Object = MibTableColumn
ruijieIPSec2TunLifeTime = _RuijieIPSec2TunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 18),
    _RuijieIPSec2TunLifeTime_Type()
)
ruijieIPSec2TunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunLifeTime.setStatus("current")


class _RuijieIPSec2TunRemainTime_Type(Integer32):
    """Custom type ruijieIPSec2TunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSec2TunRemainTime_Type.__name__ = "Integer32"
_RuijieIPSec2TunRemainTime_Object = MibTableColumn
ruijieIPSec2TunRemainTime = _RuijieIPSec2TunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 19),
    _RuijieIPSec2TunRemainTime_Type()
)
ruijieIPSec2TunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunRemainTime.setStatus("current")


class _RuijieIPSec2TunActiveTime_Type(Integer32):
    """Custom type ruijieIPSec2TunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSec2TunActiveTime_Type.__name__ = "Integer32"
_RuijieIPSec2TunActiveTime_Object = MibTableColumn
ruijieIPSec2TunActiveTime = _RuijieIPSec2TunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 20),
    _RuijieIPSec2TunActiveTime_Type()
)
ruijieIPSec2TunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunActiveTime.setStatus("current")
_RuijieIPSec2TunCreateTime_Type = TimeStamp
_RuijieIPSec2TunCreateTime_Object = MibTableColumn
ruijieIPSec2TunCreateTime = _RuijieIPSec2TunCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 21),
    _RuijieIPSec2TunCreateTime_Type()
)
ruijieIPSec2TunCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunCreateTime.setStatus("current")


class _RuijieIPSec2TunRemainSize_Type(Integer32):
    """Custom type ruijieIPSec2TunRemainSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSec2TunRemainSize_Type.__name__ = "Integer32"
_RuijieIPSec2TunRemainSize_Object = MibTableColumn
ruijieIPSec2TunRemainSize = _RuijieIPSec2TunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 23),
    _RuijieIPSec2TunRemainSize_Type()
)
ruijieIPSec2TunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunRemainSize.setStatus("current")
_RuijieIPSec2TunTotalRefreshes_Type = Counter32
_RuijieIPSec2TunTotalRefreshes_Object = MibTableColumn
ruijieIPSec2TunTotalRefreshes = _RuijieIPSec2TunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 24),
    _RuijieIPSec2TunTotalRefreshes_Type()
)
ruijieIPSec2TunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunTotalRefreshes.setStatus("current")
_RuijieIPSec2TunCurrentSaInstances_Type = Gauge32
_RuijieIPSec2TunCurrentSaInstances_Object = MibTableColumn
ruijieIPSec2TunCurrentSaInstances = _RuijieIPSec2TunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 25),
    _RuijieIPSec2TunCurrentSaInstances_Type()
)
ruijieIPSec2TunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunCurrentSaInstances.setStatus("current")
_RuijieIPSec2TunInSaEncryptAlgo_Type = RuijieEncryptAlgo
_RuijieIPSec2TunInSaEncryptAlgo_Object = MibTableColumn
ruijieIPSec2TunInSaEncryptAlgo = _RuijieIPSec2TunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 26),
    _RuijieIPSec2TunInSaEncryptAlgo_Type()
)
ruijieIPSec2TunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInSaEncryptAlgo.setStatus("current")
_RuijieIPSec2TunInSaAhAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSec2TunInSaAhAuthAlgo_Object = MibTableColumn
ruijieIPSec2TunInSaAhAuthAlgo = _RuijieIPSec2TunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 27),
    _RuijieIPSec2TunInSaAhAuthAlgo_Type()
)
ruijieIPSec2TunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInSaAhAuthAlgo.setStatus("current")
_RuijieIPSec2TunInSaEspAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSec2TunInSaEspAuthAlgo_Object = MibTableColumn
ruijieIPSec2TunInSaEspAuthAlgo = _RuijieIPSec2TunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 28),
    _RuijieIPSec2TunInSaEspAuthAlgo_Type()
)
ruijieIPSec2TunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInSaEspAuthAlgo.setStatus("current")
_RuijieIPSec2TunDiffHellmanGrp_Type = RuijieDiffHellmanGrp
_RuijieIPSec2TunDiffHellmanGrp_Object = MibTableColumn
ruijieIPSec2TunDiffHellmanGrp = _RuijieIPSec2TunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 29),
    _RuijieIPSec2TunDiffHellmanGrp_Type()
)
ruijieIPSec2TunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunDiffHellmanGrp.setStatus("current")
_RuijieIPSec2TunOutSaEncryptAlgo_Type = RuijieEncryptAlgo
_RuijieIPSec2TunOutSaEncryptAlgo_Object = MibTableColumn
ruijieIPSec2TunOutSaEncryptAlgo = _RuijieIPSec2TunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 30),
    _RuijieIPSec2TunOutSaEncryptAlgo_Type()
)
ruijieIPSec2TunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutSaEncryptAlgo.setStatus("current")
_RuijieIPSec2TunOutSaAhAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSec2TunOutSaAhAuthAlgo_Object = MibTableColumn
ruijieIPSec2TunOutSaAhAuthAlgo = _RuijieIPSec2TunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 31),
    _RuijieIPSec2TunOutSaAhAuthAlgo_Type()
)
ruijieIPSec2TunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutSaAhAuthAlgo.setStatus("current")
_RuijieIPSec2TunOutSaEspAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSec2TunOutSaEspAuthAlgo_Object = MibTableColumn
ruijieIPSec2TunOutSaEspAuthAlgo = _RuijieIPSec2TunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 32),
    _RuijieIPSec2TunOutSaEspAuthAlgo_Type()
)
ruijieIPSec2TunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutSaEspAuthAlgo.setStatus("current")
_RuijieIPSec2TunMapName_Type = DisplayString
_RuijieIPSec2TunMapName_Object = MibTableColumn
ruijieIPSec2TunMapName = _RuijieIPSec2TunMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 33),
    _RuijieIPSec2TunMapName_Type()
)
ruijieIPSec2TunMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunMapName.setStatus("current")


class _RuijieIPSec2TunSeqNum_Type(Integer32):
    """Custom type ruijieIPSec2TunSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2TunSeqNum_Type.__name__ = "Integer32"
_RuijieIPSec2TunSeqNum_Object = MibTableColumn
ruijieIPSec2TunSeqNum = _RuijieIPSec2TunSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 34),
    _RuijieIPSec2TunSeqNum_Type()
)
ruijieIPSec2TunSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunSeqNum.setStatus("current")
_RuijieIPSec2TunStatus_Type = RuijieIPSec2TunnelState
_RuijieIPSec2TunStatus_Object = MibTableColumn
ruijieIPSec2TunStatus = _RuijieIPSec2TunStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 35),
    _RuijieIPSec2TunStatus_Type()
)
ruijieIPSec2TunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSec2TunStatus.setStatus("current")
_RuijieIPSec2TunRemoteDomain_Type = DisplayString
_RuijieIPSec2TunRemoteDomain_Object = MibTableColumn
ruijieIPSec2TunRemoteDomain = _RuijieIPSec2TunRemoteDomain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 36),
    _RuijieIPSec2TunRemoteDomain_Type()
)
ruijieIPSec2TunRemoteDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSec2TunRemoteDomain.setStatus("current")
_RuijieIPSec2LastTunRemoteAddr_Type = IpAddress
_RuijieIPSec2LastTunRemoteAddr_Object = MibTableColumn
ruijieIPSec2LastTunRemoteAddr = _RuijieIPSec2LastTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 37),
    _RuijieIPSec2LastTunRemoteAddr_Type()
)
ruijieIPSec2LastTunRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSec2LastTunRemoteAddr.setStatus("current")
_RuijieIPSec2SystemSerialNumber_Type = DisplayString
_RuijieIPSec2SystemSerialNumber_Object = MibTableColumn
ruijieIPSec2SystemSerialNumber = _RuijieIPSec2SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 1, 1, 38),
    _RuijieIPSec2SystemSerialNumber_Type()
)
ruijieIPSec2SystemSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSec2SystemSerialNumber.setStatus("current")
_RuijieIPSec2TunnelStatTable_Object = MibTable
ruijieIPSec2TunnelStatTable = _RuijieIPSec2TunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelStatTable.setStatus("current")
_RuijieIPSec2TunnelStatEntry_Object = MibTableRow
ruijieIPSec2TunnelStatEntry = _RuijieIPSec2TunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1)
)
ruijieIPSec2TunnelStatEntry.setIndexNames(
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunIndex"),
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelStatEntry.setStatus("current")
_RuijieIPSec2TunInOctets_Type = Counter64
_RuijieIPSec2TunInOctets_Object = MibTableColumn
ruijieIPSec2TunInOctets = _RuijieIPSec2TunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 1),
    _RuijieIPSec2TunInOctets_Type()
)
ruijieIPSec2TunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInOctets.setStatus("current")
_RuijieIPSec2TunInDecompOctets_Type = Counter64
_RuijieIPSec2TunInDecompOctets_Object = MibTableColumn
ruijieIPSec2TunInDecompOctets = _RuijieIPSec2TunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 2),
    _RuijieIPSec2TunInDecompOctets_Type()
)
ruijieIPSec2TunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInDecompOctets.setStatus("current")
_RuijieIPSec2TunInPkts_Type = Counter64
_RuijieIPSec2TunInPkts_Object = MibTableColumn
ruijieIPSec2TunInPkts = _RuijieIPSec2TunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 3),
    _RuijieIPSec2TunInPkts_Type()
)
ruijieIPSec2TunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInPkts.setStatus("current")
_RuijieIPSec2TunInSpeed_Type = Counter64
_RuijieIPSec2TunInSpeed_Object = MibTableColumn
ruijieIPSec2TunInSpeed = _RuijieIPSec2TunInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 4),
    _RuijieIPSec2TunInSpeed_Type()
)
ruijieIPSec2TunInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInSpeed.setStatus("current")
_RuijieIPSec2TunInDropPkts_Type = Counter64
_RuijieIPSec2TunInDropPkts_Object = MibTableColumn
ruijieIPSec2TunInDropPkts = _RuijieIPSec2TunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 5),
    _RuijieIPSec2TunInDropPkts_Type()
)
ruijieIPSec2TunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunInDropPkts.setStatus("current")
_RuijieIPSec2TunOutOctets_Type = Counter64
_RuijieIPSec2TunOutOctets_Object = MibTableColumn
ruijieIPSec2TunOutOctets = _RuijieIPSec2TunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 6),
    _RuijieIPSec2TunOutOctets_Type()
)
ruijieIPSec2TunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutOctets.setStatus("current")
_RuijieIPSec2TunOutUncompOctets_Type = Counter64
_RuijieIPSec2TunOutUncompOctets_Object = MibTableColumn
ruijieIPSec2TunOutUncompOctets = _RuijieIPSec2TunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 7),
    _RuijieIPSec2TunOutUncompOctets_Type()
)
ruijieIPSec2TunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutUncompOctets.setStatus("current")
_RuijieIPSec2TunOutPkts_Type = Counter64
_RuijieIPSec2TunOutPkts_Object = MibTableColumn
ruijieIPSec2TunOutPkts = _RuijieIPSec2TunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 8),
    _RuijieIPSec2TunOutPkts_Type()
)
ruijieIPSec2TunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutPkts.setStatus("current")
_RuijieIPSec2TunOutSpeed_Type = Counter64
_RuijieIPSec2TunOutSpeed_Object = MibTableColumn
ruijieIPSec2TunOutSpeed = _RuijieIPSec2TunOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 9),
    _RuijieIPSec2TunOutSpeed_Type()
)
ruijieIPSec2TunOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutSpeed.setStatus("current")
_RuijieIPSec2TunOutDropPkts_Type = Counter64
_RuijieIPSec2TunOutDropPkts_Object = MibTableColumn
ruijieIPSec2TunOutDropPkts = _RuijieIPSec2TunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 2, 1, 10),
    _RuijieIPSec2TunOutDropPkts_Type()
)
ruijieIPSec2TunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TunOutDropPkts.setStatus("current")
_RuijieIPSec2SaTable_Object = MibTable
ruijieIPSec2SaTable = _RuijieIPSec2SaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieIPSec2SaTable.setStatus("current")
_RuijieIPSec2SaEntry_Object = MibTableRow
ruijieIPSec2SaEntry = _RuijieIPSec2SaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1)
)
ruijieIPSec2SaEntry.setIndexNames(
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaIndex"),
)
if mibBuilder.loadTexts:
    ruijieIPSec2SaEntry.setStatus("current")


class _RuijieIPSec2SaIndex_Type(Integer32):
    """Custom type ruijieIPSec2SaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSec2SaIndex_Type.__name__ = "Integer32"
_RuijieIPSec2SaIndex_Object = MibTableColumn
ruijieIPSec2SaIndex = _RuijieIPSec2SaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 1),
    _RuijieIPSec2SaIndex_Type()
)
ruijieIPSec2SaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaIndex.setStatus("current")


class _RuijieIPSec2SaDirection_Type(Integer32):
    """Custom type ruijieIPSec2SaDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_RuijieIPSec2SaDirection_Type.__name__ = "Integer32"
_RuijieIPSec2SaDirection_Object = MibTableColumn
ruijieIPSec2SaDirection = _RuijieIPSec2SaDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 2),
    _RuijieIPSec2SaDirection_Type()
)
ruijieIPSec2SaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaDirection.setStatus("current")


class _RuijieIPSec2SaValue_Type(Unsigned32):
    """Custom type ruijieIPSec2SaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieIPSec2SaValue_Type.__name__ = "Unsigned32"
_RuijieIPSec2SaValue_Object = MibTableColumn
ruijieIPSec2SaValue = _RuijieIPSec2SaValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 3),
    _RuijieIPSec2SaValue_Type()
)
ruijieIPSec2SaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaValue.setStatus("current")
_RuijieIPSec2SaProtocol_Type = RuijieSaProtocol
_RuijieIPSec2SaProtocol_Object = MibTableColumn
ruijieIPSec2SaProtocol = _RuijieIPSec2SaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 4),
    _RuijieIPSec2SaProtocol_Type()
)
ruijieIPSec2SaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaProtocol.setStatus("current")
_RuijieIPSec2SaEncryptAlgo_Type = RuijieEncryptAlgo
_RuijieIPSec2SaEncryptAlgo_Object = MibTableColumn
ruijieIPSec2SaEncryptAlgo = _RuijieIPSec2SaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 5),
    _RuijieIPSec2SaEncryptAlgo_Type()
)
ruijieIPSec2SaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaEncryptAlgo.setStatus("current")
_RuijieIPSec2SaAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSec2SaAuthAlgo_Object = MibTableColumn
ruijieIPSec2SaAuthAlgo = _RuijieIPSec2SaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 6),
    _RuijieIPSec2SaAuthAlgo_Type()
)
ruijieIPSec2SaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaAuthAlgo.setStatus("current")
_RuijieIPSec2SaStatus_Type = RuijieIPSec2TunnelState
_RuijieIPSec2SaStatus_Object = MibTableColumn
ruijieIPSec2SaStatus = _RuijieIPSec2SaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 3, 1, 7),
    _RuijieIPSec2SaStatus_Type()
)
ruijieIPSec2SaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2SaStatus.setStatus("current")
_RuijieIPSec2TrafficTable_Object = MibTable
ruijieIPSec2TrafficTable = _RuijieIPSec2TrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficTable.setStatus("current")
_RuijieIPSec2TrafficEntry_Object = MibTableRow
ruijieIPSec2TrafficEntry = _RuijieIPSec2TrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1)
)
ruijieIPSec2TrafficEntry.setIndexNames(
    (0, "RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunnelTrafficIndex"),
)
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficEntry.setStatus("current")
_RuijieIPSec2TrafficIndex_Type = Integer32
_RuijieIPSec2TrafficIndex_Object = MibTableColumn
ruijieIPSec2TrafficIndex = _RuijieIPSec2TrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 1),
    _RuijieIPSec2TrafficIndex_Type()
)
ruijieIPSec2TrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficIndex.setStatus("current")
_RuijieIPSec2TrafficLocalType_Type = RuijieTrafficType
_RuijieIPSec2TrafficLocalType_Object = MibTableColumn
ruijieIPSec2TrafficLocalType = _RuijieIPSec2TrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 2),
    _RuijieIPSec2TrafficLocalType_Type()
)
ruijieIPSec2TrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficLocalType.setStatus("current")
_RuijieIPSec2TrafficLocalAddr1_Type = IpAddress
_RuijieIPSec2TrafficLocalAddr1_Object = MibTableColumn
ruijieIPSec2TrafficLocalAddr1 = _RuijieIPSec2TrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 3),
    _RuijieIPSec2TrafficLocalAddr1_Type()
)
ruijieIPSec2TrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficLocalAddr1.setStatus("current")
_RuijieIPSec2TrafficLocalAddr2_Type = IpAddress
_RuijieIPSec2TrafficLocalAddr2_Object = MibTableColumn
ruijieIPSec2TrafficLocalAddr2 = _RuijieIPSec2TrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 4),
    _RuijieIPSec2TrafficLocalAddr2_Type()
)
ruijieIPSec2TrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficLocalAddr2.setStatus("current")


class _RuijieIPSec2TrafficLocalProtocol_Type(Integer32):
    """Custom type ruijieIPSec2TrafficLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieIPSec2TrafficLocalProtocol_Type.__name__ = "Integer32"
_RuijieIPSec2TrafficLocalProtocol_Object = MibTableColumn
ruijieIPSec2TrafficLocalProtocol = _RuijieIPSec2TrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 5),
    _RuijieIPSec2TrafficLocalProtocol_Type()
)
ruijieIPSec2TrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficLocalProtocol.setStatus("current")


class _RuijieIPSec2TrafficLocalPort_Type(Integer32):
    """Custom type ruijieIPSec2TrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieIPSec2TrafficLocalPort_Type.__name__ = "Integer32"
_RuijieIPSec2TrafficLocalPort_Object = MibTableColumn
ruijieIPSec2TrafficLocalPort = _RuijieIPSec2TrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 6),
    _RuijieIPSec2TrafficLocalPort_Type()
)
ruijieIPSec2TrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficLocalPort.setStatus("current")
_RuijieIPSec2TrafficLocalHostname_Type = DisplayString
_RuijieIPSec2TrafficLocalHostname_Object = MibTableColumn
ruijieIPSec2TrafficLocalHostname = _RuijieIPSec2TrafficLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 7),
    _RuijieIPSec2TrafficLocalHostname_Type()
)
ruijieIPSec2TrafficLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficLocalHostname.setStatus("current")
_RuijieIPSec2TrafficRemoteType_Type = RuijieTrafficType
_RuijieIPSec2TrafficRemoteType_Object = MibTableColumn
ruijieIPSec2TrafficRemoteType = _RuijieIPSec2TrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 8),
    _RuijieIPSec2TrafficRemoteType_Type()
)
ruijieIPSec2TrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficRemoteType.setStatus("current")
_RuijieIPSec2TrafficRemoteAddr1_Type = IpAddress
_RuijieIPSec2TrafficRemoteAddr1_Object = MibTableColumn
ruijieIPSec2TrafficRemoteAddr1 = _RuijieIPSec2TrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 9),
    _RuijieIPSec2TrafficRemoteAddr1_Type()
)
ruijieIPSec2TrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficRemoteAddr1.setStatus("current")
_RuijieIPSec2TrafficRemoteAddr2_Type = IpAddress
_RuijieIPSec2TrafficRemoteAddr2_Object = MibTableColumn
ruijieIPSec2TrafficRemoteAddr2 = _RuijieIPSec2TrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 10),
    _RuijieIPSec2TrafficRemoteAddr2_Type()
)
ruijieIPSec2TrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficRemoteAddr2.setStatus("current")


class _RuijieIPSec2TrafficRemoteProtocol_Type(Integer32):
    """Custom type ruijieIPSec2TrafficRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieIPSec2TrafficRemoteProtocol_Type.__name__ = "Integer32"
_RuijieIPSec2TrafficRemoteProtocol_Object = MibTableColumn
ruijieIPSec2TrafficRemoteProtocol = _RuijieIPSec2TrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 11),
    _RuijieIPSec2TrafficRemoteProtocol_Type()
)
ruijieIPSec2TrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficRemoteProtocol.setStatus("current")


class _RuijieIPSec2TrafficRemotePort_Type(Integer32):
    """Custom type ruijieIPSec2TrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieIPSec2TrafficRemotePort_Type.__name__ = "Integer32"
_RuijieIPSec2TrafficRemotePort_Object = MibTableColumn
ruijieIPSec2TrafficRemotePort = _RuijieIPSec2TrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 12),
    _RuijieIPSec2TrafficRemotePort_Type()
)
ruijieIPSec2TrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficRemotePort.setStatus("current")
_RuijieIPSec2TrafficRemoteHostname_Type = DisplayString
_RuijieIPSec2TrafficRemoteHostname_Object = MibTableColumn
ruijieIPSec2TrafficRemoteHostname = _RuijieIPSec2TrafficRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 4, 1, 13),
    _RuijieIPSec2TrafficRemoteHostname_Type()
)
ruijieIPSec2TrafficRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficRemoteHostname.setStatus("current")
_RuijieIPSec2GlobalStats_ObjectIdentity = ObjectIdentity
ruijieIPSec2GlobalStats = _RuijieIPSec2GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5)
)
_RuijieIPSec2GlobalActiveTunnels_Type = Gauge32
_RuijieIPSec2GlobalActiveTunnels_Object = MibScalar
ruijieIPSec2GlobalActiveTunnels = _RuijieIPSec2GlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 1),
    _RuijieIPSec2GlobalActiveTunnels_Type()
)
ruijieIPSec2GlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalActiveTunnels.setStatus("current")
_RuijieIPSec2GlobalActiveSas_Type = Gauge32
_RuijieIPSec2GlobalActiveSas_Object = MibScalar
ruijieIPSec2GlobalActiveSas = _RuijieIPSec2GlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 2),
    _RuijieIPSec2GlobalActiveSas_Type()
)
ruijieIPSec2GlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalActiveSas.setStatus("current")
_RuijieIPSec2GlobalInOctets_Type = Counter64
_RuijieIPSec2GlobalInOctets_Object = MibScalar
ruijieIPSec2GlobalInOctets = _RuijieIPSec2GlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 3),
    _RuijieIPSec2GlobalInOctets_Type()
)
ruijieIPSec2GlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalInOctets.setStatus("current")
_RuijieIPSec2GlobalInPkts_Type = Counter64
_RuijieIPSec2GlobalInPkts_Object = MibScalar
ruijieIPSec2GlobalInPkts = _RuijieIPSec2GlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 4),
    _RuijieIPSec2GlobalInPkts_Type()
)
ruijieIPSec2GlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalInPkts.setStatus("current")
_RuijieIPSec2GlobalInSpeed_Type = Counter64
_RuijieIPSec2GlobalInSpeed_Object = MibScalar
ruijieIPSec2GlobalInSpeed = _RuijieIPSec2GlobalInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 5),
    _RuijieIPSec2GlobalInSpeed_Type()
)
ruijieIPSec2GlobalInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalInSpeed.setStatus("current")
_RuijieIPSec2GlobalInDrops_Type = Counter64
_RuijieIPSec2GlobalInDrops_Object = MibScalar
ruijieIPSec2GlobalInDrops = _RuijieIPSec2GlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 6),
    _RuijieIPSec2GlobalInDrops_Type()
)
ruijieIPSec2GlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalInDrops.setStatus("current")
_RuijieIPSec2GlobalOutOctets_Type = Counter64
_RuijieIPSec2GlobalOutOctets_Object = MibScalar
ruijieIPSec2GlobalOutOctets = _RuijieIPSec2GlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 7),
    _RuijieIPSec2GlobalOutOctets_Type()
)
ruijieIPSec2GlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalOutOctets.setStatus("current")
_RuijieIPSec2GlobalOutPkts_Type = Counter64
_RuijieIPSec2GlobalOutPkts_Object = MibScalar
ruijieIPSec2GlobalOutPkts = _RuijieIPSec2GlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 8),
    _RuijieIPSec2GlobalOutPkts_Type()
)
ruijieIPSec2GlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalOutPkts.setStatus("current")
_RuijieIPSec2GlobalOutSpeed_Type = Counter64
_RuijieIPSec2GlobalOutSpeed_Object = MibScalar
ruijieIPSec2GlobalOutSpeed = _RuijieIPSec2GlobalOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 9),
    _RuijieIPSec2GlobalOutSpeed_Type()
)
ruijieIPSec2GlobalOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalOutSpeed.setStatus("current")
_RuijieIPSec2GlobalOutDrops_Type = Counter64
_RuijieIPSec2GlobalOutDrops_Object = MibScalar
ruijieIPSec2GlobalOutDrops = _RuijieIPSec2GlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 5, 10),
    _RuijieIPSec2GlobalOutDrops_Type()
)
ruijieIPSec2GlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalOutDrops.setStatus("current")
_RuijieIPSec2TrapObject_ObjectIdentity = ObjectIdentity
ruijieIPSec2TrapObject = _RuijieIPSec2TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 6)
)
_RuijieIPSec2MapName_Type = DisplayString
_RuijieIPSec2MapName_Object = MibScalar
ruijieIPSec2MapName = _RuijieIPSec2MapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 6, 1),
    _RuijieIPSec2MapName_Type()
)
ruijieIPSec2MapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPSec2MapName.setStatus("current")
_RuijieIPSec2SeqNum_Type = Integer32
_RuijieIPSec2SeqNum_Object = MibScalar
ruijieIPSec2SeqNum = _RuijieIPSec2SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 6, 2),
    _RuijieIPSec2SeqNum_Type()
)
ruijieIPSec2SeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPSec2SeqNum.setStatus("current")
_RuijieIPSec2SpiValue_Type = Integer32
_RuijieIPSec2SpiValue_Object = MibScalar
ruijieIPSec2SpiValue = _RuijieIPSec2SpiValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 6, 3),
    _RuijieIPSec2SpiValue_Type()
)
ruijieIPSec2SpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPSec2SpiValue.setStatus("current")
_RuijieIPSec2Trap_ObjectIdentity = ObjectIdentity
ruijieIPSec2Trap = _RuijieIPSec2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 7)
)
_RuijieIPSec2Notifications_ObjectIdentity = ObjectIdentity
ruijieIPSec2Notifications = _RuijieIPSec2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 7, 1)
)
_RuijieIPSec2Conformance_ObjectIdentity = ObjectIdentity
ruijieIPSec2Conformance = _RuijieIPSec2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2)
)
_RuijieIPSec2Compliances_ObjectIdentity = ObjectIdentity
ruijieIPSec2Compliances = _RuijieIPSec2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 1)
)
_RuijieIPSec2Groups_ObjectIdentity = ObjectIdentity
ruijieIPSec2Groups = _RuijieIPSec2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2)
)

# Managed Objects groups

ruijieIPSec2TunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 1)
)
ruijieIPSec2TunnelTableGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunIfIndex"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunLocalAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunLocalHostname"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteHostname"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunKeyType"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunEncapMode"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInitiator"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunLifeSize"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunLifeTime"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemainTime"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunActiveTime"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunCreateTime"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemainSize"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunTotalRefreshes"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunCurrentSaInstances"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInSaEncryptAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInSaAhAuthAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInSaEspAuthAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunDiffHellmanGrp"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutSaEncryptAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutSaAhAuthAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutSaEspAuthAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunMapName"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunSeqNum"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunStatus"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInDecompOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInSpeed"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInDropPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutUncompOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutSpeed"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutDropPkts"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelTableGroup.setStatus("current")

ruijieIPSec2TunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 2)
)
ruijieIPSec2TunnelStatGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInDecompOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInSpeed"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunInDropPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutUncompOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutSpeed"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunOutDropPkts"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelStatGroup.setStatus("current")

ruijieIPSec2SaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 3)
)
ruijieIPSec2SaGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaIndex"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaDirection"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaValue"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaProtocol"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaEncryptAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaAuthAlgo"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaStatus"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2SaGroup.setStatus("current")

ruijieIPSec2TrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 4)
)
ruijieIPSec2TrafficTableGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalType"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr1"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr2"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalProtocol"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalPort"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr1"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr2"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemotePort"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalHostname"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteType"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteProtocol"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteHostname"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TrafficTableGroup.setStatus("current")

ruijieIPSec2GlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 5)
)
ruijieIPSec2GlobalStatsGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalActiveTunnels"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalActiveSas"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalInOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalInPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalInSpeed"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalInDrops"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalOutOctets"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalOutPkts"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalOutSpeed"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalOutDrops"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2GlobalStatsGroup.setStatus("current")

ruijieIPSec2TrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 6)
)
ruijieIPSec2TrapObjectGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2MapName"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SeqNum"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SpiValue"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TrapObjectGroup.setStatus("current")


# Notification objects

ruijieIPSec2TunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 7, 1, 1)
)
ruijieIPSec2TunnelStart.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunIfIndex"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalType"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr1"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr2"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalProtocol"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalPort"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr1"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr2"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemotePort"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteDomain"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunLocalAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2LastTunRemoteAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SystemSerialNumber"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelStart.setStatus(
        "current"
    )

ruijieIPSec2TunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 1, 7, 1, 2)
)
ruijieIPSec2TunnelStop.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunIfIndex"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalType"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr1"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalAddr2"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalProtocol"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficLocalPort"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr1"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemoteAddr2"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficRemotePort"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunRemoteDomain"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunLocalAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2LastTunRemoteAddr"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SystemSerialNumber"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TunnelStop.setStatus(
        "current"
    )


# Notifications groups

ruijieIPSec2TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 2, 7)
)
ruijieIPSec2TrapGroup.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunnelStart"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunnelStop"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieIPSec2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 108, 2, 1, 1)
)
ruijieIPSec2Compliance.setObjects(
      *(("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunnelTableGroup"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TunnelStatGroup"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2SaGroup"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrafficTableGroup"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2GlobalStatsGroup"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrapObjectGroup"),
        ("RUIJIE-IPSEC2-MIB", "ruijieIPSec2TrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieIPSec2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IPSEC2-MIB",
    **{"RuijieIPSecNegoType": RuijieIPSecNegoType,
       "RuijieEncapMode": RuijieEncapMode,
       "RuijieEncryptAlgo": RuijieEncryptAlgo,
       "RuijieAuthAlgo": RuijieAuthAlgo,
       "RuijieDiffHellmanGrp": RuijieDiffHellmanGrp,
       "RuijieIPSecTunnelState": RuijieIPSecTunnelState,
       "RuijieSaProtocol": RuijieSaProtocol,
       "RuijieTrafficType": RuijieTrafficType,
       "RuijieIPSec2NegoType": RuijieIPSec2NegoType,
       "RuijieIPSec2TunnelState": RuijieIPSec2TunnelState,
       "ruijieIPSec2MibModule": ruijieIPSec2MibModule,
       "ruijieIPSec2Objects": ruijieIPSec2Objects,
       "ruijieIPSec2TunnelTable": ruijieIPSec2TunnelTable,
       "ruijieIPSec2TunnelEntry": ruijieIPSec2TunnelEntry,
       "ruijieIPSec2TunIfIndex": ruijieIPSec2TunIfIndex,
       "ruijieIPSec2TunnelTrafficIndex": ruijieIPSec2TunnelTrafficIndex,
       "ruijieIPSec2TunIndex": ruijieIPSec2TunIndex,
       "ruijieIPSec2TunIKETunnelIndex": ruijieIPSec2TunIKETunnelIndex,
       "ruijieIPSec2TunnelAhOutSaIndex": ruijieIPSec2TunnelAhOutSaIndex,
       "ruijieIPSec2TunnelAhInSaIndex": ruijieIPSec2TunnelAhInSaIndex,
       "ruijieIPSec2TunnelEspOutSaIndex": ruijieIPSec2TunnelEspOutSaIndex,
       "ruijieIPSec2TunnelEspInSaIndex": ruijieIPSec2TunnelEspInSaIndex,
       "ruijieIPSec2TunLocalAddr": ruijieIPSec2TunLocalAddr,
       "ruijieIPSec2TunRemoteAddr": ruijieIPSec2TunRemoteAddr,
       "ruijieIPSec2TunLocalHostname": ruijieIPSec2TunLocalHostname,
       "ruijieIPSec2TunRemoteHostname": ruijieIPSec2TunRemoteHostname,
       "ruijieIPSec2TunKeyType": ruijieIPSec2TunKeyType,
       "ruijieIPSec2TunEncapMode": ruijieIPSec2TunEncapMode,
       "ruijieIPSec2TunInitiator": ruijieIPSec2TunInitiator,
       "ruijieIPSec2TunLifeSize": ruijieIPSec2TunLifeSize,
       "ruijieIPSec2TunLifeTime": ruijieIPSec2TunLifeTime,
       "ruijieIPSec2TunRemainTime": ruijieIPSec2TunRemainTime,
       "ruijieIPSec2TunActiveTime": ruijieIPSec2TunActiveTime,
       "ruijieIPSec2TunCreateTime": ruijieIPSec2TunCreateTime,
       "ruijieIPSec2TunRemainSize": ruijieIPSec2TunRemainSize,
       "ruijieIPSec2TunTotalRefreshes": ruijieIPSec2TunTotalRefreshes,
       "ruijieIPSec2TunCurrentSaInstances": ruijieIPSec2TunCurrentSaInstances,
       "ruijieIPSec2TunInSaEncryptAlgo": ruijieIPSec2TunInSaEncryptAlgo,
       "ruijieIPSec2TunInSaAhAuthAlgo": ruijieIPSec2TunInSaAhAuthAlgo,
       "ruijieIPSec2TunInSaEspAuthAlgo": ruijieIPSec2TunInSaEspAuthAlgo,
       "ruijieIPSec2TunDiffHellmanGrp": ruijieIPSec2TunDiffHellmanGrp,
       "ruijieIPSec2TunOutSaEncryptAlgo": ruijieIPSec2TunOutSaEncryptAlgo,
       "ruijieIPSec2TunOutSaAhAuthAlgo": ruijieIPSec2TunOutSaAhAuthAlgo,
       "ruijieIPSec2TunOutSaEspAuthAlgo": ruijieIPSec2TunOutSaEspAuthAlgo,
       "ruijieIPSec2TunMapName": ruijieIPSec2TunMapName,
       "ruijieIPSec2TunSeqNum": ruijieIPSec2TunSeqNum,
       "ruijieIPSec2TunStatus": ruijieIPSec2TunStatus,
       "ruijieIPSec2TunRemoteDomain": ruijieIPSec2TunRemoteDomain,
       "ruijieIPSec2LastTunRemoteAddr": ruijieIPSec2LastTunRemoteAddr,
       "ruijieIPSec2SystemSerialNumber": ruijieIPSec2SystemSerialNumber,
       "ruijieIPSec2TunnelStatTable": ruijieIPSec2TunnelStatTable,
       "ruijieIPSec2TunnelStatEntry": ruijieIPSec2TunnelStatEntry,
       "ruijieIPSec2TunInOctets": ruijieIPSec2TunInOctets,
       "ruijieIPSec2TunInDecompOctets": ruijieIPSec2TunInDecompOctets,
       "ruijieIPSec2TunInPkts": ruijieIPSec2TunInPkts,
       "ruijieIPSec2TunInSpeed": ruijieIPSec2TunInSpeed,
       "ruijieIPSec2TunInDropPkts": ruijieIPSec2TunInDropPkts,
       "ruijieIPSec2TunOutOctets": ruijieIPSec2TunOutOctets,
       "ruijieIPSec2TunOutUncompOctets": ruijieIPSec2TunOutUncompOctets,
       "ruijieIPSec2TunOutPkts": ruijieIPSec2TunOutPkts,
       "ruijieIPSec2TunOutSpeed": ruijieIPSec2TunOutSpeed,
       "ruijieIPSec2TunOutDropPkts": ruijieIPSec2TunOutDropPkts,
       "ruijieIPSec2SaTable": ruijieIPSec2SaTable,
       "ruijieIPSec2SaEntry": ruijieIPSec2SaEntry,
       "ruijieIPSec2SaIndex": ruijieIPSec2SaIndex,
       "ruijieIPSec2SaDirection": ruijieIPSec2SaDirection,
       "ruijieIPSec2SaValue": ruijieIPSec2SaValue,
       "ruijieIPSec2SaProtocol": ruijieIPSec2SaProtocol,
       "ruijieIPSec2SaEncryptAlgo": ruijieIPSec2SaEncryptAlgo,
       "ruijieIPSec2SaAuthAlgo": ruijieIPSec2SaAuthAlgo,
       "ruijieIPSec2SaStatus": ruijieIPSec2SaStatus,
       "ruijieIPSec2TrafficTable": ruijieIPSec2TrafficTable,
       "ruijieIPSec2TrafficEntry": ruijieIPSec2TrafficEntry,
       "ruijieIPSec2TrafficIndex": ruijieIPSec2TrafficIndex,
       "ruijieIPSec2TrafficLocalType": ruijieIPSec2TrafficLocalType,
       "ruijieIPSec2TrafficLocalAddr1": ruijieIPSec2TrafficLocalAddr1,
       "ruijieIPSec2TrafficLocalAddr2": ruijieIPSec2TrafficLocalAddr2,
       "ruijieIPSec2TrafficLocalProtocol": ruijieIPSec2TrafficLocalProtocol,
       "ruijieIPSec2TrafficLocalPort": ruijieIPSec2TrafficLocalPort,
       "ruijieIPSec2TrafficLocalHostname": ruijieIPSec2TrafficLocalHostname,
       "ruijieIPSec2TrafficRemoteType": ruijieIPSec2TrafficRemoteType,
       "ruijieIPSec2TrafficRemoteAddr1": ruijieIPSec2TrafficRemoteAddr1,
       "ruijieIPSec2TrafficRemoteAddr2": ruijieIPSec2TrafficRemoteAddr2,
       "ruijieIPSec2TrafficRemoteProtocol": ruijieIPSec2TrafficRemoteProtocol,
       "ruijieIPSec2TrafficRemotePort": ruijieIPSec2TrafficRemotePort,
       "ruijieIPSec2TrafficRemoteHostname": ruijieIPSec2TrafficRemoteHostname,
       "ruijieIPSec2GlobalStats": ruijieIPSec2GlobalStats,
       "ruijieIPSec2GlobalActiveTunnels": ruijieIPSec2GlobalActiveTunnels,
       "ruijieIPSec2GlobalActiveSas": ruijieIPSec2GlobalActiveSas,
       "ruijieIPSec2GlobalInOctets": ruijieIPSec2GlobalInOctets,
       "ruijieIPSec2GlobalInPkts": ruijieIPSec2GlobalInPkts,
       "ruijieIPSec2GlobalInSpeed": ruijieIPSec2GlobalInSpeed,
       "ruijieIPSec2GlobalInDrops": ruijieIPSec2GlobalInDrops,
       "ruijieIPSec2GlobalOutOctets": ruijieIPSec2GlobalOutOctets,
       "ruijieIPSec2GlobalOutPkts": ruijieIPSec2GlobalOutPkts,
       "ruijieIPSec2GlobalOutSpeed": ruijieIPSec2GlobalOutSpeed,
       "ruijieIPSec2GlobalOutDrops": ruijieIPSec2GlobalOutDrops,
       "ruijieIPSec2TrapObject": ruijieIPSec2TrapObject,
       "ruijieIPSec2MapName": ruijieIPSec2MapName,
       "ruijieIPSec2SeqNum": ruijieIPSec2SeqNum,
       "ruijieIPSec2SpiValue": ruijieIPSec2SpiValue,
       "ruijieIPSec2Trap": ruijieIPSec2Trap,
       "ruijieIPSec2Notifications": ruijieIPSec2Notifications,
       "ruijieIPSec2TunnelStart": ruijieIPSec2TunnelStart,
       "ruijieIPSec2TunnelStop": ruijieIPSec2TunnelStop,
       "ruijieIPSec2Conformance": ruijieIPSec2Conformance,
       "ruijieIPSec2Compliances": ruijieIPSec2Compliances,
       "ruijieIPSec2Compliance": ruijieIPSec2Compliance,
       "ruijieIPSec2Groups": ruijieIPSec2Groups,
       "ruijieIPSec2TunnelTableGroup": ruijieIPSec2TunnelTableGroup,
       "ruijieIPSec2TunnelStatGroup": ruijieIPSec2TunnelStatGroup,
       "ruijieIPSec2SaGroup": ruijieIPSec2SaGroup,
       "ruijieIPSec2TrafficTableGroup": ruijieIPSec2TrafficTableGroup,
       "ruijieIPSec2GlobalStatsGroup": ruijieIPSec2GlobalStatsGroup,
       "ruijieIPSec2TrapObjectGroup": ruijieIPSec2TrapObjectGroup,
       "ruijieIPSec2TrapGroup": ruijieIPSec2TrapGroup}
)
