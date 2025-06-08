# SNMP MIB module (SFTOS-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/SFTOS-ROUTING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:17:56 2025
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

(sFTOS,) = mibBuilder.importSymbols(
    "FORCE10-REF-MIB",
    "sFTOS")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ospfAreaEntry,
 ospfIfEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfVirtIfEntry")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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

sFTOSRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sFTOSRouting.setRevisions(
        ("2005-02-18 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SpfTimerRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_AgentSwitchArpGroup_ObjectIdentity = ObjectIdentity
agentSwitchArpGroup = _AgentSwitchArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1)
)


class _AgentSwitchArpAgeoutTime_Type(Integer32):
    """Custom type agentSwitchArpAgeoutTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 21600),
    )


_AgentSwitchArpAgeoutTime_Type.__name__ = "Integer32"
_AgentSwitchArpAgeoutTime_Object = MibScalar
agentSwitchArpAgeoutTime = _AgentSwitchArpAgeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 1),
    _AgentSwitchArpAgeoutTime_Type()
)
agentSwitchArpAgeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpAgeoutTime.setStatus("current")


class _AgentSwitchArpResponseTime_Type(Integer32):
    """Custom type agentSwitchArpResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentSwitchArpResponseTime_Type.__name__ = "Integer32"
_AgentSwitchArpResponseTime_Object = MibScalar
agentSwitchArpResponseTime = _AgentSwitchArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 2),
    _AgentSwitchArpResponseTime_Type()
)
agentSwitchArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpResponseTime.setStatus("current")


class _AgentSwitchArpMaxRetries_Type(Integer32):
    """Custom type agentSwitchArpMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AgentSwitchArpMaxRetries_Type.__name__ = "Integer32"
_AgentSwitchArpMaxRetries_Object = MibScalar
agentSwitchArpMaxRetries = _AgentSwitchArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 3),
    _AgentSwitchArpMaxRetries_Type()
)
agentSwitchArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpMaxRetries.setStatus("current")
_AgentSwitchArpCacheSize_Type = Integer32
_AgentSwitchArpCacheSize_Object = MibScalar
agentSwitchArpCacheSize = _AgentSwitchArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 4),
    _AgentSwitchArpCacheSize_Type()
)
agentSwitchArpCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpCacheSize.setStatus("current")


class _AgentSwitchArpDynamicRenew_Type(Integer32):
    """Custom type agentSwitchArpDynamicRenew based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchArpDynamicRenew_Type.__name__ = "Integer32"
_AgentSwitchArpDynamicRenew_Object = MibScalar
agentSwitchArpDynamicRenew = _AgentSwitchArpDynamicRenew_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 5),
    _AgentSwitchArpDynamicRenew_Type()
)
agentSwitchArpDynamicRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpDynamicRenew.setStatus("current")
_AgentSwitchArpTotalEntryCountCurrent_Type = Gauge32
_AgentSwitchArpTotalEntryCountCurrent_Object = MibScalar
agentSwitchArpTotalEntryCountCurrent = _AgentSwitchArpTotalEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 6),
    _AgentSwitchArpTotalEntryCountCurrent_Type()
)
agentSwitchArpTotalEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpTotalEntryCountCurrent.setStatus("current")
_AgentSwitchArpTotalEntryCountPeak_Type = Gauge32
_AgentSwitchArpTotalEntryCountPeak_Object = MibScalar
agentSwitchArpTotalEntryCountPeak = _AgentSwitchArpTotalEntryCountPeak_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 7),
    _AgentSwitchArpTotalEntryCountPeak_Type()
)
agentSwitchArpTotalEntryCountPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpTotalEntryCountPeak.setStatus("current")
_AgentSwitchArpStaticEntryCountCurrent_Type = Gauge32
_AgentSwitchArpStaticEntryCountCurrent_Object = MibScalar
agentSwitchArpStaticEntryCountCurrent = _AgentSwitchArpStaticEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 8),
    _AgentSwitchArpStaticEntryCountCurrent_Type()
)
agentSwitchArpStaticEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpStaticEntryCountCurrent.setStatus("current")
_AgentSwitchArpStaticEntryCountMax_Type = Integer32
_AgentSwitchArpStaticEntryCountMax_Object = MibScalar
agentSwitchArpStaticEntryCountMax = _AgentSwitchArpStaticEntryCountMax_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 9),
    _AgentSwitchArpStaticEntryCountMax_Type()
)
agentSwitchArpStaticEntryCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpStaticEntryCountMax.setStatus("current")
_AgentSwitchArpTable_Object = MibTable
agentSwitchArpTable = _AgentSwitchArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    agentSwitchArpTable.setStatus("current")
_AgentSwitchArpEntry_Object = MibTableRow
agentSwitchArpEntry = _AgentSwitchArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1)
)
agentSwitchArpEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentSwitchArpIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchArpEntry.setStatus("current")
_AgentSwitchArpAge_Type = TimeTicks
_AgentSwitchArpAge_Object = MibTableColumn
agentSwitchArpAge = _AgentSwitchArpAge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1, 1),
    _AgentSwitchArpAge_Type()
)
agentSwitchArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpAge.setStatus("current")
_AgentSwitchArpIpAddress_Type = IpAddress
_AgentSwitchArpIpAddress_Object = MibTableColumn
agentSwitchArpIpAddress = _AgentSwitchArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1, 2),
    _AgentSwitchArpIpAddress_Type()
)
agentSwitchArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpIpAddress.setStatus("current")
_AgentSwitchArpMacAddress_Type = PhysAddress
_AgentSwitchArpMacAddress_Object = MibTableColumn
agentSwitchArpMacAddress = _AgentSwitchArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1, 3),
    _AgentSwitchArpMacAddress_Type()
)
agentSwitchArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchArpMacAddress.setStatus("current")
_AgentSwitchArpInterface_Type = Integer32
_AgentSwitchArpInterface_Object = MibTableColumn
agentSwitchArpInterface = _AgentSwitchArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1, 4),
    _AgentSwitchArpInterface_Type()
)
agentSwitchArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpInterface.setStatus("current")


class _AgentSwitchArpType_Type(Integer32):
    """Custom type agentSwitchArpType based on Integer32"""
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
        *(("local", 1),
          ("gateway", 2),
          ("static", 3),
          ("dynamic", 4))
    )


_AgentSwitchArpType_Type.__name__ = "Integer32"
_AgentSwitchArpType_Object = MibTableColumn
agentSwitchArpType = _AgentSwitchArpType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1, 5),
    _AgentSwitchArpType_Type()
)
agentSwitchArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpType.setStatus("current")
_AgentSwitchArpStatus_Type = RowStatus
_AgentSwitchArpStatus_Object = MibTableColumn
agentSwitchArpStatus = _AgentSwitchArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 10, 1, 6),
    _AgentSwitchArpStatus_Type()
)
agentSwitchArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpStatus.setStatus("current")
_AgentSwitchLocalProxyArpTable_Object = MibTable
agentSwitchLocalProxyArpTable = _AgentSwitchLocalProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    agentSwitchLocalProxyArpTable.setStatus("current")
_AgentSwitchLocalProxyArpEntry_Object = MibTableRow
agentSwitchLocalProxyArpEntry = _AgentSwitchLocalProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 11, 1)
)
agentSwitchLocalProxyArpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchLocalProxyArpEntry.setStatus("current")


class _AgentSwitchLocalProxyArpMode_Type(Integer32):
    """Custom type agentSwitchLocalProxyArpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchLocalProxyArpMode_Type.__name__ = "Integer32"
_AgentSwitchLocalProxyArpMode_Object = MibTableColumn
agentSwitchLocalProxyArpMode = _AgentSwitchLocalProxyArpMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 1, 11, 1, 1),
    _AgentSwitchLocalProxyArpMode_Type()
)
agentSwitchLocalProxyArpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchLocalProxyArpMode.setStatus("current")
_AgentSwitchIpGroup_ObjectIdentity = ObjectIdentity
agentSwitchIpGroup = _AgentSwitchIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2)
)


class _AgentSwitchIpRoutingMode_Type(Integer32):
    """Custom type agentSwitchIpRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpRoutingMode_Type.__name__ = "Integer32"
_AgentSwitchIpRoutingMode_Object = MibScalar
agentSwitchIpRoutingMode = _AgentSwitchIpRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 1),
    _AgentSwitchIpRoutingMode_Type()
)
agentSwitchIpRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRoutingMode.setStatus("current")
_AgentSwitchIpInterfaceTable_Object = MibTable
agentSwitchIpInterfaceTable = _AgentSwitchIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceTable.setStatus("current")
_AgentSwitchIpInterfaceEntry_Object = MibTableRow
agentSwitchIpInterfaceEntry = _AgentSwitchIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1)
)
agentSwitchIpInterfaceEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceEntry.setStatus("current")
_AgentSwitchIpInterfaceIfIndex_Type = Integer32
_AgentSwitchIpInterfaceIfIndex_Object = MibTableColumn
agentSwitchIpInterfaceIfIndex = _AgentSwitchIpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 1),
    _AgentSwitchIpInterfaceIfIndex_Type()
)
agentSwitchIpInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIfIndex.setStatus("current")
_AgentSwitchIpInterfaceIpAddress_Type = IpAddress
_AgentSwitchIpInterfaceIpAddress_Object = MibTableColumn
agentSwitchIpInterfaceIpAddress = _AgentSwitchIpInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 2),
    _AgentSwitchIpInterfaceIpAddress_Type()
)
agentSwitchIpInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIpAddress.setStatus("current")
_AgentSwitchIpInterfaceNetMask_Type = IpAddress
_AgentSwitchIpInterfaceNetMask_Object = MibTableColumn
agentSwitchIpInterfaceNetMask = _AgentSwitchIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 3),
    _AgentSwitchIpInterfaceNetMask_Type()
)
agentSwitchIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceNetMask.setStatus("current")


class _AgentSwitchIpInterfaceClearIp_Type(Integer32):
    """Custom type agentSwitchIpInterfaceClearIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceClearIp_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceClearIp_Object = MibTableColumn
agentSwitchIpInterfaceClearIp = _AgentSwitchIpInterfaceClearIp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 4),
    _AgentSwitchIpInterfaceClearIp_Type()
)
agentSwitchIpInterfaceClearIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceClearIp.setStatus("current")


class _AgentSwitchIpInterfaceRoutingMode_Type(Integer32):
    """Custom type agentSwitchIpInterfaceRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceRoutingMode_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceRoutingMode_Object = MibTableColumn
agentSwitchIpInterfaceRoutingMode = _AgentSwitchIpInterfaceRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 5),
    _AgentSwitchIpInterfaceRoutingMode_Type()
)
agentSwitchIpInterfaceRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceRoutingMode.setStatus("current")


class _AgentSwitchIpInterfaceProxyARPMode_Type(Integer32):
    """Custom type agentSwitchIpInterfaceProxyARPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceProxyARPMode_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceProxyARPMode_Object = MibTableColumn
agentSwitchIpInterfaceProxyARPMode = _AgentSwitchIpInterfaceProxyARPMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 6),
    _AgentSwitchIpInterfaceProxyARPMode_Type()
)
agentSwitchIpInterfaceProxyARPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceProxyARPMode.setStatus("current")


class _AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 1500),
    )


_AgentSwitchIpInterfaceMtuValue_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceMtuValue_Object = MibTableColumn
agentSwitchIpInterfaceMtuValue = _AgentSwitchIpInterfaceMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 3, 1, 7),
    _AgentSwitchIpInterfaceMtuValue_Type()
)
agentSwitchIpInterfaceMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceMtuValue.setStatus("current")
_AgentSwitchIpRouterDiscoveryTable_Object = MibTable
agentSwitchIpRouterDiscoveryTable = _AgentSwitchIpRouterDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryTable.setStatus("current")
_AgentSwitchIpRouterDiscoveryEntry_Object = MibTableRow
agentSwitchIpRouterDiscoveryEntry = _AgentSwitchIpRouterDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1)
)
agentSwitchIpRouterDiscoveryEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentSwitchIpRouterDiscoveryIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryEntry.setStatus("current")
_AgentSwitchIpRouterDiscoveryIfIndex_Type = Integer32
_AgentSwitchIpRouterDiscoveryIfIndex_Object = MibTableColumn
agentSwitchIpRouterDiscoveryIfIndex = _AgentSwitchIpRouterDiscoveryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 1),
    _AgentSwitchIpRouterDiscoveryIfIndex_Type()
)
agentSwitchIpRouterDiscoveryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryIfIndex.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryAdvertiseMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertiseMode = _AgentSwitchIpRouterDiscoveryAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 2),
    _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type()
)
agentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertiseMode.setStatus("current")


class _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object = MibTableColumn
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval = _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 3),
    _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type()
)
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus("current")


class _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object = MibTableColumn
agentSwitchIpRouterDiscoveryMinAdvertisementInterval = _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 4),
    _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type()
)
agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 9000),
    )


_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementLifetime = _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 5),
    _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type()
)
agentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus("current")


class _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryPreferenceLevel based on Integer32"""
    defaultValue = 0


_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object = MibTableColumn
agentSwitchIpRouterDiscoveryPreferenceLevel = _AgentSwitchIpRouterDiscoveryPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 6),
    _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type()
)
agentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryPreferenceLevel.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):
    """Custom type agentSwitchIpRouterDiscoveryAdvertisementAddress based on IpAddress"""
    defaultHexValue = "E0000001"


_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__ = "IpAddress"
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementAddress = _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 4, 1, 7),
    _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type()
)
agentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus("current")
_AgentSwitchIpVlanTable_Object = MibTable
agentSwitchIpVlanTable = _AgentSwitchIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    agentSwitchIpVlanTable.setStatus("current")
_AgentSwitchIpVlanEntry_Object = MibTableRow
agentSwitchIpVlanEntry = _AgentSwitchIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 5, 1)
)
agentSwitchIpVlanEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentSwitchIpVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchIpVlanEntry.setStatus("current")
_AgentSwitchIpVlanId_Type = Integer32
_AgentSwitchIpVlanId_Object = MibTableColumn
agentSwitchIpVlanId = _AgentSwitchIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 5, 1, 1),
    _AgentSwitchIpVlanId_Type()
)
agentSwitchIpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpVlanId.setStatus("current")
_AgentSwitchIpVlanIfIndex_Type = Integer32
_AgentSwitchIpVlanIfIndex_Object = MibTableColumn
agentSwitchIpVlanIfIndex = _AgentSwitchIpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 5, 1, 2),
    _AgentSwitchIpVlanIfIndex_Type()
)
agentSwitchIpVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpVlanIfIndex.setStatus("current")
_AgentSwitchIpVlanRoutingStatus_Type = RowStatus
_AgentSwitchIpVlanRoutingStatus_Object = MibTableColumn
agentSwitchIpVlanRoutingStatus = _AgentSwitchIpVlanRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 5, 1, 3),
    _AgentSwitchIpVlanRoutingStatus_Type()
)
agentSwitchIpVlanRoutingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIpVlanRoutingStatus.setStatus("current")
_AgentSwitchSecondaryAddressTable_Object = MibTable
agentSwitchSecondaryAddressTable = _AgentSwitchSecondaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    agentSwitchSecondaryAddressTable.setStatus("current")
_AgentSwitchSecondaryAddressEntry_Object = MibTableRow
agentSwitchSecondaryAddressEntry = _AgentSwitchSecondaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 6, 1)
)
agentSwitchSecondaryAddressEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "SFTOS-ROUTING-MIB", "agentSwitchSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchSecondaryAddressEntry.setStatus("current")
_AgentSwitchSecondaryIpAddress_Type = IpAddress
_AgentSwitchSecondaryIpAddress_Object = MibTableColumn
agentSwitchSecondaryIpAddress = _AgentSwitchSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 6, 1, 1),
    _AgentSwitchSecondaryIpAddress_Type()
)
agentSwitchSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSecondaryIpAddress.setStatus("current")
_AgentSwitchSecondaryNetMask_Type = IpAddress
_AgentSwitchSecondaryNetMask_Object = MibTableColumn
agentSwitchSecondaryNetMask = _AgentSwitchSecondaryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 6, 1, 2),
    _AgentSwitchSecondaryNetMask_Type()
)
agentSwitchSecondaryNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchSecondaryNetMask.setStatus("current")
_AgentSwitchSecondaryStatus_Type = RowStatus
_AgentSwitchSecondaryStatus_Object = MibTableColumn
agentSwitchSecondaryStatus = _AgentSwitchSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 2, 6, 1, 3),
    _AgentSwitchSecondaryStatus_Type()
)
agentSwitchSecondaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchSecondaryStatus.setStatus("current")
_AgentRouterRipConfigGroup_ObjectIdentity = ObjectIdentity
agentRouterRipConfigGroup = _AgentRouterRipConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3)
)


class _AgentRouterRipAdminState_Type(Integer32):
    """Custom type agentRouterRipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentRouterRipAdminState_Type.__name__ = "Integer32"
_AgentRouterRipAdminState_Object = MibScalar
agentRouterRipAdminState = _AgentRouterRipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 1),
    _AgentRouterRipAdminState_Type()
)
agentRouterRipAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipAdminState.setStatus("current")


class _AgentRouterRipSplitHorizonMode_Type(Integer32):
    """Custom type agentRouterRipSplitHorizonMode based on Integer32"""
    defaultValue = 2

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
          ("simple", 2),
          ("poisonReverse", 3))
    )


_AgentRouterRipSplitHorizonMode_Type.__name__ = "Integer32"
_AgentRouterRipSplitHorizonMode_Object = MibScalar
agentRouterRipSplitHorizonMode = _AgentRouterRipSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 2),
    _AgentRouterRipSplitHorizonMode_Type()
)
agentRouterRipSplitHorizonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipSplitHorizonMode.setStatus("current")


class _AgentRouterRipAutoSummaryMode_Type(Integer32):
    """Custom type agentRouterRipAutoSummaryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentRouterRipAutoSummaryMode_Type.__name__ = "Integer32"
_AgentRouterRipAutoSummaryMode_Object = MibScalar
agentRouterRipAutoSummaryMode = _AgentRouterRipAutoSummaryMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 3),
    _AgentRouterRipAutoSummaryMode_Type()
)
agentRouterRipAutoSummaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipAutoSummaryMode.setStatus("current")


class _AgentRouterRipHostRoutesAcceptMode_Type(Integer32):
    """Custom type agentRouterRipHostRoutesAcceptMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentRouterRipHostRoutesAcceptMode_Type.__name__ = "Integer32"
_AgentRouterRipHostRoutesAcceptMode_Object = MibScalar
agentRouterRipHostRoutesAcceptMode = _AgentRouterRipHostRoutesAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 4),
    _AgentRouterRipHostRoutesAcceptMode_Type()
)
agentRouterRipHostRoutesAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipHostRoutesAcceptMode.setStatus("current")


class _AgentRouterRipDefaultMetric_Type(Integer32):
    """Custom type agentRouterRipDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentRouterRipDefaultMetric_Type.__name__ = "Integer32"
_AgentRouterRipDefaultMetric_Object = MibScalar
agentRouterRipDefaultMetric = _AgentRouterRipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 5),
    _AgentRouterRipDefaultMetric_Type()
)
agentRouterRipDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipDefaultMetric.setStatus("current")
_AgentRouterRipDefaultMetricConfigured_Type = TruthValue
_AgentRouterRipDefaultMetricConfigured_Object = MibScalar
agentRouterRipDefaultMetricConfigured = _AgentRouterRipDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 6),
    _AgentRouterRipDefaultMetricConfigured_Type()
)
agentRouterRipDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipDefaultMetricConfigured.setStatus("current")


class _AgentRouterRipDefaultInfoOriginate_Type(TruthValue):
    """Custom type agentRouterRipDefaultInfoOriginate based on TruthValue"""
    defaultValue = 2


_AgentRouterRipDefaultInfoOriginate_Type.__name__ = "TruthValue"
_AgentRouterRipDefaultInfoOriginate_Object = MibScalar
agentRouterRipDefaultInfoOriginate = _AgentRouterRipDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 7),
    _AgentRouterRipDefaultInfoOriginate_Type()
)
agentRouterRipDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterRipDefaultInfoOriginate.setStatus("current")
_AgentRipRouteRedistTable_Object = MibTable
agentRipRouteRedistTable = _AgentRipRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    agentRipRouteRedistTable.setStatus("current")
_AgentRipRouteRedistEntry_Object = MibTableRow
agentRipRouteRedistEntry = _AgentRipRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1)
)
agentRipRouteRedistEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentRipRouteRedistSource"),
)
if mibBuilder.loadTexts:
    agentRipRouteRedistEntry.setStatus("current")


class _AgentRipRouteRedistSource_Type(Integer32):
    """Custom type agentRipRouteRedistSource based on Integer32"""
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
        *(("connected", 1),
          ("static", 2),
          ("ospf", 3),
          ("bgp", 4))
    )


_AgentRipRouteRedistSource_Type.__name__ = "Integer32"
_AgentRipRouteRedistSource_Object = MibTableColumn
agentRipRouteRedistSource = _AgentRipRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 1),
    _AgentRipRouteRedistSource_Type()
)
agentRipRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRipRouteRedistSource.setStatus("current")


class _AgentRipRouteRedistMode_Type(Integer32):
    """Custom type agentRipRouteRedistMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentRipRouteRedistMode_Type.__name__ = "Integer32"
_AgentRipRouteRedistMode_Object = MibTableColumn
agentRipRouteRedistMode = _AgentRipRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 2),
    _AgentRipRouteRedistMode_Type()
)
agentRipRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMode.setStatus("current")


class _AgentRipRouteRedistMetric_Type(Integer32):
    """Custom type agentRipRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentRipRouteRedistMetric_Type.__name__ = "Integer32"
_AgentRipRouteRedistMetric_Object = MibTableColumn
agentRipRouteRedistMetric = _AgentRipRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 3),
    _AgentRipRouteRedistMetric_Type()
)
agentRipRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMetric.setStatus("current")
_AgentRipRouteRedistMetricConfigured_Type = TruthValue
_AgentRipRouteRedistMetricConfigured_Object = MibTableColumn
agentRipRouteRedistMetricConfigured = _AgentRipRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 4),
    _AgentRipRouteRedistMetricConfigured_Type()
)
agentRipRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMetricConfigured.setStatus("current")


class _AgentRipRouteRedistMatchInternal_Type(Integer32):
    """Custom type agentRipRouteRedistMatchInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_AgentRipRouteRedistMatchInternal_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchInternal_Object = MibTableColumn
agentRipRouteRedistMatchInternal = _AgentRipRouteRedistMatchInternal_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 5),
    _AgentRipRouteRedistMatchInternal_Type()
)
agentRipRouteRedistMatchInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchInternal.setStatus("current")


class _AgentRipRouteRedistMatchExternal1_Type(Integer32):
    """Custom type agentRipRouteRedistMatchExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_AgentRipRouteRedistMatchExternal1_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchExternal1_Object = MibTableColumn
agentRipRouteRedistMatchExternal1 = _AgentRipRouteRedistMatchExternal1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 6),
    _AgentRipRouteRedistMatchExternal1_Type()
)
agentRipRouteRedistMatchExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchExternal1.setStatus("current")


class _AgentRipRouteRedistMatchExternal2_Type(Integer32):
    """Custom type agentRipRouteRedistMatchExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_AgentRipRouteRedistMatchExternal2_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchExternal2_Object = MibTableColumn
agentRipRouteRedistMatchExternal2 = _AgentRipRouteRedistMatchExternal2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 7),
    _AgentRipRouteRedistMatchExternal2_Type()
)
agentRipRouteRedistMatchExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchExternal2.setStatus("current")


class _AgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):
    """Custom type agentRipRouteRedistMatchNSSAExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_AgentRipRouteRedistMatchNSSAExternal1_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchNSSAExternal1_Object = MibTableColumn
agentRipRouteRedistMatchNSSAExternal1 = _AgentRipRouteRedistMatchNSSAExternal1_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 8),
    _AgentRipRouteRedistMatchNSSAExternal1_Type()
)
agentRipRouteRedistMatchNSSAExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchNSSAExternal1.setStatus("current")


class _AgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):
    """Custom type agentRipRouteRedistMatchNSSAExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_AgentRipRouteRedistMatchNSSAExternal2_Type.__name__ = "Integer32"
_AgentRipRouteRedistMatchNSSAExternal2_Object = MibTableColumn
agentRipRouteRedistMatchNSSAExternal2 = _AgentRipRouteRedistMatchNSSAExternal2_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 9),
    _AgentRipRouteRedistMatchNSSAExternal2_Type()
)
agentRipRouteRedistMatchNSSAExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistMatchNSSAExternal2.setStatus("current")


class _AgentRipRouteRedistDistList_Type(Unsigned32):
    """Custom type agentRipRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_AgentRipRouteRedistDistList_Type.__name__ = "Unsigned32"
_AgentRipRouteRedistDistList_Object = MibTableColumn
agentRipRouteRedistDistList = _AgentRipRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 10),
    _AgentRipRouteRedistDistList_Type()
)
agentRipRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistDistList.setStatus("current")
_AgentRipRouteRedistDistListConfigured_Type = TruthValue
_AgentRipRouteRedistDistListConfigured_Object = MibTableColumn
agentRipRouteRedistDistListConfigured = _AgentRipRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 8, 1, 11),
    _AgentRipRouteRedistDistListConfigured_Type()
)
agentRipRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRipRouteRedistDistListConfigured.setStatus("current")
_AgentRip2IfConfTable_Object = MibTable
agentRip2IfConfTable = _AgentRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    agentRip2IfConfTable.setStatus("current")
_AgentRip2IfConfEntry_Object = MibTableRow
agentRip2IfConfEntry = _AgentRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    agentRip2IfConfEntry.setStatus("current")


class _AgentRip2IfConfAuthKeyId_Type(Integer32):
    """Custom type agentRip2IfConfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentRip2IfConfAuthKeyId_Type.__name__ = "Integer32"
_AgentRip2IfConfAuthKeyId_Object = MibTableColumn
agentRip2IfConfAuthKeyId = _AgentRip2IfConfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 3, 9, 1, 1),
    _AgentRip2IfConfAuthKeyId_Type()
)
agentRip2IfConfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRip2IfConfAuthKeyId.setStatus("current")
_AgentRouterOspfConfigGroup_ObjectIdentity = ObjectIdentity
agentRouterOspfConfigGroup = _AgentRouterOspfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4)
)


class _AgentOspfDefaultMetric_Type(Integer32):
    """Custom type agentOspfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_AgentOspfDefaultMetric_Type.__name__ = "Integer32"
_AgentOspfDefaultMetric_Object = MibScalar
agentOspfDefaultMetric = _AgentOspfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 1),
    _AgentOspfDefaultMetric_Type()
)
agentOspfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultMetric.setStatus("current")
_AgentOspfDefaultMetricConfigured_Type = TruthValue
_AgentOspfDefaultMetricConfigured_Object = MibScalar
agentOspfDefaultMetricConfigured = _AgentOspfDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 2),
    _AgentOspfDefaultMetricConfigured_Type()
)
agentOspfDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultMetricConfigured.setStatus("current")


class _AgentOspfDefaultInfoOriginate_Type(TruthValue):
    """Custom type agentOspfDefaultInfoOriginate based on TruthValue"""
    defaultValue = 2


_AgentOspfDefaultInfoOriginate_Type.__name__ = "TruthValue"
_AgentOspfDefaultInfoOriginate_Object = MibScalar
agentOspfDefaultInfoOriginate = _AgentOspfDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 3),
    _AgentOspfDefaultInfoOriginate_Type()
)
agentOspfDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginate.setStatus("current")


class _AgentOspfDefaultInfoOriginateAlways_Type(TruthValue):
    """Custom type agentOspfDefaultInfoOriginateAlways based on TruthValue"""
    defaultValue = 2


_AgentOspfDefaultInfoOriginateAlways_Type.__name__ = "TruthValue"
_AgentOspfDefaultInfoOriginateAlways_Object = MibScalar
agentOspfDefaultInfoOriginateAlways = _AgentOspfDefaultInfoOriginateAlways_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 4),
    _AgentOspfDefaultInfoOriginateAlways_Type()
)
agentOspfDefaultInfoOriginateAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateAlways.setStatus("current")


class _AgentOspfDefaultInfoOriginateMetric_Type(Integer32):
    """Custom type agentOspfDefaultInfoOriginateMetric based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_AgentOspfDefaultInfoOriginateMetric_Type.__name__ = "Integer32"
_AgentOspfDefaultInfoOriginateMetric_Object = MibScalar
agentOspfDefaultInfoOriginateMetric = _AgentOspfDefaultInfoOriginateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 5),
    _AgentOspfDefaultInfoOriginateMetric_Type()
)
agentOspfDefaultInfoOriginateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateMetric.setStatus("current")
_AgentOspfDefaultInfoOriginateMetricConfigured_Type = TruthValue
_AgentOspfDefaultInfoOriginateMetricConfigured_Object = MibScalar
agentOspfDefaultInfoOriginateMetricConfigured = _AgentOspfDefaultInfoOriginateMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 6),
    _AgentOspfDefaultInfoOriginateMetricConfigured_Type()
)
agentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateMetricConfigured.setStatus("current")


class _AgentOspfDefaultInfoOriginateMetricType_Type(Integer32):
    """Custom type agentOspfDefaultInfoOriginateMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_AgentOspfDefaultInfoOriginateMetricType_Type.__name__ = "Integer32"
_AgentOspfDefaultInfoOriginateMetricType_Object = MibScalar
agentOspfDefaultInfoOriginateMetricType = _AgentOspfDefaultInfoOriginateMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 7),
    _AgentOspfDefaultInfoOriginateMetricType_Type()
)
agentOspfDefaultInfoOriginateMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfDefaultInfoOriginateMetricType.setStatus("current")
_AgentOspfRouteRedistTable_Object = MibTable
agentOspfRouteRedistTable = _AgentOspfRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8)
)
if mibBuilder.loadTexts:
    agentOspfRouteRedistTable.setStatus("current")
_AgentOspfRouteRedistEntry_Object = MibTableRow
agentOspfRouteRedistEntry = _AgentOspfRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1)
)
agentOspfRouteRedistEntry.setIndexNames(
    (0, "SFTOS-ROUTING-MIB", "agentOspfRouteRedistSource"),
)
if mibBuilder.loadTexts:
    agentOspfRouteRedistEntry.setStatus("current")


class _AgentOspfRouteRedistSource_Type(Integer32):
    """Custom type agentOspfRouteRedistSource based on Integer32"""
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
        *(("connected", 1),
          ("static", 2),
          ("rip", 3),
          ("bgp", 4))
    )


_AgentOspfRouteRedistSource_Type.__name__ = "Integer32"
_AgentOspfRouteRedistSource_Object = MibTableColumn
agentOspfRouteRedistSource = _AgentOspfRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 1),
    _AgentOspfRouteRedistSource_Type()
)
agentOspfRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfRouteRedistSource.setStatus("current")


class _AgentOspfRouteRedistMode_Type(Integer32):
    """Custom type agentOspfRouteRedistMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentOspfRouteRedistMode_Type.__name__ = "Integer32"
_AgentOspfRouteRedistMode_Object = MibTableColumn
agentOspfRouteRedistMode = _AgentOspfRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 2),
    _AgentOspfRouteRedistMode_Type()
)
agentOspfRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMode.setStatus("current")


class _AgentOspfRouteRedistMetric_Type(Integer32):
    """Custom type agentOspfRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_AgentOspfRouteRedistMetric_Type.__name__ = "Integer32"
_AgentOspfRouteRedistMetric_Object = MibTableColumn
agentOspfRouteRedistMetric = _AgentOspfRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 3),
    _AgentOspfRouteRedistMetric_Type()
)
agentOspfRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMetric.setStatus("current")
_AgentOspfRouteRedistMetricConfigured_Type = TruthValue
_AgentOspfRouteRedistMetricConfigured_Object = MibTableColumn
agentOspfRouteRedistMetricConfigured = _AgentOspfRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 4),
    _AgentOspfRouteRedistMetricConfigured_Type()
)
agentOspfRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMetricConfigured.setStatus("current")


class _AgentOspfRouteRedistMetricType_Type(Integer32):
    """Custom type agentOspfRouteRedistMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_AgentOspfRouteRedistMetricType_Type.__name__ = "Integer32"
_AgentOspfRouteRedistMetricType_Object = MibTableColumn
agentOspfRouteRedistMetricType = _AgentOspfRouteRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 5),
    _AgentOspfRouteRedistMetricType_Type()
)
agentOspfRouteRedistMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistMetricType.setStatus("current")


class _AgentOspfRouteRedistTag_Type(Unsigned32):
    """Custom type agentOspfRouteRedistTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AgentOspfRouteRedistTag_Type.__name__ = "Unsigned32"
_AgentOspfRouteRedistTag_Object = MibTableColumn
agentOspfRouteRedistTag = _AgentOspfRouteRedistTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 6),
    _AgentOspfRouteRedistTag_Type()
)
agentOspfRouteRedistTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistTag.setStatus("current")


class _AgentOspfRouteRedistSubnets_Type(TruthValue):
    """Custom type agentOspfRouteRedistSubnets based on TruthValue"""
    defaultValue = 2


_AgentOspfRouteRedistSubnets_Type.__name__ = "TruthValue"
_AgentOspfRouteRedistSubnets_Object = MibTableColumn
agentOspfRouteRedistSubnets = _AgentOspfRouteRedistSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 7),
    _AgentOspfRouteRedistSubnets_Type()
)
agentOspfRouteRedistSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistSubnets.setStatus("current")


class _AgentOspfRouteRedistDistList_Type(Unsigned32):
    """Custom type agentOspfRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_AgentOspfRouteRedistDistList_Type.__name__ = "Unsigned32"
_AgentOspfRouteRedistDistList_Object = MibTableColumn
agentOspfRouteRedistDistList = _AgentOspfRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 8),
    _AgentOspfRouteRedistDistList_Type()
)
agentOspfRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistDistList.setStatus("current")
_AgentOspfRouteRedistDistListConfigured_Type = TruthValue
_AgentOspfRouteRedistDistListConfigured_Object = MibTableColumn
agentOspfRouteRedistDistListConfigured = _AgentOspfRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 8, 1, 9),
    _AgentOspfRouteRedistDistListConfigured_Type()
)
agentOspfRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfRouteRedistDistListConfigured.setStatus("current")
_AgentOspfIfTable_Object = MibTable
agentOspfIfTable = _AgentOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 9)
)
if mibBuilder.loadTexts:
    agentOspfIfTable.setStatus("current")
_AgentOspfIfEntry_Object = MibTableRow
agentOspfIfEntry = _AgentOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    agentOspfIfEntry.setStatus("current")


class _AgentOspfIfAuthKeyId_Type(Integer32):
    """Custom type agentOspfIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOspfIfAuthKeyId_Type.__name__ = "Integer32"
_AgentOspfIfAuthKeyId_Object = MibTableColumn
agentOspfIfAuthKeyId = _AgentOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 9, 1, 1),
    _AgentOspfIfAuthKeyId_Type()
)
agentOspfIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOspfIfAuthKeyId.setStatus("current")


class _AgentOspfIfIpMtuIgnoreFlag_Type(Integer32):
    """Custom type agentOspfIfIpMtuIgnoreFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentOspfIfIpMtuIgnoreFlag_Type.__name__ = "Integer32"
_AgentOspfIfIpMtuIgnoreFlag_Object = MibTableColumn
agentOspfIfIpMtuIgnoreFlag = _AgentOspfIfIpMtuIgnoreFlag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 9, 1, 2),
    _AgentOspfIfIpMtuIgnoreFlag_Type()
)
agentOspfIfIpMtuIgnoreFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfIfIpMtuIgnoreFlag.setStatus("current")
_AgentOspfVirtIfTable_Object = MibTable
agentOspfVirtIfTable = _AgentOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 10)
)
if mibBuilder.loadTexts:
    agentOspfVirtIfTable.setStatus("current")
_AgentOspfVirtIfEntry_Object = MibTableRow
agentOspfVirtIfEntry = _AgentOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 10, 1)
)
if mibBuilder.loadTexts:
    agentOspfVirtIfEntry.setStatus("current")


class _AgentOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type agentOspfVirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_AgentOspfVirtIfAuthKeyId_Object = MibTableColumn
agentOspfVirtIfAuthKeyId = _AgentOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 10, 1, 1),
    _AgentOspfVirtIfAuthKeyId_Type()
)
agentOspfVirtIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOspfVirtIfAuthKeyId.setStatus("current")


class _AgentRouterOspfRFC1583CompatibilityMode_Type(Integer32):
    """Custom type agentRouterOspfRFC1583CompatibilityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentRouterOspfRFC1583CompatibilityMode_Type.__name__ = "Integer32"
_AgentRouterOspfRFC1583CompatibilityMode_Object = MibScalar
agentRouterOspfRFC1583CompatibilityMode = _AgentRouterOspfRFC1583CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 11),
    _AgentRouterOspfRFC1583CompatibilityMode_Type()
)
agentRouterOspfRFC1583CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterOspfRFC1583CompatibilityMode.setStatus("current")


class _AgentOspfSpfDelayTime_Type(SpfTimerRange):
    """Custom type agentOspfSpfDelayTime based on SpfTimerRange"""
    defaultValue = 5


_AgentOspfSpfDelayTime_Type.__name__ = "SpfTimerRange"
_AgentOspfSpfDelayTime_Object = MibScalar
agentOspfSpfDelayTime = _AgentOspfSpfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 12),
    _AgentOspfSpfDelayTime_Type()
)
agentOspfSpfDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfSpfDelayTime.setStatus("current")


class _AgentOspfSpfHoldTime_Type(SpfTimerRange):
    """Custom type agentOspfSpfHoldTime based on SpfTimerRange"""
    defaultValue = 10


_AgentOspfSpfHoldTime_Type.__name__ = "SpfTimerRange"
_AgentOspfSpfHoldTime_Object = MibScalar
agentOspfSpfHoldTime = _AgentOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 4, 13),
    _AgentOspfSpfHoldTime_Type()
)
agentOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOspfSpfHoldTime.setStatus("current")
_AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroupLayer3 = _AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 5)
)


class _AgentSnmpVRRPNewMasterTrapFlag_Type(Integer32):
    """Custom type agentSnmpVRRPNewMasterTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSnmpVRRPNewMasterTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpVRRPNewMasterTrapFlag_Object = MibScalar
agentSnmpVRRPNewMasterTrapFlag = _AgentSnmpVRRPNewMasterTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 5, 1),
    _AgentSnmpVRRPNewMasterTrapFlag_Type()
)
agentSnmpVRRPNewMasterTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVRRPNewMasterTrapFlag.setStatus("current")


class _AgentSnmpVRRPAuthFailureTrapFlag_Type(Integer32):
    """Custom type agentSnmpVRRPAuthFailureTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSnmpVRRPAuthFailureTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpVRRPAuthFailureTrapFlag_Object = MibScalar
agentSnmpVRRPAuthFailureTrapFlag = _AgentSnmpVRRPAuthFailureTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 5, 2),
    _AgentSnmpVRRPAuthFailureTrapFlag_Type()
)
agentSnmpVRRPAuthFailureTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVRRPAuthFailureTrapFlag.setStatus("current")
_AgentBootpDhcpRelayGroup_ObjectIdentity = ObjectIdentity
agentBootpDhcpRelayGroup = _AgentBootpDhcpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6)
)


class _AgentBootpDhcpRelayMaxHopCount_Type(Integer32):
    """Custom type agentBootpDhcpRelayMaxHopCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentBootpDhcpRelayMaxHopCount_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayMaxHopCount_Object = MibScalar
agentBootpDhcpRelayMaxHopCount = _AgentBootpDhcpRelayMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 1),
    _AgentBootpDhcpRelayMaxHopCount_Type()
)
agentBootpDhcpRelayMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayMaxHopCount.setStatus("current")
_AgentBootpDhcpRelayForwardingIp_Type = IpAddress
_AgentBootpDhcpRelayForwardingIp_Object = MibScalar
agentBootpDhcpRelayForwardingIp = _AgentBootpDhcpRelayForwardingIp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 2),
    _AgentBootpDhcpRelayForwardingIp_Type()
)
agentBootpDhcpRelayForwardingIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayForwardingIp.setStatus("current")


class _AgentBootpDhcpRelayForwardMode_Type(Integer32):
    """Custom type agentBootpDhcpRelayForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentBootpDhcpRelayForwardMode_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayForwardMode_Object = MibScalar
agentBootpDhcpRelayForwardMode = _AgentBootpDhcpRelayForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 3),
    _AgentBootpDhcpRelayForwardMode_Type()
)
agentBootpDhcpRelayForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayForwardMode.setStatus("current")


class _AgentBootpDhcpRelayMinWaitTime_Type(Integer32):
    """Custom type agentBootpDhcpRelayMinWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentBootpDhcpRelayMinWaitTime_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayMinWaitTime_Object = MibScalar
agentBootpDhcpRelayMinWaitTime = _AgentBootpDhcpRelayMinWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 4),
    _AgentBootpDhcpRelayMinWaitTime_Type()
)
agentBootpDhcpRelayMinWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayMinWaitTime.setStatus("current")


class _AgentBootpDhcpRelayCircuitIdOptionMode_Type(Integer32):
    """Custom type agentBootpDhcpRelayCircuitIdOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentBootpDhcpRelayCircuitIdOptionMode_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayCircuitIdOptionMode_Object = MibScalar
agentBootpDhcpRelayCircuitIdOptionMode = _AgentBootpDhcpRelayCircuitIdOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 5),
    _AgentBootpDhcpRelayCircuitIdOptionMode_Type()
)
agentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayCircuitIdOptionMode.setStatus("current")
_AgentBootpDhcpRelayNumOfRequestsReceived_Type = Integer32
_AgentBootpDhcpRelayNumOfRequestsReceived_Object = MibScalar
agentBootpDhcpRelayNumOfRequestsReceived = _AgentBootpDhcpRelayNumOfRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 6),
    _AgentBootpDhcpRelayNumOfRequestsReceived_Type()
)
agentBootpDhcpRelayNumOfRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfRequestsReceived.setStatus("current")
_AgentBootpDhcpRelayNumOfRequestsForwarded_Type = Integer32
_AgentBootpDhcpRelayNumOfRequestsForwarded_Object = MibScalar
agentBootpDhcpRelayNumOfRequestsForwarded = _AgentBootpDhcpRelayNumOfRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 7),
    _AgentBootpDhcpRelayNumOfRequestsForwarded_Type()
)
agentBootpDhcpRelayNumOfRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfRequestsForwarded.setStatus("current")
_AgentBootpDhcpRelayNumOfDiscards_Type = Integer32
_AgentBootpDhcpRelayNumOfDiscards_Object = MibScalar
agentBootpDhcpRelayNumOfDiscards = _AgentBootpDhcpRelayNumOfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 6, 8),
    _AgentBootpDhcpRelayNumOfDiscards_Type()
)
agentBootpDhcpRelayNumOfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfDiscards.setStatus("current")
_AgentECMPGroup_ObjectIdentity = ObjectIdentity
agentECMPGroup = _AgentECMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 7)
)


class _AgentECMPOspfMaxPaths_Type(Integer32):
    """Custom type agentECMPOspfMaxPaths based on Integer32"""
    defaultValue = 4


_AgentECMPOspfMaxPaths_Type.__name__ = "Integer32"
_AgentECMPOspfMaxPaths_Object = MibScalar
agentECMPOspfMaxPaths = _AgentECMPOspfMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 7, 1),
    _AgentECMPOspfMaxPaths_Type()
)
agentECMPOspfMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentECMPOspfMaxPaths.setStatus("current")
_AgentRouterVrrpConfigGroup_ObjectIdentity = ObjectIdentity
agentRouterVrrpConfigGroup = _AgentRouterVrrpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 8)
)


class _AgentRouterVrrpAdminState_Type(Integer32):
    """Custom type agentRouterVrrpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentRouterVrrpAdminState_Type.__name__ = "Integer32"
_AgentRouterVrrpAdminState_Object = MibScalar
agentRouterVrrpAdminState = _AgentRouterVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 2, 8, 1),
    _AgentRouterVrrpAdminState_Type()
)
agentRouterVrrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRouterVrrpAdminState.setStatus("current")
rip2IfConfEntry.registerAugmentions(
    ("SFTOS-ROUTING-MIB",
     "agentRip2IfConfEntry")
)
agentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("SFTOS-ROUTING-MIB",
     "agentOspfIfEntry")
)
agentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("SFTOS-ROUTING-MIB",
     "agentOspfVirtIfEntry")
)
agentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFTOS-ROUTING-MIB",
    **{"SpfTimerRange": SpfTimerRange,
       "sFTOSRouting": sFTOSRouting,
       "agentSwitchArpGroup": agentSwitchArpGroup,
       "agentSwitchArpAgeoutTime": agentSwitchArpAgeoutTime,
       "agentSwitchArpResponseTime": agentSwitchArpResponseTime,
       "agentSwitchArpMaxRetries": agentSwitchArpMaxRetries,
       "agentSwitchArpCacheSize": agentSwitchArpCacheSize,
       "agentSwitchArpDynamicRenew": agentSwitchArpDynamicRenew,
       "agentSwitchArpTotalEntryCountCurrent": agentSwitchArpTotalEntryCountCurrent,
       "agentSwitchArpTotalEntryCountPeak": agentSwitchArpTotalEntryCountPeak,
       "agentSwitchArpStaticEntryCountCurrent": agentSwitchArpStaticEntryCountCurrent,
       "agentSwitchArpStaticEntryCountMax": agentSwitchArpStaticEntryCountMax,
       "agentSwitchArpTable": agentSwitchArpTable,
       "agentSwitchArpEntry": agentSwitchArpEntry,
       "agentSwitchArpAge": agentSwitchArpAge,
       "agentSwitchArpIpAddress": agentSwitchArpIpAddress,
       "agentSwitchArpMacAddress": agentSwitchArpMacAddress,
       "agentSwitchArpInterface": agentSwitchArpInterface,
       "agentSwitchArpType": agentSwitchArpType,
       "agentSwitchArpStatus": agentSwitchArpStatus,
       "agentSwitchLocalProxyArpTable": agentSwitchLocalProxyArpTable,
       "agentSwitchLocalProxyArpEntry": agentSwitchLocalProxyArpEntry,
       "agentSwitchLocalProxyArpMode": agentSwitchLocalProxyArpMode,
       "agentSwitchIpGroup": agentSwitchIpGroup,
       "agentSwitchIpRoutingMode": agentSwitchIpRoutingMode,
       "agentSwitchIpInterfaceTable": agentSwitchIpInterfaceTable,
       "agentSwitchIpInterfaceEntry": agentSwitchIpInterfaceEntry,
       "agentSwitchIpInterfaceIfIndex": agentSwitchIpInterfaceIfIndex,
       "agentSwitchIpInterfaceIpAddress": agentSwitchIpInterfaceIpAddress,
       "agentSwitchIpInterfaceNetMask": agentSwitchIpInterfaceNetMask,
       "agentSwitchIpInterfaceClearIp": agentSwitchIpInterfaceClearIp,
       "agentSwitchIpInterfaceRoutingMode": agentSwitchIpInterfaceRoutingMode,
       "agentSwitchIpInterfaceProxyARPMode": agentSwitchIpInterfaceProxyARPMode,
       "agentSwitchIpInterfaceMtuValue": agentSwitchIpInterfaceMtuValue,
       "agentSwitchIpRouterDiscoveryTable": agentSwitchIpRouterDiscoveryTable,
       "agentSwitchIpRouterDiscoveryEntry": agentSwitchIpRouterDiscoveryEntry,
       "agentSwitchIpRouterDiscoveryIfIndex": agentSwitchIpRouterDiscoveryIfIndex,
       "agentSwitchIpRouterDiscoveryAdvertiseMode": agentSwitchIpRouterDiscoveryAdvertiseMode,
       "agentSwitchIpRouterDiscoveryMaxAdvertisementInterval": agentSwitchIpRouterDiscoveryMaxAdvertisementInterval,
       "agentSwitchIpRouterDiscoveryMinAdvertisementInterval": agentSwitchIpRouterDiscoveryMinAdvertisementInterval,
       "agentSwitchIpRouterDiscoveryAdvertisementLifetime": agentSwitchIpRouterDiscoveryAdvertisementLifetime,
       "agentSwitchIpRouterDiscoveryPreferenceLevel": agentSwitchIpRouterDiscoveryPreferenceLevel,
       "agentSwitchIpRouterDiscoveryAdvertisementAddress": agentSwitchIpRouterDiscoveryAdvertisementAddress,
       "agentSwitchIpVlanTable": agentSwitchIpVlanTable,
       "agentSwitchIpVlanEntry": agentSwitchIpVlanEntry,
       "agentSwitchIpVlanId": agentSwitchIpVlanId,
       "agentSwitchIpVlanIfIndex": agentSwitchIpVlanIfIndex,
       "agentSwitchIpVlanRoutingStatus": agentSwitchIpVlanRoutingStatus,
       "agentSwitchSecondaryAddressTable": agentSwitchSecondaryAddressTable,
       "agentSwitchSecondaryAddressEntry": agentSwitchSecondaryAddressEntry,
       "agentSwitchSecondaryIpAddress": agentSwitchSecondaryIpAddress,
       "agentSwitchSecondaryNetMask": agentSwitchSecondaryNetMask,
       "agentSwitchSecondaryStatus": agentSwitchSecondaryStatus,
       "agentRouterRipConfigGroup": agentRouterRipConfigGroup,
       "agentRouterRipAdminState": agentRouterRipAdminState,
       "agentRouterRipSplitHorizonMode": agentRouterRipSplitHorizonMode,
       "agentRouterRipAutoSummaryMode": agentRouterRipAutoSummaryMode,
       "agentRouterRipHostRoutesAcceptMode": agentRouterRipHostRoutesAcceptMode,
       "agentRouterRipDefaultMetric": agentRouterRipDefaultMetric,
       "agentRouterRipDefaultMetricConfigured": agentRouterRipDefaultMetricConfigured,
       "agentRouterRipDefaultInfoOriginate": agentRouterRipDefaultInfoOriginate,
       "agentRipRouteRedistTable": agentRipRouteRedistTable,
       "agentRipRouteRedistEntry": agentRipRouteRedistEntry,
       "agentRipRouteRedistSource": agentRipRouteRedistSource,
       "agentRipRouteRedistMode": agentRipRouteRedistMode,
       "agentRipRouteRedistMetric": agentRipRouteRedistMetric,
       "agentRipRouteRedistMetricConfigured": agentRipRouteRedistMetricConfigured,
       "agentRipRouteRedistMatchInternal": agentRipRouteRedistMatchInternal,
       "agentRipRouteRedistMatchExternal1": agentRipRouteRedistMatchExternal1,
       "agentRipRouteRedistMatchExternal2": agentRipRouteRedistMatchExternal2,
       "agentRipRouteRedistMatchNSSAExternal1": agentRipRouteRedistMatchNSSAExternal1,
       "agentRipRouteRedistMatchNSSAExternal2": agentRipRouteRedistMatchNSSAExternal2,
       "agentRipRouteRedistDistList": agentRipRouteRedistDistList,
       "agentRipRouteRedistDistListConfigured": agentRipRouteRedistDistListConfigured,
       "agentRip2IfConfTable": agentRip2IfConfTable,
       "agentRip2IfConfEntry": agentRip2IfConfEntry,
       "agentRip2IfConfAuthKeyId": agentRip2IfConfAuthKeyId,
       "agentRouterOspfConfigGroup": agentRouterOspfConfigGroup,
       "agentOspfDefaultMetric": agentOspfDefaultMetric,
       "agentOspfDefaultMetricConfigured": agentOspfDefaultMetricConfigured,
       "agentOspfDefaultInfoOriginate": agentOspfDefaultInfoOriginate,
       "agentOspfDefaultInfoOriginateAlways": agentOspfDefaultInfoOriginateAlways,
       "agentOspfDefaultInfoOriginateMetric": agentOspfDefaultInfoOriginateMetric,
       "agentOspfDefaultInfoOriginateMetricConfigured": agentOspfDefaultInfoOriginateMetricConfigured,
       "agentOspfDefaultInfoOriginateMetricType": agentOspfDefaultInfoOriginateMetricType,
       "agentOspfRouteRedistTable": agentOspfRouteRedistTable,
       "agentOspfRouteRedistEntry": agentOspfRouteRedistEntry,
       "agentOspfRouteRedistSource": agentOspfRouteRedistSource,
       "agentOspfRouteRedistMode": agentOspfRouteRedistMode,
       "agentOspfRouteRedistMetric": agentOspfRouteRedistMetric,
       "agentOspfRouteRedistMetricConfigured": agentOspfRouteRedistMetricConfigured,
       "agentOspfRouteRedistMetricType": agentOspfRouteRedistMetricType,
       "agentOspfRouteRedistTag": agentOspfRouteRedistTag,
       "agentOspfRouteRedistSubnets": agentOspfRouteRedistSubnets,
       "agentOspfRouteRedistDistList": agentOspfRouteRedistDistList,
       "agentOspfRouteRedistDistListConfigured": agentOspfRouteRedistDistListConfigured,
       "agentOspfIfTable": agentOspfIfTable,
       "agentOspfIfEntry": agentOspfIfEntry,
       "agentOspfIfAuthKeyId": agentOspfIfAuthKeyId,
       "agentOspfIfIpMtuIgnoreFlag": agentOspfIfIpMtuIgnoreFlag,
       "agentOspfVirtIfTable": agentOspfVirtIfTable,
       "agentOspfVirtIfEntry": agentOspfVirtIfEntry,
       "agentOspfVirtIfAuthKeyId": agentOspfVirtIfAuthKeyId,
       "agentRouterOspfRFC1583CompatibilityMode": agentRouterOspfRFC1583CompatibilityMode,
       "agentOspfSpfDelayTime": agentOspfSpfDelayTime,
       "agentOspfSpfHoldTime": agentOspfSpfHoldTime,
       "agentSnmpTrapFlagsConfigGroupLayer3": agentSnmpTrapFlagsConfigGroupLayer3,
       "agentSnmpVRRPNewMasterTrapFlag": agentSnmpVRRPNewMasterTrapFlag,
       "agentSnmpVRRPAuthFailureTrapFlag": agentSnmpVRRPAuthFailureTrapFlag,
       "agentBootpDhcpRelayGroup": agentBootpDhcpRelayGroup,
       "agentBootpDhcpRelayMaxHopCount": agentBootpDhcpRelayMaxHopCount,
       "agentBootpDhcpRelayForwardingIp": agentBootpDhcpRelayForwardingIp,
       "agentBootpDhcpRelayForwardMode": agentBootpDhcpRelayForwardMode,
       "agentBootpDhcpRelayMinWaitTime": agentBootpDhcpRelayMinWaitTime,
       "agentBootpDhcpRelayCircuitIdOptionMode": agentBootpDhcpRelayCircuitIdOptionMode,
       "agentBootpDhcpRelayNumOfRequestsReceived": agentBootpDhcpRelayNumOfRequestsReceived,
       "agentBootpDhcpRelayNumOfRequestsForwarded": agentBootpDhcpRelayNumOfRequestsForwarded,
       "agentBootpDhcpRelayNumOfDiscards": agentBootpDhcpRelayNumOfDiscards,
       "agentECMPGroup": agentECMPGroup,
       "agentECMPOspfMaxPaths": agentECMPOspfMaxPaths,
       "agentRouterVrrpConfigGroup": agentRouterVrrpConfigGroup,
       "agentRouterVrrpAdminState": agentRouterVrrpAdminState}
)
