# SNMP MIB module (RUIJIE-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ROUTE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(mplsL3VpnVrfConfMidRteThresh,
 mplsL3VpnVrfPerfCurrNumRoutes) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfConfMidRteThresh",
    "mplsL3VpnVrfPerfCurrNumRoutes")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
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

ruijieRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20)
)
if mibBuilder.loadTexts:
    ruijieRouteMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieRouteProtoType(TextualConvention, Integer32):
    status = "current"
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isis", 9),
          ("esis", 10),
          ("ciscoigrp", 11),
          ("bbnspfigp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoeigrp", 16),
          ("max", 17))
    )



# MIB Managed Objects in the order of their OIDs

_RuijieRouteMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRouteMIBObjects = _RuijieRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1)
)
_RuijieRouteServiceStatus_Type = EnabledStatus
_RuijieRouteServiceStatus_Object = MibScalar
ruijieRouteServiceStatus = _RuijieRouteServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 1),
    _RuijieRouteServiceStatus_Type()
)
ruijieRouteServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRouteServiceStatus.setStatus("current")
_RuijieRoutingProtoInfoTable_Object = MibTable
ruijieRoutingProtoInfoTable = _RuijieRoutingProtoInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieRoutingProtoInfoTable.setStatus("current")
_RuijieRoutingProtoInfoEntry_Object = MibTableRow
ruijieRoutingProtoInfoEntry = _RuijieRoutingProtoInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1)
)
ruijieRoutingProtoInfoEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieRoutingProtoInfoProtoType"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRoutingProtoInfoGateWay"),
)
if mibBuilder.loadTexts:
    ruijieRoutingProtoInfoEntry.setStatus("current")
_RuijieRoutingProtoInfoProtoType_Type = RuijieRouteProtoType
_RuijieRoutingProtoInfoProtoType_Object = MibTableColumn
ruijieRoutingProtoInfoProtoType = _RuijieRoutingProtoInfoProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 1),
    _RuijieRoutingProtoInfoProtoType_Type()
)
ruijieRoutingProtoInfoProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoutingProtoInfoProtoType.setStatus("current")
_RuijieRoutingProtoInfoGateWay_Type = IpAddress
_RuijieRoutingProtoInfoGateWay_Object = MibTableColumn
ruijieRoutingProtoInfoGateWay = _RuijieRoutingProtoInfoGateWay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 2),
    _RuijieRoutingProtoInfoGateWay_Type()
)
ruijieRoutingProtoInfoGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoutingProtoInfoGateWay.setStatus("current")
_RuijieRoutingProtoInfoDistance_Type = Unsigned32
_RuijieRoutingProtoInfoDistance_Object = MibTableColumn
ruijieRoutingProtoInfoDistance = _RuijieRoutingProtoInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 3),
    _RuijieRoutingProtoInfoDistance_Type()
)
ruijieRoutingProtoInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoutingProtoInfoDistance.setStatus("current")
_RuijieRoutingProtoInfoLastUpdate_Type = TimeTicks
_RuijieRoutingProtoInfoLastUpdate_Object = MibTableColumn
ruijieRoutingProtoInfoLastUpdate = _RuijieRoutingProtoInfoLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 2, 1, 4),
    _RuijieRoutingProtoInfoLastUpdate_Type()
)
ruijieRoutingProtoInfoLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRoutingProtoInfoLastUpdate.setStatus("current")
_RuijieDefRoutingCfgTable_Object = MibTable
ruijieDefRoutingCfgTable = _RuijieDefRoutingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgTable.setStatus("current")
_RuijieDefRoutingCfgEntry_Object = MibTableRow
ruijieDefRoutingCfgEntry = _RuijieDefRoutingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1)
)
ruijieDefRoutingCfgEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgRoutingProtoType"),
)
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgEntry.setStatus("current")
_RuijieDefRoutingCfgRoutingProtoType_Type = RuijieRouteProtoType
_RuijieDefRoutingCfgRoutingProtoType_Object = MibTableColumn
ruijieDefRoutingCfgRoutingProtoType = _RuijieDefRoutingCfgRoutingProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 1),
    _RuijieDefRoutingCfgRoutingProtoType_Type()
)
ruijieDefRoutingCfgRoutingProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgRoutingProtoType.setStatus("current")


class _RuijieDefRoutingCfgAlways_Type(TruthValue):
    """Custom type ruijieDefRoutingCfgAlways based on TruthValue"""
    defaultValue = 2


_RuijieDefRoutingCfgAlways_Type.__name__ = "TruthValue"
_RuijieDefRoutingCfgAlways_Object = MibTableColumn
ruijieDefRoutingCfgAlways = _RuijieDefRoutingCfgAlways_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 2),
    _RuijieDefRoutingCfgAlways_Type()
)
ruijieDefRoutingCfgAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgAlways.setStatus("current")


class _RuijieDefRoutingCfgMetric_Type(Unsigned32):
    """Custom type ruijieDefRoutingCfgMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_RuijieDefRoutingCfgMetric_Type.__name__ = "Unsigned32"
_RuijieDefRoutingCfgMetric_Object = MibTableColumn
ruijieDefRoutingCfgMetric = _RuijieDefRoutingCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 3),
    _RuijieDefRoutingCfgMetric_Type()
)
ruijieDefRoutingCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgMetric.setStatus("current")


class _RuijieDefRoutingCfgMetricType_Type(Integer32):
    """Custom type ruijieDefRoutingCfgMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_RuijieDefRoutingCfgMetricType_Type.__name__ = "Integer32"
_RuijieDefRoutingCfgMetricType_Object = MibTableColumn
ruijieDefRoutingCfgMetricType = _RuijieDefRoutingCfgMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 4),
    _RuijieDefRoutingCfgMetricType_Type()
)
ruijieDefRoutingCfgMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgMetricType.setStatus("current")


class _RuijieDefRoutingCfgRouteMap_Type(DisplayString):
    """Custom type ruijieDefRoutingCfgRouteMap based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDefRoutingCfgRouteMap_Type.__name__ = "DisplayString"
_RuijieDefRoutingCfgRouteMap_Object = MibTableColumn
ruijieDefRoutingCfgRouteMap = _RuijieDefRoutingCfgRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 5),
    _RuijieDefRoutingCfgRouteMap_Type()
)
ruijieDefRoutingCfgRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgRouteMap.setStatus("current")
_RuijieDefRoutingCfgStatus_Type = RowStatus
_RuijieDefRoutingCfgStatus_Object = MibTableColumn
ruijieDefRoutingCfgStatus = _RuijieDefRoutingCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 1, 3, 1, 6),
    _RuijieDefRoutingCfgStatus_Type()
)
ruijieDefRoutingCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDefRoutingCfgStatus.setStatus("current")
_RuijieRouteMapMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRouteMapMIBObjects = _RuijieRouteMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2)
)
_RuijieRouteMapTable_Object = MibTable
ruijieRouteMapTable = _RuijieRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieRouteMapTable.setStatus("current")
_RuijieRouteMapEntry_Object = MibTableRow
ruijieRouteMapEntry = _RuijieRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1)
)
ruijieRouteMapEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapName"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapSequenceNumber"),
)
if mibBuilder.loadTexts:
    ruijieRouteMapEntry.setStatus("current")


class _RuijieRouteMapName_Type(DisplayString):
    """Custom type ruijieRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRouteMapName_Type.__name__ = "DisplayString"
_RuijieRouteMapName_Object = MibTableColumn
ruijieRouteMapName = _RuijieRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 1),
    _RuijieRouteMapName_Type()
)
ruijieRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapName.setStatus("current")


class _RuijieRouteMapSequenceNumber_Type(Unsigned32):
    """Custom type ruijieRouteMapSequenceNumber based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieRouteMapSequenceNumber_Type.__name__ = "Unsigned32"
_RuijieRouteMapSequenceNumber_Object = MibTableColumn
ruijieRouteMapSequenceNumber = _RuijieRouteMapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 2),
    _RuijieRouteMapSequenceNumber_Type()
)
ruijieRouteMapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapSequenceNumber.setStatus("current")


class _RuijieRouteMapOperType_Type(Integer32):
    """Custom type ruijieRouteMapOperType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuijieRouteMapOperType_Type.__name__ = "Integer32"
_RuijieRouteMapOperType_Object = MibTableColumn
ruijieRouteMapOperType = _RuijieRouteMapOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 3),
    _RuijieRouteMapOperType_Type()
)
ruijieRouteMapOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapOperType.setStatus("current")


class _RuijieRouteMapMatchMetric_Type(Unsigned32):
    """Custom type ruijieRouteMapMatchMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieRouteMapMatchMetric_Type.__name__ = "Unsigned32"
_RuijieRouteMapMatchMetric_Object = MibTableColumn
ruijieRouteMapMatchMetric = _RuijieRouteMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 4),
    _RuijieRouteMapMatchMetric_Type()
)
ruijieRouteMapMatchMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchMetric.setStatus("current")


class _RuijieRouteMapMatchRouteType_Type(Integer32):
    """Custom type ruijieRouteMapMatchRouteType based on Integer32"""
    defaultValue = 0

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
        *(("notMatch", 0),
          ("internal", 1),
          ("external", 2),
          ("external-type1", 3),
          ("external-type2", 4))
    )


_RuijieRouteMapMatchRouteType_Type.__name__ = "Integer32"
_RuijieRouteMapMatchRouteType_Object = MibTableColumn
ruijieRouteMapMatchRouteType = _RuijieRouteMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 5),
    _RuijieRouteMapMatchRouteType_Type()
)
ruijieRouteMapMatchRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchRouteType.setStatus("current")


class _RuijieRouteMapMetricValueType_Type(Integer32):
    """Custom type ruijieRouteMapMetricValueType based on Integer32"""
    defaultValue = 0

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
        *(("noOper", 0),
          ("replace", 1),
          ("add", 2),
          ("reduce", 3))
    )


_RuijieRouteMapMetricValueType_Type.__name__ = "Integer32"
_RuijieRouteMapMetricValueType_Object = MibTableColumn
ruijieRouteMapMetricValueType = _RuijieRouteMapMetricValueType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 6),
    _RuijieRouteMapMetricValueType_Type()
)
ruijieRouteMapMetricValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapMetricValueType.setStatus("current")


class _RuijieRouteMapSetMetric_Type(Unsigned32):
    """Custom type ruijieRouteMapSetMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieRouteMapSetMetric_Type.__name__ = "Unsigned32"
_RuijieRouteMapSetMetric_Object = MibTableColumn
ruijieRouteMapSetMetric = _RuijieRouteMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 7),
    _RuijieRouteMapSetMetric_Type()
)
ruijieRouteMapSetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapSetMetric.setStatus("current")


class _RuijieRouteMapSetLevel_Type(Integer32):
    """Custom type ruijieRouteMapSetLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("stubarea", 1),
          ("backbone", 2))
    )


_RuijieRouteMapSetLevel_Type.__name__ = "Integer32"
_RuijieRouteMapSetLevel_Object = MibTableColumn
ruijieRouteMapSetLevel = _RuijieRouteMapSetLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 8),
    _RuijieRouteMapSetLevel_Type()
)
ruijieRouteMapSetLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapSetLevel.setStatus("current")


class _RuijieRouteMapSetMetricType_Type(Integer32):
    """Custom type ruijieRouteMapSetMetricType based on Integer32"""
    defaultValue = 0

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
        *(("noOper", 0),
          ("internal", 1),
          ("external", 2),
          ("type1", 3),
          ("type2", 4))
    )


_RuijieRouteMapSetMetricType_Type.__name__ = "Integer32"
_RuijieRouteMapSetMetricType_Object = MibTableColumn
ruijieRouteMapSetMetricType = _RuijieRouteMapSetMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 9),
    _RuijieRouteMapSetMetricType_Type()
)
ruijieRouteMapSetMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapSetMetricType.setStatus("current")


class _RuijieRouteMapSetNexthopSt_Type(ConfigStatus):
    """Custom type ruijieRouteMapSetNexthopSt based on ConfigStatus"""
    defaultValue = 2


_RuijieRouteMapSetNexthopSt_Type.__name__ = "ConfigStatus"
_RuijieRouteMapSetNexthopSt_Object = MibTableColumn
ruijieRouteMapSetNexthopSt = _RuijieRouteMapSetNexthopSt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 10),
    _RuijieRouteMapSetNexthopSt_Type()
)
ruijieRouteMapSetNexthopSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapSetNexthopSt.setStatus("current")
_RuijieRouteMapSetNexthop_Type = IpAddress
_RuijieRouteMapSetNexthop_Object = MibTableColumn
ruijieRouteMapSetNexthop = _RuijieRouteMapSetNexthop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 11),
    _RuijieRouteMapSetNexthop_Type()
)
ruijieRouteMapSetNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapSetNexthop.setStatus("current")
_RuijieRouteMapStatus_Type = RowStatus
_RuijieRouteMapStatus_Object = MibTableColumn
ruijieRouteMapStatus = _RuijieRouteMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 1, 1, 12),
    _RuijieRouteMapStatus_Type()
)
ruijieRouteMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapStatus.setStatus("current")
_RuijieRouteMapMatchIpAddressTable_Object = MibTable
ruijieRouteMapMatchIpAddressTable = _RuijieRouteMapMatchIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieRouteMapMatchIpAddressTable.setStatus("current")
_RuijieRouteMapMatchIpAddressEntry_Object = MibTableRow
ruijieRouteMapMatchIpAddressEntry = _RuijieRouteMapMatchIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1)
)
ruijieRouteMapMatchIpAddressEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapName"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapSequenceNumber"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchType"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchIpAddressAclName"),
)
if mibBuilder.loadTexts:
    ruijieRouteMapMatchIpAddressEntry.setStatus("current")


class _RuijieRouteMapMatchType_Type(Integer32):
    """Custom type ruijieRouteMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("nextHop", 2),
          ("source", 3))
    )


_RuijieRouteMapMatchType_Type.__name__ = "Integer32"
_RuijieRouteMapMatchType_Object = MibTableColumn
ruijieRouteMapMatchType = _RuijieRouteMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1, 1),
    _RuijieRouteMapMatchType_Type()
)
ruijieRouteMapMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchType.setStatus("current")


class _RuijieRouteMapMatchIpAddressAclName_Type(DisplayString):
    """Custom type ruijieRouteMapMatchIpAddressAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRouteMapMatchIpAddressAclName_Type.__name__ = "DisplayString"
_RuijieRouteMapMatchIpAddressAclName_Object = MibTableColumn
ruijieRouteMapMatchIpAddressAclName = _RuijieRouteMapMatchIpAddressAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1, 2),
    _RuijieRouteMapMatchIpAddressAclName_Type()
)
ruijieRouteMapMatchIpAddressAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchIpAddressAclName.setStatus("current")
_RuijieRouteMapMatchIpAddressStatus_Type = RowStatus
_RuijieRouteMapMatchIpAddressStatus_Object = MibTableColumn
ruijieRouteMapMatchIpAddressStatus = _RuijieRouteMapMatchIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 2, 1, 3),
    _RuijieRouteMapMatchIpAddressStatus_Type()
)
ruijieRouteMapMatchIpAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchIpAddressStatus.setStatus("current")
_RuijieRouteMapMatchTagTable_Object = MibTable
ruijieRouteMapMatchTagTable = _RuijieRouteMapMatchTagTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3)
)
if mibBuilder.loadTexts:
    ruijieRouteMapMatchTagTable.setStatus("current")
_RuijieRouteMapMatchTagEntry_Object = MibTableRow
ruijieRouteMapMatchTagEntry = _RuijieRouteMapMatchTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3, 1)
)
ruijieRouteMapMatchTagEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapName"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapSequenceNumber"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchTagValue"),
)
if mibBuilder.loadTexts:
    ruijieRouteMapMatchTagEntry.setStatus("current")


class _RuijieRouteMapMatchTagValue_Type(Unsigned32):
    """Custom type ruijieRouteMapMatchTagValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieRouteMapMatchTagValue_Type.__name__ = "Unsigned32"
_RuijieRouteMapMatchTagValue_Object = MibTableColumn
ruijieRouteMapMatchTagValue = _RuijieRouteMapMatchTagValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3, 1, 1),
    _RuijieRouteMapMatchTagValue_Type()
)
ruijieRouteMapMatchTagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchTagValue.setStatus("current")
_RuijieRouteMapMatchTagStatus_Type = RowStatus
_RuijieRouteMapMatchTagStatus_Object = MibTableColumn
ruijieRouteMapMatchTagStatus = _RuijieRouteMapMatchTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 3, 1, 2),
    _RuijieRouteMapMatchTagStatus_Type()
)
ruijieRouteMapMatchTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchTagStatus.setStatus("current")
_RuijieRouteMapMatchInterfaceTable_Object = MibTable
ruijieRouteMapMatchInterfaceTable = _RuijieRouteMapMatchInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4)
)
if mibBuilder.loadTexts:
    ruijieRouteMapMatchInterfaceTable.setStatus("current")
_RuijieRouteMapMatchInterfaceEntry_Object = MibTableRow
ruijieRouteMapMatchInterfaceEntry = _RuijieRouteMapMatchInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4, 1)
)
ruijieRouteMapMatchInterfaceEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapName"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapSequenceNumber"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieRouteMapMatchInterfaceEntry.setStatus("current")
_RuijieRouteMapMatchInterfaceIfIndex_Type = IfIndex
_RuijieRouteMapMatchInterfaceIfIndex_Object = MibTableColumn
ruijieRouteMapMatchInterfaceIfIndex = _RuijieRouteMapMatchInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4, 1, 1),
    _RuijieRouteMapMatchInterfaceIfIndex_Type()
)
ruijieRouteMapMatchInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchInterfaceIfIndex.setStatus("current")
_RuijieRouteMapMatchInterfaceStatus_Type = RowStatus
_RuijieRouteMapMatchInterfaceStatus_Object = MibTableColumn
ruijieRouteMapMatchInterfaceStatus = _RuijieRouteMapMatchInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 2, 4, 1, 2),
    _RuijieRouteMapMatchInterfaceStatus_Type()
)
ruijieRouteMapMatchInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteMapMatchInterfaceStatus.setStatus("current")
_RuijieRouteRedistributeMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRouteRedistributeMIBObjects = _RuijieRouteRedistributeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3)
)
_RuijieRouteRedistributeTable_Object = MibTable
ruijieRouteRedistributeTable = _RuijieRouteRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieRouteRedistributeTable.setStatus("current")
_RuijieRouteRedistributeEntry_Object = MibTableRow
ruijieRouteRedistributeEntry = _RuijieRouteRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1)
)
ruijieRouteRedistributeEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeProtocolCfg"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    ruijieRouteRedistributeEntry.setStatus("current")
_RuijieRouteRedistributeProtocolCfg_Type = RuijieRouteProtoType
_RuijieRouteRedistributeProtocolCfg_Object = MibTableColumn
ruijieRouteRedistributeProtocolCfg = _RuijieRouteRedistributeProtocolCfg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 1),
    _RuijieRouteRedistributeProtocolCfg_Type()
)
ruijieRouteRedistributeProtocolCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeProtocolCfg.setStatus("current")
_RuijieRouteRedistributeProtocol_Type = RuijieRouteProtoType
_RuijieRouteRedistributeProtocol_Object = MibTableColumn
ruijieRouteRedistributeProtocol = _RuijieRouteRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 2),
    _RuijieRouteRedistributeProtocol_Type()
)
ruijieRouteRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeProtocol.setStatus("current")


class _RuijieRouteRedistributeMetricValue_Type(Unsigned32):
    """Custom type ruijieRouteRedistributeMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_RuijieRouteRedistributeMetricValue_Type.__name__ = "Unsigned32"
_RuijieRouteRedistributeMetricValue_Object = MibTableColumn
ruijieRouteRedistributeMetricValue = _RuijieRouteRedistributeMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 3),
    _RuijieRouteRedistributeMetricValue_Type()
)
ruijieRouteRedistributeMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeMetricValue.setStatus("current")


class _RuijieRouteRedistributeMetricType_Type(Integer32):
    """Custom type ruijieRouteRedistributeMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_RuijieRouteRedistributeMetricType_Type.__name__ = "Integer32"
_RuijieRouteRedistributeMetricType_Object = MibTableColumn
ruijieRouteRedistributeMetricType = _RuijieRouteRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 4),
    _RuijieRouteRedistributeMetricType_Type()
)
ruijieRouteRedistributeMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeMetricType.setStatus("current")


class _RuijieRouteRedistributeTagValue_Type(Unsigned32):
    """Custom type ruijieRouteRedistributeTagValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RuijieRouteRedistributeTagValue_Type.__name__ = "Unsigned32"
_RuijieRouteRedistributeTagValue_Object = MibTableColumn
ruijieRouteRedistributeTagValue = _RuijieRouteRedistributeTagValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 5),
    _RuijieRouteRedistributeTagValue_Type()
)
ruijieRouteRedistributeTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeTagValue.setStatus("current")


class _RuijieRouteRedistributeRouteMapName_Type(DisplayString):
    """Custom type ruijieRouteRedistributeRouteMapName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieRouteRedistributeRouteMapName_Type.__name__ = "DisplayString"
_RuijieRouteRedistributeRouteMapName_Object = MibTableColumn
ruijieRouteRedistributeRouteMapName = _RuijieRouteRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 6),
    _RuijieRouteRedistributeRouteMapName_Type()
)
ruijieRouteRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeRouteMapName.setStatus("current")
_RuijieRouteRedistributeStatus_Type = RowStatus
_RuijieRouteRedistributeStatus_Object = MibTableColumn
ruijieRouteRedistributeStatus = _RuijieRouteRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 3, 1, 1, 7),
    _RuijieRouteRedistributeStatus_Type()
)
ruijieRouteRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRouteRedistributeStatus.setStatus("current")
_RuijieRouteFilteringMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRouteFilteringMIBObjects = _RuijieRouteFilteringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4)
)
_RuijieIpPrefixListTable_Object = MibTable
ruijieIpPrefixListTable = _RuijieIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieIpPrefixListTable.setStatus("current")
_RuijieIpPrefixListEntry_Object = MibTableRow
ruijieIpPrefixListEntry = _RuijieIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1)
)
ruijieIpPrefixListEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieIpPrefixListName"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieIpPrefixListSequence"),
)
if mibBuilder.loadTexts:
    ruijieIpPrefixListEntry.setStatus("current")


class _RuijieIpPrefixListName_Type(DisplayString):
    """Custom type ruijieIpPrefixListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieIpPrefixListName_Type.__name__ = "DisplayString"
_RuijieIpPrefixListName_Object = MibTableColumn
ruijieIpPrefixListName = _RuijieIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 1),
    _RuijieIpPrefixListName_Type()
)
ruijieIpPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpPrefixListName.setStatus("current")


class _RuijieIpPrefixListSequence_Type(Unsigned32):
    """Custom type ruijieIpPrefixListSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIpPrefixListSequence_Type.__name__ = "Unsigned32"
_RuijieIpPrefixListSequence_Object = MibTableColumn
ruijieIpPrefixListSequence = _RuijieIpPrefixListSequence_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 2),
    _RuijieIpPrefixListSequence_Type()
)
ruijieIpPrefixListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpPrefixListSequence.setStatus("current")


class _RuijieIpPrefixListOperMethod_Type(Integer32):
    """Custom type ruijieIpPrefixListOperMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuijieIpPrefixListOperMethod_Type.__name__ = "Integer32"
_RuijieIpPrefixListOperMethod_Object = MibTableColumn
ruijieIpPrefixListOperMethod = _RuijieIpPrefixListOperMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 3),
    _RuijieIpPrefixListOperMethod_Type()
)
ruijieIpPrefixListOperMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIpPrefixListOperMethod.setStatus("current")
_RuijieIpPrefixListIpAddress_Type = IpAddress
_RuijieIpPrefixListIpAddress_Object = MibTableColumn
ruijieIpPrefixListIpAddress = _RuijieIpPrefixListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 4),
    _RuijieIpPrefixListIpAddress_Type()
)
ruijieIpPrefixListIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIpPrefixListIpAddress.setStatus("current")


class _RuijieIpPrefixListMaskLength_Type(Unsigned32):
    """Custom type ruijieIpPrefixListMaskLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuijieIpPrefixListMaskLength_Type.__name__ = "Unsigned32"
_RuijieIpPrefixListMaskLength_Object = MibTableColumn
ruijieIpPrefixListMaskLength = _RuijieIpPrefixListMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 5),
    _RuijieIpPrefixListMaskLength_Type()
)
ruijieIpPrefixListMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIpPrefixListMaskLength.setStatus("current")


class _RuijieIpPrefixListMinimumPrefixLength_Type(Unsigned32):
    """Custom type ruijieIpPrefixListMinimumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuijieIpPrefixListMinimumPrefixLength_Type.__name__ = "Unsigned32"
_RuijieIpPrefixListMinimumPrefixLength_Object = MibTableColumn
ruijieIpPrefixListMinimumPrefixLength = _RuijieIpPrefixListMinimumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 6),
    _RuijieIpPrefixListMinimumPrefixLength_Type()
)
ruijieIpPrefixListMinimumPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIpPrefixListMinimumPrefixLength.setStatus("current")


class _RuijieIpPrefixListMaximumPrefixLength_Type(Unsigned32):
    """Custom type ruijieIpPrefixListMaximumPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuijieIpPrefixListMaximumPrefixLength_Type.__name__ = "Unsigned32"
_RuijieIpPrefixListMaximumPrefixLength_Object = MibTableColumn
ruijieIpPrefixListMaximumPrefixLength = _RuijieIpPrefixListMaximumPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 7),
    _RuijieIpPrefixListMaximumPrefixLength_Type()
)
ruijieIpPrefixListMaximumPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIpPrefixListMaximumPrefixLength.setStatus("current")
_RuijieIpPrefixListStatus_Type = RowStatus
_RuijieIpPrefixListStatus_Object = MibTableColumn
ruijieIpPrefixListStatus = _RuijieIpPrefixListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 1, 1, 8),
    _RuijieIpPrefixListStatus_Type()
)
ruijieIpPrefixListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIpPrefixListStatus.setStatus("current")
_RuijieDistributeListTable_Object = MibTable
ruijieDistributeListTable = _RuijieDistributeListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2)
)
if mibBuilder.loadTexts:
    ruijieDistributeListTable.setStatus("current")
_RuijieDistributeListEntry_Object = MibTableRow
ruijieDistributeListEntry = _RuijieDistributeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1)
)
ruijieDistributeListEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieDistributeListCfgProtoType"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieDistributeListIfIndex"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieDistributeListDirection"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieDistributeListFilteringProtocol"),
)
if mibBuilder.loadTexts:
    ruijieDistributeListEntry.setStatus("current")
_RuijieDistributeListCfgProtoType_Type = RuijieRouteProtoType
_RuijieDistributeListCfgProtoType_Object = MibTableColumn
ruijieDistributeListCfgProtoType = _RuijieDistributeListCfgProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 1),
    _RuijieDistributeListCfgProtoType_Type()
)
ruijieDistributeListCfgProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDistributeListCfgProtoType.setStatus("current")
_RuijieDistributeListIfIndex_Type = Unsigned32
_RuijieDistributeListIfIndex_Object = MibTableColumn
ruijieDistributeListIfIndex = _RuijieDistributeListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 2),
    _RuijieDistributeListIfIndex_Type()
)
ruijieDistributeListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDistributeListIfIndex.setStatus("current")


class _RuijieDistributeListDirection_Type(Integer32):
    """Custom type ruijieDistributeListDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("out", 1),
          ("in", 2))
    )


_RuijieDistributeListDirection_Type.__name__ = "Integer32"
_RuijieDistributeListDirection_Object = MibTableColumn
ruijieDistributeListDirection = _RuijieDistributeListDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 3),
    _RuijieDistributeListDirection_Type()
)
ruijieDistributeListDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDistributeListDirection.setStatus("current")
_RuijieDistributeListFilteringProtocol_Type = Unsigned32
_RuijieDistributeListFilteringProtocol_Object = MibTableColumn
ruijieDistributeListFilteringProtocol = _RuijieDistributeListFilteringProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 4),
    _RuijieDistributeListFilteringProtocol_Type()
)
ruijieDistributeListFilteringProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDistributeListFilteringProtocol.setStatus("current")


class _RuijieDistributeListFilterType_Type(Integer32):
    """Custom type ruijieDistributeListFilterType based on Integer32"""
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
        *(("acl", 1),
          ("gateway", 2),
          ("prefix", 3),
          ("prefix-gateway", 4))
    )


_RuijieDistributeListFilterType_Type.__name__ = "Integer32"
_RuijieDistributeListFilterType_Object = MibTableColumn
ruijieDistributeListFilterType = _RuijieDistributeListFilterType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 5),
    _RuijieDistributeListFilterType_Type()
)
ruijieDistributeListFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDistributeListFilterType.setStatus("current")


class _RuijieDistributeListAclName_Type(DisplayString):
    """Custom type ruijieDistributeListAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDistributeListAclName_Type.__name__ = "DisplayString"
_RuijieDistributeListAclName_Object = MibTableColumn
ruijieDistributeListAclName = _RuijieDistributeListAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 6),
    _RuijieDistributeListAclName_Type()
)
ruijieDistributeListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDistributeListAclName.setStatus("current")


class _RuijieDistributeListGateWayIpPrefixName_Type(DisplayString):
    """Custom type ruijieDistributeListGateWayIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDistributeListGateWayIpPrefixName_Type.__name__ = "DisplayString"
_RuijieDistributeListGateWayIpPrefixName_Object = MibTableColumn
ruijieDistributeListGateWayIpPrefixName = _RuijieDistributeListGateWayIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 7),
    _RuijieDistributeListGateWayIpPrefixName_Type()
)
ruijieDistributeListGateWayIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDistributeListGateWayIpPrefixName.setStatus("current")


class _RuijieDistributeListPrefixIpPrefixName_Type(DisplayString):
    """Custom type ruijieDistributeListPrefixIpPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDistributeListPrefixIpPrefixName_Type.__name__ = "DisplayString"
_RuijieDistributeListPrefixIpPrefixName_Object = MibTableColumn
ruijieDistributeListPrefixIpPrefixName = _RuijieDistributeListPrefixIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 8),
    _RuijieDistributeListPrefixIpPrefixName_Type()
)
ruijieDistributeListPrefixIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDistributeListPrefixIpPrefixName.setStatus("current")
_RuijieDistributeListStatus_Type = RowStatus
_RuijieDistributeListStatus_Object = MibTableColumn
ruijieDistributeListStatus = _RuijieDistributeListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 4, 2, 1, 9),
    _RuijieDistributeListStatus_Type()
)
ruijieDistributeListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieDistributeListStatus.setStatus("current")
_RuijieipCidrRouteExtendMIBObjects_ObjectIdentity = ObjectIdentity
ruijieipCidrRouteExtendMIBObjects = _RuijieipCidrRouteExtendMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5)
)
_RuijieipCidrRouteTable_Object = MibTable
ruijieipCidrRouteTable = _RuijieipCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1)
)
if mibBuilder.loadTexts:
    ruijieipCidrRouteTable.setStatus("current")
_RuijieipCidrRouteEntry_Object = MibTableRow
ruijieipCidrRouteEntry = _RuijieipCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1)
)
ruijieipCidrRouteEntry.setIndexNames(
    (0, "RUIJIE-ROUTE-MIB", "ruijieipCidrRouteDest"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMask"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieipCidrRouteTos"),
    (0, "RUIJIE-ROUTE-MIB", "ruijieipCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    ruijieipCidrRouteEntry.setStatus("current")
_RuijieipCidrRouteDest_Type = IpAddress
_RuijieipCidrRouteDest_Object = MibTableColumn
ruijieipCidrRouteDest = _RuijieipCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 1),
    _RuijieipCidrRouteDest_Type()
)
ruijieipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrRouteDest.setStatus("current")
_RuijieipCidrRouteMask_Type = IpAddress
_RuijieipCidrRouteMask_Object = MibTableColumn
ruijieipCidrRouteMask = _RuijieipCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 2),
    _RuijieipCidrRouteMask_Type()
)
ruijieipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrRouteMask.setStatus("current")
_RuijieipCidrRouteTos_Type = Integer32
_RuijieipCidrRouteTos_Object = MibTableColumn
ruijieipCidrRouteTos = _RuijieipCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 3),
    _RuijieipCidrRouteTos_Type()
)
ruijieipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrRouteTos.setStatus("current")
_RuijieipCidrRouteNextHop_Type = IpAddress
_RuijieipCidrRouteNextHop_Object = MibTableColumn
ruijieipCidrRouteNextHop = _RuijieipCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 4),
    _RuijieipCidrRouteNextHop_Type()
)
ruijieipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrRouteNextHop.setStatus("current")


class _RuijieipCidrRouteIfIndex_Type(Integer32):
    """Custom type ruijieipCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_RuijieipCidrRouteIfIndex_Type.__name__ = "Integer32"
_RuijieipCidrRouteIfIndex_Object = MibTableColumn
ruijieipCidrRouteIfIndex = _RuijieipCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 5),
    _RuijieipCidrRouteIfIndex_Type()
)
ruijieipCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteIfIndex.setStatus("current")


class _RuijieipCidrRouteType_Type(Integer32):
    """Custom type ruijieipCidrRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_RuijieipCidrRouteType_Type.__name__ = "Integer32"
_RuijieipCidrRouteType_Object = MibTableColumn
ruijieipCidrRouteType = _RuijieipCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 6),
    _RuijieipCidrRouteType_Type()
)
ruijieipCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteType.setStatus("current")


class _RuijieipCidrRouteProto_Type(Integer32):
    """Custom type ruijieipCidrRouteProto based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16),
          ("policy", 17))
    )


_RuijieipCidrRouteProto_Type.__name__ = "Integer32"
_RuijieipCidrRouteProto_Object = MibTableColumn
ruijieipCidrRouteProto = _RuijieipCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 7),
    _RuijieipCidrRouteProto_Type()
)
ruijieipCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrRouteProto.setStatus("current")


class _RuijieipCidrRouteAge_Type(Integer32):
    """Custom type ruijieipCidrRouteAge based on Integer32"""
    defaultValue = 0


_RuijieipCidrRouteAge_Type.__name__ = "Integer32"
_RuijieipCidrRouteAge_Object = MibTableColumn
ruijieipCidrRouteAge = _RuijieipCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 8),
    _RuijieipCidrRouteAge_Type()
)
ruijieipCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrRouteAge.setStatus("current")
_RuijieipCidrRouteInfo_Type = ObjectIdentifier
_RuijieipCidrRouteInfo_Object = MibTableColumn
ruijieipCidrRouteInfo = _RuijieipCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 9),
    _RuijieipCidrRouteInfo_Type()
)
ruijieipCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteInfo.setStatus("current")


class _RuijieipCidrRouteNextHopAS_Type(Integer32):
    """Custom type ruijieipCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_RuijieipCidrRouteNextHopAS_Type.__name__ = "Integer32"
_RuijieipCidrRouteNextHopAS_Object = MibTableColumn
ruijieipCidrRouteNextHopAS = _RuijieipCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 10),
    _RuijieipCidrRouteNextHopAS_Type()
)
ruijieipCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteNextHopAS.setStatus("current")


class _RuijieipCidrRouteMetric1_Type(Integer32):
    """Custom type ruijieipCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_RuijieipCidrRouteMetric1_Type.__name__ = "Integer32"
_RuijieipCidrRouteMetric1_Object = MibTableColumn
ruijieipCidrRouteMetric1 = _RuijieipCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 11),
    _RuijieipCidrRouteMetric1_Type()
)
ruijieipCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteMetric1.setStatus("current")


class _RuijieipCidrRouteMetric2_Type(Integer32):
    """Custom type ruijieipCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_RuijieipCidrRouteMetric2_Type.__name__ = "Integer32"
_RuijieipCidrRouteMetric2_Object = MibTableColumn
ruijieipCidrRouteMetric2 = _RuijieipCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 12),
    _RuijieipCidrRouteMetric2_Type()
)
ruijieipCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteMetric2.setStatus("current")


class _RuijieipCidrRouteMetric3_Type(Integer32):
    """Custom type ruijieipCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_RuijieipCidrRouteMetric3_Type.__name__ = "Integer32"
_RuijieipCidrRouteMetric3_Object = MibTableColumn
ruijieipCidrRouteMetric3 = _RuijieipCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 13),
    _RuijieipCidrRouteMetric3_Type()
)
ruijieipCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteMetric3.setStatus("current")


class _RuijieipCidrRouteMetric4_Type(Integer32):
    """Custom type ruijieipCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_RuijieipCidrRouteMetric4_Type.__name__ = "Integer32"
_RuijieipCidrRouteMetric4_Object = MibTableColumn
ruijieipCidrRouteMetric4 = _RuijieipCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 14),
    _RuijieipCidrRouteMetric4_Type()
)
ruijieipCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteMetric4.setStatus("current")


class _RuijieipCidrRouteMetric5_Type(Integer32):
    """Custom type ruijieipCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_RuijieipCidrRouteMetric5_Type.__name__ = "Integer32"
_RuijieipCidrRouteMetric5_Object = MibTableColumn
ruijieipCidrRouteMetric5 = _RuijieipCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 15),
    _RuijieipCidrRouteMetric5_Type()
)
ruijieipCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteMetric5.setStatus("current")
_RuijieipCidrRouteStatus_Type = RowStatus
_RuijieipCidrRouteStatus_Object = MibTableColumn
ruijieipCidrRouteStatus = _RuijieipCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 16),
    _RuijieipCidrRouteStatus_Type()
)
ruijieipCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieipCidrRouteStatus.setStatus("current")


class _RuijieipCidrOspfRouteType_Type(Integer32):
    """Custom type ruijieipCidrOspfRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ospf-route", 0),
          ("ospf-ia-route", 1),
          ("ospf-n1-route", 2),
          ("ospf-n2-route", 3),
          ("ospf-e1-route", 4),
          ("ospf-e2-route", 5))
    )


_RuijieipCidrOspfRouteType_Type.__name__ = "Integer32"
_RuijieipCidrOspfRouteType_Object = MibTableColumn
ruijieipCidrOspfRouteType = _RuijieipCidrOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 5, 1, 1, 17),
    _RuijieipCidrOspfRouteType_Type()
)
ruijieipCidrOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieipCidrOspfRouteType.setStatus("current")
_RuijieRouteMIBConformance_ObjectIdentity = ObjectIdentity
ruijieRouteMIBConformance = _RuijieRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6)
)
_RuijieRouteMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieRouteMIBCompliances = _RuijieRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 1)
)
_RuijieRouteMIBGroups_ObjectIdentity = ObjectIdentity
ruijieRouteMIBGroups = _RuijieRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2)
)
_RuijieRouteTrap_ObjectIdentity = ObjectIdentity
ruijieRouteTrap = _RuijieRouteTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7)
)


class _RuijieRouteVrfName_Type(DisplayString):
    """Custom type ruijieRouteVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieRouteVrfName_Type.__name__ = "DisplayString"
_RuijieRouteVrfName_Object = MibScalar
ruijieRouteVrfName = _RuijieRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 5),
    _RuijieRouteVrfName_Type()
)
ruijieRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteVrfName.setStatus("current")
_RuijieAddressFamilyAfi_Type = AddressFamilyNumbers
_RuijieAddressFamilyAfi_Object = MibScalar
ruijieAddressFamilyAfi = _RuijieAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 6),
    _RuijieAddressFamilyAfi_Type()
)
ruijieAddressFamilyAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAddressFamilyAfi.setStatus("current")
_RuijieRouteLimitNum_Type = Unsigned32
_RuijieRouteLimitNum_Object = MibScalar
ruijieRouteLimitNum = _RuijieRouteLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 7),
    _RuijieRouteLimitNum_Type()
)
ruijieRouteLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteLimitNum.setStatus("current")


class _RuijieRouteLimitThreshold_Type(Integer32):
    """Custom type ruijieRouteLimitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRouteLimitThreshold_Type.__name__ = "Integer32"
_RuijieRouteLimitThreshold_Object = MibScalar
ruijieRouteLimitThreshold = _RuijieRouteLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 8),
    _RuijieRouteLimitThreshold_Type()
)
ruijieRouteLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteLimitThreshold.setStatus("current")
_RuijieRouteLimitCurrentNum_Type = Unsigned32
_RuijieRouteLimitCurrentNum_Object = MibScalar
ruijieRouteLimitCurrentNum = _RuijieRouteLimitCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 9),
    _RuijieRouteLimitCurrentNum_Type()
)
ruijieRouteLimitCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRouteLimitCurrentNum.setStatus("current")

# Managed Objects groups

ruijieRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 1)
)
ruijieRouteMIBGroup.setObjects(
    ("RUIJIE-ROUTE-MIB", "ruijieRouteServiceStatus")
)
if mibBuilder.loadTexts:
    ruijieRouteMIBGroup.setStatus("current")

ruijieRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 2)
)
ruijieRouteInfoMIBGroup.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRoutingProtoInfoProtoType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRoutingProtoInfoGateWay"),
        ("RUIJIE-ROUTE-MIB", "ruijieRoutingProtoInfoDistance"),
        ("RUIJIE-ROUTE-MIB", "ruijieRoutingProtoInfoLastUpdate"),
        ("RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgRoutingProtoType"),
        ("RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgAlways"),
        ("RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgMetric"),
        ("RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgMetricType"),
        ("RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgRouteMap"),
        ("RUIJIE-ROUTE-MIB", "ruijieDefRoutingCfgStatus"))
)
if mibBuilder.loadTexts:
    ruijieRouteInfoMIBGroup.setStatus("current")

ruijieRouteMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 3)
)
ruijieRouteMapMIBGroup.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteMapName"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapSequenceNumber"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapOperType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchMetric"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchRouteType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMetricValueType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapSetMetric"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapSetLevel"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapSetMetricType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapSetNexthopSt"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapSetNexthopSt"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapStatus"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchIpAddressAclName"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchIpAddressStatus"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchTagValue"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchTagStatus"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchInterfaceIfIndex"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMatchInterfaceStatus"))
)
if mibBuilder.loadTexts:
    ruijieRouteMapMIBGroup.setStatus("current")

ruijieRouteRedistributeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 4)
)
ruijieRouteRedistributeMIBGroup.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeProtocolCfg"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeProtocol"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeMetricValue"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeMetricType"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeTagValue"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeRouteMapName"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeStatus"))
)
if mibBuilder.loadTexts:
    ruijieRouteRedistributeMIBGroup.setStatus("current")

ruijieRouteFilteringMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 5)
)
ruijieRouteFilteringMibGroup.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListName"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListSequence"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListOperMethod"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListIpAddress"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListMaskLength"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListMinimumPrefixLength"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListMaximumPrefixLength"),
        ("RUIJIE-ROUTE-MIB", "ruijieIpPrefixListStatus"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListCfgProtoType"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListIfIndex"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListFilterType"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListDirection"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListAclName"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListGateWayIpPrefixName"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListPrefixIpPrefixName"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListFilteringProtocol"),
        ("RUIJIE-ROUTE-MIB", "ruijieDistributeListStatus"))
)
if mibBuilder.loadTexts:
    ruijieRouteFilteringMibGroup.setStatus("current")

ruijieipCidrRouteMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 2, 6)
)
ruijieipCidrRouteMibGroup.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteDest"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMask"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteTos"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteNextHop"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteIfIndex"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteType"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteProto"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteAge"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteInfo"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteNextHopAS"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMetric1"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMetric2"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMetric3"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMetric4"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMetric5"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteStatus"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrOspfRouteType"))
)
if mibBuilder.loadTexts:
    ruijieipCidrRouteMibGroup.setStatus("current")


# Notification objects

ruijieVrfRouteThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 1)
)
ruijieVrfRouteThresholdExceed.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteVrfName"),
        ("RUIJIE-ROUTE-MIB", "ruijieAddressFamilyAfi"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitNum"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitThreshold"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitCurrentNum"))
)
if mibBuilder.loadTexts:
    ruijieVrfRouteThresholdExceed.setStatus(
        "current"
    )

ruijieVrfRouteThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 2)
)
ruijieVrfRouteThresholdClear.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteVrfName"),
        ("RUIJIE-ROUTE-MIB", "ruijieAddressFamilyAfi"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitNum"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitThreshold"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitCurrentNum"))
)
if mibBuilder.loadTexts:
    ruijieVrfRouteThresholdClear.setStatus(
        "current"
    )

ruijieVrfRouteExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 3)
)
ruijieVrfRouteExceed.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteVrfName"),
        ("RUIJIE-ROUTE-MIB", "ruijieAddressFamilyAfi"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitNum"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitCurrentNum"))
)
if mibBuilder.loadTexts:
    ruijieVrfRouteExceed.setStatus(
        "current"
    )

ruijieVrfRouteExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 4)
)
ruijieVrfRouteExceedClear.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteVrfName"),
        ("RUIJIE-ROUTE-MIB", "ruijieAddressFamilyAfi"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitNum"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteLimitCurrentNum"))
)
if mibBuilder.loadTexts:
    ruijieVrfRouteExceedClear.setStatus(
        "current"
    )

ruijieVrfMplsL3VpnRouteMidClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 7, 10)
)
ruijieVrfMplsL3VpnRouteMidClear.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfCurrNumRoutes"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfMidRteThresh"))
)
if mibBuilder.loadTexts:
    ruijieVrfMplsL3VpnRouteMidClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 20, 6, 1, 1)
)
ruijieRouteMIBCompliance.setObjects(
      *(("RUIJIE-ROUTE-MIB", "ruijieRouteMIBGroup"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteInfoMIBGroup"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteMapMIBGroup"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteRedistributeMIBGroup"),
        ("RUIJIE-ROUTE-MIB", "ruijieRouteFilteringMibGroup"),
        ("RUIJIE-ROUTE-MIB", "ruijieipCidrRouteMibGroup"))
)
if mibBuilder.loadTexts:
    ruijieRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ROUTE-MIB",
    **{"RuijieRouteProtoType": RuijieRouteProtoType,
       "ruijieRouteMIB": ruijieRouteMIB,
       "ruijieRouteMIBObjects": ruijieRouteMIBObjects,
       "ruijieRouteServiceStatus": ruijieRouteServiceStatus,
       "ruijieRoutingProtoInfoTable": ruijieRoutingProtoInfoTable,
       "ruijieRoutingProtoInfoEntry": ruijieRoutingProtoInfoEntry,
       "ruijieRoutingProtoInfoProtoType": ruijieRoutingProtoInfoProtoType,
       "ruijieRoutingProtoInfoGateWay": ruijieRoutingProtoInfoGateWay,
       "ruijieRoutingProtoInfoDistance": ruijieRoutingProtoInfoDistance,
       "ruijieRoutingProtoInfoLastUpdate": ruijieRoutingProtoInfoLastUpdate,
       "ruijieDefRoutingCfgTable": ruijieDefRoutingCfgTable,
       "ruijieDefRoutingCfgEntry": ruijieDefRoutingCfgEntry,
       "ruijieDefRoutingCfgRoutingProtoType": ruijieDefRoutingCfgRoutingProtoType,
       "ruijieDefRoutingCfgAlways": ruijieDefRoutingCfgAlways,
       "ruijieDefRoutingCfgMetric": ruijieDefRoutingCfgMetric,
       "ruijieDefRoutingCfgMetricType": ruijieDefRoutingCfgMetricType,
       "ruijieDefRoutingCfgRouteMap": ruijieDefRoutingCfgRouteMap,
       "ruijieDefRoutingCfgStatus": ruijieDefRoutingCfgStatus,
       "ruijieRouteMapMIBObjects": ruijieRouteMapMIBObjects,
       "ruijieRouteMapTable": ruijieRouteMapTable,
       "ruijieRouteMapEntry": ruijieRouteMapEntry,
       "ruijieRouteMapName": ruijieRouteMapName,
       "ruijieRouteMapSequenceNumber": ruijieRouteMapSequenceNumber,
       "ruijieRouteMapOperType": ruijieRouteMapOperType,
       "ruijieRouteMapMatchMetric": ruijieRouteMapMatchMetric,
       "ruijieRouteMapMatchRouteType": ruijieRouteMapMatchRouteType,
       "ruijieRouteMapMetricValueType": ruijieRouteMapMetricValueType,
       "ruijieRouteMapSetMetric": ruijieRouteMapSetMetric,
       "ruijieRouteMapSetLevel": ruijieRouteMapSetLevel,
       "ruijieRouteMapSetMetricType": ruijieRouteMapSetMetricType,
       "ruijieRouteMapSetNexthopSt": ruijieRouteMapSetNexthopSt,
       "ruijieRouteMapSetNexthop": ruijieRouteMapSetNexthop,
       "ruijieRouteMapStatus": ruijieRouteMapStatus,
       "ruijieRouteMapMatchIpAddressTable": ruijieRouteMapMatchIpAddressTable,
       "ruijieRouteMapMatchIpAddressEntry": ruijieRouteMapMatchIpAddressEntry,
       "ruijieRouteMapMatchType": ruijieRouteMapMatchType,
       "ruijieRouteMapMatchIpAddressAclName": ruijieRouteMapMatchIpAddressAclName,
       "ruijieRouteMapMatchIpAddressStatus": ruijieRouteMapMatchIpAddressStatus,
       "ruijieRouteMapMatchTagTable": ruijieRouteMapMatchTagTable,
       "ruijieRouteMapMatchTagEntry": ruijieRouteMapMatchTagEntry,
       "ruijieRouteMapMatchTagValue": ruijieRouteMapMatchTagValue,
       "ruijieRouteMapMatchTagStatus": ruijieRouteMapMatchTagStatus,
       "ruijieRouteMapMatchInterfaceTable": ruijieRouteMapMatchInterfaceTable,
       "ruijieRouteMapMatchInterfaceEntry": ruijieRouteMapMatchInterfaceEntry,
       "ruijieRouteMapMatchInterfaceIfIndex": ruijieRouteMapMatchInterfaceIfIndex,
       "ruijieRouteMapMatchInterfaceStatus": ruijieRouteMapMatchInterfaceStatus,
       "ruijieRouteRedistributeMIBObjects": ruijieRouteRedistributeMIBObjects,
       "ruijieRouteRedistributeTable": ruijieRouteRedistributeTable,
       "ruijieRouteRedistributeEntry": ruijieRouteRedistributeEntry,
       "ruijieRouteRedistributeProtocolCfg": ruijieRouteRedistributeProtocolCfg,
       "ruijieRouteRedistributeProtocol": ruijieRouteRedistributeProtocol,
       "ruijieRouteRedistributeMetricValue": ruijieRouteRedistributeMetricValue,
       "ruijieRouteRedistributeMetricType": ruijieRouteRedistributeMetricType,
       "ruijieRouteRedistributeTagValue": ruijieRouteRedistributeTagValue,
       "ruijieRouteRedistributeRouteMapName": ruijieRouteRedistributeRouteMapName,
       "ruijieRouteRedistributeStatus": ruijieRouteRedistributeStatus,
       "ruijieRouteFilteringMIBObjects": ruijieRouteFilteringMIBObjects,
       "ruijieIpPrefixListTable": ruijieIpPrefixListTable,
       "ruijieIpPrefixListEntry": ruijieIpPrefixListEntry,
       "ruijieIpPrefixListName": ruijieIpPrefixListName,
       "ruijieIpPrefixListSequence": ruijieIpPrefixListSequence,
       "ruijieIpPrefixListOperMethod": ruijieIpPrefixListOperMethod,
       "ruijieIpPrefixListIpAddress": ruijieIpPrefixListIpAddress,
       "ruijieIpPrefixListMaskLength": ruijieIpPrefixListMaskLength,
       "ruijieIpPrefixListMinimumPrefixLength": ruijieIpPrefixListMinimumPrefixLength,
       "ruijieIpPrefixListMaximumPrefixLength": ruijieIpPrefixListMaximumPrefixLength,
       "ruijieIpPrefixListStatus": ruijieIpPrefixListStatus,
       "ruijieDistributeListTable": ruijieDistributeListTable,
       "ruijieDistributeListEntry": ruijieDistributeListEntry,
       "ruijieDistributeListCfgProtoType": ruijieDistributeListCfgProtoType,
       "ruijieDistributeListIfIndex": ruijieDistributeListIfIndex,
       "ruijieDistributeListDirection": ruijieDistributeListDirection,
       "ruijieDistributeListFilteringProtocol": ruijieDistributeListFilteringProtocol,
       "ruijieDistributeListFilterType": ruijieDistributeListFilterType,
       "ruijieDistributeListAclName": ruijieDistributeListAclName,
       "ruijieDistributeListGateWayIpPrefixName": ruijieDistributeListGateWayIpPrefixName,
       "ruijieDistributeListPrefixIpPrefixName": ruijieDistributeListPrefixIpPrefixName,
       "ruijieDistributeListStatus": ruijieDistributeListStatus,
       "ruijieipCidrRouteExtendMIBObjects": ruijieipCidrRouteExtendMIBObjects,
       "ruijieipCidrRouteTable": ruijieipCidrRouteTable,
       "ruijieipCidrRouteEntry": ruijieipCidrRouteEntry,
       "ruijieipCidrRouteDest": ruijieipCidrRouteDest,
       "ruijieipCidrRouteMask": ruijieipCidrRouteMask,
       "ruijieipCidrRouteTos": ruijieipCidrRouteTos,
       "ruijieipCidrRouteNextHop": ruijieipCidrRouteNextHop,
       "ruijieipCidrRouteIfIndex": ruijieipCidrRouteIfIndex,
       "ruijieipCidrRouteType": ruijieipCidrRouteType,
       "ruijieipCidrRouteProto": ruijieipCidrRouteProto,
       "ruijieipCidrRouteAge": ruijieipCidrRouteAge,
       "ruijieipCidrRouteInfo": ruijieipCidrRouteInfo,
       "ruijieipCidrRouteNextHopAS": ruijieipCidrRouteNextHopAS,
       "ruijieipCidrRouteMetric1": ruijieipCidrRouteMetric1,
       "ruijieipCidrRouteMetric2": ruijieipCidrRouteMetric2,
       "ruijieipCidrRouteMetric3": ruijieipCidrRouteMetric3,
       "ruijieipCidrRouteMetric4": ruijieipCidrRouteMetric4,
       "ruijieipCidrRouteMetric5": ruijieipCidrRouteMetric5,
       "ruijieipCidrRouteStatus": ruijieipCidrRouteStatus,
       "ruijieipCidrOspfRouteType": ruijieipCidrOspfRouteType,
       "ruijieRouteMIBConformance": ruijieRouteMIBConformance,
       "ruijieRouteMIBCompliances": ruijieRouteMIBCompliances,
       "ruijieRouteMIBCompliance": ruijieRouteMIBCompliance,
       "ruijieRouteMIBGroups": ruijieRouteMIBGroups,
       "ruijieRouteMIBGroup": ruijieRouteMIBGroup,
       "ruijieRouteInfoMIBGroup": ruijieRouteInfoMIBGroup,
       "ruijieRouteMapMIBGroup": ruijieRouteMapMIBGroup,
       "ruijieRouteRedistributeMIBGroup": ruijieRouteRedistributeMIBGroup,
       "ruijieRouteFilteringMibGroup": ruijieRouteFilteringMibGroup,
       "ruijieipCidrRouteMibGroup": ruijieipCidrRouteMibGroup,
       "ruijieRouteTrap": ruijieRouteTrap,
       "ruijieVrfRouteThresholdExceed": ruijieVrfRouteThresholdExceed,
       "ruijieVrfRouteThresholdClear": ruijieVrfRouteThresholdClear,
       "ruijieVrfRouteExceed": ruijieVrfRouteExceed,
       "ruijieVrfRouteExceedClear": ruijieVrfRouteExceedClear,
       "ruijieRouteVrfName": ruijieRouteVrfName,
       "ruijieAddressFamilyAfi": ruijieAddressFamilyAfi,
       "ruijieRouteLimitNum": ruijieRouteLimitNum,
       "ruijieRouteLimitThreshold": ruijieRouteLimitThreshold,
       "ruijieRouteLimitCurrentNum": ruijieRouteLimitCurrentNum,
       "ruijieVrfMplsL3VpnRouteMidClear": ruijieVrfMplsL3VpnRouteMidClear}
)
