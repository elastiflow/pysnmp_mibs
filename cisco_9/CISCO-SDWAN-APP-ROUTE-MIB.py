# SNMP MIB module (CISCO-SDWAN-APP-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-APP-ROUTE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoSdwanAppRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001)
)
if mibBuilder.loadTexts:
    ciscoSdwanAppRouteMIB.setRevisions(
        ("2021-01-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSdwanAppRouteMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanAppRouteMIBObjects = _CiscoSdwanAppRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1)
)
_AppRouteStatisticsTable_Object = MibTable
appRouteStatisticsTable = _AppRouteStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2)
)
if mibBuilder.loadTexts:
    appRouteStatisticsTable.setStatus("current")
_AppRouteStatisticsEntry_Object = MibTableRow
appRouteStatisticsEntry = _AppRouteStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1)
)
appRouteStatisticsEntry.setIndexNames(
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"),
)
if mibBuilder.loadTexts:
    appRouteStatisticsEntry.setStatus("current")
_AppRouteStatisticsSrcIp_Type = InetAddressIP
_AppRouteStatisticsSrcIp_Object = MibTableColumn
appRouteStatisticsSrcIp = _AppRouteStatisticsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 1),
    _AppRouteStatisticsSrcIp_Type()
)
appRouteStatisticsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsSrcIp.setStatus("current")
_AppRouteStatisticsDstIp_Type = InetAddressIP
_AppRouteStatisticsDstIp_Object = MibTableColumn
appRouteStatisticsDstIp = _AppRouteStatisticsDstIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 2),
    _AppRouteStatisticsDstIp_Type()
)
appRouteStatisticsDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsDstIp.setStatus("current")


class _AppRouteStatisticsProto_Type(Integer32):
    """Custom type appRouteStatisticsProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_AppRouteStatisticsProto_Type.__name__ = "Integer32"
_AppRouteStatisticsProto_Object = MibTableColumn
appRouteStatisticsProto = _AppRouteStatisticsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 3),
    _AppRouteStatisticsProto_Type()
)
appRouteStatisticsProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsProto.setStatus("current")
_AppRouteStatisticsSrcPort_Type = UnsignedShort
_AppRouteStatisticsSrcPort_Object = MibTableColumn
appRouteStatisticsSrcPort = _AppRouteStatisticsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 4),
    _AppRouteStatisticsSrcPort_Type()
)
appRouteStatisticsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsSrcPort.setStatus("current")
_AppRouteStatisticsDstPort_Type = UnsignedShort
_AppRouteStatisticsDstPort_Object = MibTableColumn
appRouteStatisticsDstPort = _AppRouteStatisticsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 5),
    _AppRouteStatisticsDstPort_Type()
)
appRouteStatisticsDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsDstPort.setStatus("current")
_AppRouteStatisticsRemoteSystemIp_Type = InetAddressIP
_AppRouteStatisticsRemoteSystemIp_Object = MibTableColumn
appRouteStatisticsRemoteSystemIp = _AppRouteStatisticsRemoteSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 6),
    _AppRouteStatisticsRemoteSystemIp_Type()
)
appRouteStatisticsRemoteSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsRemoteSystemIp.setStatus("current")


class _AppRouteStatisticsLocalColor_Type(Integer32):
    """Custom type appRouteStatisticsLocalColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metroEthernet", 3),
          ("bizInternet", 4),
          ("publicInternet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_AppRouteStatisticsLocalColor_Type.__name__ = "Integer32"
_AppRouteStatisticsLocalColor_Object = MibTableColumn
appRouteStatisticsLocalColor = _AppRouteStatisticsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 7),
    _AppRouteStatisticsLocalColor_Type()
)
appRouteStatisticsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsLocalColor.setStatus("current")


class _AppRouteStatisticsRemoteColor_Type(Integer32):
    """Custom type appRouteStatisticsRemoteColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metroEthernet", 3),
          ("bizInternet", 4),
          ("publicInternet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_AppRouteStatisticsRemoteColor_Type.__name__ = "Integer32"
_AppRouteStatisticsRemoteColor_Object = MibTableColumn
appRouteStatisticsRemoteColor = _AppRouteStatisticsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 8),
    _AppRouteStatisticsRemoteColor_Type()
)
appRouteStatisticsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsRemoteColor.setStatus("current")
_AppRouteSlaClassTable_Object = MibTable
appRouteSlaClassTable = _AppRouteSlaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4)
)
if mibBuilder.loadTexts:
    appRouteSlaClassTable.setStatus("current")
_AppRouteSlaClassEntry_Object = MibTableRow
appRouteSlaClassEntry = _AppRouteSlaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1)
)
appRouteSlaClassEntry.setIndexNames(
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassIndex"),
)
if mibBuilder.loadTexts:
    appRouteSlaClassEntry.setStatus("current")
_AppRouteSlaClassIndex_Type = UnsignedByte
_AppRouteSlaClassIndex_Object = MibTableColumn
appRouteSlaClassIndex = _AppRouteSlaClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 1),
    _AppRouteSlaClassIndex_Type()
)
appRouteSlaClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteSlaClassIndex.setStatus("current")
_AppRouteSlaClassName_Type = String
_AppRouteSlaClassName_Object = MibTableColumn
appRouteSlaClassName = _AppRouteSlaClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 2),
    _AppRouteSlaClassName_Type()
)
appRouteSlaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassName.setStatus("current")
_AppRouteSlaClassLoss_Type = UnsignedByte
_AppRouteSlaClassLoss_Object = MibTableColumn
appRouteSlaClassLoss = _AppRouteSlaClassLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 3),
    _AppRouteSlaClassLoss_Type()
)
appRouteSlaClassLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassLoss.setStatus("current")
_AppRouteSlaClassLatency_Type = Unsigned32
_AppRouteSlaClassLatency_Object = MibTableColumn
appRouteSlaClassLatency = _AppRouteSlaClassLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 4),
    _AppRouteSlaClassLatency_Type()
)
appRouteSlaClassLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassLatency.setStatus("current")
_AppRouteSlaClassJitter_Type = Unsigned32
_AppRouteSlaClassJitter_Object = MibTableColumn
appRouteSlaClassJitter = _AppRouteSlaClassJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 5),
    _AppRouteSlaClassJitter_Type()
)
appRouteSlaClassJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteSlaClassJitter.setStatus("current")
_AppRouteStatisticsAppProbeClassTable_Object = MibTable
appRouteStatisticsAppProbeClassTable = _AppRouteStatisticsAppProbeClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5)
)
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassTable.setStatus("current")
_AppRouteStatisticsAppProbeClassEntry_Object = MibTableRow
appRouteStatisticsAppProbeClassEntry = _AppRouteStatisticsAppProbeClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1)
)
appRouteStatisticsAppProbeClassEntry.setIndexNames(
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassName"),
)
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassEntry.setStatus("current")


class _AppRouteStatisticsAppProbeClassName_Type(String):
    """Custom type appRouteStatisticsAppProbeClassName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppRouteStatisticsAppProbeClassName_Type.__name__ = "String"
_AppRouteStatisticsAppProbeClassName_Object = MibTableColumn
appRouteStatisticsAppProbeClassName = _AppRouteStatisticsAppProbeClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 1),
    _AppRouteStatisticsAppProbeClassName_Type()
)
appRouteStatisticsAppProbeClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassName.setStatus("current")
_AppRouteStatisticsAppProbeClassMeanLoss_Type = UnsignedByte
_AppRouteStatisticsAppProbeClassMeanLoss_Object = MibTableColumn
appRouteStatisticsAppProbeClassMeanLoss = _AppRouteStatisticsAppProbeClassMeanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 2),
    _AppRouteStatisticsAppProbeClassMeanLoss_Type()
)
appRouteStatisticsAppProbeClassMeanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassMeanLoss.setStatus("current")
_AppRouteStatisticsAppProbeClassMeanLatency_Type = Unsigned32
_AppRouteStatisticsAppProbeClassMeanLatency_Object = MibTableColumn
appRouteStatisticsAppProbeClassMeanLatency = _AppRouteStatisticsAppProbeClassMeanLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 3),
    _AppRouteStatisticsAppProbeClassMeanLatency_Type()
)
appRouteStatisticsAppProbeClassMeanLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassMeanLatency.setStatus("current")
_AppRouteStatisticsAppProbeClassMeanJitter_Type = Unsigned32
_AppRouteStatisticsAppProbeClassMeanJitter_Object = MibTableColumn
appRouteStatisticsAppProbeClassMeanJitter = _AppRouteStatisticsAppProbeClassMeanJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 4),
    _AppRouteStatisticsAppProbeClassMeanJitter_Type()
)
appRouteStatisticsAppProbeClassMeanJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassMeanJitter.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalTable_Object = MibTable
appRouteStatisticsAppProbeClassIntervalTable = _AppRouteStatisticsAppProbeClassIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6)
)
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalTable.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalEntry_Object = MibTableRow
appRouteStatisticsAppProbeClassIntervalEntry = _AppRouteStatisticsAppProbeClassIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1)
)
appRouteStatisticsAppProbeClassIntervalEntry.setIndexNames(
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassName"),
    (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalIndex"),
)
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalEntry.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalIndex_Type = UnsignedByte
_AppRouteStatisticsAppProbeClassIntervalIndex_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalIndex = _AppRouteStatisticsAppProbeClassIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 1),
    _AppRouteStatisticsAppProbeClassIntervalIndex_Type()
)
appRouteStatisticsAppProbeClassIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalIndex.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalTotalPackets_Type = Integer32
_AppRouteStatisticsAppProbeClassIntervalTotalPackets_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalTotalPackets = _AppRouteStatisticsAppProbeClassIntervalTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 2),
    _AppRouteStatisticsAppProbeClassIntervalTotalPackets_Type()
)
appRouteStatisticsAppProbeClassIntervalTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalTotalPackets.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalLoss_Type = Integer32
_AppRouteStatisticsAppProbeClassIntervalLoss_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalLoss = _AppRouteStatisticsAppProbeClassIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 3),
    _AppRouteStatisticsAppProbeClassIntervalLoss_Type()
)
appRouteStatisticsAppProbeClassIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalLoss.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalAverageLatency_Type = Counter64
_AppRouteStatisticsAppProbeClassIntervalAverageLatency_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalAverageLatency = _AppRouteStatisticsAppProbeClassIntervalAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 4),
    _AppRouteStatisticsAppProbeClassIntervalAverageLatency_Type()
)
appRouteStatisticsAppProbeClassIntervalAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalAverageLatency.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalAverageJitter_Type = Counter64
_AppRouteStatisticsAppProbeClassIntervalAverageJitter_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalAverageJitter = _AppRouteStatisticsAppProbeClassIntervalAverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 5),
    _AppRouteStatisticsAppProbeClassIntervalAverageJitter_Type()
)
appRouteStatisticsAppProbeClassIntervalAverageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalAverageJitter.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Type = Counter64
_AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalTxDataPkts = _AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 6),
    _AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Type()
)
appRouteStatisticsAppProbeClassIntervalTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalTxDataPkts.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Type = Counter64
_AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalRxDataPkts = _AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 7),
    _AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Type()
)
appRouteStatisticsAppProbeClassIntervalRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalRxDataPkts.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Type = Counter64
_AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts = _AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 8),
    _AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Type()
)
appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts.setStatus("current")
_AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Type = Counter64
_AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Object = MibTableColumn
appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts = _AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 9),
    _AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Type()
)
appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts.setStatus("current")
_CiscoSdwanAppRouteMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanAppRouteMIBConform = _CiscoSdwanAppRouteMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3)
)
_CiscoSdwanAppRouteMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanAppRouteMIBCompliances = _CiscoSdwanAppRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1)
)
_CiscoSdwanAppRouteMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanAppRouteMIBGroups = _CiscoSdwanAppRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2)
)

# Managed Objects groups

cSdwanAppRouteStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 1)
)
cSdwanAppRouteStatisticsGroup.setObjects(
      *(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteSystemIp"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsLocalColor"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteColor"))
)
if mibBuilder.loadTexts:
    cSdwanAppRouteStatisticsGroup.setStatus("current")

cSdwanAppRouteStatisticsAppProbeClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 2)
)
cSdwanAppRouteStatisticsAppProbeClassGroup.setObjects(
      *(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassName"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassMeanLoss"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassMeanLatency"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassMeanJitter"))
)
if mibBuilder.loadTexts:
    cSdwanAppRouteStatisticsAppProbeClassGroup.setStatus("current")

cSdwanAppRouteStatisticsAppProbeClassIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 3)
)
cSdwanAppRouteStatisticsAppProbeClassIntervalGroup.setObjects(
      *(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalTotalPackets"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalLoss"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalAverageLatency"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalAverageJitter"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalTxDataPkts"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalRxDataPkts"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts"))
)
if mibBuilder.loadTexts:
    cSdwanAppRouteStatisticsAppProbeClassIntervalGroup.setStatus("current")

cSdwanAppRouteSlaClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 4)
)
cSdwanAppRouteSlaClassGroup.setObjects(
      *(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassName"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLoss"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLatency"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassJitter"))
)
if mibBuilder.loadTexts:
    cSdwanAppRouteSlaClassGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSdwanAppRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1, 1)
)
ciscoSdwanAppRouteMIBCompliance.setObjects(
      *(("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsGroup"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsAppProbeClassGroup"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsAppProbeClassIntervalGroup"),
        ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteSlaClassGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanAppRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-APP-ROUTE-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "String": String,
       "InetAddressIP": InetAddressIP,
       "ciscoSdwanAppRouteMIB": ciscoSdwanAppRouteMIB,
       "ciscoSdwanAppRouteMIBObjects": ciscoSdwanAppRouteMIBObjects,
       "appRouteStatisticsTable": appRouteStatisticsTable,
       "appRouteStatisticsEntry": appRouteStatisticsEntry,
       "appRouteStatisticsSrcIp": appRouteStatisticsSrcIp,
       "appRouteStatisticsDstIp": appRouteStatisticsDstIp,
       "appRouteStatisticsProto": appRouteStatisticsProto,
       "appRouteStatisticsSrcPort": appRouteStatisticsSrcPort,
       "appRouteStatisticsDstPort": appRouteStatisticsDstPort,
       "appRouteStatisticsRemoteSystemIp": appRouteStatisticsRemoteSystemIp,
       "appRouteStatisticsLocalColor": appRouteStatisticsLocalColor,
       "appRouteStatisticsRemoteColor": appRouteStatisticsRemoteColor,
       "appRouteSlaClassTable": appRouteSlaClassTable,
       "appRouteSlaClassEntry": appRouteSlaClassEntry,
       "appRouteSlaClassIndex": appRouteSlaClassIndex,
       "appRouteSlaClassName": appRouteSlaClassName,
       "appRouteSlaClassLoss": appRouteSlaClassLoss,
       "appRouteSlaClassLatency": appRouteSlaClassLatency,
       "appRouteSlaClassJitter": appRouteSlaClassJitter,
       "appRouteStatisticsAppProbeClassTable": appRouteStatisticsAppProbeClassTable,
       "appRouteStatisticsAppProbeClassEntry": appRouteStatisticsAppProbeClassEntry,
       "appRouteStatisticsAppProbeClassName": appRouteStatisticsAppProbeClassName,
       "appRouteStatisticsAppProbeClassMeanLoss": appRouteStatisticsAppProbeClassMeanLoss,
       "appRouteStatisticsAppProbeClassMeanLatency": appRouteStatisticsAppProbeClassMeanLatency,
       "appRouteStatisticsAppProbeClassMeanJitter": appRouteStatisticsAppProbeClassMeanJitter,
       "appRouteStatisticsAppProbeClassIntervalTable": appRouteStatisticsAppProbeClassIntervalTable,
       "appRouteStatisticsAppProbeClassIntervalEntry": appRouteStatisticsAppProbeClassIntervalEntry,
       "appRouteStatisticsAppProbeClassIntervalIndex": appRouteStatisticsAppProbeClassIntervalIndex,
       "appRouteStatisticsAppProbeClassIntervalTotalPackets": appRouteStatisticsAppProbeClassIntervalTotalPackets,
       "appRouteStatisticsAppProbeClassIntervalLoss": appRouteStatisticsAppProbeClassIntervalLoss,
       "appRouteStatisticsAppProbeClassIntervalAverageLatency": appRouteStatisticsAppProbeClassIntervalAverageLatency,
       "appRouteStatisticsAppProbeClassIntervalAverageJitter": appRouteStatisticsAppProbeClassIntervalAverageJitter,
       "appRouteStatisticsAppProbeClassIntervalTxDataPkts": appRouteStatisticsAppProbeClassIntervalTxDataPkts,
       "appRouteStatisticsAppProbeClassIntervalRxDataPkts": appRouteStatisticsAppProbeClassIntervalRxDataPkts,
       "appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts": appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts,
       "appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts": appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts,
       "ciscoSdwanAppRouteMIBConform": ciscoSdwanAppRouteMIBConform,
       "ciscoSdwanAppRouteMIBCompliances": ciscoSdwanAppRouteMIBCompliances,
       "ciscoSdwanAppRouteMIBCompliance": ciscoSdwanAppRouteMIBCompliance,
       "ciscoSdwanAppRouteMIBGroups": ciscoSdwanAppRouteMIBGroups,
       "cSdwanAppRouteStatisticsGroup": cSdwanAppRouteStatisticsGroup,
       "cSdwanAppRouteStatisticsAppProbeClassGroup": cSdwanAppRouteStatisticsAppProbeClassGroup,
       "cSdwanAppRouteStatisticsAppProbeClassIntervalGroup": cSdwanAppRouteStatisticsAppProbeClassIntervalGroup,
       "cSdwanAppRouteSlaClassGroup": cSdwanAppRouteSlaClassGroup}
)
