# SNMP MIB module (TIMETRA-CFLOWD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-CFLOWD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:14 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TmnxActionType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxStatus) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxStatus")


# MODULE-IDENTITY

timetraCflowdMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 19)
)
if mibBuilder.loadTexts:
    timetraCflowdMIBModule.setRevisions(
        ("2014-02-01 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-20 00:00",
         "2001-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxCflowdAggScheme(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("asMatrix", 0),
          ("protocolPort", 1),
          ("sourcePrefix", 2),
          ("destinationPrefix", 3),
          ("sourceDestinationPrefix", 4),
          ("raw", 5))
    )


class TmnxCflowdTemplateSet(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("basic", 1),
          ("mplsIp", 2),
          ("l2Ip", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxCflowdConformance_ObjectIdentity = ObjectIdentity
tmnxCflowdConformance = _TmnxCflowdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19)
)
_TmnxCflowdCompliances_ObjectIdentity = ObjectIdentity
tmnxCflowdCompliances = _TmnxCflowdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 1)
)
_TmnxCflowdGroups_ObjectIdentity = ObjectIdentity
tmnxCflowdGroups = _TmnxCflowdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2)
)
_TmnxCflowdV10v0Groups_ObjectIdentity = ObjectIdentity
tmnxCflowdV10v0Groups = _TmnxCflowdV10v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 11)
)
_TmnxCflowdObjs_ObjectIdentity = ObjectIdentity
tmnxCflowdObjs = _TmnxCflowdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19)
)
_TmnxCflowdGeneralObjs_ObjectIdentity = ObjectIdentity
tmnxCflowdGeneralObjs = _TmnxCflowdGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1)
)


class _TmnxCflowdStatus_Type(TmnxStatus):
    """Custom type tmnxCflowdStatus based on TmnxStatus"""
    defaultValue = 2


_TmnxCflowdStatus_Type.__name__ = "TmnxStatus"
_TmnxCflowdStatus_Object = MibScalar
tmnxCflowdStatus = _TmnxCflowdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 1),
    _TmnxCflowdStatus_Type()
)
tmnxCflowdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdStatus.setStatus("current")


class _TmnxCflowdActiveTimeout_Type(Unsigned32):
    """Custom type tmnxCflowdActiveTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_TmnxCflowdActiveTimeout_Type.__name__ = "Unsigned32"
_TmnxCflowdActiveTimeout_Object = MibScalar
tmnxCflowdActiveTimeout = _TmnxCflowdActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 2),
    _TmnxCflowdActiveTimeout_Type()
)
tmnxCflowdActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCflowdActiveTimeout.setUnits("minutes")


class _TmnxCflowdInactiveTimeout_Type(Unsigned32):
    """Custom type tmnxCflowdInactiveTimeout based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_TmnxCflowdInactiveTimeout_Type.__name__ = "Unsigned32"
_TmnxCflowdInactiveTimeout_Object = MibScalar
tmnxCflowdInactiveTimeout = _TmnxCflowdInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 3),
    _TmnxCflowdInactiveTimeout_Type()
)
tmnxCflowdInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdInactiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCflowdInactiveTimeout.setUnits("seconds")


class _TmnxCflowdCacheSize_Type(Unsigned32):
    """Custom type tmnxCflowdCacheSize based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1500000),
    )


_TmnxCflowdCacheSize_Type.__name__ = "Unsigned32"
_TmnxCflowdCacheSize_Object = MibScalar
tmnxCflowdCacheSize = _TmnxCflowdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 4),
    _TmnxCflowdCacheSize_Type()
)
tmnxCflowdCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCflowdCacheSize.setUnits("flows")


class _TmnxCflowdSampleRate_Type(Unsigned32):
    """Custom type tmnxCflowdSampleRate based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxCflowdSampleRate_Type.__name__ = "Unsigned32"
_TmnxCflowdSampleRate_Object = MibScalar
tmnxCflowdSampleRate = _TmnxCflowdSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 5),
    _TmnxCflowdSampleRate_Type()
)
tmnxCflowdSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdSampleRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCflowdSampleRate.setUnits("packets")


class _TmnxCflowdOverflow_Type(Unsigned32):
    """Custom type tmnxCflowdOverflow based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxCflowdOverflow_Type.__name__ = "Unsigned32"
_TmnxCflowdOverflow_Object = MibScalar
tmnxCflowdOverflow = _TmnxCflowdOverflow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 6),
    _TmnxCflowdOverflow_Type()
)
tmnxCflowdOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdOverflow.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCflowdOverflow.setUnits("percentage")


class _TmnxCflowdAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxCflowdAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxCflowdAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxCflowdAdminStatus_Object = MibScalar
tmnxCflowdAdminStatus = _TmnxCflowdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 7),
    _TmnxCflowdAdminStatus_Type()
)
tmnxCflowdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdAdminStatus.setStatus("current")
_TmnxCflowdOperStatus_Type = TmnxOperState
_TmnxCflowdOperStatus_Object = MibScalar
tmnxCflowdOperStatus = _TmnxCflowdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 8),
    _TmnxCflowdOperStatus_Type()
)
tmnxCflowdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdOperStatus.setStatus("current")
_TmnxCflowdActiveFlows_Type = Gauge32
_TmnxCflowdActiveFlows_Object = MibScalar
tmnxCflowdActiveFlows = _TmnxCflowdActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 9),
    _TmnxCflowdActiveFlows_Type()
)
tmnxCflowdActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdActiveFlows.setStatus("current")
_TmnxCflowdAggregation_Type = TmnxCflowdAggScheme
_TmnxCflowdAggregation_Object = MibScalar
tmnxCflowdAggregation = _TmnxCflowdAggregation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 10),
    _TmnxCflowdAggregation_Type()
)
tmnxCflowdAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdAggregation.setStatus("current")
_TmnxCFHostTableLastChanged_Type = TimeStamp
_TmnxCFHostTableLastChanged_Object = MibScalar
tmnxCFHostTableLastChanged = _TmnxCFHostTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 11),
    _TmnxCFHostTableLastChanged_Type()
)
tmnxCFHostTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostTableLastChanged.setStatus("current")


class _TmnxCflowdMaxCollectors_Type(Integer32):
    """Custom type tmnxCflowdMaxCollectors based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxCflowdMaxCollectors_Type.__name__ = "Integer32"
_TmnxCflowdMaxCollectors_Object = MibScalar
tmnxCflowdMaxCollectors = _TmnxCflowdMaxCollectors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 12),
    _TmnxCflowdMaxCollectors_Type()
)
tmnxCflowdMaxCollectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdMaxCollectors.setStatus("current")
_TmnxCflowdTotalPktsRcvd_Type = Counter32
_TmnxCflowdTotalPktsRcvd_Object = MibScalar
tmnxCflowdTotalPktsRcvd = _TmnxCflowdTotalPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 13),
    _TmnxCflowdTotalPktsRcvd_Type()
)
tmnxCflowdTotalPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdTotalPktsRcvd.setStatus("current")
_TmnxCflowdTotalPktsDropped_Type = Counter32
_TmnxCflowdTotalPktsDropped_Object = MibScalar
tmnxCflowdTotalPktsDropped = _TmnxCflowdTotalPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 14),
    _TmnxCflowdTotalPktsDropped_Type()
)
tmnxCflowdTotalPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdTotalPktsDropped.setStatus("current")


class _TmnxCflowdTemplateRetransmit_Type(Unsigned32):
    """Custom type tmnxCflowdTemplateRetransmit based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_TmnxCflowdTemplateRetransmit_Type.__name__ = "Unsigned32"
_TmnxCflowdTemplateRetransmit_Object = MibScalar
tmnxCflowdTemplateRetransmit = _TmnxCflowdTemplateRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 15),
    _TmnxCflowdTemplateRetransmit_Type()
)
tmnxCflowdTemplateRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateRetransmit.setUnits("seconds")
_TmnxCflowdGeneralStatisticsObjs_ObjectIdentity = ObjectIdentity
tmnxCflowdGeneralStatisticsObjs = _TmnxCflowdGeneralStatisticsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16)
)
_TmnxCflowdGenRawFlowsCreated_Type = Counter32
_TmnxCflowdGenRawFlowsCreated_Object = MibScalar
tmnxCflowdGenRawFlowsCreated = _TmnxCflowdGenRawFlowsCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 1),
    _TmnxCflowdGenRawFlowsCreated_Type()
)
tmnxCflowdGenRawFlowsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenRawFlowsCreated.setStatus("current")
_TmnxCflowdGenAggrFlowsCreated_Type = Counter32
_TmnxCflowdGenAggrFlowsCreated_Object = MibScalar
tmnxCflowdGenAggrFlowsCreated = _TmnxCflowdGenAggrFlowsCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 2),
    _TmnxCflowdGenAggrFlowsCreated_Type()
)
tmnxCflowdGenAggrFlowsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenAggrFlowsCreated.setStatus("current")
_TmnxCflowdGenRawFlowsMatched_Type = Counter32
_TmnxCflowdGenRawFlowsMatched_Object = MibScalar
tmnxCflowdGenRawFlowsMatched = _TmnxCflowdGenRawFlowsMatched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 3),
    _TmnxCflowdGenRawFlowsMatched_Type()
)
tmnxCflowdGenRawFlowsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenRawFlowsMatched.setStatus("current")
_TmnxCflowdGenAggrFlowsMatched_Type = Counter32
_TmnxCflowdGenAggrFlowsMatched_Object = MibScalar
tmnxCflowdGenAggrFlowsMatched = _TmnxCflowdGenAggrFlowsMatched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 4),
    _TmnxCflowdGenAggrFlowsMatched_Type()
)
tmnxCflowdGenAggrFlowsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenAggrFlowsMatched.setStatus("current")
_TmnxCflowdGenRawFlowsFlushed_Type = Counter32
_TmnxCflowdGenRawFlowsFlushed_Object = MibScalar
tmnxCflowdGenRawFlowsFlushed = _TmnxCflowdGenRawFlowsFlushed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 5),
    _TmnxCflowdGenRawFlowsFlushed_Type()
)
tmnxCflowdGenRawFlowsFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenRawFlowsFlushed.setStatus("current")
_TmnxCflowdGenAggrFlowsFlushed_Type = Counter32
_TmnxCflowdGenAggrFlowsFlushed_Object = MibScalar
tmnxCflowdGenAggrFlowsFlushed = _TmnxCflowdGenAggrFlowsFlushed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 6),
    _TmnxCflowdGenAggrFlowsFlushed_Type()
)
tmnxCflowdGenAggrFlowsFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenAggrFlowsFlushed.setStatus("current")
_TmnxCflowdGenOverflowEvents_Type = Counter32
_TmnxCflowdGenOverflowEvents_Object = MibScalar
tmnxCflowdGenOverflowEvents = _TmnxCflowdGenOverflowEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 7),
    _TmnxCflowdGenOverflowEvents_Type()
)
tmnxCflowdGenOverflowEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenOverflowEvents.setStatus("current")
_TmnxCflowdGenDroppedFlows_Type = Counter32
_TmnxCflowdGenDroppedFlows_Object = MibScalar
tmnxCflowdGenDroppedFlows = _TmnxCflowdGenDroppedFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 16, 8),
    _TmnxCflowdGenDroppedFlows_Type()
)
tmnxCflowdGenDroppedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdGenDroppedFlows.setStatus("current")


class _TmnxCflowdExportMode_Type(Integer32):
    """Custom type tmnxCflowdExportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_TmnxCflowdExportMode_Type.__name__ = "Integer32"
_TmnxCflowdExportMode_Object = MibScalar
tmnxCflowdExportMode = _TmnxCflowdExportMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 17),
    _TmnxCflowdExportMode_Type()
)
tmnxCflowdExportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdExportMode.setStatus("current")


class _TmnxCflowdExportManual_Type(TmnxActionType):
    """Custom type tmnxCflowdExportManual based on TmnxActionType"""
    defaultValue = 2


_TmnxCflowdExportManual_Type.__name__ = "TmnxActionType"
_TmnxCflowdExportManual_Object = MibScalar
tmnxCflowdExportManual = _TmnxCflowdExportManual_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 1, 18),
    _TmnxCflowdExportManual_Type()
)
tmnxCflowdExportManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCflowdExportManual.setStatus("current")
_TmnxCflowdNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxCflowdNotificationObjects = _TmnxCflowdNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 2)
)


class _TmnxCflowdFlowFailureReasonCode_Type(Integer32):
    """Custom type tmnxCflowdFlowFailureReasonCode based on Integer32"""
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
        *(("tmnxCflowdMemAllocFailure", 0),
          ("tmnxCflowdRTLookupFailure", 1),
          ("tmnxCflowdTimerCreateFailure", 2),
          ("tmnxCflowdUDPSendFailure", 3))
    )


_TmnxCflowdFlowFailureReasonCode_Type.__name__ = "Integer32"
_TmnxCflowdFlowFailureReasonCode_Object = MibScalar
tmnxCflowdFlowFailureReasonCode = _TmnxCflowdFlowFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 2, 1),
    _TmnxCflowdFlowFailureReasonCode_Type()
)
tmnxCflowdFlowFailureReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCflowdFlowFailureReasonCode.setStatus("current")


class _TmnxCflowdFlowUnsuppIPProtoNum_Type(Unsigned32):
    """Custom type tmnxCflowdFlowUnsuppIPProtoNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxCflowdFlowUnsuppIPProtoNum_Type.__name__ = "Unsigned32"
_TmnxCflowdFlowUnsuppIPProtoNum_Object = MibScalar
tmnxCflowdFlowUnsuppIPProtoNum = _TmnxCflowdFlowUnsuppIPProtoNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 2, 2),
    _TmnxCflowdFlowUnsuppIPProtoNum_Type()
)
tmnxCflowdFlowUnsuppIPProtoNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCflowdFlowUnsuppIPProtoNum.setStatus("obsolete")
_TmnxCFHostTable_Object = MibTable
tmnxCFHostTable = _TmnxCFHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3)
)
if mibBuilder.loadTexts:
    tmnxCFHostTable.setStatus("current")
_TmnxCFHostEntry_Object = MibTableRow
tmnxCFHostEntry = _TmnxCFHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1)
)
tmnxCFHostEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostUdpPort"),
)
if mibBuilder.loadTexts:
    tmnxCFHostEntry.setStatus("current")
_TmnxCFHostAddress_Type = IpAddress
_TmnxCFHostAddress_Object = MibTableColumn
tmnxCFHostAddress = _TmnxCFHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 1),
    _TmnxCFHostAddress_Type()
)
tmnxCFHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostAddress.setStatus("current")


class _TmnxCFHostUdpPort_Type(Integer32):
    """Custom type tmnxCFHostUdpPort based on Integer32"""
    defaultValue = 2055

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxCFHostUdpPort_Type.__name__ = "Integer32"
_TmnxCFHostUdpPort_Object = MibTableColumn
tmnxCFHostUdpPort = _TmnxCFHostUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 2),
    _TmnxCFHostUdpPort_Type()
)
tmnxCFHostUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostUdpPort.setStatus("current")
_TmnxCFHostRowStatus_Type = RowStatus
_TmnxCFHostRowStatus_Object = MibTableColumn
tmnxCFHostRowStatus = _TmnxCFHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 3),
    _TmnxCFHostRowStatus_Type()
)
tmnxCFHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostRowStatus.setStatus("current")
_TmnxCFHostEntryLastChanged_Type = TimeStamp
_TmnxCFHostEntryLastChanged_Object = MibTableColumn
tmnxCFHostEntryLastChanged = _TmnxCFHostEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 4),
    _TmnxCFHostEntryLastChanged_Type()
)
tmnxCFHostEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostEntryLastChanged.setStatus("current")


class _TmnxCFHostDescription_Type(TItemDescription):
    """Custom type tmnxCFHostDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxCFHostDescription_Type.__name__ = "TItemDescription"
_TmnxCFHostDescription_Object = MibTableColumn
tmnxCFHostDescription = _TmnxCFHostDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 5),
    _TmnxCFHostDescription_Type()
)
tmnxCFHostDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostDescription.setStatus("current")


class _TmnxCFHostAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxCFHostAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxCFHostAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxCFHostAdminStatus_Object = MibTableColumn
tmnxCFHostAdminStatus = _TmnxCFHostAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 6),
    _TmnxCFHostAdminStatus_Type()
)
tmnxCFHostAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostAdminStatus.setStatus("current")
_TmnxCFHostOperStatus_Type = TmnxOperState
_TmnxCFHostOperStatus_Object = MibTableColumn
tmnxCFHostOperStatus = _TmnxCFHostOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 7),
    _TmnxCFHostOperStatus_Type()
)
tmnxCFHostOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostOperStatus.setStatus("current")


class _TmnxCFHostASType_Type(Integer32):
    """Custom type tmnxCFHostASType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("origin", 1),
          ("peer", 2))
    )


_TmnxCFHostASType_Type.__name__ = "Integer32"
_TmnxCFHostASType_Object = MibTableColumn
tmnxCFHostASType = _TmnxCFHostASType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 8),
    _TmnxCFHostASType_Type()
)
tmnxCFHostASType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostASType.setStatus("current")


class _TmnxCFHostAggregation_Type(TmnxCflowdAggScheme):
    """Custom type tmnxCFHostAggregation based on TmnxCflowdAggScheme"""
    defaultBinValue = "0"


_TmnxCFHostAggregation_Type.__name__ = "TmnxCflowdAggScheme"
_TmnxCFHostAggregation_Object = MibTableColumn
tmnxCFHostAggregation = _TmnxCFHostAggregation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 9),
    _TmnxCFHostAggregation_Type()
)
tmnxCFHostAggregation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostAggregation.setStatus("current")
_TmnxCFHostRecordsSent_Type = Counter32
_TmnxCFHostRecordsSent_Object = MibTableColumn
tmnxCFHostRecordsSent = _TmnxCFHostRecordsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 10),
    _TmnxCFHostRecordsSent_Type()
)
tmnxCFHostRecordsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostRecordsSent.setStatus("current")
_TmnxCFHostLastPktSent_Type = TimeStamp
_TmnxCFHostLastPktSent_Object = MibTableColumn
tmnxCFHostLastPktSent = _TmnxCFHostLastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 11),
    _TmnxCFHostLastPktSent_Type()
)
tmnxCFHostLastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostLastPktSent.setStatus("current")


class _TmnxCFHostVersion_Type(Unsigned32):
    """Custom type tmnxCFHostVersion based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(8, 10),
    )


_TmnxCFHostVersion_Type.__name__ = "Unsigned32"
_TmnxCFHostVersion_Object = MibTableColumn
tmnxCFHostVersion = _TmnxCFHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 12),
    _TmnxCFHostVersion_Type()
)
tmnxCFHostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostVersion.setStatus("current")


class _TmnxCFHostTemplateSet_Type(TmnxCflowdTemplateSet):
    """Custom type tmnxCFHostTemplateSet based on TmnxCflowdTemplateSet"""
    defaultValue = 0


_TmnxCFHostTemplateSet_Type.__name__ = "TmnxCflowdTemplateSet"
_TmnxCFHostTemplateSet_Object = MibTableColumn
tmnxCFHostTemplateSet = _TmnxCFHostTemplateSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 13),
    _TmnxCFHostTemplateSet_Type()
)
tmnxCFHostTemplateSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostTemplateSet.setStatus("current")
_TmnxCFHostPacketsSent_Type = Counter32
_TmnxCFHostPacketsSent_Object = MibTableColumn
tmnxCFHostPacketsSent = _TmnxCFHostPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 3, 1, 14),
    _TmnxCFHostPacketsSent_Type()
)
tmnxCFHostPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostPacketsSent.setStatus("current")
_TmnxCflowdVersionStatsTable_Object = MibTable
tmnxCflowdVersionStatsTable = _TmnxCflowdVersionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4)
)
if mibBuilder.loadTexts:
    tmnxCflowdVersionStatsTable.setStatus("current")
_TmnxCflowdVersionStatsEntry_Object = MibTableRow
tmnxCflowdVersionStatsEntry = _TmnxCflowdVersionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4, 1)
)
tmnxCflowdVersionStatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCflowdVersionIndex"),
)
if mibBuilder.loadTexts:
    tmnxCflowdVersionStatsEntry.setStatus("current")


class _TmnxCflowdVersionIndex_Type(Unsigned32):
    """Custom type tmnxCflowdVersionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(8, 10),
    )


_TmnxCflowdVersionIndex_Type.__name__ = "Unsigned32"
_TmnxCflowdVersionIndex_Object = MibTableColumn
tmnxCflowdVersionIndex = _TmnxCflowdVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4, 1, 1),
    _TmnxCflowdVersionIndex_Type()
)
tmnxCflowdVersionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCflowdVersionIndex.setStatus("current")
_TmnxCflowdVersionStatus_Type = TmnxEnabledDisabled
_TmnxCflowdVersionStatus_Object = MibTableColumn
tmnxCflowdVersionStatus = _TmnxCflowdVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4, 1, 2),
    _TmnxCflowdVersionStatus_Type()
)
tmnxCflowdVersionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdVersionStatus.setStatus("current")
_TmnxCflowdVersionSent_Type = Counter32
_TmnxCflowdVersionSent_Object = MibTableColumn
tmnxCflowdVersionSent = _TmnxCflowdVersionSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4, 1, 3),
    _TmnxCflowdVersionSent_Type()
)
tmnxCflowdVersionSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdVersionSent.setStatus("current")
_TmnxCflowdVersionOpen_Type = Counter32
_TmnxCflowdVersionOpen_Object = MibTableColumn
tmnxCflowdVersionOpen = _TmnxCflowdVersionOpen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4, 1, 4),
    _TmnxCflowdVersionOpen_Type()
)
tmnxCflowdVersionOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdVersionOpen.setStatus("current")
_TmnxCflowdVersionErrors_Type = Counter32
_TmnxCflowdVersionErrors_Object = MibTableColumn
tmnxCflowdVersionErrors = _TmnxCflowdVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 4, 1, 5),
    _TmnxCflowdVersionErrors_Type()
)
tmnxCflowdVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdVersionErrors.setStatus("current")
_TmnxCflowdV5StatsTable_Object = MibTable
tmnxCflowdV5StatsTable = _TmnxCflowdV5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 5)
)
if mibBuilder.loadTexts:
    tmnxCflowdV5StatsTable.setStatus("current")
_TmnxCflowdV5StatsEntry_Object = MibTableRow
tmnxCflowdV5StatsEntry = _TmnxCflowdV5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 5, 1)
)
tmnxCflowdV5StatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostUdpPort"),
)
if mibBuilder.loadTexts:
    tmnxCflowdV5StatsEntry.setStatus("current")
_TmnxCflowdV5Sent_Type = Counter32
_TmnxCflowdV5Sent_Object = MibTableColumn
tmnxCflowdV5Sent = _TmnxCflowdV5Sent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 5, 1, 1),
    _TmnxCflowdV5Sent_Type()
)
tmnxCflowdV5Sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdV5Sent.setStatus("current")
_TmnxCflowdV5Open_Type = Counter32
_TmnxCflowdV5Open_Object = MibTableColumn
tmnxCflowdV5Open = _TmnxCflowdV5Open_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 5, 1, 2),
    _TmnxCflowdV5Open_Type()
)
tmnxCflowdV5Open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdV5Open.setStatus("current")
_TmnxCflowdV5Errors_Type = Counter32
_TmnxCflowdV5Errors_Object = MibTableColumn
tmnxCflowdV5Errors = _TmnxCflowdV5Errors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 5, 1, 3),
    _TmnxCflowdV5Errors_Type()
)
tmnxCflowdV5Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdV5Errors.setStatus("current")
_TmnxCflowdAggregationStatsTable_Object = MibTable
tmnxCflowdAggregationStatsTable = _TmnxCflowdAggregationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6)
)
if mibBuilder.loadTexts:
    tmnxCflowdAggregationStatsTable.setStatus("current")
_TmnxCflowdAggregationStatsEntry_Object = MibTableRow
tmnxCflowdAggregationStatsEntry = _TmnxCflowdAggregationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6, 1)
)
tmnxCflowdAggregationStatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostUdpPort"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCflowdAggregationIndex"),
)
if mibBuilder.loadTexts:
    tmnxCflowdAggregationStatsEntry.setStatus("current")


class _TmnxCflowdAggregationIndex_Type(Integer32):
    """Custom type tmnxCflowdAggregationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nonAggregate", 0),
          ("asMatrix", 1),
          ("protocolPort", 2),
          ("sourcePrefix", 3),
          ("destinationPrefix", 4),
          ("sourceDestinationPrefix", 5),
          ("raw", 6))
    )


_TmnxCflowdAggregationIndex_Type.__name__ = "Integer32"
_TmnxCflowdAggregationIndex_Object = MibTableColumn
tmnxCflowdAggregationIndex = _TmnxCflowdAggregationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6, 1, 1),
    _TmnxCflowdAggregationIndex_Type()
)
tmnxCflowdAggregationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCflowdAggregationIndex.setStatus("current")
_TmnxCflowdAggregationStatus_Type = TmnxEnabledDisabled
_TmnxCflowdAggregationStatus_Object = MibTableColumn
tmnxCflowdAggregationStatus = _TmnxCflowdAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6, 1, 2),
    _TmnxCflowdAggregationStatus_Type()
)
tmnxCflowdAggregationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdAggregationStatus.setStatus("current")
_TmnxCflowdAggregationSent_Type = Counter32
_TmnxCflowdAggregationSent_Object = MibTableColumn
tmnxCflowdAggregationSent = _TmnxCflowdAggregationSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6, 1, 3),
    _TmnxCflowdAggregationSent_Type()
)
tmnxCflowdAggregationSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdAggregationSent.setStatus("current")
_TmnxCflowdAggregationOpen_Type = Counter32
_TmnxCflowdAggregationOpen_Object = MibTableColumn
tmnxCflowdAggregationOpen = _TmnxCflowdAggregationOpen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6, 1, 4),
    _TmnxCflowdAggregationOpen_Type()
)
tmnxCflowdAggregationOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdAggregationOpen.setStatus("current")
_TmnxCflowdAggregationErrors_Type = Counter32
_TmnxCflowdAggregationErrors_Object = MibTableColumn
tmnxCflowdAggregationErrors = _TmnxCflowdAggregationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 6, 1, 5),
    _TmnxCflowdAggregationErrors_Type()
)
tmnxCflowdAggregationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdAggregationErrors.setStatus("current")
_TmnxCflowdTemplateStatsTable_Object = MibTable
tmnxCflowdTemplateStatsTable = _TmnxCflowdTemplateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7)
)
if mibBuilder.loadTexts:
    tmnxCflowdTemplateStatsTable.setStatus("current")
_TmnxCflowdTemplateStatsEntry_Object = MibTableRow
tmnxCflowdTemplateStatsEntry = _TmnxCflowdTemplateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7, 1)
)
tmnxCflowdTemplateStatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostUdpPort"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCflowdTemplateFlowIndex"),
)
if mibBuilder.loadTexts:
    tmnxCflowdTemplateStatsEntry.setStatus("current")


class _TmnxCflowdTemplateFlowIndex_Type(Integer32):
    """Custom type tmnxCflowdTemplateFlowIndex based on Integer32"""
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
        *(("ipv4", 1),
          ("mpls", 2),
          ("ipv6", 3),
          ("l2", 4))
    )


_TmnxCflowdTemplateFlowIndex_Type.__name__ = "Integer32"
_TmnxCflowdTemplateFlowIndex_Object = MibTableColumn
tmnxCflowdTemplateFlowIndex = _TmnxCflowdTemplateFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7, 1, 1),
    _TmnxCflowdTemplateFlowIndex_Type()
)
tmnxCflowdTemplateFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateFlowIndex.setStatus("current")
_TmnxCflowdTemplateLastTxTime_Type = TimeStamp
_TmnxCflowdTemplateLastTxTime_Object = MibTableColumn
tmnxCflowdTemplateLastTxTime = _TmnxCflowdTemplateLastTxTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7, 1, 2),
    _TmnxCflowdTemplateLastTxTime_Type()
)
tmnxCflowdTemplateLastTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateLastTxTime.setStatus("current")
_TmnxCflowdTemplateSent_Type = Counter32
_TmnxCflowdTemplateSent_Object = MibTableColumn
tmnxCflowdTemplateSent = _TmnxCflowdTemplateSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7, 1, 3),
    _TmnxCflowdTemplateSent_Type()
)
tmnxCflowdTemplateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateSent.setStatus("current")
_TmnxCflowdTemplateOpen_Type = Counter32
_TmnxCflowdTemplateOpen_Object = MibTableColumn
tmnxCflowdTemplateOpen = _TmnxCflowdTemplateOpen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7, 1, 4),
    _TmnxCflowdTemplateOpen_Type()
)
tmnxCflowdTemplateOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateOpen.setStatus("current")
_TmnxCflowdTemplateErrors_Type = Counter32
_TmnxCflowdTemplateErrors_Object = MibTableColumn
tmnxCflowdTemplateErrors = _TmnxCflowdTemplateErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 7, 1, 5),
    _TmnxCflowdTemplateErrors_Type()
)
tmnxCflowdTemplateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCflowdTemplateErrors.setStatus("current")
_TmnxCflowdV2Objs_ObjectIdentity = ObjectIdentity
tmnxCflowdV2Objs = _TmnxCflowdV2Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8)
)
_TmnxCflowdGeneralV2Objs_ObjectIdentity = ObjectIdentity
tmnxCflowdGeneralV2Objs = _TmnxCflowdGeneralV2Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 1)
)
_TmnxCFHostCollectorTable_Object = MibTable
tmnxCFHostCollectorTable = _TmnxCFHostCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2)
)
if mibBuilder.loadTexts:
    tmnxCFHostCollectorTable.setStatus("current")
_TmnxCFHostCollectorEntry_Object = MibTableRow
tmnxCFHostCollectorEntry = _TmnxCFHostCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1)
)
tmnxCFHostCollectorEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddressType"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollUdpPort"),
)
if mibBuilder.loadTexts:
    tmnxCFHostCollectorEntry.setStatus("current")
_TmnxCFHostCollAddressType_Type = InetAddressType
_TmnxCFHostCollAddressType_Object = MibTableColumn
tmnxCFHostCollAddressType = _TmnxCFHostCollAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 1),
    _TmnxCFHostCollAddressType_Type()
)
tmnxCFHostCollAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostCollAddressType.setStatus("current")


class _TmnxCFHostCollAddress_Type(InetAddress):
    """Custom type tmnxCFHostCollAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCFHostCollAddress_Type.__name__ = "InetAddress"
_TmnxCFHostCollAddress_Object = MibTableColumn
tmnxCFHostCollAddress = _TmnxCFHostCollAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 2),
    _TmnxCFHostCollAddress_Type()
)
tmnxCFHostCollAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostCollAddress.setStatus("current")


class _TmnxCFHostCollUdpPort_Type(Integer32):
    """Custom type tmnxCFHostCollUdpPort based on Integer32"""
    defaultValue = 2055

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxCFHostCollUdpPort_Type.__name__ = "Integer32"
_TmnxCFHostCollUdpPort_Object = MibTableColumn
tmnxCFHostCollUdpPort = _TmnxCFHostCollUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 3),
    _TmnxCFHostCollUdpPort_Type()
)
tmnxCFHostCollUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostCollUdpPort.setStatus("current")
_TmnxCFHostCollRowStatus_Type = RowStatus
_TmnxCFHostCollRowStatus_Object = MibTableColumn
tmnxCFHostCollRowStatus = _TmnxCFHostCollRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 4),
    _TmnxCFHostCollRowStatus_Type()
)
tmnxCFHostCollRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollRowStatus.setStatus("current")
_TmnxCFHostCollEntryLastChanged_Type = TimeStamp
_TmnxCFHostCollEntryLastChanged_Object = MibTableColumn
tmnxCFHostCollEntryLastChanged = _TmnxCFHostCollEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 5),
    _TmnxCFHostCollEntryLastChanged_Type()
)
tmnxCFHostCollEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollEntryLastChanged.setStatus("current")


class _TmnxCFHostCollDescription_Type(TItemDescription):
    """Custom type tmnxCFHostCollDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxCFHostCollDescription_Type.__name__ = "TItemDescription"
_TmnxCFHostCollDescription_Object = MibTableColumn
tmnxCFHostCollDescription = _TmnxCFHostCollDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 6),
    _TmnxCFHostCollDescription_Type()
)
tmnxCFHostCollDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollDescription.setStatus("current")


class _TmnxCFHostCollAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxCFHostCollAdminStatus based on TmnxAdminState"""
    defaultValue = 2


_TmnxCFHostCollAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxCFHostCollAdminStatus_Object = MibTableColumn
tmnxCFHostCollAdminStatus = _TmnxCFHostCollAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 7),
    _TmnxCFHostCollAdminStatus_Type()
)
tmnxCFHostCollAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollAdminStatus.setStatus("current")
_TmnxCFHostCollOperStatus_Type = TmnxOperState
_TmnxCFHostCollOperStatus_Object = MibTableColumn
tmnxCFHostCollOperStatus = _TmnxCFHostCollOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 8),
    _TmnxCFHostCollOperStatus_Type()
)
tmnxCFHostCollOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollOperStatus.setStatus("current")


class _TmnxCFHostCollASType_Type(Integer32):
    """Custom type tmnxCFHostCollASType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("origin", 1),
          ("peer", 2))
    )


_TmnxCFHostCollASType_Type.__name__ = "Integer32"
_TmnxCFHostCollASType_Object = MibTableColumn
tmnxCFHostCollASType = _TmnxCFHostCollASType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 9),
    _TmnxCFHostCollASType_Type()
)
tmnxCFHostCollASType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollASType.setStatus("current")


class _TmnxCFHostCollAggregation_Type(TmnxCflowdAggScheme):
    """Custom type tmnxCFHostCollAggregation based on TmnxCflowdAggScheme"""
    defaultBinValue = "0"


_TmnxCFHostCollAggregation_Type.__name__ = "TmnxCflowdAggScheme"
_TmnxCFHostCollAggregation_Object = MibTableColumn
tmnxCFHostCollAggregation = _TmnxCFHostCollAggregation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 10),
    _TmnxCFHostCollAggregation_Type()
)
tmnxCFHostCollAggregation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollAggregation.setStatus("current")
_TmnxCFHostCollRecordsSent_Type = Counter32
_TmnxCFHostCollRecordsSent_Object = MibTableColumn
tmnxCFHostCollRecordsSent = _TmnxCFHostCollRecordsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 11),
    _TmnxCFHostCollRecordsSent_Type()
)
tmnxCFHostCollRecordsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollRecordsSent.setStatus("current")
_TmnxCFHostCollLastPktSent_Type = TimeStamp
_TmnxCFHostCollLastPktSent_Object = MibTableColumn
tmnxCFHostCollLastPktSent = _TmnxCFHostCollLastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 12),
    _TmnxCFHostCollLastPktSent_Type()
)
tmnxCFHostCollLastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollLastPktSent.setStatus("current")


class _TmnxCFHostCollVersion_Type(Unsigned32):
    """Custom type tmnxCFHostCollVersion based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(8, 10),
    )


_TmnxCFHostCollVersion_Type.__name__ = "Unsigned32"
_TmnxCFHostCollVersion_Object = MibTableColumn
tmnxCFHostCollVersion = _TmnxCFHostCollVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 13),
    _TmnxCFHostCollVersion_Type()
)
tmnxCFHostCollVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollVersion.setStatus("current")


class _TmnxCFHostCollTemplateSet_Type(TmnxCflowdTemplateSet):
    """Custom type tmnxCFHostCollTemplateSet based on TmnxCflowdTemplateSet"""
    defaultValue = 0


_TmnxCFHostCollTemplateSet_Type.__name__ = "TmnxCflowdTemplateSet"
_TmnxCFHostCollTemplateSet_Object = MibTableColumn
tmnxCFHostCollTemplateSet = _TmnxCFHostCollTemplateSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 14),
    _TmnxCFHostCollTemplateSet_Type()
)
tmnxCFHostCollTemplateSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplateSet.setStatus("current")
_TmnxCFHostCollPacketsSent_Type = Counter32
_TmnxCFHostCollPacketsSent_Object = MibTableColumn
tmnxCFHostCollPacketsSent = _TmnxCFHostCollPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 2, 1, 15),
    _TmnxCFHostCollPacketsSent_Type()
)
tmnxCFHostCollPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollPacketsSent.setStatus("current")
_TmnxCFHostCollV5StatsTable_Object = MibTable
tmnxCFHostCollV5StatsTable = _TmnxCFHostCollV5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 3)
)
if mibBuilder.loadTexts:
    tmnxCFHostCollV5StatsTable.setStatus("current")
_TmnxCFHostCollV5StatsEntry_Object = MibTableRow
tmnxCFHostCollV5StatsEntry = _TmnxCFHostCollV5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 3, 1)
)
tmnxCFHostCollV5StatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddressType"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollUdpPort"),
)
if mibBuilder.loadTexts:
    tmnxCFHostCollV5StatsEntry.setStatus("current")
_TmnxCFHostCollV5SentPackets_Type = Counter32
_TmnxCFHostCollV5SentPackets_Object = MibTableColumn
tmnxCFHostCollV5SentPackets = _TmnxCFHostCollV5SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 3, 1, 1),
    _TmnxCFHostCollV5SentPackets_Type()
)
tmnxCFHostCollV5SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollV5SentPackets.setStatus("current")
_TmnxCFHostCollV5OpenPackets_Type = Counter32
_TmnxCFHostCollV5OpenPackets_Object = MibTableColumn
tmnxCFHostCollV5OpenPackets = _TmnxCFHostCollV5OpenPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 3, 1, 2),
    _TmnxCFHostCollV5OpenPackets_Type()
)
tmnxCFHostCollV5OpenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollV5OpenPackets.setStatus("current")
_TmnxCFHostCollV5ErrorPackets_Type = Counter32
_TmnxCFHostCollV5ErrorPackets_Object = MibTableColumn
tmnxCFHostCollV5ErrorPackets = _TmnxCFHostCollV5ErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 3, 1, 3),
    _TmnxCFHostCollV5ErrorPackets_Type()
)
tmnxCFHostCollV5ErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollV5ErrorPackets.setStatus("current")
_TmnxCFHostCollAggrStatsTable_Object = MibTable
tmnxCFHostCollAggrStatsTable = _TmnxCFHostCollAggrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4)
)
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrStatsTable.setStatus("current")
_TmnxCFHostCollAggrStatsEntry_Object = MibTableRow
tmnxCFHostCollAggrStatsEntry = _TmnxCFHostCollAggrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4, 1)
)
tmnxCFHostCollAggrStatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddressType"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollUdpPort"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAggrIndex"),
)
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrStatsEntry.setStatus("current")


class _TmnxCFHostCollAggrIndex_Type(Integer32):
    """Custom type tmnxCFHostCollAggrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nonAggregate", 0),
          ("asMatrix", 1),
          ("protocolPort", 2),
          ("sourcePrefix", 3),
          ("destinationPrefix", 4),
          ("sourceDestinationPrefix", 5),
          ("raw", 6))
    )


_TmnxCFHostCollAggrIndex_Type.__name__ = "Integer32"
_TmnxCFHostCollAggrIndex_Object = MibTableColumn
tmnxCFHostCollAggrIndex = _TmnxCFHostCollAggrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4, 1, 1),
    _TmnxCFHostCollAggrIndex_Type()
)
tmnxCFHostCollAggrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrIndex.setStatus("current")
_TmnxCFHostCollAggrStatus_Type = TmnxEnabledDisabled
_TmnxCFHostCollAggrStatus_Object = MibTableColumn
tmnxCFHostCollAggrStatus = _TmnxCFHostCollAggrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4, 1, 2),
    _TmnxCFHostCollAggrStatus_Type()
)
tmnxCFHostCollAggrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrStatus.setStatus("current")
_TmnxCFHostCollAggrSentPackets_Type = Counter32
_TmnxCFHostCollAggrSentPackets_Object = MibTableColumn
tmnxCFHostCollAggrSentPackets = _TmnxCFHostCollAggrSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4, 1, 3),
    _TmnxCFHostCollAggrSentPackets_Type()
)
tmnxCFHostCollAggrSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrSentPackets.setStatus("current")
_TmnxCFHostCollAggrOpenPackets_Type = Counter32
_TmnxCFHostCollAggrOpenPackets_Object = MibTableColumn
tmnxCFHostCollAggrOpenPackets = _TmnxCFHostCollAggrOpenPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4, 1, 4),
    _TmnxCFHostCollAggrOpenPackets_Type()
)
tmnxCFHostCollAggrOpenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrOpenPackets.setStatus("current")
_TmnxCFHostCollAggrErrorPackets_Type = Counter32
_TmnxCFHostCollAggrErrorPackets_Object = MibTableColumn
tmnxCFHostCollAggrErrorPackets = _TmnxCFHostCollAggrErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 4, 1, 5),
    _TmnxCFHostCollAggrErrorPackets_Type()
)
tmnxCFHostCollAggrErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollAggrErrorPackets.setStatus("current")
_TmnxCFHostCollTemplStatsTable_Object = MibTable
tmnxCFHostCollTemplStatsTable = _TmnxCFHostCollTemplStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5)
)
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplStatsTable.setStatus("current")
_TmnxCFHostCollTemplStatsEntry_Object = MibTableRow
tmnxCFHostCollTemplStatsEntry = _TmnxCFHostCollTemplStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5, 1)
)
tmnxCFHostCollTemplStatsEntry.setIndexNames(
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddressType"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAddress"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollUdpPort"),
    (0, "TIMETRA-CFLOWD-MIB", "tmnxCFHostCollTemplFlowIndex"),
)
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplStatsEntry.setStatus("current")


class _TmnxCFHostCollTemplFlowIndex_Type(Integer32):
    """Custom type tmnxCFHostCollTemplFlowIndex based on Integer32"""
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
        *(("ipv4", 1),
          ("mpls", 2),
          ("ipv6", 3),
          ("l2", 4))
    )


_TmnxCFHostCollTemplFlowIndex_Type.__name__ = "Integer32"
_TmnxCFHostCollTemplFlowIndex_Object = MibTableColumn
tmnxCFHostCollTemplFlowIndex = _TmnxCFHostCollTemplFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5, 1, 1),
    _TmnxCFHostCollTemplFlowIndex_Type()
)
tmnxCFHostCollTemplFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplFlowIndex.setStatus("current")
_TmnxCFHostCollTemplLastTxTime_Type = TimeStamp
_TmnxCFHostCollTemplLastTxTime_Object = MibTableColumn
tmnxCFHostCollTemplLastTxTime = _TmnxCFHostCollTemplLastTxTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5, 1, 2),
    _TmnxCFHostCollTemplLastTxTime_Type()
)
tmnxCFHostCollTemplLastTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplLastTxTime.setStatus("current")
_TmnxCFHostCollTemplSentPackets_Type = Counter32
_TmnxCFHostCollTemplSentPackets_Object = MibTableColumn
tmnxCFHostCollTemplSentPackets = _TmnxCFHostCollTemplSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5, 1, 3),
    _TmnxCFHostCollTemplSentPackets_Type()
)
tmnxCFHostCollTemplSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplSentPackets.setStatus("current")
_TmnxCFHostCollTemplOpenPackets_Type = Counter32
_TmnxCFHostCollTemplOpenPackets_Object = MibTableColumn
tmnxCFHostCollTemplOpenPackets = _TmnxCFHostCollTemplOpenPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5, 1, 4),
    _TmnxCFHostCollTemplOpenPackets_Type()
)
tmnxCFHostCollTemplOpenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplOpenPackets.setStatus("current")
_TmnxCFHostCollTemplErrorPackets_Type = Counter32
_TmnxCFHostCollTemplErrorPackets_Object = MibTableColumn
tmnxCFHostCollTemplErrorPackets = _TmnxCFHostCollTemplErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 19, 8, 5, 1, 5),
    _TmnxCFHostCollTemplErrorPackets_Type()
)
tmnxCFHostCollTemplErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCFHostCollTemplErrorPackets.setStatus("current")
_TmnxCflowdNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxCflowdNotificationsPrefix = _TmnxCflowdNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19)
)
_TmnxCflowdNotifications_ObjectIdentity = ObjectIdentity
tmnxCflowdNotifications = _TmnxCflowdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0)
)

# Managed Objects groups

tmnxCflowdGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 1)
)
tmnxCflowdGlobalGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdActiveTimeout"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdInactiveTimeout"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdCacheSize"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdSampleRate"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdOverflow"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdAdminStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdOperStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdActiveFlows"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdAggregation"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdMaxCollectors"))
)
if mibBuilder.loadTexts:
    tmnxCflowdGlobalGroup.setStatus("current")

tmnxCflowdHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 2)
)
tmnxCflowdHostGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCFHostTableLastChanged"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostRowStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostEntryLastChanged"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostDescription"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostAdminStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostOperStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostASType"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostAggregation"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostRecordsSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostLastPktSent"))
)
if mibBuilder.loadTexts:
    tmnxCflowdHostGroup.setStatus("current")

tmnxCflowdNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 3)
)
tmnxCflowdNotifyObjsGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowUnsuppIPProtoNum"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowFailureReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxCflowdNotifyObjsGroup.setStatus("obsolete")

tmnxCflowdGlobalGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 5)
)
tmnxCflowdGlobalGroupV6v0.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdTotalPktsRcvd"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdTotalPktsDropped"))
)
if mibBuilder.loadTexts:
    tmnxCflowdGlobalGroupV6v0.setStatus("current")

tmnxCflowdObsoleteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 6)
)
tmnxCflowdObsoleteV8v0Group.setObjects(
    ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowUnsuppIPProtoNum")
)
if mibBuilder.loadTexts:
    tmnxCflowdObsoleteV8v0Group.setStatus("current")

tmnxCflowdGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 7)
)
tmnxCflowdGroupV8v0.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdTemplateRetransmit"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdTemplateLastTxTime"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostVersion"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostTemplateSet"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostPacketsSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdVersionStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdVersionSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdVersionOpen"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdVersionErrors"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV5Sent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV5Open"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV5Errors"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdAggregationStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdAggregationSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdAggregationOpen"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdAggregationErrors"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdTemplateSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdTemplateOpen"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdTemplateErrors"))
)
if mibBuilder.loadTexts:
    tmnxCflowdGroupV8v0.setStatus("current")

tmnxCflowdNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 8)
)
tmnxCflowdNotifyObjsV8v0Group.setObjects(
    ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowFailureReasonCode")
)
if mibBuilder.loadTexts:
    tmnxCflowdNotifyObjsV8v0Group.setStatus("current")

tmnxCflowdStatisticsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 10)
)
tmnxCflowdStatisticsV10v0Group.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenRawFlowsCreated"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenAggrFlowsCreated"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenRawFlowsMatched"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenAggrFlowsMatched"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenRawFlowsFlushed"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenAggrFlowsFlushed"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenOverflowEvents"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGenDroppedFlows"))
)
if mibBuilder.loadTexts:
    tmnxCflowdStatisticsV10v0Group.setStatus("current")

tmnxCflowdV2HostCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 11, 1)
)
tmnxCflowdV2HostCfgGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollRowStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollEntryLastChanged"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollDescription"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAdminStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollOperStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollASType"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAggregation"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollRecordsSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollLastPktSent"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollVersion"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollTemplateSet"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollPacketsSent"))
)
if mibBuilder.loadTexts:
    tmnxCflowdV2HostCfgGroup.setStatus("current")

tmnxCflowdV2HostStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 11, 2)
)
tmnxCflowdV2HostStatisticsGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollV5SentPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollV5OpenPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollV5ErrorPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAggrStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAggrSentPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAggrOpenPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollAggrErrorPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollTemplLastTxTime"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollTemplSentPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollTemplOpenPackets"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollTemplErrorPackets"))
)
if mibBuilder.loadTexts:
    tmnxCflowdV2HostStatisticsGroup.setStatus("current")

tmnxCflowdExportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 12)
)
tmnxCflowdExportGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdExportMode"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdExportManual"))
)
if mibBuilder.loadTexts:
    tmnxCflowdExportGroup.setStatus("current")


# Notification objects

tmnxCflowdCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 1)
)
if mibBuilder.loadTexts:
    tmnxCflowdCreated.setStatus(
        "obsolete"
    )

tmnxCflowdCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 2)
)
if mibBuilder.loadTexts:
    tmnxCflowdCreateFailure.setStatus(
        "current"
    )

tmnxCflowdDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 3)
)
if mibBuilder.loadTexts:
    tmnxCflowdDeleted.setStatus(
        "obsolete"
    )

tmnxCflowdStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 4)
)
tmnxCflowdStateChange.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdAdminStatus"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxCflowdStateChange.setStatus(
        "current"
    )

tmnxCflowdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 5)
)
if mibBuilder.loadTexts:
    tmnxCflowdCleared.setStatus(
        "obsolete"
    )

tmnxCflowdFlowCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 6)
)
tmnxCflowdFlowCreateFailure.setObjects(
    ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowFailureReasonCode")
)
if mibBuilder.loadTexts:
    tmnxCflowdFlowCreateFailure.setStatus(
        "current"
    )

tmnxCflowdFlowFlushFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 7)
)
tmnxCflowdFlowFlushFailure.setObjects(
    ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowFailureReasonCode")
)
if mibBuilder.loadTexts:
    tmnxCflowdFlowFlushFailure.setStatus(
        "obsolete"
    )

tmnxCflowdFlowUnsuppProto = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 8)
)
tmnxCflowdFlowUnsuppProto.setObjects(
    ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowUnsuppIPProtoNum")
)
if mibBuilder.loadTexts:
    tmnxCflowdFlowUnsuppProto.setStatus(
        "obsolete"
    )

tmnxCflowdPacketTxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 19, 0, 9)
)
tmnxCflowdPacketTxFailure.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCFHostCollVersion"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowFailureReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxCflowdPacketTxFailure.setStatus(
        "current"
    )


# Notifications groups

tmnxCflowdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 4)
)
tmnxCflowdNotificationGroup.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdCreated"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdCreateFailure"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdDeleted"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdStateChange"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdCleared"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowCreateFailure"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowFlushFailure"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowUnsuppProto"))
)
if mibBuilder.loadTexts:
    tmnxCflowdNotificationGroup.setStatus(
        "obsolete"
    )

tmnxCflowdNotificationV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 2, 9)
)
tmnxCflowdNotificationV8v0Group.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdCreateFailure"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdStateChange"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdFlowCreateFailure"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdPacketTxFailure"))
)
if mibBuilder.loadTexts:
    tmnxCflowdNotificationV8v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxCflowdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 1, 1)
)
tmnxCflowdCompliance.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdHostGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxCflowdCompliance.setStatus(
        "obsolete"
    )

tmnxCflowdComplianceV6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 1, 2)
)
tmnxCflowdComplianceV6v0.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdHostGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdNotificationGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroupV6v0"))
)
if mibBuilder.loadTexts:
    tmnxCflowdComplianceV6v0.setStatus(
        "obsolete"
    )

tmnxCflowdComplianceV8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 1, 3)
)
tmnxCflowdComplianceV8v0.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroupV6v0"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdHostGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdNotificationV8v0Group"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGroupV8v0"))
)
if mibBuilder.loadTexts:
    tmnxCflowdComplianceV8v0.setStatus(
        "obsolete"
    )

tmnxCflowdComplianceV10v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 1, 4)
)
tmnxCflowdComplianceV10v0.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroupV6v0"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdHostGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdNotificationV8v0Group"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGroupV8v0"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdStatisticsV10v0Group"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV2HostCfgGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV2HostStatisticsGroup"))
)
if mibBuilder.loadTexts:
    tmnxCflowdComplianceV10v0.setStatus(
        "obsolete"
    )

tmnxCflowdComplianceV12v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 19, 1, 5)
)
tmnxCflowdComplianceV12v0.setObjects(
      *(("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGlobalGroupV6v0"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdHostGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdNotificationV8v0Group"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdGroupV8v0"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdStatisticsV10v0Group"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV2HostCfgGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdV2HostStatisticsGroup"),
        ("TIMETRA-CFLOWD-MIB", "tmnxCflowdExportGroup"))
)
if mibBuilder.loadTexts:
    tmnxCflowdComplianceV12v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CFLOWD-MIB",
    **{"TmnxCflowdAggScheme": TmnxCflowdAggScheme,
       "TmnxCflowdTemplateSet": TmnxCflowdTemplateSet,
       "timetraCflowdMIBModule": timetraCflowdMIBModule,
       "tmnxCflowdConformance": tmnxCflowdConformance,
       "tmnxCflowdCompliances": tmnxCflowdCompliances,
       "tmnxCflowdCompliance": tmnxCflowdCompliance,
       "tmnxCflowdComplianceV6v0": tmnxCflowdComplianceV6v0,
       "tmnxCflowdComplianceV8v0": tmnxCflowdComplianceV8v0,
       "tmnxCflowdComplianceV10v0": tmnxCflowdComplianceV10v0,
       "tmnxCflowdComplianceV12v0": tmnxCflowdComplianceV12v0,
       "tmnxCflowdGroups": tmnxCflowdGroups,
       "tmnxCflowdGlobalGroup": tmnxCflowdGlobalGroup,
       "tmnxCflowdHostGroup": tmnxCflowdHostGroup,
       "tmnxCflowdNotifyObjsGroup": tmnxCflowdNotifyObjsGroup,
       "tmnxCflowdNotificationGroup": tmnxCflowdNotificationGroup,
       "tmnxCflowdGlobalGroupV6v0": tmnxCflowdGlobalGroupV6v0,
       "tmnxCflowdObsoleteV8v0Group": tmnxCflowdObsoleteV8v0Group,
       "tmnxCflowdGroupV8v0": tmnxCflowdGroupV8v0,
       "tmnxCflowdNotifyObjsV8v0Group": tmnxCflowdNotifyObjsV8v0Group,
       "tmnxCflowdNotificationV8v0Group": tmnxCflowdNotificationV8v0Group,
       "tmnxCflowdStatisticsV10v0Group": tmnxCflowdStatisticsV10v0Group,
       "tmnxCflowdV10v0Groups": tmnxCflowdV10v0Groups,
       "tmnxCflowdV2HostCfgGroup": tmnxCflowdV2HostCfgGroup,
       "tmnxCflowdV2HostStatisticsGroup": tmnxCflowdV2HostStatisticsGroup,
       "tmnxCflowdExportGroup": tmnxCflowdExportGroup,
       "tmnxCflowdObjs": tmnxCflowdObjs,
       "tmnxCflowdGeneralObjs": tmnxCflowdGeneralObjs,
       "tmnxCflowdStatus": tmnxCflowdStatus,
       "tmnxCflowdActiveTimeout": tmnxCflowdActiveTimeout,
       "tmnxCflowdInactiveTimeout": tmnxCflowdInactiveTimeout,
       "tmnxCflowdCacheSize": tmnxCflowdCacheSize,
       "tmnxCflowdSampleRate": tmnxCflowdSampleRate,
       "tmnxCflowdOverflow": tmnxCflowdOverflow,
       "tmnxCflowdAdminStatus": tmnxCflowdAdminStatus,
       "tmnxCflowdOperStatus": tmnxCflowdOperStatus,
       "tmnxCflowdActiveFlows": tmnxCflowdActiveFlows,
       "tmnxCflowdAggregation": tmnxCflowdAggregation,
       "tmnxCFHostTableLastChanged": tmnxCFHostTableLastChanged,
       "tmnxCflowdMaxCollectors": tmnxCflowdMaxCollectors,
       "tmnxCflowdTotalPktsRcvd": tmnxCflowdTotalPktsRcvd,
       "tmnxCflowdTotalPktsDropped": tmnxCflowdTotalPktsDropped,
       "tmnxCflowdTemplateRetransmit": tmnxCflowdTemplateRetransmit,
       "tmnxCflowdGeneralStatisticsObjs": tmnxCflowdGeneralStatisticsObjs,
       "tmnxCflowdGenRawFlowsCreated": tmnxCflowdGenRawFlowsCreated,
       "tmnxCflowdGenAggrFlowsCreated": tmnxCflowdGenAggrFlowsCreated,
       "tmnxCflowdGenRawFlowsMatched": tmnxCflowdGenRawFlowsMatched,
       "tmnxCflowdGenAggrFlowsMatched": tmnxCflowdGenAggrFlowsMatched,
       "tmnxCflowdGenRawFlowsFlushed": tmnxCflowdGenRawFlowsFlushed,
       "tmnxCflowdGenAggrFlowsFlushed": tmnxCflowdGenAggrFlowsFlushed,
       "tmnxCflowdGenOverflowEvents": tmnxCflowdGenOverflowEvents,
       "tmnxCflowdGenDroppedFlows": tmnxCflowdGenDroppedFlows,
       "tmnxCflowdExportMode": tmnxCflowdExportMode,
       "tmnxCflowdExportManual": tmnxCflowdExportManual,
       "tmnxCflowdNotificationObjects": tmnxCflowdNotificationObjects,
       "tmnxCflowdFlowFailureReasonCode": tmnxCflowdFlowFailureReasonCode,
       "tmnxCflowdFlowUnsuppIPProtoNum": tmnxCflowdFlowUnsuppIPProtoNum,
       "tmnxCFHostTable": tmnxCFHostTable,
       "tmnxCFHostEntry": tmnxCFHostEntry,
       "tmnxCFHostAddress": tmnxCFHostAddress,
       "tmnxCFHostUdpPort": tmnxCFHostUdpPort,
       "tmnxCFHostRowStatus": tmnxCFHostRowStatus,
       "tmnxCFHostEntryLastChanged": tmnxCFHostEntryLastChanged,
       "tmnxCFHostDescription": tmnxCFHostDescription,
       "tmnxCFHostAdminStatus": tmnxCFHostAdminStatus,
       "tmnxCFHostOperStatus": tmnxCFHostOperStatus,
       "tmnxCFHostASType": tmnxCFHostASType,
       "tmnxCFHostAggregation": tmnxCFHostAggregation,
       "tmnxCFHostRecordsSent": tmnxCFHostRecordsSent,
       "tmnxCFHostLastPktSent": tmnxCFHostLastPktSent,
       "tmnxCFHostVersion": tmnxCFHostVersion,
       "tmnxCFHostTemplateSet": tmnxCFHostTemplateSet,
       "tmnxCFHostPacketsSent": tmnxCFHostPacketsSent,
       "tmnxCflowdVersionStatsTable": tmnxCflowdVersionStatsTable,
       "tmnxCflowdVersionStatsEntry": tmnxCflowdVersionStatsEntry,
       "tmnxCflowdVersionIndex": tmnxCflowdVersionIndex,
       "tmnxCflowdVersionStatus": tmnxCflowdVersionStatus,
       "tmnxCflowdVersionSent": tmnxCflowdVersionSent,
       "tmnxCflowdVersionOpen": tmnxCflowdVersionOpen,
       "tmnxCflowdVersionErrors": tmnxCflowdVersionErrors,
       "tmnxCflowdV5StatsTable": tmnxCflowdV5StatsTable,
       "tmnxCflowdV5StatsEntry": tmnxCflowdV5StatsEntry,
       "tmnxCflowdV5Sent": tmnxCflowdV5Sent,
       "tmnxCflowdV5Open": tmnxCflowdV5Open,
       "tmnxCflowdV5Errors": tmnxCflowdV5Errors,
       "tmnxCflowdAggregationStatsTable": tmnxCflowdAggregationStatsTable,
       "tmnxCflowdAggregationStatsEntry": tmnxCflowdAggregationStatsEntry,
       "tmnxCflowdAggregationIndex": tmnxCflowdAggregationIndex,
       "tmnxCflowdAggregationStatus": tmnxCflowdAggregationStatus,
       "tmnxCflowdAggregationSent": tmnxCflowdAggregationSent,
       "tmnxCflowdAggregationOpen": tmnxCflowdAggregationOpen,
       "tmnxCflowdAggregationErrors": tmnxCflowdAggregationErrors,
       "tmnxCflowdTemplateStatsTable": tmnxCflowdTemplateStatsTable,
       "tmnxCflowdTemplateStatsEntry": tmnxCflowdTemplateStatsEntry,
       "tmnxCflowdTemplateFlowIndex": tmnxCflowdTemplateFlowIndex,
       "tmnxCflowdTemplateLastTxTime": tmnxCflowdTemplateLastTxTime,
       "tmnxCflowdTemplateSent": tmnxCflowdTemplateSent,
       "tmnxCflowdTemplateOpen": tmnxCflowdTemplateOpen,
       "tmnxCflowdTemplateErrors": tmnxCflowdTemplateErrors,
       "tmnxCflowdV2Objs": tmnxCflowdV2Objs,
       "tmnxCflowdGeneralV2Objs": tmnxCflowdGeneralV2Objs,
       "tmnxCFHostCollectorTable": tmnxCFHostCollectorTable,
       "tmnxCFHostCollectorEntry": tmnxCFHostCollectorEntry,
       "tmnxCFHostCollAddressType": tmnxCFHostCollAddressType,
       "tmnxCFHostCollAddress": tmnxCFHostCollAddress,
       "tmnxCFHostCollUdpPort": tmnxCFHostCollUdpPort,
       "tmnxCFHostCollRowStatus": tmnxCFHostCollRowStatus,
       "tmnxCFHostCollEntryLastChanged": tmnxCFHostCollEntryLastChanged,
       "tmnxCFHostCollDescription": tmnxCFHostCollDescription,
       "tmnxCFHostCollAdminStatus": tmnxCFHostCollAdminStatus,
       "tmnxCFHostCollOperStatus": tmnxCFHostCollOperStatus,
       "tmnxCFHostCollASType": tmnxCFHostCollASType,
       "tmnxCFHostCollAggregation": tmnxCFHostCollAggregation,
       "tmnxCFHostCollRecordsSent": tmnxCFHostCollRecordsSent,
       "tmnxCFHostCollLastPktSent": tmnxCFHostCollLastPktSent,
       "tmnxCFHostCollVersion": tmnxCFHostCollVersion,
       "tmnxCFHostCollTemplateSet": tmnxCFHostCollTemplateSet,
       "tmnxCFHostCollPacketsSent": tmnxCFHostCollPacketsSent,
       "tmnxCFHostCollV5StatsTable": tmnxCFHostCollV5StatsTable,
       "tmnxCFHostCollV5StatsEntry": tmnxCFHostCollV5StatsEntry,
       "tmnxCFHostCollV5SentPackets": tmnxCFHostCollV5SentPackets,
       "tmnxCFHostCollV5OpenPackets": tmnxCFHostCollV5OpenPackets,
       "tmnxCFHostCollV5ErrorPackets": tmnxCFHostCollV5ErrorPackets,
       "tmnxCFHostCollAggrStatsTable": tmnxCFHostCollAggrStatsTable,
       "tmnxCFHostCollAggrStatsEntry": tmnxCFHostCollAggrStatsEntry,
       "tmnxCFHostCollAggrIndex": tmnxCFHostCollAggrIndex,
       "tmnxCFHostCollAggrStatus": tmnxCFHostCollAggrStatus,
       "tmnxCFHostCollAggrSentPackets": tmnxCFHostCollAggrSentPackets,
       "tmnxCFHostCollAggrOpenPackets": tmnxCFHostCollAggrOpenPackets,
       "tmnxCFHostCollAggrErrorPackets": tmnxCFHostCollAggrErrorPackets,
       "tmnxCFHostCollTemplStatsTable": tmnxCFHostCollTemplStatsTable,
       "tmnxCFHostCollTemplStatsEntry": tmnxCFHostCollTemplStatsEntry,
       "tmnxCFHostCollTemplFlowIndex": tmnxCFHostCollTemplFlowIndex,
       "tmnxCFHostCollTemplLastTxTime": tmnxCFHostCollTemplLastTxTime,
       "tmnxCFHostCollTemplSentPackets": tmnxCFHostCollTemplSentPackets,
       "tmnxCFHostCollTemplOpenPackets": tmnxCFHostCollTemplOpenPackets,
       "tmnxCFHostCollTemplErrorPackets": tmnxCFHostCollTemplErrorPackets,
       "tmnxCflowdNotificationsPrefix": tmnxCflowdNotificationsPrefix,
       "tmnxCflowdNotifications": tmnxCflowdNotifications,
       "tmnxCflowdCreated": tmnxCflowdCreated,
       "tmnxCflowdCreateFailure": tmnxCflowdCreateFailure,
       "tmnxCflowdDeleted": tmnxCflowdDeleted,
       "tmnxCflowdStateChange": tmnxCflowdStateChange,
       "tmnxCflowdCleared": tmnxCflowdCleared,
       "tmnxCflowdFlowCreateFailure": tmnxCflowdFlowCreateFailure,
       "tmnxCflowdFlowFlushFailure": tmnxCflowdFlowFlushFailure,
       "tmnxCflowdFlowUnsuppProto": tmnxCflowdFlowUnsuppProto,
       "tmnxCflowdPacketTxFailure": tmnxCflowdPacketTxFailure}
)
