# SNMP MIB module (SCTE-HMS-HEADENDIDENT-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HEADENDIDENT-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:32:18 2025
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

hmsTextualConventionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VideoInputFrameRateType(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("autoSelect", 2),
          ("f24Hz", 3),
          ("f25Hz", 4),
          ("f29Hz97", 5),
          ("f30Hz", 6),
          ("f29or30Hz", 7),
          ("f48Hz", 8),
          ("f50Hz", 9),
          ("f59Hz94", 10),
          ("f60Hz", 11),
          ("f59or60Hz", 12))
    )



class QAMChannelModulationFormat(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("qam64", 3),
          ("qam256", 4),
          ("qam128", 5),
          ("qam512", 6),
          ("qam1024", 7))
    )



class QAMChannelInterleaveMode(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("fecI8J16", 3),
          ("fecI16J8", 4),
          ("fecI32J4", 5),
          ("fecI64J2", 6),
          ("fecI128J1", 7),
          ("fecI12J17", 8),
          ("fecI128J2", 9),
          ("fecI128J3", 10),
          ("fecI128J4", 11),
          ("fecI128J5", 12),
          ("fecI128J6", 13),
          ("fecI128J7", 14),
          ("fecI128J8", 15))
    )



class ProgDataType(TextualConvention, Integer32):
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
        *(("video", 1),
          ("audio", 2),
          ("data", 3),
          ("other", 4))
    )



class DeviceEnableDisableValues(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("enabled", 2),
          ("notSupported", 3))
    )



class MpegErrorStatus(TextualConvention, Integer32):
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
        *(("good", 1),
          ("errors", 2),
          ("notSupported", 3))
    )



class HePIDValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
        ValueRangeConstraint(65535, 65535),
    )



class HeClockSource(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("other", 2),
          ("internal", 3),
          ("external", 4),
          ("ntp", 5),
          ("none", 6))
    )



class HeResetValue(TextualConvention, Integer32):
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
        *(("reset", 1),
          ("running", 2),
          ("resetting", 3))
    )



class HeTenthVolt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeTenthdBm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeTenthdBmV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeTenthCentigrade(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeHundredthNanoMeter(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class HeTenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeOnOffControl(TextualConvention, Integer32):
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
        *(("off", 1),
          ("on", 2),
          ("meaningless", 3))
    )



class HeOnOffStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class HeAlarmControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmEnabled", 1),
          ("alarmDisabled", 2))
    )



class HeTrapRegenerate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapRegenerate", 1),
          ("trapNormal", 2))
    )



class HeDigitalAlarmSeverity(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("status", 5),
          ("clear", 6),
          ("information", 7))
    )



class HeDigitalAlarmType(TextualConvention, Integer32):
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
        *(("communication", 1),
          ("process", 2),
          ("session", 3),
          ("capacity", 4),
          ("maintenance", 5),
          ("provisioning", 6),
          ("programMgmt", 7),
          ("redundancy", 8),
          ("other", 9))
    )



class HeFaultStatus(TextualConvention, Integer32):
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
          ("fault", 2))
    )



class HeMilliAmp(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-3"


class HeHundredthWatts(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    **{"VideoInputFrameRateType": VideoInputFrameRateType,
       "QAMChannelModulationFormat": QAMChannelModulationFormat,
       "QAMChannelInterleaveMode": QAMChannelInterleaveMode,
       "ProgDataType": ProgDataType,
       "DeviceEnableDisableValues": DeviceEnableDisableValues,
       "MpegErrorStatus": MpegErrorStatus,
       "HePIDValue": HePIDValue,
       "HeClockSource": HeClockSource,
       "HeResetValue": HeResetValue,
       "HeTenthVolt": HeTenthVolt,
       "HeTenthdBm": HeTenthdBm,
       "HeTenthdBmV": HeTenthdBmV,
       "HeTenthCentigrade": HeTenthCentigrade,
       "HeHundredthNanoMeter": HeHundredthNanoMeter,
       "HeTenthdB": HeTenthdB,
       "HeOnOffControl": HeOnOffControl,
       "HeOnOffStatus": HeOnOffStatus,
       "HeAlarmControl": HeAlarmControl,
       "HeTrapRegenerate": HeTrapRegenerate,
       "HeDigitalAlarmSeverity": HeDigitalAlarmSeverity,
       "HeDigitalAlarmType": HeDigitalAlarmType,
       "HeFaultStatus": HeFaultStatus,
       "HeMilliAmp": HeMilliAmp,
       "HeHundredthWatts": HeHundredthWatts,
       "hmsTextualConventionMIB": hmsTextualConventionMIB}
)
