# SNMP MIB module (CISCO-WIRELESS-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WIRELESS-TC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:15 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoWirelessTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 137)
)
if mibBuilder.loadTexts:
    ciscoWirelessTextualConventions.setRevisions(
        ("2000-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CwrRFZeroIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



class CwrCwErrorFreeSecond(TextualConvention, Gauge32):
    status = "current"


class CwrCwErroredSecond(TextualConvention, Gauge32):
    status = "current"


class CwrCwSeverelyErroredSecond(TextualConvention, Gauge32):
    status = "current"


class CwrCwConsecutiveSevErrSecond(TextualConvention, Gauge32):
    status = "current"


class CwrCwDegradedSecond(TextualConvention, Gauge32):
    status = "current"


class CwrCwDegradedMinute(TextualConvention, Gauge32):
    status = "current"


class CwrCollectionAction(TextualConvention, Integer32):
    status = "current"
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
        *(("actionStop", 1),
          ("actionStart", 2),
          ("actionClear", 3),
          ("actionRestart", 4))
    )



class CwrCollectionStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("statusIdle", 1),
          ("statusInProgress", 2),
          ("statusStopped", 3),
          ("statusCaptured", 4))
    )



class CwrdBm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 33),
    )



class CwrdB(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class CwrThreshLimitType(TextualConvention, Integer32):
    status = "current"
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
        *(("upChange", 1),
          ("downChange", 2),
          ("highThresh", 3),
          ("lowThresh", 4),
          ("upLimit", 5),
          ("lowLimit", 6))
    )



class CwrRadioSignalAttribute(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("rsaIN", 1),
          ("rsaINR", 2),
          ("rsaConstellationVariance", 3),
          ("rsaTimingOffset", 4),
          ("rsaReceivedPower", 5),
          ("rsaGainSettingsIF", 6),
          ("rsaGainSettingsRF", 7),
          ("rsaFreqOffset", 8),
          ("rsaTotalGain", 9),
          ("rsaSyncStatus", 10))
    )



class CwrOscState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oscillatorOk", 1),
          ("osccillatorBad", 2))
    )



class P2mpRadioSignalAttribute(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rsaSinrMainAnt", 1),
          ("rsaSinrDiversityAnt", 2),
          ("rsaSinrRatio", 3),
          ("rsaTimingOffset", 4),
          ("rsaRxPowerMainAnt", 5),
          ("rsaRxPowerDiversityAnt", 6),
          ("rsaChDelaySpreadMainAnt", 7),
          ("rsaChDelaySpreadDiversityAnt", 8),
          ("rsaHeAmbientNoise", 9),
          ("rsaSuRxPowerDeltaMainAnt", 10),
          ("rsaSuRxPowerDeltaDiversityAnt", 11),
          ("rsaSuTotalTxPower", 12))
    )



class CwrRfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("main", 0),
          ("diversity", 1))
    )



class CwrFixedPointScale(TextualConvention, Integer32):
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
        *(("yocto", 1),
          ("zepto", 2),
          ("atto", 3),
          ("femto", 4),
          ("pico", 5),
          ("nano", 6),
          ("micro", 7),
          ("milli", 8),
          ("units", 9),
          ("kilo", 10),
          ("mega", 11),
          ("giga", 12),
          ("tera", 13),
          ("exa", 14),
          ("peta", 15),
          ("zetta", 16),
          ("yotta", 17))
    )



class CwrFixedPointPrecision(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )



class CwrFixedPointValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class P2mpSnapshotAttribute(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1



class CwrPercentageValue(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )



class CwrUpdateTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CwrRfFreqRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )



class WirelessGauge64(TextualConvention, Counter64):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-TC-MIB",
    **{"CwrRFZeroIndex": CwrRFZeroIndex,
       "CwrCwErrorFreeSecond": CwrCwErrorFreeSecond,
       "CwrCwErroredSecond": CwrCwErroredSecond,
       "CwrCwSeverelyErroredSecond": CwrCwSeverelyErroredSecond,
       "CwrCwConsecutiveSevErrSecond": CwrCwConsecutiveSevErrSecond,
       "CwrCwDegradedSecond": CwrCwDegradedSecond,
       "CwrCwDegradedMinute": CwrCwDegradedMinute,
       "CwrCollectionAction": CwrCollectionAction,
       "CwrCollectionStatus": CwrCollectionStatus,
       "CwrdBm": CwrdBm,
       "CwrdB": CwrdB,
       "CwrThreshLimitType": CwrThreshLimitType,
       "CwrRadioSignalAttribute": CwrRadioSignalAttribute,
       "CwrOscState": CwrOscState,
       "P2mpRadioSignalAttribute": P2mpRadioSignalAttribute,
       "CwrRfType": CwrRfType,
       "CwrFixedPointScale": CwrFixedPointScale,
       "CwrFixedPointPrecision": CwrFixedPointPrecision,
       "CwrFixedPointValue": CwrFixedPointValue,
       "P2mpSnapshotAttribute": P2mpSnapshotAttribute,
       "CwrPercentageValue": CwrPercentageValue,
       "CwrUpdateTime": CwrUpdateTime,
       "CwrRfFreqRange": CwrRfFreqRange,
       "WirelessGauge64": WirelessGauge64,
       "ciscoWirelessTextualConventions": ciscoWirelessTextualConventions}
)
