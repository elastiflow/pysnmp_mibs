# SNMP MIB module (A3COM-HUAWEI-IPSEC-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-IPSEC-MONITOR-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:06 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cIPSecMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cDiffHellmanGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("modp768", 1),
          ("modp1024", 2),
          ("modp1536", 5),
          ("modp2048", 14),
          ("invalidGroup", 2147483647))
    )



class H3cEncapMode(TextualConvention, Integer32):
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



class H3cEncryptAlgo(TextualConvention, Integer32):
    status = "current"
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
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("blowfishCbc", 3),
          ("rc5R16B64Cbc", 4),
          ("tripledesCbc", 5),
          ("castCbc", 6),
          ("aesCbc", 7),
          ("nsaCbc", 8),
          ("aesCbc128", 9),
          ("aesCbc192", 10),
          ("aesCbc256", 11),
          ("invalidAlg", 2147483647))
    )



class H3cAuthAlgo(TextualConvention, Integer32):
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



class H3cSaProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("isakmp", 1),
          ("ah", 2),
          ("esp", 3),
          ("ipcomp", 4))
    )



class H3cTrapStatus(TextualConvention, Integer32):
    status = "current"
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



class H3cIPSecIDType(TextualConvention, Integer32):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("ipv4Addr", 1),
          ("fqdn", 2),
          ("userFqdn", 3),
          ("ipv4AddrSubnet", 4),
          ("ipv6Addr", 5),
          ("ipv6AddrSubnet", 6),
          ("ipv4AddrRange", 7),
          ("ipv6AddrRange", 8),
          ("derAsn1Dn", 9),
          ("derAsn1Gn", 10),
          ("keyId", 11))
    )



class H3cTrafficType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv4AddrSubnet", 4),
          ("ipv6Addr", 5),
          ("ipv6AddrSubnet", 6),
          ("ipv4AddrRange", 7),
          ("ipv6AddrRange", 8))
    )



class H3cIPSecNegoType(TextualConvention, Integer32):
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



class H3cIPSecTunnelState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("timeout", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cIPSecObjects_ObjectIdentity = ObjectIdentity
h3cIPSecObjects = _H3cIPSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1)
)
_H3cIPSecTunnelTable_Object = MibTable
h3cIPSecTunnelTable = _H3cIPSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelTable.setStatus("current")
_H3cIPSecTunnelEntry_Object = MibTableRow
h3cIPSecTunnelEntry = _H3cIPSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1)
)
h3cIPSecTunnelEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIfIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunEntryIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelEntry.setStatus("current")


class _H3cIPSecTunIfIndex_Type(Integer32):
    """Custom type h3cIPSecTunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecTunIfIndex_Type.__name__ = "Integer32"
_H3cIPSecTunIfIndex_Object = MibTableColumn
h3cIPSecTunIfIndex = _H3cIPSecTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 1),
    _H3cIPSecTunIfIndex_Type()
)
h3cIPSecTunIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIPSecTunIfIndex.setStatus("current")


class _H3cIPSecTunEntryIndex_Type(Integer32):
    """Custom type h3cIPSecTunEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecTunEntryIndex_Type.__name__ = "Integer32"
_H3cIPSecTunEntryIndex_Object = MibTableColumn
h3cIPSecTunEntryIndex = _H3cIPSecTunEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 2),
    _H3cIPSecTunEntryIndex_Type()
)
h3cIPSecTunEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIPSecTunEntryIndex.setStatus("current")


class _H3cIPSecTunIndex_Type(Integer32):
    """Custom type h3cIPSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecTunIndex_Type.__name__ = "Integer32"
_H3cIPSecTunIndex_Object = MibTableColumn
h3cIPSecTunIndex = _H3cIPSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 3),
    _H3cIPSecTunIndex_Type()
)
h3cIPSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIPSecTunIndex.setStatus("current")


class _H3cIPSecTunIKETunnelIndex_Type(Integer32):
    """Custom type h3cIPSecTunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecTunIKETunnelIndex_Type.__name__ = "Integer32"
_H3cIPSecTunIKETunnelIndex_Object = MibTableColumn
h3cIPSecTunIKETunnelIndex = _H3cIPSecTunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 4),
    _H3cIPSecTunIKETunnelIndex_Type()
)
h3cIPSecTunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunIKETunnelIndex.setStatus("current")
_H3cIPSecTunLocalAddr_Type = IpAddress
_H3cIPSecTunLocalAddr_Object = MibTableColumn
h3cIPSecTunLocalAddr = _H3cIPSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 5),
    _H3cIPSecTunLocalAddr_Type()
)
h3cIPSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunLocalAddr.setStatus("current")
_H3cIPSecTunRemoteAddr_Type = IpAddress
_H3cIPSecTunRemoteAddr_Object = MibTableColumn
h3cIPSecTunRemoteAddr = _H3cIPSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 6),
    _H3cIPSecTunRemoteAddr_Type()
)
h3cIPSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunRemoteAddr.setStatus("current")
_H3cIPSecTunKeyType_Type = H3cIPSecNegoType
_H3cIPSecTunKeyType_Object = MibTableColumn
h3cIPSecTunKeyType = _H3cIPSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 7),
    _H3cIPSecTunKeyType_Type()
)
h3cIPSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunKeyType.setStatus("current")
_H3cIPSecTunEncapMode_Type = H3cEncapMode
_H3cIPSecTunEncapMode_Object = MibTableColumn
h3cIPSecTunEncapMode = _H3cIPSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 8),
    _H3cIPSecTunEncapMode_Type()
)
h3cIPSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunEncapMode.setStatus("current")


class _H3cIPSecTunInitiator_Type(Integer32):
    """Custom type h3cIPSecTunInitiator based on Integer32"""
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


_H3cIPSecTunInitiator_Type.__name__ = "Integer32"
_H3cIPSecTunInitiator_Object = MibTableColumn
h3cIPSecTunInitiator = _H3cIPSecTunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 9),
    _H3cIPSecTunInitiator_Type()
)
h3cIPSecTunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInitiator.setStatus("current")
_H3cIPSecTunLifeSize_Type = Gauge32
_H3cIPSecTunLifeSize_Object = MibTableColumn
h3cIPSecTunLifeSize = _H3cIPSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 10),
    _H3cIPSecTunLifeSize_Type()
)
h3cIPSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunLifeSize.setStatus("current")


class _H3cIPSecTunLifeTime_Type(Integer32):
    """Custom type h3cIPSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecTunLifeTime_Type.__name__ = "Integer32"
_H3cIPSecTunLifeTime_Object = MibTableColumn
h3cIPSecTunLifeTime = _H3cIPSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 11),
    _H3cIPSecTunLifeTime_Type()
)
h3cIPSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunLifeTime.setStatus("current")


class _H3cIPSecTunRemainTime_Type(Integer32):
    """Custom type h3cIPSecTunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cIPSecTunRemainTime_Type.__name__ = "Integer32"
_H3cIPSecTunRemainTime_Object = MibTableColumn
h3cIPSecTunRemainTime = _H3cIPSecTunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 12),
    _H3cIPSecTunRemainTime_Type()
)
h3cIPSecTunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunRemainTime.setStatus("current")


class _H3cIPSecTunActiveTime_Type(Integer32):
    """Custom type h3cIPSecTunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cIPSecTunActiveTime_Type.__name__ = "Integer32"
_H3cIPSecTunActiveTime_Object = MibTableColumn
h3cIPSecTunActiveTime = _H3cIPSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 13),
    _H3cIPSecTunActiveTime_Type()
)
h3cIPSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunActiveTime.setStatus("current")
_H3cIPSecTunRemainSize_Type = Gauge32
_H3cIPSecTunRemainSize_Object = MibTableColumn
h3cIPSecTunRemainSize = _H3cIPSecTunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 14),
    _H3cIPSecTunRemainSize_Type()
)
h3cIPSecTunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunRemainSize.setStatus("current")
_H3cIPSecTunTotalRefreshes_Type = Counter32
_H3cIPSecTunTotalRefreshes_Object = MibTableColumn
h3cIPSecTunTotalRefreshes = _H3cIPSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 15),
    _H3cIPSecTunTotalRefreshes_Type()
)
h3cIPSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunTotalRefreshes.setStatus("current")
_H3cIPSecTunCurrentSaInstances_Type = Gauge32
_H3cIPSecTunCurrentSaInstances_Object = MibTableColumn
h3cIPSecTunCurrentSaInstances = _H3cIPSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 16),
    _H3cIPSecTunCurrentSaInstances_Type()
)
h3cIPSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunCurrentSaInstances.setStatus("current")
_H3cIPSecTunInSaEncryptAlgo_Type = H3cEncryptAlgo
_H3cIPSecTunInSaEncryptAlgo_Object = MibTableColumn
h3cIPSecTunInSaEncryptAlgo = _H3cIPSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 17),
    _H3cIPSecTunInSaEncryptAlgo_Type()
)
h3cIPSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInSaEncryptAlgo.setStatus("current")
_H3cIPSecTunInSaAhAuthAlgo_Type = H3cAuthAlgo
_H3cIPSecTunInSaAhAuthAlgo_Object = MibTableColumn
h3cIPSecTunInSaAhAuthAlgo = _H3cIPSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 18),
    _H3cIPSecTunInSaAhAuthAlgo_Type()
)
h3cIPSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInSaAhAuthAlgo.setStatus("current")
_H3cIPSecTunInSaEspAuthAlgo_Type = H3cAuthAlgo
_H3cIPSecTunInSaEspAuthAlgo_Object = MibTableColumn
h3cIPSecTunInSaEspAuthAlgo = _H3cIPSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 19),
    _H3cIPSecTunInSaEspAuthAlgo_Type()
)
h3cIPSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInSaEspAuthAlgo.setStatus("current")
_H3cIPSecTunDiffHellmanGrp_Type = H3cDiffHellmanGrp
_H3cIPSecTunDiffHellmanGrp_Object = MibTableColumn
h3cIPSecTunDiffHellmanGrp = _H3cIPSecTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 20),
    _H3cIPSecTunDiffHellmanGrp_Type()
)
h3cIPSecTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunDiffHellmanGrp.setStatus("current")
_H3cIPSecTunOutSaEncryptAlgo_Type = H3cEncryptAlgo
_H3cIPSecTunOutSaEncryptAlgo_Object = MibTableColumn
h3cIPSecTunOutSaEncryptAlgo = _H3cIPSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 21),
    _H3cIPSecTunOutSaEncryptAlgo_Type()
)
h3cIPSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutSaEncryptAlgo.setStatus("current")
_H3cIPSecTunOutSaAhAuthAlgo_Type = H3cAuthAlgo
_H3cIPSecTunOutSaAhAuthAlgo_Object = MibTableColumn
h3cIPSecTunOutSaAhAuthAlgo = _H3cIPSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 22),
    _H3cIPSecTunOutSaAhAuthAlgo_Type()
)
h3cIPSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutSaAhAuthAlgo.setStatus("current")
_H3cIPSecTunOutSaEspAuthAlgo_Type = H3cAuthAlgo
_H3cIPSecTunOutSaEspAuthAlgo_Object = MibTableColumn
h3cIPSecTunOutSaEspAuthAlgo = _H3cIPSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 23),
    _H3cIPSecTunOutSaEspAuthAlgo_Type()
)
h3cIPSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutSaEspAuthAlgo.setStatus("current")
_H3cIPSecTunPolicyName_Type = DisplayString
_H3cIPSecTunPolicyName_Object = MibTableColumn
h3cIPSecTunPolicyName = _H3cIPSecTunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 24),
    _H3cIPSecTunPolicyName_Type()
)
h3cIPSecTunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunPolicyName.setStatus("current")


class _H3cIPSecTunPolicyNum_Type(Integer32):
    """Custom type h3cIPSecTunPolicyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecTunPolicyNum_Type.__name__ = "Integer32"
_H3cIPSecTunPolicyNum_Object = MibTableColumn
h3cIPSecTunPolicyNum = _H3cIPSecTunPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 25),
    _H3cIPSecTunPolicyNum_Type()
)
h3cIPSecTunPolicyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunPolicyNum.setStatus("current")


class _H3cIPSecTunStatus_Type(Integer32):
    """Custom type h3cIPSecTunStatus based on Integer32"""
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
        *(("initial", 1),
          ("ready", 2),
          ("rekeyed", 3),
          ("closed", 4))
    )


_H3cIPSecTunStatus_Type.__name__ = "Integer32"
_H3cIPSecTunStatus_Object = MibTableColumn
h3cIPSecTunStatus = _H3cIPSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 1, 1, 26),
    _H3cIPSecTunStatus_Type()
)
h3cIPSecTunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunStatus.setStatus("current")
_H3cIPSecTunnelStatTable_Object = MibTable
h3cIPSecTunnelStatTable = _H3cIPSecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelStatTable.setStatus("current")
_H3cIPSecTunnelStatEntry_Object = MibTableRow
h3cIPSecTunnelStatEntry = _H3cIPSecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1)
)
h3cIPSecTunnelStatEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIfIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunEntryIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelStatEntry.setStatus("current")
_H3cIPSecTunInOctets_Type = Counter64
_H3cIPSecTunInOctets_Object = MibTableColumn
h3cIPSecTunInOctets = _H3cIPSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 1),
    _H3cIPSecTunInOctets_Type()
)
h3cIPSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInOctets.setStatus("current")
_H3cIPSecTunInDecompOctets_Type = Counter64
_H3cIPSecTunInDecompOctets_Object = MibTableColumn
h3cIPSecTunInDecompOctets = _H3cIPSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 2),
    _H3cIPSecTunInDecompOctets_Type()
)
h3cIPSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInDecompOctets.setStatus("current")
_H3cIPSecTunInPkts_Type = Counter64
_H3cIPSecTunInPkts_Object = MibTableColumn
h3cIPSecTunInPkts = _H3cIPSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 3),
    _H3cIPSecTunInPkts_Type()
)
h3cIPSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInPkts.setStatus("current")
_H3cIPSecTunInDropPkts_Type = Counter64
_H3cIPSecTunInDropPkts_Object = MibTableColumn
h3cIPSecTunInDropPkts = _H3cIPSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 4),
    _H3cIPSecTunInDropPkts_Type()
)
h3cIPSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInDropPkts.setStatus("current")
_H3cIPSecTunInReplayDropPkts_Type = Counter32
_H3cIPSecTunInReplayDropPkts_Object = MibTableColumn
h3cIPSecTunInReplayDropPkts = _H3cIPSecTunInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 5),
    _H3cIPSecTunInReplayDropPkts_Type()
)
h3cIPSecTunInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInReplayDropPkts.setStatus("current")
_H3cIPSecTunInAuthFails_Type = Counter32
_H3cIPSecTunInAuthFails_Object = MibTableColumn
h3cIPSecTunInAuthFails = _H3cIPSecTunInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 6),
    _H3cIPSecTunInAuthFails_Type()
)
h3cIPSecTunInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInAuthFails.setStatus("current")
_H3cIPSecTunInDecryptFails_Type = Counter32
_H3cIPSecTunInDecryptFails_Object = MibTableColumn
h3cIPSecTunInDecryptFails = _H3cIPSecTunInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 7),
    _H3cIPSecTunInDecryptFails_Type()
)
h3cIPSecTunInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInDecryptFails.setStatus("current")
_H3cIPSecTunOutOctets_Type = Counter64
_H3cIPSecTunOutOctets_Object = MibTableColumn
h3cIPSecTunOutOctets = _H3cIPSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 8),
    _H3cIPSecTunOutOctets_Type()
)
h3cIPSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutOctets.setStatus("current")
_H3cIPSecTunOutUncompOctets_Type = Counter64
_H3cIPSecTunOutUncompOctets_Object = MibTableColumn
h3cIPSecTunOutUncompOctets = _H3cIPSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 9),
    _H3cIPSecTunOutUncompOctets_Type()
)
h3cIPSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutUncompOctets.setStatus("current")
_H3cIPSecTunOutPkts_Type = Counter64
_H3cIPSecTunOutPkts_Object = MibTableColumn
h3cIPSecTunOutPkts = _H3cIPSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 10),
    _H3cIPSecTunOutPkts_Type()
)
h3cIPSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutPkts.setStatus("current")
_H3cIPSecTunOutDropPkts_Type = Counter64
_H3cIPSecTunOutDropPkts_Object = MibTableColumn
h3cIPSecTunOutDropPkts = _H3cIPSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 11),
    _H3cIPSecTunOutDropPkts_Type()
)
h3cIPSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutDropPkts.setStatus("current")
_H3cIPSecTunOutEncryptFails_Type = Counter32
_H3cIPSecTunOutEncryptFails_Object = MibTableColumn
h3cIPSecTunOutEncryptFails = _H3cIPSecTunOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 12),
    _H3cIPSecTunOutEncryptFails_Type()
)
h3cIPSecTunOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunOutEncryptFails.setStatus("current")
_H3cIPSecTunNoMemoryDropPkts_Type = Counter32
_H3cIPSecTunNoMemoryDropPkts_Object = MibTableColumn
h3cIPSecTunNoMemoryDropPkts = _H3cIPSecTunNoMemoryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 13),
    _H3cIPSecTunNoMemoryDropPkts_Type()
)
h3cIPSecTunNoMemoryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunNoMemoryDropPkts.setStatus("current")
_H3cIPSecTunQueueFullDropPkts_Type = Counter32
_H3cIPSecTunQueueFullDropPkts_Object = MibTableColumn
h3cIPSecTunQueueFullDropPkts = _H3cIPSecTunQueueFullDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 14),
    _H3cIPSecTunQueueFullDropPkts_Type()
)
h3cIPSecTunQueueFullDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunQueueFullDropPkts.setStatus("current")
_H3cIPSecTunInvalidLenDropPkts_Type = Counter32
_H3cIPSecTunInvalidLenDropPkts_Object = MibTableColumn
h3cIPSecTunInvalidLenDropPkts = _H3cIPSecTunInvalidLenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 15),
    _H3cIPSecTunInvalidLenDropPkts_Type()
)
h3cIPSecTunInvalidLenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInvalidLenDropPkts.setStatus("current")
_H3cIPSecTunTooLongDropPkts_Type = Counter32
_H3cIPSecTunTooLongDropPkts_Object = MibTableColumn
h3cIPSecTunTooLongDropPkts = _H3cIPSecTunTooLongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 16),
    _H3cIPSecTunTooLongDropPkts_Type()
)
h3cIPSecTunTooLongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunTooLongDropPkts.setStatus("current")
_H3cIPSecTunInvalidSaDropPkts_Type = Counter32
_H3cIPSecTunInvalidSaDropPkts_Object = MibTableColumn
h3cIPSecTunInvalidSaDropPkts = _H3cIPSecTunInvalidSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 2, 1, 17),
    _H3cIPSecTunInvalidSaDropPkts_Type()
)
h3cIPSecTunInvalidSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTunInvalidSaDropPkts.setStatus("current")
_H3cIPSecSaTable_Object = MibTable
h3cIPSecSaTable = _H3cIPSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIPSecSaTable.setStatus("current")
_H3cIPSecSaEntry_Object = MibTableRow
h3cIPSecSaEntry = _H3cIPSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1)
)
h3cIPSecSaEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIfIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunEntryIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaIndex"),
)
if mibBuilder.loadTexts:
    h3cIPSecSaEntry.setStatus("current")


class _H3cIPSecSaIndex_Type(Integer32):
    """Custom type h3cIPSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIPSecSaIndex_Type.__name__ = "Integer32"
_H3cIPSecSaIndex_Object = MibTableColumn
h3cIPSecSaIndex = _H3cIPSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 1),
    _H3cIPSecSaIndex_Type()
)
h3cIPSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIPSecSaIndex.setStatus("current")


class _H3cIPSecSaDirection_Type(Integer32):
    """Custom type h3cIPSecSaDirection based on Integer32"""
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


_H3cIPSecSaDirection_Type.__name__ = "Integer32"
_H3cIPSecSaDirection_Object = MibTableColumn
h3cIPSecSaDirection = _H3cIPSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 2),
    _H3cIPSecSaDirection_Type()
)
h3cIPSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecSaDirection.setStatus("current")


class _H3cIPSecSaValue_Type(Unsigned32):
    """Custom type h3cIPSecSaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cIPSecSaValue_Type.__name__ = "Unsigned32"
_H3cIPSecSaValue_Object = MibTableColumn
h3cIPSecSaValue = _H3cIPSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 3),
    _H3cIPSecSaValue_Type()
)
h3cIPSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecSaValue.setStatus("current")
_H3cIPSecSaProtocol_Type = H3cSaProtocol
_H3cIPSecSaProtocol_Object = MibTableColumn
h3cIPSecSaProtocol = _H3cIPSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 4),
    _H3cIPSecSaProtocol_Type()
)
h3cIPSecSaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecSaProtocol.setStatus("current")
_H3cIPSecSaEncryptAlgo_Type = H3cEncryptAlgo
_H3cIPSecSaEncryptAlgo_Object = MibTableColumn
h3cIPSecSaEncryptAlgo = _H3cIPSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 5),
    _H3cIPSecSaEncryptAlgo_Type()
)
h3cIPSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecSaEncryptAlgo.setStatus("current")
_H3cIPSecSaAuthAlgo_Type = H3cAuthAlgo
_H3cIPSecSaAuthAlgo_Object = MibTableColumn
h3cIPSecSaAuthAlgo = _H3cIPSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 6),
    _H3cIPSecSaAuthAlgo_Type()
)
h3cIPSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecSaAuthAlgo.setStatus("current")


class _H3cIPSecSaStatus_Type(Integer32):
    """Custom type h3cIPSecSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expiring", 2))
    )


_H3cIPSecSaStatus_Type.__name__ = "Integer32"
_H3cIPSecSaStatus_Object = MibTableColumn
h3cIPSecSaStatus = _H3cIPSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 3, 1, 7),
    _H3cIPSecSaStatus_Type()
)
h3cIPSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecSaStatus.setStatus("current")
_H3cIPSecTrafficTable_Object = MibTable
h3cIPSecTrafficTable = _H3cIPSecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    h3cIPSecTrafficTable.setStatus("current")
_H3cIPSecTrafficEntry_Object = MibTableRow
h3cIPSecTrafficEntry = _H3cIPSecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1)
)
h3cIPSecTrafficEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIfIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunEntryIndex"),
    (0, "A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIndex"),
)
if mibBuilder.loadTexts:
    h3cIPSecTrafficEntry.setStatus("current")
_H3cIPSecTrafficLocalType_Type = H3cTrafficType
_H3cIPSecTrafficLocalType_Object = MibTableColumn
h3cIPSecTrafficLocalType = _H3cIPSecTrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 1),
    _H3cIPSecTrafficLocalType_Type()
)
h3cIPSecTrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficLocalType.setStatus("current")
_H3cIPSecTrafficLocalAddr1_Type = IpAddress
_H3cIPSecTrafficLocalAddr1_Object = MibTableColumn
h3cIPSecTrafficLocalAddr1 = _H3cIPSecTrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 2),
    _H3cIPSecTrafficLocalAddr1_Type()
)
h3cIPSecTrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficLocalAddr1.setStatus("current")
_H3cIPSecTrafficLocalAddr2_Type = IpAddress
_H3cIPSecTrafficLocalAddr2_Object = MibTableColumn
h3cIPSecTrafficLocalAddr2 = _H3cIPSecTrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 3),
    _H3cIPSecTrafficLocalAddr2_Type()
)
h3cIPSecTrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficLocalAddr2.setStatus("current")


class _H3cIPSecTrafficLocalProtocol_Type(Integer32):
    """Custom type h3cIPSecTrafficLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIPSecTrafficLocalProtocol_Type.__name__ = "Integer32"
_H3cIPSecTrafficLocalProtocol_Object = MibTableColumn
h3cIPSecTrafficLocalProtocol = _H3cIPSecTrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 4),
    _H3cIPSecTrafficLocalProtocol_Type()
)
h3cIPSecTrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficLocalProtocol.setStatus("current")


class _H3cIPSecTrafficLocalPort_Type(Integer32):
    """Custom type h3cIPSecTrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cIPSecTrafficLocalPort_Type.__name__ = "Integer32"
_H3cIPSecTrafficLocalPort_Object = MibTableColumn
h3cIPSecTrafficLocalPort = _H3cIPSecTrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 5),
    _H3cIPSecTrafficLocalPort_Type()
)
h3cIPSecTrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficLocalPort.setStatus("current")
_H3cIPSecTrafficRemoteType_Type = H3cTrafficType
_H3cIPSecTrafficRemoteType_Object = MibTableColumn
h3cIPSecTrafficRemoteType = _H3cIPSecTrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 6),
    _H3cIPSecTrafficRemoteType_Type()
)
h3cIPSecTrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficRemoteType.setStatus("current")
_H3cIPSecTrafficRemoteAddr1_Type = IpAddress
_H3cIPSecTrafficRemoteAddr1_Object = MibTableColumn
h3cIPSecTrafficRemoteAddr1 = _H3cIPSecTrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 7),
    _H3cIPSecTrafficRemoteAddr1_Type()
)
h3cIPSecTrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficRemoteAddr1.setStatus("current")
_H3cIPSecTrafficRemoteAddr2_Type = IpAddress
_H3cIPSecTrafficRemoteAddr2_Object = MibTableColumn
h3cIPSecTrafficRemoteAddr2 = _H3cIPSecTrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 8),
    _H3cIPSecTrafficRemoteAddr2_Type()
)
h3cIPSecTrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficRemoteAddr2.setStatus("current")


class _H3cIPSecTrafficRemoteProtocol_Type(Integer32):
    """Custom type h3cIPSecTrafficRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIPSecTrafficRemoteProtocol_Type.__name__ = "Integer32"
_H3cIPSecTrafficRemoteProtocol_Object = MibTableColumn
h3cIPSecTrafficRemoteProtocol = _H3cIPSecTrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 9),
    _H3cIPSecTrafficRemoteProtocol_Type()
)
h3cIPSecTrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficRemoteProtocol.setStatus("current")


class _H3cIPSecTrafficRemotePort_Type(Integer32):
    """Custom type h3cIPSecTrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cIPSecTrafficRemotePort_Type.__name__ = "Integer32"
_H3cIPSecTrafficRemotePort_Object = MibTableColumn
h3cIPSecTrafficRemotePort = _H3cIPSecTrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 4, 1, 10),
    _H3cIPSecTrafficRemotePort_Type()
)
h3cIPSecTrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecTrafficRemotePort.setStatus("current")
_H3cIPSecGlobalStats_ObjectIdentity = ObjectIdentity
h3cIPSecGlobalStats = _H3cIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5)
)
_H3cIPSecGlobalActiveTunnels_Type = Gauge32
_H3cIPSecGlobalActiveTunnels_Object = MibScalar
h3cIPSecGlobalActiveTunnels = _H3cIPSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 1),
    _H3cIPSecGlobalActiveTunnels_Type()
)
h3cIPSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalActiveTunnels.setStatus("current")
_H3cIPSecGlobalActiveSas_Type = Gauge32
_H3cIPSecGlobalActiveSas_Object = MibScalar
h3cIPSecGlobalActiveSas = _H3cIPSecGlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 2),
    _H3cIPSecGlobalActiveSas_Type()
)
h3cIPSecGlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalActiveSas.setStatus("current")
_H3cIPSecGlobalInOctets_Type = Counter64
_H3cIPSecGlobalInOctets_Object = MibScalar
h3cIPSecGlobalInOctets = _H3cIPSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 3),
    _H3cIPSecGlobalInOctets_Type()
)
h3cIPSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInOctets.setStatus("current")
_H3cIPSecGlobalInDecompOctets_Type = Counter64
_H3cIPSecGlobalInDecompOctets_Object = MibScalar
h3cIPSecGlobalInDecompOctets = _H3cIPSecGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 4),
    _H3cIPSecGlobalInDecompOctets_Type()
)
h3cIPSecGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInDecompOctets.setStatus("current")
_H3cIPSecGlobalInPkts_Type = Counter64
_H3cIPSecGlobalInPkts_Object = MibScalar
h3cIPSecGlobalInPkts = _H3cIPSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 5),
    _H3cIPSecGlobalInPkts_Type()
)
h3cIPSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInPkts.setStatus("current")
_H3cIPSecGlobalInDrops_Type = Counter64
_H3cIPSecGlobalInDrops_Object = MibScalar
h3cIPSecGlobalInDrops = _H3cIPSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 6),
    _H3cIPSecGlobalInDrops_Type()
)
h3cIPSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInDrops.setStatus("current")
_H3cIPSecGlobalInReplayDrops_Type = Counter32
_H3cIPSecGlobalInReplayDrops_Object = MibScalar
h3cIPSecGlobalInReplayDrops = _H3cIPSecGlobalInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 7),
    _H3cIPSecGlobalInReplayDrops_Type()
)
h3cIPSecGlobalInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInReplayDrops.setStatus("current")
_H3cIPSecGlobalInAuthFails_Type = Counter32
_H3cIPSecGlobalInAuthFails_Object = MibScalar
h3cIPSecGlobalInAuthFails = _H3cIPSecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 8),
    _H3cIPSecGlobalInAuthFails_Type()
)
h3cIPSecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInAuthFails.setStatus("current")
_H3cIPSecGlobalInDecryptFails_Type = Counter32
_H3cIPSecGlobalInDecryptFails_Object = MibScalar
h3cIPSecGlobalInDecryptFails = _H3cIPSecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 9),
    _H3cIPSecGlobalInDecryptFails_Type()
)
h3cIPSecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInDecryptFails.setStatus("current")
_H3cIPSecGlobalOutOctets_Type = Counter64
_H3cIPSecGlobalOutOctets_Object = MibScalar
h3cIPSecGlobalOutOctets = _H3cIPSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 10),
    _H3cIPSecGlobalOutOctets_Type()
)
h3cIPSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalOutOctets.setStatus("current")
_H3cIPSecGlobalOutUncompOctets_Type = Counter64
_H3cIPSecGlobalOutUncompOctets_Object = MibScalar
h3cIPSecGlobalOutUncompOctets = _H3cIPSecGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 11),
    _H3cIPSecGlobalOutUncompOctets_Type()
)
h3cIPSecGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalOutUncompOctets.setStatus("current")
_H3cIPSecGlobalOutPkts_Type = Counter64
_H3cIPSecGlobalOutPkts_Object = MibScalar
h3cIPSecGlobalOutPkts = _H3cIPSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 12),
    _H3cIPSecGlobalOutPkts_Type()
)
h3cIPSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalOutPkts.setStatus("current")
_H3cIPSecGlobalOutDrops_Type = Counter64
_H3cIPSecGlobalOutDrops_Object = MibScalar
h3cIPSecGlobalOutDrops = _H3cIPSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 13),
    _H3cIPSecGlobalOutDrops_Type()
)
h3cIPSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalOutDrops.setStatus("current")
_H3cIPSecGlobalOutEncryptFails_Type = Counter32
_H3cIPSecGlobalOutEncryptFails_Object = MibScalar
h3cIPSecGlobalOutEncryptFails = _H3cIPSecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 14),
    _H3cIPSecGlobalOutEncryptFails_Type()
)
h3cIPSecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalOutEncryptFails.setStatus("current")
_H3cIPSecGlobalNoMemoryDropPkts_Type = Counter32
_H3cIPSecGlobalNoMemoryDropPkts_Object = MibScalar
h3cIPSecGlobalNoMemoryDropPkts = _H3cIPSecGlobalNoMemoryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 15),
    _H3cIPSecGlobalNoMemoryDropPkts_Type()
)
h3cIPSecGlobalNoMemoryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalNoMemoryDropPkts.setStatus("current")
_H3cIPSecGlobalNoFindSaDropPkts_Type = Counter32
_H3cIPSecGlobalNoFindSaDropPkts_Object = MibScalar
h3cIPSecGlobalNoFindSaDropPkts = _H3cIPSecGlobalNoFindSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 16),
    _H3cIPSecGlobalNoFindSaDropPkts_Type()
)
h3cIPSecGlobalNoFindSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalNoFindSaDropPkts.setStatus("current")
_H3cIPSecGlobalQueueFullDropPkts_Type = Counter32
_H3cIPSecGlobalQueueFullDropPkts_Object = MibScalar
h3cIPSecGlobalQueueFullDropPkts = _H3cIPSecGlobalQueueFullDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 17),
    _H3cIPSecGlobalQueueFullDropPkts_Type()
)
h3cIPSecGlobalQueueFullDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalQueueFullDropPkts.setStatus("current")
_H3cIPSecGlobalInvalidLenDropPkts_Type = Counter32
_H3cIPSecGlobalInvalidLenDropPkts_Object = MibScalar
h3cIPSecGlobalInvalidLenDropPkts = _H3cIPSecGlobalInvalidLenDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 18),
    _H3cIPSecGlobalInvalidLenDropPkts_Type()
)
h3cIPSecGlobalInvalidLenDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInvalidLenDropPkts.setStatus("current")
_H3cIPSecGlobalTooLongDropPkts_Type = Counter32
_H3cIPSecGlobalTooLongDropPkts_Object = MibScalar
h3cIPSecGlobalTooLongDropPkts = _H3cIPSecGlobalTooLongDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 19),
    _H3cIPSecGlobalTooLongDropPkts_Type()
)
h3cIPSecGlobalTooLongDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalTooLongDropPkts.setStatus("current")
_H3cIPSecGlobalInvalidSaDropPkts_Type = Counter32
_H3cIPSecGlobalInvalidSaDropPkts_Object = MibScalar
h3cIPSecGlobalInvalidSaDropPkts = _H3cIPSecGlobalInvalidSaDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 5, 20),
    _H3cIPSecGlobalInvalidSaDropPkts_Type()
)
h3cIPSecGlobalInvalidSaDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIPSecGlobalInvalidSaDropPkts.setStatus("current")
_H3cIPSecTrapObject_ObjectIdentity = ObjectIdentity
h3cIPSecTrapObject = _H3cIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 6)
)
_H3cIPSecPolicyName_Type = DisplayString
_H3cIPSecPolicyName_Object = MibScalar
h3cIPSecPolicyName = _H3cIPSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 6, 1),
    _H3cIPSecPolicyName_Type()
)
h3cIPSecPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPSecPolicyName.setStatus("current")
_H3cIPSecPolicySeqNum_Type = Integer32
_H3cIPSecPolicySeqNum_Object = MibScalar
h3cIPSecPolicySeqNum = _H3cIPSecPolicySeqNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 6, 2),
    _H3cIPSecPolicySeqNum_Type()
)
h3cIPSecPolicySeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPSecPolicySeqNum.setStatus("current")
_H3cIPSecPolicySize_Type = Integer32
_H3cIPSecPolicySize_Object = MibScalar
h3cIPSecPolicySize = _H3cIPSecPolicySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 6, 3),
    _H3cIPSecPolicySize_Type()
)
h3cIPSecPolicySize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPSecPolicySize.setStatus("current")
_H3cIPSecSpiValue_Type = Integer32
_H3cIPSecSpiValue_Object = MibScalar
h3cIPSecSpiValue = _H3cIPSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 6, 4),
    _H3cIPSecSpiValue_Type()
)
h3cIPSecSpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIPSecSpiValue.setStatus("current")
_H3cIPSecTrapCntl_ObjectIdentity = ObjectIdentity
h3cIPSecTrapCntl = _H3cIPSecTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7)
)
_H3cIPSecTrapGlobalCntl_Type = H3cTrapStatus
_H3cIPSecTrapGlobalCntl_Object = MibScalar
h3cIPSecTrapGlobalCntl = _H3cIPSecTrapGlobalCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 1),
    _H3cIPSecTrapGlobalCntl_Type()
)
h3cIPSecTrapGlobalCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecTrapGlobalCntl.setStatus("current")
_H3cIPSecTunnelStartTrapCntl_Type = H3cTrapStatus
_H3cIPSecTunnelStartTrapCntl_Object = MibScalar
h3cIPSecTunnelStartTrapCntl = _H3cIPSecTunnelStartTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 2),
    _H3cIPSecTunnelStartTrapCntl_Type()
)
h3cIPSecTunnelStartTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecTunnelStartTrapCntl.setStatus("current")
_H3cIPSecTunnelStopTrapCntl_Type = H3cTrapStatus
_H3cIPSecTunnelStopTrapCntl_Object = MibScalar
h3cIPSecTunnelStopTrapCntl = _H3cIPSecTunnelStopTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 3),
    _H3cIPSecTunnelStopTrapCntl_Type()
)
h3cIPSecTunnelStopTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecTunnelStopTrapCntl.setStatus("current")
_H3cIPSecNoSaTrapCntl_Type = H3cTrapStatus
_H3cIPSecNoSaTrapCntl_Object = MibScalar
h3cIPSecNoSaTrapCntl = _H3cIPSecNoSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 4),
    _H3cIPSecNoSaTrapCntl_Type()
)
h3cIPSecNoSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecNoSaTrapCntl.setStatus("current")
_H3cIPSecAuthFailureTrapCntl_Type = H3cTrapStatus
_H3cIPSecAuthFailureTrapCntl_Object = MibScalar
h3cIPSecAuthFailureTrapCntl = _H3cIPSecAuthFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 5),
    _H3cIPSecAuthFailureTrapCntl_Type()
)
h3cIPSecAuthFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecAuthFailureTrapCntl.setStatus("current")
_H3cIPSecEncryFailureTrapCntl_Type = H3cTrapStatus
_H3cIPSecEncryFailureTrapCntl_Object = MibScalar
h3cIPSecEncryFailureTrapCntl = _H3cIPSecEncryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 6),
    _H3cIPSecEncryFailureTrapCntl_Type()
)
h3cIPSecEncryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecEncryFailureTrapCntl.setStatus("current")
_H3cIPSecDecryFailureTrapCntl_Type = H3cTrapStatus
_H3cIPSecDecryFailureTrapCntl_Object = MibScalar
h3cIPSecDecryFailureTrapCntl = _H3cIPSecDecryFailureTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 7),
    _H3cIPSecDecryFailureTrapCntl_Type()
)
h3cIPSecDecryFailureTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecDecryFailureTrapCntl.setStatus("current")
_H3cIPSecInvalidSaTrapCntl_Type = H3cTrapStatus
_H3cIPSecInvalidSaTrapCntl_Object = MibScalar
h3cIPSecInvalidSaTrapCntl = _H3cIPSecInvalidSaTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 8),
    _H3cIPSecInvalidSaTrapCntl_Type()
)
h3cIPSecInvalidSaTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecInvalidSaTrapCntl.setStatus("current")
_H3cIPSecPolicyAddTrapCntl_Type = H3cTrapStatus
_H3cIPSecPolicyAddTrapCntl_Object = MibScalar
h3cIPSecPolicyAddTrapCntl = _H3cIPSecPolicyAddTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 9),
    _H3cIPSecPolicyAddTrapCntl_Type()
)
h3cIPSecPolicyAddTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecPolicyAddTrapCntl.setStatus("current")
_H3cIPSecPolicyDelTrapCntl_Type = H3cTrapStatus
_H3cIPSecPolicyDelTrapCntl_Object = MibScalar
h3cIPSecPolicyDelTrapCntl = _H3cIPSecPolicyDelTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 10),
    _H3cIPSecPolicyDelTrapCntl_Type()
)
h3cIPSecPolicyDelTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecPolicyDelTrapCntl.setStatus("current")
_H3cIPSecPolicyAttachTrapCntl_Type = H3cTrapStatus
_H3cIPSecPolicyAttachTrapCntl_Object = MibScalar
h3cIPSecPolicyAttachTrapCntl = _H3cIPSecPolicyAttachTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 11),
    _H3cIPSecPolicyAttachTrapCntl_Type()
)
h3cIPSecPolicyAttachTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecPolicyAttachTrapCntl.setStatus("current")
_H3cIPSecPolicyDetachTrapCntl_Type = H3cTrapStatus
_H3cIPSecPolicyDetachTrapCntl_Object = MibScalar
h3cIPSecPolicyDetachTrapCntl = _H3cIPSecPolicyDetachTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 7, 12),
    _H3cIPSecPolicyDetachTrapCntl_Type()
)
h3cIPSecPolicyDetachTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIPSecPolicyDetachTrapCntl.setStatus("current")
_H3cIPSecTrap_ObjectIdentity = ObjectIdentity
h3cIPSecTrap = _H3cIPSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8)
)
_H3cIPSecNotifications_ObjectIdentity = ObjectIdentity
h3cIPSecNotifications = _H3cIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1)
)
_H3cIPSecConformance_ObjectIdentity = ObjectIdentity
h3cIPSecConformance = _H3cIPSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2)
)
_H3cIPSecCompliances_ObjectIdentity = ObjectIdentity
h3cIPSecCompliances = _H3cIPSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 1)
)
_H3cIPSecGroups_ObjectIdentity = ObjectIdentity
h3cIPSecGroups = _H3cIPSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2)
)

# Managed Objects groups

h3cIPSecTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 1)
)
h3cIPSecTunnelTableGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunIKETunnelIndex"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunKeyType"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunEncapMode"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInitiator"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLifeSize"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLifeTime"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemainTime"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunActiveTime"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemainSize"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunTotalRefreshes"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunCurrentSaInstances"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInSaEncryptAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInSaAhAuthAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInSaEspAuthAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunDiffHellmanGrp"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutSaEncryptAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutSaAhAuthAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutSaEspAuthAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunPolicyName"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunPolicyNum"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunStatus"))
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelTableGroup.setStatus("current")

h3cIPSecTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 2)
)
h3cIPSecTunnelStatGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInDecompOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInReplayDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInAuthFails"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInDecryptFails"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutUncompOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunOutEncryptFails"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunNoMemoryDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunQueueFullDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInvalidLenDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunTooLongDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunInvalidSaDropPkts"))
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelStatGroup.setStatus("current")

h3cIPSecSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 3)
)
h3cIPSecSaGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaDirection"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaValue"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaProtocol"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaEncryptAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaAuthAlgo"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaStatus"))
)
if mibBuilder.loadTexts:
    h3cIPSecSaGroup.setStatus("current")

h3cIPSecTrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 4)
)
h3cIPSecTrafficTableGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficLocalType"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficLocalAddr1"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficLocalAddr2"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficLocalProtocol"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficLocalPort"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficRemoteType"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficRemoteAddr1"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficRemoteAddr2"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficRemoteProtocol"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficRemotePort"))
)
if mibBuilder.loadTexts:
    h3cIPSecTrafficTableGroup.setStatus("current")

h3cIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 5)
)
h3cIPSecGlobalStatsGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalActiveTunnels"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalActiveSas"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInDecompOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInDrops"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInReplayDrops"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInAuthFails"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInDecryptFails"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalOutOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalOutUncompOctets"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalOutPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalOutDrops"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalOutEncryptFails"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalNoMemoryDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalNoFindSaDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalQueueFullDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInvalidLenDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalTooLongDropPkts"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalInvalidSaDropPkts"))
)
if mibBuilder.loadTexts:
    h3cIPSecGlobalStatsGroup.setStatus("current")

h3cIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 6)
)
h3cIPSecTrapObjectGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyName"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySeqNum"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySize"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    h3cIPSecTrapObjectGroup.setStatus("current")

h3cIPSecTrapCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 7)
)
h3cIPSecTrapCntlGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrapGlobalCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunnelStartTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunnelStopTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecNoSaTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecAuthFailureTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecEncryFailureTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecDecryFailureTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecInvalidSaTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyAddTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyDelTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyAttachTrapCntl"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyDetachTrapCntl"))
)
if mibBuilder.loadTexts:
    h3cIPSecTrapCntlGroup.setStatus("current")


# Notification objects

h3cIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 1)
)
h3cIPSecTunnelStart.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLifeTime"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelStart.setStatus(
        "current"
    )

h3cIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 2)
)
h3cIPSecTunnelStop.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    h3cIPSecTunnelStop.setStatus(
        "current"
    )

h3cIPSecNoSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 3)
)
h3cIPSecNoSaFailure.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIPSecNoSaFailure.setStatus(
        "current"
    )

h3cIPSecAuthFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 4)
)
h3cIPSecAuthFailFailure.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIPSecAuthFailFailure.setStatus(
        "current"
    )

h3cIPSecEncryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 5)
)
h3cIPSecEncryFailFailure.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIPSecEncryFailFailure.setStatus(
        "current"
    )

h3cIPSecDecryFailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 6)
)
h3cIPSecDecryFailFailure.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"))
)
if mibBuilder.loadTexts:
    h3cIPSecDecryFailFailure.setStatus(
        "current"
    )

h3cIPSecInvalidSaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 7)
)
h3cIPSecInvalidSaFailure.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunLocalAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunRemoteAddr"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    h3cIPSecInvalidSaFailure.setStatus(
        "current"
    )

h3cIPSecPolicyAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 8)
)
h3cIPSecPolicyAdd.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyName"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySeqNum"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySize"))
)
if mibBuilder.loadTexts:
    h3cIPSecPolicyAdd.setStatus(
        "current"
    )

h3cIPSecPolicyDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 9)
)
h3cIPSecPolicyDel.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyName"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySeqNum"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySize"))
)
if mibBuilder.loadTexts:
    h3cIPSecPolicyDel.setStatus(
        "current"
    )

h3cIPSecPolicyAttach = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 10)
)
h3cIPSecPolicyAttach.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyName"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySize"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    h3cIPSecPolicyAttach.setStatus(
        "current"
    )

h3cIPSecPolicyDetach = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 1, 8, 1, 11)
)
h3cIPSecPolicyDetach.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyName"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicySize"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    h3cIPSecPolicyDetach.setStatus(
        "current"
    )


# Notifications groups

h3cIPSecTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 2, 8)
)
h3cIPSecTrapGroup.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunnelStart"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunnelStop"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecNoSaFailure"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecAuthFailFailure"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecEncryFailFailure"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecDecryFailFailure"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecInvalidSaFailure"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyAdd"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyDel"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyAttach"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecPolicyDetach"))
)
if mibBuilder.loadTexts:
    h3cIPSecTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cIPSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 7, 2, 1, 1)
)
h3cIPSecCompliance.setObjects(
      *(("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunnelTableGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTunnelStatGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecSaGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrafficTableGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecGlobalStatsGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrapObjectGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrapCntlGroup"),
        ("A3COM-HUAWEI-IPSEC-MONITOR-MIB", "h3cIPSecTrapGroup"))
)
if mibBuilder.loadTexts:
    h3cIPSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-IPSEC-MONITOR-MIB",
    **{"H3cDiffHellmanGrp": H3cDiffHellmanGrp,
       "H3cEncapMode": H3cEncapMode,
       "H3cEncryptAlgo": H3cEncryptAlgo,
       "H3cAuthAlgo": H3cAuthAlgo,
       "H3cSaProtocol": H3cSaProtocol,
       "H3cTrapStatus": H3cTrapStatus,
       "H3cIPSecIDType": H3cIPSecIDType,
       "H3cTrafficType": H3cTrafficType,
       "H3cIPSecNegoType": H3cIPSecNegoType,
       "H3cIPSecTunnelState": H3cIPSecTunnelState,
       "h3cIPSecMonitor": h3cIPSecMonitor,
       "h3cIPSecObjects": h3cIPSecObjects,
       "h3cIPSecTunnelTable": h3cIPSecTunnelTable,
       "h3cIPSecTunnelEntry": h3cIPSecTunnelEntry,
       "h3cIPSecTunIfIndex": h3cIPSecTunIfIndex,
       "h3cIPSecTunEntryIndex": h3cIPSecTunEntryIndex,
       "h3cIPSecTunIndex": h3cIPSecTunIndex,
       "h3cIPSecTunIKETunnelIndex": h3cIPSecTunIKETunnelIndex,
       "h3cIPSecTunLocalAddr": h3cIPSecTunLocalAddr,
       "h3cIPSecTunRemoteAddr": h3cIPSecTunRemoteAddr,
       "h3cIPSecTunKeyType": h3cIPSecTunKeyType,
       "h3cIPSecTunEncapMode": h3cIPSecTunEncapMode,
       "h3cIPSecTunInitiator": h3cIPSecTunInitiator,
       "h3cIPSecTunLifeSize": h3cIPSecTunLifeSize,
       "h3cIPSecTunLifeTime": h3cIPSecTunLifeTime,
       "h3cIPSecTunRemainTime": h3cIPSecTunRemainTime,
       "h3cIPSecTunActiveTime": h3cIPSecTunActiveTime,
       "h3cIPSecTunRemainSize": h3cIPSecTunRemainSize,
       "h3cIPSecTunTotalRefreshes": h3cIPSecTunTotalRefreshes,
       "h3cIPSecTunCurrentSaInstances": h3cIPSecTunCurrentSaInstances,
       "h3cIPSecTunInSaEncryptAlgo": h3cIPSecTunInSaEncryptAlgo,
       "h3cIPSecTunInSaAhAuthAlgo": h3cIPSecTunInSaAhAuthAlgo,
       "h3cIPSecTunInSaEspAuthAlgo": h3cIPSecTunInSaEspAuthAlgo,
       "h3cIPSecTunDiffHellmanGrp": h3cIPSecTunDiffHellmanGrp,
       "h3cIPSecTunOutSaEncryptAlgo": h3cIPSecTunOutSaEncryptAlgo,
       "h3cIPSecTunOutSaAhAuthAlgo": h3cIPSecTunOutSaAhAuthAlgo,
       "h3cIPSecTunOutSaEspAuthAlgo": h3cIPSecTunOutSaEspAuthAlgo,
       "h3cIPSecTunPolicyName": h3cIPSecTunPolicyName,
       "h3cIPSecTunPolicyNum": h3cIPSecTunPolicyNum,
       "h3cIPSecTunStatus": h3cIPSecTunStatus,
       "h3cIPSecTunnelStatTable": h3cIPSecTunnelStatTable,
       "h3cIPSecTunnelStatEntry": h3cIPSecTunnelStatEntry,
       "h3cIPSecTunInOctets": h3cIPSecTunInOctets,
       "h3cIPSecTunInDecompOctets": h3cIPSecTunInDecompOctets,
       "h3cIPSecTunInPkts": h3cIPSecTunInPkts,
       "h3cIPSecTunInDropPkts": h3cIPSecTunInDropPkts,
       "h3cIPSecTunInReplayDropPkts": h3cIPSecTunInReplayDropPkts,
       "h3cIPSecTunInAuthFails": h3cIPSecTunInAuthFails,
       "h3cIPSecTunInDecryptFails": h3cIPSecTunInDecryptFails,
       "h3cIPSecTunOutOctets": h3cIPSecTunOutOctets,
       "h3cIPSecTunOutUncompOctets": h3cIPSecTunOutUncompOctets,
       "h3cIPSecTunOutPkts": h3cIPSecTunOutPkts,
       "h3cIPSecTunOutDropPkts": h3cIPSecTunOutDropPkts,
       "h3cIPSecTunOutEncryptFails": h3cIPSecTunOutEncryptFails,
       "h3cIPSecTunNoMemoryDropPkts": h3cIPSecTunNoMemoryDropPkts,
       "h3cIPSecTunQueueFullDropPkts": h3cIPSecTunQueueFullDropPkts,
       "h3cIPSecTunInvalidLenDropPkts": h3cIPSecTunInvalidLenDropPkts,
       "h3cIPSecTunTooLongDropPkts": h3cIPSecTunTooLongDropPkts,
       "h3cIPSecTunInvalidSaDropPkts": h3cIPSecTunInvalidSaDropPkts,
       "h3cIPSecSaTable": h3cIPSecSaTable,
       "h3cIPSecSaEntry": h3cIPSecSaEntry,
       "h3cIPSecSaIndex": h3cIPSecSaIndex,
       "h3cIPSecSaDirection": h3cIPSecSaDirection,
       "h3cIPSecSaValue": h3cIPSecSaValue,
       "h3cIPSecSaProtocol": h3cIPSecSaProtocol,
       "h3cIPSecSaEncryptAlgo": h3cIPSecSaEncryptAlgo,
       "h3cIPSecSaAuthAlgo": h3cIPSecSaAuthAlgo,
       "h3cIPSecSaStatus": h3cIPSecSaStatus,
       "h3cIPSecTrafficTable": h3cIPSecTrafficTable,
       "h3cIPSecTrafficEntry": h3cIPSecTrafficEntry,
       "h3cIPSecTrafficLocalType": h3cIPSecTrafficLocalType,
       "h3cIPSecTrafficLocalAddr1": h3cIPSecTrafficLocalAddr1,
       "h3cIPSecTrafficLocalAddr2": h3cIPSecTrafficLocalAddr2,
       "h3cIPSecTrafficLocalProtocol": h3cIPSecTrafficLocalProtocol,
       "h3cIPSecTrafficLocalPort": h3cIPSecTrafficLocalPort,
       "h3cIPSecTrafficRemoteType": h3cIPSecTrafficRemoteType,
       "h3cIPSecTrafficRemoteAddr1": h3cIPSecTrafficRemoteAddr1,
       "h3cIPSecTrafficRemoteAddr2": h3cIPSecTrafficRemoteAddr2,
       "h3cIPSecTrafficRemoteProtocol": h3cIPSecTrafficRemoteProtocol,
       "h3cIPSecTrafficRemotePort": h3cIPSecTrafficRemotePort,
       "h3cIPSecGlobalStats": h3cIPSecGlobalStats,
       "h3cIPSecGlobalActiveTunnels": h3cIPSecGlobalActiveTunnels,
       "h3cIPSecGlobalActiveSas": h3cIPSecGlobalActiveSas,
       "h3cIPSecGlobalInOctets": h3cIPSecGlobalInOctets,
       "h3cIPSecGlobalInDecompOctets": h3cIPSecGlobalInDecompOctets,
       "h3cIPSecGlobalInPkts": h3cIPSecGlobalInPkts,
       "h3cIPSecGlobalInDrops": h3cIPSecGlobalInDrops,
       "h3cIPSecGlobalInReplayDrops": h3cIPSecGlobalInReplayDrops,
       "h3cIPSecGlobalInAuthFails": h3cIPSecGlobalInAuthFails,
       "h3cIPSecGlobalInDecryptFails": h3cIPSecGlobalInDecryptFails,
       "h3cIPSecGlobalOutOctets": h3cIPSecGlobalOutOctets,
       "h3cIPSecGlobalOutUncompOctets": h3cIPSecGlobalOutUncompOctets,
       "h3cIPSecGlobalOutPkts": h3cIPSecGlobalOutPkts,
       "h3cIPSecGlobalOutDrops": h3cIPSecGlobalOutDrops,
       "h3cIPSecGlobalOutEncryptFails": h3cIPSecGlobalOutEncryptFails,
       "h3cIPSecGlobalNoMemoryDropPkts": h3cIPSecGlobalNoMemoryDropPkts,
       "h3cIPSecGlobalNoFindSaDropPkts": h3cIPSecGlobalNoFindSaDropPkts,
       "h3cIPSecGlobalQueueFullDropPkts": h3cIPSecGlobalQueueFullDropPkts,
       "h3cIPSecGlobalInvalidLenDropPkts": h3cIPSecGlobalInvalidLenDropPkts,
       "h3cIPSecGlobalTooLongDropPkts": h3cIPSecGlobalTooLongDropPkts,
       "h3cIPSecGlobalInvalidSaDropPkts": h3cIPSecGlobalInvalidSaDropPkts,
       "h3cIPSecTrapObject": h3cIPSecTrapObject,
       "h3cIPSecPolicyName": h3cIPSecPolicyName,
       "h3cIPSecPolicySeqNum": h3cIPSecPolicySeqNum,
       "h3cIPSecPolicySize": h3cIPSecPolicySize,
       "h3cIPSecSpiValue": h3cIPSecSpiValue,
       "h3cIPSecTrapCntl": h3cIPSecTrapCntl,
       "h3cIPSecTrapGlobalCntl": h3cIPSecTrapGlobalCntl,
       "h3cIPSecTunnelStartTrapCntl": h3cIPSecTunnelStartTrapCntl,
       "h3cIPSecTunnelStopTrapCntl": h3cIPSecTunnelStopTrapCntl,
       "h3cIPSecNoSaTrapCntl": h3cIPSecNoSaTrapCntl,
       "h3cIPSecAuthFailureTrapCntl": h3cIPSecAuthFailureTrapCntl,
       "h3cIPSecEncryFailureTrapCntl": h3cIPSecEncryFailureTrapCntl,
       "h3cIPSecDecryFailureTrapCntl": h3cIPSecDecryFailureTrapCntl,
       "h3cIPSecInvalidSaTrapCntl": h3cIPSecInvalidSaTrapCntl,
       "h3cIPSecPolicyAddTrapCntl": h3cIPSecPolicyAddTrapCntl,
       "h3cIPSecPolicyDelTrapCntl": h3cIPSecPolicyDelTrapCntl,
       "h3cIPSecPolicyAttachTrapCntl": h3cIPSecPolicyAttachTrapCntl,
       "h3cIPSecPolicyDetachTrapCntl": h3cIPSecPolicyDetachTrapCntl,
       "h3cIPSecTrap": h3cIPSecTrap,
       "h3cIPSecNotifications": h3cIPSecNotifications,
       "h3cIPSecTunnelStart": h3cIPSecTunnelStart,
       "h3cIPSecTunnelStop": h3cIPSecTunnelStop,
       "h3cIPSecNoSaFailure": h3cIPSecNoSaFailure,
       "h3cIPSecAuthFailFailure": h3cIPSecAuthFailFailure,
       "h3cIPSecEncryFailFailure": h3cIPSecEncryFailFailure,
       "h3cIPSecDecryFailFailure": h3cIPSecDecryFailFailure,
       "h3cIPSecInvalidSaFailure": h3cIPSecInvalidSaFailure,
       "h3cIPSecPolicyAdd": h3cIPSecPolicyAdd,
       "h3cIPSecPolicyDel": h3cIPSecPolicyDel,
       "h3cIPSecPolicyAttach": h3cIPSecPolicyAttach,
       "h3cIPSecPolicyDetach": h3cIPSecPolicyDetach,
       "h3cIPSecConformance": h3cIPSecConformance,
       "h3cIPSecCompliances": h3cIPSecCompliances,
       "h3cIPSecCompliance": h3cIPSecCompliance,
       "h3cIPSecGroups": h3cIPSecGroups,
       "h3cIPSecTunnelTableGroup": h3cIPSecTunnelTableGroup,
       "h3cIPSecTunnelStatGroup": h3cIPSecTunnelStatGroup,
       "h3cIPSecSaGroup": h3cIPSecSaGroup,
       "h3cIPSecTrafficTableGroup": h3cIPSecTrafficTableGroup,
       "h3cIPSecGlobalStatsGroup": h3cIPSecGlobalStatsGroup,
       "h3cIPSecTrapObjectGroup": h3cIPSecTrapObjectGroup,
       "h3cIPSecTrapCntlGroup": h3cIPSecTrapCntlGroup,
       "h3cIPSecTrapGroup": h3cIPSecTrapGroup}
)
