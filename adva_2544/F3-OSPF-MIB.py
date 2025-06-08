# SNMP MIB module (F3-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-OSPF-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(cmIpInterfaceEntry,
 ipManagementTunnelEntry) = mibBuilder.importSymbols(
    "CM-IP-MIB",
    "cmIpInterfaceEntry",
    "ipManagementTunnelEntry")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 OspfAuthenticationType,
 RouterID,
 ospfNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "OspfAuthenticationType",
    "RouterID",
    "ospfNbrEntry")

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

f3OspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35)
)
if mibBuilder.loadTexts:
    f3OspfMIB.setRevisions(
        ("2014-10-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OspfMetricType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e2", 2))
    )



class OspfRedistributionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip", 2))
    )



class OspfState(TextualConvention, Integer32):
    status = "current"
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
          ("disabled", 2),
          ("passive", 3))
    )



class OspfAreaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("stub", 2))
    )



class OspfRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bdr", 1),
          ("dr", 2),
          ("drother", 3))
    )



# MIB Managed Objects in the order of their OIDs

_F3OspfConfigObjects_ObjectIdentity = ObjectIdentity
f3OspfConfigObjects = _F3OspfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1)
)
_F3OspfRouterTable_Object = MibTable
f3OspfRouterTable = _F3OspfRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1)
)
if mibBuilder.loadTexts:
    f3OspfRouterTable.setStatus("current")
_F3OspfRouterEntry_Object = MibTableRow
f3OspfRouterEntry = _F3OspfRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1)
)
f3OspfRouterEntry.setIndexNames(
    (0, "F3-OSPF-MIB", "f3OspfRouterIndex"),
)
if mibBuilder.loadTexts:
    f3OspfRouterEntry.setStatus("current")
_F3OspfRouterIndex_Type = RouterID
_F3OspfRouterIndex_Object = MibTableColumn
f3OspfRouterIndex = _F3OspfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 1),
    _F3OspfRouterIndex_Type()
)
f3OspfRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3OspfRouterIndex.setStatus("current")
_F3OspfRouterMetricType_Type = OspfMetricType
_F3OspfRouterMetricType_Object = MibTableColumn
f3OspfRouterMetricType = _F3OspfRouterMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 2),
    _F3OspfRouterMetricType_Type()
)
f3OspfRouterMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfRouterMetricType.setStatus("current")


class _F3OspfRouterMetric_Type(Integer32):
    """Custom type f3OspfRouterMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_F3OspfRouterMetric_Type.__name__ = "Integer32"
_F3OspfRouterMetric_Object = MibTableColumn
f3OspfRouterMetric = _F3OspfRouterMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 3),
    _F3OspfRouterMetric_Type()
)
f3OspfRouterMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfRouterMetric.setStatus("current")
_F3OspfRouterRedistributionType_Type = OspfRedistributionType
_F3OspfRouterRedistributionType_Object = MibTableColumn
f3OspfRouterRedistributionType = _F3OspfRouterRedistributionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 4),
    _F3OspfRouterRedistributionType_Type()
)
f3OspfRouterRedistributionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfRouterRedistributionType.setStatus("current")
_F3OspfRouterNumAttachedAreas_Type = Unsigned32
_F3OspfRouterNumAttachedAreas_Object = MibTableColumn
f3OspfRouterNumAttachedAreas = _F3OspfRouterNumAttachedAreas_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 5),
    _F3OspfRouterNumAttachedAreas_Type()
)
f3OspfRouterNumAttachedAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OspfRouterNumAttachedAreas.setStatus("current")
_F3OspfRouterAreaBdrRtrStatus_Type = TruthValue
_F3OspfRouterAreaBdrRtrStatus_Object = MibTableColumn
f3OspfRouterAreaBdrRtrStatus = _F3OspfRouterAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 6),
    _F3OspfRouterAreaBdrRtrStatus_Type()
)
f3OspfRouterAreaBdrRtrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfRouterAreaBdrRtrStatus.setStatus("current")
_F3OspfRouterStorageType_Type = StorageType
_F3OspfRouterStorageType_Object = MibTableColumn
f3OspfRouterStorageType = _F3OspfRouterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 7),
    _F3OspfRouterStorageType_Type()
)
f3OspfRouterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfRouterStorageType.setStatus("current")
_F3OspfRouterRowStatus_Type = RowStatus
_F3OspfRouterRowStatus_Object = MibTableColumn
f3OspfRouterRowStatus = _F3OspfRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 1, 1, 8),
    _F3OspfRouterRowStatus_Type()
)
f3OspfRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfRouterRowStatus.setStatus("current")
_F3OspfAreaTable_Object = MibTable
f3OspfAreaTable = _F3OspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2)
)
if mibBuilder.loadTexts:
    f3OspfAreaTable.setStatus("current")
_F3OspfAreaEntry_Object = MibTableRow
f3OspfAreaEntry = _F3OspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1)
)
f3OspfAreaEntry.setIndexNames(
    (0, "F3-OSPF-MIB", "f3OspfAreaId"),
)
if mibBuilder.loadTexts:
    f3OspfAreaEntry.setStatus("current")
_F3OspfAreaId_Type = AreaID
_F3OspfAreaId_Object = MibTableColumn
f3OspfAreaId = _F3OspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 1),
    _F3OspfAreaId_Type()
)
f3OspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3OspfAreaId.setStatus("current")
_F3OspfAreaType_Type = OspfAreaType
_F3OspfAreaType_Object = MibTableColumn
f3OspfAreaType = _F3OspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 2),
    _F3OspfAreaType_Type()
)
f3OspfAreaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfAreaType.setStatus("current")
_F3OspfAreaAuthType_Type = OspfAuthenticationType
_F3OspfAreaAuthType_Object = MibTableColumn
f3OspfAreaAuthType = _F3OspfAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 3),
    _F3OspfAreaAuthType_Type()
)
f3OspfAreaAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfAreaAuthType.setStatus("current")


class _F3OspfAreaDefaultCost_Type(Unsigned32):
    """Custom type f3OspfAreaDefaultCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_F3OspfAreaDefaultCost_Type.__name__ = "Unsigned32"
_F3OspfAreaDefaultCost_Object = MibTableColumn
f3OspfAreaDefaultCost = _F3OspfAreaDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 4),
    _F3OspfAreaDefaultCost_Type()
)
f3OspfAreaDefaultCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfAreaDefaultCost.setStatus("current")
_F3OspfAreaSpfRuns_Type = Counter32
_F3OspfAreaSpfRuns_Object = MibTableColumn
f3OspfAreaSpfRuns = _F3OspfAreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 5),
    _F3OspfAreaSpfRuns_Type()
)
f3OspfAreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OspfAreaSpfRuns.setStatus("current")
_F3OspfAreaLsaCount_Type = Gauge32
_F3OspfAreaLsaCount_Object = MibTableColumn
f3OspfAreaLsaCount = _F3OspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 6),
    _F3OspfAreaLsaCount_Type()
)
f3OspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OspfAreaLsaCount.setStatus("current")
_F3OspfAreaStorageType_Type = StorageType
_F3OspfAreaStorageType_Object = MibTableColumn
f3OspfAreaStorageType = _F3OspfAreaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 7),
    _F3OspfAreaStorageType_Type()
)
f3OspfAreaStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfAreaStorageType.setStatus("current")
_F3OspfAreaRowStatus_Type = RowStatus
_F3OspfAreaRowStatus_Object = MibTableColumn
f3OspfAreaRowStatus = _F3OspfAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 2, 1, 8),
    _F3OspfAreaRowStatus_Type()
)
f3OspfAreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3OspfAreaRowStatus.setStatus("current")
_F3OspfIpInterfaceExtTable_Object = MibTable
f3OspfIpInterfaceExtTable = _F3OspfIpInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3)
)
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtTable.setStatus("current")
_F3OspfIpInterfaceExtEntry_Object = MibTableRow
f3OspfIpInterfaceExtEntry = _F3OspfIpInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtEntry.setStatus("current")


class _F3OspfIpInterfaceExtStatus_Type(OspfState):
    """Custom type f3OspfIpInterfaceExtStatus based on OspfState"""
    defaultValue = 1


_F3OspfIpInterfaceExtStatus_Type.__name__ = "OspfState"
_F3OspfIpInterfaceExtStatus_Object = MibTableColumn
f3OspfIpInterfaceExtStatus = _F3OspfIpInterfaceExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 1),
    _F3OspfIpInterfaceExtStatus_Type()
)
f3OspfIpInterfaceExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtStatus.setStatus("current")


class _F3OspfIpInterfaceExtAreaId_Type(AreaID):
    """Custom type f3OspfIpInterfaceExtAreaId based on AreaID"""
    defaultHexValue = "00000000"


_F3OspfIpInterfaceExtAreaId_Type.__name__ = "AreaID"
_F3OspfIpInterfaceExtAreaId_Object = MibTableColumn
f3OspfIpInterfaceExtAreaId = _F3OspfIpInterfaceExtAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 2),
    _F3OspfIpInterfaceExtAreaId_Type()
)
f3OspfIpInterfaceExtAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtAreaId.setStatus("current")


class _F3OspfIpInterfaceExtIfType_Type(Integer32):
    """Custom type f3OspfIpInterfaceExtIfType based on Integer32"""
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


_F3OspfIpInterfaceExtIfType_Type.__name__ = "Integer32"
_F3OspfIpInterfaceExtIfType_Object = MibTableColumn
f3OspfIpInterfaceExtIfType = _F3OspfIpInterfaceExtIfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 3),
    _F3OspfIpInterfaceExtIfType_Type()
)
f3OspfIpInterfaceExtIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtIfType.setStatus("current")


class _F3OspfIpInterfaceExtHelloInterval_Type(HelloRange):
    """Custom type f3OspfIpInterfaceExtHelloInterval based on HelloRange"""
    defaultValue = 10


_F3OspfIpInterfaceExtHelloInterval_Type.__name__ = "HelloRange"
_F3OspfIpInterfaceExtHelloInterval_Object = MibTableColumn
f3OspfIpInterfaceExtHelloInterval = _F3OspfIpInterfaceExtHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 4),
    _F3OspfIpInterfaceExtHelloInterval_Type()
)
f3OspfIpInterfaceExtHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtHelloInterval.setUnits("seconds")


class _F3OspfIpInterfaceExtRtrDeadInterval_Type(Integer32):
    """Custom type f3OspfIpInterfaceExtRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3OspfIpInterfaceExtRtrDeadInterval_Type.__name__ = "Integer32"
_F3OspfIpInterfaceExtRtrDeadInterval_Object = MibTableColumn
f3OspfIpInterfaceExtRtrDeadInterval = _F3OspfIpInterfaceExtRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 5),
    _F3OspfIpInterfaceExtRtrDeadInterval_Type()
)
f3OspfIpInterfaceExtRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtRtrDeadInterval.setUnits("seconds")


class _F3OspfIpInterfaceExtRetransInterval_Type(Integer32):
    """Custom type f3OspfIpInterfaceExtRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3OspfIpInterfaceExtRetransInterval_Type.__name__ = "Integer32"
_F3OspfIpInterfaceExtRetransInterval_Object = MibTableColumn
f3OspfIpInterfaceExtRetransInterval = _F3OspfIpInterfaceExtRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 6),
    _F3OspfIpInterfaceExtRetransInterval_Type()
)
f3OspfIpInterfaceExtRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtRetransInterval.setUnits("seconds")


class _F3OspfIpInterfaceExtRtrPriority_Type(DesignatedRouterPriority):
    """Custom type f3OspfIpInterfaceExtRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_F3OspfIpInterfaceExtRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_F3OspfIpInterfaceExtRtrPriority_Object = MibTableColumn
f3OspfIpInterfaceExtRtrPriority = _F3OspfIpInterfaceExtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 7),
    _F3OspfIpInterfaceExtRtrPriority_Type()
)
f3OspfIpInterfaceExtRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtRtrPriority.setStatus("current")


class _F3OspfIpInterfaceExtCost_Type(Integer32):
    """Custom type f3OspfIpInterfaceExtCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3OspfIpInterfaceExtCost_Type.__name__ = "Integer32"
_F3OspfIpInterfaceExtCost_Object = MibTableColumn
f3OspfIpInterfaceExtCost = _F3OspfIpInterfaceExtCost_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 8),
    _F3OspfIpInterfaceExtCost_Type()
)
f3OspfIpInterfaceExtCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtCost.setStatus("current")


class _F3OspfIpInterfaceExtAuthType_Type(OspfAuthenticationType):
    """Custom type f3OspfIpInterfaceExtAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_F3OspfIpInterfaceExtAuthType_Type.__name__ = "OspfAuthenticationType"
_F3OspfIpInterfaceExtAuthType_Object = MibTableColumn
f3OspfIpInterfaceExtAuthType = _F3OspfIpInterfaceExtAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 9),
    _F3OspfIpInterfaceExtAuthType_Type()
)
f3OspfIpInterfaceExtAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtAuthType.setStatus("current")


class _F3OspfIpInterfaceExtAuthKey_Type(OctetString):
    """Custom type f3OspfIpInterfaceExtAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3OspfIpInterfaceExtAuthKey_Type.__name__ = "OctetString"
_F3OspfIpInterfaceExtAuthKey_Object = MibTableColumn
f3OspfIpInterfaceExtAuthKey = _F3OspfIpInterfaceExtAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 3, 1, 10),
    _F3OspfIpInterfaceExtAuthKey_Type()
)
f3OspfIpInterfaceExtAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtAuthKey.setStatus("current")
_F3OspfIpMgmtTunnelExtTable_Object = MibTable
f3OspfIpMgmtTunnelExtTable = _F3OspfIpMgmtTunnelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4)
)
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtTable.setStatus("current")
_F3OspfIpMgmtTunnelExtEntry_Object = MibTableRow
f3OspfIpMgmtTunnelExtEntry = _F3OspfIpMgmtTunnelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1)
)
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtEntry.setStatus("current")


class _F3OspfIpMgmtTunnelExtStatus_Type(OspfState):
    """Custom type f3OspfIpMgmtTunnelExtStatus based on OspfState"""
    defaultValue = 1


_F3OspfIpMgmtTunnelExtStatus_Type.__name__ = "OspfState"
_F3OspfIpMgmtTunnelExtStatus_Object = MibTableColumn
f3OspfIpMgmtTunnelExtStatus = _F3OspfIpMgmtTunnelExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 1),
    _F3OspfIpMgmtTunnelExtStatus_Type()
)
f3OspfIpMgmtTunnelExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtStatus.setStatus("current")


class _F3OspfIpMgmtTunnelExtAreaId_Type(AreaID):
    """Custom type f3OspfIpMgmtTunnelExtAreaId based on AreaID"""
    defaultHexValue = "00000000"


_F3OspfIpMgmtTunnelExtAreaId_Type.__name__ = "AreaID"
_F3OspfIpMgmtTunnelExtAreaId_Object = MibTableColumn
f3OspfIpMgmtTunnelExtAreaId = _F3OspfIpMgmtTunnelExtAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 2),
    _F3OspfIpMgmtTunnelExtAreaId_Type()
)
f3OspfIpMgmtTunnelExtAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtAreaId.setStatus("current")


class _F3OspfIpMgmtTunnelExtIfType_Type(Integer32):
    """Custom type f3OspfIpMgmtTunnelExtIfType based on Integer32"""
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


_F3OspfIpMgmtTunnelExtIfType_Type.__name__ = "Integer32"
_F3OspfIpMgmtTunnelExtIfType_Object = MibTableColumn
f3OspfIpMgmtTunnelExtIfType = _F3OspfIpMgmtTunnelExtIfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 3),
    _F3OspfIpMgmtTunnelExtIfType_Type()
)
f3OspfIpMgmtTunnelExtIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtIfType.setStatus("current")


class _F3OspfIpMgmtTunnelExtHelloInterval_Type(HelloRange):
    """Custom type f3OspfIpMgmtTunnelExtHelloInterval based on HelloRange"""
    defaultValue = 10


_F3OspfIpMgmtTunnelExtHelloInterval_Type.__name__ = "HelloRange"
_F3OspfIpMgmtTunnelExtHelloInterval_Object = MibTableColumn
f3OspfIpMgmtTunnelExtHelloInterval = _F3OspfIpMgmtTunnelExtHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 4),
    _F3OspfIpMgmtTunnelExtHelloInterval_Type()
)
f3OspfIpMgmtTunnelExtHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtHelloInterval.setUnits("seconds")


class _F3OspfIpMgmtTunnelExtRtrDeadInterval_Type(Integer32):
    """Custom type f3OspfIpMgmtTunnelExtRtrDeadInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3OspfIpMgmtTunnelExtRtrDeadInterval_Type.__name__ = "Integer32"
_F3OspfIpMgmtTunnelExtRtrDeadInterval_Object = MibTableColumn
f3OspfIpMgmtTunnelExtRtrDeadInterval = _F3OspfIpMgmtTunnelExtRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 5),
    _F3OspfIpMgmtTunnelExtRtrDeadInterval_Type()
)
f3OspfIpMgmtTunnelExtRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtRtrDeadInterval.setUnits("seconds")


class _F3OspfIpMgmtTunnelExtRetransInterval_Type(Integer32):
    """Custom type f3OspfIpMgmtTunnelExtRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3OspfIpMgmtTunnelExtRetransInterval_Type.__name__ = "Integer32"
_F3OspfIpMgmtTunnelExtRetransInterval_Object = MibTableColumn
f3OspfIpMgmtTunnelExtRetransInterval = _F3OspfIpMgmtTunnelExtRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 6),
    _F3OspfIpMgmtTunnelExtRetransInterval_Type()
)
f3OspfIpMgmtTunnelExtRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtRetransInterval.setUnits("seconds")


class _F3OspfIpMgmtTunnelExtRtrPriority_Type(DesignatedRouterPriority):
    """Custom type f3OspfIpMgmtTunnelExtRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_F3OspfIpMgmtTunnelExtRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_F3OspfIpMgmtTunnelExtRtrPriority_Object = MibTableColumn
f3OspfIpMgmtTunnelExtRtrPriority = _F3OspfIpMgmtTunnelExtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 7),
    _F3OspfIpMgmtTunnelExtRtrPriority_Type()
)
f3OspfIpMgmtTunnelExtRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtRtrPriority.setStatus("current")


class _F3OspfIpMgmtTunnelExtCost_Type(Integer32):
    """Custom type f3OspfIpMgmtTunnelExtCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3OspfIpMgmtTunnelExtCost_Type.__name__ = "Integer32"
_F3OspfIpMgmtTunnelExtCost_Object = MibTableColumn
f3OspfIpMgmtTunnelExtCost = _F3OspfIpMgmtTunnelExtCost_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 8),
    _F3OspfIpMgmtTunnelExtCost_Type()
)
f3OspfIpMgmtTunnelExtCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtCost.setStatus("current")


class _F3OspfIpMgmtTunnelExtAuthType_Type(OspfAuthenticationType):
    """Custom type f3OspfIpMgmtTunnelExtAuthType based on OspfAuthenticationType"""
    defaultValue = 0


_F3OspfIpMgmtTunnelExtAuthType_Type.__name__ = "OspfAuthenticationType"
_F3OspfIpMgmtTunnelExtAuthType_Object = MibTableColumn
f3OspfIpMgmtTunnelExtAuthType = _F3OspfIpMgmtTunnelExtAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 9),
    _F3OspfIpMgmtTunnelExtAuthType_Type()
)
f3OspfIpMgmtTunnelExtAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtAuthType.setStatus("current")


class _F3OspfIpMgmtTunnelExtAuthKey_Type(OctetString):
    """Custom type f3OspfIpMgmtTunnelExtAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_F3OspfIpMgmtTunnelExtAuthKey_Type.__name__ = "OctetString"
_F3OspfIpMgmtTunnelExtAuthKey_Object = MibTableColumn
f3OspfIpMgmtTunnelExtAuthKey = _F3OspfIpMgmtTunnelExtAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 4, 1, 10),
    _F3OspfIpMgmtTunnelExtAuthKey_Type()
)
f3OspfIpMgmtTunnelExtAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtAuthKey.setStatus("current")
_F3OspfNbrExtTable_Object = MibTable
f3OspfNbrExtTable = _F3OspfNbrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 5)
)
if mibBuilder.loadTexts:
    f3OspfNbrExtTable.setStatus("current")
_F3OspfNbrExtEntry_Object = MibTableRow
f3OspfNbrExtEntry = _F3OspfNbrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 5, 1)
)
if mibBuilder.loadTexts:
    f3OspfNbrExtEntry.setStatus("current")
_F3OspfNbrExtRole_Type = OspfRole
_F3OspfNbrExtRole_Object = MibTableColumn
f3OspfNbrExtRole = _F3OspfNbrExtRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 1, 5, 1, 1),
    _F3OspfNbrExtRole_Type()
)
f3OspfNbrExtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3OspfNbrExtRole.setStatus("current")
_F3OspfConformance_ObjectIdentity = ObjectIdentity
f3OspfConformance = _F3OspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2)
)
_F3OspfCompliances_ObjectIdentity = ObjectIdentity
f3OspfCompliances = _F3OspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 1)
)
_F3OspfGroups_ObjectIdentity = ObjectIdentity
f3OspfGroups = _F3OspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2)
)
cmIpInterfaceEntry.registerAugmentions(
    ("F3-OSPF-MIB",
     "f3OspfIpInterfaceExtEntry")
)
f3OspfIpInterfaceExtEntry.setIndexNames(*cmIpInterfaceEntry.getIndexNames())
ipManagementTunnelEntry.registerAugmentions(
    ("F3-OSPF-MIB",
     "f3OspfIpMgmtTunnelExtEntry")
)
f3OspfIpMgmtTunnelExtEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("F3-OSPF-MIB",
     "f3OspfNbrExtEntry")
)
f3OspfNbrExtEntry.setIndexNames(*ospfNbrEntry.getIndexNames())

# Managed Objects groups

f3OspfRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 1)
)
f3OspfRouterGroup.setObjects(
      *(("F3-OSPF-MIB", "f3OspfRouterMetricType"),
        ("F3-OSPF-MIB", "f3OspfRouterMetric"),
        ("F3-OSPF-MIB", "f3OspfRouterRedistributionType"),
        ("F3-OSPF-MIB", "f3OspfRouterNumAttachedAreas"),
        ("F3-OSPF-MIB", "f3OspfRouterAreaBdrRtrStatus"),
        ("F3-OSPF-MIB", "f3OspfRouterStorageType"),
        ("F3-OSPF-MIB", "f3OspfRouterRowStatus"))
)
if mibBuilder.loadTexts:
    f3OspfRouterGroup.setStatus("current")

f3OspfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 2)
)
f3OspfAreaGroup.setObjects(
      *(("F3-OSPF-MIB", "f3OspfAreaType"),
        ("F3-OSPF-MIB", "f3OspfAreaAuthType"),
        ("F3-OSPF-MIB", "f3OspfAreaDefaultCost"),
        ("F3-OSPF-MIB", "f3OspfAreaSpfRuns"),
        ("F3-OSPF-MIB", "f3OspfAreaLsaCount"),
        ("F3-OSPF-MIB", "f3OspfAreaStorageType"),
        ("F3-OSPF-MIB", "f3OspfAreaRowStatus"))
)
if mibBuilder.loadTexts:
    f3OspfAreaGroup.setStatus("current")

f3OspfIpInterfaceExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 3)
)
f3OspfIpInterfaceExtGroup.setObjects(
      *(("F3-OSPF-MIB", "f3OspfIpInterfaceExtStatus"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtAreaId"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtIfType"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtHelloInterval"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtRtrDeadInterval"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtRetransInterval"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtRtrPriority"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtCost"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtAuthType"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtAuthKey"))
)
if mibBuilder.loadTexts:
    f3OspfIpInterfaceExtGroup.setStatus("current")

f3OspfIpMgmtTunnelExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 4)
)
f3OspfIpMgmtTunnelExtGroup.setObjects(
      *(("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtStatus"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtAreaId"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtIfType"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtHelloInterval"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtRtrDeadInterval"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtRetransInterval"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtRtrPriority"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtCost"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtAuthType"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtAuthKey"))
)
if mibBuilder.loadTexts:
    f3OspfIpMgmtTunnelExtGroup.setStatus("current")

f3OspfNbrExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 2, 5)
)
f3OspfNbrExtGroup.setObjects(
    ("F3-OSPF-MIB", "f3OspfNbrExtRole")
)
if mibBuilder.loadTexts:
    f3OspfNbrExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3OspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 35, 2, 1, 1)
)
f3OspfCompliance.setObjects(
      *(("F3-OSPF-MIB", "f3OspfRouterGroup"),
        ("F3-OSPF-MIB", "f3OspfAreaGroup"),
        ("F3-OSPF-MIB", "f3OspfIpInterfaceExtGroup"),
        ("F3-OSPF-MIB", "f3OspfIpMgmtTunnelExtGroup"),
        ("F3-OSPF-MIB", "f3OspfNbrExtGroup"))
)
if mibBuilder.loadTexts:
    f3OspfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-OSPF-MIB",
    **{"OspfMetricType": OspfMetricType,
       "OspfRedistributionType": OspfRedistributionType,
       "OspfState": OspfState,
       "OspfAreaType": OspfAreaType,
       "OspfRole": OspfRole,
       "f3OspfMIB": f3OspfMIB,
       "f3OspfConfigObjects": f3OspfConfigObjects,
       "f3OspfRouterTable": f3OspfRouterTable,
       "f3OspfRouterEntry": f3OspfRouterEntry,
       "f3OspfRouterIndex": f3OspfRouterIndex,
       "f3OspfRouterMetricType": f3OspfRouterMetricType,
       "f3OspfRouterMetric": f3OspfRouterMetric,
       "f3OspfRouterRedistributionType": f3OspfRouterRedistributionType,
       "f3OspfRouterNumAttachedAreas": f3OspfRouterNumAttachedAreas,
       "f3OspfRouterAreaBdrRtrStatus": f3OspfRouterAreaBdrRtrStatus,
       "f3OspfRouterStorageType": f3OspfRouterStorageType,
       "f3OspfRouterRowStatus": f3OspfRouterRowStatus,
       "f3OspfAreaTable": f3OspfAreaTable,
       "f3OspfAreaEntry": f3OspfAreaEntry,
       "f3OspfAreaId": f3OspfAreaId,
       "f3OspfAreaType": f3OspfAreaType,
       "f3OspfAreaAuthType": f3OspfAreaAuthType,
       "f3OspfAreaDefaultCost": f3OspfAreaDefaultCost,
       "f3OspfAreaSpfRuns": f3OspfAreaSpfRuns,
       "f3OspfAreaLsaCount": f3OspfAreaLsaCount,
       "f3OspfAreaStorageType": f3OspfAreaStorageType,
       "f3OspfAreaRowStatus": f3OspfAreaRowStatus,
       "f3OspfIpInterfaceExtTable": f3OspfIpInterfaceExtTable,
       "f3OspfIpInterfaceExtEntry": f3OspfIpInterfaceExtEntry,
       "f3OspfIpInterfaceExtStatus": f3OspfIpInterfaceExtStatus,
       "f3OspfIpInterfaceExtAreaId": f3OspfIpInterfaceExtAreaId,
       "f3OspfIpInterfaceExtIfType": f3OspfIpInterfaceExtIfType,
       "f3OspfIpInterfaceExtHelloInterval": f3OspfIpInterfaceExtHelloInterval,
       "f3OspfIpInterfaceExtRtrDeadInterval": f3OspfIpInterfaceExtRtrDeadInterval,
       "f3OspfIpInterfaceExtRetransInterval": f3OspfIpInterfaceExtRetransInterval,
       "f3OspfIpInterfaceExtRtrPriority": f3OspfIpInterfaceExtRtrPriority,
       "f3OspfIpInterfaceExtCost": f3OspfIpInterfaceExtCost,
       "f3OspfIpInterfaceExtAuthType": f3OspfIpInterfaceExtAuthType,
       "f3OspfIpInterfaceExtAuthKey": f3OspfIpInterfaceExtAuthKey,
       "f3OspfIpMgmtTunnelExtTable": f3OspfIpMgmtTunnelExtTable,
       "f3OspfIpMgmtTunnelExtEntry": f3OspfIpMgmtTunnelExtEntry,
       "f3OspfIpMgmtTunnelExtStatus": f3OspfIpMgmtTunnelExtStatus,
       "f3OspfIpMgmtTunnelExtAreaId": f3OspfIpMgmtTunnelExtAreaId,
       "f3OspfIpMgmtTunnelExtIfType": f3OspfIpMgmtTunnelExtIfType,
       "f3OspfIpMgmtTunnelExtHelloInterval": f3OspfIpMgmtTunnelExtHelloInterval,
       "f3OspfIpMgmtTunnelExtRtrDeadInterval": f3OspfIpMgmtTunnelExtRtrDeadInterval,
       "f3OspfIpMgmtTunnelExtRetransInterval": f3OspfIpMgmtTunnelExtRetransInterval,
       "f3OspfIpMgmtTunnelExtRtrPriority": f3OspfIpMgmtTunnelExtRtrPriority,
       "f3OspfIpMgmtTunnelExtCost": f3OspfIpMgmtTunnelExtCost,
       "f3OspfIpMgmtTunnelExtAuthType": f3OspfIpMgmtTunnelExtAuthType,
       "f3OspfIpMgmtTunnelExtAuthKey": f3OspfIpMgmtTunnelExtAuthKey,
       "f3OspfNbrExtTable": f3OspfNbrExtTable,
       "f3OspfNbrExtEntry": f3OspfNbrExtEntry,
       "f3OspfNbrExtRole": f3OspfNbrExtRole,
       "f3OspfConformance": f3OspfConformance,
       "f3OspfCompliances": f3OspfCompliances,
       "f3OspfCompliance": f3OspfCompliance,
       "f3OspfGroups": f3OspfGroups,
       "f3OspfRouterGroup": f3OspfRouterGroup,
       "f3OspfAreaGroup": f3OspfAreaGroup,
       "f3OspfIpInterfaceExtGroup": f3OspfIpInterfaceExtGroup,
       "f3OspfIpMgmtTunnelExtGroup": f3OspfIpMgmtTunnelExtGroup,
       "f3OspfNbrExtGroup": f3OspfNbrExtGroup}
)
