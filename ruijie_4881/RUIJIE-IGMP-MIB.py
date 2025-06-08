# SNMP MIB module (RUIJIE-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IGMP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

ruijieIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26)
)
if mibBuilder.loadTexts:
    ruijieIgmpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIgmpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIgmpMIBObjects = _RuijieIgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1)
)
_RuijieIgmpInterfaceTable_Object = MibTable
ruijieIgmpInterfaceTable = _RuijieIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceTable.setStatus("current")
_RuijieIgmpInterfaceEntry_Object = MibTableRow
ruijieIgmpInterfaceEntry = _RuijieIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1)
)
ruijieIgmpInterfaceEntry.setIndexNames(
    (0, "RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceEntry.setStatus("current")
_RuijieIgmpInterfaceIfIndex_Type = InterfaceIndex
_RuijieIgmpInterfaceIfIndex_Object = MibTableColumn
ruijieIgmpInterfaceIfIndex = _RuijieIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 1),
    _RuijieIgmpInterfaceIfIndex_Type()
)
ruijieIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceIfIndex.setStatus("current")


class _RuijieIgmpInterfaceQueryInterval_Type(Unsigned32):
    """Custom type ruijieIgmpInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieIgmpInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_RuijieIgmpInterfaceQueryInterval_Object = MibTableColumn
ruijieIgmpInterfaceQueryInterval = _RuijieIgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 2),
    _RuijieIgmpInterfaceQueryInterval_Type()
)
ruijieIgmpInterfaceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQueryInterval.setUnits("seconds")


class _RuijieIgmpInterfaceVersion_Type(Unsigned32):
    """Custom type ruijieIgmpInterfaceVersion based on Unsigned32"""
    defaultValue = 2


_RuijieIgmpInterfaceVersion_Type.__name__ = "Unsigned32"
_RuijieIgmpInterfaceVersion_Object = MibTableColumn
ruijieIgmpInterfaceVersion = _RuijieIgmpInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 3),
    _RuijieIgmpInterfaceVersion_Type()
)
ruijieIgmpInterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceVersion.setStatus("current")
_RuijieIgmpInterfaceQuerier_Type = IpAddress
_RuijieIgmpInterfaceQuerier_Object = MibTableColumn
ruijieIgmpInterfaceQuerier = _RuijieIgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 4),
    _RuijieIgmpInterfaceQuerier_Type()
)
ruijieIgmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQuerier.setStatus("current")


class _RuijieIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type ruijieIgmpInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_RuijieIgmpInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_RuijieIgmpInterfaceQueryMaxResponseTime_Object = MibTableColumn
ruijieIgmpInterfaceQueryMaxResponseTime = _RuijieIgmpInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 5),
    _RuijieIgmpInterfaceQueryMaxResponseTime_Type()
)
ruijieIgmpInterfaceQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_RuijieIgmpInterfaceQuerierUpTime_Type = TimeTicks
_RuijieIgmpInterfaceQuerierUpTime_Object = MibTableColumn
ruijieIgmpInterfaceQuerierUpTime = _RuijieIgmpInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 6),
    _RuijieIgmpInterfaceQuerierUpTime_Type()
)
ruijieIgmpInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQuerierUpTime.setStatus("current")
_RuijieIgmpInterfaceQuerierExpiryTime_Type = TimeTicks
_RuijieIgmpInterfaceQuerierExpiryTime_Object = MibTableColumn
ruijieIgmpInterfaceQuerierExpiryTime = _RuijieIgmpInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 7),
    _RuijieIgmpInterfaceQuerierExpiryTime_Type()
)
ruijieIgmpInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQuerierExpiryTime.setStatus("current")
_RuijieIgmpInterfaceVersion1QuerierTimer_Type = TimeTicks
_RuijieIgmpInterfaceVersion1QuerierTimer_Object = MibTableColumn
ruijieIgmpInterfaceVersion1QuerierTimer = _RuijieIgmpInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 8),
    _RuijieIgmpInterfaceVersion1QuerierTimer_Type()
)
ruijieIgmpInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceVersion1QuerierTimer.setStatus("current")
_RuijieIgmpInterfaceWrongVersionQueries_Type = Counter32
_RuijieIgmpInterfaceWrongVersionQueries_Object = MibTableColumn
ruijieIgmpInterfaceWrongVersionQueries = _RuijieIgmpInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 9),
    _RuijieIgmpInterfaceWrongVersionQueries_Type()
)
ruijieIgmpInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceWrongVersionQueries.setStatus("current")
_RuijieIgmpInterfaceJoins_Type = Counter32
_RuijieIgmpInterfaceJoins_Object = MibTableColumn
ruijieIgmpInterfaceJoins = _RuijieIgmpInterfaceJoins_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 10),
    _RuijieIgmpInterfaceJoins_Type()
)
ruijieIgmpInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceJoins.setStatus("current")


class _RuijieIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ruijieIgmpInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RuijieIgmpInterfaceProxyIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_RuijieIgmpInterfaceProxyIfIndex_Object = MibTableColumn
ruijieIgmpInterfaceProxyIfIndex = _RuijieIgmpInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 11),
    _RuijieIgmpInterfaceProxyIfIndex_Type()
)
ruijieIgmpInterfaceProxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceProxyIfIndex.setStatus("obsolete")
_RuijieIgmpInterfaceGroups_Type = Gauge32
_RuijieIgmpInterfaceGroups_Object = MibTableColumn
ruijieIgmpInterfaceGroups = _RuijieIgmpInterfaceGroups_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 12),
    _RuijieIgmpInterfaceGroups_Type()
)
ruijieIgmpInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceGroups.setStatus("current")


class _RuijieIgmpInterfaceRobustness_Type(Unsigned32):
    """Custom type ruijieIgmpInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieIgmpInterfaceRobustness_Type.__name__ = "Unsigned32"
_RuijieIgmpInterfaceRobustness_Object = MibTableColumn
ruijieIgmpInterfaceRobustness = _RuijieIgmpInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 13),
    _RuijieIgmpInterfaceRobustness_Type()
)
ruijieIgmpInterfaceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceRobustness.setStatus("current")


class _RuijieIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type ruijieIgmpInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_RuijieIgmpInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_RuijieIgmpInterfaceLastMembQueryIntvl_Object = MibTableColumn
ruijieIgmpInterfaceLastMembQueryIntvl = _RuijieIgmpInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 14),
    _RuijieIgmpInterfaceLastMembQueryIntvl_Type()
)
ruijieIgmpInterfaceLastMembQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")


class _RuijieIgmpInterfaceQuerierPresentTimeout_Type(Integer32):
    """Custom type ruijieIgmpInterfaceQuerierPresentTimeout based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_RuijieIgmpInterfaceQuerierPresentTimeout_Type.__name__ = "Integer32"
_RuijieIgmpInterfaceQuerierPresentTimeout_Object = MibTableColumn
ruijieIgmpInterfaceQuerierPresentTimeout = _RuijieIgmpInterfaceQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 15),
    _RuijieIgmpInterfaceQuerierPresentTimeout_Type()
)
ruijieIgmpInterfaceQuerierPresentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQuerierPresentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceQuerierPresentTimeout.setUnits("seconds")
_RuijieIgmpInterfaceLeaves_Type = Counter32
_RuijieIgmpInterfaceLeaves_Object = MibTableColumn
ruijieIgmpInterfaceLeaves = _RuijieIgmpInterfaceLeaves_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 16),
    _RuijieIgmpInterfaceLeaves_Type()
)
ruijieIgmpInterfaceLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceLeaves.setStatus("current")


class _RuijieIgmpInterfaceAccessGroupAclName_Type(DisplayString):
    """Custom type ruijieIgmpInterfaceAccessGroupAclName based on DisplayString"""
    defaultValue = OctetString("")


_RuijieIgmpInterfaceAccessGroupAclName_Type.__name__ = "DisplayString"
_RuijieIgmpInterfaceAccessGroupAclName_Object = MibTableColumn
ruijieIgmpInterfaceAccessGroupAclName = _RuijieIgmpInterfaceAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 17),
    _RuijieIgmpInterfaceAccessGroupAclName_Type()
)
ruijieIgmpInterfaceAccessGroupAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceAccessGroupAclName.setStatus("current")
_RuijieIgmpInterfaceEnabled_Type = EnabledStatus
_RuijieIgmpInterfaceEnabled_Object = MibTableColumn
ruijieIgmpInterfaceEnabled = _RuijieIgmpInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 18),
    _RuijieIgmpInterfaceEnabled_Type()
)
ruijieIgmpInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceEnabled.setStatus("current")
_RuijieIgmpInterfaceHostVersion_Type = Unsigned32
_RuijieIgmpInterfaceHostVersion_Object = MibTableColumn
ruijieIgmpInterfaceHostVersion = _RuijieIgmpInterfaceHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 1, 1, 19),
    _RuijieIgmpInterfaceHostVersion_Type()
)
ruijieIgmpInterfaceHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceHostVersion.setStatus("current")
_RuijieIgmpInterfaceStaticTable_Object = MibTable
ruijieIgmpInterfaceStaticTable = _RuijieIgmpInterfaceStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceStaticTable.setStatus("current")
_RuijieIgmpInterfaceStaticEntry_Object = MibTableRow
ruijieIgmpInterfaceStaticEntry = _RuijieIgmpInterfaceStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 2, 1)
)
ruijieIgmpInterfaceStaticEntry.setIndexNames(
    (0, "RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceStaticInterface"),
    (0, "RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceStaticGroupAddress"),
)
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceStaticEntry.setStatus("current")
_RuijieIgmpInterfaceStaticInterface_Type = InterfaceIndex
_RuijieIgmpInterfaceStaticInterface_Object = MibTableColumn
ruijieIgmpInterfaceStaticInterface = _RuijieIgmpInterfaceStaticInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 2, 1, 1),
    _RuijieIgmpInterfaceStaticInterface_Type()
)
ruijieIgmpInterfaceStaticInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceStaticInterface.setStatus("current")
_RuijieIgmpInterfaceStaticGroupAddress_Type = IpAddress
_RuijieIgmpInterfaceStaticGroupAddress_Object = MibTableColumn
ruijieIgmpInterfaceStaticGroupAddress = _RuijieIgmpInterfaceStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 2, 1, 2),
    _RuijieIgmpInterfaceStaticGroupAddress_Type()
)
ruijieIgmpInterfaceStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceStaticGroupAddress.setStatus("current")
_RuijieIgmpInterfaceStaticStatus_Type = RowStatus
_RuijieIgmpInterfaceStaticStatus_Object = MibTableColumn
ruijieIgmpInterfaceStaticStatus = _RuijieIgmpInterfaceStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 2, 1, 3),
    _RuijieIgmpInterfaceStaticStatus_Type()
)
ruijieIgmpInterfaceStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceStaticStatus.setStatus("current")
_RuijieIgmpTraps_ObjectIdentity = ObjectIdentity
ruijieIgmpTraps = _RuijieIgmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 3)
)
_RuijieIgmpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieIgmpMIBConformance = _RuijieIgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2)
)
_RuijieIgmpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieIgmpMIBCompliances = _RuijieIgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2, 1)
)
_RuijieIgmpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieIgmpMIBGroups = _RuijieIgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2, 2)
)

# Managed Objects groups

ruijieIgmpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2, 2, 1)
)
ruijieIgmpInterfaceMIBGroup.setObjects(
      *(("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceQueryInterval"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceVersion"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceQuerier"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceQueryMaxResponseTime"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceQuerierUpTime"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceQuerierExpiryTime"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceVersion1QuerierTimer"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceWrongVersionQueries"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceJoins"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceProxyIfIndex"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceGroups"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceRobustness"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceLastMembQueryIntvl"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceQuerierPresentTimeout"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceLeaves"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceAccessGroupAclName"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceEnabled"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceMIBGroup.setStatus("current")

ruijieIgmpInterfaceStaticMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2, 2, 2)
)
ruijieIgmpInterfaceStaticMIBGroup.setObjects(
    ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceStaticStatus")
)
if mibBuilder.loadTexts:
    ruijieIgmpInterfaceStaticMIBGroup.setStatus("current")


# Notification objects

ruijieIgmpVersionConflicted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 1, 3, 1)
)
ruijieIgmpVersionConflicted.setObjects(
      *(("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceIfIndex"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceVersion"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    ruijieIgmpVersionConflicted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieIgmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2, 1, 1)
)
ruijieIgmpMIBCompliance.setObjects(
      *(("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceMIBGroup"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceStaticMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieIgmpMIBCompliance.setStatus(
        "current"
    )

igmpExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 26, 2, 1, 2)
)
if mibBuilder.loadTexts:
    igmpExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IGMP-MIB",
    **{"ruijieIgmpMIB": ruijieIgmpMIB,
       "ruijieIgmpMIBObjects": ruijieIgmpMIBObjects,
       "ruijieIgmpInterfaceTable": ruijieIgmpInterfaceTable,
       "ruijieIgmpInterfaceEntry": ruijieIgmpInterfaceEntry,
       "ruijieIgmpInterfaceIfIndex": ruijieIgmpInterfaceIfIndex,
       "ruijieIgmpInterfaceQueryInterval": ruijieIgmpInterfaceQueryInterval,
       "ruijieIgmpInterfaceVersion": ruijieIgmpInterfaceVersion,
       "ruijieIgmpInterfaceQuerier": ruijieIgmpInterfaceQuerier,
       "ruijieIgmpInterfaceQueryMaxResponseTime": ruijieIgmpInterfaceQueryMaxResponseTime,
       "ruijieIgmpInterfaceQuerierUpTime": ruijieIgmpInterfaceQuerierUpTime,
       "ruijieIgmpInterfaceQuerierExpiryTime": ruijieIgmpInterfaceQuerierExpiryTime,
       "ruijieIgmpInterfaceVersion1QuerierTimer": ruijieIgmpInterfaceVersion1QuerierTimer,
       "ruijieIgmpInterfaceWrongVersionQueries": ruijieIgmpInterfaceWrongVersionQueries,
       "ruijieIgmpInterfaceJoins": ruijieIgmpInterfaceJoins,
       "ruijieIgmpInterfaceProxyIfIndex": ruijieIgmpInterfaceProxyIfIndex,
       "ruijieIgmpInterfaceGroups": ruijieIgmpInterfaceGroups,
       "ruijieIgmpInterfaceRobustness": ruijieIgmpInterfaceRobustness,
       "ruijieIgmpInterfaceLastMembQueryIntvl": ruijieIgmpInterfaceLastMembQueryIntvl,
       "ruijieIgmpInterfaceQuerierPresentTimeout": ruijieIgmpInterfaceQuerierPresentTimeout,
       "ruijieIgmpInterfaceLeaves": ruijieIgmpInterfaceLeaves,
       "ruijieIgmpInterfaceAccessGroupAclName": ruijieIgmpInterfaceAccessGroupAclName,
       "ruijieIgmpInterfaceEnabled": ruijieIgmpInterfaceEnabled,
       "ruijieIgmpInterfaceHostVersion": ruijieIgmpInterfaceHostVersion,
       "ruijieIgmpInterfaceStaticTable": ruijieIgmpInterfaceStaticTable,
       "ruijieIgmpInterfaceStaticEntry": ruijieIgmpInterfaceStaticEntry,
       "ruijieIgmpInterfaceStaticInterface": ruijieIgmpInterfaceStaticInterface,
       "ruijieIgmpInterfaceStaticGroupAddress": ruijieIgmpInterfaceStaticGroupAddress,
       "ruijieIgmpInterfaceStaticStatus": ruijieIgmpInterfaceStaticStatus,
       "ruijieIgmpTraps": ruijieIgmpTraps,
       "ruijieIgmpVersionConflicted": ruijieIgmpVersionConflicted,
       "ruijieIgmpMIBConformance": ruijieIgmpMIBConformance,
       "ruijieIgmpMIBCompliances": ruijieIgmpMIBCompliances,
       "ruijieIgmpMIBCompliance": ruijieIgmpMIBCompliance,
       "igmpExternCompliance": igmpExternCompliance,
       "ruijieIgmpMIBGroups": ruijieIgmpMIBGroups,
       "ruijieIgmpInterfaceMIBGroup": ruijieIgmpInterfaceMIBGroup,
       "ruijieIgmpInterfaceStaticMIBGroup": ruijieIgmpInterfaceStaticMIBGroup}
)
