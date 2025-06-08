# SNMP MIB module (MEF-SOAM-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mef_15007/MEF-SOAM-TC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:23:56 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mefSoamTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamTcMib.setRevisions(
        ("2012-01-10 00:00",
         "2010-10-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MefSoamTcAvailabilityType(TextualConvention, Integer32):
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
        *(("available", 1),
          ("unavailable", 2),
          ("unknown", 3))
    )



class MefSoamTcConnectivityStatusType(TextualConvention, Integer32):
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
        *(("inactive", 1),
          ("active", 2),
          ("partiallyActive", 3))
    )



class MefSoamTcDataPatternType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("zeroPattern", 1),
          ("onesPattern", 2))
    )



class MefSoamTcDelayMeasurementBinType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("twoWayFrameDelay", 1),
          ("forwardFrameDelay", 2),
          ("backwardFrameDelay", 3),
          ("twoWayIfdv", 4),
          ("forwardIfdv", 5),
          ("backwardIfdv", 6),
          ("twoWayFrameDelayRange", 7),
          ("forwardFrameDelayRange", 8),
          ("backwardFrameDelayRange", 9))
    )



class MefSoamTcIntervalTypeAisLck(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneSecond", 1),
          ("oneMinute", 2))
    )



class MefSoamTcMeasurementPeriodType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600000),
    )



class MefSoamTcMegIdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("primaryVid", 1),
          ("charString", 2),
          ("unsignedInt16", 3),
          ("rfc2865VpnId", 4),
          ("iccBased", 32))
    )



class MefSoamTcOperationTimeType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("immediate", 2),
          ("relative", 3),
          ("fixed", 4))
    )



class MefSoamTcSessionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proactive", 1),
          ("onDemand", 2))
    )



class MefSoamTcStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )



class MefSoamTcTestPatternType(TextualConvention, Integer32):
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
        *(("null", 1),
          ("nullCrc32", 2),
          ("prbs", 3),
          ("prbsCrc32", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-SOAM-TC-MIB",
    **{"MefSoamTcAvailabilityType": MefSoamTcAvailabilityType,
       "MefSoamTcConnectivityStatusType": MefSoamTcConnectivityStatusType,
       "MefSoamTcDataPatternType": MefSoamTcDataPatternType,
       "MefSoamTcDelayMeasurementBinType": MefSoamTcDelayMeasurementBinType,
       "MefSoamTcIntervalTypeAisLck": MefSoamTcIntervalTypeAisLck,
       "MefSoamTcMeasurementPeriodType": MefSoamTcMeasurementPeriodType,
       "MefSoamTcMegIdType": MefSoamTcMegIdType,
       "MefSoamTcOperationTimeType": MefSoamTcOperationTimeType,
       "MefSoamTcSessionType": MefSoamTcSessionType,
       "MefSoamTcStatusType": MefSoamTcStatusType,
       "MefSoamTcTestPatternType": MefSoamTcTestPatternType,
       "mefSoamTcMib": mefSoamTcMib}
)
