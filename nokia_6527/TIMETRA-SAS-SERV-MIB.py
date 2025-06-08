# SNMP MIB module (TIMETRA-SAS-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-SERV-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(sapBaseInfoEntry,
 sapBaseStatsEntry,
 sapEgrQosQueueStatsEntry,
 sapEncapValue,
 sapIngQosQueueInfoEntry,
 sapIngQosQueueStatsEntry,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapBaseInfoEntry",
    "sapBaseStatsEntry",
    "sapEgrQosQueueStatsEntry",
    "sapEncapValue",
    "sapIngQosQueueInfoEntry",
    "sapIngQosQueueStatsEntry",
    "sapPortId")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(TIngressBurstSize,
 TIngressCIRRate,
 TIngressPIRRate,
 TMeterMode,
 TMeterRateMode) = mibBuilder.importSymbols(
    "TIMETRA-SAS-QOS-MIB",
    "TIngressBurstSize",
    "TIngressCIRRate",
    "TIngressPIRRate",
    "TMeterMode",
    "TMeterRateMode")

(iesIfIndex,
 svcBaseInfoEntry,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfIndex",
    "svcBaseInfoEntry",
    "svcId")

(TAdaptationRule,
 TLevelOrDefault,
 TNamedItem,
 TSapIngressMeterId,
 TWeight,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TAdaptationRule",
    "TLevelOrDefault",
    "TNamedItem",
    "TSapIngressMeterId",
    "TWeight",
    "TmnxServId")


# MODULE-IDENTITY

timetraSASServicesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    timetraSASServicesMIBModule.setRevisions(
        ("1909-07-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TSapIngressAggrMeterBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(4, 2146959),
    )



class TSapIngressAggShaperRateCIRsize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 20000000),
    )



class TSapIngressAggShaperRatePIRsize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 20000000),
    )



class TSapAggShaperRateCIRsize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 20000000),
    )



class TSapAggShaperRatePIRsize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 20000000),
    )



class TQosMeterAttribute(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cbs", 0),
          ("cir", 1),
          ("cirAdaptRule", 2),
          ("mbs", 3),
          ("pir", 4),
          ("pirAdaptRule", 5),
          ("rateMode", 6),
          ("colorMode", 7))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxSASServConformance_ObjectIdentity = ObjectIdentity
tmnxSASServConformance = _TmnxSASServConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5)
)
_TmnxSASSapConformance_ObjectIdentity = ObjectIdentity
tmnxSASSapConformance = _TmnxSASSapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1)
)
_TmnxSASSapCompliances_ObjectIdentity = ObjectIdentity
tmnxSASSapCompliances = _TmnxSASSapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 1)
)
_TmnxSASSapGroups_ObjectIdentity = ObjectIdentity
tmnxSASSapGroups = _TmnxSASSapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 2)
)
_TmnxSASServGroups_ObjectIdentity = ObjectIdentity
tmnxSASServGroups = _TmnxSASServGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 2)
)
_TmnxSASServObjs_ObjectIdentity = ObjectIdentity
tmnxSASServObjs = _TmnxSASServObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8)
)
_TmnxSASSapObjs_ObjectIdentity = ObjectIdentity
tmnxSASSapObjs = _TmnxSASSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1)
)
_SapBaseStatsExtnTable_Object = MibTable
sapBaseStatsExtnTable = _SapBaseStatsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    sapBaseStatsExtnTable.setStatus("current")
_SapBaseStatsExtnEntry_Object = MibTableRow
sapBaseStatsExtnEntry = _SapBaseStatsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sapBaseStatsExtnEntry.setStatus("current")
_SapBaseStatsQosClassifiersUsed_Type = Unsigned32
_SapBaseStatsQosClassifiersUsed_Object = MibTableColumn
sapBaseStatsQosClassifiersUsed = _SapBaseStatsQosClassifiersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 1),
    _SapBaseStatsQosClassifiersUsed_Type()
)
sapBaseStatsQosClassifiersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsQosClassifiersUsed.setStatus("current")
_SapBaseStatsQosMetersUsed_Type = Unsigned32
_SapBaseStatsQosMetersUsed_Object = MibTableColumn
sapBaseStatsQosMetersUsed = _SapBaseStatsQosMetersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 2),
    _SapBaseStatsQosMetersUsed_Type()
)
sapBaseStatsQosMetersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsQosMetersUsed.setStatus("current")
_SapBaseStatsIngressForwardedPackets_Type = Counter64
_SapBaseStatsIngressForwardedPackets_Object = MibTableColumn
sapBaseStatsIngressForwardedPackets = _SapBaseStatsIngressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 3),
    _SapBaseStatsIngressForwardedPackets_Type()
)
sapBaseStatsIngressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressForwardedPackets.setStatus("current")
_SapBaseStatsIngressForwardedOctets_Type = Counter64
_SapBaseStatsIngressForwardedOctets_Object = MibTableColumn
sapBaseStatsIngressForwardedOctets = _SapBaseStatsIngressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 4),
    _SapBaseStatsIngressForwardedOctets_Type()
)
sapBaseStatsIngressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressForwardedOctets.setStatus("current")
_SapBaseStatsEgressForwardedPackets_Type = Counter64
_SapBaseStatsEgressForwardedPackets_Object = MibTableColumn
sapBaseStatsEgressForwardedPackets = _SapBaseStatsEgressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 5),
    _SapBaseStatsEgressForwardedPackets_Type()
)
sapBaseStatsEgressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressForwardedPackets.setStatus("current")
_SapBaseStatsEgressForwardedOctets_Type = Counter64
_SapBaseStatsEgressForwardedOctets_Object = MibTableColumn
sapBaseStatsEgressForwardedOctets = _SapBaseStatsEgressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 6),
    _SapBaseStatsEgressForwardedOctets_Type()
)
sapBaseStatsEgressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressForwardedOctets.setStatus("current")
_SapBaseStatsIngressExtraTagDroppedPackets_Type = Counter64
_SapBaseStatsIngressExtraTagDroppedPackets_Object = MibTableColumn
sapBaseStatsIngressExtraTagDroppedPackets = _SapBaseStatsIngressExtraTagDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 7),
    _SapBaseStatsIngressExtraTagDroppedPackets_Type()
)
sapBaseStatsIngressExtraTagDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressExtraTagDroppedPackets.setStatus("current")
_SapBaseStatsIngressExtraTagDroppedOctets_Type = Counter64
_SapBaseStatsIngressExtraTagDroppedOctets_Object = MibTableColumn
sapBaseStatsIngressExtraTagDroppedOctets = _SapBaseStatsIngressExtraTagDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 8),
    _SapBaseStatsIngressExtraTagDroppedOctets_Type()
)
sapBaseStatsIngressExtraTagDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressExtraTagDroppedOctets.setStatus("current")
_SapBaseStatsIngressDroppedPackets_Type = Counter64
_SapBaseStatsIngressDroppedPackets_Object = MibTableColumn
sapBaseStatsIngressDroppedPackets = _SapBaseStatsIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 9),
    _SapBaseStatsIngressDroppedPackets_Type()
)
sapBaseStatsIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressDroppedPackets.setStatus("current")
_SapBaseStatsIngressDroppedOctets_Type = Counter64
_SapBaseStatsIngressDroppedOctets_Object = MibTableColumn
sapBaseStatsIngressDroppedOctets = _SapBaseStatsIngressDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 1, 1, 10),
    _SapBaseStatsIngressDroppedOctets_Type()
)
sapBaseStatsIngressDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressDroppedOctets.setStatus("current")
_SapBaseInfoExtnTable_Object = MibTable
sapBaseInfoExtnTable = _SapBaseInfoExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    sapBaseInfoExtnTable.setStatus("current")
_SapBaseInfoExtnEntry_Object = MibTableRow
sapBaseInfoExtnEntry = _SapBaseInfoExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sapBaseInfoExtnEntry.setStatus("current")


class _SapBaseInfoEgressStatsPktsMode_Type(TruthValue):
    """Custom type sapBaseInfoEgressStatsPktsMode based on TruthValue"""
    defaultValue = 2


_SapBaseInfoEgressStatsPktsMode_Type.__name__ = "TruthValue"
_SapBaseInfoEgressStatsPktsMode_Object = MibTableColumn
sapBaseInfoEgressStatsPktsMode = _SapBaseInfoEgressStatsPktsMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 1),
    _SapBaseInfoEgressStatsPktsMode_Type()
)
sapBaseInfoEgressStatsPktsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoEgressStatsPktsMode.setStatus("current")


class _SapBaseInfoIngressCounterMode_Type(Integer32):
    """Custom type sapBaseInfoIngressCounterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("octet", 2))
    )


_SapBaseInfoIngressCounterMode_Type.__name__ = "Integer32"
_SapBaseInfoIngressCounterMode_Object = MibTableColumn
sapBaseInfoIngressCounterMode = _SapBaseInfoIngressCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 2),
    _SapBaseInfoIngressCounterMode_Type()
)
sapBaseInfoIngressCounterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressCounterMode.setStatus("current")


class _SapBaseInfoIngressAggregateMeterRate_Type(Integer32):
    """Custom type sapBaseInfoIngressAggregateMeterRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 20000000),
    )


_SapBaseInfoIngressAggregateMeterRate_Type.__name__ = "Integer32"
_SapBaseInfoIngressAggregateMeterRate_Object = MibTableColumn
sapBaseInfoIngressAggregateMeterRate = _SapBaseInfoIngressAggregateMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 3),
    _SapBaseInfoIngressAggregateMeterRate_Type()
)
sapBaseInfoIngressAggregateMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressAggregateMeterRate.setStatus("current")


class _SapBaseInfoIngressAggregateMeterBurst_Type(TSapIngressAggrMeterBurstSize):
    """Custom type sapBaseInfoIngressAggregateMeterBurst based on TSapIngressAggrMeterBurstSize"""
    defaultValue = -1


_SapBaseInfoIngressAggregateMeterBurst_Type.__name__ = "TSapIngressAggrMeterBurstSize"
_SapBaseInfoIngressAggregateMeterBurst_Object = MibTableColumn
sapBaseInfoIngressAggregateMeterBurst = _SapBaseInfoIngressAggregateMeterBurst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 4),
    _SapBaseInfoIngressAggregateMeterBurst_Type()
)
sapBaseInfoIngressAggregateMeterBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressAggregateMeterBurst.setStatus("current")


class _SapBaseInfoIngressWithAggregateMeter_Type(TruthValue):
    """Custom type sapBaseInfoIngressWithAggregateMeter based on TruthValue"""
    defaultValue = 2


_SapBaseInfoIngressWithAggregateMeter_Type.__name__ = "TruthValue"
_SapBaseInfoIngressWithAggregateMeter_Object = MibTableColumn
sapBaseInfoIngressWithAggregateMeter = _SapBaseInfoIngressWithAggregateMeter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 5),
    _SapBaseInfoIngressWithAggregateMeter_Type()
)
sapBaseInfoIngressWithAggregateMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressWithAggregateMeter.setStatus("current")


class _SapBaseInfoIngressExtraTagDropCount_Type(TruthValue):
    """Custom type sapBaseInfoIngressExtraTagDropCount based on TruthValue"""
    defaultValue = 2


_SapBaseInfoIngressExtraTagDropCount_Type.__name__ = "TruthValue"
_SapBaseInfoIngressExtraTagDropCount_Object = MibTableColumn
sapBaseInfoIngressExtraTagDropCount = _SapBaseInfoIngressExtraTagDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 6),
    _SapBaseInfoIngressExtraTagDropCount_Type()
)
sapBaseInfoIngressExtraTagDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressExtraTagDropCount.setStatus("current")


class _SapBaseInfoEgressStatsEnable_Type(TruthValue):
    """Custom type sapBaseInfoEgressStatsEnable based on TruthValue"""
    defaultValue = 2


_SapBaseInfoEgressStatsEnable_Type.__name__ = "TruthValue"
_SapBaseInfoEgressStatsEnable_Object = MibTableColumn
sapBaseInfoEgressStatsEnable = _SapBaseInfoEgressStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 7),
    _SapBaseInfoEgressStatsEnable_Type()
)
sapBaseInfoEgressStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoEgressStatsEnable.setStatus("current")


class _SapBaseInfoIngressStatsEnable_Type(TruthValue):
    """Custom type sapBaseInfoIngressStatsEnable based on TruthValue"""
    defaultValue = 2


_SapBaseInfoIngressStatsEnable_Type.__name__ = "TruthValue"
_SapBaseInfoIngressStatsEnable_Object = MibTableColumn
sapBaseInfoIngressStatsEnable = _SapBaseInfoIngressStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 8),
    _SapBaseInfoIngressStatsEnable_Type()
)
sapBaseInfoIngressStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressStatsEnable.setStatus("current")


class _SapBaseInfoIngressCounterType_Type(Integer32):
    """Custom type sapBaseInfoIngressCounterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-out-profile-count", 1),
          ("forward-drop-count", 2))
    )


_SapBaseInfoIngressCounterType_Type.__name__ = "Integer32"
_SapBaseInfoIngressCounterType_Object = MibTableColumn
sapBaseInfoIngressCounterType = _SapBaseInfoIngressCounterType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 9),
    _SapBaseInfoIngressCounterType_Type()
)
sapBaseInfoIngressCounterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressCounterType.setStatus("current")


class _SapBaseInfoIngressFabricPath_Type(Integer32):
    """Custom type sapBaseInfoIngressFabricPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SapBaseInfoIngressFabricPath_Type.__name__ = "Integer32"
_SapBaseInfoIngressFabricPath_Object = MibTableColumn
sapBaseInfoIngressFabricPath = _SapBaseInfoIngressFabricPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 10),
    _SapBaseInfoIngressFabricPath_Type()
)
sapBaseInfoIngressFabricPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressFabricPath.setStatus("current")


class _SapBaseInfoEthRingShgEnable_Type(TruthValue):
    """Custom type sapBaseInfoEthRingShgEnable based on TruthValue"""
    defaultValue = 2


_SapBaseInfoEthRingShgEnable_Type.__name__ = "TruthValue"
_SapBaseInfoEthRingShgEnable_Object = MibTableColumn
sapBaseInfoEthRingShgEnable = _SapBaseInfoEthRingShgEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 11),
    _SapBaseInfoEthRingShgEnable_Type()
)
sapBaseInfoEthRingShgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoEthRingShgEnable.setStatus("current")


class _SapBaseInfoIngressAggShaperRateCIR_Type(TSapIngressAggShaperRateCIRsize):
    """Custom type sapBaseInfoIngressAggShaperRateCIR based on TSapIngressAggShaperRateCIRsize"""
    defaultValue = 0


_SapBaseInfoIngressAggShaperRateCIR_Type.__name__ = "TSapIngressAggShaperRateCIRsize"
_SapBaseInfoIngressAggShaperRateCIR_Object = MibTableColumn
sapBaseInfoIngressAggShaperRateCIR = _SapBaseInfoIngressAggShaperRateCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 12),
    _SapBaseInfoIngressAggShaperRateCIR_Type()
)
sapBaseInfoIngressAggShaperRateCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressAggShaperRateCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapBaseInfoIngressAggShaperRateCIR.setUnits("kbps")


class _SapBaseInfoIngressAggShaperRatePIR_Type(TSapIngressAggShaperRatePIRsize):
    """Custom type sapBaseInfoIngressAggShaperRatePIR based on TSapIngressAggShaperRatePIRsize"""
    defaultValue = -1


_SapBaseInfoIngressAggShaperRatePIR_Type.__name__ = "TSapIngressAggShaperRatePIRsize"
_SapBaseInfoIngressAggShaperRatePIR_Object = MibTableColumn
sapBaseInfoIngressAggShaperRatePIR = _SapBaseInfoIngressAggShaperRatePIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 13),
    _SapBaseInfoIngressAggShaperRatePIR_Type()
)
sapBaseInfoIngressAggShaperRatePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoIngressAggShaperRatePIR.setStatus("current")
if mibBuilder.loadTexts:
    sapBaseInfoIngressAggShaperRatePIR.setUnits("kbps")


class _SapBaseInfoEgressAggShaperRateCIR_Type(TSapAggShaperRateCIRsize):
    """Custom type sapBaseInfoEgressAggShaperRateCIR based on TSapAggShaperRateCIRsize"""
    defaultValue = 0


_SapBaseInfoEgressAggShaperRateCIR_Type.__name__ = "TSapAggShaperRateCIRsize"
_SapBaseInfoEgressAggShaperRateCIR_Object = MibTableColumn
sapBaseInfoEgressAggShaperRateCIR = _SapBaseInfoEgressAggShaperRateCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 14),
    _SapBaseInfoEgressAggShaperRateCIR_Type()
)
sapBaseInfoEgressAggShaperRateCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoEgressAggShaperRateCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapBaseInfoEgressAggShaperRateCIR.setUnits("kbps")


class _SapBaseInfoEgressAggShaperRatePIR_Type(TSapAggShaperRatePIRsize):
    """Custom type sapBaseInfoEgressAggShaperRatePIR based on TSapAggShaperRatePIRsize"""
    defaultValue = -1


_SapBaseInfoEgressAggShaperRatePIR_Type.__name__ = "TSapAggShaperRatePIRsize"
_SapBaseInfoEgressAggShaperRatePIR_Object = MibTableColumn
sapBaseInfoEgressAggShaperRatePIR = _SapBaseInfoEgressAggShaperRatePIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 15),
    _SapBaseInfoEgressAggShaperRatePIR_Type()
)
sapBaseInfoEgressAggShaperRatePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapBaseInfoEgressAggShaperRatePIR.setStatus("current")
if mibBuilder.loadTexts:
    sapBaseInfoEgressAggShaperRatePIR.setUnits("kbps")


class _SapEgressAggRateLimitCIR_Type(Integer32):
    """Custom type sapEgressAggRateLimitCIR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SapEgressAggRateLimitCIR_Type.__name__ = "Integer32"
_SapEgressAggRateLimitCIR_Object = MibTableColumn
sapEgressAggRateLimitCIR = _SapEgressAggRateLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 16),
    _SapEgressAggRateLimitCIR_Type()
)
sapEgressAggRateLimitCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapEgressAggRateLimitCIR.setStatus("current")


class _SapEgressAggRateLimitPIR_Type(Integer32):
    """Custom type sapEgressAggRateLimitPIR based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_SapEgressAggRateLimitPIR_Type.__name__ = "Integer32"
_SapEgressAggRateLimitPIR_Object = MibTableColumn
sapEgressAggRateLimitPIR = _SapEgressAggRateLimitPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 2, 1, 17),
    _SapEgressAggRateLimitPIR_Type()
)
sapEgressAggRateLimitPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapEgressAggRateLimitPIR.setStatus("current")
_SapEgrQosQueueStatsExtnTable_Object = MibTable
sapEgrQosQueueStatsExtnTable = _SapEgrQosQueueStatsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsExtnTable.setStatus("current")
_SapEgrQosQueueStatsExtnEntry_Object = MibTableRow
sapEgrQosQueueStatsExtnEntry = _SapEgrQosQueueStatsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsExtnEntry.setStatus("current")
_SapEgrQosQueueStatsFwdPkts_Type = Counter64
_SapEgrQosQueueStatsFwdPkts_Object = MibTableColumn
sapEgrQosQueueStatsFwdPkts = _SapEgrQosQueueStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1, 1),
    _SapEgrQosQueueStatsFwdPkts_Type()
)
sapEgrQosQueueStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsFwdPkts.setStatus("current")
_SapEgrQosQueueStatsFwdOcts_Type = Counter64
_SapEgrQosQueueStatsFwdOcts_Object = MibTableColumn
sapEgrQosQueueStatsFwdOcts = _SapEgrQosQueueStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1, 2),
    _SapEgrQosQueueStatsFwdOcts_Type()
)
sapEgrQosQueueStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsFwdOcts.setStatus("current")
_SapEgrQosQueueStatsInprofDroPkts_Type = Counter64
_SapEgrQosQueueStatsInprofDroPkts_Object = MibTableColumn
sapEgrQosQueueStatsInprofDroPkts = _SapEgrQosQueueStatsInprofDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1, 3),
    _SapEgrQosQueueStatsInprofDroPkts_Type()
)
sapEgrQosQueueStatsInprofDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsInprofDroPkts.setStatus("current")
_SapEgrQosQueueStatsInprofDroOcts_Type = Counter64
_SapEgrQosQueueStatsInprofDroOcts_Object = MibTableColumn
sapEgrQosQueueStatsInprofDroOcts = _SapEgrQosQueueStatsInprofDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1, 4),
    _SapEgrQosQueueStatsInprofDroOcts_Type()
)
sapEgrQosQueueStatsInprofDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsInprofDroOcts.setStatus("current")
_SapEgrQosQueueStatsOutprofDroPkts_Type = Counter64
_SapEgrQosQueueStatsOutprofDroPkts_Object = MibTableColumn
sapEgrQosQueueStatsOutprofDroPkts = _SapEgrQosQueueStatsOutprofDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1, 5),
    _SapEgrQosQueueStatsOutprofDroPkts_Type()
)
sapEgrQosQueueStatsOutprofDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsOutprofDroPkts.setStatus("current")
_SapEgrQosQueueStatsOutprofDroOcts_Type = Counter64
_SapEgrQosQueueStatsOutprofDroOcts_Object = MibTableColumn
sapEgrQosQueueStatsOutprofDroOcts = _SapEgrQosQueueStatsOutprofDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 3, 1, 6),
    _SapEgrQosQueueStatsOutprofDroOcts_Type()
)
sapEgrQosQueueStatsOutprofDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsOutprofDroOcts.setStatus("current")
_SapIngQosQueueStatsExtnTable_Object = MibTable
sapIngQosQueueStatsExtnTable = _SapIngQosQueueStatsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    sapIngQosQueueStatsExtnTable.setStatus("current")
_SapIngQosQueueStatsExtnEntry_Object = MibTableRow
sapIngQosQueueStatsExtnEntry = _SapIngQosQueueStatsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sapIngQosQueueStatsExtnEntry.setStatus("current")
_SapIngQosQueueStatsFwdPkts_Type = Counter64
_SapIngQosQueueStatsFwdPkts_Object = MibTableColumn
sapIngQosQueueStatsFwdPkts = _SapIngQosQueueStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1, 1),
    _SapIngQosQueueStatsFwdPkts_Type()
)
sapIngQosQueueStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsFwdPkts.setStatus("current")
_SapIngQosQueueStatsFwdOcts_Type = Counter64
_SapIngQosQueueStatsFwdOcts_Object = MibTableColumn
sapIngQosQueueStatsFwdOcts = _SapIngQosQueueStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1, 2),
    _SapIngQosQueueStatsFwdOcts_Type()
)
sapIngQosQueueStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsFwdOcts.setStatus("current")
_SapIngQosQueueStatsInprofDroPkts_Type = Counter64
_SapIngQosQueueStatsInprofDroPkts_Object = MibTableColumn
sapIngQosQueueStatsInprofDroPkts = _SapIngQosQueueStatsInprofDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1, 3),
    _SapIngQosQueueStatsInprofDroPkts_Type()
)
sapIngQosQueueStatsInprofDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsInprofDroPkts.setStatus("current")
_SapIngQosQueueStatsInprofDroOcts_Type = Counter64
_SapIngQosQueueStatsInprofDroOcts_Object = MibTableColumn
sapIngQosQueueStatsInprofDroOcts = _SapIngQosQueueStatsInprofDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1, 4),
    _SapIngQosQueueStatsInprofDroOcts_Type()
)
sapIngQosQueueStatsInprofDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsInprofDroOcts.setStatus("current")
_SapIngQosQueueStatsOutprofDroPkts_Type = Counter64
_SapIngQosQueueStatsOutprofDroPkts_Object = MibTableColumn
sapIngQosQueueStatsOutprofDroPkts = _SapIngQosQueueStatsOutprofDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1, 5),
    _SapIngQosQueueStatsOutprofDroPkts_Type()
)
sapIngQosQueueStatsOutprofDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOutprofDroPkts.setStatus("current")
_SapIngQosQueueStatsOutprofDroOcts_Type = Counter64
_SapIngQosQueueStatsOutprofDroOcts_Object = MibTableColumn
sapIngQosQueueStatsOutprofDroOcts = _SapIngQosQueueStatsOutprofDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 4, 1, 6),
    _SapIngQosQueueStatsOutprofDroOcts_Type()
)
sapIngQosQueueStatsOutprofDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOutprofDroOcts.setStatus("current")
_SapIngQosMeterInfoTable_Object = MibTable
sapIngQosMeterInfoTable = _SapIngQosMeterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    sapIngQosMeterInfoTable.setStatus("current")
_SapIngQosMeterInfoEntry_Object = MibTableRow
sapIngQosMeterInfoEntry = _SapIngQosMeterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1)
)
sapIngQosMeterInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-SAS-SERV-MIB", "sapIngQosMeterOvId"),
)
if mibBuilder.loadTexts:
    sapIngQosMeterInfoEntry.setStatus("current")
_SapIngQosMeterOvId_Type = TSapIngressMeterId
_SapIngQosMeterOvId_Object = MibTableColumn
sapIngQosMeterOvId = _SapIngQosMeterOvId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 1),
    _SapIngQosMeterOvId_Type()
)
sapIngQosMeterOvId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIngQosMeterOvId.setStatus("current")
_SapIngQosMeterRowStatus_Type = RowStatus
_SapIngQosMeterRowStatus_Object = MibTableColumn
sapIngQosMeterRowStatus = _SapIngQosMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 2),
    _SapIngQosMeterRowStatus_Type()
)
sapIngQosMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterRowStatus.setStatus("current")
_SapIngQosMeterLastMgmtChange_Type = TimeStamp
_SapIngQosMeterLastMgmtChange_Object = MibTableColumn
sapIngQosMeterLastMgmtChange = _SapIngQosMeterLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 3),
    _SapIngQosMeterLastMgmtChange_Type()
)
sapIngQosMeterLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterLastMgmtChange.setStatus("current")
_SapIngQosMeterOverrideFlags_Type = TQosMeterAttribute
_SapIngQosMeterOverrideFlags_Object = MibTableColumn
sapIngQosMeterOverrideFlags = _SapIngQosMeterOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 4),
    _SapIngQosMeterOverrideFlags_Type()
)
sapIngQosMeterOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterOverrideFlags.setStatus("current")


class _SapIngQosMeterAdminCBS_Type(TIngressBurstSize):
    """Custom type sapIngQosMeterAdminCBS based on TIngressBurstSize"""
    defaultValue = -1


_SapIngQosMeterAdminCBS_Type.__name__ = "TIngressBurstSize"
_SapIngQosMeterAdminCBS_Object = MibTableColumn
sapIngQosMeterAdminCBS = _SapIngQosMeterAdminCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 5),
    _SapIngQosMeterAdminCBS_Type()
)
sapIngQosMeterAdminCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminCBS.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminCBS.setUnits("kilo bytes")


class _SapIngQosMeterAdminMBS_Type(TIngressBurstSize):
    """Custom type sapIngQosMeterAdminMBS based on TIngressBurstSize"""
    defaultValue = -1


_SapIngQosMeterAdminMBS_Type.__name__ = "TIngressBurstSize"
_SapIngQosMeterAdminMBS_Object = MibTableColumn
sapIngQosMeterAdminMBS = _SapIngQosMeterAdminMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 6),
    _SapIngQosMeterAdminMBS_Type()
)
sapIngQosMeterAdminMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminMBS.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminMBS.setUnits("kilo bytes")


class _SapIngQosMeterCIRAdaptation_Type(TAdaptationRule):
    """Custom type sapIngQosMeterCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_SapIngQosMeterCIRAdaptation_Type.__name__ = "TAdaptationRule"
_SapIngQosMeterCIRAdaptation_Object = MibTableColumn
sapIngQosMeterCIRAdaptation = _SapIngQosMeterCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 7),
    _SapIngQosMeterCIRAdaptation_Type()
)
sapIngQosMeterCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterCIRAdaptation.setStatus("current")


class _SapIngQosMeterPIRAdaptation_Type(TAdaptationRule):
    """Custom type sapIngQosMeterPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_SapIngQosMeterPIRAdaptation_Type.__name__ = "TAdaptationRule"
_SapIngQosMeterPIRAdaptation_Object = MibTableColumn
sapIngQosMeterPIRAdaptation = _SapIngQosMeterPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 8),
    _SapIngQosMeterPIRAdaptation_Type()
)
sapIngQosMeterPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterPIRAdaptation.setStatus("current")


class _SapIngQosMeterAdminPIR_Type(TIngressPIRRate):
    """Custom type sapIngQosMeterAdminPIR based on TIngressPIRRate"""
    defaultValue = -1


_SapIngQosMeterAdminPIR_Type.__name__ = "TIngressPIRRate"
_SapIngQosMeterAdminPIR_Object = MibTableColumn
sapIngQosMeterAdminPIR = _SapIngQosMeterAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 9),
    _SapIngQosMeterAdminPIR_Type()
)
sapIngQosMeterAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminPIR.setUnits("kilo bits per second")


class _SapIngQosMeterAdminCIR_Type(TIngressCIRRate):
    """Custom type sapIngQosMeterAdminCIR based on TIngressCIRRate"""
    defaultValue = -1


_SapIngQosMeterAdminCIR_Type.__name__ = "TIngressCIRRate"
_SapIngQosMeterAdminCIR_Object = MibTableColumn
sapIngQosMeterAdminCIR = _SapIngQosMeterAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 10),
    _SapIngQosMeterAdminCIR_Type()
)
sapIngQosMeterAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosMeterAdminCIR.setUnits("kilo bits per second")


class _SapIngQosMeterRateMode_Type(TMeterRateMode):
    """Custom type sapIngQosMeterRateMode based on TMeterRateMode"""
    defaultValue = 3


_SapIngQosMeterRateMode_Type.__name__ = "TMeterRateMode"
_SapIngQosMeterRateMode_Object = MibTableColumn
sapIngQosMeterRateMode = _SapIngQosMeterRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 11),
    _SapIngQosMeterRateMode_Type()
)
sapIngQosMeterRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterRateMode.setStatus("current")


class _SapIngQosMeterOperPIR_Type(TIngressPIRRate):
    """Custom type sapIngQosMeterOperPIR based on TIngressPIRRate"""
    defaultValue = -1


_SapIngQosMeterOperPIR_Type.__name__ = "TIngressPIRRate"
_SapIngQosMeterOperPIR_Object = MibTableColumn
sapIngQosMeterOperPIR = _SapIngQosMeterOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 12),
    _SapIngQosMeterOperPIR_Type()
)
sapIngQosMeterOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterOperPIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosMeterOperPIR.setUnits("kilo bits per second")


class _SapIngQosMeterOperCIR_Type(TIngressCIRRate):
    """Custom type sapIngQosMeterOperCIR based on TIngressCIRRate"""
    defaultValue = -1


_SapIngQosMeterOperCIR_Type.__name__ = "TIngressCIRRate"
_SapIngQosMeterOperCIR_Object = MibTableColumn
sapIngQosMeterOperCIR = _SapIngQosMeterOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 13),
    _SapIngQosMeterOperCIR_Type()
)
sapIngQosMeterOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosMeterOperCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosMeterOperCIR.setUnits("kilo bits per second")


class _SapIngQosMeterRateColorMode_Type(Integer32):
    """Custom type sapIngQosMeterRateColorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-blind", 2))
    )


_SapIngQosMeterRateColorMode_Type.__name__ = "Integer32"
_SapIngQosMeterRateColorMode_Object = MibTableColumn
sapIngQosMeterRateColorMode = _SapIngQosMeterRateColorMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 5, 1, 14),
    _SapIngQosMeterRateColorMode_Type()
)
sapIngQosMeterRateColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosMeterRateColorMode.setStatus("current")
_SapIngQosQueueInfoExtnTable_Object = MibTable
sapIngQosQueueInfoExtnTable = _SapIngQosQueueInfoExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    sapIngQosQueueInfoExtnTable.setStatus("current")
_SapIngQosQueueInfoExtnEntry_Object = MibTableRow
sapIngQosQueueInfoExtnEntry = _SapIngQosQueueInfoExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sapIngQosQueueInfoExtnEntry.setStatus("current")


class _SapIngQosQPolicyName_Type(TNamedItem):
    """Custom type sapIngQosQPolicyName based on TNamedItem"""
    defaultValue = OctetString("default")


_SapIngQosQPolicyName_Type.__name__ = "TNamedItem"
_SapIngQosQPolicyName_Object = MibTableColumn
sapIngQosQPolicyName = _SapIngQosQPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 6, 1, 1),
    _SapIngQosQPolicyName_Type()
)
sapIngQosQPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQPolicyName.setStatus("current")


class _SapIngQosQPIRWeight_Type(TWeight):
    """Custom type sapIngQosQPIRWeight based on TWeight"""
    defaultValue = 1


_SapIngQosQPIRWeight_Type.__name__ = "TWeight"
_SapIngQosQPIRWeight_Object = MibTableColumn
sapIngQosQPIRWeight = _SapIngQosQPIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 6, 1, 2),
    _SapIngQosQPIRWeight_Type()
)
sapIngQosQPIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQPIRWeight.setStatus("current")


class _SapIngQosQCIRLevel_Type(TLevelOrDefault):
    """Custom type sapIngQosQCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_SapIngQosQCIRLevel_Type.__name__ = "TLevelOrDefault"
_SapIngQosQCIRLevel_Object = MibTableColumn
sapIngQosQCIRLevel = _SapIngQosQCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 1, 6, 1, 3),
    _SapIngQosQCIRLevel_Type()
)
sapIngQosQCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQCIRLevel.setStatus("current")
_TmnxSASSvcObjs_ObjectIdentity = ObjectIdentity
tmnxSASSvcObjs = _TmnxSASSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2)
)
_SvcBaseInfoExtnTable_Object = MibTable
svcBaseInfoExtnTable = _SvcBaseInfoExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    svcBaseInfoExtnTable.setStatus("current")
_SvcBaseInfoExtnEntry_Object = MibTableRow
svcBaseInfoExtnEntry = _SvcBaseInfoExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    svcBaseInfoExtnEntry.setStatus("current")


class _SvcMtuCheck_Type(TruthValue):
    """Custom type svcMtuCheck based on TruthValue"""
    defaultValue = 1


_SvcMtuCheck_Type.__name__ = "TruthValue"
_SvcMtuCheck_Object = MibTableColumn
svcMtuCheck = _SvcMtuCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 1),
    _SvcMtuCheck_Type()
)
svcMtuCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMtuCheck.setStatus("current")


class _SvcSapType_Type(Integer32):
    """Custom type svcSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("null-star", 1),
          ("dot1q", 2),
          ("dot1q-preserve", 3),
          ("any", 4),
          ("dot1q-range", 5),
          ("qinq-inner-tag-preserve", 6))
    )


_SvcSapType_Type.__name__ = "Integer32"
_SvcSapType_Object = MibTableColumn
svcSapType = _SvcSapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 2),
    _SvcSapType_Type()
)
svcSapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcSapType.setStatus("current")


class _SvcUplinkType_Type(Integer32):
    """Custom type svcUplinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("l2", 1),
          ("mpls", 2))
    )


_SvcUplinkType_Type.__name__ = "Integer32"
_SvcUplinkType_Object = MibTableColumn
svcUplinkType = _SvcUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 3),
    _SvcUplinkType_Type()
)
svcUplinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcUplinkType.setStatus("current")


class _SvcCustomerVid_Type(Integer32):
    """Custom type svcCustomerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SvcCustomerVid_Type.__name__ = "Integer32"
_SvcCustomerVid_Object = MibTableColumn
svcCustomerVid = _SvcCustomerVid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 4),
    _SvcCustomerVid_Type()
)
svcCustomerVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcCustomerVid.setStatus("current")


class _SvcEpipeType_Type(Integer32):
    """Custom type svcEpipeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pbbepipe", 2))
    )


_SvcEpipeType_Type.__name__ = "Integer32"
_SvcEpipeType_Object = MibTableColumn
svcEpipeType = _SvcEpipeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 5),
    _SvcEpipeType_Type()
)
svcEpipeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEpipeType.setStatus("current")


class _SvcAllowL2ptXstpBpdu_Type(Integer32):
    """Custom type svcAllowL2ptXstpBpdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("enable", 1),
          ("disable", 2))
    )


_SvcAllowL2ptXstpBpdu_Type.__name__ = "Integer32"
_SvcAllowL2ptXstpBpdu_Object = MibTableColumn
svcAllowL2ptXstpBpdu = _SvcAllowL2ptXstpBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 6),
    _SvcAllowL2ptXstpBpdu_Type()
)
svcAllowL2ptXstpBpdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcAllowL2ptXstpBpdu.setStatus("current")


class _SvcbVplsVid_Type(Integer32):
    """Custom type svcbVplsVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SvcbVplsVid_Type.__name__ = "Integer32"
_SvcbVplsVid_Object = MibTableColumn
svcbVplsVid = _SvcbVplsVid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 2, 1, 1, 7),
    _SvcbVplsVid_Type()
)
svcbVplsVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcbVplsVid.setStatus("current")
_TmnxSASSvcTraps_ObjectIdentity = ObjectIdentity
tmnxSASSvcTraps = _TmnxSASSvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 3)
)
_TmnxSASSvcNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSASSvcNotifyObjs = _TmnxSASSvcNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 4)
)
_SvcVplsId_Type = TmnxServId
_SvcVplsId_Object = MibScalar
svcVplsId = _SvcVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 4, 1),
    _SvcVplsId_Type()
)
svcVplsId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcVplsId.setStatus("current")
_SvcIesId_Type = TmnxServId
_SvcIesId_Object = MibScalar
svcIesId = _SvcIesId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 4, 2),
    _SvcIesId_Type()
)
svcIesId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcIesId.setStatus("current")
sapBaseStatsEntry.registerAugmentions(
    ("TIMETRA-SAS-SERV-MIB",
     "sapBaseStatsExtnEntry")
)
sapBaseStatsExtnEntry.setIndexNames(*sapBaseStatsEntry.getIndexNames())
sapBaseInfoEntry.registerAugmentions(
    ("TIMETRA-SAS-SERV-MIB",
     "sapBaseInfoExtnEntry")
)
sapBaseInfoExtnEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sapEgrQosQueueStatsEntry.registerAugmentions(
    ("TIMETRA-SAS-SERV-MIB",
     "sapEgrQosQueueStatsExtnEntry")
)
sapEgrQosQueueStatsExtnEntry.setIndexNames(*sapEgrQosQueueStatsEntry.getIndexNames())
sapIngQosQueueStatsEntry.registerAugmentions(
    ("TIMETRA-SAS-SERV-MIB",
     "sapIngQosQueueStatsExtnEntry")
)
sapIngQosQueueStatsExtnEntry.setIndexNames(*sapIngQosQueueStatsEntry.getIndexNames())
sapIngQosQueueInfoEntry.registerAugmentions(
    ("TIMETRA-SAS-SERV-MIB",
     "sapIngQosQueueInfoExtnEntry")
)
sapIngQosQueueInfoExtnEntry.setIndexNames(*sapIngQosQueueInfoEntry.getIndexNames())
svcBaseInfoEntry.registerAugmentions(
    ("TIMETRA-SAS-SERV-MIB",
     "svcBaseInfoExtnEntry")
)
svcBaseInfoExtnEntry.setIndexNames(*svcBaseInfoEntry.getIndexNames())

# Managed Objects groups

tmnxSapGlobalV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 2, 28)
)
tmnxSapGlobalV1v0Group.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "sapBaseStatsQosClassifiersUsed"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsQosMetersUsed"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoEgressStatsPktsMode"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressCounterMode"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressAggregateMeterRate"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressAggregateMeterBurst"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressWithAggregateMeter"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressExtraTagDropCount"),
        ("TIMETRA-SAS-SERV-MIB", "svcMtuCheck"),
        ("TIMETRA-SAS-SERV-MIB", "svcSapType"),
        ("TIMETRA-SAS-SERV-MIB", "svcUplinkType"),
        ("TIMETRA-SAS-SERV-MIB", "svcCustomerVid"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressForwardedPackets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressForwardedOctets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsEgressForwardedPackets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsEgressForwardedOctets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressExtraTagDroppedPackets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressExtraTagDroppedOctets"))
)
if mibBuilder.loadTexts:
    tmnxSapGlobalV1v0Group.setStatus("current")

tmnxSasSapQosV2v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 2, 29)
)
tmnxSasSapQosV2v0Group.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "sapEgrQosQueueStatsFwdPkts"),
        ("TIMETRA-SAS-SERV-MIB", "sapEgrQosQueueStatsFwdOcts"),
        ("TIMETRA-SAS-SERV-MIB", "sapEgrQosQueueStatsInprofDroPkts"),
        ("TIMETRA-SAS-SERV-MIB", "sapEgrQosQueueStatsInprofDroOcts"),
        ("TIMETRA-SAS-SERV-MIB", "sapEgrQosQueueStatsOutprofDroPkts"),
        ("TIMETRA-SAS-SERV-MIB", "sapEgrQosQueueStatsOutprofDroOcts"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosQueueStatsFwdPkts"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosQueueStatsFwdOcts"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosQueueStatsInprofDroPkts"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosQueueStatsInprofDroOcts"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosQueueStatsOutprofDroPkts"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosQueueStatsOutprofDroOcts"))
)
if mibBuilder.loadTexts:
    tmnxSasSapQosV2v0Group.setStatus("current")

tmnxSapGlobalV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 2, 30)
)
tmnxSapGlobalV3v0Group.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "sapBaseStatsQosClassifiersUsed"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsQosMetersUsed"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoEgressStatsPktsMode"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoEgressStatsEnable"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressStatsEnable"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressCounterMode"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressAggregateMeterRate"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressAggregateMeterBurst"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressWithAggregateMeter"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressExtraTagDropCount"),
        ("TIMETRA-SAS-SERV-MIB", "svcMtuCheck"),
        ("TIMETRA-SAS-SERV-MIB", "svcEpipeType"),
        ("TIMETRA-SAS-SERV-MIB", "svcSapType"),
        ("TIMETRA-SAS-SERV-MIB", "svcUplinkType"),
        ("TIMETRA-SAS-SERV-MIB", "svcCustomerVid"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressForwardedPackets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressForwardedOctets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsEgressForwardedPackets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsEgressForwardedOctets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressExtraTagDroppedPackets"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseStatsIngressExtraTagDroppedOctets"))
)
if mibBuilder.loadTexts:
    tmnxSapGlobalV3v0Group.setStatus("current")

tmnxSapGlobalV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 2, 31)
)
tmnxSapGlobalV4v0Group.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressCounterType"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressFabricPath"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoEthRingShgEnable"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressAggShaperRateCIR"),
        ("TIMETRA-SAS-SERV-MIB", "sapBaseInfoIngressAggShaperRatePIR"))
)
if mibBuilder.loadTexts:
    tmnxSapGlobalV4v0Group.setStatus("current")

tmnxSapGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 2, 32)
)
tmnxSapGlobalV5v0Group.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterRowStatus"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterLastMgmtChange"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterOverrideFlags"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterAdminCBS"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterAdminMBS"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterCIRAdaptation"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterPIRAdaptation"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterAdminPIR"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterAdminCIR"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterRateMode"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterOperPIR"),
        ("TIMETRA-SAS-SERV-MIB", "sapIngQosMeterOperCIR"))
)
if mibBuilder.loadTexts:
    tmnxSapGlobalV5v0Group.setStatus("current")


# Notification objects

svcVplssvcBoundToIESSvc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 8, 3, 1)
)
svcVplssvcBoundToIESSvc.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "svcVplsId"),
        ("TIMETRA-SAS-SERV-MIB", "svcIesId"),
        ("TIMETRA-SERV-MIB", "iesIfIndex"))
)
if mibBuilder.loadTexts:
    svcVplssvcBoundToIESSvc.setStatus(
        "current"
    )


# Notifications groups

tmnxSASSvcNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 2, 1)
)
tmnxSASSvcNotifyGroup.setObjects(
    ("TIMETRA-SAS-SERV-MIB", "svcVplssvcBoundToIESSvc")
)
if mibBuilder.loadTexts:
    tmnxSASSvcNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSap72100V1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 5, 1, 1, 1)
)
tmnxSap72100V1v0Compliance.setObjects(
      *(("TIMETRA-SAS-SERV-MIB", "tmnxSapGlobalV1v0Group"),
        ("TIMETRA-SAS-SERV-MIB", "tmnxSasSapQosV2v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSap72100V1v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-SERV-MIB",
    **{"TSapIngressAggrMeterBurstSize": TSapIngressAggrMeterBurstSize,
       "TSapIngressAggShaperRateCIRsize": TSapIngressAggShaperRateCIRsize,
       "TSapIngressAggShaperRatePIRsize": TSapIngressAggShaperRatePIRsize,
       "TSapAggShaperRateCIRsize": TSapAggShaperRateCIRsize,
       "TSapAggShaperRatePIRsize": TSapAggShaperRatePIRsize,
       "TQosMeterAttribute": TQosMeterAttribute,
       "timetraSASServicesMIBModule": timetraSASServicesMIBModule,
       "tmnxSASServConformance": tmnxSASServConformance,
       "tmnxSASSapConformance": tmnxSASSapConformance,
       "tmnxSASSapCompliances": tmnxSASSapCompliances,
       "tmnxSap72100V1v0Compliance": tmnxSap72100V1v0Compliance,
       "tmnxSASSapGroups": tmnxSASSapGroups,
       "tmnxSapGlobalV1v0Group": tmnxSapGlobalV1v0Group,
       "tmnxSasSapQosV2v0Group": tmnxSasSapQosV2v0Group,
       "tmnxSapGlobalV3v0Group": tmnxSapGlobalV3v0Group,
       "tmnxSapGlobalV4v0Group": tmnxSapGlobalV4v0Group,
       "tmnxSapGlobalV5v0Group": tmnxSapGlobalV5v0Group,
       "tmnxSASServGroups": tmnxSASServGroups,
       "tmnxSASSvcNotifyGroup": tmnxSASSvcNotifyGroup,
       "tmnxSASServObjs": tmnxSASServObjs,
       "tmnxSASSapObjs": tmnxSASSapObjs,
       "sapBaseStatsExtnTable": sapBaseStatsExtnTable,
       "sapBaseStatsExtnEntry": sapBaseStatsExtnEntry,
       "sapBaseStatsQosClassifiersUsed": sapBaseStatsQosClassifiersUsed,
       "sapBaseStatsQosMetersUsed": sapBaseStatsQosMetersUsed,
       "sapBaseStatsIngressForwardedPackets": sapBaseStatsIngressForwardedPackets,
       "sapBaseStatsIngressForwardedOctets": sapBaseStatsIngressForwardedOctets,
       "sapBaseStatsEgressForwardedPackets": sapBaseStatsEgressForwardedPackets,
       "sapBaseStatsEgressForwardedOctets": sapBaseStatsEgressForwardedOctets,
       "sapBaseStatsIngressExtraTagDroppedPackets": sapBaseStatsIngressExtraTagDroppedPackets,
       "sapBaseStatsIngressExtraTagDroppedOctets": sapBaseStatsIngressExtraTagDroppedOctets,
       "sapBaseStatsIngressDroppedPackets": sapBaseStatsIngressDroppedPackets,
       "sapBaseStatsIngressDroppedOctets": sapBaseStatsIngressDroppedOctets,
       "sapBaseInfoExtnTable": sapBaseInfoExtnTable,
       "sapBaseInfoExtnEntry": sapBaseInfoExtnEntry,
       "sapBaseInfoEgressStatsPktsMode": sapBaseInfoEgressStatsPktsMode,
       "sapBaseInfoIngressCounterMode": sapBaseInfoIngressCounterMode,
       "sapBaseInfoIngressAggregateMeterRate": sapBaseInfoIngressAggregateMeterRate,
       "sapBaseInfoIngressAggregateMeterBurst": sapBaseInfoIngressAggregateMeterBurst,
       "sapBaseInfoIngressWithAggregateMeter": sapBaseInfoIngressWithAggregateMeter,
       "sapBaseInfoIngressExtraTagDropCount": sapBaseInfoIngressExtraTagDropCount,
       "sapBaseInfoEgressStatsEnable": sapBaseInfoEgressStatsEnable,
       "sapBaseInfoIngressStatsEnable": sapBaseInfoIngressStatsEnable,
       "sapBaseInfoIngressCounterType": sapBaseInfoIngressCounterType,
       "sapBaseInfoIngressFabricPath": sapBaseInfoIngressFabricPath,
       "sapBaseInfoEthRingShgEnable": sapBaseInfoEthRingShgEnable,
       "sapBaseInfoIngressAggShaperRateCIR": sapBaseInfoIngressAggShaperRateCIR,
       "sapBaseInfoIngressAggShaperRatePIR": sapBaseInfoIngressAggShaperRatePIR,
       "sapBaseInfoEgressAggShaperRateCIR": sapBaseInfoEgressAggShaperRateCIR,
       "sapBaseInfoEgressAggShaperRatePIR": sapBaseInfoEgressAggShaperRatePIR,
       "sapEgressAggRateLimitCIR": sapEgressAggRateLimitCIR,
       "sapEgressAggRateLimitPIR": sapEgressAggRateLimitPIR,
       "sapEgrQosQueueStatsExtnTable": sapEgrQosQueueStatsExtnTable,
       "sapEgrQosQueueStatsExtnEntry": sapEgrQosQueueStatsExtnEntry,
       "sapEgrQosQueueStatsFwdPkts": sapEgrQosQueueStatsFwdPkts,
       "sapEgrQosQueueStatsFwdOcts": sapEgrQosQueueStatsFwdOcts,
       "sapEgrQosQueueStatsInprofDroPkts": sapEgrQosQueueStatsInprofDroPkts,
       "sapEgrQosQueueStatsInprofDroOcts": sapEgrQosQueueStatsInprofDroOcts,
       "sapEgrQosQueueStatsOutprofDroPkts": sapEgrQosQueueStatsOutprofDroPkts,
       "sapEgrQosQueueStatsOutprofDroOcts": sapEgrQosQueueStatsOutprofDroOcts,
       "sapIngQosQueueStatsExtnTable": sapIngQosQueueStatsExtnTable,
       "sapIngQosQueueStatsExtnEntry": sapIngQosQueueStatsExtnEntry,
       "sapIngQosQueueStatsFwdPkts": sapIngQosQueueStatsFwdPkts,
       "sapIngQosQueueStatsFwdOcts": sapIngQosQueueStatsFwdOcts,
       "sapIngQosQueueStatsInprofDroPkts": sapIngQosQueueStatsInprofDroPkts,
       "sapIngQosQueueStatsInprofDroOcts": sapIngQosQueueStatsInprofDroOcts,
       "sapIngQosQueueStatsOutprofDroPkts": sapIngQosQueueStatsOutprofDroPkts,
       "sapIngQosQueueStatsOutprofDroOcts": sapIngQosQueueStatsOutprofDroOcts,
       "sapIngQosMeterInfoTable": sapIngQosMeterInfoTable,
       "sapIngQosMeterInfoEntry": sapIngQosMeterInfoEntry,
       "sapIngQosMeterOvId": sapIngQosMeterOvId,
       "sapIngQosMeterRowStatus": sapIngQosMeterRowStatus,
       "sapIngQosMeterLastMgmtChange": sapIngQosMeterLastMgmtChange,
       "sapIngQosMeterOverrideFlags": sapIngQosMeterOverrideFlags,
       "sapIngQosMeterAdminCBS": sapIngQosMeterAdminCBS,
       "sapIngQosMeterAdminMBS": sapIngQosMeterAdminMBS,
       "sapIngQosMeterCIRAdaptation": sapIngQosMeterCIRAdaptation,
       "sapIngQosMeterPIRAdaptation": sapIngQosMeterPIRAdaptation,
       "sapIngQosMeterAdminPIR": sapIngQosMeterAdminPIR,
       "sapIngQosMeterAdminCIR": sapIngQosMeterAdminCIR,
       "sapIngQosMeterRateMode": sapIngQosMeterRateMode,
       "sapIngQosMeterOperPIR": sapIngQosMeterOperPIR,
       "sapIngQosMeterOperCIR": sapIngQosMeterOperCIR,
       "sapIngQosMeterRateColorMode": sapIngQosMeterRateColorMode,
       "sapIngQosQueueInfoExtnTable": sapIngQosQueueInfoExtnTable,
       "sapIngQosQueueInfoExtnEntry": sapIngQosQueueInfoExtnEntry,
       "sapIngQosQPolicyName": sapIngQosQPolicyName,
       "sapIngQosQPIRWeight": sapIngQosQPIRWeight,
       "sapIngQosQCIRLevel": sapIngQosQCIRLevel,
       "tmnxSASSvcObjs": tmnxSASSvcObjs,
       "svcBaseInfoExtnTable": svcBaseInfoExtnTable,
       "svcBaseInfoExtnEntry": svcBaseInfoExtnEntry,
       "svcMtuCheck": svcMtuCheck,
       "svcSapType": svcSapType,
       "svcUplinkType": svcUplinkType,
       "svcCustomerVid": svcCustomerVid,
       "svcEpipeType": svcEpipeType,
       "svcAllowL2ptXstpBpdu": svcAllowL2ptXstpBpdu,
       "svcbVplsVid": svcbVplsVid,
       "tmnxSASSvcTraps": tmnxSASSvcTraps,
       "svcVplssvcBoundToIESSvc": svcVplssvcBoundToIESSvc,
       "tmnxSASSvcNotifyObjs": tmnxSASSvcNotifyObjs,
       "svcVplsId": svcVplsId,
       "svcIesId": svcIesId}
)
