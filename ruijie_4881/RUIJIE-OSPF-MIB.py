# SNMP MIB module (RUIJIE-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-OSPF-MIB.mib
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

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 PositiveInteger,
 RouterID,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "PositiveInteger",
    "RouterID",
    "Status")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus")

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

ruijieOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30)
)
if mibBuilder.loadTexts:
    ruijieOspfMIB.setRevisions(
        ("2002-11-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieOspfMIBObjects_ObjectIdentity = ObjectIdentity
ruijieOspfMIBObjects = _RuijieOspfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1)
)
_RuijieOspfGeneralMibsGroup_ObjectIdentity = ObjectIdentity
ruijieOspfGeneralMibsGroup = _RuijieOspfGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1)
)
_RuijieOspfMiniLsaInterval_Type = Unsigned32
_RuijieOspfMiniLsaInterval_Object = MibScalar
ruijieOspfMiniLsaInterval = _RuijieOspfMiniLsaInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 1),
    _RuijieOspfMiniLsaInterval_Type()
)
ruijieOspfMiniLsaInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfMiniLsaInterval.setStatus("current")
_RuijieOspfMiniLsaArrival_Type = Unsigned32
_RuijieOspfMiniLsaArrival_Object = MibScalar
ruijieOspfMiniLsaArrival = _RuijieOspfMiniLsaArrival_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 2),
    _RuijieOspfMiniLsaArrival_Type()
)
ruijieOspfMiniLsaArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfMiniLsaArrival.setStatus("current")
_RuijieOspfAreasNum_Type = Unsigned32
_RuijieOspfAreasNum_Object = MibScalar
ruijieOspfAreasNum = _RuijieOspfAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 3),
    _RuijieOspfAreasNum_Type()
)
ruijieOspfAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreasNum.setStatus("current")
_RuijieOspfNormalAreasNum_Type = Unsigned32
_RuijieOspfNormalAreasNum_Object = MibScalar
ruijieOspfNormalAreasNum = _RuijieOspfNormalAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 4),
    _RuijieOspfNormalAreasNum_Type()
)
ruijieOspfNormalAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNormalAreasNum.setStatus("current")
_RuijieOspfStubAreasNum_Type = Unsigned32
_RuijieOspfStubAreasNum_Object = MibScalar
ruijieOspfStubAreasNum = _RuijieOspfStubAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 5),
    _RuijieOspfStubAreasNum_Type()
)
ruijieOspfStubAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfStubAreasNum.setStatus("current")
_RuijieOspfNssaAreasNum_Type = Unsigned32
_RuijieOspfNssaAreasNum_Object = MibScalar
ruijieOspfNssaAreasNum = _RuijieOspfNssaAreasNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 6),
    _RuijieOspfNssaAreasNum_Type()
)
ruijieOspfNssaAreasNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNssaAreasNum.setStatus("current")


class _RuijieOspfSpfDelay_Type(Unsigned32):
    """Custom type ruijieOspfSpfDelay based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieOspfSpfDelay_Type.__name__ = "Unsigned32"
_RuijieOspfSpfDelay_Object = MibScalar
ruijieOspfSpfDelay = _RuijieOspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 7),
    _RuijieOspfSpfDelay_Type()
)
ruijieOspfSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfSpfDelay.setStatus("current")


class _RuijieOspfSpfHoldTime_Type(Unsigned32):
    """Custom type ruijieOspfSpfHoldTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieOspfSpfHoldTime_Type.__name__ = "Unsigned32"
_RuijieOspfSpfHoldTime_Object = MibScalar
ruijieOspfSpfHoldTime = _RuijieOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 8),
    _RuijieOspfSpfHoldTime_Type()
)
ruijieOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfSpfHoldTime.setStatus("current")


class _RuijieOspfAutoCostRefBandWidthRef_Type(Unsigned32):
    """Custom type ruijieOspfAutoCostRefBandWidthRef based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieOspfAutoCostRefBandWidthRef_Type.__name__ = "Unsigned32"
_RuijieOspfAutoCostRefBandWidthRef_Object = MibScalar
ruijieOspfAutoCostRefBandWidthRef = _RuijieOspfAutoCostRefBandWidthRef_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 9),
    _RuijieOspfAutoCostRefBandWidthRef_Type()
)
ruijieOspfAutoCostRefBandWidthRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfAutoCostRefBandWidthRef.setStatus("current")


class _RuijieOspfLsaGroupPacing_Type(Unsigned32):
    """Custom type ruijieOspfLsaGroupPacing based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_RuijieOspfLsaGroupPacing_Type.__name__ = "Unsigned32"
_RuijieOspfLsaGroupPacing_Object = MibScalar
ruijieOspfLsaGroupPacing = _RuijieOspfLsaGroupPacing_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 10),
    _RuijieOspfLsaGroupPacing_Type()
)
ruijieOspfLsaGroupPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfLsaGroupPacing.setStatus("current")


class _RuijieOspfInterDistance_Type(Unsigned32):
    """Custom type ruijieOspfInterDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieOspfInterDistance_Type.__name__ = "Unsigned32"
_RuijieOspfInterDistance_Object = MibScalar
ruijieOspfInterDistance = _RuijieOspfInterDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 11),
    _RuijieOspfInterDistance_Type()
)
ruijieOspfInterDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfInterDistance.setStatus("current")


class _RuijieOspfIntraDistance_Type(Unsigned32):
    """Custom type ruijieOspfIntraDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieOspfIntraDistance_Type.__name__ = "Unsigned32"
_RuijieOspfIntraDistance_Object = MibScalar
ruijieOspfIntraDistance = _RuijieOspfIntraDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 12),
    _RuijieOspfIntraDistance_Type()
)
ruijieOspfIntraDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIntraDistance.setStatus("current")


class _RuijieOspfExternDistance_Type(Unsigned32):
    """Custom type ruijieOspfExternDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieOspfExternDistance_Type.__name__ = "Unsigned32"
_RuijieOspfExternDistance_Object = MibScalar
ruijieOspfExternDistance = _RuijieOspfExternDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 13),
    _RuijieOspfExternDistance_Type()
)
ruijieOspfExternDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfExternDistance.setStatus("current")


class _RuijieOspfLogAdjChangeNotify_Type(EnabledStatus):
    """Custom type ruijieOspfLogAdjChangeNotify based on EnabledStatus"""
    defaultValue = 1


_RuijieOspfLogAdjChangeNotify_Type.__name__ = "EnabledStatus"
_RuijieOspfLogAdjChangeNotify_Object = MibScalar
ruijieOspfLogAdjChangeNotify = _RuijieOspfLogAdjChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 14),
    _RuijieOspfLogAdjChangeNotify_Type()
)
ruijieOspfLogAdjChangeNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfLogAdjChangeNotify.setStatus("current")


class _RuijieOspfPassiveStatus_Type(EnabledStatus):
    """Custom type ruijieOspfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieOspfPassiveStatus_Type.__name__ = "EnabledStatus"
_RuijieOspfPassiveStatus_Object = MibScalar
ruijieOspfPassiveStatus = _RuijieOspfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 15),
    _RuijieOspfPassiveStatus_Type()
)
ruijieOspfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfPassiveStatus.setStatus("current")


class _RuijieOspfRFC1583Compatibility_Type(EnabledStatus):
    """Custom type ruijieOspfRFC1583Compatibility based on EnabledStatus"""
    defaultValue = 1


_RuijieOspfRFC1583Compatibility_Type.__name__ = "EnabledStatus"
_RuijieOspfRFC1583Compatibility_Object = MibScalar
ruijieOspfRFC1583Compatibility = _RuijieOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 16),
    _RuijieOspfRFC1583Compatibility_Type()
)
ruijieOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfRFC1583Compatibility.setStatus("current")


class _RuijieOspfRouteRedisDefMetricVal_Type(Unsigned32):
    """Custom type ruijieOspfRouteRedisDefMetricVal based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_RuijieOspfRouteRedisDefMetricVal_Type.__name__ = "Unsigned32"
_RuijieOspfRouteRedisDefMetricVal_Object = MibScalar
ruijieOspfRouteRedisDefMetricVal = _RuijieOspfRouteRedisDefMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 17),
    _RuijieOspfRouteRedisDefMetricVal_Type()
)
ruijieOspfRouteRedisDefMetricVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfRouteRedisDefMetricVal.setStatus("current")


class _RuijieOspfAdminiDistance_Type(Unsigned32):
    """Custom type ruijieOspfAdminiDistance based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieOspfAdminiDistance_Type.__name__ = "Unsigned32"
_RuijieOspfAdminiDistance_Object = MibScalar
ruijieOspfAdminiDistance = _RuijieOspfAdminiDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 1, 18),
    _RuijieOspfAdminiDistance_Type()
)
ruijieOspfAdminiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfAdminiDistance.setStatus("current")
_RuijieOspfAreaTable_Object = MibTable
ruijieOspfAreaTable = _RuijieOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieOspfAreaTable.setStatus("current")
_RuijieOspfAreaEntry_Object = MibTableRow
ruijieOspfAreaEntry = _RuijieOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1)
)
ruijieOspfAreaEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfAreaId"),
)
if mibBuilder.loadTexts:
    ruijieOspfAreaEntry.setStatus("current")
_RuijieOspfAreaId_Type = AreaID
_RuijieOspfAreaId_Object = MibTableColumn
ruijieOspfAreaId = _RuijieOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 1),
    _RuijieOspfAreaId_Type()
)
ruijieOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaId.setStatus("current")


class _RuijieOspfAuthType_Type(Integer32):
    """Custom type ruijieOspfAuthType based on Integer32"""
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
        *(("none", 0),
          ("simplePassword", 1),
          ("md5", 2))
    )


_RuijieOspfAuthType_Type.__name__ = "Integer32"
_RuijieOspfAuthType_Object = MibTableColumn
ruijieOspfAuthType = _RuijieOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 2),
    _RuijieOspfAuthType_Type()
)
ruijieOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfAuthType.setStatus("current")


class _RuijieOspfImportAsExtern_Type(Integer32):
    """Custom type ruijieOspfImportAsExtern based on Integer32"""
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


_RuijieOspfImportAsExtern_Type.__name__ = "Integer32"
_RuijieOspfImportAsExtern_Object = MibTableColumn
ruijieOspfImportAsExtern = _RuijieOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 3),
    _RuijieOspfImportAsExtern_Type()
)
ruijieOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfImportAsExtern.setStatus("current")
_RuijieOspfSpfRuns_Type = Counter32
_RuijieOspfSpfRuns_Object = MibTableColumn
ruijieOspfSpfRuns = _RuijieOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 4),
    _RuijieOspfSpfRuns_Type()
)
ruijieOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfSpfRuns.setStatus("current")
_RuijieOspfAreaBdrRtrCount_Type = Gauge32
_RuijieOspfAreaBdrRtrCount_Object = MibTableColumn
ruijieOspfAreaBdrRtrCount = _RuijieOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 5),
    _RuijieOspfAreaBdrRtrCount_Type()
)
ruijieOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaBdrRtrCount.setStatus("current")
_RuijieOspfAsBdrRtrCount_Type = Gauge32
_RuijieOspfAsBdrRtrCount_Object = MibTableColumn
ruijieOspfAsBdrRtrCount = _RuijieOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 6),
    _RuijieOspfAsBdrRtrCount_Type()
)
ruijieOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAsBdrRtrCount.setStatus("current")
_RuijieOspfAreaLsaCount_Type = Gauge32
_RuijieOspfAreaLsaCount_Object = MibTableColumn
ruijieOspfAreaLsaCount = _RuijieOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 7),
    _RuijieOspfAreaLsaCount_Type()
)
ruijieOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaCount.setStatus("current")


class _RuijieOspfAreaLsaCksumSum_Type(Unsigned32):
    """Custom type ruijieOspfAreaLsaCksumSum based on Unsigned32"""
    defaultValue = 0


_RuijieOspfAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_RuijieOspfAreaLsaCksumSum_Object = MibTableColumn
ruijieOspfAreaLsaCksumSum = _RuijieOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 8),
    _RuijieOspfAreaLsaCksumSum_Type()
)
ruijieOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaCksumSum.setStatus("current")


class _RuijieOspfAreaSummary_Type(Integer32):
    """Custom type ruijieOspfAreaSummary based on Integer32"""
    defaultValue = 2

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


_RuijieOspfAreaSummary_Type.__name__ = "Integer32"
_RuijieOspfAreaSummary_Object = MibTableColumn
ruijieOspfAreaSummary = _RuijieOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 9),
    _RuijieOspfAreaSummary_Type()
)
ruijieOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfAreaSummary.setStatus("current")
_RuijieOspfAreaStatus_Type = RowStatus
_RuijieOspfAreaStatus_Object = MibTableColumn
ruijieOspfAreaStatus = _RuijieOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 10),
    _RuijieOspfAreaStatus_Type()
)
ruijieOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfAreaStatus.setStatus("current")
_RuijieOspfAreaInterfaceNum_Type = Unsigned32
_RuijieOspfAreaInterfaceNum_Object = MibTableColumn
ruijieOspfAreaInterfaceNum = _RuijieOspfAreaInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 11),
    _RuijieOspfAreaInterfaceNum_Type()
)
ruijieOspfAreaInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaInterfaceNum.setStatus("current")


class _RuijieOspfAreaNssaIsRedistribution_Type(TruthValue):
    """Custom type ruijieOspfAreaNssaIsRedistribution based on TruthValue"""
    defaultValue = 1


_RuijieOspfAreaNssaIsRedistribution_Type.__name__ = "TruthValue"
_RuijieOspfAreaNssaIsRedistribution_Object = MibTableColumn
ruijieOspfAreaNssaIsRedistribution = _RuijieOspfAreaNssaIsRedistribution_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 12),
    _RuijieOspfAreaNssaIsRedistribution_Type()
)
ruijieOspfAreaNssaIsRedistribution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfAreaNssaIsRedistribution.setStatus("current")


class _RuijieOspfAreaNssaIsDefInfoOriginate_Type(TruthValue):
    """Custom type ruijieOspfAreaNssaIsDefInfoOriginate based on TruthValue"""
    defaultValue = 2


_RuijieOspfAreaNssaIsDefInfoOriginate_Type.__name__ = "TruthValue"
_RuijieOspfAreaNssaIsDefInfoOriginate_Object = MibTableColumn
ruijieOspfAreaNssaIsDefInfoOriginate = _RuijieOspfAreaNssaIsDefInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 2, 1, 13),
    _RuijieOspfAreaNssaIsDefInfoOriginate_Type()
)
ruijieOspfAreaNssaIsDefInfoOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfAreaNssaIsDefInfoOriginate.setStatus("current")
_RuijieOspfAddressScopeTable_Object = MibTable
ruijieOspfAddressScopeTable = _RuijieOspfAddressScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieOspfAddressScopeTable.setStatus("current")
_RuijieOspfAddressScopeEntry_Object = MibTableRow
ruijieOspfAddressScopeEntry = _RuijieOspfAddressScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 3, 1)
)
ruijieOspfAddressScopeEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfNetWorkAreaID"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfNetWorkAddress"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfNetWorkMask"),
)
if mibBuilder.loadTexts:
    ruijieOspfAddressScopeEntry.setStatus("current")
_RuijieOspfNetWorkAreaID_Type = IpAddress
_RuijieOspfNetWorkAreaID_Object = MibTableColumn
ruijieOspfNetWorkAreaID = _RuijieOspfNetWorkAreaID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 3, 1, 1),
    _RuijieOspfNetWorkAreaID_Type()
)
ruijieOspfNetWorkAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNetWorkAreaID.setStatus("current")
_RuijieOspfNetWorkAddress_Type = IpAddress
_RuijieOspfNetWorkAddress_Object = MibTableColumn
ruijieOspfNetWorkAddress = _RuijieOspfNetWorkAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 3, 1, 2),
    _RuijieOspfNetWorkAddress_Type()
)
ruijieOspfNetWorkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNetWorkAddress.setStatus("current")
_RuijieOspfNetWorkMask_Type = IpAddress
_RuijieOspfNetWorkMask_Object = MibTableColumn
ruijieOspfNetWorkMask = _RuijieOspfNetWorkMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 3, 1, 3),
    _RuijieOspfNetWorkMask_Type()
)
ruijieOspfNetWorkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNetWorkMask.setStatus("current")
_RuijieOspfNetWorkStatus_Type = RowStatus
_RuijieOspfNetWorkStatus_Object = MibTableColumn
ruijieOspfNetWorkStatus = _RuijieOspfNetWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 3, 1, 4),
    _RuijieOspfNetWorkStatus_Type()
)
ruijieOspfNetWorkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfNetWorkStatus.setStatus("current")
_RuijieOspfIfTable_Object = MibTable
ruijieOspfIfTable = _RuijieOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieOspfIfTable.setStatus("current")
_RuijieOspfIfEntry_Object = MibTableRow
ruijieOspfIfEntry = _RuijieOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1)
)
ruijieOspfIfEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfIfIpAddress"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    ruijieOspfIfEntry.setStatus("current")
_RuijieOspfIfIpAddress_Type = IpAddress
_RuijieOspfIfIpAddress_Object = MibTableColumn
ruijieOspfIfIpAddress = _RuijieOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 1),
    _RuijieOspfIfIpAddress_Type()
)
ruijieOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfIpAddress.setStatus("current")
_RuijieOspfAddressLessIf_Type = Unsigned32
_RuijieOspfAddressLessIf_Object = MibTableColumn
ruijieOspfAddressLessIf = _RuijieOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 2),
    _RuijieOspfAddressLessIf_Type()
)
ruijieOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAddressLessIf.setStatus("current")


class _RuijieOspfIfAreaId_Type(AreaID):
    """Custom type ruijieOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_RuijieOspfIfAreaId_Type.__name__ = "AreaID"
_RuijieOspfIfAreaId_Object = MibTableColumn
ruijieOspfIfAreaId = _RuijieOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 3),
    _RuijieOspfIfAreaId_Type()
)
ruijieOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfAreaId.setStatus("current")


class _RuijieOspfIfType_Type(Integer32):
    """Custom type ruijieOspfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5),
          ("loopback", 6))
    )


_RuijieOspfIfType_Type.__name__ = "Integer32"
_RuijieOspfIfType_Object = MibTableColumn
ruijieOspfIfType = _RuijieOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 4),
    _RuijieOspfIfType_Type()
)
ruijieOspfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfType.setStatus("current")
_RuijieOspfIfAdminStat_Type = Status
_RuijieOspfIfAdminStat_Object = MibTableColumn
ruijieOspfIfAdminStat = _RuijieOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 5),
    _RuijieOspfIfAdminStat_Type()
)
ruijieOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfAdminStat.setStatus("current")


class _RuijieOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type ruijieOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RuijieOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_RuijieOspfIfRtrPriority_Object = MibTableColumn
ruijieOspfIfRtrPriority = _RuijieOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 6),
    _RuijieOspfIfRtrPriority_Type()
)
ruijieOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfRtrPriority.setStatus("current")


class _RuijieOspfIfTransitDelay_Type(Unsigned32):
    """Custom type ruijieOspfIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieOspfIfTransitDelay_Type.__name__ = "Unsigned32"
_RuijieOspfIfTransitDelay_Object = MibTableColumn
ruijieOspfIfTransitDelay = _RuijieOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 7),
    _RuijieOspfIfTransitDelay_Type()
)
ruijieOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfTransitDelay.setStatus("current")


class _RuijieOspfIfRetransInterval_Type(Unsigned32):
    """Custom type ruijieOspfIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieOspfIfRetransInterval_Type.__name__ = "Unsigned32"
_RuijieOspfIfRetransInterval_Object = MibTableColumn
ruijieOspfIfRetransInterval = _RuijieOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 8),
    _RuijieOspfIfRetransInterval_Type()
)
ruijieOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfRetransInterval.setStatus("current")


class _RuijieOspfIfHelloInterval_Type(HelloRange):
    """Custom type ruijieOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RuijieOspfIfHelloInterval_Type.__name__ = "HelloRange"
_RuijieOspfIfHelloInterval_Object = MibTableColumn
ruijieOspfIfHelloInterval = _RuijieOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 9),
    _RuijieOspfIfHelloInterval_Type()
)
ruijieOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfHelloInterval.setStatus("current")


class _RuijieOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ruijieOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_RuijieOspfIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_RuijieOspfIfRtrDeadInterval_Object = MibTableColumn
ruijieOspfIfRtrDeadInterval = _RuijieOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 10),
    _RuijieOspfIfRtrDeadInterval_Type()
)
ruijieOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfRtrDeadInterval.setStatus("current")
_RuijieOspfIfPollInterval_Type = PositiveInteger
_RuijieOspfIfPollInterval_Object = MibTableColumn
ruijieOspfIfPollInterval = _RuijieOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 11),
    _RuijieOspfIfPollInterval_Type()
)
ruijieOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfPollInterval.setStatus("current")


class _RuijieOspfIfState_Type(Integer32):
    """Custom type ruijieOspfIfState based on Integer32"""
    defaultValue = 1

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


_RuijieOspfIfState_Type.__name__ = "Integer32"
_RuijieOspfIfState_Object = MibTableColumn
ruijieOspfIfState = _RuijieOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 12),
    _RuijieOspfIfState_Type()
)
ruijieOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfState.setStatus("current")


class _RuijieOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type ruijieOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RuijieOspfIfDesignatedRouter_Type.__name__ = "IpAddress"
_RuijieOspfIfDesignatedRouter_Object = MibTableColumn
ruijieOspfIfDesignatedRouter = _RuijieOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 13),
    _RuijieOspfIfDesignatedRouter_Type()
)
ruijieOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfDesignatedRouter.setStatus("current")


class _RuijieOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type ruijieOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RuijieOspfIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_RuijieOspfIfBackupDesignatedRouter_Object = MibTableColumn
ruijieOspfIfBackupDesignatedRouter = _RuijieOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 14),
    _RuijieOspfIfBackupDesignatedRouter_Type()
)
ruijieOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfBackupDesignatedRouter.setStatus("current")
_RuijieOspfIfEvents_Type = Counter32
_RuijieOspfIfEvents_Object = MibTableColumn
ruijieOspfIfEvents = _RuijieOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 15),
    _RuijieOspfIfEvents_Type()
)
ruijieOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfEvents.setStatus("current")


class _RuijieOspfIfAuthKey_Type(OctetString):
    """Custom type ruijieOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieOspfIfAuthKey_Type.__name__ = "OctetString"
_RuijieOspfIfAuthKey_Object = MibTableColumn
ruijieOspfIfAuthKey = _RuijieOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 16),
    _RuijieOspfIfAuthKey_Type()
)
ruijieOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfAuthKey.setStatus("current")
_RuijieOspfIfStatus_Type = RowStatus
_RuijieOspfIfStatus_Object = MibTableColumn
ruijieOspfIfStatus = _RuijieOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 17),
    _RuijieOspfIfStatus_Type()
)
ruijieOspfIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfStatus.setStatus("current")


class _RuijieOspfIfMulticastForwarding_Type(Integer32):
    """Custom type ruijieOspfIfMulticastForwarding based on Integer32"""
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


_RuijieOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_RuijieOspfIfMulticastForwarding_Object = MibTableColumn
ruijieOspfIfMulticastForwarding = _RuijieOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 18),
    _RuijieOspfIfMulticastForwarding_Type()
)
ruijieOspfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfMulticastForwarding.setStatus("current")


class _RuijieOspfIfDemand_Type(TruthValue):
    """Custom type ruijieOspfIfDemand based on TruthValue"""
    defaultValue = 2


_RuijieOspfIfDemand_Type.__name__ = "TruthValue"
_RuijieOspfIfDemand_Object = MibTableColumn
ruijieOspfIfDemand = _RuijieOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 19),
    _RuijieOspfIfDemand_Type()
)
ruijieOspfIfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfDemand.setStatus("current")


class _RuijieOspfIfAuthType_Type(Integer32):
    """Custom type ruijieOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieOspfIfAuthType_Type.__name__ = "Integer32"
_RuijieOspfIfAuthType_Object = MibTableColumn
ruijieOspfIfAuthType = _RuijieOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 20),
    _RuijieOspfIfAuthType_Type()
)
ruijieOspfIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfAuthType.setStatus("current")


class _RuijieOspfIfDatabaseFilterAllOut_Type(EnabledStatus):
    """Custom type ruijieOspfIfDatabaseFilterAllOut based on EnabledStatus"""
    defaultValue = 2


_RuijieOspfIfDatabaseFilterAllOut_Type.__name__ = "EnabledStatus"
_RuijieOspfIfDatabaseFilterAllOut_Object = MibTableColumn
ruijieOspfIfDatabaseFilterAllOut = _RuijieOspfIfDatabaseFilterAllOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 21),
    _RuijieOspfIfDatabaseFilterAllOut_Type()
)
ruijieOspfIfDatabaseFilterAllOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfDatabaseFilterAllOut.setStatus("current")


class _RuijieOspfIfDesignateRouterId_Type(IpAddress):
    """Custom type ruijieOspfIfDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_RuijieOspfIfDesignateRouterId_Type.__name__ = "IpAddress"
_RuijieOspfIfDesignateRouterId_Object = MibTableColumn
ruijieOspfIfDesignateRouterId = _RuijieOspfIfDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 22),
    _RuijieOspfIfDesignateRouterId_Type()
)
ruijieOspfIfDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfDesignateRouterId.setStatus("current")


class _RuijieOspfIfBackupDesignateRouterId_Type(IpAddress):
    """Custom type ruijieOspfIfBackupDesignateRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_RuijieOspfIfBackupDesignateRouterId_Type.__name__ = "IpAddress"
_RuijieOspfIfBackupDesignateRouterId_Object = MibTableColumn
ruijieOspfIfBackupDesignateRouterId = _RuijieOspfIfBackupDesignateRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 23),
    _RuijieOspfIfBackupDesignateRouterId_Type()
)
ruijieOspfIfBackupDesignateRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfBackupDesignateRouterId.setStatus("current")
_RuijieOspfIfWaitInternal_Type = TimeTicks
_RuijieOspfIfWaitInternal_Object = MibTableColumn
ruijieOspfIfWaitInternal = _RuijieOspfIfWaitInternal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 24),
    _RuijieOspfIfWaitInternal_Type()
)
ruijieOspfIfWaitInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfWaitInternal.setStatus("current")


class _RuijieOspfIfPassiveStatus_Type(EnabledStatus):
    """Custom type ruijieOspfIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieOspfIfPassiveStatus_Type.__name__ = "EnabledStatus"
_RuijieOspfIfPassiveStatus_Object = MibTableColumn
ruijieOspfIfPassiveStatus = _RuijieOspfIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 25),
    _RuijieOspfIfPassiveStatus_Type()
)
ruijieOspfIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfPassiveStatus.setStatus("current")


class _RuijieOspfIfCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type ruijieOspfIfCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieOspfIfCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_RuijieOspfIfCurrentUsedMd5AuthKeyId_Object = MibTableColumn
ruijieOspfIfCurrentUsedMd5AuthKeyId = _RuijieOspfIfCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 4, 1, 26),
    _RuijieOspfIfCurrentUsedMd5AuthKeyId_Type()
)
ruijieOspfIfCurrentUsedMd5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieOspfIfCurrentUsedMd5AuthKeyId.setStatus("current")
_RuijieOspfIfMd5AuthKeyTable_Object = MibTable
ruijieOspfIfMd5AuthKeyTable = _RuijieOspfIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieOspfIfMd5AuthKeyTable.setStatus("current")
_RuijieOspfIfMd5AuthKeyEntry_Object = MibTableRow
ruijieOspfIfMd5AuthKeyEntry = _RuijieOspfIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 5, 1)
)
ruijieOspfIfMd5AuthKeyEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfIfMd5AuthKeyIf"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    ruijieOspfIfMd5AuthKeyEntry.setStatus("current")
_RuijieOspfIfMd5AuthKeyIf_Type = Unsigned32
_RuijieOspfIfMd5AuthKeyIf_Object = MibTableColumn
ruijieOspfIfMd5AuthKeyIf = _RuijieOspfIfMd5AuthKeyIf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 5, 1, 1),
    _RuijieOspfIfMd5AuthKeyIf_Type()
)
ruijieOspfIfMd5AuthKeyIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfMd5AuthKeyIf.setStatus("current")


class _RuijieOspfIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type ruijieOspfIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieOspfIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_RuijieOspfIfMd5AuthKeyId_Object = MibTableColumn
ruijieOspfIfMd5AuthKeyId = _RuijieOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 5, 1, 2),
    _RuijieOspfIfMd5AuthKeyId_Type()
)
ruijieOspfIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfIfMd5AuthKeyId.setStatus("current")


class _RuijieOspfIfMd5AuthKey_Type(OctetString):
    """Custom type ruijieOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_RuijieOspfIfMd5AuthKey_Object = MibTableColumn
ruijieOspfIfMd5AuthKey = _RuijieOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 5, 1, 3),
    _RuijieOspfIfMd5AuthKey_Type()
)
ruijieOspfIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfIfMd5AuthKey.setStatus("current")
_RuijieOspfIfMd5AuthKeySt_Type = ConfigStatus
_RuijieOspfIfMd5AuthKeySt_Object = MibTableColumn
ruijieOspfIfMd5AuthKeySt = _RuijieOspfIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 5, 1, 4),
    _RuijieOspfIfMd5AuthKeySt_Type()
)
ruijieOspfIfMd5AuthKeySt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfIfMd5AuthKeySt.setStatus("current")
_RuijieOspfVirtTable_Object = MibTable
ruijieOspfVirtTable = _RuijieOspfVirtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieOspfVirtTable.setStatus("current")
_RuijieOspfVirtEntry_Object = MibTableRow
ruijieOspfVirtEntry = _RuijieOspfVirtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1)
)
ruijieOspfVirtEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfVirtIfAreaId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    ruijieOspfVirtEntry.setStatus("current")
_RuijieOspfVirtIfAreaId_Type = AreaID
_RuijieOspfVirtIfAreaId_Object = MibTableColumn
ruijieOspfVirtIfAreaId = _RuijieOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 1),
    _RuijieOspfVirtIfAreaId_Type()
)
ruijieOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfAreaId.setStatus("current")
_RuijieOspfVirtIfNeighbor_Type = RouterID
_RuijieOspfVirtIfNeighbor_Object = MibTableColumn
ruijieOspfVirtIfNeighbor = _RuijieOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 2),
    _RuijieOspfVirtIfNeighbor_Type()
)
ruijieOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfNeighbor.setStatus("current")


class _RuijieOspfVirtIfTransitDelay_Type(Unsigned32):
    """Custom type ruijieOspfVirtIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieOspfVirtIfTransitDelay_Type.__name__ = "Unsigned32"
_RuijieOspfVirtIfTransitDelay_Object = MibTableColumn
ruijieOspfVirtIfTransitDelay = _RuijieOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 3),
    _RuijieOspfVirtIfTransitDelay_Type()
)
ruijieOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfTransitDelay.setStatus("current")


class _RuijieOspfVirtIfRetransInterval_Type(Unsigned32):
    """Custom type ruijieOspfVirtIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieOspfVirtIfRetransInterval_Type.__name__ = "Unsigned32"
_RuijieOspfVirtIfRetransInterval_Object = MibTableColumn
ruijieOspfVirtIfRetransInterval = _RuijieOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 4),
    _RuijieOspfVirtIfRetransInterval_Type()
)
ruijieOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfRetransInterval.setStatus("current")


class _RuijieOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type ruijieOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RuijieOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_RuijieOspfVirtIfHelloInterval_Object = MibTableColumn
ruijieOspfVirtIfHelloInterval = _RuijieOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 5),
    _RuijieOspfVirtIfHelloInterval_Type()
)
ruijieOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfHelloInterval.setStatus("current")


class _RuijieOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ruijieOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_RuijieOspfVirtIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_RuijieOspfVirtIfRtrDeadInterval_Object = MibTableColumn
ruijieOspfVirtIfRtrDeadInterval = _RuijieOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 6),
    _RuijieOspfVirtIfRtrDeadInterval_Type()
)
ruijieOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfRtrDeadInterval.setStatus("current")


class _RuijieOspfVirtIfState_Type(Integer32):
    """Custom type ruijieOspfVirtIfState based on Integer32"""
    defaultValue = 1

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


_RuijieOspfVirtIfState_Type.__name__ = "Integer32"
_RuijieOspfVirtIfState_Object = MibTableColumn
ruijieOspfVirtIfState = _RuijieOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 7),
    _RuijieOspfVirtIfState_Type()
)
ruijieOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfState.setStatus("current")
_RuijieOspfVirtIfEvents_Type = Counter32
_RuijieOspfVirtIfEvents_Object = MibTableColumn
ruijieOspfVirtIfEvents = _RuijieOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 8),
    _RuijieOspfVirtIfEvents_Type()
)
ruijieOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfEvents.setStatus("current")


class _RuijieOspfVirtIfAuthKey_Type(OctetString):
    """Custom type ruijieOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_RuijieOspfVirtIfAuthKey_Object = MibTableColumn
ruijieOspfVirtIfAuthKey = _RuijieOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 9),
    _RuijieOspfVirtIfAuthKey_Type()
)
ruijieOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfAuthKey.setStatus("current")
_RuijieOspfVirtIfStatus_Type = RowStatus
_RuijieOspfVirtIfStatus_Object = MibTableColumn
ruijieOspfVirtIfStatus = _RuijieOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 10),
    _RuijieOspfVirtIfStatus_Type()
)
ruijieOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfStatus.setStatus("current")


class _RuijieOspfVirtIfAuthType_Type(Integer32):
    """Custom type ruijieOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieOspfVirtIfAuthType_Type.__name__ = "Integer32"
_RuijieOspfVirtIfAuthType_Object = MibTableColumn
ruijieOspfVirtIfAuthType = _RuijieOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 11),
    _RuijieOspfVirtIfAuthType_Type()
)
ruijieOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfAuthType.setStatus("current")
_RuijieOspfVirtCost_Type = Unsigned32
_RuijieOspfVirtCost_Object = MibTableColumn
ruijieOspfVirtCost = _RuijieOspfVirtCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 12),
    _RuijieOspfVirtCost_Type()
)
ruijieOspfVirtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtCost.setStatus("current")
_RuijieOspfVirtNativeIfIndex_Type = Integer32
_RuijieOspfVirtNativeIfIndex_Object = MibTableColumn
ruijieOspfVirtNativeIfIndex = _RuijieOspfVirtNativeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 13),
    _RuijieOspfVirtNativeIfIndex_Type()
)
ruijieOspfVirtNativeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtNativeIfIndex.setStatus("current")


class _RuijieOspfVirtLinkState_Type(Integer32):
    """Custom type ruijieOspfVirtLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RuijieOspfVirtLinkState_Type.__name__ = "Integer32"
_RuijieOspfVirtLinkState_Object = MibTableColumn
ruijieOspfVirtLinkState = _RuijieOspfVirtLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 14),
    _RuijieOspfVirtLinkState_Type()
)
ruijieOspfVirtLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtLinkState.setStatus("current")
_RuijieOspfVirtHelloDueIn_Type = TimeTicks
_RuijieOspfVirtHelloDueIn_Object = MibTableColumn
ruijieOspfVirtHelloDueIn = _RuijieOspfVirtHelloDueIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 15),
    _RuijieOspfVirtHelloDueIn_Type()
)
ruijieOspfVirtHelloDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtHelloDueIn.setStatus("current")


class _RuijieOspfVirtCurrentUsedMd5AuthKeyId_Type(Unsigned32):
    """Custom type ruijieOspfVirtCurrentUsedMd5AuthKeyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieOspfVirtCurrentUsedMd5AuthKeyId_Type.__name__ = "Unsigned32"
_RuijieOspfVirtCurrentUsedMd5AuthKeyId_Object = MibTableColumn
ruijieOspfVirtCurrentUsedMd5AuthKeyId = _RuijieOspfVirtCurrentUsedMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 6, 1, 16),
    _RuijieOspfVirtCurrentUsedMd5AuthKeyId_Type()
)
ruijieOspfVirtCurrentUsedMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtCurrentUsedMd5AuthKeyId.setStatus("current")
_RuijieOspfVirtIfMd5AuthKeyTable_Object = MibTable
ruijieOspfVirtIfMd5AuthKeyTable = _RuijieOspfVirtIfMd5AuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKeyTable.setStatus("current")
_RuijieOspfVirtIfMd5AuthKeyEntry_Object = MibTableRow
ruijieOspfVirtIfMd5AuthKeyEntry = _RuijieOspfVirtIfMd5AuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7, 1)
)
ruijieOspfVirtIfMd5AuthKeyEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeyAreaId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeyNeighbor"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKeyEntry.setStatus("current")
_RuijieOspfVirtIfMd5AuthKeyAreaId_Type = AreaID
_RuijieOspfVirtIfMd5AuthKeyAreaId_Object = MibTableColumn
ruijieOspfVirtIfMd5AuthKeyAreaId = _RuijieOspfVirtIfMd5AuthKeyAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7, 1, 1),
    _RuijieOspfVirtIfMd5AuthKeyAreaId_Type()
)
ruijieOspfVirtIfMd5AuthKeyAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKeyAreaId.setStatus("current")
_RuijieOspfVirtIfMd5AuthKeyNeighbor_Type = RouterID
_RuijieOspfVirtIfMd5AuthKeyNeighbor_Object = MibTableColumn
ruijieOspfVirtIfMd5AuthKeyNeighbor = _RuijieOspfVirtIfMd5AuthKeyNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7, 1, 2),
    _RuijieOspfVirtIfMd5AuthKeyNeighbor_Type()
)
ruijieOspfVirtIfMd5AuthKeyNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKeyNeighbor.setStatus("current")


class _RuijieOspfVirtIfMd5AuthKeyId_Type(Unsigned32):
    """Custom type ruijieOspfVirtIfMd5AuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieOspfVirtIfMd5AuthKeyId_Type.__name__ = "Unsigned32"
_RuijieOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
ruijieOspfVirtIfMd5AuthKeyId = _RuijieOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7, 1, 3),
    _RuijieOspfVirtIfMd5AuthKeyId_Type()
)
ruijieOspfVirtIfMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKeyId.setStatus("current")


class _RuijieOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type ruijieOspfVirtIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RuijieOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_RuijieOspfVirtIfMd5AuthKey_Object = MibTableColumn
ruijieOspfVirtIfMd5AuthKey = _RuijieOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7, 1, 4),
    _RuijieOspfVirtIfMd5AuthKey_Type()
)
ruijieOspfVirtIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKey.setStatus("current")
_RuijieOspfVirtIfMd5AuthKeySt_Type = ConfigStatus
_RuijieOspfVirtIfMd5AuthKeySt_Object = MibTableColumn
ruijieOspfVirtIfMd5AuthKeySt = _RuijieOspfVirtIfMd5AuthKeySt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 7, 1, 5),
    _RuijieOspfVirtIfMd5AuthKeySt_Type()
)
ruijieOspfVirtIfMd5AuthKeySt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieOspfVirtIfMd5AuthKeySt.setStatus("current")
_RuijieOspfLsaDetailInfoMibsGroup_ObjectIdentity = ObjectIdentity
ruijieOspfLsaDetailInfoMibsGroup = _RuijieOspfLsaDetailInfoMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8)
)
_RuijieOspfLsdbTable_Object = MibTable
ruijieOspfLsdbTable = _RuijieOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ruijieOspfLsdbTable.setStatus("current")
_RuijieOspfLsdbEntry_Object = MibTableRow
ruijieOspfLsdbEntry = _RuijieOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1)
)
ruijieOspfLsdbEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbAreaId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbType"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbLsid"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ruijieOspfLsdbEntry.setStatus("current")
_RuijieOspfLsdbAreaId_Type = AreaID
_RuijieOspfLsdbAreaId_Object = MibTableColumn
ruijieOspfLsdbAreaId = _RuijieOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 1),
    _RuijieOspfLsdbAreaId_Type()
)
ruijieOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbAreaId.setStatus("current")


class _RuijieOspfLsdbType_Type(Integer32):
    """Custom type ruijieOspfLsdbType based on Integer32"""
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
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7))
    )


_RuijieOspfLsdbType_Type.__name__ = "Integer32"
_RuijieOspfLsdbType_Object = MibTableColumn
ruijieOspfLsdbType = _RuijieOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 2),
    _RuijieOspfLsdbType_Type()
)
ruijieOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbType.setStatus("current")
_RuijieOspfLsdbLsid_Type = IpAddress
_RuijieOspfLsdbLsid_Object = MibTableColumn
ruijieOspfLsdbLsid = _RuijieOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 3),
    _RuijieOspfLsdbLsid_Type()
)
ruijieOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbLsid.setStatus("current")
_RuijieOspfLsdbRouterId_Type = RouterID
_RuijieOspfLsdbRouterId_Object = MibTableColumn
ruijieOspfLsdbRouterId = _RuijieOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 4),
    _RuijieOspfLsdbRouterId_Type()
)
ruijieOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbRouterId.setStatus("current")
_RuijieOspfLsdbSequence_Type = Unsigned32
_RuijieOspfLsdbSequence_Object = MibTableColumn
ruijieOspfLsdbSequence = _RuijieOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 5),
    _RuijieOspfLsdbSequence_Type()
)
ruijieOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbSequence.setStatus("current")
_RuijieOspfLsdbAge_Type = Unsigned32
_RuijieOspfLsdbAge_Object = MibTableColumn
ruijieOspfLsdbAge = _RuijieOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 6),
    _RuijieOspfLsdbAge_Type()
)
ruijieOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbAge.setStatus("current")
_RuijieOspfLsdbChecksum_Type = Unsigned32
_RuijieOspfLsdbChecksum_Object = MibTableColumn
ruijieOspfLsdbChecksum = _RuijieOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 7),
    _RuijieOspfLsdbChecksum_Type()
)
ruijieOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbChecksum.setStatus("current")


class _RuijieOspfLsdbAdvertisement_Type(OctetString):
    """Custom type ruijieOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_RuijieOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_RuijieOspfLsdbAdvertisement_Object = MibTableColumn
ruijieOspfLsdbAdvertisement = _RuijieOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 8),
    _RuijieOspfLsdbAdvertisement_Type()
)
ruijieOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbAdvertisement.setStatus("current")


class _RuijieOspfLsdbLinkNum_Type(Unsigned32):
    """Custom type ruijieOspfLsdbLinkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RuijieOspfLsdbLinkNum_Type.__name__ = "Unsigned32"
_RuijieOspfLsdbLinkNum_Object = MibTableColumn
ruijieOspfLsdbLinkNum = _RuijieOspfLsdbLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 9),
    _RuijieOspfLsdbLinkNum_Type()
)
ruijieOspfLsdbLinkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbLinkNum.setStatus("current")


class _RuijieOspfLsdbPacketLength_Type(Unsigned32):
    """Custom type ruijieOspfLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieOspfLsdbPacketLength_Type.__name__ = "Unsigned32"
_RuijieOspfLsdbPacketLength_Object = MibTableColumn
ruijieOspfLsdbPacketLength = _RuijieOspfLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 10),
    _RuijieOspfLsdbPacketLength_Type()
)
ruijieOspfLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbPacketLength.setStatus("current")
_RuijieOspfSummaryLsaNetworkMask_Type = IpAddress
_RuijieOspfSummaryLsaNetworkMask_Object = MibTableColumn
ruijieOspfSummaryLsaNetworkMask = _RuijieOspfSummaryLsaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 11),
    _RuijieOspfSummaryLsaNetworkMask_Type()
)
ruijieOspfSummaryLsaNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfSummaryLsaNetworkMask.setStatus("current")


class _RuijieOspfSummaryLsaTos0Metric_Type(Unsigned32):
    """Custom type ruijieOspfSummaryLsaTos0Metric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieOspfSummaryLsaTos0Metric_Type.__name__ = "Unsigned32"
_RuijieOspfSummaryLsaTos0Metric_Object = MibTableColumn
ruijieOspfSummaryLsaTos0Metric = _RuijieOspfSummaryLsaTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 12),
    _RuijieOspfSummaryLsaTos0Metric_Type()
)
ruijieOspfSummaryLsaTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfSummaryLsaTos0Metric.setStatus("current")


class _RuijieOspfNssaLsaDetailMetricType_Type(Integer32):
    """Custom type ruijieOspfNssaLsaDetailMetricType based on Integer32"""
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


_RuijieOspfNssaLsaDetailMetricType_Type.__name__ = "Integer32"
_RuijieOspfNssaLsaDetailMetricType_Object = MibTableColumn
ruijieOspfNssaLsaDetailMetricType = _RuijieOspfNssaLsaDetailMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 13),
    _RuijieOspfNssaLsaDetailMetricType_Type()
)
ruijieOspfNssaLsaDetailMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNssaLsaDetailMetricType.setStatus("current")
_RuijieOspfNssaLsaDetailForwardAddr_Type = IpAddress
_RuijieOspfNssaLsaDetailForwardAddr_Object = MibTableColumn
ruijieOspfNssaLsaDetailForwardAddr = _RuijieOspfNssaLsaDetailForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 14),
    _RuijieOspfNssaLsaDetailForwardAddr_Type()
)
ruijieOspfNssaLsaDetailForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNssaLsaDetailForwardAddr.setStatus("current")
_RuijieOspfNssaLsaDetailRouteTag_Type = Unsigned32
_RuijieOspfNssaLsaDetailRouteTag_Object = MibTableColumn
ruijieOspfNssaLsaDetailRouteTag = _RuijieOspfNssaLsaDetailRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 15),
    _RuijieOspfNssaLsaDetailRouteTag_Type()
)
ruijieOspfNssaLsaDetailRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNssaLsaDetailRouteTag.setStatus("current")
_RuijieOspfLsdbOption_Type = Unsigned32
_RuijieOspfLsdbOption_Object = MibTableColumn
ruijieOspfLsdbOption = _RuijieOspfLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 1, 1, 16),
    _RuijieOspfLsdbOption_Type()
)
ruijieOspfLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsdbOption.setStatus("current")
_RuijieOspfExtLsdbTable_Object = MibTable
ruijieOspfExtLsdbTable = _RuijieOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbTable.setStatus("current")
_RuijieOspfExtLsdbEntry_Object = MibTableRow
ruijieOspfExtLsdbEntry = _RuijieOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1)
)
ruijieOspfExtLsdbEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbType"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbLsid"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbEntry.setStatus("current")


class _RuijieOspfExtLsdbType_Type(Integer32):
    """Custom type ruijieOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_RuijieOspfExtLsdbType_Type.__name__ = "Integer32"
_RuijieOspfExtLsdbType_Object = MibTableColumn
ruijieOspfExtLsdbType = _RuijieOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 1),
    _RuijieOspfExtLsdbType_Type()
)
ruijieOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbType.setStatus("current")
_RuijieOspfExtLsdbLsid_Type = IpAddress
_RuijieOspfExtLsdbLsid_Object = MibTableColumn
ruijieOspfExtLsdbLsid = _RuijieOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 2),
    _RuijieOspfExtLsdbLsid_Type()
)
ruijieOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbLsid.setStatus("current")
_RuijieOspfExtLsdbRouterId_Type = RouterID
_RuijieOspfExtLsdbRouterId_Object = MibTableColumn
ruijieOspfExtLsdbRouterId = _RuijieOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 3),
    _RuijieOspfExtLsdbRouterId_Type()
)
ruijieOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbRouterId.setStatus("current")
_RuijieOspfExtLsdbSequence_Type = Unsigned32
_RuijieOspfExtLsdbSequence_Object = MibTableColumn
ruijieOspfExtLsdbSequence = _RuijieOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 4),
    _RuijieOspfExtLsdbSequence_Type()
)
ruijieOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbSequence.setStatus("current")
_RuijieOspfExtLsdbAge_Type = Unsigned32
_RuijieOspfExtLsdbAge_Object = MibTableColumn
ruijieOspfExtLsdbAge = _RuijieOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 5),
    _RuijieOspfExtLsdbAge_Type()
)
ruijieOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbAge.setStatus("current")
_RuijieOspfExtLsdbChecksum_Type = Unsigned32
_RuijieOspfExtLsdbChecksum_Object = MibTableColumn
ruijieOspfExtLsdbChecksum = _RuijieOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 6),
    _RuijieOspfExtLsdbChecksum_Type()
)
ruijieOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbChecksum.setStatus("current")


class _RuijieOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type ruijieOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_RuijieOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_RuijieOspfExtLsdbAdvertisement_Object = MibTableColumn
ruijieOspfExtLsdbAdvertisement = _RuijieOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 7),
    _RuijieOspfExtLsdbAdvertisement_Type()
)
ruijieOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbAdvertisement.setStatus("current")
_RuijieOspfExtLsdbNetworkMask_Type = IpAddress
_RuijieOspfExtLsdbNetworkMask_Object = MibTableColumn
ruijieOspfExtLsdbNetworkMask = _RuijieOspfExtLsdbNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 8),
    _RuijieOspfExtLsdbNetworkMask_Type()
)
ruijieOspfExtLsdbNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbNetworkMask.setStatus("current")
_RuijieOspfExtLsdbMetric_Type = Integer32
_RuijieOspfExtLsdbMetric_Object = MibTableColumn
ruijieOspfExtLsdbMetric = _RuijieOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 9),
    _RuijieOspfExtLsdbMetric_Type()
)
ruijieOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbMetric.setStatus("current")


class _RuijieOspfExtLsdbMetricType_Type(Integer32):
    """Custom type ruijieOspfExtLsdbMetricType based on Integer32"""
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


_RuijieOspfExtLsdbMetricType_Type.__name__ = "Integer32"
_RuijieOspfExtLsdbMetricType_Object = MibTableColumn
ruijieOspfExtLsdbMetricType = _RuijieOspfExtLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 10),
    _RuijieOspfExtLsdbMetricType_Type()
)
ruijieOspfExtLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbMetricType.setStatus("current")
_RuijieOspfExtLsdbForwardAddr_Type = IpAddress
_RuijieOspfExtLsdbForwardAddr_Object = MibTableColumn
ruijieOspfExtLsdbForwardAddr = _RuijieOspfExtLsdbForwardAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 11),
    _RuijieOspfExtLsdbForwardAddr_Type()
)
ruijieOspfExtLsdbForwardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbForwardAddr.setStatus("current")
_RuijieOspfExtLsdbRouteTag_Type = Unsigned32
_RuijieOspfExtLsdbRouteTag_Object = MibTableColumn
ruijieOspfExtLsdbRouteTag = _RuijieOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 12),
    _RuijieOspfExtLsdbRouteTag_Type()
)
ruijieOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbRouteTag.setStatus("current")
_RuijieOspfExtLsdbOption_Type = Unsigned32
_RuijieOspfExtLsdbOption_Object = MibTableColumn
ruijieOspfExtLsdbOption = _RuijieOspfExtLsdbOption_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 13),
    _RuijieOspfExtLsdbOption_Type()
)
ruijieOspfExtLsdbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbOption.setStatus("current")


class _RuijieOspfExtLsdbPacketLength_Type(Unsigned32):
    """Custom type ruijieOspfExtLsdbPacketLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieOspfExtLsdbPacketLength_Type.__name__ = "Unsigned32"
_RuijieOspfExtLsdbPacketLength_Object = MibTableColumn
ruijieOspfExtLsdbPacketLength = _RuijieOspfExtLsdbPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 2, 1, 14),
    _RuijieOspfExtLsdbPacketLength_Type()
)
ruijieOspfExtLsdbPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfExtLsdbPacketLength.setStatus("current")
_RuijieOspfRouterLsaDetailTable_Object = MibTable
ruijieOspfRouterLsaDetailTable = _RuijieOspfRouterLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ruijieOspfRouterLsaDetailTable.setStatus("current")
_RuijieOspfRouterLsaDetailEntry_Object = MibTableRow
ruijieOspfRouterLsaDetailEntry = _RuijieOspfRouterLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 3, 1)
)
ruijieOspfRouterLsaDetailEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbAreaId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbType"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbLsid"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbRouterId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfRouterLsaDetailLinkID"),
)
if mibBuilder.loadTexts:
    ruijieOspfRouterLsaDetailEntry.setStatus("current")
_RuijieOspfRouterLsaDetailLinkID_Type = IpAddress
_RuijieOspfRouterLsaDetailLinkID_Object = MibTableColumn
ruijieOspfRouterLsaDetailLinkID = _RuijieOspfRouterLsaDetailLinkID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 3, 1, 1),
    _RuijieOspfRouterLsaDetailLinkID_Type()
)
ruijieOspfRouterLsaDetailLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouterLsaDetailLinkID.setStatus("current")


class _RuijieOspfRouterLsaDetailLinkType_Type(Integer32):
    """Custom type ruijieOspfRouterLsaDetailLinkType based on Integer32"""
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
        *(("pointtopointConnectionToAnotherRouter", 1),
          ("connectionToaTransitNetwork", 2),
          ("connectionToaStubNetwork", 3),
          ("virtualLink", 4))
    )


_RuijieOspfRouterLsaDetailLinkType_Type.__name__ = "Integer32"
_RuijieOspfRouterLsaDetailLinkType_Object = MibTableColumn
ruijieOspfRouterLsaDetailLinkType = _RuijieOspfRouterLsaDetailLinkType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 3, 1, 2),
    _RuijieOspfRouterLsaDetailLinkType_Type()
)
ruijieOspfRouterLsaDetailLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouterLsaDetailLinkType.setStatus("current")
_RuijieOspfRouterLsaDetailLinkData_Type = IpAddress
_RuijieOspfRouterLsaDetailLinkData_Object = MibTableColumn
ruijieOspfRouterLsaDetailLinkData = _RuijieOspfRouterLsaDetailLinkData_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 3, 1, 3),
    _RuijieOspfRouterLsaDetailLinkData_Type()
)
ruijieOspfRouterLsaDetailLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouterLsaDetailLinkData.setStatus("current")
_RuijieOspfRouterLsaDetailTos0Metric_Type = Unsigned32
_RuijieOspfRouterLsaDetailTos0Metric_Object = MibTableColumn
ruijieOspfRouterLsaDetailTos0Metric = _RuijieOspfRouterLsaDetailTos0Metric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 3, 1, 4),
    _RuijieOspfRouterLsaDetailTos0Metric_Type()
)
ruijieOspfRouterLsaDetailTos0Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouterLsaDetailTos0Metric.setStatus("current")
_RuijieOspfNetWorkLsaDetailTable_Object = MibTable
ruijieOspfNetWorkLsaDetailTable = _RuijieOspfNetWorkLsaDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ruijieOspfNetWorkLsaDetailTable.setStatus("current")
_RuijieOspfNetWorkLsaDetailEntry_Object = MibTableRow
ruijieOspfNetWorkLsaDetailEntry = _RuijieOspfNetWorkLsaDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 4, 1)
)
ruijieOspfNetWorkLsaDetailEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbAreaId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbType"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbLsid"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsdbRouterId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfNetWorkLsaDetailAttachedRouter"),
)
if mibBuilder.loadTexts:
    ruijieOspfNetWorkLsaDetailEntry.setStatus("current")
_RuijieOspfNetWorkLsaDetailAttachedRouter_Type = IpAddress
_RuijieOspfNetWorkLsaDetailAttachedRouter_Object = MibTableColumn
ruijieOspfNetWorkLsaDetailAttachedRouter = _RuijieOspfNetWorkLsaDetailAttachedRouter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 4, 1, 1),
    _RuijieOspfNetWorkLsaDetailAttachedRouter_Type()
)
ruijieOspfNetWorkLsaDetailAttachedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNetWorkLsaDetailAttachedRouter.setStatus("current")
_RuijieOspfNetWorkLsaDetailNetworkMask_Type = IpAddress
_RuijieOspfNetWorkLsaDetailNetworkMask_Object = MibTableColumn
ruijieOspfNetWorkLsaDetailNetworkMask = _RuijieOspfNetWorkLsaDetailNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 4, 1, 2),
    _RuijieOspfNetWorkLsaDetailNetworkMask_Type()
)
ruijieOspfNetWorkLsaDetailNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNetWorkLsaDetailNetworkMask.setStatus("current")
_RuijieOspfAreaLsaDBSumTable_Object = MibTable
ruijieOspfAreaLsaDBSumTable = _RuijieOspfAreaLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5)
)
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumTable.setStatus("current")
_RuijieOspfAreaLsaDBSumEntry_Object = MibTableRow
ruijieOspfAreaLsaDBSumEntry = _RuijieOspfAreaLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5, 1)
)
ruijieOspfAreaLsaDBSumEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumAreaId"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumEntry.setStatus("current")
_RuijieOspfAreaLsaDBSumAreaId_Type = IpAddress
_RuijieOspfAreaLsaDBSumAreaId_Object = MibTableColumn
ruijieOspfAreaLsaDBSumAreaId = _RuijieOspfAreaLsaDBSumAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5, 1, 1),
    _RuijieOspfAreaLsaDBSumAreaId_Type()
)
ruijieOspfAreaLsaDBSumAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumAreaId.setStatus("current")


class _RuijieOspfAreaLsaDBSumLsaType_Type(Integer32):
    """Custom type ruijieOspfAreaLsaDBSumLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("nssaExternalLink", 7),
          ("subtotal", 8))
    )


_RuijieOspfAreaLsaDBSumLsaType_Type.__name__ = "Integer32"
_RuijieOspfAreaLsaDBSumLsaType_Object = MibTableColumn
ruijieOspfAreaLsaDBSumLsaType = _RuijieOspfAreaLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5, 1, 2),
    _RuijieOspfAreaLsaDBSumLsaType_Type()
)
ruijieOspfAreaLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumLsaType.setStatus("current")
_RuijieOspfAreaLsaDBSumCounts_Type = Counter32
_RuijieOspfAreaLsaDBSumCounts_Object = MibTableColumn
ruijieOspfAreaLsaDBSumCounts = _RuijieOspfAreaLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5, 1, 3),
    _RuijieOspfAreaLsaDBSumCounts_Type()
)
ruijieOspfAreaLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumCounts.setStatus("current")
_RuijieOspfAreaLsaDBSumDeletes_Type = Counter32
_RuijieOspfAreaLsaDBSumDeletes_Object = MibTableColumn
ruijieOspfAreaLsaDBSumDeletes = _RuijieOspfAreaLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5, 1, 4),
    _RuijieOspfAreaLsaDBSumDeletes_Type()
)
ruijieOspfAreaLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumDeletes.setStatus("current")
_RuijieOspfAreaLsaDBSumMaxage_Type = Counter32
_RuijieOspfAreaLsaDBSumMaxage_Object = MibTableColumn
ruijieOspfAreaLsaDBSumMaxage = _RuijieOspfAreaLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 5, 1, 5),
    _RuijieOspfAreaLsaDBSumMaxage_Type()
)
ruijieOspfAreaLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfAreaLsaDBSumMaxage.setStatus("current")
_RuijieOspfLsaDBSumTable_Object = MibTable
ruijieOspfLsaDBSumTable = _RuijieOspfLsaDBSumTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 6)
)
if mibBuilder.loadTexts:
    ruijieOspfLsaDBSumTable.setStatus("current")
_RuijieOspfLsaDBSumEntry_Object = MibTableRow
ruijieOspfLsaDBSumEntry = _RuijieOspfLsaDBSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 6, 1)
)
ruijieOspfLsaDBSumEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfLsaDBSumLsaType"),
)
if mibBuilder.loadTexts:
    ruijieOspfLsaDBSumEntry.setStatus("current")


class _RuijieOspfLsaDBSumLsaType_Type(Integer32):
    """Custom type ruijieOspfLsaDBSumLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryTotalLink", 3),
          ("asSummaryTotalLink", 4),
          ("asExternalLink", 5),
          ("nssaExternalLink", 7),
          ("total", 8))
    )


_RuijieOspfLsaDBSumLsaType_Type.__name__ = "Integer32"
_RuijieOspfLsaDBSumLsaType_Object = MibTableColumn
ruijieOspfLsaDBSumLsaType = _RuijieOspfLsaDBSumLsaType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 6, 1, 1),
    _RuijieOspfLsaDBSumLsaType_Type()
)
ruijieOspfLsaDBSumLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsaDBSumLsaType.setStatus("current")
_RuijieOspfLsaDBSumCounts_Type = Counter32
_RuijieOspfLsaDBSumCounts_Object = MibTableColumn
ruijieOspfLsaDBSumCounts = _RuijieOspfLsaDBSumCounts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 6, 1, 2),
    _RuijieOspfLsaDBSumCounts_Type()
)
ruijieOspfLsaDBSumCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsaDBSumCounts.setStatus("current")
_RuijieOspfLsaDBSumDeletes_Type = Counter32
_RuijieOspfLsaDBSumDeletes_Object = MibTableColumn
ruijieOspfLsaDBSumDeletes = _RuijieOspfLsaDBSumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 6, 1, 3),
    _RuijieOspfLsaDBSumDeletes_Type()
)
ruijieOspfLsaDBSumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsaDBSumDeletes.setStatus("current")
_RuijieOspfLsaDBSumMaxage_Type = Counter32
_RuijieOspfLsaDBSumMaxage_Object = MibTableColumn
ruijieOspfLsaDBSumMaxage = _RuijieOspfLsaDBSumMaxage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 8, 6, 1, 4),
    _RuijieOspfLsaDBSumMaxage_Type()
)
ruijieOspfLsaDBSumMaxage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfLsaDBSumMaxage.setStatus("current")
_RuijieOspfNeighborTable_Object = MibTable
ruijieOspfNeighborTable = _RuijieOspfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieOspfNeighborTable.setStatus("current")
_RuijieOspfNeighborEntry_Object = MibTableRow
ruijieOspfNeighborEntry = _RuijieOspfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1)
)
ruijieOspfNeighborEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfNbrIpAddr"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    ruijieOspfNeighborEntry.setStatus("current")
_RuijieOspfNbrIpAddr_Type = IpAddress
_RuijieOspfNbrIpAddr_Object = MibTableColumn
ruijieOspfNbrIpAddr = _RuijieOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 1),
    _RuijieOspfNbrIpAddr_Type()
)
ruijieOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrIpAddr.setStatus("current")
_RuijieOspfNbrAddressLessIndex_Type = Unsigned32
_RuijieOspfNbrAddressLessIndex_Object = MibTableColumn
ruijieOspfNbrAddressLessIndex = _RuijieOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 2),
    _RuijieOspfNbrAddressLessIndex_Type()
)
ruijieOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrAddressLessIndex.setStatus("current")
_RuijieOspfNbrRtrId_Type = RouterID
_RuijieOspfNbrRtrId_Object = MibTableColumn
ruijieOspfNbrRtrId = _RuijieOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 3),
    _RuijieOspfNbrRtrId_Type()
)
ruijieOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrRtrId.setStatus("current")
_RuijieOspfNbrOptions_Type = Unsigned32
_RuijieOspfNbrOptions_Object = MibTableColumn
ruijieOspfNbrOptions = _RuijieOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 4),
    _RuijieOspfNbrOptions_Type()
)
ruijieOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrOptions.setStatus("current")
_RuijieOspfNbrPriority_Type = DesignatedRouterPriority
_RuijieOspfNbrPriority_Object = MibTableColumn
ruijieOspfNbrPriority = _RuijieOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 5),
    _RuijieOspfNbrPriority_Type()
)
ruijieOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrPriority.setStatus("current")


class _RuijieOspfNbrState_Type(Integer32):
    """Custom type ruijieOspfNbrState based on Integer32"""
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
          ("exchangeRuijie", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_RuijieOspfNbrState_Type.__name__ = "Integer32"
_RuijieOspfNbrState_Object = MibTableColumn
ruijieOspfNbrState = _RuijieOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 6),
    _RuijieOspfNbrState_Type()
)
ruijieOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrState.setStatus("current")
_RuijieOspfNbrEvents_Type = Counter32
_RuijieOspfNbrEvents_Object = MibTableColumn
ruijieOspfNbrEvents = _RuijieOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 7),
    _RuijieOspfNbrEvents_Type()
)
ruijieOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrEvents.setStatus("current")
_RuijieOspfNbrLsRetransQLen_Type = Gauge32
_RuijieOspfNbrLsRetransQLen_Object = MibTableColumn
ruijieOspfNbrLsRetransQLen = _RuijieOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 8),
    _RuijieOspfNbrLsRetransQLen_Type()
)
ruijieOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrLsRetransQLen.setStatus("current")
_RuijieOspfNbmaNbrStatus_Type = RowStatus
_RuijieOspfNbmaNbrStatus_Object = MibTableColumn
ruijieOspfNbmaNbrStatus = _RuijieOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 9),
    _RuijieOspfNbmaNbrStatus_Type()
)
ruijieOspfNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbmaNbrStatus.setStatus("current")


class _RuijieOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type ruijieOspfNbmaNbrPermanence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_RuijieOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_RuijieOspfNbmaNbrPermanence_Object = MibTableColumn
ruijieOspfNbmaNbrPermanence = _RuijieOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 10),
    _RuijieOspfNbmaNbrPermanence_Type()
)
ruijieOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbmaNbrPermanence.setStatus("current")
_RuijieOspfNbrHelloSuppressed_Type = TruthValue
_RuijieOspfNbrHelloSuppressed_Object = MibTableColumn
ruijieOspfNbrHelloSuppressed = _RuijieOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 11),
    _RuijieOspfNbrHelloSuppressed_Type()
)
ruijieOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrHelloSuppressed.setStatus("current")
_RuijieOspfNbrDeadTimeDueIn_Type = TimeTicks
_RuijieOspfNbrDeadTimeDueIn_Object = MibTableColumn
ruijieOspfNbrDeadTimeDueIn = _RuijieOspfNbrDeadTimeDueIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 12),
    _RuijieOspfNbrDeadTimeDueIn_Type()
)
ruijieOspfNbrDeadTimeDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrDeadTimeDueIn.setStatus("current")
_RuijieOspfNbrNeighborUpTime_Type = TimeTicks
_RuijieOspfNbrNeighborUpTime_Object = MibTableColumn
ruijieOspfNbrNeighborUpTime = _RuijieOspfNbrNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 13),
    _RuijieOspfNbrNeighborUpTime_Type()
)
ruijieOspfNbrNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrNeighborUpTime.setStatus("current")
_RuijieOspfNbrDR_Type = IpAddress
_RuijieOspfNbrDR_Object = MibTableColumn
ruijieOspfNbrDR = _RuijieOspfNbrDR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 14),
    _RuijieOspfNbrDR_Type()
)
ruijieOspfNbrDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrDR.setStatus("current")
_RuijieOspfNbrBDR_Type = IpAddress
_RuijieOspfNbrBDR_Object = MibTableColumn
ruijieOspfNbrBDR = _RuijieOspfNbrBDR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 15),
    _RuijieOspfNbrBDR_Type()
)
ruijieOspfNbrBDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrBDR.setStatus("current")
_RuijieOspfNbrArea_Type = IpAddress
_RuijieOspfNbrArea_Object = MibTableColumn
ruijieOspfNbrArea = _RuijieOspfNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 16),
    _RuijieOspfNbrArea_Type()
)
ruijieOspfNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrArea.setStatus("current")
_RuijieOspfNbrRetransmissionNum_Type = Counter32
_RuijieOspfNbrRetransmissionNum_Object = MibTableColumn
ruijieOspfNbrRetransmissionNum = _RuijieOspfNbrRetransmissionNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 17),
    _RuijieOspfNbrRetransmissionNum_Type()
)
ruijieOspfNbrRetransmissionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrRetransmissionNum.setStatus("current")


class _RuijieOspfNbrIfState_Type(Integer32):
    """Custom type ruijieOspfNbrIfState based on Integer32"""
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
        *(("other", 0),
          ("designatedRouter", 1),
          ("backupDesignatedRouter", 2),
          ("otherDesignatedRouter", 3))
    )


_RuijieOspfNbrIfState_Type.__name__ = "Integer32"
_RuijieOspfNbrIfState_Object = MibTableColumn
ruijieOspfNbrIfState = _RuijieOspfNbrIfState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 9, 1, 18),
    _RuijieOspfNbrIfState_Type()
)
ruijieOspfNbrIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfNbrIfState.setStatus("current")
_RuijieOspfRouteTable_Object = MibTable
ruijieOspfRouteTable = _RuijieOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieOspfRouteTable.setStatus("current")
_RuijieOspfRouteEntry_Object = MibTableRow
ruijieOspfRouteEntry = _RuijieOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1)
)
ruijieOspfRouteEntry.setIndexNames(
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfRouteDest"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfRouteArea"),
    (0, "RUIJIE-OSPF-MIB", "ruijieOspfRouteNextHop"),
)
if mibBuilder.loadTexts:
    ruijieOspfRouteEntry.setStatus("current")
_RuijieOspfRouteDest_Type = IpAddress
_RuijieOspfRouteDest_Object = MibTableColumn
ruijieOspfRouteDest = _RuijieOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 1),
    _RuijieOspfRouteDest_Type()
)
ruijieOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteDest.setStatus("current")
_RuijieOspfRouteArea_Type = IpAddress
_RuijieOspfRouteArea_Object = MibTableColumn
ruijieOspfRouteArea = _RuijieOspfRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 2),
    _RuijieOspfRouteArea_Type()
)
ruijieOspfRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteArea.setStatus("current")
_RuijieOspfRouteNextHop_Type = IpAddress
_RuijieOspfRouteNextHop_Object = MibTableColumn
ruijieOspfRouteNextHop = _RuijieOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 3),
    _RuijieOspfRouteNextHop_Type()
)
ruijieOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteNextHop.setStatus("current")
_RuijieOspfRouteCost_Type = Unsigned32
_RuijieOspfRouteCost_Object = MibTableColumn
ruijieOspfRouteCost = _RuijieOspfRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 4),
    _RuijieOspfRouteCost_Type()
)
ruijieOspfRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteCost.setStatus("current")


class _RuijieOspfRouteDRType_Type(Integer32):
    """Custom type ruijieOspfRouteDRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("asbr", 2),
          ("both", 3))
    )


_RuijieOspfRouteDRType_Type.__name__ = "Integer32"
_RuijieOspfRouteDRType_Object = MibTableColumn
ruijieOspfRouteDRType = _RuijieOspfRouteDRType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 5),
    _RuijieOspfRouteDRType_Type()
)
ruijieOspfRouteDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteDRType.setStatus("current")


class _RuijieOspfRouteType_Type(Integer32):
    """Custom type ruijieOspfRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intral-area-route", 1),
          ("inter-area-route", 2))
    )


_RuijieOspfRouteType_Type.__name__ = "Integer32"
_RuijieOspfRouteType_Object = MibTableColumn
ruijieOspfRouteType = _RuijieOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 6),
    _RuijieOspfRouteType_Type()
)
ruijieOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteType.setStatus("current")
_RuijieOspfRouteSpfNo_Type = Counter32
_RuijieOspfRouteSpfNo_Object = MibTableColumn
ruijieOspfRouteSpfNo = _RuijieOspfRouteSpfNo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 1, 10, 1, 7),
    _RuijieOspfRouteSpfNo_Type()
)
ruijieOspfRouteSpfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOspfRouteSpfNo.setStatus("current")
_RuijieOspfMIBConformance_ObjectIdentity = ObjectIdentity
ruijieOspfMIBConformance = _RuijieOspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2)
)
_RuijieOspfMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieOspfMIBCompliances = _RuijieOspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 1)
)
_RuijieOspfMIBGroups_ObjectIdentity = ObjectIdentity
ruijieOspfMIBGroups = _RuijieOspfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2)
)
_OspfMIBConformance_ObjectIdentity = ObjectIdentity
ospfMIBConformance = _OspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 3)
)
_OspfMIBCompliances_ObjectIdentity = ObjectIdentity
ospfMIBCompliances = _OspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 3, 1)
)

# Managed Objects groups

ruijieOspfBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 1)
)
ruijieOspfBaseMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfMiniLsaInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfMiniLsaArrival"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreasNum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNormalAreasNum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfStubAreasNum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNssaAreasNum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfSpfDelay"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfSpfHoldTime"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAutoCostRefBandWidthRef"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsaGroupPacing"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfInterDistance"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIntraDistance"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExternDistance"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLogAdjChangeNotify"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfPassiveStatus"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRFC1583Compatibility"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteRedisDefMetricVal"))
)
if mibBuilder.loadTexts:
    ruijieOspfBaseMIBGroup.setStatus("current")

ruijieOspfAreaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 2)
)
ruijieOspfAreaMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfAreaId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAuthType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfImportAsExtern"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfSpfRuns"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaBdrRtrCount"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAsBdrRtrCount"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaCount"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaCksumSum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaSummary"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaStatus"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaInterfaceNum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaNssaIsRedistribution"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaNssaIsDefInfoOriginate"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNetWorkAreaID"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNetWorkAddress"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNetWorkMask"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNetWorkStatus"))
)
if mibBuilder.loadTexts:
    ruijieOspfAreaMIBGroup.setStatus("current")

ruijieOspfLsaMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 3)
)
ruijieOspfLsaMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfLsdbAreaId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbLsid"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbRouterId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbSequence"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbAge"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbChecksum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbAdvertisement"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbLinkNum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbPacketLength"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfSummaryLsaNetworkMask"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfSummaryLsaTos0Metric"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNssaLsaDetailMetricType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNssaLsaDetailForwardAddr"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNssaLsaDetailRouteTag"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsdbOption"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbLsid"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbRouterId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbSequence"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbAge"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbChecksum"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbAdvertisement"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbNetworkMask"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbMetricType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbForwardAddr"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbRouteTag"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbMetric"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbOption"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfExtLsdbPacketLength"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouterLsaDetailLinkID"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouterLsaDetailLinkType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouterLsaDetailLinkData"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouterLsaDetailTos0Metric"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNetWorkLsaDetailAttachedRouter"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNetWorkLsaDetailNetworkMask"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumAreaId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumLsaType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumCounts"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumDeletes"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaLsaDBSumMaxage"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsaDBSumLsaType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsaDBSumCounts"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsaDBSumDeletes"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsaDBSumMaxage"))
)
if mibBuilder.loadTexts:
    ruijieOspfLsaMIBGroup.setStatus("current")

ruijieOspfIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 4)
)
ruijieOspfIfMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfIfIpAddress"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAddressLessIf"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfAreaId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfAdminStat"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfRtrPriority"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfTransitDelay"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfRetransInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfHelloInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfRtrDeadInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfPollInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfState"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfDesignatedRouter"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfBackupDesignatedRouter"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfEvents"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfAuthType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfAuthKey"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfStatus"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfMulticastForwarding"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfDemand"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfDatabaseFilterAllOut"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfDesignateRouterId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfBackupDesignateRouterId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfWaitInternal"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfPassiveStatus"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfCurrentUsedMd5AuthKeyId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfMd5AuthKeyIf"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfMd5AuthKeyId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfMd5AuthKey"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfMd5AuthKeySt"))
)
if mibBuilder.loadTexts:
    ruijieOspfIfMIBGroup.setStatus("current")

ruijieOspfVirtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 5)
)
ruijieOspfVirtMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfAreaId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfNeighbor"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfTransitDelay"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfRetransInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfHelloInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfRtrDeadInterval"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfState"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfEvents"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfAuthType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfAuthKey"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfStatus"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtCost"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtNativeIfIndex"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtLinkState"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtHelloDueIn"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeyAreaId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeyNeighbor"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeyId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKey"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtIfMd5AuthKeySt"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtCurrentUsedMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    ruijieOspfVirtMIBGroup.setStatus("current")

ruijieOspfNeighborMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 6)
)
ruijieOspfNeighborMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfNbrIpAddr"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrAddressLessIndex"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrRtrId"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrOptions"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrPriority"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrState"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrEvents"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrLsRetransQLen"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbmaNbrStatus"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbmaNbrPermanence"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrHelloSuppressed"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrDeadTimeDueIn"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrNeighborUpTime"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrDR"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrBDR"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrArea"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNbrRetransmissionNum"))
)
if mibBuilder.loadTexts:
    ruijieOspfNeighborMIBGroup.setStatus("current")

ruijieOspfRouteInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 2, 7)
)
ruijieOspfRouteInfoMIBGroup.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfRouteType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteDest"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteNextHop"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteCost"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteDRType"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteArea"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteSpfNo"))
)
if mibBuilder.loadTexts:
    ruijieOspfRouteInfoMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieOspfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 2, 1, 1)
)
ruijieOspfMIBCompliance.setObjects(
      *(("RUIJIE-OSPF-MIB", "ruijieOspfBaseMIBGroup"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfAreaMIBGroup"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfLsaMIBGroup"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfIfMIBGroup"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfVirtMIBGroup"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfNeighborMIBGroup"),
        ("RUIJIE-OSPF-MIB", "ruijieOspfRouteInfoMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieOspfMIBCompliance.setStatus(
        "current"
    )

ospfExternCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ospfExternCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-OSPF-MIB",
    **{"ruijieOspfMIB": ruijieOspfMIB,
       "ruijieOspfMIBObjects": ruijieOspfMIBObjects,
       "ruijieOspfGeneralMibsGroup": ruijieOspfGeneralMibsGroup,
       "ruijieOspfMiniLsaInterval": ruijieOspfMiniLsaInterval,
       "ruijieOspfMiniLsaArrival": ruijieOspfMiniLsaArrival,
       "ruijieOspfAreasNum": ruijieOspfAreasNum,
       "ruijieOspfNormalAreasNum": ruijieOspfNormalAreasNum,
       "ruijieOspfStubAreasNum": ruijieOspfStubAreasNum,
       "ruijieOspfNssaAreasNum": ruijieOspfNssaAreasNum,
       "ruijieOspfSpfDelay": ruijieOspfSpfDelay,
       "ruijieOspfSpfHoldTime": ruijieOspfSpfHoldTime,
       "ruijieOspfAutoCostRefBandWidthRef": ruijieOspfAutoCostRefBandWidthRef,
       "ruijieOspfLsaGroupPacing": ruijieOspfLsaGroupPacing,
       "ruijieOspfInterDistance": ruijieOspfInterDistance,
       "ruijieOspfIntraDistance": ruijieOspfIntraDistance,
       "ruijieOspfExternDistance": ruijieOspfExternDistance,
       "ruijieOspfLogAdjChangeNotify": ruijieOspfLogAdjChangeNotify,
       "ruijieOspfPassiveStatus": ruijieOspfPassiveStatus,
       "ruijieOspfRFC1583Compatibility": ruijieOspfRFC1583Compatibility,
       "ruijieOspfRouteRedisDefMetricVal": ruijieOspfRouteRedisDefMetricVal,
       "ruijieOspfAdminiDistance": ruijieOspfAdminiDistance,
       "ruijieOspfAreaTable": ruijieOspfAreaTable,
       "ruijieOspfAreaEntry": ruijieOspfAreaEntry,
       "ruijieOspfAreaId": ruijieOspfAreaId,
       "ruijieOspfAuthType": ruijieOspfAuthType,
       "ruijieOspfImportAsExtern": ruijieOspfImportAsExtern,
       "ruijieOspfSpfRuns": ruijieOspfSpfRuns,
       "ruijieOspfAreaBdrRtrCount": ruijieOspfAreaBdrRtrCount,
       "ruijieOspfAsBdrRtrCount": ruijieOspfAsBdrRtrCount,
       "ruijieOspfAreaLsaCount": ruijieOspfAreaLsaCount,
       "ruijieOspfAreaLsaCksumSum": ruijieOspfAreaLsaCksumSum,
       "ruijieOspfAreaSummary": ruijieOspfAreaSummary,
       "ruijieOspfAreaStatus": ruijieOspfAreaStatus,
       "ruijieOspfAreaInterfaceNum": ruijieOspfAreaInterfaceNum,
       "ruijieOspfAreaNssaIsRedistribution": ruijieOspfAreaNssaIsRedistribution,
       "ruijieOspfAreaNssaIsDefInfoOriginate": ruijieOspfAreaNssaIsDefInfoOriginate,
       "ruijieOspfAddressScopeTable": ruijieOspfAddressScopeTable,
       "ruijieOspfAddressScopeEntry": ruijieOspfAddressScopeEntry,
       "ruijieOspfNetWorkAreaID": ruijieOspfNetWorkAreaID,
       "ruijieOspfNetWorkAddress": ruijieOspfNetWorkAddress,
       "ruijieOspfNetWorkMask": ruijieOspfNetWorkMask,
       "ruijieOspfNetWorkStatus": ruijieOspfNetWorkStatus,
       "ruijieOspfIfTable": ruijieOspfIfTable,
       "ruijieOspfIfEntry": ruijieOspfIfEntry,
       "ruijieOspfIfIpAddress": ruijieOspfIfIpAddress,
       "ruijieOspfAddressLessIf": ruijieOspfAddressLessIf,
       "ruijieOspfIfAreaId": ruijieOspfIfAreaId,
       "ruijieOspfIfType": ruijieOspfIfType,
       "ruijieOspfIfAdminStat": ruijieOspfIfAdminStat,
       "ruijieOspfIfRtrPriority": ruijieOspfIfRtrPriority,
       "ruijieOspfIfTransitDelay": ruijieOspfIfTransitDelay,
       "ruijieOspfIfRetransInterval": ruijieOspfIfRetransInterval,
       "ruijieOspfIfHelloInterval": ruijieOspfIfHelloInterval,
       "ruijieOspfIfRtrDeadInterval": ruijieOspfIfRtrDeadInterval,
       "ruijieOspfIfPollInterval": ruijieOspfIfPollInterval,
       "ruijieOspfIfState": ruijieOspfIfState,
       "ruijieOspfIfDesignatedRouter": ruijieOspfIfDesignatedRouter,
       "ruijieOspfIfBackupDesignatedRouter": ruijieOspfIfBackupDesignatedRouter,
       "ruijieOspfIfEvents": ruijieOspfIfEvents,
       "ruijieOspfIfAuthKey": ruijieOspfIfAuthKey,
       "ruijieOspfIfStatus": ruijieOspfIfStatus,
       "ruijieOspfIfMulticastForwarding": ruijieOspfIfMulticastForwarding,
       "ruijieOspfIfDemand": ruijieOspfIfDemand,
       "ruijieOspfIfAuthType": ruijieOspfIfAuthType,
       "ruijieOspfIfDatabaseFilterAllOut": ruijieOspfIfDatabaseFilterAllOut,
       "ruijieOspfIfDesignateRouterId": ruijieOspfIfDesignateRouterId,
       "ruijieOspfIfBackupDesignateRouterId": ruijieOspfIfBackupDesignateRouterId,
       "ruijieOspfIfWaitInternal": ruijieOspfIfWaitInternal,
       "ruijieOspfIfPassiveStatus": ruijieOspfIfPassiveStatus,
       "ruijieOspfIfCurrentUsedMd5AuthKeyId": ruijieOspfIfCurrentUsedMd5AuthKeyId,
       "ruijieOspfIfMd5AuthKeyTable": ruijieOspfIfMd5AuthKeyTable,
       "ruijieOspfIfMd5AuthKeyEntry": ruijieOspfIfMd5AuthKeyEntry,
       "ruijieOspfIfMd5AuthKeyIf": ruijieOspfIfMd5AuthKeyIf,
       "ruijieOspfIfMd5AuthKeyId": ruijieOspfIfMd5AuthKeyId,
       "ruijieOspfIfMd5AuthKey": ruijieOspfIfMd5AuthKey,
       "ruijieOspfIfMd5AuthKeySt": ruijieOspfIfMd5AuthKeySt,
       "ruijieOspfVirtTable": ruijieOspfVirtTable,
       "ruijieOspfVirtEntry": ruijieOspfVirtEntry,
       "ruijieOspfVirtIfAreaId": ruijieOspfVirtIfAreaId,
       "ruijieOspfVirtIfNeighbor": ruijieOspfVirtIfNeighbor,
       "ruijieOspfVirtIfTransitDelay": ruijieOspfVirtIfTransitDelay,
       "ruijieOspfVirtIfRetransInterval": ruijieOspfVirtIfRetransInterval,
       "ruijieOspfVirtIfHelloInterval": ruijieOspfVirtIfHelloInterval,
       "ruijieOspfVirtIfRtrDeadInterval": ruijieOspfVirtIfRtrDeadInterval,
       "ruijieOspfVirtIfState": ruijieOspfVirtIfState,
       "ruijieOspfVirtIfEvents": ruijieOspfVirtIfEvents,
       "ruijieOspfVirtIfAuthKey": ruijieOspfVirtIfAuthKey,
       "ruijieOspfVirtIfStatus": ruijieOspfVirtIfStatus,
       "ruijieOspfVirtIfAuthType": ruijieOspfVirtIfAuthType,
       "ruijieOspfVirtCost": ruijieOspfVirtCost,
       "ruijieOspfVirtNativeIfIndex": ruijieOspfVirtNativeIfIndex,
       "ruijieOspfVirtLinkState": ruijieOspfVirtLinkState,
       "ruijieOspfVirtHelloDueIn": ruijieOspfVirtHelloDueIn,
       "ruijieOspfVirtCurrentUsedMd5AuthKeyId": ruijieOspfVirtCurrentUsedMd5AuthKeyId,
       "ruijieOspfVirtIfMd5AuthKeyTable": ruijieOspfVirtIfMd5AuthKeyTable,
       "ruijieOspfVirtIfMd5AuthKeyEntry": ruijieOspfVirtIfMd5AuthKeyEntry,
       "ruijieOspfVirtIfMd5AuthKeyAreaId": ruijieOspfVirtIfMd5AuthKeyAreaId,
       "ruijieOspfVirtIfMd5AuthKeyNeighbor": ruijieOspfVirtIfMd5AuthKeyNeighbor,
       "ruijieOspfVirtIfMd5AuthKeyId": ruijieOspfVirtIfMd5AuthKeyId,
       "ruijieOspfVirtIfMd5AuthKey": ruijieOspfVirtIfMd5AuthKey,
       "ruijieOspfVirtIfMd5AuthKeySt": ruijieOspfVirtIfMd5AuthKeySt,
       "ruijieOspfLsaDetailInfoMibsGroup": ruijieOspfLsaDetailInfoMibsGroup,
       "ruijieOspfLsdbTable": ruijieOspfLsdbTable,
       "ruijieOspfLsdbEntry": ruijieOspfLsdbEntry,
       "ruijieOspfLsdbAreaId": ruijieOspfLsdbAreaId,
       "ruijieOspfLsdbType": ruijieOspfLsdbType,
       "ruijieOspfLsdbLsid": ruijieOspfLsdbLsid,
       "ruijieOspfLsdbRouterId": ruijieOspfLsdbRouterId,
       "ruijieOspfLsdbSequence": ruijieOspfLsdbSequence,
       "ruijieOspfLsdbAge": ruijieOspfLsdbAge,
       "ruijieOspfLsdbChecksum": ruijieOspfLsdbChecksum,
       "ruijieOspfLsdbAdvertisement": ruijieOspfLsdbAdvertisement,
       "ruijieOspfLsdbLinkNum": ruijieOspfLsdbLinkNum,
       "ruijieOspfLsdbPacketLength": ruijieOspfLsdbPacketLength,
       "ruijieOspfSummaryLsaNetworkMask": ruijieOspfSummaryLsaNetworkMask,
       "ruijieOspfSummaryLsaTos0Metric": ruijieOspfSummaryLsaTos0Metric,
       "ruijieOspfNssaLsaDetailMetricType": ruijieOspfNssaLsaDetailMetricType,
       "ruijieOspfNssaLsaDetailForwardAddr": ruijieOspfNssaLsaDetailForwardAddr,
       "ruijieOspfNssaLsaDetailRouteTag": ruijieOspfNssaLsaDetailRouteTag,
       "ruijieOspfLsdbOption": ruijieOspfLsdbOption,
       "ruijieOspfExtLsdbTable": ruijieOspfExtLsdbTable,
       "ruijieOspfExtLsdbEntry": ruijieOspfExtLsdbEntry,
       "ruijieOspfExtLsdbType": ruijieOspfExtLsdbType,
       "ruijieOspfExtLsdbLsid": ruijieOspfExtLsdbLsid,
       "ruijieOspfExtLsdbRouterId": ruijieOspfExtLsdbRouterId,
       "ruijieOspfExtLsdbSequence": ruijieOspfExtLsdbSequence,
       "ruijieOspfExtLsdbAge": ruijieOspfExtLsdbAge,
       "ruijieOspfExtLsdbChecksum": ruijieOspfExtLsdbChecksum,
       "ruijieOspfExtLsdbAdvertisement": ruijieOspfExtLsdbAdvertisement,
       "ruijieOspfExtLsdbNetworkMask": ruijieOspfExtLsdbNetworkMask,
       "ruijieOspfExtLsdbMetric": ruijieOspfExtLsdbMetric,
       "ruijieOspfExtLsdbMetricType": ruijieOspfExtLsdbMetricType,
       "ruijieOspfExtLsdbForwardAddr": ruijieOspfExtLsdbForwardAddr,
       "ruijieOspfExtLsdbRouteTag": ruijieOspfExtLsdbRouteTag,
       "ruijieOspfExtLsdbOption": ruijieOspfExtLsdbOption,
       "ruijieOspfExtLsdbPacketLength": ruijieOspfExtLsdbPacketLength,
       "ruijieOspfRouterLsaDetailTable": ruijieOspfRouterLsaDetailTable,
       "ruijieOspfRouterLsaDetailEntry": ruijieOspfRouterLsaDetailEntry,
       "ruijieOspfRouterLsaDetailLinkID": ruijieOspfRouterLsaDetailLinkID,
       "ruijieOspfRouterLsaDetailLinkType": ruijieOspfRouterLsaDetailLinkType,
       "ruijieOspfRouterLsaDetailLinkData": ruijieOspfRouterLsaDetailLinkData,
       "ruijieOspfRouterLsaDetailTos0Metric": ruijieOspfRouterLsaDetailTos0Metric,
       "ruijieOspfNetWorkLsaDetailTable": ruijieOspfNetWorkLsaDetailTable,
       "ruijieOspfNetWorkLsaDetailEntry": ruijieOspfNetWorkLsaDetailEntry,
       "ruijieOspfNetWorkLsaDetailAttachedRouter": ruijieOspfNetWorkLsaDetailAttachedRouter,
       "ruijieOspfNetWorkLsaDetailNetworkMask": ruijieOspfNetWorkLsaDetailNetworkMask,
       "ruijieOspfAreaLsaDBSumTable": ruijieOspfAreaLsaDBSumTable,
       "ruijieOspfAreaLsaDBSumEntry": ruijieOspfAreaLsaDBSumEntry,
       "ruijieOspfAreaLsaDBSumAreaId": ruijieOspfAreaLsaDBSumAreaId,
       "ruijieOspfAreaLsaDBSumLsaType": ruijieOspfAreaLsaDBSumLsaType,
       "ruijieOspfAreaLsaDBSumCounts": ruijieOspfAreaLsaDBSumCounts,
       "ruijieOspfAreaLsaDBSumDeletes": ruijieOspfAreaLsaDBSumDeletes,
       "ruijieOspfAreaLsaDBSumMaxage": ruijieOspfAreaLsaDBSumMaxage,
       "ruijieOspfLsaDBSumTable": ruijieOspfLsaDBSumTable,
       "ruijieOspfLsaDBSumEntry": ruijieOspfLsaDBSumEntry,
       "ruijieOspfLsaDBSumLsaType": ruijieOspfLsaDBSumLsaType,
       "ruijieOspfLsaDBSumCounts": ruijieOspfLsaDBSumCounts,
       "ruijieOspfLsaDBSumDeletes": ruijieOspfLsaDBSumDeletes,
       "ruijieOspfLsaDBSumMaxage": ruijieOspfLsaDBSumMaxage,
       "ruijieOspfNeighborTable": ruijieOspfNeighborTable,
       "ruijieOspfNeighborEntry": ruijieOspfNeighborEntry,
       "ruijieOspfNbrIpAddr": ruijieOspfNbrIpAddr,
       "ruijieOspfNbrAddressLessIndex": ruijieOspfNbrAddressLessIndex,
       "ruijieOspfNbrRtrId": ruijieOspfNbrRtrId,
       "ruijieOspfNbrOptions": ruijieOspfNbrOptions,
       "ruijieOspfNbrPriority": ruijieOspfNbrPriority,
       "ruijieOspfNbrState": ruijieOspfNbrState,
       "ruijieOspfNbrEvents": ruijieOspfNbrEvents,
       "ruijieOspfNbrLsRetransQLen": ruijieOspfNbrLsRetransQLen,
       "ruijieOspfNbmaNbrStatus": ruijieOspfNbmaNbrStatus,
       "ruijieOspfNbmaNbrPermanence": ruijieOspfNbmaNbrPermanence,
       "ruijieOspfNbrHelloSuppressed": ruijieOspfNbrHelloSuppressed,
       "ruijieOspfNbrDeadTimeDueIn": ruijieOspfNbrDeadTimeDueIn,
       "ruijieOspfNbrNeighborUpTime": ruijieOspfNbrNeighborUpTime,
       "ruijieOspfNbrDR": ruijieOspfNbrDR,
       "ruijieOspfNbrBDR": ruijieOspfNbrBDR,
       "ruijieOspfNbrArea": ruijieOspfNbrArea,
       "ruijieOspfNbrRetransmissionNum": ruijieOspfNbrRetransmissionNum,
       "ruijieOspfNbrIfState": ruijieOspfNbrIfState,
       "ruijieOspfRouteTable": ruijieOspfRouteTable,
       "ruijieOspfRouteEntry": ruijieOspfRouteEntry,
       "ruijieOspfRouteDest": ruijieOspfRouteDest,
       "ruijieOspfRouteArea": ruijieOspfRouteArea,
       "ruijieOspfRouteNextHop": ruijieOspfRouteNextHop,
       "ruijieOspfRouteCost": ruijieOspfRouteCost,
       "ruijieOspfRouteDRType": ruijieOspfRouteDRType,
       "ruijieOspfRouteType": ruijieOspfRouteType,
       "ruijieOspfRouteSpfNo": ruijieOspfRouteSpfNo,
       "ruijieOspfMIBConformance": ruijieOspfMIBConformance,
       "ruijieOspfMIBCompliances": ruijieOspfMIBCompliances,
       "ruijieOspfMIBCompliance": ruijieOspfMIBCompliance,
       "ruijieOspfMIBGroups": ruijieOspfMIBGroups,
       "ruijieOspfBaseMIBGroup": ruijieOspfBaseMIBGroup,
       "ruijieOspfAreaMIBGroup": ruijieOspfAreaMIBGroup,
       "ruijieOspfLsaMIBGroup": ruijieOspfLsaMIBGroup,
       "ruijieOspfIfMIBGroup": ruijieOspfIfMIBGroup,
       "ruijieOspfVirtMIBGroup": ruijieOspfVirtMIBGroup,
       "ruijieOspfNeighborMIBGroup": ruijieOspfNeighborMIBGroup,
       "ruijieOspfRouteInfoMIBGroup": ruijieOspfRouteInfoMIBGroup,
       "ospfMIBConformance": ospfMIBConformance,
       "ospfMIBCompliances": ospfMIBCompliances,
       "ospfExternCompliance": ospfExternCompliance}
)
