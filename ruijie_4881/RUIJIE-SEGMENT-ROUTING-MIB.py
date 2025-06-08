# SNMP MIB module (RUIJIE-SEGMENT-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SEGMENT-ROUTING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:10 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieSegmentRoutingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163)
)
if mibBuilder.loadTexts:
    ruijieSegmentRoutingMIB.setRevisions(
        ("2019-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSegmentRoutingMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSegmentRoutingMIBObjects = _RuijieSegmentRoutingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1)
)
_RuijieSegmentRoutingCounterTable_Object = MibTable
ruijieSegmentRoutingCounterTable = _RuijieSegmentRoutingCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieSegmentRoutingCounterTable.setStatus("current")
_RuijieSegmentRoutingCounterEntry_Object = MibTableRow
ruijieSegmentRoutingCounterEntry = _RuijieSegmentRoutingCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1)
)
ruijieSegmentRoutingCounterEntry.setIndexNames(
    (0, "RUIJIE-SEGMENT-ROUTING-MIB", "segmentListID"),
)
if mibBuilder.loadTexts:
    ruijieSegmentRoutingCounterEntry.setStatus("current")
_SegmentListID_Type = Gauge32
_SegmentListID_Object = MibTableColumn
segmentListID = _SegmentListID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 1),
    _SegmentListID_Type()
)
segmentListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListID.setStatus("current")


class _SegmentListName_Type(DisplayString):
    """Custom type segmentListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SegmentListName_Type.__name__ = "DisplayString"
_SegmentListName_Object = MibTableColumn
segmentListName = _SegmentListName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 2),
    _SegmentListName_Type()
)
segmentListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListName.setStatus("current")
_SegmentListPkts_Type = Counter64
_SegmentListPkts_Object = MibTableColumn
segmentListPkts = _SegmentListPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 3),
    _SegmentListPkts_Type()
)
segmentListPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListPkts.setStatus("current")
_SegmentListOctets_Type = Counter64
_SegmentListOctets_Object = MibTableColumn
segmentListOctets = _SegmentListOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 4),
    _SegmentListOctets_Type()
)
segmentListOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListOctets.setStatus("current")
_SegmentListAvgPktsRate_Type = Counter64
_SegmentListAvgPktsRate_Object = MibTableColumn
segmentListAvgPktsRate = _SegmentListAvgPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 5),
    _SegmentListAvgPktsRate_Type()
)
segmentListAvgPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListAvgPktsRate.setStatus("current")
_SegmentListAvgOctetsRate_Type = Counter64
_SegmentListAvgOctetsRate_Object = MibTableColumn
segmentListAvgOctetsRate = _SegmentListAvgOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 6),
    _SegmentListAvgOctetsRate_Type()
)
segmentListAvgOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListAvgOctetsRate.setStatus("current")
_SegmentListPeakPktsRate_Type = Counter64
_SegmentListPeakPktsRate_Object = MibTableColumn
segmentListPeakPktsRate = _SegmentListPeakPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 7),
    _SegmentListPeakPktsRate_Type()
)
segmentListPeakPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListPeakPktsRate.setStatus("current")
_SegmentListPeakOctetsRate_Type = Counter64
_SegmentListPeakOctetsRate_Object = MibTableColumn
segmentListPeakOctetsRate = _SegmentListPeakOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 8),
    _SegmentListPeakOctetsRate_Type()
)
segmentListPeakOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListPeakOctetsRate.setStatus("current")
_SegmentListPeakRateTime_Type = DisplayString
_SegmentListPeakRateTime_Object = MibTableColumn
segmentListPeakRateTime = _SegmentListPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 9),
    _SegmentListPeakRateTime_Type()
)
segmentListPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentListPeakRateTime.setStatus("current")
_RuijieSegmentRoutingMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSegmentRoutingMIBConformance = _RuijieSegmentRoutingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 3)
)
_RuijieSegmentRoutingMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSegmentRoutingMIBCompliances = _RuijieSegmentRoutingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 3, 1)
)
_RuijieSegmentRoutingMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSegmentRoutingMIBGroups = _RuijieSegmentRoutingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 3, 2)
)

# Managed Objects groups

ruijieSegmentRoutingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 3, 2, 1)
)
ruijieSegmentRoutingMIBGroup.setObjects(
      *(("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListID"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListName"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListPkts"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListOctets"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListAvgPktsRate"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListAvgOctetsRate"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListPeakPktsRate"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListPeakOctetsRate"),
        ("RUIJIE-SEGMENT-ROUTING-MIB", "segmentListPeakRateTime"))
)
if mibBuilder.loadTexts:
    ruijieSegmentRoutingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSegmentRoutingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 3, 1, 1)
)
ruijieSegmentRoutingMIBCompliance.setObjects(
    ("RUIJIE-SEGMENT-ROUTING-MIB", "ruijieSegmentRoutingMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieSegmentRoutingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SEGMENT-ROUTING-MIB",
    **{"ruijieSegmentRoutingMIB": ruijieSegmentRoutingMIB,
       "ruijieSegmentRoutingMIBObjects": ruijieSegmentRoutingMIBObjects,
       "ruijieSegmentRoutingCounterTable": ruijieSegmentRoutingCounterTable,
       "ruijieSegmentRoutingCounterEntry": ruijieSegmentRoutingCounterEntry,
       "segmentListID": segmentListID,
       "segmentListName": segmentListName,
       "segmentListPkts": segmentListPkts,
       "segmentListOctets": segmentListOctets,
       "segmentListAvgPktsRate": segmentListAvgPktsRate,
       "segmentListAvgOctetsRate": segmentListAvgOctetsRate,
       "segmentListPeakPktsRate": segmentListPeakPktsRate,
       "segmentListPeakOctetsRate": segmentListPeakOctetsRate,
       "segmentListPeakRateTime": segmentListPeakRateTime,
       "ruijieSegmentRoutingMIBConformance": ruijieSegmentRoutingMIBConformance,
       "ruijieSegmentRoutingMIBCompliances": ruijieSegmentRoutingMIBCompliances,
       "ruijieSegmentRoutingMIBCompliance": ruijieSegmentRoutingMIBCompliance,
       "ruijieSegmentRoutingMIBGroups": ruijieSegmentRoutingMIBGroups,
       "ruijieSegmentRoutingMIBGroup": ruijieSegmentRoutingMIBGroup}
)
