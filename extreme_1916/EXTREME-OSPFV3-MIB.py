# SNMP MIB module (EXTREME-OSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-OSPFV3-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:32 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(BigMetric,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "BigMetric",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "Status")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeOspfv3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50)
)
if mibBuilder.loadTexts:
    extremeOspfv3MIB.setRevisions(
        ("2005-12-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ExtremeOspfv3UpToRefreshIntervalTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )



class ExtremeOspfv3DeadIntRangeTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class ExtremeOspfv3RouterIdTc(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ExtremeOspfv3AreaIdTc(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ExtremeOspfv3IfInstIdTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeOspfv3Notifications_ObjectIdentity = ObjectIdentity
extremeOspfv3Notifications = _ExtremeOspfv3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0)
)
_ExtremeOspfv3Objects_ObjectIdentity = ObjectIdentity
extremeOspfv3Objects = _ExtremeOspfv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1)
)
_ExtremeOspfv3GeneralGroup_ObjectIdentity = ObjectIdentity
extremeOspfv3GeneralGroup = _ExtremeOspfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1)
)
_ExtremeOspfv3RouterId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3RouterId_Object = MibScalar
extremeOspfv3RouterId = _ExtremeOspfv3RouterId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 1),
    _ExtremeOspfv3RouterId_Type()
)
extremeOspfv3RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3RouterId.setStatus("current")
_ExtremeOspfv3AdminStat_Type = Status
_ExtremeOspfv3AdminStat_Object = MibScalar
extremeOspfv3AdminStat = _ExtremeOspfv3AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 2),
    _ExtremeOspfv3AdminStat_Type()
)
extremeOspfv3AdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3AdminStat.setStatus("current")


class _ExtremeOspfv3VersionNumber_Type(Integer32):
    """Custom type extremeOspfv3VersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("version3", 3)
    )


_ExtremeOspfv3VersionNumber_Type.__name__ = "Integer32"
_ExtremeOspfv3VersionNumber_Object = MibScalar
extremeOspfv3VersionNumber = _ExtremeOspfv3VersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 3),
    _ExtremeOspfv3VersionNumber_Type()
)
extremeOspfv3VersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VersionNumber.setStatus("current")
_ExtremeOspfv3AreaBdrRtrStatus_Type = TruthValue
_ExtremeOspfv3AreaBdrRtrStatus_Object = MibScalar
extremeOspfv3AreaBdrRtrStatus = _ExtremeOspfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 4),
    _ExtremeOspfv3AreaBdrRtrStatus_Type()
)
extremeOspfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaBdrRtrStatus.setStatus("current")
_ExtremeOspfv3ASBdrRtrStatus_Type = TruthValue
_ExtremeOspfv3ASBdrRtrStatus_Object = MibScalar
extremeOspfv3ASBdrRtrStatus = _ExtremeOspfv3ASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 5),
    _ExtremeOspfv3ASBdrRtrStatus_Type()
)
extremeOspfv3ASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3ASBdrRtrStatus.setStatus("current")
_ExtremeOspfv3AsScopeLsaCount_Type = Gauge32
_ExtremeOspfv3AsScopeLsaCount_Object = MibScalar
extremeOspfv3AsScopeLsaCount = _ExtremeOspfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 6),
    _ExtremeOspfv3AsScopeLsaCount_Type()
)
extremeOspfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsScopeLsaCount.setStatus("current")
_ExtremeOspfv3AsScopeLsaCksumSum_Type = Integer32
_ExtremeOspfv3AsScopeLsaCksumSum_Object = MibScalar
extremeOspfv3AsScopeLsaCksumSum = _ExtremeOspfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 7),
    _ExtremeOspfv3AsScopeLsaCksumSum_Type()
)
extremeOspfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsScopeLsaCksumSum.setStatus("current")
_ExtremeOspfv3OriginateNewLsas_Type = Counter32
_ExtremeOspfv3OriginateNewLsas_Object = MibScalar
extremeOspfv3OriginateNewLsas = _ExtremeOspfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 8),
    _ExtremeOspfv3OriginateNewLsas_Type()
)
extremeOspfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3OriginateNewLsas.setStatus("current")
_ExtremeOspfv3RxNewLsas_Type = Counter32
_ExtremeOspfv3RxNewLsas_Object = MibScalar
extremeOspfv3RxNewLsas = _ExtremeOspfv3RxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 9),
    _ExtremeOspfv3RxNewLsas_Type()
)
extremeOspfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3RxNewLsas.setStatus("current")
_ExtremeOspfv3ExtLsaCount_Type = Gauge32
_ExtremeOspfv3ExtLsaCount_Object = MibScalar
extremeOspfv3ExtLsaCount = _ExtremeOspfv3ExtLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 10),
    _ExtremeOspfv3ExtLsaCount_Type()
)
extremeOspfv3ExtLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3ExtLsaCount.setStatus("current")


class _ExtremeOspfv3ExtAreaLsdbLimit_Type(Integer32):
    """Custom type extremeOspfv3ExtAreaLsdbLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ExtremeOspfv3ExtAreaLsdbLimit_Type.__name__ = "Integer32"
_ExtremeOspfv3ExtAreaLsdbLimit_Object = MibScalar
extremeOspfv3ExtAreaLsdbLimit = _ExtremeOspfv3ExtAreaLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 11),
    _ExtremeOspfv3ExtAreaLsdbLimit_Type()
)
extremeOspfv3ExtAreaLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3ExtAreaLsdbLimit.setStatus("current")


class _ExtremeOspfv3MulticastExtensions_Type(Bits):
    """Custom type extremeOspfv3MulticastExtensions based on Bits"""
    namedValues = NamedValues(
        *(("intraAreaMulticast", 0),
          ("interAreaMulticast", 1),
          ("interAsMulticast", 2))
    )

_ExtremeOspfv3MulticastExtensions_Type.__name__ = "Bits"
_ExtremeOspfv3MulticastExtensions_Object = MibScalar
extremeOspfv3MulticastExtensions = _ExtremeOspfv3MulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 12),
    _ExtremeOspfv3MulticastExtensions_Type()
)
extremeOspfv3MulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3MulticastExtensions.setStatus("current")
_ExtremeOspfv3ExitOverflowInterval_Type = Unsigned32
_ExtremeOspfv3ExitOverflowInterval_Object = MibScalar
extremeOspfv3ExitOverflowInterval = _ExtremeOspfv3ExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 13),
    _ExtremeOspfv3ExitOverflowInterval_Type()
)
extremeOspfv3ExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3ExitOverflowInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3ExitOverflowInterval.setUnits("seconds")
_ExtremeOspfv3DemandExtensions_Type = TruthValue
_ExtremeOspfv3DemandExtensions_Object = MibScalar
extremeOspfv3DemandExtensions = _ExtremeOspfv3DemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 14),
    _ExtremeOspfv3DemandExtensions_Type()
)
extremeOspfv3DemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3DemandExtensions.setStatus("current")
_ExtremeOspfv3ReferenceBandwidth_Type = Unsigned32
_ExtremeOspfv3ReferenceBandwidth_Object = MibScalar
extremeOspfv3ReferenceBandwidth = _ExtremeOspfv3ReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 15),
    _ExtremeOspfv3ReferenceBandwidth_Type()
)
extremeOspfv3ReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3ReferenceBandwidth.setStatus("current")


class _ExtremeOspfv3RestartSupport_Type(Integer32):
    """Custom type extremeOspfv3RestartSupport based on Integer32"""
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
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_ExtremeOspfv3RestartSupport_Type.__name__ = "Integer32"
_ExtremeOspfv3RestartSupport_Object = MibScalar
extremeOspfv3RestartSupport = _ExtremeOspfv3RestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 16),
    _ExtremeOspfv3RestartSupport_Type()
)
extremeOspfv3RestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3RestartSupport.setStatus("current")
_ExtremeOspfv3RestartInterval_Type = ExtremeOspfv3UpToRefreshIntervalTc
_ExtremeOspfv3RestartInterval_Object = MibScalar
extremeOspfv3RestartInterval = _ExtremeOspfv3RestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 17),
    _ExtremeOspfv3RestartInterval_Type()
)
extremeOspfv3RestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3RestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3RestartInterval.setUnits("seconds")


class _ExtremeOspfv3RestartStatus_Type(Integer32):
    """Custom type extremeOspfv3RestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_ExtremeOspfv3RestartStatus_Type.__name__ = "Integer32"
_ExtremeOspfv3RestartStatus_Object = MibScalar
extremeOspfv3RestartStatus = _ExtremeOspfv3RestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 18),
    _ExtremeOspfv3RestartStatus_Type()
)
extremeOspfv3RestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3RestartStatus.setStatus("current")
_ExtremeOspfv3RestartAge_Type = ExtremeOspfv3UpToRefreshIntervalTc
_ExtremeOspfv3RestartAge_Object = MibScalar
extremeOspfv3RestartAge = _ExtremeOspfv3RestartAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 19),
    _ExtremeOspfv3RestartAge_Type()
)
extremeOspfv3RestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3RestartAge.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3RestartAge.setUnits("seconds")


class _ExtremeOspfv3RestartExitRc_Type(Integer32):
    """Custom type extremeOspfv3RestartExitRc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_ExtremeOspfv3RestartExitRc_Type.__name__ = "Integer32"
_ExtremeOspfv3RestartExitRc_Object = MibScalar
extremeOspfv3RestartExitRc = _ExtremeOspfv3RestartExitRc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 20),
    _ExtremeOspfv3RestartExitRc_Type()
)
extremeOspfv3RestartExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3RestartExitRc.setStatus("current")
_ExtremeOspfv3NotificationEnable_Type = TruthValue
_ExtremeOspfv3NotificationEnable_Object = MibScalar
extremeOspfv3NotificationEnable = _ExtremeOspfv3NotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 1, 21),
    _ExtremeOspfv3NotificationEnable_Type()
)
extremeOspfv3NotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeOspfv3NotificationEnable.setStatus("current")
_ExtremeOspfv3AreaTable_Object = MibTable
extremeOspfv3AreaTable = _ExtremeOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2)
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaTable.setStatus("current")
_ExtremeOspfv3AreaEntry_Object = MibTableRow
extremeOspfv3AreaEntry = _ExtremeOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1)
)
extremeOspfv3AreaEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaId"),
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaEntry.setStatus("current")
_ExtremeOspfv3AreaId_Type = ExtremeOspfv3AreaIdTc
_ExtremeOspfv3AreaId_Object = MibTableColumn
extremeOspfv3AreaId = _ExtremeOspfv3AreaId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 1),
    _ExtremeOspfv3AreaId_Type()
)
extremeOspfv3AreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaId.setStatus("current")


class _ExtremeOspfv3ImportAsExtern_Type(Integer32):
    """Custom type extremeOspfv3ImportAsExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_ExtremeOspfv3ImportAsExtern_Type.__name__ = "Integer32"
_ExtremeOspfv3ImportAsExtern_Object = MibTableColumn
extremeOspfv3ImportAsExtern = _ExtremeOspfv3ImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 2),
    _ExtremeOspfv3ImportAsExtern_Type()
)
extremeOspfv3ImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3ImportAsExtern.setStatus("current")
_ExtremeOspfv3AreaSpfRuns_Type = Counter32
_ExtremeOspfv3AreaSpfRuns_Object = MibTableColumn
extremeOspfv3AreaSpfRuns = _ExtremeOspfv3AreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 3),
    _ExtremeOspfv3AreaSpfRuns_Type()
)
extremeOspfv3AreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaSpfRuns.setStatus("current")
_ExtremeOspfv3AreaBdrRtrCount_Type = Gauge32
_ExtremeOspfv3AreaBdrRtrCount_Object = MibTableColumn
extremeOspfv3AreaBdrRtrCount = _ExtremeOspfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 4),
    _ExtremeOspfv3AreaBdrRtrCount_Type()
)
extremeOspfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaBdrRtrCount.setStatus("current")
_ExtremeOspfv3AreaAsBdrRtrCount_Type = Gauge32
_ExtremeOspfv3AreaAsBdrRtrCount_Object = MibTableColumn
extremeOspfv3AreaAsBdrRtrCount = _ExtremeOspfv3AreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 5),
    _ExtremeOspfv3AreaAsBdrRtrCount_Type()
)
extremeOspfv3AreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAsBdrRtrCount.setStatus("current")
_ExtremeOspfv3AreaScopeLsaCount_Type = Gauge32
_ExtremeOspfv3AreaScopeLsaCount_Object = MibTableColumn
extremeOspfv3AreaScopeLsaCount = _ExtremeOspfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 6),
    _ExtremeOspfv3AreaScopeLsaCount_Type()
)
extremeOspfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaScopeLsaCount.setStatus("current")
_ExtremeOspfv3AreaScopeLsaCksumSum_Type = Integer32
_ExtremeOspfv3AreaScopeLsaCksumSum_Object = MibTableColumn
extremeOspfv3AreaScopeLsaCksumSum = _ExtremeOspfv3AreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 7),
    _ExtremeOspfv3AreaScopeLsaCksumSum_Type()
)
extremeOspfv3AreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaScopeLsaCksumSum.setStatus("current")


class _ExtremeOspfv3AreaSummary_Type(Integer32):
    """Custom type extremeOspfv3AreaSummary based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_ExtremeOspfv3AreaSummary_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaSummary_Object = MibTableColumn
extremeOspfv3AreaSummary = _ExtremeOspfv3AreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 8),
    _ExtremeOspfv3AreaSummary_Type()
)
extremeOspfv3AreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaSummary.setStatus("current")
_ExtremeOspfv3AreaStatus_Type = RowStatus
_ExtremeOspfv3AreaStatus_Object = MibTableColumn
extremeOspfv3AreaStatus = _ExtremeOspfv3AreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 9),
    _ExtremeOspfv3AreaStatus_Type()
)
extremeOspfv3AreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaStatus.setStatus("current")
_ExtremeOspfv3StubMetric_Type = BigMetric
_ExtremeOspfv3StubMetric_Object = MibTableColumn
extremeOspfv3StubMetric = _ExtremeOspfv3StubMetric_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 10),
    _ExtremeOspfv3StubMetric_Type()
)
extremeOspfv3StubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3StubMetric.setStatus("current")


class _ExtremeOspfv3AreaNssaTranslatorRole_Type(Integer32):
    """Custom type extremeOspfv3AreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_ExtremeOspfv3AreaNssaTranslatorRole_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaNssaTranslatorRole_Object = MibTableColumn
extremeOspfv3AreaNssaTranslatorRole = _ExtremeOspfv3AreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 11),
    _ExtremeOspfv3AreaNssaTranslatorRole_Type()
)
extremeOspfv3AreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaNssaTranslatorRole.setStatus("current")


class _ExtremeOspfv3AreaNssaTranslatorState_Type(Integer32):
    """Custom type extremeOspfv3AreaNssaTranslatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("elected", 2),
          ("disabled", 3))
    )


_ExtremeOspfv3AreaNssaTranslatorState_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaNssaTranslatorState_Object = MibTableColumn
extremeOspfv3AreaNssaTranslatorState = _ExtremeOspfv3AreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 12),
    _ExtremeOspfv3AreaNssaTranslatorState_Type()
)
extremeOspfv3AreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaNssaTranslatorState.setStatus("current")


class _ExtremeOspfv3AreaNssaTranslatorStabInt_Type(Unsigned32):
    """Custom type extremeOspfv3AreaNssaTranslatorStabInt based on Unsigned32"""
    defaultValue = 40


_ExtremeOspfv3AreaNssaTranslatorStabInt_Type.__name__ = "Unsigned32"
_ExtremeOspfv3AreaNssaTranslatorStabInt_Object = MibTableColumn
extremeOspfv3AreaNssaTranslatorStabInt = _ExtremeOspfv3AreaNssaTranslatorStabInt_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 13),
    _ExtremeOspfv3AreaNssaTranslatorStabInt_Type()
)
extremeOspfv3AreaNssaTranslatorStabInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaNssaTranslatorStabInt.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3AreaNssaTranslatorStabInt.setUnits("seconds")
_ExtremeOspfv3AreaNssaTranslatorEvents_Type = Counter32
_ExtremeOspfv3AreaNssaTranslatorEvents_Object = MibTableColumn
extremeOspfv3AreaNssaTranslatorEvents = _ExtremeOspfv3AreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 14),
    _ExtremeOspfv3AreaNssaTranslatorEvents_Type()
)
extremeOspfv3AreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaNssaTranslatorEvents.setStatus("current")


class _ExtremeOspfv3AreaStubMetricType_Type(Integer32):
    """Custom type extremeOspfv3AreaStubMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extremeOspfv3Metric", 1),
          ("comparableCost", 2),
          ("nonComparable", 3))
    )


_ExtremeOspfv3AreaStubMetricType_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaStubMetricType_Object = MibTableColumn
extremeOspfv3AreaStubMetricType = _ExtremeOspfv3AreaStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 2, 1, 15),
    _ExtremeOspfv3AreaStubMetricType_Type()
)
extremeOspfv3AreaStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaStubMetricType.setStatus("current")
_ExtremeOspfv3AsLsdbTable_Object = MibTable
extremeOspfv3AsLsdbTable = _ExtremeOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3)
)
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbTable.setStatus("current")
_ExtremeOspfv3AsLsdbEntry_Object = MibTableRow
extremeOspfv3AsLsdbEntry = _ExtremeOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1)
)
extremeOspfv3AsLsdbEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbRouterId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbLsid"),
)
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbEntry.setStatus("current")


class _ExtremeOspfv3AsLsdbType_Type(Unsigned32):
    """Custom type extremeOspfv3AsLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ExtremeOspfv3AsLsdbType_Type.__name__ = "Unsigned32"
_ExtremeOspfv3AsLsdbType_Object = MibTableColumn
extremeOspfv3AsLsdbType = _ExtremeOspfv3AsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 1),
    _ExtremeOspfv3AsLsdbType_Type()
)
extremeOspfv3AsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbType.setStatus("current")
_ExtremeOspfv3AsLsdbRouterId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3AsLsdbRouterId_Object = MibTableColumn
extremeOspfv3AsLsdbRouterId = _ExtremeOspfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 2),
    _ExtremeOspfv3AsLsdbRouterId_Type()
)
extremeOspfv3AsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbRouterId.setStatus("current")
_ExtremeOspfv3AsLsdbLsid_Type = Unsigned32
_ExtremeOspfv3AsLsdbLsid_Object = MibTableColumn
extremeOspfv3AsLsdbLsid = _ExtremeOspfv3AsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 3),
    _ExtremeOspfv3AsLsdbLsid_Type()
)
extremeOspfv3AsLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbLsid.setStatus("current")
_ExtremeOspfv3AsLsdbSequence_Type = Integer32
_ExtremeOspfv3AsLsdbSequence_Object = MibTableColumn
extremeOspfv3AsLsdbSequence = _ExtremeOspfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 4),
    _ExtremeOspfv3AsLsdbSequence_Type()
)
extremeOspfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbSequence.setStatus("current")
_ExtremeOspfv3AsLsdbAge_Type = Integer32
_ExtremeOspfv3AsLsdbAge_Object = MibTableColumn
extremeOspfv3AsLsdbAge = _ExtremeOspfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 5),
    _ExtremeOspfv3AsLsdbAge_Type()
)
extremeOspfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbAge.setUnits("seconds")
_ExtremeOspfv3AsLsdbChecksum_Type = Integer32
_ExtremeOspfv3AsLsdbChecksum_Object = MibTableColumn
extremeOspfv3AsLsdbChecksum = _ExtremeOspfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 6),
    _ExtremeOspfv3AsLsdbChecksum_Type()
)
extremeOspfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbChecksum.setStatus("current")


class _ExtremeOspfv3AsLsdbAdvertisement_Type(OctetString):
    """Custom type extremeOspfv3AsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_ExtremeOspfv3AsLsdbAdvertisement_Type.__name__ = "OctetString"
_ExtremeOspfv3AsLsdbAdvertisement_Object = MibTableColumn
extremeOspfv3AsLsdbAdvertisement = _ExtremeOspfv3AsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 7),
    _ExtremeOspfv3AsLsdbAdvertisement_Type()
)
extremeOspfv3AsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbAdvertisement.setStatus("current")
_ExtremeOspfv3AsLsdbTypeKnown_Type = TruthValue
_ExtremeOspfv3AsLsdbTypeKnown_Object = MibTableColumn
extremeOspfv3AsLsdbTypeKnown = _ExtremeOspfv3AsLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 3, 1, 8),
    _ExtremeOspfv3AsLsdbTypeKnown_Type()
)
extremeOspfv3AsLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbTypeKnown.setStatus("current")
_ExtremeOspfv3AreaLsdbTable_Object = MibTable
extremeOspfv3AreaLsdbTable = _ExtremeOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4)
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbTable.setStatus("current")
_ExtremeOspfv3AreaLsdbEntry_Object = MibTableRow
extremeOspfv3AreaLsdbEntry = _ExtremeOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1)
)
extremeOspfv3AreaLsdbEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbAreaId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbRouterId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbEntry.setStatus("current")
_ExtremeOspfv3AreaLsdbAreaId_Type = ExtremeOspfv3AreaIdTc
_ExtremeOspfv3AreaLsdbAreaId_Object = MibTableColumn
extremeOspfv3AreaLsdbAreaId = _ExtremeOspfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 1),
    _ExtremeOspfv3AreaLsdbAreaId_Type()
)
extremeOspfv3AreaLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbAreaId.setStatus("current")


class _ExtremeOspfv3AreaLsdbType_Type(Unsigned32):
    """Custom type extremeOspfv3AreaLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ExtremeOspfv3AreaLsdbType_Type.__name__ = "Unsigned32"
_ExtremeOspfv3AreaLsdbType_Object = MibTableColumn
extremeOspfv3AreaLsdbType = _ExtremeOspfv3AreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 2),
    _ExtremeOspfv3AreaLsdbType_Type()
)
extremeOspfv3AreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbType.setStatus("current")
_ExtremeOspfv3AreaLsdbRouterId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3AreaLsdbRouterId_Object = MibTableColumn
extremeOspfv3AreaLsdbRouterId = _ExtremeOspfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 3),
    _ExtremeOspfv3AreaLsdbRouterId_Type()
)
extremeOspfv3AreaLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbRouterId.setStatus("current")
_ExtremeOspfv3AreaLsdbLsid_Type = Unsigned32
_ExtremeOspfv3AreaLsdbLsid_Object = MibTableColumn
extremeOspfv3AreaLsdbLsid = _ExtremeOspfv3AreaLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 4),
    _ExtremeOspfv3AreaLsdbLsid_Type()
)
extremeOspfv3AreaLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbLsid.setStatus("current")
_ExtremeOspfv3AreaLsdbSequence_Type = Integer32
_ExtremeOspfv3AreaLsdbSequence_Object = MibTableColumn
extremeOspfv3AreaLsdbSequence = _ExtremeOspfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 5),
    _ExtremeOspfv3AreaLsdbSequence_Type()
)
extremeOspfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbSequence.setStatus("current")
_ExtremeOspfv3AreaLsdbAge_Type = Integer32
_ExtremeOspfv3AreaLsdbAge_Object = MibTableColumn
extremeOspfv3AreaLsdbAge = _ExtremeOspfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 6),
    _ExtremeOspfv3AreaLsdbAge_Type()
)
extremeOspfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbAge.setUnits("seconds")
_ExtremeOspfv3AreaLsdbChecksum_Type = Integer32
_ExtremeOspfv3AreaLsdbChecksum_Object = MibTableColumn
extremeOspfv3AreaLsdbChecksum = _ExtremeOspfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 7),
    _ExtremeOspfv3AreaLsdbChecksum_Type()
)
extremeOspfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbChecksum.setStatus("current")


class _ExtremeOspfv3AreaLsdbAdvertisement_Type(OctetString):
    """Custom type extremeOspfv3AreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_ExtremeOspfv3AreaLsdbAdvertisement_Type.__name__ = "OctetString"
_ExtremeOspfv3AreaLsdbAdvertisement_Object = MibTableColumn
extremeOspfv3AreaLsdbAdvertisement = _ExtremeOspfv3AreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 8),
    _ExtremeOspfv3AreaLsdbAdvertisement_Type()
)
extremeOspfv3AreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbAdvertisement.setStatus("current")
_ExtremeOspfv3AreaLsdbTypeKnown_Type = TruthValue
_ExtremeOspfv3AreaLsdbTypeKnown_Object = MibTableColumn
extremeOspfv3AreaLsdbTypeKnown = _ExtremeOspfv3AreaLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 4, 1, 9),
    _ExtremeOspfv3AreaLsdbTypeKnown_Type()
)
extremeOspfv3AreaLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbTypeKnown.setStatus("current")
_ExtremeOspfv3LinkLsdbTable_Object = MibTable
extremeOspfv3LinkLsdbTable = _ExtremeOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5)
)
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbTable.setStatus("current")
_ExtremeOspfv3LinkLsdbEntry_Object = MibTableRow
extremeOspfv3LinkLsdbEntry = _ExtremeOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1)
)
extremeOspfv3LinkLsdbEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbIfIndex"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbIfInstId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbRouterId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbEntry.setStatus("current")
_ExtremeOspfv3LinkLsdbIfIndex_Type = InterfaceIndex
_ExtremeOspfv3LinkLsdbIfIndex_Object = MibTableColumn
extremeOspfv3LinkLsdbIfIndex = _ExtremeOspfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 1),
    _ExtremeOspfv3LinkLsdbIfIndex_Type()
)
extremeOspfv3LinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbIfIndex.setStatus("current")
_ExtremeOspfv3LinkLsdbIfInstId_Type = ExtremeOspfv3IfInstIdTc
_ExtremeOspfv3LinkLsdbIfInstId_Object = MibTableColumn
extremeOspfv3LinkLsdbIfInstId = _ExtremeOspfv3LinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 2),
    _ExtremeOspfv3LinkLsdbIfInstId_Type()
)
extremeOspfv3LinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbIfInstId.setStatus("current")


class _ExtremeOspfv3LinkLsdbType_Type(Unsigned32):
    """Custom type extremeOspfv3LinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ExtremeOspfv3LinkLsdbType_Type.__name__ = "Unsigned32"
_ExtremeOspfv3LinkLsdbType_Object = MibTableColumn
extremeOspfv3LinkLsdbType = _ExtremeOspfv3LinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 3),
    _ExtremeOspfv3LinkLsdbType_Type()
)
extremeOspfv3LinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbType.setStatus("current")
_ExtremeOspfv3LinkLsdbRouterId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3LinkLsdbRouterId_Object = MibTableColumn
extremeOspfv3LinkLsdbRouterId = _ExtremeOspfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 4),
    _ExtremeOspfv3LinkLsdbRouterId_Type()
)
extremeOspfv3LinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbRouterId.setStatus("current")
_ExtremeOspfv3LinkLsdbLsid_Type = Unsigned32
_ExtremeOspfv3LinkLsdbLsid_Object = MibTableColumn
extremeOspfv3LinkLsdbLsid = _ExtremeOspfv3LinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 5),
    _ExtremeOspfv3LinkLsdbLsid_Type()
)
extremeOspfv3LinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbLsid.setStatus("current")
_ExtremeOspfv3LinkLsdbSequence_Type = Integer32
_ExtremeOspfv3LinkLsdbSequence_Object = MibTableColumn
extremeOspfv3LinkLsdbSequence = _ExtremeOspfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 6),
    _ExtremeOspfv3LinkLsdbSequence_Type()
)
extremeOspfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbSequence.setStatus("current")
_ExtremeOspfv3LinkLsdbAge_Type = Integer32
_ExtremeOspfv3LinkLsdbAge_Object = MibTableColumn
extremeOspfv3LinkLsdbAge = _ExtremeOspfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 7),
    _ExtremeOspfv3LinkLsdbAge_Type()
)
extremeOspfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbAge.setUnits("seconds")
_ExtremeOspfv3LinkLsdbChecksum_Type = Integer32
_ExtremeOspfv3LinkLsdbChecksum_Object = MibTableColumn
extremeOspfv3LinkLsdbChecksum = _ExtremeOspfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 8),
    _ExtremeOspfv3LinkLsdbChecksum_Type()
)
extremeOspfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbChecksum.setStatus("current")


class _ExtremeOspfv3LinkLsdbAdvertisement_Type(OctetString):
    """Custom type extremeOspfv3LinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_ExtremeOspfv3LinkLsdbAdvertisement_Type.__name__ = "OctetString"
_ExtremeOspfv3LinkLsdbAdvertisement_Object = MibTableColumn
extremeOspfv3LinkLsdbAdvertisement = _ExtremeOspfv3LinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 9),
    _ExtremeOspfv3LinkLsdbAdvertisement_Type()
)
extremeOspfv3LinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbAdvertisement.setStatus("current")
_ExtremeOspfv3LinkLsdbTypeKnown_Type = TruthValue
_ExtremeOspfv3LinkLsdbTypeKnown_Object = MibTableColumn
extremeOspfv3LinkLsdbTypeKnown = _ExtremeOspfv3LinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 5, 1, 10),
    _ExtremeOspfv3LinkLsdbTypeKnown_Type()
)
extremeOspfv3LinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbTypeKnown.setStatus("current")
_ExtremeOspfv3HostTable_Object = MibTable
extremeOspfv3HostTable = _ExtremeOspfv3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6)
)
if mibBuilder.loadTexts:
    extremeOspfv3HostTable.setStatus("current")
_ExtremeOspfv3HostEntry_Object = MibTableRow
extremeOspfv3HostEntry = _ExtremeOspfv3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6, 1)
)
extremeOspfv3HostEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3HostAddressType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3HostAddress"),
)
if mibBuilder.loadTexts:
    extremeOspfv3HostEntry.setStatus("current")
_ExtremeOspfv3HostAddressType_Type = InetAddressType
_ExtremeOspfv3HostAddressType_Object = MibTableColumn
extremeOspfv3HostAddressType = _ExtremeOspfv3HostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6, 1, 1),
    _ExtremeOspfv3HostAddressType_Type()
)
extremeOspfv3HostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3HostAddressType.setStatus("current")


class _ExtremeOspfv3HostAddress_Type(InetAddress):
    """Custom type extremeOspfv3HostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ExtremeOspfv3HostAddress_Type.__name__ = "InetAddress"
_ExtremeOspfv3HostAddress_Object = MibTableColumn
extremeOspfv3HostAddress = _ExtremeOspfv3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6, 1, 2),
    _ExtremeOspfv3HostAddress_Type()
)
extremeOspfv3HostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3HostAddress.setStatus("current")
_ExtremeOspfv3HostMetric_Type = Metric
_ExtremeOspfv3HostMetric_Object = MibTableColumn
extremeOspfv3HostMetric = _ExtremeOspfv3HostMetric_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6, 1, 3),
    _ExtremeOspfv3HostMetric_Type()
)
extremeOspfv3HostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3HostMetric.setStatus("current")
_ExtremeOspfv3HostStatus_Type = RowStatus
_ExtremeOspfv3HostStatus_Object = MibTableColumn
extremeOspfv3HostStatus = _ExtremeOspfv3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6, 1, 4),
    _ExtremeOspfv3HostStatus_Type()
)
extremeOspfv3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3HostStatus.setStatus("current")
_ExtremeOspfv3HostAreaID_Type = ExtremeOspfv3AreaIdTc
_ExtremeOspfv3HostAreaID_Object = MibTableColumn
extremeOspfv3HostAreaID = _ExtremeOspfv3HostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 6, 1, 5),
    _ExtremeOspfv3HostAreaID_Type()
)
extremeOspfv3HostAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3HostAreaID.setStatus("current")
_ExtremeOspfv3IfTable_Object = MibTable
extremeOspfv3IfTable = _ExtremeOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7)
)
if mibBuilder.loadTexts:
    extremeOspfv3IfTable.setStatus("current")
_ExtremeOspfv3IfEntry_Object = MibTableRow
extremeOspfv3IfEntry = _ExtremeOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1)
)
extremeOspfv3IfEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3IfIndex"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3IfInstId"),
)
if mibBuilder.loadTexts:
    extremeOspfv3IfEntry.setStatus("current")
_ExtremeOspfv3IfIndex_Type = InterfaceIndex
_ExtremeOspfv3IfIndex_Object = MibTableColumn
extremeOspfv3IfIndex = _ExtremeOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 1),
    _ExtremeOspfv3IfIndex_Type()
)
extremeOspfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3IfIndex.setStatus("current")
_ExtremeOspfv3IfInstId_Type = ExtremeOspfv3IfInstIdTc
_ExtremeOspfv3IfInstId_Object = MibTableColumn
extremeOspfv3IfInstId = _ExtremeOspfv3IfInstId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 2),
    _ExtremeOspfv3IfInstId_Type()
)
extremeOspfv3IfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3IfInstId.setStatus("current")


class _ExtremeOspfv3IfAreaId_Type(ExtremeOspfv3AreaIdTc):
    """Custom type extremeOspfv3IfAreaId based on ExtremeOspfv3AreaIdTc"""
    defaultValue = 0


_ExtremeOspfv3IfAreaId_Type.__name__ = "ExtremeOspfv3AreaIdTc"
_ExtremeOspfv3IfAreaId_Object = MibTableColumn
extremeOspfv3IfAreaId = _ExtremeOspfv3IfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 3),
    _ExtremeOspfv3IfAreaId_Type()
)
extremeOspfv3IfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfAreaId.setStatus("current")


class _ExtremeOspfv3IfType_Type(Integer32):
    """Custom type extremeOspfv3IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5))
    )


_ExtremeOspfv3IfType_Type.__name__ = "Integer32"
_ExtremeOspfv3IfType_Object = MibTableColumn
extremeOspfv3IfType = _ExtremeOspfv3IfType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 4),
    _ExtremeOspfv3IfType_Type()
)
extremeOspfv3IfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfType.setStatus("current")


class _ExtremeOspfv3IfAdminStat_Type(Status):
    """Custom type extremeOspfv3IfAdminStat based on Status"""
    defaultValue = 1


_ExtremeOspfv3IfAdminStat_Type.__name__ = "Status"
_ExtremeOspfv3IfAdminStat_Object = MibTableColumn
extremeOspfv3IfAdminStat = _ExtremeOspfv3IfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 5),
    _ExtremeOspfv3IfAdminStat_Type()
)
extremeOspfv3IfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfAdminStat.setStatus("current")


class _ExtremeOspfv3IfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type extremeOspfv3IfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_ExtremeOspfv3IfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_ExtremeOspfv3IfRtrPriority_Object = MibTableColumn
extremeOspfv3IfRtrPriority = _ExtremeOspfv3IfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 6),
    _ExtremeOspfv3IfRtrPriority_Type()
)
extremeOspfv3IfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfRtrPriority.setStatus("current")


class _ExtremeOspfv3IfTransitDelay_Type(ExtremeOspfv3UpToRefreshIntervalTc):
    """Custom type extremeOspfv3IfTransitDelay based on ExtremeOspfv3UpToRefreshIntervalTc"""
    defaultValue = 1


_ExtremeOspfv3IfTransitDelay_Type.__name__ = "ExtremeOspfv3UpToRefreshIntervalTc"
_ExtremeOspfv3IfTransitDelay_Object = MibTableColumn
extremeOspfv3IfTransitDelay = _ExtremeOspfv3IfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 7),
    _ExtremeOspfv3IfTransitDelay_Type()
)
extremeOspfv3IfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfTransitDelay.setUnits("seconds")


class _ExtremeOspfv3IfRetransInterval_Type(ExtremeOspfv3UpToRefreshIntervalTc):
    """Custom type extremeOspfv3IfRetransInterval based on ExtremeOspfv3UpToRefreshIntervalTc"""
    defaultValue = 5


_ExtremeOspfv3IfRetransInterval_Type.__name__ = "ExtremeOspfv3UpToRefreshIntervalTc"
_ExtremeOspfv3IfRetransInterval_Object = MibTableColumn
extremeOspfv3IfRetransInterval = _ExtremeOspfv3IfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 8),
    _ExtremeOspfv3IfRetransInterval_Type()
)
extremeOspfv3IfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfRetransInterval.setUnits("seconds")


class _ExtremeOspfv3IfHelloInterval_Type(HelloRange):
    """Custom type extremeOspfv3IfHelloInterval based on HelloRange"""
    defaultValue = 10


_ExtremeOspfv3IfHelloInterval_Type.__name__ = "HelloRange"
_ExtremeOspfv3IfHelloInterval_Object = MibTableColumn
extremeOspfv3IfHelloInterval = _ExtremeOspfv3IfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 9),
    _ExtremeOspfv3IfHelloInterval_Type()
)
extremeOspfv3IfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfHelloInterval.setUnits("seconds")


class _ExtremeOspfv3IfRtrDeadInterval_Type(ExtremeOspfv3DeadIntRangeTc):
    """Custom type extremeOspfv3IfRtrDeadInterval based on ExtremeOspfv3DeadIntRangeTc"""
    defaultValue = 40


_ExtremeOspfv3IfRtrDeadInterval_Type.__name__ = "ExtremeOspfv3DeadIntRangeTc"
_ExtremeOspfv3IfRtrDeadInterval_Object = MibTableColumn
extremeOspfv3IfRtrDeadInterval = _ExtremeOspfv3IfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 10),
    _ExtremeOspfv3IfRtrDeadInterval_Type()
)
extremeOspfv3IfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfRtrDeadInterval.setUnits("seconds")


class _ExtremeOspfv3IfPollInterval_Type(Unsigned32):
    """Custom type extremeOspfv3IfPollInterval based on Unsigned32"""
    defaultValue = 120


_ExtremeOspfv3IfPollInterval_Type.__name__ = "Unsigned32"
_ExtremeOspfv3IfPollInterval_Object = MibTableColumn
extremeOspfv3IfPollInterval = _ExtremeOspfv3IfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 11),
    _ExtremeOspfv3IfPollInterval_Type()
)
extremeOspfv3IfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfPollInterval.setUnits("seconds")


class _ExtremeOspfv3IfState_Type(Integer32):
    """Custom type extremeOspfv3IfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_ExtremeOspfv3IfState_Type.__name__ = "Integer32"
_ExtremeOspfv3IfState_Object = MibTableColumn
extremeOspfv3IfState = _ExtremeOspfv3IfState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 12),
    _ExtremeOspfv3IfState_Type()
)
extremeOspfv3IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3IfState.setStatus("current")
_ExtremeOspfv3IfDesignatedRouter_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3IfDesignatedRouter_Object = MibTableColumn
extremeOspfv3IfDesignatedRouter = _ExtremeOspfv3IfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 13),
    _ExtremeOspfv3IfDesignatedRouter_Type()
)
extremeOspfv3IfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3IfDesignatedRouter.setStatus("current")
_ExtremeOspfv3IfBackupDesignatedRouter_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3IfBackupDesignatedRouter_Object = MibTableColumn
extremeOspfv3IfBackupDesignatedRouter = _ExtremeOspfv3IfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 14),
    _ExtremeOspfv3IfBackupDesignatedRouter_Type()
)
extremeOspfv3IfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3IfBackupDesignatedRouter.setStatus("current")
_ExtremeOspfv3IfEvents_Type = Counter32
_ExtremeOspfv3IfEvents_Object = MibTableColumn
extremeOspfv3IfEvents = _ExtremeOspfv3IfEvents_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 15),
    _ExtremeOspfv3IfEvents_Type()
)
extremeOspfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3IfEvents.setStatus("current")
_ExtremeOspfv3IfStatus_Type = RowStatus
_ExtremeOspfv3IfStatus_Object = MibTableColumn
extremeOspfv3IfStatus = _ExtremeOspfv3IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 16),
    _ExtremeOspfv3IfStatus_Type()
)
extremeOspfv3IfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfStatus.setStatus("current")


class _ExtremeOspfv3IfMulticastForwarding_Type(Integer32):
    """Custom type extremeOspfv3IfMulticastForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_ExtremeOspfv3IfMulticastForwarding_Type.__name__ = "Integer32"
_ExtremeOspfv3IfMulticastForwarding_Object = MibTableColumn
extremeOspfv3IfMulticastForwarding = _ExtremeOspfv3IfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 17),
    _ExtremeOspfv3IfMulticastForwarding_Type()
)
extremeOspfv3IfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfMulticastForwarding.setStatus("current")


class _ExtremeOspfv3IfDemand_Type(TruthValue):
    """Custom type extremeOspfv3IfDemand based on TruthValue"""
    defaultValue = 2


_ExtremeOspfv3IfDemand_Type.__name__ = "TruthValue"
_ExtremeOspfv3IfDemand_Object = MibTableColumn
extremeOspfv3IfDemand = _ExtremeOspfv3IfDemand_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 18),
    _ExtremeOspfv3IfDemand_Type()
)
extremeOspfv3IfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfDemand.setStatus("current")
_ExtremeOspfv3IfMetricValue_Type = Metric
_ExtremeOspfv3IfMetricValue_Object = MibTableColumn
extremeOspfv3IfMetricValue = _ExtremeOspfv3IfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 19),
    _ExtremeOspfv3IfMetricValue_Type()
)
extremeOspfv3IfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfMetricValue.setStatus("current")
_ExtremeOspfv3IfLinkScopeLsaCount_Type = Gauge32
_ExtremeOspfv3IfLinkScopeLsaCount_Object = MibTableColumn
extremeOspfv3IfLinkScopeLsaCount = _ExtremeOspfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 20),
    _ExtremeOspfv3IfLinkScopeLsaCount_Type()
)
extremeOspfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3IfLinkScopeLsaCount.setStatus("current")
_ExtremeOspfv3IfLinkLsaCksumSum_Type = Integer32
_ExtremeOspfv3IfLinkLsaCksumSum_Object = MibTableColumn
extremeOspfv3IfLinkLsaCksumSum = _ExtremeOspfv3IfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 21),
    _ExtremeOspfv3IfLinkLsaCksumSum_Type()
)
extremeOspfv3IfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3IfLinkLsaCksumSum.setStatus("current")


class _ExtremeOspfv3IfDemandNbrProbe_Type(TruthValue):
    """Custom type extremeOspfv3IfDemandNbrProbe based on TruthValue"""
    defaultValue = 2


_ExtremeOspfv3IfDemandNbrProbe_Type.__name__ = "TruthValue"
_ExtremeOspfv3IfDemandNbrProbe_Object = MibTableColumn
extremeOspfv3IfDemandNbrProbe = _ExtremeOspfv3IfDemandNbrProbe_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 22),
    _ExtremeOspfv3IfDemandNbrProbe_Type()
)
extremeOspfv3IfDemandNbrProbe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfDemandNbrProbe.setStatus("current")


class _ExtremeOspfv3IfDemandNbrProbeRetxLimit_Type(Unsigned32):
    """Custom type extremeOspfv3IfDemandNbrProbeRetxLimit based on Unsigned32"""
    defaultValue = 10


_ExtremeOspfv3IfDemandNbrProbeRetxLimit_Type.__name__ = "Unsigned32"
_ExtremeOspfv3IfDemandNbrProbeRetxLimit_Object = MibTableColumn
extremeOspfv3IfDemandNbrProbeRetxLimit = _ExtremeOspfv3IfDemandNbrProbeRetxLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 23),
    _ExtremeOspfv3IfDemandNbrProbeRetxLimit_Type()
)
extremeOspfv3IfDemandNbrProbeRetxLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfDemandNbrProbeRetxLimit.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfDemandNbrProbeRetxLimit.setUnits("seconds")


class _ExtremeOspfv3IfDemandNbrProbeInterval_Type(Unsigned32):
    """Custom type extremeOspfv3IfDemandNbrProbeInterval based on Unsigned32"""
    defaultValue = 120


_ExtremeOspfv3IfDemandNbrProbeInterval_Type.__name__ = "Unsigned32"
_ExtremeOspfv3IfDemandNbrProbeInterval_Object = MibTableColumn
extremeOspfv3IfDemandNbrProbeInterval = _ExtremeOspfv3IfDemandNbrProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 7, 1, 24),
    _ExtremeOspfv3IfDemandNbrProbeInterval_Type()
)
extremeOspfv3IfDemandNbrProbeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3IfDemandNbrProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3IfDemandNbrProbeInterval.setUnits("seconds")
_ExtremeOspfv3VirtIfTable_Object = MibTable
extremeOspfv3VirtIfTable = _ExtremeOspfv3VirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8)
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfTable.setStatus("current")
_ExtremeOspfv3VirtIfEntry_Object = MibTableRow
extremeOspfv3VirtIfEntry = _ExtremeOspfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1)
)
extremeOspfv3VirtIfEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfAreaId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfEntry.setStatus("current")
_ExtremeOspfv3VirtIfAreaId_Type = ExtremeOspfv3AreaIdTc
_ExtremeOspfv3VirtIfAreaId_Object = MibTableColumn
extremeOspfv3VirtIfAreaId = _ExtremeOspfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 1),
    _ExtremeOspfv3VirtIfAreaId_Type()
)
extremeOspfv3VirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfAreaId.setStatus("current")
_ExtremeOspfv3VirtIfNeighbor_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3VirtIfNeighbor_Object = MibTableColumn
extremeOspfv3VirtIfNeighbor = _ExtremeOspfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 2),
    _ExtremeOspfv3VirtIfNeighbor_Type()
)
extremeOspfv3VirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfNeighbor.setStatus("current")
_ExtremeOspfv3VirtIfIndex_Type = InterfaceIndex
_ExtremeOspfv3VirtIfIndex_Object = MibTableColumn
extremeOspfv3VirtIfIndex = _ExtremeOspfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 3),
    _ExtremeOspfv3VirtIfIndex_Type()
)
extremeOspfv3VirtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfIndex.setStatus("current")


class _ExtremeOspfv3VirtIfInstId_Type(ExtremeOspfv3IfInstIdTc):
    """Custom type extremeOspfv3VirtIfInstId based on ExtremeOspfv3IfInstIdTc"""
    defaultValue = 0


_ExtremeOspfv3VirtIfInstId_Type.__name__ = "ExtremeOspfv3IfInstIdTc"
_ExtremeOspfv3VirtIfInstId_Object = MibTableColumn
extremeOspfv3VirtIfInstId = _ExtremeOspfv3VirtIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 4),
    _ExtremeOspfv3VirtIfInstId_Type()
)
extremeOspfv3VirtIfInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfInstId.setStatus("current")


class _ExtremeOspfv3VirtIfTransitDelay_Type(ExtremeOspfv3UpToRefreshIntervalTc):
    """Custom type extremeOspfv3VirtIfTransitDelay based on ExtremeOspfv3UpToRefreshIntervalTc"""
    defaultValue = 1


_ExtremeOspfv3VirtIfTransitDelay_Type.__name__ = "ExtremeOspfv3UpToRefreshIntervalTc"
_ExtremeOspfv3VirtIfTransitDelay_Object = MibTableColumn
extremeOspfv3VirtIfTransitDelay = _ExtremeOspfv3VirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 5),
    _ExtremeOspfv3VirtIfTransitDelay_Type()
)
extremeOspfv3VirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfTransitDelay.setUnits("seconds")


class _ExtremeOspfv3VirtIfRetransInterval_Type(ExtremeOspfv3UpToRefreshIntervalTc):
    """Custom type extremeOspfv3VirtIfRetransInterval based on ExtremeOspfv3UpToRefreshIntervalTc"""
    defaultValue = 5


_ExtremeOspfv3VirtIfRetransInterval_Type.__name__ = "ExtremeOspfv3UpToRefreshIntervalTc"
_ExtremeOspfv3VirtIfRetransInterval_Object = MibTableColumn
extremeOspfv3VirtIfRetransInterval = _ExtremeOspfv3VirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 6),
    _ExtremeOspfv3VirtIfRetransInterval_Type()
)
extremeOspfv3VirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfRetransInterval.setUnits("seconds")


class _ExtremeOspfv3VirtIfHelloInterval_Type(HelloRange):
    """Custom type extremeOspfv3VirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_ExtremeOspfv3VirtIfHelloInterval_Type.__name__ = "HelloRange"
_ExtremeOspfv3VirtIfHelloInterval_Object = MibTableColumn
extremeOspfv3VirtIfHelloInterval = _ExtremeOspfv3VirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 7),
    _ExtremeOspfv3VirtIfHelloInterval_Type()
)
extremeOspfv3VirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfHelloInterval.setUnits("seconds")


class _ExtremeOspfv3VirtIfRtrDeadInterval_Type(ExtremeOspfv3DeadIntRangeTc):
    """Custom type extremeOspfv3VirtIfRtrDeadInterval based on ExtremeOspfv3DeadIntRangeTc"""
    defaultValue = 60


_ExtremeOspfv3VirtIfRtrDeadInterval_Type.__name__ = "ExtremeOspfv3DeadIntRangeTc"
_ExtremeOspfv3VirtIfRtrDeadInterval_Object = MibTableColumn
extremeOspfv3VirtIfRtrDeadInterval = _ExtremeOspfv3VirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 8),
    _ExtremeOspfv3VirtIfRtrDeadInterval_Type()
)
extremeOspfv3VirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfRtrDeadInterval.setUnits("seconds")


class _ExtremeOspfv3VirtIfState_Type(Integer32):
    """Custom type extremeOspfv3VirtIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_ExtremeOspfv3VirtIfState_Type.__name__ = "Integer32"
_ExtremeOspfv3VirtIfState_Object = MibTableColumn
extremeOspfv3VirtIfState = _ExtremeOspfv3VirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 9),
    _ExtremeOspfv3VirtIfState_Type()
)
extremeOspfv3VirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfState.setStatus("current")
_ExtremeOspfv3VirtIfEvents_Type = Counter32
_ExtremeOspfv3VirtIfEvents_Object = MibTableColumn
extremeOspfv3VirtIfEvents = _ExtremeOspfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 10),
    _ExtremeOspfv3VirtIfEvents_Type()
)
extremeOspfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfEvents.setStatus("current")
_ExtremeOspfv3VirtIfStatus_Type = RowStatus
_ExtremeOspfv3VirtIfStatus_Object = MibTableColumn
extremeOspfv3VirtIfStatus = _ExtremeOspfv3VirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 11),
    _ExtremeOspfv3VirtIfStatus_Type()
)
extremeOspfv3VirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfStatus.setStatus("current")
_ExtremeOspfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_ExtremeOspfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
extremeOspfv3VirtIfLinkScopeLsaCount = _ExtremeOspfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 12),
    _ExtremeOspfv3VirtIfLinkScopeLsaCount_Type()
)
extremeOspfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfLinkScopeLsaCount.setStatus("current")
_ExtremeOspfv3VirtIfLinkLsaCksumSum_Type = Integer32
_ExtremeOspfv3VirtIfLinkLsaCksumSum_Object = MibTableColumn
extremeOspfv3VirtIfLinkLsaCksumSum = _ExtremeOspfv3VirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 8, 1, 13),
    _ExtremeOspfv3VirtIfLinkLsaCksumSum_Type()
)
extremeOspfv3VirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfLinkLsaCksumSum.setStatus("current")
_ExtremeOspfv3NbrTable_Object = MibTable
extremeOspfv3NbrTable = _ExtremeOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9)
)
if mibBuilder.loadTexts:
    extremeOspfv3NbrTable.setStatus("current")
_ExtremeOspfv3NbrEntry_Object = MibTableRow
extremeOspfv3NbrEntry = _ExtremeOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1)
)
extremeOspfv3NbrEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3NbrIfIndex"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3NbrIfInstId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRtrId"),
)
if mibBuilder.loadTexts:
    extremeOspfv3NbrEntry.setStatus("current")
_ExtremeOspfv3NbrIfIndex_Type = InterfaceIndex
_ExtremeOspfv3NbrIfIndex_Object = MibTableColumn
extremeOspfv3NbrIfIndex = _ExtremeOspfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 1),
    _ExtremeOspfv3NbrIfIndex_Type()
)
extremeOspfv3NbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3NbrIfIndex.setStatus("current")
_ExtremeOspfv3NbrIfInstId_Type = ExtremeOspfv3IfInstIdTc
_ExtremeOspfv3NbrIfInstId_Object = MibTableColumn
extremeOspfv3NbrIfInstId = _ExtremeOspfv3NbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 2),
    _ExtremeOspfv3NbrIfInstId_Type()
)
extremeOspfv3NbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3NbrIfInstId.setStatus("current")
_ExtremeOspfv3NbrRtrId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3NbrRtrId_Object = MibTableColumn
extremeOspfv3NbrRtrId = _ExtremeOspfv3NbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 3),
    _ExtremeOspfv3NbrRtrId_Type()
)
extremeOspfv3NbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3NbrRtrId.setStatus("current")
_ExtremeOspfv3NbrAddressType_Type = InetAddressType
_ExtremeOspfv3NbrAddressType_Object = MibTableColumn
extremeOspfv3NbrAddressType = _ExtremeOspfv3NbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 4),
    _ExtremeOspfv3NbrAddressType_Type()
)
extremeOspfv3NbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrAddressType.setStatus("current")


class _ExtremeOspfv3NbrAddress_Type(InetAddress):
    """Custom type extremeOspfv3NbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ExtremeOspfv3NbrAddress_Type.__name__ = "InetAddress"
_ExtremeOspfv3NbrAddress_Object = MibTableColumn
extremeOspfv3NbrAddress = _ExtremeOspfv3NbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 5),
    _ExtremeOspfv3NbrAddress_Type()
)
extremeOspfv3NbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrAddress.setStatus("current")
_ExtremeOspfv3NbrOptions_Type = Integer32
_ExtremeOspfv3NbrOptions_Object = MibTableColumn
extremeOspfv3NbrOptions = _ExtremeOspfv3NbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 6),
    _ExtremeOspfv3NbrOptions_Type()
)
extremeOspfv3NbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrOptions.setStatus("current")
_ExtremeOspfv3NbrPriority_Type = DesignatedRouterPriority
_ExtremeOspfv3NbrPriority_Object = MibTableColumn
extremeOspfv3NbrPriority = _ExtremeOspfv3NbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 7),
    _ExtremeOspfv3NbrPriority_Type()
)
extremeOspfv3NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrPriority.setStatus("current")


class _ExtremeOspfv3NbrState_Type(Integer32):
    """Custom type extremeOspfv3NbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_ExtremeOspfv3NbrState_Type.__name__ = "Integer32"
_ExtremeOspfv3NbrState_Object = MibTableColumn
extremeOspfv3NbrState = _ExtremeOspfv3NbrState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 8),
    _ExtremeOspfv3NbrState_Type()
)
extremeOspfv3NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrState.setStatus("current")
_ExtremeOspfv3NbrEvents_Type = Counter32
_ExtremeOspfv3NbrEvents_Object = MibTableColumn
extremeOspfv3NbrEvents = _ExtremeOspfv3NbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 9),
    _ExtremeOspfv3NbrEvents_Type()
)
extremeOspfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrEvents.setStatus("current")
_ExtremeOspfv3NbrLsRetransQLen_Type = Gauge32
_ExtremeOspfv3NbrLsRetransQLen_Object = MibTableColumn
extremeOspfv3NbrLsRetransQLen = _ExtremeOspfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 10),
    _ExtremeOspfv3NbrLsRetransQLen_Type()
)
extremeOspfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrLsRetransQLen.setStatus("current")
_ExtremeOspfv3NbrHelloSuppressed_Type = TruthValue
_ExtremeOspfv3NbrHelloSuppressed_Object = MibTableColumn
extremeOspfv3NbrHelloSuppressed = _ExtremeOspfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 11),
    _ExtremeOspfv3NbrHelloSuppressed_Type()
)
extremeOspfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrHelloSuppressed.setStatus("current")
_ExtremeOspfv3NbrIfId_Type = InterfaceIndex
_ExtremeOspfv3NbrIfId_Object = MibTableColumn
extremeOspfv3NbrIfId = _ExtremeOspfv3NbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 12),
    _ExtremeOspfv3NbrIfId_Type()
)
extremeOspfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrIfId.setStatus("current")


class _ExtremeOspfv3NbrRestartHelperStatus_Type(Integer32):
    """Custom type extremeOspfv3NbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_ExtremeOspfv3NbrRestartHelperStatus_Type.__name__ = "Integer32"
_ExtremeOspfv3NbrRestartHelperStatus_Object = MibTableColumn
extremeOspfv3NbrRestartHelperStatus = _ExtremeOspfv3NbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 13),
    _ExtremeOspfv3NbrRestartHelperStatus_Type()
)
extremeOspfv3NbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrRestartHelperStatus.setStatus("current")
_ExtremeOspfv3NbrRestartHelperAge_Type = ExtremeOspfv3UpToRefreshIntervalTc
_ExtremeOspfv3NbrRestartHelperAge_Object = MibTableColumn
extremeOspfv3NbrRestartHelperAge = _ExtremeOspfv3NbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 14),
    _ExtremeOspfv3NbrRestartHelperAge_Type()
)
extremeOspfv3NbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3NbrRestartHelperAge.setUnits("seconds")


class _ExtremeOspfv3NbrRestartHelperExitRc_Type(Integer32):
    """Custom type extremeOspfv3NbrRestartHelperExitRc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_ExtremeOspfv3NbrRestartHelperExitRc_Type.__name__ = "Integer32"
_ExtremeOspfv3NbrRestartHelperExitRc_Object = MibTableColumn
extremeOspfv3NbrRestartHelperExitRc = _ExtremeOspfv3NbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 9, 1, 15),
    _ExtremeOspfv3NbrRestartHelperExitRc_Type()
)
extremeOspfv3NbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3NbrRestartHelperExitRc.setStatus("current")
_ExtremeOspfv3CfgNbrTable_Object = MibTable
extremeOspfv3CfgNbrTable = _ExtremeOspfv3CfgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10)
)
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrTable.setStatus("current")
_ExtremeOspfv3CfgNbrEntry_Object = MibTableRow
extremeOspfv3CfgNbrEntry = _ExtremeOspfv3CfgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1)
)
extremeOspfv3CfgNbrEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrIfIndex"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrIfInstId"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrAddressType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrAddress"),
)
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrEntry.setStatus("current")
_ExtremeOspfv3CfgNbrIfIndex_Type = InterfaceIndex
_ExtremeOspfv3CfgNbrIfIndex_Object = MibTableColumn
extremeOspfv3CfgNbrIfIndex = _ExtremeOspfv3CfgNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 1),
    _ExtremeOspfv3CfgNbrIfIndex_Type()
)
extremeOspfv3CfgNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrIfIndex.setStatus("current")
_ExtremeOspfv3CfgNbrIfInstId_Type = ExtremeOspfv3IfInstIdTc
_ExtremeOspfv3CfgNbrIfInstId_Object = MibTableColumn
extremeOspfv3CfgNbrIfInstId = _ExtremeOspfv3CfgNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 2),
    _ExtremeOspfv3CfgNbrIfInstId_Type()
)
extremeOspfv3CfgNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrIfInstId.setStatus("current")
_ExtremeOspfv3CfgNbrAddressType_Type = InetAddressType
_ExtremeOspfv3CfgNbrAddressType_Object = MibTableColumn
extremeOspfv3CfgNbrAddressType = _ExtremeOspfv3CfgNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 3),
    _ExtremeOspfv3CfgNbrAddressType_Type()
)
extremeOspfv3CfgNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrAddressType.setStatus("current")


class _ExtremeOspfv3CfgNbrAddress_Type(InetAddress):
    """Custom type extremeOspfv3CfgNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ExtremeOspfv3CfgNbrAddress_Type.__name__ = "InetAddress"
_ExtremeOspfv3CfgNbrAddress_Object = MibTableColumn
extremeOspfv3CfgNbrAddress = _ExtremeOspfv3CfgNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 4),
    _ExtremeOspfv3CfgNbrAddress_Type()
)
extremeOspfv3CfgNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrAddress.setStatus("current")


class _ExtremeOspfv3CfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type extremeOspfv3CfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_ExtremeOspfv3CfgNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_ExtremeOspfv3CfgNbrPriority_Object = MibTableColumn
extremeOspfv3CfgNbrPriority = _ExtremeOspfv3CfgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 5),
    _ExtremeOspfv3CfgNbrPriority_Type()
)
extremeOspfv3CfgNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrPriority.setStatus("current")
_ExtremeOspfv3CfgNbrRtrId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3CfgNbrRtrId_Object = MibTableColumn
extremeOspfv3CfgNbrRtrId = _ExtremeOspfv3CfgNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 6),
    _ExtremeOspfv3CfgNbrRtrId_Type()
)
extremeOspfv3CfgNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrRtrId.setStatus("current")


class _ExtremeOspfv3CfgNbrState_Type(Integer32):
    """Custom type extremeOspfv3CfgNbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_ExtremeOspfv3CfgNbrState_Type.__name__ = "Integer32"
_ExtremeOspfv3CfgNbrState_Object = MibTableColumn
extremeOspfv3CfgNbrState = _ExtremeOspfv3CfgNbrState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 7),
    _ExtremeOspfv3CfgNbrState_Type()
)
extremeOspfv3CfgNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrState.setStatus("current")


class _ExtremeOspfv3CfgNbrStorageType_Type(StorageType):
    """Custom type extremeOspfv3CfgNbrStorageType based on StorageType"""
    defaultValue = 3


_ExtremeOspfv3CfgNbrStorageType_Type.__name__ = "StorageType"
_ExtremeOspfv3CfgNbrStorageType_Object = MibTableColumn
extremeOspfv3CfgNbrStorageType = _ExtremeOspfv3CfgNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 8),
    _ExtremeOspfv3CfgNbrStorageType_Type()
)
extremeOspfv3CfgNbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrStorageType.setStatus("current")
_ExtremeOspfv3CfgNbrStatus_Type = RowStatus
_ExtremeOspfv3CfgNbrStatus_Object = MibTableColumn
extremeOspfv3CfgNbrStatus = _ExtremeOspfv3CfgNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 10, 1, 9),
    _ExtremeOspfv3CfgNbrStatus_Type()
)
extremeOspfv3CfgNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrStatus.setStatus("current")
_ExtremeOspfv3VirtNbrTable_Object = MibTable
extremeOspfv3VirtNbrTable = _ExtremeOspfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11)
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrTable.setStatus("current")
_ExtremeOspfv3VirtNbrEntry_Object = MibTableRow
extremeOspfv3VirtNbrEntry = _ExtremeOspfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1)
)
extremeOspfv3VirtNbrEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrArea"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrEntry.setStatus("current")
_ExtremeOspfv3VirtNbrArea_Type = ExtremeOspfv3AreaIdTc
_ExtremeOspfv3VirtNbrArea_Object = MibTableColumn
extremeOspfv3VirtNbrArea = _ExtremeOspfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 1),
    _ExtremeOspfv3VirtNbrArea_Type()
)
extremeOspfv3VirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrArea.setStatus("current")
_ExtremeOspfv3VirtNbrRtrId_Type = ExtremeOspfv3RouterIdTc
_ExtremeOspfv3VirtNbrRtrId_Object = MibTableColumn
extremeOspfv3VirtNbrRtrId = _ExtremeOspfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 2),
    _ExtremeOspfv3VirtNbrRtrId_Type()
)
extremeOspfv3VirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrRtrId.setStatus("current")
_ExtremeOspfv3VirtNbrIfIndex_Type = InterfaceIndex
_ExtremeOspfv3VirtNbrIfIndex_Object = MibTableColumn
extremeOspfv3VirtNbrIfIndex = _ExtremeOspfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 3),
    _ExtremeOspfv3VirtNbrIfIndex_Type()
)
extremeOspfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrIfIndex.setStatus("current")
_ExtremeOspfv3VirtNbrIfInstId_Type = ExtremeOspfv3IfInstIdTc
_ExtremeOspfv3VirtNbrIfInstId_Object = MibTableColumn
extremeOspfv3VirtNbrIfInstId = _ExtremeOspfv3VirtNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 4),
    _ExtremeOspfv3VirtNbrIfInstId_Type()
)
extremeOspfv3VirtNbrIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrIfInstId.setStatus("current")
_ExtremeOspfv3VirtNbrAddressType_Type = InetAddressType
_ExtremeOspfv3VirtNbrAddressType_Object = MibTableColumn
extremeOspfv3VirtNbrAddressType = _ExtremeOspfv3VirtNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 5),
    _ExtremeOspfv3VirtNbrAddressType_Type()
)
extremeOspfv3VirtNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrAddressType.setStatus("current")


class _ExtremeOspfv3VirtNbrAddress_Type(InetAddress):
    """Custom type extremeOspfv3VirtNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ExtremeOspfv3VirtNbrAddress_Type.__name__ = "InetAddress"
_ExtremeOspfv3VirtNbrAddress_Object = MibTableColumn
extremeOspfv3VirtNbrAddress = _ExtremeOspfv3VirtNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 6),
    _ExtremeOspfv3VirtNbrAddress_Type()
)
extremeOspfv3VirtNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrAddress.setStatus("current")
_ExtremeOspfv3VirtNbrOptions_Type = Integer32
_ExtremeOspfv3VirtNbrOptions_Object = MibTableColumn
extremeOspfv3VirtNbrOptions = _ExtremeOspfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 7),
    _ExtremeOspfv3VirtNbrOptions_Type()
)
extremeOspfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrOptions.setStatus("current")


class _ExtremeOspfv3VirtNbrState_Type(Integer32):
    """Custom type extremeOspfv3VirtNbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_ExtremeOspfv3VirtNbrState_Type.__name__ = "Integer32"
_ExtremeOspfv3VirtNbrState_Object = MibTableColumn
extremeOspfv3VirtNbrState = _ExtremeOspfv3VirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 8),
    _ExtremeOspfv3VirtNbrState_Type()
)
extremeOspfv3VirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrState.setStatus("current")
_ExtremeOspfv3VirtNbrEvents_Type = Counter32
_ExtremeOspfv3VirtNbrEvents_Object = MibTableColumn
extremeOspfv3VirtNbrEvents = _ExtremeOspfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 9),
    _ExtremeOspfv3VirtNbrEvents_Type()
)
extremeOspfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrEvents.setStatus("current")
_ExtremeOspfv3VirtNbrLsRetransQLen_Type = Gauge32
_ExtremeOspfv3VirtNbrLsRetransQLen_Object = MibTableColumn
extremeOspfv3VirtNbrLsRetransQLen = _ExtremeOspfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 10),
    _ExtremeOspfv3VirtNbrLsRetransQLen_Type()
)
extremeOspfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrLsRetransQLen.setStatus("current")
_ExtremeOspfv3VirtNbrHelloSuppressed_Type = TruthValue
_ExtremeOspfv3VirtNbrHelloSuppressed_Object = MibTableColumn
extremeOspfv3VirtNbrHelloSuppressed = _ExtremeOspfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 11),
    _ExtremeOspfv3VirtNbrHelloSuppressed_Type()
)
extremeOspfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrHelloSuppressed.setStatus("current")
_ExtremeOspfv3VirtNbrIfId_Type = InterfaceIndex
_ExtremeOspfv3VirtNbrIfId_Object = MibTableColumn
extremeOspfv3VirtNbrIfId = _ExtremeOspfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 12),
    _ExtremeOspfv3VirtNbrIfId_Type()
)
extremeOspfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrIfId.setStatus("current")


class _ExtremeOspfv3VirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type extremeOspfv3VirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_ExtremeOspfv3VirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_ExtremeOspfv3VirtNbrRestartHelperStatus_Object = MibTableColumn
extremeOspfv3VirtNbrRestartHelperStatus = _ExtremeOspfv3VirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 13),
    _ExtremeOspfv3VirtNbrRestartHelperStatus_Type()
)
extremeOspfv3VirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrRestartHelperStatus.setStatus("current")
_ExtremeOspfv3VirtNbrRestartHelperAge_Type = ExtremeOspfv3UpToRefreshIntervalTc
_ExtremeOspfv3VirtNbrRestartHelperAge_Object = MibTableColumn
extremeOspfv3VirtNbrRestartHelperAge = _ExtremeOspfv3VirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 14),
    _ExtremeOspfv3VirtNbrRestartHelperAge_Type()
)
extremeOspfv3VirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrRestartHelperAge.setUnits("seconds")


class _ExtremeOspfv3VirtNbrRestartHelperExitRc_Type(Integer32):
    """Custom type extremeOspfv3VirtNbrRestartHelperExitRc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_ExtremeOspfv3VirtNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_ExtremeOspfv3VirtNbrRestartHelperExitRc_Object = MibTableColumn
extremeOspfv3VirtNbrRestartHelperExitRc = _ExtremeOspfv3VirtNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 11, 1, 15),
    _ExtremeOspfv3VirtNbrRestartHelperExitRc_Type()
)
extremeOspfv3VirtNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrRestartHelperExitRc.setStatus("current")
_ExtremeOspfv3AreaAggregateTable_Object = MibTable
extremeOspfv3AreaAggregateTable = _ExtremeOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12)
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateTable.setStatus("current")
_ExtremeOspfv3AreaAggregateEntry_Object = MibTableRow
extremeOspfv3AreaAggregateEntry = _ExtremeOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1)
)
extremeOspfv3AreaAggregateEntry.setIndexNames(
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregateAreaID"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregateAreaLsdbType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregatePrefixType"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregatePrefix"),
    (0, "EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregatePrefixLength"),
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateEntry.setStatus("current")
_ExtremeOspfv3AreaAggregateAreaID_Type = ExtremeOspfv3AreaIdTc
_ExtremeOspfv3AreaAggregateAreaID_Object = MibTableColumn
extremeOspfv3AreaAggregateAreaID = _ExtremeOspfv3AreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 1),
    _ExtremeOspfv3AreaAggregateAreaID_Type()
)
extremeOspfv3AreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateAreaID.setStatus("current")


class _ExtremeOspfv3AreaAggregateAreaLsdbType_Type(Integer32):
    """Custom type extremeOspfv3AreaAggregateAreaLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8195,
              8199)
        )
    )
    namedValues = NamedValues(
        *(("interAreaPrefixLsa", 8195),
          ("nssaExternalLsa", 8199))
    )


_ExtremeOspfv3AreaAggregateAreaLsdbType_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaAggregateAreaLsdbType_Object = MibTableColumn
extremeOspfv3AreaAggregateAreaLsdbType = _ExtremeOspfv3AreaAggregateAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 2),
    _ExtremeOspfv3AreaAggregateAreaLsdbType_Type()
)
extremeOspfv3AreaAggregateAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateAreaLsdbType.setStatus("current")
_ExtremeOspfv3AreaAggregatePrefixType_Type = InetAddressType
_ExtremeOspfv3AreaAggregatePrefixType_Object = MibTableColumn
extremeOspfv3AreaAggregatePrefixType = _ExtremeOspfv3AreaAggregatePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 4),
    _ExtremeOspfv3AreaAggregatePrefixType_Type()
)
extremeOspfv3AreaAggregatePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregatePrefixType.setStatus("current")


class _ExtremeOspfv3AreaAggregatePrefix_Type(InetAddress):
    """Custom type extremeOspfv3AreaAggregatePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ExtremeOspfv3AreaAggregatePrefix_Type.__name__ = "InetAddress"
_ExtremeOspfv3AreaAggregatePrefix_Object = MibTableColumn
extremeOspfv3AreaAggregatePrefix = _ExtremeOspfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 5),
    _ExtremeOspfv3AreaAggregatePrefix_Type()
)
extremeOspfv3AreaAggregatePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregatePrefix.setStatus("current")


class _ExtremeOspfv3AreaAggregatePrefixLength_Type(InetAddressPrefixLength):
    """Custom type extremeOspfv3AreaAggregatePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_ExtremeOspfv3AreaAggregatePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_ExtremeOspfv3AreaAggregatePrefixLength_Object = MibTableColumn
extremeOspfv3AreaAggregatePrefixLength = _ExtremeOspfv3AreaAggregatePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 6),
    _ExtremeOspfv3AreaAggregatePrefixLength_Type()
)
extremeOspfv3AreaAggregatePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregatePrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregatePrefixLength.setUnits("bits")
_ExtremeOspfv3AreaAggregateStatus_Type = RowStatus
_ExtremeOspfv3AreaAggregateStatus_Object = MibTableColumn
extremeOspfv3AreaAggregateStatus = _ExtremeOspfv3AreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 7),
    _ExtremeOspfv3AreaAggregateStatus_Type()
)
extremeOspfv3AreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateStatus.setStatus("current")


class _ExtremeOspfv3AreaAggregateEffect_Type(Integer32):
    """Custom type extremeOspfv3AreaAggregateEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_ExtremeOspfv3AreaAggregateEffect_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaAggregateEffect_Object = MibTableColumn
extremeOspfv3AreaAggregateEffect = _ExtremeOspfv3AreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 8),
    _ExtremeOspfv3AreaAggregateEffect_Type()
)
extremeOspfv3AreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateEffect.setStatus("current")


class _ExtremeOspfv3AreaAggregateRouteTag_Type(Integer32):
    """Custom type extremeOspfv3AreaAggregateRouteTag based on Integer32"""
    defaultValue = 0


_ExtremeOspfv3AreaAggregateRouteTag_Type.__name__ = "Integer32"
_ExtremeOspfv3AreaAggregateRouteTag_Object = MibTableColumn
extremeOspfv3AreaAggregateRouteTag = _ExtremeOspfv3AreaAggregateRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 12, 1, 9),
    _ExtremeOspfv3AreaAggregateRouteTag_Type()
)
extremeOspfv3AreaAggregateRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateRouteTag.setStatus("current")
_ExtremeOspfv3NotificationEntry_ObjectIdentity = ObjectIdentity
extremeOspfv3NotificationEntry = _ExtremeOspfv3NotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 13)
)


class _ExtremeOspfv3ConfigErrorType_Type(Integer32):
    """Custom type extremeOspfv3ConfigErrorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("helloIntervalMismatch", 5),
          ("deadIntervalMismatch", 6),
          ("optionMismatch", 7),
          ("mtuMismatch", 8),
          ("duplicateRouterId", 9),
          ("noError", 10))
    )


_ExtremeOspfv3ConfigErrorType_Type.__name__ = "Integer32"
_ExtremeOspfv3ConfigErrorType_Object = MibScalar
extremeOspfv3ConfigErrorType = _ExtremeOspfv3ConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 13, 1),
    _ExtremeOspfv3ConfigErrorType_Type()
)
extremeOspfv3ConfigErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeOspfv3ConfigErrorType.setStatus("current")


class _ExtremeOspfv3PacketType_Type(Integer32):
    """Custom type extremeOspfv3PacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5),
          ("nullPacket", 6))
    )


_ExtremeOspfv3PacketType_Type.__name__ = "Integer32"
_ExtremeOspfv3PacketType_Object = MibScalar
extremeOspfv3PacketType = _ExtremeOspfv3PacketType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 13, 2),
    _ExtremeOspfv3PacketType_Type()
)
extremeOspfv3PacketType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeOspfv3PacketType.setStatus("current")
_ExtremeOspfv3PacketSrc_Type = InetAddressIPv6
_ExtremeOspfv3PacketSrc_Object = MibScalar
extremeOspfv3PacketSrc = _ExtremeOspfv3PacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 1, 13, 3),
    _ExtremeOspfv3PacketSrc_Type()
)
extremeOspfv3PacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeOspfv3PacketSrc.setStatus("current")
_ExtremeOspfv3Conformance_ObjectIdentity = ObjectIdentity
extremeOspfv3Conformance = _ExtremeOspfv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2)
)
_ExtremeOspfv3Groups_ObjectIdentity = ObjectIdentity
extremeOspfv3Groups = _ExtremeOspfv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1)
)
_ExtremeOspfv3Compliances_ObjectIdentity = ObjectIdentity
extremeOspfv3Compliances = _ExtremeOspfv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 2)
)

# Managed Objects groups

extremeOspfv3BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 1)
)
extremeOspfv3BasicGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AdminStat"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VersionNumber"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaBdrRtrStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ASBdrRtrStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsScopeLsaCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsScopeLsaCksumSum"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3OriginateNewLsas"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3RxNewLsas"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ExtLsaCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ExtAreaLsdbLimit"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3MulticastExtensions"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ExitOverflowInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3DemandExtensions"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ReferenceBandwidth"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3RestartSupport"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3RestartInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3RestartStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3RestartAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3RestartExitRc"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NotificationEnable"))
)
if mibBuilder.loadTexts:
    extremeOspfv3BasicGroup.setStatus("current")

extremeOspfv3AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 2)
)
extremeOspfv3AreaGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3ImportAsExtern"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaSpfRuns"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaBdrRtrCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAsBdrRtrCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaScopeLsaCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaScopeLsaCksumSum"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaSummary"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3StubMetric"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaNssaTranslatorRole"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaNssaTranslatorState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaNssaTranslatorStabInt"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaNssaTranslatorEvents"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaStubMetricType"))
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaGroup.setStatus("current")

extremeOspfv3AsLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 3)
)
extremeOspfv3AsLsdbGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbSequence"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbChecksum"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbAdvertisement"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    extremeOspfv3AsLsdbGroup.setStatus("current")

extremeOspfv3AreaLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 4)
)
extremeOspfv3AreaLsdbGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbSequence"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbChecksum"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbAdvertisement"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaLsdbGroup.setStatus("current")

extremeOspfv3LinkLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 5)
)
extremeOspfv3LinkLsdbGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbSequence"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbChecksum"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbAdvertisement"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    extremeOspfv3LinkLsdbGroup.setStatus("current")

extremeOspfv3HostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 6)
)
extremeOspfv3HostGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3HostMetric"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3HostStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3HostAreaID"))
)
if mibBuilder.loadTexts:
    extremeOspfv3HostGroup.setStatus("current")

extremeOspfv3IfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 7)
)
extremeOspfv3IfGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3IfAreaId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfAdminStat"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfRtrPriority"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfTransitDelay"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfRetransInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfHelloInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfRtrDeadInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfPollInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfDesignatedRouter"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfBackupDesignatedRouter"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfEvents"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfMulticastForwarding"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfDemand"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfMetricValue"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfLinkScopeLsaCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfLinkLsaCksumSum"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfDemandNbrProbe"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfDemandNbrProbeRetxLimit"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfDemandNbrProbeInterval"))
)
if mibBuilder.loadTexts:
    extremeOspfv3IfGroup.setStatus("current")

extremeOspfv3VirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 8)
)
extremeOspfv3VirtIfGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfIndex"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfInstId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfTransitDelay"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfRetransInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfHelloInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfRtrDeadInterval"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfEvents"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfLinkScopeLsaCount"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfLinkLsaCksumSum"))
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfGroup.setStatus("current")

extremeOspfv3NbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 9)
)
extremeOspfv3NbrGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrAddressType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrAddress"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrOptions"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrPriority"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrEvents"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrLsRetransQLen"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrHelloSuppressed"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrIfId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    extremeOspfv3NbrGroup.setStatus("current")

extremeOspfv3CfgNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 10)
)
extremeOspfv3CfgNbrGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrPriority"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrRtrId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrStorageType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrStatus"))
)
if mibBuilder.loadTexts:
    extremeOspfv3CfgNbrGroup.setStatus("current")

extremeOspfv3VirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 11)
)
extremeOspfv3VirtNbrGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrIfIndex"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrIfInstId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrAddressType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrAddress"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrOptions"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrEvents"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrLsRetransQLen"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrHelloSuppressed"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrIfId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrGroup.setStatus("current")

extremeOspfv3AreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 12)
)
extremeOspfv3AreaAggregateGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregateStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregateEffect"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregateRouteTag"))
)
if mibBuilder.loadTexts:
    extremeOspfv3AreaAggregateGroup.setStatus("current")

extremeOspfv3NotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 13)
)
extremeOspfv3NotificationObjectGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3ConfigErrorType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3PacketType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3PacketSrc"))
)
if mibBuilder.loadTexts:
    extremeOspfv3NotificationObjectGroup.setStatus("current")


# Notification objects

extremeOspfv3VirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 1)
)
extremeOspfv3VirtIfStateChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfState"))
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfStateChange.setStatus(
        "current"
    )

extremeOspfv3NbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 2)
)
extremeOspfv3NbrStateChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrState"))
)
if mibBuilder.loadTexts:
    extremeOspfv3NbrStateChange.setStatus(
        "current"
    )

extremeOspfv3VirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 3)
)
extremeOspfv3VirtNbrStateChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrState"))
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrStateChange.setStatus(
        "current"
    )

extremeOspfv3IfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 4)
)
extremeOspfv3IfConfigError.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3PacketSrc"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ConfigErrorType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    extremeOspfv3IfConfigError.setStatus(
        "current"
    )

extremeOspfv3VirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 5)
)
extremeOspfv3VirtIfConfigError.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfState"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3ConfigErrorType"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtIfConfigError.setStatus(
        "current"
    )

extremeOspfv3IfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 6)
)
extremeOspfv3IfStateChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfState"))
)
if mibBuilder.loadTexts:
    extremeOspfv3IfStateChange.setStatus(
        "current"
    )

extremeOspfv3NssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 7)
)
extremeOspfv3NssaTranslatorStatusChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    extremeOspfv3NssaTranslatorStatusChange.setStatus(
        "current"
    )

extremeOspfv3NbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 8)
)
extremeOspfv3NbrRestartHelperStatusChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    extremeOspfv3NbrRestartHelperStatusChange.setStatus(
        "current"
    )

extremeOspfv3VirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 0, 9)
)
extremeOspfv3VirtNbrRestartHelperStatusChange.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3RouterId"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperStatus"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperAge"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    extremeOspfv3VirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )


# Notifications groups

extremeOspfv3NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 1, 14)
)
extremeOspfv3NotificationGroup.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfStateChange"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrStateChange"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrStateChange"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfConfigError"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfConfigError"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfStateChange"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NssaTranslatorStatusChange"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrRestartHelperStatusChange"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrRestartHelperStatusChange"))
)
if mibBuilder.loadTexts:
    extremeOspfv3NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

extremeOspfv3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50, 2, 2, 1)
)
extremeOspfv3Compliance.setObjects(
      *(("EXTREME-OSPFV3-MIB", "extremeOspfv3BasicGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3IfGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtIfGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NbrGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3CfgNbrGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3VirtNbrGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaAggregateGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AsLsdbGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3AreaLsdbGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3LinkLsdbGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3HostGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NotificationObjectGroup"),
        ("EXTREME-OSPFV3-MIB", "extremeOspfv3NotificationGroup"))
)
if mibBuilder.loadTexts:
    extremeOspfv3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-OSPFV3-MIB",
    **{"ExtremeOspfv3UpToRefreshIntervalTc": ExtremeOspfv3UpToRefreshIntervalTc,
       "ExtremeOspfv3DeadIntRangeTc": ExtremeOspfv3DeadIntRangeTc,
       "ExtremeOspfv3RouterIdTc": ExtremeOspfv3RouterIdTc,
       "ExtremeOspfv3AreaIdTc": ExtremeOspfv3AreaIdTc,
       "ExtremeOspfv3IfInstIdTc": ExtremeOspfv3IfInstIdTc,
       "extremeOspfv3MIB": extremeOspfv3MIB,
       "extremeOspfv3Notifications": extremeOspfv3Notifications,
       "extremeOspfv3VirtIfStateChange": extremeOspfv3VirtIfStateChange,
       "extremeOspfv3NbrStateChange": extremeOspfv3NbrStateChange,
       "extremeOspfv3VirtNbrStateChange": extremeOspfv3VirtNbrStateChange,
       "extremeOspfv3IfConfigError": extremeOspfv3IfConfigError,
       "extremeOspfv3VirtIfConfigError": extremeOspfv3VirtIfConfigError,
       "extremeOspfv3IfStateChange": extremeOspfv3IfStateChange,
       "extremeOspfv3NssaTranslatorStatusChange": extremeOspfv3NssaTranslatorStatusChange,
       "extremeOspfv3NbrRestartHelperStatusChange": extremeOspfv3NbrRestartHelperStatusChange,
       "extremeOspfv3VirtNbrRestartHelperStatusChange": extremeOspfv3VirtNbrRestartHelperStatusChange,
       "extremeOspfv3Objects": extremeOspfv3Objects,
       "extremeOspfv3GeneralGroup": extremeOspfv3GeneralGroup,
       "extremeOspfv3RouterId": extremeOspfv3RouterId,
       "extremeOspfv3AdminStat": extremeOspfv3AdminStat,
       "extremeOspfv3VersionNumber": extremeOspfv3VersionNumber,
       "extremeOspfv3AreaBdrRtrStatus": extremeOspfv3AreaBdrRtrStatus,
       "extremeOspfv3ASBdrRtrStatus": extremeOspfv3ASBdrRtrStatus,
       "extremeOspfv3AsScopeLsaCount": extremeOspfv3AsScopeLsaCount,
       "extremeOspfv3AsScopeLsaCksumSum": extremeOspfv3AsScopeLsaCksumSum,
       "extremeOspfv3OriginateNewLsas": extremeOspfv3OriginateNewLsas,
       "extremeOspfv3RxNewLsas": extremeOspfv3RxNewLsas,
       "extremeOspfv3ExtLsaCount": extremeOspfv3ExtLsaCount,
       "extremeOspfv3ExtAreaLsdbLimit": extremeOspfv3ExtAreaLsdbLimit,
       "extremeOspfv3MulticastExtensions": extremeOspfv3MulticastExtensions,
       "extremeOspfv3ExitOverflowInterval": extremeOspfv3ExitOverflowInterval,
       "extremeOspfv3DemandExtensions": extremeOspfv3DemandExtensions,
       "extremeOspfv3ReferenceBandwidth": extremeOspfv3ReferenceBandwidth,
       "extremeOspfv3RestartSupport": extremeOspfv3RestartSupport,
       "extremeOspfv3RestartInterval": extremeOspfv3RestartInterval,
       "extremeOspfv3RestartStatus": extremeOspfv3RestartStatus,
       "extremeOspfv3RestartAge": extremeOspfv3RestartAge,
       "extremeOspfv3RestartExitRc": extremeOspfv3RestartExitRc,
       "extremeOspfv3NotificationEnable": extremeOspfv3NotificationEnable,
       "extremeOspfv3AreaTable": extremeOspfv3AreaTable,
       "extremeOspfv3AreaEntry": extremeOspfv3AreaEntry,
       "extremeOspfv3AreaId": extremeOspfv3AreaId,
       "extremeOspfv3ImportAsExtern": extremeOspfv3ImportAsExtern,
       "extremeOspfv3AreaSpfRuns": extremeOspfv3AreaSpfRuns,
       "extremeOspfv3AreaBdrRtrCount": extremeOspfv3AreaBdrRtrCount,
       "extremeOspfv3AreaAsBdrRtrCount": extremeOspfv3AreaAsBdrRtrCount,
       "extremeOspfv3AreaScopeLsaCount": extremeOspfv3AreaScopeLsaCount,
       "extremeOspfv3AreaScopeLsaCksumSum": extremeOspfv3AreaScopeLsaCksumSum,
       "extremeOspfv3AreaSummary": extremeOspfv3AreaSummary,
       "extremeOspfv3AreaStatus": extremeOspfv3AreaStatus,
       "extremeOspfv3StubMetric": extremeOspfv3StubMetric,
       "extremeOspfv3AreaNssaTranslatorRole": extremeOspfv3AreaNssaTranslatorRole,
       "extremeOspfv3AreaNssaTranslatorState": extremeOspfv3AreaNssaTranslatorState,
       "extremeOspfv3AreaNssaTranslatorStabInt": extremeOspfv3AreaNssaTranslatorStabInt,
       "extremeOspfv3AreaNssaTranslatorEvents": extremeOspfv3AreaNssaTranslatorEvents,
       "extremeOspfv3AreaStubMetricType": extremeOspfv3AreaStubMetricType,
       "extremeOspfv3AsLsdbTable": extremeOspfv3AsLsdbTable,
       "extremeOspfv3AsLsdbEntry": extremeOspfv3AsLsdbEntry,
       "extremeOspfv3AsLsdbType": extremeOspfv3AsLsdbType,
       "extremeOspfv3AsLsdbRouterId": extremeOspfv3AsLsdbRouterId,
       "extremeOspfv3AsLsdbLsid": extremeOspfv3AsLsdbLsid,
       "extremeOspfv3AsLsdbSequence": extremeOspfv3AsLsdbSequence,
       "extremeOspfv3AsLsdbAge": extremeOspfv3AsLsdbAge,
       "extremeOspfv3AsLsdbChecksum": extremeOspfv3AsLsdbChecksum,
       "extremeOspfv3AsLsdbAdvertisement": extremeOspfv3AsLsdbAdvertisement,
       "extremeOspfv3AsLsdbTypeKnown": extremeOspfv3AsLsdbTypeKnown,
       "extremeOspfv3AreaLsdbTable": extremeOspfv3AreaLsdbTable,
       "extremeOspfv3AreaLsdbEntry": extremeOspfv3AreaLsdbEntry,
       "extremeOspfv3AreaLsdbAreaId": extremeOspfv3AreaLsdbAreaId,
       "extremeOspfv3AreaLsdbType": extremeOspfv3AreaLsdbType,
       "extremeOspfv3AreaLsdbRouterId": extremeOspfv3AreaLsdbRouterId,
       "extremeOspfv3AreaLsdbLsid": extremeOspfv3AreaLsdbLsid,
       "extremeOspfv3AreaLsdbSequence": extremeOspfv3AreaLsdbSequence,
       "extremeOspfv3AreaLsdbAge": extremeOspfv3AreaLsdbAge,
       "extremeOspfv3AreaLsdbChecksum": extremeOspfv3AreaLsdbChecksum,
       "extremeOspfv3AreaLsdbAdvertisement": extremeOspfv3AreaLsdbAdvertisement,
       "extremeOspfv3AreaLsdbTypeKnown": extremeOspfv3AreaLsdbTypeKnown,
       "extremeOspfv3LinkLsdbTable": extremeOspfv3LinkLsdbTable,
       "extremeOspfv3LinkLsdbEntry": extremeOspfv3LinkLsdbEntry,
       "extremeOspfv3LinkLsdbIfIndex": extremeOspfv3LinkLsdbIfIndex,
       "extremeOspfv3LinkLsdbIfInstId": extremeOspfv3LinkLsdbIfInstId,
       "extremeOspfv3LinkLsdbType": extremeOspfv3LinkLsdbType,
       "extremeOspfv3LinkLsdbRouterId": extremeOspfv3LinkLsdbRouterId,
       "extremeOspfv3LinkLsdbLsid": extremeOspfv3LinkLsdbLsid,
       "extremeOspfv3LinkLsdbSequence": extremeOspfv3LinkLsdbSequence,
       "extremeOspfv3LinkLsdbAge": extremeOspfv3LinkLsdbAge,
       "extremeOspfv3LinkLsdbChecksum": extremeOspfv3LinkLsdbChecksum,
       "extremeOspfv3LinkLsdbAdvertisement": extremeOspfv3LinkLsdbAdvertisement,
       "extremeOspfv3LinkLsdbTypeKnown": extremeOspfv3LinkLsdbTypeKnown,
       "extremeOspfv3HostTable": extremeOspfv3HostTable,
       "extremeOspfv3HostEntry": extremeOspfv3HostEntry,
       "extremeOspfv3HostAddressType": extremeOspfv3HostAddressType,
       "extremeOspfv3HostAddress": extremeOspfv3HostAddress,
       "extremeOspfv3HostMetric": extremeOspfv3HostMetric,
       "extremeOspfv3HostStatus": extremeOspfv3HostStatus,
       "extremeOspfv3HostAreaID": extremeOspfv3HostAreaID,
       "extremeOspfv3IfTable": extremeOspfv3IfTable,
       "extremeOspfv3IfEntry": extremeOspfv3IfEntry,
       "extremeOspfv3IfIndex": extremeOspfv3IfIndex,
       "extremeOspfv3IfInstId": extremeOspfv3IfInstId,
       "extremeOspfv3IfAreaId": extremeOspfv3IfAreaId,
       "extremeOspfv3IfType": extremeOspfv3IfType,
       "extremeOspfv3IfAdminStat": extremeOspfv3IfAdminStat,
       "extremeOspfv3IfRtrPriority": extremeOspfv3IfRtrPriority,
       "extremeOspfv3IfTransitDelay": extremeOspfv3IfTransitDelay,
       "extremeOspfv3IfRetransInterval": extremeOspfv3IfRetransInterval,
       "extremeOspfv3IfHelloInterval": extremeOspfv3IfHelloInterval,
       "extremeOspfv3IfRtrDeadInterval": extremeOspfv3IfRtrDeadInterval,
       "extremeOspfv3IfPollInterval": extremeOspfv3IfPollInterval,
       "extremeOspfv3IfState": extremeOspfv3IfState,
       "extremeOspfv3IfDesignatedRouter": extremeOspfv3IfDesignatedRouter,
       "extremeOspfv3IfBackupDesignatedRouter": extremeOspfv3IfBackupDesignatedRouter,
       "extremeOspfv3IfEvents": extremeOspfv3IfEvents,
       "extremeOspfv3IfStatus": extremeOspfv3IfStatus,
       "extremeOspfv3IfMulticastForwarding": extremeOspfv3IfMulticastForwarding,
       "extremeOspfv3IfDemand": extremeOspfv3IfDemand,
       "extremeOspfv3IfMetricValue": extremeOspfv3IfMetricValue,
       "extremeOspfv3IfLinkScopeLsaCount": extremeOspfv3IfLinkScopeLsaCount,
       "extremeOspfv3IfLinkLsaCksumSum": extremeOspfv3IfLinkLsaCksumSum,
       "extremeOspfv3IfDemandNbrProbe": extremeOspfv3IfDemandNbrProbe,
       "extremeOspfv3IfDemandNbrProbeRetxLimit": extremeOspfv3IfDemandNbrProbeRetxLimit,
       "extremeOspfv3IfDemandNbrProbeInterval": extremeOspfv3IfDemandNbrProbeInterval,
       "extremeOspfv3VirtIfTable": extremeOspfv3VirtIfTable,
       "extremeOspfv3VirtIfEntry": extremeOspfv3VirtIfEntry,
       "extremeOspfv3VirtIfAreaId": extremeOspfv3VirtIfAreaId,
       "extremeOspfv3VirtIfNeighbor": extremeOspfv3VirtIfNeighbor,
       "extremeOspfv3VirtIfIndex": extremeOspfv3VirtIfIndex,
       "extremeOspfv3VirtIfInstId": extremeOspfv3VirtIfInstId,
       "extremeOspfv3VirtIfTransitDelay": extremeOspfv3VirtIfTransitDelay,
       "extremeOspfv3VirtIfRetransInterval": extremeOspfv3VirtIfRetransInterval,
       "extremeOspfv3VirtIfHelloInterval": extremeOspfv3VirtIfHelloInterval,
       "extremeOspfv3VirtIfRtrDeadInterval": extremeOspfv3VirtIfRtrDeadInterval,
       "extremeOspfv3VirtIfState": extremeOspfv3VirtIfState,
       "extremeOspfv3VirtIfEvents": extremeOspfv3VirtIfEvents,
       "extremeOspfv3VirtIfStatus": extremeOspfv3VirtIfStatus,
       "extremeOspfv3VirtIfLinkScopeLsaCount": extremeOspfv3VirtIfLinkScopeLsaCount,
       "extremeOspfv3VirtIfLinkLsaCksumSum": extremeOspfv3VirtIfLinkLsaCksumSum,
       "extremeOspfv3NbrTable": extremeOspfv3NbrTable,
       "extremeOspfv3NbrEntry": extremeOspfv3NbrEntry,
       "extremeOspfv3NbrIfIndex": extremeOspfv3NbrIfIndex,
       "extremeOspfv3NbrIfInstId": extremeOspfv3NbrIfInstId,
       "extremeOspfv3NbrRtrId": extremeOspfv3NbrRtrId,
       "extremeOspfv3NbrAddressType": extremeOspfv3NbrAddressType,
       "extremeOspfv3NbrAddress": extremeOspfv3NbrAddress,
       "extremeOspfv3NbrOptions": extremeOspfv3NbrOptions,
       "extremeOspfv3NbrPriority": extremeOspfv3NbrPriority,
       "extremeOspfv3NbrState": extremeOspfv3NbrState,
       "extremeOspfv3NbrEvents": extremeOspfv3NbrEvents,
       "extremeOspfv3NbrLsRetransQLen": extremeOspfv3NbrLsRetransQLen,
       "extremeOspfv3NbrHelloSuppressed": extremeOspfv3NbrHelloSuppressed,
       "extremeOspfv3NbrIfId": extremeOspfv3NbrIfId,
       "extremeOspfv3NbrRestartHelperStatus": extremeOspfv3NbrRestartHelperStatus,
       "extremeOspfv3NbrRestartHelperAge": extremeOspfv3NbrRestartHelperAge,
       "extremeOspfv3NbrRestartHelperExitRc": extremeOspfv3NbrRestartHelperExitRc,
       "extremeOspfv3CfgNbrTable": extremeOspfv3CfgNbrTable,
       "extremeOspfv3CfgNbrEntry": extremeOspfv3CfgNbrEntry,
       "extremeOspfv3CfgNbrIfIndex": extremeOspfv3CfgNbrIfIndex,
       "extremeOspfv3CfgNbrIfInstId": extremeOspfv3CfgNbrIfInstId,
       "extremeOspfv3CfgNbrAddressType": extremeOspfv3CfgNbrAddressType,
       "extremeOspfv3CfgNbrAddress": extremeOspfv3CfgNbrAddress,
       "extremeOspfv3CfgNbrPriority": extremeOspfv3CfgNbrPriority,
       "extremeOspfv3CfgNbrRtrId": extremeOspfv3CfgNbrRtrId,
       "extremeOspfv3CfgNbrState": extremeOspfv3CfgNbrState,
       "extremeOspfv3CfgNbrStorageType": extremeOspfv3CfgNbrStorageType,
       "extremeOspfv3CfgNbrStatus": extremeOspfv3CfgNbrStatus,
       "extremeOspfv3VirtNbrTable": extremeOspfv3VirtNbrTable,
       "extremeOspfv3VirtNbrEntry": extremeOspfv3VirtNbrEntry,
       "extremeOspfv3VirtNbrArea": extremeOspfv3VirtNbrArea,
       "extremeOspfv3VirtNbrRtrId": extremeOspfv3VirtNbrRtrId,
       "extremeOspfv3VirtNbrIfIndex": extremeOspfv3VirtNbrIfIndex,
       "extremeOspfv3VirtNbrIfInstId": extremeOspfv3VirtNbrIfInstId,
       "extremeOspfv3VirtNbrAddressType": extremeOspfv3VirtNbrAddressType,
       "extremeOspfv3VirtNbrAddress": extremeOspfv3VirtNbrAddress,
       "extremeOspfv3VirtNbrOptions": extremeOspfv3VirtNbrOptions,
       "extremeOspfv3VirtNbrState": extremeOspfv3VirtNbrState,
       "extremeOspfv3VirtNbrEvents": extremeOspfv3VirtNbrEvents,
       "extremeOspfv3VirtNbrLsRetransQLen": extremeOspfv3VirtNbrLsRetransQLen,
       "extremeOspfv3VirtNbrHelloSuppressed": extremeOspfv3VirtNbrHelloSuppressed,
       "extremeOspfv3VirtNbrIfId": extremeOspfv3VirtNbrIfId,
       "extremeOspfv3VirtNbrRestartHelperStatus": extremeOspfv3VirtNbrRestartHelperStatus,
       "extremeOspfv3VirtNbrRestartHelperAge": extremeOspfv3VirtNbrRestartHelperAge,
       "extremeOspfv3VirtNbrRestartHelperExitRc": extremeOspfv3VirtNbrRestartHelperExitRc,
       "extremeOspfv3AreaAggregateTable": extremeOspfv3AreaAggregateTable,
       "extremeOspfv3AreaAggregateEntry": extremeOspfv3AreaAggregateEntry,
       "extremeOspfv3AreaAggregateAreaID": extremeOspfv3AreaAggregateAreaID,
       "extremeOspfv3AreaAggregateAreaLsdbType": extremeOspfv3AreaAggregateAreaLsdbType,
       "extremeOspfv3AreaAggregatePrefixType": extremeOspfv3AreaAggregatePrefixType,
       "extremeOspfv3AreaAggregatePrefix": extremeOspfv3AreaAggregatePrefix,
       "extremeOspfv3AreaAggregatePrefixLength": extremeOspfv3AreaAggregatePrefixLength,
       "extremeOspfv3AreaAggregateStatus": extremeOspfv3AreaAggregateStatus,
       "extremeOspfv3AreaAggregateEffect": extremeOspfv3AreaAggregateEffect,
       "extremeOspfv3AreaAggregateRouteTag": extremeOspfv3AreaAggregateRouteTag,
       "extremeOspfv3NotificationEntry": extremeOspfv3NotificationEntry,
       "extremeOspfv3ConfigErrorType": extremeOspfv3ConfigErrorType,
       "extremeOspfv3PacketType": extremeOspfv3PacketType,
       "extremeOspfv3PacketSrc": extremeOspfv3PacketSrc,
       "extremeOspfv3Conformance": extremeOspfv3Conformance,
       "extremeOspfv3Groups": extremeOspfv3Groups,
       "extremeOspfv3BasicGroup": extremeOspfv3BasicGroup,
       "extremeOspfv3AreaGroup": extremeOspfv3AreaGroup,
       "extremeOspfv3AsLsdbGroup": extremeOspfv3AsLsdbGroup,
       "extremeOspfv3AreaLsdbGroup": extremeOspfv3AreaLsdbGroup,
       "extremeOspfv3LinkLsdbGroup": extremeOspfv3LinkLsdbGroup,
       "extremeOspfv3HostGroup": extremeOspfv3HostGroup,
       "extremeOspfv3IfGroup": extremeOspfv3IfGroup,
       "extremeOspfv3VirtIfGroup": extremeOspfv3VirtIfGroup,
       "extremeOspfv3NbrGroup": extremeOspfv3NbrGroup,
       "extremeOspfv3CfgNbrGroup": extremeOspfv3CfgNbrGroup,
       "extremeOspfv3VirtNbrGroup": extremeOspfv3VirtNbrGroup,
       "extremeOspfv3AreaAggregateGroup": extremeOspfv3AreaAggregateGroup,
       "extremeOspfv3NotificationObjectGroup": extremeOspfv3NotificationObjectGroup,
       "extremeOspfv3NotificationGroup": extremeOspfv3NotificationGroup,
       "extremeOspfv3Compliances": extremeOspfv3Compliances,
       "extremeOspfv3Compliance": extremeOspfv3Compliance}
)
