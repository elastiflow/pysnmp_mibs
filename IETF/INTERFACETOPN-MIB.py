# SNMP MIB module (INTERFACETOPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/INTERFACETOPN-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:36:15 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

interfaceTopNMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InterfaceTopNObjects_ObjectIdentity = ObjectIdentity
interfaceTopNObjects = _InterfaceTopNObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 1)
)


class _InterfaceTopNCaps_Type(Bits):
    """Custom type interfaceTopNCaps based on Bits"""
    namedValues = NamedValues(
        *(("ifInOctets", 0),
          ("ifInUcastPkts", 1),
          ("ifInNUcastPkts", 2),
          ("ifInDiscards", 3),
          ("ifInErrors", 4),
          ("ifInUnknownProtos", 5),
          ("ifOutOctets", 6),
          ("ifOutUcastPkts", 7),
          ("ifOutNUcastPkts", 8),
          ("ifOutDiscards", 9),
          ("ifOutErrors", 10),
          ("ifInMulticastPkts", 11),
          ("ifInBroadcastPkts", 12),
          ("ifOutMulticastPkts", 13),
          ("ifOutBroadcastPkts", 14),
          ("ifHCInOctets", 15),
          ("ifHCInUcastPkts", 16),
          ("ifHCInMulticastPkts", 17),
          ("ifHCInBroadcastPkts", 18),
          ("ifHCOutOctets", 19),
          ("ifHCOutUcastPkts", 20),
          ("ifHCOutMulticastPkts", 21),
          ("ifHCOutBroadcastPkts", 22),
          ("dot3StatsAlignmentErrors", 23),
          ("dot3StatsFCSErrors", 24),
          ("dot3StatsSingleCollisionFrames", 25),
          ("dot3StatsMultipleCollisionFrames", 26),
          ("dot3StatsSQETestErrors", 27),
          ("dot3StatsDeferredTransmissions", 28),
          ("dot3StatsLateCollisions", 29),
          ("dot3StatsExcessiveCollisions", 30),
          ("dot3StatsInternalMacTxErrors", 31),
          ("dot3StatsCarrierSenseErrors", 32),
          ("dot3StatsFrameTooLongs", 33),
          ("dot3StatsInternalMacRxErrors", 34),
          ("dot3StatsSymbolErrors", 35),
          ("dot3InPauseFrames", 36),
          ("dot3OutPauseFrames", 37),
          ("dot5StatsLineErrors", 38),
          ("dot5StatsBurstErrors", 39),
          ("dot5StatsACErrors", 40),
          ("dot5StatsAbortTransErrors", 41),
          ("dot5StatsInternalErrors", 42),
          ("dot5StatsLostFrameErrors", 43),
          ("dot5StatsReceiveCongestions", 44),
          ("dot5StatsFrameCopiedErrors", 45),
          ("dot5StatsTokenErrors", 46),
          ("dot5StatsSoftErrors", 47),
          ("dot5StatsHardErrors", 48),
          ("dot5StatsSignalLoss", 49),
          ("dot5StatsTransmitBeacons", 50),
          ("dot5StatsRecoverys", 51),
          ("dot5StatsLobeWires", 52),
          ("dot5StatsRemoves", 53),
          ("dot5StatsSingles", 54),
          ("dot5StatsFreqErrors", 55),
          ("etherStatsDropEvents", 56),
          ("etherStatsOctets", 57),
          ("etherStatsPkts", 58),
          ("etherStatsBroadcastPkts", 59),
          ("etherStatsMulticastPkts", 60),
          ("etherStatsCRCAlignErrors", 61),
          ("etherStatsUndersizePkts", 62),
          ("etherStatsOversizePkts", 63),
          ("etherStatsFragments", 64),
          ("etherStatsJabbers", 65),
          ("etherStatsCollisions", 66),
          ("etherStatsPkts64Octets", 67),
          ("etherStatsPkts65to127Octets", 68),
          ("etherStatsPkts128to255Octets", 69),
          ("etherStatsPkts256to511Octets", 70),
          ("etherStatsPkts512to1023Octets", 71),
          ("etherStatsPkts1024to1518Octets", 72),
          ("dot1dTpPortInFrames", 73),
          ("dot1dTpPortOutFrames", 74),
          ("dot1dTpPortInDiscards", 75))
    )

_InterfaceTopNCaps_Type.__name__ = "Bits"
_InterfaceTopNCaps_Object = MibScalar
interfaceTopNCaps = _InterfaceTopNCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 1),
    _InterfaceTopNCaps_Type()
)
interfaceTopNCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNCaps.setStatus("current")
_InterfaceTopNControlTable_Object = MibTable
interfaceTopNControlTable = _InterfaceTopNControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2)
)
if mibBuilder.loadTexts:
    interfaceTopNControlTable.setStatus("current")
_InterfaceTopNControlEntry_Object = MibTableRow
interfaceTopNControlEntry = _InterfaceTopNControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1)
)
interfaceTopNControlEntry.setIndexNames(
    (0, "INTERFACETOPN-MIB", "interfaceTopNControlIndex"),
)
if mibBuilder.loadTexts:
    interfaceTopNControlEntry.setStatus("current")


class _InterfaceTopNControlIndex_Type(Integer32):
    """Custom type interfaceTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InterfaceTopNControlIndex_Type.__name__ = "Integer32"
_InterfaceTopNControlIndex_Object = MibTableColumn
interfaceTopNControlIndex = _InterfaceTopNControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 1),
    _InterfaceTopNControlIndex_Type()
)
interfaceTopNControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceTopNControlIndex.setStatus("current")


class _InterfaceTopNObjectVariable_Type(Integer32):
    """Custom type interfaceTopNObjectVariable based on Integer32"""
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
              75)
        )
    )
    namedValues = NamedValues(
        *(("ifInOctets", 0),
          ("ifInUcastPkts", 1),
          ("ifInNUcastPkts", 2),
          ("ifInDiscards", 3),
          ("ifInErrors", 4),
          ("ifInUnknownProtos", 5),
          ("ifOutOctets", 6),
          ("ifOutUcastPkts", 7),
          ("ifOutNUcastPkts", 8),
          ("ifOutDiscards", 9),
          ("ifOutErrors", 10),
          ("ifInMulticastPkts", 11),
          ("ifInBroadcastPkts", 12),
          ("ifOutMulticastPkts", 13),
          ("ifOutBroadcastPkts", 14),
          ("ifHCInOctets", 15),
          ("ifHCInUcastPkts", 16),
          ("ifHCInMulticastPkts", 17),
          ("ifHCInBroadcastPkts", 18),
          ("ifHCOutOctets", 19),
          ("ifHCOutUcastPkts", 20),
          ("ifHCOutMulticastPkts", 21),
          ("ifHCOutBroadcastPkts", 22),
          ("dot3StatsAlignmentErrors", 23),
          ("dot3StatsFCSErrors", 24),
          ("dot3StatsSingleCollisionFrames", 25),
          ("dot3StatsMultipleCollisionFrames", 26),
          ("dot3StatsSQETestErrors", 27),
          ("dot3StatsDeferredTransmissions", 28),
          ("dot3StatsLateCollisions", 29),
          ("dot3StatsExcessiveCollisions", 30),
          ("dot3StatsInternalMacTxErrors", 31),
          ("dot3StatsCarrierSenseErrors", 32),
          ("dot3StatsFrameTooLongs", 33),
          ("dot3StatsInternalMacRxErrors", 34),
          ("dot3StatsSymbolErrors", 35),
          ("dot3InPauseFrames", 36),
          ("dot3OutPauseFrames", 37),
          ("dot5StatsLineErrors", 38),
          ("dot5StatsBurstErrors", 39),
          ("dot5StatsACErrors", 40),
          ("dot5StatsAbortTransErrors", 41),
          ("dot5StatsInternalErrors", 42),
          ("dot5StatsLostFrameErrors", 43),
          ("dot5StatsReceiveCongestions", 44),
          ("dot5StatsFrameCopiedErrors", 45),
          ("dot5StatsTokenErrors", 46),
          ("dot5StatsSoftErrors", 47),
          ("dot5StatsHardErrors", 48),
          ("dot5StatsSignalLoss", 49),
          ("dot5StatsTransmitBeacons", 50),
          ("dot5StatsRecoverys", 51),
          ("dot5StatsLobeWires", 52),
          ("dot5StatsRemoves", 53),
          ("dot5StatsSingles", 54),
          ("dot5StatsFreqErrors", 55),
          ("etherStatsDropEvents", 56),
          ("etherStatsOctets", 57),
          ("etherStatsPkts", 58),
          ("etherStatsBroadcastPkts", 59),
          ("etherStatsMulticastPkts", 60),
          ("etherStatsCRCAlignErrors", 61),
          ("etherStatsUndersizePkts", 62),
          ("etherStatsOversizePkts", 63),
          ("etherStatsFragments", 64),
          ("etherStatsJabbers", 65),
          ("etherStatsCollisions", 66),
          ("etherStatsPkts64Octets", 67),
          ("etherStatsPkts65to127Octets", 68),
          ("etherStatsPkts128to255Octets", 69),
          ("etherStatsPkts256to511Octets", 70),
          ("etherStatsPkts512to1023Octets", 71),
          ("etherStatsPkts1024to1518Octets", 72),
          ("dot1dTpPortInFrames", 73),
          ("dot1dTpPortOutFrames", 74),
          ("dot1dTpPortInDiscards", 75))
    )


_InterfaceTopNObjectVariable_Type.__name__ = "Integer32"
_InterfaceTopNObjectVariable_Object = MibTableColumn
interfaceTopNObjectVariable = _InterfaceTopNObjectVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 2),
    _InterfaceTopNObjectVariable_Type()
)
interfaceTopNObjectVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNObjectVariable.setStatus("current")


class _InterfaceTopNObjectSampleType_Type(Integer32):
    """Custom type interfaceTopNObjectSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2),
          ("bandwidthPercentage", 3))
    )


_InterfaceTopNObjectSampleType_Type.__name__ = "Integer32"
_InterfaceTopNObjectSampleType_Object = MibTableColumn
interfaceTopNObjectSampleType = _InterfaceTopNObjectSampleType_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 3),
    _InterfaceTopNObjectSampleType_Type()
)
interfaceTopNObjectSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNObjectSampleType.setStatus("current")
_InterfaceTopNNormalizationReq_Type = TruthValue
_InterfaceTopNNormalizationReq_Object = MibTableColumn
interfaceTopNNormalizationReq = _InterfaceTopNNormalizationReq_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 4),
    _InterfaceTopNNormalizationReq_Type()
)
interfaceTopNNormalizationReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNNormalizationReq.setStatus("current")


class _InterfaceTopNNormalizationFactor_Type(Integer32):
    """Custom type interfaceTopNNormalizationFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InterfaceTopNNormalizationFactor_Type.__name__ = "Integer32"
_InterfaceTopNNormalizationFactor_Object = MibTableColumn
interfaceTopNNormalizationFactor = _InterfaceTopNNormalizationFactor_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 5),
    _InterfaceTopNNormalizationFactor_Type()
)
interfaceTopNNormalizationFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNNormalizationFactor.setStatus("current")


class _InterfaceTopNTimeRemaining_Type(Integer32):
    """Custom type interfaceTopNTimeRemaining based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InterfaceTopNTimeRemaining_Type.__name__ = "Integer32"
_InterfaceTopNTimeRemaining_Object = MibTableColumn
interfaceTopNTimeRemaining = _InterfaceTopNTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 6),
    _InterfaceTopNTimeRemaining_Type()
)
interfaceTopNTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNTimeRemaining.setStatus("current")


class _InterfaceTopNDuration_Type(Integer32):
    """Custom type interfaceTopNDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InterfaceTopNDuration_Type.__name__ = "Integer32"
_InterfaceTopNDuration_Object = MibTableColumn
interfaceTopNDuration = _InterfaceTopNDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 7),
    _InterfaceTopNDuration_Type()
)
interfaceTopNDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNDuration.setStatus("current")


class _InterfaceTopNRequestedSize_Type(Integer32):
    """Custom type interfaceTopNRequestedSize based on Integer32"""
    defaultValue = 10


_InterfaceTopNRequestedSize_Type.__name__ = "Integer32"
_InterfaceTopNRequestedSize_Object = MibTableColumn
interfaceTopNRequestedSize = _InterfaceTopNRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 8),
    _InterfaceTopNRequestedSize_Type()
)
interfaceTopNRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNRequestedSize.setStatus("current")


class _InterfaceTopNGrantedSize_Type(Integer32):
    """Custom type interfaceTopNGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InterfaceTopNGrantedSize_Type.__name__ = "Integer32"
_InterfaceTopNGrantedSize_Object = MibTableColumn
interfaceTopNGrantedSize = _InterfaceTopNGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 9),
    _InterfaceTopNGrantedSize_Type()
)
interfaceTopNGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNGrantedSize.setStatus("current")
_InterfaceTopNStartTime_Type = TimeStamp
_InterfaceTopNStartTime_Object = MibTableColumn
interfaceTopNStartTime = _InterfaceTopNStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 10),
    _InterfaceTopNStartTime_Type()
)
interfaceTopNStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNStartTime.setStatus("current")
_InterfaceTopNOwner_Type = OwnerString
_InterfaceTopNOwner_Object = MibTableColumn
interfaceTopNOwner = _InterfaceTopNOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 11),
    _InterfaceTopNOwner_Type()
)
interfaceTopNOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNOwner.setStatus("current")
_InterfaceTopNLastCompletionTime_Type = TimeStamp
_InterfaceTopNLastCompletionTime_Object = MibTableColumn
interfaceTopNLastCompletionTime = _InterfaceTopNLastCompletionTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 12),
    _InterfaceTopNLastCompletionTime_Type()
)
interfaceTopNLastCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNLastCompletionTime.setStatus("current")
_InterfaceTopNRowStatus_Type = RowStatus
_InterfaceTopNRowStatus_Object = MibTableColumn
interfaceTopNRowStatus = _InterfaceTopNRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 13),
    _InterfaceTopNRowStatus_Type()
)
interfaceTopNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNRowStatus.setStatus("current")
_InterfaceTopNTable_Object = MibTable
interfaceTopNTable = _InterfaceTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3)
)
if mibBuilder.loadTexts:
    interfaceTopNTable.setStatus("current")
_InterfaceTopNEntry_Object = MibTableRow
interfaceTopNEntry = _InterfaceTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1)
)
interfaceTopNEntry.setIndexNames(
    (0, "INTERFACETOPN-MIB", "interfaceTopNControlIndex"),
    (0, "INTERFACETOPN-MIB", "interfaceTopNIndex"),
)
if mibBuilder.loadTexts:
    interfaceTopNEntry.setStatus("current")


class _InterfaceTopNIndex_Type(Integer32):
    """Custom type interfaceTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InterfaceTopNIndex_Type.__name__ = "Integer32"
_InterfaceTopNIndex_Object = MibTableColumn
interfaceTopNIndex = _InterfaceTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 1),
    _InterfaceTopNIndex_Type()
)
interfaceTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceTopNIndex.setStatus("current")


class _InterfaceTopNDataSourceIndex_Type(Integer32):
    """Custom type interfaceTopNDataSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InterfaceTopNDataSourceIndex_Type.__name__ = "Integer32"
_InterfaceTopNDataSourceIndex_Object = MibTableColumn
interfaceTopNDataSourceIndex = _InterfaceTopNDataSourceIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 2),
    _InterfaceTopNDataSourceIndex_Type()
)
interfaceTopNDataSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNDataSourceIndex.setStatus("current")
_InterfaceTopNValue_Type = Gauge32
_InterfaceTopNValue_Object = MibTableColumn
interfaceTopNValue = _InterfaceTopNValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 3),
    _InterfaceTopNValue_Type()
)
interfaceTopNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNValue.setStatus("current")
_InterfaceTopNValue64_Type = CounterBasedGauge64
_InterfaceTopNValue64_Object = MibTableColumn
interfaceTopNValue64 = _InterfaceTopNValue64_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 4),
    _InterfaceTopNValue64_Type()
)
interfaceTopNValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNValue64.setStatus("current")
_InterfaceTopNNotifications_ObjectIdentity = ObjectIdentity
interfaceTopNNotifications = _InterfaceTopNNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 2)
)
_InterfaceTopNConformance_ObjectIdentity = ObjectIdentity
interfaceTopNConformance = _InterfaceTopNConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 3)
)
_InterfaceTopNCompliances_ObjectIdentity = ObjectIdentity
interfaceTopNCompliances = _InterfaceTopNCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 1)
)
_InterfaceTopNGroups_ObjectIdentity = ObjectIdentity
interfaceTopNGroups = _InterfaceTopNGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 2)
)

# Managed Objects groups

interfaceTopNGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 2, 1)
)
interfaceTopNGroup.setObjects(
      *(("INTERFACETOPN-MIB", "interfaceTopNCaps"),
        ("INTERFACETOPN-MIB", "interfaceTopNObjectVariable"),
        ("INTERFACETOPN-MIB", "interfaceTopNObjectSampleType"),
        ("INTERFACETOPN-MIB", "interfaceTopNNormalizationReq"),
        ("INTERFACETOPN-MIB", "interfaceTopNNormalizationFactor"),
        ("INTERFACETOPN-MIB", "interfaceTopNTimeRemaining"),
        ("INTERFACETOPN-MIB", "interfaceTopNDuration"),
        ("INTERFACETOPN-MIB", "interfaceTopNRequestedSize"),
        ("INTERFACETOPN-MIB", "interfaceTopNGrantedSize"),
        ("INTERFACETOPN-MIB", "interfaceTopNStartTime"),
        ("INTERFACETOPN-MIB", "interfaceTopNOwner"),
        ("INTERFACETOPN-MIB", "interfaceTopNLastCompletionTime"),
        ("INTERFACETOPN-MIB", "interfaceTopNRowStatus"),
        ("INTERFACETOPN-MIB", "interfaceTopNDataSourceIndex"),
        ("INTERFACETOPN-MIB", "interfaceTopNValue"),
        ("INTERFACETOPN-MIB", "interfaceTopNValue64"))
)
if mibBuilder.loadTexts:
    interfaceTopNGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

interfaceTopNCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 1, 1)
)
interfaceTopNCompliance.setObjects(
    ("INTERFACETOPN-MIB", "interfaceTopNGroup")
)
if mibBuilder.loadTexts:
    interfaceTopNCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTERFACETOPN-MIB",
    **{"interfaceTopNMIB": interfaceTopNMIB,
       "interfaceTopNObjects": interfaceTopNObjects,
       "interfaceTopNCaps": interfaceTopNCaps,
       "interfaceTopNControlTable": interfaceTopNControlTable,
       "interfaceTopNControlEntry": interfaceTopNControlEntry,
       "interfaceTopNControlIndex": interfaceTopNControlIndex,
       "interfaceTopNObjectVariable": interfaceTopNObjectVariable,
       "interfaceTopNObjectSampleType": interfaceTopNObjectSampleType,
       "interfaceTopNNormalizationReq": interfaceTopNNormalizationReq,
       "interfaceTopNNormalizationFactor": interfaceTopNNormalizationFactor,
       "interfaceTopNTimeRemaining": interfaceTopNTimeRemaining,
       "interfaceTopNDuration": interfaceTopNDuration,
       "interfaceTopNRequestedSize": interfaceTopNRequestedSize,
       "interfaceTopNGrantedSize": interfaceTopNGrantedSize,
       "interfaceTopNStartTime": interfaceTopNStartTime,
       "interfaceTopNOwner": interfaceTopNOwner,
       "interfaceTopNLastCompletionTime": interfaceTopNLastCompletionTime,
       "interfaceTopNRowStatus": interfaceTopNRowStatus,
       "interfaceTopNTable": interfaceTopNTable,
       "interfaceTopNEntry": interfaceTopNEntry,
       "interfaceTopNIndex": interfaceTopNIndex,
       "interfaceTopNDataSourceIndex": interfaceTopNDataSourceIndex,
       "interfaceTopNValue": interfaceTopNValue,
       "interfaceTopNValue64": interfaceTopNValue64,
       "interfaceTopNNotifications": interfaceTopNNotifications,
       "interfaceTopNConformance": interfaceTopNConformance,
       "interfaceTopNCompliances": interfaceTopNCompliances,
       "interfaceTopNCompliance": interfaceTopNCompliance,
       "interfaceTopNGroups": interfaceTopNGroups,
       "interfaceTopNGroup": interfaceTopNGroup}
)
