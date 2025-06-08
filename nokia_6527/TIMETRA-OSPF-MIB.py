# SNMP MIB module (TIMETRA-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-OSPF-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:39 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Metric,
 Status,
 ospfAddressLessIf,
 ospfAreaEntry,
 ospfIfEntry,
 ospfIfIpAddress,
 ospfNbrEntry,
 ospfRouterId,
 ospfVirtIfAreaId,
 ospfVirtIfEntry,
 ospfVirtIfNeighbor,
 ospfVirtNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "Metric",
    "Status",
    "ospfAddressLessIf",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfIfIpAddress",
    "ospfNbrEntry",
    "ospfRouterId",
    "ospfVirtIfAreaId",
    "ospfVirtIfEntry",
    "ospfVirtIfNeighbor",
    "ospfVirtNbrEntry")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxOperState")

(vRtrID,
 vRtrName) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrName")


# MODULE-IDENTITY

timetraOspfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    timetraOspfMIBModule.setRevisions(
        ("1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OspfInternalPreference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class OspfExternalPreference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxVRtrOspfConformance_ObjectIdentity = ObjectIdentity
tmnxVRtrOspfConformance = _TmnxVRtrOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5)
)
_TmnxVRtrOspfCompliances_ObjectIdentity = ObjectIdentity
tmnxVRtrOspfCompliances = _TmnxVRtrOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 1)
)
_TmnxVRtrOspfGroups_ObjectIdentity = ObjectIdentity
tmnxVRtrOspfGroups = _TmnxVRtrOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2)
)
_TmnxVRtrOspfObjs_ObjectIdentity = ObjectIdentity
tmnxVRtrOspfObjs = _TmnxVRtrOspfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5)
)
_VRtrOspfGeneralObjs_ObjectIdentity = ObjectIdentity
vRtrOspfGeneralObjs = _VRtrOspfGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1)
)


class _VRtrOspfSpfSpacing_Type(Integer32):
    """Custom type vRtrOspfSpfSpacing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_VRtrOspfSpfSpacing_Type.__name__ = "Integer32"
_VRtrOspfSpfSpacing_Object = MibScalar
vRtrOspfSpfSpacing = _VRtrOspfSpfSpacing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 3),
    _VRtrOspfSpfSpacing_Type()
)
vRtrOspfSpfSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfSpfSpacing.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfSpfSpacing.setUnits("seconds")


class _VRtrOspfSpfHoldDown_Type(Integer32):
    """Custom type vRtrOspfSpfHoldDown based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_VRtrOspfSpfHoldDown_Type.__name__ = "Integer32"
_VRtrOspfSpfHoldDown_Object = MibScalar
vRtrOspfSpfHoldDown = _VRtrOspfSpfHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 4),
    _VRtrOspfSpfHoldDown_Type()
)
vRtrOspfSpfHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfSpfHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfSpfHoldDown.setUnits("seconds")
_VRtrOspfLastExtSpfRunTime_Type = TimeStamp
_VRtrOspfLastExtSpfRunTime_Object = MibScalar
vRtrOspfLastExtSpfRunTime = _VRtrOspfLastExtSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 5),
    _VRtrOspfLastExtSpfRunTime_Type()
)
vRtrOspfLastExtSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastExtSpfRunTime.setStatus("current")
_VRtrOspfExtSpfRuns_Type = Counter32
_VRtrOspfExtSpfRuns_Object = MibScalar
vRtrOspfExtSpfRuns = _VRtrOspfExtSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 6),
    _VRtrOspfExtSpfRuns_Type()
)
vRtrOspfExtSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfExtSpfRuns.setStatus("current")


class _VRtrOspfLsaAgingInterval_Type(Integer32):
    """Custom type vRtrOspfLsaAgingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrOspfLsaAgingInterval_Type.__name__ = "Integer32"
_VRtrOspfLsaAgingInterval_Object = MibScalar
vRtrOspfLsaAgingInterval = _VRtrOspfLsaAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 7),
    _VRtrOspfLsaAgingInterval_Type()
)
vRtrOspfLsaAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfLsaAgingInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfLsaAgingInterval.setUnits("seconds")


class _VRtrOspfMaxLsaAgingCount_Type(Integer32):
    """Custom type vRtrOspfMaxLsaAgingCount based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_VRtrOspfMaxLsaAgingCount_Type.__name__ = "Integer32"
_VRtrOspfMaxLsaAgingCount_Object = MibScalar
vRtrOspfMaxLsaAgingCount = _VRtrOspfMaxLsaAgingCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 8),
    _VRtrOspfMaxLsaAgingCount_Type()
)
vRtrOspfMaxLsaAgingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfMaxLsaAgingCount.setStatus("current")


class _VRtrOspfBaseRefCost_Type(Integer32):
    """Custom type vRtrOspfBaseRefCost based on Integer32"""
    defaultValue = 100000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_VRtrOspfBaseRefCost_Type.__name__ = "Integer32"
_VRtrOspfBaseRefCost_Object = MibScalar
vRtrOspfBaseRefCost = _VRtrOspfBaseRefCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 9),
    _VRtrOspfBaseRefCost_Type()
)
vRtrOspfBaseRefCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfBaseRefCost.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfBaseRefCost.setUnits("kilobits per second")
_VRtrOspfBackBoneRouter_Type = TruthValue
_VRtrOspfBackBoneRouter_Object = MibScalar
vRtrOspfBackBoneRouter = _VRtrOspfBackBoneRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 10),
    _VRtrOspfBackBoneRouter_Type()
)
vRtrOspfBackBoneRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfBackBoneRouter.setStatus("current")
_VRtrOspfLastEnabledTime_Type = TimeStamp
_VRtrOspfLastEnabledTime_Object = MibScalar
vRtrOspfLastEnabledTime = _VRtrOspfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 11),
    _VRtrOspfLastEnabledTime_Type()
)
vRtrOspfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastEnabledTime.setStatus("current")
_VRtrOspfLastOverflowEnteredTime_Type = TimeStamp
_VRtrOspfLastOverflowEnteredTime_Object = MibScalar
vRtrOspfLastOverflowEnteredTime = _VRtrOspfLastOverflowEnteredTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 12),
    _VRtrOspfLastOverflowEnteredTime_Type()
)
vRtrOspfLastOverflowEnteredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastOverflowEnteredTime.setStatus("current")
_VRtrOspfLastOverflowExitTime_Type = TimeStamp
_VRtrOspfLastOverflowExitTime_Object = MibScalar
vRtrOspfLastOverflowExitTime = _VRtrOspfLastOverflowExitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 13),
    _VRtrOspfLastOverflowExitTime_Type()
)
vRtrOspfLastOverflowExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastOverflowExitTime.setStatus("current")
_VRtrOspfInOverflowState_Type = TruthValue
_VRtrOspfInOverflowState_Object = MibScalar
vRtrOspfInOverflowState = _VRtrOspfInOverflowState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 14),
    _VRtrOspfInOverflowState_Type()
)
vRtrOspfInOverflowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfInOverflowState.setStatus("current")


class _VRtrOspfPreference_Type(OspfInternalPreference):
    """Custom type vRtrOspfPreference based on OspfInternalPreference"""
    defaultValue = 10


_VRtrOspfPreference_Type.__name__ = "OspfInternalPreference"
_VRtrOspfPreference_Object = MibScalar
vRtrOspfPreference = _VRtrOspfPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 15),
    _VRtrOspfPreference_Type()
)
vRtrOspfPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfPreference.setStatus("current")


class _VRtrOspfExternalPreference_Type(OspfExternalPreference):
    """Custom type vRtrOspfExternalPreference based on OspfExternalPreference"""
    defaultValue = 150


_VRtrOspfExternalPreference_Type.__name__ = "OspfExternalPreference"
_VRtrOspfExternalPreference_Object = MibScalar
vRtrOspfExternalPreference = _VRtrOspfExternalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 16),
    _VRtrOspfExternalPreference_Type()
)
vRtrOspfExternalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfExternalPreference.setStatus("current")


class _VRtrOspfExportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrOspfExportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrOspfExportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrOspfExportPolicy1_Object = MibScalar
vRtrOspfExportPolicy1 = _VRtrOspfExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 17),
    _VRtrOspfExportPolicy1_Type()
)
vRtrOspfExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfExportPolicy1.setStatus("current")


class _VRtrOspfExportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrOspfExportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrOspfExportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrOspfExportPolicy2_Object = MibScalar
vRtrOspfExportPolicy2 = _VRtrOspfExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 18),
    _VRtrOspfExportPolicy2_Type()
)
vRtrOspfExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfExportPolicy2.setStatus("current")


class _VRtrOspfExportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrOspfExportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrOspfExportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrOspfExportPolicy3_Object = MibScalar
vRtrOspfExportPolicy3 = _VRtrOspfExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 19),
    _VRtrOspfExportPolicy3_Type()
)
vRtrOspfExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfExportPolicy3.setStatus("current")


class _VRtrOspfExportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrOspfExportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrOspfExportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrOspfExportPolicy4_Object = MibScalar
vRtrOspfExportPolicy4 = _VRtrOspfExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 20),
    _VRtrOspfExportPolicy4_Type()
)
vRtrOspfExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfExportPolicy4.setStatus("current")


class _VRtrOspfExportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrOspfExportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrOspfExportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrOspfExportPolicy5_Object = MibScalar
vRtrOspfExportPolicy5 = _VRtrOspfExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 21),
    _VRtrOspfExportPolicy5_Type()
)
vRtrOspfExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfExportPolicy5.setStatus("current")


class _VRtrOspfTransmitInterval_Type(Unsigned32):
    """Custom type vRtrOspfTransmitInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967),
    )


_VRtrOspfTransmitInterval_Type.__name__ = "Unsigned32"
_VRtrOspfTransmitInterval_Object = MibScalar
vRtrOspfTransmitInterval = _VRtrOspfTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 22),
    _VRtrOspfTransmitInterval_Type()
)
vRtrOspfTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfTransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfTransmitInterval.setUnits("milliseconds")


class _VRtrOspfManualSpfTrigger_Type(Integer32):
    """Custom type vRtrOspfManualSpfTrigger based on Integer32"""
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
        *(("noAction", 1),
          ("runTotalSpf", 2),
          ("runExternalsSpf", 3))
    )


_VRtrOspfManualSpfTrigger_Type.__name__ = "Integer32"
_VRtrOspfManualSpfTrigger_Object = MibScalar
vRtrOspfManualSpfTrigger = _VRtrOspfManualSpfTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 23),
    _VRtrOspfManualSpfTrigger_Type()
)
vRtrOspfManualSpfTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrOspfManualSpfTrigger.setStatus("current")
_VRtrOspfType11LsaCount_Type = Counter32
_VRtrOspfType11LsaCount_Object = MibScalar
vRtrOspfType11LsaCount = _VRtrOspfType11LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 24),
    _VRtrOspfType11LsaCount_Type()
)
vRtrOspfType11LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfType11LsaCount.setStatus("current")
_VRtrOspfType11LsaChecksumSum_Type = Unsigned32
_VRtrOspfType11LsaChecksumSum_Object = MibScalar
vRtrOspfType11LsaChecksumSum = _VRtrOspfType11LsaChecksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 25),
    _VRtrOspfType11LsaChecksumSum_Type()
)
vRtrOspfType11LsaChecksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfType11LsaChecksumSum.setStatus("current")
_VRtrOspfIncrementalInterSpfRuns_Type = Counter32
_VRtrOspfIncrementalInterSpfRuns_Object = MibScalar
vRtrOspfIncrementalInterSpfRuns = _VRtrOspfIncrementalInterSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 26),
    _VRtrOspfIncrementalInterSpfRuns_Type()
)
vRtrOspfIncrementalInterSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIncrementalInterSpfRuns.setStatus("current")
_VRtrOspfIncrementalExtSpfRuns_Type = Counter32
_VRtrOspfIncrementalExtSpfRuns_Object = MibScalar
vRtrOspfIncrementalExtSpfRuns = _VRtrOspfIncrementalExtSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 27),
    _VRtrOspfIncrementalExtSpfRuns_Type()
)
vRtrOspfIncrementalExtSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIncrementalExtSpfRuns.setStatus("current")
_VRtrOspfMaxSpfRunTime_Type = TimeInterval
_VRtrOspfMaxSpfRunTime_Object = MibScalar
vRtrOspfMaxSpfRunTime = _VRtrOspfMaxSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 28),
    _VRtrOspfMaxSpfRunTime_Type()
)
vRtrOspfMaxSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfMaxSpfRunTime.setStatus("current")
_VRtrOspfMinSpfRunTime_Type = TimeInterval
_VRtrOspfMinSpfRunTime_Object = MibScalar
vRtrOspfMinSpfRunTime = _VRtrOspfMinSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 29),
    _VRtrOspfMinSpfRunTime_Type()
)
vRtrOspfMinSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfMinSpfRunTime.setStatus("current")
_VRtrOspfAvgSpfRunTime_Type = TimeInterval
_VRtrOspfAvgSpfRunTime_Object = MibScalar
vRtrOspfAvgSpfRunTime = _VRtrOspfAvgSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 30),
    _VRtrOspfAvgSpfRunTime_Type()
)
vRtrOspfAvgSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAvgSpfRunTime.setStatus("current")
_VRtrOspfExtSpfRunTime_Type = TimeInterval
_VRtrOspfExtSpfRunTime_Object = MibScalar
vRtrOspfExtSpfRunTime = _VRtrOspfExtSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 31),
    _VRtrOspfExtSpfRunTime_Type()
)
vRtrOspfExtSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfExtSpfRunTime.setStatus("current")
_VRtrOspfOverloadAdmStat_Type = Status
_VRtrOspfOverloadAdmStat_Object = MibScalar
vRtrOspfOverloadAdmStat = _VRtrOspfOverloadAdmStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 32),
    _VRtrOspfOverloadAdmStat_Type()
)
vRtrOspfOverloadAdmStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfOverloadAdmStat.setStatus("current")


class _VRtrOspfOverloadOperStat_Type(Integer32):
    """Custom type vRtrOspfOverloadOperStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overload", 1),
          ("noOverload", 2))
    )


_VRtrOspfOverloadOperStat_Type.__name__ = "Integer32"
_VRtrOspfOverloadOperStat_Object = MibScalar
vRtrOspfOverloadOperStat = _VRtrOspfOverloadOperStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 33),
    _VRtrOspfOverloadOperStat_Type()
)
vRtrOspfOverloadOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfOverloadOperStat.setStatus("current")


class _VRtrOspfOverloadInterval_Type(TimeInterval):
    """Custom type vRtrOspfOverloadInterval based on TimeInterval"""
    defaultValue = 0

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrOspfOverloadInterval_Type.__name__ = "TimeInterval"
_VRtrOspfOverloadInterval_Object = MibScalar
vRtrOspfOverloadInterval = _VRtrOspfOverloadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 34),
    _VRtrOspfOverloadInterval_Type()
)
vRtrOspfOverloadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfOverloadInterval.setStatus("current")


class _VRtrOspfBootOverloadAdmStat_Type(Integer32):
    """Custom type vRtrOspfBootOverloadAdmStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledWaitForBgp", 3))
    )


_VRtrOspfBootOverloadAdmStat_Type.__name__ = "Integer32"
_VRtrOspfBootOverloadAdmStat_Object = MibScalar
vRtrOspfBootOverloadAdmStat = _VRtrOspfBootOverloadAdmStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 35),
    _VRtrOspfBootOverloadAdmStat_Type()
)
vRtrOspfBootOverloadAdmStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfBootOverloadAdmStat.setStatus("current")


class _VRtrOspfBootOverloadInterval_Type(TimeInterval):
    """Custom type vRtrOspfBootOverloadInterval based on TimeInterval"""
    defaultValue = 0

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrOspfBootOverloadInterval_Type.__name__ = "TimeInterval"
_VRtrOspfBootOverloadInterval_Object = MibScalar
vRtrOspfBootOverloadInterval = _VRtrOspfBootOverloadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 36),
    _VRtrOspfBootOverloadInterval_Type()
)
vRtrOspfBootOverloadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfBootOverloadInterval.setStatus("current")


class _VRtrOspfOverloadRemInterval_Type(TimeInterval):
    """Custom type vRtrOspfOverloadRemInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrOspfOverloadRemInterval_Type.__name__ = "TimeInterval"
_VRtrOspfOverloadRemInterval_Object = MibScalar
vRtrOspfOverloadRemInterval = _VRtrOspfOverloadRemInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 37),
    _VRtrOspfOverloadRemInterval_Type()
)
vRtrOspfOverloadRemInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfOverloadRemInterval.setStatus("current")
_VRtrOspfLastOverloadEnteredTime_Type = TimeStamp
_VRtrOspfLastOverloadEnteredTime_Object = MibScalar
vRtrOspfLastOverloadEnteredTime = _VRtrOspfLastOverloadEnteredTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 38),
    _VRtrOspfLastOverloadEnteredTime_Type()
)
vRtrOspfLastOverloadEnteredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastOverloadEnteredTime.setStatus("current")
_VRtrOspfLastOverloadExitTime_Type = TimeStamp
_VRtrOspfLastOverloadExitTime_Object = MibScalar
vRtrOspfLastOverloadExitTime = _VRtrOspfLastOverloadExitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 39),
    _VRtrOspfLastOverloadExitTime_Type()
)
vRtrOspfLastOverloadExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastOverloadExitTime.setStatus("current")


class _VRtrOspfLastOverloadExitCode_Type(Integer32):
    """Custom type vRtrOspfLastOverloadExitCode based on Integer32"""
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
        *(("none", 1),
          ("bgpSigRecv", 2),
          ("timerExpired", 3),
          ("manualExit", 4))
    )


_VRtrOspfLastOverloadExitCode_Type.__name__ = "Integer32"
_VRtrOspfLastOverloadExitCode_Object = MibScalar
vRtrOspfLastOverloadExitCode = _VRtrOspfLastOverloadExitCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 40),
    _VRtrOspfLastOverloadExitCode_Type()
)
vRtrOspfLastOverloadExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastOverloadExitCode.setStatus("current")
_VRtrOspfOverloadCounts_Type = Counter32
_VRtrOspfOverloadCounts_Object = MibScalar
vRtrOspfOverloadCounts = _VRtrOspfOverloadCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 41),
    _VRtrOspfOverloadCounts_Type()
)
vRtrOspfOverloadCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfOverloadCounts.setStatus("current")
_VRtrOspfCSPFRequests_Type = Counter32
_VRtrOspfCSPFRequests_Object = MibScalar
vRtrOspfCSPFRequests = _VRtrOspfCSPFRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 42),
    _VRtrOspfCSPFRequests_Type()
)
vRtrOspfCSPFRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfCSPFRequests.setStatus("current")
_VRtrOspfCSPFDroppedRequests_Type = Counter32
_VRtrOspfCSPFDroppedRequests_Object = MibScalar
vRtrOspfCSPFDroppedRequests = _VRtrOspfCSPFDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 43),
    _VRtrOspfCSPFDroppedRequests_Type()
)
vRtrOspfCSPFDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfCSPFDroppedRequests.setStatus("current")
_VRtrOspfCSPFPathsFound_Type = Counter32
_VRtrOspfCSPFPathsFound_Object = MibScalar
vRtrOspfCSPFPathsFound = _VRtrOspfCSPFPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 44),
    _VRtrOspfCSPFPathsFound_Type()
)
vRtrOspfCSPFPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfCSPFPathsFound.setStatus("current")
_VRtrOspfCSPFPathsNotFound_Type = Counter32
_VRtrOspfCSPFPathsNotFound_Object = MibScalar
vRtrOspfCSPFPathsNotFound = _VRtrOspfCSPFPathsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 45),
    _VRtrOspfCSPFPathsNotFound_Type()
)
vRtrOspfCSPFPathsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfCSPFPathsNotFound.setStatus("current")
_VRtrOspfSpfAttemptsFailed_Type = Counter32
_VRtrOspfSpfAttemptsFailed_Object = MibScalar
vRtrOspfSpfAttemptsFailed = _VRtrOspfSpfAttemptsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 46),
    _VRtrOspfSpfAttemptsFailed_Type()
)
vRtrOspfSpfAttemptsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfSpfAttemptsFailed.setStatus("current")


class _VRtrOspfLastOverloadEnterCode_Type(Integer32):
    """Custom type vRtrOspfLastOverloadEnterCode based on Integer32"""
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
        *(("none", 1),
          ("spfFailed", 2),
          ("bootOverload", 3),
          ("manualOverload", 4))
    )


_VRtrOspfLastOverloadEnterCode_Type.__name__ = "Integer32"
_VRtrOspfLastOverloadEnterCode_Object = MibScalar
vRtrOspfLastOverloadEnterCode = _VRtrOspfLastOverloadEnterCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 1, 47),
    _VRtrOspfLastOverloadEnterCode_Type()
)
vRtrOspfLastOverloadEnterCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfLastOverloadEnterCode.setStatus("current")
_VRtrOspfIfTable_Object = MibTable
vRtrOspfIfTable = _VRtrOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    vRtrOspfIfTable.setStatus("current")
_VRtrOspfIfEntry_Object = MibTableRow
vRtrOspfIfEntry = _VRtrOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrOspfIfEntry.setStatus("current")
_VRtrOspfIfLastEnabledTime_Type = TimeStamp
_VRtrOspfIfLastEnabledTime_Object = MibTableColumn
vRtrOspfIfLastEnabledTime = _VRtrOspfIfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 1),
    _VRtrOspfIfLastEnabledTime_Type()
)
vRtrOspfIfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfLastEnabledTime.setStatus("current")


class _VRtrOspfIfNetworkType_Type(Integer32):
    """Custom type vRtrOspfIfNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stub", 1),
          ("transit", 2))
    )


_VRtrOspfIfNetworkType_Type.__name__ = "Integer32"
_VRtrOspfIfNetworkType_Object = MibTableColumn
vRtrOspfIfNetworkType = _VRtrOspfIfNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 2),
    _VRtrOspfIfNetworkType_Type()
)
vRtrOspfIfNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfNetworkType.setStatus("current")
_VRtrOspfIfVRtrIfIndex_Type = InterfaceIndex
_VRtrOspfIfVRtrIfIndex_Object = MibTableColumn
vRtrOspfIfVRtrIfIndex = _VRtrOspfIfVRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 3),
    _VRtrOspfIfVRtrIfIndex_Type()
)
vRtrOspfIfVRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfVRtrIfIndex.setStatus("current")
_VRtrOspfIfPassive_Type = TruthValue
_VRtrOspfIfPassive_Object = MibTableColumn
vRtrOspfIfPassive = _VRtrOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 4),
    _VRtrOspfIfPassive_Type()
)
vRtrOspfIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfPassive.setStatus("current")


class _VRtrOspfIfMTU_Type(Integer32):
    """Custom type vRtrOspfIfMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9198),
    )


_VRtrOspfIfMTU_Type.__name__ = "Integer32"
_VRtrOspfIfMTU_Object = MibTableColumn
vRtrOspfIfMTU = _VRtrOspfIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 5),
    _VRtrOspfIfMTU_Type()
)
vRtrOspfIfMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfMTU.setStatus("current")
_VRtrOspfIfTxPackets_Type = Counter32
_VRtrOspfIfTxPackets_Object = MibTableColumn
vRtrOspfIfTxPackets = _VRtrOspfIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 6),
    _VRtrOspfIfTxPackets_Type()
)
vRtrOspfIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfTxPackets.setStatus("current")
_VRtrOspfIfTxHellos_Type = Counter32
_VRtrOspfIfTxHellos_Object = MibTableColumn
vRtrOspfIfTxHellos = _VRtrOspfIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 7),
    _VRtrOspfIfTxHellos_Type()
)
vRtrOspfIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfTxHellos.setStatus("current")
_VRtrOspfIfTxDBDs_Type = Counter32
_VRtrOspfIfTxDBDs_Object = MibTableColumn
vRtrOspfIfTxDBDs = _VRtrOspfIfTxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 8),
    _VRtrOspfIfTxDBDs_Type()
)
vRtrOspfIfTxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfTxDBDs.setStatus("current")
_VRtrOspfIfTxLSRs_Type = Counter32
_VRtrOspfIfTxLSRs_Object = MibTableColumn
vRtrOspfIfTxLSRs = _VRtrOspfIfTxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 9),
    _VRtrOspfIfTxLSRs_Type()
)
vRtrOspfIfTxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfTxLSRs.setStatus("current")
_VRtrOspfIfTxLSUs_Type = Counter32
_VRtrOspfIfTxLSUs_Object = MibTableColumn
vRtrOspfIfTxLSUs = _VRtrOspfIfTxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 10),
    _VRtrOspfIfTxLSUs_Type()
)
vRtrOspfIfTxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfTxLSUs.setStatus("current")
_VRtrOspfIfTxLSAcks_Type = Counter32
_VRtrOspfIfTxLSAcks_Object = MibTableColumn
vRtrOspfIfTxLSAcks = _VRtrOspfIfTxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 11),
    _VRtrOspfIfTxLSAcks_Type()
)
vRtrOspfIfTxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfTxLSAcks.setStatus("current")
_VRtrOspfIfRxPackets_Type = Counter32
_VRtrOspfIfRxPackets_Object = MibTableColumn
vRtrOspfIfRxPackets = _VRtrOspfIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 12),
    _VRtrOspfIfRxPackets_Type()
)
vRtrOspfIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxPackets.setStatus("current")
_VRtrOspfIfRxHellos_Type = Counter32
_VRtrOspfIfRxHellos_Object = MibTableColumn
vRtrOspfIfRxHellos = _VRtrOspfIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 13),
    _VRtrOspfIfRxHellos_Type()
)
vRtrOspfIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxHellos.setStatus("current")
_VRtrOspfIfRxDBDs_Type = Counter32
_VRtrOspfIfRxDBDs_Object = MibTableColumn
vRtrOspfIfRxDBDs = _VRtrOspfIfRxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 14),
    _VRtrOspfIfRxDBDs_Type()
)
vRtrOspfIfRxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxDBDs.setStatus("current")
_VRtrOspfIfRxLSRs_Type = Counter32
_VRtrOspfIfRxLSRs_Object = MibTableColumn
vRtrOspfIfRxLSRs = _VRtrOspfIfRxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 15),
    _VRtrOspfIfRxLSRs_Type()
)
vRtrOspfIfRxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxLSRs.setStatus("current")
_VRtrOspfIfRxLSUs_Type = Counter32
_VRtrOspfIfRxLSUs_Object = MibTableColumn
vRtrOspfIfRxLSUs = _VRtrOspfIfRxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 16),
    _VRtrOspfIfRxLSUs_Type()
)
vRtrOspfIfRxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxLSUs.setStatus("current")
_VRtrOspfIfRxLSAcks_Type = Counter32
_VRtrOspfIfRxLSAcks_Object = MibTableColumn
vRtrOspfIfRxLSAcks = _VRtrOspfIfRxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 17),
    _VRtrOspfIfRxLSAcks_Type()
)
vRtrOspfIfRxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxLSAcks.setStatus("current")
_VRtrOspfIfDiscardPackets_Type = Counter32
_VRtrOspfIfDiscardPackets_Object = MibTableColumn
vRtrOspfIfDiscardPackets = _VRtrOspfIfDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 18),
    _VRtrOspfIfDiscardPackets_Type()
)
vRtrOspfIfDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfDiscardPackets.setStatus("current")
_VRtrOspfIfRetransmitOuts_Type = Counter32
_VRtrOspfIfRetransmitOuts_Object = MibTableColumn
vRtrOspfIfRetransmitOuts = _VRtrOspfIfRetransmitOuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 19),
    _VRtrOspfIfRetransmitOuts_Type()
)
vRtrOspfIfRetransmitOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRetransmitOuts.setStatus("current")
_VRtrOspfIfBadVersions_Type = Counter32
_VRtrOspfIfBadVersions_Object = MibTableColumn
vRtrOspfIfBadVersions = _VRtrOspfIfBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 20),
    _VRtrOspfIfBadVersions_Type()
)
vRtrOspfIfBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadVersions.setStatus("current")
_VRtrOspfIfBadNetworks_Type = Counter32
_VRtrOspfIfBadNetworks_Object = MibTableColumn
vRtrOspfIfBadNetworks = _VRtrOspfIfBadNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 21),
    _VRtrOspfIfBadNetworks_Type()
)
vRtrOspfIfBadNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadNetworks.setStatus("current")
_VRtrOspfIfBadVirtualLinks_Type = Counter32
_VRtrOspfIfBadVirtualLinks_Object = MibTableColumn
vRtrOspfIfBadVirtualLinks = _VRtrOspfIfBadVirtualLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 22),
    _VRtrOspfIfBadVirtualLinks_Type()
)
vRtrOspfIfBadVirtualLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadVirtualLinks.setStatus("current")
_VRtrOspfIfBadAreas_Type = Counter32
_VRtrOspfIfBadAreas_Object = MibTableColumn
vRtrOspfIfBadAreas = _VRtrOspfIfBadAreas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 23),
    _VRtrOspfIfBadAreas_Type()
)
vRtrOspfIfBadAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadAreas.setStatus("current")
_VRtrOspfIfBadDstAddrs_Type = Counter32
_VRtrOspfIfBadDstAddrs_Object = MibTableColumn
vRtrOspfIfBadDstAddrs = _VRtrOspfIfBadDstAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 24),
    _VRtrOspfIfBadDstAddrs_Type()
)
vRtrOspfIfBadDstAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadDstAddrs.setStatus("current")
_VRtrOspfIfBadAuthTypes_Type = Counter32
_VRtrOspfIfBadAuthTypes_Object = MibTableColumn
vRtrOspfIfBadAuthTypes = _VRtrOspfIfBadAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 25),
    _VRtrOspfIfBadAuthTypes_Type()
)
vRtrOspfIfBadAuthTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadAuthTypes.setStatus("current")
_VRtrOspfIfAuthFailures_Type = Counter32
_VRtrOspfIfAuthFailures_Object = MibTableColumn
vRtrOspfIfAuthFailures = _VRtrOspfIfAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 26),
    _VRtrOspfIfAuthFailures_Type()
)
vRtrOspfIfAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfAuthFailures.setStatus("current")
_VRtrOspfIfBadNeighbors_Type = Counter32
_VRtrOspfIfBadNeighbors_Object = MibTableColumn
vRtrOspfIfBadNeighbors = _VRtrOspfIfBadNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 27),
    _VRtrOspfIfBadNeighbors_Type()
)
vRtrOspfIfBadNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadNeighbors.setStatus("current")
_VRtrOspfIfBadPacketTypes_Type = Counter32
_VRtrOspfIfBadPacketTypes_Object = MibTableColumn
vRtrOspfIfBadPacketTypes = _VRtrOspfIfBadPacketTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 28),
    _VRtrOspfIfBadPacketTypes_Type()
)
vRtrOspfIfBadPacketTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadPacketTypes.setStatus("current")
_VRtrOspfIfNeighborCount_Type = Integer32
_VRtrOspfIfNeighborCount_Object = MibTableColumn
vRtrOspfIfNeighborCount = _VRtrOspfIfNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 29),
    _VRtrOspfIfNeighborCount_Type()
)
vRtrOspfIfNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfNeighborCount.setStatus("current")


class _VRtrOspfIfAdvertiseSubnet_Type(TruthValue):
    """Custom type vRtrOspfIfAdvertiseSubnet based on TruthValue"""
    defaultValue = 1


_VRtrOspfIfAdvertiseSubnet_Type.__name__ = "TruthValue"
_VRtrOspfIfAdvertiseSubnet_Object = MibTableColumn
vRtrOspfIfAdvertiseSubnet = _VRtrOspfIfAdvertiseSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 30),
    _VRtrOspfIfAdvertiseSubnet_Type()
)
vRtrOspfIfAdvertiseSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfAdvertiseSubnet.setStatus("current")
_VRtrOspfIfLastEventTime_Type = TimeStamp
_VRtrOspfIfLastEventTime_Object = MibTableColumn
vRtrOspfIfLastEventTime = _VRtrOspfIfLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 31),
    _VRtrOspfIfLastEventTime_Type()
)
vRtrOspfIfLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfLastEventTime.setStatus("current")
_VRtrOspfIfBadLengths_Type = Counter32
_VRtrOspfIfBadLengths_Object = MibTableColumn
vRtrOspfIfBadLengths = _VRtrOspfIfBadLengths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 32),
    _VRtrOspfIfBadLengths_Type()
)
vRtrOspfIfBadLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadLengths.setStatus("current")
_VRtrOspfIfBadHelloIntervals_Type = Counter32
_VRtrOspfIfBadHelloIntervals_Object = MibTableColumn
vRtrOspfIfBadHelloIntervals = _VRtrOspfIfBadHelloIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 33),
    _VRtrOspfIfBadHelloIntervals_Type()
)
vRtrOspfIfBadHelloIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadHelloIntervals.setStatus("current")
_VRtrOspfIfBadDeadIntervals_Type = Counter32
_VRtrOspfIfBadDeadIntervals_Object = MibTableColumn
vRtrOspfIfBadDeadIntervals = _VRtrOspfIfBadDeadIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 34),
    _VRtrOspfIfBadDeadIntervals_Type()
)
vRtrOspfIfBadDeadIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadDeadIntervals.setStatus("current")
_VRtrOspfIfBadOptions_Type = Counter32
_VRtrOspfIfBadOptions_Object = MibTableColumn
vRtrOspfIfBadOptions = _VRtrOspfIfBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 35),
    _VRtrOspfIfBadOptions_Type()
)
vRtrOspfIfBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfBadOptions.setStatus("current")


class _VRtrOspfIfMD5TransmitKeyId_Type(Integer32):
    """Custom type vRtrOspfIfMD5TransmitKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrOspfIfMD5TransmitKeyId_Type.__name__ = "Integer32"
_VRtrOspfIfMD5TransmitKeyId_Object = MibTableColumn
vRtrOspfIfMD5TransmitKeyId = _VRtrOspfIfMD5TransmitKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 36),
    _VRtrOspfIfMD5TransmitKeyId_Type()
)
vRtrOspfIfMD5TransmitKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfMD5TransmitKeyId.setStatus("current")
_VRtrOspfIfOperMTU_Type = Integer32
_VRtrOspfIfOperMTU_Object = MibTableColumn
vRtrOspfIfOperMTU = _VRtrOspfIfOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 37),
    _VRtrOspfIfOperMTU_Type()
)
vRtrOspfIfOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfOperMTU.setStatus("current")
_VRtrOspfIfRxBadChecksums_Type = Counter32
_VRtrOspfIfRxBadChecksums_Object = MibTableColumn
vRtrOspfIfRxBadChecksums = _VRtrOspfIfRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 2, 1, 38),
    _VRtrOspfIfRxBadChecksums_Type()
)
vRtrOspfIfRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfIfRxBadChecksums.setStatus("current")
_VRtrOspfVirtIfTable_Object = MibTable
vRtrOspfVirtIfTable = _VRtrOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTable.setStatus("current")
_VRtrOspfVirtIfEntry_Object = MibTableRow
vRtrOspfVirtIfEntry = _VRtrOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    vRtrOspfVirtIfEntry.setStatus("current")
_VRtrOspfVirtIfCreateTime_Type = TimeStamp
_VRtrOspfVirtIfCreateTime_Object = MibTableColumn
vRtrOspfVirtIfCreateTime = _VRtrOspfVirtIfCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 1),
    _VRtrOspfVirtIfCreateTime_Type()
)
vRtrOspfVirtIfCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfCreateTime.setStatus("current")
_VRtrOspfVirtIfTxPackets_Type = Counter32
_VRtrOspfVirtIfTxPackets_Object = MibTableColumn
vRtrOspfVirtIfTxPackets = _VRtrOspfVirtIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 2),
    _VRtrOspfVirtIfTxPackets_Type()
)
vRtrOspfVirtIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTxPackets.setStatus("current")
_VRtrOspfVirtIfTxHellos_Type = Counter32
_VRtrOspfVirtIfTxHellos_Object = MibTableColumn
vRtrOspfVirtIfTxHellos = _VRtrOspfVirtIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 3),
    _VRtrOspfVirtIfTxHellos_Type()
)
vRtrOspfVirtIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTxHellos.setStatus("current")
_VRtrOspfVirtIfTxDBDs_Type = Counter32
_VRtrOspfVirtIfTxDBDs_Object = MibTableColumn
vRtrOspfVirtIfTxDBDs = _VRtrOspfVirtIfTxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 4),
    _VRtrOspfVirtIfTxDBDs_Type()
)
vRtrOspfVirtIfTxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTxDBDs.setStatus("current")
_VRtrOspfVirtIfTxLSRs_Type = Counter32
_VRtrOspfVirtIfTxLSRs_Object = MibTableColumn
vRtrOspfVirtIfTxLSRs = _VRtrOspfVirtIfTxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 5),
    _VRtrOspfVirtIfTxLSRs_Type()
)
vRtrOspfVirtIfTxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTxLSRs.setStatus("current")
_VRtrOspfVirtIfTxLSUs_Type = Counter32
_VRtrOspfVirtIfTxLSUs_Object = MibTableColumn
vRtrOspfVirtIfTxLSUs = _VRtrOspfVirtIfTxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 6),
    _VRtrOspfVirtIfTxLSUs_Type()
)
vRtrOspfVirtIfTxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTxLSUs.setStatus("current")
_VRtrOspfVirtIfTxLSAcks_Type = Counter32
_VRtrOspfVirtIfTxLSAcks_Object = MibTableColumn
vRtrOspfVirtIfTxLSAcks = _VRtrOspfVirtIfTxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 7),
    _VRtrOspfVirtIfTxLSAcks_Type()
)
vRtrOspfVirtIfTxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfTxLSAcks.setStatus("current")
_VRtrOspfVirtIfRxPackets_Type = Counter32
_VRtrOspfVirtIfRxPackets_Object = MibTableColumn
vRtrOspfVirtIfRxPackets = _VRtrOspfVirtIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 8),
    _VRtrOspfVirtIfRxPackets_Type()
)
vRtrOspfVirtIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxPackets.setStatus("current")
_VRtrOspfVirtIfRxHellos_Type = Counter32
_VRtrOspfVirtIfRxHellos_Object = MibTableColumn
vRtrOspfVirtIfRxHellos = _VRtrOspfVirtIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 9),
    _VRtrOspfVirtIfRxHellos_Type()
)
vRtrOspfVirtIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxHellos.setStatus("current")
_VRtrOspfVirtIfRxDBDs_Type = Counter32
_VRtrOspfVirtIfRxDBDs_Object = MibTableColumn
vRtrOspfVirtIfRxDBDs = _VRtrOspfVirtIfRxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 10),
    _VRtrOspfVirtIfRxDBDs_Type()
)
vRtrOspfVirtIfRxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxDBDs.setStatus("current")
_VRtrOspfVirtIfRxLSRs_Type = Counter32
_VRtrOspfVirtIfRxLSRs_Object = MibTableColumn
vRtrOspfVirtIfRxLSRs = _VRtrOspfVirtIfRxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 11),
    _VRtrOspfVirtIfRxLSRs_Type()
)
vRtrOspfVirtIfRxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxLSRs.setStatus("current")
_VRtrOspfVirtIfRxLSUs_Type = Counter32
_VRtrOspfVirtIfRxLSUs_Object = MibTableColumn
vRtrOspfVirtIfRxLSUs = _VRtrOspfVirtIfRxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 12),
    _VRtrOspfVirtIfRxLSUs_Type()
)
vRtrOspfVirtIfRxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxLSUs.setStatus("current")
_VRtrOspfVirtIfRxLSAcks_Type = Counter32
_VRtrOspfVirtIfRxLSAcks_Object = MibTableColumn
vRtrOspfVirtIfRxLSAcks = _VRtrOspfVirtIfRxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 13),
    _VRtrOspfVirtIfRxLSAcks_Type()
)
vRtrOspfVirtIfRxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxLSAcks.setStatus("current")
_VRtrOspfVirtIfDiscardPackets_Type = Counter32
_VRtrOspfVirtIfDiscardPackets_Object = MibTableColumn
vRtrOspfVirtIfDiscardPackets = _VRtrOspfVirtIfDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 14),
    _VRtrOspfVirtIfDiscardPackets_Type()
)
vRtrOspfVirtIfDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfDiscardPackets.setStatus("current")
_VRtrOspfVirtIfRetransmitOuts_Type = Counter32
_VRtrOspfVirtIfRetransmitOuts_Object = MibTableColumn
vRtrOspfVirtIfRetransmitOuts = _VRtrOspfVirtIfRetransmitOuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 15),
    _VRtrOspfVirtIfRetransmitOuts_Type()
)
vRtrOspfVirtIfRetransmitOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRetransmitOuts.setStatus("current")
_VRtrOspfVirtIfBadVersions_Type = Counter32
_VRtrOspfVirtIfBadVersions_Object = MibTableColumn
vRtrOspfVirtIfBadVersions = _VRtrOspfVirtIfBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 16),
    _VRtrOspfVirtIfBadVersions_Type()
)
vRtrOspfVirtIfBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadVersions.setStatus("current")
_VRtrOspfVirtIfBadNetworks_Type = Counter32
_VRtrOspfVirtIfBadNetworks_Object = MibTableColumn
vRtrOspfVirtIfBadNetworks = _VRtrOspfVirtIfBadNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 17),
    _VRtrOspfVirtIfBadNetworks_Type()
)
vRtrOspfVirtIfBadNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadNetworks.setStatus("current")
_VRtrOspfVirtIfBadAreas_Type = Counter32
_VRtrOspfVirtIfBadAreas_Object = MibTableColumn
vRtrOspfVirtIfBadAreas = _VRtrOspfVirtIfBadAreas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 18),
    _VRtrOspfVirtIfBadAreas_Type()
)
vRtrOspfVirtIfBadAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadAreas.setStatus("current")
_VRtrOspfVirtIfBadDstAddrs_Type = Counter32
_VRtrOspfVirtIfBadDstAddrs_Object = MibTableColumn
vRtrOspfVirtIfBadDstAddrs = _VRtrOspfVirtIfBadDstAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 19),
    _VRtrOspfVirtIfBadDstAddrs_Type()
)
vRtrOspfVirtIfBadDstAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadDstAddrs.setStatus("current")
_VRtrOspfVirtIfBadAuthTypes_Type = Counter32
_VRtrOspfVirtIfBadAuthTypes_Object = MibTableColumn
vRtrOspfVirtIfBadAuthTypes = _VRtrOspfVirtIfBadAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 20),
    _VRtrOspfVirtIfBadAuthTypes_Type()
)
vRtrOspfVirtIfBadAuthTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadAuthTypes.setStatus("current")
_VRtrOspfVirtIfAuthFailures_Type = Counter32
_VRtrOspfVirtIfAuthFailures_Object = MibTableColumn
vRtrOspfVirtIfAuthFailures = _VRtrOspfVirtIfAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 21),
    _VRtrOspfVirtIfAuthFailures_Type()
)
vRtrOspfVirtIfAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfAuthFailures.setStatus("current")
_VRtrOspfVirtIfBadNeighbors_Type = Counter32
_VRtrOspfVirtIfBadNeighbors_Object = MibTableColumn
vRtrOspfVirtIfBadNeighbors = _VRtrOspfVirtIfBadNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 22),
    _VRtrOspfVirtIfBadNeighbors_Type()
)
vRtrOspfVirtIfBadNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadNeighbors.setStatus("current")
_VRtrOspfVirtIfBadPacketTypes_Type = Counter32
_VRtrOspfVirtIfBadPacketTypes_Object = MibTableColumn
vRtrOspfVirtIfBadPacketTypes = _VRtrOspfVirtIfBadPacketTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 23),
    _VRtrOspfVirtIfBadPacketTypes_Type()
)
vRtrOspfVirtIfBadPacketTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadPacketTypes.setStatus("current")
_VRtrOspfVirtIfLocalIpAddress_Type = IpAddress
_VRtrOspfVirtIfLocalIpAddress_Object = MibTableColumn
vRtrOspfVirtIfLocalIpAddress = _VRtrOspfVirtIfLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 24),
    _VRtrOspfVirtIfLocalIpAddress_Type()
)
vRtrOspfVirtIfLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfLocalIpAddress.setStatus("current")
_VRtrOspfVirtIfCost_Type = Metric
_VRtrOspfVirtIfCost_Object = MibTableColumn
vRtrOspfVirtIfCost = _VRtrOspfVirtIfCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 25),
    _VRtrOspfVirtIfCost_Type()
)
vRtrOspfVirtIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfCost.setStatus("current")
_VRtrOspfVirtIfLastEventTime_Type = TimeStamp
_VRtrOspfVirtIfLastEventTime_Object = MibTableColumn
vRtrOspfVirtIfLastEventTime = _VRtrOspfVirtIfLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 26),
    _VRtrOspfVirtIfLastEventTime_Type()
)
vRtrOspfVirtIfLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfLastEventTime.setStatus("current")
_VRtrOspfVirtIfBadLengths_Type = Counter32
_VRtrOspfVirtIfBadLengths_Object = MibTableColumn
vRtrOspfVirtIfBadLengths = _VRtrOspfVirtIfBadLengths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 27),
    _VRtrOspfVirtIfBadLengths_Type()
)
vRtrOspfVirtIfBadLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadLengths.setStatus("current")
_VRtrOspfVirtIfBadHelloIntervals_Type = Counter32
_VRtrOspfVirtIfBadHelloIntervals_Object = MibTableColumn
vRtrOspfVirtIfBadHelloIntervals = _VRtrOspfVirtIfBadHelloIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 28),
    _VRtrOspfVirtIfBadHelloIntervals_Type()
)
vRtrOspfVirtIfBadHelloIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadHelloIntervals.setStatus("current")
_VRtrOspfVirtIfBadDeadIntervals_Type = Counter32
_VRtrOspfVirtIfBadDeadIntervals_Object = MibTableColumn
vRtrOspfVirtIfBadDeadIntervals = _VRtrOspfVirtIfBadDeadIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 29),
    _VRtrOspfVirtIfBadDeadIntervals_Type()
)
vRtrOspfVirtIfBadDeadIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadDeadIntervals.setStatus("current")
_VRtrOspfVirtIfBadOptions_Type = Counter32
_VRtrOspfVirtIfBadOptions_Object = MibTableColumn
vRtrOspfVirtIfBadOptions = _VRtrOspfVirtIfBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 30),
    _VRtrOspfVirtIfBadOptions_Type()
)
vRtrOspfVirtIfBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfBadOptions.setStatus("current")


class _VRtrOspfVirtIfMD5TransmitKeyId_Type(Integer32):
    """Custom type vRtrOspfVirtIfMD5TransmitKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrOspfVirtIfMD5TransmitKeyId_Type.__name__ = "Integer32"
_VRtrOspfVirtIfMD5TransmitKeyId_Object = MibTableColumn
vRtrOspfVirtIfMD5TransmitKeyId = _VRtrOspfVirtIfMD5TransmitKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 31),
    _VRtrOspfVirtIfMD5TransmitKeyId_Type()
)
vRtrOspfVirtIfMD5TransmitKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5TransmitKeyId.setStatus("current")
_VRtrOspfVirtIfAdminStat_Type = Status
_VRtrOspfVirtIfAdminStat_Object = MibTableColumn
vRtrOspfVirtIfAdminStat = _VRtrOspfVirtIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 32),
    _VRtrOspfVirtIfAdminStat_Type()
)
vRtrOspfVirtIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfAdminStat.setStatus("current")
_VRtrOspfVirtIfRxBadChecksums_Type = Counter32
_VRtrOspfVirtIfRxBadChecksums_Object = MibTableColumn
vRtrOspfVirtIfRxBadChecksums = _VRtrOspfVirtIfRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 3, 1, 33),
    _VRtrOspfVirtIfRxBadChecksums_Type()
)
vRtrOspfVirtIfRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfRxBadChecksums.setStatus("current")
_VRtrOspfAreaTable_Object = MibTable
vRtrOspfAreaTable = _VRtrOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    vRtrOspfAreaTable.setStatus("current")
_VRtrOspfAreaEntry_Object = MibTableRow
vRtrOspfAreaEntry = _VRtrOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrOspfAreaEntry.setStatus("current")
_VRtrOspfAreaActiveInterfaces_Type = Unsigned32
_VRtrOspfAreaActiveInterfaces_Object = MibTableColumn
vRtrOspfAreaActiveInterfaces = _VRtrOspfAreaActiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 1),
    _VRtrOspfAreaActiveInterfaces_Type()
)
vRtrOspfAreaActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaActiveInterfaces.setStatus("current")
_VRtrOspfAreaLastSpfRunTime_Type = TimeStamp
_VRtrOspfAreaLastSpfRunTime_Object = MibTableColumn
vRtrOspfAreaLastSpfRunTime = _VRtrOspfAreaLastSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 2),
    _VRtrOspfAreaLastSpfRunTime_Type()
)
vRtrOspfAreaLastSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaLastSpfRunTime.setStatus("current")


class _VRtrOspfAreaOriginateDefault_Type(Integer32):
    """Custom type vRtrOspfAreaOriginateDefault based on Integer32"""
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
        *(("noOriginate", 1),
          ("originateType3", 2),
          ("originateType7", 3))
    )


_VRtrOspfAreaOriginateDefault_Type.__name__ = "Integer32"
_VRtrOspfAreaOriginateDefault_Object = MibTableColumn
vRtrOspfAreaOriginateDefault = _VRtrOspfAreaOriginateDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 3),
    _VRtrOspfAreaOriginateDefault_Type()
)
vRtrOspfAreaOriginateDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfAreaOriginateDefault.setStatus("current")


class _VRtrOspfAreaNssaRedistribute_Type(TruthValue):
    """Custom type vRtrOspfAreaNssaRedistribute based on TruthValue"""
    defaultValue = 1


_VRtrOspfAreaNssaRedistribute_Type.__name__ = "TruthValue"
_VRtrOspfAreaNssaRedistribute_Object = MibTableColumn
vRtrOspfAreaNssaRedistribute = _VRtrOspfAreaNssaRedistribute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 4),
    _VRtrOspfAreaNssaRedistribute_Type()
)
vRtrOspfAreaNssaRedistribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfAreaNssaRedistribute.setStatus("current")
_VRtrOspfAreaInterfaceCount_Type = Unsigned32
_VRtrOspfAreaInterfaceCount_Object = MibTableColumn
vRtrOspfAreaInterfaceCount = _VRtrOspfAreaInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 5),
    _VRtrOspfAreaInterfaceCount_Type()
)
vRtrOspfAreaInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaInterfaceCount.setStatus("current")
_VRtrOspfAreaVirtualLinkCount_Type = Unsigned32
_VRtrOspfAreaVirtualLinkCount_Object = MibTableColumn
vRtrOspfAreaVirtualLinkCount = _VRtrOspfAreaVirtualLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 6),
    _VRtrOspfAreaVirtualLinkCount_Type()
)
vRtrOspfAreaVirtualLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaVirtualLinkCount.setStatus("current")
_VRtrOspfAreaType1LsaCount_Type = Unsigned32
_VRtrOspfAreaType1LsaCount_Object = MibTableColumn
vRtrOspfAreaType1LsaCount = _VRtrOspfAreaType1LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 7),
    _VRtrOspfAreaType1LsaCount_Type()
)
vRtrOspfAreaType1LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaType1LsaCount.setStatus("current")
_VRtrOspfAreaType2LsaCount_Type = Unsigned32
_VRtrOspfAreaType2LsaCount_Object = MibTableColumn
vRtrOspfAreaType2LsaCount = _VRtrOspfAreaType2LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 8),
    _VRtrOspfAreaType2LsaCount_Type()
)
vRtrOspfAreaType2LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaType2LsaCount.setStatus("current")
_VRtrOspfAreaType3LsaCount_Type = Unsigned32
_VRtrOspfAreaType3LsaCount_Object = MibTableColumn
vRtrOspfAreaType3LsaCount = _VRtrOspfAreaType3LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 9),
    _VRtrOspfAreaType3LsaCount_Type()
)
vRtrOspfAreaType3LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaType3LsaCount.setStatus("current")
_VRtrOspfAreaType4LsaCount_Type = Unsigned32
_VRtrOspfAreaType4LsaCount_Object = MibTableColumn
vRtrOspfAreaType4LsaCount = _VRtrOspfAreaType4LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 10),
    _VRtrOspfAreaType4LsaCount_Type()
)
vRtrOspfAreaType4LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaType4LsaCount.setStatus("current")
_VRtrOspfAreaType7LsaCount_Type = Unsigned32
_VRtrOspfAreaType7LsaCount_Object = MibTableColumn
vRtrOspfAreaType7LsaCount = _VRtrOspfAreaType7LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 11),
    _VRtrOspfAreaType7LsaCount_Type()
)
vRtrOspfAreaType7LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaType7LsaCount.setStatus("current")
_VRtrOspfAreaType10LsaCount_Type = Unsigned32
_VRtrOspfAreaType10LsaCount_Object = MibTableColumn
vRtrOspfAreaType10LsaCount = _VRtrOspfAreaType10LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 12),
    _VRtrOspfAreaType10LsaCount_Type()
)
vRtrOspfAreaType10LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfAreaType10LsaCount.setStatus("current")


class _VRtrOspfAreaRangeBlackhole_Type(TruthValue):
    """Custom type vRtrOspfAreaRangeBlackhole based on TruthValue"""
    defaultValue = 1


_VRtrOspfAreaRangeBlackhole_Type.__name__ = "TruthValue"
_VRtrOspfAreaRangeBlackhole_Object = MibTableColumn
vRtrOspfAreaRangeBlackhole = _VRtrOspfAreaRangeBlackhole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 4, 1, 13),
    _VRtrOspfAreaRangeBlackhole_Type()
)
vRtrOspfAreaRangeBlackhole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfAreaRangeBlackhole.setStatus("current")
_VRtrOspfIfMD5KeyTable_Object = MibTable
vRtrOspfIfMD5KeyTable = _VRtrOspfIfMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyTable.setStatus("current")
_VRtrOspfIfMD5KeyEntry_Object = MibTableRow
vRtrOspfIfMD5KeyEntry = _VRtrOspfIfMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5, 1)
)
vRtrOspfIfMD5KeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
    (0, "TIMETRA-OSPF-MIB", "vRtrOspfIfMD5KeyIndex"),
)
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyEntry.setStatus("current")


class _VRtrOspfIfMD5KeyIndex_Type(Integer32):
    """Custom type vRtrOspfIfMD5KeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrOspfIfMD5KeyIndex_Type.__name__ = "Integer32"
_VRtrOspfIfMD5KeyIndex_Object = MibTableColumn
vRtrOspfIfMD5KeyIndex = _VRtrOspfIfMD5KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5, 1, 1),
    _VRtrOspfIfMD5KeyIndex_Type()
)
vRtrOspfIfMD5KeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyIndex.setStatus("current")
_VRtrOspfIfMD5KeyStatus_Type = RowStatus
_VRtrOspfIfMD5KeyStatus_Object = MibTableColumn
vRtrOspfIfMD5KeyStatus = _VRtrOspfIfMD5KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5, 1, 2),
    _VRtrOspfIfMD5KeyStatus_Type()
)
vRtrOspfIfMD5KeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyStatus.setStatus("current")


class _VRtrOspfIfMD5KeyKey_Type(OctetString):
    """Custom type vRtrOspfIfMD5KeyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrOspfIfMD5KeyKey_Type.__name__ = "OctetString"
_VRtrOspfIfMD5KeyKey_Object = MibTableColumn
vRtrOspfIfMD5KeyKey = _VRtrOspfIfMD5KeyKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5, 1, 3),
    _VRtrOspfIfMD5KeyKey_Type()
)
vRtrOspfIfMD5KeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyKey.setStatus("current")
_VRtrOspfIfMD5KeyStartTime_Type = DateAndTime
_VRtrOspfIfMD5KeyStartTime_Object = MibTableColumn
vRtrOspfIfMD5KeyStartTime = _VRtrOspfIfMD5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5, 1, 4),
    _VRtrOspfIfMD5KeyStartTime_Type()
)
vRtrOspfIfMD5KeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyStartTime.setStatus("current")
_VRtrOspfIfMD5KeyStopTime_Type = DateAndTime
_VRtrOspfIfMD5KeyStopTime_Object = MibTableColumn
vRtrOspfIfMD5KeyStopTime = _VRtrOspfIfMD5KeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 5, 1, 5),
    _VRtrOspfIfMD5KeyStopTime_Type()
)
vRtrOspfIfMD5KeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfIfMD5KeyStopTime.setStatus("current")
_VRtrOspfVirtIfMD5KeyTable_Object = MibTable
vRtrOspfVirtIfMD5KeyTable = _VRtrOspfVirtIfMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyTable.setStatus("current")
_VRtrOspfVirtIfMD5KeyEntry_Object = MibTableRow
vRtrOspfVirtIfMD5KeyEntry = _VRtrOspfVirtIfMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6, 1)
)
vRtrOspfVirtIfMD5KeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "OSPF-MIB", "ospfVirtIfAreaId"),
    (0, "OSPF-MIB", "ospfVirtIfNeighbor"),
    (0, "TIMETRA-OSPF-MIB", "vRtrOspfVirtIfMD5KeyIndex"),
)
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyEntry.setStatus("current")


class _VRtrOspfVirtIfMD5KeyIndex_Type(Integer32):
    """Custom type vRtrOspfVirtIfMD5KeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrOspfVirtIfMD5KeyIndex_Type.__name__ = "Integer32"
_VRtrOspfVirtIfMD5KeyIndex_Object = MibTableColumn
vRtrOspfVirtIfMD5KeyIndex = _VRtrOspfVirtIfMD5KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6, 1, 1),
    _VRtrOspfVirtIfMD5KeyIndex_Type()
)
vRtrOspfVirtIfMD5KeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyIndex.setStatus("current")
_VRtrOspfVirtIfMD5KeyStatus_Type = RowStatus
_VRtrOspfVirtIfMD5KeyStatus_Object = MibTableColumn
vRtrOspfVirtIfMD5KeyStatus = _VRtrOspfVirtIfMD5KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6, 1, 2),
    _VRtrOspfVirtIfMD5KeyStatus_Type()
)
vRtrOspfVirtIfMD5KeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyStatus.setStatus("current")


class _VRtrOspfVirtIfMD5KeyKey_Type(OctetString):
    """Custom type vRtrOspfVirtIfMD5KeyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrOspfVirtIfMD5KeyKey_Type.__name__ = "OctetString"
_VRtrOspfVirtIfMD5KeyKey_Object = MibTableColumn
vRtrOspfVirtIfMD5KeyKey = _VRtrOspfVirtIfMD5KeyKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6, 1, 3),
    _VRtrOspfVirtIfMD5KeyKey_Type()
)
vRtrOspfVirtIfMD5KeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyKey.setStatus("current")
_VRtrOspfVirtIfMD5KeyStartTime_Type = DateAndTime
_VRtrOspfVirtIfMD5KeyStartTime_Object = MibTableColumn
vRtrOspfVirtIfMD5KeyStartTime = _VRtrOspfVirtIfMD5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6, 1, 4),
    _VRtrOspfVirtIfMD5KeyStartTime_Type()
)
vRtrOspfVirtIfMD5KeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyStartTime.setStatus("current")
_VRtrOspfVirtIfMD5KeyStopTime_Type = DateAndTime
_VRtrOspfVirtIfMD5KeyStopTime_Object = MibTableColumn
vRtrOspfVirtIfMD5KeyStopTime = _VRtrOspfVirtIfMD5KeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 6, 1, 5),
    _VRtrOspfVirtIfMD5KeyStopTime_Type()
)
vRtrOspfVirtIfMD5KeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfVirtIfMD5KeyStopTime.setStatus("current")
_VRtrOspfNbrTable_Object = MibTable
vRtrOspfNbrTable = _VRtrOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8)
)
if mibBuilder.loadTexts:
    vRtrOspfNbrTable.setStatus("current")
_VRtrOspfNbrEntry_Object = MibTableRow
vRtrOspfNbrEntry = _VRtrOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrOspfNbrEntry.setStatus("current")
_VRtrOspfNbrUpTime_Type = TimeInterval
_VRtrOspfNbrUpTime_Object = MibTableColumn
vRtrOspfNbrUpTime = _VRtrOspfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 1),
    _VRtrOspfNbrUpTime_Type()
)
vRtrOspfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrUpTime.setStatus("current")
_VRtrOspfNbrLastEventTime_Type = TimeStamp
_VRtrOspfNbrLastEventTime_Object = MibTableColumn
vRtrOspfNbrLastEventTime = _VRtrOspfNbrLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 2),
    _VRtrOspfNbrLastEventTime_Type()
)
vRtrOspfNbrLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrLastEventTime.setStatus("current")


class _VRtrOspfNbrDeadTimeOutstanding_Type(Unsigned32):
    """Custom type vRtrOspfNbrDeadTimeOutstanding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrOspfNbrDeadTimeOutstanding_Type.__name__ = "Unsigned32"
_VRtrOspfNbrDeadTimeOutstanding_Object = MibTableColumn
vRtrOspfNbrDeadTimeOutstanding = _VRtrOspfNbrDeadTimeOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 3),
    _VRtrOspfNbrDeadTimeOutstanding_Type()
)
vRtrOspfNbrDeadTimeOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrDeadTimeOutstanding.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfNbrDeadTimeOutstanding.setUnits("seconds")
_VRtrOspfNbrBadNbrStates_Type = Counter32
_VRtrOspfNbrBadNbrStates_Object = MibTableColumn
vRtrOspfNbrBadNbrStates = _VRtrOspfNbrBadNbrStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 4),
    _VRtrOspfNbrBadNbrStates_Type()
)
vRtrOspfNbrBadNbrStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrBadNbrStates.setStatus("current")
_VRtrOspfNbrLsaInstallFailed_Type = Counter32
_VRtrOspfNbrLsaInstallFailed_Object = MibTableColumn
vRtrOspfNbrLsaInstallFailed = _VRtrOspfNbrLsaInstallFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 5),
    _VRtrOspfNbrLsaInstallFailed_Type()
)
vRtrOspfNbrLsaInstallFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrLsaInstallFailed.setStatus("current")
_VRtrOspfNbrBadSeqNums_Type = Counter32
_VRtrOspfNbrBadSeqNums_Object = MibTableColumn
vRtrOspfNbrBadSeqNums = _VRtrOspfNbrBadSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 6),
    _VRtrOspfNbrBadSeqNums_Type()
)
vRtrOspfNbrBadSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrBadSeqNums.setStatus("current")
_VRtrOspfNbrBadMTUs_Type = Counter32
_VRtrOspfNbrBadMTUs_Object = MibTableColumn
vRtrOspfNbrBadMTUs = _VRtrOspfNbrBadMTUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 7),
    _VRtrOspfNbrBadMTUs_Type()
)
vRtrOspfNbrBadMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrBadMTUs.setStatus("current")
_VRtrOspfNbrBadPackets_Type = Counter32
_VRtrOspfNbrBadPackets_Object = MibTableColumn
vRtrOspfNbrBadPackets = _VRtrOspfNbrBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 8),
    _VRtrOspfNbrBadPackets_Type()
)
vRtrOspfNbrBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrBadPackets.setStatus("current")
_VRtrOspfNbrLsaNotInLsdbs_Type = Counter32
_VRtrOspfNbrLsaNotInLsdbs_Object = MibTableColumn
vRtrOspfNbrLsaNotInLsdbs = _VRtrOspfNbrLsaNotInLsdbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 9),
    _VRtrOspfNbrLsaNotInLsdbs_Type()
)
vRtrOspfNbrLsaNotInLsdbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrLsaNotInLsdbs.setStatus("current")
_VRtrOspfNbrOptionMismatches_Type = Counter32
_VRtrOspfNbrOptionMismatches_Object = MibTableColumn
vRtrOspfNbrOptionMismatches = _VRtrOspfNbrOptionMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 10),
    _VRtrOspfNbrOptionMismatches_Type()
)
vRtrOspfNbrOptionMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrOptionMismatches.setStatus("current")
_VRtrOspfNbrDuplicates_Type = Counter32
_VRtrOspfNbrDuplicates_Object = MibTableColumn
vRtrOspfNbrDuplicates = _VRtrOspfNbrDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 11),
    _VRtrOspfNbrDuplicates_Type()
)
vRtrOspfNbrDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrDuplicates.setStatus("current")
_VRtrOspfNbrIfIndex_Type = InterfaceIndex
_VRtrOspfNbrIfIndex_Object = MibTableColumn
vRtrOspfNbrIfIndex = _VRtrOspfNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 8, 1, 12),
    _VRtrOspfNbrIfIndex_Type()
)
vRtrOspfNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfNbrIfIndex.setStatus("current")
_VRtrOspfVirtNbrTable_Object = MibTable
vRtrOspfVirtNbrTable = _VRtrOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9)
)
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrTable.setStatus("current")
_VRtrOspfVirtNbrEntry_Object = MibTableRow
vRtrOspfVirtNbrEntry = _VRtrOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrEntry.setStatus("current")
_VRtrOspfVirtNbrUpTime_Type = TimeInterval
_VRtrOspfVirtNbrUpTime_Object = MibTableColumn
vRtrOspfVirtNbrUpTime = _VRtrOspfVirtNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 1),
    _VRtrOspfVirtNbrUpTime_Type()
)
vRtrOspfVirtNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrUpTime.setStatus("current")
_VRtrOspfVirtNbrLastEventTime_Type = TimeStamp
_VRtrOspfVirtNbrLastEventTime_Object = MibTableColumn
vRtrOspfVirtNbrLastEventTime = _VRtrOspfVirtNbrLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 2),
    _VRtrOspfVirtNbrLastEventTime_Type()
)
vRtrOspfVirtNbrLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrLastEventTime.setStatus("current")


class _VRtrOspfVirtNbrDeadTimeOutstanding_Type(Unsigned32):
    """Custom type vRtrOspfVirtNbrDeadTimeOutstanding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrOspfVirtNbrDeadTimeOutstanding_Type.__name__ = "Unsigned32"
_VRtrOspfVirtNbrDeadTimeOutstanding_Object = MibTableColumn
vRtrOspfVirtNbrDeadTimeOutstanding = _VRtrOspfVirtNbrDeadTimeOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 3),
    _VRtrOspfVirtNbrDeadTimeOutstanding_Type()
)
vRtrOspfVirtNbrDeadTimeOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrDeadTimeOutstanding.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrDeadTimeOutstanding.setUnits("seconds")
_VRtrOspfVirtNbrBadNbrStates_Type = Counter32
_VRtrOspfVirtNbrBadNbrStates_Object = MibTableColumn
vRtrOspfVirtNbrBadNbrStates = _VRtrOspfVirtNbrBadNbrStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 4),
    _VRtrOspfVirtNbrBadNbrStates_Type()
)
vRtrOspfVirtNbrBadNbrStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrBadNbrStates.setStatus("current")
_VRtrOspfVirtNbrLsaInstallFailed_Type = Counter32
_VRtrOspfVirtNbrLsaInstallFailed_Object = MibTableColumn
vRtrOspfVirtNbrLsaInstallFailed = _VRtrOspfVirtNbrLsaInstallFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 5),
    _VRtrOspfVirtNbrLsaInstallFailed_Type()
)
vRtrOspfVirtNbrLsaInstallFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrLsaInstallFailed.setStatus("current")
_VRtrOspfVirtNbrBadSeqNums_Type = Counter32
_VRtrOspfVirtNbrBadSeqNums_Object = MibTableColumn
vRtrOspfVirtNbrBadSeqNums = _VRtrOspfVirtNbrBadSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 6),
    _VRtrOspfVirtNbrBadSeqNums_Type()
)
vRtrOspfVirtNbrBadSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrBadSeqNums.setStatus("current")
_VRtrOspfVirtNbrBadMTUs_Type = Counter32
_VRtrOspfVirtNbrBadMTUs_Object = MibTableColumn
vRtrOspfVirtNbrBadMTUs = _VRtrOspfVirtNbrBadMTUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 7),
    _VRtrOspfVirtNbrBadMTUs_Type()
)
vRtrOspfVirtNbrBadMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrBadMTUs.setStatus("current")
_VRtrOspfVirtNbrBadPackets_Type = Counter32
_VRtrOspfVirtNbrBadPackets_Object = MibTableColumn
vRtrOspfVirtNbrBadPackets = _VRtrOspfVirtNbrBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 8),
    _VRtrOspfVirtNbrBadPackets_Type()
)
vRtrOspfVirtNbrBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrBadPackets.setStatus("current")
_VRtrOspfVirtNbrLsaNotInLsdbs_Type = Counter32
_VRtrOspfVirtNbrLsaNotInLsdbs_Object = MibTableColumn
vRtrOspfVirtNbrLsaNotInLsdbs = _VRtrOspfVirtNbrLsaNotInLsdbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 9),
    _VRtrOspfVirtNbrLsaNotInLsdbs_Type()
)
vRtrOspfVirtNbrLsaNotInLsdbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrLsaNotInLsdbs.setStatus("current")
_VRtrOspfVirtNbrOptionMismatches_Type = Counter32
_VRtrOspfVirtNbrOptionMismatches_Object = MibTableColumn
vRtrOspfVirtNbrOptionMismatches = _VRtrOspfVirtNbrOptionMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 10),
    _VRtrOspfVirtNbrOptionMismatches_Type()
)
vRtrOspfVirtNbrOptionMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrOptionMismatches.setStatus("current")
_VRtrOspfVirtNbrDuplicates_Type = Counter32
_VRtrOspfVirtNbrDuplicates_Object = MibTableColumn
vRtrOspfVirtNbrDuplicates = _VRtrOspfVirtNbrDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 9, 1, 11),
    _VRtrOspfVirtNbrDuplicates_Type()
)
vRtrOspfVirtNbrDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfVirtNbrDuplicates.setStatus("current")
_VRtrOspfGRTable_Object = MibTable
vRtrOspfGRTable = _VRtrOspfGRTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10)
)
if mibBuilder.loadTexts:
    vRtrOspfGRTable.setStatus("current")
_VRtrOspfGREntry_Object = MibTableRow
vRtrOspfGREntry = _VRtrOspfGREntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1)
)
vRtrOspfGREntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrOspfGREntry.setStatus("current")
_VRtrOspfGRRowStatus_Type = RowStatus
_VRtrOspfGRRowStatus_Object = MibTableColumn
vRtrOspfGRRowStatus = _VRtrOspfGRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1, 1),
    _VRtrOspfGRRowStatus_Type()
)
vRtrOspfGRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfGRRowStatus.setStatus("current")


class _VRtrOspfGRHelper_Type(TruthValue):
    """Custom type vRtrOspfGRHelper based on TruthValue"""
    defaultValue = 1


_VRtrOspfGRHelper_Type.__name__ = "TruthValue"
_VRtrOspfGRHelper_Object = MibTableColumn
vRtrOspfGRHelper = _VRtrOspfGRHelper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1, 2),
    _VRtrOspfGRHelper_Type()
)
vRtrOspfGRHelper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfGRHelper.setStatus("current")


class _VRtrOspfGRNotifyDuration_Type(Unsigned32):
    """Custom type vRtrOspfGRNotifyDuration based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VRtrOspfGRNotifyDuration_Type.__name__ = "Unsigned32"
_VRtrOspfGRNotifyDuration_Object = MibTableColumn
vRtrOspfGRNotifyDuration = _VRtrOspfGRNotifyDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1, 3),
    _VRtrOspfGRNotifyDuration_Type()
)
vRtrOspfGRNotifyDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfGRNotifyDuration.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfGRNotifyDuration.setUnits("seconds")


class _VRtrOspfGRRestartDuration_Type(Unsigned32):
    """Custom type vRtrOspfGRRestartDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_VRtrOspfGRRestartDuration_Type.__name__ = "Unsigned32"
_VRtrOspfGRRestartDuration_Object = MibTableColumn
vRtrOspfGRRestartDuration = _VRtrOspfGRRestartDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1, 4),
    _VRtrOspfGRRestartDuration_Type()
)
vRtrOspfGRRestartDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfGRRestartDuration.setStatus("current")
if mibBuilder.loadTexts:
    vRtrOspfGRRestartDuration.setUnits("seconds")


class _VRtrOspfGRAdminState_Type(TmnxAdminState):
    """Custom type vRtrOspfGRAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrOspfGRAdminState_Type.__name__ = "TmnxAdminState"
_VRtrOspfGRAdminState_Object = MibTableColumn
vRtrOspfGRAdminState = _VRtrOspfGRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1, 5),
    _VRtrOspfGRAdminState_Type()
)
vRtrOspfGRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfGRAdminState.setStatus("current")
_VRtrOspfGROperState_Type = TmnxOperState
_VRtrOspfGROperState_Object = MibTableColumn
vRtrOspfGROperState = _VRtrOspfGROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 5, 10, 1, 6),
    _VRtrOspfGROperState_Type()
)
vRtrOspfGROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOspfGROperState.setStatus("current")
_TmnxVRtrOspfNotifications_ObjectIdentity = ObjectIdentity
tmnxVRtrOspfNotifications = _TmnxVRtrOspfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 5, 0)
)
ospfIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-MIB",
     "vRtrOspfIfEntry")
)
vRtrOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-MIB",
     "vRtrOspfVirtIfEntry")
)
vRtrOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfAreaEntry.registerAugmentions(
    ("TIMETRA-OSPF-MIB",
     "vRtrOspfAreaEntry")
)
vRtrOspfAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("TIMETRA-OSPF-MIB",
     "vRtrOspfNbrEntry")
)
vRtrOspfNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions(
    ("TIMETRA-OSPF-MIB",
     "vRtrOspfVirtNbrEntry")
)
vRtrOspfVirtNbrEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())

# Managed Objects groups

tmnxVRtrOspfGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 1)
)
tmnxVRtrOspfGlobalGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfSpfSpacing"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfSpfHoldDown"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastExtSpfRunTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExtSpfRuns"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLsaAgingInterval"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfMaxLsaAgingCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfBaseRefCost"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfBackBoneRouter"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastEnabledTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverflowEnteredTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverflowExitTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfInOverflowState"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfPreference"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExternalPreference"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExportPolicy1"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExportPolicy2"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExportPolicy3"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExportPolicy4"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExportPolicy5"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfTransmitInterval"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfManualSpfTrigger"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfType11LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfType11LsaChecksumSum"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIncrementalInterSpfRuns"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIncrementalExtSpfRuns"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfMaxSpfRunTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfMinSpfRunTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAvgSpfRunTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfExtSpfRunTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadAdmStat"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadOperStat"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadInterval"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfBootOverloadAdmStat"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfBootOverloadInterval"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadRemInterval"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverloadEnteredTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverloadExitTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverloadExitCode"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadCounts"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfCSPFRequests"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfCSPFDroppedRequests"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfCSPFPathsFound"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfCSPFPathsNotFound"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfSpfAttemptsFailed"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverloadEnterCode"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfGlobalGroup.setStatus("current")

tmnxVRtrOspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 2)
)
tmnxVRtrOspfIfGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfIfLastEnabledTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfNetworkType"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfVRtrIfIndex"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfPassive"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfMTU"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfTxPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfTxHellos"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfTxDBDs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfTxLSRs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfTxLSUs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfTxLSAcks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxHellos"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxDBDs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxLSRs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxLSUs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxLSAcks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfDiscardPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRetransmitOuts"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadVersions"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadNetworks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadVirtualLinks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadAreas"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadDstAddrs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadAuthTypes"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfAuthFailures"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadNeighbors"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadPacketTypes"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfNeighborCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfAdvertiseSubnet"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfLastEventTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadLengths"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadHelloIntervals"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadDeadIntervals"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfBadOptions"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfOperMTU"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfRxBadChecksums"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfMD5KeyStatus"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfMD5KeyKey"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfIfMD5KeyStopTime"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfIfGroup.setStatus("current")

tmnxVRtrOspfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 3)
)
tmnxVRtrOspfVirtIfGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfCreateTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfTxPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfTxHellos"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfTxDBDs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfTxLSRs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfTxLSUs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfTxLSAcks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxHellos"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxDBDs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxLSRs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxLSUs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxLSAcks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfDiscardPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRetransmitOuts"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadVersions"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadNetworks"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadAreas"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadDstAddrs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadAuthTypes"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfAuthFailures"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadNeighbors"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadPacketTypes"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfLocalIpAddress"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfCost"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfLastEventTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadLengths"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadHelloIntervals"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadDeadIntervals"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfBadOptions"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfAdminStat"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfRxBadChecksums"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfMD5KeyStatus"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfMD5KeyKey"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtIfMD5KeyStopTime"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfVirtIfGroup.setStatus("current")

tmnxVRtrOspfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 4)
)
tmnxVRtrOspfAreaGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfAreaActiveInterfaces"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaLastSpfRunTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaOriginateDefault"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaNssaRedistribute"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaInterfaceCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaVirtualLinkCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaType1LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaType2LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaType3LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaType4LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaType7LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaType10LsaCount"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfAreaRangeBlackhole"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfAreaGroup.setStatus("current")

tmnxVRtrOspfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 5)
)
tmnxVRtrOspfNbrGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfNbrUpTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrLastEventTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrDeadTimeOutstanding"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrBadNbrStates"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrLsaInstallFailed"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrBadSeqNums"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrBadMTUs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrBadPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrOptionMismatches"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrDuplicates"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfNbrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfNbrGroup.setStatus("current")

tmnxVRtrOspfVirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 6)
)
tmnxVRtrOspfVirtNbrGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrUpTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrLastEventTime"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrDeadTimeOutstanding"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrBadNbrStates"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrLsaInstallFailed"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrBadSeqNums"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrBadMTUs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrBadPackets"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrOptionMismatches"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfVirtNbrDuplicates"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfVirtNbrGroup.setStatus("current")

tmnxVRtrOspfGRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 7)
)
tmnxVRtrOspfGRGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfGRRowStatus"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfGRHelper"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfGRNotifyDuration"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfGRRestartDuration"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfGRAdminState"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfGROperState"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfGRGroup.setStatus("current")


# Notification objects

vRtrOspfSpfRunsStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 5, 0, 1)
)
vRtrOspfSpfRunsStopped.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrName"),
        ("OSPF-MIB", "ospfRouterId"))
)
if mibBuilder.loadTexts:
    vRtrOspfSpfRunsStopped.setStatus(
        "current"
    )

vRtrOspfSpfRunsRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 5, 0, 2)
)
vRtrOspfSpfRunsRestarted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrName"),
        ("OSPF-MIB", "ospfRouterId"))
)
if mibBuilder.loadTexts:
    vRtrOspfSpfRunsRestarted.setStatus(
        "current"
    )

vRtrOspfOverloadEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 5, 0, 3)
)
vRtrOspfOverloadEntered.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrName"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverloadEnterCode"))
)
if mibBuilder.loadTexts:
    vRtrOspfOverloadEntered.setStatus(
        "current"
    )

vRtrOspfOverloadExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 5, 0, 4)
)
vRtrOspfOverloadExited.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrName"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfLastOverloadExitCode"))
)
if mibBuilder.loadTexts:
    vRtrOspfOverloadExited.setStatus(
        "current"
    )


# Notifications groups

tmnxVRtrOspfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 2, 9)
)
tmnxVRtrOspfNotificationGroup.setObjects(
      *(("TIMETRA-OSPF-MIB", "vRtrOspfSpfRunsStopped"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfSpfRunsRestarted"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadEntered"),
        ("TIMETRA-OSPF-MIB", "vRtrOspfOverloadExited"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxVRtrOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 5, 1, 1)
)
tmnxVRtrOspfCompliance.setObjects(
      *(("TIMETRA-OSPF-MIB", "tmnxVRtrOspfGlobalGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfIfGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfVirtIfGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfAreaGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfNbrGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfGRGroup"),
        ("TIMETRA-OSPF-MIB", "tmnxVRtrOspfNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxVRtrOspfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OSPF-MIB",
    **{"OspfInternalPreference": OspfInternalPreference,
       "OspfExternalPreference": OspfExternalPreference,
       "timetraOspfMIBModule": timetraOspfMIBModule,
       "tmnxVRtrOspfConformance": tmnxVRtrOspfConformance,
       "tmnxVRtrOspfCompliances": tmnxVRtrOspfCompliances,
       "tmnxVRtrOspfCompliance": tmnxVRtrOspfCompliance,
       "tmnxVRtrOspfGroups": tmnxVRtrOspfGroups,
       "tmnxVRtrOspfGlobalGroup": tmnxVRtrOspfGlobalGroup,
       "tmnxVRtrOspfIfGroup": tmnxVRtrOspfIfGroup,
       "tmnxVRtrOspfVirtIfGroup": tmnxVRtrOspfVirtIfGroup,
       "tmnxVRtrOspfAreaGroup": tmnxVRtrOspfAreaGroup,
       "tmnxVRtrOspfNbrGroup": tmnxVRtrOspfNbrGroup,
       "tmnxVRtrOspfVirtNbrGroup": tmnxVRtrOspfVirtNbrGroup,
       "tmnxVRtrOspfGRGroup": tmnxVRtrOspfGRGroup,
       "tmnxVRtrOspfNotificationGroup": tmnxVRtrOspfNotificationGroup,
       "tmnxVRtrOspfObjs": tmnxVRtrOspfObjs,
       "vRtrOspfGeneralObjs": vRtrOspfGeneralObjs,
       "vRtrOspfSpfSpacing": vRtrOspfSpfSpacing,
       "vRtrOspfSpfHoldDown": vRtrOspfSpfHoldDown,
       "vRtrOspfLastExtSpfRunTime": vRtrOspfLastExtSpfRunTime,
       "vRtrOspfExtSpfRuns": vRtrOspfExtSpfRuns,
       "vRtrOspfLsaAgingInterval": vRtrOspfLsaAgingInterval,
       "vRtrOspfMaxLsaAgingCount": vRtrOspfMaxLsaAgingCount,
       "vRtrOspfBaseRefCost": vRtrOspfBaseRefCost,
       "vRtrOspfBackBoneRouter": vRtrOspfBackBoneRouter,
       "vRtrOspfLastEnabledTime": vRtrOspfLastEnabledTime,
       "vRtrOspfLastOverflowEnteredTime": vRtrOspfLastOverflowEnteredTime,
       "vRtrOspfLastOverflowExitTime": vRtrOspfLastOverflowExitTime,
       "vRtrOspfInOverflowState": vRtrOspfInOverflowState,
       "vRtrOspfPreference": vRtrOspfPreference,
       "vRtrOspfExternalPreference": vRtrOspfExternalPreference,
       "vRtrOspfExportPolicy1": vRtrOspfExportPolicy1,
       "vRtrOspfExportPolicy2": vRtrOspfExportPolicy2,
       "vRtrOspfExportPolicy3": vRtrOspfExportPolicy3,
       "vRtrOspfExportPolicy4": vRtrOspfExportPolicy4,
       "vRtrOspfExportPolicy5": vRtrOspfExportPolicy5,
       "vRtrOspfTransmitInterval": vRtrOspfTransmitInterval,
       "vRtrOspfManualSpfTrigger": vRtrOspfManualSpfTrigger,
       "vRtrOspfType11LsaCount": vRtrOspfType11LsaCount,
       "vRtrOspfType11LsaChecksumSum": vRtrOspfType11LsaChecksumSum,
       "vRtrOspfIncrementalInterSpfRuns": vRtrOspfIncrementalInterSpfRuns,
       "vRtrOspfIncrementalExtSpfRuns": vRtrOspfIncrementalExtSpfRuns,
       "vRtrOspfMaxSpfRunTime": vRtrOspfMaxSpfRunTime,
       "vRtrOspfMinSpfRunTime": vRtrOspfMinSpfRunTime,
       "vRtrOspfAvgSpfRunTime": vRtrOspfAvgSpfRunTime,
       "vRtrOspfExtSpfRunTime": vRtrOspfExtSpfRunTime,
       "vRtrOspfOverloadAdmStat": vRtrOspfOverloadAdmStat,
       "vRtrOspfOverloadOperStat": vRtrOspfOverloadOperStat,
       "vRtrOspfOverloadInterval": vRtrOspfOverloadInterval,
       "vRtrOspfBootOverloadAdmStat": vRtrOspfBootOverloadAdmStat,
       "vRtrOspfBootOverloadInterval": vRtrOspfBootOverloadInterval,
       "vRtrOspfOverloadRemInterval": vRtrOspfOverloadRemInterval,
       "vRtrOspfLastOverloadEnteredTime": vRtrOspfLastOverloadEnteredTime,
       "vRtrOspfLastOverloadExitTime": vRtrOspfLastOverloadExitTime,
       "vRtrOspfLastOverloadExitCode": vRtrOspfLastOverloadExitCode,
       "vRtrOspfOverloadCounts": vRtrOspfOverloadCounts,
       "vRtrOspfCSPFRequests": vRtrOspfCSPFRequests,
       "vRtrOspfCSPFDroppedRequests": vRtrOspfCSPFDroppedRequests,
       "vRtrOspfCSPFPathsFound": vRtrOspfCSPFPathsFound,
       "vRtrOspfCSPFPathsNotFound": vRtrOspfCSPFPathsNotFound,
       "vRtrOspfSpfAttemptsFailed": vRtrOspfSpfAttemptsFailed,
       "vRtrOspfLastOverloadEnterCode": vRtrOspfLastOverloadEnterCode,
       "vRtrOspfIfTable": vRtrOspfIfTable,
       "vRtrOspfIfEntry": vRtrOspfIfEntry,
       "vRtrOspfIfLastEnabledTime": vRtrOspfIfLastEnabledTime,
       "vRtrOspfIfNetworkType": vRtrOspfIfNetworkType,
       "vRtrOspfIfVRtrIfIndex": vRtrOspfIfVRtrIfIndex,
       "vRtrOspfIfPassive": vRtrOspfIfPassive,
       "vRtrOspfIfMTU": vRtrOspfIfMTU,
       "vRtrOspfIfTxPackets": vRtrOspfIfTxPackets,
       "vRtrOspfIfTxHellos": vRtrOspfIfTxHellos,
       "vRtrOspfIfTxDBDs": vRtrOspfIfTxDBDs,
       "vRtrOspfIfTxLSRs": vRtrOspfIfTxLSRs,
       "vRtrOspfIfTxLSUs": vRtrOspfIfTxLSUs,
       "vRtrOspfIfTxLSAcks": vRtrOspfIfTxLSAcks,
       "vRtrOspfIfRxPackets": vRtrOspfIfRxPackets,
       "vRtrOspfIfRxHellos": vRtrOspfIfRxHellos,
       "vRtrOspfIfRxDBDs": vRtrOspfIfRxDBDs,
       "vRtrOspfIfRxLSRs": vRtrOspfIfRxLSRs,
       "vRtrOspfIfRxLSUs": vRtrOspfIfRxLSUs,
       "vRtrOspfIfRxLSAcks": vRtrOspfIfRxLSAcks,
       "vRtrOspfIfDiscardPackets": vRtrOspfIfDiscardPackets,
       "vRtrOspfIfRetransmitOuts": vRtrOspfIfRetransmitOuts,
       "vRtrOspfIfBadVersions": vRtrOspfIfBadVersions,
       "vRtrOspfIfBadNetworks": vRtrOspfIfBadNetworks,
       "vRtrOspfIfBadVirtualLinks": vRtrOspfIfBadVirtualLinks,
       "vRtrOspfIfBadAreas": vRtrOspfIfBadAreas,
       "vRtrOspfIfBadDstAddrs": vRtrOspfIfBadDstAddrs,
       "vRtrOspfIfBadAuthTypes": vRtrOspfIfBadAuthTypes,
       "vRtrOspfIfAuthFailures": vRtrOspfIfAuthFailures,
       "vRtrOspfIfBadNeighbors": vRtrOspfIfBadNeighbors,
       "vRtrOspfIfBadPacketTypes": vRtrOspfIfBadPacketTypes,
       "vRtrOspfIfNeighborCount": vRtrOspfIfNeighborCount,
       "vRtrOspfIfAdvertiseSubnet": vRtrOspfIfAdvertiseSubnet,
       "vRtrOspfIfLastEventTime": vRtrOspfIfLastEventTime,
       "vRtrOspfIfBadLengths": vRtrOspfIfBadLengths,
       "vRtrOspfIfBadHelloIntervals": vRtrOspfIfBadHelloIntervals,
       "vRtrOspfIfBadDeadIntervals": vRtrOspfIfBadDeadIntervals,
       "vRtrOspfIfBadOptions": vRtrOspfIfBadOptions,
       "vRtrOspfIfMD5TransmitKeyId": vRtrOspfIfMD5TransmitKeyId,
       "vRtrOspfIfOperMTU": vRtrOspfIfOperMTU,
       "vRtrOspfIfRxBadChecksums": vRtrOspfIfRxBadChecksums,
       "vRtrOspfVirtIfTable": vRtrOspfVirtIfTable,
       "vRtrOspfVirtIfEntry": vRtrOspfVirtIfEntry,
       "vRtrOspfVirtIfCreateTime": vRtrOspfVirtIfCreateTime,
       "vRtrOspfVirtIfTxPackets": vRtrOspfVirtIfTxPackets,
       "vRtrOspfVirtIfTxHellos": vRtrOspfVirtIfTxHellos,
       "vRtrOspfVirtIfTxDBDs": vRtrOspfVirtIfTxDBDs,
       "vRtrOspfVirtIfTxLSRs": vRtrOspfVirtIfTxLSRs,
       "vRtrOspfVirtIfTxLSUs": vRtrOspfVirtIfTxLSUs,
       "vRtrOspfVirtIfTxLSAcks": vRtrOspfVirtIfTxLSAcks,
       "vRtrOspfVirtIfRxPackets": vRtrOspfVirtIfRxPackets,
       "vRtrOspfVirtIfRxHellos": vRtrOspfVirtIfRxHellos,
       "vRtrOspfVirtIfRxDBDs": vRtrOspfVirtIfRxDBDs,
       "vRtrOspfVirtIfRxLSRs": vRtrOspfVirtIfRxLSRs,
       "vRtrOspfVirtIfRxLSUs": vRtrOspfVirtIfRxLSUs,
       "vRtrOspfVirtIfRxLSAcks": vRtrOspfVirtIfRxLSAcks,
       "vRtrOspfVirtIfDiscardPackets": vRtrOspfVirtIfDiscardPackets,
       "vRtrOspfVirtIfRetransmitOuts": vRtrOspfVirtIfRetransmitOuts,
       "vRtrOspfVirtIfBadVersions": vRtrOspfVirtIfBadVersions,
       "vRtrOspfVirtIfBadNetworks": vRtrOspfVirtIfBadNetworks,
       "vRtrOspfVirtIfBadAreas": vRtrOspfVirtIfBadAreas,
       "vRtrOspfVirtIfBadDstAddrs": vRtrOspfVirtIfBadDstAddrs,
       "vRtrOspfVirtIfBadAuthTypes": vRtrOspfVirtIfBadAuthTypes,
       "vRtrOspfVirtIfAuthFailures": vRtrOspfVirtIfAuthFailures,
       "vRtrOspfVirtIfBadNeighbors": vRtrOspfVirtIfBadNeighbors,
       "vRtrOspfVirtIfBadPacketTypes": vRtrOspfVirtIfBadPacketTypes,
       "vRtrOspfVirtIfLocalIpAddress": vRtrOspfVirtIfLocalIpAddress,
       "vRtrOspfVirtIfCost": vRtrOspfVirtIfCost,
       "vRtrOspfVirtIfLastEventTime": vRtrOspfVirtIfLastEventTime,
       "vRtrOspfVirtIfBadLengths": vRtrOspfVirtIfBadLengths,
       "vRtrOspfVirtIfBadHelloIntervals": vRtrOspfVirtIfBadHelloIntervals,
       "vRtrOspfVirtIfBadDeadIntervals": vRtrOspfVirtIfBadDeadIntervals,
       "vRtrOspfVirtIfBadOptions": vRtrOspfVirtIfBadOptions,
       "vRtrOspfVirtIfMD5TransmitKeyId": vRtrOspfVirtIfMD5TransmitKeyId,
       "vRtrOspfVirtIfAdminStat": vRtrOspfVirtIfAdminStat,
       "vRtrOspfVirtIfRxBadChecksums": vRtrOspfVirtIfRxBadChecksums,
       "vRtrOspfAreaTable": vRtrOspfAreaTable,
       "vRtrOspfAreaEntry": vRtrOspfAreaEntry,
       "vRtrOspfAreaActiveInterfaces": vRtrOspfAreaActiveInterfaces,
       "vRtrOspfAreaLastSpfRunTime": vRtrOspfAreaLastSpfRunTime,
       "vRtrOspfAreaOriginateDefault": vRtrOspfAreaOriginateDefault,
       "vRtrOspfAreaNssaRedistribute": vRtrOspfAreaNssaRedistribute,
       "vRtrOspfAreaInterfaceCount": vRtrOspfAreaInterfaceCount,
       "vRtrOspfAreaVirtualLinkCount": vRtrOspfAreaVirtualLinkCount,
       "vRtrOspfAreaType1LsaCount": vRtrOspfAreaType1LsaCount,
       "vRtrOspfAreaType2LsaCount": vRtrOspfAreaType2LsaCount,
       "vRtrOspfAreaType3LsaCount": vRtrOspfAreaType3LsaCount,
       "vRtrOspfAreaType4LsaCount": vRtrOspfAreaType4LsaCount,
       "vRtrOspfAreaType7LsaCount": vRtrOspfAreaType7LsaCount,
       "vRtrOspfAreaType10LsaCount": vRtrOspfAreaType10LsaCount,
       "vRtrOspfAreaRangeBlackhole": vRtrOspfAreaRangeBlackhole,
       "vRtrOspfIfMD5KeyTable": vRtrOspfIfMD5KeyTable,
       "vRtrOspfIfMD5KeyEntry": vRtrOspfIfMD5KeyEntry,
       "vRtrOspfIfMD5KeyIndex": vRtrOspfIfMD5KeyIndex,
       "vRtrOspfIfMD5KeyStatus": vRtrOspfIfMD5KeyStatus,
       "vRtrOspfIfMD5KeyKey": vRtrOspfIfMD5KeyKey,
       "vRtrOspfIfMD5KeyStartTime": vRtrOspfIfMD5KeyStartTime,
       "vRtrOspfIfMD5KeyStopTime": vRtrOspfIfMD5KeyStopTime,
       "vRtrOspfVirtIfMD5KeyTable": vRtrOspfVirtIfMD5KeyTable,
       "vRtrOspfVirtIfMD5KeyEntry": vRtrOspfVirtIfMD5KeyEntry,
       "vRtrOspfVirtIfMD5KeyIndex": vRtrOspfVirtIfMD5KeyIndex,
       "vRtrOspfVirtIfMD5KeyStatus": vRtrOspfVirtIfMD5KeyStatus,
       "vRtrOspfVirtIfMD5KeyKey": vRtrOspfVirtIfMD5KeyKey,
       "vRtrOspfVirtIfMD5KeyStartTime": vRtrOspfVirtIfMD5KeyStartTime,
       "vRtrOspfVirtIfMD5KeyStopTime": vRtrOspfVirtIfMD5KeyStopTime,
       "vRtrOspfNbrTable": vRtrOspfNbrTable,
       "vRtrOspfNbrEntry": vRtrOspfNbrEntry,
       "vRtrOspfNbrUpTime": vRtrOspfNbrUpTime,
       "vRtrOspfNbrLastEventTime": vRtrOspfNbrLastEventTime,
       "vRtrOspfNbrDeadTimeOutstanding": vRtrOspfNbrDeadTimeOutstanding,
       "vRtrOspfNbrBadNbrStates": vRtrOspfNbrBadNbrStates,
       "vRtrOspfNbrLsaInstallFailed": vRtrOspfNbrLsaInstallFailed,
       "vRtrOspfNbrBadSeqNums": vRtrOspfNbrBadSeqNums,
       "vRtrOspfNbrBadMTUs": vRtrOspfNbrBadMTUs,
       "vRtrOspfNbrBadPackets": vRtrOspfNbrBadPackets,
       "vRtrOspfNbrLsaNotInLsdbs": vRtrOspfNbrLsaNotInLsdbs,
       "vRtrOspfNbrOptionMismatches": vRtrOspfNbrOptionMismatches,
       "vRtrOspfNbrDuplicates": vRtrOspfNbrDuplicates,
       "vRtrOspfNbrIfIndex": vRtrOspfNbrIfIndex,
       "vRtrOspfVirtNbrTable": vRtrOspfVirtNbrTable,
       "vRtrOspfVirtNbrEntry": vRtrOspfVirtNbrEntry,
       "vRtrOspfVirtNbrUpTime": vRtrOspfVirtNbrUpTime,
       "vRtrOspfVirtNbrLastEventTime": vRtrOspfVirtNbrLastEventTime,
       "vRtrOspfVirtNbrDeadTimeOutstanding": vRtrOspfVirtNbrDeadTimeOutstanding,
       "vRtrOspfVirtNbrBadNbrStates": vRtrOspfVirtNbrBadNbrStates,
       "vRtrOspfVirtNbrLsaInstallFailed": vRtrOspfVirtNbrLsaInstallFailed,
       "vRtrOspfVirtNbrBadSeqNums": vRtrOspfVirtNbrBadSeqNums,
       "vRtrOspfVirtNbrBadMTUs": vRtrOspfVirtNbrBadMTUs,
       "vRtrOspfVirtNbrBadPackets": vRtrOspfVirtNbrBadPackets,
       "vRtrOspfVirtNbrLsaNotInLsdbs": vRtrOspfVirtNbrLsaNotInLsdbs,
       "vRtrOspfVirtNbrOptionMismatches": vRtrOspfVirtNbrOptionMismatches,
       "vRtrOspfVirtNbrDuplicates": vRtrOspfVirtNbrDuplicates,
       "vRtrOspfGRTable": vRtrOspfGRTable,
       "vRtrOspfGREntry": vRtrOspfGREntry,
       "vRtrOspfGRRowStatus": vRtrOspfGRRowStatus,
       "vRtrOspfGRHelper": vRtrOspfGRHelper,
       "vRtrOspfGRNotifyDuration": vRtrOspfGRNotifyDuration,
       "vRtrOspfGRRestartDuration": vRtrOspfGRRestartDuration,
       "vRtrOspfGRAdminState": vRtrOspfGRAdminState,
       "vRtrOspfGROperState": vRtrOspfGROperState,
       "tmnxVRtrOspfNotifications": tmnxVRtrOspfNotifications,
       "vRtrOspfSpfRunsStopped": vRtrOspfSpfRunsStopped,
       "vRtrOspfSpfRunsRestarted": vRtrOspfSpfRunsRestarted,
       "vRtrOspfOverloadEntered": vRtrOspfOverloadEntered,
       "vRtrOspfOverloadExited": vRtrOspfOverloadExited}
)
