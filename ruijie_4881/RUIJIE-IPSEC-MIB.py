# SNMP MIB module (RUIJIE-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IPSEC-MIB.mib
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

ruijieIPSecMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94)
)
if mibBuilder.loadTexts:
    ruijieIPSecMonitor.setRevisions(
        ("2011-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieDiffHellmanGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("modp768", 1),
          ("modp1024", 2),
          ("invalidMode", 2147483647))
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
              1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1),
          ("sha", 2),
          ("invalidAlg", 2147483647))
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



class RuijieTunnelProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              17,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ip", 4),
          ("tcp", 6),
          ("udp", 17),
          ("esp", 50),
          ("ah", 51))
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



# MIB Managed Objects in the order of their OIDs

_RuijieIPSecObjects_ObjectIdentity = ObjectIdentity
ruijieIPSecObjects = _RuijieIPSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1)
)
_RuijieIPSecTunnelTable_Object = MibTable
ruijieIPSecTunnelTable = _RuijieIPSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelTable.setStatus("current")
_RuijieIPSecTunnelEntry_Object = MibTableRow
ruijieIPSecTunnelEntry = _RuijieIPSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1)
)
ruijieIPSecTunnelEntry.setIndexNames(
    (0, "RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelEntry.setStatus("current")


class _RuijieIPSecTunIfIndex_Type(Integer32):
    """Custom type ruijieIPSecTunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecTunIfIndex_Type.__name__ = "Integer32"
_RuijieIPSecTunIfIndex_Object = MibTableColumn
ruijieIPSecTunIfIndex = _RuijieIPSecTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 1),
    _RuijieIPSecTunIfIndex_Type()
)
ruijieIPSecTunIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIPSecTunIfIndex.setStatus("current")


class _RuijieIPSecTunIndex_Type(Integer32):
    """Custom type ruijieIPSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecTunIndex_Type.__name__ = "Integer32"
_RuijieIPSecTunIndex_Object = MibTableColumn
ruijieIPSecTunIndex = _RuijieIPSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 2),
    _RuijieIPSecTunIndex_Type()
)
ruijieIPSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIPSecTunIndex.setStatus("current")


class _RuijieIPSecTunIKETunnelIndex_Type(Integer32):
    """Custom type ruijieIPSecTunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecTunIKETunnelIndex_Type.__name__ = "Integer32"
_RuijieIPSecTunIKETunnelIndex_Object = MibTableColumn
ruijieIPSecTunIKETunnelIndex = _RuijieIPSecTunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 3),
    _RuijieIPSecTunIKETunnelIndex_Type()
)
ruijieIPSecTunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunIKETunnelIndex.setStatus("current")
_RuijieIPSecTunLocalAddr_Type = IpAddress
_RuijieIPSecTunLocalAddr_Object = MibTableColumn
ruijieIPSecTunLocalAddr = _RuijieIPSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 4),
    _RuijieIPSecTunLocalAddr_Type()
)
ruijieIPSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunLocalAddr.setStatus("current")
_RuijieIPSecTunRemoteAddr_Type = IpAddress
_RuijieIPSecTunRemoteAddr_Object = MibTableColumn
ruijieIPSecTunRemoteAddr = _RuijieIPSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 5),
    _RuijieIPSecTunRemoteAddr_Type()
)
ruijieIPSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunRemoteAddr.setStatus("current")
_RuijieIPSecTunLocalHostname_Type = DisplayString
_RuijieIPSecTunLocalHostname_Object = MibTableColumn
ruijieIPSecTunLocalHostname = _RuijieIPSecTunLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 6),
    _RuijieIPSecTunLocalHostname_Type()
)
ruijieIPSecTunLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunLocalHostname.setStatus("current")
_RuijieIPSecTunRemoteHostname_Type = DisplayString
_RuijieIPSecTunRemoteHostname_Object = MibTableColumn
ruijieIPSecTunRemoteHostname = _RuijieIPSecTunRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 7),
    _RuijieIPSecTunRemoteHostname_Type()
)
ruijieIPSecTunRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunRemoteHostname.setStatus("current")
_RuijieIPSecTunKeyType_Type = RuijieIPSecNegoType
_RuijieIPSecTunKeyType_Object = MibTableColumn
ruijieIPSecTunKeyType = _RuijieIPSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 8),
    _RuijieIPSecTunKeyType_Type()
)
ruijieIPSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunKeyType.setStatus("current")
_RuijieIPSecTunEncapMode_Type = RuijieEncapMode
_RuijieIPSecTunEncapMode_Object = MibTableColumn
ruijieIPSecTunEncapMode = _RuijieIPSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 9),
    _RuijieIPSecTunEncapMode_Type()
)
ruijieIPSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunEncapMode.setStatus("current")


class _RuijieIPSecTunInitiator_Type(Integer32):
    """Custom type ruijieIPSecTunInitiator based on Integer32"""
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


_RuijieIPSecTunInitiator_Type.__name__ = "Integer32"
_RuijieIPSecTunInitiator_Object = MibTableColumn
ruijieIPSecTunInitiator = _RuijieIPSecTunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 10),
    _RuijieIPSecTunInitiator_Type()
)
ruijieIPSecTunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInitiator.setStatus("current")


class _RuijieIPSecTunLifeSize_Type(Integer32):
    """Custom type ruijieIPSecTunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecTunLifeSize_Type.__name__ = "Integer32"
_RuijieIPSecTunLifeSize_Object = MibTableColumn
ruijieIPSecTunLifeSize = _RuijieIPSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 11),
    _RuijieIPSecTunLifeSize_Type()
)
ruijieIPSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunLifeSize.setStatus("current")


class _RuijieIPSecTunLifeTime_Type(Integer32):
    """Custom type ruijieIPSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecTunLifeTime_Type.__name__ = "Integer32"
_RuijieIPSecTunLifeTime_Object = MibTableColumn
ruijieIPSecTunLifeTime = _RuijieIPSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 12),
    _RuijieIPSecTunLifeTime_Type()
)
ruijieIPSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunLifeTime.setStatus("current")


class _RuijieIPSecTunRemainTime_Type(Integer32):
    """Custom type ruijieIPSecTunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSecTunRemainTime_Type.__name__ = "Integer32"
_RuijieIPSecTunRemainTime_Object = MibTableColumn
ruijieIPSecTunRemainTime = _RuijieIPSecTunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 13),
    _RuijieIPSecTunRemainTime_Type()
)
ruijieIPSecTunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunRemainTime.setStatus("current")


class _RuijieIPSecTunActiveTime_Type(Integer32):
    """Custom type ruijieIPSecTunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSecTunActiveTime_Type.__name__ = "Integer32"
_RuijieIPSecTunActiveTime_Object = MibTableColumn
ruijieIPSecTunActiveTime = _RuijieIPSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 14),
    _RuijieIPSecTunActiveTime_Type()
)
ruijieIPSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunActiveTime.setStatus("current")


class _RuijieIPSecTunCreateTime_Type(Integer32):
    """Custom type ruijieIPSecTunCreateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSecTunCreateTime_Type.__name__ = "Integer32"
_RuijieIPSecTunCreateTime_Object = MibTableColumn
ruijieIPSecTunCreateTime = _RuijieIPSecTunCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 15),
    _RuijieIPSecTunCreateTime_Type()
)
ruijieIPSecTunCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunCreateTime.setStatus("current")


class _RuijieIPSecTunRemainSize_Type(Integer32):
    """Custom type ruijieIPSecTunRemainSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIPSecTunRemainSize_Type.__name__ = "Integer32"
_RuijieIPSecTunRemainSize_Object = MibTableColumn
ruijieIPSecTunRemainSize = _RuijieIPSecTunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 16),
    _RuijieIPSecTunRemainSize_Type()
)
ruijieIPSecTunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunRemainSize.setStatus("current")
_RuijieIPSecTunTotalRefreshes_Type = Counter32
_RuijieIPSecTunTotalRefreshes_Object = MibTableColumn
ruijieIPSecTunTotalRefreshes = _RuijieIPSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 17),
    _RuijieIPSecTunTotalRefreshes_Type()
)
ruijieIPSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunTotalRefreshes.setStatus("current")
_RuijieIPSecTunCurrentSaInstances_Type = Gauge32
_RuijieIPSecTunCurrentSaInstances_Object = MibTableColumn
ruijieIPSecTunCurrentSaInstances = _RuijieIPSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 18),
    _RuijieIPSecTunCurrentSaInstances_Type()
)
ruijieIPSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunCurrentSaInstances.setStatus("current")
_RuijieIPSecTunInSaEncryptAlgo_Type = RuijieEncryptAlgo
_RuijieIPSecTunInSaEncryptAlgo_Object = MibTableColumn
ruijieIPSecTunInSaEncryptAlgo = _RuijieIPSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 19),
    _RuijieIPSecTunInSaEncryptAlgo_Type()
)
ruijieIPSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInSaEncryptAlgo.setStatus("current")
_RuijieIPSecTunInSaAhAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSecTunInSaAhAuthAlgo_Object = MibTableColumn
ruijieIPSecTunInSaAhAuthAlgo = _RuijieIPSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 20),
    _RuijieIPSecTunInSaAhAuthAlgo_Type()
)
ruijieIPSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInSaAhAuthAlgo.setStatus("current")
_RuijieIPSecTunInSaEspAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSecTunInSaEspAuthAlgo_Object = MibTableColumn
ruijieIPSecTunInSaEspAuthAlgo = _RuijieIPSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 21),
    _RuijieIPSecTunInSaEspAuthAlgo_Type()
)
ruijieIPSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInSaEspAuthAlgo.setStatus("current")
_RuijieIPSecTunDiffHellmanGrp_Type = RuijieDiffHellmanGrp
_RuijieIPSecTunDiffHellmanGrp_Object = MibTableColumn
ruijieIPSecTunDiffHellmanGrp = _RuijieIPSecTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 22),
    _RuijieIPSecTunDiffHellmanGrp_Type()
)
ruijieIPSecTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunDiffHellmanGrp.setStatus("current")
_RuijieIPSecTunOutSaEncryptAlgo_Type = RuijieEncryptAlgo
_RuijieIPSecTunOutSaEncryptAlgo_Object = MibTableColumn
ruijieIPSecTunOutSaEncryptAlgo = _RuijieIPSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 23),
    _RuijieIPSecTunOutSaEncryptAlgo_Type()
)
ruijieIPSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutSaEncryptAlgo.setStatus("current")
_RuijieIPSecTunOutSaAhAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSecTunOutSaAhAuthAlgo_Object = MibTableColumn
ruijieIPSecTunOutSaAhAuthAlgo = _RuijieIPSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 24),
    _RuijieIPSecTunOutSaAhAuthAlgo_Type()
)
ruijieIPSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutSaAhAuthAlgo.setStatus("current")
_RuijieIPSecTunOutSaEspAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSecTunOutSaEspAuthAlgo_Object = MibTableColumn
ruijieIPSecTunOutSaEspAuthAlgo = _RuijieIPSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 25),
    _RuijieIPSecTunOutSaEspAuthAlgo_Type()
)
ruijieIPSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutSaEspAuthAlgo.setStatus("current")
_RuijieIPSecTunMapName_Type = DisplayString
_RuijieIPSecTunMapName_Object = MibTableColumn
ruijieIPSecTunMapName = _RuijieIPSecTunMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 26),
    _RuijieIPSecTunMapName_Type()
)
ruijieIPSecTunMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunMapName.setStatus("current")


class _RuijieIPSecTunSeqNum_Type(Integer32):
    """Custom type ruijieIPSecTunSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecTunSeqNum_Type.__name__ = "Integer32"
_RuijieIPSecTunSeqNum_Object = MibTableColumn
ruijieIPSecTunSeqNum = _RuijieIPSecTunSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 27),
    _RuijieIPSecTunSeqNum_Type()
)
ruijieIPSecTunSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunSeqNum.setStatus("current")
_RuijieIPSecTunStatus_Type = RuijieIPSecTunnelState
_RuijieIPSecTunStatus_Object = MibTableColumn
ruijieIPSecTunStatus = _RuijieIPSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 1, 1, 28),
    _RuijieIPSecTunStatus_Type()
)
ruijieIPSecTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSecTunStatus.setStatus("current")
_RuijieIPSecTunnelStatTable_Object = MibTable
ruijieIPSecTunnelStatTable = _RuijieIPSecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelStatTable.setStatus("current")
_RuijieIPSecTunnelStatEntry_Object = MibTableRow
ruijieIPSecTunnelStatEntry = _RuijieIPSecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1)
)
ruijieIPSecTunnelStatEntry.setIndexNames(
    (0, "RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelStatEntry.setStatus("current")
_RuijieIPSecTunInOctets_Type = Counter64
_RuijieIPSecTunInOctets_Object = MibTableColumn
ruijieIPSecTunInOctets = _RuijieIPSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 1),
    _RuijieIPSecTunInOctets_Type()
)
ruijieIPSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInOctets.setStatus("current")
_RuijieIPSecTunInDecompOctets_Type = Counter64
_RuijieIPSecTunInDecompOctets_Object = MibTableColumn
ruijieIPSecTunInDecompOctets = _RuijieIPSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 2),
    _RuijieIPSecTunInDecompOctets_Type()
)
ruijieIPSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInDecompOctets.setStatus("current")
_RuijieIPSecTunInPkts_Type = Counter64
_RuijieIPSecTunInPkts_Object = MibTableColumn
ruijieIPSecTunInPkts = _RuijieIPSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 3),
    _RuijieIPSecTunInPkts_Type()
)
ruijieIPSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInPkts.setStatus("current")
_RuijieIPSecTunInSpeed_Type = Counter64
_RuijieIPSecTunInSpeed_Object = MibTableColumn
ruijieIPSecTunInSpeed = _RuijieIPSecTunInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 4),
    _RuijieIPSecTunInSpeed_Type()
)
ruijieIPSecTunInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInSpeed.setStatus("current")
_RuijieIPSecTunInDropPkts_Type = Counter64
_RuijieIPSecTunInDropPkts_Object = MibTableColumn
ruijieIPSecTunInDropPkts = _RuijieIPSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 5),
    _RuijieIPSecTunInDropPkts_Type()
)
ruijieIPSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunInDropPkts.setStatus("current")
_RuijieIPSecTunOutOctets_Type = Counter64
_RuijieIPSecTunOutOctets_Object = MibTableColumn
ruijieIPSecTunOutOctets = _RuijieIPSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 6),
    _RuijieIPSecTunOutOctets_Type()
)
ruijieIPSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutOctets.setStatus("current")
_RuijieIPSecTunOutUncompOctets_Type = Counter64
_RuijieIPSecTunOutUncompOctets_Object = MibTableColumn
ruijieIPSecTunOutUncompOctets = _RuijieIPSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 7),
    _RuijieIPSecTunOutUncompOctets_Type()
)
ruijieIPSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutUncompOctets.setStatus("current")
_RuijieIPSecTunOutPkts_Type = Counter64
_RuijieIPSecTunOutPkts_Object = MibTableColumn
ruijieIPSecTunOutPkts = _RuijieIPSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 8),
    _RuijieIPSecTunOutPkts_Type()
)
ruijieIPSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutPkts.setStatus("current")
_RuijieIPSecTunOutSpeed_Type = Counter64
_RuijieIPSecTunOutSpeed_Object = MibTableColumn
ruijieIPSecTunOutSpeed = _RuijieIPSecTunOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 9),
    _RuijieIPSecTunOutSpeed_Type()
)
ruijieIPSecTunOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutSpeed.setStatus("current")
_RuijieIPSecTunOutDropPkts_Type = Counter64
_RuijieIPSecTunOutDropPkts_Object = MibTableColumn
ruijieIPSecTunOutDropPkts = _RuijieIPSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 2, 1, 10),
    _RuijieIPSecTunOutDropPkts_Type()
)
ruijieIPSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTunOutDropPkts.setStatus("current")
_RuijieIPSecSaTable_Object = MibTable
ruijieIPSecSaTable = _RuijieIPSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieIPSecSaTable.setStatus("current")
_RuijieIPSecSaEntry_Object = MibTableRow
ruijieIPSecSaEntry = _RuijieIPSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1)
)
ruijieIPSecSaEntry.setIndexNames(
    (0, "RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    ruijieIPSecSaEntry.setStatus("current")


class _RuijieIPSecSaIndex_Type(Integer32):
    """Custom type ruijieIPSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieIPSecSaIndex_Type.__name__ = "Integer32"
_RuijieIPSecSaIndex_Object = MibTableColumn
ruijieIPSecSaIndex = _RuijieIPSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 1),
    _RuijieIPSecSaIndex_Type()
)
ruijieIPSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIPSecSaIndex.setStatus("current")


class _RuijieIPSecSaDirection_Type(Integer32):
    """Custom type ruijieIPSecSaDirection based on Integer32"""
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


_RuijieIPSecSaDirection_Type.__name__ = "Integer32"
_RuijieIPSecSaDirection_Object = MibTableColumn
ruijieIPSecSaDirection = _RuijieIPSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 2),
    _RuijieIPSecSaDirection_Type()
)
ruijieIPSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecSaDirection.setStatus("current")


class _RuijieIPSecSaValue_Type(Unsigned32):
    """Custom type ruijieIPSecSaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuijieIPSecSaValue_Type.__name__ = "Unsigned32"
_RuijieIPSecSaValue_Object = MibTableColumn
ruijieIPSecSaValue = _RuijieIPSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 3),
    _RuijieIPSecSaValue_Type()
)
ruijieIPSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecSaValue.setStatus("current")
_RuijieIPSecSaProtocol_Type = RuijieSaProtocol
_RuijieIPSecSaProtocol_Object = MibTableColumn
ruijieIPSecSaProtocol = _RuijieIPSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 4),
    _RuijieIPSecSaProtocol_Type()
)
ruijieIPSecSaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecSaProtocol.setStatus("current")
_RuijieIPSecSaEncryptAlgo_Type = RuijieEncryptAlgo
_RuijieIPSecSaEncryptAlgo_Object = MibTableColumn
ruijieIPSecSaEncryptAlgo = _RuijieIPSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 5),
    _RuijieIPSecSaEncryptAlgo_Type()
)
ruijieIPSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecSaEncryptAlgo.setStatus("current")
_RuijieIPSecSaAuthAlgo_Type = RuijieAuthAlgo
_RuijieIPSecSaAuthAlgo_Object = MibTableColumn
ruijieIPSecSaAuthAlgo = _RuijieIPSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 6),
    _RuijieIPSecSaAuthAlgo_Type()
)
ruijieIPSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecSaAuthAlgo.setStatus("current")
_RuijieIPSecSaStatus_Type = RuijieIPSecTunnelState
_RuijieIPSecSaStatus_Object = MibTableColumn
ruijieIPSecSaStatus = _RuijieIPSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 3, 1, 7),
    _RuijieIPSecSaStatus_Type()
)
ruijieIPSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecSaStatus.setStatus("current")
_RuijieIPSecTrafficTable_Object = MibTable
ruijieIPSecTrafficTable = _RuijieIPSecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieIPSecTrafficTable.setStatus("current")
_RuijieIPSecTrafficEntry_Object = MibTableRow
ruijieIPSecTrafficEntry = _RuijieIPSecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1)
)
ruijieIPSecTrafficEntry.setIndexNames(
    (0, "RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    ruijieIPSecTrafficEntry.setStatus("current")
_RuijieIPSecTrafficLocalType_Type = RuijieTrafficType
_RuijieIPSecTrafficLocalType_Object = MibTableColumn
ruijieIPSecTrafficLocalType = _RuijieIPSecTrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 1),
    _RuijieIPSecTrafficLocalType_Type()
)
ruijieIPSecTrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficLocalType.setStatus("current")
_RuijieIPSecTrafficLocalAddr1_Type = IpAddress
_RuijieIPSecTrafficLocalAddr1_Object = MibTableColumn
ruijieIPSecTrafficLocalAddr1 = _RuijieIPSecTrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 2),
    _RuijieIPSecTrafficLocalAddr1_Type()
)
ruijieIPSecTrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficLocalAddr1.setStatus("current")
_RuijieIPSecTrafficLocalAddr2_Type = IpAddress
_RuijieIPSecTrafficLocalAddr2_Object = MibTableColumn
ruijieIPSecTrafficLocalAddr2 = _RuijieIPSecTrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 3),
    _RuijieIPSecTrafficLocalAddr2_Type()
)
ruijieIPSecTrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficLocalAddr2.setStatus("current")
_RuijieIPSecTrafficLocalProtocol_Type = RuijieTunnelProtocol
_RuijieIPSecTrafficLocalProtocol_Object = MibTableColumn
ruijieIPSecTrafficLocalProtocol = _RuijieIPSecTrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 4),
    _RuijieIPSecTrafficLocalProtocol_Type()
)
ruijieIPSecTrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficLocalProtocol.setStatus("current")


class _RuijieIPSecTrafficLocalPort_Type(Integer32):
    """Custom type ruijieIPSecTrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieIPSecTrafficLocalPort_Type.__name__ = "Integer32"
_RuijieIPSecTrafficLocalPort_Object = MibTableColumn
ruijieIPSecTrafficLocalPort = _RuijieIPSecTrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 5),
    _RuijieIPSecTrafficLocalPort_Type()
)
ruijieIPSecTrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficLocalPort.setStatus("current")
_RuijieIPSecTrafficLocalHostname_Type = DisplayString
_RuijieIPSecTrafficLocalHostname_Object = MibTableColumn
ruijieIPSecTrafficLocalHostname = _RuijieIPSecTrafficLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 6),
    _RuijieIPSecTrafficLocalHostname_Type()
)
ruijieIPSecTrafficLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficLocalHostname.setStatus("current")
_RuijieIPSecTrafficRemoteType_Type = RuijieTrafficType
_RuijieIPSecTrafficRemoteType_Object = MibTableColumn
ruijieIPSecTrafficRemoteType = _RuijieIPSecTrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 7),
    _RuijieIPSecTrafficRemoteType_Type()
)
ruijieIPSecTrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficRemoteType.setStatus("current")
_RuijieIPSecTrafficRemoteAddr1_Type = IpAddress
_RuijieIPSecTrafficRemoteAddr1_Object = MibTableColumn
ruijieIPSecTrafficRemoteAddr1 = _RuijieIPSecTrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 8),
    _RuijieIPSecTrafficRemoteAddr1_Type()
)
ruijieIPSecTrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficRemoteAddr1.setStatus("current")
_RuijieIPSecTrafficRemoteAddr2_Type = IpAddress
_RuijieIPSecTrafficRemoteAddr2_Object = MibTableColumn
ruijieIPSecTrafficRemoteAddr2 = _RuijieIPSecTrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 9),
    _RuijieIPSecTrafficRemoteAddr2_Type()
)
ruijieIPSecTrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficRemoteAddr2.setStatus("current")
_RuijieIPSecTrafficRemoteProtocol_Type = RuijieTunnelProtocol
_RuijieIPSecTrafficRemoteProtocol_Object = MibTableColumn
ruijieIPSecTrafficRemoteProtocol = _RuijieIPSecTrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 10),
    _RuijieIPSecTrafficRemoteProtocol_Type()
)
ruijieIPSecTrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficRemoteProtocol.setStatus("current")


class _RuijieIPSecTrafficRemotePort_Type(Integer32):
    """Custom type ruijieIPSecTrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieIPSecTrafficRemotePort_Type.__name__ = "Integer32"
_RuijieIPSecTrafficRemotePort_Object = MibTableColumn
ruijieIPSecTrafficRemotePort = _RuijieIPSecTrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 11),
    _RuijieIPSecTrafficRemotePort_Type()
)
ruijieIPSecTrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficRemotePort.setStatus("current")
_RuijieIPSecTrafficRemoteHostname_Type = DisplayString
_RuijieIPSecTrafficRemoteHostname_Object = MibTableColumn
ruijieIPSecTrafficRemoteHostname = _RuijieIPSecTrafficRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 4, 1, 12),
    _RuijieIPSecTrafficRemoteHostname_Type()
)
ruijieIPSecTrafficRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecTrafficRemoteHostname.setStatus("current")
_RuijieIPSecGlobalStats_ObjectIdentity = ObjectIdentity
ruijieIPSecGlobalStats = _RuijieIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5)
)
_RuijieIPSecGlobalActiveTunnels_Type = Gauge32
_RuijieIPSecGlobalActiveTunnels_Object = MibScalar
ruijieIPSecGlobalActiveTunnels = _RuijieIPSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 1),
    _RuijieIPSecGlobalActiveTunnels_Type()
)
ruijieIPSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalActiveTunnels.setStatus("current")
_RuijieIPSecGlobalActiveSas_Type = Gauge32
_RuijieIPSecGlobalActiveSas_Object = MibScalar
ruijieIPSecGlobalActiveSas = _RuijieIPSecGlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 2),
    _RuijieIPSecGlobalActiveSas_Type()
)
ruijieIPSecGlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalActiveSas.setStatus("current")
_RuijieIPSecGlobalInOctets_Type = Counter64
_RuijieIPSecGlobalInOctets_Object = MibScalar
ruijieIPSecGlobalInOctets = _RuijieIPSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 3),
    _RuijieIPSecGlobalInOctets_Type()
)
ruijieIPSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalInOctets.setStatus("current")
_RuijieIPSecGlobalInPkts_Type = Counter64
_RuijieIPSecGlobalInPkts_Object = MibScalar
ruijieIPSecGlobalInPkts = _RuijieIPSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 4),
    _RuijieIPSecGlobalInPkts_Type()
)
ruijieIPSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalInPkts.setStatus("current")
_RuijieIPSecGlobalInSpeed_Type = Counter64
_RuijieIPSecGlobalInSpeed_Object = MibScalar
ruijieIPSecGlobalInSpeed = _RuijieIPSecGlobalInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 5),
    _RuijieIPSecGlobalInSpeed_Type()
)
ruijieIPSecGlobalInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalInSpeed.setStatus("current")
_RuijieIPSecGlobalInDrops_Type = Counter64
_RuijieIPSecGlobalInDrops_Object = MibScalar
ruijieIPSecGlobalInDrops = _RuijieIPSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 6),
    _RuijieIPSecGlobalInDrops_Type()
)
ruijieIPSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalInDrops.setStatus("current")
_RuijieIPSecGlobalOutOctets_Type = Counter64
_RuijieIPSecGlobalOutOctets_Object = MibScalar
ruijieIPSecGlobalOutOctets = _RuijieIPSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 7),
    _RuijieIPSecGlobalOutOctets_Type()
)
ruijieIPSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalOutOctets.setStatus("current")
_RuijieIPSecGlobalOutPkts_Type = Counter64
_RuijieIPSecGlobalOutPkts_Object = MibScalar
ruijieIPSecGlobalOutPkts = _RuijieIPSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 8),
    _RuijieIPSecGlobalOutPkts_Type()
)
ruijieIPSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalOutPkts.setStatus("current")
_RuijieIPSecGlobalOutSpeed_Type = Counter64
_RuijieIPSecGlobalOutSpeed_Object = MibScalar
ruijieIPSecGlobalOutSpeed = _RuijieIPSecGlobalOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 9),
    _RuijieIPSecGlobalOutSpeed_Type()
)
ruijieIPSecGlobalOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalOutSpeed.setStatus("current")
_RuijieIPSecGlobalOutDrops_Type = Counter64
_RuijieIPSecGlobalOutDrops_Object = MibScalar
ruijieIPSecGlobalOutDrops = _RuijieIPSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 5, 10),
    _RuijieIPSecGlobalOutDrops_Type()
)
ruijieIPSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSecGlobalOutDrops.setStatus("current")
_RuijieIPSecTrapObject_ObjectIdentity = ObjectIdentity
ruijieIPSecTrapObject = _RuijieIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 6)
)
_RuijieIPSecMapName_Type = DisplayString
_RuijieIPSecMapName_Object = MibScalar
ruijieIPSecMapName = _RuijieIPSecMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 6, 1),
    _RuijieIPSecMapName_Type()
)
ruijieIPSecMapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPSecMapName.setStatus("current")
_RuijieIPSecSeqNum_Type = Integer32
_RuijieIPSecSeqNum_Object = MibScalar
ruijieIPSecSeqNum = _RuijieIPSecSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 6, 2),
    _RuijieIPSecSeqNum_Type()
)
ruijieIPSecSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPSecSeqNum.setStatus("current")
_RuijieIPSecSpiValue_Type = Integer32
_RuijieIPSecSpiValue_Object = MibScalar
ruijieIPSecSpiValue = _RuijieIPSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 6, 3),
    _RuijieIPSecSpiValue_Type()
)
ruijieIPSecSpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieIPSecSpiValue.setStatus("current")
_RuijieIPSecTrap_ObjectIdentity = ObjectIdentity
ruijieIPSecTrap = _RuijieIPSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 7)
)
_RuijieIPSecNotifications_ObjectIdentity = ObjectIdentity
ruijieIPSecNotifications = _RuijieIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 7, 1)
)
_RuijieIPSecConformance_ObjectIdentity = ObjectIdentity
ruijieIPSecConformance = _RuijieIPSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2)
)
_RuijieIPSecCompliances_ObjectIdentity = ObjectIdentity
ruijieIPSecCompliances = _RuijieIPSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 1)
)
_RuijieIPSecGroups_ObjectIdentity = ObjectIdentity
ruijieIPSecGroups = _RuijieIPSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2)
)

# Managed Objects groups

ruijieIPSecTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 1)
)
ruijieIPSecTunnelTableGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTunIKETunnelIndex"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLocalAddr"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLocalHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunKeyType"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunEncapMode"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInitiator"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLifeSize"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLifeTime"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemainTime"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunActiveTime"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemainSize"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunTotalRefreshes"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunCurrentSaInstances"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInSaEncryptAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInSaAhAuthAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInSaEspAuthAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunDiffHellmanGrp"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutSaEncryptAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutSaAhAuthAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutSaEspAuthAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunStatus"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelTableGroup.setStatus("current")

ruijieIPSecTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 2)
)
ruijieIPSecTunnelStatGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInOctets"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInDecompOctets"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInPkts"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInSpeed"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunInDropPkts"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutOctets"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutUncompOctets"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutPkts"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutSpeed"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunOutDropPkts"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelStatGroup.setStatus("current")

ruijieIPSecSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 3)
)
ruijieIPSecSaGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecSaDirection"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSaValue"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSaProtocol"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSaEncryptAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSaAuthAlgo"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSaStatus"))
)
if mibBuilder.loadTexts:
    ruijieIPSecSaGroup.setStatus("current")

ruijieIPSecTrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 4)
)
ruijieIPSecTrafficTableGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficLocalType"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficLocalAddr1"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficLocalAddr2"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficLocalProtocol"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficLocalPort"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficLocalHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficRemoteType"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficRemoteAddr1"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficRemoteAddr2"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficRemoteProtocol"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficRemotePort"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficRemoteHostname"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTrafficTableGroup.setStatus("current")

ruijieIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 5)
)
ruijieIPSecGlobalStatsGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalActiveTunnels"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalActiveSas"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalInOctets"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalInPkts"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalInDrops"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalInSpeed"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalOutOctets"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalOutPkts"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalOutDrops"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalOutSpeed"))
)
if mibBuilder.loadTexts:
    ruijieIPSecGlobalStatsGroup.setStatus("current")

ruijieIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 6)
)
ruijieIPSecTrapObjectGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecMapName"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSeqNum"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTrapObjectGroup.setStatus("current")


# Notification objects

ruijieIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 7, 1, 1)
)
ruijieIPSecTunnelStart.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLocalAddr"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLocalHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLifeTime"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelStart.setStatus(
        "current"
    )

ruijieIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 1, 7, 1, 2)
)
ruijieIPSecTunnelStop.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLocalAddr"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteAddr"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunLocalHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunRemoteHostname"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTunnelStop.setStatus(
        "current"
    )


# Notifications groups

ruijieIPSecTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 2, 7)
)
ruijieIPSecTrapGroup.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTunnelStart"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunnelStop"))
)
if mibBuilder.loadTexts:
    ruijieIPSecTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieIPSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 94, 2, 1, 1)
)
ruijieIPSecCompliance.setObjects(
      *(("RUIJIE-IPSEC-MIB", "ruijieIPSecTunnelTableGroup"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTunnelStatGroup"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecSaGroup"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrafficTableGroup"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecGlobalStatsGroup"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrapObjectGroup"),
        ("RUIJIE-IPSEC-MIB", "ruijieIPSecTrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieIPSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IPSEC-MIB",
    **{"RuijieDiffHellmanGrp": RuijieDiffHellmanGrp,
       "RuijieEncapMode": RuijieEncapMode,
       "RuijieEncryptAlgo": RuijieEncryptAlgo,
       "RuijieAuthAlgo": RuijieAuthAlgo,
       "RuijieSaProtocol": RuijieSaProtocol,
       "RuijieTunnelProtocol": RuijieTunnelProtocol,
       "RuijieTrafficType": RuijieTrafficType,
       "RuijieIPSecNegoType": RuijieIPSecNegoType,
       "RuijieIPSecTunnelState": RuijieIPSecTunnelState,
       "ruijieIPSecMonitor": ruijieIPSecMonitor,
       "ruijieIPSecObjects": ruijieIPSecObjects,
       "ruijieIPSecTunnelTable": ruijieIPSecTunnelTable,
       "ruijieIPSecTunnelEntry": ruijieIPSecTunnelEntry,
       "ruijieIPSecTunIfIndex": ruijieIPSecTunIfIndex,
       "ruijieIPSecTunIndex": ruijieIPSecTunIndex,
       "ruijieIPSecTunIKETunnelIndex": ruijieIPSecTunIKETunnelIndex,
       "ruijieIPSecTunLocalAddr": ruijieIPSecTunLocalAddr,
       "ruijieIPSecTunRemoteAddr": ruijieIPSecTunRemoteAddr,
       "ruijieIPSecTunLocalHostname": ruijieIPSecTunLocalHostname,
       "ruijieIPSecTunRemoteHostname": ruijieIPSecTunRemoteHostname,
       "ruijieIPSecTunKeyType": ruijieIPSecTunKeyType,
       "ruijieIPSecTunEncapMode": ruijieIPSecTunEncapMode,
       "ruijieIPSecTunInitiator": ruijieIPSecTunInitiator,
       "ruijieIPSecTunLifeSize": ruijieIPSecTunLifeSize,
       "ruijieIPSecTunLifeTime": ruijieIPSecTunLifeTime,
       "ruijieIPSecTunRemainTime": ruijieIPSecTunRemainTime,
       "ruijieIPSecTunActiveTime": ruijieIPSecTunActiveTime,
       "ruijieIPSecTunCreateTime": ruijieIPSecTunCreateTime,
       "ruijieIPSecTunRemainSize": ruijieIPSecTunRemainSize,
       "ruijieIPSecTunTotalRefreshes": ruijieIPSecTunTotalRefreshes,
       "ruijieIPSecTunCurrentSaInstances": ruijieIPSecTunCurrentSaInstances,
       "ruijieIPSecTunInSaEncryptAlgo": ruijieIPSecTunInSaEncryptAlgo,
       "ruijieIPSecTunInSaAhAuthAlgo": ruijieIPSecTunInSaAhAuthAlgo,
       "ruijieIPSecTunInSaEspAuthAlgo": ruijieIPSecTunInSaEspAuthAlgo,
       "ruijieIPSecTunDiffHellmanGrp": ruijieIPSecTunDiffHellmanGrp,
       "ruijieIPSecTunOutSaEncryptAlgo": ruijieIPSecTunOutSaEncryptAlgo,
       "ruijieIPSecTunOutSaAhAuthAlgo": ruijieIPSecTunOutSaAhAuthAlgo,
       "ruijieIPSecTunOutSaEspAuthAlgo": ruijieIPSecTunOutSaEspAuthAlgo,
       "ruijieIPSecTunMapName": ruijieIPSecTunMapName,
       "ruijieIPSecTunSeqNum": ruijieIPSecTunSeqNum,
       "ruijieIPSecTunStatus": ruijieIPSecTunStatus,
       "ruijieIPSecTunnelStatTable": ruijieIPSecTunnelStatTable,
       "ruijieIPSecTunnelStatEntry": ruijieIPSecTunnelStatEntry,
       "ruijieIPSecTunInOctets": ruijieIPSecTunInOctets,
       "ruijieIPSecTunInDecompOctets": ruijieIPSecTunInDecompOctets,
       "ruijieIPSecTunInPkts": ruijieIPSecTunInPkts,
       "ruijieIPSecTunInSpeed": ruijieIPSecTunInSpeed,
       "ruijieIPSecTunInDropPkts": ruijieIPSecTunInDropPkts,
       "ruijieIPSecTunOutOctets": ruijieIPSecTunOutOctets,
       "ruijieIPSecTunOutUncompOctets": ruijieIPSecTunOutUncompOctets,
       "ruijieIPSecTunOutPkts": ruijieIPSecTunOutPkts,
       "ruijieIPSecTunOutSpeed": ruijieIPSecTunOutSpeed,
       "ruijieIPSecTunOutDropPkts": ruijieIPSecTunOutDropPkts,
       "ruijieIPSecSaTable": ruijieIPSecSaTable,
       "ruijieIPSecSaEntry": ruijieIPSecSaEntry,
       "ruijieIPSecSaIndex": ruijieIPSecSaIndex,
       "ruijieIPSecSaDirection": ruijieIPSecSaDirection,
       "ruijieIPSecSaValue": ruijieIPSecSaValue,
       "ruijieIPSecSaProtocol": ruijieIPSecSaProtocol,
       "ruijieIPSecSaEncryptAlgo": ruijieIPSecSaEncryptAlgo,
       "ruijieIPSecSaAuthAlgo": ruijieIPSecSaAuthAlgo,
       "ruijieIPSecSaStatus": ruijieIPSecSaStatus,
       "ruijieIPSecTrafficTable": ruijieIPSecTrafficTable,
       "ruijieIPSecTrafficEntry": ruijieIPSecTrafficEntry,
       "ruijieIPSecTrafficLocalType": ruijieIPSecTrafficLocalType,
       "ruijieIPSecTrafficLocalAddr1": ruijieIPSecTrafficLocalAddr1,
       "ruijieIPSecTrafficLocalAddr2": ruijieIPSecTrafficLocalAddr2,
       "ruijieIPSecTrafficLocalProtocol": ruijieIPSecTrafficLocalProtocol,
       "ruijieIPSecTrafficLocalPort": ruijieIPSecTrafficLocalPort,
       "ruijieIPSecTrafficLocalHostname": ruijieIPSecTrafficLocalHostname,
       "ruijieIPSecTrafficRemoteType": ruijieIPSecTrafficRemoteType,
       "ruijieIPSecTrafficRemoteAddr1": ruijieIPSecTrafficRemoteAddr1,
       "ruijieIPSecTrafficRemoteAddr2": ruijieIPSecTrafficRemoteAddr2,
       "ruijieIPSecTrafficRemoteProtocol": ruijieIPSecTrafficRemoteProtocol,
       "ruijieIPSecTrafficRemotePort": ruijieIPSecTrafficRemotePort,
       "ruijieIPSecTrafficRemoteHostname": ruijieIPSecTrafficRemoteHostname,
       "ruijieIPSecGlobalStats": ruijieIPSecGlobalStats,
       "ruijieIPSecGlobalActiveTunnels": ruijieIPSecGlobalActiveTunnels,
       "ruijieIPSecGlobalActiveSas": ruijieIPSecGlobalActiveSas,
       "ruijieIPSecGlobalInOctets": ruijieIPSecGlobalInOctets,
       "ruijieIPSecGlobalInPkts": ruijieIPSecGlobalInPkts,
       "ruijieIPSecGlobalInSpeed": ruijieIPSecGlobalInSpeed,
       "ruijieIPSecGlobalInDrops": ruijieIPSecGlobalInDrops,
       "ruijieIPSecGlobalOutOctets": ruijieIPSecGlobalOutOctets,
       "ruijieIPSecGlobalOutPkts": ruijieIPSecGlobalOutPkts,
       "ruijieIPSecGlobalOutSpeed": ruijieIPSecGlobalOutSpeed,
       "ruijieIPSecGlobalOutDrops": ruijieIPSecGlobalOutDrops,
       "ruijieIPSecTrapObject": ruijieIPSecTrapObject,
       "ruijieIPSecMapName": ruijieIPSecMapName,
       "ruijieIPSecSeqNum": ruijieIPSecSeqNum,
       "ruijieIPSecSpiValue": ruijieIPSecSpiValue,
       "ruijieIPSecTrap": ruijieIPSecTrap,
       "ruijieIPSecNotifications": ruijieIPSecNotifications,
       "ruijieIPSecTunnelStart": ruijieIPSecTunnelStart,
       "ruijieIPSecTunnelStop": ruijieIPSecTunnelStop,
       "ruijieIPSecConformance": ruijieIPSecConformance,
       "ruijieIPSecCompliances": ruijieIPSecCompliances,
       "ruijieIPSecCompliance": ruijieIPSecCompliance,
       "ruijieIPSecGroups": ruijieIPSecGroups,
       "ruijieIPSecTunnelTableGroup": ruijieIPSecTunnelTableGroup,
       "ruijieIPSecTunnelStatGroup": ruijieIPSecTunnelStatGroup,
       "ruijieIPSecSaGroup": ruijieIPSecSaGroup,
       "ruijieIPSecTrafficTableGroup": ruijieIPSecTrafficTableGroup,
       "ruijieIPSecGlobalStatsGroup": ruijieIPSecGlobalStatsGroup,
       "ruijieIPSecTrapObjectGroup": ruijieIPSecTrapObjectGroup,
       "ruijieIPSecTrapGroup": ruijieIPSecTrapGroup}
)
