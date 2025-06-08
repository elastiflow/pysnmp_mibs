# SNMP MIB module (IANA-IPPM-METRICS-REGISTRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IANA-IPPM-METRICS-REGISTRY-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:35:45 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaIppmMetricsRegistry = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 128)
)
if mibBuilder.loadTexts:
    ianaIppmMetricsRegistry.setRevisions(
        ("2005-07-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IanaIppmMetrics_ObjectIdentity = ObjectIdentity
ianaIppmMetrics = _IanaIppmMetrics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1)
)
if mibBuilder.loadTexts:
    ianaIppmMetrics.setStatus("current")
_IetfInstantUnidirConnectivity_ObjectIdentity = ObjectIdentity
ietfInstantUnidirConnectivity = _IetfInstantUnidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 1)
)
if mibBuilder.loadTexts:
    ietfInstantUnidirConnectivity.setStatus("current")
_IetfInstantBidirConnectivity_ObjectIdentity = ObjectIdentity
ietfInstantBidirConnectivity = _IetfInstantBidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 2)
)
if mibBuilder.loadTexts:
    ietfInstantBidirConnectivity.setStatus("current")
_IetfIntervalUnidirConnectivity_ObjectIdentity = ObjectIdentity
ietfIntervalUnidirConnectivity = _IetfIntervalUnidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 3)
)
if mibBuilder.loadTexts:
    ietfIntervalUnidirConnectivity.setStatus("current")
_IetfIntervalBidirConnectivity_ObjectIdentity = ObjectIdentity
ietfIntervalBidirConnectivity = _IetfIntervalBidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 4)
)
if mibBuilder.loadTexts:
    ietfIntervalBidirConnectivity.setStatus("current")
_IetfIntervalTemporalConnectivity_ObjectIdentity = ObjectIdentity
ietfIntervalTemporalConnectivity = _IetfIntervalTemporalConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 5)
)
if mibBuilder.loadTexts:
    ietfIntervalTemporalConnectivity.setStatus("current")
_IetfOneWayDelay_ObjectIdentity = ObjectIdentity
ietfOneWayDelay = _IetfOneWayDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 6)
)
if mibBuilder.loadTexts:
    ietfOneWayDelay.setStatus("current")
_IetfOneWayDelayPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayDelayPoissonStream = _IetfOneWayDelayPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 7)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayPoissonStream.setStatus("current")
_IetfOneWayDelayPercentile_ObjectIdentity = ObjectIdentity
ietfOneWayDelayPercentile = _IetfOneWayDelayPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 8)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayPercentile.setStatus("current")
_IetfOneWayDelayMedian_ObjectIdentity = ObjectIdentity
ietfOneWayDelayMedian = _IetfOneWayDelayMedian_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 9)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayMedian.setStatus("current")
_IetfOneWayDelayMinimum_ObjectIdentity = ObjectIdentity
ietfOneWayDelayMinimum = _IetfOneWayDelayMinimum_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 10)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayMinimum.setStatus("current")
_IetfOneWayDelayInversePercentile_ObjectIdentity = ObjectIdentity
ietfOneWayDelayInversePercentile = _IetfOneWayDelayInversePercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 11)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayInversePercentile.setStatus("current")
_IetfOneWayPktLoss_ObjectIdentity = ObjectIdentity
ietfOneWayPktLoss = _IetfOneWayPktLoss_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 12)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLoss.setStatus("current")
_IetfOneWayPktLossPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayPktLossPoissonStream = _IetfOneWayPktLossPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 13)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLossPoissonStream.setStatus("current")
_IetfOneWayPktLossAverage_ObjectIdentity = ObjectIdentity
ietfOneWayPktLossAverage = _IetfOneWayPktLossAverage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 14)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLossAverage.setStatus("current")
_IetfRoundTripDelay_ObjectIdentity = ObjectIdentity
ietfRoundTripDelay = _IetfRoundTripDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 15)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelay.setStatus("current")
_IetfRoundTripDelayPoissonStream_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayPoissonStream = _IetfRoundTripDelayPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 16)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayPoissonStream.setStatus("current")
_IetfRoundTripDelayPercentile_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayPercentile = _IetfRoundTripDelayPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 17)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayPercentile.setStatus("current")
_IetfRoundTripDelayMedian_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayMedian = _IetfRoundTripDelayMedian_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 18)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayMedian.setStatus("current")
_IetfRoundTripDelayMinimum_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayMinimum = _IetfRoundTripDelayMinimum_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 19)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayMinimum.setStatus("current")
_IetfRoundTripDelayInvPercentile_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayInvPercentile = _IetfRoundTripDelayInvPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 20)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayInvPercentile.setStatus("current")
_IetfOneWayLossDistanceStream_ObjectIdentity = ObjectIdentity
ietfOneWayLossDistanceStream = _IetfOneWayLossDistanceStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 21)
)
if mibBuilder.loadTexts:
    ietfOneWayLossDistanceStream.setStatus("current")
_IetfOneWayLossPeriodStream_ObjectIdentity = ObjectIdentity
ietfOneWayLossPeriodStream = _IetfOneWayLossPeriodStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 22)
)
if mibBuilder.loadTexts:
    ietfOneWayLossPeriodStream.setStatus("current")
_IetfOneWayLossNoticeableRate_ObjectIdentity = ObjectIdentity
ietfOneWayLossNoticeableRate = _IetfOneWayLossNoticeableRate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 23)
)
if mibBuilder.loadTexts:
    ietfOneWayLossNoticeableRate.setStatus("current")
_IetfOneWayLossPeriodTotal_ObjectIdentity = ObjectIdentity
ietfOneWayLossPeriodTotal = _IetfOneWayLossPeriodTotal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 24)
)
if mibBuilder.loadTexts:
    ietfOneWayLossPeriodTotal.setStatus("current")
_IetfOneWayLossPeriodLengths_ObjectIdentity = ObjectIdentity
ietfOneWayLossPeriodLengths = _IetfOneWayLossPeriodLengths_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 25)
)
if mibBuilder.loadTexts:
    ietfOneWayLossPeriodLengths.setStatus("current")
_IetfOneWayInterLossPeriodLengths_ObjectIdentity = ObjectIdentity
ietfOneWayInterLossPeriodLengths = _IetfOneWayInterLossPeriodLengths_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 26)
)
if mibBuilder.loadTexts:
    ietfOneWayInterLossPeriodLengths.setStatus("current")
_IetfOneWayIpdv_ObjectIdentity = ObjectIdentity
ietfOneWayIpdv = _IetfOneWayIpdv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 27)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdv.setStatus("current")
_IetfOneWayIpdvPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvPoissonStream = _IetfOneWayIpdvPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 28)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvPoissonStream.setStatus("current")
_IetfOneWayIpdvPercentile_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvPercentile = _IetfOneWayIpdvPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 29)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvPercentile.setStatus("current")
_IetfOneWayIpdvInversePercentile_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvInversePercentile = _IetfOneWayIpdvInversePercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 30)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvInversePercentile.setStatus("current")
_IetfOneWayIpdvJitter_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvJitter = _IetfOneWayIpdvJitter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 31)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvJitter.setStatus("current")
_IetfOneWayPeakToPeakIpdv_ObjectIdentity = ObjectIdentity
ietfOneWayPeakToPeakIpdv = _IetfOneWayPeakToPeakIpdv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 32)
)
if mibBuilder.loadTexts:
    ietfOneWayPeakToPeakIpdv.setStatus("current")
_IetfOneWayDelayPeriodicStream_ObjectIdentity = ObjectIdentity
ietfOneWayDelayPeriodicStream = _IetfOneWayDelayPeriodicStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 33)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayPeriodicStream.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-IPPM-METRICS-REGISTRY-MIB",
    **{"ianaIppmMetricsRegistry": ianaIppmMetricsRegistry,
       "ianaIppmMetrics": ianaIppmMetrics,
       "ietfInstantUnidirConnectivity": ietfInstantUnidirConnectivity,
       "ietfInstantBidirConnectivity": ietfInstantBidirConnectivity,
       "ietfIntervalUnidirConnectivity": ietfIntervalUnidirConnectivity,
       "ietfIntervalBidirConnectivity": ietfIntervalBidirConnectivity,
       "ietfIntervalTemporalConnectivity": ietfIntervalTemporalConnectivity,
       "ietfOneWayDelay": ietfOneWayDelay,
       "ietfOneWayDelayPoissonStream": ietfOneWayDelayPoissonStream,
       "ietfOneWayDelayPercentile": ietfOneWayDelayPercentile,
       "ietfOneWayDelayMedian": ietfOneWayDelayMedian,
       "ietfOneWayDelayMinimum": ietfOneWayDelayMinimum,
       "ietfOneWayDelayInversePercentile": ietfOneWayDelayInversePercentile,
       "ietfOneWayPktLoss": ietfOneWayPktLoss,
       "ietfOneWayPktLossPoissonStream": ietfOneWayPktLossPoissonStream,
       "ietfOneWayPktLossAverage": ietfOneWayPktLossAverage,
       "ietfRoundTripDelay": ietfRoundTripDelay,
       "ietfRoundTripDelayPoissonStream": ietfRoundTripDelayPoissonStream,
       "ietfRoundTripDelayPercentile": ietfRoundTripDelayPercentile,
       "ietfRoundTripDelayMedian": ietfRoundTripDelayMedian,
       "ietfRoundTripDelayMinimum": ietfRoundTripDelayMinimum,
       "ietfRoundTripDelayInvPercentile": ietfRoundTripDelayInvPercentile,
       "ietfOneWayLossDistanceStream": ietfOneWayLossDistanceStream,
       "ietfOneWayLossPeriodStream": ietfOneWayLossPeriodStream,
       "ietfOneWayLossNoticeableRate": ietfOneWayLossNoticeableRate,
       "ietfOneWayLossPeriodTotal": ietfOneWayLossPeriodTotal,
       "ietfOneWayLossPeriodLengths": ietfOneWayLossPeriodLengths,
       "ietfOneWayInterLossPeriodLengths": ietfOneWayInterLossPeriodLengths,
       "ietfOneWayIpdv": ietfOneWayIpdv,
       "ietfOneWayIpdvPoissonStream": ietfOneWayIpdvPoissonStream,
       "ietfOneWayIpdvPercentile": ietfOneWayIpdvPercentile,
       "ietfOneWayIpdvInversePercentile": ietfOneWayIpdvInversePercentile,
       "ietfOneWayIpdvJitter": ietfOneWayIpdvJitter,
       "ietfOneWayPeakToPeakIpdv": ietfOneWayPeakToPeakIpdv,
       "ietfOneWayDelayPeriodicStream": ietfOneWayDelayPeriodicStream}
)
