# SNMP MIB module (ARISTA-FIB-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-FIB-STATS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(InetAddressPrefixLength,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength",
    "InetVersion")

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

aristaFIBStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23)
)
if mibBuilder.loadTexts:
    aristaFIBStatsMIB.setRevisions(
        ("2017-05-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RouteType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9,
              13,
              14,
              200,
              201,
              202,
              203,
              204,
              205)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 8),
          ("isIs", 9),
          ("ospf", 13),
          ("bgp", 14),
          ("ospfv3", 200),
          ("staticNonPersistent", 201),
          ("staticNexthopGroup", 202),
          ("attached", 203),
          ("vcs", 204),
          ("internal", 205))
    )



# MIB Managed Objects in the order of their OIDs

_AristaFIBStatsMibObjects_ObjectIdentity = ObjectIdentity
aristaFIBStatsMibObjects = _AristaFIBStatsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1)
)
_AristaFIBStatsSummaryTable_Object = MibTable
aristaFIBStatsSummaryTable = _AristaFIBStatsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1)
)
if mibBuilder.loadTexts:
    aristaFIBStatsSummaryTable.setStatus("current")
_AristaFIBStatsSummaryEntry_Object = MibTableRow
aristaFIBStatsSummaryEntry = _AristaFIBStatsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1, 1)
)
aristaFIBStatsSummaryEntry.setIndexNames(
    (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsAF"),
)
if mibBuilder.loadTexts:
    aristaFIBStatsSummaryEntry.setStatus("current")
_AristaFIBStatsAF_Type = InetVersion
_AristaFIBStatsAF_Object = MibTableColumn
aristaFIBStatsAF = _AristaFIBStatsAF_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1, 1, 1),
    _AristaFIBStatsAF_Type()
)
aristaFIBStatsAF.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaFIBStatsAF.setStatus("current")
_AristaFIBStatsTotalRoutes_Type = Gauge32
_AristaFIBStatsTotalRoutes_Object = MibTableColumn
aristaFIBStatsTotalRoutes = _AristaFIBStatsTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 1, 1, 2),
    _AristaFIBStatsTotalRoutes_Type()
)
aristaFIBStatsTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaFIBStatsTotalRoutes.setStatus("current")
_AristaFIBStatsByRouteTypeTable_Object = MibTable
aristaFIBStatsByRouteTypeTable = _AristaFIBStatsByRouteTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2)
)
if mibBuilder.loadTexts:
    aristaFIBStatsByRouteTypeTable.setStatus("current")
_AristaFIBStatsByRouteTypeEntry_Object = MibTableRow
aristaFIBStatsByRouteTypeEntry = _AristaFIBStatsByRouteTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2, 1)
)
aristaFIBStatsByRouteTypeEntry.setIndexNames(
    (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsAF"),
    (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsRouteType"),
)
if mibBuilder.loadTexts:
    aristaFIBStatsByRouteTypeEntry.setStatus("current")
_AristaFIBStatsRouteType_Type = RouteType
_AristaFIBStatsRouteType_Object = MibTableColumn
aristaFIBStatsRouteType = _AristaFIBStatsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2, 1, 1),
    _AristaFIBStatsRouteType_Type()
)
aristaFIBStatsRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaFIBStatsRouteType.setStatus("current")
_AristaFIBStatsTotalRoutesForRouteType_Type = Gauge32
_AristaFIBStatsTotalRoutesForRouteType_Object = MibTableColumn
aristaFIBStatsTotalRoutesForRouteType = _AristaFIBStatsTotalRoutesForRouteType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 2, 1, 2),
    _AristaFIBStatsTotalRoutesForRouteType_Type()
)
aristaFIBStatsTotalRoutesForRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaFIBStatsTotalRoutesForRouteType.setStatus("current")
_AristaFIBStatsByPrefixLenTable_Object = MibTable
aristaFIBStatsByPrefixLenTable = _AristaFIBStatsByPrefixLenTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3)
)
if mibBuilder.loadTexts:
    aristaFIBStatsByPrefixLenTable.setStatus("current")
_AristaFIBStatsByPrefixLenEntry_Object = MibTableRow
aristaFIBStatsByPrefixLenEntry = _AristaFIBStatsByPrefixLenEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3, 1)
)
aristaFIBStatsByPrefixLenEntry.setIndexNames(
    (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsAF"),
    (0, "ARISTA-FIB-STATS-MIB", "aristaFIBStatsPrefixLen"),
)
if mibBuilder.loadTexts:
    aristaFIBStatsByPrefixLenEntry.setStatus("current")
_AristaFIBStatsPrefixLen_Type = InetAddressPrefixLength
_AristaFIBStatsPrefixLen_Object = MibTableColumn
aristaFIBStatsPrefixLen = _AristaFIBStatsPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3, 1, 1),
    _AristaFIBStatsPrefixLen_Type()
)
aristaFIBStatsPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaFIBStatsPrefixLen.setStatus("current")
_AristaFIBStatsTotalRoutesForPrefixLen_Type = Gauge32
_AristaFIBStatsTotalRoutesForPrefixLen_Object = MibTableColumn
aristaFIBStatsTotalRoutesForPrefixLen = _AristaFIBStatsTotalRoutesForPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 1, 3, 1, 2),
    _AristaFIBStatsTotalRoutesForPrefixLen_Type()
)
aristaFIBStatsTotalRoutesForPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaFIBStatsTotalRoutesForPrefixLen.setStatus("current")
_AristaFIBStatsMibConformance_ObjectIdentity = ObjectIdentity
aristaFIBStatsMibConformance = _AristaFIBStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 2)
)
_AristaFIBStatsMibCompliances_ObjectIdentity = ObjectIdentity
aristaFIBStatsMibCompliances = _AristaFIBStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 1)
)
_AristaFIBStatsMibGroups_ObjectIdentity = ObjectIdentity
aristaFIBStatsMibGroups = _AristaFIBStatsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 2)
)

# Managed Objects groups

aristaFIBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 2, 1)
)
aristaFIBStatsGroup.setObjects(
      *(("ARISTA-FIB-STATS-MIB", "aristaFIBStatsTotalRoutes"),
        ("ARISTA-FIB-STATS-MIB", "aristaFIBStatsTotalRoutesForRouteType"),
        ("ARISTA-FIB-STATS-MIB", "aristaFIBStatsTotalRoutesForPrefixLen"))
)
if mibBuilder.loadTexts:
    aristaFIBStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaFIBStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 23, 2, 1, 1)
)
aristaFIBStatsMibCompliance.setObjects(
    ("ARISTA-FIB-STATS-MIB", "aristaFIBStatsGroup")
)
if mibBuilder.loadTexts:
    aristaFIBStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-FIB-STATS-MIB",
    **{"RouteType": RouteType,
       "aristaFIBStatsMIB": aristaFIBStatsMIB,
       "aristaFIBStatsMibObjects": aristaFIBStatsMibObjects,
       "aristaFIBStatsSummaryTable": aristaFIBStatsSummaryTable,
       "aristaFIBStatsSummaryEntry": aristaFIBStatsSummaryEntry,
       "aristaFIBStatsAF": aristaFIBStatsAF,
       "aristaFIBStatsTotalRoutes": aristaFIBStatsTotalRoutes,
       "aristaFIBStatsByRouteTypeTable": aristaFIBStatsByRouteTypeTable,
       "aristaFIBStatsByRouteTypeEntry": aristaFIBStatsByRouteTypeEntry,
       "aristaFIBStatsRouteType": aristaFIBStatsRouteType,
       "aristaFIBStatsTotalRoutesForRouteType": aristaFIBStatsTotalRoutesForRouteType,
       "aristaFIBStatsByPrefixLenTable": aristaFIBStatsByPrefixLenTable,
       "aristaFIBStatsByPrefixLenEntry": aristaFIBStatsByPrefixLenEntry,
       "aristaFIBStatsPrefixLen": aristaFIBStatsPrefixLen,
       "aristaFIBStatsTotalRoutesForPrefixLen": aristaFIBStatsTotalRoutesForPrefixLen,
       "aristaFIBStatsMibConformance": aristaFIBStatsMibConformance,
       "aristaFIBStatsMibCompliances": aristaFIBStatsMibCompliances,
       "aristaFIBStatsMibCompliance": aristaFIBStatsMibCompliance,
       "aristaFIBStatsMibGroups": aristaFIBStatsMibGroups,
       "aristaFIBStatsGroup": aristaFIBStatsGroup}
)
