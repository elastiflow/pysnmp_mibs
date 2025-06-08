# SNMP MIB module (RUIJIE-CAPWAP-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-DHCP-SERVER-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(ruijieIfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-INTERFACE-MIB",
    "ruijieIfIndex")

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

ruijieCapwapDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58)
)
if mibBuilder.loadTexts:
    ruijieCapwapDhcpMIB.setRevisions(
        ("2009-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCapwapDhcpMIBTrap_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpMIBTrap = _RuijieCapwapDhcpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 0)
)
_RuijieCapwapDhcpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpMIBObjects = _RuijieCapwapDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1)
)
_RuijieCapwapDhcpGlobalConfig_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpGlobalConfig = _RuijieCapwapDhcpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1)
)
_RuijieLDhcpClearAllStats_Type = TruthValue
_RuijieLDhcpClearAllStats_Object = MibScalar
ruijieLDhcpClearAllStats = _RuijieLDhcpClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1, 1),
    _RuijieLDhcpClearAllStats_Type()
)
ruijieLDhcpClearAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLDhcpClearAllStats.setStatus("current")


class _RuijieLDhcpStartService_Type(Integer32):
    """Custom type ruijieLDhcpStartService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieLDhcpStartService_Type.__name__ = "Integer32"
_RuijieLDhcpStartService_Object = MibScalar
ruijieLDhcpStartService = _RuijieLDhcpStartService_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1, 2),
    _RuijieLDhcpStartService_Type()
)
ruijieLDhcpStartService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLDhcpStartService.setStatus("current")
_RuijieDhcpClientMacAddress_Type = MacAddress
_RuijieDhcpClientMacAddress_Object = MibScalar
ruijieDhcpClientMacAddress = _RuijieDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1, 3),
    _RuijieDhcpClientMacAddress_Type()
)
ruijieDhcpClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDhcpClientMacAddress.setStatus("current")


class _RuijieLDhcpStartTIService_Type(Integer32):
    """Custom type ruijieLDhcpStartTIService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieLDhcpStartTIService_Type.__name__ = "Integer32"
_RuijieLDhcpStartTIService_Object = MibScalar
ruijieLDhcpStartTIService = _RuijieLDhcpStartTIService_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1, 4),
    _RuijieLDhcpStartTIService_Type()
)
ruijieLDhcpStartTIService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLDhcpStartTIService.setStatus("current")
_RuijieDhcpServerTlvNum_Type = Integer32
_RuijieDhcpServerTlvNum_Object = MibScalar
ruijieDhcpServerTlvNum = _RuijieDhcpServerTlvNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1, 5),
    _RuijieDhcpServerTlvNum_Type()
)
ruijieDhcpServerTlvNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDhcpServerTlvNum.setStatus("current")
_RuijieDhcpServerTlv_Type = DisplayString
_RuijieDhcpServerTlv_Object = MibScalar
ruijieDhcpServerTlv = _RuijieDhcpServerTlv_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 1, 6),
    _RuijieDhcpServerTlv_Type()
)
ruijieDhcpServerTlv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieDhcpServerTlv.setStatus("current")
_RuijieCapwapDhcpShowStats_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpShowStats = _RuijieCapwapDhcpShowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2)
)
_RuijieLDhcpDiscoverPkts_Type = Unsigned32
_RuijieLDhcpDiscoverPkts_Object = MibScalar
ruijieLDhcpDiscoverPkts = _RuijieLDhcpDiscoverPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 1),
    _RuijieLDhcpDiscoverPkts_Type()
)
ruijieLDhcpDiscoverPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpDiscoverPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpDiscoverPkts.setUnits("packets")
_RuijieLDhcpRequestPkts_Type = Unsigned32
_RuijieLDhcpRequestPkts_Object = MibScalar
ruijieLDhcpRequestPkts = _RuijieLDhcpRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 2),
    _RuijieLDhcpRequestPkts_Type()
)
ruijieLDhcpRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpRequestPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpRequestPkts.setUnits("packets")
_RuijieLDhcpDeclinePkts_Type = Unsigned32
_RuijieLDhcpDeclinePkts_Object = MibScalar
ruijieLDhcpDeclinePkts = _RuijieLDhcpDeclinePkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 3),
    _RuijieLDhcpDeclinePkts_Type()
)
ruijieLDhcpDeclinePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpDeclinePkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpDeclinePkts.setUnits("packets")
_RuijieLDhcpInformPkts_Type = Unsigned32
_RuijieLDhcpInformPkts_Object = MibScalar
ruijieLDhcpInformPkts = _RuijieLDhcpInformPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 4),
    _RuijieLDhcpInformPkts_Type()
)
ruijieLDhcpInformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpInformPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpInformPkts.setUnits("packets")
_RuijieLDhcpReleasePkts_Type = Unsigned32
_RuijieLDhcpReleasePkts_Object = MibScalar
ruijieLDhcpReleasePkts = _RuijieLDhcpReleasePkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 5),
    _RuijieLDhcpReleasePkts_Type()
)
ruijieLDhcpReleasePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpReleasePkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpReleasePkts.setUnits("packets")
_RuijieLDhcpReplyPkts_Type = Unsigned32
_RuijieLDhcpReplyPkts_Object = MibScalar
ruijieLDhcpReplyPkts = _RuijieLDhcpReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 6),
    _RuijieLDhcpReplyPkts_Type()
)
ruijieLDhcpReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpReplyPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpReplyPkts.setUnits("packets")
_RuijieLDhcpOfferPkts_Type = Unsigned32
_RuijieLDhcpOfferPkts_Object = MibScalar
ruijieLDhcpOfferPkts = _RuijieLDhcpOfferPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 7),
    _RuijieLDhcpOfferPkts_Type()
)
ruijieLDhcpOfferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpOfferPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpOfferPkts.setUnits("packets")
_RuijieLDhcpAckPkts_Type = Unsigned32
_RuijieLDhcpAckPkts_Object = MibScalar
ruijieLDhcpAckPkts = _RuijieLDhcpAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 8),
    _RuijieLDhcpAckPkts_Type()
)
ruijieLDhcpAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpAckPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpAckPkts.setUnits("packets")
_RuijieLDhcpNakPkts_Type = Unsigned32
_RuijieLDhcpNakPkts_Object = MibScalar
ruijieLDhcpNakPkts = _RuijieLDhcpNakPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 9),
    _RuijieLDhcpNakPkts_Type()
)
ruijieLDhcpNakPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpNakPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpNakPkts.setUnits("packets")
_RuijieLDhcpReqTimes_Type = Unsigned32
_RuijieLDhcpReqTimes_Object = MibScalar
ruijieLDhcpReqTimes = _RuijieLDhcpReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 10),
    _RuijieLDhcpReqTimes_Type()
)
ruijieLDhcpReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpReqTimes.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpReqTimes.setUnits("packets")
_RuijieLDhcpReqSucTimes_Type = Unsigned32
_RuijieLDhcpReqSucTimes_Object = MibScalar
ruijieLDhcpReqSucTimes = _RuijieLDhcpReqSucTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 2, 11),
    _RuijieLDhcpReqSucTimes_Type()
)
ruijieLDhcpReqSucTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLDhcpReqSucTimes.setStatus("current")
if mibBuilder.loadTexts:
    ruijieLDhcpReqSucTimes.setUnits("packets")
_RuijieCapwapDhcpServerConfig_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpServerConfig = _RuijieCapwapDhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3)
)
_RuijieDhcpScopeTable_Object = MibTable
ruijieDhcpScopeTable = _RuijieDhcpScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpScopeTable.setStatus("current")
_RuijieDhcpScopeEntry_Object = MibTableRow
ruijieDhcpScopeEntry = _RuijieDhcpScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1)
)
ruijieDhcpScopeEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpScopeEntry.setStatus("current")


class _RuijieDhcpScopeIndex_Type(Unsigned32):
    """Custom type ruijieDhcpScopeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieDhcpScopeIndex_Type.__name__ = "Unsigned32"
_RuijieDhcpScopeIndex_Object = MibTableColumn
ruijieDhcpScopeIndex = _RuijieDhcpScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 1),
    _RuijieDhcpScopeIndex_Type()
)
ruijieDhcpScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDhcpScopeIndex.setStatus("current")


class _RuijieDhcpScopeName_Type(DisplayString):
    """Custom type ruijieDhcpScopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieDhcpScopeName_Type.__name__ = "DisplayString"
_RuijieDhcpScopeName_Object = MibTableColumn
ruijieDhcpScopeName = _RuijieDhcpScopeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 2),
    _RuijieDhcpScopeName_Type()
)
ruijieDhcpScopeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeName.setStatus("current")


class _RuijieDhcpScopeLeaseTime_Type(Integer32):
    """Custom type ruijieDhcpScopeLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 8640000),
    )


_RuijieDhcpScopeLeaseTime_Type.__name__ = "Integer32"
_RuijieDhcpScopeLeaseTime_Object = MibTableColumn
ruijieDhcpScopeLeaseTime = _RuijieDhcpScopeLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 3),
    _RuijieDhcpScopeLeaseTime_Type()
)
ruijieDhcpScopeLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeLeaseTime.setStatus("current")
_RuijieDhcpScopeNetwork_Type = IpAddress
_RuijieDhcpScopeNetwork_Object = MibTableColumn
ruijieDhcpScopeNetwork = _RuijieDhcpScopeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 4),
    _RuijieDhcpScopeNetwork_Type()
)
ruijieDhcpScopeNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeNetwork.setStatus("current")
_RuijieDhcpScopeNetmask_Type = IpAddress
_RuijieDhcpScopeNetmask_Object = MibTableColumn
ruijieDhcpScopeNetmask = _RuijieDhcpScopeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 5),
    _RuijieDhcpScopeNetmask_Type()
)
ruijieDhcpScopeNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeNetmask.setStatus("current")
_RuijieDhcpScopePoolStartAddress_Type = IpAddress
_RuijieDhcpScopePoolStartAddress_Object = MibTableColumn
ruijieDhcpScopePoolStartAddress = _RuijieDhcpScopePoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 6),
    _RuijieDhcpScopePoolStartAddress_Type()
)
ruijieDhcpScopePoolStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopePoolStartAddress.setStatus("current")
_RuijieDhcpScopePoolEndAddress_Type = IpAddress
_RuijieDhcpScopePoolEndAddress_Object = MibTableColumn
ruijieDhcpScopePoolEndAddress = _RuijieDhcpScopePoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 7),
    _RuijieDhcpScopePoolEndAddress_Type()
)
ruijieDhcpScopePoolEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopePoolEndAddress.setStatus("current")
_RuijieDhcpScopeDefaultRouterAddress1_Type = IpAddress
_RuijieDhcpScopeDefaultRouterAddress1_Object = MibTableColumn
ruijieDhcpScopeDefaultRouterAddress1 = _RuijieDhcpScopeDefaultRouterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 8),
    _RuijieDhcpScopeDefaultRouterAddress1_Type()
)
ruijieDhcpScopeDefaultRouterAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDefaultRouterAddress1.setStatus("current")
_RuijieDhcpScopeDefaultRouterAddress2_Type = IpAddress
_RuijieDhcpScopeDefaultRouterAddress2_Object = MibTableColumn
ruijieDhcpScopeDefaultRouterAddress2 = _RuijieDhcpScopeDefaultRouterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 9),
    _RuijieDhcpScopeDefaultRouterAddress2_Type()
)
ruijieDhcpScopeDefaultRouterAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDefaultRouterAddress2.setStatus("current")
_RuijieDhcpScopeDefaultRouterAddress3_Type = IpAddress
_RuijieDhcpScopeDefaultRouterAddress3_Object = MibTableColumn
ruijieDhcpScopeDefaultRouterAddress3 = _RuijieDhcpScopeDefaultRouterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 10),
    _RuijieDhcpScopeDefaultRouterAddress3_Type()
)
ruijieDhcpScopeDefaultRouterAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDefaultRouterAddress3.setStatus("current")


class _RuijieDhcpScopeDnsDomainName_Type(DisplayString):
    """Custom type ruijieDhcpScopeDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieDhcpScopeDnsDomainName_Type.__name__ = "DisplayString"
_RuijieDhcpScopeDnsDomainName_Object = MibTableColumn
ruijieDhcpScopeDnsDomainName = _RuijieDhcpScopeDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 11),
    _RuijieDhcpScopeDnsDomainName_Type()
)
ruijieDhcpScopeDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDnsDomainName.setStatus("current")
_RuijieDhcpScopeDnsServerAddress1_Type = IpAddress
_RuijieDhcpScopeDnsServerAddress1_Object = MibTableColumn
ruijieDhcpScopeDnsServerAddress1 = _RuijieDhcpScopeDnsServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 12),
    _RuijieDhcpScopeDnsServerAddress1_Type()
)
ruijieDhcpScopeDnsServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDnsServerAddress1.setStatus("current")
_RuijieDhcpScopeDnsServerAddress2_Type = IpAddress
_RuijieDhcpScopeDnsServerAddress2_Object = MibTableColumn
ruijieDhcpScopeDnsServerAddress2 = _RuijieDhcpScopeDnsServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 13),
    _RuijieDhcpScopeDnsServerAddress2_Type()
)
ruijieDhcpScopeDnsServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDnsServerAddress2.setStatus("current")
_RuijieDhcpScopeDnsServerAddress3_Type = IpAddress
_RuijieDhcpScopeDnsServerAddress3_Object = MibTableColumn
ruijieDhcpScopeDnsServerAddress3 = _RuijieDhcpScopeDnsServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 14),
    _RuijieDhcpScopeDnsServerAddress3_Type()
)
ruijieDhcpScopeDnsServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeDnsServerAddress3.setStatus("current")
_RuijieDhcpScopeNetbiosNameServerAddress1_Type = IpAddress
_RuijieDhcpScopeNetbiosNameServerAddress1_Object = MibTableColumn
ruijieDhcpScopeNetbiosNameServerAddress1 = _RuijieDhcpScopeNetbiosNameServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 15),
    _RuijieDhcpScopeNetbiosNameServerAddress1_Type()
)
ruijieDhcpScopeNetbiosNameServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeNetbiosNameServerAddress1.setStatus("current")
_RuijieDhcpScopeNetbiosNameServerAddress2_Type = IpAddress
_RuijieDhcpScopeNetbiosNameServerAddress2_Object = MibTableColumn
ruijieDhcpScopeNetbiosNameServerAddress2 = _RuijieDhcpScopeNetbiosNameServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 16),
    _RuijieDhcpScopeNetbiosNameServerAddress2_Type()
)
ruijieDhcpScopeNetbiosNameServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeNetbiosNameServerAddress2.setStatus("current")
_RuijieDhcpScopeNetbiosNameServerAddress3_Type = IpAddress
_RuijieDhcpScopeNetbiosNameServerAddress3_Object = MibTableColumn
ruijieDhcpScopeNetbiosNameServerAddress3 = _RuijieDhcpScopeNetbiosNameServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 17),
    _RuijieDhcpScopeNetbiosNameServerAddress3_Type()
)
ruijieDhcpScopeNetbiosNameServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeNetbiosNameServerAddress3.setStatus("current")


class _RuijieDhcpScopeState_Type(Integer32):
    """Custom type ruijieDhcpScopeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieDhcpScopeState_Type.__name__ = "Integer32"
_RuijieDhcpScopeState_Object = MibTableColumn
ruijieDhcpScopeState = _RuijieDhcpScopeState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 18),
    _RuijieDhcpScopeState_Type()
)
ruijieDhcpScopeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeState.setStatus("current")
_RuijieDhcpScopeRowStatus_Type = RowStatus
_RuijieDhcpScopeRowStatus_Object = MibTableColumn
ruijieDhcpScopeRowStatus = _RuijieDhcpScopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 19),
    _RuijieDhcpScopeRowStatus_Type()
)
ruijieDhcpScopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpScopeRowStatus.setStatus("current")


class _RuijieDhcpIPPoolUsage_Type(Integer32):
    """Custom type ruijieDhcpIPPoolUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieDhcpIPPoolUsage_Type.__name__ = "Integer32"
_RuijieDhcpIPPoolUsage_Object = MibTableColumn
ruijieDhcpIPPoolUsage = _RuijieDhcpIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 20),
    _RuijieDhcpIPPoolUsage_Type()
)
ruijieDhcpIPPoolUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpIPPoolUsage.setStatus("current")
_RuijieDhcpoption43_Type = IpAddress
_RuijieDhcpoption43_Object = MibTableColumn
ruijieDhcpoption43 = _RuijieDhcpoption43_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 21),
    _RuijieDhcpoption43_Type()
)
ruijieDhcpoption43.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpoption43.setStatus("current")
_RuijieDhcpoption138_Type = IpAddress
_RuijieDhcpoption138_Object = MibTableColumn
ruijieDhcpoption138 = _RuijieDhcpoption138_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 22),
    _RuijieDhcpoption138_Type()
)
ruijieDhcpoption138.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpoption138.setStatus("current")
_RuijieDhcpReqtimes_Type = Unsigned32
_RuijieDhcpReqtimes_Object = MibTableColumn
ruijieDhcpReqtimes = _RuijieDhcpReqtimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 23),
    _RuijieDhcpReqtimes_Type()
)
ruijieDhcpReqtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpReqtimes.setStatus("current")
_RuijieDhcpReqSuctimes_Type = Unsigned32
_RuijieDhcpReqSuctimes_Object = MibTableColumn
ruijieDhcpReqSuctimes = _RuijieDhcpReqSuctimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 24),
    _RuijieDhcpReqSuctimes_Type()
)
ruijieDhcpReqSuctimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpReqSuctimes.setStatus("current")
_RuijieDhcpTotalIPNum_Type = Integer32
_RuijieDhcpTotalIPNum_Object = MibTableColumn
ruijieDhcpTotalIPNum = _RuijieDhcpTotalIPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 25),
    _RuijieDhcpTotalIPNum_Type()
)
ruijieDhcpTotalIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpTotalIPNum.setStatus("current")
_RuijieDhcpCurrentUsedIPNum_Type = Integer32
_RuijieDhcpCurrentUsedIPNum_Object = MibTableColumn
ruijieDhcpCurrentUsedIPNum = _RuijieDhcpCurrentUsedIPNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 26),
    _RuijieDhcpCurrentUsedIPNum_Type()
)
ruijieDhcpCurrentUsedIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpCurrentUsedIPNum.setStatus("current")
_RuijieDhcpOffertimes_Type = Unsigned32
_RuijieDhcpOffertimes_Object = MibTableColumn
ruijieDhcpOffertimes = _RuijieDhcpOffertimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 27),
    _RuijieDhcpOffertimes_Type()
)
ruijieDhcpOffertimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpOffertimes.setStatus("current")
_RuijieDhcpAcktimes_Type = Unsigned32
_RuijieDhcpAcktimes_Object = MibTableColumn
ruijieDhcpAcktimes = _RuijieDhcpAcktimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 1, 1, 28),
    _RuijieDhcpAcktimes_Type()
)
ruijieDhcpAcktimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpAcktimes.setStatus("current")
_RuijieDhcpServerIpVlanTable_Object = MibTable
ruijieDhcpServerIpVlanTable = _RuijieDhcpServerIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpServerIpVlanTable.setStatus("current")
_RuijieDhcpServerIpVlanEntry_Object = MibTableRow
ruijieDhcpServerIpVlanEntry = _RuijieDhcpServerIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 2, 1)
)
ruijieDhcpServerIpVlanEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpServerIpVlanIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpServerIpVlanEntry.setStatus("current")


class _RuijieDhcpServerIpVlanIndex_Type(Unsigned32):
    """Custom type ruijieDhcpServerIpVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieDhcpServerIpVlanIndex_Type.__name__ = "Unsigned32"
_RuijieDhcpServerIpVlanIndex_Object = MibTableColumn
ruijieDhcpServerIpVlanIndex = _RuijieDhcpServerIpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 2, 1, 1),
    _RuijieDhcpServerIpVlanIndex_Type()
)
ruijieDhcpServerIpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDhcpServerIpVlanIndex.setStatus("current")
_RuijieDhcpServerIpVlanOnlineUserNum_Type = Unsigned32
_RuijieDhcpServerIpVlanOnlineUserNum_Object = MibTableColumn
ruijieDhcpServerIpVlanOnlineUserNum = _RuijieDhcpServerIpVlanOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 3, 2, 1, 2),
    _RuijieDhcpServerIpVlanOnlineUserNum_Type()
)
ruijieDhcpServerIpVlanOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDhcpServerIpVlanOnlineUserNum.setStatus("current")
_RuijieCapwapDhcpRelayConfig_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpRelayConfig = _RuijieCapwapDhcpRelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4)
)
_RuijieDhcpGlobalServerAddrTable_Object = MibTable
ruijieDhcpGlobalServerAddrTable = _RuijieDhcpGlobalServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieDhcpGlobalServerAddrTable.setStatus("current")
_RuijieDhcpGlobalServerAddrEntry_Object = MibTableRow
ruijieDhcpGlobalServerAddrEntry = _RuijieDhcpGlobalServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 1, 1)
)
ruijieDhcpGlobalServerAddrEntry.setIndexNames(
    (0, "RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpGlobalServerIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpGlobalServerAddrEntry.setStatus("current")


class _RuijieDhcpGlobalServerIndex_Type(Integer32):
    """Custom type ruijieDhcpGlobalServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RuijieDhcpGlobalServerIndex_Type.__name__ = "Integer32"
_RuijieDhcpGlobalServerIndex_Object = MibTableColumn
ruijieDhcpGlobalServerIndex = _RuijieDhcpGlobalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 1, 1, 1),
    _RuijieDhcpGlobalServerIndex_Type()
)
ruijieDhcpGlobalServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDhcpGlobalServerIndex.setStatus("current")
_RuijieDhcpGlobalServerAddress_Type = IpAddress
_RuijieDhcpGlobalServerAddress_Object = MibTableColumn
ruijieDhcpGlobalServerAddress = _RuijieDhcpGlobalServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 1, 1, 2),
    _RuijieDhcpGlobalServerAddress_Type()
)
ruijieDhcpGlobalServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpGlobalServerAddress.setStatus("current")
_RuijieDhcpGlobalServerRowStatus_Type = RowStatus
_RuijieDhcpGlobalServerRowStatus_Object = MibTableColumn
ruijieDhcpGlobalServerRowStatus = _RuijieDhcpGlobalServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 1, 1, 3),
    _RuijieDhcpGlobalServerRowStatus_Type()
)
ruijieDhcpGlobalServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpGlobalServerRowStatus.setStatus("current")
_RuijieDhcpIntfServerAddrTable_Object = MibTable
ruijieDhcpIntfServerAddrTable = _RuijieDhcpIntfServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ruijieDhcpIntfServerAddrTable.setStatus("current")
_RuijieDhcpIntfServerAddrEntry_Object = MibTableRow
ruijieDhcpIntfServerAddrEntry = _RuijieDhcpIntfServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 2, 1)
)
ruijieDhcpIntfServerAddrEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-MIB", "ruijieIfIndex"),
    (0, "RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpIntfServerIndex"),
)
if mibBuilder.loadTexts:
    ruijieDhcpIntfServerAddrEntry.setStatus("current")


class _RuijieDhcpIntfServerIndex_Type(Integer32):
    """Custom type ruijieDhcpIntfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RuijieDhcpIntfServerIndex_Type.__name__ = "Integer32"
_RuijieDhcpIntfServerIndex_Object = MibTableColumn
ruijieDhcpIntfServerIndex = _RuijieDhcpIntfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 2, 1, 1),
    _RuijieDhcpIntfServerIndex_Type()
)
ruijieDhcpIntfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieDhcpIntfServerIndex.setStatus("current")
_RuijieDhcpIntfServerAddress_Type = IpAddress
_RuijieDhcpIntfServerAddress_Object = MibTableColumn
ruijieDhcpIntfServerAddress = _RuijieDhcpIntfServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 2, 1, 2),
    _RuijieDhcpIntfServerAddress_Type()
)
ruijieDhcpIntfServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpIntfServerAddress.setStatus("current")
_RuijieDhcpIntfServerRowStatus_Type = RowStatus
_RuijieDhcpIntfServerRowStatus_Object = MibTableColumn
ruijieDhcpIntfServerRowStatus = _RuijieDhcpIntfServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 1, 4, 2, 1, 3),
    _RuijieDhcpIntfServerRowStatus_Type()
)
ruijieDhcpIntfServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDhcpIntfServerRowStatus.setStatus("current")
_RuijieCapwapDhcpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpMIBConformance = _RuijieCapwapDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2)
)
_RuijieCapwapDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpMIBCompliances = _RuijieCapwapDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 1)
)
_RuijieCapwapDhcpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieCapwapDhcpMIBGroups = _RuijieCapwapDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 2)
)

# Managed Objects groups

ruijieCapwapDhcpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 2, 1)
)
ruijieCapwapDhcpMIBGroup.setObjects(
      *(("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpClearAllStats"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpStartService"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpDiscoverPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpRequestPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpDeclinePkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpInformPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpReleasePkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpReplyPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpOfferPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpAckPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpNakPkts"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpReqTimes"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieLDhcpReqSucTimes"))
)
if mibBuilder.loadTexts:
    ruijieCapwapDhcpMIBGroup.setStatus("current")

ruijieCapwapDhcpServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 2, 2)
)
ruijieCapwapDhcpServerConfigGroup.setObjects(
      *(("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeName"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeLeaseTime"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeNetwork"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeNetmask"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDefaultRouterAddress1"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDefaultRouterAddress2"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDefaultRouterAddress3"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDnsDomainName"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDnsServerAddress1"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDnsServerAddress2"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeDnsServerAddress3"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeNetbiosNameServerAddress1"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeNetbiosNameServerAddress2"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeNetbiosNameServerAddress3"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeState"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeRowStatus"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpIPPoolUsage"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpoption43"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpoption138"))
)
if mibBuilder.loadTexts:
    ruijieCapwapDhcpServerConfigGroup.setStatus("current")

ruijieCapwapDhcpRelayGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 2, 3)
)
ruijieCapwapDhcpRelayGlobalConfigGroup.setObjects(
      *(("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpGlobalServerAddress"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpGlobalServerRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieCapwapDhcpRelayGlobalConfigGroup.setStatus("current")

ruijieCapwapDhcpRelayIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 2, 4)
)
ruijieCapwapDhcpRelayIntfConfigGroup.setObjects(
      *(("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpIntfServerAddress"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpIntfServerRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieCapwapDhcpRelayIntfConfigGroup.setStatus("current")


# Notification objects

ruijieDhcpAddressExhaustTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 0, 1)
)
ruijieDhcpAddressExhaustTrap.setObjects(
    ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeName")
)
if mibBuilder.loadTexts:
    ruijieDhcpAddressExhaustTrap.setStatus(
        "current"
    )

ruijieDhcpAddressExhaustRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 0, 2)
)
ruijieDhcpAddressExhaustRecovTrap.setObjects(
    ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpScopeName")
)
if mibBuilder.loadTexts:
    ruijieDhcpAddressExhaustRecovTrap.setStatus(
        "current"
    )

ruijieDhcpClientFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 0, 3)
)
ruijieDhcpClientFailTrap.setObjects(
    ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpClientMacAddress")
)
if mibBuilder.loadTexts:
    ruijieDhcpClientFailTrap.setStatus(
        "current"
    )

ruijieDhcpServerInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 0, 4)
)
ruijieDhcpServerInfoTrap.setObjects(
      *(("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpServerTlvNum"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieDhcpServerTlv"))
)
if mibBuilder.loadTexts:
    ruijieDhcpServerInfoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCapwapDhcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 58, 2, 1, 1)
)
ruijieCapwapDhcpMIBCompliance.setObjects(
      *(("RUIJIE-CAPWAP-DHCP-MIB", "ruijieCapwapDhcpMIBGroup"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieCapwapDhcpServerConfigGroup"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieCapwapDhcpRelayGlobalConfigGroup"),
        ("RUIJIE-CAPWAP-DHCP-MIB", "ruijieCapwapDhcpRelayIntfConfigGroup"))
)
if mibBuilder.loadTexts:
    ruijieCapwapDhcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CAPWAP-DHCP-MIB",
    **{"ruijieCapwapDhcpMIB": ruijieCapwapDhcpMIB,
       "ruijieCapwapDhcpMIBTrap": ruijieCapwapDhcpMIBTrap,
       "ruijieDhcpAddressExhaustTrap": ruijieDhcpAddressExhaustTrap,
       "ruijieDhcpAddressExhaustRecovTrap": ruijieDhcpAddressExhaustRecovTrap,
       "ruijieDhcpClientFailTrap": ruijieDhcpClientFailTrap,
       "ruijieDhcpServerInfoTrap": ruijieDhcpServerInfoTrap,
       "ruijieCapwapDhcpMIBObjects": ruijieCapwapDhcpMIBObjects,
       "ruijieCapwapDhcpGlobalConfig": ruijieCapwapDhcpGlobalConfig,
       "ruijieLDhcpClearAllStats": ruijieLDhcpClearAllStats,
       "ruijieLDhcpStartService": ruijieLDhcpStartService,
       "ruijieDhcpClientMacAddress": ruijieDhcpClientMacAddress,
       "ruijieLDhcpStartTIService": ruijieLDhcpStartTIService,
       "ruijieDhcpServerTlvNum": ruijieDhcpServerTlvNum,
       "ruijieDhcpServerTlv": ruijieDhcpServerTlv,
       "ruijieCapwapDhcpShowStats": ruijieCapwapDhcpShowStats,
       "ruijieLDhcpDiscoverPkts": ruijieLDhcpDiscoverPkts,
       "ruijieLDhcpRequestPkts": ruijieLDhcpRequestPkts,
       "ruijieLDhcpDeclinePkts": ruijieLDhcpDeclinePkts,
       "ruijieLDhcpInformPkts": ruijieLDhcpInformPkts,
       "ruijieLDhcpReleasePkts": ruijieLDhcpReleasePkts,
       "ruijieLDhcpReplyPkts": ruijieLDhcpReplyPkts,
       "ruijieLDhcpOfferPkts": ruijieLDhcpOfferPkts,
       "ruijieLDhcpAckPkts": ruijieLDhcpAckPkts,
       "ruijieLDhcpNakPkts": ruijieLDhcpNakPkts,
       "ruijieLDhcpReqTimes": ruijieLDhcpReqTimes,
       "ruijieLDhcpReqSucTimes": ruijieLDhcpReqSucTimes,
       "ruijieCapwapDhcpServerConfig": ruijieCapwapDhcpServerConfig,
       "ruijieDhcpScopeTable": ruijieDhcpScopeTable,
       "ruijieDhcpScopeEntry": ruijieDhcpScopeEntry,
       "ruijieDhcpScopeIndex": ruijieDhcpScopeIndex,
       "ruijieDhcpScopeName": ruijieDhcpScopeName,
       "ruijieDhcpScopeLeaseTime": ruijieDhcpScopeLeaseTime,
       "ruijieDhcpScopeNetwork": ruijieDhcpScopeNetwork,
       "ruijieDhcpScopeNetmask": ruijieDhcpScopeNetmask,
       "ruijieDhcpScopePoolStartAddress": ruijieDhcpScopePoolStartAddress,
       "ruijieDhcpScopePoolEndAddress": ruijieDhcpScopePoolEndAddress,
       "ruijieDhcpScopeDefaultRouterAddress1": ruijieDhcpScopeDefaultRouterAddress1,
       "ruijieDhcpScopeDefaultRouterAddress2": ruijieDhcpScopeDefaultRouterAddress2,
       "ruijieDhcpScopeDefaultRouterAddress3": ruijieDhcpScopeDefaultRouterAddress3,
       "ruijieDhcpScopeDnsDomainName": ruijieDhcpScopeDnsDomainName,
       "ruijieDhcpScopeDnsServerAddress1": ruijieDhcpScopeDnsServerAddress1,
       "ruijieDhcpScopeDnsServerAddress2": ruijieDhcpScopeDnsServerAddress2,
       "ruijieDhcpScopeDnsServerAddress3": ruijieDhcpScopeDnsServerAddress3,
       "ruijieDhcpScopeNetbiosNameServerAddress1": ruijieDhcpScopeNetbiosNameServerAddress1,
       "ruijieDhcpScopeNetbiosNameServerAddress2": ruijieDhcpScopeNetbiosNameServerAddress2,
       "ruijieDhcpScopeNetbiosNameServerAddress3": ruijieDhcpScopeNetbiosNameServerAddress3,
       "ruijieDhcpScopeState": ruijieDhcpScopeState,
       "ruijieDhcpScopeRowStatus": ruijieDhcpScopeRowStatus,
       "ruijieDhcpIPPoolUsage": ruijieDhcpIPPoolUsage,
       "ruijieDhcpoption43": ruijieDhcpoption43,
       "ruijieDhcpoption138": ruijieDhcpoption138,
       "ruijieDhcpReqtimes": ruijieDhcpReqtimes,
       "ruijieDhcpReqSuctimes": ruijieDhcpReqSuctimes,
       "ruijieDhcpTotalIPNum": ruijieDhcpTotalIPNum,
       "ruijieDhcpCurrentUsedIPNum": ruijieDhcpCurrentUsedIPNum,
       "ruijieDhcpOffertimes": ruijieDhcpOffertimes,
       "ruijieDhcpAcktimes": ruijieDhcpAcktimes,
       "ruijieDhcpServerIpVlanTable": ruijieDhcpServerIpVlanTable,
       "ruijieDhcpServerIpVlanEntry": ruijieDhcpServerIpVlanEntry,
       "ruijieDhcpServerIpVlanIndex": ruijieDhcpServerIpVlanIndex,
       "ruijieDhcpServerIpVlanOnlineUserNum": ruijieDhcpServerIpVlanOnlineUserNum,
       "ruijieCapwapDhcpRelayConfig": ruijieCapwapDhcpRelayConfig,
       "ruijieDhcpGlobalServerAddrTable": ruijieDhcpGlobalServerAddrTable,
       "ruijieDhcpGlobalServerAddrEntry": ruijieDhcpGlobalServerAddrEntry,
       "ruijieDhcpGlobalServerIndex": ruijieDhcpGlobalServerIndex,
       "ruijieDhcpGlobalServerAddress": ruijieDhcpGlobalServerAddress,
       "ruijieDhcpGlobalServerRowStatus": ruijieDhcpGlobalServerRowStatus,
       "ruijieDhcpIntfServerAddrTable": ruijieDhcpIntfServerAddrTable,
       "ruijieDhcpIntfServerAddrEntry": ruijieDhcpIntfServerAddrEntry,
       "ruijieDhcpIntfServerIndex": ruijieDhcpIntfServerIndex,
       "ruijieDhcpIntfServerAddress": ruijieDhcpIntfServerAddress,
       "ruijieDhcpIntfServerRowStatus": ruijieDhcpIntfServerRowStatus,
       "ruijieCapwapDhcpMIBConformance": ruijieCapwapDhcpMIBConformance,
       "ruijieCapwapDhcpMIBCompliances": ruijieCapwapDhcpMIBCompliances,
       "ruijieCapwapDhcpMIBCompliance": ruijieCapwapDhcpMIBCompliance,
       "ruijieCapwapDhcpMIBGroups": ruijieCapwapDhcpMIBGroups,
       "ruijieCapwapDhcpMIBGroup": ruijieCapwapDhcpMIBGroup,
       "ruijieCapwapDhcpServerConfigGroup": ruijieCapwapDhcpServerConfigGroup,
       "ruijieCapwapDhcpRelayGlobalConfigGroup": ruijieCapwapDhcpRelayGlobalConfigGroup,
       "ruijieCapwapDhcpRelayIntfConfigGroup": ruijieCapwapDhcpRelayIntfConfigGroup}
)
