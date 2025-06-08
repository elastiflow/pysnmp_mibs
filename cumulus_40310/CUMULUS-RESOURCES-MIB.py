# SNMP MIB module (CUMULUS-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cumulus_40310/CUMULUS-RESOURCES-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:08:37 2025
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

(cumulusMib,) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "cumulusMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

resourceUtilization = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1)
)
if mibBuilder.loadTexts:
    resourceUtilization.setRevisions(
        ("2016-06-06 00:00",
         "2015-10-26 00:00",
         "2012-07-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L3Tables_ObjectIdentity = ObjectIdentity
l3Tables = _L3Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1)
)
_L3HostTableCurrentEntries_Type = Integer32
_L3HostTableCurrentEntries_Object = MibScalar
l3HostTableCurrentEntries = _L3HostTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 1),
    _L3HostTableCurrentEntries_Type()
)
l3HostTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3HostTableCurrentEntries.setStatus("current")
_L3HostTableMaxEntries_Type = Integer32
_L3HostTableMaxEntries_Object = MibScalar
l3HostTableMaxEntries = _L3HostTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 2),
    _L3HostTableMaxEntries_Type()
)
l3HostTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3HostTableMaxEntries.setStatus("current")
_L3RoutingTableCurrentEntries_Type = Integer32
_L3RoutingTableCurrentEntries_Object = MibScalar
l3RoutingTableCurrentEntries = _L3RoutingTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 3),
    _L3RoutingTableCurrentEntries_Type()
)
l3RoutingTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3RoutingTableCurrentEntries.setStatus("current")
_L3RoutingTableMaxEntries_Type = Integer32
_L3RoutingTableMaxEntries_Object = MibScalar
l3RoutingTableMaxEntries = _L3RoutingTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 4),
    _L3RoutingTableMaxEntries_Type()
)
l3RoutingTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3RoutingTableMaxEntries.setStatus("current")
_L3NextHopTableCurrentEntries_Type = Integer32
_L3NextHopTableCurrentEntries_Object = MibScalar
l3NextHopTableCurrentEntries = _L3NextHopTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 5),
    _L3NextHopTableCurrentEntries_Type()
)
l3NextHopTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NextHopTableCurrentEntries.setStatus("current")
_L3NextHopTableMaxEntries_Type = Integer32
_L3NextHopTableMaxEntries_Object = MibScalar
l3NextHopTableMaxEntries = _L3NextHopTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 6),
    _L3NextHopTableMaxEntries_Type()
)
l3NextHopTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NextHopTableMaxEntries.setStatus("current")
_L3EcmpGroupTableCurrentEntries_Type = Integer32
_L3EcmpGroupTableCurrentEntries_Object = MibScalar
l3EcmpGroupTableCurrentEntries = _L3EcmpGroupTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 7),
    _L3EcmpGroupTableCurrentEntries_Type()
)
l3EcmpGroupTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpGroupTableCurrentEntries.setStatus("current")
_L3EcmpGroupTableMaxEntries_Type = Integer32
_L3EcmpGroupTableMaxEntries_Object = MibScalar
l3EcmpGroupTableMaxEntries = _L3EcmpGroupTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 8),
    _L3EcmpGroupTableMaxEntries_Type()
)
l3EcmpGroupTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpGroupTableMaxEntries.setStatus("current")
_L3EcmpNextHopTableCurrentEntries_Type = Integer32
_L3EcmpNextHopTableCurrentEntries_Object = MibScalar
l3EcmpNextHopTableCurrentEntries = _L3EcmpNextHopTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 9),
    _L3EcmpNextHopTableCurrentEntries_Type()
)
l3EcmpNextHopTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpNextHopTableCurrentEntries.setStatus("current")
_L3EcmpNextHopTableMaxEntries_Type = Integer32
_L3EcmpNextHopTableMaxEntries_Object = MibScalar
l3EcmpNextHopTableMaxEntries = _L3EcmpNextHopTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 10),
    _L3EcmpNextHopTableMaxEntries_Type()
)
l3EcmpNextHopTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpNextHopTableMaxEntries.setStatus("current")
_IngressAclCurrentEntries_Type = Integer32
_IngressAclCurrentEntries_Object = MibScalar
ingressAclCurrentEntries = _IngressAclCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 11),
    _IngressAclCurrentEntries_Type()
)
ingressAclCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclCurrentEntries.setStatus("current")
_IngressAclMaxEntries_Type = Integer32
_IngressAclMaxEntries_Object = MibScalar
ingressAclMaxEntries = _IngressAclMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 12),
    _IngressAclMaxEntries_Type()
)
ingressAclMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclMaxEntries.setStatus("current")
_IngressAclCurrentCounters_Type = Integer32
_IngressAclCurrentCounters_Object = MibScalar
ingressAclCurrentCounters = _IngressAclCurrentCounters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 13),
    _IngressAclCurrentCounters_Type()
)
ingressAclCurrentCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclCurrentCounters.setStatus("current")
_IngressAclMaxCounters_Type = Integer32
_IngressAclMaxCounters_Object = MibScalar
ingressAclMaxCounters = _IngressAclMaxCounters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 14),
    _IngressAclMaxCounters_Type()
)
ingressAclMaxCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclMaxCounters.setStatus("current")
_IngressAclCurrentMeters_Type = Integer32
_IngressAclCurrentMeters_Object = MibScalar
ingressAclCurrentMeters = _IngressAclCurrentMeters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 15),
    _IngressAclCurrentMeters_Type()
)
ingressAclCurrentMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclCurrentMeters.setStatus("current")
_IngressAclMaxMeters_Type = Integer32
_IngressAclMaxMeters_Object = MibScalar
ingressAclMaxMeters = _IngressAclMaxMeters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 16),
    _IngressAclMaxMeters_Type()
)
ingressAclMaxMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclMaxMeters.setStatus("current")
_IngressAclCurrentSlices_Type = Integer32
_IngressAclCurrentSlices_Object = MibScalar
ingressAclCurrentSlices = _IngressAclCurrentSlices_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 17),
    _IngressAclCurrentSlices_Type()
)
ingressAclCurrentSlices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclCurrentSlices.setStatus("current")
_IngressAclMaxSlices_Type = Integer32
_IngressAclMaxSlices_Object = MibScalar
ingressAclMaxSlices = _IngressAclMaxSlices_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 18),
    _IngressAclMaxSlices_Type()
)
ingressAclMaxSlices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressAclMaxSlices.setStatus("current")
_EgressAclCurrentEntries_Type = Integer32
_EgressAclCurrentEntries_Object = MibScalar
egressAclCurrentEntries = _EgressAclCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 19),
    _EgressAclCurrentEntries_Type()
)
egressAclCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclCurrentEntries.setStatus("current")
_EgressAclMaxEntries_Type = Integer32
_EgressAclMaxEntries_Object = MibScalar
egressAclMaxEntries = _EgressAclMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 20),
    _EgressAclMaxEntries_Type()
)
egressAclMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclMaxEntries.setStatus("current")
_EgressAclCurrentCounters_Type = Integer32
_EgressAclCurrentCounters_Object = MibScalar
egressAclCurrentCounters = _EgressAclCurrentCounters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 21),
    _EgressAclCurrentCounters_Type()
)
egressAclCurrentCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclCurrentCounters.setStatus("current")
_EgressAclMaxCounters_Type = Integer32
_EgressAclMaxCounters_Object = MibScalar
egressAclMaxCounters = _EgressAclMaxCounters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 22),
    _EgressAclMaxCounters_Type()
)
egressAclMaxCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclMaxCounters.setStatus("current")
_EgressAclCurrentMeters_Type = Integer32
_EgressAclCurrentMeters_Object = MibScalar
egressAclCurrentMeters = _EgressAclCurrentMeters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 23),
    _EgressAclCurrentMeters_Type()
)
egressAclCurrentMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclCurrentMeters.setStatus("current")
_EgressAclMaxMeters_Type = Integer32
_EgressAclMaxMeters_Object = MibScalar
egressAclMaxMeters = _EgressAclMaxMeters_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 24),
    _EgressAclMaxMeters_Type()
)
egressAclMaxMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclMaxMeters.setStatus("current")
_EgressAclCurrentSlices_Type = Integer32
_EgressAclCurrentSlices_Object = MibScalar
egressAclCurrentSlices = _EgressAclCurrentSlices_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 25),
    _EgressAclCurrentSlices_Type()
)
egressAclCurrentSlices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclCurrentSlices.setStatus("current")
_EgressAclMaxSlices_Type = Integer32
_EgressAclMaxSlices_Object = MibScalar
egressAclMaxSlices = _EgressAclMaxSlices_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 26),
    _EgressAclMaxSlices_Type()
)
egressAclMaxSlices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egressAclMaxSlices.setStatus("current")
_ForwardingProfile_Type = DisplayString
_ForwardingProfile_Object = MibScalar
forwardingProfile = _ForwardingProfile_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 27),
    _ForwardingProfile_Type()
)
forwardingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardingProfile.setStatus("current")
_L2Tables_ObjectIdentity = ObjectIdentity
l2Tables = _L2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2)
)
_L2MacTableCurrentEntries_Type = Integer32
_L2MacTableCurrentEntries_Object = MibScalar
l2MacTableCurrentEntries = _L2MacTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 1),
    _L2MacTableCurrentEntries_Type()
)
l2MacTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2MacTableCurrentEntries.setStatus("current")
_L2MacTableMaxEntries_Type = Integer32
_L2MacTableMaxEntries_Object = MibScalar
l2MacTableMaxEntries = _L2MacTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 2),
    _L2MacTableMaxEntries_Type()
)
l2MacTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2MacTableMaxEntries.setStatus("current")
_L2CacheTableCurrentEntries_Type = Integer32
_L2CacheTableCurrentEntries_Object = MibScalar
l2CacheTableCurrentEntries = _L2CacheTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 3),
    _L2CacheTableCurrentEntries_Type()
)
l2CacheTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CacheTableCurrentEntries.setStatus("current")
_L2CacheTableMaxEntries_Type = Integer32
_L2CacheTableMaxEntries_Object = MibScalar
l2CacheTableMaxEntries = _L2CacheTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 4),
    _L2CacheTableMaxEntries_Type()
)
l2CacheTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CacheTableMaxEntries.setStatus("current")
_BufferUtilizn_ObjectIdentity = ObjectIdentity
bufferUtilizn = _BufferUtilizn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3)
)


class _BufUtiliznComputeTime_Type(DisplayString):
    """Custom type bufUtiliznComputeTime based on DisplayString"""
    defaultValue = OctetString("0")


_BufUtiliznComputeTime_Type.__name__ = "DisplayString"
_BufUtiliznComputeTime_Object = MibScalar
bufUtiliznComputeTime = _BufUtiliznComputeTime_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 1),
    _BufUtiliznComputeTime_Type()
)
bufUtiliznComputeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznComputeTime.setStatus("current")
_BufUtiliznPollInterval_Type = Integer32
_BufUtiliznPollInterval_Object = MibScalar
bufUtiliznPollInterval = _BufUtiliznPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 2),
    _BufUtiliznPollInterval_Type()
)
bufUtiliznPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznPollInterval.setStatus("current")
_BufUtiliznMeasureInterval_Type = Integer32
_BufUtiliznMeasureInterval_Object = MibScalar
bufUtiliznMeasureInterval = _BufUtiliznMeasureInterval_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 3),
    _BufUtiliznMeasureInterval_Type()
)
bufUtiliznMeasureInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznMeasureInterval.setStatus("current")
_BufUtiliznTable_Object = MibTable
bufUtiliznTable = _BufUtiliznTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4)
)
if mibBuilder.loadTexts:
    bufUtiliznTable.setStatus("current")
_BufUtiliznEntry_Object = MibTableRow
bufUtiliznEntry = _BufUtiliznEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1)
)
bufUtiliznEntry.setIndexNames(
    (0, "CUMULUS-RESOURCES-MIB", "bufServicePoolID"),
)
if mibBuilder.loadTexts:
    bufUtiliznEntry.setStatus("current")
_BufServicePoolID_Type = Integer32
_BufServicePoolID_Object = MibTableColumn
bufServicePoolID = _BufServicePoolID_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 1),
    _BufServicePoolID_Type()
)
bufServicePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufServicePoolID.setStatus("current")
_BufMin_Type = Integer32
_BufMin_Object = MibTableColumn
bufMin = _BufMin_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 2),
    _BufMin_Type()
)
bufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufMin.setStatus("current")
_BufMax_Type = Integer32
_BufMax_Object = MibTableColumn
bufMax = _BufMax_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 3),
    _BufMax_Type()
)
bufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufMax.setStatus("current")
_BufAvg_Type = DisplayString
_BufAvg_Object = MibTableColumn
bufAvg = _BufAvg_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 4),
    _BufAvg_Type()
)
bufAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufAvg.setStatus("current")
_BufVariance_Type = DisplayString
_BufVariance_Object = MibTableColumn
bufVariance = _BufVariance_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 5),
    _BufVariance_Type()
)
bufVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufVariance.setStatus("current")
_BufStdDev_Type = DisplayString
_BufStdDev_Object = MibTableColumn
bufStdDev = _BufStdDev_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 6),
    _BufStdDev_Type()
)
bufStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufStdDev.setStatus("current")
_BufCurr_Type = Integer32
_BufCurr_Object = MibTableColumn
bufCurr = _BufCurr_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 7),
    _BufCurr_Type()
)
bufCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufCurr.setStatus("current")
_PortPGBufUtiliznTable_Object = MibTable
portPGBufUtiliznTable = _PortPGBufUtiliznTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5)
)
if mibBuilder.loadTexts:
    portPGBufUtiliznTable.setStatus("current")
_PortPGBufUtiliznEntry_Object = MibTableRow
portPGBufUtiliznEntry = _PortPGBufUtiliznEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1)
)
portPGBufUtiliznEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portPGBufUtiliznEntry.setStatus("current")
_PortPGBufUtiliznPortName_Type = DisplayString
_PortPGBufUtiliznPortName_Object = MibTableColumn
portPGBufUtiliznPortName = _PortPGBufUtiliznPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 1),
    _PortPGBufUtiliznPortName_Type()
)
portPGBufUtiliznPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPGBufUtiliznPortName.setStatus("deprecated")
_Pg0BufCurrUsage_Type = Counter64
_Pg0BufCurrUsage_Object = MibTableColumn
pg0BufCurrUsage = _Pg0BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 2),
    _Pg0BufCurrUsage_Type()
)
pg0BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg0BufCurrUsage.setStatus("current")
_Pg0BufMaxUsage_Type = Counter64
_Pg0BufMaxUsage_Object = MibTableColumn
pg0BufMaxUsage = _Pg0BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 3),
    _Pg0BufMaxUsage_Type()
)
pg0BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg0BufMaxUsage.setStatus("current")
_Pg1BufCurrUsage_Type = Counter64
_Pg1BufCurrUsage_Object = MibTableColumn
pg1BufCurrUsage = _Pg1BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 4),
    _Pg1BufCurrUsage_Type()
)
pg1BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg1BufCurrUsage.setStatus("current")
_Pg1BufMaxUsage_Type = Counter64
_Pg1BufMaxUsage_Object = MibTableColumn
pg1BufMaxUsage = _Pg1BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 5),
    _Pg1BufMaxUsage_Type()
)
pg1BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg1BufMaxUsage.setStatus("current")
_Pg2BufCurrUsage_Type = Counter64
_Pg2BufCurrUsage_Object = MibTableColumn
pg2BufCurrUsage = _Pg2BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 6),
    _Pg2BufCurrUsage_Type()
)
pg2BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg2BufCurrUsage.setStatus("current")
_Pg2BufMaxUsage_Type = Counter64
_Pg2BufMaxUsage_Object = MibTableColumn
pg2BufMaxUsage = _Pg2BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 7),
    _Pg2BufMaxUsage_Type()
)
pg2BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg2BufMaxUsage.setStatus("current")
_Pg3BufCurrUsage_Type = Counter64
_Pg3BufCurrUsage_Object = MibTableColumn
pg3BufCurrUsage = _Pg3BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 8),
    _Pg3BufCurrUsage_Type()
)
pg3BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg3BufCurrUsage.setStatus("current")
_Pg3BufMaxUsage_Type = Counter64
_Pg3BufMaxUsage_Object = MibTableColumn
pg3BufMaxUsage = _Pg3BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 9),
    _Pg3BufMaxUsage_Type()
)
pg3BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg3BufMaxUsage.setStatus("current")
_Pg4BufCurrUsage_Type = Counter64
_Pg4BufCurrUsage_Object = MibTableColumn
pg4BufCurrUsage = _Pg4BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 10),
    _Pg4BufCurrUsage_Type()
)
pg4BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg4BufCurrUsage.setStatus("current")
_Pg4BufMaxUsage_Type = Counter64
_Pg4BufMaxUsage_Object = MibTableColumn
pg4BufMaxUsage = _Pg4BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 11),
    _Pg4BufMaxUsage_Type()
)
pg4BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg4BufMaxUsage.setStatus("current")
_Pg5BufCurrUsage_Type = Counter64
_Pg5BufCurrUsage_Object = MibTableColumn
pg5BufCurrUsage = _Pg5BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 12),
    _Pg5BufCurrUsage_Type()
)
pg5BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg5BufCurrUsage.setStatus("current")
_Pg5BufMaxUsage_Type = Counter64
_Pg5BufMaxUsage_Object = MibTableColumn
pg5BufMaxUsage = _Pg5BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 13),
    _Pg5BufMaxUsage_Type()
)
pg5BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg5BufMaxUsage.setStatus("current")
_Pg6BufCurrUsage_Type = Counter64
_Pg6BufCurrUsage_Object = MibTableColumn
pg6BufCurrUsage = _Pg6BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 14),
    _Pg6BufCurrUsage_Type()
)
pg6BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg6BufCurrUsage.setStatus("current")
_Pg6BufMaxUsage_Type = Counter64
_Pg6BufMaxUsage_Object = MibTableColumn
pg6BufMaxUsage = _Pg6BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 15),
    _Pg6BufMaxUsage_Type()
)
pg6BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg6BufMaxUsage.setStatus("current")
_Pg7BufCurrUsage_Type = Counter64
_Pg7BufCurrUsage_Object = MibTableColumn
pg7BufCurrUsage = _Pg7BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 16),
    _Pg7BufCurrUsage_Type()
)
pg7BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg7BufCurrUsage.setStatus("current")
_Pg7BufMaxUsage_Type = Counter64
_Pg7BufMaxUsage_Object = MibTableColumn
pg7BufMaxUsage = _Pg7BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 17),
    _Pg7BufMaxUsage_Type()
)
pg7BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg7BufMaxUsage.setStatus("current")
_Pg9BufCurrUsage_Type = Counter64
_Pg9BufCurrUsage_Object = MibTableColumn
pg9BufCurrUsage = _Pg9BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 20),
    _Pg9BufCurrUsage_Type()
)
pg9BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg9BufCurrUsage.setStatus("current")
_Pg9BufMaxUsage_Type = Counter64
_Pg9BufMaxUsage_Object = MibTableColumn
pg9BufMaxUsage = _Pg9BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 5, 1, 21),
    _Pg9BufMaxUsage_Type()
)
pg9BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pg9BufMaxUsage.setStatus("current")
_PortPoolBufUtiliznTable_Object = MibTable
portPoolBufUtiliznTable = _PortPoolBufUtiliznTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6)
)
if mibBuilder.loadTexts:
    portPoolBufUtiliznTable.setStatus("current")
_PortPoolBufUtiliznEntry_Object = MibTableRow
portPoolBufUtiliznEntry = _PortPoolBufUtiliznEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1)
)
portPoolBufUtiliznEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portPoolBufUtiliznEntry.setStatus("current")
_PortPoolBufUtiliznPortName_Type = DisplayString
_PortPoolBufUtiliznPortName_Object = MibTableColumn
portPoolBufUtiliznPortName = _PortPoolBufUtiliznPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 1),
    _PortPoolBufUtiliznPortName_Type()
)
portPoolBufUtiliznPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPoolBufUtiliznPortName.setStatus("deprecated")
_IPool0BufCurrUsage_Type = Counter64
_IPool0BufCurrUsage_Object = MibTableColumn
iPool0BufCurrUsage = _IPool0BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 2),
    _IPool0BufCurrUsage_Type()
)
iPool0BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool0BufCurrUsage.setStatus("current")
_IPool0BufMaxUsage_Type = Counter64
_IPool0BufMaxUsage_Object = MibTableColumn
iPool0BufMaxUsage = _IPool0BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 3),
    _IPool0BufMaxUsage_Type()
)
iPool0BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool0BufMaxUsage.setStatus("current")
_IPool1BufCurrUsage_Type = Counter64
_IPool1BufCurrUsage_Object = MibTableColumn
iPool1BufCurrUsage = _IPool1BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 4),
    _IPool1BufCurrUsage_Type()
)
iPool1BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool1BufCurrUsage.setStatus("current")
_IPool1BufMaxUsage_Type = Counter64
_IPool1BufMaxUsage_Object = MibTableColumn
iPool1BufMaxUsage = _IPool1BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 5),
    _IPool1BufMaxUsage_Type()
)
iPool1BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool1BufMaxUsage.setStatus("current")
_IPool2BufCurrUsage_Type = Counter64
_IPool2BufCurrUsage_Object = MibTableColumn
iPool2BufCurrUsage = _IPool2BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 6),
    _IPool2BufCurrUsage_Type()
)
iPool2BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool2BufCurrUsage.setStatus("current")
_IPool2BufMaxUsage_Type = Counter64
_IPool2BufMaxUsage_Object = MibTableColumn
iPool2BufMaxUsage = _IPool2BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 7),
    _IPool2BufMaxUsage_Type()
)
iPool2BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool2BufMaxUsage.setStatus("current")
_IPool3BufCurrUsage_Type = Counter64
_IPool3BufCurrUsage_Object = MibTableColumn
iPool3BufCurrUsage = _IPool3BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 8),
    _IPool3BufCurrUsage_Type()
)
iPool3BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool3BufCurrUsage.setStatus("current")
_IPool3BufMaxUsage_Type = Counter64
_IPool3BufMaxUsage_Object = MibTableColumn
iPool3BufMaxUsage = _IPool3BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 9),
    _IPool3BufMaxUsage_Type()
)
iPool3BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool3BufMaxUsage.setStatus("current")
_IPool4BufCurrUsage_Type = Counter64
_IPool4BufCurrUsage_Object = MibTableColumn
iPool4BufCurrUsage = _IPool4BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 10),
    _IPool4BufCurrUsage_Type()
)
iPool4BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool4BufCurrUsage.setStatus("current")
_IPool4BufMaxUsage_Type = Counter64
_IPool4BufMaxUsage_Object = MibTableColumn
iPool4BufMaxUsage = _IPool4BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 11),
    _IPool4BufMaxUsage_Type()
)
iPool4BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool4BufMaxUsage.setStatus("current")
_IPool5BufCurrUsage_Type = Counter64
_IPool5BufCurrUsage_Object = MibTableColumn
iPool5BufCurrUsage = _IPool5BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 12),
    _IPool5BufCurrUsage_Type()
)
iPool5BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool5BufCurrUsage.setStatus("current")
_IPool5BufMaxUsage_Type = Counter64
_IPool5BufMaxUsage_Object = MibTableColumn
iPool5BufMaxUsage = _IPool5BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 13),
    _IPool5BufMaxUsage_Type()
)
iPool5BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool5BufMaxUsage.setStatus("current")
_IPool6BufCurrUsage_Type = Counter64
_IPool6BufCurrUsage_Object = MibTableColumn
iPool6BufCurrUsage = _IPool6BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 14),
    _IPool6BufCurrUsage_Type()
)
iPool6BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool6BufCurrUsage.setStatus("current")
_IPool6BufMaxUsage_Type = Counter64
_IPool6BufMaxUsage_Object = MibTableColumn
iPool6BufMaxUsage = _IPool6BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 15),
    _IPool6BufMaxUsage_Type()
)
iPool6BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool6BufMaxUsage.setStatus("current")
_IPool7BufCurrUsage_Type = Counter64
_IPool7BufCurrUsage_Object = MibTableColumn
iPool7BufCurrUsage = _IPool7BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 16),
    _IPool7BufCurrUsage_Type()
)
iPool7BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool7BufCurrUsage.setStatus("current")
_IPool7BufMaxUsage_Type = Counter64
_IPool7BufMaxUsage_Object = MibTableColumn
iPool7BufMaxUsage = _IPool7BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 17),
    _IPool7BufMaxUsage_Type()
)
iPool7BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool7BufMaxUsage.setStatus("current")
_IPool8BufCurrUsage_Type = Counter64
_IPool8BufCurrUsage_Object = MibTableColumn
iPool8BufCurrUsage = _IPool8BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 18),
    _IPool8BufCurrUsage_Type()
)
iPool8BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool8BufCurrUsage.setStatus("current")
_IPool8BufMaxUsage_Type = Counter64
_IPool8BufMaxUsage_Object = MibTableColumn
iPool8BufMaxUsage = _IPool8BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 19),
    _IPool8BufMaxUsage_Type()
)
iPool8BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool8BufMaxUsage.setStatus("current")
_IPool9BufCurrUsage_Type = Counter64
_IPool9BufCurrUsage_Object = MibTableColumn
iPool9BufCurrUsage = _IPool9BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 20),
    _IPool9BufCurrUsage_Type()
)
iPool9BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool9BufCurrUsage.setStatus("current")
_IPool9BufMaxUsage_Type = Counter64
_IPool9BufMaxUsage_Object = MibTableColumn
iPool9BufMaxUsage = _IPool9BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 21),
    _IPool9BufMaxUsage_Type()
)
iPool9BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPool9BufMaxUsage.setStatus("current")
_EPool11BufCurrUsage_Type = Counter64
_EPool11BufCurrUsage_Object = MibTableColumn
ePool11BufCurrUsage = _EPool11BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 22),
    _EPool11BufCurrUsage_Type()
)
ePool11BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool11BufCurrUsage.setStatus("current")
_EPool11BufMaxUsage_Type = Counter64
_EPool11BufMaxUsage_Object = MibTableColumn
ePool11BufMaxUsage = _EPool11BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 23),
    _EPool11BufMaxUsage_Type()
)
ePool11BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool11BufMaxUsage.setStatus("current")
_EPool12BufCurrUsage_Type = Counter64
_EPool12BufCurrUsage_Object = MibTableColumn
ePool12BufCurrUsage = _EPool12BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 24),
    _EPool12BufCurrUsage_Type()
)
ePool12BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool12BufCurrUsage.setStatus("current")
_EPool12BufMaxUsage_Type = Counter64
_EPool12BufMaxUsage_Object = MibTableColumn
ePool12BufMaxUsage = _EPool12BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 25),
    _EPool12BufMaxUsage_Type()
)
ePool12BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool12BufMaxUsage.setStatus("current")
_EPool13BufCurrUsage_Type = Counter64
_EPool13BufCurrUsage_Object = MibTableColumn
ePool13BufCurrUsage = _EPool13BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 26),
    _EPool13BufCurrUsage_Type()
)
ePool13BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool13BufCurrUsage.setStatus("current")
_EPool13BufMaxUsage_Type = Counter64
_EPool13BufMaxUsage_Object = MibTableColumn
ePool13BufMaxUsage = _EPool13BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 27),
    _EPool13BufMaxUsage_Type()
)
ePool13BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool13BufMaxUsage.setStatus("current")
_EPool14BufCurrUsage_Type = Counter64
_EPool14BufCurrUsage_Object = MibTableColumn
ePool14BufCurrUsage = _EPool14BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 28),
    _EPool14BufCurrUsage_Type()
)
ePool14BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool14BufCurrUsage.setStatus("current")
_EPool14BufMaxUsage_Type = Counter64
_EPool14BufMaxUsage_Object = MibTableColumn
ePool14BufMaxUsage = _EPool14BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 29),
    _EPool14BufMaxUsage_Type()
)
ePool14BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool14BufMaxUsage.setStatus("current")
_EPool15BufCurrUsage_Type = Counter64
_EPool15BufCurrUsage_Object = MibTableColumn
ePool15BufCurrUsage = _EPool15BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 30),
    _EPool15BufCurrUsage_Type()
)
ePool15BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool15BufCurrUsage.setStatus("current")
_EPool15BufMaxUsage_Type = Counter64
_EPool15BufMaxUsage_Object = MibTableColumn
ePool15BufMaxUsage = _EPool15BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 31),
    _EPool15BufMaxUsage_Type()
)
ePool15BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool15BufMaxUsage.setStatus("current")
_EPool16BufCurrUsage_Type = Counter64
_EPool16BufCurrUsage_Object = MibTableColumn
ePool16BufCurrUsage = _EPool16BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 32),
    _EPool16BufCurrUsage_Type()
)
ePool16BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool16BufCurrUsage.setStatus("current")
_EPool16BufMaxUsage_Type = Counter64
_EPool16BufMaxUsage_Object = MibTableColumn
ePool16BufMaxUsage = _EPool16BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 33),
    _EPool16BufMaxUsage_Type()
)
ePool16BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool16BufMaxUsage.setStatus("current")
_EPool17BufCurrUsage_Type = Counter64
_EPool17BufCurrUsage_Object = MibTableColumn
ePool17BufCurrUsage = _EPool17BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 34),
    _EPool17BufCurrUsage_Type()
)
ePool17BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool17BufCurrUsage.setStatus("current")
_EPool17BufMaxUsage_Type = Counter64
_EPool17BufMaxUsage_Object = MibTableColumn
ePool17BufMaxUsage = _EPool17BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 35),
    _EPool17BufMaxUsage_Type()
)
ePool17BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool17BufMaxUsage.setStatus("current")
_EPool18BufCurrUsage_Type = Counter64
_EPool18BufCurrUsage_Object = MibTableColumn
ePool18BufCurrUsage = _EPool18BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 36),
    _EPool18BufCurrUsage_Type()
)
ePool18BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool18BufCurrUsage.setStatus("current")
_EPool18BufMaxUsage_Type = Counter64
_EPool18BufMaxUsage_Object = MibTableColumn
ePool18BufMaxUsage = _EPool18BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 37),
    _EPool18BufMaxUsage_Type()
)
ePool18BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool18BufMaxUsage.setStatus("current")
_EPool19BufCurrUsage_Type = Counter64
_EPool19BufCurrUsage_Object = MibTableColumn
ePool19BufCurrUsage = _EPool19BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 38),
    _EPool19BufCurrUsage_Type()
)
ePool19BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool19BufCurrUsage.setStatus("current")
_EPool19BufMaxUsage_Type = Counter64
_EPool19BufMaxUsage_Object = MibTableColumn
ePool19BufMaxUsage = _EPool19BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 39),
    _EPool19BufMaxUsage_Type()
)
ePool19BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool19BufMaxUsage.setStatus("current")
_EPool20BufCurrUsage_Type = Counter64
_EPool20BufCurrUsage_Object = MibTableColumn
ePool20BufCurrUsage = _EPool20BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 40),
    _EPool20BufCurrUsage_Type()
)
ePool20BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool20BufCurrUsage.setStatus("current")
_EPool20BufMaxUsage_Type = Counter64
_EPool20BufMaxUsage_Object = MibTableColumn
ePool20BufMaxUsage = _EPool20BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 6, 1, 41),
    _EPool20BufMaxUsage_Type()
)
ePool20BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePool20BufMaxUsage.setStatus("current")
_PortTCBufUtiliznTable_Object = MibTable
portTCBufUtiliznTable = _PortTCBufUtiliznTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7)
)
if mibBuilder.loadTexts:
    portTCBufUtiliznTable.setStatus("current")
_PortTCBufUtiliznEntry_Object = MibTableRow
portTCBufUtiliznEntry = _PortTCBufUtiliznEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1)
)
portTCBufUtiliznEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portTCBufUtiliznEntry.setStatus("current")
_PortTCBufUtiliznPortName_Type = DisplayString
_PortTCBufUtiliznPortName_Object = MibTableColumn
portTCBufUtiliznPortName = _PortTCBufUtiliznPortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 1),
    _PortTCBufUtiliznPortName_Type()
)
portTCBufUtiliznPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTCBufUtiliznPortName.setStatus("deprecated")
_Tc0BufCurrUsage_Type = Counter64
_Tc0BufCurrUsage_Object = MibTableColumn
tc0BufCurrUsage = _Tc0BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 2),
    _Tc0BufCurrUsage_Type()
)
tc0BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc0BufCurrUsage.setStatus("current")
_Tc0BufMaxUsage_Type = Counter64
_Tc0BufMaxUsage_Object = MibTableColumn
tc0BufMaxUsage = _Tc0BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 3),
    _Tc0BufMaxUsage_Type()
)
tc0BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc0BufMaxUsage.setStatus("current")
_Tc1BufCurrUsage_Type = Counter64
_Tc1BufCurrUsage_Object = MibTableColumn
tc1BufCurrUsage = _Tc1BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 4),
    _Tc1BufCurrUsage_Type()
)
tc1BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc1BufCurrUsage.setStatus("current")
_Tc1BufMaxUsage_Type = Counter64
_Tc1BufMaxUsage_Object = MibTableColumn
tc1BufMaxUsage = _Tc1BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 5),
    _Tc1BufMaxUsage_Type()
)
tc1BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc1BufMaxUsage.setStatus("current")
_Tc2BufCurrUsage_Type = Counter64
_Tc2BufCurrUsage_Object = MibTableColumn
tc2BufCurrUsage = _Tc2BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 6),
    _Tc2BufCurrUsage_Type()
)
tc2BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc2BufCurrUsage.setStatus("current")
_Tc2BufMaxUsage_Type = Counter64
_Tc2BufMaxUsage_Object = MibTableColumn
tc2BufMaxUsage = _Tc2BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 7),
    _Tc2BufMaxUsage_Type()
)
tc2BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc2BufMaxUsage.setStatus("current")
_Tc3BufCurrUsage_Type = Counter64
_Tc3BufCurrUsage_Object = MibTableColumn
tc3BufCurrUsage = _Tc3BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 8),
    _Tc3BufCurrUsage_Type()
)
tc3BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc3BufCurrUsage.setStatus("current")
_Tc3BufMaxUsage_Type = Counter64
_Tc3BufMaxUsage_Object = MibTableColumn
tc3BufMaxUsage = _Tc3BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 9),
    _Tc3BufMaxUsage_Type()
)
tc3BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc3BufMaxUsage.setStatus("current")
_Tc4BufCurrUsage_Type = Counter64
_Tc4BufCurrUsage_Object = MibTableColumn
tc4BufCurrUsage = _Tc4BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 10),
    _Tc4BufCurrUsage_Type()
)
tc4BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc4BufCurrUsage.setStatus("current")
_Tc4BufMaxUsage_Type = Counter64
_Tc4BufMaxUsage_Object = MibTableColumn
tc4BufMaxUsage = _Tc4BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 11),
    _Tc4BufMaxUsage_Type()
)
tc4BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc4BufMaxUsage.setStatus("current")
_Tc5BufCurrUsage_Type = Counter64
_Tc5BufCurrUsage_Object = MibTableColumn
tc5BufCurrUsage = _Tc5BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 12),
    _Tc5BufCurrUsage_Type()
)
tc5BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc5BufCurrUsage.setStatus("current")
_Tc5BufMaxUsage_Type = Counter64
_Tc5BufMaxUsage_Object = MibTableColumn
tc5BufMaxUsage = _Tc5BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 13),
    _Tc5BufMaxUsage_Type()
)
tc5BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc5BufMaxUsage.setStatus("current")
_Tc6BufCurrUsage_Type = Counter64
_Tc6BufCurrUsage_Object = MibTableColumn
tc6BufCurrUsage = _Tc6BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 14),
    _Tc6BufCurrUsage_Type()
)
tc6BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc6BufCurrUsage.setStatus("current")
_Tc6BufMaxUsage_Type = Counter64
_Tc6BufMaxUsage_Object = MibTableColumn
tc6BufMaxUsage = _Tc6BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 15),
    _Tc6BufMaxUsage_Type()
)
tc6BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc6BufMaxUsage.setStatus("current")
_Tc7BufCurrUsage_Type = Counter64
_Tc7BufCurrUsage_Object = MibTableColumn
tc7BufCurrUsage = _Tc7BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 16),
    _Tc7BufCurrUsage_Type()
)
tc7BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc7BufCurrUsage.setStatus("current")
_Tc7BufMaxUsage_Type = Counter64
_Tc7BufMaxUsage_Object = MibTableColumn
tc7BufMaxUsage = _Tc7BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 17),
    _Tc7BufMaxUsage_Type()
)
tc7BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc7BufMaxUsage.setStatus("current")
_Tc8BufCurrUsage_Type = Counter64
_Tc8BufCurrUsage_Object = MibTableColumn
tc8BufCurrUsage = _Tc8BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 18),
    _Tc8BufCurrUsage_Type()
)
tc8BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc8BufCurrUsage.setStatus("current")
_Tc8BufMaxUsage_Type = Counter64
_Tc8BufMaxUsage_Object = MibTableColumn
tc8BufMaxUsage = _Tc8BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 19),
    _Tc8BufMaxUsage_Type()
)
tc8BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc8BufMaxUsage.setStatus("current")
_Tc9BufCurrUsage_Type = Counter64
_Tc9BufCurrUsage_Object = MibTableColumn
tc9BufCurrUsage = _Tc9BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 20),
    _Tc9BufCurrUsage_Type()
)
tc9BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc9BufCurrUsage.setStatus("current")
_Tc9BufMaxUsage_Type = Counter64
_Tc9BufMaxUsage_Object = MibTableColumn
tc9BufMaxUsage = _Tc9BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 21),
    _Tc9BufMaxUsage_Type()
)
tc9BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc9BufMaxUsage.setStatus("current")
_Tc10BufCurrUsage_Type = Counter64
_Tc10BufCurrUsage_Object = MibTableColumn
tc10BufCurrUsage = _Tc10BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 22),
    _Tc10BufCurrUsage_Type()
)
tc10BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc10BufCurrUsage.setStatus("current")
_Tc10BufMaxUsage_Type = Counter64
_Tc10BufMaxUsage_Object = MibTableColumn
tc10BufMaxUsage = _Tc10BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 23),
    _Tc10BufMaxUsage_Type()
)
tc10BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc10BufMaxUsage.setStatus("current")
_Tc11BufCurrUsage_Type = Counter64
_Tc11BufCurrUsage_Object = MibTableColumn
tc11BufCurrUsage = _Tc11BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 24),
    _Tc11BufCurrUsage_Type()
)
tc11BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc11BufCurrUsage.setStatus("current")
_Tc11BufMaxUsage_Type = Counter64
_Tc11BufMaxUsage_Object = MibTableColumn
tc11BufMaxUsage = _Tc11BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 25),
    _Tc11BufMaxUsage_Type()
)
tc11BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc11BufMaxUsage.setStatus("current")
_Tc12BufCurrUsage_Type = Counter64
_Tc12BufCurrUsage_Object = MibTableColumn
tc12BufCurrUsage = _Tc12BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 26),
    _Tc12BufCurrUsage_Type()
)
tc12BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc12BufCurrUsage.setStatus("current")
_Tc12BufMaxUsage_Type = Counter64
_Tc12BufMaxUsage_Object = MibTableColumn
tc12BufMaxUsage = _Tc12BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 27),
    _Tc12BufMaxUsage_Type()
)
tc12BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc12BufMaxUsage.setStatus("current")
_Tc13BufCurrUsage_Type = Counter64
_Tc13BufCurrUsage_Object = MibTableColumn
tc13BufCurrUsage = _Tc13BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 28),
    _Tc13BufCurrUsage_Type()
)
tc13BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc13BufCurrUsage.setStatus("current")
_Tc13BufMaxUsage_Type = Counter64
_Tc13BufMaxUsage_Object = MibTableColumn
tc13BufMaxUsage = _Tc13BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 29),
    _Tc13BufMaxUsage_Type()
)
tc13BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc13BufMaxUsage.setStatus("current")
_Tc14BufCurrUsage_Type = Counter64
_Tc14BufCurrUsage_Object = MibTableColumn
tc14BufCurrUsage = _Tc14BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 30),
    _Tc14BufCurrUsage_Type()
)
tc14BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc14BufCurrUsage.setStatus("current")
_Tc14BufMaxUsage_Type = Counter64
_Tc14BufMaxUsage_Object = MibTableColumn
tc14BufMaxUsage = _Tc14BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 31),
    _Tc14BufMaxUsage_Type()
)
tc14BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc14BufMaxUsage.setStatus("current")
_Tc15BufCurrUsage_Type = Counter64
_Tc15BufCurrUsage_Object = MibTableColumn
tc15BufCurrUsage = _Tc15BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 32),
    _Tc15BufCurrUsage_Type()
)
tc15BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc15BufCurrUsage.setStatus("current")
_Tc15BufMaxUsage_Type = Counter64
_Tc15BufMaxUsage_Object = MibTableColumn
tc15BufMaxUsage = _Tc15BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 33),
    _Tc15BufMaxUsage_Type()
)
tc15BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc15BufMaxUsage.setStatus("current")
_Tc16BufCurrUsage_Type = Counter64
_Tc16BufCurrUsage_Object = MibTableColumn
tc16BufCurrUsage = _Tc16BufCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 34),
    _Tc16BufCurrUsage_Type()
)
tc16BufCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc16BufCurrUsage.setStatus("current")
_Tc16BufMaxUsage_Type = Counter64
_Tc16BufMaxUsage_Object = MibTableColumn
tc16BufMaxUsage = _Tc16BufMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 7, 1, 35),
    _Tc16BufMaxUsage_Type()
)
tc16BufMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tc16BufMaxUsage.setStatus("current")
_BufUtiliznCellSize_Type = Integer32
_BufUtiliznCellSize_Object = MibScalar
bufUtiliznCellSize = _BufUtiliznCellSize_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 8),
    _BufUtiliznCellSize_Type()
)
bufUtiliznCellSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznCellSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-RESOURCES-MIB",
    **{"resourceUtilization": resourceUtilization,
       "l3Tables": l3Tables,
       "l3HostTableCurrentEntries": l3HostTableCurrentEntries,
       "l3HostTableMaxEntries": l3HostTableMaxEntries,
       "l3RoutingTableCurrentEntries": l3RoutingTableCurrentEntries,
       "l3RoutingTableMaxEntries": l3RoutingTableMaxEntries,
       "l3NextHopTableCurrentEntries": l3NextHopTableCurrentEntries,
       "l3NextHopTableMaxEntries": l3NextHopTableMaxEntries,
       "l3EcmpGroupTableCurrentEntries": l3EcmpGroupTableCurrentEntries,
       "l3EcmpGroupTableMaxEntries": l3EcmpGroupTableMaxEntries,
       "l3EcmpNextHopTableCurrentEntries": l3EcmpNextHopTableCurrentEntries,
       "l3EcmpNextHopTableMaxEntries": l3EcmpNextHopTableMaxEntries,
       "ingressAclCurrentEntries": ingressAclCurrentEntries,
       "ingressAclMaxEntries": ingressAclMaxEntries,
       "ingressAclCurrentCounters": ingressAclCurrentCounters,
       "ingressAclMaxCounters": ingressAclMaxCounters,
       "ingressAclCurrentMeters": ingressAclCurrentMeters,
       "ingressAclMaxMeters": ingressAclMaxMeters,
       "ingressAclCurrentSlices": ingressAclCurrentSlices,
       "ingressAclMaxSlices": ingressAclMaxSlices,
       "egressAclCurrentEntries": egressAclCurrentEntries,
       "egressAclMaxEntries": egressAclMaxEntries,
       "egressAclCurrentCounters": egressAclCurrentCounters,
       "egressAclMaxCounters": egressAclMaxCounters,
       "egressAclCurrentMeters": egressAclCurrentMeters,
       "egressAclMaxMeters": egressAclMaxMeters,
       "egressAclCurrentSlices": egressAclCurrentSlices,
       "egressAclMaxSlices": egressAclMaxSlices,
       "forwardingProfile": forwardingProfile,
       "l2Tables": l2Tables,
       "l2MacTableCurrentEntries": l2MacTableCurrentEntries,
       "l2MacTableMaxEntries": l2MacTableMaxEntries,
       "l2CacheTableCurrentEntries": l2CacheTableCurrentEntries,
       "l2CacheTableMaxEntries": l2CacheTableMaxEntries,
       "bufferUtilizn": bufferUtilizn,
       "bufUtiliznComputeTime": bufUtiliznComputeTime,
       "bufUtiliznPollInterval": bufUtiliznPollInterval,
       "bufUtiliznMeasureInterval": bufUtiliznMeasureInterval,
       "bufUtiliznTable": bufUtiliznTable,
       "bufUtiliznEntry": bufUtiliznEntry,
       "bufServicePoolID": bufServicePoolID,
       "bufMin": bufMin,
       "bufMax": bufMax,
       "bufAvg": bufAvg,
       "bufVariance": bufVariance,
       "bufStdDev": bufStdDev,
       "bufCurr": bufCurr,
       "portPGBufUtiliznTable": portPGBufUtiliznTable,
       "portPGBufUtiliznEntry": portPGBufUtiliznEntry,
       "portPGBufUtiliznPortName": portPGBufUtiliznPortName,
       "pg0BufCurrUsage": pg0BufCurrUsage,
       "pg0BufMaxUsage": pg0BufMaxUsage,
       "pg1BufCurrUsage": pg1BufCurrUsage,
       "pg1BufMaxUsage": pg1BufMaxUsage,
       "pg2BufCurrUsage": pg2BufCurrUsage,
       "pg2BufMaxUsage": pg2BufMaxUsage,
       "pg3BufCurrUsage": pg3BufCurrUsage,
       "pg3BufMaxUsage": pg3BufMaxUsage,
       "pg4BufCurrUsage": pg4BufCurrUsage,
       "pg4BufMaxUsage": pg4BufMaxUsage,
       "pg5BufCurrUsage": pg5BufCurrUsage,
       "pg5BufMaxUsage": pg5BufMaxUsage,
       "pg6BufCurrUsage": pg6BufCurrUsage,
       "pg6BufMaxUsage": pg6BufMaxUsage,
       "pg7BufCurrUsage": pg7BufCurrUsage,
       "pg7BufMaxUsage": pg7BufMaxUsage,
       "pg9BufCurrUsage": pg9BufCurrUsage,
       "pg9BufMaxUsage": pg9BufMaxUsage,
       "portPoolBufUtiliznTable": portPoolBufUtiliznTable,
       "portPoolBufUtiliznEntry": portPoolBufUtiliznEntry,
       "portPoolBufUtiliznPortName": portPoolBufUtiliznPortName,
       "iPool0BufCurrUsage": iPool0BufCurrUsage,
       "iPool0BufMaxUsage": iPool0BufMaxUsage,
       "iPool1BufCurrUsage": iPool1BufCurrUsage,
       "iPool1BufMaxUsage": iPool1BufMaxUsage,
       "iPool2BufCurrUsage": iPool2BufCurrUsage,
       "iPool2BufMaxUsage": iPool2BufMaxUsage,
       "iPool3BufCurrUsage": iPool3BufCurrUsage,
       "iPool3BufMaxUsage": iPool3BufMaxUsage,
       "iPool4BufCurrUsage": iPool4BufCurrUsage,
       "iPool4BufMaxUsage": iPool4BufMaxUsage,
       "iPool5BufCurrUsage": iPool5BufCurrUsage,
       "iPool5BufMaxUsage": iPool5BufMaxUsage,
       "iPool6BufCurrUsage": iPool6BufCurrUsage,
       "iPool6BufMaxUsage": iPool6BufMaxUsage,
       "iPool7BufCurrUsage": iPool7BufCurrUsage,
       "iPool7BufMaxUsage": iPool7BufMaxUsage,
       "iPool8BufCurrUsage": iPool8BufCurrUsage,
       "iPool8BufMaxUsage": iPool8BufMaxUsage,
       "iPool9BufCurrUsage": iPool9BufCurrUsage,
       "iPool9BufMaxUsage": iPool9BufMaxUsage,
       "ePool11BufCurrUsage": ePool11BufCurrUsage,
       "ePool11BufMaxUsage": ePool11BufMaxUsage,
       "ePool12BufCurrUsage": ePool12BufCurrUsage,
       "ePool12BufMaxUsage": ePool12BufMaxUsage,
       "ePool13BufCurrUsage": ePool13BufCurrUsage,
       "ePool13BufMaxUsage": ePool13BufMaxUsage,
       "ePool14BufCurrUsage": ePool14BufCurrUsage,
       "ePool14BufMaxUsage": ePool14BufMaxUsage,
       "ePool15BufCurrUsage": ePool15BufCurrUsage,
       "ePool15BufMaxUsage": ePool15BufMaxUsage,
       "ePool16BufCurrUsage": ePool16BufCurrUsage,
       "ePool16BufMaxUsage": ePool16BufMaxUsage,
       "ePool17BufCurrUsage": ePool17BufCurrUsage,
       "ePool17BufMaxUsage": ePool17BufMaxUsage,
       "ePool18BufCurrUsage": ePool18BufCurrUsage,
       "ePool18BufMaxUsage": ePool18BufMaxUsage,
       "ePool19BufCurrUsage": ePool19BufCurrUsage,
       "ePool19BufMaxUsage": ePool19BufMaxUsage,
       "ePool20BufCurrUsage": ePool20BufCurrUsage,
       "ePool20BufMaxUsage": ePool20BufMaxUsage,
       "portTCBufUtiliznTable": portTCBufUtiliznTable,
       "portTCBufUtiliznEntry": portTCBufUtiliznEntry,
       "portTCBufUtiliznPortName": portTCBufUtiliznPortName,
       "tc0BufCurrUsage": tc0BufCurrUsage,
       "tc0BufMaxUsage": tc0BufMaxUsage,
       "tc1BufCurrUsage": tc1BufCurrUsage,
       "tc1BufMaxUsage": tc1BufMaxUsage,
       "tc2BufCurrUsage": tc2BufCurrUsage,
       "tc2BufMaxUsage": tc2BufMaxUsage,
       "tc3BufCurrUsage": tc3BufCurrUsage,
       "tc3BufMaxUsage": tc3BufMaxUsage,
       "tc4BufCurrUsage": tc4BufCurrUsage,
       "tc4BufMaxUsage": tc4BufMaxUsage,
       "tc5BufCurrUsage": tc5BufCurrUsage,
       "tc5BufMaxUsage": tc5BufMaxUsage,
       "tc6BufCurrUsage": tc6BufCurrUsage,
       "tc6BufMaxUsage": tc6BufMaxUsage,
       "tc7BufCurrUsage": tc7BufCurrUsage,
       "tc7BufMaxUsage": tc7BufMaxUsage,
       "tc8BufCurrUsage": tc8BufCurrUsage,
       "tc8BufMaxUsage": tc8BufMaxUsage,
       "tc9BufCurrUsage": tc9BufCurrUsage,
       "tc9BufMaxUsage": tc9BufMaxUsage,
       "tc10BufCurrUsage": tc10BufCurrUsage,
       "tc10BufMaxUsage": tc10BufMaxUsage,
       "tc11BufCurrUsage": tc11BufCurrUsage,
       "tc11BufMaxUsage": tc11BufMaxUsage,
       "tc12BufCurrUsage": tc12BufCurrUsage,
       "tc12BufMaxUsage": tc12BufMaxUsage,
       "tc13BufCurrUsage": tc13BufCurrUsage,
       "tc13BufMaxUsage": tc13BufMaxUsage,
       "tc14BufCurrUsage": tc14BufCurrUsage,
       "tc14BufMaxUsage": tc14BufMaxUsage,
       "tc15BufCurrUsage": tc15BufCurrUsage,
       "tc15BufMaxUsage": tc15BufMaxUsage,
       "tc16BufCurrUsage": tc16BufCurrUsage,
       "tc16BufMaxUsage": tc16BufMaxUsage,
       "bufUtiliznCellSize": bufUtiliznCellSize}
)
