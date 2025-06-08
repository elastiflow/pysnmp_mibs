# SNMP MIB module (RUIJIE-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijiePingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    ruijiePingMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiePingMIBObjects_ObjectIdentity = ObjectIdentity
ruijiePingMIBObjects = _RuijiePingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1)
)
_RuijiePingTable_Object = MibTable
ruijiePingTable = _RuijiePingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiePingTable.setStatus("current")
_RuijiePingEntry_Object = MibTableRow
ruijiePingEntry = _RuijiePingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1)
)
ruijiePingEntry.setIndexNames(
    (0, "RUIJIE-PING-MIB", "ruijiePingIndex"),
)
if mibBuilder.loadTexts:
    ruijiePingEntry.setStatus("current")


class _RuijiePingIndex_Type(Integer32):
    """Custom type ruijiePingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijiePingIndex_Type.__name__ = "Integer32"
_RuijiePingIndex_Object = MibTableColumn
ruijiePingIndex = _RuijiePingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 1),
    _RuijiePingIndex_Type()
)
ruijiePingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePingIndex.setStatus("current")
_RuijiePingAddress_Type = IpAddress
_RuijiePingAddress_Object = MibTableColumn
ruijiePingAddress = _RuijiePingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 2),
    _RuijiePingAddress_Type()
)
ruijiePingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingAddress.setStatus("current")


class _RuijiePingDataLength_Type(Unsigned32):
    """Custom type ruijiePingDataLength based on Unsigned32"""
    defaultValue = 100


_RuijiePingDataLength_Type.__name__ = "Unsigned32"
_RuijiePingDataLength_Object = MibTableColumn
ruijiePingDataLength = _RuijiePingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 3),
    _RuijiePingDataLength_Type()
)
ruijiePingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingDataLength.setStatus("current")


class _RuijiePingTimes_Type(Unsigned32):
    """Custom type ruijiePingTimes based on Unsigned32"""
    defaultValue = 5


_RuijiePingTimes_Type.__name__ = "Unsigned32"
_RuijiePingTimes_Object = MibTableColumn
ruijiePingTimes = _RuijiePingTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 4),
    _RuijiePingTimes_Type()
)
ruijiePingTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingTimes.setStatus("current")


class _RuijiePingTimeOuts_Type(Unsigned32):
    """Custom type ruijiePingTimeOuts based on Unsigned32"""
    defaultValue = 2000


_RuijiePingTimeOuts_Type.__name__ = "Unsigned32"
_RuijiePingTimeOuts_Object = MibTableColumn
ruijiePingTimeOuts = _RuijiePingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 5),
    _RuijiePingTimeOuts_Type()
)
ruijiePingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingTimeOuts.setStatus("current")
_RuijiePingReturns_Type = Unsigned32
_RuijiePingReturns_Object = MibTableColumn
ruijiePingReturns = _RuijiePingReturns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 6),
    _RuijiePingReturns_Type()
)
ruijiePingReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePingReturns.setStatus("current")
_RuijiePingMaxTime_Type = Unsigned32
_RuijiePingMaxTime_Object = MibTableColumn
ruijiePingMaxTime = _RuijiePingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 7),
    _RuijiePingMaxTime_Type()
)
ruijiePingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePingMaxTime.setStatus("current")
_RuijiePingAvTime_Type = Unsigned32
_RuijiePingAvTime_Object = MibTableColumn
ruijiePingAvTime = _RuijiePingAvTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 8),
    _RuijiePingAvTime_Type()
)
ruijiePingAvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePingAvTime.setStatus("current")
_RuijiePingMinTime_Type = Unsigned32
_RuijiePingMinTime_Object = MibTableColumn
ruijiePingMinTime = _RuijiePingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 9),
    _RuijiePingMinTime_Type()
)
ruijiePingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePingMinTime.setStatus("current")
_RuijiePingCompleted_Type = TruthValue
_RuijiePingCompleted_Object = MibTableColumn
ruijiePingCompleted = _RuijiePingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 10),
    _RuijiePingCompleted_Type()
)
ruijiePingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePingCompleted.setStatus("current")
_RuijiePingEntryStauts_Type = RowStatus
_RuijiePingEntryStauts_Object = MibTableColumn
ruijiePingEntryStauts = _RuijiePingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 11),
    _RuijiePingEntryStauts_Type()
)
ruijiePingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingEntryStauts.setStatus("current")
_RuijiePingSourceIp_Type = IpAddress
_RuijiePingSourceIp_Object = MibTableColumn
ruijiePingSourceIp = _RuijiePingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 12),
    _RuijiePingSourceIp_Type()
)
ruijiePingSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingSourceIp.setStatus("current")
_RuijiePingSourceInterfaceIndex_Type = IfIndex
_RuijiePingSourceInterfaceIndex_Object = MibTableColumn
ruijiePingSourceInterfaceIndex = _RuijiePingSourceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 13),
    _RuijiePingSourceInterfaceIndex_Type()
)
ruijiePingSourceInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingSourceInterfaceIndex.setStatus("current")


class _RuijiePingTypeOfService_Type(Unsigned32):
    """Custom type ruijiePingTypeOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijiePingTypeOfService_Type.__name__ = "Unsigned32"
_RuijiePingTypeOfService_Object = MibTableColumn
ruijiePingTypeOfService = _RuijiePingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 1, 1, 1, 14),
    _RuijiePingTypeOfService_Type()
)
ruijiePingTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePingTypeOfService.setStatus("current")
_RuijiePingMIBConformance_ObjectIdentity = ObjectIdentity
ruijiePingMIBConformance = _RuijiePingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 2)
)
_RuijiePingMIBCompliances_ObjectIdentity = ObjectIdentity
ruijiePingMIBCompliances = _RuijiePingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 2, 1)
)
_RuijiePingMIBGroups_ObjectIdentity = ObjectIdentity
ruijiePingMIBGroups = _RuijiePingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 2, 2)
)
_TraceRouteMIBObjects_ObjectIdentity = ObjectIdentity
traceRouteMIBObjects = _TraceRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3)
)
_TraceRouteTable_Object = MibTable
traceRouteTable = _TraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    traceRouteTable.setStatus("current")
_TraceRouteEntry_Object = MibTableRow
traceRouteEntry = _TraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1)
)
traceRouteEntry.setIndexNames(
    (0, "RUIJIE-PING-MIB", "traceRouteIndex"),
)
if mibBuilder.loadTexts:
    traceRouteEntry.setStatus("current")


class _TraceRouteIndex_Type(Unsigned32):
    """Custom type traceRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TraceRouteIndex_Type.__name__ = "Unsigned32"
_TraceRouteIndex_Object = MibTableColumn
traceRouteIndex = _TraceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1, 1),
    _TraceRouteIndex_Type()
)
traceRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteIndex.setStatus("current")
_TraceRouteTargetAddr_Type = IpAddress
_TraceRouteTargetAddr_Object = MibTableColumn
traceRouteTargetAddr = _TraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1, 2),
    _TraceRouteTargetAddr_Type()
)
traceRouteTargetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteTargetAddr.setStatus("current")


class _TraceRouteHopCount_Type(Unsigned32):
    """Custom type traceRouteHopCount based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TraceRouteHopCount_Type.__name__ = "Unsigned32"
_TraceRouteHopCount_Object = MibTableColumn
traceRouteHopCount = _TraceRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1, 3),
    _TraceRouteHopCount_Type()
)
traceRouteHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteHopCount.setStatus("current")


class _TraceRoutePingCount_Type(Unsigned32):
    """Custom type traceRoutePingCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TraceRoutePingCount_Type.__name__ = "Unsigned32"
_TraceRoutePingCount_Object = MibTableColumn
traceRoutePingCount = _TraceRoutePingCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1, 4),
    _TraceRoutePingCount_Type()
)
traceRoutePingCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRoutePingCount.setStatus("current")


class _TraceRoutePingTimeout_Type(Unsigned32):
    """Custom type traceRoutePingTimeout based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_TraceRoutePingTimeout_Type.__name__ = "Unsigned32"
_TraceRoutePingTimeout_Object = MibTableColumn
traceRoutePingTimeout = _TraceRoutePingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1, 5),
    _TraceRoutePingTimeout_Type()
)
traceRoutePingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRoutePingTimeout.setStatus("current")
_TraceRouteRowStatus_Type = RowStatus
_TraceRouteRowStatus_Object = MibTableColumn
traceRouteRowStatus = _TraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 1, 1, 6),
    _TraceRouteRowStatus_Type()
)
traceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteRowStatus.setStatus("current")
_TraceRouteHopsTable_Object = MibTable
traceRouteHopsTable = _TraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    traceRouteHopsTable.setStatus("current")
_TraceRouteHopsEntry_Object = MibTableRow
traceRouteHopsEntry = _TraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1)
)
traceRouteHopsEntry.setIndexNames(
    (0, "RUIJIE-PING-MIB", "traceRouteIndex"),
    (0, "RUIJIE-PING-MIB", "traceRouteHopIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHopsEntry.setStatus("current")
_TraceRouteHopIndex_Type = Unsigned32
_TraceRouteHopIndex_Object = MibTableColumn
traceRouteHopIndex = _TraceRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1, 1),
    _TraceRouteHopIndex_Type()
)
traceRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopIndex.setStatus("current")
_TraceRouteHopPingIndex_Type = Unsigned32
_TraceRouteHopPingIndex_Object = MibTableColumn
traceRouteHopPingIndex = _TraceRouteHopPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1, 2),
    _TraceRouteHopPingIndex_Type()
)
traceRouteHopPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingIndex.setStatus("current")
_TraceRouteHopPingCompleted_Type = TruthValue
_TraceRouteHopPingCompleted_Object = MibTableColumn
traceRouteHopPingCompleted = _TraceRouteHopPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1, 3),
    _TraceRouteHopPingCompleted_Type()
)
traceRouteHopPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingCompleted.setStatus("current")
_TraceRouteHopPingResult_Type = TruthValue
_TraceRouteHopPingResult_Object = MibTableColumn
traceRouteHopPingResult = _TraceRouteHopPingResult_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1, 4),
    _TraceRouteHopPingResult_Type()
)
traceRouteHopPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingResult.setStatus("current")
_TraceRouteHopPingReturnTime_Type = Unsigned32
_TraceRouteHopPingReturnTime_Object = MibTableColumn
traceRouteHopPingReturnTime = _TraceRouteHopPingReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1, 5),
    _TraceRouteHopPingReturnTime_Type()
)
traceRouteHopPingReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingReturnTime.setStatus("current")
_TraceRouteHopAddr_Type = IpAddress
_TraceRouteHopAddr_Object = MibTableColumn
traceRouteHopAddr = _TraceRouteHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 3, 2, 1, 6),
    _TraceRouteHopAddr_Type()
)
traceRouteHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopAddr.setStatus("current")

# Managed Objects groups

ruijiePingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 2, 2, 1)
)
ruijiePingMIBGroup.setObjects(
      *(("RUIJIE-PING-MIB", "ruijiePingIndex"),
        ("RUIJIE-PING-MIB", "ruijiePingAddress"),
        ("RUIJIE-PING-MIB", "ruijiePingDataLength"),
        ("RUIJIE-PING-MIB", "ruijiePingTimes"),
        ("RUIJIE-PING-MIB", "ruijiePingTimeOuts"),
        ("RUIJIE-PING-MIB", "ruijiePingReturns"),
        ("RUIJIE-PING-MIB", "ruijiePingMaxTime"),
        ("RUIJIE-PING-MIB", "ruijiePingAvTime"),
        ("RUIJIE-PING-MIB", "ruijiePingMinTime"),
        ("RUIJIE-PING-MIB", "ruijiePingCompleted"),
        ("RUIJIE-PING-MIB", "ruijiePingEntryStauts"),
        ("RUIJIE-PING-MIB", "ruijiePingSourceIp"),
        ("RUIJIE-PING-MIB", "ruijiePingSourceInterfaceIndex"),
        ("RUIJIE-PING-MIB", "ruijiePingTypeOfService"))
)
if mibBuilder.loadTexts:
    ruijiePingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijiePingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 3, 2, 1, 1)
)
ruijiePingMIBCompliance.setObjects(
    ("RUIJIE-PING-MIB", "ruijiePingMIBGroup")
)
if mibBuilder.loadTexts:
    ruijiePingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PING-MIB",
    **{"ruijiePingMIB": ruijiePingMIB,
       "ruijiePingMIBObjects": ruijiePingMIBObjects,
       "ruijiePingTable": ruijiePingTable,
       "ruijiePingEntry": ruijiePingEntry,
       "ruijiePingIndex": ruijiePingIndex,
       "ruijiePingAddress": ruijiePingAddress,
       "ruijiePingDataLength": ruijiePingDataLength,
       "ruijiePingTimes": ruijiePingTimes,
       "ruijiePingTimeOuts": ruijiePingTimeOuts,
       "ruijiePingReturns": ruijiePingReturns,
       "ruijiePingMaxTime": ruijiePingMaxTime,
       "ruijiePingAvTime": ruijiePingAvTime,
       "ruijiePingMinTime": ruijiePingMinTime,
       "ruijiePingCompleted": ruijiePingCompleted,
       "ruijiePingEntryStauts": ruijiePingEntryStauts,
       "ruijiePingSourceIp": ruijiePingSourceIp,
       "ruijiePingSourceInterfaceIndex": ruijiePingSourceInterfaceIndex,
       "ruijiePingTypeOfService": ruijiePingTypeOfService,
       "ruijiePingMIBConformance": ruijiePingMIBConformance,
       "ruijiePingMIBCompliances": ruijiePingMIBCompliances,
       "ruijiePingMIBCompliance": ruijiePingMIBCompliance,
       "ruijiePingMIBGroups": ruijiePingMIBGroups,
       "ruijiePingMIBGroup": ruijiePingMIBGroup,
       "traceRouteMIBObjects": traceRouteMIBObjects,
       "traceRouteTable": traceRouteTable,
       "traceRouteEntry": traceRouteEntry,
       "traceRouteIndex": traceRouteIndex,
       "traceRouteTargetAddr": traceRouteTargetAddr,
       "traceRouteHopCount": traceRouteHopCount,
       "traceRoutePingCount": traceRoutePingCount,
       "traceRoutePingTimeout": traceRoutePingTimeout,
       "traceRouteRowStatus": traceRouteRowStatus,
       "traceRouteHopsTable": traceRouteHopsTable,
       "traceRouteHopsEntry": traceRouteHopsEntry,
       "traceRouteHopIndex": traceRouteHopIndex,
       "traceRouteHopPingIndex": traceRouteHopPingIndex,
       "traceRouteHopPingCompleted": traceRouteHopPingCompleted,
       "traceRouteHopPingResult": traceRouteHopPingResult,
       "traceRouteHopPingReturnTime": traceRouteHopPingReturnTime,
       "traceRouteHopAddr": traceRouteHopAddr}
)
